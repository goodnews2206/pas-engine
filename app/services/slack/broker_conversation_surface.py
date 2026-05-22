"""
PAS204 — Broker conversation surface.

Pure function that turns broker-typed text into a bounded
structured broker-facing response. Composes:

  * broker_conversation_intents.match_broker_intent (classifier)
  * broker_response_voice.response_for_intent       (voice)
  * broker_response_voice.next_step_suggestions     (next-steps)

The output is a closed dict carrying:

    {
      "intent":             one of INTENT_CODES,
      "score":              int,
      "response_text":      plain-English answer body,
      "suggested_next":     tuple of next-step strings,
      "evidence_grounded":  bool — True iff a PAS201 digest was
                            supplied AND used,
      "no_data_available":  bool — True for any intent that
                            depends on data we don't have here,
      "clarifying_question": Optional[str] — set only when intent
                            == fallback_clarify and the text was
                            ambiguous enough that a single
                            clarifying question would help.
    }

No I/O. No mutation. No outbound Slack API call. No simulation
execution. Output text is defensively scrubbed of forbidden
live-routing tokens.
"""

from __future__ import annotations

from typing import Dict, Optional

from app.services.slack.broker_conversation_intents import (
    match_broker_intent,
)
from app.services.slack.broker_question_catalogue import (
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
    INTENT_LEAD_SOURCE_QUALITY,
    INTENT_LEADS_TODAY_COUNT,
    INTENT_MISSED_LEADS,
    INTENT_REALTOR_LEAD_HANDLING,
    INTENT_RESPONSE_SPEED,
    INTENT_SAFETY_TRUST,
    INTENT_STALE_LEADS,
    INTENT_WHAT_SHOULD_I_DO,
    INTENT_ZILLOW_LEAD_HANDLING,
)
from app.services.slack.broker_response_voice import (
    FORBIDDEN_OUTPUT_TOKENS,
    next_step_suggestions,
    response_for_intent,
)


# Intents that depend on real operational data (lead counts,
# response speed, callbacks owed, etc.). When the surface has no
# data plumbed in, the response says so explicitly rather than
# inventing numbers.
_DATA_DEPENDENT_INTENTS = frozenset((
    INTENT_LEADS_TODAY_COUNT,
    INTENT_HOT_LEADS_SUMMARY,
    INTENT_MISSED_LEADS,
    INTENT_STALE_LEADS,
    INTENT_CALLBACK_REQUESTS,
    INTENT_APPOINTMENTS_TODAY,
    INTENT_AGENT_ROUTING_STATUS,
    INTENT_RESPONSE_SPEED,
    INTENT_LEAD_SOURCE_QUALITY,
    INTENT_CRM_SYNC_STATUS,
    INTENT_ZILLOW_LEAD_HANDLING,
    INTENT_REALTOR_LEAD_HANDLING,
    INTENT_FACEBOOK_LEAD_HANDLING,
))


# Intents that surface PAS201 evidence when available.
_EVIDENCE_GROUNDED_INTENTS = frozenset((
    INTENT_EVIDENCE_DIGEST,
    INTENT_SAFETY_TRUST,
))


# Closed catalogue of single-line clarifying questions. The
# surface picks at most one based on the fallback-trigger
# pattern.
_CLARIFYING_QUESTIONS = (
    "Which area are you asking about — leads, callbacks, "
    "appointments, response speed, integrations, or safety?",
)


def _enforce_no_forbidden_tokens(text: str) -> str:
    lower = text.lower()
    for tok in FORBIDDEN_OUTPUT_TOKENS:
        if tok in lower:
            return (
                "I'm rendering this through the safe fallback — "
                "the underlying response contained an unsafe phrase."
            )
    return text


def build_broker_response(
    text: str,
    *,
    evidence: Optional[Dict] = None,
) -> Dict[str, object]:
    """Turn broker-typed text into a bounded structured response.

    Parameters
    ----------
    text : str
        Whatever the broker typed. May be empty, malformed,
        typo-laden, or a fragment.
    evidence : Optional[dict]
        Parsed PAS201 digest. When supplied AND the intent is
        one of `_EVIDENCE_GROUNDED_INTENTS`, the response body
        is enriched with digest-derived sentences via the
        PAS204 response voice. When omitted, the body is honest
        about not having grounded data.
    """
    classification = match_broker_intent(text)
    intent = classification["intent"]

    body = response_for_intent(intent, evidence=evidence)
    body = _enforce_no_forbidden_tokens(body)

    suggestions = next_step_suggestions(intent)

    no_data = (intent in _DATA_DEPENDENT_INTENTS)
    evidence_grounded = bool(
        intent in _EVIDENCE_GROUNDED_INTENTS and evidence is not None
    )

    clarifying: Optional[str] = None
    if intent == INTENT_FALLBACK_CLARIFY:
        # Only ask the clarifying question if the input was
        # truly ambiguous — not for empty / single-keystroke
        # input.
        tokens = classification.get("tokens") or ()
        if len(tokens) >= 2:
            clarifying = _CLARIFYING_QUESTIONS[0]

    return {
        "intent":             intent,
        "score":              int(classification.get("score") or 0),
        "response_text":      body,
        "suggested_next":     suggestions,
        "evidence_grounded":  evidence_grounded,
        "no_data_available":  no_data,
        "clarifying_question": clarifying,
    }
