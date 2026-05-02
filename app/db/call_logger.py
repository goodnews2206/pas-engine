"""
Call Logger — Supabase CRUD for the `calls` table

Lifecycle:
  create_call_record()      → on call start
  update_call_outcome()     → on call end (outcome + transcript + metadata)
  finalize_call_on_hangup() → on Twilio status callback (duration finalized)
"""

import logging
from datetime import datetime, timezone
from typing import Optional

from app.db.event_logger import log_event_bg
from app.db.supabase_client import get_supabase

logger = logging.getLogger("pas.call_logger")


async def create_call_record(
    call_sid: str,
    phone_number: str,
    email: str = "",
    source: str = "inbound",
    brokerage_id: str = "demo",
):
    """Insert a new call record when the call starts."""
    try:
        db = get_supabase()
        db.table("calls").insert({
            "id": call_sid,
            "brokerage_id": brokerage_id,
            "phone_number": phone_number,
            "email": email,
            "source": source,
            "start_time": datetime.now(timezone.utc).isoformat(),
            "call_status": "active",
            "outcome": "pending",
        }).execute()
        logger.info(f"[{call_sid}] Call record created | source={source} | brokerage={brokerage_id}")
        log_event_bg(
            "call.started",
            brokerage_id=brokerage_id,
            call_id=call_sid,
            event_category="call",
            event_source="call_logger",
            payload={"source": source},
        )
    except Exception as e:
        logger.error(f"[{call_sid}] Failed to create call record: {e}")


async def update_call_outcome(
    call_sid: str,
    outcome: str,
    transcript: Optional[str] = None,
    metadata: Optional[dict] = None,
    summary: Optional[str] = None,
    call_status: Optional[str] = None,
    duration_seconds: Optional[int] = None,
):
    """Update outcome + transcript + summary + optional status when a call ends."""
    try:
        db = get_supabase()
        payload: dict = {
            "outcome": outcome,
            "end_time": datetime.now(timezone.utc).isoformat(),
        }
        if transcript:
            payload["transcript"] = transcript
        if metadata:
            payload["metadata"] = metadata
        if summary:
            payload["summary"] = summary
        if call_status:
            payload["call_status"] = call_status
        if duration_seconds is not None:
            payload["duration_seconds"] = duration_seconds

        db.table("calls").update(payload).eq("id", call_sid).execute()
        logger.info(f"[{call_sid}] Outcome updated: {outcome}")
    except Exception as e:
        logger.error(f"[{call_sid}] Failed to update outcome: {e}")


async def finalize_call_on_hangup(
    call_sid: str,
    duration_seconds: int,
    raw_status: str,
):
    """Finalize duration + status from Twilio status callback."""
    status_map = {
        "completed": "completed",
        "busy": "failed",
        "no-answer": "failed",
        "canceled": "dropped",
        "failed": "failed",
    }
    call_status = status_map.get(raw_status, "failed")

    try:
        db = get_supabase()
        db.table("calls").update({
            "duration_seconds": duration_seconds,
            "call_status": call_status,
        }).eq("id", call_sid).execute()
        logger.info(f"[{call_sid}] Finalized: status={call_status} duration={duration_seconds}s")
        if call_status in ("failed", "dropped"):
            log_event_bg(
                "call.failed",
                call_id=call_sid,
                event_category="call",
                event_source="call_logger",
                severity="warning",
                payload={
                    "raw_status": raw_status,
                    "mapped_status": call_status,
                    "duration_seconds": duration_seconds,
                },
            )
    except Exception as e:
        logger.error(f"[{call_sid}] Failed to finalize call: {e}")
