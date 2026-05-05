"""
Tests for app.auth.principal — pure dataclass + role-helper logic.

No DB. No FastAPI. No network. Runnable directly:
    python tests/auth/test_principal.py
"""

import os
import sys

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")),
)

from dataclasses import FrozenInstanceError

from app.auth.principal import (
    Principal,
    ROLE_ADMIN,
    ROLE_ADMIN_LEGACY,
    ROLE_OWNER,
    ROLE_AGENT,
    ROLE_VIEWER,
    ROLE_DEMO_VIEWER,
    ROLE_BROKERAGE_LEGACY,
    SOURCE_JWT,
    SOURCE_LEGACY_ADMIN,
    SOURCE_LEGACY_BROKERAGE,
)


def _admin_jwt():
    return Principal(
        user_id="00000000-0000-0000-0000-000000000001",
        email="ops@orvn.com",
        role=ROLE_ADMIN,
        brokerage_id=None,
        source=SOURCE_JWT,
    )


def _admin_legacy():
    return Principal(
        user_id="legacy:admin",
        email=None,
        role=ROLE_ADMIN_LEGACY,
        brokerage_id=None,
        source=SOURCE_LEGACY_ADMIN,
    )


def _owner_jwt():
    return Principal(
        user_id="00000000-0000-0000-0000-000000000010",
        email="owner@brokerage.com",
        role=ROLE_OWNER,
        brokerage_id="remax-miami",
        source=SOURCE_JWT,
    )


def _agent_jwt():
    return Principal(
        user_id="00000000-0000-0000-0000-000000000011",
        email="agent@brokerage.com",
        role=ROLE_AGENT,
        brokerage_id="remax-miami",
        source=SOURCE_JWT,
    )


def _viewer_jwt():
    return Principal(
        user_id="00000000-0000-0000-0000-000000000012",
        email="viewer@brokerage.com",
        role=ROLE_VIEWER,
        brokerage_id="remax-miami",
        source=SOURCE_JWT,
    )


def _demo_jwt():
    return Principal(
        user_id="00000000-0000-0000-0000-000000000020",
        email="demo@orvn.com",
        role=ROLE_DEMO_VIEWER,
        brokerage_id="demo",
        source=SOURCE_JWT,
    )


def _brokerage_legacy():
    return Principal(
        user_id="legacy:remax-miami",
        email=None,
        role=ROLE_BROKERAGE_LEGACY,
        brokerage_id="remax-miami",
        source=SOURCE_LEGACY_BROKERAGE,
    )


# ───────────── is_admin ─────────────

def test_is_admin_true_for_admin_jwt():
    assert _admin_jwt().is_admin is True


def test_is_admin_true_for_admin_legacy():
    assert _admin_legacy().is_admin is True


def test_is_admin_false_for_owner():
    assert _owner_jwt().is_admin is False


def test_is_admin_false_for_brokerage_legacy():
    # brokerage_legacy is NOT an admin — even though it's legacy, it
    # represents an X-API-Key holder, not an X-Admin-Key holder.
    assert _brokerage_legacy().is_admin is False


# ───────────── is_brokerage_user ─────────────

def test_is_brokerage_user_true_for_owner():
    assert _owner_jwt().is_brokerage_user is True


def test_is_brokerage_user_true_for_agent_viewer_demo_legacy():
    assert _agent_jwt().is_brokerage_user is True
    assert _viewer_jwt().is_brokerage_user is True
    assert _demo_jwt().is_brokerage_user is True
    assert _brokerage_legacy().is_brokerage_user is True


def test_is_brokerage_user_false_when_brokerage_id_missing():
    p = Principal(
        user_id="x",
        email=None,
        role=ROLE_OWNER,
        brokerage_id=None,            # owner role but no brokerage scope — not usable
        source=SOURCE_JWT,
    )
    assert p.is_brokerage_user is False


def test_is_brokerage_user_false_for_admin():
    assert _admin_jwt().is_brokerage_user is False
    assert _admin_legacy().is_brokerage_user is False


# ───────────── is_owner / is_agent / is_viewer / is_demo_viewer ─────────────

def test_is_owner_true_for_owner():
    assert _owner_jwt().is_owner is True


def test_is_owner_true_for_brokerage_legacy_transition_concession():
    # Legacy X-API-Key holders are treated as owner-equivalent until
    # ENABLE_LEGACY_BROKERAGE_KEY_AUTH flips off in PAS133D.
    assert _brokerage_legacy().is_owner is True


def test_is_owner_false_for_agent_viewer_demo_admin():
    assert _agent_jwt().is_owner is False
    assert _viewer_jwt().is_owner is False
    assert _demo_jwt().is_owner is False
    assert _admin_jwt().is_owner is False


def test_is_agent_true_only_for_agent():
    assert _agent_jwt().is_agent is True
    for p in [_owner_jwt(), _viewer_jwt(), _demo_jwt(), _admin_jwt(), _brokerage_legacy()]:
        assert p.is_agent is False, f"{p.role} should not be is_agent"


def test_is_viewer_true_only_for_viewer():
    assert _viewer_jwt().is_viewer is True
    for p in [_owner_jwt(), _agent_jwt(), _demo_jwt(), _admin_jwt(), _brokerage_legacy()]:
        assert p.is_viewer is False, f"{p.role} should not be is_viewer"


def test_is_demo_viewer_true_only_for_demo_viewer():
    assert _demo_jwt().is_demo_viewer is True
    for p in [_owner_jwt(), _agent_jwt(), _viewer_jwt(), _admin_jwt(), _brokerage_legacy()]:
        assert p.is_demo_viewer is False, f"{p.role} should not be is_demo_viewer"


# ───────────── is_legacy ─────────────

def test_is_legacy_true_for_admin_legacy():
    assert _admin_legacy().is_legacy is True


def test_is_legacy_true_for_brokerage_legacy():
    assert _brokerage_legacy().is_legacy is True


def test_is_legacy_false_for_jwt_admin_and_owner():
    assert _admin_jwt().is_legacy is False
    assert _owner_jwt().is_legacy is False


def test_is_legacy_true_when_source_is_legacy_even_if_role_is_not():
    # Defensive: a malformed Principal (legacy source but non-legacy role)
    # should still report is_legacy=True so audit logs and gates can't be
    # tricked by an inconsistent construction.
    p = Principal(
        user_id="x",
        email=None,
        role=ROLE_OWNER,                    # non-legacy role
        brokerage_id="remax-miami",
        source=SOURCE_LEGACY_BROKERAGE,     # but legacy source
    )
    assert p.is_legacy is True


# ───────────── immutability ─────────────

def test_principal_is_frozen():
    p = _owner_jwt()
    try:
        p.role = ROLE_ADMIN  # type: ignore[misc]
    except FrozenInstanceError:
        return
    raise AssertionError("Principal must be frozen — assignment should raise FrozenInstanceError")


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
