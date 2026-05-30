"""
PAS209 — Bounded action-proposal package tests.

Coverage:

  * build_proposal returns None for CANDIDATE / REJECTED / DEFERRED
    recommendations and for non-Recommendation inputs.
  * Only APPROVED_FOR_MANUAL_REVIEW recommendations produce a
    proposal.
  * Every action_type has a draft / safety_notes / rollback_notes
    template; no action_type is missing from the template map.
  * Every emitted ActionProposal carries
    required_human_review=True, allowed_channel='MANUAL_ONLY',
    live_behavior_changed=False.
  * proposal_id is deterministic given (recommendation_id, action).
  * build_proposal_package walks the digest and includes one
    proposal per approved recommendation.
  * Renderers leak no PAS internals / closed-vocab tokens / IDs.
  * Source has no execute/dispatch/send_real/auto_apply identifiers.
  * Source imports no Twilio / Slack outbound / scheduler / worker /
    supabase / openai / anthropic.
  * Closed vocabularies are stable.
"""

from __future__ import annotations

import ast
import json
import pathlib
import sys
from typing import Tuple

import pytest


_REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))


from app.services.proactive.action_proposals import (  # noqa: E402
    ALLOWED_CHANNEL_MANUAL_ONLY,
    ALLOWED_CHANNELS,
    ActionProposal,
    ActionProposalPackage,
    _PROPOSAL_TEMPLATES,
    build_proposal,
    build_proposal_package,
    to_broker_report,
    to_machine_json,
)
from app.services.proactive.observer import observe  # noqa: E402
from app.services.proactive.observer_models import SIGNAL_TYPES  # noqa: E402
from app.services.proactive.recommendations import (  # noqa: E402
    APPROVAL_APPROVED_FOR_MANUAL_REVIEW,
    APPROVAL_CANDIDATE,
    APPROVAL_DEFERRED,
    APPROVAL_REJECTED,
    RECOMMENDED_ACTION_TYPES,
    SIGNAL_TO_ACTION_TYPE,
    Recommendation,
    RecommendationDigest,
    apply_decision,
    build_recommendation,
    build_recommendations,
)
from app.services.slack.proactive_digest_intent import (  # noqa: E402
    build_demo_snapshot,
)


SOURCE_PATH = _REPO_ROOT / "app" / "services" / "proactive" / "action_proposals.py"


def _read_source() -> str:
    return SOURCE_PATH.read_text(encoding="utf-8")


def _approved_rec(signal_type: str = "callback_overdue") -> Recommendation:
    from app.services.proactive.observer_models import AttentionSignal
    sig = AttentionSignal(
        signal_id              = f"pas205-sig-{signal_type}-001",
        signal_type            = signal_type,
        severity               = "high",
        subject_type           = "lead",
        subject_ref            = "L-001",
        reason                 = "test",
        recommended_next_step  = "test next step",
        evidence               = {"k": "v"},
        created_at             = "2026-05-25T01:00:00Z",
        live_behavior_changed  = False,
    )
    rec = build_recommendation(sig)
    assert rec is not None
    return apply_decision(rec, APPROVAL_APPROVED_FOR_MANUAL_REVIEW, operator_ref="op-1")


# ──────────────────────────────────────────────────────────────────
# Template integrity
# ──────────────────────────────────────────────────────────────────


def test_every_action_type_has_a_template() -> None:
    for action in RECOMMENDED_ACTION_TYPES:
        assert action in _PROPOSAL_TEMPLATES, (
            f"PAS209 missing template for action '{action}'"
        )
        draft, safety, rollback = _PROPOSAL_TEMPLATES[action]
        assert isinstance(draft, str) and draft.strip()
        assert isinstance(safety, tuple) and len(safety) >= 1
        assert isinstance(rollback, tuple) and len(rollback) >= 1


def test_no_extra_templates_beyond_action_vocabulary() -> None:
    extras = set(_PROPOSAL_TEMPLATES) - set(RECOMMENDED_ACTION_TYPES)
    assert not extras, f"PAS209 template map has stray entries: {extras}"


def test_allowed_channels_is_closed_to_manual_only() -> None:
    assert ALLOWED_CHANNELS == (ALLOWED_CHANNEL_MANUAL_ONLY,)
    assert ALLOWED_CHANNEL_MANUAL_ONLY == "MANUAL_ONLY"


# ──────────────────────────────────────────────────────────────────
# build_proposal — gating
# ──────────────────────────────────────────────────────────────────


def test_build_proposal_returns_none_for_candidate() -> None:
    from app.services.proactive.observer_models import AttentionSignal
    sig = AttentionSignal(
        signal_id="pas205-sig-1", signal_type="callback_overdue",
        severity="high", subject_type="lead", subject_ref="L-1",
        reason="", recommended_next_step="", evidence={},
        created_at="2026-05-25T01:00:00Z", live_behavior_changed=False,
    )
    rec = build_recommendation(sig)
    assert rec is not None
    assert rec.approval_status == APPROVAL_CANDIDATE
    assert build_proposal(rec) is None


def test_build_proposal_returns_none_for_rejected() -> None:
    from app.services.proactive.observer_models import AttentionSignal
    sig = AttentionSignal(
        signal_id="pas205-sig-2", signal_type="callback_overdue",
        severity="high", subject_type="lead", subject_ref="L-2",
        reason="", recommended_next_step="", evidence={},
        created_at="2026-05-25T01:00:00Z", live_behavior_changed=False,
    )
    rec = build_recommendation(sig)
    rejected = apply_decision(rec, APPROVAL_REJECTED, operator_ref="op-1")
    assert build_proposal(rejected) is None


def test_build_proposal_returns_none_for_deferred() -> None:
    from app.services.proactive.observer_models import AttentionSignal
    sig = AttentionSignal(
        signal_id="pas205-sig-3", signal_type="callback_overdue",
        severity="high", subject_type="lead", subject_ref="L-3",
        reason="", recommended_next_step="", evidence={},
        created_at="2026-05-25T01:00:00Z", live_behavior_changed=False,
    )
    rec = build_recommendation(sig)
    deferred = apply_decision(rec, APPROVAL_DEFERRED, operator_ref="op-1")
    assert build_proposal(deferred) is None


def test_build_proposal_returns_none_for_non_recommendation() -> None:
    assert build_proposal(None) is None  # type: ignore[arg-type]
    assert build_proposal("not a rec") is None  # type: ignore[arg-type]
    assert build_proposal({"approval_status": "APPROVED_FOR_MANUAL_REVIEW"}) is None  # type: ignore[arg-type]


# ──────────────────────────────────────────────────────────────────
# build_proposal — happy path
# ──────────────────────────────────────────────────────────────────


@pytest.mark.parametrize("signal_type", list(SIGNAL_TYPES))
def test_build_proposal_for_every_signal_type(signal_type: str) -> None:
    rec = _approved_rec(signal_type)
    prop = build_proposal(rec)
    assert prop is not None, f"PAS209 produced no proposal for {signal_type}"
    assert prop.recommendation_id == rec.recommendation_id
    assert prop.signal_type == signal_type
    assert prop.proposed_action_type == SIGNAL_TO_ACTION_TYPE[signal_type]
    assert prop.draft_message_or_instruction.strip()
    assert len(prop.safety_notes) >= 1
    assert len(prop.rollback_notes) >= 1


def test_proposal_hard_invariants_always_set() -> None:
    rec = _approved_rec("callback_overdue")
    prop = build_proposal(rec)
    assert prop.required_human_review is True
    assert prop.allowed_channel == ALLOWED_CHANNEL_MANUAL_ONLY
    assert prop.live_behavior_changed is False


def test_proposal_id_is_deterministic() -> None:
    r1 = _approved_rec("callback_overdue")
    r2 = _approved_rec("callback_overdue")
    p1 = build_proposal(r1)
    p2 = build_proposal(r2)
    assert p1.proposal_id == p2.proposal_id


def test_proposal_id_differs_across_signal_types() -> None:
    p1 = build_proposal(_approved_rec("callback_overdue"))
    p2 = build_proposal(_approved_rec("lead_unassigned"))
    assert p1.proposal_id != p2.proposal_id


def test_proposal_is_frozen() -> None:
    import dataclasses
    prop = build_proposal(_approved_rec("callback_overdue"))
    with pytest.raises(dataclasses.FrozenInstanceError):
        prop.live_behavior_changed = True  # type: ignore[misc]


# ──────────────────────────────────────────────────────────────────
# build_proposal_package
# ──────────────────────────────────────────────────────────────────


def _digest_with_first_n_approved(n: int) -> RecommendationDigest:
    snap = build_demo_snapshot()
    rd = build_recommendations(observe(snap))
    new_recs = list(rd.recommendations)
    for i in range(min(n, len(new_recs))):
        new_recs[i] = apply_decision(
            new_recs[i], APPROVAL_APPROVED_FOR_MANUAL_REVIEW, operator_ref="op-1",
        )
    return RecommendationDigest(
        digest_id              = rd.digest_id,
        generated_at           = rd.generated_at,
        source_digest_id       = rd.source_digest_id,
        observed_at            = rd.observed_at,
        phase                  = rd.phase,
        allowed_environment    = rd.allowed_environment,
        live_behavior_changed  = rd.live_behavior_changed,
        recommendations        = tuple(new_recs),
        counts_by_status       = rd.counts_by_status,
        counts_by_action_type  = rd.counts_by_action_type,
    )


def test_build_proposal_package_empty_when_no_approved() -> None:
    rd = _digest_with_first_n_approved(0)
    pkg = build_proposal_package(rd)
    assert pkg.proposals == ()
    assert pkg.phase == "PAS209"
    assert pkg.live_behavior_changed is False
    assert sum(pkg.counts_by_action_type.values()) == 0


def test_build_proposal_package_includes_only_approved() -> None:
    rd = _digest_with_first_n_approved(3)
    pkg = build_proposal_package(rd)
    assert len(pkg.proposals) == 3
    for p in pkg.proposals:
        assert p.required_human_review is True
        assert p.allowed_channel == ALLOWED_CHANNEL_MANUAL_ONLY
        assert p.live_behavior_changed is False


def test_build_proposal_package_is_deterministic() -> None:
    rd1 = _digest_with_first_n_approved(2)
    rd2 = _digest_with_first_n_approved(2)
    pkg1 = build_proposal_package(rd1)
    pkg2 = build_proposal_package(rd2)
    assert pkg1.package_id == pkg2.package_id
    assert [p.proposal_id for p in pkg1.proposals] == [p.proposal_id for p in pkg2.proposals]


def test_build_proposal_package_rejects_non_digest() -> None:
    with pytest.raises(TypeError):
        build_proposal_package("not a digest")  # type: ignore[arg-type]


# ──────────────────────────────────────────────────────────────────
# Renderers
# ──────────────────────────────────────────────────────────────────


def test_machine_json_is_serialisable() -> None:
    rd = _digest_with_first_n_approved(3)
    pkg = build_proposal_package(rd)
    machine = to_machine_json(pkg)
    blob = json.dumps(machine, sort_keys=True)
    parsed = json.loads(blob)
    assert parsed["phase"] == "PAS209"
    assert parsed["live_behavior_changed"] is False
    assert len(parsed["proposals"]) == 3
    for p in parsed["proposals"]:
        assert p["required_human_review"] is True
        assert p["allowed_channel"] == "MANUAL_ONLY"
        assert p["live_behavior_changed"] is False


def test_broker_report_empty_message_when_no_proposals() -> None:
    rd = _digest_with_first_n_approved(0)
    pkg = build_proposal_package(rd)
    out = to_broker_report(pkg)
    assert "no approved items" in out.lower()


def test_broker_report_says_manual_only() -> None:
    rd = _digest_with_first_n_approved(2)
    pkg = build_proposal_package(rd)
    out = to_broker_report(pkg)
    assert "Manual only" in out
    assert "PAS will not send" in out
    assert "human" in out.lower()


def test_broker_report_leaks_no_pas_internals() -> None:
    rd = _digest_with_first_n_approved(3)
    pkg = build_proposal_package(rd)
    out = to_broker_report(pkg)
    for token in (
        "SIMULATION_ONLY",
        "live_behavior_changed",
        "signal_id",
        "recommendation_id",
        "proposal_id",
        "pas209-prop-",
        "pas209-pkg-",
        "pas208-rec-",
    ):
        assert token not in out, f"broker report leaked '{token}'"


# ──────────────────────────────────────────────────────────────────
# Source safety invariants
# ──────────────────────────────────────────────────────────────────


def test_source_has_no_db_mutation_methods() -> None:
    src = _read_source()
    for token in (".insert(", ".update(", ".delete(", ".upsert(", ".rpc("):
        assert token not in src, f"PAS209 source contains '{token}'"


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
        assert token not in src, f"PAS209 source contains identifier '{token}'"


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
        assert token not in src, f"PAS209 source mentions outbound token '{token}'"


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
                    f"PAS209 imports forbidden module: {alias.name}"
                )
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                root = node.module.split(".")[0]
                assert root not in forbidden, (
                    f"PAS209 imports forbidden module: {node.module}"
                )


def test_source_has_no_scheduler_or_worker_tokens() -> None:
    src = _read_source()
    for token in ("apscheduler", "celery", "schedule_job", "worker.start", "cron"):
        assert token not in src, f"PAS209 source contains scheduler/worker token '{token}'"


def test_source_does_not_touch_migration_artifact() -> None:
    assert "combined_supabase_migration" not in _read_source()


def test_source_does_not_reference_engine_or_state_machine() -> None:
    src = _read_source()
    for token in ("app.engine", "state_machine", "app.services.outbound"):
        assert token not in src, f"PAS209 source mentions '{token}'"
