"""
PAS208 — Operator-approval recommendation tests.

Coverage:

  * Every PAS205 signal type has a corresponding
    recommended_action_type, and every action type is reachable
    from at least one signal type.
  * build_recommendations is deterministic — same digest produces
    the same recommendation_ids and digest_id.
  * Every recommendation starts in CANDIDATE.
  * apply_decision is pure (returns a new object), accepts only
    bounded decisions, requires a non-empty operator_ref, and
    refuses re-decisions on already-terminal states.
  * Recommendation always carries operator_required=True and
    live_behavior_changed=False.
  * Source has no execute/dispatch/send/auto_apply identifiers.
  * Source imports no Twilio / Slack outbound / scheduler / worker.
  * Renderers leak no PAS internals into broker output.
  * Closed vocabularies are stable and sized correctly.
"""

from __future__ import annotations

import ast
import json
import pathlib
import sys
from typing import List, Tuple

import pytest


_REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))


from app.services.proactive.observer import observe  # noqa: E402
from app.services.proactive.observer_models import (  # noqa: E402
    SIGNAL_TYPES,
    AttentionSignal,
    NeedsAttentionDigest,
)
from app.services.proactive.recommendations import (  # noqa: E402
    APPROVAL_APPROVED_FOR_MANUAL_REVIEW,
    APPROVAL_CANDIDATE,
    APPROVAL_DEFERRED,
    APPROVAL_REJECTED,
    APPROVAL_STATES,
    RECOMMENDED_ACTION_TYPES,
    SIGNAL_TO_ACTION_TYPE,
    TERMINAL_APPROVAL_STATES,
    Recommendation,
    RecommendationDigest,
    apply_decision,
    build_recommendation,
    build_recommendations,
    to_broker_report,
    to_machine_json,
)
from app.services.slack.proactive_digest_intent import build_demo_snapshot  # noqa: E402


REC_SOURCE_PATH = (
    _REPO_ROOT / "app" / "services" / "proactive" / "recommendations.py"
)


def _read_source() -> str:
    return REC_SOURCE_PATH.read_text(encoding="utf-8")


# ──────────────────────────────────────────────────────────────────
# Vocabulary integrity
# ──────────────────────────────────────────────────────────────────


def test_every_signal_type_has_an_action_type() -> None:
    for sig_type in SIGNAL_TYPES:
        assert sig_type in SIGNAL_TO_ACTION_TYPE, (
            f"PAS208 missing action mapping for signal '{sig_type}'"
        )


def test_every_mapped_action_type_is_a_known_action() -> None:
    for action in SIGNAL_TO_ACTION_TYPE.values():
        assert action in RECOMMENDED_ACTION_TYPES, (
            f"action '{action}' not in RECOMMENDED_ACTION_TYPES"
        )


def test_action_types_match_signal_type_count() -> None:
    assert len(RECOMMENDED_ACTION_TYPES) == len(SIGNAL_TYPES) == 10


def test_approval_states_are_exactly_four() -> None:
    assert APPROVAL_STATES == (
        APPROVAL_CANDIDATE,
        APPROVAL_APPROVED_FOR_MANUAL_REVIEW,
        APPROVAL_REJECTED,
        APPROVAL_DEFERRED,
    )
    assert TERMINAL_APPROVAL_STATES == (
        APPROVAL_APPROVED_FOR_MANUAL_REVIEW,
        APPROVAL_REJECTED,
        APPROVAL_DEFERRED,
    )
    assert APPROVAL_CANDIDATE not in TERMINAL_APPROVAL_STATES


# ──────────────────────────────────────────────────────────────────
# Builder behaviour
# ──────────────────────────────────────────────────────────────────


def _signal(sig_type: str, idx: int = 0) -> AttentionSignal:
    return AttentionSignal(
        signal_id              = f"pas205-sig-{sig_type}-{idx}",
        signal_type            = sig_type,
        severity               = "high",
        subject_type           = "lead",
        subject_ref            = f"L-{idx:03d}",
        reason                 = "test",
        recommended_next_step  = "test next step",
        evidence               = {"k": "v"},
        created_at             = "2026-05-25T01:00:00Z",
        live_behavior_changed  = False,
    )


def _digest_with(signals: Tuple[AttentionSignal, ...]) -> NeedsAttentionDigest:
    return NeedsAttentionDigest(
        digest_id              = "pas205-dgst-fixture",
        generated_at           = "2026-05-25T01:00:00Z",
        observed_at            = "2026-05-25T01:00:00Z",
        signals                = signals,
    )


def test_build_recommendation_maps_each_signal_type_to_expected_action() -> None:
    for sig_type in SIGNAL_TYPES:
        rec = build_recommendation(_signal(sig_type))
        assert rec is not None, f"missing rec for {sig_type}"
        assert rec.signal_type == sig_type
        assert rec.recommended_action_type == SIGNAL_TO_ACTION_TYPE[sig_type]
        assert rec.approval_status == APPROVAL_CANDIDATE
        assert rec.operator_required is True
        assert rec.live_behavior_changed is False


def test_build_recommendation_returns_none_for_unknown_signal_type() -> None:
    bogus = AttentionSignal(
        signal_id              = "pas205-sig-bogus",
        signal_type            = "made_up_signal",
        severity               = "low",
        subject_type           = "lead",
        subject_ref            = "L-001",
        reason                 = "",
        recommended_next_step  = "",
        evidence               = {},
        created_at             = "2026-05-25T01:00:00Z",
        live_behavior_changed  = False,
    )
    assert build_recommendation(bogus) is None


def test_build_recommendation_returns_none_for_non_signal() -> None:
    assert build_recommendation("not a signal") is None  # type: ignore[arg-type]
    assert build_recommendation(None) is None             # type: ignore[arg-type]


def test_build_recommendations_is_deterministic() -> None:
    snap = build_demo_snapshot()
    d1 = observe(snap)
    d2 = observe(snap)
    rd1 = build_recommendations(d1)
    rd2 = build_recommendations(d2)
    assert rd1.digest_id == rd2.digest_id
    assert [r.recommendation_id for r in rd1.recommendations] == \
           [r.recommendation_id for r in rd2.recommendations]


def test_build_recommendations_carries_phase_and_invariants() -> None:
    snap = build_demo_snapshot()
    rd = build_recommendations(observe(snap))
    assert rd.phase == "PAS208"
    assert rd.allowed_environment == "SIMULATION_ONLY"
    assert rd.live_behavior_changed is False
    assert all(r.operator_required is True for r in rd.recommendations)
    assert all(r.live_behavior_changed is False for r in rd.recommendations)
    assert all(r.approval_status == APPROVAL_CANDIDATE for r in rd.recommendations)


def test_build_recommendations_counts_match_recommendations() -> None:
    snap = build_demo_snapshot()
    rd = build_recommendations(observe(snap))
    # All recommendations start as CANDIDATE.
    assert rd.counts_by_status[APPROVAL_CANDIDATE] == len(rd.recommendations)
    for state in (APPROVAL_APPROVED_FOR_MANUAL_REVIEW, APPROVAL_REJECTED, APPROVAL_DEFERRED):
        assert rd.counts_by_status[state] == 0
    # Sum over actions equals total recommendation count.
    assert sum(rd.counts_by_action_type.values()) == len(rd.recommendations)


def test_build_recommendations_rejects_non_digest() -> None:
    with pytest.raises(TypeError):
        build_recommendations("not a digest")  # type: ignore[arg-type]


# ──────────────────────────────────────────────────────────────────
# State machine
# ──────────────────────────────────────────────────────────────────


@pytest.fixture()
def candidate_rec() -> Recommendation:
    return build_recommendation(_signal("callback_overdue"))  # type: ignore[return-value]


@pytest.mark.parametrize("decision", [
    APPROVAL_APPROVED_FOR_MANUAL_REVIEW,
    APPROVAL_REJECTED,
    APPROVAL_DEFERRED,
])
def test_apply_decision_transitions_to_each_terminal_state(
    candidate_rec: Recommendation, decision: str,
) -> None:
    out = apply_decision(candidate_rec, decision, operator_ref="op-1")
    assert out is not candidate_rec  # new object
    assert out.approval_status == decision
    assert out.decided_by == "op-1"
    assert out.decided_at  # populated
    assert out.live_behavior_changed is False
    assert out.operator_required is True
    # Original untouched
    assert candidate_rec.approval_status == APPROVAL_CANDIDATE
    assert candidate_rec.decided_at is None


def test_apply_decision_records_reason_and_timestamp(
    candidate_rec: Recommendation,
) -> None:
    out = apply_decision(
        candidate_rec,
        APPROVAL_APPROVED_FOR_MANUAL_REVIEW,
        operator_ref="op-1",
        reason="checked with lead manager",
        decided_at="2026-05-25T02:00:00Z",
    )
    assert out.decided_at == "2026-05-25T02:00:00Z"
    assert out.decision_reason == "checked with lead manager"


def test_apply_decision_rejects_unknown_decision(
    candidate_rec: Recommendation,
) -> None:
    for bad in ("approve", "yes", "OK", "approve!", "", APPROVAL_CANDIDATE):
        with pytest.raises(ValueError):
            apply_decision(candidate_rec, bad, operator_ref="op-1")


def test_apply_decision_requires_non_empty_operator_ref(
    candidate_rec: Recommendation,
) -> None:
    for bad in ("", "   ", None):
        with pytest.raises((ValueError, TypeError)):
            apply_decision(candidate_rec, APPROVAL_APPROVED_FOR_MANUAL_REVIEW, operator_ref=bad)  # type: ignore[arg-type]


def test_apply_decision_refuses_redecision_on_already_terminal_states(
    candidate_rec: Recommendation,
) -> None:
    approved = apply_decision(candidate_rec, APPROVAL_APPROVED_FOR_MANUAL_REVIEW, operator_ref="op-1")
    with pytest.raises(ValueError):
        apply_decision(approved, APPROVAL_REJECTED, operator_ref="op-1")
    rejected = apply_decision(candidate_rec, APPROVAL_REJECTED, operator_ref="op-1")
    with pytest.raises(ValueError):
        apply_decision(rejected, APPROVAL_APPROVED_FOR_MANUAL_REVIEW, operator_ref="op-1")


def test_apply_decision_allows_redecision_from_deferred(
    candidate_rec: Recommendation,
) -> None:
    deferred = apply_decision(candidate_rec, APPROVAL_DEFERRED, operator_ref="op-1")
    # DEFERRED is the only re-entry point; can transition again.
    approved = apply_decision(deferred, APPROVAL_APPROVED_FOR_MANUAL_REVIEW, operator_ref="op-1")
    assert approved.approval_status == APPROVAL_APPROVED_FOR_MANUAL_REVIEW


def test_apply_decision_rejects_non_recommendation() -> None:
    with pytest.raises(TypeError):
        apply_decision("not a rec", APPROVAL_REJECTED, operator_ref="op-1")  # type: ignore[arg-type]


# ──────────────────────────────────────────────────────────────────
# Recommendation immutability
# ──────────────────────────────────────────────────────────────────


def test_recommendation_dataclass_is_frozen(candidate_rec: Recommendation) -> None:
    import dataclasses
    with pytest.raises(dataclasses.FrozenInstanceError):
        candidate_rec.approval_status = APPROVAL_REJECTED  # type: ignore[misc]


# ──────────────────────────────────────────────────────────────────
# Renderers
# ──────────────────────────────────────────────────────────────────


def test_machine_json_is_json_serialisable() -> None:
    snap = build_demo_snapshot()
    rd = build_recommendations(observe(snap))
    machine = to_machine_json(rd)
    blob = json.dumps(machine, sort_keys=True)
    parsed = json.loads(blob)
    assert parsed["phase"] == "PAS208"
    assert parsed["live_behavior_changed"] is False
    assert len(parsed["recommendations"]) == len(rd.recommendations)


def test_broker_report_says_nothing_when_no_recommendations() -> None:
    empty_digest = _digest_with(())
    rd = build_recommendations(empty_digest)
    out = to_broker_report(rd)
    assert "nothing for you to approve" in out.lower()
    assert "I have not taken any action" in out


def test_broker_report_does_not_leak_pas_internals() -> None:
    snap = build_demo_snapshot()
    rd = build_recommendations(observe(snap))
    out = to_broker_report(rd)
    for token in (
        "SIMULATION_ONLY",
        "live_behavior_changed",
        "signal_id",
        "recommendation_id",
        "pas208-rec-",
        "pas208-dgst-",
    ):
        assert token not in out, f"broker report leaked '{token}'"


def test_broker_report_mentions_operator_decision_and_no_action() -> None:
    snap = build_demo_snapshot()
    rd = build_recommendations(observe(snap))
    out = to_broker_report(rd)
    assert "you decide" in out.lower()
    assert "i have not taken any action" in out.lower()


# ──────────────────────────────────────────────────────────────────
# Source-level safety invariants
# ──────────────────────────────────────────────────────────────────


def test_source_has_no_db_mutation_methods() -> None:
    src = _read_source()
    for token in (".insert(", ".update(", ".delete(", ".upsert(", ".rpc("):
        assert token not in src, f"PAS208 source contains '{token}'"


def test_source_has_no_executor_identifiers() -> None:
    src = _read_source()
    for token in (
        "def execute",
        "def dispatch",
        "def send_real_",
        "def auto_apply",
        "def auto_promote",
        "def post_to_slack",
        "def route_lead_live",
    ):
        assert token not in src, f"PAS208 source contains forbidden identifier '{token}'"


def test_source_has_no_outbound_messaging_calls() -> None:
    src = _read_source()
    for token in (
        "send_slack_message",
        "twilio_client",
        "requests.post",
        "httpx.post",
        "send_sms",
        "send_email",
    ):
        assert token not in src, f"PAS208 source mentions outbound token '{token}'"


def test_source_imports_no_forbidden_modules() -> None:
    src = _read_source()
    tree = ast.parse(src)
    forbidden = {
        "twilio", "slack_sdk", "openai", "anthropic",
        "smtplib", "apscheduler", "celery", "supabase",
    }
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                root = alias.name.split(".")[0]
                assert root not in forbidden, (
                    f"PAS208 imports forbidden module: {alias.name}"
                )
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                root = node.module.split(".")[0]
                assert root not in forbidden, (
                    f"PAS208 imports forbidden module: {node.module}"
                )


def test_source_has_no_scheduler_or_worker_tokens() -> None:
    src = _read_source()
    for token in ("apscheduler", "celery", "schedule_job", "worker.start", "cron"):
        assert token not in src, f"PAS208 source contains scheduler/worker token '{token}'"


def test_source_does_not_touch_migration_artifact() -> None:
    assert "combined_supabase_migration" not in _read_source()


def test_recommendation_id_is_deterministic() -> None:
    s1 = _signal("callback_overdue", 1)
    s2 = _signal("callback_overdue", 1)
    r1 = build_recommendation(s1)
    r2 = build_recommendation(s2)
    assert r1.recommendation_id == r2.recommendation_id


def test_recommendation_ids_differ_across_subjects() -> None:
    r1 = build_recommendation(_signal("callback_overdue", 1))
    r2 = build_recommendation(_signal("callback_overdue", 2))
    assert r1.recommendation_id != r2.recommendation_id


def test_recommendation_action_type_changes_recommendation_id() -> None:
    # Two different signal types on the same subject must produce
    # different recommendation_ids.
    r1 = build_recommendation(_signal("callback_overdue", 1))
    r2 = build_recommendation(_signal("lead_unassigned", 1))
    assert r1.recommendation_id != r2.recommendation_id
