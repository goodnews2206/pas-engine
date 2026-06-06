# scripts_readiness/pas188_operational_scaling_readiness_check

- **pyc:** `scripts\__pycache__\pas188_operational_scaling_readiness_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/pas188_operational_scaling_readiness_check.py`
- **co_filename (from bytecode):** `C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS188 — Operational scaling automation readiness gate.

Deterministic, non-mutating evaluator for "is PAS188 wired
correctly, additive-only, and free of regressions across
the PAS160-PAS187 + PAS-SECURITY-01/02/03/04 doctrine?".

Walks the repo and verifies:

  * PAS188 surfaces exist (doc / readiness gate / two
    migration proposals / three services / route / two
    runner scripts / test file).
  * Doctrine clauses present in the PAS188 doc.
  * No PAS188 doc smuggles a forbidden out-of-scope
    feature token in a positive sense.
  * Fleet-status cache is in-process, TTL-bounded, never
    schedules anything autonomous.
  * Circuit-breaker is operator-driven; the service does
    NOT auto-trip / does NOT mutate Twilio / Cal.com /
    worker.
  * Incident log is append-only; mutation tokens are
    restricted to status / resolved_* / metadata.
  * Daily-ops runner script is read-only; contains no
    `subprocess.run(` for deploys / migrations /
    scheduler installs.
  * Migration-promotion runner never executes the
    migration (no `subprocess`, no `psycopg2`, no
    `supabase` import).
  * Operator-incidents route requires admin auth + has
    no tenant surface + mutation routes are confined to
    incidents + circuit-breakers.
  * Dashboard carries the PAS188 fleet panel anchors
    (additive PAS185-A-style mount).
  * Event contract carries the 5 PAS188 event types.
  * `app/main.py` mounts the operator_incidents router.
  * No Gmail / google-auth / IMAP / POP3 / Composio /
    TrustClaw / embedding / vector imports in any
    PAS188 surface.
  * Memory Review surface untouched.
  * Worker remains OFF by default.
  * PAS160-PAS187 + PAS-SECURITY-01/02/03/04 readiness
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

`__annotate__`, `_aggregate`, `_build_parser`, `_check`, `_now_iso`, `_operator_actions`, `_print_summary`, `_read_text`, `_strip_python_comments_and_strings`, `_write_report`, `check_circuit_breaker_invariants`, `check_daily_runner_no_scheduler`, `check_dashboard_anchors_present`, `check_doc_no_forbidden_scope`, `check_doc_required_clauses`, `check_event_contract_has_pas188_types`, `check_fleet_cache_invariants`, `check_incident_log_invariants`, `check_main_mounts_incidents_router`, `check_memory_review_intact`, `check_migration_runner_does_not_execute`, `check_operator_incidents_route_invariants`, `check_pas188_files_present`, `check_prior_phases_intact`, `check_self_no_env_or_db`, `check_service_no_forbidden_imports`, `check_service_no_scheduler_or_loop`, `check_worker_off_by_default`, `evaluate`, `main`

## Env-key candidates

`BLOCK`, `FAIL`, `NOT_READY`, `PAS188`, `PASS`, `READY`

## String constants (redacted where noted)

- '\nPAS188 — Operational scaling automation readiness gate.\n\nDeterministic, non-mutating evaluator for "is PAS188 wired\ncorrectly, additive-only, and free of regressions across\nthe PAS160-PAS187 + PAS-SECURITY-01/02/03/04 doctrine?".\n\nWalks the repo and verifies:\n\n  * PAS188 surfaces exist (doc / readiness gate / two\n    migration proposals / three services / route / two\n    runner scripts / test file).\n  * Doctrine clauses present in the PAS188 doc.\n  * No PAS188 doc smuggles a forbidden out-of-scope\n    feature token in a positive sense.\n  * Fleet-status cache is in-process, TTL-bounded, never\n    schedules anything autonomous.\n  * Circuit-breaker is operator-driven; the service does\n    NOT auto-trip / does NOT mutate Twilio / Cal.com /\n    worker.\n  * Incident log is append-only; mutation tokens are\n    restricted to status / resolved_* / metadata.\n  * Daily-ops runner script is read-only; contains no\n    `subprocess.run(` for deploys / migrations /\n    scheduler installs.\n  * Migration-promotion runner never executes the\n    migration (no `subprocess`, no `psycopg2`, no\n    `supabase` import).\n  * Operator-incidents route requires admin auth + has\n    no tenant surface + mutation routes are confined to\n    incidents + circuit-breakers.\n  * Dashboard carries the PAS188 fleet panel anchors\n    (additive PAS185-A-style mount).\n  * Event contract carries the 5 PAS188 event types.\n  * `app/main.py` mounts the operator_incidents router.\n  * No Gmail / google-auth / IMAP / POP3 / Composio /\n    TrustClaw / embedding / vector imports in any\n    PAS188 surface.\n  * Memory Review surface untouched.\n  * Worker remains OFF by default.\n  * PAS160-PAS187 + PAS-SECURITY-01/02/03/04 readiness\n    scripts still on disk.\n\nRead-only: never reads .env, never touches Supabase,\nnever executes a deploy / migration / network call.\n\nExit codes:\n  0 — READY\n  1 — NOT_READY (one or more BLOCK checks failed)\n  2 — bad CLI args\n'
- 'utf-8'
- 'READY'
- 'NOT_READY'
- 'BLOCK'
- 'app/routes/operator_incidents.py'
- 'app/static/dashboard/index.html'
- 'app/services/events/contract.py'
- 'severity'
- 'detail'
- 'pas188_operational_scaling_readiness_report.json'
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
- 'Required PAS188 artefact present: '
- 'missing'
- 'prior_phase:'
- 'Prior-phase readiness script intact: '
- 'missing — PAS188 must not delete'
- 'memory_review:'
- 'Memory Review file present: '
- 'Memory Review file deleted — PAS188 must not touch'
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
- 'SERVICE files (not runner scripts) must have no\nscheduler / autonomous loop tokens.'
- 'service_scheduler:'
- ' contains no scheduler / cron / autonomous loop'
- 'app/services/operator/fleet_status_cache.py'
- 'fleet_cache:token:'
- 'fleet_status_cache.py carries: '
- 'token missing'
- 'fleet_cache:no_autonomous_warming'
- 'fleet_status_cache.py contains no autonomous warming pattern'
- 'app/services/operator/circuit_breaker.py'
- 'circuit_breaker:token:'
- 'circuit_breaker.py carries: '
- 'circuit_breaker:no_external_mutation'
- 'circuit_breaker.py does NOT mutate Twilio / Cal.com / etc'
- 'app/services/operator/incident_log.py'
- 'incident_log:token:'
- 'incident_log.py carries: '
- 'incident_log:no_autonomous_opener'
- 'incident_log.py does NOT define an autonomous opener'
- 'def delete_incident'
- 'incident_log:no_delete_function'
- 'incident_log.py exports no delete function (append-only doctrine)'
- 'found def delete_incident'
- 'dashboard:'
- 'Dashboard anchor present: '
- 'anchor missing'
- 'contract:event:'
- 'events/contract.py carries event_type literal: '
- 'literal missing — contract drift'
- 'app/main.py'
- 'main:mount:'
- 'app/main.py contains: '
- 'mount missing — route inaccessible'
- 'incidents_route:require_admin'
- 'def require_admin'
- ' declares require_admin dependency'
- 'require_admin missing'
- 'check_rate_limit'
- 'surface="admin"'
- 'incidents_route:rate_limit'
- ' wires PAS-SECURITY-04 rate limit'
- 'rate_limit / surface=admin missing'
- 'incidents_route:no_tenant_surface'
- ' declares no tenant surface'
- 'incidents_route:endpoint:'
- 'endpoint declared: '
- 'endpoint missing'
- 'scripts/run_daily_ops_checklist_report.py'
- 'daily_runner:no_scheduler'
- 'run_daily_ops_checklist_report.py contains no scheduler / loop'
- 'scripts/run_migration_promotion_checklist.py'
- 'migration_runner:no_execution'
- 'run_migration_promotion_checklist.py does NOT execute migrations or call Supabase'
- 'dotenv import'
- 'supabase import'
- 'load_dotenv('
- 'load_dotenv() call'
- 'environ read'
- 'get_supabase'
- 'supabase client call'
- 'self_check:no_env_or_db_or_network'
- 'PAS188 readiness checker never reads .env / touches DB / hits network'
- 'checks'
- 'verdict'
- 'blockers'
- 'info'
- 'List[str]'
- ' — '
- 'see report'
- 'phase'
- 'PAS188'
- 'generated_at'
- 'ready'
- 'blocker_count'
- 'info_count'
- 'check_count'
- 'pass_count'
- 'fail_count'
- 'operator_actions'
- 'argparse.ArgumentParser'
- 'pas188_operational_scaling_readiness_check'
- 'PAS188 — Operational scaling automation readiness gate. Read-only — never reads .env, never touches Supabase, never executes a deploy / migration.'
- '--repo-root'
- '--output'
- '--json'
- 'store_true'
- '--summary-only'
- '--strict'
- 'report'
- 'None'
- '[PAS188] verdict='
- ' blockers='
- ' info='
- ' checks='
- ' pass='
- ' fail='
- '[PAS188] operator actions:'
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

   1           LOAD_CONST               0 ('\nPAS188 — Operational scaling automation readiness gate.\n\nDeterministic, non-mutating evaluator for "is PAS188 wired\ncorrectly, additive-only, and free of regressions across\nthe PAS160-PAS187 + PAS-SECURITY-01/02/03/04 doctrine?".\n\nWalks the repo and verifies:\n\n  * PAS188 surfaces exist (doc / readiness gate / two\n    migration proposals / three services / route / two\n    runner scripts / test file).\n  * Doctrine clauses present in the PAS188 doc.\n  * No PAS188 doc smuggles a forbidden out-of-scope\n    feature token in a positive sense.\n  * Fleet-status cache is in-process, TTL-bounded, never\n    schedules anything autonomous.\n  * Circuit-breaker is operator-driven; the service does\n    NOT auto-trip / does NOT mutate Twilio / Cal.com /\n    worker.\n  * Incident log is append-only; mutation tokens are\n    restricted to status / resolved_* / metadata.\n  * Daily-ops runner script is read-only; contains no\n    `subprocess.run(` for deploys / migrations /\n    scheduler installs.\n  * Migration-promotion runner never executes the\n    migration (no `subprocess`, no `psycopg2`, no\n    `supabase` import).\n  * Operator-incidents route requires admin auth + has\n    no tenant surface + mutation routes are confined to\n    incidents + circuit-breakers.\n  * Dashboard carries the PAS188 fleet panel anchors\n    (additive PAS185-A-style mount).\n  * Event contract carries the 5 PAS188 event types.\n  * `app/main.py` mounts the operator_incidents router.\n  * No Gmail / google-auth / IMAP / POP3 / Composio /\n    TrustClaw / embedding / vector imports in any\n    PAS188 surface.\n  * Memory Review surface untouched.\n  * Worker remains OFF by default.\n  * PAS160-PAS187 + PAS-SECURITY-01/02/03/04 readiness\n    scripts still on disk.\n\nRead-only: never reads .env, never touches Supabase,\nnever executes a deploy / migration / network call.\n\nExit codes:\n  0 — READY\n  1 — NOT_READY (one or more BLOCK checks failed)\n  2 — bad CLI args\n')
               STORE_NAME               0 (__doc__)

  53           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  55           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  56           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (json)
               STORE_NAME               4 (json)

  57           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (os)
               STORE_NAME               5 (os)

  58           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (sys)
               STORE_NAME               6 (sys)

  59           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              7 (datetime)
               IMPORT_FROM              7 (datetime)
               STORE_NAME               7 (datetime)
               IMPORT_FROM              8 (timezone)
               STORE_NAME               8 (timezone)
               POP_TOP

  60           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Path',))
               IMPORT_NAME              9 (pathlib)
               IMPORT_FROM             10 (Path)
               STORE_NAME              10 (Path)
               POP_TOP

  61           LOAD_SMALL_INT           0
               LOAD_CONST               5 (('List', 'Optional'))
               IMPORT_NAME             11 (typing)
               IMPORT_FROM             12 (List)
               STORE_NAME              12 (List)
               IMPORT_FROM             13 (Optional)
               STORE_NAME              13 (Optional)
               POP_TOP

  64           LOAD_NAME                6 (sys)
               LOAD_ATTR               28 (stdout)
               LOAD_NAME                6 (sys)
               LOAD_ATTR               30 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              16 (_stream)

  65           NOP

  66   L2:     LOAD_NAME               16 (_stream)
               LOAD_ATTR               35 (reconfigure + NULL|self)
               LOAD_CONST               6 ('utf-8')
               LOAD_CONST               7 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  64   L4:     END_FOR
               POP_ITER

  71           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               41 (abspath + NULL|self)

  72           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               43 (join + NULL|self)
               LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               45 (dirname + NULL|self)
               LOAD_NAME               23 (__file__)
               CALL                     1
               LOAD_CONST               8 ('..')
               CALL                     2

  71           CALL                     1
               STORE_NAME              24 (_REPO_ROOT_DEFAULT)

  76           LOAD_CONST               9 ('READY')
               STORE_NAME              25 (VERDICT_READY)

  77           LOAD_CONST              10 ('NOT_READY')
               STORE_NAME              26 (VERDICT_NOT_READY)

  79           LOAD_CONST              11 ('BLOCK')
               STORE_NAME              27 (SEVERITY_BLOCK)

  86           LOAD_CONST              78 (('docs/pas188_operational_scaling_automation.md', 'scripts/pas188_operational_scaling_readiness_check.py', 'scripts/migrate_v37_brokerage_circuit_breakers.sql', 'scripts/migrate_v38_operator_incidents.sql', 'app/services/operator/fleet_status_cache.py', 'app/services/operator/circuit_breaker.py', 'app/services/operator/incident_log.py', 'app/routes/operator_incidents.py', 'scripts/run_daily_ops_checklist_report.py', 'scripts/run_migration_promotion_checklist.py', 'tests/mvp/test_pas188_operational_scaling.py'))
               STORE_NAME              28 (PAS188_FILES)

 101           LOAD_CONST              79 (('scripts/pas160_mvp_sequence_check.py', 'scripts/pas161_lead_ingestion_readiness_check.py', 'scripts/pas162_pending_calls_readiness_check.py', 'scripts/pas163_candidate_pipeline_readiness_check.py', 'scripts/pas164_email_ingestion_readiness_check.py', 'scripts/pas165_email_auth_dedupe_readiness_check.py', 'scripts/pas166_email_dedupe_policy_readiness_check.py', 'scripts/pas167_email_secret_reaper_readiness_check.py', 'scripts/pas168_email_secret_rotation_readiness_check.py', 'scripts/pas169_crypto_roundtrip_check.py', 'scripts/pas169_launch_readiness_check.py', 'scripts/pas_launch_integrity_check.py', 'scripts/pas170_operator_survival_readiness_check.py', 'scripts/pas171_external_pilot_readiness_check.py', 'scripts/pas172_pilot_operations_readiness_check.py', 'scripts/pas173_brokerage_operator_readiness_check.py', 'scripts/pas174_operator_audit_readiness_check.py', 'scripts/pas175_audit_integrity_readiness_check.py', 'scripts/pas176_audit_chain_readiness_check.py', 'scripts/pas177_tenant_audit_verification_readiness_check.py', 'scripts/pas178_audit_window_chain_readiness_check.py', 'scripts/pas179_controlled_learning_readiness_check.py', 'scripts/pas180_learning_review_readiness_check.py', 'scripts/pas181_manual_test_harness_readiness_check.py', 'scripts/pas182_adaptive_memory_bridge_readiness_check.py', 'scripts/pas183_onboarding_product_readiness_check.py', 'scripts/pas184_pilot_experience_readiness_check.py', 'scripts/pas186_final_cutover_readiness_check.py', 'scripts/pas187_fleet_cutover_readiness_check.py', 'scripts/pas_security_01_hardening_readiness_check.py', 'scripts/pas_security_02_rate_limit_scanner_readiness_check.py', 'scripts/pas_security_03_admin_webhook_ci_readiness_check.py', 'scripts/pas_security_04_operator_reveal_https_readiness_check.py'))
               STORE_NAME              29 (PRIOR_PHASE_FILES)

 138           LOAD_CONST              80 (('app/services/memory/review.py', 'app/services/memory/review_stats.py', 'app/services/memory/review_export.py', 'app/services/memory/review_actors.py', 'app/services/memory/review_alerts.py', 'app/services/memory/operator_console.py'))
               STORE_NAME              30 (MEMORY_REVIEW_FILES)

 148           LOAD_CONST              81 ((('docs/pas188_operational_scaling_automation.md', (('purpose', ('purpose',)), ('relationship-to-pas186-187', ('relationship to pas187',)), ('fleet-status-cache-doctrine', ('fleet-status cache doctrine',)), ('circuit-breaker-doctrine', ('per-brokerage circuit-breaker doctrine',)), ('incident-log-doctrine', ('structured incident log doctrine',)), ('migration-promotion-doctrine', ('migration-promotion checklist doctrine',)), ('daily-report-doctrine', ('operator-run daily checklist report doctrine',)), ('dashboard-panel-doctrine', ('dashboard fleet panel doctrine',)), ('stop-the-rollout', ('stop-the-rollout',)), ('escalation-workflow', ('escalation workflow',)), ('rollout-tier-doctrine', ('rollout tier doctrine',)), ('rollback-workflow', ('rollback workflow',)), ('no-autonomous-remediation', ('no autonomous remediation',)), ('no-gmail', ('no gmail',)), ('composio', ('composio',)), ('remaining-limitations', ('remaining limitations',)), ('intentionally-does-not-build', ('intentionally does not build',)))),))
               STORE_NAME              31 (DOC_REQUIRED_CLAUSES)

 171           LOAD_CONST              82 (('gmail oauth integration', 'composio integration', 'trustclaw', 'auto-approve memory', 'ai chat assistant enabled', 'embedding model', 'vector database', 'imap inbox scanner', 'pop3 inbox scanner'))
               STORE_NAME              32 (FORBIDDEN_DOC_TOKENS)

 184           LOAD_CONST              83 (('app/services/operator/fleet_status_cache.py', 'app/services/operator/circuit_breaker.py', 'app/services/operator/incident_log.py', 'app/routes/operator_incidents.py', 'scripts/run_daily_ops_checklist_report.py', 'scripts/run_migration_promotion_checklist.py'))
               STORE_NAME              33 (SERVICE_FILES)

 194           LOAD_CONST              84 (('from googleapiclient', 'import googleapiclient', 'from google.oauth2', 'import google.oauth2', 'from google_auth_oauthlib', 'import google_auth_oauthlib', 'from imaplib', 'import imaplib', 'from poplib', 'import poplib', 'from composio', 'import composio', 'from trustclaw', 'import trustclaw', 'from chromadb', 'import chromadb', 'from pinecone', 'import pinecone', 'from pgvector', 'import pgvector', 'from sentence_transformers', 'import sentence_transformers', 'from openai', 'import openai'))
               STORE_NAME              34 (FORBIDDEN_IMPORT_PREFIXES)

 224           LOAD_CONST              85 (('apscheduler.schedulers', 'from celery', 'import celery', 'from croniter', 'import croniter', 'schedule.every(', 'while True:', 'asyncio.create_task(auto_'))
               STORE_NAME              35 (FORBIDDEN_SERVICE_TOKENS)

 238           LOAD_CONST              86 (('import psycopg2', 'from psycopg2', 'import supabase', 'from supabase', 'subprocess.run(', 'subprocess.call(', 'subprocess.Popen(', 'os.system(', 'requests.post(', 'httpx.post('))
               STORE_NAME              36 (FORBIDDEN_MIGRATION_RUNNER_TOKENS)

 254           LOAD_CONST              87 (('apscheduler.schedulers', 'from celery', 'import celery', 'from croniter', 'import croniter', 'schedule.every(', 'while True:', 'crontab.write'))
               STORE_NAME              37 (FORBIDDEN_DAILY_RUNNER_TOKENS)

 266           LOAD_CONST              13 ('app/static/dashboard/index.html')
               STORE_NAME              38 (DASHBOARD_FILE)

 269           LOAD_CONST              88 ((('pas188:fleet-section-label', 'Fleet Observability'), ('pas188:fleet-container', 'aFleetStatusContent'), ('pas188:fleet-loader-name', 'loadOperatorFleetStatus'), ('pas188:fleet-renderer-name', 'renderOperatorFleetStatus'), ('pas188:fleet-mount-call', "loadOperatorFleetStatus('aFleetStatusContent')"), ('pas185a:snapshot-container', 'aPilotOpsContent'), ('pas185a:learning-container', 'aIntelLearning')))
               STORE_NAME              39 (DASHBOARD_REQUIRED_ANCHORS)

 281           LOAD_CONST              12 ('app/routes/operator_incidents.py')
               STORE_NAME              40 (CUTOVER_ROUTE_FILE)

 285           LOAD_CONST              89 (('def trip_breaker', 'def reset_breaker', 'def current_breaker_state', 'def list_breakers', 'STATUS_OK', 'STATUS_TRIPPED', 'STATUS_RESETTING', 'OPERATOR_REQUESTED'))
               STORE_NAME              41 (CIRCUIT_BREAKER_REQUIRED_TOKENS)

 299           LOAD_CONST              90 (('twilio_client.', 'calcom_client.', 'disable_inbound(', 'stop_outbound(', 'pause_brokerage('))
               STORE_NAME              42 (CIRCUIT_BREAKER_FORBIDDEN_TOKENS)

 308           LOAD_CONST              91 (('def open_incident', 'def update_incident_status', 'def resolve_incident', 'def list_incidents', 'STATUS_OPEN', 'STATUS_RESOLVED'))
               STORE_NAME              43 (INCIDENT_LOG_REQUIRED_TOKENS)

 320           LOAD_CONST              92 (('def auto_open_incident', 'def autonomous_open(', 'asyncio.create_task(open_incident'))
               STORE_NAME              44 (INCIDENT_LOG_FORBIDDEN_TOKENS)

 327           LOAD_CONST              93 (('def get_fleet_brokerage_health_summary', 'def get_fleet_chain_status_report', 'def get_fleet_rollout_readiness_summary', 'def get_fleet_exception_report', 'def invalidate', 'def cache_stats', 'def configure_ttl', '_TTL_DEFAULT'))
               STORE_NAME              45 (FLEET_CACHE_REQUIRED_TOKENS)

 341           LOAD_CONST              94 (('threading.Timer(', 'Thread(target=', 'apscheduler.schedulers', 'while True:', 'asyncio.create_task('))
               STORE_NAME              46 (FLEET_CACHE_FORBIDDEN_TOKENS)

 351           LOAD_CONST              14 ('app/services/events/contract.py')
               STORE_NAME              47 (EVENT_CONTRACT_FILE)

 352           LOAD_CONST              95 (('"incident.opened"', '"incident.status_changed"', '"incident.resolved"', '"circuit_breaker.tripped"', '"circuit_breaker.reset"'))
               STORE_NAME              48 (EVENT_CONTRACT_REQUIRED_EVENT_TYPES)

 361           LOAD_CONST              96 (('operator_incidents_router', 'from app.routes.operator_incidents import'))
               STORE_NAME              49 (MAIN_PY_REQUIRED_MOUNT_TOKENS)

 371           LOAD_CONST              15 ('severity')
               LOAD_NAME               27 (SEVERITY_BLOCK)
               LOAD_CONST              16 ('detail')
               LOAD_CONST              17 ('')
               BUILD_MAP                2
               LOAD_CONST              18 (<code object __annotate__ at 0x0000018C18025F30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 371>)
               MAKE_FUNCTION
               LOAD_CONST              19 (<code object _check at 0x0000018C17FA34B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 371>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              50 (_check)

 381           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA31E0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 381>)
               MAKE_FUNCTION
               LOAD_CONST              21 (<code object _now_iso at 0x0000018C18038170, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 381>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              51 (_now_iso)

 385           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA3A50, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 385>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object _read_text at 0x0000018C18053E10, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 385>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              52 (_read_text)

 392           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA3E10, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 392>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object _strip_python_comments_and_strings at 0x0000018C17E923B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 392>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              53 (_strip_python_comments_and_strings)

 433           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA3960, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 433>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object check_pas188_files_present at 0x0000018C18060F60, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 433>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              54 (check_pas188_files_present)

 446           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA3C30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 446>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object check_prior_phases_intact at 0x0000018C180606F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 446>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              55 (check_prior_phases_intact)

 459           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA3690, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 459>)
               MAKE_FUNCTION
               LOAD_CONST              31 (<code object check_memory_review_intact at 0x0000018C18061110, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 459>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              56 (check_memory_review_intact)

 472           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA30F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 472>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object check_worker_off_by_default at 0x0000018C1794EBB0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 472>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              57 (check_worker_off_by_default)

 487           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA3F00, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 487>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object check_doc_required_clauses at 0x0000018C17D8AAB0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 487>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              58 (check_doc_required_clauses)

 504           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C17FA3870, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 504>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object check_doc_no_forbidden_scope at 0x0000018C17ECE220, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 504>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              59 (check_doc_no_forbidden_scope)

 519           LOAD_CONST              38 (<code object __annotate__ at 0x0000018C17FA3000, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 519>)
               MAKE_FUNCTION
               LOAD_CONST              39 (<code object check_service_no_forbidden_imports at 0x0000018C17F78F70, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 519>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              60 (check_service_no_forbidden_imports)

 541           LOAD_CONST              40 (<code object __annotate__ at 0x0000018C18114120, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 541>)
               MAKE_FUNCTION
               LOAD_CONST              41 (<code object check_service_no_scheduler_or_loop at 0x0000018C17ECE6C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 541>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              61 (check_service_no_scheduler_or_loop)

 568           LOAD_CONST              42 (<code object __annotate__ at 0x0000018C18114210, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 568>)
               MAKE_FUNCTION
               LOAD_CONST              43 (<code object check_fleet_cache_invariants at 0x0000018C17F79230, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 568>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              62 (check_fleet_cache_invariants)

 591           LOAD_CONST              44 (<code object __annotate__ at 0x0000018C18114300, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 591>)
               MAKE_FUNCTION
               LOAD_CONST              45 (<code object check_circuit_breaker_invariants at 0x0000018C17F78730, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 591>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              63 (check_circuit_breaker_invariants)

 614           LOAD_CONST              46 (<code object __annotate__ at 0x0000018C181143F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 614>)
               MAKE_FUNCTION
               LOAD_CONST              47 (<code object check_incident_log_invariants at 0x0000018C182DA010, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 614>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              64 (check_incident_log_invariants)

 646           LOAD_CONST              48 (<code object __annotate__ at 0x0000018C181144E0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 646>)
               MAKE_FUNCTION
               LOAD_CONST              49 (<code object check_dashboard_anchors_present at 0x0000018C1794E810, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 646>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              65 (check_dashboard_anchors_present)

 660           LOAD_CONST              50 (<code object __annotate__ at 0x0000018C181145D0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 660>)
               MAKE_FUNCTION
               LOAD_CONST              51 (<code object check_event_contract_has_pas188_types at 0x0000018C1794F690, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 660>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              66 (check_event_contract_has_pas188_types)

 675           LOAD_CONST              52 (<code object __annotate__ at 0x0000018C181146C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 675>)
               MAKE_FUNCTION
               LOAD_CONST              53 (<code object check_main_mounts_incidents_router at 0x0000018C1794F860, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 675>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              67 (check_main_mounts_incidents_router)

 690           LOAD_CONST              54 (<code object __annotate__ at 0x0000018C181147B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 690>)
               MAKE_FUNCTION
               LOAD_CONST              55 (<code object check_operator_incidents_route_invariants at 0x0000018C17D51060, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 690>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              68 (check_operator_incidents_route_invariants)

 738           LOAD_CONST              56 (<code object __annotate__ at 0x0000018C18114990, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 738>)
               MAKE_FUNCTION
               LOAD_CONST              57 (<code object check_daily_runner_no_scheduler at 0x0000018C17EC5380, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 738>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              69 (check_daily_runner_no_scheduler)

 753           LOAD_CONST              58 (<code object __annotate__ at 0x0000018C18114A80, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 753>)
               MAKE_FUNCTION
               LOAD_CONST              59 (<code object check_migration_runner_does_not_execute at 0x0000018C17EC4280, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 753>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              70 (check_migration_runner_does_not_execute)

 768           LOAD_CONST              60 (<code object __annotate__ at 0x0000018C18114B70, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 768>)
               MAKE_FUNCTION
               LOAD_CONST              61 (<code object check_self_no_env_or_db at 0x0000018C17EA3D00, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 768>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              71 (check_self_no_env_or_db)

 816           LOAD_CONST              62 (<code object __annotate__ at 0x0000018C18114C60, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 816>)
               MAKE_FUNCTION
               LOAD_CONST              63 (<code object _aggregate at 0x0000018C1800B0A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 816>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              72 (_aggregate)

 825           LOAD_CONST              64 (<code object __annotate__ at 0x0000018C18114D50, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 825>)
               MAKE_FUNCTION
               LOAD_CONST              65 (<code object _operator_actions at 0x0000018C18048AB0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 825>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              73 (_operator_actions)

 835           LOAD_CONST              66 (<code object __annotate__ at 0x0000018C18114E40, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 835>)
               MAKE_FUNCTION
               LOAD_CONST              67 (<code object evaluate at 0x0000018C182EA5C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 835>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              74 (evaluate)

 872           LOAD_CONST              68 ('pas188_operational_scaling_readiness_report.json')
               STORE_NAME              75 (REPORT_FILENAME)

 875           LOAD_CONST              69 (<code object __annotate__ at 0x0000018C18114F30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 875>)
               MAKE_FUNCTION
               LOAD_CONST              70 (<code object _build_parser at 0x0000018C179C3A50, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 875>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              76 (_build_parser)

 892           LOAD_CONST              71 (<code object __annotate__ at 0x0000018C18115020, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 892>)
               MAKE_FUNCTION
               LOAD_CONST              72 (<code object _print_summary at 0x0000018C17D8C5C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 892>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              77 (_print_summary)

 910           LOAD_CONST              73 (<code object __annotate__ at 0x0000018C18026030, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 910>)
               MAKE_FUNCTION
               LOAD_CONST              74 (<code object _write_report at 0x0000018C180FC990, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 910>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              78 (_write_report)

 924           LOAD_CONST              97 ((None,))
               LOAD_CONST              75 (<code object __annotate__ at 0x0000018C18114030, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 924>)
               MAKE_FUNCTION
               LOAD_CONST              76 (<code object main at 0x0000018C17D88C40, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 924>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              79 (main)

 949           LOAD_NAME               80 (__name__)
               LOAD_CONST              77 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 950           LOAD_NAME                6 (sys)
               LOAD_ATTR              162 (exit)
               PUSH_NULL
               LOAD_NAME               79 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 949   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  67           LOAD_NAME               18 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  68   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          383 (to L1)

  67   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025F30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 371>:
371           RESUME                   0
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

Disassembly of <code object _check at 0x0000018C17FA34B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 371>:
371           RESUME                   0

373           LOAD_CONST               0 ('id')
              LOAD_FAST_BORROW         0 (check_id)

374           LOAD_CONST               1 ('status')
              LOAD_FAST_BORROW         1 (status)

375           LOAD_CONST               2 ('label')
              LOAD_FAST_BORROW         2 (label)

376           LOAD_CONST               3 ('severity')
              LOAD_FAST_BORROW         3 (severity)

377           LOAD_CONST               4 ('detail')
              LOAD_FAST_BORROW         4 (detail)

372           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 381>:
381           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038170, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 381>:
381           RESUME                   0

382           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 385>:
385           RESUME                   0
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

Disassembly of <code object _read_text at 0x0000018C18053E10, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 385>:
 385           RESUME                   0

 386           NOP

 387   L1:     LOAD_FAST_BORROW         0 (path)
               LOAD_ATTR                1 (read_text + NULL|self)
               LOAD_CONST               0 ('utf-8')
               LOAD_CONST               1 ('replace')
               LOAD_CONST               2 (('encoding', 'errors'))
               CALL_KW                  2
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 388           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 389   L4:     POP_EXCEPT
               LOAD_CONST               3 (None)
               RETURN_VALUE

 388   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 392>:
392           RESUME                   0
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

Disassembly of <code object _strip_python_comments_and_strings at 0x0000018C17E923B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 392>:
392            RESUME                   0

395            BUILD_LIST               0
               STORE_FAST               1 (out)

396            LOAD_SMALL_INT           0
               LOAD_GLOBAL              1 (len + NULL)
               LOAD_FAST_BORROW         0 (src)
               CALL                     1
               STORE_FAST_STORE_FAST   50 (n, i)

397    L1:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (i, n)
               COMPARE_OP              18 (bool(<))
               EXTENDED_ARG             1
               POP_JUMP_IF_FALSE      282 (to L13)
               NOT_TAKEN

398            LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               BINARY_OP               26 ([])
               STORE_FAST               4 (ch)

399            LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               1 ('#')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       38 (to L3)
               NOT_TAKEN

400            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_CONST               2 ('\n')
               LOAD_FAST_BORROW         2 (i)
               CALL                     2
               STORE_FAST               5 (j)

401            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L2)
               NOT_TAKEN

402            JUMP_FORWARD           240 (to L13)

403    L2:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

404            JUMP_BACKWARD           59 (to L1)

405    L3:     LOAD_FAST_BORROW         0 (src)
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

406    L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               BINARY_SLICE
               STORE_FAST               6 (quote)

407            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 98 (quote, i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               CALL                     2
               STORE_FAST               7 (end)

408            LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L5)
               NOT_TAKEN

409            JUMP_FORWARD           138 (to L13)

410    L5:     LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

411            JUMP_BACKWARD          161 (to L1)

412    L6:     LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               7 (('"', "'"))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       92 (to L12)
               NOT_TAKEN

413            LOAD_FAST                4 (ch)
               STORE_FAST               6 (quote)

414            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               5 (j)

415    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (j, n)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       63 (to L11)
               NOT_TAKEN

416            LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
               BINARY_OP               26 ([])
               LOAD_CONST               5 ('\\')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       12 (to L8)
               NOT_TAKEN

417            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           2
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)

418            JUMP_BACKWARD           30 (to L7)

419    L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
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

420    L9:     JUMP_FORWARD            11 (to L11)

421   L10:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)
               JUMP_BACKWARD           68 (to L7)

422   L11:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

423            EXTENDED_ARG             1
               JUMP_BACKWARD          259 (to L1)

424   L12:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (ch)
               CALL                     1
               POP_TOP

425            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               2 (i)
               EXTENDED_ARG             1
               JUMP_BACKWARD          288 (to L1)

426   L13:     LOAD_CONST               6 ('')
               LOAD_ATTR                9 (join + NULL|self)
               LOAD_FAST_BORROW         1 (out)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 433>:
433           RESUME                   0
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

Disassembly of <code object check_pas188_files_present at 0x0000018C18060F60, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 433>:
433           RESUME                   0

434           BUILD_LIST               0
              STORE_FAST               1 (out)

435           LOAD_GLOBAL              0 (PAS188_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

436           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

437           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

438           LOAD_CONST               0 ('file:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

439           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

440   L3:     LOAD_CONST               3 ('Required PAS188 artefact present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

441           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing')

437   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

435   L6:     END_FOR
              POP_ITER

443           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 446>:
446           RESUME                   0
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

Disassembly of <code object check_prior_phases_intact at 0x0000018C180606F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 446>:
446           RESUME                   0

447           BUILD_LIST               0
              STORE_FAST               1 (out)

448           LOAD_GLOBAL              0 (PRIOR_PHASE_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

449           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

450           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

451           LOAD_CONST               0 ('prior_phase:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

452           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

453   L3:     LOAD_CONST               3 ('Prior-phase readiness script intact: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

454           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing — PAS188 must not delete')

450   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

448   L6:     END_FOR
              POP_ITER

456           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 459>:
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

Disassembly of <code object check_memory_review_intact at 0x0000018C18061110, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 459>:
459           RESUME                   0

460           BUILD_LIST               0
              STORE_FAST               1 (out)

461           LOAD_GLOBAL              0 (MEMORY_REVIEW_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

462           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

463           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

464           LOAD_CONST               0 ('memory_review:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

465           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

466   L3:     LOAD_CONST               3 ('Memory Review file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

467           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('Memory Review file deleted — PAS188 must not touch')

463   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

461   L6:     END_FOR
              POP_ITER

469           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA30F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 472>:
472           RESUME                   0
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

Disassembly of <code object check_worker_off_by_default at 0x0000018C1794EBB0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 472>:
472           RESUME                   0

473           LOAD_GLOBAL              1 (Path + NULL)
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

474           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         1 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               2 (src)

476           LOAD_CONST               5 ('_ENV_FLAG_ENABLED_LITERAL = "true"')
              LOAD_FAST_BORROW         2 (src)
              CONTAINS_OP              0 (in)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         6 (to L2)
              NOT_TAKEN
              POP_TOP

477           LOAD_CONST               6 ("_ENV_FLAG_ENABLED_LITERAL = 'true'")
              LOAD_FAST_BORROW         2 (src)
              CONTAINS_OP              0 (in)

475   L2:     STORE_FAST               3 (ok)

479           LOAD_GLOBAL              5 (_check + NULL)

480           LOAD_CONST               7 ('worker:off_by_default')

481           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               8 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               9 ('FAIL')

482   L4:     LOAD_CONST              10 ('Pending-call worker is OFF by default')

483           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        9 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')

479           LOAD_CONST              12 (('detail',))
              CALL_KW                  4
              BUILD_LIST               1
              RETURN_VALUE

483   L5:     LOAD_CONST              11 ('missing strict enable-literal constant')

479           LOAD_CONST              12 (('detail',))
              CALL_KW                  4
              BUILD_LIST               1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3F00, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 487>:
487           RESUME                   0
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

Disassembly of <code object check_doc_required_clauses at 0x0000018C17D8AAB0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 487>:
  --            MAKE_CELL                9 (lower)

 487            RESUME                   0

 488            BUILD_LIST               0
                STORE_FAST               1 (out)

 489            LOAD_GLOBAL              0 (DOC_REQUIRED_CLAUSES)
                GET_ITER
        L1:     FOR_ITER               208 (to L14)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   35 (relpath, clauses)

 490            LOAD_GLOBAL              3 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_FAST_BORROW         2 (relpath)
                BINARY_OP               11 (/)
                STORE_FAST               4 (fp)

 491            LOAD_GLOBAL              5 (_read_text + NULL)
                LOAD_FAST_BORROW         4 (fp)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L2)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               0 ('')
        L2:     STORE_FAST               5 (src)

 492            LOAD_FAST_BORROW         5 (src)
                LOAD_ATTR                7 (lower + NULL|self)
                CALL                     0
                STORE_DEREF              9 (lower)

 493            LOAD_FAST_BORROW         3 (clauses)
                GET_ITER
        L3:     FOR_ITER               142 (to L13)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST  103 (name, phrases)

 494            LOAD_GLOBAL              8 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L7)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         9 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               1 (<code object <genexpr> at 0x0000018C18025E30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 494>)
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
                LOAD_CONST               1 (<code object <genexpr> at 0x0000018C18025E30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 494>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         7 (phrases)
                GET_ITER
                CALL                     0
                CALL                     1
        L8:     STORE_FAST               8 (present)

 495            LOAD_FAST                1 (out)
                LOAD_ATTR               11 (append + NULL|self)
                LOAD_GLOBAL             13 (_check + NULL)

 496            LOAD_CONST               4 ('doc:')
                LOAD_FAST_BORROW         2 (relpath)
                FORMAT_SIMPLE
                LOAD_CONST               5 (':clause:')
                LOAD_FAST_BORROW         6 (name)
                FORMAT_SIMPLE
                BUILD_STRING             4

 497            LOAD_FAST_BORROW         8 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L9)
                NOT_TAKEN
                LOAD_CONST               6 ('PASS')
                JUMP_FORWARD             1 (to L10)
        L9:     LOAD_CONST               7 ('FAIL')

 498   L10:     LOAD_FAST_BORROW         2 (relpath)
                FORMAT_SIMPLE
                LOAD_CONST               8 (' carries clause: ')
                LOAD_FAST_BORROW         6 (name)
                FORMAT_SIMPLE
                BUILD_STRING             3

 499            LOAD_FAST_BORROW         8 (present)
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

 495   L12:     LOAD_CONST              11 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          144 (to L3)

 493   L13:     END_FOR
                POP_ITER
                JUMP_BACKWARD          210 (to L1)

 489   L14:     END_FOR
                POP_ITER

 501            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18025E30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 494>:
  --           COPY_FREE_VARS           1

 494           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 504>:
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

Disassembly of <code object check_doc_no_forbidden_scope at 0x0000018C17ECE220, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 504>:
 504            RESUME                   0

 505            BUILD_LIST               0
                STORE_FAST               1 (out)

 506            LOAD_GLOBAL              0 (DOC_REQUIRED_CLAUSES)
                GET_ITER
        L1:     FOR_ITER               165 (to L13)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   35 (relpath, _)

 507            LOAD_GLOBAL              3 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_FAST_BORROW         2 (relpath)
                BINARY_OP               11 (/)
                STORE_FAST               4 (fp)

 508            LOAD_GLOBAL              5 (_read_text + NULL)
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

 509            LOAD_GLOBAL              8 (FORBIDDEN_DOC_TOKENS)
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

 510            LOAD_FAST                1 (out)
                LOAD_ATTR               11 (append + NULL|self)
                LOAD_GLOBAL             13 (_check + NULL)

 511            LOAD_CONST               1 ('doc_scope:')
                LOAD_FAST_BORROW         2 (relpath)
                FORMAT_SIMPLE
                BUILD_STRING             2

 512            LOAD_FAST_BORROW         7 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L9)
                NOT_TAKEN
                LOAD_CONST               2 ('FAIL')
                JUMP_FORWARD             1 (to L10)
        L9:     LOAD_CONST               3 ('PASS')

 513   L10:     LOAD_FAST_BORROW         2 (relpath)
                FORMAT_SIMPLE
                LOAD_CONST               4 (' introduces no out-of-scope feature token')
                BUILD_STRING             2

 514            LOAD_FAST_BORROW         7 (bad)
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

 510   L12:     LOAD_CONST               7 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          167 (to L1)

 506   L13:     END_FOR
                POP_ITER

 516            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L14:     SWAP                     2
                POP_TOP

 509            SWAP                     2
                STORE_FAST               6 (t)
                RERAISE                  0
ExceptionTable:
  L3 to L5 -> L14 [3]
  L6 to L8 -> L14 [3]

Disassembly of <code object __annotate__ at 0x0000018C17FA3000, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 519>:
519           RESUME                   0
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

Disassembly of <code object check_service_no_forbidden_imports at 0x0000018C17F78F70, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 519>:
519            RESUME                   0

520            BUILD_LIST               0
               STORE_FAST               1 (out)

521            LOAD_GLOBAL              0 (SERVICE_FILES)
               GET_ITER
       L1:     FOR_ITER               228 (to L12)
               STORE_FAST               2 (relpath)

522            LOAD_GLOBAL              3 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         2 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               3 (fp)

523            LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         3 (fp)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L2:     STORE_FAST               4 (src)

524            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         4 (src)
               CALL                     1
               STORE_FAST               5 (executable)

525            BUILD_LIST               0
               STORE_FAST               6 (bad)

526            LOAD_FAST_BORROW         5 (executable)
               LOAD_ATTR                9 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L3:     FOR_ITER                75 (to L7)
               STORE_FAST               7 (line)

527            LOAD_FAST_BORROW         7 (line)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0
               STORE_FAST               8 (stripped)

528            LOAD_GLOBAL             12 (FORBIDDEN_IMPORT_PREFIXES)
               GET_ITER
       L4:     FOR_ITER                46 (to L6)
               STORE_FAST               9 (pref)

529            LOAD_FAST_BORROW         8 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_FAST_BORROW         9 (pref)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           28 (to L4)

530    L5:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_FAST_BORROW         9 (pref)
               CALL                     1
               POP_TOP

531            POP_TOP
               JUMP_BACKWARD           73 (to L3)

528    L6:     END_FOR
               POP_ITER
               JUMP_BACKWARD           77 (to L3)

526    L7:     END_FOR
               POP_ITER

532            LOAD_FAST                1 (out)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_GLOBAL             19 (_check + NULL)

533            LOAD_CONST               1 ('service_imports:')
               LOAD_FAST_BORROW         2 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

534            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN
               LOAD_CONST               2 ('FAIL')
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST               3 ('PASS')

535    L9:     LOAD_FAST_BORROW         2 (relpath)
               FORMAT_SIMPLE
               LOAD_CONST               4 (' contains no forbidden import')
               BUILD_STRING             2

536            LOAD_FAST_BORROW         6 (bad)
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

532   L11:     LOAD_CONST               7 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          230 (to L1)

521   L12:     END_FOR
               POP_ITER

538            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114120, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 541>:
541           RESUME                   0
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

Disassembly of <code object check_service_no_scheduler_or_loop at 0x0000018C17ECE6C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 541>:
541            RESUME                   0

544            BUILD_LIST               0
               STORE_FAST               1 (out)

545            LOAD_CONST               9 (('app/services/operator/fleet_status_cache.py', 'app/services/operator/circuit_breaker.py', 'app/services/operator/incident_log.py', 'app/routes/operator_incidents.py'))
               STORE_FAST               2 (service_only)

551            LOAD_FAST_BORROW         2 (service_only)
               GET_ITER
       L1:     FOR_ITER               171 (to L10)
               STORE_FAST               3 (relpath)

552            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (fp)

553            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (fp)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L2:     STORE_FAST               5 (src)

554            LOAD_GLOBAL              5 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         5 (src)
               CALL                     1
               STORE_FAST               6 (executable)

555            BUILD_LIST               0
               STORE_FAST               7 (bad)

556            LOAD_GLOBAL              6 (FORBIDDEN_SERVICE_TOKENS)
               GET_ITER
       L3:     FOR_ITER                28 (to L5)
               STORE_FAST               8 (tok)

557            LOAD_FAST_BORROW_LOAD_FAST_BORROW 134 (tok, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L3)

558    L4:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_FAST_BORROW         8 (tok)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L3)

556    L5:     END_FOR
               POP_ITER

559            LOAD_FAST                1 (out)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_GLOBAL             11 (_check + NULL)

560            LOAD_CONST               2 ('service_scheduler:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

561            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L6)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L7)
       L6:     LOAD_CONST               4 ('PASS')

562    L7:     LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               LOAD_CONST               5 (' contains no scheduler / cron / autonomous loop')
               BUILD_STRING             2

563            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L8)
               NOT_TAKEN
               LOAD_CONST               6 ('disqualifying: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               13 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST               1 ('')

559    L9:     LOAD_CONST               8 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          173 (to L1)

551   L10:     END_FOR
               POP_ITER

565            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114210, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 568>:
568           RESUME                   0
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

Disassembly of <code object check_fleet_cache_invariants at 0x0000018C17F79230, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 568>:
 568            RESUME                   0

 569            BUILD_LIST               0
                STORE_FAST               1 (out)

 570            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('app/services/operator/fleet_status_cache.py')
                BINARY_OP               11 (/)
                STORE_FAST               2 (fp)

 571            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (fp)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               1 ('')
        L1:     STORE_FAST               3 (src)

 572            LOAD_GLOBAL              4 (FLEET_CACHE_REQUIRED_TOKENS)
                GET_ITER
        L2:     FOR_ITER                70 (to L7)
                STORE_FAST               4 (tok)

 573            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
                CONTAINS_OP              0 (in)
                STORE_FAST               5 (ok)

 574            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 575            LOAD_CONST               2 ('fleet_cache:token:')
                LOAD_FAST_BORROW         4 (tok)
                LOAD_CONST               3 (slice(None, 60, None))
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                BUILD_STRING             2

 576            LOAD_FAST_BORROW         5 (ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L3)
                NOT_TAKEN
                LOAD_CONST               4 ('PASS')
                JUMP_FORWARD             1 (to L4)
        L3:     LOAD_CONST               5 ('FAIL')

 577    L4:     LOAD_CONST               6 ('fleet_status_cache.py carries: ')
                LOAD_FAST_BORROW         4 (tok)
                FORMAT_SIMPLE
                BUILD_STRING             2

 578            LOAD_FAST_BORROW         5 (ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN
                LOAD_CONST               1 ('')
                JUMP_FORWARD             1 (to L6)
        L5:     LOAD_CONST               7 ('token missing')

 574    L6:     LOAD_CONST               8 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           72 (to L2)

 572    L7:     END_FOR
                POP_ITER

 580            LOAD_GLOBAL             11 (_strip_python_comments_and_strings + NULL)
                LOAD_FAST_BORROW         3 (src)
                CALL                     1
                STORE_FAST               6 (executable)

 581            LOAD_GLOBAL             12 (FLEET_CACHE_FORBIDDEN_TOKENS)
                GET_ITER
                LOAD_FAST_AND_CLEAR      7 (t)
                SWAP                     2
        L8:     BUILD_LIST               0
                SWAP                     2
        L9:     FOR_ITER                13 (to L12)
                STORE_FAST_LOAD_FAST   119 (t, t)
                LOAD_FAST_BORROW         6 (executable)
                CONTAINS_OP              0 (in)
       L10:     POP_JUMP_IF_TRUE         3 (to L11)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L9)
       L11:     LOAD_FAST_BORROW         7 (t)
                LIST_APPEND              2
                JUMP_BACKWARD           15 (to L9)
       L12:     END_FOR
                POP_ITER
       L13:     STORE_FAST               8 (bad)
                STORE_FAST               7 (t)

 582            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 583            LOAD_CONST               9 ('fleet_cache:no_autonomous_warming')

 584            LOAD_FAST_BORROW         8 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L14)
                NOT_TAKEN
                LOAD_CONST               5 ('FAIL')
                JUMP_FORWARD             1 (to L15)
       L14:     LOAD_CONST               4 ('PASS')

 585   L15:     LOAD_CONST              10 ('fleet_status_cache.py contains no autonomous warming pattern')

 586            LOAD_FAST_BORROW         8 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L16)
                NOT_TAKEN
                LOAD_CONST              11 ('disqualifying: ')
                LOAD_CONST              12 (', ')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_FAST_BORROW         8 (bad)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L17)
       L16:     LOAD_CONST               1 ('')

 582   L17:     LOAD_CONST               8 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 588            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L18:     SWAP                     2
                POP_TOP

 581            SWAP                     2
                STORE_FAST               7 (t)
                RERAISE                  0
ExceptionTable:
  L8 to L10 -> L18 [2]
  L11 to L13 -> L18 [2]

Disassembly of <code object __annotate__ at 0x0000018C18114300, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 591>:
591           RESUME                   0
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

Disassembly of <code object check_circuit_breaker_invariants at 0x0000018C17F78730, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 591>:
 591            RESUME                   0

 592            BUILD_LIST               0
                STORE_FAST               1 (out)

 593            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('app/services/operator/circuit_breaker.py')
                BINARY_OP               11 (/)
                STORE_FAST               2 (fp)

 594            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (fp)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               1 ('')
        L1:     STORE_FAST               3 (src)

 595            LOAD_GLOBAL              4 (CIRCUIT_BREAKER_REQUIRED_TOKENS)
                GET_ITER
        L2:     FOR_ITER                70 (to L7)
                STORE_FAST               4 (tok)

 596            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
                CONTAINS_OP              0 (in)
                STORE_FAST               5 (ok)

 597            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 598            LOAD_CONST               2 ('circuit_breaker:token:')
                LOAD_FAST_BORROW         4 (tok)
                LOAD_CONST               3 (slice(None, 60, None))
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                BUILD_STRING             2

 599            LOAD_FAST_BORROW         5 (ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L3)
                NOT_TAKEN
                LOAD_CONST               4 ('PASS')
                JUMP_FORWARD             1 (to L4)
        L3:     LOAD_CONST               5 ('FAIL')

 600    L4:     LOAD_CONST               6 ('circuit_breaker.py carries: ')
                LOAD_FAST_BORROW         4 (tok)
                FORMAT_SIMPLE
                BUILD_STRING             2

 601            LOAD_FAST_BORROW         5 (ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN
                LOAD_CONST               1 ('')
                JUMP_FORWARD             1 (to L6)
        L5:     LOAD_CONST               7 ('token missing')

 597    L6:     LOAD_CONST               8 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           72 (to L2)

 595    L7:     END_FOR
                POP_ITER

 603            LOAD_GLOBAL             11 (_strip_python_comments_and_strings + NULL)
                LOAD_FAST_BORROW         3 (src)
                CALL                     1
                STORE_FAST               6 (executable)

 604            LOAD_GLOBAL             12 (CIRCUIT_BREAKER_FORBIDDEN_TOKENS)
                GET_ITER
                LOAD_FAST_AND_CLEAR      7 (t)
                SWAP                     2
        L8:     BUILD_LIST               0
                SWAP                     2
        L9:     FOR_ITER                13 (to L12)
                STORE_FAST_LOAD_FAST   119 (t, t)
                LOAD_FAST_BORROW         6 (executable)
                CONTAINS_OP              0 (in)
       L10:     POP_JUMP_IF_TRUE         3 (to L11)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L9)
       L11:     LOAD_FAST_BORROW         7 (t)
                LIST_APPEND              2
                JUMP_BACKWARD           15 (to L9)
       L12:     END_FOR
                POP_ITER
       L13:     STORE_FAST               8 (bad)
                STORE_FAST               7 (t)

 605            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 606            LOAD_CONST               9 ('circuit_breaker:no_external_mutation')

 607            LOAD_FAST_BORROW         8 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L14)
                NOT_TAKEN
                LOAD_CONST               5 ('FAIL')
                JUMP_FORWARD             1 (to L15)
       L14:     LOAD_CONST               4 ('PASS')

 608   L15:     LOAD_CONST              10 ('circuit_breaker.py does NOT mutate Twilio / Cal.com / etc')

 609            LOAD_FAST_BORROW         8 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L16)
                NOT_TAKEN
                LOAD_CONST              11 ('disqualifying: ')
                LOAD_CONST              12 (', ')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_FAST_BORROW         8 (bad)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L17)
       L16:     LOAD_CONST               1 ('')

 605   L17:     LOAD_CONST               8 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 611            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L18:     SWAP                     2
                POP_TOP

 604            SWAP                     2
                STORE_FAST               7 (t)
                RERAISE                  0
ExceptionTable:
  L8 to L10 -> L18 [2]
  L11 to L13 -> L18 [2]

Disassembly of <code object __annotate__ at 0x0000018C181143F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 614>:
614           RESUME                   0
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

Disassembly of <code object check_incident_log_invariants at 0x0000018C182DA010, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 614>:
 614            RESUME                   0

 615            BUILD_LIST               0
                STORE_FAST               1 (out)

 616            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('app/services/operator/incident_log.py')
                BINARY_OP               11 (/)
                STORE_FAST               2 (fp)

 617            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (fp)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               1 ('')
        L1:     STORE_FAST               3 (src)

 618            LOAD_GLOBAL              4 (INCIDENT_LOG_REQUIRED_TOKENS)
                GET_ITER
        L2:     FOR_ITER                70 (to L7)
                STORE_FAST               4 (tok)

 619            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
                CONTAINS_OP              0 (in)
                STORE_FAST               5 (ok)

 620            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 621            LOAD_CONST               2 ('incident_log:token:')
                LOAD_FAST_BORROW         4 (tok)
                LOAD_CONST               3 (slice(None, 60, None))
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                BUILD_STRING             2

 622            LOAD_FAST_BORROW         5 (ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L3)
                NOT_TAKEN
                LOAD_CONST               4 ('PASS')
                JUMP_FORWARD             1 (to L4)
        L3:     LOAD_CONST               5 ('FAIL')

 623    L4:     LOAD_CONST               6 ('incident_log.py carries: ')
                LOAD_FAST_BORROW         4 (tok)
                FORMAT_SIMPLE
                BUILD_STRING             2

 624            LOAD_FAST_BORROW         5 (ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN
                LOAD_CONST               1 ('')
                JUMP_FORWARD             1 (to L6)
        L5:     LOAD_CONST               7 ('token missing')

 620    L6:     LOAD_CONST               8 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           72 (to L2)

 618    L7:     END_FOR
                POP_ITER

 626            LOAD_GLOBAL             11 (_strip_python_comments_and_strings + NULL)
                LOAD_FAST_BORROW         3 (src)
                CALL                     1
                STORE_FAST               6 (executable)

 627            LOAD_GLOBAL             12 (INCIDENT_LOG_FORBIDDEN_TOKENS)
                GET_ITER
                LOAD_FAST_AND_CLEAR      7 (t)
                SWAP                     2
        L8:     BUILD_LIST               0
                SWAP                     2
        L9:     FOR_ITER                13 (to L12)
                STORE_FAST_LOAD_FAST   119 (t, t)
                LOAD_FAST_BORROW         6 (executable)
                CONTAINS_OP              0 (in)
       L10:     POP_JUMP_IF_TRUE         3 (to L11)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L9)
       L11:     LOAD_FAST_BORROW         7 (t)
                LIST_APPEND              2
                JUMP_BACKWARD           15 (to L9)
       L12:     END_FOR
                POP_ITER
       L13:     STORE_FAST               8 (bad)
                STORE_FAST               7 (t)

 628            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 629            LOAD_CONST               9 ('incident_log:no_autonomous_opener')

 630            LOAD_FAST_BORROW         8 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L14)
                NOT_TAKEN
                LOAD_CONST               5 ('FAIL')
                JUMP_FORWARD             1 (to L15)
       L14:     LOAD_CONST               4 ('PASS')

 631   L15:     LOAD_CONST              10 ('incident_log.py does NOT define an autonomous opener')

 632            LOAD_FAST_BORROW         8 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L16)
                NOT_TAKEN
                LOAD_CONST              11 ('disqualifying: ')
                LOAD_CONST              12 (', ')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_FAST_BORROW         8 (bad)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L17)
       L16:     LOAD_CONST               1 ('')

 628   L17:     LOAD_CONST               8 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 636            LOAD_CONST              13 ('def delete_incident')
                LOAD_FAST_BORROW         3 (src)
                CONTAINS_OP              0 (in)
                STORE_FAST               9 (has_delete)

 637            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 638            LOAD_CONST              14 ('incident_log:no_delete_function')

 639            LOAD_FAST_BORROW         9 (has_delete)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L18)
                NOT_TAKEN
                LOAD_CONST               5 ('FAIL')
                JUMP_FORWARD             1 (to L19)
       L18:     LOAD_CONST               4 ('PASS')

 640   L19:     LOAD_CONST              15 ('incident_log.py exports no delete function (append-only doctrine)')

 641            LOAD_FAST_BORROW         9 (has_delete)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L20)
                NOT_TAKEN
                LOAD_CONST              16 ('found def delete_incident')
                JUMP_FORWARD             1 (to L21)
       L20:     LOAD_CONST               1 ('')

 637   L21:     LOAD_CONST               8 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 643            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L22:     SWAP                     2
                POP_TOP

 627            SWAP                     2
                STORE_FAST               7 (t)
                RERAISE                  0
ExceptionTable:
  L8 to L10 -> L22 [2]
  L11 to L13 -> L22 [2]

Disassembly of <code object __annotate__ at 0x0000018C181144E0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 646>:
646           RESUME                   0
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

Disassembly of <code object check_dashboard_anchors_present at 0x0000018C1794E810, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 646>:
646           RESUME                   0

647           BUILD_LIST               0
              STORE_FAST               1 (out)

648           LOAD_GLOBAL              1 (_read_text + NULL)
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

649           LOAD_GLOBAL              6 (DASHBOARD_REQUIRED_ANCHORS)
              GET_ITER
      L2:     FOR_ITER                65 (to L7)
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST   52 (cid, needle)

650           LOAD_FAST_BORROW_LOAD_FAST_BORROW 66 (needle, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

651           LOAD_FAST                1 (out)
              LOAD_ATTR                9 (append + NULL|self)
              LOAD_GLOBAL             11 (_check + NULL)

652           LOAD_CONST               1 ('dashboard:')
              LOAD_FAST_BORROW         3 (cid)
              FORMAT_SIMPLE
              BUILD_STRING             2

653           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               2 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               3 ('FAIL')

654   L4:     LOAD_CONST               4 ('Dashboard anchor present: ')
              LOAD_FAST_BORROW         4 (needle)
              FORMAT_SIMPLE
              BUILD_STRING             2

655           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               0 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               5 ('anchor missing')

651   L6:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           67 (to L2)

649   L7:     END_FOR
              POP_ITER

657           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181145D0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 660>:
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

Disassembly of <code object check_event_contract_has_pas188_types at 0x0000018C1794F690, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 660>:
660           RESUME                   0

661           BUILD_LIST               0
              STORE_FAST               1 (out)

662           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_GLOBAL              2 (EVENT_CONTRACT_FILE)
              BINARY_OP               11 (/)
              STORE_FAST               2 (fp)

663           LOAD_GLOBAL              5 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (fp)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               0 ('')
      L1:     STORE_FAST               3 (src)

664           LOAD_GLOBAL              6 (EVENT_CONTRACT_REQUIRED_EVENT_TYPES)
              GET_ITER
      L2:     FOR_ITER                63 (to L7)
              STORE_FAST               4 (tok)

665           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

666           LOAD_FAST                1 (out)
              LOAD_ATTR                9 (append + NULL|self)
              LOAD_GLOBAL             11 (_check + NULL)

667           LOAD_CONST               1 ('contract:event:')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

668           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               2 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               3 ('FAIL')

669   L4:     LOAD_CONST               4 ('events/contract.py carries event_type literal: ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

670           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               0 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               5 ('literal missing — contract drift')

666   L6:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           65 (to L2)

664   L7:     END_FOR
              POP_ITER

672           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181146C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 675>:
675           RESUME                   0
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

Disassembly of <code object check_main_mounts_incidents_router at 0x0000018C1794F860, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 675>:
675           RESUME                   0

676           BUILD_LIST               0
              STORE_FAST               1 (out)

677           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app/main.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (fp)

678           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (fp)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 ('')
      L1:     STORE_FAST               3 (src)

679           LOAD_GLOBAL              4 (MAIN_PY_REQUIRED_MOUNT_TOKENS)
              GET_ITER
      L2:     FOR_ITER                70 (to L7)
              STORE_FAST               4 (tok)

680           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

681           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

682           LOAD_CONST               2 ('main:mount:')
              LOAD_FAST_BORROW         4 (tok)
              LOAD_CONST               3 (slice(None, 60, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

683           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               4 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               5 ('FAIL')

684   L4:     LOAD_CONST               6 ('app/main.py contains: ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

685           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               1 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               7 ('mount missing — route inaccessible')

681   L6:     LOAD_CONST               8 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           72 (to L2)

679   L7:     END_FOR
              POP_ITER

687           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181147B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 690>:
690           RESUME                   0
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

Disassembly of <code object check_operator_incidents_route_invariants at 0x0000018C17D51060, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 690>:
 690            RESUME                   0

 691            BUILD_LIST               0
                STORE_FAST               1 (out)

 692            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_GLOBAL              2 (CUTOVER_ROUTE_FILE)
                BINARY_OP               11 (/)
                STORE_FAST               2 (fp)

 693            LOAD_GLOBAL              5 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (fp)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               0 ('')
        L1:     STORE_FAST               3 (src)

 695            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 696            LOAD_CONST               1 ('incidents_route:require_admin')

 697            LOAD_CONST               2 ('def require_admin')
                LOAD_FAST_BORROW         3 (src)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L2)
                NOT_TAKEN
                LOAD_CONST               3 ('PASS')
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               4 ('FAIL')

 698    L3:     LOAD_GLOBAL              2 (CUTOVER_ROUTE_FILE)
                FORMAT_SIMPLE
                LOAD_CONST               5 (' declares require_admin dependency')
                BUILD_STRING             2

 699            LOAD_CONST               2 ('def require_admin')
                LOAD_FAST_BORROW         3 (src)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L4)
                NOT_TAKEN
                LOAD_CONST               0 ('')
                JUMP_FORWARD             1 (to L5)
        L4:     LOAD_CONST               6 ('require_admin missing')

 695    L5:     LOAD_CONST               7 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 702            LOAD_CONST               8 ('check_rate_limit')
                LOAD_FAST_BORROW         3 (src)
                CONTAINS_OP              0 (in)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        6 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               9 ('surface="admin"')
                LOAD_FAST_BORROW         3 (src)
                CONTAINS_OP              0 (in)
        L6:     STORE_FAST               4 (rl_ok)

 703            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 704            LOAD_CONST              10 ('incidents_route:rate_limit')

 705            LOAD_FAST_BORROW         4 (rl_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L7)
                NOT_TAKEN
                LOAD_CONST               3 ('PASS')
                JUMP_FORWARD             1 (to L8)
        L7:     LOAD_CONST               4 ('FAIL')

 706    L8:     LOAD_GLOBAL              2 (CUTOVER_ROUTE_FILE)
                FORMAT_SIMPLE
                LOAD_CONST              11 (' wires PAS-SECURITY-04 rate limit')
                BUILD_STRING             2

 707            LOAD_FAST_BORROW         4 (rl_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L9)
                NOT_TAKEN
                LOAD_CONST               0 ('')
                JUMP_FORWARD             1 (to L10)
        L9:     LOAD_CONST              12 ('rate_limit / surface=admin missing')

 703   L10:     LOAD_CONST               7 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 710            LOAD_GLOBAL             11 (_strip_python_comments_and_strings + NULL)
                LOAD_FAST_BORROW         3 (src)
                CALL                     1
                STORE_FAST               5 (executable)

 711            LOAD_CONST              21 (('/tenant/', 'tenant_router', 'X-API-Key'))
                GET_ITER
                LOAD_FAST_AND_CLEAR      6 (t)
                SWAP                     2
       L11:     BUILD_LIST               0
                SWAP                     2
       L12:     FOR_ITER                13 (to L15)
                STORE_FAST_LOAD_FAST   102 (t, t)
                LOAD_FAST_BORROW         5 (executable)
                CONTAINS_OP              0 (in)
       L13:     POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L12)
       L14:     LOAD_FAST_BORROW         6 (t)
                LIST_APPEND              2
                JUMP_BACKWARD           15 (to L12)
       L15:     END_FOR
                POP_ITER
       L16:     STORE_FAST               7 (bad)
                STORE_FAST               6 (t)

 712            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 713            LOAD_CONST              13 ('incidents_route:no_tenant_surface')

 714            LOAD_FAST_BORROW         7 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L17)
                NOT_TAKEN
                LOAD_CONST               4 ('FAIL')
                JUMP_FORWARD             1 (to L18)
       L17:     LOAD_CONST               3 ('PASS')

 715   L18:     LOAD_GLOBAL              2 (CUTOVER_ROUTE_FILE)
                FORMAT_SIMPLE
                LOAD_CONST              14 (' declares no tenant surface')
                BUILD_STRING             2

 716            LOAD_FAST_BORROW         7 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L19)
                NOT_TAKEN
                LOAD_CONST              15 ('disqualifying: ')
                LOAD_CONST              16 (', ')
                LOAD_ATTR               13 (join + NULL|self)
                LOAD_FAST_BORROW         7 (bad)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L20)
       L19:     LOAD_CONST               0 ('')

 712   L20:     LOAD_CONST               7 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 719            LOAD_CONST              22 (('@router.get("/incidents")', '@router.post("/incidents/open")', '@router.post("/incidents/{incident_id}/status")', '@router.post("/incidents/{incident_id}/resolve")', '@router.get("/circuit-breakers")', '@router.post("/circuit-breakers/{brokerage_id}/trip")', '@router.post("/circuit-breakers/{brokerage_id}/reset")'))
                STORE_FAST               8 (required_endpoints)

 728            LOAD_FAST_BORROW         8 (required_endpoints)
                GET_ITER
       L21:     FOR_ITER                62 (to L26)
                STORE_FAST               9 (ep)

 729            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 730            LOAD_CONST              17 ('incidents_route:endpoint:')
                LOAD_FAST_BORROW         9 (ep)
                LOAD_CONST              18 (slice(None, 80, None))
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                BUILD_STRING             2

 731            LOAD_FAST_BORROW_LOAD_FAST_BORROW 147 (ep, src)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L22)
                NOT_TAKEN
                LOAD_CONST               3 ('PASS')
                JUMP_FORWARD             1 (to L23)
       L22:     LOAD_CONST               4 ('FAIL')

 732   L23:     LOAD_CONST              19 ('endpoint declared: ')
                LOAD_FAST_BORROW         9 (ep)
                FORMAT_SIMPLE
                BUILD_STRING             2

 733            LOAD_FAST_BORROW_LOAD_FAST_BORROW 147 (ep, src)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L24)
                NOT_TAKEN
                LOAD_CONST               0 ('')
                JUMP_FORWARD             1 (to L25)
       L24:     LOAD_CONST              20 ('endpoint missing')

 729   L25:     LOAD_CONST               7 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           64 (to L21)

 728   L26:     END_FOR
                POP_ITER

 735            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L27:     SWAP                     2
                POP_TOP

 711            SWAP                     2
                STORE_FAST               6 (t)
                RERAISE                  0
ExceptionTable:
  L11 to L13 -> L27 [2]
  L14 to L16 -> L27 [2]

Disassembly of <code object __annotate__ at 0x0000018C18114990, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 738>:
738           RESUME                   0
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

Disassembly of <code object check_daily_runner_no_scheduler at 0x0000018C17EC5380, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 738>:
 738            RESUME                   0

 739            BUILD_LIST               0
                STORE_FAST               1 (out)

 740            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('scripts/run_daily_ops_checklist_report.py')
                BINARY_OP               11 (/)
                STORE_FAST               2 (fp)

 741            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (fp)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               1 ('')
        L1:     STORE_FAST               3 (src)

 742            LOAD_GLOBAL              5 (_strip_python_comments_and_strings + NULL)
                LOAD_FAST_BORROW         3 (src)
                CALL                     1
                STORE_FAST               4 (executable)

 743            LOAD_GLOBAL              6 (FORBIDDEN_DAILY_RUNNER_TOKENS)
                GET_ITER
                LOAD_FAST_AND_CLEAR      5 (t)
                SWAP                     2
        L2:     BUILD_LIST               0
                SWAP                     2
        L3:     FOR_ITER                13 (to L6)
                STORE_FAST_LOAD_FAST    85 (t, t)
                LOAD_FAST_BORROW         4 (executable)
                CONTAINS_OP              0 (in)
        L4:     POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L3)
        L5:     LOAD_FAST_BORROW         5 (t)
                LIST_APPEND              2
                JUMP_BACKWARD           15 (to L3)
        L6:     END_FOR
                POP_ITER
        L7:     STORE_FAST               6 (bad)
                STORE_FAST               5 (t)

 744            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 745            LOAD_CONST               2 ('daily_runner:no_scheduler')

 746            LOAD_FAST_BORROW         6 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               3 ('FAIL')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               4 ('PASS')

 747    L9:     LOAD_CONST               5 ('run_daily_ops_checklist_report.py contains no scheduler / loop')

 748            LOAD_FAST_BORROW         6 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L10)
                NOT_TAKEN
                LOAD_CONST               6 ('disqualifying: ')
                LOAD_CONST               7 (', ')
                LOAD_ATTR               13 (join + NULL|self)
                LOAD_FAST_BORROW         6 (bad)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L11)
       L10:     LOAD_CONST               1 ('')

 744   L11:     LOAD_CONST               8 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 750            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L12:     SWAP                     2
                POP_TOP

 743            SWAP                     2
                STORE_FAST               5 (t)
                RERAISE                  0
ExceptionTable:
  L2 to L4 -> L12 [2]
  L5 to L7 -> L12 [2]

Disassembly of <code object __annotate__ at 0x0000018C18114A80, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 753>:
753           RESUME                   0
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

Disassembly of <code object check_migration_runner_does_not_execute at 0x0000018C17EC4280, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 753>:
 753            RESUME                   0

 754            BUILD_LIST               0
                STORE_FAST               1 (out)

 755            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('scripts/run_migration_promotion_checklist.py')
                BINARY_OP               11 (/)
                STORE_FAST               2 (fp)

 756            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (fp)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               1 ('')
        L1:     STORE_FAST               3 (src)

 757            LOAD_GLOBAL              5 (_strip_python_comments_and_strings + NULL)
                LOAD_FAST_BORROW         3 (src)
                CALL                     1
                STORE_FAST               4 (executable)

 758            LOAD_GLOBAL              6 (FORBIDDEN_MIGRATION_RUNNER_TOKENS)
                GET_ITER
                LOAD_FAST_AND_CLEAR      5 (t)
                SWAP                     2
        L2:     BUILD_LIST               0
                SWAP                     2
        L3:     FOR_ITER                13 (to L6)
                STORE_FAST_LOAD_FAST    85 (t, t)
                LOAD_FAST_BORROW         4 (executable)
                CONTAINS_OP              0 (in)
        L4:     POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L3)
        L5:     LOAD_FAST_BORROW         5 (t)
                LIST_APPEND              2
                JUMP_BACKWARD           15 (to L3)
        L6:     END_FOR
                POP_ITER
        L7:     STORE_FAST               6 (bad)
                STORE_FAST               5 (t)

 759            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 760            LOAD_CONST               2 ('migration_runner:no_execution')

 761            LOAD_FAST_BORROW         6 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               3 ('FAIL')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               4 ('PASS')

 762    L9:     LOAD_CONST               5 ('run_migration_promotion_checklist.py does NOT execute migrations or call Supabase')

 763            LOAD_FAST_BORROW         6 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L10)
                NOT_TAKEN
                LOAD_CONST               6 ('disqualifying: ')
                LOAD_CONST               7 (', ')
                LOAD_ATTR               13 (join + NULL|self)
                LOAD_FAST_BORROW         6 (bad)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L11)
       L10:     LOAD_CONST               1 ('')

 759   L11:     LOAD_CONST               8 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 765            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L12:     SWAP                     2
                POP_TOP

 758            SWAP                     2
                STORE_FAST               5 (t)
                RERAISE                  0
ExceptionTable:
  L2 to L4 -> L12 [2]
  L5 to L7 -> L12 [2]

Disassembly of <code object __annotate__ at 0x0000018C18114B70, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 768>:
768           RESUME                   0
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

Disassembly of <code object check_self_no_env_or_db at 0x0000018C17EA3D00, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 768>:
768            RESUME                   0

771            BUILD_LIST               0
               STORE_FAST               1 (out)

772            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_GLOBAL              2 (__file__)
               CALL                     1
               STORE_FAST               2 (fp)

773            LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (fp)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L1:     STORE_FAST               3 (src)

774            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               4 (executable)

775            BUILD_LIST               0
               STORE_FAST               5 (bad)

776            LOAD_FAST_BORROW         4 (executable)
               LOAD_ATTR                9 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L2:     FOR_ITER               199 (to L9)
               STORE_FAST               6 (line)

777            LOAD_FAST_BORROW         6 (line)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0
               STORE_FAST               7 (stripped)

778            LOAD_FAST_BORROW         7 (stripped)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN

779            JUMP_BACKWARD           29 (to L2)

780    L3:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              15 (('import dotenv', 'from dotenv'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L4)
               NOT_TAKEN

781            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               1 ('dotenv import')
               CALL                     1
               POP_TOP

782    L4:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              16 (('import supabase', 'from supabase'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L5)
               NOT_TAKEN

783            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               2 ('supabase import')
               CALL                     1
               POP_TOP

784    L5:     LOAD_CONST               3 ('load_dotenv(')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       18 (to L6)
               NOT_TAKEN

785            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               4 ('load_dotenv() call')
               CALL                     1
               POP_TOP

786    L6:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              17 (('os.environ[', 'getenv('))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L7)
               NOT_TAKEN

787            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               5 ('environ read')
               CALL                     1
               POP_TOP

788    L7:     LOAD_CONST               6 ('get_supabase')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD          182 (to L2)

789    L8:     LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               7 ('supabase client call')
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          201 (to L2)

776    L9:     END_FOR
               POP_ITER

790            LOAD_CONST              18 (('subprocess.run(', 'subprocess.call(', 'requests.get(', 'requests.post(', 'httpx.get(', 'httpx.post(', 'urllib.request.urlopen(', 'git push', 'railway deploy'))
               GET_ITER
      L10:     FOR_ITER                28 (to L12)
               STORE_FAST               8 (tok)

801            LOAD_FAST_BORROW_LOAD_FAST_BORROW 132 (tok, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L11)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L10)

802   L11:     LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_FAST_BORROW         8 (tok)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L10)

790   L12:     END_FOR
               POP_ITER

803            LOAD_FAST                1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             17 (_check + NULL)

804            LOAD_CONST               8 ('self_check:no_env_or_db_or_network')

805            LOAD_FAST_BORROW         5 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L13)
               NOT_TAKEN
               LOAD_CONST               9 ('FAIL')
               JUMP_FORWARD             1 (to L14)
      L13:     LOAD_CONST              10 ('PASS')

806   L14:     LOAD_CONST              11 ('PAS188 readiness checker never reads .env / touches DB / hits network')

807            LOAD_FAST_BORROW         5 (bad)
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

803   L16:     LOAD_CONST              14 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

809            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114C60, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 816>:
816           RESUME                   0
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

Disassembly of <code object _aggregate at 0x0000018C1800B0A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 816>:
 816            RESUME                   0

 817            LOAD_FAST_BORROW         0 (checks)
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

 819            LOAD_CONST               3 ('verdict')
                LOAD_FAST_BORROW         2 (blockers)
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L9)
                NOT_TAKEN
                LOAD_GLOBAL              4 (VERDICT_NOT_READY)
                JUMP_FORWARD             5 (to L10)
        L9:     LOAD_GLOBAL              6 (VERDICT_READY)

 820   L10:     LOAD_CONST               4 ('blockers')
                LOAD_FAST_BORROW         2 (blockers)

 821            LOAD_CONST               5 ('info')
                BUILD_LIST               0

 818            BUILD_MAP                3
                RETURN_VALUE

  --   L11:     SWAP                     2
                POP_TOP

 817            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L11 [2]
  L4 to L5 -> L11 [2]
  L6 to L8 -> L11 [2]

Disassembly of <code object __annotate__ at 0x0000018C18114D50, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 825>:
825           RESUME                   0
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

Disassembly of <code object _operator_actions at 0x0000018C18048AB0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 825>:
825           RESUME                   0

826           BUILD_LIST               0
              STORE_FAST               1 (out)

827           LOAD_FAST_BORROW         0 (checks)
              GET_ITER
      L1:     FOR_ITER               109 (to L5)
              STORE_FAST               2 (c)

828           LOAD_FAST_BORROW         2 (c)
              LOAD_CONST               0 ('status')
              BINARY_OP               26 ([])
              LOAD_CONST               1 ('FAIL')
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

829           JUMP_BACKWARD           19 (to L1)

830   L2:     LOAD_FAST_BORROW         2 (c)
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

831           LOAD_FAST                1 (out)
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

827   L5:     END_FOR
              POP_ITER

832           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114E40, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 835>:
835           RESUME                   0
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

Disassembly of <code object evaluate at 0x0000018C182EA5C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 835>:
835           RESUME                   0

836           BUILD_LIST               0
              STORE_FAST               1 (checks)

837           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              3 (check_pas188_files_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

838           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              5 (check_prior_phases_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

839           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              7 (check_memory_review_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

840           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              9 (check_worker_off_by_default + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

841           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             11 (check_doc_required_clauses + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

842           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             13 (check_doc_no_forbidden_scope + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

843           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             15 (check_service_no_forbidden_imports + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

844           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             17 (check_service_no_scheduler_or_loop + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

845           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             19 (check_fleet_cache_invariants + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

846           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             21 (check_circuit_breaker_invariants + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

847           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             23 (check_incident_log_invariants + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

848           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             25 (check_dashboard_anchors_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

849           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             27 (check_event_contract_has_pas188_types + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

850           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             29 (check_main_mounts_incidents_router + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

851           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             31 (check_operator_incidents_route_invariants + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

852           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             33 (check_daily_runner_no_scheduler + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

853           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             35 (check_migration_runner_does_not_execute + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

854           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             37 (check_self_no_env_or_db + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

856           LOAD_GLOBAL             39 (_aggregate + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1
              STORE_FAST               2 (agg)

858           LOAD_CONST               0 ('phase')
              LOAD_CONST               1 ('PAS188')

859           LOAD_CONST               2 ('generated_at')
              LOAD_GLOBAL             41 (_now_iso + NULL)
              CALL                     0

860           LOAD_CONST               3 ('verdict')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])

861           LOAD_CONST               4 ('ready')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])
              LOAD_GLOBAL             42 (VERDICT_READY)
              COMPARE_OP              72 (==)

862           LOAD_CONST               5 ('blocker_count')
              LOAD_GLOBAL             45 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               6 ('blockers')
              BINARY_OP               26 ([])
              CALL                     1

863           LOAD_CONST               7 ('info_count')
              LOAD_GLOBAL             45 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               8 ('info')
              BINARY_OP               26 ([])
              CALL                     1

864           LOAD_CONST               9 ('check_count')
              LOAD_GLOBAL             45 (len + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

865           LOAD_CONST              10 ('pass_count')
              LOAD_GLOBAL             47 (sum + NULL)
              LOAD_CONST              11 (<code object <genexpr> at 0x0000018C18128150, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 865>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

866           LOAD_CONST              12 ('fail_count')
              LOAD_GLOBAL             47 (sum + NULL)
              LOAD_CONST              13 (<code object <genexpr> at 0x0000018C181284B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 866>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

867           LOAD_CONST              14 ('checks')
              LOAD_FAST_BORROW         1 (checks)

868           LOAD_CONST              15 ('operator_actions')
              LOAD_GLOBAL             49 (_operator_actions + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

857           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18128150, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 865>:
 865           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C181284B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 866>:
 866           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C18114F30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 875>:
875           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C179C3A50, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 875>:
875           RESUME                   0

876           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

877           LOAD_CONST               0 ('pas188_operational_scaling_readiness_check')

879           LOAD_CONST               1 ('PAS188 — Operational scaling automation readiness gate. Read-only — never reads .env, never touches Supabase, never executes a deploy / migration.')

876           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

884           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               3 ('--repo-root')
              LOAD_GLOBAL              6 (_REPO_ROOT_DEFAULT)
              LOAD_CONST               4 (('default',))
              CALL_KW                  2
              POP_TOP

885           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               5 ('--output')
              LOAD_GLOBAL              8 (REPORT_FILENAME)
              LOAD_CONST               4 (('default',))
              CALL_KW                  2
              POP_TOP

886           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               6 ('--json')
              LOAD_CONST               7 ('store_true')
              LOAD_CONST               8 (('action',))
              CALL_KW                  2
              POP_TOP

887           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               9 ('--summary-only')
              LOAD_CONST               7 ('store_true')
              LOAD_CONST               8 (('action',))
              CALL_KW                  2
              POP_TOP

888           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST              10 ('--strict')
              LOAD_CONST               7 ('store_true')
              LOAD_CONST               8 (('action',))
              CALL_KW                  2
              POP_TOP

889           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18115020, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 892>:
892           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C17D8C5C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 892>:
892           RESUME                   0

893           LOAD_GLOBAL              1 (print + NULL)

894           LOAD_CONST               0 ('[PAS188] verdict=')
              LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               1 ('verdict')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               2 (' blockers=')

895           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               3 ('blocker_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' info=')

896           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               5 ('info_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' checks=')

897           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               7 ('check_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' pass=')

898           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               9 ('pass_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              10 (' fail=')

899           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              11 ('fail_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE

894           BUILD_STRING            12

893           CALL                     1
              POP_TOP

901           LOAD_FAST_BORROW         0 (report)
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

902           LOAD_FAST_BORROW         1 (actions)
              TO_BOOL
              POP_JUMP_IF_FALSE       93 (to L5)
              NOT_TAKEN

903           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              13 ('[PAS188] operator actions:')
              CALL                     1
              POP_TOP

904           LOAD_FAST_BORROW         1 (actions)
              LOAD_CONST              14 (slice(None, 25, None))
              BINARY_OP               26 ([])
              GET_ITER
      L2:     FOR_ITER                17 (to L3)
              STORE_FAST               2 (a)

905           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              15 ('  - ')
              LOAD_FAST_BORROW         2 (a)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L2)

904   L3:     END_FOR
              POP_ITER

906           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         1 (actions)
              CALL                     1
              LOAD_SMALL_INT          25
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       34 (to L4)
              NOT_TAKEN

907           LOAD_GLOBAL              1 (print + NULL)
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

906   L4:     LOAD_CONST              18 (None)
              RETURN_VALUE

902   L5:     LOAD_CONST              18 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026030, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 910>:
910           RESUME                   0
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

Disassembly of <code object _write_report at 0x0000018C180FC990, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 910>:
 910           RESUME                   0

 911           NOP

 912   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

 913           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

 914           LOAD_CONST               3 ('utf-8')

 912           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 916           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

 917   L4:     LOAD_GLOBAL             11 (print + NULL)

 918           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

 919           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

 918           BUILD_STRING             4

 920           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

 917           LOAD_CONST               7 (('file',))
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

 916   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18114030, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 924>:
924           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17D88C40, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas188_operational_scaling_readiness_check.py", line 924>:
 924            RESUME                   0

 925            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 926            NOP

 927    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 931    L2:     LOAD_GLOBAL             10 (os)
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

 932            LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               21 (isdir + NULL|self)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L4)
                NOT_TAKEN

 933            LOAD_GLOBAL             23 (print + NULL)
                LOAD_CONST               2 ('error: --repo-root not a directory: ')
                LOAD_FAST                4 (repo_root)
                FORMAT_SIMPLE
                BUILD_STRING             2
                LOAD_GLOBAL             24 (sys)
                LOAD_ATTR               26 (stderr)
                LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

 934            LOAD_SMALL_INT           2
                RETURN_VALUE

 936    L4:     LOAD_GLOBAL             29 (evaluate + NULL)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                STORE_FAST               5 (report)

 938            LOAD_FAST                2 (args)
                LOAD_ATTR               30 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L5)
                NOT_TAKEN

 939            LOAD_GLOBAL             33 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               34 (output)
                LOAD_FAST                5 (report)
                CALL                     2
                POP_TOP

 941    L5:     LOAD_GLOBAL             37 (_print_summary + NULL)
                LOAD_FAST                5 (report)
                CALL                     1
                POP_TOP

 943            LOAD_FAST                2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L6)
                NOT_TAKEN

 944            LOAD_GLOBAL             23 (print + NULL)
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

 946    L6:     LOAD_FAST                5 (report)
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

 928            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L17)
                NOT_TAKEN
                STORE_FAST               3 (e)

 929    L9:     LOAD_FAST                3 (e)
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

 928   L17:     RERAISE                  0

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
