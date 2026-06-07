"""
Agent Store — per-brokerage human agent records.

Responsibilities:
  - CRUD for agents
  - Availability management (available / busy / offline)
  - Best-fit routing: matches lead intent + area + language to the right agent
  - Performance tracking: total_assigned, total_closed → close_rate (computed by DB)
"""

import logging
from datetime import datetime, timezone
from typing import Optional

from app.db.supabase_client import get_supabase

logger = logging.getLogger("pas.agents")


# ───────────── CRUD ─────────────

def create_agent(brokerage_id: str, data: dict) -> dict:
    now = datetime.now(timezone.utc).isoformat()
    payload = {
        "brokerage_id": brokerage_id,
        "name": data["name"],
        "phone": data.get("phone", ""),
        "email": data.get("email", ""),
        "slack_member_id": data.get("slack_member_id", ""),
        "status": "available",
        "specialties": data.get("specialties", []),
        "areas": data.get("areas", []),
        "languages": data.get("languages", ["en"]),
        "total_assigned": 0,
        "total_closed": 0,
        "created_at": now,
        "updated_at": now,
    }
    db = get_supabase()
    result = db.table("agents").insert(payload).execute()
    logger.info(f"Agent created | brokerage={brokerage_id} | name={data['name']}")
    return result.data[0] if result.data else payload


def get_agent(agent_id: str, brokerage_id: Optional[str] = None) -> Optional[dict]:
    """Fetch one agent by id.

    PAS211E: pass ``brokerage_id`` from any tenant-facing caller — the lookup is
    then scoped to that tenant and returns ``None`` for an agent owned by a
    different brokerage (defence-in-depth against cross-tenant IDOR). Admin /
    internal callers may omit it for a global lookup.
    """
    try:
        db = get_supabase()
        q = db.table("agents").select("*").eq("id", agent_id)
        if brokerage_id:
            q = q.eq("brokerage_id", brokerage_id)
        result = q.limit(1).execute()
        return result.data[0] if result.data else None
    except Exception as e:
        logger.error(f"get_agent failed: {e}")
        return None


def list_agents(brokerage_id: str, status: str = None) -> list:
    try:
        db = get_supabase()
        q = db.table("agents").select("*").eq("brokerage_id", brokerage_id)
        if status:
            q = q.eq("status", status)
        result = q.order("close_rate", desc=True).execute()
        return result.data or []
    except Exception as e:
        logger.error(f"list_agents failed: {e}")
        return []


def update_agent(agent_id: str, updates: dict, brokerage_id: Optional[str] = None) -> bool:
    """Update one agent.

    PAS211E: when ``brokerage_id`` is supplied (tenant-facing callers) the write
    carries an additional ``brokerage_id`` predicate, so an attempt to mutate an
    agent owned by another tenant matches zero rows and changes nothing.
    """
    try:
        updates["updated_at"] = datetime.now(timezone.utc).isoformat()
        db = get_supabase()
        q = db.table("agents").update(updates).eq("id", agent_id)
        if brokerage_id:
            q = q.eq("brokerage_id", brokerage_id)
        q.execute()
        return True
    except Exception as e:
        logger.error(f"update_agent failed: {e}")
        return False


def delete_agent(agent_id: str, brokerage_id: Optional[str] = None) -> bool:
    """Delete one agent.

    PAS211E: tenant-scoped when ``brokerage_id`` is supplied — a cross-tenant
    delete matches zero rows (defence-in-depth).
    """
    try:
        db = get_supabase()
        q = db.table("agents").delete().eq("id", agent_id)
        if brokerage_id:
            q = q.eq("brokerage_id", brokerage_id)
        q.execute()
        return True
    except Exception as e:
        logger.error(f"delete_agent failed: {e}")
        return False


# ───────────── AVAILABILITY ─────────────

def set_agent_status(agent_id: str, status: str, brokerage_id: Optional[str] = None) -> bool:
    """status: available | busy | offline (PAS211E: tenant-scoped when given)."""
    return update_agent(agent_id, {"status": status}, brokerage_id=brokerage_id)


# ───────────── BEST-FIT ROUTING ─────────────

def get_best_available_agent(
    brokerage_id: str,
    intent: str = "",
    area: str = "",
    language: str = "en",
) -> Optional[dict]:
    """
    Scores all available agents and returns the best fit for this lead.

    Scoring:
      +3  specialty matches lead intent (buying/selling/renting)
      +2  area matches lead's area
      +1  language match
      tie-break: highest close_rate wins
    """
    agents = list_agents(brokerage_id, status="available")
    if not agents:
        return None

    def score(agent: dict) -> float:
        s = 0.0
        specialties = [x.lower() for x in (agent.get("specialties") or [])]
        areas = [x.lower() for x in (agent.get("areas") or [])]
        languages = [x.lower() for x in (agent.get("languages") or ["en"])]

        if intent and intent.lower() in specialties:
            s += 3
        if area and any(area.lower() in a for a in areas):
            s += 2
        if language.lower() in languages:
            s += 1

        # Tie-break by close rate
        s += (agent.get("close_rate") or 0) * 0.01
        return s

    ranked = sorted(agents, key=score, reverse=True)
    best = ranked[0]
    logger.info(
        f"Best-fit agent | brokerage={brokerage_id} | agent={best['name']} "
        f"| intent={intent} | available={len(agents)}"
    )
    return best


# ───────────── PERFORMANCE TRACKING ─────────────

def record_assignment(agent_id: str):
    """Call when an appointment is assigned to this agent."""
    try:
        db = get_supabase()
        current = db.table("agents").select("total_assigned").eq("id", agent_id).limit(1).execute()
        if current.data:
            count = (current.data[0].get("total_assigned") or 0) + 1
            db.table("agents").update({
                "total_assigned": count,
                "status": "busy",
                "updated_at": datetime.now(timezone.utc).isoformat(),
            }).eq("id", agent_id).execute()
    except Exception as e:
        logger.error(f"record_assignment failed: {e}")


def record_close(agent_id: str):
    """Call when an agent successfully closes a deal. Admin-triggered."""
    try:
        db = get_supabase()
        current = db.table("agents").select("total_closed").eq("id", agent_id).limit(1).execute()
        if current.data:
            count = (current.data[0].get("total_closed") or 0) + 1
            db.table("agents").update({
                "total_closed": count,
                "updated_at": datetime.now(timezone.utc).isoformat(),
            }).eq("id", agent_id).execute()
    except Exception as e:
        logger.error(f"record_close failed: {e}")


def get_agent_leaderboard(brokerage_id: str) -> list:
    """Returns agents ranked by close rate for the brokerage dashboard."""
    try:
        db = get_supabase()
        result = (
            db.table("agents")
            .select("id, name, status, specialties, total_assigned, total_closed, close_rate")
            .eq("brokerage_id", brokerage_id)
            .order("close_rate", desc=True)
            .execute()
        )
        return result.data or []
    except Exception as e:
        logger.error(f"get_agent_leaderboard failed: {e}")
        return []
