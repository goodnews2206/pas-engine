"""
Lead Notification Formatter (PAS134).

Pure-function rendering of lead-outcome notifications into the three
shapes the senders expect:

    {"subject": str, "email_body": str, "slack_message": str}

Inputs are flexible: callers pass a `call_data` dict assembled from
whatever the call-finalisation path has on hand. Missing fields are
rendered as "—" so the formatter never crashes on partial data.

Expected `call_data` shape (all keys optional except outcome):
    {
        "outcome":       "callback_requested" | "qualified_callback_requested" | "booked" | ...,
        "call_id":       "<call_sid>",
        "brokerage_id":  "<id>",
        "lead": {
            "name":          "Jane Doe",
            "phone_number":  "+1305...",
            "intent":        "buy",
            "budget":        "$500k",
            "timeline":      "1 month",
            "booking_slot":  "Tue 14:00",     # only on booked
        },
        "workflow_url":  "https://.../dashboard/calls/<sid>",
    }
"""

from typing import Any


_DASH = "—"


def _safe_str(value: Any) -> str:
    """Convert any field into a non-empty display string, falling back to em-dash."""
    if value is None:
        return _DASH
    s = str(value).strip()
    return s if s else _DASH


def _action_label(outcome: str, lead: dict) -> str:
    """Human-readable 'what happened' line for a given outcome."""
    if outcome == "booked":
        slot = _safe_str(lead.get("booking_slot"))
        return f"Property viewing booked ({slot})" if slot != _DASH else "Property viewing booked"
    if outcome == "callback_requested":
        return "Callback scheduled"
    if outcome == "qualified_callback_requested":
        return "Qualified callback scheduled"
    if outcome == "transferred":
        return "Transferred to agent"
    if outcome == "not_booked":
        return "Lead followup needed"
    return f"Outcome: {outcome}"


def _subject_for(outcome: str) -> str:
    if outcome == "booked":
        return "New Lead — Booking Confirmed"
    if outcome in ("callback_requested", "qualified_callback_requested"):
        return "New Lead — Callback Scheduled"
    if outcome == "transferred":
        return "New Lead — Transferred to Agent"
    return "New Lead — Update"


def format_lead_notification(call_data: dict) -> dict:
    """
    Render a lead-outcome notification into subject + email + Slack bodies.

    Pure function. Does not touch Supabase, Resend, Slack, or settings.
    Safe to call with partial / messy data — every field is defensively
    coerced to a display string.
    """
    data = call_data or {}
    lead = data.get("lead") or {}

    outcome = (data.get("outcome") or "").strip() or "unknown"
    intent = _safe_str(lead.get("intent"))
    budget = _safe_str(lead.get("budget"))
    timeline = _safe_str(lead.get("timeline"))
    name = _safe_str(lead.get("name"))
    phone = _safe_str(lead.get("phone_number"))
    workflow_url = (data.get("workflow_url") or "").strip()
    action = _action_label(outcome, lead)

    subject = _subject_for(outcome)

    # ── Email body — plain text, line-per-field, optional workflow link ──
    email_lines = [
        f"Lead intent: {intent}",
        f"Budget: {budget}",
        f"Timeline: {timeline}",
        f"Action: {action}",
    ]
    if name != _DASH or phone != _DASH:
        email_lines.append("")
        email_lines.append(f"Lead: {name} ({phone})")
    if workflow_url:
        email_lines.append("")
        email_lines.append(f"View workflow: {workflow_url}")
    email_body = "\n".join(email_lines)

    # ── Slack message — same content, lightly Slack-flavoured ──
    slack_lines = [
        "*New PAS Lead*",
        "",
        f"Intent: {intent}",
        f"Budget: {budget}",
        f"Timeline: {timeline}",
        f"Action: {action}",
    ]
    if name != _DASH or phone != _DASH:
        slack_lines.append("")
        slack_lines.append(f"Lead: {name} ({phone})")
    if workflow_url:
        slack_lines.append("")
        # Slack mrkdwn link syntax: <url|label>
        slack_lines.append(f"→ <{workflow_url}|View workflow>")
    slack_message = "\n".join(slack_lines)

    return {
        "subject": subject,
        "email_body": email_body,
        "slack_message": slack_message,
    }
