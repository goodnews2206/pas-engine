"""
PAS140A — Unified event contract: canonical vocabulary.

This module is intentionally pure data. No imports from app.*, no
runtime validators, no I/O. Its purpose is twofold:

  1. Documentation source-of-truth for which event_type / actor /
     workflow_stage / source values PAS recognises.

  2. Test target — tests assert that every event_type currently logged
     by the codebase appears in KNOWN_EVENT_TYPES, so a typo in a new
     event_type literal is caught by CI rather than silently ignored
     by the workflow mapper.

Strict runtime enforcement is deliberately deferred. PAS140A keeps
event_logger permissive (unknown event_types are still inserted)
because:

  - The codebase has many existing call sites that this module must
    not break.
  - PAS140B / PAS141 will introduce new event_types incrementally;
    requiring a contract update before each new emit would slow that
    work down without buying safety.

When PAS reaches the brain phase (PAS141+) and the schema stabilises,
flip on a `STRICT=True` mode that warns (not raises) on unknown
event_types — see app/db/event_logger.log_event for the seam.

References:
  - scripts/migrate_v8_event_contract.sql — DB columns
  - app/db/event_logger.py — write path that consumes these constants
  - PAS139/PAS140 audit report — full rationale
"""

from typing import FrozenSet


# ── EVENT TYPES ─────────────────────────────────────────────────────
# Every event_type currently emitted by the codebase, as of PAS140A.
# Keep this set in sync with new emits as they land. Tests in
# tests/event_contract/test_contract_constants.py guard the set.
#
# Naming convention: "<noun>.<past-tense-or-state>", lowercase, dot
# separator, no version suffix. Past-tense for state changes
# ("call.started"), nouns for terminal aggregates ("call.ended").

KNOWN_EVENT_TYPES: FrozenSet[str] = frozenset({
    # Call lifecycle
    "call.started",
    "call.ended",
    "call.failed",
    "call.ended_with_callback",

    # Engine state machine
    "state.transition",

    # Lead extraction & memory
    "lead.extracted",
    "lead.updated",

    # Conversation events
    "objection.detected",
    "callback.requested",

    # Turn-level utterances (PAS140C)
    # Together these reconstruct the conversation turn-by-turn from the
    # event stream alone, no `calls.transcript` join required. Volume
    # is significant (≈ 1 row per spoken turn) so emission is gated by
    # Settings.PAS_EVENT_TURN_LOGGING — see app/config.py.
    "lead.uttered",
    "pas.uttered",

    # Booking flow
    "booking.attempted",
    "booking.confirmed",
    "booking.failed",

    # Provider / system health
    "provider.failed",
    "system.error",

    # PAS144H — runtime memory injection observability. Emitted from
    # PASEngine._build_prompt_with_memory. Payloads are structural only
    # — never carry memory summaries, evidence, raw prompts, transcripts,
    # or formatted memory text. See state_machine.py for the emit sites.
    "memory.injection.skipped",
    "memory.injection.attempted",
    "memory.injection.succeeded",
    "memory.injection.failed",

    # PAS144L — operator-approved memory-rollout audit trail. Emitted
    # from app/services/memory/approval.py. Payloads are structural
    # only (approval_id, brokerage_id, recommended_action,
    # target_enabled, dry_run, applied, error_code) — never carry
    # plan evidence, memory text, transcripts, or prompts.
    "memory.rollout.approved",
    "memory.rollout.applied",
    "memory.rollout.failed",

    # PAS163 — outbound dial + memory candidate pipeline. Emitted
    # from the pending-call worker, the outbound dial adapter, and
    # the memory candidate pipeline. Payloads are structural only —
    # call_id / pending_call_id / source / candidate_count /
    # failed_count / warning_count / error_code. NEVER carry phone /
    # email / name / transcript / raw_payload / evidence text /
    # summary text / prompt text.
    "pending_call.dialed",
    "pending_call.failed",
    "memory.candidate.generated",
    "memory.candidate.generation_failed",

    # PAS164 — email lead ingestion. Emitted from
    # app/routes/email_ingestion.py for each parse / ingest
    # request. Payloads are structural only — source / has_phone
    # / has_email / call_eligible / call_queued / warning_count
    # / error_code. NEVER carry phone / email / name / subject /
    # body / property / transcript / raw_payload.
    "email.lead.parsed",
    "email.lead.ingested",
    "email.lead.failed",
    "email.lead.not_call_eligible",

    # PAS165 — email forwarder authentication + dedupe.
    # Emitted from app/routes/email_ingestion.py alongside the
    # PAS164 outcome event. Payloads are structural only —
    # source / call_queued / warning_count / forwarder_verified
    # / duplicate / error_code. NEVER carry phone / email /
    # name / subject / sender / body / signature / dedupe_key.
    "email.lead.duplicate",
    "email.forwarder.signature_invalid",
    "email.forwarder.signature_missing",
    "email.forwarder.signature_unconfigured",
    "email.forwarder.verified",

    # PAS166 — durable email dedupe + signature-required
    # policy. Emitted from app/routes/email_ingestion.py.
    # Payloads structural only — source / forwarder_verified
    # / forwarder_required / dedupe_durable / duplicate /
    # warning_count / error_code. NEVER carry dedupe_key /
    # signature / secret / phone / email / name / subject /
    # sender / body / raw_email / raw_body / property_address
    # / notes / transcript.
    "email.dedupe.durable_registered",
    "email.dedupe.durable_duplicate",
    "email.dedupe.fallback_process_local",
    "email.forwarder.signature_required_missing",
    "email.forwarder.secret_missing",

    # PAS167 — email forwarder secret-at-rest encryption +
    # operator dedupe reaper. Emitted from
    # app/routes/email_ingestion.py and from the operator
    # reaper script. Payloads structural only — source /
    # encryption_enabled / plaintext_fallback / dry_run /
    # deleted_count / limit / older_than_hours /
    # warning_count / error_code. NEVER carry secret /
    # encrypted_secret / signature / dedupe_key / phone /
    # email / name / subject / sender / body / raw_email /
    # raw_body / property_address / notes / transcript.
    "email.dedupe.reaper.dry_run",
    "email.dedupe.reaper.deleted",
    "email.forwarder.secret.encrypted",
    "email.forwarder.secret.decrypt_failed",
    "email.forwarder.secret.plaintext_fallback",

    # PAS168 — operator-driven kid-aware secret rotation.
    # Emitted from scripts/rotate_email_forwarder_secret.py
    # for each batch run (dry-run vs execute) and from
    # per-row failure paths. Payloads structural only —
    # dry_run / rotated_count / skipped_count /
    # failed_count / limit / kid / encryption_enabled /
    # warning_count / error_code. NEVER carry secret /
    # encrypted_secret / key / key_material / signature /
    # dedupe_key / phone / email / name / subject / sender
    # / body / raw_email / raw_body / property_address /
    # notes / transcript.
    "email.forwarder.secret.rotation_dry_run",
    "email.forwarder.secret.rotated",
    "email.forwarder.secret.rotation_failed",

    # PAS170 — operator survival kit.
    # Pending-call resilience + dedupe + callback lifecycle
    # + alert transport. Payloads structural only — see the
    # PAS170 allow-list in app/routes/admin.py / the
    # readiness checker. NEVER carry phone / email / name /
    # raw_payload / raw_email / raw_body / transcript /
    # summary / secret / signature / dedupe_key.
    "pending_call.stale_detected",
    "pending_call.recovered",
    "pending_call.duplicate_suppressed",
    "callback.schedule.proposed",
    "callback.reminder.due",
    "alert.slack.sent",
    "alert.slack.failed",
    "provider.failure_storm.detected",
    "worker.liveness.missing",

    # PAS171 — external pilot hardening.
    # Durable backing for pending-call dedupe + callback
    # schedule, plus pilot-grade outbound Slack hardening.
    # Payloads structural only — see the PAS171 doctrine in
    # docs/pas171_external_pilot_hardening.md. NEVER carry
    # phone / email / name / raw_payload / raw_email /
    # raw_body / transcript / summary / secret / signature /
    # dedupe_key.
    "pending_call.dedupe.durable_registered",
    "pending_call.dedupe.durable_duplicate",
    "pending_call.dedupe.fallback_process_local",
    "callback.schedule.durable_registered",
    "callback.schedule.durable_duplicate",
    "callback.schedule.fallback_process_local",
    "external_pilot.heartbeat",
    "external_pilot.dedupe_fallback",
    "external_pilot.callback_schedule_fallback",
    "external_pilot.cal_com_sanity_failed",
    "external_pilot.cal_com_sanity_ok",

    # PAS172 — pilot operations control layer.
    # Durable worker heartbeat + reapers + Slack employee mode
    # (OPS-ONLY) + operator ops routes. Payloads structural
    # only — see app/services/events/contract.py allow-list +
    # the PAS172 readiness checker. NEVER carry phone / email
    # / name / transcript / raw_payload / raw_email / raw_body
    # / summary / secret / signature / dedupe_key /
    # callback_notes.
    "worker.heartbeat.started",
    "worker.heartbeat.updated",
    "worker.heartbeat.stale",
    "worker.heartbeat.stopped",
    "callback.reminder.generated",
    "reaper.pending_call_dedupe.executed",
    "reaper.callback_schedule.executed",
    "slack.employee.summary.generated",

    # PAS173 — brokerage operator system + controlled
    # self-serve. Payloads structural only — see
    # docs/pas173_brokerage_operator_system.md. NEVER carry
    # phone / email / name / transcript / raw_payload /
    # raw_email / raw_body / summary / secret / signature /
    # dedupe_key / callback_notes / env_values.
    "brokerage.onboarding.started",
    "brokerage.onboarding.completed",
    "brokerage.stage.updated",
    "brokerage.paused",
    "brokerage.resumed",
    "brokerage.launch.readiness_generated",
    "operator.action.executed",

    # PAS174 — operator audit layer + tenant visibility.
    # Payloads structural only — see
    # docs/pas174_operator_audit_layer.md. NEVER carry phone
    # / email / transcript / raw_payload / secret /
    # signature / env_values / callback_notes / dedupe_key.
    "operator.audit.logged",
    "operator.audit.failed",
    "tenant.visibility.requested",
    "connectivity.probe.executed",
    "connectivity.probe.failed",

    # PAS175 — audit integrity + tenant audit visibility +
    # three bounded operator actions. Payloads structural
    # only — see docs/pas175_audit_integrity_and_tenant_audit_
    # visibility.md. NEVER carry phone / email / transcript /
    # raw_payload / secret / signature / env_values /
    # callback_notes / dedupe_key.
    "audit.chain.verified",
    "audit.chain.broken",
    "audit.reaper.executed",
    "tenant.audit.requested",
    "operator.action.readiness_email_requested",
    "operator.action.rotation_requested",
    "operator.action.pilot_stage_evidenced",

    # PAS176 — audit chain Merkle + verification + tenant
    # acknowledgement. Payloads structural only — see
    # docs/pas176_audit_chain_verification.md. NEVER carry
    # phone / email / transcript / raw_payload / secret /
    # signature / env_values / callback_notes / dedupe_key.
    "audit.merkle.root_persisted",
    "audit.chain.window_verified",
    "audit.chain.window_break_detected",
    "audit.backfill.executed",
    "tenant.audit.acknowledged",

    # PAS177 — durable tenant ACK + Merkle inclusion proofs.
    # Payloads structural only — see
    # docs/pas177_tenant_audit_acknowledgements_and_inclusion_proofs.md.
    # NEVER carry phone / email / transcript / raw_payload /
    # secret / signature / env_values / callback_notes /
    # dedupe_key / raw_audit_metadata.
    "tenant.audit.acknowledgement.failed",
    "tenant.audit.proof.generated",
    "tenant.audit.proof.verification_failed",
    "audit.verification.scheduled_template_generated",

    # PAS178 — cross-window audit chain + verification
    # persistence. Payloads structural only — see
    # docs/pas178_audit_window_chain_and_dashboards.md. NEVER
    # carry phone / email / transcript / raw_payload / secret /
    # signature / env_values / callback_notes / dedupe_key /
    # raw_audit_metadata / merkle_proof / merkle_leaf_text.
    "audit.window_chain.generated",
    "audit.window_chain.verified",
    "audit.window_chain.broken",
    "audit.verification_run.persisted",
    "tenant.audit.dashboard.viewed",
    "tenant.audit.chain_status.viewed",

    # PAS179 — controlled learning + scenario simulation
    # architecture (locked-by-default). Payloads structural
    # only — see docs/pas179_controlled_learning_architecture.md.
    # NEVER carry phone / email / transcript / raw_payload /
    # raw_email / raw_body / secret / signature / env_values /
    # dedupe_key / rationale_text / rationale_freeform / name /
    # summary_text / callback_notes.
    "learning.policy.resolved",
    "learning.simulation.planned",
    "learning.simulation.completed",
    "learning.recommendation.generated",
    "learning.recommendation.rejected_by_guardrail",
    "learning.automatic_mode.blocked",

    # PAS180 — operator learning recommendation review surface.
    # Payloads structural only — see
    # docs/pas180_learning_recommendation_review.md. NEVER
    # carry phone / email / transcript / raw_payload / raw_email
    # / raw_body / secret / signature / env_values / dedupe_key
    # / rationale_text / prompt_text / live_mutation_payload.
    "learning.recommendation.reviewed",
    "learning.recommendation.approved_for_manual_test",
    "learning.recommendation.rejected",
    "learning.recommendation.expired",
    "tenant.learning.recommendation.viewed",

    # PAS181 — bounded manual-test execution harness
    # (simulation-only). Payloads structural only — see
    # docs/pas181_manual_test_execution_harness.md. NEVER
    # carry phone / email / transcript / raw_payload / raw_email
    # / raw_body / secret / signature / env_values / dedupe_key
    # / rationale_text / prompt_text / live_mutation_payload /
    # evidence_raw.
    "learning.manual_test.planned",
    "learning.manual_test.started",
    "learning.manual_test.completed",
    "learning.manual_test.failed",
    "learning.manual_test.cancelled",
    "tenant.learning.manual_test.viewed",

    # PAS-SECURITY-01 — defensive hardening audit events.
    # Payloads structural only — see
    # docs/pas_security_01_defensive_hardening_audit.md.
    # Allowed keys: route, surface, status, warning_count,
    # error_code, environment, auth_required,
    # signature_required. NEVER carry phone / email / name /
    # transcript / raw_payload / raw_email / raw_body / secret
    # / signature / token / api_key / env_values / stack_trace.
    "security.cors.audit_completed",
    "security.redirect.blocked",
    "security.webhook.unauthorized",
    "security.rate_limit.gap_detected",
    "security.error_safety.audit_completed",

    # PAS-SECURITY-02 — rate-limit / scanner / API-key
    # rotation events. Payloads structural only — see
    # docs/pas_security_02_rate_limit_scanner_key_rotation.md.
    # Allowed keys: brokerage_id, surface, actor_type,
    # actor_id (sha256 fingerprint, never raw IP / UA),
    # status, warning_count, error_code, scanner,
    # dependency_count, vulnerability_count, rotation_id.
    # NEVER carry raw IP / user-agent / API key / signature /
    # token / env_value / stack_trace / phone / email.
    "security.rate_limit.allowed",
    "security.rate_limit.blocked",
    "security.dependency_audit.completed",
    "security.dependency_audit.warning",
    "security.api_key_rotation.requested",
    "security.api_key_rotation.approved",
    "security.api_key_rotation.completed",
    "security.api_key_rotation.failed",

    # PAS-SECURITY-03 — admin/webhook rate-limit + atomic
    # counter RPC + CI scanner gate + API-key delivery
    # doctrine. Payloads structural only — see
    # docs/pas_security_03_admin_webhook_ci_gate.md. Allowed
    # keys: brokerage_id, surface, route, actor_type,
    # actor_id (sha256 fingerprint, never raw IP / UA),
    # status, warning_count, error_code, scanner,
    # vulnerability_count, severity, ci_mode, rpc_available.
    # NEVER carry raw IP / user-agent / API key / signature /
    # token / env_value / stack_trace / phone / email.
    "security.rate_limit.atomic_incremented",
    "security.rate_limit.rpc_unavailable",
    "security.admin.rate_limit_blocked",
    "security.webhook.rate_limit_blocked",
    "security.dependency_ci_gate.completed",
    "security.dependency_ci_gate.failed",
    "security.api_key_delivery.deferred",

    # PAS-SECURITY-04 — operator-route consolidation + one-time
    # API-key reveal + severity-aware CI gate + HTTPS
    # enforcement. Payloads structural only — see
    # docs/pas_security_04_operator_reveal_https.md. Allowed
    # keys: brokerage_id, route, actor_type, actor_id (sha256
    # fingerprint, never raw IP / UA / key), status,
    # warning_count, error_code, rotation_id, severity,
    # vulnerability_count, threshold, environment. NEVER carry
    # raw IP / user-agent / API key / signature / token /
    # reveal_token / env_value / stack_trace / phone / email /
    # raw_headers.
    "security.operator.auth_failed",
    "security.operator.rate_limit_blocked",
    "security.api_key_reveal.created",
    "security.api_key_reveal.succeeded",
    "security.api_key_reveal.failed",
    "security.dependency_ci_gate.severity_blocked",
    "security.https.insecure_request_blocked",

    # PAS182 — adaptive memory bridge from completed manual-test
    # runs into PAS163 memory CANDIDATES only. Payloads structural
    # only — see docs/pas182_adaptive_memory_bridge.md. Allowed
    # keys: brokerage_id, recommendation_id, test_run_id,
    # memory_candidate_id, status, risk_score, confidence_score,
    # warning_count, error_code, actor_type, actor_id. NEVER carry
    # phone / email / transcript / raw_payload / raw_email /
    # raw_body / secret / signature / env_values / dedupe_key /
    # rationale_text / prompt_text / evidence_raw /
    # live_mutation_payload.
    "learning.adaptive_memory.bridge_confirmed",
    "learning.adaptive_memory.candidate_created",
    "learning.adaptive_memory.bridge_rejected",
    "tenant.learning.adaptive_memory.viewed",

    # PAS187 — fleet observability + two-person cutover
    # discipline + daily ops checklist. Allowed payload
    # keys: brokerage_id, cutover_id, checklist_run_id,
    # status, target_stage, actor_type, actor_id,
    # warning_count, incident_count, action_required,
    # error_code. NEVER carry phone / email / name /
    # raw_payload / raw_email / raw_body / transcript /
    # secret / signature / token / api_key / env_values /
    # stack_trace.
    "fleet.status.generated",
    "fleet.rollout_readiness.generated",
    "cutover.requested",
    "cutover.first_approved",
    "cutover.second_approved",
    "cutover.rejected",
    "daily_ops.checklist.completed",
    "daily_ops.checklist.failed",

    # PAS188 — operational scaling automation. Allowed
    # payload keys: brokerage_id, incident_id, breaker_id,
    # severity, status, reason_code, resolution_code,
    # actor_type, actor_id, warning_count, incident_count,
    # action_required, error_code. NEVER carry phone /
    # email / name / raw_payload / raw_email / raw_body /
    # transcript / secret / signature / token / api_key /
    # env_values / stack_trace.
    "incident.opened",
    "incident.status_changed",
    "incident.resolved",
    "circuit_breaker.tripped",
    "circuit_breaker.reset",

    # PAS189 — operational wire-through + tenant incident
    # visibility. Allowed payload keys: brokerage_id,
    # incident_id, status, warning_count, error_code,
    # route, run_count, dry_run, action_required. NEVER
    # carry phone / email / name / raw_payload /
    # raw_email / raw_body / transcript / secret /
    # signature / token / api_key / env_values /
    # stack_trace / operator_notes.
    "circuit_breaker.outbound_blocked",
    "fleet.cache.invalidated",
    "daily_ops.runner.watch_started",
    "daily_ops.runner.watch_completed",
    "tenant.incident.viewed",

    # PAS190 — final operational wire-through polish.
    # Allowed payload keys: brokerage_id, status,
    # warning_count, error_code, route, run_count,
    # notification_attempted, filter_count,
    # action_required. NEVER carry phone / email / name /
    # raw_payload / raw_email / raw_body / transcript /
    # secret / signature / token / api_key / env_values /
    # stack_trace / operator_notes / webhook_url.
    "circuit_breaker.outbound_dial_blocked",
    "fleet.cache.row_invalidated",
    "daily_ops.runner.slack_notify_attempted",
    "tenant.incident.filtered_viewed",
    "operator.policy_report.generated",

    # PAS191 — bounded Slack natural-language operator
    # commands. Deterministic alias table → closed intent
    # code → safe formatter. NO LLM, NO mutation, NO PII.
    # Allowed payload keys: brokerage_id, intent, surface.
    # NEVER carry phone / email / name / raw_payload /
    # raw_email / raw_body / transcript / secret / signature /
    # token / api_key / env_values / stack_trace /
    # operator_notes / webhook_url / prompt_text.
    "slack.intent.matched",
    "slack.intent.unknown",
})


# ── ACTORS ──────────────────────────────────────────────────────────
# Who took the action that produced the event. Distinct from
# event_source (which is "where in the codebase" — kept for legacy
# observability) and from provider (which is the third-party vendor).

ALLOWED_ACTORS: FrozenSet[str] = frozenset({
    "lead",      # the inbound caller / outbound lead
    "pas",       # the PAS engine itself (LLM, state machine, prompt)
    "system",    # call_logger, lead_memory, scheduler — non-PAS infra
    "broker",    # human action via portal / Slack / admin
    "provider",  # external vendor signal (Twilio status, Cal.com webhook)
})


# ── WORKFLOW STAGES ─────────────────────────────────────────────────
# Mirror the keys produced by app/services/workflows/mapper.py so the
# new pas_events.workflow_stage column aligns with the existing
# dashboard skeleton without any consumer changes. Adding a new stage
# here is a contract change — update mapper.py in the same PR.

ALLOWED_WORKFLOW_STAGES: FrozenSet[str] = frozenset({
    "lead_received",
    "pas_calling",
    "intent_captured",
    "budget_captured",
    "timeline_captured",
    "objection_handling",  # not a mapper.py step today; reserved for PAS141
    "booking_attempted",
    "booking_confirmed",
    "callback_requested",
    "followup_scheduled",
    "completed",
})


# ── SOURCES ─────────────────────────────────────────────────────────
# Origin of the traffic that produced the event. Critical for keeping
# replay / simulated / production traffic separable in any future
# training dataset.

ALLOWED_SOURCES: FrozenSet[str] = frozenset({
    # Traffic-origin sources — describe where the conversation came from.
    "voice",      # live Twilio inbound or outbound call
    "simulated",  # /simulate-call HTTP endpoint
    "replay",     # PAS142 evaluation framework re-runs (future)
    "imported",   # offline import of historical / partner data
    "manual",     # broker- or admin-issued manual entry
    # Subsystem sources — for events that have no traffic origin
    # (provider failures during background work, ops errors, etc.).
    # Added in PAS140B because provider.failed and system.error
    # events can fire without an attached call/lead.
    "llm",            # LLM-provider failures (claude_client, summary, slack, training)
    "ops",            # operational subsystem errors (error_store mirror)
    # PAS144H — runtime memory-injection observability events
    # (memory.injection.{skipped,attempted,succeeded,failed}).
    "memory_runtime",
})
