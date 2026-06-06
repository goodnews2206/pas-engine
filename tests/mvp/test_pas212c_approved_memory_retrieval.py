"""PAS212C — approved memory retrieval tests (read-only).

Covers: approved retrievable; candidate/rejected/archived NOT retrievable;
tenant isolation; subject + candidate_type filters; context formatting includes
evidence/provenance/confidence; formatting implies no behaviour change.
"""
from app.services.memory import candidate_contracts as cc
from app.services.memory.approved_memory_retrieval import (
    CONTEXT_SOURCE,
    format_approved_context,
    retrieve_approved,
)
from app.services.memory.candidate_generation import generate_candidates
from app.services.memory.candidate_store import MemoryCandidateStore

NOW = "2026-06-06T00:00:00+00:00"

LEADS = [
    {"id": "L1", "intent": "buying", "budget": "500k", "timeline": "1 month", "source": "web"},
    {"id": "L2", "intent": "selling", "source": "web"},
]
EVENTS = [
    {"id": "E1", "event_type": "call.objection_detected", "lead_id": "L1"},
    {"id": "E2", "event_type": "call.objection_detected", "lead_id": "L1"},
    {"id": "E3", "event_type": "call.callback_captured", "lead_id": "L1"},
]


def _by_type(cands, ctype):
    return next(c for c in cands if c.candidate_type == ctype)


def _seed():
    """Store with: lead_fact(L1)=approved, callback(L1)=rejected,
    repeated_objection(L1)=archived, lead_fact(L2)=candidate."""
    store = MemoryCandidateStore()
    cands = generate_candidates("brk-A", leads=LEADS, events=EVENTS, now=NOW)
    store.add_candidates("brk-A", cands)
    l1_fact = next(c for c in cands if c.candidate_type == cc.TYPE_LEAD_FACT and c.subject_id == "L1")
    cb = _by_type(cands, cc.TYPE_CALLBACK_PREFERENCE)
    obj = _by_type(cands, cc.TYPE_REPEATED_OBJECTION)
    store.approve("brk-A", l1_fact.id, reviewer="owner@brk", now=NOW)
    store.reject("brk-A", cb.id, reviewer="owner@brk", now=NOW)
    store.archive("brk-A", obj.id, reviewer="owner@brk", now=NOW)
    return store, l1_fact, cb, obj


def test_approved_memory_is_retrievable():
    store, l1_fact, _, _ = _seed()
    got = retrieve_approved("brk-A", store=store)
    ids = [m.id for m in got]
    assert l1_fact.id in ids
    assert all(m.status == cc.STATUS_APPROVED for m in got)


def test_candidate_memory_is_not_retrievable():
    store, _, _, _ = _seed()
    got = retrieve_approved("brk-A", store=store)
    # L2 lead_fact remains a candidate → excluded
    assert all(m.status == cc.STATUS_APPROVED for m in got)
    assert not any(m.subject_id == "L2" for m in got)


def test_rejected_memory_is_not_retrievable():
    store, _, cb, _ = _seed()
    got = retrieve_approved("brk-A", store=store)
    assert cb.id not in [m.id for m in got]


def test_archived_memory_is_not_retrievable():
    store, _, _, obj = _seed()
    got = retrieve_approved("brk-A", store=store)
    assert obj.id not in [m.id for m in got]


def test_tenant_isolation_enforced():
    store, _, _, _ = _seed()
    assert retrieve_approved("brk-B", store=store) == []


def test_subject_filters_work():
    store, l1_fact, _, _ = _seed()
    # subject_type + subject_id filter
    got = retrieve_approved("brk-A", store=store, subject_type=cc.SUBJECT_LEAD, subject_id="L1")
    assert [m.id for m in got] == [l1_fact.id]
    # non-matching subject → empty
    assert retrieve_approved("brk-A", store=store, subject_id="L2") == []


def test_candidate_type_filter_works():
    store, l1_fact, _, _ = _seed()
    got = retrieve_approved("brk-A", store=store, candidate_type=cc.TYPE_LEAD_FACT)
    assert [m.id for m in got] == [l1_fact.id]
    # a type with no approved record → empty
    assert retrieve_approved("brk-A", store=store, candidate_type=cc.TYPE_CALLBACK_PREFERENCE) == []


def test_empty_list_when_none():
    store = MemoryCandidateStore()  # nothing stored
    assert retrieve_approved("brk-A", store=store) == []


def test_formatted_context_includes_evidence_provenance_confidence():
    store, l1_fact, _, _ = _seed()
    blocks = format_approved_context(retrieve_approved("brk-A", store=store))
    assert blocks
    b = blocks[0]
    assert b["source"] == CONTEXT_SOURCE == "approved_memory"
    assert b["evidence_refs"] == list(l1_fact.evidence_refs) and b["evidence_refs"]
    assert b["provenance"] == l1_fact.provenance
    assert b["confidence"] == l1_fact.confidence
    assert b["approved_memory"] == l1_fact.proposed_memory


def test_formatted_context_implies_no_behaviour_change():
    store, _, _, _ = _seed()
    blocks = format_approved_context(retrieve_approved("brk-A", store=store))
    for b in blocks:
        assert b["read_only"] is True
        assert b["source"] == "approved_memory"
        # formatter must not introduce injection/directive scaffolding
        for forbidden_key in ("instruction", "directive", "system_prompt", "inject", "command"):
            assert forbidden_key not in b
        # no transcript leakage in surfaced fields
        blob = (b["approved_memory"] + " " + " ".join(b["evidence_refs"])).lower()
        for tok in ("transcript", "turns", "raw_text", "utterance"):
            assert tok not in blob


def test_retrieval_never_returns_unapproved_even_if_present():
    store, _, _, _ = _seed()
    # everything that comes back is approved, nothing else
    got = retrieve_approved("brk-A", store=store)
    assert got and all(m.status == cc.STATUS_APPROVED for m in got)
    # total approved count matches store's own approved list
    assert len(got) == len(store.list_candidates("brk-A", status=cc.STATUS_APPROVED))
