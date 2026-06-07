"""PAS213B — durable digital-lead ingestion: persistence, dedupe, events.

Builds on PAS213 (test_pas213_digital_lead_ingestion.py). Focus here is the
durability upgrade:

  * durable dedupe survives a *new store instance* (proxy for a process restart)
  * dedupe stays tenant-scoped when durable
  * the durable store is the service default (process-local warning gone)
  * full event lifecycle: lead.ingested / lead.duplicate / lead.rejected
  * no raw PII (phone/email/name/message) in any event payload
  * the durable store and ingestion modules import nothing outbound
  * the migration proposal exists for the schema gap (and is not auto-applied)
"""
import ast
import inspect
import os

import pytest

from app.services.ingestion import lead_dedupe as dd
from app.services.ingestion import lead_ingestion as svc
from app.services.ingestion import lead_normalizers as norm
from app.services.ingestion import lead_contracts as lc
from app.services.ingestion.lead_dedupe import (
    SupabaseLeadDedupeStore,
    default_durable_dedupe_store,
)
from app.services.ingestion.lead_ingestion import ingest_digital_lead

BRK_A = {"id": "brk-A"}
BRK_B = {"id": "brk-B"}

REPO_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
)


# ── A minimal in-memory Supabase double with a real UNIQUE constraint ──
# Emulates just the verbs the durable store uses: table().select().eq()
# .eq().limit().execute() and table().insert().execute(), enforcing
# UNIQUE(brokerage_id, dedupe_key) so the race backstop is exercised.
class _Result:
    def __init__(self, data):
        self.data = data


class _Query:
    def __init__(self, table):
        self._table = table
        self._filters = {}
        self._limit = None

    def select(self, *a, **k):
        return self

    def eq(self, col, val):
        self._filters[col] = val
        return self

    def limit(self, n):
        self._limit = n
        return self

    def execute(self):
        rows = [
            r for r in self._table.rows
            if all(r.get(c) == v for c, v in self._filters.items())
        ]
        if self._limit is not None:
            rows = rows[: self._limit]
        return _Result(list(rows))


class _Insert:
    def __init__(self, table, row):
        self._table = table
        self._row = row

    def execute(self):
        for r in self._table.rows:
            if (r.get("brokerage_id") == self._row.get("brokerage_id")
                    and r.get("dedupe_key") == self._row.get("dedupe_key")):
                raise Exception("duplicate key value violates unique constraint")
        self._table.rows.append(dict(self._row))
        return _Result([dict(self._row)])


class _Table:
    def __init__(self, store, name):
        self._store = store
        self.name = name

    @property
    def rows(self):
        return self._store.tables.setdefault(self.name, [])

    def select(self, *a, **k):
        return _Query(self)

    def insert(self, row):
        return _Insert(self, row)


class FakeSupabase:
    def __init__(self):
        self.tables = {}

    def table(self, name):
        return _Table(self, name)


class _Recorder:
    def __init__(self):
        self.writes = []
        self.events = []

    def writer(self, brokerage_id, phone, updates):
        self.writes.append((brokerage_id, phone, dict(updates)))

    def sink(self, event_type, **kw):
        self.events.append((event_type, kw))


def _durable(fake):
    return SupabaseLeadDedupeStore(client_factory=lambda: fake)


def _ingest(payload, *, brokerage=BRK_A, store=None, rec=None):
    rec = rec or _Recorder()
    res = ingest_digital_lead(
        payload, brokerage=brokerage, dedupe_store=store,
        lead_writer=rec.writer, event_sink=rec.sink,
    )
    return res, rec


# ── persistence ────────────────────────────────────────────────────
def test_durable_writer_called_on_accepted_lead():
    fake = FakeSupabase()
    res, rec = _ingest(
        {"source": "website_form", "phone": "2125551234", "name": "Marcus"},
        store=_durable(fake),
    )
    assert res["status"] == "ingested"
    assert res["lead_created"] is True
    assert rec.writes and rec.writes[0][0] == "brk-A"
    assert rec.writes[0][1] == "+12125551234"
    # durable store recorded the key durably (one ledger row)
    assert len(fake.tables.get(dd.DEDUPE_TABLE, [])) == 1


# ── durable dedupe survives a new store instance (restart proxy) ────
def test_durable_dedupe_survives_new_store_instance():
    fake = FakeSupabase()
    p = {"source": "realtor_com", "phone": "2125551234", "external_lead_id": "RC-1"}

    res1, rec1 = _ingest(p, store=_durable(fake))           # first store instance
    res2, rec2 = _ingest(p, store=_durable(fake))           # brand-new instance, same DB

    assert res1["status"] == "ingested"
    assert res2["status"] == "duplicate"
    assert res2["dedupe_key"] == res1["dedupe_key"]
    assert rec2.writes == []                                # not written again


def test_durable_dedupe_is_tenant_scoped():
    fake = FakeSupabase()
    p = {"source": "zillow", "phone": "2125551234", "message": "interested"}
    res_a, _ = _ingest(p, brokerage=BRK_A, store=_durable(fake))
    res_b, _ = _ingest(p, brokerage=BRK_B, store=_durable(fake))
    assert res_a["status"] == "ingested"
    assert res_b["status"] == "ingested"          # other tenant → not a duplicate
    assert res_a["dedupe_key"] != res_b["dedupe_key"]


def test_durable_store_fails_open_on_db_error():
    # A client that raises on every call → store must treat lead as new, never
    # drop it. (Mirrors the table-not-yet-migrated / transient-outage case.)
    class _Broken:
        def table(self, *_a, **_k):
            raise RuntimeError("supabase down")

    res, rec = _ingest(
        {"source": "manual", "phone": "2125551234"},
        store=SupabaseLeadDedupeStore(client_factory=lambda: _Broken()),
    )
    assert res["status"] == "ingested"
    assert rec.writes and rec.writes[0][1] == "+12125551234"


# ── default is durable (route relies on service defaults) ───────────
def test_durable_store_is_service_default():
    assert default_durable_dedupe_store().durable is True
    # No injected dedupe_store ⇒ service resolves the durable default, so the
    # process-local warning must NOT appear (durable store, fails open if the
    # live client is unavailable in the test env).
    rec = _Recorder()
    res = ingest_digital_lead(
        {"source": "manual", "phone": "2125551234"},
        brokerage=BRK_A, lead_writer=rec.writer, event_sink=rec.sink,
    )
    assert res["status"] == "ingested"
    assert dd.PROCESS_LOCAL_WARNING not in res.get("warnings", [])


def test_route_relies_on_service_default_dedupe():
    import app.routes.lead_ingestion as route_mod
    src = inspect.getsource(route_mod.ingest_lead)
    # The route must not pin a process-local store; it delegates to the
    # service's durable default.
    assert "dedupe_store" not in src


# ── event lifecycle ────────────────────────────────────────────────
def test_accepted_lead_emits_ingested_event():
    fake = FakeSupabase()
    res, rec = _ingest(
        {"source": "facebook", "phone": "2125551234", "email": "a@b.com"},
        store=_durable(fake),
    )
    assert res["status"] == "ingested"
    types = [e[0] for e in rec.events]
    assert "lead.ingested" in types
    ev = next(kw for t, kw in rec.events if t == "lead.ingested")
    assert ev["brokerage_id"] == "brk-A"
    assert ev["event_source"] == "digital_ingestion"
    assert ev["payload"]["has_email"] is True


def test_duplicate_emits_duplicate_event():
    fake = FakeSupabase()
    p = {"source": "zillow", "phone": "2125551234", "message": "123 Main"}
    _ingest(p, store=_durable(fake))
    res2, rec2 = _ingest(p, store=_durable(fake))
    assert res2["status"] == "duplicate"
    types = [e[0] for e in rec2.events]
    assert types == ["lead.duplicate"]
    ev = rec2.events[0][1]
    assert ev["event_source"] == "digital_ingestion"
    assert ev["payload"]["dedupe_key"] == res2["dedupe_key"]


def test_rejected_lead_emits_safe_event():
    res, rec = _ingest({"source": "website_form", "name": "No Phone"})
    assert res["status"] == "rejected"
    types = [e[0] for e in rec.events]
    assert types == ["lead.rejected"]
    payload = rec.events[0][1]["payload"]
    assert payload["reason"] == "normalization_failed"
    assert "missing_or_invalid_phone" in payload["errors"]


def test_tenant_mismatch_emits_rejected_event():
    res, rec = _ingest(
        {"source": "manual", "phone": "2125551234", "brokerage_id": "brk-EVIL"}
    )
    assert res["status"] == "failed" and res["error"] == "tenant_mismatch"
    assert rec.writes == []
    assert [e[0] for e in rec.events] == ["lead.rejected"]
    assert rec.events[0][1]["payload"]["reason"] == "tenant_mismatch"


def test_tenant_unresolved_emits_no_event():
    # No tenant ⇒ nothing to scope an event to ⇒ emit nothing.
    res, rec = _ingest({"source": "manual", "phone": "2125551234"},
                       brokerage={"id": ""})
    assert res["status"] == "failed" and res["error"] == "tenant_unresolved"
    assert rec.events == []


# ── PII safety across every emitted event ──────────────────────────
def test_no_raw_pii_in_any_event_payload():
    fake = FakeSupabase()
    phone_raw, email_raw = "2125551234", "marcus@example.com"
    p = {
        "source": "website_form", "phone": phone_raw, "email": email_raw,
        "name": "Marcus Lee", "message": "looking in Brooklyn",
        "external_lead_id": "WF-7",
    }
    rec = _Recorder()
    _ingest(p, store=_durable(fake), rec=rec)               # ingested
    _ingest(p, store=_durable(fake), rec=rec)               # duplicate
    _ingest({"source": "manual", "name": "x"}, rec=rec)     # rejected (no phone)

    assert {e[0] for e in rec.events} == {
        "lead.ingested", "lead.duplicate", "lead.rejected"
    }
    forbidden_keys = {"phone", "email", "name", "message", "notes"}
    norm_phone = norm.normalize_phone(phone_raw)
    for _type, kw in rec.events:
        payload = kw["payload"]
        assert forbidden_keys.isdisjoint(payload.keys())
        blob = repr(payload)
        assert phone_raw not in blob and norm_phone not in blob
        assert email_raw not in blob
        assert "Marcus" not in blob and "Brooklyn" not in blob


# ── no outbound imports anywhere in the ingestion package ──────────
def test_durable_modules_have_no_outbound_or_engine_imports():
    for mod in (svc, norm, lc, dd):
        tree = ast.parse(inspect.getsource(mod))
        imported = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported += [a.name for a in node.names]
            elif isinstance(node, ast.ImportFrom):
                imported.append(node.module or "")
        joined = " ".join(imported)
        for bad in ("twilio", "calcom", "state_machine", "websocket_handler", "outbound"):
            assert bad not in joined, f"{mod.__name__} must not import {bad}"


# ── the migration proposal exists for the schema gap ───────────────
def test_migration_proposal_exists_and_is_safe():
    path = os.path.join(
        REPO_ROOT, "scripts", "migrate_v8_digital_ingestion_dedupe.sql"
    )
    assert os.path.isfile(path), "PAS213B durable dedupe migration proposal missing"
    sql = open(path, encoding="utf-8").read()
    assert "lead_ingestion_dedupe" in sql
    assert "CREATE TABLE IF NOT EXISTS" in sql            # idempotent-safe
    assert "UNIQUE (brokerage_id, dedupe_key)" in sql     # tenant-scoped race backstop
