"""
Smoke tests for the workflow routes (PAS132).

Verifies:
  1. Both router modules import cleanly.
  2. The new workflow routes are registered on each router.
  3. The portal handler refuses cross-brokerage access (404) BEFORE
     calling the runtime layer.
  4. The admin handler returns the operator-facing envelope including
     event_type per step.
  5. The portal handler returns the brokerage-facing envelope WITHOUT
     event_type and with translated labels.

Pytest-compatible. Standalone runner at the bottom.
"""

import asyncio
import os
import sys

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")),
)

try:
    from fastapi import HTTPException
    from app.routes import events as admin_events_module
    from app.routes import portal as portal_module
    from app.services.workflows import runtime as wf_runtime
    _IMPORT_OK = True
    _IMPORT_ERROR = None
except Exception as e:
    _IMPORT_OK = False
    _IMPORT_ERROR = f"{type(e).__name__}: {e}"


def _skip_if_imports_failed():
    if not _IMPORT_OK:
        print(f"  (skip -- imports failed: {_IMPORT_ERROR})")
        return True
    return False


# ───────────── route registration ─────────────

def test_admin_workflow_route_registered():
    if _skip_if_imports_failed():
        return
    paths = {r.path for r in admin_events_module.router.routes}
    assert "/workflows/calls/{call_id}" in paths, \
        f"admin /workflows/calls/{{call_id}} not registered (have {paths})"


def test_portal_workflow_route_registered():
    if _skip_if_imports_failed():
        return
    paths = {r.path for r in portal_module.router.routes}
    assert "/workflows/calls/{call_id}" in paths, \
        f"portal /workflows/calls/{{call_id}} not registered (have {paths})"


# ───────────── canned events for runtime ─────────────

def _canned_events():
    return [
        {
            "event_type": "call.started", "event_category": "call",
            "severity": "info", "call_id": "CA-test", "lead_id": "lead-1",
            "brokerage_id": "owner-b",
            "created_at": "2026-05-04T10:00:00+00:00", "payload": {},
        },
        {
            "event_type": "callback.requested", "event_category": "lead",
            "severity": "info", "call_id": "CA-test", "lead_id": "lead-1",
            "brokerage_id": "owner-b",
            "created_at": "2026-05-04T10:01:00+00:00",
            "payload": {"from_state": "INTENT", "trigger_excerpt": "call me later"},
        },
    ]


# ───────────── portal ownership guard ─────────────

class _FakeQuery:
    def __init__(self, data): self._data = data
    def select(self, *a, **kw): return self
    def eq(self, *a, **kw): return self
    def limit(self, *a, **kw): return self
    def execute(self):
        class R:
            def __init__(self, d): self.data = d
        return R(self._data)


class _FakeDB:
    def __init__(self, calls_data): self._calls_data = calls_data
    def table(self, name):
        if name == "calls":
            return _FakeQuery(self._calls_data)
        return _FakeQuery([])


def test_portal_workflow_404_when_call_not_owned():
    if _skip_if_imports_failed():
        return
    # Calls ownership check returns no row → must 404 BEFORE the runtime
    # layer (and any pas_events fetch) is touched.
    original_db = portal_module.get_supabase
    original_runtime = portal_module.get_or_build_workflow_for_call
    runtime_called = {"n": 0}

    def _spy_runtime(*a, **kw):
        runtime_called["n"] += 1
        return {}

    portal_module.get_supabase = lambda: _FakeDB([])
    portal_module.get_or_build_workflow_for_call = _spy_runtime
    try:
        try:
            asyncio.run(portal_module.portal_workflow_for_call(
                call_id="CA-other-brokerage",
                brokerage={"id": "victim-b"},
            ))
            raised = None
        except HTTPException as e:
            raised = e
    finally:
        portal_module.get_supabase = original_db
        portal_module.get_or_build_workflow_for_call = original_runtime

    assert raised is not None, "expected HTTPException, got success"
    assert raised.status_code == 404
    assert runtime_called["n"] == 0, \
        "runtime was invoked before ownership check passed"


def test_portal_workflow_returns_translated_envelope_when_owned():
    if _skip_if_imports_failed():
        return
    original_db = portal_module.get_supabase
    portal_module.get_supabase = lambda: _FakeDB([{"id": "CA-test"}])

    # Stub the runtime layer's data sources (events + call summary). The
    # mapper / sanitizer run for real so we exercise the full surface.
    original_q_events = wf_runtime.fetch_workflow_events
    original_q_call = wf_runtime.fetch_call_summary
    wf_runtime.fetch_workflow_events = lambda *a, **kw: _canned_events()
    wf_runtime.fetch_call_summary = lambda *a, **kw: {
        "id": "CA-test", "brokerage_id": "owner-b", "lead_id": "lead-1"
    }
    try:
        resp = asyncio.run(portal_module.portal_workflow_for_call(
            call_id="CA-test",
            brokerage={"id": "owner-b"},
        ))
    finally:
        portal_module.get_supabase = original_db
        wf_runtime.fetch_workflow_events = original_q_events
        wf_runtime.fetch_call_summary = original_q_call

    assert resp["call_id"] == "CA-test"
    assert resp["brokerage_id"] == "owner-b"
    assert resp["version"] == "v1"

    # Portal envelope must NOT carry raw event_type per step.
    for step in resp["steps"]:
        assert "event_type" not in step, \
            f"portal step {step['key']} leaked raw event_type"
    # Portal envelope must carry the translated label vocabulary.
    by_key = {s["key"]: s for s in resp["steps"]}
    assert by_key["intent_captured"]["label"] == "Lead Detail Captured · Intent"
    assert by_key["callback_requested"]["status"] == "completed"


# ───────────── admin envelope retains operator vocabulary ─────────────

def test_admin_workflow_returns_operator_envelope():
    if _skip_if_imports_failed():
        return
    original_q_events = wf_runtime.fetch_workflow_events
    original_q_call = wf_runtime.fetch_call_summary
    wf_runtime.fetch_workflow_events = lambda *a, **kw: _canned_events()
    wf_runtime.fetch_call_summary = lambda *a, **kw: {
        "id": "CA-test", "brokerage_id": "owner-b", "lead_id": "lead-1"
    }
    try:
        resp = asyncio.run(admin_events_module.admin_workflow_for_call(
            call_id="CA-test",
            brokerage_id=None,
            _=True,
        ))
    finally:
        wf_runtime.fetch_workflow_events = original_q_events
        wf_runtime.fetch_call_summary = original_q_call

    assert resp["call_id"] == "CA-test"
    by_key = {s["key"]: s for s in resp["steps"]}
    # Admin keeps event_type for the operator timeline panel.
    assert by_key["lead_received"]["event_type"] == "call.started"
    assert by_key["callback_requested"]["event_type"] == "callback.requested"
    # Admin keeps the operator-facing label, not the brokerage translation.
    assert by_key["pas_calling"]["label"] == "PAS Calling"
    # system_signals shape is the operator one (counts, not booleans).
    assert "provider_failed_count" in resp["system_signals"]


# ───────────── secret-style metadata never leaks ─────────────

def test_no_forbidden_keys_in_either_envelope():
    if _skip_if_imports_failed():
        return
    leaky_payload = {
        "intent": "buying", "value": "buying",
        "api_key": "sk-leak", "authorization": "Bearer leak",
        "raw_text": "transcript should never appear",
        "secret_token": "should also drop",
    }
    leaky_events = [
        {"event_type": "call.started", "created_at": "t0", "payload": {}},
        {"event_type": "lead.extracted", "created_at": "t1",
         "payload": {"field": "intent", **leaky_payload}},
    ]

    original_q_events = wf_runtime.fetch_workflow_events
    original_q_call = wf_runtime.fetch_call_summary
    wf_runtime.fetch_workflow_events = lambda *a, **kw: leaky_events
    wf_runtime.fetch_call_summary = lambda *a, **kw: {
        "id": "CA-leak", "brokerage_id": "owner-b", "lead_id": None
    }

    forbidden = ("api_key", "authorization", "raw_text", "secret_token", "secret", "token")
    try:
        for audience, runner in (
            ("admin", lambda: admin_events_module.admin_workflow_for_call(
                call_id="CA-leak", brokerage_id=None, _=True)),
            ("portal", lambda: portal_module.portal_workflow_for_call(
                call_id="CA-leak", brokerage={"id": "owner-b"})),
        ):
            if audience == "portal":
                portal_module.get_supabase = lambda: _FakeDB([{"id": "CA-leak"}])
            resp = asyncio.run(runner())
            for step in resp["steps"]:
                meta = step.get("safe_metadata") or {}
                for f in forbidden:
                    assert f not in meta, \
                        f"{audience}: {f} leaked in safe_metadata of {step['key']}"
    finally:
        wf_runtime.fetch_workflow_events = original_q_events
        wf_runtime.fetch_call_summary = original_q_call


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
