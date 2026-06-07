"""PAS213 — pure lead normalizers.

Every function is a pure function that NEVER raises, even on ``None`` / non-dict
/ malformed input. The top-level ``normalize_digital_lead`` returns a structural
envelope::

    {"status": "ok",     "lead": NormalizedLead, "warnings": [...]}
    {"status": "failed", "errors": [...]}

Phone is required (corpus contract); a payload without a usable phone is a
``failed`` result, not an exception.
"""
from __future__ import annotations

from typing import Any, Dict, List, Mapping

from app.services.ingestion.lead_contracts import (
    KNOWN_PAYLOAD_KEYS,
    NormalizedLead,
    normalize_source,
)


def normalize_phone(raw: Any) -> str:
    """Best-effort E.164-ish normalisation. Returns '' when not derivable."""
    if not raw:
        return ""
    s = str(raw).strip()
    plus = s.startswith("+")
    digits = "".join(ch for ch in s if ch.isdigit())
    if not digits:
        return ""
    if plus:
        return "+" + digits if len(digits) >= 8 else ""
    if len(digits) == 10:  # assume US/CA (this is a US real-estate product)
        return "+1" + digits
    if len(digits) == 11 and digits.startswith("1"):
        return "+" + digits
    if len(digits) >= 8:
        return "+" + digits  # best-effort international without a leading +
    return ""


def normalize_email(raw: Any) -> str:
    if not raw:
        return ""
    s = str(raw).strip().lower()
    if "@" in s and "." in s.split("@")[-1] and 3 <= len(s) <= 254:
        return s
    return ""


def normalize_name(raw: Any) -> str:
    if not raw:
        return ""
    return " ".join(str(raw).split())


def _trim(raw: Any) -> str:
    return "" if raw is None else str(raw).strip()


def normalize_digital_lead(payload: Any) -> Dict[str, Any]:
    """Turn a raw payload dict into a NormalizedLead envelope. Never raises."""
    if not isinstance(payload, Mapping):
        return {"status": "failed", "errors": ["payload_not_an_object"]}

    warnings: List[str] = []
    source, src_warn = normalize_source(payload.get("source"))
    warnings += list(src_warn)

    phone = normalize_phone(payload.get("phone"))
    if not phone:
        return {"status": "failed", "errors": ["missing_or_invalid_phone"]}

    email = normalize_email(payload.get("email"))
    name = normalize_name(payload.get("name"))

    # Preserve any unrecognised keys into metadata (don't lose raw context).
    base_meta = payload.get("metadata")
    metadata: Dict[str, Any] = dict(base_meta) if isinstance(base_meta, Mapping) else {}
    for k, v in payload.items():
        if k not in KNOWN_PAYLOAD_KEYS:
            metadata[k] = v

    lead = NormalizedLead(
        source=source,
        external_lead_id=_trim(payload.get("external_lead_id")),
        name=name,
        phone=phone,
        email=email,
        message=_trim(payload.get("message")),
        budget=_trim(payload.get("budget")),
        timeline=_trim(payload.get("timeline")),
        intent=_trim(payload.get("intent")),
        property_location=_trim(payload.get("property_location")),
        received_at=_trim(payload.get("received_at")),
        raw_source_label=_trim(payload.get("raw_source_label")) or _trim(payload.get("source")),
        metadata=metadata,
        warnings=tuple(warnings),
    )
    return {"status": "ok", "lead": lead, "warnings": warnings}
