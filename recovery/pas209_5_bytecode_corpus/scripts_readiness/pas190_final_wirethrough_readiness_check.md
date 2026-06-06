# scripts_readiness/pas190_final_wirethrough_readiness_check

- **pyc:** `scripts\__pycache__\pas190_final_wirethrough_readiness_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/pas190_final_wirethrough_readiness_check.py`
- **co_filename (from bytecode):** `C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS190 — Final operational wire-through polish readiness gate.

Deterministic, non-mutating evaluator for "is PAS190 wired
correctly, additive-only, fail-open, and free of regressions
across the PAS160-PAS189 + PAS-SECURITY-01/02/03/04 doctrine?".

Walks the repo and verifies:

  * PAS190 surfaces exist (doc / readiness gate / new
    operator_policy_report service / test file).
  * Doctrine clauses present; no forbidden-feature tokens.
  * Per-row cache invalidation: required tokens in
    `fleet_status_cache.py` + `cache_invalidation.py`;
    no autonomous warming.
  * Outbound-dial breaker read-through in
    `app/services/outbound/dial.py`: required tokens
    + fail-open guard.
  * Daily-runner `--slack-webhook-url` + `--notify-on-*`
    flags: present; no webhook URL printing; no scheduler.
  * Tenant incident date filters in projection + route.
  * Dashboard pagination ergonomics anchors present.
  * Operator policy report service + 2 routes.
  * Event contract carries 5 PAS190 event types.
  * No Gmail / google-auth / IMAP / POP3 / Composio /
    TrustClaw / embedding / vector imports in any
    PAS190 surface.
  * Memory Review surface untouched.
  * Worker remains OFF by default.
  * PAS160-PAS189 + PAS-SECURITY-01/02/03/04 readiness
    scripts still on disk.

Read-only: never reads .env, never touches Supabase,
never executes a deploy / migration / network call.

Exit codes:
  0 — READY
  1 — NOT_READY (one or more BLOCK checks failed)
  2 — bad CLI args
```

## Imports

`List`, `Optional`, `Path`, `__future__`, `annotations`, `argparse`, `datetime`, `json`, `os`, `pathlib`, `sys`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_aggregate`, `_build_parser`, `_check`, `_now_iso`, `_operator_actions`, `_print_summary`, `_read_text`, `_strip_python_comments_and_strings`, `_write_report`, `check_cache_invariants`, `check_daily_runner_slack`, `check_dashboard_anchors_present`, `check_doc_no_forbidden_scope`, `check_doc_required_clauses`, `check_event_contract_has_pas190_types`, `check_memory_review_intact`, `check_outbound_dial_wirethrough`, `check_pas190_files_present`, `check_policy_module_read_only`, `check_policy_report_invariants`, `check_prior_phases_intact`, `check_self_no_env_or_db`, `check_service_no_forbidden_imports`, `check_tenant_filters`, `check_worker_off_by_default`, `evaluate`, `main`

## Env-key candidates

`BLOCK`, `FAIL`, `NOT_READY`, `PAS190`, `PASS`, `READY`

## String constants (redacted where noted)

- '\nPAS190 — Final operational wire-through polish readiness gate.\n\nDeterministic, non-mutating evaluator for "is PAS190 wired\ncorrectly, additive-only, fail-open, and free of regressions\nacross the PAS160-PAS189 + PAS-SECURITY-01/02/03/04 doctrine?".\n\nWalks the repo and verifies:\n\n  * PAS190 surfaces exist (doc / readiness gate / new\n    operator_policy_report service / test file).\n  * Doctrine clauses present; no forbidden-feature tokens.\n  * Per-row cache invalidation: required tokens in\n    `fleet_status_cache.py` + `cache_invalidation.py`;\n    no autonomous warming.\n  * Outbound-dial breaker read-through in\n    `app/services/outbound/dial.py`: required tokens\n    + fail-open guard.\n  * Daily-runner `--slack-webhook-url` + `--notify-on-*`\n    flags: present; no webhook URL printing; no scheduler.\n  * Tenant incident date filters in projection + route.\n  * Dashboard pagination ergonomics anchors present.\n  * Operator policy report service + 2 routes.\n  * Event contract carries 5 PAS190 event types.\n  * No Gmail / google-auth / IMAP / POP3 / Composio /\n    TrustClaw / embedding / vector imports in any\n    PAS190 surface.\n  * Memory Review surface untouched.\n  * Worker remains OFF by default.\n  * PAS160-PAS189 + PAS-SECURITY-01/02/03/04 readiness\n    scripts still on disk.\n\nRead-only: never reads .env, never touches Supabase,\nnever executes a deploy / migration / network call.\n\nExit codes:\n  0 — READY\n  1 — NOT_READY (one or more BLOCK checks failed)\n  2 — bad CLI args\n'
- 'utf-8'
- 'READY'
- 'NOT_READY'
- 'BLOCK'
- 'app/services/operator/operator_policy_report.py'
- 'app/services/operator/circuit_breaker_policy.py'
- 'app/services/operator/cache_invalidation.py'
- 'app/services/operator/fleet_status_cache.py'
- 'app/services/tenant/tenant_incident_projection.py'
- 'app/routes/tenant_incidents.py'
- 'app/services/outbound/dial.py'
- 'scripts/run_daily_ops_checklist_report.py'
- 'app/static/dashboard/index.html'
- 'app/routes/operator_fleet.py'
- 'app/services/events/contract.py'
- 'severity'
- 'detail'
- 'pas190_final_wirethrough_readiness_report.json'
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
- 'Required PAS190 artefact present: '
- 'missing'
- 'prior_phase:'
- 'Prior-phase readiness script intact: '
- 'missing — PAS190 must not delete'
- 'memory_review:'
- 'Memory Review file present: '
- 'Memory Review file deleted — PAS190 must not touch'
- 'app'
- 'services'
- 'ingestion'
- 'worker.py'
- '_ENV_FLAG_ENABLED_LITERAL = "true"'
- "_ENV_FLAG_ENABLED_LITERAL = 'true'"
- 'worker:off_by_default'
- 'Pending-call worker is OFF by default'
- 'missing strict enable-literal constant'
- 'doc:'
- ':clause:'
- ' carries clause: '
- 'missing any of: '
- 'doc_scope:'
- ' introduces no out-of-scope feature token'
- 'disqualifying: '
- 'service_imports:'
- ' contains no forbidden import'
- 'cache_inv:token:'
- 'cache_invalidation.py carries: '
- 'token missing'
- 'fleet_cache:token:'
- 'fleet_status_cache.py carries: '
- 'fleet_cache:no_autonomous_warming'
- 'fleet_status_cache.py contains no autonomous warming pattern'
- 'dial:token:'
- 'dial.py carries: '
- 'dial:pattern:'
- 'dial.py carries fail-open pattern: '
- 'pattern missing'
- 'dial:no_breaker_mutation_or_auto_trip'
- 'dial.py does NOT mutate breaker state and has no auto-trip'
- 'policy_module:read_only'
- 'circuit_breaker_policy.py remains read-only (no auto-trip)'
- 'daily_runner:token:'
- 'run_daily_ops_checklist_report.py carries: '
- 'daily_runner:no_webhook_url_print'
- 'run_daily_ops_checklist_report.py never prints the webhook URL and installs no scheduler'
- 'tenant_proj:token:'
- 'tenant_incident_projection.py carries: '
- 'tenant_route:token:'
- 'tenant_incidents.py carries: '
- 'dashboard:'
- 'Dashboard anchor present: '
- 'anchor missing'
- 'policy_report:token:'
- 'operator_policy_report.py carries: '
- 'fleet_route:token:'
- 'operator_fleet.py carries: '
- 'contract:event:'
- 'events/contract.py carries event_type literal: '
- 'literal missing — contract drift'
- 'dotenv import'
- 'supabase import'
- 'load_dotenv('
- 'load_dotenv() call'
- 'environ read'
- 'get_supabase'
- 'supabase client call'
- 'self_check:no_env_or_db_or_network'
- 'PAS190 readiness checker never reads .env / touches DB / hits network'
- 'checks'
- 'verdict'
- 'blockers'
- 'info'
- 'List[str]'
- ' — '
- 'see report'
- 'phase'
- 'PAS190'
- 'generated_at'
- 'ready'
- 'blocker_count'
- 'info_count'
- 'check_count'
- 'pass_count'
- 'fail_count'
- 'operator_actions'
- 'argparse.ArgumentParser'
- 🔒 '<REDACTED:high-entropy blob, len=40>'
- 'PAS190 — Final operational wire-through polish readiness gate. Read-only — never reads .env, never touches Supabase, never executes a deploy / migration.'
- '--repo-root'
- '--output'
- '--json'
- 'store_true'
- '--summary-only'
- '--strict'
- 'report'
- 'None'
- '[PAS190] verdict='
- ' blockers='
- ' info='
- ' checks='
- ' pass='
- ' fail='
- '[PAS190] operator actions:'
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

   1           LOAD_CONST               0 ('\nPAS190 — Final operational wire-through polish readiness gate.\n\nDeterministic, non-mutating evaluator for "is PAS190 wired\ncorrectly, additive-only, fail-open, and free of regressions\nacross the PAS160-PAS189 + PAS-SECURITY-01/02/03/04 doctrine?".\n\nWalks the repo and verifies:\n\n  * PAS190 surfaces exist (doc / readiness gate / new\n    operator_policy_report service / test file).\n  * Doctrine clauses present; no forbidden-feature tokens.\n  * Per-row cache invalidation: required tokens in\n    `fleet_status_cache.py` + `cache_invalidation.py`;\n    no autonomous warming.\n  * Outbound-dial breaker read-through in\n    `app/services/outbound/dial.py`: required tokens\n    + fail-open guard.\n  * Daily-runner `--slack-webhook-url` + `--notify-on-*`\n    flags: present; no webhook URL printing; no scheduler.\n  * Tenant incident date filters in projection + route.\n  * Dashboard pagination ergonomics anchors present.\n  * Operator policy report service + 2 routes.\n  * Event contract carries 5 PAS190 event types.\n  * No Gmail / google-auth / IMAP / POP3 / Composio /\n    TrustClaw / embedding / vector imports in any\n    PAS190 surface.\n  * Memory Review surface untouched.\n  * Worker remains OFF by default.\n  * PAS160-PAS189 + PAS-SECURITY-01/02/03/04 readiness\n    scripts still on disk.\n\nRead-only: never reads .env, never touches Supabase,\nnever executes a deploy / migration / network call.\n\nExit codes:\n  0 — READY\n  1 — NOT_READY (one or more BLOCK checks failed)\n  2 — bad CLI args\n')
               STORE_NAME               0 (__doc__)

  42           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  44           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  45           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (json)
               STORE_NAME               4 (json)

  46           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (os)
               STORE_NAME               5 (os)

  47           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (sys)
               STORE_NAME               6 (sys)

  48           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              7 (datetime)
               IMPORT_FROM              7 (datetime)
               STORE_NAME               7 (datetime)
               IMPORT_FROM              8 (timezone)
               STORE_NAME               8 (timezone)
               POP_TOP

  49           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Path',))
               IMPORT_NAME              9 (pathlib)
               IMPORT_FROM             10 (Path)
               STORE_NAME              10 (Path)
               POP_TOP

  50           LOAD_SMALL_INT           0
               LOAD_CONST               5 (('List', 'Optional'))
               IMPORT_NAME             11 (typing)
               IMPORT_FROM             12 (List)
               STORE_NAME              12 (List)
               IMPORT_FROM             13 (Optional)
               STORE_NAME              13 (Optional)
               POP_TOP

  53           LOAD_NAME                6 (sys)
               LOAD_ATTR               28 (stdout)
               LOAD_NAME                6 (sys)
               LOAD_ATTR               30 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              16 (_stream)

  54           NOP

  55   L2:     LOAD_NAME               16 (_stream)
               LOAD_ATTR               35 (reconfigure + NULL|self)
               LOAD_CONST               6 ('utf-8')
               LOAD_CONST               7 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  53   L4:     END_FOR
               POP_ITER

  60           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               41 (abspath + NULL|self)

  61           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               43 (join + NULL|self)
               LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               45 (dirname + NULL|self)
               LOAD_NAME               23 (__file__)
               CALL                     1
               LOAD_CONST               8 ('..')
               CALL                     2

  60           CALL                     1
               STORE_NAME              24 (_REPO_ROOT_DEFAULT)

  65           LOAD_CONST               9 ('READY')
               STORE_NAME              25 (VERDICT_READY)

  66           LOAD_CONST              10 ('NOT_READY')
               STORE_NAME              26 (VERDICT_NOT_READY)

  68           LOAD_CONST              11 ('BLOCK')
               STORE_NAME              27 (SEVERITY_BLOCK)

  75           LOAD_CONST              82 (('docs/pas190_final_wirethrough_pilot_rehearsal.md', 'scripts/pas190_final_wirethrough_readiness_check.py', 'app/services/operator/operator_policy_report.py', 'tests/mvp/test_pas190_final_wirethrough.py'))
               STORE_NAME              28 (PAS190_FILES)

  83           LOAD_CONST              83 (('scripts/pas160_mvp_sequence_check.py', 'scripts/pas161_lead_ingestion_readiness_check.py', 'scripts/pas162_pending_calls_readiness_check.py', 'scripts/pas163_candidate_pipeline_readiness_check.py', 'scripts/pas164_email_ingestion_readiness_check.py', 'scripts/pas165_email_auth_dedupe_readiness_check.py', 'scripts/pas166_email_dedupe_policy_readiness_check.py', 'scripts/pas167_email_secret_reaper_readiness_check.py', 'scripts/pas168_email_secret_rotation_readiness_check.py', 'scripts/pas169_crypto_roundtrip_check.py', 'scripts/pas169_launch_readiness_check.py', 'scripts/pas_launch_integrity_check.py', 'scripts/pas170_operator_survival_readiness_check.py', 'scripts/pas171_external_pilot_readiness_check.py', 'scripts/pas172_pilot_operations_readiness_check.py', 'scripts/pas173_brokerage_operator_readiness_check.py', 'scripts/pas174_operator_audit_readiness_check.py', 'scripts/pas175_audit_integrity_readiness_check.py', 'scripts/pas176_audit_chain_readiness_check.py', 'scripts/pas177_tenant_audit_verification_readiness_check.py', 'scripts/pas178_audit_window_chain_readiness_check.py', 'scripts/pas179_controlled_learning_readiness_check.py', 'scripts/pas180_learning_review_readiness_check.py', 'scripts/pas181_manual_test_harness_readiness_check.py', 'scripts/pas182_adaptive_memory_bridge_readiness_check.py', 'scripts/pas183_onboarding_product_readiness_check.py', 'scripts/pas184_pilot_experience_readiness_check.py', 'scripts/pas186_final_cutover_readiness_check.py', 'scripts/pas187_fleet_cutover_readiness_check.py', 'scripts/pas188_operational_scaling_readiness_check.py', 'scripts/pas189_operational_wirethrough_readiness_check.py', 'scripts/pas_security_01_hardening_readiness_check.py', 'scripts/pas_security_02_rate_limit_scanner_readiness_check.py', 'scripts/pas_security_03_admin_webhook_ci_readiness_check.py', 'scripts/pas_security_04_operator_reveal_https_readiness_check.py'))
               STORE_NAME              29 (PRIOR_PHASE_FILES)

 122           LOAD_CONST              84 (('app/services/memory/review.py', 'app/services/memory/review_stats.py', 'app/services/memory/review_export.py', 'app/services/memory/review_actors.py', 'app/services/memory/review_alerts.py', 'app/services/memory/operator_console.py'))
               STORE_NAME              30 (MEMORY_REVIEW_FILES)

 132           LOAD_CONST              85 ((('docs/pas190_final_wirethrough_pilot_rehearsal.md', (('purpose', ('purpose',)), ('relationship-to-pas189', ('relationship to pas189',)), ('final-wire-through-doctrine', ('final wire-through doctrine',)), ('breaker-read-through-doctrine', ('breaker read-through doctrine',)), ('fail-open-doctrine', ('fail-open doctrine',)), ('slack-notify-doctrine', ('slack notify doctrine',)), ('tenant-incident-filter-doctrine', ('tenant incident filter doctrine',)), ('operator-policy-report-doctrine', ('operator policy report doctrine',)), ('dashboard-pagination-doctrine', ('dashboard pagination doctrine',)), ('pilot-rehearsal-procedure', ('pilot rehearsal procedure',)), ('no-autonomous-remediation', ('no autonomous remediation',)), ('rollback-workflow', ('rollback workflow',)), ('remaining-limitations', ('remaining limitations',)), ('intentionally-does-not-build', ('intentionally does not build',)), ('no-gmail', ('no gmail',)), ('composio', ('composio',)))),))
               STORE_NAME              31 (DOC_REQUIRED_CLAUSES)

 154           LOAD_CONST              86 (('gmail oauth integration', 'composio integration', 'trustclaw', 'auto-approve memory', 'ai chat assistant enabled', 'embedding model', 'vector database', 'imap inbox scanner', 'pop3 inbox scanner', 'auto-trip enabled', 'autonomous trip'))
               STORE_NAME              32 (FORBIDDEN_DOC_TOKENS)

 169           LOAD_CONST              87 (('app/services/operator/circuit_breaker_policy.py', 'app/services/operator/cache_invalidation.py', 'app/services/operator/fleet_status_cache.py', 'app/services/operator/operator_policy_report.py', 'app/services/tenant/tenant_incident_projection.py', 'app/routes/tenant_incidents.py', 'app/services/outbound/dial.py'))
               STORE_NAME              33 (SERVICE_FILES)

 180           LOAD_CONST              88 (('from googleapiclient', 'import googleapiclient', 'from google.oauth2', 'import google.oauth2', 'from google_auth_oauthlib', 'import google_auth_oauthlib', 'from imaplib', 'import imaplib', 'from poplib', 'import poplib', 'from composio', 'import composio', 'from trustclaw', 'import trustclaw', 'from chromadb', 'import chromadb', 'from pinecone', 'import pinecone', 'from pgvector', 'import pgvector', 'from sentence_transformers', 'import sentence_transformers', 'from openai', 'import openai'))
               STORE_NAME              34 (FORBIDDEN_IMPORT_PREFIXES)

 209           LOAD_CONST              14 ('app/services/operator/cache_invalidation.py')
               STORE_NAME              35 (CACHE_INV_FILE)

 210           LOAD_CONST              89 (('def invalidate_fleet_status_row', 'def invalidate_fleet_status_rows', 'def invalidate_fleet_status_for_incident', 'def invalidate_fleet_status_for_cutover', 'def invalidate_fleet_status_for_breaker', 'fleet.cache.row_invalidated'))
               STORE_NAME              36 (CACHE_INV_REQUIRED_TOKENS)

 219           LOAD_CONST              15 ('app/services/operator/fleet_status_cache.py')
               STORE_NAME              37 (FLEET_CACHE_FILE)

 220           LOAD_CONST              90 (('def invalidate_for_brokerage', 'ids_marker', '_TTL_DEFAULT'))
               STORE_NAME              38 (FLEET_CACHE_REQUIRED_TOKENS)

 225           LOAD_CONST              91 (('threading.Timer(', 'Thread(target=', 'apscheduler.schedulers', 'while True:', 'asyncio.create_task('))
               STORE_NAME              39 (FLEET_CACHE_FORBIDDEN_TOKENS)

 235           LOAD_CONST              18 ('app/services/outbound/dial.py')
               STORE_NAME              40 (DIAL_FILE)

 236           LOAD_CONST              92 (('should_block_new_outbound_for_brokerage', 'brokerage_circuit_breaker_tripped', 'circuit_breaker.outbound_dial_blocked', '# Fail-open:'))
               STORE_NAME              41 (DIAL_REQUIRED_TOKENS)

 242           LOAD_CONST              93 (('except Exception:',))
               STORE_NAME              42 (DIAL_REQUIRED_PATTERNS)

 245           LOAD_CONST              94 (('trip_breaker(', 'reset_breaker(', 'def auto_trip', 'threading.Timer('))
               STORE_NAME              43 (DIAL_FORBIDDEN_TOKENS)

 254           LOAD_CONST              13 ('app/services/operator/circuit_breaker_policy.py')
               STORE_NAME              44 (POLICY_FILE)

 255           LOAD_CONST              95 (('def trip_breaker', 'def reset_breaker', 'def auto_trip', 'threading.Timer(', 'Thread(target='))
               STORE_NAME              45 (POLICY_FORBIDDEN_TOKENS)

 265           LOAD_CONST              19 ('scripts/run_daily_ops_checklist_report.py')
               STORE_NAME              46 (DAILY_RUNNER_FILE)

 266           LOAD_CONST              96 (('--slack-webhook-url', '--notify-on-failure', '--notify-on-warning', 'def _slack_notify', 'def _maybe_notify', '[PAS190-notify]', '--watch', '--max-runs', 'KeyboardInterrupt'))
               STORE_NAME              47 (DAILY_RUNNER_REQUIRED_TOKENS)

 280           LOAD_CONST              97 (('print(args.slack_webhook_url', 'print(webhook_url', 'print(f"slack_webhook_url={', "print(f'slack_webhook_url={", 'apscheduler.schedulers', 'from celery', 'import celery', 'schedule.every(', 'crontab.write', 'os.fork('))
               STORE_NAME              48 (DAILY_RUNNER_FORBIDDEN_TOKENS)

 295           LOAD_CONST              16 ('app/services/tenant/tenant_incident_projection.py')
               STORE_NAME              49 (TENANT_PROJ_FILE)

 296           LOAD_CONST              98 (('_safe_iso_date', 'date_from', 'date_to', 'offset', 'filter_count', 'gte("opened_at"', 'lte("opened_at"'))
               STORE_NAME              50 (TENANT_PROJ_REQUIRED_TOKENS)

 308           LOAD_CONST              17 ('app/routes/tenant_incidents.py')
               STORE_NAME              51 (TENANT_ROUTE_FILE)

 309           LOAD_CONST              99 (('date_from:', 'date_to:', 'offset:', 'tenant.incident.filtered_viewed'))
               STORE_NAME              52 (TENANT_ROUTE_REQUIRED_TOKENS)

 318           LOAD_CONST              20 ('app/static/dashboard/index.html')
               STORE_NAME              53 (DASHBOARD_FILE)

 319           LOAD_CONST             100 ((('pas190:pagination-page-counter', 'showing '), ('pas190:pagination-disabled-attr', 'disabled aria-disabled'), ('pas190:pagination-end-of-fleet', 'End of fleet'), ('pas190:pagination-cap-message', 'Pagination cap reached'), ('pas189:fleet-state', 'pas189FleetState'), ('pas189:fleet-fetch-page', '_pas189FleetFetchPage'), ('pas189:fleet-load-more', '_pas189FleetLoadMore'), ('pas185a:snapshot-container', 'aPilotOpsContent'), ('pas185a:learning-container', 'aIntelLearning'), ('pas188:fleet-container', 'aFleetStatusContent'), ('design02:skip-link', 'skip-link'), ('design02:reduced-motion', 'prefers-reduced-motion'), ('design02:dvh', '100dvh')))
               STORE_NAME              54 (DASHBOARD_REQUIRED_ANCHORS)

 339           LOAD_CONST              12 ('app/services/operator/operator_policy_report.py')
               STORE_NAME              55 (POLICY_REPORT_FILE)

 340           LOAD_CONST             101 (('def operator_policy_report', 'def brokerage_policy_report', 'def fleet_policy_exception_report', '_SECTION_BREAKER', '_SECTION_DAILY_CHECKLIST', '_SECTION_MIGRATION', '_SECTION_INCIDENT', '_SECTION_CUTOVER', '_SECTION_SECURITY', '_SECTION_LEARNING'))
               STORE_NAME              56 (POLICY_REPORT_REQUIRED_TOKENS)

 355           LOAD_CONST              21 ('app/routes/operator_fleet.py')
               STORE_NAME              57 (FLEET_ROUTE_FILE)

 356           LOAD_CONST             102 (('@router.get("/fleet/policy-report")', '@router.get("/fleet/policy-report/{brokerage_id}")', 'operator.policy_report.generated'))
               STORE_NAME              58 (FLEET_ROUTE_REQUIRED_TOKENS)

 364           LOAD_CONST              22 ('app/services/events/contract.py')
               STORE_NAME              59 (EVENT_CONTRACT_FILE)

 365           LOAD_CONST             103 (('"circuit_breaker.outbound_dial_blocked"', '"fleet.cache.row_invalidated"', '"daily_ops.runner.slack_notify_attempted"', '"tenant.incident.filtered_viewed"', '"operator.policy_report.generated"'))
               STORE_NAME              60 (EVENT_CONTRACT_REQUIRED_EVENT_TYPES)

 378           LOAD_CONST              23 ('severity')
               LOAD_NAME               27 (SEVERITY_BLOCK)
               LOAD_CONST              24 ('detail')
               LOAD_CONST              25 ('')
               BUILD_MAP                2
               LOAD_CONST              26 (<code object __annotate__ at 0x0000018C18024C30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 378>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object _check at 0x0000018C17FA3A50, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 378>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              61 (_check)

 388           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA31E0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 388>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object _now_iso at 0x0000018C18038170, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 388>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              62 (_now_iso)

 392           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA3E10, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 392>)
               MAKE_FUNCTION
               LOAD_CONST              31 (<code object _read_text at 0x0000018C18053870, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 392>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              63 (_read_text)

 399           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA3960, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 399>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object _strip_python_comments_and_strings at 0x0000018C17E921E0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 399>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              64 (_strip_python_comments_and_strings)

 438           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA3C30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 438>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object check_pas190_files_present at 0x0000018C18060F60, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 438>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              65 (check_pas190_files_present)

 451           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C17FA3690, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 451>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object check_prior_phases_intact at 0x0000018C180606F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 451>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              66 (check_prior_phases_intact)

 464           LOAD_CONST              38 (<code object __annotate__ at 0x0000018C17FA30F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 464>)
               MAKE_FUNCTION
               LOAD_CONST              39 (<code object check_memory_review_intact at 0x0000018C18061110, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 464>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              67 (check_memory_review_intact)

 477           LOAD_CONST              40 (<code object __annotate__ at 0x0000018C17FA3F00, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 477>)
               MAKE_FUNCTION
               LOAD_CONST              41 (<code object check_worker_off_by_default at 0x0000018C1794EBB0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 477>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              68 (check_worker_off_by_default)

 492           LOAD_CONST              42 (<code object __annotate__ at 0x0000018C17FA2010, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 492>)
               MAKE_FUNCTION
               LOAD_CONST              43 (<code object check_doc_required_clauses at 0x0000018C17D8AAB0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 492>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              69 (check_doc_required_clauses)

 509           LOAD_CONST              44 (<code object __annotate__ at 0x0000018C17FA3000, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 509>)
               MAKE_FUNCTION
               LOAD_CONST              45 (<code object check_doc_no_forbidden_scope at 0x0000018C17ECE220, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 509>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              70 (check_doc_no_forbidden_scope)

 524           LOAD_CONST              46 (<code object __annotate__ at 0x0000018C18114120, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 524>)
               MAKE_FUNCTION
               LOAD_CONST              47 (<code object check_service_no_forbidden_imports at 0x0000018C17F78CB0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 524>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              71 (check_service_no_forbidden_imports)

 546           LOAD_CONST              48 (<code object __annotate__ at 0x0000018C18114210, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 546>)
               MAKE_FUNCTION
               LOAD_CONST              49 (<code object check_cache_invariants at 0x0000018C17E939D0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 546>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              72 (check_cache_invariants)

 575           LOAD_CONST              50 (<code object __annotate__ at 0x0000018C18114300, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 575>)
               MAKE_FUNCTION
               LOAD_CONST              51 (<code object check_outbound_dial_wirethrough at 0x0000018C17F74010, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 575>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              73 (check_outbound_dial_wirethrough)

 603           LOAD_CONST              52 (<code object __annotate__ at 0x0000018C181143F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 603>)
               MAKE_FUNCTION
               LOAD_CONST              53 (<code object check_policy_module_read_only at 0x0000018C17EC4280, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 603>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              74 (check_policy_module_read_only)

 617           LOAD_CONST              54 (<code object __annotate__ at 0x0000018C181144E0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 617>)
               MAKE_FUNCTION
               LOAD_CONST              55 (<code object check_daily_runner_slack at 0x0000018C17D8A570, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 617>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              75 (check_daily_runner_slack)

 639           LOAD_CONST              56 (<code object __annotate__ at 0x0000018C181146C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 639>)
               MAKE_FUNCTION
               LOAD_CONST              57 (<code object check_tenant_filters at 0x0000018C17D86020, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 639>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              76 (check_tenant_filters)

 660           LOAD_CONST              58 (<code object __annotate__ at 0x0000018C181147B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 660>)
               MAKE_FUNCTION
               LOAD_CONST              59 (<code object check_dashboard_anchors_present at 0x0000018C1794E810, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 660>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              77 (check_dashboard_anchors_present)

 674           LOAD_CONST              60 (<code object __annotate__ at 0x0000018C181148A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 674>)
               MAKE_FUNCTION
               LOAD_CONST              61 (<code object check_policy_report_invariants at 0x0000018C17D872F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 674>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              78 (check_policy_report_invariants)

 695           LOAD_CONST              62 (<code object __annotate__ at 0x0000018C18114990, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 695>)
               MAKE_FUNCTION
               LOAD_CONST              63 (<code object check_event_contract_has_pas190_types at 0x0000018C18048C70, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 695>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              79 (check_event_contract_has_pas190_types)

 709           LOAD_CONST              64 (<code object __annotate__ at 0x0000018C18114A80, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 709>)
               MAKE_FUNCTION
               LOAD_CONST              65 (<code object check_self_no_env_or_db at 0x0000018C17EA4870, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 709>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              80 (check_self_no_env_or_db)

 755           LOAD_CONST              66 (<code object __annotate__ at 0x0000018C18114B70, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 755>)
               MAKE_FUNCTION
               LOAD_CONST              67 (<code object _aggregate at 0x0000018C1800B0A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 755>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              81 (_aggregate)

 764           LOAD_CONST              68 (<code object __annotate__ at 0x0000018C18114C60, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 764>)
               MAKE_FUNCTION
               LOAD_CONST              69 (<code object _operator_actions at 0x0000018C18048730, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 764>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              82 (_operator_actions)

 774           LOAD_CONST              70 (<code object __annotate__ at 0x0000018C18114D50, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 774>)
               MAKE_FUNCTION
               LOAD_CONST              71 (<code object evaluate at 0x0000018C17ED9FB0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 774>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              83 (evaluate)

 809           LOAD_CONST              72 ('pas190_final_wirethrough_readiness_report.json')
               STORE_NAME              84 (REPORT_FILENAME)

 812           LOAD_CONST              73 (<code object __annotate__ at 0x0000018C18114F30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 812>)
               MAKE_FUNCTION
               LOAD_CONST              74 (<code object _build_parser at 0x0000018C18128030, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 812>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              85 (_build_parser)

 830           LOAD_CONST              75 (<code object __annotate__ at 0x0000018C18115020, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 830>)
               MAKE_FUNCTION
               LOAD_CONST              76 (<code object _print_summary at 0x0000018C17D8D460, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 830>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              86 (_print_summary)

 848           LOAD_CONST              77 (<code object __annotate__ at 0x0000018C18024F30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 848>)
               MAKE_FUNCTION
               LOAD_CONST              78 (<code object _write_report at 0x0000018C18128210, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 848>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              87 (_write_report)

 862           LOAD_CONST             104 ((None,))
               LOAD_CONST              79 (<code object __annotate__ at 0x0000018C18114030, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 862>)
               MAKE_FUNCTION
               LOAD_CONST              80 (<code object main at 0x0000018C17D88890, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 862>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              88 (main)

 887           LOAD_NAME               89 (__name__)
               LOAD_CONST              81 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 888           LOAD_NAME                6 (sys)
               LOAD_ATTR              180 (exit)
               PUSH_NULL
               LOAD_NAME               88 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 887   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  56           LOAD_NAME               18 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  57   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          393 (to L1)

  56   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 378>:
378           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('check_id')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('status')
              LOAD_CONST               2 ('str')
              LOAD_CONST               4 ('label')
              LOAD_CONST               2 ('str')
              LOAD_CONST               5 ('severity')
              LOAD_CONST               2 ('str')
              LOAD_CONST               6 ('detail')
              LOAD_CONST               2 ('str')
              LOAD_CONST               7 ('return')
              LOAD_CONST               8 ('dict')
              BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _check at 0x0000018C17FA3A50, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 378>:
378           RESUME                   0

380           LOAD_CONST               0 ('id')
              LOAD_FAST_BORROW         0 (check_id)

381           LOAD_CONST               1 ('status')
              LOAD_FAST_BORROW         1 (status)

382           LOAD_CONST               2 ('label')
              LOAD_FAST_BORROW         2 (label)

383           LOAD_CONST               3 ('severity')
              LOAD_FAST_BORROW         3 (severity)

384           LOAD_CONST               4 ('detail')
              LOAD_FAST_BORROW         4 (detail)

379           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 388>:
388           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038170, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 388>:
388           RESUME                   0

389           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 392>:
392           RESUME                   0
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

Disassembly of <code object _read_text at 0x0000018C18053870, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 392>:
 392           RESUME                   0

 393           NOP

 394   L1:     LOAD_FAST_BORROW         0 (path)
               LOAD_ATTR                1 (read_text + NULL|self)
               LOAD_CONST               0 ('utf-8')
               LOAD_CONST               1 ('replace')
               LOAD_CONST               2 (('encoding', 'errors'))
               CALL_KW                  2
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 395           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 396   L4:     POP_EXCEPT
               LOAD_CONST               3 (None)
               RETURN_VALUE

 395   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 399>:
399           RESUME                   0
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

Disassembly of <code object _strip_python_comments_and_strings at 0x0000018C17E921E0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 399>:
399            RESUME                   0

400            BUILD_LIST               0
               STORE_FAST               1 (out)

401            LOAD_SMALL_INT           0
               LOAD_GLOBAL              1 (len + NULL)
               LOAD_FAST_BORROW         0 (src)
               CALL                     1
               STORE_FAST_STORE_FAST   50 (n, i)

402    L1:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (i, n)
               COMPARE_OP              18 (bool(<))
               EXTENDED_ARG             1
               POP_JUMP_IF_FALSE      282 (to L13)
               NOT_TAKEN

403            LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               BINARY_OP               26 ([])
               STORE_FAST               4 (ch)

404            LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               1 ('#')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       38 (to L3)
               NOT_TAKEN

405            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_CONST               2 ('\n')
               LOAD_FAST_BORROW         2 (i)
               CALL                     2
               STORE_FAST               5 (j)

406            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L2)
               NOT_TAKEN

407            JUMP_FORWARD           240 (to L13)

408    L2:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

409            JUMP_BACKWARD           59 (to L1)

410    L3:     LOAD_FAST_BORROW         0 (src)
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

411    L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               BINARY_SLICE
               STORE_FAST               6 (quote)

412            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 98 (quote, i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               CALL                     2
               STORE_FAST               7 (end)

413            LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L5)
               NOT_TAKEN

414            JUMP_FORWARD           138 (to L13)

415    L5:     LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

416            JUMP_BACKWARD          161 (to L1)

417    L6:     LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               7 (('"', "'"))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       92 (to L12)
               NOT_TAKEN

418            LOAD_FAST                4 (ch)
               STORE_FAST               6 (quote)

419            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               5 (j)

420    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (j, n)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       63 (to L11)
               NOT_TAKEN

421            LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
               BINARY_OP               26 ([])
               LOAD_CONST               5 ('\\')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       12 (to L8)
               NOT_TAKEN

422            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           2
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)

423            JUMP_BACKWARD           30 (to L7)

424    L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
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

425    L9:     JUMP_FORWARD            11 (to L11)

426   L10:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)
               JUMP_BACKWARD           68 (to L7)

427   L11:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

428            EXTENDED_ARG             1
               JUMP_BACKWARD          259 (to L1)

429   L12:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (ch)
               CALL                     1
               POP_TOP

430            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               2 (i)
               EXTENDED_ARG             1
               JUMP_BACKWARD          288 (to L1)

431   L13:     LOAD_CONST               6 ('')
               LOAD_ATTR                9 (join + NULL|self)
               LOAD_FAST_BORROW         1 (out)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 438>:
438           RESUME                   0
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

Disassembly of <code object check_pas190_files_present at 0x0000018C18060F60, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 438>:
438           RESUME                   0

439           BUILD_LIST               0
              STORE_FAST               1 (out)

440           LOAD_GLOBAL              0 (PAS190_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

441           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

442           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

443           LOAD_CONST               0 ('file:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

444           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

445   L3:     LOAD_CONST               3 ('Required PAS190 artefact present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

446           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing')

442   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

440   L6:     END_FOR
              POP_ITER

448           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 451>:
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

Disassembly of <code object check_prior_phases_intact at 0x0000018C180606F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 451>:
451           RESUME                   0

452           BUILD_LIST               0
              STORE_FAST               1 (out)

453           LOAD_GLOBAL              0 (PRIOR_PHASE_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

454           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

455           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

456           LOAD_CONST               0 ('prior_phase:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

457           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

458   L3:     LOAD_CONST               3 ('Prior-phase readiness script intact: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

459           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing — PAS190 must not delete')

455   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

453   L6:     END_FOR
              POP_ITER

461           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA30F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 464>:
464           RESUME                   0
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

Disassembly of <code object check_memory_review_intact at 0x0000018C18061110, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 464>:
464           RESUME                   0

465           BUILD_LIST               0
              STORE_FAST               1 (out)

466           LOAD_GLOBAL              0 (MEMORY_REVIEW_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

467           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

468           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

469           LOAD_CONST               0 ('memory_review:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

470           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

471   L3:     LOAD_CONST               3 ('Memory Review file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

472           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('Memory Review file deleted — PAS190 must not touch')

468   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

466   L6:     END_FOR
              POP_ITER

474           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3F00, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 477>:
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

Disassembly of <code object check_worker_off_by_default at 0x0000018C1794EBB0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 477>:
477           RESUME                   0

478           LOAD_GLOBAL              1 (Path + NULL)
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
              STORE_FAST               1 (p)

479           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         1 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               2 (src)

481           LOAD_CONST               5 ('_ENV_FLAG_ENABLED_LITERAL = "true"')
              LOAD_FAST_BORROW         2 (src)
              CONTAINS_OP              0 (in)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         6 (to L2)
              NOT_TAKEN
              POP_TOP

482           LOAD_CONST               6 ("_ENV_FLAG_ENABLED_LITERAL = 'true'")
              LOAD_FAST_BORROW         2 (src)
              CONTAINS_OP              0 (in)

480   L2:     STORE_FAST               3 (ok)

484           LOAD_GLOBAL              5 (_check + NULL)

485           LOAD_CONST               7 ('worker:off_by_default')

486           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               8 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               9 ('FAIL')

487   L4:     LOAD_CONST              10 ('Pending-call worker is OFF by default')

488           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        9 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')

484           LOAD_CONST              12 (('detail',))
              CALL_KW                  4
              BUILD_LIST               1
              RETURN_VALUE

488   L5:     LOAD_CONST              11 ('missing strict enable-literal constant')

484           LOAD_CONST              12 (('detail',))
              CALL_KW                  4
              BUILD_LIST               1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2010, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 492>:
492           RESUME                   0
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

Disassembly of <code object check_doc_required_clauses at 0x0000018C17D8AAB0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 492>:
  --            MAKE_CELL                9 (lower)

 492            RESUME                   0

 493            BUILD_LIST               0
                STORE_FAST               1 (out)

 494            LOAD_GLOBAL              0 (DOC_REQUIRED_CLAUSES)
                GET_ITER
        L1:     FOR_ITER               208 (to L14)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   35 (relpath, clauses)

 495            LOAD_GLOBAL              3 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_FAST_BORROW         2 (relpath)
                BINARY_OP               11 (/)
                STORE_FAST               4 (fp)

 496            LOAD_GLOBAL              5 (_read_text + NULL)
                LOAD_FAST_BORROW         4 (fp)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L2)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               0 ('')
        L2:     STORE_FAST               5 (src)

 497            LOAD_FAST_BORROW         5 (src)
                LOAD_ATTR                7 (lower + NULL|self)
                CALL                     0
                STORE_DEREF              9 (lower)

 498            LOAD_FAST_BORROW         3 (clauses)
                GET_ITER
        L3:     FOR_ITER               142 (to L13)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST  103 (name, phrases)

 499            LOAD_GLOBAL              8 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L7)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         9 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               1 (<code object <genexpr> at 0x0000018C18026630, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 499>)
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
                LOAD_CONST               1 (<code object <genexpr> at 0x0000018C18026630, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 499>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         7 (phrases)
                GET_ITER
                CALL                     0
                CALL                     1
        L8:     STORE_FAST               8 (present)

 500            LOAD_FAST                1 (out)
                LOAD_ATTR               11 (append + NULL|self)
                LOAD_GLOBAL             13 (_check + NULL)

 501            LOAD_CONST               4 ('doc:')
                LOAD_FAST_BORROW         2 (relpath)
                FORMAT_SIMPLE
                LOAD_CONST               5 (':clause:')
                LOAD_FAST_BORROW         6 (name)
                FORMAT_SIMPLE
                BUILD_STRING             4

 502            LOAD_FAST_BORROW         8 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L9)
                NOT_TAKEN
                LOAD_CONST               6 ('PASS')
                JUMP_FORWARD             1 (to L10)
        L9:     LOAD_CONST               7 ('FAIL')

 503   L10:     LOAD_FAST_BORROW         2 (relpath)
                FORMAT_SIMPLE
                LOAD_CONST               8 (' carries clause: ')
                LOAD_FAST_BORROW         6 (name)
                FORMAT_SIMPLE
                BUILD_STRING             3

 504            LOAD_FAST_BORROW         8 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L11)
                NOT_TAKEN
                LOAD_CONST               0 ('')
                JUMP_FORWARD            19 (to L12)
       L11:     LOAD_CONST               9 ('missing any of: ')
                LOAD_CONST              10 (', ')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_FAST_BORROW         7 (phrases)
                CALL                     1
                FORMAT_SIMPLE
                BUILD_STRING             2

 500   L12:     LOAD_CONST              11 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          144 (to L3)

 498   L13:     END_FOR
                POP_ITER
                JUMP_BACKWARD          210 (to L1)

 494   L14:     END_FOR
                POP_ITER

 506            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18026630, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 499>:
  --           COPY_FREE_VARS           1

 499           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3000, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 509>:
509           RESUME                   0
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

Disassembly of <code object check_doc_no_forbidden_scope at 0x0000018C17ECE220, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 509>:
 509            RESUME                   0

 510            BUILD_LIST               0
                STORE_FAST               1 (out)

 511            LOAD_GLOBAL              0 (DOC_REQUIRED_CLAUSES)
                GET_ITER
        L1:     FOR_ITER               165 (to L13)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   35 (relpath, _)

 512            LOAD_GLOBAL              3 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_FAST_BORROW         2 (relpath)
                BINARY_OP               11 (/)
                STORE_FAST               4 (fp)

 513            LOAD_GLOBAL              5 (_read_text + NULL)
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

 514            LOAD_GLOBAL              8 (FORBIDDEN_DOC_TOKENS)
                GET_ITER
                LOAD_FAST_AND_CLEAR      6 (t)
                SWAP                     2
        L3:     BUILD_LIST               0
                SWAP                     2
        L4:     FOR_ITER                13 (to L7)
                STORE_FAST_LOAD_FAST   102 (t, t)
                LOAD_FAST_BORROW         5 (src)
                CONTAINS_OP              0 (in)
        L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L4)
        L6:     LOAD_FAST_BORROW         6 (t)
                LIST_APPEND              2
                JUMP_BACKWARD           15 (to L4)
        L7:     END_FOR
                POP_ITER
        L8:     STORE_FAST               7 (bad)
                STORE_FAST               6 (t)

 515            LOAD_FAST                1 (out)
                LOAD_ATTR               11 (append + NULL|self)
                LOAD_GLOBAL             13 (_check + NULL)

 516            LOAD_CONST               1 ('doc_scope:')
                LOAD_FAST_BORROW         2 (relpath)
                FORMAT_SIMPLE
                BUILD_STRING             2

 517            LOAD_FAST_BORROW         7 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L9)
                NOT_TAKEN
                LOAD_CONST               2 ('FAIL')
                JUMP_FORWARD             1 (to L10)
        L9:     LOAD_CONST               3 ('PASS')

 518   L10:     LOAD_FAST_BORROW         2 (relpath)
                FORMAT_SIMPLE
                LOAD_CONST               4 (' introduces no out-of-scope feature token')
                BUILD_STRING             2

 519            LOAD_FAST_BORROW         7 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L11)
                NOT_TAKEN
                LOAD_CONST               5 ('disqualifying: ')
                LOAD_CONST               6 (', ')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_FAST_BORROW         7 (bad)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L12)
       L11:     LOAD_CONST               0 ('')

 515   L12:     LOAD_CONST               7 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          167 (to L1)

 511   L13:     END_FOR
                POP_ITER

 521            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L14:     SWAP                     2
                POP_TOP

 514            SWAP                     2
                STORE_FAST               6 (t)
                RERAISE                  0
ExceptionTable:
  L3 to L5 -> L14 [3]
  L6 to L8 -> L14 [3]

Disassembly of <code object __annotate__ at 0x0000018C18114120, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 524>:
524           RESUME                   0
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

Disassembly of <code object check_service_no_forbidden_imports at 0x0000018C17F78CB0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 524>:
524            RESUME                   0

525            BUILD_LIST               0
               STORE_FAST               1 (out)

526            LOAD_GLOBAL              0 (SERVICE_FILES)
               GET_ITER
       L1:     FOR_ITER               228 (to L12)
               STORE_FAST               2 (relpath)

527            LOAD_GLOBAL              3 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         2 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               3 (fp)

528            LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         3 (fp)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L2:     STORE_FAST               4 (src)

529            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         4 (src)
               CALL                     1
               STORE_FAST               5 (executable)

530            BUILD_LIST               0
               STORE_FAST               6 (bad)

531            LOAD_FAST_BORROW         5 (executable)
               LOAD_ATTR                9 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L3:     FOR_ITER                75 (to L7)
               STORE_FAST               7 (line)

532            LOAD_FAST_BORROW         7 (line)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0
               STORE_FAST               8 (stripped)

533            LOAD_GLOBAL             12 (FORBIDDEN_IMPORT_PREFIXES)
               GET_ITER
       L4:     FOR_ITER                46 (to L6)
               STORE_FAST               9 (pref)

534            LOAD_FAST_BORROW         8 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_FAST_BORROW         9 (pref)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           28 (to L4)

535    L5:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_FAST_BORROW         9 (pref)
               CALL                     1
               POP_TOP

536            POP_TOP
               JUMP_BACKWARD           73 (to L3)

533    L6:     END_FOR
               POP_ITER
               JUMP_BACKWARD           77 (to L3)

531    L7:     END_FOR
               POP_ITER

537            LOAD_FAST                1 (out)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_GLOBAL             19 (_check + NULL)

538            LOAD_CONST               1 ('service_imports:')
               LOAD_FAST_BORROW         2 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

539            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN
               LOAD_CONST               2 ('FAIL')
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST               3 ('PASS')

540    L9:     LOAD_FAST_BORROW         2 (relpath)
               FORMAT_SIMPLE
               LOAD_CONST               4 (' contains no forbidden import')
               BUILD_STRING             2

541            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L10)
               NOT_TAKEN
               LOAD_CONST               5 ('disqualifying: ')
               LOAD_CONST               6 (', ')
               LOAD_ATTR               21 (join + NULL|self)
               LOAD_FAST_BORROW         6 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST               0 ('')

537   L11:     LOAD_CONST               7 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          230 (to L1)

526   L12:     END_FOR
               POP_ITER

543            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114210, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 546>:
546           RESUME                   0
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

Disassembly of <code object check_cache_invariants at 0x0000018C17E939D0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 546>:
 546            RESUME                   0

 547            BUILD_LIST               0
                STORE_FAST               1 (out)

 548            LOAD_GLOBAL              1 (_read_text + NULL)
                LOAD_GLOBAL              3 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_GLOBAL              4 (CACHE_INV_FILE)
                BINARY_OP               11 (/)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               0 ('')
        L1:     STORE_FAST               2 (inv_src)

 549            LOAD_GLOBAL              6 (CACHE_INV_REQUIRED_TOKENS)
                GET_ITER
        L2:     FOR_ITER                62 (to L7)
                STORE_FAST               3 (tok)

 550            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 551            LOAD_CONST               1 ('cache_inv:token:')
                LOAD_FAST_BORROW         3 (tok)
                LOAD_CONST               2 (slice(None, 60, None))
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                BUILD_STRING             2

 552            LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (tok, inv_src)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L3)
                NOT_TAKEN
                LOAD_CONST               3 ('PASS')
                JUMP_FORWARD             1 (to L4)
        L3:     LOAD_CONST               4 ('FAIL')

 553    L4:     LOAD_CONST               5 ('cache_invalidation.py carries: ')
                LOAD_FAST_BORROW         3 (tok)
                FORMAT_SIMPLE
                BUILD_STRING             2

 554            LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (tok, inv_src)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN
                LOAD_CONST               0 ('')
                JUMP_FORWARD             1 (to L6)
        L5:     LOAD_CONST               6 ('token missing')

 550    L6:     LOAD_CONST               7 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           64 (to L2)

 549    L7:     END_FOR
                POP_ITER

 556            LOAD_GLOBAL              1 (_read_text + NULL)
                LOAD_GLOBAL              3 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_GLOBAL             12 (FLEET_CACHE_FILE)
                BINARY_OP               11 (/)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               0 ('')
        L8:     STORE_FAST               4 (fc_src)

 557            LOAD_GLOBAL             14 (FLEET_CACHE_REQUIRED_TOKENS)
                GET_ITER
        L9:     FOR_ITER                62 (to L14)
                STORE_FAST               3 (tok)

 558            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 559            LOAD_CONST               8 ('fleet_cache:token:')
                LOAD_FAST_BORROW         3 (tok)
                LOAD_CONST               2 (slice(None, 60, None))
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                BUILD_STRING             2

 560            LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (tok, fc_src)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN
                LOAD_CONST               3 ('PASS')
                JUMP_FORWARD             1 (to L11)
       L10:     LOAD_CONST               4 ('FAIL')

 561   L11:     LOAD_CONST               9 ('fleet_status_cache.py carries: ')
                LOAD_FAST_BORROW         3 (tok)
                FORMAT_SIMPLE
                BUILD_STRING             2

 562            LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (tok, fc_src)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L12)
                NOT_TAKEN
                LOAD_CONST               0 ('')
                JUMP_FORWARD             1 (to L13)
       L12:     LOAD_CONST               6 ('token missing')

 558   L13:     LOAD_CONST               7 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           64 (to L9)

 557   L14:     END_FOR
                POP_ITER

 564            LOAD_GLOBAL             17 (_strip_python_comments_and_strings + NULL)
                LOAD_FAST_BORROW         4 (fc_src)
                CALL                     1
                STORE_FAST               5 (fc_exec)

 565            LOAD_GLOBAL             18 (FLEET_CACHE_FORBIDDEN_TOKENS)
                GET_ITER
                LOAD_FAST_AND_CLEAR      6 (t)
                SWAP                     2
       L15:     BUILD_LIST               0
                SWAP                     2
       L16:     FOR_ITER                13 (to L19)
                STORE_FAST_LOAD_FAST   102 (t, t)
                LOAD_FAST_BORROW         5 (fc_exec)
                CONTAINS_OP              0 (in)
       L17:     POP_JUMP_IF_TRUE         3 (to L18)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L16)
       L18:     LOAD_FAST_BORROW         6 (t)
                LIST_APPEND              2
                JUMP_BACKWARD           15 (to L16)
       L19:     END_FOR
                POP_ITER
       L20:     STORE_FAST               7 (bad)
                STORE_FAST               6 (t)

 566            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 567            LOAD_CONST              10 ('fleet_cache:no_autonomous_warming')

 568            LOAD_FAST_BORROW         7 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L21)
                NOT_TAKEN
                LOAD_CONST               4 ('FAIL')
                JUMP_FORWARD             1 (to L22)
       L21:     LOAD_CONST               3 ('PASS')

 569   L22:     LOAD_CONST              11 ('fleet_status_cache.py contains no autonomous warming pattern')

 570            LOAD_FAST_BORROW         7 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L23)
                NOT_TAKEN
                LOAD_CONST              12 ('disqualifying: ')
                LOAD_CONST              13 (', ')
                LOAD_ATTR               21 (join + NULL|self)
                LOAD_FAST_BORROW         7 (bad)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L24)
       L23:     LOAD_CONST               0 ('')

 566   L24:     LOAD_CONST               7 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 572            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L25:     SWAP                     2
                POP_TOP

 565            SWAP                     2
                STORE_FAST               6 (t)
                RERAISE                  0
ExceptionTable:
  L15 to L17 -> L25 [2]
  L18 to L20 -> L25 [2]

Disassembly of <code object __annotate__ at 0x0000018C18114300, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 575>:
575           RESUME                   0
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

Disassembly of <code object check_outbound_dial_wirethrough at 0x0000018C17F74010, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 575>:
 575            RESUME                   0

 576            BUILD_LIST               0
                STORE_FAST               1 (out)

 577            LOAD_GLOBAL              1 (_read_text + NULL)
                LOAD_GLOBAL              3 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_GLOBAL              4 (DIAL_FILE)
                BINARY_OP               11 (/)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               0 ('')
        L1:     STORE_FAST               2 (src)

 578            LOAD_GLOBAL              6 (DIAL_REQUIRED_TOKENS)
                GET_ITER
        L2:     FOR_ITER                62 (to L7)
                STORE_FAST               3 (tok)

 579            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 580            LOAD_CONST               1 ('dial:token:')
                LOAD_FAST_BORROW         3 (tok)
                LOAD_CONST               2 (slice(None, 60, None))
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                BUILD_STRING             2

 581            LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (tok, src)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L3)
                NOT_TAKEN
                LOAD_CONST               3 ('PASS')
                JUMP_FORWARD             1 (to L4)
        L3:     LOAD_CONST               4 ('FAIL')

 582    L4:     LOAD_CONST               5 ('dial.py carries: ')
                LOAD_FAST_BORROW         3 (tok)
                FORMAT_SIMPLE
                BUILD_STRING             2

 583            LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (tok, src)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN
                LOAD_CONST               0 ('')
                JUMP_FORWARD             1 (to L6)
        L5:     LOAD_CONST               6 ('token missing')

 579    L6:     LOAD_CONST               7 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           64 (to L2)

 578    L7:     END_FOR
                POP_ITER

 585            LOAD_GLOBAL             12 (DIAL_REQUIRED_PATTERNS)
                GET_ITER
        L8:     FOR_ITER                62 (to L13)
                STORE_FAST               4 (pat)

 586            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 587            LOAD_CONST               8 ('dial:pattern:')
                LOAD_FAST_BORROW         4 (pat)
                LOAD_CONST               2 (slice(None, 60, None))
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                BUILD_STRING             2

 588            LOAD_FAST_BORROW_LOAD_FAST_BORROW 66 (pat, src)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L9)
                NOT_TAKEN
                LOAD_CONST               3 ('PASS')
                JUMP_FORWARD             1 (to L10)
        L9:     LOAD_CONST               4 ('FAIL')

 589   L10:     LOAD_CONST               9 ('dial.py carries fail-open pattern: ')
                LOAD_FAST_BORROW         4 (pat)
                FORMAT_SIMPLE
                BUILD_STRING             2

 590            LOAD_FAST_BORROW_LOAD_FAST_BORROW 66 (pat, src)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L11)
                NOT_TAKEN
                LOAD_CONST               0 ('')
                JUMP_FORWARD             1 (to L12)
       L11:     LOAD_CONST              10 ('pattern missing')

 586   L12:     LOAD_CONST               7 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           64 (to L8)

 585   L13:     END_FOR
                POP_ITER

 592            LOAD_GLOBAL             15 (_strip_python_comments_and_strings + NULL)
                LOAD_FAST_BORROW         2 (src)
                CALL                     1
                STORE_FAST               5 (executable)

 593            LOAD_GLOBAL             16 (DIAL_FORBIDDEN_TOKENS)
                GET_ITER
                LOAD_FAST_AND_CLEAR      6 (t)
                SWAP                     2
       L14:     BUILD_LIST               0
                SWAP                     2
       L15:     FOR_ITER                13 (to L18)
                STORE_FAST_LOAD_FAST   102 (t, t)
                LOAD_FAST_BORROW         5 (executable)
                CONTAINS_OP              0 (in)
       L16:     POP_JUMP_IF_TRUE         3 (to L17)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L15)
       L17:     LOAD_FAST_BORROW         6 (t)
                LIST_APPEND              2
                JUMP_BACKWARD           15 (to L15)
       L18:     END_FOR
                POP_ITER
       L19:     STORE_FAST               7 (bad)
                STORE_FAST               6 (t)

 594            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 595            LOAD_CONST              11 ('dial:no_breaker_mutation_or_auto_trip')

 596            LOAD_FAST_BORROW         7 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L20)
                NOT_TAKEN
                LOAD_CONST               4 ('FAIL')
                JUMP_FORWARD             1 (to L21)
       L20:     LOAD_CONST               3 ('PASS')

 597   L21:     LOAD_CONST              12 ('dial.py does NOT mutate breaker state and has no auto-trip')

 598            LOAD_FAST_BORROW         7 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L22)
                NOT_TAKEN
                LOAD_CONST              13 ('disqualifying: ')
                LOAD_CONST              14 (', ')
                LOAD_ATTR               19 (join + NULL|self)
                LOAD_FAST_BORROW         7 (bad)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L23)
       L22:     LOAD_CONST               0 ('')

 594   L23:     LOAD_CONST               7 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 600            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L24:     SWAP                     2
                POP_TOP

 593            SWAP                     2
                STORE_FAST               6 (t)
                RERAISE                  0
ExceptionTable:
  L14 to L16 -> L24 [2]
  L17 to L19 -> L24 [2]

Disassembly of <code object __annotate__ at 0x0000018C181143F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 603>:
603           RESUME                   0
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

Disassembly of <code object check_policy_module_read_only at 0x0000018C17EC4280, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 603>:
 603            RESUME                   0

 604            BUILD_LIST               0
                STORE_FAST               1 (out)

 605            LOAD_GLOBAL              1 (_read_text + NULL)
                LOAD_GLOBAL              3 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_GLOBAL              4 (POLICY_FILE)
                BINARY_OP               11 (/)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               0 ('')
        L1:     STORE_FAST               2 (src)

 606            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
                LOAD_FAST_BORROW         2 (src)
                CALL                     1
                STORE_FAST               3 (executable)

 607            LOAD_GLOBAL              8 (POLICY_FORBIDDEN_TOKENS)
                GET_ITER
                LOAD_FAST_AND_CLEAR      4 (t)
                SWAP                     2
        L2:     BUILD_LIST               0
                SWAP                     2
        L3:     FOR_ITER                13 (to L6)
                STORE_FAST_LOAD_FAST    68 (t, t)
                LOAD_FAST_BORROW         3 (executable)
                CONTAINS_OP              0 (in)
        L4:     POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L3)
        L5:     LOAD_FAST_BORROW         4 (t)
                LIST_APPEND              2
                JUMP_BACKWARD           15 (to L3)
        L6:     END_FOR
                POP_ITER
        L7:     STORE_FAST               5 (bad)
                STORE_FAST               4 (t)

 608            LOAD_FAST                1 (out)
                LOAD_ATTR               11 (append + NULL|self)
                LOAD_GLOBAL             13 (_check + NULL)

 609            LOAD_CONST               1 ('policy_module:read_only')

 610            LOAD_FAST_BORROW         5 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               2 ('FAIL')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               3 ('PASS')

 611    L9:     LOAD_CONST               4 ('circuit_breaker_policy.py remains read-only (no auto-trip)')

 612            LOAD_FAST_BORROW         5 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L10)
                NOT_TAKEN
                LOAD_CONST               5 ('disqualifying: ')
                LOAD_CONST               6 (', ')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_FAST_BORROW         5 (bad)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L11)
       L10:     LOAD_CONST               0 ('')

 608   L11:     LOAD_CONST               7 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 614            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L12:     SWAP                     2
                POP_TOP

 607            SWAP                     2
                STORE_FAST               4 (t)
                RERAISE                  0
ExceptionTable:
  L2 to L4 -> L12 [2]
  L5 to L7 -> L12 [2]

Disassembly of <code object __annotate__ at 0x0000018C181144E0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 617>:
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

Disassembly of <code object check_daily_runner_slack at 0x0000018C17D8A570, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 617>:
 617            RESUME                   0

 618            BUILD_LIST               0
                STORE_FAST               1 (out)

 619            LOAD_GLOBAL              1 (_read_text + NULL)
                LOAD_GLOBAL              3 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_GLOBAL              4 (DAILY_RUNNER_FILE)
                BINARY_OP               11 (/)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               0 ('')
        L1:     STORE_FAST               2 (src)

 620            LOAD_GLOBAL              6 (DAILY_RUNNER_REQUIRED_TOKENS)
                GET_ITER
        L2:     FOR_ITER                62 (to L7)
                STORE_FAST               3 (tok)

 621            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 622            LOAD_CONST               1 ('daily_runner:token:')
                LOAD_FAST_BORROW         3 (tok)
                LOAD_CONST               2 (slice(None, 60, None))
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                BUILD_STRING             2

 623            LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (tok, src)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L3)
                NOT_TAKEN
                LOAD_CONST               3 ('PASS')
                JUMP_FORWARD             1 (to L4)
        L3:     LOAD_CONST               4 ('FAIL')

 624    L4:     LOAD_CONST               5 ('run_daily_ops_checklist_report.py carries: ')
                LOAD_FAST_BORROW         3 (tok)
                FORMAT_SIMPLE
                BUILD_STRING             2

 625            LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (tok, src)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN
                LOAD_CONST               0 ('')
                JUMP_FORWARD             1 (to L6)
        L5:     LOAD_CONST               6 ('token missing')

 621    L6:     LOAD_CONST               7 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           64 (to L2)

 620    L7:     END_FOR
                POP_ITER

 628            LOAD_GLOBAL             12 (DAILY_RUNNER_FORBIDDEN_TOKENS)
                GET_ITER
                LOAD_FAST_AND_CLEAR      4 (t)
                SWAP                     2
        L8:     BUILD_LIST               0
                SWAP                     2
        L9:     FOR_ITER                13 (to L12)
                STORE_FAST_LOAD_FAST    68 (t, t)
                LOAD_FAST_BORROW         2 (src)
                CONTAINS_OP              0 (in)
       L10:     POP_JUMP_IF_TRUE         3 (to L11)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L9)
       L11:     LOAD_FAST_BORROW         4 (t)
                LIST_APPEND              2
                JUMP_BACKWARD           15 (to L9)
       L12:     END_FOR
                POP_ITER
       L13:     STORE_FAST               5 (bad)
                STORE_FAST               4 (t)

 629            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 630            LOAD_CONST               8 ('daily_runner:no_webhook_url_print')

 631            LOAD_FAST_BORROW         5 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L14)
                NOT_TAKEN
                LOAD_CONST               4 ('FAIL')
                JUMP_FORWARD             1 (to L15)
       L14:     LOAD_CONST               3 ('PASS')

 632   L15:     LOAD_CONST               9 ('run_daily_ops_checklist_report.py never prints the webhook URL and installs no scheduler')

 634            LOAD_FAST_BORROW         5 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L16)
                NOT_TAKEN
                LOAD_CONST              10 ('disqualifying: ')
                LOAD_CONST              11 (', ')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_FAST_BORROW         5 (bad)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L17)
       L16:     LOAD_CONST               0 ('')

 629   L17:     LOAD_CONST               7 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 636            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L18:     SWAP                     2
                POP_TOP

 628            SWAP                     2
                STORE_FAST               4 (t)
                RERAISE                  0
ExceptionTable:
  L8 to L10 -> L18 [2]
  L11 to L13 -> L18 [2]

Disassembly of <code object __annotate__ at 0x0000018C181146C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 639>:
639           RESUME                   0
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

Disassembly of <code object check_tenant_filters at 0x0000018C17D86020, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 639>:
639            RESUME                   0

640            BUILD_LIST               0
               STORE_FAST               1 (out)

641            LOAD_GLOBAL              1 (_read_text + NULL)
               LOAD_GLOBAL              3 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_GLOBAL              4 (TENANT_PROJ_FILE)
               BINARY_OP               11 (/)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L1:     STORE_FAST               2 (proj_src)

642            LOAD_GLOBAL              6 (TENANT_PROJ_REQUIRED_TOKENS)
               GET_ITER
       L2:     FOR_ITER                62 (to L7)
               STORE_FAST               3 (tok)

643            LOAD_FAST                1 (out)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_GLOBAL             11 (_check + NULL)

644            LOAD_CONST               1 ('tenant_proj:token:')
               LOAD_FAST_BORROW         3 (tok)
               LOAD_CONST               2 (slice(None, 60, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

645            LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (tok, proj_src)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               3 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               4 ('FAIL')

646    L4:     LOAD_CONST               5 ('tenant_incident_projection.py carries: ')
               LOAD_FAST_BORROW         3 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

647            LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (tok, proj_src)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               0 ('')
               JUMP_FORWARD             1 (to L6)
       L5:     LOAD_CONST               6 ('token missing')

643    L6:     LOAD_CONST               7 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           64 (to L2)

642    L7:     END_FOR
               POP_ITER

649            LOAD_GLOBAL              1 (_read_text + NULL)
               LOAD_GLOBAL              3 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_GLOBAL             12 (TENANT_ROUTE_FILE)
               BINARY_OP               11 (/)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L8:     STORE_FAST               4 (route_src)

650            LOAD_GLOBAL             14 (TENANT_ROUTE_REQUIRED_TOKENS)
               GET_ITER
       L9:     FOR_ITER                62 (to L14)
               STORE_FAST               3 (tok)

651            LOAD_FAST                1 (out)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_GLOBAL             11 (_check + NULL)

652            LOAD_CONST               8 ('tenant_route:token:')
               LOAD_FAST_BORROW         3 (tok)
               LOAD_CONST               2 (slice(None, 60, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

653            LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (tok, route_src)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST               3 ('PASS')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST               4 ('FAIL')

654   L11:     LOAD_CONST               9 ('tenant_incidents.py carries: ')
               LOAD_FAST_BORROW         3 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

655            LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (tok, route_src)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        3 (to L12)
               NOT_TAKEN
               LOAD_CONST               0 ('')
               JUMP_FORWARD             1 (to L13)
      L12:     LOAD_CONST               6 ('token missing')

651   L13:     LOAD_CONST               7 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           64 (to L9)

650   L14:     END_FOR
               POP_ITER

657            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181147B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 660>:
660           RESUME                   0
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

Disassembly of <code object check_dashboard_anchors_present at 0x0000018C1794E810, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 660>:
660           RESUME                   0

661           BUILD_LIST               0
              STORE_FAST               1 (out)

662           LOAD_GLOBAL              1 (_read_text + NULL)
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

663           LOAD_GLOBAL              6 (DASHBOARD_REQUIRED_ANCHORS)
              GET_ITER
      L2:     FOR_ITER                65 (to L7)
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST   52 (cid, needle)

664           LOAD_FAST_BORROW_LOAD_FAST_BORROW 66 (needle, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

665           LOAD_FAST                1 (out)
              LOAD_ATTR                9 (append + NULL|self)
              LOAD_GLOBAL             11 (_check + NULL)

666           LOAD_CONST               1 ('dashboard:')
              LOAD_FAST_BORROW         3 (cid)
              FORMAT_SIMPLE
              BUILD_STRING             2

667           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               2 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               3 ('FAIL')

668   L4:     LOAD_CONST               4 ('Dashboard anchor present: ')
              LOAD_FAST_BORROW         4 (needle)
              FORMAT_SIMPLE
              BUILD_STRING             2

669           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               0 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               5 ('anchor missing')

665   L6:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           67 (to L2)

663   L7:     END_FOR
              POP_ITER

671           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181148A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 674>:
674           RESUME                   0
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

Disassembly of <code object check_policy_report_invariants at 0x0000018C17D872F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 674>:
674            RESUME                   0

675            BUILD_LIST               0
               STORE_FAST               1 (out)

676            LOAD_GLOBAL              1 (_read_text + NULL)
               LOAD_GLOBAL              3 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_GLOBAL              4 (POLICY_REPORT_FILE)
               BINARY_OP               11 (/)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L1:     STORE_FAST               2 (pr_src)

677            LOAD_GLOBAL              6 (POLICY_REPORT_REQUIRED_TOKENS)
               GET_ITER
       L2:     FOR_ITER                62 (to L7)
               STORE_FAST               3 (tok)

678            LOAD_FAST                1 (out)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_GLOBAL             11 (_check + NULL)

679            LOAD_CONST               1 ('policy_report:token:')
               LOAD_FAST_BORROW         3 (tok)
               LOAD_CONST               2 (slice(None, 60, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

680            LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (tok, pr_src)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               3 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               4 ('FAIL')

681    L4:     LOAD_CONST               5 ('operator_policy_report.py carries: ')
               LOAD_FAST_BORROW         3 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

682            LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (tok, pr_src)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               0 ('')
               JUMP_FORWARD             1 (to L6)
       L5:     LOAD_CONST               6 ('token missing')

678    L6:     LOAD_CONST               7 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           64 (to L2)

677    L7:     END_FOR
               POP_ITER

684            LOAD_GLOBAL              1 (_read_text + NULL)
               LOAD_GLOBAL              3 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_GLOBAL             12 (FLEET_ROUTE_FILE)
               BINARY_OP               11 (/)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L8:     STORE_FAST               4 (fr_src)

685            LOAD_GLOBAL             14 (FLEET_ROUTE_REQUIRED_TOKENS)
               GET_ITER
       L9:     FOR_ITER                62 (to L14)
               STORE_FAST               3 (tok)

686            LOAD_FAST                1 (out)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_GLOBAL             11 (_check + NULL)

687            LOAD_CONST               8 ('fleet_route:token:')
               LOAD_FAST_BORROW         3 (tok)
               LOAD_CONST               2 (slice(None, 60, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

688            LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (tok, fr_src)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST               3 ('PASS')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST               4 ('FAIL')

689   L11:     LOAD_CONST               9 ('operator_fleet.py carries: ')
               LOAD_FAST_BORROW         3 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

690            LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (tok, fr_src)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        3 (to L12)
               NOT_TAKEN
               LOAD_CONST               0 ('')
               JUMP_FORWARD             1 (to L13)
      L12:     LOAD_CONST               6 ('token missing')

686   L13:     LOAD_CONST               7 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           64 (to L9)

685   L14:     END_FOR
               POP_ITER

692            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114990, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 695>:
695           RESUME                   0
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

Disassembly of <code object check_event_contract_has_pas190_types at 0x0000018C18048C70, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 695>:
695           RESUME                   0

696           BUILD_LIST               0
              STORE_FAST               1 (out)

697           LOAD_GLOBAL              1 (_read_text + NULL)
              LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_GLOBAL              4 (EVENT_CONTRACT_FILE)
              BINARY_OP               11 (/)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               0 ('')
      L1:     STORE_FAST               2 (src)

698           LOAD_GLOBAL              6 (EVENT_CONTRACT_REQUIRED_EVENT_TYPES)
              GET_ITER
      L2:     FOR_ITER                63 (to L7)
              STORE_FAST               3 (tok)

699           LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               4 (ok)

700           LOAD_FAST                1 (out)
              LOAD_ATTR                9 (append + NULL|self)
              LOAD_GLOBAL             11 (_check + NULL)

701           LOAD_CONST               1 ('contract:event:')
              LOAD_FAST_BORROW         3 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

702           LOAD_FAST_BORROW         4 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               2 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               3 ('FAIL')

703   L4:     LOAD_CONST               4 ('events/contract.py carries event_type literal: ')
              LOAD_FAST_BORROW         3 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

704           LOAD_FAST_BORROW         4 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               0 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               5 ('literal missing — contract drift')

700   L6:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           65 (to L2)

698   L7:     END_FOR
              POP_ITER

706           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114A80, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 709>:
709           RESUME                   0
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

Disassembly of <code object check_self_no_env_or_db at 0x0000018C17EA4870, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 709>:
709            RESUME                   0

710            BUILD_LIST               0
               STORE_FAST               1 (out)

711            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_GLOBAL              2 (__file__)
               CALL                     1
               STORE_FAST               2 (fp)

712            LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (fp)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L1:     STORE_FAST               3 (src)

713            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               4 (executable)

714            BUILD_LIST               0
               STORE_FAST               5 (bad)

715            LOAD_FAST_BORROW         4 (executable)
               LOAD_ATTR                9 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L2:     FOR_ITER               199 (to L9)
               STORE_FAST               6 (line)

716            LOAD_FAST_BORROW         6 (line)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0
               STORE_FAST               7 (stripped)

717            LOAD_FAST_BORROW         7 (stripped)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN

718            JUMP_BACKWARD           29 (to L2)

719    L3:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              15 (('import dotenv', 'from dotenv'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L4)
               NOT_TAKEN

720            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               1 ('dotenv import')
               CALL                     1
               POP_TOP

721    L4:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              16 (('import supabase', 'from supabase'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L5)
               NOT_TAKEN

722            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               2 ('supabase import')
               CALL                     1
               POP_TOP

723    L5:     LOAD_CONST               3 ('load_dotenv(')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       18 (to L6)
               NOT_TAKEN

724            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               4 ('load_dotenv() call')
               CALL                     1
               POP_TOP

725    L6:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              17 (('os.environ[', 'getenv('))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L7)
               NOT_TAKEN

726            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               5 ('environ read')
               CALL                     1
               POP_TOP

727    L7:     LOAD_CONST               6 ('get_supabase')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD          182 (to L2)

728    L8:     LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               7 ('supabase client call')
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          201 (to L2)

715    L9:     END_FOR
               POP_ITER

729            LOAD_CONST              18 (('subprocess.run(', 'subprocess.call(', 'requests.get(', 'requests.post(', 'httpx.get(', 'httpx.post(', 'urllib.request.urlopen(', 'git push', 'railway deploy'))
               GET_ITER
      L10:     FOR_ITER                28 (to L12)
               STORE_FAST               8 (tok)

740            LOAD_FAST_BORROW_LOAD_FAST_BORROW 132 (tok, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L11)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L10)

741   L11:     LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_FAST_BORROW         8 (tok)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L10)

729   L12:     END_FOR
               POP_ITER

742            LOAD_FAST                1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             17 (_check + NULL)

743            LOAD_CONST               8 ('self_check:no_env_or_db_or_network')

744            LOAD_FAST_BORROW         5 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L13)
               NOT_TAKEN
               LOAD_CONST               9 ('FAIL')
               JUMP_FORWARD             1 (to L14)
      L13:     LOAD_CONST              10 ('PASS')

745   L14:     LOAD_CONST              11 ('PAS190 readiness checker never reads .env / touches DB / hits network')

746            LOAD_FAST_BORROW         5 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L15)
               NOT_TAKEN
               LOAD_CONST              12 ('disqualifying: ')
               LOAD_CONST              13 (', ')
               LOAD_ATTR               19 (join + NULL|self)
               LOAD_FAST_BORROW         5 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L16)
      L15:     LOAD_CONST               0 ('')

742   L16:     LOAD_CONST              14 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

748            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114B70, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 755>:
755           RESUME                   0
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

Disassembly of <code object _aggregate at 0x0000018C1800B0A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 755>:
 755            RESUME                   0

 756            LOAD_FAST_BORROW         0 (checks)
                GET_ITER
                LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2
        L2:     FOR_ITER                48 (to L7)
                STORE_FAST_LOAD_FAST    17 (c, c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))
        L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           18 (to L2)
        L4:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              2 (SEVERITY_BLOCK)
                COMPARE_OP              88 (bool(==))
        L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           46 (to L2)
        L6:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           50 (to L2)
        L7:     END_FOR
                POP_ITER
        L8:     STORE_FAST               2 (blockers)
                STORE_FAST               1 (c)

 758            LOAD_CONST               3 ('verdict')
                LOAD_FAST_BORROW         2 (blockers)
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L9)
                NOT_TAKEN
                LOAD_GLOBAL              4 (VERDICT_NOT_READY)
                JUMP_FORWARD             5 (to L10)
        L9:     LOAD_GLOBAL              6 (VERDICT_READY)

 759   L10:     LOAD_CONST               4 ('blockers')
                LOAD_FAST_BORROW         2 (blockers)

 760            LOAD_CONST               5 ('info')
                BUILD_LIST               0

 757            BUILD_MAP                3
                RETURN_VALUE

  --   L11:     SWAP                     2
                POP_TOP

 756            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L11 [2]
  L4 to L5 -> L11 [2]
  L6 to L8 -> L11 [2]

Disassembly of <code object __annotate__ at 0x0000018C18114C60, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 764>:
764           RESUME                   0
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

Disassembly of <code object _operator_actions at 0x0000018C18048730, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 764>:
764           RESUME                   0

765           BUILD_LIST               0
              STORE_FAST               1 (out)

766           LOAD_FAST_BORROW         0 (checks)
              GET_ITER
      L1:     FOR_ITER               109 (to L5)
              STORE_FAST               2 (c)

767           LOAD_FAST_BORROW         2 (c)
              LOAD_CONST               0 ('status')
              BINARY_OP               26 ([])
              LOAD_CONST               1 ('FAIL')
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

768           JUMP_BACKWARD           19 (to L1)

769   L2:     LOAD_FAST_BORROW         2 (c)
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

770           LOAD_FAST                1 (out)
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

766   L5:     END_FOR
              POP_ITER

771           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114D50, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 774>:
774           RESUME                   0
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

Disassembly of <code object evaluate at 0x0000018C17ED9FB0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 774>:
774           RESUME                   0

775           BUILD_LIST               0
              STORE_FAST               1 (checks)

776           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              3 (check_pas190_files_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

777           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              5 (check_prior_phases_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

778           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              7 (check_memory_review_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

779           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              9 (check_worker_off_by_default + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

780           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             11 (check_doc_required_clauses + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

781           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             13 (check_doc_no_forbidden_scope + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

782           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             15 (check_service_no_forbidden_imports + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

783           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             17 (check_cache_invariants + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

784           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             19 (check_outbound_dial_wirethrough + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

785           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             21 (check_policy_module_read_only + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

786           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             23 (check_daily_runner_slack + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

787           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             25 (check_tenant_filters + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

788           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             27 (check_dashboard_anchors_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

789           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             29 (check_policy_report_invariants + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

790           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             31 (check_event_contract_has_pas190_types + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

791           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             33 (check_self_no_env_or_db + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

793           LOAD_GLOBAL             35 (_aggregate + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1
              STORE_FAST               2 (agg)

795           LOAD_CONST               0 ('phase')
              LOAD_CONST               1 ('PAS190')

796           LOAD_CONST               2 ('generated_at')
              LOAD_GLOBAL             37 (_now_iso + NULL)
              CALL                     0

797           LOAD_CONST               3 ('verdict')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])

798           LOAD_CONST               4 ('ready')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])
              LOAD_GLOBAL             38 (VERDICT_READY)
              COMPARE_OP              72 (==)

799           LOAD_CONST               5 ('blocker_count')
              LOAD_GLOBAL             41 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               6 ('blockers')
              BINARY_OP               26 ([])
              CALL                     1

800           LOAD_CONST               7 ('info_count')
              LOAD_GLOBAL             41 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               8 ('info')
              BINARY_OP               26 ([])
              CALL                     1

801           LOAD_CONST               9 ('check_count')
              LOAD_GLOBAL             41 (len + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

802           LOAD_CONST              10 ('pass_count')
              LOAD_GLOBAL             43 (sum + NULL)
              LOAD_CONST              11 (<code object <genexpr> at 0x0000018C180532D0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 802>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

803           LOAD_CONST              12 ('fail_count')
              LOAD_GLOBAL             43 (sum + NULL)
              LOAD_CONST              13 (<code object <genexpr> at 0x0000018C18053510, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 803>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

804           LOAD_CONST              14 ('checks')
              LOAD_FAST_BORROW         1 (checks)

805           LOAD_CONST              15 ('operator_actions')
              LOAD_GLOBAL             45 (_operator_actions + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

794           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C180532D0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 802>:
 802           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C18053510, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 803>:
 803           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C18114F30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 812>:
812           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C18128030, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 812>:
812           RESUME                   0

813           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

814           LOAD_CONST               0 ('pas190_final_wirethrough_readiness_check')

816           LOAD_CONST               1 ('PAS190 — Final operational wire-through polish readiness gate. Read-only — never reads .env, never touches Supabase, never executes a deploy / migration.')

813           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

822           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               3 ('--repo-root')
              LOAD_GLOBAL              6 (_REPO_ROOT_DEFAULT)
              LOAD_CONST               4 (('default',))
              CALL_KW                  2
              POP_TOP

823           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               5 ('--output')
              LOAD_GLOBAL              8 (REPORT_FILENAME)
              LOAD_CONST               4 (('default',))
              CALL_KW                  2
              POP_TOP

824           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               6 ('--json')
              LOAD_CONST               7 ('store_true')
              LOAD_CONST               8 (('action',))
              CALL_KW                  2
              POP_TOP

825           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               9 ('--summary-only')
              LOAD_CONST               7 ('store_true')
              LOAD_CONST               8 (('action',))
              CALL_KW                  2
              POP_TOP

826           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST              10 ('--strict')
              LOAD_CONST               7 ('store_true')
              LOAD_CONST               8 (('action',))
              CALL_KW                  2
              POP_TOP

827           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18115020, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 830>:
830           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C17D8D460, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 830>:
830           RESUME                   0

831           LOAD_GLOBAL              1 (print + NULL)

832           LOAD_CONST               0 ('[PAS190] verdict=')
              LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               1 ('verdict')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               2 (' blockers=')

833           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               3 ('blocker_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' info=')

834           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               5 ('info_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' checks=')

835           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               7 ('check_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' pass=')

836           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               9 ('pass_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              10 (' fail=')

837           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              11 ('fail_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE

832           BUILD_STRING            12

831           CALL                     1
              POP_TOP

839           LOAD_FAST_BORROW         0 (report)
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

840           LOAD_FAST_BORROW         1 (actions)
              TO_BOOL
              POP_JUMP_IF_FALSE       93 (to L5)
              NOT_TAKEN

841           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              13 ('[PAS190] operator actions:')
              CALL                     1
              POP_TOP

842           LOAD_FAST_BORROW         1 (actions)
              LOAD_CONST              14 (slice(None, 25, None))
              BINARY_OP               26 ([])
              GET_ITER
      L2:     FOR_ITER                17 (to L3)
              STORE_FAST               2 (a)

843           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              15 ('  - ')
              LOAD_FAST_BORROW         2 (a)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L2)

842   L3:     END_FOR
              POP_ITER

844           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         1 (actions)
              CALL                     1
              LOAD_SMALL_INT          25
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       34 (to L4)
              NOT_TAKEN

845           LOAD_GLOBAL              1 (print + NULL)
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

844   L4:     LOAD_CONST              18 (None)
              RETURN_VALUE

840   L5:     LOAD_CONST              18 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024F30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 848>:
848           RESUME                   0
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

Disassembly of <code object _write_report at 0x0000018C18128210, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 848>:
 848           RESUME                   0

 849           NOP

 850   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

 851           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

 852           LOAD_CONST               3 ('utf-8')

 850           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 854           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

 855   L4:     LOAD_GLOBAL             11 (print + NULL)

 856           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

 857           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

 856           BUILD_STRING             4

 858           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

 855           LOAD_CONST               7 (('file',))
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

 854   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18114030, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 862>:
862           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17D88890, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas190_final_wirethrough_readiness_check.py", line 862>:
 862            RESUME                   0

 863            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 864            NOP

 865    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 869    L2:     LOAD_GLOBAL             10 (os)
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

 870            LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               21 (isdir + NULL|self)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L4)
                NOT_TAKEN

 871            LOAD_GLOBAL             23 (print + NULL)
                LOAD_CONST               2 ('error: --repo-root not a directory: ')
                LOAD_FAST                4 (repo_root)
                FORMAT_SIMPLE
                BUILD_STRING             2
                LOAD_GLOBAL             24 (sys)
                LOAD_ATTR               26 (stderr)
                LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

 872            LOAD_SMALL_INT           2
                RETURN_VALUE

 874    L4:     LOAD_GLOBAL             29 (evaluate + NULL)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                STORE_FAST               5 (report)

 876            LOAD_FAST                2 (args)
                LOAD_ATTR               30 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L5)
                NOT_TAKEN

 877            LOAD_GLOBAL             33 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               34 (output)
                LOAD_FAST                5 (report)
                CALL                     2
                POP_TOP

 879    L5:     LOAD_GLOBAL             37 (_print_summary + NULL)
                LOAD_FAST                5 (report)
                CALL                     1
                POP_TOP

 881            LOAD_FAST                2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L6)
                NOT_TAKEN

 882            LOAD_GLOBAL             23 (print + NULL)
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

 884    L6:     LOAD_FAST                5 (report)
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

 866            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L17)
                NOT_TAKEN
                STORE_FAST               3 (e)

 867    L9:     LOAD_FAST                3 (e)
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

 866   L17:     RERAISE                  0

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
