"""
Brokerage Portal API — self-serve dashboard endpoints for brokerage clients.

Auth: X-API-Key header matching the brokerage's api_key field in Supabase.
No admin key required — each brokerage only sees its own data.

Routes (all prefixed /portal):
  GET   /portal/overview              → KPI summary (calls, booking rate, best agent)
  GET   /portal/calls                 → paginated call history
  GET   /portal/leads                 → paginated lead memory
  PATCH /portal/leads/{lead_id}/status → update lead status
  GET   /portal/agents                → agent leaderboard + availability
  GET   /portal/bookings              → upcoming/past appointment list
  GET   /portal/insights              → intelligence cards (objections, intent, booking trend)
  GET   /portal/calculator-prefill    → real data to pre-fill the revenue calculator
  GET   /portal/training              → self-training history + current insights
  GET   /portal/settings              → current editable config
  PATCH /portal/settings              → update agent name, phone, Slack webhook
  GET   /portal/notifications         → notification preferences
  PATCH /portal/notifications         → update notification preferences
  POST  /portal/control               → pause | resume | add_property | remove_property
"""

import logging
from datetime import datetime, timedelta, timezone
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Header, Query

from pydantic import BaseModel

from app.db.booking_store import list_bookings
from app.db.brokerage_store import (
    get_brokerage_by_api_key,
    update_brokerage,
    set_brokerage_active,
    update_featured_properties,
)
from app.db.agent_store import list_agents, get_agent_leaderboard
from app.db.supabase_client import get_supabase
from app.services.intelligence.leakage import detect_leakage
from app.services.intelligence.queries import (
    callback_events,
    events_for_call,
    fetch_call_and_lead_context,
    recent_events,
)
from app.services.intelligence.sanitize import sanitize_event_for_portal
from app.services.intelligence.scoring import SCORING_VERSION

router = APIRouter()
logger = logging.getLogger("pas.portal")


# ───────────── MODELS ─────────────

class PortalSettingsUpdate(BaseModel):
    agent_name: Optional[str] = None
    agent_phone: Optional[str] = None
    slack_webhook_url: Optional[str] = None


class PortalControlBody(BaseModel):
    action: str                          # pause | resume | add_property | remove_property
    property_data: Optional[dict] = None # for add_property
    remove_index: Optional[int] = None   # for remove_property


class LeadStatusUpdate(BaseModel):
    status: str   # new | qualified | booked | transferred | nurture | not_ready | not_interested | do_not_call | closed


class NotificationConfigUpdate(BaseModel):
    notify_on_booking: Optional[bool] = None
    notify_on_transfer: Optional[bool] = None
    notify_on_high_intent: Optional[bool] = None
    notify_on_failure: Optional[bool] = None
    daily_summary: Optional[bool] = None
    weekly_report: Optional[bool] = None
    channels: Optional[list] = None


# ───────────── AUTH ─────────────

def require_brokerage(x_api_key: str = Header(...)):
    """Authenticate a brokerage client by API key. Returns the full brokerage record."""
    brokerage = get_brokerage_by_api_key(x_api_key)
    if not brokerage or brokerage.get("id") == "demo":
        raise HTTPException(status_code=401, detail="Invalid API key")
    # NOTE: active=False (paused) does NOT block dashboard access — clients must be
    # able to log in and resume. The active flag only gates call handling.
    return brokerage


# ───────────── ROUTES ─────────────

@router.get("/overview")
async def portal_overview(brokerage=Depends(require_brokerage)):
    """
    Dashboard KPIs: calls today, this week, booking rate, best agent, lead count.
    This is the first request the dashboard makes after login.
    """
    brokerage_id = brokerage["id"]
    db = get_supabase()
    now = datetime.now(timezone.utc)
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0).isoformat()
    week_start = (now - timedelta(days=7)).isoformat()

    try:
        calls_today = db.table("calls").select("id", count="exact").eq("brokerage_id", brokerage_id).gte("start_time", today_start).execute()
        calls_week = db.table("calls").select("id", count="exact").eq("brokerage_id", brokerage_id).gte("start_time", week_start).execute()
        booked_week = db.table("calls").select("id", count="exact").eq("brokerage_id", brokerage_id).eq("outcome", "booked").gte("start_time", week_start).execute()
        total_leads = db.table("leads").select("id", count="exact").eq("brokerage_id", brokerage_id).execute()
    except Exception as e:
        logger.error(f"portal_overview DB error for {brokerage_id}: {e}")
        raise HTTPException(status_code=500, detail="Failed to load dashboard data")

    agents = get_agent_leaderboard(brokerage_id)
    week_count = calls_week.count or 0
    booked_count = booked_week.count or 0
    booking_rate = round(booked_count * 100 / week_count, 1) if week_count else 0
    available_count = len([a for a in agents if a.get("status") == "available"])

    best_agent = agents[0] if agents else None
    training_config = brokerage.get("training_config") or {}

    return {
        "brokerage_name": brokerage["name"],
        "calls_today": calls_today.count or 0,
        "calls_this_week": week_count,
        "booked_this_week": booked_count,
        "booking_rate_pct": booking_rate,
        "total_leads": total_leads.count or 0,
        "available_agents": available_count,
        "total_agents": len(agents),
        "best_agent": {
            "name": best_agent["name"],
            "close_rate": float(best_agent.get("close_rate") or 0),
            "total_closed": best_agent.get("total_closed", 0),
            "total_assigned": best_agent.get("total_assigned", 0),
        } if best_agent else None,
        "training_version": brokerage.get("training_version", 0),
        "last_trained_at": training_config.get("trained_at"),
    }


@router.get("/calls")
async def portal_calls(
    limit: int = Query(default=20, le=50),
    offset: int = Query(default=0),
    outcome: Optional[str] = Query(default=None),
    brokerage=Depends(require_brokerage),
):
    """Paginated call history. Filter by outcome: booked | not_interested | incomplete | pending."""
    try:
        db = get_supabase()
        q = (
            db.table("calls")
            .select("id, phone_number, source, outcome, call_status, duration_seconds, summary, start_time")
            .eq("brokerage_id", brokerage["id"])
            .order("start_time", desc=True)
            .range(offset, offset + limit - 1)
        )
        if outcome:
            q = q.eq("outcome", outcome)
        result = q.execute()
        return {"calls": result.data or [], "offset": offset, "limit": limit}
    except Exception as e:
        logger.error(f"portal_calls error: {e}")
        raise HTTPException(status_code=500, detail="Failed to load calls")


@router.get("/leads")
async def portal_leads(
    limit: int = Query(default=20, le=50),
    offset: int = Query(default=0),
    brokerage=Depends(require_brokerage),
):
    """Paginated lead memory — every prospect PAS has spoken with for this brokerage."""
    try:
        db = get_supabase()
        result = (
            db.table("leads")
            .select("id, name, phone_number, intent, budget, timeline, total_calls, last_call_at, last_booked_at, updated_at")
            .eq("brokerage_id", brokerage["id"])
            .order("updated_at", desc=True)
            .range(offset, offset + limit - 1)
            .execute()
        )
        return {"leads": result.data or [], "offset": offset, "limit": limit}
    except Exception as e:
        logger.error(f"portal_leads error: {e}")
        raise HTTPException(status_code=500, detail="Failed to load leads")


@router.get("/agents")
async def portal_agents(brokerage=Depends(require_brokerage)):
    """Agent leaderboard ranked by close rate, with current availability."""
    brokerage_id = brokerage["id"]
    leaderboard = get_agent_leaderboard(brokerage_id)
    agents = list_agents(brokerage_id)
    available_count = len([a for a in agents if a.get("status") == "available"])
    return {
        "leaderboard": leaderboard,
        "available_count": available_count,
        "total_count": len(agents),
    }


@router.get("/calculator-prefill")
async def portal_calculator_prefill(brokerage=Depends(require_brokerage)):
    """
    Returns real brokerage data to pre-fill the revenue calculator.
    Monthly leads = calls in last 30 days.
    Close rate = average across all agents.
    Commission and ISA cost must be filled in manually (PAS does not store financials).
    """
    brokerage_id = brokerage["id"]
    try:
        db = get_supabase()
        month_ago = (datetime.now(timezone.utc) - timedelta(days=30)).isoformat()
        calls_30d = db.table("calls").select("id", count="exact").eq("brokerage_id", brokerage_id).gte("start_time", month_ago).execute()
        total_leads = db.table("leads").select("id", count="exact").eq("brokerage_id", brokerage_id).execute()
    except Exception as e:
        logger.error(f"portal_calculator_prefill error: {e}")
        raise HTTPException(status_code=500, detail="Failed to load calculator data")

    agents = get_agent_leaderboard(brokerage_id)
    avg_close_rate = 0.0
    if agents:
        rates = [float(a.get("close_rate") or 0) for a in agents]
        avg_close_rate = round(sum(rates) / len(rates), 1)

    return {
        "monthly_leads": calls_30d.count or 0,
        "crm_size": total_leads.count or 0,
        "avg_close_rate_pct": avg_close_rate,
        "note": "avg_commission and isa_cost must be filled in manually — PAS does not store financial figures",
    }


@router.get("/training")
async def portal_training(brokerage=Depends(require_brokerage)):
    """Self-training history — every Claude-generated improvement and the metrics at the time."""
    try:
        db = get_supabase()
        result = (
            db.table("training_logs")
            .select("version, calls_analyzed, booking_rate, insights, created_at")
            .eq("brokerage_id", brokerage["id"])
            .order("created_at", desc=True)
            .limit(10)
            .execute()
        )
    except Exception as e:
        logger.error(f"portal_training error: {e}")
        raise HTTPException(status_code=500, detail="Failed to load training data")

    config = brokerage.get("training_config") or {}
    return {
        "current_version": brokerage.get("training_version", 0),
        "last_trained_at": config.get("trained_at"),
        "insights": config.get("insights", {}),
        "history": result.data or [],
    }


@router.get("/settings")
async def portal_get_settings(brokerage=Depends(require_brokerage)):
    """Current brokerage config editable by the client."""
    return {
        "name": brokerage.get("name"),
        "agent_name": brokerage.get("agent_name", "Alex"),
        "agent_phone": brokerage.get("agent_phone", ""),
        "slack_webhook_url": brokerage.get("slack_webhook_url", ""),
        "featured_properties": brokerage.get("featured_properties") or [],
        "active": brokerage.get("active", True),
        "call_count": brokerage.get("call_count", 0),
    }


@router.patch("/settings")
async def portal_update_settings(body: PortalSettingsUpdate, brokerage=Depends(require_brokerage)):
    """Update agent name, backup phone, or Slack webhook — changes take effect on the next call."""
    changes = {k: v for k, v in body.model_dump().items() if v is not None}
    if not changes:
        raise HTTPException(status_code=400, detail="No fields to update.")
    ok = update_brokerage(brokerage["id"], changes)
    if not ok:
        raise HTTPException(status_code=500, detail="Update failed.")
    logger.info(f"Portal settings updated | brokerage={brokerage['id']} | fields={list(changes.keys())}")
    return {"status": "updated", "fields": list(changes.keys())}


@router.post("/control")
async def portal_control(body: PortalControlBody, brokerage=Depends(require_brokerage)):
    """
    Give PAS an instruction without going through the backend:
      pause           → stop accepting/making calls
      resume          → re-enable calls
      add_property    → push a featured property Alex mentions on calls
      remove_property → remove a featured property by list index
    """
    brokerage_id = brokerage["id"]

    if body.action == "pause":
        set_brokerage_active(brokerage_id, False)
        logger.info(f"PAS paused via portal | brokerage={brokerage_id}")
        return {"status": "paused", "active": False}

    elif body.action == "resume":
        set_brokerage_active(brokerage_id, True)
        logger.info(f"PAS resumed via portal | brokerage={brokerage_id}")
        return {"status": "resumed", "active": True}

    elif body.action == "add_property":
        if not body.property_data:
            raise HTTPException(status_code=400, detail="property_data required for add_property")
        props = list(brokerage.get("featured_properties") or [])
        props.append(body.property_data)
        update_featured_properties(brokerage_id, props)
        return {"status": "property_added", "total": len(props), "properties": props}

    elif body.action == "remove_property":
        if body.remove_index is None:
            raise HTTPException(status_code=400, detail="remove_index required for remove_property")
        props = list(brokerage.get("featured_properties") or [])
        if 0 <= body.remove_index < len(props):
            removed = props.pop(body.remove_index)
            update_featured_properties(brokerage_id, props)
            return {"status": "property_removed", "removed": removed, "total": len(props), "properties": props}
        raise HTTPException(status_code=400, detail=f"Index {body.remove_index} out of range.")

    else:
        raise HTTPException(status_code=400, detail=f"Unknown action '{body.action}'. Valid: pause | resume | add_property | remove_property")


# ───────────── BOOKINGS ─────────────

@router.get("/bookings")
async def portal_bookings(
    status: Optional[str] = Query(default=None),
    limit: int = Query(default=20, le=50),
    offset: int = Query(default=0),
    brokerage=Depends(require_brokerage),
):
    """
    Upcoming and past appointments booked by PAS.
    Filter by status: scheduled | completed | cancelled | no_show | rescheduled
    """
    brokerage_id = brokerage["id"]
    features = brokerage.get("features") or {}
    if not features.get("booking_enabled", True):
        raise HTTPException(status_code=403, detail="Booking feature is not enabled for this account.")

    bookings = list_bookings(brokerage_id, status=status, limit=limit, offset=offset)
    return {"bookings": bookings, "offset": offset, "limit": limit}


# ───────────── INSIGHTS ─────────────

@router.get("/insights")
async def portal_insights(brokerage=Depends(require_brokerage)):
    """
    AI intelligence cards — the brain of the brokerage dashboard.

    Returns:
      - top_objections: which objections PAS heard most
      - intent_breakdown: how many leads are high/medium/low intent
      - best_call_hours: hour-of-day breakdown of completed calls
      - booking_trend: daily booking count for the last 14 days
      - recent_training_insight: latest insight Claude produced
    """
    brokerage_id = brokerage["id"]
    features = brokerage.get("features") or {}
    if not features.get("insights_enabled", True):
        raise HTTPException(status_code=403, detail="Insights feature is not enabled for this account.")

    try:
        db = get_supabase()
        now = datetime.now(timezone.utc)
        two_weeks_ago = (now - timedelta(days=14)).isoformat()

        # Pull recent calls for analysis
        calls = (
            db.table("calls")
            .select("outcome, call_status, metadata, start_time, duration_seconds")
            .eq("brokerage_id", brokerage_id)
            .gte("start_time", two_weeks_ago)
            .execute()
            .data or []
        )

        # Top objections
        from collections import Counter
        objection_counter: Counter = Counter()
        intent_counter: Counter = Counter()
        hour_counter: Counter = Counter()

        for call in calls:
            meta = call.get("metadata") or {}
            for obj in meta.get("objections_detected") or []:
                cat = obj.get("category", "other")
                objection_counter[cat] += obj.get("count", 1)
            intent = meta.get("intent_level")
            if intent:
                intent_counter[intent] += 1
            if call.get("start_time"):
                try:
                    hour = datetime.fromisoformat(call["start_time"].replace("Z", "+00:00")).hour
                    hour_counter[hour] += 1
                except Exception:
                    pass

        top_objections = [
            {"category": c, "count": n}
            for c, n in objection_counter.most_common(5)
        ]

        # Booking trend: daily count over last 14 days
        bookings_14d = (
            db.table("bookings")
            .select("slot_time")
            .eq("brokerage_id", brokerage_id)
            .gte("slot_time", two_weeks_ago)
            .execute()
            .data or []
        )
        booking_by_day: Counter = Counter()
        for b in bookings_14d:
            if b.get("slot_time"):
                try:
                    day = b["slot_time"][:10]
                    booking_by_day[day] += 1
                except Exception:
                    pass
        booking_trend = [
            {"date": d, "bookings": booking_by_day[d]}
            for d in sorted(booking_by_day)
        ]

        # Latest Claude insight from training
        training_config = brokerage.get("training_config") or {}
        latest_insight = training_config.get("insights", {})

        return {
            "brokerage_id": brokerage_id,
            "period_days": 14,
            "top_objections": top_objections,
            "intent_breakdown": dict(intent_counter),
            "best_call_hours": [
                {"hour": h, "calls": hour_counter[h]}
                for h in sorted(hour_counter, key=lambda x: -hour_counter[x])[:6]
            ],
            "booking_trend": booking_trend,
            "latest_training_insight": latest_insight,
        }

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"portal_insights error for {brokerage_id}: {e}")
        raise HTTPException(status_code=500, detail="Failed to load insights")


# ───────────── LEAD STATUS ─────────────

# ───────────── CALL DETAIL ─────────────

@router.get("/calls/{call_id}")
async def portal_call_detail(call_id: str, brokerage=Depends(require_brokerage)):
    """Full call record (transcript, summary, metadata) scoped to the authenticated brokerage."""
    try:
        db = get_supabase()
        result = (
            db.table("calls")
            .select("*")
            .eq("id", call_id)
            .eq("brokerage_id", brokerage["id"])
            .limit(1)
            .execute()
        )
        if not result.data:
            raise HTTPException(status_code=404, detail="Call not found")
        return {"call": result.data[0]}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"portal_call_detail error: {e}")
        raise HTTPException(status_code=500, detail="Failed to load call")


# ───────────── LEAD DETAIL ─────────────

@router.get("/leads/{lead_id}")
async def portal_lead_detail(lead_id: str, brokerage=Depends(require_brokerage)):
    """Lead detail with call history for the authenticated brokerage."""
    try:
        db = get_supabase()
        result = (
            db.table("leads")
            .select("*")
            .eq("id", lead_id)
            .eq("brokerage_id", brokerage["id"])
            .limit(1)
            .execute()
        )
        if not result.data:
            raise HTTPException(status_code=404, detail="Lead not found")
        lead = result.data[0]
        calls_result = (
            db.table("calls")
            .select("id, outcome, call_status, duration_seconds, summary, start_time")
            .eq("brokerage_id", brokerage["id"])
            .eq("phone_number", lead["phone_number"])
            .order("start_time", desc=True)
            .limit(10)
            .execute()
        )
        return {"lead": lead, "calls": calls_result.data or []}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"portal_lead_detail error: {e}")
        raise HTTPException(status_code=500, detail="Failed to load lead")


# ───────────── AGENT CRUD (portal-scoped) ─────────────

class PortalAgentCreate(BaseModel):
    name: str
    phone: str = ""
    email: str = ""
    slack_member_id: str = ""
    specialties: list = []
    areas: list = []
    languages: list = ["en"]
    role: str = "agent"


class PortalAgentUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    slack_member_id: Optional[str] = None
    specialties: Optional[list] = None
    areas: Optional[list] = None
    languages: Optional[list] = None
    role: Optional[str] = None


class PortalAgentStatusUpdate(BaseModel):
    status: str  # available | busy | offline


@router.post("/agents", status_code=201)
async def portal_add_agent(body: PortalAgentCreate, brokerage=Depends(require_brokerage)):
    """Add a new agent to the authenticated brokerage."""
    from app.db.agent_store import create_agent
    try:
        agent = create_agent(brokerage["id"], body.model_dump())
        logger.info(f"Portal agent created | brokerage={brokerage['id']} | name={body.name}")
        return {"agent": agent}
    except Exception as e:
        logger.error(f"portal_add_agent error: {e}")
        raise HTTPException(status_code=500, detail="Failed to create agent")


@router.patch("/agents/{agent_id}")
async def portal_update_agent(agent_id: str, body: PortalAgentUpdate, brokerage=Depends(require_brokerage)):
    """Update an agent's profile. Only fields provided are changed."""
    from app.db.agent_store import update_agent, get_agent
    agent = get_agent(agent_id)
    if not agent or agent.get("brokerage_id") != brokerage["id"]:
        raise HTTPException(status_code=404, detail="Agent not found")
    updates = body.model_dump(exclude_unset=True)
    if not updates:
        raise HTTPException(status_code=400, detail="No fields to update")
    ok = update_agent(agent_id, updates)
    if not ok:
        raise HTTPException(status_code=500, detail="Update failed")
    return {"status": "updated", "agent_id": agent_id}


@router.delete("/agents/{agent_id}")
async def portal_delete_agent(agent_id: str, brokerage=Depends(require_brokerage)):
    """Remove an agent from the authenticated brokerage."""
    from app.db.agent_store import delete_agent, get_agent
    agent = get_agent(agent_id)
    if not agent or agent.get("brokerage_id") != brokerage["id"]:
        raise HTTPException(status_code=404, detail="Agent not found")
    ok = delete_agent(agent_id)
    if not ok:
        raise HTTPException(status_code=500, detail="Delete failed")
    return {"status": "deleted", "agent_id": agent_id}


@router.patch("/agents/{agent_id}/status")
async def portal_set_agent_status(
    agent_id: str,
    body: PortalAgentStatusUpdate,
    brokerage=Depends(require_brokerage),
):
    """Set agent availability: available | busy | offline."""
    from app.db.agent_store import set_agent_status, get_agent
    if body.status not in ("available", "busy", "offline"):
        raise HTTPException(status_code=400, detail="status must be: available | busy | offline")
    agent = get_agent(agent_id)
    if not agent or agent.get("brokerage_id") != brokerage["id"]:
        raise HTTPException(status_code=404, detail="Agent not found")
    ok = set_agent_status(agent_id, body.status)
    if not ok:
        raise HTTPException(status_code=500, detail="Status update failed")
    return {"status": "updated", "agent_id": agent_id, "new_status": body.status}


_VALID_LEAD_STATUSES = {
    "new", "qualified", "booked", "transferred",
    "nurture", "not_ready", "not_interested", "do_not_call", "closed",
}


@router.patch("/leads/{lead_id}/status")
async def portal_update_lead_status(
    lead_id: str,
    body: LeadStatusUpdate,
    brokerage=Depends(require_brokerage),
):
    """Update the qualification status of a lead in the brokerage's CRM memory."""
    if body.status not in _VALID_LEAD_STATUSES:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid status '{body.status}'. Valid: {', '.join(sorted(_VALID_LEAD_STATUSES))}",
        )
    try:
        db = get_supabase()
        result = db.table("leads").select("id").eq("id", lead_id).eq("brokerage_id", brokerage["id"]).limit(1).execute()
        if not result.data:
            raise HTTPException(status_code=404, detail="Lead not found")
        db.table("leads").update({
            "status": body.status,
            "updated_at": datetime.now(timezone.utc).isoformat(),
        }).eq("id", lead_id).execute()
        logger.info(f"Lead {lead_id} status set to {body.status} | brokerage={brokerage['id']}")
        return {"status": "updated", "lead_id": lead_id, "new_status": body.status}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"portal_update_lead_status error: {e}")
        raise HTTPException(status_code=500, detail="Failed to update lead status")


# ───────────── NOTIFICATIONS ─────────────

@router.get("/notifications")
async def portal_get_notifications(brokerage=Depends(require_brokerage)):
    """Return the brokerage's current notification preferences."""
    return {
        "brokerage_id": brokerage["id"],
        "notification_config": brokerage.get("notification_config") or {},
    }


@router.patch("/notifications")
async def portal_update_notifications(body: NotificationConfigUpdate, brokerage=Depends(require_brokerage)):
    """
    Update notification preferences. Only provided fields are changed.
    Changes take effect on the next qualifying event (booking, transfer, etc.).
    """
    updates = body.model_dump(exclude_unset=True)
    if not updates:
        raise HTTPException(status_code=400, detail="No fields provided.")

    existing = brokerage.get("notification_config") or {}
    merged = {**existing, **updates}

    ok = update_brokerage(brokerage["id"], {"notification_config": merged})
    if not ok:
        raise HTTPException(status_code=500, detail="Failed to save notification preferences.")

    logger.info(f"Notification config updated | brokerage={brokerage['id']} | fields={list(updates.keys())}")
    return {
        "status": "updated",
        "brokerage_id": brokerage["id"],
        "notification_config": merged,
    }


# ───────────── EVENT VISIBILITY + INTELLIGENCE (PAS129/PAS130) ─────────────

_PORTAL_CALLBACK_EVENT_TYPES = ("callback.requested", "call.ended_with_callback")
_PORTAL_SUMMARY_DEFAULT_DAYS = 7
_PORTAL_SUMMARY_MAX_EVENTS = 100


@router.get("/events/recent")
async def portal_events_recent(
    event_type: Optional[str] = Query(default=None),
    severity: Optional[str] = Query(default=None),
    since_iso: Optional[str] = Query(default=None),
    limit: int = Query(default=25, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    brokerage=Depends(require_brokerage),
):
    """Most recent pas_events for this brokerage. Payloads are sanitised."""
    events = recent_events(
        brokerage_id=brokerage["id"],
        event_type=event_type,
        severity=severity,
        since_iso=since_iso,
        limit=limit,
        offset=offset,
    )
    cleaned = [sanitize_event_for_portal(e) for e in events]
    return {
        "events": cleaned,
        "count": len(cleaned),
        "limit": limit,
        "offset": offset,
    }


@router.get("/callbacks")
async def portal_callbacks(
    since_iso: Optional[str] = Query(default=None),
    limit: int = Query(default=50, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    brokerage=Depends(require_brokerage),
):
    """Callback queue for this brokerage. Payloads are sanitised."""
    events = callback_events(
        brokerage_id=brokerage["id"],
        since_iso=since_iso,
        limit=limit,
        offset=offset,
    )
    cleaned = [sanitize_event_for_portal(e) for e in events]
    return {
        "events": cleaned,
        "count": len(cleaned),
        "limit": limit,
        "offset": offset,
    }


@router.get("/calls/{call_id}/timeline")
async def portal_call_timeline(call_id: str, brokerage=Depends(require_brokerage)):
    """
    Full event timeline for a single call. Sanitised payloads.

    SECURITY: must verify the call belongs to the authenticated brokerage
    BEFORE returning its timeline. Mirrors the portal_call_detail pattern.
    """
    if not call_id:
        raise HTTPException(status_code=400, detail="call_id required")
    try:
        db = get_supabase()
        result = (
            db.table("calls")
            .select("id")
            .eq("id", call_id)
            .eq("brokerage_id", brokerage["id"])
            .limit(1)
            .execute()
        )
        if not result.data:
            raise HTTPException(status_code=404, detail="Call not found")
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"portal_call_timeline ownership check failed for {call_id}: {e}")
        raise HTTPException(status_code=500, detail="Failed to verify call ownership")

    events = events_for_call(call_id, brokerage_id=brokerage["id"])
    cleaned = [sanitize_event_for_portal(e) for e in events]
    return {"call_id": call_id, "events": cleaned, "count": len(cleaned)}


@router.get("/intelligence/summary")
async def portal_intelligence_summary(
    since_iso: Optional[str] = Query(default=None),
    brokerage=Depends(require_brokerage),
):
    """
    Aggregate KPIs for this brokerage over a window (default 7 days).
    Counts only — no PII. Returns leakage-category breakdown.
    """
    from collections import Counter

    if not since_iso:
        since_iso = (
            datetime.now(timezone.utc) - timedelta(days=_PORTAL_SUMMARY_DEFAULT_DAYS)
        ).isoformat()

    events = recent_events(
        brokerage_id=brokerage["id"],
        since_iso=since_iso,
        limit=_PORTAL_SUMMARY_MAX_EVENTS,
    )

    by_category: Counter = Counter()
    by_severity: Counter = Counter()
    by_event_type: Counter = Counter()
    callback_count = 0
    by_call: dict = {}

    for e in events:
        by_category[(e or {}).get("event_category") or "unknown"] += 1
        by_severity[(e or {}).get("severity") or "unknown"] += 1
        by_event_type[(e or {}).get("event_type") or "unknown"] += 1
        if (e or {}).get("event_type") in _PORTAL_CALLBACK_EVENT_TYPES:
            callback_count += 1
        cid = (e or {}).get("call_id")
        if cid:
            by_call.setdefault(cid, []).append(e)

    # Enrich detect_leakage with real call + lead context. Without these
    # rows, response_leakage / qualification_leakage / DNC paths cannot
    # classify correctly. Fetches degrade to {} on failure (never raise).
    # Brokerage filter forced — defence in depth against stray foreign ids.
    distinct_lead_ids = {(e or {}).get("lead_id") for e in events if (e or {}).get("lead_id")}
    calls_by_id, leads_by_id = fetch_call_and_lead_context(
        list(by_call.keys()),
        list(distinct_lead_ids),
        brokerage_id=brokerage["id"],
    )

    leakage_counts: Counter = Counter()
    for cid, evs in by_call.items():
        call_row = calls_by_id.get(cid, {})
        cid_lead_id = next(
            ((e or {}).get("lead_id") for e in evs if (e or {}).get("lead_id")),
            None,
        )
        lead_row = leads_by_id.get(cid_lead_id, {}) if cid_lead_id else {}
        leakage_counts[detect_leakage(lead_row, call_row, evs)] += 1

    return {
        "period_since": since_iso,
        "brokerage_id": brokerage["id"],
        "events_total": len(events),
        "events_by_category": dict(by_category),
        "events_by_severity": dict(by_severity),
        "events_by_type": dict(by_event_type),
        "callback_events_count": callback_count,
        "leakage_breakdown": dict(leakage_counts),
        "calls_analyzed": len(by_call),
        "version": SCORING_VERSION,
    }
