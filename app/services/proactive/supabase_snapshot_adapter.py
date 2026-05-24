"""
PAS206 — Read-only Supabase snapshot adapter for PAS205 observer.

Connects the PAS205 read-only proactive observer to existing PAS
Supabase tables. The adapter is, by construction:

  * READ-ONLY. The only Supabase query verbs it issues are
    `select`, `eq`, `limit`, `order`, and `execute`. There is no
    `insert`, `update`, `delete`, `upsert`, or `rpc` anywhere in
    this module. The readiness gate asserts this textually.
  * Safe under missing optional tables. If a table is absent or a
    select raises, the source is marked unavailable and the rest
    of the snapshot loads normally.
  * Pure normalisation. The adapter never persists, never mutates,
    never schedules, never sends.

It returns a `SupabaseSnapshotResult` envelope:

  snapshot              — PAS205 ObservedSnapshot ready for observe()
  source_status         — per-source "ok" | "empty" | "unavailable"
  unavailable_sources   — tuple of sources that did not load
  row_counts            — per-source row count actually normalised
  loaded_at             — ISO 8601 UTC timestamp adapter ran at
  read_only             — always True (hard invariant)
  brokerage_id          — scope filter applied to the read

The adapter does not import the live `supabase` package. Callers
inject a client object (the production singleton or a stub). This
keeps the adapter unit-testable without a live DB and the
readiness gate textual assertions tight.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Iterable, List, Mapping, Optional, Sequence, Tuple

from app.services.proactive.observer_models import (
    ObservedAgent,
    ObservedBooking,
    ObservedCall,
    ObservedCallback,
    ObservedLead,
    ObservedSnapshot,
)


# ──────────────────────────────────────────────────────────────────
# Allowed read sources. Anything not in this tuple will be ignored
# by the adapter even if a caller asks for it. This is the closed
# read vocabulary — symmetric to the closed signal vocabulary on
# the observer side.
# ──────────────────────────────────────────────────────────────────

SOURCE_LEADS     = "leads"
SOURCE_CALLS     = "calls"
SOURCE_BOOKINGS  = "bookings"
SOURCE_AGENTS    = "agents"
SOURCE_CALLBACKS = "callbacks"

ALLOWED_SOURCES: Tuple[str, ...] = (
    SOURCE_LEADS,
    SOURCE_CALLS,
    SOURCE_BOOKINGS,
    SOURCE_AGENTS,
    SOURCE_CALLBACKS,
)

OPTIONAL_SOURCES: Tuple[str, ...] = (
    SOURCE_CALLBACKS,
)

STATUS_OK          = "ok"
STATUS_EMPTY       = "empty"
STATUS_UNAVAILABLE = "unavailable"


# ──────────────────────────────────────────────────────────────────
# Result envelope.
# ──────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class SupabaseSnapshotResult:
    snapshot:            ObservedSnapshot
    source_status:       Mapping[str, str]
    unavailable_sources: Tuple[str, ...]
    row_counts:          Mapping[str, int]
    loaded_at:           str
    brokerage_id:        str
    read_only:           bool = True


# ──────────────────────────────────────────────────────────────────
# Helpers.
# ──────────────────────────────────────────────────────────────────

def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _coerce_str(value: Any) -> Optional[str]:
    if value is None:
        return None
    if isinstance(value, str):
        return value or None
    try:
        return str(value)
    except Exception:
        return None


def _coerce_int(value: Any, default: int = 0) -> int:
    if value is None:
        return default
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _coerce_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in ("true", "t", "1", "yes", "y")
    if isinstance(value, (int, float)):
        return bool(value)
    return False


def _normalise_call_outcome(raw: Any) -> Optional[str]:
    """Map a DB `outcome` value into the PAS205 observed-call vocabulary.

    PAS205 cares about three high-level outcomes:
      answered | no_answer | failed
    Plus an explicit None for "unknown yet".
    """
    value = _coerce_str(raw)
    if value is None:
        return None
    v = value.strip().lower()
    if v in ("answered", "completed", "booked", "ok", "success"):
        return "answered"
    if v in ("no_answer", "no-answer", "voicemail", "missed", "unanswered"):
        return "no_answer"
    if v in ("failed", "error", "busy", "rejected", "cancelled", "no_show"):
        return "failed"
    if v == "pending":
        return None
    return v


def _normalise_booking_state(raw: Any) -> str:
    """Map a DB booking status to PAS205 confirmation_state.

    PAS205 confirmation_state ∈ {"pending", "confirmed", "failed"}.
    """
    value = _coerce_str(raw)
    if value is None:
        return "pending"
    v = value.strip().lower()
    if v in ("scheduled", "rescheduled", "pending"):
        return "pending"
    if v in ("completed", "confirmed"):
        return "confirmed"
    if v in ("failed", "no_show", "cancelled"):
        return "failed"
    return "pending"


def _normalise_callback_state(raw: Any) -> str:
    """Map a DB callback status to PAS205 callback state."""
    value = _coerce_str(raw)
    if value is None:
        return "pending"
    v = value.strip().lower()
    if v in ("completed", "done"):
        return "completed"
    if v in ("cancelled", "canceled"):
        return "cancelled"
    return "pending"


# ──────────────────────────────────────────────────────────────────
# Per-source read helpers.
#
# Each helper:
#   - issues a select-only query
#   - swallows any exception (missing table, transient error, etc)
#     into ("unavailable", []) so the snapshot still loads
#   - returns a tuple: (status, rows)
# ──────────────────────────────────────────────────────────────────

def _safe_select(
    client:        Any,
    table_name:    str,
    brokerage_id:  str,
    columns:       str = "*",
    limit:         Optional[int] = None,
) -> Tuple[str, List[Mapping[str, Any]]]:
    try:
        query = client.table(table_name).select(columns).eq("brokerage_id", brokerage_id)
        if limit is not None:
            query = query.limit(limit)
        result = query.execute()
    except Exception:
        return STATUS_UNAVAILABLE, []

    rows = getattr(result, "data", None)
    if rows is None and isinstance(result, dict):
        rows = result.get("data")
    if not rows:
        return STATUS_EMPTY, []
    return STATUS_OK, list(rows)


def _normalise_leads(rows: Iterable[Mapping[str, Any]]) -> Tuple[ObservedLead, ...]:
    out: List[ObservedLead] = []
    for row in rows:
        ref = _coerce_str(row.get("id")) or _coerce_str(row.get("phone_number"))
        created = _coerce_str(row.get("created_at"))
        if not ref or not created:
            continue
        out.append(
            ObservedLead(
                lead_ref           = ref,
                created_at         = created,
                first_response_at  = _coerce_str(row.get("first_response_at")),
                last_activity_at   = _coerce_str(row.get("last_activity_at"))
                                     or _coerce_str(row.get("updated_at"))
                                     or _coerce_str(row.get("last_call_at")),
                assigned_agent_ref = _coerce_str(row.get("assigned_agent_id"))
                                     or _coerce_str(row.get("agent_id")),
                source             = _coerce_str(row.get("source")),
                value_tier         = _coerce_str(row.get("value_tier")),
                after_hours        = _coerce_bool(row.get("after_hours")),
                needs_human_review = _coerce_bool(row.get("needs_human_review")),
            )
        )
    return tuple(out)


def _normalise_calls(rows: Iterable[Mapping[str, Any]]) -> Tuple[ObservedCall, ...]:
    out: List[ObservedCall] = []
    for row in rows:
        ref      = _coerce_str(row.get("id"))
        lead_ref = _coerce_str(row.get("lead_id")) or _coerce_str(row.get("phone_number"))
        started  = _coerce_str(row.get("start_time")) or _coerce_str(row.get("started_at"))
        if not ref or not lead_ref or not started:
            continue
        out.append(
            ObservedCall(
                call_ref      = ref,
                lead_ref      = lead_ref,
                started_at    = started,
                ended_at      = _coerce_str(row.get("end_time")) or _coerce_str(row.get("ended_at")),
                outcome       = _normalise_call_outcome(row.get("outcome")),
                attempt_index = _coerce_int(row.get("attempt_index"), default=1),
            )
        )
    return tuple(out)


def _normalise_bookings(rows: Iterable[Mapping[str, Any]]) -> Tuple[ObservedBooking, ...]:
    out: List[ObservedBooking] = []
    for row in rows:
        ref      = _coerce_str(row.get("id"))
        lead_ref = (
            _coerce_str(row.get("lead_id"))
            or _coerce_str(row.get("call_sid"))
            or _coerce_str(row.get("lead_phone"))
        )
        proposed = _coerce_str(row.get("slot_time")) or _coerce_str(row.get("proposed_at"))
        if not ref or not lead_ref or not proposed:
            continue
        out.append(
            ObservedBooking(
                booking_ref        = ref,
                lead_ref           = lead_ref,
                proposed_at        = proposed,
                confirmation_state = _normalise_booking_state(row.get("status")),
                last_attempt_at    = _coerce_str(row.get("updated_at"))
                                     or _coerce_str(row.get("last_attempt_at")),
            )
        )
    return tuple(out)


def _normalise_agents(rows: Iterable[Mapping[str, Any]]) -> Tuple[ObservedAgent, ...]:
    out: List[ObservedAgent] = []
    for row in rows:
        ref = _coerce_str(row.get("id"))
        if not ref:
            continue
        status_val = (_coerce_str(row.get("status")) or "").strip().lower()
        available = status_val in ("available", "online", "ready")
        out.append(
            ObservedAgent(
                agent_ref    = ref,
                available    = available,
                last_seen_at = _coerce_str(row.get("last_seen_at"))
                               or _coerce_str(row.get("updated_at")),
            )
        )
    return tuple(out)


def _normalise_callbacks(rows: Iterable[Mapping[str, Any]]) -> Tuple[ObservedCallback, ...]:
    out: List[ObservedCallback] = []
    for row in rows:
        ref       = _coerce_str(row.get("id"))
        lead_ref  = _coerce_str(row.get("lead_id")) or _coerce_str(row.get("phone_number"))
        requested = _coerce_str(row.get("requested_at")) or _coerce_str(row.get("created_at"))
        scheduled = _coerce_str(row.get("scheduled_at"))
        if not ref or not lead_ref or not requested or not scheduled:
            continue
        out.append(
            ObservedCallback(
                callback_ref = ref,
                lead_ref     = lead_ref,
                requested_at = requested,
                scheduled_at = scheduled,
                completed_at = _coerce_str(row.get("completed_at")),
                state        = _normalise_callback_state(row.get("status")),
            )
        )
    return tuple(out)


# ──────────────────────────────────────────────────────────────────
# Public entry point.
# ──────────────────────────────────────────────────────────────────

def load_snapshot(
    client:        Any,
    brokerage_id:  str,
    *,
    row_limit:     Optional[int] = 500,
    loaded_at:     Optional[str] = None,
) -> SupabaseSnapshotResult:
    """Pull a normalised PAS205 snapshot from Supabase, read-only.

    Parameters
    ----------
    client : Any
        A Supabase client object exposing `.table(name)`. Production
        callers pass the singleton from `app.db.supabase_client`.
        Tests inject a stub.
    brokerage_id : str
        Scope filter for every source. Required, never None.
    row_limit : int, optional
        Per-source cap on rows. Read-only does not need pagination
        for the proactive digest — a recent slice is sufficient.
    loaded_at : str, optional
        Override the load timestamp for deterministic tests.

    Returns
    -------
    SupabaseSnapshotResult
        Envelope with snapshot, per-source status, row counts,
        and the read_only=True invariant.
    """
    if not isinstance(brokerage_id, str) or not brokerage_id.strip():
        raise ValueError("brokerage_id is required and must be a non-empty string")

    timestamp = loaded_at or _now_iso()

    # Per-source reads. Each call is wrapped in _safe_select so a
    # missing table degrades to ("unavailable", []) rather than
    # raising.
    leads_status,     lead_rows     = _safe_select(client, SOURCE_LEADS,     brokerage_id, limit=row_limit)
    calls_status,     call_rows     = _safe_select(client, SOURCE_CALLS,     brokerage_id, limit=row_limit)
    bookings_status,  booking_rows  = _safe_select(client, SOURCE_BOOKINGS,  brokerage_id, limit=row_limit)
    agents_status,    agent_rows    = _safe_select(client, SOURCE_AGENTS,    brokerage_id, limit=row_limit)
    callbacks_status, callback_rows = _safe_select(client, SOURCE_CALLBACKS, brokerage_id, limit=row_limit)

    leads     = _normalise_leads(lead_rows)
    calls     = _normalise_calls(call_rows)
    bookings  = _normalise_bookings(booking_rows)
    agents    = _normalise_agents(agent_rows)
    callbacks = _normalise_callbacks(callback_rows)

    snapshot = ObservedSnapshot(
        observed_at = timestamp,
        leads       = leads,
        calls       = calls,
        bookings    = bookings,
        callbacks   = callbacks,
        agents      = agents,
    )

    source_status = {
        SOURCE_LEADS:     leads_status,
        SOURCE_CALLS:     calls_status,
        SOURCE_BOOKINGS:  bookings_status,
        SOURCE_AGENTS:    agents_status,
        SOURCE_CALLBACKS: callbacks_status,
    }

    unavailable: List[str] = [
        name for name, status in source_status.items()
        if status == STATUS_UNAVAILABLE
    ]

    row_counts = {
        SOURCE_LEADS:     len(leads),
        SOURCE_CALLS:     len(calls),
        SOURCE_BOOKINGS:  len(bookings),
        SOURCE_AGENTS:    len(agents),
        SOURCE_CALLBACKS: len(callbacks),
    }

    return SupabaseSnapshotResult(
        snapshot            = snapshot,
        source_status       = source_status,
        unavailable_sources = tuple(unavailable),
        row_counts          = row_counts,
        loaded_at           = timestamp,
        brokerage_id        = brokerage_id,
        read_only           = True,
    )


__all__ = (
    "SOURCE_LEADS",
    "SOURCE_CALLS",
    "SOURCE_BOOKINGS",
    "SOURCE_AGENTS",
    "SOURCE_CALLBACKS",
    "ALLOWED_SOURCES",
    "OPTIONAL_SOURCES",
    "STATUS_OK",
    "STATUS_EMPTY",
    "STATUS_UNAVAILABLE",
    "SupabaseSnapshotResult",
    "load_snapshot",
)
