"""
Tests for app.auth.resolver real Supabase JWT verification (PAS211G.2).

Pure unit tests — no DB, no FastAPI, no network, no Supabase connection, no
.env reads. Settings are overridden in-process and test-local secrets are used.

Runnable directly:
    python tests/auth/test_jwt_resolver.py
"""

import base64
import contextlib
import json
import os
import sys
import time
import types

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")),
)

import jwt

from app.auth import resolver as R
from app.auth.principal import AUTH_JWT, SOURCE_JWT


# test-local secrets — never real Supabase secrets. Kept >= 64 bytes so HS256
# and HS512 test-token encoding doesn't emit RFC 7518 short-key warnings.
SECRET = "test-only-jwt-secret-do-not-use-in-prod-" + ("0123456789" * 4)
OTHER_SECRET = "a-different-test-secret-also-not-real-" + ("9876543210" * 4)


@contextlib.contextmanager
def _settings(enabled=True, secret=SECRET, audience="", issuer=""):
    """Swap resolver.get_settings for a fake so tests never touch env/.env.
    Avoids pytest fixtures so the file is also runnable directly."""
    fake = types.SimpleNamespace(
        JWT_AUTH_ENABLED=enabled,
        SUPABASE_JWT_SECRET=secret,
        JWT_AUDIENCE=audience,
        JWT_ISSUER=issuer,
    )
    original = R.get_settings
    R.get_settings = lambda: fake
    try:
        yield
    finally:
        R.get_settings = original


def _token(secret=SECRET, alg="HS256", *, exp_delta=3600, **claims):
    payload = {"sub": "user-1", "exp": int(time.time()) + exp_delta}
    payload.update(claims)
    return jwt.encode(payload, secret, algorithm=alg)


def _b64url(obj):
    return base64.urlsafe_b64encode(json.dumps(obj).encode()).rstrip(b"=").decode()


def _alg_none_token(**claims):
    """Hand-built alg=none token with an empty signature."""
    payload = {"sub": "user-1", "exp": int(time.time()) + 3600}
    payload.update(claims)
    return f"{_b64url({'alg': 'none', 'typ': 'JWT'})}.{_b64url(payload)}."


# ───────────── disabled / no-secret / no-token ─────────────

def test_disabled_returns_none_even_with_valid_token():
    token = _token()  # encoded outside the disabled context, with the real secret
    with _settings(enabled=False):
        assert R.resolve_principal_from_jwt(token) is None


def test_enabled_no_secret_returns_none():
    token = _token()
    with _settings(enabled=True, secret=""):
        assert R.resolve_principal_from_jwt(token) is None


def test_missing_token_returns_none():
    with _settings():
        assert R.resolve_principal_from_jwt(None) is None
        assert R.resolve_principal_from_jwt("") is None


# ───────────── bearer-header parsing (non-bearer / malformed) ─────────────

def _req(headers):
    return types.SimpleNamespace(headers=headers)


def test_non_bearer_authorization_header_yields_no_token():
    assert R._bearer_token(_req({"Authorization": "Basic dXNlcjpwYXNz"})) is None
    assert R._bearer_token(_req({})) is None
    assert R._bearer_token(_req({"Authorization": "Bearer "})) is None


def test_malformed_bearer_token_returns_none():
    with _settings():
        assert R.resolve_principal_from_jwt("not-a-jwt") is None
        assert R.resolve_principal_from_jwt("a.b.c.d.e") is None


# ───────────── valid tokens ─────────────

def test_valid_token_full_claims_returns_principal():
    with _settings(audience="authenticated", issuer="https://proj.supabase.co/auth/v1"):
        token = _token(
            sub="u-123",
            email="owner@brokerage.com",
            role="owner",
            brokerage_id="remax-miami",
            permissions=["leads:read", "calls:read"],
            session_id="sess-9",
            principal_type="BROKER_OWNER",
            aud="authenticated",
            iss="https://proj.supabase.co/auth/v1",
        )
        p = R.resolve_principal_from_jwt(token)
    assert p is not None
    assert p.user_id == "u-123"
    assert p.email == "owner@brokerage.com"
    assert p.role == "owner"
    assert p.brokerage_id == "remax-miami"
    assert p.principal_type == "BROKER_OWNER"
    assert p.permissions == ("leads:read", "calls:read")
    assert p.session_id == "sess-9"
    assert p.source == SOURCE_JWT
    assert p.auth_method == AUTH_JWT


def test_valid_token_minimal_claims_returns_low_trust_principal():
    """Only a subject — no role/brokerage. Must still verify, but yield a
    principal with no privileges (deny-by-default downstream)."""
    with _settings():
        p = R.resolve_principal_from_jwt(_token(sub="u-min"))
    assert p is not None
    assert p.user_id == "u-min"
    assert p.role == ""
    assert p.brokerage_id is None
    assert p.principal_type is None
    assert p.permissions == ()
    assert p.is_admin is False
    assert p.is_brokerage_user is False


def test_principal_type_inferred_from_role_when_claim_absent():
    with _settings():
        p_owner = R.resolve_principal_from_jwt(_token(role="owner", brokerage_id="b1"))
        p_agent = R.resolve_principal_from_jwt(_token(role="agent", brokerage_id="b1"))
    assert p_owner.principal_type == "BROKER_OWNER"
    assert p_agent.principal_type == "AGENT"


def test_unrecognised_explicit_principal_type_is_ignored():
    with _settings():
        p = R.resolve_principal_from_jwt(
            _token(role="owner", brokerage_id="b1", principal_type="GOD_MODE")
        )
    # garbage explicit type ignored; falls back to role inference
    assert p.principal_type == "BROKER_OWNER"


def test_session_id_falls_back_to_jti():
    with _settings():
        p = R.resolve_principal_from_jwt(_token(jti="jti-abc"))
    assert p.session_id == "jti-abc"


# ───────────── expiry / signature ─────────────

def test_expired_token_returns_none():
    with _settings():
        assert R.resolve_principal_from_jwt(_token(exp_delta=-60)) is None


def test_tampered_signature_returns_none():
    # signed with a different secret than the verifier is configured with
    bad = _token(secret=OTHER_SECRET)
    with _settings(secret=SECRET):
        assert R.resolve_principal_from_jwt(bad) is None


# ───────────── issuer / audience ─────────────

def test_wrong_issuer_returns_none_when_issuer_configured():
    with _settings(issuer="https://expected.supabase.co/auth/v1"):
        token = _token(iss="https://attacker.example.com")
        assert R.resolve_principal_from_jwt(token) is None


def test_correct_issuer_accepted():
    iss = "https://expected.supabase.co/auth/v1"
    with _settings(issuer=iss):
        assert R.resolve_principal_from_jwt(_token(iss=iss)) is not None


def test_wrong_audience_returns_none_when_audience_configured():
    with _settings(audience="authenticated"):
        token = _token(aud="some-other-audience")
        assert R.resolve_principal_from_jwt(token) is None


def test_correct_audience_accepted():
    with _settings(audience="authenticated"):
        assert R.resolve_principal_from_jwt(_token(aud="authenticated")) is not None


def test_token_with_aud_accepted_when_no_audience_configured():
    # Supabase always sets aud="authenticated"; with no pinned audience we must
    # not reject it.
    with _settings(audience=""):
        assert R.resolve_principal_from_jwt(_token(aud="authenticated")) is not None


# ───────────── subject required ─────────────

def test_missing_sub_returns_none():
    with _settings():
        # a token signed correctly but with no subject claim
        token = jwt.encode({"email": "x@y.com", "exp": int(time.time()) + 60}, SECRET, algorithm="HS256")
        assert R.resolve_principal_from_jwt(token) is None


# ───────────── algorithm hardening ─────────────

def test_alg_none_rejected():
    with _settings():
        assert R.resolve_principal_from_jwt(_alg_none_token()) is None


def test_unsupported_alg_rejected():
    # HS512 token must be rejected — verifier pins HS256 only.
    with _settings():
        assert R.resolve_principal_from_jwt(_token(alg="HS512")) is None


# ───────────── stub alias still callable ─────────────

def test_stub_alias_points_at_real_verifier():
    assert R.resolve_principal_from_jwt_stub is R.resolve_principal_from_jwt
    with _settings(enabled=False):
        assert R.resolve_principal_from_jwt_stub(_token()) is None


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
