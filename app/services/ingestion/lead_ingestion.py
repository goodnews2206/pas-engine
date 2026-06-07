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
``lead_writer`` (defaults to lead_memory.upsert_lead — a durable, tenant-scoped
write into the ``leads`` table that PAS210 reads), ``event_sink`` (defaults to
event_logger.log_event_bg — a durable append into ``pas_events``), and
``dedupe_store`` (PAS213B default: the durable Supabase-backed store).

PAS213B — durability:
  * Dedupe defaults to :class:`SupabaseLeadDedupeStore` so duplicates are
    detected across process restarts (was process-local in PAS213). Injecting a
    :class:`LeadDedupeStore` keeps the process-local v1 behaviour (and surfaces
    the ``lead_dedupe_store_is_process_local`` warning).
  * Events are emitted for the full lifecycle: ``lead.ingested``,
    ``lead.duplicate``, and ``lead.rejected`` — all PII-free (structural facts
    and an opaque dedupe-key hash only).
"""
from __future__ import annotations

import logging
from typing import Any, Callable, Dict, Mapping, Optional

from app.services.ingestion.lead_contracts import normalize_source
from app.services.ingestion.lead_dedupe import (
    PROCESS_LOCAL_WARNING,
    LeadDedupeStore,
    dedupe_key,
    default_durable_dedupe_store,
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


def _safe_source_label(payload: Any) -> Optional[str]:
    """Closed-vocabulary source label for an event payload — never raw PII."""
    if not isinstance(payload, Mapping):
        return None
    source, _ = normalize_source(payload.get("source"))
    return source


def _emit(
    sink: "EventSink",
    event_type: str,
    tenant: str,
    *,
    severity: str = "info",
    payload: Dict[str, Any],
) -> None:
    """Emit a structural ingestion event. Never raises; never carries raw PII."""
    try:
        sink(
            event_type,
            brokerage_id=tenant,
            event_category="lead",
            event_source=SOURCE_MODE,
            severity=severity,
            payload=payload,
        )
    except Exception:
        logger.warning("digital lead event emit failed (%s)", event_type, exc_info=False)


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
    sink = event_sink or _default_event_sink

    # 1. Tenant resolution — fail closed. No tenant ⇒ nothing to scope an event
    #    to, so emit nothing (a tenant-less event would violate isolation).
    tenant = str((brokerage or {}).get("id") or "").strip()
    if not tenant or tenant == "demo":
        return _result("failed", None, error="tenant_unresolved")

    # 2. Reject a payload that claims a different tenant (no silent override).
    if isinstance(payload, Mapping):
        claimed = str(payload.get("brokerage_id") or "").strip()
        if claimed and claimed != tenant:
            _emit(sink, "lead.rejected", tenant, severity="warning", payload={
                "reason": "tenant_mismatch",
                "claimed_brokerage_id": claimed,  # a tenant id, not PII
                "source": _safe_source_label(payload),
            })
            return _result("failed", tenant, error="tenant_mismatch")

    # 3. Normalize (pure, never raises).
    norm = normalize_digital_lead(payload)
    if norm.get("status") != "ok":
        errors = norm.get("errors", [])
        _emit(sink, "lead.rejected", tenant, payload={
            "reason": "normalization_failed",
            "errors": errors,
            "source": _safe_source_label(payload),
        })
        return _result("rejected", tenant, errors=errors)
    lead = norm["lead"]

    # 4. Dedupe (tenant-scoped, deterministic, idempotent). Durable by default
    #    (PAS213B); a process-local store surfaces the structural warning.
    store = dedupe_store or default_durable_dedupe_store()
    warnings = list(norm.get("warnings", []))
    if not getattr(store, "durable", False):
        warnings.append(PROCESS_LOCAL_WARNING)
    key = dedupe_key(tenant, lead)
    if store.is_duplicate(tenant, key):
        _emit(sink, "lead.duplicate", tenant, payload={
            "source": lead.source,
            "raw_source_label": lead.raw_source_label,
            "external_lead_id": lead.external_lead_id or None,
            "dedupe_key": key,
        })
        return _result(
            "duplicate", tenant, dedupe_key=key, source=lead.source,
            lead_created=False, warnings=warnings,
        )

    # 5. Persist the lead (tenant-scoped) via the existing durable leads writer.
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

    # 6. Durably record the dedupe key only after the lead is persisted, so a
    #    write failure can't strand a key and silently drop a legitimate retry.
    store.register(
        tenant, key,
        source=lead.source,
        external_lead_id=lead.external_lead_id or None,
    )

    # 7. Emit a structural event (no phone/email/raw PII in the payload).
    _emit(sink, "lead.ingested", tenant, payload={
        "source": lead.source,
        "raw_source_label": lead.raw_source_label,
        "external_lead_id": lead.external_lead_id or None,
        "dedupe_key": key,
        "has_email": bool(lead.email),
        "has_message": bool(lead.message),
        "lead_created": lead_created,
    })

    return _result(
        "ingested", tenant, dedupe_key=key, source=lead.source,
        lead_created=lead_created, warnings=warnings,
    )


__all__ = ("SOURCE_MODE", "ingest_digital_lead")
