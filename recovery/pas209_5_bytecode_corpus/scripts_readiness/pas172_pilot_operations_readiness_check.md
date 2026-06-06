# scripts_readiness/pas172_pilot_operations_readiness_check

- **pyc:** `scripts\__pycache__\pas172_pilot_operations_readiness_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/pas172_pilot_operations_readiness_check.py`
- **co_filename (from bytecode):** `scripts\pas172_pilot_operations_readiness_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS172 — Pilot operations readiness gate.

Deterministic, non-mutating evaluator for "is the PAS172 pilot
operations control layer wired correctly and free of regressions
in the PAS160-PAS171 doctrine?".

Walks the repo and verifies:

  * PAS160-PAS171 readiness scripts still exist.
  * PAS172 surfaces exist:
      - scripts/migrate_v20_worker_heartbeats.sql
      - app/services/worker/heartbeat_service.py
      - app/services/worker/heartbeat_monitor.py
      - scripts/reap_pending_call_dedupe.py
      - scripts/reap_callback_schedule.py
      - app/routes/operator_ops.py
      - app/services/slack/employee_mode.py
      - scripts/pas172_pilot_operations_readiness_check.py
      - docs/pas172_pilot_operations_control_layer.md
      - docs/orvn_pilot_ops_runbook.md
      - tests/mvp/test_pas172_pilot_operations.py
  * Migration v20 carries ``PROPOSAL ONLY`` + ``DO NOT EXECUTE``
    + closed worker_type / status enums + tenant write denial.
  * heartbeat_service exposes the documented surface
    (register / update / stopped + closed enums + allow-listed
    metadata keys).
  * heartbeat_monitor exposes the documented surface
    (heartbeat_monitor_report + stale_worker_report).
  * Reapers carry the dry-run-by-default + bounded-limit +
    structural-envelope guardrails.
  * operator_ops route exposes the four GET routes + admin-auth
    + no transcript/raw payload surface + the defensive
    forbidden-token scanner.
  * employee_mode carries the four block builders + the closed
    Block Kit type allow-list + the forbidden-token scanner +
    no interactive components.
  * Worker still OFF by default
    (``_ENV_FLAG_ENABLED_LITERAL = "true"`` literal intact).
  * FastAPI lifespan in ``app/main.py`` does NOT auto-start
    the worker (PAS162/PAS170/PAS171 invariant).
  * No Gmail / Google / OAuth / IMAP / POP3 / inbox-scan /
    Memory Review / embedding / vector / Composio / TrustClaw
    imports in any PAS172 file.
  * Memory Review (PAS147-PAS158) untouched.
  * Event contract registers every PAS172 event type.
  * Docs carry the required clauses.
  * Operator runbook carries the required clauses.
  * Supports ``--summary-only`` / ``--json``.
  * Exits 0 ready, 1 blockers, 2 bad args.
  * Never reads ``.env``.
  * Never touches production data.
```

## Imports

`List`, `Optional`, `Path`, `__future__`, `annotations`, `argparse`, `datetime`, `json`, `os`, `pathlib`, `sys`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_aggregate`, `_build_parser`, `_check`, `_now_iso`, `_operator_actions`, `_print_summary`, `_read_text`, `_strip_python_comments_and_strings`, `_write_report`, `check_docs_required_clauses`, `check_employee_mode`, `check_event_contract`, `check_files_present`, `check_heartbeat_monitor`, `check_heartbeat_service`, `check_memory_review_intact`, `check_no_forbidden_imports`, `check_no_inbox_scan_tokens`, `check_no_startup_worker`, `check_operator_ops`, `check_prior_phases_intact`, `check_reaper_callback`, `check_reaper_dedupe`, `check_runbook_required_clauses`, `check_self_no_env_or_db`, `check_v20_sql`, `check_worker_off_by_default`, `evaluate`, `main`

## Env-key candidates

`BLOCK`, `FAIL`, `INFO`, `NOT_READY`, `PAS172`, `PASS`, `READY`

## String constants (redacted where noted)

- '\nPAS172 — Pilot operations readiness gate.\n\nDeterministic, non-mutating evaluator for "is the PAS172 pilot\noperations control layer wired correctly and free of regressions\nin the PAS160-PAS171 doctrine?".\n\nWalks the repo and verifies:\n\n  * PAS160-PAS171 readiness scripts still exist.\n  * PAS172 surfaces exist:\n      - scripts/migrate_v20_worker_heartbeats.sql\n      - app/services/worker/heartbeat_service.py\n      - app/services/worker/heartbeat_monitor.py\n      - scripts/reap_pending_call_dedupe.py\n      - scripts/reap_callback_schedule.py\n      - app/routes/operator_ops.py\n      - app/services/slack/employee_mode.py\n      - scripts/pas172_pilot_operations_readiness_check.py\n      - docs/pas172_pilot_operations_control_layer.md\n      - docs/orvn_pilot_ops_runbook.md\n      - tests/mvp/test_pas172_pilot_operations.py\n  * Migration v20 carries ``PROPOSAL ONLY`` + ``DO NOT EXECUTE``\n    + closed worker_type / status enums + tenant write denial.\n  * heartbeat_service exposes the documented surface\n    (register / update / stopped + closed enums + allow-listed\n    metadata keys).\n  * heartbeat_monitor exposes the documented surface\n    (heartbeat_monitor_report + stale_worker_report).\n  * Reapers carry the dry-run-by-default + bounded-limit +\n    structural-envelope guardrails.\n  * operator_ops route exposes the four GET routes + admin-auth\n    + no transcript/raw payload surface + the defensive\n    forbidden-token scanner.\n  * employee_mode carries the four block builders + the closed\n    Block Kit type allow-list + the forbidden-token scanner +\n    no interactive components.\n  * Worker still OFF by default\n    (``_ENV_FLAG_ENABLED_LITERAL = "true"`` literal intact).\n  * FastAPI lifespan in ``app/main.py`` does NOT auto-start\n    the worker (PAS162/PAS170/PAS171 invariant).\n  * No Gmail / Google / OAuth / IMAP / POP3 / inbox-scan /\n    Memory Review / embedding / vector / Composio / TrustClaw\n    imports in any PAS172 file.\n  * Memory Review (PAS147-PAS158) untouched.\n  * Event contract registers every PAS172 event type.\n  * Docs carry the required clauses.\n  * Operator runbook carries the required clauses.\n  * Supports ``--summary-only`` / ``--json``.\n  * Exits 0 ready, 1 blockers, 2 bad args.\n  * Never reads ``.env``.\n  * Never touches production data.\n'
- 'utf-8'
- 'READY'
- 'NOT_READY'
- 'BLOCK'
- 'INFO'
- 'severity'
- 'detail'
- 'pas172_pilot_operations_readiness_report.json'
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
- 'Required PAS172 file present: '
- 'missing'
- 'prior_phase:'
- 'Prior-phase readiness script intact: '
- 'missing — PAS172 must not delete'
- 'memory_review:'
- 'Memory Review file present: '
- 'Memory Review file deleted — PAS172 must not touch'
- 'app'
- 'services'
- 'ingestion'
- 'worker.py'
- '_ENV_FLAG_ENABLED_LITERAL = "true"'
- "_ENV_FLAG_ENABLED_LITERAL = 'true'"
- 'worker:off_by_default'
- 'Pending-call worker is OFF by default (strict env literal)'
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
- 'worker'
- 'heartbeat_service.py'
- 'heartbeat_service:'
- 'Heartbeat service token: '
- 'missing token '
- 'heartbeat_monitor.py'
- 'heartbeat_monitor:'
- 'Heartbeat monitor token: '
- 'scripts'
- 'reap_pending_call_dedupe.py'
- 'reap_dedupe:'
- 'Pending-call dedupe reaper token: '
- 'reap_callback_schedule.py'
- 'reap_callback:'
- 'Callback schedule reaper token: '
- 'routes'
- 'operator_ops.py'
- 'operator_ops:'
- 'Operator ops route token: '
- 'operator_ops:no_pii_exposure'
- 'Operator ops routes do not reference transcript/raw payload'
- 'operator_ops_router'
- 'prefix="/ops"'
- 'operator_ops:router_mounted'
- 'operator_ops_router is mounted at /ops in app/main.py'
- 'expected `operator_ops_router` import + `include_router(..., prefix="/ops")`'
- 'slack'
- 'employee_mode.py'
- 'employee_mode:'
- 'Slack employee-mode token: '
- 'employee_mode:no_interactive_components'
- 'Slack employee mode has no interactive components'
- 'interactive tokens: '
- 'migrate_v20_worker_heartbeats.sql'
- 'proposal only'
- 'v20_sql:proposal_only'
- "v20 SQL carries 'PROPOSAL ONLY' guardrail"
- "missing 'PROPOSAL ONLY' label"
- 'do not execute'
- 'v20_sql:do_not_execute'
- "v20 SQL carries 'DO NOT EXECUTE' trailer"
- 'missing trailer'
- 'v20_sql:closed_worker_type_enum'
- 'v20 SQL carries the closed worker_type enum literals'
- 'missing one or more worker_type literals'
- 'v20_sql:closed_status_enum'
- 'v20 SQL carries the closed status enum literals'
- 'missing one or more status literals'
- 'pas_worker_heartbeats_tenant_no_insert'
- 'with check (false)'
- 'v20_sql:tenant_no_write'
- 'v20 SQL denies tenant write'
- 'missing tenant-write denial'
- 'pas_worker_heartbeats_tenant_no_select'
- 'v20_sql:tenant_no_select'
- 'v20 SQL denies tenant SELECT (workers are operator-only)'
- 'missing tenant-select denial'
- 'events'
- 'contract.py'
- 'events:'
- 'Event contract registers '
- 'missing event type '
- 'app/services/worker/__init__.py'
- 'forbidden_import:'
- 'No forbidden imports: '
- 'forbidden import prefixes: '
- 'app/services/worker/heartbeat_service.py'
- 'no_inbox_scan:'
- 'No inbox-scanning tokens: '
- 'inbox-scan tokens present: '
- 'docs'
- 'pas172_pilot_operations_control_layer.md'
- 'docs:phrase:'
- 'Control-layer doc carries clause: '
- 'expected one of: '
- ' | '
- 'orvn_pilot_ops_runbook.md'
- 'runbook:phrase:'
- 'Operator runbook carries clause: '
- 'dotenv import'
- 'supabase import'
- 'load_dotenv()'
- 'load_dotenv() call'
- 'environ read'
- 'get_supabase'
- 'supabase client call'
- 'self_check:no_env_or_db'
- 'PAS172 readiness checker never reads .env / touches DB'
- 'disqualifying patterns: '
- 'checks'
- 'verdict'
- 'blockers'
- 'info'
- 'List[str]'
- ' — '
- 'see report'
- 'phase'
- 'PAS172'
- 'generated_at'
- 'ready'
- 'blocker_count'
- 'info_count'
- 'check_count'
- 'pass_count'
- 'fail_count'
- 'operator_actions'
- 'argparse.ArgumentParser'
- 'pas172_pilot_operations_readiness_check'
- 'PAS172 — Evaluate the pilot operations control layer (worker heartbeat + reapers + Slack employee mode + operator ops routes). Read-only — never reads .env, never touches Supabase, never runs a migration.'
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
- '[PAS172] verdict='
- ' blockers='
- ' info='
- ' checks='
- ' pass='
- ' fail='
- '[PAS172] operator actions:'
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

   1           LOAD_CONST               0 ('\nPAS172 — Pilot operations readiness gate.\n\nDeterministic, non-mutating evaluator for "is the PAS172 pilot\noperations control layer wired correctly and free of regressions\nin the PAS160-PAS171 doctrine?".\n\nWalks the repo and verifies:\n\n  * PAS160-PAS171 readiness scripts still exist.\n  * PAS172 surfaces exist:\n      - scripts/migrate_v20_worker_heartbeats.sql\n      - app/services/worker/heartbeat_service.py\n      - app/services/worker/heartbeat_monitor.py\n      - scripts/reap_pending_call_dedupe.py\n      - scripts/reap_callback_schedule.py\n      - app/routes/operator_ops.py\n      - app/services/slack/employee_mode.py\n      - scripts/pas172_pilot_operations_readiness_check.py\n      - docs/pas172_pilot_operations_control_layer.md\n      - docs/orvn_pilot_ops_runbook.md\n      - tests/mvp/test_pas172_pilot_operations.py\n  * Migration v20 carries ``PROPOSAL ONLY`` + ``DO NOT EXECUTE``\n    + closed worker_type / status enums + tenant write denial.\n  * heartbeat_service exposes the documented surface\n    (register / update / stopped + closed enums + allow-listed\n    metadata keys).\n  * heartbeat_monitor exposes the documented surface\n    (heartbeat_monitor_report + stale_worker_report).\n  * Reapers carry the dry-run-by-default + bounded-limit +\n    structural-envelope guardrails.\n  * operator_ops route exposes the four GET routes + admin-auth\n    + no transcript/raw payload surface + the defensive\n    forbidden-token scanner.\n  * employee_mode carries the four block builders + the closed\n    Block Kit type allow-list + the forbidden-token scanner +\n    no interactive components.\n  * Worker still OFF by default\n    (``_ENV_FLAG_ENABLED_LITERAL = "true"`` literal intact).\n  * FastAPI lifespan in ``app/main.py`` does NOT auto-start\n    the worker (PAS162/PAS170/PAS171 invariant).\n  * No Gmail / Google / OAuth / IMAP / POP3 / inbox-scan /\n    Memory Review / embedding / vector / Composio / TrustClaw\n    imports in any PAS172 file.\n  * Memory Review (PAS147-PAS158) untouched.\n  * Event contract registers every PAS172 event type.\n  * Docs carry the required clauses.\n  * Operator runbook carries the required clauses.\n  * Supports ``--summary-only`` / ``--json``.\n  * Exits 0 ready, 1 blockers, 2 bad args.\n  * Never reads ``.env``.\n  * Never touches production data.\n')
               STORE_NAME               0 (__doc__)

  55           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  57           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  58           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (json)
               STORE_NAME               4 (json)

  59           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (os)
               STORE_NAME               5 (os)

  60           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (sys)
               STORE_NAME               6 (sys)

  61           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              7 (datetime)
               IMPORT_FROM              7 (datetime)
               STORE_NAME               7 (datetime)
               IMPORT_FROM              8 (timezone)
               STORE_NAME               8 (timezone)
               POP_TOP

  62           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Path',))
               IMPORT_NAME              9 (pathlib)
               IMPORT_FROM             10 (Path)
               STORE_NAME              10 (Path)
               POP_TOP

  63           LOAD_SMALL_INT           0
               LOAD_CONST               5 (('List', 'Optional'))
               IMPORT_NAME             11 (typing)
               IMPORT_FROM             12 (List)
               STORE_NAME              12 (List)
               IMPORT_FROM             13 (Optional)
               STORE_NAME              13 (Optional)
               POP_TOP

  66           LOAD_NAME                6 (sys)
               LOAD_ATTR               28 (stdout)
               LOAD_NAME                6 (sys)
               LOAD_ATTR               30 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              16 (_stream)

  67           NOP

  68   L2:     LOAD_NAME               16 (_stream)
               LOAD_ATTR               35 (reconfigure + NULL|self)
               LOAD_CONST               6 ('utf-8')
               LOAD_CONST               7 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  66   L4:     END_FOR
               POP_ITER

  73           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               41 (abspath + NULL|self)

  74           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               43 (join + NULL|self)
               LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               45 (dirname + NULL|self)
               LOAD_NAME               23 (__file__)
               CALL                     1
               LOAD_CONST               8 ('..')
               CALL                     2

  73           CALL                     1
               STORE_NAME              24 (_REPO_ROOT_DEFAULT)

  78           LOAD_CONST               9 ('READY')
               STORE_NAME              25 (VERDICT_READY)

  79           LOAD_CONST              10 ('NOT_READY')
               STORE_NAME              26 (VERDICT_NOT_READY)

  81           LOAD_CONST              11 ('BLOCK')
               STORE_NAME              27 (SEVERITY_BLOCK)

  82           LOAD_CONST              12 ('INFO')
               STORE_NAME              28 (SEVERITY_INFO)

  89           LOAD_CONST              76 (('scripts/migrate_v20_worker_heartbeats.sql', 'app/services/worker/__init__.py', 'app/services/worker/heartbeat_service.py', 'app/services/worker/heartbeat_monitor.py', 'scripts/reap_pending_call_dedupe.py', 'scripts/reap_callback_schedule.py', 'app/routes/operator_ops.py', 'app/services/slack/__init__.py', 'app/services/slack/employee_mode.py', 'scripts/pas172_pilot_operations_readiness_check.py', 'docs/pas172_pilot_operations_control_layer.md', 'docs/orvn_pilot_ops_runbook.md', 'tests/mvp/test_pas172_pilot_operations.py'))
               STORE_NAME              29 (REQUIRED_FILES)

 105           LOAD_CONST              77 (('scripts/pas160_mvp_sequence_check.py', 'scripts/pas161_lead_ingestion_readiness_check.py', 'scripts/pas162_pending_calls_readiness_check.py', 'scripts/pas163_candidate_pipeline_readiness_check.py', 'scripts/pas164_email_ingestion_readiness_check.py', 'scripts/pas165_email_auth_dedupe_readiness_check.py', 'scripts/pas166_email_dedupe_policy_readiness_check.py', 'scripts/pas167_email_secret_reaper_readiness_check.py', 'scripts/pas168_email_secret_rotation_readiness_check.py', 'scripts/pas169_crypto_roundtrip_check.py', 'scripts/pas169_launch_readiness_check.py', 'scripts/pas_launch_integrity_check.py', 'scripts/pas170_operator_survival_readiness_check.py', 'scripts/pas171_external_pilot_readiness_check.py'))
               STORE_NAME              30 (PRIOR_PHASE_FILES)

 122           LOAD_CONST              78 (('app/services/memory/review.py', 'app/services/memory/review_stats.py', 'app/services/memory/review_export.py', 'app/services/memory/review_actors.py', 'app/services/memory/review_alerts.py', 'app/services/memory/operator_console.py'))
               STORE_NAME              31 (MEMORY_REVIEW_FILES)

 132           LOAD_CONST              79 (('def register_worker_heartbeat(', 'def update_worker_heartbeat(', 'def mark_worker_stopped(', 'ALLOWED_WORKER_TYPES', 'ALLOWED_STATUSES', 'ALLOWED_METADATA_KEYS', '_TABLE = "pas_worker_heartbeats"', 'heartbeat_store_unavailable'))
               STORE_NAME              32 (REQUIRED_HEARTBEAT_SERVICE_TOKENS)

 143           LOAD_CONST              80 (('def heartbeat_monitor_report(', 'def stale_worker_report(', 'DEFAULT_STALE_AFTER_SECONDS', '_TABLE = "pas_worker_heartbeats"'))
               STORE_NAME              33 (REQUIRED_HEARTBEAT_MONITOR_TOKENS)

 150           LOAD_CONST              81 (('def reap(', '--execute', '--older-than-hours', '--limit', 'dry_run:           bool = True', '_HARD_CAP_LIMIT', '_DEFAULT_OLDER_THAN_HOURS', '_DEFAULT_LIMIT', 'durable_pending_call_dedupe_unavailable'))
               STORE_NAME              34 (REQUIRED_REAP_DEDUPE_TOKENS)

 162           LOAD_CONST              82 (('def reap(', '--execute', '--older-than-hours', '--limit', 'TERMINAL_STATUSES = ("completed", "cancelled", "overdue", "failed")', '_HARD_CAP_LIMIT', '_DEFAULT_OLDER_THAN_HOURS', '_DEFAULT_LIMIT', 'durable_callback_schedule_unavailable'))
               STORE_NAME              35 (REQUIRED_REAP_CALLBACK_TOKENS)

 174           LOAD_CONST              83 (('def require_admin(', '@router.get("/workers/status")', '@router.get("/pending-calls/queue")', '@router.get("/callbacks/pending")', '@router.get("/recovery/stale-dialing")', '_FORBIDDEN_RESPONSE_TOKENS', '_final_envelope', 'ops_envelope_forbidden_token'))
               STORE_NAME              36 (REQUIRED_OPERATOR_OPS_TOKENS)

 185           LOAD_CONST              84 (('def build_worker_status_block(', 'def build_queue_summary_block(', 'def build_callback_summary_block(', 'def build_recovery_summary_block(', 'FORBIDDEN_BLOCK_TOKENS', 'ALLOWED_BLOCK_TYPES', '_scan_blocks_for_forbidden_tokens'))
               STORE_NAME              37 (REQUIRED_EMPLOYEE_MODE_TOKENS)

 196           LOAD_CONST              85 (('external_pilot.heartbeat', 'worker.heartbeat.started', 'worker.heartbeat.updated', 'worker.heartbeat.stale', 'worker.heartbeat.stopped', 'callback.reminder.generated', 'reaper.pending_call_dedupe.executed', 'reaper.callback_schedule.executed', 'slack.employee.summary.generated'))
               STORE_NAME              38 (REQUIRED_EVENT_TYPES)

 211           LOAD_CONST              86 (('import gmail', 'from gmail', 'import googleapiclient', 'from googleapiclient', 'import google.oauth2', 'from google.oauth2', 'from google.auth', 'import google.auth', 'from google_auth_oauthlib', 'import imaplib', 'from imaplib', 'import poplib', 'from poplib', 'import composio', 'from composio', 'import trustclaw', 'from trustclaw', 'import chromadb', 'from chromadb', 'import pinecone', 'from pinecone', 'import langchain', 'from langchain', 'import faiss', 'import pgvector', 'from pgvector', 'from openai import embeddings', 'from openai.embeddings', 'from app.services.memory', 'import app.services.memory'))
               STORE_NAME              39 (FORBIDDEN_IMPORT_LINE_PREFIXES)

 232           LOAD_CONST              87 (('imaplib', 'poplib', 'fetch_inbox', 'gmail_oauth', 'gmail_token', 'users().messages'))
               STORE_NAME              40 (FORBIDDEN_INBOX_TOKENS)

 243           LOAD_CONST              88 (('block_actions', 'view_submission', 'interactivity', 'slash_command_callback', '"type": "button"', '"type": "actions"'))
               STORE_NAME              41 (FORBIDDEN_SLACK_INTERACTIVE_TOKENS)

 256           LOAD_CONST              89 (('transcript', 'raw_payload', 'raw_email'))
               STORE_NAME              42 (FORBIDDEN_OPS_EXPOSURE_TOKENS)

 267           LOAD_CONST              13 ('severity')

 269           LOAD_NAME               27 (SEVERITY_BLOCK)

 267           LOAD_CONST              14 ('detail')

 269           LOAD_CONST              15 ('')

 267           BUILD_MAP                2
               LOAD_CONST              16 (<code object __annotate__ at 0x0000018C18025030, file "scripts\pas172_pilot_operations_readiness_check.py", line 267>)
               MAKE_FUNCTION
               LOAD_CONST              17 (<code object _check at 0x0000018C17FA2970, file "scripts\pas172_pilot_operations_readiness_check.py", line 267>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              43 (_check)

 280           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA2F10, file "scripts\pas172_pilot_operations_readiness_check.py", line 280>)
               MAKE_FUNCTION
               LOAD_CONST              19 (<code object _now_iso at 0x0000018C18038670, file "scripts\pas172_pilot_operations_readiness_check.py", line 280>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              44 (_now_iso)

 284           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA33C0, file "scripts\pas172_pilot_operations_readiness_check.py", line 284>)
               MAKE_FUNCTION
               LOAD_CONST              21 (<code object _read_text at 0x0000018C18053750, file "scripts\pas172_pilot_operations_readiness_check.py", line 284>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              45 (_read_text)

 291           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA35A0, file "scripts\pas172_pilot_operations_readiness_check.py", line 291>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object _strip_python_comments_and_strings at 0x0000018C17D6DFC0, file "scripts\pas172_pilot_operations_readiness_check.py", line 291>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              46 (_strip_python_comments_and_strings)

 330           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA3D20, file "scripts\pas172_pilot_operations_readiness_check.py", line 330>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object check_files_present at 0x0000018C180608A0, file "scripts\pas172_pilot_operations_readiness_check.py", line 330>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              47 (check_files_present)

 344           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA1D40, file "scripts\pas172_pilot_operations_readiness_check.py", line 344>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object check_prior_phases_intact at 0x0000018C18060A50, file "scripts\pas172_pilot_operations_readiness_check.py", line 344>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              48 (check_prior_phases_intact)

 358           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA2880, file "scripts\pas172_pilot_operations_readiness_check.py", line 358>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object check_memory_review_intact at 0x0000018C18060C00, file "scripts\pas172_pilot_operations_readiness_check.py", line 358>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              49 (check_memory_review_intact)

 372           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA2100, file "scripts\pas172_pilot_operations_readiness_check.py", line 372>)
               MAKE_FUNCTION
               LOAD_CONST              31 (<code object check_worker_off_by_default at 0x0000018C179A7290, file "scripts\pas172_pilot_operations_readiness_check.py", line 372>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              50 (check_worker_off_by_default)

 390           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA2B50, file "scripts\pas172_pilot_operations_readiness_check.py", line 390>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object check_no_startup_worker at 0x0000018C17EA5040, file "scripts\pas172_pilot_operations_readiness_check.py", line 390>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              51 (check_no_startup_worker)

 414           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA3780, file "scripts\pas172_pilot_operations_readiness_check.py", line 414>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object check_heartbeat_service at 0x0000018C17F001D0, file "scripts\pas172_pilot_operations_readiness_check.py", line 414>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              52 (check_heartbeat_service)

 430           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C17FA1E30, file "scripts\pas172_pilot_operations_readiness_check.py", line 430>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object check_heartbeat_monitor at 0x0000018C17F01040, file "scripts\pas172_pilot_operations_readiness_check.py", line 430>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              53 (check_heartbeat_monitor)

 446           LOAD_CONST              38 (<code object __annotate__ at 0x0000018C17FA2E20, file "scripts\pas172_pilot_operations_readiness_check.py", line 446>)
               MAKE_FUNCTION
               LOAD_CONST              39 (<code object check_reaper_dedupe at 0x0000018C1801CDC0, file "scripts\pas172_pilot_operations_readiness_check.py", line 446>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              54 (check_reaper_dedupe)

 462           LOAD_CONST              40 (<code object __annotate__ at 0x0000018C17FA21F0, file "scripts\pas172_pilot_operations_readiness_check.py", line 462>)
               MAKE_FUNCTION
               LOAD_CONST              41 (<code object check_reaper_callback at 0x0000018C1801CFB0, file "scripts\pas172_pilot_operations_readiness_check.py", line 462>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              55 (check_reaper_callback)

 478           LOAD_CONST              42 (<code object __annotate__ at 0x0000018C17FA26A0, file "scripts\pas172_pilot_operations_readiness_check.py", line 478>)
               MAKE_FUNCTION
               LOAD_CONST              43 (<code object check_operator_ops at 0x0000018C17EFB9B0, file "scripts\pas172_pilot_operations_readiness_check.py", line 478>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              56 (check_operator_ops)

 524           LOAD_CONST              44 (<code object __annotate__ at 0x0000018C17FA2790, file "scripts\pas172_pilot_operations_readiness_check.py", line 524>)
               MAKE_FUNCTION
               LOAD_CONST              45 (<code object check_employee_mode at 0x0000018C17EDFB10, file "scripts\pas172_pilot_operations_readiness_check.py", line 524>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              57 (check_employee_mode)

 554           LOAD_CONST              46 (<code object __annotate__ at 0x0000018C17FA22E0, file "scripts\pas172_pilot_operations_readiness_check.py", line 554>)
               MAKE_FUNCTION
               LOAD_CONST              47 (<code object check_v20_sql at 0x0000018C181A00E0, file "scripts\pas172_pilot_operations_readiness_check.py", line 554>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              58 (check_v20_sql)

 629           LOAD_CONST              48 (<code object __annotate__ at 0x0000018C17FA24C0, file "scripts\pas172_pilot_operations_readiness_check.py", line 629>)
               MAKE_FUNCTION
               LOAD_CONST              49 (<code object check_event_contract at 0x0000018C17FEE030, file "scripts\pas172_pilot_operations_readiness_check.py", line 629>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              59 (check_event_contract)

 645           LOAD_CONST              50 (<code object __annotate__ at 0x0000018C17FA25B0, file "scripts\pas172_pilot_operations_readiness_check.py", line 645>)
               MAKE_FUNCTION
               LOAD_CONST              51 (<code object check_no_forbidden_imports at 0x0000018C17F84C80, file "scripts\pas172_pilot_operations_readiness_check.py", line 645>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              60 (check_no_forbidden_imports)

 682           LOAD_CONST              52 (<code object __annotate__ at 0x0000018C17FA23D0, file "scripts\pas172_pilot_operations_readiness_check.py", line 682>)
               MAKE_FUNCTION
               LOAD_CONST              53 (<code object check_no_inbox_scan_tokens at 0x0000018C17CD2160, file "scripts\pas172_pilot_operations_readiness_check.py", line 682>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              61 (check_no_inbox_scan_tokens)

 714           LOAD_CONST              54 (<code object __annotate__ at 0x0000018C17FA2A60, file "scripts\pas172_pilot_operations_readiness_check.py", line 714>)
               MAKE_FUNCTION
               LOAD_CONST              55 (<code object check_docs_required_clauses at 0x0000018C17D8A770, file "scripts\pas172_pilot_operations_readiness_check.py", line 714>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              62 (check_docs_required_clauses)

 754           LOAD_CONST              56 (<code object __annotate__ at 0x0000018C17FA2C40, file "scripts\pas172_pilot_operations_readiness_check.py", line 754>)
               MAKE_FUNCTION
               LOAD_CONST              57 (<code object check_runbook_required_clauses at 0x0000018C17D8AA10, file "scripts\pas172_pilot_operations_readiness_check.py", line 754>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              63 (check_runbook_required_clauses)

 788           LOAD_CONST              58 (<code object __annotate__ at 0x0000018C17FA3690, file "scripts\pas172_pilot_operations_readiness_check.py", line 788>)
               MAKE_FUNCTION
               LOAD_CONST              59 (<code object check_self_no_env_or_db at 0x0000018C17D884E0, file "scripts\pas172_pilot_operations_readiness_check.py", line 788>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              64 (check_self_no_env_or_db)

 822           LOAD_CONST              60 (<code object __annotate__ at 0x0000018C17FA30F0, file "scripts\pas172_pilot_operations_readiness_check.py", line 822>)
               MAKE_FUNCTION
               LOAD_CONST              61 (<code object _aggregate at 0x0000018C17EC5380, file "scripts\pas172_pilot_operations_readiness_check.py", line 822>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              65 (_aggregate)

 838           LOAD_CONST              62 (<code object __annotate__ at 0x0000018C17FA3F00, file "scripts\pas172_pilot_operations_readiness_check.py", line 838>)
               MAKE_FUNCTION
               LOAD_CONST              63 (<code object _operator_actions at 0x0000018C18048C70, file "scripts\pas172_pilot_operations_readiness_check.py", line 838>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              66 (_operator_actions)

 848           LOAD_CONST              64 (<code object __annotate__ at 0x0000018C17FA2010, file "scripts\pas172_pilot_operations_readiness_check.py", line 848>)
               MAKE_FUNCTION
               LOAD_CONST              65 (<code object evaluate at 0x0000018C17D8BF50, file "scripts\pas172_pilot_operations_readiness_check.py", line 848>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              67 (evaluate)

 885           LOAD_CONST              66 ('pas172_pilot_operations_readiness_report.json')
               STORE_NAME              68 (REPORT_FILENAME)

 888           LOAD_CONST              67 (<code object __annotate__ at 0x0000018C17FA3870, file "scripts\pas172_pilot_operations_readiness_check.py", line 888>)
               MAKE_FUNCTION
               LOAD_CONST              68 (<code object _build_parser at 0x0000018C1801CBD0, file "scripts\pas172_pilot_operations_readiness_check.py", line 888>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              69 (_build_parser)

 922           LOAD_CONST              69 (<code object __annotate__ at 0x0000018C17FA3000, file "scripts\pas172_pilot_operations_readiness_check.py", line 922>)
               MAKE_FUNCTION
               LOAD_CONST              70 (<code object _print_summary at 0x0000018C17D8E300, file "scripts\pas172_pilot_operations_readiness_check.py", line 922>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              70 (_print_summary)

 940           LOAD_CONST              71 (<code object __annotate__ at 0x0000018C18024930, file "scripts\pas172_pilot_operations_readiness_check.py", line 940>)
               MAKE_FUNCTION
               LOAD_CONST              72 (<code object _write_report at 0x0000018C180FC7B0, file "scripts\pas172_pilot_operations_readiness_check.py", line 940>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              71 (_write_report)

 954           LOAD_CONST              90 ((None,))
               LOAD_CONST              73 (<code object __annotate__ at 0x0000018C18114030, file "scripts\pas172_pilot_operations_readiness_check.py", line 954>)
               MAKE_FUNCTION
               LOAD_CONST              74 (<code object main at 0x0000018C17D88FF0, file "scripts\pas172_pilot_operations_readiness_check.py", line 954>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              72 (main)

 982           LOAD_NAME               73 (__name__)
               LOAD_CONST              75 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 983           LOAD_NAME                6 (sys)
               LOAD_ATTR              148 (exit)
               PUSH_NULL
               LOAD_NAME               72 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 982   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  69           LOAD_NAME               18 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  70   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          369 (to L1)

  69   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025030, file "scripts\pas172_pilot_operations_readiness_check.py", line 267>:
267           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('check_id')

268           LOAD_CONST               2 ('str')

267           LOAD_CONST               3 ('status')

268           LOAD_CONST               2 ('str')

267           LOAD_CONST               4 ('label')

268           LOAD_CONST               2 ('str')

267           LOAD_CONST               5 ('severity')

269           LOAD_CONST               2 ('str')

267           LOAD_CONST               6 ('detail')

269           LOAD_CONST               2 ('str')

267           LOAD_CONST               7 ('return')

270           LOAD_CONST               8 ('dict')

267           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _check at 0x0000018C17FA2970, file "scripts\pas172_pilot_operations_readiness_check.py", line 267>:
267           RESUME                   0

272           LOAD_CONST               0 ('id')
              LOAD_FAST_BORROW         0 (check_id)

273           LOAD_CONST               1 ('status')
              LOAD_FAST_BORROW         1 (status)

274           LOAD_CONST               2 ('label')
              LOAD_FAST_BORROW         2 (label)

275           LOAD_CONST               3 ('severity')
              LOAD_FAST_BORROW         3 (severity)

276           LOAD_CONST               4 ('detail')
              LOAD_FAST_BORROW         4 (detail)

271           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "scripts\pas172_pilot_operations_readiness_check.py", line 280>:
280           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038670, file "scripts\pas172_pilot_operations_readiness_check.py", line 280>:
280           RESUME                   0

281           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "scripts\pas172_pilot_operations_readiness_check.py", line 284>:
284           RESUME                   0
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

Disassembly of <code object _read_text at 0x0000018C18053750, file "scripts\pas172_pilot_operations_readiness_check.py", line 284>:
 284           RESUME                   0

 285           NOP

 286   L1:     LOAD_FAST_BORROW         0 (path)
               LOAD_ATTR                1 (read_text + NULL|self)
               LOAD_CONST               0 ('utf-8')
               LOAD_CONST               1 ('replace')
               LOAD_CONST               2 (('encoding', 'errors'))
               CALL_KW                  2
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 287           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 288   L4:     POP_EXCEPT
               LOAD_CONST               3 (None)
               RETURN_VALUE

 287   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "scripts\pas172_pilot_operations_readiness_check.py", line 291>:
291           RESUME                   0
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

Disassembly of <code object _strip_python_comments_and_strings at 0x0000018C17D6DFC0, file "scripts\pas172_pilot_operations_readiness_check.py", line 291>:
291            RESUME                   0

292            BUILD_LIST               0
               STORE_FAST               1 (out)

293            LOAD_SMALL_INT           0
               LOAD_GLOBAL              1 (len + NULL)
               LOAD_FAST_BORROW         0 (src)
               CALL                     1
               STORE_FAST_STORE_FAST   50 (n, i)

294    L1:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (i, n)
               COMPARE_OP              18 (bool(<))
               EXTENDED_ARG             1
               POP_JUMP_IF_FALSE      282 (to L13)
               NOT_TAKEN

295            LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               BINARY_OP               26 ([])
               STORE_FAST               4 (ch)

296            LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               1 ('#')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       38 (to L3)
               NOT_TAKEN

297            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_CONST               2 ('\n')
               LOAD_FAST_BORROW         2 (i)
               CALL                     2
               STORE_FAST               5 (j)

298            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L2)
               NOT_TAKEN

299            JUMP_FORWARD           240 (to L13)

300    L2:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

301            JUMP_BACKWARD           59 (to L1)

302    L3:     LOAD_FAST_BORROW         0 (src)
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

303    L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               BINARY_SLICE
               STORE_FAST               6 (quote)

304            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 98 (quote, i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               CALL                     2
               STORE_FAST               7 (end)

305            LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L5)
               NOT_TAKEN

306            JUMP_FORWARD           138 (to L13)

307    L5:     LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

308            JUMP_BACKWARD          161 (to L1)

309    L6:     LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               7 (('"', "'"))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       92 (to L12)
               NOT_TAKEN

310            LOAD_FAST                4 (ch)
               STORE_FAST               6 (quote)

311            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               5 (j)

312    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (j, n)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       63 (to L11)
               NOT_TAKEN

313            LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
               BINARY_OP               26 ([])
               LOAD_CONST               5 ('\\')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       12 (to L8)
               NOT_TAKEN

314            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           2
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)

315            JUMP_BACKWARD           30 (to L7)

316    L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
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

317    L9:     JUMP_FORWARD            11 (to L11)

318   L10:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)
               JUMP_BACKWARD           68 (to L7)

319   L11:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

320            EXTENDED_ARG             1
               JUMP_BACKWARD          259 (to L1)

321   L12:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (ch)
               CALL                     1
               POP_TOP

322            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               2 (i)
               EXTENDED_ARG             1
               JUMP_BACKWARD          288 (to L1)

323   L13:     LOAD_CONST               6 ('')
               LOAD_ATTR                9 (join + NULL|self)
               LOAD_FAST_BORROW         1 (out)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3D20, file "scripts\pas172_pilot_operations_readiness_check.py", line 330>:
330           RESUME                   0
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

Disassembly of <code object check_files_present at 0x0000018C180608A0, file "scripts\pas172_pilot_operations_readiness_check.py", line 330>:
330           RESUME                   0

331           BUILD_LIST               0
              STORE_FAST               1 (out)

332           LOAD_GLOBAL              0 (REQUIRED_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

333           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

334           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

335           LOAD_CONST               0 ('file:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

336           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

337   L3:     LOAD_CONST               3 ('Required PAS172 file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

338           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

339           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing')

334   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

332   L6:     END_FOR
              POP_ITER

341           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1D40, file "scripts\pas172_pilot_operations_readiness_check.py", line 344>:
344           RESUME                   0
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

Disassembly of <code object check_prior_phases_intact at 0x0000018C18060A50, file "scripts\pas172_pilot_operations_readiness_check.py", line 344>:
344           RESUME                   0

345           BUILD_LIST               0
              STORE_FAST               1 (out)

346           LOAD_GLOBAL              0 (PRIOR_PHASE_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

347           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

348           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

349           LOAD_CONST               0 ('prior_phase:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

350           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

351   L3:     LOAD_CONST               3 ('Prior-phase readiness script intact: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

352           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

353           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing — PAS172 must not delete')

348   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

346   L6:     END_FOR
              POP_ITER

355           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "scripts\pas172_pilot_operations_readiness_check.py", line 358>:
358           RESUME                   0
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

Disassembly of <code object check_memory_review_intact at 0x0000018C18060C00, file "scripts\pas172_pilot_operations_readiness_check.py", line 358>:
358           RESUME                   0

359           BUILD_LIST               0
              STORE_FAST               1 (out)

360           LOAD_GLOBAL              0 (MEMORY_REVIEW_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

361           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

362           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

363           LOAD_CONST               0 ('memory_review:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

364           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

365   L3:     LOAD_CONST               3 ('Memory Review file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

366           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

367           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('Memory Review file deleted — PAS172 must not touch')

362   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

360   L6:     END_FOR
              POP_ITER

369           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "scripts\pas172_pilot_operations_readiness_check.py", line 372>:
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

Disassembly of <code object check_worker_off_by_default at 0x0000018C179A7290, file "scripts\pas172_pilot_operations_readiness_check.py", line 372>:
372           RESUME                   0

373           BUILD_LIST               0
              STORE_FAST               1 (out)

374           LOAD_GLOBAL              1 (Path + NULL)
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

375           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

377           LOAD_CONST               5 ('_ENV_FLAG_ENABLED_LITERAL = "true"')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         6 (to L2)
              NOT_TAKEN
              POP_TOP

378           LOAD_CONST               6 ("_ENV_FLAG_ENABLED_LITERAL = 'true'")
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)

376   L2:     STORE_FAST               4 (literal_ok)

380           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

381           LOAD_CONST               7 ('worker:off_by_default')

382           LOAD_FAST_BORROW         4 (literal_ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               8 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               9 ('FAIL')

383   L4:     LOAD_CONST              10 ('Pending-call worker is OFF by default (strict env literal)')

384           LOAD_GLOBAL              8 (SEVERITY_BLOCK)

385           LOAD_FAST_BORROW         4 (literal_ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST              11 ('missing strict enable-literal constant')

380   L6:     LOAD_CONST              12 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP

387           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "scripts\pas172_pilot_operations_readiness_check.py", line 390>:
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

Disassembly of <code object check_no_startup_worker at 0x0000018C17EA5040, file "scripts\pas172_pilot_operations_readiness_check.py", line 390>:
390           RESUME                   0

391           BUILD_LIST               0
              STORE_FAST               1 (out)

392           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('main.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

393           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               2 ('')
      L1:     STORE_FAST               3 (src)

394           LOAD_GLOBAL              5 (_strip_python_comments_and_strings + NULL)
              LOAD_FAST_BORROW         3 (src)
              CALL                     1
              STORE_FAST               4 (executable)

395           BUILD_LIST               0
              STORE_FAST               5 (bad)

396           LOAD_CONST               3 ('from app.services.ingestion.worker')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L2)
              NOT_TAKEN

397           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               4 ('from app.services.ingestion.worker import …')
              CALL                     1
              POP_TOP

398   L2:     LOAD_CONST               5 ('import app.services.ingestion.worker')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L3)
              NOT_TAKEN

399           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               5 ('import app.services.ingestion.worker')
              CALL                     1
              POP_TOP

400   L3:     LOAD_CONST               6 ('run_worker_loop')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L4)
              NOT_TAKEN

401           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               7 ('run_worker_loop reference')
              CALL                     1
              POP_TOP

402   L4:     LOAD_CONST               8 ('process_pending_call(')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L5)
              NOT_TAKEN

403           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               9 ('process_pending_call call')
              CALL                     1
              POP_TOP

404   L5:     LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

405           LOAD_CONST              10 ('main:no_startup_worker')

406           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L6)
              NOT_TAKEN
              LOAD_CONST              11 ('FAIL')
              JUMP_FORWARD             1 (to L7)
      L6:     LOAD_CONST              12 ('PASS')

407   L7:     LOAD_CONST              13 ('FastAPI lifespan does not auto-start the pending-call worker')

408           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

409           LOAD_FAST_BORROW         5 (bad)
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

404   L9:     LOAD_CONST              16 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP

411           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "scripts\pas172_pilot_operations_readiness_check.py", line 414>:
414           RESUME                   0
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

Disassembly of <code object check_heartbeat_service at 0x0000018C17F001D0, file "scripts\pas172_pilot_operations_readiness_check.py", line 414>:
414           RESUME                   0

415           BUILD_LIST               0
              STORE_FAST               1 (out)

416           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('services')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('worker')
              BINARY_OP               11 (/)
              LOAD_CONST               3 ('heartbeat_service.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

417           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

418           LOAD_GLOBAL              4 (REQUIRED_HEARTBEAT_SERVICE_TOKENS)
              GET_ITER
      L2:     FOR_ITER                78 (to L7)
              STORE_FAST               4 (tok)

419           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

420           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

421           LOAD_CONST               5 ('heartbeat_service:')
              LOAD_FAST_BORROW         4 (tok)
              LOAD_CONST               6 (slice(None, 48, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

422           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               7 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               8 ('FAIL')

423   L4:     LOAD_CONST               9 ('Heartbeat service token: ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

424           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

425           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             4 (to L6)
      L5:     LOAD_CONST              10 ('missing token ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

420   L6:     LOAD_CONST              11 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           80 (to L2)

418   L7:     END_FOR
              POP_ITER

427           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "scripts\pas172_pilot_operations_readiness_check.py", line 430>:
430           RESUME                   0
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

Disassembly of <code object check_heartbeat_monitor at 0x0000018C17F01040, file "scripts\pas172_pilot_operations_readiness_check.py", line 430>:
430           RESUME                   0

431           BUILD_LIST               0
              STORE_FAST               1 (out)

432           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('services')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('worker')
              BINARY_OP               11 (/)
              LOAD_CONST               3 ('heartbeat_monitor.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

433           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

434           LOAD_GLOBAL              4 (REQUIRED_HEARTBEAT_MONITOR_TOKENS)
              GET_ITER
      L2:     FOR_ITER                78 (to L7)
              STORE_FAST               4 (tok)

435           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

436           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

437           LOAD_CONST               5 ('heartbeat_monitor:')
              LOAD_FAST_BORROW         4 (tok)
              LOAD_CONST               6 (slice(None, 48, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

438           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               7 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               8 ('FAIL')

439   L4:     LOAD_CONST               9 ('Heartbeat monitor token: ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

440           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

441           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             4 (to L6)
      L5:     LOAD_CONST              10 ('missing token ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

436   L6:     LOAD_CONST              11 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           80 (to L2)

434   L7:     END_FOR
              POP_ITER

443           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "scripts\pas172_pilot_operations_readiness_check.py", line 446>:
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

Disassembly of <code object check_reaper_dedupe at 0x0000018C1801CDC0, file "scripts\pas172_pilot_operations_readiness_check.py", line 446>:
446           RESUME                   0

447           BUILD_LIST               0
              STORE_FAST               1 (out)

448           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('scripts')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('reap_pending_call_dedupe.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

449           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               2 ('')
      L1:     STORE_FAST               3 (src)

450           LOAD_GLOBAL              4 (REQUIRED_REAP_DEDUPE_TOKENS)
              GET_ITER
      L2:     FOR_ITER                78 (to L7)
              STORE_FAST               4 (tok)

451           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

452           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

453           LOAD_CONST               3 ('reap_dedupe:')
              LOAD_FAST_BORROW         4 (tok)
              LOAD_CONST               4 (slice(None, 48, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

454           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               5 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               6 ('FAIL')

455   L4:     LOAD_CONST               7 ('Pending-call dedupe reaper token: ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

456           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

457           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               2 ('')
              JUMP_FORWARD             4 (to L6)
      L5:     LOAD_CONST               8 ('missing token ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

452   L6:     LOAD_CONST               9 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           80 (to L2)

450   L7:     END_FOR
              POP_ITER

459           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "scripts\pas172_pilot_operations_readiness_check.py", line 462>:
462           RESUME                   0
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

Disassembly of <code object check_reaper_callback at 0x0000018C1801CFB0, file "scripts\pas172_pilot_operations_readiness_check.py", line 462>:
462           RESUME                   0

463           BUILD_LIST               0
              STORE_FAST               1 (out)

464           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('scripts')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('reap_callback_schedule.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

465           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               2 ('')
      L1:     STORE_FAST               3 (src)

466           LOAD_GLOBAL              4 (REQUIRED_REAP_CALLBACK_TOKENS)
              GET_ITER
      L2:     FOR_ITER                78 (to L7)
              STORE_FAST               4 (tok)

467           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

468           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

469           LOAD_CONST               3 ('reap_callback:')
              LOAD_FAST_BORROW         4 (tok)
              LOAD_CONST               4 (slice(None, 48, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

470           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               5 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               6 ('FAIL')

471   L4:     LOAD_CONST               7 ('Callback schedule reaper token: ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

472           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

473           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               2 ('')
              JUMP_FORWARD             4 (to L6)
      L5:     LOAD_CONST               8 ('missing token ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

468   L6:     LOAD_CONST               9 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           80 (to L2)

466   L7:     END_FOR
              POP_ITER

475           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA26A0, file "scripts\pas172_pilot_operations_readiness_check.py", line 478>:
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

Disassembly of <code object check_operator_ops at 0x0000018C17EFB9B0, file "scripts\pas172_pilot_operations_readiness_check.py", line 478>:
478            RESUME                   0

479            BUILD_LIST               0
               STORE_FAST               1 (out)

480            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('routes')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('operator_ops.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

481            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               3 ('')
       L1:     STORE_FAST               3 (src)

482            LOAD_GLOBAL              4 (REQUIRED_OPERATOR_OPS_TOKENS)
               GET_ITER
       L2:     FOR_ITER                78 (to L7)
               STORE_FAST               4 (tok)

483            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

484            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

485            LOAD_CONST               4 ('operator_ops:')
               LOAD_FAST_BORROW         4 (tok)
               LOAD_CONST               5 (slice(None, 48, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

486            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               6 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               7 ('FAIL')

487    L4:     LOAD_CONST               8 ('Operator ops route token: ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

488            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

489            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               3 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST               9 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

484    L6:     LOAD_CONST              10 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           80 (to L2)

482    L7:     END_FOR
               POP_ITER

493            LOAD_GLOBAL             13 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               6 (executable)

494            BUILD_LIST               0
               STORE_FAST               7 (bad)

495            LOAD_GLOBAL             14 (FORBIDDEN_OPS_EXPOSURE_TOKENS)
               GET_ITER
       L8:     FOR_ITER                28 (to L10)
               STORE_FAST               4 (tok)

496            LOAD_FAST_BORROW_LOAD_FAST_BORROW 70 (tok, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L9)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L8)

497    L9:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (tok)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L8)

495   L10:     END_FOR
               POP_ITER

498            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

499            LOAD_CONST              11 ('operator_ops:no_pii_exposure')

500            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               7 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               6 ('PASS')

501   L12:     LOAD_CONST              12 ('Operator ops routes do not reference transcript/raw payload')

502            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

503            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L13)
               NOT_TAKEN
               LOAD_CONST              13 ('disqualifying tokens: ')
               LOAD_CONST              14 (', ')
               LOAD_ATTR               17 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L14)
      L13:     LOAD_CONST               3 ('')

498   L14:     LOAD_CONST              10 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

506            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST              15 ('main.py')
               BINARY_OP               11 (/)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L15)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               3 ('')
      L15:     STORE_FAST               8 (main_src)

508            LOAD_CONST              16 ('operator_ops_router')
               LOAD_FAST_BORROW         8 (main_src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        6 (to L16)
               NOT_TAKEN
               POP_TOP

509            LOAD_CONST              17 ('prefix="/ops"')
               LOAD_FAST_BORROW         8 (main_src)
               CONTAINS_OP              0 (in)

507   L16:     STORE_FAST               9 (router_ok)

511            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

512            LOAD_CONST              18 ('operator_ops:router_mounted')

513            LOAD_FAST_BORROW         9 (router_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L17)
               NOT_TAKEN
               LOAD_CONST               6 ('PASS')
               JUMP_FORWARD             1 (to L18)
      L17:     LOAD_CONST               7 ('FAIL')

514   L18:     LOAD_CONST              19 ('operator_ops_router is mounted at /ops in app/main.py')

515            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

516            LOAD_FAST_BORROW         9 (router_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L19)
               NOT_TAKEN
               LOAD_CONST               3 ('')
               JUMP_FORWARD             1 (to L20)

517   L19:     LOAD_CONST              20 ('expected `operator_ops_router` import + `include_router(..., prefix="/ops")`')

511   L20:     LOAD_CONST              10 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

521            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2790, file "scripts\pas172_pilot_operations_readiness_check.py", line 524>:
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

Disassembly of <code object check_employee_mode at 0x0000018C17EDFB10, file "scripts\pas172_pilot_operations_readiness_check.py", line 524>:
524            RESUME                   0

525            BUILD_LIST               0
               STORE_FAST               1 (out)

526            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('services')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('slack')
               BINARY_OP               11 (/)
               LOAD_CONST               3 ('employee_mode.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

527            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')
       L1:     STORE_FAST               3 (src)

528            LOAD_GLOBAL              4 (REQUIRED_EMPLOYEE_MODE_TOKENS)
               GET_ITER
       L2:     FOR_ITER                78 (to L7)
               STORE_FAST               4 (tok)

529            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

530            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

531            LOAD_CONST               5 ('employee_mode:')
               LOAD_FAST_BORROW         4 (tok)
               LOAD_CONST               6 (slice(None, 48, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

532            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               8 ('FAIL')

533    L4:     LOAD_CONST               9 ('Slack employee-mode token: ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

534            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

535            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST              10 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

530    L6:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           80 (to L2)

528    L7:     END_FOR
               POP_ITER

538            LOAD_GLOBAL             13 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               6 (executable)

539            BUILD_LIST               0
               STORE_FAST               7 (bad_interactive)

540            LOAD_GLOBAL             14 (FORBIDDEN_SLACK_INTERACTIVE_TOKENS)
               GET_ITER
       L8:     FOR_ITER                28 (to L10)
               STORE_FAST               4 (tok)

541            LOAD_FAST_BORROW_LOAD_FAST_BORROW 70 (tok, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L9)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L8)

542    L9:     LOAD_FAST_BORROW         7 (bad_interactive)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (tok)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L8)

540   L10:     END_FOR
               POP_ITER

543            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

544            LOAD_CONST              12 ('employee_mode:no_interactive_components')

545            LOAD_FAST_BORROW         7 (bad_interactive)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               8 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               7 ('PASS')

546   L12:     LOAD_CONST              13 ('Slack employee mode has no interactive components')

547            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

549            LOAD_FAST_BORROW         7 (bad_interactive)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L13)
               NOT_TAKEN

548            LOAD_CONST              14 ('interactive tokens: ')
               LOAD_CONST              15 (', ')
               LOAD_ATTR               17 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad_interactive)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L14)

549   L13:     LOAD_CONST               4 ('')

543   L14:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

551            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA22E0, file "scripts\pas172_pilot_operations_readiness_check.py", line 554>:
554           RESUME                   0
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

Disassembly of <code object check_v20_sql at 0x0000018C181A00E0, file "scripts\pas172_pilot_operations_readiness_check.py", line 554>:
  --            MAKE_CELL               10 (src)

 554            RESUME                   0

 555            BUILD_LIST               0
                STORE_FAST               1 (out)

 556            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('scripts')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('migrate_v20_worker_heartbeats.sql')
                BINARY_OP               11 (/)
                STORE_FAST               2 (p)

 557            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (p)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L1:     STORE_DEREF             10 (src)

 558            LOAD_DEREF              10 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_FAST               3 (lower)

 559            LOAD_CONST               3 ('proposal only')
                LOAD_FAST_BORROW         3 (lower)
                CONTAINS_OP              0 (in)
                STORE_FAST               4 (proposal_ok)

 560            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 561            LOAD_CONST               4 ('v20_sql:proposal_only')

 562            LOAD_FAST_BORROW         4 (proposal_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L2)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               6 ('FAIL')

 563    L3:     LOAD_CONST               7 ("v20 SQL carries 'PROPOSAL ONLY' guardrail")

 564            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 565            LOAD_FAST_BORROW         4 (proposal_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L4)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L5)
        L4:     LOAD_CONST               8 ("missing 'PROPOSAL ONLY' label")

 560    L5:     LOAD_CONST               9 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 567            LOAD_CONST              10 ('do not execute')
                LOAD_FAST_BORROW         3 (lower)
                CONTAINS_OP              0 (in)
                STORE_FAST               5 (do_not_exec)

 568            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 569            LOAD_CONST              11 ('v20_sql:do_not_execute')

 570            LOAD_FAST_BORROW         5 (do_not_exec)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L7)
        L6:     LOAD_CONST               6 ('FAIL')

 571    L7:     LOAD_CONST              12 ("v20 SQL carries 'DO NOT EXECUTE' trailer")

 572            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 573            LOAD_FAST_BORROW         5 (do_not_exec)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST              13 ('missing trailer')

 568    L9:     LOAD_CONST               9 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 576            LOAD_GLOBAL             12 (all)
                COPY                     1
                LOAD_COMMON_CONSTANT     3 (<built-in function all>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L13)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW        10 (src)
                BUILD_TUPLE              1
                LOAD_CONST              14 (<code object <genexpr> at 0x0000018C18026430, file "scripts\pas172_pilot_operations_readiness_check.py", line 576>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 577            LOAD_CONST              33 (("'pending_call_worker'", "'callback_reminder_worker'", "'operator_reaper'", "'monitoring_dispatcher'"))
                GET_ITER

 576            CALL                     0
       L10:     FOR_ITER                12 (to L12)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L11)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L10)
       L11:     POP_ITER
                LOAD_CONST              15 (False)
                JUMP_FORWARD            20 (to L14)
       L12:     END_FOR
                POP_ITER
                LOAD_CONST              16 (True)
                JUMP_FORWARD            16 (to L14)
       L13:     PUSH_NULL
                LOAD_FAST_BORROW        10 (src)
                BUILD_TUPLE              1
                LOAD_CONST              14 (<code object <genexpr> at 0x0000018C18026430, file "scripts\pas172_pilot_operations_readiness_check.py", line 576>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 577            LOAD_CONST              33 (("'pending_call_worker'", "'callback_reminder_worker'", "'operator_reaper'", "'monitoring_dispatcher'"))
                GET_ITER

 576            CALL                     0
                CALL                     1
       L14:     STORE_FAST               6 (types_ok)

 584            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 585            LOAD_CONST              17 ('v20_sql:closed_worker_type_enum')

 586            LOAD_FAST_BORROW         6 (types_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L15)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L16)
       L15:     LOAD_CONST               6 ('FAIL')

 587   L16:     LOAD_CONST              18 ('v20 SQL carries the closed worker_type enum literals')

 588            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 589            LOAD_FAST_BORROW         6 (types_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L17)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L18)
       L17:     LOAD_CONST              19 ('missing one or more worker_type literals')

 584   L18:     LOAD_CONST               9 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 592            LOAD_GLOBAL             12 (all)
                COPY                     1
                LOAD_COMMON_CONSTANT     3 (<built-in function all>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L22)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW        10 (src)
                BUILD_TUPLE              1
                LOAD_CONST              20 (<code object <genexpr> at 0x0000018C18025E30, file "scripts\pas172_pilot_operations_readiness_check.py", line 592>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 593            LOAD_CONST              34 (("'STARTING'", "'RUNNING'", "'DEGRADED'", "'STOPPED'"))
                GET_ITER

 592            CALL                     0
       L19:     FOR_ITER                12 (to L21)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L20)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L19)
       L20:     POP_ITER
                LOAD_CONST              15 (False)
                JUMP_FORWARD            20 (to L23)
       L21:     END_FOR
                POP_ITER
                LOAD_CONST              16 (True)
                JUMP_FORWARD            16 (to L23)
       L22:     PUSH_NULL
                LOAD_FAST_BORROW        10 (src)
                BUILD_TUPLE              1
                LOAD_CONST              20 (<code object <genexpr> at 0x0000018C18025E30, file "scripts\pas172_pilot_operations_readiness_check.py", line 592>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 593            LOAD_CONST              34 (("'STARTING'", "'RUNNING'", "'DEGRADED'", "'STOPPED'"))
                GET_ITER

 592            CALL                     0
                CALL                     1
       L23:     STORE_FAST               7 (status_ok)

 600            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 601            LOAD_CONST              21 ('v20_sql:closed_status_enum')

 602            LOAD_FAST_BORROW         7 (status_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L24)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L25)
       L24:     LOAD_CONST               6 ('FAIL')

 603   L25:     LOAD_CONST              22 ('v20 SQL carries the closed status enum literals')

 604            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 605            LOAD_FAST_BORROW         7 (status_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L26)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L27)
       L26:     LOAD_CONST              23 ('missing one or more status literals')

 600   L27:     LOAD_CONST               9 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 608            LOAD_CONST              24 ('pas_worker_heartbeats_tenant_no_insert')
                LOAD_DEREF              10 (src)
                CONTAINS_OP              0 (in)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         6 (to L28)
                NOT_TAKEN
                POP_TOP

 609            LOAD_CONST              25 ('with check (false)')
                LOAD_FAST_BORROW         3 (lower)
                CONTAINS_OP              0 (in)

 607   L28:     STORE_FAST               8 (tenant_no_write)

 611            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 612            LOAD_CONST              26 ('v20_sql:tenant_no_write')

 613            LOAD_FAST_BORROW         8 (tenant_no_write)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L29)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L30)
       L29:     LOAD_CONST               6 ('FAIL')

 614   L30:     LOAD_CONST              27 ('v20 SQL denies tenant write')

 615            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 616            LOAD_FAST_BORROW         8 (tenant_no_write)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L31)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L32)
       L31:     LOAD_CONST              28 ('missing tenant-write denial')

 611   L32:     LOAD_CONST               9 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 618            LOAD_CONST              29 ('pas_worker_heartbeats_tenant_no_select')
                LOAD_DEREF              10 (src)
                CONTAINS_OP              0 (in)
                STORE_FAST               9 (tenant_no_select)

 619            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 620            LOAD_CONST              30 ('v20_sql:tenant_no_select')

 621            LOAD_FAST_BORROW         9 (tenant_no_select)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L33)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L34)
       L33:     LOAD_CONST               6 ('FAIL')

 622   L34:     LOAD_CONST              31 ('v20 SQL denies tenant SELECT (workers are operator-only)')

 623            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 624            LOAD_FAST_BORROW         9 (tenant_no_select)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L35)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L36)
       L35:     LOAD_CONST              32 ('missing tenant-select denial')

 619   L36:     LOAD_CONST               9 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 626            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18026430, file "scripts\pas172_pilot_operations_readiness_check.py", line 576>:
  --           COPY_FREE_VARS           1

 576           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 577   L2:     FOR_ITER                 9 (to L3)
               STORE_FAST_LOAD_FAST    17 (t, t)
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

Disassembly of <code object <genexpr> at 0x0000018C18025E30, file "scripts\pas172_pilot_operations_readiness_check.py", line 592>:
  --           COPY_FREE_VARS           1

 592           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 593   L2:     FOR_ITER                 9 (to L3)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA24C0, file "scripts\pas172_pilot_operations_readiness_check.py", line 629>:
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

Disassembly of <code object check_event_contract at 0x0000018C17FEE030, file "scripts\pas172_pilot_operations_readiness_check.py", line 629>:
629           RESUME                   0

630           BUILD_LIST               0
              STORE_FAST               1 (out)

631           LOAD_GLOBAL              1 (Path + NULL)
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

632           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

633           LOAD_GLOBAL              4 (REQUIRED_EVENT_TYPES)
              GET_ITER
      L2:     FOR_ITER                72 (to L7)
              STORE_FAST               4 (required)

634           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (required, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

635           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

636           LOAD_CONST               5 ('events:')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

637           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               6 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               7 ('FAIL')

638   L4:     LOAD_CONST               8 ('Event contract registers ')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

639           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

640           LOAD_FAST_BORROW         5 (ok)
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

635   L6:     LOAD_CONST              10 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           74 (to L2)

633   L7:     END_FOR
              POP_ITER

642           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA25B0, file "scripts\pas172_pilot_operations_readiness_check.py", line 645>:
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

Disassembly of <code object check_no_forbidden_imports at 0x0000018C17F84C80, file "scripts\pas172_pilot_operations_readiness_check.py", line 645>:
645            RESUME                   0

646            BUILD_LIST               0
               STORE_FAST               1 (out)

647            LOAD_CONST              10 (('app/services/worker/__init__.py', 'app/services/worker/heartbeat_service.py', 'app/services/worker/heartbeat_monitor.py', 'scripts/reap_pending_call_dedupe.py', 'scripts/reap_callback_schedule.py', 'app/routes/operator_ops.py', 'app/services/slack/__init__.py', 'app/services/slack/employee_mode.py', 'scripts/pas172_pilot_operations_readiness_check.py'))
               STORE_FAST               2 (files)

658            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     EXTENDED_ARG             1
               FOR_ITER               297 (to L15)
               STORE_FAST               3 (relpath)

659            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

660            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

661            JUMP_BACKWARD           46 (to L1)

662    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

663            BUILD_LIST               0
               STORE_FAST               6 (bad)

664            LOAD_FAST_BORROW         5 (src)
               LOAD_ATTR                7 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L4:     FOR_ITER               107 (to L10)
               STORE_FAST               7 (line)

665            LOAD_FAST_BORROW         7 (line)
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               STORE_FAST               8 (stripped)

666            LOAD_FAST_BORROW         8 (stripped)
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

667    L5:     JUMP_BACKWARD           52 (to L4)

668    L6:     LOAD_GLOBAL             12 (FORBIDDEN_IMPORT_LINE_PREFIXES)
               GET_ITER
       L7:     FOR_ITER                45 (to L9)
               STORE_FAST               9 (prefix)

669            LOAD_FAST_BORROW         8 (stripped)
               LOAD_ATTR               11 (startswith + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD           28 (to L7)

670    L8:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           47 (to L7)

668    L9:     END_FOR
               POP_ITER
               JUMP_BACKWARD          109 (to L4)

664   L10:     END_FOR
               POP_ITER

671            LOAD_FAST                1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             17 (_check + NULL)

672            LOAD_CONST               3 ('forbidden_import:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

673            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               4 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               5 ('PASS')

674   L12:     LOAD_CONST               6 ('No forbidden imports: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

675            LOAD_GLOBAL             18 (SEVERITY_BLOCK)

677            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       43 (to L13)
               NOT_TAKEN

676            LOAD_CONST               7 ('forbidden import prefixes: ')
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

677   L13:     LOAD_CONST               1 ('')

671   L14:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          300 (to L1)

658   L15:     END_FOR
               POP_ITER

679            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "scripts\pas172_pilot_operations_readiness_check.py", line 682>:
682           RESUME                   0
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

Disassembly of <code object check_no_inbox_scan_tokens at 0x0000018C17CD2160, file "scripts\pas172_pilot_operations_readiness_check.py", line 682>:
682            RESUME                   0

683            BUILD_LIST               0
               STORE_FAST               1 (out)

684            LOAD_CONST               9 (('app/services/worker/heartbeat_service.py', 'app/services/worker/heartbeat_monitor.py', 'scripts/reap_pending_call_dedupe.py', 'scripts/reap_callback_schedule.py', 'app/routes/operator_ops.py', 'app/services/slack/employee_mode.py', 'scripts/pas172_pilot_operations_readiness_check.py'))
               STORE_FAST               2 (files)

693            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               200 (to L11)
               STORE_FAST               3 (relpath)

694            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

695            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

696            JUMP_BACKWARD           45 (to L1)

697    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

698            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         5 (src)
               CALL                     1
               STORE_FAST               6 (executable)

699            BUILD_LIST               0
               STORE_FAST               7 (bad)

700            LOAD_GLOBAL              8 (FORBIDDEN_INBOX_TOKENS)
               GET_ITER
       L4:     FOR_ITER                28 (to L6)
               STORE_FAST               8 (token)

701            LOAD_FAST_BORROW_LOAD_FAST_BORROW 134 (token, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L4)

702    L5:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_FAST_BORROW         8 (token)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L4)

700    L6:     END_FOR
               POP_ITER

703            LOAD_FAST                1 (out)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_GLOBAL             13 (_check + NULL)

704            LOAD_CONST               2 ('no_inbox_scan:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

705            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L7)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L8)
       L7:     LOAD_CONST               4 ('PASS')

706    L8:     LOAD_CONST               5 ('No inbox-scanning tokens: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

707            LOAD_GLOBAL             14 (SEVERITY_BLOCK)

709            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L9)
               NOT_TAKEN

708            LOAD_CONST               6 ('inbox-scan tokens present: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               17 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L10)

709    L9:     LOAD_CONST               1 ('')

703   L10:     LOAD_CONST               8 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          202 (to L1)

693   L11:     END_FOR
               POP_ITER

711            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "scripts\pas172_pilot_operations_readiness_check.py", line 714>:
714           RESUME                   0
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

Disassembly of <code object check_docs_required_clauses at 0x0000018C17D8A770, file "scripts\pas172_pilot_operations_readiness_check.py", line 714>:
  --            MAKE_CELL                8 (lower)

 714            RESUME                   0

 715            BUILD_LIST               0
                STORE_FAST               1 (out)

 716            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('docs')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('pas172_pilot_operations_control_layer.md')
                BINARY_OP               11 (/)
                STORE_FAST               2 (doc)

 717            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (doc)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L1:     STORE_FAST               3 (src)

 718            LOAD_FAST_BORROW         3 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_DEREF              8 (lower)

 719            LOAD_CONST              13 ((('purpose', ('purpose',)), ('heartbeat', ('heartbeat',)), ('worker-off', ('off by default', 'operator-driven', 'operator driven')), ('slack-scope', ('slack employee mode', 'ops-only', 'outbound-display')), ('no-autonomous', ('no-autonomous', 'no autonomous', 'autonomous action')), ('reaper', ('reaper',)), ('stale-worker', ('stale worker',)), ('operator-checklist', ('operator checklist', 'runbook', 'pilot operator')), ('escalation', ('escalation',)), ('rollback', ('rollback',)), ('no-gmail', ('no gmail',)), ('not-built', ('intentionally not built', 'intentionally does not', 'deliberately not')), ('limitations', ('limitation',))))
                STORE_FAST               4 (required_phrases)

 741            LOAD_FAST_BORROW         4 (required_phrases)
                GET_ITER
        L2:     FOR_ITER               146 (to L12)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   86 (name, phrases)

 742            LOAD_GLOBAL              6 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         8 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18024F30, file "scripts\pas172_pilot_operations_readiness_check.py", line 742>)
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
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18024F30, file "scripts\pas172_pilot_operations_readiness_check.py", line 742>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         6 (phrases)
                GET_ITER
                CALL                     0
                CALL                     1
        L7:     STORE_FAST               7 (present)

 743            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 744            LOAD_CONST               6 ('docs:phrase:')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 745            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               8 ('FAIL')

 746    L9:     LOAD_CONST               9 ('Control-layer doc carries clause: ')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 747            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 749            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L10)
                NOT_TAKEN

 748            LOAD_CONST              10 ('expected one of: ')
                LOAD_CONST              11 (' | ')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_FAST_BORROW         6 (phrases)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L11)

 749   L10:     LOAD_CONST               2 ('')

 743   L11:     LOAD_CONST              12 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          148 (to L2)

 741   L12:     END_FOR
                POP_ITER

 751            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18024F30, file "scripts\pas172_pilot_operations_readiness_check.py", line 742>:
  --           COPY_FREE_VARS           1

 742           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "scripts\pas172_pilot_operations_readiness_check.py", line 754>:
754           RESUME                   0
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

Disassembly of <code object check_runbook_required_clauses at 0x0000018C17D8AA10, file "scripts\pas172_pilot_operations_readiness_check.py", line 754>:
  --            MAKE_CELL                8 (lower)

 754            RESUME                   0

 755            BUILD_LIST               0
                STORE_FAST               1 (out)

 756            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('docs')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('orvn_pilot_ops_runbook.md')
                BINARY_OP               11 (/)
                STORE_FAST               2 (doc)

 757            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (doc)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L1:     STORE_FAST               3 (src)

 758            LOAD_FAST_BORROW         3 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_DEREF              8 (lower)

 759            LOAD_CONST              13 ((('daily-quick-look', ('daily quick-look', 'daily quick look', 'quick-look')), ('heartbeat-setup', ('register_worker_heartbeat', 'wire heartbeats')), ('reapers', ('reap_pending_call_dedupe', 'reap_callback_schedule')), ('stale-recovery', ('recover_stale_dialing_rows', 'stale-dialing')), ('escalation', ('escalation',)), ('rollback', ('rollback',)), ('no-gmail', ('no gmail',)), ('doctrine', ('doctrine',)), ('end-of-pilot', ('end-of-pilot', 'end of pilot', 'post-mortem'))))
                STORE_FAST               4 (required_phrases)

 775            LOAD_FAST_BORROW         4 (required_phrases)
                GET_ITER
        L2:     FOR_ITER               146 (to L12)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   86 (name, phrases)

 776            LOAD_GLOBAL              6 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         8 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18025530, file "scripts\pas172_pilot_operations_readiness_check.py", line 776>)
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
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18025530, file "scripts\pas172_pilot_operations_readiness_check.py", line 776>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         6 (phrases)
                GET_ITER
                CALL                     0
                CALL                     1
        L7:     STORE_FAST               7 (present)

 777            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 778            LOAD_CONST               6 ('runbook:phrase:')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 779            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               8 ('FAIL')

 780    L9:     LOAD_CONST               9 ('Operator runbook carries clause: ')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 781            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 783            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L10)
                NOT_TAKEN

 782            LOAD_CONST              10 ('expected one of: ')
                LOAD_CONST              11 (' | ')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_FAST_BORROW         6 (phrases)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L11)

 783   L10:     LOAD_CONST               2 ('')

 777   L11:     LOAD_CONST              12 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          148 (to L2)

 775   L12:     END_FOR
                POP_ITER

 785            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18025530, file "scripts\pas172_pilot_operations_readiness_check.py", line 776>:
  --           COPY_FREE_VARS           1

 776           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "scripts\pas172_pilot_operations_readiness_check.py", line 788>:
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

Disassembly of <code object check_self_no_env_or_db at 0x0000018C17D884E0, file "scripts\pas172_pilot_operations_readiness_check.py", line 788>:
788            RESUME                   0

789            BUILD_LIST               0
               STORE_FAST               1 (out)

790            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_GLOBAL              2 (__file__)
               CALL                     1
               LOAD_ATTR                5 (resolve + NULL|self)
               CALL                     0
               STORE_FAST               2 (self_path)

791            LOAD_GLOBAL              7 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (self_path)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L1:     STORE_FAST               3 (src)

792            LOAD_GLOBAL              9 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               4 (executable)

793            BUILD_LIST               0
               STORE_FAST               5 (bad)

794            LOAD_FAST_BORROW         4 (executable)
               LOAD_ATTR               11 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L2:     FOR_ITER               199 (to L9)
               STORE_FAST               6 (raw_line)

795            LOAD_FAST_BORROW         6 (raw_line)
               LOAD_ATTR               13 (strip + NULL|self)
               CALL                     0
               STORE_FAST               7 (stripped)

796            LOAD_FAST_BORROW         7 (stripped)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN

797            JUMP_BACKWARD           29 (to L2)

798    L3:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              15 (('import dotenv', 'from dotenv'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L4)
               NOT_TAKEN

799            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               1 ('dotenv import')
               CALL                     1
               POP_TOP

800    L4:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              16 (('import supabase', 'from supabase'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L5)
               NOT_TAKEN

801            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               2 ('supabase import')
               CALL                     1
               POP_TOP

802    L5:     LOAD_CONST               3 ('load_dotenv()')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       18 (to L6)
               NOT_TAKEN

803            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               4 ('load_dotenv() call')
               CALL                     1
               POP_TOP

804    L6:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              17 (('os.environ[', 'getenv('))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L7)
               NOT_TAKEN

805            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               5 ('environ read')
               CALL                     1
               POP_TOP

806    L7:     LOAD_CONST               6 ('get_supabase')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD          182 (to L2)

807    L8:     LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               7 ('supabase client call')
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          201 (to L2)

794    L9:     END_FOR
               POP_ITER

808            LOAD_FAST                1 (out)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_GLOBAL             19 (_check + NULL)

809            LOAD_CONST               8 ('self_check:no_env_or_db')

810            LOAD_FAST_BORROW         5 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST               9 ('FAIL')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST              10 ('PASS')

811   L11:     LOAD_CONST              11 ('PAS172 readiness checker never reads .env / touches DB')

812            LOAD_GLOBAL             20 (SEVERITY_BLOCK)

813            LOAD_FAST_BORROW         5 (bad)
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

808   L13:     LOAD_CONST              14 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

815            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA30F0, file "scripts\pas172_pilot_operations_readiness_check.py", line 822>:
822           RESUME                   0
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

Disassembly of <code object _aggregate at 0x0000018C17EC5380, file "scripts\pas172_pilot_operations_readiness_check.py", line 822>:
 822            RESUME                   0

 824            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 823            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2

 824    L2:     FOR_ITER                49 (to L7)
                STORE_FAST               1 (c)

 825            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 824    L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L2)

 825    L4:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              2 (SEVERITY_BLOCK)
                COMPARE_OP              88 (bool(==))

 824    L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L2)
        L6:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L2)
        L7:     END_FOR
                POP_ITER

 823    L8:     STORE_FAST               2 (blockers)
                STORE_FAST               1 (c)

 828            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 827            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L9:     BUILD_LIST               0
                SWAP                     2

 828   L10:     FOR_ITER                49 (to L15)
                STORE_FAST               1 (c)

 829            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 828   L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L10)

 829   L12:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              4 (SEVERITY_INFO)
                COMPARE_OP              88 (bool(==))

 828   L13:     POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L10)
       L14:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L10)
       L15:     END_FOR
                POP_ITER

 827   L16:     STORE_FAST               3 (info)
                STORE_FAST               1 (c)

 832            LOAD_CONST               3 ('verdict')
                LOAD_FAST_BORROW         2 (blockers)
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L17)
                NOT_TAKEN
                LOAD_GLOBAL              6 (VERDICT_NOT_READY)
                JUMP_FORWARD             5 (to L18)
       L17:     LOAD_GLOBAL              8 (VERDICT_READY)

 833   L18:     LOAD_CONST               4 ('blockers')
                LOAD_FAST_BORROW         2 (blockers)

 834            LOAD_CONST               5 ('info')
                LOAD_FAST_BORROW         3 (info)

 831            BUILD_MAP                3
                RETURN_VALUE

  --   L19:     SWAP                     2
                POP_TOP

 823            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0

  --   L20:     SWAP                     2
                POP_TOP

 827            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L19 [2]
  L4 to L5 -> L19 [2]
  L6 to L8 -> L19 [2]
  L9 to L11 -> L20 [2]
  L12 to L13 -> L20 [2]
  L14 to L16 -> L20 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA3F00, file "scripts\pas172_pilot_operations_readiness_check.py", line 838>:
838           RESUME                   0
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

Disassembly of <code object _operator_actions at 0x0000018C18048C70, file "scripts\pas172_pilot_operations_readiness_check.py", line 838>:
838           RESUME                   0

839           BUILD_LIST               0
              STORE_FAST               1 (out)

840           LOAD_FAST_BORROW         0 (checks)
              GET_ITER
      L1:     FOR_ITER               109 (to L5)
              STORE_FAST               2 (c)

841           LOAD_FAST_BORROW         2 (c)
              LOAD_CONST               0 ('status')
              BINARY_OP               26 ([])
              LOAD_CONST               1 ('FAIL')
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

842           JUMP_BACKWARD           19 (to L1)

843   L2:     LOAD_FAST_BORROW         2 (c)
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

844           LOAD_FAST                1 (out)
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

840   L5:     END_FOR
              POP_ITER

845           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2010, file "scripts\pas172_pilot_operations_readiness_check.py", line 848>:
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
              LOAD_CONST               4 ('dict')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object evaluate at 0x0000018C17D8BF50, file "scripts\pas172_pilot_operations_readiness_check.py", line 848>:
848           RESUME                   0

849           BUILD_LIST               0
              STORE_FAST               1 (checks)

850           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              3 (check_files_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

851           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              5 (check_prior_phases_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

852           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              7 (check_memory_review_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

853           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              9 (check_worker_off_by_default + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

854           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             11 (check_no_startup_worker + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

855           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             13 (check_heartbeat_service + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

856           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             15 (check_heartbeat_monitor + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

857           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             17 (check_reaper_dedupe + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

858           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             19 (check_reaper_callback + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

859           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             21 (check_operator_ops + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

860           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             23 (check_employee_mode + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

861           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             25 (check_v20_sql + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

862           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             27 (check_event_contract + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

863           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             29 (check_no_forbidden_imports + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

864           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             31 (check_no_inbox_scan_tokens + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

865           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             33 (check_docs_required_clauses + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

866           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             35 (check_runbook_required_clauses + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

867           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             37 (check_self_no_env_or_db + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

869           LOAD_GLOBAL             39 (_aggregate + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1
              STORE_FAST               2 (agg)

871           LOAD_CONST               0 ('phase')
              LOAD_CONST               1 ('PAS172')

872           LOAD_CONST               2 ('generated_at')
              LOAD_GLOBAL             41 (_now_iso + NULL)
              CALL                     0

873           LOAD_CONST               3 ('verdict')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])

874           LOAD_CONST               4 ('ready')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])
              LOAD_GLOBAL             42 (VERDICT_READY)
              COMPARE_OP              72 (==)

875           LOAD_CONST               5 ('blocker_count')
              LOAD_GLOBAL             45 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               6 ('blockers')
              BINARY_OP               26 ([])
              CALL                     1

876           LOAD_CONST               7 ('info_count')
              LOAD_GLOBAL             45 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               8 ('info')
              BINARY_OP               26 ([])
              CALL                     1

877           LOAD_CONST               9 ('check_count')
              LOAD_GLOBAL             45 (len + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

878           LOAD_CONST              10 ('pass_count')
              LOAD_GLOBAL             47 (sum + NULL)
              LOAD_CONST              11 (<code object <genexpr> at 0x0000018C180533F0, file "scripts\pas172_pilot_operations_readiness_check.py", line 878>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

879           LOAD_CONST              12 ('fail_count')
              LOAD_GLOBAL             47 (sum + NULL)
              LOAD_CONST              13 (<code object <genexpr> at 0x0000018C18053090, file "scripts\pas172_pilot_operations_readiness_check.py", line 879>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

880           LOAD_CONST              14 ('checks')
              LOAD_FAST_BORROW         1 (checks)

881           LOAD_CONST              15 ('operator_actions')
              LOAD_GLOBAL             49 (_operator_actions + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

870           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C180533F0, file "scripts\pas172_pilot_operations_readiness_check.py", line 878>:
 878           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C18053090, file "scripts\pas172_pilot_operations_readiness_check.py", line 879>:
 879           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "scripts\pas172_pilot_operations_readiness_check.py", line 888>:
888           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C1801CBD0, file "scripts\pas172_pilot_operations_readiness_check.py", line 888>:
888           RESUME                   0

889           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

890           LOAD_CONST               0 ('pas172_pilot_operations_readiness_check')

892           LOAD_CONST               1 ('PAS172 — Evaluate the pilot operations control layer (worker heartbeat + reapers + Slack employee mode + operator ops routes). Read-only — never reads .env, never touches Supabase, never runs a migration.')

889           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

899           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

900           LOAD_CONST               3 ('--repo-root')
              LOAD_GLOBAL              6 (_REPO_ROOT_DEFAULT)

901           LOAD_CONST               4 ('Repo root (default: parent of this script).')

899           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

903           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

904           LOAD_CONST               6 ('--output')
              LOAD_GLOBAL              8 (REPORT_FILENAME)

905           LOAD_CONST               7 ('Where to write the JSON report (default ./')
              LOAD_GLOBAL              8 (REPORT_FILENAME)
              FORMAT_SIMPLE
              LOAD_CONST               8 (').')
              BUILD_STRING             3

903           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

907           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

908           LOAD_CONST               9 ('--json')
              LOAD_CONST              10 ('store_true')

909           LOAD_CONST              11 ('Emit JSON on stdout in addition to the summary.')

907           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

911           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

912           LOAD_CONST              13 ('--summary-only')
              LOAD_CONST              10 ('store_true')

913           LOAD_CONST              14 ('Skip writing the JSON report file.')

911           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

915           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

916           LOAD_CONST              15 ('--strict')
              LOAD_CONST              10 ('store_true')

917           LOAD_CONST              16 ('Exit 1 unless verdict == READY (default policy is the same).')

915           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

919           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3000, file "scripts\pas172_pilot_operations_readiness_check.py", line 922>:
922           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C17D8E300, file "scripts\pas172_pilot_operations_readiness_check.py", line 922>:
922           RESUME                   0

923           LOAD_GLOBAL              1 (print + NULL)

924           LOAD_CONST               0 ('[PAS172] verdict=')
              LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               1 ('verdict')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               2 (' blockers=')

925           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               3 ('blocker_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' info=')

926           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               5 ('info_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' checks=')

927           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               7 ('check_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' pass=')

928           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               9 ('pass_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              10 (' fail=')

929           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              11 ('fail_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE

924           BUILD_STRING            12

923           CALL                     1
              POP_TOP

931           LOAD_FAST_BORROW         0 (report)
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

932           LOAD_FAST_BORROW         1 (actions)
              TO_BOOL
              POP_JUMP_IF_FALSE       93 (to L5)
              NOT_TAKEN

933           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              13 ('[PAS172] operator actions:')
              CALL                     1
              POP_TOP

934           LOAD_FAST_BORROW         1 (actions)
              LOAD_CONST              14 (slice(None, 25, None))
              BINARY_OP               26 ([])
              GET_ITER
      L2:     FOR_ITER                17 (to L3)
              STORE_FAST               2 (a)

935           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              15 ('  - ')
              LOAD_FAST_BORROW         2 (a)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L2)

934   L3:     END_FOR
              POP_ITER

936           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         1 (actions)
              CALL                     1
              LOAD_SMALL_INT          25
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       34 (to L4)
              NOT_TAKEN

937           LOAD_GLOBAL              1 (print + NULL)
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

936   L4:     LOAD_CONST              18 (None)
              RETURN_VALUE

932   L5:     LOAD_CONST              18 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024930, file "scripts\pas172_pilot_operations_readiness_check.py", line 940>:
940           RESUME                   0
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

Disassembly of <code object _write_report at 0x0000018C180FC7B0, file "scripts\pas172_pilot_operations_readiness_check.py", line 940>:
 940           RESUME                   0

 941           NOP

 942   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

 943           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

 944           LOAD_CONST               3 ('utf-8')

 942           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 946           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

 947   L4:     LOAD_GLOBAL             11 (print + NULL)

 948           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

 949           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

 948           BUILD_STRING             4

 950           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

 947           LOAD_CONST               7 (('file',))
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

 946   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18114030, file "scripts\pas172_pilot_operations_readiness_check.py", line 954>:
954           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17D88FF0, file "scripts\pas172_pilot_operations_readiness_check.py", line 954>:
 954            RESUME                   0

 955            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 956            NOP

 957    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 961    L2:     LOAD_GLOBAL             10 (os)
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

 962            LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               21 (isdir + NULL|self)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L4)
                NOT_TAKEN

 963            LOAD_GLOBAL             23 (print + NULL)

 964            LOAD_CONST               2 ('error: --repo-root not a directory: ')
                LOAD_FAST                4 (repo_root)
                FORMAT_SIMPLE
                BUILD_STRING             2

 965            LOAD_GLOBAL             24 (sys)
                LOAD_ATTR               26 (stderr)

 963            LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

 967            LOAD_SMALL_INT           2
                RETURN_VALUE

 969    L4:     LOAD_GLOBAL             29 (evaluate + NULL)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                STORE_FAST               5 (report)

 971            LOAD_FAST                2 (args)
                LOAD_ATTR               30 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L5)
                NOT_TAKEN

 972            LOAD_GLOBAL             33 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               34 (output)
                LOAD_FAST                5 (report)
                CALL                     2
                POP_TOP

 974    L5:     LOAD_GLOBAL             37 (_print_summary + NULL)
                LOAD_FAST                5 (report)
                CALL                     1
                POP_TOP

 976            LOAD_FAST                2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L6)
                NOT_TAKEN

 977            LOAD_GLOBAL             23 (print + NULL)
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

 979    L6:     LOAD_FAST                5 (report)
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

 958            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L17)
                NOT_TAKEN
                STORE_FAST               3 (e)

 959    L9:     LOAD_FAST                3 (e)
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

 958   L17:     RERAISE                  0

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
