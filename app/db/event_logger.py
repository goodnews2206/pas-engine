"""
Event Logger — append to pas_events.

Universal event sink for PAS. Every operationally interesting event (call
lifecycle, state transition, lead extraction, objection, booking, provider
failure, system error) flows through here.

Safety contract — nothing in PAS should break because event logging failed:
  - log_event() never raises; returns True/False.
  - log_event_bg() is fire-and-forget; runs the Supabase insert on a worker
    thread so the live audio loop is never stalled by HTTP latency.
  - Payload is truncated to ~8 KB before insert.
  - Invalid severity falls back to 'info'.

Usage:
    from app.db.event_logger import log_event, log_event_bg

    # Hot path (live call) — never await:
    log_event_bg(
        "state.transition",
        brokerage_id=brokerage_id,
        call_id=call_sid,
        state="BUDGET",
        event_category="call",
        event_source="state_machine",
        payload={"from": "INTENT", "to": "BUDGET"},
    )

    # Cold path (background task / route handler):
    log_event(
        "system.error",
        brokerage_id=brokerage_id,
        severity="error",
        payload={"service": "calcom", "message": "Booking failed"},
    )
"""

import asyncio
import json
import logging
import threading
from datetime import datetime, timezone
from typing import Optional

from app.db.supabase_client import get_supabase

logger = logging.getLogger("pas.event_logger")

VALID_SEVERITIES = {"debug", "info", "warning", "error", "critical"}

# Soft cap on serialized payload size. Keeps a single event row small enough
# that high-volume logging cannot blow up storage. Anything larger gets
# replaced with a marker — caller should reference call_id/lead_id instead
# of embedding large blobs.
_MAX_PAYLOAD_BYTES = 8 * 1024


def _normalize_severity(severity: Optional[str]) -> str:
    if not severity or severity not in VALID_SEVERITIES:
        return "info"
    return severity


def _truncate_payload(payload: Optional[dict]) -> dict:
    if not payload:
        return {}
    try:
        encoded = json.dumps(payload, default=str)
    except Exception as e:
        # `default=str` invokes repr() on unknown types, which can raise
        # arbitrary exceptions. Don't let a misbehaving payload field
        # break event logging — replace with a marker.
        logger.warning(f"event_logger: payload not JSON-serializable ({e}) — replacing with marker")
        return {"_payload_error": "not_json_serializable"}
    if len(encoded) <= _MAX_PAYLOAD_BYTES:
        return payload
    return {
        "_payload_truncated": True,
        "_original_bytes": len(encoded),
        "_excerpt": encoded[: _MAX_PAYLOAD_BYTES - 200],
    }


def log_event(
    event_type: str,
    *,
    brokerage_id: Optional[str] = None,
    call_id: Optional[str] = None,
    lead_id: Optional[str] = None,
    agent_id: Optional[str] = None,
    user_id: Optional[str] = None,
    event_category: Optional[str] = None,
    event_source: Optional[str] = None,
    provider: Optional[str] = None,
    state: Optional[str] = None,
    severity: str = "info",
    payload: Optional[dict] = None,
) -> bool:
    """
    Append an event row to pas_events. Synchronous Supabase POST.
    Never raises — returns False on any failure.

    For the live audio path, prefer log_event_bg() so a slow Supabase call
    cannot stall the call loop.
    """
    try:
        if not event_type:
            return False
        row = {
            "event_type": event_type,
            "event_category": event_category,
            "event_source": event_source,
            "severity": _normalize_severity(severity),
            "brokerage_id": brokerage_id,
            "call_id": call_id,
            "lead_id": lead_id,
            "agent_id": agent_id,
            "user_id": user_id,
            "provider": provider,
            "state": state,
            "payload": _truncate_payload(payload),
            "created_at": datetime.now(timezone.utc).isoformat(),
        }
        db = get_supabase()
        db.table("pas_events").insert(row).execute()
        return True
    except Exception as e:
        # Intentionally silent at error level — event logging must never
        # cascade. Keep this at warning so it's visible in server logs.
        logger.warning(f"log_event failed (non-critical) [{event_type}]: {e}")
        return False


def log_event_bg(
    event_type: str,
    *,
    brokerage_id: Optional[str] = None,
    call_id: Optional[str] = None,
    lead_id: Optional[str] = None,
    agent_id: Optional[str] = None,
    user_id: Optional[str] = None,
    event_category: Optional[str] = None,
    event_source: Optional[str] = None,
    provider: Optional[str] = None,
    state: Optional[str] = None,
    severity: str = "info",
    payload: Optional[dict] = None,
) -> None:
    """
    Fire-and-forget version of log_event.

    Schedules the synchronous Supabase insert on a background worker so the
    caller (live websocket audio path, state machine hot transitions) is
    never blocked by HTTP latency. Safe to call from sync or async code.
    Never raises.
    """
    kwargs = dict(
        brokerage_id=brokerage_id,
        call_id=call_id,
        lead_id=lead_id,
        agent_id=agent_id,
        user_id=user_id,
        event_category=event_category,
        event_source=event_source,
        provider=provider,
        state=state,
        severity=severity,
        payload=payload,
    )

    def _run():
        try:
            log_event(event_type, **kwargs)
        except Exception as e:  # belt-and-braces; log_event already swallows
            logger.warning(f"log_event_bg worker failed [{event_type}]: {e}")

    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None

    if loop is not None:
        # Inside an async context — schedule on the default executor so we
        # don't block the event loop on Supabase HTTP.
        try:
            loop.run_in_executor(None, _run)
            return
        except Exception as e:
            logger.warning(f"log_event_bg executor schedule failed [{event_type}]: {e}")

    # Sync caller (or executor schedule failed) — run on a daemon thread.
    try:
        threading.Thread(target=_run, daemon=True).start()
    except Exception as e:
        logger.warning(f"log_event_bg thread start failed [{event_type}]: {e}")
