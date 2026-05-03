"""
Admin Intelligence + Event Visibility (PAS129/PAS130).

Read-only views over pas_events and the deterministic intelligence
algorithms. All routes require X-Admin-Key (existing require_admin
dependency from app.routes.admin).

Mounted under /admin in main.py.

Routes:
  GET /admin/events/recent              → newest pas_events rows
  GET /admin/events/callbacks           → callback queue (admin view)
  GET /admin/events/calls/{call_id}     → full event timeline for a call
  GET /admin/intelligence/summary       → aggregated KPIs + leakage breakdown
"""

import logging
from collections import Counter
from datetime import datetime, timedelta, timezone
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query

from app.routes.admin import require_admin
from app.services.intelligence.leakage import detect_leakage
from app.services.intelligence.queries import (
    callback_events,
    events_for_call,
    fetch_call_and_lead_context,
    recent_events,
)
from app.services.intelligence.scoring import SCORING_VERSION

router = APIRouter()
logger = logging.getLogger("pas.events")

_SUMMARY_DEFAULT_DAYS = 7
_SUMMARY_MAX_EVENTS = 100
_CALLBACK_EVENT_TYPES = ("callback.requested", "call.ended_with_callback")


def _default_since_iso(days: int = _SUMMARY_DEFAULT_DAYS) -> str:
    return (datetime.now(timezone.utc) - timedelta(days=days)).isoformat()


@router.get("/events/recent")
async def admin_events_recent(
    brokerage_id: Optional[str] = Query(default=None),
    event_type: Optional[str] = Query(default=None),
    severity: Optional[str] = Query(default=None),
    since_iso: Optional[str] = Query(default=None),
    limit: int = Query(default=25, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    _=Depends(require_admin),
):
    """Most recent pas_events rows, newest first. Admin sees full payloads."""
    events = recent_events(
        brokerage_id=brokerage_id,
        event_type=event_type,
        severity=severity,
        since_iso=since_iso,
        limit=limit,
        offset=offset,
    )
    return {
        "events": events,
        "count": len(events),
        "limit": limit,
        "offset": offset,
    }


@router.get("/events/callbacks")
async def admin_events_callbacks(
    brokerage_id: Optional[str] = Query(default=None),
    since_iso: Optional[str] = Query(default=None),
    limit: int = Query(default=50, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    _=Depends(require_admin),
):
    """callback.requested + call.ended_with_callback events, newest first."""
    events = callback_events(
        brokerage_id=brokerage_id,
        since_iso=since_iso,
        limit=limit,
        offset=offset,
    )
    return {
        "events": events,
        "count": len(events),
        "limit": limit,
        "offset": offset,
    }


@router.get("/events/calls/{call_id}")
async def admin_events_for_call(
    call_id: str,
    brokerage_id: Optional[str] = Query(default=None),
    limit: int = Query(default=100, ge=1, le=100),
    _=Depends(require_admin),
):
    """All pas_events for a single call, oldest first (timeline order)."""
    if not call_id:
        raise HTTPException(status_code=400, detail="call_id required")
    events = events_for_call(call_id, brokerage_id=brokerage_id, limit=limit)
    return {"call_id": call_id, "events": events, "count": len(events)}


@router.get("/intelligence/summary")
async def admin_intelligence_summary(
    brokerage_id: Optional[str] = Query(default=None),
    since_iso: Optional[str] = Query(default=None),
    _=Depends(require_admin),
):
    """
    Aggregate KPIs over the recent event window.

    Returns event counts by category/severity/type, callback volume, and a
    leakage-category breakdown computed by grouping events by call_id and
    running detect_leakage on each group. Window defaults to last 7 days.
    Bounded to the most recent _SUMMARY_MAX_EVENTS events.
    """
    if not since_iso:
        since_iso = _default_since_iso()

    events = recent_events(
        brokerage_id=brokerage_id,
        since_iso=since_iso,
        limit=_SUMMARY_MAX_EVENTS,
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
        if (e or {}).get("event_type") in _CALLBACK_EVENT_TYPES:
            callback_count += 1
        cid = (e or {}).get("call_id")
        if cid:
            by_call.setdefault(cid, []).append(e)

    # Enrich detect_leakage with real call + lead context. Without these
    # rows, response_leakage / qualification_leakage / DNC paths cannot
    # classify correctly. Fetches degrade to {} on failure (never raise).
    distinct_lead_ids = {(e or {}).get("lead_id") for e in events if (e or {}).get("lead_id")}
    calls_by_id, leads_by_id = fetch_call_and_lead_context(
        list(by_call.keys()),
        list(distinct_lead_ids),
        brokerage_id=brokerage_id,
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
        "brokerage_id": brokerage_id,
        "events_total": len(events),
        "events_by_category": dict(by_category),
        "events_by_severity": dict(by_severity),
        "events_by_type": dict(by_event_type),
        "callback_events_count": callback_count,
        "leakage_breakdown": dict(leakage_counts),
        "calls_analyzed": len(by_call),
        "version": SCORING_VERSION,
    }
