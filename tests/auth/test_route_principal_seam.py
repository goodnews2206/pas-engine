"""
Tests for the PAS211G.3 route principal seam in require_admin (app/routes/admin.py)
and require_brokerage (app/routes/portal.py).

Pure unit tests — dependencies are called directly (no TestClient, no live
server), settings are monkeypatched, brokerage lookups are mocked, JWTs are
signed with a test-local secret. No DB, no network, no Supabase, no .env.

Goal: prove legacy X-Admin-Key / X-API-Key behavior is preserved, and the gated
JWT path is fail-closed and inert by default (JWT_AUTH_ENABLED=False).
"""

import os
import sys
import time

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")),
)

import jwt
import pytest
from fastapi import HTTPException

import app.routes.admin as admin_mod
import app.routes.portal as portal_mod
import app.auth.resolver as resolver_mod
from app.routes.admin import require_admin
from app.routes.portal import require_brokerage
from app.config import Settings


# test-local secret (>= 32 bytes; never a real Supabase secret)
SECRET = "route-seam-test-secret-not-real-" + ("0123456789" * 4)


def _settings(**kw):
    base = {"ENVIRONMENT": "development", "BASE_URL": "http://localhost:8000"}
    base.update(kw)
    return Settings(**base)


def _set_settings(monkeypatch, **kw):
    """Point admin, portal, AND resolver get_settings at the same fake."""
    s = _settings(**kw)
    monkeypatch.setattr(admin_mod, "get_settings", lambda: s)
    monkeypatch.setattr(portal_mod, "get_settings", lambda: s)
    monkeypatch.setattr(resolver_mod, "get_settings", lambda: s)
    return s


def _jwt(**claims):
    payload = {"sub": "user-1", "exp": int(time.time()) + 3600}
    payload.update(claims)
    return jwt.encode(payload, SECRET, algorithm="HS256")


def _bearer(**claims):
    return f"Bearer {_jwt(**claims)}"


# ═════════════ require_admin — legacy X-Admin-Key (unchanged) ═════════════

def test_admin_legacy_valid_key_accepted(monkeypatch):
    _set_settings(monkeypatch, ADMIN_API_KEY="s3cret")
    assert require_admin(x_admin_key="s3cret", authorization=None) is True


def test_admin_legacy_invalid_key_rejected_401(monkeypatch):
    _set_settings(monkeypatch, ADMIN_API_KEY="s3cret")
    with pytest.raises(HTTPException) as e:
        require_admin(x_admin_key="wrong", authorization=None)
    assert e.value.status_code == 401


def test_admin_legacy_missing_key_is_422_compat(monkeypatch):
    # A completely absent X-Admin-Key preserves FastAPI's prior 422 (not 401).
    _set_settings(monkeypatch, ADMIN_API_KEY="s3cret")
    with pytest.raises(HTTPException) as e:
        require_admin(x_admin_key=None, authorization=None)
    assert e.value.status_code == 422


def test_admin_empty_configured_key_rejects(monkeypatch):
    _set_settings(monkeypatch, ADMIN_API_KEY="")
    with pytest.raises(HTTPException) as e:
        require_admin(x_admin_key="anything", authorization=None)
    assert e.value.status_code == 401


# ═════════════ require_admin — JWT disabled (default) ═════════════

def test_admin_jwt_disabled_authorization_header_is_inert(monkeypatch):
    # Valid admin token present, but JWT disabled → header ignored, legacy wins.
    _set_settings(monkeypatch, ADMIN_API_KEY="k")  # JWT_AUTH_ENABLED defaults False
    assert require_admin(x_admin_key="k", authorization=_bearer(role="admin")) is True
    # And with no key, the bearer must NOT authenticate → missing-credential 422.
    with pytest.raises(HTTPException) as e:
        require_admin(x_admin_key=None, authorization=_bearer(role="admin"))
    assert e.value.status_code == 422


# ═════════════ require_admin — JWT enabled ═════════════

def test_admin_jwt_valid_admin_accepted(monkeypatch):
    _set_settings(monkeypatch, ADMIN_API_KEY="k", JWT_AUTH_ENABLED=True, SUPABASE_JWT_SECRET=SECRET)
    result = require_admin(x_admin_key=None, authorization=_bearer(role="admin"))
    assert result is not True            # returns the Principal, not the legacy bool
    assert result.is_admin is True


def test_admin_jwt_non_admin_rejected_403(monkeypatch):
    _set_settings(monkeypatch, ADMIN_API_KEY="k", JWT_AUTH_ENABLED=True, SUPABASE_JWT_SECRET=SECRET)
    with pytest.raises(HTTPException) as e:
        require_admin(x_admin_key=None, authorization=_bearer(role="agent", brokerage_id="b1"))
    assert e.value.status_code == 403


def test_admin_jwt_invalid_bearer_fails_closed_no_legacy_fallback(monkeypatch):
    # Bearer present + JWT enabled + token invalid → 401, MUST NOT fall back to
    # the (otherwise valid) X-Admin-Key.
    _set_settings(monkeypatch, ADMIN_API_KEY="k", JWT_AUTH_ENABLED=True, SUPABASE_JWT_SECRET=SECRET)
    with pytest.raises(HTTPException) as e:
        require_admin(x_admin_key="k", authorization="Bearer not-a-jwt")
    assert e.value.status_code == 401


def test_admin_jwt_enabled_no_bearer_uses_legacy(monkeypatch):
    # JWT enabled but no Bearer header → legacy key path still works.
    _set_settings(monkeypatch, ADMIN_API_KEY="k", JWT_AUTH_ENABLED=True, SUPABASE_JWT_SECRET=SECRET)
    assert require_admin(x_admin_key="k", authorization=None) is True


def test_admin_jwt_enabled_no_bearer_no_key_is_422(monkeypatch):
    # Consistent missing-credential response: no Bearer + no key → 422.
    _set_settings(monkeypatch, ADMIN_API_KEY="k", JWT_AUTH_ENABLED=True, SUPABASE_JWT_SECRET=SECRET)
    with pytest.raises(HTTPException) as e:
        require_admin(x_admin_key=None, authorization=None)
    assert e.value.status_code == 422


# ═════════════ require_brokerage — legacy X-API-Key (unchanged) ═════════════

def test_brokerage_legacy_valid_key_returns_dict(monkeypatch):
    _set_settings(monkeypatch)  # JWT disabled
    monkeypatch.setattr(portal_mod, "get_brokerage_by_api_key",
                        lambda k: {"id": "remax-miami", "name": "RE/MAX Miami"} if k == "good" else None)
    result = require_brokerage(x_api_key="good", authorization=None)
    assert isinstance(result, dict)
    assert result["id"] == "remax-miami"   # return contract preserved (dict, not Principal)


def test_brokerage_legacy_invalid_key_rejected_401(monkeypatch):
    _set_settings(monkeypatch)
    monkeypatch.setattr(portal_mod, "get_brokerage_by_api_key", lambda k: None)
    with pytest.raises(HTTPException) as e:
        require_brokerage(x_api_key="bad", authorization=None)
    assert e.value.status_code == 401


def test_brokerage_legacy_missing_key_is_422_compat(monkeypatch):
    # A completely absent X-API-Key preserves FastAPI's prior 422 (not 401).
    _set_settings(monkeypatch)
    monkeypatch.setattr(portal_mod, "get_brokerage_by_api_key", lambda k: None)
    with pytest.raises(HTTPException) as e:
        require_brokerage(x_api_key=None, authorization=None)
    assert e.value.status_code == 422


def test_brokerage_demo_rejected_401(monkeypatch):
    _set_settings(monkeypatch)
    monkeypatch.setattr(portal_mod, "get_brokerage_by_api_key", lambda k: {"id": "demo"})
    with pytest.raises(HTTPException) as e:
        require_brokerage(x_api_key="demo-key", authorization=None)
    assert e.value.status_code == 401


# ═════════════ require_brokerage — JWT disabled (default) ═════════════

def test_brokerage_jwt_disabled_authorization_inert(monkeypatch):
    _set_settings(monkeypatch)  # JWT disabled
    monkeypatch.setattr(portal_mod, "get_brokerage_by_api_key", lambda k: None)
    # A valid-looking brokerage bearer must NOT authenticate while disabled →
    # falls through to legacy, where the absent X-API-Key is the 422 compat case.
    with pytest.raises(HTTPException) as e:
        require_brokerage(x_api_key=None, authorization=_bearer(role="owner", brokerage_id="b1"))
    assert e.value.status_code == 422


# ═════════════ require_brokerage — JWT enabled ═════════════

def test_brokerage_jwt_valid_owner_returns_dict_by_verified_claim(monkeypatch):
    _set_settings(monkeypatch, JWT_AUTH_ENABLED=True, SUPABASE_JWT_SECRET=SECRET)
    monkeypatch.setattr(portal_mod, "get_brokerage_by_id",
                        lambda bid: {"id": "b1", "name": "Brokerage One"} if bid == "b1" else {"id": "demo"})
    result = require_brokerage(x_api_key=None, authorization=_bearer(role="owner", brokerage_id="b1"))
    assert isinstance(result, dict)
    assert result["id"] == "b1"


def test_brokerage_jwt_without_brokerage_id_rejected_403(monkeypatch):
    _set_settings(monkeypatch, JWT_AUTH_ENABLED=True, SUPABASE_JWT_SECRET=SECRET)
    with pytest.raises(HTTPException) as e:
        require_brokerage(x_api_key=None, authorization=_bearer(role="owner"))  # no brokerage_id
    assert e.value.status_code == 403


def test_brokerage_jwt_invalid_bearer_fails_closed_no_legacy_fallback(monkeypatch):
    # Bearer present + JWT enabled + invalid → 401, MUST NOT fall back to a valid X-API-Key.
    _set_settings(monkeypatch, JWT_AUTH_ENABLED=True, SUPABASE_JWT_SECRET=SECRET)
    monkeypatch.setattr(portal_mod, "get_brokerage_by_api_key",
                        lambda k: {"id": "b1", "name": "Brokerage One"})
    with pytest.raises(HTTPException) as e:
        require_brokerage(x_api_key="good", authorization="Bearer not-a-jwt")
    assert e.value.status_code == 401


def test_brokerage_jwt_claim_brokerage_not_found_rejected_403(monkeypatch):
    _set_settings(monkeypatch, JWT_AUTH_ENABLED=True, SUPABASE_JWT_SECRET=SECRET)
    monkeypatch.setattr(portal_mod, "get_brokerage_by_id", lambda bid: {"id": "demo"})  # not found
    with pytest.raises(HTTPException) as e:
        require_brokerage(x_api_key=None, authorization=_bearer(role="owner", brokerage_id="ghost"))
    assert e.value.status_code == 403


def test_brokerage_jwt_enabled_no_bearer_no_key_is_422(monkeypatch):
    # Consistent missing-credential response: no Bearer + no key → 422.
    _set_settings(monkeypatch, JWT_AUTH_ENABLED=True, SUPABASE_JWT_SECRET=SECRET)
    monkeypatch.setattr(portal_mod, "get_brokerage_by_api_key", lambda k: None)
    with pytest.raises(HTTPException) as e:
        require_brokerage(x_api_key=None, authorization=None)
    assert e.value.status_code == 422
