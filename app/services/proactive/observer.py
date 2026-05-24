"""
PAS205 — Read-only proactive observer.

Inspects an in-memory ObservedSnapshot of brokerage pipeline state
and emits a NeedsAttentionDigest of closed-vocabulary
AttentionSignals. The observer is:

  * Pure function. Same snapshot + same `now` produce the same
    digest forever.
  * Deterministic. No randomness. No timezone surprises (UTC only).
  * Read-only. No DB session, no network client, no Twilio, no
    Slack outbound. No mutation methods anywhere.
  * Closed-vocabulary. Every signal_type is in `SIGNAL_TYPES`.
  * Explainable. Every signal carries a human `reason` and a
    structured `evidence` mapping.

The observer is the *signal* layer of the proactive stack. Later
PAS layers will turn signals into recommendations (PAS208) and
operator-approved actions (PAS209). PAS205 only watches.

Hard contract (asserted by tests and the readiness gate):

  * No imports of twilio, slack_sdk, openai, anthropic, dotenv,
    supabase, app.engine, app.services.notifications,
    app.services.outbound, or the live state machine.
  * No identifiers named apply_*, deploy_*, send_real_*,
    auto_apply, auto_promote, post_to_slack, route_lead_live,
    etc.
  * Every emitted signal has `live_behavior_changed=False`.
"""

from __future__ import annotations

import hashlib
from datetime import datetime, timezone
from typing import Counter as _Counter
from typing import Dict, List, Mapping, Optional, Tuple

from app.services.proactive.observer_models import (
    SEVERITY_HIGH,
    SEVERITY_LOW,
    SEVERITY_MEDIUM,
    SIGNAL_AFTER_HOURS_LEAD_PENDING,
    SIGNAL_CALLBACK_OVERDUE,
    SIGNAL_FAILED_BOOKING_CONFIRMATION,
    SIGNAL_HIGH_VALUE_LEAD_WAITING,
    SIGNAL_LEAD_UNASSIGNED,
    SIGNAL_MISSED_FIRST_RESPONSE,
    SIGNAL_NEEDS_HUMAN_REVIEW,
    SIGNAL_NO_AGENT_AVAILABLE,
    SIGNAL_REPEATED_FAILED_CALLS,
    SIGNAL_STALE_LEAD,
    SIGNAL_TYPES,
    SUBJECT_BOOKING,
    SUBJECT_CALL,
    SUBJECT_CALLBACK,
    SUBJECT_LEAD,
    SUBJECT_PIPELINE,
    AttentionSignal,
    NeedsAttentionDigest,
    ObservedBooking,
    ObservedCall,
    ObservedCallback,
    ObservedLead,
    ObservedSnapshot,
)


# ──────────────────────────────────────────────────────────────────
# Thresholds.
#
# Every threshold is a constant. They are calibrated for the
# demo data and the deterministic test fixtures; production layers
# (PAS206+) will be able to override via an explicit policy object,
# but PAS205 itself takes no config from the environment.
# ──────────────────────────────────────────────────────────────────

FIRST_RESPONSE_TARGET_SECONDS:  int = 5 * 60           # 5 minutes
STALE_LEAD_AGE_SECONDS:         int = 48 * 60 * 60     # 48 hours of inactivity
CALLBACK_GRACE_SECONDS:         int = 10 * 60          # 10 minutes past scheduled_at
REPEATED_FAILED_CALL_THRESHOLD: int = 3                # 3+ failed attempts
AFTER_HOURS_PENDING_SECONDS:    int = 15 * 60          # 15 minutes pending after-hours


# ──────────────────────────────────────────────────────────────────
# Time helpers (UTC only, ISO 8601).
# ──────────────────────────────────────────────────────────────────

def _parse_iso(value: Optional[str]) -> Optional[datetime]:
    if not value:
        return None
    text = value.strip()
    if not text:
        return None
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(text)
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def _format_iso(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _seconds_between(later: datetime, earlier: datetime) -> int:
    return int((later - earlier).total_seconds())


# ──────────────────────────────────────────────────────────────────
# Deterministic signal-id derivation.
#
# We hash the closed tuple (signal_type, subject_ref, observed_at)
# so the same snapshot at the same instant produces the same
# signal_id every time. No randomness. No counters. No clocks.
# ──────────────────────────────────────────────────────────────────

def _signal_id(signal_type: str, subject_ref: str, observed_at: str) -> str:
    seed = f"{signal_type}|{subject_ref}|{observed_at}".encode("utf-8")
    digest = hashlib.sha256(seed).hexdigest()[:16]
    return f"pas205-sig-{digest}"


def _digest_id(observed_at: str, signal_count: int) -> str:
    seed = f"pas205-digest|{observed_at}|{signal_count}".encode("utf-8")
    digest = hashlib.sha256(seed).hexdigest()[:16]
    return f"pas205-dgst-{digest}"


def _make_signal(
    signal_type:   str,
    severity:      str,
    subject_type:  str,
    subject_ref:   str,
    reason:        str,
    next_step:     str,
    evidence:      Mapping[str, object],
    observed_at:   str,
) -> AttentionSignal:
    return AttentionSignal(
        signal_id              = _signal_id(signal_type, subject_ref, observed_at),
        signal_type            = signal_type,
        severity               = severity,
        subject_type           = subject_type,
        subject_ref            = subject_ref,
        reason                 = reason,
        recommended_next_step  = next_step,
        evidence               = dict(evidence),
        created_at             = observed_at,
        live_behavior_changed  = False,
    )


# ──────────────────────────────────────────────────────────────────
# Rule implementations.
#
# Each rule reads from the snapshot and returns 0..N signals. Rules
# never mutate anything, never raise on missing optional fields,
# and never recommend an action that PAS205 itself could perform.
# Every recommended_next_step is phrased as observer-to-human
# advice ("ask an agent to call back", not "call back").
# ──────────────────────────────────────────────────────────────────

def _rule_callback_overdue(
    snap: ObservedSnapshot,
    now:  datetime,
    observed_at: str,
) -> List[AttentionSignal]:
    out: List[AttentionSignal] = []
    for cb in snap.callbacks:
        if cb.state != "pending":
            continue
        scheduled = _parse_iso(cb.scheduled_at)
        if scheduled is None:
            continue
        late_seconds = _seconds_between(now, scheduled)
        if late_seconds <= CALLBACK_GRACE_SECONDS:
            continue
        if late_seconds > 60 * 60:
            severity = SEVERITY_HIGH
        elif late_seconds > 30 * 60:
            severity = SEVERITY_MEDIUM
        else:
            severity = SEVERITY_LOW
        out.append(_make_signal(
            signal_type   = SIGNAL_CALLBACK_OVERDUE,
            severity      = severity,
            subject_type  = SUBJECT_CALLBACK,
            subject_ref   = cb.callback_ref,
            reason        = (
                f"a callback for lead {cb.lead_ref} was scheduled for "
                f"{cb.scheduled_at} and has not been completed"
            ),
            next_step     = (
                "ask an agent to return this callback, or reschedule it "
                "and confirm with the lead"
            ),
            evidence      = {
                "lead_ref":     cb.lead_ref,
                "scheduled_at": cb.scheduled_at,
                "late_seconds": late_seconds,
            },
            observed_at   = observed_at,
        ))
    return out


def _rule_lead_unassigned(
    snap: ObservedSnapshot,
    now:  datetime,
    observed_at: str,
) -> List[AttentionSignal]:
    out: List[AttentionSignal] = []
    for lead in snap.leads:
        if lead.assigned_agent_ref:
            continue
        created = _parse_iso(lead.created_at)
        # An unassigned brand-new lead (< 60 seconds) is normal in
        # a brokerage workflow; only flag if it has been sitting.
        if created is None or _seconds_between(now, created) < 60:
            continue
        wait_seconds = _seconds_between(now, created)
        severity = (
            SEVERITY_HIGH
            if wait_seconds > FIRST_RESPONSE_TARGET_SECONDS
            else SEVERITY_MEDIUM
        )
        out.append(_make_signal(
            signal_type   = SIGNAL_LEAD_UNASSIGNED,
            severity      = severity,
            subject_type  = SUBJECT_LEAD,
            subject_ref   = lead.lead_ref,
            reason        = (
                f"lead {lead.lead_ref} has no assigned agent "
                f"{wait_seconds // 60} minutes after coming in"
            ),
            next_step     = "assign an agent to this lead and start first contact",
            evidence      = {
                "created_at":   lead.created_at,
                "wait_seconds": wait_seconds,
                "source":       lead.source or "unknown",
            },
            observed_at   = observed_at,
        ))
    return out


def _rule_stale_lead(
    snap: ObservedSnapshot,
    now:  datetime,
    observed_at: str,
) -> List[AttentionSignal]:
    out: List[AttentionSignal] = []
    for lead in snap.leads:
        last = _parse_iso(lead.last_activity_at) or _parse_iso(lead.created_at)
        if last is None:
            continue
        idle = _seconds_between(now, last)
        if idle < STALE_LEAD_AGE_SECONDS:
            continue
        severity = SEVERITY_LOW if idle < STALE_LEAD_AGE_SECONDS * 2 else SEVERITY_MEDIUM
        out.append(_make_signal(
            signal_type   = SIGNAL_STALE_LEAD,
            severity      = severity,
            subject_type  = SUBJECT_LEAD,
            subject_ref   = lead.lead_ref,
            reason        = (
                f"lead {lead.lead_ref} has had no activity for "
                f"{idle // 3600} hours"
            ),
            next_step     = (
                "ask an agent to send a soft check-in to this lead; "
                "do not push for a sale"
            ),
            evidence      = {
                "last_activity_at": lead.last_activity_at or lead.created_at,
                "idle_seconds":     idle,
            },
            observed_at   = observed_at,
        ))
    return out


def _rule_missed_first_response(
    snap: ObservedSnapshot,
    now:  datetime,
    observed_at: str,
) -> List[AttentionSignal]:
    out: List[AttentionSignal] = []
    for lead in snap.leads:
        if lead.first_response_at:
            continue
        created = _parse_iso(lead.created_at)
        if created is None:
            continue
        elapsed = _seconds_between(now, created)
        if elapsed <= FIRST_RESPONSE_TARGET_SECONDS:
            continue
        severity = SEVERITY_HIGH if elapsed > FIRST_RESPONSE_TARGET_SECONDS * 3 else SEVERITY_MEDIUM
        out.append(_make_signal(
            signal_type   = SIGNAL_MISSED_FIRST_RESPONSE,
            severity      = severity,
            subject_type  = SUBJECT_LEAD,
            subject_ref   = lead.lead_ref,
            reason        = (
                f"lead {lead.lead_ref} came in "
                f"{elapsed // 60} minutes ago and still has no first response"
            ),
            next_step     = (
                "ask the on-shift agent to make first contact now; "
                "speed-to-lead matters most in the first 5 minutes"
            ),
            evidence      = {
                "created_at":     lead.created_at,
                "elapsed_seconds": elapsed,
                "target_seconds": FIRST_RESPONSE_TARGET_SECONDS,
            },
            observed_at   = observed_at,
        ))
    return out


def _rule_failed_booking_confirmation(
    snap: ObservedSnapshot,
    now:  datetime,
    observed_at: str,
) -> List[AttentionSignal]:
    out: List[AttentionSignal] = []
    for b in snap.bookings:
        if b.confirmation_state != "failed":
            continue
        out.append(_make_signal(
            signal_type   = SIGNAL_FAILED_BOOKING_CONFIRMATION,
            severity      = SEVERITY_HIGH,
            subject_type  = SUBJECT_BOOKING,
            subject_ref   = b.booking_ref,
            reason        = (
                f"booking attempt for lead {b.lead_ref} did not get "
                f"confirmed (proposed for {b.proposed_at})"
            ),
            next_step     = (
                "ask an agent to call the lead and confirm the time "
                "directly, then update the calendar"
            ),
            evidence      = {
                "lead_ref":         b.lead_ref,
                "proposed_at":      b.proposed_at,
                "last_attempt_at":  b.last_attempt_at or "",
            },
            observed_at   = observed_at,
        ))
    return out


def _rule_no_agent_available(
    snap: ObservedSnapshot,
    now:  datetime,
    observed_at: str,
) -> List[AttentionSignal]:
    # Only meaningful if there are open leads waiting AND no agent
    # is available. If neither side is true, stay quiet.
    if not snap.agents:
        return []
    any_available = any(a.available for a in snap.agents)
    if any_available:
        return []
    waiting = [
        lead for lead in snap.leads
        if not lead.first_response_at
    ]
    if not waiting:
        return []
    return [_make_signal(
        signal_type   = SIGNAL_NO_AGENT_AVAILABLE,
        severity      = SEVERITY_HIGH,
        subject_type  = SUBJECT_PIPELINE,
        subject_ref   = "agents",
        reason        = (
            f"no agent is currently available and {len(waiting)} lead(s) "
            f"are still waiting for first contact"
        ),
        next_step     = (
            "bring a backup agent online, or shift coverage so a human "
            "can answer; PAS will keep the leads warm but cannot replace "
            "a human first contact"
        ),
        evidence      = {
            "available_agents":     0,
            "configured_agents":    len(snap.agents),
            "waiting_lead_refs":    [lead.lead_ref for lead in waiting],
        },
        observed_at   = observed_at,
    )]


def _rule_repeated_failed_calls(
    snap: ObservedSnapshot,
    now:  datetime,
    observed_at: str,
) -> List[AttentionSignal]:
    by_lead: Dict[str, int] = {}
    last_attempt: Dict[str, str] = {}
    for call in snap.calls:
        if call.outcome != "failed":
            continue
        by_lead[call.lead_ref] = by_lead.get(call.lead_ref, 0) + 1
        # Keep the latest started_at we have seen, by string compare
        # — ISO 8601 sorts lexicographically.
        if call.started_at > last_attempt.get(call.lead_ref, ""):
            last_attempt[call.lead_ref] = call.started_at
    out: List[AttentionSignal] = []
    for lead_ref, count in sorted(by_lead.items()):
        if count < REPEATED_FAILED_CALL_THRESHOLD:
            continue
        severity = SEVERITY_HIGH if count >= REPEATED_FAILED_CALL_THRESHOLD + 1 else SEVERITY_MEDIUM
        out.append(_make_signal(
            signal_type   = SIGNAL_REPEATED_FAILED_CALLS,
            severity      = severity,
            subject_type  = SUBJECT_LEAD,
            subject_ref   = lead_ref,
            reason        = (
                f"lead {lead_ref} has had {count} failed call attempts; "
                f"the contact channel may be broken"
            ),
            next_step     = (
                "ask an agent to try a different channel (SMS, email) "
                "and confirm the phone number on file is correct"
            ),
            evidence      = {
                "failed_attempts":    count,
                "last_attempt_at":    last_attempt.get(lead_ref, ""),
            },
            observed_at   = observed_at,
        ))
    return out


def _rule_after_hours_lead_pending(
    snap: ObservedSnapshot,
    now:  datetime,
    observed_at: str,
) -> List[AttentionSignal]:
    out: List[AttentionSignal] = []
    for lead in snap.leads:
        if not lead.after_hours:
            continue
        if lead.first_response_at:
            continue
        created = _parse_iso(lead.created_at)
        if created is None:
            continue
        waited = _seconds_between(now, created)
        if waited < AFTER_HOURS_PENDING_SECONDS:
            continue
        out.append(_make_signal(
            signal_type   = SIGNAL_AFTER_HOURS_LEAD_PENDING,
            severity      = SEVERITY_MEDIUM,
            subject_type  = SUBJECT_LEAD,
            subject_ref   = lead.lead_ref,
            reason        = (
                f"lead {lead.lead_ref} arrived after hours and has been "
                f"waiting {waited // 60} minutes without first contact"
            ),
            next_step     = (
                "confirm after-hours coverage is on call; if no human is "
                "available, plan a polite morning-first-touch and note it "
                "for the broker"
            ),
            evidence      = {
                "created_at":   lead.created_at,
                "wait_seconds": waited,
            },
            observed_at   = observed_at,
        ))
    return out


def _rule_high_value_lead_waiting(
    snap: ObservedSnapshot,
    now:  datetime,
    observed_at: str,
) -> List[AttentionSignal]:
    out: List[AttentionSignal] = []
    for lead in snap.leads:
        if (lead.value_tier or "").lower() != "high":
            continue
        if lead.first_response_at:
            continue
        created = _parse_iso(lead.created_at)
        if created is None:
            continue
        waited = _seconds_between(now, created)
        if waited <= 60:
            continue
        # High-value leads get high severity at any meaningful wait.
        severity = (
            SEVERITY_HIGH
            if waited > FIRST_RESPONSE_TARGET_SECONDS // 2
            else SEVERITY_MEDIUM
        )
        out.append(_make_signal(
            signal_type   = SIGNAL_HIGH_VALUE_LEAD_WAITING,
            severity      = severity,
            subject_type  = SUBJECT_LEAD,
            subject_ref   = lead.lead_ref,
            reason        = (
                f"high-value lead {lead.lead_ref} has been waiting "
                f"{waited // 60} minutes for first contact"
            ),
            next_step     = (
                "have a senior agent take this one personally; high-value "
                "leads close faster when a human reaches out within minutes"
            ),
            evidence      = {
                "value_tier":   lead.value_tier,
                "wait_seconds": waited,
                "source":       lead.source or "unknown",
            },
            observed_at   = observed_at,
        ))
    return out


def _rule_needs_human_review(
    snap: ObservedSnapshot,
    now:  datetime,
    observed_at: str,
) -> List[AttentionSignal]:
    out: List[AttentionSignal] = []
    for lead in snap.leads:
        if not lead.needs_human_review:
            continue
        out.append(_make_signal(
            signal_type   = SIGNAL_NEEDS_HUMAN_REVIEW,
            severity      = SEVERITY_HIGH,
            subject_type  = SUBJECT_LEAD,
            subject_ref   = lead.lead_ref,
            reason        = (
                f"lead {lead.lead_ref} was flagged for human review "
                f"(unclear intent, sensitive context, or compliance edge case)"
            ),
            next_step     = (
                "ask a manager or compliance owner to read the transcript "
                "before PAS continues automated handling"
            ),
            evidence      = {
                "source":          lead.source or "unknown",
                "last_activity":   lead.last_activity_at or lead.created_at,
            },
            observed_at   = observed_at,
        ))
    return out


_RULES: Tuple = (
    _rule_callback_overdue,
    _rule_lead_unassigned,
    _rule_stale_lead,
    _rule_missed_first_response,
    _rule_failed_booking_confirmation,
    _rule_no_agent_available,
    _rule_repeated_failed_calls,
    _rule_after_hours_lead_pending,
    _rule_high_value_lead_waiting,
    _rule_needs_human_review,
)


# Deterministic severity ordering: high -> medium -> low.
_SEVERITY_ORDER: Dict[str, int] = {
    SEVERITY_HIGH:   0,
    SEVERITY_MEDIUM: 1,
    SEVERITY_LOW:    2,
}


def _signal_sort_key(s: AttentionSignal) -> Tuple[int, int, str, str]:
    type_rank = SIGNAL_TYPES.index(s.signal_type) if s.signal_type in SIGNAL_TYPES else 999
    return (
        _SEVERITY_ORDER.get(s.severity, 9),
        type_rank,
        s.subject_ref,
        s.signal_id,
    )


# ──────────────────────────────────────────────────────────────────
# Public entry point.
# ──────────────────────────────────────────────────────────────────

def observe(
    snapshot: ObservedSnapshot,
    now:      Optional[datetime] = None,
) -> NeedsAttentionDigest:
    """Run every PAS205 rule against `snapshot` and return a digest.

    `now` defaults to the snapshot's `observed_at` when omitted.
    Passing `now` explicitly is the supported way to get
    deterministic output in tests and fixtures.
    """
    observed_at_dt = _parse_iso(snapshot.observed_at)
    if observed_at_dt is None:
        raise ValueError(
            "ObservedSnapshot.observed_at must be a valid ISO 8601 UTC timestamp"
        )

    if now is None:
        now_dt = observed_at_dt
    else:
        if now.tzinfo is None:
            now_dt = now.replace(tzinfo=timezone.utc)
        else:
            now_dt = now.astimezone(timezone.utc)

    observed_at_str = _format_iso(observed_at_dt)

    signals: List[AttentionSignal] = []
    for rule in _RULES:
        signals.extend(rule(snapshot, now_dt, observed_at_str))

    signals.sort(key=_signal_sort_key)

    by_severity: _Counter[str] = _Counter(s.severity for s in signals)
    by_type:     _Counter[str] = _Counter(s.signal_type for s in signals)

    counts_by_severity = {
        sev: int(by_severity.get(sev, 0))
        for sev in (SEVERITY_HIGH, SEVERITY_MEDIUM, SEVERITY_LOW)
    }
    counts_by_signal_type = {
        st: int(by_type.get(st, 0)) for st in SIGNAL_TYPES
    }

    return NeedsAttentionDigest(
        digest_id              = _digest_id(observed_at_str, len(signals)),
        generated_at           = observed_at_str,
        observed_at            = observed_at_str,
        phase                  = "PAS205",
        allowed_environment    = "SIMULATION_ONLY",
        live_behavior_changed  = False,
        signals                = tuple(signals),
        counts_by_severity     = counts_by_severity,
        counts_by_signal_type  = counts_by_signal_type,
    )


__all__ = (
    "observe",
    "FIRST_RESPONSE_TARGET_SECONDS",
    "STALE_LEAD_AGE_SECONDS",
    "CALLBACK_GRACE_SECONDS",
    "REPEATED_FAILED_CALL_THRESHOLD",
    "AFTER_HOURS_PENDING_SECONDS",
)
