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

def format_stats(data: Dict[str, object]) -> str:
    """All-time stats. Inputs: total, completed, booked."""
    total     = int(data.get("total")     or 0)
    completed = int(data.get("completed") or 0)
    booked    = int(data.get("booked")    or 0)
    pct = round(booked * 100 / completed, 1) if completed else 0.0
    return _safe(
        "📊 *All-time stats*\n"
        f"Total calls: {total} · Completed: {completed}\n"
        f"Booked: {booked} · Conversion: {pct}%"
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
    """Static help message — closed list of supported questions."""
    return _safe(
        "👋 *PAS — questions I can answer*\n"
        "• `stats` — all-time conversion\n"
        "• `calls today` / `calls this week` — call volume\n"
        "• `response rate` — pickup rate\n"
        "• `bookings today` / `did we book any clients`\n"
        "• `callbacks due` — pending callbacks\n"
        "• `queue` — pending-call queue depth\n"
        "• `incidents` — open operational incidents\n"
        "• `policy` — circuit breaker + cutover posture\n"
        "• `health` — DB / worker / telephony\n"
        "• `are we paused`\n"
        "• `help` — this list\n"
        "\nMutation commands (`pause`, `resume`, `push`, `remove`) "
        "use the exact command — they are NOT natural-language."
    )


def format_unknown() -> str:
    """Unknown / unsupported intent fallback."""
    return _safe(
        "🤔 I didn't recognise that question. Try `help` to see the "
        "list of read-only questions, or use an exact mutation command "
        "(`pause`, `resume`, `push …`, `remove …`)."
    )


def format_error(intent: str, error_class: str = "Exception") -> str:
    """Generic error fallback. Never echoes the underlying message."""
    safe_intent = (intent or "").strip().lower()
    if safe_intent not in {
        "stats", "calls_today", "calls_week", "response_rate",
        "bookings_today", "callbacks_due", "queue", "incidents",
        "policy", "health", "paused_status",
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
