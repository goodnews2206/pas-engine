"""
PAS198 — Manual-test runtime tests.

Coverage:

  * Happy path:
      - valid READY_FOR_MANUAL_TEST/SIMULATION_ONLY package
        executes against the closed catalogue and produces a
        runtime artefact with every required key.
      - status == "EXECUTED"
      - allowed_environment == "SIMULATION_ONLY"
      - live_behavior_changed is False
      - executed_strategy == package.strategy_id
      - executed_scenarios match the closed PAS193 catalogue
        (when execution completes)
      - transcript_bundle contains one entry per executed scenario
      - safety_outcome carries the closed-vocabulary outcome
      - capability_summary carries the four capability rates
      - runtime_score carries pass_rate + average_score +
        per_scenario evaluation
      - runtime_id is deterministic for fixed inputs
      - runtime_id changes when package_id, strategy_id, or
        executed_scenarios change

  * Unhappy paths:
      - status != READY_FOR_MANUAL_TEST raises
      - allowed_environment != SIMULATION_ONLY raises
      - live_behavior_changed != False raises
      - missing keys raise
      - empty package_id / strategy_id raises
      - unknown strategy_id raises
      - blank created_at raises
      - scenarios that are not in the closed catalogue raise

  * Per-turn / transcript:
      - turns are strictly sequenced from 1
      - actors only in {agent, lead}
      - agent text non-empty
      - capability_markers drawn from closed vocab
      - safety_markers drawn from closed vocab
      - transcript_integrity_valid True on canned runs

  * Source-surface invariants:
      - PAS198 source carries no forbidden status literals
        (APPROVED, APPLIED, AUTO_APPLIED, LIVE, DEPLOYED)
      - PAS198 source carries no live-mutation identifiers
      - PAS198 source carries no banned imports (twilio, slack,
        supabase, openai, anthropic, dotenv, state machine)
      - PAS198 transcripts carry no real phone numbers
      - PAS198 transcripts carry no production brokerage IDs

  * CLI:
      - happy-path package writes a runtime artefact
      - --summary-only suppresses file write
      - missing --package exits 2
      - rejected package status exits 2
      - rejected package environment exits 2

  * Readiness gate:
      - exit 0 / verdict=READY on clean branch
      - JSON envelope valid

  * Carry-forward:
      - PAS193..PAS197 tests still pass
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


from app.services.simulation.manual_test_runtime import (  # noqa: E402
    ACTORS,
    CAPABILITY_MARKERS,
    EXECUTION_STATUSES,
    EXECUTION_STATUS_COMPLETED,
    PER_SCENARIO_EVALUATION_KEYS,
    RUNTIME_ENVIRONMENT_SIMULATION_ONLY,
    RUNTIME_REQUIRED_KEYS,
    SAFETY_MARKERS,
    SAFETY_OUTCOMES,
    SAFETY_OUTCOME_CLEAN,
    STATUS_EXECUTED,
    TRANSCRIPT_ENTRY_REQUIRED_KEYS,
    TURN_REQUIRED_KEYS,
    ManualTestRuntimeValidationError,
    execute_manual_test_runtime,
)
from app.services.simulation.scenarios import SCENARIOS  # noqa: E402
from app.services.simulation.strategies import STRATEGY_IDS  # noqa: E402


def _read(relpath: str) -> str:
    return (_REPO_ROOT / relpath).read_text(encoding="utf-8")


def _ready_package(
    package_id: str = "pas197-pkg-2b7c50e63bf5fb88",
    strategy_id: str = "callback_first",
) -> dict:
    return {
        "package_id":            package_id,
        "phase":                 "PAS197",
        "recommendation_id":     "pas195-rec-9a9566a11d621684",
        "review_id":             "pas196-rev-e1dbeb79b1f9c192",
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


# ──────────────────────────────────────────────────────────────────
# Happy path
# ──────────────────────────────────────────────────────────────────

def test_runtime_executes_valid_package():
    rt = execute_manual_test_runtime(
        _ready_package(), created_at="2026-05-22T00:00:00Z",
    )
    assert isinstance(rt, dict)


def test_runtime_carries_every_required_key():
    rt = execute_manual_test_runtime(
        _ready_package(), created_at="2026-05-22T00:00:00Z",
    )
    for k in RUNTIME_REQUIRED_KEYS:
        assert k in rt, f"missing {k}"


def test_runtime_status_is_executed():
    rt = execute_manual_test_runtime(
        _ready_package(), created_at="2026-05-22T00:00:00Z",
    )
    assert rt["status"] == STATUS_EXECUTED == "EXECUTED"


def test_runtime_allowed_environment_is_simulation_only():
    rt = execute_manual_test_runtime(
        _ready_package(), created_at="2026-05-22T00:00:00Z",
    )
    assert rt["allowed_environment"] == RUNTIME_ENVIRONMENT_SIMULATION_ONLY
    assert rt["allowed_environment"] == "SIMULATION_ONLY"


def test_runtime_live_behavior_changed_is_false():
    rt = execute_manual_test_runtime(
        _ready_package(), created_at="2026-05-22T00:00:00Z",
    )
    assert rt["live_behavior_changed"] is False


def test_runtime_executed_strategy_matches_package():
    rt = execute_manual_test_runtime(
        _ready_package(strategy_id="balanced"),
        created_at="2026-05-22T00:00:00Z",
    )
    assert rt["executed_strategy"] == "balanced"


def test_runtime_runs_full_catalogue_on_clean_strategy():
    rt = execute_manual_test_runtime(
        _ready_package(strategy_id="callback_first"),
        created_at="2026-05-22T00:00:00Z",
    )
    catalogue_ids = [s["scenario_id"] for s in SCENARIOS]
    assert rt["executed_scenarios"] == catalogue_ids
    assert rt["execution_status"] == EXECUTION_STATUS_COMPLETED


def test_runtime_transcript_bundle_aligns_with_executed_scenarios():
    rt = execute_manual_test_runtime(
        _ready_package(), created_at="2026-05-22T00:00:00Z",
    )
    bundle_ids = [b["scenario_id"] for b in rt["transcript_bundle"]]
    assert bundle_ids == rt["executed_scenarios"]
    for entry in rt["transcript_bundle"]:
        for k in TRANSCRIPT_ENTRY_REQUIRED_KEYS:
            assert k in entry


def test_runtime_id_deterministic_for_same_inputs():
    a = execute_manual_test_runtime(
        _ready_package(), created_at="2026-05-22T00:00:00Z",
    )
    b = execute_manual_test_runtime(
        _ready_package(), created_at="2026-05-22T00:00:00Z",
    )
    assert a == b


def test_runtime_id_changes_with_any_hash_input():
    base = execute_manual_test_runtime(
        _ready_package(), created_at="2026-05-22T00:00:00Z",
    )
    variants = (
        execute_manual_test_runtime(
            _ready_package(package_id="pas197-pkg-different"),
            created_at="2026-05-22T00:00:00Z",
        ),
        execute_manual_test_runtime(
            _ready_package(strategy_id="balanced"),
            created_at="2026-05-22T00:00:00Z",
        ),
        execute_manual_test_runtime(
            _ready_package(),
            created_at="2026-05-22T00:00:00Z",
            scenarios=(SCENARIOS[0],),
        ),
    )
    for v in variants:
        assert v["runtime_id"] != base["runtime_id"]


def test_runtime_id_carries_pas198_prefix():
    rt = execute_manual_test_runtime(
        _ready_package(), created_at="2026-05-22T00:00:00Z",
    )
    assert rt["runtime_id"].startswith("pas198-rt-")


def test_runtime_safety_outcome_in_closed_vocab():
    rt = execute_manual_test_runtime(
        _ready_package(), created_at="2026-05-22T00:00:00Z",
    )
    assert rt["safety_outcome"]["outcome"] in SAFETY_OUTCOMES


def test_runtime_safety_outcome_clean_on_callback_first():
    rt = execute_manual_test_runtime(
        _ready_package(strategy_id="callback_first"),
        created_at="2026-05-22T00:00:00Z",
    )
    assert rt["safety_outcome"]["outcome"] == SAFETY_OUTCOME_CLEAN
    assert rt["safety_outcome"]["auto_fail_count"] == 0
    assert rt["safety_outcome"]["auto_fail_reasons"] == []


def test_runtime_capability_summary_keys():
    rt = execute_manual_test_runtime(
        _ready_package(), created_at="2026-05-22T00:00:00Z",
    )
    caps = rt["capability_summary"]
    for k in (
        "scenarios",
        "qualification_captured_rate",
        "objection_handled_rate",
        "callback_captured_rate",
        "booking_attempted_rate",
    ):
        assert k in caps


def test_runtime_score_per_scenario_carries_evaluation_keys():
    rt = execute_manual_test_runtime(
        _ready_package(), created_at="2026-05-22T00:00:00Z",
    )
    rows = rt["runtime_score"]["per_scenario"]
    assert len(rows) == len(rt["executed_scenarios"])
    for row in rows:
        for k in PER_SCENARIO_EVALUATION_KEYS:
            assert k in row, f"per-scenario missing {k}"


def test_runtime_execution_status_in_closed_vocab():
    rt = execute_manual_test_runtime(
        _ready_package(), created_at="2026-05-22T00:00:00Z",
    )
    assert rt["execution_status"] in EXECUTION_STATUSES


# ──────────────────────────────────────────────────────────────────
# Unhappy paths
# ──────────────────────────────────────────────────────────────────

@pytest.mark.parametrize(
    "bad_status",
    ["CANDIDATE", "APPROVED_FOR_MANUAL_TEST", "REJECTED", "EXPIRED",
     "EXECUTED"],
)
def test_non_ready_package_status_rejected(bad_status):
    pkg = _ready_package()
    pkg["status"] = bad_status
    with pytest.raises(ManualTestRuntimeValidationError):
        execute_manual_test_runtime(pkg, created_at="2026-05-22T00:00:00Z")


@pytest.mark.parametrize(
    "bad_env",
    ["PRODUCTION", "LIVE", "STAGING", "MANUAL", ""],
)
def test_wrong_environment_rejected(bad_env):
    pkg = _ready_package()
    pkg["allowed_environment"] = bad_env
    with pytest.raises(ManualTestRuntimeValidationError):
        execute_manual_test_runtime(pkg, created_at="2026-05-22T00:00:00Z")


def test_live_behavior_changed_true_rejected():
    pkg = _ready_package()
    pkg["live_behavior_changed"] = True
    with pytest.raises(ManualTestRuntimeValidationError):
        execute_manual_test_runtime(pkg, created_at="2026-05-22T00:00:00Z")


def test_missing_required_key_rejected():
    pkg = _ready_package()
    del pkg["strategy_id"]
    with pytest.raises(ManualTestRuntimeValidationError):
        execute_manual_test_runtime(pkg, created_at="2026-05-22T00:00:00Z")


@pytest.mark.parametrize("bad_pkg_id", [None, "", 0, False])
def test_empty_package_id_rejected(bad_pkg_id):
    pkg = _ready_package()
    pkg["package_id"] = bad_pkg_id
    with pytest.raises(ManualTestRuntimeValidationError):
        execute_manual_test_runtime(pkg, created_at="2026-05-22T00:00:00Z")


@pytest.mark.parametrize("bad_sid", [None, "", 0, False])
def test_empty_strategy_id_rejected(bad_sid):
    pkg = _ready_package()
    pkg["strategy_id"] = bad_sid
    with pytest.raises(ManualTestRuntimeValidationError):
        execute_manual_test_runtime(pkg, created_at="2026-05-22T00:00:00Z")


def test_unknown_strategy_id_rejected():
    pkg = _ready_package(strategy_id="totally_made_up")
    with pytest.raises(ManualTestRuntimeValidationError):
        execute_manual_test_runtime(pkg, created_at="2026-05-22T00:00:00Z")


def test_blank_created_at_rejected():
    with pytest.raises(ManualTestRuntimeValidationError):
        execute_manual_test_runtime(_ready_package(), created_at="")


def test_unknown_scenario_id_rejected():
    bogus = {
        "scenario_id":      "pas999_made_up",
        "scenario_type":    "high_intent_buyer",
        "supported":        True,
        "lead_script":      ("hello",),
        "success_criteria": ("qualification_captured",),
    }
    with pytest.raises(ManualTestRuntimeValidationError):
        execute_manual_test_runtime(
            _ready_package(),
            created_at="2026-05-22T00:00:00Z",
            scenarios=(bogus,),
        )


# ──────────────────────────────────────────────────────────────────
# Per-turn / transcript invariants
# ──────────────────────────────────────────────────────────────────

def test_turns_strictly_sequenced_from_one():
    rt = execute_manual_test_runtime(
        _ready_package(), created_at="2026-05-22T00:00:00Z",
    )
    for entry in rt["transcript_bundle"]:
        if not entry["turns"]:
            continue
        for idx, t in enumerate(entry["turns"]):
            assert t["sequence_id"] == idx + 1, entry["scenario_id"]


def test_turn_actors_in_closed_vocab():
    rt = execute_manual_test_runtime(
        _ready_package(), created_at="2026-05-22T00:00:00Z",
    )
    for entry in rt["transcript_bundle"]:
        for t in entry["turns"]:
            assert t["actor"] in ACTORS


def test_turn_carries_every_required_key():
    rt = execute_manual_test_runtime(
        _ready_package(), created_at="2026-05-22T00:00:00Z",
    )
    for entry in rt["transcript_bundle"]:
        for t in entry["turns"]:
            for k in TURN_REQUIRED_KEYS:
                assert k in t


def test_agent_turn_text_non_empty():
    rt = execute_manual_test_runtime(
        _ready_package(), created_at="2026-05-22T00:00:00Z",
    )
    for entry in rt["transcript_bundle"]:
        for t in entry["turns"]:
            if t["actor"] == "agent":
                assert t["text"]


def test_capability_markers_in_closed_vocab():
    rt = execute_manual_test_runtime(
        _ready_package(), created_at="2026-05-22T00:00:00Z",
    )
    for entry in rt["transcript_bundle"]:
        for t in entry["turns"]:
            for m in t.get("capability_markers") or ():
                assert m in CAPABILITY_MARKERS
        for m in entry.get("capability_markers") or ():
            assert m in CAPABILITY_MARKERS


def test_safety_markers_in_closed_vocab():
    rt = execute_manual_test_runtime(
        _ready_package(), created_at="2026-05-22T00:00:00Z",
    )
    for entry in rt["transcript_bundle"]:
        for t in entry["turns"]:
            for m in t.get("safety_markers") or ():
                assert m in SAFETY_MARKERS
        for m in entry.get("safety_markers") or ():
            assert m in SAFETY_MARKERS


def test_safety_markers_field_always_present_on_entries_and_turns():
    rt = execute_manual_test_runtime(
        _ready_package(), created_at="2026-05-22T00:00:00Z",
    )
    for entry in rt["transcript_bundle"]:
        assert "safety_markers" in entry
        assert isinstance(entry["safety_markers"], list)
        for t in entry["turns"]:
            assert "safety_markers" in t
            assert isinstance(t["safety_markers"], list)


def test_transcript_integrity_valid_on_clean_run():
    rt = execute_manual_test_runtime(
        _ready_package(strategy_id="callback_first"),
        created_at="2026-05-22T00:00:00Z",
    )
    for row in rt["runtime_score"]["per_scenario"]:
        assert row["transcript_integrity_valid"] is True, row["scenario_id"]


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


_PAS198_FILES = (
    "app/services/simulation/manual_test_runtime.py",
    "scripts/pas198_run_manual_test_runtime.py",
    "scripts/pas198_manual_test_runtime_readiness_check.py",
)

# Forbidden-literal / forbidden-identifier scans exclude the
# readiness gate, which legitimately enumerates these tokens as
# string constants in order to detect them elsewhere.
_PAS198_FILES_FOR_FORBIDDEN_LITERAL_SCAN = (
    "app/services/simulation/manual_test_runtime.py",
    "scripts/pas198_run_manual_test_runtime.py",
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


@pytest.mark.parametrize("relpath", _PAS198_FILES_FOR_FORBIDDEN_LITERAL_SCAN)
def test_forbidden_status_literals_absent(relpath):
    consts = _string_constants(_read(relpath))
    for tok in _FORBIDDEN_STATUS_LITERALS:
        assert tok not in consts, (
            f"{relpath} carries forbidden status literal {tok!r}"
        )


@pytest.mark.parametrize("relpath", _PAS198_FILES_FOR_FORBIDDEN_LITERAL_SCAN)
def test_forbidden_identifiers_absent(relpath):
    names = _identifier_names(_read(relpath))
    for tok in _FORBIDDEN_IDENTIFIERS:
        assert tok not in names, (
            f"{relpath} carries forbidden identifier {tok!r}"
        )


@pytest.mark.parametrize("relpath", _PAS198_FILES)
def test_no_banned_imports_in_pas198_file(relpath):
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
    re.compile(r"\+\d[\d\s.\-]{6,14}\d"),
    re.compile(r"(?<!\d)\d{10,15}(?!\d)"),
)

_PROD_ID_RES = (
    re.compile(r"\bbrokerage_id\s*=\s*[\"']?[0-9a-fA-F\-]{8,}[\"']?"),
    re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b"),
)


def test_transcripts_carry_no_phone_numbers():
    rt = execute_manual_test_runtime(
        _ready_package(), created_at="2026-05-22T00:00:00Z",
    )
    for entry in rt["transcript_bundle"]:
        for t in entry["turns"]:
            for pat in _PHONE_RES:
                assert not pat.search(t["text"] or ""), (
                    f"phone-shaped token in {entry['scenario_id']} "
                    f"turn {t['sequence_id']}"
                )


def test_transcripts_carry_no_production_brokerage_ids():
    rt = execute_manual_test_runtime(
        _ready_package(), created_at="2026-05-22T00:00:00Z",
    )
    for entry in rt["transcript_bundle"]:
        for t in entry["turns"]:
            for pat in _PROD_ID_RES:
                assert not pat.search(t["text"] or ""), (
                    f"production brokerage id in {entry['scenario_id']} "
                    f"turn {t['sequence_id']}"
                )


def test_runtime_carries_no_freeform_text_fields():
    rt = execute_manual_test_runtime(
        _ready_package(), created_at="2026-05-22T00:00:00Z",
    )
    for forbidden in ("notes", "note", "free_text", "comment",
                      "operator_notes", "operator_comment"):
        assert forbidden not in rt, (
            f"runtime carries forbidden free-form field {forbidden!r}"
        )


def test_runtime_does_not_mutate_input_package():
    pkg = _ready_package()
    before = json.dumps(pkg, sort_keys=True)
    execute_manual_test_runtime(pkg, created_at="2026-05-22T00:00:00Z")
    after = json.dumps(pkg, sort_keys=True)
    assert before == after


# ──────────────────────────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────────────────────────

_RUNNER = _REPO_ROOT / "scripts" / "pas198_run_manual_test_runtime.py"


def _run_cli(*argv):
    return subprocess.run(
        [sys.executable, str(_RUNNER), *argv],
        cwd=str(_REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=180,
    )


def _write_package(tmp: pathlib.Path,
                   *, status: str = "READY_FOR_MANUAL_TEST",
                   allowed_environment: str = "SIMULATION_ONLY",
                   strategy_id: str = "callback_first") -> pathlib.Path:
    pkg = _ready_package(strategy_id=strategy_id)
    pkg["status"] = status
    pkg["allowed_environment"] = allowed_environment
    fp = tmp / "package.json"
    fp.write_text(json.dumps(pkg), encoding="utf-8")
    return fp


def test_runner_writes_runtime_on_happy_path():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        pkg_path = _write_package(tp)
        proc = _run_cli(
            "--package",    str(pkg_path),
            "--output-dir", str(tp),
        )
        assert proc.returncode == 0, proc.stdout + proc.stderr
        files = list(tp.glob("pas198_manual_test_runtime_*.json"))
        assert len(files) == 1
        payload = json.loads(files[0].read_text(encoding="utf-8"))
        for k in RUNTIME_REQUIRED_KEYS:
            assert k in payload
        assert payload["status"] == "EXECUTED"
        assert payload["allowed_environment"] == "SIMULATION_ONLY"
        assert payload["live_behavior_changed"] is False


def test_runner_summary_only_does_not_write_file():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        pkg_path = _write_package(tp)
        proc = _run_cli(
            "--package",    str(pkg_path),
            "--output-dir", str(tp),
            "--summary-only",
        )
        assert proc.returncode == 0, proc.stdout + proc.stderr
        files = list(tp.glob("pas198_manual_test_runtime_*.json"))
        assert files == []


def test_runner_missing_package_exits_2():
    proc = _run_cli("--summary-only")
    assert proc.returncode == 2


def test_runner_rejected_status_exits_2():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        pkg_path = _write_package(tp, status="CANDIDATE")
        proc = _run_cli(
            "--package",    str(pkg_path),
            "--output-dir", str(tp),
            "--summary-only",
        )
        assert proc.returncode == 2


def test_runner_rejected_environment_exits_2():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        pkg_path = _write_package(tp, allowed_environment="PRODUCTION")
        proc = _run_cli(
            "--package",    str(pkg_path),
            "--output-dir", str(tp),
            "--summary-only",
        )
        assert proc.returncode == 2


# ──────────────────────────────────────────────────────────────────
# Readiness gate
# ──────────────────────────────────────────────────────────────────

_GATE = _REPO_ROOT / "scripts" / "pas198_manual_test_runtime_readiness_check.py"


def test_readiness_gate_runs_clean_summary_only():
    proc = subprocess.run(
        [sys.executable, str(_GATE), "--summary-only"],
        cwd=str(_REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=180,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "verdict=READY" in proc.stdout


def test_readiness_gate_json_envelope_valid():
    proc = subprocess.run(
        [sys.executable, str(_GATE), "--summary-only", "--json"],
        cwd=str(_REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=180,
    )
    assert proc.returncode == 0
    payload_str = proc.stdout[proc.stdout.find("{"):]
    payload = json.loads(payload_str)
    assert payload["phase"] == "PAS198"
    assert payload["verdict"] == "READY"
    assert payload["ready"] is True
    assert payload["fail_count"] == 0
    assert payload["check_count"] > 0


# ──────────────────────────────────────────────────────────────────
# Carry-forward
# ──────────────────────────────────────────────────────────────────

def test_pas193_to_pas197_tests_still_pass():
    proc = subprocess.run(
        [
            sys.executable, "-m", "pytest",
            "tests/mvp/test_pas193_simulation_layer.py",
            "tests/mvp/test_pas194_strategy_comparison.py",
            "tests/mvp/test_pas195_simulation_recommendations.py",
            "tests/mvp/test_pas196_simulation_recommendation_review.py",
            "tests/mvp/test_pas197_manual_test_package.py",
            "-q",
        ],
        cwd=str(_REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=600,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr


# ──────────────────────────────────────────────────────────────────
# Doc invariants
# ──────────────────────────────────────────────────────────────────

def test_doc_present_and_carries_required_clauses():
    doc = _read("docs/pas198_manual_test_runtime.md").lower()
    for clause in (
        "what pas198 proves",
        "what pas198 does not prove",
        "claimable",
        "still not claimable",
        "future pas199",
        "manual test",
        "runtime",
        "operator",
        "safety",
        "simulation_only",
    ):
        assert clause in doc, f"doc missing clause {clause!r}"


# ──────────────────────────────────────────────────────────────────
# Strategy catalogue sanity
# ──────────────────────────────────────────────────────────────────

def test_known_strategies_all_executable():
    for sid in STRATEGY_IDS:
        rt = execute_manual_test_runtime(
            _ready_package(strategy_id=sid),
            created_at="2026-05-22T00:00:00Z",
        )
        assert rt["executed_strategy"] == sid
        assert rt["status"] == "EXECUTED"
        assert rt["allowed_environment"] == "SIMULATION_ONLY"
        assert rt["live_behavior_changed"] is False
