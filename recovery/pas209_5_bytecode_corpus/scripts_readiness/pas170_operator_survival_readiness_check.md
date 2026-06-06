# scripts_readiness/pas170_operator_survival_readiness_check

- **pyc:** `scripts\__pycache__\pas170_operator_survival_readiness_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/pas170_operator_survival_readiness_check.py`
- **co_filename (from bytecode):** `scripts\pas170_operator_survival_readiness_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS170 — Operator survival kit readiness gate.

Deterministic, non-mutating evaluator for "is the PAS170
survival kit wired correctly and free of regressions in the
PAS160–PAS169 doctrine?".

Walks the repo and verifies:

  * Pending-call dedupe + recovery modules exist and expose
    their documented surface.
  * Worker is still OFF by default
    (``_ENV_FLAG_ENABLED_LITERAL = "true"`` literal intact).
  * FastAPI lifespan in ``app/main.py`` does NOT auto-start
    the worker.
  * Stale-DIALING detection helper present.
  * Pending-call queue visibility helper present.
  * Callback schedule SQL is PROPOSAL ONLY.
  * Callback schedule service exposes the documented surface.
  * Slack alert transport is optional and structural-only
    (no PII fields in the allow-list).
  * Cal.com timezone is no longer hard-coded as the ONLY
    source (the resolver exists; the literal default remains
    as fallback).
  * Event contract registers every PAS170 event type.
  * No Slack interactive components added (no Block Kit
    actions / modals / slash commands).
  * No Gmail / Google / OAuth / IMAP / POP3 / inbox-scan /
    Memory Review / embedding / vector / Composio / TrustClaw
    imports.
  * Prior PAS160–PAS169 readiness scripts still exist.
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

`__annotate__`, `_aggregate`, `_build_parser`, `_check`, `_now_iso`, `_operator_actions`, `_print_summary`, `_read_text`, `_strip_python_comments_and_strings`, `_write_report`, `check_calcom_timezone_hotfix`, `check_callback_service`, `check_callback_sql_proposal`, `check_docs_required_doctrine`, `check_event_contract`, `check_files_present`, `check_memory_review_intact`, `check_no_forbidden_imports`, `check_no_inbox_scan_tokens`, `check_no_startup_worker`, `check_pending_call_dedupe`, `check_pending_call_recovery`, `check_prior_phases_intact`, `check_self_no_env_or_db`, `check_slack_alert_transport`, `check_worker_off_by_default`, `evaluate`, `main`

## Env-key candidates

`BLOCK`, `FAIL`, `INFO`, `NOT_READY`, `PAS170`, `PASS`, `READY`

## String constants (redacted where noted)

- '\nPAS170 — Operator survival kit readiness gate.\n\nDeterministic, non-mutating evaluator for "is the PAS170\nsurvival kit wired correctly and free of regressions in the\nPAS160–PAS169 doctrine?".\n\nWalks the repo and verifies:\n\n  * Pending-call dedupe + recovery modules exist and expose\n    their documented surface.\n  * Worker is still OFF by default\n    (``_ENV_FLAG_ENABLED_LITERAL = "true"`` literal intact).\n  * FastAPI lifespan in ``app/main.py`` does NOT auto-start\n    the worker.\n  * Stale-DIALING detection helper present.\n  * Pending-call queue visibility helper present.\n  * Callback schedule SQL is PROPOSAL ONLY.\n  * Callback schedule service exposes the documented surface.\n  * Slack alert transport is optional and structural-only\n    (no PII fields in the allow-list).\n  * Cal.com timezone is no longer hard-coded as the ONLY\n    source (the resolver exists; the literal default remains\n    as fallback).\n  * Event contract registers every PAS170 event type.\n  * No Slack interactive components added (no Block Kit\n    actions / modals / slash commands).\n  * No Gmail / Google / OAuth / IMAP / POP3 / inbox-scan /\n    Memory Review / embedding / vector / Composio / TrustClaw\n    imports.\n  * Prior PAS160–PAS169 readiness scripts still exist.\n  * Supports ``--summary-only`` / ``--json``.\n  * Exits 0 ready, 1 blockers, 2 bad args.\n  * Never reads ``.env``.\n  * Never touches production data.\n'
- 'utf-8'
- 'READY'
- 'NOT_READY'
- 'BLOCK'
- 'INFO'
- 'severity'
- 'detail'
- 'pas170_operator_survival_readiness_report.json'
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
- 'Required PAS170 file present: '
- 'missing'
- 'prior_phase:'
- 'Prior-phase script intact: '
- 'missing — PAS170 must not delete'
- 'memory_review:'
- 'Memory Review file present: '
- 'Memory Review file deleted'
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
- 'pending_call_dedupe.py'
- 'dedupe_token:'
- 'Pending-call dedupe carries token: '
- 'missing token '
- '_normalise_brokerage'
- 'dedupe:per_brokerage_scope'
- 'Dedupe key includes per-brokerage scope'
- 'missing brokerage normalisation'
- 'pending_calls.py'
- 'register_pending_call_dedupe'
- 'build_pending_call_dedupe_key'
- 'dedupe:wired_into_create_pending_call'
- 'create_pending_call calls the dedupe layer'
- 'missing dedupe wiring in pending_calls.py'
- 'pending_call_recovery.py'
- 'recovery_token:'
- 'Pending-call recovery carries token: '
- 'dry_run:             bool = True'
- 'dry_run: bool = True'
- 'dry_run:             bool=True'
- 'recovery:dry_run_by_default'
- 'recover_stale_dialing_rows is dry-run by default'
- 'expected dry_run default=True'
- 'callbacks'
- 'callback_schedule.py'
- 'callback_token:'
- 'Callback service carries token: '
- 'place_outbound_call('
- 'callback:no_auto_dial'
- 'Callback service does not auto-dial'
- 'auto-dial reference present in executable'
- 'scripts'
- 'migrate_v17_callback_schedule.sql'
- 'proposal only'
- 'callback_sql:proposal_only'
- "Callback schedule SQL carries 'PROPOSAL ONLY' guardrail"
- "missing 'PROPOSAL ONLY' label"
- 'do not execute'
- 'callback_sql:do_not_execute'
- "Callback schedule SQL carries 'DO NOT EXECUTE' trailer"
- 'missing trailer'
- 'tenant_no_insert'
- 'revoke insert'
- 'with check (false)'
- 'callback_sql:tenant_no_write'
- 'Callback schedule SQL denies tenant write'
- 'missing tenant-write denial'
- "'pending'"
- "'completed'"
- "'cancelled'"
- 'callback_sql:closed_status_enum'
- 'Callback schedule SQL carries closed status enum'
- 'missing status enum values'
- 'monitoring'
- 'slack_alert_transport.py'
- 'slack_token:'
- 'Slack transport carries token: '
- 'slack_webhook_not_configured'
- 'webhook_not_configured'
- 'slack:optional'
- 'Slack alert transport is optional (webhook resolves to skip)'
- 'missing skipped/not-configured path'
- 'slack:no_interactive_components'
- 'Slack transport has no interactive components'
- 'interactive tokens present: '
- '_ALERT_PAYLOAD_ALLOWED'
- '_ALLOWED_BLOCK_KEYS'
- 'slack:allow_list_excludes:'
- 'Slack allow-list excludes forbidden key: '
- 'forbidden allow-list key '
- ' present'
- 'booking'
- 'calcom_client.py'
- '_resolve_brokerage_timezone'
- 'calcom:timezone_resolver'
- 'Cal.com timezone resolver helper present'
- 'missing _resolve_brokerage_timezone'
- '"timeZone": tz_name'
- '"timeZone": booking_tz'
- '"timeZone": tz'
- '"timeZone": resolved_tz'
- 'calcom:timezone_variable_used'
- 'Cal.com payload uses a resolved timezone variable'
- 'expected timeZone payload to reference a resolved variable, not a string literal'
- 'events'
- 'contract.py'
- 'events:'
- 'Event contract registers '
- 'missing event type '
- 'app/services/ingestion/pending_call_dedupe.py'
- 'forbidden_import:'
- 'No forbidden imports: '
- 'forbidden import prefixes: '
- 'no_inbox_scan:'
- 'No inbox-scanning tokens: '
- 'inbox-scan tokens present: '
- 'docs'
- 'pas170_operator_survival_kit.md'
- 'docs:phrase:'
- 'Doc carries clause: '
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
- 'PAS170 readiness checker never reads .env / touches DB'
- 'disqualifying patterns: '
- 'checks'
- 'verdict'
- 'blockers'
- 'info'
- 'List[str]'
- ' — '
- 'see report'
- 'phase'
- 'PAS170'
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
- 'PAS170 — Evaluate the operator survival kit (worker resilience, pending-call dedupe, callback schedule, Slack alert transport, Cal.com timezone hotfix). Read-only — never reads .env, never touches Supabase, never runs a migration.'
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
- '[PAS170] verdict='
- ' blockers='
- ' info='
- ' checks='
- ' pass='
- ' fail='
- '[PAS170] operator actions:'
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

   1           LOAD_CONST               0 ('\nPAS170 — Operator survival kit readiness gate.\n\nDeterministic, non-mutating evaluator for "is the PAS170\nsurvival kit wired correctly and free of regressions in the\nPAS160–PAS169 doctrine?".\n\nWalks the repo and verifies:\n\n  * Pending-call dedupe + recovery modules exist and expose\n    their documented surface.\n  * Worker is still OFF by default\n    (``_ENV_FLAG_ENABLED_LITERAL = "true"`` literal intact).\n  * FastAPI lifespan in ``app/main.py`` does NOT auto-start\n    the worker.\n  * Stale-DIALING detection helper present.\n  * Pending-call queue visibility helper present.\n  * Callback schedule SQL is PROPOSAL ONLY.\n  * Callback schedule service exposes the documented surface.\n  * Slack alert transport is optional and structural-only\n    (no PII fields in the allow-list).\n  * Cal.com timezone is no longer hard-coded as the ONLY\n    source (the resolver exists; the literal default remains\n    as fallback).\n  * Event contract registers every PAS170 event type.\n  * No Slack interactive components added (no Block Kit\n    actions / modals / slash commands).\n  * No Gmail / Google / OAuth / IMAP / POP3 / inbox-scan /\n    Memory Review / embedding / vector / Composio / TrustClaw\n    imports.\n  * Prior PAS160–PAS169 readiness scripts still exist.\n  * Supports ``--summary-only`` / ``--json``.\n  * Exits 0 ready, 1 blockers, 2 bad args.\n  * Never reads ``.env``.\n  * Never touches production data.\n')
               STORE_NAME               0 (__doc__)

  38           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  40           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  41           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (json)
               STORE_NAME               4 (json)

  42           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (os)
               STORE_NAME               5 (os)

  43           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (sys)
               STORE_NAME               6 (sys)

  44           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              7 (datetime)
               IMPORT_FROM              7 (datetime)
               STORE_NAME               7 (datetime)
               IMPORT_FROM              8 (timezone)
               STORE_NAME               8 (timezone)
               POP_TOP

  45           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Path',))
               IMPORT_NAME              9 (pathlib)
               IMPORT_FROM             10 (Path)
               STORE_NAME              10 (Path)
               POP_TOP

  46           LOAD_SMALL_INT           0
               LOAD_CONST               5 (('List', 'Optional'))
               IMPORT_NAME             11 (typing)
               IMPORT_FROM             12 (List)
               STORE_NAME              12 (List)
               IMPORT_FROM             13 (Optional)
               STORE_NAME              13 (Optional)
               POP_TOP

  49           LOAD_NAME                6 (sys)
               LOAD_ATTR               28 (stdout)
               LOAD_NAME                6 (sys)
               LOAD_ATTR               30 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              16 (_stream)

  50           NOP

  51   L2:     LOAD_NAME               16 (_stream)
               LOAD_ATTR               35 (reconfigure + NULL|self)
               LOAD_CONST               6 ('utf-8')
               LOAD_CONST               7 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  49   L4:     END_FOR
               POP_ITER

  56           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               41 (abspath + NULL|self)

  57           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               43 (join + NULL|self)
               LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               45 (dirname + NULL|self)
               LOAD_NAME               23 (__file__)
               CALL                     1
               LOAD_CONST               8 ('..')
               CALL                     2

  56           CALL                     1
               STORE_NAME              24 (_REPO_ROOT_DEFAULT)

  61           LOAD_CONST               9 ('READY')
               STORE_NAME              25 (VERDICT_READY)

  62           LOAD_CONST              10 ('NOT_READY')
               STORE_NAME              26 (VERDICT_NOT_READY)

  64           LOAD_CONST              11 ('BLOCK')
               STORE_NAME              27 (SEVERITY_BLOCK)

  65           LOAD_CONST              12 ('INFO')
               STORE_NAME              28 (SEVERITY_INFO)

  72           LOAD_CONST              72 (('app/services/ingestion/pending_call_dedupe.py', 'app/services/ingestion/pending_call_recovery.py', 'app/services/callbacks/__init__.py', 'app/services/callbacks/callback_schedule.py', 'app/services/monitoring/slack_alert_transport.py', 'scripts/migrate_v17_callback_schedule.sql', 'scripts/pas170_operator_survival_readiness_check.py', 'scripts/pas170_demo_brokerage_smoke_plan.py', 'docs/pas170_operator_survival_kit.md', 'tests/mvp/test_pas170_operator_survival_kit.py'))
               STORE_NAME              29 (REQUIRED_FILES)

  85           LOAD_CONST              73 (('scripts/pas160_mvp_sequence_check.py', 'scripts/pas161_lead_ingestion_readiness_check.py', 'scripts/pas162_pending_calls_readiness_check.py', 'scripts/pas163_candidate_pipeline_readiness_check.py', 'scripts/pas164_email_ingestion_readiness_check.py', 'scripts/pas165_email_auth_dedupe_readiness_check.py', 'scripts/pas166_email_dedupe_policy_readiness_check.py', 'scripts/pas167_email_secret_reaper_readiness_check.py', 'scripts/pas168_email_secret_rotation_readiness_check.py', 'scripts/pas169_crypto_roundtrip_check.py', 'scripts/pas169_launch_readiness_check.py', 'scripts/pas_launch_integrity_check.py'))
               STORE_NAME              30 (PRIOR_PHASE_FILES)

 100           LOAD_CONST              74 (('app/services/memory/review.py', 'app/services/memory/review_stats.py', 'app/services/memory/review_export.py', 'app/services/memory/review_actors.py', 'app/services/memory/review_alerts.py', 'app/services/memory/operator_console.py'))
               STORE_NAME              31 (MEMORY_REVIEW_FILES)

 110           LOAD_CONST              75 (('def build_pending_call_dedupe_key(', 'def is_duplicate_pending_call(', 'def register_pending_call_dedupe(', 'PENDING_CALL_DEDUPE_TTL_SECONDS', 'duplicate_pending_call_suppressed'))
               STORE_NAME              32 (REQUIRED_DEDUPE_TOKENS)

 118           LOAD_CONST              76 (('def queue_status_report(', 'def detect_stale_dialing_rows(', 'def recover_stale_dialing_rows(', 'DEFAULT_STALE_AFTER_SECONDS'))
               STORE_NAME              33 (REQUIRED_RECOVERY_TOKENS)

 125           LOAD_CONST              77 (('def schedule_callback(', 'def list_pending_callbacks(', 'def reminder_report(', 'def mark_callback_completed(', 'def mark_callback_overdue(', 'ALLOWED_CALLBACK_STATUSES'))
               STORE_NAME              34 (REQUIRED_CALLBACK_TOKENS)

 134           LOAD_CONST              78 (('def send_alert_to_slack(', 'alert_to_safe_dict'))
               STORE_NAME              35 (REQUIRED_SLACK_TOKENS)

 143           LOAD_CONST              79 (('pending_call.stale_detected', 'pending_call.recovered', 'pending_call.duplicate_suppressed', 'callback.schedule.proposed', 'callback.reminder.due', 'alert.slack.sent', 'alert.slack.failed', 'provider.failure_storm.detected', 'worker.liveness.missing'))
               STORE_NAME              36 (REQUIRED_EVENT_TYPES)

 157           LOAD_CONST              80 (('phone', 'email', 'name', 'raw_payload', 'raw_email', 'raw_body', 'transcript', 'summary', 'secret', 'signature', 'dedupe_key'))
               STORE_NAME              37 (FORBIDDEN_BLOCK_TOKENS)

 171           LOAD_CONST              81 (('import gmail', 'from gmail', 'import googleapiclient', 'from googleapiclient', 'import google.oauth2', 'from google.oauth2', 'from google.auth', 'import google.auth', 'from google_auth_oauthlib', 'import imaplib', 'from imaplib', 'import poplib', 'from poplib', 'import composio', 'from composio', 'import trustclaw', 'from trustclaw', 'import chromadb', 'from chromadb', 'import pinecone', 'from pinecone', 'import langchain', 'from langchain', 'import numpy', 'import faiss', 'import pgvector', 'from pgvector', 'from openai import embeddings', 'from openai.embeddings', 'from app.services.memory', 'import app.services.memory'))
               STORE_NAME              38 (FORBIDDEN_IMPORT_LINE_PREFIXES)

 193           LOAD_CONST              82 (('imaplib', 'poplib', 'fetch_inbox', 'gmail_oauth', 'gmail_token', 'users().messages'))
               STORE_NAME              39 (FORBIDDEN_INBOX_TOKENS)

 205           LOAD_CONST              83 (('block_actions', 'view_submission', 'interactivity', '"type": "button"', '"type": "actions"', 'slash_command_callback'))
               STORE_NAME              40 (FORBIDDEN_SLACK_INTERACTIVE_TOKENS)

 219           LOAD_CONST              13 ('severity')

 221           LOAD_NAME               27 (SEVERITY_BLOCK)

 219           LOAD_CONST              14 ('detail')

 221           LOAD_CONST              15 ('')

 219           BUILD_MAP                2
               LOAD_CONST              16 (<code object __annotate__ at 0x0000018C18025A30, file "scripts\pas170_operator_survival_readiness_check.py", line 219>)
               MAKE_FUNCTION
               LOAD_CONST              17 (<code object _check at 0x0000018C17FA2F10, file "scripts\pas170_operator_survival_readiness_check.py", line 219>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              41 (_check)

 232           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA33C0, file "scripts\pas170_operator_survival_readiness_check.py", line 232>)
               MAKE_FUNCTION
               LOAD_CONST              19 (<code object _now_iso at 0x0000018C18038CB0, file "scripts\pas170_operator_survival_readiness_check.py", line 232>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              42 (_now_iso)

 236           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA35A0, file "scripts\pas170_operator_survival_readiness_check.py", line 236>)
               MAKE_FUNCTION
               LOAD_CONST              21 (<code object _read_text at 0x0000018C18053AB0, file "scripts\pas170_operator_survival_readiness_check.py", line 236>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              43 (_read_text)

 243           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA3D20, file "scripts\pas170_operator_survival_readiness_check.py", line 243>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object _strip_python_comments_and_strings at 0x0000018C17D81580, file "scripts\pas170_operator_survival_readiness_check.py", line 243>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              44 (_strip_python_comments_and_strings)

 282           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA1D40, file "scripts\pas170_operator_survival_readiness_check.py", line 282>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object check_files_present at 0x0000018C180608A0, file "scripts\pas170_operator_survival_readiness_check.py", line 282>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              45 (check_files_present)

 296           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA2880, file "scripts\pas170_operator_survival_readiness_check.py", line 296>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object check_prior_phases_intact at 0x0000018C18060A50, file "scripts\pas170_operator_survival_readiness_check.py", line 296>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              46 (check_prior_phases_intact)

 310           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA2100, file "scripts\pas170_operator_survival_readiness_check.py", line 310>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object check_memory_review_intact at 0x0000018C18060C00, file "scripts\pas170_operator_survival_readiness_check.py", line 310>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              47 (check_memory_review_intact)

 324           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA2B50, file "scripts\pas170_operator_survival_readiness_check.py", line 324>)
               MAKE_FUNCTION
               LOAD_CONST              31 (<code object check_worker_off_by_default at 0x0000018C179A7290, file "scripts\pas170_operator_survival_readiness_check.py", line 324>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              48 (check_worker_off_by_default)

 342           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA32D0, file "scripts\pas170_operator_survival_readiness_check.py", line 342>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object check_no_startup_worker at 0x0000018C17EA3FC0, file "scripts\pas170_operator_survival_readiness_check.py", line 342>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              49 (check_no_startup_worker)

 366           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA1E30, file "scripts\pas170_operator_survival_readiness_check.py", line 366>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object check_pending_call_dedupe at 0x0000018C17E56EA0, file "scripts\pas170_operator_survival_readiness_check.py", line 366>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              50 (check_pending_call_dedupe)

 407           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C17FA2E20, file "scripts\pas170_operator_survival_readiness_check.py", line 407>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object check_pending_call_recovery at 0x0000018C17EA4280, file "scripts\pas170_operator_survival_readiness_check.py", line 407>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              51 (check_pending_call_recovery)

 432           LOAD_CONST              38 (<code object __annotate__ at 0x0000018C17FA21F0, file "scripts\pas170_operator_survival_readiness_check.py", line 432>)
               MAKE_FUNCTION
               LOAD_CONST              39 (<code object check_callback_service at 0x0000018C17EA4AC0, file "scripts\pas170_operator_survival_readiness_check.py", line 432>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              52 (check_callback_service)

 463           LOAD_CONST              40 (<code object __annotate__ at 0x0000018C17FA26A0, file "scripts\pas170_operator_survival_readiness_check.py", line 463>)
               MAKE_FUNCTION
               LOAD_CONST              41 (<code object check_callback_sql_proposal at 0x0000018C17D88FF0, file "scripts\pas170_operator_survival_readiness_check.py", line 463>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              53 (check_callback_sql_proposal)

 512           LOAD_CONST              42 (<code object __annotate__ at 0x0000018C17FA2790, file "scripts\pas170_operator_survival_readiness_check.py", line 512>)
               MAKE_FUNCTION
               LOAD_CONST              43 (<code object check_slack_alert_transport at 0x0000018C17E59E70, file "scripts\pas170_operator_survival_readiness_check.py", line 512>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              54 (check_slack_alert_transport)

 574           LOAD_CONST              44 (<code object __annotate__ at 0x0000018C17FA22E0, file "scripts\pas170_operator_survival_readiness_check.py", line 574>)
               MAKE_FUNCTION
               LOAD_CONST              45 (<code object check_calcom_timezone_hotfix at 0x0000018C17D8AA10, file "scripts\pas170_operator_survival_readiness_check.py", line 574>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              55 (check_calcom_timezone_hotfix)

 613           LOAD_CONST              46 (<code object __annotate__ at 0x0000018C17FA24C0, file "scripts\pas170_operator_survival_readiness_check.py", line 613>)
               MAKE_FUNCTION
               LOAD_CONST              47 (<code object check_event_contract at 0x0000018C17FED630, file "scripts\pas170_operator_survival_readiness_check.py", line 613>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              56 (check_event_contract)

 629           LOAD_CONST              48 (<code object __annotate__ at 0x0000018C17FA25B0, file "scripts\pas170_operator_survival_readiness_check.py", line 629>)
               MAKE_FUNCTION
               LOAD_CONST              49 (<code object check_no_forbidden_imports at 0x0000018C17F84C80, file "scripts\pas170_operator_survival_readiness_check.py", line 629>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              57 (check_no_forbidden_imports)

 663           LOAD_CONST              50 (<code object __annotate__ at 0x0000018C17FA23D0, file "scripts\pas170_operator_survival_readiness_check.py", line 663>)
               MAKE_FUNCTION
               LOAD_CONST              51 (<code object check_no_inbox_scan_tokens at 0x0000018C17CD1490, file "scripts\pas170_operator_survival_readiness_check.py", line 663>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              58 (check_no_inbox_scan_tokens)

 694           LOAD_CONST              52 (<code object __annotate__ at 0x0000018C17FA2A60, file "scripts\pas170_operator_survival_readiness_check.py", line 694>)
               MAKE_FUNCTION
               LOAD_CONST              53 (<code object check_docs_required_doctrine at 0x0000018C17D8ACB0, file "scripts\pas170_operator_survival_readiness_check.py", line 694>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              59 (check_docs_required_doctrine)

 733           LOAD_CONST              54 (<code object __annotate__ at 0x0000018C17FA2C40, file "scripts\pas170_operator_survival_readiness_check.py", line 733>)
               MAKE_FUNCTION
               LOAD_CONST              55 (<code object check_self_no_env_or_db at 0x0000018C17D893A0, file "scripts\pas170_operator_survival_readiness_check.py", line 733>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              60 (check_self_no_env_or_db)

 767           LOAD_CONST              56 (<code object __annotate__ at 0x0000018C17FA3690, file "scripts\pas170_operator_survival_readiness_check.py", line 767>)
               MAKE_FUNCTION
               LOAD_CONST              57 (<code object _aggregate at 0x0000018C17EC4280, file "scripts\pas170_operator_survival_readiness_check.py", line 767>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              61 (_aggregate)

 783           LOAD_CONST              58 (<code object __annotate__ at 0x0000018C17FA30F0, file "scripts\pas170_operator_survival_readiness_check.py", line 783>)
               MAKE_FUNCTION
               LOAD_CONST              59 (<code object _operator_actions at 0x0000018C180483B0, file "scripts\pas170_operator_survival_readiness_check.py", line 783>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              62 (_operator_actions)

 793           LOAD_CONST              60 (<code object __annotate__ at 0x0000018C17FA3F00, file "scripts\pas170_operator_survival_readiness_check.py", line 793>)
               MAKE_FUNCTION
               LOAD_CONST              61 (<code object evaluate at 0x0000018C17E95410, file "scripts\pas170_operator_survival_readiness_check.py", line 793>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              63 (evaluate)

 828           LOAD_CONST              62 ('pas170_operator_survival_readiness_report.json')
               STORE_NAME              64 (REPORT_FILENAME)

 831           LOAD_CONST              63 (<code object __annotate__ at 0x0000018C17FA3870, file "scripts\pas170_operator_survival_readiness_check.py", line 831>)
               MAKE_FUNCTION
               LOAD_CONST              64 (<code object _build_parser at 0x0000018C1801CDC0, file "scripts\pas170_operator_survival_readiness_check.py", line 831>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              65 (_build_parser)

 866           LOAD_CONST              65 (<code object __annotate__ at 0x0000018C17FA3000, file "scripts\pas170_operator_survival_readiness_check.py", line 866>)
               MAKE_FUNCTION
               LOAD_CONST              66 (<code object _print_summary at 0x0000018C17D8E300, file "scripts\pas170_operator_survival_readiness_check.py", line 866>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              66 (_print_summary)

 884           LOAD_CONST              67 (<code object __annotate__ at 0x0000018C18025130, file "scripts\pas170_operator_survival_readiness_check.py", line 884>)
               MAKE_FUNCTION
               LOAD_CONST              68 (<code object _write_report at 0x0000018C180FC030, file "scripts\pas170_operator_survival_readiness_check.py", line 884>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              67 (_write_report)

 898           LOAD_CONST              84 ((None,))
               LOAD_CONST              69 (<code object __annotate__ at 0x0000018C18114030, file "scripts\pas170_operator_survival_readiness_check.py", line 898>)
               MAKE_FUNCTION
               LOAD_CONST              70 (<code object main at 0x0000018C17D88890, file "scripts\pas170_operator_survival_readiness_check.py", line 898>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              68 (main)

 926           LOAD_NAME               69 (__name__)
               LOAD_CONST              71 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 927           LOAD_NAME                6 (sys)
               LOAD_ATTR              140 (exit)
               PUSH_NULL
               LOAD_NAME               68 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 926   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  52           LOAD_NAME               18 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  53   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          353 (to L1)

  52   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025A30, file "scripts\pas170_operator_survival_readiness_check.py", line 219>:
219           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('check_id')

220           LOAD_CONST               2 ('str')

219           LOAD_CONST               3 ('status')

220           LOAD_CONST               2 ('str')

219           LOAD_CONST               4 ('label')

220           LOAD_CONST               2 ('str')

219           LOAD_CONST               5 ('severity')

221           LOAD_CONST               2 ('str')

219           LOAD_CONST               6 ('detail')

221           LOAD_CONST               2 ('str')

219           LOAD_CONST               7 ('return')

222           LOAD_CONST               8 ('dict')

219           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _check at 0x0000018C17FA2F10, file "scripts\pas170_operator_survival_readiness_check.py", line 219>:
219           RESUME                   0

224           LOAD_CONST               0 ('id')
              LOAD_FAST_BORROW         0 (check_id)

225           LOAD_CONST               1 ('status')
              LOAD_FAST_BORROW         1 (status)

226           LOAD_CONST               2 ('label')
              LOAD_FAST_BORROW         2 (label)

227           LOAD_CONST               3 ('severity')
              LOAD_FAST_BORROW         3 (severity)

228           LOAD_CONST               4 ('detail')
              LOAD_FAST_BORROW         4 (detail)

223           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "scripts\pas170_operator_survival_readiness_check.py", line 232>:
232           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038CB0, file "scripts\pas170_operator_survival_readiness_check.py", line 232>:
232           RESUME                   0

233           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "scripts\pas170_operator_survival_readiness_check.py", line 236>:
236           RESUME                   0
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

Disassembly of <code object _read_text at 0x0000018C18053AB0, file "scripts\pas170_operator_survival_readiness_check.py", line 236>:
 236           RESUME                   0

 237           NOP

 238   L1:     LOAD_FAST_BORROW         0 (path)
               LOAD_ATTR                1 (read_text + NULL|self)
               LOAD_CONST               0 ('utf-8')
               LOAD_CONST               1 ('replace')
               LOAD_CONST               2 (('encoding', 'errors'))
               CALL_KW                  2
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 239           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 240   L4:     POP_EXCEPT
               LOAD_CONST               3 (None)
               RETURN_VALUE

 239   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3D20, file "scripts\pas170_operator_survival_readiness_check.py", line 243>:
243           RESUME                   0
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

Disassembly of <code object _strip_python_comments_and_strings at 0x0000018C17D81580, file "scripts\pas170_operator_survival_readiness_check.py", line 243>:
243            RESUME                   0

244            BUILD_LIST               0
               STORE_FAST               1 (out)

245            LOAD_SMALL_INT           0
               LOAD_GLOBAL              1 (len + NULL)
               LOAD_FAST_BORROW         0 (src)
               CALL                     1
               STORE_FAST_STORE_FAST   50 (n, i)

246    L1:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (i, n)
               COMPARE_OP              18 (bool(<))
               EXTENDED_ARG             1
               POP_JUMP_IF_FALSE      282 (to L13)
               NOT_TAKEN

247            LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               BINARY_OP               26 ([])
               STORE_FAST               4 (ch)

248            LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               1 ('#')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       38 (to L3)
               NOT_TAKEN

249            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_CONST               2 ('\n')
               LOAD_FAST_BORROW         2 (i)
               CALL                     2
               STORE_FAST               5 (j)

250            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L2)
               NOT_TAKEN

251            JUMP_FORWARD           240 (to L13)

252    L2:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

253            JUMP_BACKWARD           59 (to L1)

254    L3:     LOAD_FAST_BORROW         0 (src)
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

255    L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               BINARY_SLICE
               STORE_FAST               6 (quote)

256            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 98 (quote, i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               CALL                     2
               STORE_FAST               7 (end)

257            LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L5)
               NOT_TAKEN

258            JUMP_FORWARD           138 (to L13)

259    L5:     LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

260            JUMP_BACKWARD          161 (to L1)

261    L6:     LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               7 (('"', "'"))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       92 (to L12)
               NOT_TAKEN

262            LOAD_FAST                4 (ch)
               STORE_FAST               6 (quote)

263            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               5 (j)

264    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (j, n)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       63 (to L11)
               NOT_TAKEN

265            LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
               BINARY_OP               26 ([])
               LOAD_CONST               5 ('\\')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       12 (to L8)
               NOT_TAKEN

266            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           2
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)

267            JUMP_BACKWARD           30 (to L7)

268    L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
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

269    L9:     JUMP_FORWARD            11 (to L11)

270   L10:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)
               JUMP_BACKWARD           68 (to L7)

271   L11:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

272            EXTENDED_ARG             1
               JUMP_BACKWARD          259 (to L1)

273   L12:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (ch)
               CALL                     1
               POP_TOP

274            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               2 (i)
               EXTENDED_ARG             1
               JUMP_BACKWARD          288 (to L1)

275   L13:     LOAD_CONST               6 ('')
               LOAD_ATTR                9 (join + NULL|self)
               LOAD_FAST_BORROW         1 (out)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1D40, file "scripts\pas170_operator_survival_readiness_check.py", line 282>:
282           RESUME                   0
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

Disassembly of <code object check_files_present at 0x0000018C180608A0, file "scripts\pas170_operator_survival_readiness_check.py", line 282>:
282           RESUME                   0

283           BUILD_LIST               0
              STORE_FAST               1 (out)

284           LOAD_GLOBAL              0 (REQUIRED_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

285           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

286           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

287           LOAD_CONST               0 ('file:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

288           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

289   L3:     LOAD_CONST               3 ('Required PAS170 file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

290           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

291           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing')

286   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

284   L6:     END_FOR
              POP_ITER

293           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "scripts\pas170_operator_survival_readiness_check.py", line 296>:
296           RESUME                   0
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

Disassembly of <code object check_prior_phases_intact at 0x0000018C18060A50, file "scripts\pas170_operator_survival_readiness_check.py", line 296>:
296           RESUME                   0

297           BUILD_LIST               0
              STORE_FAST               1 (out)

298           LOAD_GLOBAL              0 (PRIOR_PHASE_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

299           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

300           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

301           LOAD_CONST               0 ('prior_phase:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

302           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

303   L3:     LOAD_CONST               3 ('Prior-phase script intact: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

304           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

305           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing — PAS170 must not delete')

300   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

298   L6:     END_FOR
              POP_ITER

307           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "scripts\pas170_operator_survival_readiness_check.py", line 310>:
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

Disassembly of <code object check_memory_review_intact at 0x0000018C18060C00, file "scripts\pas170_operator_survival_readiness_check.py", line 310>:
310           RESUME                   0

311           BUILD_LIST               0
              STORE_FAST               1 (out)

312           LOAD_GLOBAL              0 (MEMORY_REVIEW_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
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

315           LOAD_CONST               0 ('memory_review:')
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

317   L3:     LOAD_CONST               3 ('Memory Review file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

318           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

319           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('Memory Review file deleted')

314   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

312   L6:     END_FOR
              POP_ITER

321           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "scripts\pas170_operator_survival_readiness_check.py", line 324>:
324           RESUME                   0
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

Disassembly of <code object check_worker_off_by_default at 0x0000018C179A7290, file "scripts\pas170_operator_survival_readiness_check.py", line 324>:
324           RESUME                   0

325           BUILD_LIST               0
              STORE_FAST               1 (out)

326           LOAD_GLOBAL              1 (Path + NULL)
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

327           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

329           LOAD_CONST               5 ('_ENV_FLAG_ENABLED_LITERAL = "true"')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         6 (to L2)
              NOT_TAKEN
              POP_TOP

330           LOAD_CONST               6 ("_ENV_FLAG_ENABLED_LITERAL = 'true'")
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)

328   L2:     STORE_FAST               4 (literal_ok)

332           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

333           LOAD_CONST               7 ('worker:off_by_default')

334           LOAD_FAST_BORROW         4 (literal_ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               8 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               9 ('FAIL')

335   L4:     LOAD_CONST              10 ('Pending-call worker is OFF by default (strict env literal)')

336           LOAD_GLOBAL              8 (SEVERITY_BLOCK)

337           LOAD_FAST_BORROW         4 (literal_ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST              11 ('missing strict enable-literal constant')

332   L6:     LOAD_CONST              12 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP

339           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA32D0, file "scripts\pas170_operator_survival_readiness_check.py", line 342>:
342           RESUME                   0
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

Disassembly of <code object check_no_startup_worker at 0x0000018C17EA3FC0, file "scripts\pas170_operator_survival_readiness_check.py", line 342>:
342           RESUME                   0

343           BUILD_LIST               0
              STORE_FAST               1 (out)

344           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('main.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

345           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               2 ('')
      L1:     STORE_FAST               3 (src)

346           LOAD_GLOBAL              5 (_strip_python_comments_and_strings + NULL)
              LOAD_FAST_BORROW         3 (src)
              CALL                     1
              STORE_FAST               4 (executable)

347           BUILD_LIST               0
              STORE_FAST               5 (bad)

348           LOAD_CONST               3 ('from app.services.ingestion.worker')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L2)
              NOT_TAKEN

349           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               4 ('from app.services.ingestion.worker import …')
              CALL                     1
              POP_TOP

350   L2:     LOAD_CONST               5 ('import app.services.ingestion.worker')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L3)
              NOT_TAKEN

351           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               5 ('import app.services.ingestion.worker')
              CALL                     1
              POP_TOP

352   L3:     LOAD_CONST               6 ('run_worker_loop')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L4)
              NOT_TAKEN

353           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               7 ('run_worker_loop reference')
              CALL                     1
              POP_TOP

354   L4:     LOAD_CONST               8 ('process_pending_call(')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L5)
              NOT_TAKEN

355           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               9 ('process_pending_call call')
              CALL                     1
              POP_TOP

356   L5:     LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

357           LOAD_CONST              10 ('main:no_startup_worker')

358           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L6)
              NOT_TAKEN
              LOAD_CONST              11 ('FAIL')
              JUMP_FORWARD             1 (to L7)
      L6:     LOAD_CONST              12 ('PASS')

359   L7:     LOAD_CONST              13 ('FastAPI lifespan does not auto-start the pending-call worker')

360           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

361           LOAD_FAST_BORROW         5 (bad)
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

356   L9:     LOAD_CONST              16 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP

363           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "scripts\pas170_operator_survival_readiness_check.py", line 366>:
366           RESUME                   0
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

Disassembly of <code object check_pending_call_dedupe at 0x0000018C17E56EA0, file "scripts\pas170_operator_survival_readiness_check.py", line 366>:
366            RESUME                   0

367            BUILD_LIST               0
               STORE_FAST               1 (out)

368            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('services')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('ingestion')
               BINARY_OP               11 (/)
               LOAD_CONST               3 ('pending_call_dedupe.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

369            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')
       L1:     STORE_FAST               3 (src)

370            LOAD_GLOBAL              4 (REQUIRED_DEDUPE_TOKENS)
               GET_ITER
       L2:     FOR_ITER                78 (to L7)
               STORE_FAST               4 (tok)

371            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

372            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

373            LOAD_CONST               5 ('dedupe_token:')
               LOAD_FAST_BORROW         4 (tok)
               LOAD_CONST               6 (slice(None, 40, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

374            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               8 ('FAIL')

375    L4:     LOAD_CONST               9 ('Pending-call dedupe carries token: ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

376            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

377            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST              10 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

372    L6:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           80 (to L2)

370    L7:     END_FOR
               POP_ITER

382            LOAD_CONST              12 ('_normalise_brokerage')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               STORE_FAST               6 (bid_ok)

383            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

384            LOAD_CONST              13 ('dedupe:per_brokerage_scope')

385            LOAD_FAST_BORROW         6 (bid_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST               8 ('FAIL')

386    L9:     LOAD_CONST              14 ('Dedupe key includes per-brokerage scope')

387            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

388            LOAD_FAST_BORROW         6 (bid_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST              15 ('missing brokerage normalisation')

383   L11:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

391            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('services')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('ingestion')
               BINARY_OP               11 (/)
               LOAD_CONST              16 ('pending_calls.py')
               BINARY_OP               11 (/)
               STORE_FAST               7 (seam)

392            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         7 (seam)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L12)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')
      L12:     STORE_FAST               8 (seam_src)

394            LOAD_CONST              17 ('register_pending_call_dedupe')
               LOAD_FAST_BORROW         8 (seam_src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        6 (to L13)
               NOT_TAKEN
               POP_TOP

395            LOAD_CONST              18 ('build_pending_call_dedupe_key')
               LOAD_FAST_BORROW         8 (seam_src)
               CONTAINS_OP              0 (in)

393   L13:     STORE_FAST               9 (wired)

397            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

398            LOAD_CONST              19 ('dedupe:wired_into_create_pending_call')

399            LOAD_FAST_BORROW         9 (wired)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L14)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L15)
      L14:     LOAD_CONST               8 ('FAIL')

400   L15:     LOAD_CONST              20 ('create_pending_call calls the dedupe layer')

401            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

402            LOAD_FAST_BORROW         9 (wired)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L16)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L17)
      L16:     LOAD_CONST              21 ('missing dedupe wiring in pending_calls.py')

397   L17:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

404            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "scripts\pas170_operator_survival_readiness_check.py", line 407>:
407           RESUME                   0
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

Disassembly of <code object check_pending_call_recovery at 0x0000018C17EA4280, file "scripts\pas170_operator_survival_readiness_check.py", line 407>:
407            RESUME                   0

408            BUILD_LIST               0
               STORE_FAST               1 (out)

409            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('services')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('ingestion')
               BINARY_OP               11 (/)
               LOAD_CONST               3 ('pending_call_recovery.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

410            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')
       L1:     STORE_FAST               3 (src)

411            LOAD_GLOBAL              4 (REQUIRED_RECOVERY_TOKENS)
               GET_ITER
       L2:     FOR_ITER                78 (to L7)
               STORE_FAST               4 (tok)

412            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

413            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

414            LOAD_CONST               5 ('recovery_token:')
               LOAD_FAST_BORROW         4 (tok)
               LOAD_CONST               6 (slice(None, 40, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

415            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               8 ('FAIL')

416    L4:     LOAD_CONST               9 ('Pending-call recovery carries token: ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

417            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

418            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST              10 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

413    L6:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           80 (to L2)

411    L7:     END_FOR
               POP_ITER

421            LOAD_CONST              12 ('dry_run:             bool = True')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        19 (to L8)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              13 ('dry_run: bool = True')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L8)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              14 ('dry_run:             bool=True')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
       L8:     STORE_FAST               6 (dry_default)

422            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

423            LOAD_CONST              15 ('recovery:dry_run_by_default')

424            LOAD_FAST_BORROW         6 (dry_default)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L10)
       L9:     LOAD_CONST               8 ('FAIL')

425   L10:     LOAD_CONST              16 ('recover_stale_dialing_rows is dry-run by default')

426            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

427            LOAD_FAST_BORROW         6 (dry_default)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST              17 ('expected dry_run default=True')

422   L12:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

429            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "scripts\pas170_operator_survival_readiness_check.py", line 432>:
432           RESUME                   0
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

Disassembly of <code object check_callback_service at 0x0000018C17EA4AC0, file "scripts\pas170_operator_survival_readiness_check.py", line 432>:
432            RESUME                   0

433            BUILD_LIST               0
               STORE_FAST               1 (out)

434            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('services')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('callbacks')
               BINARY_OP               11 (/)
               LOAD_CONST               3 ('callback_schedule.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

435            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')
       L1:     STORE_FAST               3 (src)

436            LOAD_GLOBAL              4 (REQUIRED_CALLBACK_TOKENS)
               GET_ITER
       L2:     FOR_ITER                78 (to L7)
               STORE_FAST               4 (tok)

437            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

438            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

439            LOAD_CONST               5 ('callback_token:')
               LOAD_FAST_BORROW         4 (tok)
               LOAD_CONST               6 (slice(None, 40, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

440            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               8 ('FAIL')

441    L4:     LOAD_CONST               9 ('Callback service carries token: ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

442            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

443            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST              10 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

438    L6:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           80 (to L2)

436    L7:     END_FOR
               POP_ITER

447            LOAD_GLOBAL             13 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               6 (executable)

449            LOAD_CONST              12 ('place_outbound_call(')
               LOAD_FAST_BORROW         6 (executable)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L8)
               NOT_TAKEN
               POP_TOP

450            LOAD_CONST              13 ('process_pending_call(')
               LOAD_FAST_BORROW         6 (executable)
               CONTAINS_OP              0 (in)

448    L8:     STORE_FAST               7 (auto_dial)

452            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

453            LOAD_CONST              14 ('callback:no_auto_dial')

454            LOAD_FAST_BORROW         7 (auto_dial)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN
               LOAD_CONST               8 ('FAIL')
               JUMP_FORWARD             1 (to L10)
       L9:     LOAD_CONST               7 ('PASS')

455   L10:     LOAD_CONST              15 ('Callback service does not auto-dial')

456            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

458            LOAD_FAST_BORROW         7 (auto_dial)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN

457            LOAD_CONST              16 ('auto-dial reference present in executable')
               JUMP_FORWARD             1 (to L12)

458   L11:     LOAD_CONST               4 ('')

452   L12:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

460            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA26A0, file "scripts\pas170_operator_survival_readiness_check.py", line 463>:
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

Disassembly of <code object check_callback_sql_proposal at 0x0000018C17D88FF0, file "scripts\pas170_operator_survival_readiness_check.py", line 463>:
463            RESUME                   0

464            BUILD_LIST               0
               STORE_FAST               1 (out)

465            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('scripts')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('migrate_v17_callback_schedule.sql')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

466            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               2 ('')
       L1:     STORE_FAST               3 (src)

467            LOAD_FAST_BORROW         3 (src)
               LOAD_ATTR                5 (lower + NULL|self)
               CALL                     0
               STORE_FAST               4 (lower)

468            LOAD_CONST               3 ('proposal only')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (proposal_ok)

469            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

470            LOAD_CONST               4 ('callback_sql:proposal_only')

471            LOAD_FAST_BORROW         5 (proposal_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L2)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L3)
       L2:     LOAD_CONST               6 ('FAIL')

472    L3:     LOAD_CONST               7 ("Callback schedule SQL carries 'PROPOSAL ONLY' guardrail")

473            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

474            LOAD_FAST_BORROW         5 (proposal_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L5)
       L4:     LOAD_CONST               8 ("missing 'PROPOSAL ONLY' label")

469    L5:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

476            LOAD_CONST              10 ('do not execute')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)
               STORE_FAST               6 (do_not_exec)

477            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

478            LOAD_CONST              11 ('callback_sql:do_not_execute')

479            LOAD_FAST_BORROW         6 (do_not_exec)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L6)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L7)
       L6:     LOAD_CONST               6 ('FAIL')

480    L7:     LOAD_CONST              12 ("Callback schedule SQL carries 'DO NOT EXECUTE' trailer")

481            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

482            LOAD_FAST_BORROW         6 (do_not_exec)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST              13 ('missing trailer')

477    L9:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

486            LOAD_CONST              14 ('tenant_no_insert')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        19 (to L10)
               NOT_TAKEN
               POP_TOP

487            LOAD_CONST              15 ('revoke insert')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)

486            COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L10)
               NOT_TAKEN
               POP_TOP

488            LOAD_CONST              16 ('with check (false)')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)

485   L10:     STORE_FAST               7 (tenant_no_write)

490            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

491            LOAD_CONST              17 ('callback_sql:tenant_no_write')

492            LOAD_FAST_BORROW         7 (tenant_no_write)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               6 ('FAIL')

493   L12:     LOAD_CONST              18 ('Callback schedule SQL denies tenant write')

494            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

495            LOAD_FAST_BORROW         7 (tenant_no_write)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L13)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L14)
      L13:     LOAD_CONST              19 ('missing tenant-write denial')

490   L14:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

499            LOAD_CONST              20 ("'pending'")
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       19 (to L15)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              21 ("'completed'")
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        6 (to L15)
               NOT_TAKEN
               POP_TOP

500            LOAD_CONST              22 ("'cancelled'")
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)

498   L15:     STORE_FAST               8 (status_enum_ok)

502            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

503            LOAD_CONST              23 ('callback_sql:closed_status_enum')

504            LOAD_FAST_BORROW         8 (status_enum_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L16)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L17)
      L16:     LOAD_CONST               6 ('FAIL')

505   L17:     LOAD_CONST              24 ('Callback schedule SQL carries closed status enum')

506            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

507            LOAD_FAST_BORROW         8 (status_enum_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L18)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L19)
      L18:     LOAD_CONST              25 ('missing status enum values')

502   L19:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

509            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2790, file "scripts\pas170_operator_survival_readiness_check.py", line 512>:
512           RESUME                   0
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

Disassembly of <code object check_slack_alert_transport at 0x0000018C17E59E70, file "scripts\pas170_operator_survival_readiness_check.py", line 512>:
512            RESUME                   0

513            BUILD_LIST               0
               STORE_FAST               1 (out)

514            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('services')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('monitoring')
               BINARY_OP               11 (/)
               LOAD_CONST               3 ('slack_alert_transport.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

515            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')
       L1:     STORE_FAST               3 (src)

516            LOAD_GLOBAL              4 (REQUIRED_SLACK_TOKENS)
               GET_ITER
       L2:     FOR_ITER                78 (to L7)
               STORE_FAST               4 (tok)

517            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

518            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

519            LOAD_CONST               5 ('slack_token:')
               LOAD_FAST_BORROW         4 (tok)
               LOAD_CONST               6 (slice(None, 40, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

520            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               8 ('FAIL')

521    L4:     LOAD_CONST               9 ('Slack transport carries token: ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

522            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

523            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST              10 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

518    L6:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           80 (to L2)

516    L7:     END_FOR
               POP_ITER

528            LOAD_CONST              12 ('slack_webhook_not_configured')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L8)
               NOT_TAKEN
               POP_TOP

529            LOAD_CONST              13 ('webhook_not_configured')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

527    L8:     STORE_FAST               6 (optional)

531            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

532            LOAD_CONST              14 ('slack:optional')

533            LOAD_FAST_BORROW         6 (optional)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L10)
       L9:     LOAD_CONST               8 ('FAIL')

534   L10:     LOAD_CONST              15 ('Slack alert transport is optional (webhook resolves to skip)')

535            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

536            LOAD_FAST_BORROW         6 (optional)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST              16 ('missing skipped/not-configured path')

531   L12:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

539            LOAD_GLOBAL             13 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               7 (executable)

540            BUILD_LIST               0
               STORE_FAST               8 (bad_interactive)

541            LOAD_GLOBAL             14 (FORBIDDEN_SLACK_INTERACTIVE_TOKENS)
               GET_ITER
      L13:     FOR_ITER                28 (to L15)
               STORE_FAST               4 (tok)

542            LOAD_FAST_BORROW_LOAD_FAST_BORROW 71 (tok, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L14)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L13)

543   L14:     LOAD_FAST_BORROW         8 (bad_interactive)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (tok)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L13)

541   L15:     END_FOR
               POP_ITER

544            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

545            LOAD_CONST              17 ('slack:no_interactive_components')

546            LOAD_FAST_BORROW         8 (bad_interactive)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L16)
               NOT_TAKEN
               LOAD_CONST               8 ('FAIL')
               JUMP_FORWARD             1 (to L17)
      L16:     LOAD_CONST               7 ('PASS')

547   L17:     LOAD_CONST              18 ('Slack transport has no interactive components')

548            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

551            LOAD_FAST_BORROW         8 (bad_interactive)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L18)
               NOT_TAKEN

549            LOAD_CONST              19 ('interactive tokens present: ')

550            LOAD_CONST              20 (', ')
               LOAD_ATTR               17 (join + NULL|self)
               LOAD_FAST_BORROW         8 (bad_interactive)
               CALL                     1

549            BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L19)

551   L18:     LOAD_CONST               4 ('')

544   L19:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

556            LOAD_FAST_BORROW         3 (src)
               LOAD_ATTR               19 (find + NULL|self)
               LOAD_CONST              21 ('_ALERT_PAYLOAD_ALLOWED')
               CALL                     1
               STORE_FAST               9 (allow_idx)

557            LOAD_FAST_BORROW         9 (allow_idx)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       18 (to L20)
               NOT_TAKEN

558            LOAD_FAST_BORROW         3 (src)
               LOAD_ATTR               19 (find + NULL|self)
               LOAD_CONST              22 ('_ALLOWED_BLOCK_KEYS')
               CALL                     1
               STORE_FAST               9 (allow_idx)

559   L20:     LOAD_FAST_BORROW         9 (allow_idx)
               LOAD_SMALL_INT           0
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE       12 (to L21)
               NOT_TAKEN
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 57 (src, allow_idx)
               LOAD_FAST_BORROW         9 (allow_idx)
               LOAD_CONST              23 (1024)
               BINARY_OP                0 (+)
               BINARY_SLICE
               JUMP_FORWARD             1 (to L22)
      L21:     LOAD_CONST               4 ('')
      L22:     STORE_FAST              10 (allow_window)

560            LOAD_GLOBAL             20 (FORBIDDEN_BLOCK_TOKENS)
               GET_ITER
      L23:     FOR_ITER                79 (to L28)
               STORE_FAST              11 (forbidden)

561            LOAD_CONST              24 ('"')
               LOAD_FAST_BORROW        11 (forbidden)
               FORMAT_SIMPLE
               LOAD_CONST              24 ('"')
               BUILD_STRING             3
               STORE_FAST              12 (candidate)

562            LOAD_FAST_BORROW_LOAD_FAST_BORROW 202 (candidate, allow_window)
               CONTAINS_OP              0 (in)
               STORE_FAST              13 (present)

563            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

564            LOAD_CONST              25 ('slack:allow_list_excludes:')
               LOAD_FAST_BORROW        11 (forbidden)
               FORMAT_SIMPLE
               BUILD_STRING             2

565            LOAD_FAST_BORROW        13 (present)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L24)
               NOT_TAKEN
               LOAD_CONST               8 ('FAIL')
               JUMP_FORWARD             1 (to L25)
      L24:     LOAD_CONST               7 ('PASS')

566   L25:     LOAD_CONST              26 ('Slack allow-list excludes forbidden key: ')
               LOAD_FAST_BORROW        11 (forbidden)
               FORMAT_SIMPLE
               BUILD_STRING             2

567            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

569            LOAD_FAST_BORROW        13 (present)
               TO_BOOL
               POP_JUMP_IF_FALSE        8 (to L26)
               NOT_TAKEN

568            LOAD_CONST              27 ('forbidden allow-list key ')
               LOAD_FAST_BORROW        11 (forbidden)
               CONVERT_VALUE            2 (repr)
               FORMAT_SIMPLE
               LOAD_CONST              28 (' present')
               BUILD_STRING             3
               JUMP_FORWARD             1 (to L27)

569   L26:     LOAD_CONST               4 ('')

563   L27:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           81 (to L23)

560   L28:     END_FOR
               POP_ITER

571            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA22E0, file "scripts\pas170_operator_survival_readiness_check.py", line 574>:
574           RESUME                   0
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

Disassembly of <code object check_calcom_timezone_hotfix at 0x0000018C17D8AA10, file "scripts\pas170_operator_survival_readiness_check.py", line 574>:
574            RESUME                   0

575            BUILD_LIST               0
               STORE_FAST               1 (out)

576            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('services')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('booking')
               BINARY_OP               11 (/)
               LOAD_CONST               3 ('calcom_client.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

577            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')
       L1:     STORE_FAST               3 (src)

579            LOAD_CONST               5 ('_resolve_brokerage_timezone')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               STORE_FAST               4 (resolver_ok)

580            LOAD_FAST                1 (out)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_GLOBAL              7 (_check + NULL)

581            LOAD_CONST               6 ('calcom:timezone_resolver')

582            LOAD_FAST_BORROW         4 (resolver_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L2)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L3)
       L2:     LOAD_CONST               8 ('FAIL')

583    L3:     LOAD_CONST               9 ('Cal.com timezone resolver helper present')

584            LOAD_GLOBAL              8 (SEVERITY_BLOCK)

585            LOAD_FAST_BORROW         4 (resolver_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L5)
       L4:     LOAD_CONST              10 ('missing _resolve_brokerage_timezone')

580    L5:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

595            LOAD_CONST              12 ('"timeZone": tz_name')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        32 (to L6)
               NOT_TAKEN
               POP_TOP

596            LOAD_CONST              13 ('"timeZone": booking_tz')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

595            COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        19 (to L6)
               NOT_TAKEN
               POP_TOP

597            LOAD_CONST              14 ('"timeZone": tz')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

595            COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L6)
               NOT_TAKEN
               POP_TOP

598            LOAD_CONST              15 ('"timeZone": resolved_tz')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

594    L6:     STORE_FAST               5 (uses_variable)

600            LOAD_FAST                1 (out)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_GLOBAL              7 (_check + NULL)

601            LOAD_CONST              16 ('calcom:timezone_variable_used')

602            LOAD_FAST_BORROW         5 (uses_variable)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L7)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L8)
       L7:     LOAD_CONST               8 ('FAIL')

603    L8:     LOAD_CONST              17 ('Cal.com payload uses a resolved timezone variable')

604            LOAD_GLOBAL              8 (SEVERITY_BLOCK)

605            LOAD_FAST_BORROW         5 (uses_variable)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L10)

606    L9:     LOAD_CONST              18 ('expected timeZone payload to reference a resolved variable, not a string literal')

600   L10:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

610            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA24C0, file "scripts\pas170_operator_survival_readiness_check.py", line 613>:
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

Disassembly of <code object check_event_contract at 0x0000018C17FED630, file "scripts\pas170_operator_survival_readiness_check.py", line 613>:
613           RESUME                   0

614           BUILD_LIST               0
              STORE_FAST               1 (out)

615           LOAD_GLOBAL              1 (Path + NULL)
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

616           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

617           LOAD_GLOBAL              4 (REQUIRED_EVENT_TYPES)
              GET_ITER
      L2:     FOR_ITER                72 (to L7)
              STORE_FAST               4 (required)

618           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (required, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

619           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

620           LOAD_CONST               5 ('events:')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

621           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               6 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               7 ('FAIL')

622   L4:     LOAD_CONST               8 ('Event contract registers ')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

623           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

624           LOAD_FAST_BORROW         5 (ok)
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

619   L6:     LOAD_CONST              10 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           74 (to L2)

617   L7:     END_FOR
              POP_ITER

626           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA25B0, file "scripts\pas170_operator_survival_readiness_check.py", line 629>:
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

Disassembly of <code object check_no_forbidden_imports at 0x0000018C17F84C80, file "scripts\pas170_operator_survival_readiness_check.py", line 629>:
629            RESUME                   0

630            BUILD_LIST               0
               STORE_FAST               1 (out)

631            LOAD_CONST              10 (('app/services/ingestion/pending_call_dedupe.py', 'app/services/ingestion/pending_call_recovery.py', 'app/services/callbacks/callback_schedule.py', 'app/services/monitoring/slack_alert_transport.py', 'scripts/pas170_operator_survival_readiness_check.py', 'scripts/pas170_demo_brokerage_smoke_plan.py'))
               STORE_FAST               2 (files)

639            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     EXTENDED_ARG             1
               FOR_ITER               297 (to L15)
               STORE_FAST               3 (relpath)

640            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

641            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

642            JUMP_BACKWARD           46 (to L1)

643    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

644            BUILD_LIST               0
               STORE_FAST               6 (bad)

645            LOAD_FAST_BORROW         5 (src)
               LOAD_ATTR                7 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L4:     FOR_ITER               107 (to L10)
               STORE_FAST               7 (line)

646            LOAD_FAST_BORROW         7 (line)
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               STORE_FAST               8 (stripped)

647            LOAD_FAST_BORROW         8 (stripped)
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

648    L5:     JUMP_BACKWARD           52 (to L4)

649    L6:     LOAD_GLOBAL             12 (FORBIDDEN_IMPORT_LINE_PREFIXES)
               GET_ITER
       L7:     FOR_ITER                45 (to L9)
               STORE_FAST               9 (prefix)

650            LOAD_FAST_BORROW         8 (stripped)
               LOAD_ATTR               11 (startswith + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD           28 (to L7)

651    L8:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           47 (to L7)

649    L9:     END_FOR
               POP_ITER
               JUMP_BACKWARD          109 (to L4)

645   L10:     END_FOR
               POP_ITER

652            LOAD_FAST                1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             17 (_check + NULL)

653            LOAD_CONST               3 ('forbidden_import:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

654            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               4 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               5 ('PASS')

655   L12:     LOAD_CONST               6 ('No forbidden imports: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

656            LOAD_GLOBAL             18 (SEVERITY_BLOCK)

658            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       43 (to L13)
               NOT_TAKEN

657            LOAD_CONST               7 ('forbidden import prefixes: ')
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

658   L13:     LOAD_CONST               1 ('')

652   L14:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          300 (to L1)

639   L15:     END_FOR
               POP_ITER

660            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "scripts\pas170_operator_survival_readiness_check.py", line 663>:
663           RESUME                   0
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

Disassembly of <code object check_no_inbox_scan_tokens at 0x0000018C17CD1490, file "scripts\pas170_operator_survival_readiness_check.py", line 663>:
663            RESUME                   0

664            BUILD_LIST               0
               STORE_FAST               1 (out)

665            LOAD_CONST               9 (('app/services/ingestion/pending_call_dedupe.py', 'app/services/ingestion/pending_call_recovery.py', 'app/services/callbacks/callback_schedule.py', 'app/services/monitoring/slack_alert_transport.py', 'scripts/pas170_operator_survival_readiness_check.py', 'scripts/pas170_demo_brokerage_smoke_plan.py'))
               STORE_FAST               2 (files)

673            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               200 (to L11)
               STORE_FAST               3 (relpath)

674            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

675            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

676            JUMP_BACKWARD           45 (to L1)

677    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

678            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         5 (src)
               CALL                     1
               STORE_FAST               6 (executable)

679            BUILD_LIST               0
               STORE_FAST               7 (bad)

680            LOAD_GLOBAL              8 (FORBIDDEN_INBOX_TOKENS)
               GET_ITER
       L4:     FOR_ITER                28 (to L6)
               STORE_FAST               8 (token)

681            LOAD_FAST_BORROW_LOAD_FAST_BORROW 134 (token, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L4)

682    L5:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_FAST_BORROW         8 (token)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L4)

680    L6:     END_FOR
               POP_ITER

683            LOAD_FAST                1 (out)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_GLOBAL             13 (_check + NULL)

684            LOAD_CONST               2 ('no_inbox_scan:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

685            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L7)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L8)
       L7:     LOAD_CONST               4 ('PASS')

686    L8:     LOAD_CONST               5 ('No inbox-scanning tokens: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

687            LOAD_GLOBAL             14 (SEVERITY_BLOCK)

689            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L9)
               NOT_TAKEN

688            LOAD_CONST               6 ('inbox-scan tokens present: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               17 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L10)

689    L9:     LOAD_CONST               1 ('')

683   L10:     LOAD_CONST               8 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          202 (to L1)

673   L11:     END_FOR
               POP_ITER

691            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "scripts\pas170_operator_survival_readiness_check.py", line 694>:
694           RESUME                   0
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

Disassembly of <code object check_docs_required_doctrine at 0x0000018C17D8ACB0, file "scripts\pas170_operator_survival_readiness_check.py", line 694>:
  --            MAKE_CELL                8 (lower)

 694            RESUME                   0

 695            BUILD_LIST               0
                STORE_FAST               1 (out)

 696            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('docs')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('pas170_operator_survival_kit.md')
                BINARY_OP               11 (/)
                STORE_FAST               2 (doc)

 697            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (doc)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L1:     STORE_FAST               3 (src)

 698            LOAD_FAST_BORROW         3 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_DEREF              8 (lower)

 699            LOAD_CONST              13 ((('purpose', ('purpose',)), ('worker-resilience', ('worker resilience', 'stale dialing', 'stale lock')), ('pending-dedupe', ('pending-call dedupe', 'duplicate suppression', 'duplicate pending call')), ('callback-lifecycle', ('callback lifecycle', 'callback schedule', 'reminder')), ('alert-transport', ('alert transport', 'slack webhook')), ('calcom-timezone', ('cal.com', 'timezone')), ('no-auto-enable', ('off by default', 'operator-driven', 'no auto-enable', 'operator driven')), ('no-gmail', ('no gmail',)), ('no-inbox', ('no inbox',)), ('not-built', ('intentionally not built', 'deliberately not', 'what is intentionally not')), ('brokerage-pilot', ('brokerage pilot', 'real brokerage', 'brokerage pilots')), ('limitations', ('limitation',))))
                STORE_FAST               4 (required_phrases)

 720            LOAD_FAST_BORROW         4 (required_phrases)
                GET_ITER
        L2:     FOR_ITER               146 (to L12)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   86 (name, phrases)

 721            LOAD_GLOBAL              6 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         8 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18026130, file "scripts\pas170_operator_survival_readiness_check.py", line 721>)
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
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18026130, file "scripts\pas170_operator_survival_readiness_check.py", line 721>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         6 (phrases)
                GET_ITER
                CALL                     0
                CALL                     1
        L7:     STORE_FAST               7 (present)

 722            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 723            LOAD_CONST               6 ('docs:phrase:')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 724            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               8 ('FAIL')

 725    L9:     LOAD_CONST               9 ('Doc carries clause: ')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 726            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 728            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L10)
                NOT_TAKEN

 727            LOAD_CONST              10 ('expected one of: ')
                LOAD_CONST              11 (' | ')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_FAST_BORROW         6 (phrases)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L11)

 728   L10:     LOAD_CONST               2 ('')

 722   L11:     LOAD_CONST              12 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          148 (to L2)

 720   L12:     END_FOR
                POP_ITER

 730            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18026130, file "scripts\pas170_operator_survival_readiness_check.py", line 721>:
  --           COPY_FREE_VARS           1

 721           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "scripts\pas170_operator_survival_readiness_check.py", line 733>:
733           RESUME                   0
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

Disassembly of <code object check_self_no_env_or_db at 0x0000018C17D893A0, file "scripts\pas170_operator_survival_readiness_check.py", line 733>:
733            RESUME                   0

734            BUILD_LIST               0
               STORE_FAST               1 (out)

735            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_GLOBAL              2 (__file__)
               CALL                     1
               LOAD_ATTR                5 (resolve + NULL|self)
               CALL                     0
               STORE_FAST               2 (self_path)

736            LOAD_GLOBAL              7 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (self_path)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L1:     STORE_FAST               3 (src)

737            LOAD_GLOBAL              9 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               4 (executable)

738            BUILD_LIST               0
               STORE_FAST               5 (bad)

739            LOAD_FAST_BORROW         4 (executable)
               LOAD_ATTR               11 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L2:     FOR_ITER               199 (to L9)
               STORE_FAST               6 (raw_line)

740            LOAD_FAST_BORROW         6 (raw_line)
               LOAD_ATTR               13 (strip + NULL|self)
               CALL                     0
               STORE_FAST               7 (stripped)

741            LOAD_FAST_BORROW         7 (stripped)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN

742            JUMP_BACKWARD           29 (to L2)

743    L3:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              15 (('import dotenv', 'from dotenv'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L4)
               NOT_TAKEN

744            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               1 ('dotenv import')
               CALL                     1
               POP_TOP

745    L4:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              16 (('import supabase', 'from supabase'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L5)
               NOT_TAKEN

746            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               2 ('supabase import')
               CALL                     1
               POP_TOP

747    L5:     LOAD_CONST               3 ('load_dotenv()')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       18 (to L6)
               NOT_TAKEN

748            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               4 ('load_dotenv() call')
               CALL                     1
               POP_TOP

749    L6:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              17 (('os.environ[', 'getenv('))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L7)
               NOT_TAKEN

750            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               5 ('environ read')
               CALL                     1
               POP_TOP

751    L7:     LOAD_CONST               6 ('get_supabase')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD          182 (to L2)

752    L8:     LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               7 ('supabase client call')
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          201 (to L2)

739    L9:     END_FOR
               POP_ITER

753            LOAD_FAST                1 (out)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_GLOBAL             19 (_check + NULL)

754            LOAD_CONST               8 ('self_check:no_env_or_db')

755            LOAD_FAST_BORROW         5 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST               9 ('FAIL')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST              10 ('PASS')

756   L11:     LOAD_CONST              11 ('PAS170 readiness checker never reads .env / touches DB')

757            LOAD_GLOBAL             20 (SEVERITY_BLOCK)

758            LOAD_FAST_BORROW         5 (bad)
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

753   L13:     LOAD_CONST              14 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

760            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "scripts\pas170_operator_survival_readiness_check.py", line 767>:
767           RESUME                   0
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

Disassembly of <code object _aggregate at 0x0000018C17EC4280, file "scripts\pas170_operator_survival_readiness_check.py", line 767>:
 767            RESUME                   0

 769            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 768            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2

 769    L2:     FOR_ITER                49 (to L7)
                STORE_FAST               1 (c)

 770            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 769    L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L2)

 770    L4:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              2 (SEVERITY_BLOCK)
                COMPARE_OP              88 (bool(==))

 769    L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L2)
        L6:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L2)
        L7:     END_FOR
                POP_ITER

 768    L8:     STORE_FAST               2 (blockers)
                STORE_FAST               1 (c)

 773            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 772            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L9:     BUILD_LIST               0
                SWAP                     2

 773   L10:     FOR_ITER                49 (to L15)
                STORE_FAST               1 (c)

 774            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 773   L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L10)

 774   L12:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              4 (SEVERITY_INFO)
                COMPARE_OP              88 (bool(==))

 773   L13:     POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L10)
       L14:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L10)
       L15:     END_FOR
                POP_ITER

 772   L16:     STORE_FAST               3 (info)
                STORE_FAST               1 (c)

 777            LOAD_CONST               3 ('verdict')
                LOAD_FAST_BORROW         2 (blockers)
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L17)
                NOT_TAKEN
                LOAD_GLOBAL              6 (VERDICT_NOT_READY)
                JUMP_FORWARD             5 (to L18)
       L17:     LOAD_GLOBAL              8 (VERDICT_READY)

 778   L18:     LOAD_CONST               4 ('blockers')
                LOAD_FAST_BORROW         2 (blockers)

 779            LOAD_CONST               5 ('info')
                LOAD_FAST_BORROW         3 (info)

 776            BUILD_MAP                3
                RETURN_VALUE

  --   L19:     SWAP                     2
                POP_TOP

 768            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0

  --   L20:     SWAP                     2
                POP_TOP

 772            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L19 [2]
  L4 to L5 -> L19 [2]
  L6 to L8 -> L19 [2]
  L9 to L11 -> L20 [2]
  L12 to L13 -> L20 [2]
  L14 to L16 -> L20 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA30F0, file "scripts\pas170_operator_survival_readiness_check.py", line 783>:
783           RESUME                   0
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

Disassembly of <code object _operator_actions at 0x0000018C180483B0, file "scripts\pas170_operator_survival_readiness_check.py", line 783>:
783           RESUME                   0

784           BUILD_LIST               0
              STORE_FAST               1 (out)

785           LOAD_FAST_BORROW         0 (checks)
              GET_ITER
      L1:     FOR_ITER               109 (to L5)
              STORE_FAST               2 (c)

786           LOAD_FAST_BORROW         2 (c)
              LOAD_CONST               0 ('status')
              BINARY_OP               26 ([])
              LOAD_CONST               1 ('FAIL')
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

787           JUMP_BACKWARD           19 (to L1)

788   L2:     LOAD_FAST_BORROW         2 (c)
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

789           LOAD_FAST                1 (out)
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

785   L5:     END_FOR
              POP_ITER

790           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3F00, file "scripts\pas170_operator_survival_readiness_check.py", line 793>:
793           RESUME                   0
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

Disassembly of <code object evaluate at 0x0000018C17E95410, file "scripts\pas170_operator_survival_readiness_check.py", line 793>:
793           RESUME                   0

794           BUILD_LIST               0
              STORE_FAST               1 (checks)

795           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              3 (check_files_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

796           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              5 (check_prior_phases_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

797           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              7 (check_memory_review_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

798           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              9 (check_worker_off_by_default + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

799           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             11 (check_no_startup_worker + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

800           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             13 (check_pending_call_dedupe + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

801           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             15 (check_pending_call_recovery + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

802           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             17 (check_callback_service + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

803           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             19 (check_callback_sql_proposal + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

804           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             21 (check_slack_alert_transport + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

805           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             23 (check_calcom_timezone_hotfix + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

806           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             25 (check_event_contract + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

807           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             27 (check_no_forbidden_imports + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

808           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             29 (check_no_inbox_scan_tokens + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

809           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             31 (check_docs_required_doctrine + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

810           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             33 (check_self_no_env_or_db + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

812           LOAD_GLOBAL             35 (_aggregate + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1
              STORE_FAST               2 (agg)

814           LOAD_CONST               0 ('phase')
              LOAD_CONST               1 ('PAS170')

815           LOAD_CONST               2 ('generated_at')
              LOAD_GLOBAL             37 (_now_iso + NULL)
              CALL                     0

816           LOAD_CONST               3 ('verdict')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])

817           LOAD_CONST               4 ('ready')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])
              LOAD_GLOBAL             38 (VERDICT_READY)
              COMPARE_OP              72 (==)

818           LOAD_CONST               5 ('blocker_count')
              LOAD_GLOBAL             41 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               6 ('blockers')
              BINARY_OP               26 ([])
              CALL                     1

819           LOAD_CONST               7 ('info_count')
              LOAD_GLOBAL             41 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               8 ('info')
              BINARY_OP               26 ([])
              CALL                     1

820           LOAD_CONST               9 ('check_count')
              LOAD_GLOBAL             41 (len + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

821           LOAD_CONST              10 ('pass_count')
              LOAD_GLOBAL             43 (sum + NULL)
              LOAD_CONST              11 (<code object <genexpr> at 0x0000018C180532D0, file "scripts\pas170_operator_survival_readiness_check.py", line 821>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

822           LOAD_CONST              12 ('fail_count')
              LOAD_GLOBAL             43 (sum + NULL)
              LOAD_CONST              13 (<code object <genexpr> at 0x0000018C18053630, file "scripts\pas170_operator_survival_readiness_check.py", line 822>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

823           LOAD_CONST              14 ('checks')
              LOAD_FAST_BORROW         1 (checks)

824           LOAD_CONST              15 ('operator_actions')
              LOAD_GLOBAL             45 (_operator_actions + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

813           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C180532D0, file "scripts\pas170_operator_survival_readiness_check.py", line 821>:
 821           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C18053630, file "scripts\pas170_operator_survival_readiness_check.py", line 822>:
 822           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "scripts\pas170_operator_survival_readiness_check.py", line 831>:
831           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C1801CDC0, file "scripts\pas170_operator_survival_readiness_check.py", line 831>:
831           RESUME                   0

832           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

833           LOAD_CONST               0 ('pas170_operator_survival_readiness_check')

835           LOAD_CONST               1 ('PAS170 — Evaluate the operator survival kit (worker resilience, pending-call dedupe, callback schedule, Slack alert transport, Cal.com timezone hotfix). Read-only — never reads .env, never touches Supabase, never runs a migration.')

832           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

843           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

844           LOAD_CONST               3 ('--repo-root')
              LOAD_GLOBAL              6 (_REPO_ROOT_DEFAULT)

845           LOAD_CONST               4 ('Repo root (default: parent of this script).')

843           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

847           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

848           LOAD_CONST               6 ('--output')
              LOAD_GLOBAL              8 (REPORT_FILENAME)

849           LOAD_CONST               7 ('Where to write the JSON report (default ./')
              LOAD_GLOBAL              8 (REPORT_FILENAME)
              FORMAT_SIMPLE
              LOAD_CONST               8 (').')
              BUILD_STRING             3

847           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

851           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

852           LOAD_CONST               9 ('--json')
              LOAD_CONST              10 ('store_true')

853           LOAD_CONST              11 ('Emit JSON on stdout in addition to the summary.')

851           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

855           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

856           LOAD_CONST              13 ('--summary-only')
              LOAD_CONST              10 ('store_true')

857           LOAD_CONST              14 ('Skip writing the JSON report file.')

855           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

859           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

860           LOAD_CONST              15 ('--strict')
              LOAD_CONST              10 ('store_true')

861           LOAD_CONST              16 ('Exit 1 unless verdict == READY (default policy is the same).')

859           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

863           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3000, file "scripts\pas170_operator_survival_readiness_check.py", line 866>:
866           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C17D8E300, file "scripts\pas170_operator_survival_readiness_check.py", line 866>:
866           RESUME                   0

867           LOAD_GLOBAL              1 (print + NULL)

868           LOAD_CONST               0 ('[PAS170] verdict=')
              LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               1 ('verdict')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               2 (' blockers=')

869           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               3 ('blocker_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' info=')

870           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               5 ('info_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' checks=')

871           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               7 ('check_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' pass=')

872           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               9 ('pass_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              10 (' fail=')

873           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              11 ('fail_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE

868           BUILD_STRING            12

867           CALL                     1
              POP_TOP

875           LOAD_FAST_BORROW         0 (report)
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

876           LOAD_FAST_BORROW         1 (actions)
              TO_BOOL
              POP_JUMP_IF_FALSE       93 (to L5)
              NOT_TAKEN

877           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              13 ('[PAS170] operator actions:')
              CALL                     1
              POP_TOP

878           LOAD_FAST_BORROW         1 (actions)
              LOAD_CONST              14 (slice(None, 25, None))
              BINARY_OP               26 ([])
              GET_ITER
      L2:     FOR_ITER                17 (to L3)
              STORE_FAST               2 (a)

879           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              15 ('  - ')
              LOAD_FAST_BORROW         2 (a)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L2)

878   L3:     END_FOR
              POP_ITER

880           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         1 (actions)
              CALL                     1
              LOAD_SMALL_INT          25
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       34 (to L4)
              NOT_TAKEN

881           LOAD_GLOBAL              1 (print + NULL)
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

880   L4:     LOAD_CONST              18 (None)
              RETURN_VALUE

876   L5:     LOAD_CONST              18 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025130, file "scripts\pas170_operator_survival_readiness_check.py", line 884>:
884           RESUME                   0
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

Disassembly of <code object _write_report at 0x0000018C180FC030, file "scripts\pas170_operator_survival_readiness_check.py", line 884>:
 884           RESUME                   0

 885           NOP

 886   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

 887           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

 888           LOAD_CONST               3 ('utf-8')

 886           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 890           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

 891   L4:     LOAD_GLOBAL             11 (print + NULL)

 892           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

 893           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

 892           BUILD_STRING             4

 894           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

 891           LOAD_CONST               7 (('file',))
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

 890   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18114030, file "scripts\pas170_operator_survival_readiness_check.py", line 898>:
898           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17D88890, file "scripts\pas170_operator_survival_readiness_check.py", line 898>:
 898            RESUME                   0

 899            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 900            NOP

 901    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 905    L2:     LOAD_GLOBAL             10 (os)
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

 906            LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               21 (isdir + NULL|self)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L4)
                NOT_TAKEN

 907            LOAD_GLOBAL             23 (print + NULL)

 908            LOAD_CONST               2 ('error: --repo-root not a directory: ')
                LOAD_FAST                4 (repo_root)
                FORMAT_SIMPLE
                BUILD_STRING             2

 909            LOAD_GLOBAL             24 (sys)
                LOAD_ATTR               26 (stderr)

 907            LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

 911            LOAD_SMALL_INT           2
                RETURN_VALUE

 913    L4:     LOAD_GLOBAL             29 (evaluate + NULL)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                STORE_FAST               5 (report)

 915            LOAD_FAST                2 (args)
                LOAD_ATTR               30 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L5)
                NOT_TAKEN

 916            LOAD_GLOBAL             33 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               34 (output)
                LOAD_FAST                5 (report)
                CALL                     2
                POP_TOP

 918    L5:     LOAD_GLOBAL             37 (_print_summary + NULL)
                LOAD_FAST                5 (report)
                CALL                     1
                POP_TOP

 920            LOAD_FAST                2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L6)
                NOT_TAKEN

 921            LOAD_GLOBAL             23 (print + NULL)
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

 923    L6:     LOAD_FAST                5 (report)
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

 902            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L17)
                NOT_TAKEN
                STORE_FAST               3 (e)

 903    L9:     LOAD_FAST                3 (e)
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

 902   L17:     RERAISE                  0

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
