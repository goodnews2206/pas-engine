"""PAS212 — memory candidate pipeline tests (narrow, deterministic, read-only).

Covers: deterministic generation, brokerage_id presence + tenant pin, evidence
required, default status CANDIDATE, explicit approval, rejection ≠ approval,
no automatic behaviour change, tenant isolation, missing-evidence → no candidate.
"""
import importlib

from app.services.memory import candidate_contracts as cc
from app.services.memory.candidate_generation import (
    generate_candidates,
    generate_lead_fact_candidates,
)
from app.services.memory.candidate_store import MemoryCandidateStore

NOW = "2026-06-06T00:00:00+00:00"

LEADS = [
    {"id": "L1", "brokerage_id": "brk-A", "intent": "buying", "budget": "500k", "timeline": "1 month", "source": "web"},
    {"id": "L2", "brokerage_id": "brk-A", "intent": "selling", "source": "web", "last_booked_at": "x"},
    {"id": "L3", "brokerage_id": "brk-A", "source": "web", "last_booked_at": "x"},
]
EVENTS = [
    {"id": "E1", "event_type": "call.objection_detected", "lead_id": "L1"},
    {"id": "E2", "event_type": "call.objection_detected", "lead_id": "L1"},
    {"id": "E3", "event_type": "call.callback_captured", "lead_id": "L1"},
]


# 1. deterministic generation
def test_generation_is_deterministic():
    a = generate_candidates("brk-A", leads=LEADS, events=EVENTS, now=NOW)
    b = generate_candidates("brk-A", leads=LEADS, events=EVENTS, now=NOW)
    assert [c.id for c in a] == [c.id for c in b]
    assert a == b  # full structural equality, including ids


# 2. candidates include brokerage_id + tenant pin from argument only
def test_all_candidates_carry_brokerage_id_from_argument():
    # input rows claim brk-EVIL; the explicit argument must win.
    poisoned = [dict(L, brokerage_id="brk-EVIL") for L in LEADS]
    cands = generate_candidates("brk-A", leads=poisoned, events=EVENTS, now=NOW)
    assert cands
    assert all(c.brokerage_id == "brk-A" for c in cands)


# 3. evidence_refs required
def test_evidence_required_in_contract_and_generation():
    # contract: a candidate with no evidence is invalid
    bad = cc.MemoryCandidate(
        id="x", brokerage_id="brk-A", subject_type=cc.SUBJECT_LEAD, subject_id="L1",
        candidate_type=cc.TYPE_LEAD_FACT, proposed_memory="fact", evidence_refs=(),
        provenance="p", confidence=0.5,
    )
    assert "missing evidence_refs" in cc.validate_candidate(bad)
    # generation: every emitted candidate has non-empty evidence
    for c in generate_candidates("brk-A", leads=LEADS, events=EVENTS, now=NOW):
        assert c.evidence_refs


# 9. missing evidence does not create candidate
def test_missing_evidence_yields_no_candidate():
    # lead with no id → no evidence → no lead_fact candidate
    cands = generate_lead_fact_candidates("brk-A", [{"intent": "buying"}], now=NOW)
    assert cands == []
    # single objection (below threshold) → no repeated-objection candidate
    one = generate_candidates("brk-A", events=[EVENTS[0]], now=NOW)
    assert not any(c.candidate_type == cc.TYPE_REPEATED_OBJECTION for c in one)


# 4. default status is candidate
def test_default_status_is_candidate():
    for c in generate_candidates("brk-A", leads=LEADS, events=EVENTS, now=NOW):
        assert c.status == cc.STATUS_CANDIDATE
        assert c.reviewed_by is None and c.reviewed_at is None


# 5. approval is explicit
def test_approval_is_explicit_and_recorded():
    store = MemoryCandidateStore()
    cands = generate_candidates("brk-A", leads=LEADS, events=EVENTS, now=NOW)
    store.add_candidates("brk-A", cands)
    cid = cands[0].id
    # no reviewer → refused
    assert store.approve("brk-A", cid, reviewer="", now=NOW)["status"] == "failed"
    # explicit reviewer → approved + recorded
    res = store.approve("brk-A", cid, reviewer="owner@brk", now=NOW)
    assert res["status"] == "ok"
    assert res["candidate"].status == cc.STATUS_APPROVED
    assert res["candidate"].reviewed_by == "owner@brk"
    assert res["candidate"].reviewed_at == NOW


# 6. rejected candidates are not approved
def test_rejected_candidate_cannot_be_approved():
    store = MemoryCandidateStore()
    cands = generate_candidates("brk-A", leads=LEADS, events=EVENTS, now=NOW)
    store.add_candidates("brk-A", cands)
    cid = cands[0].id
    assert store.reject("brk-A", cid, reviewer="owner@brk", now=NOW)["status"] == "ok"
    assert store.get_candidate("brk-A", cid).status == cc.STATUS_REJECTED
    # cannot approve a rejected candidate
    assert store.approve("brk-A", cid, reviewer="owner@brk", now=NOW)["status"] == "failed"
    # rejected candidate stays stored (auditable) and not in approved list
    assert store.get_candidate("brk-A", cid) is not None
    assert cid not in [c.id for c in store.list_candidates("brk-A", status=cc.STATUS_APPROVED)]


# 7. no automatic behaviour change (structural: store imports nothing behavioural)
def test_store_has_no_behaviour_changing_imports():
    import ast
    import inspect
    import app.services.memory.candidate_store as cs_mod
    import app.services.memory.candidate_generation as gen_mod

    forbidden = ("state_machine", "brokerage_store", "calcom", "twilio", "outbound", "websocket")
    for mod in (cs_mod, gen_mod):
        tree = ast.parse(inspect.getsource(mod))
        imported = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported += [a.name for a in node.names]
            elif isinstance(node, ast.ImportFrom):
                imported.append(node.module or "")
        joined = " ".join(imported)
        for bad in forbidden:
            assert bad not in joined, f"{mod.__name__} must not import anything touching {bad}"


# 8. tenant isolation
def test_tenant_isolation_across_brokerages():
    store = MemoryCandidateStore()
    cands = generate_candidates("brk-A", leads=LEADS, events=EVENTS, now=NOW)
    store.add_candidates("brk-A", cands)
    cid = cands[0].id
    # brk-B cannot see or transition brk-A's candidate
    assert store.get_candidate("brk-B", cid) is None
    assert store.list_candidates("brk-B") == []
    assert store.approve("brk-B", cid, reviewer="intruder", now=NOW)["status"] == "failed"
    # brk-A's candidate is untouched
    assert store.get_candidate("brk-A", cid).status == cc.STATUS_CANDIDATE


def test_add_candidates_rejects_cross_tenant_records():
    store = MemoryCandidateStore()
    cands = generate_candidates("brk-A", leads=LEADS, events=EVENTS, now=NOW)
    # try to file brk-A candidates under brk-B → skipped (tenant pin guard)
    stored = store.add_candidates("brk-B", cands)
    assert stored == []
    assert store.list_candidates("brk-B") == []


def test_regeneration_is_idempotent_and_preserves_review():
    store = MemoryCandidateStore()
    cands = generate_candidates("brk-A", leads=LEADS, events=EVENTS, now=NOW)
    store.add_candidates("brk-A", cands)
    cid = cands[0].id
    store.approve("brk-A", cid, reviewer="owner@brk", now=NOW)
    # regenerate identical candidates and re-add → prior approval is preserved
    again = generate_candidates("brk-A", leads=LEADS, events=EVENTS, now=NOW)
    store.add_candidates("brk-A", again)
    assert store.get_candidate("brk-A", cid).status == cc.STATUS_APPROVED
