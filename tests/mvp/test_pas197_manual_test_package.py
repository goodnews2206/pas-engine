"""
PAS197 — Manual-test package tests.

Coverage:

  * Happy path:
      - approved review + CANDIDATE recommendation -> package
      - package carries every required key
      - status == READY_FOR_MANUAL_TEST
      - allowed_environment == SIMULATION_ONLY
      - live_behavior_changed is False
      - strategy_id == recommendation.recommended_strategy
      - package_id deterministic for fixed inputs
      - package_id changes when any of its hash inputs change

  * Unhappy paths:
      - review.new_status != APPROVED_FOR_MANUAL_TEST raises
        (REJECTED, EXPIRED, CANDIDATE all rejected)
      - review.live_behavior_changed != False raises
      - recommendation.status != CANDIDATE raises
      - recommendation.operator_required != True raises
      - recommendation.recommended_strategy missing / empty / None
        raises
      - recommendation_id mismatch between recommendation and
        review raises
      - missing required keys in either payload raises
      - bad created_at raises

  * Source-surface invariants:
      - PAS197 source carries no forbidden status literals
        (APPROVED, APPLIED, AUTO_APPLIED, LIVE, DEPLOYED)
      - PAS197 source carries no live-mutation identifiers
        (apply_recommendation, deploy_strategy,
        switch_strategy_live, auto_apply, auto_promote,
        force_promote, live_apply, auto_deploy)
      - PAS197 source carries no banned imports (twilio, slack,
        supabase, openai, anthropic, dotenv, state machine)

  * Test-plan / metrics / rollback / safety vocabularies:
      - each non-empty
      - each drawn from a single closed tuple per category
      - no forbidden tokens appear

  * CLI:
      - happy-path approve writes a package
      - --summary-only suppresses file write
      - missing --recommendation exits 2
      - missing --review exits 2
      - rejected review exits 2
      - mismatched recommendation/review ids exits 2

  * Readiness gate:
      - exit 0 / verdict=READY on clean main
      - JSON envelope valid

  * Carry-forward:
      - PAS193 / PAS194 / PAS195 / PAS196 tests still pass
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


from app.services.simulation.manual_test_package import (  # noqa: E402
    ALLOWED_ENVIRONMENT_SIMULATION_ONLY,
    PACKAGE_REQUIRED_KEYS,
    PACKAGE_ROLLBACK_NOTES,
    PACKAGE_SAFETY_NOTES,
    PACKAGE_SUCCESS_METRICS,
    PACKAGE_TEST_STEPS,
    STATUS_READY_FOR_MANUAL_TEST,
    ManualTestPackageValidationError,
    build_manual_test_package,
)


def _read(relpath: str) -> str:
    return (_REPO_ROOT / relpath).read_text(encoding="utf-8")


def _candidate_recommendation(
    rec_id: str = "pas195-rec-9a9566a11d621684",
    strategy: str = "callback_first",
) -> dict:
    return {
        "recommendation_id":     rec_id,
        "status":                "CANDIDATE",
        "operator_required":     True,
        "recommended_strategy":  strategy,
        "phase":                 "PAS195",
    }


def _approved_review(
    rec_id: str = "pas195-rec-9a9566a11d621684",
    review_id: str = "pas196-rev-deadbeefcafebabe",
) -> dict:
    return {
        "review_id":             review_id,
        "recommendation_id":     rec_id,
        "new_status":            "APPROVED_FOR_MANUAL_TEST",
        "previous_status":       "CANDIDATE",
        "live_behavior_changed": False,
        "operator_required":     True,
        "phase":                 "PAS196",
    }


# ──────────────────────────────────────────────────────────────────
# Happy path
# ──────────────────────────────────────────────────────────────────

def test_approved_pair_produces_package():
    pkg = build_manual_test_package(
        _candidate_recommendation(),
        _approved_review(),
        created_at="2026-05-21T00:00:00Z",
    )
    assert isinstance(pkg, dict)


def test_package_carries_every_required_key():
    pkg = build_manual_test_package(
        _candidate_recommendation(),
        _approved_review(),
        created_at="2026-05-21T00:00:00Z",
    )
    for k in PACKAGE_REQUIRED_KEYS:
        assert k in pkg, f"missing {k}"


def test_package_status_is_ready_for_manual_test():
    pkg = build_manual_test_package(
        _candidate_recommendation(),
        _approved_review(),
        created_at="2026-05-21T00:00:00Z",
    )
    assert pkg["status"] == STATUS_READY_FOR_MANUAL_TEST
    assert pkg["status"] == "READY_FOR_MANUAL_TEST"


def test_package_allowed_environment_is_simulation_only():
    pkg = build_manual_test_package(
        _candidate_recommendation(),
        _approved_review(),
        created_at="2026-05-21T00:00:00Z",
    )
    assert pkg["allowed_environment"] == ALLOWED_ENVIRONMENT_SIMULATION_ONLY
    assert pkg["allowed_environment"] == "SIMULATION_ONLY"


def test_package_live_behavior_changed_is_false():
    pkg = build_manual_test_package(
        _candidate_recommendation(),
        _approved_review(),
        created_at="2026-05-21T00:00:00Z",
    )
    assert pkg["live_behavior_changed"] is False


def test_package_strategy_id_matches_recommendation():
    rec = _candidate_recommendation(strategy="balanced")
    pkg = build_manual_test_package(
        rec, _approved_review(), created_at="2026-05-21T00:00:00Z",
    )
    assert pkg["strategy_id"] == "balanced"


def test_package_id_deterministic_for_same_inputs():
    a = build_manual_test_package(
        _candidate_recommendation(), _approved_review(),
        created_at="2026-05-21T00:00:00Z",
    )
    b = build_manual_test_package(
        _candidate_recommendation(), _approved_review(),
        created_at="2026-05-21T00:00:00Z",
    )
    assert a == b


def test_package_id_changes_with_any_hash_input():
    base = build_manual_test_package(
        _candidate_recommendation(), _approved_review(),
        created_at="2026-05-21T00:00:00Z",
    )
    variants = (
        build_manual_test_package(
            _candidate_recommendation("pas195-rec-other"),
            _approved_review("pas195-rec-other"),
            created_at="2026-05-21T00:00:00Z",
        ),
        build_manual_test_package(
            _candidate_recommendation(),
            _approved_review(review_id="pas196-rev-different"),
            created_at="2026-05-21T00:00:00Z",
        ),
        build_manual_test_package(
            _candidate_recommendation(strategy="balanced"),
            _approved_review(),
            created_at="2026-05-21T00:00:00Z",
        ),
    )
    for v in variants:
        assert v["package_id"] != base["package_id"]


def test_package_id_carries_pas197_prefix():
    pkg = build_manual_test_package(
        _candidate_recommendation(), _approved_review(),
        created_at="2026-05-21T00:00:00Z",
    )
    assert pkg["package_id"].startswith("pas197-pkg-")


# ──────────────────────────────────────────────────────────────────
# Unhappy paths
# ──────────────────────────────────────────────────────────────────

@pytest.mark.parametrize("bad_status", ["REJECTED", "EXPIRED", "CANDIDATE"])
def test_non_approved_review_raises(bad_status):
    rev = _approved_review()
    rev["new_status"] = bad_status
    with pytest.raises(ManualTestPackageValidationError):
        build_manual_test_package(
            _candidate_recommendation(), rev,
            created_at="2026-05-21T00:00:00Z",
        )


def test_review_live_behavior_changed_true_raises():
    rev = _approved_review()
    rev["live_behavior_changed"] = True
    with pytest.raises(ManualTestPackageValidationError):
        build_manual_test_package(
            _candidate_recommendation(), rev,
            created_at="2026-05-21T00:00:00Z",
        )


@pytest.mark.parametrize("bad_status", ["REJECTED", "EXPIRED",
                                        "READY_FOR_MANUAL_TEST"])
def test_non_candidate_recommendation_status_raises(bad_status):
    rec = _candidate_recommendation()
    rec["status"] = bad_status
    with pytest.raises(ManualTestPackageValidationError):
        build_manual_test_package(
            rec, _approved_review(),
            created_at="2026-05-21T00:00:00Z",
        )


def test_operator_required_false_raises():
    rec = _candidate_recommendation()
    rec["operator_required"] = False
    with pytest.raises(ManualTestPackageValidationError):
        build_manual_test_package(
            rec, _approved_review(),
            created_at="2026-05-21T00:00:00Z",
        )


@pytest.mark.parametrize("bad_strategy", [None, "", 0, False])
def test_missing_recommended_strategy_raises(bad_strategy):
    rec = _candidate_recommendation()
    rec["recommended_strategy"] = bad_strategy
    with pytest.raises(ManualTestPackageValidationError):
        build_manual_test_package(
            rec, _approved_review(),
            created_at="2026-05-21T00:00:00Z",
        )


def test_recommendation_id_mismatch_raises():
    rec = _candidate_recommendation("pas195-rec-AAA")
    rev = _approved_review("pas195-rec-BBB")
    with pytest.raises(ManualTestPackageValidationError):
        build_manual_test_package(
            rec, rev, created_at="2026-05-21T00:00:00Z",
        )


def test_missing_keys_in_recommendation_raises():
    bad = {"recommendation_id": "x"}  # missing status, etc.
    with pytest.raises(ManualTestPackageValidationError):
        build_manual_test_package(
            bad, _approved_review(),
            created_at="2026-05-21T00:00:00Z",
        )


def test_missing_keys_in_review_raises():
    bad = {"review_id": "x"}  # missing new_status, etc.
    with pytest.raises(ManualTestPackageValidationError):
        build_manual_test_package(
            _candidate_recommendation(), bad,
            created_at="2026-05-21T00:00:00Z",
        )


def test_blank_created_at_raises():
    with pytest.raises(ManualTestPackageValidationError):
        build_manual_test_package(
            _candidate_recommendation(), _approved_review(),
            created_at="",
        )


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


_PAS197_FILES = (
    "app/services/simulation/manual_test_package.py",
    "scripts/pas197_create_manual_test_package.py",
    "scripts/pas197_manual_test_package_readiness_check.py",
)


# Forbidden-literal / forbidden-identifier scans exclude the
# readiness gate, which legitimately enumerates these tokens as
# string constants in order to detect them elsewhere.
_PAS197_FILES_FOR_FORBIDDEN_LITERAL_SCAN = (
    "app/services/simulation/manual_test_package.py",
    "scripts/pas197_create_manual_test_package.py",
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


@pytest.mark.parametrize("relpath", _PAS197_FILES_FOR_FORBIDDEN_LITERAL_SCAN)
def test_forbidden_status_literals_absent(relpath):
    consts = _string_constants(_read(relpath))
    for tok in _FORBIDDEN_STATUS_LITERALS:
        assert tok not in consts, (
            f"{relpath} carries forbidden status literal {tok!r}"
        )


@pytest.mark.parametrize("relpath", _PAS197_FILES_FOR_FORBIDDEN_LITERAL_SCAN)
def test_forbidden_identifiers_absent(relpath):
    names = _identifier_names(_read(relpath))
    for tok in _FORBIDDEN_IDENTIFIERS:
        assert tok not in names, (
            f"{relpath} carries forbidden identifier {tok!r}"
        )


@pytest.mark.parametrize("relpath", _PAS197_FILES)
def test_no_banned_imports_in_pas197_file(relpath):
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
# Vocabularies
# ──────────────────────────────────────────────────────────────────

def test_test_plan_vocabulary_non_empty_and_bounded():
    pkg = build_manual_test_package(
        _candidate_recommendation(), _approved_review(),
        created_at="2026-05-21T00:00:00Z",
    )
    assert len(pkg["test_plan"]) > 0
    for token in pkg["test_plan"]:
        assert token in PACKAGE_TEST_STEPS


def test_success_metrics_vocabulary_non_empty_and_bounded():
    pkg = build_manual_test_package(
        _candidate_recommendation(), _approved_review(),
        created_at="2026-05-21T00:00:00Z",
    )
    assert len(pkg["success_metrics"]) > 0
    for token in pkg["success_metrics"]:
        assert token in PACKAGE_SUCCESS_METRICS


def test_rollback_notes_vocabulary_non_empty_and_bounded():
    pkg = build_manual_test_package(
        _candidate_recommendation(), _approved_review(),
        created_at="2026-05-21T00:00:00Z",
    )
    assert len(pkg["rollback_notes"]) > 0
    for token in pkg["rollback_notes"]:
        assert token in PACKAGE_ROLLBACK_NOTES


def test_safety_notes_vocabulary_non_empty_and_bounded():
    pkg = build_manual_test_package(
        _candidate_recommendation(), _approved_review(),
        created_at="2026-05-21T00:00:00Z",
    )
    assert len(pkg["safety_notes"]) > 0
    for token in pkg["safety_notes"]:
        assert token in PACKAGE_SAFETY_NOTES


def test_package_carries_no_freeform_text_fields():
    pkg = build_manual_test_package(
        _candidate_recommendation(), _approved_review(),
        created_at="2026-05-21T00:00:00Z",
    )
    for forbidden in ("notes", "note", "free_text", "comment",
                      "operator_notes", "operator_comment"):
        assert forbidden not in pkg, (
            f"package carries forbidden free-form field {forbidden!r}"
        )


# ──────────────────────────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────────────────────────

_RUNNER = _REPO_ROOT / "scripts" / "pas197_create_manual_test_package.py"


def _run_cli(*argv):
    return subprocess.run(
        [sys.executable, str(_RUNNER), *argv],
        cwd=str(_REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=180,
    )


def _write_pair(tmp: pathlib.Path,
                *, review_status: str = "APPROVED_FOR_MANUAL_TEST",
                rec_id: str = "pas195-rec-9a9566a11d621684",
                review_rec_id: str = "pas195-rec-9a9566a11d621684"):
    rec_path = tmp / "rec.json"
    rev_path = tmp / "rev.json"
    rec = _candidate_recommendation(rec_id)
    rev = _approved_review(review_rec_id)
    rev["new_status"] = review_status
    rec_path.write_text(json.dumps(rec), encoding="utf-8")
    rev_path.write_text(json.dumps(rev), encoding="utf-8")
    return rec_path, rev_path


def test_runner_writes_package_on_happy_path():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        rec_path, rev_path = _write_pair(tp)
        proc = _run_cli(
            "--recommendation", str(rec_path),
            "--review",         str(rev_path),
            "--output-dir",     str(tp),
        )
        assert proc.returncode == 0, proc.stdout + proc.stderr
        files = list(tp.glob("pas197_manual_test_package_*.json"))
        assert len(files) == 1
        payload = json.loads(files[0].read_text(encoding="utf-8"))
        for k in PACKAGE_REQUIRED_KEYS:
            assert k in payload
        assert payload["status"] == "READY_FOR_MANUAL_TEST"
        assert payload["allowed_environment"] == "SIMULATION_ONLY"
        assert payload["live_behavior_changed"] is False


def test_runner_summary_only_does_not_write_file():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        rec_path, rev_path = _write_pair(tp)
        proc = _run_cli(
            "--recommendation", str(rec_path),
            "--review",         str(rev_path),
            "--output-dir",     str(tp),
            "--summary-only",
        )
        assert proc.returncode == 0, proc.stdout + proc.stderr
        files = list(tp.glob("pas197_manual_test_package_*.json"))
        assert files == []


def test_runner_missing_recommendation_exits_2():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        _, rev_path = _write_pair(tp)
        proc = _run_cli(
            "--review",         str(rev_path),
            "--output-dir",     str(tp),
            "--summary-only",
        )
        assert proc.returncode == 2


def test_runner_missing_review_exits_2():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        rec_path, _ = _write_pair(tp)
        proc = _run_cli(
            "--recommendation", str(rec_path),
            "--output-dir",     str(tp),
            "--summary-only",
        )
        assert proc.returncode == 2


def test_runner_rejected_review_exits_2():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        rec_path, rev_path = _write_pair(tp, review_status="REJECTED")
        proc = _run_cli(
            "--recommendation", str(rec_path),
            "--review",         str(rev_path),
            "--output-dir",     str(tp),
            "--summary-only",
        )
        assert proc.returncode == 2


def test_runner_mismatched_ids_exits_2():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        rec_path, rev_path = _write_pair(
            tp,
            rec_id="pas195-rec-AAA",
            review_rec_id="pas195-rec-BBB",
        )
        proc = _run_cli(
            "--recommendation", str(rec_path),
            "--review",         str(rev_path),
            "--output-dir",     str(tp),
            "--summary-only",
        )
        assert proc.returncode == 2


# ──────────────────────────────────────────────────────────────────
# Readiness gate
# ──────────────────────────────────────────────────────────────────

_GATE = _REPO_ROOT / "scripts" / "pas197_manual_test_package_readiness_check.py"


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
    assert payload["phase"] == "PAS197"
    assert payload["verdict"] == "READY"
    assert payload["ready"] is True
    assert payload["fail_count"] == 0
    assert payload["check_count"] > 0


# ──────────────────────────────────────────────────────────────────
# Carry-forward
# ──────────────────────────────────────────────────────────────────

def test_pas193_to_pas196_tests_still_pass():
    proc = subprocess.run(
        [
            sys.executable, "-m", "pytest",
            "tests/mvp/test_pas193_simulation_layer.py",
            "tests/mvp/test_pas194_strategy_comparison.py",
            "tests/mvp/test_pas195_simulation_recommendations.py",
            "tests/mvp/test_pas196_simulation_recommendation_review.py",
            "-q",
        ],
        cwd=str(_REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=420,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr


# ──────────────────────────────────────────────────────────────────
# Doc invariants
# ──────────────────────────────────────────────────────────────────

def test_doc_present_and_carries_required_clauses():
    doc = _read("docs/pas197_manual_test_package.md").lower()
    for clause in (
        "what pas197 proves",
        "what pas197 does not prove",
        "claimable",
        "still not claimable",
        "future pas198",
        "manual test",
        "package",
        "operator",
        "safety",
    ):
        assert clause in doc, f"doc missing clause {clause!r}"
