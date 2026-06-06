"""PAS213 — digital lead ingestion contracts.

Pure dataclasses / enums / validation. No I/O. Defines the public input shape
(`DigitalLeadPayload` fields) and the canonical `NormalizedLead` that the
pipeline produces.

Doctrine (from the corpus `contracts` spec):
  * ``phone`` is required (the leads table + call paths are phone-keyed).
  * ``source`` is required.
  * ``brokerage_id`` is **never** a field on the normalized lead — tenant scope
    is resolved from auth, so carrying it here would invite a payload-trust
    regression.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, Tuple

# Closed source vocabulary.
SOURCE_WEBSITE_FORM = "website_form"
SOURCE_ZILLOW = "zillow"
SOURCE_REALTOR = "realtor_com"
SOURCE_FACEBOOK = "facebook"
SOURCE_MANUAL = "manual"
SOURCE_EMAIL_FORWARDER = "email_forwarder"
ALL_SOURCES = (
    SOURCE_WEBSITE_FORM,
    SOURCE_ZILLOW,
    SOURCE_REALTOR,
    SOURCE_FACEBOOK,
    SOURCE_MANUAL,
    SOURCE_EMAIL_FORWARDER,
)

# Recognised input keys (anything else is preserved into metadata).
KNOWN_PAYLOAD_KEYS = (
    "brokerage_id",  # accepted only for an auth cross-check; never trusted as tenant
    "source",
    "external_lead_id",
    "name",
    "phone",
    "email",
    "message",
    "budget",
    "timeline",
    "intent",
    "property_location",
    "received_at",
    "raw_source_label",
    "metadata",
)


@dataclass(frozen=True)
class NormalizedLead:
    """Canonical lead shape. Deliberately carries NO brokerage_id."""

    source: str
    external_lead_id: str = ""
    name: str = ""
    phone: str = ""        # required, E.164-ish; empty == invalid
    email: str = ""
    message: str = ""
    budget: str = ""
    timeline: str = ""
    intent: str = ""
    property_location: str = ""
    received_at: str = ""
    raw_source_label: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)
    warnings: Tuple[str, ...] = ()


def normalize_source(raw: Any) -> Tuple[str, Tuple[str, ...]]:
    """Map an input source to the closed vocabulary. Unknown → 'manual' with a
    structural warning. Never raises."""
    s = str(raw or "").strip().lower()
    if s in ALL_SOURCES:
        return s, ()
    return SOURCE_MANUAL, ("unknown_source_mapped_to_manual",)
