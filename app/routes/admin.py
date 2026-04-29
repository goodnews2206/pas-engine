"""
Admin API — manage brokerage accounts, view stats, trigger self-training.

Auth: all routes require the X-Admin-Key header matching ADMIN_API_KEY in .env.

Routes:
  POST   /admin/brokerages              → create a new brokerage account
  GET    /admin/brokerages              → list all accounts
  GET    /admin/brokerages/{id}         → account detail + live stats
  PATCH  /admin/brokerages/{id}         → update config (name, agent, Slack, etc.)
  DELETE /admin/brokerages/{id}         → deactivate (soft delete)
  POST   /admin/brokerages/{id}/train   → trigger self-training now
  POST   /admin/brokerages/{id}/rotate-key → generate a new API key
  GET    /admin/brokerages/{id}/leads   → paginated lead memory
  GET    /admin/brokerages/{id}/calls   → recent call history
"""

import logging
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
)
from app.db.supabase_client import get_supabase
from app.services.training.self_trainer import run_training

router = APIRouter()
logger = logging.getLogger("pas.admin")


# ───────────── AUTH ─────────────

def require_admin(x_admin_key: str = Header(...)):
    settings = get_settings()
    if not settings.ADMIN_API_KEY or x_admin_key != settings.ADMIN_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid admin key")
    return True


# ───────────── MODELS ─────────────

class BrokerageCreate(BaseModel):
    id: str                          # "remax-miami" — URL-safe slug
    name: str                        # "RE/MAX Miami"
    agent_name: str = "Alex"
    twilio_phone: str = ""
    agent_phone: str = ""
    slack_webhook_url: str = ""
    slack_team_id: str = ""
    slack_signing_secret: str = ""


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
    changes = body.model_dump(exclude_unset=True)
    if not changes:
        raise HTTPException(status_code=400, detail="No fields to update.")
    ok = update_brokerage(brokerage_id, changes)
    if not ok:
        raise HTTPException(status_code=500, detail="Update failed — check Supabase connection.")
    return {"status": "updated", "fields": list(changes.keys())}


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
