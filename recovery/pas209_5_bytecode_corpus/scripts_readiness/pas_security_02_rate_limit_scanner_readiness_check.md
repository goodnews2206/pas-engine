# scripts_readiness/pas_security_02_rate_limit_scanner_readiness_check

- **pyc:** `scripts\__pycache__\pas_security_02_rate_limit_scanner_readiness_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/pas_security_02_rate_limit_scanner_readiness_check.py`
- **co_filename (from bytecode):** `scripts/pas_security_02_rate_limit_scanner_readiness_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS-SECURITY-02 — Rate-limit + scanner + key-rotation readiness gate.

Deterministic, non-mutating evaluator for "is PAS-SECURITY-02
wired correctly and free of regressions in the
PAS160-PAS-SECURITY-01 doctrine?".

Walks the repo and verifies:

  * PAS160-PAS181 + PAS-SECURITY-01 readiness scripts still
    exist.
  * PAS-SECURITY-02 surfaces exist:
      - scripts/migrate_v31_rate_limit_counters.sql
      - scripts/migrate_v32_api_key_rotation_events.sql
      - app/services/security/rate_limit.py
      - app/services/security/rate_limit_store.py
      - app/services/security/dependency_scanner.py
      - app/services/security/api_key_rotation.py
      - app/routes/security_api_key_rotation.py
      - scripts/security_dependency_audit.py
      - scripts/pas_security_02_rate_limit_scanner_readiness_check.py
      - docs/pas_security_02_rate_limit_scanner_key_rotation.md
      - tests/mvp/test_pas_security_02_rate_limit_scanner.py
  * v31 SQL: PROPOSAL ONLY, closed surface enum, tenant
    denied, service_role INSERT/UPDATE/aged-DELETE.
  * v32 SQL: PROPOSAL ONLY, closed status enum, sha256
    fingerprint pin, restricted operator UPDATE, no raw key
    column.
  * rate_limit service surface tokens present + no raw IP
    storage.
  * rate_limit_store has process-local fallback marker.
  * dependency_scanner is report-only (no auto-fix tokens).
  * api_key_rotation has fingerprint helper + strict
    transition map + no raw key echo.
  * api-key rotation routes mounted at /tenant/api-key and
    /ops/api-key-rotation.
  * email_ingestion.py wires check_rate_limit (surface
    email_ingestion).
  * slack_command.py wires check_rate_limit (surface
    slack_command).
  * No raw API key column / no token echo in security
    files.
  * No auto-fix tokens (pip install / npm audit fix / etc.).
  * No Gmail / OAuth / IMAP / POP3 / Composio / TrustClaw /
    embeddings / vector / LLM imports.
  * Memory Review (PAS147-PAS158) untouched.
  * audit_service still has no UPDATE / DELETE helpers.
  * Event contract registers PAS-SECURITY-02 events.
  * Worker still OFF by default.
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

`__annotate__`, `_aggregate`, `_build_parser`, `_check`, `_now_iso`, `_operator_actions`, `_print_summary`, `_read_text`, `_strip_python_comments_and_strings`, `_write_report`, `check_audit_cli`, `check_audit_service_invariant`, `check_dependency_scanner`, `check_doc_required_clauses`, `check_email_ingestion_rate_limit_wired`, `check_event_contract`, `check_files_present`, `check_main_router_mounts`, `check_memory_review_intact`, `check_no_forbidden_imports`, `check_no_inbox_scan_tokens`, `check_prior_phases_intact`, `check_rate_limit_service`, `check_rate_limit_store`, `check_rotation_routes`, `check_rotation_service`, `check_self_no_env_or_db`, `check_slack_command_rate_limit_wired`, `check_v31_sql`, `check_v32_sql`, `check_worker_off_by_default`, `evaluate`, `main`

## Env-key candidates

`BLOCK`, `FAIL`, `INFO`, `NOT_READY`, `PASS`, `READY`

## String constants (redacted where noted)

- '\nPAS-SECURITY-02 — Rate-limit + scanner + key-rotation readiness gate.\n\nDeterministic, non-mutating evaluator for "is PAS-SECURITY-02\nwired correctly and free of regressions in the\nPAS160-PAS-SECURITY-01 doctrine?".\n\nWalks the repo and verifies:\n\n  * PAS160-PAS181 + PAS-SECURITY-01 readiness scripts still\n    exist.\n  * PAS-SECURITY-02 surfaces exist:\n      - scripts/migrate_v31_rate_limit_counters.sql\n      - scripts/migrate_v32_api_key_rotation_events.sql\n      - app/services/security/rate_limit.py\n      - app/services/security/rate_limit_store.py\n      - app/services/security/dependency_scanner.py\n      - app/services/security/api_key_rotation.py\n      - app/routes/security_api_key_rotation.py\n      - scripts/security_dependency_audit.py\n      - scripts/pas_security_02_rate_limit_scanner_readiness_check.py\n      - docs/pas_security_02_rate_limit_scanner_key_rotation.md\n      - tests/mvp/test_pas_security_02_rate_limit_scanner.py\n  * v31 SQL: PROPOSAL ONLY, closed surface enum, tenant\n    denied, service_role INSERT/UPDATE/aged-DELETE.\n  * v32 SQL: PROPOSAL ONLY, closed status enum, sha256\n    fingerprint pin, restricted operator UPDATE, no raw key\n    column.\n  * rate_limit service surface tokens present + no raw IP\n    storage.\n  * rate_limit_store has process-local fallback marker.\n  * dependency_scanner is report-only (no auto-fix tokens).\n  * api_key_rotation has fingerprint helper + strict\n    transition map + no raw key echo.\n  * api-key rotation routes mounted at /tenant/api-key and\n    /ops/api-key-rotation.\n  * email_ingestion.py wires check_rate_limit (surface\n    email_ingestion).\n  * slack_command.py wires check_rate_limit (surface\n    slack_command).\n  * No raw API key column / no token echo in security\n    files.\n  * No auto-fix tokens (pip install / npm audit fix / etc.).\n  * No Gmail / OAuth / IMAP / POP3 / Composio / TrustClaw /\n    embeddings / vector / LLM imports.\n  * Memory Review (PAS147-PAS158) untouched.\n  * audit_service still has no UPDATE / DELETE helpers.\n  * Event contract registers PAS-SECURITY-02 events.\n  * Worker still OFF by default.\n  * Supports --summary-only / --json.\n  * Exits 0 ready, 1 blockers, 2 bad args.\n  * Never reads .env.\n  * Never touches production data.\n'
- 'utf-8'
- 'READY'
- 'NOT_READY'
- 'BLOCK'
- 'INFO'
- 'severity'
- 'detail'
- 'pas_security_02_rate_limit_scanner_readiness_report.json'
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
- 'Required PAS-SECURITY-02 file present: '
- 'missing'
- 'prior_phase:'
- 'Prior-phase readiness script intact: '
- 'missing — PAS-SECURITY-02 must not delete'
- 'memory_review:'
- 'Memory Review file present: '
- 'Memory Review file deleted — PAS-SECURITY-02 must not touch'
- 'app'
- 'services'
- 'ingestion'
- 'worker.py'
- '_ENV_FLAG_ENABLED_LITERAL = "true"'
- "_ENV_FLAG_ENABLED_LITERAL = 'true'"
- 'worker:off_by_default'
- 'Pending-call worker is OFF by default'
- 'missing strict enable-literal constant'
- 'scripts'
- 'migrate_v31_rate_limit_counters.sql'
- 'v31_sql:proposal_only'
- 'proposal only'
- "v31 SQL carries 'PROPOSAL ONLY' guardrail"
- 'missing label'
- 'v31_sql:do_not_execute'
- 'do not execute'
- "v31 SQL carries 'DO NOT EXECUTE' trailer"
- 'missing trailer'
- 'CREATE TABLE IF NOT EXISTS pas_rate_limit_counters'
- 'v31_sql:table_present'
- 'v31 SQL creates pas_rate_limit_counters'
- 'v31_sql:closed_surface_enum'
- 'v31 SQL carries the closed surface enum'
- 'pas_rate_limit_counters_tenant_no_select'
- 'pas_rate_limit_counters_tenant_no_insert'
- 'pas_rate_limit_counters_tenant_no_update'
- 'pas_rate_limit_counters_tenant_no_delete'
- 'pas_rate_limit_counters_service_role_aged_delete'
- 'v31_sql:tenant_denied_service_role_aged_delete'
- 'v31 SQL denies tenant all ops + service_role aged-DELETE policy'
- 'migrate_v32_api_key_rotation_events.sql'
- 'v32_sql:proposal_only'
- "v32 SQL carries 'PROPOSAL ONLY' guardrail"
- 'v32_sql:do_not_execute'
- "v32 SQL carries 'DO NOT EXECUTE' trailer"
- 'CREATE TABLE IF NOT EXISTS pas_api_key_rotation_events'
- 'v32_sql:table_present'
- 'v32 SQL creates pas_api_key_rotation_events'
- 'v32_sql:closed_status_enum'
- 'v32 SQL carries the closed status enum'
- 'raw_api_key'
- ' api_key '
- 'v32_sql:no_raw_api_key_column'
- 'v32 SQL does NOT define a raw API-key column'
- 'raw api_key column detected'
- "'^[0-9a-f]{64}$'"
- 'v32_sql:fingerprint_check_constraint'
- 'v32 SQL pins fingerprint columns to sha256 hex'
- 'pas_api_key_rotation_events_tenant_select'
- 'pas_api_key_rotation_events_tenant_insert'
- 'pas_api_key_rotation_events_tenant_no_update'
- 'pas_api_key_rotation_events_tenant_no_delete'
- 'pas_api_key_rotation_events_service_role_review_update'
- 'pas_api_key_rotation_events_service_role_no_delete'
- 'WITH CHECK'
- 'v32_sql:append_only_with_review_update'
- 'v32 SQL denies tenant UPDATE/DELETE; service_role restricted UPDATE; no DELETE'
- 'security'
- 'rate_limit.py'
- 'rate_limit:'
- 'rate_limit module exports '
- 'missing token '
- 'rate_limit_store.py'
- 'rate_limit_store:'
- 'rate_limit_store module exports '
- 'dependency_scanner.py'
- 'scanner:'
- 'dependency_scanner exports '
- 'scanner:no_auto_fix'
- 'dependency_scanner does not call auto-fix / upgrade helpers'
- 'disqualifying tokens: '
- 'api_key_rotation.py'
- 'rotation:'
- 'api_key_rotation module exports '
- 'routes'
- 'security_api_key_rotation.py'
- 'rotation_routes:'
- 'rotation routes file declares '
- 'rotation_routes:no_raw_key_storage_or_echo'
- 'rotation routes never reference raw_api_key / raw_ip / user_agent_raw'
- 'security_dependency_audit.py'
- 'audit_cli:'
- 'security_dependency_audit CLI exports '
- 'audit_cli:no_auto_fix'
- 'security_dependency_audit CLI does not call auto-fix / upgrade'
- 'email_ingestion.py'
- 'check_rate_limit('
- 'surface="email_ingestion"'
- 'rate_limit_wired:email_ingestion'
- 'email_ingestion route wires check_rate_limit(surface=email_ingestion)'
- 'slack_command.py'
- 'surface="slack_command"'
- 'rate_limit_wired:slack_command'
- 'slack_command route wires check_rate_limit(surface=slack_command)'
- 'operator'
- 'audit_service.py'
- 'audit_service:append_only_carry'
- 'Audit service still has no UPDATE / DELETE mutation helpers (carry-forward invariant)'
- 'events'
- 'contract.py'
- 'events:'
- 'Event contract registers '
- 'missing event type '
- 'main.py'
- 'main:mount:'
- 'app/main.py mounts '
- 'missing mount token '
- 'app/services/security/rate_limit.py'
- 'forbidden_import:'
- 'No forbidden imports: '
- 'forbidden import prefixes: '
- 'no_inbox_scan:'
- 'No inbox-scanning tokens: '
- 'inbox-scan tokens present: '
- 'docs'
- 'pas_security_02_rate_limit_scanner_key_rotation.md'
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
- 'PAS-SECURITY-02 readiness checker never reads .env / touches DB'
- 'disqualifying patterns: '
- 'checks'
- 'verdict'
- 'blockers'
- 'info'
- 'List[str]'
- ' — '
- 'see report'
- 'phase'
- 'PAS-SECURITY-02'
- 'generated_at'
- 'ready'
- 'blocker_count'
- 'info_count'
- 'check_count'
- 'pass_count'
- 'fail_count'
- 'operator_actions'
- 'argparse.ArgumentParser'
- 'pas_security_02_rate_limit_scanner_readiness_check'
- 'PAS-SECURITY-02 — Evaluate rate-limit + scanner + API-key rotation surfaces. Read-only — never reads .env, never touches Supabase, never runs a migration.'
- '--repo-root'
- '--output'
- '--json'
- 'store_true'
- '--summary-only'
- '--strict'
- 'report'
- 'None'
- '[PAS-SECURITY-02] verdict='
- ' blockers='
- ' info='
- ' checks='
- ' pass='
- ' fail='
- '[PAS-SECURITY-02] operator actions:'
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

   1           LOAD_CONST               0 ('\nPAS-SECURITY-02 — Rate-limit + scanner + key-rotation readiness gate.\n\nDeterministic, non-mutating evaluator for "is PAS-SECURITY-02\nwired correctly and free of regressions in the\nPAS160-PAS-SECURITY-01 doctrine?".\n\nWalks the repo and verifies:\n\n  * PAS160-PAS181 + PAS-SECURITY-01 readiness scripts still\n    exist.\n  * PAS-SECURITY-02 surfaces exist:\n      - scripts/migrate_v31_rate_limit_counters.sql\n      - scripts/migrate_v32_api_key_rotation_events.sql\n      - app/services/security/rate_limit.py\n      - app/services/security/rate_limit_store.py\n      - app/services/security/dependency_scanner.py\n      - app/services/security/api_key_rotation.py\n      - app/routes/security_api_key_rotation.py\n      - scripts/security_dependency_audit.py\n      - scripts/pas_security_02_rate_limit_scanner_readiness_check.py\n      - docs/pas_security_02_rate_limit_scanner_key_rotation.md\n      - tests/mvp/test_pas_security_02_rate_limit_scanner.py\n  * v31 SQL: PROPOSAL ONLY, closed surface enum, tenant\n    denied, service_role INSERT/UPDATE/aged-DELETE.\n  * v32 SQL: PROPOSAL ONLY, closed status enum, sha256\n    fingerprint pin, restricted operator UPDATE, no raw key\n    column.\n  * rate_limit service surface tokens present + no raw IP\n    storage.\n  * rate_limit_store has process-local fallback marker.\n  * dependency_scanner is report-only (no auto-fix tokens).\n  * api_key_rotation has fingerprint helper + strict\n    transition map + no raw key echo.\n  * api-key rotation routes mounted at /tenant/api-key and\n    /ops/api-key-rotation.\n  * email_ingestion.py wires check_rate_limit (surface\n    email_ingestion).\n  * slack_command.py wires check_rate_limit (surface\n    slack_command).\n  * No raw API key column / no token echo in security\n    files.\n  * No auto-fix tokens (pip install / npm audit fix / etc.).\n  * No Gmail / OAuth / IMAP / POP3 / Composio / TrustClaw /\n    embeddings / vector / LLM imports.\n  * Memory Review (PAS147-PAS158) untouched.\n  * audit_service still has no UPDATE / DELETE helpers.\n  * Event contract registers PAS-SECURITY-02 events.\n  * Worker still OFF by default.\n  * Supports --summary-only / --json.\n  * Exits 0 ready, 1 blockers, 2 bad args.\n  * Never reads .env.\n  * Never touches production data.\n')
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

  83           LOAD_CONST              12 ('INFO')
               STORE_NAME              28 (SEVERITY_INFO)

  86           LOAD_CONST              82 (('scripts/migrate_v31_rate_limit_counters.sql', 'scripts/migrate_v32_api_key_rotation_events.sql', 'app/services/security/rate_limit.py', 'app/services/security/rate_limit_store.py', 'app/services/security/dependency_scanner.py', 'app/services/security/api_key_rotation.py', 'app/routes/security_api_key_rotation.py', 'scripts/security_dependency_audit.py', 'scripts/pas_security_02_rate_limit_scanner_readiness_check.py', 'docs/pas_security_02_rate_limit_scanner_key_rotation.md', 'tests/mvp/test_pas_security_02_rate_limit_scanner.py'))
               STORE_NAME              29 (REQUIRED_FILES)

 101           LOAD_CONST              83 (('scripts/pas160_mvp_sequence_check.py', 'scripts/pas169_launch_readiness_check.py', 'scripts/pas_launch_integrity_check.py', 'scripts/pas170_operator_survival_readiness_check.py', 'scripts/pas171_external_pilot_readiness_check.py', 'scripts/pas172_pilot_operations_readiness_check.py', 'scripts/pas173_brokerage_operator_readiness_check.py', 'scripts/pas174_operator_audit_readiness_check.py', 'scripts/pas175_audit_integrity_readiness_check.py', 'scripts/pas176_audit_chain_readiness_check.py', 'scripts/pas177_tenant_audit_verification_readiness_check.py', 'scripts/pas178_audit_window_chain_readiness_check.py', 'scripts/pas179_controlled_learning_readiness_check.py', 'scripts/pas180_learning_review_readiness_check.py', 'scripts/pas181_manual_test_harness_readiness_check.py', 'scripts/pas_security_01_hardening_readiness_check.py'))
               STORE_NAME              30 (PRIOR_PHASE_FILES)

 120           LOAD_CONST              84 (('app/services/memory/review.py', 'app/services/memory/review_stats.py', 'app/services/memory/review_export.py', 'app/services/memory/review_actors.py', 'app/services/memory/review_alerts.py', 'app/services/memory/operator_console.py'))
               STORE_NAME              31 (MEMORY_REVIEW_FILES)

 130           LOAD_CONST              85 (('def build_rate_limit_bucket_key(', 'def resolve_rate_limit_policy(', 'def check_rate_limit(', 'def record_rate_limit_hit(', 'def rate_limit_report(', 'def rate_limit_public_error(', 'ALLOWED_SURFACES', 'DEFAULT_POLICIES', 'email_ingestion', 'slack_command', 'api_key_rotation'))
               STORE_NAME              32 (REQUIRED_RATE_LIMIT_TOKENS)

 144           LOAD_CONST              86 (('def read_counter(', 'def increment_counter(', 'ALLOWED_STORE_BACKENDS', 'ALLOWED_COUNTER_METADATA_KEYS', 'rate_limit_store_process_local', '_TABLE = "pas_rate_limit_counters"'))
               STORE_NAME              33 (REQUIRED_STORE_TOKENS)

 153           LOAD_CONST              87 (('def detect_python_lockfile(', 'def detect_node_lockfile(', 'def scan_python_dependencies(', 'def scan_node_dependencies(', 'def scan_all(', 'scanner_unavailable'))
               STORE_NAME              34 (REQUIRED_SCANNER_TOKENS)

 162           LOAD_CONST              88 (('def request_api_key_rotation(', 'def approve_api_key_rotation(', 'def cancel_api_key_rotation(', 'def fail_api_key_rotation(', 'def rotate_api_key_if_helper_available(', 'def api_key_rotation_status(', 'def list_api_key_rotation_events(', 'def fingerprint_api_key(', 'ALLOWED_ROTATION_STATUSES', 'ALLOWED_TRANSITIONS', '_TABLE = "pas_api_key_rotation_events"'))
               STORE_NAME              35 (REQUIRED_ROTATION_SERVICE_TOKENS)

 176           LOAD_CONST              89 (('tenant_router', 'operator_router', '@tenant_router.post("/rotation-request")', '@tenant_router.get("/rotation-status")', '@operator_router.post("/{rotation_id}/approve")', '@operator_router.post("/{rotation_id}/cancel")', '@operator_router.post("/{rotation_id}/fail")', 'require_brokerage', 'require_admin'))
               STORE_NAME              36 (REQUIRED_ROTATION_ROUTE_TOKENS)

 188           LOAD_CONST              90 (('scan_python_dependencies', 'scan_node_dependencies', '--python-only', '--node-only', '--json'))
               STORE_NAME              37 (REQUIRED_AUDIT_CLI_TOKENS)

 197           LOAD_CONST              91 (('security.cors.audit_completed', 'security.rate_limit.allowed', 'security.rate_limit.blocked', 'security.dependency_audit.completed', 'security.dependency_audit.warning', 'security.api_key_rotation.requested', 'security.api_key_rotation.approved', 'security.api_key_rotation.completed', 'security.api_key_rotation.failed'))
               STORE_NAME              38 (REQUIRED_EVENT_TYPES)

 214           LOAD_CONST              92 (('raw_api_key', 'raw_ip', 'user_agent_raw'))
               STORE_NAME              39 (FORBIDDEN_RAW_KEY_TOKENS)

 223           LOAD_CONST              93 (('pip install', 'pip-audit fix', 'npm audit fix', 'npm install', 'poetry update', 'yarn upgrade'))
               STORE_NAME              40 (FORBIDDEN_AUTO_FIX_TOKENS)

 233           LOAD_CONST              94 (('import gmail', 'from gmail', 'import googleapiclient', 'from googleapiclient', 'import google.oauth2', 'from google.oauth2', 'from google.auth', 'import google.auth', 'from google_auth_oauthlib', 'import imaplib', 'from imaplib', 'import poplib', 'from poplib', 'import composio', 'from composio', 'import trustclaw', 'from trustclaw', 'import chromadb', 'from chromadb', 'import pinecone', 'from pinecone', 'import langchain', 'from langchain', 'import faiss', 'import pgvector', 'from pgvector', 'from openai import embeddings', 'from openai.embeddings', 'from anthropic', 'import anthropic', 'from openai', 'import openai'))
               STORE_NAME              41 (FORBIDDEN_IMPORT_LINE_PREFIXES)

 257           LOAD_CONST              95 (('imaplib', 'poplib', 'fetch_inbox', 'gmail_oauth', 'gmail_token', 'users().messages'))
               STORE_NAME              42 (FORBIDDEN_INBOX_TOKENS)

 271           LOAD_CONST              13 ('severity')

 273           LOAD_NAME               27 (SEVERITY_BLOCK)

 271           LOAD_CONST              14 ('detail')

 273           LOAD_CONST              15 ('')

 271           BUILD_MAP                2
               LOAD_CONST              16 (<code object __annotate__ at 0x0000018C18025030, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 271>)
               MAKE_FUNCTION
               LOAD_CONST              17 (<code object _check at 0x0000018C17FA31E0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 271>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              43 (_check)

 284           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA2A60, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 284>)
               MAKE_FUNCTION
               LOAD_CONST              19 (<code object _now_iso at 0x0000018C18038F30, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 284>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              44 (_now_iso)

 288           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA2970, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 288>)
               MAKE_FUNCTION
               LOAD_CONST              21 (<code object _read_text at 0x0000018C180533F0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 288>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              45 (_read_text)

 295           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA23D0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 295>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object _strip_python_comments_and_strings at 0x0000018C17D521D0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 295>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              46 (_strip_python_comments_and_strings)

 334           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA3B40, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 334>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object check_files_present at 0x0000018C180612C0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 334>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              47 (check_files_present)

 347           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA2F10, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 347>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object check_prior_phases_intact at 0x0000018C18060F60, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 347>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              48 (check_prior_phases_intact)

 360           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA33C0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 360>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object check_memory_review_intact at 0x0000018C180606F0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 360>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              49 (check_memory_review_intact)

 373           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA35A0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 373>)
               MAKE_FUNCTION
               LOAD_CONST              31 (<code object check_worker_off_by_default at 0x0000018C179C3E10, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 373>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              50 (check_worker_off_by_default)

 390           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA3D20, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 390>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object check_v31_sql at 0x0000018C181A24E0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 390>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              51 (check_v31_sql)

 441           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA1D40, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 441>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object check_v32_sql at 0x0000018C17D7E060, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 441>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              52 (check_v32_sql)

 506           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C17FA2880, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 506>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object check_rate_limit_service at 0x0000018C17FEDE30, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 506>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              53 (check_rate_limit_service)

 521           LOAD_CONST              38 (<code object __annotate__ at 0x0000018C17FA2100, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 521>)
               MAKE_FUNCTION
               LOAD_CONST              39 (<code object check_rate_limit_store at 0x0000018C17FED630, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 521>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              54 (check_rate_limit_store)

 536           LOAD_CONST              40 (<code object __annotate__ at 0x0000018C17FA2B50, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 536>)
               MAKE_FUNCTION
               LOAD_CONST              41 (<code object check_dependency_scanner at 0x0000018C17EDA430, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 536>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              55 (check_dependency_scanner)

 563           LOAD_CONST              42 (<code object __annotate__ at 0x0000018C17FA32D0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 563>)
               MAKE_FUNCTION
               LOAD_CONST              43 (<code object check_rotation_service at 0x0000018C17FEDC30, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 563>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              56 (check_rotation_service)

 578           LOAD_CONST              44 (<code object __annotate__ at 0x0000018C17FA3780, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 578>)
               MAKE_FUNCTION
               LOAD_CONST              45 (<code object check_rotation_routes at 0x0000018C17E7EB40, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 578>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              57 (check_rotation_routes)

 605           LOAD_CONST              46 (<code object __annotate__ at 0x0000018C17FA1E30, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 605>)
               MAKE_FUNCTION
               LOAD_CONST              47 (<code object check_audit_cli at 0x0000018C17F76C60, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 605>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              58 (check_audit_cli)

 632           LOAD_CONST              48 (<code object __annotate__ at 0x0000018C17FA2E20, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 632>)
               MAKE_FUNCTION
               LOAD_CONST              49 (<code object check_email_ingestion_rate_limit_wired at 0x0000018C180488F0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 632>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              59 (check_email_ingestion_rate_limit_wired)

 648           LOAD_CONST              50 (<code object __annotate__ at 0x0000018C17FA21F0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 648>)
               MAKE_FUNCTION
               LOAD_CONST              51 (<code object check_slack_command_rate_limit_wired at 0x0000018C18048AB0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 648>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              60 (check_slack_command_rate_limit_wired)

 664           LOAD_CONST              52 (<code object __annotate__ at 0x0000018C17FA26A0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 664>)
               MAKE_FUNCTION
               LOAD_CONST              53 (<code object check_audit_service_invariant at 0x0000018C182DBDA0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 664>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              61 (check_audit_service_invariant)

 689           LOAD_CONST              54 (<code object __annotate__ at 0x0000018C17FA2790, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 689>)
               MAKE_FUNCTION
               LOAD_CONST              55 (<code object check_event_contract at 0x0000018C179A7290, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 689>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              62 (check_event_contract)

 704           LOAD_CONST              56 (<code object __annotate__ at 0x0000018C17FA22E0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 704>)
               MAKE_FUNCTION
               LOAD_CONST              57 (<code object check_main_router_mounts at 0x0000018C18128030, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 704>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              63 (check_main_router_mounts)

 725           LOAD_CONST              58 (<code object __annotate__ at 0x0000018C17FA24C0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 725>)
               MAKE_FUNCTION
               LOAD_CONST              59 (<code object check_no_forbidden_imports at 0x0000018C17EA46C0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 725>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              64 (check_no_forbidden_imports)

 759           LOAD_CONST              60 (<code object __annotate__ at 0x0000018C17FA25B0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 759>)
               MAKE_FUNCTION
               LOAD_CONST              61 (<code object check_no_inbox_scan_tokens at 0x0000018C17CC2E60, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 759>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              65 (check_no_inbox_scan_tokens)

 788           LOAD_CONST              62 (<code object __annotate__ at 0x0000018C17FA2C40, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 788>)
               MAKE_FUNCTION
               LOAD_CONST              63 (<code object check_doc_required_clauses at 0x0000018C17CD1490, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 788>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              66 (check_doc_required_clauses)

 834           LOAD_CONST              64 (<code object __annotate__ at 0x0000018C17FA3A50, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 834>)
               MAKE_FUNCTION
               LOAD_CONST              65 (<code object check_self_no_env_or_db at 0x0000018C17D88C40, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 834>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              67 (check_self_no_env_or_db)

 867           LOAD_CONST              66 (<code object __annotate__ at 0x0000018C181153E0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 867>)
               MAKE_FUNCTION
               LOAD_CONST              67 (<code object _aggregate at 0x0000018C17FA92F0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 867>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              68 (_aggregate)

 879           LOAD_CONST              68 (<code object __annotate__ at 0x0000018C181154D0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 879>)
               MAKE_FUNCTION
               LOAD_CONST              69 (<code object _operator_actions at 0x0000018C18048C70, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 879>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              69 (_operator_actions)

 889           LOAD_CONST              70 (<code object __annotate__ at 0x0000018C181155C0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 889>)
               MAKE_FUNCTION
               LOAD_CONST              71 (<code object evaluate at 0x0000018C177C5D50, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 889>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              70 (evaluate)

 929           LOAD_CONST              72 ('pas_security_02_rate_limit_scanner_readiness_report.json')
               STORE_NAME              71 (REPORT_FILENAME)

 932           LOAD_CONST              73 (<code object __annotate__ at 0x0000018C18115980, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 932>)
               MAKE_FUNCTION
               LOAD_CONST              74 (<code object _build_parser at 0x0000018C181287B0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 932>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              72 (_build_parser)

 950           LOAD_CONST              75 (<code object __annotate__ at 0x0000018C18115A70, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 950>)
               MAKE_FUNCTION
               LOAD_CONST              76 (<code object _print_summary at 0x0000018C17D8C5C0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 950>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              73 (_print_summary)

 968           LOAD_CONST              77 (<code object __annotate__ at 0x0000018C18025A30, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 968>)
               MAKE_FUNCTION
               LOAD_CONST              78 (<code object _write_report at 0x0000018C18128990, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 968>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              74 (_write_report)

 982           LOAD_CONST              96 ((None,))
               LOAD_CONST              79 (<code object __annotate__ at 0x0000018C18115110, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 982>)
               MAKE_FUNCTION
               LOAD_CONST              80 (<code object main at 0x0000018C17D88FF0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 982>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              75 (main)

1007           LOAD_NAME               76 (__name__)
               LOAD_CONST              81 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

1008           LOAD_NAME                6 (sys)
               LOAD_ATTR              154 (exit)
               PUSH_NULL
               LOAD_NAME               75 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

1007   L5:     LOAD_CONST               2 (None)
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

Disassembly of <code object __annotate__ at 0x0000018C18025030, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 271>:
271           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('check_id')

272           LOAD_CONST               2 ('str')

271           LOAD_CONST               3 ('status')

272           LOAD_CONST               2 ('str')

271           LOAD_CONST               4 ('label')

272           LOAD_CONST               2 ('str')

271           LOAD_CONST               5 ('severity')

273           LOAD_CONST               2 ('str')

271           LOAD_CONST               6 ('detail')

273           LOAD_CONST               2 ('str')

271           LOAD_CONST               7 ('return')

274           LOAD_CONST               8 ('dict')

271           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _check at 0x0000018C17FA31E0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 271>:
271           RESUME                   0

276           LOAD_CONST               0 ('id')
              LOAD_FAST_BORROW         0 (check_id)

277           LOAD_CONST               1 ('status')
              LOAD_FAST_BORROW         1 (status)

278           LOAD_CONST               2 ('label')
              LOAD_FAST_BORROW         2 (label)

279           LOAD_CONST               3 ('severity')
              LOAD_FAST_BORROW         3 (severity)

280           LOAD_CONST               4 ('detail')
              LOAD_FAST_BORROW         4 (detail)

275           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 284>:
284           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038F30, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 284>:
284           RESUME                   0

285           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 288>:
288           RESUME                   0
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

Disassembly of <code object _read_text at 0x0000018C180533F0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 288>:
 288           RESUME                   0

 289           NOP

 290   L1:     LOAD_FAST_BORROW         0 (path)
               LOAD_ATTR                1 (read_text + NULL|self)
               LOAD_CONST               0 ('utf-8')
               LOAD_CONST               1 ('replace')
               LOAD_CONST               2 (('encoding', 'errors'))
               CALL_KW                  2
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 291           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 292   L4:     POP_EXCEPT
               LOAD_CONST               3 (None)
               RETURN_VALUE

 291   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 295>:
295           RESUME                   0
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

Disassembly of <code object _strip_python_comments_and_strings at 0x0000018C17D521D0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 295>:
295            RESUME                   0

296            BUILD_LIST               0
               STORE_FAST               1 (out)

297            LOAD_SMALL_INT           0
               LOAD_GLOBAL              1 (len + NULL)
               LOAD_FAST_BORROW         0 (src)
               CALL                     1
               STORE_FAST_STORE_FAST   50 (n, i)

298    L1:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (i, n)
               COMPARE_OP              18 (bool(<))
               EXTENDED_ARG             1
               POP_JUMP_IF_FALSE      282 (to L13)
               NOT_TAKEN

299            LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               BINARY_OP               26 ([])
               STORE_FAST               4 (ch)

300            LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               1 ('#')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       38 (to L3)
               NOT_TAKEN

301            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_CONST               2 ('\n')
               LOAD_FAST_BORROW         2 (i)
               CALL                     2
               STORE_FAST               5 (j)

302            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L2)
               NOT_TAKEN

303            JUMP_FORWARD           240 (to L13)

304    L2:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

305            JUMP_BACKWARD           59 (to L1)

306    L3:     LOAD_FAST_BORROW         0 (src)
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

307    L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               BINARY_SLICE
               STORE_FAST               6 (quote)

308            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 98 (quote, i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               CALL                     2
               STORE_FAST               7 (end)

309            LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L5)
               NOT_TAKEN

310            JUMP_FORWARD           138 (to L13)

311    L5:     LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

312            JUMP_BACKWARD          161 (to L1)

313    L6:     LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               7 (('"', "'"))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       92 (to L12)
               NOT_TAKEN

314            LOAD_FAST                4 (ch)
               STORE_FAST               6 (quote)

315            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               5 (j)

316    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (j, n)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       63 (to L11)
               NOT_TAKEN

317            LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
               BINARY_OP               26 ([])
               LOAD_CONST               5 ('\\')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       12 (to L8)
               NOT_TAKEN

318            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           2
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)

319            JUMP_BACKWARD           30 (to L7)

320    L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
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

321    L9:     JUMP_FORWARD            11 (to L11)

322   L10:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)
               JUMP_BACKWARD           68 (to L7)

323   L11:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

324            EXTENDED_ARG             1
               JUMP_BACKWARD          259 (to L1)

325   L12:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (ch)
               CALL                     1
               POP_TOP

326            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               2 (i)
               EXTENDED_ARG             1
               JUMP_BACKWARD          288 (to L1)

327   L13:     LOAD_CONST               6 ('')
               LOAD_ATTR                9 (join + NULL|self)
               LOAD_FAST_BORROW         1 (out)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 334>:
334           RESUME                   0
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

Disassembly of <code object check_files_present at 0x0000018C180612C0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 334>:
334           RESUME                   0

335           BUILD_LIST               0
              STORE_FAST               1 (out)

336           LOAD_GLOBAL              0 (REQUIRED_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

337           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

338           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

339           LOAD_CONST               0 ('file:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

340           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

341   L3:     LOAD_CONST               3 ('Required PAS-SECURITY-02 file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

342           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing')

338   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

336   L6:     END_FOR
              POP_ITER

344           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 347>:
347           RESUME                   0
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

Disassembly of <code object check_prior_phases_intact at 0x0000018C18060F60, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 347>:
347           RESUME                   0

348           BUILD_LIST               0
              STORE_FAST               1 (out)

349           LOAD_GLOBAL              0 (PRIOR_PHASE_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

350           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

351           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

352           LOAD_CONST               0 ('prior_phase:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

353           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

354   L3:     LOAD_CONST               3 ('Prior-phase readiness script intact: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

355           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing — PAS-SECURITY-02 must not delete')

351   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

349   L6:     END_FOR
              POP_ITER

357           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 360>:
360           RESUME                   0
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

Disassembly of <code object check_memory_review_intact at 0x0000018C180606F0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 360>:
360           RESUME                   0

361           BUILD_LIST               0
              STORE_FAST               1 (out)

362           LOAD_GLOBAL              0 (MEMORY_REVIEW_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

363           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

364           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

365           LOAD_CONST               0 ('memory_review:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

366           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

367   L3:     LOAD_CONST               3 ('Memory Review file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

368           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('Memory Review file deleted — PAS-SECURITY-02 must not touch')

364   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

362   L6:     END_FOR
              POP_ITER

370           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 373>:
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

Disassembly of <code object check_worker_off_by_default at 0x0000018C179C3E10, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 373>:
373           RESUME                   0

374           BUILD_LIST               0
              STORE_FAST               1 (out)

375           LOAD_GLOBAL              1 (Path + NULL)
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

376           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

378           LOAD_CONST               5 ('_ENV_FLAG_ENABLED_LITERAL = "true"')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         6 (to L2)
              NOT_TAKEN
              POP_TOP

379           LOAD_CONST               6 ("_ENV_FLAG_ENABLED_LITERAL = 'true'")
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)

377   L2:     STORE_FAST               4 (literal_ok)

381           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

382           LOAD_CONST               7 ('worker:off_by_default')

383           LOAD_FAST_BORROW         4 (literal_ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               8 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               9 ('FAIL')

384   L4:     LOAD_CONST              10 ('Pending-call worker is OFF by default')

385           LOAD_FAST_BORROW         4 (literal_ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST              11 ('missing strict enable-literal constant')

381   L6:     LOAD_CONST              12 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

387           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3D20, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 390>:
390           RESUME                   0
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

Disassembly of <code object check_v31_sql at 0x0000018C181A24E0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 390>:
  --            MAKE_CELL                7 (src)

 390            RESUME                   0

 391            BUILD_LIST               0
                STORE_FAST               1 (out)

 392            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('scripts')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('migrate_v31_rate_limit_counters.sql')
                BINARY_OP               11 (/)
                STORE_FAST               2 (p)

 393            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (p)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L1:     STORE_DEREF              7 (src)

 394            LOAD_DEREF               7 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_FAST               3 (lower)

 395            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 396            LOAD_CONST               3 ('v31_sql:proposal_only')

 397            LOAD_CONST               4 ('proposal only')
                LOAD_FAST_BORROW         3 (lower)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L2)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               6 ('FAIL')

 398    L3:     LOAD_CONST               7 ("v31 SQL carries 'PROPOSAL ONLY' guardrail")

 399            LOAD_CONST               4 ('proposal only')
                LOAD_FAST_BORROW         3 (lower)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L4)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L5)
        L4:     LOAD_CONST               8 ('missing label')

 395    L5:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 401            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 402            LOAD_CONST              10 ('v31_sql:do_not_execute')

 403            LOAD_CONST              11 ('do not execute')
                LOAD_FAST_BORROW         3 (lower)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L7)
        L6:     LOAD_CONST               6 ('FAIL')

 404    L7:     LOAD_CONST              12 ("v31 SQL carries 'DO NOT EXECUTE' trailer")

 405            LOAD_CONST              11 ('do not execute')
                LOAD_FAST_BORROW         3 (lower)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST              13 ('missing trailer')

 401    L9:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 407            LOAD_CONST              14 ('CREATE TABLE IF NOT EXISTS pas_rate_limit_counters')
                LOAD_DEREF               7 (src)
                CONTAINS_OP              0 (in)
                STORE_FAST               4 (table_ok)

 408            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 409            LOAD_CONST              15 ('v31_sql:table_present')

 410            LOAD_FAST_BORROW         4 (table_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L11)
       L10:     LOAD_CONST               6 ('FAIL')

 411   L11:     LOAD_CONST              16 ('v31 SQL creates pas_rate_limit_counters')

 408            CALL                     3
                CALL                     1
                POP_TOP

 413            LOAD_GLOBAL             10 (all)
                COPY                     1
                LOAD_COMMON_CONSTANT     3 (<built-in function all>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L15)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         7 (src)
                BUILD_TUPLE              1
                LOAD_CONST              17 (<code object <genexpr> at 0x0000018C18025830, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 413>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 414            LOAD_CONST              29 (("'email_ingestion'", "'slack_command'", "'admin'", "'tenant_api'", "'api_key_rotation'", "'webhook_generic'", "'webhook_followupboss'", "'webhook_gohighlevel'", "'webhook_zapier'"))
                GET_ITER

 413            CALL                     0
       L12:     FOR_ITER                12 (to L14)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L13)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L12)
       L13:     POP_ITER
                LOAD_CONST              18 (False)
                JUMP_FORWARD            20 (to L16)
       L14:     END_FOR
                POP_ITER
                LOAD_CONST              19 (True)
                JUMP_FORWARD            16 (to L16)
       L15:     PUSH_NULL
                LOAD_FAST_BORROW         7 (src)
                BUILD_TUPLE              1
                LOAD_CONST              17 (<code object <genexpr> at 0x0000018C18025830, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 413>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 414            LOAD_CONST              29 (("'email_ingestion'", "'slack_command'", "'admin'", "'tenant_api'", "'api_key_rotation'", "'webhook_generic'", "'webhook_followupboss'", "'webhook_gohighlevel'", "'webhook_zapier'"))
                GET_ITER

 413            CALL                     0
                CALL                     1
       L16:     STORE_FAST               5 (surfaces_ok)

 421            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 422            LOAD_CONST              20 ('v31_sql:closed_surface_enum')

 423            LOAD_FAST_BORROW         5 (surfaces_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L17)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L18)
       L17:     LOAD_CONST               6 ('FAIL')

 424   L18:     LOAD_CONST              21 ('v31 SQL carries the closed surface enum')

 421            CALL                     3
                CALL                     1
                POP_TOP

 427            LOAD_CONST              22 ('pas_rate_limit_counters_tenant_no_select')
                LOAD_DEREF               7 (src)
                CONTAINS_OP              0 (in)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       45 (to L19)
                NOT_TAKEN
                POP_TOP

 428            LOAD_CONST              23 ('pas_rate_limit_counters_tenant_no_insert')
                LOAD_DEREF               7 (src)
                CONTAINS_OP              0 (in)

 427            COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       32 (to L19)
                NOT_TAKEN
                POP_TOP

 429            LOAD_CONST              24 ('pas_rate_limit_counters_tenant_no_update')
                LOAD_DEREF               7 (src)
                CONTAINS_OP              0 (in)

 427            COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L19)
                NOT_TAKEN
                POP_TOP

 430            LOAD_CONST              25 ('pas_rate_limit_counters_tenant_no_delete')
                LOAD_DEREF               7 (src)
                CONTAINS_OP              0 (in)

 427            COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        6 (to L19)
                NOT_TAKEN
                POP_TOP

 431            LOAD_CONST              26 ('pas_rate_limit_counters_service_role_aged_delete')
                LOAD_DEREF               7 (src)
                CONTAINS_OP              0 (in)

 426   L19:     STORE_FAST               6 (policies_ok)

 433            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 434            LOAD_CONST              27 ('v31_sql:tenant_denied_service_role_aged_delete')

 435            LOAD_FAST_BORROW         6 (policies_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L20)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L21)
       L20:     LOAD_CONST               6 ('FAIL')

 436   L21:     LOAD_CONST              28 ('v31 SQL denies tenant all ops + service_role aged-DELETE policy')

 433            CALL                     3
                CALL                     1
                POP_TOP

 438            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18025830, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 413>:
  --           COPY_FREE_VARS           1

 413           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 414   L2:     FOR_ITER                 9 (to L3)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA1D40, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 441>:
441           RESUME                   0
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

Disassembly of <code object check_v32_sql at 0x0000018C17D7E060, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 441>:
  --            MAKE_CELL                9 (src)

 441            RESUME                   0

 442            BUILD_LIST               0
                STORE_FAST               1 (out)

 443            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('scripts')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('migrate_v32_api_key_rotation_events.sql')
                BINARY_OP               11 (/)
                STORE_FAST               2 (p)

 444            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (p)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L1:     STORE_DEREF              9 (src)

 445            LOAD_DEREF               9 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_FAST               3 (lower)

 446            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 447            LOAD_CONST               3 ('v32_sql:proposal_only')

 448            LOAD_CONST               4 ('proposal only')
                LOAD_FAST_BORROW         3 (lower)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L2)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               6 ('FAIL')

 449    L3:     LOAD_CONST               7 ("v32 SQL carries 'PROPOSAL ONLY' guardrail")

 446            CALL                     3
                CALL                     1
                POP_TOP

 451            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 452            LOAD_CONST               8 ('v32_sql:do_not_execute')

 453            LOAD_CONST               9 ('do not execute')
                LOAD_FAST_BORROW         3 (lower)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L4)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L5)
        L4:     LOAD_CONST               6 ('FAIL')

 454    L5:     LOAD_CONST              10 ("v32 SQL carries 'DO NOT EXECUTE' trailer")

 451            CALL                     3
                CALL                     1
                POP_TOP

 456            LOAD_CONST              11 ('CREATE TABLE IF NOT EXISTS pas_api_key_rotation_events')
                LOAD_DEREF               9 (src)
                CONTAINS_OP              0 (in)
                STORE_FAST               4 (table_ok)

 457            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 458            LOAD_CONST              12 ('v32_sql:table_present')

 459            LOAD_FAST_BORROW         4 (table_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L7)
        L6:     LOAD_CONST               6 ('FAIL')

 460    L7:     LOAD_CONST              13 ('v32 SQL creates pas_api_key_rotation_events')

 457            CALL                     3
                CALL                     1
                POP_TOP

 462            LOAD_GLOBAL             10 (all)
                COPY                     1
                LOAD_COMMON_CONSTANT     3 (<built-in function all>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L11)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         9 (src)
                BUILD_TUPLE              1
                LOAD_CONST              14 (<code object <genexpr> at 0x0000018C18025230, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 462>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 463            LOAD_CONST              37 (("'REQUESTED'", "'APPROVED'", "'ROTATED'", "'FAILED'", "'CANCELLED'"))
                GET_ITER

 462            CALL                     0
        L8:     FOR_ITER                12 (to L10)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L9)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L8)
        L9:     POP_ITER
                LOAD_CONST              15 (False)
                JUMP_FORWARD            20 (to L12)
       L10:     END_FOR
                POP_ITER
                LOAD_CONST              16 (True)
                JUMP_FORWARD            16 (to L12)
       L11:     PUSH_NULL
                LOAD_FAST_BORROW         9 (src)
                BUILD_TUPLE              1
                LOAD_CONST              14 (<code object <genexpr> at 0x0000018C18025230, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 462>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 463            LOAD_CONST              37 (("'REQUESTED'", "'APPROVED'", "'ROTATED'", "'FAILED'", "'CANCELLED'"))
                GET_ITER

 462            CALL                     0
                CALL                     1
       L12:     STORE_FAST               5 (status_ok)

 468            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 469            LOAD_CONST              17 ('v32_sql:closed_status_enum')

 470            LOAD_FAST_BORROW         5 (status_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L13)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L14)
       L13:     LOAD_CONST               6 ('FAIL')

 471   L14:     LOAD_CONST              18 ('v32 SQL carries the closed status enum')

 468            CALL                     3
                CALL                     1
                POP_TOP

 474            LOAD_CONST              19 ('raw_api_key')
                LOAD_DEREF               9 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                CONTAINS_OP              0 (in)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        20 (to L15)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              20 (' api_key ')
                LOAD_DEREF               9 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                CONTAINS_OP              0 (in)
       L15:     STORE_FAST               6 (raw_key_present)

 475            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 476            LOAD_CONST              21 ('v32_sql:no_raw_api_key_column')

 477            LOAD_FAST_BORROW         6 (raw_key_present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L16)
                NOT_TAKEN
                LOAD_CONST               6 ('FAIL')
                JUMP_FORWARD             1 (to L17)
       L16:     LOAD_CONST               5 ('PASS')

 478   L17:     LOAD_CONST              22 ('v32 SQL does NOT define a raw API-key column')

 479            LOAD_FAST_BORROW         6 (raw_key_present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L18)
                NOT_TAKEN
                LOAD_CONST              23 ('raw api_key column detected')
                JUMP_FORWARD             1 (to L19)
       L18:     LOAD_CONST               2 ('')

 475   L19:     LOAD_CONST              24 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 482            LOAD_CONST              25 ("'^[0-9a-f]{64}$'")
                LOAD_DEREF               9 (src)
                CONTAINS_OP              0 (in)
                STORE_FAST               7 (fp_ok)

 483            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 484            LOAD_CONST              26 ('v32_sql:fingerprint_check_constraint')

 485            LOAD_FAST_BORROW         7 (fp_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L20)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L21)
       L20:     LOAD_CONST               6 ('FAIL')

 486   L21:     LOAD_CONST              27 ('v32 SQL pins fingerprint columns to sha256 hex')

 483            CALL                     3
                CALL                     1
                POP_TOP

 490            LOAD_CONST              28 ('pas_api_key_rotation_events_tenant_select')
                LOAD_DEREF               9 (src)
                CONTAINS_OP              0 (in)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       71 (to L22)
                NOT_TAKEN
                POP_TOP

 491            LOAD_CONST              29 ('pas_api_key_rotation_events_tenant_insert')
                LOAD_DEREF               9 (src)
                CONTAINS_OP              0 (in)

 490            COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       58 (to L22)
                NOT_TAKEN
                POP_TOP

 492            LOAD_CONST              30 ('pas_api_key_rotation_events_tenant_no_update')
                LOAD_DEREF               9 (src)
                CONTAINS_OP              0 (in)

 490            COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       45 (to L22)
                NOT_TAKEN
                POP_TOP

 493            LOAD_CONST              31 ('pas_api_key_rotation_events_tenant_no_delete')
                LOAD_DEREF               9 (src)
                CONTAINS_OP              0 (in)

 490            COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       32 (to L22)
                NOT_TAKEN
                POP_TOP

 494            LOAD_CONST              32 ('pas_api_key_rotation_events_service_role_review_update')
                LOAD_DEREF               9 (src)
                CONTAINS_OP              0 (in)

 490            COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L22)
                NOT_TAKEN
                POP_TOP

 495            LOAD_CONST              33 ('pas_api_key_rotation_events_service_role_no_delete')
                LOAD_DEREF               9 (src)
                CONTAINS_OP              0 (in)

 490            COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        6 (to L22)
                NOT_TAKEN
                POP_TOP

 496            LOAD_CONST              34 ('WITH CHECK')
                LOAD_DEREF               9 (src)
                CONTAINS_OP              0 (in)

 489   L22:     STORE_FAST               8 (policies_ok)

 498            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 499            LOAD_CONST              35 ('v32_sql:append_only_with_review_update')

 500            LOAD_FAST_BORROW         8 (policies_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L23)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L24)
       L23:     LOAD_CONST               6 ('FAIL')

 501   L24:     LOAD_CONST              36 ('v32 SQL denies tenant UPDATE/DELETE; service_role restricted UPDATE; no DELETE')

 498            CALL                     3
                CALL                     1
                POP_TOP

 503            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18025230, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 462>:
  --           COPY_FREE_VARS           1

 462           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 463   L2:     FOR_ITER                 9 (to L3)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 506>:
506           RESUME                   0
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

Disassembly of <code object check_rate_limit_service at 0x0000018C17FEDE30, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 506>:
506           RESUME                   0

507           BUILD_LIST               0
              STORE_FAST               1 (out)

508           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('services')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('security')
              BINARY_OP               11 (/)
              LOAD_CONST               3 ('rate_limit.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

509           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

510           LOAD_GLOBAL              4 (REQUIRED_RATE_LIMIT_TOKENS)
              GET_ITER
      L2:     FOR_ITER                73 (to L7)
              STORE_FAST               4 (tok)

511           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

512           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

513           LOAD_CONST               5 ('rate_limit:')
              LOAD_FAST_BORROW         4 (tok)
              LOAD_CONST               6 (slice(None, 48, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

514           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               7 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               8 ('FAIL')

515   L4:     LOAD_CONST               9 ('rate_limit module exports ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

516           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             4 (to L6)
      L5:     LOAD_CONST              10 ('missing token ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

512   L6:     LOAD_CONST              11 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           75 (to L2)

510   L7:     END_FOR
              POP_ITER

518           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 521>:
521           RESUME                   0
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

Disassembly of <code object check_rate_limit_store at 0x0000018C17FED630, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 521>:
521           RESUME                   0

522           BUILD_LIST               0
              STORE_FAST               1 (out)

523           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('services')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('security')
              BINARY_OP               11 (/)
              LOAD_CONST               3 ('rate_limit_store.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

524           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

525           LOAD_GLOBAL              4 (REQUIRED_STORE_TOKENS)
              GET_ITER
      L2:     FOR_ITER                73 (to L7)
              STORE_FAST               4 (tok)

526           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

527           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

528           LOAD_CONST               5 ('rate_limit_store:')
              LOAD_FAST_BORROW         4 (tok)
              LOAD_CONST               6 (slice(None, 48, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

529           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               7 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               8 ('FAIL')

530   L4:     LOAD_CONST               9 ('rate_limit_store module exports ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

531           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             4 (to L6)
      L5:     LOAD_CONST              10 ('missing token ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

527   L6:     LOAD_CONST              11 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           75 (to L2)

525   L7:     END_FOR
              POP_ITER

533           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 536>:
536           RESUME                   0
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

Disassembly of <code object check_dependency_scanner at 0x0000018C17EDA430, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 536>:
536            RESUME                   0

537            BUILD_LIST               0
               STORE_FAST               1 (out)

538            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('services')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('security')
               BINARY_OP               11 (/)
               LOAD_CONST               3 ('dependency_scanner.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

539            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')
       L1:     STORE_FAST               3 (src)

540            LOAD_GLOBAL              4 (REQUIRED_SCANNER_TOKENS)
               GET_ITER
       L2:     FOR_ITER                73 (to L7)
               STORE_FAST               4 (tok)

541            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

542            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

543            LOAD_CONST               5 ('scanner:')
               LOAD_FAST_BORROW         4 (tok)
               LOAD_CONST               6 (slice(None, 48, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

544            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               8 ('FAIL')

545    L4:     LOAD_CONST               9 ('dependency_scanner exports ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

546            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST              10 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

542    L6:     LOAD_CONST              11 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           75 (to L2)

540    L7:     END_FOR
               POP_ITER

549            LOAD_GLOBAL             11 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               6 (executable)

550            BUILD_LIST               0
               STORE_FAST               7 (bad)

551            LOAD_GLOBAL             12 (FORBIDDEN_AUTO_FIX_TOKENS)
               GET_ITER
       L8:     FOR_ITER                57 (to L10)
               STORE_FAST               4 (tok)

552            LOAD_FAST_BORROW         4 (tok)
               LOAD_ATTR               15 (lower + NULL|self)
               CALL                     0
               LOAD_FAST_BORROW         6 (executable)
               LOAD_ATTR               15 (lower + NULL|self)
               CALL                     0
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L9)
               NOT_TAKEN
               JUMP_BACKWARD           40 (to L8)

553    L9:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (tok)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           59 (to L8)

551   L10:     END_FOR
               POP_ITER

554            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

555            LOAD_CONST              12 ('scanner:no_auto_fix')

556            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               8 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               7 ('PASS')

557   L12:     LOAD_CONST              13 ('dependency_scanner does not call auto-fix / upgrade helpers')

558            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L13)
               NOT_TAKEN
               LOAD_CONST              14 ('disqualifying tokens: ')
               LOAD_CONST              15 (', ')
               LOAD_ATTR               17 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L14)
      L13:     LOAD_CONST               4 ('')

554   L14:     LOAD_CONST              11 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

560            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA32D0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 563>:
563           RESUME                   0
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

Disassembly of <code object check_rotation_service at 0x0000018C17FEDC30, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 563>:
563           RESUME                   0

564           BUILD_LIST               0
              STORE_FAST               1 (out)

565           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('services')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('security')
              BINARY_OP               11 (/)
              LOAD_CONST               3 ('api_key_rotation.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

566           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

567           LOAD_GLOBAL              4 (REQUIRED_ROTATION_SERVICE_TOKENS)
              GET_ITER
      L2:     FOR_ITER                73 (to L7)
              STORE_FAST               4 (tok)

568           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

569           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

570           LOAD_CONST               5 ('rotation:')
              LOAD_FAST_BORROW         4 (tok)
              LOAD_CONST               6 (slice(None, 48, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

571           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               7 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               8 ('FAIL')

572   L4:     LOAD_CONST               9 ('api_key_rotation module exports ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

573           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             4 (to L6)
      L5:     LOAD_CONST              10 ('missing token ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

569   L6:     LOAD_CONST              11 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           75 (to L2)

567   L7:     END_FOR
              POP_ITER

575           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 578>:
578           RESUME                   0
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

Disassembly of <code object check_rotation_routes at 0x0000018C17E7EB40, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 578>:
578            RESUME                   0

579            BUILD_LIST               0
               STORE_FAST               1 (out)

580            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('routes')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('security_api_key_rotation.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

581            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               3 ('')
       L1:     STORE_FAST               3 (src)

582            LOAD_GLOBAL              4 (REQUIRED_ROTATION_ROUTE_TOKENS)
               GET_ITER
       L2:     FOR_ITER                73 (to L7)
               STORE_FAST               4 (tok)

583            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

584            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

585            LOAD_CONST               4 ('rotation_routes:')
               LOAD_FAST_BORROW         4 (tok)
               LOAD_CONST               5 (slice(None, 48, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

586            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               6 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               7 ('FAIL')

587    L4:     LOAD_CONST               8 ('rotation routes file declares ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

588            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               3 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST               9 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

584    L6:     LOAD_CONST              10 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           75 (to L2)

582    L7:     END_FOR
               POP_ITER

591            LOAD_GLOBAL             11 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               6 (executable)

592            BUILD_LIST               0
               STORE_FAST               7 (bad)

593            LOAD_GLOBAL             12 (FORBIDDEN_RAW_KEY_TOKENS)
               GET_ITER
       L8:     FOR_ITER                28 (to L10)
               STORE_FAST               4 (tok)

594            LOAD_FAST_BORROW_LOAD_FAST_BORROW 70 (tok, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L9)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L8)

595    L9:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (tok)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L8)

593   L10:     END_FOR
               POP_ITER

596            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

597            LOAD_CONST              11 ('rotation_routes:no_raw_key_storage_or_echo')

598            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               7 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               6 ('PASS')

599   L12:     LOAD_CONST              12 ('rotation routes never reference raw_api_key / raw_ip / user_agent_raw')

600            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L13)
               NOT_TAKEN
               LOAD_CONST              13 ('disqualifying tokens: ')
               LOAD_CONST              14 (', ')
               LOAD_ATTR               15 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L14)
      L13:     LOAD_CONST               3 ('')

596   L14:     LOAD_CONST              10 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

602            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 605>:
605           RESUME                   0
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

Disassembly of <code object check_audit_cli at 0x0000018C17F76C60, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 605>:
605            RESUME                   0

606            BUILD_LIST               0
               STORE_FAST               1 (out)

607            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('scripts')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('security_dependency_audit.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

608            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               2 ('')
       L1:     STORE_FAST               3 (src)

609            LOAD_GLOBAL              4 (REQUIRED_AUDIT_CLI_TOKENS)
               GET_ITER
       L2:     FOR_ITER                73 (to L7)
               STORE_FAST               4 (tok)

610            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

611            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

612            LOAD_CONST               3 ('audit_cli:')
               LOAD_FAST_BORROW         4 (tok)
               LOAD_CONST               4 (slice(None, 48, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

613            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               6 ('FAIL')

614    L4:     LOAD_CONST               7 ('security_dependency_audit CLI exports ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

615            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST               8 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

611    L6:     LOAD_CONST               9 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           75 (to L2)

609    L7:     END_FOR
               POP_ITER

618            LOAD_GLOBAL             11 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               6 (executable)

619            BUILD_LIST               0
               STORE_FAST               7 (bad)

620            LOAD_GLOBAL             12 (FORBIDDEN_AUTO_FIX_TOKENS)
               GET_ITER
       L8:     FOR_ITER                57 (to L10)
               STORE_FAST               4 (tok)

621            LOAD_FAST_BORROW         4 (tok)
               LOAD_ATTR               15 (lower + NULL|self)
               CALL                     0
               LOAD_FAST_BORROW         6 (executable)
               LOAD_ATTR               15 (lower + NULL|self)
               CALL                     0
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L9)
               NOT_TAKEN
               JUMP_BACKWARD           40 (to L8)

622    L9:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (tok)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           59 (to L8)

620   L10:     END_FOR
               POP_ITER

623            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

624            LOAD_CONST              10 ('audit_cli:no_auto_fix')

625            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               6 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               5 ('PASS')

626   L12:     LOAD_CONST              11 ('security_dependency_audit CLI does not call auto-fix / upgrade')

627            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L13)
               NOT_TAKEN
               LOAD_CONST              12 ('disqualifying tokens: ')
               LOAD_CONST              13 (', ')
               LOAD_ATTR               17 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L14)
      L13:     LOAD_CONST               2 ('')

623   L14:     LOAD_CONST               9 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

629            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 632>:
632           RESUME                   0
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

Disassembly of <code object check_email_ingestion_rate_limit_wired at 0x0000018C180488F0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 632>:
632           RESUME                   0

633           BUILD_LIST               0
              STORE_FAST               1 (out)

634           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('routes')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('email_ingestion.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

635           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               3 ('')
      L1:     STORE_FAST               3 (src)

637           LOAD_CONST               4 ('check_rate_limit(')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE        6 (to L2)
              NOT_TAKEN
              POP_TOP

638           LOAD_CONST               5 ('surface="email_ingestion"')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)

636   L2:     STORE_FAST               4 (ok)

640           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

641           LOAD_CONST               6 ('rate_limit_wired:email_ingestion')

642           LOAD_FAST_BORROW         4 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               7 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               8 ('FAIL')

643   L4:     LOAD_CONST               9 ('email_ingestion route wires check_rate_limit(surface=email_ingestion)')

640           CALL                     3
              CALL                     1
              POP_TOP

645           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 648>:
648           RESUME                   0
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

Disassembly of <code object check_slack_command_rate_limit_wired at 0x0000018C18048AB0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 648>:
648           RESUME                   0

649           BUILD_LIST               0
              STORE_FAST               1 (out)

650           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('routes')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('slack_command.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

651           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               3 ('')
      L1:     STORE_FAST               3 (src)

653           LOAD_CONST               4 ('check_rate_limit(')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE        6 (to L2)
              NOT_TAKEN
              POP_TOP

654           LOAD_CONST               5 ('surface="slack_command"')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)

652   L2:     STORE_FAST               4 (ok)

656           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

657           LOAD_CONST               6 ('rate_limit_wired:slack_command')

658           LOAD_FAST_BORROW         4 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               7 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               8 ('FAIL')

659   L4:     LOAD_CONST               9 ('slack_command route wires check_rate_limit(surface=slack_command)')

656           CALL                     3
              CALL                     1
              POP_TOP

661           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA26A0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 664>:
664           RESUME                   0
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

Disassembly of <code object check_audit_service_invariant at 0x0000018C182DBDA0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 664>:
664           RESUME                   0

665           BUILD_LIST               0
              STORE_FAST               1 (out)

666           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('services')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('operator')
              BINARY_OP               11 (/)
              LOAD_CONST               3 ('audit_service.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

667           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

668           LOAD_CONST              12 (('def update_audit_', 'def delete_audit_', 'def update_operator_audit_', 'def delete_operator_audit_', 'def mutate_audit_', 'def truncate_audit_'))
              STORE_FAST               4 (forbidden)

676           BUILD_LIST               0
              STORE_FAST               5 (bad)

677           LOAD_FAST_BORROW         4 (forbidden)
              GET_ITER
      L2:     FOR_ITER                28 (to L4)
              STORE_FAST               6 (tok)

678           LOAD_FAST_BORROW_LOAD_FAST_BORROW 99 (tok, src)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

679   L3:     LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_FAST_BORROW         6 (tok)
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           30 (to L2)

677   L4:     END_FOR
              POP_ITER

680           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

681           LOAD_CONST               5 ('audit_service:append_only_carry')

682           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               6 ('FAIL')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               7 ('PASS')

683   L6:     LOAD_CONST               8 ('Audit service still has no UPDATE / DELETE mutation helpers (carry-forward invariant)')

684           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE       25 (to L7)
              NOT_TAKEN
              LOAD_CONST               9 ('disqualifying tokens: ')
              LOAD_CONST              10 (', ')
              LOAD_ATTR                9 (join + NULL|self)
              LOAD_FAST_BORROW         5 (bad)
              CALL                     1
              BINARY_OP                0 (+)
              JUMP_FORWARD             1 (to L8)
      L7:     LOAD_CONST               4 ('')

680   L8:     LOAD_CONST              11 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

686           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2790, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 689>:
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

Disassembly of <code object check_event_contract at 0x0000018C179A7290, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 689>:
689           RESUME                   0

690           BUILD_LIST               0
              STORE_FAST               1 (out)

691           LOAD_GLOBAL              1 (Path + NULL)
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

692           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

693           LOAD_GLOBAL              4 (REQUIRED_EVENT_TYPES)
              GET_ITER
      L2:     FOR_ITER                67 (to L7)
              STORE_FAST               4 (required)

694           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (required, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

695           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

696           LOAD_CONST               5 ('events:')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

697           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               6 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               7 ('FAIL')

698   L4:     LOAD_CONST               8 ('Event contract registers ')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

699           LOAD_FAST_BORROW         5 (ok)
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

695   L6:     LOAD_CONST              10 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           69 (to L2)

693   L7:     END_FOR
              POP_ITER

701           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA22E0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 704>:
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

Disassembly of <code object check_main_router_mounts at 0x0000018C18128030, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 704>:
704           RESUME                   0

705           BUILD_LIST               0
              STORE_FAST               1 (out)

706           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('main.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

707           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               2 ('')
      L1:     STORE_FAST               3 (src)

708           LOAD_CONST              10 (('tenant_api_key_router', 'operator_api_key_router', '/tenant/api-key', '/ops/api-key-rotation'))
              STORE_FAST               4 (required)

714           LOAD_FAST_BORROW         4 (required)
              GET_ITER
      L2:     FOR_ITER                74 (to L7)
              STORE_FAST               5 (tok)

715           LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               6 (ok)

716           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

717           LOAD_CONST               3 ('main:mount:')
              LOAD_FAST_BORROW         5 (tok)
              LOAD_CONST               4 (slice(None, 48, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

718           LOAD_FAST_BORROW         6 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               5 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               6 ('FAIL')

719   L4:     LOAD_CONST               7 ('app/main.py mounts ')
              LOAD_FAST_BORROW         5 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

720           LOAD_FAST_BORROW         6 (ok)
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

716   L6:     LOAD_CONST               9 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           76 (to L2)

714   L7:     END_FOR
              POP_ITER

722           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA24C0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 725>:
725           RESUME                   0
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

Disassembly of <code object check_no_forbidden_imports at 0x0000018C17EA46C0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 725>:
725            RESUME                   0

726            BUILD_LIST               0
               STORE_FAST               1 (out)

727            LOAD_CONST              10 (('app/services/security/rate_limit.py', 'app/services/security/rate_limit_store.py', 'app/services/security/dependency_scanner.py', 'app/services/security/api_key_rotation.py', 'app/routes/security_api_key_rotation.py', 'scripts/security_dependency_audit.py', 'scripts/pas_security_02_rate_limit_scanner_readiness_check.py'))
               STORE_FAST               2 (files)

736            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     EXTENDED_ARG             1
               FOR_ITER               292 (to L15)
               STORE_FAST               3 (relpath)

737            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

738            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

739            JUMP_BACKWARD           46 (to L1)

740    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

741            BUILD_LIST               0
               STORE_FAST               6 (bad)

742            LOAD_FAST_BORROW         5 (src)
               LOAD_ATTR                7 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L4:     FOR_ITER               107 (to L10)
               STORE_FAST               7 (line)

743            LOAD_FAST_BORROW         7 (line)
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               STORE_FAST               8 (stripped)

744            LOAD_FAST_BORROW         8 (stripped)
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

745    L5:     JUMP_BACKWARD           52 (to L4)

746    L6:     LOAD_GLOBAL             12 (FORBIDDEN_IMPORT_LINE_PREFIXES)
               GET_ITER
       L7:     FOR_ITER                45 (to L9)
               STORE_FAST               9 (prefix)

747            LOAD_FAST_BORROW         8 (stripped)
               LOAD_ATTR               11 (startswith + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD           28 (to L7)

748    L8:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           47 (to L7)

746    L9:     END_FOR
               POP_ITER
               JUMP_BACKWARD          109 (to L4)

742   L10:     END_FOR
               POP_ITER

749            LOAD_FAST                1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             17 (_check + NULL)

750            LOAD_CONST               3 ('forbidden_import:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

751            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               4 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               5 ('PASS')

752   L12:     LOAD_CONST               6 ('No forbidden imports: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

754            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       43 (to L13)
               NOT_TAKEN

753            LOAD_CONST               7 ('forbidden import prefixes: ')
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

754   L13:     LOAD_CONST               1 ('')

749   L14:     LOAD_CONST               9 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          295 (to L1)

736   L15:     END_FOR
               POP_ITER

756            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA25B0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 759>:
759           RESUME                   0
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

Disassembly of <code object check_no_inbox_scan_tokens at 0x0000018C17CC2E60, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 759>:
759            RESUME                   0

760            BUILD_LIST               0
               STORE_FAST               1 (out)

761            LOAD_CONST               9 (('app/services/security/rate_limit.py', 'app/services/security/rate_limit_store.py', 'app/services/security/dependency_scanner.py', 'app/services/security/api_key_rotation.py', 'app/routes/security_api_key_rotation.py'))
               STORE_FAST               2 (files)

768            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               195 (to L11)
               STORE_FAST               3 (relpath)

769            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

770            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

771            JUMP_BACKWARD           45 (to L1)

772    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

773            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         5 (src)
               CALL                     1
               STORE_FAST               6 (executable)

774            BUILD_LIST               0
               STORE_FAST               7 (bad)

775            LOAD_GLOBAL              8 (FORBIDDEN_INBOX_TOKENS)
               GET_ITER
       L4:     FOR_ITER                28 (to L6)
               STORE_FAST               8 (token)

776            LOAD_FAST_BORROW_LOAD_FAST_BORROW 134 (token, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L4)

777    L5:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_FAST_BORROW         8 (token)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L4)

775    L6:     END_FOR
               POP_ITER

778            LOAD_FAST                1 (out)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_GLOBAL             13 (_check + NULL)

779            LOAD_CONST               2 ('no_inbox_scan:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

780            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L7)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L8)
       L7:     LOAD_CONST               4 ('PASS')

781    L8:     LOAD_CONST               5 ('No inbox-scanning tokens: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

783            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L9)
               NOT_TAKEN

782            LOAD_CONST               6 ('inbox-scan tokens present: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               15 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L10)

783    L9:     LOAD_CONST               1 ('')

778   L10:     LOAD_CONST               8 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          197 (to L1)

768   L11:     END_FOR
               POP_ITER

785            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 788>:
788           RESUME                   0
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

Disassembly of <code object check_doc_required_clauses at 0x0000018C17CD1490, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 788>:
  --            MAKE_CELL                8 (lower)

 788            RESUME                   0

 789            BUILD_LIST               0
                STORE_FAST               1 (out)

 790            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('docs')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('pas_security_02_rate_limit_scanner_key_rotation.md')
                BINARY_OP               11 (/)
                STORE_FAST               2 (doc)

 791            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (doc)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L1:     STORE_FAST               3 (src)

 792            LOAD_FAST_BORROW         3 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_DEREF              8 (lower)

 793            LOAD_CONST              13 ((('purpose', ('purpose',)), ('pas-security-01', ('relationship to pas-security-01', 'relationship to the pas-security-01')), ('rate-limit-doctrine', ('rate-limit doctrine',)), ('process-shared', ('process-shared limiter doctrine', 'process-shared')), ('process-local-fallback', ('process-local fallback', 'process_local_fallback')), ('dependency-audit', ('dependency audit doctrine',)), ('no-auto-fix', ('no-auto-fix', 'no auto-fix')), ('api-key-rotation', ('api-key rotation doctrine', 'api key rotation doctrine')), ('no-raw-key-echo', ('no raw-key echo', 'no-raw-key-echo', 'no raw key echo')), ('tenant-initiated', ('tenant-initiated request model', 'tenant-initiated')), ('operator-approval', ('operator approval model', 'operator approval')), ('limitations', ('limitation',)), ('not-built', ('intentionally does not', 'intentionally not build', 'deliberately not')), ('no-gmail', ('no gmail',)), ('no-autonomous', ('no autonomous remediation', 'no autonomous'))))
                STORE_FAST               4 (required_phrases)

 822            LOAD_FAST_BORROW         4 (required_phrases)
                GET_ITER
        L2:     FOR_ITER               141 (to L12)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   86 (name, phrases)

 823            LOAD_GLOBAL              6 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         8 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18024B30, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 823>)
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
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18024B30, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 823>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         6 (phrases)
                GET_ITER
                CALL                     0
                CALL                     1
        L7:     STORE_FAST               7 (present)

 824            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 825            LOAD_CONST               6 ('docs:phrase:')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 826            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               8 ('FAIL')

 827    L9:     LOAD_CONST               9 ('Doctrine doc carries clause: ')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 829            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L10)
                NOT_TAKEN

 828            LOAD_CONST              10 ('expected one of: ')
                LOAD_CONST              11 (' | ')
                LOAD_ATTR               13 (join + NULL|self)
                LOAD_FAST_BORROW         6 (phrases)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L11)

 829   L10:     LOAD_CONST               2 ('')

 824   L11:     LOAD_CONST              12 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          143 (to L2)

 822   L12:     END_FOR
                POP_ITER

 831            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18024B30, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 823>:
  --           COPY_FREE_VARS           1

 823           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 834>:
834           RESUME                   0
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

Disassembly of <code object check_self_no_env_or_db at 0x0000018C17D88C40, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 834>:
834            RESUME                   0

835            BUILD_LIST               0
               STORE_FAST               1 (out)

836            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_GLOBAL              2 (__file__)
               CALL                     1
               LOAD_ATTR                5 (resolve + NULL|self)
               CALL                     0
               STORE_FAST               2 (self_path)

837            LOAD_GLOBAL              7 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (self_path)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L1:     STORE_FAST               3 (src)

838            LOAD_GLOBAL              9 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               4 (executable)

839            BUILD_LIST               0
               STORE_FAST               5 (bad)

840            LOAD_FAST_BORROW         4 (executable)
               LOAD_ATTR               11 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L2:     FOR_ITER               199 (to L9)
               STORE_FAST               6 (raw_line)

841            LOAD_FAST_BORROW         6 (raw_line)
               LOAD_ATTR               13 (strip + NULL|self)
               CALL                     0
               STORE_FAST               7 (stripped)

842            LOAD_FAST_BORROW         7 (stripped)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN

843            JUMP_BACKWARD           29 (to L2)

844    L3:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              15 (('import dotenv', 'from dotenv'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L4)
               NOT_TAKEN

845            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               1 ('dotenv import')
               CALL                     1
               POP_TOP

846    L4:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              16 (('import supabase', 'from supabase'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L5)
               NOT_TAKEN

847            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               2 ('supabase import')
               CALL                     1
               POP_TOP

848    L5:     LOAD_CONST               3 ('load_dotenv()')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       18 (to L6)
               NOT_TAKEN

849            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               4 ('load_dotenv() call')
               CALL                     1
               POP_TOP

850    L6:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              17 (('os.environ[', 'getenv('))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L7)
               NOT_TAKEN

851            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               5 ('environ read')
               CALL                     1
               POP_TOP

852    L7:     LOAD_CONST               6 ('get_supabase')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD          182 (to L2)

853    L8:     LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               7 ('supabase client call')
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          201 (to L2)

840    L9:     END_FOR
               POP_ITER

854            LOAD_FAST                1 (out)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_GLOBAL             19 (_check + NULL)

855            LOAD_CONST               8 ('self_check:no_env_or_db')

856            LOAD_FAST_BORROW         5 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST               9 ('FAIL')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST              10 ('PASS')

857   L11:     LOAD_CONST              11 ('PAS-SECURITY-02 readiness checker never reads .env / touches DB')

858            LOAD_FAST_BORROW         5 (bad)
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

854   L13:     LOAD_CONST              14 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

860            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181153E0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 867>:
867           RESUME                   0
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

Disassembly of <code object _aggregate at 0x0000018C17FA92F0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 867>:
 867            RESUME                   0

 869            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 868            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2

 869    L2:     FOR_ITER                49 (to L7)
                STORE_FAST               1 (c)

 870            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 869    L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L2)

 870    L4:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              2 (SEVERITY_BLOCK)
                COMPARE_OP              88 (bool(==))

 869    L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L2)
        L6:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L2)
        L7:     END_FOR
                POP_ITER

 868    L8:     STORE_FAST               2 (blockers)
                STORE_FAST               1 (c)

 873            LOAD_CONST               3 ('verdict')
                LOAD_FAST_BORROW         2 (blockers)
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L9)
                NOT_TAKEN
                LOAD_GLOBAL              4 (VERDICT_NOT_READY)
                JUMP_FORWARD             5 (to L10)
        L9:     LOAD_GLOBAL              6 (VERDICT_READY)

 874   L10:     LOAD_CONST               4 ('blockers')
                LOAD_FAST_BORROW         2 (blockers)

 875            LOAD_CONST               5 ('info')
                BUILD_LIST               0

 872            BUILD_MAP                3
                RETURN_VALUE

  --   L11:     SWAP                     2
                POP_TOP

 868            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L11 [2]
  L4 to L5 -> L11 [2]
  L6 to L8 -> L11 [2]

Disassembly of <code object __annotate__ at 0x0000018C181154D0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 879>:
879           RESUME                   0
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

Disassembly of <code object _operator_actions at 0x0000018C18048C70, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 879>:
879           RESUME                   0

880           BUILD_LIST               0
              STORE_FAST               1 (out)

881           LOAD_FAST_BORROW         0 (checks)
              GET_ITER
      L1:     FOR_ITER               109 (to L5)
              STORE_FAST               2 (c)

882           LOAD_FAST_BORROW         2 (c)
              LOAD_CONST               0 ('status')
              BINARY_OP               26 ([])
              LOAD_CONST               1 ('FAIL')
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

883           JUMP_BACKWARD           19 (to L1)

884   L2:     LOAD_FAST_BORROW         2 (c)
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

885           LOAD_FAST                1 (out)
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

881   L5:     END_FOR
              POP_ITER

886           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181155C0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 889>:
889           RESUME                   0
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

Disassembly of <code object evaluate at 0x0000018C177C5D50, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 889>:
889           RESUME                   0

890           BUILD_LIST               0
              STORE_FAST               1 (checks)

891           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              3 (check_files_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

892           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              5 (check_prior_phases_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

893           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              7 (check_memory_review_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

894           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              9 (check_worker_off_by_default + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

895           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             11 (check_v31_sql + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

896           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             13 (check_v32_sql + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

897           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             15 (check_rate_limit_service + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

898           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             17 (check_rate_limit_store + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

899           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             19 (check_dependency_scanner + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

900           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             21 (check_rotation_service + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

901           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             23 (check_rotation_routes + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

902           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             25 (check_audit_cli + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

903           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             27 (check_email_ingestion_rate_limit_wired + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

904           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             29 (check_slack_command_rate_limit_wired + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

905           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             31 (check_audit_service_invariant + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

906           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             33 (check_event_contract + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

907           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             35 (check_main_router_mounts + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

908           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             37 (check_no_forbidden_imports + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

909           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             39 (check_no_inbox_scan_tokens + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

910           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             41 (check_doc_required_clauses + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

911           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             43 (check_self_no_env_or_db + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

913           LOAD_GLOBAL             45 (_aggregate + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1
              STORE_FAST               2 (agg)

915           LOAD_CONST               0 ('phase')
              LOAD_CONST               1 ('PAS-SECURITY-02')

916           LOAD_CONST               2 ('generated_at')
              LOAD_GLOBAL             47 (_now_iso + NULL)
              CALL                     0

917           LOAD_CONST               3 ('verdict')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])

918           LOAD_CONST               4 ('ready')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])
              LOAD_GLOBAL             48 (VERDICT_READY)
              COMPARE_OP              72 (==)

919           LOAD_CONST               5 ('blocker_count')
              LOAD_GLOBAL             51 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               6 ('blockers')
              BINARY_OP               26 ([])
              CALL                     1

920           LOAD_CONST               7 ('info_count')
              LOAD_GLOBAL             51 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               8 ('info')
              BINARY_OP               26 ([])
              CALL                     1

921           LOAD_CONST               9 ('check_count')
              LOAD_GLOBAL             51 (len + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

922           LOAD_CONST              10 ('pass_count')
              LOAD_GLOBAL             53 (sum + NULL)
              LOAD_CONST              11 (<code object <genexpr> at 0x0000018C18053CF0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 922>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

923           LOAD_CONST              12 ('fail_count')
              LOAD_GLOBAL             53 (sum + NULL)
              LOAD_CONST              13 (<code object <genexpr> at 0x0000018C18053BD0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 923>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

924           LOAD_CONST              14 ('checks')
              LOAD_FAST_BORROW         1 (checks)

925           LOAD_CONST              15 ('operator_actions')
              LOAD_GLOBAL             55 (_operator_actions + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

914           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18053CF0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 922>:
 922           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C18053BD0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 923>:
 923           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C18115980, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 932>:
932           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C181287B0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 932>:
932           RESUME                   0

933           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

934           LOAD_CONST               0 ('pas_security_02_rate_limit_scanner_readiness_check')

936           LOAD_CONST               1 ('PAS-SECURITY-02 — Evaluate rate-limit + scanner + API-key rotation surfaces. Read-only — never reads .env, never touches Supabase, never runs a migration.')

933           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

942           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               3 ('--repo-root')
              LOAD_GLOBAL              6 (_REPO_ROOT_DEFAULT)
              LOAD_CONST               4 (('default',))
              CALL_KW                  2
              POP_TOP

943           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               5 ('--output')
              LOAD_GLOBAL              8 (REPORT_FILENAME)
              LOAD_CONST               4 (('default',))
              CALL_KW                  2
              POP_TOP

944           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               6 ('--json')
              LOAD_CONST               7 ('store_true')
              LOAD_CONST               8 (('action',))
              CALL_KW                  2
              POP_TOP

945           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               9 ('--summary-only')
              LOAD_CONST               7 ('store_true')
              LOAD_CONST               8 (('action',))
              CALL_KW                  2
              POP_TOP

946           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST              10 ('--strict')
              LOAD_CONST               7 ('store_true')
              LOAD_CONST               8 (('action',))
              CALL_KW                  2
              POP_TOP

947           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18115A70, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 950>:
950           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C17D8C5C0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 950>:
950           RESUME                   0

951           LOAD_GLOBAL              1 (print + NULL)

952           LOAD_CONST               0 ('[PAS-SECURITY-02] verdict=')
              LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               1 ('verdict')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               2 (' blockers=')

953           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               3 ('blocker_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' info=')

954           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               5 ('info_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' checks=')

955           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               7 ('check_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' pass=')

956           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               9 ('pass_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              10 (' fail=')

957           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              11 ('fail_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE

952           BUILD_STRING            12

951           CALL                     1
              POP_TOP

959           LOAD_FAST_BORROW         0 (report)
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

960           LOAD_FAST_BORROW         1 (actions)
              TO_BOOL
              POP_JUMP_IF_FALSE       93 (to L5)
              NOT_TAKEN

961           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              13 ('[PAS-SECURITY-02] operator actions:')
              CALL                     1
              POP_TOP

962           LOAD_FAST_BORROW         1 (actions)
              LOAD_CONST              14 (slice(None, 25, None))
              BINARY_OP               26 ([])
              GET_ITER
      L2:     FOR_ITER                17 (to L3)
              STORE_FAST               2 (a)

963           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              15 ('  - ')
              LOAD_FAST_BORROW         2 (a)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L2)

962   L3:     END_FOR
              POP_ITER

964           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         1 (actions)
              CALL                     1
              LOAD_SMALL_INT          25
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       34 (to L4)
              NOT_TAKEN

965           LOAD_GLOBAL              1 (print + NULL)
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

964   L4:     LOAD_CONST              18 (None)
              RETURN_VALUE

960   L5:     LOAD_CONST              18 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025A30, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 968>:
968           RESUME                   0
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

Disassembly of <code object _write_report at 0x0000018C18128990, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 968>:
 968           RESUME                   0

 969           NOP

 970   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

 971           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

 972           LOAD_CONST               3 ('utf-8')

 970           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 974           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

 975   L4:     LOAD_GLOBAL             11 (print + NULL)

 976           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

 977           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

 976           BUILD_STRING             4

 978           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

 975           LOAD_CONST               7 (('file',))
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

 974   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18115110, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 982>:
982           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17D88FF0, file "scripts/pas_security_02_rate_limit_scanner_readiness_check.py", line 982>:
 982            RESUME                   0

 983            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 984            NOP

 985    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 989    L2:     LOAD_GLOBAL             10 (os)
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

 990            LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               21 (isdir + NULL|self)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L4)
                NOT_TAKEN

 991            LOAD_GLOBAL             23 (print + NULL)
                LOAD_CONST               2 ('error: --repo-root not a directory: ')
                LOAD_FAST                4 (repo_root)
                FORMAT_SIMPLE
                BUILD_STRING             2
                LOAD_GLOBAL             24 (sys)
                LOAD_ATTR               26 (stderr)
                LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

 992            LOAD_SMALL_INT           2
                RETURN_VALUE

 994    L4:     LOAD_GLOBAL             29 (evaluate + NULL)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                STORE_FAST               5 (report)

 996            LOAD_FAST                2 (args)
                LOAD_ATTR               30 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L5)
                NOT_TAKEN

 997            LOAD_GLOBAL             33 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               34 (output)
                LOAD_FAST                5 (report)
                CALL                     2
                POP_TOP

 999    L5:     LOAD_GLOBAL             37 (_print_summary + NULL)
                LOAD_FAST                5 (report)
                CALL                     1
                POP_TOP

1001            LOAD_FAST                2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L6)
                NOT_TAKEN

1002            LOAD_GLOBAL             23 (print + NULL)
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

1004    L6:     LOAD_FAST                5 (report)
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

 986            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L17)
                NOT_TAKEN
                STORE_FAST               3 (e)

 987    L9:     LOAD_FAST                3 (e)
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

 986   L17:     RERAISE                  0

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
