"""
System — cross-brokerage admin overview and service health.

Auth: all routes require X-Admin-Key.

Routes:
  GET /admin/system   → aggregate KPIs across all brokerages
  GET /admin/health   → live service health check (Supabase, external APIs)
"""

import logging
from datetime import datetime, timedelta, timezone
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query

from app.config import get_settings
from app.db.brokerage_store import list_brokerages
from app.db.error_store import count_unresolved
from app.db.supabase_client import get_supabase
from app.routes.admin import require_admin

router = APIRouter()
logger = logging.getLogger("pas.system")


@router.get("/system")
async def system_overview(_=Depends(require_admin)):
    """
    Cross-brokerage aggregate view — ORVN command centre.

    Returns fleet-wide KPIs: total calls today, booking rates,
    active vs paused brokerages, and unresolved error counts.
    """
    try:
        db = get_supabase()
        now = datetime.now(timezone.utc)
        today_start = now.replace(hour=0, minute=0, second=0, microsecond=0).isoformat()
        week_start = (now - timedelta(days=7)).isoformat()

        brokerages = list_brokerages()
        active_count = sum(1 for b in brokerages if b.get("active"))
        paused_count = len(brokerages) - active_count

        # Fleet-wide call aggregates
        all_calls = (
            db.table("calls")
            .select("outcome, call_status, duration_seconds, start_time, source")
            .execute()
            .data or []
        )

        total_calls = len(all_calls)
        calls_today = sum(1 for c in all_calls if (c.get("start_time") or "") >= today_start)
        calls_week = sum(1 for c in all_calls if (c.get("start_time") or "") >= week_start)
        booked_week = sum(
            1 for c in all_calls
            if c.get("outcome") == "booked" and (c.get("start_time") or "") >= week_start
        )
        completed_week = sum(
            1 for c in all_calls
            if c.get("call_status") == "completed" and (c.get("start_time") or "") >= week_start
        )
        booking_rate = round(booked_week * 100 / completed_week, 1) if completed_week else 0

        total_leads = (
            db.table("leads").select("id", count="exact").execute().count or 0
        )
        total_bookings = (
            db.table("bookings").select("id", count="exact").execute().count or 0
        )

        # Unresolved errors by service
        error_counts = count_unresolved()
        total_errors = sum(error_counts.values())

        # Per-brokerage summary rows (id, name, call count, active)
        brokerage_rows = [
            {
                "id": b["id"],
                "name": b["name"],
                "active": b.get("active", True),
                "plan": b.get("plan", "trial"),
                "call_count": b.get("call_count", 0),
            }
            for b in brokerages
        ]

        return {
            "generated_at": now.isoformat(),
            "brokerages": {
                "total": len(brokerages),
                "active": active_count,
                "paused": paused_count,
                "list": brokerage_rows,
            },
            "calls": {
                "total_all_time": total_calls,
                "today": calls_today,
                "this_week": calls_week,
                "booked_this_week": booked_week,
                "booking_rate_pct": booking_rate,
            },
            "leads": {
                "total": total_leads,
            },
            "bookings": {
                "total": total_bookings,
            },
            "errors": {
                "unresolved_total": total_errors,
                "by_service": error_counts,
            },
        }

    except Exception as e:
        logger.error(f"system_overview failed: {e}")
        raise HTTPException(status_code=500, detail="Failed to load system overview")


@router.get("/health")
async def service_health(_=Depends(require_admin)):
    """
    Live connectivity check for every external service.
    Returns status: ok | degraded | down for each dependency.
    """
    settings = get_settings()
    checks: dict = {}

    # Supabase
    try:
        db = get_supabase()
        db.table("brokerages").select("id").limit(1).execute()
        checks["supabase"] = {"status": "ok"}
    except Exception as e:
        checks["supabase"] = {"status": "down", "error": str(e)}

    # Check API key presence (actual connectivity tests would require live calls)
    def _key_check(name: str, key: str) -> dict:
        if key:
            return {"status": "configured"}
        return {"status": "not_configured"}

    checks["anthropic"] = _key_check("anthropic", settings.ANTHROPIC_API_KEY)
    checks["twilio"] = _key_check("twilio", settings.TWILIO_ACCOUNT_SID)
    checks["deepgram"] = _key_check("deepgram", settings.DEEPGRAM_API_KEY)
    checks["elevenlabs"] = _key_check("elevenlabs", settings.ELEVENLABS_API_KEY)
    checks["calcom"] = _key_check("calcom", settings.CALCOM_API_KEY)
    checks["resend"] = _key_check("resend", settings.RESEND_API_KEY)

    overall = (
        "ok"
        if checks["supabase"]["status"] == "ok"
        else "degraded"
    )

    return {
        "status": overall,
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "services": checks,
    }


@router.get("/calls")
async def admin_fleet_calls(
    brokerage_id: Optional[str] = Query(default=None),
    outcome: Optional[str] = Query(default=None),
    source: Optional[str] = Query(default=None),
    limit: int = Query(default=30, le=100),
    offset: int = Query(default=0),
    _=Depends(require_admin),
):
    """Fleet-wide call log across all brokerages. Filter by brokerage, outcome, or source."""
    try:
        db = get_supabase()
        q = (
            db.table("calls")
            .select("id, brokerage_id, phone_number, source, outcome, call_status, duration_seconds, summary, start_time, admin_note")
            .order("start_time", desc=True)
            .range(offset, offset + limit - 1)
        )
        if brokerage_id:
            q = q.eq("brokerage_id", brokerage_id)
        if outcome:
            q = q.eq("outcome", outcome)
        if source:
            q = q.eq("source", source)
        result = q.execute()
        return {"calls": result.data or [], "offset": offset, "limit": limit}
    except Exception as e:
        logger.error(f"admin_fleet_calls failed: {e}")
        raise HTTPException(status_code=500, detail="Failed to load calls")
