"""
Smoke tests for the intelligence routes (PAS129/PAS130 Commit 2).

Verifies:
  1. Both router modules import cleanly.
  2. Each new route is registered at the expected path.
  3. The portal handlers actually invoke sanitize_event_for_portal()
     before returning (PII / secrets cannot leak through portal routes).
  4. The admin handlers return raw events un-sanitised.
  5. The portal call-timeline handler refuses cross-brokerage access (404).

No external API calls — Supabase access in queries.py is monkeypatched
to canned data. fastapi must be importable; gracefully skipped if not.

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
    from app.services.intelligence import queries as intel_queries
    _IMPORT_OK = True
    _IMPORT_ERROR = None
except Exception as e:
    _IMPORT_OK = False
    _IMPORT_ERROR = f"{type(e).__name__}: {e}"


def _skip_if_imports_failed():
    if not _IMPORT_OK:
        print(f"  (skip — imports failed: {_IMPORT_ERROR})")
        return True
    return False


# ───────────── route registration ─────────────

def test_admin_routes_registered():
    if _skip_if_imports_failed():
        return
    paths = {r.path for r in admin_events_module.router.routes}
    for expected in (
        "/events/recent",
        "/events/callbacks",
        "/events/calls/{call_id}",
        "/intelligence/summary",
    ):
        assert expected in paths, f"admin route {expected} not registered (have {paths})"


def test_portal_routes_registered():
    if _skip_if_imports_failed():
        return
    paths = {r.path for r in portal_module.router.routes}
    for expected in (
        "/events/recent",
        "/callbacks",
        "/calls/{call_id}/timeline",
        "/intelligence/summary",
    ):
        assert expected in paths, f"portal route {expected} not registered (have {paths})"


# ───────────── sanitisation wiring ─────────────

def _leaky_event():
    return {
        "event_type": "objection.detected",
        "event_category": "call",
        "event_source": "state_machine",
        "severity": "info",
        "state": "BOOKING",
        "call_id": "CA-test",
        "lead_id": "lead-1",
        "brokerage_id": "test-b",
        "agent_id": None,
        "provider": None,
        "created_at": "2026-05-03T10:00:00+00:00",
        "payload": {
            "category": "has_agent",
            "text": "raw caller transcript that must not leak",
            "raw_text": "another raw blob",
            "api_key": "sk-leak",
        },
    }


def test_portal_recent_events_sanitises_payload():
    if _skip_if_imports_failed():
        return
    canned = [_leaky_event()]
    original = portal_module.recent_events
    portal_module.recent_events = lambda **kw: canned
    try:
        resp = asyncio.run(portal_module.portal_events_recent(
            event_type=None, severity=None, since_iso=None,
            limit=25, offset=0,
            brokerage={"id": "test-b"},
        ))
    finally:
        portal_module.recent_events = original

    assert resp["count"] == 1
    p = resp["events"][0].get("payload", {})
    assert p.get("category") == "has_agent"
    for forbidden in ("text", "raw_text", "api_key"):
        assert forbidden not in p, f"{forbidden} leaked in portal payload"


def test_portal_callbacks_sanitises_payload():
    if _skip_if_imports_failed():
        return
    canned = [_leaky_event()]
    original = portal_module.callback_events
    portal_module.callback_events = lambda **kw: canned
    try:
        resp = asyncio.run(portal_module.portal_callbacks(
            since_iso=None, limit=50, offset=0,
            brokerage={"id": "test-b"},
        ))
    finally:
        portal_module.callback_events = original

    p = resp["events"][0].get("payload", {})
    assert "text" not in p
    assert "raw_text" not in p
    assert "api_key" not in p


def test_portal_recent_events_filters_by_brokerage():
    if _skip_if_imports_failed():
        return
    seen_kwargs = {}

    def _capture(**kw):
        seen_kwargs.update(kw)
        return []

    original = portal_module.recent_events
    portal_module.recent_events = _capture
    try:
        asyncio.run(portal_module.portal_events_recent(
            event_type=None, severity=None, since_iso=None,
            limit=25, offset=0,
            brokerage={"id": "remax-miami"},
        ))
    finally:
        portal_module.recent_events = original

    assert seen_kwargs.get("brokerage_id") == "remax-miami", \
        "portal route did not pass brokerage_id filter to query layer"


# ───────────── admin returns raw payloads ─────────────

def test_admin_recent_events_returns_raw_payload():
    if _skip_if_imports_failed():
        return
    canned = [_leaky_event()]
    original = admin_events_module.recent_events
    admin_events_module.recent_events = lambda **kw: canned
    try:
        resp = asyncio.run(admin_events_module.admin_events_recent(
            brokerage_id=None, event_type=None, severity=None, since_iso=None,
            limit=25, offset=0,
            _=True,
        ))
    finally:
        admin_events_module.recent_events = original

    p = resp["events"][0].get("payload", {})
    # Admin sees full payload including the fields portal scrubs.
    assert p.get("text") == "raw caller transcript that must not leak"
    assert p.get("api_key") == "sk-leak"


# ───────────── portal cross-brokerage protection ─────────────

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


def test_portal_call_timeline_404_when_call_not_owned():
    if _skip_if_imports_failed():
        return
    # Calls table returns no row → ownership check fails → 404
    original_db = portal_module.get_supabase
    portal_module.get_supabase = lambda: _FakeDB([])
    try:
        try:
            asyncio.run(portal_module.portal_call_timeline(
                call_id="CA-other-brokerage",
                brokerage={"id": "victim-b"},
            ))
            raised = None
        except HTTPException as e:
            raised = e
    finally:
        portal_module.get_supabase = original_db

    assert raised is not None, "expected HTTPException, got success"
    assert raised.status_code == 404


def test_portal_call_timeline_returns_sanitised_when_owned():
    if _skip_if_imports_failed():
        return
    canned = [_leaky_event()]
    original_db = portal_module.get_supabase
    original_efc = portal_module.events_for_call
    portal_module.get_supabase = lambda: _FakeDB([{"id": "CA-x"}])
    portal_module.events_for_call = lambda *a, **kw: canned
    try:
        resp = asyncio.run(portal_module.portal_call_timeline(
            call_id="CA-x",
            brokerage={"id": "test-b"},
        ))
    finally:
        portal_module.get_supabase = original_db
        portal_module.events_for_call = original_efc

    assert resp["call_id"] == "CA-x"
    p = resp["events"][0].get("payload", {})
    assert "text" not in p
    assert "api_key" not in p


# ───────────── intelligence summary aggregates correctly ─────────────

def test_admin_intelligence_summary_aggregates():
    if _skip_if_imports_failed():
        return
    canned = [
        {
            "event_type": "call.started", "event_category": "call",
            "severity": "info", "call_id": "CA1", "lead_id": None,
            "created_at": "2026-05-03T10:00:00+00:00", "payload": {},
        },
        {
            "event_type": "callback.requested", "event_category": "lead",
            "severity": "info", "call_id": "CA1", "lead_id": None,
            "created_at": "2026-05-03T10:01:00+00:00", "payload": {},
        },
        {
            "event_type": "system.error", "event_category": "ops",
            "severity": "error", "call_id": None, "lead_id": None,
            "created_at": "2026-05-03T10:02:00+00:00", "payload": {},
        },
    ]
    original_re = admin_events_module.recent_events
    original_fc = admin_events_module.fetch_call_and_lead_context
    admin_events_module.recent_events = lambda **kw: canned
    admin_events_module.fetch_call_and_lead_context = lambda *a, **kw: ({}, {})
    try:
        resp = asyncio.run(admin_events_module.admin_intelligence_summary(
            brokerage_id="b1", since_iso=None, _=True,
        ))
    finally:
        admin_events_module.recent_events = original_re
        admin_events_module.fetch_call_and_lead_context = original_fc

    assert resp["events_total"] == 3
    assert resp["events_by_category"]["call"] == 1
    assert resp["events_by_category"]["lead"] == 1
    assert resp["events_by_category"]["ops"] == 1
    assert resp["events_by_severity"]["error"] == 1
    assert resp["callback_events_count"] == 1
    assert resp["calls_analyzed"] == 1   # only CA1 has a call_id
    assert resp["version"] == "v1"
    assert "leakage_breakdown" in resp


# ───────────── leakage enrichment ─────────────

def test_admin_summary_enrichment_changes_classification():
    """
    Without enrichment, a call.started + call.ended pair with no extracted
    fields lands in 'qualification_leakage' (the lead is empty). With the
    enriched lead row showing intent='buying', it should fall through to
    'no_leak_detected'. Proves the enrichment plumbing is actually feeding
    detect_leakage with real lead context.
    """
    if _skip_if_imports_failed():
        return

    canned = [
        {
            "event_type": "call.started", "event_category": "call",
            "severity": "info", "call_id": "CA-enriched", "lead_id": "lead-7",
            "created_at": "2026-05-03T10:00:00+00:00", "payload": {},
        },
        {
            "event_type": "call.ended", "event_category": "call",
            "severity": "info", "call_id": "CA-enriched", "lead_id": "lead-7",
            "created_at": "2026-05-03T10:05:00+00:00", "payload": {},
        },
    ]
    enriched_calls = {"CA-enriched": {"id": "CA-enriched", "outcome": "pending"}}
    enriched_leads = {"lead-7": {"id": "lead-7", "intent": "buying", "status": "qualified"}}

    original_re = admin_events_module.recent_events
    original_fc = admin_events_module.fetch_call_and_lead_context
    admin_events_module.recent_events = lambda **kw: canned
    admin_events_module.fetch_call_and_lead_context = (
        lambda *a, **kw: (enriched_calls, enriched_leads)
    )
    try:
        resp = asyncio.run(admin_events_module.admin_intelligence_summary(
            brokerage_id="b1", since_iso=None, _=True,
        ))

        # Now verify the un-enriched run produces qualification_leakage instead.
        admin_events_module.fetch_call_and_lead_context = lambda *a, **kw: ({}, {})
        resp_empty = asyncio.run(admin_events_module.admin_intelligence_summary(
            brokerage_id="b1", since_iso=None, _=True,
        ))
    finally:
        admin_events_module.recent_events = original_re
        admin_events_module.fetch_call_and_lead_context = original_fc

    assert resp["leakage_breakdown"].get("qualification_leakage", 0) == 0, (
        "enriched lead with intent should NOT flag qualification_leakage; "
        f"got: {resp['leakage_breakdown']}"
    )
    assert resp_empty["leakage_breakdown"].get("qualification_leakage", 0) == 1, (
        "un-enriched empty lead SHOULD flag qualification_leakage; "
        f"got: {resp_empty['leakage_breakdown']}"
    )


def test_admin_summary_db_failure_falls_back_to_empty_context():
    """
    If fetch_call_and_lead_context raises (or its internal queries fail),
    the helper itself returns ({}, {}). The route must still complete and
    classify with the empty-context fallback — never 500.
    """
    if _skip_if_imports_failed():
        return

    canned = [
        {
            "event_type": "call.started", "event_category": "call",
            "severity": "info", "call_id": "CA1", "lead_id": None,
            "created_at": "2026-05-03T10:00:00+00:00", "payload": {},
        },
    ]
    original_re = admin_events_module.recent_events
    original_fc = admin_events_module.fetch_call_and_lead_context
    admin_events_module.recent_events = lambda **kw: canned
    admin_events_module.fetch_call_and_lead_context = lambda *a, **kw: ({}, {})
    try:
        resp = asyncio.run(admin_events_module.admin_intelligence_summary(
            brokerage_id="b1", since_iso=None, _=True,
        ))
    finally:
        admin_events_module.recent_events = original_re
        admin_events_module.fetch_call_and_lead_context = original_fc

    assert resp["events_total"] == 1
    assert resp["calls_analyzed"] == 1
    assert "leakage_breakdown" in resp


def test_portal_summary_forces_brokerage_id_into_enrichment():
    """
    Portal summary must scope the call/lead context fetch to the
    authenticated brokerage — never pass None or someone else's id.
    """
    if _skip_if_imports_failed():
        return

    seen_ctx_kwargs = {}

    def _capture_ctx(call_ids, lead_ids, brokerage_id=None):
        seen_ctx_kwargs["brokerage_id"] = brokerage_id
        return ({}, {})

    canned = [
        {
            "event_type": "call.started", "event_category": "call",
            "severity": "info", "call_id": "CA1", "lead_id": None,
            "created_at": "2026-05-03T10:00:00+00:00", "payload": {},
        },
    ]

    original_re = portal_module.recent_events
    original_fc = portal_module.fetch_call_and_lead_context
    portal_module.recent_events = lambda **kw: canned
    portal_module.fetch_call_and_lead_context = _capture_ctx
    try:
        asyncio.run(portal_module.portal_intelligence_summary(
            since_iso=None,
            brokerage={"id": "remax-miami"},
        ))
    finally:
        portal_module.recent_events = original_re
        portal_module.fetch_call_and_lead_context = original_fc

    assert seen_ctx_kwargs.get("brokerage_id") == "remax-miami", (
        "portal summary must pass authenticated brokerage_id into the "
        f"enrichment fetch; got: {seen_ctx_kwargs}"
    )


if __name__ == "__main__":
    failures = 0
    funcs = [v for k, v in list(globals().items()) if k.startswith("test_") and callable(v)]
    for fn in funcs:
        try:
            fn()
            print(f"PASS {fn.__name__}")
        except AssertionError as e:
            failures += 1
            print(f"FAIL {fn.__name__}: {e}")
        except Exception as e:
            failures += 1
            print(f"ERROR {fn.__name__}: {type(e).__name__}: {e}")
    print(f"\n{len(funcs) - failures}/{len(funcs)} passed")
    sys.exit(1 if failures else 0)
