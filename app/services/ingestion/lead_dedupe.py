"""PAS213 — deterministic, tenant-scoped lead dedupe (process-local v1).

A repeated digital-lead submission (a form double-post, a forwarder loop, a
manual re-send) must not create two operational records. The dedupe key is
deterministic — it NEVER includes randomness — so two callers given the same
lead under the same tenant compute the same key.

Doctrine:
  * ``brokerage_id`` is required and is part of every key → **no cross-tenant
    dedupe** (and the store is also bucketed per tenant, belt-and-suspenders).
  * Process-local v1: every consumer surfaces the structural warning
    ``lead_dedupe_store_is_process_local`` so the in-memory registry is never
    mistaken for durable. Durable Supabase-backed dedupe is PAS213C.
"""
from __future__ import annotations

import hashlib
import threading
from typing import Dict, Set

from app.services.ingestion.lead_contracts import NormalizedLead

PROCESS_LOCAL_WARNING = "lead_dedupe_store_is_process_local"


def _sha(basis: str) -> str:
    return "dl_" + hashlib.sha256(basis.encode("utf-8")).hexdigest()[:16]


def dedupe_key(brokerage_id: str, lead: NormalizedLead) -> str:
    """Deterministic key. Prefers (tenant, source, external_lead_id); else falls
    back to (tenant, normalized contact, message-hash or received-day)."""
    if lead.external_lead_id:
        basis = f"{brokerage_id}|{lead.source}|ext:{lead.external_lead_id}"
    else:
        contact = lead.phone or lead.email or ""
        message = (lead.message or "").strip().lower()
        if message:
            tail = "msg:" + hashlib.sha256(message.encode("utf-8")).hexdigest()[:12]
        else:
            tail = "day:" + (lead.received_at or "")[:10]
        basis = f"{brokerage_id}|contact:{contact}|{tail}"
    return _sha(basis)


class LeadDedupeStore:
    """Process-local, tenant-bucketed seen-key registry."""

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._by_tenant: Dict[str, Set[str]] = {}

    def is_duplicate(self, brokerage_id: str, key: str) -> bool:
        with self._lock:
            return key in self._by_tenant.get(brokerage_id, set())

    def register(self, brokerage_id: str, key: str) -> None:
        with self._lock:
            self._by_tenant.setdefault(brokerage_id, set()).add(key)


_default_store = LeadDedupeStore()


def default_dedupe_store() -> LeadDedupeStore:
    return _default_store


__all__ = (
    "PROCESS_LOCAL_WARNING",
    "dedupe_key",
    "LeadDedupeStore",
    "default_dedupe_store",
)
