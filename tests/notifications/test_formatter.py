"""
Tests for app.services.notifications.formatter — pure formatting.

No DB, no HTTP, no FastAPI. Runnable directly:
    python tests/notifications/test_formatter.py
"""

import os
import sys

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")),
)

from app.services.notifications.formatter import format_lead_notification


def _callback_data():
    return {
        "call_id": "SIM-YC-W26-CALLBACK-001",
        "brokerage_id": "remax-miami",
        "outcome": "callback_requested",
        "lead": {
            "name": "Jane Doe",
            "phone_number": "+13055551234",
            "intent": "Buy",
            "budget": "$500k",
            "timeline": "Next month",
        },
        "workflow_url": "https://example.com/dashboard/calls/SIM-YC-W26-CALLBACK-001",
    }


def _booked_data():
    d = _callback_data()
    d["outcome"] = "booked"
    d["lead"]["booking_slot"] = "Tue 14:00"
    return d


# ───────────── shape contract ─────────────

def test_returns_three_keys():
    out = format_lead_notification(_callback_data())
    assert set(out.keys()) == {"subject", "email_body", "slack_message"}


def test_all_values_are_strings():
    out = format_lead_notification(_callback_data())
    for k, v in out.items():
        assert isinstance(v, str), f"{k} is not str: {type(v)}"


# ───────────── subject ─────────────

def test_subject_callback():
    out = format_lead_notification(_callback_data())
    assert out["subject"] == "New Lead — Callback Scheduled"


def test_subject_booked():
    out = format_lead_notification(_booked_data())
    assert out["subject"] == "New Lead — Booking Confirmed"


def test_subject_qualified_callback():
    d = _callback_data()
    d["outcome"] = "qualified_callback_requested"
    out = format_lead_notification(d)
    assert out["subject"] == "New Lead — Callback Scheduled"


def test_subject_falls_back_for_unknown_outcome():
    d = _callback_data()
    d["outcome"] = "weird_outcome"
    out = format_lead_notification(d)
    assert out["subject"] == "New Lead — Update"


# ───────────── email body ─────────────

def test_email_body_contains_required_lines():
    out = format_lead_notification(_callback_data())
    body = out["email_body"]
    assert "Lead intent: Buy" in body
    assert "Budget: $500k" in body
    assert "Timeline: Next month" in body
    assert "Action: Callback scheduled" in body
    assert "View workflow:" in body
    assert "https://example.com/dashboard/calls/SIM-YC-W26-CALLBACK-001" in body


def test_email_body_booked_includes_slot():
    out = format_lead_notification(_booked_data())
    assert "Action: Property viewing booked (Tue 14:00)" in out["email_body"]


def test_email_body_handles_missing_workflow_url():
    d = _callback_data()
    d["workflow_url"] = ""
    out = format_lead_notification(d)
    assert "View workflow:" not in out["email_body"]


def test_email_body_uses_dashes_for_missing_fields():
    d = {
        "outcome": "callback_requested",
        "lead": {},
    }
    out = format_lead_notification(d)
    assert "Lead intent: —" in out["email_body"]
    assert "Budget: —" in out["email_body"]
    assert "Timeline: —" in out["email_body"]


# ───────────── slack message ─────────────

def test_slack_message_starts_with_header():
    out = format_lead_notification(_callback_data())
    assert out["slack_message"].startswith("*New PAS Lead*")


def test_slack_message_contains_required_fields():
    out = format_lead_notification(_callback_data())
    msg = out["slack_message"]
    assert "Intent: Buy" in msg
    assert "Budget: $500k" in msg
    assert "Timeline: Next month" in msg
    assert "Action: Callback scheduled" in msg


def test_slack_message_uses_mrkdwn_link():
    out = format_lead_notification(_callback_data())
    assert "<https://example.com/dashboard/calls/SIM-YC-W26-CALLBACK-001|View workflow>" in out["slack_message"]


def test_slack_message_handles_missing_workflow_url():
    d = _callback_data()
    d["workflow_url"] = ""
    out = format_lead_notification(d)
    assert "View workflow" not in out["slack_message"]


# ───────────── defensive ─────────────

def test_handles_none_call_data():
    # Should not crash; produces an "unknown" outcome notification.
    out = format_lead_notification(None)
    assert "subject" in out
    assert "email_body" in out
    assert "slack_message" in out


def test_handles_empty_dict():
    out = format_lead_notification({})
    assert "subject" in out
    assert "Lead intent: —" in out["email_body"]


def test_handles_lead_field_with_none_values():
    d = {
        "outcome": "booked",
        "lead": {"intent": None, "budget": None, "timeline": None, "name": None, "phone_number": None},
    }
    out = format_lead_notification(d)
    assert "Lead intent: —" in out["email_body"]
    assert "Budget: —" in out["email_body"]


def test_handles_non_string_outcome():
    out = format_lead_notification({"outcome": "", "lead": {}})
    assert out["subject"] == "New Lead — Update"


# ───────────── runner ─────────────

if __name__ == "__main__":
    fns = [v for k, v in list(globals().items()) if k.startswith("test_") and callable(v)]
    failures = 0
    for fn in fns:
        name = fn.__name__
        try:
            fn()
            print(f"  PASS {name}")
        except AssertionError as e:
            failures += 1
            print(f"  FAIL {name} -- {e}")
        except Exception as e:
            failures += 1
            print(f"  FAIL {name} -- {type(e).__name__}: {e}")
    print(f"\n{len(fns) - failures}/{len(fns)} passed")
    sys.exit(0 if failures == 0 else 1)
