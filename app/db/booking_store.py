"""
Booking Store — tracks every appointment PAS creates.

A booking record is created whenever book_appointment() succeeds.
It is the primary evidence of PAS business value:
  - client can see upcoming appointments
  - admin can mark completed / no-show
  - analytics can measure booking→completion conversion

Statuses:
  scheduled | cancelled | rescheduled | completed | no_show | failed
"""

import logging
from datetime import datetime, timezone
from typing import Optional

from app.db.supabase_client import get_supabase

logger = logging.getLogger("pas.bookings")


def create_booking(
    booking_id: str,
    brokerage_id: str,
    call_sid: str,
    slot_time: str,
    lead_name: str = "",
    lead_phone: str = "",
    lead_email: str = "",
    notes: str = "",
    calcom_url: str = "",
    agent_id: Optional[str] = None,
    lead_id: Optional[str] = None,
) -> bool:
    """Insert a booking record after Cal.com confirms the appointment."""
    try:
        db = get_supabase()
        now = datetime.now(timezone.utc).isoformat()
        payload = {
            "id": booking_id,
            "brokerage_id": brokerage_id,
            "call_sid": call_sid,
            "status": "scheduled",
            "slot_time": slot_time,
            "lead_name": lead_name,
            "lead_phone": lead_phone,
            "lead_email": lead_email,
            "notes": notes,
            "calcom_url": calcom_url,
            "created_at": now,
            "updated_at": now,
        }
        if agent_id:
            payload["agent_id"] = agent_id
        if lead_id:
            payload["lead_id"] = lead_id

        db.table("bookings").insert(payload).execute()
        logger.info(f"Booking record created | id={booking_id} | brokerage={brokerage_id} | slot={slot_time}")
        return True
    except Exception as e:
        logger.error(f"Failed to create booking record {booking_id}: {e}")
        return False


def update_booking_status(booking_id: str, status: str, admin_note: str = "") -> bool:
    """Update booking status: completed | no_show | cancelled | rescheduled."""
    try:
        db = get_supabase()
        payload = {
            "status": status,
            "updated_at": datetime.now(timezone.utc).isoformat(),
        }
        if admin_note:
            payload["admin_note"] = admin_note
        db.table("bookings").update(payload).eq("id", booking_id).execute()
        logger.info(f"Booking {booking_id} status → {status}")
        return True
    except Exception as e:
        logger.error(f"update_booking_status failed for {booking_id}: {e}")
        return False


def list_bookings(
    brokerage_id: str,
    status: Optional[str] = None,
    limit: int = 25,
    offset: int = 0,
) -> list:
    """Return paginated bookings for a brokerage, newest first."""
    try:
        db = get_supabase()
        q = (
            db.table("bookings")
            .select("*")
            .eq("brokerage_id", brokerage_id)
            .order("slot_time", desc=True)
            .range(offset, offset + limit - 1)
        )
        if status:
            q = q.eq("status", status)
        return q.execute().data or []
    except Exception as e:
        logger.error(f"list_bookings failed for {brokerage_id}: {e}")
        return []


def get_booking(booking_id: str) -> Optional[dict]:
    try:
        db = get_supabase()
        result = db.table("bookings").select("*").eq("id", booking_id).limit(1).execute()
        return result.data[0] if result.data else None
    except Exception as e:
        logger.error(f"get_booking failed for {booking_id}: {e}")
        return None


def count_bookings_by_status(brokerage_id: str) -> dict:
    """Return count breakdown by status for the brokerage dashboard."""
    try:
        db = get_supabase()
        rows = (
            db.table("bookings")
            .select("status")
            .eq("brokerage_id", brokerage_id)
            .execute()
            .data or []
        )
        counts: dict = {}
        for row in rows:
            s = row.get("status", "unknown")
            counts[s] = counts.get(s, 0) + 1
        return counts
    except Exception as e:
        logger.error(f"count_bookings_by_status failed for {brokerage_id}: {e}")
        return {}
