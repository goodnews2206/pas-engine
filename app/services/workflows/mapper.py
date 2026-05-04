"""
Deterministic pas_events → workflow mapping.

`map_events_to_workflow(events)` walks events in chronological order
(oldest first) and folds them into a fixed step skeleton. No LLM, no
provider calls, no I/O — every input produces the same output.

Step skeleton (always present, in this order):

  1. lead_received         detect    Lead Received
  2. pas_calling           detect    PAS Calling
  3. intent_captured       decide    Intent Captured
  4. budget_captured       decide    Budget Captured
  5. timeline_captured     decide    Timeline Captured
  6. booking_attempted     act       Booking Attempted
  7. booking_confirmed     outcome   Appointment Confirmed
  8. callback_requested    outcome   Callback Requested
  9. followup_scheduled    outcome   Follow-up Scheduled
 10. completed             outcome   Conversation Completed

booking_confirmed and callback_requested are mutually-exclusive terminal
branches; whichever the conversation produced becomes `completed`, the
other becomes `skipped`. followup_scheduled is only reached on a callback.

Status precedence inside a single step:
  failed > warning > completed > running > skipped > pending
A later event cannot weaken a step's status (e.g. a later `running` won't
overwrite a prior `completed`).
"""

from typing import Iterable, Optional

# ── Step skeleton ────────────────────────────────────────────────────────────

# (key, label, category)
_STEP_SKELETON = [
    ("lead_received",       "Lead Received",          "detect"),
    ("pas_calling",         "PAS Calling",            "detect"),
    ("intent_captured",     "Intent Captured",        "decide"),
    ("budget_captured",     "Budget Captured",        "decide"),
    ("timeline_captured",   "Timeline Captured",      "decide"),
    ("booking_attempted",   "Booking Attempted",      "act"),
    ("booking_confirmed",   "Appointment Confirmed",  "outcome"),
    ("callback_requested",  "Callback Requested",     "outcome"),
    ("followup_scheduled",  "Follow-up Scheduled",    "outcome"),
    ("completed",           "Conversation Completed", "outcome"),
]

# Status ranking — higher wins when an update arrives. Skipped is below
# pending so a real signal can flip skipped → completed if events arrive
# out of order; pending is the floor.
_STATUS_RANK = {
    "pending":   0,
    "skipped":   1,
    "running":   2,
    "completed": 3,
    "warning":   4,
    "failed":    5,
}

_TERMINAL_STATUSES = {"completed", "warning", "failed", "skipped"}

# Static safe details — short, business-readable, no provider names.
# Per-step the runtime layer may overlay an audience-specific translation.
_DEFAULT_DETAIL = {
    "lead_received":      "Lead entered PAS workflow",
    "pas_calling":        "PAS started the qualification conversation",
    "intent_captured":    "Lead intent identified",
    "budget_captured":    "Lead budget recorded",
    "timeline_captured":  "Lead timeline recorded",
    "booking_attempted":  "PAS attempted to schedule a viewing",
    "booking_confirmed":  "Viewing confirmed on the calendar",
    "callback_requested": "Lead asked PAS to follow up later",
    "followup_scheduled": "Callback window saved for the team",
    "completed":          "PAS finished the conversation",
}


def _new_skeleton() -> list:
    return [
        {
            "key": key,
            "label": label,
            "category": cat,
            "status": "pending",
            "event_type": None,
            "timestamp": None,
            "detail": _DEFAULT_DETAIL.get(key, ""),
            "safe_metadata": {},
            "order_index": idx + 1,
        }
        for idx, (key, label, cat) in enumerate(_STEP_SKELETON)
    ]


def _step_index(steps: list, key: str) -> int:
    for i, s in enumerate(steps):
        if s["key"] == key:
            return i
    return -1


def _bump(step: dict, status: str, event_type: Optional[str], ts: Optional[str], detail: Optional[str] = None, meta: Optional[dict] = None) -> None:
    """Apply a status update with rank-based precedence. Status only
    monotonically rises within a step. Always records the event_type and
    timestamp of the latest signal that touched the step."""
    if status not in _STATUS_RANK:
        return
    cur_rank = _STATUS_RANK.get(step.get("status") or "pending", 0)
    new_rank = _STATUS_RANK[status]
    if new_rank > cur_rank:
        step["status"] = status
    if event_type:
        step["event_type"] = event_type
    if ts:
        step["timestamp"] = ts
    if detail:
        step["detail"] = detail
    if meta:
        # Merge shallowly. Caller is responsible for keeping payload-derived
        # values short and free of secrets — sanitisation is the route layer's
        # job, not the mapper's.
        clean = {k: v for k, v in meta.items() if isinstance(k, str)}
        step["safe_metadata"].update(clean)


def _safe_meta(payload: Optional[dict], allowed_keys: Iterable[str]) -> dict:
    """Return only the requested keys from payload, with string values
    truncated to 120 chars and dict/list values dropped. Never includes
    forbidden secret-style keys regardless of the allow list."""
    if not isinstance(payload, dict):
        return {}
    forbidden_substrings = ("secret", "password", "token", "api_key", "auth")
    out: dict = {}
    for k in allowed_keys:
        if not isinstance(k, str):
            continue
        kl = k.lower()
        if any(s in kl for s in forbidden_substrings):
            continue
        v = payload.get(k)
        if v is None:
            continue
        if isinstance(v, str):
            out[k] = v[:120]
        elif isinstance(v, (int, float, bool)):
            out[k] = v
        # dicts/lists deliberately dropped — nodes display short scalars only.
    return out


def map_events_to_workflow(events: Optional[list]) -> dict:
    """
    Fold an ordered (oldest first) list of pas_events rows into a
    workflow object. Returns a dict with shape:

        {
          "steps": [...],
          "workflow_status": "pending|running|warning|failed|completed",
          "current_step": "<step key or None>",
          "leak_detected_at": "<step key or None>",
          "events_count": int,
          "system_signals": {...},  # provider.failed counts etc.
        }

    Never raises. Unknown event_types are ignored.
    """
    steps = _new_skeleton()
    events = events or []

    # System signals — admin-only consumers can surface these. Portal
    # callers should ignore. Counts only, no provider names embedded
    # in the user-visible label.
    system_signals = {
        "provider_failed_count": 0,
        "system_error_count": 0,
        "objection_count": 0,
    }
    leak_detected_at: Optional[str] = None
    has_terminal = False
    has_failed = False
    call_failed = False
    booking_branch_taken: Optional[str] = None  # 'confirmed' | 'callback'
    booking_attempt_event_seen = False  # actual booking.* event, not just state.transition

    def _idx(key: str) -> int:
        return _step_index(steps, key)

    for ev in events:
        if not isinstance(ev, dict):
            continue
        et = ev.get("event_type") or ""
        ts = ev.get("created_at")
        payload = ev.get("payload") if isinstance(ev.get("payload"), dict) else {}

        if et == "call.started":
            _bump(steps[_idx("lead_received")], "completed", et, ts)
            _bump(steps[_idx("pas_calling")],   "running",   et, ts)

        elif et == "state.transition":
            to_state = (payload.get("to") or ev.get("state") or "").upper()
            from_state = (payload.get("from") or "").upper()
            # Once we leave GREETING, PAS is fully engaged.
            if from_state == "GREETING" or to_state in {"INTENT", "BUDGET", "TIMELINE", "BOOKING", "CLOSING", "DONE"}:
                _bump(steps[_idx("pas_calling")], "completed", et, ts)
            if to_state == "INTENT":
                _bump(steps[_idx("intent_captured")], "running", et, ts)
            elif to_state == "BUDGET":
                _bump(steps[_idx("intent_captured")], "completed", et, ts)
                _bump(steps[_idx("budget_captured")], "running", et, ts)
            elif to_state == "TIMELINE":
                _bump(steps[_idx("budget_captured")], "completed", et, ts)
                _bump(steps[_idx("timeline_captured")], "running", et, ts)
            elif to_state == "BOOKING":
                _bump(steps[_idx("timeline_captured")], "completed", et, ts)
                _bump(steps[_idx("booking_attempted")], "running", et, ts)
            elif to_state in {"CLOSING", "DONE"}:
                # Conversation is wrapping. Don't force completed yet — wait
                # for the explicit terminal call.* event.
                pass

        elif et == "lead.extracted":
            field = (payload.get("field") or "").lower()
            if field == "intent":
                _bump(steps[_idx("intent_captured")], "completed", et, ts,
                      meta=_safe_meta(payload, ("field", "value")))
            elif field == "budget":
                _bump(steps[_idx("budget_captured")], "completed", et, ts,
                      meta=_safe_meta(payload, ("field", "value")))
            elif field == "timeline":
                _bump(steps[_idx("timeline_captured")], "completed", et, ts,
                      meta=_safe_meta(payload, ("field", "value")))
            # email/phone — no dedicated step; ignored (the spec mentions
            # Contact Captured but a brokerage already has phone/email at
            # call.start, so a separate step would mostly be noise).

        elif et == "objection.detected":
            system_signals["objection_count"] += 1
            # An objection is a soft warning attached to whichever decide
            # step is currently running. Don't escalate the step to warning
            # automatically — many objections are handled and the
            # conversation continues normally. Tracked for system_signals.

        elif et == "booking.attempted":
            booking_attempt_event_seen = True
            _bump(steps[_idx("booking_attempted")], "running", et, ts,
                  meta=_safe_meta(payload, ("intent", "budget", "timeline", "has_email")))

        elif et == "booking.confirmed":
            booking_attempt_event_seen = True
            _bump(steps[_idx("booking_attempted")], "completed", et, ts)
            _bump(steps[_idx("booking_confirmed")], "completed", et, ts,
                  meta=_safe_meta(payload, ("slot",)))
            booking_branch_taken = "confirmed"

        elif et == "booking.failed":
            # Booking attempted itself becomes warning, and we record the
            # leak. Don't fail the workflow — a callback/follow-up may still
            # recover the lead.
            booking_attempt_event_seen = True
            _bump(steps[_idx("booking_attempted")], "warning", et, ts,
                  detail="Booking attempt did not confirm — needs retry")
            leak_detected_at = leak_detected_at or "booking_failed"

        elif et == "callback.requested":
            _bump(steps[_idx("callback_requested")], "completed", et, ts,
                  meta=_safe_meta(payload, ("from_state",)))
            booking_branch_taken = "callback"

        elif et == "call.ended_with_callback":
            _bump(steps[_idx("callback_requested")], "completed", et, ts)
            _bump(steps[_idx("followup_scheduled")], "completed", et, ts,
                  meta=_safe_meta(payload, ("preferred_time_normalized", "best_number_confirmed", "callback_confirmed")))
            booking_branch_taken = booking_branch_taken or "callback"
            has_terminal = True

        elif et == "call.ended":
            has_terminal = True
            outcome = (payload.get("outcome") or "").lower()
            if outcome == "booked":
                _bump(steps[_idx("booking_confirmed")], "completed", et, ts)
                booking_branch_taken = booking_branch_taken or "confirmed"
            elif outcome in {"callback_requested", "qualified_callback_requested"}:
                _bump(steps[_idx("callback_requested")], "completed", et, ts)
                _bump(steps[_idx("followup_scheduled")], "completed", et, ts)
                booking_branch_taken = booking_branch_taken or "callback"

        elif et == "call.failed":
            has_terminal = True
            has_failed = True
            call_failed = True

        elif et == "provider.failed":
            system_signals["provider_failed_count"] += 1

        elif et == "system.error":
            system_signals["system_error_count"] += 1

    # ── Resolve branch / terminal state ──────────────────────────────────────

    if has_terminal:
        _bump(steps[_idx("completed")], "failed" if call_failed else "completed",
              "call.failed" if call_failed else "call.ended", None)

        # If we entered the BOOKING state via state.transition but no
        # actual booking.* event ever fired (lead pivoted to a callback
        # before PAS asked the calendar), the booking_attempted step is
        # logically skipped, not completed. Demote it from running so the
        # promote-running pass below doesn't carry it across.
        if not booking_attempt_event_seen:
            ba = steps[_idx("booking_attempted")]
            if ba["status"] == "running":
                ba["status"] = "skipped"

        # Mark the unused booking branch as skipped.
        if booking_branch_taken == "confirmed":
            for k in ("callback_requested", "followup_scheduled"):
                s = steps[_idx(k)]
                if s["status"] == "pending":
                    _bump(s, "skipped", None, None)
        elif booking_branch_taken == "callback":
            s = steps[_idx("booking_confirmed")]
            if s["status"] == "pending":
                _bump(s, "skipped", None, None)
        else:
            # No booking branch resolved — call ended without a clear
            # outcome. Skip the outcome branches that never started.
            for k in ("booking_confirmed", "callback_requested", "followup_scheduled"):
                s = steps[_idx(k)]
                if s["status"] == "pending":
                    _bump(s, "skipped", None, None)

        # Any still-running decide/act steps at terminal time get
        # promoted to completed — the call moved past them.
        for s in steps:
            if s["status"] == "running":
                _bump(s, "completed", s.get("event_type"), s.get("timestamp"))

    # ── Workflow-level status + current_step ────────────────────────────────

    statuses = [s["status"] for s in steps]
    if any(st == "failed" for st in statuses):
        workflow_status = "failed"
    elif any(st == "warning" for st in statuses) or leak_detected_at:
        # If we have a terminal event AND no failed step, a warning still
        # represents a recoverable leak — surface as 'warning' overall.
        if has_terminal:
            workflow_status = "warning"
        else:
            workflow_status = "running"
    elif has_terminal:
        workflow_status = "completed"
    elif any(st in {"running", "completed"} for st in statuses):
        workflow_status = "running"
    else:
        workflow_status = "pending"

    current_step = _resolve_current_step(steps)

    return {
        "steps": steps,
        "workflow_status": workflow_status,
        "current_step": current_step,
        "leak_detected_at": leak_detected_at,
        "events_count": len(events),
        "system_signals": system_signals,
    }


def _resolve_current_step(steps: list) -> Optional[str]:
    """latest running > latest warning > latest completed > first pending."""
    latest_running = None
    latest_warning = None
    latest_completed = None
    first_pending = None
    for s in steps:
        st = s.get("status")
        if st == "running":
            latest_running = s
        elif st == "warning":
            latest_warning = s
        elif st == "completed":
            latest_completed = s
        elif st == "pending" and first_pending is None:
            first_pending = s
    chosen = latest_running or latest_warning or latest_completed or first_pending
    return chosen["key"] if chosen else None
