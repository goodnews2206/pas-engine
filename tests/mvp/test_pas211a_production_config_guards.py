"""PAS211A — production config + signature guard tests (RN-1, RN-2).

Narrow: RN-1 fail-fast on production-like host with non-production ENVIRONMENT;
RN-2 Twilio/Slack signature verification cannot be silently bypassed in
production; local development behaviour is preserved.
"""
import pytest

from app.config import Settings, _PRODUCTION_INDICATOR_VARS


@pytest.fixture(autouse=True)
def _clear_prod_indicators(monkeypatch):
    # Ensure the host's own env can't leak production indicators into tests.
    for var in _PRODUCTION_INDICATOR_VARS:
        monkeypatch.delenv(var, raising=False)
    yield


def _settings(**kw):
    base = {"ENVIRONMENT": "development", "BASE_URL": "http://localhost:8000"}
    base.update(kw)
    return Settings(**base)


# ── RN-1 ────────────────────────────────────────────────────────────

def test_local_development_does_not_fail_fast():
    s = _settings(ENVIRONMENT="development")
    assert s.looks_like_production() is False
    s.validate_runtime_security()  # must not raise


def test_prod_indicator_with_non_production_environment_fails_fast(monkeypatch):
    monkeypatch.setenv("RENDER", "1")
    s = _settings(ENVIRONMENT="development")
    assert s.looks_like_production() is True
    with pytest.raises(RuntimeError):
        s.validate_runtime_security()


def test_prod_indicator_with_unset_environment_fails_fast(monkeypatch):
    monkeypatch.setenv("FLY_APP_NAME", "pas")
    s = _settings(ENVIRONMENT="")  # unset / empty behaves as non-production
    with pytest.raises(RuntimeError):
        s.validate_runtime_security()


def test_https_base_url_is_a_production_indicator(monkeypatch):
    s = _settings(ENVIRONMENT="development", BASE_URL="https://pas.orvnlabs.com")
    assert "BASE_URL(https)" in s.production_indicators()
    with pytest.raises(RuntimeError):
        s.validate_runtime_security()


def test_prod_indicator_with_explicit_production_is_allowed(monkeypatch):
    monkeypatch.setenv("RAILWAY_PROJECT_ID", "abc123")
    s = _settings(ENVIRONMENT="production", BASE_URL="https://pas.orvnlabs.com")
    assert s.is_production is True
    s.validate_runtime_security()  # must not raise


def test_prod_value_alias_accepted(monkeypatch):
    monkeypatch.setenv("HEROKU_APP_NAME", "pas")
    s = _settings(ENVIRONMENT="prod")
    assert s.is_production is True
    s.validate_runtime_security()  # must not raise


# ── RN-2 (signature-verification seam) ──────────────────────────────

def test_require_twilio_signature_true_in_production():
    assert _settings(ENVIRONMENT="production").require_twilio_signature is True


def test_require_twilio_signature_true_for_non_dev_envs():
    # staging / test / anything-not-development enforces verification (fail-safe).
    assert _settings(ENVIRONMENT="staging").require_twilio_signature is True


def test_require_twilio_signature_false_only_in_explicit_development():
    assert _settings(ENVIRONMENT="development").require_twilio_signature is False


# ── RN-2 route-level enforcement ────────────────────────────────────

def test_twilio_voice_rejects_unsigned_request_in_production(monkeypatch):
    from fastapi.testclient import TestClient
    import app.routes.twilio_webhook as tw
    from app.main import app

    monkeypatch.setattr(tw, "settings", _settings(ENVIRONMENT="production"))
    with TestClient(app) as client:
        resp = client.post("/twilio/voice", data={"CallSid": "CA1", "From": "+15550001111"})
    assert resp.status_code == 403  # forged (unsigned) webhook rejected in prod


def test_twilio_status_rejects_unsigned_request_in_production(monkeypatch):
    from fastapi.testclient import TestClient
    import app.routes.twilio_webhook as tw
    from app.main import app

    monkeypatch.setattr(tw, "settings", _settings(ENVIRONMENT="production"))
    with TestClient(app) as client:
        resp = client.post("/twilio/status", data={"CallSid": "CA1", "CallStatus": "completed"})
    assert resp.status_code == 403


def test_slack_command_fails_closed_when_signing_secret_missing(monkeypatch):
    from fastapi.testclient import TestClient
    import app.routes.slack_command as sc
    from app.main import app

    # Linked brokerage but no signing secret configured → must reject, never allow.
    monkeypatch.setattr(
        sc, "get_brokerage_by_slack_team",
        lambda team_id: {"id": "brk-1", "slack_signing_secret": ""},
    )
    with TestClient(app) as client:
        resp = client.post(
            "/slack/command",
            data={"team_id": "T1", "text": "stats"},
        )
    assert resp.status_code == 403  # fail-closed, no silent bypass
