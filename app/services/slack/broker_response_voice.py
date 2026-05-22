"""
PAS204 — Broker-facing response voice.

Pure-function translator that converts PAS technical tokens and
intent codes into plain-English, staff-style sentences. No LLM,
no network, no mutation. The output vocabulary is bounded.

The translator addresses three audiences:

  * `translate_token(token)` — atomic technical -> human. Used
    when the surface needs to render a PAS200/201 closed-vocab
    token in plain English.
  * `translate_tokens(tokens)` — bullet-list-friendly batch.
  * `response_for_intent(intent_code, *, evidence)` — full
    broker-facing reply per intent, optionally grounded in
    PAS201 evidence (the digest dict). When evidence is absent
    or incomplete, the response says so explicitly instead of
    inventing data.

The response voice deliberately:

  * Never claims live behaviour. The phrase "no real leads" /
    "no live behavior was changed" appears on every PAS201-
    grounded reply.
  * Never names a real broker, lead, address, phone, or
    production system identifier.
  * Never emits a forbidden live-routing token. A defensive
    guard (`_enforce_no_forbidden_tokens`) blocks any rendered
    sentence containing live_routing_active, live_call_routed,
    strategy_deployed_live, real_lead_handled, or
    production_traffic_served.
"""

from __future__ import annotations

from typing import Dict, Iterable, List, Optional, Tuple

from app.services.slack.broker_question_catalogue import (
    INTENT_AFTER_HOURS_COVERAGE,
    INTENT_AGENT_ROUTING_STATUS,
    INTENT_APPOINTMENTS_TODAY,
    INTENT_CALLBACK_REQUESTS,
    INTENT_CRM_SYNC_STATUS,
    INTENT_DASHBOARD_EXPLANATION,
    INTENT_EVIDENCE_DIGEST,
    INTENT_FACEBOOK_LEAD_HANDLING,
    INTENT_FALLBACK_CLARIFY,
    INTENT_HOT_LEADS_SUMMARY,
    INTENT_INTEGRATION_QUESTIONS,
    INTENT_ISA_COMPARISON,
    INTENT_LEAD_SOURCE_QUALITY,
    INTENT_LEADS_TODAY_COUNT,
    INTENT_MISSED_LEADS,
    INTENT_REALTOR_LEAD_HANDLING,
    INTENT_RESPONSE_SPEED,
    INTENT_SAFETY_TRUST,
    INTENT_STALE_LEADS,
    INTENT_TRAINING_PAS,
    INTENT_WHAT_SHOULD_I_DO,
    INTENT_ZILLOW_LEAD_HANDLING,
)


# ──────────────────────────────────────────────────────────────────
# Closed token -> human translation table
# ──────────────────────────────────────────────────────────────────

TOKEN_TRANSLATIONS: Dict[str, str] = {
    # Environment / safety markers (PAS197-PAS202)
    "SIMULATION_ONLY": (
        "This was tested safely in rehearsal. It hasn't touched real leads yet."
    ),
    "live_behavior_changed=False": (
        "No live behavior was changed."
    ),
    "READY_FOR_MANUAL_TEST": (
        "A strategy is queued for manual review by an operator."
    ),
    "APPROVED_FOR_MANUAL_TEST": (
        "An operator approved this strategy for manual review."
    ),
    "EXECUTED": (
        "The rehearsal ran end-to-end without errors."
    ),
    # PAS200 behavioural flags
    "behavioral_low_friction_observed": (
        "The conversations stayed smooth and didn't push the lead too hard."
    ),
    "behavioral_high_friction_observed": (
        "Some scenarios got bumpy — the lead pushed back more than expected."
    ),
    "behavioral_good_pacing_observed": (
        "The pacing felt natural — discovery before any commitment ask."
    ),
    "behavioral_high_pressure_observed": (
        "The strategy leans pushy — too many appointment asks too early."
    ),
    "low_trust_strategy": (
        "The strategy is safe, but some replies still feel a little too transactional."
    ),
    "behavioral_low_trust_observed": (
        "Replies skewed a bit transactional. A warmer tone would help."
    ),
    "behavioral_trust_preservation_observed": (
        "PAS acknowledged the lead before any qualification ask."
    ),
    "behavioral_callback_continuity_observed": (
        "PAS offered a callback as a natural next step, not a hard sell."
    ),
    "behavioral_early_escalation_observed": (
        "PAS jumped to booking too early in some scenarios."
    ),
    # PAS201 evidence / lineage / safety
    "runtime_pass_rate_100_percent": (
        "Every rehearsal scenario passed."
    ),
    "runtime_pass_rate_at_or_above_95_percent": (
        "Almost every rehearsal scenario passed (>= 95%)."
    ),
    "runtime_pass_rate_at_or_above_75_percent": (
        "Most rehearsal scenarios passed (>= 75%)."
    ),
    "runtime_pass_rate_below_75_percent": (
        "Pass rate is below the 75% bar — more rehearsal is needed."
    ),
    "safety_outcome_clean": (
        "Safety checks passed cleanly across the whole rehearsal."
    ),
    "safety_outcome_auto_fail": (
        "At least one rehearsal scenario triggered a safety auto-fail."
    ),
    "lineage_intact": (
        "All the test artifacts connect end-to-end as expected."
    ),
    "lineage_broken": (
        "The rehearsal artifacts don't line up — something is missing in the chain."
    ),
    "artifact_integrity_complete": (
        "Every integrity check on the rehearsal artifacts passed."
    ),
    "artifact_integrity_incomplete": (
        "One or more integrity checks on the rehearsal artifacts failed."
    ),
    "no_live_behavior_change_anywhere_in_lineage": (
        "Nothing in the chain touched any real lead."
    ),
    # PAS201 claimable_now / not_claimable_yet vocab
    "no_live_behavior_changed": (
        "No live behavior was changed during this rehearsal."
    ),
    "no_pii_in_simulation_artifacts": (
        "Nothing in the rehearsal carries any personal info."
    ),
    "safety_auto_fails_remain_absolute": (
        "Safety failures stop the rehearsal — they are never silently ignored."
    ),
    "operator_approved_strategy_for_manual_test": (
        "An operator already approved this strategy for manual review."
    ),
    "manual_test_executed_in_simulation_only": (
        "The manual test ran in rehearsal, not against real leads."
    ),
    "lineage_inspectable_end_to_end": (
        "Every step of the rehearsal can be reviewed from start to finish."
    ),
    "behavioral_evaluation_emitted_deterministically": (
        "Behavioural scoring is repeatable — same rehearsal, same scores."
    ),
    "synthetic_rehearsal_passed_for_strategy": (
        "The full rehearsal passed for this strategy."
    ),
    "live_call_routing_remains_out_of_scope": (
        "Live call routing isn't on yet — rehearsal only."
    ),
    "calibration_against_live_call_outcomes_pending": (
        "We haven't yet compared rehearsal results to live-call outcomes."
    ),
    "automated_promotion_to_runtime_strategy_pending": (
        "Strategies don't auto-promote into production — humans still decide."
    ),
    "real_lead_exposure_remains_out_of_scope": (
        "No real lead has been routed through this strategy."
    ),
    "slack_operator_surface_for_runtime_runs_pending": (
        "Triggering rehearsal runs from Slack isn't built yet."
    ),
    # Evidence strength labels
    "strong": (
        "Strong — every safety check passed and the rehearsal cleared the pass-rate bar."
    ),
    "moderate": (
        "Moderate — rehearsal mostly passed, but a few scenarios could use attention."
    ),
    "weak": (
        "Weak — pass rate is below the bar; another rehearsal is recommended."
    ),
    "blocked": (
        "Blocked — a safety issue surfaced; the rehearsal evidence is not safe to claim yet."
    ),
    # Strategy ids — kept human-neutral.
    "callback_first": "the callback-first strategy",
    "balanced":       "the balanced strategy",
    "conservative":   "the conservative strategy",
    "assertive":      "the assertive strategy",
    "booking_first":  "the booking-first strategy",
}


# Defensive guard — these tokens must never appear in any
# rendered broker-facing response. Mirrors PAS202.
FORBIDDEN_OUTPUT_TOKENS: Tuple[str, ...] = (
    "live_routing_active",
    "live_call_routed",
    "strategy_deployed_live",
    "real_lead_handled",
    "production_traffic_served",
)


# Closed vocabulary of "next things you can ask PAS". Used by
# every intent response to nudge the broker forward.
NEXT_STEP_SUGGESTIONS_BY_INTENT: Dict[str, Tuple[str, ...]] = {
    INTENT_LEADS_TODAY_COUNT: (
        "Ask: \"hot leads\" to see the most engaged ones first.",
        "Ask: \"any leads we missed\" to spot dropped follow-ups.",
    ),
    INTENT_HOT_LEADS_SUMMARY: (
        "Ask: \"any callbacks owed\" to make sure none are slipping.",
        "Ask: \"appointments today\" to confirm bookings landed.",
    ),
    INTENT_MISSED_LEADS: (
        "Ask: \"stale leads\" to surface older threads worth a nudge.",
        "Ask: \"who needs a callback\" to fix the immediate gap.",
    ),
    INTENT_STALE_LEADS: (
        "Ask: \"hot leads\" to focus on the warmest threads first.",
        "Ask: \"missed leads\" to catch anything that slipped through.",
    ),
    INTENT_CALLBACK_REQUESTS: (
        "Ask: \"appointments today\" to see what made it onto the calendar.",
        "Ask: \"hot leads\" to prioritise the rest of the day.",
    ),
    INTENT_APPOINTMENTS_TODAY: (
        "Ask: \"hot leads\" for the next set of warm threads.",
        "Ask: \"any callbacks owed\" to keep momentum.",
    ),
    INTENT_AGENT_ROUTING_STATUS: (
        "Ask: \"appointments today\" to see where routing landed bookings.",
        "Ask: \"response speed\" to check how fast routed leads were touched.",
    ),
    INTENT_RESPONSE_SPEED: (
        "Ask: \"any leads we missed\" if speed dipped this morning.",
        "Ask: \"which source converts best\" to see where speed matters most.",
    ),
    INTENT_LEAD_SOURCE_QUALITY: (
        "Ask: \"zillow leads\" / \"facebook leads\" for source-specific detail.",
        "Ask: \"appointments today\" to tie source to outcomes.",
    ),
    INTENT_CRM_SYNC_STATUS: (
        "Ask: \"integrations\" to review the rest of the connections.",
        "Ask: \"any leads we missed\" to spot anything left out of the sync.",
    ),
    INTENT_ZILLOW_LEAD_HANDLING: (
        "Ask: \"response speed\" to see how fast Zillow leads were answered.",
        "Ask: \"appointments today\" to see which Zillow leads booked.",
    ),
    INTENT_REALTOR_LEAD_HANDLING: (
        "Ask: \"response speed\" to see how fast realtor.com leads were answered.",
        "Ask: \"appointments today\" to see which realtor.com leads booked.",
    ),
    INTENT_FACEBOOK_LEAD_HANDLING: (
        "Ask: \"response speed\" to see how fast Facebook leads were answered.",
        "Ask: \"appointments today\" to see which Facebook leads booked.",
    ),
    INTENT_ISA_COMPARISON: (
        "Ask: \"simulation digest\" to see the rehearsal evidence for the current strategy.",
        "Ask: \"is pas safe to use\" for a plain-English safety summary.",
    ),
    INTENT_AFTER_HOURS_COVERAGE: (
        "Ask: \"any leads we missed\" if you're worried about overnight gaps.",
        "Ask: \"response speed\" to see how fast after-hours leads were answered.",
    ),
    INTENT_TRAINING_PAS: (
        "Ask: \"simulation digest\" to see how the current strategy is performing.",
        "Ask: \"is pas safe to use\" before changing strategy settings.",
    ),
    INTENT_INTEGRATION_QUESTIONS: (
        "Ask: \"crm sync\" once an integration is connected.",
        "Ask: \"any leads we missed\" to confirm the new pipe is delivering.",
    ),
    INTENT_DASHBOARD_EXPLANATION: (
        "Ask: \"response speed\" to see the speed metric in plain English.",
        "Ask: \"which source converts best\" to see the conversion metric in context.",
    ),
    INTENT_EVIDENCE_DIGEST: (
        "Ask: \"is pas safe to use\" for the plain-English safety summary.",
        "Ask: \"what should I do next\" to see prioritised actions.",
    ),
    INTENT_SAFETY_TRUST: (
        "Ask: \"simulation digest\" to see the underlying rehearsal evidence.",
        "Ask: \"what should I do next\" for prioritised actions.",
    ),
    INTENT_WHAT_SHOULD_I_DO: (
        "Ask: \"hot leads\" to start the day with warm threads.",
        "Ask: \"any callbacks owed\" to clear time-sensitive promises first.",
    ),
    INTENT_FALLBACK_CLARIFY: (
        "Try: \"how many leads today\" or \"hot leads\" or \"what should I do\".",
    ),
}


# ──────────────────────────────────────────────────────────────────
# Public translation helpers
# ──────────────────────────────────────────────────────────────────

def translate_token(token: str) -> str:
    """Atomic technical token -> human sentence. Empty string if
    the token is not in the closed translation table."""
    if not isinstance(token, str) or not token:
        return ""
    return TOKEN_TRANSLATIONS.get(token, "")


def translate_tokens(tokens: Iterable[str]) -> List[str]:
    """Batch translation. Returns a list of human sentences,
    skipping tokens not in the translation table."""
    out: List[str] = []
    for t in tokens:
        s = translate_token(t)
        if s:
            out.append(s)
    return out


def _enforce_no_forbidden_tokens(text: str) -> str:
    """Drop in defence-in-depth — if any forbidden live-routing
    token slipped through, swap the whole rendering for a safe
    fallback. This should never trigger in practice."""
    lower = text.lower()
    for tok in FORBIDDEN_OUTPUT_TOKENS:
        if tok in lower:
            return (
                "I'm rendering this through the safe fallback — the "
                "underlying response contained an unsafe phrase."
            )
    return text


# ──────────────────────────────────────────────────────────────────
# Per-intent response bodies
# ──────────────────────────────────────────────────────────────────
#
# Each helper takes an optional `evidence` dict (the parsed
# PAS201 digest) so the response can be grounded when evidence
# is available; otherwise it gives a generic, honest answer that
# never invents data.

def _digest_grounded(evidence: Optional[dict]) -> List[str]:
    """Return one-line human translations of the most useful
    PAS201 digest fields. Empty list if evidence is None."""
    if not isinstance(evidence, dict):
        return []
    out: List[str] = []
    strength = evidence.get("evidence_strength")
    if isinstance(strength, str):
        line = translate_token(strength)
        if line:
            out.append(line)
    # Operator highlights — closed-vocab, safe to translate.
    op = evidence.get("operator_summary") or {}
    for hl in op.get("highlights") or []:
        line = translate_token(hl)
        if line:
            out.append(line)
    # Safety env reminder, always.
    out.append(translate_token("no_live_behavior_changed"))
    return out


def _response_leads_today_count(evidence) -> str:
    return (
        "I don't have today's lead counts in front of me, but here's how to "
        "think about it: I can tell you new leads, missed leads, and "
        "callbacks owed by name (just ask). I never invent numbers — if I "
        "can't see the data, I'll say so."
    )


def _response_hot_leads(evidence) -> str:
    return (
        "Hot leads are the ones engaging most — quick replies, repeat "
        "questions, time-window asks. I can't list specific names without "
        "more data plumbed in, but I'll never guess. Ask \"any callbacks "
        "owed\" to make sure none of them are slipping."
    )


def _response_missed_leads(evidence) -> str:
    return (
        "A missed lead is one PAS didn't reach in the response window. "
        "I can't list them by name without more data plumbed in, but I "
        "won't invent any. The fastest fix is usually checking response "
        "speed and callback gaps — ask either of those next."
    )


def _response_stale_leads(evidence) -> str:
    return (
        "Stale leads are old threads that have gone quiet. The recovery "
        "play is a soft nudge, not a hard sell. I'll never claim to have "
        "re-touched a stale lead unless I actually have. Ask \"hot leads\" "
        "to keep your warmest threads front of mind."
    )


def _response_callbacks(evidence) -> str:
    return (
        "Callbacks owed are the time-sensitive promises — \"I'll call you "
        "tomorrow at 9\" type things. I can't list them by name without "
        "more data plumbed in. If you'd like, ask \"appointments today\" "
        "to see what made it onto the calendar."
    )


def _response_appointments(evidence) -> str:
    return (
        "Appointments today is the booked-showing count. I'll never claim "
        "a booking PAS didn't actually make. If the number is zero, that "
        "doesn't mean the day was wasted — ask \"hot leads\" to see the "
        "warmest threads to push toward a booking."
    )


def _response_agent_routing(evidence) -> str:
    return (
        "Agent routing is who PAS hands warm leads off to. I'll never "
        "claim to have routed a lead I haven't. Ask \"appointments today\" "
        "to see which routing landed real bookings."
    )


def _response_response_speed(evidence) -> str:
    return (
        "Response speed is how fast PAS reaches a new lead — minutes "
        "matter, especially for portal leads. I won't fabricate a number; "
        "ask \"any leads we missed\" if you're worried the speed dipped "
        "today."
    )


def _response_lead_source_quality(evidence) -> str:
    return (
        "Lead source quality compares how well each pipe (Zillow, "
        "realtor.com, Facebook, organic) converts to a booking. I won't "
        "guess if I can't see the data. Ask about a specific source "
        "(\"zillow leads\", \"facebook leads\") for source-specific "
        "detail."
    )


def _response_crm_sync(evidence) -> str:
    return (
        "CRM sync is whether PAS and your CRM are seeing the same leads. "
        "If something looks off, ask \"integrations\" to review which "
        "pipes are connected. I'll never silently overwrite a CRM record."
    )


def _response_source_handling(source_name: str) -> str:
    return (
        f"{source_name} leads come in through their portal feed and PAS "
        f"answers like any other lead — same response-speed bar, same "
        f"safety rules, same handoff to an agent when warm. I won't "
        f"claim PAS replied unless it actually did. Ask \"response speed\" "
        f"to see how fast we answered today."
    )


def _response_isa_comparison(evidence) -> str:
    return (
        "PAS isn't trying to be your ISA — it's a 24/7 first-touch and "
        "qualification layer that hands warm leads to your agents. It's "
        "more consistent at 2 AM, less nuanced on weird objections. The "
        "current strategy has been rehearsed in simulation; ask "
        "\"simulation digest\" for that evidence."
    )


def _response_after_hours(evidence) -> str:
    return (
        "PAS answers leads at any hour — nights, weekends, holidays. "
        "Live calls follow your brokerage's hours; PAS does the "
        "first-touch and books callbacks. Ask \"any leads we missed\" "
        "if you suspect an overnight gap."
    )


def _response_training(evidence) -> str:
    return (
        "Training PAS means adjusting the strategy and tone. Today, "
        "operators approve strategy changes after rehearsal — PAS "
        "doesn't auto-learn from real calls. Ask \"simulation digest\" "
        "to see how the current strategy is performing."
    )


def _response_integrations(evidence) -> str:
    return (
        "PAS connects to CRMs (e.g., Follow Up Boss, Lofty), portals "
        "(Zillow, realtor.com), and Facebook Lead Ads. Setup is a "
        "one-time wiring step. Ask \"crm sync\" once you've connected "
        "something."
    )


def _response_dashboard(evidence) -> str:
    return (
        "The dashboard shows the operational basics — leads today, "
        "response speed, conversion, queue depth. Each number is a "
        "literal count or rate; nothing is estimated. Ask \"response "
        "speed\" or \"which source converts best\" to dig into a "
        "specific metric."
    )


def _response_evidence_digest(evidence) -> str:
    lines = [
        "Here's what the rehearsal evidence says today:",
    ]
    grounded = _digest_grounded(evidence)
    if grounded:
        lines.extend(f"- {g}" for g in grounded)
    else:
        lines.append(
            "- No rehearsal digest is on disk yet. Run the PAS201 "
            "digest generator first to populate one."
        )
        lines.append(
            "- " + translate_token("no_live_behavior_changed")
        )
    return "\n".join(lines)


def _response_safety(evidence) -> str:
    base = (
        "PAS is safe to use today for the rehearsal surface — it never "
        "routes a real call without operator sign-off. "
        + translate_token("no_live_behavior_changed")
    )
    grounded = _digest_grounded(evidence)
    if grounded:
        base += "\nFrom the latest rehearsal:\n" + "\n".join(
            f"- {g}" for g in grounded
        )
    return base


def _response_what_should_i_do(evidence) -> str:
    return (
        "The fastest payoff is usually: clear the callbacks you owe, "
        "then work the hot leads, then catch up on anything missed. "
        "Ask \"any callbacks owed\", then \"hot leads\", then \"missed "
        "leads\" in that order — that's most of a productive morning."
    )


def _response_fallback_clarify(evidence) -> str:
    return (
        "I didn't catch that one. I can answer questions about leads "
        "(today / hot / missed / stale), callbacks, appointments, "
        "response speed, source quality, CRM sync, integrations, the "
        "dashboard, the simulation digest, safety, and \"what should I "
        "do next\". Try one of those, or rephrase what you wanted."
    )


_INTENT_RESPONSE_BUILDERS = {
    INTENT_LEADS_TODAY_COUNT:      _response_leads_today_count,
    INTENT_HOT_LEADS_SUMMARY:      _response_hot_leads,
    INTENT_MISSED_LEADS:           _response_missed_leads,
    INTENT_STALE_LEADS:            _response_stale_leads,
    INTENT_CALLBACK_REQUESTS:      _response_callbacks,
    INTENT_APPOINTMENTS_TODAY:     _response_appointments,
    INTENT_AGENT_ROUTING_STATUS:   _response_agent_routing,
    INTENT_RESPONSE_SPEED:         _response_response_speed,
    INTENT_LEAD_SOURCE_QUALITY:    _response_lead_source_quality,
    INTENT_CRM_SYNC_STATUS:        _response_crm_sync,
    INTENT_ZILLOW_LEAD_HANDLING:   lambda e: _response_source_handling("Zillow"),
    INTENT_REALTOR_LEAD_HANDLING:  lambda e: _response_source_handling("realtor.com"),
    INTENT_FACEBOOK_LEAD_HANDLING: lambda e: _response_source_handling("Facebook"),
    INTENT_ISA_COMPARISON:         _response_isa_comparison,
    INTENT_AFTER_HOURS_COVERAGE:   _response_after_hours,
    INTENT_TRAINING_PAS:           _response_training,
    INTENT_INTEGRATION_QUESTIONS:  _response_integrations,
    INTENT_DASHBOARD_EXPLANATION:  _response_dashboard,
    INTENT_EVIDENCE_DIGEST:        _response_evidence_digest,
    INTENT_SAFETY_TRUST:           _response_safety,
    INTENT_WHAT_SHOULD_I_DO:       _response_what_should_i_do,
    INTENT_FALLBACK_CLARIFY:       _response_fallback_clarify,
}


def response_for_intent(
    intent_code: str, *, evidence: Optional[dict] = None,
) -> str:
    """Build the full broker-facing reply for an intent.
    Defensively scrubs the output of forbidden live-routing
    tokens. Always returns a non-empty string."""
    builder = _INTENT_RESPONSE_BUILDERS.get(intent_code) \
        or _response_fallback_clarify
    text = builder(evidence)
    return _enforce_no_forbidden_tokens(text)


def next_step_suggestions(intent_code: str) -> Tuple[str, ...]:
    """Closed-vocab next-step nudges for the given intent."""
    return NEXT_STEP_SUGGESTIONS_BY_INTENT.get(
        intent_code, NEXT_STEP_SUGGESTIONS_BY_INTENT[INTENT_FALLBACK_CLARIFY],
    )
