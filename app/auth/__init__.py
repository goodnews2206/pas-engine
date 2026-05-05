"""
PAS auth package (PAS133).

Holds the Principal model and — once PAS133B lands — the JWT resolver
and FastAPI dependencies (require_admin_user, require_brokerage_user,
require_brokerage_owner, require_brokerage_member, require_demo_viewer,
assert_brokerage_scope).

PAS133A introduces only the Principal dataclass and role constants.
No route uses this package yet; X-Admin-Key and X-API-Key auth in the
existing routes is unchanged.
"""

from app.auth.principal import (  # re-export for ergonomic imports
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

__all__ = [
    "Principal",
    "ROLE_ADMIN",
    "ROLE_ADMIN_LEGACY",
    "ROLE_OWNER",
    "ROLE_AGENT",
    "ROLE_VIEWER",
    "ROLE_DEMO_VIEWER",
    "ROLE_BROKERAGE_LEGACY",
    "SOURCE_JWT",
    "SOURCE_LEGACY_ADMIN",
    "SOURCE_LEGACY_BROKERAGE",
]
