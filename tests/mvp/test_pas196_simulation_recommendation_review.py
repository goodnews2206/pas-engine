"""
PAS196 — Simulation recommendation review tests.

Coverage:

  * Status machine:
      - ALLOWED_STATUSES exactly == {CANDIDATE,
        APPROVED_FOR_MANUAL_TEST, REJECTED, EXPIRED}
      - ALLOWED_TRANSITIONS exactly the four allowed pairs
      - is_allowed_transition correct on positive + negative cases

  * Forbidden status values:
      - The strings APPROVED, APPLIED, AUTO_APPLIED, LIVE, DEPLOYED
        never appear as string literals or identifier names in the
        review service or the review CLI

  * submit_review happy paths:
      - approve-manual-test transitions CANDIDATE ->
        APPROVED_FOR_MANUAL_TEST
      - reject transitions CANDIDATE -> REJECTED
      - expire transitions CANDIDATE -> EXPIRED
      - expire transitions APPROVED_FOR_MANUAL_TEST -> EXPIRED

  * submit_review unhappy paths:
      - invalid action raises
      - invalid actor_id_token shape raises
      - invalid actor_type raises
      - invalid reason_token raises
      - bad recommendation shape raises
      - transitions from REJECTED/EXPIRED raise
      - approve-manual-test on already APPROVED_FOR_MANUAL_TEST
        raises (cannot re-approve)

  * Envelope contract:
      - every required key present
      - operator_required always True
      - live_behavior_changed always False
      - envelope carries no raw notes / free-form text fields
      - actor_id_token shape stable; reason_token from REASON_TOKENS

  * Determinism:
      - review_id reproducible for same inputs
      - review_id changes when any field changes

  * Import safety:
      - PAS196 sources free of twilio / slack / supabase / openai
        / anthropic / dotenv / state machine
      - PAS196 sources free of load_dotenv / get_supabase

  * CLI:
      - happy-path approve-manual-test writes an envelope
      - --summary-only suppresses file write
      - unknown action exits 2
      - invalid actor token exits 2
      - invalid reason token exits 2

  * Readiness gate:
      - exit 0 / verdict=READY on clean main
      - JSON envelope valid

  * Carry-forward:
      - PAS193 / PAS194 / PAS195 tests still pass
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


from app.services.simulation.recommendation_review import (  # noqa: E402
    ACTOR_TYPES,
    ALLOWED_STATUSES,
    ALLOWED_TRANSITIONS,
    REASON_TOKENS,
    REVIEW_ACTIONS,
    REVIEW_ENVELOPE_REQUIRED_KEYS,
    STATUS_APPROVED_FOR_MANUAL_TEST,
    STATUS_CANDIDATE,
    STATUS_EXPIRED,
    STATUS_REJECTED,
    ReviewValidationError,
    is_allowed_transition,
    submit_review,
)


def _read(relpath: str) -> str:
    return (_REPO_ROOT / relpath).read_text(encoding="utf-8")


def _candidate(rec_id: str = "pas195-rec-deadbeefcafebabe") -> dict:
    return {
        "recommendation_id":   rec_id,
        "status":              STATUS_CANDIDATE,
        "phase":               "PAS195",
        "operator_required":   True,
        "recommended_strategy": "callback_first",
    }


# ──────────────────────────────────────────────────────────────────
# Status machine
# ──────────────────────────────────────────────────────────────────

def test_allowed_statuses_exact_set():
    assert set(ALLOWED_STATUSES) == {
        STATUS_CANDIDATE,
        STATUS_APPROVED_FOR_MANUAL_TEST,
        STATUS_REJECTED,
        STATUS_EXPIRED,
    }


def test_allowed_transitions_exact_set():
    assert set(ALLOWED_TRANSITIONS) == {
        (STATUS_CANDIDATE,                STATUS_APPROVED_FOR_MANUAL_TEST),
        (STATUS_CANDIDATE,                STATUS_REJECTED),
        (STATUS_CANDIDATE,                STATUS_EXPIRED),
        (STATUS_APPROVED_FOR_MANUAL_TEST, STATUS_EXPIRED),
    }


@pytest.mark.parametrize("pair", [
    (STATUS_CANDIDATE,                STATUS_APPROVED_FOR_MANUAL_TEST),
    (STATUS_CANDIDATE,                STATUS_REJECTED),
    (STATUS_CANDIDATE,                STATUS_EXPIRED),
    (STATUS_APPROVED_FOR_MANUAL_TEST, STATUS_EXPIRED),
])
def test_is_allowed_transition_true_for_allowed(pair):
    assert is_allowed_transition(*pair) is True


@pytest.mark.parametrize("pair", [
    (STATUS_REJECTED,                 STATUS_APPROVED_FOR_MANUAL_TEST),
    (STATUS_REJECTED,                 STATUS_EXPIRED),
    (STATUS_REJECTED,                 STATUS_CANDIDATE),
    (STATUS_EXPIRED,                  STATUS_CANDIDATE),
    (STATUS_EXPIRED,                  STATUS_REJECTED),
    (STATUS_APPROVED_FOR_MANUAL_TEST, STATUS_REJECTED),
    (STATUS_APPROVED_FOR_MANUAL_TEST, STATUS_CANDIDATE),
    (STATUS_CANDIDATE,                STATUS_CANDIDATE),
])
def test_is_allowed_transition_false_for_forbidden(pair):
    assert is_allowed_transition(*pair) is False


# ──────────────────────────────────────────────────────────────────
# Forbidden status literals + identifiers absent
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

_PAS196_FILES = (
    "app/services/simulation/recommendation_review.py",
    "scripts/pas196_review_simulation_recommendation.py",
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


@pytest.mark.parametrize("relpath", _PAS196_FILES)
def test_forbidden_status_literals_absent_from_source(relpath):
    consts = _string_constants(_read(relpath))
    for tok in _FORBIDDEN_STATUS_LITERALS:
        assert tok not in consts, (
            f"{relpath} carries forbidden status literal {tok!r}"
        )


@pytest.mark.parametrize("relpath", _PAS196_FILES)
def test_forbidden_identifiers_absent_from_source(relpath):
    names = _identifier_names(_read(relpath))
    for tok in _FORBIDDEN_IDENTIFIERS:
        assert tok not in names, (
            f"{relpath} carries forbidden identifier {tok!r}"
        )


# ──────────────────────────────────────────────────────────────────
# submit_review — happy paths
# ──────────────────────────────────────────────────────────────────

def test_approve_manual_test_transitions_candidate_to_approved_for_manual_test():
    env = submit_review(
        _candidate(),
        "approve-manual-test",
        actor_id_token="op_abcd1234",
        reason_token="operator_approved_for_manual_test",
        reviewed_at="2026-05-21T00:00:00Z",
    )
    assert env["previous_status"] == STATUS_CANDIDATE
    assert env["new_status"]      == STATUS_APPROVED_FOR_MANUAL_TEST


def test_reject_transitions_candidate_to_rejected():
    env = submit_review(
        _candidate(),
        "reject",
        actor_id_token="op_abcd1234",
        reason_token="operator_rejected_unsafe",
        reviewed_at="2026-05-21T00:00:00Z",
    )
    assert env["new_status"] == STATUS_REJECTED


def test_expire_transitions_candidate_to_expired():
    env = submit_review(
        _candidate(),
        "expire",
        actor_id_token="auto_expiry",
        actor_type="automated_expiry",
        reason_token="candidate_expired_age",
        reviewed_at="2026-05-21T00:00:00Z",
    )
    assert env["new_status"] == STATUS_EXPIRED


def test_expire_transitions_approved_for_manual_test_to_expired():
    rec = _candidate()
    rec["status"] = STATUS_APPROVED_FOR_MANUAL_TEST
    env = submit_review(
        rec,
        "expire",
        actor_id_token="op_zzzz0001",
        reason_token="manual_test_complete_expiring",
        reviewed_at="2026-05-21T00:00:00Z",
    )
    assert env["previous_status"] == STATUS_APPROVED_FOR_MANUAL_TEST
    assert env["new_status"]      == STATUS_EXPIRED


# ──────────────────────────────────────────────────────────────────
# submit_review — unhappy paths
# ──────────────────────────────────────────────────────────────────

def test_invalid_action_raises():
    with pytest.raises(ReviewValidationError):
        submit_review(
            _candidate(),
            "deploy",
            actor_id_token="op_abcd1234",
            reason_token="operator_approved_for_manual_test",
            reviewed_at="2026-05-21T00:00:00Z",
        )


def test_invalid_actor_id_token_raises():
    with pytest.raises(ReviewValidationError):
        submit_review(
            _candidate(),
            "reject",
            actor_id_token="U01234567",  # Slack-shaped, not allowed
            reason_token="operator_rejected_unsafe",
            reviewed_at="2026-05-21T00:00:00Z",
        )


def test_invalid_actor_type_raises():
    with pytest.raises(ReviewValidationError):
        submit_review(
            _candidate(),
            "reject",
            actor_id_token="op_abcd1234",
            reason_token="operator_rejected_unsafe",
            reviewed_at="2026-05-21T00:00:00Z",
            actor_type="not_an_actor_type",
        )


def test_invalid_reason_token_raises():
    with pytest.raises(ReviewValidationError):
        submit_review(
            _candidate(),
            "reject",
            actor_id_token="op_abcd1234",
            reason_token="i_typed_a_free_form_note",
            reviewed_at="2026-05-21T00:00:00Z",
        )


def test_missing_recommendation_id_raises():
    bad = {"status": STATUS_CANDIDATE}
    with pytest.raises(ReviewValidationError):
        submit_review(
            bad,
            "reject",
            actor_id_token="op_abcd1234",
            reason_token="operator_rejected_unsafe",
            reviewed_at="2026-05-21T00:00:00Z",
        )


def test_off_catalogue_recommendation_status_raises():
    bad = {"recommendation_id": "x", "status": "APPROVED"}
    with pytest.raises(ReviewValidationError):
        submit_review(
            bad,
            "reject",
            actor_id_token="op_abcd1234",
            reason_token="operator_rejected_unsafe",
            reviewed_at="2026-05-21T00:00:00Z",
        )


def test_cannot_approve_already_approved_for_manual_test():
    rec = _candidate()
    rec["status"] = STATUS_APPROVED_FOR_MANUAL_TEST
    with pytest.raises(ReviewValidationError):
        submit_review(
            rec,
            "approve-manual-test",
            actor_id_token="op_abcd1234",
            reason_token="operator_approved_for_manual_test",
            reviewed_at="2026-05-21T00:00:00Z",
        )


def test_cannot_reject_from_rejected_or_expired():
    for terminal in (STATUS_REJECTED, STATUS_EXPIRED):
        rec = _candidate()
        rec["status"] = terminal
        with pytest.raises(ReviewValidationError):
            submit_review(
                rec,
                "reject",
                actor_id_token="op_abcd1234",
                reason_token="operator_rejected_unsafe",
                reviewed_at="2026-05-21T00:00:00Z",
            )


def test_blank_reviewed_at_raises():
    with pytest.raises(ReviewValidationError):
        submit_review(
            _candidate(),
            "reject",
            actor_id_token="op_abcd1234",
            reason_token="operator_rejected_unsafe",
            reviewed_at="",
        )


# ──────────────────────────────────────────────────────────────────
# Envelope contract
# ──────────────────────────────────────────────────────────────────

def test_envelope_carries_every_required_key():
    env = submit_review(
        _candidate(),
        "reject",
        actor_id_token="op_abcd1234",
        reason_token="operator_rejected_unsafe",
        reviewed_at="2026-05-21T00:00:00Z",
    )
    for k in REVIEW_ENVELOPE_REQUIRED_KEYS:
        assert k in env, f"missing {k}"


def test_envelope_operator_required_always_true():
    env = submit_review(
        _candidate(),
        "approve-manual-test",
        actor_id_token="op_abcd1234",
        reason_token="operator_approved_for_manual_test",
        reviewed_at="2026-05-21T00:00:00Z",
    )
    assert env["operator_required"] is True


def test_envelope_live_behavior_changed_always_false():
    for action, reason in (
        ("approve-manual-test", "operator_approved_for_manual_test"),
        ("reject",              "operator_rejected_unsafe"),
        ("expire",              "candidate_expired_age"),
    ):
        env = submit_review(
            _candidate(),
            action,
            actor_id_token=("auto_expiry" if action == "expire" else "op_abcd1234"),
            actor_type=("automated_expiry" if action == "expire" else "operator"),
            reason_token=reason,
            reviewed_at="2026-05-21T00:00:00Z",
        )
        assert env["live_behavior_changed"] is False


def test_envelope_carries_no_freeform_text_fields():
    env = submit_review(
        _candidate(),
        "reject",
        actor_id_token="op_abcd1234",
        reason_token="operator_rejected_unsafe",
        reviewed_at="2026-05-21T00:00:00Z",
    )
    for forbidden in ("notes", "note", "free_text", "comment", "operator_notes"):
        assert forbidden not in env, (
            f"envelope carries forbidden freeform field {forbidden!r}"
        )


def test_envelope_actor_id_token_shape():
    env = submit_review(
        _candidate(),
        "reject",
        actor_id_token="op_abcd1234",
        reason_token="operator_rejected_unsafe",
        reviewed_at="2026-05-21T00:00:00Z",
    )
    assert re.match(r"^op_[a-z0-9]{4,32}$", env["actor_id_token"])


def test_envelope_review_id_carries_pas196_prefix():
    env = submit_review(
        _candidate(),
        "reject",
        actor_id_token="op_abcd1234",
        reason_token="operator_rejected_unsafe",
        reviewed_at="2026-05-21T00:00:00Z",
    )
    assert env["review_id"].startswith("pas196-rev-")


# ──────────────────────────────────────────────────────────────────
# Determinism
# ──────────────────────────────────────────────────────────────────

def test_review_id_deterministic_for_same_inputs():
    a = submit_review(
        _candidate(),
        "reject",
        actor_id_token="op_abcd1234",
        reason_token="operator_rejected_unsafe",
        reviewed_at="2026-05-21T00:00:00Z",
    )
    b = submit_review(
        _candidate(),
        "reject",
        actor_id_token="op_abcd1234",
        reason_token="operator_rejected_unsafe",
        reviewed_at="2026-05-21T00:00:00Z",
    )
    assert a == b


def test_review_id_changes_with_any_input_change():
    base = submit_review(
        _candidate(),
        "reject",
        actor_id_token="op_abcd1234",
        reason_token="operator_rejected_unsafe",
        reviewed_at="2026-05-21T00:00:00Z",
    )
    variants = (
        submit_review(_candidate("pas195-rec-other-recommendation"),
                      "reject",
                      actor_id_token="op_abcd1234",
                      reason_token="operator_rejected_unsafe",
                      reviewed_at="2026-05-21T00:00:00Z"),
        submit_review(_candidate(),
                      "reject",
                      actor_id_token="op_efef5678",
                      reason_token="operator_rejected_unsafe",
                      reviewed_at="2026-05-21T00:00:00Z"),
        submit_review(_candidate(),
                      "reject",
                      actor_id_token="op_abcd1234",
                      reason_token="operator_rejected_low_confidence",
                      reviewed_at="2026-05-21T00:00:00Z"),
        submit_review(_candidate(),
                      "reject",
                      actor_id_token="op_abcd1234",
                      reason_token="operator_rejected_unsafe",
                      reviewed_at="2026-05-21T11:11:11Z"),
    )
    for v in variants:
        assert v["review_id"] != base["review_id"]


# ──────────────────────────────────────────────────────────────────
# Import safety
# ──────────────────────────────────────────────────────────────────

_BANNED_IMPORT_HEADS = ("twilio", "slack_sdk", "openai", "anthropic",
                        "dotenv", "supabase")
_BANNED_IMPORT_PREFIXES = (
    "app.services.slack",
    "app.routes.slack_command",
    "app.engine.state_machine",
    "app.engine",
)
_BANNED_CALLS = ("load_dotenv", "get_supabase")


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


@pytest.mark.parametrize("relpath", (
    "app/services/simulation/recommendation_review.py",
    "scripts/pas196_review_simulation_recommendation.py",
    "scripts/pas196_simulation_recommendation_review_readiness_check.py",
))
def test_no_banned_imports_in_pas196_file(relpath):
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

_RUNNER = _REPO_ROOT / "scripts" / "pas196_review_simulation_recommendation.py"


def _write_recommendation(tmp: pathlib.Path) -> pathlib.Path:
    path = tmp / "candidate.json"
    path.write_text(json.dumps(_candidate()), encoding="utf-8")
    return path


def _run_cli(*argv):
    return subprocess.run(
        [sys.executable, str(_RUNNER), *argv],
        cwd=str(_REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=180,
    )


def test_runner_approve_manual_test_writes_envelope():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        rec = _write_recommendation(tp)
        proc = _run_cli(
            "--recommendation", str(rec),
            "--action", "approve-manual-test",
            "--actor-id-token", "op_abcd1234",
            "--reason-token", "operator_approved_for_manual_test",
            "--output-dir", str(tp),
        )
        assert proc.returncode == 0, proc.stdout + proc.stderr
        files = list(tp.glob("pas196_recommendation_review_*.json"))
        assert len(files) == 1
        payload = json.loads(files[0].read_text(encoding="utf-8"))
        assert payload["new_status"] == STATUS_APPROVED_FOR_MANUAL_TEST
        assert payload["operator_required"] is True
        assert payload["live_behavior_changed"] is False


def test_runner_summary_only_does_not_write_file():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        rec = _write_recommendation(tp)
        proc = _run_cli(
            "--recommendation", str(rec),
            "--action", "reject",
            "--actor-id-token", "op_abcd1234",
            "--reason-token", "operator_rejected_unsafe",
            "--output-dir", str(tp),
            "--summary-only",
        )
        assert proc.returncode == 0, proc.stdout + proc.stderr
        files = list(tp.glob("pas196_recommendation_review_*.json"))
        assert files == []


def test_runner_rejects_unknown_action():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        rec = _write_recommendation(tp)
        proc = _run_cli(
            "--recommendation", str(rec),
            "--action", "deploy",
            "--actor-id-token", "op_abcd1234",
            "--reason-token", "operator_rejected_unsafe",
            "--output-dir", str(tp),
            "--summary-only",
        )
        assert proc.returncode == 2, proc.stdout + proc.stderr


def test_runner_rejects_bad_actor_token():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        rec = _write_recommendation(tp)
        proc = _run_cli(
            "--recommendation", str(rec),
            "--action", "reject",
            "--actor-id-token", "U01234567",
            "--reason-token", "operator_rejected_unsafe",
            "--output-dir", str(tp),
            "--summary-only",
        )
        assert proc.returncode == 2, proc.stdout + proc.stderr


def test_runner_rejects_off_catalogue_reason_token():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        rec = _write_recommendation(tp)
        proc = _run_cli(
            "--recommendation", str(rec),
            "--action", "reject",
            "--actor-id-token", "op_abcd1234",
            "--reason-token", "i_typed_a_free_form_note",
            "--output-dir", str(tp),
            "--summary-only",
        )
        assert proc.returncode == 2, proc.stdout + proc.stderr


# ──────────────────────────────────────────────────────────────────
# Readiness gate
# ──────────────────────────────────────────────────────────────────

_GATE = _REPO_ROOT / "scripts" / "pas196_simulation_recommendation_review_readiness_check.py"


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
    assert payload["phase"] == "PAS196"
    assert payload["verdict"] == "READY"
    assert payload["ready"] is True
    assert payload["fail_count"] == 0
    assert payload["check_count"] > 0


# ──────────────────────────────────────────────────────────────────
# Carry-forward
# ──────────────────────────────────────────────────────────────────

def test_pas193_to_pas195_tests_still_pass():
    proc = subprocess.run(
        [
            sys.executable, "-m", "pytest",
            "tests/mvp/test_pas193_simulation_layer.py",
            "tests/mvp/test_pas194_strategy_comparison.py",
            "tests/mvp/test_pas195_simulation_recommendations.py",
            "-q",
        ],
        cwd=str(_REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=360,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr


# ──────────────────────────────────────────────────────────────────
# Doc invariants
# ──────────────────────────────────────────────────────────────────

def test_doc_present_and_carries_required_clauses():
    doc = _read("docs/pas196_simulation_recommendation_review.md").lower()
    for clause in (
        "what pas196 proves",
        "what pas196 does not prove",
        "claimable",
        "still not claimable",
        "future pas197",
        "review",
        "operator",
        "safety",
        "transition",
    ):
        assert clause in doc, f"doc missing clause {clause!r}"
