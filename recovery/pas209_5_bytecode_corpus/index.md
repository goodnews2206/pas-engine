# PAS209.5 Bytecode Recovery Corpus — Index

Durable text artifacts extracted from **source-less** `.pyc` bytecode (CPython 3.14) — the only surviving residue of the lost PAS160–190 work.

This is a **reconstruction specification, not restored source code.** No decompilation was performed (no CPython-3.14 decompiler exists); artifacts are produced via stdlib `marshal` + `dis` only.

**Modules captured:** 216  |  **Redacted modules:** 22  |  **Redactions:** 22

| Subsystem | Modules |
|---|---|
| ingestion | 15 |
| memory | 28 |
| security | 12 |
| operator | 18 |
| learning | 13 |
| monitoring | 6 |
| optimization | 7 |
| replay | 4 |
| tenant | 5 |
| callbacks | 3 |
| worker | 3 |
| outbound | 2 |
| brokerage | 4 |
| simulation | 2 |
| slack | 1 |
| routes | 16 |
| scripts_readiness | 77 |
| **TOTAL** | **216** |

## ingestion

- [`__init__`](ingestion/__init__.md) — PAS161 — Lead ingestion subsystem.
- [`contracts`](ingestion/contracts.md) — PAS161 — Canonical normalized lead contract.
- [`email_auth`](ingestion/email_auth.md) — PAS165 — Email forwarder signature verification.
- [`email_dedupe`](ingestion/email_dedupe.md) — PAS165 — Email lead deduplication (process-local v1).
- [`email_dedupe_store`](ingestion/email_dedupe_store.md) — PAS166 — Durable email dedupe store (Supabase-backed v1).
- [`email_forwarder_secret_store`](ingestion/email_forwarder_secret_store.md) — PAS167 / PAS168 — Email forwarder secret store.
- [`email_ingestion`](ingestion/email_ingestion.md) — PAS164 / PAS165 / PAS166 — Email lead ingestion service.
- [`email_parser`](ingestion/email_parser.md) — PAS164 — Email lead parser.
- [`normalizers`](ingestion/normalizers.md) — PAS161 — Provider-specific normalizers.
- [`pending_call_dedupe`](ingestion/pending_call_dedupe.md) — PAS170 — Pending-call dedupe (process-local v1).
- [`pending_call_dedupe_store`](ingestion/pending_call_dedupe_store.md) — PAS171 — Durable pending-call dedupe store (Supabase-backed v1).
- [`pending_call_recovery`](ingestion/pending_call_recovery.md) — PAS170 — Pending-call queue visibility + stale DIALING
- [`pending_calls`](ingestion/pending_calls.md) — PAS161 — Pending-call durability layer (process-local v1).
- [`security`](ingestion/security.md) — PAS161 — Webhook security helpers.
- [`worker`](ingestion/worker.md) — PAS162 — Pending-call auto-dial worker.

## memory

- [`__init__`](memory/__init__.md) — PAS144A — Operational Memory module.
- [`approval`](memory/approval.md) — PAS144L — Signed Operator Approval + Safe Apply Adapter.
- [`audit`](memory/audit.md) — PAS144C — Memory review audit helpers (pure).
- [`batch_rollout`](memory/batch_rollout.md) — PAS144N — Batch rollout planner (pure).
- [`candidate_pipeline`](memory/candidate_pipeline.md) — PAS163 — Memory candidate pipeline.
- [`classifier`](memory/classifier.md) — PAS144A — Deterministic memory classifiers.
- [`contracts`](memory/contracts.md) — PAS144A — Operational Memory Contracts.
- [`diagnostics`](memory/diagnostics.md) — PAS144I — Memory-injection runtime diagnostics.
- [`formatter`](memory/formatter.md) — PAS144F — Memory → prompt formatter.
- [`governance`](memory/governance.md) — PAS144A — Memory governance.
- [`impact`](memory/impact.md) — PAS144J — Memory-injection impact correlation + rollout guardrails.
- [`injection`](memory/injection.md) — PAS144F — Operator-gated runtime memory injection.
- [`manifest_store`](memory/manifest_store.md) — PAS144N — Signed manifest persistence.
- [`operator_console`](memory/operator_console.md) — PAS147 — Operator memory review console.
- [`portal_visibility`](memory/portal_visibility.md) — PAS146 — Portal-side PAS Brain visibility composer.
- [`queries`](memory/queries.md) — PAS144B — Tenant-scoped memory read helpers.
- [`queue`](memory/queue.md) — PAS144D — Memory review / expiration queue surfaces.
- [`ranking`](memory/ranking.md) — PAS144E — Deterministic memory ranking.
- [`retrieval`](memory/retrieval.md) — PAS144E — Controlled active-memory retrieval.
- [`review`](memory/review.md) — PAS144C — Memory review + promotion workflow.
- [`review_actors`](memory/review_actors.md) — PAS154 — Memory review actor catalog (read-only, structural).
- [`review_alerts`](memory/review_alerts.md) — PAS155 — Memory review operator drift alerts (read-only, structural).
- [`review_export`](memory/review_export.md) — PAS152 — Memory review CSV export (read-only, structural).
- [`review_stats`](memory/review_stats.md) — PAS150 — Memory review stats (read-only, structural).
- [`rollout`](memory/rollout.md) — PAS144K — Operator-approved memory-rollout controller.
- [`rollout_ledger`](memory/rollout_ledger.md) — PAS144M — Memory Rollout Ledger.
- [`store`](memory/store.md) — PAS144B — Tenant-isolated memory store.
- [`sweeper`](memory/sweeper.md) — PAS144D — Memory expiration sweep.

## security

- [`__init__`](security/__init__.md) — PAS-SECURITY-01 — Defensive hardening helpers (additive).
- [`api_key_reveal`](security/api_key_reveal.md) — PAS-SECURITY-04 — One-time API-key reveal service.
- [`api_key_rotation`](security/api_key_rotation.md) — PAS-SECURITY-02 — Tenant-initiated / operator-approved API-key
- [`cors_policy`](security/cors_policy.md) — PAS-SECURITY-01 — CORS policy validators (additive).
- [`dependency_scanner`](security/dependency_scanner.md) — PAS-SECURITY-02 — Report-only dependency scanner.
- [`error_safety`](security/error_safety.md) — PAS-SECURITY-01 — Public-response error-safety helpers.
- [`https_enforcement`](security/https_enforcement.md) — PAS-SECURITY-04 — App-layer HTTPS enforcement helper.
- [`operator_auth`](security/operator_auth.md) — PAS-SECURITY-04 — Consolidated operator/admin auth + rate-limit
- [`rate_limit`](security/rate_limit.md) — PAS-SECURITY-02 — Per-tenant / per-surface rate limit service.
- [`rate_limit_rpc`](security/rate_limit_rpc.md) — PAS-SECURITY-03 — Atomic rate-limit RPC service.
- [`rate_limit_store`](security/rate_limit_store.md) — PAS-SECURITY-02 — Rate-limit counter store (DB-backed + fallback).
- [`redirect_validation`](security/redirect_validation.md) — PAS-SECURITY-01 — Redirect-target allow-list guard (additive).

## operator

- [`__init__`](operator/__init__.md) — PAS173 — operator-actions package.
- [`audit_chain_verifier`](operator/audit_chain_verifier.md) — PAS176 — Audit chain verifier + Merkle root computation.
- [`audit_integrity`](operator/audit_integrity.md) — PAS175 — Operator audit log integrity service.
- [`audit_service`](operator/audit_service.md) — PAS174 — Operator action audit service (Supabase-backed v1).
- [`audit_verification_runs`](operator/audit_verification_runs.md) — PAS178 — Durable audit verification run persistence.
- [`audit_window_chain`](operator/audit_window_chain.md) — PAS178 — Cross-window Merkle chain service.
- [`cache_invalidation`](operator/cache_invalidation.md) — PAS189 — Operator-only fleet-status cache invalidation
- [`circuit_breaker`](operator/circuit_breaker.md) — PAS188 — Per-brokerage circuit-breaker service.
- [`circuit_breaker_policy`](operator/circuit_breaker_policy.md) — PAS189 — Circuit-breaker policy (advisory read-through).
- [`connectivity_probes`](operator/connectivity_probes.md) — PAS174 — Connectivity probes (DRY-RUN ONLY).
- [`cutover_approval`](operator/cutover_approval.md) — PAS187 — Two-person cutover approval service.
- [`daily_ops_checklist`](operator/daily_ops_checklist.md) — PAS187 — Daily operator checklist runner (durable record).
- [`fleet_status`](operator/fleet_status.md) — PAS187 — Fleet observability aggregator (read-only).
- [`fleet_status_cache`](operator/fleet_status_cache.md) — PAS188 — Fleet-status TTL cache (in-process, read-only).
- [`incident_log`](operator/incident_log.md) — PAS188 — Structured incident log (operator-opened only,
- [`merkle_inclusion_proofs`](operator/merkle_inclusion_proofs.md) — PAS177 — Merkle inclusion proof generation + verification.
- [`operator_actions`](operator/operator_actions.md) — PAS173 — Operator action dispatcher (closed allow-list).
- [`operator_policy_report`](operator/operator_policy_report.md) — PAS190 — Operator policy report (read-only roll-up).

## learning

- [`__init__`](learning/__init__.md) — PAS179 — Controlled learning architecture (locked-by-default).
- [`adaptive_memory_bridge`](learning/adaptive_memory_bridge.md) — PAS182 — Adaptive memory bridge.
- [`adaptive_memory_projection`](learning/adaptive_memory_projection.md) — PAS182 — Safe projections for adaptive-memory bridge envelopes.
- [`guardrails`](learning/guardrails.md) — PAS179 — Controlled learning guardrails.
- [`learning_policy`](learning/learning_policy.md) — PAS179 — Manual / automatic learning-mode policy.
- [`manual_test_evidence`](learning/manual_test_evidence.md) — PAS181 — Bounded evidence packets for manual-test runs.
- [`manual_test_harness`](learning/manual_test_harness.md) — PAS181 — Bounded manual-test execution harness.
- [`manual_test_scoring`](learning/manual_test_scoring.md) — PAS181 — Deterministic manual-test scoring.
- [`outcome_feedback`](learning/outcome_feedback.md) — PAS179 — Bounded outcome feedback contract.
- [`recommendation_engine`](learning/recommendation_engine.md) — PAS179 — Learning recommendation engine (CANDIDATE-only).
- [`recommendation_projection`](learning/recommendation_projection.md) — PAS180 — Safe projections for learning recommendation records.
- [`recommendation_review`](learning/recommendation_review.md) — PAS180 — Operator learning recommendation review service.
- [`scenario_contracts`](learning/scenario_contracts.md) — PAS179 — Deterministic scenario contracts.

## monitoring

- [`__init__`](monitoring/__init__.md) — PAS143F1 — Monitoring contracts package.
- [`contracts`](monitoring/contracts.md) — PAS143F1 — Monitoring alert contracts.
- [`detectors`](monitoring/detectors.md) — PAS143F2 — Deterministic monitoring detectors.
- [`dispatcher`](monitoring/dispatcher.md) — PAS143F2 — Monitoring dispatcher.
- [`report`](monitoring/report.md) — PAS143F2 — Monitoring report aggregation.
- [`slack_alert_transport`](monitoring/slack_alert_transport.md) — PAS170 — Slack alert transport (optional, structural).

## optimization

- [`__init__`](optimization/__init__.md) — PAS143A — Comparative optimization framework.
- [`matrix_runner`](optimization/matrix_runner.md) — PAS143A — Scenario × Strategy matrix runner.
- [`metrics`](optimization/metrics.md) — PAS143A — Pure aggregation over a matrix of scenario × strategy results.
- [`ranking`](optimization/ranking.md) — PAS143A — Deterministic strategy ranking.
- [`recommendations`](optimization/recommendations.md) — PAS143C — Optimization recommendation layer.
- [`report`](optimization/report.md) — PAS143A — One-shot optimization report.
- [`strategies`](optimization/strategies.md) — PAS143A — Strategy variant registry.

## replay

- [`__init__`](replay/__init__.md) — PAS141 — Replay + Evaluation scaffold.
- [`evaluator`](replay/evaluator.md) — PAS141 — Deterministic evaluation of a reconstructed call.
- [`event_reader`](replay/event_reader.md) — PAS141 — Read + normalize pas_events rows for replay.
- [`reconstruction`](replay/reconstruction.md) — PAS141 — Conversation + lifecycle reconstruction from normalized events.

## tenant

- [`__init__`](tenant/__init__.md) — PAS174 — tenant visibility package.
- [`tenant_audit_ack_store`](tenant/tenant_audit_ack_store.md) — PAS177 — Durable tenant audit acknowledgement store (Supabase-backed v1).
- [`tenant_audit_dashboard`](tenant/tenant_audit_dashboard.md) — PAS178 — Tenant audit dashboard service.
- [`tenant_incident_projection`](tenant/tenant_incident_projection.md) — PAS189 — Tenant-facing incident projection (safe read-only).
- [`tenant_visibility_service`](tenant/tenant_visibility_service.md) — PAS174 — Tenant visibility service.

## callbacks

- [`__init__`](callbacks/__init__.md) — PAS170 — Callback lifecycle minimum surface.
- [`callback_schedule`](callbacks/callback_schedule.md) — PAS170 — Callback schedule service (process-local v1).
- [`callback_schedule_store`](callbacks/callback_schedule_store.md) — PAS171 — Durable callback-schedule store (Supabase-backed v1).

## worker

- [`__init__`](worker/__init__.md) — PAS172 — worker package.
- [`heartbeat_monitor`](worker/heartbeat_monitor.md) — PAS172 — Worker heartbeat monitor (read-only).
- [`heartbeat_service`](worker/heartbeat_service.md) — PAS172 — Worker heartbeat service (Supabase-backed v1).

## outbound

- [`__init__`](outbound/__init__.md) — PAS163 — Outbound dial adapter package.
- [`dial`](outbound/dial.md) — PAS163 — Outbound dial adapter.

## brokerage

- [`__init__`](brokerage/__init__.md) — PAS173 — brokerage operator-system package.
- [`config_validator`](brokerage/config_validator.md) — PAS173 — Brokerage configuration validator.
- [`onboarding_templates`](brokerage/onboarding_templates.md) — PAS173 — Brokerage onboarding templates (deterministic).
- [`profile_service`](brokerage/profile_service.md) — PAS173 — Brokerage profile service (Supabase-backed v1).

## simulation

- [`behavior`](simulation/behavior.md) — PAS143B — Behavioral divergence layer.
- [`runner`](simulation/runner.md) — PAS142 — Scenario runner.

## slack

- [`employee_mode`](slack/employee_mode.md) — PAS172 — Slack Employee Mode v1 (OPS-ONLY block builders).

## routes

- [`email_ingestion`](routes/email_ingestion.md) — PAS164/PAS165 — Email lead ingestion routes.
- [`lead_ingestion`](routes/lead_ingestion.md) — PAS161 — Lead ingestion webhook routes.
- [`operator_adaptive_memory`](routes/operator_adaptive_memory.md) — PAS182 — Operator adaptive-memory bridge routes.
- [`operator_brokerages`](routes/operator_brokerages.md) — PAS173 — Multi-brokerage operator routes.
- [`operator_fleet`](routes/operator_fleet.md) — PAS187 — Operator fleet observability + two-person cutover
- [`operator_incidents`](routes/operator_incidents.md) — PAS188 — Operator incidents + circuit-breaker routes
- [`operator_learning`](routes/operator_learning.md) — PAS180 — Operator learning recommendation review routes.
- [`operator_learning_dashboard`](routes/operator_learning_dashboard.md) — PAS184 — Operator learning unified dashboard (read-only).
- [`operator_learning_tests`](routes/operator_learning_tests.md) — PAS181 — Operator manual-test routes.
- [`operator_ops`](routes/operator_ops.md) — PAS172 — Operator Ops routes.
- [`security_api_key_rotation`](routes/security_api_key_rotation.md) — PAS-SECURITY-02 — API-key rotation routes.
- [`tenant_adaptive_memory`](routes/tenant_adaptive_memory.md) — PAS182 — Tenant adaptive-memory bridge-status route.
- [`tenant_incidents`](routes/tenant_incidents.md) — PAS189 — Tenant-facing incident routes (read-only).
- [`tenant_learning`](routes/tenant_learning.md) — PAS180 — Tenant-safe learning recommendation visibility routes.
- [`tenant_learning_tests`](routes/tenant_learning_tests.md) — PAS181 — Tenant-safe manual-test visibility routes.
- [`tenant_portal`](routes/tenant_portal.md) — PAS174 — Tenant visibility routes.

## scripts_readiness

- [`apply_memory_rollout_plan`](scripts_readiness/apply_memory_rollout_plan.md) — PAS144L — Apply Memory Rollout Plan CLI.
- [`backfill_operator_audit_hashes`](scripts_readiness/backfill_operator_audit_hashes.md) — PAS176 — Pre-v23 audit-row hash backfill (operator-driven).
- [`backup_database`](scripts_readiness/backup_database.md) — PAS143D — Operator-initiated PostgreSQL backup wrapper.
- [`export_events`](scripts_readiness/export_events.md) — PAS143D — Export pas_events to newline-delimited JSON.
- [`generate_audit_inclusion_proof`](scripts_readiness/generate_audit_inclusion_proof.md) — PAS177 — Operator-runnable audit-entry inclusion proof CLI.
- [`inspect_backup_archive`](scripts_readiness/inspect_backup_archive.md) — PAS143G — Offline archive inspection.
- [`integrity_check`](scripts_readiness/integrity_check.md) — PAS143E — Offline integrity checker.
- [`memory_batch_rollout_plan`](scripts_readiness/memory_batch_rollout_plan.md) — PAS144N — Batch rollout planner CLI.
- [`memory_diagnostics`](scripts_readiness/memory_diagnostics.md) — PAS144I — Memory-injection diagnostics CLI.
- [`memory_expiration_sweep`](scripts_readiness/memory_expiration_sweep.md) — PAS144D — Memory expiration sweep CLI.
- [`memory_impact_report`](scripts_readiness/memory_impact_report.md) — PAS144J — Memory-injection impact report CLI.
- [`memory_rollout_history`](scripts_readiness/memory_rollout_history.md) — PAS144M — Memory Rollout History CLI.
- [`memory_rollout_plan`](scripts_readiness/memory_rollout_plan.md) — PAS144K — Operator-approved memory-rollout planner CLI.
- [`package_backup`](scripts_readiness/package_backup.md) — PAS143G — Encrypted offsite backup packaging.
- [`pas145_mvp_readiness_check`](scripts_readiness/pas145_mvp_readiness_check.md) — PAS145 — MVP operator readiness gate.
- [`pas158_memory_review_readiness_check`](scripts_readiness/pas158_memory_review_readiness_check.md) — PAS158 — Memory Review subsystem readiness gate.
- [`pas160_mvp_sequence_check`](scripts_readiness/pas160_mvp_sequence_check.md) — PAS160 — Production MVP doctrine + sequence lock gate.
- [`pas161_lead_ingestion_readiness_check`](scripts_readiness/pas161_lead_ingestion_readiness_check.md) — PAS161 — Lead ingestion readiness gate.
- [`pas162_pending_calls_readiness_check`](scripts_readiness/pas162_pending_calls_readiness_check.md) — PAS162 — Durable pending-calls + auto-dial worker readiness gate.
- [`pas163_candidate_pipeline_readiness_check`](scripts_readiness/pas163_candidate_pipeline_readiness_check.md) — PAS163 — Outbound dial + memory candidate pipeline readiness gate.
- [`pas164_email_ingestion_readiness_check`](scripts_readiness/pas164_email_ingestion_readiness_check.md) — PAS164 — Email lead ingestion readiness gate.
- [`pas165_email_auth_dedupe_readiness_check`](scripts_readiness/pas165_email_auth_dedupe_readiness_check.md) — PAS165 — Email forwarder authentication + dedupe readiness gate.
- [`pas166_email_dedupe_policy_readiness_check`](scripts_readiness/pas166_email_dedupe_policy_readiness_check.md) — PAS166 — Durable email dedupe + signature-required policy
- [`pas167_email_secret_reaper_readiness_check`](scripts_readiness/pas167_email_secret_reaper_readiness_check.md) — PAS167 — Email forwarder secret-at-rest encryption + dedupe
- [`pas168_email_secret_rotation_readiness_check`](scripts_readiness/pas168_email_secret_rotation_readiness_check.md) — PAS168 — Real crypto dependency + operator secret rotation
- [`pas169_crypto_roundtrip_check`](scripts_readiness/pas169_crypto_roundtrip_check.md) — PAS169 — Crypto roundtrip checker.
- [`pas169_launch_readiness_check`](scripts_readiness/pas169_launch_readiness_check.md) — PAS169 — Launch readiness gate.
- [`pas170_demo_brokerage_smoke_plan`](scripts_readiness/pas170_demo_brokerage_smoke_plan.md) — PAS170 — Demo brokerage smoke plan generator.
- [`pas170_operator_survival_readiness_check`](scripts_readiness/pas170_operator_survival_readiness_check.md) — PAS170 — Operator survival kit readiness gate.
- [`pas171_external_pilot_readiness_check`](scripts_readiness/pas171_external_pilot_readiness_check.md) — PAS171 — External pilot readiness gate.
- [`pas172_pilot_operations_readiness_check`](scripts_readiness/pas172_pilot_operations_readiness_check.md) — PAS172 — Pilot operations readiness gate.
- [`pas173_brokerage_operator_readiness_check`](scripts_readiness/pas173_brokerage_operator_readiness_check.md) — PAS173 — Brokerage operator system readiness gate.
- [`pas174_operator_audit_readiness_check`](scripts_readiness/pas174_operator_audit_readiness_check.md) — PAS174 — Operator audit layer + tenant visibility readiness gate.
- [`pas175_audit_integrity_readiness_check`](scripts_readiness/pas175_audit_integrity_readiness_check.md) — PAS175 — Audit integrity + tenant audit visibility readiness gate.
- [`pas176_audit_chain_readiness_check`](scripts_readiness/pas176_audit_chain_readiness_check.md) — PAS176 — Audit chain verification + tenant acknowledgement readiness gate.
- [`pas177_tenant_audit_verification_readiness_check`](scripts_readiness/pas177_tenant_audit_verification_readiness_check.md) — PAS177 — Durable tenant ACK + Merkle inclusion proofs readiness gate.
- [`pas178_audit_window_chain_readiness_check`](scripts_readiness/pas178_audit_window_chain_readiness_check.md) — PAS178 — Cross-window audit chain + verification persistence readiness gate.
- [`pas179_controlled_learning_readiness_check`](scripts_readiness/pas179_controlled_learning_readiness_check.md) — PAS179 — Controlled learning architecture readiness gate.
- [`pas180_learning_review_readiness_check`](scripts_readiness/pas180_learning_review_readiness_check.md) — PAS180 — Operator learning recommendation review readiness gate.
- [`pas181_manual_test_harness_readiness_check`](scripts_readiness/pas181_manual_test_harness_readiness_check.md) — PAS181 — Bounded manual-test execution harness readiness gate.
- [`pas182_adaptive_memory_bridge_readiness_check`](scripts_readiness/pas182_adaptive_memory_bridge_readiness_check.md) — PAS182 — Adaptive memory bridge readiness gate.
- [`pas183_onboarding_product_readiness_check`](scripts_readiness/pas183_onboarding_product_readiness_check.md) — PAS183 — Onboarding + product experience readiness gate.
- [`pas184_pilot_experience_readiness_check`](scripts_readiness/pas184_pilot_experience_readiness_check.md) — PAS184 — Pilot experience polish readiness gate.
- [`pas186_final_cutover_readiness_check`](scripts_readiness/pas186_final_cutover_readiness_check.md) — PAS186 — Final pilot cutover readiness gate.
- [`pas187_fleet_cutover_readiness_check`](scripts_readiness/pas187_fleet_cutover_readiness_check.md) — PAS187 — Fleet observability + two-person cutover discipline
- [`pas188_operational_scaling_readiness_check`](scripts_readiness/pas188_operational_scaling_readiness_check.md) — PAS188 — Operational scaling automation readiness gate.
- [`pas189_operational_wirethrough_readiness_check`](scripts_readiness/pas189_operational_wirethrough_readiness_check.md) — PAS189 — Operational wire-through readiness gate.
- [`pas190_final_wirethrough_readiness_check`](scripts_readiness/pas190_final_wirethrough_readiness_check.md) — PAS190 — Final operational wire-through polish readiness gate.
- [`pas_launch_integrity_check`](scripts_readiness/pas_launch_integrity_check.md) — PAS-LAUNCH-01 — Final deployment integrity gate.
- [`pas_security_01_hardening_readiness_check`](scripts_readiness/pas_security_01_hardening_readiness_check.md) — PAS-SECURITY-01 — Defensive hardening readiness gate.
- [`pas_security_02_rate_limit_scanner_readiness_check`](scripts_readiness/pas_security_02_rate_limit_scanner_readiness_check.md) — PAS-SECURITY-02 — Rate-limit + scanner + key-rotation readiness gate.
- [`pas_security_03_admin_webhook_ci_readiness_check`](scripts_readiness/pas_security_03_admin_webhook_ci_readiness_check.md) — PAS-SECURITY-03 — Admin / webhook rate-limit + atomic counter
- [`pas_security_04_operator_reveal_https_readiness_check`](scripts_readiness/pas_security_04_operator_reveal_https_readiness_check.md) — PAS-SECURITY-04 — Operator route consolidation + one-time
- [`persist_audit_verification_run`](scripts_readiness/persist_audit_verification_run.md) — PAS178 — Operator-runnable verification-run persistence CLI.
- [`pre_pas144_readiness_check`](scripts_readiness/pre_pas144_readiness_check.md) — PAS143I — Pre-PAS144 operator readiness gate.
- [`reap_callback_schedule`](scripts_readiness/reap_callback_schedule.md) — PAS172 — Operator reaper for the PAS171 callback schedule
- [`reap_email_dedupe`](scripts_readiness/reap_email_dedupe.md) — PAS167 — Email dedupe reaper (operator-only).
- [`reap_operator_audit_log`](scripts_readiness/reap_operator_audit_log.md) — PAS175 — Operator-driven audit-log retention reaper.
- [`reap_pending_call_dedupe`](scripts_readiness/reap_pending_call_dedupe.md) — PAS172 — Operator reaper for the PAS171 pending-call dedupe
- [`replay_call`](scripts_readiness/replay_call.md) — PAS141 — CLI: replay one call from pas_events.
- [`restore_drill`](scripts_readiness/restore_drill.md) — PAS143G — Restore drill runner.
- [`rotate_email_forwarder_secret`](scripts_readiness/rotate_email_forwarder_secret.md) — PAS168 — Email forwarder secret rotation (operator-only).
- [`run_daily_ops_checklist_report`](scripts_readiness/run_daily_ops_checklist_report.md) — PAS188 — Operator-run daily ops checklist report runner.
- [`run_migration_promotion_checklist`](scripts_readiness/run_migration_promotion_checklist.md) — PAS188 — Operator-run migration-promotion checklist
- [`run_monitoring_check`](scripts_readiness/run_monitoring_check.md) — PAS143F2 — Monitoring CLI.
- [`run_optimization`](scripts_readiness/run_optimization.md) — PAS143A — CLI: run the strategy × scenario matrix and report rankings.
- [`run_pending_calls_worker`](scripts_readiness/run_pending_calls_worker.md) — PAS162 — Pending-call worker CLI.
- [`run_simulations`](scripts_readiness/run_simulations.md) — PAS142 — CLI: run PAS simulation scenarios in-process.
- [`scheduled_audit_verification_template`](scripts_readiness/scheduled_audit_verification_template.md) — PAS177 — Scheduled audit verification operator template.
- [`security_audit`](scripts_readiness/security_audit.md) — PAS143E — Static security & integrity audit scanner.
- [`security_ci_dependency_gate`](scripts_readiness/security_ci_dependency_gate.md) — PAS-SECURITY-03 — CI dependency scanner gate.
- [`security_dependency_audit`](scripts_readiness/security_dependency_audit.md) — PAS-SECURITY-02 — Operator-runnable dependency audit CLI.
- [`seed_demo_brokerage`](scripts_readiness/seed_demo_brokerage.md) — PAS138A — Seed: demo brokerage (Python, idempotent).
- [`seed_memory_candidate_demo`](scripts_readiness/seed_memory_candidate_demo.md) — PAS163 — Memory candidate demo seed.
- [`verify_audit_window_chain`](scripts_readiness/verify_audit_window_chain.md) — PAS178 — Operator-runnable cross-window chain verifier CLI.
- [`verify_backup`](scripts_readiness/verify_backup.md) — PAS143D — Verify a backup directory before trusting it.
- [`verify_operator_audit_chain`](scripts_readiness/verify_operator_audit_chain.md) — PAS176 — Operator-runnable audit chain verifier CLI.
