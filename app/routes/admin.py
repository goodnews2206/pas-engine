"""
Admin API — manage brokerage accounts, view stats, trigger self-training.

Auth: all routes require the X-Admin-Key header matching ADMIN_API_KEY in .env.

Routes:
  POST   /admin/brokerages                        → create a new brokerage account
  GET    /admin/brokerages                        → list all accounts
  GET    /admin/brokerages/{id}                   → account detail + live stats
  PATCH  /admin/brokerages/{id}                   → update config
  DELETE /admin/brokerages/{id}                   → deactivate (soft delete)
  POST   /admin/brokerages/{id}/train             → trigger self-training now
  POST   /admin/brokerages/{id}/rotate-key        → generate a new API key
  GET    /admin/brokerages/{id}/leads             → paginated lead memory
  GET    /admin/brokerages/{id}/calls             → recent call history
  GET    /admin/brokerages/{id}/metrics           → operational KPI dashboard
  POST   /admin/brokerages/{id}/invite            → generate onboarding invite key
  GET    /admin/brokerages/{id}/invite            → view current invite key status
  DELETE /admin/brokerages/{id}/invite            → revoke invite key
  GET    /admin/brokerages/{id}/features          → view feature flags
  PATCH  /admin/brokerages/{id}/features          → update feature flags
  GET    /admin/brokerages/{id}/bookings          → Cal.com bookings for brokerage
  GET    /admin/calls/{call_id}                   → full call detail with transcript
  PATCH  /admin/calls/{call_id}/note              → add admin note to a call
  GET    /admin/error-logs                        → system error logs
  PATCH  /admin/error-logs/{error_id}/resolve     → mark error resolved
"""

import hmac
import logging
from collections import Counter
from datetime import datetime, timedelta, timezone
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Header, Query
from pydantic import BaseModel

from app.config import get_settings
from app.db.brokerage_store import (
    create_brokerage,
    get_brokerage_by_id,
    get_brokerage_stats,
    list_brokerages,
    rotate_api_key,
    set_brokerage_active,
    update_brokerage,
    update_featured_properties,
)
from app.db.agent_store import list_agents
from app.db.booking_store import list_bookings
from app.db.error_store import list_errors, resolve_error
from app.db.invite_store import generate_invite_key, get_invite_status, revoke_invite_key
from app.db.supabase_client import get_supabase
from app.services.training.self_trainer import run_training

router = APIRouter()
logger = logging.getLogger("pas.admin")


# ───────────── AUTH ─────────────

def require_admin(x_admin_key: str = Header(...)):
    settings = get_settings()
    expected = settings.ADMIN_API_KEY or ""
    # PAS211D: constant-time compare so the admin secret can't be recovered
    # byte-by-byte via response-timing. An empty configured key always rejects.
    # (The weak/empty-key production startup refusal in main.py is unchanged.)
    if not expected or not hmac.compare_digest(
        (x_admin_key or "").encode("utf-8"), expected.encode("utf-8")
    ):
        raise HTTPException(status_code=401, detail="Invalid admin key")
    return True


# ───────────── MODELS ─────────────

class BrokerageCreate(BaseModel):
    id: str                             # "remax-miami" — URL-safe slug
    name: str                           # "RE/MAX Miami"
    agent_name: str = "Alex"
    twilio_phone: str = ""
    agent_phone: str = ""
    slack_webhook_url: str = ""
    slack_team_id: str = ""
    slack_signing_secret: str = ""
    # Operational config
    transfer_enabled: bool = True
    booking_enabled: bool = True
    ai_disclosure_enabled: bool = True
    max_objection_attempts: int = 2
    tone: str = "professional"          # professional | friendly | formal
    script_style: str = "default"
    market_location: str = ""
    after_hours_behavior: str = "callback"  # callback | voicemail | none
    calcom_event_type_id: int = 0


class BrokerageUpdate(BaseModel):
    name: Optional[str] = None
    agent_name: Optional[str] = None
    twilio_phone: Optional[str] = None
    agent_phone: Optional[str] = None
    slack_webhook_url: Optional[str] = None
    slack_team_id: Optional[str] = None
    slack_signing_secret: Optional[str] = None
    featured_properties: Optional[list] = None
    active: Optional[bool] = None
    # Owner / account fields
    owner_name: Optional[str] = None
    owner_email: Optional[str] = None
    owner_phone: Optional[str] = None
    company_website: Optional[str] = None
    crm_used: Optional[str] = None
    plan: Optional[str] = None
    billing_status: Optional[str] = None
    trial_ends_at: Optional[str] = None
    setup_fee_paid: Optional[bool] = None
    internal_notes: Optional[str] = None
    # Operational config (stored in config JSONB)
    transfer_enabled: Optional[bool] = None
    booking_enabled: Optional[bool] = None
    ai_disclosure_enabled: Optional[bool] = None
    max_objection_attempts: Optional[int] = None
    tone: Optional[str] = None
    script_style: Optional[str] = None
    market_location: Optional[str] = None
    after_hours_behavior: Optional[str] = None
    calcom_event_type_id: Optional[int] = None


class FeatureFlagsUpdate(BaseModel):
    simulation_enabled: Optional[bool] = None
    analytics_enabled: Optional[bool] = None
    insights_enabled: Optional[bool] = None
    reports_enabled: Optional[bool] = None
    self_training_enabled: Optional[bool] = None
    booking_enabled: Optional[bool] = None
    transfer_enabled: Optional[bool] = None
    sms_enabled: Optional[bool] = None
    email_notifications: Optional[bool] = None
    slack_notifications: Optional[bool] = None
    call_recording: Optional[bool] = None
    crm_sync: Optional[bool] = None


class CallNoteBody(BaseModel):
    note: str


class ErrorResolveBody(BaseModel):
    admin_note: str = ""


# ───────────── ROUTES ─────────────

@router.post("/brokerages", status_code=201)
async def create_account(body: BrokerageCreate, _=Depends(require_admin)):
    """Onboard a new brokerage. Returns the account including its generated API key."""
    existing = get_brokerage_by_id(body.id)
    if existing["id"] == body.id and existing["id"] != "demo":
        raise HTTPException(status_code=409, detail=f"Brokerage '{body.id}' already exists.")
    try:
        account = create_brokerage(body.model_dump())
        logger.info(f"Admin created brokerage: {body.id}")
        return {
            "brokerage": account,
            "note": "Save the api_key — it is shown only once and used for /outbound/call requests.",
        }
    except Exception as e:
        logger.error(f"Failed to create brokerage {body.id}: {e}")
        raise HTTPException(status_code=500, detail="Failed to create brokerage — check server logs.")


@router.get("/brokerages")
async def list_accounts(_=Depends(require_admin)):
    """List all brokerage accounts with high-level stats."""
    brokerages = list_brokerages()
    return {"brokerages": brokerages, "count": len(brokerages)}


@router.get("/brokerages/{brokerage_id}")
async def get_account(brokerage_id: str, _=Depends(require_admin)):
    """Full account detail with call stats and training history."""
    brokerage = get_brokerage_by_id(brokerage_id)
    if brokerage["id"] == "demo" and brokerage_id != "demo":
        raise HTTPException(status_code=404, detail="Brokerage not found")
    stats = get_brokerage_stats(brokerage_id)
    return {"brokerage": brokerage, "stats": stats}


@router.patch("/brokerages/{brokerage_id}")
async def update_account(brokerage_id: str, body: BrokerageUpdate, _=Depends(require_admin)):
    """Update any config field. Only provided fields are changed."""
    all_changes = body.model_dump(exclude_unset=True)
    if not all_changes:
        raise HTTPException(status_code=400, detail="No fields to update.")

    # Separate top-level DB columns from config JSONB fields
    _config_keys = {
        "transfer_enabled", "booking_enabled", "ai_disclosure_enabled",
        "max_objection_attempts", "tone", "script_style", "market_location",
        "after_hours_behavior", "calcom_event_type_id",
    }
    top_level = {k: v for k, v in all_changes.items() if k not in _config_keys}
    config_updates = {k: v for k, v in all_changes.items() if k in _config_keys}

    if config_updates:
        # Merge into existing config JSONB rather than overwriting it
        existing = get_brokerage_by_id(brokerage_id)
        if existing["id"] == "demo" and brokerage_id != "demo":
            raise HTTPException(status_code=404, detail="Brokerage not found")
        merged_config = {
            "transfer_enabled": existing.get("transfer_enabled", True),
            "booking_enabled": existing.get("booking_enabled", True),
            "ai_disclosure_enabled": existing.get("ai_disclosure_enabled", True),
            "max_objection_attempts": existing.get("max_objection_attempts", 2),
            "tone": existing.get("tone", "professional"),
            "script_style": existing.get("script_style", "default"),
            "market_location": existing.get("market_location", ""),
            "after_hours_behavior": existing.get("after_hours_behavior", "callback"),
            "calcom_event_type_id": existing.get("calcom_event_type_id", 0),
        }
        merged_config.update(config_updates)
        top_level["config"] = merged_config

    if not top_level:
        raise HTTPException(status_code=400, detail="No fields to update.")

    ok = update_brokerage(brokerage_id, top_level)
    if not ok:
        raise HTTPException(status_code=500, detail="Update failed — check Supabase connection.")
    return {"status": "updated", "fields": list(all_changes.keys())}


@router.delete("/brokerages/{brokerage_id}")
async def deactivate_account(brokerage_id: str, _=Depends(require_admin)):
    """Deactivate a brokerage (soft delete — data is preserved)."""
    ok = set_brokerage_active(brokerage_id, False)
    if not ok:
        raise HTTPException(status_code=500, detail="Deactivation failed.")
    return {"status": "deactivated", "brokerage_id": brokerage_id}


@router.post("/brokerages/{brokerage_id}/reactivate")
async def reactivate_account(brokerage_id: str, _=Depends(require_admin)):
    """Reactivate a previously paused brokerage."""
    ok = set_brokerage_active(brokerage_id, True)
    if not ok:
        raise HTTPException(status_code=500, detail="Reactivation failed.")
    return {"status": "reactivated", "brokerage_id": brokerage_id}


@router.post("/brokerages/{brokerage_id}/train")
async def trigger_training(brokerage_id: str, _=Depends(require_admin)):
    """
    Manually trigger a self-training run for a brokerage.
    Claude will analyse recent call transcripts and update the brokerage's scripts.
    """
    config = await run_training(brokerage_id)
    if not config:
        return {
            "status": "skipped",
            "reason": "Not enough completed call transcripts (minimum 5 required).",
        }
    return {
        "status": "trained",
        "insights": config.get("insights", {}),
        "booking_prompt_updated": bool(config.get("booking_prompt")),
        "objection_prompt_updated": bool(config.get("objection_system_prompt")),
    }


@router.post("/brokerages/{brokerage_id}/rotate-key")
async def rotate_key(brokerage_id: str, _=Depends(require_admin)):
    """Generate a new API key. The old key stops working immediately."""
    new_key = rotate_api_key(brokerage_id)
    if not new_key:
        raise HTTPException(status_code=500, detail="Key rotation failed.")
    return {
        "status": "rotated",
        "api_key": new_key,
        "note": "Update any integrations using the old key immediately.",
    }


@router.get("/brokerages/{brokerage_id}/leads")
async def get_leads(
    brokerage_id: str,
    limit: int = Query(default=25, le=100),
    offset: int = Query(default=0),
    _=Depends(require_admin),
):
    """Paginated lead memory for a brokerage."""
    try:
        db = get_supabase()
        result = (
            db.table("leads")
            .select("*")
            .eq("brokerage_id", brokerage_id)
            .order("updated_at", desc=True)
            .range(offset, offset + limit - 1)
            .execute()
        )
        return {"leads": result.data or [], "offset": offset, "limit": limit}
    except Exception as e:
        logger.error(f"Failed to fetch leads for brokerage {brokerage_id}: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch leads — check server logs.")


@router.get("/brokerages/{brokerage_id}/calls")
async def get_calls(
    brokerage_id: str,
    limit: int = Query(default=25, le=100),
    offset: int = Query(default=0),
    outcome: Optional[str] = Query(default=None),
    _=Depends(require_admin),
):
    """Recent call history for a brokerage, optionally filtered by outcome."""
    try:
        db = get_supabase()
        query = (
            db.table("calls")
            .select("id, phone_number, email, source, outcome, call_status, duration_seconds, summary, start_time")
            .eq("brokerage_id", brokerage_id)
            .order("start_time", desc=True)
            .range(offset, offset + limit - 1)
        )
        if outcome:
            query = query.eq("outcome", outcome)
        result = query.execute()
        return {"calls": result.data or [], "offset": offset, "limit": limit}
    except Exception as e:
        logger.error(f"Failed to fetch calls for brokerage {brokerage_id}: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch calls — check server logs.")


@router.get("/brokerages/{brokerage_id}/training")
async def get_training_history(brokerage_id: str, _=Depends(require_admin)):
    """Full training log — every Claude-generated improvement and the conversion rate at the time."""
    try:
        db = get_supabase()
        result = (
            db.table("training_logs")
            .select("*")
            .eq("brokerage_id", brokerage_id)
            .order("created_at", desc=True)
            .execute()
        )
        return {"training_logs": result.data or []}
    except Exception as e:
        logger.error(f"Failed to fetch training logs for brokerage {brokerage_id}: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch training history — check server logs.")


@router.get("/brokerages/{brokerage_id}/metrics")
async def get_metrics(brokerage_id: str, _=Depends(require_admin)):
    """
    Operational metrics dashboard for a brokerage.

    Returns all KPIs needed to show business value:
      - call volumes (today / this week / total)
      - booking rate, transfer rate
      - outcome distribution
      - top objections (from call metadata)
      - average call duration
      - agent availability
    """
    try:
        db = get_supabase()
        now = datetime.now(timezone.utc)
        today_start = now.replace(hour=0, minute=0, second=0, microsecond=0).isoformat()
        week_start = (now - timedelta(days=7)).isoformat()

        # Fetch all calls with the fields we need for aggregation
        all_calls = (
            db.table("calls")
            .select("outcome, call_status, duration_seconds, source, start_time, metadata")
            .eq("brokerage_id", brokerage_id)
            .execute()
            .data or []
        )

        total_calls = len(all_calls)
        completed = [c for c in all_calls if c.get("call_status") == "completed"]
        booked = [c for c in all_calls if c.get("outcome") == "booked"]
        transferred = [c for c in all_calls if c.get("outcome") == "transferred"]
        failed = [c for c in all_calls if c.get("call_status") in ("failed", "dropped")]
        simulated = [c for c in all_calls if c.get("source") == "simulated"]

        calls_today = [c for c in all_calls if (c.get("start_time") or "") >= today_start]
        calls_this_week = [c for c in all_calls if (c.get("start_time") or "") >= week_start]

        completed_count = len(completed)
        booking_rate = round(len(booked) * 100 / completed_count, 1) if completed_count else 0
        transfer_rate = round(len(transferred) * 100 / completed_count, 1) if completed_count else 0

        durations = [c["duration_seconds"] for c in completed if c.get("duration_seconds")]
        avg_duration = round(sum(durations) / len(durations), 1) if durations else 0

        # Aggregate objections from metadata JSONB
        objection_counter: Counter = Counter()
        for call in all_calls:
            meta = call.get("metadata") or {}
            for obj in meta.get("objections_detected") or []:
                cat = obj.get("category", "other")
                cnt = obj.get("count", 1)
                objection_counter[cat] += cnt

        top_objections = [
            {"category": cat, "count": cnt}
            for cat, cnt in objection_counter.most_common(5)
        ]

        # Lead count
        total_leads = (
            db.table("leads")
            .select("id", count="exact")
            .eq("brokerage_id", brokerage_id)
            .execute()
            .count or 0
        )

        # Agent availability
        agents = list_agents(brokerage_id)
        active_agents = len([a for a in agents if a.get("status") == "available"])

        return {
            "brokerage_id": brokerage_id,
            "total_calls": total_calls,
            "total_leads": total_leads,
            "booked_calls": len(booked),
            "transferred_calls": len(transferred),
            "failed_calls": len(failed),
            "simulated_calls": len(simulated),
            "booking_rate": booking_rate,
            "transfer_rate": transfer_rate,
            "top_objections": top_objections,
            "average_call_duration": avg_duration,
            "active_agents": active_agents,
            "total_agents": len(agents),
            "calls_today": len(calls_today),
            "calls_this_week": len(calls_this_week),
            "outcome_distribution": {
                "booked": len(booked),
                "transferred": len(transferred),
                "not_booked": len([c for c in all_calls if c.get("outcome") == "not_booked"]),
                "pending": len([c for c in all_calls if c.get("outcome") == "pending"]),
            },
        }
    except Exception as e:
        logger.error(f"Metrics query failed for {brokerage_id}: {e}")
        raise HTTPException(status_code=500, detail="Failed to load metrics — check server logs.")


# ───────────── INVITE KEY MANAGEMENT ─────────────

@router.post("/brokerages/{brokerage_id}/invite", status_code=201)
async def create_invite(brokerage_id: str, _=Depends(require_admin)):
    """
    Generate a one-time onboarding invite key for a brokerage.
    Any previously unused key for this brokerage is revoked first.
    The brokerage uses POST /onboarding/claim to exchange the key for their api_key.
    """
    brokerage = get_brokerage_by_id(brokerage_id)
    if brokerage["id"] == "demo" and brokerage_id != "demo":
        raise HTTPException(status_code=404, detail="Brokerage not found")
    result = generate_invite_key(brokerage_id)
    logger.info(f"Admin generated invite key for {brokerage_id}")
    return result


@router.get("/brokerages/{brokerage_id}/invite")
async def view_invite(brokerage_id: str, _=Depends(require_admin)):
    """View the current invite key status for a brokerage (does not expose the key itself)."""
    status = get_invite_status(brokerage_id)
    if not status:
        return {"status": "none", "brokerage_id": brokerage_id}
    return status


@router.delete("/brokerages/{brokerage_id}/invite")
async def delete_invite(brokerage_id: str, _=Depends(require_admin)):
    """Revoke all unused invite keys for a brokerage."""
    ok = revoke_invite_key(brokerage_id)
    if not ok:
        raise HTTPException(status_code=500, detail="Failed to revoke invite key.")
    return {"status": "revoked", "brokerage_id": brokerage_id}


# ───────────── FEATURE FLAGS ─────────────

@router.get("/brokerages/{brokerage_id}/features")
async def get_features(brokerage_id: str, _=Depends(require_admin)):
    """View which portal features are active for a brokerage."""
    brokerage = get_brokerage_by_id(brokerage_id)
    if brokerage["id"] == "demo" and brokerage_id != "demo":
        raise HTTPException(status_code=404, detail="Brokerage not found")
    return {
        "brokerage_id": brokerage_id,
        "features": brokerage.get("features", {}),
    }


@router.patch("/brokerages/{brokerage_id}/features")
async def update_features(brokerage_id: str, body: FeatureFlagsUpdate, _=Depends(require_admin)):
    """
    Enable or disable specific portal features for a brokerage.
    Only provided fields are changed — unset features keep their current value.
    """
    brokerage = get_brokerage_by_id(brokerage_id)
    if brokerage["id"] == "demo" and brokerage_id != "demo":
        raise HTTPException(status_code=404, detail="Brokerage not found")

    updates = body.model_dump(exclude_unset=True)
    if not updates:
        raise HTTPException(status_code=400, detail="No feature flags provided.")

    existing_features = brokerage.get("features") or {}
    merged = {**existing_features, **updates}

    ok = update_brokerage(brokerage_id, {"features": merged})
    if not ok:
        raise HTTPException(status_code=500, detail="Failed to update features.")

    logger.info(f"Feature flags updated | brokerage={brokerage_id} | changes={list(updates.keys())}")
    return {"status": "updated", "brokerage_id": brokerage_id, "features": merged}


# ───────────── BOOKINGS ─────────────

@router.get("/brokerages/{brokerage_id}/bookings")
async def get_bookings(
    brokerage_id: str,
    status: Optional[str] = Query(default=None),
    limit: int = Query(default=25, le=100),
    offset: int = Query(default=0),
    _=Depends(require_admin),
):
    """Paginated Cal.com bookings for a brokerage, optionally filtered by status."""
    bookings = list_bookings(brokerage_id, status=status, limit=limit, offset=offset)
    return {"bookings": bookings, "offset": offset, "limit": limit}


# ───────────── CALL DETAIL + NOTES ─────────────

@router.get("/calls/{call_id}")
async def get_call_detail(call_id: str, _=Depends(require_admin)):
    """Full call record including transcript, metadata, and summary."""
    try:
        db = get_supabase()
        result = db.table("calls").select("*").eq("id", call_id).limit(1).execute()
        if not result.data:
            raise HTTPException(status_code=404, detail="Call not found")
        return {"call": result.data[0]}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"get_call_detail failed for {call_id}: {e}")
        raise HTTPException(status_code=500, detail="Failed to load call detail")


@router.patch("/calls/{call_id}/note")
async def add_call_note(call_id: str, body: CallNoteBody, _=Depends(require_admin)):
    """Attach an admin note to a call record (appended to existing notes)."""
    if not body.note.strip():
        raise HTTPException(status_code=400, detail="Note cannot be empty.")
    try:
        db = get_supabase()
        db.table("calls").update({
            "admin_note": body.note,
        }).eq("id", call_id).execute()
        logger.info(f"Admin note added to call {call_id}")
        return {"status": "noted", "call_id": call_id}
    except Exception as e:
        logger.error(f"add_call_note failed for {call_id}: {e}")
        raise HTTPException(status_code=500, detail="Failed to save note")


# ───────────── ERROR LOGS ─────────────

@router.get("/error-logs")
async def get_error_logs(
    resolved: Optional[bool] = Query(default=None),
    service: Optional[str] = Query(default=None),
    brokerage_id: Optional[str] = Query(default=None),
    limit: int = Query(default=50, le=200),
    offset: int = Query(default=0),
    _=Depends(require_admin),
):
    """
    System error log browser. Filter by resolved status, service, or brokerage.
    Newest first. Unresolved errors are shown by default.
    """
    errors = list_errors(
        resolved=resolved,
        service=service,
        brokerage_id=brokerage_id,
        limit=limit,
        offset=offset,
    )
    return {"errors": errors, "count": len(errors), "offset": offset, "limit": limit}


@router.patch("/error-logs/{error_id}/resolve")
async def resolve_error_log(error_id: str, body: ErrorResolveBody, _=Depends(require_admin)):
    """Mark an error as resolved, optionally adding an admin note."""
    ok = resolve_error(error_id, admin_note=body.admin_note)
    if not ok:
        raise HTTPException(status_code=500, detail="Failed to resolve error.")
    return {"status": "resolved", "error_id": error_id}
