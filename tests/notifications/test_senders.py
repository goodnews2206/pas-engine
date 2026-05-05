"""
Failure-tolerance tests for the PAS134 senders + dispatcher.

Verifies the contract that every transport returns False (and never
raises) when its credential is missing or its remote call fails. No
real network calls — Resend and Slack endpoints are short-circuited
either by missing config or by monkey-patching the inner http call.

Runnable directly:
    python tests/notifications/test_senders.py
"""

import asyncio
import os
import sys

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")),
)

# Force RESEND_API_KEY blank for the email-skip path, and set a known
# BASE_URL so the dispatcher's workflow link is deterministic. Both
# happen BEFORE we import anything that calls get_settings(), so the
# Settings cache picks them up on first access.
os.environ["RESEND_API_KEY"] = ""
os.environ["BASE_URL"] = "https://example.test"

from app.services.notifications import email_sender as es
from app.services.notifications import slack_sender as ss
from app.services.notifications import lead_alerts as la


def _run(coro):
    return asyncio.get_event_loop().run_until_complete(coro) \
        if sys.version_info < (3, 10) else asyncio.run(coro)


# ───────────── email_sender ─────────────

def test_email_skips_when_api_key_missing():
    # RESEND_API_KEY is "" via env above.
    result = _run(es.send_email_notification(
        to=["owner@example.com"],
        subject="hi",
        body="body",
    ))
    assert result is False


def test_email_skips_when_no_recipients():
    # Even with a key, empty 'to' must short-circuit.
    es_settings = es.get_settings()
    original_key = es_settings.RESEND_API_KEY
    object.__setattr__(es_settings, "RESEND_API_KEY", "fake-but-present")
    try:
        result = _run(es.send_email_notification(to=[], subject="x", body="y"))
        assert result is False
        result = _run(es.send_email_notification(to=["", None, "  "], subject="x", body="y"))
        assert result is False
    finally:
        object.__setattr__(es_settings, "RESEND_API_KEY", original_key)


def test_email_returns_false_on_network_failure(monkeypatch=None):
    # With key present and a recipient, force the http POST to raise.
    es_settings = es.get_settings()
    original_key = es_settings.RESEND_API_KEY
    object.__setattr__(es_settings, "RESEND_API_KEY", "fake-but-present")

    class _BoomClient:
        def __init__(self, *a, **kw): pass
        async def __aenter__(self): return self
        async def __aexit__(self, *a): return False
        async def post(self, *a, **kw):
            raise RuntimeError("simulated network failure")

    original_async_client = es.httpx.AsyncClient
    es.httpx.AsyncClient = _BoomClient  # type: ignore[assignment]
    try:
        result = _run(es.send_email_notification(
            to=["owner@example.com"],
            subject="hi",
            body="body",
        ))
        assert result is False
    finally:
        es.httpx.AsyncClient = original_async_client  # type: ignore[assignment]
        object.__setattr__(es_settings, "RESEND_API_KEY", original_key)


# ───────────── slack_sender ─────────────

def test_slack_skips_when_webhook_empty():
    assert _run(ss.send_slack_notification("", "hi")) is False
    assert _run(ss.send_slack_notification(None, "hi")) is False  # type: ignore[arg-type]


def test_slack_skips_when_message_empty():
    assert _run(ss.send_slack_notification("https://hooks.slack.com/x", "")) is False


def test_slack_returns_false_on_network_failure():
    class _BoomClient:
        def __init__(self, *a, **kw): pass
        async def __aenter__(self): return self
        async def __aexit__(self, *a): return False
        async def post(self, *a, **kw):
            raise RuntimeError("simulated slack outage")

    original = ss.httpx.AsyncClient
    ss.httpx.AsyncClient = _BoomClient  # type: ignore[assignment]
    try:
        result = _run(ss.send_slack_notification(
            "https://hooks.slack.com/services/AAA/BBB/CCC",
            "test",
        ))
        assert result is False
    finally:
        ss.httpx.AsyncClient = original  # type: ignore[assignment]


# ───────────── dispatch_lead_notification ─────────────

def test_dispatch_skips_when_no_destinations_configured():
    brokerage = {"id": "remax-miami", "notification_config": {}}
    status = _run(la.dispatch_lead_notification(
        call_sid="SIM-1",
        brokerage=brokerage,
        outcome="callback_requested",
        lead={"intent": "Buy", "budget": "$500k", "timeline": "1 month"},
    ))
    assert status["skipped"] is True
    assert status["email_recipients"] == 0
    assert status["slack_configured"] is False


def test_dispatch_resolves_email_from_notification_config_list():
    # New PAS133-shape config wins over legacy owner_email.
    brokerage = {
        "id": "remax-miami",
        "owner_email": "fallback@example.com",
        "notification_config": {"email": ["a@example.com", "b@example.com"]},
    }
    captured: dict = {"subject": None, "to": None, "body": None}

    async def fake_email(to, subject, body):
        captured["to"] = list(to)
        captured["subject"] = subject
        captured["body"] = body
        return True

    original = la.send_email_notification
    la.send_email_notification = fake_email  # type: ignore[assignment]
    try:
        status = _run(la.dispatch_lead_notification(
            call_sid="SIM-CALLBACK",
            brokerage=brokerage,
            outcome="callback_requested",
            lead={"intent": "Buy", "budget": "$500k", "timeline": "1 month"},
        ))
    finally:
        la.send_email_notification = original  # type: ignore[assignment]

    assert status["skipped"] is False
    assert status["email_ok"] is True
    assert status["email_recipients"] == 2
    assert captured["to"] == ["a@example.com", "b@example.com"]
    assert captured["subject"] == "New Lead — Callback Scheduled"
    assert "Lead intent: Buy" in captured["body"]


def test_dispatch_falls_back_to_legacy_owner_email_and_webhook():
    # Legacy-shaped brokerage record (today's data).
    brokerage = {
        "id": "remax-miami",
        "owner_email": "owner@example.com",
        "slack_webhook_url": "https://hooks.slack.com/services/X/Y/Z",
        "notification_config": {},
    }
    email_call: dict = {"to": None}
    slack_call: dict = {"webhook": None, "message": None}

    async def fake_email(to, subject, body):
        email_call["to"] = list(to)
        return True

    async def fake_slack(webhook_url, message):
        slack_call["webhook"] = webhook_url
        slack_call["message"] = message
        return True

    orig_e = la.send_email_notification
    orig_s = la.send_slack_notification
    la.send_email_notification = fake_email  # type: ignore[assignment]
    la.send_slack_notification = fake_slack  # type: ignore[assignment]
    try:
        status = _run(la.dispatch_lead_notification(
            call_sid="SIM-LEGACY",
            brokerage=brokerage,
            outcome="booked",
            lead={"intent": "Sell", "budget": "$1M", "timeline": "3 weeks", "booking_slot": "Wed 15:00"},
        ))
    finally:
        la.send_email_notification = orig_e  # type: ignore[assignment]
        la.send_slack_notification = orig_s  # type: ignore[assignment]

    assert status["skipped"] is False
    assert email_call["to"] == ["owner@example.com"]
    assert slack_call["webhook"] == "https://hooks.slack.com/services/X/Y/Z"
    assert "*New PAS Lead*" in (slack_call["message"] or "")
    assert "Action: Property viewing booked (Wed 15:00)" in (slack_call["message"] or "")


def test_dispatch_continues_when_email_leg_raises():
    brokerage = {
        "id": "remax-miami",
        "owner_email": "owner@example.com",
        "slack_webhook_url": "https://hooks.slack.com/services/X/Y/Z",
    }
    slack_called = {"hit": False}

    async def boom_email(*a, **kw):
        raise RuntimeError("email boom")

    async def fake_slack(webhook_url, message):
        slack_called["hit"] = True
        return True

    orig_e = la.send_email_notification
    orig_s = la.send_slack_notification
    la.send_email_notification = boom_email  # type: ignore[assignment]
    la.send_slack_notification = fake_slack  # type: ignore[assignment]
    try:
        status = _run(la.dispatch_lead_notification(
            call_sid="SIM-EMAIL-BOOM",
            brokerage=brokerage,
            outcome="callback_requested",
            lead={},
        ))
    finally:
        la.send_email_notification = orig_e  # type: ignore[assignment]
        la.send_slack_notification = orig_s  # type: ignore[assignment]

    # Email leg failed but dispatcher must NOT raise; Slack must still fire.
    assert status["email_ok"] is False
    assert status["slack_ok"] is True
    assert slack_called["hit"] is True


def test_dispatch_includes_workflow_url_in_messages():
    brokerage = {
        "id": "remax-miami",
        "owner_email": "owner@example.com",
        "slack_webhook_url": "https://hooks.slack.com/services/X/Y/Z",
    }
    captured: dict = {"email_body": None, "slack_message": None}

    async def fake_email(to, subject, body):
        captured["email_body"] = body
        return True

    async def fake_slack(webhook_url, message):
        captured["slack_message"] = message
        return True

    orig_e = la.send_email_notification
    orig_s = la.send_slack_notification
    la.send_email_notification = fake_email  # type: ignore[assignment]
    la.send_slack_notification = fake_slack  # type: ignore[assignment]
    try:
        _run(la.dispatch_lead_notification(
            call_sid="SIM-YC-W26-CALLBACK-001",
            brokerage=brokerage,
            outcome="callback_requested",
            lead={"intent": "Buy", "budget": "$500k", "timeline": "Next month"},
        ))
    finally:
        la.send_email_notification = orig_e  # type: ignore[assignment]
        la.send_slack_notification = orig_s  # type: ignore[assignment]

    expected = "https://example.test/dashboard/calls/SIM-YC-W26-CALLBACK-001"
    assert expected in (captured["email_body"] or "")
    assert expected in (captured["slack_message"] or "")


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
