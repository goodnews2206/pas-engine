"""
Bounded query helpers over pas_events.

Thin Supabase wrappers used by the (future) intelligence routes. Every
function:
  - Caps `limit` at MAX_LIMIT (100).
  - Accepts an optional brokerage_id filter — required for portal callers
    (the route layer is responsible for passing it).
  - Never raises. Returns [] on any failure.
  - Performs no LLM/provider calls and reads no secrets.
"""

import logging
from typing import Optional

from app.db.supabase_client import get_supabase

logger = logging.getLogger("pas.intelligence.queries")

MAX_LIMIT = 100
DEFAULT_LIMIT = 25


def _bounded_limit(limit) -> int:
    if not isinstance(limit, int) or limit <= 0:
        return DEFAULT_LIMIT
    return min(limit, MAX_LIMIT)


def _bounded_offset(offset) -> int:
    if not isinstance(offset, int) or offset < 0:
        return 0
    return offset


def recent_events(
    brokerage_id: Optional[str] = None,
    event_type: Optional[str] = None,
    severity: Optional[str] = None,
    since_iso: Optional[str] = None,
    limit: int = DEFAULT_LIMIT,
    offset: int = 0,
) -> list:
    """Most recent pas_events rows, newest first. Filters AND-combined."""
    try:
        db = get_supabase()
        capped = _bounded_limit(limit)
        off = _bounded_offset(offset)
        q = (
            db.table("pas_events")
            .select("*")
            .order("created_at", desc=True)
            .range(off, off + capped - 1)
        )
        if brokerage_id:
            q = q.eq("brokerage_id", brokerage_id)
        if event_type:
            q = q.eq("event_type", event_type)
        if severity:
            q = q.eq("severity", severity)
        if since_iso:
            q = q.gte("created_at", since_iso)
        return q.execute().data or []
    except Exception as e:
        logger.warning(f"recent_events failed: {e}")
        return []


def events_for_call(
    call_id: str,
    brokerage_id: Optional[str] = None,
    limit: int = MAX_LIMIT,
) -> list:
    """All pas_events for a single call, oldest first (timeline order)."""
    if not call_id:
        return []
    try:
        db = get_supabase()
        capped = _bounded_limit(limit)
        q = (
            db.table("pas_events")
            .select("*")
            .eq("call_id", call_id)
            .order("created_at", desc=False)
            .limit(capped)
        )
        if brokerage_id:
            q = q.eq("brokerage_id", brokerage_id)
        return q.execute().data or []
    except Exception as e:
        logger.warning(f"events_for_call failed for {call_id}: {e}")
        return []


def fetch_call_and_lead_context(
    call_ids,
    lead_ids,
    brokerage_id: Optional[str] = None,
) -> tuple:
    """
    Batch-fetch call rows and lead rows for leakage classification context.

    Returns ``(calls_by_id, leads_by_id)``. Both are dicts keyed by primary
    key id. On any DB failure the failing half degrades to ``{}`` — never
    raises. Bounded to MAX_LIMIT (100) ids per side.

    The `brokerage_id` filter, when supplied, is applied to BOTH queries so
    a portal caller cannot pull foreign-brokerage rows even if a stray
    call_id sneaks in.

    Selected columns are the minimum needed by detect_leakage:
      calls : id, outcome, call_status, source, brokerage_id
      leads : id, status, intent, budget, timeline, outcome, brokerage_id
    """
    calls_by_id: dict = {}
    leads_by_id: dict = {}

    cap_call_ids = [cid for cid in (call_ids or []) if cid][:MAX_LIMIT]
    cap_lead_ids = [lid for lid in (lead_ids or []) if lid][:MAX_LIMIT]

    if cap_call_ids:
        try:
            db = get_supabase()
            q = (
                db.table("calls")
                .select("id, outcome, call_status, source, brokerage_id")
                .in_("id", cap_call_ids)
            )
            if brokerage_id:
                q = q.eq("brokerage_id", brokerage_id)
            for row in q.execute().data or []:
                rid = (row or {}).get("id")
                if rid:
                    calls_by_id[rid] = row
        except Exception as e:
            logger.warning(f"fetch_call_and_lead_context (calls) failed: {e}")

    if cap_lead_ids:
        try:
            db = get_supabase()
            q = (
                db.table("leads")
                .select("id, status, intent, budget, timeline, outcome, brokerage_id")
                .in_("id", cap_lead_ids)
            )
            if brokerage_id:
                q = q.eq("brokerage_id", brokerage_id)
            for row in q.execute().data or []:
                rid = (row or {}).get("id")
                if rid:
                    leads_by_id[rid] = row
        except Exception as e:
            logger.warning(f"fetch_call_and_lead_context (leads) failed: {e}")

    return calls_by_id, leads_by_id


def callback_events(
    brokerage_id: Optional[str] = None,
    since_iso: Optional[str] = None,
    limit: int = 50,
    offset: int = 0,
) -> list:
    """
    callback.requested + call.ended_with_callback events, newest first.
    Powers the callback queue panel.
    """
    try:
        db = get_supabase()
        capped = _bounded_limit(limit)
        off = _bounded_offset(offset)
        q = (
            db.table("pas_events")
            .select("*")
            .in_("event_type", ["callback.requested", "call.ended_with_callback"])
            .order("created_at", desc=True)
            .range(off, off + capped - 1)
        )
        if brokerage_id:
            q = q.eq("brokerage_id", brokerage_id)
        if since_iso:
            q = q.gte("created_at", since_iso)
        return q.execute().data or []
    except Exception as e:
        logger.warning(f"callback_events failed: {e}")
        return []
