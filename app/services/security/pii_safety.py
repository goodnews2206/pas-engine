"""PAS211I — PII redaction / masking utilities.

Deterministic, stdlib-only helpers to keep raw contact PII and secret-shaped
strings out of logs, events, and error records — while preserving operational
usefulness (event names, statuses, source labels, booleans, lengths are kept).

Doctrine:
  * **Never logs raw text** during sanitization.
  * **Conservative.** Only phone/email/secret-shaped tokens are masked in free
    text; structured non-PII fields pass through untouched.
  * **Deterministic.** Same input → same output.
"""
from __future__ import annotations

import re
from typing import Any, Dict

# ── patterns ────────────────────────────────────────────────────────
_EMAIL_RE = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}")
# A run that looks like a phone number: optional +, then 7+ digits possibly with
# separators. Kept tight enough to avoid eating ordinary numbers/ids.
_PHONE_RE = re.compile(r"\+?\d[\d\s().\-]{5,}\d")
# Secret-shaped tokens: pas_/orvn_ keys, sk-/xox*- provider keys, JWTs, hashes.
_SECRET_RE = re.compile(
    r"(?:pas_[A-Za-z0-9_\-]{8,}"
    r"|orvn_[A-Za-z0-9_\-]{8,}"
    r"|sk-[A-Za-z0-9]{12,}"
    r"|xox[bsparo]-[A-Za-z0-9\-]{8,}"
    r"|eyJ[A-Za-z0-9_\-]{8,}\.[A-Za-z0-9_\-]{6,}\.[A-Za-z0-9_\-]{6,}"
    r"|sha256\$[a-fA-F0-9]{8,})"
)

# Keys whose VALUE is free-text that may carry spoken PII — replaced with a
# length marker in event/log payload sanitization.
_RAW_TEXT_KEYS = frozenset({
    "raw_text", "text", "transcript", "excerpt", "trigger_excerpt",
    "message_text", "utterance", "objection_text", "callback_reason_excerpt",
})
# Keys whose VALUE is contact PII — masked in payload sanitization.
_PHONE_KEYS = frozenset({"phone", "phone_number", "lead_phone", "caller", "agent_phone", "callee"})
_EMAIL_KEYS = frozenset({"email", "lead_email", "from_email", "recipient"})
_NAME_KEYS = frozenset({"name", "lead_name", "agent_name", "full_name"})


def mask_phone(value: Any) -> str:
    """Mask a phone to first-3 / last-2 of its digits (e.g. +1305...34 → 130***34)."""
    s = str(value or "")
    digits = re.sub(r"\D", "", s)
    if not digits:
        return s
    if len(digits) <= 4:
        return "*" * len(digits)
    return digits[:3] + "*" * (len(digits) - 5) + digits[-2:]


def mask_email(value: Any) -> str:
    """Mask the local part of an email, keep the domain (a@b.com → a***@b.com)."""
    s = str(value or "")
    m = _EMAIL_RE.search(s)
    if not m:
        return s
    local, _, domain = m.group(0).partition("@")
    masked_local = (local[0] + "***") if local else "***"
    return s.replace(m.group(0), f"{masked_local}@{domain}")


def mask_name_if_needed(value: Any) -> str:
    """Keep a given name, drop the rest (Marcus Lee → Marcus ***). Empty → ''."""
    s = str(value or "").strip()
    if not s:
        return ""
    parts = s.split()
    return parts[0] if len(parts) == 1 else f"{parts[0]} ***"


def redact_pii(text: Any) -> str:
    """Redact emails, phones, and secret-shaped tokens from a free-text string."""
    s = str(text or "")
    if not s:
        return s
    s = _SECRET_RE.sub("[secret]", s)
    s = _EMAIL_RE.sub("[email]", s)
    s = _PHONE_RE.sub("[phone]", s)
    return s


def sanitize_error_message(text: Any, *, max_len: int = 1000) -> str:
    """Redact PII/secrets from an error message/detail before it is stored."""
    return redact_pii(text)[:max_len]


def _sanitize_value(key: str, value: Any, depth: int) -> Any:
    if isinstance(value, dict):
        return _sanitize_dict(value, depth + 1)
    if isinstance(value, (list, tuple)):
        return [_sanitize_value(key, v, depth + 1) for v in value]
    if isinstance(value, str):
        k = key.lower()
        if k in _RAW_TEXT_KEYS:
            return f"[redacted:len={len(value)}]"
        if k in _PHONE_KEYS:
            return mask_phone(value)
        if k in _EMAIL_KEYS:
            return mask_email(value)
        if k in _NAME_KEYS:
            return mask_name_if_needed(value)
        return redact_pii(value)
    return value


def _sanitize_dict(payload: Dict[str, Any], depth: int = 0) -> Dict[str, Any]:
    if depth > 6 or not isinstance(payload, dict):
        return payload
    return {k: _sanitize_value(str(k), v, depth) for k, v in payload.items()}


def sanitize_event_payload(payload: Any) -> Any:
    """Sanitize a pas_events payload: replace raw-text keys with a length marker,
    mask contact-PII keys, redact PII patterns from any other string. Structured
    fields (event names, statuses, source labels, booleans, counts) are kept."""
    if not isinstance(payload, dict):
        return payload
    return _sanitize_dict(payload)


# Log payloads use the same rules as events.
sanitize_log_payload = sanitize_event_payload


def sanitize_slack_payload(payload: Any) -> Any:
    """For Slack: redact only SECRET-shaped tokens (lead contact details are an
    intentional, customer-controlled operational handoff — see PAS211I doc), and
    never let a secret slip through."""
    if isinstance(payload, dict):
        return {k: sanitize_slack_payload(v) for k, v in payload.items()}
    if isinstance(payload, (list, tuple)):
        return [sanitize_slack_payload(v) for v in payload]
    if isinstance(payload, str):
        return _SECRET_RE.sub("[secret]", payload)
    return payload


__all__ = (
    "mask_phone",
    "mask_email",
    "mask_name_if_needed",
    "redact_pii",
    "sanitize_error_message",
    "sanitize_event_payload",
    "sanitize_log_payload",
    "sanitize_slack_payload",
)
