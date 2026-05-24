"""
PAS208 — Operator-approval layer over PAS205 attention signals.

Turns each PAS205 ``AttentionSignal`` into a bounded
``Recommendation`` object that an operator can approve, reject, or
defer. PAS208 itself does **not** execute anything. The approval
state is metadata describing what the operator decided, not an
instruction the engine will carry out. Bounded action execution
remains out of scope until PAS209.

Hard safety doctrine (asserted by tests and the readiness gate):

  * READ-ONLY. No DB write, no Twilio call, no Slack outbound API
    call, no SMS, no email, no scheduler, no worker.
  * No execution method exists on ``Recommendation``. Applying a
    decision returns a new frozen ``Recommendation`` value
    object; nothing in the engine changes.
  * Closed vocabulary for every state and every action type. A
    new recommended_action_type can only be added by appending to
    ``RECOMMENDED_ACTION_TYPES`` and wiring the mapping below.
  * Every emitted recommendation carries
    ``live_behavior_changed=False`` and ``operator_required=True``.
  * The recommendation_id is a deterministic hash of
    ``(signal_id, recommended_action_type)`` so identical inputs
    produce identical outputs across processes.

Public surface:

  * ``RECOMMENDED_ACTION_TYPES``      — closed tuple of action types
  * ``APPROVAL_STATES``               — closed tuple of states
  * ``SIGNAL_TO_ACTION_TYPE``         — closed mapping
  * ``Recommendation``                — frozen dataclass
  * ``RecommendationDigest``          — frozen dataclass
  * ``build_recommendations(digest)`` — pure builder from PAS205 digest
  * ``apply_decision(rec, decision, operator_ref, ...)``
                                      — pure state transition
  * ``to_machine_json(rdigest)``      — JSON-ready dict
  * ``to_broker_report(rdigest)``     — broker-friendly summary
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Counter as _Counter
from typing import Dict, List, Mapping, Optional, Tuple

from app.services.proactive.observer_models import (
    SIGNAL_AFTER_HOURS_LEAD_PENDING,
    SIGNAL_CALLBACK_OVERDUE,
    SIGNAL_FAILED_BOOKING_CONFIRMATION,
    SIGNAL_HIGH_VALUE_LEAD_WAITING,
    SIGNAL_LEAD_UNASSIGNED,
    SIGNAL_MISSED_FIRST_RESPONSE,
    SIGNAL_NEEDS_HUMAN_REVIEW,
    SIGNAL_NO_AGENT_AVAILABLE,
    SIGNAL_REPEATED_FAILED_CALLS,
    SIGNAL_STALE_LEAD,
    SIGNAL_TYPES,
    AttentionSignal,
    NeedsAttentionDigest,
)


# ──────────────────────────────────────────────────────────────────
# Closed vocabularies.
# ──────────────────────────────────────────────────────────────────

# Recommended action types — what PAS208 proposes the operator do.
# Adding a new entry requires:
#   * appending to RECOMMENDED_ACTION_TYPES (preserve order)
#   * wiring SIGNAL_TO_ACTION_TYPE
#   * adding a human reason template below
#   * appending a tests case + readiness gate check
ACTION_DRAFT_CALLBACK_FOLLOWUP     = "draft_callback_followup"
ACTION_DRAFT_AGENT_ASSIGNMENT      = "draft_agent_assignment"
ACTION_DRAFT_SOFT_CHECKIN          = "draft_soft_checkin"
ACTION_DRAFT_FIRST_CONTACT         = "draft_first_contact"
ACTION_DRAFT_BOOKING_RETRY         = "draft_booking_retry"
ACTION_DRAFT_COVERAGE_SHIFT        = "draft_coverage_shift"
ACTION_DRAFT_ALTERNATE_CHANNEL     = "draft_alternate_channel"
ACTION_DRAFT_AFTER_HOURS_PLAN      = "draft_after_hours_plan"
ACTION_DRAFT_SENIOR_AGENT_HANDOFF  = "draft_senior_agent_handoff"
ACTION_DRAFT_HUMAN_REVIEW_REQUEST  = "draft_human_review_request"

RECOMMENDED_ACTION_TYPES: Tuple[str, ...] = (
    ACTION_DRAFT_CALLBACK_FOLLOWUP,
    ACTION_DRAFT_AGENT_ASSIGNMENT,
    ACTION_DRAFT_SOFT_CHECKIN,
    ACTION_DRAFT_FIRST_CONTACT,
    ACTION_DRAFT_BOOKING_RETRY,
    ACTION_DRAFT_COVERAGE_SHIFT,
    ACTION_DRAFT_ALTERNATE_CHANNEL,
    ACTION_DRAFT_AFTER_HOURS_PLAN,
    ACTION_DRAFT_SENIOR_AGENT_HANDOFF,
    ACTION_DRAFT_HUMAN_REVIEW_REQUEST,
)


# Approval state machine.
APPROVAL_CANDIDATE                 = "CANDIDATE"
APPROVAL_APPROVED_FOR_MANUAL_REVIEW = "APPROVED_FOR_MANUAL_REVIEW"
APPROVAL_REJECTED                  = "REJECTED"
APPROVAL_DEFERRED                  = "DEFERRED"

APPROVAL_STATES: Tuple[str, ...] = (
    APPROVAL_CANDIDATE,
    APPROVAL_APPROVED_FOR_MANUAL_REVIEW,
    APPROVAL_REJECTED,
    APPROVAL_DEFERRED,
)

# Decisions an operator can apply. CANDIDATE is excluded — that is
# the initial state, never a destination.
TERMINAL_APPROVAL_STATES: Tuple[str, ...] = (
    APPROVAL_APPROVED_FOR_MANUAL_REVIEW,
    APPROVAL_REJECTED,
    APPROVAL_DEFERRED,
)


# Mapping from PAS205 signal_type → PAS208 recommended_action_type.
# This is the closed contract between observer and approval layer.
SIGNAL_TO_ACTION_TYPE: Mapping[str, str] = {
    SIGNAL_CALLBACK_OVERDUE:            ACTION_DRAFT_CALLBACK_FOLLOWUP,
    SIGNAL_LEAD_UNASSIGNED:             ACTION_DRAFT_AGENT_ASSIGNMENT,
    SIGNAL_STALE_LEAD:                  ACTION_DRAFT_SOFT_CHECKIN,
    SIGNAL_MISSED_FIRST_RESPONSE:       ACTION_DRAFT_FIRST_CONTACT,
    SIGNAL_FAILED_BOOKING_CONFIRMATION: ACTION_DRAFT_BOOKING_RETRY,
    SIGNAL_NO_AGENT_AVAILABLE:          ACTION_DRAFT_COVERAGE_SHIFT,
    SIGNAL_REPEATED_FAILED_CALLS:       ACTION_DRAFT_ALTERNATE_CHANNEL,
    SIGNAL_AFTER_HOURS_LEAD_PENDING:    ACTION_DRAFT_AFTER_HOURS_PLAN,
    SIGNAL_HIGH_VALUE_LEAD_WAITING:     ACTION_DRAFT_SENIOR_AGENT_HANDOFF,
    SIGNAL_NEEDS_HUMAN_REVIEW:          ACTION_DRAFT_HUMAN_REVIEW_REQUEST,
}


# Human-friendly broker-voice reason templates per action type.
# These are deliberately short, non-technical, and never instruct
# the engine — they describe what the operator could approve doing.
_ACTION_REASON: Mapping[str, str] = {
    ACTION_DRAFT_CALLBACK_FOLLOWUP:
        "Approve a callback follow-up draft for the operator to send.",
    ACTION_DRAFT_AGENT_ASSIGNMENT:
        "Approve assigning this lead to an available agent for first contact.",
    ACTION_DRAFT_SOFT_CHECKIN:
        "Approve a soft check-in draft to re-engage this quiet lead.",
    ACTION_DRAFT_FIRST_CONTACT:
        "Approve a first-contact draft to close the response gap.",
    ACTION_DRAFT_BOOKING_RETRY:
        "Approve a booking confirmation retry the operator can send manually.",
    ACTION_DRAFT_COVERAGE_SHIFT:
        "Approve a coverage shift so a human is on first contact.",
    ACTION_DRAFT_ALTERNATE_CHANNEL:
        "Approve trying an alternate channel (SMS / email) for this lead.",
    ACTION_DRAFT_AFTER_HOURS_PLAN:
        "Approve an after-hours plan that hands this lead to the next on-shift agent.",
    ACTION_DRAFT_SENIOR_AGENT_HANDOFF:
        "Approve handing this high-value lead to a senior agent.",
    ACTION_DRAFT_HUMAN_REVIEW_REQUEST:
        "Approve a human review request so a manager can read the transcript.",
}


# ──────────────────────────────────────────────────────────────────
# Value objects.
# ──────────────────────────────────────────────────────────────────


@dataclass(frozen=True)
class Recommendation:
    """A bounded, frozen recommendation derived from a PAS205 signal.

    There is NO execute method. ``apply_decision`` returns a new
    ``Recommendation`` with the updated approval state, leaving
    the original untouched. The engine never reads this object;
    it lives entirely in the operator-facing approval surface.
    """
    recommendation_id:        str
    signal_id:                str
    signal_type:              str
    severity:                 str
    subject_type:             str
    subject_ref:              str
    recommended_action_type:  str
    approval_status:          str
    reason:                   str
    evidence:                 Mapping[str, object] = field(default_factory=dict)
    created_at:               str = ""
    decided_at:               Optional[str] = None
    decided_by:               Optional[str] = None
    decision_reason:          Optional[str] = None
    # Hard PAS208 invariants — never flipped by any code in this
    # module. The readiness gate asserts the defaults are True /
    # False respectively and that no path overwrites them.
    operator_required:        bool = True
    live_behavior_changed:    bool = False


@dataclass(frozen=True)
class RecommendationDigest:
    """A bounded digest of recommendations derived from a single
    PAS205 ``NeedsAttentionDigest``. Pure value object — no I/O.
    """
    digest_id:                  str
    generated_at:               str
    source_digest_id:           str
    observed_at:                str
    phase:                      str = "PAS208"
    allowed_environment:        str = "SIMULATION_ONLY"
    live_behavior_changed:      bool = False
    recommendations:            Tuple[Recommendation, ...] = ()
    counts_by_status:           Mapping[str, int] = field(default_factory=dict)
    counts_by_action_type:      Mapping[str, int] = field(default_factory=dict)


# ──────────────────────────────────────────────────────────────────
# Helpers.
# ──────────────────────────────────────────────────────────────────


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _recommendation_id(signal_id: str, action_type: str) -> str:
    payload = f"{signal_id}|{action_type}".encode("utf-8")
    return "pas208-rec-" + hashlib.sha256(payload).hexdigest()[:16]


def _digest_id(source_digest_id: str, n_recs: int, observed_at: str) -> str:
    payload = f"{source_digest_id}|{n_recs}|{observed_at}".encode("utf-8")
    return "pas208-dgst-" + hashlib.sha256(payload).hexdigest()[:16]


def _action_type_for(signal_type: str) -> Optional[str]:
    return SIGNAL_TO_ACTION_TYPE.get(signal_type)


def _reason_for(action_type: str) -> str:
    return _ACTION_REASON.get(action_type, "")


# ──────────────────────────────────────────────────────────────────
# Pure builders and transitions.
# ──────────────────────────────────────────────────────────────────


def build_recommendation(signal: AttentionSignal) -> Optional[Recommendation]:
    """Build a single ``Recommendation`` from a PAS205 signal.

    Returns ``None`` if the signal_type is not covered by
    ``SIGNAL_TO_ACTION_TYPE``. This is the closed-vocabulary safety
    net — an unrecognised signal silently produces no
    recommendation rather than raising or guessing.
    """
    if not isinstance(signal, AttentionSignal):
        return None
    action_type = _action_type_for(signal.signal_type)
    if action_type is None:
        return None
    return Recommendation(
        recommendation_id       = _recommendation_id(signal.signal_id, action_type),
        signal_id               = signal.signal_id,
        signal_type             = signal.signal_type,
        severity                = signal.severity,
        subject_type            = signal.subject_type,
        subject_ref             = signal.subject_ref,
        recommended_action_type = action_type,
        approval_status         = APPROVAL_CANDIDATE,
        reason                  = _reason_for(action_type),
        evidence                = dict(signal.evidence or {}),
        created_at              = signal.created_at or "",
        decided_at              = None,
        decided_by              = None,
        decision_reason         = None,
        operator_required       = True,
        live_behavior_changed   = False,
    )


def build_recommendations(digest: NeedsAttentionDigest) -> RecommendationDigest:
    """Build a full ``RecommendationDigest`` from a PAS205 digest.

    Pure function — same input always produces the same output.
    """
    if not isinstance(digest, NeedsAttentionDigest):
        raise TypeError("build_recommendations expects a NeedsAttentionDigest")

    recs: List[Recommendation] = []
    for sig in digest.signals:
        rec = build_recommendation(sig)
        if rec is not None:
            recs.append(rec)

    # Initial status is always CANDIDATE for every recommendation.
    by_status: _Counter[str] = _Counter(r.approval_status for r in recs)
    by_action: _Counter[str] = _Counter(r.recommended_action_type for r in recs)

    counts_by_status = {
        state: int(by_status.get(state, 0)) for state in APPROVAL_STATES
    }
    counts_by_action_type = {
        atype: int(by_action.get(atype, 0)) for atype in RECOMMENDED_ACTION_TYPES
    }

    return RecommendationDigest(
        digest_id              = _digest_id(digest.digest_id, len(recs), digest.observed_at),
        generated_at           = digest.observed_at,
        source_digest_id       = digest.digest_id,
        observed_at            = digest.observed_at,
        phase                  = "PAS208",
        allowed_environment    = "SIMULATION_ONLY",
        live_behavior_changed  = False,
        recommendations        = tuple(recs),
        counts_by_status       = counts_by_status,
        counts_by_action_type  = counts_by_action_type,
    )


def apply_decision(
    rec:           Recommendation,
    decision:      str,
    operator_ref:  str,
    *,
    reason:        str = "",
    decided_at:    Optional[str] = None,
) -> Recommendation:
    """Return a NEW ``Recommendation`` with the approval state
    transitioned to ``decision``.

    The original is not mutated. No I/O. No engine call. No write.

    Raises ``ValueError`` if:
      * the decision is not in ``TERMINAL_APPROVAL_STATES``;
      * the current state is already terminal (no re-decisions
        without an explicit defer-then-approve sequence — DEFERRED
        is the only re-entry point).
    """
    if not isinstance(rec, Recommendation):
        raise TypeError("apply_decision expects a Recommendation")
    if decision not in TERMINAL_APPROVAL_STATES:
        raise ValueError(
            f"unknown decision {decision!r}; expected one of "
            f"{TERMINAL_APPROVAL_STATES}"
        )
    if not isinstance(operator_ref, str) or not operator_ref.strip():
        raise ValueError("operator_ref is required and must be a non-empty string")
    if rec.approval_status in (APPROVAL_APPROVED_FOR_MANUAL_REVIEW, APPROVAL_REJECTED):
        raise ValueError(
            f"recommendation {rec.recommendation_id} is already in a "
            f"terminal state ({rec.approval_status}); decisions cannot "
            "be re-applied without going through DEFERRED first"
        )

    return Recommendation(
        recommendation_id       = rec.recommendation_id,
        signal_id               = rec.signal_id,
        signal_type             = rec.signal_type,
        severity                = rec.severity,
        subject_type            = rec.subject_type,
        subject_ref             = rec.subject_ref,
        recommended_action_type = rec.recommended_action_type,
        approval_status         = decision,
        reason                  = rec.reason,
        evidence                = dict(rec.evidence or {}),
        created_at              = rec.created_at,
        decided_at              = decided_at or _now_iso(),
        decided_by              = operator_ref,
        decision_reason         = reason or None,
        operator_required       = True,
        live_behavior_changed   = False,
    )


# ──────────────────────────────────────────────────────────────────
# Renderers.
# ──────────────────────────────────────────────────────────────────


def _rec_to_dict(rec: Recommendation) -> Dict[str, object]:
    return {
        "recommendation_id":        rec.recommendation_id,
        "signal_id":                rec.signal_id,
        "signal_type":              rec.signal_type,
        "severity":                 rec.severity,
        "subject_type":             rec.subject_type,
        "subject_ref":              rec.subject_ref,
        "recommended_action_type":  rec.recommended_action_type,
        "approval_status":          rec.approval_status,
        "reason":                   rec.reason,
        "evidence":                 dict(rec.evidence or {}),
        "created_at":               rec.created_at,
        "decided_at":               rec.decided_at,
        "decided_by":               rec.decided_by,
        "decision_reason":          rec.decision_reason,
        "operator_required":        rec.operator_required,
        "live_behavior_changed":    rec.live_behavior_changed,
    }


def to_machine_json(rdigest: RecommendationDigest) -> Dict[str, object]:
    return {
        "phase":                  rdigest.phase,
        "allowed_environment":    rdigest.allowed_environment,
        "live_behavior_changed":  rdigest.live_behavior_changed,
        "digest_id":              rdigest.digest_id,
        "generated_at":           rdigest.generated_at,
        "observed_at":            rdigest.observed_at,
        "source_digest_id":       rdigest.source_digest_id,
        "counts_by_status":       dict(rdigest.counts_by_status),
        "counts_by_action_type":  dict(rdigest.counts_by_action_type),
        "recommendations":        [_rec_to_dict(r) for r in rdigest.recommendations],
    }


def to_broker_report(rdigest: RecommendationDigest) -> str:
    """Broker-voice summary of the recommendation digest. Used by
    the CLI for stdout; PAS207-style Slack wiring is deliberately
    out of scope for PAS208 itself.
    """
    if not rdigest.recommendations:
        return (
            "There is nothing for you to approve right now. "
            "I have not taken any action — I only watch and propose."
        )

    lines: List[str] = []
    lines.append(
        f"I have {len(rdigest.recommendations)} item(s) you may want to "
        "approve for manual review. Nothing has been done yet — you decide."
    )
    for r in rdigest.recommendations:
        lines.append("")
        lines.append(f"- {r.reason}")
        lines.append(
            f"    Subject: {r.subject_type} {r.subject_ref} "
            f"(severity {r.severity})."
        )
        lines.append(f"    Current state: {r.approval_status}.")
    lines.append("")
    lines.append(
        "I have not taken any action — you decide which to approve, "
        "reject, or defer. PAS will not act until a human says so."
    )
    return "\n".join(lines)


__all__ = (
    "ACTION_DRAFT_CALLBACK_FOLLOWUP",
    "ACTION_DRAFT_AGENT_ASSIGNMENT",
    "ACTION_DRAFT_SOFT_CHECKIN",
    "ACTION_DRAFT_FIRST_CONTACT",
    "ACTION_DRAFT_BOOKING_RETRY",
    "ACTION_DRAFT_COVERAGE_SHIFT",
    "ACTION_DRAFT_ALTERNATE_CHANNEL",
    "ACTION_DRAFT_AFTER_HOURS_PLAN",
    "ACTION_DRAFT_SENIOR_AGENT_HANDOFF",
    "ACTION_DRAFT_HUMAN_REVIEW_REQUEST",
    "RECOMMENDED_ACTION_TYPES",
    "APPROVAL_CANDIDATE",
    "APPROVAL_APPROVED_FOR_MANUAL_REVIEW",
    "APPROVAL_REJECTED",
    "APPROVAL_DEFERRED",
    "APPROVAL_STATES",
    "TERMINAL_APPROVAL_STATES",
    "SIGNAL_TO_ACTION_TYPE",
    "Recommendation",
    "RecommendationDigest",
    "build_recommendation",
    "build_recommendations",
    "apply_decision",
    "to_machine_json",
    "to_broker_report",
)
