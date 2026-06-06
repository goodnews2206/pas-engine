# scripts_readiness/pas179_controlled_learning_readiness_check

- **pyc:** `scripts\__pycache__\pas179_controlled_learning_readiness_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/pas179_controlled_learning_readiness_check.py`
- **co_filename (from bytecode):** `scripts/pas179_controlled_learning_readiness_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS179 — Controlled learning architecture readiness gate.

Deterministic, non-mutating evaluator for "is PAS179 wired
correctly and free of regressions in the PAS160-PAS178
doctrine?".

Walks the repo and verifies:

  * PAS160-PAS178 readiness scripts still exist.
  * PAS179 surfaces exist:
      - scripts/migrate_v28_learning_recommendations.sql
      - scripts/migrate_v29_simulation_runs.sql
      - app/services/learning/learning_policy.py
      - app/services/learning/scenario_contracts.py
      - app/services/learning/outcome_feedback.py
      - app/services/learning/recommendation_engine.py
      - app/services/learning/guardrails.py
      - scripts/pas179_controlled_learning_readiness_check.py
      - docs/pas179_controlled_learning_architecture.md
      - tests/mvp/test_pas179_controlled_learning_architecture.py
  * v28 SQL carries PROPOSAL ONLY + DO NOT EXECUTE + closed
    recommendation_type + status enums + RLS tenant SELECT
    scoped + tenant INSERT/UPDATE/DELETE denied + service_role
    INSERT CANDIDATE-only + restricted operator UPDATE gated
    to CANDIDATE → terminal transitions + no DELETE.
  * v29 SQL carries PROPOSAL ONLY + DO NOT EXECUTE + closed
    scenario_type + mode + status enums + RLS tenant SELECT
    scoped + tenant INSERT/UPDATE/DELETE denied + service_role
    INSERT-only + no UPDATE / no DELETE policies + fingerprint
    sha256 hex CHECK pins.
  * Default learning mode is MANUAL.
  * Automatic mode is structurally represented but blocked.
  * No auto-approval helper in any PAS179 source file.
  * No live mutation imports (outbound FSM, memory review,
    booking, slack core, worker, audit_service).
  * No LLM calls (no anthropic / openai imports).
  * No embeddings / vector DB / Gmail / OAuth / IMAP / POP3 /
    inbox-scanning / Composio / TrustClaw imports.
  * Memory Review (PAS147-PAS158) untouched.
  * audit_service.py STILL has no UPDATE / DELETE helpers
    (PAS174-PAS178 carry-forward).
  * Event contract registers every PAS179 event type.
  * Worker still OFF by default; FastAPI lifespan does not
    auto-start the worker.
  * Supports --summary-only / --json.
  * Exits 0 ready, 1 blockers, 2 bad args.
  * Never reads .env.
  * Never touches production data.
```

## Imports

`List`, `Optional`, `Path`, `__future__`, `annotations`, `argparse`, `datetime`, `json`, `os`, `pathlib`, `sys`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_aggregate`, `_build_parser`, `_check`, `_now_iso`, `_operator_actions`, `_print_summary`, `_read_text`, `_strip_python_comments_and_strings`, `_write_report`, `check_audit_service_invariant`, `check_doc_required_clauses`, `check_event_contract`, `check_files_present`, `check_guardrails`, `check_memory_review_intact`, `check_no_auto_approval_tokens`, `check_no_forbidden_imports`, `check_no_inbox_scan_tokens`, `check_no_live_mutation_imports`, `check_no_startup_worker`, `check_outcome_feedback`, `check_policy_service`, `check_prior_phases_intact`, `check_recommendation_engine`, `check_scenario_contracts`, `check_self_no_env_or_db`, `check_v28_sql`, `check_v29_sql`, `check_worker_off_by_default`, `evaluate`, `main`

## Env-key candidates

`BLOCK`, `FAIL`, `NOT_READY`, `PAS179`, `PASS`, `READY`

## String constants (redacted where noted)

- '\nPAS179 — Controlled learning architecture readiness gate.\n\nDeterministic, non-mutating evaluator for "is PAS179 wired\ncorrectly and free of regressions in the PAS160-PAS178\ndoctrine?".\n\nWalks the repo and verifies:\n\n  * PAS160-PAS178 readiness scripts still exist.\n  * PAS179 surfaces exist:\n      - scripts/migrate_v28_learning_recommendations.sql\n      - scripts/migrate_v29_simulation_runs.sql\n      - app/services/learning/learning_policy.py\n      - app/services/learning/scenario_contracts.py\n      - app/services/learning/outcome_feedback.py\n      - app/services/learning/recommendation_engine.py\n      - app/services/learning/guardrails.py\n      - scripts/pas179_controlled_learning_readiness_check.py\n      - docs/pas179_controlled_learning_architecture.md\n      - tests/mvp/test_pas179_controlled_learning_architecture.py\n  * v28 SQL carries PROPOSAL ONLY + DO NOT EXECUTE + closed\n    recommendation_type + status enums + RLS tenant SELECT\n    scoped + tenant INSERT/UPDATE/DELETE denied + service_role\n    INSERT CANDIDATE-only + restricted operator UPDATE gated\n    to CANDIDATE → terminal transitions + no DELETE.\n  * v29 SQL carries PROPOSAL ONLY + DO NOT EXECUTE + closed\n    scenario_type + mode + status enums + RLS tenant SELECT\n    scoped + tenant INSERT/UPDATE/DELETE denied + service_role\n    INSERT-only + no UPDATE / no DELETE policies + fingerprint\n    sha256 hex CHECK pins.\n  * Default learning mode is MANUAL.\n  * Automatic mode is structurally represented but blocked.\n  * No auto-approval helper in any PAS179 source file.\n  * No live mutation imports (outbound FSM, memory review,\n    booking, slack core, worker, audit_service).\n  * No LLM calls (no anthropic / openai imports).\n  * No embeddings / vector DB / Gmail / OAuth / IMAP / POP3 /\n    inbox-scanning / Composio / TrustClaw imports.\n  * Memory Review (PAS147-PAS158) untouched.\n  * audit_service.py STILL has no UPDATE / DELETE helpers\n    (PAS174-PAS178 carry-forward).\n  * Event contract registers every PAS179 event type.\n  * Worker still OFF by default; FastAPI lifespan does not\n    auto-start the worker.\n  * Supports --summary-only / --json.\n  * Exits 0 ready, 1 blockers, 2 bad args.\n  * Never reads .env.\n  * Never touches production data.\n'
- 'utf-8'
- 'READY'
- 'NOT_READY'
- 'BLOCK'
- 'severity'
- 'detail'
- 'pas179_controlled_learning_readiness_report.json'
- 'check_id'
- 'str'
- 'status'
- 'label'
- 'return'
- 'dict'
- 'seconds'
- 'path'
- 'Path'
- 'Optional[str]'
- 'replace'
- 'src'
- '"""'
- "'''"
- 'repo_root'
- 'List[dict]'
- 'file:'
- 'PASS'
- 'FAIL'
- 'Required PAS179 file present: '
- 'missing'
- 'prior_phase:'
- 'Prior-phase readiness script intact: '
- 'missing — PAS179 must not delete'
- 'memory_review:'
- 'Memory Review file present: '
- 'Memory Review file deleted — PAS179 must not touch'
- 'app'
- 'services'
- 'ingestion'
- 'worker.py'
- '_ENV_FLAG_ENABLED_LITERAL = "true"'
- "_ENV_FLAG_ENABLED_LITERAL = 'true'"
- 'worker:off_by_default'
- 'Pending-call worker is OFF by default'
- 'missing strict enable-literal constant'
- 'main.py'
- 'from app.services.ingestion.worker'
- 'from app.services.ingestion.worker import …'
- 'import app.services.ingestion.worker'
- 'run_worker_loop'
- 'run_worker_loop reference'
- 'process_pending_call('
- 'process_pending_call call'
- 'main:no_startup_worker'
- 'FastAPI lifespan does not auto-start the pending-call worker'
- 'disqualifying tokens: '
- 'learning'
- 'learning_policy.py'
- 'policy:'
- 'Learning policy token: '
- 'missing token '
- 'return "MANUAL"'
- "return 'MANUAL'"
- 'policy:default_manual'
- 'Learning policy defaults to MANUAL'
- 'missing explicit MANUAL default return'
- 'scenario_contracts.py'
- 'scenario:'
- 'Scenario contracts token: '
- 'outcome_feedback.py'
- 'outcome:'
- 'Outcome feedback token: '
- 'recommendation_engine.py'
- 'recommendation:'
- 'Recommendation engine token: '
- 'guardrails.py'
- 'guardrails:'
- 'Guardrails token: '
- 'app/services/learning/learning_policy.py'
- 'no_auto_approval:'
- 'No auto-approval / live-mutation tokens: '
- 'no_live_mutation_import:'
- 'No live-mutation imports: '
- 'forbidden imports: '
- 'PAS174-PAS178 invariant: audit_service has no\nUPDATE / DELETE helpers. PAS179 must preserve.'
- 'operator'
- 'audit_service.py'
- 'audit_service:append_only_carry'
- 'Audit service still has no UPDATE / DELETE mutation helpers (carry-forward invariant)'
- 'scripts'
- 'migrate_v28_learning_recommendations.sql'
- 'proposal only'
- 'v28_sql:proposal_only'
- "v28 SQL carries 'PROPOSAL ONLY' guardrail"
- "missing 'PROPOSAL ONLY' label"
- 'do not execute'
- 'v28_sql:do_not_execute'
- "v28 SQL carries 'DO NOT EXECUTE' trailer"
- 'missing trailer'
- 'CREATE TABLE IF NOT EXISTS pas_learning_recommendations'
- 'v28_sql:table_present'
- 'v28 SQL creates pas_learning_recommendations'
- 'missing CREATE TABLE'
- 'v28_sql:closed_recommendation_type_enum'
- 'v28 SQL carries the closed recommendation_type enum'
- 'missing one or more recommendation_type literals'
- 'v28_sql:closed_status_enum'
- 'v28 SQL carries the closed status enum'
- 'missing one or more status literals'
- 'pas_learning_recommendations_tenant_no_insert'
- 'pas_learning_recommendations_tenant_no_update'
- 'pas_learning_recommendations_tenant_no_delete'
- 'pas_learning_recommendations_service_role_insert'
- "WITH CHECK (status = 'CANDIDATE')"
- 'pas_learning_recommendations_service_role_review_update'
- 'pas_learning_recommendations_service_role_no_delete'
- 'v28_sql:append_only_with_review_update'
- 'v28 SQL denies tenant writes; service_role INSERT CANDIDATE-only; restricted operator UPDATE; no DELETE'
- 'missing one or more required policies'
- 'pas_learning_recommendations_tenant_select'
- "brokerage_id = (auth.jwt() ->> 'brokerage_id')"
- 'v28_sql:tenant_select_scoped'
- 'v28 SQL scopes tenant SELECT to own brokerage_id'
- 'missing tenant SELECT policy with brokerage_id scope'
- '>= 0 AND confidence_score <= 1'
- '>= 0 AND risk_score <= 1'
- '>= 0 AND usefulness_score <= 1'
- 'v28_sql:score_bounds'
- 'v28 SQL pins confidence/risk/usefulness scores to [0,1]'
- 'missing one or more score range CHECKs'
- 'migrate_v29_simulation_runs.sql'
- 'v29_sql:proposal_only'
- "v29 SQL carries 'PROPOSAL ONLY' guardrail"
- 'v29_sql:do_not_execute'
- "v29 SQL carries 'DO NOT EXECUTE' trailer"
- 'CREATE TABLE IF NOT EXISTS pas_simulation_runs'
- 'v29_sql:table_present'
- 'v29 SQL creates pas_simulation_runs'
- 'v29_sql:closed_scenario_type_enum'
- 'v29 SQL carries the closed scenario_type enum'
- 'missing one or more scenario_type literals'
- 'v29_sql:closed_mode_enum'
- 'v29 SQL carries the closed mode enum'
- 'missing one or more mode literals'
- 'v29_sql:closed_status_enum'
- 'v29 SQL carries the closed status enum'
- 'pas_simulation_runs_tenant_no_insert'
- 'pas_simulation_runs_tenant_no_update'
- 'pas_simulation_runs_tenant_no_delete'
- 'pas_simulation_runs_service_role_no_update'
- 'pas_simulation_runs_service_role_no_delete'
- 'v29_sql:append_only_policies'
- 'v29 SQL denies tenant writes + service_role UPDATE/DELETE'
- 'missing one or more no-update/no-delete/no-insert policies'
- 'pas_simulation_runs_tenant_select'
- 'v29_sql:tenant_select_scoped'
- 'v29 SQL scopes tenant SELECT to own brokerage_id'
- 'missing tenant SELECT policy'
- "'^[0-9a-f]{64}$'"
- 'v29_sql:fingerprint_check_constraint'
- 'v29 SQL pins fingerprint columns to sha256 hex shape'
- 'missing ^[0-9a-f]{64}$ regex'
- 'events'
- 'contract.py'
- 'events:'
- 'Event contract registers '
- 'missing event type '
- 'forbidden_import:'
- 'No forbidden imports: '
- 'forbidden import prefixes: '
- 'no_inbox_scan:'
- 'No inbox-scanning tokens: '
- 'inbox-scan tokens present: '
- 'docs'
- 'pas179_controlled_learning_architecture.md'
- 'docs:phrase:'
- 'Doctrine doc carries clause: '
- 'expected one of: '
- ' | '
- 'dotenv import'
- 'supabase import'
- 'load_dotenv()'
- 'load_dotenv() call'
- 'environ read'
- 'get_supabase'
- 'supabase client call'
- 'self_check:no_env_or_db'
- 'PAS179 readiness checker never reads .env / touches DB'
- 'disqualifying patterns: '
- 'checks'
- 'verdict'
- 'blockers'
- 'info'
- 'List[str]'
- ' — '
- 'see report'
- 'phase'
- 'PAS179'
- 'generated_at'
- 'ready'
- 'blocker_count'
- 'info_count'
- 'check_count'
- 'pass_count'
- 'fail_count'
- 'operator_actions'
- 'argparse.ArgumentParser'
- 🔒 '<REDACTED:high-entropy blob, len=42>'
- 'PAS179 — Evaluate controlled-learning architecture + scenario simulation contracts + guardrails. Read-only — never reads .env, never touches Supabase, never runs a migration.'
- '--repo-root'
- '--output'
- '--json'
- 'store_true'
- '--summary-only'
- '--strict'
- 'report'
- 'None'
- '[PAS179] verdict='
- ' blockers='
- ' info='
- ' checks='
- ' pass='
- ' fail='
- '[PAS179] operator actions:'
- '  - '
- '  ... and '
- ' more (see report file)'
- 'payload'
- '  [warn] failed to write report at '
- 'argv'
- 'Optional[List[str]]'
- 'int'
- 'error: --repo-root not a directory: '

## Disassembly

```
   0           RESUME                   0

   1           LOAD_CONST               0 ('\nPAS179 — Controlled learning architecture readiness gate.\n\nDeterministic, non-mutating evaluator for "is PAS179 wired\ncorrectly and free of regressions in the PAS160-PAS178\ndoctrine?".\n\nWalks the repo and verifies:\n\n  * PAS160-PAS178 readiness scripts still exist.\n  * PAS179 surfaces exist:\n      - scripts/migrate_v28_learning_recommendations.sql\n      - scripts/migrate_v29_simulation_runs.sql\n      - app/services/learning/learning_policy.py\n      - app/services/learning/scenario_contracts.py\n      - app/services/learning/outcome_feedback.py\n      - app/services/learning/recommendation_engine.py\n      - app/services/learning/guardrails.py\n      - scripts/pas179_controlled_learning_readiness_check.py\n      - docs/pas179_controlled_learning_architecture.md\n      - tests/mvp/test_pas179_controlled_learning_architecture.py\n  * v28 SQL carries PROPOSAL ONLY + DO NOT EXECUTE + closed\n    recommendation_type + status enums + RLS tenant SELECT\n    scoped + tenant INSERT/UPDATE/DELETE denied + service_role\n    INSERT CANDIDATE-only + restricted operator UPDATE gated\n    to CANDIDATE → terminal transitions + no DELETE.\n  * v29 SQL carries PROPOSAL ONLY + DO NOT EXECUTE + closed\n    scenario_type + mode + status enums + RLS tenant SELECT\n    scoped + tenant INSERT/UPDATE/DELETE denied + service_role\n    INSERT-only + no UPDATE / no DELETE policies + fingerprint\n    sha256 hex CHECK pins.\n  * Default learning mode is MANUAL.\n  * Automatic mode is structurally represented but blocked.\n  * No auto-approval helper in any PAS179 source file.\n  * No live mutation imports (outbound FSM, memory review,\n    booking, slack core, worker, audit_service).\n  * No LLM calls (no anthropic / openai imports).\n  * No embeddings / vector DB / Gmail / OAuth / IMAP / POP3 /\n    inbox-scanning / Composio / TrustClaw imports.\n  * Memory Review (PAS147-PAS158) untouched.\n  * audit_service.py STILL has no UPDATE / DELETE helpers\n    (PAS174-PAS178 carry-forward).\n  * Event contract registers every PAS179 event type.\n  * Worker still OFF by default; FastAPI lifespan does not\n    auto-start the worker.\n  * Supports --summary-only / --json.\n  * Exits 0 ready, 1 blockers, 2 bad args.\n  * Never reads .env.\n  * Never touches production data.\n')
               STORE_NAME               0 (__doc__)

  52           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  54           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  55           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (json)
               STORE_NAME               4 (json)

  56           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (os)
               STORE_NAME               5 (os)

  57           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (sys)
               STORE_NAME               6 (sys)

  58           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              7 (datetime)
               IMPORT_FROM              7 (datetime)
               STORE_NAME               7 (datetime)
               IMPORT_FROM              8 (timezone)
               STORE_NAME               8 (timezone)
               POP_TOP

  59           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Path',))
               IMPORT_NAME              9 (pathlib)
               IMPORT_FROM             10 (Path)
               STORE_NAME              10 (Path)
               POP_TOP

  60           LOAD_SMALL_INT           0
               LOAD_CONST               5 (('List', 'Optional'))
               IMPORT_NAME             11 (typing)
               IMPORT_FROM             12 (List)
               STORE_NAME              12 (List)
               IMPORT_FROM             13 (Optional)
               STORE_NAME              13 (Optional)
               POP_TOP

  63           LOAD_NAME                6 (sys)
               LOAD_ATTR               28 (stdout)
               LOAD_NAME                6 (sys)
               LOAD_ATTR               30 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              16 (_stream)

  64           NOP

  65   L2:     LOAD_NAME               16 (_stream)
               LOAD_ATTR               35 (reconfigure + NULL|self)
               LOAD_CONST               6 ('utf-8')
               LOAD_CONST               7 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  63   L4:     END_FOR
               POP_ITER

  70           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               41 (abspath + NULL|self)

  71           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               43 (join + NULL|self)
               LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               45 (dirname + NULL|self)
               LOAD_NAME               23 (__file__)
               CALL                     1
               LOAD_CONST               8 ('..')
               CALL                     2

  70           CALL                     1
               STORE_NAME              24 (_REPO_ROOT_DEFAULT)

  75           LOAD_CONST               9 ('READY')
               STORE_NAME              25 (VERDICT_READY)

  76           LOAD_CONST              10 ('NOT_READY')
               STORE_NAME              26 (VERDICT_NOT_READY)

  78           LOAD_CONST              11 ('BLOCK')
               STORE_NAME              27 (SEVERITY_BLOCK)

  85           LOAD_CONST              79 (('scripts/migrate_v28_learning_recommendations.sql', 'scripts/migrate_v29_simulation_runs.sql', 'app/services/learning/learning_policy.py', 'app/services/learning/scenario_contracts.py', 'app/services/learning/outcome_feedback.py', 'app/services/learning/recommendation_engine.py', 'app/services/learning/guardrails.py', 'scripts/pas179_controlled_learning_readiness_check.py', 'docs/pas179_controlled_learning_architecture.md', 'tests/mvp/test_pas179_controlled_learning_architecture.py'))
               STORE_NAME              28 (REQUIRED_FILES)

  98           LOAD_CONST              80 (('scripts/pas160_mvp_sequence_check.py', 'scripts/pas161_lead_ingestion_readiness_check.py', 'scripts/pas162_pending_calls_readiness_check.py', 'scripts/pas163_candidate_pipeline_readiness_check.py', 'scripts/pas164_email_ingestion_readiness_check.py', 'scripts/pas165_email_auth_dedupe_readiness_check.py', 'scripts/pas166_email_dedupe_policy_readiness_check.py', 'scripts/pas167_email_secret_reaper_readiness_check.py', 'scripts/pas168_email_secret_rotation_readiness_check.py', 'scripts/pas169_crypto_roundtrip_check.py', 'scripts/pas169_launch_readiness_check.py', 'scripts/pas_launch_integrity_check.py', 'scripts/pas170_operator_survival_readiness_check.py', 'scripts/pas171_external_pilot_readiness_check.py', 'scripts/pas172_pilot_operations_readiness_check.py', 'scripts/pas173_brokerage_operator_readiness_check.py', 'scripts/pas174_operator_audit_readiness_check.py', 'scripts/pas175_audit_integrity_readiness_check.py', 'scripts/pas176_audit_chain_readiness_check.py', 'scripts/pas177_tenant_audit_verification_readiness_check.py', 'scripts/pas178_audit_window_chain_readiness_check.py'))
               STORE_NAME              29 (PRIOR_PHASE_FILES)

 122           LOAD_CONST              81 (('app/services/memory/review.py', 'app/services/memory/review_stats.py', 'app/services/memory/review_export.py', 'app/services/memory/review_actors.py', 'app/services/memory/review_alerts.py', 'app/services/memory/operator_console.py'))
               STORE_NAME              30 (MEMORY_REVIEW_FILES)

 132           LOAD_CONST              82 (('def resolve_learning_mode(', 'def learning_mode_policy(', 'def automatic_mode_allowed(', 'def manual_mode_required(', 'def learning_policy_report(', 'ALLOWED_LEARNING_MODES', 'PAS_ADAPTIVE_LEARNING_AUTOMATIC_ENABLED', 'adaptive_learning_enabled', '_GLOBAL_ENV_FLAG_ENABLED_LITERAL', 'AUTOMATIC_LOCKED'))
               STORE_NAME              31 (REQUIRED_POLICY_TOKENS)

 145           LOAD_CONST              83 (('def build_scenario(', 'def scenario_fingerprint(', 'ALLOWED_SCENARIO_TYPES', 'FORBIDDEN_SCENARIO_FIELDS', 'ALLOWED_SCENARIO_FIELDS', 'def LeadResponseScenario(', 'def ObjectionHandlingScenario(', 'def CallbackFlowScenario(', 'def BookingFlowScenario(', 'def DuplicateSuppressionScenario(', 'def WorkerFailureScenario(', 'def ProviderFailureScenario(', 'def MemoryInjectionEffectScenario('))
               STORE_NAME              32 (REQUIRED_SCENARIO_TOKENS)

 161           LOAD_CONST              84 (('def build_outcome_feedback(', 'def outcome_feedback_fingerprint(', 'def score_outcome_feedback(', 'def feedback_summary(', 'ALLOWED_OUTCOMES', 'FORBIDDEN_FEEDBACK_FIELDS'))
               STORE_NAME              33 (REQUIRED_OUTCOME_TOKENS)

 170           LOAD_CONST              85 (('def build_learning_recommendation(', 'def score_learning_recommendation(', 'def recommendation_report(', 'def persist_learning_recommendation(', 'ALLOWED_RECOMMENDATION_TYPES', 'ALLOWED_RECOMMENDED_ACTIONS', 'ALLOWED_RATIONALE_TOKENS', '_TABLE = "pas_learning_recommendations"', 'learning_recommendations_store_unavailable', 'recommendation_status_must_be_candidate'))
               STORE_NAME              34 (REQUIRED_RECOMMENDATION_TOKENS)

 183           LOAD_CONST              86 (('def learning_forbidden_field_scan(', 'def validate_learning_recommendation(', 'def validate_simulation_safety(', 'def validate_adaptive_memory_guardrails(', 'FORBIDDEN_FIELDS', 'requires_operator_review'))
               STORE_NAME              35 (REQUIRED_GUARDRAIL_TOKENS)

 195           LOAD_CONST              87 (('auto_approve', 'auto_apply', 'auto_apply_recommendation', 'automatic_approve', 'apply_live', 'mutate_live'))
               STORE_NAME              36 (FORBIDDEN_AUTO_APPROVAL_TOKENS)

 207           LOAD_CONST              88 (('from app.engine.state_machine', 'import app.engine.state_machine', 'from app.services.memory.review', 'import app.services.memory.review', 'from app.services.memory.approval', 'import app.services.memory.approval', 'from app.services.booking', 'import app.services.booking', 'from app.services.outbound', 'import app.services.outbound', 'from app.services.worker', 'import app.services.worker', 'from app.services.ingestion.worker', 'import app.services.ingestion.worker', 'from app.services.operator.audit_service', 'import app.services.operator.audit_service', 'from app.services.slack', 'import app.services.slack'))
               STORE_NAME              37 (FORBIDDEN_LIVE_MUTATION_IMPORTS)

 229           LOAD_CONST              89 (('audit.window_chain.generated', 'audit.verification_run.persisted', 'learning.policy.resolved', 'learning.simulation.planned', 'learning.simulation.completed', 'learning.recommendation.generated', 'learning.recommendation.rejected_by_guardrail', 'learning.automatic_mode.blocked'))
               STORE_NAME              38 (REQUIRED_EVENT_TYPES)

 243           LOAD_CONST              90 (('import gmail', 'from gmail', 'import googleapiclient', 'from googleapiclient', 'import google.oauth2', 'from google.oauth2', 'from google.auth', 'import google.auth', 'from google_auth_oauthlib', 'import imaplib', 'from imaplib', 'import poplib', 'from poplib', 'import composio', 'from composio', 'import trustclaw', 'from trustclaw', 'import chromadb', 'from chromadb', 'import pinecone', 'from pinecone', 'import langchain', 'from langchain', 'import faiss', 'import pgvector', 'from pgvector', 'from openai import embeddings', 'from openai.embeddings', 'from anthropic', 'import anthropic', 'from openai', 'import openai'))
               STORE_NAME              39 (FORBIDDEN_IMPORT_LINE_PREFIXES)

 267           LOAD_CONST              91 (('imaplib', 'poplib', 'fetch_inbox', 'gmail_oauth', 'gmail_token', 'users().messages'))
               STORE_NAME              40 (FORBIDDEN_INBOX_TOKENS)

 281           LOAD_CONST              12 ('severity')

 283           LOAD_NAME               27 (SEVERITY_BLOCK)

 281           LOAD_CONST              13 ('detail')

 283           LOAD_CONST              14 ('')

 281           BUILD_MAP                2
               LOAD_CONST              15 (<code object __annotate__ at 0x0000018C18025530, file "scripts/pas179_controlled_learning_readiness_check.py", line 281>)
               MAKE_FUNCTION
               LOAD_CONST              16 (<code object _check at 0x0000018C17FA3B40, file "scripts/pas179_controlled_learning_readiness_check.py", line 281>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              41 (_check)

 294           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C17FA3A50, file "scripts/pas179_controlled_learning_readiness_check.py", line 294>)
               MAKE_FUNCTION
               LOAD_CONST              18 (<code object _now_iso at 0x0000018C18038CB0, file "scripts/pas179_controlled_learning_readiness_check.py", line 294>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              42 (_now_iso)

 298           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA31E0, file "scripts/pas179_controlled_learning_readiness_check.py", line 298>)
               MAKE_FUNCTION
               LOAD_CONST              20 (<code object _read_text at 0x0000018C180531B0, file "scripts/pas179_controlled_learning_readiness_check.py", line 298>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              43 (_read_text)

 305           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA3E10, file "scripts/pas179_controlled_learning_readiness_check.py", line 305>)
               MAKE_FUNCTION
               LOAD_CONST              22 (<code object _strip_python_comments_and_strings at 0x0000018C17ED3EB0, file "scripts/pas179_controlled_learning_readiness_check.py", line 305>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              44 (_strip_python_comments_and_strings)

 344           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA3960, file "scripts/pas179_controlled_learning_readiness_check.py", line 344>)
               MAKE_FUNCTION
               LOAD_CONST              24 (<code object check_files_present at 0x0000018C18061110, file "scripts/pas179_controlled_learning_readiness_check.py", line 344>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              45 (check_files_present)

 357           LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA3C30, file "scripts/pas179_controlled_learning_readiness_check.py", line 357>)
               MAKE_FUNCTION
               LOAD_CONST              26 (<code object check_prior_phases_intact at 0x0000018C18060DB0, file "scripts/pas179_controlled_learning_readiness_check.py", line 357>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              46 (check_prior_phases_intact)

 370           LOAD_CONST              27 (<code object __annotate__ at 0x0000018C18114120, file "scripts/pas179_controlled_learning_readiness_check.py", line 370>)
               MAKE_FUNCTION
               LOAD_CONST              28 (<code object check_memory_review_intact at 0x0000018C180612C0, file "scripts/pas179_controlled_learning_readiness_check.py", line 370>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              47 (check_memory_review_intact)

 383           LOAD_CONST              29 (<code object __annotate__ at 0x0000018C18114210, file "scripts/pas179_controlled_learning_readiness_check.py", line 383>)
               MAKE_FUNCTION
               LOAD_CONST              30 (<code object check_worker_off_by_default at 0x0000018C179C3E10, file "scripts/pas179_controlled_learning_readiness_check.py", line 383>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              48 (check_worker_off_by_default)

 400           LOAD_CONST              31 (<code object __annotate__ at 0x0000018C18114300, file "scripts/pas179_controlled_learning_readiness_check.py", line 400>)
               MAKE_FUNCTION
               LOAD_CONST              32 (<code object check_no_startup_worker at 0x0000018C17D86830, file "scripts/pas179_controlled_learning_readiness_check.py", line 400>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              49 (check_no_startup_worker)

 423           LOAD_CONST              33 (<code object __annotate__ at 0x0000018C181144E0, file "scripts/pas179_controlled_learning_readiness_check.py", line 423>)
               MAKE_FUNCTION
               LOAD_CONST              34 (<code object check_policy_service at 0x0000018C17CD0A50, file "scripts/pas179_controlled_learning_readiness_check.py", line 423>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              50 (check_policy_service)

 451           LOAD_CONST              35 (<code object __annotate__ at 0x0000018C181145D0, file "scripts/pas179_controlled_learning_readiness_check.py", line 451>)
               MAKE_FUNCTION
               LOAD_CONST              36 (<code object check_scenario_contracts at 0x0000018C17FED830, file "scripts/pas179_controlled_learning_readiness_check.py", line 451>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              51 (check_scenario_contracts)

 466           LOAD_CONST              37 (<code object __annotate__ at 0x0000018C181146C0, file "scripts/pas179_controlled_learning_readiness_check.py", line 466>)
               MAKE_FUNCTION
               LOAD_CONST              38 (<code object check_outcome_feedback at 0x0000018C17FEE030, file "scripts/pas179_controlled_learning_readiness_check.py", line 466>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              52 (check_outcome_feedback)

 481           LOAD_CONST              39 (<code object __annotate__ at 0x0000018C181147B0, file "scripts/pas179_controlled_learning_readiness_check.py", line 481>)
               MAKE_FUNCTION
               LOAD_CONST              40 (<code object check_recommendation_engine at 0x0000018C17FED630, file "scripts/pas179_controlled_learning_readiness_check.py", line 481>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              53 (check_recommendation_engine)

 496           LOAD_CONST              41 (<code object __annotate__ at 0x0000018C181148A0, file "scripts/pas179_controlled_learning_readiness_check.py", line 496>)
               MAKE_FUNCTION
               LOAD_CONST              42 (<code object check_guardrails at 0x0000018C17FEDC30, file "scripts/pas179_controlled_learning_readiness_check.py", line 496>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              54 (check_guardrails)

 511           LOAD_CONST              43 (<code object __annotate__ at 0x0000018C18114990, file "scripts/pas179_controlled_learning_readiness_check.py", line 511>)
               MAKE_FUNCTION
               LOAD_CONST              44 (<code object check_no_auto_approval_tokens at 0x0000018C182FF320, file "scripts/pas179_controlled_learning_readiness_check.py", line 511>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              55 (check_no_auto_approval_tokens)

 540           LOAD_CONST              45 (<code object __annotate__ at 0x0000018C18114A80, file "scripts/pas179_controlled_learning_readiness_check.py", line 540>)
               MAKE_FUNCTION
               LOAD_CONST              46 (<code object check_no_live_mutation_imports at 0x0000018C17F72FD0, file "scripts/pas179_controlled_learning_readiness_check.py", line 540>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              56 (check_no_live_mutation_imports)

 572           LOAD_CONST              47 (<code object __annotate__ at 0x0000018C18114B70, file "scripts/pas179_controlled_learning_readiness_check.py", line 572>)
               MAKE_FUNCTION
               LOAD_CONST              48 (<code object check_audit_service_invariant at 0x0000018C182DAEE0, file "scripts/pas179_controlled_learning_readiness_check.py", line 572>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              57 (check_audit_service_invariant)

 599           LOAD_CONST              49 (<code object __annotate__ at 0x0000018C18114C60, file "scripts/pas179_controlled_learning_readiness_check.py", line 599>)
               MAKE_FUNCTION
               LOAD_CONST              50 (<code object check_v28_sql at 0x0000018C17D7C560, file "scripts/pas179_controlled_learning_readiness_check.py", line 599>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              58 (check_v28_sql)

 697           LOAD_CONST              51 (<code object __annotate__ at 0x0000018C18114D50, file "scripts/pas179_controlled_learning_readiness_check.py", line 697>)
               MAKE_FUNCTION
               LOAD_CONST              52 (<code object check_v29_sql at 0x0000018C17F79F10, file "scripts/pas179_controlled_learning_readiness_check.py", line 697>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              59 (check_v29_sql)

 792           LOAD_CONST              53 (<code object __annotate__ at 0x0000018C18114E40, file "scripts/pas179_controlled_learning_readiness_check.py", line 792>)
               MAKE_FUNCTION
               LOAD_CONST              54 (<code object check_event_contract at 0x0000018C1801C9E0, file "scripts/pas179_controlled_learning_readiness_check.py", line 792>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              60 (check_event_contract)

 807           LOAD_CONST              55 (<code object __annotate__ at 0x0000018C18114F30, file "scripts/pas179_controlled_learning_readiness_check.py", line 807>)
               MAKE_FUNCTION
               LOAD_CONST              56 (<code object check_no_forbidden_imports at 0x0000018C17F73CD0, file "scripts/pas179_controlled_learning_readiness_check.py", line 807>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              61 (check_no_forbidden_imports)

 840           LOAD_CONST              57 (<code object __annotate__ at 0x0000018C18115020, file "scripts/pas179_controlled_learning_readiness_check.py", line 840>)
               MAKE_FUNCTION
               LOAD_CONST              58 (<code object check_no_inbox_scan_tokens at 0x0000018C17CC1F60, file "scripts/pas179_controlled_learning_readiness_check.py", line 840>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              62 (check_no_inbox_scan_tokens)

 869           LOAD_CONST              59 (<code object __annotate__ at 0x0000018C18115200, file "scripts/pas179_controlled_learning_readiness_check.py", line 869>)
               MAKE_FUNCTION
               LOAD_CONST              60 (<code object check_doc_required_clauses at 0x0000018C17CD0CE0, file "scripts/pas179_controlled_learning_readiness_check.py", line 869>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              63 (check_doc_required_clauses)

 915           LOAD_CONST              61 (<code object __annotate__ at 0x0000018C181152F0, file "scripts/pas179_controlled_learning_readiness_check.py", line 915>)
               MAKE_FUNCTION
               LOAD_CONST              62 (<code object check_self_no_env_or_db at 0x0000018C17D88890, file "scripts/pas179_controlled_learning_readiness_check.py", line 915>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              64 (check_self_no_env_or_db)

 948           LOAD_CONST              63 (<code object __annotate__ at 0x0000018C181153E0, file "scripts/pas179_controlled_learning_readiness_check.py", line 948>)
               MAKE_FUNCTION
               LOAD_CONST              64 (<code object _aggregate at 0x0000018C1800B0A0, file "scripts/pas179_controlled_learning_readiness_check.py", line 948>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              65 (_aggregate)

 960           LOAD_CONST              65 (<code object __annotate__ at 0x0000018C181154D0, file "scripts/pas179_controlled_learning_readiness_check.py", line 960>)
               MAKE_FUNCTION
               LOAD_CONST              66 (<code object _operator_actions at 0x0000018C18048C70, file "scripts/pas179_controlled_learning_readiness_check.py", line 960>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              66 (_operator_actions)

 970           LOAD_CONST              67 (<code object __annotate__ at 0x0000018C181155C0, file "scripts/pas179_controlled_learning_readiness_check.py", line 970>)
               MAKE_FUNCTION
               LOAD_CONST              68 (<code object evaluate at 0x0000018C177C69F0, file "scripts/pas179_controlled_learning_readiness_check.py", line 970>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              67 (evaluate)

1009           LOAD_CONST              69 ('pas179_controlled_learning_readiness_report.json')
               STORE_NAME              68 (REPORT_FILENAME)

1012           LOAD_CONST              70 (<code object __annotate__ at 0x0000018C18115980, file "scripts/pas179_controlled_learning_readiness_check.py", line 1012>)
               MAKE_FUNCTION
               LOAD_CONST              71 (<code object _build_parser at 0x0000018C180FC210, file "scripts/pas179_controlled_learning_readiness_check.py", line 1012>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              69 (_build_parser)

1030           LOAD_CONST              72 (<code object __annotate__ at 0x0000018C18115A70, file "scripts/pas179_controlled_learning_readiness_check.py", line 1030>)
               MAKE_FUNCTION
               LOAD_CONST              73 (<code object _print_summary at 0x0000018C17D8C5C0, file "scripts/pas179_controlled_learning_readiness_check.py", line 1030>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              70 (_print_summary)

1048           LOAD_CONST              74 (<code object __annotate__ at 0x0000018C18025230, file "scripts/pas179_controlled_learning_readiness_check.py", line 1048>)
               MAKE_FUNCTION
               LOAD_CONST              75 (<code object _write_report at 0x0000018C180FC990, file "scripts/pas179_controlled_learning_readiness_check.py", line 1048>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              71 (_write_report)

1062           LOAD_CONST              92 ((None,))
               LOAD_CONST              76 (<code object __annotate__ at 0x0000018C18115B60, file "scripts/pas179_controlled_learning_readiness_check.py", line 1062>)
               MAKE_FUNCTION
               LOAD_CONST              77 (<code object main at 0x0000018C17D884E0, file "scripts/pas179_controlled_learning_readiness_check.py", line 1062>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              72 (main)

1087           LOAD_NAME               73 (__name__)
               LOAD_CONST              78 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

1088           LOAD_NAME                6 (sys)
               LOAD_ATTR              148 (exit)
               PUSH_NULL
               LOAD_NAME               72 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

1087   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  66           LOAD_NAME               18 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  67   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          377 (to L1)

  66   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025530, file "scripts/pas179_controlled_learning_readiness_check.py", line 281>:
281           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('check_id')

282           LOAD_CONST               2 ('str')

281           LOAD_CONST               3 ('status')

282           LOAD_CONST               2 ('str')

281           LOAD_CONST               4 ('label')

282           LOAD_CONST               2 ('str')

281           LOAD_CONST               5 ('severity')

283           LOAD_CONST               2 ('str')

281           LOAD_CONST               6 ('detail')

283           LOAD_CONST               2 ('str')

281           LOAD_CONST               7 ('return')

284           LOAD_CONST               8 ('dict')

281           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _check at 0x0000018C17FA3B40, file "scripts/pas179_controlled_learning_readiness_check.py", line 281>:
281           RESUME                   0

286           LOAD_CONST               0 ('id')
              LOAD_FAST_BORROW         0 (check_id)

287           LOAD_CONST               1 ('status')
              LOAD_FAST_BORROW         1 (status)

288           LOAD_CONST               2 ('label')
              LOAD_FAST_BORROW         2 (label)

289           LOAD_CONST               3 ('severity')
              LOAD_FAST_BORROW         3 (severity)

290           LOAD_CONST               4 ('detail')
              LOAD_FAST_BORROW         4 (detail)

285           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "scripts/pas179_controlled_learning_readiness_check.py", line 294>:
294           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('str')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _now_iso at 0x0000018C18038CB0, file "scripts/pas179_controlled_learning_readiness_check.py", line 294>:
294           RESUME                   0

295           LOAD_GLOBAL              0 (datetime)
              LOAD_ATTR                2 (now)
              PUSH_NULL
              LOAD_GLOBAL              4 (timezone)
              LOAD_ATTR                6 (utc)
              CALL                     1
              LOAD_ATTR                9 (isoformat + NULL|self)
              LOAD_CONST               0 ('seconds')
              LOAD_CONST               1 (('timespec',))
              CALL_KW                  1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "scripts/pas179_controlled_learning_readiness_check.py", line 298>:
298           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('path')
              LOAD_CONST               2 ('Path')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _read_text at 0x0000018C180531B0, file "scripts/pas179_controlled_learning_readiness_check.py", line 298>:
 298           RESUME                   0

 299           NOP

 300   L1:     LOAD_FAST_BORROW         0 (path)
               LOAD_ATTR                1 (read_text + NULL|self)
               LOAD_CONST               0 ('utf-8')
               LOAD_CONST               1 ('replace')
               LOAD_CONST               2 (('encoding', 'errors'))
               CALL_KW                  2
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 301           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 302   L4:     POP_EXCEPT
               LOAD_CONST               3 (None)
               RETURN_VALUE

 301   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "scripts/pas179_controlled_learning_readiness_check.py", line 305>:
305           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('src')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               2 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _strip_python_comments_and_strings at 0x0000018C17ED3EB0, file "scripts/pas179_controlled_learning_readiness_check.py", line 305>:
305            RESUME                   0

306            BUILD_LIST               0
               STORE_FAST               1 (out)

307            LOAD_SMALL_INT           0
               LOAD_GLOBAL              1 (len + NULL)
               LOAD_FAST_BORROW         0 (src)
               CALL                     1
               STORE_FAST_STORE_FAST   50 (n, i)

308    L1:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (i, n)
               COMPARE_OP              18 (bool(<))
               EXTENDED_ARG             1
               POP_JUMP_IF_FALSE      282 (to L13)
               NOT_TAKEN

309            LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               BINARY_OP               26 ([])
               STORE_FAST               4 (ch)

310            LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               1 ('#')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       38 (to L3)
               NOT_TAKEN

311            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_CONST               2 ('\n')
               LOAD_FAST_BORROW         2 (i)
               CALL                     2
               STORE_FAST               5 (j)

312            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L2)
               NOT_TAKEN

313            JUMP_FORWARD           240 (to L13)

314    L2:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

315            JUMP_BACKWARD           59 (to L1)

316    L3:     LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                5 (startswith + NULL|self)
               LOAD_CONST               3 ('"""')
               LOAD_FAST_BORROW         2 (i)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        25 (to L4)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                5 (startswith + NULL|self)
               LOAD_CONST               4 ("'''")
               LOAD_FAST_BORROW         2 (i)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       55 (to L6)
               NOT_TAKEN

317    L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               BINARY_SLICE
               STORE_FAST               6 (quote)

318            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 98 (quote, i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               CALL                     2
               STORE_FAST               7 (end)

319            LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L5)
               NOT_TAKEN

320            JUMP_FORWARD           138 (to L13)

321    L5:     LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

322            JUMP_BACKWARD          161 (to L1)

323    L6:     LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               7 (('"', "'"))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       92 (to L12)
               NOT_TAKEN

324            LOAD_FAST                4 (ch)
               STORE_FAST               6 (quote)

325            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               5 (j)

326    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (j, n)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       63 (to L11)
               NOT_TAKEN

327            LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
               BINARY_OP               26 ([])
               LOAD_CONST               5 ('\\')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       12 (to L8)
               NOT_TAKEN

328            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           2
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)

329            JUMP_BACKWARD           30 (to L7)

330    L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
               BINARY_OP               26 ([])
               LOAD_FAST_BORROW         6 (quote)
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_TRUE        14 (to L9)
               NOT_TAKEN
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
               BINARY_OP               26 ([])
               LOAD_CONST               2 ('\n')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE        2 (to L10)
               NOT_TAKEN

331    L9:     JUMP_FORWARD            11 (to L11)

332   L10:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)
               JUMP_BACKWARD           68 (to L7)

333   L11:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

334            EXTENDED_ARG             1
               JUMP_BACKWARD          259 (to L1)

335   L12:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (ch)
               CALL                     1
               POP_TOP

336            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               2 (i)
               EXTENDED_ARG             1
               JUMP_BACKWARD          288 (to L1)

337   L13:     LOAD_CONST               6 ('')
               LOAD_ATTR                9 (join + NULL|self)
               LOAD_FAST_BORROW         1 (out)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "scripts/pas179_controlled_learning_readiness_check.py", line 344>:
344           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_files_present at 0x0000018C18061110, file "scripts/pas179_controlled_learning_readiness_check.py", line 344>:
344           RESUME                   0

345           BUILD_LIST               0
              STORE_FAST               1 (out)

346           LOAD_GLOBAL              0 (REQUIRED_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

347           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

348           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

349           LOAD_CONST               0 ('file:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

350           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

351   L3:     LOAD_CONST               3 ('Required PAS179 file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

352           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing')

348   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

346   L6:     END_FOR
              POP_ITER

354           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "scripts/pas179_controlled_learning_readiness_check.py", line 357>:
357           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_prior_phases_intact at 0x0000018C18060DB0, file "scripts/pas179_controlled_learning_readiness_check.py", line 357>:
357           RESUME                   0

358           BUILD_LIST               0
              STORE_FAST               1 (out)

359           LOAD_GLOBAL              0 (PRIOR_PHASE_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

360           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

361           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

362           LOAD_CONST               0 ('prior_phase:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

363           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

364   L3:     LOAD_CONST               3 ('Prior-phase readiness script intact: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

365           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing — PAS179 must not delete')

361   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

359   L6:     END_FOR
              POP_ITER

367           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114120, file "scripts/pas179_controlled_learning_readiness_check.py", line 370>:
370           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_memory_review_intact at 0x0000018C180612C0, file "scripts/pas179_controlled_learning_readiness_check.py", line 370>:
370           RESUME                   0

371           BUILD_LIST               0
              STORE_FAST               1 (out)

372           LOAD_GLOBAL              0 (MEMORY_REVIEW_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

373           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

374           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

375           LOAD_CONST               0 ('memory_review:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

376           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

377   L3:     LOAD_CONST               3 ('Memory Review file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

378           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('Memory Review file deleted — PAS179 must not touch')

374   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

372   L6:     END_FOR
              POP_ITER

380           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114210, file "scripts/pas179_controlled_learning_readiness_check.py", line 383>:
383           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_worker_off_by_default at 0x0000018C179C3E10, file "scripts/pas179_controlled_learning_readiness_check.py", line 383>:
383           RESUME                   0

384           BUILD_LIST               0
              STORE_FAST               1 (out)

385           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('services')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('ingestion')
              BINARY_OP               11 (/)
              LOAD_CONST               3 ('worker.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

386           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

388           LOAD_CONST               5 ('_ENV_FLAG_ENABLED_LITERAL = "true"')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         6 (to L2)
              NOT_TAKEN
              POP_TOP

389           LOAD_CONST               6 ("_ENV_FLAG_ENABLED_LITERAL = 'true'")
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)

387   L2:     STORE_FAST               4 (literal_ok)

391           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

392           LOAD_CONST               7 ('worker:off_by_default')

393           LOAD_FAST_BORROW         4 (literal_ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               8 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               9 ('FAIL')

394   L4:     LOAD_CONST              10 ('Pending-call worker is OFF by default')

395           LOAD_FAST_BORROW         4 (literal_ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST              11 ('missing strict enable-literal constant')

391   L6:     LOAD_CONST              12 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

397           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114300, file "scripts/pas179_controlled_learning_readiness_check.py", line 400>:
400           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_no_startup_worker at 0x0000018C17D86830, file "scripts/pas179_controlled_learning_readiness_check.py", line 400>:
400           RESUME                   0

401           BUILD_LIST               0
              STORE_FAST               1 (out)

402           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('main.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

403           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               2 ('')
      L1:     STORE_FAST               3 (src)

404           LOAD_GLOBAL              5 (_strip_python_comments_and_strings + NULL)
              LOAD_FAST_BORROW         3 (src)
              CALL                     1
              STORE_FAST               4 (executable)

405           BUILD_LIST               0
              STORE_FAST               5 (bad)

406           LOAD_CONST               3 ('from app.services.ingestion.worker')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L2)
              NOT_TAKEN

407           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               4 ('from app.services.ingestion.worker import …')
              CALL                     1
              POP_TOP

408   L2:     LOAD_CONST               5 ('import app.services.ingestion.worker')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L3)
              NOT_TAKEN

409           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               5 ('import app.services.ingestion.worker')
              CALL                     1
              POP_TOP

410   L3:     LOAD_CONST               6 ('run_worker_loop')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L4)
              NOT_TAKEN

411           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               7 ('run_worker_loop reference')
              CALL                     1
              POP_TOP

412   L4:     LOAD_CONST               8 ('process_pending_call(')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L5)
              NOT_TAKEN

413           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               9 ('process_pending_call call')
              CALL                     1
              POP_TOP

414   L5:     LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

415           LOAD_CONST              10 ('main:no_startup_worker')

416           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L6)
              NOT_TAKEN
              LOAD_CONST              11 ('FAIL')
              JUMP_FORWARD             1 (to L7)
      L6:     LOAD_CONST              12 ('PASS')

417   L7:     LOAD_CONST              13 ('FastAPI lifespan does not auto-start the pending-call worker')

418           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE       25 (to L8)
              NOT_TAKEN
              LOAD_CONST              14 ('disqualifying tokens: ')
              LOAD_CONST              15 (', ')
              LOAD_ATTR               11 (join + NULL|self)
              LOAD_FAST_BORROW         5 (bad)
              CALL                     1
              BINARY_OP                0 (+)
              JUMP_FORWARD             1 (to L9)
      L8:     LOAD_CONST               2 ('')

414   L9:     LOAD_CONST              16 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

420           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181144E0, file "scripts/pas179_controlled_learning_readiness_check.py", line 423>:
423           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_policy_service at 0x0000018C17CD0A50, file "scripts/pas179_controlled_learning_readiness_check.py", line 423>:
423            RESUME                   0

424            BUILD_LIST               0
               STORE_FAST               1 (out)

425            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('services')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('learning')
               BINARY_OP               11 (/)
               LOAD_CONST               3 ('learning_policy.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

426            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')
       L1:     STORE_FAST               3 (src)

427            LOAD_GLOBAL              4 (REQUIRED_POLICY_TOKENS)
               GET_ITER
       L2:     FOR_ITER                73 (to L7)
               STORE_FAST               4 (tok)

428            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

429            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

430            LOAD_CONST               5 ('policy:')
               LOAD_FAST_BORROW         4 (tok)
               LOAD_CONST               6 (slice(None, 48, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

431            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               8 ('FAIL')

432    L4:     LOAD_CONST               9 ('Learning policy token: ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

433            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST              10 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

429    L6:     LOAD_CONST              11 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           75 (to L2)

427    L7:     END_FOR
               POP_ITER

439            LOAD_CONST              12 ('return "MANUAL"')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L8)
               NOT_TAKEN
               POP_TOP

440            LOAD_CONST              13 ("return 'MANUAL'")
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

438    L8:     STORE_FAST               6 (default_manual_ok)

442            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

443            LOAD_CONST              14 ('policy:default_manual')

444            LOAD_FAST_BORROW         6 (default_manual_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L10)
       L9:     LOAD_CONST               8 ('FAIL')

445   L10:     LOAD_CONST              15 ('Learning policy defaults to MANUAL')

446            LOAD_FAST_BORROW         6 (default_manual_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST              16 ('missing explicit MANUAL default return')

442   L12:     LOAD_CONST              11 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

448            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181145D0, file "scripts/pas179_controlled_learning_readiness_check.py", line 451>:
451           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_scenario_contracts at 0x0000018C17FED830, file "scripts/pas179_controlled_learning_readiness_check.py", line 451>:
451           RESUME                   0

452           BUILD_LIST               0
              STORE_FAST               1 (out)

453           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('services')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('learning')
              BINARY_OP               11 (/)
              LOAD_CONST               3 ('scenario_contracts.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

454           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

455           LOAD_GLOBAL              4 (REQUIRED_SCENARIO_TOKENS)
              GET_ITER
      L2:     FOR_ITER                73 (to L7)
              STORE_FAST               4 (tok)

456           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

457           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

458           LOAD_CONST               5 ('scenario:')
              LOAD_FAST_BORROW         4 (tok)
              LOAD_CONST               6 (slice(None, 48, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

459           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               7 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               8 ('FAIL')

460   L4:     LOAD_CONST               9 ('Scenario contracts token: ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

461           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             4 (to L6)
      L5:     LOAD_CONST              10 ('missing token ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

457   L6:     LOAD_CONST              11 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           75 (to L2)

455   L7:     END_FOR
              POP_ITER

463           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181146C0, file "scripts/pas179_controlled_learning_readiness_check.py", line 466>:
466           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_outcome_feedback at 0x0000018C17FEE030, file "scripts/pas179_controlled_learning_readiness_check.py", line 466>:
466           RESUME                   0

467           BUILD_LIST               0
              STORE_FAST               1 (out)

468           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('services')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('learning')
              BINARY_OP               11 (/)
              LOAD_CONST               3 ('outcome_feedback.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

469           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

470           LOAD_GLOBAL              4 (REQUIRED_OUTCOME_TOKENS)
              GET_ITER
      L2:     FOR_ITER                73 (to L7)
              STORE_FAST               4 (tok)

471           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

472           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

473           LOAD_CONST               5 ('outcome:')
              LOAD_FAST_BORROW         4 (tok)
              LOAD_CONST               6 (slice(None, 48, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

474           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               7 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               8 ('FAIL')

475   L4:     LOAD_CONST               9 ('Outcome feedback token: ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

476           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             4 (to L6)
      L5:     LOAD_CONST              10 ('missing token ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

472   L6:     LOAD_CONST              11 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           75 (to L2)

470   L7:     END_FOR
              POP_ITER

478           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181147B0, file "scripts/pas179_controlled_learning_readiness_check.py", line 481>:
481           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_recommendation_engine at 0x0000018C17FED630, file "scripts/pas179_controlled_learning_readiness_check.py", line 481>:
481           RESUME                   0

482           BUILD_LIST               0
              STORE_FAST               1 (out)

483           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('services')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('learning')
              BINARY_OP               11 (/)
              LOAD_CONST               3 ('recommendation_engine.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

484           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

485           LOAD_GLOBAL              4 (REQUIRED_RECOMMENDATION_TOKENS)
              GET_ITER
      L2:     FOR_ITER                73 (to L7)
              STORE_FAST               4 (tok)

486           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

487           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

488           LOAD_CONST               5 ('recommendation:')
              LOAD_FAST_BORROW         4 (tok)
              LOAD_CONST               6 (slice(None, 48, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

489           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               7 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               8 ('FAIL')

490   L4:     LOAD_CONST               9 ('Recommendation engine token: ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

491           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             4 (to L6)
      L5:     LOAD_CONST              10 ('missing token ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

487   L6:     LOAD_CONST              11 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           75 (to L2)

485   L7:     END_FOR
              POP_ITER

493           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181148A0, file "scripts/pas179_controlled_learning_readiness_check.py", line 496>:
496           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_guardrails at 0x0000018C17FEDC30, file "scripts/pas179_controlled_learning_readiness_check.py", line 496>:
496           RESUME                   0

497           BUILD_LIST               0
              STORE_FAST               1 (out)

498           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('services')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('learning')
              BINARY_OP               11 (/)
              LOAD_CONST               3 ('guardrails.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

499           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

500           LOAD_GLOBAL              4 (REQUIRED_GUARDRAIL_TOKENS)
              GET_ITER
      L2:     FOR_ITER                73 (to L7)
              STORE_FAST               4 (tok)

501           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

502           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

503           LOAD_CONST               5 ('guardrails:')
              LOAD_FAST_BORROW         4 (tok)
              LOAD_CONST               6 (slice(None, 48, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

504           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               7 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               8 ('FAIL')

505   L4:     LOAD_CONST               9 ('Guardrails token: ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

506           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             4 (to L6)
      L5:     LOAD_CONST              10 ('missing token ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

502   L6:     LOAD_CONST              11 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           75 (to L2)

500   L7:     END_FOR
              POP_ITER

508           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114990, file "scripts/pas179_controlled_learning_readiness_check.py", line 511>:
511           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_no_auto_approval_tokens at 0x0000018C182FF320, file "scripts/pas179_controlled_learning_readiness_check.py", line 511>:
511            RESUME                   0

512            BUILD_LIST               0
               STORE_FAST               1 (out)

513            LOAD_CONST               9 (('app/services/learning/learning_policy.py', 'app/services/learning/scenario_contracts.py', 'app/services/learning/outcome_feedback.py', 'app/services/learning/recommendation_engine.py', 'app/services/learning/guardrails.py'))
               STORE_FAST               2 (files)

520            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               242 (to L11)
               STORE_FAST               3 (relpath)

521            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

522            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

523            JUMP_BACKWARD           45 (to L1)

524    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

525            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         5 (src)
               CALL                     1
               STORE_FAST               6 (executable)

526            BUILD_LIST               0
               STORE_FAST               7 (bad)

527            LOAD_GLOBAL              8 (FORBIDDEN_AUTO_APPROVAL_TOKENS)
               GET_ITER
       L4:     FOR_ITER                57 (to L6)
               STORE_FAST               8 (tok)

528            LOAD_FAST_BORROW         8 (tok)
               LOAD_ATTR               11 (lower + NULL|self)
               CALL                     0
               LOAD_FAST_BORROW         6 (executable)
               LOAD_ATTR               11 (lower + NULL|self)
               CALL                     0
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           40 (to L4)

529    L5:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR               13 (append + NULL|self)
               LOAD_FAST_BORROW         8 (tok)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           59 (to L4)

527    L6:     END_FOR
               POP_ITER

530            LOAD_FAST                1 (out)
               LOAD_ATTR               13 (append + NULL|self)
               LOAD_GLOBAL             15 (_check + NULL)

531            LOAD_CONST               2 ('no_auto_approval:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

532            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L7)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L8)
       L7:     LOAD_CONST               4 ('PASS')

533    L8:     LOAD_CONST               5 ('No auto-approval / live-mutation tokens: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

535            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       43 (to L9)
               NOT_TAKEN

534            LOAD_CONST               6 ('disqualifying tokens: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               17 (join + NULL|self)
               LOAD_GLOBAL             19 (sorted + NULL)
               LOAD_GLOBAL             21 (set + NULL)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               CALL                     1
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L10)

535    L9:     LOAD_CONST               1 ('')

530   L10:     LOAD_CONST               8 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          244 (to L1)

520   L11:     END_FOR
               POP_ITER

537            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114A80, file "scripts/pas179_controlled_learning_readiness_check.py", line 540>:
540           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_no_live_mutation_imports at 0x0000018C17F72FD0, file "scripts/pas179_controlled_learning_readiness_check.py", line 540>:
540            RESUME                   0

541            BUILD_LIST               0
               STORE_FAST               1 (out)

542            LOAD_CONST              10 (('app/services/learning/learning_policy.py', 'app/services/learning/scenario_contracts.py', 'app/services/learning/outcome_feedback.py', 'app/services/learning/recommendation_engine.py', 'app/services/learning/guardrails.py'))
               STORE_FAST               2 (files)

549            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     EXTENDED_ARG             1
               FOR_ITER               292 (to L15)
               STORE_FAST               3 (relpath)

550            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

551            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

552            JUMP_BACKWARD           46 (to L1)

553    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

554            BUILD_LIST               0
               STORE_FAST               6 (bad)

555            LOAD_FAST_BORROW         5 (src)
               LOAD_ATTR                7 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L4:     FOR_ITER               107 (to L10)
               STORE_FAST               7 (line)

556            LOAD_FAST_BORROW         7 (line)
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               STORE_FAST               8 (stripped)

557            LOAD_FAST_BORROW         8 (stripped)
               TO_BOOL
               POP_JUMP_IF_FALSE       24 (to L5)
               NOT_TAKEN
               LOAD_FAST_BORROW         8 (stripped)
               LOAD_ATTR               11 (startswith + NULL|self)
               LOAD_CONST               2 ('#')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L6)
               NOT_TAKEN

558    L5:     JUMP_BACKWARD           52 (to L4)

559    L6:     LOAD_GLOBAL             12 (FORBIDDEN_LIVE_MUTATION_IMPORTS)
               GET_ITER
       L7:     FOR_ITER                45 (to L9)
               STORE_FAST               9 (prefix)

560            LOAD_FAST_BORROW         8 (stripped)
               LOAD_ATTR               11 (startswith + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD           28 (to L7)

561    L8:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           47 (to L7)

559    L9:     END_FOR
               POP_ITER
               JUMP_BACKWARD          109 (to L4)

555   L10:     END_FOR
               POP_ITER

562            LOAD_FAST                1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             17 (_check + NULL)

563            LOAD_CONST               3 ('no_live_mutation_import:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

564            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               4 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               5 ('PASS')

565   L12:     LOAD_CONST               6 ('No live-mutation imports: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

567            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       43 (to L13)
               NOT_TAKEN

566            LOAD_CONST               7 ('forbidden imports: ')
               LOAD_CONST               8 (', ')
               LOAD_ATTR               19 (join + NULL|self)
               LOAD_GLOBAL             21 (sorted + NULL)
               LOAD_GLOBAL             23 (set + NULL)
               LOAD_FAST_BORROW         6 (bad)
               CALL                     1
               CALL                     1
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L14)

567   L13:     LOAD_CONST               1 ('')

562   L14:     LOAD_CONST               9 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          295 (to L1)

549   L15:     END_FOR
               POP_ITER

569            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114B70, file "scripts/pas179_controlled_learning_readiness_check.py", line 572>:
572           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_audit_service_invariant at 0x0000018C182DAEE0, file "scripts/pas179_controlled_learning_readiness_check.py", line 572>:
572           RESUME                   0

575           BUILD_LIST               0
              STORE_FAST               1 (out)

576           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               1 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('services')
              BINARY_OP               11 (/)
              LOAD_CONST               3 ('operator')
              BINARY_OP               11 (/)
              LOAD_CONST               4 ('audit_service.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

577           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               5 ('')
      L1:     STORE_FAST               3 (src)

578           LOAD_CONST              13 (('def update_audit_', 'def delete_audit_', 'def update_operator_audit_', 'def delete_operator_audit_', 'def mutate_audit_', 'def truncate_audit_'))
              STORE_FAST               4 (forbidden)

586           BUILD_LIST               0
              STORE_FAST               5 (bad)

587           LOAD_FAST_BORROW         4 (forbidden)
              GET_ITER
      L2:     FOR_ITER                28 (to L4)
              STORE_FAST               6 (tok)

588           LOAD_FAST_BORROW_LOAD_FAST_BORROW 99 (tok, src)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

589   L3:     LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_FAST_BORROW         6 (tok)
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           30 (to L2)

587   L4:     END_FOR
              POP_ITER

590           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

591           LOAD_CONST               6 ('audit_service:append_only_carry')

592           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               7 ('FAIL')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               8 ('PASS')

593   L6:     LOAD_CONST               9 ('Audit service still has no UPDATE / DELETE mutation helpers (carry-forward invariant)')

594           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE       25 (to L7)
              NOT_TAKEN
              LOAD_CONST              10 ('disqualifying tokens: ')
              LOAD_CONST              11 (', ')
              LOAD_ATTR                9 (join + NULL|self)
              LOAD_FAST_BORROW         5 (bad)
              CALL                     1
              BINARY_OP                0 (+)
              JUMP_FORWARD             1 (to L8)
      L7:     LOAD_CONST               5 ('')

590   L8:     LOAD_CONST              12 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

596           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114C60, file "scripts/pas179_controlled_learning_readiness_check.py", line 599>:
599           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_v28_sql at 0x0000018C17D7C560, file "scripts/pas179_controlled_learning_readiness_check.py", line 599>:
  --            MAKE_CELL               12 (src)

 599            RESUME                   0

 600            BUILD_LIST               0
                STORE_FAST               1 (out)

 601            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('scripts')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('migrate_v28_learning_recommendations.sql')
                BINARY_OP               11 (/)
                STORE_FAST               2 (p)

 602            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (p)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L1:     STORE_DEREF             12 (src)

 603            LOAD_DEREF              12 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_FAST               3 (lower)

 604            LOAD_CONST               3 ('proposal only')
                LOAD_FAST_BORROW         3 (lower)
                CONTAINS_OP              0 (in)
                STORE_FAST               4 (proposal_ok)

 605            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 606            LOAD_CONST               4 ('v28_sql:proposal_only')

 607            LOAD_FAST_BORROW         4 (proposal_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L2)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               6 ('FAIL')

 608    L3:     LOAD_CONST               7 ("v28 SQL carries 'PROPOSAL ONLY' guardrail")

 609            LOAD_FAST_BORROW         4 (proposal_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L4)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L5)
        L4:     LOAD_CONST               8 ("missing 'PROPOSAL ONLY' label")

 605    L5:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 611            LOAD_CONST              10 ('do not execute')
                LOAD_FAST_BORROW         3 (lower)
                CONTAINS_OP              0 (in)
                STORE_FAST               5 (do_not_exec)

 612            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 613            LOAD_CONST              11 ('v28_sql:do_not_execute')

 614            LOAD_FAST_BORROW         5 (do_not_exec)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L7)
        L6:     LOAD_CONST               6 ('FAIL')

 615    L7:     LOAD_CONST              12 ("v28 SQL carries 'DO NOT EXECUTE' trailer")

 616            LOAD_FAST_BORROW         5 (do_not_exec)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST              13 ('missing trailer')

 612    L9:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 618            LOAD_CONST              14 ('CREATE TABLE IF NOT EXISTS pas_learning_recommendations')
                LOAD_DEREF              12 (src)
                CONTAINS_OP              0 (in)
                STORE_FAST               6 (table_ok)

 619            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 620            LOAD_CONST              15 ('v28_sql:table_present')

 621            LOAD_FAST_BORROW         6 (table_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L11)
       L10:     LOAD_CONST               6 ('FAIL')

 622   L11:     LOAD_CONST              16 ('v28 SQL creates pas_learning_recommendations')

 623            LOAD_FAST_BORROW         6 (table_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L12)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L13)
       L12:     LOAD_CONST              17 ('missing CREATE TABLE')

 619   L13:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 625            LOAD_GLOBAL             10 (all)
                COPY                     1
                LOAD_COMMON_CONSTANT     3 (<built-in function all>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L17)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW        12 (src)
                BUILD_TUPLE              1
                LOAD_CONST              18 (<code object <genexpr> at 0x0000018C18025030, file "scripts/pas179_controlled_learning_readiness_check.py", line 625>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 626            LOAD_CONST              49 (("'MEMORY_UPDATE'", "'SCRIPT_BRANCH_REVIEW'", "'CALLBACK_TIMING_REVIEW'", "'LEAD_PRIORITY_REVIEW'", "'ROUTING_RULE_REVIEW'", "'OBJECTION_PATTERN_REVIEW'"))
                GET_ITER

 625            CALL                     0
       L14:     FOR_ITER                12 (to L16)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L15)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L14)
       L15:     POP_ITER
                LOAD_CONST              19 (False)
                JUMP_FORWARD            20 (to L18)
       L16:     END_FOR
                POP_ITER
                LOAD_CONST              20 (True)
                JUMP_FORWARD            16 (to L18)
       L17:     PUSH_NULL
                LOAD_FAST_BORROW        12 (src)
                BUILD_TUPLE              1
                LOAD_CONST              18 (<code object <genexpr> at 0x0000018C18025030, file "scripts/pas179_controlled_learning_readiness_check.py", line 625>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 626            LOAD_CONST              49 (("'MEMORY_UPDATE'", "'SCRIPT_BRANCH_REVIEW'", "'CALLBACK_TIMING_REVIEW'", "'LEAD_PRIORITY_REVIEW'", "'ROUTING_RULE_REVIEW'", "'OBJECTION_PATTERN_REVIEW'"))
                GET_ITER

 625            CALL                     0
                CALL                     1
       L18:     STORE_FAST               7 (rec_types_ok)

 635            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 636            LOAD_CONST              21 ('v28_sql:closed_recommendation_type_enum')

 637            LOAD_FAST_BORROW         7 (rec_types_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L19)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L20)
       L19:     LOAD_CONST               6 ('FAIL')

 638   L20:     LOAD_CONST              22 ('v28 SQL carries the closed recommendation_type enum')

 639            LOAD_FAST_BORROW         7 (rec_types_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L21)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L22)
       L21:     LOAD_CONST              23 ('missing one or more recommendation_type literals')

 635   L22:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 641            LOAD_GLOBAL             10 (all)
                COPY                     1
                LOAD_COMMON_CONSTANT     3 (<built-in function all>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L26)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW        12 (src)
                BUILD_TUPLE              1
                LOAD_CONST              24 (<code object <genexpr> at 0x0000018C18025730, file "scripts/pas179_controlled_learning_readiness_check.py", line 641>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 642            LOAD_CONST              50 (("'CANDIDATE'", "'APPROVED_FOR_MANUAL_TEST'", "'REJECTED'", "'EXPIRED'"))
                GET_ITER

 641            CALL                     0
       L23:     FOR_ITER                12 (to L25)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L24)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L23)
       L24:     POP_ITER
                LOAD_CONST              19 (False)
                JUMP_FORWARD            20 (to L27)
       L25:     END_FOR
                POP_ITER
                LOAD_CONST              20 (True)
                JUMP_FORWARD            16 (to L27)
       L26:     PUSH_NULL
                LOAD_FAST_BORROW        12 (src)
                BUILD_TUPLE              1
                LOAD_CONST              24 (<code object <genexpr> at 0x0000018C18025730, file "scripts/pas179_controlled_learning_readiness_check.py", line 641>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 642            LOAD_CONST              50 (("'CANDIDATE'", "'APPROVED_FOR_MANUAL_TEST'", "'REJECTED'", "'EXPIRED'"))
                GET_ITER

 641            CALL                     0
                CALL                     1
       L27:     STORE_FAST               8 (status_ok)

 649            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 650            LOAD_CONST              25 ('v28_sql:closed_status_enum')

 651            LOAD_FAST_BORROW         8 (status_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L28)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L29)
       L28:     LOAD_CONST               6 ('FAIL')

 652   L29:     LOAD_CONST              26 ('v28 SQL carries the closed status enum')

 653            LOAD_FAST_BORROW         8 (status_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L30)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L31)
       L30:     LOAD_CONST              27 ('missing one or more status literals')

 649   L31:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 658            LOAD_CONST              28 ('pas_learning_recommendations_tenant_no_insert')
                LOAD_DEREF              12 (src)
                CONTAINS_OP              0 (in)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       71 (to L32)
                NOT_TAKEN
                POP_TOP

 659            LOAD_CONST              29 ('pas_learning_recommendations_tenant_no_update')
                LOAD_DEREF              12 (src)
                CONTAINS_OP              0 (in)

 658            COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       58 (to L32)
                NOT_TAKEN
                POP_TOP

 660            LOAD_CONST              30 ('pas_learning_recommendations_tenant_no_delete')
                LOAD_DEREF              12 (src)
                CONTAINS_OP              0 (in)

 658            COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       45 (to L32)
                NOT_TAKEN
                POP_TOP

 661            LOAD_CONST              31 ('pas_learning_recommendations_service_role_insert')
                LOAD_DEREF              12 (src)
                CONTAINS_OP              0 (in)

 658            COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       32 (to L32)
                NOT_TAKEN
                POP_TOP

 662            LOAD_CONST              32 ("WITH CHECK (status = 'CANDIDATE')")
                LOAD_DEREF              12 (src)
                CONTAINS_OP              0 (in)

 658            COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L32)
                NOT_TAKEN
                POP_TOP

 663            LOAD_CONST              33 ('pas_learning_recommendations_service_role_review_update')
                LOAD_DEREF              12 (src)
                CONTAINS_OP              0 (in)

 658            COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        6 (to L32)
                NOT_TAKEN
                POP_TOP

 664            LOAD_CONST              34 ('pas_learning_recommendations_service_role_no_delete')
                LOAD_DEREF              12 (src)
                CONTAINS_OP              0 (in)

 657   L32:     STORE_FAST               9 (policies_ok)

 666            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 667            LOAD_CONST              35 ('v28_sql:append_only_with_review_update')

 668            LOAD_FAST_BORROW         9 (policies_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L33)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L34)
       L33:     LOAD_CONST               6 ('FAIL')

 669   L34:     LOAD_CONST              36 ('v28 SQL denies tenant writes; service_role INSERT CANDIDATE-only; restricted operator UPDATE; no DELETE')

 670            LOAD_FAST_BORROW         9 (policies_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L35)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L36)
       L35:     LOAD_CONST              37 ('missing one or more required policies')

 666   L36:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 673            LOAD_CONST              38 ('pas_learning_recommendations_tenant_select')
                LOAD_DEREF              12 (src)
                CONTAINS_OP              0 (in)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        6 (to L37)
                NOT_TAKEN
                POP_TOP

 674            LOAD_CONST              39 ("brokerage_id = (auth.jwt() ->> 'brokerage_id')")
                LOAD_DEREF              12 (src)
                CONTAINS_OP              0 (in)

 672   L37:     STORE_FAST              10 (select_scoped)

 676            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 677            LOAD_CONST              40 ('v28_sql:tenant_select_scoped')

 678            LOAD_FAST_BORROW        10 (select_scoped)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L38)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L39)
       L38:     LOAD_CONST               6 ('FAIL')

 679   L39:     LOAD_CONST              41 ('v28 SQL scopes tenant SELECT to own brokerage_id')

 680            LOAD_FAST_BORROW        10 (select_scoped)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L40)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L41)
       L40:     LOAD_CONST              42 ('missing tenant SELECT policy with brokerage_id scope')

 676   L41:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 684            LOAD_CONST              43 ('>= 0 AND confidence_score <= 1')
                LOAD_DEREF              12 (src)
                CONTAINS_OP              0 (in)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L42)
                NOT_TAKEN
                POP_TOP

 685            LOAD_CONST              44 ('>= 0 AND risk_score <= 1')
                LOAD_DEREF              12 (src)
                CONTAINS_OP              0 (in)

 684            COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        6 (to L42)
                NOT_TAKEN
                POP_TOP

 686            LOAD_CONST              45 ('>= 0 AND usefulness_score <= 1')
                LOAD_DEREF              12 (src)
                CONTAINS_OP              0 (in)

 683   L42:     STORE_FAST              11 (score_chk)

 688            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 689            LOAD_CONST              46 ('v28_sql:score_bounds')

 690            LOAD_FAST_BORROW        11 (score_chk)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L43)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L44)
       L43:     LOAD_CONST               6 ('FAIL')

 691   L44:     LOAD_CONST              47 ('v28 SQL pins confidence/risk/usefulness scores to [0,1]')

 692            LOAD_FAST_BORROW        11 (score_chk)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L45)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L46)
       L45:     LOAD_CONST              48 ('missing one or more score range CHECKs')

 688   L46:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 694            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18025030, file "scripts/pas179_controlled_learning_readiness_check.py", line 625>:
  --           COPY_FREE_VARS           1

 625           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 626   L2:     FOR_ITER                 9 (to L3)
               STORE_FAST_LOAD_FAST    17 (s, s)
               LOAD_DEREF               2 (src)
               CONTAINS_OP              0 (in)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           11 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C18025730, file "scripts/pas179_controlled_learning_readiness_check.py", line 641>:
  --           COPY_FREE_VARS           1

 641           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 642   L2:     FOR_ITER                 9 (to L3)
               STORE_FAST_LOAD_FAST    17 (s, s)
               LOAD_DEREF               2 (src)
               CONTAINS_OP              0 (in)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           11 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18114D50, file "scripts/pas179_controlled_learning_readiness_check.py", line 697>:
697           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_v29_sql at 0x0000018C17F79F10, file "scripts/pas179_controlled_learning_readiness_check.py", line 697>:
  --            MAKE_CELL               13 (src)

 697            RESUME                   0

 698            BUILD_LIST               0
                STORE_FAST               1 (out)

 699            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('scripts')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('migrate_v29_simulation_runs.sql')
                BINARY_OP               11 (/)
                STORE_FAST               2 (p)

 700            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (p)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L1:     STORE_DEREF             13 (src)

 701            LOAD_DEREF              13 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_FAST               3 (lower)

 702            LOAD_CONST               3 ('proposal only')
                LOAD_FAST_BORROW         3 (lower)
                CONTAINS_OP              0 (in)
                STORE_FAST               4 (proposal_ok)

 703            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 704            LOAD_CONST               4 ('v29_sql:proposal_only')

 705            LOAD_FAST_BORROW         4 (proposal_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L2)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               6 ('FAIL')

 706    L3:     LOAD_CONST               7 ("v29 SQL carries 'PROPOSAL ONLY' guardrail")

 707            LOAD_FAST_BORROW         4 (proposal_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L4)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L5)
        L4:     LOAD_CONST               8 ("missing 'PROPOSAL ONLY' label")

 703    L5:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 709            LOAD_CONST              10 ('do not execute')
                LOAD_FAST_BORROW         3 (lower)
                CONTAINS_OP              0 (in)
                STORE_FAST               5 (do_not_exec)

 710            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 711            LOAD_CONST              11 ('v29_sql:do_not_execute')

 712            LOAD_FAST_BORROW         5 (do_not_exec)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L7)
        L6:     LOAD_CONST               6 ('FAIL')

 713    L7:     LOAD_CONST              12 ("v29 SQL carries 'DO NOT EXECUTE' trailer")

 714            LOAD_FAST_BORROW         5 (do_not_exec)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST              13 ('missing trailer')

 710    L9:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 716            LOAD_CONST              14 ('CREATE TABLE IF NOT EXISTS pas_simulation_runs')
                LOAD_DEREF              13 (src)
                CONTAINS_OP              0 (in)
                STORE_FAST               6 (table_ok)

 717            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 718            LOAD_CONST              15 ('v29_sql:table_present')

 719            LOAD_FAST_BORROW         6 (table_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L11)
       L10:     LOAD_CONST               6 ('FAIL')

 720   L11:     LOAD_CONST              16 ('v29 SQL creates pas_simulation_runs')

 721            LOAD_FAST_BORROW         6 (table_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L12)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L13)
       L12:     LOAD_CONST              17 ('missing CREATE TABLE')

 717   L13:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 723            LOAD_GLOBAL             10 (all)
                COPY                     1
                LOAD_COMMON_CONSTANT     3 (<built-in function all>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L17)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW        13 (src)
                BUILD_TUPLE              1
                LOAD_CONST              18 (<code object <genexpr> at 0x0000018C18025C30, file "scripts/pas179_controlled_learning_readiness_check.py", line 723>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 724            LOAD_CONST              49 (("'LEAD_RESPONSE'", "'OBJECTION_HANDLING'", "'CALLBACK_FLOW'", "'BOOKING_FLOW'", "'DUPLICATE_SUPPRESSION'", "'WORKER_FAILURE'", "'PROVIDER_FAILURE'", "'MEMORY_INJECTION_EFFECT'"))
                GET_ITER

 723            CALL                     0
       L14:     FOR_ITER                12 (to L16)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L15)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L14)
       L15:     POP_ITER
                LOAD_CONST              19 (False)
                JUMP_FORWARD            20 (to L18)
       L16:     END_FOR
                POP_ITER
                LOAD_CONST              20 (True)
                JUMP_FORWARD            16 (to L18)
       L17:     PUSH_NULL
                LOAD_FAST_BORROW        13 (src)
                BUILD_TUPLE              1
                LOAD_CONST              18 (<code object <genexpr> at 0x0000018C18025C30, file "scripts/pas179_controlled_learning_readiness_check.py", line 723>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 724            LOAD_CONST              49 (("'LEAD_RESPONSE'", "'OBJECTION_HANDLING'", "'CALLBACK_FLOW'", "'BOOKING_FLOW'", "'DUPLICATE_SUPPRESSION'", "'WORKER_FAILURE'", "'PROVIDER_FAILURE'", "'MEMORY_INJECTION_EFFECT'"))
                GET_ITER

 723            CALL                     0
                CALL                     1
       L18:     STORE_FAST               7 (scenario_ok)

 735            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 736            LOAD_CONST              21 ('v29_sql:closed_scenario_type_enum')

 737            LOAD_FAST_BORROW         7 (scenario_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L19)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L20)
       L19:     LOAD_CONST               6 ('FAIL')

 738   L20:     LOAD_CONST              22 ('v29 SQL carries the closed scenario_type enum')

 739            LOAD_FAST_BORROW         7 (scenario_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L21)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L22)
       L21:     LOAD_CONST              23 ('missing one or more scenario_type literals')

 735   L22:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 741            LOAD_GLOBAL             10 (all)
                COPY                     1
                LOAD_COMMON_CONSTANT     3 (<built-in function all>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L26)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW        13 (src)
                BUILD_TUPLE              1
                LOAD_CONST              24 (<code object <genexpr> at 0x0000018C18024F30, file "scripts/pas179_controlled_learning_readiness_check.py", line 741>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_CONST              50 (("'MANUAL'", "'AUTOMATIC_LOCKED'"))
                GET_ITER
                CALL                     0
       L23:     FOR_ITER                12 (to L25)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L24)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L23)
       L24:     POP_ITER
                LOAD_CONST              19 (False)
                JUMP_FORWARD            20 (to L27)
       L25:     END_FOR
                POP_ITER
                LOAD_CONST              20 (True)
                JUMP_FORWARD            16 (to L27)
       L26:     PUSH_NULL
                LOAD_FAST_BORROW        13 (src)
                BUILD_TUPLE              1
                LOAD_CONST              24 (<code object <genexpr> at 0x0000018C18024F30, file "scripts/pas179_controlled_learning_readiness_check.py", line 741>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_CONST              50 (("'MANUAL'", "'AUTOMATIC_LOCKED'"))
                GET_ITER
                CALL                     0
                CALL                     1
       L27:     STORE_FAST               8 (mode_ok)

 742            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 743            LOAD_CONST              25 ('v29_sql:closed_mode_enum')

 744            LOAD_FAST_BORROW         8 (mode_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L28)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L29)
       L28:     LOAD_CONST               6 ('FAIL')

 745   L29:     LOAD_CONST              26 ('v29 SQL carries the closed mode enum')

 746            LOAD_FAST_BORROW         8 (mode_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L30)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L31)
       L30:     LOAD_CONST              27 ('missing one or more mode literals')

 742   L31:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 748            LOAD_GLOBAL             10 (all)
                COPY                     1
                LOAD_COMMON_CONSTANT     3 (<built-in function all>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L35)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW        13 (src)
                BUILD_TUPLE              1
                LOAD_CONST              28 (<code object <genexpr> at 0x0000018C18024C30, file "scripts/pas179_controlled_learning_readiness_check.py", line 748>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 749            LOAD_CONST              51 (("'PLANNED'", "'RUNNING'", "'COMPLETED'", "'FAILED'", "'SKIPPED'"))
                GET_ITER

 748            CALL                     0
       L32:     FOR_ITER                12 (to L34)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L33)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L32)
       L33:     POP_ITER
                LOAD_CONST              19 (False)
                JUMP_FORWARD            20 (to L36)
       L34:     END_FOR
                POP_ITER
                LOAD_CONST              20 (True)
                JUMP_FORWARD            16 (to L36)
       L35:     PUSH_NULL
                LOAD_FAST_BORROW        13 (src)
                BUILD_TUPLE              1
                LOAD_CONST              28 (<code object <genexpr> at 0x0000018C18024C30, file "scripts/pas179_controlled_learning_readiness_check.py", line 748>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 749            LOAD_CONST              51 (("'PLANNED'", "'RUNNING'", "'COMPLETED'", "'FAILED'", "'SKIPPED'"))
                GET_ITER

 748            CALL                     0
                CALL                     1
       L36:     STORE_FAST               9 (status_ok)

 753            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 754            LOAD_CONST              29 ('v29_sql:closed_status_enum')

 755            LOAD_FAST_BORROW         9 (status_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L37)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L38)
       L37:     LOAD_CONST               6 ('FAIL')

 756   L38:     LOAD_CONST              30 ('v29 SQL carries the closed status enum')

 757            LOAD_FAST_BORROW         9 (status_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L39)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L40)
       L39:     LOAD_CONST              31 ('missing one or more status literals')

 753   L40:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 760            LOAD_CONST              32 ('pas_simulation_runs_tenant_no_insert')
                LOAD_DEREF              13 (src)
                CONTAINS_OP              0 (in)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       45 (to L41)
                NOT_TAKEN
                POP_TOP

 761            LOAD_CONST              33 ('pas_simulation_runs_tenant_no_update')
                LOAD_DEREF              13 (src)
                CONTAINS_OP              0 (in)

 760            COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       32 (to L41)
                NOT_TAKEN
                POP_TOP

 762            LOAD_CONST              34 ('pas_simulation_runs_tenant_no_delete')
                LOAD_DEREF              13 (src)
                CONTAINS_OP              0 (in)

 760            COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L41)
                NOT_TAKEN
                POP_TOP

 763            LOAD_CONST              35 ('pas_simulation_runs_service_role_no_update')
                LOAD_DEREF              13 (src)
                CONTAINS_OP              0 (in)

 760            COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        6 (to L41)
                NOT_TAKEN
                POP_TOP

 764            LOAD_CONST              36 ('pas_simulation_runs_service_role_no_delete')
                LOAD_DEREF              13 (src)
                CONTAINS_OP              0 (in)

 759   L41:     STORE_FAST              10 (append_only_ok)

 766            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 767            LOAD_CONST              37 ('v29_sql:append_only_policies')

 768            LOAD_FAST_BORROW        10 (append_only_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L42)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L43)
       L42:     LOAD_CONST               6 ('FAIL')

 769   L43:     LOAD_CONST              38 ('v29 SQL denies tenant writes + service_role UPDATE/DELETE')

 770            LOAD_FAST_BORROW        10 (append_only_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L44)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L45)
       L44:     LOAD_CONST              39 ('missing one or more no-update/no-delete/no-insert policies')

 766   L45:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 773            LOAD_CONST              40 ('pas_simulation_runs_tenant_select')
                LOAD_DEREF              13 (src)
                CONTAINS_OP              0 (in)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        6 (to L46)
                NOT_TAKEN
                POP_TOP

 774            LOAD_CONST              41 ("brokerage_id = (auth.jwt() ->> 'brokerage_id')")
                LOAD_DEREF              13 (src)
                CONTAINS_OP              0 (in)

 772   L46:     STORE_FAST              11 (select_scoped)

 776            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 777            LOAD_CONST              42 ('v29_sql:tenant_select_scoped')

 778            LOAD_FAST_BORROW        11 (select_scoped)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L47)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L48)
       L47:     LOAD_CONST               6 ('FAIL')

 779   L48:     LOAD_CONST              43 ('v29 SQL scopes tenant SELECT to own brokerage_id')

 780            LOAD_FAST_BORROW        11 (select_scoped)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L49)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L50)
       L49:     LOAD_CONST              44 ('missing tenant SELECT policy')

 776   L50:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 782            LOAD_CONST              45 ("'^[0-9a-f]{64}$'")
                LOAD_DEREF              13 (src)
                CONTAINS_OP              0 (in)
                STORE_FAST              12 (sha_chk)

 783            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 784            LOAD_CONST              46 ('v29_sql:fingerprint_check_constraint')

 785            LOAD_FAST_BORROW        12 (sha_chk)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L51)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L52)
       L51:     LOAD_CONST               6 ('FAIL')

 786   L52:     LOAD_CONST              47 ('v29 SQL pins fingerprint columns to sha256 hex shape')

 787            LOAD_FAST_BORROW        12 (sha_chk)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L53)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L54)
       L53:     LOAD_CONST              48 ('missing ^[0-9a-f]{64}$ regex')

 783   L54:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 789            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18025C30, file "scripts/pas179_controlled_learning_readiness_check.py", line 723>:
  --           COPY_FREE_VARS           1

 723           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 724   L2:     FOR_ITER                 9 (to L3)
               STORE_FAST_LOAD_FAST    17 (s, s)
               LOAD_DEREF               2 (src)
               CONTAINS_OP              0 (in)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           11 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C18024F30, file "scripts/pas179_controlled_learning_readiness_check.py", line 741>:
  --           COPY_FREE_VARS           1

 741           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                 9 (to L3)
               STORE_FAST_LOAD_FAST    17 (s, s)
               LOAD_DEREF               2 (src)
               CONTAINS_OP              0 (in)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           11 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C18024C30, file "scripts/pas179_controlled_learning_readiness_check.py", line 748>:
  --           COPY_FREE_VARS           1

 748           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 749   L2:     FOR_ITER                 9 (to L3)
               STORE_FAST_LOAD_FAST    17 (s, s)
               LOAD_DEREF               2 (src)
               CONTAINS_OP              0 (in)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           11 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18114E40, file "scripts/pas179_controlled_learning_readiness_check.py", line 792>:
792           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_event_contract at 0x0000018C1801C9E0, file "scripts/pas179_controlled_learning_readiness_check.py", line 792>:
792           RESUME                   0

793           BUILD_LIST               0
              STORE_FAST               1 (out)

794           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('services')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('events')
              BINARY_OP               11 (/)
              LOAD_CONST               3 ('contract.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

795           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

796           LOAD_GLOBAL              4 (REQUIRED_EVENT_TYPES)
              GET_ITER
      L2:     FOR_ITER                67 (to L7)
              STORE_FAST               4 (required)

797           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (required, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

798           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

799           LOAD_CONST               5 ('events:')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

800           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               6 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               7 ('FAIL')

801   L4:     LOAD_CONST               8 ('Event contract registers ')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

802           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             5 (to L6)
      L5:     LOAD_CONST               9 ('missing event type ')
              LOAD_FAST_BORROW         4 (required)
              CONVERT_VALUE            2 (repr)
              FORMAT_SIMPLE
              BUILD_STRING             2

798   L6:     LOAD_CONST              10 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           69 (to L2)

796   L7:     END_FOR
              POP_ITER

804           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114F30, file "scripts/pas179_controlled_learning_readiness_check.py", line 807>:
807           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_no_forbidden_imports at 0x0000018C17F73CD0, file "scripts/pas179_controlled_learning_readiness_check.py", line 807>:
807            RESUME                   0

808            BUILD_LIST               0
               STORE_FAST               1 (out)

809            LOAD_CONST              10 (('app/services/learning/learning_policy.py', 'app/services/learning/scenario_contracts.py', 'app/services/learning/outcome_feedback.py', 'app/services/learning/recommendation_engine.py', 'app/services/learning/guardrails.py', 'scripts/pas179_controlled_learning_readiness_check.py'))
               STORE_FAST               2 (files)

817            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     EXTENDED_ARG             1
               FOR_ITER               292 (to L15)
               STORE_FAST               3 (relpath)

818            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

819            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

820            JUMP_BACKWARD           46 (to L1)

821    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

822            BUILD_LIST               0
               STORE_FAST               6 (bad)

823            LOAD_FAST_BORROW         5 (src)
               LOAD_ATTR                7 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L4:     FOR_ITER               107 (to L10)
               STORE_FAST               7 (line)

824            LOAD_FAST_BORROW         7 (line)
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               STORE_FAST               8 (stripped)

825            LOAD_FAST_BORROW         8 (stripped)
               TO_BOOL
               POP_JUMP_IF_FALSE       24 (to L5)
               NOT_TAKEN
               LOAD_FAST_BORROW         8 (stripped)
               LOAD_ATTR               11 (startswith + NULL|self)
               LOAD_CONST               2 ('#')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L6)
               NOT_TAKEN

826    L5:     JUMP_BACKWARD           52 (to L4)

827    L6:     LOAD_GLOBAL             12 (FORBIDDEN_IMPORT_LINE_PREFIXES)
               GET_ITER
       L7:     FOR_ITER                45 (to L9)
               STORE_FAST               9 (prefix)

828            LOAD_FAST_BORROW         8 (stripped)
               LOAD_ATTR               11 (startswith + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD           28 (to L7)

829    L8:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           47 (to L7)

827    L9:     END_FOR
               POP_ITER
               JUMP_BACKWARD          109 (to L4)

823   L10:     END_FOR
               POP_ITER

830            LOAD_FAST                1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             17 (_check + NULL)

831            LOAD_CONST               3 ('forbidden_import:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

832            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               4 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               5 ('PASS')

833   L12:     LOAD_CONST               6 ('No forbidden imports: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

835            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       43 (to L13)
               NOT_TAKEN

834            LOAD_CONST               7 ('forbidden import prefixes: ')
               LOAD_CONST               8 (', ')
               LOAD_ATTR               19 (join + NULL|self)
               LOAD_GLOBAL             21 (sorted + NULL)
               LOAD_GLOBAL             23 (set + NULL)
               LOAD_FAST_BORROW         6 (bad)
               CALL                     1
               CALL                     1
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L14)

835   L13:     LOAD_CONST               1 ('')

830   L14:     LOAD_CONST               9 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          295 (to L1)

817   L15:     END_FOR
               POP_ITER

837            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18115020, file "scripts/pas179_controlled_learning_readiness_check.py", line 840>:
840           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_no_inbox_scan_tokens at 0x0000018C17CC1F60, file "scripts/pas179_controlled_learning_readiness_check.py", line 840>:
840            RESUME                   0

841            BUILD_LIST               0
               STORE_FAST               1 (out)

842            LOAD_CONST               9 (('app/services/learning/learning_policy.py', 'app/services/learning/scenario_contracts.py', 'app/services/learning/outcome_feedback.py', 'app/services/learning/recommendation_engine.py', 'app/services/learning/guardrails.py'))
               STORE_FAST               2 (files)

849            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               195 (to L11)
               STORE_FAST               3 (relpath)

850            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

851            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

852            JUMP_BACKWARD           45 (to L1)

853    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

854            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         5 (src)
               CALL                     1
               STORE_FAST               6 (executable)

855            BUILD_LIST               0
               STORE_FAST               7 (bad)

856            LOAD_GLOBAL              8 (FORBIDDEN_INBOX_TOKENS)
               GET_ITER
       L4:     FOR_ITER                28 (to L6)
               STORE_FAST               8 (token)

857            LOAD_FAST_BORROW_LOAD_FAST_BORROW 134 (token, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L4)

858    L5:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_FAST_BORROW         8 (token)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L4)

856    L6:     END_FOR
               POP_ITER

859            LOAD_FAST                1 (out)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_GLOBAL             13 (_check + NULL)

860            LOAD_CONST               2 ('no_inbox_scan:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

861            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L7)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L8)
       L7:     LOAD_CONST               4 ('PASS')

862    L8:     LOAD_CONST               5 ('No inbox-scanning tokens: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

864            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L9)
               NOT_TAKEN

863            LOAD_CONST               6 ('inbox-scan tokens present: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               15 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L10)

864    L9:     LOAD_CONST               1 ('')

859   L10:     LOAD_CONST               8 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          197 (to L1)

849   L11:     END_FOR
               POP_ITER

866            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18115200, file "scripts/pas179_controlled_learning_readiness_check.py", line 869>:
869           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_doc_required_clauses at 0x0000018C17CD0CE0, file "scripts/pas179_controlled_learning_readiness_check.py", line 869>:
  --            MAKE_CELL                8 (lower)

 869            RESUME                   0

 870            BUILD_LIST               0
                STORE_FAST               1 (out)

 871            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('docs')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('pas179_controlled_learning_architecture.md')
                BINARY_OP               11 (/)
                STORE_FAST               2 (doc)

 872            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (doc)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L1:     STORE_FAST               3 (src)

 873            LOAD_FAST_BORROW         3 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_DEREF              8 (lower)

 874            LOAD_CONST              13 ((('purpose', ('purpose',)), ('pas163', ('pas163',)), ('pas178', ('pas178',)), ('manual-vs-automatic', ('manual vs automatic', 'manual / automatic', 'manual default')), ('locked-by-default', ('locked by default', 'locked-by-default')), ('no-auto-approval', ('no-auto-approval', 'no auto-approval', 'no auto approval')), ('no-live-mutation', ('no live mutation', 'no-live-mutation', 'does not mutate live')), ('scenario-simulation', ('scenario simulation', 'scenario simulation doctrine')), ('outcome-feedback', ('outcome feedback', 'outcome feedback doctrine')), ('adaptive-memory', ('adaptive memory', 'adaptive memory guardrail')), ('tenant-isolation', ('tenant isolation',)), ('future-pas180', ('pas180', 'pas181', 'pas182')), ('no-gmail', ('no gmail',)), ('limitations', ('limitation',)), ('not-built', ('intentionally not built', 'intentionally does not', 'deliberately not'))))
                STORE_FAST               4 (required_phrases)

 903            LOAD_FAST_BORROW         4 (required_phrases)
                GET_ITER
        L2:     FOR_ITER               141 (to L12)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   86 (name, phrases)

 904            LOAD_GLOBAL              6 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         8 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18026330, file "scripts/pas179_controlled_learning_readiness_check.py", line 904>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         6 (phrases)
                GET_ITER
                CALL                     0
        L3:     FOR_ITER                12 (to L5)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L3)
        L4:     POP_ITER
                LOAD_CONST               4 (True)
                JUMP_FORWARD            20 (to L7)
        L5:     END_FOR
                POP_ITER
                LOAD_CONST               5 (False)
                JUMP_FORWARD            16 (to L7)
        L6:     PUSH_NULL
                LOAD_FAST_BORROW         8 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18026330, file "scripts/pas179_controlled_learning_readiness_check.py", line 904>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         6 (phrases)
                GET_ITER
                CALL                     0
                CALL                     1
        L7:     STORE_FAST               7 (present)

 905            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 906            LOAD_CONST               6 ('docs:phrase:')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 907            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               8 ('FAIL')

 908    L9:     LOAD_CONST               9 ('Doctrine doc carries clause: ')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 910            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L10)
                NOT_TAKEN

 909            LOAD_CONST              10 ('expected one of: ')
                LOAD_CONST              11 (' | ')
                LOAD_ATTR               13 (join + NULL|self)
                LOAD_FAST_BORROW         6 (phrases)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L11)

 910   L10:     LOAD_CONST               2 ('')

 905   L11:     LOAD_CONST              12 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          143 (to L2)

 903   L12:     END_FOR
                POP_ITER

 912            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18026330, file "scripts/pas179_controlled_learning_readiness_check.py", line 904>:
  --           COPY_FREE_VARS           1

 904           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                 9 (to L3)
               STORE_FAST_LOAD_FAST    17 (p, p)
               LOAD_DEREF               2 (lower)
               CONTAINS_OP              0 (in)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           11 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C181152F0, file "scripts/pas179_controlled_learning_readiness_check.py", line 915>:
915           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_self_no_env_or_db at 0x0000018C17D88890, file "scripts/pas179_controlled_learning_readiness_check.py", line 915>:
915            RESUME                   0

916            BUILD_LIST               0
               STORE_FAST               1 (out)

917            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_GLOBAL              2 (__file__)
               CALL                     1
               LOAD_ATTR                5 (resolve + NULL|self)
               CALL                     0
               STORE_FAST               2 (self_path)

918            LOAD_GLOBAL              7 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (self_path)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L1:     STORE_FAST               3 (src)

919            LOAD_GLOBAL              9 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               4 (executable)

920            BUILD_LIST               0
               STORE_FAST               5 (bad)

921            LOAD_FAST_BORROW         4 (executable)
               LOAD_ATTR               11 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L2:     FOR_ITER               199 (to L9)
               STORE_FAST               6 (raw_line)

922            LOAD_FAST_BORROW         6 (raw_line)
               LOAD_ATTR               13 (strip + NULL|self)
               CALL                     0
               STORE_FAST               7 (stripped)

923            LOAD_FAST_BORROW         7 (stripped)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN

924            JUMP_BACKWARD           29 (to L2)

925    L3:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              15 (('import dotenv', 'from dotenv'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L4)
               NOT_TAKEN

926            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               1 ('dotenv import')
               CALL                     1
               POP_TOP

927    L4:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              16 (('import supabase', 'from supabase'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L5)
               NOT_TAKEN

928            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               2 ('supabase import')
               CALL                     1
               POP_TOP

929    L5:     LOAD_CONST               3 ('load_dotenv()')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       18 (to L6)
               NOT_TAKEN

930            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               4 ('load_dotenv() call')
               CALL                     1
               POP_TOP

931    L6:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              17 (('os.environ[', 'getenv('))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L7)
               NOT_TAKEN

932            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               5 ('environ read')
               CALL                     1
               POP_TOP

933    L7:     LOAD_CONST               6 ('get_supabase')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD          182 (to L2)

934    L8:     LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               7 ('supabase client call')
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          201 (to L2)

921    L9:     END_FOR
               POP_ITER

935            LOAD_FAST                1 (out)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_GLOBAL             19 (_check + NULL)

936            LOAD_CONST               8 ('self_check:no_env_or_db')

937            LOAD_FAST_BORROW         5 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST               9 ('FAIL')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST              10 ('PASS')

938   L11:     LOAD_CONST              11 ('PAS179 readiness checker never reads .env / touches DB')

939            LOAD_FAST_BORROW         5 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L12)
               NOT_TAKEN
               LOAD_CONST              12 ('disqualifying patterns: ')
               LOAD_CONST              13 (', ')
               LOAD_ATTR               21 (join + NULL|self)
               LOAD_FAST_BORROW         5 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L13)
      L12:     LOAD_CONST               0 ('')

935   L13:     LOAD_CONST              14 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

941            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181153E0, file "scripts/pas179_controlled_learning_readiness_check.py", line 948>:
948           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('checks')
              LOAD_CONST               2 ('List[dict]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('dict')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _aggregate at 0x0000018C1800B0A0, file "scripts/pas179_controlled_learning_readiness_check.py", line 948>:
 948            RESUME                   0

 950            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 949            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2

 950    L2:     FOR_ITER                49 (to L7)
                STORE_FAST               1 (c)

 951            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 950    L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L2)

 951    L4:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              2 (SEVERITY_BLOCK)
                COMPARE_OP              88 (bool(==))

 950    L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L2)
        L6:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L2)
        L7:     END_FOR
                POP_ITER

 949    L8:     STORE_FAST               2 (blockers)
                STORE_FAST               1 (c)

 954            LOAD_CONST               3 ('verdict')
                LOAD_FAST_BORROW         2 (blockers)
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L9)
                NOT_TAKEN
                LOAD_GLOBAL              4 (VERDICT_NOT_READY)
                JUMP_FORWARD             5 (to L10)
        L9:     LOAD_GLOBAL              6 (VERDICT_READY)

 955   L10:     LOAD_CONST               4 ('blockers')
                LOAD_FAST_BORROW         2 (blockers)

 956            LOAD_CONST               5 ('info')
                BUILD_LIST               0

 953            BUILD_MAP                3
                RETURN_VALUE

  --   L11:     SWAP                     2
                POP_TOP

 949            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L11 [2]
  L4 to L5 -> L11 [2]
  L6 to L8 -> L11 [2]

Disassembly of <code object __annotate__ at 0x0000018C181154D0, file "scripts/pas179_controlled_learning_readiness_check.py", line 960>:
960           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('checks')
              LOAD_CONST               2 ('List[dict]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _operator_actions at 0x0000018C18048C70, file "scripts/pas179_controlled_learning_readiness_check.py", line 960>:
960           RESUME                   0

961           BUILD_LIST               0
              STORE_FAST               1 (out)

962           LOAD_FAST_BORROW         0 (checks)
              GET_ITER
      L1:     FOR_ITER               109 (to L5)
              STORE_FAST               2 (c)

963           LOAD_FAST_BORROW         2 (c)
              LOAD_CONST               0 ('status')
              BINARY_OP               26 ([])
              LOAD_CONST               1 ('FAIL')
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

964           JUMP_BACKWARD           19 (to L1)

965   L2:     LOAD_FAST_BORROW         2 (c)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               2 ('severity')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         7 (to L3)
              NOT_TAKEN
              POP_TOP
              LOAD_GLOBAL              2 (SEVERITY_BLOCK)
      L3:     STORE_FAST               3 (sev)

966           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_CONST               3 ('[')
              LOAD_FAST                3 (sev)
              FORMAT_SIMPLE
              LOAD_CONST               4 ('] ')
              LOAD_FAST_BORROW         2 (c)
              LOAD_CONST               5 ('id')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' — ')
              LOAD_FAST_BORROW         2 (c)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               7 ('detail')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               8 ('see report')
      L4:     FORMAT_SIMPLE
              LOAD_CONST               9 ('.')
              BUILD_STRING             7
              CALL                     1
              POP_TOP
              JUMP_BACKWARD          111 (to L1)

962   L5:     END_FOR
              POP_ITER

967           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181155C0, file "scripts/pas179_controlled_learning_readiness_check.py", line 970>:
970           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('dict')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object evaluate at 0x0000018C177C69F0, file "scripts/pas179_controlled_learning_readiness_check.py", line 970>:
 970           RESUME                   0

 971           BUILD_LIST               0
               STORE_FAST               1 (checks)

 972           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL              3 (check_files_present + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

 973           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL              5 (check_prior_phases_intact + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

 974           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL              7 (check_memory_review_intact + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

 975           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL              9 (check_worker_off_by_default + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

 976           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             11 (check_no_startup_worker + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

 977           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             13 (check_policy_service + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

 978           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             15 (check_scenario_contracts + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

 979           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             17 (check_outcome_feedback + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

 980           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             19 (check_recommendation_engine + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

 981           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             21 (check_guardrails + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

 982           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             23 (check_no_auto_approval_tokens + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

 983           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             25 (check_no_live_mutation_imports + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

 984           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             27 (check_audit_service_invariant + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

 985           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             29 (check_v28_sql + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

 986           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             31 (check_v29_sql + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

 987           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             33 (check_event_contract + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

 988           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             35 (check_no_forbidden_imports + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

 989           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             37 (check_no_inbox_scan_tokens + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

 990           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             39 (check_doc_required_clauses + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

 991           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             41 (check_self_no_env_or_db + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

 993           LOAD_GLOBAL             43 (_aggregate + NULL)
               LOAD_FAST_BORROW         1 (checks)
               CALL                     1
               STORE_FAST               2 (agg)

 995           LOAD_CONST               0 ('phase')
               LOAD_CONST               1 ('PAS179')

 996           LOAD_CONST               2 ('generated_at')
               LOAD_GLOBAL             45 (_now_iso + NULL)
               CALL                     0

 997           LOAD_CONST               3 ('verdict')
               LOAD_FAST_BORROW         2 (agg)
               LOAD_CONST               3 ('verdict')
               BINARY_OP               26 ([])

 998           LOAD_CONST               4 ('ready')
               LOAD_FAST_BORROW         2 (agg)
               LOAD_CONST               3 ('verdict')
               BINARY_OP               26 ([])
               LOAD_GLOBAL             46 (VERDICT_READY)
               COMPARE_OP              72 (==)

 999           LOAD_CONST               5 ('blocker_count')
               LOAD_GLOBAL             49 (len + NULL)
               LOAD_FAST_BORROW         2 (agg)
               LOAD_CONST               6 ('blockers')
               BINARY_OP               26 ([])
               CALL                     1

1000           LOAD_CONST               7 ('info_count')
               LOAD_GLOBAL             49 (len + NULL)
               LOAD_FAST_BORROW         2 (agg)
               LOAD_CONST               8 ('info')
               BINARY_OP               26 ([])
               CALL                     1

1001           LOAD_CONST               9 ('check_count')
               LOAD_GLOBAL             49 (len + NULL)
               LOAD_FAST_BORROW         1 (checks)
               CALL                     1

1002           LOAD_CONST              10 ('pass_count')
               LOAD_GLOBAL             51 (sum + NULL)
               LOAD_CONST              11 (<code object <genexpr> at 0x0000018C18053870, file "scripts/pas179_controlled_learning_readiness_check.py", line 1002>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         1 (checks)
               GET_ITER
               CALL                     0
               CALL                     1

1003           LOAD_CONST              12 ('fail_count')
               LOAD_GLOBAL             51 (sum + NULL)
               LOAD_CONST              13 (<code object <genexpr> at 0x0000018C18052F70, file "scripts/pas179_controlled_learning_readiness_check.py", line 1003>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         1 (checks)
               GET_ITER
               CALL                     0
               CALL                     1

1004           LOAD_CONST              14 ('checks')
               LOAD_FAST_BORROW         1 (checks)

1005           LOAD_CONST              15 ('operator_actions')
               LOAD_GLOBAL             53 (_operator_actions + NULL)
               LOAD_FAST_BORROW         1 (checks)
               CALL                     1

 994           BUILD_MAP               11
               RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18053870, file "scripts/pas179_controlled_learning_readiness_check.py", line 1002>:
1002           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                22 (to L5)
               STORE_FAST_LOAD_FAST    17 (c, c)
               LOAD_CONST               0 ('status')
               BINARY_OP               26 ([])
               LOAD_CONST               1 ('PASS')
               COMPARE_OP              88 (bool(==))
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           18 (to L2)
       L4:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           24 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C18052F70, file "scripts/pas179_controlled_learning_readiness_check.py", line 1003>:
1003           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                22 (to L5)
               STORE_FAST_LOAD_FAST    17 (c, c)
               LOAD_CONST               0 ('status')
               BINARY_OP               26 ([])
               LOAD_CONST               1 ('FAIL')
               COMPARE_OP              88 (bool(==))
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           18 (to L2)
       L4:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           24 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18115980, file "scripts/pas179_controlled_learning_readiness_check.py", line 1012>:
1012           RESUME                   0
               LOAD_FAST_BORROW         0 (format)
               LOAD_SMALL_INT           2
               COMPARE_OP             132 (>)
               POP_JUMP_IF_FALSE        3 (to L1)
               NOT_TAKEN
               LOAD_COMMON_CONSTANT     1 (NotImplementedError)
               RAISE_VARARGS            1
       L1:     LOAD_CONST               1 ('return')
               LOAD_CONST               2 ('argparse.ArgumentParser')
               BUILD_MAP                1
               RETURN_VALUE

Disassembly of <code object _build_parser at 0x0000018C180FC210, file "scripts/pas179_controlled_learning_readiness_check.py", line 1012>:
1012           RESUME                   0

1013           LOAD_GLOBAL              0 (argparse)
               LOAD_ATTR                2 (ArgumentParser)
               PUSH_NULL

1014           LOAD_CONST               0 ('pas179_controlled_learning_readiness_check')

1016           LOAD_CONST               1 ('PAS179 — Evaluate controlled-learning architecture + scenario simulation contracts + guardrails. Read-only — never reads .env, never touches Supabase, never runs a migration.')

1013           LOAD_CONST               2 (('prog', 'description'))
               CALL_KW                  2
               STORE_FAST               0 (p)

1022           LOAD_FAST_BORROW         0 (p)
               LOAD_ATTR                5 (add_argument + NULL|self)
               LOAD_CONST               3 ('--repo-root')
               LOAD_GLOBAL              6 (_REPO_ROOT_DEFAULT)
               LOAD_CONST               4 (('default',))
               CALL_KW                  2
               POP_TOP

1023           LOAD_FAST_BORROW         0 (p)
               LOAD_ATTR                5 (add_argument + NULL|self)
               LOAD_CONST               5 ('--output')
               LOAD_GLOBAL              8 (REPORT_FILENAME)
               LOAD_CONST               4 (('default',))
               CALL_KW                  2
               POP_TOP

1024           LOAD_FAST_BORROW         0 (p)
               LOAD_ATTR                5 (add_argument + NULL|self)
               LOAD_CONST               6 ('--json')
               LOAD_CONST               7 ('store_true')
               LOAD_CONST               8 (('action',))
               CALL_KW                  2
               POP_TOP

1025           LOAD_FAST_BORROW         0 (p)
               LOAD_ATTR                5 (add_argument + NULL|self)
               LOAD_CONST               9 ('--summary-only')
               LOAD_CONST               7 ('store_true')
               LOAD_CONST               8 (('action',))
               CALL_KW                  2
               POP_TOP

1026           LOAD_FAST_BORROW         0 (p)
               LOAD_ATTR                5 (add_argument + NULL|self)
               LOAD_CONST              10 ('--strict')
               LOAD_CONST               7 ('store_true')
               LOAD_CONST               8 (('action',))
               CALL_KW                  2
               POP_TOP

1027           LOAD_FAST_BORROW         0 (p)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18115A70, file "scripts/pas179_controlled_learning_readiness_check.py", line 1030>:
1030           RESUME                   0
               LOAD_FAST_BORROW         0 (format)
               LOAD_SMALL_INT           2
               COMPARE_OP             132 (>)
               POP_JUMP_IF_FALSE        3 (to L1)
               NOT_TAKEN
               LOAD_COMMON_CONSTANT     1 (NotImplementedError)
               RAISE_VARARGS            1
       L1:     LOAD_CONST               1 ('report')
               LOAD_CONST               2 ('dict')
               LOAD_CONST               3 ('return')
               LOAD_CONST               4 ('None')
               BUILD_MAP                2
               RETURN_VALUE

Disassembly of <code object _print_summary at 0x0000018C17D8C5C0, file "scripts/pas179_controlled_learning_readiness_check.py", line 1030>:
1030           RESUME                   0

1031           LOAD_GLOBAL              1 (print + NULL)

1032           LOAD_CONST               0 ('[PAS179] verdict=')
               LOAD_FAST_BORROW         0 (report)
               LOAD_CONST               1 ('verdict')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               LOAD_CONST               2 (' blockers=')

1033           LOAD_FAST_BORROW         0 (report)
               LOAD_CONST               3 ('blocker_count')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               LOAD_CONST               4 (' info=')

1034           LOAD_FAST_BORROW         0 (report)
               LOAD_CONST               5 ('info_count')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               LOAD_CONST               6 (' checks=')

1035           LOAD_FAST_BORROW         0 (report)
               LOAD_CONST               7 ('check_count')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               LOAD_CONST               8 (' pass=')

1036           LOAD_FAST_BORROW         0 (report)
               LOAD_CONST               9 ('pass_count')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               LOAD_CONST              10 (' fail=')

1037           LOAD_FAST_BORROW         0 (report)
               LOAD_CONST              11 ('fail_count')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE

1032           BUILD_STRING            12

1031           CALL                     1
               POP_TOP

1039           LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              12 ('operator_actions')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               BUILD_LIST               0
       L1:     STORE_FAST               1 (actions)

1040           LOAD_FAST_BORROW         1 (actions)
               TO_BOOL
               POP_JUMP_IF_FALSE       93 (to L5)
               NOT_TAKEN

1041           LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST              13 ('[PAS179] operator actions:')
               CALL                     1
               POP_TOP

1042           LOAD_FAST_BORROW         1 (actions)
               LOAD_CONST              14 (slice(None, 25, None))
               BINARY_OP               26 ([])
               GET_ITER
       L2:     FOR_ITER                17 (to L3)
               STORE_FAST               2 (a)

1043           LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST              15 ('  - ')
               LOAD_FAST_BORROW         2 (a)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           19 (to L2)

1042   L3:     END_FOR
               POP_ITER

1044           LOAD_GLOBAL              5 (len + NULL)
               LOAD_FAST_BORROW         1 (actions)
               CALL                     1
               LOAD_SMALL_INT          25
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE       34 (to L4)
               NOT_TAKEN

1045           LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST              16 ('  ... and ')
               LOAD_GLOBAL              5 (len + NULL)
               LOAD_FAST_BORROW         1 (actions)
               CALL                     1
               LOAD_SMALL_INT          25
               BINARY_OP               10 (-)
               FORMAT_SIMPLE
               LOAD_CONST              17 (' more (see report file)')
               BUILD_STRING             3
               CALL                     1
               POP_TOP
               LOAD_CONST              18 (None)
               RETURN_VALUE

1044   L4:     LOAD_CONST              18 (None)
               RETURN_VALUE

1040   L5:     LOAD_CONST              18 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025230, file "scripts/pas179_controlled_learning_readiness_check.py", line 1048>:
1048           RESUME                   0
               LOAD_FAST_BORROW         0 (format)
               LOAD_SMALL_INT           2
               COMPARE_OP             132 (>)
               POP_JUMP_IF_FALSE        3 (to L1)
               NOT_TAKEN
               LOAD_COMMON_CONSTANT     1 (NotImplementedError)
               RAISE_VARARGS            1
       L1:     LOAD_CONST               1 ('path')
               LOAD_CONST               2 ('str')
               LOAD_CONST               3 ('payload')
               LOAD_CONST               4 ('dict')
               LOAD_CONST               5 ('return')
               LOAD_CONST               6 ('None')
               BUILD_MAP                3
               RETURN_VALUE

Disassembly of <code object _write_report at 0x0000018C180FC990, file "scripts/pas179_controlled_learning_readiness_check.py", line 1048>:
1048           RESUME                   0

1049           NOP

1050   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

1051           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

1052           LOAD_CONST               3 ('utf-8')

1050           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

1054           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

1055   L4:     LOAD_GLOBAL             11 (print + NULL)

1056           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

1057           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

1056           BUILD_STRING             4

1058           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

1055           LOAD_CONST               7 (('file',))
               CALL_KW                  2
               POP_TOP
       L5:     POP_EXCEPT
               LOAD_CONST               8 (None)
               STORE_FAST               2 (e)
               DELETE_FAST              2 (e)
               LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               8 (None)
               STORE_FAST               2 (e)
               DELETE_FAST              2 (e)
               RERAISE                  1

1054   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18115B60, file "scripts/pas179_controlled_learning_readiness_check.py", line 1062>:
1062           RESUME                   0
               LOAD_FAST_BORROW         0 (format)
               LOAD_SMALL_INT           2
               COMPARE_OP             132 (>)
               POP_JUMP_IF_FALSE        3 (to L1)
               NOT_TAKEN
               LOAD_COMMON_CONSTANT     1 (NotImplementedError)
               RAISE_VARARGS            1
       L1:     LOAD_CONST               1 ('argv')
               LOAD_CONST               2 ('Optional[List[str]]')
               LOAD_CONST               3 ('return')
               LOAD_CONST               4 ('int')
               BUILD_MAP                2
               RETURN_VALUE

Disassembly of <code object main at 0x0000018C17D884E0, file "scripts/pas179_controlled_learning_readiness_check.py", line 1062>:
1062            RESUME                   0

1063            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

1064            NOP

1065    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

1069    L2:     LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               15 (abspath + NULL|self)
                LOAD_FAST                2 (args)
                LOAD_ATTR               16 (repo_root)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         7 (to L3)
                NOT_TAKEN
                POP_TOP
                LOAD_GLOBAL             18 (_REPO_ROOT_DEFAULT)
        L3:     CALL                     1
                STORE_FAST               4 (repo_root)

1070            LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               21 (isdir + NULL|self)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L4)
                NOT_TAKEN

1071            LOAD_GLOBAL             23 (print + NULL)
                LOAD_CONST               2 ('error: --repo-root not a directory: ')
                LOAD_FAST                4 (repo_root)
                FORMAT_SIMPLE
                BUILD_STRING             2
                LOAD_GLOBAL             24 (sys)
                LOAD_ATTR               26 (stderr)
                LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

1072            LOAD_SMALL_INT           2
                RETURN_VALUE

1074    L4:     LOAD_GLOBAL             29 (evaluate + NULL)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                STORE_FAST               5 (report)

1076            LOAD_FAST                2 (args)
                LOAD_ATTR               30 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L5)
                NOT_TAKEN

1077            LOAD_GLOBAL             33 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               34 (output)
                LOAD_FAST                5 (report)
                CALL                     2
                POP_TOP

1079    L5:     LOAD_GLOBAL             37 (_print_summary + NULL)
                LOAD_FAST                5 (report)
                CALL                     1
                POP_TOP

1081            LOAD_FAST                2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L6)
                NOT_TAKEN

1082            LOAD_GLOBAL             23 (print + NULL)
                LOAD_GLOBAL             38 (json)
                LOAD_ATTR               40 (dumps)
                PUSH_NULL
                LOAD_FAST                5 (report)
                LOAD_SMALL_INT           2
                LOAD_CONST               4 (True)
                LOAD_CONST               5 (('indent', 'sort_keys'))
                CALL_KW                  3
                CALL                     1
                POP_TOP

1084    L6:     LOAD_FAST                5 (report)
                LOAD_CONST               6 ('verdict')
                BINARY_OP               26 ([])
                LOAD_GLOBAL             42 (VERDICT_READY)
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L7)
                NOT_TAKEN
                LOAD_SMALL_INT           0
                RETURN_VALUE
        L7:     LOAD_SMALL_INT           1
                RETURN_VALUE

  --    L8:     PUSH_EXC_INFO

1066            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L17)
                NOT_TAKEN
                STORE_FAST               3 (e)

1067    L9:     LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                LOAD_CONST               7 ((0, None))
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN
                LOAD_SMALL_INT           2
                JUMP_FORWARD            30 (to L14)
       L10:     LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
       L11:     NOT_TAKEN
       L12:     POP_TOP
                LOAD_SMALL_INT           0
       L13:     CALL                     1
       L14:     SWAP                     2
       L15:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RETURN_VALUE

  --   L16:     LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

1066   L17:     RERAISE                  0

  --   L18:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L8 [0]
  L8 to L9 -> L18 [1] lasti
  L9 to L11 -> L16 [1] lasti
  L12 to L14 -> L16 [1] lasti
  L14 to L15 -> L18 [1] lasti
  L16 to L18 -> L18 [1] lasti
```
