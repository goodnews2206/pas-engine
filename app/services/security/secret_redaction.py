"""PAS211F — redact secret fields before a record leaves the API.

Admin list/detail responses must never echo a tenant's stored credentials. This
masks the known secret fields on a brokerage record (and, generically, any dict
key that looks secret) with a non-reversible marker. The raw API key is shown
ONLY once — at create/rotate — via the explicit ``keep_api_key=True`` flag.

Pure functions, no I/O, no dependency.
"""
from __future__ import annotations

from typing import Any, Dict

REDACTED = "***redacted***"

# Always-masked fields on a brokerage record returned by admin reads.
_BROKERAGE_SECRET_FIELDS = (
    "api_key",
    "api_key_hash",
    "slack_signing_secret",
    "slack_webhook_url",
)

# Generic key-name fragments — defence-in-depth for nested / unexpected shapes.
_SECRET_FRAGMENTS = (
    "api_key",
    "secret",
    "signing_secret",
    "webhook_url",
    "key_hash",
    "password",
    "private_key",
    "auth_token",
)


def _looks_secret(key: Any) -> bool:
    if not isinstance(key, str):
        return False
    k = key.lower()
    return any(frag in k for frag in _SECRET_FRAGMENTS)


def redact_secret_fields(value: Any, _depth: int = 0) -> Any:
    """Recursively mask any dict entry whose key looks secret."""
    if _depth > 6:
        return value
    if isinstance(value, dict):
        return {
            k: (REDACTED if _looks_secret(k) else redact_secret_fields(v, _depth + 1))
            for k, v in value.items()
        }
    if isinstance(value, (list, tuple)):
        return [redact_secret_fields(v, _depth + 1) for v in value]
    return value


def redact_brokerage(brokerage: Dict[str, Any], *, keep_api_key: bool = False) -> Dict[str, Any]:
    """Return a copy of a brokerage dict with secret fields masked.

    ``keep_api_key=True`` is used ONLY by the create/rotate one-time-display
    paths. ``slack_signing_secret`` and ``slack_webhook_url`` are ALWAYS masked.
    """
    if not isinstance(brokerage, dict):
        return brokerage
    out = dict(brokerage)
    for field in _BROKERAGE_SECRET_FIELDS:
        if field in out:
            if field == "api_key" and keep_api_key:
                continue
            out[field] = REDACTED
    return out


__all__ = ("REDACTED", "redact_brokerage", "redact_secret_fields")
