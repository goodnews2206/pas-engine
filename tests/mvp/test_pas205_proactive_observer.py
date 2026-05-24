"""
PAS205 — Read-only proactive observer tests.

Coverage:

  * Each signal type fires on a focused fixture and stays quiet
    when the fixture is clean.
  * Clean pipeline emits zero signals.
  * Digest is deterministic — same snapshot at the same instant
    produces the same digest id and the same signal ids.
  * Human renderers carry no closed-vocab technical tokens and no
    "PAS205" / "SIMULATION_ONLY" / "live_behavior_changed" leak.
  * Source invariants:
      - observer_models.py / observer.py / observer_digest.py
        import no Twilio, Slack outbound, Supabase, LLM, dotenv,
        notifications, state machine, or worker modules.
      - No forbidden live-mutation / outbound identifiers.
      - No DB writes anywhere in the production surface.
  * Every emitted signal has live_behavior_changed=False.
"""

from __future__ import annotations

import ast
import json
import pathlib
import re
import sys
from datetime import datetime, timezone
from typing import List, Tuple

import pytest


_REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))


from app.services.proactive.observer import (  # noqa: E402
    AFTER_HOURS_PENDING_SECONDS,
    CALLBACK_GRACE_SECONDS,
    FIRST_RESPONSE_TARGET_SECONDS,
    REPEATED_FAILED_CALL_THRESHOLD,
    STALE_LEAD_AGE_SECONDS,
    observe,
)
from app.services.proactive.observer_digest import (  # noqa: E402
    FORBIDDEN_OUTPUT_TOKENS,
    to_broker_report,
    to_machine_json,
    to_slack_summary,
)
from app.services.proactive.observer_models import (  # noqa: E402
    SEVERITY_HIGH,
    SEVERITY_LOW,
    SEVERITY_MEDIUM,
    SEVERITIES,
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
    SUBJECT_TYPES,
    ObservedAgent,
    ObservedBooking,
    ObservedCall,
    ObservedCallback,
    ObservedLead,
    ObservedSnapshot,
)


# Anchor "now" for every fixture.
NOW_STR = "2026-05-23T14:00:00Z"
NOW_DT  = datetime(2026, 5, 23, 14, 0, 0, tzinfo=timezone.utc)


PRODUCTION_FILES: Tuple[str, ...] = (
    "app/services/proactive/observer_models.py",
    "app/services/proactive/observer.py",
    "app/services/proactive/observer_digest.py",
)


# ──────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────

def _snap(**kwargs) -> ObservedSnapshot:
    return ObservedSnapshot(observed_at=NOW_STR, **kwargs)


def _read(rel: str) -> str:
    return (_REPO_ROOT / rel).read_text(encoding="utf-8")


def _types(signals) -> List[str]:
    return [s.signal_type for s in signals]


# ──────────────────────────────────────────────────────────────────
# Vocabulary contract
# ──────────────────────────────────────────────────────────────────

def test_signal_type_vocabulary_is_exactly_ten():
    assert len(SIGNAL_TYPES) == 10
    expected = {
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
    }
    assert set(SIGNAL_TYPES) == expected


def test_severity_vocabulary_is_closed():
    assert SEVERITIES == (SEVERITY_LOW, SEVERITY_MEDIUM, SEVERITY_HIGH)


def test_subject_type_vocabulary_is_closed():
    assert "lead" in SUBJECT_TYPES
    assert "call" in SUBJECT_TYPES
    assert "booking" in SUBJECT_TYPES
    assert "callback" in SUBJECT_TYPES
    assert "pipeline" in SUBJECT_TYPES


# ──────────────────────────────────────────────────────────────────
# Clean pipeline => no signals
# ──────────────────────────────────────────────────────────────────

def test_clean_pipeline_emits_zero_signals():
    leads = (
        ObservedLead(
            lead_ref="L-clean-1",
            created_at="2026-05-23T13:59:30Z",
            first_response_at="2026-05-23T13:59:45Z",
            last_activity_at="2026-05-23T13:59:55Z",
            assigned_agent_ref="A-1",
            source="zillow",
        ),
    )
    callbacks = (
        ObservedCallback(
            callback_ref="K-clean-1",
            lead_ref="L-clean-1",
            requested_at="2026-05-23T13:00:00Z",
            scheduled_at="2026-05-23T15:00:00Z",
            state="pending",
        ),
    )
    bookings = (
        ObservedBooking(
            booking_ref="B-clean-1",
            lead_ref="L-clean-1",
            proposed_at="2026-05-25T15:00:00Z",
            confirmation_state="confirmed",
        ),
    )
    agents = (ObservedAgent(agent_ref="A-1", available=True),)
    digest = observe(_snap(
        leads=leads, callbacks=callbacks, bookings=bookings, agents=agents,
    ))
    assert digest.signals == ()
    assert digest.counts_by_severity[SEVERITY_HIGH] == 0
    assert digest.counts_by_severity[SEVERITY_MEDIUM] == 0
    assert digest.counts_by_severity[SEVERITY_LOW] == 0


# ──────────────────────────────────────────────────────────────────
# Per-rule detection
# ──────────────────────────────────────────────────────────────────

def test_detects_overdue_callbacks():
    callbacks = (
        ObservedCallback(
            callback_ref="K-late",
            lead_ref="L-1",
            requested_at="2026-05-23T12:00:00Z",
            scheduled_at="2026-05-23T13:00:00Z",  # 60 min late at NOW
            state="pending",
        ),
        # On-time, future schedule => no signal.
        ObservedCallback(
            callback_ref="K-future",
            lead_ref="L-2",
            requested_at="2026-05-23T13:55:00Z",
            scheduled_at="2026-05-23T15:00:00Z",
            state="pending",
        ),
    )
    digest = observe(_snap(callbacks=callbacks))
    types = _types(digest.signals)
    assert SIGNAL_CALLBACK_OVERDUE in types
    assert types.count(SIGNAL_CALLBACK_OVERDUE) == 1


def test_detects_unassigned_leads():
    leads = (
        # Brand-new and unassigned => grace window; NOT flagged.
        ObservedLead(
            lead_ref="L-fresh",
            created_at="2026-05-23T13:59:50Z",
        ),
        # Older unassigned => flagged.
        ObservedLead(
            lead_ref="L-waiting",
            created_at="2026-05-23T13:30:00Z",
        ),
    )
    digest = observe(_snap(leads=leads))
    by_subj = {(s.signal_type, s.subject_ref) for s in digest.signals}
    assert (SIGNAL_LEAD_UNASSIGNED, "L-waiting") in by_subj
    assert (SIGNAL_LEAD_UNASSIGNED, "L-fresh") not in by_subj


def test_detects_stale_leads():
    leads = (
        ObservedLead(
            lead_ref="L-stale",
            created_at="2026-05-20T00:00:00Z",
            first_response_at="2026-05-20T00:01:00Z",
            last_activity_at="2026-05-20T01:00:00Z",
            assigned_agent_ref="A-1",
        ),
    )
    digest = observe(_snap(leads=leads))
    assert SIGNAL_STALE_LEAD in _types(digest.signals)


def test_detects_failed_booking_confirmation():
    bookings = (
        ObservedBooking(
            booking_ref="B-fail",
            lead_ref="L-1",
            proposed_at="2026-05-24T16:00:00Z",
            confirmation_state="failed",
        ),
    )
    digest = observe(_snap(bookings=bookings))
    assert SIGNAL_FAILED_BOOKING_CONFIRMATION in _types(digest.signals)


def test_detects_no_agent_available():
    leads = (
        ObservedLead(lead_ref="L-wait", created_at="2026-05-23T13:50:00Z"),
    )
    agents = (
        ObservedAgent(agent_ref="A-1", available=False),
        ObservedAgent(agent_ref="A-2", available=False),
    )
    digest = observe(_snap(leads=leads, agents=agents))
    assert SIGNAL_NO_AGENT_AVAILABLE in _types(digest.signals)


def test_no_agent_signal_quiet_when_someone_available():
    leads = (
        ObservedLead(lead_ref="L-wait", created_at="2026-05-23T13:50:00Z"),
    )
    agents = (
        ObservedAgent(agent_ref="A-1", available=False),
        ObservedAgent(agent_ref="A-2", available=True),
    )
    digest = observe(_snap(leads=leads, agents=agents))
    assert SIGNAL_NO_AGENT_AVAILABLE not in _types(digest.signals)


def test_detects_repeated_failed_calls():
    calls = tuple(
        ObservedCall(
            call_ref=f"C-{i}",
            lead_ref="L-1",
            started_at=f"2026-05-23T12:{i:02d}:00Z",
            outcome="failed",
            attempt_index=i,
        )
        for i in range(1, REPEATED_FAILED_CALL_THRESHOLD + 1)
    )
    digest = observe(_snap(calls=calls))
    assert SIGNAL_REPEATED_FAILED_CALLS in _types(digest.signals)


def test_repeated_failed_calls_under_threshold_is_quiet():
    calls = tuple(
        ObservedCall(
            call_ref=f"C-{i}",
            lead_ref="L-1",
            started_at=f"2026-05-23T12:{i:02d}:00Z",
            outcome="failed",
            attempt_index=i,
        )
        for i in range(1, REPEATED_FAILED_CALL_THRESHOLD)  # one short
    )
    digest = observe(_snap(calls=calls))
    assert SIGNAL_REPEATED_FAILED_CALLS not in _types(digest.signals)


def test_detects_missed_first_response():
    leads = (
        ObservedLead(
            lead_ref="L-late",
            created_at="2026-05-23T13:40:00Z",  # > 5 min ago, no first response
            assigned_agent_ref="A-1",
        ),
    )
    digest = observe(_snap(leads=leads))
    assert SIGNAL_MISSED_FIRST_RESPONSE in _types(digest.signals)


def test_detects_after_hours_lead_pending():
    leads = (
        ObservedLead(
            lead_ref="L-night",
            created_at="2026-05-23T02:00:00Z",
            assigned_agent_ref="A-1",
            after_hours=True,
        ),
    )
    digest = observe(_snap(leads=leads))
    assert SIGNAL_AFTER_HOURS_LEAD_PENDING in _types(digest.signals)


def test_detects_high_value_lead_waiting():
    leads = (
        ObservedLead(
            lead_ref="L-VIP",
            created_at="2026-05-23T13:55:00Z",
            assigned_agent_ref="A-1",
            value_tier="high",
        ),
    )
    digest = observe(_snap(leads=leads))
    assert SIGNAL_HIGH_VALUE_LEAD_WAITING in _types(digest.signals)


def test_detects_needs_human_review():
    leads = (
        ObservedLead(
            lead_ref="L-review",
            created_at="2026-05-23T13:00:00Z",
            first_response_at="2026-05-23T13:01:00Z",
            assigned_agent_ref="A-1",
            needs_human_review=True,
        ),
    )
    digest = observe(_snap(leads=leads))
    assert SIGNAL_NEEDS_HUMAN_REVIEW in _types(digest.signals)


# ──────────────────────────────────────────────────────────────────
# Determinism
# ──────────────────────────────────────────────────────────────────

def _busy_snapshot() -> ObservedSnapshot:
    leads = (
        ObservedLead(lead_ref="L-1", created_at="2026-05-23T13:40:00Z",
                     assigned_agent_ref="A-1"),
        ObservedLead(lead_ref="L-2", created_at="2026-05-23T13:35:00Z"),
        ObservedLead(lead_ref="L-vip", created_at="2026-05-23T13:55:00Z",
                     assigned_agent_ref="A-2", value_tier="high"),
    )
    bookings = (
        ObservedBooking(booking_ref="B-1", lead_ref="L-1",
                        proposed_at="2026-05-24T15:00:00Z",
                        confirmation_state="failed"),
    )
    callbacks = (
        ObservedCallback(callback_ref="K-1", lead_ref="L-1",
                         requested_at="2026-05-23T12:00:00Z",
                         scheduled_at="2026-05-23T13:00:00Z",
                         state="pending"),
    )
    agents = (
        ObservedAgent(agent_ref="A-1", available=True),
        ObservedAgent(agent_ref="A-2", available=True),
    )
    return ObservedSnapshot(
        observed_at=NOW_STR,
        leads=leads, bookings=bookings, callbacks=callbacks, agents=agents,
    )


def test_digest_is_deterministic():
    d1 = observe(_busy_snapshot())
    d2 = observe(_busy_snapshot())
    assert d1.digest_id == d2.digest_id
    assert [s.signal_id for s in d1.signals] == [s.signal_id for s in d2.signals]
    assert json.dumps(to_machine_json(d1), sort_keys=True) == \
           json.dumps(to_machine_json(d2), sort_keys=True)


def test_signals_sorted_severity_then_type():
    digest = observe(_busy_snapshot())
    # Severity ranks: high=0, medium=1, low=2 — non-decreasing.
    sev_rank = {SEVERITY_HIGH: 0, SEVERITY_MEDIUM: 1, SEVERITY_LOW: 2}
    ranks = [sev_rank[s.severity] for s in digest.signals]
    assert ranks == sorted(ranks)


def test_every_signal_has_live_behavior_changed_false():
    digest = observe(_busy_snapshot())
    assert digest.signals  # this fixture is supposed to emit > 0
    for s in digest.signals:
        assert s.live_behavior_changed is False
    assert digest.live_behavior_changed is False


def test_digest_carries_simulation_only_phase():
    digest = observe(_busy_snapshot())
    assert digest.phase == "PAS205"
    assert digest.allowed_environment == "SIMULATION_ONLY"


# ──────────────────────────────────────────────────────────────────
# Human renderers
# ──────────────────────────────────────────────────────────────────

def test_slack_summary_clean_state_is_friendly():
    digest = observe(_snap())
    text = to_slack_summary(digest)
    assert "nothing needs attention" in text.lower()
    for token in FORBIDDEN_OUTPUT_TOKENS:
        assert token not in text


def test_slack_summary_busy_state_uses_natural_language():
    digest = observe(_busy_snapshot())
    text = to_slack_summary(digest)
    assert len(text) > 30
    for token in FORBIDDEN_OUTPUT_TOKENS:
        assert token not in text


def test_broker_report_uses_natural_language():
    digest = observe(_busy_snapshot())
    report = to_broker_report(digest)
    assert "pipeline" in report.lower()
    for token in FORBIDDEN_OUTPUT_TOKENS:
        assert token not in report


def test_machine_json_contains_required_fields():
    digest = observe(_busy_snapshot())
    obj = to_machine_json(digest)
    assert obj["phase"] == "PAS205"
    assert obj["allowed_environment"] == "SIMULATION_ONLY"
    assert obj["live_behavior_changed"] is False
    assert "signals" in obj and isinstance(obj["signals"], list)
    for s in obj["signals"]:
        for key in (
            "signal_id", "signal_type", "severity", "subject_type",
            "subject_ref", "reason", "recommended_next_step",
            "evidence", "created_at", "live_behavior_changed",
        ):
            assert key in s
        assert s["signal_type"] in SIGNAL_TYPES
        assert s["severity"] in SEVERITIES
        assert s["live_behavior_changed"] is False


# ──────────────────────────────────────────────────────────────────
# Read-only / no-mutation contract
# ──────────────────────────────────────────────────────────────────

BANNED_IMPORT_MODULES: Tuple[str, ...] = (
    "twilio",
    "slack_sdk",
    "openai",
    "anthropic",
    "dotenv",
    "supabase",
)


BANNED_IMPORT_PREFIXES: Tuple[str, ...] = (
    "twilio.",
    "slack_sdk.",
    "openai.",
    "anthropic.",
    "dotenv.",
    "supabase.",
    "app.engine",
    "app.services.notifications",
    "app.services.outbound",
    "app.services.worker",
    "app.routes",
    "app.services.slack.slack_client",
    "app.services.slack.slack_sender",
    "app.services.notifications.sms_client",
    "app.services.notifications.email_client",
    "app.services.notifications.slack_client",
    "app.services.notifications.slack_sender",
)


FORBIDDEN_IDENTIFIERS: Tuple[str, ...] = (
    "apply_recommendation",
    "deploy_strategy",
    "switch_strategy_live",
    "auto_apply",
    "auto_promote",
    "force_promote",
    "live_apply",
    "auto_deploy",
    "route_lead_live",
    "route_call_live",
    "send_real_sms",
    "send_real_call",
    "send_slack_message",
    "post_to_slack",
    "place_call",
    "outbound_call",
)


# Disallowed I/O / mutation call names — anywhere in the
# production surface. We don't want PAS205 to grow a writer.
BANNED_CALL_NAMES: Tuple[str, ...] = (
    "load_dotenv",
    "get_supabase",
)


def _imports_calls_names(src: str) -> Tuple[set, set, set]:
    imports, calls, names = set(), set(), set()
    try:
        tree = ast.parse(src)
    except Exception:
        return imports, calls, names
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module)
                for alias in node.names:
                    imports.add(f"{node.module}.{alias.name}")
        elif isinstance(node, ast.Call):
            f = node.func
            if isinstance(f, ast.Name):
                calls.add(f.id)
            elif isinstance(f, ast.Attribute):
                calls.add(f.attr)
        if isinstance(node, ast.FunctionDef):
            names.add(node.name)
        elif isinstance(node, ast.AsyncFunctionDef):
            names.add(node.name)
        elif isinstance(node, ast.Name):
            names.add(node.id)
        elif isinstance(node, ast.Attribute):
            names.add(node.attr)
    return imports, calls, names


@pytest.mark.parametrize("rel", PRODUCTION_FILES)
def test_production_files_have_no_banned_imports(rel: str):
    src = _read(rel)
    imports, calls, _ = _imports_calls_names(src)
    bad: List[str] = []
    for mod in imports:
        if mod in BANNED_IMPORT_MODULES:
            bad.append(mod)
            continue
        for pref in BANNED_IMPORT_PREFIXES:
            if mod == pref or mod.startswith(pref + ".") or mod.startswith(pref):
                bad.append(mod)
                break
    for name in calls:
        if name in BANNED_CALL_NAMES:
            bad.append(f"call:{name}")
    assert not bad, f"{rel} has banned imports/calls: {sorted(set(bad))}"


@pytest.mark.parametrize("rel", PRODUCTION_FILES)
def test_production_files_have_no_forbidden_identifiers(rel: str):
    src = _read(rel)
    _, _, names = _imports_calls_names(src)
    bad = sorted(n for n in FORBIDDEN_IDENTIFIERS if n in names)
    assert not bad, f"{rel} declares forbidden identifiers: {bad}"


@pytest.mark.parametrize("rel", PRODUCTION_FILES)
def test_production_files_do_not_write_or_open_files(rel: str):
    src = _read(rel)
    # No `open(`, no `.write_text(`, no `.write(` in the observer core.
    # (The runner script is allowed to write reports — these checks
    # only cover observer_models, observer, observer_digest.)
    forbidden_io = ("open(", ".write_text(", ".write(", ".unlink(", ".mkdir(")
    bad = [tok for tok in forbidden_io if tok in src]
    assert not bad, f"{rel} contains forbidden I/O calls: {bad}"


def test_no_combined_supabase_migration_committed():
    fp = _REPO_ROOT / "scripts" / "combined_supabase_migration.sql"
    assert not fp.is_file()


def test_no_new_pas205_migration():
    bad = []
    scripts = _REPO_ROOT / "scripts"
    for child in scripts.iterdir():
        name = child.name.lower()
        if "pas205" in name and (name.endswith(".sql") or "migrate" in name):
            bad.append(child.name)
    assert not bad, f"PAS205 must not introduce migrations: {bad}"
