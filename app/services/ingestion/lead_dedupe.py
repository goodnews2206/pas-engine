"""PAS213 — deterministic, tenant-scoped lead dedupe.

A repeated digital-lead submission (a form double-post, a forwarder loop, a
manual re-send) must not create two operational records. The dedupe key is
deterministic — it NEVER includes randomness — so two callers given the same
lead under the same tenant compute the same key.

Doctrine:
  * ``brokerage_id`` is required and is part of every key → **no cross-tenant
    dedupe** (and every store is also bucketed/filtered per tenant,
    belt-and-suspenders).
  * Two store implementations share one interface (``is_duplicate`` /
    ``register`` + a ``durable`` flag):
      - :class:`LeadDedupeStore` — process-local v1. Surfaces the structural
        warning ``lead_dedupe_store_is_process_local`` so the in-memory
        registry is never mistaken for durable.
      - :class:`SupabaseLeadDedupeStore` — **PAS213B** durable store backed by
        the ``lead_ingestion_dedupe`` table (see
        ``scripts/migrate_v8_digital_ingestion_dedupe.sql``). Survives process
        restart; the ``UNIQUE(brokerage_id, dedupe_key)`` constraint is the
        race backstop; fails **open** (treats the lead as new) on any DB error
        so a transient outage never silently drops a paying client's lead.
"""
from __future__ import annotations

import hashlib
import logging
import threading
from typing import Any, Callable, Dict, Optional, Set

from app.services.ingestion.lead_contracts import NormalizedLead

logger = logging.getLogger("pas.ingestion.dedupe")

PROCESS_LOCAL_WARNING = "lead_dedupe_store_is_process_local"

# Durable store backing table — created by the (un-applied) PAS213B migration
# proposal scripts/migrate_v8_digital_ingestion_dedupe.sql.
DEDUPE_TABLE = "lead_ingestion_dedupe"


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
    """Process-local, tenant-bucketed seen-key registry (PAS213 v1).

    Not durable: the registry is lost on restart. Consumers surface
    ``PROCESS_LOCAL_WARNING`` whenever this store is used.
    """

    durable = False

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._by_tenant: Dict[str, Set[str]] = {}

    def is_duplicate(self, brokerage_id: str, key: str) -> bool:
        with self._lock:
            return key in self._by_tenant.get(brokerage_id, set())

    def register(self, brokerage_id: str, key: str, **meta: Any) -> None:
        # ``meta`` (source / external_lead_id / lead_id) is accepted for
        # interface parity with the durable store and intentionally ignored.
        with self._lock:
            self._by_tenant.setdefault(brokerage_id, set()).add(key)


class SupabaseLeadDedupeStore:
    """Durable, tenant-scoped dedupe backed by ``lead_ingestion_dedupe`` (PAS213B).

    Restart-survival: the seen-key set lives in Postgres, not in process memory.
    Tenant isolation: every read filters on ``brokerage_id`` and every write
    carries it; the ``UNIQUE(brokerage_id, dedupe_key)`` constraint means a key
    seen under one tenant can never dedupe another tenant's lead.

    Failure posture (deliberate): on ANY Supabase error — table not yet created
    because the migration is unapplied, transient network failure, etc. — the
    store **fails open**: ``is_duplicate`` returns False and ``register`` is a
    best-effort insert. Failing open can let a rare duplicate through, but it
    never silently *loses* a lead, which is the stronger guarantee a paying
    brokerage needs.

    A client object is injected (production passes the singleton from
    ``app.db.supabase_client``); tests inject a stub. The live client is
    resolved lazily so importing this module never requires an initialised DB.
    """

    durable = True

    def __init__(self, client_factory: Optional[Callable[[], Any]] = None) -> None:
        self._client_factory = client_factory

    def _client(self) -> Any:
        if self._client_factory is not None:
            return self._client_factory()
        from app.db.supabase_client import get_supabase

        return get_supabase()

    @staticmethod
    def _rows(result: Any) -> Any:
        rows = getattr(result, "data", None)
        if rows is None and isinstance(result, dict):
            rows = result.get("data")
        return rows

    def is_duplicate(self, brokerage_id: str, key: str) -> bool:
        try:
            db = self._client()
            result = (
                db.table(DEDUPE_TABLE)
                .select("dedupe_key")
                .eq("brokerage_id", brokerage_id)
                .eq("dedupe_key", key)
                .limit(1)
                .execute()
            )
            return bool(self._rows(result))
        except Exception as e:  # fail open — never drop a lead on a lookup error
            logger.warning(
                "durable dedupe lookup unavailable; failing open (treating as new): %s", e
            )
            return False

    def register(self, brokerage_id: str, key: str, **meta: Any) -> None:
        row: Dict[str, Any] = {"brokerage_id": brokerage_id, "dedupe_key": key}
        for fld in ("source", "external_lead_id", "lead_id"):
            val = meta.get(fld)
            if val:
                row[fld] = val
        try:
            db = self._client()
            # Insert is the source of truth; the UNIQUE(brokerage_id, dedupe_key)
            # constraint rejects a concurrent/duplicate registration, which we
            # swallow — the key is already durably recorded either way.
            db.table(DEDUPE_TABLE).insert(row).execute()
        except Exception as e:
            logger.warning(
                "durable dedupe register skipped (key already recorded or table "
                "unavailable — apply scripts/migrate_v8_digital_ingestion_dedupe.sql): %s",
                e,
            )


_default_store = LeadDedupeStore()
_default_durable_store = SupabaseLeadDedupeStore()


def default_dedupe_store() -> LeadDedupeStore:
    """Process-local store (PAS213 default; retained for back-compat)."""
    return _default_store


def default_durable_dedupe_store() -> SupabaseLeadDedupeStore:
    """Durable store — the PAS213B production default for the ingestion path."""
    return _default_durable_store


__all__ = (
    "PROCESS_LOCAL_WARNING",
    "DEDUPE_TABLE",
    "dedupe_key",
    "LeadDedupeStore",
    "SupabaseLeadDedupeStore",
    "default_dedupe_store",
    "default_durable_dedupe_store",
)
