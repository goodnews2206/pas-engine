"""PAS211J — Twilio webhook URL pinning + replay guard.

Hardens Twilio webhook authenticity ahead of paid-client voice traffic:

  * The signed URL used for signature verification is pinned to the configured
    BASE_URL and is NEVER rebuilt from spoofable X-Forwarded-* / Host headers.
  * A replayed signed request (identical X-Twilio-Signature on the same route)
    is rejected within a conservative TTL window; a distinct request is accepted.
  * Missing/invalid BASE_URL fails closed in production.
  * Explicit development remains usable without live Twilio signatures.
  * The PAS211D per-IP rate limits on /voice and /status stay intact.

These exercise the verification seam directly (no voice business logic) so the
security property — not the call flow — is what's under test.
"""
import inspect

import pytest
from fastapi import HTTPException
from starlette.requests import Request
from twilio.request_validator import RequestValidator

from app.config import Settings
import app.routes.twilio_webhook as tw
from app.utils import twilio_replay


_TOKEN = "test_auth_token_pas211j"
_PINNED_BASE = "https://pas.orvnlabs.com"


def _settings(**kw):
    base = {
        "ENVIRONMENT": "production",
        "BASE_URL": _PINNED_BASE,
        "TWILIO_AUTH_TOKEN": _TOKEN,
    }
    base.update(kw)
    return Settings(**base)


def _make_request(path="/twilio/voice", query=b"", headers=None):
    """Minimal ASGI POST request — enough for header/url/client access. We never
    call .form()/.body() here (form params are passed to the verifier directly)."""
    raw_headers = [(k.lower().encode(), v.encode()) for k, v in (headers or {}).items()]
    scope = {
        "type": "http",
        "method": "POST",
        "path": path,
        "raw_path": path.encode(),
        "query_string": query,
        "headers": raw_headers,
        "scheme": "http",
        "server": ("testserver", 80),
        "client": ("1.2.3.4", 5000),
    }
    return Request(scope)


def _sign(url, params, token=_TOKEN):
    return RequestValidator(token).compute_signature(url, params)


@pytest.fixture(autouse=True)
def _isolate(monkeypatch):
    # Pin module settings to a production posture and start each test with an
    # empty replay cache so cases don't leak signatures into one another.
    monkeypatch.setattr(tw, "settings", _settings())
    twilio_replay.reset()
    yield
    twilio_replay.reset()


# ── URL pinning ─────────────────────────────────────────────────────

def test_pinned_url_derives_from_base_url_not_request_host():
    req = _make_request("/twilio/voice", headers={"Host": "whatever", "X-Forwarded-Host": "evil"})
    assert tw._pinned_webhook_url(req) == f"{_PINNED_BASE}/twilio/voice"


def test_pinned_url_preserves_path_and_query():
    req = _make_request("/twilio/status", query=b"brokerage=42&x=y")
    assert tw._pinned_webhook_url(req) == f"{_PINNED_BASE}/twilio/status?brokerage=42&x=y"


def test_valid_signature_against_pinned_url_is_accepted():
    params = {"CallSid": "CA_ok", "From": "+15550001111"}
    sig = _sign(f"{_PINNED_BASE}/twilio/voice", params)
    req = _make_request("/twilio/voice", headers={"X-Twilio-Signature": sig})
    assert tw._verify_twilio(req, params) is True


def test_spoofed_forwarded_headers_do_not_change_verification_target():
    """A signature valid for the BASE_URL still validates even when an attacker
    sets X-Forwarded-Host / X-Forwarded-Proto / Host to a domain they control."""
    params = {"CallSid": "CA_ok", "From": "+15550001111"}
    good_sig = _sign(f"{_PINNED_BASE}/twilio/voice", params)
    req = _make_request("/twilio/voice", headers={
        "X-Twilio-Signature": good_sig,
        "X-Forwarded-Host": "evil.attacker.example",
        "X-Forwarded-Proto": "http",
        "Host": "evil.attacker.example",
    })
    assert tw._verify_twilio(req, params) is True


def test_signature_for_spoofed_host_url_is_rejected():
    """Conversely, a signature computed for the attacker-controlled host must
    FAIL — proof the forwarded headers cannot move the signed target."""
    params = {"CallSid": "CA_ok", "From": "+15550001111"}
    evil_sig = _sign("http://evil.attacker.example/twilio/voice", params)
    req = _make_request("/twilio/voice", headers={
        "X-Twilio-Signature": evil_sig,
        "X-Forwarded-Host": "evil.attacker.example",
        "X-Forwarded-Proto": "http",
    })
    assert tw._verify_twilio(req, params) is False


# ── Fail-closed on missing/invalid BASE_URL ─────────────────────────

@pytest.mark.parametrize("bad_base", ["", "   ", "pas.orvnlabs.com", "ftp://pas.orvnlabs.com"])
def test_missing_or_invalid_base_url_fails_closed(monkeypatch, bad_base):
    monkeypatch.setattr(tw, "settings", _settings(BASE_URL=bad_base))
    params = {"CallSid": "CA_ok"}
    # Even a "valid"-looking signature can't pass when there's no canonical URL.
    sig = _sign("https://anything/twilio/voice", params)
    req = _make_request("/twilio/voice", headers={"X-Twilio-Signature": sig})
    assert tw._pinned_webhook_url(req) == ""
    assert tw._verify_twilio(req, params) is False
    with pytest.raises(HTTPException) as e:
        tw._reject_unverified_or_replayed(req, params, "voice")
    assert e.value.status_code == 403


# ── Replay guard ────────────────────────────────────────────────────

def test_duplicate_signed_request_is_rejected_within_window():
    params = {"CallSid": "CA_replay", "From": "+15550002222"}
    sig = _sign(f"{_PINNED_BASE}/twilio/voice", params)
    req = _make_request("/twilio/voice", headers={"X-Twilio-Signature": sig})
    # First delivery is accepted (no raise).
    assert tw._reject_unverified_or_replayed(req, params, "voice") is None
    # Byte-for-byte replay of the same signed request is rejected.
    with pytest.raises(HTTPException) as e:
        tw._reject_unverified_or_replayed(req, params, "voice")
    assert e.value.status_code == 403
    assert "replay" in e.value.detail.lower()


def test_distinct_signed_request_is_accepted():
    p1 = {"CallSid": "CA_one", "From": "+15550003333"}
    p2 = {"CallSid": "CA_two", "From": "+15550004444"}
    r1 = _make_request("/twilio/voice", headers={"X-Twilio-Signature": _sign(f"{_PINNED_BASE}/twilio/voice", p1)})
    r2 = _make_request("/twilio/voice", headers={"X-Twilio-Signature": _sign(f"{_PINNED_BASE}/twilio/voice", p2)})
    assert tw._reject_unverified_or_replayed(r1, p1, "voice") is None
    # A genuinely different call (different CallSid -> different signature) passes.
    assert tw._reject_unverified_or_replayed(r2, p2, "voice") is None


def test_replay_guard_unit_is_deterministic():
    assert twilio_replay.is_replay("/twilio/voice", "sigA") is False
    assert twilio_replay.is_replay("/twilio/voice", "sigA") is True   # same -> replay
    assert twilio_replay.is_replay("/twilio/status", "sigA") is False  # other route -> distinct
    assert twilio_replay.is_replay("/twilio/voice", "sigB") is False   # other sig -> distinct
    # Empty signature is never a replay (dev mode, no live signatures).
    assert twilio_replay.is_replay("/twilio/voice", "") is False
    assert twilio_replay.is_replay("/twilio/voice", "") is False


# ── /twilio/status hardening + /voice end-to-end rejection ──────────

def test_twilio_voice_rejects_invalid_signature_in_production():
    from fastapi.testclient import TestClient
    from app.main import app
    with TestClient(app) as client:
        resp = client.post(
            "/twilio/voice",
            data={"CallSid": "CA1", "From": "+15550001111"},
            headers={"X-Twilio-Signature": "obviously-wrong"},
        )
    assert resp.status_code == 403


def test_twilio_status_rejects_invalid_signature_in_production():
    from fastapi.testclient import TestClient
    from app.main import app
    with TestClient(app) as client:
        resp = client.post(
            "/twilio/status",
            data={"CallSid": "CA1", "CallStatus": "completed"},
            headers={"X-Twilio-Signature": "obviously-wrong"},
        )
    assert resp.status_code == 403


def test_status_goes_through_same_pinned_verify_and_replay_gate():
    params = {"CallSid": "CA_status", "CallStatus": "completed", "CallDuration": "12"}
    sig = _sign(f"{_PINNED_BASE}/twilio/status", params)
    req = _make_request("/twilio/status", headers={"X-Twilio-Signature": sig})
    assert tw._reject_unverified_or_replayed(req, params, "status") is None
    with pytest.raises(HTTPException) as e:
        tw._reject_unverified_or_replayed(req, params, "status")
    assert e.value.status_code == 403


def test_voice_and_status_keep_rate_limit():
    """PAS211D per-IP throttles must survive PAS211J (source-level guard mirrors
    the PAS211D test so a refactor can't silently drop them)."""
    voice_src = inspect.getsource(tw.incoming_call)
    status_src = inspect.getsource(tw.call_status)
    assert "rate_limit(" in voice_src and "twilio_voice" in voice_src
    assert "rate_limit(" in status_src and "twilio_status" in status_src


# ── Development remains usable ───────────────────────────────────────

def test_development_skips_signature_and_replay(monkeypatch):
    monkeypatch.setattr(tw, "settings", _settings(ENVIRONMENT="development"))
    req = _make_request("/twilio/voice")  # no signature header at all
    # No raise, no replay bookkeeping — dev behaviour preserved.
    assert tw._reject_unverified_or_replayed(req, {}, "voice") is None
    assert tw._reject_unverified_or_replayed(req, {}, "voice") is None
    assert tw.settings.require_twilio_signature is False
