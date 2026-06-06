# scripts_readiness/pas_security_03_admin_webhook_ci_readiness_check

- **pyc:** `scripts\__pycache__\pas_security_03_admin_webhook_ci_readiness_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/pas_security_03_admin_webhook_ci_readiness_check.py`
- **co_filename (from bytecode):** `scripts/pas_security_03_admin_webhook_ci_readiness_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS-SECURITY-03 — Admin / webhook rate-limit + atomic counter
+ CI scanner gate readiness check.

Deterministic, non-mutating evaluator for "is PAS-SECURITY-03
wired correctly and free of regressions in the
PAS160-PAS-SECURITY-02 doctrine?".

Walks the repo and verifies:

  * PAS160-PAS181 + PAS-SECURITY-01/02 readiness scripts still
    exist.
  * PAS-SECURITY-03 surfaces exist:
      - scripts/migrate_v33_rate_limit_atomic_rpc.sql
      - app/services/security/rate_limit_rpc.py
      - scripts/security_ci_dependency_gate.py
      - scripts/pas_security_03_admin_webhook_ci_readiness_check.py
      - docs/pas_security_03_admin_webhook_ci_gate.md
      - docs/pas_waf_boundary_security_baseline.md
      - docs/pas_api_key_delivery_doctrine.md
      - tests/mvp/test_pas_security_03_admin_webhook_ci.py
  * v33 SQL: PROPOSAL ONLY, ON CONFLICT DO UPDATE, SECURITY
    DEFINER, tenant/anon REVOKE EXECUTE, service_role GRANT
    EXECUTE.
  * rate_limit_rpc service surface tokens present + fallback
    warning marker.
  * Admin route rate-limit wired in app/routes/admin.py's
    require_admin.
  * Webhook route rate-limit wired in app/routes/lead_ingestion.py's
    _ingest helper.
  * CI dependency gate exists; no auto-fix in executable form.
  * API key delivery doctrine doc + WAF baseline doc exist.
  * No raw API key storage in PAS-SECURITY-03 surfaces.
  * No token / signature echo.
  * No auto dependency fix.
  * Process-local fallback warning still exists (carry-forward).
  * No Gmail / OAuth / IMAP / POP3 / Composio / TrustClaw /
    embeddings / vector / LLM imports.
  * Memory Review (PAS147-PAS158) untouched.
  * audit_service still has no UPDATE / DELETE helpers.
  * Event contract registers PAS-SECURITY-03 events.
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

`__annotate__`, `_aggregate`, `_build_parser`, `_check`, `_now_iso`, `_operator_actions`, `_print_summary`, `_read_text`, `_strip_python_comments_and_strings`, `_write_report`, `check_admin_rate_limit_wired`, `check_audit_service_invariant`, `check_ci_gate_script`, `check_event_contract`, `check_files_present`, `check_key_delivery_doctrine_doc`, `check_memory_review_intact`, `check_no_forbidden_imports`, `check_no_inbox_scan_tokens`, `check_no_raw_key_storage`, `check_pas_security_02_carry_forward`, `check_pas_security_03_doctrine_doc`, `check_prior_phases_intact`, `check_rpc_service`, `check_self_no_env_or_db`, `check_v33_sql`, `check_waf_baseline_doc`, `check_webhook_rate_limit_wired`, `check_worker_off_by_default`, `evaluate`, `main`

## Env-key candidates

`BLOCK`, `FAIL`, `INFO`, `NOT_READY`, `PASS`, `READY`

## String constants (redacted where noted)

- '\nPAS-SECURITY-03 — Admin / webhook rate-limit + atomic counter\n+ CI scanner gate readiness check.\n\nDeterministic, non-mutating evaluator for "is PAS-SECURITY-03\nwired correctly and free of regressions in the\nPAS160-PAS-SECURITY-02 doctrine?".\n\nWalks the repo and verifies:\n\n  * PAS160-PAS181 + PAS-SECURITY-01/02 readiness scripts still\n    exist.\n  * PAS-SECURITY-03 surfaces exist:\n      - scripts/migrate_v33_rate_limit_atomic_rpc.sql\n      - app/services/security/rate_limit_rpc.py\n      - scripts/security_ci_dependency_gate.py\n      - scripts/pas_security_03_admin_webhook_ci_readiness_check.py\n      - docs/pas_security_03_admin_webhook_ci_gate.md\n      - docs/pas_waf_boundary_security_baseline.md\n      - docs/pas_api_key_delivery_doctrine.md\n      - tests/mvp/test_pas_security_03_admin_webhook_ci.py\n  * v33 SQL: PROPOSAL ONLY, ON CONFLICT DO UPDATE, SECURITY\n    DEFINER, tenant/anon REVOKE EXECUTE, service_role GRANT\n    EXECUTE.\n  * rate_limit_rpc service surface tokens present + fallback\n    warning marker.\n  * Admin route rate-limit wired in app/routes/admin.py\'s\n    require_admin.\n  * Webhook route rate-limit wired in app/routes/lead_ingestion.py\'s\n    _ingest helper.\n  * CI dependency gate exists; no auto-fix in executable form.\n  * API key delivery doctrine doc + WAF baseline doc exist.\n  * No raw API key storage in PAS-SECURITY-03 surfaces.\n  * No token / signature echo.\n  * No auto dependency fix.\n  * Process-local fallback warning still exists (carry-forward).\n  * No Gmail / OAuth / IMAP / POP3 / Composio / TrustClaw /\n    embeddings / vector / LLM imports.\n  * Memory Review (PAS147-PAS158) untouched.\n  * audit_service still has no UPDATE / DELETE helpers.\n  * Event contract registers PAS-SECURITY-03 events.\n  * Worker still OFF by default.\n  * Supports --summary-only / --json.\n  * Exits 0 ready, 1 blockers, 2 bad args.\n  * Never reads .env.\n  * Never touches production data.\n'
- 'utf-8'
- 'READY'
- 'NOT_READY'
- 'BLOCK'
- 'INFO'
- 'severity'
- 'detail'
- 'pas_security_03_admin_webhook_ci_readiness_report.json'
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
- 'Required PAS-SECURITY-03 file present: '
- 'missing'
- 'prior_phase:'
- 'Prior-phase readiness script intact: '
- 'missing — PAS-SECURITY-03 must not delete'
- 'memory_review:'
- 'Memory Review file present: '
- 'Memory Review file deleted — PAS-SECURITY-03 must not touch'
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
- 'migrate_v33_rate_limit_atomic_rpc.sql'
- 'v33_sql:proposal_only'
- 'proposal only'
- "v33 SQL carries 'PROPOSAL ONLY' guardrail"
- 'v33_sql:do_not_execute'
- 'do not execute'
- "v33 SQL carries 'DO NOT EXECUTE' trailer"
- 'v33_sql:on_conflict_update'
- 'ON CONFLICT (bucket_key) DO UPDATE'
- 'v33 SQL carries atomic ON CONFLICT (bucket_key) DO UPDATE'
- 'v33_sql:security_definer'
- 'SECURITY DEFINER'
- 'v33 SQL function is SECURITY DEFINER'
- 'CREATE OR REPLACE FUNCTION pas_increment_rate_limit_counter'
- 'v33_sql:rpc_function_name'
- 'v33 SQL defines pas_increment_rate_limit_counter(...)'
- 'REVOKE ALL ON FUNCTION pas_increment_rate_limit_counter'
- 'FROM authenticated'
- 'FROM anon'
- 'v33_sql:tenant_anon_revoke'
- 'v33 SQL REVOKEs EXECUTE from authenticated + anon'
- 'GRANT EXECUTE ON FUNCTION pas_increment_rate_limit_counter'
- 'TO service_role'
- 'v33_sql:service_role_grant'
- 'v33 SQL GRANTs EXECUTE to service_role'
- 'pas_rate_limit_increment_result'
- 'CREATE TYPE pas_rate_limit_increment_result AS'
- 'v33_sql:closed_return_type'
- 'v33 SQL defines the closed pas_rate_limit_increment_result type'
- 'security'
- 'rate_limit_rpc.py'
- 'rpc:'
- 'rate_limit_rpc module exports '
- 'missing token '
- 'routes'
- 'admin.py'
- 'check_rate_limit('
- 'surface="admin"'
- 'actor_type="ADMIN"'
- 'status_code=429'
- 'admin:rate_limit_wired'
- '/admin/* routes wire check_rate_limit(surface=admin, actor_type=ADMIN) and 429'
- 'missing required admin rate-limit wiring'
- 'lead_ingestion.py'
- 'webhook_generic'
- 'webhook_zapier'
- 'webhook_followupboss'
- 'webhook_gohighlevel'
- 'rate_limit_public_error('
- 'webhook:rate_limit_wired'
- '/webhooks/* routes wire check_rate_limit for all 4 surfaces + public 429 envelope'
- 'missing webhook rate-limit wiring'
- 'security_ci_dependency_gate.py'
- 'ci_gate:'
- 'CI dependency gate exports '
- 'ci_gate:no_auto_fix'
- 'CI dependency gate does not call auto-fix / upgrade helpers (executable form)'
- 'disqualifying tokens: '
- 'PAS-SECURITY-03 surfaces (rpc service + admin/webhook\nwiring + CI gate + key-delivery doctrine) MUST NEVER carry\nraw key / raw IP / user-agent-raw tokens in executable\nform.'
- 'no_raw_key_storage:'
- 'No raw_api_key / raw_ip / user_agent_raw tokens in executable: '
- 'docs'
- 'pas_api_key_delivery_doctrine.md'
- 'docs:key_delivery:'
- 'key-delivery doctrine carries clause: '
- 'expected one of: '
- ' | '
- 'docs:key_delivery:no_raw_key_hack'
- 'key-delivery doctrine does not include raw-key-echo hack tokens'
- 'pas_waf_boundary_security_baseline.md'
- 'docs:waf:'
- 'WAF baseline doc carries clause: '
- 'pas_security_03_admin_webhook_ci_gate.md'
- 'docs:pas_security_03:'
- 'PAS-SECURITY-03 doctrine carries clause: '
- 'operator'
- 'audit_service.py'
- 'audit_service:append_only_carry'
- 'Audit service still has no UPDATE / DELETE mutation helpers (carry-forward invariant)'
- 'events'
- 'contract.py'
- 'events:'
- 'Event contract registers '
- 'missing event type '
- 'app/services/security/rate_limit_rpc.py'
- 'forbidden_import:'
- 'No forbidden imports: '
- 'forbidden import prefixes: '
- 'no_inbox_scan:'
- 'No inbox-scanning tokens: '
- 'inbox-scan tokens present: '
- 'The PAS-SECURITY-02 process-local fallback marker MUST\nstill exist in rate_limit_store.py.'
- 'rate_limit_store.py'
- 'rate_limit_store_process_local'
- 'carry_forward:process_local_fallback'
- 'PAS-SECURITY-02 process-local fallback marker still present'
- 'dotenv import'
- 'supabase import'
- 'load_dotenv()'
- 'load_dotenv() call'
- 'environ read'
- 'get_supabase'
- 'supabase client call'
- 'self_check:no_env_or_db'
- 'PAS-SECURITY-03 readiness checker never reads .env / touches DB'
- 'disqualifying patterns: '
- 'checks'
- 'verdict'
- 'blockers'
- 'info'
- 'List[str]'
- ' — '
- 'see report'
- 'phase'
- 'PAS-SECURITY-03'
- 'generated_at'
- 'ready'
- 'blocker_count'
- 'info_count'
- 'check_count'
- 'pass_count'
- 'fail_count'
- 'operator_actions'
- 'argparse.ArgumentParser'
- 🔒 '<REDACTED:high-entropy blob, len=48>'
- 'PAS-SECURITY-03 — Evaluate admin/webhook rate-limit wiring + atomic counter RPC + CI scanner gate + API-key delivery doctrine + WAF baseline. Read-only — never reads .env, never touches Supabase, never runs a migration.'
- '--repo-root'
- '--output'
- '--json'
- 'store_true'
- '--summary-only'
- '--strict'
- 'report'
- 'None'
- '[PAS-SECURITY-03] verdict='
- ' blockers='
- ' info='
- ' checks='
- ' pass='
- ' fail='
- '[PAS-SECURITY-03] operator actions:'
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

   1           LOAD_CONST               0 ('\nPAS-SECURITY-03 — Admin / webhook rate-limit + atomic counter\n+ CI scanner gate readiness check.\n\nDeterministic, non-mutating evaluator for "is PAS-SECURITY-03\nwired correctly and free of regressions in the\nPAS160-PAS-SECURITY-02 doctrine?".\n\nWalks the repo and verifies:\n\n  * PAS160-PAS181 + PAS-SECURITY-01/02 readiness scripts still\n    exist.\n  * PAS-SECURITY-03 surfaces exist:\n      - scripts/migrate_v33_rate_limit_atomic_rpc.sql\n      - app/services/security/rate_limit_rpc.py\n      - scripts/security_ci_dependency_gate.py\n      - scripts/pas_security_03_admin_webhook_ci_readiness_check.py\n      - docs/pas_security_03_admin_webhook_ci_gate.md\n      - docs/pas_waf_boundary_security_baseline.md\n      - docs/pas_api_key_delivery_doctrine.md\n      - tests/mvp/test_pas_security_03_admin_webhook_ci.py\n  * v33 SQL: PROPOSAL ONLY, ON CONFLICT DO UPDATE, SECURITY\n    DEFINER, tenant/anon REVOKE EXECUTE, service_role GRANT\n    EXECUTE.\n  * rate_limit_rpc service surface tokens present + fallback\n    warning marker.\n  * Admin route rate-limit wired in app/routes/admin.py\'s\n    require_admin.\n  * Webhook route rate-limit wired in app/routes/lead_ingestion.py\'s\n    _ingest helper.\n  * CI dependency gate exists; no auto-fix in executable form.\n  * API key delivery doctrine doc + WAF baseline doc exist.\n  * No raw API key storage in PAS-SECURITY-03 surfaces.\n  * No token / signature echo.\n  * No auto dependency fix.\n  * Process-local fallback warning still exists (carry-forward).\n  * No Gmail / OAuth / IMAP / POP3 / Composio / TrustClaw /\n    embeddings / vector / LLM imports.\n  * Memory Review (PAS147-PAS158) untouched.\n  * audit_service still has no UPDATE / DELETE helpers.\n  * Event contract registers PAS-SECURITY-03 events.\n  * Worker still OFF by default.\n  * Supports --summary-only / --json.\n  * Exits 0 ready, 1 blockers, 2 bad args.\n  * Never reads .env.\n  * Never touches production data.\n')
               STORE_NAME               0 (__doc__)

  49           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  51           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  52           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (json)
               STORE_NAME               4 (json)

  53           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (os)
               STORE_NAME               5 (os)

  54           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (sys)
               STORE_NAME               6 (sys)

  55           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              7 (datetime)
               IMPORT_FROM              7 (datetime)
               STORE_NAME               7 (datetime)
               IMPORT_FROM              8 (timezone)
               STORE_NAME               8 (timezone)
               POP_TOP

  56           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Path',))
               IMPORT_NAME              9 (pathlib)
               IMPORT_FROM             10 (Path)
               STORE_NAME              10 (Path)
               POP_TOP

  57           LOAD_SMALL_INT           0
               LOAD_CONST               5 (('List', 'Optional'))
               IMPORT_NAME             11 (typing)
               IMPORT_FROM             12 (List)
               STORE_NAME              12 (List)
               IMPORT_FROM             13 (Optional)
               STORE_NAME              13 (Optional)
               POP_TOP

  60           LOAD_NAME                6 (sys)
               LOAD_ATTR               28 (stdout)
               LOAD_NAME                6 (sys)
               LOAD_ATTR               30 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              16 (_stream)

  61           NOP

  62   L2:     LOAD_NAME               16 (_stream)
               LOAD_ATTR               35 (reconfigure + NULL|self)
               LOAD_CONST               6 ('utf-8')
               LOAD_CONST               7 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  60   L4:     END_FOR
               POP_ITER

  67           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               41 (abspath + NULL|self)

  68           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               43 (join + NULL|self)
               LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               45 (dirname + NULL|self)
               LOAD_NAME               23 (__file__)
               CALL                     1
               LOAD_CONST               8 ('..')
               CALL                     2

  67           CALL                     1
               STORE_NAME              24 (_REPO_ROOT_DEFAULT)

  72           LOAD_CONST               9 ('READY')
               STORE_NAME              25 (VERDICT_READY)

  73           LOAD_CONST              10 ('NOT_READY')
               STORE_NAME              26 (VERDICT_NOT_READY)

  75           LOAD_CONST              11 ('BLOCK')
               STORE_NAME              27 (SEVERITY_BLOCK)

  76           LOAD_CONST              12 ('INFO')
               STORE_NAME              28 (SEVERITY_INFO)

  79           LOAD_CONST              78 (('scripts/migrate_v33_rate_limit_atomic_rpc.sql', 'app/services/security/rate_limit_rpc.py', 'scripts/security_ci_dependency_gate.py', 'scripts/pas_security_03_admin_webhook_ci_readiness_check.py', 'docs/pas_security_03_admin_webhook_ci_gate.md', 'docs/pas_waf_boundary_security_baseline.md', 'docs/pas_api_key_delivery_doctrine.md', 'tests/mvp/test_pas_security_03_admin_webhook_ci.py'))
               STORE_NAME              29 (REQUIRED_FILES)

  91           LOAD_CONST              79 (('scripts/pas160_mvp_sequence_check.py', 'scripts/pas169_launch_readiness_check.py', 'scripts/pas_launch_integrity_check.py', 'scripts/pas170_operator_survival_readiness_check.py', 'scripts/pas171_external_pilot_readiness_check.py', 'scripts/pas172_pilot_operations_readiness_check.py', 'scripts/pas173_brokerage_operator_readiness_check.py', 'scripts/pas174_operator_audit_readiness_check.py', 'scripts/pas175_audit_integrity_readiness_check.py', 'scripts/pas176_audit_chain_readiness_check.py', 'scripts/pas177_tenant_audit_verification_readiness_check.py', 'scripts/pas178_audit_window_chain_readiness_check.py', 'scripts/pas179_controlled_learning_readiness_check.py', 'scripts/pas180_learning_review_readiness_check.py', 'scripts/pas181_manual_test_harness_readiness_check.py', 'scripts/pas_security_01_hardening_readiness_check.py', 'scripts/pas_security_02_rate_limit_scanner_readiness_check.py'))
               STORE_NAME              30 (PRIOR_PHASE_FILES)

 111           LOAD_CONST              80 (('app/services/memory/review.py', 'app/services/memory/review_stats.py', 'app/services/memory/review_export.py', 'app/services/memory/review_actors.py', 'app/services/memory/review_alerts.py', 'app/services/memory/operator_console.py'))
               STORE_NAME              31 (MEMORY_REVIEW_FILES)

 121           LOAD_CONST              81 (('def atomic_rate_limit_available(', 'def increment_rate_limit_counter_atomic(', 'def atomic_rate_limit_report(', 'ALLOWED_RPC_BACKENDS', '_RPC_NAME = "pas_increment_rate_limit_counter"', 'rate_limit_rpc_unavailable'))
               STORE_NAME              32 (REQUIRED_RPC_SERVICE_TOKENS)

 131           LOAD_CONST              82 (('def main(', '--fail-on-high', '--fail-on-critical', '--allow-missing-scanner', '--json', 'scan_python_dependencies', 'scan_node_dependencies'))
               STORE_NAME              33 (REQUIRED_CI_GATE_TOKENS)

 142           LOAD_CONST              83 (('security.rate_limit.allowed', 'security.api_key_rotation.requested', 'security.rate_limit.atomic_incremented', 'security.rate_limit.rpc_unavailable', 'security.admin.rate_limit_blocked', 'security.webhook.rate_limit_blocked', 'security.dependency_ci_gate.completed', 'security.dependency_ci_gate.failed', 'security.api_key_delivery.deferred'))
               STORE_NAME              34 (REQUIRED_EVENT_TYPES)

 157           LOAD_CONST              84 (('import gmail', 'from gmail', 'import googleapiclient', 'from googleapiclient', 'import google.oauth2', 'from google.oauth2', 'from google.auth', 'import google.auth', 'from google_auth_oauthlib', 'import imaplib', 'from imaplib', 'import poplib', 'from poplib', 'import composio', 'from composio', 'import trustclaw', 'from trustclaw', 'import chromadb', 'from chromadb', 'import pinecone', 'from pinecone', 'import langchain', 'from langchain', 'import faiss', 'import pgvector', 'from pgvector', 'from openai import embeddings', 'from openai.embeddings', 'from anthropic', 'import anthropic', 'from openai', 'import openai'))
               STORE_NAME              35 (FORBIDDEN_IMPORT_LINE_PREFIXES)

 181           LOAD_CONST              85 (('imaplib', 'poplib', 'fetch_inbox', 'gmail_oauth', 'gmail_token', 'users().messages'))
               STORE_NAME              36 (FORBIDDEN_INBOX_TOKENS)

 191           LOAD_CONST              86 (('pip install', 'pip-audit fix', 'npm audit fix', 'npm install', 'poetry update', 'yarn upgrade'))
               STORE_NAME              37 (FORBIDDEN_AUTO_FIX_TOKENS)

 201           LOAD_CONST              87 (('raw_api_key', 'raw_ip', 'user_agent_raw'))
               STORE_NAME              38 (FORBIDDEN_RAW_KEY_TOKENS)

 212           LOAD_CONST              13 ('severity')

 214           LOAD_NAME               27 (SEVERITY_BLOCK)

 212           LOAD_CONST              14 ('detail')

 214           LOAD_CONST              15 ('')

 212           BUILD_MAP                2
               LOAD_CONST              16 (<code object __annotate__ at 0x0000018C18024C30, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 212>)
               MAKE_FUNCTION
               LOAD_CONST              17 (<code object _check at 0x0000018C17FA34B0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 212>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              39 (_check)

 225           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA3E10, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 225>)
               MAKE_FUNCTION
               LOAD_CONST              19 (<code object _now_iso at 0x0000018C180388F0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 225>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              40 (_now_iso)

 229           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA3960, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 229>)
               MAKE_FUNCTION
               LOAD_CONST              21 (<code object _read_text at 0x0000018C180532D0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 229>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              41 (_read_text)

 236           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA3C30, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 236>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object _strip_python_comments_and_strings at 0x0000018C17D81580, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 236>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              42 (_strip_python_comments_and_strings)

 275           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA3690, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 275>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object check_files_present at 0x0000018C18061110, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 275>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              43 (check_files_present)

 288           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA30F0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 288>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object check_prior_phases_intact at 0x0000018C18060A50, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 288>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              44 (check_prior_phases_intact)

 301           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA3F00, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 301>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object check_memory_review_intact at 0x0000018C180608A0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 301>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              45 (check_memory_review_intact)

 314           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA2010, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 314>)
               MAKE_FUNCTION
               LOAD_CONST              31 (<code object check_worker_off_by_default at 0x0000018C179C3C30, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 314>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              46 (check_worker_off_by_default)

 331           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA3870, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 331>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object check_v33_sql at 0x0000018C17E58EF0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 331>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              47 (check_v33_sql)

 395           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA3000, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 395>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object check_rpc_service at 0x0000018C17FEDA30, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 395>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              48 (check_rpc_service)

 410           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C181143F0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 410>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object check_admin_rate_limit_wired at 0x0000018C17FED830, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 410>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              49 (check_admin_rate_limit_wired)

 429           LOAD_CONST              38 (<code object __annotate__ at 0x0000018C18114120, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 429>)
               MAKE_FUNCTION
               LOAD_CONST              39 (<code object check_webhook_rate_limit_wired at 0x0000018C182DA720, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 429>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              50 (check_webhook_rate_limit_wired)

 450           LOAD_CONST              40 (<code object __annotate__ at 0x0000018C18114300, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 450>)
               MAKE_FUNCTION
               LOAD_CONST              41 (<code object check_ci_gate_script at 0x0000018C182E5510, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 450>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              51 (check_ci_gate_script)

 477           LOAD_CONST              42 (<code object __annotate__ at 0x0000018C181144E0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 477>)
               MAKE_FUNCTION
               LOAD_CONST              43 (<code object check_no_raw_key_storage at 0x0000018C17CC1F60, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 477>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              52 (check_no_raw_key_storage)

 507           LOAD_CONST              44 (<code object __annotate__ at 0x0000018C181145D0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 507>)
               MAKE_FUNCTION
               LOAD_CONST              45 (<code object check_key_delivery_doctrine_doc at 0x0000018C17F753C0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 507>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              53 (check_key_delivery_doctrine_doc)

 555           LOAD_CONST              46 (<code object __annotate__ at 0x0000018C181146C0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 555>)
               MAKE_FUNCTION
               LOAD_CONST              47 (<code object check_waf_baseline_doc at 0x0000018C17CD2160, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 555>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              54 (check_waf_baseline_doc)

 596           LOAD_CONST              48 (<code object __annotate__ at 0x0000018C181147B0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 596>)
               MAKE_FUNCTION
               LOAD_CONST              49 (<code object check_pas_security_03_doctrine_doc at 0x0000018C17CD0530, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 596>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              55 (check_pas_security_03_doctrine_doc)

 641           LOAD_CONST              50 (<code object __annotate__ at 0x0000018C181148A0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 641>)
               MAKE_FUNCTION
               LOAD_CONST              51 (<code object check_audit_service_invariant at 0x0000018C182DB020, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 641>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              56 (check_audit_service_invariant)

 666           LOAD_CONST              52 (<code object __annotate__ at 0x0000018C18114990, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 666>)
               MAKE_FUNCTION
               LOAD_CONST              53 (<code object check_event_contract at 0x0000018C1801C9E0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 666>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              57 (check_event_contract)

 681           LOAD_CONST              54 (<code object __annotate__ at 0x0000018C18114A80, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 681>)
               MAKE_FUNCTION
               LOAD_CONST              55 (<code object check_no_forbidden_imports at 0x0000018C17EA4A00, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 681>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              58 (check_no_forbidden_imports)

 711           LOAD_CONST              56 (<code object __annotate__ at 0x0000018C18114B70, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 711>)
               MAKE_FUNCTION
               LOAD_CONST              57 (<code object check_no_inbox_scan_tokens at 0x0000018C17CC2960, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 711>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              59 (check_no_inbox_scan_tokens)

 737           LOAD_CONST              58 (<code object __annotate__ at 0x0000018C18114D50, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 737>)
               MAKE_FUNCTION
               LOAD_CONST              59 (<code object check_pas_security_02_carry_forward at 0x0000018C18060DB0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 737>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              60 (check_pas_security_02_carry_forward)

 752           LOAD_CONST              60 (<code object __annotate__ at 0x0000018C18114E40, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 752>)
               MAKE_FUNCTION
               LOAD_CONST              61 (<code object check_self_no_env_or_db at 0x0000018C17D893A0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 752>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              61 (check_self_no_env_or_db)

 785           LOAD_CONST              62 (<code object __annotate__ at 0x0000018C18114F30, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 785>)
               MAKE_FUNCTION
               LOAD_CONST              63 (<code object _aggregate at 0x0000018C1800B230, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 785>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              62 (_aggregate)

 797           LOAD_CONST              64 (<code object __annotate__ at 0x0000018C18115020, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 797>)
               MAKE_FUNCTION
               LOAD_CONST              65 (<code object _operator_actions at 0x0000018C18048E30, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 797>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              63 (_operator_actions)

 807           LOAD_CONST              66 (<code object __annotate__ at 0x0000018C18114030, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 807>)
               MAKE_FUNCTION
               LOAD_CONST              67 (<code object evaluate at 0x0000018C17D7CA90, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 807>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              64 (evaluate)

 845           LOAD_CONST              68 ('pas_security_03_admin_webhook_ci_readiness_report.json')
               STORE_NAME              65 (REPORT_FILENAME)

 848           LOAD_CONST              69 (<code object __annotate__ at 0x0000018C181156B0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 848>)
               MAKE_FUNCTION
               LOAD_CONST              70 (<code object _build_parser at 0x0000018C181285D0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 848>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              66 (_build_parser)

 867           LOAD_CONST              71 (<code object __annotate__ at 0x0000018C181152F0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 867>)
               MAKE_FUNCTION
               LOAD_CONST              72 (<code object _print_summary at 0x0000018C17D8CD10, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 867>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              67 (_print_summary)

 885           LOAD_CONST              73 (<code object __annotate__ at 0x0000018C18026630, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 885>)
               MAKE_FUNCTION
               LOAD_CONST              74 (<code object _write_report at 0x0000018C18128B70, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 885>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              68 (_write_report)

 899           LOAD_CONST              88 ((None,))
               LOAD_CONST              75 (<code object __annotate__ at 0x0000018C18115C50, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 899>)
               MAKE_FUNCTION
               LOAD_CONST              76 (<code object main at 0x0000018C17D89750, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 899>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              69 (main)

 924           LOAD_NAME               70 (__name__)
               LOAD_CONST              77 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 925           LOAD_NAME                6 (sys)
               LOAD_ATTR              142 (exit)
               PUSH_NULL
               LOAD_NAME               69 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 924   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  63           LOAD_NAME               18 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  64   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          367 (to L1)

  63   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 212>:
212           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('check_id')

213           LOAD_CONST               2 ('str')

212           LOAD_CONST               3 ('status')

213           LOAD_CONST               2 ('str')

212           LOAD_CONST               4 ('label')

213           LOAD_CONST               2 ('str')

212           LOAD_CONST               5 ('severity')

214           LOAD_CONST               2 ('str')

212           LOAD_CONST               6 ('detail')

214           LOAD_CONST               2 ('str')

212           LOAD_CONST               7 ('return')

215           LOAD_CONST               8 ('dict')

212           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _check at 0x0000018C17FA34B0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 212>:
212           RESUME                   0

217           LOAD_CONST               0 ('id')
              LOAD_FAST_BORROW         0 (check_id)

218           LOAD_CONST               1 ('status')
              LOAD_FAST_BORROW         1 (status)

219           LOAD_CONST               2 ('label')
              LOAD_FAST_BORROW         2 (label)

220           LOAD_CONST               3 ('severity')
              LOAD_FAST_BORROW         3 (severity)

221           LOAD_CONST               4 ('detail')
              LOAD_FAST_BORROW         4 (detail)

216           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 225>:
225           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C180388F0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 225>:
225           RESUME                   0

226           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 229>:
229           RESUME                   0
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

Disassembly of <code object _read_text at 0x0000018C180532D0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 229>:
 229           RESUME                   0

 230           NOP

 231   L1:     LOAD_FAST_BORROW         0 (path)
               LOAD_ATTR                1 (read_text + NULL|self)
               LOAD_CONST               0 ('utf-8')
               LOAD_CONST               1 ('replace')
               LOAD_CONST               2 (('encoding', 'errors'))
               CALL_KW                  2
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 232           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 233   L4:     POP_EXCEPT
               LOAD_CONST               3 (None)
               RETURN_VALUE

 232   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 236>:
236           RESUME                   0
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

Disassembly of <code object _strip_python_comments_and_strings at 0x0000018C17D81580, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 236>:
236            RESUME                   0

237            BUILD_LIST               0
               STORE_FAST               1 (out)

238            LOAD_SMALL_INT           0
               LOAD_GLOBAL              1 (len + NULL)
               LOAD_FAST_BORROW         0 (src)
               CALL                     1
               STORE_FAST_STORE_FAST   50 (n, i)

239    L1:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (i, n)
               COMPARE_OP              18 (bool(<))
               EXTENDED_ARG             1
               POP_JUMP_IF_FALSE      282 (to L13)
               NOT_TAKEN

240            LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               BINARY_OP               26 ([])
               STORE_FAST               4 (ch)

241            LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               1 ('#')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       38 (to L3)
               NOT_TAKEN

242            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_CONST               2 ('\n')
               LOAD_FAST_BORROW         2 (i)
               CALL                     2
               STORE_FAST               5 (j)

243            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L2)
               NOT_TAKEN

244            JUMP_FORWARD           240 (to L13)

245    L2:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

246            JUMP_BACKWARD           59 (to L1)

247    L3:     LOAD_FAST_BORROW         0 (src)
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

248    L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               BINARY_SLICE
               STORE_FAST               6 (quote)

249            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 98 (quote, i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               CALL                     2
               STORE_FAST               7 (end)

250            LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L5)
               NOT_TAKEN

251            JUMP_FORWARD           138 (to L13)

252    L5:     LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

253            JUMP_BACKWARD          161 (to L1)

254    L6:     LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               7 (('"', "'"))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       92 (to L12)
               NOT_TAKEN

255            LOAD_FAST                4 (ch)
               STORE_FAST               6 (quote)

256            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               5 (j)

257    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (j, n)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       63 (to L11)
               NOT_TAKEN

258            LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
               BINARY_OP               26 ([])
               LOAD_CONST               5 ('\\')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       12 (to L8)
               NOT_TAKEN

259            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           2
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)

260            JUMP_BACKWARD           30 (to L7)

261    L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
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

262    L9:     JUMP_FORWARD            11 (to L11)

263   L10:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)
               JUMP_BACKWARD           68 (to L7)

264   L11:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

265            EXTENDED_ARG             1
               JUMP_BACKWARD          259 (to L1)

266   L12:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (ch)
               CALL                     1
               POP_TOP

267            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               2 (i)
               EXTENDED_ARG             1
               JUMP_BACKWARD          288 (to L1)

268   L13:     LOAD_CONST               6 ('')
               LOAD_ATTR                9 (join + NULL|self)
               LOAD_FAST_BORROW         1 (out)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 275>:
275           RESUME                   0
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

Disassembly of <code object check_files_present at 0x0000018C18061110, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 275>:
275           RESUME                   0

276           BUILD_LIST               0
              STORE_FAST               1 (out)

277           LOAD_GLOBAL              0 (REQUIRED_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

278           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

279           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

280           LOAD_CONST               0 ('file:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

281           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

282   L3:     LOAD_CONST               3 ('Required PAS-SECURITY-03 file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

283           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing')

279   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

277   L6:     END_FOR
              POP_ITER

285           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA30F0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 288>:
288           RESUME                   0
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

Disassembly of <code object check_prior_phases_intact at 0x0000018C18060A50, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 288>:
288           RESUME                   0

289           BUILD_LIST               0
              STORE_FAST               1 (out)

290           LOAD_GLOBAL              0 (PRIOR_PHASE_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

291           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

292           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

293           LOAD_CONST               0 ('prior_phase:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

294           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

295   L3:     LOAD_CONST               3 ('Prior-phase readiness script intact: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

296           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing — PAS-SECURITY-03 must not delete')

292   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

290   L6:     END_FOR
              POP_ITER

298           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3F00, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 301>:
301           RESUME                   0
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

Disassembly of <code object check_memory_review_intact at 0x0000018C180608A0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 301>:
301           RESUME                   0

302           BUILD_LIST               0
              STORE_FAST               1 (out)

303           LOAD_GLOBAL              0 (MEMORY_REVIEW_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

304           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

305           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

306           LOAD_CONST               0 ('memory_review:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

307           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

308   L3:     LOAD_CONST               3 ('Memory Review file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

309           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('Memory Review file deleted — PAS-SECURITY-03 must not touch')

305   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

303   L6:     END_FOR
              POP_ITER

311           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2010, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 314>:
314           RESUME                   0
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

Disassembly of <code object check_worker_off_by_default at 0x0000018C179C3C30, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 314>:
314           RESUME                   0

315           BUILD_LIST               0
              STORE_FAST               1 (out)

316           LOAD_GLOBAL              1 (Path + NULL)
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

317           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

319           LOAD_CONST               5 ('_ENV_FLAG_ENABLED_LITERAL = "true"')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         6 (to L2)
              NOT_TAKEN
              POP_TOP

320           LOAD_CONST               6 ("_ENV_FLAG_ENABLED_LITERAL = 'true'")
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)

318   L2:     STORE_FAST               4 (literal_ok)

322           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

323           LOAD_CONST               7 ('worker:off_by_default')

324           LOAD_FAST_BORROW         4 (literal_ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               8 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               9 ('FAIL')

325   L4:     LOAD_CONST              10 ('Pending-call worker is OFF by default')

326           LOAD_FAST_BORROW         4 (literal_ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST              11 ('missing strict enable-literal constant')

322   L6:     LOAD_CONST              12 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

328           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 331>:
331           RESUME                   0
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

Disassembly of <code object check_v33_sql at 0x0000018C17E58EF0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 331>:
331            RESUME                   0

332            BUILD_LIST               0
               STORE_FAST               1 (out)

333            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('scripts')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('migrate_v33_rate_limit_atomic_rpc.sql')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

334            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               2 ('')
       L1:     STORE_FAST               3 (src)

335            LOAD_FAST_BORROW         3 (src)
               LOAD_ATTR                5 (lower + NULL|self)
               CALL                     0
               STORE_FAST               4 (lower)

336            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

337            LOAD_CONST               3 ('v33_sql:proposal_only')

338            LOAD_CONST               4 ('proposal only')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        3 (to L2)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L3)
       L2:     LOAD_CONST               6 ('FAIL')

339    L3:     LOAD_CONST               7 ("v33 SQL carries 'PROPOSAL ONLY' guardrail")

336            CALL                     3
               CALL                     1
               POP_TOP

341            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

342            LOAD_CONST               8 ('v33_sql:do_not_execute')

343            LOAD_CONST               9 ('do not execute')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L5)
       L4:     LOAD_CONST               6 ('FAIL')

344    L5:     LOAD_CONST              10 ("v33 SQL carries 'DO NOT EXECUTE' trailer")

341            CALL                     3
               CALL                     1
               POP_TOP

346            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

347            LOAD_CONST              11 ('v33_sql:on_conflict_update')

348            LOAD_CONST              12 ('ON CONFLICT (bucket_key) DO UPDATE')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        3 (to L6)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L7)
       L6:     LOAD_CONST               6 ('FAIL')

349    L7:     LOAD_CONST              13 ('v33 SQL carries atomic ON CONFLICT (bucket_key) DO UPDATE')

346            CALL                     3
               CALL                     1
               POP_TOP

351            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

352            LOAD_CONST              14 ('v33_sql:security_definer')

353            LOAD_CONST              15 ('SECURITY DEFINER')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST               6 ('FAIL')

354    L9:     LOAD_CONST              16 ('v33 SQL function is SECURITY DEFINER')

351            CALL                     3
               CALL                     1
               POP_TOP

356            LOAD_CONST              17 ('CREATE OR REPLACE FUNCTION pas_increment_rate_limit_counter')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (rpc_name_ok)

357            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

358            LOAD_CONST              18 ('v33_sql:rpc_function_name')

359            LOAD_FAST_BORROW         5 (rpc_name_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST               6 ('FAIL')

360   L11:     LOAD_CONST              19 ('v33 SQL defines pas_increment_rate_limit_counter(...)')

357            CALL                     3
               CALL                     1
               POP_TOP

364            LOAD_CONST              20 ('REVOKE ALL ON FUNCTION pas_increment_rate_limit_counter')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       19 (to L12)
               NOT_TAKEN
               POP_TOP

365            LOAD_CONST              21 ('FROM authenticated')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

364            COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        6 (to L12)
               NOT_TAKEN
               POP_TOP

366            LOAD_CONST              22 ('FROM anon')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

363   L12:     STORE_FAST               6 (revokes_ok)

368            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

369            LOAD_CONST              23 ('v33_sql:tenant_anon_revoke')

370            LOAD_FAST_BORROW         6 (revokes_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L13)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L14)
      L13:     LOAD_CONST               6 ('FAIL')

371   L14:     LOAD_CONST              24 ('v33 SQL REVOKEs EXECUTE from authenticated + anon')

368            CALL                     3
               CALL                     1
               POP_TOP

374            LOAD_CONST              25 ('GRANT EXECUTE ON FUNCTION pas_increment_rate_limit_counter')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        6 (to L15)
               NOT_TAKEN
               POP_TOP

375            LOAD_CONST              26 ('TO service_role')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

373   L15:     STORE_FAST               7 (grant_ok)

377            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

378            LOAD_CONST              27 ('v33_sql:service_role_grant')

379            LOAD_FAST_BORROW         7 (grant_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L16)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L17)
      L16:     LOAD_CONST               6 ('FAIL')

380   L17:     LOAD_CONST              28 ('v33 SQL GRANTs EXECUTE to service_role')

377            CALL                     3
               CALL                     1
               POP_TOP

384            LOAD_CONST              29 ('pas_rate_limit_increment_result')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        6 (to L18)
               NOT_TAKEN
               POP_TOP

385            LOAD_CONST              30 ('CREATE TYPE pas_rate_limit_increment_result AS')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

383   L18:     STORE_FAST               8 (return_ok)

387            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

388            LOAD_CONST              31 ('v33_sql:closed_return_type')

389            LOAD_FAST_BORROW         8 (return_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L19)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L20)
      L19:     LOAD_CONST               6 ('FAIL')

390   L20:     LOAD_CONST              32 ('v33 SQL defines the closed pas_rate_limit_increment_result type')

387            CALL                     3
               CALL                     1
               POP_TOP

392            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3000, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 395>:
395           RESUME                   0
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

Disassembly of <code object check_rpc_service at 0x0000018C17FEDA30, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 395>:
395           RESUME                   0

396           BUILD_LIST               0
              STORE_FAST               1 (out)

397           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('services')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('security')
              BINARY_OP               11 (/)
              LOAD_CONST               3 ('rate_limit_rpc.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

398           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

399           LOAD_GLOBAL              4 (REQUIRED_RPC_SERVICE_TOKENS)
              GET_ITER
      L2:     FOR_ITER                73 (to L7)
              STORE_FAST               4 (tok)

400           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

401           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

402           LOAD_CONST               5 ('rpc:')
              LOAD_FAST_BORROW         4 (tok)
              LOAD_CONST               6 (slice(None, 48, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

403           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               7 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               8 ('FAIL')

404   L4:     LOAD_CONST               9 ('rate_limit_rpc module exports ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

405           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             4 (to L6)
      L5:     LOAD_CONST              10 ('missing token ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

401   L6:     LOAD_CONST              11 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           75 (to L2)

399   L7:     END_FOR
              POP_ITER

407           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181143F0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 410>:
410           RESUME                   0
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

Disassembly of <code object check_admin_rate_limit_wired at 0x0000018C17FED830, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 410>:
410           RESUME                   0

411           BUILD_LIST               0
              STORE_FAST               1 (out)

412           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('routes')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('admin.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

413           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               3 ('')
      L1:     STORE_FAST               3 (src)

415           LOAD_CONST               4 ('check_rate_limit(')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       32 (to L2)
              NOT_TAKEN
              POP_TOP

416           LOAD_CONST               5 ('surface="admin"')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)

415           COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       19 (to L2)
              NOT_TAKEN
              POP_TOP

417           LOAD_CONST               6 ('actor_type="ADMIN"')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)

415           COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE        6 (to L2)
              NOT_TAKEN
              POP_TOP

418           LOAD_CONST               7 ('status_code=429')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)

414   L2:     STORE_FAST               4 (ok)

420           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

421           LOAD_CONST               8 ('admin:rate_limit_wired')

422           LOAD_FAST_BORROW         4 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               9 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST              10 ('FAIL')

423   L4:     LOAD_CONST              11 ('/admin/* routes wire check_rate_limit(surface=admin, actor_type=ADMIN) and 429')

424           LOAD_FAST_BORROW         4 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               3 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST              12 ('missing required admin rate-limit wiring')

420   L6:     LOAD_CONST              13 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

426           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114120, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 429>:
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

Disassembly of <code object check_webhook_rate_limit_wired at 0x0000018C182DA720, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 429>:
429           RESUME                   0

430           BUILD_LIST               0
              STORE_FAST               1 (out)

431           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('routes')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('lead_ingestion.py')
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
              LOAD_CONST               3 ('')
      L1:     STORE_FAST               3 (src)

434           LOAD_CONST               4 ('check_rate_limit(')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       58 (to L2)
              NOT_TAKEN
              POP_TOP

435           LOAD_CONST               5 ('webhook_generic')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)

434           COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       45 (to L2)
              NOT_TAKEN
              POP_TOP

436           LOAD_CONST               6 ('webhook_zapier')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)

434           COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       32 (to L2)
              NOT_TAKEN
              POP_TOP

437           LOAD_CONST               7 ('webhook_followupboss')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)

434           COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       19 (to L2)
              NOT_TAKEN
              POP_TOP

438           LOAD_CONST               8 ('webhook_gohighlevel')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)

434           COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE        6 (to L2)
              NOT_TAKEN
              POP_TOP

439           LOAD_CONST               9 ('rate_limit_public_error(')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)

433   L2:     STORE_FAST               4 (ok)

441           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

442           LOAD_CONST              10 ('webhook:rate_limit_wired')

443           LOAD_FAST_BORROW         4 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST              11 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST              12 ('FAIL')

444   L4:     LOAD_CONST              13 ('/webhooks/* routes wire check_rate_limit for all 4 surfaces + public 429 envelope')

445           LOAD_FAST_BORROW         4 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               3 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST              14 ('missing webhook rate-limit wiring')

441   L6:     LOAD_CONST              15 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

447           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114300, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 450>:
450           RESUME                   0
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

Disassembly of <code object check_ci_gate_script at 0x0000018C182E5510, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 450>:
450            RESUME                   0

451            BUILD_LIST               0
               STORE_FAST               1 (out)

452            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('scripts')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('security_ci_dependency_gate.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

453            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               2 ('')
       L1:     STORE_FAST               3 (src)

454            LOAD_GLOBAL              4 (REQUIRED_CI_GATE_TOKENS)
               GET_ITER
       L2:     FOR_ITER                73 (to L7)
               STORE_FAST               4 (tok)

455            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

456            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

457            LOAD_CONST               3 ('ci_gate:')
               LOAD_FAST_BORROW         4 (tok)
               LOAD_CONST               4 (slice(None, 48, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

458            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               6 ('FAIL')

459    L4:     LOAD_CONST               7 ('CI dependency gate exports ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

460            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST               8 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

456    L6:     LOAD_CONST               9 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           75 (to L2)

454    L7:     END_FOR
               POP_ITER

463            LOAD_GLOBAL             11 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               6 (executable)

464            BUILD_LIST               0
               STORE_FAST               7 (bad)

465            LOAD_GLOBAL             12 (FORBIDDEN_AUTO_FIX_TOKENS)
               GET_ITER
       L8:     FOR_ITER                57 (to L10)
               STORE_FAST               4 (tok)

466            LOAD_FAST_BORROW         4 (tok)
               LOAD_ATTR               15 (lower + NULL|self)
               CALL                     0
               LOAD_FAST_BORROW         6 (executable)
               LOAD_ATTR               15 (lower + NULL|self)
               CALL                     0
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L9)
               NOT_TAKEN
               JUMP_BACKWARD           40 (to L8)

467    L9:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (tok)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           59 (to L8)

465   L10:     END_FOR
               POP_ITER

468            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

469            LOAD_CONST              10 ('ci_gate:no_auto_fix')

470            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               6 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               5 ('PASS')

471   L12:     LOAD_CONST              11 ('CI dependency gate does not call auto-fix / upgrade helpers (executable form)')

472            LOAD_FAST_BORROW         7 (bad)
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

468   L14:     LOAD_CONST               9 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

474            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181144E0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 477>:
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

Disassembly of <code object check_no_raw_key_storage at 0x0000018C17CC1F60, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 477>:
477            RESUME                   0

482            BUILD_LIST               0
               STORE_FAST               1 (out)

483            LOAD_CONST               9 (('app/services/security/rate_limit_rpc.py', 'scripts/security_ci_dependency_gate.py', 'scripts/pas_security_03_admin_webhook_ci_readiness_check.py'))
               STORE_FAST               2 (files)

488            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               195 (to L11)
               STORE_FAST               3 (relpath)

489            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

490            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

491            JUMP_BACKWARD           45 (to L1)

492    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

493            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         5 (src)
               CALL                     1
               STORE_FAST               6 (executable)

494            BUILD_LIST               0
               STORE_FAST               7 (bad)

495            LOAD_GLOBAL              8 (FORBIDDEN_RAW_KEY_TOKENS)
               GET_ITER
       L4:     FOR_ITER                28 (to L6)
               STORE_FAST               8 (tok)

496            LOAD_FAST_BORROW_LOAD_FAST_BORROW 134 (tok, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L4)

497    L5:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_FAST_BORROW         8 (tok)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L4)

495    L6:     END_FOR
               POP_ITER

498            LOAD_FAST                1 (out)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_GLOBAL             13 (_check + NULL)

499            LOAD_CONST               2 ('no_raw_key_storage:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

500            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L7)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L8)
       L7:     LOAD_CONST               4 ('PASS')

501    L8:     LOAD_CONST               5 ('No raw_api_key / raw_ip / user_agent_raw tokens in executable: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

502            LOAD_FAST_BORROW         7 (bad)
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

498   L10:     LOAD_CONST               8 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          197 (to L1)

488   L11:     END_FOR
               POP_ITER

504            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181145D0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 507>:
507           RESUME                   0
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

Disassembly of <code object check_key_delivery_doctrine_doc at 0x0000018C17F753C0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 507>:
  --            MAKE_CELL               11 (lower)

 507            RESUME                   0

 508            BUILD_LIST               0
                STORE_FAST               1 (out)

 509            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('docs')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('pas_api_key_delivery_doctrine.md')
                BINARY_OP               11 (/)
                STORE_FAST               2 (doc)

 510            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (doc)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L1:     STORE_FAST               3 (src)

 511            LOAD_FAST_BORROW         3 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_DEREF             11 (lower)

 513            LOAD_CONST              17 ((('purpose', ('purpose',)), ('current-limitation', ('current limitation',)), ('never-logged', ('never be logged', 'never logged')), ('never-stored', ('never be stored', 'never stored')), ('recommended-channels', ('recommended delivery channels', 'recommended delivery')), ('one-time-reveal', ('one-time reveal',)), ('operator-assisted', ('operator-assisted',)), ('future-options', ('future',)), ('email-unsafe', ('plaintext email', 'plaintext')), ('deferred', ('deferred', 'intentionally does not'))))
                STORE_FAST               4 (required_phrases)

 528            LOAD_FAST_BORROW         4 (required_phrases)
                GET_ITER
        L2:     FOR_ITER               141 (to L12)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   86 (name, phrases)

 529            LOAD_GLOBAL              6 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW        11 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18024F30, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 529>)
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
                LOAD_FAST_BORROW        11 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18024F30, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 529>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         6 (phrases)
                GET_ITER
                CALL                     0
                CALL                     1
        L7:     STORE_FAST               7 (present)

 530            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 531            LOAD_CONST               6 ('docs:key_delivery:')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 532            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               8 ('FAIL')

 533    L9:     LOAD_CONST               9 ('key-delivery doctrine carries clause: ')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 535            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L10)
                NOT_TAKEN

 534            LOAD_CONST              10 ('expected one of: ')
                LOAD_CONST              11 (' | ')
                LOAD_ATTR               13 (join + NULL|self)
                LOAD_FAST_BORROW         6 (phrases)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L11)

 535   L10:     LOAD_CONST               2 ('')

 530   L11:     LOAD_CONST              12 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          143 (to L2)

 528   L12:     END_FOR
                POP_ITER

 541            LOAD_CONST              18 (('raw_api_key', 'user_agent_raw'))
                STORE_FAST               8 (bad_tokens)

 542            BUILD_LIST               0
                STORE_FAST               9 (bad)

 543            LOAD_FAST_BORROW         8 (bad_tokens)
                GET_ITER
       L13:     FOR_ITER                42 (to L15)
                STORE_FAST              10 (tok)

 544            LOAD_FAST_BORROW_LOAD_FAST_BORROW 163 (tok, src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN
                JUMP_BACKWARD           25 (to L13)

 545   L14:     LOAD_FAST_BORROW         9 (bad)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_FAST_BORROW        10 (tok)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           44 (to L13)

 543   L15:     END_FOR
                POP_ITER

 546            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 547            LOAD_CONST              13 ('docs:key_delivery:no_raw_key_hack')

 548            LOAD_FAST_BORROW         9 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L16)
                NOT_TAKEN
                LOAD_CONST               8 ('FAIL')
                JUMP_FORWARD             1 (to L17)
       L16:     LOAD_CONST               7 ('PASS')

 549   L17:     LOAD_CONST              14 ('key-delivery doctrine does not include raw-key-echo hack tokens')

 550            LOAD_FAST_BORROW         9 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L18)
                NOT_TAKEN
                LOAD_CONST              15 ('disqualifying tokens: ')
                LOAD_CONST              16 (', ')
                LOAD_ATTR               13 (join + NULL|self)
                LOAD_FAST_BORROW         9 (bad)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L19)
       L18:     LOAD_CONST               2 ('')

 546   L19:     LOAD_CONST              12 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 552            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18024F30, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 529>:
  --           COPY_FREE_VARS           1

 529           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C181146C0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 555>:
555           RESUME                   0
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

Disassembly of <code object check_waf_baseline_doc at 0x0000018C17CD2160, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 555>:
  --            MAKE_CELL                8 (lower)

 555            RESUME                   0

 556            BUILD_LIST               0
                STORE_FAST               1 (out)

 557            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('docs')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('pas_waf_boundary_security_baseline.md')
                BINARY_OP               11 (/)
                STORE_FAST               2 (doc)

 558            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (doc)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L1:     STORE_FAST               3 (src)

 559            LOAD_FAST_BORROW         3 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_DEREF              8 (lower)

 560            LOAD_CONST              13 ((('purpose', ('purpose',)), ('production-boundary', ('production boundary doctrine', 'production boundary')), ('waf-cdn-posture', ('recommended waf', 'recommended waf / cdn')), ('allowed-origins', ('allowed origins',)), ('tls-only', ('tls-only',)), ('body-size', ('request body size limits', 'request body size')), ('bot-rate', ('bot / rate-limit', 'bot/rate-limit', 'bot-rate-limit', 'bot detection')), ('ip-allowlist', ('ip allowlist for admin', 'ip allowlist')), ('webhook-protection', ('webhook endpoint protection', 'webhook endpoint')), ('checklist', ('deploy-environment checklist', 'deploy environment checklist')), ('app-vs-infra', ('app-layer vs infrastructure', 'app layer vs')), ('limitations', ('known limitations',))))
                STORE_FAST               4 (required_phrases)

 584            LOAD_FAST_BORROW         4 (required_phrases)
                GET_ITER
        L2:     FOR_ITER               141 (to L12)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   86 (name, phrases)

 585            LOAD_GLOBAL              6 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         8 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18025C30, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 585>)
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
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18025C30, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 585>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         6 (phrases)
                GET_ITER
                CALL                     0
                CALL                     1
        L7:     STORE_FAST               7 (present)

 586            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 587            LOAD_CONST               6 ('docs:waf:')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 588            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               8 ('FAIL')

 589    L9:     LOAD_CONST               9 ('WAF baseline doc carries clause: ')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 591            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L10)
                NOT_TAKEN

 590            LOAD_CONST              10 ('expected one of: ')
                LOAD_CONST              11 (' | ')
                LOAD_ATTR               13 (join + NULL|self)
                LOAD_FAST_BORROW         6 (phrases)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L11)

 591   L10:     LOAD_CONST               2 ('')

 586   L11:     LOAD_CONST              12 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          143 (to L2)

 584   L12:     END_FOR
                POP_ITER

 593            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18025C30, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 585>:
  --           COPY_FREE_VARS           1

 585           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C181147B0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 596>:
596           RESUME                   0
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

Disassembly of <code object check_pas_security_03_doctrine_doc at 0x0000018C17CD0530, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 596>:
  --            MAKE_CELL                8 (lower)

 596            RESUME                   0

 597            BUILD_LIST               0
                STORE_FAST               1 (out)

 598            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('docs')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('pas_security_03_admin_webhook_ci_gate.md')
                BINARY_OP               11 (/)
                STORE_FAST               2 (doc)

 599            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (doc)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L1:     STORE_FAST               3 (src)

 600            LOAD_FAST_BORROW         3 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_DEREF              8 (lower)

 601            LOAD_CONST              13 ((('purpose', ('purpose',)), ('pas-security-01-02', ('relationship to pas-security-01',)), ('admin-rate-limit', ('admin route rate-limit doctrine', 'admin route rate-limit')), ('webhook-rate-limit', ('webhook route rate-limit doctrine', 'webhook route rate-limit')), ('atomic-counter', ('atomic counter doctrine', 'atomic counter')), ('fallback', ('fallback limitation', 'fallback')), ('ci-scanner', ('ci scanner doctrine', 'ci scanner')), ('no-auto-fix', ('no-auto-fix', 'no auto-fix')), ('key-delivery-ref', ('key delivery doctrine reference', 'key delivery doctrine')), ('waf-baseline-ref', ('waf baseline reference', 'waf baseline')), ('limitations', ('remaining limitations', 'limitation')), ('not-built', ('intentionally does not', 'intentionally not build', 'deliberately not')), ('no-gmail', ('no gmail',)), ('no-autonomous', ('no autonomous remediation', 'no autonomous'))))
                STORE_FAST               4 (required_phrases)

 629            LOAD_FAST_BORROW         4 (required_phrases)
                GET_ITER
        L2:     FOR_ITER               141 (to L12)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   86 (name, phrases)

 630            LOAD_GLOBAL              6 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         8 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18026130, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 630>)
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
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18026130, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 630>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         6 (phrases)
                GET_ITER
                CALL                     0
                CALL                     1
        L7:     STORE_FAST               7 (present)

 631            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 632            LOAD_CONST               6 ('docs:pas_security_03:')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 633            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               8 ('FAIL')

 634    L9:     LOAD_CONST               9 ('PAS-SECURITY-03 doctrine carries clause: ')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 636            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L10)
                NOT_TAKEN

 635            LOAD_CONST              10 ('expected one of: ')
                LOAD_CONST              11 (' | ')
                LOAD_ATTR               13 (join + NULL|self)
                LOAD_FAST_BORROW         6 (phrases)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L11)

 636   L10:     LOAD_CONST               2 ('')

 631   L11:     LOAD_CONST              12 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          143 (to L2)

 629   L12:     END_FOR
                POP_ITER

 638            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18026130, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 630>:
  --           COPY_FREE_VARS           1

 630           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C181148A0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 641>:
641           RESUME                   0
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

Disassembly of <code object check_audit_service_invariant at 0x0000018C182DB020, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 641>:
641           RESUME                   0

642           BUILD_LIST               0
              STORE_FAST               1 (out)

643           LOAD_GLOBAL              1 (Path + NULL)
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

644           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

645           LOAD_CONST              12 (('def update_audit_', 'def delete_audit_', 'def update_operator_audit_', 'def delete_operator_audit_', 'def mutate_audit_', 'def truncate_audit_'))
              STORE_FAST               4 (forbidden)

653           BUILD_LIST               0
              STORE_FAST               5 (bad)

654           LOAD_FAST_BORROW         4 (forbidden)
              GET_ITER
      L2:     FOR_ITER                28 (to L4)
              STORE_FAST               6 (tok)

655           LOAD_FAST_BORROW_LOAD_FAST_BORROW 99 (tok, src)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

656   L3:     LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_FAST_BORROW         6 (tok)
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           30 (to L2)

654   L4:     END_FOR
              POP_ITER

657           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

658           LOAD_CONST               5 ('audit_service:append_only_carry')

659           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               6 ('FAIL')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               7 ('PASS')

660   L6:     LOAD_CONST               8 ('Audit service still has no UPDATE / DELETE mutation helpers (carry-forward invariant)')

661           LOAD_FAST_BORROW         5 (bad)
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

657   L8:     LOAD_CONST              11 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

663           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114990, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 666>:
666           RESUME                   0
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

Disassembly of <code object check_event_contract at 0x0000018C1801C9E0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 666>:
666           RESUME                   0

667           BUILD_LIST               0
              STORE_FAST               1 (out)

668           LOAD_GLOBAL              1 (Path + NULL)
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

669           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

670           LOAD_GLOBAL              4 (REQUIRED_EVENT_TYPES)
              GET_ITER
      L2:     FOR_ITER                67 (to L7)
              STORE_FAST               4 (required)

671           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (required, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

672           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

673           LOAD_CONST               5 ('events:')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

674           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               6 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               7 ('FAIL')

675   L4:     LOAD_CONST               8 ('Event contract registers ')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

676           LOAD_FAST_BORROW         5 (ok)
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

672   L6:     LOAD_CONST              10 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           69 (to L2)

670   L7:     END_FOR
              POP_ITER

678           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114A80, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 681>:
681           RESUME                   0
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

Disassembly of <code object check_no_forbidden_imports at 0x0000018C17EA4A00, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 681>:
681            RESUME                   0

682            BUILD_LIST               0
               STORE_FAST               1 (out)

683            LOAD_CONST              10 (('app/services/security/rate_limit_rpc.py', 'scripts/security_ci_dependency_gate.py', 'scripts/pas_security_03_admin_webhook_ci_readiness_check.py'))
               STORE_FAST               2 (files)

688            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     EXTENDED_ARG             1
               FOR_ITER               292 (to L15)
               STORE_FAST               3 (relpath)

689            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

690            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

691            JUMP_BACKWARD           46 (to L1)

692    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

693            BUILD_LIST               0
               STORE_FAST               6 (bad)

694            LOAD_FAST_BORROW         5 (src)
               LOAD_ATTR                7 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L4:     FOR_ITER               107 (to L10)
               STORE_FAST               7 (line)

695            LOAD_FAST_BORROW         7 (line)
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               STORE_FAST               8 (stripped)

696            LOAD_FAST_BORROW         8 (stripped)
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

697    L5:     JUMP_BACKWARD           52 (to L4)

698    L6:     LOAD_GLOBAL             12 (FORBIDDEN_IMPORT_LINE_PREFIXES)
               GET_ITER
       L7:     FOR_ITER                45 (to L9)
               STORE_FAST               9 (prefix)

699            LOAD_FAST_BORROW         8 (stripped)
               LOAD_ATTR               11 (startswith + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD           28 (to L7)

700    L8:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           47 (to L7)

698    L9:     END_FOR
               POP_ITER
               JUMP_BACKWARD          109 (to L4)

694   L10:     END_FOR
               POP_ITER

701            LOAD_FAST                1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             17 (_check + NULL)

702            LOAD_CONST               3 ('forbidden_import:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

703            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               4 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               5 ('PASS')

704   L12:     LOAD_CONST               6 ('No forbidden imports: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

706            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       43 (to L13)
               NOT_TAKEN

705            LOAD_CONST               7 ('forbidden import prefixes: ')
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

706   L13:     LOAD_CONST               1 ('')

701   L14:     LOAD_CONST               9 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          295 (to L1)

688   L15:     END_FOR
               POP_ITER

708            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114B70, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 711>:
711           RESUME                   0
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

Disassembly of <code object check_no_inbox_scan_tokens at 0x0000018C17CC2960, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 711>:
711            RESUME                   0

712            BUILD_LIST               0
               STORE_FAST               1 (out)

713            LOAD_CONST               9 (('app/services/security/rate_limit_rpc.py', 'scripts/security_ci_dependency_gate.py'))
               STORE_FAST               2 (files)

717            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               195 (to L11)
               STORE_FAST               3 (relpath)

718            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

719            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

720            JUMP_BACKWARD           45 (to L1)

721    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

722            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         5 (src)
               CALL                     1
               STORE_FAST               6 (executable)

723            BUILD_LIST               0
               STORE_FAST               7 (bad)

724            LOAD_GLOBAL              8 (FORBIDDEN_INBOX_TOKENS)
               GET_ITER
       L4:     FOR_ITER                28 (to L6)
               STORE_FAST               8 (token)

725            LOAD_FAST_BORROW_LOAD_FAST_BORROW 134 (token, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L4)

726    L5:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_FAST_BORROW         8 (token)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L4)

724    L6:     END_FOR
               POP_ITER

727            LOAD_FAST                1 (out)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_GLOBAL             13 (_check + NULL)

728            LOAD_CONST               2 ('no_inbox_scan:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

729            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L7)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L8)
       L7:     LOAD_CONST               4 ('PASS')

730    L8:     LOAD_CONST               5 ('No inbox-scanning tokens: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

732            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L9)
               NOT_TAKEN

731            LOAD_CONST               6 ('inbox-scan tokens present: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               15 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L10)

732    L9:     LOAD_CONST               1 ('')

727   L10:     LOAD_CONST               8 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          197 (to L1)

717   L11:     END_FOR
               POP_ITER

734            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114D50, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 737>:
737           RESUME                   0
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

Disassembly of <code object check_pas_security_02_carry_forward at 0x0000018C18060DB0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 737>:
737           RESUME                   0

740           BUILD_LIST               0
              STORE_FAST               1 (out)

741           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               1 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('services')
              BINARY_OP               11 (/)
              LOAD_CONST               3 ('security')
              BINARY_OP               11 (/)
              LOAD_CONST               4 ('rate_limit_store.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

742           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               5 ('')
      L1:     STORE_FAST               3 (src)

743           LOAD_CONST               6 ('rate_limit_store_process_local')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)
              STORE_FAST               4 (ok)

744           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

745           LOAD_CONST               7 ('carry_forward:process_local_fallback')

746           LOAD_FAST_BORROW         4 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               8 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               9 ('FAIL')

747   L3:     LOAD_CONST              10 ('PAS-SECURITY-02 process-local fallback marker still present')

744           CALL                     3
              CALL                     1
              POP_TOP

749           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114E40, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 752>:
752           RESUME                   0
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

Disassembly of <code object check_self_no_env_or_db at 0x0000018C17D893A0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 752>:
752            RESUME                   0

753            BUILD_LIST               0
               STORE_FAST               1 (out)

754            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_GLOBAL              2 (__file__)
               CALL                     1
               LOAD_ATTR                5 (resolve + NULL|self)
               CALL                     0
               STORE_FAST               2 (self_path)

755            LOAD_GLOBAL              7 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (self_path)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L1:     STORE_FAST               3 (src)

756            LOAD_GLOBAL              9 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               4 (executable)

757            BUILD_LIST               0
               STORE_FAST               5 (bad)

758            LOAD_FAST_BORROW         4 (executable)
               LOAD_ATTR               11 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L2:     FOR_ITER               199 (to L9)
               STORE_FAST               6 (raw_line)

759            LOAD_FAST_BORROW         6 (raw_line)
               LOAD_ATTR               13 (strip + NULL|self)
               CALL                     0
               STORE_FAST               7 (stripped)

760            LOAD_FAST_BORROW         7 (stripped)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN

761            JUMP_BACKWARD           29 (to L2)

762    L3:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              15 (('import dotenv', 'from dotenv'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L4)
               NOT_TAKEN

763            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               1 ('dotenv import')
               CALL                     1
               POP_TOP

764    L4:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              16 (('import supabase', 'from supabase'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L5)
               NOT_TAKEN

765            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               2 ('supabase import')
               CALL                     1
               POP_TOP

766    L5:     LOAD_CONST               3 ('load_dotenv()')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       18 (to L6)
               NOT_TAKEN

767            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               4 ('load_dotenv() call')
               CALL                     1
               POP_TOP

768    L6:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              17 (('os.environ[', 'getenv('))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L7)
               NOT_TAKEN

769            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               5 ('environ read')
               CALL                     1
               POP_TOP

770    L7:     LOAD_CONST               6 ('get_supabase')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD          182 (to L2)

771    L8:     LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               7 ('supabase client call')
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          201 (to L2)

758    L9:     END_FOR
               POP_ITER

772            LOAD_FAST                1 (out)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_GLOBAL             19 (_check + NULL)

773            LOAD_CONST               8 ('self_check:no_env_or_db')

774            LOAD_FAST_BORROW         5 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST               9 ('FAIL')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST              10 ('PASS')

775   L11:     LOAD_CONST              11 ('PAS-SECURITY-03 readiness checker never reads .env / touches DB')

776            LOAD_FAST_BORROW         5 (bad)
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

772   L13:     LOAD_CONST              14 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

778            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114F30, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 785>:
785           RESUME                   0
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

Disassembly of <code object _aggregate at 0x0000018C1800B230, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 785>:
 785            RESUME                   0

 787            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 786            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2

 787    L2:     FOR_ITER                49 (to L7)
                STORE_FAST               1 (c)

 788            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 787    L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L2)

 788    L4:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              2 (SEVERITY_BLOCK)
                COMPARE_OP              88 (bool(==))

 787    L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L2)
        L6:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L2)
        L7:     END_FOR
                POP_ITER

 786    L8:     STORE_FAST               2 (blockers)
                STORE_FAST               1 (c)

 791            LOAD_CONST               3 ('verdict')
                LOAD_FAST_BORROW         2 (blockers)
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L9)
                NOT_TAKEN
                LOAD_GLOBAL              4 (VERDICT_NOT_READY)
                JUMP_FORWARD             5 (to L10)
        L9:     LOAD_GLOBAL              6 (VERDICT_READY)

 792   L10:     LOAD_CONST               4 ('blockers')
                LOAD_FAST_BORROW         2 (blockers)

 793            LOAD_CONST               5 ('info')
                BUILD_LIST               0

 790            BUILD_MAP                3
                RETURN_VALUE

  --   L11:     SWAP                     2
                POP_TOP

 786            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L11 [2]
  L4 to L5 -> L11 [2]
  L6 to L8 -> L11 [2]

Disassembly of <code object __annotate__ at 0x0000018C18115020, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 797>:
797           RESUME                   0
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

Disassembly of <code object _operator_actions at 0x0000018C18048E30, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 797>:
797           RESUME                   0

798           BUILD_LIST               0
              STORE_FAST               1 (out)

799           LOAD_FAST_BORROW         0 (checks)
              GET_ITER
      L1:     FOR_ITER               109 (to L5)
              STORE_FAST               2 (c)

800           LOAD_FAST_BORROW         2 (c)
              LOAD_CONST               0 ('status')
              BINARY_OP               26 ([])
              LOAD_CONST               1 ('FAIL')
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

801           JUMP_BACKWARD           19 (to L1)

802   L2:     LOAD_FAST_BORROW         2 (c)
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

803           LOAD_FAST                1 (out)
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

799   L5:     END_FOR
              POP_ITER

804           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114030, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 807>:
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
              LOAD_CONST               4 ('dict')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object evaluate at 0x0000018C17D7CA90, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 807>:
807           RESUME                   0

808           BUILD_LIST               0
              STORE_FAST               1 (checks)

809           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              3 (check_files_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

810           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              5 (check_prior_phases_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

811           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              7 (check_memory_review_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

812           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              9 (check_worker_off_by_default + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

813           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             11 (check_v33_sql + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

814           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             13 (check_rpc_service + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

815           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             15 (check_admin_rate_limit_wired + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

816           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             17 (check_webhook_rate_limit_wired + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

817           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             19 (check_ci_gate_script + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

818           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             21 (check_no_raw_key_storage + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

819           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             23 (check_key_delivery_doctrine_doc + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

820           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             25 (check_waf_baseline_doc + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

821           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             27 (check_pas_security_03_doctrine_doc + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

822           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             29 (check_audit_service_invariant + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

823           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             31 (check_event_contract + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

824           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             33 (check_no_forbidden_imports + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

825           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             35 (check_no_inbox_scan_tokens + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

826           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             37 (check_pas_security_02_carry_forward + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

827           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             39 (check_self_no_env_or_db + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

829           LOAD_GLOBAL             41 (_aggregate + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1
              STORE_FAST               2 (agg)

831           LOAD_CONST               0 ('phase')
              LOAD_CONST               1 ('PAS-SECURITY-03')

832           LOAD_CONST               2 ('generated_at')
              LOAD_GLOBAL             43 (_now_iso + NULL)
              CALL                     0

833           LOAD_CONST               3 ('verdict')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])

834           LOAD_CONST               4 ('ready')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])
              LOAD_GLOBAL             44 (VERDICT_READY)
              COMPARE_OP              72 (==)

835           LOAD_CONST               5 ('blocker_count')
              LOAD_GLOBAL             47 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               6 ('blockers')
              BINARY_OP               26 ([])
              CALL                     1

836           LOAD_CONST               7 ('info_count')
              LOAD_GLOBAL             47 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               8 ('info')
              BINARY_OP               26 ([])
              CALL                     1

837           LOAD_CONST               9 ('check_count')
              LOAD_GLOBAL             47 (len + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

838           LOAD_CONST              10 ('pass_count')
              LOAD_GLOBAL             49 (sum + NULL)
              LOAD_CONST              11 (<code object <genexpr> at 0x0000018C18053870, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 838>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

839           LOAD_CONST              12 ('fail_count')
              LOAD_GLOBAL             49 (sum + NULL)
              LOAD_CONST              13 (<code object <genexpr> at 0x0000018C180531B0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 839>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

840           LOAD_CONST              14 ('checks')
              LOAD_FAST_BORROW         1 (checks)

841           LOAD_CONST              15 ('operator_actions')
              LOAD_GLOBAL             51 (_operator_actions + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

830           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18053870, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 838>:
 838           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C180531B0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 839>:
 839           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C181156B0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 848>:
848           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C181285D0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 848>:
848           RESUME                   0

849           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

850           LOAD_CONST               0 ('pas_security_03_admin_webhook_ci_readiness_check')

852           LOAD_CONST               1 ('PAS-SECURITY-03 — Evaluate admin/webhook rate-limit wiring + atomic counter RPC + CI scanner gate + API-key delivery doctrine + WAF baseline. Read-only — never reads .env, never touches Supabase, never runs a migration.')

849           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

859           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               3 ('--repo-root')
              LOAD_GLOBAL              6 (_REPO_ROOT_DEFAULT)
              LOAD_CONST               4 (('default',))
              CALL_KW                  2
              POP_TOP

860           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               5 ('--output')
              LOAD_GLOBAL              8 (REPORT_FILENAME)
              LOAD_CONST               4 (('default',))
              CALL_KW                  2
              POP_TOP

861           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               6 ('--json')
              LOAD_CONST               7 ('store_true')
              LOAD_CONST               8 (('action',))
              CALL_KW                  2
              POP_TOP

862           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               9 ('--summary-only')
              LOAD_CONST               7 ('store_true')
              LOAD_CONST               8 (('action',))
              CALL_KW                  2
              POP_TOP

863           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST              10 ('--strict')
              LOAD_CONST               7 ('store_true')
              LOAD_CONST               8 (('action',))
              CALL_KW                  2
              POP_TOP

864           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181152F0, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 867>:
867           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C17D8CD10, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 867>:
867           RESUME                   0

868           LOAD_GLOBAL              1 (print + NULL)

869           LOAD_CONST               0 ('[PAS-SECURITY-03] verdict=')
              LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               1 ('verdict')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               2 (' blockers=')

870           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               3 ('blocker_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' info=')

871           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               5 ('info_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' checks=')

872           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               7 ('check_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' pass=')

873           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               9 ('pass_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              10 (' fail=')

874           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              11 ('fail_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE

869           BUILD_STRING            12

868           CALL                     1
              POP_TOP

876           LOAD_FAST_BORROW         0 (report)
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

877           LOAD_FAST_BORROW         1 (actions)
              TO_BOOL
              POP_JUMP_IF_FALSE       93 (to L5)
              NOT_TAKEN

878           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              13 ('[PAS-SECURITY-03] operator actions:')
              CALL                     1
              POP_TOP

879           LOAD_FAST_BORROW         1 (actions)
              LOAD_CONST              14 (slice(None, 25, None))
              BINARY_OP               26 ([])
              GET_ITER
      L2:     FOR_ITER                17 (to L3)
              STORE_FAST               2 (a)

880           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              15 ('  - ')
              LOAD_FAST_BORROW         2 (a)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L2)

879   L3:     END_FOR
              POP_ITER

881           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         1 (actions)
              CALL                     1
              LOAD_SMALL_INT          25
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       34 (to L4)
              NOT_TAKEN

882           LOAD_GLOBAL              1 (print + NULL)
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

881   L4:     LOAD_CONST              18 (None)
              RETURN_VALUE

877   L5:     LOAD_CONST              18 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026630, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 885>:
885           RESUME                   0
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

Disassembly of <code object _write_report at 0x0000018C18128B70, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 885>:
 885           RESUME                   0

 886           NOP

 887   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

 888           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

 889           LOAD_CONST               3 ('utf-8')

 887           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 891           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

 892   L4:     LOAD_GLOBAL             11 (print + NULL)

 893           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

 894           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

 893           BUILD_STRING             4

 895           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

 892           LOAD_CONST               7 (('file',))
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

 891   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18115C50, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 899>:
899           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17D89750, file "scripts/pas_security_03_admin_webhook_ci_readiness_check.py", line 899>:
 899            RESUME                   0

 900            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 901            NOP

 902    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 906    L2:     LOAD_GLOBAL             10 (os)
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

 907            LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               21 (isdir + NULL|self)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L4)
                NOT_TAKEN

 908            LOAD_GLOBAL             23 (print + NULL)
                LOAD_CONST               2 ('error: --repo-root not a directory: ')
                LOAD_FAST                4 (repo_root)
                FORMAT_SIMPLE
                BUILD_STRING             2
                LOAD_GLOBAL             24 (sys)
                LOAD_ATTR               26 (stderr)
                LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

 909            LOAD_SMALL_INT           2
                RETURN_VALUE

 911    L4:     LOAD_GLOBAL             29 (evaluate + NULL)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                STORE_FAST               5 (report)

 913            LOAD_FAST                2 (args)
                LOAD_ATTR               30 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L5)
                NOT_TAKEN

 914            LOAD_GLOBAL             33 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               34 (output)
                LOAD_FAST                5 (report)
                CALL                     2
                POP_TOP

 916    L5:     LOAD_GLOBAL             37 (_print_summary + NULL)
                LOAD_FAST                5 (report)
                CALL                     1
                POP_TOP

 918            LOAD_FAST                2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L6)
                NOT_TAKEN

 919            LOAD_GLOBAL             23 (print + NULL)
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

 921    L6:     LOAD_FAST                5 (report)
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

 903            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L17)
                NOT_TAKEN
                STORE_FAST               3 (e)

 904    L9:     LOAD_FAST                3 (e)
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

 903   L17:     RERAISE                  0

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
