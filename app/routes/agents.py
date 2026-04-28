"""
Agent Management API — nested under /admin/brokerages/{brokerage_id}/agents

All routes require X-Admin-Key header.

Routes:
  POST   /admin/brokerages/{id}/agents              → add an agent
  GET    /admin/brokerages/{id}/agents              → list agents (+ leaderboard)
  GET    /admin/brokerages/{id}/agents/{agent_id}   → agent detail
  PATCH  /admin/brokerages/{id}/agents/{agent_id}   → update profile/availability
  DELETE /admin/brokerages/{id}/agents/{agent_id}   → remove agent
  POST   /admin/brokerages/{id}/agents/{agent_id}/close → record a closed deal
  GET    /admin/brokerages/{id}/agents/leaderboard  → ranked by close rate
"""

import logging
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from app.db.agent_store import (
    create_agent,
    delete_agent,
    get_agent,
    get_agent_leaderboard,
    list_agents,
    record_close,
    set_agent_status,
    update_agent,
)
from app.routes.admin import require_admin

router = APIRouter()
logger = logging.getLogger("pas.agents_api")


# ───────────── MODELS ─────────────

class AgentCreate(BaseModel):
    name: str
    phone: str = ""
    email: str = ""
    slack_member_id: str = ""          # Slack User ID for @mentions
    specialties: List[str] = []        # ["buying", "selling", "luxury", "commercial"]
    areas: List[str] = []              # ["Miami Beach", "Brickell", "Downtown"]
    languages: List[str] = ["en"]


class AgentUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    slack_member_id: Optional[str] = None
    status: Optional[str] = None      # available | busy | offline
    specialties: Optional[List[str]] = None
    areas: Optional[List[str]] = None
    languages: Optional[List[str]] = None


# ───────────── ROUTES ─────────────

@router.post("/brokerages/{brokerage_id}/agents", status_code=201)
async def add_agent(brokerage_id: str, body: AgentCreate, _=Depends(require_admin)):
    """Add a new agent to a brokerage. PAS will route bookings to them."""
    try:
        agent = create_agent(brokerage_id, body.model_dump())
        return {"agent": agent}
    except Exception as e:
        logger.error(f"Failed to create agent for brokerage {brokerage_id}: {e}")
        raise HTTPException(status_code=500, detail="Failed to create agent — check server logs.")


@router.get("/brokerages/{brokerage_id}/agents")
async def list_brokerage_agents(
    brokerage_id: str,
    status: Optional[str] = None,
    _=Depends(require_admin),
):
    """
    List all agents for a brokerage.
    Filter by status: ?status=available | busy | offline
    """
    agents = list_agents(brokerage_id, status=status)
    available = [a for a in agents if a.get("status") == "available"]
    return {
        "agents": agents,
        "count": len(agents),
        "available_count": len(available),
    }


@router.get("/brokerages/{brokerage_id}/agents/leaderboard")
async def agent_leaderboard(brokerage_id: str, _=Depends(require_admin)):
    """Agents ranked by close rate — use this to understand top performers."""
    return {"leaderboard": get_agent_leaderboard(brokerage_id)}


@router.get("/brokerages/{brokerage_id}/agents/{agent_id}")
async def get_agent_detail(brokerage_id: str, agent_id: str, _=Depends(require_admin)):
    agent = get_agent(agent_id)
    if not agent or agent.get("brokerage_id") != brokerage_id:
        raise HTTPException(status_code=404, detail="Agent not found")
    return {"agent": agent}


@router.patch("/brokerages/{brokerage_id}/agents/{agent_id}")
async def update_agent_profile(
    brokerage_id: str,
    agent_id: str,
    body: AgentUpdate,
    _=Depends(require_admin),
):
    """
    Update any agent field — including status.
    Brokerages can set status=offline when an agent is on leave,
    status=available when they're back, status=busy during viewings.
    """
    # Ownership check — prevent cross-brokerage mutation
    agent = get_agent(agent_id)
    if not agent or agent.get("brokerage_id") != brokerage_id:
        raise HTTPException(status_code=404, detail="Agent not found")

    changes = {k: v for k, v in body.model_dump().items() if v is not None}
    if not changes:
        raise HTTPException(status_code=400, detail="No fields to update.")

    if "status" in changes and changes["status"] not in ("available", "busy", "offline"):
        raise HTTPException(status_code=400, detail="status must be available | busy | offline")

    ok = update_agent(agent_id, changes)
    if not ok:
        raise HTTPException(status_code=500, detail="Update failed.")
    return {"status": "updated", "fields": list(changes.keys())}


@router.delete("/brokerages/{brokerage_id}/agents/{agent_id}")
async def remove_agent(brokerage_id: str, agent_id: str, _=Depends(require_admin)):
    """Remove an agent. Their historical stats remain on past call records."""
    # Ownership check — prevent cross-brokerage deletion
    agent = get_agent(agent_id)
    if not agent or agent.get("brokerage_id") != brokerage_id:
        raise HTTPException(status_code=404, detail="Agent not found")

    ok = delete_agent(agent_id)
    if not ok:
        raise HTTPException(status_code=500, detail="Delete failed.")
    return {"status": "removed", "agent_id": agent_id}


@router.post("/brokerages/{brokerage_id}/agents/{agent_id}/close")
async def record_agent_close(brokerage_id: str, agent_id: str, _=Depends(require_admin)):
    """
    Record a successful deal close for an agent.
    This updates their total_closed and close_rate (computed column in DB).
    Call this from your CRM or manually when a deal is confirmed.
    """
    agent = get_agent(agent_id)
    if not agent or agent.get("brokerage_id") != brokerage_id:
        raise HTTPException(status_code=404, detail="Agent not found")
    record_close(agent_id)
    return {
        "status": "recorded",
        "agent": agent.get("name"),
        "note": "close_rate will update automatically based on total_closed / total_assigned",
    }


@router.patch("/brokerages/{brokerage_id}/agents/{agent_id}/status")
async def set_status(
    brokerage_id: str,
    agent_id: str,
    status: str,
    _=Depends(require_admin),
):
    """Quick endpoint to flip an agent's availability status."""
    if status not in ("available", "busy", "offline"):
        raise HTTPException(status_code=400, detail="status must be available | busy | offline")
    ok = set_agent_status(agent_id, status)
    if not ok:
        raise HTTPException(status_code=500, detail="Status update failed.")
    return {"status": "updated", "agent_id": agent_id, "new_status": status}
