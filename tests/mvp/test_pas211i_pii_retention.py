"""PAS211I — PII minimization, error redaction, and readiness-gate cleanup.

Proves: the PII sanitizer masks phone/email/secret strings; error_store redacts
before storing; pas_events no longer carry raw spoken text (lead.extracted /
objection / callback); ingestion events stay PII-free; Slack payloads never leak
secrets (while lead contact for handoff is intentionally kept) and the Slack
sanitizer is wired into BOTH send transports; benign operational fields survive;
and the stale readiness-gate self-checks are gone.
"""
import asyncio
import inspect
import json
import re
import subprocess
import sys
from pathlib import Path

import pytest

from app.services.security.pii_safety import (
    mask_email,
    mask_name_if_needed,
    mask_phone,
    redact_pii,
    sanitize_error_message,
    sanitize_event_payload,
    sanitize_slack_payload,
)

_REPO_ROOT = Path(__file__).resolve().parents[2]


# ── masking primitives ─────────────────────────────────────────────
def test_mask_phone():
    # 11 digits -> first 3 + (len-5) stars + last 2
    assert mask_phone("+13055551234") == "130******34"
    assert "5555" not in mask_phone("305-555-1234")
    assert mask_phone("") == ""


def test_mask_email():
    out = mask_email("marcus.lee@example.com")
    assert out.endswith("@example.com")
    assert "marcus.lee" not in out


def test_mask_name_if_needed():
    assert mask_name_if_needed("Marcus Lee") == "Marcus ***"
    assert mask_name_if_needed("Marcus") == "Marcus"
    assert mask_name_if_needed("") == ""


def test_redact_pii_free_text():
    raw = "Call Marcus at 305-555-1234 or marcus@example.com, key pas_abcdefghijklmno"
    out = redact_pii(raw)
    assert "305-555-1234" not in out and "[phone]" in out
    assert "marcus@example.com" not in out and "[email]" in out
    assert "pas_abcdefghijklmno" not in out and "[secret]" in out


def test_redact_pii_preserves_benign():
    benign = "Booking failed: Cal.com returned 422 for event_type 17"
    assert redact_pii(benign) == benign


# ── event payload sanitizer ────────────────────────────────────────
def test_sanitize_event_payload_masks_and_keeps_structure():
    payload = {
        "event_type": "lead.ingested",          # structured — keep
        "source": "website_form",               # label — keep
        "lead_created": True,                    # bool — keep
        "phone": "+13055551234",                 # PII key — mask
        "email": "a@b.com",                      # PII key — mask
        "raw_text": "I'm Marcus, call me at 305-555-1234",  # raw text — drop to len
        "notes": "interested in 123 Main",       # free text — pii-redact only
    }
    out = sanitize_event_payload(payload)
    assert out["event_type"] == "lead.ingested" and out["source"] == "website_form"
    assert out["lead_created"] is True
    assert out["phone"] != "+13055551234" and "5555" not in out["phone"]
    assert out["email"] != "a@b.com"
    assert out["raw_text"].startswith("[redacted:len=")
    assert "305-555-1234" not in str(out)


# ── error_store redaction ──────────────────────────────────────────
def test_error_store_redacts_pii_and_secrets(monkeypatch):
    import app.db.error_store as es

    captured = {}

    def _fake_event(evt, **kw):
        captured["event_payload"] = kw.get("payload")

    class _Ins:
        def __init__(self, row): captured["row"] = row
        def execute(self): return None

    class _Tbl:
        def insert(self, row): return _Ins(row)

    class _DB:
        def table(self, name): return _Tbl()

    monkeypatch.setattr(es, "log_event_bg", _fake_event)
    monkeypatch.setattr(es, "get_supabase", lambda: _DB())

    jwt = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkw.AbCdEfGhIjKlMnOp"
    ok = es.log_error(
        "calcom",
        message="Booking failed for marcus@example.com (305-555-1234)",
        detail=f"Authorization: Bearer {jwt} ; key pas_abcdefghijklmnop",
    )
    assert ok is True
    blob = str(captured["event_payload"]) + str(captured["row"])
    assert "marcus@example.com" not in blob
    assert "305-555-1234" not in blob
    assert "pas_abcdefghijklmnop" not in blob
    assert jwt not in blob
    # still useful: the service label survives
    assert captured["row"]["service"] == "calcom"


# ── pas_events no longer carry raw spoken text ─────────────────────
def test_lead_extracted_event_has_no_raw_text():
    import app.engine.state_machine as sm
    src = inspect.getsource(sm.PASEngine._log_lead_extracted)
    assert '"raw_text"' not in src           # raw spoken text removed
    assert "raw_text_len" in src             # replaced by a length signal


def test_objection_and_callback_events_have_no_raw_excerpts():
    import app.engine.state_machine as sm
    full = inspect.getsource(sm)
    assert '"text": text[:500]' not in full          # objection raw text gone
    assert '"trigger_excerpt": (text or "")[:200]' not in full  # callback excerpt gone
    assert "text_len" in full and "trigger_len" in full


# ── ingestion events remain PII-free ───────────────────────────────
def test_ingestion_events_are_pii_free():
    # PAS213 already builds PII-free events: the lead.ingested payload carries
    # has_email / has_message booleans (structural), not raw phone/email/message.
    import app.services.ingestion.lead_ingestion as li
    src = inspect.getsource(li.ingest_digital_lead)
    # isolate the lead.ingested event payload block
    assert "has_email" in src and "has_message" in src
    block = src[src.find('"lead.ingested"'):]
    block = block[: block.find("return")]
    for raw_key in ('"phone"', '"email"', '"name"', '"message"'):
        assert raw_key not in block, f"event payload must not contain {raw_key}"


# ── Slack payload: secrets never leak, contact handoff kept ────────
def test_sanitize_slack_payload_strips_secrets_keeps_contact():
    payload = {
        "lead_name": "Marcus Lee",
        "lead_phone": "+13055551234",       # intentional operational handoff — kept
        "webhook": "pas_abcdefghijklmnop",  # secret — redacted
    }
    out = sanitize_slack_payload(payload)
    assert out["lead_name"] == "Marcus Lee"            # handoff preserved
    assert out["lead_phone"] == "+13055551234"
    assert out["webhook"] == "[secret]"                # secret removed


# ── Slack send boundary: sanitizer is actually wired ──────────────


class _FakeResp:
    def __init__(self, status_code=200, text="ok"):
        self.status_code = status_code
        self.text = text

    def raise_for_status(self):
        return None


def _fake_async_client(captured):
    """A drop-in for httpx.AsyncClient that records the posted JSON body."""
    class _Client:
        def __init__(self, *a, **k):
            pass

        async def __aenter__(self):
            return self

        async def __aexit__(self, *a):
            return False

        async def post(self, url, json=None):
            captured["url"] = url
            captured["json"] = json
            return _FakeResp()

    return _Client


def test_slack_send_paths_wire_sanitizer():
    # Both Slack transports must reference sanitize_slack_payload at their send
    # boundary — the runtime guarantee, not just a utility that exists.
    import app.services.notifications.slack_client as sc
    import app.services.notifications.slack_sender as ss
    assert "sanitize_slack_payload" in inspect.getsource(sc._post_to_slack)
    assert "sanitize_slack_payload" in inspect.getsource(ss.send_slack_notification)


def test_slack_client_strips_secrets_keeps_contact(monkeypatch):
    import app.services.notifications.slack_client as sc
    captured = {}
    monkeypatch.setattr(sc.httpx, "AsyncClient", _fake_async_client(captured))

    lead = {"name": "Marcus Lee", "phone_number": "+13055551234",
            "email": "marcus@example.com", "intent": "buy", "budget": "500k",
            "timeline": "3 months", "booking_slot": ""}
    # A secret accidentally echoed into the summary text must not reach Slack.
    summary = "Confirmed. leaked pas_abcdefghijklmnop and sk-ABCDEFGHIJKL1234"
    asyncio.run(sc.send_call_summary(
        "https://hooks.slack.com/services/T000/B000/SECRETTOKEN0123456789",
        summary, "booked", lead, 142))

    blob = json.dumps(captured["json"])
    assert "pas_abcdefghijklmnop" not in blob
    assert "sk-ABCDEFGHIJKL1234" not in blob
    assert "[secret]" in blob
    # intentional operational handoff preserved
    assert "Marcus Lee" in blob and "+13055551234" in blob and "marcus@example.com" in blob


def test_slack_sender_strips_secrets_keeps_text(monkeypatch):
    import app.services.notifications.slack_sender as ss
    captured = {}
    monkeypatch.setattr(ss.httpx, "AsyncClient", _fake_async_client(captured))

    msg = "New lead Marcus (+13055551234) — token xoxb-abcdefghij1234567890"
    ok = asyncio.run(ss.send_slack_notification(
        "https://hooks.slack.com/services/T000/B000/SECRETTOKEN0123456789", msg))

    assert ok is True
    blob = json.dumps(captured["json"])
    assert "xoxb-abcdefghij1234567890" not in blob
    assert "[secret]" in blob
    # normal operational content still works
    assert "Marcus" in blob and "+13055551234" in blob


def test_slack_failure_does_not_log_webhook_url(monkeypatch, caplog):
    import app.services.notifications.slack_client as sc
    webhook = "https://hooks.slack.com/services/T000/B000/SECRETTOKEN0123456789"

    class _Boom:
        def __init__(self, *a, **k):
            pass

        async def __aenter__(self):
            return self

        async def __aexit__(self, *a):
            return False

        async def post(self, url, json=None):
            raise RuntimeError(f"Server error '500' for url '{url}'")

    monkeypatch.setattr(sc.httpx, "AsyncClient", _Boom)
    with caplog.at_level("ERROR"):
        asyncio.run(sc._post_to_slack(
            webhook, [{"type": "section", "text": {"type": "mrkdwn", "text": "hi"}}]))

    logged = " ".join(r.getMessage() for r in caplog.records)
    assert "SECRETTOKEN0123456789" not in logged
    assert webhook not in logged
    assert "[slack-webhook]" in logged


# ── benign operational event fields remain useful ──────────────────
def test_benign_event_fields_preserved():
    payload = {"outcome": "booked", "duration_seconds": 142, "states_visited": 5,
               "source": "simulated", "is_outbound": False}
    out = sanitize_event_payload(payload)
    assert out == payload   # nothing PII-shaped → untouched


# ── readiness-gate cleanup ─────────────────────────────────────────
def test_pas191_readiness_gate_is_ready():
    proc = subprocess.run(
        [sys.executable, str(_REPO_ROOT / "scripts" / "pas191_slack_nl_command_readiness_check.py"),
         "--summary-only"],
        cwd=str(_REPO_ROOT), capture_output=True, text=True, timeout=120,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "verdict=READY" in proc.stdout
    assert "blockers=0" in proc.stdout


def test_retired_checkpoint_scripts_stay_absent():
    for rel in (
        "scripts/pas186_final_cutover_readiness_check.py",
        "scripts/pas190_final_wirethrough_readiness_check.py",
        "scripts/pas170_operator_survival_readiness_check.py",
    ):
        assert not (_REPO_ROOT / rel).exists()
