"""
PAS191 — Safe Response Formatter for Bounded Slack NL Intents.

Pure-function formatters that turn an intent code + a closed,
pre-redacted DB result into a Slack-safe response string.

Hard rules:

  * NO PII. Responses never include phone numbers, emails, names,
    transcripts, raw payloads, secrets, signatures, dedupe keys,
    API keys, or webhook URLs. Counts and labels only.

  * NO free-form text from the LLM. Strings are built from a
    closed template per intent.

  * NO exceptions raised. If a query fails, the formatter emits
    a generic "couldn't fetch" message (with an opaque error
    class name) so the brokerage sees a useful response, not a
    stack trace.

  * NO speculative state. If a value is missing we say so
    explicitly ("not available") rather than inventing zero.

  * NO inline links to external systems. Slack messages must
    be safe to forward inside the brokerage's Slack workspace.

The functions in this module accept already-redacted data
structures. They do NOT call the DB themselves; that lives in
app/routes/slack_command.py via the existing query helpers and
PAS189 surfaces. This keeps formatting deterministic and unit
testable.
"""

from __future__ import annotations

from typing import Dict, Optional

# PAS204-C — verdict tokens for demo / rehearsal labelling.
# Kept as string constants here to avoid an import dependency
# on demo_data_detector when format_stats is called from old
# code paths that don't supply the flag at all.
_DEMO_VERDICT_DEMO_DETECTED:  str = "demo_detected"
_DEMO_VERDICT_NO_DEMO_SIGNAL: str = "no_demo_signal"
_DEMO_VERDICT_UNKNOWN:        str = "unknown"


# Forbidden tokens — defence in depth. If any of these appear in
# the formatted string we collapse to a safe fallback.
_PII_FORBIDDEN_TOKENS = (
    "phone",
    "phone_number",
    "email",
    "lead_name",
    "transcript",
    "raw_payload",
    "raw_email",
    "raw_body",
    "secret",
    "signature",
    "dedupe_key",
    "api_key",
    "webhook_url",
    "stack_trace",
)


def _safe(text: str) -> str:
    """
    Defence-in-depth: if a PII token slipped into the formatted
    text, drop the full message and replace it with a generic
    no-data line. This should never fire in practice; it exists
    to keep the Slack surface safe even if a future caller passes
    in unredacted data.
    """
    if not isinstance(text, str):
        return "ℹ️ No data available."
    lowered = text.lower()
    for tok in _PII_FORBIDDEN_TOKENS:
        if tok in lowered:
            return "ℹ️ Response redacted — contact operator."
    return text


# ──────────────────────────────────────────────────────────────────
# Per-intent formatters
# ──────────────────────────────────────────────────────────────────

def format_stats(
    data: Dict[str, object],
    *,
    demo_verdict: Optional[str] = None,
) -> str:
    """All-time stats. Inputs: total, completed, booked.

    PAS204-C: optional `demo_verdict` token (closed vocab from
    `demo_data_detector.VERDICT_VALUES`) lets the caller label
    the rendered output:

      * "demo_detected"     -> header replaced with
                               "📊 Demo stats — rehearsal data",
                               no trailing note.
      * "no_demo_signal"    -> normal header, no note (real
                               production data, detector found
                               no markers).
      * "unknown"           -> normal header + trailing
                               conservative note prompting the
                               operator to verify the env.
      * None (legacy)       -> identical output to pre-PAS204-C.
                               Backwards-compatible default.
    """
    total     = int(data.get("total")     or 0)
    completed = int(data.get("completed") or 0)
    booked    = int(data.get("booked")    or 0)
    pct = round(booked * 100 / completed, 1) if completed else 0.0
    if demo_verdict == _DEMO_VERDICT_DEMO_DETECTED:
        header = "📊 *Demo stats — rehearsal data*"
        note = ""
    elif demo_verdict == _DEMO_VERDICT_UNKNOWN:
        header = "📊 *All-time stats*"
        note = (
            "\n_Note: verify whether this environment is using "
            "demo/rehearsal data before sharing publicly._"
        )
    else:  # None or "no_demo_signal" — preserve legacy output.
        header = "📊 *All-time stats*"
        note = ""
    return _safe(
        f"{header}\n"
        f"Total calls: {total} · Completed: {completed}\n"
        f"Booked: {booked} · Conversion: {pct}%"
        f"{note}"
    )


def format_calls_today(data: Dict[str, object]) -> str:
    """Today's call volume. Inputs: total, booked, not_booked."""
    total      = int(data.get("total")      or 0)
    booked     = int(data.get("booked")     or 0)
    not_booked = int(data.get("not_booked") or 0)
    pct = round(booked * 100 / total, 1) if total else 0.0
    return _safe(
        "📞 *Calls today*\n"
        f"Total: {total} · Booked: {booked} · Not booked: {not_booked}\n"
        f"Conversion: {pct}%"
    )


def format_calls_week(data: Dict[str, object]) -> str:
    """This week's call volume."""
    total      = int(data.get("total")      or 0)
    booked     = int(data.get("booked")     or 0)
    not_booked = int(data.get("not_booked") or 0)
    pct = round(booked * 100 / total, 1) if total else 0.0
    return _safe(
        "📞 *Calls this week*\n"
        f"Total: {total} · Booked: {booked} · Not booked: {not_booked}\n"
        f"Conversion: {pct}%"
    )


def format_response_rate(data: Dict[str, object]) -> str:
    """Pickup / answer rate. Inputs: total, completed."""
    total     = int(data.get("total")     or 0)
    completed = int(data.get("completed") or 0)
    pct = round(completed * 100 / total, 1) if total else 0.0
    return _safe(
        "📈 *Response rate*\n"
        f"Dialled: {total} · Connected: {completed}\n"
        f"Pickup rate: {pct}%"
    )


def format_bookings_today(data: Dict[str, object]) -> str:
    """Bookings booked today. Inputs: booked_count."""
    booked = int(data.get("booked_count") or 0)
    if booked == 0:
        return _safe("📅 *Bookings today*\nNo showings booked yet today.")
    plural = "showing" if booked == 1 else "showings"
    return _safe(f"📅 *Bookings today*\n{booked} {plural} booked.")


def format_callbacks_due(data: Dict[str, object]) -> str:
    """Pending callbacks. Inputs: pending_count, overdue_count."""
    pending = int(data.get("pending_count") or 0)
    overdue = int(data.get("overdue_count") or 0)
    if pending == 0 and overdue == 0:
        return _safe("📞 *Callbacks*\nNo pending callbacks.")
    return _safe(
        "📞 *Callbacks*\n"
        f"Pending: {pending} · Overdue: {overdue}"
    )


def format_queue(data: Dict[str, object]) -> str:
    """Pending-call queue depth. Inputs: queue_size, worker_state."""
    size = int(data.get("queue_size") or 0)
    worker_state = str(data.get("worker_state") or "off")
    if worker_state not in ("on", "off"):
        worker_state = "off"
    return _safe(
        "📋 *Call queue*\n"
        f"Pending calls: {size} · Worker: {worker_state}"
    )


def format_incidents(data: Dict[str, object]) -> str:
    """Open incidents summary. Inputs: open_count, severity_counts (dict)."""
    open_count = int(data.get("open_count") or 0)
    sev = data.get("severity_counts") or {}
    if not isinstance(sev, dict):
        sev = {}
    if open_count == 0:
        return _safe("🟢 *Incidents*\nNo open incidents.")
    parts = []
    for label in ("critical", "high", "medium", "low"):
        n = int(sev.get(label) or 0)
        if n:
            parts.append(f"{label}: {n}")
    breakdown = (" · " + " · ".join(parts)) if parts else ""
    return _safe(f"🚨 *Incidents*\nOpen: {open_count}{breakdown}")


def format_policy(data: Dict[str, object]) -> str:
    """
    Policy posture roll-up summary. Inputs: breaker_state,
    cutover_state, security_gate.
    """
    breaker  = str(data.get("breaker_state")  or "unknown")
    cutover  = str(data.get("cutover_state")  or "unknown")
    security = str(data.get("security_gate")  or "unknown")
    return _safe(
        "🛡️ *Policy posture*\n"
        f"Circuit breaker: {breaker}\n"
        f"Cutover: {cutover}\n"
        f"Security gate: {security}"
    )


def format_health(data: Dict[str, object]) -> str:
    """System health. Inputs: db, worker, twilio (each str)."""
    db      = str(data.get("db")      or "unknown")
    worker  = str(data.get("worker")  or "unknown")
    twilio  = str(data.get("twilio")  or "unknown")
    return _safe(
        "🩺 *System health*\n"
        f"Database: {db}\n"
        f"Worker: {worker}\n"
        f"Telephony: {twilio}"
    )


def format_leads_today(data: Dict[str, object]) -> str:
    """
    Today's new-lead intake. Inputs:
      new_leads      — count of leads created today
      call_eligible  — count of new leads not yet called
      pending_queue  — count of pending-call queue entries today
    All inputs default to 0 if missing / unavailable.
    """
    new_leads     = int(data.get("new_leads")     or 0)
    call_eligible = int(data.get("call_eligible") or 0)
    pending_queue = int(data.get("pending_queue") or 0)
    return _safe(
        "🧲 *Leads today*\n"
        f"New leads: {new_leads}\n"
        f"Call eligible: {call_eligible}\n"
        f"Pending queue: {pending_queue}"
    )


# ──────────────────────────────────────────────────────────────────
# PAS192 — operator-experience formatters
# ──────────────────────────────────────────────────────────────────
#
# Both formatters below accept a closed, pre-aggregated dict from
# the dispatcher in app/routes/slack_command.py. They never touch
# the DB and never receive raw row data. Same PII guard as every
# other PAS191 formatter — the _safe() filter scrubs the output if
# a poisoned label sneaks in.

# Closed allow-list of warning codes the dispatcher may pass to
# format_today_summary. The formatter ignores anything else, which
# keeps the surface bounded and prevents a future caller from
# accidentally rendering arbitrary text.
_TODAY_SUMMARY_WARNING_LABELS: Dict[str, str] = {
    "no_agents":         "No agents are configured — assign one to route bookings.",
    "queue_backed_up":   "Pending call queue is backed up.",
    "worker_off":        "Pending-call worker is OFF.",
    "low_response_rate": "Today's response rate is below 30%.",
    "no_bookings":       "No bookings yet today.",
    "no_calls":          "No calls placed yet today.",
    "no_leads":          "No new leads yet today.",
    "incidents_open":    "Open operational incidents need attention.",
    "paused":            "PAS is paused — outbound calls won't run.",
}


# Closed allow-list of next-action priority codes. The dispatcher
# can only emit codes from this map; arbitrary text is dropped.
_NEXT_ACTION_LABELS: Dict[str, str] = {
    "assign_agents":           "Assign agents — none are configured.",
    "review_callbacks":        "Review overdue callbacks.",
    "follow_up_leads":         "Follow up call-eligible leads.",
    "review_queue":            "Review pending-call queue.",
    "resolve_incidents":       "Resolve open operational incidents.",
    "resume_pas":              "Resume PAS — it is currently paused.",
    "start_worker":            "Start the pending-call worker.",
    "review_failed_bookings":  "Review calls that ended without a booking.",
    "review_response_rate":    "Investigate today's low response rate.",
}


def format_today_summary(data: Dict[str, object]) -> str:
    """
    Operator daily wrap. Inputs (all ints unless noted):
      new_leads, calls_total, calls_connected, bookings,
      response_rate (float, 0-100), pending_queue,
      warnings (list of warning codes, optional).
    """
    new_leads       = int(data.get("new_leads")       or 0)
    calls_total     = int(data.get("calls_total")     or 0)
    calls_connected = int(data.get("calls_connected") or 0)
    bookings        = int(data.get("bookings")        or 0)
    pending_queue   = int(data.get("pending_queue")   or 0)
    try:
        response_rate = float(data.get("response_rate") or 0.0)
    except (TypeError, ValueError):
        response_rate = 0.0
    if response_rate < 0.0:
        response_rate = 0.0
    if response_rate > 100.0:
        response_rate = 100.0

    raw_warnings = data.get("warnings") or []
    warning_lines: list = []
    if isinstance(raw_warnings, (list, tuple)):
        for code in raw_warnings:
            label = _TODAY_SUMMARY_WARNING_LABELS.get(str(code))
            if label:
                warning_lines.append(f"• {label}")

    lines = [
        "🗓️ *Today's summary*",
        f"New leads: {new_leads}",
        f"Calls: {calls_total} · Connected: {calls_connected}",
        f"Bookings: {bookings}",
        f"Response rate: {round(response_rate, 1)}%",
        f"Pending queue: {pending_queue}",
    ]
    if warning_lines:
        lines.append("")
        lines.append("⚠️ *Watch:*")
        lines.extend(warning_lines)
    return _safe("\n".join(lines))


def format_next_action(data: Dict[str, object]) -> str:
    """
    Top 3 operational priorities the operator can act on next.
    Inputs:
      priorities — list of {"code": str, "detail": str|None} items
                   (detail is optional; if present and contains no
                   forbidden tokens it is appended to the label).
    Up to three priorities are rendered. If the list is empty, a
    no-action-needed message is returned.
    """
    raw = data.get("priorities") or []
    rendered: list = []
    if isinstance(raw, (list, tuple)):
        for item in raw:
            if len(rendered) >= 3:
                break
            if not isinstance(item, dict):
                continue
            code = str(item.get("code") or "")
            base = _NEXT_ACTION_LABELS.get(code)
            if not base:
                continue
            detail_raw = item.get("detail")
            line = base
            if isinstance(detail_raw, str) and detail_raw.strip():
                # Detail is only allowed to be a short count phrase
                # (digits + simple words). Anything richer is dropped.
                detail_clean = detail_raw.strip()
                if len(detail_clean) <= 80 and all(
                    ch.isalnum() or ch in " .,/()-" for ch in detail_clean
                ):
                    line = f"{base} ({detail_clean})"
            rendered.append(line)

    if not rendered:
        return _safe(
            "✅ *Next action*\n"
            "Nothing urgent surfaced from today's data. Try "
            "`summary` for a full operator wrap."
        )
    lines = ["🎯 *Next action — top priorities*"]
    for idx, line in enumerate(rendered, start=1):
        lines.append(f"{idx}. {line}")
    return _safe("\n".join(lines))


def format_paused_status(data: Dict[str, object]) -> str:
    """Active / paused status. Inputs: active (bool)."""
    raw = data.get("active")
    if raw is None:
        return _safe("⚠️ Paused status not available.")
    active = bool(raw)
    if active:
        return _safe("▶️ *PAS is active.* Outbound calls will run.")
    return _safe("⏸️ *PAS is paused.* No outbound calls.")


def format_help() -> str:
    """
    Static help message — natural-language examples first, then a
    short note on mutation commands. PAS192 rewords this so a
    brokerage owner sees real questions, not command jargon.
    """
    return _safe(
        "👋 *PAS — questions I can answer*\n"
        "Try things like:\n"
        "• _how many leads did we get today?_\n"
        "• _what's our response rate?_\n"
        "• _what should I do now?_\n"
        "• _show today's summary_\n"
        "• _did we book any clients today?_\n"
        "• _how many calls have we had today?_\n"
        "• _what callbacks do we owe?_\n"
        "• _are we paused?_\n"
        "• _any open incidents?_\n"
        "• _is the system up?_\n"
        "\nQuick references: `summary` · `next action` · `stats` · "
        "`calls today` · `calls this week` · `response rate` · "
        "`leads today` · `bookings today` · `callbacks` · `queue` · "
        "`incidents` · `policy` · `health` · `are we paused`.\n"
        "\nMutation commands (`pause`, `resume`, `push`, `remove`) "
        "still use the exact command — natural-language mutation is "
        "intentionally not supported in this phase."
    )


def format_unknown() -> str:
    """
    Unknown / unsupported intent fallback. PAS192 rewords this so
    a brokerage operator sees something they can act on instead of
    a robotic 'didn't understand' line.
    """
    return _safe(
        "🤔 I didn't catch that. I can answer operational "
        "questions about leads, calls, bookings, response rate, "
        "queue, callbacks, incidents, policy, health, and today's "
        "summary. Try: _what happened today?_ or _what should I "
        "do now?_ — type `help` for more."
    )


def format_error(intent: str, error_class: str = "Exception") -> str:
    """Generic error fallback. Never echoes the underlying message."""
    safe_intent = (intent or "").strip().lower()
    if safe_intent not in {
        "stats", "calls_today", "calls_week", "response_rate",
        "bookings_today", "callbacks_due", "queue", "incidents",
        "policy", "health", "paused_status", "leads_today",
        "today_summary", "next_action",
    }:
        safe_intent = "request"
    cls_raw = (error_class or "Exception").strip()
    # Take only the leading identifier — defends against callers
    # that pass a stringified exception like "ValueError('secret')"
    # instead of the bare type(e).__name__.
    cls_chars: list = []
    for ch in cls_raw:
        if ch.isalnum() or ch == "_":
            cls_chars.append(ch)
        else:
            break
    cls = "".join(cls_chars) or "Exception"
    return _safe(f"❌ Couldn't fetch {safe_intent.replace('_', ' ')} ({cls}).")
