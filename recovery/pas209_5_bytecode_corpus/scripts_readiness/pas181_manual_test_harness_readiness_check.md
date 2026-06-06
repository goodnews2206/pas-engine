# scripts_readiness/pas181_manual_test_harness_readiness_check

- **pyc:** `scripts\__pycache__\pas181_manual_test_harness_readiness_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/pas181_manual_test_harness_readiness_check.py`
- **co_filename (from bytecode):** `scripts/pas181_manual_test_harness_readiness_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS181 — Bounded manual-test execution harness readiness gate.

Deterministic, non-mutating evaluator for "is PAS181 wired
correctly and free of regressions in the PAS160-PAS180
doctrine?".

Walks the repo and verifies:

  * PAS160-PAS180 readiness scripts still exist.
  * PAS181 surfaces exist:
      - scripts/migrate_v30_learning_manual_test_runs.sql
      - app/services/learning/manual_test_harness.py
      - app/services/learning/manual_test_evidence.py
      - app/services/learning/manual_test_scoring.py
      - app/routes/operator_learning_tests.py
      - app/routes/tenant_learning_tests.py
      - scripts/pas181_manual_test_harness_readiness_check.py
      - docs/pas181_manual_test_execution_harness.md
      - tests/mvp/test_pas181_manual_test_harness.py
  * v30 SQL carries PROPOSAL ONLY + DO NOT EXECUTE + closed
    status/mode enums + sha256 fingerprint pin + RLS tenant
    SELECT scoped + service_role INSERT PLANNED-only +
    restricted operator UPDATE + no DELETE.
  * manual_test_harness exposes documented surface, eligibility
    is APPROVED_FOR_MANUAL_TEST, only SIMULATION_ONLY /
    OBSERVATIONAL_ONLY mode tokens appear.
  * manual_test_evidence exposes documented surface with
    closed allow-lists + tenant projection narrower than
    operator projection.
  * manual_test_scoring exposes documented surface +
    HIGH_RISK_THRESHOLD constant.
  * operator_learning_tests has the 5 documented routes
    under require_admin.
  * tenant_learning_tests has the 2 documented GET routes
    under require_brokerage (no POST surface).
  * No forbidden statuses (LIVE / APPLIED / AUTO_APPLIED /
    DEPLOYED) in PAS181 source.
  * No live-mutation imports.
  * No LLM / embeddings / vector / Gmail / OAuth / IMAP /
    POP3 / inbox-scanning / Composio / TrustClaw imports.
  * Memory Review (PAS147-PAS158) untouched.
  * audit_service.py STILL has no UPDATE / DELETE helpers
    (PAS174-PAS180 carry-forward).
  * PAS179 / PAS180 services intact.
  * Event contract registers every PAS181 event type.
  * main.py mounts both new routers.
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

`__annotate__`, `_aggregate`, `_build_parser`, `_check`, `_now_iso`, `_operator_actions`, `_print_summary`, `_read_text`, `_strip_python_comments_and_strings`, `_write_report`, `check_audit_service_invariant`, `check_doc_required_clauses`, `check_event_contract`, `check_evidence_service`, `check_files_present`, `check_harness_service`, `check_main_router_mounts`, `check_memory_review_intact`, `check_no_auto_approval_tokens`, `check_no_forbidden_imports`, `check_no_forbidden_status_tokens`, `check_no_inbox_scan_tokens`, `check_no_live_mutation_imports`, `check_no_startup_worker`, `check_operator_routes`, `check_prior_phases_intact`, `check_scoring_service`, `check_self_no_env_or_db`, `check_tenant_routes`, `check_v30_sql`, `check_worker_off_by_default`, `evaluate`, `main`

## Env-key candidates

`BLOCK`, `FAIL`, `NOT_READY`, `PAS181`, `PASS`, `READY`

## String constants (redacted where noted)

- '\nPAS181 — Bounded manual-test execution harness readiness gate.\n\nDeterministic, non-mutating evaluator for "is PAS181 wired\ncorrectly and free of regressions in the PAS160-PAS180\ndoctrine?".\n\nWalks the repo and verifies:\n\n  * PAS160-PAS180 readiness scripts still exist.\n  * PAS181 surfaces exist:\n      - scripts/migrate_v30_learning_manual_test_runs.sql\n      - app/services/learning/manual_test_harness.py\n      - app/services/learning/manual_test_evidence.py\n      - app/services/learning/manual_test_scoring.py\n      - app/routes/operator_learning_tests.py\n      - app/routes/tenant_learning_tests.py\n      - scripts/pas181_manual_test_harness_readiness_check.py\n      - docs/pas181_manual_test_execution_harness.md\n      - tests/mvp/test_pas181_manual_test_harness.py\n  * v30 SQL carries PROPOSAL ONLY + DO NOT EXECUTE + closed\n    status/mode enums + sha256 fingerprint pin + RLS tenant\n    SELECT scoped + service_role INSERT PLANNED-only +\n    restricted operator UPDATE + no DELETE.\n  * manual_test_harness exposes documented surface, eligibility\n    is APPROVED_FOR_MANUAL_TEST, only SIMULATION_ONLY /\n    OBSERVATIONAL_ONLY mode tokens appear.\n  * manual_test_evidence exposes documented surface with\n    closed allow-lists + tenant projection narrower than\n    operator projection.\n  * manual_test_scoring exposes documented surface +\n    HIGH_RISK_THRESHOLD constant.\n  * operator_learning_tests has the 5 documented routes\n    under require_admin.\n  * tenant_learning_tests has the 2 documented GET routes\n    under require_brokerage (no POST surface).\n  * No forbidden statuses (LIVE / APPLIED / AUTO_APPLIED /\n    DEPLOYED) in PAS181 source.\n  * No live-mutation imports.\n  * No LLM / embeddings / vector / Gmail / OAuth / IMAP /\n    POP3 / inbox-scanning / Composio / TrustClaw imports.\n  * Memory Review (PAS147-PAS158) untouched.\n  * audit_service.py STILL has no UPDATE / DELETE helpers\n    (PAS174-PAS180 carry-forward).\n  * PAS179 / PAS180 services intact.\n  * Event contract registers every PAS181 event type.\n  * main.py mounts both new routers.\n  * Worker still OFF by default; FastAPI lifespan does not\n    auto-start the worker.\n  * Supports --summary-only / --json.\n  * Exits 0 ready, 1 blockers, 2 bad args.\n  * Never reads .env.\n  * Never touches production data.\n'
- 'utf-8'
- 'READY'
- 'NOT_READY'
- 'BLOCK'
- 'severity'
- 'detail'
- 'pas181_manual_test_harness_readiness_report.json'
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
- 'Required PAS181 file present: '
- 'missing'
- 'prior_phase:'
- 'Prior-phase readiness script intact: '
- 'missing — PAS181 must not delete'
- 'pas179_180_service:'
- 'PAS179/PAS180 service intact: '
- 'PAS179/PAS180 service deleted — PAS181 must not touch'
- 'memory_review:'
- 'Memory Review file present: '
- 'Memory Review file deleted — PAS181 must not touch'
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
- 'manual_test_harness.py'
- 'harness:'
- 'Manual-test harness token: '
- 'missing token '
- 'manual_test_evidence.py'
- 'evidence:'
- 'Manual-test evidence token: '
- 'manual_test_scoring.py'
- 'scoring:'
- 'Manual-test scoring token: '
- 'routes'
- 'operator_learning_tests.py'
- 'operator_routes:'
- 'Operator-test route token: '
- 'require_admin'
- 'x_admin_key'
- 'operator_routes:require_admin'
- 'Operator-test routes use require_admin (X-Admin-Key)'
- 'missing require_admin / X-Admin-Key tokens'
- 'tenant_learning_tests.py'
- 'tenant_routes:'
- 'Tenant-test route token: '
- 'require_brokerage'
- 'x_api_key'
- 'tenant_routes:tenant_auth_only'
- 'Tenant-test routes use X-API-Key (require_brokerage), never admin'
- 'missing require_brokerage / x_api_key tokens'
- '@router.post'
- 'tenant_routes:no_mutation_surface'
- 'Tenant-test routes have NO @router.post surface'
- 'tenant route file declares a POST route'
- 'app/services/learning/manual_test_harness.py'
- 'no_forbidden_status:'
- 'No forbidden status tokens: '
- 'no_auto_approval:'
- 'No auto-approval / live-mutation tokens: '
- 'no_live_mutation_import:'
- 'No live-mutation imports: '
- 'forbidden imports: '
- 'PAS174-PAS180 invariant: audit_service has no\nUPDATE / DELETE helpers. PAS181 must preserve.'
- 'operator'
- 'audit_service.py'
- 'audit_service:append_only_carry'
- 'Audit service still has no UPDATE / DELETE mutation helpers (carry-forward invariant)'
- 'scripts'
- 'migrate_v30_learning_manual_test_runs.sql'
- 'proposal only'
- 'v30_sql:proposal_only'
- "v30 SQL carries 'PROPOSAL ONLY' guardrail"
- "missing 'PROPOSAL ONLY' label"
- 'do not execute'
- 'v30_sql:do_not_execute'
- "v30 SQL carries 'DO NOT EXECUTE' trailer"
- 'missing trailer'
- 'CREATE TABLE IF NOT EXISTS pas_learning_manual_test_runs'
- 'v30_sql:table_present'
- 'v30 SQL creates pas_learning_manual_test_runs'
- 'missing CREATE TABLE'
- 'v30_sql:closed_status_enum'
- 'v30 SQL carries the closed status enum'
- 'missing one or more status literals'
- 'v30_sql:no_forbidden_status'
- 'v30 SQL must not carry forbidden status tokens (LIVE / APPLIED / AUTO_APPLIED / DEPLOYED)'
- 'forbidden status literal present'
- 'v30_sql:closed_mode_enum'
- 'v30 SQL carries the closed mode enum'
- 'missing one or more mode literals'
- "'^[0-9a-f]{64}$'"
- 'v30_sql:fingerprint_check_constraint'
- 'v30 SQL pins evidence_fingerprint to sha256 hex shape'
- 'missing ^[0-9a-f]{64}$ regex'
- 'pas_learning_manual_test_runs_tenant_no_insert'
- 'pas_learning_manual_test_runs_tenant_no_update'
- 'pas_learning_manual_test_runs_tenant_no_delete'
- 'pas_learning_manual_test_runs_service_role_no_delete'
- 'pas_learning_manual_test_runs_service_role_review_update'
- "WITH CHECK (status = 'PLANNED')"
- 'v30_sql:append_only_with_review_update'
- 'v30 SQL denies tenant writes; service_role INSERT PLANNED-only; restricted operator UPDATE; no DELETE'
- 'missing one or more required policies'
- 'pas_learning_manual_test_runs_tenant_select'
- "brokerage_id = (auth.jwt() ->> 'brokerage_id')"
- 'v30_sql:tenant_select_scoped'
- 'v30 SQL scopes tenant SELECT to own brokerage_id'
- 'missing tenant SELECT policy'
- '>= 0 AND score <= 1'
- '>= 0 AND confidence_score <= 1'
- '>= 0 AND risk_score <= 1'
- 'v30_sql:score_bounds'
- 'v30 SQL pins score/confidence/risk to [0,1]'
- 'missing one or more score range CHECKs'
- 'events'
- 'contract.py'
- 'events:'
- 'Event contract registers '
- 'missing event type '
- 'main:mount:'
- 'app/main.py mounts '
- 'missing mount token '
- 'forbidden_import:'
- 'No forbidden imports: '
- 'forbidden import prefixes: '
- 'no_inbox_scan:'
- 'No inbox-scanning tokens: '
- 'inbox-scan tokens present: '
- 'docs'
- 'pas181_manual_test_execution_harness.md'
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
- 'PAS181 readiness checker never reads .env / touches DB'
- 'disqualifying patterns: '
- 'checks'
- 'verdict'
- 'blockers'
- 'info'
- 'List[str]'
- ' — '
- 'see report'
- 'phase'
- 'PAS181'
- 'generated_at'
- 'ready'
- 'blocker_count'
- 'info_count'
- 'check_count'
- 'pass_count'
- 'fail_count'
- 'operator_actions'
- 'argparse.ArgumentParser'
- 'pas181_manual_test_harness_readiness_check'
- 'PAS181 — Evaluate bounded manual-test execution harness (services + routes + audit trail). Read-only — never reads .env, never touches Supabase, never runs a migration.'
- '--repo-root'
- '--output'
- '--json'
- 'store_true'
- '--summary-only'
- '--strict'
- 'report'
- 'None'
- '[PAS181] verdict='
- ' blockers='
- ' info='
- ' checks='
- ' pass='
- ' fail='
- '[PAS181] operator actions:'
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

   1           LOAD_CONST               0 ('\nPAS181 — Bounded manual-test execution harness readiness gate.\n\nDeterministic, non-mutating evaluator for "is PAS181 wired\ncorrectly and free of regressions in the PAS160-PAS180\ndoctrine?".\n\nWalks the repo and verifies:\n\n  * PAS160-PAS180 readiness scripts still exist.\n  * PAS181 surfaces exist:\n      - scripts/migrate_v30_learning_manual_test_runs.sql\n      - app/services/learning/manual_test_harness.py\n      - app/services/learning/manual_test_evidence.py\n      - app/services/learning/manual_test_scoring.py\n      - app/routes/operator_learning_tests.py\n      - app/routes/tenant_learning_tests.py\n      - scripts/pas181_manual_test_harness_readiness_check.py\n      - docs/pas181_manual_test_execution_harness.md\n      - tests/mvp/test_pas181_manual_test_harness.py\n  * v30 SQL carries PROPOSAL ONLY + DO NOT EXECUTE + closed\n    status/mode enums + sha256 fingerprint pin + RLS tenant\n    SELECT scoped + service_role INSERT PLANNED-only +\n    restricted operator UPDATE + no DELETE.\n  * manual_test_harness exposes documented surface, eligibility\n    is APPROVED_FOR_MANUAL_TEST, only SIMULATION_ONLY /\n    OBSERVATIONAL_ONLY mode tokens appear.\n  * manual_test_evidence exposes documented surface with\n    closed allow-lists + tenant projection narrower than\n    operator projection.\n  * manual_test_scoring exposes documented surface +\n    HIGH_RISK_THRESHOLD constant.\n  * operator_learning_tests has the 5 documented routes\n    under require_admin.\n  * tenant_learning_tests has the 2 documented GET routes\n    under require_brokerage (no POST surface).\n  * No forbidden statuses (LIVE / APPLIED / AUTO_APPLIED /\n    DEPLOYED) in PAS181 source.\n  * No live-mutation imports.\n  * No LLM / embeddings / vector / Gmail / OAuth / IMAP /\n    POP3 / inbox-scanning / Composio / TrustClaw imports.\n  * Memory Review (PAS147-PAS158) untouched.\n  * audit_service.py STILL has no UPDATE / DELETE helpers\n    (PAS174-PAS180 carry-forward).\n  * PAS179 / PAS180 services intact.\n  * Event contract registers every PAS181 event type.\n  * main.py mounts both new routers.\n  * Worker still OFF by default; FastAPI lifespan does not\n    auto-start the worker.\n  * Supports --summary-only / --json.\n  * Exits 0 ready, 1 blockers, 2 bad args.\n  * Never reads .env.\n  * Never touches production data.\n')
               STORE_NAME               0 (__doc__)

  56           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  58           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  59           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (json)
               STORE_NAME               4 (json)

  60           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (os)
               STORE_NAME               5 (os)

  61           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (sys)
               STORE_NAME               6 (sys)

  62           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              7 (datetime)
               IMPORT_FROM              7 (datetime)
               STORE_NAME               7 (datetime)
               IMPORT_FROM              8 (timezone)
               STORE_NAME               8 (timezone)
               POP_TOP

  63           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Path',))
               IMPORT_NAME              9 (pathlib)
               IMPORT_FROM             10 (Path)
               STORE_NAME              10 (Path)
               POP_TOP

  64           LOAD_SMALL_INT           0
               LOAD_CONST               5 (('List', 'Optional'))
               IMPORT_NAME             11 (typing)
               IMPORT_FROM             12 (List)
               STORE_NAME              12 (List)
               IMPORT_FROM             13 (Optional)
               STORE_NAME              13 (Optional)
               POP_TOP

  67           LOAD_NAME                6 (sys)
               LOAD_ATTR               28 (stdout)
               LOAD_NAME                6 (sys)
               LOAD_ATTR               30 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              16 (_stream)

  68           NOP

  69   L2:     LOAD_NAME               16 (_stream)
               LOAD_ATTR               35 (reconfigure + NULL|self)
               LOAD_CONST               6 ('utf-8')
               LOAD_CONST               7 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  67   L4:     END_FOR
               POP_ITER

  74           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               41 (abspath + NULL|self)

  75           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               43 (join + NULL|self)
               LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               45 (dirname + NULL|self)
               LOAD_NAME               23 (__file__)
               CALL                     1
               LOAD_CONST               8 ('..')
               CALL                     2

  74           CALL                     1
               STORE_NAME              24 (_REPO_ROOT_DEFAULT)

  79           LOAD_CONST               9 ('READY')
               STORE_NAME              25 (VERDICT_READY)

  80           LOAD_CONST              10 ('NOT_READY')
               STORE_NAME              26 (VERDICT_NOT_READY)

  82           LOAD_CONST              11 ('BLOCK')
               STORE_NAME              27 (SEVERITY_BLOCK)

  89           LOAD_CONST              81 (('scripts/migrate_v30_learning_manual_test_runs.sql', 'app/services/learning/manual_test_harness.py', 'app/services/learning/manual_test_evidence.py', 'app/services/learning/manual_test_scoring.py', 'app/routes/operator_learning_tests.py', 'app/routes/tenant_learning_tests.py', 'scripts/pas181_manual_test_harness_readiness_check.py', 'docs/pas181_manual_test_execution_harness.md', 'tests/mvp/test_pas181_manual_test_harness.py'))
               STORE_NAME              28 (REQUIRED_FILES)

 101           LOAD_CONST              82 (('scripts/pas160_mvp_sequence_check.py', 'scripts/pas161_lead_ingestion_readiness_check.py', 'scripts/pas162_pending_calls_readiness_check.py', 'scripts/pas163_candidate_pipeline_readiness_check.py', 'scripts/pas164_email_ingestion_readiness_check.py', 'scripts/pas165_email_auth_dedupe_readiness_check.py', 'scripts/pas166_email_dedupe_policy_readiness_check.py', 'scripts/pas167_email_secret_reaper_readiness_check.py', 'scripts/pas168_email_secret_rotation_readiness_check.py', 'scripts/pas169_crypto_roundtrip_check.py', 'scripts/pas169_launch_readiness_check.py', 'scripts/pas_launch_integrity_check.py', 'scripts/pas170_operator_survival_readiness_check.py', 'scripts/pas171_external_pilot_readiness_check.py', 'scripts/pas172_pilot_operations_readiness_check.py', 'scripts/pas173_brokerage_operator_readiness_check.py', 'scripts/pas174_operator_audit_readiness_check.py', 'scripts/pas175_audit_integrity_readiness_check.py', 'scripts/pas176_audit_chain_readiness_check.py', 'scripts/pas177_tenant_audit_verification_readiness_check.py', 'scripts/pas178_audit_window_chain_readiness_check.py', 'scripts/pas179_controlled_learning_readiness_check.py', 'scripts/pas180_learning_review_readiness_check.py'))
               STORE_NAME              29 (PRIOR_PHASE_FILES)

 127           LOAD_CONST              83 (('app/services/memory/review.py', 'app/services/memory/review_stats.py', 'app/services/memory/review_export.py', 'app/services/memory/review_actors.py', 'app/services/memory/review_alerts.py', 'app/services/memory/operator_console.py'))
               STORE_NAME              30 (MEMORY_REVIEW_FILES)

 136           LOAD_CONST              84 (('app/services/learning/learning_policy.py', 'app/services/learning/scenario_contracts.py', 'app/services/learning/outcome_feedback.py', 'app/services/learning/recommendation_engine.py', 'app/services/learning/guardrails.py', 'app/services/learning/recommendation_review.py', 'app/services/learning/recommendation_projection.py', 'app/routes/operator_learning.py', 'app/routes/tenant_learning.py'))
               STORE_NAME              31 (PAS179_PAS180_FILES)

 149           LOAD_CONST              85 (('def create_manual_test_plan(', 'def run_manual_test_simulation(', 'def complete_manual_test_run(', 'def cancel_manual_test_run(', 'def manual_test_run_report(', 'def get_manual_test_run(', 'ALLOWED_MANUAL_TEST_STATUSES', 'ALLOWED_MANUAL_TEST_MODES', 'ALLOWED_HARNESS_TRANSITIONS', 'MANUAL_TEST_ELIGIBLE_RECOMMENDATION_STATUS', '_TABLE = "pas_learning_manual_test_runs"', 'APPROVED_FOR_MANUAL_TEST', 'SIMULATION_ONLY', 'OBSERVATIONAL_ONLY', 'recommendation_not_eligible', 'high_risk_acknowledgement_required'))
               STORE_NAME              32 (REQUIRED_HARNESS_TOKENS)

 168           LOAD_CONST              86 (('def build_manual_test_evidence_packet(', 'def evidence_fingerprint(', 'def evidence_public_projection(', 'def evidence_operator_projection(', 'FORBIDDEN_EVIDENCE_FIELDS', 'ALLOWED_EVIDENCE_KEYS', 'OPERATOR_EVIDENCE_KEYS', 'TENANT_EVIDENCE_KEYS'))
               STORE_NAME              33 (REQUIRED_EVIDENCE_TOKENS)

 179           LOAD_CONST              87 (('def score_manual_test_result(', 'def score_risk_delta(', 'def score_usefulness_delta(', 'def score_confidence_delta(', 'HIGH_RISK_THRESHOLD'))
               STORE_NAME              34 (REQUIRED_SCORING_TOKENS)

 187           LOAD_CONST              88 (('@router.get("/tests")', '@router.get("/tests/{test_run_id}")', '@router.post("/recommendations/{recommendation_id}/manual-tests")', '@router.post("/tests/{test_run_id}/cancel")', '@router.post("/tests/{test_run_id}/complete")', 'def require_admin(', 'list_tests_route', 'get_test_route', 'create_and_run_test_route', 'cancel_test_route', 'complete_test_route'))
               STORE_NAME              35 (REQUIRED_OPERATOR_ROUTE_TOKENS)

 201           LOAD_CONST              89 (('@router.get("/tests")', '@router.get("/tests/{test_run_id}")', 'def require_brokerage(', 'tenant_tests_list_route', 'tenant_tests_get_route'))
               STORE_NAME              36 (REQUIRED_TENANT_ROUTE_TOKENS)

 211           LOAD_CONST              90 (('"LIVE"', "'LIVE'", '"APPLIED"', "'APPLIED'", '"AUTO_APPLIED"', "'AUTO_APPLIED'", '"DEPLOYED"', "'DEPLOYED'", '"APPROVED"', "'APPROVED'"))
               STORE_NAME              37 (FORBIDDEN_STATUS_TOKENS)

 227           LOAD_CONST              91 (('auto_approve', 'auto_apply', 'apply_live', 'mutate_live', 'auto_applied'))
               STORE_NAME              38 (FORBIDDEN_AUTO_APPROVAL_TOKENS)

 238           LOAD_CONST              92 (('from app.engine.state_machine', 'import app.engine.state_machine', 'from app.services.memory.review', 'import app.services.memory.review', 'from app.services.memory.approval', 'import app.services.memory.approval', 'from app.services.booking', 'import app.services.booking', 'from app.services.outbound', 'import app.services.outbound', 'from app.services.worker', 'import app.services.worker', 'from app.services.ingestion.worker', 'import app.services.ingestion.worker', 'from app.services.slack', 'import app.services.slack'))
               STORE_NAME              39 (FORBIDDEN_LIVE_MUTATION_IMPORTS)

 258           LOAD_CONST              93 (('learning.recommendation.approved_for_manual_test', 'learning.manual_test.planned', 'learning.manual_test.started', 'learning.manual_test.completed', 'learning.manual_test.failed', 'learning.manual_test.cancelled', 'tenant.learning.manual_test.viewed'))
               STORE_NAME              40 (REQUIRED_EVENT_TYPES)

 271           LOAD_CONST              94 (('import gmail', 'from gmail', 'import googleapiclient', 'from googleapiclient', 'import google.oauth2', 'from google.oauth2', 'from google.auth', 'import google.auth', 'from google_auth_oauthlib', 'import imaplib', 'from imaplib', 'import poplib', 'from poplib', 'import composio', 'from composio', 'import trustclaw', 'from trustclaw', 'import chromadb', 'from chromadb', 'import pinecone', 'from pinecone', 'import langchain', 'from langchain', 'import faiss', 'import pgvector', 'from pgvector', 'from openai import embeddings', 'from openai.embeddings', 'from anthropic', 'import anthropic', 'from openai', 'import openai'))
               STORE_NAME              41 (FORBIDDEN_IMPORT_LINE_PREFIXES)

 295           LOAD_CONST              95 (('imaplib', 'poplib', 'fetch_inbox', 'gmail_oauth', 'gmail_token', 'users().messages'))
               STORE_NAME              42 (FORBIDDEN_INBOX_TOKENS)

 309           LOAD_CONST              12 ('severity')

 311           LOAD_NAME               27 (SEVERITY_BLOCK)

 309           LOAD_CONST              13 ('detail')

 311           LOAD_CONST              14 ('')

 309           BUILD_MAP                2
               LOAD_CONST              15 (<code object __annotate__ at 0x0000018C18026130, file "scripts/pas181_manual_test_harness_readiness_check.py", line 309>)
               MAKE_FUNCTION
               LOAD_CONST              16 (<code object _check at 0x0000018C17FA34B0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 309>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              43 (_check)

 322           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C17FA31E0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 322>)
               MAKE_FUNCTION
               LOAD_CONST              18 (<code object _now_iso at 0x0000018C180388F0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 322>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              44 (_now_iso)

 326           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA3A50, file "scripts/pas181_manual_test_harness_readiness_check.py", line 326>)
               MAKE_FUNCTION
               LOAD_CONST              20 (<code object _read_text at 0x0000018C18053CF0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 326>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              45 (_read_text)

 333           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA3E10, file "scripts/pas181_manual_test_harness_readiness_check.py", line 333>)
               MAKE_FUNCTION
               LOAD_CONST              22 (<code object _strip_python_comments_and_strings at 0x0000018C17E59E70, file "scripts/pas181_manual_test_harness_readiness_check.py", line 333>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              46 (_strip_python_comments_and_strings)

 372           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA3960, file "scripts/pas181_manual_test_harness_readiness_check.py", line 372>)
               MAKE_FUNCTION
               LOAD_CONST              24 (<code object check_files_present at 0x0000018C18061110, file "scripts/pas181_manual_test_harness_readiness_check.py", line 372>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              47 (check_files_present)

 385           LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA3C30, file "scripts/pas181_manual_test_harness_readiness_check.py", line 385>)
               MAKE_FUNCTION
               LOAD_CONST              26 (<code object check_prior_phases_intact at 0x0000018C17CC1CE0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 385>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              48 (check_prior_phases_intact)

 406           LOAD_CONST              27 (<code object __annotate__ at 0x0000018C18114120, file "scripts/pas181_manual_test_harness_readiness_check.py", line 406>)
               MAKE_FUNCTION
               LOAD_CONST              28 (<code object check_memory_review_intact at 0x0000018C18060DB0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 406>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              49 (check_memory_review_intact)

 419           LOAD_CONST              29 (<code object __annotate__ at 0x0000018C18114210, file "scripts/pas181_manual_test_harness_readiness_check.py", line 419>)
               MAKE_FUNCTION
               LOAD_CONST              30 (<code object check_worker_off_by_default at 0x0000018C179C3C30, file "scripts/pas181_manual_test_harness_readiness_check.py", line 419>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              50 (check_worker_off_by_default)

 436           LOAD_CONST              31 (<code object __annotate__ at 0x0000018C18114300, file "scripts/pas181_manual_test_harness_readiness_check.py", line 436>)
               MAKE_FUNCTION
               LOAD_CONST              32 (<code object check_no_startup_worker at 0x0000018C17D87040, file "scripts/pas181_manual_test_harness_readiness_check.py", line 436>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              51 (check_no_startup_worker)

 459           LOAD_CONST              33 (<code object __annotate__ at 0x0000018C181144E0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 459>)
               MAKE_FUNCTION
               LOAD_CONST              34 (<code object check_harness_service at 0x0000018C17FEE430, file "scripts/pas181_manual_test_harness_readiness_check.py", line 459>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              52 (check_harness_service)

 474           LOAD_CONST              35 (<code object __annotate__ at 0x0000018C181145D0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 474>)
               MAKE_FUNCTION
               LOAD_CONST              36 (<code object check_evidence_service at 0x0000018C17FEE030, file "scripts/pas181_manual_test_harness_readiness_check.py", line 474>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              53 (check_evidence_service)

 489           LOAD_CONST              37 (<code object __annotate__ at 0x0000018C181146C0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 489>)
               MAKE_FUNCTION
               LOAD_CONST              38 (<code object check_scoring_service at 0x0000018C17FEDC30, file "scripts/pas181_manual_test_harness_readiness_check.py", line 489>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              54 (check_scoring_service)

 504           LOAD_CONST              39 (<code object __annotate__ at 0x0000018C181147B0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 504>)
               MAKE_FUNCTION
               LOAD_CONST              40 (<code object check_operator_routes at 0x0000018C17D51060, file "scripts/pas181_manual_test_harness_readiness_check.py", line 504>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              55 (check_operator_routes)

 526           LOAD_CONST              41 (<code object __annotate__ at 0x0000018C181148A0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 526>)
               MAKE_FUNCTION
               LOAD_CONST              42 (<code object check_tenant_routes at 0x0000018C17F74010, file "scripts/pas181_manual_test_harness_readiness_check.py", line 526>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              56 (check_tenant_routes)

 560           LOAD_CONST              43 (<code object __annotate__ at 0x0000018C18114990, file "scripts/pas181_manual_test_harness_readiness_check.py", line 560>)
               MAKE_FUNCTION
               LOAD_CONST              44 (<code object check_no_forbidden_status_tokens at 0x0000018C17E92930, file "scripts/pas181_manual_test_harness_readiness_check.py", line 560>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              57 (check_no_forbidden_status_tokens)

 588           LOAD_CONST              45 (<code object __annotate__ at 0x0000018C18114A80, file "scripts/pas181_manual_test_harness_readiness_check.py", line 588>)
               MAKE_FUNCTION
               LOAD_CONST              46 (<code object check_no_auto_approval_tokens at 0x0000018C182FF040, file "scripts/pas181_manual_test_harness_readiness_check.py", line 588>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              58 (check_no_auto_approval_tokens)

 617           LOAD_CONST              47 (<code object __annotate__ at 0x0000018C18114B70, file "scripts/pas181_manual_test_harness_readiness_check.py", line 617>)
               MAKE_FUNCTION
               LOAD_CONST              48 (<code object check_no_live_mutation_imports at 0x0000018C17F74350, file "scripts/pas181_manual_test_harness_readiness_check.py", line 617>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              59 (check_no_live_mutation_imports)

 649           LOAD_CONST              49 (<code object __annotate__ at 0x0000018C18114C60, file "scripts/pas181_manual_test_harness_readiness_check.py", line 649>)
               MAKE_FUNCTION
               LOAD_CONST              50 (<code object check_audit_service_invariant at 0x0000018C182DD2E0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 649>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              60 (check_audit_service_invariant)

 676           LOAD_CONST              51 (<code object __annotate__ at 0x0000018C18114D50, file "scripts/pas181_manual_test_harness_readiness_check.py", line 676>)
               MAKE_FUNCTION
               LOAD_CONST              52 (<code object check_v30_sql at 0x0000018C17F7DB80, file "scripts/pas181_manual_test_harness_readiness_check.py", line 676>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              61 (check_v30_sql)

 786           LOAD_CONST              53 (<code object __annotate__ at 0x0000018C18114E40, file "scripts/pas181_manual_test_harness_readiness_check.py", line 786>)
               MAKE_FUNCTION
               LOAD_CONST              54 (<code object check_event_contract at 0x0000018C1801C9E0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 786>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              62 (check_event_contract)

 801           LOAD_CONST              55 (<code object __annotate__ at 0x0000018C18114F30, file "scripts/pas181_manual_test_harness_readiness_check.py", line 801>)
               MAKE_FUNCTION
               LOAD_CONST              56 (<code object check_main_router_mounts at 0x0000018C180FC990, file "scripts/pas181_manual_test_harness_readiness_check.py", line 801>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              63 (check_main_router_mounts)

 820           LOAD_CONST              57 (<code object __annotate__ at 0x0000018C18115020, file "scripts/pas181_manual_test_harness_readiness_check.py", line 820>)
               MAKE_FUNCTION
               LOAD_CONST              58 (<code object check_no_forbidden_imports at 0x0000018C17F74690, file "scripts/pas181_manual_test_harness_readiness_check.py", line 820>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              64 (check_no_forbidden_imports)

 853           LOAD_CONST              59 (<code object __annotate__ at 0x0000018C18115110, file "scripts/pas181_manual_test_harness_readiness_check.py", line 853>)
               MAKE_FUNCTION
               LOAD_CONST              60 (<code object check_no_inbox_scan_tokens at 0x0000018C17CC1F60, file "scripts/pas181_manual_test_harness_readiness_check.py", line 853>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              65 (check_no_inbox_scan_tokens)

 882           LOAD_CONST              61 (<code object __annotate__ at 0x0000018C181152F0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 882>)
               MAKE_FUNCTION
               LOAD_CONST              62 (<code object check_doc_required_clauses at 0x0000018C17E92410, file "scripts/pas181_manual_test_harness_readiness_check.py", line 882>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              66 (check_doc_required_clauses)

 929           LOAD_CONST              63 (<code object __annotate__ at 0x0000018C181153E0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 929>)
               MAKE_FUNCTION
               LOAD_CONST              64 (<code object check_self_no_env_or_db at 0x0000018C17D893A0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 929>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              67 (check_self_no_env_or_db)

 962           LOAD_CONST              65 (<code object __annotate__ at 0x0000018C181154D0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 962>)
               MAKE_FUNCTION
               LOAD_CONST              66 (<code object _aggregate at 0x0000018C1800B0A0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 962>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              68 (_aggregate)

 974           LOAD_CONST              67 (<code object __annotate__ at 0x0000018C181155C0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 974>)
               MAKE_FUNCTION
               LOAD_CONST              68 (<code object _operator_actions at 0x0000018C180483B0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 974>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              69 (_operator_actions)

 984           LOAD_CONST              69 (<code object __annotate__ at 0x0000018C18115980, file "scripts/pas181_manual_test_harness_readiness_check.py", line 984>)
               MAKE_FUNCTION
               LOAD_CONST              70 (<code object evaluate at 0x0000018C177C69F0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 984>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              70 (evaluate)

1024           LOAD_CONST              71 ('pas181_manual_test_harness_readiness_report.json')
               STORE_NAME              71 (REPORT_FILENAME)

1027           LOAD_CONST              72 (<code object __annotate__ at 0x0000018C18115A70, file "scripts/pas181_manual_test_harness_readiness_check.py", line 1027>)
               MAKE_FUNCTION
               LOAD_CONST              73 (<code object _build_parser at 0x0000018C180FC7B0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 1027>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              72 (_build_parser)

1045           LOAD_CONST              74 (<code object __annotate__ at 0x0000018C18115B60, file "scripts/pas181_manual_test_harness_readiness_check.py", line 1045>)
               MAKE_FUNCTION
               LOAD_CONST              75 (<code object _print_summary at 0x0000018C17D8C5C0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 1045>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              73 (_print_summary)

1063           LOAD_CONST              76 (<code object __annotate__ at 0x0000018C18026330, file "scripts/pas181_manual_test_harness_readiness_check.py", line 1063>)
               MAKE_FUNCTION
               LOAD_CONST              77 (<code object _write_report at 0x0000018C180FCF30, file "scripts/pas181_manual_test_harness_readiness_check.py", line 1063>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              74 (_write_report)

1077           LOAD_CONST              96 ((None,))
               LOAD_CONST              78 (<code object __annotate__ at 0x0000018C18115C50, file "scripts/pas181_manual_test_harness_readiness_check.py", line 1077>)
               MAKE_FUNCTION
               LOAD_CONST              79 (<code object main at 0x0000018C17D89750, file "scripts/pas181_manual_test_harness_readiness_check.py", line 1077>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              75 (main)

1102           LOAD_NAME               76 (__name__)
               LOAD_CONST              80 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

1103           LOAD_NAME                6 (sys)
               LOAD_ATTR              154 (exit)
               PUSH_NULL
               LOAD_NAME               75 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

1102   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  70           LOAD_NAME               18 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  71   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          387 (to L1)

  70   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026130, file "scripts/pas181_manual_test_harness_readiness_check.py", line 309>:
309           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('check_id')

310           LOAD_CONST               2 ('str')

309           LOAD_CONST               3 ('status')

310           LOAD_CONST               2 ('str')

309           LOAD_CONST               4 ('label')

310           LOAD_CONST               2 ('str')

309           LOAD_CONST               5 ('severity')

311           LOAD_CONST               2 ('str')

309           LOAD_CONST               6 ('detail')

311           LOAD_CONST               2 ('str')

309           LOAD_CONST               7 ('return')

312           LOAD_CONST               8 ('dict')

309           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _check at 0x0000018C17FA34B0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 309>:
309           RESUME                   0

314           LOAD_CONST               0 ('id')
              LOAD_FAST_BORROW         0 (check_id)

315           LOAD_CONST               1 ('status')
              LOAD_FAST_BORROW         1 (status)

316           LOAD_CONST               2 ('label')
              LOAD_FAST_BORROW         2 (label)

317           LOAD_CONST               3 ('severity')
              LOAD_FAST_BORROW         3 (severity)

318           LOAD_CONST               4 ('detail')
              LOAD_FAST_BORROW         4 (detail)

313           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 322>:
322           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C180388F0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 322>:
322           RESUME                   0

323           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "scripts/pas181_manual_test_harness_readiness_check.py", line 326>:
326           RESUME                   0
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

Disassembly of <code object _read_text at 0x0000018C18053CF0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 326>:
 326           RESUME                   0

 327           NOP

 328   L1:     LOAD_FAST_BORROW         0 (path)
               LOAD_ATTR                1 (read_text + NULL|self)
               LOAD_CONST               0 ('utf-8')
               LOAD_CONST               1 ('replace')
               LOAD_CONST               2 (('encoding', 'errors'))
               CALL_KW                  2
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 329           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 330   L4:     POP_EXCEPT
               LOAD_CONST               3 (None)
               RETURN_VALUE

 329   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "scripts/pas181_manual_test_harness_readiness_check.py", line 333>:
333           RESUME                   0
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

Disassembly of <code object _strip_python_comments_and_strings at 0x0000018C17E59E70, file "scripts/pas181_manual_test_harness_readiness_check.py", line 333>:
333            RESUME                   0

334            BUILD_LIST               0
               STORE_FAST               1 (out)

335            LOAD_SMALL_INT           0
               LOAD_GLOBAL              1 (len + NULL)
               LOAD_FAST_BORROW         0 (src)
               CALL                     1
               STORE_FAST_STORE_FAST   50 (n, i)

336    L1:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (i, n)
               COMPARE_OP              18 (bool(<))
               EXTENDED_ARG             1
               POP_JUMP_IF_FALSE      282 (to L13)
               NOT_TAKEN

337            LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               BINARY_OP               26 ([])
               STORE_FAST               4 (ch)

338            LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               1 ('#')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       38 (to L3)
               NOT_TAKEN

339            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_CONST               2 ('\n')
               LOAD_FAST_BORROW         2 (i)
               CALL                     2
               STORE_FAST               5 (j)

340            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L2)
               NOT_TAKEN

341            JUMP_FORWARD           240 (to L13)

342    L2:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

343            JUMP_BACKWARD           59 (to L1)

344    L3:     LOAD_FAST_BORROW         0 (src)
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

345    L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               BINARY_SLICE
               STORE_FAST               6 (quote)

346            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 98 (quote, i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               CALL                     2
               STORE_FAST               7 (end)

347            LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L5)
               NOT_TAKEN

348            JUMP_FORWARD           138 (to L13)

349    L5:     LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

350            JUMP_BACKWARD          161 (to L1)

351    L6:     LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               7 (('"', "'"))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       92 (to L12)
               NOT_TAKEN

352            LOAD_FAST                4 (ch)
               STORE_FAST               6 (quote)

353            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               5 (j)

354    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (j, n)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       63 (to L11)
               NOT_TAKEN

355            LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
               BINARY_OP               26 ([])
               LOAD_CONST               5 ('\\')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       12 (to L8)
               NOT_TAKEN

356            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           2
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)

357            JUMP_BACKWARD           30 (to L7)

358    L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
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

359    L9:     JUMP_FORWARD            11 (to L11)

360   L10:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)
               JUMP_BACKWARD           68 (to L7)

361   L11:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

362            EXTENDED_ARG             1
               JUMP_BACKWARD          259 (to L1)

363   L12:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (ch)
               CALL                     1
               POP_TOP

364            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               2 (i)
               EXTENDED_ARG             1
               JUMP_BACKWARD          288 (to L1)

365   L13:     LOAD_CONST               6 ('')
               LOAD_ATTR                9 (join + NULL|self)
               LOAD_FAST_BORROW         1 (out)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "scripts/pas181_manual_test_harness_readiness_check.py", line 372>:
372           RESUME                   0
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

Disassembly of <code object check_files_present at 0x0000018C18061110, file "scripts/pas181_manual_test_harness_readiness_check.py", line 372>:
372           RESUME                   0

373           BUILD_LIST               0
              STORE_FAST               1 (out)

374           LOAD_GLOBAL              0 (REQUIRED_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

375           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

376           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

377           LOAD_CONST               0 ('file:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

378           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

379   L3:     LOAD_CONST               3 ('Required PAS181 file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

380           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing')

376   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

374   L6:     END_FOR
              POP_ITER

382           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "scripts/pas181_manual_test_harness_readiness_check.py", line 385>:
385           RESUME                   0
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

Disassembly of <code object check_prior_phases_intact at 0x0000018C17CC1CE0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 385>:
385            RESUME                   0

386            BUILD_LIST               0
               STORE_FAST               1 (out)

387            LOAD_GLOBAL              0 (PRIOR_PHASE_FILES)
               GET_ITER
       L1:     FOR_ITER                91 (to L6)
               STORE_FAST               2 (p)

388            LOAD_GLOBAL              3 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         2 (p)
               BINARY_OP               11 (/)
               LOAD_ATTR                5 (is_file + NULL|self)
               CALL                     0
               STORE_FAST               3 (ok)

389            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

390            LOAD_CONST               0 ('prior_phase:')
               LOAD_FAST_BORROW         2 (p)
               FORMAT_SIMPLE
               BUILD_STRING             2

391            LOAD_FAST_BORROW         3 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L2)
               NOT_TAKEN
               LOAD_CONST               1 ('PASS')
               JUMP_FORWARD             1 (to L3)
       L2:     LOAD_CONST               2 ('FAIL')

392    L3:     LOAD_CONST               3 ('Prior-phase readiness script intact: ')
               LOAD_FAST_BORROW         2 (p)
               FORMAT_SIMPLE
               BUILD_STRING             2

393            LOAD_FAST_BORROW         3 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L5)
       L4:     LOAD_CONST               5 ('missing — PAS181 must not delete')

389    L5:     LOAD_CONST               6 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           93 (to L1)

387    L6:     END_FOR
               POP_ITER

395            LOAD_GLOBAL             10 (PAS179_PAS180_FILES)
               GET_ITER
       L7:     FOR_ITER                91 (to L12)
               STORE_FAST               2 (p)

396            LOAD_GLOBAL              3 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         2 (p)
               BINARY_OP               11 (/)
               LOAD_ATTR                5 (is_file + NULL|self)
               CALL                     0
               STORE_FAST               3 (ok)

397            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

398            LOAD_CONST               7 ('pas179_180_service:')
               LOAD_FAST_BORROW         2 (p)
               FORMAT_SIMPLE
               BUILD_STRING             2

399            LOAD_FAST_BORROW         3 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN
               LOAD_CONST               1 ('PASS')
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST               2 ('FAIL')

400    L9:     LOAD_CONST               8 ('PAS179/PAS180 service intact: ')
               LOAD_FAST_BORROW         2 (p)
               FORMAT_SIMPLE
               BUILD_STRING             2

401            LOAD_FAST_BORROW         3 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST               9 ('PAS179/PAS180 service deleted — PAS181 must not touch')

397   L11:     LOAD_CONST               6 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           93 (to L7)

395   L12:     END_FOR
               POP_ITER

403            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114120, file "scripts/pas181_manual_test_harness_readiness_check.py", line 406>:
406           RESUME                   0
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

Disassembly of <code object check_memory_review_intact at 0x0000018C18060DB0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 406>:
406           RESUME                   0

407           BUILD_LIST               0
              STORE_FAST               1 (out)

408           LOAD_GLOBAL              0 (MEMORY_REVIEW_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

409           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

410           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

411           LOAD_CONST               0 ('memory_review:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

412           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

413   L3:     LOAD_CONST               3 ('Memory Review file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

414           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('Memory Review file deleted — PAS181 must not touch')

410   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

408   L6:     END_FOR
              POP_ITER

416           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114210, file "scripts/pas181_manual_test_harness_readiness_check.py", line 419>:
419           RESUME                   0
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

Disassembly of <code object check_worker_off_by_default at 0x0000018C179C3C30, file "scripts/pas181_manual_test_harness_readiness_check.py", line 419>:
419           RESUME                   0

420           BUILD_LIST               0
              STORE_FAST               1 (out)

421           LOAD_GLOBAL              1 (Path + NULL)
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

422           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

424           LOAD_CONST               5 ('_ENV_FLAG_ENABLED_LITERAL = "true"')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         6 (to L2)
              NOT_TAKEN
              POP_TOP

425           LOAD_CONST               6 ("_ENV_FLAG_ENABLED_LITERAL = 'true'")
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)

423   L2:     STORE_FAST               4 (literal_ok)

427           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

428           LOAD_CONST               7 ('worker:off_by_default')

429           LOAD_FAST_BORROW         4 (literal_ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               8 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               9 ('FAIL')

430   L4:     LOAD_CONST              10 ('Pending-call worker is OFF by default')

431           LOAD_FAST_BORROW         4 (literal_ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST              11 ('missing strict enable-literal constant')

427   L6:     LOAD_CONST              12 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

433           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114300, file "scripts/pas181_manual_test_harness_readiness_check.py", line 436>:
436           RESUME                   0
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

Disassembly of <code object check_no_startup_worker at 0x0000018C17D87040, file "scripts/pas181_manual_test_harness_readiness_check.py", line 436>:
436           RESUME                   0

437           BUILD_LIST               0
              STORE_FAST               1 (out)

438           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('main.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

439           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               2 ('')
      L1:     STORE_FAST               3 (src)

440           LOAD_GLOBAL              5 (_strip_python_comments_and_strings + NULL)
              LOAD_FAST_BORROW         3 (src)
              CALL                     1
              STORE_FAST               4 (executable)

441           BUILD_LIST               0
              STORE_FAST               5 (bad)

442           LOAD_CONST               3 ('from app.services.ingestion.worker')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L2)
              NOT_TAKEN

443           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               4 ('from app.services.ingestion.worker import …')
              CALL                     1
              POP_TOP

444   L2:     LOAD_CONST               5 ('import app.services.ingestion.worker')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L3)
              NOT_TAKEN

445           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               5 ('import app.services.ingestion.worker')
              CALL                     1
              POP_TOP

446   L3:     LOAD_CONST               6 ('run_worker_loop')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L4)
              NOT_TAKEN

447           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               7 ('run_worker_loop reference')
              CALL                     1
              POP_TOP

448   L4:     LOAD_CONST               8 ('process_pending_call(')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L5)
              NOT_TAKEN

449           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               9 ('process_pending_call call')
              CALL                     1
              POP_TOP

450   L5:     LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

451           LOAD_CONST              10 ('main:no_startup_worker')

452           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L6)
              NOT_TAKEN
              LOAD_CONST              11 ('FAIL')
              JUMP_FORWARD             1 (to L7)
      L6:     LOAD_CONST              12 ('PASS')

453   L7:     LOAD_CONST              13 ('FastAPI lifespan does not auto-start the pending-call worker')

454           LOAD_FAST_BORROW         5 (bad)
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

450   L9:     LOAD_CONST              16 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

456           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181144E0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 459>:
459           RESUME                   0
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

Disassembly of <code object check_harness_service at 0x0000018C17FEE430, file "scripts/pas181_manual_test_harness_readiness_check.py", line 459>:
459           RESUME                   0

460           BUILD_LIST               0
              STORE_FAST               1 (out)

461           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('services')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('learning')
              BINARY_OP               11 (/)
              LOAD_CONST               3 ('manual_test_harness.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

462           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

463           LOAD_GLOBAL              4 (REQUIRED_HARNESS_TOKENS)
              GET_ITER
      L2:     FOR_ITER                73 (to L7)
              STORE_FAST               4 (tok)

464           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

465           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

466           LOAD_CONST               5 ('harness:')
              LOAD_FAST_BORROW         4 (tok)
              LOAD_CONST               6 (slice(None, 48, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

467           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               7 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               8 ('FAIL')

468   L4:     LOAD_CONST               9 ('Manual-test harness token: ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

469           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             4 (to L6)
      L5:     LOAD_CONST              10 ('missing token ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

465   L6:     LOAD_CONST              11 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           75 (to L2)

463   L7:     END_FOR
              POP_ITER

471           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181145D0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 474>:
474           RESUME                   0
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

Disassembly of <code object check_evidence_service at 0x0000018C17FEE030, file "scripts/pas181_manual_test_harness_readiness_check.py", line 474>:
474           RESUME                   0

475           BUILD_LIST               0
              STORE_FAST               1 (out)

476           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('services')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('learning')
              BINARY_OP               11 (/)
              LOAD_CONST               3 ('manual_test_evidence.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

477           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

478           LOAD_GLOBAL              4 (REQUIRED_EVIDENCE_TOKENS)
              GET_ITER
      L2:     FOR_ITER                73 (to L7)
              STORE_FAST               4 (tok)

479           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

480           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

481           LOAD_CONST               5 ('evidence:')
              LOAD_FAST_BORROW         4 (tok)
              LOAD_CONST               6 (slice(None, 48, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

482           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               7 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               8 ('FAIL')

483   L4:     LOAD_CONST               9 ('Manual-test evidence token: ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

484           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             4 (to L6)
      L5:     LOAD_CONST              10 ('missing token ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

480   L6:     LOAD_CONST              11 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           75 (to L2)

478   L7:     END_FOR
              POP_ITER

486           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181146C0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 489>:
489           RESUME                   0
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

Disassembly of <code object check_scoring_service at 0x0000018C17FEDC30, file "scripts/pas181_manual_test_harness_readiness_check.py", line 489>:
489           RESUME                   0

490           BUILD_LIST               0
              STORE_FAST               1 (out)

491           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('services')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('learning')
              BINARY_OP               11 (/)
              LOAD_CONST               3 ('manual_test_scoring.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

492           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

493           LOAD_GLOBAL              4 (REQUIRED_SCORING_TOKENS)
              GET_ITER
      L2:     FOR_ITER                73 (to L7)
              STORE_FAST               4 (tok)

494           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

495           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

496           LOAD_CONST               5 ('scoring:')
              LOAD_FAST_BORROW         4 (tok)
              LOAD_CONST               6 (slice(None, 48, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

497           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               7 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               8 ('FAIL')

498   L4:     LOAD_CONST               9 ('Manual-test scoring token: ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

499           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             4 (to L6)
      L5:     LOAD_CONST              10 ('missing token ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

495   L6:     LOAD_CONST              11 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           75 (to L2)

493   L7:     END_FOR
              POP_ITER

501           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181147B0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 504>:
504           RESUME                   0
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

Disassembly of <code object check_operator_routes at 0x0000018C17D51060, file "scripts/pas181_manual_test_harness_readiness_check.py", line 504>:
504            RESUME                   0

505            BUILD_LIST               0
               STORE_FAST               1 (out)

506            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('routes')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('operator_learning_tests.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

507            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               3 ('')
       L1:     STORE_FAST               3 (src)

508            LOAD_GLOBAL              4 (REQUIRED_OPERATOR_ROUTE_TOKENS)
               GET_ITER
       L2:     FOR_ITER                73 (to L7)
               STORE_FAST               4 (tok)

509            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

510            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

511            LOAD_CONST               4 ('operator_routes:')
               LOAD_FAST_BORROW         4 (tok)
               LOAD_CONST               5 (slice(None, 48, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

512            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               6 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               7 ('FAIL')

513    L4:     LOAD_CONST               8 ('Operator-test route token: ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

514            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               3 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST               9 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

510    L6:     LOAD_CONST              10 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           75 (to L2)

508    L7:     END_FOR
               POP_ITER

516            LOAD_CONST              11 ('require_admin')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       20 (to L8)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              12 ('x_admin_key')
               LOAD_FAST_BORROW         3 (src)
               LOAD_ATTR               11 (lower + NULL|self)
               CALL                     0
               CONTAINS_OP              0 (in)
       L8:     STORE_FAST               6 (auth_ok)

517            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

518            LOAD_CONST              13 ('operator_routes:require_admin')

519            LOAD_FAST_BORROW         6 (auth_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN
               LOAD_CONST               6 ('PASS')
               JUMP_FORWARD             1 (to L10)
       L9:     LOAD_CONST               7 ('FAIL')

520   L10:     LOAD_CONST              14 ('Operator-test routes use require_admin (X-Admin-Key)')

521            LOAD_FAST_BORROW         6 (auth_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               3 ('')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST              15 ('missing require_admin / X-Admin-Key tokens')

517   L12:     LOAD_CONST              10 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

523            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181148A0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 526>:
526           RESUME                   0
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

Disassembly of <code object check_tenant_routes at 0x0000018C17F74010, file "scripts/pas181_manual_test_harness_readiness_check.py", line 526>:
526            RESUME                   0

527            BUILD_LIST               0
               STORE_FAST               1 (out)

528            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('routes')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('tenant_learning_tests.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

529            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               3 ('')
       L1:     STORE_FAST               3 (src)

530            LOAD_GLOBAL              4 (REQUIRED_TENANT_ROUTE_TOKENS)
               GET_ITER
       L2:     FOR_ITER                73 (to L7)
               STORE_FAST               4 (tok)

531            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

532            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

533            LOAD_CONST               4 ('tenant_routes:')
               LOAD_FAST_BORROW         4 (tok)
               LOAD_CONST               5 (slice(None, 48, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

534            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               6 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               7 ('FAIL')

535    L4:     LOAD_CONST               8 ('Tenant-test route token: ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

536            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               3 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST               9 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

532    L6:     LOAD_CONST              10 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           75 (to L2)

530    L7:     END_FOR
               POP_ITER

539            LOAD_CONST              11 ('require_brokerage')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       33 (to L8)
               NOT_TAKEN
               POP_TOP

540            LOAD_CONST              12 ('x_api_key')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

539            COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       20 (to L8)
               NOT_TAKEN
               POP_TOP

541            LOAD_CONST              13 ('x_admin_key')
               LOAD_FAST_BORROW         3 (src)
               LOAD_ATTR               11 (lower + NULL|self)
               CALL                     0
               CONTAINS_OP              1 (not in)

538    L8:     STORE_FAST               6 (auth_ok)

543            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

544            LOAD_CONST              14 ('tenant_routes:tenant_auth_only')

545            LOAD_FAST_BORROW         6 (auth_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN
               LOAD_CONST               6 ('PASS')
               JUMP_FORWARD             1 (to L10)
       L9:     LOAD_CONST               7 ('FAIL')

546   L10:     LOAD_CONST              15 ('Tenant-test routes use X-API-Key (require_brokerage), never admin')

547            LOAD_FAST_BORROW         6 (auth_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               3 ('')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST              16 ('missing require_brokerage / x_api_key tokens')

543   L12:     LOAD_CONST              10 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

549            LOAD_GLOBAL             13 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               7 (executable)

550            LOAD_CONST              17 ('@router.post')
               LOAD_FAST_BORROW         7 (executable)
               CONTAINS_OP              1 (not in)
               STORE_FAST               8 (no_post)

551            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

552            LOAD_CONST              18 ('tenant_routes:no_mutation_surface')

553            LOAD_FAST_BORROW         8 (no_post)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L13)
               NOT_TAKEN
               LOAD_CONST               6 ('PASS')
               JUMP_FORWARD             1 (to L14)
      L13:     LOAD_CONST               7 ('FAIL')

554   L14:     LOAD_CONST              19 ('Tenant-test routes have NO @router.post surface')

555            LOAD_FAST_BORROW         8 (no_post)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L15)
               NOT_TAKEN
               LOAD_CONST               3 ('')
               JUMP_FORWARD             1 (to L16)
      L15:     LOAD_CONST              20 ('tenant route file declares a POST route')

551   L16:     LOAD_CONST              10 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

557            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114990, file "scripts/pas181_manual_test_harness_readiness_check.py", line 560>:
560           RESUME                   0
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

Disassembly of <code object check_no_forbidden_status_tokens at 0x0000018C17E92930, file "scripts/pas181_manual_test_harness_readiness_check.py", line 560>:
560            RESUME                   0

561            BUILD_LIST               0
               STORE_FAST               1 (out)

562            LOAD_CONST               9 (('app/services/learning/manual_test_harness.py', 'app/services/learning/manual_test_evidence.py', 'app/services/learning/manual_test_scoring.py', 'app/routes/operator_learning_tests.py', 'app/routes/tenant_learning_tests.py'))
               STORE_FAST               2 (files)

569            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               202 (to L11)
               STORE_FAST               3 (relpath)

570            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

571            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

572            JUMP_BACKWARD           45 (to L1)

573    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

574            BUILD_LIST               0
               STORE_FAST               6 (bad)

575            LOAD_GLOBAL              6 (FORBIDDEN_STATUS_TOKENS)
               GET_ITER
       L4:     FOR_ITER                28 (to L6)
               STORE_FAST               7 (tok)

576            LOAD_FAST_BORROW_LOAD_FAST_BORROW 117 (tok, src)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L4)

577    L5:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_FAST_BORROW         7 (tok)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L4)

575    L6:     END_FOR
               POP_ITER

578            LOAD_FAST                1 (out)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_GLOBAL             11 (_check + NULL)

579            LOAD_CONST               2 ('no_forbidden_status:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

580            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L7)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L8)
       L7:     LOAD_CONST               4 ('PASS')

581    L8:     LOAD_CONST               5 ('No forbidden status tokens: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

583            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       43 (to L9)
               NOT_TAKEN

582            LOAD_CONST               6 ('disqualifying tokens: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               13 (join + NULL|self)
               LOAD_GLOBAL             15 (sorted + NULL)
               LOAD_GLOBAL             17 (set + NULL)
               LOAD_FAST_BORROW         6 (bad)
               CALL                     1
               CALL                     1
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L10)

583    L9:     LOAD_CONST               1 ('')

578   L10:     LOAD_CONST               8 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          204 (to L1)

569   L11:     END_FOR
               POP_ITER

585            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114A80, file "scripts/pas181_manual_test_harness_readiness_check.py", line 588>:
588           RESUME                   0
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

Disassembly of <code object check_no_auto_approval_tokens at 0x0000018C182FF040, file "scripts/pas181_manual_test_harness_readiness_check.py", line 588>:
588            RESUME                   0

589            BUILD_LIST               0
               STORE_FAST               1 (out)

590            LOAD_CONST               9 (('app/services/learning/manual_test_harness.py', 'app/services/learning/manual_test_evidence.py', 'app/services/learning/manual_test_scoring.py', 'app/routes/operator_learning_tests.py', 'app/routes/tenant_learning_tests.py'))
               STORE_FAST               2 (files)

597            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               242 (to L11)
               STORE_FAST               3 (relpath)

598            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

599            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

600            JUMP_BACKWARD           45 (to L1)

601    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

602            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         5 (src)
               CALL                     1
               STORE_FAST               6 (executable)

603            BUILD_LIST               0
               STORE_FAST               7 (bad)

604            LOAD_GLOBAL              8 (FORBIDDEN_AUTO_APPROVAL_TOKENS)
               GET_ITER
       L4:     FOR_ITER                57 (to L6)
               STORE_FAST               8 (tok)

605            LOAD_FAST_BORROW         8 (tok)
               LOAD_ATTR               11 (lower + NULL|self)
               CALL                     0
               LOAD_FAST_BORROW         6 (executable)
               LOAD_ATTR               11 (lower + NULL|self)
               CALL                     0
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           40 (to L4)

606    L5:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR               13 (append + NULL|self)
               LOAD_FAST_BORROW         8 (tok)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           59 (to L4)

604    L6:     END_FOR
               POP_ITER

607            LOAD_FAST                1 (out)
               LOAD_ATTR               13 (append + NULL|self)
               LOAD_GLOBAL             15 (_check + NULL)

608            LOAD_CONST               2 ('no_auto_approval:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

609            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L7)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L8)
       L7:     LOAD_CONST               4 ('PASS')

610    L8:     LOAD_CONST               5 ('No auto-approval / live-mutation tokens: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

612            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       43 (to L9)
               NOT_TAKEN

611            LOAD_CONST               6 ('disqualifying tokens: ')
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

612    L9:     LOAD_CONST               1 ('')

607   L10:     LOAD_CONST               8 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          244 (to L1)

597   L11:     END_FOR
               POP_ITER

614            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114B70, file "scripts/pas181_manual_test_harness_readiness_check.py", line 617>:
617           RESUME                   0
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

Disassembly of <code object check_no_live_mutation_imports at 0x0000018C17F74350, file "scripts/pas181_manual_test_harness_readiness_check.py", line 617>:
617            RESUME                   0

618            BUILD_LIST               0
               STORE_FAST               1 (out)

619            LOAD_CONST              10 (('app/services/learning/manual_test_harness.py', 'app/services/learning/manual_test_evidence.py', 'app/services/learning/manual_test_scoring.py', 'app/routes/operator_learning_tests.py', 'app/routes/tenant_learning_tests.py'))
               STORE_FAST               2 (files)

626            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     EXTENDED_ARG             1
               FOR_ITER               292 (to L15)
               STORE_FAST               3 (relpath)

627            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

628            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

629            JUMP_BACKWARD           46 (to L1)

630    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

631            BUILD_LIST               0
               STORE_FAST               6 (bad)

632            LOAD_FAST_BORROW         5 (src)
               LOAD_ATTR                7 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L4:     FOR_ITER               107 (to L10)
               STORE_FAST               7 (line)

633            LOAD_FAST_BORROW         7 (line)
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               STORE_FAST               8 (stripped)

634            LOAD_FAST_BORROW         8 (stripped)
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

635    L5:     JUMP_BACKWARD           52 (to L4)

636    L6:     LOAD_GLOBAL             12 (FORBIDDEN_LIVE_MUTATION_IMPORTS)
               GET_ITER
       L7:     FOR_ITER                45 (to L9)
               STORE_FAST               9 (prefix)

637            LOAD_FAST_BORROW         8 (stripped)
               LOAD_ATTR               11 (startswith + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD           28 (to L7)

638    L8:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           47 (to L7)

636    L9:     END_FOR
               POP_ITER
               JUMP_BACKWARD          109 (to L4)

632   L10:     END_FOR
               POP_ITER

639            LOAD_FAST                1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             17 (_check + NULL)

640            LOAD_CONST               3 ('no_live_mutation_import:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

641            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               4 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               5 ('PASS')

642   L12:     LOAD_CONST               6 ('No live-mutation imports: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

644            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       43 (to L13)
               NOT_TAKEN

643            LOAD_CONST               7 ('forbidden imports: ')
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

644   L13:     LOAD_CONST               1 ('')

639   L14:     LOAD_CONST               9 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          295 (to L1)

626   L15:     END_FOR
               POP_ITER

646            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114C60, file "scripts/pas181_manual_test_harness_readiness_check.py", line 649>:
649           RESUME                   0
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

Disassembly of <code object check_audit_service_invariant at 0x0000018C182DD2E0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 649>:
649           RESUME                   0

652           BUILD_LIST               0
              STORE_FAST               1 (out)

653           LOAD_GLOBAL              1 (Path + NULL)
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

654           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               5 ('')
      L1:     STORE_FAST               3 (src)

655           LOAD_CONST              13 (('def update_audit_', 'def delete_audit_', 'def update_operator_audit_', 'def delete_operator_audit_', 'def mutate_audit_', 'def truncate_audit_'))
              STORE_FAST               4 (forbidden)

663           BUILD_LIST               0
              STORE_FAST               5 (bad)

664           LOAD_FAST_BORROW         4 (forbidden)
              GET_ITER
      L2:     FOR_ITER                28 (to L4)
              STORE_FAST               6 (tok)

665           LOAD_FAST_BORROW_LOAD_FAST_BORROW 99 (tok, src)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

666   L3:     LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_FAST_BORROW         6 (tok)
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           30 (to L2)

664   L4:     END_FOR
              POP_ITER

667           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

668           LOAD_CONST               6 ('audit_service:append_only_carry')

669           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               7 ('FAIL')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               8 ('PASS')

670   L6:     LOAD_CONST               9 ('Audit service still has no UPDATE / DELETE mutation helpers (carry-forward invariant)')

671           LOAD_FAST_BORROW         5 (bad)
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

667   L8:     LOAD_CONST              12 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

673           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114D50, file "scripts/pas181_manual_test_harness_readiness_check.py", line 676>:
676           RESUME                   0
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

Disassembly of <code object check_v30_sql at 0x0000018C17F7DB80, file "scripts/pas181_manual_test_harness_readiness_check.py", line 676>:
  --            MAKE_CELL               14 (src)

 676            RESUME                   0

 677            BUILD_LIST               0
                STORE_FAST               1 (out)

 678            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('scripts')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('migrate_v30_learning_manual_test_runs.sql')
                BINARY_OP               11 (/)
                STORE_FAST               2 (p)

 679            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (p)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L1:     STORE_DEREF             14 (src)

 680            LOAD_DEREF              14 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_FAST               3 (lower)

 681            LOAD_CONST               3 ('proposal only')
                LOAD_FAST_BORROW         3 (lower)
                CONTAINS_OP              0 (in)
                STORE_FAST               4 (proposal_ok)

 682            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 683            LOAD_CONST               4 ('v30_sql:proposal_only')

 684            LOAD_FAST_BORROW         4 (proposal_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L2)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               6 ('FAIL')

 685    L3:     LOAD_CONST               7 ("v30 SQL carries 'PROPOSAL ONLY' guardrail")

 686            LOAD_FAST_BORROW         4 (proposal_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L4)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L5)
        L4:     LOAD_CONST               8 ("missing 'PROPOSAL ONLY' label")

 682    L5:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 688            LOAD_CONST              10 ('do not execute')
                LOAD_FAST_BORROW         3 (lower)
                CONTAINS_OP              0 (in)
                STORE_FAST               5 (do_not_exec)

 689            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 690            LOAD_CONST              11 ('v30_sql:do_not_execute')

 691            LOAD_FAST_BORROW         5 (do_not_exec)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L7)
        L6:     LOAD_CONST               6 ('FAIL')

 692    L7:     LOAD_CONST              12 ("v30 SQL carries 'DO NOT EXECUTE' trailer")

 693            LOAD_FAST_BORROW         5 (do_not_exec)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST              13 ('missing trailer')

 689    L9:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 695            LOAD_CONST              14 ('CREATE TABLE IF NOT EXISTS pas_learning_manual_test_runs')
                LOAD_DEREF              14 (src)
                CONTAINS_OP              0 (in)
                STORE_FAST               6 (table_ok)

 696            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 697            LOAD_CONST              15 ('v30_sql:table_present')

 698            LOAD_FAST_BORROW         6 (table_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L11)
       L10:     LOAD_CONST               6 ('FAIL')

 699   L11:     LOAD_CONST              16 ('v30 SQL creates pas_learning_manual_test_runs')

 700            LOAD_FAST_BORROW         6 (table_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L12)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L13)
       L12:     LOAD_CONST              17 ('missing CREATE TABLE')

 696   L13:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 703            LOAD_GLOBAL             10 (all)
                COPY                     1
                LOAD_COMMON_CONSTANT     3 (<built-in function all>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L17)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW        14 (src)
                BUILD_TUPLE              1
                LOAD_CONST              18 (<code object <genexpr> at 0x0000018C18025730, file "scripts/pas181_manual_test_harness_readiness_check.py", line 703>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 704            LOAD_CONST              56 (("'PLANNED'", "'RUNNING'", "'COMPLETED'", "'FAILED'", "'CANCELLED'"))
                GET_ITER

 703            CALL                     0
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
                LOAD_FAST_BORROW        14 (src)
                BUILD_TUPLE              1
                LOAD_CONST              18 (<code object <genexpr> at 0x0000018C18025730, file "scripts/pas181_manual_test_harness_readiness_check.py", line 703>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 704            LOAD_CONST              56 (("'PLANNED'", "'RUNNING'", "'COMPLETED'", "'FAILED'", "'CANCELLED'"))
                GET_ITER

 703            CALL                     0
                CALL                     1
       L18:     STORE_FAST               7 (status_ok)

 712            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 713            LOAD_CONST              21 ('v30_sql:closed_status_enum')

 714            LOAD_FAST_BORROW         7 (status_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L19)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L20)
       L19:     LOAD_CONST               6 ('FAIL')

 715   L20:     LOAD_CONST              22 ('v30 SQL carries the closed status enum')

 716            LOAD_FAST_BORROW         7 (status_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L21)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L22)
       L21:     LOAD_CONST              23 ('missing one or more status literals')

 712   L22:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 718            LOAD_GLOBAL             12 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L26)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW        14 (src)
                BUILD_TUPLE              1
                LOAD_CONST              24 (<code object <genexpr> at 0x0000018C18025C30, file "scripts/pas181_manual_test_harness_readiness_check.py", line 718>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 719            LOAD_CONST              57 (("'LIVE'", "'APPLIED'", "'AUTO_APPLIED'", "'DEPLOYED'"))
                GET_ITER

 718            CALL                     0
       L23:     FOR_ITER                12 (to L25)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L24)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L23)
       L24:     POP_ITER
                LOAD_CONST              20 (True)
                JUMP_FORWARD            20 (to L27)
       L25:     END_FOR
                POP_ITER
                LOAD_CONST              19 (False)
                JUMP_FORWARD            16 (to L27)
       L26:     PUSH_NULL
                LOAD_FAST_BORROW        14 (src)
                BUILD_TUPLE              1
                LOAD_CONST              24 (<code object <genexpr> at 0x0000018C18025C30, file "scripts/pas181_manual_test_harness_readiness_check.py", line 718>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 719            LOAD_CONST              57 (("'LIVE'", "'APPLIED'", "'AUTO_APPLIED'", "'DEPLOYED'"))
                GET_ITER

 718            CALL                     0
                CALL                     1
       L27:     STORE_FAST               8 (forbidden_status_in_sql)

 721            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 722            LOAD_CONST              25 ('v30_sql:no_forbidden_status')

 723            LOAD_FAST_BORROW         8 (forbidden_status_in_sql)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L28)
                NOT_TAKEN
                LOAD_CONST               6 ('FAIL')
                JUMP_FORWARD             1 (to L29)
       L28:     LOAD_CONST               5 ('PASS')

 724   L29:     LOAD_CONST              26 ('v30 SQL must not carry forbidden status tokens (LIVE / APPLIED / AUTO_APPLIED / DEPLOYED)')

 725            LOAD_FAST_BORROW         8 (forbidden_status_in_sql)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L30)
                NOT_TAKEN
                LOAD_CONST              27 ('forbidden status literal present')
                JUMP_FORWARD             1 (to L31)
       L30:     LOAD_CONST               2 ('')

 721   L31:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 728            LOAD_GLOBAL             10 (all)
                COPY                     1
                LOAD_COMMON_CONSTANT     3 (<built-in function all>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L35)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW        14 (src)
                BUILD_TUPLE              1
                LOAD_CONST              28 (<code object <genexpr> at 0x0000018C18024F30, file "scripts/pas181_manual_test_harness_readiness_check.py", line 728>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 729            LOAD_CONST              58 (("'SIMULATION_ONLY'", "'OBSERVATIONAL_ONLY'"))
                GET_ITER

 728            CALL                     0
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
                LOAD_FAST_BORROW        14 (src)
                BUILD_TUPLE              1
                LOAD_CONST              28 (<code object <genexpr> at 0x0000018C18024F30, file "scripts/pas181_manual_test_harness_readiness_check.py", line 728>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 729            LOAD_CONST              58 (("'SIMULATION_ONLY'", "'OBSERVATIONAL_ONLY'"))
                GET_ITER

 728            CALL                     0
                CALL                     1
       L36:     STORE_FAST               9 (mode_ok)

 731            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 732            LOAD_CONST              29 ('v30_sql:closed_mode_enum')

 733            LOAD_FAST_BORROW         9 (mode_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L37)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L38)
       L37:     LOAD_CONST               6 ('FAIL')

 734   L38:     LOAD_CONST              30 ('v30 SQL carries the closed mode enum')

 735            LOAD_FAST_BORROW         9 (mode_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L39)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L40)
       L39:     LOAD_CONST              31 ('missing one or more mode literals')

 731   L40:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 738            LOAD_CONST              32 ("'^[0-9a-f]{64}$'")
                LOAD_DEREF              14 (src)
                CONTAINS_OP              0 (in)
                STORE_FAST              10 (sha_chk)

 739            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 740            LOAD_CONST              33 ('v30_sql:fingerprint_check_constraint')

 741            LOAD_FAST_BORROW        10 (sha_chk)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L41)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L42)
       L41:     LOAD_CONST               6 ('FAIL')

 742   L42:     LOAD_CONST              34 ('v30 SQL pins evidence_fingerprint to sha256 hex shape')

 743            LOAD_FAST_BORROW        10 (sha_chk)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L43)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L44)
       L43:     LOAD_CONST              35 ('missing ^[0-9a-f]{64}$ regex')

 739   L44:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 748            LOAD_CONST              36 ('pas_learning_manual_test_runs_tenant_no_insert')
                LOAD_DEREF              14 (src)
                CONTAINS_OP              0 (in)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       58 (to L45)
                NOT_TAKEN
                POP_TOP

 749            LOAD_CONST              37 ('pas_learning_manual_test_runs_tenant_no_update')
                LOAD_DEREF              14 (src)
                CONTAINS_OP              0 (in)

 748            COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       45 (to L45)
                NOT_TAKEN
                POP_TOP

 750            LOAD_CONST              38 ('pas_learning_manual_test_runs_tenant_no_delete')
                LOAD_DEREF              14 (src)
                CONTAINS_OP              0 (in)

 748            COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       32 (to L45)
                NOT_TAKEN
                POP_TOP

 751            LOAD_CONST              39 ('pas_learning_manual_test_runs_service_role_no_delete')
                LOAD_DEREF              14 (src)
                CONTAINS_OP              0 (in)

 748            COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L45)
                NOT_TAKEN
                POP_TOP

 752            LOAD_CONST              40 ('pas_learning_manual_test_runs_service_role_review_update')
                LOAD_DEREF              14 (src)
                CONTAINS_OP              0 (in)

 748            COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        6 (to L45)
                NOT_TAKEN
                POP_TOP

 753            LOAD_CONST              41 ("WITH CHECK (status = 'PLANNED')")
                LOAD_DEREF              14 (src)
                CONTAINS_OP              0 (in)

 747   L45:     STORE_FAST              11 (policies_ok)

 755            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 756            LOAD_CONST              42 ('v30_sql:append_only_with_review_update')

 757            LOAD_FAST_BORROW        11 (policies_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L46)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L47)
       L46:     LOAD_CONST               6 ('FAIL')

 758   L47:     LOAD_CONST              43 ('v30 SQL denies tenant writes; service_role INSERT PLANNED-only; restricted operator UPDATE; no DELETE')

 759            LOAD_FAST_BORROW        11 (policies_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L48)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L49)
       L48:     LOAD_CONST              44 ('missing one or more required policies')

 755   L49:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 762            LOAD_CONST              45 ('pas_learning_manual_test_runs_tenant_select')
                LOAD_DEREF              14 (src)
                CONTAINS_OP              0 (in)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        6 (to L50)
                NOT_TAKEN
                POP_TOP

 763            LOAD_CONST              46 ("brokerage_id = (auth.jwt() ->> 'brokerage_id')")
                LOAD_DEREF              14 (src)
                CONTAINS_OP              0 (in)

 761   L50:     STORE_FAST              12 (select_scoped)

 765            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 766            LOAD_CONST              47 ('v30_sql:tenant_select_scoped')

 767            LOAD_FAST_BORROW        12 (select_scoped)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L51)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L52)
       L51:     LOAD_CONST               6 ('FAIL')

 768   L52:     LOAD_CONST              48 ('v30 SQL scopes tenant SELECT to own brokerage_id')

 769            LOAD_FAST_BORROW        12 (select_scoped)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L53)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L54)
       L53:     LOAD_CONST              49 ('missing tenant SELECT policy')

 765   L54:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 773            LOAD_CONST              50 ('>= 0 AND score <= 1')
                LOAD_DEREF              14 (src)
                CONTAINS_OP              0 (in)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L55)
                NOT_TAKEN
                POP_TOP

 774            LOAD_CONST              51 ('>= 0 AND confidence_score <= 1')
                LOAD_DEREF              14 (src)
                CONTAINS_OP              0 (in)

 773            COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        6 (to L55)
                NOT_TAKEN
                POP_TOP

 775            LOAD_CONST              52 ('>= 0 AND risk_score <= 1')
                LOAD_DEREF              14 (src)
                CONTAINS_OP              0 (in)

 772   L55:     STORE_FAST              13 (score_chk)

 777            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 778            LOAD_CONST              53 ('v30_sql:score_bounds')

 779            LOAD_FAST_BORROW        13 (score_chk)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L56)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L57)
       L56:     LOAD_CONST               6 ('FAIL')

 780   L57:     LOAD_CONST              54 ('v30 SQL pins score/confidence/risk to [0,1]')

 781            LOAD_FAST_BORROW        13 (score_chk)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L58)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L59)
       L58:     LOAD_CONST              55 ('missing one or more score range CHECKs')

 777   L59:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 783            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18025730, file "scripts/pas181_manual_test_harness_readiness_check.py", line 703>:
  --           COPY_FREE_VARS           1

 703           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 704   L2:     FOR_ITER                 9 (to L3)
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

Disassembly of <code object <genexpr> at 0x0000018C18025C30, file "scripts/pas181_manual_test_harness_readiness_check.py", line 718>:
  --           COPY_FREE_VARS           1

 718           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 719   L2:     FOR_ITER                 9 (to L3)
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

Disassembly of <code object <genexpr> at 0x0000018C18024F30, file "scripts/pas181_manual_test_harness_readiness_check.py", line 728>:
  --           COPY_FREE_VARS           1

 728           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 729   L2:     FOR_ITER                 9 (to L3)
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

Disassembly of <code object __annotate__ at 0x0000018C18114E40, file "scripts/pas181_manual_test_harness_readiness_check.py", line 786>:
786           RESUME                   0
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

Disassembly of <code object check_event_contract at 0x0000018C1801C9E0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 786>:
786           RESUME                   0

787           BUILD_LIST               0
              STORE_FAST               1 (out)

788           LOAD_GLOBAL              1 (Path + NULL)
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

789           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

790           LOAD_GLOBAL              4 (REQUIRED_EVENT_TYPES)
              GET_ITER
      L2:     FOR_ITER                67 (to L7)
              STORE_FAST               4 (required)

791           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (required, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

792           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

793           LOAD_CONST               5 ('events:')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

794           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               6 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               7 ('FAIL')

795   L4:     LOAD_CONST               8 ('Event contract registers ')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

796           LOAD_FAST_BORROW         5 (ok)
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

792   L6:     LOAD_CONST              10 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           69 (to L2)

790   L7:     END_FOR
              POP_ITER

798           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114F30, file "scripts/pas181_manual_test_harness_readiness_check.py", line 801>:
801           RESUME                   0
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

Disassembly of <code object check_main_router_mounts at 0x0000018C180FC990, file "scripts/pas181_manual_test_harness_readiness_check.py", line 801>:
801           RESUME                   0

802           BUILD_LIST               0
              STORE_FAST               1 (out)

803           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('main.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

804           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               2 ('')
      L1:     STORE_FAST               3 (src)

805           LOAD_CONST              10 (('operator_learning_tests_router', 'tenant_learning_tests_router'))
              STORE_FAST               4 (required)

809           LOAD_FAST_BORROW         4 (required)
              GET_ITER
      L2:     FOR_ITER                74 (to L7)
              STORE_FAST               5 (tok)

810           LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               6 (ok)

811           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

812           LOAD_CONST               3 ('main:mount:')
              LOAD_FAST_BORROW         5 (tok)
              LOAD_CONST               4 (slice(None, 48, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

813           LOAD_FAST_BORROW         6 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               5 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               6 ('FAIL')

814   L4:     LOAD_CONST               7 ('app/main.py mounts ')
              LOAD_FAST_BORROW         5 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

815           LOAD_FAST_BORROW         6 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               2 ('')
              JUMP_FORWARD             5 (to L6)
      L5:     LOAD_CONST               8 ('missing mount token ')
              LOAD_FAST_BORROW         5 (tok)
              CONVERT_VALUE            2 (repr)
              FORMAT_SIMPLE
              BUILD_STRING             2

811   L6:     LOAD_CONST               9 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           76 (to L2)

809   L7:     END_FOR
              POP_ITER

817           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18115020, file "scripts/pas181_manual_test_harness_readiness_check.py", line 820>:
820           RESUME                   0
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

Disassembly of <code object check_no_forbidden_imports at 0x0000018C17F74690, file "scripts/pas181_manual_test_harness_readiness_check.py", line 820>:
820            RESUME                   0

821            BUILD_LIST               0
               STORE_FAST               1 (out)

822            LOAD_CONST              10 (('app/services/learning/manual_test_harness.py', 'app/services/learning/manual_test_evidence.py', 'app/services/learning/manual_test_scoring.py', 'app/routes/operator_learning_tests.py', 'app/routes/tenant_learning_tests.py', 'scripts/pas181_manual_test_harness_readiness_check.py'))
               STORE_FAST               2 (files)

830            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     EXTENDED_ARG             1
               FOR_ITER               292 (to L15)
               STORE_FAST               3 (relpath)

831            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

832            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

833            JUMP_BACKWARD           46 (to L1)

834    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

835            BUILD_LIST               0
               STORE_FAST               6 (bad)

836            LOAD_FAST_BORROW         5 (src)
               LOAD_ATTR                7 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L4:     FOR_ITER               107 (to L10)
               STORE_FAST               7 (line)

837            LOAD_FAST_BORROW         7 (line)
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               STORE_FAST               8 (stripped)

838            LOAD_FAST_BORROW         8 (stripped)
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

839    L5:     JUMP_BACKWARD           52 (to L4)

840    L6:     LOAD_GLOBAL             12 (FORBIDDEN_IMPORT_LINE_PREFIXES)
               GET_ITER
       L7:     FOR_ITER                45 (to L9)
               STORE_FAST               9 (prefix)

841            LOAD_FAST_BORROW         8 (stripped)
               LOAD_ATTR               11 (startswith + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD           28 (to L7)

842    L8:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           47 (to L7)

840    L9:     END_FOR
               POP_ITER
               JUMP_BACKWARD          109 (to L4)

836   L10:     END_FOR
               POP_ITER

843            LOAD_FAST                1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             17 (_check + NULL)

844            LOAD_CONST               3 ('forbidden_import:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

845            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               4 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               5 ('PASS')

846   L12:     LOAD_CONST               6 ('No forbidden imports: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

848            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       43 (to L13)
               NOT_TAKEN

847            LOAD_CONST               7 ('forbidden import prefixes: ')
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

848   L13:     LOAD_CONST               1 ('')

843   L14:     LOAD_CONST               9 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          295 (to L1)

830   L15:     END_FOR
               POP_ITER

850            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18115110, file "scripts/pas181_manual_test_harness_readiness_check.py", line 853>:
853           RESUME                   0
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

Disassembly of <code object check_no_inbox_scan_tokens at 0x0000018C17CC1F60, file "scripts/pas181_manual_test_harness_readiness_check.py", line 853>:
853            RESUME                   0

854            BUILD_LIST               0
               STORE_FAST               1 (out)

855            LOAD_CONST               9 (('app/services/learning/manual_test_harness.py', 'app/services/learning/manual_test_evidence.py', 'app/services/learning/manual_test_scoring.py', 'app/routes/operator_learning_tests.py', 'app/routes/tenant_learning_tests.py'))
               STORE_FAST               2 (files)

862            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               195 (to L11)
               STORE_FAST               3 (relpath)

863            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

864            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

865            JUMP_BACKWARD           45 (to L1)

866    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

867            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         5 (src)
               CALL                     1
               STORE_FAST               6 (executable)

868            BUILD_LIST               0
               STORE_FAST               7 (bad)

869            LOAD_GLOBAL              8 (FORBIDDEN_INBOX_TOKENS)
               GET_ITER
       L4:     FOR_ITER                28 (to L6)
               STORE_FAST               8 (token)

870            LOAD_FAST_BORROW_LOAD_FAST_BORROW 134 (token, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L4)

871    L5:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_FAST_BORROW         8 (token)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L4)

869    L6:     END_FOR
               POP_ITER

872            LOAD_FAST                1 (out)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_GLOBAL             13 (_check + NULL)

873            LOAD_CONST               2 ('no_inbox_scan:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

874            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L7)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L8)
       L7:     LOAD_CONST               4 ('PASS')

875    L8:     LOAD_CONST               5 ('No inbox-scanning tokens: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

877            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L9)
               NOT_TAKEN

876            LOAD_CONST               6 ('inbox-scan tokens present: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               15 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L10)

877    L9:     LOAD_CONST               1 ('')

872   L10:     LOAD_CONST               8 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          197 (to L1)

862   L11:     END_FOR
               POP_ITER

879            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181152F0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 882>:
882           RESUME                   0
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

Disassembly of <code object check_doc_required_clauses at 0x0000018C17E92410, file "scripts/pas181_manual_test_harness_readiness_check.py", line 882>:
  --            MAKE_CELL                8 (lower)

 882            RESUME                   0

 883            BUILD_LIST               0
                STORE_FAST               1 (out)

 884            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('docs')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('pas181_manual_test_execution_harness.md')
                BINARY_OP               11 (/)
                STORE_FAST               2 (doc)

 885            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (doc)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L1:     STORE_FAST               3 (src)

 886            LOAD_FAST_BORROW         3 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_DEREF              8 (lower)

 887            LOAD_CONST              13 ((('purpose', ('purpose',)), ('pas179-pas180', ('relationship to pas179',)), ('simulation-only', ('simulation-only doctrine', 'simulation-only')), ('observational-only', ('observational-only doctrine', 'observational only')), ('no-live-mutation', ('no live mutation', 'no-live-mutation', 'does not mutate live')), ('eligibility', ('approved_for_manual_test eligibility', 'approved_for_manual_test')), ('evidence-packet', ('evidence packet doctrine', 'evidence packet')), ('deterministic-scoring', ('deterministic scoring', 'deterministic scoring doctrine')), ('operator-confirmation', ('operator confirmation gate', 'operator confirmation')), ('tenant-visibility', ('tenant visibility', 'tenant visibility doctrine')), ('future-pas182', ('pas182',)), ('no-gmail', ('no gmail',)), ('no-llm', ('no-llm', 'no llm', 'no-llm / embedding')), ('limitations', ('limitation',)), ('not-built', ('intentionally not built', 'intentionally does not', 'deliberately not'))))
                STORE_FAST               4 (required_phrases)

 917            LOAD_FAST_BORROW         4 (required_phrases)
                GET_ITER
        L2:     FOR_ITER               141 (to L12)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   86 (name, phrases)

 918            LOAD_GLOBAL              6 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         8 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18024C30, file "scripts/pas181_manual_test_harness_readiness_check.py", line 918>)
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
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18024C30, file "scripts/pas181_manual_test_harness_readiness_check.py", line 918>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         6 (phrases)
                GET_ITER
                CALL                     0
                CALL                     1
        L7:     STORE_FAST               7 (present)

 919            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 920            LOAD_CONST               6 ('docs:phrase:')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 921            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               8 ('FAIL')

 922    L9:     LOAD_CONST               9 ('Doctrine doc carries clause: ')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 924            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L10)
                NOT_TAKEN

 923            LOAD_CONST              10 ('expected one of: ')
                LOAD_CONST              11 (' | ')
                LOAD_ATTR               13 (join + NULL|self)
                LOAD_FAST_BORROW         6 (phrases)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L11)

 924   L10:     LOAD_CONST               2 ('')

 919   L11:     LOAD_CONST              12 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          143 (to L2)

 917   L12:     END_FOR
                POP_ITER

 926            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18024C30, file "scripts/pas181_manual_test_harness_readiness_check.py", line 918>:
  --           COPY_FREE_VARS           1

 918           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C181153E0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 929>:
929           RESUME                   0
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

Disassembly of <code object check_self_no_env_or_db at 0x0000018C17D893A0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 929>:
929            RESUME                   0

930            BUILD_LIST               0
               STORE_FAST               1 (out)

931            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_GLOBAL              2 (__file__)
               CALL                     1
               LOAD_ATTR                5 (resolve + NULL|self)
               CALL                     0
               STORE_FAST               2 (self_path)

932            LOAD_GLOBAL              7 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (self_path)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L1:     STORE_FAST               3 (src)

933            LOAD_GLOBAL              9 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               4 (executable)

934            BUILD_LIST               0
               STORE_FAST               5 (bad)

935            LOAD_FAST_BORROW         4 (executable)
               LOAD_ATTR               11 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L2:     FOR_ITER               199 (to L9)
               STORE_FAST               6 (raw_line)

936            LOAD_FAST_BORROW         6 (raw_line)
               LOAD_ATTR               13 (strip + NULL|self)
               CALL                     0
               STORE_FAST               7 (stripped)

937            LOAD_FAST_BORROW         7 (stripped)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN

938            JUMP_BACKWARD           29 (to L2)

939    L3:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              15 (('import dotenv', 'from dotenv'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L4)
               NOT_TAKEN

940            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               1 ('dotenv import')
               CALL                     1
               POP_TOP

941    L4:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              16 (('import supabase', 'from supabase'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L5)
               NOT_TAKEN

942            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               2 ('supabase import')
               CALL                     1
               POP_TOP

943    L5:     LOAD_CONST               3 ('load_dotenv()')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       18 (to L6)
               NOT_TAKEN

944            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               4 ('load_dotenv() call')
               CALL                     1
               POP_TOP

945    L6:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              17 (('os.environ[', 'getenv('))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L7)
               NOT_TAKEN

946            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               5 ('environ read')
               CALL                     1
               POP_TOP

947    L7:     LOAD_CONST               6 ('get_supabase')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD          182 (to L2)

948    L8:     LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               7 ('supabase client call')
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          201 (to L2)

935    L9:     END_FOR
               POP_ITER

949            LOAD_FAST                1 (out)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_GLOBAL             19 (_check + NULL)

950            LOAD_CONST               8 ('self_check:no_env_or_db')

951            LOAD_FAST_BORROW         5 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST               9 ('FAIL')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST              10 ('PASS')

952   L11:     LOAD_CONST              11 ('PAS181 readiness checker never reads .env / touches DB')

953            LOAD_FAST_BORROW         5 (bad)
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

949   L13:     LOAD_CONST              14 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

955            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181154D0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 962>:
962           RESUME                   0
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

Disassembly of <code object _aggregate at 0x0000018C1800B0A0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 962>:
 962            RESUME                   0

 964            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 963            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2

 964    L2:     FOR_ITER                49 (to L7)
                STORE_FAST               1 (c)

 965            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 964    L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L2)

 965    L4:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              2 (SEVERITY_BLOCK)
                COMPARE_OP              88 (bool(==))

 964    L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L2)
        L6:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L2)
        L7:     END_FOR
                POP_ITER

 963    L8:     STORE_FAST               2 (blockers)
                STORE_FAST               1 (c)

 968            LOAD_CONST               3 ('verdict')
                LOAD_FAST_BORROW         2 (blockers)
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L9)
                NOT_TAKEN
                LOAD_GLOBAL              4 (VERDICT_NOT_READY)
                JUMP_FORWARD             5 (to L10)
        L9:     LOAD_GLOBAL              6 (VERDICT_READY)

 969   L10:     LOAD_CONST               4 ('blockers')
                LOAD_FAST_BORROW         2 (blockers)

 970            LOAD_CONST               5 ('info')
                BUILD_LIST               0

 967            BUILD_MAP                3
                RETURN_VALUE

  --   L11:     SWAP                     2
                POP_TOP

 963            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L11 [2]
  L4 to L5 -> L11 [2]
  L6 to L8 -> L11 [2]

Disassembly of <code object __annotate__ at 0x0000018C181155C0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 974>:
974           RESUME                   0
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

Disassembly of <code object _operator_actions at 0x0000018C180483B0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 974>:
974           RESUME                   0

975           BUILD_LIST               0
              STORE_FAST               1 (out)

976           LOAD_FAST_BORROW         0 (checks)
              GET_ITER
      L1:     FOR_ITER               109 (to L5)
              STORE_FAST               2 (c)

977           LOAD_FAST_BORROW         2 (c)
              LOAD_CONST               0 ('status')
              BINARY_OP               26 ([])
              LOAD_CONST               1 ('FAIL')
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

978           JUMP_BACKWARD           19 (to L1)

979   L2:     LOAD_FAST_BORROW         2 (c)
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

980           LOAD_FAST                1 (out)
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

976   L5:     END_FOR
              POP_ITER

981           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18115980, file "scripts/pas181_manual_test_harness_readiness_check.py", line 984>:
984           RESUME                   0
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

Disassembly of <code object evaluate at 0x0000018C177C69F0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 984>:
 984           RESUME                   0

 985           BUILD_LIST               0
               STORE_FAST               1 (checks)

 986           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL              3 (check_files_present + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

 987           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL              5 (check_prior_phases_intact + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

 988           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL              7 (check_memory_review_intact + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

 989           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL              9 (check_worker_off_by_default + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

 990           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             11 (check_no_startup_worker + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

 991           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             13 (check_harness_service + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

 992           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             15 (check_evidence_service + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

 993           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             17 (check_scoring_service + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

 994           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             19 (check_operator_routes + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

 995           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             21 (check_tenant_routes + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

 996           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             23 (check_no_forbidden_status_tokens + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

 997           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             25 (check_no_auto_approval_tokens + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

 998           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             27 (check_no_live_mutation_imports + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

 999           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             29 (check_audit_service_invariant + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1000           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             31 (check_v30_sql + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1001           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             33 (check_event_contract + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1002           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             35 (check_main_router_mounts + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1003           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             37 (check_no_forbidden_imports + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1004           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             39 (check_no_inbox_scan_tokens + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1005           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             41 (check_doc_required_clauses + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1006           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             43 (check_self_no_env_or_db + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1008           LOAD_GLOBAL             45 (_aggregate + NULL)
               LOAD_FAST_BORROW         1 (checks)
               CALL                     1
               STORE_FAST               2 (agg)

1010           LOAD_CONST               0 ('phase')
               LOAD_CONST               1 ('PAS181')

1011           LOAD_CONST               2 ('generated_at')
               LOAD_GLOBAL             47 (_now_iso + NULL)
               CALL                     0

1012           LOAD_CONST               3 ('verdict')
               LOAD_FAST_BORROW         2 (agg)
               LOAD_CONST               3 ('verdict')
               BINARY_OP               26 ([])

1013           LOAD_CONST               4 ('ready')
               LOAD_FAST_BORROW         2 (agg)
               LOAD_CONST               3 ('verdict')
               BINARY_OP               26 ([])
               LOAD_GLOBAL             48 (VERDICT_READY)
               COMPARE_OP              72 (==)

1014           LOAD_CONST               5 ('blocker_count')
               LOAD_GLOBAL             51 (len + NULL)
               LOAD_FAST_BORROW         2 (agg)
               LOAD_CONST               6 ('blockers')
               BINARY_OP               26 ([])
               CALL                     1

1015           LOAD_CONST               7 ('info_count')
               LOAD_GLOBAL             51 (len + NULL)
               LOAD_FAST_BORROW         2 (agg)
               LOAD_CONST               8 ('info')
               BINARY_OP               26 ([])
               CALL                     1

1016           LOAD_CONST               9 ('check_count')
               LOAD_GLOBAL             51 (len + NULL)
               LOAD_FAST_BORROW         1 (checks)
               CALL                     1

1017           LOAD_CONST              10 ('pass_count')
               LOAD_GLOBAL             53 (sum + NULL)
               LOAD_CONST              11 (<code object <genexpr> at 0x0000018C18053990, file "scripts/pas181_manual_test_harness_readiness_check.py", line 1017>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         1 (checks)
               GET_ITER
               CALL                     0
               CALL                     1

1018           LOAD_CONST              12 ('fail_count')
               LOAD_GLOBAL             53 (sum + NULL)
               LOAD_CONST              13 (<code object <genexpr> at 0x0000018C18053E10, file "scripts/pas181_manual_test_harness_readiness_check.py", line 1018>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         1 (checks)
               GET_ITER
               CALL                     0
               CALL                     1

1019           LOAD_CONST              14 ('checks')
               LOAD_FAST_BORROW         1 (checks)

1020           LOAD_CONST              15 ('operator_actions')
               LOAD_GLOBAL             55 (_operator_actions + NULL)
               LOAD_FAST_BORROW         1 (checks)
               CALL                     1

1009           BUILD_MAP               11
               RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18053990, file "scripts/pas181_manual_test_harness_readiness_check.py", line 1017>:
1017           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C18053E10, file "scripts/pas181_manual_test_harness_readiness_check.py", line 1018>:
1018           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C18115A70, file "scripts/pas181_manual_test_harness_readiness_check.py", line 1027>:
1027           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C180FC7B0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 1027>:
1027           RESUME                   0

1028           LOAD_GLOBAL              0 (argparse)
               LOAD_ATTR                2 (ArgumentParser)
               PUSH_NULL

1029           LOAD_CONST               0 ('pas181_manual_test_harness_readiness_check')

1031           LOAD_CONST               1 ('PAS181 — Evaluate bounded manual-test execution harness (services + routes + audit trail). Read-only — never reads .env, never touches Supabase, never runs a migration.')

1028           LOAD_CONST               2 (('prog', 'description'))
               CALL_KW                  2
               STORE_FAST               0 (p)

1037           LOAD_FAST_BORROW         0 (p)
               LOAD_ATTR                5 (add_argument + NULL|self)
               LOAD_CONST               3 ('--repo-root')
               LOAD_GLOBAL              6 (_REPO_ROOT_DEFAULT)
               LOAD_CONST               4 (('default',))
               CALL_KW                  2
               POP_TOP

1038           LOAD_FAST_BORROW         0 (p)
               LOAD_ATTR                5 (add_argument + NULL|self)
               LOAD_CONST               5 ('--output')
               LOAD_GLOBAL              8 (REPORT_FILENAME)
               LOAD_CONST               4 (('default',))
               CALL_KW                  2
               POP_TOP

1039           LOAD_FAST_BORROW         0 (p)
               LOAD_ATTR                5 (add_argument + NULL|self)
               LOAD_CONST               6 ('--json')
               LOAD_CONST               7 ('store_true')
               LOAD_CONST               8 (('action',))
               CALL_KW                  2
               POP_TOP

1040           LOAD_FAST_BORROW         0 (p)
               LOAD_ATTR                5 (add_argument + NULL|self)
               LOAD_CONST               9 ('--summary-only')
               LOAD_CONST               7 ('store_true')
               LOAD_CONST               8 (('action',))
               CALL_KW                  2
               POP_TOP

1041           LOAD_FAST_BORROW         0 (p)
               LOAD_ATTR                5 (add_argument + NULL|self)
               LOAD_CONST              10 ('--strict')
               LOAD_CONST               7 ('store_true')
               LOAD_CONST               8 (('action',))
               CALL_KW                  2
               POP_TOP

1042           LOAD_FAST_BORROW         0 (p)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18115B60, file "scripts/pas181_manual_test_harness_readiness_check.py", line 1045>:
1045           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C17D8C5C0, file "scripts/pas181_manual_test_harness_readiness_check.py", line 1045>:
1045           RESUME                   0

1046           LOAD_GLOBAL              1 (print + NULL)

1047           LOAD_CONST               0 ('[PAS181] verdict=')
               LOAD_FAST_BORROW         0 (report)
               LOAD_CONST               1 ('verdict')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               LOAD_CONST               2 (' blockers=')

1048           LOAD_FAST_BORROW         0 (report)
               LOAD_CONST               3 ('blocker_count')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               LOAD_CONST               4 (' info=')

1049           LOAD_FAST_BORROW         0 (report)
               LOAD_CONST               5 ('info_count')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               LOAD_CONST               6 (' checks=')

1050           LOAD_FAST_BORROW         0 (report)
               LOAD_CONST               7 ('check_count')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               LOAD_CONST               8 (' pass=')

1051           LOAD_FAST_BORROW         0 (report)
               LOAD_CONST               9 ('pass_count')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               LOAD_CONST              10 (' fail=')

1052           LOAD_FAST_BORROW         0 (report)
               LOAD_CONST              11 ('fail_count')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE

1047           BUILD_STRING            12

1046           CALL                     1
               POP_TOP

1054           LOAD_FAST_BORROW         0 (report)
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

1055           LOAD_FAST_BORROW         1 (actions)
               TO_BOOL
               POP_JUMP_IF_FALSE       93 (to L5)
               NOT_TAKEN

1056           LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST              13 ('[PAS181] operator actions:')
               CALL                     1
               POP_TOP

1057           LOAD_FAST_BORROW         1 (actions)
               LOAD_CONST              14 (slice(None, 25, None))
               BINARY_OP               26 ([])
               GET_ITER
       L2:     FOR_ITER                17 (to L3)
               STORE_FAST               2 (a)

1058           LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST              15 ('  - ')
               LOAD_FAST_BORROW         2 (a)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           19 (to L2)

1057   L3:     END_FOR
               POP_ITER

1059           LOAD_GLOBAL              5 (len + NULL)
               LOAD_FAST_BORROW         1 (actions)
               CALL                     1
               LOAD_SMALL_INT          25
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE       34 (to L4)
               NOT_TAKEN

1060           LOAD_GLOBAL              1 (print + NULL)
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

1059   L4:     LOAD_CONST              18 (None)
               RETURN_VALUE

1055   L5:     LOAD_CONST              18 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026330, file "scripts/pas181_manual_test_harness_readiness_check.py", line 1063>:
1063           RESUME                   0
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

Disassembly of <code object _write_report at 0x0000018C180FCF30, file "scripts/pas181_manual_test_harness_readiness_check.py", line 1063>:
1063           RESUME                   0

1064           NOP

1065   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

1066           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

1067           LOAD_CONST               3 ('utf-8')

1065           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

1069           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

1070   L4:     LOAD_GLOBAL             11 (print + NULL)

1071           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

1072           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

1071           BUILD_STRING             4

1073           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

1070           LOAD_CONST               7 (('file',))
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

1069   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18115C50, file "scripts/pas181_manual_test_harness_readiness_check.py", line 1077>:
1077           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17D89750, file "scripts/pas181_manual_test_harness_readiness_check.py", line 1077>:
1077            RESUME                   0

1078            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

1079            NOP

1080    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

1084    L2:     LOAD_GLOBAL             10 (os)
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

1085            LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               21 (isdir + NULL|self)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L4)
                NOT_TAKEN

1086            LOAD_GLOBAL             23 (print + NULL)
                LOAD_CONST               2 ('error: --repo-root not a directory: ')
                LOAD_FAST                4 (repo_root)
                FORMAT_SIMPLE
                BUILD_STRING             2
                LOAD_GLOBAL             24 (sys)
                LOAD_ATTR               26 (stderr)
                LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

1087            LOAD_SMALL_INT           2
                RETURN_VALUE

1089    L4:     LOAD_GLOBAL             29 (evaluate + NULL)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                STORE_FAST               5 (report)

1091            LOAD_FAST                2 (args)
                LOAD_ATTR               30 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L5)
                NOT_TAKEN

1092            LOAD_GLOBAL             33 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               34 (output)
                LOAD_FAST                5 (report)
                CALL                     2
                POP_TOP

1094    L5:     LOAD_GLOBAL             37 (_print_summary + NULL)
                LOAD_FAST                5 (report)
                CALL                     1
                POP_TOP

1096            LOAD_FAST                2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L6)
                NOT_TAKEN

1097            LOAD_GLOBAL             23 (print + NULL)
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

1099    L6:     LOAD_FAST                5 (report)
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

1081            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L17)
                NOT_TAKEN
                STORE_FAST               3 (e)

1082    L9:     LOAD_FAST                3 (e)
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

1081   L17:     RERAISE                  0

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
