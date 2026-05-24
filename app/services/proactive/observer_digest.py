"""
PAS205 — Observer digest formatter.

Renders a NeedsAttentionDigest three ways:

  * Machine JSON     — every field a downstream layer needs.
  * Slack-style text — a short, plain-English summary an operator
                       could paste into Slack manually (PAS205
                       itself never sends anything).
  * Broker report    — a longer, no-jargon "staff member talking
                       to a broker" paragraph.

Hard rules:

  * No Slack outbound, no Twilio, no email send, no network.
  * No closed-vocab technical tokens in human output.
  * Deterministic. Same digest -> same string forever.
  * Closed vocabulary for the JSON shape (matches
    observer_models).
"""

from __future__ import annotations

from typing import Dict, List, Mapping, Tuple

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
    AttentionSignal,
    NeedsAttentionDigest,
)


# Tokens that must never appear verbatim in human output. These
# are PAS internal closed-vocab tokens that the digest must
# translate away. A test asserts none of them leak.
FORBIDDEN_OUTPUT_TOKENS: Tuple[str, ...] = (
    "callback_overdue",
    "lead_unassigned",
    "stale_lead",
    "missed_first_response",
    "failed_booking_confirmation",
    "no_agent_available",
    "repeated_failed_calls",
    "after_hours_lead_pending",
    "high_value_lead_waiting",
    "needs_human_review",
    "SIMULATION_ONLY",
    "live_behavior_changed",
    "PAS205",
)


# Per-signal-type human label, singular and plural.
_LABEL_SINGULAR: Mapping[str, str] = {
    SIGNAL_CALLBACK_OVERDUE:            "callback is overdue",
    SIGNAL_LEAD_UNASSIGNED:             "lead has no assigned agent",
    SIGNAL_STALE_LEAD:                  "lead has gone quiet",
    SIGNAL_MISSED_FIRST_RESPONSE:       "lead is still waiting for first contact",
    SIGNAL_FAILED_BOOKING_CONFIRMATION: "booking attempt did not confirm",
    SIGNAL_NO_AGENT_AVAILABLE:          "no agent is currently available",
    SIGNAL_REPEATED_FAILED_CALLS:       "lead has multiple failed call attempts",
    SIGNAL_AFTER_HOURS_LEAD_PENDING:    "after-hours lead is waiting",
    SIGNAL_HIGH_VALUE_LEAD_WAITING:     "high-value lead is waiting",
    SIGNAL_NEEDS_HUMAN_REVIEW:          "lead needs a human to take a look",
}

_LABEL_PLURAL: Mapping[str, str] = {
    SIGNAL_CALLBACK_OVERDUE:            "callbacks are overdue",
    SIGNAL_LEAD_UNASSIGNED:             "leads have no assigned agent",
    SIGNAL_STALE_LEAD:                  "leads have gone quiet",
    SIGNAL_MISSED_FIRST_RESPONSE:       "leads are still waiting for first contact",
    SIGNAL_FAILED_BOOKING_CONFIRMATION: "booking attempts did not confirm",
    SIGNAL_NO_AGENT_AVAILABLE:          "coverage gaps are open right now",
    SIGNAL_REPEATED_FAILED_CALLS:       "leads have multiple failed call attempts",
    SIGNAL_AFTER_HOURS_LEAD_PENDING:    "after-hours leads are waiting",
    SIGNAL_HIGH_VALUE_LEAD_WAITING:     "high-value leads are waiting",
    SIGNAL_NEEDS_HUMAN_REVIEW:          "leads need a human to take a look",
}


def _number_word(n: int) -> str:
    words = {
        1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
    }
    return words.get(n, str(n))


def _label_for(signal_type: str, count: int) -> str:
    table = _LABEL_SINGULAR if count == 1 else _LABEL_PLURAL
    return table.get(signal_type, "items need attention")


def _join_clauses(clauses: List[str]) -> str:
    if not clauses:
        return ""
    if len(clauses) == 1:
        return clauses[0]
    if len(clauses) == 2:
        return f"{clauses[0]}, and {clauses[1]}"
    return ", ".join(clauses[:-1]) + ", and " + clauses[-1]


# ──────────────────────────────────────────────────────────────────
# Machine JSON.
# ──────────────────────────────────────────────────────────────────

def to_machine_json(digest: NeedsAttentionDigest) -> Dict[str, object]:
    return {
        "digest_id":             digest.digest_id,
        "phase":                 digest.phase,
        "allowed_environment":   digest.allowed_environment,
        "live_behavior_changed": bool(digest.live_behavior_changed),
        "generated_at":          digest.generated_at,
        "observed_at":           digest.observed_at,
        "counts_by_severity":    dict(digest.counts_by_severity),
        "counts_by_signal_type": dict(digest.counts_by_signal_type),
        "signals": [
            {
                "signal_id":             s.signal_id,
                "signal_type":           s.signal_type,
                "severity":              s.severity,
                "subject_type":          s.subject_type,
                "subject_ref":           s.subject_ref,
                "reason":                s.reason,
                "recommended_next_step": s.recommended_next_step,
                "evidence":              dict(s.evidence),
                "created_at":            s.created_at,
                "live_behavior_changed": bool(s.live_behavior_changed),
            }
            for s in digest.signals
        ],
    }


# ──────────────────────────────────────────────────────────────────
# Slack-style human summary.
# ──────────────────────────────────────────────────────────────────

def to_slack_summary(digest: NeedsAttentionDigest) -> str:
    total = len(digest.signals)
    if total == 0:
        return (
            "I checked the pipeline and nothing needs attention right now. "
            "Leads are moving, callbacks are on time, and coverage looks fine."
        )

    counts = digest.counts_by_signal_type
    clauses: List[str] = []
    for signal_type, count in counts.items():
        if not count:
            continue
        clauses.append(f"{_number_word(count)} {_label_for(signal_type, count)}")

    header = (
        f"I found {_number_word(total)} thing"
        f"{'s' if total != 1 else ''} that need"
        f"{'' if total != 1 else 's'} attention."
    )
    body = _join_clauses(clauses)
    if body:
        body = body[0].upper() + body[1:] + "."

    high = digest.counts_by_severity.get(SEVERITY_HIGH, 0)
    suffix = ""
    if high:
        word = _number_word(high)
        suffix = (
            f" {word[0].upper()}{word[1:]} of these are time-sensitive — "
            f"worth eyes on them first."
        )

    return f"{header} {body}{suffix}".strip()


# ──────────────────────────────────────────────────────────────────
# Broker-friendly long-form report.
# ──────────────────────────────────────────────────────────────────

def to_broker_report(digest: NeedsAttentionDigest) -> str:
    total = len(digest.signals)
    lines: List[str] = []
    lines.append(f"Here is what I noticed in the pipeline as of {digest.observed_at}.")
    lines.append("")

    if total == 0:
        lines.append(
            "Nothing currently needs attention. Leads have been responded "
            "to on time, callbacks are on schedule, and there is coverage "
            "for inbound activity. I will keep watching."
        )
        return "\n".join(lines)

    high = digest.counts_by_severity.get(SEVERITY_HIGH, 0)
    med  = digest.counts_by_severity.get(SEVERITY_MEDIUM, 0)
    low  = digest.counts_by_severity.get(SEVERITY_LOW, 0)

    summary = (
        f"I found {_number_word(total)} item"
        f"{'s' if total != 1 else ''} worth your attention"
    )
    breakdown_parts: List[str] = []
    if high:
        breakdown_parts.append(f"{_number_word(high)} time-sensitive")
    if med:
        breakdown_parts.append(f"{_number_word(med)} medium")
    if low:
        breakdown_parts.append(f"{_number_word(low)} low-priority")
    if breakdown_parts:
        summary += " — " + ", ".join(breakdown_parts)
    summary += "."
    lines.append(summary)
    lines.append("")

    # Group by signal_type, preserving the digest's deterministic
    # severity-then-type ordering of the signal list.
    seen_types: List[str] = []
    grouped: Dict[str, List[AttentionSignal]] = {}
    for s in digest.signals:
        if s.signal_type not in grouped:
            grouped[s.signal_type] = []
            seen_types.append(s.signal_type)
        grouped[s.signal_type].append(s)

    for stype in seen_types:
        group = grouped[stype]
        label = _label_for(stype, len(group))
        lines.append(f"- {_number_word(len(group))} {label}.")
        for s in group:
            # The reason already starts lowercase by convention;
            # capitalise the first letter when surfacing it.
            reason = s.reason[0].upper() + s.reason[1:] if s.reason else ""
            lines.append(f"    - {reason}.")
            lines.append(f"      Suggested next step: {s.recommended_next_step}.")
        lines.append("")

    lines.append(
        "I have not taken any action — I only watch. Decide which of these "
        "you want a human to handle next."
    )
    return "\n".join(lines).rstrip() + "\n"


__all__ = (
    "to_machine_json",
    "to_slack_summary",
    "to_broker_report",
    "FORBIDDEN_OUTPUT_TOKENS",
)
