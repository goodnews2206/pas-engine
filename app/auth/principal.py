"""
Principal — the authenticated identity attached to a request.

A Principal represents whoever is making a request to /admin/* or /portal/*.
It is built either from a verified Supabase Auth JWT (preferred) or from a
legacy X-Admin-Key / X-API-Key match (transition only).

PAS133A defines the dataclass and helper properties. The resolver that
maps a FastAPI Request to a Principal lands in PAS133B; nothing in the
running app constructs Principals yet.

Role vocabulary
───────────────
JWT-sourced:
  admin           — ORVN operator, full /admin/* access
  owner           — brokerage owner, full /portal/* for their brokerage
  agent           — brokerage agent, scoped read/write within brokerage
  viewer          — brokerage read-only
  demo_viewer     — read-only access to the seeded demo brokerage only

Legacy-key-sourced (transition only, behind ENABLE_LEGACY_*_AUTH flags):
  admin_legacy        — synthetic principal for X-Admin-Key holders
  brokerage_legacy    — synthetic principal for X-API-Key holders (treated
                        as owner-equivalent for backward compatibility)

Source vocabulary
─────────────────
  jwt                  — verified Bearer token from Supabase Auth
  legacy_admin_key     — X-Admin-Key header
  legacy_brokerage_key — X-API-Key header
"""

from dataclasses import dataclass
from typing import Optional


# ───────────── role constants ─────────────

ROLE_ADMIN: str = "admin"
ROLE_ADMIN_LEGACY: str = "admin_legacy"
ROLE_OWNER: str = "owner"
ROLE_AGENT: str = "agent"
ROLE_VIEWER: str = "viewer"
ROLE_DEMO_VIEWER: str = "demo_viewer"
ROLE_BROKERAGE_LEGACY: str = "brokerage_legacy"


# ───────────── source constants ─────────────

SOURCE_JWT: str = "jwt"
SOURCE_LEGACY_ADMIN: str = "legacy_admin_key"
SOURCE_LEGACY_BROKERAGE: str = "legacy_brokerage_key"


# ───────────── role buckets ─────────────

# Roles that grant access to /admin/*. admin_legacy is a transition
# concession — once ENABLE_LEGACY_ADMIN_KEY_AUTH is off it can never
# be constructed.
_ADMIN_ROLES = frozenset({ROLE_ADMIN, ROLE_ADMIN_LEGACY})

# Roles that represent a brokerage-scoped user. brokerage_id MUST be
# present on the Principal for is_brokerage_user to be True.
_BROKERAGE_ROLES = frozenset({
    ROLE_OWNER,
    ROLE_AGENT,
    ROLE_VIEWER,
    ROLE_DEMO_VIEWER,
    ROLE_BROKERAGE_LEGACY,
})

# Roles that came from a legacy key, not a verified JWT.
_LEGACY_ROLES = frozenset({ROLE_ADMIN_LEGACY, ROLE_BROKERAGE_LEGACY})

# Sources that came from a legacy key (paired check — covers a Principal
# constructed with a non-legacy role label but a legacy source, which the
# resolver in PAS133B must never produce but defence-in-depth here).
_LEGACY_SOURCES = frozenset({SOURCE_LEGACY_ADMIN, SOURCE_LEGACY_BROKERAGE})


# ───────────── Principal ─────────────

@dataclass(frozen=True)
class Principal:
    """
    Immutable identity for one authenticated request.

    Frozen so handlers cannot mutate the principal mid-request — any
    role/scope change must come from a fresh authentication.
    """

    user_id: Optional[str]
    email: Optional[str]
    role: str
    brokerage_id: Optional[str]
    source: str

    # ── role helpers ──

    @property
    def is_admin(self) -> bool:
        """True for ORVN admins (JWT or legacy key)."""
        return self.role in _ADMIN_ROLES

    @property
    def is_brokerage_user(self) -> bool:
        """
        True for any brokerage-scoped principal (owner / agent / viewer /
        demo_viewer / brokerage_legacy) that has a brokerage_id set.
        A brokerage role without a brokerage_id is not a usable principal.
        """
        return self.role in _BROKERAGE_ROLES and bool(self.brokerage_id)

    @property
    def is_owner(self) -> bool:
        """
        True for the brokerage owner role. brokerage_legacy is included
        as a transition concession — legacy X-API-Key holders are treated
        as owner-equivalent until PAS133D turns the flag off.
        """
        return self.role in (ROLE_OWNER, ROLE_BROKERAGE_LEGACY)

    @property
    def is_agent(self) -> bool:
        return self.role == ROLE_AGENT

    @property
    def is_viewer(self) -> bool:
        return self.role == ROLE_VIEWER

    @property
    def is_demo_viewer(self) -> bool:
        return self.role == ROLE_DEMO_VIEWER

    @property
    def is_legacy(self) -> bool:
        """True if this principal was authenticated by a legacy key."""
        return self.role in _LEGACY_ROLES or self.source in _LEGACY_SOURCES
