"""
Audience-specific translation for workflow steps.

The mapper produces a single canonical workflow object. This module
adapts each step for the consuming surface:

  audience='admin'   → operator vocabulary, raw event_type allowed,
                       provider/system signals retained.
  audience='portal'  → business vocabulary only. No raw event_type.
                       No provider names. Forbidden secret-style keys
                       in safe_metadata are dropped defensively.

Never raises. Always returns a fresh dict — the input workflow is not
mutated.
"""

from copy import deepcopy
from typing import Optional

# Brokerage-facing translations. Keyed by the canonical step key from the
# mapper. Fields not listed here pass through unchanged (label/category/
# order_index/status/timestamp).
_PORTAL_LABEL = {
    "lead_received":      "Lead Received",
    "pas_calling":        "PAS On The Call",
    "intent_captured":    "Lead Detail Captured · Intent",
    "budget_captured":    "Lead Detail Captured · Budget",
    "timeline_captured":  "Lead Detail Captured · Timeline",
    "booking_attempted":  "Booking Requested",
    "booking_confirmed":  "Appointment Confirmed",
    "callback_requested": "Callback Requested",
    "followup_scheduled": "Follow-up Scheduled",
    "completed":          "Conversation Completed",
}

_PORTAL_DETAIL = {
    "lead_received":      "Lead entered the workflow",
    "pas_calling":        "PAS started qualifying the lead",
    "intent_captured":    "PAS captured what the lead is looking for",
    "budget_captured":    "PAS captured the lead's budget",
    "timeline_captured":  "PAS captured the lead's timeline",
    "booking_attempted":  "PAS asked the calendar to schedule a viewing",
    "booking_confirmed":  "Viewing locked into the calendar",
    "callback_requested": "Lead asked PAS to follow up later",
    "followup_scheduled": "Callback time saved for the team",
    "completed":          "PAS finished the conversation with the lead",
}

# Keys we will never expose in any audience's safe_metadata.
_FORBIDDEN_META_KEYS = {
    "api_key", "x_api_key", "x_admin_key", "authorization",
    "secret", "password", "token", "raw_text", "text", "message",
    "transcript", "prompt", "response", "body",
}
_FORBIDDEN_SUBSTRINGS = ("secret", "password", "token", "api_key", "auth")

# Detail string we surface to the brokerage when a provider failure
# materially affected the conversation. Generic — never names Twilio,
# Deepgram, ElevenLabs, Anthropic, Cal.com, etc.
_PORTAL_SYSTEM_DELAY = "PAS recovered from a brief system delay"


def sanitize_meta(meta: Optional[dict]) -> dict:
    """Drop secret-looking keys, truncate long strings, drop nested
    structures. Mirrors the policy used by intelligence.sanitize but
    operates on the small per-step safe_metadata bag instead of full
    pas_events payloads."""
    if not isinstance(meta, dict):
        return {}
    out: dict = {}
    for k, v in meta.items():
        if not isinstance(k, str):
            continue
        kl = k.lower()
        if kl in _FORBIDDEN_META_KEYS:
            continue
        if any(sub in kl for sub in _FORBIDDEN_SUBSTRINGS):
            continue
        if isinstance(v, str):
            if len(v) > 120:
                continue
            out[k] = v
        elif isinstance(v, (int, float, bool)):
            out[k] = v
        # nested dicts/lists deliberately dropped
    return out


def sanitize_workflow_for_audience(workflow: dict, audience: str = "admin") -> dict:
    """
    Return a copy of the workflow object adapted for the given audience.

    Both audiences receive the same step skeleton and same statuses — the
    visible difference is in label/detail/event_type and which system
    signals are surfaced.
    """
    if not isinstance(workflow, dict):
        return {}
    out = deepcopy(workflow)
    aud = (audience or "admin").lower()

    # System signals — admin sees everything. Portal sees a translated
    # boolean cue only.
    sys_sig = out.get("system_signals") or {}
    if aud == "portal":
        had_provider_issue = bool((sys_sig or {}).get("provider_failed_count", 0))
        out["system_signals"] = {"system_delay_observed": had_provider_issue}
    else:
        out["system_signals"] = {
            "provider_failed_count": int(sys_sig.get("provider_failed_count") or 0),
            "system_error_count":    int(sys_sig.get("system_error_count")    or 0),
            "objection_count":       int(sys_sig.get("objection_count")       or 0),
        }

    cleaned_steps = []
    for step in (out.get("steps") or []):
        if not isinstance(step, dict):
            continue
        clean = dict(step)
        clean["safe_metadata"] = sanitize_meta(step.get("safe_metadata"))
        if aud == "portal":
            clean["label"]  = _PORTAL_LABEL.get(step.get("key"), step.get("label") or "")
            clean["detail"] = _PORTAL_DETAIL.get(step.get("key"), step.get("detail") or "")
            # Portal must not see raw event_type strings — they leak
            # implementation vocabulary (state.transition, callback.requested).
            clean.pop("event_type", None)
            # If a portal step shows a system delay, swap detail.
            if had_provider_issue and step.get("key") == "pas_calling" and step.get("status") in {"warning", "failed"}:
                clean["detail"] = _PORTAL_SYSTEM_DELAY
        cleaned_steps.append(clean)
    out["steps"] = cleaned_steps

    # leak_detected_at may stay — it's a step key, not provider detail.
    return out
