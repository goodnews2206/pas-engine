"""
PAS202 — Operator evidence-digest surface tests.

Coverage:

  * Happy path:
      - format_operator_summary accepts a valid PAS201 digest
      - operator summary carries every required key
      - evidence_strength surfaces in all three renderings
      - recommended_next_action surfaces in all three renderings
      - text renderer is deterministic
      - Slack renderer is deterministic
      - structured summary is deterministic
      - claimable_now / not_claimable_yet preserved verbatim

  * Bounded-environment rejection:
      - digest.phase != PAS201 raises
      - digest.allowed_environment != SIMULATION_ONLY raises
      - digest.live_behavior_changed != False raises
      - missing required keys raises
      - non-dict input raises

  * Safe-output invariants:
      - no PII tokens in any rendering
      - no production brokerage IDs in any rendering
      - no live-routing assertions in any rendering
      - forbidden output tokens never emitted
      - Slack rendering does not exceed the configured byte cap

  * Source-surface invariants:
      - no forbidden status literals
      - no live-mutation identifiers
      - no banned imports (slack_sdk, twilio, supabase, openai,
        anthropic, dotenv, state machine)

  * CLI:
      - happy path renders text
      - --json prints structured JSON
      - --slack prints Slack markdown
      - --write-summary writes operator-summary JSON
      - missing --digest exits 2
      - rejected digest exits 2

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

import pytest


_REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))


from app.services.simulation.evidence_digest import (  # noqa: E402
    build_evidence_digest,
)
from app.services.simulation.evidence_digest_surface import (  # noqa: E402
    FORBIDDEN_OUTPUT_TOKENS,
    OPERATOR_SUMMARY_REQUIRED_KEYS,
    SLACK_OUTPUT_MAX_CHARS,
    EvidenceDigestSurfaceValidationError,
    format_digest_as_text,
    format_digest_for_slack,
    format_operator_summary,
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
GEN_AT     = "2026-05-22T08:00:00Z"


def _candidate_recommendation() -> dict:
    return {
        "recommendation_id":    REC_ID,
        "status":               "CANDIDATE",
        "operator_required":    True,
        "recommended_strategy": "callback_first",
        "rejected_strategy":    "assertive",
        "recommendation_type":  "promote_strategy",
        "confidence_level":     "high",
        "pass_rate_threshold":  0.95,
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


def _ready_package() -> dict:
    return {
        "package_id":            PACKAGE_ID,
        "phase":                 "PAS197",
        "recommendation_id":     REC_ID,
        "review_id":             REVIEW_ID,
        "strategy_id":           "callback_first",
        "status":                "READY_FOR_MANUAL_TEST",
        "live_behavior_changed": False,
        "allowed_environment":   "SIMULATION_ONLY",
        "test_plan":             [],
        "success_metrics":       [],
        "rollback_notes":        [],
        "safety_notes":          [],
        "created_at":            "2026-05-21T12:22:47Z",
    }


def _build_digest() -> dict:
    rec = _candidate_recommendation()
    rev = _approved_review()
    pkg = _ready_package()
    rt = execute_manual_test_runtime(
        pkg, created_at="2026-05-22T04:00:00Z",
    )
    insp = build_inspection(rec, rev, pkg, rt, generated_at=GEN_AT)
    beh = build_behavioral_evaluation(
        rt, generated_at=GEN_AT, inspection=insp,
    )
    return build_evidence_digest(
        rec, rev, pkg, rt, insp, beh, generated_at=GEN_AT,
    )


# ──────────────────────────────────────────────────────────────────
# Happy path
# ──────────────────────────────────────────────────────────────────

def test_operator_summary_built_from_valid_digest():
    s = format_operator_summary(_build_digest())
    assert isinstance(s, dict)


def test_operator_summary_carries_every_required_key():
    s = format_operator_summary(_build_digest())
    for k in OPERATOR_SUMMARY_REQUIRED_KEYS:
        assert k in s, f"missing {k}"


def test_operator_summary_mirrors_strategy_and_strength():
    digest = _build_digest()
    s = format_operator_summary(digest)
    assert s["strategy_id"]       == digest["strategy_id"]
    assert s["evidence_strength"] == digest["evidence_strength"]


def test_operator_summary_preserves_claim_lists_verbatim():
    digest = _build_digest()
    s = format_operator_summary(digest)
    assert s["claimable_now"]      == list(digest["claimable_now"])
    assert s["not_claimable_yet"]  == list(digest["not_claimable_yet"])


def test_text_renderer_includes_evidence_strength():
    digest = _build_digest()
    txt = format_digest_as_text(digest)
    assert digest["evidence_strength"] in txt


def test_text_renderer_includes_recommended_next_action():
    digest = _build_digest()
    txt = format_digest_as_text(digest)
    # PAS204-B humanises the recommended-next-action token into a
    # plain-English sentence. The raw token no longer appears
    # verbatim, but the humanised phrase always does.
    assert "Recommended next:" in txt
    assert "Review the rehearsal evidence" in txt or "pilot" in txt


def test_text_renderer_is_deterministic():
    d = _build_digest()
    assert format_digest_as_text(d) == format_digest_as_text(d)


def test_structured_summary_is_deterministic():
    d = _build_digest()
    assert format_operator_summary(d) == format_operator_summary(d)


def test_slack_renderer_includes_evidence_strength():
    digest = _build_digest()
    out = format_digest_for_slack(digest)
    assert digest["evidence_strength"] in out


def test_slack_renderer_includes_recommended_next_action():
    digest = _build_digest()
    out = format_digest_for_slack(digest)
    # PAS204-B humanises the recommended-next-action token. The
    # raw token no longer appears verbatim, but the humanised
    # phrase always does.
    assert "*Recommended next:*" in out
    assert "Review the rehearsal evidence" in out or "pilot" in out


def test_slack_renderer_is_deterministic():
    d = _build_digest()
    assert format_digest_for_slack(d) == format_digest_for_slack(d)


def test_slack_renderer_under_byte_cap():
    out = format_digest_for_slack(_build_digest())
    assert len(out) <= SLACK_OUTPUT_MAX_CHARS


def test_renderers_include_simulation_only_marker():
    digest = _build_digest()
    txt = format_digest_as_text(digest)
    slack = format_digest_for_slack(digest)
    assert "SIMULATION_ONLY" in txt
    assert "SIMULATION_ONLY" in slack


# ──────────────────────────────────────────────────────────────────
# Bounded-environment rejection
# ──────────────────────────────────────────────────────────────────

def test_non_dict_input_rejected():
    with pytest.raises(EvidenceDigestSurfaceValidationError):
        format_operator_summary("not a dict")  # type: ignore


def test_non_pas201_phase_rejected():
    d = _build_digest()
    d["phase"] = "PAS200"
    with pytest.raises(EvidenceDigestSurfaceValidationError):
        format_operator_summary(d)


def test_wrong_environment_rejected():
    d = _build_digest()
    d["allowed_environment"] = "PRODUCTION"
    with pytest.raises(EvidenceDigestSurfaceValidationError):
        format_operator_summary(d)


def test_live_behavior_changed_true_rejected():
    d = _build_digest()
    d["live_behavior_changed"] = True
    with pytest.raises(EvidenceDigestSurfaceValidationError):
        format_operator_summary(d)


def test_missing_required_key_rejected():
    d = _build_digest()
    del d["operator_summary"]
    with pytest.raises(EvidenceDigestSurfaceValidationError):
        format_operator_summary(d)


# ──────────────────────────────────────────────────────────────────
# Safe-output invariants
# ──────────────────────────────────────────────────────────────────

_PHONE_RES = (
    re.compile(r"\b\d{3}[\s.\-]\d{3}[\s.\-]\d{4}\b"),
    re.compile(r"\(\d{3}\)\s*\d{3}[\s.\-]?\d{4}"),
)

_PROD_ID_RES = (
    re.compile(r"\bbrokerage_id\s*=\s*[\"']?[0-9a-fA-F\-]{8,}[\"']?"),
    re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b"),
)


def test_output_contains_no_phone_numbers():
    digest = _build_digest()
    for text in (
        format_digest_as_text(digest),
        format_digest_for_slack(digest),
        json.dumps(format_operator_summary(digest), sort_keys=True),
    ):
        for pat in _PHONE_RES:
            assert not pat.search(text), "phone-shaped token in output"


def test_output_contains_no_production_brokerage_ids():
    digest = _build_digest()
    for text in (
        format_digest_as_text(digest),
        format_digest_for_slack(digest),
        json.dumps(format_operator_summary(digest), sort_keys=True),
    ):
        for pat in _PROD_ID_RES:
            assert not pat.search(text), "production brokerage id in output"


def test_output_contains_no_live_routing_assertions():
    digest = _build_digest()
    for text in (
        format_digest_as_text(digest),
        format_digest_for_slack(digest),
    ):
        lower = text.lower()
        for tok in FORBIDDEN_OUTPUT_TOKENS:
            assert tok not in lower, (
                f"forbidden token {tok!r} appeared in output"
            )
        # No accidental phrase claiming live routing is happening.
        for phrase in (
            "live call active",
            "production strategy enabled",
            "real lead routed",
            "calling live",
        ):
            assert phrase not in lower


def test_text_output_carries_no_raw_internal_tokens():
    # PAS204-B humanises the text rendering. The assertion shifts
    # from "every line is a structured label" to "no underscore-
    # snake-case PAS internal closed-vocab tokens leak verbatim
    # into the output". The fixed labels SIMULATION_ONLY and the
    # individual artifact IDs (pas195-rec-..., pas200-beval-...)
    # are still allowed because they are not internal jargon —
    # they're stable audit identifiers.
    digest = _build_digest()
    txt = format_digest_as_text(digest)
    raw_internal_tokens = (
        "runtime_pass_rate_100_percent",
        "runtime_pass_rate_at_or_above_95_percent",
        "runtime_pass_rate_at_or_above_75_percent",
        "runtime_pass_rate_below_75_percent",
        "safety_outcome_clean",
        "safety_outcome_auto_fail",
        "lineage_intact",
        "lineage_broken",
        "artifact_integrity_complete",
        "artifact_integrity_incomplete",
        "behavioral_low_friction_observed",
        "behavioral_high_friction_observed",
        "behavioral_good_pacing_observed",
        "behavioral_high_pressure_observed",
        "behavioral_low_trust_observed",
        "behavioral_trust_preservation_observed",
        "behavioral_callback_continuity_observed",
        "behavioral_early_escalation_observed",
        "no_live_behavior_change_anywhere_in_lineage",
        "behavioral_evaluation_emitted_deterministically",
        "lineage_inspectable_end_to_end",
        "manual_test_executed_in_simulation_only",
        "operator_approved_strategy_for_manual_test",
        "safety_auto_fails_remain_absolute",
        "synthetic_rehearsal_passed_for_strategy",
        "no_pii_in_simulation_artifacts",
        "live_call_routing_remains_out_of_scope",
        "calibration_against_live_call_outcomes_pending",
        "automated_promotion_to_runtime_strategy_pending",
        "real_lead_exposure_remains_out_of_scope",
        "slack_operator_surface_for_runtime_runs_pending",
        "review_digest_then_decide_pilot_step",
        "expand_synthetic_catalogue_before_pilot",
        "rerun_manual_test_with_alternative_strategy",
        "block_until_safety_issue_resolved",
    )
    for tok in raw_internal_tokens:
        assert tok not in txt, (
            f"PAS202 text output leaked raw internal token {tok!r}"
        )


def test_slack_output_carries_no_raw_internal_tokens():
    digest = _build_digest()
    out = format_digest_for_slack(digest)
    raw_internal_tokens = (
        "runtime_pass_rate_100_percent",
        "safety_outcome_clean",
        "lineage_intact",
        "artifact_integrity_complete",
        "behavioral_low_friction_observed",
        "behavioral_low_trust_observed",
        "behavioral_callback_continuity_observed",
        "no_live_behavior_change_anywhere_in_lineage",
        "lineage_inspectable_end_to_end",
        "manual_test_executed_in_simulation_only",
        "operator_approved_strategy_for_manual_test",
        "no_pii_in_simulation_artifacts",
        "live_call_routing_remains_out_of_scope",
        "calibration_against_live_call_outcomes_pending",
        "automated_promotion_to_runtime_strategy_pending",
        "real_lead_exposure_remains_out_of_scope",
        "review_digest_then_decide_pilot_step",
    )
    for tok in raw_internal_tokens:
        assert tok not in out, (
            f"PAS202 Slack output leaked raw internal token {tok!r}"
        )


def test_summary_does_not_mutate_input_digest():
    digest = _build_digest()
    before = json.dumps(digest, sort_keys=True)
    format_operator_summary(digest)
    format_digest_as_text(digest)
    format_digest_for_slack(digest)
    after = json.dumps(digest, sort_keys=True)
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
    "send_slack_message",
    "post_to_slack",
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


_PAS202_FILES = (
    "app/services/simulation/evidence_digest_surface.py",
    "scripts/pas202_view_simulation_evidence_digest.py",
    "scripts/pas202_evidence_digest_surface_readiness_check.py",
)


_PAS202_FILES_FOR_FORBIDDEN_LITERAL_SCAN = (
    "app/services/simulation/evidence_digest_surface.py",
    "scripts/pas202_view_simulation_evidence_digest.py",
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


@pytest.mark.parametrize("relpath", _PAS202_FILES_FOR_FORBIDDEN_LITERAL_SCAN)
def test_forbidden_status_literals_absent(relpath):
    consts = _string_constants(_read(relpath))
    for tok in _FORBIDDEN_STATUS_LITERALS:
        assert tok not in consts, (
            f"{relpath} carries forbidden status literal {tok!r}"
        )


@pytest.mark.parametrize("relpath", _PAS202_FILES_FOR_FORBIDDEN_LITERAL_SCAN)
def test_forbidden_identifiers_absent(relpath):
    names = _identifier_names(_read(relpath))
    for tok in _FORBIDDEN_IDENTIFIERS:
        assert tok not in names, (
            f"{relpath} carries forbidden identifier {tok!r}"
        )


@pytest.mark.parametrize("relpath", _PAS202_FILES)
def test_no_banned_imports_in_pas202_file(relpath):
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

_RUNNER = _REPO_ROOT / "scripts" / "pas202_view_simulation_evidence_digest.py"


def _run_cli(*argv):
    return subprocess.run(
        [sys.executable, str(_RUNNER), *argv],
        cwd=str(_REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=120,
    )


def _write_digest_file(tp: pathlib.Path,
                       *, mutate: dict = None) -> pathlib.Path:
    digest = _build_digest()
    if mutate:
        for k, v in mutate.items():
            digest[k] = v
    fp = tp / "digest.json"
    fp.write_text(json.dumps(digest), encoding="utf-8")
    return fp


def test_runner_default_prints_text_summary():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        fp = _write_digest_file(tp)
        proc = _run_cli("--digest", str(fp))
        assert proc.returncode == 0, proc.stdout + proc.stderr
        # PAS204-B humanised header keeps the audit identifier
        # and the SIMULATION_ONLY marker but rewrites the
        # narrative labels.
        assert "PAS201 evidence digest" in proc.stdout
        assert "SIMULATION_ONLY" in proc.stdout
        assert "Evidence:" in proc.stdout or "Recommended next:" in proc.stdout


def test_runner_json_prints_structured_summary():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        fp = _write_digest_file(tp)
        proc = _run_cli("--digest", str(fp), "--json")
        assert proc.returncode == 0, proc.stdout + proc.stderr
        # Locate the JSON payload in stdout.
        payload_str = proc.stdout[proc.stdout.find("{"):]
        payload = json.loads(payload_str)
        for k in OPERATOR_SUMMARY_REQUIRED_KEYS:
            assert k in payload


def test_runner_slack_prints_markdown():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        fp = _write_digest_file(tp)
        proc = _run_cli("--digest", str(fp), "--slack")
        assert proc.returncode == 0, proc.stdout + proc.stderr
        # PAS204-B renames the Slack header. Audit markers
        # (SIMULATION_ONLY, the digest id) are still present.
        assert "*PAS rehearsal evidence*" in proc.stdout
        assert "SIMULATION_ONLY" in proc.stdout
        assert "*Recommended next:*" in proc.stdout
        assert "*Summary:*" in proc.stdout


def test_runner_write_summary_writes_file():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        fp = _write_digest_file(tp)
        proc = _run_cli(
            "--digest",         str(fp),
            "--output-dir",     str(tp),
            "--write-summary",
        )
        assert proc.returncode == 0, proc.stdout + proc.stderr
        files = list(tp.glob("pas202_evidence_digest_operator_summary_*.json"))
        assert len(files) == 1
        payload = json.loads(files[0].read_text(encoding="utf-8"))
        for k in OPERATOR_SUMMARY_REQUIRED_KEYS:
            assert k in payload


def test_runner_missing_digest_exits_2():
    proc = _run_cli()
    assert proc.returncode == 2


def test_runner_rejected_digest_exits_2():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        fp = _write_digest_file(tp, mutate={"phase": "PAS200"})
        proc = _run_cli("--digest", str(fp))
        assert proc.returncode == 2


# ──────────────────────────────────────────────────────────────────
# Readiness gate
# ──────────────────────────────────────────────────────────────────

_GATE = _REPO_ROOT / "scripts" / "pas202_evidence_digest_surface_readiness_check.py"


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
    assert payload["phase"] == "PAS202"
    assert payload["verdict"] == "READY"
    assert payload["ready"] is True
    assert payload["fail_count"] == 0
    assert payload["check_count"] > 0


# ──────────────────────────────────────────────────────────────────
# Doc invariants
# ──────────────────────────────────────────────────────────────────

def test_doc_present_and_carries_required_clauses():
    doc = _read("docs/pas202_evidence_digest_surface.md").lower()
    for clause in (
        "what pas202 proves",
        "what pas202 does not prove",
        "claimable",
        "future pas203",
        "operator",
        "safety",
        "simulation_only",
        "surface",
        "digest",
        "read",
    ):
        assert clause in doc, f"doc missing clause {clause!r}"
