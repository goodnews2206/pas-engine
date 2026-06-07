"""PAS211F — secrets storage + rotation readiness.

Proves the PAS211C secrets findings are reduced:
  * admin list/detail no longer return plaintext api_key / slack_signing_secret /
    slack_webhook_url; create/rotate show the raw api_key exactly once;
  * a hashing layer (stdlib, no new dep) deterministically hashes high-entropy
    keys and, when SECRETS_HASHING_ENABLED, stores the HASH (not plaintext) for
    brokerage api_keys and invite keys, with a legacy plaintext fallback;
  * the redaction helper strips secret-shaped fields;
  * the migration proposal exists, adds api_key_hash, and has no destructive SQL.

Hashing is OFF by default → existing behaviour is unchanged; the activated path
is exercised here against an in-memory fake DB modelling post-migration columns.
"""
import os
import re

import pytest

from app.config import Settings, _PRODUCTION_INDICATOR_VARS


@pytest.fixture(autouse=True)
def _clean_env(monkeypatch):
    for var in _PRODUCTION_INDICATOR_VARS:
        monkeypatch.delenv(var, raising=False)
    yield


def _settings(**kw):
    base = {"ENVIRONMENT": "development", "BASE_URL": "http://localhost:8000"}
    base.update(kw)
    return Settings(**base)


# ── in-memory Supabase double (insert + select/eq/limit + update) ──
class _Res:
    def __init__(self, data):
        self.data = data


class _Q:
    def __init__(self, rows, op):
        self._rows, self._op, self._payload, self._filters, self._limit = rows, op, None, {}, None

    def select(self, *a, **k):
        return self

    def update(self, payload):
        self._op, self._payload = "update", payload
        return self

    def eq(self, c, v):
        self._filters[c] = v
        return self

    def order(self, *a, **k):
        return self

    def limit(self, n):
        self._limit = n
        return self

    def execute(self):
        matched = [r for r in self._rows if all(r.get(c) == v for c, v in self._filters.items())]
        if self._op == "update":
            for r in matched:
                r.update(self._payload)
            return _Res(list(matched))
        return _Res(matched[: self._limit] if self._limit else list(matched))


class _Ins:
    def __init__(self, rows, payload):
        self._rows, self._payload = rows, payload

    def execute(self):
        self._rows.append(dict(self._payload))
        return _Res([dict(self._payload)])


class _Table:
    def __init__(self, rows):
        self._rows = rows

    def select(self, *a, **k):
        return _Q(self._rows, "select")

    def update(self, payload):
        q = _Q(self._rows, "update")
        q._payload = payload
        return q

    def insert(self, payload):
        return _Ins(self._rows, payload)


class FakeDB:
    def __init__(self):
        self.tables = {}

    def table(self, name):
        return _Table(self.tables.setdefault(name, []))


# ── hashing utility ────────────────────────────────────────────────
def test_hash_is_deterministic_distinct_and_prefixed():
    from app.services.security.secret_hash import hash_api_key
    assert hash_api_key("pas_abc") == hash_api_key("pas_abc")
    assert hash_api_key("pas_abc") != hash_api_key("pas_xyz")
    assert hash_api_key("pas_abc").startswith("sha256$")
    assert hash_api_key("") == ""


def test_hash_verify_and_pepper_effect():
    from app.services.security.secret_hash import hash_secret, verify_secret
    h = hash_secret("pas_abc", pepper="P1")
    assert verify_secret("pas_abc", h, pepper="P1") is True
    assert verify_secret("pas_xyz", h, pepper="P1") is False
    # A different pepper yields a different hash (DB-theft resistance).
    assert hash_secret("pas_abc", pepper="P1") != hash_secret("pas_abc", pepper="P2")


# ── redaction helper ───────────────────────────────────────────────
def test_redact_brokerage_masks_secrets_keeps_other_fields():
    from app.services.security.secret_redaction import redact_brokerage, REDACTED
    b = {"id": "x", "name": "N", "api_key": "pas_s", "slack_signing_secret": "xoxs",
         "slack_webhook_url": "https://hook", "api_key_hash": "sha256$z"}
    r = redact_brokerage(b)
    assert r["api_key"] == REDACTED
    assert r["slack_signing_secret"] == REDACTED
    assert r["slack_webhook_url"] == REDACTED
    assert r["api_key_hash"] == REDACTED
    assert r["name"] == "N" and r["id"] == "x"


def test_redact_brokerage_keep_api_key_for_one_time_display():
    from app.services.security.secret_redaction import redact_brokerage, REDACTED
    b = {"id": "x", "api_key": "pas_raw", "slack_signing_secret": "xoxs"}
    r = redact_brokerage(b, keep_api_key=True)
    assert r["api_key"] == "pas_raw"               # shown once at create/rotate
    assert r["slack_signing_secret"] == REDACTED   # never echoed


def test_redact_secret_fields_recursive():
    from app.services.security.secret_redaction import redact_secret_fields, REDACTED
    out = redact_secret_fields({"a": 1, "config": {"slack_signing_secret": "s", "tone": "pro"}})
    assert out["config"]["slack_signing_secret"] == REDACTED
    assert out["config"]["tone"] == "pro" and out["a"] == 1


# ── admin reads do not leak secrets (route level) ──────────────────
def test_admin_list_redacts_secrets(monkeypatch):
    from fastapi.testclient import TestClient
    import app.routes.admin as admin
    from app.main import app
    from app.services.security.secret_redaction import REDACTED

    monkeypatch.setattr(admin, "get_settings", lambda: _settings(ADMIN_API_KEY="k"))
    monkeypatch.setattr(admin, "list_brokerages", lambda: [
        {"id": "b1", "name": "N", "api_key": "pas_leak",
         "slack_signing_secret": "xoxs_leak", "slack_webhook_url": "https://leak"},
    ])
    with TestClient(app) as c:
        resp = c.get("/admin/brokerages", headers={"X-Admin-Key": "k"})
    assert resp.status_code == 200
    body = resp.text
    assert "pas_leak" not in body and "xoxs_leak" not in body and "https://leak" not in body
    b0 = resp.json()["brokerages"][0]
    assert b0["api_key"] == REDACTED and b0["slack_signing_secret"] == REDACTED


def test_admin_detail_redacts_secrets(monkeypatch):
    from fastapi.testclient import TestClient
    import app.routes.admin as admin
    from app.main import app

    monkeypatch.setattr(admin, "get_settings", lambda: _settings(ADMIN_API_KEY="k"))
    monkeypatch.setattr(admin, "get_brokerage_by_id",
                        lambda bid: {"id": bid, "name": "N", "api_key": "pas_leak",
                                     "slack_signing_secret": "xoxs_leak", "slack_webhook_url": "https://leak"})
    monkeypatch.setattr(admin, "get_brokerage_stats", lambda bid: {})
    with TestClient(app) as c:
        resp = c.get("/admin/brokerages/b1", headers={"X-Admin-Key": "k"})
    assert resp.status_code == 200
    assert "pas_leak" not in resp.text and "xoxs_leak" not in resp.text


def test_admin_create_shows_api_key_once_but_redacts_slack(monkeypatch):
    from fastapi.testclient import TestClient
    import app.routes.admin as admin
    from app.main import app
    from app.services.security.secret_redaction import REDACTED

    monkeypatch.setattr(admin, "get_settings", lambda: _settings(ADMIN_API_KEY="k"))
    monkeypatch.setattr(admin, "get_brokerage_by_id", lambda bid: {"id": "demo"})  # no collision
    monkeypatch.setattr(admin, "create_brokerage",
                        lambda data: {"id": data["id"], "name": data["name"], "api_key": "pas_new_raw",
                                      "slack_signing_secret": "xoxs_leak", "slack_webhook_url": ""})
    with TestClient(app) as c:
        resp = c.post("/admin/brokerages", headers={"X-Admin-Key": "k"},
                      json={"id": "b1", "name": "N"})
    assert resp.status_code == 201
    br = resp.json()["brokerage"]
    assert br["api_key"] == "pas_new_raw"            # raw key shown once
    assert br["slack_signing_secret"] == REDACTED    # slack secret never echoed


# ── hashed storage path (SECRETS_HASHING_ENABLED) ──────────────────
def test_create_brokerage_stores_hash_not_plaintext_when_enabled(monkeypatch):
    import app.db.brokerage_store as bs
    from app.services.security.secret_hash import hash_api_key
    db = FakeDB()
    monkeypatch.setattr(bs, "get_supabase", lambda: db)
    monkeypatch.setattr(bs, "get_settings", lambda: _settings(SECRETS_HASHING_ENABLED=True))

    created = bs.create_brokerage({"id": "b1", "name": "N"})
    raw = created["api_key"]
    assert raw.startswith("pas_")                       # raw returned once
    stored = db.tables["brokerages"][0]
    assert stored["api_key"] == ""                      # no plaintext at rest
    assert stored["api_key_hash"] == hash_api_key(raw)  # hash stored

    # And the key resolves via the hashed lookup.
    found = bs.get_brokerage_by_api_key(raw)
    assert found and found["id"] == "b1"
    # A wrong key does not resolve.
    assert bs.get_brokerage_by_api_key("pas_wrong") is None


def test_rotate_api_key_stores_hash_when_enabled(monkeypatch):
    import app.db.brokerage_store as bs
    from app.services.security.secret_hash import hash_api_key
    db = FakeDB()
    db.tables["brokerages"] = [{"id": "b1", "api_key": "pas_old", "api_key_hash": None}]
    monkeypatch.setattr(bs, "get_supabase", lambda: db)
    monkeypatch.setattr(bs, "get_settings", lambda: _settings(SECRETS_HASHING_ENABLED=True))

    new_key = bs.rotate_api_key("b1")
    row = db.tables["brokerages"][0]
    assert new_key.startswith("pas_")
    assert row["api_key"] == "" and row["api_key_hash"] == hash_api_key(new_key)


def test_legacy_plaintext_lookup_still_works_when_disabled(monkeypatch):
    import app.db.brokerage_store as bs
    db = FakeDB()
    db.tables["brokerages"] = [{"id": "b1", "api_key": "pas_legacy"}]
    monkeypatch.setattr(bs, "get_supabase", lambda: db)
    monkeypatch.setattr(bs, "get_settings", lambda: _settings(SECRETS_HASHING_ENABLED=False))
    found = bs.get_brokerage_by_api_key("pas_legacy")
    assert found and found["id"] == "b1"


def test_invite_key_hash_path_when_enabled(monkeypatch):
    import app.db.invite_store as iv
    from app.services.security.secret_hash import hash_invite_key
    db = FakeDB()
    monkeypatch.setattr(iv, "get_supabase", lambda: db)
    monkeypatch.setattr(iv, "get_settings", lambda: _settings(SECRETS_HASHING_ENABLED=True))

    out = iv.generate_invite_key("b1")
    raw = out["key"]
    assert raw.startswith("orvn_")
    stored = db.tables["onboarding_keys"][0]
    assert stored["key"] == ""                          # no plaintext at rest
    assert stored["key_hash"] == hash_invite_key(raw)   # hash stored


# ── migration proposal ─────────────────────────────────────────────
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
MIGRATION = os.path.join(REPO_ROOT, "scripts", "migrate_v10_secrets_encryption_rotation.sql")


def _executable_sql(text):
    return "\n".join(
        (line if line.find("--") == -1 else line[: line.find("--")])
        for line in text.splitlines()
    )


def test_migration_proposal_exists_and_adds_api_key_hash():
    assert os.path.isfile(MIGRATION), "PAS211F secrets migration proposal missing"
    sql = open(MIGRATION, encoding="utf-8").read()
    assert "api_key_hash" in sql
    assert "ADD COLUMN IF NOT EXISTS" in sql              # additive / idempotent


def test_migration_has_no_destructive_sql():
    sql = _executable_sql(open(MIGRATION, encoding="utf-8").read())
    for verb in (r"\bDROP\b", r"\bDELETE\b", r"\bTRUNCATE\b"):
        assert not re.search(verb, sql, re.IGNORECASE), f"destructive {verb} present"
