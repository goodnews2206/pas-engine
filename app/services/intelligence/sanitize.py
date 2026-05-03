"""
Portal payload sanitiser.

Strips PII / provider detail before returning pas_events rows to the
brokerage portal. Admin routes do NOT use this — admin sees full payloads.

Defensive defaults:
  - Top-level fields not on the safe-list are dropped.
  - Payload fields on the deny-list are dropped.
  - Any payload key whose name contains 'secret', 'token', 'password',
    'api_key', or 'auth' is dropped even if not explicitly listed.
  - Free-form strings longer than 200 chars are dropped (categorical
    fields are short enums; long strings are likely free text).
  - Dicts and lists are sanitised recursively.

The input row is never mutated — a new dict is returned.
"""

from typing import Any

# Fields that are always safe to pass through at the top level.
_SAFE_TOP_LEVEL = {
    "event_type", "event_category", "event_source", "severity", "state",
    "call_id", "lead_id", "brokerage_id", "agent_id", "provider", "created_at",
}

# Top-level keys that must never appear in portal output regardless of source.
_FORBIDDEN_TOP_LEVEL = {"api_key", "x_api_key", "x_admin_key", "authorization"}

# Payload keys that must always be dropped.
_FORBIDDEN_PAYLOAD_FIELDS = {
    "text",
    "raw_text",
    "trigger_excerpt",
    "detail_excerpt",
    "message",
    "error",
    "stack_trace",
    "traceback",
    "api_key",
    "x_api_key",
    "x_admin_key",
    "authorization",
    "secret",
    "password",
    "token",
}

# Substrings that, if present in a payload key name, force a drop. Catches
# fields not in the explicit list (e.g. "twilio_auth_token", "user_secret").
_FORBIDDEN_KEY_SUBSTRINGS = ("secret", "password", "token", "api_key", "auth")

# Soft cap — any free-form string longer than this is dropped from payload.
_PAYLOAD_STRING_MAX = 200


def sanitize_event_for_portal(event_row: Any) -> dict:
    """
    Return a sanitised copy of a pas_events row safe to return to the
    brokerage portal. Always returns a dict (empty if input is not a mapping).
    """
    if not isinstance(event_row, dict):
        return {}

    out: dict = {}
    for k, v in event_row.items():
        if not isinstance(k, str):
            continue
        kl = k.lower()
        if kl in _FORBIDDEN_TOP_LEVEL:
            continue
        if k == "payload":
            out["payload"] = _sanitize_payload(v)
            continue
        if k in _SAFE_TOP_LEVEL:
            out[k] = v
        # Anything else: drop silently. Better to under-share than over-share.
    return out


def _sanitize_payload(payload: Any) -> dict:
    if not isinstance(payload, dict):
        return {}
    cleaned: dict = {}
    for k, v in payload.items():
        if not isinstance(k, str):
            continue
        kl = k.lower()
        if kl in _FORBIDDEN_PAYLOAD_FIELDS:
            continue
        if any(token in kl for token in _FORBIDDEN_KEY_SUBSTRINGS):
            continue
        if isinstance(v, str):
            if len(v) > _PAYLOAD_STRING_MAX:
                continue
            cleaned[k] = v
        elif isinstance(v, dict):
            cleaned[k] = _sanitize_payload(v)
        elif isinstance(v, list):
            cleaned[k] = [
                _sanitize_payload(x) if isinstance(x, dict)
                else x
                for x in v
                if not (isinstance(x, str) and len(x) > _PAYLOAD_STRING_MAX)
            ]
        else:
            cleaned[k] = v
    return cleaned
