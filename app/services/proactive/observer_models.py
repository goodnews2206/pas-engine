"""
PAS205 — Proactive observer domain model.

Bounded, frozen dataclasses for the read-only proactive observer.
These are pure value objects: they carry no DB session, no network
client, no live-action method. They describe what the observer
*saw* and what it *recommends as next step* — never what it did.

Safety doctrine:

  * No DB imports. No network imports. No LLM imports.
  * No mutation methods. Every dataclass is frozen.
  * Closed vocabulary for `SignalType` and `Severity`.
  * Every emitted `AttentionSignal` carries
    `live_behavior_changed=False` — PAS205 cannot, by construction,
    flip live behavior.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping, Optional, Tuple


# ──────────────────────────────────────────────────────────────────
# Closed signal vocabulary.
# Add a new signal type ONLY by appending here and wiring a
# deterministic rule in observer.py. Order is stable and tested.
# ──────────────────────────────────────────────────────────────────

SIGNAL_CALLBACK_OVERDUE              = "callback_overdue"
SIGNAL_LEAD_UNASSIGNED               = "lead_unassigned"
SIGNAL_STALE_LEAD                    = "stale_lead"
SIGNAL_MISSED_FIRST_RESPONSE         = "missed_first_response"
SIGNAL_FAILED_BOOKING_CONFIRMATION   = "failed_booking_confirmation"
SIGNAL_NO_AGENT_AVAILABLE            = "no_agent_available"
SIGNAL_REPEATED_FAILED_CALLS         = "repeated_failed_calls"
SIGNAL_AFTER_HOURS_LEAD_PENDING      = "after_hours_lead_pending"
SIGNAL_HIGH_VALUE_LEAD_WAITING       = "high_value_lead_waiting"
SIGNAL_NEEDS_HUMAN_REVIEW            = "needs_human_review"


SIGNAL_TYPES: Tuple[str, ...] = (
    SIGNAL_CALLBACK_OVERDUE,
    SIGNAL_LEAD_UNASSIGNED,
    SIGNAL_STALE_LEAD,
    SIGNAL_MISSED_FIRST_RESPONSE,
    SIGNAL_FAILED_BOOKING_CONFIRMATION,
    SIGNAL_NO_AGENT_AVAILABLE,
    SIGNAL_REPEATED_FAILED_CALLS,
    SIGNAL_AFTER_HOURS_LEAD_PENDING,
    SIGNAL_HIGH_VALUE_LEAD_WAITING,
    SIGNAL_NEEDS_HUMAN_REVIEW,
)


SEVERITY_LOW    = "low"
SEVERITY_MEDIUM = "medium"
SEVERITY_HIGH   = "high"

SEVERITIES: Tuple[str, ...] = (SEVERITY_LOW, SEVERITY_MEDIUM, SEVERITY_HIGH)


SUBJECT_LEAD     = "lead"
SUBJECT_CALL     = "call"
SUBJECT_BOOKING  = "booking"
SUBJECT_CALLBACK = "callback"
SUBJECT_PIPELINE = "pipeline"

SUBJECT_TYPES: Tuple[str, ...] = (
    SUBJECT_LEAD,
    SUBJECT_CALL,
    SUBJECT_BOOKING,
    SUBJECT_CALLBACK,
    SUBJECT_PIPELINE,
)


# ──────────────────────────────────────────────────────────────────
# Observed snapshot value objects.
#
# Inputs to the observer are pure dicts or these frozen dataclasses.
# The observer never persists or mutates them.
# ──────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class ObservedLead:
    lead_ref:           str
    created_at:         str
    first_response_at:  Optional[str] = None
    last_activity_at:   Optional[str] = None
    assigned_agent_ref: Optional[str] = None
    source:             Optional[str] = None
    value_tier:         Optional[str] = None       # "low" | "standard" | "high"
    after_hours:        bool          = False
    needs_human_review: bool          = False


@dataclass(frozen=True)
class ObservedCall:
    call_ref:          str
    lead_ref:          str
    started_at:        str
    ended_at:          Optional[str] = None
    outcome:           Optional[str] = None        # "answered" | "no_answer" | "failed" | ...
    attempt_index:     int           = 1


@dataclass(frozen=True)
class ObservedBooking:
    booking_ref:       str
    lead_ref:          str
    proposed_at:       str
    confirmation_state: str                        # "pending" | "confirmed" | "failed"
    last_attempt_at:   Optional[str] = None


@dataclass(frozen=True)
class ObservedCallback:
    callback_ref:      str
    lead_ref:          str
    requested_at:      str
    scheduled_at:      str
    completed_at:      Optional[str] = None
    state:             str = "pending"             # "pending" | "completed" | "cancelled"


@dataclass(frozen=True)
class ObservedAgent:
    agent_ref:         str
    available:         bool
    last_seen_at:      Optional[str] = None


@dataclass(frozen=True)
class ObservedSnapshot:
    observed_at:       str
    leads:             Tuple[ObservedLead, ...]       = ()
    calls:             Tuple[ObservedCall, ...]       = ()
    bookings:          Tuple[ObservedBooking, ...]    = ()
    callbacks:         Tuple[ObservedCallback, ...]   = ()
    agents:            Tuple[ObservedAgent, ...]      = ()


# ──────────────────────────────────────────────────────────────────
# Outputs of the observer.
# ──────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class AttentionSignal:
    signal_id:              str
    signal_type:            str
    severity:               str
    subject_type:           str
    subject_ref:            str
    reason:                 str
    recommended_next_step:  str
    evidence:               Mapping[str, object] = field(default_factory=dict)
    created_at:             str = ""
    # PAS205 hard invariant — the observer CANNOT flip live
    # behavior. This field is set by the observer to False and is
    # asserted by tests and the readiness gate.
    live_behavior_changed:  bool = False


@dataclass(frozen=True)
class NeedsAttentionDigest:
    digest_id:              str
    generated_at:           str
    observed_at:            str
    phase:                  str = "PAS205"
    allowed_environment:    str = "SIMULATION_ONLY"
    live_behavior_changed:  bool = False
    signals:                Tuple[AttentionSignal, ...] = ()
    counts_by_severity:     Mapping[str, int] = field(default_factory=dict)
    counts_by_signal_type:  Mapping[str, int] = field(default_factory=dict)


__all__ = (
    "SIGNAL_CALLBACK_OVERDUE",
    "SIGNAL_LEAD_UNASSIGNED",
    "SIGNAL_STALE_LEAD",
    "SIGNAL_MISSED_FIRST_RESPONSE",
    "SIGNAL_FAILED_BOOKING_CONFIRMATION",
    "SIGNAL_NO_AGENT_AVAILABLE",
    "SIGNAL_REPEATED_FAILED_CALLS",
    "SIGNAL_AFTER_HOURS_LEAD_PENDING",
    "SIGNAL_HIGH_VALUE_LEAD_WAITING",
    "SIGNAL_NEEDS_HUMAN_REVIEW",
    "SIGNAL_TYPES",
    "SEVERITY_LOW",
    "SEVERITY_MEDIUM",
    "SEVERITY_HIGH",
    "SEVERITIES",
    "SUBJECT_LEAD",
    "SUBJECT_CALL",
    "SUBJECT_BOOKING",
    "SUBJECT_CALLBACK",
    "SUBJECT_PIPELINE",
    "SUBJECT_TYPES",
    "ObservedLead",
    "ObservedCall",
    "ObservedBooking",
    "ObservedCallback",
    "ObservedAgent",
    "ObservedSnapshot",
    "AttentionSignal",
    "NeedsAttentionDigest",
)
