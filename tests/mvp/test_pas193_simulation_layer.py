"""
PAS193 — Simulation layer tests.

Coverage:

  * Scenario catalogue:
      - count >= 20
      - schema integrity (required keys, value shapes)
      - scenario_id uniqueness + naming convention
      - at most one unsupported scenario, and it must be the
        Spanish-language placeholder
      - no scenario carries phone/email/SSN/UUID PII shapes

  * Runner imports / safety:
      - source of the runner does not import twilio
      - source of the runner does not import any Slack client
      - source of the simulation package does not import twilio
        or Slack
      - source of the simulation package does not import the
        live state machine

  * Scorer:
      - deterministic (same input → same output across runs)
      - unsafe outputs auto-fail (score=0, passed=False)
      - PII-shaped agent utterance auto-fails
      - empty transcript auto-fails
      - unsupported scenarios only pass with safe handoff

  * Report:
      - includes every required key
      - rates are between 0 and 1
      - report_id deterministic for fixed inputs
      - generated_at echoes the caller value verbatim
      - no real PII patterns, no production brokerage IDs

  * Runner CLI:
      - --count 0 succeeds with zero-result report
      - --count 20 succeeds and writes a JSON file under
        reports/simulations/
      - --summary-only never writes a file
      - --strict exit 0 (current adapter never auto-fails)
"""

from __future__ import annotations

import ast
import importlib.util
import json
import os
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
    SCENARIO_REQUIRED_KEYS,
    SCENARIO_TYPES,
    SUPPORTED_SCENARIOS,
    UNSUPPORTED_SCENARIOS,
    scenario_count,
)
from app.services.simulation.adapter import (  # noqa: E402
    AGENT_ACTIONS,
    run_batch,
    run_scenario,
)
from app.services.simulation.scoring import (  # noqa: E402
    FAILURE_REASONS,
    score_conversation,
)
from app.services.simulation.report import (  # noqa: E402
    REPORT_REQUIRED_KEYS,
    build_report,
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
# Scenario catalogue
# ──────────────────────────────────────────────────────────────────

def test_scenario_count_at_least_twenty():
    assert scenario_count() >= 20


def test_every_scenario_has_required_keys():
    for s in SCENARIOS:
        for key in SCENARIO_REQUIRED_KEYS:
            assert key in s, f"{s.get('scenario_id')} missing {key}"


def test_scenario_ids_are_unique_and_well_formed():
    seen = set()
    pat = re.compile(r"^pas193_sim_[a-z0-9_]+$")
    for s in SCENARIOS:
        sid = s["scenario_id"]
        assert pat.match(sid), f"bad id shape: {sid}"
        assert sid not in seen, f"duplicate id: {sid}"
        seen.add(sid)


def test_scenario_types_drawn_from_catalogue():
    for s in SCENARIOS:
        assert s["scenario_type"] in SCENARIO_TYPES, (
            f"{s['scenario_id']} has off-catalogue type "
            f"{s['scenario_type']!r}"
        )


def test_only_language_placeholder_is_unsupported():
    assert len(UNSUPPORTED_SCENARIOS) == 1
    assert UNSUPPORTED_SCENARIOS[0]["scenario_type"] == "language_unsupported"
    assert len(SUPPORTED_SCENARIOS) == scenario_count() - 1


def test_no_scenario_carries_pii_shapes():
    for s in SCENARIOS:
        blob = " ".join([
            s["initial_message"],
            " ".join(s["lead_script"]),
            s["lead_profile"],
        ])
        for pat in _PII_LIKE:
            assert not pat.search(blob), (
                f"{s['scenario_id']} carries PII-shaped token"
            )


# ──────────────────────────────────────────────────────────────────
# Runner / package import safety
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

_SIMULATION_FILES = (
    "app/services/simulation/__init__.py",
    "app/services/simulation/scenarios.py",
    "app/services/simulation/adapter.py",
    "app/services/simulation/scoring.py",
    "app/services/simulation/report.py",
    "scripts/pas193_run_simulation_batch.py",
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


@pytest.mark.parametrize("relpath", _SIMULATION_FILES)
def test_no_banned_imports_in_simulation_layer(relpath):
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


def test_runner_does_not_import_state_machine():
    imports, _ = _imports_and_calls(_read("scripts/pas193_run_simulation_batch.py"))
    for mod in imports:
        assert "state_machine" not in mod
        assert not mod.startswith("app.engine")


# ──────────────────────────────────────────────────────────────────
# Scorer determinism + safety
# ──────────────────────────────────────────────────────────────────

def test_scorer_is_deterministic_under_repeat():
    s = SCENARIOS[0]
    conv = run_scenario(s)
    a = score_conversation(conv, s)
    b = score_conversation(conv, s)
    assert a == b


def test_scorer_full_pass_for_high_intent_buyer():
    s = SCENARIOS[0]
    result = score_conversation(run_scenario(s), s)
    assert result["passed"] is True
    assert result["score"] >= 50
    assert result["recommendation_label"] in ("promote_to_pilot", "needs_rehearsal")


def test_unsafe_flag_forces_score_zero():
    s = SCENARIOS[0]
    conv = run_scenario(s)
    conv["safety"]["unsafe_claim"] = True
    result = score_conversation(conv, s)
    assert result["score"] == 0
    assert result["passed"] is False
    assert "unsafe_claim" in result["failure_reasons"]
    assert result["recommendation_label"] == "block_unsafe"


def test_pii_pattern_in_agent_utterance_forces_failure():
    s = SCENARIOS[0]
    conv = run_scenario(s)
    conv["agent_utterances"] = list(conv["agent_utterances"]) + [
        "Call me at +1 555-123-4567",
    ]
    result = score_conversation(conv, s)
    assert result["passed"] is False
    assert "pii_pattern_in_utterance" in result["failure_reasons"]
    assert result["score"] == 0


def test_empty_transcript_auto_fails():
    s = SCENARIOS[0]
    conv = run_scenario(s)
    conv["turns"] = []
    result = score_conversation(conv, s)
    assert result["passed"] is False
    assert "empty_transcript" in result["failure_reasons"]
    assert result["score"] == 0


def test_unsupported_scenario_must_handoff_safely():
    s = UNSUPPORTED_SCENARIOS[0]
    conv = run_scenario(s)
    result = score_conversation(conv, s)
    assert result["recommendation_label"] == "unsupported_profile"
    assert "objection_handled" in conv["capabilities"]
    assert "callback_captured" in conv["capabilities"]
    assert result["passed"] is True


def test_failure_reasons_are_all_drawn_from_controlled_vocabulary():
    s = SCENARIOS[0]
    conv = run_scenario(s)
    conv["safety"]["unsafe_claim"] = True
    conv["safety"]["pii_leak"] = True
    result = score_conversation(conv, s)
    for reason in result["failure_reasons"]:
        assert reason in FAILURE_REASONS


# ──────────────────────────────────────────────────────────────────
# Adapter action vocabulary
# ──────────────────────────────────────────────────────────────────

def test_adapter_only_emits_known_actions():
    for s in SCENARIOS:
        conv = run_scenario(s)
        for action in conv["actions"]:
            assert action in AGENT_ACTIONS


def test_run_batch_returns_one_record_per_scenario():
    batch = run_batch(SCENARIOS)
    assert len(batch) == len(SCENARIOS)
    for record, scenario in zip(batch, SCENARIOS):
        assert record["scenario_id"] == scenario["scenario_id"]


# ──────────────────────────────────────────────────────────────────
# Report
# ──────────────────────────────────────────────────────────────────

def _full_scored_batch():
    scored = []
    for s in SCENARIOS:
        result = score_conversation(run_scenario(s), s)
        scored.append({
            "scenario_id":           s["scenario_id"],
            "scenario_type":         s["scenario_type"],
            "supported":             s["supported"],
            "score":                 result["score"],
            "passed":                result["passed"],
            "failure_reasons":       result["failure_reasons"],
            "recommendation_label":  result["recommendation_label"],
            "capabilities_observed": result["capabilities_observed"],
            "missing_criteria":      result["missing_criteria"],
        })
    return scored


def test_report_carries_every_required_key():
    scored = _full_scored_batch()
    report = build_report(scored, generated_at="2026-05-21T00:00:00Z", seed=42)
    for k in REPORT_REQUIRED_KEYS:
        assert k in report, f"report missing {k}"


def test_report_rates_are_unit_interval():
    scored = _full_scored_batch()
    report = build_report(scored, generated_at="2026-05-21T00:00:00Z", seed=42)
    for k in (
        "pass_rate",
        "booking_attempt_rate",
        "callback_capture_rate",
        "objection_handling_rate",
    ):
        assert 0.0 <= float(report[k]) <= 1.0


def test_report_id_is_deterministic():
    scored = _full_scored_batch()
    r1 = build_report(scored, generated_at="2026-05-21T00:00:00Z", seed=7)
    r2 = build_report(scored, generated_at="2026-05-21T00:00:00Z", seed=7)
    assert r1["report_id"] == r2["report_id"]


def test_report_seed_changes_report_id():
    scored = _full_scored_batch()
    r1 = build_report(scored, generated_at="2026-05-21T00:00:00Z", seed=7)
    r2 = build_report(scored, generated_at="2026-05-21T00:00:00Z", seed=8)
    assert r1["report_id"] != r2["report_id"]


def test_report_generated_at_echoes_caller():
    scored = _full_scored_batch()
    ts = "2026-05-21T12:34:56Z"
    report = build_report(scored, generated_at=ts, seed=0)
    assert report["generated_at"] == ts


def test_report_carries_no_pii_or_production_ids():
    scored = _full_scored_batch()
    blob = json.dumps(build_report(scored, generated_at="2026-05-21T00:00:00Z", seed=0))
    for pat in _PII_LIKE:
        assert not pat.search(blob), "report contains PII-shaped token"


# ──────────────────────────────────────────────────────────────────
# Runner CLI
# ──────────────────────────────────────────────────────────────────

_RUNNER = _REPO_ROOT / "scripts" / "pas193_run_simulation_batch.py"


def _run_cli(*argv):
    proc = subprocess.run(
        [sys.executable, str(_RUNNER), *argv],
        cwd=str(_REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=180,
    )
    return proc


def test_runner_count_zero_succeeds():
    with tempfile.TemporaryDirectory() as tmp:
        proc = _run_cli("--count", "0", "--output-dir", tmp, "--summary-only")
        assert proc.returncode == 0, proc.stdout + proc.stderr
        assert "runs=0" in proc.stdout


def test_runner_default_count_writes_report_file():
    with tempfile.TemporaryDirectory() as tmp:
        proc = _run_cli("--count", "20", "--output-dir", tmp, "--seed", "11")
        assert proc.returncode == 0, proc.stdout + proc.stderr
        files = list(pathlib.Path(tmp).glob("pas193_simulation_batch_*.json"))
        assert len(files) == 1
        payload = json.loads(files[0].read_text(encoding="utf-8"))
        for k in REPORT_REQUIRED_KEYS:
            assert k in payload
        assert payload["total_simulations"] == 20


def test_runner_summary_only_does_not_write_file():
    with tempfile.TemporaryDirectory() as tmp:
        proc = _run_cli("--count", "5", "--output-dir", tmp, "--summary-only")
        assert proc.returncode == 0, proc.stdout + proc.stderr
        files = list(pathlib.Path(tmp).glob("pas193_simulation_batch_*.json"))
        assert files == []


def test_runner_strict_mode_passes_for_clean_adapter():
    with tempfile.TemporaryDirectory() as tmp:
        proc = _run_cli("--count", "20", "--output-dir", tmp,
                        "--summary-only", "--strict")
        assert proc.returncode == 0, proc.stdout + proc.stderr


# ──────────────────────────────────────────────────────────────────
# Readiness gate
# ──────────────────────────────────────────────────────────────────

_GATE = _REPO_ROOT / "scripts" / "pas193_simulation_layer_readiness_check.py"


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
    assert payload["phase"] == "PAS193"
    assert payload["verdict"] == "READY"
    assert payload["ready"] is True
    assert payload["fail_count"] == 0
    assert payload["check_count"] > 0


# ──────────────────────────────────────────────────────────────────
# Doc invariants
# ──────────────────────────────────────────────────────────────────

def test_doc_present_and_carries_required_clauses():
    doc = _read("docs/pas193_simulation_layer_proof.md").lower()
    for clause in (
        "purpose",
        "what pas193 proves",
        "what pas193 does not prove",
        "safety constraints",
        "how to run",
        "claimable",
        "still not claimable",
    ):
        assert clause in doc, f"doc missing clause {clause!r}"
