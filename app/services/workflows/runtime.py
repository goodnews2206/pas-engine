"""
Workflow runtime — derive a live workflow_run + steps for a single call.

V1 is fully derived: there is no workflow_runs / workflow_steps table yet.
The runtime fetches pas_events via the existing intelligence query layer,
folds them through the deterministic mapper, and adapts the result for
the requesting audience. The output shape matches what a future
DB-persisted workflow row would look like, so adding persistence later is
a swap of `get_or_build_workflow_for_call` internals — the route contract
does not change.

Never raises. Returns a populated workflow envelope even when the call
has no events yet (steps all `pending`).
"""

import logging
from typing import Optional

from app.services.workflows.mapper import map_events_to_workflow
from app.services.workflows.queries import fetch_call_summary, fetch_workflow_events
from app.services.workflows.sanitize import sanitize_workflow_for_audience

logger = logging.getLogger("pas.workflows.runtime")

WORKFLOW_VERSION = "v1"


def _empty_envelope(call_id: str, brokerage_id: Optional[str], lead_id: Optional[str]) -> dict:
    return {
        "workflow_id":     f"derived:{call_id}" if call_id else None,
        "call_id":         call_id,
        "lead_id":         lead_id,
        "brokerage_id":    brokerage_id,
        "workflow_type":   "lead_response",
        "workflow_status": "pending",
        "current_step":    None,
        "leak_detected_at": None,
        "steps":           [],
        "events_count":    0,
        "system_signals":  {},
        "version":         WORKFLOW_VERSION,
    }


def get_or_build_workflow_for_call(
    call_id: str,
    brokerage_id: Optional[str] = None,
    audience: str = "admin",
) -> dict:
    """
    Return the workflow envelope for a single call_id.

    Args:
      call_id:       canonical call_id / call_sid
      brokerage_id:  required for portal callers (route enforces). When
                     supplied, both the events query and the call summary
                     query restrict to this brokerage as defence-in-depth.
      audience:      'admin' or 'portal' — drives translation only.

    Returns a dict with the shape documented in PART 2 of the PAS132 spec.
    Never raises. On total DB failure, returns an empty envelope rather
    than 500-ing.
    """
    if not call_id:
        return _empty_envelope(call_id="", brokerage_id=brokerage_id, lead_id=None)

    call_row = fetch_call_summary(call_id, brokerage_id=brokerage_id)
    events = fetch_workflow_events(call_id, brokerage_id=brokerage_id)

    # Lead id resolution: prefer the calls.lead_id column; fall back to
    # the first non-empty lead_id we observe in the event stream.
    lead_id = (call_row or {}).get("lead_id")
    if not lead_id:
        for ev in events:
            lid = (ev or {}).get("lead_id")
            if lid:
                lead_id = lid
                break

    resolved_brokerage = brokerage_id or (call_row or {}).get("brokerage_id")

    folded = map_events_to_workflow(events)

    envelope = {
        "workflow_id":     f"derived:{call_id}",
        "call_id":         call_id,
        "lead_id":         lead_id,
        "brokerage_id":    resolved_brokerage,
        "workflow_type":   "lead_response",
        "workflow_status": folded["workflow_status"],
        "current_step":    folded["current_step"],
        "leak_detected_at": folded["leak_detected_at"],
        "steps":           folded["steps"],
        "events_count":    folded["events_count"],
        "system_signals":  folded["system_signals"],
        "version":         WORKFLOW_VERSION,
    }

    return sanitize_workflow_for_audience(envelope, audience=audience)
