"""PAS211G.1 — principal contract + resolver boundary.

Proves the auth boundary scaffolding works WITHOUT changing any production route:
  * admin key → ORVN_ADMIN principal; bad key → None
  * brokerage API key → brokerage-scoped principal (BROKER_OWNER, or
    INTEGRATION_FORWARDER on the ingestion surface); bad key → None
  * JWT path is a safe stub: disabled → None; enabled-without-impl → None
    (fail closed, never a principal)
  * authz helpers (type / scope / permission) are pure and deny-by-default
  * existing admin + ingestion API-key behaviour is unchanged
  * no secret value is logged by the resolver
"""
import pytest

from app.config import Settings, _PRODUCTION_INDICATOR_VARS
from app.auth import authz, resolver
from app.auth.authz import (
    AuthorizationError,
    has_permission,
    require_brokerage_scope,
    require_principal_type,
)
from app.auth.principal import (
    Principal,
    ROLE_ADMIN_LEGACY,
    ROLE_BROKERAGE_LEGACY,
    SOURCE_LEGACY_ADMIN,
    SOURCE_LEGACY_BROKERAGE,
    TYPE_AGENT,
    TYPE_BROKER_OWNER,
    TYPE_INTEGRATION_FORWARDER,
    TYPE_ORVN_ADMIN,
    AUTH_ADMIN_KEY,
    AUTH_BROKERAGE_API_KEY,
)


@pytest.fixture(autouse=True)
def _clean_env(monkeypatch):
    for var in _PRODUCTION_INDICATOR_VARS:
        monkeypatch.delenv(var, raising=False)
    yield


def _settings(**kw):
    base = {"ENVIRONMENT": "development", "BASE_URL": "http://localhost:8000"}
    base.update(kw)
    return Settings(**base)


# ── Principal contract extensions ──────────────────────────────────
def test_principal_backward_compatible_five_field_construction():
    # PAS133A construction (no PAS211G fields) must still work.
    p = Principal(user_id="x", email=None, role=ROLE_BROKERAGE_LEGACY,
                  brokerage_id="b1", source=SOURCE_LEGACY_BROKERAGE)
    assert p.is_brokerage_user is True
    assert p.principal_type is None and p.permissions == () and p.auth_method is None


def test_principal_new_helpers():
    owner = Principal("legacy:b1", None, ROLE_BROKERAGE_LEGACY, "b1",
                      SOURCE_LEGACY_BROKERAGE, principal_type=TYPE_BROKER_OWNER)
    assert owner.principal_id == "legacy:b1"
    assert owner.is_brokerage_scoped is True
    assert owner.require_brokerage_id() == "b1"

    admin = Principal("legacy:admin", None, ROLE_ADMIN_LEGACY, None,
                      SOURCE_LEGACY_ADMIN, principal_type=TYPE_ORVN_ADMIN)
    assert admin.is_admin is True
    assert admin.is_brokerage_scoped is False


def test_require_brokerage_id_raises_without_tenant():
    admin = Principal("legacy:admin", None, ROLE_ADMIN_LEGACY, None,
                      SOURCE_LEGACY_ADMIN, principal_type=TYPE_ORVN_ADMIN)
    with pytest.raises(ValueError):
        admin.require_brokerage_id()


# ── resolver: admin key ────────────────────────────────────────────
def test_admin_key_resolves_to_orvn_admin(monkeypatch):
    monkeypatch.setattr(resolver, "get_settings", lambda: _settings(ADMIN_API_KEY="s3cret"))
    p = resolver.resolve_principal_from_admin_key("s3cret")
    assert p is not None
    assert p.principal_type == TYPE_ORVN_ADMIN
    assert p.is_admin is True
    assert p.auth_method == AUTH_ADMIN_KEY
    assert p.brokerage_id is None


def test_invalid_admin_key_rejected(monkeypatch):
    monkeypatch.setattr(resolver, "get_settings", lambda: _settings(ADMIN_API_KEY="s3cret"))
    assert resolver.resolve_principal_from_admin_key("wrong") is None
    assert resolver.resolve_principal_from_admin_key("") is None
    assert resolver.resolve_principal_from_admin_key(None) is None


def test_admin_key_empty_configured_never_matches(monkeypatch):
    monkeypatch.setattr(resolver, "get_settings", lambda: _settings(ADMIN_API_KEY=""))
    assert resolver.resolve_principal_from_admin_key("anything") is None


# ── resolver: brokerage api key ────────────────────────────────────
def test_brokerage_api_key_resolves_to_owner(monkeypatch):
    monkeypatch.setattr(resolver, "get_settings", lambda: _settings())
    import app.db.brokerage_store as bs
    monkeypatch.setattr(bs, "get_brokerage_by_api_key", lambda k: {"id": "brk-A"} if k == "good" else None)
    p = resolver.resolve_principal_from_brokerage_api_key("good")
    assert p is not None
    assert p.principal_type == TYPE_BROKER_OWNER
    assert p.brokerage_id == "brk-A"
    assert p.is_brokerage_scoped is True
    assert p.auth_method == AUTH_BROKERAGE_API_KEY


def test_brokerage_api_key_ingestion_surface_is_integration(monkeypatch):
    monkeypatch.setattr(resolver, "get_settings", lambda: _settings())
    import app.db.brokerage_store as bs
    monkeypatch.setattr(bs, "get_brokerage_by_api_key", lambda k: {"id": "brk-A"})
    p = resolver.resolve_principal_from_brokerage_api_key("good", surface="ingestion")
    assert p.principal_type == TYPE_INTEGRATION_FORWARDER
    assert p.brokerage_id == "brk-A"


def test_invalid_brokerage_api_key_rejected(monkeypatch):
    monkeypatch.setattr(resolver, "get_settings", lambda: _settings())
    import app.db.brokerage_store as bs
    monkeypatch.setattr(bs, "get_brokerage_by_api_key", lambda k: None)
    assert resolver.resolve_principal_from_brokerage_api_key("bad") is None
    assert resolver.resolve_principal_from_brokerage_api_key("") is None
    # the demo tenant never resolves to a usable principal
    monkeypatch.setattr(bs, "get_brokerage_by_api_key", lambda k: {"id": "demo"})
    assert resolver.resolve_principal_from_brokerage_api_key("good") is None


# ── resolver: JWT stub (fail closed) ───────────────────────────────
def test_jwt_disabled_returns_none(monkeypatch):
    monkeypatch.setattr(resolver, "get_settings", lambda: _settings(JWT_AUTH_ENABLED=False))
    assert resolver.resolve_principal_from_jwt_stub("any.token") is None


def test_jwt_enabled_without_impl_fails_closed(monkeypatch):
    monkeypatch.setattr(resolver, "get_settings", lambda: _settings(JWT_AUTH_ENABLED=True))
    # Must NOT construct a principal from an unverified token.
    assert resolver.resolve_principal_from_jwt_stub("forged.jwt.token") is None


def test_jwt_stub_does_not_log_token_value(monkeypatch, caplog):
    monkeypatch.setattr(resolver, "get_settings", lambda: _settings(JWT_AUTH_ENABLED=True))
    with caplog.at_level("WARNING"):
        resolver.resolve_principal_from_jwt_stub("SUPER-SECRET-TOKEN-123")
    assert "SUPER-SECRET-TOKEN-123" not in caplog.text


# ── resolver: legacy disabled ──────────────────────────────────────
def test_legacy_disabled_returns_none(monkeypatch):
    monkeypatch.setattr(resolver, "get_settings",
                        lambda: _settings(ADMIN_API_KEY="s3cret", ENABLE_LEGACY_API_KEY_AUTH=False))
    assert resolver.resolve_principal_from_admin_key("s3cret") is None


# ── authz helpers (pure) ───────────────────────────────────────────
def _owner(bid="brk-A"):
    return Principal("legacy:b", None, ROLE_BROKERAGE_LEGACY, bid,
                     SOURCE_LEGACY_BROKERAGE, principal_type=TYPE_BROKER_OWNER,
                     permissions=("read_leads",))


def _admin():
    return Principal("legacy:admin", None, ROLE_ADMIN_LEGACY, None,
                     SOURCE_LEGACY_ADMIN, principal_type=TYPE_ORVN_ADMIN)


def test_require_principal_type():
    assert require_principal_type(_admin(), {TYPE_ORVN_ADMIN}) is not None
    with pytest.raises(AuthorizationError):
        require_principal_type(_owner(), {TYPE_ORVN_ADMIN})
    with pytest.raises(AuthorizationError):
        require_principal_type(None, {TYPE_ORVN_ADMIN})


def test_require_brokerage_scope():
    assert require_brokerage_scope(_owner("brk-A"), "brk-A") is not None
    with pytest.raises(AuthorizationError):
        require_brokerage_scope(_owner("brk-A"), "brk-B")     # cross-tenant denied
    # admin is cross-tenant → passes for any brokerage
    assert require_brokerage_scope(_admin(), "brk-Z") is not None
    with pytest.raises(AuthorizationError):
        require_brokerage_scope(None, "brk-A")                # deny by default


def test_has_permission():
    assert has_permission(_owner(), "read_leads") is True
    assert has_permission(_owner(), "rotate_keys") is False
    assert has_permission(_admin(), "anything") is True       # admin implicitly all
    assert has_permission(None, "read_leads") is False


# ── legacy compatibility: existing auth unchanged ──────────────────
def test_existing_admin_require_admin_unchanged(monkeypatch):
    import app.routes.admin as admin
    from app.routes.admin import require_admin
    from fastapi import HTTPException
    monkeypatch.setattr(admin, "get_settings", lambda: _settings(ADMIN_API_KEY="k"))
    assert require_admin("k") is True
    with pytest.raises(HTTPException):
        require_admin("wrong")


def test_existing_ingestion_api_key_route_unchanged(monkeypatch):
    from fastapi.testclient import TestClient
    import app.routes.lead_ingestion as route_mod
    from app.main import app
    monkeypatch.setattr(route_mod, "get_brokerage_by_api_key", lambda k: {"id": "brk-A"})
    monkeypatch.setattr(route_mod, "ingest_digital_lead",
                        lambda payload, brokerage: {"status": "ingested", "source_mode": "digital_ingestion",
                                                    "brokerage_id": brokerage["id"], "source": payload.get("source")})
    with TestClient(app) as c:
        resp = c.post("/ingest/lead", headers={"X-API-Key": "pas_x"},
                      json={"source": "website_form", "phone": "2125551234"})
    assert resp.status_code == 201
