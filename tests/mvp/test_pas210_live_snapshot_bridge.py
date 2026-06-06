"""PAS210 — Live Operational Snapshot Bridge tests (narrow, read-only).

Covers: default-demo behaviour, flag-enabled live path, brokerage_id required,
fail-closed on missing tenant, safe adapter-failure handling, no silent
demo/live mixing, source-mode transparency, and demo-behaviour preservation.
"""
import importlib

import pytest

bridge = importlib.import_module("app.services.proactive.live_snapshot_bridge")
from app.services.slack.proactive_digest_intent import (  # noqa: E402
    try_route_needs_attention,
)

FLAG = bridge.LIVE_SNAPSHOT_FLAG
ATTENTION_TEXT = "what needs attention"
NON_MATCH_TEXT = "next steps"  # PAS191-owned, must not match PAS207


# ── stub Supabase client (read-only chainable, returns empty rows) ──
class _FakeResp:
    data: list = []


class _FakeQuery:
    def select(self, *a, **k):
        return self

    def eq(self, *a, **k):
        return self

    def limit(self, *a, **k):
        return self

    def order(self, *a, **k):
        return self

    def execute(self):
        return _FakeResp()


class _FakeClient:
    def table(self, name):
        return _FakeQuery()


@pytest.fixture(autouse=True)
def _clear_flag(monkeypatch):
    monkeypatch.delenv(FLAG, raising=False)
    yield


# 1. Default behavior remains demo (flag unset).
def test_default_behaviour_is_demo():
    res = bridge.build_needs_attention_bridge(ATTENTION_TEXT, brokerage_id="brk-1")
    assert res is not None
    assert res.source_mode == bridge.SOURCE_MODE_DEMO


# 8. Existing demo behavior preserved byte-for-byte when flag is off.
def test_demo_text_identical_to_legacy_path():
    res = bridge.build_needs_attention_bridge(ATTENTION_TEXT, brokerage_id="brk-1")
    legacy = try_route_needs_attention(ATTENTION_TEXT)
    assert res.text == legacy


# Non-matching text falls through unchanged (returns None).
def test_non_matching_text_returns_none():
    assert bridge.build_needs_attention_bridge(NON_MATCH_TEXT, brokerage_id="brk-1") is None


# 2. Flag enabled uses live adapter (tenant present, client ok).
def test_flag_enabled_uses_live(monkeypatch):
    monkeypatch.setenv(FLAG, "true")
    res = bridge.build_needs_attention_bridge(
        ATTENTION_TEXT, brokerage_id="brk-live", client_factory=lambda: _FakeClient()
    )
    assert res.source_mode == bridge.SOURCE_MODE_LIVE
    assert res.available is True
    assert "live operational data" in res.text
    assert "brk-live" in res.text


# 3 + 4. brokerage_id required; missing → fail closed (unavailable, no data).
def test_missing_brokerage_fails_closed(monkeypatch):
    monkeypatch.setenv(FLAG, "true")
    res = bridge.build_needs_attention_bridge(
        ATTENTION_TEXT, brokerage_id=None, client_factory=lambda: _FakeClient()
    )
    assert res.source_mode == bridge.SOURCE_MODE_UNAVAILABLE
    assert res.available is False
    # resolve_snapshot fails closed before any read.
    resolution = bridge.resolve_snapshot(None, client_factory=lambda: _FakeClient())
    assert resolution.snapshot is None
    assert resolution.detail == "brokerage_id_required"


def test_blank_brokerage_also_fails_closed(monkeypatch):
    monkeypatch.setenv(FLAG, "true")
    res = bridge.build_needs_attention_bridge(
        ATTENTION_TEXT, brokerage_id="   ", client_factory=lambda: _FakeClient()
    )
    assert res.source_mode == bridge.SOURCE_MODE_UNAVAILABLE
    assert res.available is False


# 5. Adapter failure handled safely (no crash, unavailable, no demo fallback).
def test_adapter_failure_is_unavailable_not_demo(monkeypatch):
    monkeypatch.setenv(FLAG, "true")

    def _boom():
        raise RuntimeError("supabase down")

    res = bridge.build_needs_attention_bridge(
        ATTENTION_TEXT, brokerage_id="brk-x", client_factory=_boom
    )
    assert res.source_mode == bridge.SOURCE_MODE_UNAVAILABLE
    assert res.available is False
    # Must NOT be the demo output.
    assert res.text != try_route_needs_attention(ATTENTION_TEXT)


# 6. No silent mixing: unavailable text carries no demo content + explicit label.
def test_no_silent_mixing_on_unavailable(monkeypatch):
    monkeypatch.setenv(FLAG, "true")
    res = bridge.build_needs_attention_bridge(
        ATTENTION_TEXT, brokerage_id=None, client_factory=lambda: _FakeClient()
    )
    assert "source: unavailable" in res.text.lower()
    # demo digest never mentions "unavailable"; ensure we didn't blend.
    assert res.text != try_route_needs_attention(ATTENTION_TEXT)


# 7. Source mode is always exposed (transparency) across all modes.
def test_source_mode_always_present(monkeypatch):
    # demo
    r_demo = bridge.build_needs_attention_bridge(ATTENTION_TEXT, brokerage_id="b")
    # live
    monkeypatch.setenv(FLAG, "true")
    r_live = bridge.build_needs_attention_bridge(
        ATTENTION_TEXT, brokerage_id="b", client_factory=lambda: _FakeClient()
    )
    # unavailable
    r_unavail = bridge.build_needs_attention_bridge(ATTENTION_TEXT, brokerage_id=None)
    assert {r_demo.source_mode, r_live.source_mode, r_unavail.source_mode} == {
        bridge.SOURCE_MODE_DEMO,
        bridge.SOURCE_MODE_LIVE,
        bridge.SOURCE_MODE_UNAVAILABLE,
    }


# Flag must be the literal "true" — other truthy strings stay demo.
def test_flag_must_be_literal_true(monkeypatch):
    monkeypatch.setenv(FLAG, "1")
    assert bridge.live_snapshot_enabled() is False
    res = bridge.build_needs_attention_bridge(ATTENTION_TEXT, brokerage_id="b")
    assert res.source_mode == bridge.SOURCE_MODE_DEMO


# Live read is tenant-scoped: the brokerage_id reaches the adapter unchanged.
def test_live_read_is_tenant_scoped(monkeypatch):
    monkeypatch.setenv(FLAG, "true")
    seen = {}

    class _Capture(_FakeQuery):
        def eq(self, col, val):
            if col == "brokerage_id":
                seen["brokerage_id"] = val
            return self

    class _CaptureClient:
        def table(self, name):
            return _Capture()

    res = bridge.resolve_snapshot("brk-scope-7", client_factory=lambda: _CaptureClient())
    assert res.source_mode == bridge.SOURCE_MODE_LIVE
    assert seen.get("brokerage_id") == "brk-scope-7"
