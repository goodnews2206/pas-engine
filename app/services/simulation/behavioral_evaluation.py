"""
PAS200 — Deterministic behavioral runtime evaluation.

Pure function. Consumes a PAS198 runtime artefact (and, optionally,
a PAS199 inspection artefact for cross-reference) and produces a
structured behavioural-quality assessment of HOW the synthetic
conversation behaved — not just whether it passed.

The evaluation is strictly read-only and SIMULATION_ONLY. It never
imports Twilio, Slack, Supabase, OpenAI, Anthropic, dotenv, or the
live state machine. It never reads .env, never opens a network
connection, never mutates anything. The CLI is the only writer; it
writes exclusively under reports/simulations/.

Scoring is deterministic and structural. All scores derive from
sequence structure, turn ordering, agent-action vocabulary,
acknowledgement patterns, and the closed-vocabulary safety markers
PAS198 already recorded. No LLM, no embeddings, no learning, no
probability.

Contract for a valid input runtime:

  * runtime["status"]                == "EXECUTED"
  * runtime["allowed_environment"]   == "SIMULATION_ONLY"
  * runtime["live_behavior_changed"] is False
  * runtime["runtime_id"]            is a non-empty string
  * runtime["transcript_bundle"]     is a non-empty list

Optional inspection contract:

  * inspection["runtime_id"]            == runtime["runtime_id"]
  * inspection["allowed_environment"]   == "SIMULATION_ONLY"
  * inspection["live_behavior_changed"] is False

Any contract violation raises BehavioralEvaluationValidationError.

Output behavioural-evaluation artefact (closed schema):

  * behavioral_evaluation_id    — deterministic SHA-256 hash
  * phase                       — "PAS200"
  * generated_at                — caller-supplied ISO timestamp
  * allowed_environment         — fixed to "SIMULATION_ONLY"
  * live_behavior_changed       — fixed to False
  * runtime_id                  — copied from runtime
  * inspection_id               — copied from inspection or None
  * transcript_hash             — SHA-256 of bounded transcript
                                   projection (turns only)
  * aggregate_scores            — {pressure, pacing, continuity,
                                    trust, friction} floats 0..1
  * scenario_summaries          — per-scenario scores +
                                    annotation counts
  * turn_annotations            — closed-vocabulary turn-level
                                    annotations referencing
                                    scenario_id + sequence_id
  * behavioral_flags            — closed-vocabulary aggregate
                                    findings
  * artifact_integrity          — boolean integrity checks
"""

from __future__ import annotations

import hashlib
import json
from typing import Dict, List, Optional, Sequence, Tuple


# ──────────────────────────────────────────────────────────────────
# Closed vocabularies
# ──────────────────────────────────────────────────────────────────

BEHAVIORAL_EVALUATION_ENVIRONMENT_SIMULATION_ONLY: str = "SIMULATION_ONLY"

REQUIRED_RUNTIME_STATUS:      str = "EXECUTED"
REQUIRED_RUNTIME_ENVIRONMENT: str = "SIMULATION_ONLY"


SCORE_KEYS: Tuple[str, ...] = (
    "pressure_score",
    "pacing_score",
    "continuity_score",
    "trust_score",
    "friction_score",
)


TURN_ANNOTATIONS: Tuple[str, ...] = (
    "EARLY_ESCALATION",
    "STACKED_QUALIFICATION",
    "CONTEXT_RESET",
    "ACKNOWLEDGMENT_PRESENT",
    "CALLBACK_CONTINUITY",
    "HIGH_PRESSURE_SEQUENCE",
    "SOFT_DISCOVERY",
    "TRUST_PRESERVING_LANGUAGE",
    "HESITATION_AFTER_PUSH",
    "NATURAL_TRANSITION",
)


BEHAVIORAL_FLAGS: Tuple[str, ...] = (
    "high_pressure_strategy",
    "low_trust_strategy",
    "context_reset_repeated",
    "early_escalation_observed",
    "good_pacing_observed",
    "trust_preservation_observed",
    "natural_transitions_dominant",
    "low_friction_observed",
    "high_friction_observed",
    "stacked_qualification_observed",
    "callback_continuity_observed",
    "soft_discovery_observed",
    "trust_preserving_language_observed",
    "hesitation_after_push_observed",
    "acknowledgment_present_observed",
)


BEHAVIORAL_EVALUATION_REQUIRED_KEYS: Tuple[str, ...] = (
    "behavioral_evaluation_id",
    "phase",
    "generated_at",
    "allowed_environment",
    "live_behavior_changed",
    "runtime_id",
    "inspection_id",
    "transcript_hash",
    "aggregate_scores",
    "scenario_summaries",
    "turn_annotations",
    "behavioral_flags",
    "artifact_integrity",
)


SCENARIO_SUMMARY_KEYS: Tuple[str, ...] = (
    "scenario_id",
    "scenario_type",
    "supported",
    "pressure_score",
    "pacing_score",
    "continuity_score",
    "trust_score",
    "friction_score",
    "annotation_counts",
)


TURN_ANNOTATION_KEYS: Tuple[str, ...] = (
    "scenario_id",
    "sequence_id",
    "actor",
    "agent_action",
    "annotations",
)


ARTIFACT_INTEGRITY_KEYS: Tuple[str, ...] = (
    "runtime_status_executed",
    "runtime_allowed_environment_simulation_only",
    "runtime_live_behavior_changed_false",
    "runtime_transcript_bundle_non_empty",
    "scenarios_covered_match_runtime",
    "annotations_reference_known_sequence_ids",
    "scores_within_unit_interval",
    "annotations_drawn_from_closed_vocabulary",
    "flags_drawn_from_closed_vocabulary",
)


ACTOR_AGENT: str = "agent"
ACTOR_LEAD:  str = "lead"
ACTORS: Tuple[str, ...] = (ACTOR_AGENT, ACTOR_LEAD)


# Agent-action semantic groupings used by the scorers. These
# names are the PAS193 adapter vocabulary; PAS200 only reads
# them, never executes them.
_TRUST_PRESERVING_ACTIONS: Tuple[str, ...] = (
    "handle_objection",
    "polite_disengage",
    "respect_channel_preference",
    "decline_unsupported_language",
)


_DISCOVERY_ACTIONS: Tuple[str, ...] = (
    "ask_intent",
    "qualify",
)


_COMMITMENT_PRESSURE_ACTIONS: Tuple[str, ...] = (
    "offer_appointment",
)


_BOOKING_AND_CALLBACK_ACTIONS: Tuple[str, ...] = (
    "offer_appointment",
    "offer_callback",
)


# ──────────────────────────────────────────────────────────────────
# Validation
# ──────────────────────────────────────────────────────────────────

class BehavioralEvaluationValidationError(ValueError):
    """Raised when a runtime/inspection input violates the contract."""


def _require_keys(payload: Dict, keys: Tuple[str, ...], label: str) -> None:
    if not isinstance(payload, dict):
        raise BehavioralEvaluationValidationError(
            f"{label} must be a dict"
        )
    for k in keys:
        if k not in payload:
            raise BehavioralEvaluationValidationError(
                f"{label} missing required key {k!r}"
            )


def _require_non_empty_str(value, label: str) -> None:
    if not isinstance(value, str) or not value:
        raise BehavioralEvaluationValidationError(
            f"{label} must be a non-empty string"
        )


def _validate_runtime(runtime: Dict) -> None:
    _require_keys(
        runtime,
        ("runtime_id", "status", "allowed_environment",
         "live_behavior_changed", "transcript_bundle",
         "executed_scenarios"),
        label="runtime",
    )
    _require_non_empty_str(runtime["runtime_id"], "runtime.runtime_id")
    if runtime["status"] != REQUIRED_RUNTIME_STATUS:
        raise BehavioralEvaluationValidationError(
            f"runtime.status must be {REQUIRED_RUNTIME_STATUS!r}; "
            f"got {runtime['status']!r}"
        )
    if runtime["allowed_environment"] != REQUIRED_RUNTIME_ENVIRONMENT:
        raise BehavioralEvaluationValidationError(
            f"runtime.allowed_environment must be "
            f"{REQUIRED_RUNTIME_ENVIRONMENT!r}; "
            f"got {runtime['allowed_environment']!r}"
        )
    if runtime["live_behavior_changed"] is not False:
        raise BehavioralEvaluationValidationError(
            "runtime.live_behavior_changed must be False"
        )
    bundle = runtime["transcript_bundle"]
    if not isinstance(bundle, list) or not bundle:
        raise BehavioralEvaluationValidationError(
            "runtime.transcript_bundle must be a non-empty list"
        )
    for idx, entry in enumerate(bundle):
        if not isinstance(entry, dict):
            raise BehavioralEvaluationValidationError(
                f"runtime.transcript_bundle[{idx}] must be a dict"
            )
        for k in ("scenario_id", "turns"):
            if k not in entry:
                raise BehavioralEvaluationValidationError(
                    f"runtime.transcript_bundle[{idx}] missing key {k!r}"
                )
        turns = entry["turns"]
        if not isinstance(turns, list):
            raise BehavioralEvaluationValidationError(
                f"runtime.transcript_bundle[{idx}].turns must be a list"
            )
        for tidx, t in enumerate(turns):
            if not isinstance(t, dict):
                raise BehavioralEvaluationValidationError(
                    f"runtime.transcript_bundle[{idx}].turns[{tidx}] "
                    f"must be a dict"
                )
            for k in ("sequence_id", "actor"):
                if k not in t:
                    raise BehavioralEvaluationValidationError(
                        f"runtime.transcript_bundle[{idx}].turns[{tidx}] "
                        f"missing key {k!r}"
                    )
            if t["actor"] not in ACTORS:
                raise BehavioralEvaluationValidationError(
                    f"runtime.transcript_bundle[{idx}].turns[{tidx}] "
                    f"actor {t['actor']!r} not in {ACTORS}"
                )


def _validate_inspection(inspection: Dict, runtime: Dict) -> None:
    _require_keys(
        inspection,
        ("inspection_id", "allowed_environment",
         "live_behavior_changed", "lineage_summary"),
        label="inspection",
    )
    _require_non_empty_str(
        inspection["inspection_id"], "inspection.inspection_id",
    )
    if inspection["allowed_environment"] != REQUIRED_RUNTIME_ENVIRONMENT:
        raise BehavioralEvaluationValidationError(
            f"inspection.allowed_environment must be "
            f"{REQUIRED_RUNTIME_ENVIRONMENT!r}; "
            f"got {inspection['allowed_environment']!r}"
        )
    if inspection["live_behavior_changed"] is not False:
        raise BehavioralEvaluationValidationError(
            "inspection.live_behavior_changed must be False"
        )
    insp_rt_id = (inspection.get("lineage_summary") or {}).get("runtime_id")
    if insp_rt_id != runtime["runtime_id"]:
        raise BehavioralEvaluationValidationError(
            f"inspection.lineage_summary.runtime_id ({insp_rt_id!r}) "
            f"must match runtime.runtime_id ({runtime['runtime_id']!r})"
        )


# ──────────────────────────────────────────────────────────────────
# Hash helpers
# ──────────────────────────────────────────────────────────────────

def _transcript_hash(bundle: Sequence[Dict]) -> str:
    """
    Deterministic SHA-256 over the bounded transcript projection:
    per-turn (scenario_id, sequence_id, actor, agent_action,
    capability_markers, safety_markers). Text bodies are excluded
    so the hash is stable against whitespace/encoding noise.
    """
    projection: List[Dict] = []
    for entry in bundle:
        sid = entry.get("scenario_id")
        for t in entry.get("turns") or []:
            projection.append({
                "scenario_id":        sid,
                "sequence_id":        t.get("sequence_id"),
                "actor":              t.get("actor"),
                "agent_action":       t.get("agent_action"),
                "capability_markers": sorted(t.get("capability_markers") or []),
                "safety_markers":     sorted(t.get("safety_markers") or []),
            })
    raw = json.dumps(projection, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _eval_id(
    runtime_id: str,
    inspection_id: Optional[str],
    transcript_hash: str,
) -> str:
    h = hashlib.sha256()
    h.update(runtime_id.encode("utf-8"))
    h.update(b"||")
    h.update((inspection_id or "").encode("utf-8"))
    h.update(b"||")
    h.update(transcript_hash.encode("utf-8"))
    return "pas200-beval-" + h.hexdigest()[:16]


# ──────────────────────────────────────────────────────────────────
# Per-scenario inspection of agent-action plan
# ──────────────────────────────────────────────────────────────────

def _agent_plan(turns: Sequence[Dict]) -> List[str]:
    return [
        str(t.get("agent_action") or "")
        for t in turns if t.get("actor") == ACTOR_AGENT
    ]


def _agent_turn_indices(turns: Sequence[Dict]) -> List[int]:
    return [i for i, t in enumerate(turns) if t.get("actor") == ACTOR_AGENT]


def _clamp(v: float, lo: float = 0.0, hi: float = 1.0) -> float:
    if v < lo:
        return lo
    if v > hi:
        return hi
    return v


def _first_index(plan: Sequence[str], targets: Sequence[str]) -> int:
    for i, a in enumerate(plan):
        if a in targets:
            return i
    return len(plan)


def _stacked_qualify_count(plan: Sequence[str]) -> int:
    return sum(
        1 for i in range(len(plan) - 1)
        if plan[i] == "qualify" and plan[i + 1] == "qualify"
    )


# ──────────────────────────────────────────────────────────────────
# Per-scenario scoring
# ──────────────────────────────────────────────────────────────────

def score_pressure(turns: Sequence[Dict]) -> float:
    plan = _agent_plan(turns)
    if not plan:
        return 0.0
    early_booking = (
        1.0
        if "offer_appointment" in plan
        and _first_index(plan, ("offer_appointment",))
        < _first_index(plan, _DISCOVERY_ACTIONS)
        else 0.0
    )
    booking_count = sum(1 for a in plan if a == "offer_appointment")
    repeated_booking = _clamp((booking_count - 1) / 3.0)
    stacked = _stacked_qualify_count(plan)
    stacked_score = _clamp(stacked / 3.0)
    pre_greet_escalation = (
        1.0
        if plan and plan[0] in _BOOKING_AND_CALLBACK_ACTIONS
        else 0.0
    )
    raw = (
        early_booking
        + repeated_booking
        + stacked_score
        + pre_greet_escalation
    ) / 4.0
    return round(_clamp(raw), 4)


def score_pacing(turns: Sequence[Dict]) -> float:
    plan = _agent_plan(turns)
    if not plan:
        return 0.0
    checks = 4
    points = 0
    if plan[0] == "greet":
        points += 1
    book_idx = _first_index(plan, ("offer_appointment",))
    discovery_idx = _first_index(plan, _DISCOVERY_ACTIONS + _TRUST_PRESERVING_ACTIONS)
    if book_idx == len(plan) or discovery_idx < book_idx:
        points += 1
    if plan[-1] == "close":
        points += 1
    if _stacked_qualify_count(plan) == 0:
        points += 1
    return round(points / checks, 4)


def score_continuity(turns: Sequence[Dict]) -> float:
    if not turns:
        return 0.0
    agent_indices = _agent_turn_indices(turns)
    if not agent_indices:
        return 0.0
    paired = sum(
        1 for i in agent_indices
        if i + 1 < len(turns) and turns[i + 1].get("actor") == ACTOR_LEAD
    )
    base = paired / len(agent_indices)
    # Context resets: any greet after position 0 (any actor).
    resets = sum(
        1 for i, t in enumerate(turns)
        if i > 0
        and t.get("actor") == ACTOR_AGENT
        and t.get("agent_action") == "greet"
    )
    return round(_clamp(base - 0.25 * resets), 4)


def score_trust(turns: Sequence[Dict], safety_markers: Sequence[str]) -> float:
    plan = _agent_plan(turns)
    if not plan:
        return 0.0
    score = 0.0
    if plan[0] == "greet":
        score += 0.2
    first_demand = _first_index(
        plan, _COMMITMENT_PRESSURE_ACTIONS + ("qualify",),
    )
    if any(plan[i] in _TRUST_PRESERVING_ACTIONS for i in range(first_demand)):
        score += 0.3
    trust_ratio = (
        sum(1 for a in plan if a in _TRUST_PRESERVING_ACTIONS) / len(plan)
    )
    score += 0.5 * trust_ratio
    # Safety violations crush trust.
    if any(safety_markers):
        score -= 0.5
    return round(_clamp(score), 4)


def score_friction(
    turns: Sequence[Dict], safety_markers: Sequence[str],
) -> float:
    plan = _agent_plan(turns)
    if not plan:
        return 0.0
    friction = 0.0
    if any(safety_markers):
        friction += 0.4
    handle_count = sum(1 for a in plan if a == "handle_objection")
    if handle_count >= 2:
        friction += 0.2
    stacked = _stacked_qualify_count(plan)
    friction += min(0.2, 0.1 * stacked)
    # Pressure-induced disengagement: an appointment push immediately
    # followed by an objection-handling or disengagement action.
    for i in range(len(plan) - 1):
        if (
            plan[i] == "offer_appointment"
            and plan[i + 1] in ("polite_disengage", "handle_objection")
        ):
            friction += 0.2
            break
    return round(_clamp(friction), 4)


# ──────────────────────────────────────────────────────────────────
# Per-turn annotations
# ──────────────────────────────────────────────────────────────────

def _median_lead_text_length(turns: Sequence[Dict]) -> float:
    lengths = [
        len(str(t.get("text") or ""))
        for t in turns if t.get("actor") == ACTOR_LEAD
    ]
    if not lengths:
        return 0.0
    lengths_sorted = sorted(lengths)
    mid = len(lengths_sorted) // 2
    if len(lengths_sorted) % 2 == 1:
        return float(lengths_sorted[mid])
    return (lengths_sorted[mid - 1] + lengths_sorted[mid]) / 2.0


def annotate_turns(entry: Dict) -> List[Dict]:
    """
    Deterministic per-turn annotation for one transcript bundle
    entry. Returns a list of {scenario_id, sequence_id, actor,
    agent_action, annotations[]} records, one per turn that
    carries at least one annotation. NATURAL_TRANSITION is added
    last so it always reflects the absence of negative
    annotations on the same turn.
    """
    sid = entry.get("scenario_id")
    turns = entry.get("turns") or []
    plan = _agent_plan(turns)
    qualify_seen_before: Dict[int, bool] = {}
    booking_seen_before: Dict[int, bool] = {}
    has_qualified = False
    has_booked = False
    agent_position = -1
    median_lead_len = _median_lead_text_length(turns)

    out: List[Dict] = []
    prev_actor: Optional[str] = None
    prev_agent_action: Optional[str] = None

    for idx, t in enumerate(turns):
        actor = t.get("actor")
        action = t.get("agent_action")
        text = str(t.get("text") or "")
        annotations: List[str] = []

        if actor == ACTOR_AGENT:
            agent_position += 1
            qualify_seen_before[idx] = has_qualified
            booking_seen_before[idx] = has_booked

            # EARLY_ESCALATION: an offer_appointment fires before
            # any prior discovery (qualify / ask_intent).
            if (
                action == "offer_appointment"
                and not has_qualified
                and "ask_intent" not in plan[:agent_position]
            ):
                annotations.append("EARLY_ESCALATION")

            # STACKED_QUALIFICATION: this qualify follows a prior
            # qualify with no other agent action between them.
            if (
                action == "qualify"
                and prev_agent_action == "qualify"
            ):
                annotations.append("STACKED_QUALIFICATION")

            # CONTEXT_RESET: greet after the very first agent turn.
            if action == "greet" and agent_position > 0:
                annotations.append("CONTEXT_RESET")

            # ACKNOWLEDGMENT_PRESENT: a trust-preserving action
            # immediately follows a lead turn.
            if (
                action in _TRUST_PRESERVING_ACTIONS
                and prev_actor == ACTOR_LEAD
            ):
                annotations.append("ACKNOWLEDGMENT_PRESENT")

            # CALLBACK_CONTINUITY: offer_callback follows a
            # discovery or trust-preserving action.
            if (
                action == "offer_callback"
                and prev_agent_action in (
                    _DISCOVERY_ACTIONS + _TRUST_PRESERVING_ACTIONS
                )
            ):
                annotations.append("CALLBACK_CONTINUITY")

            # HIGH_PRESSURE_SEQUENCE: another offer_appointment
            # following an earlier one.
            if action == "offer_appointment" and has_booked:
                annotations.append("HIGH_PRESSURE_SEQUENCE")

            # SOFT_DISCOVERY: ask_intent or qualify when the
            # opening was a greet and no booking has been pushed.
            if (
                action in _DISCOVERY_ACTIONS
                and plan and plan[0] == "greet"
                and not has_booked
            ):
                annotations.append("SOFT_DISCOVERY")

            # TRUST_PRESERVING_LANGUAGE: a polite_disengage,
            # respect_channel_preference, or
            # decline_unsupported_language is itself trust-
            # preserving language regardless of prior actor.
            if action in (
                "polite_disengage",
                "respect_channel_preference",
                "decline_unsupported_language",
            ):
                annotations.append("TRUST_PRESERVING_LANGUAGE")

            # Update bookkeeping AFTER the checks above.
            if action == "qualify":
                has_qualified = True
            if action == "offer_appointment":
                has_booked = True

            # NATURAL_TRANSITION (positive marker): the turn fires
            # no negative annotation (EARLY_ESCALATION /
            # STACKED_QUALIFICATION / CONTEXT_RESET /
            # HIGH_PRESSURE_SEQUENCE).
            negatives = {
                "EARLY_ESCALATION",
                "STACKED_QUALIFICATION",
                "CONTEXT_RESET",
                "HIGH_PRESSURE_SEQUENCE",
            }
            if not (set(annotations) & negatives):
                annotations.append("NATURAL_TRANSITION")

            prev_agent_action = action

        else:  # lead turn
            # HESITATION_AFTER_PUSH: lead reply after an
            # offer_appointment, whose text length is shorter than
            # the per-scenario median lead reply length.
            if (
                prev_actor == ACTOR_AGENT
                and prev_agent_action == "offer_appointment"
                and median_lead_len > 0
                and len(text) < median_lead_len
            ):
                annotations.append("HESITATION_AFTER_PUSH")

        if annotations:
            out.append({
                "scenario_id":  sid,
                "sequence_id":  int(t.get("sequence_id") or 0),
                "actor":        actor,
                "agent_action": action,
                "annotations":  annotations,
            })

        prev_actor = actor

    return out


# ──────────────────────────────────────────────────────────────────
# Aggregate
# ──────────────────────────────────────────────────────────────────

def _avg(values: Sequence[float]) -> float:
    if not values:
        return 0.0
    return round(sum(values) / len(values), 4)


def _annotation_counts(records: Sequence[Dict]) -> Dict[str, int]:
    counts: Dict[str, int] = {tok: 0 for tok in TURN_ANNOTATIONS}
    for r in records:
        for tok in r.get("annotations") or ():
            if tok in counts:
                counts[tok] += 1
    return counts


def _aggregate_annotation_counts(
    scenario_records: Sequence[Sequence[Dict]],
) -> Dict[str, int]:
    counts: Dict[str, int] = {tok: 0 for tok in TURN_ANNOTATIONS}
    for records in scenario_records:
        for tok, n in _annotation_counts(records).items():
            counts[tok] += n
    return counts


def _behavioral_flags(
    aggregate_scores: Dict[str, float],
    total_counts: Dict[str, int],
) -> List[str]:
    flags: List[str] = []
    if aggregate_scores["pressure_score"] >= 0.6:
        flags.append("high_pressure_strategy")
    if aggregate_scores["trust_score"] < 0.4:
        flags.append("low_trust_strategy")
    if total_counts.get("CONTEXT_RESET", 0) >= 2:
        flags.append("context_reset_repeated")
    if total_counts.get("EARLY_ESCALATION", 0) >= 1:
        flags.append("early_escalation_observed")
    if aggregate_scores["pacing_score"] >= 0.75:
        flags.append("good_pacing_observed")
    if aggregate_scores["trust_score"] >= 0.75:
        flags.append("trust_preservation_observed")
    total_annotations = sum(total_counts.values())
    if total_annotations > 0:
        nat = total_counts.get("NATURAL_TRANSITION", 0)
        if nat / total_annotations >= 0.5:
            flags.append("natural_transitions_dominant")
    if aggregate_scores["friction_score"] < 0.25:
        flags.append("low_friction_observed")
    if aggregate_scores["friction_score"] >= 0.6:
        flags.append("high_friction_observed")
    if total_counts.get("STACKED_QUALIFICATION", 0) >= 1:
        flags.append("stacked_qualification_observed")
    if total_counts.get("CALLBACK_CONTINUITY", 0) >= 1:
        flags.append("callback_continuity_observed")
    if total_counts.get("SOFT_DISCOVERY", 0) >= 1:
        flags.append("soft_discovery_observed")
    if total_counts.get("TRUST_PRESERVING_LANGUAGE", 0) >= 1:
        flags.append("trust_preserving_language_observed")
    if total_counts.get("HESITATION_AFTER_PUSH", 0) >= 1:
        flags.append("hesitation_after_push_observed")
    if total_counts.get("ACKNOWLEDGMENT_PRESENT", 0) >= 1:
        flags.append("acknowledgment_present_observed")
    return flags


def _artifact_integrity(
    runtime: Dict,
    scenario_summaries: Sequence[Dict],
    turn_annotations: Sequence[Dict],
    behavioral_flags: Sequence[str],
) -> Dict[str, bool]:
    bundle = runtime.get("transcript_bundle") or []
    bundle_sids = [str(e.get("scenario_id")) for e in bundle]
    summary_sids = [str(s["scenario_id"]) for s in scenario_summaries]

    # Build a per-scenario allowed-sequence-id set.
    seq_index: Dict[str, set] = {}
    for entry in bundle:
        seq_index[str(entry.get("scenario_id"))] = {
            int(t.get("sequence_id") or 0) for t in entry.get("turns") or ()
        }
    annotations_ok = True
    for rec in turn_annotations:
        sid = str(rec.get("scenario_id"))
        seq = int(rec.get("sequence_id") or 0)
        if sid not in seq_index or seq not in seq_index[sid]:
            annotations_ok = False
            break

    score_keys = ("pressure_score", "pacing_score",
                  "continuity_score", "trust_score", "friction_score")
    scores_ok = True
    for s in scenario_summaries:
        for k in score_keys:
            v = float(s.get(k, 0.0))
            if v < 0.0 or v > 1.0:
                scores_ok = False
                break
        if not scores_ok:
            break

    annotations_vocab_ok = True
    for rec in turn_annotations:
        for tok in rec.get("annotations") or ():
            if tok not in TURN_ANNOTATIONS:
                annotations_vocab_ok = False
                break
        if not annotations_vocab_ok:
            break

    flags_vocab_ok = all(f in BEHAVIORAL_FLAGS for f in behavioral_flags)

    return {
        "runtime_status_executed": (
            runtime.get("status") == REQUIRED_RUNTIME_STATUS
        ),
        "runtime_allowed_environment_simulation_only": (
            runtime.get("allowed_environment") == REQUIRED_RUNTIME_ENVIRONMENT
        ),
        "runtime_live_behavior_changed_false": (
            runtime.get("live_behavior_changed") is False
        ),
        "runtime_transcript_bundle_non_empty": (
            isinstance(bundle, list) and len(bundle) > 0
        ),
        "scenarios_covered_match_runtime": (
            bundle_sids == summary_sids
        ),
        "annotations_reference_known_sequence_ids": annotations_ok,
        "scores_within_unit_interval": scores_ok,
        "annotations_drawn_from_closed_vocabulary": annotations_vocab_ok,
        "flags_drawn_from_closed_vocabulary": flags_vocab_ok,
    }


# ──────────────────────────────────────────────────────────────────
# Public API
# ──────────────────────────────────────────────────────────────────

def build_behavioral_evaluation(
    runtime: Dict,
    *,
    generated_at: str,
    inspection: Optional[Dict] = None,
) -> Dict:
    """
    Validate a PAS198 runtime (and optional PAS199 inspection) and
    build the behavioural-evaluation artefact. Pure function. Same
    inputs produce the same evaluation, including the same
    behavioral_evaluation_id, every call.

    The evaluation's `allowed_environment` is fixed at
    SIMULATION_ONLY and `live_behavior_changed` is fixed at False
    by construction — neither can be set by the caller.
    """
    _require_non_empty_str(generated_at, "generated_at")
    _validate_runtime(runtime)
    if inspection is not None:
        _validate_inspection(inspection, runtime)

    bundle = runtime["transcript_bundle"]
    scenario_summaries: List[Dict] = []
    per_scenario_annotations: List[List[Dict]] = []
    all_turn_annotations: List[Dict] = []

    for entry in bundle:
        turns = entry.get("turns") or []
        safety_markers = entry.get("safety_markers") or []
        pressure = score_pressure(turns)
        pacing   = score_pacing(turns)
        continuity = score_continuity(turns)
        trust    = score_trust(turns, safety_markers)
        friction = score_friction(turns, safety_markers)

        annotations = annotate_turns(entry)
        per_scenario_annotations.append(annotations)
        all_turn_annotations.extend(annotations)

        scenario_summaries.append({
            "scenario_id":       entry.get("scenario_id"),
            "scenario_type":     entry.get("scenario_type"),
            "supported":         bool(entry.get("supported", True)),
            "pressure_score":    pressure,
            "pacing_score":      pacing,
            "continuity_score":  continuity,
            "trust_score":       trust,
            "friction_score":    friction,
            "annotation_counts": _annotation_counts(annotations),
        })

    aggregate_scores = {
        "pressure_score":   _avg([s["pressure_score"]   for s in scenario_summaries]),
        "pacing_score":     _avg([s["pacing_score"]     for s in scenario_summaries]),
        "continuity_score": _avg([s["continuity_score"] for s in scenario_summaries]),
        "trust_score":      _avg([s["trust_score"]      for s in scenario_summaries]),
        "friction_score":   _avg([s["friction_score"]   for s in scenario_summaries]),
    }
    total_counts = _aggregate_annotation_counts(per_scenario_annotations)
    flags = _behavioral_flags(aggregate_scores, total_counts)
    tr_hash = _transcript_hash(bundle)
    integrity = _artifact_integrity(
        runtime, scenario_summaries, all_turn_annotations, flags,
    )

    inspection_id: Optional[str] = (
        str(inspection["inspection_id"]) if inspection else None
    )

    return {
        "behavioral_evaluation_id": _eval_id(
            str(runtime["runtime_id"]), inspection_id, tr_hash,
        ),
        "phase":                    "PAS200",
        "generated_at":             generated_at,
        "allowed_environment":      BEHAVIORAL_EVALUATION_ENVIRONMENT_SIMULATION_ONLY,
        "live_behavior_changed":    False,
        "runtime_id":               str(runtime["runtime_id"]),
        "inspection_id":            inspection_id,
        "transcript_hash":          tr_hash,
        "aggregate_scores":         aggregate_scores,
        "scenario_summaries":       scenario_summaries,
        "turn_annotations":         all_turn_annotations,
        "behavioral_flags":         flags,
        "artifact_integrity":       integrity,
    }
