"""
PAS198 — Bounded manual-test runtime.

Pure function. Consumes a PAS197 manual-test package and executes
the package's recommended strategy against the closed PAS193
scenario catalogue, producing a transcript bundle, runtime
evaluation, capability summary, safety outcome, and an execution
artefact.

The runtime is SIMULATION_ONLY by construction. It refuses any
package whose status is not READY_FOR_MANUAL_TEST, whose
allowed_environment is not SIMULATION_ONLY, or whose
live_behavior_changed is not False. It never imports Twilio,
Slack, Supabase, OpenAI, Anthropic, dotenv, or the live state
machine. It never opens a network connection, never reads .env,
never mutates anything. The CLI is the only writer; it writes
exclusively under reports/simulations/.

Contract for a valid input package:

  * package["status"]                == "READY_FOR_MANUAL_TEST"
  * package["allowed_environment"]   == "SIMULATION_ONLY"
  * package["live_behavior_changed"] is False
  * package["package_id"]            is a non-empty string
  * package["strategy_id"]           is a non-empty string drawn
                                       from STRATEGY_IDS

Any contract violation raises ManualTestRuntimeValidationError.

Output runtime artefact (closed schema):

  * runtime_id              — deterministic SHA-256-derived hash
  * phase                   — "PAS198"
  * package_id              — copied from the package
  * executed_strategy       — copied from package.strategy_id
  * executed_scenarios      — closed list of scenario_ids that
                              actually ran (may be shorter than
                              the catalogue if execution halted
                              on safety / empty transcript)
  * transcript_bundle       — one entry per executed scenario
  * runtime_score           — aggregate + per-scenario evaluation
  * capability_summary      — aggregate capability rates
  * safety_outcome          — {outcome, auto_fail_count,
                                auto_fail_reasons}
  * execution_status        — completed | halted_on_safety |
                               halted_on_empty_transcript
  * allowed_environment     — fixed to "SIMULATION_ONLY"
  * live_behavior_changed   — fixed to False
  * status                  — "EXECUTED"
  * created_at              — caller-supplied ISO timestamp
"""

from __future__ import annotations

import hashlib
from typing import Dict, List, Optional, Sequence, Tuple

from app.services.simulation.adapter import _ACTION_CAPABILITIES
from app.services.simulation.comparison import run_scenario_under_strategy
from app.services.simulation.scenarios import SCENARIOS
from app.services.simulation.scoring import score_conversation
from app.services.simulation.strategies import STRATEGY_IDS


# ──────────────────────────────────────────────────────────────────
# Closed vocabularies
# ──────────────────────────────────────────────────────────────────

STATUS_EXECUTED: str = "EXECUTED"

RUNTIME_ENVIRONMENT_SIMULATION_ONLY: str = "SIMULATION_ONLY"

REQUIRED_PACKAGE_STATUS:              str = "READY_FOR_MANUAL_TEST"
REQUIRED_PACKAGE_ALLOWED_ENVIRONMENT: str = "SIMULATION_ONLY"


EXECUTION_STATUS_COMPLETED:                  str = "completed"
EXECUTION_STATUS_HALTED_ON_SAFETY:           str = "halted_on_safety"
EXECUTION_STATUS_HALTED_ON_EMPTY_TRANSCRIPT: str = "halted_on_empty_transcript"

EXECUTION_STATUSES: Tuple[str, ...] = (
    EXECUTION_STATUS_COMPLETED,
    EXECUTION_STATUS_HALTED_ON_SAFETY,
    EXECUTION_STATUS_HALTED_ON_EMPTY_TRANSCRIPT,
)


SAFETY_OUTCOME_CLEAN:     str = "clean"
SAFETY_OUTCOME_AUTO_FAIL: str = "auto_fail"

SAFETY_OUTCOMES: Tuple[str, ...] = (
    SAFETY_OUTCOME_CLEAN,
    SAFETY_OUTCOME_AUTO_FAIL,
)


ACTOR_AGENT: str = "agent"
ACTOR_LEAD:  str = "lead"

ACTORS: Tuple[str, ...] = (ACTOR_AGENT, ACTOR_LEAD)


CAPABILITY_MARKERS: Tuple[str, ...] = (
    "qualification_captured",
    "appointment_attempted",
    "callback_captured",
    "objection_handled",
    "conversation_completed",
)


SAFETY_MARKERS: Tuple[str, ...] = (
    "unsafe_claim",
    "pii_leak",
    "hallucinated_policy",
    "agent_poaching",
    "qualification_pressure",
    "language_misclaim",
    "pii_pattern_in_utterance",
    "supported_false_no_safe_handoff",
    "empty_transcript",
)


RUNTIME_REQUIRED_KEYS: Tuple[str, ...] = (
    "runtime_id",
    "phase",
    "package_id",
    "executed_strategy",
    "executed_scenarios",
    "transcript_bundle",
    "runtime_score",
    "capability_summary",
    "safety_outcome",
    "execution_status",
    "allowed_environment",
    "live_behavior_changed",
    "status",
    "created_at",
)


PER_SCENARIO_EVALUATION_KEYS: Tuple[str, ...] = (
    "scenario_id",
    "scenario_type",
    "supported",
    "score",
    "passed",
    "qualification_captured",
    "objection_handled",
    "callback_captured",
    "booking_attempted",
    "unsafe_output_detected",
    "hallucinated_policy_detected",
    "pii_leak_detected",
    "transcript_integrity_valid",
    "failure_reasons",
)


TRANSCRIPT_ENTRY_REQUIRED_KEYS: Tuple[str, ...] = (
    "scenario_id",
    "scenario_type",
    "supported",
    "turns",
    "capability_markers",
    "safety_markers",
)


TURN_REQUIRED_KEYS: Tuple[str, ...] = (
    "sequence_id",
    "actor",
    "agent_action",
    "text",
    "capability_markers",
    "safety_markers",
)


# Closed bounded synthetic scenario catalogue (the PAS193 surface).
# Frozen at module import. The runtime never grows or shrinks it.
_RUNTIME_SCENARIOS: Tuple[Dict, ...] = SCENARIOS


# ──────────────────────────────────────────────────────────────────
# Validation
# ──────────────────────────────────────────────────────────────────

class ManualTestRuntimeValidationError(ValueError):
    """Raised when a PAS197 package violates the PAS198 contract."""


def _require_keys(payload: Dict, keys: Tuple[str, ...], label: str) -> None:
    for k in keys:
        if k not in payload:
            raise ManualTestRuntimeValidationError(
                f"{label} missing required key {k!r}"
            )


def _validate_package(package: Dict) -> None:
    if not isinstance(package, dict):
        raise ManualTestRuntimeValidationError(
            "package must be a dict"
        )
    _require_keys(
        package,
        ("package_id", "status", "allowed_environment",
         "live_behavior_changed", "strategy_id"),
        label="package",
    )
    if package["status"] != REQUIRED_PACKAGE_STATUS:
        raise ManualTestRuntimeValidationError(
            f"package.status must be {REQUIRED_PACKAGE_STATUS!r}; "
            f"got {package['status']!r}"
        )
    if package["allowed_environment"] != REQUIRED_PACKAGE_ALLOWED_ENVIRONMENT:
        raise ManualTestRuntimeValidationError(
            f"package.allowed_environment must be "
            f"{REQUIRED_PACKAGE_ALLOWED_ENVIRONMENT!r}; "
            f"got {package['allowed_environment']!r}"
        )
    if package["live_behavior_changed"] is not False:
        raise ManualTestRuntimeValidationError(
            "package.live_behavior_changed must be False"
        )
    pkg_id = package["package_id"]
    if not isinstance(pkg_id, str) or not pkg_id:
        raise ManualTestRuntimeValidationError(
            "package.package_id must be a non-empty string"
        )
    sid = package["strategy_id"]
    if not isinstance(sid, str) or not sid:
        raise ManualTestRuntimeValidationError(
            "package.strategy_id must be a non-empty string"
        )
    if sid not in STRATEGY_IDS:
        raise ManualTestRuntimeValidationError(
            f"package.strategy_id {sid!r} not in known STRATEGY_IDS"
        )


# ──────────────────────────────────────────────────────────────────
# Internal helpers
# ──────────────────────────────────────────────────────────────────

def _runtime_id(
    package_id: str,
    strategy_id: str,
    scenario_ids: Sequence[str],
) -> str:
    h = hashlib.sha256()
    h.update(package_id.encode("utf-8"))
    h.update(b"||")
    h.update(strategy_id.encode("utf-8"))
    h.update(b"||")
    h.update(("|".join(scenario_ids)).encode("utf-8"))
    return "pas198-rt-" + h.hexdigest()[:16]


def _build_scenario_transcript(conversation: Dict) -> List[Dict]:
    """
    Re-shape the (agent_text, lead_text) pairs from
    run_scenario_under_strategy into per-actor turns with
    deterministic sequence_ids and explicit actor labels.
    """
    out: List[Dict] = []
    seq = 0
    for turn in conversation.get("turns", []):
        seq += 1
        agent_action = turn["agent_action"]
        agent_caps = list(_ACTION_CAPABILITIES.get(agent_action, ()))
        out.append({
            "sequence_id":        seq,
            "actor":              ACTOR_AGENT,
            "agent_action":       agent_action,
            "text":               turn["agent_text"],
            "capability_markers": agent_caps,
            "safety_markers":     [],
        })
        lead_text = turn.get("lead_text") or ""
        if lead_text:
            seq += 1
            out.append({
                "sequence_id":        seq,
                "actor":              ACTOR_LEAD,
                "agent_action":       None,
                "text":               lead_text,
                "capability_markers": [],
                "safety_markers":     [],
            })
    return out


def _conversation_safety_markers(
    conversation: Dict, score_result: Dict,
) -> List[str]:
    found: List[str] = []
    safety = conversation.get("safety") or {}
    for flag in SAFETY_MARKERS:
        if bool(safety.get(flag)):
            found.append(flag)
    for reason in score_result.get("failure_reasons") or ():
        if reason in SAFETY_MARKERS and reason not in found:
            found.append(reason)
    return sorted(set(found))


def _transcript_integrity_valid(
    transcript: List[Dict], score_result: Dict,
) -> bool:
    if not transcript:
        return False
    for idx, t in enumerate(transcript):
        if t.get("sequence_id") != idx + 1:
            return False
        if t.get("actor") not in ACTORS:
            return False
        for k in TURN_REQUIRED_KEYS:
            if k not in t:
                return False
        for m in t.get("capability_markers") or ():
            if m not in CAPABILITY_MARKERS:
                return False
        for m in t.get("safety_markers") or ():
            if m not in SAFETY_MARKERS:
                return False
        if t["actor"] == ACTOR_AGENT and not t.get("text"):
            return False
    if "pii_pattern_in_utterance" in (score_result.get("failure_reasons") or ()):
        return False
    return True


def _rate(numerator: int, denominator: int) -> float:
    if denominator <= 0:
        return 0.0
    return round(numerator / denominator, 4)


def _avg(values: Sequence[float]) -> float:
    if not values:
        return 0.0
    return round(sum(values) / len(values), 2)


def _per_scenario_evaluation(
    scenario: Dict,
    conversation: Dict,
    transcript: List[Dict],
    score_result: Dict,
) -> Dict:
    caps = set(score_result.get("capabilities_observed") or ())
    reasons = list(score_result.get("failure_reasons") or ())
    safety = conversation.get("safety") or {}
    return {
        "scenario_id":               scenario["scenario_id"],
        "scenario_type":             scenario["scenario_type"],
        "supported":                 bool(scenario["supported"]),
        "score":                     int(score_result.get("score", 0)),
        "passed":                    bool(score_result.get("passed", False)),
        "qualification_captured":    "qualification_captured" in caps,
        "objection_handled":         "objection_handled"      in caps,
        "callback_captured":         "callback_captured"      in caps,
        "booking_attempted":         "appointment_attempted"  in caps,
        "unsafe_output_detected":    (
            bool(safety.get("unsafe_claim"))
            or "unsafe_claim" in reasons
        ),
        "hallucinated_policy_detected": (
            bool(safety.get("hallucinated_policy"))
            or "hallucinated_policy" in reasons
        ),
        "pii_leak_detected": (
            bool(safety.get("pii_leak"))
            or "pii_leak" in reasons
            or "pii_pattern_in_utterance" in reasons
        ),
        "transcript_integrity_valid": _transcript_integrity_valid(
            transcript, score_result,
        ),
        "failure_reasons":           reasons,
    }


def _capability_summary(per_scenario_rows: Sequence[Dict]) -> Dict:
    total = len(per_scenario_rows)
    qc = sum(1 for r in per_scenario_rows if r["qualification_captured"])
    oh = sum(1 for r in per_scenario_rows if r["objection_handled"])
    cb = sum(1 for r in per_scenario_rows if r["callback_captured"])
    ba = sum(1 for r in per_scenario_rows if r["booking_attempted"])
    return {
        "scenarios":                   total,
        "qualification_captured_rate": _rate(qc, total),
        "objection_handled_rate":      _rate(oh, total),
        "callback_captured_rate":      _rate(cb, total),
        "booking_attempted_rate":      _rate(ba, total),
    }


def _runtime_score(per_scenario_rows: Sequence[Dict]) -> Dict:
    total = len(per_scenario_rows)
    passed = sum(1 for r in per_scenario_rows if r["passed"])
    scores = [float(r["score"]) for r in per_scenario_rows]
    return {
        "scenarios":     total,
        "passed":        passed,
        "pass_rate":     _rate(passed, total),
        "average_score": _avg(scores),
        "per_scenario":  list(per_scenario_rows),
    }


def _safety_outcome(per_scenario_rows: Sequence[Dict]) -> Dict:
    auto_fail_reasons: List[str] = []
    auto_fail_count = 0
    for r in per_scenario_rows:
        flagged = (
            r["unsafe_output_detected"]
            or r["hallucinated_policy_detected"]
            or r["pii_leak_detected"]
        )
        for reason in r["failure_reasons"]:
            if reason in SAFETY_MARKERS and reason != "supported_false_no_safe_handoff":
                if reason not in auto_fail_reasons:
                    auto_fail_reasons.append(reason)
                flagged = True
        if flagged:
            auto_fail_count += 1
    outcome = (
        SAFETY_OUTCOME_AUTO_FAIL if auto_fail_count > 0
        else SAFETY_OUTCOME_CLEAN
    )
    return {
        "outcome":           outcome,
        "auto_fail_count":   auto_fail_count,
        "auto_fail_reasons": sorted(set(auto_fail_reasons)),
    }


# ──────────────────────────────────────────────────────────────────
# Public API
# ──────────────────────────────────────────────────────────────────

def execute_manual_test_runtime(
    package: Dict,
    *,
    created_at: str,
    scenarios: Optional[Sequence[Dict]] = None,
) -> Dict:
    """
    Validate a PAS197 package and execute its recommended strategy
    against the closed PAS193 scenario catalogue. Pure function.
    Same inputs produce the same runtime artefact, including the
    same runtime_id, every call.

    The runtime's `allowed_environment` is fixed at SIMULATION_ONLY
    and `live_behavior_changed` is fixed at False by construction —
    neither can be set by the caller.

    The optional `scenarios` argument allows callers to pin to a
    specific subset of the catalogue (for tests). If omitted, the
    full closed catalogue is used. Scenarios passed by the caller
    must already exist in the closed catalogue; the runtime does
    not introduce new synthetic surfaces.
    """
    if not isinstance(created_at, str) or not created_at:
        raise ManualTestRuntimeValidationError(
            "created_at must be a non-empty ISO timestamp string"
        )
    _validate_package(package)

    if scenarios is None:
        run_scenarios: Tuple[Dict, ...] = _RUNTIME_SCENARIOS
    else:
        known_ids = {s["scenario_id"] for s in _RUNTIME_SCENARIOS}
        for s in scenarios:
            sid = s.get("scenario_id")
            if sid not in known_ids:
                raise ManualTestRuntimeValidationError(
                    f"scenario {sid!r} not in the closed PAS193 catalogue"
                )
        run_scenarios = tuple(scenarios)

    strategy_id = str(package["strategy_id"])
    package_id  = str(package["package_id"])

    transcript_bundle: List[Dict] = []
    per_scenario_rows: List[Dict] = []
    executed_scenario_ids: List[str] = []
    execution_status: str = EXECUTION_STATUS_COMPLETED

    for scenario in run_scenarios:
        conversation = run_scenario_under_strategy(strategy_id, scenario)
        transcript = _build_scenario_transcript(conversation)
        score_result = score_conversation(conversation, scenario)

        if not transcript:
            execution_status = EXECUTION_STATUS_HALTED_ON_EMPTY_TRANSCRIPT
            transcript_bundle.append({
                "scenario_id":        scenario["scenario_id"],
                "scenario_type":      scenario["scenario_type"],
                "supported":          bool(scenario["supported"]),
                "turns":              [],
                "capability_markers": [],
                "safety_markers":     ["empty_transcript"],
            })
            per_scenario_rows.append(_per_scenario_evaluation(
                scenario, conversation, transcript, score_result,
            ))
            executed_scenario_ids.append(scenario["scenario_id"])
            break

        bundle_caps = list(score_result.get("capabilities_observed") or ())
        bundle_safety_markers = _conversation_safety_markers(
            conversation, score_result,
        )

        transcript_bundle.append({
            "scenario_id":        scenario["scenario_id"],
            "scenario_type":      scenario["scenario_type"],
            "supported":          bool(scenario["supported"]),
            "turns":              transcript,
            "capability_markers": bundle_caps,
            "safety_markers":     bundle_safety_markers,
        })
        per_scenario_rows.append(_per_scenario_evaluation(
            scenario, conversation, transcript, score_result,
        ))
        executed_scenario_ids.append(scenario["scenario_id"])

        # Safety auto-fail halts execution (PAS193 doctrine).
        if score_result.get("recommendation_label") == "block_unsafe":
            execution_status = EXECUTION_STATUS_HALTED_ON_SAFETY
            break

    runtime_score    = _runtime_score(per_scenario_rows)
    capability_sum   = _capability_summary(per_scenario_rows)
    safety_outcome   = _safety_outcome(per_scenario_rows)

    return {
        "runtime_id":             _runtime_id(
            package_id, strategy_id, executed_scenario_ids,
        ),
        "phase":                  "PAS198",
        "package_id":             package_id,
        "executed_strategy":      strategy_id,
        "executed_scenarios":     executed_scenario_ids,
        "transcript_bundle":      transcript_bundle,
        "runtime_score":          runtime_score,
        "capability_summary":     capability_sum,
        "safety_outcome":         safety_outcome,
        "execution_status":       execution_status,
        "allowed_environment":    RUNTIME_ENVIRONMENT_SIMULATION_ONLY,
        "live_behavior_changed":  False,
        "status":                 STATUS_EXECUTED,
        "created_at":             created_at,
    }
