"""
Tests for app.db.audit_log — payload redaction, row construction, and
the failure-tolerant fire-and-forget contract.

No live Supabase. Inserts are stubbed by monkey-patching _insert_audit
or by relying on the fact that get_supabase() raises when uninitialised
(which log_audit must swallow).

Runnable directly:
    python tests/auth/test_audit_log.py
"""

import os
import sys
import time

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")),
)

from app.db import audit_log as al
from app.auth.principal import (
    Principal,
    ROLE_ADMIN,
    ROLE_ADMIN_LEGACY,
    ROLE_OWNER,
    ROLE_BROKERAGE_LEGACY,
    SOURCE_JWT,
    SOURCE_LEGACY_ADMIN,
    SOURCE_LEGACY_BROKERAGE,
)


# ───────────── _looks_secret ─────────────

def test_looks_secret_matches_common_names():
    for k in [
        "api_key", "API_KEY", "X-API-Key", "x-admin-key",
        "password", "user_password", "Passwd",
        "token", "access_token", "refresh_token", "setup_token",
        "secret", "client_secret", "slack_signing_secret",
        "Authorization", "bearer_token",
        "key_hash", "private_key", "session_id", "Cookie", "jwt",
    ]:
        assert al._looks_secret(k), f"expected {k!r} to be secret"


def test_looks_secret_ignores_innocent_keys():
    for k in ["name", "email", "brokerage_id", "id", "created_at", "phone", "tone"]:
        assert not al._looks_secret(k), f"expected {k!r} to be non-secret"


def test_looks_secret_handles_non_string_keys():
    # Numeric keys (rare but possible in JSON-shaped dicts) should not crash.
    assert al._looks_secret(42) is False
    assert al._looks_secret(None) is False


# ───────────── _redact ─────────────

def test_redact_strips_top_level_secret_keys():
    out = al._redact({
        "name": "RE/MAX Miami",
        "api_key": "pas_xxxxxxxx",
        "password": "hunter2",
    })
    assert out["name"] == "RE/MAX Miami"
    assert out["api_key"] == al._REDACTED
    assert out["password"] == al._REDACTED


def test_redact_strips_nested_secret_keys():
    out = al._redact({
        "config": {
            "tone": "professional",
            "slack_signing_secret": "xoxs-...",
        },
        "owner": {
            "email": "owner@brokerage.com",
            "session_id": "sb_session_abc",
        },
    })
    assert out["config"]["tone"] == "professional"
    assert out["config"]["slack_signing_secret"] == al._REDACTED
    assert out["owner"]["email"] == "owner@brokerage.com"
    assert out["owner"]["session_id"] == al._REDACTED


def test_redact_handles_lists_of_dicts():
    out = al._redact({
        "members": [
            {"email": "a@b.com", "password": "p1"},
            {"email": "c@d.com", "api_key": "k2"},
        ],
    })
    assert out["members"][0]["email"] == "a@b.com"
    assert out["members"][0]["password"] == al._REDACTED
    assert out["members"][1]["api_key"] == al._REDACTED


def test_redact_preserves_non_dict_values():
    out = al._redact({"count": 5, "active": True, "tags": ["a", "b"]})
    assert out == {"count": 5, "active": True, "tags": ["a", "b"]}


def test_redact_passes_through_primitives():
    assert al._redact(5) == 5
    assert al._redact("hello") == "hello"
    assert al._redact(None) is None


# ───────────── _truncate_payload ─────────────

def test_truncate_payload_keeps_small_payload():
    p = {"a": 1, "b": "x"}
    assert al._truncate_payload(p) == p


def test_truncate_payload_marks_oversized_payload():
    huge = {"big": "x" * (al._MAX_PAYLOAD_BYTES + 1000)}
    out = al._truncate_payload(huge)
    assert out["_payload_truncated"] is True
    assert out["_original_bytes"] > al._MAX_PAYLOAD_BYTES


def test_truncate_payload_handles_non_serializable():
    class Weird:
        def __repr__(self):
            raise RuntimeError("boom")

    out = al._truncate_payload({"x": Weird()})
    # Either the marker dict (default=str raised) or the original — both
    # are acceptable; what we care about is no exception bubbled up.
    assert isinstance(out, dict)


# ───────────── _actor_fields ─────────────

def test_actor_fields_none_returns_system():
    uid, email, atype = al._actor_fields(None)
    assert (uid, email, atype) == (None, None, "system")


def test_actor_fields_admin_principal():
    p = Principal(
        user_id="u1", email="ops@orvn.com",
        role=ROLE_ADMIN, brokerage_id=None, source=SOURCE_JWT,
    )
    assert al._actor_fields(p) == ("u1", "ops@orvn.com", "admin")


def test_actor_fields_admin_legacy_principal_marked_legacy_key():
    p = Principal(
        user_id="legacy:admin", email=None,
        role=ROLE_ADMIN_LEGACY, brokerage_id=None, source=SOURCE_LEGACY_ADMIN,
    )
    assert al._actor_fields(p) == ("legacy:admin", None, "legacy_key")


def test_actor_fields_owner_principal():
    p = Principal(
        user_id="u2", email="owner@brokerage.com",
        role=ROLE_OWNER, brokerage_id="remax-miami", source=SOURCE_JWT,
    )
    assert al._actor_fields(p) == ("u2", "owner@brokerage.com", "brokerage_user")


def test_actor_fields_brokerage_legacy_principal_marked_legacy_key():
    p = Principal(
        user_id="legacy:remax", email=None,
        role=ROLE_BROKERAGE_LEGACY, brokerage_id="remax-miami",
        source=SOURCE_LEGACY_BROKERAGE,
    )
    assert al._actor_fields(p) == ("legacy:remax", None, "legacy_key")


def test_actor_fields_dict_with_explicit_actor_type():
    out = al._actor_fields({"user_id": "u", "email": "e", "actor_type": "admin"})
    assert out == ("u", "e", "admin")


def test_actor_fields_dict_without_explicit_actor_type():
    # Falls through to derivation — no role/brokerage_id ⇒ system.
    out = al._actor_fields({"user_id": "u", "email": "e"})
    assert out == ("u", "e", "system")


# ───────────── _build_row ─────────────

def test_build_row_redacts_payload_and_sets_actor_fields():
    p = Principal(
        user_id="u1", email="ops@orvn.com",
        role=ROLE_ADMIN, brokerage_id=None, source=SOURCE_JWT,
    )
    row = al._build_row(
        "brokerage.created",
        actor=p,
        brokerage_id="remax-miami",
        target="remax-miami",
        payload={"name": "RE/MAX Miami", "api_key": "pas_should_not_appear"},
        request_id="req-1",
        ip="1.2.3.4",
    )

    assert row["event_type"] == "brokerage.created"
    assert row["actor_type"] == "admin"
    assert row["actor_user_id"] == "u1"
    assert row["actor_email"] == "ops@orvn.com"
    assert row["brokerage_id"] == "remax-miami"
    assert row["target"] == "remax-miami"
    assert row["request_id"] == "req-1"
    assert row["ip"] == "1.2.3.4"

    # The redacted payload must NOT carry the original secret value, and
    # MUST keep the non-secret fields intact.
    assert row["payload"]["name"] == "RE/MAX Miami"
    assert row["payload"]["api_key"] == al._REDACTED
    serialized = str(row["payload"])
    assert "pas_should_not_appear" not in serialized


def test_build_row_no_actor_records_system():
    row = al._build_row(
        "system.startup",
        actor=None,
        brokerage_id=None,
        target=None,
        payload=None,
        request_id=None,
        ip=None,
    )
    assert row["actor_type"] == "system"
    assert row["actor_user_id"] is None
    assert row["actor_email"] is None
    assert row["payload"] == {}


# ───────────── log_audit — failure tolerance ─────────────

def test_log_audit_does_not_raise_when_supabase_uninitialised():
    # Supabase has not been init'd in this test process — get_supabase()
    # will raise inside _insert_audit, and log_audit must swallow it.
    try:
        result = al.log_audit(
            "test.event",
            actor=None,
            brokerage_id="x",
            target="x",
            payload={"hello": "world"},
        )
    except Exception as e:
        raise AssertionError(f"log_audit raised but must never raise: {e}")
    assert result is None
    # Give the daemon thread a moment to attempt its insert + warning so
    # we know the failure path actually ran without bubbling.
    time.sleep(0.05)


def test_log_audit_drops_empty_event_type():
    # Empty event_type should be silently dropped — no exception, no work.
    result = al.log_audit("", actor=None, payload={"x": 1})
    assert result is None


def test_log_audit_swallow_when_insert_raises(monkeypatch=None):
    # Force _insert_audit to raise — the worker wrapper must catch it.
    captured: dict = {"called": False}

    def boom(_row):
        captured["called"] = True
        raise RuntimeError("simulated supabase outage")

    original = al._insert_audit
    al._insert_audit = boom  # type: ignore[assignment]
    try:
        al.log_audit("test.boom", actor=None, payload={"k": "v"})
        # The worker is async — wait briefly for it to run.
        for _ in range(20):
            if captured["called"]:
                break
            time.sleep(0.02)
    finally:
        al._insert_audit = original  # type: ignore[assignment]

    # The contract is "log_audit never raises" — reaching here is the
    # primary assertion. Bonus check that the worker did fire.
    assert captured["called"] is True


def test_log_audit_strips_secrets_via_build_row(monkeypatch=None):
    # End-to-end: pass a payload with a secret, capture the row that
    # _insert_audit would receive, and confirm the secret is gone.
    captured: dict = {"row": None}

    def capture(row):
        captured["row"] = row
        return True

    original = al._insert_audit
    al._insert_audit = capture  # type: ignore[assignment]
    try:
        al.log_audit(
            "invite.generated",
            actor=None,
            brokerage_id="remax-miami",
            target="remax-miami",
            payload={"setup_token": "orvn_setup_secret", "ttl_days": 3},
        )
        for _ in range(50):
            if captured["row"] is not None:
                break
            time.sleep(0.02)
    finally:
        al._insert_audit = original  # type: ignore[assignment]

    assert captured["row"] is not None, "audit worker did not deliver row"
    pl = captured["row"]["payload"]
    assert pl["setup_token"] == al._REDACTED
    assert pl["ttl_days"] == 3
    assert "orvn_setup_secret" not in str(pl)


# ───────────── runner ─────────────

if __name__ == "__main__":
    fns = [v for k, v in list(globals().items()) if k.startswith("test_") and callable(v)]
    failures = 0
    for fn in fns:
        name = fn.__name__
        try:
            fn()
            print(f"  PASS {name}")
        except AssertionError as e:
            failures += 1
            print(f"  FAIL {name} -- {e}")
        except Exception as e:
            failures += 1
            print(f"  FAIL {name} -- {type(e).__name__}: {e}")
    print(f"\n{len(fns) - failures}/{len(fns)} passed")
    sys.exit(0 if failures == 0 else 1)
