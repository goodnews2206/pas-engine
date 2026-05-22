"""
PAS201 — Simulation evidence digest tests.

Coverage:

  * Happy path:
      - digest builds from a valid PAS195..PAS200 chain
      - phase == "PAS201"
      - allowed_environment == "SIMULATION_ONLY"
      - live_behavior_changed is False
      - digest_id is deterministic for fixed inputs
      - digest_id carries pas201 prefix
      - digest_id changes when any of its hash inputs changes
      - strategy_id mirrors the package
      - evidence_strength is "strong" for the current
        callback_first chain
      - artifact_integrity is all-True on a clean lineage

  * Broken-lineage rejection:
      - review.recommendation_id mismatch raises
      - package.recommendation_id mismatch raises
      - package.review_id mismatch raises
      - package.strategy_id != recommendation.recommended_strategy
        raises
      - runtime.package_id mismatch raises
      - runtime.executed_strategy != package.strategy_id raises
      - inspection.lineage_summary.runtime_id mismatch raises
      - inspection.lineage_summary.recommendation_id mismatch
        raises
      - behavioral_evaluation.runtime_id mismatch raises
      - behavioral_evaluation.inspection_id mismatch raises
      - recommendation.status != CANDIDATE raises
      - review.new_status != APPROVED_FOR_MANUAL_TEST raises
      - review.live_behavior_changed != False raises
      - package.status / environment / live mismatches raise
      - runtime.status / environment / live mismatches raise
      - inspection phase != PAS199 raises
      - behavioral_evaluation phase != PAS200 raises
      - blank generated_at raises

  * Evidence strength:
      - clean callback_first chain -> "strong"
      - safety auto_fail -> "blocked"
      - pass_rate 0.80 -> "moderate"
      - pass_rate 0.60 -> "weak"
      - broken inspection_integrity -> "blocked"

  * Claimable / not-claimable invariants:
      - claimable_now drawn from CLAIMABLE_NOW_VOCAB
      - not_claimable_yet drawn from NOT_CLAIMABLE_YET_VOCAB
      - claimable_now never asserts live routing activity
      - not_claimable_yet always references live-routing gating
      - blocked digest restricts claimable_now to the always-true
        subset

  * Bounded-environment invariants:
      - no PII tokens in the digest
      - no production brokerage IDs in the digest
      - no free-form operator-note fields
      - inputs not mutated

  * Source-surface invariants:
      - no forbidden status literals
      - no live-mutation identifiers
      - no banned imports

  * CLI:
      - happy-path writes digest
      - --summary-only suppresses file write
      - missing --runtime exits 2
      - rejected lineage exits 2

  * Readiness gate:
      - exit 0 / verdict=READY
      - JSON envelope valid
"""

from __future__ import annotations

import ast
import json
import pathlib
import re
import subprocess
import sys
import tempfile
from typing import Optional

import pytest


_REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))


from app.services.simulation.evidence_digest import (  # noqa: E402
    ARTIFACT_INTEGRITY_KEYS,
    BEHAVIORAL_SUMMARY_KEYS,
    CLAIMABLE_NOW_VOCAB,
    DIGEST_ENVIRONMENT_SIMULATION_ONLY,
    DIGEST_REQUIRED_KEYS,
    EVIDENCE_STRENGTH_VALUES,
    INSPECTION_SUMMARY_KEYS,
    NOT_CLAIMABLE_YET_VOCAB,
    OPERATOR_HIGHLIGHTS,
    OPERATOR_NEXT_ACTIONS,
    OPERATOR_SUMMARY_KEYS,
    PACKAGE_SUMMARY_KEYS,
    RECOMMENDATION_SUMMARY_KEYS,
    REVIEW_SUMMARY_KEYS,
    RUNTIME_SUMMARY_KEYS,
    EvidenceDigestValidationError,
    build_evidence_digest,
)
from app.services.simulation.behavioral_evaluation import (  # noqa: E402
    build_behavioral_evaluation,
)
from app.services.simulation.manual_test_runtime import (  # noqa: E402
    execute_manual_test_runtime,
)
from app.services.simulation.runtime_inspection import (  # noqa: E402
    build_inspection,
)


def _read(relpath: str) -> str:
    return (_REPO_ROOT / relpath).read_text(encoding="utf-8")


# ──────────────────────────────────────────────────────────────────
# Fixtures
# ──────────────────────────────────────────────────────────────────

REC_ID     = "pas195-rec-9a9566a11d621684"
REVIEW_ID  = "pas196-rev-deadbeefcafebabe"
PACKAGE_ID = "pas197-pkg-2b7c50e63bf5fb88"
GEN_AT     = "2026-05-22T07:00:00Z"


def _candidate_recommendation(
    rec_id: str = REC_ID, strategy: str = "callback_first",
    rejected: str = "assertive",
) -> dict:
    return {
        "recommendation_id":    rec_id,
        "status":               "CANDIDATE",
        "operator_required":    True,
        "recommended_strategy": strategy,
        "rejected_strategy":    rejected,
        "recommendation_type":  "promote_strategy",
        "confidence_level":     "high",
        "pass_rate_threshold":  0.95,
        "phase":                "PAS195",
    }


def _approved_review(
    rec_id: str = REC_ID, review_id: str = REVIEW_ID,
) -> dict:
    return {
        "review_id":             review_id,
        "recommendation_id":     rec_id,
        "previous_status":       "CANDIDATE",
        "new_status":            "APPROVED_FOR_MANUAL_TEST",
        "live_behavior_changed": False,
        "actor_type":            "operator",
        "actor_id_token":        "op_demo0001",
        "reason_token":          "operator_approved_for_manual_test",
        "reviewed_at":           "2026-05-21T12:06:02Z",
        "operator_required":     True,
        "phase":                 "PAS196",
    }


def _ready_package(
    rec_id: str = REC_ID, review_id: str = REVIEW_ID,
    package_id: str = PACKAGE_ID, strategy_id: str = "callback_first",
) -> dict:
    return {
        "package_id":            package_id,
        "phase":                 "PAS197",
        "recommendation_id":     rec_id,
        "review_id":             review_id,
        "strategy_id":           strategy_id,
        "status":                "READY_FOR_MANUAL_TEST",
        "live_behavior_changed": False,
        "allowed_environment":   "SIMULATION_ONLY",
        "test_plan":             [],
        "success_metrics":       [],
        "rollback_notes":        [],
        "safety_notes":          [],
        "created_at":            "2026-05-21T12:22:47Z",
    }


def _executed_runtime(strategy_id: str = "callback_first") -> dict:
    return execute_manual_test_runtime(
        _ready_package(strategy_id=strategy_id),
        created_at="2026-05-22T04:00:00Z",
    )


def _matching_inspection(
    runtime: dict, strategy: str = "callback_first",
) -> dict:
    return build_inspection(
        _candidate_recommendation(strategy=strategy),
        _approved_review(),
        _ready_package(strategy_id=strategy),
        runtime,
        generated_at=GEN_AT,
    )


def _matching_behavioral(runtime: dict, inspection: dict) -> dict:
    return build_behavioral_evaluation(
        runtime, generated_at=GEN_AT, inspection=inspection,
    )


def _clean_chain():
    rec  = _candidate_recommendation()
    rev  = _approved_review()
    pkg  = _ready_package()
    rt   = _executed_runtime()
    insp = _matching_inspection(rt)
    beh  = _matching_behavioral(rt, insp)
    return rec, rev, pkg, rt, insp, beh


# ──────────────────────────────────────────────────────────────────
# Happy path
# ──────────────────────────────────────────────────────────────────

def test_digest_builds_from_clean_chain():
    rec, rev, pkg, rt, insp, beh = _clean_chain()
    d = build_evidence_digest(
        rec, rev, pkg, rt, insp, beh, generated_at=GEN_AT,
    )
    assert isinstance(d, dict)


def test_digest_carries_every_required_key():
    d = build_evidence_digest(*_clean_chain(), generated_at=GEN_AT)
    for k in DIGEST_REQUIRED_KEYS:
        assert k in d, f"missing {k}"


def test_digest_phase_is_pas201():
    d = build_evidence_digest(*_clean_chain(), generated_at=GEN_AT)
    assert d["phase"] == "PAS201"


def test_digest_environment_is_simulation_only():
    d = build_evidence_digest(*_clean_chain(), generated_at=GEN_AT)
    assert d["allowed_environment"] == DIGEST_ENVIRONMENT_SIMULATION_ONLY
    assert d["allowed_environment"] == "SIMULATION_ONLY"


def test_digest_live_behavior_changed_is_false():
    d = build_evidence_digest(*_clean_chain(), generated_at=GEN_AT)
    assert d["live_behavior_changed"] is False


def test_digest_id_is_deterministic():
    a = build_evidence_digest(*_clean_chain(), generated_at=GEN_AT)
    b = build_evidence_digest(*_clean_chain(), generated_at=GEN_AT)
    assert a == b


def test_digest_id_carries_pas201_prefix():
    d = build_evidence_digest(*_clean_chain(), generated_at=GEN_AT)
    assert d["digest_id"].startswith("pas201-dgst-")


def test_digest_id_changes_when_any_hash_input_changes():
    base = build_evidence_digest(*_clean_chain(), generated_at=GEN_AT)
    rec, rev, pkg, rt, insp, beh = _clean_chain()

    rec2 = dict(rec); rec2["recommendation_id"] = "pas195-rec-other"
    rev2 = dict(rev); rev2["recommendation_id"] = "pas195-rec-other"
    pkg2 = dict(pkg); pkg2["recommendation_id"] = "pas195-rec-other"
    # rebuild downstream so lineage holds
    insp2 = build_inspection(rec2, rev2, pkg2, rt, generated_at=GEN_AT)
    beh2 = build_behavioral_evaluation(rt, generated_at=GEN_AT, inspection=insp2)
    v = build_evidence_digest(rec2, rev2, pkg2, rt, insp2, beh2, generated_at=GEN_AT)
    assert v["digest_id"] != base["digest_id"]


def test_digest_strategy_id_mirrors_package():
    d = build_evidence_digest(*_clean_chain(), generated_at=GEN_AT)
    assert d["strategy_id"] == "callback_first"


def test_digest_summary_keys_present():
    d = build_evidence_digest(*_clean_chain(), generated_at=GEN_AT)
    for k in RECOMMENDATION_SUMMARY_KEYS:
        assert k in d["recommendation_summary"]
    for k in REVIEW_SUMMARY_KEYS:
        assert k in d["review_summary"]
    for k in PACKAGE_SUMMARY_KEYS:
        assert k in d["package_summary"]
    for k in RUNTIME_SUMMARY_KEYS:
        assert k in d["runtime_summary"]
    for k in INSPECTION_SUMMARY_KEYS:
        assert k in d["inspection_summary"]
    for k in BEHAVIORAL_SUMMARY_KEYS:
        assert k in d["behavioral_summary"]
    for k in OPERATOR_SUMMARY_KEYS:
        assert k in d["operator_summary"]


def test_artifact_integrity_all_true_on_clean_chain():
    d = build_evidence_digest(*_clean_chain(), generated_at=GEN_AT)
    integ = d["artifact_integrity"]
    for k in ARTIFACT_INTEGRITY_KEYS:
        assert k in integ, f"integrity missing {k}"
        assert integ[k] is True, f"integrity check {k} unexpectedly False"


def test_evidence_strength_strong_for_clean_callback_first_chain():
    d = build_evidence_digest(*_clean_chain(), generated_at=GEN_AT)
    assert d["evidence_strength"] == "strong"
    assert d["evidence_strength"] in EVIDENCE_STRENGTH_VALUES


def test_operator_summary_highlights_drawn_from_closed_vocab():
    d = build_evidence_digest(*_clean_chain(), generated_at=GEN_AT)
    for h in d["operator_summary"]["highlights"]:
        assert h in OPERATOR_HIGHLIGHTS


def test_operator_summary_next_action_drawn_from_closed_vocab():
    d = build_evidence_digest(*_clean_chain(), generated_at=GEN_AT)
    assert d["operator_summary"]["recommended_next_action"] in OPERATOR_NEXT_ACTIONS


def test_operator_summary_next_action_for_strong_is_review_then_decide():
    d = build_evidence_digest(*_clean_chain(), generated_at=GEN_AT)
    assert d["operator_summary"]["recommended_next_action"] == (
        "review_digest_then_decide_pilot_step"
    )


# ──────────────────────────────────────────────────────────────────
# Broken-lineage rejection
# ──────────────────────────────────────────────────────────────────

def test_review_recommendation_id_mismatch_raises():
    rec, rev, pkg, rt, insp, beh = _clean_chain()
    rev2 = dict(rev); rev2["recommendation_id"] = "pas195-rec-other"
    with pytest.raises(EvidenceDigestValidationError):
        build_evidence_digest(rec, rev2, pkg, rt, insp, beh, generated_at=GEN_AT)


def test_package_recommendation_id_mismatch_raises():
    rec, rev, pkg, rt, insp, beh = _clean_chain()
    pkg2 = dict(pkg); pkg2["recommendation_id"] = "pas195-rec-other"
    with pytest.raises(EvidenceDigestValidationError):
        build_evidence_digest(rec, rev, pkg2, rt, insp, beh, generated_at=GEN_AT)


def test_package_review_id_mismatch_raises():
    rec, rev, pkg, rt, insp, beh = _clean_chain()
    pkg2 = dict(pkg); pkg2["review_id"] = "pas196-rev-other"
    with pytest.raises(EvidenceDigestValidationError):
        build_evidence_digest(rec, rev, pkg2, rt, insp, beh, generated_at=GEN_AT)


def test_package_strategy_id_mismatch_raises():
    rec, rev, pkg, rt, insp, beh = _clean_chain()
    pkg2 = dict(pkg); pkg2["strategy_id"] = "balanced"
    with pytest.raises(EvidenceDigestValidationError):
        build_evidence_digest(rec, rev, pkg2, rt, insp, beh, generated_at=GEN_AT)


def test_runtime_package_id_mismatch_raises():
    rec, rev, pkg, rt, insp, beh = _clean_chain()
    rt2 = dict(rt); rt2["package_id"] = "pas197-pkg-other"
    with pytest.raises(EvidenceDigestValidationError):
        build_evidence_digest(rec, rev, pkg, rt2, insp, beh, generated_at=GEN_AT)


def test_runtime_executed_strategy_mismatch_raises():
    rec, rev, pkg, rt, insp, beh = _clean_chain()
    rt2 = dict(rt); rt2["executed_strategy"] = "balanced"
    with pytest.raises(EvidenceDigestValidationError):
        build_evidence_digest(rec, rev, pkg, rt2, insp, beh, generated_at=GEN_AT)


def test_inspection_lineage_runtime_id_mismatch_raises():
    rec, rev, pkg, rt, insp, beh = _clean_chain()
    insp2 = json.loads(json.dumps(insp))
    insp2["lineage_summary"]["runtime_id"] = "pas198-rt-other"
    with pytest.raises(EvidenceDigestValidationError):
        build_evidence_digest(rec, rev, pkg, rt, insp2, beh, generated_at=GEN_AT)


def test_inspection_lineage_recommendation_id_mismatch_raises():
    rec, rev, pkg, rt, insp, beh = _clean_chain()
    insp2 = json.loads(json.dumps(insp))
    insp2["lineage_summary"]["recommendation_id"] = "pas195-rec-other"
    with pytest.raises(EvidenceDigestValidationError):
        build_evidence_digest(rec, rev, pkg, rt, insp2, beh, generated_at=GEN_AT)


def test_behavioral_runtime_id_mismatch_raises():
    rec, rev, pkg, rt, insp, beh = _clean_chain()
    beh2 = dict(beh); beh2["runtime_id"] = "pas198-rt-other"
    with pytest.raises(EvidenceDigestValidationError):
        build_evidence_digest(rec, rev, pkg, rt, insp, beh2, generated_at=GEN_AT)


def test_behavioral_inspection_id_mismatch_raises():
    rec, rev, pkg, rt, insp, beh = _clean_chain()
    beh2 = dict(beh); beh2["inspection_id"] = "pas199-insp-other"
    with pytest.raises(EvidenceDigestValidationError):
        build_evidence_digest(rec, rev, pkg, rt, insp, beh2, generated_at=GEN_AT)


@pytest.mark.parametrize("bad_status", ["REJECTED", "EXPIRED",
                                        "APPROVED_FOR_MANUAL_TEST"])
def test_recommendation_status_not_candidate_raises(bad_status):
    rec, rev, pkg, rt, insp, beh = _clean_chain()
    rec2 = dict(rec); rec2["status"] = bad_status
    with pytest.raises(EvidenceDigestValidationError):
        build_evidence_digest(rec2, rev, pkg, rt, insp, beh, generated_at=GEN_AT)


@pytest.mark.parametrize("bad_status", ["REJECTED", "EXPIRED", "CANDIDATE"])
def test_review_new_status_not_approved_raises(bad_status):
    rec, rev, pkg, rt, insp, beh = _clean_chain()
    rev2 = dict(rev); rev2["new_status"] = bad_status
    with pytest.raises(EvidenceDigestValidationError):
        build_evidence_digest(rec, rev2, pkg, rt, insp, beh, generated_at=GEN_AT)


def test_review_live_behavior_changed_true_raises():
    rec, rev, pkg, rt, insp, beh = _clean_chain()
    rev2 = dict(rev); rev2["live_behavior_changed"] = True
    with pytest.raises(EvidenceDigestValidationError):
        build_evidence_digest(rec, rev2, pkg, rt, insp, beh, generated_at=GEN_AT)


@pytest.mark.parametrize("field,bad", [
    ("status",                "CANDIDATE"),
    ("allowed_environment",   "PRODUCTION"),
    ("live_behavior_changed", True),
])
def test_package_field_mismatches_raise(field, bad):
    rec, rev, pkg, rt, insp, beh = _clean_chain()
    pkg2 = dict(pkg); pkg2[field] = bad
    with pytest.raises(EvidenceDigestValidationError):
        build_evidence_digest(rec, rev, pkg2, rt, insp, beh, generated_at=GEN_AT)


@pytest.mark.parametrize("field,bad", [
    ("status",                "READY_FOR_MANUAL_TEST"),
    ("allowed_environment",   "PRODUCTION"),
    ("live_behavior_changed", True),
])
def test_runtime_field_mismatches_raise(field, bad):
    rec, rev, pkg, rt, insp, beh = _clean_chain()
    rt2 = dict(rt); rt2[field] = bad
    with pytest.raises(EvidenceDigestValidationError):
        build_evidence_digest(rec, rev, pkg, rt2, insp, beh, generated_at=GEN_AT)


def test_inspection_phase_not_pas199_raises():
    rec, rev, pkg, rt, insp, beh = _clean_chain()
    insp2 = dict(insp); insp2["phase"] = "PAS198"
    with pytest.raises(EvidenceDigestValidationError):
        build_evidence_digest(rec, rev, pkg, rt, insp2, beh, generated_at=GEN_AT)


def test_behavioral_phase_not_pas200_raises():
    rec, rev, pkg, rt, insp, beh = _clean_chain()
    beh2 = dict(beh); beh2["phase"] = "PAS199"
    with pytest.raises(EvidenceDigestValidationError):
        build_evidence_digest(rec, rev, pkg, rt, insp, beh2, generated_at=GEN_AT)


def test_blank_generated_at_raises():
    with pytest.raises(EvidenceDigestValidationError):
        build_evidence_digest(*_clean_chain(), generated_at="")


# ──────────────────────────────────────────────────────────────────
# Evidence strength rules
# ──────────────────────────────────────────────────────────────────

def test_evidence_strength_blocked_on_safety_auto_fail():
    rec, rev, pkg, rt, insp, beh = _clean_chain()
    rt2 = json.loads(json.dumps(rt))
    rt2["safety_outcome"]["outcome"] = "auto_fail"
    d = build_evidence_digest(rec, rev, pkg, rt2, insp, beh, generated_at=GEN_AT)
    assert d["evidence_strength"] == "blocked"


def test_evidence_strength_moderate_on_pass_rate_080():
    rec, rev, pkg, rt, insp, beh = _clean_chain()
    rt2 = json.loads(json.dumps(rt))
    rt2["runtime_score"]["pass_rate"] = 0.80
    d = build_evidence_digest(rec, rev, pkg, rt2, insp, beh, generated_at=GEN_AT)
    assert d["evidence_strength"] == "moderate"


def test_evidence_strength_weak_on_pass_rate_060():
    rec, rev, pkg, rt, insp, beh = _clean_chain()
    rt2 = json.loads(json.dumps(rt))
    rt2["runtime_score"]["pass_rate"] = 0.60
    d = build_evidence_digest(rec, rev, pkg, rt2, insp, beh, generated_at=GEN_AT)
    assert d["evidence_strength"] == "weak"


def test_evidence_strength_blocked_when_inspection_integrity_breaks():
    rec, rev, pkg, rt, insp, beh = _clean_chain()
    insp2 = json.loads(json.dumps(insp))
    first_key = next(iter(insp2["artifact_integrity"]))
    insp2["artifact_integrity"][first_key] = False
    d = build_evidence_digest(rec, rev, pkg, rt, insp2, beh, generated_at=GEN_AT)
    assert d["evidence_strength"] == "blocked"


# ──────────────────────────────────────────────────────────────────
# Claimable / not-claimable invariants
# ──────────────────────────────────────────────────────────────────

def test_claimable_now_drawn_from_closed_vocab():
    d = build_evidence_digest(*_clean_chain(), generated_at=GEN_AT)
    for tok in d["claimable_now"]:
        assert tok in CLAIMABLE_NOW_VOCAB


def test_not_claimable_yet_drawn_from_closed_vocab():
    d = build_evidence_digest(*_clean_chain(), generated_at=GEN_AT)
    for tok in d["not_claimable_yet"]:
        assert tok in NOT_CLAIMABLE_YET_VOCAB


def test_claimable_now_excludes_live_routing_claims():
    d = build_evidence_digest(*_clean_chain(), generated_at=GEN_AT)
    # No token in claimable_now may assert that live call routing
    # or real lead exposure is happening.
    for tok in d["claimable_now"]:
        assert "live_call" not in tok
        assert "real_lead" not in tok
        assert "live_routing" not in tok
        # The only "live_*" token allowed is the negative one
        # explicitly asserting no live change.
        if tok.startswith("no_live") or tok == "no_live_behavior_changed":
            continue
        assert "live" not in tok or tok == "no_live_behavior_changed"


def test_not_claimable_yet_references_live_routing_gating():
    d = build_evidence_digest(*_clean_chain(), generated_at=GEN_AT)
    # The list must always remind operators that live routing
    # remains gated.
    assert "live_call_routing_remains_out_of_scope" in d["not_claimable_yet"]
    assert "real_lead_exposure_remains_out_of_scope" in d["not_claimable_yet"]


def test_not_claimable_yet_does_not_assert_live_routing_active():
    d = build_evidence_digest(*_clean_chain(), generated_at=GEN_AT)
    # Defensive: every not_claimable_yet token names a gap, not
    # an active capability.
    for tok in d["not_claimable_yet"]:
        assert (
            tok.endswith("_out_of_scope")
            or tok.endswith("_pending")
        ), tok


def test_blocked_digest_restricts_claimable_now():
    rec, rev, pkg, rt, insp, beh = _clean_chain()
    rt2 = json.loads(json.dumps(rt))
    rt2["safety_outcome"]["outcome"] = "auto_fail"
    d = build_evidence_digest(rec, rev, pkg, rt2, insp, beh, generated_at=GEN_AT)
    assert d["evidence_strength"] == "blocked"
    # Blocked digests only carry the always-true claims; never the
    # rehearsal-passed claim.
    assert "synthetic_rehearsal_passed_for_strategy" not in d["claimable_now"]
    assert "operator_approved_strategy_for_manual_test" not in d["claimable_now"]
    assert "no_live_behavior_changed" in d["claimable_now"]
    assert "no_pii_in_simulation_artifacts" in d["claimable_now"]


def test_strong_digest_carries_synthetic_rehearsal_passed_claim():
    d = build_evidence_digest(*_clean_chain(), generated_at=GEN_AT)
    assert d["evidence_strength"] == "strong"
    assert "synthetic_rehearsal_passed_for_strategy" in d["claimable_now"]


# ──────────────────────────────────────────────────────────────────
# Bounded-environment invariants
# ──────────────────────────────────────────────────────────────────

_PHONE_RES = (
    re.compile(r"\b\d{3}[\s.\-]\d{3}[\s.\-]\d{4}\b"),
    re.compile(r"\(\d{3}\)\s*\d{3}[\s.\-]?\d{4}"),
)

_PROD_ID_RES = (
    re.compile(r"\bbrokerage_id\s*=\s*[\"']?[0-9a-fA-F\-]{8,}[\"']?"),
    re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b"),
)


def test_digest_carries_no_phone_numbers():
    d = build_evidence_digest(*_clean_chain(), generated_at=GEN_AT)
    text = json.dumps(d, sort_keys=True)
    for pat in _PHONE_RES:
        assert not pat.search(text), "phone-shaped token in digest"


def test_digest_carries_no_production_brokerage_ids():
    d = build_evidence_digest(*_clean_chain(), generated_at=GEN_AT)
    text = json.dumps(d, sort_keys=True)
    for pat in _PROD_ID_RES:
        assert not pat.search(text), "production brokerage id in digest"


def test_digest_carries_no_freeform_text_fields():
    d = build_evidence_digest(*_clean_chain(), generated_at=GEN_AT)
    for forbidden in ("notes", "note", "free_text", "comment",
                      "operator_notes", "operator_comment", "headline"):
        assert forbidden not in d, (
            f"digest carries forbidden free-form field {forbidden!r}"
        )


def test_digest_does_not_mutate_inputs():
    rec, rev, pkg, rt, insp, beh = _clean_chain()
    before = (
        json.dumps(rec, sort_keys=True),
        json.dumps(rev, sort_keys=True),
        json.dumps(pkg, sort_keys=True),
        json.dumps(rt,  sort_keys=True),
        json.dumps(insp, sort_keys=True),
        json.dumps(beh, sort_keys=True),
    )
    build_evidence_digest(rec, rev, pkg, rt, insp, beh, generated_at=GEN_AT)
    after = (
        json.dumps(rec, sort_keys=True),
        json.dumps(rev, sort_keys=True),
        json.dumps(pkg, sort_keys=True),
        json.dumps(rt,  sort_keys=True),
        json.dumps(insp, sort_keys=True),
        json.dumps(beh, sort_keys=True),
    )
    assert before == after


# ──────────────────────────────────────────────────────────────────
# Source-surface invariants
# ──────────────────────────────────────────────────────────────────

_FORBIDDEN_STATUS_LITERALS = ("APPROVED", "APPLIED", "AUTO_APPLIED",
                              "LIVE", "DEPLOYED")
_FORBIDDEN_IDENTIFIERS = (
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
)

_BANNED_IMPORT_HEADS = ("twilio", "slack_sdk", "openai", "anthropic",
                        "dotenv", "supabase")
_BANNED_IMPORT_PREFIXES = (
    "app.services.slack",
    "app.routes.slack_command",
    "app.engine.state_machine",
    "app.engine",
)
_BANNED_CALLS = ("load_dotenv", "get_supabase")


_PAS201_FILES = (
    "app/services/simulation/evidence_digest.py",
    "scripts/pas201_build_simulation_evidence_digest.py",
    "scripts/pas201_evidence_digest_readiness_check.py",
)


_PAS201_FILES_FOR_FORBIDDEN_LITERAL_SCAN = (
    "app/services/simulation/evidence_digest.py",
    "scripts/pas201_build_simulation_evidence_digest.py",
)


def _string_constants(src: str):
    out = set()
    try:
        tree = ast.parse(src)
    except Exception:
        return out
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            out.add(node.value)
    return out


def _identifier_names(src: str):
    out = set()
    try:
        tree = ast.parse(src)
    except Exception:
        return out
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            out.add(node.name)
        elif isinstance(node, ast.AsyncFunctionDef):
            out.add(node.name)
        elif isinstance(node, ast.Name):
            out.add(node.id)
        elif isinstance(node, ast.Attribute):
            out.add(node.attr)
    return out


def _imports_and_calls(src: str):
    imports, calls = set(), set()
    tree = ast.parse(src)
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module)
        elif isinstance(node, ast.Call):
            func = node.func
            if isinstance(func, ast.Name):
                calls.add(func.id)
            elif isinstance(func, ast.Attribute):
                calls.add(func.attr)
    return imports, calls


@pytest.mark.parametrize("relpath", _PAS201_FILES_FOR_FORBIDDEN_LITERAL_SCAN)
def test_forbidden_status_literals_absent(relpath):
    consts = _string_constants(_read(relpath))
    for tok in _FORBIDDEN_STATUS_LITERALS:
        assert tok not in consts, (
            f"{relpath} carries forbidden status literal {tok!r}"
        )


@pytest.mark.parametrize("relpath", _PAS201_FILES_FOR_FORBIDDEN_LITERAL_SCAN)
def test_forbidden_identifiers_absent(relpath):
    names = _identifier_names(_read(relpath))
    for tok in _FORBIDDEN_IDENTIFIERS:
        assert tok not in names, (
            f"{relpath} carries forbidden identifier {tok!r}"
        )


@pytest.mark.parametrize("relpath", _PAS201_FILES)
def test_no_banned_imports_in_pas201_file(relpath):
    imports, calls = _imports_and_calls(_read(relpath))
    for mod in imports:
        head = mod.split(".")[0]
        assert head not in _BANNED_IMPORT_HEADS, f"{relpath} imports {mod}"
        for pref in _BANNED_IMPORT_PREFIXES:
            assert not (mod == pref or mod.startswith(pref + ".")), (
                f"{relpath} imports {mod}"
            )
    for c in calls:
        assert c not in _BANNED_CALLS, f"{relpath} calls {c}()"


# ──────────────────────────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────────────────────────

_RUNNER = _REPO_ROOT / "scripts" / "pas201_build_simulation_evidence_digest.py"


def _run_cli(*argv):
    return subprocess.run(
        [sys.executable, str(_RUNNER), *argv],
        cwd=str(_REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=300,
    )


def _write_chain_files(tp: pathlib.Path,
                       *, mutate: Optional[dict] = None) -> dict:
    rec, rev, pkg, rt, insp, beh = _clean_chain()
    if mutate:
        if "package_recommendation_id" in mutate:
            pkg = dict(pkg)
            pkg["recommendation_id"] = mutate["package_recommendation_id"]
    paths = {}
    for name, payload in (
        ("rec.json", rec), ("rev.json", rev), ("pkg.json", pkg),
        ("rt.json",  rt),  ("insp.json", insp), ("beh.json", beh),
    ):
        fp = tp / name
        fp.write_text(json.dumps(payload), encoding="utf-8")
        paths[name] = fp
    return paths


def test_runner_writes_digest_on_happy_path():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        paths = _write_chain_files(tp)
        proc = _run_cli(
            "--recommendation",        str(paths["rec.json"]),
            "--review",                str(paths["rev.json"]),
            "--package",               str(paths["pkg.json"]),
            "--runtime",               str(paths["rt.json"]),
            "--inspection",            str(paths["insp.json"]),
            "--behavioral-evaluation", str(paths["beh.json"]),
            "--output-dir",            str(tp),
        )
        assert proc.returncode == 0, proc.stdout + proc.stderr
        files = list(tp.glob("pas201_simulation_evidence_digest_*.json"))
        assert len(files) == 1
        payload = json.loads(files[0].read_text(encoding="utf-8"))
        for k in DIGEST_REQUIRED_KEYS:
            assert k in payload
        assert payload["allowed_environment"] == "SIMULATION_ONLY"
        assert payload["live_behavior_changed"] is False
        assert payload["phase"] == "PAS201"


def test_runner_summary_only_does_not_write_file():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        paths = _write_chain_files(tp)
        proc = _run_cli(
            "--recommendation",        str(paths["rec.json"]),
            "--review",                str(paths["rev.json"]),
            "--package",               str(paths["pkg.json"]),
            "--runtime",               str(paths["rt.json"]),
            "--inspection",            str(paths["insp.json"]),
            "--behavioral-evaluation", str(paths["beh.json"]),
            "--output-dir",            str(tp),
            "--summary-only",
        )
        assert proc.returncode == 0, proc.stdout + proc.stderr
        files = list(tp.glob("pas201_simulation_evidence_digest_*.json"))
        assert files == []


def test_runner_missing_runtime_exits_2():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        paths = _write_chain_files(tp)
        proc = _run_cli(
            "--recommendation",        str(paths["rec.json"]),
            "--review",                str(paths["rev.json"]),
            "--package",               str(paths["pkg.json"]),
            "--inspection",            str(paths["insp.json"]),
            "--behavioral-evaluation", str(paths["beh.json"]),
            "--output-dir",            str(tp),
            "--summary-only",
        )
        assert proc.returncode == 2


def test_runner_broken_lineage_exits_2():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        paths = _write_chain_files(
            tp,
            mutate={"package_recommendation_id": "pas195-rec-other"},
        )
        proc = _run_cli(
            "--recommendation",        str(paths["rec.json"]),
            "--review",                str(paths["rev.json"]),
            "--package",               str(paths["pkg.json"]),
            "--runtime",               str(paths["rt.json"]),
            "--inspection",            str(paths["insp.json"]),
            "--behavioral-evaluation", str(paths["beh.json"]),
            "--output-dir",            str(tp),
            "--summary-only",
        )
        assert proc.returncode == 2


# ──────────────────────────────────────────────────────────────────
# Readiness gate
# ──────────────────────────────────────────────────────────────────

_GATE = _REPO_ROOT / "scripts" / "pas201_evidence_digest_readiness_check.py"


def test_readiness_gate_runs_clean_summary_only():
    proc = subprocess.run(
        [sys.executable, str(_GATE), "--summary-only"],
        cwd=str(_REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=300,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "verdict=READY" in proc.stdout


def test_readiness_gate_json_envelope_valid():
    proc = subprocess.run(
        [sys.executable, str(_GATE), "--summary-only", "--json"],
        cwd=str(_REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=300,
    )
    assert proc.returncode == 0
    payload_str = proc.stdout[proc.stdout.find("{"):]
    payload = json.loads(payload_str)
    assert payload["phase"] == "PAS201"
    assert payload["verdict"] == "READY"
    assert payload["ready"] is True
    assert payload["fail_count"] == 0
    assert payload["check_count"] > 0


# ──────────────────────────────────────────────────────────────────
# Doc invariants
# ──────────────────────────────────────────────────────────────────

def test_doc_present_and_carries_required_clauses():
    doc = _read("docs/pas201_simulation_evidence_digest.md").lower()
    for clause in (
        "what pas201 proves",
        "what pas201 does not prove",
        "claimable",
        "still not claimable",
        "future pas202",
        "digest",
        "evidence",
        "operator",
        "safety",
        "simulation_only",
        "demo",
        "investor",
    ):
        assert clause in doc, f"doc missing clause {clause!r}"
