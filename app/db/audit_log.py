"""
Audit Log — append to the audit_log table (PAS133A scaffolding).

Append-only record of security-relevant events:
    brokerage created / deactivated / reactivated
    invite generated / accepted / revoked
    user added / removed
    integration added / changed
    api_key rotated
    settings changed
    call/workflow viewed (sensitive read)

Safety contract — same shape as app.db.event_logger.log_event_bg:
  - log_audit() never raises; returns None.
  - Insert runs on a background worker so route handlers are never
    stalled by Supabase HTTP latency.
  - Payloads are recursively scrubbed of obvious secret-like keys
    BEFORE the row is constructed (api_key, password, token, secret,
    bearer, authorization, jwt, cookie, etc.). Values are replaced
    with the literal "***REDACTED***".
  - Payload is truncated to ~8 KB.
  - Invalid actor_type falls back to 'system'.

PAS133A: nothing in the running app calls this yet. It exists so that
PAS133B route changes can drop log_audit() calls into mutating handlers
without touching this module.

Usage (once wired in PAS133B):

    from app.db.audit_log import log_audit

    log_audit(
        "brokerage.created",
        actor=principal,                      # Principal or dict or None
        brokerage_id="remax-miami",
        target="remax-miami",
        payload={"name": "RE/MAX Miami"},     # secrets stripped automatically
        request_id=request.headers.get("x-request-id"),
        ip=request.client.host,
    )
"""

import asyncio
import json
import logging
import threading
from datetime import datetime, timezone
from typing import Any, Optional

from app.db.supabase_client import get_supabase

logger = logging.getLogger("pas.audit_log")

# Soft cap on serialized payload size — same threshold as pas_events.
_MAX_PAYLOAD_BYTES = 8 * 1024

# Schema CHECK on audit_log.actor_type. Must match scripts/migrate_v7.sql.
_VALID_ACTOR_TYPES = frozenset({"admin", "brokerage_user", "legacy_key", "system"})

# Substrings that mark a payload key as secret-like. Case-insensitive
# match: any key whose lower() contains one of these is redacted.
_SECRET_KEY_FRAGMENTS = (
    "api_key",
    "apikey",
    "password",
    "passwd",
    "token",                # access_token, refresh_token, setup_token, jwt token
    "secret",               # client_secret, signing_secret
    "authorization",
    "bearer",
    "key_hash",             # never re-emit a hashed credential
    "x-admin-key",
    "x-api-key",
    "private_key",
    "session",              # session_id, sb_access_session, etc.
    "cookie",
    "jwt",
)

_REDACTED = "***REDACTED***"

# Bound recursion for pathological nested payloads. Anything deeper just
# gets returned as-is — keys at depth > _MAX_REDACT_DEPTH are extremely
# unlikely to be meaningful audit data.
_MAX_REDACT_DEPTH = 6


# ───────────── helpers ─────────────

def _looks_secret(key: Any) -> bool:
    """True when a dict key name looks like it carries a secret."""
    if not isinstance(key, str):
        return False
    k = key.lower()
    return any(frag in k for frag in _SECRET_KEY_FRAGMENTS)


def _redact(value: Any, depth: int = 0) -> Any:
    """
    Walk a JSON-shaped value and replace any dict entry whose key looks
    secret with "***REDACTED***". Lists are recursed element-wise. All
    other types pass through.
    """
    if depth > _MAX_REDACT_DEPTH:
        return value
    if isinstance(value, dict):
        out: dict = {}
        for k, v in value.items():
            if _looks_secret(k):
                out[k] = _REDACTED
            else:
                out[k] = _redact(v, depth + 1)
        return out
    if isinstance(value, list):
        return [_redact(v, depth + 1) for v in value]
    if isinstance(value, tuple):
        return [_redact(v, depth + 1) for v in value]
    return value


def _truncate_payload(payload: Optional[dict]) -> dict:
    """Mirror event_logger._truncate_payload — same 8 KB ceiling, marker on overflow."""
    if not payload:
        return {}
    try:
        encoded = json.dumps(payload, default=str)
    except Exception as e:
        logger.warning(f"audit_log: payload not JSON-serializable ({e}) — replacing with marker")
        return {"_payload_error": "not_json_serializable"}
    if len(encoded) <= _MAX_PAYLOAD_BYTES:
        return payload
    return {
        "_payload_truncated": True,
        "_original_bytes": len(encoded),
        "_excerpt": encoded[: _MAX_PAYLOAD_BYTES - 200],
    }


def _actor_fields(actor: Any) -> tuple[Optional[str], Optional[str], str]:
    """
    Reduce an actor to (user_id, email, actor_type) where actor_type is
    one of the four schema-allowed values. Duck-types Principal-like
    objects so this module does not depend on app.auth.

    Acceptable shapes:
      None                      → (None, None, 'system')
      dict                      → reads 'user_id', 'email', 'actor_type'
      Principal (or any object  → reads .user_id, .email, derives type
        with the same surface)    from .is_legacy / .is_admin / .is_brokerage_user
    """
    if actor is None:
        return None, None, "system"

    if isinstance(actor, dict):
        user_id = actor.get("user_id")
        email = actor.get("email")
        explicit = actor.get("actor_type")
        if explicit in _VALID_ACTOR_TYPES:
            return user_id, email, explicit
        # No explicit actor_type — try to derive from a 'role' / 'source'
        # if the caller supplied one; otherwise fall through to 'system'.
        if actor.get("source", "").startswith("legacy_"):
            return user_id, email, "legacy_key"
        if actor.get("role") in ("admin", "admin_legacy"):
            return user_id, email, "legacy_key" if actor.get("role") == "admin_legacy" else "admin"
        if actor.get("brokerage_id"):
            return user_id, email, "brokerage_user"
        return user_id, email, "system"

    # Duck-type a Principal-like object.
    user_id = getattr(actor, "user_id", None)
    email = getattr(actor, "email", None)
    is_legacy = bool(getattr(actor, "is_legacy", False))
    if is_legacy:
        return user_id, email, "legacy_key"
    if bool(getattr(actor, "is_admin", False)):
        return user_id, email, "admin"
    if bool(getattr(actor, "is_brokerage_user", False)):
        return user_id, email, "brokerage_user"
    return user_id, email, "system"


def _build_row(
    event_type: str,
    *,
    actor: Any,
    brokerage_id: Optional[str],
    target: Optional[str],
    payload: Optional[dict],
    request_id: Optional[str],
    ip: Optional[str],
) -> dict:
    """Pure function — assemble the audit_log row dict, with redaction + truncation."""
    actor_user_id, actor_email, actor_type = _actor_fields(actor)

    redacted = _redact(payload) if payload else {}
    safe_payload = _truncate_payload(redacted if isinstance(redacted, dict) else {"_payload_error": "non_dict"})

    return {
        "occurred_at": datetime.now(timezone.utc).isoformat(),
        "actor_user_id": actor_user_id,
        "actor_email": actor_email,
        "actor_type": actor_type,
        "brokerage_id": brokerage_id,
        "event_type": event_type,
        "target": target,
        "payload": safe_payload,
        "request_id": request_id,
        "ip": ip,
    }


def _insert_audit(row: dict) -> bool:
    """
    Synchronous Supabase insert into audit_log. Never raises. Returns
    True on success, False on any failure (including Supabase not
    initialised — which is the expected state in unit tests).
    """
    try:
        db = get_supabase()
        db.table("audit_log").insert(row).execute()
        return True
    except Exception as e:
        # Audit failures must never cascade into the request path —
        # mirror event_logger's warning-level swallow.
        logger.warning(f"audit_log insert failed (non-critical) [{row.get('event_type')}]: {e}")
        return False


# ───────────── public API ─────────────

def log_audit(
    event_type: str,
    *,
    actor: Any = None,
    brokerage_id: Optional[str] = None,
    target: Optional[str] = None,
    payload: Optional[dict] = None,
    request_id: Optional[str] = None,
    ip: Optional[str] = None,
) -> None:
    """
    Append a row to audit_log without blocking the caller. Never raises.

    Schedules the synchronous Supabase insert on a background worker so
    request handlers (admin endpoints, portal endpoints) are not stalled
    by Supabase HTTP latency. Safe to call from sync or async code.

    Parameters
    ----------
    event_type : str
        Dotted event name, e.g. "brokerage.created", "invite.generated".
        Required — empty/missing names are dropped silently.
    actor : Principal | dict | None
        Who performed the action. None → recorded as actor_type='system'.
    brokerage_id : str | None
        Tenant scope. None for ORVN-wide events.
    target : str | None
        The id of the entity affected (brokerage_id, call_id, user_id, etc.).
    payload : dict | None
        Structured context. Any key matching common secret-like names is
        redacted before insert. Truncated to ~8 KB.
    request_id : str | None
        Correlation id from the inbound HTTP request, if present.
    ip : str | None
        Client IP for the row.
    """
    if not event_type:
        # Nothing to do — keep this silent so misuse cannot spam logs.
        return None

    try:
        row = _build_row(
            event_type,
            actor=actor,
            brokerage_id=brokerage_id,
            target=target,
            payload=payload,
            request_id=request_id,
            ip=ip,
        )
    except Exception as e:
        # _build_row should never raise (redaction + truncation each
        # swallow), but defence-in-depth — never let audit construction
        # crash a route.
        logger.warning(f"audit_log build failed (non-critical) [{event_type}]: {e}")
        return None

    def _run() -> None:
        try:
            _insert_audit(row)
        except Exception as e:  # belt-and-braces; _insert_audit already swallows
            logger.warning(f"audit_log worker failed [{event_type}]: {e}")

    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None

    if loop is not None:
        try:
            loop.run_in_executor(None, _run)
            return None
        except Exception as e:
            logger.warning(f"audit_log executor schedule failed [{event_type}]: {e}")

    try:
        threading.Thread(target=_run, daemon=True).start()
    except Exception as e:
        logger.warning(f"audit_log thread start failed [{event_type}]: {e}")

    return None
