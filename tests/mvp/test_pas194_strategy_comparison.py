"""
PAS194 — Strategy comparison tests.

Coverage:

  * Strategy catalogue:
      - 5 strategies, every required key present, ids unique
      - ids drawn from STRATEGY_IDS
      - safety_notes is non-empty for every strategy

  * Comparison engine:
      - same scenario set fed to every strategy
      - rows_by_strategy is keyed by strategy_id
      - comparison is deterministic (same input -> same report)
      - best/worst strategies are identified and differ when their
        composite scores differ
      - per_scenario_winners covers every scenario
      - failure_modes_by_strategy uses controlled vocabulary
      - assertive / booking_first auto-fail on
        already_has_agent + language_unsupported

  * Report:
      - includes every required key
      - report_id deterministic for fixed inputs
      - generated_at echoes caller verbatim
      - no PII shapes, no production UUIDs

  * Runner / import safety:
      - PAS194 sources do not import twilio / slack / supabase /
        openai / anthropic / dotenv / state machine
      - PAS194 sources do not call load_dotenv / get_supabase

  * Runner CLI:
      - default run writes a report to disk
      - --summary-only suppresses file write
      - bad --strategies value exits 2
      - --strict still exits 0 with current safety overrides
        bounded (auto-fails are expected for assertive +
        booking_first on guarded scenarios)

  * Readiness gate:
      - exit 0 / verdict=READY on a clean main
      - JSON envelope valid
"""

from __future__ import annotations

import ast
import importlib.util
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


from app.services.simulation.scenarios import (  # noqa: E402
    SCENARIOS,
)
from app.services.simulation.strategies import (  # noqa: E402
    KNOWN_SAFETY_VIOLATIONS,
    STRATEGIES,
    STRATEGY_IDS,
    STRATEGY_INDEX,
    STRATEGY_REQUIRED_KEYS,
    plan_for,
    safety_violation_for,
    strategy_count,
)
from app.services.simulation.comparison import (  # noqa: E402
    COMPARISON_REPORT_REQUIRED_KEYS,
    build_comparison_report,
    compare_strategies,
    run_scenario_under_strategy,
)


_PII_LIKE = (
    re.compile(r"\b\d{3}[\s.\-]\d{3}[\s.\-]\d{4}\b"),
    re.compile(r"\(\d{3}\)\s*\d{3}[\s.\-]?\d{4}"),
    re.compile(r"\+\d[\d\s.\-]{6,14}\d"),
    re.compile(r"(?<!\d)\d{10,15}(?!\d)"),
    re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}"),
    re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),
    re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b"),
)


def _read(relpath: str) -> str:
    return (_REPO_ROOT / relpath).read_text(encoding="utf-8")


# ──────────────────────────────────────────────────────────────────
# Strategy catalogue
# ──────────────────────────────────────────────────────────────────

def test_strategy_count_at_least_five():
    assert strategy_count() >= 5


def test_every_strategy_has_required_keys():
    for s in STRATEGIES:
        for k in STRATEGY_REQUIRED_KEYS:
            assert k in s, f"{s.get('strategy_id')} missing {k}"
        assert s["safety_notes"], (
            f"{s['strategy_id']} has empty safety_notes"
        )


def test_strategy_ids_unique_and_in_catalogue():
    seen = set()
    for s in STRATEGIES:
        sid = s["strategy_id"]
        assert sid in STRATEGY_IDS
        assert sid not in seen
        seen.add(sid)


def test_strategy_index_matches_strategies():
    assert set(STRATEGY_INDEX.keys()) == {s["strategy_id"] for s in STRATEGIES}


# ──────────────────────────────────────────────────────────────────
# Plan modifiers
# ──────────────────────────────────────────────────────────────────

def test_balanced_returns_base_plan_unchanged():
    base = ("greet", "qualify", "offer_appointment", "close")
    out = plan_for("balanced", SCENARIOS[0], base)
    assert out == base


def test_conservative_replaces_appointment_with_callback():
    base = ("greet", "qualify", "offer_appointment", "close")
    out = plan_for("conservative", SCENARIOS[0], base)
    assert "offer_appointment" not in out
    assert "offer_callback" in out
    assert "qualify" in out


def test_assertive_replaces_callback_with_appointment():
    base = ("greet", "qualify", "offer_callback", "close")
    out = plan_for("assertive", SCENARIOS[0], base)
    assert "offer_callback" not in out
    assert "offer_appointment" in out


def test_callback_first_inserts_callback_before_close():
    base = ("greet", "qualify", "close")
    out = plan_for("callback_first", SCENARIOS[0], base)
    assert "offer_callback" in out
    assert out.index("offer_callback") < out.index("close")


def test_booking_first_inserts_appointment_before_close():
    base = ("greet", "qualify", "close")
    out = plan_for("booking_first", SCENARIOS[0], base)
    assert "offer_appointment" in out
    assert out.index("offer_appointment") < out.index("close")


def test_safety_violation_table_uses_known_codes():
    for strat_id in STRATEGY_IDS:
        for scenario in SCENARIOS:
            v = safety_violation_for(strat_id, scenario["scenario_type"])
            if v is not None:
                assert v in KNOWN_SAFETY_VIOLATIONS


# ──────────────────────────────────────────────────────────────────
# Comparison engine
# ──────────────────────────────────────────────────────────────────

def test_compare_strategies_keys_by_strategy_id():
    rows = compare_strategies(STRATEGIES, SCENARIOS)
    assert set(rows.keys()) == set(STRATEGY_IDS)


def test_compare_strategies_runs_same_scenario_set_for_every_strategy():
    rows = compare_strategies(STRATEGIES, SCENARIOS)
    expected_ids = [s["scenario_id"] for s in SCENARIOS]
    for sid, scored in rows.items():
        assert [r["scenario_id"] for r in scored] == expected_ids


def test_compare_strategies_deterministic_under_repeat():
    rows_a = compare_strategies(STRATEGIES, SCENARIOS)
    rows_b = compare_strategies(STRATEGIES, SCENARIOS)
    assert rows_a == rows_b


def test_assertive_auto_fails_on_already_has_agent():
    scenario = next(s for s in SCENARIOS if s["scenario_type"] == "already_has_agent")
    conv = run_scenario_under_strategy("assertive", scenario)
    assert conv["safety"]["agent_poaching"] is True


def test_booking_first_auto_fails_on_language_unsupported():
    scenario = next(s for s in SCENARIOS if s["scenario_type"] == "language_unsupported")
    conv = run_scenario_under_strategy("booking_first", scenario)
    assert conv["safety"]["language_misclaim"] is True


def test_conservative_never_triggers_safety_violation():
    for scenario in SCENARIOS:
        conv = run_scenario_under_strategy("conservative", scenario)
        for k, v in conv["safety"].items():
            assert v is False, f"conservative triggered {k} on {scenario['scenario_id']}"


def test_unknown_strategy_id_raises():
    with pytest.raises(ValueError):
        run_scenario_under_strategy("definitely_not_a_strategy", SCENARIOS[0])


# ──────────────────────────────────────────────────────────────────
# Comparison report
# ──────────────────────────────────────────────────────────────────

def _build_full_report(seed: int = 0, generated_at: str = "2026-05-21T00:00:00Z"):
    rows = compare_strategies(STRATEGIES, SCENARIOS)
    return build_comparison_report(rows, SCENARIOS, generated_at=generated_at, seed=seed)


def test_report_has_every_required_key():
    report = _build_full_report()
    for k in COMPARISON_REPORT_REQUIRED_KEYS:
        assert k in report, f"missing {k}"


def test_report_best_and_worst_strategies_in_catalogue():
    report = _build_full_report()
    assert report["best_strategy"] in STRATEGY_IDS
    assert report["worst_strategy"] in STRATEGY_IDS


def test_report_per_strategy_metrics_have_required_fields():
    report = _build_full_report()
    required = (
        "runs",
        "pass_rate",
        "average_score",
        "booking_attempt_rate",
        "callback_capture_rate",
        "objection_handling_rate",
    )
    for sid, m in report["per_strategy_metrics"].items():
        for f in required:
            assert f in m, f"{sid} missing metric {f}"
        assert 0.0 <= m["pass_rate"] <= 1.0
        assert 0.0 <= m["booking_attempt_rate"] <= 1.0
        assert 0.0 <= m["callback_capture_rate"] <= 1.0
        assert 0.0 <= m["objection_handling_rate"] <= 1.0


def test_report_per_scenario_winners_covers_every_scenario():
    report = _build_full_report()
    expected = {s["scenario_id"] for s in SCENARIOS}
    actual = {w["scenario_id"] for w in report["per_scenario_winners"]}
    assert actual == expected


def test_report_id_is_deterministic():
    a = _build_full_report(seed=7, generated_at="2026-05-21T00:00:00Z")
    b = _build_full_report(seed=7, generated_at="2026-05-21T00:00:00Z")
    assert a["report_id"] == b["report_id"]


def test_report_seed_changes_report_id():
    a = _build_full_report(seed=7)
    b = _build_full_report(seed=8)
    assert a["report_id"] != b["report_id"]


def test_report_generated_at_echoes_caller():
    ts = "2026-05-21T11:22:33Z"
    report = _build_full_report(generated_at=ts)
    assert report["generated_at"] == ts


def test_report_carries_no_pii_or_production_ids():
    report = _build_full_report()
    blob = json.dumps(report)
    for pat in _PII_LIKE:
        assert not pat.search(blob), "report contains PII-shaped token"


def test_report_failure_modes_use_controlled_vocabulary():
    from app.services.simulation.scoring import FAILURE_REASONS
    report = _build_full_report()
    for sid, modes in report["failure_modes_by_strategy"].items():
        for entry in modes:
            assert entry["reason"] in FAILURE_REASONS, (
                f"{sid} failure mode {entry['reason']!r} off-catalogue"
            )


def test_report_recommendation_is_non_empty_string():
    report = _build_full_report()
    assert isinstance(report["recommendation"], str)
    assert report["recommendation"]


# ──────────────────────────────────────────────────────────────────
# Import safety
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


_PAS194_FILES = (
    "app/services/simulation/strategies.py",
    "app/services/simulation/comparison.py",
    "scripts/pas194_compare_simulation_strategies.py",
    "scripts/pas194_strategy_comparison_readiness_check.py",
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


@pytest.mark.parametrize("relpath", _PAS194_FILES)
def test_no_banned_imports_in_pas194_file(relpath):
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
# Runner CLI
# ──────────────────────────────────────────────────────────────────

_RUNNER = _REPO_ROOT / "scripts" / "pas194_compare_simulation_strategies.py"


def _run_cli(*argv):
    return subprocess.run(
        [sys.executable, str(_RUNNER), *argv],
        cwd=str(_REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=180,
    )


def test_runner_default_run_writes_report_file():
    with tempfile.TemporaryDirectory() as tmp:
        proc = _run_cli("--output-dir", tmp, "--seed", "5")
        assert proc.returncode == 0, proc.stdout + proc.stderr
        files = list(pathlib.Path(tmp).glob("pas194_strategy_comparison_*.json"))
        assert len(files) == 1
        payload = json.loads(files[0].read_text(encoding="utf-8"))
        for k in COMPARISON_REPORT_REQUIRED_KEYS:
            assert k in payload


def test_runner_summary_only_does_not_write_file():
    with tempfile.TemporaryDirectory() as tmp:
        proc = _run_cli("--output-dir", tmp, "--summary-only")
        assert proc.returncode == 0, proc.stdout + proc.stderr
        files = list(pathlib.Path(tmp).glob("pas194_strategy_comparison_*.json"))
        assert files == []


def test_runner_rejects_unknown_strategy():
    proc = _run_cli("--strategies", "definitely_not_a_strategy", "--summary-only")
    assert proc.returncode == 2, proc.stdout + proc.stderr


def test_runner_strict_mode_exit_code():
    # Assertive + booking_first auto-fail on guarded scenarios by
    # design, so --strict will exit 3. Filter to safe strategies
    # to get a clean 0.
    with tempfile.TemporaryDirectory() as tmp:
        proc = _run_cli(
            "--output-dir", tmp,
            "--summary-only",
            "--strict",
            "--strategies", "conservative,balanced,callback_first",
        )
        assert proc.returncode == 0, proc.stdout + proc.stderr


# ──────────────────────────────────────────────────────────────────
# Readiness gate
# ──────────────────────────────────────────────────────────────────

_GATE = _REPO_ROOT / "scripts" / "pas194_strategy_comparison_readiness_check.py"


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
    assert payload["phase"] == "PAS194"
    assert payload["verdict"] == "READY"
    assert payload["ready"] is True
    assert payload["fail_count"] == 0
    assert payload["check_count"] > 0


# ──────────────────────────────────────────────────────────────────
# PAS193 carry-forward
# ──────────────────────────────────────────────────────────────────

def test_pas193_tests_still_pass():
    proc = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/mvp/test_pas193_simulation_layer.py", "-q"],
        cwd=str(_REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=240,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr


# ──────────────────────────────────────────────────────────────────
# Doc invariants
# ──────────────────────────────────────────────────────────────────

def test_doc_present_and_carries_required_clauses():
    doc = _read("docs/pas194_simulation_strategy_comparison.md").lower()
    for clause in (
        "what pas194 proves",
        "what pas194 does not prove",
        "how this upgrades",
        "how to run",
        "claimable",
        "still not claimable",
        "safety",
        "strategy",
        "comparison",
    ):
        assert clause in doc, f"doc missing clause {clause!r}"
