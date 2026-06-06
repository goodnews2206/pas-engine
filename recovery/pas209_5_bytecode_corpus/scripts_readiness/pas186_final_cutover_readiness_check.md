# scripts_readiness/pas186_final_cutover_readiness_check

- **pyc:** `scripts\__pycache__\pas186_final_cutover_readiness_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/pas186_final_cutover_readiness_check.py`
- **co_filename (from bytecode):** `C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS186 — Final pilot cutover readiness gate.

Deterministic, non-mutating evaluator for "is ORVN's pilot
cutover surface intact, complete, and free of regressions
across the PAS160-PAS185 + PAS-SECURITY-01/02/03/04 doctrine?".

This is the **final** readiness gate before the first
external brokerage onboarding. It does NOT execute any
deploy, migration, rollback, or recommendation. It does NOT
read .env. It does NOT touch Supabase. It does NOT call any
network. It walks the repo, asserts invariants on disk, and
emits a structural verdict envelope.

Target check budget: >= 120.

Exit codes:
  0 — READY
  1 — NOT_READY (one or more BLOCK checks failed)
  2 — bad CLI args
```

## Imports

`List`, `Optional`, `Path`, `Tuple`, `__future__`, `annotations`, `argparse`, `datetime`, `json`, `os`, `pathlib`, `sys`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_aggregate`, `_build_parser`, `_check`, `_now_iso`, `_operator_actions`, `_print_summary`, `_read_text`, `_strip_python_comments_and_strings`, `_write_report`, `check_audit_service_append_only`, `check_dashboard_anchors_present`, `check_dashboard_no_forbidden_tokens`, `check_learning_dashboard_no_mutation`, `check_main_mounts_required_routers`, `check_main_no_autostart_worker`, `check_memory_review_intact`, `check_no_forbidden_future_migrations`, `check_no_live_adaptive_memory_mutation`, `check_no_live_learning_mutation`, `check_no_raw_key_reveal`, `check_no_wildcard_cors`, `check_pas185_mounts_present`, `check_pas186_doc_clauses`, `check_pas186_docs_no_forbidden_scope`, `check_pas186_files_present`, `check_prior_readiness_gates_callable`, `check_required_migrations_present`, `check_self_no_deploy_execution`, `check_self_no_env_or_db`, `check_tenant_routes_read_only`, `evaluate`, `main`

## Env-key candidates

`BLOCK`, `DOC_REQUIRED_CLAUSES`, `FAIL`, `NOT_READY`, `PAS186`, `PASS`, `READY`

## String constants (redacted where noted)

- '\nPAS186 — Final pilot cutover readiness gate.\n\nDeterministic, non-mutating evaluator for "is ORVN\'s pilot\ncutover surface intact, complete, and free of regressions\nacross the PAS160-PAS185 + PAS-SECURITY-01/02/03/04 doctrine?".\n\nThis is the **final** readiness gate before the first\nexternal brokerage onboarding. It does NOT execute any\ndeploy, migration, rollback, or recommendation. It does NOT\nread .env. It does NOT touch Supabase. It does NOT call any\nnetwork. It walks the repo, asserts invariants on disk, and\nemits a structural verdict envelope.\n\nTarget check budget: >= 120.\n\nExit codes:\n  0 — READY\n  1 — NOT_READY (one or more BLOCK checks failed)\n  2 — bad CLI args\n'
- 'utf-8'
- 'READY'
- 'NOT_READY'
- 'BLOCK'
- 'Tuple[Tuple[str, Tuple[Tuple[str, Tuple[str, ...]], ...]], ...]'
- 'DOC_REQUIRED_CLAUSES'
- 'app/static/dashboard/index.html'
- 'allow_origins=["*"]'
- 'app/services/operator/audit_service.py'
- 'app/routes/operator_learning_dashboard.py'
- 'app/routes/security_api_key_rotation.py'
- 'severity'
- 'detail'
- 'pas186_final_cutover_readiness_report.json'
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
- 'Required PAS186 file present: '
- 'missing'
- 'prior_gate:'
- 'Prior readiness gate present: '
- 'missing — cutover § 1 step 3 would fail'
- 'def main('
- 'if __name__'
- 'prior_gate_entrypoint:'
- 'Prior readiness gate has main entrypoint: '
- 'no main() / __main__ guard'
- 'migration:'
- 'Required migration on disk: '
- 'missing — cutover § 2 cannot promote'
- 'scripts'
- 'future_migrations:scripts_dir_present'
- 'scripts/ directory missing'
- 'repo layout broken'
- 'scripts/ directory present'
- 'migrate_v'
- '.sql'
- 'future_migrations:no_unratified'
- 'No migration > v'
- ' on disk (unratified future migrations would violate cutover § 2)'
- 'unratified: '
- 'combined_supabase_migration.sql'
- 'future_migrations:combined_offlimits_left_alone'
- 'combined_supabase_migration.sql is left alone (off-limits per project memory)'
- 'present and untouched'
- 'not on disk'
- 'doc:'
- ':clause:'
- ' carries clause: '
- 'missing any of: '
- 'doc_scope:'
- ' introduces no out-of-scope feature token'
- 'disqualifying: '
- 'dashboard:'
- 'Dashboard anchor present: '
- 'anchor missing'
- 'dashboard_forbidden:'
- 'Dashboard carries no forbidden token: '
- 'token observed — out of scope'
- 'PAS185-A mount-point integrity (the helpers must be\ninvoked from existing admin loaders).'
- 'PAS185-A mount artefact present: '
- 'missing — operator surface invisible'
- 'app'
- 'main.py'
- 'main_no_autostart:'
- 'app/main.py does not auto-start: '
- 'forbidden token in executable code'
- 'main_router:'
- 'app/main.py mounts router: '
- 'operator surface not mounted'
- 'app/main.py'
- 'cors:no_wildcard_in_main'
- 'app/main.py does not configure wildcard CORS origins'
- 'docs/pas186_final_pilot_cutover.md'
- 'wildcard cors'
- 'cors:doc_clause_present'
- 'Cutover doctrine names wildcard-CORS ban'
- 'missing wildcard cors clause'
- 'audit_service:no_'
- 'audit_service.py free of mutation helper: '
- 'disqualifying token'
- 'learning_route:no_'
- ' declares no '
- 'forbidden decorator in executable code'
- 'Walk all admin route files and ensure none introduces a\nPOST/PATCH/DELETE/PUT mutating a learning_* resource.'
- 'routes'
- '*.py'
- 'no_live_learning_mutation'
- 'No admin route declares mutation against a learning_* resource'
- 'Same shape as the learning-mutation check but scoped to\nadaptive-memory.'
- 'no_live_adaptive_memory_mutation'
- 'No admin route declares mutation against an adaptive-memory resource'
- 'tenant_readonly:'
- ' does not declare '
- ' against /audit'
- 'No source file (other than the official rotation route)\nmay carry a raw-key reveal pattern.'
- 'no_raw_key_reveal:outside_official_route'
- 'No raw-key reveal outside the official rotation route'
- 'no_raw_key_reveal:official_route_present'
- 'Official key-rotation route present: '
- 'memory_review:'
- 'Memory Review file present: '
- 'PAS147-158 surface broken'
- 'dotenv import'
- 'supabase import'
- 'load_dotenv('
- 'load_dotenv() call'
- 'environ read'
- 'get_supabase'
- 'supabase client call'
- 'self_check:no_env_or_db'
- 'PAS186 readiness checker never reads .env / touches DB'
- 'The PAS186 readiness check must NEVER execute a deploy,\nmigration, rollback, or HTTP call to any external service.'
- 'self_check:no_deploy_execution'
- 'PAS186 readiness checker never executes a deploy / migration / network call'
- 'checks'
- 'verdict'
- 'blockers'
- 'info'
- 'List[str]'
- ' — '
- 'see report'
- 'phase'
- 'PAS186'
- 'generated_at'
- 'ready'
- 'blocker_count'
- 'info_count'
- 'check_count'
- 'pass_count'
- 'fail_count'
- 'operator_actions'
- 'argparse.ArgumentParser'
- 'pas186_final_cutover_readiness_check'
- 'PAS186 — Final pilot cutover readiness gate. Read-only — never reads .env, never touches Supabase, never executes a deploy / migration / rollback.'
- '--repo-root'
- '--output'
- '--json'
- 'store_true'
- '--summary-only'
- '--strict'
- 'report'
- 'None'
- '[PAS186] verdict='
- ' blockers='
- ' info='
- ' checks='
- ' pass='
- ' fail='
- '[PAS186] operator actions:'
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
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS186 — Final pilot cutover readiness gate.\n\nDeterministic, non-mutating evaluator for "is ORVN\'s pilot\ncutover surface intact, complete, and free of regressions\nacross the PAS160-PAS185 + PAS-SECURITY-01/02/03/04 doctrine?".\n\nThis is the **final** readiness gate before the first\nexternal brokerage onboarding. It does NOT execute any\ndeploy, migration, rollback, or recommendation. It does NOT\nread .env. It does NOT touch Supabase. It does NOT call any\nnetwork. It walks the repo, asserts invariants on disk, and\nemits a structural verdict envelope.\n\nTarget check budget: >= 120.\n\nExit codes:\n  0 — READY\n  1 — NOT_READY (one or more BLOCK checks failed)\n  2 — bad CLI args\n')
               STORE_NAME               1 (__doc__)

  23           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  25           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (argparse)
               STORE_NAME               4 (argparse)

  26           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (json)
               STORE_NAME               5 (json)

  27           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (os)
               STORE_NAME               6 (os)

  28           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              7 (sys)
               STORE_NAME               7 (sys)

  29           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              8 (datetime)
               IMPORT_FROM              8 (datetime)
               STORE_NAME               8 (datetime)
               IMPORT_FROM              9 (timezone)
               STORE_NAME               9 (timezone)
               POP_TOP

  30           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Path',))
               IMPORT_NAME             10 (pathlib)
               IMPORT_FROM             11 (Path)
               STORE_NAME              11 (Path)
               POP_TOP

  31           LOAD_SMALL_INT           0
               LOAD_CONST               5 (('List', 'Optional', 'Tuple'))
               IMPORT_NAME             12 (typing)
               IMPORT_FROM             13 (List)
               STORE_NAME              13 (List)
               IMPORT_FROM             14 (Optional)
               STORE_NAME              14 (Optional)
               IMPORT_FROM             15 (Tuple)
               STORE_NAME              15 (Tuple)
               POP_TOP

  34           LOAD_NAME                7 (sys)
               LOAD_ATTR               32 (stdout)
               LOAD_NAME                7 (sys)
               LOAD_ATTR               34 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              18 (_stream)

  35           NOP

  36   L2:     LOAD_NAME               18 (_stream)
               LOAD_ATTR               39 (reconfigure + NULL|self)
               LOAD_CONST               6 ('utf-8')
               LOAD_CONST               7 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  34   L4:     END_FOR
               POP_ITER

  41           LOAD_NAME                6 (os)
               LOAD_ATTR               42 (path)
               LOAD_ATTR               45 (abspath + NULL|self)

  42           LOAD_NAME                6 (os)
               LOAD_ATTR               42 (path)
               LOAD_ATTR               47 (join + NULL|self)
               LOAD_NAME                6 (os)
               LOAD_ATTR               42 (path)
               LOAD_ATTR               49 (dirname + NULL|self)
               LOAD_NAME               25 (__file__)
               CALL                     1
               LOAD_CONST               8 ('..')
               CALL                     2

  41           CALL                     1
               STORE_NAME              26 (_REPO_ROOT_DEFAULT)

  46           LOAD_CONST               9 ('READY')
               STORE_NAME              27 (VERDICT_READY)

  47           LOAD_CONST              10 ('NOT_READY')
               STORE_NAME              28 (VERDICT_NOT_READY)

  49           LOAD_CONST              11 ('BLOCK')
               STORE_NAME              29 (SEVERITY_BLOCK)

  56           LOAD_CONST              88 (('docs/pas186_final_pilot_cutover.md', 'docs/orvn_brokerage_cutover_checklist.md', 'docs/orvn_daily_pilot_operations_checklist.md', 'scripts/pas186_final_cutover_readiness_check.py', 'tests/mvp/test_pas186_final_cutover.py'))
               STORE_NAME              30 (PAS186_FILES)

  69           LOAD_CONST              89 (('scripts/pas160_mvp_sequence_check.py', 'scripts/pas161_lead_ingestion_readiness_check.py', 'scripts/pas162_pending_calls_readiness_check.py', 'scripts/pas163_candidate_pipeline_readiness_check.py', 'scripts/pas164_email_ingestion_readiness_check.py', 'scripts/pas165_email_auth_dedupe_readiness_check.py', 'scripts/pas166_email_dedupe_policy_readiness_check.py', 'scripts/pas167_email_secret_reaper_readiness_check.py', 'scripts/pas168_email_secret_rotation_readiness_check.py', 'scripts/pas169_crypto_roundtrip_check.py', 'scripts/pas169_launch_readiness_check.py', 'scripts/pas_launch_integrity_check.py', 'scripts/pas170_operator_survival_readiness_check.py', 'scripts/pas171_external_pilot_readiness_check.py', 'scripts/pas172_pilot_operations_readiness_check.py', 'scripts/pas173_brokerage_operator_readiness_check.py', 'scripts/pas174_operator_audit_readiness_check.py', 'scripts/pas175_audit_integrity_readiness_check.py', 'scripts/pas176_audit_chain_readiness_check.py', 'scripts/pas177_tenant_audit_verification_readiness_check.py', 'scripts/pas178_audit_window_chain_readiness_check.py', 'scripts/pas179_controlled_learning_readiness_check.py', 'scripts/pas180_learning_review_readiness_check.py', 'scripts/pas181_manual_test_harness_readiness_check.py', 'scripts/pas182_adaptive_memory_bridge_readiness_check.py', 'scripts/pas183_onboarding_product_readiness_check.py', 'scripts/pas184_pilot_experience_readiness_check.py', 'scripts/pas_security_01_hardening_readiness_check.py', 'scripts/pas_security_02_rate_limit_scanner_readiness_check.py', 'scripts/pas_security_03_admin_webhook_ci_readiness_check.py', 'scripts/pas_security_04_operator_reveal_https_readiness_check.py', 'scripts/pre_pas144_readiness_check.py'))
               STORE_NAME              31 (PRIOR_READINESS_GATES)

 107           LOAD_CONST              90 (('scripts/migrate_v2.sql', 'scripts/migrate_v3.sql', 'scripts/migrate_v4.sql', 'scripts/migrate_v5.sql', 'scripts/migrate_v6.sql', 'scripts/migrate_v7.sql', 'scripts/migrate_v8_event_contract.sql', 'scripts/migrate_v9_column_privileges.sql', 'scripts/migrate_v10_memory_store.sql', 'scripts/migrate_v11_memory_review_audit.sql', 'scripts/migrate_v12_memory_rollout_ledger.sql', 'scripts/migrate_v13_memory_rollout_manifests.sql', 'scripts/migrate_v14_pending_calls.sql', 'scripts/migrate_v15_email_dedupe.sql', 'scripts/migrate_v16_email_secret_encryption.sql', 'scripts/migrate_v17_callback_schedule.sql', 'scripts/migrate_v18_pending_call_dedupe.sql', 'scripts/migrate_v19_callback_schedule.sql', 'scripts/migrate_v20_worker_heartbeats.sql', 'scripts/migrate_v21_brokerage_profiles.sql', 'scripts/migrate_v22_operator_actions_log.sql', 'scripts/migrate_v23_audit_hash_chain.sql', 'scripts/migrate_v24_audit_merkle_roots.sql', 'scripts/migrate_v25_tenant_audit_acknowledgements.sql', 'scripts/migrate_v26_audit_window_chain.sql', 'scripts/migrate_v27_audit_verification_runs.sql', 'scripts/migrate_v28_learning_recommendations.sql', 'scripts/migrate_v29_simulation_runs.sql', 'scripts/migrate_v30_learning_manual_test_runs.sql', 'scripts/migrate_v31_rate_limit_counters.sql', 'scripts/migrate_v32_api_key_rotation_events.sql', 'scripts/migrate_v33_rate_limit_atomic_rpc.sql', 'scripts/migrate_v34_api_key_one_time_reveal.sql'))
               STORE_NAME              32 (REQUIRED_MIGRATIONS)

 155           LOAD_SMALL_INT          38
               STORE_NAME              33 (MAX_RATIFIED_MIGRATION_V)

 160           LOAD_CONST              91 ((('docs/pas186_final_pilot_cutover.md', (('hard-constraints', ('hard constraints',)), ('exact-deploy-order', ('exact deploy order',)), ('exact-migration', ('exact migration-promotion order', 'exact migration promotion order')), ('exact-env-var', ('exact env-var order', 'exact env var order')), ('exact-rollback', ('exact rollback order',)), ('operator-ownership', ('operator ownership boundaries',)), ('required-daily-checks', ('required daily checks',)), ('stop-the-rollout', ('stop-the-rollout', 'stop the rollout')), ('escalation-rules', ('escalation rules',)), ('severity-matrix', ('pilot severity matrix', 'severity matrix')), ('first-48-hour', ('first-48-hour', 'first 48-hour')), ('data-handling', ('data-handling doctrine', 'data handling doctrine')), ('no-pii-export', ('no-pii-export', 'no pii export')), ('operator-communication', ('operator communication doctrine',)), ('no-engine-fsm', ('no engine fsm',)), ('no-new-route', ('no new route',)), ('no-new-dependency', ('no new dependency', 'no new dependencies')), ('no-auto-execution', ('no auto-execution', 'no auto execution', 'auto-execute')), ('no-gmail', ('no gmail',)), ('no-composio', ('no composio', 'composio')), ('no-ai-chat', ('no ai chat', 'ai chat assistant')), ('no-slack-employee', ('slack employee-mode', 'slack employee mode')), ('no-learning-autopilot', ('learning autopilot',)), ('no-adaptive-autowrite', ('adaptive-memory autowrite', 'adaptive memory autowrite')), ('rollback-timeline', ('≤ 15 minutes', '<= 15 minutes', '15 minutes')), ('pas185-snapshot', ('pilot ops snapshot', 'pilot-ops snapshot')), ('readiness-gate-source', ('single source of truth',)))), ('docs/orvn_brokerage_cutover_checklist.md', (('pre-onboarding', ('pre-onboarding qualification',)), ('brokerage-readiness', ('brokerage readiness criteria',)), ('twilio-readiness', ('twilio readiness',)), ('slack-readiness', ('slack readiness',)), ('webhook-readiness', ('webhook readiness',)), ('api-key-readiness', ('api-key readiness', 'api key readiness')), ('timezone-verification', ('timezone verification',)), ('callback-expectations', ('callback expectations',)), ('operator-escalation', ('operator escalation path',)), ('rollback-expectations', ('rollback expectations',)), ('signed-pilot', ('signed pilot expectations', 'pilot operating agreement')), ('sixty-second-flow', ('60-second onboarding', '60 second onboarding', 'exact 60-second')), ('post-go-live', ('post-go-live verification', 'post go live verification')), ('no-raw-key-slack', ('no raw key value', 'raw values never pasted', 'never pasted in slack')), ('deferred-reveal', ('deferred-reveal', 'deferred reveal')), ('no-pii-paste', ('no pii / no secrets', 'no pii pasted', 'no raw secret')), ('rollback-timeline', ('≤ 15 min', '<= 15 min', '15 min')))), ('docs/orvn_daily_pilot_operations_checklist.md', (('queue-depth', ('queue-depth review',)), ('stale-dialing', ('stale-dialing review',)), ('callback-review', ('callback review',)), ('booking-review', ('booking review',)), ('audit-verification', ('audit verification review',)), ('learning-recommendation', ('learning recommendation review',)), ('rate-limit', ('rate-limit review',)), ('verification-run', ('verification-run review',)), ('broker-pulse', ('broker satisfaction pulse',)), ('incident-logging', ('incident logging discipline',)), ('no-mutation-invoked', ('no mutation surfaces invoked',)), ('no-pii-captured', ('no pii captured',)), ('daily-signoff', ('daily sign-off', 'daily signoff')), ('autopilot-disabled', ('learning_autopilot_enabled',)), ('adaptive-autowrite-disabled', ('adaptive_memory_autowrite_enabled',))))))
               STORE_NAME              34 (DOC_REQUIRED_CLAUSES)
               LOAD_CONST              12 ('Tuple[Tuple[str, Tuple[Tuple[str, Tuple[str, ...]], ...]], ...]')
               LOAD_NAME               35 (__annotations__)
               LOAD_CONST              13 ('DOC_REQUIRED_CLAUSES')
               STORE_SUBSCR

 262           LOAD_CONST              92 (('gmail oauth integration', 'composio integration', 'trustclaw', 'auto-approve memory', 'ai chat assistant enabled', 'embedding model', 'vector database', 'vector db', 'imap inbox', 'pop3 inbox'))
               STORE_NAME              36 (FORBIDDEN_DOC_TOKENS)

 276           LOAD_CONST              14 ('app/static/dashboard/index.html')
               STORE_NAME              37 (DASHBOARD_FILE)

 280           LOAD_CONST              93 ((('pas184:error-banner-class', '.pas-error-banner'), ('pas184:skeleton-class', '.pas-skeleton'), ('pas184:js-namespace', 'window.PAS'), ('pas184:js-error-helper', 'errorBannerHtml'), ('pas184:js-skeleton-helper', 'skeletonRowsHtml'), ('pas184:js-error-code-label', 'errorCodeLabel'), ('pas185:pilot-ops-helper', 'loadPilotOpsSnapshot'), ('pas185:learning-helper', 'loadOperatorLearningDashboard'), ('pas185:render-snapshot', 'renderPilotOpsSnapshot'), ('pas185:render-learning', 'renderOperatorLearningDashboard'), ('pas185a:dashboard-mount', 'aPilotOpsContent'), ('pas185a:intel-mount', 'aIntelLearning'), ('pas185:skip-link', 'skip-link'), ('pas185:main-anchor', 'id="main"'), ('pas185:reduced-motion', 'prefers-reduced-motion'), ('pas185:overscroll', 'overscroll-behavior'), ('pas185:dvh', '100dvh')))
               STORE_NAME              38 (DASHBOARD_REQUIRED_ANCHORS)

 302           LOAD_CONST              94 (('gmail oauth', 'google.oauth2', 'composio', 'trustclaw', 'ai chat assistant', 'chatgpt assistant', 'tailwindcss', 'shadcn', 'from "react"', "from 'react'", 'import react', 'uipro-cli', 'v0.dev'))
               STORE_NAME              39 (DASHBOARD_FORBIDDEN_TOKENS)

 320           LOAD_CONST              95 (('from app.services.ingestion.worker', 'import app.services.ingestion.worker', 'run_worker_loop', 'process_pending_call(', 'asyncio.create_task(learning_autopilot', 'asyncio.create_task(adaptive_memory_autowrite', 'BackgroundTasks().add_task(learning_autopilot', 'BackgroundTasks().add_task(adaptive_memory_autowrite'))
               STORE_NAME              40 (MAIN_PY_FORBIDDEN_EXECUTABLE_TOKENS)

 334           LOAD_CONST              96 (('operator_learning_dashboard_router',))
               STORE_NAME              41 (MAIN_PY_REQUIRED_ROUTER_MOUNTS)

 341           LOAD_CONST              15 ('allow_origins=["*"]')
               STORE_NAME              42 (CORS_FORBIDDEN_PATTERN)

 342           LOAD_CONST              97 (('allow_origins=["*"]', "allow_origins=['*']", 'allow_origins = ["*"]', "allow_origins = ['*']"))
               STORE_NAME              43 (CORS_FORBIDDEN_ALT_PATTERNS)

 351           LOAD_CONST              16 ('app/services/operator/audit_service.py')
               STORE_NAME              44 (AUDIT_SERVICE_FILE)

 352           LOAD_CONST              98 (('def update_audit_', 'def delete_audit_', 'def update_operator_audit_', 'def delete_operator_audit_', 'def mutate_audit_', 'def truncate_audit_'))
               STORE_NAME              45 (AUDIT_SERVICE_FORBIDDEN)

 364           LOAD_CONST              17 ('app/routes/operator_learning_dashboard.py')
               STORE_NAME              46 (LEARNING_DASHBOARD_ROUTE)

 365           LOAD_CONST              99 (('@router.post', '@router.patch', '@router.delete', '@router.put'))
               STORE_NAME              47 (LEARNING_DASHBOARD_FORBIDDEN_DECORATORS)

 374           LOAD_CONST             100 (('app/routes/tenant_portal.py',))
               STORE_NAME              48 (TENANT_READONLY_FILES)

 377           LOAD_CONST             101 (('@router.post("/audit', '@router.patch("/audit', '@router.delete("/audit', '@router.put("/audit'))
               STORE_NAME              49 (TENANT_READONLY_FORBIDDEN_DECORATORS)

 390           LOAD_CONST              18 ('app/routes/security_api_key_rotation.py')
               STORE_NAME              50 (KEY_REVEAL_OFFICIAL_FILE)

 394           LOAD_CONST             102 (('"raw_api_key":', "'raw_api_key':", '"plaintext_key":', "'plaintext_key':", '"api_key_plain":', "'api_key_plain':"))
               STORE_NAME              51 (RAW_KEY_REVEAL_FORBIDDEN_PATTERNS)

 405           LOAD_CONST             103 (('app/services/memory/review.py', 'app/services/memory/review_stats.py', 'app/services/memory/review_export.py', 'app/services/memory/review_actors.py', 'app/services/memory/review_alerts.py', 'app/services/memory/operator_console.py'))
               STORE_NAME              52 (MEMORY_REVIEW_FILES)

 419           LOAD_CONST              19 ('severity')

 424           LOAD_NAME               29 (SEVERITY_BLOCK)

 419           LOAD_CONST              20 ('detail')

 425           LOAD_CONST              21 ('')

 419           BUILD_MAP                2
               LOAD_CONST              22 (<code object __annotate__ at 0x0000018C18025C30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 419>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object _check at 0x0000018C17FA34B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 419>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              53 (_check)

 436           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA31E0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 436>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object _now_iso at 0x0000018C18038170, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 436>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              54 (_now_iso)

 440           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA3A50, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 440>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object _read_text at 0x0000018C18053990, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 440>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              55 (_read_text)

 447           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA3E10, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 447>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object _strip_python_comments_and_strings at 0x0000018C182DA010, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 447>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              56 (_strip_python_comments_and_strings)

 491           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA3960, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 491>)
               MAKE_FUNCTION
               LOAD_CONST              31 (<code object check_pas186_files_present at 0x0000018C18060F60, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 491>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              57 (check_pas186_files_present)

 504           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA3C30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 504>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object check_prior_readiness_gates_callable at 0x0000018C17D87040, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 504>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              58 (check_prior_readiness_gates_callable)

 530           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA3690, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 530>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object check_required_migrations_present at 0x0000018C180606F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 530>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              59 (check_required_migrations_present)

 543           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C17FA30F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 543>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object check_no_forbidden_future_migrations at 0x0000018C17D8BD50, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 543>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              60 (check_no_forbidden_future_migrations)

 595           LOAD_CONST              38 (<code object __annotate__ at 0x0000018C17FA2010, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 595>)
               MAKE_FUNCTION
               LOAD_CONST              39 (<code object check_pas186_doc_clauses at 0x0000018C17D8AAB0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 595>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              61 (check_pas186_doc_clauses)

 613           LOAD_CONST              40 (<code object __annotate__ at 0x0000018C17FA3000, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 613>)
               MAKE_FUNCTION
               LOAD_CONST              41 (<code object check_pas186_docs_no_forbidden_scope at 0x0000018C18300780, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 613>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              62 (check_pas186_docs_no_forbidden_scope)

 631           LOAD_CONST              42 (<code object __annotate__ at 0x0000018C18114120, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 631>)
               MAKE_FUNCTION
               LOAD_CONST              43 (<code object check_dashboard_anchors_present at 0x0000018C1794EBB0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 631>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              63 (check_dashboard_anchors_present)

 645           LOAD_CONST              44 (<code object __annotate__ at 0x0000018C18114210, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 645>)
               MAKE_FUNCTION
               LOAD_CONST              45 (<code object check_dashboard_no_forbidden_tokens at 0x0000018C180FC990, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 645>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              64 (check_dashboard_no_forbidden_tokens)

 659           LOAD_CONST              46 (<code object __annotate__ at 0x0000018C18114300, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 659>)
               MAKE_FUNCTION
               LOAD_CONST              47 (<code object check_pas185_mounts_present at 0x0000018C18048730, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 659>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              65 (check_pas185_mounts_present)

 689           LOAD_CONST              48 (<code object __annotate__ at 0x0000018C181143F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 689>)
               MAKE_FUNCTION
               LOAD_CONST              49 (<code object check_main_no_autostart_worker at 0x0000018C17EC5380, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 689>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              66 (check_main_no_autostart_worker)

 705           LOAD_CONST              50 (<code object __annotate__ at 0x0000018C181144E0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 705>)
               MAKE_FUNCTION
               LOAD_CONST              51 (<code object check_main_mounts_required_routers at 0x0000018C1794E810, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 705>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              67 (check_main_mounts_required_routers)

 720           LOAD_CONST              52 (<code object __annotate__ at 0x0000018C181145D0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 720>)
               MAKE_FUNCTION
               LOAD_CONST              53 (<code object check_no_wildcard_cors at 0x0000018C17D79E90, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 720>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              68 (check_no_wildcard_cors)

 748           LOAD_CONST              54 (<code object __annotate__ at 0x0000018C181146C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 748>)
               MAKE_FUNCTION
               LOAD_CONST              55 (<code object check_audit_service_append_only at 0x0000018C182DD0A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 748>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              69 (check_audit_service_append_only)

 763           LOAD_CONST              56 (<code object __annotate__ at 0x0000018C181147B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 763>)
               MAKE_FUNCTION
               LOAD_CONST              57 (<code object check_learning_dashboard_no_mutation at 0x0000018C17ED8D80, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 763>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              70 (check_learning_dashboard_no_mutation)

 779           LOAD_CONST              58 (<code object __annotate__ at 0x0000018C181148A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 779>)
               MAKE_FUNCTION
               LOAD_CONST              59 (<code object check_no_live_learning_mutation at 0x0000018C17F73CD0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 779>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              71 (check_no_live_learning_mutation)

 815           LOAD_CONST              60 (<code object __annotate__ at 0x0000018C18114990, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 815>)
               MAKE_FUNCTION
               LOAD_CONST              61 (<code object check_no_live_adaptive_memory_mutation at 0x0000018C17F73310, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 815>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              72 (check_no_live_adaptive_memory_mutation)

 848           LOAD_CONST              62 (<code object __annotate__ at 0x0000018C18114A80, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 848>)
               MAKE_FUNCTION
               LOAD_CONST              63 (<code object check_tenant_routes_read_only at 0x0000018C17ECF6F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 848>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              73 (check_tenant_routes_read_only)

 865           LOAD_CONST              64 (<code object __annotate__ at 0x0000018C18114B70, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 865>)
               MAKE_FUNCTION
               LOAD_CONST              65 (<code object check_no_raw_key_reveal at 0x0000018C18325410, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 865>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              74 (check_no_raw_key_reveal)

 907           LOAD_CONST              66 (<code object __annotate__ at 0x0000018C18114C60, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 907>)
               MAKE_FUNCTION
               LOAD_CONST              67 (<code object check_memory_review_intact at 0x0000018C18061110, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 907>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              75 (check_memory_review_intact)

 920           LOAD_CONST              68 (<code object __annotate__ at 0x0000018C18114D50, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 920>)
               MAKE_FUNCTION
               LOAD_CONST              69 (<code object check_self_no_env_or_db at 0x0000018C17E92B90, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 920>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              76 (check_self_no_env_or_db)

 954           LOAD_CONST              70 (<code object __annotate__ at 0x0000018C18114E40, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 954>)
               MAKE_FUNCTION
               LOAD_CONST              71 (<code object check_self_no_deploy_execution at 0x0000018C17EC46C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 954>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              77 (check_self_no_deploy_execution)

 995           LOAD_CONST              72 (<code object __annotate__ at 0x0000018C18114F30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 995>)
               MAKE_FUNCTION
               LOAD_CONST              73 (<code object _aggregate at 0x0000018C1800B0A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 995>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              78 (_aggregate)

1007           LOAD_CONST              74 (<code object __annotate__ at 0x0000018C18115020, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 1007>)
               MAKE_FUNCTION
               LOAD_CONST              75 (<code object _operator_actions at 0x0000018C180488F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 1007>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              79 (_operator_actions)

1017           LOAD_CONST              76 (<code object __annotate__ at 0x0000018C18114030, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 1017>)
               MAKE_FUNCTION
               LOAD_CONST              77 (<code object evaluate at 0x0000018C177C5D50, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 1017>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              80 (evaluate)

1057           LOAD_CONST              78 ('pas186_final_cutover_readiness_report.json')
               STORE_NAME              81 (REPORT_FILENAME)

1060           LOAD_CONST              79 (<code object __annotate__ at 0x0000018C181156B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 1060>)
               MAKE_FUNCTION
               LOAD_CONST              80 (<code object _build_parser at 0x0000018C180FC3F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 1060>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              82 (_build_parser)

1078           LOAD_CONST              81 (<code object __annotate__ at 0x0000018C18115110, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 1078>)
               MAKE_FUNCTION
               LOAD_CONST              82 (<code object _print_summary at 0x0000018C17D8C5C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 1078>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              83 (_print_summary)

1096           LOAD_CONST              83 (<code object __annotate__ at 0x0000018C18025030, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 1096>)
               MAKE_FUNCTION
               LOAD_CONST              84 (<code object _write_report at 0x0000018C180FCF30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 1096>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              84 (_write_report)

1110           LOAD_CONST             104 ((None,))
               LOAD_CONST              85 (<code object __annotate__ at 0x0000018C18115200, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 1110>)
               MAKE_FUNCTION
               LOAD_CONST              86 (<code object main at 0x0000018C17D89750, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 1110>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              85 (main)

1135           LOAD_NAME               86 (__name__)
               LOAD_CONST              87 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

1136           LOAD_NAME                7 (sys)
               LOAD_ATTR              174 (exit)
               PUSH_NULL
               LOAD_NAME               85 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

1135   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  37           LOAD_NAME               20 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  38   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          406 (to L1)

  37   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025C30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 419>:
419           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('check_id')

420           LOAD_CONST               2 ('str')

419           LOAD_CONST               3 ('status')

421           LOAD_CONST               2 ('str')

419           LOAD_CONST               4 ('label')

422           LOAD_CONST               2 ('str')

419           LOAD_CONST               5 ('severity')

424           LOAD_CONST               2 ('str')

419           LOAD_CONST               6 ('detail')

425           LOAD_CONST               2 ('str')

419           LOAD_CONST               7 ('return')

426           LOAD_CONST               8 ('dict')

419           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _check at 0x0000018C17FA34B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 419>:
419           RESUME                   0

428           LOAD_CONST               0 ('id')
              LOAD_FAST_BORROW         0 (check_id)

429           LOAD_CONST               1 ('status')
              LOAD_FAST_BORROW         1 (status)

430           LOAD_CONST               2 ('label')
              LOAD_FAST_BORROW         2 (label)

431           LOAD_CONST               3 ('severity')
              LOAD_FAST_BORROW         3 (severity)

432           LOAD_CONST               4 ('detail')
              LOAD_FAST_BORROW         4 (detail)

427           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 436>:
436           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038170, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 436>:
436           RESUME                   0

437           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 440>:
440           RESUME                   0
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

Disassembly of <code object _read_text at 0x0000018C18053990, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 440>:
 440           RESUME                   0

 441           NOP

 442   L1:     LOAD_FAST_BORROW         0 (path)
               LOAD_ATTR                1 (read_text + NULL|self)
               LOAD_CONST               0 ('utf-8')
               LOAD_CONST               1 ('replace')
               LOAD_CONST               2 (('encoding', 'errors'))
               CALL_KW                  2
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 443           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 444   L4:     POP_EXCEPT
               LOAD_CONST               3 (None)
               RETURN_VALUE

 443   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 447>:
447           RESUME                   0
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

Disassembly of <code object _strip_python_comments_and_strings at 0x0000018C182DA010, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 447>:
447            RESUME                   0

453            BUILD_LIST               0
               STORE_FAST               1 (out)

454            LOAD_SMALL_INT           0
               LOAD_GLOBAL              1 (len + NULL)
               LOAD_FAST_BORROW         0 (src)
               CALL                     1
               STORE_FAST_STORE_FAST   50 (n, i)

455    L1:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (i, n)
               COMPARE_OP              18 (bool(<))
               EXTENDED_ARG             1
               POP_JUMP_IF_FALSE      282 (to L13)
               NOT_TAKEN

456            LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               BINARY_OP               26 ([])
               STORE_FAST               4 (ch)

457            LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               1 ('#')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       38 (to L3)
               NOT_TAKEN

458            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_CONST               2 ('\n')
               LOAD_FAST_BORROW         2 (i)
               CALL                     2
               STORE_FAST               5 (j)

459            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L2)
               NOT_TAKEN

460            JUMP_FORWARD           240 (to L13)

461    L2:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

462            JUMP_BACKWARD           59 (to L1)

463    L3:     LOAD_FAST_BORROW         0 (src)
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

464    L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               BINARY_SLICE
               STORE_FAST               6 (quote)

465            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 98 (quote, i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               CALL                     2
               STORE_FAST               7 (end)

466            LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L5)
               NOT_TAKEN

467            JUMP_FORWARD           138 (to L13)

468    L5:     LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

469            JUMP_BACKWARD          161 (to L1)

470    L6:     LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               7 (('"', "'"))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       92 (to L12)
               NOT_TAKEN

471            LOAD_FAST                4 (ch)
               STORE_FAST               6 (quote)

472            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               5 (j)

473    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (j, n)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       63 (to L11)
               NOT_TAKEN

474            LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
               BINARY_OP               26 ([])
               LOAD_CONST               5 ('\\')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       12 (to L8)
               NOT_TAKEN

475            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           2
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)

476            JUMP_BACKWARD           30 (to L7)

477    L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
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

478    L9:     JUMP_FORWARD            11 (to L11)

479   L10:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)
               JUMP_BACKWARD           68 (to L7)

480   L11:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

481            EXTENDED_ARG             1
               JUMP_BACKWARD          259 (to L1)

482   L12:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (ch)
               CALL                     1
               POP_TOP

483            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               2 (i)
               EXTENDED_ARG             1
               JUMP_BACKWARD          288 (to L1)

484   L13:     LOAD_CONST               6 ('')
               LOAD_ATTR                9 (join + NULL|self)
               LOAD_FAST_BORROW         1 (out)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 491>:
491           RESUME                   0
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

Disassembly of <code object check_pas186_files_present at 0x0000018C18060F60, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 491>:
491           RESUME                   0

492           BUILD_LIST               0
              STORE_FAST               1 (out)

493           LOAD_GLOBAL              0 (PAS186_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

494           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

495           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

496           LOAD_CONST               0 ('file:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

497           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

498   L3:     LOAD_CONST               3 ('Required PAS186 file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

499           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing')

495   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

493   L6:     END_FOR
              POP_ITER

501           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 504>:
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

Disassembly of <code object check_prior_readiness_gates_callable at 0x0000018C17D87040, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 504>:
504            RESUME                   0

505            BUILD_LIST               0
               STORE_FAST               1 (out)

506            LOAD_GLOBAL              0 (PRIOR_READINESS_GATES)
               GET_ITER
       L1:     FOR_ITER                93 (to L6)
               STORE_FAST               2 (p)

507            LOAD_GLOBAL              3 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         2 (p)
               BINARY_OP               11 (/)
               STORE_FAST               3 (fp)

508            LOAD_FAST_BORROW         3 (fp)
               LOAD_ATTR                5 (is_file + NULL|self)
               CALL                     0
               STORE_FAST               4 (ok)

509            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

510            LOAD_CONST               0 ('prior_gate:')
               LOAD_FAST_BORROW         2 (p)
               FORMAT_SIMPLE
               BUILD_STRING             2

511            LOAD_FAST_BORROW         4 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L2)
               NOT_TAKEN
               LOAD_CONST               1 ('PASS')
               JUMP_FORWARD             1 (to L3)
       L2:     LOAD_CONST               2 ('FAIL')

512    L3:     LOAD_CONST               3 ('Prior readiness gate present: ')
               LOAD_FAST_BORROW         2 (p)
               FORMAT_SIMPLE
               BUILD_STRING             2

513            LOAD_FAST_BORROW         4 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L5)
       L4:     LOAD_CONST               5 ('missing — cutover § 1 step 3 would fail')

509    L5:     LOAD_CONST               6 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           95 (to L1)

506    L6:     END_FOR
               POP_ITER

517            LOAD_GLOBAL              0 (PRIOR_READINESS_GATES)
               GET_ITER
       L7:     FOR_ITER               116 (to L14)
               STORE_FAST               2 (p)

518            LOAD_GLOBAL              3 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         2 (p)
               BINARY_OP               11 (/)
               STORE_FAST               3 (fp)

519            LOAD_GLOBAL             11 (_read_text + NULL)
               LOAD_FAST_BORROW         3 (fp)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')
       L8:     STORE_FAST               5 (src)

520            LOAD_CONST               7 ('def main(')
               LOAD_FAST_BORROW         5 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L9)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               8 ('if __name__')
               LOAD_FAST_BORROW         5 (src)
               CONTAINS_OP              0 (in)
       L9:     STORE_FAST               6 (has_main)

521            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

522            LOAD_CONST               9 ('prior_gate_entrypoint:')
               LOAD_FAST_BORROW         2 (p)
               FORMAT_SIMPLE
               BUILD_STRING             2

523            LOAD_FAST_BORROW         6 (has_main)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST               1 ('PASS')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST               2 ('FAIL')

524   L11:     LOAD_CONST              10 ('Prior readiness gate has main entrypoint: ')
               LOAD_FAST_BORROW         2 (p)
               FORMAT_SIMPLE
               BUILD_STRING             2

525            LOAD_FAST_BORROW         6 (has_main)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L12)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L13)
      L12:     LOAD_CONST              11 ('no main() / __main__ guard')

521   L13:     LOAD_CONST               6 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          118 (to L7)

517   L14:     END_FOR
               POP_ITER

527            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 530>:
530           RESUME                   0
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

Disassembly of <code object check_required_migrations_present at 0x0000018C180606F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 530>:
530           RESUME                   0

531           BUILD_LIST               0
              STORE_FAST               1 (out)

532           LOAD_GLOBAL              0 (REQUIRED_MIGRATIONS)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

533           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

534           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

535           LOAD_CONST               0 ('migration:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

536           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

537   L3:     LOAD_CONST               3 ('Required migration on disk: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

538           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing — cutover § 2 cannot promote')

534   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

532   L6:     END_FOR
              POP_ITER

540           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA30F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 543>:
543           RESUME                   0
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

Disassembly of <code object check_no_forbidden_future_migrations at 0x0000018C17D8BD50, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 543>:
 543            RESUME                   0

 544            BUILD_LIST               0
                STORE_FAST               1 (out)

 545            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('scripts')
                BINARY_OP               11 (/)
                STORE_FAST               2 (scripts_dir)

 546            LOAD_FAST_BORROW         2 (scripts_dir)
                LOAD_ATTR                3 (is_dir + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L1)
                NOT_TAKEN

 547            LOAD_FAST_BORROW         1 (out)
                LOAD_ATTR                5 (append + NULL|self)
                LOAD_GLOBAL              7 (_check + NULL)

 548            LOAD_CONST               1 ('future_migrations:scripts_dir_present')

 549            LOAD_CONST               2 ('FAIL')

 550            LOAD_CONST               3 ('scripts/ directory missing')

 551            LOAD_CONST               4 ('repo layout broken')

 547            LOAD_CONST               5 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 553            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

 554    L1:     LOAD_FAST_BORROW         1 (out)
                LOAD_ATTR                5 (append + NULL|self)
                LOAD_GLOBAL              7 (_check + NULL)

 555            LOAD_CONST               1 ('future_migrations:scripts_dir_present')

 556            LOAD_CONST               6 ('PASS')

 557            LOAD_CONST               7 ('scripts/ directory present')

 554            CALL                     3
                CALL                     1
                POP_TOP

 559            BUILD_LIST               0
                STORE_FAST               3 (bad)

 560            LOAD_FAST_BORROW         2 (scripts_dir)
                LOAD_ATTR                9 (iterdir + NULL|self)
                CALL                     0
                GET_ITER
        L2:     FOR_ITER               169 (to L8)
                STORE_FAST               4 (entry)

 561            LOAD_FAST_BORROW         4 (entry)
                LOAD_ATTR               10 (name)
                STORE_FAST               5 (name)

 562            LOAD_FAST_BORROW         5 (name)
                LOAD_ATTR               13 (startswith + NULL|self)
                LOAD_CONST               8 ('migrate_v')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L3)
                NOT_TAKEN

 563            JUMP_BACKWARD           40 (to L2)

 564    L3:     LOAD_FAST_BORROW         5 (name)
                LOAD_ATTR               15 (endswith + NULL|self)
                LOAD_CONST               9 ('.sql')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN

 565            JUMP_BACKWARD           65 (to L2)

 566    L4:     NOP

 567    L5:     LOAD_FAST_BORROW         5 (name)
                LOAD_GLOBAL             17 (len + NULL)
                LOAD_CONST               8 ('migrate_v')
                CALL                     1
                LOAD_CONST              10 (None)
                BINARY_SLICE
                STORE_FAST               6 (tail)

 568            LOAD_FAST_BORROW         6 (tail)
                LOAD_ATTR               19 (split + NULL|self)
                LOAD_CONST              11 ('_')
                LOAD_SMALL_INT           1
                CALL                     2
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                LOAD_ATTR               19 (split + NULL|self)
                LOAD_CONST              12 ('.')
                LOAD_SMALL_INT           1
                CALL                     2
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                STORE_FAST               7 (num_str)

 569            LOAD_GLOBAL             21 (int + NULL)
                LOAD_FAST_BORROW         7 (num_str)
                CALL                     1
                STORE_FAST               8 (n)

 572    L6:     LOAD_FAST                8 (n)
                LOAD_GLOBAL             24 (MAX_RATIFIED_MIGRATION_V)
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                JUMP_BACKWARD          152 (to L2)

 573    L7:     LOAD_FAST                3 (bad)
                LOAD_ATTR                5 (append + NULL|self)
                LOAD_FAST                5 (name)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          171 (to L2)

 560    L8:     END_FOR
                POP_ITER

 574            LOAD_FAST                1 (out)
                LOAD_ATTR                5 (append + NULL|self)
                LOAD_GLOBAL              7 (_check + NULL)

 575            LOAD_CONST              13 ('future_migrations:no_unratified')

 576            LOAD_FAST_BORROW         3 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L9)
                NOT_TAKEN
                LOAD_CONST               2 ('FAIL')
                JUMP_FORWARD             1 (to L10)
        L9:     LOAD_CONST               6 ('PASS')

 578   L10:     LOAD_CONST              14 ('No migration > v')
                LOAD_GLOBAL             24 (MAX_RATIFIED_MIGRATION_V)
                FORMAT_SIMPLE
                LOAD_CONST              15 (' on disk (unratified future migrations would violate cutover § 2)')
                BUILD_STRING             3

 582            LOAD_FAST_BORROW         3 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE       34 (to L11)
                NOT_TAKEN
                LOAD_CONST              16 ('unratified: ')
                LOAD_CONST              17 (', ')
                LOAD_ATTR               27 (join + NULL|self)
                LOAD_GLOBAL             29 (sorted + NULL)
                LOAD_FAST_BORROW         3 (bad)
                CALL                     1
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L12)
       L11:     LOAD_CONST              18 ('')

 574   L12:     LOAD_CONST               5 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 585            LOAD_FAST_BORROW         2 (scripts_dir)
                LOAD_CONST              19 ('combined_supabase_migration.sql')
                BINARY_OP               11 (/)
                STORE_FAST               9 (off_limits)

 586            LOAD_FAST                1 (out)
                LOAD_ATTR                5 (append + NULL|self)
                LOAD_GLOBAL              7 (_check + NULL)

 587            LOAD_CONST              20 ('future_migrations:combined_offlimits_left_alone')

 588            LOAD_CONST               6 ('PASS')

 589            LOAD_CONST              21 ('combined_supabase_migration.sql is left alone (off-limits per project memory)')

 590            LOAD_FAST_BORROW         9 (off_limits)
                LOAD_ATTR               31 (is_file + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L13)
                NOT_TAKEN
                LOAD_CONST              22 ('present and untouched')
                JUMP_FORWARD             1 (to L14)
       L13:     LOAD_CONST              23 ('not on disk')

 586   L14:     LOAD_CONST               5 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 592            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L15:     PUSH_EXC_INFO

 570            LOAD_GLOBAL             22 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L17)
                NOT_TAKEN
                POP_TOP

 571   L16:     POP_EXCEPT
                EXTENDED_ARG             1
                JUMP_BACKWARD          342 (to L2)

 570   L17:     RERAISE                  0

  --   L18:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L5 to L6 -> L15 [1]
  L15 to L16 -> L18 [2] lasti
  L17 to L18 -> L18 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2010, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 595>:
595           RESUME                   0
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

Disassembly of <code object check_pas186_doc_clauses at 0x0000018C17D8AAB0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 595>:
  --            MAKE_CELL                9 (lower)

 595            RESUME                   0

 596            BUILD_LIST               0
                STORE_FAST               1 (out)

 597            LOAD_GLOBAL              0 (DOC_REQUIRED_CLAUSES)
                GET_ITER
        L1:     FOR_ITER               208 (to L14)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   35 (relpath, clauses)

 598            LOAD_GLOBAL              3 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_FAST_BORROW         2 (relpath)
                BINARY_OP               11 (/)
                STORE_FAST               4 (fp)

 599            LOAD_GLOBAL              5 (_read_text + NULL)
                LOAD_FAST_BORROW         4 (fp)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L2)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               0 ('')
        L2:     STORE_FAST               5 (src)

 600            LOAD_FAST_BORROW         5 (src)
                LOAD_ATTR                7 (lower + NULL|self)
                CALL                     0
                STORE_DEREF              9 (lower)

 601            LOAD_FAST_BORROW         3 (clauses)
                GET_ITER
        L3:     FOR_ITER               142 (to L13)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST  103 (name, phrases)

 602            LOAD_GLOBAL              8 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L7)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         9 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               1 (<code object <genexpr> at 0x0000018C18025D30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 602>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         7 (phrases)
                GET_ITER
                CALL                     0
        L4:     FOR_ITER                12 (to L6)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L4)
        L5:     POP_ITER
                LOAD_CONST               2 (True)
                JUMP_FORWARD            20 (to L8)
        L6:     END_FOR
                POP_ITER
                LOAD_CONST               3 (False)
                JUMP_FORWARD            16 (to L8)
        L7:     PUSH_NULL
                LOAD_FAST_BORROW         9 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               1 (<code object <genexpr> at 0x0000018C18025D30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 602>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         7 (phrases)
                GET_ITER
                CALL                     0
                CALL                     1
        L8:     STORE_FAST               8 (present)

 603            LOAD_FAST                1 (out)
                LOAD_ATTR               11 (append + NULL|self)
                LOAD_GLOBAL             13 (_check + NULL)

 604            LOAD_CONST               4 ('doc:')
                LOAD_FAST_BORROW         2 (relpath)
                FORMAT_SIMPLE
                LOAD_CONST               5 (':clause:')
                LOAD_FAST_BORROW         6 (name)
                FORMAT_SIMPLE
                BUILD_STRING             4

 605            LOAD_FAST_BORROW         8 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L9)
                NOT_TAKEN
                LOAD_CONST               6 ('PASS')
                JUMP_FORWARD             1 (to L10)
        L9:     LOAD_CONST               7 ('FAIL')

 606   L10:     LOAD_FAST_BORROW         2 (relpath)
                FORMAT_SIMPLE
                LOAD_CONST               8 (' carries clause: ')
                LOAD_FAST_BORROW         6 (name)
                FORMAT_SIMPLE
                BUILD_STRING             3

 607            LOAD_FAST_BORROW         8 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L11)
                NOT_TAKEN
                LOAD_CONST               0 ('')
                JUMP_FORWARD            19 (to L12)

 608   L11:     LOAD_CONST               9 ('missing any of: ')
                LOAD_CONST              10 (', ')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_FAST_BORROW         7 (phrases)
                CALL                     1
                FORMAT_SIMPLE
                BUILD_STRING             2

 603   L12:     LOAD_CONST              11 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          144 (to L3)

 601   L13:     END_FOR
                POP_ITER
                JUMP_BACKWARD          210 (to L1)

 597   L14:     END_FOR
                POP_ITER

 610            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18025D30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 602>:
  --           COPY_FREE_VARS           1

 602           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3000, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 613>:
613           RESUME                   0
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

Disassembly of <code object check_pas186_docs_no_forbidden_scope at 0x0000018C18300780, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 613>:
613            RESUME                   0

614            BUILD_LIST               0
               STORE_FAST               1 (out)

615            LOAD_GLOBAL              0 (DOC_REQUIRED_CLAUSES)
               GET_ITER
       L1:     FOR_ITER               176 (to L10)
               UNPACK_SEQUENCE          2
               STORE_FAST_STORE_FAST   35 (relpath, _)

616            LOAD_GLOBAL              3 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         2 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (fp)

617            LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (fp)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L2:     LOAD_ATTR                7 (lower + NULL|self)
               CALL                     0
               STORE_FAST               5 (src)

618            BUILD_LIST               0
               STORE_FAST               6 (bad)

619            LOAD_GLOBAL              8 (FORBIDDEN_DOC_TOKENS)
               GET_ITER
       L3:     FOR_ITER                28 (to L5)
               STORE_FAST               7 (tok)

620            LOAD_FAST_BORROW_LOAD_FAST_BORROW 117 (tok, src)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L3)

621    L4:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_FAST_BORROW         7 (tok)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L3)

619    L5:     END_FOR
               POP_ITER

622            LOAD_FAST                1 (out)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_GLOBAL             13 (_check + NULL)

623            LOAD_CONST               1 ('doc_scope:')
               LOAD_FAST_BORROW         2 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

624            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L6)
               NOT_TAKEN
               LOAD_CONST               2 ('FAIL')
               JUMP_FORWARD             1 (to L7)
       L6:     LOAD_CONST               3 ('PASS')

625    L7:     LOAD_FAST_BORROW         2 (relpath)
               FORMAT_SIMPLE
               LOAD_CONST               4 (' introduces no out-of-scope feature token')
               BUILD_STRING             2

626            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L8)
               NOT_TAKEN
               LOAD_CONST               5 ('disqualifying: ')
               LOAD_CONST               6 (', ')
               LOAD_ATTR               15 (join + NULL|self)
               LOAD_FAST_BORROW         6 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST               0 ('')

622    L9:     LOAD_CONST               7 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          178 (to L1)

615   L10:     END_FOR
               POP_ITER

628            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114120, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 631>:
631           RESUME                   0
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

Disassembly of <code object check_dashboard_anchors_present at 0x0000018C1794EBB0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 631>:
631           RESUME                   0

632           BUILD_LIST               0
              STORE_FAST               1 (out)

633           LOAD_GLOBAL              1 (_read_text + NULL)
              LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_GLOBAL              4 (DASHBOARD_FILE)
              BINARY_OP               11 (/)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               0 ('')
      L1:     STORE_FAST               2 (src)

634           LOAD_GLOBAL              6 (DASHBOARD_REQUIRED_ANCHORS)
              GET_ITER
      L2:     FOR_ITER                65 (to L7)
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST   52 (cid, needle)

635           LOAD_FAST_BORROW_LOAD_FAST_BORROW 66 (needle, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

636           LOAD_FAST                1 (out)
              LOAD_ATTR                9 (append + NULL|self)
              LOAD_GLOBAL             11 (_check + NULL)

637           LOAD_CONST               1 ('dashboard:')
              LOAD_FAST_BORROW         3 (cid)
              FORMAT_SIMPLE
              BUILD_STRING             2

638           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               2 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               3 ('FAIL')

639   L4:     LOAD_CONST               4 ('Dashboard anchor present: ')
              LOAD_FAST_BORROW         4 (needle)
              FORMAT_SIMPLE
              BUILD_STRING             2

640           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               0 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               5 ('anchor missing')

636   L6:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           67 (to L2)

634   L7:     END_FOR
              POP_ITER

642           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114210, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 645>:
645           RESUME                   0
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

Disassembly of <code object check_dashboard_no_forbidden_tokens at 0x0000018C180FC990, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 645>:
645           RESUME                   0

646           BUILD_LIST               0
              STORE_FAST               1 (out)

647           LOAD_GLOBAL              1 (_read_text + NULL)
              LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_GLOBAL              4 (DASHBOARD_FILE)
              BINARY_OP               11 (/)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               0 ('')
      L1:     LOAD_ATTR                7 (lower + NULL|self)
              CALL                     0
              STORE_FAST               2 (src)

648           LOAD_GLOBAL              8 (DASHBOARD_FORBIDDEN_TOKENS)
              GET_ITER
      L2:     FOR_ITER                63 (to L7)
              STORE_FAST               3 (tok)

649           LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (tok, src)
              CONTAINS_OP              1 (not in)
              STORE_FAST               4 (ok)

650           LOAD_FAST                1 (out)
              LOAD_ATTR               11 (append + NULL|self)
              LOAD_GLOBAL             13 (_check + NULL)

651           LOAD_CONST               1 ('dashboard_forbidden:')
              LOAD_FAST_BORROW         3 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

652           LOAD_FAST_BORROW         4 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               2 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               3 ('FAIL')

653   L4:     LOAD_CONST               4 ('Dashboard carries no forbidden token: ')
              LOAD_FAST_BORROW         3 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

654           LOAD_FAST_BORROW         4 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               0 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               5 ('token observed — out of scope')

650   L6:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           65 (to L2)

648   L7:     END_FOR
              POP_ITER

656           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114300, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 659>:
659           RESUME                   0
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

Disassembly of <code object check_pas185_mounts_present at 0x0000018C18048730, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 659>:
659           RESUME                   0

662           BUILD_LIST               0
              STORE_FAST               1 (out)

663           LOAD_GLOBAL              1 (_read_text + NULL)
              LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_GLOBAL              4 (DASHBOARD_FILE)
              BINARY_OP               11 (/)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 ('')
      L1:     STORE_FAST               2 (src)

664           LOAD_CONST               7 ((('pas185a:snapshot_mount_call', "loadPilotOpsSnapshot('aPilotOpsContent')"), ('pas185a:snapshot_mount_container', 'id="aPilotOpsContent"'), ('pas185a:learning_mount_call', "loadOperatorLearningDashboard('aIntelLearning')"), ('pas185a:learning_mount_container', 'id="aIntelLearning"'), ('pas185a:snapshot_section_label', 'Pilot Ops Snapshot'), ('pas185a:learning_section_label', 'Learning Surface')))
              STORE_FAST               3 (mounts)

678           LOAD_FAST_BORROW         3 (mounts)
              GET_ITER
      L2:     FOR_ITER                62 (to L7)
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST   69 (cid, needle)

679           LOAD_FAST_BORROW_LOAD_FAST_BORROW 82 (needle, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               6 (ok)

680           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

681           LOAD_FAST                4 (cid)

682           LOAD_FAST_BORROW         6 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               2 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               3 ('FAIL')

683   L4:     LOAD_CONST               4 ('PAS185-A mount artefact present: ')
              LOAD_FAST_BORROW         5 (needle)
              FORMAT_SIMPLE
              BUILD_STRING             2

684           LOAD_FAST_BORROW         6 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               1 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               5 ('missing — operator surface invisible')

680   L6:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           64 (to L2)

678   L7:     END_FOR
              POP_ITER

686           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181143F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 689>:
689           RESUME                   0
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

Disassembly of <code object check_main_no_autostart_worker at 0x0000018C17EC5380, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 689>:
689           RESUME                   0

690           BUILD_LIST               0
              STORE_FAST               1 (out)

691           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('main.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (fp)

692           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (fp)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               2 ('')
      L1:     STORE_FAST               3 (src)

693           LOAD_GLOBAL              5 (_strip_python_comments_and_strings + NULL)
              LOAD_FAST_BORROW         3 (src)
              CALL                     1
              STORE_FAST               4 (executable)

694           LOAD_GLOBAL              6 (MAIN_PY_FORBIDDEN_EXECUTABLE_TOKENS)
              GET_ITER
      L2:     FOR_ITER                85 (to L7)
              STORE_FAST               5 (tok)

695           LOAD_FAST_BORROW_LOAD_FAST_BORROW 84 (tok, executable)
              CONTAINS_OP              0 (in)
              STORE_FAST               6 (bad)

696           LOAD_FAST                1 (out)
              LOAD_ATTR                9 (append + NULL|self)
              LOAD_GLOBAL             11 (_check + NULL)

697           LOAD_CONST               3 ('main_no_autostart:')
              LOAD_FAST_BORROW         5 (tok)
              LOAD_ATTR               13 (strip + NULL|self)
              CALL                     0
              LOAD_CONST               4 (slice(None, 80, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

698           LOAD_FAST_BORROW         6 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               5 ('FAIL')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               6 ('PASS')

699   L4:     LOAD_CONST               7 ('app/main.py does not auto-start: ')
              LOAD_FAST_BORROW         5 (tok)
              CONVERT_VALUE            2 (repr)
              FORMAT_SIMPLE
              BUILD_STRING             2

700           LOAD_FAST_BORROW         6 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               8 ('forbidden token in executable code')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               2 ('')

696   L6:     LOAD_CONST               9 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           87 (to L2)

694   L7:     END_FOR
              POP_ITER

702           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181144E0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 705>:
705           RESUME                   0
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

Disassembly of <code object check_main_mounts_required_routers at 0x0000018C1794E810, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 705>:
705           RESUME                   0

706           BUILD_LIST               0
              STORE_FAST               1 (out)

707           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('main.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (fp)

708           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (fp)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               2 ('')
      L1:     STORE_FAST               3 (src)

709           LOAD_GLOBAL              4 (MAIN_PY_REQUIRED_ROUTER_MOUNTS)
              GET_ITER
      L2:     FOR_ITER                63 (to L7)
              STORE_FAST               4 (tok)

710           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

711           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

712           LOAD_CONST               3 ('main_router:')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

713           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               4 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               5 ('FAIL')

714   L4:     LOAD_CONST               6 ('app/main.py mounts router: ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

715           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               2 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               7 ('operator surface not mounted')

711   L6:     LOAD_CONST               8 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           65 (to L2)

709   L7:     END_FOR
              POP_ITER

717           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181145D0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 720>:
720           RESUME                   0
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

Disassembly of <code object check_no_wildcard_cors at 0x0000018C17D79E90, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 720>:
720            RESUME                   0

721            BUILD_LIST               0
               STORE_FAST               1 (out)

722            BUILD_LIST               0
               STORE_FAST               2 (bad_paths)

723            LOAD_CONST              16 (('app/main.py',))
               GET_ITER
       L1:     FOR_ITER               136 (to L6)
               STORE_FAST               3 (relpath)

724            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (fp)

725            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (fp)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L2:     STORE_FAST               5 (src)

726            LOAD_GLOBAL              5 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         5 (src)
               CALL                     1
               STORE_FAST               6 (executable)

727            LOAD_GLOBAL              6 (CORS_FORBIDDEN_PATTERN)
               BUILD_LIST               1
               LOAD_GLOBAL              8 (CORS_FORBIDDEN_ALT_PATTERNS)
               LIST_EXTEND              1
               GET_ITER
       L3:     FOR_ITER                66 (to L5)
               STORE_FAST               7 (pattern)

728            LOAD_FAST_BORROW         7 (pattern)
               LOAD_ATTR               11 (replace + NULL|self)
               LOAD_CONST               2 (' ')
               LOAD_CONST               1 ('')
               CALL                     2
               LOAD_FAST_BORROW         6 (executable)
               LOAD_ATTR               11 (replace + NULL|self)
               LOAD_CONST               2 (' ')
               LOAD_CONST               1 ('')
               CALL                     2
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           44 (to L3)

729    L4:     LOAD_FAST_BORROW         2 (bad_paths)
               LOAD_ATTR               13 (append + NULL|self)
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               LOAD_CONST               3 (':')
               LOAD_FAST_BORROW         7 (pattern)
               FORMAT_SIMPLE
               BUILD_STRING             3
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           68 (to L3)

727    L5:     END_FOR
               POP_ITER
               JUMP_BACKWARD          138 (to L1)

723    L6:     END_FOR
               POP_ITER

730            LOAD_FAST                1 (out)
               LOAD_ATTR               13 (append + NULL|self)
               LOAD_GLOBAL             15 (_check + NULL)

731            LOAD_CONST               4 ('cors:no_wildcard_in_main')

732            LOAD_FAST_BORROW         2 (bad_paths)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L7)
               NOT_TAKEN
               LOAD_CONST               5 ('FAIL')
               JUMP_FORWARD             1 (to L8)
       L7:     LOAD_CONST               6 ('PASS')

733    L8:     LOAD_CONST               7 ('app/main.py does not configure wildcard CORS origins')

734            LOAD_FAST_BORROW         2 (bad_paths)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L9)
               NOT_TAKEN
               LOAD_CONST               8 ('disqualifying: ')
               LOAD_CONST               9 ('; ')
               LOAD_ATTR               17 (join + NULL|self)
               LOAD_FAST_BORROW         2 (bad_paths)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L10)
       L9:     LOAD_CONST               1 ('')

730   L10:     LOAD_CONST              10 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

737            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST              11 ('docs/pas186_final_pilot_cutover.md')
               BINARY_OP               11 (/)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L11)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
      L11:     LOAD_ATTR               19 (lower + NULL|self)
               CALL                     0
               STORE_FAST               8 (cutover_src)

738            LOAD_CONST              12 ('wildcard cors')
               LOAD_FAST_BORROW         8 (cutover_src)
               CONTAINS_OP              0 (in)
               STORE_FAST               9 (ok)

739            LOAD_FAST                1 (out)
               LOAD_ATTR               13 (append + NULL|self)
               LOAD_GLOBAL             15 (_check + NULL)

740            LOAD_CONST              13 ('cors:doc_clause_present')

741            LOAD_FAST_BORROW         9 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L12)
               NOT_TAKEN
               LOAD_CONST               6 ('PASS')
               JUMP_FORWARD             1 (to L13)
      L12:     LOAD_CONST               5 ('FAIL')

742   L13:     LOAD_CONST              14 ('Cutover doctrine names wildcard-CORS ban')

743            LOAD_FAST_BORROW         9 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L14)
               NOT_TAKEN
               LOAD_CONST               1 ('')
               JUMP_FORWARD             1 (to L15)
      L14:     LOAD_CONST              15 ('missing wildcard cors clause')

739   L15:     LOAD_CONST              10 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

745            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181146C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 748>:
748           RESUME                   0
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

Disassembly of <code object check_audit_service_append_only at 0x0000018C182DD0A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 748>:
748           RESUME                   0

749           BUILD_LIST               0
              STORE_FAST               1 (out)

750           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_GLOBAL              2 (AUDIT_SERVICE_FILE)
              BINARY_OP               11 (/)
              STORE_FAST               2 (fp)

751           LOAD_GLOBAL              5 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (fp)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               0 ('')
      L1:     STORE_FAST               3 (src)

752           LOAD_GLOBAL              6 (AUDIT_SERVICE_FORBIDDEN)
              GET_ITER
      L2:     FOR_ITER               115 (to L7)
              STORE_FAST               4 (tok)

753           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (bad)

754           LOAD_FAST                1 (out)
              LOAD_ATTR                9 (append + NULL|self)
              LOAD_GLOBAL             11 (_check + NULL)

755           LOAD_CONST               1 ('audit_service:no_')
              LOAD_FAST_BORROW         4 (tok)
              LOAD_ATTR               13 (strip + NULL|self)
              CALL                     0
              LOAD_ATTR               15 (rstrip + NULL|self)
              LOAD_CONST               2 ('(')
              CALL                     1
              LOAD_ATTR               13 (strip + NULL|self)
              LOAD_CONST               3 ('_')
              CALL                     1
              LOAD_CONST               4 (slice(None, 50, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

756           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               5 ('FAIL')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               6 ('PASS')

757   L4:     LOAD_CONST               7 ('audit_service.py free of mutation helper: ')
              LOAD_FAST_BORROW         4 (tok)
              CONVERT_VALUE            2 (repr)
              FORMAT_SIMPLE
              BUILD_STRING             2

758           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               8 ('disqualifying token')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               0 ('')

754   L6:     LOAD_CONST               9 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD          117 (to L2)

752   L7:     END_FOR
              POP_ITER

760           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181147B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 763>:
763           RESUME                   0
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

Disassembly of <code object check_learning_dashboard_no_mutation at 0x0000018C17ED8D80, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 763>:
763           RESUME                   0

764           BUILD_LIST               0
              STORE_FAST               1 (out)

765           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_GLOBAL              2 (LEARNING_DASHBOARD_ROUTE)
              BINARY_OP               11 (/)
              STORE_FAST               2 (fp)

766           LOAD_GLOBAL              5 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (fp)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               0 ('')
      L1:     STORE_FAST               3 (src)

767           LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
              LOAD_FAST_BORROW         3 (src)
              CALL                     1
              STORE_FAST               4 (executable)

768           LOAD_GLOBAL              8 (LEARNING_DASHBOARD_FORBIDDEN_DECORATORS)
              GET_ITER
      L2:     FOR_ITER               100 (to L7)
              STORE_FAST               5 (tok)

769           LOAD_FAST_BORROW_LOAD_FAST_BORROW 84 (tok, executable)
              CONTAINS_OP              0 (in)
              STORE_FAST               6 (bad)

770           LOAD_FAST                1 (out)
              LOAD_ATTR               11 (append + NULL|self)
              LOAD_GLOBAL             13 (_check + NULL)

771           LOAD_CONST               1 ('learning_route:no_')
              LOAD_FAST_BORROW         5 (tok)
              LOAD_ATTR               15 (strip + NULL|self)
              LOAD_CONST               2 ('@')
              CALL                     1
              LOAD_ATTR               17 (replace + NULL|self)
              LOAD_CONST               3 ('.')
              LOAD_CONST               4 ('_')
              CALL                     2
              FORMAT_SIMPLE
              BUILD_STRING             2

772           LOAD_FAST_BORROW         6 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               5 ('FAIL')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               6 ('PASS')

773   L4:     LOAD_GLOBAL              2 (LEARNING_DASHBOARD_ROUTE)
              FORMAT_SIMPLE
              LOAD_CONST               7 (' declares no ')
              LOAD_FAST_BORROW         5 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             3

774           LOAD_FAST_BORROW         6 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               8 ('forbidden decorator in executable code')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               0 ('')

770   L6:     LOAD_CONST               9 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD          102 (to L2)

768   L7:     END_FOR
              POP_ITER

776           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181148A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 779>:
779           RESUME                   0
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

Disassembly of <code object check_no_live_learning_mutation at 0x0000018C17F73CD0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 779>:
779            RESUME                   0

782            BUILD_LIST               0
               STORE_FAST               1 (out)

783            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               1 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('routes')
               BINARY_OP               11 (/)
               STORE_FAST               2 (routes_dir)

784            LOAD_FAST_BORROW         2 (routes_dir)
               LOAD_ATTR                3 (is_dir + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_FALSE       27 (to L1)
               NOT_TAKEN
               LOAD_GLOBAL              5 (sorted + NULL)
               LOAD_FAST_BORROW         2 (routes_dir)
               LOAD_ATTR                7 (glob + NULL|self)
               LOAD_CONST               3 ('*.py')
               CALL                     1
               CALL                     1
               JUMP_FORWARD             1 (to L2)
       L1:     BUILD_LIST               0
       L2:     STORE_FAST               3 (files)

785            BUILD_LIST               0
               STORE_FAST               4 (bad)

786            LOAD_FAST_BORROW         3 (files)
               GET_ITER
       L3:     FOR_ITER               145 (to L12)
               STORE_FAST               5 (fp)

787            LOAD_GLOBAL              9 (_read_text + NULL)
               LOAD_FAST_BORROW         5 (fp)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')
       L4:     STORE_FAST               6 (src)

788            LOAD_GLOBAL             11 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         6 (src)
               CALL                     1
               STORE_FAST               7 (executable)

789            LOAD_CONST              13 (('@router.post', '@router.patch', '@router.delete', '@router.put'))
               GET_ITER
       L5:     FOR_ITER               104 (to L11)
               STORE_FAST               8 (verb)

790            LOAD_CONST              14 (('learning_recommendations', 'learning_manual_test', 'adaptive_memory_bridge'))
               GET_ITER
       L6:     FOR_ITER                95 (to L10)
               STORE_FAST               9 (kw)

796            LOAD_SMALL_INT           0
               STORE_FAST              10 (idx)

797    L7:     NOP

798            LOAD_FAST_BORROW         7 (executable)
               LOAD_ATTR               13 (find + NULL|self)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 138 (verb, idx)
               CALL                     2
               STORE_FAST              11 (i)

799            LOAD_FAST_BORROW        11 (i)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN

800            JUMP_BACKWARD           32 (to L6)

801    L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 123 (executable, i)
               LOAD_FAST_BORROW        11 (i)
               LOAD_SMALL_INT         160
               BINARY_OP                0 (+)
               BINARY_SLICE
               STORE_FAST              12 (window)

802            LOAD_FAST_BORROW_LOAD_FAST_BORROW 156 (kw, window)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       38 (to L9)
               NOT_TAKEN

803            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_FAST_BORROW         5 (fp)
               LOAD_ATTR               16 (name)
               FORMAT_SIMPLE
               LOAD_CONST               5 ('::')
               LOAD_FAST_BORROW         8 (verb)
               FORMAT_SIMPLE
               LOAD_CONST               5 ('::')
               LOAD_FAST_BORROW         9 (kw)
               FORMAT_SIMPLE
               BUILD_STRING             5
               CALL                     1
               POP_TOP

804            JUMP_BACKWARD           86 (to L6)

805    L9:     LOAD_FAST_BORROW        11 (i)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST              10 (idx)
               JUMP_BACKWARD           92 (to L7)

790   L10:     END_FOR
               POP_ITER
               JUMP_BACKWARD          106 (to L5)

789   L11:     END_FOR
               POP_ITER
               JUMP_BACKWARD          147 (to L3)

786   L12:     END_FOR
               POP_ITER

806            LOAD_FAST                1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             19 (_check + NULL)

807            LOAD_CONST               6 ('no_live_learning_mutation')

808            LOAD_FAST_BORROW         4 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L13)
               NOT_TAKEN
               LOAD_CONST               7 ('FAIL')
               JUMP_FORWARD             1 (to L14)
      L13:     LOAD_CONST               8 ('PASS')

809   L14:     LOAD_CONST               9 ('No admin route declares mutation against a learning_* resource')

810            LOAD_FAST_BORROW         4 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L15)
               NOT_TAKEN
               LOAD_CONST              10 ('disqualifying: ')
               LOAD_CONST              11 ('; ')
               LOAD_ATTR               21 (join + NULL|self)
               LOAD_FAST_BORROW         4 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L16)
      L15:     LOAD_CONST               4 ('')

806   L16:     LOAD_CONST              12 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

812            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114990, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 815>:
815           RESUME                   0
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

Disassembly of <code object check_no_live_adaptive_memory_mutation at 0x0000018C17F73310, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 815>:
815            RESUME                   0

818            BUILD_LIST               0
               STORE_FAST               1 (out)

819            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               1 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('routes')
               BINARY_OP               11 (/)
               STORE_FAST               2 (routes_dir)

820            LOAD_FAST_BORROW         2 (routes_dir)
               LOAD_ATTR                3 (is_dir + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_FALSE       27 (to L1)
               NOT_TAKEN
               LOAD_GLOBAL              5 (sorted + NULL)
               LOAD_FAST_BORROW         2 (routes_dir)
               LOAD_ATTR                7 (glob + NULL|self)
               LOAD_CONST               3 ('*.py')
               CALL                     1
               CALL                     1
               JUMP_FORWARD             1 (to L2)
       L1:     BUILD_LIST               0
       L2:     STORE_FAST               3 (files)

821            BUILD_LIST               0
               STORE_FAST               4 (bad)

822            LOAD_FAST_BORROW         3 (files)
               GET_ITER
       L3:     FOR_ITER               145 (to L12)
               STORE_FAST               5 (fp)

823            LOAD_GLOBAL              9 (_read_text + NULL)
               LOAD_FAST_BORROW         5 (fp)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')
       L4:     STORE_FAST               6 (src)

824            LOAD_GLOBAL             11 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         6 (src)
               CALL                     1
               STORE_FAST               7 (executable)

825            LOAD_CONST              13 (('@router.post', '@router.patch', '@router.delete', '@router.put'))
               GET_ITER
       L5:     FOR_ITER               104 (to L11)
               STORE_FAST               8 (verb)

826            LOAD_CONST              14 (('adaptive_memory', 'memory_bridge', 'memory_autowrite'))
               GET_ITER
       L6:     FOR_ITER                95 (to L10)
               STORE_FAST               9 (kw)

829            LOAD_SMALL_INT           0
               STORE_FAST              10 (idx)

830    L7:     NOP

831            LOAD_FAST_BORROW         7 (executable)
               LOAD_ATTR               13 (find + NULL|self)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 138 (verb, idx)
               CALL                     2
               STORE_FAST              11 (i)

832            LOAD_FAST_BORROW        11 (i)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN

833            JUMP_BACKWARD           32 (to L6)

834    L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 123 (executable, i)
               LOAD_FAST_BORROW        11 (i)
               LOAD_SMALL_INT         160
               BINARY_OP                0 (+)
               BINARY_SLICE
               STORE_FAST              12 (window)

835            LOAD_FAST_BORROW_LOAD_FAST_BORROW 156 (kw, window)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       38 (to L9)
               NOT_TAKEN

836            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_FAST_BORROW         5 (fp)
               LOAD_ATTR               16 (name)
               FORMAT_SIMPLE
               LOAD_CONST               5 ('::')
               LOAD_FAST_BORROW         8 (verb)
               FORMAT_SIMPLE
               LOAD_CONST               5 ('::')
               LOAD_FAST_BORROW         9 (kw)
               FORMAT_SIMPLE
               BUILD_STRING             5
               CALL                     1
               POP_TOP

837            JUMP_BACKWARD           86 (to L6)

838    L9:     LOAD_FAST_BORROW        11 (i)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST              10 (idx)
               JUMP_BACKWARD           92 (to L7)

826   L10:     END_FOR
               POP_ITER
               JUMP_BACKWARD          106 (to L5)

825   L11:     END_FOR
               POP_ITER
               JUMP_BACKWARD          147 (to L3)

822   L12:     END_FOR
               POP_ITER

839            LOAD_FAST                1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             19 (_check + NULL)

840            LOAD_CONST               6 ('no_live_adaptive_memory_mutation')

841            LOAD_FAST_BORROW         4 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L13)
               NOT_TAKEN
               LOAD_CONST               7 ('FAIL')
               JUMP_FORWARD             1 (to L14)
      L13:     LOAD_CONST               8 ('PASS')

842   L14:     LOAD_CONST               9 ('No admin route declares mutation against an adaptive-memory resource')

843            LOAD_FAST_BORROW         4 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L15)
               NOT_TAKEN
               LOAD_CONST              10 ('disqualifying: ')
               LOAD_CONST              11 ('; ')
               LOAD_ATTR               21 (join + NULL|self)
               LOAD_FAST_BORROW         4 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L16)
      L15:     LOAD_CONST               4 ('')

839   L16:     LOAD_CONST              12 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

845            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114A80, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 848>:
848           RESUME                   0
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

Disassembly of <code object check_tenant_routes_read_only at 0x0000018C17ECF6F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 848>:
848           RESUME                   0

849           BUILD_LIST               0
              STORE_FAST               1 (out)

850           LOAD_GLOBAL              0 (TENANT_READONLY_FILES)
              GET_ITER
      L1:     FOR_ITER               170 (to L9)
              STORE_FAST               2 (relpath)

851           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (relpath)
              BINARY_OP               11 (/)
              STORE_FAST               3 (fp)

852           LOAD_GLOBAL              5 (_read_text + NULL)
              LOAD_FAST_BORROW         3 (fp)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               0 ('')
      L2:     STORE_FAST               4 (src)

853           LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
              LOAD_FAST_BORROW         4 (src)
              CALL                     1
              STORE_FAST               5 (executable)

854           LOAD_GLOBAL              8 (TENANT_READONLY_FORBIDDEN_DECORATORS)
              GET_ITER
      L3:     FOR_ITER               107 (to L8)
              STORE_FAST               6 (tok)

855           LOAD_FAST_BORROW_LOAD_FAST_BORROW 101 (tok, executable)
              CONTAINS_OP              0 (in)
              STORE_FAST               7 (bad)

856           LOAD_FAST                1 (out)
              LOAD_ATTR               11 (append + NULL|self)
              LOAD_GLOBAL             13 (_check + NULL)

857           LOAD_CONST               1 ('tenant_readonly:')
              LOAD_FAST_BORROW         2 (relpath)
              FORMAT_SIMPLE
              LOAD_CONST               2 (':')
              LOAD_FAST_BORROW         6 (tok)
              LOAD_ATTR               15 (strip + NULL|self)
              LOAD_CONST               3 ('@')
              CALL                     1
              LOAD_ATTR               17 (replace + NULL|self)
              LOAD_CONST               4 ('.')
              LOAD_CONST               5 ('_')
              CALL                     2
              LOAD_CONST               6 (slice(None, 60, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             4

858           LOAD_FAST_BORROW         7 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               7 ('FAIL')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               8 ('PASS')

859   L5:     LOAD_FAST_BORROW         2 (relpath)
              FORMAT_SIMPLE
              LOAD_CONST               9 (' does not declare ')
              LOAD_FAST_BORROW         6 (tok)
              FORMAT_SIMPLE
              LOAD_CONST              10 (' against /audit')
              BUILD_STRING             4

860           LOAD_FAST_BORROW         7 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L6)
              NOT_TAKEN
              LOAD_CONST              11 ('forbidden decorator in executable code')
              JUMP_FORWARD             1 (to L7)
      L6:     LOAD_CONST               0 ('')

856   L7:     LOAD_CONST              12 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD          109 (to L3)

854   L8:     END_FOR
              POP_ITER
              JUMP_BACKWARD          172 (to L1)

850   L9:     END_FOR
              POP_ITER

862           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114B70, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 865>:
865           RESUME                   0
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

Disassembly of <code object check_no_raw_key_reveal at 0x0000018C18325410, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 865>:
 865            RESUME                   0

 868            BUILD_LIST               0
                STORE_FAST               1 (out)

 869            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               1 ('app')
                BINARY_OP               11 (/)
                STORE_FAST               2 (app_dir)

 870            LOAD_FAST_BORROW         2 (app_dir)
                LOAD_ATTR                3 (is_dir + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       57 (to L7)
                NOT_TAKEN
                LOAD_FAST_BORROW         2 (app_dir)
                LOAD_ATTR                5 (rglob + NULL|self)
                LOAD_CONST               2 ('*.py')
                CALL                     1
                GET_ITER
                LOAD_FAST_AND_CLEAR      3 (p)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2
        L2:     FOR_ITER                28 (to L5)
                STORE_FAST_LOAD_FAST    51 (p, p)
                LOAD_ATTR                7 (is_file + NULL|self)
                CALL                     0
                TO_BOOL
        L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           26 (to L2)
        L4:     LOAD_FAST_BORROW         3 (p)
                LIST_APPEND              2
                JUMP_BACKWARD           30 (to L2)
        L5:     END_FOR
                POP_ITER
        L6:     SWAP                     2
                STORE_FAST               3 (p)
                JUMP_FORWARD             1 (to L8)
        L7:     BUILD_LIST               0
        L8:     STORE_FAST               4 (files)

 871            BUILD_LIST               0
                STORE_FAST               5 (bad)

 872            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_GLOBAL              8 (KEY_REVEAL_OFFICIAL_FILE)
                BINARY_OP               11 (/)
                LOAD_ATTR               11 (resolve + NULL|self)
                CALL                     0
                STORE_FAST               6 (official)

 873            LOAD_FAST_BORROW         6 (official)
                BUILD_SET                1
                STORE_FAST               7 (allowlist)

 874            LOAD_CONST              15 (('app/services/security/api_key_reveal.py', 'app/services/security/api_key_rotation.py'))
                GET_ITER
        L9:     FOR_ITER                50 (to L10)
                STORE_FAST               8 (relpath)

 878            LOAD_FAST_BORROW         7 (allowlist)
                LOAD_ATTR               13 (add + NULL|self)
                LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_FAST_BORROW         8 (relpath)
                BINARY_OP               11 (/)
                LOAD_ATTR               11 (resolve + NULL|self)
                CALL                     0
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           52 (to L9)

 874   L10:     END_FOR
                POP_ITER

 879            LOAD_FAST_BORROW         4 (files)
                GET_ITER
       L11:     FOR_ITER               117 (to L19)
                STORE_FAST               9 (fp)

 880            NOP

 881   L12:     LOAD_FAST_BORROW         9 (fp)
                LOAD_ATTR               11 (resolve + NULL|self)
                CALL                     0
                STORE_FAST              10 (resolved)

 884   L13:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 167 (resolved, allowlist)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L14)
                NOT_TAKEN

 885            JUMP_BACKWARD           28 (to L11)

 886   L14:     LOAD_GLOBAL             17 (_read_text + NULL)
                LOAD_FAST_BORROW         9 (fp)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L15)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               3 ('')
       L15:     STORE_FAST              11 (src)

 887            LOAD_GLOBAL             18 (RAW_KEY_REVEAL_FORBIDDEN_PATTERNS)
                GET_ITER
       L16:     FOR_ITER                58 (to L18)
                STORE_FAST              12 (pat)

 888            LOAD_FAST_BORROW_LOAD_FAST_BORROW 203 (pat, src)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_TRUE         3 (to L17)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L16)

 889   L17:     LOAD_FAST_BORROW         5 (bad)
                LOAD_ATTR               21 (append + NULL|self)
                LOAD_FAST_BORROW         9 (fp)
                LOAD_ATTR               23 (relative_to + NULL|self)
                LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                CALL                     1
                FORMAT_SIMPLE
                LOAD_CONST               4 ('::')
                LOAD_FAST_BORROW        12 (pat)
                FORMAT_SIMPLE
                BUILD_STRING             3
                CALL                     1
                POP_TOP

 890            POP_TOP
                JUMP_BACKWARD          115 (to L11)

 887   L18:     END_FOR
                POP_ITER
                JUMP_BACKWARD          119 (to L11)

 879   L19:     END_FOR
                POP_ITER

 891            LOAD_FAST                1 (out)
                LOAD_ATTR               21 (append + NULL|self)
                LOAD_GLOBAL             25 (_check + NULL)

 892            LOAD_CONST               5 ('no_raw_key_reveal:outside_official_route')

 893            LOAD_FAST_BORROW         5 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L20)
                NOT_TAKEN
                LOAD_CONST               6 ('FAIL')
                JUMP_FORWARD             1 (to L21)
       L20:     LOAD_CONST               7 ('PASS')

 894   L21:     LOAD_CONST               8 ('No raw-key reveal outside the official rotation route')

 895            LOAD_FAST_BORROW         5 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L22)
                NOT_TAKEN
                LOAD_CONST               9 ('disqualifying: ')
                LOAD_CONST              10 ('; ')
                LOAD_ATTR               27 (join + NULL|self)
                LOAD_FAST_BORROW         5 (bad)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L23)
       L22:     LOAD_CONST               3 ('')

 891   L23:     LOAD_CONST              11 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 898            LOAD_FAST                1 (out)
                LOAD_ATTR               21 (append + NULL|self)
                LOAD_GLOBAL             25 (_check + NULL)

 899            LOAD_CONST              12 ('no_raw_key_reveal:official_route_present')

 900            LOAD_FAST_BORROW         6 (official)
                LOAD_ATTR                7 (is_file + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L24)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L25)
       L24:     LOAD_CONST               6 ('FAIL')

 901   L25:     LOAD_CONST              13 ('Official key-rotation route present: ')
                LOAD_GLOBAL              8 (KEY_REVEAL_OFFICIAL_FILE)
                FORMAT_SIMPLE
                BUILD_STRING             2

 902            LOAD_FAST_BORROW         6 (official)
                LOAD_ATTR                7 (is_file + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L26)
                NOT_TAKEN
                LOAD_CONST               3 ('')
                JUMP_FORWARD             1 (to L27)
       L26:     LOAD_CONST              14 ('missing')

 898   L27:     LOAD_CONST              11 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 904            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L28:     SWAP                     2
                POP_TOP

 870            SWAP                     2
                STORE_FAST               3 (p)
                RERAISE                  0

  --   L29:     PUSH_EXC_INFO

 882            LOAD_GLOBAL             14 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        7 (to L31)
                NOT_TAKEN
                POP_TOP

 883            LOAD_FAST                9 (fp)
                STORE_FAST              10 (resolved)
       L30:     POP_EXCEPT
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 281 (to L13)

 882   L31:     RERAISE                  0

  --   L32:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L3 -> L28 [2]
  L4 to L6 -> L28 [2]
  L12 to L13 -> L29 [1]
  L29 to L30 -> L32 [2] lasti
  L31 to L32 -> L32 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18114C60, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 907>:
907           RESUME                   0
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

Disassembly of <code object check_memory_review_intact at 0x0000018C18061110, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 907>:
907           RESUME                   0

908           BUILD_LIST               0
              STORE_FAST               1 (out)

909           LOAD_GLOBAL              0 (MEMORY_REVIEW_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

910           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

911           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

912           LOAD_CONST               0 ('memory_review:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

913           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

914   L3:     LOAD_CONST               3 ('Memory Review file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

915           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('PAS147-158 surface broken')

911   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

909   L6:     END_FOR
              POP_ITER

917           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114D50, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 920>:
920           RESUME                   0
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

Disassembly of <code object check_self_no_env_or_db at 0x0000018C17E92B90, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 920>:
920            RESUME                   0

926            BUILD_LIST               0
               STORE_FAST               1 (out)

927            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_GLOBAL              2 (__file__)
               CALL                     1
               STORE_FAST               2 (fp)

928            LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (fp)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L1:     STORE_FAST               3 (src)

929            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               4 (executable)

930            BUILD_LIST               0
               STORE_FAST               5 (bad)

931            LOAD_FAST_BORROW         4 (executable)
               LOAD_ATTR                9 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L2:     FOR_ITER               199 (to L9)
               STORE_FAST               6 (line)

932            LOAD_FAST_BORROW         6 (line)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0
               STORE_FAST               7 (stripped)

933            LOAD_FAST_BORROW         7 (stripped)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN

934            JUMP_BACKWARD           29 (to L2)

935    L3:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              15 (('import dotenv', 'from dotenv'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L4)
               NOT_TAKEN

936            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               1 ('dotenv import')
               CALL                     1
               POP_TOP

937    L4:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              16 (('import supabase', 'from supabase'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L5)
               NOT_TAKEN

938            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               2 ('supabase import')
               CALL                     1
               POP_TOP

939    L5:     LOAD_CONST               3 ('load_dotenv(')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       18 (to L6)
               NOT_TAKEN

940            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               4 ('load_dotenv() call')
               CALL                     1
               POP_TOP

941    L6:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              17 (('os.environ[', 'getenv('))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L7)
               NOT_TAKEN

942            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               5 ('environ read')
               CALL                     1
               POP_TOP

943    L7:     LOAD_CONST               6 ('get_supabase')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD          182 (to L2)

944    L8:     LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               7 ('supabase client call')
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          201 (to L2)

931    L9:     END_FOR
               POP_ITER

945            LOAD_FAST                1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             17 (_check + NULL)

946            LOAD_CONST               8 ('self_check:no_env_or_db')

947            LOAD_FAST_BORROW         5 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST               9 ('FAIL')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST              10 ('PASS')

948   L11:     LOAD_CONST              11 ('PAS186 readiness checker never reads .env / touches DB')

949            LOAD_FAST_BORROW         5 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L12)
               NOT_TAKEN
               LOAD_CONST              12 ('disqualifying: ')
               LOAD_CONST              13 (', ')
               LOAD_ATTR               19 (join + NULL|self)
               LOAD_FAST_BORROW         5 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L13)
      L12:     LOAD_CONST               0 ('')

945   L13:     LOAD_CONST              14 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

951            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114E40, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 954>:
954           RESUME                   0
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

Disassembly of <code object check_self_no_deploy_execution at 0x0000018C17EC46C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 954>:
954           RESUME                   0

957           BUILD_LIST               0
              STORE_FAST               1 (out)

958           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_GLOBAL              2 (__file__)
              CALL                     1
              STORE_FAST               2 (fp)

959           LOAD_GLOBAL              5 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (fp)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 ('')
      L1:     STORE_FAST               3 (src)

960           BUILD_LIST               0
              STORE_FAST               4 (bad)

961           LOAD_CONST               9 (('subprocess.run(', 'subprocess.call(', 'subprocess.Popen(', 'os.system(', 'requests.get(', 'requests.post(', 'urllib.request.urlopen(', 'httpx.get(', 'httpx.post(', 'from twilio', 'from anthropic', 'from deepgram', 'from elevenlabs', 'git push', 'railway deploy'))
              STORE_FAST               5 (forbidden_tokens)

978           LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
              LOAD_FAST_BORROW         3 (src)
              CALL                     1
              STORE_FAST               6 (executable)

979           LOAD_FAST_BORROW         5 (forbidden_tokens)
              GET_ITER
      L2:     FOR_ITER                28 (to L4)
              STORE_FAST               7 (tok)

980           LOAD_FAST_BORROW_LOAD_FAST_BORROW 118 (tok, executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

981   L3:     LOAD_FAST_BORROW         4 (bad)
              LOAD_ATTR                9 (append + NULL|self)
              LOAD_FAST_BORROW         7 (tok)
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           30 (to L2)

979   L4:     END_FOR
              POP_ITER

982           LOAD_FAST                1 (out)
              LOAD_ATTR                9 (append + NULL|self)
              LOAD_GLOBAL             11 (_check + NULL)

983           LOAD_CONST               2 ('self_check:no_deploy_execution')

984           LOAD_FAST_BORROW         4 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               3 ('FAIL')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               4 ('PASS')

985   L6:     LOAD_CONST               5 ('PAS186 readiness checker never executes a deploy / migration / network call')

986           LOAD_FAST_BORROW         4 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE       25 (to L7)
              NOT_TAKEN
              LOAD_CONST               6 ('disqualifying: ')
              LOAD_CONST               7 (', ')
              LOAD_ATTR               13 (join + NULL|self)
              LOAD_FAST_BORROW         4 (bad)
              CALL                     1
              BINARY_OP                0 (+)
              JUMP_FORWARD             1 (to L8)
      L7:     LOAD_CONST               1 ('')

982   L8:     LOAD_CONST               8 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

988           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114F30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 995>:
995           RESUME                   0
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

Disassembly of <code object _aggregate at 0x0000018C1800B0A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 995>:
 995            RESUME                   0

 997            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 996            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2

 997    L2:     FOR_ITER                49 (to L7)
                STORE_FAST               1 (c)

 998            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 997    L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L2)

 998    L4:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              2 (SEVERITY_BLOCK)
                COMPARE_OP              88 (bool(==))

 997    L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L2)
        L6:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L2)
        L7:     END_FOR
                POP_ITER

 996    L8:     STORE_FAST               2 (blockers)
                STORE_FAST               1 (c)

1001            LOAD_CONST               3 ('verdict')
                LOAD_FAST_BORROW         2 (blockers)
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L9)
                NOT_TAKEN
                LOAD_GLOBAL              4 (VERDICT_NOT_READY)
                JUMP_FORWARD             5 (to L10)
        L9:     LOAD_GLOBAL              6 (VERDICT_READY)

1002   L10:     LOAD_CONST               4 ('blockers')
                LOAD_FAST_BORROW         2 (blockers)

1003            LOAD_CONST               5 ('info')
                BUILD_LIST               0

1000            BUILD_MAP                3
                RETURN_VALUE

  --   L11:     SWAP                     2
                POP_TOP

 996            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L11 [2]
  L4 to L5 -> L11 [2]
  L6 to L8 -> L11 [2]

Disassembly of <code object __annotate__ at 0x0000018C18115020, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 1007>:
1007           RESUME                   0
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

Disassembly of <code object _operator_actions at 0x0000018C180488F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 1007>:
1007           RESUME                   0

1008           BUILD_LIST               0
               STORE_FAST               1 (out)

1009           LOAD_FAST_BORROW         0 (checks)
               GET_ITER
       L1:     FOR_ITER               109 (to L5)
               STORE_FAST               2 (c)

1010           LOAD_FAST_BORROW         2 (c)
               LOAD_CONST               0 ('status')
               BINARY_OP               26 ([])
               LOAD_CONST               1 ('FAIL')
               COMPARE_OP             119 (bool(!=))
               POP_JUMP_IF_FALSE        3 (to L2)
               NOT_TAKEN

1011           JUMP_BACKWARD           19 (to L1)

1012   L2:     LOAD_FAST_BORROW         2 (c)
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

1013           LOAD_FAST                1 (out)
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

1009   L5:     END_FOR
               POP_ITER

1014           LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114030, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 1017>:
1017           RESUME                   0
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

Disassembly of <code object evaluate at 0x0000018C177C5D50, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 1017>:
1017           RESUME                   0

1018           BUILD_LIST               0
               STORE_FAST               1 (checks)

1019           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL              3 (check_pas186_files_present + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1020           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL              5 (check_prior_readiness_gates_callable + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1021           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL              7 (check_required_migrations_present + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1022           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL              9 (check_no_forbidden_future_migrations + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1023           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             11 (check_pas186_doc_clauses + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1024           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             13 (check_pas186_docs_no_forbidden_scope + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1025           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             15 (check_dashboard_anchors_present + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1026           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             17 (check_dashboard_no_forbidden_tokens + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1027           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             19 (check_pas185_mounts_present + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1028           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             21 (check_main_no_autostart_worker + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1029           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             23 (check_main_mounts_required_routers + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1030           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             25 (check_no_wildcard_cors + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1031           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             27 (check_audit_service_append_only + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1032           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             29 (check_learning_dashboard_no_mutation + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1033           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             31 (check_no_live_learning_mutation + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1034           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             33 (check_no_live_adaptive_memory_mutation + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1035           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             35 (check_tenant_routes_read_only + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1036           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             37 (check_no_raw_key_reveal + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1037           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             39 (check_memory_review_intact + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1038           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             41 (check_self_no_env_or_db + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1039           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             43 (check_self_no_deploy_execution + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1041           LOAD_GLOBAL             45 (_aggregate + NULL)
               LOAD_FAST_BORROW         1 (checks)
               CALL                     1
               STORE_FAST               2 (agg)

1043           LOAD_CONST               0 ('phase')
               LOAD_CONST               1 ('PAS186')

1044           LOAD_CONST               2 ('generated_at')
               LOAD_GLOBAL             47 (_now_iso + NULL)
               CALL                     0

1045           LOAD_CONST               3 ('verdict')
               LOAD_FAST_BORROW         2 (agg)
               LOAD_CONST               3 ('verdict')
               BINARY_OP               26 ([])

1046           LOAD_CONST               4 ('ready')
               LOAD_FAST_BORROW         2 (agg)
               LOAD_CONST               3 ('verdict')
               BINARY_OP               26 ([])
               LOAD_GLOBAL             48 (VERDICT_READY)
               COMPARE_OP              72 (==)

1047           LOAD_CONST               5 ('blocker_count')
               LOAD_GLOBAL             51 (len + NULL)
               LOAD_FAST_BORROW         2 (agg)
               LOAD_CONST               6 ('blockers')
               BINARY_OP               26 ([])
               CALL                     1

1048           LOAD_CONST               7 ('info_count')
               LOAD_GLOBAL             51 (len + NULL)
               LOAD_FAST_BORROW         2 (agg)
               LOAD_CONST               8 ('info')
               BINARY_OP               26 ([])
               CALL                     1

1049           LOAD_CONST               9 ('check_count')
               LOAD_GLOBAL             51 (len + NULL)
               LOAD_FAST_BORROW         1 (checks)
               CALL                     1

1050           LOAD_CONST              10 ('pass_count')
               LOAD_GLOBAL             53 (sum + NULL)
               LOAD_CONST              11 (<code object <genexpr> at 0x0000018C180531B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 1050>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         1 (checks)
               GET_ITER
               CALL                     0
               CALL                     1

1051           LOAD_CONST              12 ('fail_count')
               LOAD_GLOBAL             53 (sum + NULL)
               LOAD_CONST              13 (<code object <genexpr> at 0x0000018C18053750, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 1051>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         1 (checks)
               GET_ITER
               CALL                     0
               CALL                     1

1052           LOAD_CONST              14 ('checks')
               LOAD_FAST_BORROW         1 (checks)

1053           LOAD_CONST              15 ('operator_actions')
               LOAD_GLOBAL             55 (_operator_actions + NULL)
               LOAD_FAST_BORROW         1 (checks)
               CALL                     1

1042           BUILD_MAP               11
               RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C180531B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 1050>:
1050           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C18053750, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 1051>:
1051           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C181156B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 1060>:
1060           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C180FC3F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 1060>:
1060           RESUME                   0

1061           LOAD_GLOBAL              0 (argparse)
               LOAD_ATTR                2 (ArgumentParser)
               PUSH_NULL

1062           LOAD_CONST               0 ('pas186_final_cutover_readiness_check')

1064           LOAD_CONST               1 ('PAS186 — Final pilot cutover readiness gate. Read-only — never reads .env, never touches Supabase, never executes a deploy / migration / rollback.')

1061           LOAD_CONST               2 (('prog', 'description'))
               CALL_KW                  2
               STORE_FAST               0 (p)

1070           LOAD_FAST_BORROW         0 (p)
               LOAD_ATTR                5 (add_argument + NULL|self)
               LOAD_CONST               3 ('--repo-root')
               LOAD_GLOBAL              6 (_REPO_ROOT_DEFAULT)
               LOAD_CONST               4 (('default',))
               CALL_KW                  2
               POP_TOP

1071           LOAD_FAST_BORROW         0 (p)
               LOAD_ATTR                5 (add_argument + NULL|self)
               LOAD_CONST               5 ('--output')
               LOAD_GLOBAL              8 (REPORT_FILENAME)
               LOAD_CONST               4 (('default',))
               CALL_KW                  2
               POP_TOP

1072           LOAD_FAST_BORROW         0 (p)
               LOAD_ATTR                5 (add_argument + NULL|self)
               LOAD_CONST               6 ('--json')
               LOAD_CONST               7 ('store_true')
               LOAD_CONST               8 (('action',))
               CALL_KW                  2
               POP_TOP

1073           LOAD_FAST_BORROW         0 (p)
               LOAD_ATTR                5 (add_argument + NULL|self)
               LOAD_CONST               9 ('--summary-only')
               LOAD_CONST               7 ('store_true')
               LOAD_CONST               8 (('action',))
               CALL_KW                  2
               POP_TOP

1074           LOAD_FAST_BORROW         0 (p)
               LOAD_ATTR                5 (add_argument + NULL|self)
               LOAD_CONST              10 ('--strict')
               LOAD_CONST               7 ('store_true')
               LOAD_CONST               8 (('action',))
               CALL_KW                  2
               POP_TOP

1075           LOAD_FAST_BORROW         0 (p)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18115110, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 1078>:
1078           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C17D8C5C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 1078>:
1078           RESUME                   0

1079           LOAD_GLOBAL              1 (print + NULL)

1080           LOAD_CONST               0 ('[PAS186] verdict=')
               LOAD_FAST_BORROW         0 (report)
               LOAD_CONST               1 ('verdict')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               LOAD_CONST               2 (' blockers=')

1081           LOAD_FAST_BORROW         0 (report)
               LOAD_CONST               3 ('blocker_count')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               LOAD_CONST               4 (' info=')

1082           LOAD_FAST_BORROW         0 (report)
               LOAD_CONST               5 ('info_count')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               LOAD_CONST               6 (' checks=')

1083           LOAD_FAST_BORROW         0 (report)
               LOAD_CONST               7 ('check_count')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               LOAD_CONST               8 (' pass=')

1084           LOAD_FAST_BORROW         0 (report)
               LOAD_CONST               9 ('pass_count')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               LOAD_CONST              10 (' fail=')

1085           LOAD_FAST_BORROW         0 (report)
               LOAD_CONST              11 ('fail_count')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE

1080           BUILD_STRING            12

1079           CALL                     1
               POP_TOP

1087           LOAD_FAST_BORROW         0 (report)
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

1088           LOAD_FAST_BORROW         1 (actions)
               TO_BOOL
               POP_JUMP_IF_FALSE       93 (to L5)
               NOT_TAKEN

1089           LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST              13 ('[PAS186] operator actions:')
               CALL                     1
               POP_TOP

1090           LOAD_FAST_BORROW         1 (actions)
               LOAD_CONST              14 (slice(None, 25, None))
               BINARY_OP               26 ([])
               GET_ITER
       L2:     FOR_ITER                17 (to L3)
               STORE_FAST               2 (a)

1091           LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST              15 ('  - ')
               LOAD_FAST_BORROW         2 (a)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           19 (to L2)

1090   L3:     END_FOR
               POP_ITER

1092           LOAD_GLOBAL              5 (len + NULL)
               LOAD_FAST_BORROW         1 (actions)
               CALL                     1
               LOAD_SMALL_INT          25
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE       34 (to L4)
               NOT_TAKEN

1093           LOAD_GLOBAL              1 (print + NULL)
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

1092   L4:     LOAD_CONST              18 (None)
               RETURN_VALUE

1088   L5:     LOAD_CONST              18 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025030, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 1096>:
1096           RESUME                   0
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

Disassembly of <code object _write_report at 0x0000018C180FCF30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 1096>:
1096           RESUME                   0

1097           NOP

1098   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

1099           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

1100           LOAD_CONST               3 ('utf-8')

1098           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

1102           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

1103   L4:     LOAD_GLOBAL             11 (print + NULL)

1104           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

1105           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

1104           BUILD_STRING             4

1106           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

1103           LOAD_CONST               7 (('file',))
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

1102   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18115200, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 1110>:
1110           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17D89750, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas186_final_cutover_readiness_check.py", line 1110>:
1110            RESUME                   0

1111            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

1112            NOP

1113    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

1117    L2:     LOAD_GLOBAL             10 (os)
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

1118            LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               21 (isdir + NULL|self)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L4)
                NOT_TAKEN

1119            LOAD_GLOBAL             23 (print + NULL)
                LOAD_CONST               2 ('error: --repo-root not a directory: ')
                LOAD_FAST                4 (repo_root)
                FORMAT_SIMPLE
                BUILD_STRING             2
                LOAD_GLOBAL             24 (sys)
                LOAD_ATTR               26 (stderr)
                LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

1120            LOAD_SMALL_INT           2
                RETURN_VALUE

1122    L4:     LOAD_GLOBAL             29 (evaluate + NULL)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                STORE_FAST               5 (report)

1124            LOAD_FAST                2 (args)
                LOAD_ATTR               30 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L5)
                NOT_TAKEN

1125            LOAD_GLOBAL             33 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               34 (output)
                LOAD_FAST                5 (report)
                CALL                     2
                POP_TOP

1127    L5:     LOAD_GLOBAL             37 (_print_summary + NULL)
                LOAD_FAST                5 (report)
                CALL                     1
                POP_TOP

1129            LOAD_FAST                2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L6)
                NOT_TAKEN

1130            LOAD_GLOBAL             23 (print + NULL)
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

1132    L6:     LOAD_FAST                5 (report)
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

1114            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L17)
                NOT_TAKEN
                STORE_FAST               3 (e)

1115    L9:     LOAD_FAST                3 (e)
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

1114   L17:     RERAISE                  0

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
