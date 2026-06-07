"""
PAS auth package (PAS133 + PAS211G.1).

Holds the Principal model, the PAS211G principal-type / auth-method vocabulary,
the resolver boundary (app.auth.resolver), and pure authorization helpers
(app.auth.authz).

PAS211G.1 adds the resolver + authz scaffolding but does NOT enforce it on any
production route yet (route migration is PAS211G.3). X-Admin-Key and X-API-Key
auth in the existing routes is unchanged; the JWT path is a fail-closed stub.
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
    SOURCE_SLACK_SIGNATURE,
    SOURCE_TWILIO_SIGNATURE,
    SOURCE_SYSTEM,
    TYPE_ORVN_ADMIN,
    TYPE_BROKER_OWNER,
    TYPE_TEAM_LEAD,
    TYPE_AGENT,
    TYPE_INTEGRATION_FORWARDER,
    TYPE_SLACK_OPERATOR,
    TYPE_SYSTEM_WORKER,
    ALL_PRINCIPAL_TYPES,
    AUTH_ADMIN_KEY,
    AUTH_BROKERAGE_API_KEY,
    AUTH_JWT,
    AUTH_SLACK_SIGNATURE,
    AUTH_TWILIO_SIGNATURE,
    AUTH_SYSTEM,
)
from app.auth.authz import (
    AuthorizationError,
    has_permission,
    require_principal_type,
    require_brokerage_scope,
)
from app.auth.resolver import (
    resolve_principal_from_request,
    resolve_principal_from_admin_key,
    resolve_principal_from_brokerage_api_key,
    resolve_principal_from_jwt_stub,
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
    "SOURCE_SLACK_SIGNATURE",
    "SOURCE_TWILIO_SIGNATURE",
    "SOURCE_SYSTEM",
    "TYPE_ORVN_ADMIN",
    "TYPE_BROKER_OWNER",
    "TYPE_TEAM_LEAD",
    "TYPE_AGENT",
    "TYPE_INTEGRATION_FORWARDER",
    "TYPE_SLACK_OPERATOR",
    "TYPE_SYSTEM_WORKER",
    "ALL_PRINCIPAL_TYPES",
    "AUTH_ADMIN_KEY",
    "AUTH_BROKERAGE_API_KEY",
    "AUTH_JWT",
    "AUTH_SLACK_SIGNATURE",
    "AUTH_TWILIO_SIGNATURE",
    "AUTH_SYSTEM",
    "AuthorizationError",
    "has_permission",
    "require_principal_type",
    "require_brokerage_scope",
    "resolve_principal_from_request",
    "resolve_principal_from_admin_key",
    "resolve_principal_from_brokerage_api_key",
    "resolve_principal_from_jwt_stub",
]
