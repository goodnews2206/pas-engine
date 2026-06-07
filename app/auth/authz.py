"""PAS211G.1 — pure authorization helpers.

Small, framework-free predicates over a :class:`Principal`. They do NOT raise
HTTP errors and are NOT wired into routes yet (route enforcement is PAS211G.3) —
keeping them pure makes them trivially testable now and reusable later behind a
FastAPI dependency.

``require_*`` raise :class:`AuthorizationError` on failure; ``has_permission``
returns a bool.
"""
from __future__ import annotations

from typing import Iterable, Optional

from app.auth.principal import Principal


class AuthorizationError(Exception):
    """Raised when a principal is missing or lacks the required type/scope."""


def has_permission(principal: Optional[Principal], permission: str) -> bool:
    """True if the principal holds ``permission``. ORVN admins implicitly hold
    every permission. A missing principal holds none."""
    if principal is None:
        return False
    if principal.is_admin:
        return True
    return permission in (principal.permissions or ())


def require_principal_type(
    principal: Optional[Principal],
    allowed: Iterable[str],
) -> Principal:
    """Return the principal if its ``principal_type`` is in ``allowed``; else
    raise AuthorizationError. A missing principal always fails (deny by default)."""
    allowed_set = set(allowed)
    if principal is None or principal.principal_type not in allowed_set:
        got = None if principal is None else principal.principal_type
        raise AuthorizationError(
            f"principal_type {got!r} not in allowed {sorted(allowed_set)!r}"
        )
    return principal


def require_brokerage_scope(
    principal: Optional[Principal],
    brokerage_id: str,
) -> Principal:
    """Return the principal if it may act on ``brokerage_id``; else raise.

    ORVN admins are cross-tenant and pass for any brokerage. Every other
    principal must be tenant-scoped to exactly ``brokerage_id``. A missing
    principal or a missing/blank target tenant always fails (deny by default).
    """
    if principal is None:
        raise AuthorizationError("no principal")
    if principal.is_admin:
        return principal
    if not brokerage_id:
        raise AuthorizationError("no target brokerage_id")
    if not principal.brokerage_id or principal.brokerage_id != brokerage_id:
        raise AuthorizationError(
            f"principal brokerage {principal.brokerage_id!r} != target {brokerage_id!r}"
        )
    return principal


__all__ = (
    "AuthorizationError",
    "has_permission",
    "require_principal_type",
    "require_brokerage_scope",
)
