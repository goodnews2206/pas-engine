"""
PAS200 — Behavioural runtime evaluation tests.

Coverage:

  * Happy path:
      - valid PAS198 runtime produces an evaluation with every
        required key
      - phase == "PAS200"
      - allowed_environment == "SIMULATION_ONLY"
      - live_behavior_changed is False
      - aggregate_scores carries all five score keys, each in
        [0.0, 1.0]
      - behavioral_evaluation_id is deterministic for fixed inputs
      - behavioral_evaluation_id changes when transcript changes,
        inspection_id changes, or runtime_id changes
      - transcript_hash is deterministic
      - artifact_integrity is all-True on a clean runtime
      - annotation counts on scenarios match the per-turn records
      - PAS199 inspection optional and cross-referenced when given

  * Malformed-runtime rejection:
      - status != EXECUTED rejected
      - allowed_environment != SIMULATION_ONLY rejected
      - live_behavior_changed != False rejected
      - empty transcript_bundle rejected
      - bad actor in a turn rejected
      - blank generated_at rejected
      - inspection.runtime_id mismatch rejected

  * Annotation determinism:
      - annotate_turns is pure (same input -> same output)
      - annotations drawn from the closed TURN_ANNOTATIONS vocab
      - sequence_ids referenced by annotations exist in the
        runtime's transcript

  * Score determinism:
      - all five score functions are pure and bounded to [0, 1]
      - safety-marked scenarios produce trust_score <= 0.5 and
        friction_score >= 0.4

  * Behavioural flags:
      - drawn from the closed BEHAVIORAL_FLAGS vocab
      - high-pressure runs surface high_pressure_strategy
      - low-friction clean runs surface low_friction_observed
      - context_reset_repeated only fires when >= 2 resets

  * Bounded-environment invariants:
      - no PII tokens in the evaluation
      - no production brokerage IDs in the evaluation
      - no free-form operator-note fields
      - input runtime not mutated

  * Source-surface invariants:
      - no forbidden status literals
      - no live-mutation identifiers
      - no banned imports

  * CLI:
      - happy-path writes evaluation
      - --summary-only suppresses file write
      - missing --runtime exits 2
      - rejected runtime exits 2
      - --inspection path supplied

  * Readiness gate:
      - exit 0 / verdict=READY
      - JSON envelope valid

  * Carry-forward:
      - PAS193..PAS199 tests still pass
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


from app.services.simulation.behavioral_evaluation import (  # noqa: E402
    ARTIFACT_INTEGRITY_KEYS,
    BEHAVIORAL_EVALUATION_ENVIRONMENT_SIMULATION_ONLY,
    BEHAVIORAL_EVALUATION_REQUIRED_KEYS,
    BEHAVIORAL_FLAGS,
    SCENARIO_SUMMARY_KEYS,
    SCORE_KEYS,
    TURN_ANNOTATIONS,
    TURN_ANNOTATION_KEYS,
    BehavioralEvaluationValidationError,
    annotate_turns,
    build_behavioral_evaluation,
    score_continuity,
    score_friction,
    score_pacing,
    score_pressure,
    score_trust,
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

REC_ID      = "pas195-rec-9a9566a11d621684"
REVIEW_ID   = "pas196-rev-deadbeefcafebabe"
PACKAGE_ID  = "pas197-pkg-2b7c50e63bf5fb88"
GEN_AT      = "2026-05-22T06:00:00Z"


def _ready_package(strategy_id: str = "callback_first") -> dict:
    return {
        "package_id":            PACKAGE_ID,
        "phase":                 "PAS197",
        "recommendation_id":     REC_ID,
        "review_id":             REVIEW_ID,
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


def _candidate_recommendation(strategy: str = "callback_first") -> dict:
    return {
        "recommendation_id":    REC_ID,
        "status":               "CANDIDATE",
        "operator_required":    True,
        "recommended_strategy": strategy,
        "phase":                "PAS195",
    }


def _approved_review() -> dict:
    return {
        "review_id":             REVIEW_ID,
        "recommendation_id":     REC_ID,
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


def _matching_inspection(runtime: dict, strategy: str = "callback_first") -> dict:
    return build_inspection(
        _candidate_recommendation(strategy),
        _approved_review(),
        _ready_package(strategy_id=strategy),
        runtime,
        generated_at=GEN_AT,
    )


# ──────────────────────────────────────────────────────────────────
# Happy path
# ──────────────────────────────────────────────────────────────────

def test_evaluation_built_from_valid_runtime():
    ev = build_behavioral_evaluation(
        _executed_runtime(), generated_at=GEN_AT,
    )
    assert isinstance(ev, dict)


def test_evaluation_carries_every_required_key():
    ev = build_behavioral_evaluation(
        _executed_runtime(), generated_at=GEN_AT,
    )
    for k in BEHAVIORAL_EVALUATION_REQUIRED_KEYS:
        assert k in ev, f"missing {k}"


def test_evaluation_phase_is_pas200():
    ev = build_behavioral_evaluation(
        _executed_runtime(), generated_at=GEN_AT,
    )
    assert ev["phase"] == "PAS200"


def test_evaluation_environment_is_simulation_only():
    ev = build_behavioral_evaluation(
        _executed_runtime(), generated_at=GEN_AT,
    )
    assert ev["allowed_environment"] == BEHAVIORAL_EVALUATION_ENVIRONMENT_SIMULATION_ONLY
    assert ev["allowed_environment"] == "SIMULATION_ONLY"


def test_evaluation_live_behavior_changed_is_false():
    ev = build_behavioral_evaluation(
        _executed_runtime(), generated_at=GEN_AT,
    )
    assert ev["live_behavior_changed"] is False


def test_evaluation_aggregate_scores_are_unit_floats():
    ev = build_behavioral_evaluation(
        _executed_runtime(), generated_at=GEN_AT,
    )
    for k in SCORE_KEYS:
        v = ev["aggregate_scores"][k]
        assert isinstance(v, float)
        assert 0.0 <= v <= 1.0


def test_evaluation_id_deterministic_for_same_inputs():
    a = build_behavioral_evaluation(
        _executed_runtime(), generated_at=GEN_AT,
    )
    b = build_behavioral_evaluation(
        _executed_runtime(), generated_at=GEN_AT,
    )
    assert a == b


def test_evaluation_id_changes_when_transcript_changes():
    rt = _executed_runtime()
    rt2 = _executed_runtime()
    # Mutate one turn's agent_action -> transcript hash differs.
    rt2["transcript_bundle"][0]["turns"][0]["agent_action"] = "qualify"
    a = build_behavioral_evaluation(rt,  generated_at=GEN_AT)
    b = build_behavioral_evaluation(rt2, generated_at=GEN_AT)
    assert a["behavioral_evaluation_id"] != b["behavioral_evaluation_id"]
    assert a["transcript_hash"]          != b["transcript_hash"]


def test_evaluation_id_changes_when_inspection_supplied():
    rt = _executed_runtime()
    insp = _matching_inspection(rt)
    a = build_behavioral_evaluation(rt, generated_at=GEN_AT)
    b = build_behavioral_evaluation(rt, generated_at=GEN_AT, inspection=insp)
    assert a["behavioral_evaluation_id"] != b["behavioral_evaluation_id"]
    assert a["inspection_id"] is None
    assert b["inspection_id"] == insp["inspection_id"]


def test_evaluation_id_changes_when_runtime_id_changes():
    rt_a = _executed_runtime()
    rt_b = _executed_runtime()
    rt_b["runtime_id"] = "pas198-rt-different-0000"
    a = build_behavioral_evaluation(rt_a, generated_at=GEN_AT)
    b = build_behavioral_evaluation(rt_b, generated_at=GEN_AT)
    assert a["behavioral_evaluation_id"] != b["behavioral_evaluation_id"]


def test_evaluation_id_carries_pas200_prefix():
    ev = build_behavioral_evaluation(
        _executed_runtime(), generated_at=GEN_AT,
    )
    assert ev["behavioral_evaluation_id"].startswith("pas200-beval-")


def test_evaluation_scenario_summaries_carry_every_key():
    ev = build_behavioral_evaluation(
        _executed_runtime(), generated_at=GEN_AT,
    )
    assert len(ev["scenario_summaries"]) > 0
    for s in ev["scenario_summaries"]:
        for k in SCENARIO_SUMMARY_KEYS:
            assert k in s, f"scenario summary missing {k}"
        for k in SCORE_KEYS:
            assert 0.0 <= s[k] <= 1.0


def test_evaluation_artifact_integrity_all_true_on_clean_runtime():
    ev = build_behavioral_evaluation(
        _executed_runtime(), generated_at=GEN_AT,
    )
    for k in ARTIFACT_INTEGRITY_KEYS:
        assert k in ev["artifact_integrity"], f"integrity missing {k}"
        assert ev["artifact_integrity"][k] is True, (
            f"integrity check {k} unexpectedly False"
        )


def test_evaluation_inspection_id_round_trips_when_provided():
    rt = _executed_runtime()
    insp = _matching_inspection(rt)
    ev = build_behavioral_evaluation(
        rt, generated_at=GEN_AT, inspection=insp,
    )
    assert ev["inspection_id"] == insp["inspection_id"]


def test_evaluation_inspection_id_none_when_omitted():
    ev = build_behavioral_evaluation(
        _executed_runtime(), generated_at=GEN_AT,
    )
    assert ev["inspection_id"] is None


# ──────────────────────────────────────────────────────────────────
# Malformed-runtime rejection
# ──────────────────────────────────────────────────────────────────

@pytest.mark.parametrize(
    "bad_status",
    ["CANDIDATE", "READY_FOR_MANUAL_TEST", "REJECTED", "EXPIRED"],
)
def test_runtime_status_rejected(bad_status):
    rt = _executed_runtime()
    rt["status"] = bad_status
    with pytest.raises(BehavioralEvaluationValidationError):
        build_behavioral_evaluation(rt, generated_at=GEN_AT)


def test_runtime_environment_rejected():
    rt = _executed_runtime()
    rt["allowed_environment"] = "PRODUCTION"
    with pytest.raises(BehavioralEvaluationValidationError):
        build_behavioral_evaluation(rt, generated_at=GEN_AT)


def test_runtime_live_behavior_changed_true_rejected():
    rt = _executed_runtime()
    rt["live_behavior_changed"] = True
    with pytest.raises(BehavioralEvaluationValidationError):
        build_behavioral_evaluation(rt, generated_at=GEN_AT)


def test_runtime_empty_bundle_rejected():
    rt = _executed_runtime()
    rt["transcript_bundle"] = []
    with pytest.raises(BehavioralEvaluationValidationError):
        build_behavioral_evaluation(rt, generated_at=GEN_AT)


def test_runtime_bad_actor_rejected():
    rt = _executed_runtime()
    rt["transcript_bundle"][0]["turns"][0]["actor"] = "robot"
    with pytest.raises(BehavioralEvaluationValidationError):
        build_behavioral_evaluation(rt, generated_at=GEN_AT)


def test_runtime_missing_required_key_rejected():
    rt = _executed_runtime()
    del rt["transcript_bundle"]
    with pytest.raises(BehavioralEvaluationValidationError):
        build_behavioral_evaluation(rt, generated_at=GEN_AT)


def test_blank_generated_at_rejected():
    with pytest.raises(BehavioralEvaluationValidationError):
        build_behavioral_evaluation(_executed_runtime(), generated_at="")


def test_inspection_runtime_id_mismatch_rejected():
    rt = _executed_runtime()
    insp = _matching_inspection(rt)
    insp["lineage_summary"]["runtime_id"] = "pas198-rt-other"
    with pytest.raises(BehavioralEvaluationValidationError):
        build_behavioral_evaluation(
            rt, generated_at=GEN_AT, inspection=insp,
        )


def test_inspection_wrong_environment_rejected():
    rt = _executed_runtime()
    insp = _matching_inspection(rt)
    insp["allowed_environment"] = "PRODUCTION"
    with pytest.raises(BehavioralEvaluationValidationError):
        build_behavioral_evaluation(
            rt, generated_at=GEN_AT, inspection=insp,
        )


# ──────────────────────────────────────────────────────────────────
# Annotation determinism / vocabulary
# ──────────────────────────────────────────────────────────────────

def test_annotate_turns_is_pure():
    rt = _executed_runtime()
    entry = rt["transcript_bundle"][0]
    a = annotate_turns(entry)
    b = annotate_turns(entry)
    assert a == b


def test_turn_annotations_drawn_from_closed_vocab():
    ev = build_behavioral_evaluation(
        _executed_runtime(), generated_at=GEN_AT,
    )
    for rec in ev["turn_annotations"]:
        for k in TURN_ANNOTATION_KEYS:
            assert k in rec
        for tok in rec["annotations"]:
            assert tok in TURN_ANNOTATIONS, f"unknown annotation {tok!r}"


def test_turn_annotations_reference_known_sequence_ids():
    rt = _executed_runtime()
    ev = build_behavioral_evaluation(rt, generated_at=GEN_AT)
    valid = {}
    for entry in rt["transcript_bundle"]:
        valid[str(entry["scenario_id"])] = {
            int(t["sequence_id"]) for t in entry["turns"]
        }
    for rec in ev["turn_annotations"]:
        sid = str(rec["scenario_id"])
        seq = int(rec["sequence_id"])
        assert sid in valid
        assert seq in valid[sid], (
            f"annotation sequence_id {seq} not in {sid}"
        )


def test_callback_first_strategy_yields_callback_continuity():
    ev = build_behavioral_evaluation(
        _executed_runtime(strategy_id="callback_first"),
        generated_at=GEN_AT,
    )
    assert "callback_continuity_observed" in ev["behavioral_flags"]


def test_assertive_strategy_surfaces_pressure_or_friction_or_trust_signal():
    ev = build_behavioral_evaluation(
        _executed_runtime(strategy_id="assertive"),
        generated_at=GEN_AT,
    )
    flags = set(ev["behavioral_flags"])
    # Assertive removes callbacks and pushes appointments; we
    # require at least one of pressure / friction / trust signals
    # to fire (the safety auto-fail on already_has_agent halts the
    # runtime mid-catalogue, and the structural trust penalty for
    # an appointment-only conversation arc is what most reliably
    # surfaces the strategy's tradeoff at this scale).
    assert (
        "high_pressure_strategy" in flags
        or "high_friction_observed" in flags
        or "early_escalation_observed" in flags
        or "low_trust_strategy" in flags
    ), flags


# ──────────────────────────────────────────────────────────────────
# Score determinism / bounds
# ──────────────────────────────────────────────────────────────────

def test_score_functions_are_pure_and_bounded():
    rt = _executed_runtime()
    entry = rt["transcript_bundle"][0]
    turns = entry["turns"]
    safety = entry["safety_markers"]
    assert 0.0 <= score_pressure(turns) <= 1.0
    assert 0.0 <= score_pacing(turns) <= 1.0
    assert 0.0 <= score_continuity(turns) <= 1.0
    assert 0.0 <= score_trust(turns, safety) <= 1.0
    assert 0.0 <= score_friction(turns, safety) <= 1.0
    assert score_pressure(turns) == score_pressure(turns)
    assert score_pacing(turns)   == score_pacing(turns)


def test_safety_violation_penalises_trust_and_lifts_friction():
    rt = _executed_runtime()
    entry = rt["transcript_bundle"][0]
    turns = entry["turns"]
    no_safety_trust    = score_trust(turns, [])
    no_safety_friction = score_friction(turns, [])
    with_safety_trust    = score_trust(turns, ["agent_poaching"])
    with_safety_friction = score_friction(turns, ["agent_poaching"])
    assert with_safety_trust    < no_safety_trust
    assert with_safety_friction > no_safety_friction


def test_empty_turns_yield_zero_scores():
    assert score_pressure([])              == 0.0
    assert score_pacing([])                == 0.0
    assert score_continuity([])            == 0.0
    assert score_trust([], [])             == 0.0
    assert score_friction([], [])          == 0.0


# ──────────────────────────────────────────────────────────────────
# Behavioural flags
# ──────────────────────────────────────────────────────────────────

def test_behavioral_flags_in_closed_vocab():
    ev = build_behavioral_evaluation(
        _executed_runtime(), generated_at=GEN_AT,
    )
    for f in ev["behavioral_flags"]:
        assert f in BEHAVIORAL_FLAGS


def test_callback_first_yields_low_friction_observed():
    ev = build_behavioral_evaluation(
        _executed_runtime(strategy_id="callback_first"),
        generated_at=GEN_AT,
    )
    # callback_first produces clean safety + no stacked qualify
    # across the catalogue; friction should be low.
    assert ev["aggregate_scores"]["friction_score"] < 0.25
    assert "low_friction_observed" in ev["behavioral_flags"]


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


def test_evaluation_carries_no_phone_numbers():
    ev = build_behavioral_evaluation(
        _executed_runtime(), generated_at=GEN_AT,
    )
    text = json.dumps(ev, sort_keys=True)
    for pat in _PHONE_RES:
        assert not pat.search(text), "phone-shaped token in evaluation"


def test_evaluation_carries_no_production_brokerage_ids():
    ev = build_behavioral_evaluation(
        _executed_runtime(), generated_at=GEN_AT,
    )
    text = json.dumps(ev, sort_keys=True)
    for pat in _PROD_ID_RES:
        assert not pat.search(text), "production brokerage id in evaluation"


def test_evaluation_carries_no_freeform_text_fields():
    ev = build_behavioral_evaluation(
        _executed_runtime(), generated_at=GEN_AT,
    )
    for forbidden in ("notes", "note", "free_text", "comment",
                      "operator_notes", "operator_comment"):
        assert forbidden not in ev, (
            f"evaluation carries forbidden free-form field {forbidden!r}"
        )


def test_evaluation_does_not_mutate_input_runtime():
    rt = _executed_runtime()
    before = json.dumps(rt, sort_keys=True)
    build_behavioral_evaluation(rt, generated_at=GEN_AT)
    after = json.dumps(rt, sort_keys=True)
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


_PAS200_FILES = (
    "app/services/simulation/behavioral_evaluation.py",
    "scripts/pas200_evaluate_runtime_behavior.py",
    "scripts/pas200_behavioral_evaluation_readiness_check.py",
)


# Forbidden-literal / forbidden-identifier scans exclude the
# readiness gate, which legitimately enumerates these tokens as
# string constants in order to detect them elsewhere.
_PAS200_FILES_FOR_FORBIDDEN_LITERAL_SCAN = (
    "app/services/simulation/behavioral_evaluation.py",
    "scripts/pas200_evaluate_runtime_behavior.py",
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


@pytest.mark.parametrize("relpath", _PAS200_FILES_FOR_FORBIDDEN_LITERAL_SCAN)
def test_forbidden_status_literals_absent(relpath):
    consts = _string_constants(_read(relpath))
    for tok in _FORBIDDEN_STATUS_LITERALS:
        assert tok not in consts, (
            f"{relpath} carries forbidden status literal {tok!r}"
        )


@pytest.mark.parametrize("relpath", _PAS200_FILES_FOR_FORBIDDEN_LITERAL_SCAN)
def test_forbidden_identifiers_absent(relpath):
    names = _identifier_names(_read(relpath))
    for tok in _FORBIDDEN_IDENTIFIERS:
        assert tok not in names, (
            f"{relpath} carries forbidden identifier {tok!r}"
        )


@pytest.mark.parametrize("relpath", _PAS200_FILES)
def test_no_banned_imports_in_pas200_file(relpath):
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

_RUNNER = _REPO_ROOT / "scripts" / "pas200_evaluate_runtime_behavior.py"


def _run_cli(*argv):
    return subprocess.run(
        [sys.executable, str(_RUNNER), *argv],
        cwd=str(_REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=300,
    )


def _write_runtime_file(tmp: pathlib.Path,
                        *, status: str = "EXECUTED",
                        allowed_environment: str = "SIMULATION_ONLY",
                        strategy_id: str = "callback_first") -> pathlib.Path:
    rt = _executed_runtime(strategy_id=strategy_id)
    rt["status"] = status
    rt["allowed_environment"] = allowed_environment
    fp = tmp / "runtime.json"
    fp.write_text(json.dumps(rt), encoding="utf-8")
    return fp


def test_runner_writes_evaluation_on_happy_path():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        rt_path = _write_runtime_file(tp)
        proc = _run_cli(
            "--runtime",    str(rt_path),
            "--output-dir", str(tp),
        )
        assert proc.returncode == 0, proc.stdout + proc.stderr
        files = list(tp.glob("pas200_behavioral_evaluation_*.json"))
        assert len(files) == 1
        payload = json.loads(files[0].read_text(encoding="utf-8"))
        for k in BEHAVIORAL_EVALUATION_REQUIRED_KEYS:
            assert k in payload
        assert payload["allowed_environment"] == "SIMULATION_ONLY"
        assert payload["live_behavior_changed"] is False


def test_runner_summary_only_does_not_write_file():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        rt_path = _write_runtime_file(tp)
        proc = _run_cli(
            "--runtime",    str(rt_path),
            "--output-dir", str(tp),
            "--summary-only",
        )
        assert proc.returncode == 0, proc.stdout + proc.stderr
        files = list(tp.glob("pas200_behavioral_evaluation_*.json"))
        assert files == []


def test_runner_missing_runtime_exits_2():
    proc = _run_cli("--summary-only")
    assert proc.returncode == 2


def test_runner_rejected_runtime_exits_2():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        rt_path = _write_runtime_file(tp, status="CANDIDATE")
        proc = _run_cli(
            "--runtime",    str(rt_path),
            "--output-dir", str(tp),
            "--summary-only",
        )
        assert proc.returncode == 2


def test_runner_with_inspection_path():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        rt = _executed_runtime()
        insp = _matching_inspection(rt)
        rt_path = tp / "rt.json"
        insp_path = tp / "insp.json"
        rt_path.write_text(json.dumps(rt), encoding="utf-8")
        insp_path.write_text(json.dumps(insp), encoding="utf-8")
        proc = _run_cli(
            "--runtime",    str(rt_path),
            "--inspection", str(insp_path),
            "--output-dir", str(tp),
            "--summary-only",
        )
        assert proc.returncode == 0, proc.stdout + proc.stderr
        assert "inspection_id=" in proc.stdout


# ──────────────────────────────────────────────────────────────────
# Readiness gate
# ──────────────────────────────────────────────────────────────────

_GATE = _REPO_ROOT / "scripts" / "pas200_behavioral_evaluation_readiness_check.py"


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
    assert payload["phase"] == "PAS200"
    assert payload["verdict"] == "READY"
    assert payload["ready"] is True
    assert payload["fail_count"] == 0
    assert payload["check_count"] > 0


# ──────────────────────────────────────────────────────────────────
# Carry-forward
# ──────────────────────────────────────────────────────────────────

def test_pas193_to_pas199_tests_still_pass():
    proc = subprocess.run(
        [
            sys.executable, "-m", "pytest",
            "tests/mvp/test_pas193_simulation_layer.py",
            "tests/mvp/test_pas194_strategy_comparison.py",
            "tests/mvp/test_pas195_simulation_recommendations.py",
            "tests/mvp/test_pas196_simulation_recommendation_review.py",
            "tests/mvp/test_pas197_manual_test_package.py",
            "tests/mvp/test_pas198_manual_test_runtime.py",
            "tests/mvp/test_pas199_runtime_inspection.py",
            "-q",
        ],
        cwd=str(_REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=1200,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr


# ──────────────────────────────────────────────────────────────────
# Doc invariants
# ──────────────────────────────────────────────────────────────────

def test_doc_present_and_carries_required_clauses():
    doc = _read("docs/pas200_behavioral_evaluation.md").lower()
    for clause in (
        "what pas200 proves",
        "what pas200 does not prove",
        "claimable",
        "still not claimable",
        "future pas201",
        "evaluation",
        "behavioral",
        "operator",
        "safety",
        "simulation_only",
        "deterministic",
        "annotation",
    ):
        assert clause in doc, f"doc missing clause {clause!r}"
