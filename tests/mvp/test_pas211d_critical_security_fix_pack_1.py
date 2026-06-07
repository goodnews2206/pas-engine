"""PAS211D — critical security fix pack 1.

Proves the PAS211C-audit critical/high exposures are closed:
  * /simulate-call: 404 in production; never writes an arbitrary tenant from the
    request body (anonymous callers are limited to the demo tenant).
  * /demo/token: 404 in production; CORS is not wildcard outside development;
    per-IP rate limited.
  * admin key comparison is constant-time (hmac.compare_digest) and behaviour is
    unchanged for valid/invalid keys.
  * client IP for rate limiting ignores spoofed X-Forwarded-For by default and
    only honours it under an explicit trusted-proxy opt-in.
  * newly added per-IP rate limits (onboarding /claim, /twilio/status) are wired.

All settings are constructed locally / monkeypatched — no DB, no network.
"""
import inspect
from types import SimpleNamespace

import pytest
from fastapi import HTTPException

from app.config import Settings, _PRODUCTION_INDICATOR_VARS


@pytest.fixture(autouse=True)
def _clean_env(monkeypatch):
    # Keep the host's own platform env from leaking production indicators, and
    # start each test with an empty rate-limit window.
    for var in _PRODUCTION_INDICATOR_VARS:
        monkeypatch.delenv(var, raising=False)
    import app.utils.rate_limiter as rl
    rl._windows.clear()
    yield
    rl._windows.clear()


def _settings(**kw):
    base = {"ENVIRONMENT": "development", "BASE_URL": "http://localhost:8000"}
    base.update(kw)
    return Settings(**base)


def _req(xff=None, host="9.9.9.9"):
    headers = {"X-Forwarded-For": xff} if xff else {}
    return SimpleNamespace(headers=headers, client=SimpleNamespace(host=host))


# ── config gate ─────────────────────────────────────────────────────
def test_demo_endpoints_disabled_in_production_by_default():
    assert _settings(ENVIRONMENT="production").demo_endpoints_allowed is False


def test_demo_endpoints_reenablable_in_production_explicitly():
    assert _settings(ENVIRONMENT="production", ENABLE_DEMO_ENDPOINTS=True).demo_endpoints_allowed is True


def test_demo_endpoints_open_outside_production():
    assert _settings(ENVIRONMENT="development").demo_endpoints_allowed is True
    assert _settings(ENVIRONMENT="staging").demo_endpoints_allowed is True


# ── /simulate-call ──────────────────────────────────────────────────
def test_simulate_call_404_in_production(monkeypatch):
    from fastapi.testclient import TestClient
    import app.routes.simulate as sim
    from app.main import app

    monkeypatch.setattr(sim, "get_settings", lambda: _settings(ENVIRONMENT="production"))
    with TestClient(app) as client:
        resp = client.post("/simulate-call", json={"brokerage_id": "demo", "message": ""})
    assert resp.status_code == 404


def test_simulate_authorization_blocks_anonymous_real_tenant(monkeypatch):
    import app.routes.simulate as sim

    # demo tenant: always allowed, no key needed.
    sim._authorize_simulation("demo", None)  # must not raise

    # real tenant without a key → 401.
    with pytest.raises(HTTPException) as e1:
        sim._authorize_simulation("brk-real", None)
    assert e1.value.status_code == 401

    # real tenant with an unknown key → 403.
    monkeypatch.setattr(sim, "get_brokerage_by_api_key", lambda k: None)
    with pytest.raises(HTTPException) as e2:
        sim._authorize_simulation("brk-real", "pas_bad")
    assert e2.value.status_code == 403

    # real tenant with a key belonging to a DIFFERENT tenant → 403 (no poisoning).
    monkeypatch.setattr(sim, "get_brokerage_by_api_key", lambda k: {"id": "brk-other"})
    with pytest.raises(HTTPException) as e3:
        sim._authorize_simulation("brk-real", "pas_other")
    assert e3.value.status_code == 403

    # real tenant with its OWN matching key → allowed.
    monkeypatch.setattr(sim, "get_brokerage_by_api_key", lambda k: {"id": "brk-real"})
    sim._authorize_simulation("brk-real", "pas_real")  # must not raise


def test_simulate_route_rejects_real_tenant_without_key(monkeypatch):
    from fastapi.testclient import TestClient
    import app.routes.simulate as sim
    from app.main import app

    monkeypatch.setattr(sim, "get_settings", lambda: _settings(ENVIRONMENT="development"))
    with TestClient(app) as client:
        resp = client.post("/simulate-call", json={"brokerage_id": "remax-miami", "message": ""})
    assert resp.status_code == 401  # cannot drive a real tenant anonymously


def test_simulate_available_in_dev_for_demo(monkeypatch):
    from fastapi.testclient import TestClient
    import app.routes.simulate as sim
    from app.main import app

    monkeypatch.setattr(sim, "get_settings", lambda: _settings(ENVIRONMENT="development"))
    monkeypatch.setattr(sim, "get_brokerage_by_id", lambda bid: {"id": "demo", "name": "Demo"})
    with TestClient(app) as client:
        resp = client.post("/simulate-call", json={"brokerage_id": "demo", "message": ""})
    # Reachable in dev (not gated): a session is created and a greeting returned.
    assert resp.status_code == 200
    assert resp.json().get("call_sid")


# ── /demo/token ─────────────────────────────────────────────────────
def test_demo_token_404_in_production(monkeypatch):
    from fastapi.testclient import TestClient
    import app.routes.demo as demo
    from app.main import app

    monkeypatch.setattr(demo, "get_settings", lambda: _settings(ENVIRONMENT="production"))
    with TestClient(app) as client:
        resp = client.get("/demo/token")
    assert resp.status_code == 404


def test_demo_token_cors_not_wildcard_outside_dev(monkeypatch):
    from fastapi.testclient import TestClient
    import app.routes.demo as demo
    from app.main import app

    prod = _settings(ENVIRONMENT="production", ENABLE_DEMO_ENDPOINTS=True,
                     BASE_URL="https://pas.orvnlabs.com")
    monkeypatch.setattr(demo, "get_settings", lambda: prod)
    with TestClient(app) as client:
        resp = client.get("/demo/token")  # 503 (no twilio cfg) but past the gate
    acao = resp.headers.get("access-control-allow-origin")
    assert acao != "*"
    assert acao == "https://pas.orvnlabs.com"


def test_demo_token_rate_limited(monkeypatch):
    from fastapi.testclient import TestClient
    import app.routes.demo as demo
    from app.main import app

    monkeypatch.setattr(demo, "get_settings", lambda: _settings(ENVIRONMENT="development"))
    with TestClient(app) as client:
        codes = [client.get("/demo/token").status_code for _ in range(11)]
    # First 10 pass the limiter (503 — demo not configured in test env); 11th is throttled.
    assert codes[:10] == [503] * 10
    assert codes[10] == 429


# ── admin constant-time compare ─────────────────────────────────────
def test_require_admin_uses_constant_time_compare():
    from app.routes.admin import require_admin
    src = inspect.getsource(require_admin)
    assert "compare_digest" in src
    assert "!=" not in src  # the old non-constant-time compare is gone


def test_require_admin_valid_and_invalid(monkeypatch):
    import app.routes.admin as admin
    from app.routes.admin import require_admin

    monkeypatch.setattr(admin, "get_settings", lambda: _settings(ADMIN_API_KEY="s3cret-key"))
    assert require_admin("s3cret-key") is True
    with pytest.raises(HTTPException) as e:
        require_admin("wrong")
    assert e.value.status_code == 401


def test_require_admin_empty_configured_key_rejects(monkeypatch):
    import app.routes.admin as admin
    from app.routes.admin import require_admin

    monkeypatch.setattr(admin, "get_settings", lambda: _settings(ADMIN_API_KEY=""))
    with pytest.raises(HTTPException) as e:
        require_admin("anything")
    assert e.value.status_code == 401


# ── client IP / X-Forwarded-For ─────────────────────────────────────
def test_xff_ignored_by_default(monkeypatch):
    import app.utils.rate_limiter as rl

    monkeypatch.setattr(rl, "get_settings", lambda: _settings(TRUST_PROXY_HEADERS=False))
    # Two different spoofed XFF values, same real peer → same bucket key.
    k1 = rl.client_ip(_req(xff="1.1.1.1", host="5.5.5.5"))
    k2 = rl.client_ip(_req(xff="2.2.2.2", host="5.5.5.5"))
    assert k1 == k2 == "5.5.5.5"


def test_xff_honoured_only_with_explicit_trusted_proxy(monkeypatch):
    import app.utils.rate_limiter as rl

    monkeypatch.setattr(rl, "get_settings", lambda: _settings(TRUST_PROXY_HEADERS=True))
    assert rl.client_ip(_req(xff="1.1.1.1, 2.2.2.2", host="5.5.5.5")) == "1.1.1.1"


def test_spoofed_xff_does_not_bypass_rate_limit(monkeypatch):
    import app.utils.rate_limiter as rl

    monkeypatch.setattr(rl, "get_settings", lambda: _settings(TRUST_PROXY_HEADERS=False))
    # Same peer, rotating XFF: all map to one bucket, so the limit still bites.
    key = rl.client_ip(_req(xff="rotate-1", host="7.7.7.7"))
    for _ in range(5):
        rl.rate_limit(key, max_requests=5, window_seconds=60)
    with pytest.raises(HTTPException) as e:
        rl.rate_limit(key, max_requests=5, window_seconds=60)
    assert e.value.status_code == 429


# ── newly added route rate limits ───────────────────────────────────
def test_onboarding_claim_is_rate_limited():
    from fastapi.testclient import TestClient
    from app.main import app

    with TestClient(app) as client:
        codes = [
            client.post("/onboarding/claim", json={"key": "bad-format"}).status_code
            for _ in range(11)
        ]
    # Invalid format → 400 (limiter runs first); the 11th request is throttled.
    assert codes[:10] == [400] * 10
    assert codes[10] == 429


def test_twilio_status_has_rate_limit():
    import app.routes.twilio_webhook as tw
    assert "rate_limit(" in inspect.getsource(tw.call_status)
    assert "twilio_status" in inspect.getsource(tw.call_status)
