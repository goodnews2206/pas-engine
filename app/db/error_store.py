"""
Error Store — system error logging to Supabase.

Every external service failure (Twilio, Deepgram, ElevenLabs, Anthropic,
Cal.com, Supabase itself) is captured here. Makes failures visible and
actionable from the admin dashboard instead of buried in server logs.

Usage:
    from app.db.error_store import log_error
    await log_error("calcom", brokerage_id="remax-miami", message="Booking failed", ...)
"""

import logging
from datetime import datetime, timezone
from typing import Optional

from app.db.event_logger import log_event_bg
from app.db.supabase_client import get_supabase
from app.services.security.pii_safety import sanitize_error_message

logger = logging.getLogger("pas.error_store")

VALID_SERVICES = {
    "twilio", "deepgram", "elevenlabs", "anthropic",
    "calcom", "supabase", "system", "simulate", "portal",
}
VALID_SEVERITIES = {"debug", "info", "warning", "error", "critical"}


def log_error(
    service: str,
    message: str,
    brokerage_id: Optional[str] = None,
    call_sid: Optional[str] = None,
    severity: str = "error",
    detail: Optional[str] = None,
) -> bool:
    """
    Write an error record to the error_logs table.
    Also dual-writes to pas_events (system.error) so the universal event
    stream stays the single source of truth. error_logs is retained for
    the resolved/admin_note workflow.

    Never raises — if either DB write fails we fall back to standard
    logger only.
    """
    safe_service = service if service in VALID_SERVICES else "system"
    safe_severity = severity if severity in VALID_SEVERITIES else "error"

    # PAS211I: redact PII / secret-shaped tokens BEFORE the message/detail reach
    # pas_events, the error_logs table, or the admin dashboard. An upstream
    # exception can echo a phone/email or an Authorization bearer token.
    safe_message = sanitize_error_message(message, max_len=500)
    safe_detail = sanitize_error_message(detail, max_len=1000) if detail else None

    # Mirror to pas_events first (fire-and-forget, non-blocking).
    log_event_bg(
        "system.error",
        brokerage_id=brokerage_id,
        call_id=call_sid,
        event_category="ops",
        event_source="error_store",
        provider=safe_service if safe_service != "system" else None,
        severity=safe_severity,
        payload={
            "service": safe_service,
            "message": safe_message,
            "detail_excerpt": safe_detail,
        },
    )

    try:
        db = get_supabase()
        db.table("error_logs").insert({
            "service": safe_service,
            "brokerage_id": brokerage_id,
            "call_sid": call_sid,
            "severity": safe_severity,
            "message": safe_message,
            "detail": safe_detail,
            "resolved": False,
            "created_at": datetime.now(timezone.utc).isoformat(),
        }).execute()
        return True
    except Exception as e:
        # Intentionally silent — if DB logging fails, don't cascade
        logger.warning(f"error_store.log_error failed (non-critical): {e}")
        return False


def list_errors(
    resolved: Optional[bool] = None,
    service: Optional[str] = None,
    brokerage_id: Optional[str] = None,
    limit: int = 50,
    offset: int = 0,
) -> list:
    try:
        db = get_supabase()
        q = (
            db.table("error_logs")
            .select("*")
            .order("created_at", desc=True)
            .range(offset, offset + limit - 1)
        )
        if resolved is not None:
            q = q.eq("resolved", resolved)
        if service:
            q = q.eq("service", service)
        if brokerage_id:
            q = q.eq("brokerage_id", brokerage_id)
        return q.execute().data or []
    except Exception as e:
        logger.error(f"list_errors failed: {e}")
        return []


def resolve_error(error_id: str, admin_note: str = "") -> bool:
    try:
        db = get_supabase()
        payload = {
            "resolved": True,
            "resolved_at": datetime.now(timezone.utc).isoformat(),
        }
        if admin_note:
            payload["admin_note"] = admin_note
        db.table("error_logs").update(payload).eq("id", error_id).execute()
        return True
    except Exception as e:
        logger.error(f"resolve_error failed for {error_id}: {e}")
        return False


def count_unresolved() -> dict:
    """Returns unresolved error counts per service — for the admin health panel."""
    try:
        db = get_supabase()
        rows = (
            db.table("error_logs")
            .select("service")
            .eq("resolved", False)
            .execute()
            .data or []
        )
        counts: dict = {}
        for row in rows:
            svc = row.get("service", "system")
            counts[svc] = counts.get(svc, 0) + 1
        return counts
    except Exception as e:
        logger.warning(f"count_unresolved failed: {e}")
        return {}
