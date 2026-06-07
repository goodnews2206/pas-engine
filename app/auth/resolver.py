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

from app.auth.principal import (
    AUTH_ADMIN_KEY,
    AUTH_BROKERAGE_API_KEY,
    ROLE_ADMIN_LEGACY,
    ROLE_BROKERAGE_LEGACY,
    SOURCE_LEGACY_ADMIN,
    SOURCE_LEGACY_BROKERAGE,
    TYPE_BROKER_OWNER,
    TYPE_INTEGRATION_FORWARDER,
    TYPE_ORVN_ADMIN,
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


def resolve_principal_from_jwt_stub(token: Optional[str]) -> Optional[Principal]:
    """JWT path — SAFE STUB (PAS211G.1).

    * JWT disabled (default) → ``None`` (no Bearer auth offered).
    * JWT enabled but verification not yet implemented → ``None`` (FAIL CLOSED).

    It NEVER constructs a Principal from an unverified token. Real HS256
    verification (Supabase Auth) lands in PAS211G.2.
    """
    if not get_settings().JWT_AUTH_ENABLED:
        return None
    if token:
        logger.warning(
            "JWT_AUTH_ENABLED is true but JWT verification is not implemented yet "
            "(PAS211G.2) — failing closed; Bearer token rejected."
        )
    return None


def _bearer_token(request) -> Optional[str]:
    auth = request.headers.get("Authorization") or ""
    if auth.lower().startswith("bearer "):
        return auth[7:].strip() or None
    return None


def _surface_for_path(path: str) -> Optional[str]:
    if path.startswith("/ingest"):
        return "ingestion"
    return None


def resolve_principal_from_request(request) -> Optional[Principal]:
    """Resolve a Principal from a FastAPI/Starlette request, in precedence
    order: verified JWT (stub) → X-Admin-Key → X-API-Key. Returns ``None`` when
    no credential resolves. No route is forced to use this in PAS211G.1.
    """
    # 1. JWT (safe stub — never grants in G.1).
    principal = resolve_principal_from_jwt_stub(_bearer_token(request))
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
    "resolve_principal_from_jwt_stub",
)
