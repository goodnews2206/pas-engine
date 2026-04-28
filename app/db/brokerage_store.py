"""
Brokerage Store — per-tenant config: lookup, creation, and updates.

Each brokerage is identified by:
  - twilio_phone  → used by inbound/outbound Twilio webhook
  - id            → used by outbound trigger + admin API
  - api_key       → brokerage's credential for calling the PAS API

Falls back to a safe demo config when Supabase is unavailable.
"""

import logging
import secrets
from datetime import datetime, timezone
from typing import Optional

from app.db.supabase_client import get_supabase

logger = logging.getLogger("pas.brokerage")

_DEFAULT_BROKERAGE: dict = {
    "id": "demo",
    "name": "ORVN Realty",
    "agent_name": "Alex",
    "twilio_phone": "",
    "agent_phone": "",
    "slack_webhook_url": "",
    "slack_team_id": "",
    "slack_signing_secret": "",
    "api_key": "",
    "featured_properties": [],
    "active": True,
    "call_count": 0,
    "training_version": 0,
    "training_config": {},
}


def _row(row: dict) -> dict:
    return {
        "id": row.get("id", "demo"),
        "name": row.get("name", "ORVN Realty"),
        "agent_name": row.get("agent_name", "Alex"),
        "twilio_phone": row.get("twilio_phone", ""),
        "agent_phone": row.get("agent_phone", ""),
        "slack_webhook_url": row.get("slack_webhook_url", ""),
        "slack_team_id": row.get("slack_team_id", ""),
        "slack_signing_secret": row.get("slack_signing_secret", ""),
        "api_key": row.get("api_key", ""),
        "featured_properties": row.get("featured_properties") or [],
        "active": row.get("active", True),
        "call_count": row.get("call_count", 0),
        "training_version": row.get("training_version", 0),
        "training_config": row.get("training_config") or {},
    }


# ───────────── LOOKUPS ─────────────

def get_brokerage_by_phone(twilio_phone: str) -> dict:
    try:
        db = get_supabase()
        result = db.table("brokerages").select("*").eq("twilio_phone", twilio_phone).limit(1).execute()
        if result.data:
            return _row(result.data[0])
    except Exception as e:
        logger.warning(f"Brokerage lookup by phone failed: {e}")
    return dict(_DEFAULT_BROKERAGE)


def get_brokerage_by_id(brokerage_id: str) -> dict:
    try:
        db = get_supabase()
        result = db.table("brokerages").select("*").eq("id", brokerage_id).limit(1).execute()
        if result.data:
            return _row(result.data[0])
    except Exception as e:
        logger.warning(f"Brokerage lookup by id failed: {e}")
    return dict(_DEFAULT_BROKERAGE)


def get_brokerage_by_api_key(api_key: str) -> Optional[dict]:
    """Validates the brokerage's API key for authenticated endpoints."""
    if not api_key:
        return None
    try:
        db = get_supabase()
        result = db.table("brokerages").select("*").eq("api_key", api_key).limit(1).execute()
        if result.data:
            return _row(result.data[0])
    except Exception as e:
        logger.warning(f"Brokerage lookup by api_key failed: {e}")
    return None


def get_brokerage_by_slack_team(team_id: str) -> Optional[dict]:
    try:
        db = get_supabase()
        result = db.table("brokerages").select("*").eq("slack_team_id", team_id).limit(1).execute()
        if result.data:
            return _row(result.data[0])
    except Exception as e:
        logger.warning(f"Brokerage lookup by slack_team failed: {e}")
    return None


def list_brokerages() -> list:
    try:
        db = get_supabase()
        result = db.table("brokerages").select("*").order("created_at", desc=True).execute()
        return [_row(r) for r in (result.data or [])]
    except Exception as e:
        logger.error(f"Failed to list brokerages: {e}")
        return []


# ───────────── CREATE / UPDATE ─────────────

def create_brokerage(data: dict) -> dict:
    """
    Create a new brokerage account.
    Generates a unique API key automatically.
    Returns the created brokerage dict.
    """
    now = datetime.now(timezone.utc).isoformat()
    api_key = "pas_" + secrets.token_urlsafe(32)

    payload = {
        "id": data["id"],
        "name": data["name"],
        "agent_name": data.get("agent_name", "Alex"),
        "twilio_phone": data.get("twilio_phone", ""),
        "agent_phone": data.get("agent_phone", ""),
        "slack_webhook_url": data.get("slack_webhook_url", ""),
        "slack_team_id": data.get("slack_team_id", ""),
        "slack_signing_secret": data.get("slack_signing_secret", ""),
        "api_key": api_key,
        "featured_properties": data.get("featured_properties", []),
        "active": True,
        "call_count": 0,
        "training_version": 0,
        "training_config": {},
        "created_at": now,
        "updated_at": now,
    }

    db = get_supabase()
    db.table("brokerages").insert(payload).execute()
    logger.info(f"Brokerage created | id={data['id']}")
    return _row(payload)


def update_brokerage(brokerage_id: str, updates: dict) -> bool:
    try:
        updates["updated_at"] = datetime.now(timezone.utc).isoformat()
        db = get_supabase()
        db.table("brokerages").update(updates).eq("id", brokerage_id).execute()
        logger.info(f"Brokerage updated | id={brokerage_id} | fields={list(updates.keys())}")
        return True
    except Exception as e:
        logger.error(f"Failed to update brokerage {brokerage_id}: {e}")
        return False


def rotate_api_key(brokerage_id: str) -> str:
    """Generate and store a new API key for a brokerage."""
    new_key = "pas_" + secrets.token_urlsafe(32)
    update_brokerage(brokerage_id, {"api_key": new_key})
    return new_key


# ───────────── CALL COUNT + ACTIVE FLAG ─────────────

def increment_call_count(brokerage_id: str) -> int:
    """
    Increments call_count atomically and returns the new count.
    Used to trigger self-training at the threshold.
    """
    if brokerage_id == "demo":
        return 0
    try:
        db = get_supabase()
        current = db.table("brokerages").select("call_count").eq("id", brokerage_id).limit(1).execute()
        count = (current.data[0].get("call_count") or 0) + 1 if current.data else 1
        db.table("brokerages").update({
            "call_count": count,
            "updated_at": datetime.now(timezone.utc).isoformat(),
        }).eq("id", brokerage_id).execute()
        return count
    except Exception as e:
        logger.warning(f"Failed to increment call count for {brokerage_id}: {e}")
        return 0


def set_brokerage_active(brokerage_id: str, active: bool) -> bool:
    return update_brokerage(brokerage_id, {"active": active})


def update_featured_properties(brokerage_id: str, properties: list) -> bool:
    return update_brokerage(brokerage_id, {"featured_properties": properties})


# ───────────── STATS ─────────────

def get_brokerage_stats(brokerage_id: str) -> dict:
    """Returns aggregate call stats for the admin dashboard."""
    try:
        db = get_supabase()
        calls = db.table("calls").select("outcome, call_status, duration_seconds").eq("brokerage_id", brokerage_id).execute().data or []
        leads = db.table("leads").select("id, last_booked_at").eq("brokerage_id", brokerage_id).execute().data or []
        training_logs = (
            db.table("training_logs")
            .select("version, booking_rate, trained_at:created_at")
            .eq("brokerage_id", brokerage_id)
            .order("created_at", desc=True)
            .limit(5)
            .execute()
            .data or []
        )
        total = len(calls)
        booked = sum(1 for c in calls if c["outcome"] == "booked")
        completed = sum(1 for c in calls if c["call_status"] == "completed")
        avg_duration = (
            round(sum(c["duration_seconds"] or 0 for c in calls) / completed, 1)
            if completed else 0
        )
        conversion = round(booked * 100 / completed, 1) if completed else 0
        return {
            "total_calls": total,
            "completed_calls": completed,
            "booked": booked,
            "conversion_pct": conversion,
            "avg_duration_seconds": avg_duration,
            "total_leads_in_memory": len(leads),
            "training_history": training_logs,
        }
    except Exception as e:
        logger.error(f"Stats query failed for {brokerage_id}: {e}")
        return {}
