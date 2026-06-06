# scripts_readiness/pas189_operational_wirethrough_readiness_check

- **pyc:** `scripts\__pycache__\pas189_operational_wirethrough_readiness_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/pas189_operational_wirethrough_readiness_check.py`
- **co_filename (from bytecode):** `C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS189 — Operational wire-through readiness gate.

Deterministic, non-mutating evaluator for "is PAS189 wired
correctly, additive-only, fail-open, and free of regressions
across the PAS160-PAS188 + PAS-SECURITY-01/02/03/04 doctrine?".

Walks the repo and verifies:

  * PAS189 surfaces exist (doc / readiness gate / three
    services / one route / test file).
  * Doctrine clauses present in the PAS189 doc; no
    forbidden-feature tokens.
  * Circuit-breaker policy module: required tokens
    present (read-only API + fail-open warning) AND
    forbidden tokens absent (auto-trip, threading.Timer,
    scheduler, while-True loop, ledger mutation calls).
  * Cache invalidation service: required tokens present
    (operator-only invalidation surface) AND forbidden
    tokens absent (background invalidation thread).
  * Tenant incident projection: required tokens present
    (brokerage-scoped safe projection) AND forbidden
    tokens absent (cross-brokerage filter bypass /
    operator-side leak / mutation surface).
  * Tenant incidents route: required tokens (X-API-Key
    auth, admin key rejection, GET only) + forbidden
    tokens (POST/PATCH/DELETE in any /tenant/incidents
    route).
  * Daily-runner --watch mode: required CLI flags +
    forbidden scheduler/daemon tokens.
  * /ops/fleet/status: pagination (limit + offset)
    declared.
  * Dashboard fleet panel: PAS189 pagination anchors
    present + PAS185-A + PAS188 anchors preserved.
  * Circuit-breaker wire-through: create_pending_call
    carries the should_block check + fail-open guard +
    no mutation of breaker.
  * Event contract carries the 5 PAS189 event types.
  * `app/main.py` mounts the tenant_incidents router.
  * No Gmail / google-auth / IMAP / POP3 / Composio /
    TrustClaw / embedding / vector imports in any
    PAS189 surface.
  * Memory Review surface untouched.
  * Worker remains OFF by default.
  * PAS160-PAS188 + PAS-SECURITY-01/02/03/04 readiness
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

`__annotate__`, `_aggregate`, `_build_parser`, `_check`, `_now_iso`, `_operator_actions`, `_print_summary`, `_read_text`, `_strip_python_comments_and_strings`, `_write_report`, `check_cache_inv_invariants`, `check_daily_runner_watch`, `check_dashboard_anchors_present`, `check_doc_no_forbidden_scope`, `check_doc_required_clauses`, `check_event_contract_has_pas189_types`, `check_main_mounts_tenant_router`, `check_memory_review_intact`, `check_pagination_invariants`, `check_pas189_files_present`, `check_pending_calls_wirethrough`, `check_policy_invariants`, `check_prior_phases_intact`, `check_self_no_env_or_db`, `check_service_no_forbidden_imports`, `check_service_no_scheduler_or_loop`, `check_tenant_projection_invariants`, `check_tenant_route_invariants`, `check_worker_off_by_default`, `evaluate`, `main`

## Env-key candidates

`BLOCK`, `FAIL`, `NOT_READY`, `PAS189`, `PASS`, `READY`

## String constants (redacted where noted)

- '\nPAS189 — Operational wire-through readiness gate.\n\nDeterministic, non-mutating evaluator for "is PAS189 wired\ncorrectly, additive-only, fail-open, and free of regressions\nacross the PAS160-PAS188 + PAS-SECURITY-01/02/03/04 doctrine?".\n\nWalks the repo and verifies:\n\n  * PAS189 surfaces exist (doc / readiness gate / three\n    services / one route / test file).\n  * Doctrine clauses present in the PAS189 doc; no\n    forbidden-feature tokens.\n  * Circuit-breaker policy module: required tokens\n    present (read-only API + fail-open warning) AND\n    forbidden tokens absent (auto-trip, threading.Timer,\n    scheduler, while-True loop, ledger mutation calls).\n  * Cache invalidation service: required tokens present\n    (operator-only invalidation surface) AND forbidden\n    tokens absent (background invalidation thread).\n  * Tenant incident projection: required tokens present\n    (brokerage-scoped safe projection) AND forbidden\n    tokens absent (cross-brokerage filter bypass /\n    operator-side leak / mutation surface).\n  * Tenant incidents route: required tokens (X-API-Key\n    auth, admin key rejection, GET only) + forbidden\n    tokens (POST/PATCH/DELETE in any /tenant/incidents\n    route).\n  * Daily-runner --watch mode: required CLI flags +\n    forbidden scheduler/daemon tokens.\n  * /ops/fleet/status: pagination (limit + offset)\n    declared.\n  * Dashboard fleet panel: PAS189 pagination anchors\n    present + PAS185-A + PAS188 anchors preserved.\n  * Circuit-breaker wire-through: create_pending_call\n    carries the should_block check + fail-open guard +\n    no mutation of breaker.\n  * Event contract carries the 5 PAS189 event types.\n  * `app/main.py` mounts the tenant_incidents router.\n  * No Gmail / google-auth / IMAP / POP3 / Composio /\n    TrustClaw / embedding / vector imports in any\n    PAS189 surface.\n  * Memory Review surface untouched.\n  * Worker remains OFF by default.\n  * PAS160-PAS188 + PAS-SECURITY-01/02/03/04 readiness\n    scripts still on disk.\n\nRead-only: never reads .env, never touches Supabase,\nnever executes a deploy / migration / network call.\n\nExit codes:\n  0 — READY\n  1 — NOT_READY (one or more BLOCK checks failed)\n  2 — bad CLI args\n'
- 'utf-8'
- 'READY'
- 'NOT_READY'
- 'BLOCK'
- 'app/services/operator/circuit_breaker_policy.py'
- 'app/services/operator/cache_invalidation.py'
- 'app/services/tenant/tenant_incident_projection.py'
- 'app/routes/tenant_incidents.py'
- 'scripts/run_daily_ops_checklist_report.py'
- 'app/routes/operator_fleet.py'
- 'app/static/dashboard/index.html'
- 'app/services/ingestion/pending_calls.py'
- 'app/services/events/contract.py'
- 'severity'
- 'detail'
- 'pas189_operational_wirethrough_readiness_report.json'
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
- 'Required PAS189 artefact present: '
- 'missing'
- 'prior_phase:'
- 'Prior-phase readiness script intact: '
- 'missing — PAS189 must not delete'
- 'memory_review:'
- 'Memory Review file present: '
- 'Memory Review file deleted — PAS189 must not touch'
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
- 'service_scheduler:'
- ' contains no scheduler / cron / autonomous loop'
- 'policy:token:'
- 'circuit_breaker_policy.py carries: '
- 'token missing'
- 'policy:no_auto_trip'
- 'circuit_breaker_policy.py is read-only (no auto-trip / mutation / thread)'
- 'cache_inv:token:'
- 'cache_invalidation.py carries: '
- 'cache_inv:no_background_thread'
- 'cache_invalidation.py contains no background invalidation thread / scheduler'
- 'tenant_proj:token:'
- 'tenant_incident_projection.py carries: '
- 'tenant_proj:no_mutation'
- 'tenant_incident_projection.py has no mutation surface'
- 'tenant_route:token:'
- 'tenant_incidents.py carries: '
- 'tenant_route:read_only'
- 'tenant_incidents.py declares no mutation route on /incidents'
- 'daily_runner:token:'
- 'run_daily_ops_checklist_report.py carries: '
- 'daily_runner:no_scheduler_or_daemon'
- 'run_daily_ops_checklist_report.py contains no scheduler / cron / daemonize'
- 'pagination:token:'
- 'operator_fleet.py carries: '
- 'dashboard:'
- 'Dashboard anchor present: '
- 'anchor missing'
- 'pending_calls:token:'
- 'pending_calls.py carries: '
- 'pending_calls:pattern:'
- 'pending_calls.py carries fail-open pattern: '
- 'pattern missing'
- 'current_breaker_state('
- 'pending_calls:no_breaker_mutation'
- 'pending_calls.py does NOT mutate breaker state'
- 'contract:event:'
- 'events/contract.py carries event_type literal: '
- 'literal missing — contract drift'
- 'app/main.py'
- 'main:mount:'
- 'app/main.py contains: '
- 'mount missing — route inaccessible'
- 'dotenv import'
- 'supabase import'
- 'load_dotenv('
- 'load_dotenv() call'
- 'environ read'
- 'get_supabase'
- 'supabase client call'
- 'self_check:no_env_or_db_or_network'
- 'PAS189 readiness checker never reads .env / touches DB / hits network'
- 'checks'
- 'verdict'
- 'blockers'
- 'info'
- 'List[str]'
- ' — '
- 'see report'
- 'phase'
- 'PAS189'
- 'generated_at'
- 'ready'
- 'blocker_count'
- 'info_count'
- 'check_count'
- 'pass_count'
- 'fail_count'
- 'operator_actions'
- 'argparse.ArgumentParser'
- 🔒 '<REDACTED:high-entropy blob, len=46>'
- 'PAS189 — Operational wire-through readiness gate. Read-only — never reads .env, never touches Supabase, never executes a deploy / migration.'
- '--repo-root'
- '--output'
- '--json'
- 'store_true'
- '--summary-only'
- '--strict'
- 'report'
- 'None'
- '[PAS189] verdict='
- ' blockers='
- ' info='
- ' checks='
- ' pass='
- ' fail='
- '[PAS189] operator actions:'
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

   1           LOAD_CONST               0 ('\nPAS189 — Operational wire-through readiness gate.\n\nDeterministic, non-mutating evaluator for "is PAS189 wired\ncorrectly, additive-only, fail-open, and free of regressions\nacross the PAS160-PAS188 + PAS-SECURITY-01/02/03/04 doctrine?".\n\nWalks the repo and verifies:\n\n  * PAS189 surfaces exist (doc / readiness gate / three\n    services / one route / test file).\n  * Doctrine clauses present in the PAS189 doc; no\n    forbidden-feature tokens.\n  * Circuit-breaker policy module: required tokens\n    present (read-only API + fail-open warning) AND\n    forbidden tokens absent (auto-trip, threading.Timer,\n    scheduler, while-True loop, ledger mutation calls).\n  * Cache invalidation service: required tokens present\n    (operator-only invalidation surface) AND forbidden\n    tokens absent (background invalidation thread).\n  * Tenant incident projection: required tokens present\n    (brokerage-scoped safe projection) AND forbidden\n    tokens absent (cross-brokerage filter bypass /\n    operator-side leak / mutation surface).\n  * Tenant incidents route: required tokens (X-API-Key\n    auth, admin key rejection, GET only) + forbidden\n    tokens (POST/PATCH/DELETE in any /tenant/incidents\n    route).\n  * Daily-runner --watch mode: required CLI flags +\n    forbidden scheduler/daemon tokens.\n  * /ops/fleet/status: pagination (limit + offset)\n    declared.\n  * Dashboard fleet panel: PAS189 pagination anchors\n    present + PAS185-A + PAS188 anchors preserved.\n  * Circuit-breaker wire-through: create_pending_call\n    carries the should_block check + fail-open guard +\n    no mutation of breaker.\n  * Event contract carries the 5 PAS189 event types.\n  * `app/main.py` mounts the tenant_incidents router.\n  * No Gmail / google-auth / IMAP / POP3 / Composio /\n    TrustClaw / embedding / vector imports in any\n    PAS189 surface.\n  * Memory Review surface untouched.\n  * Worker remains OFF by default.\n  * PAS160-PAS188 + PAS-SECURITY-01/02/03/04 readiness\n    scripts still on disk.\n\nRead-only: never reads .env, never touches Supabase,\nnever executes a deploy / migration / network call.\n\nExit codes:\n  0 — READY\n  1 — NOT_READY (one or more BLOCK checks failed)\n  2 — bad CLI args\n')
               STORE_NAME               0 (__doc__)

  57           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  59           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  60           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (json)
               STORE_NAME               4 (json)

  61           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (os)
               STORE_NAME               5 (os)

  62           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (sys)
               STORE_NAME               6 (sys)

  63           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              7 (datetime)
               IMPORT_FROM              7 (datetime)
               STORE_NAME               7 (datetime)
               IMPORT_FROM              8 (timezone)
               STORE_NAME               8 (timezone)
               POP_TOP

  64           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Path',))
               IMPORT_NAME              9 (pathlib)
               IMPORT_FROM             10 (Path)
               STORE_NAME              10 (Path)
               POP_TOP

  65           LOAD_SMALL_INT           0
               LOAD_CONST               5 (('List', 'Optional'))
               IMPORT_NAME             11 (typing)
               IMPORT_FROM             12 (List)
               STORE_NAME              12 (List)
               IMPORT_FROM             13 (Optional)
               STORE_NAME              13 (Optional)
               POP_TOP

  68           LOAD_NAME                6 (sys)
               LOAD_ATTR               28 (stdout)
               LOAD_NAME                6 (sys)
               LOAD_ATTR               30 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              16 (_stream)

  69           NOP

  70   L2:     LOAD_NAME               16 (_stream)
               LOAD_ATTR               35 (reconfigure + NULL|self)
               LOAD_CONST               6 ('utf-8')
               LOAD_CONST               7 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  68   L4:     END_FOR
               POP_ITER

  75           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               41 (abspath + NULL|self)

  76           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               43 (join + NULL|self)
               LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               45 (dirname + NULL|self)
               LOAD_NAME               23 (__file__)
               CALL                     1
               LOAD_CONST               8 ('..')
               CALL                     2

  75           CALL                     1
               STORE_NAME              24 (_REPO_ROOT_DEFAULT)

  80           LOAD_CONST               9 ('READY')
               STORE_NAME              25 (VERDICT_READY)

  81           LOAD_CONST              10 ('NOT_READY')
               STORE_NAME              26 (VERDICT_NOT_READY)

  83           LOAD_CONST              11 ('BLOCK')
               STORE_NAME              27 (SEVERITY_BLOCK)

  90           LOAD_CONST              86 (('docs/pas189_operational_wirethrough.md', 'scripts/pas189_operational_wirethrough_readiness_check.py', 'app/services/operator/circuit_breaker_policy.py', 'app/services/operator/cache_invalidation.py', 'app/services/tenant/tenant_incident_projection.py', 'app/routes/tenant_incidents.py', 'tests/mvp/test_pas189_operational_wirethrough.py'))
               STORE_NAME              28 (PAS189_FILES)

 101           LOAD_CONST              87 (('scripts/pas160_mvp_sequence_check.py', 'scripts/pas161_lead_ingestion_readiness_check.py', 'scripts/pas162_pending_calls_readiness_check.py', 'scripts/pas163_candidate_pipeline_readiness_check.py', 'scripts/pas164_email_ingestion_readiness_check.py', 'scripts/pas165_email_auth_dedupe_readiness_check.py', 'scripts/pas166_email_dedupe_policy_readiness_check.py', 'scripts/pas167_email_secret_reaper_readiness_check.py', 'scripts/pas168_email_secret_rotation_readiness_check.py', 'scripts/pas169_crypto_roundtrip_check.py', 'scripts/pas169_launch_readiness_check.py', 'scripts/pas_launch_integrity_check.py', 'scripts/pas170_operator_survival_readiness_check.py', 'scripts/pas171_external_pilot_readiness_check.py', 'scripts/pas172_pilot_operations_readiness_check.py', 'scripts/pas173_brokerage_operator_readiness_check.py', 'scripts/pas174_operator_audit_readiness_check.py', 'scripts/pas175_audit_integrity_readiness_check.py', 'scripts/pas176_audit_chain_readiness_check.py', 'scripts/pas177_tenant_audit_verification_readiness_check.py', 'scripts/pas178_audit_window_chain_readiness_check.py', 'scripts/pas179_controlled_learning_readiness_check.py', 'scripts/pas180_learning_review_readiness_check.py', 'scripts/pas181_manual_test_harness_readiness_check.py', 'scripts/pas182_adaptive_memory_bridge_readiness_check.py', 'scripts/pas183_onboarding_product_readiness_check.py', 'scripts/pas184_pilot_experience_readiness_check.py', 'scripts/pas186_final_cutover_readiness_check.py', 'scripts/pas187_fleet_cutover_readiness_check.py', 'scripts/pas188_operational_scaling_readiness_check.py', 'scripts/pas_security_01_hardening_readiness_check.py', 'scripts/pas_security_02_rate_limit_scanner_readiness_check.py', 'scripts/pas_security_03_admin_webhook_ci_readiness_check.py', 'scripts/pas_security_04_operator_reveal_https_readiness_check.py'))
               STORE_NAME              29 (PRIOR_PHASE_FILES)

 139           LOAD_CONST              88 (('app/services/memory/review.py', 'app/services/memory/review_stats.py', 'app/services/memory/review_export.py', 'app/services/memory/review_actors.py', 'app/services/memory/review_alerts.py', 'app/services/memory/operator_console.py'))
               STORE_NAME              30 (MEMORY_REVIEW_FILES)

 149           LOAD_CONST              89 ((('docs/pas189_operational_wirethrough.md', (('purpose', ('purpose',)), ('relationship-to-pas188', ('relationship to pas188',)), ('circuit-breaker-wirethrough', ('circuit-breaker wire-through doctrine',)), ('fail-open-doctrine', ('fail-open doctrine',)), ('no-auto-trip-doctrine', ('no auto-trip doctrine',)), ('cache-invalidation-doctrine', ('cache invalidation doctrine',)), ('daily-runner-watch', ('daily-runner watch-mode doctrine', 'watch-mode doctrine')), ('dashboard-pagination', ('dashboard pagination doctrine',)), ('tenant-incident-visibility', ('tenant incident visibility doctrine',)), ('no-autonomous-remediation', ('no autonomous remediation',)), ('rollback-workflow', ('rollback workflow',)), ('remaining-limitations', ('remaining limitations',)), ('intentionally-does-not-build', ('intentionally does not build',)), ('no-gmail', ('no gmail',)), ('composio', ('composio',)))),))
               STORE_NAME              31 (DOC_REQUIRED_CLAUSES)

 171           LOAD_CONST              90 (('gmail oauth integration', 'composio integration', 'trustclaw', 'auto-approve memory', 'ai chat assistant enabled', 'embedding model', 'vector database', 'imap inbox scanner', 'pop3 inbox scanner', 'auto-trip enabled', 'autonomous trip'))
               STORE_NAME              32 (FORBIDDEN_DOC_TOKENS)

 186           LOAD_CONST              91 (('app/services/operator/circuit_breaker_policy.py', 'app/services/operator/cache_invalidation.py', 'app/services/tenant/tenant_incident_projection.py', 'app/routes/tenant_incidents.py'))
               STORE_NAME              33 (SERVICE_FILES)

 194           LOAD_CONST              92 (('from googleapiclient', 'import googleapiclient', 'from google.oauth2', 'import google.oauth2', 'from google_auth_oauthlib', 'import google_auth_oauthlib', 'from imaplib', 'import imaplib', 'from poplib', 'import poplib', 'from composio', 'import composio', 'from trustclaw', 'import trustclaw', 'from chromadb', 'import chromadb', 'from pinecone', 'import pinecone', 'from pgvector', 'import pgvector', 'from sentence_transformers', 'import sentence_transformers', 'from openai', 'import openai'))
               STORE_NAME              34 (FORBIDDEN_IMPORT_PREFIXES)

 222           LOAD_CONST              93 (('apscheduler.schedulers', 'from celery', 'import celery', 'from croniter', 'import croniter', 'schedule.every(', 'while True:', 'asyncio.create_task(auto_'))
               STORE_NAME              35 (FORBIDDEN_SERVICE_TOKENS)

 235           LOAD_CONST              12 ('app/services/operator/circuit_breaker_policy.py')
               STORE_NAME              36 (POLICY_FILE)

 236           LOAD_CONST              94 (('def brokerage_circuit_breaker_status', 'def should_block_new_outbound_for_brokerage', 'def circuit_breaker_public_warning', 'def circuit_breaker_policy_report', 'brokerage_circuit_breaker_tripped', 'policy_check_failed_fail_open', 'return False'))
               STORE_NAME              37 (POLICY_REQUIRED_TOKENS)

 249           LOAD_CONST              95 (('def trip_breaker', 'def reset_breaker', 'def auto_trip', 'def autonomous_trip', 'threading.Timer(', 'Thread(target='))
               STORE_NAME              38 (POLICY_FORBIDDEN_TOKENS)

 260           LOAD_CONST              13 ('app/services/operator/cache_invalidation.py')
               STORE_NAME              39 (CACHE_INV_FILE)

 261           LOAD_CONST              96 (('def invalidate_fleet_status_for_brokerage', 'def invalidate_fleet_status_all', 'def cache_invalidation_report', 'fleet.cache.invalidated'))
               STORE_NAME              40 (CACHE_INV_REQUIRED_TOKENS)

 267           LOAD_CONST              97 (('threading.Timer(', 'Thread(target=', 'apscheduler.schedulers', 'while True:'))
               STORE_NAME              41 (CACHE_INV_FORBIDDEN_TOKENS)

 276           LOAD_CONST              14 ('app/services/tenant/tenant_incident_projection.py')
               STORE_NAME              42 (TENANT_PROJ_FILE)

 277           LOAD_CONST              98 (('def list_tenant_incidents_for_brokerage', 'def get_tenant_incident_for_brokerage', '_TENANT_ROW_ALLOWLIST', 'eq("brokerage_id", bid)', 'eq("incident_id", iid)'))
               STORE_NAME              43 (TENANT_PROJ_REQUIRED_TOKENS)

 284           LOAD_CONST              99 (('def open_incident', 'def update_incident', 'def resolve_incident', 'def delete_incident', '.insert(', '.update(', '.delete('))
               STORE_NAME              44 (TENANT_PROJ_FORBIDDEN_TOKENS)

 297           LOAD_CONST              15 ('app/routes/tenant_incidents.py')
               STORE_NAME              45 (TENANT_ROUTE_FILE)

 298           LOAD_CONST             100 (('@router.get("/incidents")', '@router.get("/incidents/{incident_id}")', 'def require_brokerage', 'Admin key not accepted on tenant surface'))
               STORE_NAME              46 (TENANT_ROUTE_REQUIRED_TOKENS)

 304           LOAD_CONST             101 (('@router.post("/incidents', '@router.patch("/incidents', '@router.delete("/incidents', '@router.put("/incidents'))
               STORE_NAME              47 (TENANT_ROUTE_FORBIDDEN_TOKENS)

 313           LOAD_CONST              16 ('scripts/run_daily_ops_checklist_report.py')
               STORE_NAME              48 (DAILY_RUNNER_FILE)

 314           LOAD_CONST             102 (('--watch', '--interval-seconds', '--max-runs', 'PAS189-watch', 'KeyboardInterrupt'))
               STORE_NAME              49 (DAILY_RUNNER_REQUIRED_TOKENS)

 321           LOAD_CONST             103 (('apscheduler.schedulers', 'from celery', 'import celery', 'from croniter', 'import croniter', 'schedule.every(', 'crontab.write', 'os.fork('))
               STORE_NAME              50 (DAILY_RUNNER_FORBIDDEN_TOKENS)

 334           LOAD_CONST              17 ('app/routes/operator_fleet.py')
               STORE_NAME              51 (FLEET_ROUTE_FILE)

 335           LOAD_CONST             104 (('offset: int = Query(0)', '"offset"', '"limit"', 'total_in_window'))
               STORE_NAME              52 (FLEET_ROUTE_REQUIRED_TOKENS)

 344           LOAD_CONST              18 ('app/static/dashboard/index.html')
               STORE_NAME              53 (DASHBOARD_FILE)

 345           LOAD_CONST             105 ((('pas189:fleet-page-size', 'PAS189_FLEET_PAGE_SIZE'), ('pas189:fleet-max-pages', 'PAS189_FLEET_MAX_PAGES'), ('pas189:fleet-state', 'pas189FleetState'), ('pas189:fleet-fetch-page', '_pas189FleetFetchPage'), ('pas189:fleet-load-more', '_pas189FleetLoadMore'), ('pas189:fleet-load-more-button', 'Load more brokerages'), ('pas185a:snapshot-container', 'aPilotOpsContent'), ('pas185a:learning-container', 'aIntelLearning'), ('pas188:fleet-container', 'aFleetStatusContent'), ('pas188:fleet-loader', 'loadOperatorFleetStatus'), ('design02:skip-link', 'skip-link'), ('design02:reduced-motion', 'prefers-reduced-motion'), ('design02:dvh', '100dvh')))
               STORE_NAME              54 (DASHBOARD_REQUIRED_ANCHORS)

 366           LOAD_CONST              19 ('app/services/ingestion/pending_calls.py')
               STORE_NAME              55 (PENDING_CALLS_FILE)

 367           LOAD_CONST             106 (('should_block_new_outbound_for_brokerage', 'brokerage_circuit_breaker_tripped', 'circuit_breaker_policy', 'circuit_breaker.outbound_blocked'))
               STORE_NAME              56 (PENDING_CALLS_REQUIRED_TOKENS)

 374           LOAD_CONST             107 (('except Exception:', '# Fail-open:'))
               STORE_NAME              57 (PENDING_CALLS_REQUIRED_PATTERNS)

 381           LOAD_CONST              20 ('app/services/events/contract.py')
               STORE_NAME              58 (EVENT_CONTRACT_FILE)

 382           LOAD_CONST             108 (('"circuit_breaker.outbound_blocked"', '"fleet.cache.invalidated"', '"daily_ops.runner.watch_started"', '"daily_ops.runner.watch_completed"', '"tenant.incident.viewed"'))
               STORE_NAME              59 (EVENT_CONTRACT_REQUIRED_EVENT_TYPES)

 391           LOAD_CONST             109 (('tenant_incidents_router', 'from app.routes.tenant_incidents import'))
               STORE_NAME              60 (MAIN_PY_REQUIRED_MOUNT_TOKENS)

 401           LOAD_CONST              21 ('severity')
               LOAD_NAME               27 (SEVERITY_BLOCK)
               LOAD_CONST              22 ('detail')
               LOAD_CONST              23 ('')
               BUILD_MAP                2
               LOAD_CONST              24 (<code object __annotate__ at 0x0000018C18025130, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 401>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object _check at 0x0000018C17FA2970, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 401>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              61 (_check)

 411           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA23D0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 411>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object _now_iso at 0x0000018C18038CB0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 411>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              62 (_now_iso)

 415           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA3B40, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 415>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object _read_text at 0x0000018C180531B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 415>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              63 (_read_text)

 422           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA2F10, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 422>)
               MAKE_FUNCTION
               LOAD_CONST              31 (<code object _strip_python_comments_and_strings at 0x0000018C17D81580, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 422>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              64 (_strip_python_comments_and_strings)

 463           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA33C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 463>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object check_pas189_files_present at 0x0000018C180612C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 463>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              65 (check_pas189_files_present)

 476           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA35A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 476>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object check_prior_phases_intact at 0x0000018C18060A50, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 476>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              66 (check_prior_phases_intact)

 489           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C17FA3D20, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 489>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object check_memory_review_intact at 0x0000018C180608A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 489>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              67 (check_memory_review_intact)

 502           LOAD_CONST              38 (<code object __annotate__ at 0x0000018C17FA1D40, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 502>)
               MAKE_FUNCTION
               LOAD_CONST              39 (<code object check_worker_off_by_default at 0x0000018C1794ED80, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 502>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              68 (check_worker_off_by_default)

 517           LOAD_CONST              40 (<code object __annotate__ at 0x0000018C17FA2880, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 517>)
               MAKE_FUNCTION
               LOAD_CONST              41 (<code object check_doc_required_clauses at 0x0000018C17D8BA70, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 517>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              69 (check_doc_required_clauses)

 534           LOAD_CONST              42 (<code object __annotate__ at 0x0000018C17FA2B50, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 534>)
               MAKE_FUNCTION
               LOAD_CONST              43 (<code object check_doc_no_forbidden_scope at 0x0000018C17ECE910, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 534>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              70 (check_doc_no_forbidden_scope)

 549           LOAD_CONST              44 (<code object __annotate__ at 0x0000018C17FA32D0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 549>)
               MAKE_FUNCTION
               LOAD_CONST              45 (<code object check_service_no_forbidden_imports at 0x0000018C17F789F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 549>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              71 (check_service_no_forbidden_imports)

 571           LOAD_CONST              46 (<code object __annotate__ at 0x0000018C17FA3780, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 571>)
               MAKE_FUNCTION
               LOAD_CONST              47 (<code object check_service_no_scheduler_or_loop at 0x0000018C17D76C00, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 571>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              72 (check_service_no_scheduler_or_loop)

 587           LOAD_CONST              48 (<code object __annotate__ at 0x0000018C17FA1E30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 587>)
               MAKE_FUNCTION
               LOAD_CONST              49 (<code object check_policy_invariants at 0x0000018C17D862D0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 587>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              73 (check_policy_invariants)

 608           LOAD_CONST              50 (<code object __annotate__ at 0x0000018C17FA2E20, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 608>)
               MAKE_FUNCTION
               LOAD_CONST              51 (<code object check_cache_inv_invariants at 0x0000018C17D875A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 608>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              74 (check_cache_inv_invariants)

 629           LOAD_CONST              52 (<code object __annotate__ at 0x0000018C17FA21F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 629>)
               MAKE_FUNCTION
               LOAD_CONST              53 (<code object check_tenant_projection_invariants at 0x0000018C17D86D90, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 629>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              75 (check_tenant_projection_invariants)

 650           LOAD_CONST              54 (<code object __annotate__ at 0x0000018C17FA26A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 650>)
               MAKE_FUNCTION
               LOAD_CONST              55 (<code object check_tenant_route_invariants at 0x0000018C17D8B290, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 650>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              76 (check_tenant_route_invariants)

 670           LOAD_CONST              56 (<code object __annotate__ at 0x0000018C17FA22E0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 670>)
               MAKE_FUNCTION
               LOAD_CONST              57 (<code object check_daily_runner_watch at 0x0000018C17D87850, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 670>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              77 (check_daily_runner_watch)

 691           LOAD_CONST              58 (<code object __annotate__ at 0x0000018C17FA24C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 691>)
               MAKE_FUNCTION
               LOAD_CONST              59 (<code object check_pagination_invariants at 0x0000018C18048E30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 691>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              78 (check_pagination_invariants)

 704           LOAD_CONST              60 (<code object __annotate__ at 0x0000018C17FA25B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 704>)
               MAKE_FUNCTION
               LOAD_CONST              61 (<code object check_dashboard_anchors_present at 0x0000018C1794E9E0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 704>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              79 (check_dashboard_anchors_present)

 718           LOAD_CONST              62 (<code object __annotate__ at 0x0000018C17FA2D30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 718>)
               MAKE_FUNCTION
               LOAD_CONST              63 (<code object check_pending_calls_wirethrough at 0x0000018C17D6DFC0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 718>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              80 (check_pending_calls_wirethrough)

 756           LOAD_CONST              64 (<code object __annotate__ at 0x0000018C17FA2A60, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 756>)
               MAKE_FUNCTION
               LOAD_CONST              65 (<code object check_event_contract_has_pas189_types at 0x0000018C180483B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 756>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              81 (check_event_contract_has_pas189_types)

 770           LOAD_CONST              66 (<code object __annotate__ at 0x0000018C17FA2C40, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 770>)
               MAKE_FUNCTION
               LOAD_CONST              67 (<code object check_main_mounts_tenant_router at 0x0000018C1794EF50, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 770>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              82 (check_main_mounts_tenant_router)

 784           LOAD_CONST              68 (<code object __annotate__ at 0x0000018C181152F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 784>)
               MAKE_FUNCTION
               LOAD_CONST              69 (<code object check_self_no_env_or_db at 0x0000018C17EA44A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 784>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              83 (check_self_no_env_or_db)

 830           LOAD_CONST              70 (<code object __annotate__ at 0x0000018C181153E0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 830>)
               MAKE_FUNCTION
               LOAD_CONST              71 (<code object _aggregate at 0x0000018C1800B230, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 830>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              84 (_aggregate)

 839           LOAD_CONST              72 (<code object __annotate__ at 0x0000018C181154D0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 839>)
               MAKE_FUNCTION
               LOAD_CONST              73 (<code object _operator_actions at 0x0000018C180488F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 839>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              85 (_operator_actions)

 849           LOAD_CONST              74 (<code object __annotate__ at 0x0000018C181155C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 849>)
               MAKE_FUNCTION
               LOAD_CONST              75 (<code object evaluate at 0x0000018C17D7C560, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 849>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              86 (evaluate)

 887           LOAD_CONST              76 ('pas189_operational_wirethrough_readiness_report.json')
               STORE_NAME              87 (REPORT_FILENAME)

 890           LOAD_CONST              77 (<code object __annotate__ at 0x0000018C18115980, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 890>)
               MAKE_FUNCTION
               LOAD_CONST              78 (<code object _build_parser at 0x0000018C179C3C30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 890>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              88 (_build_parser)

 908           LOAD_CONST              79 (<code object __annotate__ at 0x0000018C18115A70, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 908>)
               MAKE_FUNCTION
               LOAD_CONST              80 (<code object _print_summary at 0x0000018C17D8E300, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 908>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              89 (_print_summary)

 926           LOAD_CONST              81 (<code object __annotate__ at 0x0000018C18024930, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 926>)
               MAKE_FUNCTION
               LOAD_CONST              82 (<code object _write_report at 0x0000018C179C3E10, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 926>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              90 (_write_report)

 940           LOAD_CONST             110 ((None,))
               LOAD_CONST              83 (<code object __annotate__ at 0x0000018C18115110, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 940>)
               MAKE_FUNCTION
               LOAD_CONST              84 (<code object main at 0x0000018C17D88FF0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 940>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              91 (main)

 965           LOAD_NAME               92 (__name__)
               LOAD_CONST              85 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 966           LOAD_NAME                6 (sys)
               LOAD_ATTR              186 (exit)
               PUSH_NULL
               LOAD_NAME               91 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 965   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  71           LOAD_NAME               18 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  72   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          411 (to L1)

  71   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025130, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 401>:
401           RESUME                   0
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

Disassembly of <code object _check at 0x0000018C17FA2970, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 401>:
401           RESUME                   0

403           LOAD_CONST               0 ('id')
              LOAD_FAST_BORROW         0 (check_id)

404           LOAD_CONST               1 ('status')
              LOAD_FAST_BORROW         1 (status)

405           LOAD_CONST               2 ('label')
              LOAD_FAST_BORROW         2 (label)

406           LOAD_CONST               3 ('severity')
              LOAD_FAST_BORROW         3 (severity)

407           LOAD_CONST               4 ('detail')
              LOAD_FAST_BORROW         4 (detail)

402           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 411>:
411           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038CB0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 411>:
411           RESUME                   0

412           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 415>:
415           RESUME                   0
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

Disassembly of <code object _read_text at 0x0000018C180531B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 415>:
 415           RESUME                   0

 416           NOP

 417   L1:     LOAD_FAST_BORROW         0 (path)
               LOAD_ATTR                1 (read_text + NULL|self)
               LOAD_CONST               0 ('utf-8')
               LOAD_CONST               1 ('replace')
               LOAD_CONST               2 (('encoding', 'errors'))
               CALL_KW                  2
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 418           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 419   L4:     POP_EXCEPT
               LOAD_CONST               3 (None)
               RETURN_VALUE

 418   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 422>:
422           RESUME                   0
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

Disassembly of <code object _strip_python_comments_and_strings at 0x0000018C17D81580, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 422>:
422            RESUME                   0

425            BUILD_LIST               0
               STORE_FAST               1 (out)

426            LOAD_SMALL_INT           0
               LOAD_GLOBAL              1 (len + NULL)
               LOAD_FAST_BORROW         0 (src)
               CALL                     1
               STORE_FAST_STORE_FAST   50 (n, i)

427    L1:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (i, n)
               COMPARE_OP              18 (bool(<))
               EXTENDED_ARG             1
               POP_JUMP_IF_FALSE      282 (to L13)
               NOT_TAKEN

428            LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               BINARY_OP               26 ([])
               STORE_FAST               4 (ch)

429            LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               1 ('#')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       38 (to L3)
               NOT_TAKEN

430            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_CONST               2 ('\n')
               LOAD_FAST_BORROW         2 (i)
               CALL                     2
               STORE_FAST               5 (j)

431            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L2)
               NOT_TAKEN

432            JUMP_FORWARD           240 (to L13)

433    L2:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

434            JUMP_BACKWARD           59 (to L1)

435    L3:     LOAD_FAST_BORROW         0 (src)
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

436    L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               BINARY_SLICE
               STORE_FAST               6 (quote)

437            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 98 (quote, i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               CALL                     2
               STORE_FAST               7 (end)

438            LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L5)
               NOT_TAKEN

439            JUMP_FORWARD           138 (to L13)

440    L5:     LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

441            JUMP_BACKWARD          161 (to L1)

442    L6:     LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               7 (('"', "'"))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       92 (to L12)
               NOT_TAKEN

443            LOAD_FAST                4 (ch)
               STORE_FAST               6 (quote)

444            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               5 (j)

445    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (j, n)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       63 (to L11)
               NOT_TAKEN

446            LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
               BINARY_OP               26 ([])
               LOAD_CONST               5 ('\\')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       12 (to L8)
               NOT_TAKEN

447            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           2
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)

448            JUMP_BACKWARD           30 (to L7)

449    L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
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

450    L9:     JUMP_FORWARD            11 (to L11)

451   L10:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)
               JUMP_BACKWARD           68 (to L7)

452   L11:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

453            EXTENDED_ARG             1
               JUMP_BACKWARD          259 (to L1)

454   L12:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (ch)
               CALL                     1
               POP_TOP

455            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               2 (i)
               EXTENDED_ARG             1
               JUMP_BACKWARD          288 (to L1)

456   L13:     LOAD_CONST               6 ('')
               LOAD_ATTR                9 (join + NULL|self)
               LOAD_FAST_BORROW         1 (out)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 463>:
463           RESUME                   0
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

Disassembly of <code object check_pas189_files_present at 0x0000018C180612C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 463>:
463           RESUME                   0

464           BUILD_LIST               0
              STORE_FAST               1 (out)

465           LOAD_GLOBAL              0 (PAS189_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

466           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

467           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

468           LOAD_CONST               0 ('file:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

469           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

470   L3:     LOAD_CONST               3 ('Required PAS189 artefact present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

471           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing')

467   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

465   L6:     END_FOR
              POP_ITER

473           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 476>:
476           RESUME                   0
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

Disassembly of <code object check_prior_phases_intact at 0x0000018C18060A50, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 476>:
476           RESUME                   0

477           BUILD_LIST               0
              STORE_FAST               1 (out)

478           LOAD_GLOBAL              0 (PRIOR_PHASE_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

479           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

480           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

481           LOAD_CONST               0 ('prior_phase:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

482           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

483   L3:     LOAD_CONST               3 ('Prior-phase readiness script intact: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

484           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing — PAS189 must not delete')

480   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

478   L6:     END_FOR
              POP_ITER

486           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3D20, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 489>:
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

Disassembly of <code object check_memory_review_intact at 0x0000018C180608A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 489>:
489           RESUME                   0

490           BUILD_LIST               0
              STORE_FAST               1 (out)

491           LOAD_GLOBAL              0 (MEMORY_REVIEW_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

492           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

493           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

494           LOAD_CONST               0 ('memory_review:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

495           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

496   L3:     LOAD_CONST               3 ('Memory Review file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

497           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('Memory Review file deleted — PAS189 must not touch')

493   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

491   L6:     END_FOR
              POP_ITER

499           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1D40, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 502>:
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

Disassembly of <code object check_worker_off_by_default at 0x0000018C1794ED80, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 502>:
502           RESUME                   0

503           LOAD_GLOBAL              1 (Path + NULL)
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

504           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         1 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               2 (src)

506           LOAD_CONST               5 ('_ENV_FLAG_ENABLED_LITERAL = "true"')
              LOAD_FAST_BORROW         2 (src)
              CONTAINS_OP              0 (in)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         6 (to L2)
              NOT_TAKEN
              POP_TOP

507           LOAD_CONST               6 ("_ENV_FLAG_ENABLED_LITERAL = 'true'")
              LOAD_FAST_BORROW         2 (src)
              CONTAINS_OP              0 (in)

505   L2:     STORE_FAST               3 (ok)

509           LOAD_GLOBAL              5 (_check + NULL)

510           LOAD_CONST               7 ('worker:off_by_default')

511           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               8 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               9 ('FAIL')

512   L4:     LOAD_CONST              10 ('Pending-call worker is OFF by default')

513           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        9 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')

509           LOAD_CONST              12 (('detail',))
              CALL_KW                  4
              BUILD_LIST               1
              RETURN_VALUE

513   L5:     LOAD_CONST              11 ('missing strict enable-literal constant')

509           LOAD_CONST              12 (('detail',))
              CALL_KW                  4
              BUILD_LIST               1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 517>:
517           RESUME                   0
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

Disassembly of <code object check_doc_required_clauses at 0x0000018C17D8BA70, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 517>:
  --            MAKE_CELL                9 (lower)

 517            RESUME                   0

 518            BUILD_LIST               0
                STORE_FAST               1 (out)

 519            LOAD_GLOBAL              0 (DOC_REQUIRED_CLAUSES)
                GET_ITER
        L1:     FOR_ITER               208 (to L14)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   35 (relpath, clauses)

 520            LOAD_GLOBAL              3 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_FAST_BORROW         2 (relpath)
                BINARY_OP               11 (/)
                STORE_FAST               4 (fp)

 521            LOAD_GLOBAL              5 (_read_text + NULL)
                LOAD_FAST_BORROW         4 (fp)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L2)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               0 ('')
        L2:     STORE_FAST               5 (src)

 522            LOAD_FAST_BORROW         5 (src)
                LOAD_ATTR                7 (lower + NULL|self)
                CALL                     0
                STORE_DEREF              9 (lower)

 523            LOAD_FAST_BORROW         3 (clauses)
                GET_ITER
        L3:     FOR_ITER               142 (to L13)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST  103 (name, phrases)

 524            LOAD_GLOBAL              8 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L7)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         9 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               1 (<code object <genexpr> at 0x0000018C18026430, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 524>)
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
                LOAD_CONST               1 (<code object <genexpr> at 0x0000018C18026430, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 524>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         7 (phrases)
                GET_ITER
                CALL                     0
                CALL                     1
        L8:     STORE_FAST               8 (present)

 525            LOAD_FAST                1 (out)
                LOAD_ATTR               11 (append + NULL|self)
                LOAD_GLOBAL             13 (_check + NULL)

 526            LOAD_CONST               4 ('doc:')
                LOAD_FAST_BORROW         2 (relpath)
                FORMAT_SIMPLE
                LOAD_CONST               5 (':clause:')
                LOAD_FAST_BORROW         6 (name)
                FORMAT_SIMPLE
                BUILD_STRING             4

 527            LOAD_FAST_BORROW         8 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L9)
                NOT_TAKEN
                LOAD_CONST               6 ('PASS')
                JUMP_FORWARD             1 (to L10)
        L9:     LOAD_CONST               7 ('FAIL')

 528   L10:     LOAD_FAST_BORROW         2 (relpath)
                FORMAT_SIMPLE
                LOAD_CONST               8 (' carries clause: ')
                LOAD_FAST_BORROW         6 (name)
                FORMAT_SIMPLE
                BUILD_STRING             3

 529            LOAD_FAST_BORROW         8 (present)
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

 525   L12:     LOAD_CONST              11 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          144 (to L3)

 523   L13:     END_FOR
                POP_ITER
                JUMP_BACKWARD          210 (to L1)

 519   L14:     END_FOR
                POP_ITER

 531            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18026430, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 524>:
  --           COPY_FREE_VARS           1

 524           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 534>:
534           RESUME                   0
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

Disassembly of <code object check_doc_no_forbidden_scope at 0x0000018C17ECE910, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 534>:
 534            RESUME                   0

 535            BUILD_LIST               0
                STORE_FAST               1 (out)

 536            LOAD_GLOBAL              0 (DOC_REQUIRED_CLAUSES)
                GET_ITER
        L1:     FOR_ITER               165 (to L13)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   35 (relpath, _)

 537            LOAD_GLOBAL              3 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_FAST_BORROW         2 (relpath)
                BINARY_OP               11 (/)
                STORE_FAST               4 (fp)

 538            LOAD_GLOBAL              5 (_read_text + NULL)
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

 539            LOAD_GLOBAL              8 (FORBIDDEN_DOC_TOKENS)
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

 540            LOAD_FAST                1 (out)
                LOAD_ATTR               11 (append + NULL|self)
                LOAD_GLOBAL             13 (_check + NULL)

 541            LOAD_CONST               1 ('doc_scope:')
                LOAD_FAST_BORROW         2 (relpath)
                FORMAT_SIMPLE
                BUILD_STRING             2

 542            LOAD_FAST_BORROW         7 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L9)
                NOT_TAKEN
                LOAD_CONST               2 ('FAIL')
                JUMP_FORWARD             1 (to L10)
        L9:     LOAD_CONST               3 ('PASS')

 543   L10:     LOAD_FAST_BORROW         2 (relpath)
                FORMAT_SIMPLE
                LOAD_CONST               4 (' introduces no out-of-scope feature token')
                BUILD_STRING             2

 544            LOAD_FAST_BORROW         7 (bad)
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

 540   L12:     LOAD_CONST               7 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          167 (to L1)

 536   L13:     END_FOR
                POP_ITER

 546            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L14:     SWAP                     2
                POP_TOP

 539            SWAP                     2
                STORE_FAST               6 (t)
                RERAISE                  0
ExceptionTable:
  L3 to L5 -> L14 [3]
  L6 to L8 -> L14 [3]

Disassembly of <code object __annotate__ at 0x0000018C17FA32D0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 549>:
549           RESUME                   0
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

Disassembly of <code object check_service_no_forbidden_imports at 0x0000018C17F789F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 549>:
549            RESUME                   0

550            BUILD_LIST               0
               STORE_FAST               1 (out)

551            LOAD_GLOBAL              0 (SERVICE_FILES)
               GET_ITER
       L1:     FOR_ITER               228 (to L12)
               STORE_FAST               2 (relpath)

552            LOAD_GLOBAL              3 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         2 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               3 (fp)

553            LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         3 (fp)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L2:     STORE_FAST               4 (src)

554            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         4 (src)
               CALL                     1
               STORE_FAST               5 (executable)

555            BUILD_LIST               0
               STORE_FAST               6 (bad)

556            LOAD_FAST_BORROW         5 (executable)
               LOAD_ATTR                9 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L3:     FOR_ITER                75 (to L7)
               STORE_FAST               7 (line)

557            LOAD_FAST_BORROW         7 (line)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0
               STORE_FAST               8 (stripped)

558            LOAD_GLOBAL             12 (FORBIDDEN_IMPORT_PREFIXES)
               GET_ITER
       L4:     FOR_ITER                46 (to L6)
               STORE_FAST               9 (pref)

559            LOAD_FAST_BORROW         8 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_FAST_BORROW         9 (pref)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           28 (to L4)

560    L5:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_FAST_BORROW         9 (pref)
               CALL                     1
               POP_TOP

561            POP_TOP
               JUMP_BACKWARD           73 (to L3)

558    L6:     END_FOR
               POP_ITER
               JUMP_BACKWARD           77 (to L3)

556    L7:     END_FOR
               POP_ITER

562            LOAD_FAST                1 (out)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_GLOBAL             19 (_check + NULL)

563            LOAD_CONST               1 ('service_imports:')
               LOAD_FAST_BORROW         2 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

564            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN
               LOAD_CONST               2 ('FAIL')
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST               3 ('PASS')

565    L9:     LOAD_FAST_BORROW         2 (relpath)
               FORMAT_SIMPLE
               LOAD_CONST               4 (' contains no forbidden import')
               BUILD_STRING             2

566            LOAD_FAST_BORROW         6 (bad)
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

562   L11:     LOAD_CONST               7 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          230 (to L1)

551   L12:     END_FOR
               POP_ITER

568            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 571>:
571           RESUME                   0
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

Disassembly of <code object check_service_no_scheduler_or_loop at 0x0000018C17D76C00, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 571>:
 571            RESUME                   0

 572            BUILD_LIST               0
                STORE_FAST               1 (out)

 573            LOAD_GLOBAL              0 (SERVICE_FILES)
                GET_ITER
        L1:     FOR_ITER               160 (to L13)
                STORE_FAST               2 (relpath)

 574            LOAD_GLOBAL              3 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_FAST_BORROW         2 (relpath)
                BINARY_OP               11 (/)
                STORE_FAST               3 (fp)

 575            LOAD_GLOBAL              5 (_read_text + NULL)
                LOAD_FAST_BORROW         3 (fp)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L2)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               0 ('')
        L2:     STORE_FAST               4 (src)

 576            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
                LOAD_FAST_BORROW         4 (src)
                CALL                     1
                STORE_FAST               5 (executable)

 577            LOAD_GLOBAL              8 (FORBIDDEN_SERVICE_TOKENS)
                GET_ITER
                LOAD_FAST_AND_CLEAR      6 (t)
                SWAP                     2
        L3:     BUILD_LIST               0
                SWAP                     2
        L4:     FOR_ITER                13 (to L7)
                STORE_FAST_LOAD_FAST   102 (t, t)
                LOAD_FAST_BORROW         5 (executable)
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

 578            LOAD_FAST                1 (out)
                LOAD_ATTR               11 (append + NULL|self)
                LOAD_GLOBAL             13 (_check + NULL)

 579            LOAD_CONST               1 ('service_scheduler:')
                LOAD_FAST_BORROW         2 (relpath)
                FORMAT_SIMPLE
                BUILD_STRING             2

 580            LOAD_FAST_BORROW         7 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L9)
                NOT_TAKEN
                LOAD_CONST               2 ('FAIL')
                JUMP_FORWARD             1 (to L10)
        L9:     LOAD_CONST               3 ('PASS')

 581   L10:     LOAD_FAST_BORROW         2 (relpath)
                FORMAT_SIMPLE
                LOAD_CONST               4 (' contains no scheduler / cron / autonomous loop')
                BUILD_STRING             2

 582            LOAD_FAST_BORROW         7 (bad)
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

 578   L12:     LOAD_CONST               7 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          162 (to L1)

 573   L13:     END_FOR
                POP_ITER

 584            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L14:     SWAP                     2
                POP_TOP

 577            SWAP                     2
                STORE_FAST               6 (t)
                RERAISE                  0
ExceptionTable:
  L3 to L5 -> L14 [3]
  L6 to L8 -> L14 [3]

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 587>:
587           RESUME                   0
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

Disassembly of <code object check_policy_invariants at 0x0000018C17D862D0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 587>:
 587            RESUME                   0

 588            BUILD_LIST               0
                STORE_FAST               1 (out)

 589            LOAD_GLOBAL              1 (_read_text + NULL)
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

 590            LOAD_GLOBAL              6 (POLICY_REQUIRED_TOKENS)
                GET_ITER
        L2:     FOR_ITER                62 (to L7)
                STORE_FAST               3 (tok)

 591            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 592            LOAD_CONST               1 ('policy:token:')
                LOAD_FAST_BORROW         3 (tok)
                LOAD_CONST               2 (slice(None, 60, None))
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                BUILD_STRING             2

 593            LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (tok, src)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L3)
                NOT_TAKEN
                LOAD_CONST               3 ('PASS')
                JUMP_FORWARD             1 (to L4)
        L3:     LOAD_CONST               4 ('FAIL')

 594    L4:     LOAD_CONST               5 ('circuit_breaker_policy.py carries: ')
                LOAD_FAST_BORROW         3 (tok)
                FORMAT_SIMPLE
                BUILD_STRING             2

 595            LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (tok, src)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN
                LOAD_CONST               0 ('')
                JUMP_FORWARD             1 (to L6)
        L5:     LOAD_CONST               6 ('token missing')

 591    L6:     LOAD_CONST               7 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           64 (to L2)

 590    L7:     END_FOR
                POP_ITER

 597            LOAD_GLOBAL             13 (_strip_python_comments_and_strings + NULL)
                LOAD_FAST_BORROW         2 (src)
                CALL                     1
                STORE_FAST               4 (executable)

 598            LOAD_GLOBAL             14 (POLICY_FORBIDDEN_TOKENS)
                GET_ITER
                LOAD_FAST_AND_CLEAR      5 (t)
                SWAP                     2
        L8:     BUILD_LIST               0
                SWAP                     2
        L9:     FOR_ITER                13 (to L12)
                STORE_FAST_LOAD_FAST    85 (t, t)
                LOAD_FAST_BORROW         4 (executable)
                CONTAINS_OP              0 (in)
       L10:     POP_JUMP_IF_TRUE         3 (to L11)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L9)
       L11:     LOAD_FAST_BORROW         5 (t)
                LIST_APPEND              2
                JUMP_BACKWARD           15 (to L9)
       L12:     END_FOR
                POP_ITER
       L13:     STORE_FAST               6 (bad)
                STORE_FAST               5 (t)

 599            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 600            LOAD_CONST               8 ('policy:no_auto_trip')

 601            LOAD_FAST_BORROW         6 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L14)
                NOT_TAKEN
                LOAD_CONST               4 ('FAIL')
                JUMP_FORWARD             1 (to L15)
       L14:     LOAD_CONST               3 ('PASS')

 602   L15:     LOAD_CONST               9 ('circuit_breaker_policy.py is read-only (no auto-trip / mutation / thread)')

 603            LOAD_FAST_BORROW         6 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L16)
                NOT_TAKEN
                LOAD_CONST              10 ('disqualifying: ')
                LOAD_CONST              11 (', ')
                LOAD_ATTR               17 (join + NULL|self)
                LOAD_FAST_BORROW         6 (bad)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L17)
       L16:     LOAD_CONST               0 ('')

 599   L17:     LOAD_CONST               7 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 605            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L18:     SWAP                     2
                POP_TOP

 598            SWAP                     2
                STORE_FAST               5 (t)
                RERAISE                  0
ExceptionTable:
  L8 to L10 -> L18 [2]
  L11 to L13 -> L18 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 608>:
608           RESUME                   0
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

Disassembly of <code object check_cache_inv_invariants at 0x0000018C17D875A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 608>:
 608            RESUME                   0

 609            BUILD_LIST               0
                STORE_FAST               1 (out)

 610            LOAD_GLOBAL              1 (_read_text + NULL)
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
        L1:     STORE_FAST               2 (src)

 611            LOAD_GLOBAL              6 (CACHE_INV_REQUIRED_TOKENS)
                GET_ITER
        L2:     FOR_ITER                62 (to L7)
                STORE_FAST               3 (tok)

 612            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 613            LOAD_CONST               1 ('cache_inv:token:')
                LOAD_FAST_BORROW         3 (tok)
                LOAD_CONST               2 (slice(None, 60, None))
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                BUILD_STRING             2

 614            LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (tok, src)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L3)
                NOT_TAKEN
                LOAD_CONST               3 ('PASS')
                JUMP_FORWARD             1 (to L4)
        L3:     LOAD_CONST               4 ('FAIL')

 615    L4:     LOAD_CONST               5 ('cache_invalidation.py carries: ')
                LOAD_FAST_BORROW         3 (tok)
                FORMAT_SIMPLE
                BUILD_STRING             2

 616            LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (tok, src)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN
                LOAD_CONST               0 ('')
                JUMP_FORWARD             1 (to L6)
        L5:     LOAD_CONST               6 ('token missing')

 612    L6:     LOAD_CONST               7 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           64 (to L2)

 611    L7:     END_FOR
                POP_ITER

 618            LOAD_GLOBAL             13 (_strip_python_comments_and_strings + NULL)
                LOAD_FAST_BORROW         2 (src)
                CALL                     1
                STORE_FAST               4 (executable)

 619            LOAD_GLOBAL             14 (CACHE_INV_FORBIDDEN_TOKENS)
                GET_ITER
                LOAD_FAST_AND_CLEAR      5 (t)
                SWAP                     2
        L8:     BUILD_LIST               0
                SWAP                     2
        L9:     FOR_ITER                13 (to L12)
                STORE_FAST_LOAD_FAST    85 (t, t)
                LOAD_FAST_BORROW         4 (executable)
                CONTAINS_OP              0 (in)
       L10:     POP_JUMP_IF_TRUE         3 (to L11)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L9)
       L11:     LOAD_FAST_BORROW         5 (t)
                LIST_APPEND              2
                JUMP_BACKWARD           15 (to L9)
       L12:     END_FOR
                POP_ITER
       L13:     STORE_FAST               6 (bad)
                STORE_FAST               5 (t)

 620            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 621            LOAD_CONST               8 ('cache_inv:no_background_thread')

 622            LOAD_FAST_BORROW         6 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L14)
                NOT_TAKEN
                LOAD_CONST               4 ('FAIL')
                JUMP_FORWARD             1 (to L15)
       L14:     LOAD_CONST               3 ('PASS')

 623   L15:     LOAD_CONST               9 ('cache_invalidation.py contains no background invalidation thread / scheduler')

 624            LOAD_FAST_BORROW         6 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L16)
                NOT_TAKEN
                LOAD_CONST              10 ('disqualifying: ')
                LOAD_CONST              11 (', ')
                LOAD_ATTR               17 (join + NULL|self)
                LOAD_FAST_BORROW         6 (bad)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L17)
       L16:     LOAD_CONST               0 ('')

 620   L17:     LOAD_CONST               7 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 626            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L18:     SWAP                     2
                POP_TOP

 619            SWAP                     2
                STORE_FAST               5 (t)
                RERAISE                  0
ExceptionTable:
  L8 to L10 -> L18 [2]
  L11 to L13 -> L18 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 629>:
629           RESUME                   0
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

Disassembly of <code object check_tenant_projection_invariants at 0x0000018C17D86D90, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 629>:
 629            RESUME                   0

 630            BUILD_LIST               0
                STORE_FAST               1 (out)

 631            LOAD_GLOBAL              1 (_read_text + NULL)
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
        L1:     STORE_FAST               2 (src)

 632            LOAD_GLOBAL              6 (TENANT_PROJ_REQUIRED_TOKENS)
                GET_ITER
        L2:     FOR_ITER                62 (to L7)
                STORE_FAST               3 (tok)

 633            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 634            LOAD_CONST               1 ('tenant_proj:token:')
                LOAD_FAST_BORROW         3 (tok)
                LOAD_CONST               2 (slice(None, 60, None))
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                BUILD_STRING             2

 635            LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (tok, src)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L3)
                NOT_TAKEN
                LOAD_CONST               3 ('PASS')
                JUMP_FORWARD             1 (to L4)
        L3:     LOAD_CONST               4 ('FAIL')

 636    L4:     LOAD_CONST               5 ('tenant_incident_projection.py carries: ')
                LOAD_FAST_BORROW         3 (tok)
                FORMAT_SIMPLE
                BUILD_STRING             2

 637            LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (tok, src)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN
                LOAD_CONST               0 ('')
                JUMP_FORWARD             1 (to L6)
        L5:     LOAD_CONST               6 ('token missing')

 633    L6:     LOAD_CONST               7 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           64 (to L2)

 632    L7:     END_FOR
                POP_ITER

 639            LOAD_GLOBAL             13 (_strip_python_comments_and_strings + NULL)
                LOAD_FAST_BORROW         2 (src)
                CALL                     1
                STORE_FAST               4 (executable)

 640            LOAD_GLOBAL             14 (TENANT_PROJ_FORBIDDEN_TOKENS)
                GET_ITER
                LOAD_FAST_AND_CLEAR      5 (t)
                SWAP                     2
        L8:     BUILD_LIST               0
                SWAP                     2
        L9:     FOR_ITER                13 (to L12)
                STORE_FAST_LOAD_FAST    85 (t, t)
                LOAD_FAST_BORROW         4 (executable)
                CONTAINS_OP              0 (in)
       L10:     POP_JUMP_IF_TRUE         3 (to L11)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L9)
       L11:     LOAD_FAST_BORROW         5 (t)
                LIST_APPEND              2
                JUMP_BACKWARD           15 (to L9)
       L12:     END_FOR
                POP_ITER
       L13:     STORE_FAST               6 (bad)
                STORE_FAST               5 (t)

 641            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 642            LOAD_CONST               8 ('tenant_proj:no_mutation')

 643            LOAD_FAST_BORROW         6 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L14)
                NOT_TAKEN
                LOAD_CONST               4 ('FAIL')
                JUMP_FORWARD             1 (to L15)
       L14:     LOAD_CONST               3 ('PASS')

 644   L15:     LOAD_CONST               9 ('tenant_incident_projection.py has no mutation surface')

 645            LOAD_FAST_BORROW         6 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L16)
                NOT_TAKEN
                LOAD_CONST              10 ('disqualifying: ')
                LOAD_CONST              11 (', ')
                LOAD_ATTR               17 (join + NULL|self)
                LOAD_FAST_BORROW         6 (bad)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L17)
       L16:     LOAD_CONST               0 ('')

 641   L17:     LOAD_CONST               7 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 647            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L18:     SWAP                     2
                POP_TOP

 640            SWAP                     2
                STORE_FAST               5 (t)
                RERAISE                  0
ExceptionTable:
  L8 to L10 -> L18 [2]
  L11 to L13 -> L18 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA26A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 650>:
650           RESUME                   0
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

Disassembly of <code object check_tenant_route_invariants at 0x0000018C17D8B290, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 650>:
 650            RESUME                   0

 651            BUILD_LIST               0
                STORE_FAST               1 (out)

 652            LOAD_GLOBAL              1 (_read_text + NULL)
                LOAD_GLOBAL              3 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_GLOBAL              4 (TENANT_ROUTE_FILE)
                BINARY_OP               11 (/)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               0 ('')
        L1:     STORE_FAST               2 (src)

 653            LOAD_GLOBAL              6 (TENANT_ROUTE_REQUIRED_TOKENS)
                GET_ITER
        L2:     FOR_ITER                62 (to L7)
                STORE_FAST               3 (tok)

 654            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 655            LOAD_CONST               1 ('tenant_route:token:')
                LOAD_FAST_BORROW         3 (tok)
                LOAD_CONST               2 (slice(None, 60, None))
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                BUILD_STRING             2

 656            LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (tok, src)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L3)
                NOT_TAKEN
                LOAD_CONST               3 ('PASS')
                JUMP_FORWARD             1 (to L4)
        L3:     LOAD_CONST               4 ('FAIL')

 657    L4:     LOAD_CONST               5 ('tenant_incidents.py carries: ')
                LOAD_FAST_BORROW         3 (tok)
                FORMAT_SIMPLE
                BUILD_STRING             2

 658            LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (tok, src)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN
                LOAD_CONST               0 ('')
                JUMP_FORWARD             1 (to L6)
        L5:     LOAD_CONST               6 ('token missing')

 654    L6:     LOAD_CONST               7 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           64 (to L2)

 653    L7:     END_FOR
                POP_ITER

 660            LOAD_GLOBAL             12 (TENANT_ROUTE_FORBIDDEN_TOKENS)
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

 661            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 662            LOAD_CONST               8 ('tenant_route:read_only')

 663            LOAD_FAST_BORROW         5 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L14)
                NOT_TAKEN
                LOAD_CONST               4 ('FAIL')
                JUMP_FORWARD             1 (to L15)
       L14:     LOAD_CONST               3 ('PASS')

 664   L15:     LOAD_CONST               9 ('tenant_incidents.py declares no mutation route on /incidents')

 665            LOAD_FAST_BORROW         5 (bad)
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

 661   L17:     LOAD_CONST               7 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 667            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L18:     SWAP                     2
                POP_TOP

 660            SWAP                     2
                STORE_FAST               4 (t)
                RERAISE                  0
ExceptionTable:
  L8 to L10 -> L18 [2]
  L11 to L13 -> L18 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA22E0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 670>:
670           RESUME                   0
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

Disassembly of <code object check_daily_runner_watch at 0x0000018C17D87850, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 670>:
 670            RESUME                   0

 671            BUILD_LIST               0
                STORE_FAST               1 (out)

 672            LOAD_GLOBAL              1 (_read_text + NULL)
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

 673            LOAD_GLOBAL              6 (DAILY_RUNNER_REQUIRED_TOKENS)
                GET_ITER
        L2:     FOR_ITER                62 (to L7)
                STORE_FAST               3 (tok)

 674            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 675            LOAD_CONST               1 ('daily_runner:token:')
                LOAD_FAST_BORROW         3 (tok)
                LOAD_CONST               2 (slice(None, 60, None))
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                BUILD_STRING             2

 676            LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (tok, src)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L3)
                NOT_TAKEN
                LOAD_CONST               3 ('PASS')
                JUMP_FORWARD             1 (to L4)
        L3:     LOAD_CONST               4 ('FAIL')

 677    L4:     LOAD_CONST               5 ('run_daily_ops_checklist_report.py carries: ')
                LOAD_FAST_BORROW         3 (tok)
                FORMAT_SIMPLE
                BUILD_STRING             2

 678            LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (tok, src)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN
                LOAD_CONST               0 ('')
                JUMP_FORWARD             1 (to L6)
        L5:     LOAD_CONST               6 ('token missing')

 674    L6:     LOAD_CONST               7 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           64 (to L2)

 673    L7:     END_FOR
                POP_ITER

 680            LOAD_GLOBAL             13 (_strip_python_comments_and_strings + NULL)
                LOAD_FAST_BORROW         2 (src)
                CALL                     1
                STORE_FAST               4 (executable)

 681            LOAD_GLOBAL             14 (DAILY_RUNNER_FORBIDDEN_TOKENS)
                GET_ITER
                LOAD_FAST_AND_CLEAR      5 (t)
                SWAP                     2
        L8:     BUILD_LIST               0
                SWAP                     2
        L9:     FOR_ITER                13 (to L12)
                STORE_FAST_LOAD_FAST    85 (t, t)
                LOAD_FAST_BORROW         4 (executable)
                CONTAINS_OP              0 (in)
       L10:     POP_JUMP_IF_TRUE         3 (to L11)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L9)
       L11:     LOAD_FAST_BORROW         5 (t)
                LIST_APPEND              2
                JUMP_BACKWARD           15 (to L9)
       L12:     END_FOR
                POP_ITER
       L13:     STORE_FAST               6 (bad)
                STORE_FAST               5 (t)

 682            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 683            LOAD_CONST               8 ('daily_runner:no_scheduler_or_daemon')

 684            LOAD_FAST_BORROW         6 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L14)
                NOT_TAKEN
                LOAD_CONST               4 ('FAIL')
                JUMP_FORWARD             1 (to L15)
       L14:     LOAD_CONST               3 ('PASS')

 685   L15:     LOAD_CONST               9 ('run_daily_ops_checklist_report.py contains no scheduler / cron / daemonize')

 686            LOAD_FAST_BORROW         6 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L16)
                NOT_TAKEN
                LOAD_CONST              10 ('disqualifying: ')
                LOAD_CONST              11 (', ')
                LOAD_ATTR               17 (join + NULL|self)
                LOAD_FAST_BORROW         6 (bad)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L17)
       L16:     LOAD_CONST               0 ('')

 682   L17:     LOAD_CONST               7 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 688            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L18:     SWAP                     2
                POP_TOP

 681            SWAP                     2
                STORE_FAST               5 (t)
                RERAISE                  0
ExceptionTable:
  L8 to L10 -> L18 [2]
  L11 to L13 -> L18 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA24C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 691>:
691           RESUME                   0
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

Disassembly of <code object check_pagination_invariants at 0x0000018C18048E30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 691>:
691           RESUME                   0

692           BUILD_LIST               0
              STORE_FAST               1 (out)

693           LOAD_GLOBAL              1 (_read_text + NULL)
              LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_GLOBAL              4 (FLEET_ROUTE_FILE)
              BINARY_OP               11 (/)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               0 ('')
      L1:     STORE_FAST               2 (src)

694           LOAD_GLOBAL              6 (FLEET_ROUTE_REQUIRED_TOKENS)
              GET_ITER
      L2:     FOR_ITER                62 (to L7)
              STORE_FAST               3 (tok)

695           LOAD_FAST                1 (out)
              LOAD_ATTR                9 (append + NULL|self)
              LOAD_GLOBAL             11 (_check + NULL)

696           LOAD_CONST               1 ('pagination:token:')
              LOAD_FAST_BORROW         3 (tok)
              LOAD_CONST               2 (slice(None, 60, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

697           LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (tok, src)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               3 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               4 ('FAIL')

698   L4:     LOAD_CONST               5 ('operator_fleet.py carries: ')
              LOAD_FAST_BORROW         3 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

699           LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (tok, src)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               0 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               6 ('token missing')

695   L6:     LOAD_CONST               7 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           64 (to L2)

694   L7:     END_FOR
              POP_ITER

701           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA25B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 704>:
704           RESUME                   0
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

Disassembly of <code object check_dashboard_anchors_present at 0x0000018C1794E9E0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 704>:
704           RESUME                   0

705           BUILD_LIST               0
              STORE_FAST               1 (out)

706           LOAD_GLOBAL              1 (_read_text + NULL)
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

707           LOAD_GLOBAL              6 (DASHBOARD_REQUIRED_ANCHORS)
              GET_ITER
      L2:     FOR_ITER                65 (to L7)
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST   52 (cid, needle)

708           LOAD_FAST_BORROW_LOAD_FAST_BORROW 66 (needle, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

709           LOAD_FAST                1 (out)
              LOAD_ATTR                9 (append + NULL|self)
              LOAD_GLOBAL             11 (_check + NULL)

710           LOAD_CONST               1 ('dashboard:')
              LOAD_FAST_BORROW         3 (cid)
              FORMAT_SIMPLE
              BUILD_STRING             2

711           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               2 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               3 ('FAIL')

712   L4:     LOAD_CONST               4 ('Dashboard anchor present: ')
              LOAD_FAST_BORROW         4 (needle)
              FORMAT_SIMPLE
              BUILD_STRING             2

713           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               0 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               5 ('anchor missing')

709   L6:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           67 (to L2)

707   L7:     END_FOR
              POP_ITER

715           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 718>:
718           RESUME                   0
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

Disassembly of <code object check_pending_calls_wirethrough at 0x0000018C17D6DFC0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 718>:
718            RESUME                   0

719            BUILD_LIST               0
               STORE_FAST               1 (out)

720            LOAD_GLOBAL              1 (_read_text + NULL)
               LOAD_GLOBAL              3 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_GLOBAL              4 (PENDING_CALLS_FILE)
               BINARY_OP               11 (/)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L1:     STORE_FAST               2 (src)

721            LOAD_GLOBAL              6 (PENDING_CALLS_REQUIRED_TOKENS)
               GET_ITER
       L2:     FOR_ITER                62 (to L7)
               STORE_FAST               3 (tok)

722            LOAD_FAST                1 (out)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_GLOBAL             11 (_check + NULL)

723            LOAD_CONST               1 ('pending_calls:token:')
               LOAD_FAST_BORROW         3 (tok)
               LOAD_CONST               2 (slice(None, 60, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

724            LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (tok, src)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               3 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               4 ('FAIL')

725    L4:     LOAD_CONST               5 ('pending_calls.py carries: ')
               LOAD_FAST_BORROW         3 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

726            LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (tok, src)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               0 ('')
               JUMP_FORWARD             1 (to L6)
       L5:     LOAD_CONST               6 ('token missing')

722    L6:     LOAD_CONST               7 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           64 (to L2)

721    L7:     END_FOR
               POP_ITER

728            LOAD_GLOBAL             12 (PENDING_CALLS_REQUIRED_PATTERNS)
               GET_ITER
       L8:     FOR_ITER                62 (to L13)
               STORE_FAST               4 (pat)

729            LOAD_FAST                1 (out)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_GLOBAL             11 (_check + NULL)

730            LOAD_CONST               8 ('pending_calls:pattern:')
               LOAD_FAST_BORROW         4 (pat)
               LOAD_CONST               2 (slice(None, 60, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

731            LOAD_FAST_BORROW_LOAD_FAST_BORROW 66 (pat, src)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN
               LOAD_CONST               3 ('PASS')
               JUMP_FORWARD             1 (to L10)
       L9:     LOAD_CONST               4 ('FAIL')

732   L10:     LOAD_CONST               9 ('pending_calls.py carries fail-open pattern: ')
               LOAD_FAST_BORROW         4 (pat)
               FORMAT_SIMPLE
               BUILD_STRING             2

733            LOAD_FAST_BORROW_LOAD_FAST_BORROW 66 (pat, src)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               0 ('')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST              10 ('pattern missing')

729   L12:     LOAD_CONST               7 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           64 (to L8)

728   L13:     END_FOR
               POP_ITER

737            LOAD_GLOBAL             15 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         2 (src)
               CALL                     1
               STORE_FAST               5 (executable)

738            BUILD_LIST               0
               STORE_FAST               6 (bad)

739            LOAD_CONST              16 (('trip_breaker(', 'reset_breaker(', 'current_breaker_state('))
               GET_ITER
      L14:     FOR_ITER                37 (to L17)
               STORE_FAST               3 (tok)

745            LOAD_FAST_BORROW_LOAD_FAST_BORROW 53 (tok, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L15)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L14)
      L15:     LOAD_FAST_BORROW         3 (tok)
               LOAD_CONST              11 ('current_breaker_state(')
               COMPARE_OP             119 (bool(!=))
               POP_JUMP_IF_TRUE         3 (to L16)
               NOT_TAKEN
               JUMP_BACKWARD           20 (to L14)

746   L16:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_FAST_BORROW         3 (tok)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           39 (to L14)

739   L17:     END_FOR
               POP_ITER

747            LOAD_FAST                1 (out)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_GLOBAL             11 (_check + NULL)

748            LOAD_CONST              12 ('pending_calls:no_breaker_mutation')

749            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L18)
               NOT_TAKEN
               LOAD_CONST               4 ('FAIL')
               JUMP_FORWARD             1 (to L19)
      L18:     LOAD_CONST               3 ('PASS')

750   L19:     LOAD_CONST              13 ('pending_calls.py does NOT mutate breaker state')

751            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L20)
               NOT_TAKEN
               LOAD_CONST              14 ('disqualifying: ')
               LOAD_CONST              15 (', ')
               LOAD_ATTR               17 (join + NULL|self)
               LOAD_FAST_BORROW         6 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L21)
      L20:     LOAD_CONST               0 ('')

747   L21:     LOAD_CONST               7 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

753            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 756>:
756           RESUME                   0
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

Disassembly of <code object check_event_contract_has_pas189_types at 0x0000018C180483B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 756>:
756           RESUME                   0

757           BUILD_LIST               0
              STORE_FAST               1 (out)

758           LOAD_GLOBAL              1 (_read_text + NULL)
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

759           LOAD_GLOBAL              6 (EVENT_CONTRACT_REQUIRED_EVENT_TYPES)
              GET_ITER
      L2:     FOR_ITER                63 (to L7)
              STORE_FAST               3 (tok)

760           LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               4 (ok)

761           LOAD_FAST                1 (out)
              LOAD_ATTR                9 (append + NULL|self)
              LOAD_GLOBAL             11 (_check + NULL)

762           LOAD_CONST               1 ('contract:event:')
              LOAD_FAST_BORROW         3 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

763           LOAD_FAST_BORROW         4 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               2 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               3 ('FAIL')

764   L4:     LOAD_CONST               4 ('events/contract.py carries event_type literal: ')
              LOAD_FAST_BORROW         3 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

765           LOAD_FAST_BORROW         4 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               0 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               5 ('literal missing — contract drift')

761   L6:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           65 (to L2)

759   L7:     END_FOR
              POP_ITER

767           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 770>:
770           RESUME                   0
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

Disassembly of <code object check_main_mounts_tenant_router at 0x0000018C1794EF50, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 770>:
770           RESUME                   0

771           BUILD_LIST               0
              STORE_FAST               1 (out)

772           LOAD_GLOBAL              1 (_read_text + NULL)
              LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app/main.py')
              BINARY_OP               11 (/)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 ('')
      L1:     STORE_FAST               2 (src)

773           LOAD_GLOBAL              4 (MAIN_PY_REQUIRED_MOUNT_TOKENS)
              GET_ITER
      L2:     FOR_ITER                70 (to L7)
              STORE_FAST               3 (tok)

774           LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               4 (ok)

775           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

776           LOAD_CONST               2 ('main:mount:')
              LOAD_FAST_BORROW         3 (tok)
              LOAD_CONST               3 (slice(None, 60, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

777           LOAD_FAST_BORROW         4 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               4 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               5 ('FAIL')

778   L4:     LOAD_CONST               6 ('app/main.py contains: ')
              LOAD_FAST_BORROW         3 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

779           LOAD_FAST_BORROW         4 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               1 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               7 ('mount missing — route inaccessible')

775   L6:     LOAD_CONST               8 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           72 (to L2)

773   L7:     END_FOR
              POP_ITER

781           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181152F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 784>:
784           RESUME                   0
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

Disassembly of <code object check_self_no_env_or_db at 0x0000018C17EA44A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 784>:
784            RESUME                   0

785            BUILD_LIST               0
               STORE_FAST               1 (out)

786            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_GLOBAL              2 (__file__)
               CALL                     1
               STORE_FAST               2 (fp)

787            LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (fp)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L1:     STORE_FAST               3 (src)

788            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               4 (executable)

789            BUILD_LIST               0
               STORE_FAST               5 (bad)

790            LOAD_FAST_BORROW         4 (executable)
               LOAD_ATTR                9 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L2:     FOR_ITER               199 (to L9)
               STORE_FAST               6 (line)

791            LOAD_FAST_BORROW         6 (line)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0
               STORE_FAST               7 (stripped)

792            LOAD_FAST_BORROW         7 (stripped)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN

793            JUMP_BACKWARD           29 (to L2)

794    L3:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              15 (('import dotenv', 'from dotenv'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L4)
               NOT_TAKEN

795            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               1 ('dotenv import')
               CALL                     1
               POP_TOP

796    L4:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              16 (('import supabase', 'from supabase'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L5)
               NOT_TAKEN

797            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               2 ('supabase import')
               CALL                     1
               POP_TOP

798    L5:     LOAD_CONST               3 ('load_dotenv(')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       18 (to L6)
               NOT_TAKEN

799            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               4 ('load_dotenv() call')
               CALL                     1
               POP_TOP

800    L6:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              17 (('os.environ[', 'getenv('))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L7)
               NOT_TAKEN

801            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               5 ('environ read')
               CALL                     1
               POP_TOP

802    L7:     LOAD_CONST               6 ('get_supabase')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD          182 (to L2)

803    L8:     LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               7 ('supabase client call')
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          201 (to L2)

790    L9:     END_FOR
               POP_ITER

804            LOAD_CONST              18 (('subprocess.run(', 'subprocess.call(', 'requests.get(', 'requests.post(', 'httpx.get(', 'httpx.post(', 'urllib.request.urlopen(', 'git push', 'railway deploy'))
               GET_ITER
      L10:     FOR_ITER                28 (to L12)
               STORE_FAST               8 (tok)

815            LOAD_FAST_BORROW_LOAD_FAST_BORROW 132 (tok, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L11)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L10)

816   L11:     LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_FAST_BORROW         8 (tok)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L10)

804   L12:     END_FOR
               POP_ITER

817            LOAD_FAST                1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             17 (_check + NULL)

818            LOAD_CONST               8 ('self_check:no_env_or_db_or_network')

819            LOAD_FAST_BORROW         5 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L13)
               NOT_TAKEN
               LOAD_CONST               9 ('FAIL')
               JUMP_FORWARD             1 (to L14)
      L13:     LOAD_CONST              10 ('PASS')

820   L14:     LOAD_CONST              11 ('PAS189 readiness checker never reads .env / touches DB / hits network')

821            LOAD_FAST_BORROW         5 (bad)
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

817   L16:     LOAD_CONST              14 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

823            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181153E0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 830>:
830           RESUME                   0
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

Disassembly of <code object _aggregate at 0x0000018C1800B230, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 830>:
 830            RESUME                   0

 831            LOAD_FAST_BORROW         0 (checks)
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

 833            LOAD_CONST               3 ('verdict')
                LOAD_FAST_BORROW         2 (blockers)
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L9)
                NOT_TAKEN
                LOAD_GLOBAL              4 (VERDICT_NOT_READY)
                JUMP_FORWARD             5 (to L10)
        L9:     LOAD_GLOBAL              6 (VERDICT_READY)

 834   L10:     LOAD_CONST               4 ('blockers')
                LOAD_FAST_BORROW         2 (blockers)

 835            LOAD_CONST               5 ('info')
                BUILD_LIST               0

 832            BUILD_MAP                3
                RETURN_VALUE

  --   L11:     SWAP                     2
                POP_TOP

 831            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L11 [2]
  L4 to L5 -> L11 [2]
  L6 to L8 -> L11 [2]

Disassembly of <code object __annotate__ at 0x0000018C181154D0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 839>:
839           RESUME                   0
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

Disassembly of <code object _operator_actions at 0x0000018C180488F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 839>:
839           RESUME                   0

840           BUILD_LIST               0
              STORE_FAST               1 (out)

841           LOAD_FAST_BORROW         0 (checks)
              GET_ITER
      L1:     FOR_ITER               109 (to L5)
              STORE_FAST               2 (c)

842           LOAD_FAST_BORROW         2 (c)
              LOAD_CONST               0 ('status')
              BINARY_OP               26 ([])
              LOAD_CONST               1 ('FAIL')
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

843           JUMP_BACKWARD           19 (to L1)

844   L2:     LOAD_FAST_BORROW         2 (c)
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

845           LOAD_FAST                1 (out)
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

841   L5:     END_FOR
              POP_ITER

846           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181155C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 849>:
849           RESUME                   0
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

Disassembly of <code object evaluate at 0x0000018C17D7C560, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 849>:
849           RESUME                   0

850           BUILD_LIST               0
              STORE_FAST               1 (checks)

851           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              3 (check_pas189_files_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

852           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              5 (check_prior_phases_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

853           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              7 (check_memory_review_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

854           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              9 (check_worker_off_by_default + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

855           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             11 (check_doc_required_clauses + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

856           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             13 (check_doc_no_forbidden_scope + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

857           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             15 (check_service_no_forbidden_imports + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

858           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             17 (check_service_no_scheduler_or_loop + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

859           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             19 (check_policy_invariants + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

860           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             21 (check_cache_inv_invariants + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

861           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             23 (check_tenant_projection_invariants + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

862           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             25 (check_tenant_route_invariants + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

863           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             27 (check_daily_runner_watch + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

864           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             29 (check_pagination_invariants + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

865           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             31 (check_dashboard_anchors_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

866           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             33 (check_pending_calls_wirethrough + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

867           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             35 (check_event_contract_has_pas189_types + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

868           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             37 (check_main_mounts_tenant_router + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

869           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             39 (check_self_no_env_or_db + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

871           LOAD_GLOBAL             41 (_aggregate + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1
              STORE_FAST               2 (agg)

873           LOAD_CONST               0 ('phase')
              LOAD_CONST               1 ('PAS189')

874           LOAD_CONST               2 ('generated_at')
              LOAD_GLOBAL             43 (_now_iso + NULL)
              CALL                     0

875           LOAD_CONST               3 ('verdict')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])

876           LOAD_CONST               4 ('ready')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])
              LOAD_GLOBAL             44 (VERDICT_READY)
              COMPARE_OP              72 (==)

877           LOAD_CONST               5 ('blocker_count')
              LOAD_GLOBAL             47 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               6 ('blockers')
              BINARY_OP               26 ([])
              CALL                     1

878           LOAD_CONST               7 ('info_count')
              LOAD_GLOBAL             47 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               8 ('info')
              BINARY_OP               26 ([])
              CALL                     1

879           LOAD_CONST               9 ('check_count')
              LOAD_GLOBAL             47 (len + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

880           LOAD_CONST              10 ('pass_count')
              LOAD_GLOBAL             49 (sum + NULL)
              LOAD_CONST              11 (<code object <genexpr> at 0x0000018C180533F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 880>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

881           LOAD_CONST              12 ('fail_count')
              LOAD_GLOBAL             49 (sum + NULL)
              LOAD_CONST              13 (<code object <genexpr> at 0x0000018C18053090, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 881>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

882           LOAD_CONST              14 ('checks')
              LOAD_FAST_BORROW         1 (checks)

883           LOAD_CONST              15 ('operator_actions')
              LOAD_GLOBAL             51 (_operator_actions + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

872           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C180533F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 880>:
 880           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C18053090, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 881>:
 881           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C18115980, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 890>:
890           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C179C3C30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 890>:
890           RESUME                   0

891           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

892           LOAD_CONST               0 ('pas189_operational_wirethrough_readiness_check')

894           LOAD_CONST               1 ('PAS189 — Operational wire-through readiness gate. Read-only — never reads .env, never touches Supabase, never executes a deploy / migration.')

891           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

900           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               3 ('--repo-root')
              LOAD_GLOBAL              6 (_REPO_ROOT_DEFAULT)
              LOAD_CONST               4 (('default',))
              CALL_KW                  2
              POP_TOP

901           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               5 ('--output')
              LOAD_GLOBAL              8 (REPORT_FILENAME)
              LOAD_CONST               4 (('default',))
              CALL_KW                  2
              POP_TOP

902           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               6 ('--json')
              LOAD_CONST               7 ('store_true')
              LOAD_CONST               8 (('action',))
              CALL_KW                  2
              POP_TOP

903           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               9 ('--summary-only')
              LOAD_CONST               7 ('store_true')
              LOAD_CONST               8 (('action',))
              CALL_KW                  2
              POP_TOP

904           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST              10 ('--strict')
              LOAD_CONST               7 ('store_true')
              LOAD_CONST               8 (('action',))
              CALL_KW                  2
              POP_TOP

905           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18115A70, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 908>:
908           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C17D8E300, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 908>:
908           RESUME                   0

909           LOAD_GLOBAL              1 (print + NULL)

910           LOAD_CONST               0 ('[PAS189] verdict=')
              LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               1 ('verdict')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               2 (' blockers=')

911           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               3 ('blocker_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' info=')

912           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               5 ('info_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' checks=')

913           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               7 ('check_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' pass=')

914           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               9 ('pass_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              10 (' fail=')

915           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              11 ('fail_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE

910           BUILD_STRING            12

909           CALL                     1
              POP_TOP

917           LOAD_FAST_BORROW         0 (report)
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

918           LOAD_FAST_BORROW         1 (actions)
              TO_BOOL
              POP_JUMP_IF_FALSE       93 (to L5)
              NOT_TAKEN

919           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              13 ('[PAS189] operator actions:')
              CALL                     1
              POP_TOP

920           LOAD_FAST_BORROW         1 (actions)
              LOAD_CONST              14 (slice(None, 25, None))
              BINARY_OP               26 ([])
              GET_ITER
      L2:     FOR_ITER                17 (to L3)
              STORE_FAST               2 (a)

921           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              15 ('  - ')
              LOAD_FAST_BORROW         2 (a)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L2)

920   L3:     END_FOR
              POP_ITER

922           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         1 (actions)
              CALL                     1
              LOAD_SMALL_INT          25
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       34 (to L4)
              NOT_TAKEN

923           LOAD_GLOBAL              1 (print + NULL)
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

922   L4:     LOAD_CONST              18 (None)
              RETURN_VALUE

918   L5:     LOAD_CONST              18 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024930, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 926>:
926           RESUME                   0
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

Disassembly of <code object _write_report at 0x0000018C179C3E10, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 926>:
 926           RESUME                   0

 927           NOP

 928   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

 929           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

 930           LOAD_CONST               3 ('utf-8')

 928           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 932           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

 933   L4:     LOAD_GLOBAL             11 (print + NULL)

 934           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

 935           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

 934           BUILD_STRING             4

 936           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

 933           LOAD_CONST               7 (('file',))
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

 932   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18115110, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 940>:
940           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17D88FF0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas189_operational_wirethrough_readiness_check.py", line 940>:
 940            RESUME                   0

 941            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 942            NOP

 943    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 947    L2:     LOAD_GLOBAL             10 (os)
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

 948            LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               21 (isdir + NULL|self)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L4)
                NOT_TAKEN

 949            LOAD_GLOBAL             23 (print + NULL)
                LOAD_CONST               2 ('error: --repo-root not a directory: ')
                LOAD_FAST                4 (repo_root)
                FORMAT_SIMPLE
                BUILD_STRING             2
                LOAD_GLOBAL             24 (sys)
                LOAD_ATTR               26 (stderr)
                LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

 950            LOAD_SMALL_INT           2
                RETURN_VALUE

 952    L4:     LOAD_GLOBAL             29 (evaluate + NULL)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                STORE_FAST               5 (report)

 954            LOAD_FAST                2 (args)
                LOAD_ATTR               30 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L5)
                NOT_TAKEN

 955            LOAD_GLOBAL             33 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               34 (output)
                LOAD_FAST                5 (report)
                CALL                     2
                POP_TOP

 957    L5:     LOAD_GLOBAL             37 (_print_summary + NULL)
                LOAD_FAST                5 (report)
                CALL                     1
                POP_TOP

 959            LOAD_FAST                2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L6)
                NOT_TAKEN

 960            LOAD_GLOBAL             23 (print + NULL)
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

 962    L6:     LOAD_FAST                5 (report)
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

 944            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L17)
                NOT_TAKEN
                STORE_FAST               3 (e)

 945    L9:     LOAD_FAST                3 (e)
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

 944   L17:     RERAISE                  0

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
