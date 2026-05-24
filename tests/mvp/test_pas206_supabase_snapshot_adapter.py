"""
PAS206 — Read-only Supabase snapshot adapter tests.

Coverage:

  * Adapter issues select-only queries (no insert/update/delete/upsert/rpc).
  * Missing optional table (callbacks) fails safely → status='unavailable'.
  * Missing required table (e.g. leads) also fails safely; the
    snapshot still loads and other sources populate.
  * Rows normalize correctly into PAS205 observer models.
  * Observer can consume the normalized snapshot without raising.
  * read_only=True invariant is preserved.
  * Source has no Twilio / Slack outbound / migration imports.
  * No mutation method names anywhere in the adapter source.
"""

from __future__ import annotations

import ast
import pathlib
import sys
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Tuple

import pytest


_REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))


from app.services.proactive.observer import observe  # noqa: E402
from app.services.proactive.observer_models import (  # noqa: E402
    ObservedAgent,
    ObservedBooking,
    ObservedCall,
    ObservedCallback,
    ObservedLead,
    ObservedSnapshot,
)
from app.services.proactive.supabase_snapshot_adapter import (  # noqa: E402
    ALLOWED_SOURCES,
    OPTIONAL_SOURCES,
    SOURCE_AGENTS,
    SOURCE_BOOKINGS,
    SOURCE_CALLBACKS,
    SOURCE_CALLS,
    SOURCE_LEADS,
    STATUS_EMPTY,
    STATUS_OK,
    STATUS_UNAVAILABLE,
    SupabaseSnapshotResult,
    load_snapshot,
)


# ──────────────────────────────────────────────────────────────────
# Fake Supabase client.
#
# Records every method invocation so the test suite can assert the
# adapter never calls anything outside the select/eq/limit/order/
# execute vocabulary.
# ──────────────────────────────────────────────────────────────────

class _Result:
    def __init__(self, rows: List[dict]) -> None:
        self.data = rows


class _Query:
    def __init__(self, recorder: "_Recorder", table: str, rows: List[dict]) -> None:
        self._recorder = recorder
        self._table = table
        self._rows = rows
        self._eq_filters: List[Tuple[str, Any]] = []
        self._limit: Optional[int] = None

    def select(self, cols: str = "*") -> "_Query":
        self._recorder.calls.append((self._table, "select", cols))
        return self

    def eq(self, col: str, val: Any) -> "_Query":
        self._recorder.calls.append((self._table, "eq", col, val))
        self._eq_filters.append((col, val))
        return self

    def limit(self, n: int) -> "_Query":
        self._recorder.calls.append((self._table, "limit", n))
        self._limit = int(n)
        return self

    def order(self, col: str, **kwargs: Any) -> "_Query":
        self._recorder.calls.append((self._table, "order", col))
        return self

    def execute(self) -> _Result:
        self._recorder.calls.append((self._table, "execute"))
        rows = self._rows
        if self._eq_filters:
            for col, val in self._eq_filters:
                rows = [r for r in rows if r.get(col) == val]
        if self._limit is not None:
            rows = rows[: self._limit]
        return _Result(list(rows))


class _MissingTableQuery:
    def __init__(self, recorder: "_Recorder", table: str) -> None:
        self._recorder = recorder
        self._table = table

    def select(self, cols: str = "*") -> "_MissingTableQuery":
        self._recorder.calls.append((self._table, "select_missing", cols))
        raise RuntimeError(f"relation '{self._table}' does not exist")


class _Recorder:
    def __init__(self) -> None:
        self.calls: List[tuple] = []


class FakeSupabase:
    def __init__(self, dataset: Dict[str, Optional[List[dict]]]) -> None:
        self._dataset = dataset
        self.recorder = _Recorder()

    def table(self, name: str):
        rows = self._dataset.get(name, None)
        if rows is None:
            return _MissingTableQuery(self.recorder, name)
        return _Query(self.recorder, name, list(rows))


# ──────────────────────────────────────────────────────────────────
# Fixture data.
# ──────────────────────────────────────────────────────────────────

BROKERAGE = "demo-brokerage"

LEAD_ROWS = [
    {
        "id": "L-1",
        "brokerage_id": BROKERAGE,
        "phone_number": "+15550001",
        "created_at": "2026-05-24T01:00:00Z",
        "updated_at": "2026-05-24T01:00:00Z",
        "first_response_at": None,
        "last_activity_at": "2026-05-24T01:00:00Z",
        "assigned_agent_id": None,
        "source": "web",
        "value_tier": "high",
        "after_hours": False,
        "needs_human_review": False,
    },
    {
        "id": "L-2",
        "brokerage_id": BROKERAGE,
        "phone_number": "+15550002",
        "created_at": "2026-05-23T22:00:00Z",
        "updated_at": "2026-05-23T22:30:00Z",
        "first_response_at": "2026-05-23T22:15:00Z",
        "last_activity_at": "2026-05-23T22:30:00Z",
        "assigned_agent_id": "A-1",
        "source": "phone",
        "value_tier": "standard",
        "after_hours": True,
        "needs_human_review": False,
    },
    # Skipped lead — no created_at, normaliser should drop.
    {
        "id": "L-3",
        "brokerage_id": BROKERAGE,
        "phone_number": "+15550003",
    },
]

CALL_ROWS = [
    {
        "id": "C-1",
        "brokerage_id": BROKERAGE,
        "lead_id": "L-1",
        "start_time": "2026-05-24T01:05:00Z",
        "outcome": "failed",
        "attempt_index": 1,
    },
    {
        "id": "C-2",
        "brokerage_id": BROKERAGE,
        "lead_id": "L-1",
        "start_time": "2026-05-24T01:15:00Z",
        "outcome": "answered",
        "attempt_index": 2,
    },
]

BOOKING_ROWS = [
    {
        "id": "B-1",
        "brokerage_id": BROKERAGE,
        "lead_id": "L-2",
        "slot_time": "2026-05-25T15:00:00Z",
        "status": "failed",
        "updated_at": "2026-05-24T01:30:00Z",
    },
    {
        "id": "B-2",
        "brokerage_id": BROKERAGE,
        "lead_id": "L-1",
        "slot_time": "2026-05-25T16:00:00Z",
        "status": "scheduled",
        "updated_at": "2026-05-24T01:35:00Z",
    },
]

AGENT_ROWS = [
    {
        "id": "A-1",
        "brokerage_id": BROKERAGE,
        "status": "busy",
        "updated_at": "2026-05-24T01:00:00Z",
    },
    {
        "id": "A-2",
        "brokerage_id": BROKERAGE,
        "status": "available",
        "updated_at": "2026-05-24T00:30:00Z",
    },
]

CALLBACK_ROWS = [
    {
        "id": "K-1",
        "brokerage_id": BROKERAGE,
        "lead_id": "L-1",
        "requested_at": "2026-05-24T00:00:00Z",
        "scheduled_at": "2026-05-24T00:30:00Z",
        "status": "pending",
    },
]


def _full_dataset() -> Dict[str, List[dict]]:
    return {
        SOURCE_LEADS:     list(LEAD_ROWS),
        SOURCE_CALLS:     list(CALL_ROWS),
        SOURCE_BOOKINGS:  list(BOOKING_ROWS),
        SOURCE_AGENTS:    list(AGENT_ROWS),
        SOURCE_CALLBACKS: list(CALLBACK_ROWS),
    }


def _dataset_without(*excluded: str) -> Dict[str, Optional[List[dict]]]:
    base: Dict[str, Optional[List[dict]]] = _full_dataset()  # type: ignore[assignment]
    for name in excluded:
        base.pop(name, None)
    return base


# ──────────────────────────────────────────────────────────────────
# Tests.
# ──────────────────────────────────────────────────────────────────


def test_load_snapshot_returns_envelope_with_read_only_true() -> None:
    client = FakeSupabase(_full_dataset())
    result = load_snapshot(client, brokerage_id=BROKERAGE, loaded_at="2026-05-24T01:45:00Z")
    assert isinstance(result, SupabaseSnapshotResult)
    assert result.read_only is True
    assert result.brokerage_id == BROKERAGE
    assert result.loaded_at == "2026-05-24T01:45:00Z"


def test_load_snapshot_normalizes_leads() -> None:
    client = FakeSupabase(_full_dataset())
    result = load_snapshot(client, brokerage_id=BROKERAGE)
    leads = result.snapshot.leads
    assert all(isinstance(l, ObservedLead) for l in leads)
    refs = {l.lead_ref for l in leads}
    assert "L-1" in refs and "L-2" in refs
    # L-3 lacks created_at and must be dropped, not raise.
    assert "L-3" not in refs
    lead1 = next(l for l in leads if l.lead_ref == "L-1")
    assert lead1.first_response_at is None
    assert lead1.value_tier == "high"
    assert lead1.after_hours is False
    assert lead1.assigned_agent_ref is None
    lead2 = next(l for l in leads if l.lead_ref == "L-2")
    assert lead2.assigned_agent_ref == "A-1"
    assert lead2.after_hours is True


def test_load_snapshot_normalizes_calls_with_outcome_mapping() -> None:
    client = FakeSupabase(_full_dataset())
    result = load_snapshot(client, brokerage_id=BROKERAGE)
    calls = result.snapshot.calls
    assert all(isinstance(c, ObservedCall) for c in calls)
    by_ref = {c.call_ref: c for c in calls}
    assert by_ref["C-1"].outcome == "failed"
    assert by_ref["C-2"].outcome == "answered"
    assert by_ref["C-1"].attempt_index == 1
    assert by_ref["C-2"].attempt_index == 2


def test_load_snapshot_normalizes_bookings_with_state_mapping() -> None:
    client = FakeSupabase(_full_dataset())
    result = load_snapshot(client, brokerage_id=BROKERAGE)
    bookings = result.snapshot.bookings
    assert all(isinstance(b, ObservedBooking) for b in bookings)
    by_ref = {b.booking_ref: b for b in bookings}
    assert by_ref["B-1"].confirmation_state == "failed"
    assert by_ref["B-2"].confirmation_state == "pending"


def test_load_snapshot_normalizes_agents_availability() -> None:
    client = FakeSupabase(_full_dataset())
    result = load_snapshot(client, brokerage_id=BROKERAGE)
    agents = result.snapshot.agents
    by_ref = {a.agent_ref: a for a in agents}
    assert by_ref["A-1"].available is False
    assert by_ref["A-2"].available is True


def test_load_snapshot_normalizes_callbacks() -> None:
    client = FakeSupabase(_full_dataset())
    result = load_snapshot(client, brokerage_id=BROKERAGE)
    callbacks = result.snapshot.callbacks
    assert len(callbacks) == 1
    cb = callbacks[0]
    assert isinstance(cb, ObservedCallback)
    assert cb.callback_ref == "K-1"
    assert cb.state == "pending"


def test_missing_optional_callbacks_table_is_unavailable_not_fatal() -> None:
    client = FakeSupabase(_dataset_without(SOURCE_CALLBACKS))
    result = load_snapshot(client, brokerage_id=BROKERAGE)
    assert result.source_status[SOURCE_CALLBACKS] == STATUS_UNAVAILABLE
    assert SOURCE_CALLBACKS in result.unavailable_sources
    # Rest of the snapshot still loaded.
    assert len(result.snapshot.leads) >= 1
    assert len(result.snapshot.calls) >= 1


def test_missing_required_leads_table_does_not_raise() -> None:
    client = FakeSupabase(_dataset_without(SOURCE_LEADS))
    result = load_snapshot(client, brokerage_id=BROKERAGE)
    assert result.source_status[SOURCE_LEADS] == STATUS_UNAVAILABLE
    assert SOURCE_LEADS in result.unavailable_sources
    assert len(result.snapshot.leads) == 0
    # Other sources unaffected.
    assert len(result.snapshot.calls) >= 1


def test_empty_table_reports_empty_status() -> None:
    data = _full_dataset()
    data[SOURCE_BOOKINGS] = []
    client = FakeSupabase(data)
    result = load_snapshot(client, brokerage_id=BROKERAGE)
    assert result.source_status[SOURCE_BOOKINGS] == STATUS_EMPTY
    assert SOURCE_BOOKINGS not in result.unavailable_sources
    assert len(result.snapshot.bookings) == 0


def test_row_counts_match_normalized_lengths() -> None:
    client = FakeSupabase(_full_dataset())
    result = load_snapshot(client, brokerage_id=BROKERAGE)
    snap = result.snapshot
    assert result.row_counts[SOURCE_LEADS]     == len(snap.leads)
    assert result.row_counts[SOURCE_CALLS]     == len(snap.calls)
    assert result.row_counts[SOURCE_BOOKINGS]  == len(snap.bookings)
    assert result.row_counts[SOURCE_AGENTS]    == len(snap.agents)
    assert result.row_counts[SOURCE_CALLBACKS] == len(snap.callbacks)


def test_observer_consumes_loaded_snapshot_without_raising() -> None:
    client = FakeSupabase(_full_dataset())
    result = load_snapshot(
        client,
        brokerage_id=BROKERAGE,
        loaded_at="2026-05-24T02:00:00Z",
    )
    digest = observe(result.snapshot)
    assert digest.phase == "PAS205"
    assert digest.live_behavior_changed is False
    assert isinstance(digest.signals, tuple)


def test_brokerage_id_is_required() -> None:
    client = FakeSupabase(_full_dataset())
    with pytest.raises(ValueError):
        load_snapshot(client, brokerage_id="")


def test_adapter_only_calls_select_eq_limit_execute() -> None:
    client = FakeSupabase(_full_dataset())
    load_snapshot(client, brokerage_id=BROKERAGE)
    allowed_methods = {"select", "eq", "limit", "order", "execute", "select_missing"}
    methods_used = {call[1] for call in client.recorder.calls}
    forbidden = methods_used - allowed_methods
    assert not forbidden, f"adapter called forbidden methods: {forbidden}"


def test_adapter_scopes_every_query_by_brokerage_id() -> None:
    client = FakeSupabase(_full_dataset())
    load_snapshot(client, brokerage_id=BROKERAGE)
    eq_calls = [c for c in client.recorder.calls if c[1] == "eq"]
    # Every non-missing table should have an eq("brokerage_id", BROKERAGE).
    for c in eq_calls:
        _table, _verb, col, val = c
        assert col == "brokerage_id"
        assert val == BROKERAGE


# ──────────────────────────────────────────────────────────────────
# Source-level safety invariants.
# ──────────────────────────────────────────────────────────────────


ADAPTER_PATH = _REPO_ROOT / "app" / "services" / "proactive" / "supabase_snapshot_adapter.py"


def _adapter_source() -> str:
    return ADAPTER_PATH.read_text(encoding="utf-8")


def test_adapter_source_has_no_mutation_methods() -> None:
    src = _adapter_source()
    for forbidden in (
        ".insert(",
        ".update(",
        ".delete(",
        ".upsert(",
        ".rpc(",
    ):
        assert forbidden not in src, f"adapter source contains forbidden call '{forbidden}'"


def test_adapter_source_has_no_twilio_or_slack_outbound_imports() -> None:
    src = _adapter_source()
    tree = ast.parse(src)
    forbidden_modules = {
        "twilio",
        "slack_sdk",
        "slack",
        "openai",
        "anthropic",
        "smtplib",
        "email",
    }
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                root = alias.name.split(".")[0]
                assert root not in forbidden_modules, (
                    f"adapter imports forbidden module: {alias.name}"
                )
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                root = node.module.split(".")[0]
                assert root not in forbidden_modules, (
                    f"adapter imports forbidden module: {node.module}"
                )


def test_adapter_source_has_no_scheduler_or_worker_imports() -> None:
    src = _adapter_source()
    for forbidden in (
        "from apscheduler",
        "import apscheduler",
        "from celery",
        "import celery",
        "worker.start",
        "cron",
    ):
        assert forbidden not in src, f"adapter mentions scheduler/worker token '{forbidden}'"


def test_adapter_source_declares_read_only_invariant() -> None:
    src = _adapter_source()
    assert "read_only" in src
    assert "READ-ONLY" in src or "read-only" in src


def test_adapter_source_handles_missing_table_safely() -> None:
    src = _adapter_source()
    # _safe_select must broadly catch exceptions so a missing
    # table degrades to an unavailable source rather than raising.
    assert "except Exception" in src
    assert "STATUS_UNAVAILABLE" in src


def test_adapter_does_not_touch_combined_supabase_migration() -> None:
    src = _adapter_source()
    assert "combined_supabase_migration" not in src


def test_allowed_sources_vocabulary_is_closed_and_stable() -> None:
    assert ALLOWED_SOURCES == (
        SOURCE_LEADS,
        SOURCE_CALLS,
        SOURCE_BOOKINGS,
        SOURCE_AGENTS,
        SOURCE_CALLBACKS,
    )
    assert SOURCE_CALLBACKS in OPTIONAL_SOURCES


def test_loaded_at_defaults_to_current_utc_when_omitted() -> None:
    client = FakeSupabase(_full_dataset())
    before = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    result = load_snapshot(client, brokerage_id=BROKERAGE)
    after = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    assert before <= result.loaded_at <= after
    assert result.snapshot.observed_at == result.loaded_at
