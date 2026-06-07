"""PAS211E — tenant isolation / RLS hardening.

Proves the PAS211C tenancy findings are closed:
  * intelligence queries fail CLOSED on a missing tenant scope (no silent global
    reads) and return only the scoped tenant's rows when a brokerage_id is given;
  * agent + booking store helpers enforce a brokerage_id predicate so a
    cross-tenant read returns none and a cross-tenant update/delete changes
    nothing;
  * the PAS210 snapshot adapter still requires a brokerage_id;
  * ingestion stays tenant-pinned and memory retrieval/context stay
    tenant-isolated;
  * the RLS policy migration proposal exists, contains real policies, documents
    the service-role limitation, and has no destructive SQL.

All DB access is modelled by an in-memory fake client — no network.
"""
import os
import re

import pytest


# ── in-memory Supabase double that honours .eq() filters ───────────
class _Res:
    def __init__(self, data):
        self.data = data


class _Q:
    def __init__(self, rows, op):
        self._rows = rows           # live reference to the table list
        self._op = op
        self._payload = None
        self._filters = {}
        self._limit = None

    # query builders (all chainable; order/range are no-ops for the test)
    def select(self, *a, **k):
        return self

    def update(self, payload):
        self._op, self._payload = "update", payload
        return self

    def delete(self):
        self._op = "delete"
        return self

    def eq(self, col, val):
        self._filters[col] = val
        return self

    def in_(self, col, vals):
        self._filters.setdefault("_in", []).append((col, set(vals)))
        return self

    def order(self, *a, **k):
        return self

    def range(self, *a, **k):
        return self

    def gte(self, *a, **k):
        return self

    def limit(self, n):
        self._limit = n
        return self

    def _match(self, r):
        for c, v in self._filters.items():
            if c == "_in":
                if not all(r.get(col) in vals for col, vals in v):
                    return False
            elif r.get(c) != v:
                return False
        return True

    def execute(self):
        matched = [r for r in self._rows if self._match(r)]
        if self._op == "update":
            for r in matched:
                r.update(self._payload)
            return _Res(list(matched))
        if self._op == "delete":
            keep_ids = {id(m) for m in matched}
            self._rows[:] = [r for r in self._rows if id(r) not in keep_ids]
            return _Res(list(matched))
        data = matched[: self._limit] if self._limit else list(matched)
        return _Res(data)


class _Table:
    def __init__(self, rows):
        self._rows = rows

    def select(self, *a, **k):
        return _Q(self._rows, "select")

    def update(self, payload):
        q = _Q(self._rows, "update")
        q._payload = payload
        return q

    def delete(self):
        return _Q(self._rows, "delete")


class FakeDB:
    def __init__(self):
        self.tables = {}

    def seed(self, name, rows):
        self.tables[name] = [dict(r) for r in rows]
        return self

    def table(self, name):
        return _Table(self.tables.setdefault(name, []))


# ── intelligence queries: fail-closed + scoped ─────────────────────
def test_intelligence_queries_fail_closed_without_tenant():
    from app.services.intelligence import queries as q
    # No brokerage_id and no allow_global → empty, never the global stream.
    assert q.recent_events() == []
    assert q.callback_events() == []
    assert q.events_for_call("CA1") == []
    assert q.fetch_call_and_lead_context(["CA1"], ["L1"]) == ({}, {})


def test_intelligence_recent_events_scoped_to_tenant(monkeypatch):
    from app.services.intelligence import queries as q
    db = FakeDB().seed("pas_events", [
        {"id": 1, "brokerage_id": "brk-A", "event_type": "lead.ingested"},
        {"id": 2, "brokerage_id": "brk-B", "event_type": "lead.ingested"},
    ])
    monkeypatch.setattr(q, "get_supabase", lambda: db)
    rows = q.recent_events(brokerage_id="brk-A")
    assert {r["brokerage_id"] for r in rows} == {"brk-A"}
    assert len(rows) == 1


def test_intelligence_allow_global_is_explicit_admin_opt_in(monkeypatch):
    from app.services.intelligence import queries as q
    db = FakeDB().seed("pas_events", [
        {"id": 1, "brokerage_id": "brk-A"},
        {"id": 2, "brokerage_id": "brk-B"},
    ])
    monkeypatch.setattr(q, "get_supabase", lambda: db)
    rows = q.recent_events(allow_global=True)   # admin explicitly opts in
    assert len(rows) == 2


# ── agent store: tenant predicate ──────────────────────────────────
def _agent_db():
    return FakeDB().seed("agents", [
        {"id": "a1", "brokerage_id": "brk-A", "name": "Alice", "status": "available"},
        {"id": "a2", "brokerage_id": "brk-B", "name": "Bob", "status": "available"},
    ])


def test_get_agent_cross_tenant_returns_none(monkeypatch):
    import app.db.agent_store as ag
    monkeypatch.setattr(ag, "get_supabase", lambda: _agent_db())
    assert ag.get_agent("a1", brokerage_id="brk-A")["name"] == "Alice"
    assert ag.get_agent("a1", brokerage_id="brk-B") is None  # other tenant


def test_update_agent_cross_tenant_changes_nothing(monkeypatch):
    db = _agent_db()
    import app.db.agent_store as ag
    monkeypatch.setattr(ag, "get_supabase", lambda: db)
    ag.update_agent("a1", {"name": "HACKED"}, brokerage_id="brk-B")  # wrong tenant
    assert db.tables["agents"][0]["name"] == "Alice"                 # untouched
    ag.update_agent("a1", {"name": "Alice2"}, brokerage_id="brk-A")  # right tenant
    assert db.tables["agents"][0]["name"] == "Alice2"


def test_delete_agent_cross_tenant_deletes_nothing(monkeypatch):
    db = _agent_db()
    import app.db.agent_store as ag
    monkeypatch.setattr(ag, "get_supabase", lambda: db)
    ag.delete_agent("a1", brokerage_id="brk-B")                      # wrong tenant
    assert any(r["id"] == "a1" for r in db.tables["agents"])         # still there
    ag.delete_agent("a1", brokerage_id="brk-A")                      # right tenant
    assert not any(r["id"] == "a1" for r in db.tables["agents"])


# ── booking store: tenant predicate ────────────────────────────────
def _booking_db():
    return FakeDB().seed("bookings", [
        {"id": "b1", "brokerage_id": "brk-A", "status": "scheduled", "lead_phone": "+1"},
        {"id": "b2", "brokerage_id": "brk-B", "status": "scheduled"},
    ])


def test_get_booking_cross_tenant_returns_none(monkeypatch):
    import app.db.booking_store as bk
    monkeypatch.setattr(bk, "get_supabase", lambda: _booking_db())
    assert bk.get_booking("b1", brokerage_id="brk-A")["id"] == "b1"
    assert bk.get_booking("b1", brokerage_id="brk-B") is None       # no PII leak


def test_update_booking_status_cross_tenant_changes_nothing(monkeypatch):
    db = _booking_db()
    import app.db.booking_store as bk
    monkeypatch.setattr(bk, "get_supabase", lambda: db)
    bk.update_booking_status("b1", "cancelled", brokerage_id="brk-B")   # wrong tenant
    assert db.tables["bookings"][0]["status"] == "scheduled"           # untouched
    bk.update_booking_status("b1", "completed", brokerage_id="brk-A")   # right tenant
    assert db.tables["bookings"][0]["status"] == "completed"


# ── PAS210 snapshot still requires a tenant ────────────────────────
def test_snapshot_adapter_requires_brokerage_id():
    from app.services.proactive.supabase_snapshot_adapter import load_snapshot
    with pytest.raises(ValueError):
        load_snapshot(client=object(), brokerage_id="")


# ── ingestion stays tenant-pinned ──────────────────────────────────
def test_ingestion_dedupe_key_is_tenant_pinned():
    from app.services.ingestion.lead_dedupe import dedupe_key
    from app.services.ingestion.lead_contracts import NormalizedLead
    lead = NormalizedLead(source="zillow", phone="+12125551234", message="hi")
    assert dedupe_key("brk-A", lead) != dedupe_key("brk-B", lead)


# ── memory retrieval / context stay tenant-isolated ────────────────
def test_memory_retrieval_requires_tenant():
    from app.services.memory.approved_memory_retrieval import retrieve_approved
    assert retrieve_approved("") == []   # no tenant → no read (never global)


def test_memory_context_requires_tenant_and_is_default_off():
    from app.services.memory.memory_context_boundary import build_memory_context
    # Default-off (flag not set) → never enabled even with a tenant.
    assert build_memory_context("brk-A").get("enabled") is False
    # Even if the flag were on, a missing tenant yields enabled=False.
    assert build_memory_context(None).get("enabled") is False


# ── RLS migration proposal ─────────────────────────────────────────
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
MIGRATION = os.path.join(REPO_ROOT, "scripts", "migrate_v9_tenant_rls_policies.sql")


def _executable_sql(text):
    return "\n".join(
        (line if line.find("--") == -1 else line[: line.find("--")])
        for line in text.splitlines()
    )


def test_rls_migration_proposal_exists_with_policies():
    assert os.path.isfile(MIGRATION), "PAS211E RLS policy migration proposal missing"
    sql = open(MIGRATION, encoding="utf-8").read()
    assert "CREATE POLICY" in sql                       # real policies, not just ENABLE
    assert "auth.jwt()" in sql                          # tenant claim model
    assert "brokerage_id" in sql


def test_rls_migration_documents_service_role_limitation():
    sql = open(MIGRATION, encoding="utf-8").read().lower()
    assert "service-role" in sql or "service role" in sql
    assert "bypassrls" in sql or "bypass" in sql
    assert "pas211g" in sql                             # future JWT/RBAC dependency


def test_rls_migration_has_no_destructive_sql():
    sql = _executable_sql(open(MIGRATION, encoding="utf-8").read())
    for verb in (r"\bDROP\b", r"\bDELETE\b", r"\bTRUNCATE\b"):
        assert not re.search(verb, sql, re.IGNORECASE), f"destructive {verb} present"
    # The only ALTER permitted is (idempotent) ENABLE ROW LEVEL SECURITY.
    for alter in re.findall(r"ALTER\s+TABLE.*?;", sql, re.IGNORECASE | re.DOTALL):
        assert "ENABLE ROW LEVEL SECURITY" in alter.upper()
