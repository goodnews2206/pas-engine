"""
Workflow query helpers.

Thin wrappers that resolve the call/lead context the runtime needs. The
event timeline itself is fetched via the existing intelligence.queries
module — no duplicate Supabase logic — so the brokerage filter behaviour
matches everywhere else in the codebase.

Never raises; degrades to {} / [] on failure.
"""

import logging
from typing import Optional

from app.db.supabase_client import get_supabase
from app.services.intelligence.queries import events_for_call

logger = logging.getLogger("pas.workflows.queries")


def fetch_workflow_events(call_id: str, brokerage_id: Optional[str] = None) -> list:
    """All pas_events for a call in chronological order."""
    return events_for_call(call_id, brokerage_id=brokerage_id, limit=100)


def fetch_call_summary(call_id: str, brokerage_id: Optional[str] = None) -> dict:
    """
    Resolve the small set of `calls` columns the runtime layer needs to
    populate workflow_run identity (lead_id + brokerage_id) and to enforce
    portal ownership at the route layer.

    Returns {} on failure or when the row is not found.
    """
    if not call_id:
        return {}
    try:
        db = get_supabase()
        q = (
            db.table("calls")
            .select("id, brokerage_id, lead_id, outcome, call_status, source")
            .eq("id", call_id)
            .limit(1)
        )
        if brokerage_id:
            q = q.eq("brokerage_id", brokerage_id)
        rows = q.execute().data or []
        return rows[0] if rows else {}
    except Exception as e:
        logger.warning(f"fetch_call_summary failed for {call_id}: {e}")
        return {}
