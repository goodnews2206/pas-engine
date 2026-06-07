"""
Lead Memory — persistent prospect records per brokerage.

Gives PAS context on returning callers:
  "Hi Marcus — welcome back. Last time you were looking to buy in the $400–500k range."

Also tracks total call count, last booking, and cumulative notes.
"""

import logging
from datetime import datetime, timezone
from typing import Optional

from app.db.event_logger import log_event_bg
from app.db.supabase_client import get_supabase
from app.services.security.pii_safety import mask_phone

logger = logging.getLogger("pas.memory")


def get_lead(brokerage_id: str, phone_number: str) -> Optional[dict]:
    """Return existing lead record or None. Never raises."""
    try:
        db = get_supabase()
        result = (
            db.table("leads")
            .select("*")
            .eq("brokerage_id", brokerage_id)
            .eq("phone_number", phone_number)
            .limit(1)
            .execute()
        )
        if result.data:
            return result.data[0]
    except Exception as e:
        logger.warning(f"Lead memory lookup failed for {mask_phone(phone_number)}: {e}")
    return None


def upsert_lead(brokerage_id: str, phone_number: str, updates: dict):
    """
    Create or update a lead record after a call ends.
    `updates` should contain any fields that changed this call.
    """
    try:
        db = get_supabase()
        now = datetime.now(timezone.utc).isoformat()

        # Fetch existing to merge notes
        existing = get_lead(brokerage_id, phone_number)
        if existing:
            # Merge cumulative notes
            old_notes = existing.get("notes") or ""
            new_note = updates.pop("notes", "")
            if new_note and new_note not in old_notes:
                updates["notes"] = (old_notes + "\n" + new_note).strip() if old_notes else new_note

            updates["total_calls"] = (existing.get("total_calls") or 0) + 1
            updates["updated_at"] = now
            db.table("leads").update(updates).eq("id", existing["id"]).execute()
            logger.info(f"Lead updated | brokerage={brokerage_id} | phone={mask_phone(phone_number)}")
            log_event_bg(
                "lead.updated",
                brokerage_id=brokerage_id,
                lead_id=existing.get("id"),
                event_category="lead",
                event_source="lead_memory",
                payload={
                    "is_new": False,
                    "fields_changed": sorted(updates.keys()),
                },
            )
        else:
            db.table("leads").insert({
                "brokerage_id": brokerage_id,
                "phone_number": phone_number,
                "total_calls": 1,
                "created_at": now,
                "updated_at": now,
                **updates,
            }).execute()
            logger.info(f"Lead created | brokerage={brokerage_id} | phone={mask_phone(phone_number)}")
            log_event_bg(
                "lead.updated",
                brokerage_id=brokerage_id,
                event_category="lead",
                event_source="lead_memory",
                payload={
                    "is_new": True,
                    "fields_changed": sorted(updates.keys()),
                },
            )
    except Exception as e:
        logger.error(f"Lead upsert failed for {mask_phone(phone_number)}: {e}")


def mark_booked(brokerage_id: str, phone_number: str):
    try:
        db = get_supabase()
        db.table("leads").update({
            "last_booked_at": datetime.now(timezone.utc).isoformat(),
            "updated_at": datetime.now(timezone.utc).isoformat(),
        }).eq("brokerage_id", brokerage_id).eq("phone_number", phone_number).execute()
    except Exception as e:
        logger.warning(f"mark_booked failed: {e}")
