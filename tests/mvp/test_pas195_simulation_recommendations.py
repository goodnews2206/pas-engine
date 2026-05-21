"""
PAS195 — Simulation recommendation tests.

Coverage:

  * Module surface:
      - generate_recommendation produces every required key
      - status is always CANDIDATE
      - operator_required is always True
      - recommendation_type drawn from RECOMMENDATION_TYPES
      - confidence_level drawn from CONFIDENCE_LEVELS

  * Logic against the current deterministic PAS194 comparison:
      - callback_first is the recommended strategy
      - assertive is the rejected strategy (worst)
      - assertive and booking_first are disqualified by safety
      - balanced and callback_first remain safe candidates
      - conservative is disqualified by failing the pass_rate
        threshold rather than by safety

  * Threshold behaviour:
      - threshold of 1.0 still recommends callback_first
      - threshold of 0.99 still recommends callback_first
      - threshold of 0.9 keeps callback_first the winner (its
        avg_score remains the highest among safe candidates)
      - extreme threshold (e.g. 1.01) yields no_safe_promotion

  * Safety:
      - any failure_modes entry whose reason is a safety
        auto-fail code disqualifies the strategy
      - 'recommended_strategy' is None when no safe candidate
        meets the threshold

  * Determinism:
      - recommendation_id reproducible for the same comparison +
        threshold
      - different threshold changes recommendation_id

  * Import safety:
      - recommendation module + CLI free of twilio / slack_sdk /
        openai / anthropic / dotenv / supabase / state machine
      - no load_dotenv / get_supabase calls

  * Forbidden-language:
      - no autonomous-apply tokens in PAS195 source

  * CLI:
      - default run writes a recommendation JSON
      - --summary-only suppresses the file write
      - --from-report path reads a comparison report from disk
      - invalid --pass-rate-threshold exits 2

  * Readiness gate:
      - exit 0 / verdict=READY on a clean main
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

import pytest


_REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))


from app.services.simulation.scenarios import SCENARIOS  # noqa: E402
from app.services.simulation.strategies import STRATEGIES  # noqa: E402
from app.services.simulation.comparison import (  # noqa: E402
    build_comparison_report,
    compare_strategies,
)
from app.services.simulation.recommendations import (  # noqa: E402
    CONFIDENCE_LEVELS,
    RECOMMENDATION_REQUIRED_KEYS,
    RECOMMENDATION_TYPES,
    SAFETY_AUTO_FAIL_REASONS,
    STATUS_CANDIDATE,
    generate_recommendation,
)


def _read(relpath: str) -> str:
    return (_REPO_ROOT / relpath).read_text(encoding="utf-8")


def _build_comparison_report(seed: int = 0,
                             generated_at: str = "2026-05-21T00:00:00Z"):
    rows = compare_strategies(STRATEGIES, SCENARIOS)
    return build_comparison_report(
        rows, SCENARIOS, generated_at=generated_at, seed=seed,
    )


# ──────────────────────────────────────────────────────────────────
# Module surface
# ──────────────────────────────────────────────────────────────────

def test_recommendation_carries_every_required_key():
    rec = generate_recommendation(_build_comparison_report())
    for key in RECOMMENDATION_REQUIRED_KEYS:
        assert key in rec, f"missing {key}"


def test_recommendation_status_is_candidate_only():
    rec = generate_recommendation(_build_comparison_report())
    assert rec["status"] == STATUS_CANDIDATE
    assert STATUS_CANDIDATE == "CANDIDATE"


def test_recommendation_operator_required_is_true():
    rec = generate_recommendation(_build_comparison_report())
    assert rec["operator_required"] is True


def test_recommendation_type_in_catalogue():
    rec = generate_recommendation(_build_comparison_report())
    assert rec["recommendation_type"] in RECOMMENDATION_TYPES


def test_recommendation_confidence_in_catalogue():
    rec = generate_recommendation(_build_comparison_report())
    assert rec["confidence_level"] in CONFIDENCE_LEVELS


# ──────────────────────────────────────────────────────────────────
# Logic against the deterministic PAS194 comparison
# ──────────────────────────────────────────────────────────────────

def test_callback_first_is_recommended_from_current_comparison():
    rec = generate_recommendation(_build_comparison_report())
    assert rec["recommended_strategy"] == "callback_first"
    assert rec["recommendation_type"] == "promote_strategy"


def test_assertive_is_rejected_strategy():
    rec = generate_recommendation(_build_comparison_report())
    assert rec["rejected_strategy"] == "assertive"


def test_assertive_and_booking_first_are_disqualified_by_safety():
    rec = generate_recommendation(_build_comparison_report())
    disqualified = set(rec["evidence_summary"]["disqualified_strategies"])
    assert "assertive" in disqualified
    assert "booking_first" in disqualified


def test_safe_candidates_above_threshold_include_balanced_and_callback_first():
    rec = generate_recommendation(_build_comparison_report())
    safe = set(rec["evidence_summary"]["safe_strategies_above_threshold"])
    assert "balanced" in safe
    assert "callback_first" in safe


def test_conservative_is_not_disqualified_by_safety():
    rec = generate_recommendation(_build_comparison_report())
    disqualified = set(rec["evidence_summary"]["disqualified_strategies"])
    assert "conservative" not in disqualified
    safe = set(rec["evidence_summary"]["safe_strategies_above_threshold"])
    assert "conservative" not in safe


def test_recommendation_confidence_is_high_for_callback_first():
    rec = generate_recommendation(_build_comparison_report())
    assert rec["confidence_level"] == "high"


# ──────────────────────────────────────────────────────────────────
# Threshold behaviour
# ──────────────────────────────────────────────────────────────────

def test_threshold_1_0_still_recommends_callback_first():
    rec = generate_recommendation(_build_comparison_report(),
                                  pass_rate_threshold=1.0)
    assert rec["recommended_strategy"] == "callback_first"


def test_threshold_0_99_still_recommends_callback_first():
    rec = generate_recommendation(_build_comparison_report(),
                                  pass_rate_threshold=0.99)
    assert rec["recommended_strategy"] == "callback_first"


def test_threshold_0_9_keeps_callback_first_winner():
    rec = generate_recommendation(_build_comparison_report(),
                                  pass_rate_threshold=0.9)
    assert rec["recommended_strategy"] == "callback_first"


def test_extreme_threshold_yields_no_safe_promotion():
    rec = generate_recommendation(_build_comparison_report(),
                                  pass_rate_threshold=1.01)
    assert rec["recommendation_type"] == "no_safe_promotion"
    assert rec["recommended_strategy"] is None
    assert rec["confidence_level"] == "low"


# ──────────────────────────────────────────────────────────────────
# Safety logic
# ──────────────────────────────────────────────────────────────────

def test_synthetic_safety_violation_disqualifies_strategy():
    base = _build_comparison_report()
    base["failure_modes_by_strategy"]["callback_first"] = [
        {"reason": "unsafe_claim", "count": 1}
    ]
    rec = generate_recommendation(base)
    disqualified = set(rec["evidence_summary"]["disqualified_strategies"])
    assert "callback_first" in disqualified
    assert rec["recommended_strategy"] != "callback_first"


def test_recommended_strategy_is_none_when_all_unsafe():
    base = _build_comparison_report()
    for sid in list(base["failure_modes_by_strategy"].keys()):
        base["failure_modes_by_strategy"][sid] = [
            {"reason": "unsafe_claim", "count": 1}
        ]
    rec = generate_recommendation(base)
    assert rec["recommendation_type"] == "no_safe_promotion"
    assert rec["recommended_strategy"] is None


def test_safety_auto_fail_reasons_are_a_subset_of_scoring_failures():
    from app.services.simulation.scoring import FAILURE_REASONS
    for code in SAFETY_AUTO_FAIL_REASONS:
        assert code in FAILURE_REASONS, (
            f"PAS195 safety auto-fail code {code!r} not in scoring vocabulary"
        )


# ──────────────────────────────────────────────────────────────────
# Determinism
# ──────────────────────────────────────────────────────────────────

def test_recommendation_id_is_deterministic_for_same_inputs():
    a = generate_recommendation(_build_comparison_report())
    b = generate_recommendation(_build_comparison_report())
    assert a["recommendation_id"] == b["recommendation_id"]


def test_recommendation_id_changes_with_threshold():
    a = generate_recommendation(_build_comparison_report(),
                                pass_rate_threshold=0.95)
    b = generate_recommendation(_build_comparison_report(),
                                pass_rate_threshold=0.90)
    assert a["recommendation_id"] != b["recommendation_id"]


def test_recommendation_id_changes_with_comparison_report_id():
    a = generate_recommendation(_build_comparison_report(seed=1))
    b = generate_recommendation(_build_comparison_report(seed=2))
    assert a["recommendation_id"] != b["recommendation_id"]


# ──────────────────────────────────────────────────────────────────
# Import safety + forbidden language
# ──────────────────────────────────────────────────────────────────

_BANNED_IMPORT_HEADS = (
    "twilio",
    "slack_sdk",
    "openai",
    "anthropic",
    "dotenv",
    "supabase",
)

_BANNED_IMPORT_PREFIXES = (
    "app.services.slack",
    "app.routes.slack_command",
    "app.engine.state_machine",
    "app.engine",
)

_BANNED_CALLS = ("load_dotenv", "get_supabase")

_PAS195_FILES = (
    "app/services/simulation/recommendations.py",
    "scripts/pas195_generate_simulation_recommendation.py",
    "scripts/pas195_simulation_recommendation_readiness_check.py",
)


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


@pytest.mark.parametrize("relpath", _PAS195_FILES)
def test_no_banned_imports_in_pas195_file(relpath):
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


# Names that would indicate the recommendation engine is doing
# something live. These must not appear as function definitions or
# attribute accesses in PAS195 code.
_FORBIDDEN_NAMES = (
    "apply_recommendation",
    "deploy_strategy",
    "switch_strategy_live",
    "auto_apply",
    "auto_promote",
    "force_promote",
    "live_apply",
    "auto_deploy",
)


@pytest.mark.parametrize("relpath", (
    "app/services/simulation/recommendations.py",
    "scripts/pas195_generate_simulation_recommendation.py",
))
def test_no_autonomous_apply_names_in_pas195_source(relpath):
    src = _read(relpath)
    tree = ast.parse(src)
    names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            names.add(node.name)
        elif isinstance(node, ast.AsyncFunctionDef):
            names.add(node.name)
        elif isinstance(node, ast.Name):
            names.add(node.id)
        elif isinstance(node, ast.Attribute):
            names.add(node.attr)
    for tok in _FORBIDDEN_NAMES:
        assert tok not in names, f"{relpath} uses forbidden name {tok!r}"


# ──────────────────────────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────────────────────────

_RUNNER = _REPO_ROOT / "scripts" / "pas195_generate_simulation_recommendation.py"


def _run_cli(*argv):
    return subprocess.run(
        [sys.executable, str(_RUNNER), *argv],
        cwd=str(_REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=180,
    )


def test_runner_default_writes_recommendation():
    with tempfile.TemporaryDirectory() as tmp:
        proc = _run_cli("--output-dir", tmp, "--seed", "3")
        assert proc.returncode == 0, proc.stdout + proc.stderr
        files = list(pathlib.Path(tmp).glob("pas195_recommendation_*.json"))
        assert len(files) == 1
        payload = json.loads(files[0].read_text(encoding="utf-8"))
        for k in RECOMMENDATION_REQUIRED_KEYS:
            assert k in payload
        assert payload["status"] == "CANDIDATE"
        assert payload["operator_required"] is True


def test_runner_summary_only_does_not_write_file():
    with tempfile.TemporaryDirectory() as tmp:
        proc = _run_cli("--output-dir", tmp, "--summary-only")
        assert proc.returncode == 0, proc.stdout + proc.stderr
        files = list(pathlib.Path(tmp).glob("pas195_recommendation_*.json"))
        assert files == []


def test_runner_reads_existing_comparison_report():
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = pathlib.Path(tmp)
        comp_path = tmp_path / "comparison.json"
        comp_path.write_text(
            json.dumps(_build_comparison_report(seed=4)),
            encoding="utf-8",
        )
        proc = _run_cli(
            "--from-report", str(comp_path),
            "--output-dir", str(tmp_path),
            "--summary-only",
        )
        assert proc.returncode == 0, proc.stdout + proc.stderr
        assert "recommended=callback_first" in proc.stdout


def test_runner_rejects_invalid_threshold():
    proc = _run_cli("--pass-rate-threshold", "1.5", "--summary-only")
    assert proc.returncode == 2, proc.stdout + proc.stderr


# ──────────────────────────────────────────────────────────────────
# Readiness gate
# ──────────────────────────────────────────────────────────────────

_GATE = _REPO_ROOT / "scripts" / "pas195_simulation_recommendation_readiness_check.py"


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
    assert payload["phase"] == "PAS195"
    assert payload["verdict"] == "READY"
    assert payload["ready"] is True
    assert payload["fail_count"] == 0
    assert payload["check_count"] > 0


# ──────────────────────────────────────────────────────────────────
# Carry-forward
# ──────────────────────────────────────────────────────────────────

def test_pas193_pas194_tests_still_pass():
    proc = subprocess.run(
        [
            sys.executable, "-m", "pytest",
            "tests/mvp/test_pas193_simulation_layer.py",
            "tests/mvp/test_pas194_strategy_comparison.py",
            "-q",
        ],
        cwd=str(_REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=300,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr


# ──────────────────────────────────────────────────────────────────
# Doc invariants
# ──────────────────────────────────────────────────────────────────

def test_doc_present_and_carries_required_clauses():
    doc = _read("docs/pas195_simulation_recommendation_layer.md").lower()
    for clause in (
        "what pas195 proves",
        "what pas195 does not prove",
        "claimable",
        "still not claimable",
        "future pas196",
        "candidate",
        "operator review",
        "safety",
        "recommendation",
    ):
        assert clause in doc, f"doc missing clause {clause!r}"
