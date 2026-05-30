"""
PAS209 — Bounded action proposal packages.

Converts each PAS208 ``Recommendation`` whose ``approval_status``
is ``APPROVED_FOR_MANUAL_REVIEW`` into a strictly bounded
``ActionProposal`` package the operator can read, copy, and
execute *manually*. PAS209 itself does **not** execute anything.
There is no Twilio call, no SMS / email send, no CRM write, no
Slack outbound, no DB mutation, no scheduler, no autonomous
action. The proposal package is a frozen value object describing
what a human could do — never an instruction the engine carries
out.

Hard safety doctrine (asserted by tests and the readiness gate):

  * Only ``APPROVAL_APPROVED_FOR_MANUAL_REVIEW`` recommendations
    yield a proposal. Every other approval state silently returns
    ``None`` — the closed-vocabulary safety net.
  * Every emitted ``ActionProposal`` carries
    ``required_human_review=True``, ``allowed_channel="MANUAL_ONLY"``,
    and ``live_behavior_changed=False``. The defaults are frozen
    and the readiness gate asserts no code path overwrites them.
  * The proposed_action_type is the SAME closed vocabulary PAS208
    uses (the ten ``draft_*`` actions). PAS209 does not introduce
    new action types.
  * The module imports nothing from the live outbound surfaces,
    LLM clients, scheduler libraries, or the engine. The readiness
    gate asserts the closed allow-list textually and via AST walk
    of the import graph.
  * proposal_id is a deterministic SHA-256 hash of
    ``(recommendation_id, proposed_action_type)`` so identical
    inputs produce identical outputs across processes.

Public surface:

  * ``ALLOWED_CHANNEL_MANUAL_ONLY``       — sole legal channel
  * ``ALLOWED_CHANNELS``                  — closed tuple
  * ``ActionProposal``                    — frozen dataclass
  * ``ActionProposalPackage``             — frozen dataclass
  * ``build_proposal(recommendation)``    — pure builder
  * ``build_proposal_package(rec_digest)``— pure batch builder
  * ``to_machine_json(pkg)``              — JSON-ready dict
  * ``to_broker_report(pkg)``             — broker-voice summary
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Counter as _Counter
from typing import Dict, List, Mapping, Optional, Tuple

from app.services.proactive.recommendations import (
    ACTION_DRAFT_AFTER_HOURS_PLAN,
    ACTION_DRAFT_AGENT_ASSIGNMENT,
    ACTION_DRAFT_ALTERNATE_CHANNEL,
    ACTION_DRAFT_BOOKING_RETRY,
    ACTION_DRAFT_CALLBACK_FOLLOWUP,
    ACTION_DRAFT_COVERAGE_SHIFT,
    ACTION_DRAFT_FIRST_CONTACT,
    ACTION_DRAFT_HUMAN_REVIEW_REQUEST,
    ACTION_DRAFT_SENIOR_AGENT_HANDOFF,
    ACTION_DRAFT_SOFT_CHECKIN,
    APPROVAL_APPROVED_FOR_MANUAL_REVIEW,
    RECOMMENDED_ACTION_TYPES,
    Recommendation,
    RecommendationDigest,
)


# ──────────────────────────────────────────────────────────────────
# Closed vocabularies.
# ──────────────────────────────────────────────────────────────────

ALLOWED_CHANNEL_MANUAL_ONLY = "MANUAL_ONLY"

ALLOWED_CHANNELS: Tuple[str, ...] = (
    ALLOWED_CHANNEL_MANUAL_ONLY,
)


# Per-action draft template: a tuple of
# (draft_message_or_instruction, safety_notes_tuple, rollback_notes_tuple).
#
# The "draft" is plain text. Nothing in this module sends it. The
# safety / rollback notes describe what the operator should check
# before they manually send anything, and how to undo it if they
# already did. The notes are intentionally short and broker-voice.

_NO_DRAFT = "No draft generated — operator should compose manually."


_PROPOSAL_TEMPLATES: Mapping[str, Tuple[str, Tuple[str, ...], Tuple[str, ...]]] = {

    ACTION_DRAFT_CALLBACK_FOLLOWUP: (
        "Hi {{lead_name|there}} — sorry we missed reaching you for the "
        "scheduled callback. Are you free for a quick call now, or would "
        "later today work better? — {{agent_name|the team}}",
        (
            "Confirm the lead consented to being contacted in this channel "
            "before sending.",
            "Confirm the callback was actually missed; do not send if a "
            "human has already reached out.",
            "If the lead is on the do-not-contact list, skip and log a "
            "manual note instead.",
        ),
        (
            "If sent in error, follow up with a short apology message and "
            "mark the callback as cancelled in the calendar.",
        ),
    ),

    ACTION_DRAFT_AGENT_ASSIGNMENT: (
        "Assign lead {{lead_ref}} to an available agent. The agent should "
        "make first contact within the next 5 minutes; speed-to-lead is the "
        "single biggest predictor of conversion.",
        (
            "Confirm the chosen agent is actually available (not on another "
            "call, not on PTO).",
            "Do not assign a lead the agent has explicitly declined or that "
            "violates routing rules (area / specialty / language).",
        ),
        (
            "If the assignment was wrong, reassign in the agent CRM and "
            "leave a one-line note explaining why.",
        ),
    ),

    ACTION_DRAFT_SOFT_CHECKIN: (
        "Hi {{lead_name|there}} — wanted to check in. Are you still actively "
        "looking? No pressure either way; happy to keep an eye out for new "
        "listings that match what you mentioned. — {{agent_name|the team}}",
        (
            "Confirm the lead has not opted out of marketing-style messages.",
            "Tone is soft check-in, not a sales push. Do not include "
            "pricing, promotions, or urgency.",
        ),
        (
            "If the lead replies negatively, mark the lead as cold and "
            "stop further outreach for at least 30 days.",
        ),
    ),

    ACTION_DRAFT_FIRST_CONTACT: (
        "Hi {{lead_name|there}} — thanks for getting in touch. I saw your "
        "request come through. When is a good 5-minute window for me to "
        "call you back today? — {{agent_name|the team}}",
        (
            "Confirm the lead's first-response window is still within the "
            "speed-to-lead SLA before sending.",
            "Use the channel the lead originally arrived on (phone, web, "
            "referral) unless they specifically asked for another.",
        ),
        (
            "If first contact has already happened offline, mark the "
            "lead as contacted and skip this draft.",
        ),
    ),

    ACTION_DRAFT_BOOKING_RETRY: (
        "Hi {{lead_name|there}} — wanted to confirm we still have you down "
        "for {{slot_time|the scheduled time}}. Does that still work, or "
        "would you like to reschedule? — {{agent_name|the team}}",
        (
            "Confirm the booking is actually unconfirmed, not already "
            "confirmed by a different channel.",
            "Do NOT double-charge or double-book.",
        ),
        (
            "If the lead says no, mark the booking cancelled and offer "
            "two alternative times manually.",
        ),
    ),

    ACTION_DRAFT_COVERAGE_SHIFT: (
        "Bring a backup agent online or shift coverage so a human can "
        "handle the next first-contact. PAS will keep leads warm but "
        "cannot replace a human first-contact response.",
        (
            "Confirm the on-shift schedule before paging anyone.",
            "Coverage shifts should be agreed verbally with the agent — "
            "do not silently re-assign their shift in the rota system.",
        ),
        (
            "If the page was sent in error, send a follow-up note within "
            "60 seconds clarifying.",
        ),
    ),

    ACTION_DRAFT_ALTERNATE_CHANNEL: (
        "Hi {{lead_name|there}} — having trouble reaching you on the phone. "
        "Is there a better number, or would email or SMS work? — "
        "{{agent_name|the team}}",
        (
            "Confirm the phone number on file is actually wrong before "
            "switching channels.",
            "Do not switch channel without operator approval — the lead "
            "originally consented to a specific channel.",
        ),
        (
            "If the alternate channel was wrong, return to the original "
            "channel and leave a one-line note explaining.",
        ),
    ),

    ACTION_DRAFT_AFTER_HOURS_PLAN: (
        "Hand this after-hours lead to the next on-shift agent. Provide "
        "a brief: timing, source, and any context the lead shared.",
        (
            "Do not call after-hours unless the lead explicitly asked for "
            "an after-hours call back.",
            "If the brokerage has a do-not-call window, respect it.",
        ),
        (
            "If the lead is reached too early, apologise and reschedule "
            "to the agreed window.",
        ),
    ),

    ACTION_DRAFT_SENIOR_AGENT_HANDOFF: (
        "Hand high-value lead {{lead_ref}} to a senior agent immediately. "
        "Senior agent should take this one personally; high-value leads "
        "close faster with a human reaching out within minutes.",
        (
            "Confirm the lead truly qualifies as high-value (value_tier "
            "evidence) before paging a senior agent.",
            "Do not page a senior agent who is already on another "
            "high-value call.",
        ),
        (
            "If the handoff was wrong, return the lead to its previous "
            "assignment and leave a brief note for the original agent.",
        ),
    ),

    ACTION_DRAFT_HUMAN_REVIEW_REQUEST: (
        "Ask a manager or compliance owner to read this lead's transcript "
        "before PAS continues automated handling. Surface the lead_ref, "
        "the reason flagged, and a short context summary.",
        (
            "Do not act on the flagged content until a human has reviewed.",
            "If the content includes sensitive personal data, hand it to "
            "the compliance owner directly, not the general team channel.",
        ),
        (
            "If review confirms the flag was false, mark the lead as "
            "cleared and resume normal handling.",
        ),
    ),
}


# ──────────────────────────────────────────────────────────────────
# Value objects.
# ──────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class ActionProposal:
    """A bounded, frozen proposal package derived from a PAS208
    ``Recommendation`` that the operator has already approved for
    manual review.

    There is NO execute method. The draft is plain text the
    operator can copy and paste, or use as a starting point for
    their own composition. The engine never reads this object.
    """
    proposal_id:                  str
    recommendation_id:            str
    signal_id:                    str
    signal_type:                  str
    severity:                     str
    subject_type:                 str
    subject_ref:                  str
    proposed_action_type:         str
    draft_message_or_instruction: str
    safety_notes:                 Tuple[str, ...]
    rollback_notes:               Tuple[str, ...]
    evidence:                     Mapping[str, object] = field(default_factory=dict)
    created_at:                   str = ""
    # Hard PAS209 invariants — never flipped by any code in this
    # module. The readiness gate asserts both defaults and that no
    # code path overwrites them.
    required_human_review:        bool = True
    allowed_channel:              str  = ALLOWED_CHANNEL_MANUAL_ONLY
    live_behavior_changed:        bool = False


@dataclass(frozen=True)
class ActionProposalPackage:
    """A bounded package of proposals derived from a single PAS208
    ``RecommendationDigest``. Pure value object — no I/O.
    """
    package_id:                       str
    generated_at:                     str
    source_recommendation_digest_id:  str
    observed_at:                      str
    phase:                            str = "PAS209"
    allowed_environment:              str = "SIMULATION_ONLY"
    live_behavior_changed:            bool = False
    proposals:                        Tuple[ActionProposal, ...] = ()
    counts_by_action_type:            Mapping[str, int] = field(default_factory=dict)


# ──────────────────────────────────────────────────────────────────
# Helpers.
# ──────────────────────────────────────────────────────────────────


def _proposal_id(recommendation_id: str, action_type: str) -> str:
    payload = f"{recommendation_id}|{action_type}".encode("utf-8")
    return "pas209-prop-" + hashlib.sha256(payload).hexdigest()[:16]


def _package_id(source_digest_id: str, n_props: int, observed_at: str) -> str:
    payload = f"{source_digest_id}|{n_props}|{observed_at}".encode("utf-8")
    return "pas209-pkg-" + hashlib.sha256(payload).hexdigest()[:16]


def _template_for(action_type: str) -> Optional[Tuple[str, Tuple[str, ...], Tuple[str, ...]]]:
    return _PROPOSAL_TEMPLATES.get(action_type)


# ──────────────────────────────────────────────────────────────────
# Pure builders.
# ──────────────────────────────────────────────────────────────────


def build_proposal(recommendation: Recommendation) -> Optional[ActionProposal]:
    """Build a single ``ActionProposal`` from a PAS208
    ``Recommendation``.

    Returns ``None`` when:

      * ``recommendation`` is not a ``Recommendation`` instance, or
      * its ``approval_status`` is not
        ``APPROVAL_APPROVED_FOR_MANUAL_REVIEW`` — PAS209 refuses to
        propose anything for CANDIDATE / REJECTED / DEFERRED
        recommendations, or
      * the ``recommended_action_type`` is not in the closed
        ``_PROPOSAL_TEMPLATES`` map.

    This is the closed-vocabulary safety net — an unrecognised or
    unapproved input silently produces no proposal rather than
    raising or guessing.
    """
    if not isinstance(recommendation, Recommendation):
        return None
    if recommendation.approval_status != APPROVAL_APPROVED_FOR_MANUAL_REVIEW:
        return None
    template = _template_for(recommendation.recommended_action_type)
    if template is None:
        return None

    draft, safety_notes, rollback_notes = template
    return ActionProposal(
        proposal_id                  = _proposal_id(
            recommendation.recommendation_id,
            recommendation.recommended_action_type,
        ),
        recommendation_id            = recommendation.recommendation_id,
        signal_id                    = recommendation.signal_id,
        signal_type                  = recommendation.signal_type,
        severity                     = recommendation.severity,
        subject_type                 = recommendation.subject_type,
        subject_ref                  = recommendation.subject_ref,
        proposed_action_type         = recommendation.recommended_action_type,
        draft_message_or_instruction = draft,
        safety_notes                 = safety_notes,
        rollback_notes               = rollback_notes,
        evidence                     = dict(recommendation.evidence or {}),
        created_at                   = recommendation.created_at or "",
        required_human_review        = True,
        allowed_channel              = ALLOWED_CHANNEL_MANUAL_ONLY,
        live_behavior_changed        = False,
    )


def build_proposal_package(
    rec_digest: RecommendationDigest,
) -> ActionProposalPackage:
    """Build an ``ActionProposalPackage`` from a PAS208 digest.

    Iterates ``rec_digest.recommendations`` and includes one
    ``ActionProposal`` per recommendation whose state is
    ``APPROVED_FOR_MANUAL_REVIEW``. Pure function — no I/O.
    """
    if not isinstance(rec_digest, RecommendationDigest):
        raise TypeError(
            "build_proposal_package expects a RecommendationDigest"
        )

    proposals: List[ActionProposal] = []
    for rec in rec_digest.recommendations:
        prop = build_proposal(rec)
        if prop is not None:
            proposals.append(prop)

    by_action: _Counter[str] = _Counter(p.proposed_action_type for p in proposals)
    counts_by_action_type = {
        atype: int(by_action.get(atype, 0)) for atype in RECOMMENDED_ACTION_TYPES
    }

    return ActionProposalPackage(
        package_id                       = _package_id(
            rec_digest.digest_id, len(proposals), rec_digest.observed_at,
        ),
        generated_at                     = rec_digest.observed_at,
        source_recommendation_digest_id  = rec_digest.digest_id,
        observed_at                      = rec_digest.observed_at,
        phase                            = "PAS209",
        allowed_environment              = "SIMULATION_ONLY",
        live_behavior_changed            = False,
        proposals                        = tuple(proposals),
        counts_by_action_type            = counts_by_action_type,
    )


# ──────────────────────────────────────────────────────────────────
# Renderers.
# ──────────────────────────────────────────────────────────────────


def _proposal_to_dict(p: ActionProposal) -> Dict[str, object]:
    return {
        "proposal_id":                  p.proposal_id,
        "recommendation_id":            p.recommendation_id,
        "signal_id":                    p.signal_id,
        "signal_type":                  p.signal_type,
        "severity":                     p.severity,
        "subject_type":                 p.subject_type,
        "subject_ref":                  p.subject_ref,
        "proposed_action_type":         p.proposed_action_type,
        "draft_message_or_instruction": p.draft_message_or_instruction,
        "safety_notes":                 list(p.safety_notes),
        "rollback_notes":               list(p.rollback_notes),
        "evidence":                     dict(p.evidence or {}),
        "created_at":                   p.created_at,
        "required_human_review":        p.required_human_review,
        "allowed_channel":              p.allowed_channel,
        "live_behavior_changed":        p.live_behavior_changed,
    }


def to_machine_json(pkg: ActionProposalPackage) -> Dict[str, object]:
    return {
        "phase":                            pkg.phase,
        "allowed_environment":              pkg.allowed_environment,
        "live_behavior_changed":            pkg.live_behavior_changed,
        "package_id":                       pkg.package_id,
        "generated_at":                     pkg.generated_at,
        "observed_at":                      pkg.observed_at,
        "source_recommendation_digest_id":  pkg.source_recommendation_digest_id,
        "counts_by_action_type":            dict(pkg.counts_by_action_type),
        "proposals":                        [_proposal_to_dict(p) for p in pkg.proposals],
    }


def to_broker_report(pkg: ActionProposalPackage) -> str:
    """Broker-voice summary of the proposal package.

    Every emitted proposal includes a draft a human can read and
    decide to send manually, plus safety and rollback notes. The
    summary never mentions PAS internals or closed-vocab tokens.
    """
    if not pkg.proposals:
        return (
            "There are no approved items to package for manual action right "
            "now. PAS waits for an operator to approve a recommendation "
            "before it will draft anything."
        )

    lines: List[str] = []
    lines.append(
        f"I have {len(pkg.proposals)} item(s) packaged for manual review. "
        "Nothing has been sent — a human still needs to read each draft, "
        "decide if it is appropriate, and send it manually."
    )
    for p in pkg.proposals:
        lines.append("")
        lines.append(
            f"- Subject: {p.subject_type} {p.subject_ref} (severity {p.severity})."
        )
        lines.append("  Draft to review:")
        for ln in p.draft_message_or_instruction.splitlines() or [
            p.draft_message_or_instruction
        ]:
            lines.append(f"    {ln}")
        if p.safety_notes:
            lines.append("  Before you send, check:")
            for note in p.safety_notes:
                lines.append(f"    * {note}")
        if p.rollback_notes:
            lines.append("  If something goes wrong after you send:")
            for note in p.rollback_notes:
                lines.append(f"    * {note}")
    lines.append("")
    lines.append(
        "Manual only. PAS will not send any of this. A human reviewing the "
        "drafts is required."
    )
    return "\n".join(lines)


__all__ = (
    "ALLOWED_CHANNEL_MANUAL_ONLY",
    "ALLOWED_CHANNELS",
    "ActionProposal",
    "ActionProposalPackage",
    "build_proposal",
    "build_proposal_package",
    "to_machine_json",
    "to_broker_report",
)
