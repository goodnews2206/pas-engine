# scripts_readiness/pas178_audit_window_chain_readiness_check

- **pyc:** `scripts\__pycache__\pas178_audit_window_chain_readiness_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/pas178_audit_window_chain_readiness_check.py`
- **co_filename (from bytecode):** `scripts/pas178_audit_window_chain_readiness_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS178 — Cross-window audit chain + verification persistence readiness gate.

Deterministic, non-mutating evaluator for "is PAS178 wired
correctly and free of regressions in the PAS160-PAS177
doctrine?".

Walks the repo and verifies:

  * PAS160-PAS177 readiness scripts still exist.
  * PAS178 surfaces exist:
      - scripts/migrate_v26_audit_window_chain.sql
      - scripts/migrate_v27_audit_verification_runs.sql
      - app/services/operator/audit_window_chain.py
      - app/services/operator/audit_verification_runs.py
      - app/services/tenant/tenant_audit_dashboard.py
      - scripts/verify_audit_window_chain.py
      - scripts/persist_audit_verification_run.py
      - scripts/pas178_audit_window_chain_readiness_check.py
      - docs/pas178_audit_window_chain_and_dashboards.md
      - tests/mvp/test_pas178_audit_window_chain.py
  * v26 SQL carries PROPOSAL ONLY + DO NOT EXECUTE + closed
    actor_type + status enums + RLS tenant SELECT scoped +
    tenant INSERT denied + service_role INSERT-only +
    no UPDATE / no DELETE for tenant AND service_role.
  * v27 SQL carries PROPOSAL ONLY + DO NOT EXECUTE + closed
    verification_type + status enums + RLS tenant SELECT
    scoped + tenant INSERT denied + service_role INSERT-only +
    no UPDATE / no DELETE policies.
  * audit_window_chain service exposes the documented surface
    (compute / generate / verify / chain_status_report /
    brokerage_chain_badge + closed enums + metadata allow-list).
  * audit_window_chain has NO update / delete helpers
    (append-only invariant).
  * audit_verification_runs service exposes the documented
    surface (build / persist / list / summary / latest-badge +
    closed enums + metadata allow-list).
  * audit_verification_runs has NO update / delete helpers
    (append-only invariant).
  * tenant_audit_dashboard exposes the documented surface
    (dashboard_summary / chain_status_summary /
    verification_history_summary / non_repudiation_summary +
    closed payload-key allow-list).
  * tenant_audit_dashboard has NO update / delete helpers.
  * tenant_portal exposes the three new routes
    (GET /tenant/audit/dashboard,
     GET /tenant/audit/chain-status,
     GET /tenant/audit/verification-history) under
    require_brokerage.
  * operator_brokerages exposes the two new routes
    (GET /operator/brokerages/{id}/audit-chain-status,
     GET /operator/brokerages/{id}/verification-runs) under
    require_admin.
  * verify_audit_window_chain CLI is read-only by default.
  * persist_audit_verification_run CLI is dry-run by default;
    --execute required to write.
  * No autonomous remediation surfaces.
  * audit_service.py STILL has no UPDATE / DELETE helpers
    (PAS174/PAS175/PAS176/PAS177 carry-forward).
  * No Gmail / Google / OAuth / IMAP / POP3 / inbox-scan /
    Memory Review / embedding / vector / Composio / TrustClaw
    / OpenAI / Anthropic imports.
  * Memory Review (PAS147-PAS158) untouched.
  * Event contract registers every PAS178 event type.
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

`__annotate__`, `_aggregate`, `_build_parser`, `_check`, `_now_iso`, `_operator_actions`, `_print_summary`, `_read_text`, `_strip_python_comments_and_strings`, `_write_report`, `check_ack_store_invariant`, `check_audit_service_invariant`, `check_chain_service`, `check_dashboard_service`, `check_doc_required_clauses`, `check_event_contract`, `check_files_present`, `check_memory_review_intact`, `check_no_forbidden_imports`, `check_no_inbox_scan_tokens`, `check_no_startup_worker`, `check_operator_routes`, `check_persist_script`, `check_prior_phases_intact`, `check_runs_service`, `check_self_no_env_or_db`, `check_tenant_routes`, `check_v26_sql`, `check_v27_sql`, `check_verify_script`, `check_worker_off_by_default`, `evaluate`, `main`

## Env-key candidates

`BLOCK`, `FAIL`, `NOT_READY`, `PAS178`, `PASS`, `READY`

## String constants (redacted where noted)

- '\nPAS178 — Cross-window audit chain + verification persistence readiness gate.\n\nDeterministic, non-mutating evaluator for "is PAS178 wired\ncorrectly and free of regressions in the PAS160-PAS177\ndoctrine?".\n\nWalks the repo and verifies:\n\n  * PAS160-PAS177 readiness scripts still exist.\n  * PAS178 surfaces exist:\n      - scripts/migrate_v26_audit_window_chain.sql\n      - scripts/migrate_v27_audit_verification_runs.sql\n      - app/services/operator/audit_window_chain.py\n      - app/services/operator/audit_verification_runs.py\n      - app/services/tenant/tenant_audit_dashboard.py\n      - scripts/verify_audit_window_chain.py\n      - scripts/persist_audit_verification_run.py\n      - scripts/pas178_audit_window_chain_readiness_check.py\n      - docs/pas178_audit_window_chain_and_dashboards.md\n      - tests/mvp/test_pas178_audit_window_chain.py\n  * v26 SQL carries PROPOSAL ONLY + DO NOT EXECUTE + closed\n    actor_type + status enums + RLS tenant SELECT scoped +\n    tenant INSERT denied + service_role INSERT-only +\n    no UPDATE / no DELETE for tenant AND service_role.\n  * v27 SQL carries PROPOSAL ONLY + DO NOT EXECUTE + closed\n    verification_type + status enums + RLS tenant SELECT\n    scoped + tenant INSERT denied + service_role INSERT-only +\n    no UPDATE / no DELETE policies.\n  * audit_window_chain service exposes the documented surface\n    (compute / generate / verify / chain_status_report /\n    brokerage_chain_badge + closed enums + metadata allow-list).\n  * audit_window_chain has NO update / delete helpers\n    (append-only invariant).\n  * audit_verification_runs service exposes the documented\n    surface (build / persist / list / summary / latest-badge +\n    closed enums + metadata allow-list).\n  * audit_verification_runs has NO update / delete helpers\n    (append-only invariant).\n  * tenant_audit_dashboard exposes the documented surface\n    (dashboard_summary / chain_status_summary /\n    verification_history_summary / non_repudiation_summary +\n    closed payload-key allow-list).\n  * tenant_audit_dashboard has NO update / delete helpers.\n  * tenant_portal exposes the three new routes\n    (GET /tenant/audit/dashboard,\n     GET /tenant/audit/chain-status,\n     GET /tenant/audit/verification-history) under\n    require_brokerage.\n  * operator_brokerages exposes the two new routes\n    (GET /operator/brokerages/{id}/audit-chain-status,\n     GET /operator/brokerages/{id}/verification-runs) under\n    require_admin.\n  * verify_audit_window_chain CLI is read-only by default.\n  * persist_audit_verification_run CLI is dry-run by default;\n    --execute required to write.\n  * No autonomous remediation surfaces.\n  * audit_service.py STILL has no UPDATE / DELETE helpers\n    (PAS174/PAS175/PAS176/PAS177 carry-forward).\n  * No Gmail / Google / OAuth / IMAP / POP3 / inbox-scan /\n    Memory Review / embedding / vector / Composio / TrustClaw\n    / OpenAI / Anthropic imports.\n  * Memory Review (PAS147-PAS158) untouched.\n  * Event contract registers every PAS178 event type.\n  * Worker still OFF by default; FastAPI lifespan does not\n    auto-start the worker.\n  * Supports --summary-only / --json.\n  * Exits 0 ready, 1 blockers, 2 bad args.\n  * Never reads .env.\n  * Never touches production data.\n'
- 'utf-8'
- 'READY'
- 'NOT_READY'
- 'BLOCK'
- 'severity'
- 'detail'
- 'pas178_audit_window_chain_readiness_report.json'
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
- 'Required PAS178 file present: '
- 'missing'
- 'prior_phase:'
- 'Prior-phase readiness script intact: '
- 'missing — PAS178 must not delete'
- 'memory_review:'
- 'Memory Review file present: '
- 'Memory Review file deleted — PAS178 must not touch'
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
- 'operator'
- 'audit_window_chain.py'
- 'chain_service:'
- 'Cross-window chain service token: '
- 'missing token '
- 'chain_service:append_only_invariant'
- 'Cross-window chain service has no UPDATE / DELETE helpers'
- 'audit_verification_runs.py'
- 'runs_service:'
- 'Verification-runs service token: '
- 'runs_service:append_only_invariant'
- 'Verification-runs service has no UPDATE / DELETE helpers'
- 'tenant'
- 'tenant_audit_dashboard.py'
- 'dashboard_service:'
- 'Tenant audit dashboard token: '
- 'dashboard_service:no_mutation'
- 'Tenant audit dashboard has no mutation helpers'
- 'routes'
- 'tenant_portal.py'
- 'tenant_routes:'
- 'Tenant route token: '
- 'operator_brokerages.py'
- 'operator_routes:'
- 'Operator route token: '
- 'require_admin'
- 'operator_routes:require_admin'
- 'Operator routes use require_admin (X-Admin-Key)'
- 'missing require_admin token'
- 'scripts'
- 'verify_audit_window_chain.py'
- 'verify_script:'
- 'Verify-chain CLI token: '
- 'verify_script:read_only'
- 'Verify-chain CLI is read-only (no DB writes via the supabase fluent API)'
- 'disqualifying patterns: '
- 'persist_audit_verification_run.py'
- 'persist_script:'
- 'Persist-verification-run CLI token: '
- '"--execute", action="store_true"'
- "'--execute', action='store_true'"
- '"--execute", action=\'store_true\''
- '\'--execute\', action="store_true"'
- 'persist_script:dry_run_default'
- 'Persist-verification-run CLI is dry-run by default (--execute required)'
- 'missing --execute store_true flag'
- 'persist_script:append_only'
- 'Persist-verification-run CLI does not UPDATE/DELETE'
- 'PAS174/PAS175/PAS176/PAS177 invariant: audit_service has no\nUPDATE / DELETE helpers. PAS178 must preserve.'
- 'audit_service.py'
- 'audit_service:append_only_carry'
- 'Audit service still has no UPDATE / DELETE mutation helpers (carry-forward invariant)'
- 'PAS177 invariant: tenant ack store has no UPDATE / DELETE\nhelpers. PAS178 must preserve.'
- 'tenant_audit_ack_store.py'
- 'ack_store:append_only_carry'
- 'Tenant ack store still has no UPDATE / DELETE mutation helpers (carry-forward invariant)'
- 'migrate_v26_audit_window_chain.sql'
- 'proposal only'
- 'v26_sql:proposal_only'
- "v26 SQL carries 'PROPOSAL ONLY' guardrail"
- "missing 'PROPOSAL ONLY' label"
- 'do not execute'
- 'v26_sql:do_not_execute'
- "v26 SQL carries 'DO NOT EXECUTE' trailer"
- 'missing trailer'
- 'CREATE TABLE IF NOT EXISTS pas_audit_window_chain'
- 'v26_sql:table_present'
- 'v26 SQL creates pas_audit_window_chain'
- 'missing CREATE TABLE'
- 'v26_sql:closed_actor_type_enum'
- 'v26 SQL carries the closed actor_type enum'
- 'missing one or more actor_type literals'
- 'v26_sql:closed_status_enum'
- 'v26 SQL carries the closed status enum'
- 'missing one or more status literals'
- 'pas_audit_window_chain_tenant_no_insert'
- 'pas_audit_window_chain_tenant_no_update'
- 'pas_audit_window_chain_tenant_no_delete'
- 'pas_audit_window_chain_service_role_no_update'
- 'pas_audit_window_chain_service_role_no_delete'
- 'v26_sql:append_only_policies'
- 'v26 SQL denies tenant INSERT + tenant UPDATE/DELETE + service_role UPDATE/DELETE'
- 'missing one or more no-update/no-delete/no-insert policies'
- 'pas_audit_window_chain_tenant_select'
- "brokerage_id = (auth.jwt() ->> 'brokerage_id')"
- 'v26_sql:tenant_select_scoped'
- 'v26 SQL scopes tenant SELECT to own brokerage_id'
- "expected pas_audit_window_chain_tenant_select policy with brokerage_id == auth.jwt()->>'brokerage_id'"
- "'^[0-9a-f]{64}$'"
- 'v26_sql:sha256_check_constraints'
- 'v26 SQL pins hash columns to sha256 hex shape'
- 'missing ^[0-9a-f]{64}$ regex'
- 'migrate_v27_audit_verification_runs.sql'
- 'v27_sql:proposal_only'
- "v27 SQL carries 'PROPOSAL ONLY' guardrail"
- 'v27_sql:do_not_execute'
- "v27 SQL carries 'DO NOT EXECUTE' trailer"
- 'CREATE TABLE IF NOT EXISTS pas_audit_verification_runs'
- 'v27_sql:table_present'
- 'v27 SQL creates pas_audit_verification_runs'
- 'v27_sql:closed_verification_type_enum'
- 'v27 SQL carries the closed verification_type enum'
- 'missing one or more verification_type literals'
- 'v27_sql:closed_status_enum'
- 'v27 SQL carries the closed status enum'
- 'pas_audit_verification_runs_tenant_no_insert'
- 'pas_audit_verification_runs_tenant_no_update'
- 'pas_audit_verification_runs_tenant_no_delete'
- 'pas_audit_verification_runs_service_role_no_update'
- 'pas_audit_verification_runs_service_role_no_delete'
- 'v27_sql:append_only_policies'
- 'v27 SQL denies tenant INSERT + tenant UPDATE/DELETE + service_role UPDATE/DELETE'
- 'pas_audit_verification_runs_tenant_select'
- 'v27_sql:tenant_select_scoped'
- 'v27 SQL scopes tenant SELECT to own brokerage_id'
- 'missing tenant SELECT policy with brokerage_id scope'
- 'events'
- 'contract.py'
- 'events:'
- 'Event contract registers '
- 'missing event type '
- 'app/services/operator/audit_window_chain.py'
- 'forbidden_import:'
- 'No forbidden imports: '
- 'forbidden import prefixes: '
- 'no_inbox_scan:'
- 'No inbox-scanning tokens: '
- 'inbox-scan tokens present: '
- 'docs'
- 'pas178_audit_window_chain_and_dashboards.md'
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
- 'PAS178 readiness checker never reads .env / touches DB'
- 'checks'
- 'verdict'
- 'blockers'
- 'info'
- 'List[str]'
- ' — '
- 'see report'
- 'phase'
- 'PAS178'
- 'generated_at'
- 'ready'
- 'blocker_count'
- 'info_count'
- 'check_count'
- 'pass_count'
- 'fail_count'
- 'operator_actions'
- 'argparse.ArgumentParser'
- 🔒 '<REDACTED:high-entropy blob, len=41>'
- 'PAS178 — Evaluate cross-window audit chain + verification persistence + tenant dashboard surfaces. Read-only — never reads .env, never touches Supabase, never runs a migration.'
- '--repo-root'
- '--output'
- '--json'
- 'store_true'
- '--summary-only'
- '--strict'
- 'report'
- 'None'
- '[PAS178] verdict='
- ' blockers='
- ' info='
- ' checks='
- ' pass='
- ' fail='
- '[PAS178] operator actions:'
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

   1           LOAD_CONST               0 ('\nPAS178 — Cross-window audit chain + verification persistence readiness gate.\n\nDeterministic, non-mutating evaluator for "is PAS178 wired\ncorrectly and free of regressions in the PAS160-PAS177\ndoctrine?".\n\nWalks the repo and verifies:\n\n  * PAS160-PAS177 readiness scripts still exist.\n  * PAS178 surfaces exist:\n      - scripts/migrate_v26_audit_window_chain.sql\n      - scripts/migrate_v27_audit_verification_runs.sql\n      - app/services/operator/audit_window_chain.py\n      - app/services/operator/audit_verification_runs.py\n      - app/services/tenant/tenant_audit_dashboard.py\n      - scripts/verify_audit_window_chain.py\n      - scripts/persist_audit_verification_run.py\n      - scripts/pas178_audit_window_chain_readiness_check.py\n      - docs/pas178_audit_window_chain_and_dashboards.md\n      - tests/mvp/test_pas178_audit_window_chain.py\n  * v26 SQL carries PROPOSAL ONLY + DO NOT EXECUTE + closed\n    actor_type + status enums + RLS tenant SELECT scoped +\n    tenant INSERT denied + service_role INSERT-only +\n    no UPDATE / no DELETE for tenant AND service_role.\n  * v27 SQL carries PROPOSAL ONLY + DO NOT EXECUTE + closed\n    verification_type + status enums + RLS tenant SELECT\n    scoped + tenant INSERT denied + service_role INSERT-only +\n    no UPDATE / no DELETE policies.\n  * audit_window_chain service exposes the documented surface\n    (compute / generate / verify / chain_status_report /\n    brokerage_chain_badge + closed enums + metadata allow-list).\n  * audit_window_chain has NO update / delete helpers\n    (append-only invariant).\n  * audit_verification_runs service exposes the documented\n    surface (build / persist / list / summary / latest-badge +\n    closed enums + metadata allow-list).\n  * audit_verification_runs has NO update / delete helpers\n    (append-only invariant).\n  * tenant_audit_dashboard exposes the documented surface\n    (dashboard_summary / chain_status_summary /\n    verification_history_summary / non_repudiation_summary +\n    closed payload-key allow-list).\n  * tenant_audit_dashboard has NO update / delete helpers.\n  * tenant_portal exposes the three new routes\n    (GET /tenant/audit/dashboard,\n     GET /tenant/audit/chain-status,\n     GET /tenant/audit/verification-history) under\n    require_brokerage.\n  * operator_brokerages exposes the two new routes\n    (GET /operator/brokerages/{id}/audit-chain-status,\n     GET /operator/brokerages/{id}/verification-runs) under\n    require_admin.\n  * verify_audit_window_chain CLI is read-only by default.\n  * persist_audit_verification_run CLI is dry-run by default;\n    --execute required to write.\n  * No autonomous remediation surfaces.\n  * audit_service.py STILL has no UPDATE / DELETE helpers\n    (PAS174/PAS175/PAS176/PAS177 carry-forward).\n  * No Gmail / Google / OAuth / IMAP / POP3 / inbox-scan /\n    Memory Review / embedding / vector / Composio / TrustClaw\n    / OpenAI / Anthropic imports.\n  * Memory Review (PAS147-PAS158) untouched.\n  * Event contract registers every PAS178 event type.\n  * Worker still OFF by default; FastAPI lifespan does not\n    auto-start the worker.\n  * Supports --summary-only / --json.\n  * Exits 0 ready, 1 blockers, 2 bad args.\n  * Never reads .env.\n  * Never touches production data.\n')
               STORE_NAME               0 (__doc__)

  73           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  75           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  76           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (json)
               STORE_NAME               4 (json)

  77           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (os)
               STORE_NAME               5 (os)

  78           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (sys)
               STORE_NAME               6 (sys)

  79           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              7 (datetime)
               IMPORT_FROM              7 (datetime)
               STORE_NAME               7 (datetime)
               IMPORT_FROM              8 (timezone)
               STORE_NAME               8 (timezone)
               POP_TOP

  80           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Path',))
               IMPORT_NAME              9 (pathlib)
               IMPORT_FROM             10 (Path)
               STORE_NAME              10 (Path)
               POP_TOP

  81           LOAD_SMALL_INT           0
               LOAD_CONST               5 (('List', 'Optional'))
               IMPORT_NAME             11 (typing)
               IMPORT_FROM             12 (List)
               STORE_NAME              12 (List)
               IMPORT_FROM             13 (Optional)
               STORE_NAME              13 (Optional)
               POP_TOP

  84           LOAD_NAME                6 (sys)
               LOAD_ATTR               28 (stdout)
               LOAD_NAME                6 (sys)
               LOAD_ATTR               30 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              16 (_stream)

  85           NOP

  86   L2:     LOAD_NAME               16 (_stream)
               LOAD_ATTR               35 (reconfigure + NULL|self)
               LOAD_CONST               6 ('utf-8')
               LOAD_CONST               7 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  84   L4:     END_FOR
               POP_ITER

  91           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               41 (abspath + NULL|self)

  92           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               43 (join + NULL|self)
               LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               45 (dirname + NULL|self)
               LOAD_NAME               23 (__file__)
               CALL                     1
               LOAD_CONST               8 ('..')
               CALL                     2

  91           CALL                     1
               STORE_NAME              24 (_REPO_ROOT_DEFAULT)

  96           LOAD_CONST               9 ('READY')
               STORE_NAME              25 (VERDICT_READY)

  97           LOAD_CONST              10 ('NOT_READY')
               STORE_NAME              26 (VERDICT_NOT_READY)

  99           LOAD_CONST              11 ('BLOCK')
               STORE_NAME              27 (SEVERITY_BLOCK)

 106           LOAD_CONST              81 (('scripts/migrate_v26_audit_window_chain.sql', 'scripts/migrate_v27_audit_verification_runs.sql', 'app/services/operator/audit_window_chain.py', 'app/services/operator/audit_verification_runs.py', 'app/services/tenant/tenant_audit_dashboard.py', 'scripts/verify_audit_window_chain.py', 'scripts/persist_audit_verification_run.py', 'scripts/pas178_audit_window_chain_readiness_check.py', 'docs/pas178_audit_window_chain_and_dashboards.md', 'tests/mvp/test_pas178_audit_window_chain.py'))
               STORE_NAME              28 (REQUIRED_FILES)

 119           LOAD_CONST              82 (('scripts/pas160_mvp_sequence_check.py', 'scripts/pas161_lead_ingestion_readiness_check.py', 'scripts/pas162_pending_calls_readiness_check.py', 'scripts/pas163_candidate_pipeline_readiness_check.py', 'scripts/pas164_email_ingestion_readiness_check.py', 'scripts/pas165_email_auth_dedupe_readiness_check.py', 'scripts/pas166_email_dedupe_policy_readiness_check.py', 'scripts/pas167_email_secret_reaper_readiness_check.py', 'scripts/pas168_email_secret_rotation_readiness_check.py', 'scripts/pas169_crypto_roundtrip_check.py', 'scripts/pas169_launch_readiness_check.py', 'scripts/pas_launch_integrity_check.py', 'scripts/pas170_operator_survival_readiness_check.py', 'scripts/pas171_external_pilot_readiness_check.py', 'scripts/pas172_pilot_operations_readiness_check.py', 'scripts/pas173_brokerage_operator_readiness_check.py', 'scripts/pas174_operator_audit_readiness_check.py', 'scripts/pas175_audit_integrity_readiness_check.py', 'scripts/pas176_audit_chain_readiness_check.py', 'scripts/pas177_tenant_audit_verification_readiness_check.py'))
               STORE_NAME              29 (PRIOR_PHASE_FILES)

 142           LOAD_CONST              83 (('app/services/memory/review.py', 'app/services/memory/review_stats.py', 'app/services/memory/review_export.py', 'app/services/memory/review_actors.py', 'app/services/memory/review_alerts.py', 'app/services/memory/operator_console.py'))
               STORE_NAME              30 (MEMORY_REVIEW_FILES)

 152           LOAD_CONST              84 (('def compute_audit_window_chain_hash(', 'def generate_audit_window_chain_entry(', 'def verify_audit_window_chain(', 'def chain_status_report(', 'def brokerage_chain_badge(', 'ALLOWED_ACTOR_TYPES', 'ALLOWED_CHAIN_STATUSES', 'ALLOWED_METADATA_KEYS', 'GENESIS_CHAIN_SENTINEL', '_CHAIN_TABLE  = "pas_audit_window_chain"', 'audit_window_chain_store_unavailable'))
               STORE_NAME              31 (REQUIRED_CHAIN_SERVICE_TOKENS)

 168           LOAD_CONST              85 (('def update_chain_', 'def delete_chain_', 'def update_audit_window_chain_', 'def delete_audit_window_chain_', 'def mutate_chain_', 'def truncate_chain_'))
               STORE_NAME              32 (FORBIDDEN_CHAIN_MUTATION_TOKENS)

 177           LOAD_CONST              86 (('def build_verification_run_record(', 'def persist_verification_run(', 'def list_verification_runs(', 'def verification_run_summary(', 'def latest_verification_status_for_brokerage(', 'ALLOWED_VERIFICATION_TYPES', 'ALLOWED_RUN_STATUSES', 'ALLOWED_ACTOR_TYPES', 'ALLOWED_METADATA_KEYS', '_TABLE = "pas_audit_verification_runs"', 'audit_verification_runs_unavailable'))
               STORE_NAME              33 (REQUIRED_RUNS_SERVICE_TOKENS)

 193           LOAD_CONST              87 (('def update_run_', 'def delete_run_', 'def update_verification_run_', 'def delete_verification_run_', 'def mutate_run_', 'def truncate_run_'))
               STORE_NAME              34 (FORBIDDEN_RUNS_MUTATION_TOKENS)

 202           LOAD_CONST              88 (('def tenant_audit_dashboard_summary(', 'def tenant_chain_status_summary(', 'def tenant_verification_history_summary(', 'def tenant_non_repudiation_summary(', 'TENANT_DASHBOARD_PAYLOAD_KEYS', 'latest_chain_status', 'latest_verification_status', 'action_required'))
               STORE_NAME              35 (REQUIRED_DASHBOARD_TOKENS)

 214           LOAD_CONST              89 (('def update_dashboard_', 'def delete_dashboard_', 'def mutate_dashboard_'))
               STORE_NAME              36 (FORBIDDEN_DASHBOARD_MUTATION_TOKENS)

 220           LOAD_CONST              90 (('@router.get("/audit/dashboard")', '@router.get("/audit/chain-status")', '@router.get("/audit/verification-history")', 'tenant_audit_dashboard_route', 'tenant_audit_chain_status_route', 'tenant_audit_verification_history_route'))
               STORE_NAME              37 (REQUIRED_TENANT_ROUTE_TOKENS)

 230           LOAD_CONST              91 (('@router.get("/{brokerage_id}/audit-chain-status")', '@router.get("/{brokerage_id}/verification-runs")', 'get_brokerage_audit_chain_status', 'get_brokerage_verification_runs'))
               STORE_NAME              38 (REQUIRED_OPERATOR_ROUTE_TOKENS)

 237           LOAD_CONST              92 (('def verify(', '--brokerage-id', '--alert', '--json', 'verify_audit_window_chain'))
               STORE_NAME              39 (REQUIRED_VERIFY_SCRIPT_TOKENS)

 245           LOAD_CONST              93 (('def persist(', '--brokerage-id', '--verification-type', '--status', '--execute', '--json', 'build_verification_run_record', 'persist_verification_run'))
               STORE_NAME              40 (REQUIRED_PERSIST_SCRIPT_TOKENS)

 257           LOAD_CONST              94 (('tenant.audit.proof.generated', 'audit.verification.scheduled_template_generated', 'audit.window_chain.generated', 'audit.window_chain.verified', 'audit.window_chain.broken', 'audit.verification_run.persisted', 'tenant.audit.dashboard.viewed', 'tenant.audit.chain_status.viewed'))
               STORE_NAME              41 (REQUIRED_EVENT_TYPES)

 271           LOAD_CONST              95 (('import gmail', 'from gmail', 'import googleapiclient', 'from googleapiclient', 'import google.oauth2', 'from google.oauth2', 'from google.auth', 'import google.auth', 'from google_auth_oauthlib', 'import imaplib', 'from imaplib', 'import poplib', 'from poplib', 'import composio', 'from composio', 'import trustclaw', 'from trustclaw', 'import chromadb', 'from chromadb', 'import pinecone', 'from pinecone', 'import langchain', 'from langchain', 'import faiss', 'import pgvector', 'from pgvector', 'from openai import embeddings', 'from openai.embeddings', 'from app.services.memory', 'import app.services.memory', 'from anthropic', 'import anthropic', 'from openai', 'import openai'))
               STORE_NAME              42 (FORBIDDEN_IMPORT_LINE_PREFIXES)

 296           LOAD_CONST              96 (('imaplib', 'poplib', 'fetch_inbox', 'gmail_oauth', 'gmail_token', 'users().messages'))
               STORE_NAME              43 (FORBIDDEN_INBOX_TOKENS)

 310           LOAD_CONST              12 ('severity')

 312           LOAD_NAME               27 (SEVERITY_BLOCK)

 310           LOAD_CONST              13 ('detail')

 312           LOAD_CONST              14 ('')

 310           BUILD_MAP                2
               LOAD_CONST              15 (<code object __annotate__ at 0x0000018C18025F30, file "scripts/pas178_audit_window_chain_readiness_check.py", line 310>)
               MAKE_FUNCTION
               LOAD_CONST              16 (<code object _check at 0x0000018C17FA2970, file "scripts/pas178_audit_window_chain_readiness_check.py", line 310>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              44 (_check)

 323           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C17FA2F10, file "scripts/pas178_audit_window_chain_readiness_check.py", line 323>)
               MAKE_FUNCTION
               LOAD_CONST              18 (<code object _now_iso at 0x0000018C18038A30, file "scripts/pas178_audit_window_chain_readiness_check.py", line 323>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              45 (_now_iso)

 327           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA33C0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 327>)
               MAKE_FUNCTION
               LOAD_CONST              20 (<code object _read_text at 0x0000018C18053AB0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 327>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              46 (_read_text)

 334           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA35A0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 334>)
               MAKE_FUNCTION
               LOAD_CONST              22 (<code object _strip_python_comments_and_strings at 0x0000018C17D6DFC0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 334>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              47 (_strip_python_comments_and_strings)

 373           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA3D20, file "scripts/pas178_audit_window_chain_readiness_check.py", line 373>)
               MAKE_FUNCTION
               LOAD_CONST              24 (<code object check_files_present at 0x0000018C18060A50, file "scripts/pas178_audit_window_chain_readiness_check.py", line 373>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              48 (check_files_present)

 386           LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA1D40, file "scripts/pas178_audit_window_chain_readiness_check.py", line 386>)
               MAKE_FUNCTION
               LOAD_CONST              26 (<code object check_prior_phases_intact at 0x0000018C180608A0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 386>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              49 (check_prior_phases_intact)

 399           LOAD_CONST              27 (<code object __annotate__ at 0x0000018C17FA2880, file "scripts/pas178_audit_window_chain_readiness_check.py", line 399>)
               MAKE_FUNCTION
               LOAD_CONST              28 (<code object check_memory_review_intact at 0x0000018C18060C00, file "scripts/pas178_audit_window_chain_readiness_check.py", line 399>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              50 (check_memory_review_intact)

 412           LOAD_CONST              29 (<code object __annotate__ at 0x0000018C17FA2100, file "scripts/pas178_audit_window_chain_readiness_check.py", line 412>)
               MAKE_FUNCTION
               LOAD_CONST              30 (<code object check_worker_off_by_default at 0x0000018C179C3A50, file "scripts/pas178_audit_window_chain_readiness_check.py", line 412>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              51 (check_worker_off_by_default)

 429           LOAD_CONST              31 (<code object __annotate__ at 0x0000018C17FA2B50, file "scripts/pas178_audit_window_chain_readiness_check.py", line 429>)
               MAKE_FUNCTION
               LOAD_CONST              32 (<code object check_no_startup_worker at 0x0000018C17D86D90, file "scripts/pas178_audit_window_chain_readiness_check.py", line 429>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              52 (check_no_startup_worker)

 452           LOAD_CONST              33 (<code object __annotate__ at 0x0000018C17FA3780, file "scripts/pas178_audit_window_chain_readiness_check.py", line 452>)
               MAKE_FUNCTION
               LOAD_CONST              34 (<code object check_chain_service at 0x0000018C18300180, file "scripts/pas178_audit_window_chain_readiness_check.py", line 452>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              53 (check_chain_service)

 477           LOAD_CONST              35 (<code object __annotate__ at 0x0000018C17FA1E30, file "scripts/pas178_audit_window_chain_readiness_check.py", line 477>)
               MAKE_FUNCTION
               LOAD_CONST              36 (<code object check_runs_service at 0x0000018C182FFBC0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 477>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              54 (check_runs_service)

 502           LOAD_CONST              37 (<code object __annotate__ at 0x0000018C17FA2E20, file "scripts/pas178_audit_window_chain_readiness_check.py", line 502>)
               MAKE_FUNCTION
               LOAD_CONST              38 (<code object check_dashboard_service at 0x0000018C18300A20, file "scripts/pas178_audit_window_chain_readiness_check.py", line 502>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              55 (check_dashboard_service)

 527           LOAD_CONST              39 (<code object __annotate__ at 0x0000018C17FA21F0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 527>)
               MAKE_FUNCTION
               LOAD_CONST              40 (<code object check_tenant_routes at 0x0000018C179A7290, file "scripts/pas178_audit_window_chain_readiness_check.py", line 527>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              56 (check_tenant_routes)

 542           LOAD_CONST              41 (<code object __annotate__ at 0x0000018C17FA26A0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 542>)
               MAKE_FUNCTION
               LOAD_CONST              42 (<code object check_operator_routes at 0x0000018C17E598D0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 542>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              57 (check_operator_routes)

 565           LOAD_CONST              43 (<code object __annotate__ at 0x0000018C17FA2790, file "scripts/pas178_audit_window_chain_readiness_check.py", line 565>)
               MAKE_FUNCTION
               LOAD_CONST              44 (<code object check_verify_script at 0x0000018C182FF600, file "scripts/pas178_audit_window_chain_readiness_check.py", line 565>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              58 (check_verify_script)

 604           LOAD_CONST              45 (<code object __annotate__ at 0x0000018C17FA22E0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 604>)
               MAKE_FUNCTION
               LOAD_CONST              46 (<code object check_persist_script at 0x0000018C17D8B6C0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 604>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              59 (check_persist_script)

 651           LOAD_CONST              47 (<code object __annotate__ at 0x0000018C17FA24C0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 651>)
               MAKE_FUNCTION
               LOAD_CONST              48 (<code object check_audit_service_invariant at 0x0000018C182DBEA0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 651>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              60 (check_audit_service_invariant)

 678           LOAD_CONST              49 (<code object __annotate__ at 0x0000018C17FA25B0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 678>)
               MAKE_FUNCTION
               LOAD_CONST              50 (<code object check_ack_store_invariant at 0x0000018C182DD9A0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 678>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              61 (check_ack_store_invariant)

 705           LOAD_CONST              51 (<code object __annotate__ at 0x0000018C17FA23D0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 705>)
               MAKE_FUNCTION
               LOAD_CONST              52 (<code object check_v26_sql at 0x0000018C177C63A0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 705>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              62 (check_v26_sql)

 794           LOAD_CONST              53 (<code object __annotate__ at 0x0000018C17FA2D30, file "scripts/pas178_audit_window_chain_readiness_check.py", line 794>)
               MAKE_FUNCTION
               LOAD_CONST              54 (<code object check_v27_sql at 0x0000018C1863D8E0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 794>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              63 (check_v27_sql)

 873           LOAD_CONST              55 (<code object __annotate__ at 0x0000018C17FA2A60, file "scripts/pas178_audit_window_chain_readiness_check.py", line 873>)
               MAKE_FUNCTION
               LOAD_CONST              56 (<code object check_event_contract at 0x0000018C1801CFB0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 873>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              64 (check_event_contract)

 888           LOAD_CONST              57 (<code object __annotate__ at 0x0000018C17FA2C40, file "scripts/pas178_audit_window_chain_readiness_check.py", line 888>)
               MAKE_FUNCTION
               LOAD_CONST              58 (<code object check_no_forbidden_imports at 0x0000018C17F73990, file "scripts/pas178_audit_window_chain_readiness_check.py", line 888>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              65 (check_no_forbidden_imports)

 921           LOAD_CONST              59 (<code object __annotate__ at 0x0000018C17FA3690, file "scripts/pas178_audit_window_chain_readiness_check.py", line 921>)
               MAKE_FUNCTION
               LOAD_CONST              60 (<code object check_no_inbox_scan_tokens at 0x0000018C17CC1CE0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 921>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              66 (check_no_inbox_scan_tokens)

 951           LOAD_CONST              61 (<code object __annotate__ at 0x0000018C17FA3F00, file "scripts/pas178_audit_window_chain_readiness_check.py", line 951>)
               MAKE_FUNCTION
               LOAD_CONST              62 (<code object check_doc_required_clauses at 0x0000018C17CD1ED0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 951>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              67 (check_doc_required_clauses)

 989           LOAD_CONST              63 (<code object __annotate__ at 0x0000018C17FA2010, file "scripts/pas178_audit_window_chain_readiness_check.py", line 989>)
               MAKE_FUNCTION
               LOAD_CONST              64 (<code object check_self_no_env_or_db at 0x0000018C17D893A0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 989>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              68 (check_self_no_env_or_db)

1022           LOAD_CONST              65 (<code object __annotate__ at 0x0000018C17FA3870, file "scripts/pas178_audit_window_chain_readiness_check.py", line 1022>)
               MAKE_FUNCTION
               LOAD_CONST              66 (<code object _aggregate at 0x0000018C1800AA60, file "scripts/pas178_audit_window_chain_readiness_check.py", line 1022>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              69 (_aggregate)

1034           LOAD_CONST              67 (<code object __annotate__ at 0x0000018C17FA3000, file "scripts/pas178_audit_window_chain_readiness_check.py", line 1034>)
               MAKE_FUNCTION
               LOAD_CONST              68 (<code object _operator_actions at 0x0000018C180488F0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 1034>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              70 (_operator_actions)

1044           LOAD_CONST              69 (<code object __annotate__ at 0x0000018C18114030, file "scripts/pas178_audit_window_chain_readiness_check.py", line 1044>)
               MAKE_FUNCTION
               LOAD_CONST              70 (<code object evaluate at 0x0000018C177C5D50, file "scripts/pas178_audit_window_chain_readiness_check.py", line 1044>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              71 (evaluate)

1084           LOAD_CONST              71 ('pas178_audit_window_chain_readiness_report.json')
               STORE_NAME              72 (REPORT_FILENAME)

1087           LOAD_CONST              72 (<code object __annotate__ at 0x0000018C181156B0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 1087>)
               MAKE_FUNCTION
               LOAD_CONST              73 (<code object _build_parser at 0x0000018C180FC030, file "scripts/pas178_audit_window_chain_readiness_check.py", line 1087>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              73 (_build_parser)

1105           LOAD_CONST              74 (<code object __annotate__ at 0x0000018C181157A0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 1105>)
               MAKE_FUNCTION
               LOAD_CONST              75 (<code object _print_summary at 0x0000018C17D8E300, file "scripts/pas178_audit_window_chain_readiness_check.py", line 1105>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              74 (_print_summary)

1123           LOAD_CONST              76 (<code object __annotate__ at 0x0000018C18026430, file "scripts/pas178_audit_window_chain_readiness_check.py", line 1123>)
               MAKE_FUNCTION
               LOAD_CONST              77 (<code object _write_report at 0x0000018C180FC3F0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 1123>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              75 (_write_report)

1137           LOAD_CONST              97 ((None,))
               LOAD_CONST              78 (<code object __annotate__ at 0x0000018C18115890, file "scripts/pas178_audit_window_chain_readiness_check.py", line 1137>)
               MAKE_FUNCTION
               LOAD_CONST              79 (<code object main at 0x0000018C17D87D80, file "scripts/pas178_audit_window_chain_readiness_check.py", line 1137>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              76 (main)

1162           LOAD_NAME               77 (__name__)
               LOAD_CONST              80 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

1163           LOAD_NAME                6 (sys)
               LOAD_ATTR              156 (exit)
               PUSH_NULL
               LOAD_NAME               76 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

1162   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  87           LOAD_NAME               18 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  88   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          389 (to L1)

  87   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025F30, file "scripts/pas178_audit_window_chain_readiness_check.py", line 310>:
310           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('check_id')

311           LOAD_CONST               2 ('str')

310           LOAD_CONST               3 ('status')

311           LOAD_CONST               2 ('str')

310           LOAD_CONST               4 ('label')

311           LOAD_CONST               2 ('str')

310           LOAD_CONST               5 ('severity')

312           LOAD_CONST               2 ('str')

310           LOAD_CONST               6 ('detail')

312           LOAD_CONST               2 ('str')

310           LOAD_CONST               7 ('return')

313           LOAD_CONST               8 ('dict')

310           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _check at 0x0000018C17FA2970, file "scripts/pas178_audit_window_chain_readiness_check.py", line 310>:
310           RESUME                   0

315           LOAD_CONST               0 ('id')
              LOAD_FAST_BORROW         0 (check_id)

316           LOAD_CONST               1 ('status')
              LOAD_FAST_BORROW         1 (status)

317           LOAD_CONST               2 ('label')
              LOAD_FAST_BORROW         2 (label)

318           LOAD_CONST               3 ('severity')
              LOAD_FAST_BORROW         3 (severity)

319           LOAD_CONST               4 ('detail')
              LOAD_FAST_BORROW         4 (detail)

314           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "scripts/pas178_audit_window_chain_readiness_check.py", line 323>:
323           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038A30, file "scripts/pas178_audit_window_chain_readiness_check.py", line 323>:
323           RESUME                   0

324           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 327>:
327           RESUME                   0
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

Disassembly of <code object _read_text at 0x0000018C18053AB0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 327>:
 327           RESUME                   0

 328           NOP

 329   L1:     LOAD_FAST_BORROW         0 (path)
               LOAD_ATTR                1 (read_text + NULL|self)
               LOAD_CONST               0 ('utf-8')
               LOAD_CONST               1 ('replace')
               LOAD_CONST               2 (('encoding', 'errors'))
               CALL_KW                  2
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 330           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 331   L4:     POP_EXCEPT
               LOAD_CONST               3 (None)
               RETURN_VALUE

 330   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 334>:
334           RESUME                   0
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

Disassembly of <code object _strip_python_comments_and_strings at 0x0000018C17D6DFC0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 334>:
334            RESUME                   0

335            BUILD_LIST               0
               STORE_FAST               1 (out)

336            LOAD_SMALL_INT           0
               LOAD_GLOBAL              1 (len + NULL)
               LOAD_FAST_BORROW         0 (src)
               CALL                     1
               STORE_FAST_STORE_FAST   50 (n, i)

337    L1:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (i, n)
               COMPARE_OP              18 (bool(<))
               EXTENDED_ARG             1
               POP_JUMP_IF_FALSE      282 (to L13)
               NOT_TAKEN

338            LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               BINARY_OP               26 ([])
               STORE_FAST               4 (ch)

339            LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               1 ('#')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       38 (to L3)
               NOT_TAKEN

340            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_CONST               2 ('\n')
               LOAD_FAST_BORROW         2 (i)
               CALL                     2
               STORE_FAST               5 (j)

341            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L2)
               NOT_TAKEN

342            JUMP_FORWARD           240 (to L13)

343    L2:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

344            JUMP_BACKWARD           59 (to L1)

345    L3:     LOAD_FAST_BORROW         0 (src)
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

346    L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               BINARY_SLICE
               STORE_FAST               6 (quote)

347            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 98 (quote, i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               CALL                     2
               STORE_FAST               7 (end)

348            LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L5)
               NOT_TAKEN

349            JUMP_FORWARD           138 (to L13)

350    L5:     LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

351            JUMP_BACKWARD          161 (to L1)

352    L6:     LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               7 (('"', "'"))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       92 (to L12)
               NOT_TAKEN

353            LOAD_FAST                4 (ch)
               STORE_FAST               6 (quote)

354            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               5 (j)

355    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (j, n)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       63 (to L11)
               NOT_TAKEN

356            LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
               BINARY_OP               26 ([])
               LOAD_CONST               5 ('\\')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       12 (to L8)
               NOT_TAKEN

357            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           2
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)

358            JUMP_BACKWARD           30 (to L7)

359    L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
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

360    L9:     JUMP_FORWARD            11 (to L11)

361   L10:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)
               JUMP_BACKWARD           68 (to L7)

362   L11:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

363            EXTENDED_ARG             1
               JUMP_BACKWARD          259 (to L1)

364   L12:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (ch)
               CALL                     1
               POP_TOP

365            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               2 (i)
               EXTENDED_ARG             1
               JUMP_BACKWARD          288 (to L1)

366   L13:     LOAD_CONST               6 ('')
               LOAD_ATTR                9 (join + NULL|self)
               LOAD_FAST_BORROW         1 (out)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3D20, file "scripts/pas178_audit_window_chain_readiness_check.py", line 373>:
373           RESUME                   0
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

Disassembly of <code object check_files_present at 0x0000018C18060A50, file "scripts/pas178_audit_window_chain_readiness_check.py", line 373>:
373           RESUME                   0

374           BUILD_LIST               0
              STORE_FAST               1 (out)

375           LOAD_GLOBAL              0 (REQUIRED_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

376           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

377           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

378           LOAD_CONST               0 ('file:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

379           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

380   L3:     LOAD_CONST               3 ('Required PAS178 file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

381           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing')

377   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

375   L6:     END_FOR
              POP_ITER

383           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1D40, file "scripts/pas178_audit_window_chain_readiness_check.py", line 386>:
386           RESUME                   0
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

Disassembly of <code object check_prior_phases_intact at 0x0000018C180608A0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 386>:
386           RESUME                   0

387           BUILD_LIST               0
              STORE_FAST               1 (out)

388           LOAD_GLOBAL              0 (PRIOR_PHASE_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

389           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

390           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

391           LOAD_CONST               0 ('prior_phase:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

392           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

393   L3:     LOAD_CONST               3 ('Prior-phase readiness script intact: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

394           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing — PAS178 must not delete')

390   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

388   L6:     END_FOR
              POP_ITER

396           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "scripts/pas178_audit_window_chain_readiness_check.py", line 399>:
399           RESUME                   0
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

Disassembly of <code object check_memory_review_intact at 0x0000018C18060C00, file "scripts/pas178_audit_window_chain_readiness_check.py", line 399>:
399           RESUME                   0

400           BUILD_LIST               0
              STORE_FAST               1 (out)

401           LOAD_GLOBAL              0 (MEMORY_REVIEW_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

402           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

403           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

404           LOAD_CONST               0 ('memory_review:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

405           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

406   L3:     LOAD_CONST               3 ('Memory Review file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

407           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('Memory Review file deleted — PAS178 must not touch')

403   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

401   L6:     END_FOR
              POP_ITER

409           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "scripts/pas178_audit_window_chain_readiness_check.py", line 412>:
412           RESUME                   0
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

Disassembly of <code object check_worker_off_by_default at 0x0000018C179C3A50, file "scripts/pas178_audit_window_chain_readiness_check.py", line 412>:
412           RESUME                   0

413           BUILD_LIST               0
              STORE_FAST               1 (out)

414           LOAD_GLOBAL              1 (Path + NULL)
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

415           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

417           LOAD_CONST               5 ('_ENV_FLAG_ENABLED_LITERAL = "true"')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         6 (to L2)
              NOT_TAKEN
              POP_TOP

418           LOAD_CONST               6 ("_ENV_FLAG_ENABLED_LITERAL = 'true'")
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)

416   L2:     STORE_FAST               4 (literal_ok)

420           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

421           LOAD_CONST               7 ('worker:off_by_default')

422           LOAD_FAST_BORROW         4 (literal_ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               8 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               9 ('FAIL')

423   L4:     LOAD_CONST              10 ('Pending-call worker is OFF by default')

424           LOAD_FAST_BORROW         4 (literal_ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST              11 ('missing strict enable-literal constant')

420   L6:     LOAD_CONST              12 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

426           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "scripts/pas178_audit_window_chain_readiness_check.py", line 429>:
429           RESUME                   0
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

Disassembly of <code object check_no_startup_worker at 0x0000018C17D86D90, file "scripts/pas178_audit_window_chain_readiness_check.py", line 429>:
429           RESUME                   0

430           BUILD_LIST               0
              STORE_FAST               1 (out)

431           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('main.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

432           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               2 ('')
      L1:     STORE_FAST               3 (src)

433           LOAD_GLOBAL              5 (_strip_python_comments_and_strings + NULL)
              LOAD_FAST_BORROW         3 (src)
              CALL                     1
              STORE_FAST               4 (executable)

434           BUILD_LIST               0
              STORE_FAST               5 (bad)

435           LOAD_CONST               3 ('from app.services.ingestion.worker')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L2)
              NOT_TAKEN

436           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               4 ('from app.services.ingestion.worker import …')
              CALL                     1
              POP_TOP

437   L2:     LOAD_CONST               5 ('import app.services.ingestion.worker')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L3)
              NOT_TAKEN

438           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               5 ('import app.services.ingestion.worker')
              CALL                     1
              POP_TOP

439   L3:     LOAD_CONST               6 ('run_worker_loop')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L4)
              NOT_TAKEN

440           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               7 ('run_worker_loop reference')
              CALL                     1
              POP_TOP

441   L4:     LOAD_CONST               8 ('process_pending_call(')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L5)
              NOT_TAKEN

442           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               9 ('process_pending_call call')
              CALL                     1
              POP_TOP

443   L5:     LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

444           LOAD_CONST              10 ('main:no_startup_worker')

445           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L6)
              NOT_TAKEN
              LOAD_CONST              11 ('FAIL')
              JUMP_FORWARD             1 (to L7)
      L6:     LOAD_CONST              12 ('PASS')

446   L7:     LOAD_CONST              13 ('FastAPI lifespan does not auto-start the pending-call worker')

447           LOAD_FAST_BORROW         5 (bad)
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

443   L9:     LOAD_CONST              16 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

449           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "scripts/pas178_audit_window_chain_readiness_check.py", line 452>:
452           RESUME                   0
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

Disassembly of <code object check_chain_service at 0x0000018C18300180, file "scripts/pas178_audit_window_chain_readiness_check.py", line 452>:
452            RESUME                   0

453            BUILD_LIST               0
               STORE_FAST               1 (out)

454            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('services')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('operator')
               BINARY_OP               11 (/)
               LOAD_CONST               3 ('audit_window_chain.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

455            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')
       L1:     STORE_FAST               3 (src)

456            LOAD_GLOBAL              4 (REQUIRED_CHAIN_SERVICE_TOKENS)
               GET_ITER
       L2:     FOR_ITER                73 (to L7)
               STORE_FAST               4 (tok)

457            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

458            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

459            LOAD_CONST               5 ('chain_service:')
               LOAD_FAST_BORROW         4 (tok)
               LOAD_CONST               6 (slice(None, 48, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

460            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               8 ('FAIL')

461    L4:     LOAD_CONST               9 ('Cross-window chain service token: ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

462            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST              10 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

458    L6:     LOAD_CONST              11 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           75 (to L2)

456    L7:     END_FOR
               POP_ITER

464            BUILD_LIST               0
               STORE_FAST               6 (bad)

465            LOAD_GLOBAL             10 (FORBIDDEN_CHAIN_MUTATION_TOKENS)
               GET_ITER
       L8:     FOR_ITER                28 (to L10)
               STORE_FAST               4 (tok)

466            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L9)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L8)

467    L9:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (tok)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L8)

465   L10:     END_FOR
               POP_ITER

468            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

469            LOAD_CONST              12 ('chain_service:append_only_invariant')

470            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               8 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               7 ('PASS')

471   L12:     LOAD_CONST              13 ('Cross-window chain service has no UPDATE / DELETE helpers')

472            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L13)
               NOT_TAKEN
               LOAD_CONST              14 ('disqualifying tokens: ')
               LOAD_CONST              15 (', ')
               LOAD_ATTR               13 (join + NULL|self)
               LOAD_FAST_BORROW         6 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L14)
      L13:     LOAD_CONST               4 ('')

468   L14:     LOAD_CONST              11 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

474            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "scripts/pas178_audit_window_chain_readiness_check.py", line 477>:
477           RESUME                   0
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

Disassembly of <code object check_runs_service at 0x0000018C182FFBC0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 477>:
477            RESUME                   0

478            BUILD_LIST               0
               STORE_FAST               1 (out)

479            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('services')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('operator')
               BINARY_OP               11 (/)
               LOAD_CONST               3 ('audit_verification_runs.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

480            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')
       L1:     STORE_FAST               3 (src)

481            LOAD_GLOBAL              4 (REQUIRED_RUNS_SERVICE_TOKENS)
               GET_ITER
       L2:     FOR_ITER                73 (to L7)
               STORE_FAST               4 (tok)

482            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

483            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

484            LOAD_CONST               5 ('runs_service:')
               LOAD_FAST_BORROW         4 (tok)
               LOAD_CONST               6 (slice(None, 48, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

485            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               8 ('FAIL')

486    L4:     LOAD_CONST               9 ('Verification-runs service token: ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

487            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST              10 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

483    L6:     LOAD_CONST              11 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           75 (to L2)

481    L7:     END_FOR
               POP_ITER

489            BUILD_LIST               0
               STORE_FAST               6 (bad)

490            LOAD_GLOBAL             10 (FORBIDDEN_RUNS_MUTATION_TOKENS)
               GET_ITER
       L8:     FOR_ITER                28 (to L10)
               STORE_FAST               4 (tok)

491            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L9)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L8)

492    L9:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (tok)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L8)

490   L10:     END_FOR
               POP_ITER

493            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

494            LOAD_CONST              12 ('runs_service:append_only_invariant')

495            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               8 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               7 ('PASS')

496   L12:     LOAD_CONST              13 ('Verification-runs service has no UPDATE / DELETE helpers')

497            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L13)
               NOT_TAKEN
               LOAD_CONST              14 ('disqualifying tokens: ')
               LOAD_CONST              15 (', ')
               LOAD_ATTR               13 (join + NULL|self)
               LOAD_FAST_BORROW         6 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L14)
      L13:     LOAD_CONST               4 ('')

493   L14:     LOAD_CONST              11 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

499            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "scripts/pas178_audit_window_chain_readiness_check.py", line 502>:
502           RESUME                   0
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

Disassembly of <code object check_dashboard_service at 0x0000018C18300A20, file "scripts/pas178_audit_window_chain_readiness_check.py", line 502>:
502            RESUME                   0

503            BUILD_LIST               0
               STORE_FAST               1 (out)

504            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('services')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('tenant')
               BINARY_OP               11 (/)
               LOAD_CONST               3 ('tenant_audit_dashboard.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

505            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')
       L1:     STORE_FAST               3 (src)

506            LOAD_GLOBAL              4 (REQUIRED_DASHBOARD_TOKENS)
               GET_ITER
       L2:     FOR_ITER                73 (to L7)
               STORE_FAST               4 (tok)

507            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

508            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

509            LOAD_CONST               5 ('dashboard_service:')
               LOAD_FAST_BORROW         4 (tok)
               LOAD_CONST               6 (slice(None, 48, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

510            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               8 ('FAIL')

511    L4:     LOAD_CONST               9 ('Tenant audit dashboard token: ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

512            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST              10 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

508    L6:     LOAD_CONST              11 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           75 (to L2)

506    L7:     END_FOR
               POP_ITER

514            BUILD_LIST               0
               STORE_FAST               6 (bad)

515            LOAD_GLOBAL             10 (FORBIDDEN_DASHBOARD_MUTATION_TOKENS)
               GET_ITER
       L8:     FOR_ITER                28 (to L10)
               STORE_FAST               4 (tok)

516            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L9)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L8)

517    L9:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (tok)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L8)

515   L10:     END_FOR
               POP_ITER

518            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

519            LOAD_CONST              12 ('dashboard_service:no_mutation')

520            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               8 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               7 ('PASS')

521   L12:     LOAD_CONST              13 ('Tenant audit dashboard has no mutation helpers')

522            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L13)
               NOT_TAKEN
               LOAD_CONST              14 ('disqualifying tokens: ')
               LOAD_CONST              15 (', ')
               LOAD_ATTR               13 (join + NULL|self)
               LOAD_FAST_BORROW         6 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L14)
      L13:     LOAD_CONST               4 ('')

518   L14:     LOAD_CONST              11 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

524            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 527>:
527           RESUME                   0
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

Disassembly of <code object check_tenant_routes at 0x0000018C179A7290, file "scripts/pas178_audit_window_chain_readiness_check.py", line 527>:
527           RESUME                   0

528           BUILD_LIST               0
              STORE_FAST               1 (out)

529           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('routes')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('tenant_portal.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

530           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               3 ('')
      L1:     STORE_FAST               3 (src)

531           LOAD_GLOBAL              4 (REQUIRED_TENANT_ROUTE_TOKENS)
              GET_ITER
      L2:     FOR_ITER                73 (to L7)
              STORE_FAST               4 (tok)

532           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

533           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

534           LOAD_CONST               4 ('tenant_routes:')
              LOAD_FAST_BORROW         4 (tok)
              LOAD_CONST               5 (slice(None, 48, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

535           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               6 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               7 ('FAIL')

536   L4:     LOAD_CONST               8 ('Tenant route token: ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

537           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               3 ('')
              JUMP_FORWARD             4 (to L6)
      L5:     LOAD_CONST               9 ('missing token ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

533   L6:     LOAD_CONST              10 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           75 (to L2)

531   L7:     END_FOR
              POP_ITER

539           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA26A0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 542>:
542           RESUME                   0
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

Disassembly of <code object check_operator_routes at 0x0000018C17E598D0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 542>:
542            RESUME                   0

543            BUILD_LIST               0
               STORE_FAST               1 (out)

544            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('routes')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('operator_brokerages.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

545            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               3 ('')
       L1:     STORE_FAST               3 (src)

546            LOAD_GLOBAL              4 (REQUIRED_OPERATOR_ROUTE_TOKENS)
               GET_ITER
       L2:     FOR_ITER                73 (to L7)
               STORE_FAST               4 (tok)

547            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

548            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

549            LOAD_CONST               4 ('operator_routes:')
               LOAD_FAST_BORROW         4 (tok)
               LOAD_CONST               5 (slice(None, 48, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

550            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               6 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               7 ('FAIL')

551    L4:     LOAD_CONST               8 ('Operator route token: ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

552            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               3 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST               9 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

548    L6:     LOAD_CONST              10 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           75 (to L2)

546    L7:     END_FOR
               POP_ITER

555            LOAD_CONST              11 ('require_admin')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               STORE_FAST               6 (auth_ok)

556            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

557            LOAD_CONST              12 ('operator_routes:require_admin')

558            LOAD_FAST_BORROW         6 (auth_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN
               LOAD_CONST               6 ('PASS')
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST               7 ('FAIL')

559    L9:     LOAD_CONST              13 ('Operator routes use require_admin (X-Admin-Key)')

560            LOAD_FAST_BORROW         6 (auth_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST               3 ('')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST              14 ('missing require_admin token')

556   L11:     LOAD_CONST              10 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

562            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2790, file "scripts/pas178_audit_window_chain_readiness_check.py", line 565>:
565           RESUME                   0
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

Disassembly of <code object check_verify_script at 0x0000018C182FF600, file "scripts/pas178_audit_window_chain_readiness_check.py", line 565>:
565            RESUME                   0

566            BUILD_LIST               0
               STORE_FAST               1 (out)

567            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('scripts')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('verify_audit_window_chain.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

568            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               2 ('')
       L1:     STORE_FAST               3 (src)

569            LOAD_GLOBAL              4 (REQUIRED_VERIFY_SCRIPT_TOKENS)
               GET_ITER
       L2:     FOR_ITER                73 (to L7)
               STORE_FAST               4 (tok)

570            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

571            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

572            LOAD_CONST               3 ('verify_script:')
               LOAD_FAST_BORROW         4 (tok)
               LOAD_CONST               4 (slice(None, 48, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

573            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               6 ('FAIL')

574    L4:     LOAD_CONST               7 ('Verify-chain CLI token: ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

575            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST               8 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

571    L6:     LOAD_CONST               9 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           75 (to L2)

569    L7:     END_FOR
               POP_ITER

578            LOAD_GLOBAL             11 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               6 (executable)

579            BUILD_LIST               0
               STORE_FAST               7 (bad)

580            LOAD_CONST              14 (('table(_AUDIT_TABLE).insert', 'table(_MERKLE_TABLE).insert', 'table(_CHAIN_TABLE).insert', 'table(_TABLE).insert', 'table("pas_', '.insert({', '.insert([', '.update({', '.delete().execute', '.delete().eq'))
               STORE_FAST               8 (write_patterns)

592            LOAD_FAST_BORROW         8 (write_patterns)
               GET_ITER
       L8:     FOR_ITER                28 (to L10)
               STORE_FAST               9 (verb)

593            LOAD_FAST_BORROW_LOAD_FAST_BORROW 150 (verb, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L9)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L8)

594    L9:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         9 (verb)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L8)

592   L10:     END_FOR
               POP_ITER

595            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

596            LOAD_CONST              10 ('verify_script:read_only')

597            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               6 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               5 ('PASS')

598   L12:     LOAD_CONST              11 ('Verify-chain CLI is read-only (no DB writes via the supabase fluent API)')

599            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L13)
               NOT_TAKEN
               LOAD_CONST              12 ('disqualifying patterns: ')
               LOAD_CONST              13 (', ')
               LOAD_ATTR               13 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L14)
      L13:     LOAD_CONST               2 ('')

595   L14:     LOAD_CONST               9 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

601            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA22E0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 604>:
604           RESUME                   0
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

Disassembly of <code object check_persist_script at 0x0000018C17D8B6C0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 604>:
604            RESUME                   0

605            BUILD_LIST               0
               STORE_FAST               1 (out)

606            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('scripts')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('persist_audit_verification_run.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

607            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               2 ('')
       L1:     STORE_FAST               3 (src)

608            LOAD_GLOBAL              4 (REQUIRED_PERSIST_SCRIPT_TOKENS)
               GET_ITER
       L2:     FOR_ITER                73 (to L7)
               STORE_FAST               4 (tok)

609            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

610            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

611            LOAD_CONST               3 ('persist_script:')
               LOAD_FAST_BORROW         4 (tok)
               LOAD_CONST               4 (slice(None, 48, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

612            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               6 ('FAIL')

613    L4:     LOAD_CONST               7 ('Persist-verification-run CLI token: ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

614            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST               8 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

610    L6:     LOAD_CONST               9 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           75 (to L2)

608    L7:     END_FOR
               POP_ITER

619            LOAD_CONST              10 ('"--execute", action="store_true"')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        32 (to L8)
               NOT_TAKEN
               POP_TOP

620            LOAD_CONST              11 ("'--execute', action='store_true'")
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

619            COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        19 (to L8)
               NOT_TAKEN
               POP_TOP

621            LOAD_CONST              12 ('"--execute", action=\'store_true\'')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

619            COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L8)
               NOT_TAKEN
               POP_TOP

622            LOAD_CONST              13 ('\'--execute\', action="store_true"')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

618    L8:     STORE_FAST               6 (dry_run_ok)

624            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

625            LOAD_CONST              14 ('persist_script:dry_run_default')

626            LOAD_FAST_BORROW         6 (dry_run_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L10)
       L9:     LOAD_CONST               6 ('FAIL')

627   L10:     LOAD_CONST              15 ('Persist-verification-run CLI is dry-run by default (--execute required)')

628            LOAD_FAST_BORROW         6 (dry_run_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST              16 ('missing --execute store_true flag')

624   L12:     LOAD_CONST               9 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

631            LOAD_GLOBAL             11 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               7 (executable)

632            BUILD_LIST               0
               STORE_FAST               8 (bad)

633            LOAD_CONST              21 (('.update({', '.update([', '.delete().execute', '.delete().eq'))
               STORE_FAST               9 (forbidden)

639            LOAD_FAST_BORROW         9 (forbidden)
               GET_ITER
      L13:     FOR_ITER                28 (to L15)
               STORE_FAST              10 (verb)

640            LOAD_FAST_BORROW_LOAD_FAST_BORROW 167 (verb, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L14)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L13)

641   L14:     LOAD_FAST_BORROW         8 (bad)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW        10 (verb)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L13)

639   L15:     END_FOR
               POP_ITER

642            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

643            LOAD_CONST              17 ('persist_script:append_only')

644            LOAD_FAST_BORROW         8 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L16)
               NOT_TAKEN
               LOAD_CONST               6 ('FAIL')
               JUMP_FORWARD             1 (to L17)
      L16:     LOAD_CONST               5 ('PASS')

645   L17:     LOAD_CONST              18 ('Persist-verification-run CLI does not UPDATE/DELETE')

646            LOAD_FAST_BORROW         8 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L18)
               NOT_TAKEN
               LOAD_CONST              19 ('disqualifying patterns: ')
               LOAD_CONST              20 (', ')
               LOAD_ATTR               13 (join + NULL|self)
               LOAD_FAST_BORROW         8 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L19)
      L18:     LOAD_CONST               2 ('')

642   L19:     LOAD_CONST               9 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

648            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA24C0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 651>:
651           RESUME                   0
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

Disassembly of <code object check_audit_service_invariant at 0x0000018C182DBEA0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 651>:
651           RESUME                   0

654           BUILD_LIST               0
              STORE_FAST               1 (out)

655           LOAD_GLOBAL              1 (Path + NULL)
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

656           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               5 ('')
      L1:     STORE_FAST               3 (src)

657           LOAD_CONST              13 (('def update_audit_', 'def delete_audit_', 'def update_operator_audit_', 'def delete_operator_audit_', 'def mutate_audit_', 'def truncate_audit_'))
              STORE_FAST               4 (forbidden)

665           BUILD_LIST               0
              STORE_FAST               5 (bad)

666           LOAD_FAST_BORROW         4 (forbidden)
              GET_ITER
      L2:     FOR_ITER                28 (to L4)
              STORE_FAST               6 (tok)

667           LOAD_FAST_BORROW_LOAD_FAST_BORROW 99 (tok, src)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

668   L3:     LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_FAST_BORROW         6 (tok)
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           30 (to L2)

666   L4:     END_FOR
              POP_ITER

669           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

670           LOAD_CONST               6 ('audit_service:append_only_carry')

671           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               7 ('FAIL')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               8 ('PASS')

672   L6:     LOAD_CONST               9 ('Audit service still has no UPDATE / DELETE mutation helpers (carry-forward invariant)')

673           LOAD_FAST_BORROW         5 (bad)
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

669   L8:     LOAD_CONST              12 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

675           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA25B0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 678>:
678           RESUME                   0
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

Disassembly of <code object check_ack_store_invariant at 0x0000018C182DD9A0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 678>:
678           RESUME                   0

681           BUILD_LIST               0
              STORE_FAST               1 (out)

682           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               1 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('services')
              BINARY_OP               11 (/)
              LOAD_CONST               3 ('tenant')
              BINARY_OP               11 (/)
              LOAD_CONST               4 ('tenant_audit_ack_store.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

683           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               5 ('')
      L1:     STORE_FAST               3 (src)

684           LOAD_CONST              13 (('def update_ack_', 'def delete_ack_', 'def update_acknowledgement_', 'def delete_acknowledgement_', 'def mutate_ack_', 'def truncate_ack_'))
              STORE_FAST               4 (forbidden)

692           BUILD_LIST               0
              STORE_FAST               5 (bad)

693           LOAD_FAST_BORROW         4 (forbidden)
              GET_ITER
      L2:     FOR_ITER                28 (to L4)
              STORE_FAST               6 (tok)

694           LOAD_FAST_BORROW_LOAD_FAST_BORROW 99 (tok, src)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

695   L3:     LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_FAST_BORROW         6 (tok)
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           30 (to L2)

693   L4:     END_FOR
              POP_ITER

696           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

697           LOAD_CONST               6 ('ack_store:append_only_carry')

698           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               7 ('FAIL')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               8 ('PASS')

699   L6:     LOAD_CONST               9 ('Tenant ack store still has no UPDATE / DELETE mutation helpers (carry-forward invariant)')

700           LOAD_FAST_BORROW         5 (bad)
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

696   L8:     LOAD_CONST              12 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

702           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 705>:
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

Disassembly of <code object check_v26_sql at 0x0000018C177C63A0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 705>:
  --            MAKE_CELL               12 (src)

 705            RESUME                   0

 706            BUILD_LIST               0
                STORE_FAST               1 (out)

 707            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('scripts')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('migrate_v26_audit_window_chain.sql')
                BINARY_OP               11 (/)
                STORE_FAST               2 (p)

 708            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (p)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L1:     STORE_DEREF             12 (src)

 709            LOAD_DEREF              12 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_FAST               3 (lower)

 710            LOAD_CONST               3 ('proposal only')
                LOAD_FAST_BORROW         3 (lower)
                CONTAINS_OP              0 (in)
                STORE_FAST               4 (proposal_ok)

 711            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 712            LOAD_CONST               4 ('v26_sql:proposal_only')

 713            LOAD_FAST_BORROW         4 (proposal_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L2)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               6 ('FAIL')

 714    L3:     LOAD_CONST               7 ("v26 SQL carries 'PROPOSAL ONLY' guardrail")

 715            LOAD_FAST_BORROW         4 (proposal_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L4)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L5)
        L4:     LOAD_CONST               8 ("missing 'PROPOSAL ONLY' label")

 711    L5:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 717            LOAD_CONST              10 ('do not execute')
                LOAD_FAST_BORROW         3 (lower)
                CONTAINS_OP              0 (in)
                STORE_FAST               5 (do_not_exec)

 718            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 719            LOAD_CONST              11 ('v26_sql:do_not_execute')

 720            LOAD_FAST_BORROW         5 (do_not_exec)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L7)
        L6:     LOAD_CONST               6 ('FAIL')

 721    L7:     LOAD_CONST              12 ("v26 SQL carries 'DO NOT EXECUTE' trailer")

 722            LOAD_FAST_BORROW         5 (do_not_exec)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST              13 ('missing trailer')

 718    L9:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 724            LOAD_CONST              14 ('CREATE TABLE IF NOT EXISTS pas_audit_window_chain')
                LOAD_DEREF              12 (src)
                CONTAINS_OP              0 (in)
                STORE_FAST               6 (table_ok)

 725            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 726            LOAD_CONST              15 ('v26_sql:table_present')

 727            LOAD_FAST_BORROW         6 (table_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L11)
       L10:     LOAD_CONST               6 ('FAIL')

 728   L11:     LOAD_CONST              16 ('v26 SQL creates pas_audit_window_chain')

 729            LOAD_FAST_BORROW         6 (table_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L12)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L13)
       L12:     LOAD_CONST              17 ('missing CREATE TABLE')

 725   L13:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 732            LOAD_GLOBAL             10 (all)
                COPY                     1
                LOAD_COMMON_CONSTANT     3 (<built-in function all>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L17)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW        12 (src)
                BUILD_TUPLE              1
                LOAD_CONST              18 (<code object <genexpr> at 0x0000018C18026230, file "scripts/pas178_audit_window_chain_readiness_check.py", line 732>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 733            LOAD_CONST              45 (("'OPERATOR'", "'ADMIN'", "'SYSTEM'"))
                GET_ITER

 732            CALL                     0
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
                LOAD_CONST              18 (<code object <genexpr> at 0x0000018C18026230, file "scripts/pas178_audit_window_chain_readiness_check.py", line 732>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 733            LOAD_CONST              45 (("'OPERATOR'", "'ADMIN'", "'SYSTEM'"))
                GET_ITER

 732            CALL                     0
                CALL                     1
       L18:     STORE_FAST               7 (actor_types_ok)

 735            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 736            LOAD_CONST              21 ('v26_sql:closed_actor_type_enum')

 737            LOAD_FAST_BORROW         7 (actor_types_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L19)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L20)
       L19:     LOAD_CONST               6 ('FAIL')

 738   L20:     LOAD_CONST              22 ('v26 SQL carries the closed actor_type enum')

 739            LOAD_FAST_BORROW         7 (actor_types_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L21)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L22)
       L21:     LOAD_CONST              23 ('missing one or more actor_type literals')

 735   L22:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 742            LOAD_GLOBAL             10 (all)
                COPY                     1
                LOAD_COMMON_CONSTANT     3 (<built-in function all>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L26)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW        12 (src)
                BUILD_TUPLE              1
                LOAD_CONST              24 (<code object <genexpr> at 0x0000018C18024B30, file "scripts/pas178_audit_window_chain_readiness_check.py", line 742>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 743            LOAD_CONST              46 (("'GENERATED'", "'VERIFIED'", "'BROKEN'", "'SUPERSEDED'"))
                GET_ITER

 742            CALL                     0
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
                LOAD_CONST              24 (<code object <genexpr> at 0x0000018C18024B30, file "scripts/pas178_audit_window_chain_readiness_check.py", line 742>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 743            LOAD_CONST              46 (("'GENERATED'", "'VERIFIED'", "'BROKEN'", "'SUPERSEDED'"))
                GET_ITER

 742            CALL                     0
                CALL                     1
       L27:     STORE_FAST               8 (status_types_ok)

 750            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 751            LOAD_CONST              25 ('v26_sql:closed_status_enum')

 752            LOAD_FAST_BORROW         8 (status_types_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L28)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L29)
       L28:     LOAD_CONST               6 ('FAIL')

 753   L29:     LOAD_CONST              26 ('v26 SQL carries the closed status enum')

 754            LOAD_FAST_BORROW         8 (status_types_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L30)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L31)
       L30:     LOAD_CONST              27 ('missing one or more status literals')

 750   L31:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 758            LOAD_CONST              28 ('pas_audit_window_chain_tenant_no_insert')
                LOAD_DEREF              12 (src)
                CONTAINS_OP              0 (in)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       45 (to L32)
                NOT_TAKEN
                POP_TOP

 759            LOAD_CONST              29 ('pas_audit_window_chain_tenant_no_update')
                LOAD_DEREF              12 (src)
                CONTAINS_OP              0 (in)

 758            COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       32 (to L32)
                NOT_TAKEN
                POP_TOP

 760            LOAD_CONST              30 ('pas_audit_window_chain_tenant_no_delete')
                LOAD_DEREF              12 (src)
                CONTAINS_OP              0 (in)

 758            COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L32)
                NOT_TAKEN
                POP_TOP

 761            LOAD_CONST              31 ('pas_audit_window_chain_service_role_no_update')
                LOAD_DEREF              12 (src)
                CONTAINS_OP              0 (in)

 758            COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        6 (to L32)
                NOT_TAKEN
                POP_TOP

 762            LOAD_CONST              32 ('pas_audit_window_chain_service_role_no_delete')
                LOAD_DEREF              12 (src)
                CONTAINS_OP              0 (in)

 757   L32:     STORE_FAST               9 (append_only_ok)

 764            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 765            LOAD_CONST              33 ('v26_sql:append_only_policies')

 766            LOAD_FAST_BORROW         9 (append_only_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L33)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L34)
       L33:     LOAD_CONST               6 ('FAIL')

 767   L34:     LOAD_CONST              34 ('v26 SQL denies tenant INSERT + tenant UPDATE/DELETE + service_role UPDATE/DELETE')

 768            LOAD_FAST_BORROW         9 (append_only_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L35)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L36)
       L35:     LOAD_CONST              35 ('missing one or more no-update/no-delete/no-insert policies')

 764   L36:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 772            LOAD_CONST              36 ('pas_audit_window_chain_tenant_select')
                LOAD_DEREF              12 (src)
                CONTAINS_OP              0 (in)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        6 (to L37)
                NOT_TAKEN
                POP_TOP

 773            LOAD_CONST              37 ("brokerage_id = (auth.jwt() ->> 'brokerage_id')")
                LOAD_DEREF              12 (src)
                CONTAINS_OP              0 (in)

 771   L37:     STORE_FAST              10 (select_scoped)

 775            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 776            LOAD_CONST              38 ('v26_sql:tenant_select_scoped')

 777            LOAD_FAST_BORROW        10 (select_scoped)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L38)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L39)
       L38:     LOAD_CONST               6 ('FAIL')

 778   L39:     LOAD_CONST              39 ('v26 SQL scopes tenant SELECT to own brokerage_id')

 779            LOAD_FAST_BORROW        10 (select_scoped)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L40)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L41)

 780   L40:     LOAD_CONST              40 ("expected pas_audit_window_chain_tenant_select policy with brokerage_id == auth.jwt()->>'brokerage_id'")

 775   L41:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 784            LOAD_CONST              41 ("'^[0-9a-f]{64}$'")
                LOAD_DEREF              12 (src)
                CONTAINS_OP              0 (in)
                STORE_FAST              11 (sha_chk)

 785            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 786            LOAD_CONST              42 ('v26_sql:sha256_check_constraints')

 787            LOAD_FAST_BORROW        11 (sha_chk)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L42)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L43)
       L42:     LOAD_CONST               6 ('FAIL')

 788   L43:     LOAD_CONST              43 ('v26 SQL pins hash columns to sha256 hex shape')

 789            LOAD_FAST_BORROW        11 (sha_chk)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L44)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L45)
       L44:     LOAD_CONST              44 ('missing ^[0-9a-f]{64}$ regex')

 785   L45:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 791            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18026230, file "scripts/pas178_audit_window_chain_readiness_check.py", line 732>:
  --           COPY_FREE_VARS           1

 732           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 733   L2:     FOR_ITER                 9 (to L3)
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

Disassembly of <code object <genexpr> at 0x0000018C18024B30, file "scripts/pas178_audit_window_chain_readiness_check.py", line 742>:
  --           COPY_FREE_VARS           1

 742           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 743   L2:     FOR_ITER                 9 (to L3)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "scripts/pas178_audit_window_chain_readiness_check.py", line 794>:
794           RESUME                   0
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

Disassembly of <code object check_v27_sql at 0x0000018C1863D8E0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 794>:
  --            MAKE_CELL               11 (src)

 794            RESUME                   0

 795            BUILD_LIST               0
                STORE_FAST               1 (out)

 796            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('scripts')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('migrate_v27_audit_verification_runs.sql')
                BINARY_OP               11 (/)
                STORE_FAST               2 (p)

 797            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (p)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L1:     STORE_DEREF             11 (src)

 798            LOAD_DEREF              11 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_FAST               3 (lower)

 799            LOAD_CONST               3 ('proposal only')
                LOAD_FAST_BORROW         3 (lower)
                CONTAINS_OP              0 (in)
                STORE_FAST               4 (proposal_ok)

 800            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 801            LOAD_CONST               4 ('v27_sql:proposal_only')

 802            LOAD_FAST_BORROW         4 (proposal_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L2)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               6 ('FAIL')

 803    L3:     LOAD_CONST               7 ("v27 SQL carries 'PROPOSAL ONLY' guardrail")

 804            LOAD_FAST_BORROW         4 (proposal_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L4)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L5)
        L4:     LOAD_CONST               8 ("missing 'PROPOSAL ONLY' label")

 800    L5:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 806            LOAD_CONST              10 ('do not execute')
                LOAD_FAST_BORROW         3 (lower)
                CONTAINS_OP              0 (in)
                STORE_FAST               5 (do_not_exec)

 807            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 808            LOAD_CONST              11 ('v27_sql:do_not_execute')

 809            LOAD_FAST_BORROW         5 (do_not_exec)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L7)
        L6:     LOAD_CONST               6 ('FAIL')

 810    L7:     LOAD_CONST              12 ("v27 SQL carries 'DO NOT EXECUTE' trailer")

 811            LOAD_FAST_BORROW         5 (do_not_exec)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST              13 ('missing trailer')

 807    L9:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 813            LOAD_CONST              14 ('CREATE TABLE IF NOT EXISTS pas_audit_verification_runs')
                LOAD_DEREF              11 (src)
                CONTAINS_OP              0 (in)
                STORE_FAST               6 (table_ok)

 814            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 815            LOAD_CONST              15 ('v27_sql:table_present')

 816            LOAD_FAST_BORROW         6 (table_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L11)
       L10:     LOAD_CONST               6 ('FAIL')

 817   L11:     LOAD_CONST              16 ('v27 SQL creates pas_audit_verification_runs')

 818            LOAD_FAST_BORROW         6 (table_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L12)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L13)
       L12:     LOAD_CONST              17 ('missing CREATE TABLE')

 814   L13:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 821            LOAD_GLOBAL             10 (all)
                COPY                     1
                LOAD_COMMON_CONSTANT     3 (<built-in function all>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L17)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW        11 (src)
                BUILD_TUPLE              1
                LOAD_CONST              18 (<code object <genexpr> at 0x0000018C18025A30, file "scripts/pas178_audit_window_chain_readiness_check.py", line 821>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 822            LOAD_CONST              41 (("'AUDIT_ROW_HASH_CHAIN'", "'MERKLE_WINDOW'", "'CROSS_WINDOW_CHAIN'", "'FULL_AUDIT_INTEGRITY'"))
                GET_ITER

 821            CALL                     0
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
                LOAD_FAST_BORROW        11 (src)
                BUILD_TUPLE              1
                LOAD_CONST              18 (<code object <genexpr> at 0x0000018C18025A30, file "scripts/pas178_audit_window_chain_readiness_check.py", line 821>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 822            LOAD_CONST              41 (("'AUDIT_ROW_HASH_CHAIN'", "'MERKLE_WINDOW'", "'CROSS_WINDOW_CHAIN'", "'FULL_AUDIT_INTEGRITY'"))
                GET_ITER

 821            CALL                     0
                CALL                     1
       L18:     STORE_FAST               7 (type_ok)

 829            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 830            LOAD_CONST              21 ('v27_sql:closed_verification_type_enum')

 831            LOAD_FAST_BORROW         7 (type_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L19)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L20)
       L19:     LOAD_CONST               6 ('FAIL')

 832   L20:     LOAD_CONST              22 ('v27 SQL carries the closed verification_type enum')

 833            LOAD_FAST_BORROW         7 (type_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L21)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L22)
       L21:     LOAD_CONST              23 ('missing one or more verification_type literals')

 829   L22:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 836            LOAD_GLOBAL             10 (all)
                COPY                     1
                LOAD_COMMON_CONSTANT     3 (<built-in function all>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L26)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW        11 (src)
                BUILD_TUPLE              1
                LOAD_CONST              24 (<code object <genexpr> at 0x0000018C18025830, file "scripts/pas178_audit_window_chain_readiness_check.py", line 836>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 837            LOAD_CONST              42 (("'PASSED'", "'FAILED'", "'SKIPPED'", "'PARTIAL'"))
                GET_ITER

 836            CALL                     0
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
                LOAD_FAST_BORROW        11 (src)
                BUILD_TUPLE              1
                LOAD_CONST              24 (<code object <genexpr> at 0x0000018C18025830, file "scripts/pas178_audit_window_chain_readiness_check.py", line 836>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 837            LOAD_CONST              42 (("'PASSED'", "'FAILED'", "'SKIPPED'", "'PARTIAL'"))
                GET_ITER

 836            CALL                     0
                CALL                     1
       L27:     STORE_FAST               8 (status_ok)

 839            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 840            LOAD_CONST              25 ('v27_sql:closed_status_enum')

 841            LOAD_FAST_BORROW         8 (status_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L28)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L29)
       L28:     LOAD_CONST               6 ('FAIL')

 842   L29:     LOAD_CONST              26 ('v27 SQL carries the closed status enum')

 843            LOAD_FAST_BORROW         8 (status_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L30)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L31)
       L30:     LOAD_CONST              27 ('missing one or more status literals')

 839   L31:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 847            LOAD_CONST              28 ('pas_audit_verification_runs_tenant_no_insert')
                LOAD_DEREF              11 (src)
                CONTAINS_OP              0 (in)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       45 (to L32)
                NOT_TAKEN
                POP_TOP

 848            LOAD_CONST              29 ('pas_audit_verification_runs_tenant_no_update')
                LOAD_DEREF              11 (src)
                CONTAINS_OP              0 (in)

 847            COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       32 (to L32)
                NOT_TAKEN
                POP_TOP

 849            LOAD_CONST              30 ('pas_audit_verification_runs_tenant_no_delete')
                LOAD_DEREF              11 (src)
                CONTAINS_OP              0 (in)

 847            COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L32)
                NOT_TAKEN
                POP_TOP

 850            LOAD_CONST              31 ('pas_audit_verification_runs_service_role_no_update')
                LOAD_DEREF              11 (src)
                CONTAINS_OP              0 (in)

 847            COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        6 (to L32)
                NOT_TAKEN
                POP_TOP

 851            LOAD_CONST              32 ('pas_audit_verification_runs_service_role_no_delete')
                LOAD_DEREF              11 (src)
                CONTAINS_OP              0 (in)

 846   L32:     STORE_FAST               9 (append_only_ok)

 853            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 854            LOAD_CONST              33 ('v27_sql:append_only_policies')

 855            LOAD_FAST_BORROW         9 (append_only_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L33)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L34)
       L33:     LOAD_CONST               6 ('FAIL')

 856   L34:     LOAD_CONST              34 ('v27 SQL denies tenant INSERT + tenant UPDATE/DELETE + service_role UPDATE/DELETE')

 857            LOAD_FAST_BORROW         9 (append_only_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L35)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L36)
       L35:     LOAD_CONST              35 ('missing one or more no-update/no-delete/no-insert policies')

 853   L36:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 861            LOAD_CONST              36 ('pas_audit_verification_runs_tenant_select')
                LOAD_DEREF              11 (src)
                CONTAINS_OP              0 (in)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        6 (to L37)
                NOT_TAKEN
                POP_TOP

 862            LOAD_CONST              37 ("brokerage_id = (auth.jwt() ->> 'brokerage_id')")
                LOAD_DEREF              11 (src)
                CONTAINS_OP              0 (in)

 860   L37:     STORE_FAST              10 (select_scoped)

 864            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 865            LOAD_CONST              38 ('v27_sql:tenant_select_scoped')

 866            LOAD_FAST_BORROW        10 (select_scoped)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L38)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L39)
       L38:     LOAD_CONST               6 ('FAIL')

 867   L39:     LOAD_CONST              39 ('v27 SQL scopes tenant SELECT to own brokerage_id')

 868            LOAD_FAST_BORROW        10 (select_scoped)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L40)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L41)
       L40:     LOAD_CONST              40 ('missing tenant SELECT policy with brokerage_id scope')

 864   L41:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 870            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18025A30, file "scripts/pas178_audit_window_chain_readiness_check.py", line 821>:
  --           COPY_FREE_VARS           1

 821           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 822   L2:     FOR_ITER                 9 (to L3)
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

Disassembly of <code object <genexpr> at 0x0000018C18025830, file "scripts/pas178_audit_window_chain_readiness_check.py", line 836>:
  --           COPY_FREE_VARS           1

 836           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 837   L2:     FOR_ITER                 9 (to L3)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "scripts/pas178_audit_window_chain_readiness_check.py", line 873>:
873           RESUME                   0
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

Disassembly of <code object check_event_contract at 0x0000018C1801CFB0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 873>:
873           RESUME                   0

874           BUILD_LIST               0
              STORE_FAST               1 (out)

875           LOAD_GLOBAL              1 (Path + NULL)
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

876           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

877           LOAD_GLOBAL              4 (REQUIRED_EVENT_TYPES)
              GET_ITER
      L2:     FOR_ITER                67 (to L7)
              STORE_FAST               4 (required)

878           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (required, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

879           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

880           LOAD_CONST               5 ('events:')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

881           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               6 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               7 ('FAIL')

882   L4:     LOAD_CONST               8 ('Event contract registers ')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

883           LOAD_FAST_BORROW         5 (ok)
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

879   L6:     LOAD_CONST              10 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           69 (to L2)

877   L7:     END_FOR
              POP_ITER

885           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "scripts/pas178_audit_window_chain_readiness_check.py", line 888>:
888           RESUME                   0
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

Disassembly of <code object check_no_forbidden_imports at 0x0000018C17F73990, file "scripts/pas178_audit_window_chain_readiness_check.py", line 888>:
888            RESUME                   0

889            BUILD_LIST               0
               STORE_FAST               1 (out)

890            LOAD_CONST              10 (('app/services/operator/audit_window_chain.py', 'app/services/operator/audit_verification_runs.py', 'app/services/tenant/tenant_audit_dashboard.py', 'scripts/verify_audit_window_chain.py', 'scripts/persist_audit_verification_run.py', 'scripts/pas178_audit_window_chain_readiness_check.py'))
               STORE_FAST               2 (files)

898            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     EXTENDED_ARG             1
               FOR_ITER               292 (to L15)
               STORE_FAST               3 (relpath)

899            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

900            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

901            JUMP_BACKWARD           46 (to L1)

902    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

903            BUILD_LIST               0
               STORE_FAST               6 (bad)

904            LOAD_FAST_BORROW         5 (src)
               LOAD_ATTR                7 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L4:     FOR_ITER               107 (to L10)
               STORE_FAST               7 (line)

905            LOAD_FAST_BORROW         7 (line)
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               STORE_FAST               8 (stripped)

906            LOAD_FAST_BORROW         8 (stripped)
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

907    L5:     JUMP_BACKWARD           52 (to L4)

908    L6:     LOAD_GLOBAL             12 (FORBIDDEN_IMPORT_LINE_PREFIXES)
               GET_ITER
       L7:     FOR_ITER                45 (to L9)
               STORE_FAST               9 (prefix)

909            LOAD_FAST_BORROW         8 (stripped)
               LOAD_ATTR               11 (startswith + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD           28 (to L7)

910    L8:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           47 (to L7)

908    L9:     END_FOR
               POP_ITER
               JUMP_BACKWARD          109 (to L4)

904   L10:     END_FOR
               POP_ITER

911            LOAD_FAST                1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             17 (_check + NULL)

912            LOAD_CONST               3 ('forbidden_import:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

913            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               4 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               5 ('PASS')

914   L12:     LOAD_CONST               6 ('No forbidden imports: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

916            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       43 (to L13)
               NOT_TAKEN

915            LOAD_CONST               7 ('forbidden import prefixes: ')
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

916   L13:     LOAD_CONST               1 ('')

911   L14:     LOAD_CONST               9 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          295 (to L1)

898   L15:     END_FOR
               POP_ITER

918            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "scripts/pas178_audit_window_chain_readiness_check.py", line 921>:
921           RESUME                   0
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

Disassembly of <code object check_no_inbox_scan_tokens at 0x0000018C17CC1CE0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 921>:
921            RESUME                   0

922            BUILD_LIST               0
               STORE_FAST               1 (out)

923            LOAD_CONST               9 (('app/services/operator/audit_window_chain.py', 'app/services/operator/audit_verification_runs.py', 'app/services/tenant/tenant_audit_dashboard.py', 'scripts/verify_audit_window_chain.py', 'scripts/persist_audit_verification_run.py', 'scripts/pas178_audit_window_chain_readiness_check.py'))
               STORE_FAST               2 (files)

931            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               195 (to L11)
               STORE_FAST               3 (relpath)

932            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

933            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

934            JUMP_BACKWARD           45 (to L1)

935    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

936            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         5 (src)
               CALL                     1
               STORE_FAST               6 (executable)

937            BUILD_LIST               0
               STORE_FAST               7 (bad)

938            LOAD_GLOBAL              8 (FORBIDDEN_INBOX_TOKENS)
               GET_ITER
       L4:     FOR_ITER                28 (to L6)
               STORE_FAST               8 (token)

939            LOAD_FAST_BORROW_LOAD_FAST_BORROW 134 (token, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L4)

940    L5:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_FAST_BORROW         8 (token)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L4)

938    L6:     END_FOR
               POP_ITER

941            LOAD_FAST                1 (out)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_GLOBAL             13 (_check + NULL)

942            LOAD_CONST               2 ('no_inbox_scan:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

943            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L7)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L8)
       L7:     LOAD_CONST               4 ('PASS')

944    L8:     LOAD_CONST               5 ('No inbox-scanning tokens: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

946            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L9)
               NOT_TAKEN

945            LOAD_CONST               6 ('inbox-scan tokens present: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               15 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L10)

946    L9:     LOAD_CONST               1 ('')

941   L10:     LOAD_CONST               8 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          197 (to L1)

931   L11:     END_FOR
               POP_ITER

948            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3F00, file "scripts/pas178_audit_window_chain_readiness_check.py", line 951>:
951           RESUME                   0
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

Disassembly of <code object check_doc_required_clauses at 0x0000018C17CD1ED0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 951>:
  --            MAKE_CELL                8 (lower)

 951            RESUME                   0

 952            BUILD_LIST               0
                STORE_FAST               1 (out)

 953            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('docs')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('pas178_audit_window_chain_and_dashboards.md')
                BINARY_OP               11 (/)
                STORE_FAST               2 (doc)

 954            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (doc)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L1:     STORE_FAST               3 (src)

 955            LOAD_FAST_BORROW         3 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_DEREF              8 (lower)

 956            LOAD_CONST              13 ((('purpose', ('purpose',)), ('cross-window', ('cross-window',)), ('chain-doctrine', ('cross-window chain doctrine', 'chain doctrine')), ('verification-run', ('verification-run persistence doctrine', 'verification run persistence', 'verification-run persistence')), ('tenant-dashboard', ('tenant audit dashboard doctrine', 'tenant audit dashboard')), ('append-only', ('append-only',)), ('no-autonomous', ('no autonomous', 'no-autonomous', 'no automatic remediation')), ('rollback', ('rollback',)), ('escalation', ('escalation',)), ('no-gmail', ('no gmail',)), ('limitations', ('limitation',)), ('not-built', ('intentionally not built', 'intentionally does not', 'deliberately not'))))
                STORE_FAST               4 (required_phrases)

 977            LOAD_FAST_BORROW         4 (required_phrases)
                GET_ITER
        L2:     FOR_ITER               141 (to L12)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   86 (name, phrases)

 978            LOAD_GLOBAL              6 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         8 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18025D30, file "scripts/pas178_audit_window_chain_readiness_check.py", line 978>)
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
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18025D30, file "scripts/pas178_audit_window_chain_readiness_check.py", line 978>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         6 (phrases)
                GET_ITER
                CALL                     0
                CALL                     1
        L7:     STORE_FAST               7 (present)

 979            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 980            LOAD_CONST               6 ('docs:phrase:')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 981            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               8 ('FAIL')

 982    L9:     LOAD_CONST               9 ('Doctrine doc carries clause: ')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 984            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L10)
                NOT_TAKEN

 983            LOAD_CONST              10 ('expected one of: ')
                LOAD_CONST              11 (' | ')
                LOAD_ATTR               13 (join + NULL|self)
                LOAD_FAST_BORROW         6 (phrases)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L11)

 984   L10:     LOAD_CONST               2 ('')

 979   L11:     LOAD_CONST              12 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          143 (to L2)

 977   L12:     END_FOR
                POP_ITER

 986            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18025D30, file "scripts/pas178_audit_window_chain_readiness_check.py", line 978>:
  --           COPY_FREE_VARS           1

 978           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2010, file "scripts/pas178_audit_window_chain_readiness_check.py", line 989>:
989           RESUME                   0
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

Disassembly of <code object check_self_no_env_or_db at 0x0000018C17D893A0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 989>:
 989            RESUME                   0

 990            BUILD_LIST               0
                STORE_FAST               1 (out)

 991            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_GLOBAL              2 (__file__)
                CALL                     1
                LOAD_ATTR                5 (resolve + NULL|self)
                CALL                     0
                STORE_FAST               2 (self_path)

 992            LOAD_GLOBAL              7 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (self_path)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               0 ('')
        L1:     STORE_FAST               3 (src)

 993            LOAD_GLOBAL              9 (_strip_python_comments_and_strings + NULL)
                LOAD_FAST_BORROW         3 (src)
                CALL                     1
                STORE_FAST               4 (executable)

 994            BUILD_LIST               0
                STORE_FAST               5 (bad)

 995            LOAD_FAST_BORROW         4 (executable)
                LOAD_ATTR               11 (splitlines + NULL|self)
                CALL                     0
                GET_ITER
        L2:     FOR_ITER               199 (to L9)
                STORE_FAST               6 (raw_line)

 996            LOAD_FAST_BORROW         6 (raw_line)
                LOAD_ATTR               13 (strip + NULL|self)
                CALL                     0
                STORE_FAST               7 (stripped)

 997            LOAD_FAST_BORROW         7 (stripped)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L3)
                NOT_TAKEN

 998            JUMP_BACKWARD           29 (to L2)

 999    L3:     LOAD_FAST_BORROW         7 (stripped)
                LOAD_ATTR               15 (startswith + NULL|self)
                LOAD_CONST              15 (('import dotenv', 'from dotenv'))
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L4)
                NOT_TAKEN

1000            LOAD_FAST_BORROW         5 (bad)
                LOAD_ATTR               17 (append + NULL|self)
                LOAD_CONST               1 ('dotenv import')
                CALL                     1
                POP_TOP

1001    L4:     LOAD_FAST_BORROW         7 (stripped)
                LOAD_ATTR               15 (startswith + NULL|self)
                LOAD_CONST              16 (('import supabase', 'from supabase'))
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L5)
                NOT_TAKEN

1002            LOAD_FAST_BORROW         5 (bad)
                LOAD_ATTR               17 (append + NULL|self)
                LOAD_CONST               2 ('supabase import')
                CALL                     1
                POP_TOP

1003    L5:     LOAD_CONST               3 ('load_dotenv()')
                LOAD_FAST_BORROW         7 (stripped)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       18 (to L6)
                NOT_TAKEN

1004            LOAD_FAST_BORROW         5 (bad)
                LOAD_ATTR               17 (append + NULL|self)
                LOAD_CONST               4 ('load_dotenv() call')
                CALL                     1
                POP_TOP

1005    L6:     LOAD_FAST_BORROW         7 (stripped)
                LOAD_ATTR               15 (startswith + NULL|self)
                LOAD_CONST              17 (('os.environ[', 'getenv('))
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L7)
                NOT_TAKEN

1006            LOAD_FAST_BORROW         5 (bad)
                LOAD_ATTR               17 (append + NULL|self)
                LOAD_CONST               5 ('environ read')
                CALL                     1
                POP_TOP

1007    L7:     LOAD_CONST               6 ('get_supabase')
                LOAD_FAST_BORROW         7 (stripped)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN
                JUMP_BACKWARD          182 (to L2)

1008    L8:     LOAD_FAST_BORROW         5 (bad)
                LOAD_ATTR               17 (append + NULL|self)
                LOAD_CONST               7 ('supabase client call')
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          201 (to L2)

 995    L9:     END_FOR
                POP_ITER

1009            LOAD_FAST                1 (out)
                LOAD_ATTR               17 (append + NULL|self)
                LOAD_GLOBAL             19 (_check + NULL)

1010            LOAD_CONST               8 ('self_check:no_env_or_db')

1011            LOAD_FAST_BORROW         5 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN
                LOAD_CONST               9 ('FAIL')
                JUMP_FORWARD             1 (to L11)
       L10:     LOAD_CONST              10 ('PASS')

1012   L11:     LOAD_CONST              11 ('PAS178 readiness checker never reads .env / touches DB')

1013            LOAD_FAST_BORROW         5 (bad)
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

1009   L13:     LOAD_CONST              14 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

1015            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "scripts/pas178_audit_window_chain_readiness_check.py", line 1022>:
1022           RESUME                   0
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

Disassembly of <code object _aggregate at 0x0000018C1800AA60, file "scripts/pas178_audit_window_chain_readiness_check.py", line 1022>:
1022            RESUME                   0

1024            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

1023            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2

1024    L2:     FOR_ITER                49 (to L7)
                STORE_FAST               1 (c)

1025            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

1024    L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L2)

1025    L4:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              2 (SEVERITY_BLOCK)
                COMPARE_OP              88 (bool(==))

1024    L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L2)
        L6:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L2)
        L7:     END_FOR
                POP_ITER

1023    L8:     STORE_FAST               2 (blockers)
                STORE_FAST               1 (c)

1028            LOAD_CONST               3 ('verdict')
                LOAD_FAST_BORROW         2 (blockers)
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L9)
                NOT_TAKEN
                LOAD_GLOBAL              4 (VERDICT_NOT_READY)
                JUMP_FORWARD             5 (to L10)
        L9:     LOAD_GLOBAL              6 (VERDICT_READY)

1029   L10:     LOAD_CONST               4 ('blockers')
                LOAD_FAST_BORROW         2 (blockers)

1030            LOAD_CONST               5 ('info')
                BUILD_LIST               0

1027            BUILD_MAP                3
                RETURN_VALUE

  --   L11:     SWAP                     2
                POP_TOP

1023            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L11 [2]
  L4 to L5 -> L11 [2]
  L6 to L8 -> L11 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA3000, file "scripts/pas178_audit_window_chain_readiness_check.py", line 1034>:
1034           RESUME                   0
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

Disassembly of <code object _operator_actions at 0x0000018C180488F0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 1034>:
1034           RESUME                   0

1035           BUILD_LIST               0
               STORE_FAST               1 (out)

1036           LOAD_FAST_BORROW         0 (checks)
               GET_ITER
       L1:     FOR_ITER               109 (to L5)
               STORE_FAST               2 (c)

1037           LOAD_FAST_BORROW         2 (c)
               LOAD_CONST               0 ('status')
               BINARY_OP               26 ([])
               LOAD_CONST               1 ('FAIL')
               COMPARE_OP             119 (bool(!=))
               POP_JUMP_IF_FALSE        3 (to L2)
               NOT_TAKEN

1038           JUMP_BACKWARD           19 (to L1)

1039   L2:     LOAD_FAST_BORROW         2 (c)
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

1040           LOAD_FAST                1 (out)
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

1036   L5:     END_FOR
               POP_ITER

1041           LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114030, file "scripts/pas178_audit_window_chain_readiness_check.py", line 1044>:
1044           RESUME                   0
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

Disassembly of <code object evaluate at 0x0000018C177C5D50, file "scripts/pas178_audit_window_chain_readiness_check.py", line 1044>:
1044           RESUME                   0

1045           BUILD_LIST               0
               STORE_FAST               1 (checks)

1046           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL              3 (check_files_present + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1047           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL              5 (check_prior_phases_intact + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1048           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL              7 (check_memory_review_intact + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1049           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL              9 (check_worker_off_by_default + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1050           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             11 (check_no_startup_worker + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1051           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             13 (check_chain_service + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1052           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             15 (check_runs_service + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1053           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             17 (check_dashboard_service + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1054           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             19 (check_tenant_routes + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1055           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             21 (check_operator_routes + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1056           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             23 (check_verify_script + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1057           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             25 (check_persist_script + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1058           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             27 (check_audit_service_invariant + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1059           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             29 (check_ack_store_invariant + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1060           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             31 (check_v26_sql + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1061           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             33 (check_v27_sql + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1062           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             35 (check_event_contract + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1063           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             37 (check_no_forbidden_imports + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1064           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             39 (check_no_inbox_scan_tokens + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1065           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             41 (check_doc_required_clauses + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1066           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             43 (check_self_no_env_or_db + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1068           LOAD_GLOBAL             45 (_aggregate + NULL)
               LOAD_FAST_BORROW         1 (checks)
               CALL                     1
               STORE_FAST               2 (agg)

1070           LOAD_CONST               0 ('phase')
               LOAD_CONST               1 ('PAS178')

1071           LOAD_CONST               2 ('generated_at')
               LOAD_GLOBAL             47 (_now_iso + NULL)
               CALL                     0

1072           LOAD_CONST               3 ('verdict')
               LOAD_FAST_BORROW         2 (agg)
               LOAD_CONST               3 ('verdict')
               BINARY_OP               26 ([])

1073           LOAD_CONST               4 ('ready')
               LOAD_FAST_BORROW         2 (agg)
               LOAD_CONST               3 ('verdict')
               BINARY_OP               26 ([])
               LOAD_GLOBAL             48 (VERDICT_READY)
               COMPARE_OP              72 (==)

1074           LOAD_CONST               5 ('blocker_count')
               LOAD_GLOBAL             51 (len + NULL)
               LOAD_FAST_BORROW         2 (agg)
               LOAD_CONST               6 ('blockers')
               BINARY_OP               26 ([])
               CALL                     1

1075           LOAD_CONST               7 ('info_count')
               LOAD_GLOBAL             51 (len + NULL)
               LOAD_FAST_BORROW         2 (agg)
               LOAD_CONST               8 ('info')
               BINARY_OP               26 ([])
               CALL                     1

1076           LOAD_CONST               9 ('check_count')
               LOAD_GLOBAL             51 (len + NULL)
               LOAD_FAST_BORROW         1 (checks)
               CALL                     1

1077           LOAD_CONST              10 ('pass_count')
               LOAD_GLOBAL             53 (sum + NULL)
               LOAD_CONST              11 (<code object <genexpr> at 0x0000018C180532D0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 1077>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         1 (checks)
               GET_ITER
               CALL                     0
               CALL                     1

1078           LOAD_CONST              12 ('fail_count')
               LOAD_GLOBAL             53 (sum + NULL)
               LOAD_CONST              13 (<code object <genexpr> at 0x0000018C18053E10, file "scripts/pas178_audit_window_chain_readiness_check.py", line 1078>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         1 (checks)
               GET_ITER
               CALL                     0
               CALL                     1

1079           LOAD_CONST              14 ('checks')
               LOAD_FAST_BORROW         1 (checks)

1080           LOAD_CONST              15 ('operator_actions')
               LOAD_GLOBAL             55 (_operator_actions + NULL)
               LOAD_FAST_BORROW         1 (checks)
               CALL                     1

1069           BUILD_MAP               11
               RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C180532D0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 1077>:
1077           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C18053E10, file "scripts/pas178_audit_window_chain_readiness_check.py", line 1078>:
1078           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C181156B0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 1087>:
1087           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C180FC030, file "scripts/pas178_audit_window_chain_readiness_check.py", line 1087>:
1087           RESUME                   0

1088           LOAD_GLOBAL              0 (argparse)
               LOAD_ATTR                2 (ArgumentParser)
               PUSH_NULL

1089           LOAD_CONST               0 ('pas178_audit_window_chain_readiness_check')

1091           LOAD_CONST               1 ('PAS178 — Evaluate cross-window audit chain + verification persistence + tenant dashboard surfaces. Read-only — never reads .env, never touches Supabase, never runs a migration.')

1088           LOAD_CONST               2 (('prog', 'description'))
               CALL_KW                  2
               STORE_FAST               0 (p)

1097           LOAD_FAST_BORROW         0 (p)
               LOAD_ATTR                5 (add_argument + NULL|self)
               LOAD_CONST               3 ('--repo-root')
               LOAD_GLOBAL              6 (_REPO_ROOT_DEFAULT)
               LOAD_CONST               4 (('default',))
               CALL_KW                  2
               POP_TOP

1098           LOAD_FAST_BORROW         0 (p)
               LOAD_ATTR                5 (add_argument + NULL|self)
               LOAD_CONST               5 ('--output')
               LOAD_GLOBAL              8 (REPORT_FILENAME)
               LOAD_CONST               4 (('default',))
               CALL_KW                  2
               POP_TOP

1099           LOAD_FAST_BORROW         0 (p)
               LOAD_ATTR                5 (add_argument + NULL|self)
               LOAD_CONST               6 ('--json')
               LOAD_CONST               7 ('store_true')
               LOAD_CONST               8 (('action',))
               CALL_KW                  2
               POP_TOP

1100           LOAD_FAST_BORROW         0 (p)
               LOAD_ATTR                5 (add_argument + NULL|self)
               LOAD_CONST               9 ('--summary-only')
               LOAD_CONST               7 ('store_true')
               LOAD_CONST               8 (('action',))
               CALL_KW                  2
               POP_TOP

1101           LOAD_FAST_BORROW         0 (p)
               LOAD_ATTR                5 (add_argument + NULL|self)
               LOAD_CONST              10 ('--strict')
               LOAD_CONST               7 ('store_true')
               LOAD_CONST               8 (('action',))
               CALL_KW                  2
               POP_TOP

1102           LOAD_FAST_BORROW         0 (p)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181157A0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 1105>:
1105           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C17D8E300, file "scripts/pas178_audit_window_chain_readiness_check.py", line 1105>:
1105           RESUME                   0

1106           LOAD_GLOBAL              1 (print + NULL)

1107           LOAD_CONST               0 ('[PAS178] verdict=')
               LOAD_FAST_BORROW         0 (report)
               LOAD_CONST               1 ('verdict')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               LOAD_CONST               2 (' blockers=')

1108           LOAD_FAST_BORROW         0 (report)
               LOAD_CONST               3 ('blocker_count')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               LOAD_CONST               4 (' info=')

1109           LOAD_FAST_BORROW         0 (report)
               LOAD_CONST               5 ('info_count')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               LOAD_CONST               6 (' checks=')

1110           LOAD_FAST_BORROW         0 (report)
               LOAD_CONST               7 ('check_count')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               LOAD_CONST               8 (' pass=')

1111           LOAD_FAST_BORROW         0 (report)
               LOAD_CONST               9 ('pass_count')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               LOAD_CONST              10 (' fail=')

1112           LOAD_FAST_BORROW         0 (report)
               LOAD_CONST              11 ('fail_count')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE

1107           BUILD_STRING            12

1106           CALL                     1
               POP_TOP

1114           LOAD_FAST_BORROW         0 (report)
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

1115           LOAD_FAST_BORROW         1 (actions)
               TO_BOOL
               POP_JUMP_IF_FALSE       93 (to L5)
               NOT_TAKEN

1116           LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST              13 ('[PAS178] operator actions:')
               CALL                     1
               POP_TOP

1117           LOAD_FAST_BORROW         1 (actions)
               LOAD_CONST              14 (slice(None, 25, None))
               BINARY_OP               26 ([])
               GET_ITER
       L2:     FOR_ITER                17 (to L3)
               STORE_FAST               2 (a)

1118           LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST              15 ('  - ')
               LOAD_FAST_BORROW         2 (a)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           19 (to L2)

1117   L3:     END_FOR
               POP_ITER

1119           LOAD_GLOBAL              5 (len + NULL)
               LOAD_FAST_BORROW         1 (actions)
               CALL                     1
               LOAD_SMALL_INT          25
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE       34 (to L4)
               NOT_TAKEN

1120           LOAD_GLOBAL              1 (print + NULL)
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

1119   L4:     LOAD_CONST              18 (None)
               RETURN_VALUE

1115   L5:     LOAD_CONST              18 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026430, file "scripts/pas178_audit_window_chain_readiness_check.py", line 1123>:
1123           RESUME                   0
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

Disassembly of <code object _write_report at 0x0000018C180FC3F0, file "scripts/pas178_audit_window_chain_readiness_check.py", line 1123>:
1123           RESUME                   0

1124           NOP

1125   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

1126           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

1127           LOAD_CONST               3 ('utf-8')

1125           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

1129           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

1130   L4:     LOAD_GLOBAL             11 (print + NULL)

1131           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

1132           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

1131           BUILD_STRING             4

1133           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

1130           LOAD_CONST               7 (('file',))
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

1129   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18115890, file "scripts/pas178_audit_window_chain_readiness_check.py", line 1137>:
1137           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17D87D80, file "scripts/pas178_audit_window_chain_readiness_check.py", line 1137>:
1137            RESUME                   0

1138            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

1139            NOP

1140    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

1144    L2:     LOAD_GLOBAL             10 (os)
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

1145            LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               21 (isdir + NULL|self)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L4)
                NOT_TAKEN

1146            LOAD_GLOBAL             23 (print + NULL)
                LOAD_CONST               2 ('error: --repo-root not a directory: ')
                LOAD_FAST                4 (repo_root)
                FORMAT_SIMPLE
                BUILD_STRING             2
                LOAD_GLOBAL             24 (sys)
                LOAD_ATTR               26 (stderr)
                LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

1147            LOAD_SMALL_INT           2
                RETURN_VALUE

1149    L4:     LOAD_GLOBAL             29 (evaluate + NULL)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                STORE_FAST               5 (report)

1151            LOAD_FAST                2 (args)
                LOAD_ATTR               30 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L5)
                NOT_TAKEN

1152            LOAD_GLOBAL             33 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               34 (output)
                LOAD_FAST                5 (report)
                CALL                     2
                POP_TOP

1154    L5:     LOAD_GLOBAL             37 (_print_summary + NULL)
                LOAD_FAST                5 (report)
                CALL                     1
                POP_TOP

1156            LOAD_FAST                2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L6)
                NOT_TAKEN

1157            LOAD_GLOBAL             23 (print + NULL)
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

1159    L6:     LOAD_FAST                5 (report)
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

1141            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L17)
                NOT_TAKEN
                STORE_FAST               3 (e)

1142    L9:     LOAD_FAST                3 (e)
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

1141   L17:     RERAISE                  0

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
