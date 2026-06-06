# scripts_readiness/pas175_audit_integrity_readiness_check

- **pyc:** `scripts\__pycache__\pas175_audit_integrity_readiness_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/pas175_audit_integrity_readiness_check.py`
- **co_filename (from bytecode):** `scripts\pas175_audit_integrity_readiness_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS175 — Audit integrity + tenant audit visibility readiness gate.

Deterministic, non-mutating evaluator for "is PAS175 wired
correctly and free of regressions in the PAS160-PAS174
doctrine?".

Walks the repo and verifies:

  * PAS160-PAS174 readiness scripts still exist.
  * PAS175 surfaces exist:
      - scripts/migrate_v23_audit_hash_chain.sql
      - app/services/operator/audit_integrity.py
      - scripts/reap_operator_audit_log.py
      - scripts/pas175_audit_integrity_readiness_check.py
      - docs/pas175_audit_integrity_and_tenant_audit_visibility.md
      - tests/mvp/test_pas175_audit_integrity.py
  * v23 SQL carries PROPOSAL ONLY + DO NOT EXECUTE + the
    aged_delete policy + the hash-chain column ADDs.
  * audit_integrity exposes the documented surface
    (compute_row_hash / compute_chain_head / verify_audit_chain).
  * audit_service.log_operator_action writes prev_hash +
    row_hash (the chain integration point).
  * audit_service still has NO update / delete helpers (PAS174
    invariant carried).
  * reap_operator_audit_log script defaults dry-run AND clamps
    to a 60-day script-side floor.
  * tenant_portal.py exposes /tenant/audit, is GET-only, and
    uses require_brokerage (X-API-Key) auth.
  * tenant_visibility_service exposes tenant_audit_history.
  * operator_actions allow-list extends to the three new
    bounded actions.
  * No Gmail / Google / OAuth / IMAP / POP3 / inbox-scan /
    Memory Review / embedding / vector / Composio / TrustClaw
    / OpenAI / Anthropic imports in any PAS175 file.
  * Memory Review (PAS147-PAS158) untouched.
  * Event contract registers every PAS175 event type.
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

`__annotate__`, `_aggregate`, `_build_parser`, `_check`, `_now_iso`, `_operator_actions`, `_print_summary`, `_read_text`, `_strip_python_comments_and_strings`, `_write_report`, `check_audit_integrity`, `check_audit_service_hash_wiring`, `check_doc_required_clauses`, `check_event_contract`, `check_files_present`, `check_memory_review_intact`, `check_no_forbidden_imports`, `check_no_inbox_scan_tokens`, `check_no_startup_worker`, `check_operator_actions_pas175`, `check_prior_phases_intact`, `check_reaper`, `check_self_no_env_or_db`, `check_tenant_audit_route`, `check_tenant_visibility_audit`, `check_v23_sql`, `check_worker_off_by_default`, `evaluate`, `main`

## Env-key candidates

`BLOCK`, `FAIL`, `INFO`, `NOT_READY`, `PAS175`, `PASS`, `READY`

## String constants (redacted where noted)

- '\nPAS175 — Audit integrity + tenant audit visibility readiness gate.\n\nDeterministic, non-mutating evaluator for "is PAS175 wired\ncorrectly and free of regressions in the PAS160-PAS174\ndoctrine?".\n\nWalks the repo and verifies:\n\n  * PAS160-PAS174 readiness scripts still exist.\n  * PAS175 surfaces exist:\n      - scripts/migrate_v23_audit_hash_chain.sql\n      - app/services/operator/audit_integrity.py\n      - scripts/reap_operator_audit_log.py\n      - scripts/pas175_audit_integrity_readiness_check.py\n      - docs/pas175_audit_integrity_and_tenant_audit_visibility.md\n      - tests/mvp/test_pas175_audit_integrity.py\n  * v23 SQL carries PROPOSAL ONLY + DO NOT EXECUTE + the\n    aged_delete policy + the hash-chain column ADDs.\n  * audit_integrity exposes the documented surface\n    (compute_row_hash / compute_chain_head / verify_audit_chain).\n  * audit_service.log_operator_action writes prev_hash +\n    row_hash (the chain integration point).\n  * audit_service still has NO update / delete helpers (PAS174\n    invariant carried).\n  * reap_operator_audit_log script defaults dry-run AND clamps\n    to a 60-day script-side floor.\n  * tenant_portal.py exposes /tenant/audit, is GET-only, and\n    uses require_brokerage (X-API-Key) auth.\n  * tenant_visibility_service exposes tenant_audit_history.\n  * operator_actions allow-list extends to the three new\n    bounded actions.\n  * No Gmail / Google / OAuth / IMAP / POP3 / inbox-scan /\n    Memory Review / embedding / vector / Composio / TrustClaw\n    / OpenAI / Anthropic imports in any PAS175 file.\n  * Memory Review (PAS147-PAS158) untouched.\n  * Event contract registers every PAS175 event type.\n  * Worker still OFF by default; FastAPI lifespan does not\n    auto-start the worker.\n  * Supports --summary-only / --json.\n  * Exits 0 ready, 1 blockers, 2 bad args.\n  * Never reads .env.\n  * Never touches production data.\n'
- 'utf-8'
- 'READY'
- 'NOT_READY'
- 'BLOCK'
- 'INFO'
- 'severity'
- 'detail'
- 'pas175_audit_integrity_readiness_report.json'
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
- 'Required PAS175 file present: '
- 'missing'
- 'prior_phase:'
- 'Prior-phase readiness script intact: '
- 'missing — PAS175 must not delete'
- 'memory_review:'
- 'Memory Review file present: '
- 'Memory Review file deleted — PAS175 must not touch'
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
- 'audit_integrity.py'
- 'audit_integrity:'
- 'Audit integrity token: '
- 'missing token '
- 'audit_service.py'
- 'audit_service_hash:'
- 'Audit service hash-wiring token: '
- 'audit_service:append_only_invariant_carried'
- 'Audit service still has no UPDATE / DELETE mutation helpers (PAS174 invariant)'
- 'scripts'
- 'reap_operator_audit_log.py'
- 'reaper:'
- 'Audit reaper token: '
- '_MIN_OLDER_THAN_DAYS     = 60'
- '_MIN_OLDER_THAN_DAYS = 60'
- 'reaper:60_day_floor'
- 'Audit reaper script clamps minimum age to 60 days'
- 'missing _MIN_OLDER_THAN_DAYS = 60 literal'
- 'routes'
- 'tenant_portal.py'
- 'tenant_audit_route:'
- 'Tenant audit route token: '
- 'tenant_audit_route:read_only'
- 'Tenant /audit route is read-only (no POST/PATCH/DELETE/PUT)'
- 'tenant'
- 'tenant_visibility_service.py'
- 'tenant_visibility_audit:'
- 'Tenant visibility audit token: '
- 'operator_actions.py'
- 'operator_actions_pas175:'
- 'Operator actions PAS175 token: '
- 'migrate_v23_audit_hash_chain.sql'
- 'proposal only'
- 'v23_sql:proposal_only'
- "v23 SQL carries 'PROPOSAL ONLY' guardrail"
- "missing 'PROPOSAL ONLY' label"
- 'do not execute'
- 'v23_sql:do_not_execute'
- "v23 SQL carries 'DO NOT EXECUTE' trailer"
- 'missing trailer'
- 'ADD COLUMN IF NOT EXISTS prev_hash text'
- 'ADD COLUMN IF NOT EXISTS row_hash'
- 'v23_sql:hash_chain_columns'
- 'v23 SQL adds prev_hash and row_hash columns'
- 'missing column ADDs'
- '[0-9a-f]{64}'
- 'v23_sql:hash_shape_check'
- 'v23 SQL pins prev_hash / row_hash to sha256 hex shape'
- 'missing sha256 shape CHECK'
- 'pas_operator_actions_log_service_role_aged_delete'
- "now() - interval '30 days'"
- 'v23_sql:aged_delete_policy'
- 'v23 SQL introduces aged-DELETE policy with 30-day floor'
- "expected pas_operator_actions_log_service_role_aged_delete policy + 'now() - interval 30 days' clause"
- 'pas_operator_actions_log_tenant_no_delete'
- 'v23_sql:tenant_delete_forbidden'
- 'v23 SQL keeps tenant DELETE forbidden'
- 'missing tenant-delete denial'
- 'events'
- 'contract.py'
- 'events:'
- 'Event contract registers '
- 'missing event type '
- 'app/services/operator/audit_integrity.py'
- 'forbidden_import:'
- 'No forbidden imports: '
- 'forbidden import prefixes: '
- 'no_inbox_scan:'
- 'No inbox-scanning tokens: '
- 'inbox-scan tokens present: '
- 'docs'
- 'pas175_audit_integrity_and_tenant_audit_visibility.md'
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
- 'PAS175 readiness checker never reads .env / touches DB'
- 'disqualifying patterns: '
- 'checks'
- 'verdict'
- 'blockers'
- 'info'
- 'List[str]'
- ' — '
- 'see report'
- 'phase'
- 'PAS175'
- 'generated_at'
- 'ready'
- 'blocker_count'
- 'info_count'
- 'check_count'
- 'pass_count'
- 'fail_count'
- 'operator_actions'
- 'argparse.ArgumentParser'
- 'pas175_audit_integrity_readiness_check'
- 'PAS175 — Evaluate audit integrity + tenant audit visibility surfaces. Read-only — never reads .env, never touches Supabase, never runs a migration.'
- '--repo-root'
- 'Repo root (default: parent of this script).'
- '--output'
- 'Where to write the JSON report (default ./'
- '--json'
- 'store_true'
- 'Emit JSON on stdout in addition to the summary.'
- '--summary-only'
- 'Skip writing the JSON report file.'
- '--strict'
- 'Exit 1 unless verdict == READY (default policy is the same).'
- 'report'
- 'None'
- '[PAS175] verdict='
- ' blockers='
- ' info='
- ' checks='
- ' pass='
- ' fail='
- '[PAS175] operator actions:'
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

   1           LOAD_CONST               0 ('\nPAS175 — Audit integrity + tenant audit visibility readiness gate.\n\nDeterministic, non-mutating evaluator for "is PAS175 wired\ncorrectly and free of regressions in the PAS160-PAS174\ndoctrine?".\n\nWalks the repo and verifies:\n\n  * PAS160-PAS174 readiness scripts still exist.\n  * PAS175 surfaces exist:\n      - scripts/migrate_v23_audit_hash_chain.sql\n      - app/services/operator/audit_integrity.py\n      - scripts/reap_operator_audit_log.py\n      - scripts/pas175_audit_integrity_readiness_check.py\n      - docs/pas175_audit_integrity_and_tenant_audit_visibility.md\n      - tests/mvp/test_pas175_audit_integrity.py\n  * v23 SQL carries PROPOSAL ONLY + DO NOT EXECUTE + the\n    aged_delete policy + the hash-chain column ADDs.\n  * audit_integrity exposes the documented surface\n    (compute_row_hash / compute_chain_head / verify_audit_chain).\n  * audit_service.log_operator_action writes prev_hash +\n    row_hash (the chain integration point).\n  * audit_service still has NO update / delete helpers (PAS174\n    invariant carried).\n  * reap_operator_audit_log script defaults dry-run AND clamps\n    to a 60-day script-side floor.\n  * tenant_portal.py exposes /tenant/audit, is GET-only, and\n    uses require_brokerage (X-API-Key) auth.\n  * tenant_visibility_service exposes tenant_audit_history.\n  * operator_actions allow-list extends to the three new\n    bounded actions.\n  * No Gmail / Google / OAuth / IMAP / POP3 / inbox-scan /\n    Memory Review / embedding / vector / Composio / TrustClaw\n    / OpenAI / Anthropic imports in any PAS175 file.\n  * Memory Review (PAS147-PAS158) untouched.\n  * Event contract registers every PAS175 event type.\n  * Worker still OFF by default; FastAPI lifespan does not\n    auto-start the worker.\n  * Supports --summary-only / --json.\n  * Exits 0 ready, 1 blockers, 2 bad args.\n  * Never reads .env.\n  * Never touches production data.\n')
               STORE_NAME               0 (__doc__)

  46           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  48           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  49           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (json)
               STORE_NAME               4 (json)

  50           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (os)
               STORE_NAME               5 (os)

  51           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (sys)
               STORE_NAME               6 (sys)

  52           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              7 (datetime)
               IMPORT_FROM              7 (datetime)
               STORE_NAME               7 (datetime)
               IMPORT_FROM              8 (timezone)
               STORE_NAME               8 (timezone)
               POP_TOP

  53           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Path',))
               IMPORT_NAME              9 (pathlib)
               IMPORT_FROM             10 (Path)
               STORE_NAME              10 (Path)
               POP_TOP

  54           LOAD_SMALL_INT           0
               LOAD_CONST               5 (('List', 'Optional'))
               IMPORT_NAME             11 (typing)
               IMPORT_FROM             12 (List)
               STORE_NAME              12 (List)
               IMPORT_FROM             13 (Optional)
               STORE_NAME              13 (Optional)
               POP_TOP

  57           LOAD_NAME                6 (sys)
               LOAD_ATTR               28 (stdout)
               LOAD_NAME                6 (sys)
               LOAD_ATTR               30 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              16 (_stream)

  58           NOP

  59   L2:     LOAD_NAME               16 (_stream)
               LOAD_ATTR               35 (reconfigure + NULL|self)
               LOAD_CONST               6 ('utf-8')
               LOAD_CONST               7 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  57   L4:     END_FOR
               POP_ITER

  64           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               41 (abspath + NULL|self)

  65           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               43 (join + NULL|self)
               LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               45 (dirname + NULL|self)
               LOAD_NAME               23 (__file__)
               CALL                     1
               LOAD_CONST               8 ('..')
               CALL                     2

  64           CALL                     1
               STORE_NAME              24 (_REPO_ROOT_DEFAULT)

  69           LOAD_CONST               9 ('READY')
               STORE_NAME              25 (VERDICT_READY)

  70           LOAD_CONST              10 ('NOT_READY')
               STORE_NAME              26 (VERDICT_NOT_READY)

  72           LOAD_CONST              11 ('BLOCK')
               STORE_NAME              27 (SEVERITY_BLOCK)

  73           LOAD_CONST              12 ('INFO')
               STORE_NAME              28 (SEVERITY_INFO)

  80           LOAD_CONST              74 (('scripts/migrate_v23_audit_hash_chain.sql', 'app/services/operator/audit_integrity.py', 'scripts/reap_operator_audit_log.py', 'scripts/pas175_audit_integrity_readiness_check.py', 'docs/pas175_audit_integrity_and_tenant_audit_visibility.md', 'tests/mvp/test_pas175_audit_integrity.py'))
               STORE_NAME              29 (REQUIRED_FILES)

  89           LOAD_CONST              75 (('scripts/pas160_mvp_sequence_check.py', 'scripts/pas161_lead_ingestion_readiness_check.py', 'scripts/pas162_pending_calls_readiness_check.py', 'scripts/pas163_candidate_pipeline_readiness_check.py', 'scripts/pas164_email_ingestion_readiness_check.py', 'scripts/pas165_email_auth_dedupe_readiness_check.py', 'scripts/pas166_email_dedupe_policy_readiness_check.py', 'scripts/pas167_email_secret_reaper_readiness_check.py', 'scripts/pas168_email_secret_rotation_readiness_check.py', 'scripts/pas169_crypto_roundtrip_check.py', 'scripts/pas169_launch_readiness_check.py', 'scripts/pas_launch_integrity_check.py', 'scripts/pas170_operator_survival_readiness_check.py', 'scripts/pas171_external_pilot_readiness_check.py', 'scripts/pas172_pilot_operations_readiness_check.py', 'scripts/pas173_brokerage_operator_readiness_check.py', 'scripts/pas174_operator_audit_readiness_check.py'))
               STORE_NAME              30 (PRIOR_PHASE_FILES)

 109           LOAD_CONST              76 (('app/services/memory/review.py', 'app/services/memory/review_stats.py', 'app/services/memory/review_export.py', 'app/services/memory/review_actors.py', 'app/services/memory/review_alerts.py', 'app/services/memory/operator_console.py'))
               STORE_NAME              31 (MEMORY_REVIEW_FILES)

 119           LOAD_CONST              77 (('def compute_row_hash(', 'def compute_chain_head(', 'def verify_audit_chain(', 'GENESIS_HASH', '_HASH_FIELDS', '_METADATA_ALLOW_LIST'))
               STORE_NAME              32 (REQUIRED_AUDIT_INTEGRITY_TOKENS)

 128           LOAD_CONST              78 (('prev_hash', 'row_hash', '_read_chain_head_safe', 'compute_row_hash'))
               STORE_NAME              33 (REQUIRED_AUDIT_SERVICE_HASH_TOKENS)

 137           LOAD_CONST              79 (('def update_audit_', 'def delete_audit_', 'def update_operator_audit_', 'def delete_operator_audit_', 'def mutate_audit_', 'def truncate_audit_', '.update(', '.delete('))
               STORE_NAME              34 (FORBIDDEN_AUDIT_MUTATION_TOKENS)

 148           LOAD_CONST              80 (('def reap(', '--execute', '--older-than-days', '--limit', 'dry_run:         bool = True', '_DEFAULT_OLDER_THAN_DAYS', '_MIN_OLDER_THAN_DAYS', '_MAX_OLDER_THAN_DAYS', '_HARD_CAP_LIMIT', 'audit_store_unavailable'))
               STORE_NAME              35 (REQUIRED_REAPER_TOKENS)

 161           LOAD_CONST              81 (('@router.get("/audit")', 'tenant_audit_history', 'require_brokerage'))
               STORE_NAME              36 (REQUIRED_TENANT_AUDIT_TOKENS)

 167           LOAD_CONST              82 (('def tenant_audit_history(', '_TENANT_AUDIT_FIELDS_SOURCE', '_TENANT_AUDIT_METADATA_KEYS', '_TENANT_AUDIT_FIELD_RENAME', 'entry_id'))
               STORE_NAME              37 (REQUIRED_TENANT_VISIBILITY_AUDIT_TOKENS)

 175           LOAD_CONST              83 (('request_readiness_email', 'rotate_brokerage_api_key', 'mark_pilot_stage_with_evidence', '_handle_request_readiness_email', '_handle_rotate_brokerage_api_key', '_handle_mark_pilot_stage_with_evidence', 'pas175_rotation_proposal_only', 'pas175_request_only_no_email_sent'))
               STORE_NAME              38 (REQUIRED_OPERATOR_ACTIONS_PAS175_TOKENS)

 187           LOAD_CONST              84 (('operator.audit.logged', 'audit.chain.verified', 'audit.chain.broken', 'audit.reaper.executed', 'tenant.audit.requested', 'operator.action.readiness_email_requested', 'operator.action.rotation_requested', 'operator.action.pilot_stage_evidenced'))
               STORE_NAME              39 (REQUIRED_EVENT_TYPES)

 201           LOAD_CONST              85 (('import gmail', 'from gmail', 'import googleapiclient', 'from googleapiclient', 'import google.oauth2', 'from google.oauth2', 'from google.auth', 'import google.auth', 'from google_auth_oauthlib', 'import imaplib', 'from imaplib', 'import poplib', 'from poplib', 'import composio', 'from composio', 'import trustclaw', 'from trustclaw', 'import chromadb', 'from chromadb', 'import pinecone', 'from pinecone', 'import langchain', 'from langchain', 'import faiss', 'import pgvector', 'from pgvector', 'from openai import embeddings', 'from openai.embeddings', 'from app.services.memory', 'import app.services.memory', 'from anthropic', 'import anthropic', 'from openai', 'import openai'))
               STORE_NAME              40 (FORBIDDEN_IMPORT_LINE_PREFIXES)

 226           LOAD_CONST              86 (('imaplib', 'poplib', 'fetch_inbox', 'gmail_oauth', 'gmail_token', 'users().messages'))
               STORE_NAME              41 (FORBIDDEN_INBOX_TOKENS)

 240           LOAD_CONST              13 ('severity')

 242           LOAD_NAME               27 (SEVERITY_BLOCK)

 240           LOAD_CONST              14 ('detail')

 242           LOAD_CONST              15 ('')

 240           BUILD_MAP                2
               LOAD_CONST              16 (<code object __annotate__ at 0x0000018C18026530, file "scripts\pas175_audit_integrity_readiness_check.py", line 240>)
               MAKE_FUNCTION
               LOAD_CONST              17 (<code object _check at 0x0000018C17FA3B40, file "scripts\pas175_audit_integrity_readiness_check.py", line 240>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              42 (_check)

 253           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA34B0, file "scripts\pas175_audit_integrity_readiness_check.py", line 253>)
               MAKE_FUNCTION
               LOAD_CONST              19 (<code object _now_iso at 0x0000018C18038670, file "scripts\pas175_audit_integrity_readiness_check.py", line 253>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              43 (_now_iso)

 257           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA3A50, file "scripts\pas175_audit_integrity_readiness_check.py", line 257>)
               MAKE_FUNCTION
               LOAD_CONST              21 (<code object _read_text at 0x0000018C18053CF0, file "scripts\pas175_audit_integrity_readiness_check.py", line 257>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              44 (_read_text)

 264           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA31E0, file "scripts\pas175_audit_integrity_readiness_check.py", line 264>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object _strip_python_comments_and_strings at 0x0000018C17D81580, file "scripts\pas175_audit_integrity_readiness_check.py", line 264>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              45 (_strip_python_comments_and_strings)

 303           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA3E10, file "scripts\pas175_audit_integrity_readiness_check.py", line 303>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object check_files_present at 0x0000018C18061470, file "scripts\pas175_audit_integrity_readiness_check.py", line 303>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              46 (check_files_present)

 317           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA3960, file "scripts\pas175_audit_integrity_readiness_check.py", line 317>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object check_prior_phases_intact at 0x0000018C180606F0, file "scripts\pas175_audit_integrity_readiness_check.py", line 317>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              47 (check_prior_phases_intact)

 331           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA3C30, file "scripts\pas175_audit_integrity_readiness_check.py", line 331>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object check_memory_review_intact at 0x0000018C18061110, file "scripts\pas175_audit_integrity_readiness_check.py", line 331>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              48 (check_memory_review_intact)

 345           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C18114120, file "scripts\pas175_audit_integrity_readiness_check.py", line 345>)
               MAKE_FUNCTION
               LOAD_CONST              31 (<code object check_worker_off_by_default at 0x0000018C1801C9E0, file "scripts\pas175_audit_integrity_readiness_check.py", line 345>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              49 (check_worker_off_by_default)

 363           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C18114210, file "scripts\pas175_audit_integrity_readiness_check.py", line 363>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object check_no_startup_worker at 0x0000018C17EA4280, file "scripts\pas175_audit_integrity_readiness_check.py", line 363>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              50 (check_no_startup_worker)

 387           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C181143F0, file "scripts\pas175_audit_integrity_readiness_check.py", line 387>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object check_audit_integrity at 0x0000018C17F001D0, file "scripts\pas175_audit_integrity_readiness_check.py", line 387>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              51 (check_audit_integrity)

 403           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C181144E0, file "scripts\pas175_audit_integrity_readiness_check.py", line 403>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object check_audit_service_hash_wiring at 0x0000018C17EDFE20, file "scripts\pas175_audit_integrity_readiness_check.py", line 403>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              52 (check_audit_service_hash_wiring)

 433           LOAD_CONST              38 (<code object __annotate__ at 0x0000018C181145D0, file "scripts\pas175_audit_integrity_readiness_check.py", line 433>)
               MAKE_FUNCTION
               LOAD_CONST              39 (<code object check_reaper at 0x0000018C17CC1CE0, file "scripts\pas175_audit_integrity_readiness_check.py", line 433>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              53 (check_reaper)

 458           LOAD_CONST              40 (<code object __annotate__ at 0x0000018C181147B0, file "scripts\pas175_audit_integrity_readiness_check.py", line 458>)
               MAKE_FUNCTION
               LOAD_CONST              41 (<code object check_tenant_audit_route at 0x0000018C17E577A0, file "scripts\pas175_audit_integrity_readiness_check.py", line 458>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              54 (check_tenant_audit_route)

 489           LOAD_CONST              42 (<code object __annotate__ at 0x0000018C181148A0, file "scripts\pas175_audit_integrity_readiness_check.py", line 489>)
               MAKE_FUNCTION
               LOAD_CONST              43 (<code object check_tenant_visibility_audit at 0x0000018C17F01460, file "scripts\pas175_audit_integrity_readiness_check.py", line 489>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              55 (check_tenant_visibility_audit)

 505           LOAD_CONST              44 (<code object __annotate__ at 0x0000018C18114990, file "scripts\pas175_audit_integrity_readiness_check.py", line 505>)
               MAKE_FUNCTION
               LOAD_CONST              45 (<code object check_operator_actions_pas175 at 0x0000018C17F003E0, file "scripts\pas175_audit_integrity_readiness_check.py", line 505>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              56 (check_operator_actions_pas175)

 521           LOAD_CONST              46 (<code object __annotate__ at 0x0000018C18114A80, file "scripts\pas175_audit_integrity_readiness_check.py", line 521>)
               MAKE_FUNCTION
               LOAD_CONST              47 (<code object check_v23_sql at 0x0000018C177883D0, file "scripts\pas175_audit_integrity_readiness_check.py", line 521>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              57 (check_v23_sql)

 590           LOAD_CONST              48 (<code object __annotate__ at 0x0000018C18114B70, file "scripts\pas175_audit_integrity_readiness_check.py", line 590>)
               MAKE_FUNCTION
               LOAD_CONST              49 (<code object check_event_contract at 0x0000018C17FED830, file "scripts\pas175_audit_integrity_readiness_check.py", line 590>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              58 (check_event_contract)

 606           LOAD_CONST              50 (<code object __annotate__ at 0x0000018C18114C60, file "scripts\pas175_audit_integrity_readiness_check.py", line 606>)
               MAKE_FUNCTION
               LOAD_CONST              51 (<code object check_no_forbidden_imports at 0x0000018C17D8BF50, file "scripts\pas175_audit_integrity_readiness_check.py", line 606>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              59 (check_no_forbidden_imports)

 637           LOAD_CONST              52 (<code object __annotate__ at 0x0000018C18114D50, file "scripts\pas175_audit_integrity_readiness_check.py", line 637>)
               MAKE_FUNCTION
               LOAD_CONST              53 (<code object check_no_inbox_scan_tokens at 0x0000018C17CD0F70, file "scripts\pas175_audit_integrity_readiness_check.py", line 637>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              60 (check_no_inbox_scan_tokens)

 665           LOAD_CONST              54 (<code object __annotate__ at 0x0000018C18114F30, file "scripts\pas175_audit_integrity_readiness_check.py", line 665>)
               MAKE_FUNCTION
               LOAD_CONST              55 (<code object check_doc_required_clauses at 0x0000018C17D8AF50, file "scripts\pas175_audit_integrity_readiness_check.py", line 665>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              61 (check_doc_required_clauses)

 700           LOAD_CONST              56 (<code object __annotate__ at 0x0000018C18115020, file "scripts\pas175_audit_integrity_readiness_check.py", line 700>)
               MAKE_FUNCTION
               LOAD_CONST              57 (<code object check_self_no_env_or_db at 0x0000018C17D88890, file "scripts\pas175_audit_integrity_readiness_check.py", line 700>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              62 (check_self_no_env_or_db)

 734           LOAD_CONST              58 (<code object __annotate__ at 0x0000018C18115110, file "scripts\pas175_audit_integrity_readiness_check.py", line 734>)
               MAKE_FUNCTION
               LOAD_CONST              59 (<code object _aggregate at 0x0000018C17EC4280, file "scripts\pas175_audit_integrity_readiness_check.py", line 734>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              63 (_aggregate)

 750           LOAD_CONST              60 (<code object __annotate__ at 0x0000018C18115200, file "scripts\pas175_audit_integrity_readiness_check.py", line 750>)
               MAKE_FUNCTION
               LOAD_CONST              61 (<code object _operator_actions at 0x0000018C18048C70, file "scripts\pas175_audit_integrity_readiness_check.py", line 750>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              64 (_operator_actions)

 760           LOAD_CONST              62 (<code object __annotate__ at 0x0000018C181152F0, file "scripts\pas175_audit_integrity_readiness_check.py", line 760>)
               MAKE_FUNCTION
               LOAD_CONST              63 (<code object evaluate at 0x0000018C17E93E60, file "scripts\pas175_audit_integrity_readiness_check.py", line 760>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              65 (evaluate)

 796           LOAD_CONST              64 ('pas175_audit_integrity_readiness_report.json')
               STORE_NAME              66 (REPORT_FILENAME)

 799           LOAD_CONST              65 (<code object __annotate__ at 0x0000018C181154D0, file "scripts\pas175_audit_integrity_readiness_check.py", line 799>)
               MAKE_FUNCTION
               LOAD_CONST              66 (<code object _build_parser at 0x0000018C1801C7F0, file "scripts\pas175_audit_integrity_readiness_check.py", line 799>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              67 (_build_parser)

 832           LOAD_CONST              67 (<code object __annotate__ at 0x0000018C181155C0, file "scripts\pas175_audit_integrity_readiness_check.py", line 832>)
               MAKE_FUNCTION
               LOAD_CONST              68 (<code object _print_summary at 0x0000018C17D8E300, file "scripts\pas175_audit_integrity_readiness_check.py", line 832>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              68 (_print_summary)

 850           LOAD_CONST              69 (<code object __annotate__ at 0x0000018C18024B30, file "scripts\pas175_audit_integrity_readiness_check.py", line 850>)
               MAKE_FUNCTION
               LOAD_CONST              70 (<code object _write_report at 0x0000018C180FC030, file "scripts\pas175_audit_integrity_readiness_check.py", line 850>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              69 (_write_report)

 864           LOAD_CONST              87 ((None,))
               LOAD_CONST              71 (<code object __annotate__ at 0x0000018C181156B0, file "scripts\pas175_audit_integrity_readiness_check.py", line 864>)
               MAKE_FUNCTION
               LOAD_CONST              72 (<code object main at 0x0000018C17D88FF0, file "scripts\pas175_audit_integrity_readiness_check.py", line 864>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              70 (main)

 892           LOAD_NAME               71 (__name__)
               LOAD_CONST              73 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 893           LOAD_NAME                6 (sys)
               LOAD_ATTR              144 (exit)
               PUSH_NULL
               LOAD_NAME               70 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 892   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  60           LOAD_NAME               18 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  61   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          361 (to L1)

  60   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026530, file "scripts\pas175_audit_integrity_readiness_check.py", line 240>:
240           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('check_id')

241           LOAD_CONST               2 ('str')

240           LOAD_CONST               3 ('status')

241           LOAD_CONST               2 ('str')

240           LOAD_CONST               4 ('label')

241           LOAD_CONST               2 ('str')

240           LOAD_CONST               5 ('severity')

242           LOAD_CONST               2 ('str')

240           LOAD_CONST               6 ('detail')

242           LOAD_CONST               2 ('str')

240           LOAD_CONST               7 ('return')

243           LOAD_CONST               8 ('dict')

240           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _check at 0x0000018C17FA3B40, file "scripts\pas175_audit_integrity_readiness_check.py", line 240>:
240           RESUME                   0

245           LOAD_CONST               0 ('id')
              LOAD_FAST_BORROW         0 (check_id)

246           LOAD_CONST               1 ('status')
              LOAD_FAST_BORROW         1 (status)

247           LOAD_CONST               2 ('label')
              LOAD_FAST_BORROW         2 (label)

248           LOAD_CONST               3 ('severity')
              LOAD_FAST_BORROW         3 (severity)

249           LOAD_CONST               4 ('detail')
              LOAD_FAST_BORROW         4 (detail)

244           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "scripts\pas175_audit_integrity_readiness_check.py", line 253>:
253           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038670, file "scripts\pas175_audit_integrity_readiness_check.py", line 253>:
253           RESUME                   0

254           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "scripts\pas175_audit_integrity_readiness_check.py", line 257>:
257           RESUME                   0
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

Disassembly of <code object _read_text at 0x0000018C18053CF0, file "scripts\pas175_audit_integrity_readiness_check.py", line 257>:
 257           RESUME                   0

 258           NOP

 259   L1:     LOAD_FAST_BORROW         0 (path)
               LOAD_ATTR                1 (read_text + NULL|self)
               LOAD_CONST               0 ('utf-8')
               LOAD_CONST               1 ('replace')
               LOAD_CONST               2 (('encoding', 'errors'))
               CALL_KW                  2
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 260           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 261   L4:     POP_EXCEPT
               LOAD_CONST               3 (None)
               RETURN_VALUE

 260   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "scripts\pas175_audit_integrity_readiness_check.py", line 264>:
264           RESUME                   0
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

Disassembly of <code object _strip_python_comments_and_strings at 0x0000018C17D81580, file "scripts\pas175_audit_integrity_readiness_check.py", line 264>:
264            RESUME                   0

265            BUILD_LIST               0
               STORE_FAST               1 (out)

266            LOAD_SMALL_INT           0
               LOAD_GLOBAL              1 (len + NULL)
               LOAD_FAST_BORROW         0 (src)
               CALL                     1
               STORE_FAST_STORE_FAST   50 (n, i)

267    L1:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (i, n)
               COMPARE_OP              18 (bool(<))
               EXTENDED_ARG             1
               POP_JUMP_IF_FALSE      282 (to L13)
               NOT_TAKEN

268            LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               BINARY_OP               26 ([])
               STORE_FAST               4 (ch)

269            LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               1 ('#')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       38 (to L3)
               NOT_TAKEN

270            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_CONST               2 ('\n')
               LOAD_FAST_BORROW         2 (i)
               CALL                     2
               STORE_FAST               5 (j)

271            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L2)
               NOT_TAKEN

272            JUMP_FORWARD           240 (to L13)

273    L2:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

274            JUMP_BACKWARD           59 (to L1)

275    L3:     LOAD_FAST_BORROW         0 (src)
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

276    L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               BINARY_SLICE
               STORE_FAST               6 (quote)

277            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 98 (quote, i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               CALL                     2
               STORE_FAST               7 (end)

278            LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L5)
               NOT_TAKEN

279            JUMP_FORWARD           138 (to L13)

280    L5:     LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

281            JUMP_BACKWARD          161 (to L1)

282    L6:     LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               7 (('"', "'"))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       92 (to L12)
               NOT_TAKEN

283            LOAD_FAST                4 (ch)
               STORE_FAST               6 (quote)

284            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               5 (j)

285    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (j, n)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       63 (to L11)
               NOT_TAKEN

286            LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
               BINARY_OP               26 ([])
               LOAD_CONST               5 ('\\')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       12 (to L8)
               NOT_TAKEN

287            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           2
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)

288            JUMP_BACKWARD           30 (to L7)

289    L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
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

290    L9:     JUMP_FORWARD            11 (to L11)

291   L10:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)
               JUMP_BACKWARD           68 (to L7)

292   L11:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

293            EXTENDED_ARG             1
               JUMP_BACKWARD          259 (to L1)

294   L12:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (ch)
               CALL                     1
               POP_TOP

295            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               2 (i)
               EXTENDED_ARG             1
               JUMP_BACKWARD          288 (to L1)

296   L13:     LOAD_CONST               6 ('')
               LOAD_ATTR                9 (join + NULL|self)
               LOAD_FAST_BORROW         1 (out)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "scripts\pas175_audit_integrity_readiness_check.py", line 303>:
303           RESUME                   0
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

Disassembly of <code object check_files_present at 0x0000018C18061470, file "scripts\pas175_audit_integrity_readiness_check.py", line 303>:
303           RESUME                   0

304           BUILD_LIST               0
              STORE_FAST               1 (out)

305           LOAD_GLOBAL              0 (REQUIRED_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

306           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

307           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

308           LOAD_CONST               0 ('file:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

309           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

310   L3:     LOAD_CONST               3 ('Required PAS175 file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

311           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

312           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing')

307   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

305   L6:     END_FOR
              POP_ITER

314           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "scripts\pas175_audit_integrity_readiness_check.py", line 317>:
317           RESUME                   0
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

Disassembly of <code object check_prior_phases_intact at 0x0000018C180606F0, file "scripts\pas175_audit_integrity_readiness_check.py", line 317>:
317           RESUME                   0

318           BUILD_LIST               0
              STORE_FAST               1 (out)

319           LOAD_GLOBAL              0 (PRIOR_PHASE_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

320           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

321           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

322           LOAD_CONST               0 ('prior_phase:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

323           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

324   L3:     LOAD_CONST               3 ('Prior-phase readiness script intact: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

325           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

326           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing — PAS175 must not delete')

321   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

319   L6:     END_FOR
              POP_ITER

328           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "scripts\pas175_audit_integrity_readiness_check.py", line 331>:
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

Disassembly of <code object check_memory_review_intact at 0x0000018C18061110, file "scripts\pas175_audit_integrity_readiness_check.py", line 331>:
331           RESUME                   0

332           BUILD_LIST               0
              STORE_FAST               1 (out)

333           LOAD_GLOBAL              0 (MEMORY_REVIEW_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

334           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

335           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

336           LOAD_CONST               0 ('memory_review:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

337           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

338   L3:     LOAD_CONST               3 ('Memory Review file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

339           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

340           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('Memory Review file deleted — PAS175 must not touch')

335   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

333   L6:     END_FOR
              POP_ITER

342           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114120, file "scripts\pas175_audit_integrity_readiness_check.py", line 345>:
345           RESUME                   0
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

Disassembly of <code object check_worker_off_by_default at 0x0000018C1801C9E0, file "scripts\pas175_audit_integrity_readiness_check.py", line 345>:
345           RESUME                   0

346           BUILD_LIST               0
              STORE_FAST               1 (out)

347           LOAD_GLOBAL              1 (Path + NULL)
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

348           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

350           LOAD_CONST               5 ('_ENV_FLAG_ENABLED_LITERAL = "true"')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         6 (to L2)
              NOT_TAKEN
              POP_TOP

351           LOAD_CONST               6 ("_ENV_FLAG_ENABLED_LITERAL = 'true'")
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)

349   L2:     STORE_FAST               4 (literal_ok)

353           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

354           LOAD_CONST               7 ('worker:off_by_default')

355           LOAD_FAST_BORROW         4 (literal_ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               8 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               9 ('FAIL')

356   L4:     LOAD_CONST              10 ('Pending-call worker is OFF by default')

357           LOAD_GLOBAL              8 (SEVERITY_BLOCK)

358           LOAD_FAST_BORROW         4 (literal_ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST              11 ('missing strict enable-literal constant')

353   L6:     LOAD_CONST              12 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP

360           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114210, file "scripts\pas175_audit_integrity_readiness_check.py", line 363>:
363           RESUME                   0
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

Disassembly of <code object check_no_startup_worker at 0x0000018C17EA4280, file "scripts\pas175_audit_integrity_readiness_check.py", line 363>:
363           RESUME                   0

364           BUILD_LIST               0
              STORE_FAST               1 (out)

365           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('main.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

366           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               2 ('')
      L1:     STORE_FAST               3 (src)

367           LOAD_GLOBAL              5 (_strip_python_comments_and_strings + NULL)
              LOAD_FAST_BORROW         3 (src)
              CALL                     1
              STORE_FAST               4 (executable)

368           BUILD_LIST               0
              STORE_FAST               5 (bad)

369           LOAD_CONST               3 ('from app.services.ingestion.worker')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L2)
              NOT_TAKEN

370           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               4 ('from app.services.ingestion.worker import …')
              CALL                     1
              POP_TOP

371   L2:     LOAD_CONST               5 ('import app.services.ingestion.worker')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L3)
              NOT_TAKEN

372           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               5 ('import app.services.ingestion.worker')
              CALL                     1
              POP_TOP

373   L3:     LOAD_CONST               6 ('run_worker_loop')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L4)
              NOT_TAKEN

374           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               7 ('run_worker_loop reference')
              CALL                     1
              POP_TOP

375   L4:     LOAD_CONST               8 ('process_pending_call(')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L5)
              NOT_TAKEN

376           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               9 ('process_pending_call call')
              CALL                     1
              POP_TOP

377   L5:     LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

378           LOAD_CONST              10 ('main:no_startup_worker')

379           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L6)
              NOT_TAKEN
              LOAD_CONST              11 ('FAIL')
              JUMP_FORWARD             1 (to L7)
      L6:     LOAD_CONST              12 ('PASS')

380   L7:     LOAD_CONST              13 ('FastAPI lifespan does not auto-start the pending-call worker')

381           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

382           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE       25 (to L8)
              NOT_TAKEN
              LOAD_CONST              14 ('disqualifying tokens: ')
              LOAD_CONST              15 (', ')
              LOAD_ATTR               13 (join + NULL|self)
              LOAD_FAST_BORROW         5 (bad)
              CALL                     1
              BINARY_OP                0 (+)
              JUMP_FORWARD             1 (to L9)
      L8:     LOAD_CONST               2 ('')

377   L9:     LOAD_CONST              16 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP

384           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181143F0, file "scripts\pas175_audit_integrity_readiness_check.py", line 387>:
387           RESUME                   0
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

Disassembly of <code object check_audit_integrity at 0x0000018C17F001D0, file "scripts\pas175_audit_integrity_readiness_check.py", line 387>:
387           RESUME                   0

388           BUILD_LIST               0
              STORE_FAST               1 (out)

389           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('services')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('operator')
              BINARY_OP               11 (/)
              LOAD_CONST               3 ('audit_integrity.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

390           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

391           LOAD_GLOBAL              4 (REQUIRED_AUDIT_INTEGRITY_TOKENS)
              GET_ITER
      L2:     FOR_ITER                78 (to L7)
              STORE_FAST               4 (tok)

392           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

393           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

394           LOAD_CONST               5 ('audit_integrity:')
              LOAD_FAST_BORROW         4 (tok)
              LOAD_CONST               6 (slice(None, 48, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

395           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               7 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               8 ('FAIL')

396   L4:     LOAD_CONST               9 ('Audit integrity token: ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

397           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

398           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             4 (to L6)
      L5:     LOAD_CONST              10 ('missing token ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

393   L6:     LOAD_CONST              11 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           80 (to L2)

391   L7:     END_FOR
              POP_ITER

400           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181144E0, file "scripts\pas175_audit_integrity_readiness_check.py", line 403>:
403           RESUME                   0
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

Disassembly of <code object check_audit_service_hash_wiring at 0x0000018C17EDFE20, file "scripts\pas175_audit_integrity_readiness_check.py", line 403>:
403            RESUME                   0

404            BUILD_LIST               0
               STORE_FAST               1 (out)

405            LOAD_GLOBAL              1 (Path + NULL)
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

406            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')
       L1:     STORE_FAST               3 (src)

407            LOAD_GLOBAL              4 (REQUIRED_AUDIT_SERVICE_HASH_TOKENS)
               GET_ITER
       L2:     FOR_ITER                78 (to L7)
               STORE_FAST               4 (tok)

408            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

409            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

410            LOAD_CONST               5 ('audit_service_hash:')
               LOAD_FAST_BORROW         4 (tok)
               LOAD_CONST               6 (slice(None, 48, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

411            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               8 ('FAIL')

412    L4:     LOAD_CONST               9 ('Audit service hash-wiring token: ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

413            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

414            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST              10 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

409    L6:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           80 (to L2)

407    L7:     END_FOR
               POP_ITER

418            LOAD_GLOBAL             13 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               6 (executable)

419            BUILD_LIST               0
               STORE_FAST               7 (bad)

420            LOAD_GLOBAL             14 (FORBIDDEN_AUDIT_MUTATION_TOKENS)
               GET_ITER
       L8:     FOR_ITER                28 (to L10)
               STORE_FAST               4 (tok)

421            LOAD_FAST_BORROW_LOAD_FAST_BORROW 70 (tok, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L9)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L8)

422    L9:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (tok)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L8)

420   L10:     END_FOR
               POP_ITER

423            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

424            LOAD_CONST              12 ('audit_service:append_only_invariant_carried')

425            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               8 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               7 ('PASS')

426   L12:     LOAD_CONST              13 ('Audit service still has no UPDATE / DELETE mutation helpers (PAS174 invariant)')

427            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

428            LOAD_FAST_BORROW         7 (bad)
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

423   L14:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

430            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181145D0, file "scripts\pas175_audit_integrity_readiness_check.py", line 433>:
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

Disassembly of <code object check_reaper at 0x0000018C17CC1CE0, file "scripts\pas175_audit_integrity_readiness_check.py", line 433>:
433            RESUME                   0

434            BUILD_LIST               0
               STORE_FAST               1 (out)

435            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('scripts')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('reap_operator_audit_log.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

436            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               2 ('')
       L1:     STORE_FAST               3 (src)

437            LOAD_GLOBAL              4 (REQUIRED_REAPER_TOKENS)
               GET_ITER
       L2:     FOR_ITER                78 (to L7)
               STORE_FAST               4 (tok)

438            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

439            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

440            LOAD_CONST               3 ('reaper:')
               LOAD_FAST_BORROW         4 (tok)
               LOAD_CONST               4 (slice(None, 48, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

441            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               6 ('FAIL')

442    L4:     LOAD_CONST               7 ('Audit reaper token: ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

443            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

444            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST               8 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

439    L6:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           80 (to L2)

437    L7:     END_FOR
               POP_ITER

447            LOAD_CONST              10 ('_MIN_OLDER_THAN_DAYS     = 60')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L8)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              11 ('_MIN_OLDER_THAN_DAYS = 60')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
       L8:     STORE_FAST               6 (floor_ok)

448            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

449            LOAD_CONST              12 ('reaper:60_day_floor')

450            LOAD_FAST_BORROW         6 (floor_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L10)
       L9:     LOAD_CONST               6 ('FAIL')

451   L10:     LOAD_CONST              13 ('Audit reaper script clamps minimum age to 60 days')

452            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

453            LOAD_FAST_BORROW         6 (floor_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST              14 ('missing _MIN_OLDER_THAN_DAYS = 60 literal')

448   L12:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

455            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181147B0, file "scripts\pas175_audit_integrity_readiness_check.py", line 458>:
458           RESUME                   0
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

Disassembly of <code object check_tenant_audit_route at 0x0000018C17E577A0, file "scripts\pas175_audit_integrity_readiness_check.py", line 458>:
458            RESUME                   0

459            BUILD_LIST               0
               STORE_FAST               1 (out)

460            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('routes')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('tenant_portal.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

461            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               3 ('')
       L1:     STORE_FAST               3 (src)

462            LOAD_GLOBAL              4 (REQUIRED_TENANT_AUDIT_TOKENS)
               GET_ITER
       L2:     FOR_ITER                78 (to L7)
               STORE_FAST               4 (tok)

463            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

464            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

465            LOAD_CONST               4 ('tenant_audit_route:')
               LOAD_FAST_BORROW         4 (tok)
               LOAD_CONST               5 (slice(None, 48, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

466            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               6 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               7 ('FAIL')

467    L4:     LOAD_CONST               8 ('Tenant audit route token: ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

468            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

469            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               3 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST               9 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

464    L6:     LOAD_CONST              10 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           80 (to L2)

462    L7:     END_FOR
               POP_ITER

473            LOAD_GLOBAL             13 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               6 (executable)

474            BUILD_LIST               0
               STORE_FAST               7 (bad)

475            LOAD_CONST              15 (('router.post("/audit', 'router.patch("/audit', 'router.delete("/audit', 'router.put("/audit'))
               GET_ITER
       L8:     FOR_ITER                28 (to L10)
               STORE_FAST               8 (verb)

477            LOAD_FAST_BORROW_LOAD_FAST_BORROW 134 (verb, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L9)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L8)

478    L9:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         8 (verb)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L8)

475   L10:     END_FOR
               POP_ITER

479            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

480            LOAD_CONST              11 ('tenant_audit_route:read_only')

481            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               7 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               6 ('PASS')

482   L12:     LOAD_CONST              12 ('Tenant /audit route is read-only (no POST/PATCH/DELETE/PUT)')

483            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

484            LOAD_FAST_BORROW         7 (bad)
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

479   L14:     LOAD_CONST              10 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

486            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181148A0, file "scripts\pas175_audit_integrity_readiness_check.py", line 489>:
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

Disassembly of <code object check_tenant_visibility_audit at 0x0000018C17F01460, file "scripts\pas175_audit_integrity_readiness_check.py", line 489>:
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
              LOAD_CONST               2 ('tenant')
              BINARY_OP               11 (/)
              LOAD_CONST               3 ('tenant_visibility_service.py')
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

493           LOAD_GLOBAL              4 (REQUIRED_TENANT_VISIBILITY_AUDIT_TOKENS)
              GET_ITER
      L2:     FOR_ITER                78 (to L7)
              STORE_FAST               4 (tok)

494           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

495           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

496           LOAD_CONST               5 ('tenant_visibility_audit:')
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

498   L4:     LOAD_CONST               9 ('Tenant visibility audit token: ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

499           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

500           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             4 (to L6)
      L5:     LOAD_CONST              10 ('missing token ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

495   L6:     LOAD_CONST              11 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           80 (to L2)

493   L7:     END_FOR
              POP_ITER

502           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114990, file "scripts\pas175_audit_integrity_readiness_check.py", line 505>:
505           RESUME                   0
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

Disassembly of <code object check_operator_actions_pas175 at 0x0000018C17F003E0, file "scripts\pas175_audit_integrity_readiness_check.py", line 505>:
505           RESUME                   0

506           BUILD_LIST               0
              STORE_FAST               1 (out)

507           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('services')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('operator')
              BINARY_OP               11 (/)
              LOAD_CONST               3 ('operator_actions.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

508           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

509           LOAD_GLOBAL              4 (REQUIRED_OPERATOR_ACTIONS_PAS175_TOKENS)
              GET_ITER
      L2:     FOR_ITER                78 (to L7)
              STORE_FAST               4 (tok)

510           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

511           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

512           LOAD_CONST               5 ('operator_actions_pas175:')
              LOAD_FAST_BORROW         4 (tok)
              LOAD_CONST               6 (slice(None, 48, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

513           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               7 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               8 ('FAIL')

514   L4:     LOAD_CONST               9 ('Operator actions PAS175 token: ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

515           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

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

511   L6:     LOAD_CONST              11 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           80 (to L2)

509   L7:     END_FOR
              POP_ITER

518           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114A80, file "scripts\pas175_audit_integrity_readiness_check.py", line 521>:
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

Disassembly of <code object check_v23_sql at 0x0000018C177883D0, file "scripts\pas175_audit_integrity_readiness_check.py", line 521>:
521            RESUME                   0

522            BUILD_LIST               0
               STORE_FAST               1 (out)

523            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('scripts')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('migrate_v23_audit_hash_chain.sql')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

524            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               2 ('')
       L1:     STORE_FAST               3 (src)

525            LOAD_FAST_BORROW         3 (src)
               LOAD_ATTR                5 (lower + NULL|self)
               CALL                     0
               STORE_FAST               4 (lower)

526            LOAD_CONST               3 ('proposal only')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (proposal_ok)

527            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

528            LOAD_CONST               4 ('v23_sql:proposal_only')

529            LOAD_FAST_BORROW         5 (proposal_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L2)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L3)
       L2:     LOAD_CONST               6 ('FAIL')

530    L3:     LOAD_CONST               7 ("v23 SQL carries 'PROPOSAL ONLY' guardrail")

531            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

532            LOAD_FAST_BORROW         5 (proposal_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L5)
       L4:     LOAD_CONST               8 ("missing 'PROPOSAL ONLY' label")

527    L5:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

534            LOAD_CONST              10 ('do not execute')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)
               STORE_FAST               6 (do_not_exec)

535            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

536            LOAD_CONST              11 ('v23_sql:do_not_execute')

537            LOAD_FAST_BORROW         6 (do_not_exec)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L6)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L7)
       L6:     LOAD_CONST               6 ('FAIL')

538    L7:     LOAD_CONST              12 ("v23 SQL carries 'DO NOT EXECUTE' trailer")

539            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

540            LOAD_FAST_BORROW         6 (do_not_exec)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST              13 ('missing trailer')

535    L9:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

544            LOAD_CONST              14 ('ADD COLUMN IF NOT EXISTS prev_hash text')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        6 (to L10)
               NOT_TAKEN
               POP_TOP

545            LOAD_CONST              15 ('ADD COLUMN IF NOT EXISTS row_hash')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

543   L10:     STORE_FAST               7 (cols_ok)

547            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

548            LOAD_CONST              16 ('v23_sql:hash_chain_columns')

549            LOAD_FAST_BORROW         7 (cols_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               6 ('FAIL')

550   L12:     LOAD_CONST              17 ('v23 SQL adds prev_hash and row_hash columns')

551            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

552            LOAD_FAST_BORROW         7 (cols_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L13)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L14)
      L13:     LOAD_CONST              18 ('missing column ADDs')

547   L14:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

555            LOAD_CONST              19 ('[0-9a-f]{64}')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               STORE_FAST               8 (shape_ok)

556            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

557            LOAD_CONST              20 ('v23_sql:hash_shape_check')

558            LOAD_FAST_BORROW         8 (shape_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L15)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L16)
      L15:     LOAD_CONST               6 ('FAIL')

559   L16:     LOAD_CONST              21 ('v23 SQL pins prev_hash / row_hash to sha256 hex shape')

560            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

561            LOAD_FAST_BORROW         8 (shape_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L17)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L18)
      L17:     LOAD_CONST              22 ('missing sha256 shape CHECK')

556   L18:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

565            LOAD_CONST              23 ('pas_operator_actions_log_service_role_aged_delete')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       36 (to L19)
               NOT_TAKEN
               POP_TOP

566            LOAD_CONST              24 ("now() - interval '30 days'")
               LOAD_FAST_BORROW         3 (src)
               LOAD_ATTR                5 (lower + NULL|self)
               CALL                     0
               LOAD_ATTR               13 (replace + NULL|self)
               LOAD_CONST              25 ('\n')
               LOAD_CONST              26 (' ')
               CALL                     2
               CONTAINS_OP              0 (in)

564   L19:     STORE_FAST               9 (aged_delete_ok)

568            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

569            LOAD_CONST              27 ('v23_sql:aged_delete_policy')

570            LOAD_FAST_BORROW         9 (aged_delete_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L20)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L21)
      L20:     LOAD_CONST               6 ('FAIL')

571   L21:     LOAD_CONST              28 ('v23 SQL introduces aged-DELETE policy with 30-day floor')

572            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

573            LOAD_FAST_BORROW         9 (aged_delete_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L22)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L23)

574   L22:     LOAD_CONST              29 ("expected pas_operator_actions_log_service_role_aged_delete policy + 'now() - interval 30 days' clause")

568   L23:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

579            LOAD_CONST              30 ('pas_operator_actions_log_tenant_no_delete')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               STORE_FAST              10 (tenant_no_delete)

580            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

581            LOAD_CONST              31 ('v23_sql:tenant_delete_forbidden')

582            LOAD_FAST_BORROW        10 (tenant_no_delete)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L24)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L25)
      L24:     LOAD_CONST               6 ('FAIL')

583   L25:     LOAD_CONST              32 ('v23 SQL keeps tenant DELETE forbidden')

584            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

585            LOAD_FAST_BORROW        10 (tenant_no_delete)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L26)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L27)
      L26:     LOAD_CONST              33 ('missing tenant-delete denial')

580   L27:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

587            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114B70, file "scripts\pas175_audit_integrity_readiness_check.py", line 590>:
590           RESUME                   0
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

Disassembly of <code object check_event_contract at 0x0000018C17FED830, file "scripts\pas175_audit_integrity_readiness_check.py", line 590>:
590           RESUME                   0

591           BUILD_LIST               0
              STORE_FAST               1 (out)

592           LOAD_GLOBAL              1 (Path + NULL)
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

593           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

594           LOAD_GLOBAL              4 (REQUIRED_EVENT_TYPES)
              GET_ITER
      L2:     FOR_ITER                72 (to L7)
              STORE_FAST               4 (required)

595           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (required, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

596           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

597           LOAD_CONST               5 ('events:')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

598           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               6 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               7 ('FAIL')

599   L4:     LOAD_CONST               8 ('Event contract registers ')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

600           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

601           LOAD_FAST_BORROW         5 (ok)
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

596   L6:     LOAD_CONST              10 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           74 (to L2)

594   L7:     END_FOR
              POP_ITER

603           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114C60, file "scripts\pas175_audit_integrity_readiness_check.py", line 606>:
606           RESUME                   0
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

Disassembly of <code object check_no_forbidden_imports at 0x0000018C17D8BF50, file "scripts\pas175_audit_integrity_readiness_check.py", line 606>:
606            RESUME                   0

607            BUILD_LIST               0
               STORE_FAST               1 (out)

608            LOAD_CONST              10 (('app/services/operator/audit_integrity.py', 'scripts/reap_operator_audit_log.py', 'scripts/pas175_audit_integrity_readiness_check.py'))
               STORE_FAST               2 (files)

613            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     EXTENDED_ARG             1
               FOR_ITER               297 (to L15)
               STORE_FAST               3 (relpath)

614            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

615            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

616            JUMP_BACKWARD           46 (to L1)

617    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

618            BUILD_LIST               0
               STORE_FAST               6 (bad)

619            LOAD_FAST_BORROW         5 (src)
               LOAD_ATTR                7 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L4:     FOR_ITER               107 (to L10)
               STORE_FAST               7 (line)

620            LOAD_FAST_BORROW         7 (line)
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               STORE_FAST               8 (stripped)

621            LOAD_FAST_BORROW         8 (stripped)
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

622    L5:     JUMP_BACKWARD           52 (to L4)

623    L6:     LOAD_GLOBAL             12 (FORBIDDEN_IMPORT_LINE_PREFIXES)
               GET_ITER
       L7:     FOR_ITER                45 (to L9)
               STORE_FAST               9 (prefix)

624            LOAD_FAST_BORROW         8 (stripped)
               LOAD_ATTR               11 (startswith + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD           28 (to L7)

625    L8:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           47 (to L7)

623    L9:     END_FOR
               POP_ITER
               JUMP_BACKWARD          109 (to L4)

619   L10:     END_FOR
               POP_ITER

626            LOAD_FAST                1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             17 (_check + NULL)

627            LOAD_CONST               3 ('forbidden_import:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

628            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               4 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               5 ('PASS')

629   L12:     LOAD_CONST               6 ('No forbidden imports: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

630            LOAD_GLOBAL             18 (SEVERITY_BLOCK)

632            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       43 (to L13)
               NOT_TAKEN

631            LOAD_CONST               7 ('forbidden import prefixes: ')
               LOAD_CONST               8 (', ')
               LOAD_ATTR               21 (join + NULL|self)
               LOAD_GLOBAL             23 (sorted + NULL)
               LOAD_GLOBAL             25 (set + NULL)
               LOAD_FAST_BORROW         6 (bad)
               CALL                     1
               CALL                     1
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L14)

632   L13:     LOAD_CONST               1 ('')

626   L14:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          300 (to L1)

613   L15:     END_FOR
               POP_ITER

634            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114D50, file "scripts\pas175_audit_integrity_readiness_check.py", line 637>:
637           RESUME                   0
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

Disassembly of <code object check_no_inbox_scan_tokens at 0x0000018C17CD0F70, file "scripts\pas175_audit_integrity_readiness_check.py", line 637>:
637            RESUME                   0

638            BUILD_LIST               0
               STORE_FAST               1 (out)

639            LOAD_CONST               9 (('app/services/operator/audit_integrity.py', 'scripts/reap_operator_audit_log.py', 'scripts/pas175_audit_integrity_readiness_check.py'))
               STORE_FAST               2 (files)

644            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               200 (to L11)
               STORE_FAST               3 (relpath)

645            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

646            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

647            JUMP_BACKWARD           45 (to L1)

648    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

649            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         5 (src)
               CALL                     1
               STORE_FAST               6 (executable)

650            BUILD_LIST               0
               STORE_FAST               7 (bad)

651            LOAD_GLOBAL              8 (FORBIDDEN_INBOX_TOKENS)
               GET_ITER
       L4:     FOR_ITER                28 (to L6)
               STORE_FAST               8 (token)

652            LOAD_FAST_BORROW_LOAD_FAST_BORROW 134 (token, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L4)

653    L5:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_FAST_BORROW         8 (token)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L4)

651    L6:     END_FOR
               POP_ITER

654            LOAD_FAST                1 (out)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_GLOBAL             13 (_check + NULL)

655            LOAD_CONST               2 ('no_inbox_scan:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

656            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L7)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L8)
       L7:     LOAD_CONST               4 ('PASS')

657    L8:     LOAD_CONST               5 ('No inbox-scanning tokens: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

658            LOAD_GLOBAL             14 (SEVERITY_BLOCK)

660            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L9)
               NOT_TAKEN

659            LOAD_CONST               6 ('inbox-scan tokens present: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               17 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L10)

660    L9:     LOAD_CONST               1 ('')

654   L10:     LOAD_CONST               8 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          202 (to L1)

644   L11:     END_FOR
               POP_ITER

662            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114F30, file "scripts\pas175_audit_integrity_readiness_check.py", line 665>:
665           RESUME                   0
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

Disassembly of <code object check_doc_required_clauses at 0x0000018C17D8AF50, file "scripts\pas175_audit_integrity_readiness_check.py", line 665>:
  --            MAKE_CELL                8 (lower)

 665            RESUME                   0

 666            BUILD_LIST               0
                STORE_FAST               1 (out)

 667            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('docs')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('pas175_audit_integrity_and_tenant_audit_visibility.md')
                BINARY_OP               11 (/)
                STORE_FAST               2 (doc)

 668            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (doc)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L1:     STORE_FAST               3 (src)

 669            LOAD_FAST_BORROW         3 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_DEREF              8 (lower)

 670            LOAD_CONST              13 ((('tenant-audit', ('tenant audit visibility', 'tenant_audit')), ('audit-reaper', ('audit reaper',)), ('hash-chain', ('hash-chain', 'hash chain')), ('operator-actions', ('request_readiness_email', 'rotate_brokerage_api_key', 'mark_pilot_stage_with_evidence')), ('no-autonomous', ('no autonomous', 'no-autonomous', 'no autonomous-remediation')), ('rollback', ('rollback',)), ('escalation', ('escalation',)), ('no-gmail', ('no gmail',)), ('limitations', ('limitation',)), ('not-built', ('intentionally not built', 'intentionally does not', 'deliberately not'))))
                STORE_FAST               4 (required_phrases)

 687            LOAD_FAST_BORROW         4 (required_phrases)
                GET_ITER
        L2:     FOR_ITER               146 (to L12)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   86 (name, phrases)

 688            LOAD_GLOBAL              6 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         8 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18026630, file "scripts\pas175_audit_integrity_readiness_check.py", line 688>)
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
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18026630, file "scripts\pas175_audit_integrity_readiness_check.py", line 688>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         6 (phrases)
                GET_ITER
                CALL                     0
                CALL                     1
        L7:     STORE_FAST               7 (present)

 689            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 690            LOAD_CONST               6 ('docs:phrase:')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 691            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               8 ('FAIL')

 692    L9:     LOAD_CONST               9 ('Doctrine doc carries clause: ')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 693            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 695            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L10)
                NOT_TAKEN

 694            LOAD_CONST              10 ('expected one of: ')
                LOAD_CONST              11 (' | ')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_FAST_BORROW         6 (phrases)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L11)

 695   L10:     LOAD_CONST               2 ('')

 689   L11:     LOAD_CONST              12 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          148 (to L2)

 687   L12:     END_FOR
                POP_ITER

 697            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18026630, file "scripts\pas175_audit_integrity_readiness_check.py", line 688>:
  --           COPY_FREE_VARS           1

 688           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C18115020, file "scripts\pas175_audit_integrity_readiness_check.py", line 700>:
700           RESUME                   0
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

Disassembly of <code object check_self_no_env_or_db at 0x0000018C17D88890, file "scripts\pas175_audit_integrity_readiness_check.py", line 700>:
700            RESUME                   0

701            BUILD_LIST               0
               STORE_FAST               1 (out)

702            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_GLOBAL              2 (__file__)
               CALL                     1
               LOAD_ATTR                5 (resolve + NULL|self)
               CALL                     0
               STORE_FAST               2 (self_path)

703            LOAD_GLOBAL              7 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (self_path)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L1:     STORE_FAST               3 (src)

704            LOAD_GLOBAL              9 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               4 (executable)

705            BUILD_LIST               0
               STORE_FAST               5 (bad)

706            LOAD_FAST_BORROW         4 (executable)
               LOAD_ATTR               11 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L2:     FOR_ITER               199 (to L9)
               STORE_FAST               6 (raw_line)

707            LOAD_FAST_BORROW         6 (raw_line)
               LOAD_ATTR               13 (strip + NULL|self)
               CALL                     0
               STORE_FAST               7 (stripped)

708            LOAD_FAST_BORROW         7 (stripped)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN

709            JUMP_BACKWARD           29 (to L2)

710    L3:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              15 (('import dotenv', 'from dotenv'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L4)
               NOT_TAKEN

711            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               1 ('dotenv import')
               CALL                     1
               POP_TOP

712    L4:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              16 (('import supabase', 'from supabase'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L5)
               NOT_TAKEN

713            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               2 ('supabase import')
               CALL                     1
               POP_TOP

714    L5:     LOAD_CONST               3 ('load_dotenv()')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       18 (to L6)
               NOT_TAKEN

715            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               4 ('load_dotenv() call')
               CALL                     1
               POP_TOP

716    L6:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              17 (('os.environ[', 'getenv('))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L7)
               NOT_TAKEN

717            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               5 ('environ read')
               CALL                     1
               POP_TOP

718    L7:     LOAD_CONST               6 ('get_supabase')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD          182 (to L2)

719    L8:     LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               7 ('supabase client call')
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          201 (to L2)

706    L9:     END_FOR
               POP_ITER

720            LOAD_FAST                1 (out)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_GLOBAL             19 (_check + NULL)

721            LOAD_CONST               8 ('self_check:no_env_or_db')

722            LOAD_FAST_BORROW         5 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST               9 ('FAIL')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST              10 ('PASS')

723   L11:     LOAD_CONST              11 ('PAS175 readiness checker never reads .env / touches DB')

724            LOAD_GLOBAL             20 (SEVERITY_BLOCK)

725            LOAD_FAST_BORROW         5 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L12)
               NOT_TAKEN
               LOAD_CONST              12 ('disqualifying patterns: ')
               LOAD_CONST              13 (', ')
               LOAD_ATTR               23 (join + NULL|self)
               LOAD_FAST_BORROW         5 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L13)
      L12:     LOAD_CONST               0 ('')

720   L13:     LOAD_CONST              14 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

727            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18115110, file "scripts\pas175_audit_integrity_readiness_check.py", line 734>:
734           RESUME                   0
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

Disassembly of <code object _aggregate at 0x0000018C17EC4280, file "scripts\pas175_audit_integrity_readiness_check.py", line 734>:
 734            RESUME                   0

 736            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 735            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2

 736    L2:     FOR_ITER                49 (to L7)
                STORE_FAST               1 (c)

 737            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 736    L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L2)

 737    L4:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              2 (SEVERITY_BLOCK)
                COMPARE_OP              88 (bool(==))

 736    L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L2)
        L6:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L2)
        L7:     END_FOR
                POP_ITER

 735    L8:     STORE_FAST               2 (blockers)
                STORE_FAST               1 (c)

 740            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 739            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L9:     BUILD_LIST               0
                SWAP                     2

 740   L10:     FOR_ITER                49 (to L15)
                STORE_FAST               1 (c)

 741            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 740   L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L10)

 741   L12:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              4 (SEVERITY_INFO)
                COMPARE_OP              88 (bool(==))

 740   L13:     POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L10)
       L14:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L10)
       L15:     END_FOR
                POP_ITER

 739   L16:     STORE_FAST               3 (info)
                STORE_FAST               1 (c)

 744            LOAD_CONST               3 ('verdict')
                LOAD_FAST_BORROW         2 (blockers)
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L17)
                NOT_TAKEN
                LOAD_GLOBAL              6 (VERDICT_NOT_READY)
                JUMP_FORWARD             5 (to L18)
       L17:     LOAD_GLOBAL              8 (VERDICT_READY)

 745   L18:     LOAD_CONST               4 ('blockers')
                LOAD_FAST_BORROW         2 (blockers)

 746            LOAD_CONST               5 ('info')
                LOAD_FAST_BORROW         3 (info)

 743            BUILD_MAP                3
                RETURN_VALUE

  --   L19:     SWAP                     2
                POP_TOP

 735            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0

  --   L20:     SWAP                     2
                POP_TOP

 739            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L19 [2]
  L4 to L5 -> L19 [2]
  L6 to L8 -> L19 [2]
  L9 to L11 -> L20 [2]
  L12 to L13 -> L20 [2]
  L14 to L16 -> L20 [2]

Disassembly of <code object __annotate__ at 0x0000018C18115200, file "scripts\pas175_audit_integrity_readiness_check.py", line 750>:
750           RESUME                   0
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

Disassembly of <code object _operator_actions at 0x0000018C18048C70, file "scripts\pas175_audit_integrity_readiness_check.py", line 750>:
750           RESUME                   0

751           BUILD_LIST               0
              STORE_FAST               1 (out)

752           LOAD_FAST_BORROW         0 (checks)
              GET_ITER
      L1:     FOR_ITER               109 (to L5)
              STORE_FAST               2 (c)

753           LOAD_FAST_BORROW         2 (c)
              LOAD_CONST               0 ('status')
              BINARY_OP               26 ([])
              LOAD_CONST               1 ('FAIL')
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

754           JUMP_BACKWARD           19 (to L1)

755   L2:     LOAD_FAST_BORROW         2 (c)
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

756           LOAD_FAST                1 (out)
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

752   L5:     END_FOR
              POP_ITER

757           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181152F0, file "scripts\pas175_audit_integrity_readiness_check.py", line 760>:
760           RESUME                   0
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

Disassembly of <code object evaluate at 0x0000018C17E93E60, file "scripts\pas175_audit_integrity_readiness_check.py", line 760>:
760           RESUME                   0

761           BUILD_LIST               0
              STORE_FAST               1 (checks)

762           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              3 (check_files_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

763           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              5 (check_prior_phases_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

764           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              7 (check_memory_review_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

765           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              9 (check_worker_off_by_default + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

766           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             11 (check_no_startup_worker + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

767           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             13 (check_audit_integrity + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

768           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             15 (check_audit_service_hash_wiring + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

769           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             17 (check_reaper + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

770           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             19 (check_tenant_audit_route + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

771           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             21 (check_tenant_visibility_audit + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

772           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             23 (check_operator_actions_pas175 + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

773           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             25 (check_v23_sql + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

774           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             27 (check_event_contract + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

775           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             29 (check_no_forbidden_imports + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

776           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             31 (check_no_inbox_scan_tokens + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

777           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             33 (check_doc_required_clauses + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

778           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             35 (check_self_no_env_or_db + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

780           LOAD_GLOBAL             37 (_aggregate + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1
              STORE_FAST               2 (agg)

782           LOAD_CONST               0 ('phase')
              LOAD_CONST               1 ('PAS175')

783           LOAD_CONST               2 ('generated_at')
              LOAD_GLOBAL             39 (_now_iso + NULL)
              CALL                     0

784           LOAD_CONST               3 ('verdict')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])

785           LOAD_CONST               4 ('ready')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])
              LOAD_GLOBAL             40 (VERDICT_READY)
              COMPARE_OP              72 (==)

786           LOAD_CONST               5 ('blocker_count')
              LOAD_GLOBAL             43 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               6 ('blockers')
              BINARY_OP               26 ([])
              CALL                     1

787           LOAD_CONST               7 ('info_count')
              LOAD_GLOBAL             43 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               8 ('info')
              BINARY_OP               26 ([])
              CALL                     1

788           LOAD_CONST               9 ('check_count')
              LOAD_GLOBAL             43 (len + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

789           LOAD_CONST              10 ('pass_count')
              LOAD_GLOBAL             45 (sum + NULL)
              LOAD_CONST              11 (<code object <genexpr> at 0x0000018C18053750, file "scripts\pas175_audit_integrity_readiness_check.py", line 789>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

790           LOAD_CONST              12 ('fail_count')
              LOAD_GLOBAL             45 (sum + NULL)
              LOAD_CONST              13 (<code object <genexpr> at 0x0000018C18053870, file "scripts\pas175_audit_integrity_readiness_check.py", line 790>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

791           LOAD_CONST              14 ('checks')
              LOAD_FAST_BORROW         1 (checks)

792           LOAD_CONST              15 ('operator_actions')
              LOAD_GLOBAL             47 (_operator_actions + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

781           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18053750, file "scripts\pas175_audit_integrity_readiness_check.py", line 789>:
 789           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C18053870, file "scripts\pas175_audit_integrity_readiness_check.py", line 790>:
 790           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C181154D0, file "scripts\pas175_audit_integrity_readiness_check.py", line 799>:
799           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C1801C7F0, file "scripts\pas175_audit_integrity_readiness_check.py", line 799>:
799           RESUME                   0

800           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

801           LOAD_CONST               0 ('pas175_audit_integrity_readiness_check')

803           LOAD_CONST               1 ('PAS175 — Evaluate audit integrity + tenant audit visibility surfaces. Read-only — never reads .env, never touches Supabase, never runs a migration.')

800           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

809           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

810           LOAD_CONST               3 ('--repo-root')
              LOAD_GLOBAL              6 (_REPO_ROOT_DEFAULT)

811           LOAD_CONST               4 ('Repo root (default: parent of this script).')

809           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

813           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

814           LOAD_CONST               6 ('--output')
              LOAD_GLOBAL              8 (REPORT_FILENAME)

815           LOAD_CONST               7 ('Where to write the JSON report (default ./')
              LOAD_GLOBAL              8 (REPORT_FILENAME)
              FORMAT_SIMPLE
              LOAD_CONST               8 (').')
              BUILD_STRING             3

813           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

817           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

818           LOAD_CONST               9 ('--json')
              LOAD_CONST              10 ('store_true')

819           LOAD_CONST              11 ('Emit JSON on stdout in addition to the summary.')

817           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

821           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

822           LOAD_CONST              13 ('--summary-only')
              LOAD_CONST              10 ('store_true')

823           LOAD_CONST              14 ('Skip writing the JSON report file.')

821           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

825           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

826           LOAD_CONST              15 ('--strict')
              LOAD_CONST              10 ('store_true')

827           LOAD_CONST              16 ('Exit 1 unless verdict == READY (default policy is the same).')

825           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

829           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181155C0, file "scripts\pas175_audit_integrity_readiness_check.py", line 832>:
832           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C17D8E300, file "scripts\pas175_audit_integrity_readiness_check.py", line 832>:
832           RESUME                   0

833           LOAD_GLOBAL              1 (print + NULL)

834           LOAD_CONST               0 ('[PAS175] verdict=')
              LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               1 ('verdict')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               2 (' blockers=')

835           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               3 ('blocker_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' info=')

836           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               5 ('info_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' checks=')

837           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               7 ('check_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' pass=')

838           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               9 ('pass_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              10 (' fail=')

839           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              11 ('fail_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE

834           BUILD_STRING            12

833           CALL                     1
              POP_TOP

841           LOAD_FAST_BORROW         0 (report)
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

842           LOAD_FAST_BORROW         1 (actions)
              TO_BOOL
              POP_JUMP_IF_FALSE       93 (to L5)
              NOT_TAKEN

843           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              13 ('[PAS175] operator actions:')
              CALL                     1
              POP_TOP

844           LOAD_FAST_BORROW         1 (actions)
              LOAD_CONST              14 (slice(None, 25, None))
              BINARY_OP               26 ([])
              GET_ITER
      L2:     FOR_ITER                17 (to L3)
              STORE_FAST               2 (a)

845           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              15 ('  - ')
              LOAD_FAST_BORROW         2 (a)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L2)

844   L3:     END_FOR
              POP_ITER

846           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         1 (actions)
              CALL                     1
              LOAD_SMALL_INT          25
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       34 (to L4)
              NOT_TAKEN

847           LOAD_GLOBAL              1 (print + NULL)
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

846   L4:     LOAD_CONST              18 (None)
              RETURN_VALUE

842   L5:     LOAD_CONST              18 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024B30, file "scripts\pas175_audit_integrity_readiness_check.py", line 850>:
850           RESUME                   0
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

Disassembly of <code object _write_report at 0x0000018C180FC030, file "scripts\pas175_audit_integrity_readiness_check.py", line 850>:
 850           RESUME                   0

 851           NOP

 852   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

 853           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

 854           LOAD_CONST               3 ('utf-8')

 852           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 856           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

 857   L4:     LOAD_GLOBAL             11 (print + NULL)

 858           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

 859           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

 858           BUILD_STRING             4

 860           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

 857           LOAD_CONST               7 (('file',))
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

 856   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C181156B0, file "scripts\pas175_audit_integrity_readiness_check.py", line 864>:
864           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17D88FF0, file "scripts\pas175_audit_integrity_readiness_check.py", line 864>:
 864            RESUME                   0

 865            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 866            NOP

 867    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 871    L2:     LOAD_GLOBAL             10 (os)
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

 872            LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               21 (isdir + NULL|self)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L4)
                NOT_TAKEN

 873            LOAD_GLOBAL             23 (print + NULL)

 874            LOAD_CONST               2 ('error: --repo-root not a directory: ')
                LOAD_FAST                4 (repo_root)
                FORMAT_SIMPLE
                BUILD_STRING             2

 875            LOAD_GLOBAL             24 (sys)
                LOAD_ATTR               26 (stderr)

 873            LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

 877            LOAD_SMALL_INT           2
                RETURN_VALUE

 879    L4:     LOAD_GLOBAL             29 (evaluate + NULL)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                STORE_FAST               5 (report)

 881            LOAD_FAST                2 (args)
                LOAD_ATTR               30 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L5)
                NOT_TAKEN

 882            LOAD_GLOBAL             33 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               34 (output)
                LOAD_FAST                5 (report)
                CALL                     2
                POP_TOP

 884    L5:     LOAD_GLOBAL             37 (_print_summary + NULL)
                LOAD_FAST                5 (report)
                CALL                     1
                POP_TOP

 886            LOAD_FAST                2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L6)
                NOT_TAKEN

 887            LOAD_GLOBAL             23 (print + NULL)
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

 889    L6:     LOAD_FAST                5 (report)
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

 868            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L17)
                NOT_TAKEN
                STORE_FAST               3 (e)

 869    L9:     LOAD_FAST                3 (e)
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

 868   L17:     RERAISE                  0

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
