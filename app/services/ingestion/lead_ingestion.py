"""PAS213 — digital lead ingestion service.

Service-first entry point: takes an authenticated brokerage + a raw digital lead
payload, normalizes, dedupes, writes a tenant-scoped lead record, and emits an
operational event — returning a source-transparent envelope.

Safety doctrine:
  * **Tenant from auth only.** ``brokerage_id`` is the authenticated brokerage's
    id; any ``brokerage_id`` in the payload is only allowed to *match* it (else
    rejected). Never inferred.
  * **No outbound call.** This service imports nothing from Twilio / the call
    engine and never dials. Pending-call enqueue is deferred (PAS213C).
  * **No automatic memory approval**, no behaviour change outside ingestion.
  * **No secrets/PII in the event payload** — only structural facts.

Dependencies are injectable so the service is unit-testable without a DB:
``lead_writer`` (defaults to lead_memory.upsert_lead), ``event_sink`` (defaults
to event_logger.log_event_bg), ``dedupe_store`` (defaults to the process-local
registry).
"""
from __future__ import annotations

import logging
from typing import Any, Callable, Dict, Mapping, Optional

from app.services.ingestion.lead_dedupe import (
    PROCESS_LOCAL_WARNING,
    LeadDedupeStore,
    dedupe_key,
    default_dedupe_store,
)
from app.services.ingestion.lead_normalizers import normalize_digital_lead

logger = logging.getLogger("pas.ingestion.lead")

SOURCE_MODE = "digital_ingestion"

LeadWriter = Callable[..., Any]
EventSink = Callable[..., Any]


def _default_lead_writer(brokerage_id: str, phone: str, updates: Dict[str, Any]) -> Any:
    from app.db.lead_memory import upsert_lead

    return upsert_lead(brokerage_id, phone, updates)


def _default_event_sink(*args: Any, **kwargs: Any) -> Any:
    from app.db.event_logger import log_event_bg

    return log_event_bg(*args, **kwargs)


def _result(status: str, brokerage_id: Optional[str], **extra: Any) -> Dict[str, Any]:
    base = {"status": status, "source_mode": SOURCE_MODE, "brokerage_id": brokerage_id}
    base.update(extra)
    return base


def ingest_digital_lead(
    payload: Any,
    *,
    brokerage: Optional[Mapping[str, Any]],
    dedupe_store: Optional[LeadDedupeStore] = None,
    lead_writer: Optional[LeadWriter] = None,
    event_sink: Optional[EventSink] = None,
) -> Dict[str, Any]:
    """Ingest one digital lead. Returns a source-transparent envelope; never
    raises for normal control flow."""
    # 1. Tenant resolution — fail closed.
    tenant = str((brokerage or {}).get("id") or "").strip()
    if not tenant or tenant == "demo":
        return _result("failed", None, error="tenant_unresolved")

    # 2. Reject a payload that claims a different tenant (no silent override).
    if isinstance(payload, Mapping):
        claimed = str(payload.get("brokerage_id") or "").strip()
        if claimed and claimed != tenant:
            return _result("failed", tenant, error="tenant_mismatch")

    # 3. Normalize (pure, never raises).
    norm = normalize_digital_lead(payload)
    if norm.get("status") != "ok":
        return _result("rejected", tenant, errors=norm.get("errors", []))
    lead = norm["lead"]
    warnings = list(norm.get("warnings", [])) + [PROCESS_LOCAL_WARNING]

    # 4. Dedupe (tenant-scoped, deterministic, idempotent).
    store = dedupe_store or default_dedupe_store()
    key = dedupe_key(tenant, lead)
    if store.is_duplicate(tenant, key):
        return _result(
            "duplicate", tenant, dedupe_key=key, source=lead.source,
            lead_created=False, warnings=warnings,
        )

    # 5. Persist the lead (tenant-scoped) via the existing leads pattern.
    writer = lead_writer or _default_lead_writer
    updates = {
        "name": lead.name,
        "email": lead.email,
        "intent": lead.intent,
        "budget": lead.budget,
        "timeline": lead.timeline,
        "source": lead.source,
        "property_interest": lead.property_location,
    }
    if lead.message:
        updates["notes"] = lead.message
    updates = {k: v for k, v in updates.items() if v}
    try:
        writer(tenant, lead.phone, updates)
        lead_created = True
    except Exception:  # writer should be defensive; never fail ingestion on it
        logger.warning("digital lead writer failed; recording event only", exc_info=False)
        lead_created = False

    store.register(tenant, key)

    # 6. Emit a structural event (no phone/email/raw PII in the payload).
    sink = event_sink or _default_event_sink
    try:
        sink(
            "lead.ingested",
            brokerage_id=tenant,
            event_category="lead",
            event_source=SOURCE_MODE,
            severity="info",
            payload={
                "source": lead.source,
                "raw_source_label": lead.raw_source_label,
                "external_lead_id": lead.external_lead_id or None,
                "dedupe_key": key,
                "has_email": bool(lead.email),
                "has_message": bool(lead.message),
                "lead_created": lead_created,
            },
        )
    except Exception:
        logger.warning("digital lead event emit failed", exc_info=False)

    return _result(
        "ingested", tenant, dedupe_key=key, source=lead.source,
        lead_created=lead_created, warnings=warnings,
    )


__all__ = ("SOURCE_MODE", "ingest_digital_lead")
