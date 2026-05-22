"""
PAS199 — Operational runtime inspection tests.

Coverage:

  * Happy path:
      - valid four-artefact lineage produces an inspection with
        every required key
      - inspection_id deterministic for fixed inputs
      - inspection_id changes when any of its hash inputs change
      - allowed_environment == "SIMULATION_ONLY"
      - live_behavior_changed is False
      - lineage_summary carries every key
      - runtime_summary / safety_summary / capability_summary /
        transcript_summary / artifact_integrity all carry every
        required key
      - artifact_integrity is all-True on a clean lineage

  * Broken-lineage rejection:
      - review.recommendation_id mismatch rejected
      - package.recommendation_id mismatch rejected
      - package.review_id mismatch rejected
      - package.strategy_id != recommendation.recommended_strategy
        rejected
      - runtime.package_id mismatch rejected
      - runtime.executed_strategy mismatch rejected
      - recommendation.status != CANDIDATE rejected
      - review.new_status != APPROVED_FOR_MANUAL_TEST rejected
      - review.live_behavior_changed != False rejected
      - package.status != READY_FOR_MANUAL_TEST rejected
      - package.allowed_environment != SIMULATION_ONLY rejected
      - package.live_behavior_changed != False rejected
      - runtime.status != EXECUTED rejected
      - runtime.allowed_environment != SIMULATION_ONLY rejected
      - runtime.live_behavior_changed != False rejected
      - missing required keys rejected
      - blank generated_at rejected

  * Transcript replay:
      - replay_transcript returns the bounded record shape
      - replay is deterministic (same runtime -> same replay)
      - replay refuses unknown scenario_ids
      - replay sequence_ids strictly increasing from 1
      - replay actors in closed vocab
      - replay capability markers in closed vocab
      - replay safety markers in closed vocab

  * Runtime comparison:
      - same runtime compared with itself -> zero deltas
      - comparison deterministic
      - comparison rejects non-EXECUTED / non-SIMULATION_ONLY
        runtimes
      - comparison surfaces flipped scenarios

  * Source-surface invariants:
      - no forbidden status literals
      - no live-mutation identifiers
      - no banned imports
      - no free-form operator notes

  * CLI:
      - happy-path writes inspection
      - --summary-only suppresses file write
      - missing --runtime exits 2
      - mismatched lineage exits 2
      - --compare-runtime path supplied

  * Readiness gate:
      - exit 0 / verdict=READY
      - JSON envelope valid

  * Carry-forward:
      - PAS193..PAS198 tests still pass
"""

from __future__ import annotations

import ast
import json
import pathlib
import re
import subprocess
import sys
import tempfile

import pytest


_REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))


from app.services.simulation.runtime_inspection import (  # noqa: E402
    ACTORS,
    ARTIFACT_INTEGRITY_KEYS,
    CAPABILITY_MARKERS,
    CAPABILITY_SUMMARY_KEYS,
    COMPARISON_KEYS,
    INSPECTION_ENVIRONMENT_SIMULATION_ONLY,
    INSPECTION_REQUIRED_KEYS,
    LINEAGE_SUMMARY_KEYS,
    REPLAY_KEYS,
    RUNTIME_SUMMARY_KEYS,
    RuntimeInspectionValidationError,
    SAFETY_MARKERS,
    SAFETY_SUMMARY_KEYS,
    TRANSCRIPT_SUMMARY_KEYS,
    build_inspection,
    compare_runtimes,
    replay_transcript,
)
from app.services.simulation.manual_test_runtime import (  # noqa: E402
    execute_manual_test_runtime,
)


def _read(relpath: str) -> str:
    return (_REPO_ROOT / relpath).read_text(encoding="utf-8")


# ──────────────────────────────────────────────────────────────────
# Synthetic four-artefact lineage
# ──────────────────────────────────────────────────────────────────

REC_ID      = "pas195-rec-9a9566a11d621684"
REVIEW_ID   = "pas196-rev-deadbeefcafebabe"
PACKAGE_ID  = "pas197-pkg-2b7c50e63bf5fb88"
STRATEGY_ID = "callback_first"
GEN_AT      = "2026-05-22T05:00:00Z"


def _candidate_recommendation(
    rec_id: str = REC_ID,
    strategy: str = STRATEGY_ID,
) -> dict:
    return {
        "recommendation_id":    rec_id,
        "status":               "CANDIDATE",
        "operator_required":    True,
        "recommended_strategy": strategy,
        "phase":                "PAS195",
    }


def _approved_review(
    rec_id: str = REC_ID,
    review_id: str = REVIEW_ID,
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
    rec_id: str = REC_ID,
    review_id: str = REVIEW_ID,
    package_id: str = PACKAGE_ID,
    strategy_id: str = STRATEGY_ID,
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


def _executed_runtime(
    package_id: str = PACKAGE_ID,
    strategy_id: str = STRATEGY_ID,
) -> dict:
    pkg = _ready_package(package_id=package_id, strategy_id=strategy_id)
    return execute_manual_test_runtime(
        pkg, created_at="2026-05-22T04:00:00Z",
    )


# ──────────────────────────────────────────────────────────────────
# Happy path
# ──────────────────────────────────────────────────────────────────

def test_inspection_built_from_clean_lineage():
    insp = build_inspection(
        _candidate_recommendation(),
        _approved_review(),
        _ready_package(),
        _executed_runtime(),
        generated_at=GEN_AT,
    )
    assert isinstance(insp, dict)


def test_inspection_carries_every_required_key():
    insp = build_inspection(
        _candidate_recommendation(),
        _approved_review(),
        _ready_package(),
        _executed_runtime(),
        generated_at=GEN_AT,
    )
    for k in INSPECTION_REQUIRED_KEYS:
        assert k in insp, f"missing {k}"


def test_inspection_environment_is_simulation_only():
    insp = build_inspection(
        _candidate_recommendation(),
        _approved_review(),
        _ready_package(),
        _executed_runtime(),
        generated_at=GEN_AT,
    )
    assert insp["allowed_environment"] == INSPECTION_ENVIRONMENT_SIMULATION_ONLY
    assert insp["allowed_environment"] == "SIMULATION_ONLY"


def test_inspection_live_behavior_changed_is_false():
    insp = build_inspection(
        _candidate_recommendation(),
        _approved_review(),
        _ready_package(),
        _executed_runtime(),
        generated_at=GEN_AT,
    )
    assert insp["live_behavior_changed"] is False


def test_inspection_id_deterministic_for_same_inputs():
    a = build_inspection(
        _candidate_recommendation(),
        _approved_review(),
        _ready_package(),
        _executed_runtime(),
        generated_at=GEN_AT,
    )
    b = build_inspection(
        _candidate_recommendation(),
        _approved_review(),
        _ready_package(),
        _executed_runtime(),
        generated_at=GEN_AT,
    )
    assert a == b


def test_inspection_id_changes_with_compare_runtime():
    base = build_inspection(
        _candidate_recommendation(),
        _approved_review(),
        _ready_package(),
        _executed_runtime(),
        generated_at=GEN_AT,
    )
    other_runtime = _executed_runtime(
        package_id="pas197-pkg-2b7c50e63bf5fb88",
        strategy_id="balanced",
    )
    # build a matching package + recommendation for that other runtime
    other_pkg = _ready_package(strategy_id="balanced")
    other_rec = _candidate_recommendation(strategy="balanced")
    other_run = execute_manual_test_runtime(
        other_pkg, created_at="2026-05-22T04:00:00Z",
    )
    with_compare = build_inspection(
        other_rec, _approved_review(), other_pkg, other_run,
        generated_at=GEN_AT,
        compare_runtime=other_runtime,
    )
    assert with_compare["inspection_id"] != base["inspection_id"]


def test_inspection_id_carries_pas199_prefix():
    insp = build_inspection(
        _candidate_recommendation(),
        _approved_review(),
        _ready_package(),
        _executed_runtime(),
        generated_at=GEN_AT,
    )
    assert insp["inspection_id"].startswith("pas199-insp-")


def test_lineage_summary_keys_present():
    insp = build_inspection(
        _candidate_recommendation(),
        _approved_review(),
        _ready_package(),
        _executed_runtime(),
        generated_at=GEN_AT,
    )
    for k in LINEAGE_SUMMARY_KEYS:
        assert k in insp["lineage_summary"]
    assert insp["lineage_summary"]["lineage_intact"] is True
    assert insp["lineage_summary"]["strategy_id"] == STRATEGY_ID


def test_runtime_summary_keys_present():
    insp = build_inspection(
        _candidate_recommendation(),
        _approved_review(),
        _ready_package(),
        _executed_runtime(),
        generated_at=GEN_AT,
    )
    for k in RUNTIME_SUMMARY_KEYS:
        assert k in insp["runtime_summary"]


def test_safety_summary_keys_present():
    insp = build_inspection(
        _candidate_recommendation(),
        _approved_review(),
        _ready_package(),
        _executed_runtime(),
        generated_at=GEN_AT,
    )
    for k in SAFETY_SUMMARY_KEYS:
        assert k in insp["safety_summary"]


def test_capability_summary_keys_present():
    insp = build_inspection(
        _candidate_recommendation(),
        _approved_review(),
        _ready_package(),
        _executed_runtime(),
        generated_at=GEN_AT,
    )
    for k in CAPABILITY_SUMMARY_KEYS:
        assert k in insp["capability_summary"]


def test_transcript_summary_keys_present():
    insp = build_inspection(
        _candidate_recommendation(),
        _approved_review(),
        _ready_package(),
        _executed_runtime(),
        generated_at=GEN_AT,
    )
    for k in TRANSCRIPT_SUMMARY_KEYS:
        assert k in insp["transcript_summary"]
    assert insp["transcript_summary"]["scenario_count"] > 0
    assert insp["transcript_summary"]["total_turns"] > 0


def test_artifact_integrity_all_true_on_clean_lineage():
    insp = build_inspection(
        _candidate_recommendation(),
        _approved_review(),
        _ready_package(),
        _executed_runtime(),
        generated_at=GEN_AT,
    )
    integ = insp["artifact_integrity"]
    for k in ARTIFACT_INTEGRITY_KEYS:
        assert k in integ, f"integrity missing {k}"
        assert integ[k] is True, f"integrity check {k} unexpectedly False"


def test_comparison_null_without_compare_runtime():
    insp = build_inspection(
        _candidate_recommendation(),
        _approved_review(),
        _ready_package(),
        _executed_runtime(),
        generated_at=GEN_AT,
    )
    assert insp["comparison"] is None


# ──────────────────────────────────────────────────────────────────
# Broken-lineage rejection
# ──────────────────────────────────────────────────────────────────

def test_review_recommendation_id_mismatch_rejected():
    rev = _approved_review(rec_id="pas195-rec-other")
    with pytest.raises(RuntimeInspectionValidationError):
        build_inspection(
            _candidate_recommendation(), rev,
            _ready_package(), _executed_runtime(),
            generated_at=GEN_AT,
        )


def test_package_recommendation_id_mismatch_rejected():
    pkg = _ready_package(rec_id="pas195-rec-other")
    with pytest.raises(RuntimeInspectionValidationError):
        build_inspection(
            _candidate_recommendation(), _approved_review(),
            pkg, _executed_runtime(),
            generated_at=GEN_AT,
        )


def test_package_review_id_mismatch_rejected():
    pkg = _ready_package(review_id="pas196-rev-other")
    with pytest.raises(RuntimeInspectionValidationError):
        build_inspection(
            _candidate_recommendation(), _approved_review(),
            pkg, _executed_runtime(),
            generated_at=GEN_AT,
        )


def test_package_strategy_id_mismatch_rejected():
    pkg = _ready_package(strategy_id="balanced")
    with pytest.raises(RuntimeInspectionValidationError):
        build_inspection(
            _candidate_recommendation(strategy="callback_first"),
            _approved_review(), pkg, _executed_runtime(),
            generated_at=GEN_AT,
        )


def test_runtime_package_id_mismatch_rejected():
    rt = _executed_runtime(package_id="pas197-pkg-different")
    with pytest.raises(RuntimeInspectionValidationError):
        build_inspection(
            _candidate_recommendation(), _approved_review(),
            _ready_package(), rt, generated_at=GEN_AT,
        )


def test_runtime_executed_strategy_mismatch_rejected():
    pkg = _ready_package(strategy_id="callback_first")
    rt = _executed_runtime(strategy_id="balanced")
    with pytest.raises(RuntimeInspectionValidationError):
        build_inspection(
            _candidate_recommendation(strategy="callback_first"),
            _approved_review(), pkg, rt, generated_at=GEN_AT,
        )


@pytest.mark.parametrize("bad_status", ["REJECTED", "EXPIRED",
                                        "APPROVED_FOR_MANUAL_TEST"])
def test_recommendation_status_not_candidate_rejected(bad_status):
    rec = _candidate_recommendation()
    rec["status"] = bad_status
    with pytest.raises(RuntimeInspectionValidationError):
        build_inspection(
            rec, _approved_review(), _ready_package(),
            _executed_runtime(), generated_at=GEN_AT,
        )


@pytest.mark.parametrize("bad_status", ["REJECTED", "EXPIRED", "CANDIDATE"])
def test_review_new_status_not_approved_rejected(bad_status):
    rev = _approved_review()
    rev["new_status"] = bad_status
    with pytest.raises(RuntimeInspectionValidationError):
        build_inspection(
            _candidate_recommendation(), rev, _ready_package(),
            _executed_runtime(), generated_at=GEN_AT,
        )


def test_review_live_behavior_changed_true_rejected():
    rev = _approved_review()
    rev["live_behavior_changed"] = True
    with pytest.raises(RuntimeInspectionValidationError):
        build_inspection(
            _candidate_recommendation(), rev, _ready_package(),
            _executed_runtime(), generated_at=GEN_AT,
        )


@pytest.mark.parametrize("bad_status", ["CANDIDATE", "REJECTED", "EXECUTED"])
def test_package_status_rejected(bad_status):
    pkg = _ready_package()
    pkg["status"] = bad_status
    with pytest.raises(RuntimeInspectionValidationError):
        build_inspection(
            _candidate_recommendation(), _approved_review(),
            pkg, _executed_runtime(), generated_at=GEN_AT,
        )


def test_package_environment_rejected():
    pkg = _ready_package()
    pkg["allowed_environment"] = "PRODUCTION"
    with pytest.raises(RuntimeInspectionValidationError):
        build_inspection(
            _candidate_recommendation(), _approved_review(),
            pkg, _executed_runtime(), generated_at=GEN_AT,
        )


def test_package_live_behavior_changed_true_rejected():
    pkg = _ready_package()
    pkg["live_behavior_changed"] = True
    with pytest.raises(RuntimeInspectionValidationError):
        build_inspection(
            _candidate_recommendation(), _approved_review(),
            pkg, _executed_runtime(), generated_at=GEN_AT,
        )


@pytest.mark.parametrize("bad_status", ["READY_FOR_MANUAL_TEST",
                                        "CANDIDATE", "REJECTED"])
def test_runtime_status_rejected(bad_status):
    rt = _executed_runtime()
    rt["status"] = bad_status
    with pytest.raises(RuntimeInspectionValidationError):
        build_inspection(
            _candidate_recommendation(), _approved_review(),
            _ready_package(), rt, generated_at=GEN_AT,
        )


def test_runtime_environment_rejected():
    rt = _executed_runtime()
    rt["allowed_environment"] = "PRODUCTION"
    with pytest.raises(RuntimeInspectionValidationError):
        build_inspection(
            _candidate_recommendation(), _approved_review(),
            _ready_package(), rt, generated_at=GEN_AT,
        )


def test_runtime_live_behavior_changed_true_rejected():
    rt = _executed_runtime()
    rt["live_behavior_changed"] = True
    with pytest.raises(RuntimeInspectionValidationError):
        build_inspection(
            _candidate_recommendation(), _approved_review(),
            _ready_package(), rt, generated_at=GEN_AT,
        )


def test_missing_required_key_in_recommendation_rejected():
    rec = _candidate_recommendation()
    del rec["recommended_strategy"]
    with pytest.raises(RuntimeInspectionValidationError):
        build_inspection(
            rec, _approved_review(), _ready_package(),
            _executed_runtime(), generated_at=GEN_AT,
        )


def test_missing_required_key_in_runtime_rejected():
    rt = _executed_runtime()
    del rt["runtime_score"]
    with pytest.raises(RuntimeInspectionValidationError):
        build_inspection(
            _candidate_recommendation(), _approved_review(),
            _ready_package(), rt, generated_at=GEN_AT,
        )


def test_blank_generated_at_rejected():
    with pytest.raises(RuntimeInspectionValidationError):
        build_inspection(
            _candidate_recommendation(), _approved_review(),
            _ready_package(), _executed_runtime(),
            generated_at="",
        )


# ──────────────────────────────────────────────────────────────────
# Transcript replay
# ──────────────────────────────────────────────────────────────────

def test_replay_returns_bounded_shape():
    rt = _executed_runtime()
    sid = rt["transcript_bundle"][0]["scenario_id"]
    replay = replay_transcript(rt, sid)
    for k in REPLAY_KEYS:
        assert k in replay


def test_replay_is_deterministic():
    rt = _executed_runtime()
    sid = rt["transcript_bundle"][0]["scenario_id"]
    a = replay_transcript(rt, sid)
    b = replay_transcript(rt, sid)
    assert a == b


def test_replay_unknown_scenario_rejected():
    rt = _executed_runtime()
    with pytest.raises(RuntimeInspectionValidationError):
        replay_transcript(rt, "pas999_made_up")


def test_replay_sequence_ids_strictly_increasing_from_one():
    rt = _executed_runtime()
    for entry in rt["transcript_bundle"]:
        sid = entry["scenario_id"]
        replay = replay_transcript(rt, sid)
        seq = replay["sequence_ids"]
        for idx, n in enumerate(seq):
            assert n == idx + 1, sid


def test_replay_actors_in_closed_vocab():
    rt = _executed_runtime()
    for entry in rt["transcript_bundle"]:
        replay = replay_transcript(rt, entry["scenario_id"])
        for a in replay["actors"]:
            assert a in ACTORS


def test_replay_capability_markers_in_closed_vocab():
    rt = _executed_runtime()
    for entry in rt["transcript_bundle"]:
        replay = replay_transcript(rt, entry["scenario_id"])
        for turn_markers in replay["capability_markers"]:
            for m in turn_markers:
                assert m in CAPABILITY_MARKERS


def test_replay_safety_markers_in_closed_vocab():
    rt = _executed_runtime()
    for entry in rt["transcript_bundle"]:
        replay = replay_transcript(rt, entry["scenario_id"])
        for turn_markers in replay["safety_markers"]:
            for m in turn_markers:
                assert m in SAFETY_MARKERS


# ──────────────────────────────────────────────────────────────────
# Runtime comparison
# ──────────────────────────────────────────────────────────────────

def test_compare_runtime_with_itself_zero_deltas():
    rt = _executed_runtime()
    cmp = compare_runtimes(rt, rt)
    for k in COMPARISON_KEYS:
        assert k in cmp
    assert cmp["pass_rate_delta"]     == 0.0
    assert cmp["average_score_delta"] == 0.0
    for v in cmp["capability_delta"].values():
        assert v == 0.0
    assert cmp["safety_delta"]["auto_fail_count_delta"] == 0
    assert cmp["safety_delta"]["outcome_changed"]       is False
    assert cmp["transcript_size_delta"]["total_turns_delta"]    == 0
    assert cmp["transcript_size_delta"]["scenario_count_delta"] == 0
    assert cmp["flipped_scenarios"] == []


def test_compare_is_deterministic():
    rt = _executed_runtime()
    a = compare_runtimes(rt, rt)
    b = compare_runtimes(rt, rt)
    assert a == b


def test_compare_rejects_non_executed_runtime():
    rt_a = _executed_runtime()
    rt_b = _executed_runtime()
    rt_b["status"] = "CANDIDATE"
    with pytest.raises(RuntimeInspectionValidationError):
        compare_runtimes(rt_a, rt_b)


def test_compare_rejects_wrong_environment():
    rt_a = _executed_runtime()
    rt_b = _executed_runtime()
    rt_b["allowed_environment"] = "PRODUCTION"
    with pytest.raises(RuntimeInspectionValidationError):
        compare_runtimes(rt_a, rt_b)


def test_compare_rejects_live_behavior_changed_true():
    rt_a = _executed_runtime()
    rt_b = _executed_runtime()
    rt_b["live_behavior_changed"] = True
    with pytest.raises(RuntimeInspectionValidationError):
        compare_runtimes(rt_a, rt_b)


def test_compare_surfaces_flipped_scenarios():
    rt_a = _executed_runtime()
    rt_b = _executed_runtime()
    # Flip one scenario's passed flag in rt_b.
    rt_b["runtime_score"]["per_scenario"][0]["passed"] = (
        not rt_b["runtime_score"]["per_scenario"][0]["passed"]
    )
    cmp = compare_runtimes(rt_a, rt_b)
    sids = [f["scenario_id"] for f in cmp["flipped_scenarios"]]
    assert rt_b["runtime_score"]["per_scenario"][0]["scenario_id"] in sids


def test_compare_records_capability_deltas():
    rt_a = _executed_runtime()
    rt_b = _executed_runtime()
    rt_b["capability_summary"]["callback_captured_rate"] = (
        float(rt_a["capability_summary"]["callback_captured_rate"]) - 0.25
    )
    cmp = compare_runtimes(rt_a, rt_b)
    assert cmp["capability_delta"]["callback_captured_rate"] == -0.25


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


_PAS199_FILES = (
    "app/services/simulation/runtime_inspection.py",
    "scripts/pas199_inspect_runtime_lineage.py",
    "scripts/pas199_runtime_inspection_readiness_check.py",
)


# Forbidden-literal / forbidden-identifier scans exclude the
# readiness gate, which legitimately enumerates these tokens as
# string constants in order to detect them elsewhere.
_PAS199_FILES_FOR_FORBIDDEN_LITERAL_SCAN = (
    "app/services/simulation/runtime_inspection.py",
    "scripts/pas199_inspect_runtime_lineage.py",
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


@pytest.mark.parametrize("relpath", _PAS199_FILES_FOR_FORBIDDEN_LITERAL_SCAN)
def test_forbidden_status_literals_absent(relpath):
    consts = _string_constants(_read(relpath))
    for tok in _FORBIDDEN_STATUS_LITERALS:
        assert tok not in consts, (
            f"{relpath} carries forbidden status literal {tok!r}"
        )


@pytest.mark.parametrize("relpath", _PAS199_FILES_FOR_FORBIDDEN_LITERAL_SCAN)
def test_forbidden_identifiers_absent(relpath):
    names = _identifier_names(_read(relpath))
    for tok in _FORBIDDEN_IDENTIFIERS:
        assert tok not in names, (
            f"{relpath} carries forbidden identifier {tok!r}"
        )


@pytest.mark.parametrize("relpath", _PAS199_FILES)
def test_no_banned_imports_in_pas199_file(relpath):
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
# No live mutation / no PII / no production brokerage ids
# ──────────────────────────────────────────────────────────────────

_PHONE_RES = (
    re.compile(r"\b\d{3}[\s.\-]\d{3}[\s.\-]\d{4}\b"),
    re.compile(r"\(\d{3}\)\s*\d{3}[\s.\-]?\d{4}"),
)

_PROD_ID_RES = (
    re.compile(r"\bbrokerage_id\s*=\s*[\"']?[0-9a-fA-F\-]{8,}[\"']?"),
    re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b"),
)


def test_inspection_carries_no_phone_numbers():
    insp = build_inspection(
        _candidate_recommendation(),
        _approved_review(),
        _ready_package(),
        _executed_runtime(),
        generated_at=GEN_AT,
    )
    text = json.dumps(insp, sort_keys=True)
    for pat in _PHONE_RES:
        assert not pat.search(text), "phone-shaped token in inspection"


def test_inspection_carries_no_production_brokerage_ids():
    insp = build_inspection(
        _candidate_recommendation(),
        _approved_review(),
        _ready_package(),
        _executed_runtime(),
        generated_at=GEN_AT,
    )
    text = json.dumps(insp, sort_keys=True)
    for pat in _PROD_ID_RES:
        assert not pat.search(text), "production brokerage id in inspection"


def test_inspection_carries_no_freeform_text_fields():
    insp = build_inspection(
        _candidate_recommendation(),
        _approved_review(),
        _ready_package(),
        _executed_runtime(),
        generated_at=GEN_AT,
    )
    for forbidden in ("notes", "note", "free_text", "comment",
                      "operator_notes", "operator_comment"):
        assert forbidden not in insp, (
            f"inspection carries forbidden free-form field {forbidden!r}"
        )


def test_inspection_does_not_mutate_inputs():
    rec = _candidate_recommendation()
    rev = _approved_review()
    pkg = _ready_package()
    rt  = _executed_runtime()
    before = (
        json.dumps(rec, sort_keys=True),
        json.dumps(rev, sort_keys=True),
        json.dumps(pkg, sort_keys=True),
        json.dumps(rt,  sort_keys=True),
    )
    build_inspection(rec, rev, pkg, rt, generated_at=GEN_AT)
    after = (
        json.dumps(rec, sort_keys=True),
        json.dumps(rev, sort_keys=True),
        json.dumps(pkg, sort_keys=True),
        json.dumps(rt,  sort_keys=True),
    )
    assert before == after


# ──────────────────────────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────────────────────────

_RUNNER = _REPO_ROOT / "scripts" / "pas199_inspect_runtime_lineage.py"


def _run_cli(*argv):
    return subprocess.run(
        [sys.executable, str(_RUNNER), *argv],
        cwd=str(_REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=300,
    )


def _write_chain(tmp: pathlib.Path,
                 *, mutate_package_rec_id: bool = False) -> dict:
    rec = _candidate_recommendation()
    rev = _approved_review()
    pkg = _ready_package()
    rt  = _executed_runtime()
    if mutate_package_rec_id:
        pkg["recommendation_id"] = "pas195-rec-mismatch"
    paths = {}
    for name, payload in (
        ("rec.json", rec), ("rev.json", rev),
        ("pkg.json", pkg), ("rt.json",  rt),
    ):
        fp = tmp / name
        fp.write_text(json.dumps(payload), encoding="utf-8")
        paths[name] = fp
    return paths


def test_runner_writes_inspection_on_happy_path():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        paths = _write_chain(tp)
        proc = _run_cli(
            "--recommendation", str(paths["rec.json"]),
            "--review",         str(paths["rev.json"]),
            "--package",        str(paths["pkg.json"]),
            "--runtime",        str(paths["rt.json"]),
            "--output-dir",     str(tp),
        )
        assert proc.returncode == 0, proc.stdout + proc.stderr
        files = list(tp.glob("pas199_runtime_inspection_*.json"))
        assert len(files) == 1
        payload = json.loads(files[0].read_text(encoding="utf-8"))
        for k in INSPECTION_REQUIRED_KEYS:
            assert k in payload
        assert payload["allowed_environment"] == "SIMULATION_ONLY"
        assert payload["live_behavior_changed"] is False


def test_runner_summary_only_does_not_write_file():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        paths = _write_chain(tp)
        proc = _run_cli(
            "--recommendation", str(paths["rec.json"]),
            "--review",         str(paths["rev.json"]),
            "--package",        str(paths["pkg.json"]),
            "--runtime",        str(paths["rt.json"]),
            "--output-dir",     str(tp),
            "--summary-only",
        )
        assert proc.returncode == 0, proc.stdout + proc.stderr
        files = list(tp.glob("pas199_runtime_inspection_*.json"))
        assert files == []


def test_runner_missing_runtime_exits_2():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        paths = _write_chain(tp)
        proc = _run_cli(
            "--recommendation", str(paths["rec.json"]),
            "--review",         str(paths["rev.json"]),
            "--package",        str(paths["pkg.json"]),
            "--output-dir",     str(tp),
            "--summary-only",
        )
        assert proc.returncode == 2


def test_runner_broken_lineage_exits_2():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        paths = _write_chain(tp, mutate_package_rec_id=True)
        proc = _run_cli(
            "--recommendation", str(paths["rec.json"]),
            "--review",         str(paths["rev.json"]),
            "--package",        str(paths["pkg.json"]),
            "--runtime",        str(paths["rt.json"]),
            "--output-dir",     str(tp),
            "--summary-only",
        )
        assert proc.returncode == 2


def test_runner_with_compare_runtime():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        paths = _write_chain(tp)
        # Use the same runtime as compare target.
        cmp_path = tp / "rt_b.json"
        cmp_path.write_text(
            (tp / "rt.json").read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        proc = _run_cli(
            "--recommendation",   str(paths["rec.json"]),
            "--review",           str(paths["rev.json"]),
            "--package",          str(paths["pkg.json"]),
            "--runtime",          str(paths["rt.json"]),
            "--compare-runtime",  str(cmp_path),
            "--output-dir",       str(tp),
            "--summary-only",
        )
        assert proc.returncode == 0, proc.stdout + proc.stderr
        assert "comparison" in proc.stdout


# ──────────────────────────────────────────────────────────────────
# Readiness gate
# ──────────────────────────────────────────────────────────────────

_GATE = _REPO_ROOT / "scripts" / "pas199_runtime_inspection_readiness_check.py"


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
    assert payload["phase"] == "PAS199"
    assert payload["verdict"] == "READY"
    assert payload["ready"] is True
    assert payload["fail_count"] == 0
    assert payload["check_count"] > 0


# ──────────────────────────────────────────────────────────────────
# Carry-forward
# ──────────────────────────────────────────────────────────────────

def test_pas193_to_pas198_tests_still_pass():
    proc = subprocess.run(
        [
            sys.executable, "-m", "pytest",
            "tests/mvp/test_pas193_simulation_layer.py",
            "tests/mvp/test_pas194_strategy_comparison.py",
            "tests/mvp/test_pas195_simulation_recommendations.py",
            "tests/mvp/test_pas196_simulation_recommendation_review.py",
            "tests/mvp/test_pas197_manual_test_package.py",
            "tests/mvp/test_pas198_manual_test_runtime.py",
            "-q",
        ],
        cwd=str(_REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=900,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr


# ──────────────────────────────────────────────────────────────────
# Doc invariants
# ──────────────────────────────────────────────────────────────────

def test_doc_present_and_carries_required_clauses():
    doc = _read("docs/pas199_runtime_inspection.md").lower()
    for clause in (
        "what pas199 proves",
        "what pas199 does not prove",
        "claimable",
        "still not claimable",
        "future pas200",
        "lineage",
        "runtime",
        "inspection",
        "operator",
        "safety",
        "simulation_only",
    ):
        assert clause in doc, f"doc missing clause {clause!r}"
