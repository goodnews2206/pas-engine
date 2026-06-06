# scripts_readiness/pas_security_04_operator_reveal_https_readiness_check

- **pyc:** `scripts\__pycache__\pas_security_04_operator_reveal_https_readiness_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/pas_security_04_operator_reveal_https_readiness_check.py`
- **co_filename (from bytecode):** `scripts/pas_security_04_operator_reveal_https_readiness_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS-SECURITY-04 — Operator route consolidation + one-time
reveal + severity-aware CI + HTTPS enforcement readiness gate.

Deterministic, non-mutating evaluator for "is PAS-SECURITY-04
wired correctly and free of regressions in the
PAS160-PAS-SECURITY-03 doctrine?".

Walks the repo and verifies:

  * PAS160-PAS181 + PAS-SECURITY-01/02/03 readiness scripts
    still exist.
  * PAS-SECURITY-04 surfaces exist:
      - scripts/migrate_v34_api_key_one_time_reveal.sql
      - app/services/security/operator_auth.py
      - app/services/security/api_key_reveal.py
      - app/services/security/https_enforcement.py
      - scripts/pas_security_04_operator_reveal_https_readiness_check.py
      - docs/pas_security_04_operator_reveal_https.md
      - tests/mvp/test_pas_security_04_operator_reveal_https.py
  * v34 SQL: PROPOSAL ONLY, ALTER TABLE on v32, sha256 hex
    pin, USING (revealed_at IS NULL) one-time semantics,
    extended service_role UPDATE policy.
  * operator_auth.py exposes documented surface.
  * api_key_reveal.py exposes documented surface; raw_api_key
    path is deferred.
  * https_enforcement.py exposes documented surface.
  * /admin/*, /ops/*, security_api_key_rotation.py operator
    router all have require_admin wired with check_rate_limit.
  * tenant reveal route exists at GET /tenant/api-key/rotation/{id}/reveal.
  * tenant reveal route's raw_api_key path is None (deferred).
  * Severity-aware scanner exports ALLOWED_SEVERITY_TIERS +
    _classify_severity helper.
  * CI gate accepts --fail-on-medium / --fail-on-high /
    --fail-on-critical and maps to closed thresholds.
  * app/main.py registers HTTPSEnforcementMiddleware.
  * No raw key / token / signature echo in PAS-SECURITY-04
    surfaces.
  * No auto-fix tokens in executable form.
  * Process-local fallback marker still exists (carry-forward).
  * No Gmail / OAuth / IMAP / POP3 / Composio / TrustClaw /
    embeddings / vector / LLM imports.
  * Memory Review (PAS147-PAS158) untouched.
  * audit_service still has no UPDATE / DELETE helpers.
  * Event contract registers PAS-SECURITY-04 events.
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

`__annotate__`, `_aggregate`, `_build_parser`, `_check`, `_now_iso`, `_operator_actions`, `_print_summary`, `_read_text`, `_strip_python_comments_and_strings`, `_write_report`, `check_api_key_reveal_service`, `check_audit_service_invariant`, `check_ci_gate_severity_flags`, `check_doc_required_clauses`, `check_event_contract`, `check_files_present`, `check_https_enforcement_service`, `check_https_middleware`, `check_memory_review_intact`, `check_no_forbidden_imports`, `check_no_inbox_scan_tokens`, `check_no_raw_key_storage_or_echo`, `check_operator_auth_service`, `check_operator_route_rate_limit_wired`, `check_prior_phases_intact`, `check_process_local_fallback_carry_forward`, `check_reveal_route_present`, `check_self_no_env_or_db`, `check_severity_scanner`, `check_v34_sql`, `check_worker_off_by_default`, `evaluate`, `main`

## Env-key candidates

`BLOCK`, `FAIL`, `INFO`, `NOT_READY`, `PASS`, `READY`

## String constants (redacted where noted)

- '\nPAS-SECURITY-04 — Operator route consolidation + one-time\nreveal + severity-aware CI + HTTPS enforcement readiness gate.\n\nDeterministic, non-mutating evaluator for "is PAS-SECURITY-04\nwired correctly and free of regressions in the\nPAS160-PAS-SECURITY-03 doctrine?".\n\nWalks the repo and verifies:\n\n  * PAS160-PAS181 + PAS-SECURITY-01/02/03 readiness scripts\n    still exist.\n  * PAS-SECURITY-04 surfaces exist:\n      - scripts/migrate_v34_api_key_one_time_reveal.sql\n      - app/services/security/operator_auth.py\n      - app/services/security/api_key_reveal.py\n      - app/services/security/https_enforcement.py\n      - scripts/pas_security_04_operator_reveal_https_readiness_check.py\n      - docs/pas_security_04_operator_reveal_https.md\n      - tests/mvp/test_pas_security_04_operator_reveal_https.py\n  * v34 SQL: PROPOSAL ONLY, ALTER TABLE on v32, sha256 hex\n    pin, USING (revealed_at IS NULL) one-time semantics,\n    extended service_role UPDATE policy.\n  * operator_auth.py exposes documented surface.\n  * api_key_reveal.py exposes documented surface; raw_api_key\n    path is deferred.\n  * https_enforcement.py exposes documented surface.\n  * /admin/*, /ops/*, security_api_key_rotation.py operator\n    router all have require_admin wired with check_rate_limit.\n  * tenant reveal route exists at GET /tenant/api-key/rotation/{id}/reveal.\n  * tenant reveal route\'s raw_api_key path is None (deferred).\n  * Severity-aware scanner exports ALLOWED_SEVERITY_TIERS +\n    _classify_severity helper.\n  * CI gate accepts --fail-on-medium / --fail-on-high /\n    --fail-on-critical and maps to closed thresholds.\n  * app/main.py registers HTTPSEnforcementMiddleware.\n  * No raw key / token / signature echo in PAS-SECURITY-04\n    surfaces.\n  * No auto-fix tokens in executable form.\n  * Process-local fallback marker still exists (carry-forward).\n  * No Gmail / OAuth / IMAP / POP3 / Composio / TrustClaw /\n    embeddings / vector / LLM imports.\n  * Memory Review (PAS147-PAS158) untouched.\n  * audit_service still has no UPDATE / DELETE helpers.\n  * Event contract registers PAS-SECURITY-04 events.\n  * Worker still OFF by default.\n  * Supports --summary-only / --json.\n  * Exits 0 ready, 1 blockers, 2 bad args.\n  * Never reads .env.\n  * Never touches production data.\n'
- 'utf-8'
- 'READY'
- 'NOT_READY'
- 'BLOCK'
- 'INFO'
- 'severity'
- 'detail'
- 'pas_security_04_operator_reveal_https_readiness_report.json'
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
- 'Required PAS-SECURITY-04 file present: '
- 'missing'
- 'prior_phase:'
- 'Prior-phase readiness script intact: '
- 'missing — PAS-SECURITY-04 must not delete'
- 'memory_review:'
- 'Memory Review file present: '
- 'Memory Review file deleted — PAS-SECURITY-04 must not touch'
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
- 'migrate_v34_api_key_one_time_reveal.sql'
- 'v34_sql:proposal_only'
- 'proposal only'
- "v34 SQL carries 'PROPOSAL ONLY' guardrail"
- 'v34_sql:do_not_execute'
- 'do not execute'
- "v34 SQL carries 'DO NOT EXECUTE' trailer"
- 'ALTER TABLE pas_api_key_rotation_events'
- 'v34_sql:alter_v32_table'
- 'v34 SQL ALTERs pas_api_key_rotation_events'
- 'reveal_token_hash'
- 'reveal_token_expires_at'
- 'revealed_at'
- 'reveal_attempt_count'
- 'v34_sql:reveal_columns'
- 'v34 SQL adds all four reveal columns'
- "'^[0-9a-f]{64}$'"
- 'v34_sql:sha256_pin'
- 'v34 SQL pins reveal_token_hash to sha256 hex shape'
- 'revealed_at IS NULL'
- 'v34_sql:one_time_semantics'
- 'v34 SQL enforces one-time reveal via USING (revealed_at IS NULL)'
- 'security'
- 'operator_auth.py'
- 'operator_auth:'
- 'operator_auth module exports '
- 'missing token '
- 'api_key_reveal.py'
- 'reveal_service:'
- 'api_key_reveal module exports '
- 'raw_key_reveal_unsupported'
- 'reveal_service:deferred_raw_key'
- "api_key_reveal's raw-key path is deferred (raw_key_reveal_unsupported error code)"
- 'https_enforcement.py'
- 'https_enforcement:'
- 'https_enforcement module exports '
- "Every operator route file's require_admin wires\ncheck_rate_limit(surface=admin, actor_type=ADMIN)."
- 'check_rate_limit('
- 'surface="admin"'
- 'actor_type="ADMIN"'
- 'status_code=429'
- 'operator_route_rate_limit:'
- ' wires operator/admin rate-limit'
- 'missing required rate-limit wiring'
- 'routes'
- 'security_api_key_rotation.py'
- '/rotation/{rotation_id}/reveal'
- 'tenant_rotation_reveal_route'
- 'reveal_rotated_api_key_once'
- 'reveal_route:tenant_get_reveal'
- 'Tenant GET /tenant/api-key/rotation/{id}/reveal route wired'
- 'missing reveal route or handler'
- 'raw_api_key_value'
- 'reveal_route:no_raw_key_value'
- 'Reveal route does NOT reference a raw_api_key_value variable'
- 'dependency_scanner.py'
- 'severity_scanner:'
- 'dependency_scanner exports '
- 'security_ci_dependency_gate.py'
- 'ci_gate:'
- 'security_ci_dependency_gate exports '
- 'ci_gate:no_auto_fix'
- 'CI gate has no auto-fix tokens in executable form'
- 'disqualifying tokens: '
- 'main.py'
- 'HTTPSEnforcementMiddleware'
- 'add_middleware(HTTPSEnforcementMiddleware'
- 'should_reject_insecure_request'
- 'main:https_middleware'
- 'app/main.py registers HTTPSEnforcementMiddleware'
- 'missing HTTPS middleware wiring'
- 'PAS-SECURITY-04 surfaces MUST NEVER carry forbidden raw-\nkey / raw-token / user-agent-raw tokens in executable form.'
- 'no_raw_key_or_token:'
- 'No raw_api_key_value / raw_reveal_token / user_agent_raw in executable: '
- 'operator'
- 'audit_service.py'
- 'audit_service:append_only_carry'
- 'Audit service still has no UPDATE / DELETE mutation helpers (carry-forward invariant)'
- 'events'
- 'contract.py'
- 'events:'
- 'Event contract registers '
- 'missing event type '
- 'app/services/security/operator_auth.py'
- 'forbidden_import:'
- 'No forbidden imports: '
- 'forbidden import prefixes: '
- 'no_inbox_scan:'
- 'No inbox-scanning tokens: '
- 'inbox-scan tokens present: '
- 'rate_limit_store.py'
- 'rate_limit_store_process_local'
- 'carry_forward:process_local_fallback'
- 'PAS-SECURITY-02 process-local fallback marker still present'
- 'docs'
- 'pas_security_04_operator_reveal_https.md'
- 'docs:pas_security_04:'
- 'PAS-SECURITY-04 doctrine carries clause: '
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
- 'PAS-SECURITY-04 readiness checker never reads .env / touches DB'
- 'disqualifying patterns: '
- 'checks'
- 'verdict'
- 'blockers'
- 'info'
- 'List[str]'
- ' — '
- 'see report'
- 'phase'
- 'PAS-SECURITY-04'
- 'generated_at'
- 'ready'
- 'blocker_count'
- 'info_count'
- 'check_count'
- 'pass_count'
- 'fail_count'
- 'operator_actions'
- 'argparse.ArgumentParser'
- 'pas_security_04_operator_reveal_https_readiness_check'
- 'PAS-SECURITY-04 — Evaluate operator-route consolidation + one-time API-key reveal + severity-aware CI gate + HTTPS enforcement. Read-only — never reads .env, never touches Supabase, never runs a migration.'
- '--repo-root'
- '--output'
- '--json'
- 'store_true'
- '--summary-only'
- '--strict'
- 'report'
- 'None'
- '[PAS-SECURITY-04] verdict='
- ' blockers='
- ' info='
- ' checks='
- ' pass='
- ' fail='
- '[PAS-SECURITY-04] operator actions:'
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

   1           LOAD_CONST               0 ('\nPAS-SECURITY-04 — Operator route consolidation + one-time\nreveal + severity-aware CI + HTTPS enforcement readiness gate.\n\nDeterministic, non-mutating evaluator for "is PAS-SECURITY-04\nwired correctly and free of regressions in the\nPAS160-PAS-SECURITY-03 doctrine?".\n\nWalks the repo and verifies:\n\n  * PAS160-PAS181 + PAS-SECURITY-01/02/03 readiness scripts\n    still exist.\n  * PAS-SECURITY-04 surfaces exist:\n      - scripts/migrate_v34_api_key_one_time_reveal.sql\n      - app/services/security/operator_auth.py\n      - app/services/security/api_key_reveal.py\n      - app/services/security/https_enforcement.py\n      - scripts/pas_security_04_operator_reveal_https_readiness_check.py\n      - docs/pas_security_04_operator_reveal_https.md\n      - tests/mvp/test_pas_security_04_operator_reveal_https.py\n  * v34 SQL: PROPOSAL ONLY, ALTER TABLE on v32, sha256 hex\n    pin, USING (revealed_at IS NULL) one-time semantics,\n    extended service_role UPDATE policy.\n  * operator_auth.py exposes documented surface.\n  * api_key_reveal.py exposes documented surface; raw_api_key\n    path is deferred.\n  * https_enforcement.py exposes documented surface.\n  * /admin/*, /ops/*, security_api_key_rotation.py operator\n    router all have require_admin wired with check_rate_limit.\n  * tenant reveal route exists at GET /tenant/api-key/rotation/{id}/reveal.\n  * tenant reveal route\'s raw_api_key path is None (deferred).\n  * Severity-aware scanner exports ALLOWED_SEVERITY_TIERS +\n    _classify_severity helper.\n  * CI gate accepts --fail-on-medium / --fail-on-high /\n    --fail-on-critical and maps to closed thresholds.\n  * app/main.py registers HTTPSEnforcementMiddleware.\n  * No raw key / token / signature echo in PAS-SECURITY-04\n    surfaces.\n  * No auto-fix tokens in executable form.\n  * Process-local fallback marker still exists (carry-forward).\n  * No Gmail / OAuth / IMAP / POP3 / Composio / TrustClaw /\n    embeddings / vector / LLM imports.\n  * Memory Review (PAS147-PAS158) untouched.\n  * audit_service still has no UPDATE / DELETE helpers.\n  * Event contract registers PAS-SECURITY-04 events.\n  * Worker still OFF by default.\n  * Supports --summary-only / --json.\n  * Exits 0 ready, 1 blockers, 2 bad args.\n  * Never reads .env.\n  * Never touches production data.\n')
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

  80           LOAD_CONST              12 ('INFO')
               STORE_NAME              28 (SEVERITY_INFO)

  83           LOAD_CONST              82 (('scripts/migrate_v34_api_key_one_time_reveal.sql', 'app/services/security/operator_auth.py', 'app/services/security/api_key_reveal.py', 'app/services/security/https_enforcement.py', 'scripts/pas_security_04_operator_reveal_https_readiness_check.py', 'docs/pas_security_04_operator_reveal_https.md', 'tests/mvp/test_pas_security_04_operator_reveal_https.py'))
               STORE_NAME              29 (REQUIRED_FILES)

  94           LOAD_CONST              83 (('scripts/pas160_mvp_sequence_check.py', 'scripts/pas169_launch_readiness_check.py', 'scripts/pas_launch_integrity_check.py', 'scripts/pas170_operator_survival_readiness_check.py', 'scripts/pas171_external_pilot_readiness_check.py', 'scripts/pas172_pilot_operations_readiness_check.py', 'scripts/pas173_brokerage_operator_readiness_check.py', 'scripts/pas174_operator_audit_readiness_check.py', 'scripts/pas175_audit_integrity_readiness_check.py', 'scripts/pas176_audit_chain_readiness_check.py', 'scripts/pas177_tenant_audit_verification_readiness_check.py', 'scripts/pas178_audit_window_chain_readiness_check.py', 'scripts/pas179_controlled_learning_readiness_check.py', 'scripts/pas180_learning_review_readiness_check.py', 'scripts/pas181_manual_test_harness_readiness_check.py', 'scripts/pas_security_01_hardening_readiness_check.py', 'scripts/pas_security_02_rate_limit_scanner_readiness_check.py', 'scripts/pas_security_03_admin_webhook_ci_readiness_check.py'))
               STORE_NAME              30 (PRIOR_PHASE_FILES)

 115           LOAD_CONST              84 (('app/services/memory/review.py', 'app/services/memory/review_stats.py', 'app/services/memory/review_export.py', 'app/services/memory/review_actors.py', 'app/services/memory/review_alerts.py', 'app/services/memory/operator_console.py'))
               STORE_NAME              31 (MEMORY_REVIEW_FILES)

 125           LOAD_CONST              85 (('def require_operator_or_admin(', 'def operator_actor_context(', 'def operator_rate_limit_context(', 'ALLOWED_ACTOR_TYPES', 'OPERATOR_AUTH_SURFACE', 'actor_fingerprint'))
               STORE_NAME              32 (REQUIRED_OPERATOR_AUTH_TOKENS)

 134           LOAD_CONST              86 (('def create_one_time_reveal_token(', 'def verify_one_time_reveal_token(', 'def reveal_rotated_api_key_once(', 'def mark_reveal_attempt(', 'def reveal_status(', 'ALLOWED_REVEAL_STATUSES', 'REVEAL_TOKEN_TTL_SECONDS', 'raw_key_reveal_unsupported', '_TABLE = "pas_api_key_rotation_events"'))
               STORE_NAME              33 (REQUIRED_REVEAL_TOKENS)

 146           LOAD_CONST              87 (('def https_enforcement_enabled(', 'def should_reject_insecure_request(', 'def insecure_request_public_error(', 'ALLOWED_ENVIRONMENT_TIERS', 'PRODUCTION_TIER_ENVIRONMENTS'))
               STORE_NAME              34 (REQUIRED_HTTPS_TOKENS)

 154           LOAD_CONST              88 (('app/routes/admin.py', 'app/routes/operator_ops.py', 'app/routes/operator_brokerages.py', 'app/routes/operator_learning.py', 'app/routes/operator_learning_tests.py', 'app/routes/security_api_key_rotation.py'))
               STORE_NAME              35 (OPERATOR_ROUTE_FILES)

 164           LOAD_CONST              89 (('security.admin.rate_limit_blocked', 'security.api_key_rotation.requested', 'security.operator.auth_failed', 'security.operator.rate_limit_blocked', 'security.api_key_reveal.created', 'security.api_key_reveal.succeeded', 'security.api_key_reveal.failed', 'security.dependency_ci_gate.severity_blocked', 'security.https.insecure_request_blocked'))
               STORE_NAME              36 (REQUIRED_EVENT_TYPES)

 179           LOAD_CONST              90 (('import gmail', 'from gmail', 'import googleapiclient', 'from googleapiclient', 'import google.oauth2', 'from google.oauth2', 'from google.auth', 'import google.auth', 'from google_auth_oauthlib', 'import imaplib', 'from imaplib', 'import poplib', 'from poplib', 'import composio', 'from composio', 'import trustclaw', 'from trustclaw', 'import chromadb', 'from chromadb', 'import pinecone', 'from pinecone', 'import langchain', 'from langchain', 'import faiss', 'import pgvector', 'from pgvector', 'from openai import embeddings', 'from openai.embeddings', 'from anthropic', 'import anthropic', 'from openai', 'import openai'))
               STORE_NAME              37 (FORBIDDEN_IMPORT_LINE_PREFIXES)

 203           LOAD_CONST              91 (('imaplib', 'poplib', 'fetch_inbox', 'gmail_oauth', 'gmail_token', 'users().messages'))
               STORE_NAME              38 (FORBIDDEN_INBOX_TOKENS)

 213           LOAD_CONST              92 (('pip install', 'pip-audit fix', 'npm audit fix', 'npm install', 'poetry update', 'yarn upgrade'))
               STORE_NAME              39 (FORBIDDEN_AUTO_FIX_TOKENS)

 223           LOAD_CONST              93 (('raw_api_key_value', 'raw_reveal_token', 'user_agent_raw'))
               STORE_NAME              40 (FORBIDDEN_RAW_KEY_TOKENS)

 234           LOAD_CONST              13 ('severity')

 236           LOAD_NAME               27 (SEVERITY_BLOCK)

 234           LOAD_CONST              14 ('detail')

 236           LOAD_CONST              15 ('')

 234           BUILD_MAP                2
               LOAD_CONST              16 (<code object __annotate__ at 0x0000018C18024B30, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 234>)
               MAKE_FUNCTION
               LOAD_CONST              17 (<code object _check at 0x0000018C17FA2A60, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 234>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              41 (_check)

 247           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA2970, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 247>)
               MAKE_FUNCTION
               LOAD_CONST              19 (<code object _now_iso at 0x0000018C18038170, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 247>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              42 (_now_iso)

 251           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA23D0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 251>)
               MAKE_FUNCTION
               LOAD_CONST              21 (<code object _read_text at 0x0000018C18052F70, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 251>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              43 (_read_text)

 258           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA3B40, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 258>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object _strip_python_comments_and_strings at 0x0000018C18646C00, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 258>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              44 (_strip_python_comments_and_strings)

 297           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA2F10, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 297>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object check_files_present at 0x0000018C18060F60, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 297>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              45 (check_files_present)

 310           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA33C0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 310>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object check_prior_phases_intact at 0x0000018C180612C0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 310>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              46 (check_prior_phases_intact)

 323           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA35A0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 323>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object check_memory_review_intact at 0x0000018C180606F0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 323>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              47 (check_memory_review_intact)

 336           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA3D20, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 336>)
               MAKE_FUNCTION
               LOAD_CONST              31 (<code object check_worker_off_by_default at 0x0000018C18128030, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 336>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              48 (check_worker_off_by_default)

 353           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA1D40, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 353>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object check_v34_sql at 0x0000018C17D8BD50, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 353>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              49 (check_v34_sql)

 404           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA2880, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 404>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object check_operator_auth_service at 0x0000018C17FEDE30, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 404>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              50 (check_operator_auth_service)

 419           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C17FA2100, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 419>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object check_api_key_reveal_service at 0x0000018C181B05D0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 419>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              51 (check_api_key_reveal_service)

 441           LOAD_CONST              38 (<code object __annotate__ at 0x0000018C17FA2B50, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 441>)
               MAKE_FUNCTION
               LOAD_CONST              39 (<code object check_https_enforcement_service at 0x0000018C17FEDC30, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 441>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              52 (check_https_enforcement_service)

 456           LOAD_CONST              40 (<code object __annotate__ at 0x0000018C17FA32D0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 456>)
               MAKE_FUNCTION
               LOAD_CONST              41 (<code object check_operator_route_rate_limit_wired at 0x0000018C17EC44A0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 456>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              53 (check_operator_route_rate_limit_wired)

 478           LOAD_CONST              42 (<code object __annotate__ at 0x0000018C17FA3780, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 478>)
               MAKE_FUNCTION
               LOAD_CONST              43 (<code object check_reveal_route_present at 0x0000018C17ECEDB0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 478>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              54 (check_reveal_route_present)

 504           LOAD_CONST              44 (<code object __annotate__ at 0x0000018C17FA1E30, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 504>)
               MAKE_FUNCTION
               LOAD_CONST              45 (<code object check_severity_scanner at 0x0000018C17FEE430, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 504>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              55 (check_severity_scanner)

 526           LOAD_CONST              46 (<code object __annotate__ at 0x0000018C17FA2E20, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 526>)
               MAKE_FUNCTION
               LOAD_CONST              47 (<code object check_ci_gate_severity_flags at 0x0000018C17EE1CC0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 526>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              56 (check_ci_gate_severity_flags)

 560           LOAD_CONST              48 (<code object __annotate__ at 0x0000018C17FA21F0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 560>)
               MAKE_FUNCTION
               LOAD_CONST              49 (<code object check_https_middleware at 0x0000018C181287B0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 560>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              57 (check_https_middleware)

 578           LOAD_CONST              50 (<code object __annotate__ at 0x0000018C17FA26A0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 578>)
               MAKE_FUNCTION
               LOAD_CONST              51 (<code object check_no_raw_key_storage_or_echo at 0x0000018C17CC2E60, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 578>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              58 (check_no_raw_key_storage_or_echo)

 607           LOAD_CONST              52 (<code object __annotate__ at 0x0000018C17FA22E0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 607>)
               MAKE_FUNCTION
               LOAD_CONST              53 (<code object check_audit_service_invariant at 0x0000018C182DCD60, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 607>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              59 (check_audit_service_invariant)

 632           LOAD_CONST              54 (<code object __annotate__ at 0x0000018C17FA24C0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 632>)
               MAKE_FUNCTION
               LOAD_CONST              55 (<code object check_event_contract at 0x0000018C179A7290, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 632>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              60 (check_event_contract)

 647           LOAD_CONST              56 (<code object __annotate__ at 0x0000018C17FA25B0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 647>)
               MAKE_FUNCTION
               LOAD_CONST              57 (<code object check_no_forbidden_imports at 0x0000018C17EA53C0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 647>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              61 (check_no_forbidden_imports)

 678           LOAD_CONST              58 (<code object __annotate__ at 0x0000018C17FA2D30, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 678>)
               MAKE_FUNCTION
               LOAD_CONST              59 (<code object check_no_inbox_scan_tokens at 0x0000018C17CC1CE0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 678>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              62 (check_no_inbox_scan_tokens)

 705           LOAD_CONST              60 (<code object __annotate__ at 0x0000018C17FA3A50, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 705>)
               MAKE_FUNCTION
               LOAD_CONST              61 (<code object check_process_local_fallback_carry_forward at 0x0000018C18060C00, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 705>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              63 (check_process_local_fallback_carry_forward)

 718           LOAD_CONST              62 (<code object __annotate__ at 0x0000018C181153E0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 718>)
               MAKE_FUNCTION
               LOAD_CONST              63 (<code object check_doc_required_clauses at 0x0000018C17CD0CE0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 718>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              64 (check_doc_required_clauses)

 763           LOAD_CONST              64 (<code object __annotate__ at 0x0000018C181154D0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 763>)
               MAKE_FUNCTION
               LOAD_CONST              65 (<code object check_self_no_env_or_db at 0x0000018C17D884E0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 763>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              65 (check_self_no_env_or_db)

 796           LOAD_CONST              66 (<code object __annotate__ at 0x0000018C181155C0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 796>)
               MAKE_FUNCTION
               LOAD_CONST              67 (<code object _aggregate at 0x0000018C1800B0A0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 796>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              66 (_aggregate)

 808           LOAD_CONST              68 (<code object __annotate__ at 0x0000018C18115980, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 808>)
               MAKE_FUNCTION
               LOAD_CONST              69 (<code object _operator_actions at 0x0000018C18048AB0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 808>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              67 (_operator_actions)

 818           LOAD_CONST              70 (<code object __annotate__ at 0x0000018C18115A70, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 818>)
               MAKE_FUNCTION
               LOAD_CONST              71 (<code object evaluate at 0x0000018C177C63A0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 818>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              68 (evaluate)

 858           LOAD_CONST              72 ('pas_security_04_operator_reveal_https_readiness_report.json')
               STORE_NAME              69 (REPORT_FILENAME)

 861           LOAD_CONST              73 (<code object __annotate__ at 0x0000018C18115110, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 861>)
               MAKE_FUNCTION
               LOAD_CONST              74 (<code object _build_parser at 0x0000018C181283F0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 861>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              70 (_build_parser)

 880           LOAD_CONST              75 (<code object __annotate__ at 0x0000018C18115D40, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 880>)
               MAKE_FUNCTION
               LOAD_CONST              76 (<code object _print_summary at 0x0000018C17D8C5C0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 880>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              71 (_print_summary)

 898           LOAD_CONST              77 (<code object __annotate__ at 0x0000018C18024930, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 898>)
               MAKE_FUNCTION
               LOAD_CONST              78 (<code object _write_report at 0x0000018C18128D50, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 898>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              72 (_write_report)

 912           LOAD_CONST              94 ((None,))
               LOAD_CONST              79 (<code object __annotate__ at 0x0000018C181157A0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 912>)
               MAKE_FUNCTION
               LOAD_CONST              80 (<code object main at 0x0000018C17D88890, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 912>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              73 (main)

 937           LOAD_NAME               74 (__name__)
               LOAD_CONST              81 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 938           LOAD_NAME                6 (sys)
               LOAD_ATTR              150 (exit)
               PUSH_NULL
               LOAD_NAME               73 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 937   L5:     LOAD_CONST               2 (None)
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

Disassembly of <code object __annotate__ at 0x0000018C18024B30, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 234>:
234           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('check_id')

235           LOAD_CONST               2 ('str')

234           LOAD_CONST               3 ('status')

235           LOAD_CONST               2 ('str')

234           LOAD_CONST               4 ('label')

235           LOAD_CONST               2 ('str')

234           LOAD_CONST               5 ('severity')

236           LOAD_CONST               2 ('str')

234           LOAD_CONST               6 ('detail')

236           LOAD_CONST               2 ('str')

234           LOAD_CONST               7 ('return')

237           LOAD_CONST               8 ('dict')

234           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _check at 0x0000018C17FA2A60, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 234>:
234           RESUME                   0

239           LOAD_CONST               0 ('id')
              LOAD_FAST_BORROW         0 (check_id)

240           LOAD_CONST               1 ('status')
              LOAD_FAST_BORROW         1 (status)

241           LOAD_CONST               2 ('label')
              LOAD_FAST_BORROW         2 (label)

242           LOAD_CONST               3 ('severity')
              LOAD_FAST_BORROW         3 (severity)

243           LOAD_CONST               4 ('detail')
              LOAD_FAST_BORROW         4 (detail)

238           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 247>:
247           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038170, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 247>:
247           RESUME                   0

248           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 251>:
251           RESUME                   0
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

Disassembly of <code object _read_text at 0x0000018C18052F70, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 251>:
 251           RESUME                   0

 252           NOP

 253   L1:     LOAD_FAST_BORROW         0 (path)
               LOAD_ATTR                1 (read_text + NULL|self)
               LOAD_CONST               0 ('utf-8')
               LOAD_CONST               1 ('replace')
               LOAD_CONST               2 (('encoding', 'errors'))
               CALL_KW                  2
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 254           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 255   L4:     POP_EXCEPT
               LOAD_CONST               3 (None)
               RETURN_VALUE

 254   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 258>:
258           RESUME                   0
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

Disassembly of <code object _strip_python_comments_and_strings at 0x0000018C18646C00, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 258>:
258            RESUME                   0

259            BUILD_LIST               0
               STORE_FAST               1 (out)

260            LOAD_SMALL_INT           0
               LOAD_GLOBAL              1 (len + NULL)
               LOAD_FAST_BORROW         0 (src)
               CALL                     1
               STORE_FAST_STORE_FAST   50 (n, i)

261    L1:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (i, n)
               COMPARE_OP              18 (bool(<))
               EXTENDED_ARG             1
               POP_JUMP_IF_FALSE      282 (to L13)
               NOT_TAKEN

262            LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               BINARY_OP               26 ([])
               STORE_FAST               4 (ch)

263            LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               1 ('#')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       38 (to L3)
               NOT_TAKEN

264            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_CONST               2 ('\n')
               LOAD_FAST_BORROW         2 (i)
               CALL                     2
               STORE_FAST               5 (j)

265            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L2)
               NOT_TAKEN

266            JUMP_FORWARD           240 (to L13)

267    L2:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

268            JUMP_BACKWARD           59 (to L1)

269    L3:     LOAD_FAST_BORROW         0 (src)
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

270    L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               BINARY_SLICE
               STORE_FAST               6 (quote)

271            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 98 (quote, i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               CALL                     2
               STORE_FAST               7 (end)

272            LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L5)
               NOT_TAKEN

273            JUMP_FORWARD           138 (to L13)

274    L5:     LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

275            JUMP_BACKWARD          161 (to L1)

276    L6:     LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               7 (('"', "'"))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       92 (to L12)
               NOT_TAKEN

277            LOAD_FAST                4 (ch)
               STORE_FAST               6 (quote)

278            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               5 (j)

279    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (j, n)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       63 (to L11)
               NOT_TAKEN

280            LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
               BINARY_OP               26 ([])
               LOAD_CONST               5 ('\\')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       12 (to L8)
               NOT_TAKEN

281            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           2
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)

282            JUMP_BACKWARD           30 (to L7)

283    L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
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

284    L9:     JUMP_FORWARD            11 (to L11)

285   L10:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)
               JUMP_BACKWARD           68 (to L7)

286   L11:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

287            EXTENDED_ARG             1
               JUMP_BACKWARD          259 (to L1)

288   L12:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (ch)
               CALL                     1
               POP_TOP

289            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               2 (i)
               EXTENDED_ARG             1
               JUMP_BACKWARD          288 (to L1)

290   L13:     LOAD_CONST               6 ('')
               LOAD_ATTR                9 (join + NULL|self)
               LOAD_FAST_BORROW         1 (out)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 297>:
297           RESUME                   0
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

Disassembly of <code object check_files_present at 0x0000018C18060F60, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 297>:
297           RESUME                   0

298           BUILD_LIST               0
              STORE_FAST               1 (out)

299           LOAD_GLOBAL              0 (REQUIRED_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

300           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

301           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

302           LOAD_CONST               0 ('file:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

303           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

304   L3:     LOAD_CONST               3 ('Required PAS-SECURITY-04 file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

305           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing')

301   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

299   L6:     END_FOR
              POP_ITER

307           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 310>:
310           RESUME                   0
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

Disassembly of <code object check_prior_phases_intact at 0x0000018C180612C0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 310>:
310           RESUME                   0

311           BUILD_LIST               0
              STORE_FAST               1 (out)

312           LOAD_GLOBAL              0 (PRIOR_PHASE_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

313           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

314           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

315           LOAD_CONST               0 ('prior_phase:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

316           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

317   L3:     LOAD_CONST               3 ('Prior-phase readiness script intact: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

318           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing — PAS-SECURITY-04 must not delete')

314   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

312   L6:     END_FOR
              POP_ITER

320           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 323>:
323           RESUME                   0
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

Disassembly of <code object check_memory_review_intact at 0x0000018C180606F0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 323>:
323           RESUME                   0

324           BUILD_LIST               0
              STORE_FAST               1 (out)

325           LOAD_GLOBAL              0 (MEMORY_REVIEW_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

326           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

327           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

328           LOAD_CONST               0 ('memory_review:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

329           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

330   L3:     LOAD_CONST               3 ('Memory Review file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

331           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('Memory Review file deleted — PAS-SECURITY-04 must not touch')

327   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

325   L6:     END_FOR
              POP_ITER

333           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3D20, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 336>:
336           RESUME                   0
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

Disassembly of <code object check_worker_off_by_default at 0x0000018C18128030, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 336>:
336           RESUME                   0

337           BUILD_LIST               0
              STORE_FAST               1 (out)

338           LOAD_GLOBAL              1 (Path + NULL)
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

339           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

341           LOAD_CONST               5 ('_ENV_FLAG_ENABLED_LITERAL = "true"')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         6 (to L2)
              NOT_TAKEN
              POP_TOP

342           LOAD_CONST               6 ("_ENV_FLAG_ENABLED_LITERAL = 'true'")
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)

340   L2:     STORE_FAST               4 (literal_ok)

344           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

345           LOAD_CONST               7 ('worker:off_by_default')

346           LOAD_FAST_BORROW         4 (literal_ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               8 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               9 ('FAIL')

347   L4:     LOAD_CONST              10 ('Pending-call worker is OFF by default')

348           LOAD_FAST_BORROW         4 (literal_ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST              11 ('missing strict enable-literal constant')

344   L6:     LOAD_CONST              12 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

350           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1D40, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 353>:
353           RESUME                   0
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

Disassembly of <code object check_v34_sql at 0x0000018C17D8BD50, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 353>:
353            RESUME                   0

354            BUILD_LIST               0
               STORE_FAST               1 (out)

355            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('scripts')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('migrate_v34_api_key_one_time_reveal.sql')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

356            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               2 ('')
       L1:     STORE_FAST               3 (src)

357            LOAD_FAST_BORROW         3 (src)
               LOAD_ATTR                5 (lower + NULL|self)
               CALL                     0
               STORE_FAST               4 (lower)

358            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

359            LOAD_CONST               3 ('v34_sql:proposal_only')

360            LOAD_CONST               4 ('proposal only')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        3 (to L2)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L3)
       L2:     LOAD_CONST               6 ('FAIL')

361    L3:     LOAD_CONST               7 ("v34 SQL carries 'PROPOSAL ONLY' guardrail")

358            CALL                     3
               CALL                     1
               POP_TOP

363            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

364            LOAD_CONST               8 ('v34_sql:do_not_execute')

365            LOAD_CONST               9 ('do not execute')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L5)
       L4:     LOAD_CONST               6 ('FAIL')

366    L5:     LOAD_CONST              10 ("v34 SQL carries 'DO NOT EXECUTE' trailer")

363            CALL                     3
               CALL                     1
               POP_TOP

369            LOAD_CONST              11 ('ALTER TABLE pas_api_key_rotation_events')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (alter_ok)

370            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

371            LOAD_CONST              12 ('v34_sql:alter_v32_table')

372            LOAD_FAST_BORROW         5 (alter_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L6)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L7)
       L6:     LOAD_CONST               6 ('FAIL')

373    L7:     LOAD_CONST              13 ('v34 SQL ALTERs pas_api_key_rotation_events')

370            CALL                     3
               CALL                     1
               POP_TOP

377            LOAD_CONST              14 ('reveal_token_hash')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       32 (to L8)
               NOT_TAKEN
               POP_TOP

378            LOAD_CONST              15 ('reveal_token_expires_at')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

377            COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       19 (to L8)
               NOT_TAKEN
               POP_TOP

379            LOAD_CONST              16 ('revealed_at')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

377            COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

380            LOAD_CONST              17 ('reveal_attempt_count')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

376    L8:     STORE_FAST               6 (cols_ok)

382            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

383            LOAD_CONST              18 ('v34_sql:reveal_columns')

384            LOAD_FAST_BORROW         6 (cols_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L10)
       L9:     LOAD_CONST               6 ('FAIL')

385   L10:     LOAD_CONST              19 ('v34 SQL adds all four reveal columns')

382            CALL                     3
               CALL                     1
               POP_TOP

388            LOAD_CONST              20 ("'^[0-9a-f]{64}$'")
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               STORE_FAST               7 (sha_ok)

389            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

390            LOAD_CONST              21 ('v34_sql:sha256_pin')

391            LOAD_FAST_BORROW         7 (sha_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               6 ('FAIL')

392   L12:     LOAD_CONST              22 ('v34 SQL pins reveal_token_hash to sha256 hex shape')

389            CALL                     3
               CALL                     1
               POP_TOP

395            LOAD_CONST              23 ('revealed_at IS NULL')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               STORE_FAST               8 (onetime_ok)

396            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

397            LOAD_CONST              24 ('v34_sql:one_time_semantics')

398            LOAD_FAST_BORROW         8 (onetime_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L13)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L14)
      L13:     LOAD_CONST               6 ('FAIL')

399   L14:     LOAD_CONST              25 ('v34 SQL enforces one-time reveal via USING (revealed_at IS NULL)')

396            CALL                     3
               CALL                     1
               POP_TOP

401            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 404>:
404           RESUME                   0
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

Disassembly of <code object check_operator_auth_service at 0x0000018C17FEDE30, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 404>:
404           RESUME                   0

405           BUILD_LIST               0
              STORE_FAST               1 (out)

406           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('services')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('security')
              BINARY_OP               11 (/)
              LOAD_CONST               3 ('operator_auth.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

407           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

408           LOAD_GLOBAL              4 (REQUIRED_OPERATOR_AUTH_TOKENS)
              GET_ITER
      L2:     FOR_ITER                73 (to L7)
              STORE_FAST               4 (tok)

409           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

410           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

411           LOAD_CONST               5 ('operator_auth:')
              LOAD_FAST_BORROW         4 (tok)
              LOAD_CONST               6 (slice(None, 48, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

412           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               7 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               8 ('FAIL')

413   L4:     LOAD_CONST               9 ('operator_auth module exports ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

414           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             4 (to L6)
      L5:     LOAD_CONST              10 ('missing token ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

410   L6:     LOAD_CONST              11 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           75 (to L2)

408   L7:     END_FOR
              POP_ITER

416           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 419>:
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

Disassembly of <code object check_api_key_reveal_service at 0x0000018C181B05D0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 419>:
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
              LOAD_CONST               2 ('security')
              BINARY_OP               11 (/)
              LOAD_CONST               3 ('api_key_reveal.py')
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

423           LOAD_GLOBAL              4 (REQUIRED_REVEAL_TOKENS)
              GET_ITER
      L2:     FOR_ITER                73 (to L7)
              STORE_FAST               4 (tok)

424           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

425           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

426           LOAD_CONST               5 ('reveal_service:')
              LOAD_FAST_BORROW         4 (tok)
              LOAD_CONST               6 (slice(None, 48, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

427           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               7 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               8 ('FAIL')

428   L4:     LOAD_CONST               9 ('api_key_reveal module exports ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

429           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             4 (to L6)
      L5:     LOAD_CONST              10 ('missing token ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

425   L6:     LOAD_CONST              11 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           75 (to L2)

423   L7:     END_FOR
              POP_ITER

432           LOAD_CONST              12 ('raw_key_reveal_unsupported')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)
              STORE_FAST               6 (deferred_ok)

433           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

434           LOAD_CONST              13 ('reveal_service:deferred_raw_key')

435           LOAD_FAST_BORROW         6 (deferred_ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L8)
              NOT_TAKEN
              LOAD_CONST               7 ('PASS')
              JUMP_FORWARD             1 (to L9)
      L8:     LOAD_CONST               8 ('FAIL')

436   L9:     LOAD_CONST              14 ("api_key_reveal's raw-key path is deferred (raw_key_reveal_unsupported error code)")

433           CALL                     3
              CALL                     1
              POP_TOP

438           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 441>:
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

Disassembly of <code object check_https_enforcement_service at 0x0000018C17FEDC30, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 441>:
441           RESUME                   0

442           BUILD_LIST               0
              STORE_FAST               1 (out)

443           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('services')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('security')
              BINARY_OP               11 (/)
              LOAD_CONST               3 ('https_enforcement.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

444           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

445           LOAD_GLOBAL              4 (REQUIRED_HTTPS_TOKENS)
              GET_ITER
      L2:     FOR_ITER                73 (to L7)
              STORE_FAST               4 (tok)

446           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

447           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

448           LOAD_CONST               5 ('https_enforcement:')
              LOAD_FAST_BORROW         4 (tok)
              LOAD_CONST               6 (slice(None, 48, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

449           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               7 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               8 ('FAIL')

450   L4:     LOAD_CONST               9 ('https_enforcement module exports ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

451           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             4 (to L6)
      L5:     LOAD_CONST              10 ('missing token ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

447   L6:     LOAD_CONST              11 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           75 (to L2)

445   L7:     END_FOR
              POP_ITER

453           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA32D0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 456>:
456           RESUME                   0
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

Disassembly of <code object check_operator_route_rate_limit_wired at 0x0000018C17EC44A0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 456>:
456           RESUME                   0

459           BUILD_LIST               0
              STORE_FAST               1 (out)

460           LOAD_GLOBAL              0 (OPERATOR_ROUTE_FILES)
              GET_ITER
      L1:     FOR_ITER               142 (to L8)
              STORE_FAST               2 (relpath)

461           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (relpath)
              BINARY_OP               11 (/)
              STORE_FAST               3 (p)

462           LOAD_GLOBAL              5 (_read_text + NULL)
              LOAD_FAST_BORROW         3 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 ('')
      L2:     STORE_FAST               4 (src)

464           LOAD_CONST               2 ('check_rate_limit(')
              LOAD_FAST_BORROW         4 (src)
              CONTAINS_OP              0 (in)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       32 (to L3)
              NOT_TAKEN
              POP_TOP

465           LOAD_CONST               3 ('surface="admin"')
              LOAD_FAST_BORROW         4 (src)
              CONTAINS_OP              0 (in)

464           COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       19 (to L3)
              NOT_TAKEN
              POP_TOP

466           LOAD_CONST               4 ('actor_type="ADMIN"')
              LOAD_FAST_BORROW         4 (src)
              CONTAINS_OP              0 (in)

464           COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE        6 (to L3)
              NOT_TAKEN
              POP_TOP

467           LOAD_CONST               5 ('status_code=429')
              LOAD_FAST_BORROW         4 (src)
              CONTAINS_OP              0 (in)

463   L3:     STORE_FAST               5 (ok)

469           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

470           LOAD_CONST               6 ('operator_route_rate_limit:')
              LOAD_FAST_BORROW         2 (relpath)
              FORMAT_SIMPLE
              BUILD_STRING             2

471           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               7 ('PASS')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               8 ('FAIL')

472   L5:     LOAD_FAST_BORROW         2 (relpath)
              FORMAT_SIMPLE
              LOAD_CONST               9 (' wires operator/admin rate-limit')
              BUILD_STRING             2

473           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L6)
              NOT_TAKEN
              LOAD_CONST               1 ('')
              JUMP_FORWARD             1 (to L7)
      L6:     LOAD_CONST              10 ('missing required rate-limit wiring')

469   L7:     LOAD_CONST              11 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD          144 (to L1)

460   L8:     END_FOR
              POP_ITER

475           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 478>:
478           RESUME                   0
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

Disassembly of <code object check_reveal_route_present at 0x0000018C17ECEDB0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 478>:
478           RESUME                   0

479           BUILD_LIST               0
              STORE_FAST               1 (out)

480           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('routes')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('security_api_key_rotation.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

481           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               3 ('')
      L1:     STORE_FAST               3 (src)

483           LOAD_CONST               4 ('/rotation/{rotation_id}/reveal')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       19 (to L2)
              NOT_TAKEN
              POP_TOP

484           LOAD_CONST               5 ('tenant_rotation_reveal_route')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)

483           COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE        6 (to L2)
              NOT_TAKEN
              POP_TOP

485           LOAD_CONST               6 ('reveal_rotated_api_key_once')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)

482   L2:     STORE_FAST               4 (ok)

487           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

488           LOAD_CONST               7 ('reveal_route:tenant_get_reveal')

489           LOAD_FAST_BORROW         4 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               8 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               9 ('FAIL')

490   L4:     LOAD_CONST              10 ('Tenant GET /tenant/api-key/rotation/{id}/reveal route wired')

491           LOAD_FAST_BORROW         4 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               3 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST              11 ('missing reveal route or handler')

487   L6:     LOAD_CONST              12 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

495           LOAD_CONST              13 ('raw_api_key_value')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (raw_key_present)

496           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

497           LOAD_CONST              14 ('reveal_route:no_raw_key_value')

498           LOAD_FAST_BORROW         5 (raw_key_present)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L7)
              NOT_TAKEN
              LOAD_CONST               9 ('FAIL')
              JUMP_FORWARD             1 (to L8)
      L7:     LOAD_CONST               8 ('PASS')

499   L8:     LOAD_CONST              15 ('Reveal route does NOT reference a raw_api_key_value variable')

496           CALL                     3
              CALL                     1
              POP_TOP

501           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 504>:
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

Disassembly of <code object check_severity_scanner at 0x0000018C17FEE430, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 504>:
504           RESUME                   0

505           BUILD_LIST               0
              STORE_FAST               1 (out)

506           LOAD_GLOBAL              1 (Path + NULL)
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

507           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

508           LOAD_CONST              12 (('ALLOWED_SEVERITY_TIERS', 'def _classify_severity(', 'def _cvss_to_tier(', 'def _label_to_tier(', 'severities'))
              STORE_FAST               4 (ok_tokens)

515           LOAD_FAST_BORROW         4 (ok_tokens)
              GET_ITER
      L2:     FOR_ITER                73 (to L7)
              STORE_FAST               5 (tok)

516           LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               6 (ok)

517           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

518           LOAD_CONST               5 ('severity_scanner:')
              LOAD_FAST_BORROW         5 (tok)
              LOAD_CONST               6 (slice(None, 48, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

519           LOAD_FAST_BORROW         6 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               7 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               8 ('FAIL')

520   L4:     LOAD_CONST               9 ('dependency_scanner exports ')
              LOAD_FAST_BORROW         5 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

521           LOAD_FAST_BORROW         6 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             4 (to L6)
      L5:     LOAD_CONST              10 ('missing token ')
              LOAD_FAST_BORROW         5 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

517   L6:     LOAD_CONST              11 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           75 (to L2)

515   L7:     END_FOR
              POP_ITER

523           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 526>:
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

Disassembly of <code object check_ci_gate_severity_flags at 0x0000018C17EE1CC0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 526>:
526            RESUME                   0

527            BUILD_LIST               0
               STORE_FAST               1 (out)

528            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('scripts')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('security_ci_dependency_gate.py')
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
               LOAD_CONST               2 ('')
       L1:     STORE_FAST               3 (src)

530            LOAD_CONST              14 (('--fail-on-medium', '--fail-on-high', '--fail-on-critical', 'severities', 'UNKNOWN'))
               STORE_FAST               4 (ok_tokens)

537            LOAD_FAST_BORROW         4 (ok_tokens)
               GET_ITER
       L2:     FOR_ITER                73 (to L7)
               STORE_FAST               5 (tok)

538            LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               6 (ok)

539            LOAD_FAST                1 (out)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_GLOBAL              7 (_check + NULL)

540            LOAD_CONST               3 ('ci_gate:')
               LOAD_FAST_BORROW         5 (tok)
               LOAD_CONST               4 (slice(None, 48, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

541            LOAD_FAST_BORROW         6 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               6 ('FAIL')

542    L4:     LOAD_CONST               7 ('security_ci_dependency_gate exports ')
               LOAD_FAST_BORROW         5 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

543            LOAD_FAST_BORROW         6 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST               8 ('missing token ')
               LOAD_FAST_BORROW         5 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

539    L6:     LOAD_CONST               9 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           75 (to L2)

537    L7:     END_FOR
               POP_ITER

546            LOAD_GLOBAL              9 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               7 (executable)

547            BUILD_LIST               0
               STORE_FAST               8 (bad)

548            LOAD_GLOBAL             10 (FORBIDDEN_AUTO_FIX_TOKENS)
               GET_ITER
       L8:     FOR_ITER                57 (to L10)
               STORE_FAST               5 (tok)

549            LOAD_FAST_BORROW         5 (tok)
               LOAD_ATTR               13 (lower + NULL|self)
               CALL                     0
               LOAD_FAST_BORROW         7 (executable)
               LOAD_ATTR               13 (lower + NULL|self)
               CALL                     0
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L9)
               NOT_TAKEN
               JUMP_BACKWARD           40 (to L8)

550    L9:     LOAD_FAST_BORROW         8 (bad)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_FAST_BORROW         5 (tok)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           59 (to L8)

548   L10:     END_FOR
               POP_ITER

551            LOAD_FAST                1 (out)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_GLOBAL              7 (_check + NULL)

552            LOAD_CONST              10 ('ci_gate:no_auto_fix')

553            LOAD_FAST_BORROW         8 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               6 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               5 ('PASS')

554   L12:     LOAD_CONST              11 ('CI gate has no auto-fix tokens in executable form')

555            LOAD_FAST_BORROW         8 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L13)
               NOT_TAKEN
               LOAD_CONST              12 ('disqualifying tokens: ')
               LOAD_CONST              13 (', ')
               LOAD_ATTR               15 (join + NULL|self)
               LOAD_FAST_BORROW         8 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L14)
      L13:     LOAD_CONST               2 ('')

551   L14:     LOAD_CONST               9 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

557            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 560>:
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

Disassembly of <code object check_https_middleware at 0x0000018C181287B0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 560>:
560           RESUME                   0

561           BUILD_LIST               0
              STORE_FAST               1 (out)

562           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('main.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

563           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               2 ('')
      L1:     STORE_FAST               3 (src)

565           LOAD_CONST               3 ('HTTPSEnforcementMiddleware')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       19 (to L2)
              NOT_TAKEN
              POP_TOP

566           LOAD_CONST               4 ('add_middleware(HTTPSEnforcementMiddleware')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)

565           COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE        6 (to L2)
              NOT_TAKEN
              POP_TOP

567           LOAD_CONST               5 ('should_reject_insecure_request')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)

564   L2:     STORE_FAST               4 (ok)

569           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

570           LOAD_CONST               6 ('main:https_middleware')

571           LOAD_FAST_BORROW         4 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               7 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               8 ('FAIL')

572   L4:     LOAD_CONST               9 ('app/main.py registers HTTPSEnforcementMiddleware')

573           LOAD_FAST_BORROW         4 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               2 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST              10 ('missing HTTPS middleware wiring')

569   L6:     LOAD_CONST              11 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

575           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA26A0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 578>:
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

Disassembly of <code object check_no_raw_key_storage_or_echo at 0x0000018C17CC2E60, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 578>:
578            RESUME                   0

581            BUILD_LIST               0
               STORE_FAST               1 (out)

582            LOAD_CONST               9 (('app/services/security/operator_auth.py', 'app/services/security/api_key_reveal.py', 'app/services/security/https_enforcement.py', 'scripts/pas_security_04_operator_reveal_https_readiness_check.py'))
               STORE_FAST               2 (files)

588            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               195 (to L11)
               STORE_FAST               3 (relpath)

589            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

590            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

591            JUMP_BACKWARD           45 (to L1)

592    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

593            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         5 (src)
               CALL                     1
               STORE_FAST               6 (executable)

594            BUILD_LIST               0
               STORE_FAST               7 (bad)

595            LOAD_GLOBAL              8 (FORBIDDEN_RAW_KEY_TOKENS)
               GET_ITER
       L4:     FOR_ITER                28 (to L6)
               STORE_FAST               8 (tok)

596            LOAD_FAST_BORROW_LOAD_FAST_BORROW 134 (tok, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L4)

597    L5:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_FAST_BORROW         8 (tok)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L4)

595    L6:     END_FOR
               POP_ITER

598            LOAD_FAST                1 (out)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_GLOBAL             13 (_check + NULL)

599            LOAD_CONST               2 ('no_raw_key_or_token:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

600            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L7)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L8)
       L7:     LOAD_CONST               4 ('PASS')

601    L8:     LOAD_CONST               5 ('No raw_api_key_value / raw_reveal_token / user_agent_raw in executable: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

602            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L9)
               NOT_TAKEN
               LOAD_CONST               6 ('disqualifying tokens: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               15 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L10)
       L9:     LOAD_CONST               1 ('')

598   L10:     LOAD_CONST               8 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          197 (to L1)

588   L11:     END_FOR
               POP_ITER

604            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA22E0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 607>:
607           RESUME                   0
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

Disassembly of <code object check_audit_service_invariant at 0x0000018C182DCD60, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 607>:
607           RESUME                   0

608           BUILD_LIST               0
              STORE_FAST               1 (out)

609           LOAD_GLOBAL              1 (Path + NULL)
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

610           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

611           LOAD_CONST              12 (('def update_audit_', 'def delete_audit_', 'def update_operator_audit_', 'def delete_operator_audit_', 'def mutate_audit_', 'def truncate_audit_'))
              STORE_FAST               4 (forbidden)

619           BUILD_LIST               0
              STORE_FAST               5 (bad)

620           LOAD_FAST_BORROW         4 (forbidden)
              GET_ITER
      L2:     FOR_ITER                28 (to L4)
              STORE_FAST               6 (tok)

621           LOAD_FAST_BORROW_LOAD_FAST_BORROW 99 (tok, src)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

622   L3:     LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_FAST_BORROW         6 (tok)
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           30 (to L2)

620   L4:     END_FOR
              POP_ITER

623           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

624           LOAD_CONST               5 ('audit_service:append_only_carry')

625           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               6 ('FAIL')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               7 ('PASS')

626   L6:     LOAD_CONST               8 ('Audit service still has no UPDATE / DELETE mutation helpers (carry-forward invariant)')

627           LOAD_FAST_BORROW         5 (bad)
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

623   L8:     LOAD_CONST              11 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

629           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA24C0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 632>:
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

Disassembly of <code object check_event_contract at 0x0000018C179A7290, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 632>:
632           RESUME                   0

633           BUILD_LIST               0
              STORE_FAST               1 (out)

634           LOAD_GLOBAL              1 (Path + NULL)
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

635           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

636           LOAD_GLOBAL              4 (REQUIRED_EVENT_TYPES)
              GET_ITER
      L2:     FOR_ITER                67 (to L7)
              STORE_FAST               4 (required)

637           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (required, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

638           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

639           LOAD_CONST               5 ('events:')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

640           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               6 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               7 ('FAIL')

641   L4:     LOAD_CONST               8 ('Event contract registers ')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

642           LOAD_FAST_BORROW         5 (ok)
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

638   L6:     LOAD_CONST              10 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           69 (to L2)

636   L7:     END_FOR
              POP_ITER

644           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA25B0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 647>:
647           RESUME                   0
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

Disassembly of <code object check_no_forbidden_imports at 0x0000018C17EA53C0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 647>:
647            RESUME                   0

648            BUILD_LIST               0
               STORE_FAST               1 (out)

649            LOAD_CONST              10 (('app/services/security/operator_auth.py', 'app/services/security/api_key_reveal.py', 'app/services/security/https_enforcement.py', 'scripts/pas_security_04_operator_reveal_https_readiness_check.py'))
               STORE_FAST               2 (files)

655            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     EXTENDED_ARG             1
               FOR_ITER               292 (to L15)
               STORE_FAST               3 (relpath)

656            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

657            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

658            JUMP_BACKWARD           46 (to L1)

659    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

660            BUILD_LIST               0
               STORE_FAST               6 (bad)

661            LOAD_FAST_BORROW         5 (src)
               LOAD_ATTR                7 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L4:     FOR_ITER               107 (to L10)
               STORE_FAST               7 (line)

662            LOAD_FAST_BORROW         7 (line)
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               STORE_FAST               8 (stripped)

663            LOAD_FAST_BORROW         8 (stripped)
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

664    L5:     JUMP_BACKWARD           52 (to L4)

665    L6:     LOAD_GLOBAL             12 (FORBIDDEN_IMPORT_LINE_PREFIXES)
               GET_ITER
       L7:     FOR_ITER                45 (to L9)
               STORE_FAST               9 (prefix)

666            LOAD_FAST_BORROW         8 (stripped)
               LOAD_ATTR               11 (startswith + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD           28 (to L7)

667    L8:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           47 (to L7)

665    L9:     END_FOR
               POP_ITER
               JUMP_BACKWARD          109 (to L4)

661   L10:     END_FOR
               POP_ITER

668            LOAD_FAST                1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             17 (_check + NULL)

669            LOAD_CONST               3 ('forbidden_import:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

670            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               4 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               5 ('PASS')

671   L12:     LOAD_CONST               6 ('No forbidden imports: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

673            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       43 (to L13)
               NOT_TAKEN

672            LOAD_CONST               7 ('forbidden import prefixes: ')
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

673   L13:     LOAD_CONST               1 ('')

668   L14:     LOAD_CONST               9 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          295 (to L1)

655   L15:     END_FOR
               POP_ITER

675            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 678>:
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

Disassembly of <code object check_no_inbox_scan_tokens at 0x0000018C17CC1CE0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 678>:
678            RESUME                   0

679            BUILD_LIST               0
               STORE_FAST               1 (out)

680            LOAD_CONST               9 (('app/services/security/operator_auth.py', 'app/services/security/api_key_reveal.py', 'app/services/security/https_enforcement.py'))
               STORE_FAST               2 (files)

685            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               195 (to L11)
               STORE_FAST               3 (relpath)

686            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

687            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

688            JUMP_BACKWARD           45 (to L1)

689    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

690            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         5 (src)
               CALL                     1
               STORE_FAST               6 (executable)

691            BUILD_LIST               0
               STORE_FAST               7 (bad)

692            LOAD_GLOBAL              8 (FORBIDDEN_INBOX_TOKENS)
               GET_ITER
       L4:     FOR_ITER                28 (to L6)
               STORE_FAST               8 (token)

693            LOAD_FAST_BORROW_LOAD_FAST_BORROW 134 (token, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L4)

694    L5:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_FAST_BORROW         8 (token)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L4)

692    L6:     END_FOR
               POP_ITER

695            LOAD_FAST                1 (out)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_GLOBAL             13 (_check + NULL)

696            LOAD_CONST               2 ('no_inbox_scan:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

697            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L7)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L8)
       L7:     LOAD_CONST               4 ('PASS')

698    L8:     LOAD_CONST               5 ('No inbox-scanning tokens: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

700            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L9)
               NOT_TAKEN

699            LOAD_CONST               6 ('inbox-scan tokens present: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               15 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L10)

700    L9:     LOAD_CONST               1 ('')

695   L10:     LOAD_CONST               8 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          197 (to L1)

685   L11:     END_FOR
               POP_ITER

702            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 705>:
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

Disassembly of <code object check_process_local_fallback_carry_forward at 0x0000018C18060C00, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 705>:
705           RESUME                   0

706           BUILD_LIST               0
              STORE_FAST               1 (out)

707           LOAD_GLOBAL              1 (Path + NULL)
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

708           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

709           LOAD_CONST               5 ('rate_limit_store_process_local')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)
              STORE_FAST               4 (ok)

710           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

711           LOAD_CONST               6 ('carry_forward:process_local_fallback')

712           LOAD_FAST_BORROW         4 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               7 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               8 ('FAIL')

713   L3:     LOAD_CONST               9 ('PAS-SECURITY-02 process-local fallback marker still present')

710           CALL                     3
              CALL                     1
              POP_TOP

715           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181153E0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 718>:
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

Disassembly of <code object check_doc_required_clauses at 0x0000018C17CD0CE0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 718>:
  --            MAKE_CELL                8 (lower)

 718            RESUME                   0

 719            BUILD_LIST               0
                STORE_FAST               1 (out)

 720            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('docs')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('pas_security_04_operator_reveal_https.md')
                BINARY_OP               11 (/)
                STORE_FAST               2 (doc)

 721            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (doc)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L1:     STORE_FAST               3 (src)

 722            LOAD_FAST_BORROW         3 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_DEREF              8 (lower)

 723            LOAD_CONST              13 ((('purpose', ('purpose',)), ('pas-security-01-02-03', ('relationship to pas-security-01',)), ('operator-auth', ('operator auth consolidation doctrine', 'operator auth consolidation')), ('operator-rate-limit', ('operator rate-limit doctrine', 'operator rate-limit')), ('one-time-reveal', ('one-time reveal doctrine', 'one-time reveal')), ('unsupported-reveal', ('unsupported reveal fallback', 'deferred raw-key', 'deferred')), ('severity-ci', ('severity-aware ci doctrine', 'severity-aware ci')), ('https-enforcement', ('https enforcement doctrine', 'https enforcement')), ('proxy-header-trust', ('proxy / header trust doctrine', 'proxy / header', 'header trust doctrine')), ('limitations', ('remaining limitations', 'limitation')), ('not-built', ('intentionally does not', 'intentionally not build', 'deliberately not')), ('no-gmail', ('no gmail',)), ('no-autonomous', ('no autonomous remediation', 'no autonomous'))))
                STORE_FAST               4 (required_phrases)

 751            LOAD_FAST_BORROW         4 (required_phrases)
                GET_ITER
        L2:     FOR_ITER               141 (to L12)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   86 (name, phrases)

 752            LOAD_GLOBAL              6 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         8 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18025130, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 752>)
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
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18025130, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 752>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         6 (phrases)
                GET_ITER
                CALL                     0
                CALL                     1
        L7:     STORE_FAST               7 (present)

 753            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 754            LOAD_CONST               6 ('docs:pas_security_04:')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 755            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               8 ('FAIL')

 756    L9:     LOAD_CONST               9 ('PAS-SECURITY-04 doctrine carries clause: ')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 758            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L10)
                NOT_TAKEN

 757            LOAD_CONST              10 ('expected one of: ')
                LOAD_CONST              11 (' | ')
                LOAD_ATTR               13 (join + NULL|self)
                LOAD_FAST_BORROW         6 (phrases)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L11)

 758   L10:     LOAD_CONST               2 ('')

 753   L11:     LOAD_CONST              12 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          143 (to L2)

 751   L12:     END_FOR
                POP_ITER

 760            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18025130, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 752>:
  --           COPY_FREE_VARS           1

 752           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C181154D0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 763>:
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

Disassembly of <code object check_self_no_env_or_db at 0x0000018C17D884E0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 763>:
763            RESUME                   0

764            BUILD_LIST               0
               STORE_FAST               1 (out)

765            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_GLOBAL              2 (__file__)
               CALL                     1
               LOAD_ATTR                5 (resolve + NULL|self)
               CALL                     0
               STORE_FAST               2 (self_path)

766            LOAD_GLOBAL              7 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (self_path)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L1:     STORE_FAST               3 (src)

767            LOAD_GLOBAL              9 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               4 (executable)

768            BUILD_LIST               0
               STORE_FAST               5 (bad)

769            LOAD_FAST_BORROW         4 (executable)
               LOAD_ATTR               11 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L2:     FOR_ITER               199 (to L9)
               STORE_FAST               6 (raw_line)

770            LOAD_FAST_BORROW         6 (raw_line)
               LOAD_ATTR               13 (strip + NULL|self)
               CALL                     0
               STORE_FAST               7 (stripped)

771            LOAD_FAST_BORROW         7 (stripped)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN

772            JUMP_BACKWARD           29 (to L2)

773    L3:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              15 (('import dotenv', 'from dotenv'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L4)
               NOT_TAKEN

774            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               1 ('dotenv import')
               CALL                     1
               POP_TOP

775    L4:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              16 (('import supabase', 'from supabase'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L5)
               NOT_TAKEN

776            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               2 ('supabase import')
               CALL                     1
               POP_TOP

777    L5:     LOAD_CONST               3 ('load_dotenv()')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       18 (to L6)
               NOT_TAKEN

778            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               4 ('load_dotenv() call')
               CALL                     1
               POP_TOP

779    L6:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              17 (('os.environ[', 'getenv('))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L7)
               NOT_TAKEN

780            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               5 ('environ read')
               CALL                     1
               POP_TOP

781    L7:     LOAD_CONST               6 ('get_supabase')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD          182 (to L2)

782    L8:     LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               7 ('supabase client call')
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          201 (to L2)

769    L9:     END_FOR
               POP_ITER

783            LOAD_FAST                1 (out)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_GLOBAL             19 (_check + NULL)

784            LOAD_CONST               8 ('self_check:no_env_or_db')

785            LOAD_FAST_BORROW         5 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST               9 ('FAIL')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST              10 ('PASS')

786   L11:     LOAD_CONST              11 ('PAS-SECURITY-04 readiness checker never reads .env / touches DB')

787            LOAD_FAST_BORROW         5 (bad)
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

783   L13:     LOAD_CONST              14 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

789            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181155C0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 796>:
796           RESUME                   0
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

Disassembly of <code object _aggregate at 0x0000018C1800B0A0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 796>:
 796            RESUME                   0

 798            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 797            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2

 798    L2:     FOR_ITER                49 (to L7)
                STORE_FAST               1 (c)

 799            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 798    L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L2)

 799    L4:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              2 (SEVERITY_BLOCK)
                COMPARE_OP              88 (bool(==))

 798    L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L2)
        L6:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L2)
        L7:     END_FOR
                POP_ITER

 797    L8:     STORE_FAST               2 (blockers)
                STORE_FAST               1 (c)

 802            LOAD_CONST               3 ('verdict')
                LOAD_FAST_BORROW         2 (blockers)
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L9)
                NOT_TAKEN
                LOAD_GLOBAL              4 (VERDICT_NOT_READY)
                JUMP_FORWARD             5 (to L10)
        L9:     LOAD_GLOBAL              6 (VERDICT_READY)

 803   L10:     LOAD_CONST               4 ('blockers')
                LOAD_FAST_BORROW         2 (blockers)

 804            LOAD_CONST               5 ('info')
                BUILD_LIST               0

 801            BUILD_MAP                3
                RETURN_VALUE

  --   L11:     SWAP                     2
                POP_TOP

 797            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L11 [2]
  L4 to L5 -> L11 [2]
  L6 to L8 -> L11 [2]

Disassembly of <code object __annotate__ at 0x0000018C18115980, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 808>:
808           RESUME                   0
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

Disassembly of <code object _operator_actions at 0x0000018C18048AB0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 808>:
808           RESUME                   0

809           BUILD_LIST               0
              STORE_FAST               1 (out)

810           LOAD_FAST_BORROW         0 (checks)
              GET_ITER
      L1:     FOR_ITER               109 (to L5)
              STORE_FAST               2 (c)

811           LOAD_FAST_BORROW         2 (c)
              LOAD_CONST               0 ('status')
              BINARY_OP               26 ([])
              LOAD_CONST               1 ('FAIL')
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

812           JUMP_BACKWARD           19 (to L1)

813   L2:     LOAD_FAST_BORROW         2 (c)
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

814           LOAD_FAST                1 (out)
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

810   L5:     END_FOR
              POP_ITER

815           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18115A70, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 818>:
818           RESUME                   0
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

Disassembly of <code object evaluate at 0x0000018C177C63A0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 818>:
818           RESUME                   0

819           BUILD_LIST               0
              STORE_FAST               1 (checks)

820           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              3 (check_files_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

821           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              5 (check_prior_phases_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

822           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              7 (check_memory_review_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

823           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              9 (check_worker_off_by_default + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

824           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             11 (check_v34_sql + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

825           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             13 (check_operator_auth_service + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

826           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             15 (check_api_key_reveal_service + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

827           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             17 (check_https_enforcement_service + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

828           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             19 (check_operator_route_rate_limit_wired + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

829           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             21 (check_reveal_route_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

830           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             23 (check_severity_scanner + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

831           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             25 (check_ci_gate_severity_flags + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

832           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             27 (check_https_middleware + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

833           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             29 (check_no_raw_key_storage_or_echo + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

834           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             31 (check_audit_service_invariant + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

835           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             33 (check_event_contract + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

836           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             35 (check_no_forbidden_imports + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

837           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             37 (check_no_inbox_scan_tokens + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

838           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             39 (check_process_local_fallback_carry_forward + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

839           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             41 (check_doc_required_clauses + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

840           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             43 (check_self_no_env_or_db + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

842           LOAD_GLOBAL             45 (_aggregate + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1
              STORE_FAST               2 (agg)

844           LOAD_CONST               0 ('phase')
              LOAD_CONST               1 ('PAS-SECURITY-04')

845           LOAD_CONST               2 ('generated_at')
              LOAD_GLOBAL             47 (_now_iso + NULL)
              CALL                     0

846           LOAD_CONST               3 ('verdict')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])

847           LOAD_CONST               4 ('ready')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])
              LOAD_GLOBAL             48 (VERDICT_READY)
              COMPARE_OP              72 (==)

848           LOAD_CONST               5 ('blocker_count')
              LOAD_GLOBAL             51 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               6 ('blockers')
              BINARY_OP               26 ([])
              CALL                     1

849           LOAD_CONST               7 ('info_count')
              LOAD_GLOBAL             51 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               8 ('info')
              BINARY_OP               26 ([])
              CALL                     1

850           LOAD_CONST               9 ('check_count')
              LOAD_GLOBAL             51 (len + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

851           LOAD_CONST              10 ('pass_count')
              LOAD_GLOBAL             53 (sum + NULL)
              LOAD_CONST              11 (<code object <genexpr> at 0x0000018C18053750, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 851>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

852           LOAD_CONST              12 ('fail_count')
              LOAD_GLOBAL             53 (sum + NULL)
              LOAD_CONST              13 (<code object <genexpr> at 0x0000018C18053E10, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 852>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

853           LOAD_CONST              14 ('checks')
              LOAD_FAST_BORROW         1 (checks)

854           LOAD_CONST              15 ('operator_actions')
              LOAD_GLOBAL             55 (_operator_actions + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

843           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18053750, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 851>:
 851           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C18053E10, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 852>:
 852           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C18115110, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 861>:
861           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C181283F0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 861>:
861           RESUME                   0

862           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

863           LOAD_CONST               0 ('pas_security_04_operator_reveal_https_readiness_check')

865           LOAD_CONST               1 ('PAS-SECURITY-04 — Evaluate operator-route consolidation + one-time API-key reveal + severity-aware CI gate + HTTPS enforcement. Read-only — never reads .env, never touches Supabase, never runs a migration.')

862           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

872           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               3 ('--repo-root')
              LOAD_GLOBAL              6 (_REPO_ROOT_DEFAULT)
              LOAD_CONST               4 (('default',))
              CALL_KW                  2
              POP_TOP

873           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               5 ('--output')
              LOAD_GLOBAL              8 (REPORT_FILENAME)
              LOAD_CONST               4 (('default',))
              CALL_KW                  2
              POP_TOP

874           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               6 ('--json')
              LOAD_CONST               7 ('store_true')
              LOAD_CONST               8 (('action',))
              CALL_KW                  2
              POP_TOP

875           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               9 ('--summary-only')
              LOAD_CONST               7 ('store_true')
              LOAD_CONST               8 (('action',))
              CALL_KW                  2
              POP_TOP

876           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST              10 ('--strict')
              LOAD_CONST               7 ('store_true')
              LOAD_CONST               8 (('action',))
              CALL_KW                  2
              POP_TOP

877           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18115D40, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 880>:
880           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C17D8C5C0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 880>:
880           RESUME                   0

881           LOAD_GLOBAL              1 (print + NULL)

882           LOAD_CONST               0 ('[PAS-SECURITY-04] verdict=')
              LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               1 ('verdict')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               2 (' blockers=')

883           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               3 ('blocker_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' info=')

884           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               5 ('info_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' checks=')

885           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               7 ('check_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' pass=')

886           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               9 ('pass_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              10 (' fail=')

887           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              11 ('fail_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE

882           BUILD_STRING            12

881           CALL                     1
              POP_TOP

889           LOAD_FAST_BORROW         0 (report)
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

890           LOAD_FAST_BORROW         1 (actions)
              TO_BOOL
              POP_JUMP_IF_FALSE       93 (to L5)
              NOT_TAKEN

891           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              13 ('[PAS-SECURITY-04] operator actions:')
              CALL                     1
              POP_TOP

892           LOAD_FAST_BORROW         1 (actions)
              LOAD_CONST              14 (slice(None, 25, None))
              BINARY_OP               26 ([])
              GET_ITER
      L2:     FOR_ITER                17 (to L3)
              STORE_FAST               2 (a)

893           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              15 ('  - ')
              LOAD_FAST_BORROW         2 (a)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L2)

892   L3:     END_FOR
              POP_ITER

894           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         1 (actions)
              CALL                     1
              LOAD_SMALL_INT          25
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       34 (to L4)
              NOT_TAKEN

895           LOAD_GLOBAL              1 (print + NULL)
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

894   L4:     LOAD_CONST              18 (None)
              RETURN_VALUE

890   L5:     LOAD_CONST              18 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024930, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 898>:
898           RESUME                   0
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

Disassembly of <code object _write_report at 0x0000018C18128D50, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 898>:
 898           RESUME                   0

 899           NOP

 900   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

 901           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

 902           LOAD_CONST               3 ('utf-8')

 900           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 904           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

 905   L4:     LOAD_GLOBAL             11 (print + NULL)

 906           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

 907           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

 906           BUILD_STRING             4

 908           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

 905           LOAD_CONST               7 (('file',))
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

 904   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C181157A0, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 912>:
912           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17D88890, file "scripts/pas_security_04_operator_reveal_https_readiness_check.py", line 912>:
 912            RESUME                   0

 913            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 914            NOP

 915    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 919    L2:     LOAD_GLOBAL             10 (os)
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

 920            LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               21 (isdir + NULL|self)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L4)
                NOT_TAKEN

 921            LOAD_GLOBAL             23 (print + NULL)
                LOAD_CONST               2 ('error: --repo-root not a directory: ')
                LOAD_FAST                4 (repo_root)
                FORMAT_SIMPLE
                BUILD_STRING             2
                LOAD_GLOBAL             24 (sys)
                LOAD_ATTR               26 (stderr)
                LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

 922            LOAD_SMALL_INT           2
                RETURN_VALUE

 924    L4:     LOAD_GLOBAL             29 (evaluate + NULL)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                STORE_FAST               5 (report)

 926            LOAD_FAST                2 (args)
                LOAD_ATTR               30 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L5)
                NOT_TAKEN

 927            LOAD_GLOBAL             33 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               34 (output)
                LOAD_FAST                5 (report)
                CALL                     2
                POP_TOP

 929    L5:     LOAD_GLOBAL             37 (_print_summary + NULL)
                LOAD_FAST                5 (report)
                CALL                     1
                POP_TOP

 931            LOAD_FAST                2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L6)
                NOT_TAKEN

 932            LOAD_GLOBAL             23 (print + NULL)
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

 934    L6:     LOAD_FAST                5 (report)
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

 916            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L17)
                NOT_TAKEN
                STORE_FAST               3 (e)

 917    L9:     LOAD_FAST                3 (e)
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

 916   L17:     RERAISE                  0

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
