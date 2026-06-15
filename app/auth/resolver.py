"""PAS211G.1 — principal resolver boundary.

Turns an inbound request's credentials into a :class:`Principal`, reusing the
EXISTING auth checks (constant-time admin-key compare; brokerage api-key lookup)
so this layer never drifts from production behaviour.

Scope of PAS211G.1 (deliberately narrow):
  * This boundary is SCAFFOLDING. No production route is forced through it yet
    (route migration is PAS211G.3). It exists so the verifier (PAS211G.2) and
    the scoped client (PAS211G.4) have a single seam to build on.
  * Legacy X-Admin-Key / X-API-Key resolve to principals so existing flows are
    representable without any behaviour change.
  * The JWT path is a SAFE STUB: it returns ``None`` while JWT is disabled and
    FAILS CLOSED (still ``None``) if enabled before real verification lands — it
    must never grant access without a verified token.
  * Unknown / invalid credentials resolve to ``None``. No secret is logged.
"""
from __future__ import annotations

import hmac
import logging
from typing import Optional

import jwt

from app.auth.principal import (
    ALL_PRINCIPAL_TYPES,
    AUTH_ADMIN_KEY,
    AUTH_BROKERAGE_API_KEY,
    AUTH_JWT,
    ROLE_ADMIN_LEGACY,
    ROLE_AGENT,
    ROLE_BROKERAGE_LEGACY,
    ROLE_OWNER,
    SOURCE_JWT,
    SOURCE_LEGACY_ADMIN,
    SOURCE_LEGACY_BROKERAGE,
    TYPE_AGENT,
    TYPE_BROKER_OWNER,
    TYPE_INTEGRATION_FORWARDER,
    TYPE_ORVN_ADMIN,
    TYPE_TEAM_LEAD,
    Principal,
)
from app.config import get_settings

logger = logging.getLogger("pas.auth.resolver")


def _admin_key_matches(presented: Optional[str]) -> bool:
    """Constant-time compare against ADMIN_API_KEY (mirrors admin.require_admin).
    Empty configured key or empty presentation always fails."""
    expected = get_settings().ADMIN_API_KEY or ""
    if not expected or not presented:
        return False
    return hmac.compare_digest(presented.encode("utf-8"), expected.encode("utf-8"))


def resolve_principal_from_admin_key(x_admin_key: Optional[str]) -> Optional[Principal]:
    """X-Admin-Key → ORVN_ADMIN principal (legacy auth). None if it doesn't match
    or legacy admin-key auth is disabled."""
    settings = get_settings()
    if not (settings.ENABLE_LEGACY_API_KEY_AUTH and settings.ENABLE_LEGACY_ADMIN_KEY_AUTH):
        return None
    if not _admin_key_matches(x_admin_key):
        return None
    return Principal(
        user_id="legacy:admin",
        email=None,
        role=ROLE_ADMIN_LEGACY,
        brokerage_id=None,
        source=SOURCE_LEGACY_ADMIN,
        principal_type=TYPE_ORVN_ADMIN,
        auth_method=AUTH_ADMIN_KEY,
    )


def resolve_principal_from_brokerage_api_key(
    x_api_key: Optional[str],
    *,
    surface: Optional[str] = None,
) -> Optional[Principal]:
    """X-API-Key → brokerage-scoped principal (legacy auth).

    ``surface="ingestion"`` resolves an INTEGRATION_FORWARDER (machine caller,
    ingest-only); any other surface resolves a BROKER_OWNER-equivalent (the same
    owner-equivalence the portal already grants legacy keys). None if the key is
    unknown/empty or legacy key auth is disabled.
    """
    settings = get_settings()
    if not (settings.ENABLE_LEGACY_API_KEY_AUTH and settings.ENABLE_LEGACY_BROKERAGE_KEY_AUTH):
        return None
    if not x_api_key:
        return None

    # Reuse the existing, hash-aware lookup — no drift from production auth.
    from app.db.brokerage_store import get_brokerage_by_api_key

    brokerage = get_brokerage_by_api_key(x_api_key)
    if not brokerage or not brokerage.get("id") or brokerage.get("id") == "demo":
        return None

    ptype = TYPE_INTEGRATION_FORWARDER if surface == "ingestion" else TYPE_BROKER_OWNER
    return Principal(
        user_id=f"legacy:{brokerage['id']}",
        email=None,
        role=ROLE_BROKERAGE_LEGACY,
        brokerage_id=brokerage["id"],
        source=SOURCE_LEGACY_BROKERAGE,
        principal_type=ptype,
        auth_method=AUTH_BROKERAGE_API_KEY,
    )


# Map a verified Supabase app-role claim onto the coarse PAS211G principal_type.
# Used ONLY when the token carries no explicit, recognised ``principal_type``
# claim. Conservative by design: a role we can't map leaves principal_type unset
# (``None``) rather than inventing a privileged type. (No ROLE_TEAM_LEAD constant
# exists yet — the literal mirrors the plan's future brokerage role, PAS301G.)
_JWT_ROLE_TO_TYPE = {
    ROLE_OWNER: TYPE_BROKER_OWNER,
    ROLE_AGENT: TYPE_AGENT,
    "team_lead": TYPE_TEAM_LEAD,
}


def _principal_from_claims(claims: dict) -> Optional[Principal]:
    """Build a Principal from ALREADY-VERIFIED JWT claims.

    Returns ``None`` when the token carries no usable subject — a production
    identity is never minted without a verified ``sub`` / ``user_id``. Tenant
    scope, role, and permissions come ONLY from verified claims; nothing is read
    from the request body or query (PAS doctrine: ``brokerage_id`` is never
    trusted from inbound payloads).
    """
    user_id = claims.get("sub") or claims.get("user_id")
    if not user_id:
        return None

    role = claims.get("role") or ""
    brokerage_id = claims.get("brokerage_id") or None
    email = claims.get("email") or None

    # principal_type: an explicit, RECOGNISED claim wins; otherwise infer from
    # the verified app role; otherwise leave unset (deny-by-default downstream).
    ptype = claims.get("principal_type")
    if ptype not in ALL_PRINCIPAL_TYPES:
        ptype = _JWT_ROLE_TO_TYPE.get(role)

    perms = claims.get("permissions")
    permissions = (
        tuple(p for p in perms if isinstance(p, str))
        if isinstance(perms, (list, tuple))
        else ()
    )

    session_id = claims.get("session_id") or claims.get("jti") or None

    return Principal(
        user_id=str(user_id),
        email=email,
        role=role,
        brokerage_id=brokerage_id,
        source=SOURCE_JWT,
        principal_type=ptype,
        permissions=permissions,
        auth_method=AUTH_JWT,
        session_id=session_id,
    )


def resolve_principal_from_jwt(token: Optional[str]) -> Optional[Principal]:
    """Bearer token → Principal via REAL Supabase JWT verification (PAS211G.2).

    Fail-closed at every step — returns ``None`` rather than a partial / zero-
    trust identity whenever anything is off:

      * ``JWT_AUTH_ENABLED`` is False (default)             → None (no Bearer auth)
      * ``SUPABASE_JWT_SECRET`` is missing                  → None (cannot verify)
      * no token                                            → None
      * malformed / unsupported-alg / ``alg=none`` / bad signature → None
      * expired                                             → None
      * wrong issuer  (when ``JWT_ISSUER`` is configured)   → None
      * wrong audience (when ``JWT_AUDIENCE`` is configured)→ None
      * no verified subject claim                           → None

    Verification is pinned to **HS256** (the Supabase Auth access-token signing
    algorithm); the token is NEVER decoded without signature verification for
    any trust decision, and ``alg=none`` is rejected. PAS211G.2 does NOT wire
    this into any route — route enforcement is PAS211G.3.
    """
    settings = get_settings()
    if not settings.JWT_AUTH_ENABLED:
        return None

    secret = settings.SUPABASE_JWT_SECRET or ""
    if not secret:
        logger.warning(
            "JWT_AUTH_ENABLED is true but SUPABASE_JWT_SECRET is empty — "
            "failing closed; Bearer token rejected."
        )
        return None

    if not token:
        return None

    decode_kwargs = {"algorithms": ["HS256"]}
    options: dict = {}
    if settings.JWT_AUDIENCE:
        decode_kwargs["audience"] = settings.JWT_AUDIENCE
    else:
        # Supabase tokens always carry aud="authenticated"; when no expected
        # audience is pinned we must NOT verify aud or every valid token fails.
        options["verify_aud"] = False
    if settings.JWT_ISSUER:
        decode_kwargs["issuer"] = settings.JWT_ISSUER
    if options:
        decode_kwargs["options"] = options

    try:
        claims = jwt.decode(token, secret, **decode_kwargs)
    except jwt.PyJWTError as exc:
        logger.warning("JWT verification rejected token: %s", type(exc).__name__)
        return None
    except Exception:  # pragma: no cover - defensive, never trust on error
        logger.warning("Unexpected error verifying JWT — failing closed.")
        return None

    return _principal_from_claims(claims)


# Backwards-compatible alias. PAS211G.1 shipped a fail-closed stub under this
# name; it now points at the real verifier so existing imports/exports keep
# working without any route-layer change.
resolve_principal_from_jwt_stub = resolve_principal_from_jwt


def extract_bearer_token(authorization: Optional[str]) -> Optional[str]:
    """Parse an ``Authorization`` header value → the bearer token, or None.

    Returns None for a missing, non-Bearer, or empty-token header. Shared by the
    resolver and by route dependencies (PAS211G.3) so Bearer parsing lives in one
    place.
    """
    auth = authorization or ""
    if auth.lower().startswith("bearer "):
        return auth[7:].strip() or None
    return None


def _bearer_token(request) -> Optional[str]:
    return extract_bearer_token(request.headers.get("Authorization"))


def _surface_for_path(path: str) -> Optional[str]:
    if path.startswith("/ingest"):
        return "ingestion"
    return None


def resolve_principal_from_request(request) -> Optional[Principal]:
    """Resolve a Principal from a FastAPI/Starlette request, in precedence
    order: verified JWT (stub) → X-Admin-Key → X-API-Key. Returns ``None`` when
    no credential resolves. No route is forced to use this in PAS211G.1.
    """
    # 1. JWT (real verification — PAS211G.2; still unwired from routes).
    principal = resolve_principal_from_jwt(_bearer_token(request))
    if principal is not None:
        return principal

    # 2. Admin key.
    principal = resolve_principal_from_admin_key(request.headers.get("X-Admin-Key"))
    if principal is not None:
        return principal

    # 3. Brokerage API key (surface-aware).
    principal = resolve_principal_from_brokerage_api_key(
        request.headers.get("X-API-Key"),
        surface=_surface_for_path(request.url.path),
    )
    return principal


__all__ = (
    "resolve_principal_from_request",
    "resolve_principal_from_admin_key",
    "resolve_principal_from_brokerage_api_key",
    "resolve_principal_from_jwt",
    "resolve_principal_from_jwt_stub",
    "extract_bearer_token",
)
