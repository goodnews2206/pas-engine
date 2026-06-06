# scripts_readiness/pas171_external_pilot_readiness_check

- **pyc:** `scripts\__pycache__\pas171_external_pilot_readiness_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/pas171_external_pilot_readiness_check.py`
- **co_filename (from bytecode):** `scripts\pas171_external_pilot_readiness_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS171 — External pilot readiness gate.

Deterministic, non-mutating evaluator for "is PAS hardened
enough for one trusted external brokerage pilot?".

Walks the repo and verifies:

  * PAS160-PAS170 readiness scripts still exist (no regression).
  * PAS171 surfaces exist:
      - scripts/migrate_v18_pending_call_dedupe.sql
      - scripts/migrate_v19_callback_schedule.sql
      - app/services/ingestion/pending_call_dedupe_store.py
      - app/services/callbacks/callback_schedule_store.py
      - scripts/pas171_external_pilot_readiness_check.py
      - docs/pas171_external_pilot_hardening.md
      - docs/orvn_external_pilot_operator_checklist.md
      - tests/mvp/test_pas171_external_pilot_hardening.py
  * Migration v18 carries ``PROPOSAL ONLY`` + ``DO NOT EXECUTE``
    + tenant-write denial + sha256 shape constraint.
  * Migration v19 carries ``PROPOSAL ONLY`` + ``DO NOT EXECUTE``
    + tenant-write denial + the lower-case closed status enum
    + the partial unique index on (brokerage_id, source_call_id)
    where status IN (pending, reminded).
  * Durable pending-call dedupe store exposes the documented
    surface (register / is_duplicate / mark_duplicate_seen /
    enabled).
  * Durable callback schedule store exposes the documented
    surface (register / list / reminder_report / mark_* for
    each lifecycle status).
  * Slack pilot transport exposes
    ``send_pilot_alert_to_slack`` + ``emit_worker_liveness_
    heartbeat`` + ``emit_pilot_fallback_notice`` AND keeps the
    allow-list of alert id prefixes closed.
  * No Slack interactive components added.
  * Event contract registers every PAS171 event type.
  * No Gmail / Google / OAuth / IMAP / POP3 / inbox-scan /
    Memory Review / embedding / vector / Composio / TrustClaw
    imports in any PAS171 file.
  * Worker is still OFF by default
    (``_ENV_FLAG_ENABLED_LITERAL = "true"`` literal intact).
  * FastAPI lifespan in ``app/main.py`` does NOT auto-start
    the worker.
  * Docs carry the required clauses.
  * Operator checklist carries the required clauses
    (env-var enumeration, migration order, Cal.com probe,
    rollback path).
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

`__annotate__`, `_aggregate`, `_build_parser`, `_check`, `_now_iso`, `_operator_actions`, `_print_summary`, `_read_text`, `_strip_python_comments_and_strings`, `_write_report`, `check_callback_store_tokens`, `check_callback_v19_sql`, `check_dedupe_store_tokens`, `check_dedupe_v18_sql`, `check_doc_required_clauses`, `check_event_contract`, `check_files_present`, `check_memory_review_intact`, `check_no_forbidden_imports`, `check_no_inbox_scan_tokens`, `check_no_startup_worker`, `check_operator_checklist_clauses`, `check_prior_phases_intact`, `check_self_no_env_or_db`, `check_slack_pilot_hardening`, `check_worker_off_by_default`, `evaluate`, `main`

## Env-key candidates

`BLOCK`, `FAIL`, `INFO`, `NOT_READY`, `PAS171`, `PASS`, `READY`

## String constants (redacted where noted)

- '\nPAS171 — External pilot readiness gate.\n\nDeterministic, non-mutating evaluator for "is PAS hardened\nenough for one trusted external brokerage pilot?".\n\nWalks the repo and verifies:\n\n  * PAS160-PAS170 readiness scripts still exist (no regression).\n  * PAS171 surfaces exist:\n      - scripts/migrate_v18_pending_call_dedupe.sql\n      - scripts/migrate_v19_callback_schedule.sql\n      - app/services/ingestion/pending_call_dedupe_store.py\n      - app/services/callbacks/callback_schedule_store.py\n      - scripts/pas171_external_pilot_readiness_check.py\n      - docs/pas171_external_pilot_hardening.md\n      - docs/orvn_external_pilot_operator_checklist.md\n      - tests/mvp/test_pas171_external_pilot_hardening.py\n  * Migration v18 carries ``PROPOSAL ONLY`` + ``DO NOT EXECUTE``\n    + tenant-write denial + sha256 shape constraint.\n  * Migration v19 carries ``PROPOSAL ONLY`` + ``DO NOT EXECUTE``\n    + tenant-write denial + the lower-case closed status enum\n    + the partial unique index on (brokerage_id, source_call_id)\n    where status IN (pending, reminded).\n  * Durable pending-call dedupe store exposes the documented\n    surface (register / is_duplicate / mark_duplicate_seen /\n    enabled).\n  * Durable callback schedule store exposes the documented\n    surface (register / list / reminder_report / mark_* for\n    each lifecycle status).\n  * Slack pilot transport exposes\n    ``send_pilot_alert_to_slack`` + ``emit_worker_liveness_\n    heartbeat`` + ``emit_pilot_fallback_notice`` AND keeps the\n    allow-list of alert id prefixes closed.\n  * No Slack interactive components added.\n  * Event contract registers every PAS171 event type.\n  * No Gmail / Google / OAuth / IMAP / POP3 / inbox-scan /\n    Memory Review / embedding / vector / Composio / TrustClaw\n    imports in any PAS171 file.\n  * Worker is still OFF by default\n    (``_ENV_FLAG_ENABLED_LITERAL = "true"`` literal intact).\n  * FastAPI lifespan in ``app/main.py`` does NOT auto-start\n    the worker.\n  * Docs carry the required clauses.\n  * Operator checklist carries the required clauses\n    (env-var enumeration, migration order, Cal.com probe,\n    rollback path).\n  * Supports ``--summary-only`` / ``--json``.\n  * Exits 0 ready, 1 blockers, 2 bad args.\n  * Never reads ``.env``.\n  * Never touches production data.\n'
- 'utf-8'
- 'READY'
- 'NOT_READY'
- 'BLOCK'
- 'INFO'
- 'severity'
- 'detail'
- 'pas171_external_pilot_readiness_report.json'
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
- 'Required PAS171 file present: '
- 'missing'
- 'prior_phase:'
- 'Prior-phase readiness script intact: '
- 'missing — PAS171 must not delete'
- 'memory_review:'
- 'Memory Review file present: '
- 'Memory Review file deleted — PAS171 must not touch'
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
- 'pending_call_dedupe_store.py'
- 'dedupe_store_token:'
- 'Durable pending-call dedupe store token: '
- 'missing token '
- 'callbacks'
- 'callback_schedule_store.py'
- 'callback_store_token:'
- 'Durable callback schedule store token: '
- 'scripts'
- 'migrate_v18_pending_call_dedupe.sql'
- 'proposal only'
- 'dedupe_v18_sql:proposal_only'
- "v18 dedupe SQL carries 'PROPOSAL ONLY' guardrail"
- "missing 'PROPOSAL ONLY' label"
- 'do not execute'
- 'dedupe_v18_sql:do_not_execute'
- "v18 dedupe SQL carries 'DO NOT EXECUTE' trailer"
- 'missing trailer'
- 'pas_pending_call_dedupe_tenant_no_insert'
- 'with check (false)'
- 'dedupe_v18_sql:tenant_no_write'
- 'v18 dedupe SQL denies tenant write'
- 'missing tenant-write denial'
- '[0-9a-f]{64}'
- 'dedupe_v18_sql:sha256_shape'
- 'v18 dedupe SQL pins the dedupe_key shape to sha256 hex'
- 'missing sha256 shape CHECK constraint'
- 'for delete'
- 'no_delete'
- 'dedupe_v18_sql:no_delete_grant'
- 'v18 dedupe SQL has no DELETE grant (delete only present as a denial)'
- 'DELETE appears outside denial policy'
- 'migrate_v19_callback_schedule.sql'
- 'callback_v19_sql:proposal_only'
- "v19 callback SQL carries 'PROPOSAL ONLY' guardrail"
- 'callback_v19_sql:do_not_execute'
- "v19 callback SQL carries 'DO NOT EXECUTE' trailer"
- 'pas_callback_schedule_tenant_no_insert'
- 'callback_v19_sql:tenant_no_write'
- 'v19 callback SQL denies tenant write'
- "'pending'"
- "'reminded'"
- "'completed'"
- "'overdue'"
- "'cancelled'"
- "'failed'"
- 'callback_v19_sql:lower_case_status_enum'
- 'v19 callback SQL carries lower-case closed status enum'
- 'missing one or more lower-case status literals'
- 'create unique index'
- "where status in ('pending', 'reminded')"
- 'callback_v19_sql:partial_unique_active'
- 'v19 callback SQL has a partial unique index on active rows'
- "expected CREATE UNIQUE INDEX … WHERE status IN ('pending', 'reminded')"
- 'callback_v19_sql:no_delete_grant'
- 'v19 callback SQL has no DELETE grant (delete only present as a denial)'
- 'monitoring'
- 'slack_alert_transport.py'
- 'slack_pilot_token:'
- 'Slack pilot transport token: '
- 'slack:no_interactive_components'
- 'Slack pilot transport has no interactive components'
- 'interactive tokens present: '
- '_PILOT_ALERT_ID_ALLOWED_PREFIXES = ('
- 'worker.liveness.missing:'
- 'slack:pilot_alert_allow_list_closed'
- 'Pilot alert id allow-list is a closed literal tuple'
- 'expected literal tuple declaration + the canonical worker.liveness.missing: prefix'
- 'events'
- 'contract.py'
- 'events:'
- 'Event contract registers '
- 'missing event type '
- 'app/services/ingestion/pending_call_dedupe_store.py'
- 'forbidden_import:'
- 'No forbidden imports: '
- 'forbidden import prefixes: '
- 'no_inbox_scan:'
- 'No inbox-scanning tokens: '
- 'inbox-scan tokens present: '
- 'docs'
- 'pas171_external_pilot_hardening.md'
- 'docs:phrase:'
- 'Hardening doc carries clause: '
- 'expected one of: '
- ' | '
- 'orvn_external_pilot_operator_checklist.md'
- 'operator_checklist:phrase:'
- 'Operator checklist carries clause: '
- 'dotenv import'
- 'supabase import'
- 'load_dotenv()'
- 'load_dotenv() call'
- 'environ read'
- 'get_supabase'
- 'supabase client call'
- 'self_check:no_env_or_db'
- 'PAS171 readiness checker never reads .env / touches DB'
- 'disqualifying patterns: '
- 'checks'
- 'verdict'
- 'blockers'
- 'info'
- 'List[str]'
- ' — '
- 'see report'
- 'phase'
- 'PAS171'
- 'generated_at'
- 'ready'
- 'blocker_count'
- 'info_count'
- 'check_count'
- 'pass_count'
- 'fail_count'
- 'operator_actions'
- 'argparse.ArgumentParser'
- 'pas171_external_pilot_readiness_check'
- 'PAS171 — Evaluate external pilot hardening (durable pending-call dedupe + durable callback schedule + pilot Slack hardening + operator checklist). Read-only — never reads .env, never touches Supabase, never runs a migration.'
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
- '[PAS171] verdict='
- ' blockers='
- ' info='
- ' checks='
- ' pass='
- ' fail='
- '[PAS171] operator actions:'
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

   1           LOAD_CONST               0 ('\nPAS171 — External pilot readiness gate.\n\nDeterministic, non-mutating evaluator for "is PAS hardened\nenough for one trusted external brokerage pilot?".\n\nWalks the repo and verifies:\n\n  * PAS160-PAS170 readiness scripts still exist (no regression).\n  * PAS171 surfaces exist:\n      - scripts/migrate_v18_pending_call_dedupe.sql\n      - scripts/migrate_v19_callback_schedule.sql\n      - app/services/ingestion/pending_call_dedupe_store.py\n      - app/services/callbacks/callback_schedule_store.py\n      - scripts/pas171_external_pilot_readiness_check.py\n      - docs/pas171_external_pilot_hardening.md\n      - docs/orvn_external_pilot_operator_checklist.md\n      - tests/mvp/test_pas171_external_pilot_hardening.py\n  * Migration v18 carries ``PROPOSAL ONLY`` + ``DO NOT EXECUTE``\n    + tenant-write denial + sha256 shape constraint.\n  * Migration v19 carries ``PROPOSAL ONLY`` + ``DO NOT EXECUTE``\n    + tenant-write denial + the lower-case closed status enum\n    + the partial unique index on (brokerage_id, source_call_id)\n    where status IN (pending, reminded).\n  * Durable pending-call dedupe store exposes the documented\n    surface (register / is_duplicate / mark_duplicate_seen /\n    enabled).\n  * Durable callback schedule store exposes the documented\n    surface (register / list / reminder_report / mark_* for\n    each lifecycle status).\n  * Slack pilot transport exposes\n    ``send_pilot_alert_to_slack`` + ``emit_worker_liveness_\n    heartbeat`` + ``emit_pilot_fallback_notice`` AND keeps the\n    allow-list of alert id prefixes closed.\n  * No Slack interactive components added.\n  * Event contract registers every PAS171 event type.\n  * No Gmail / Google / OAuth / IMAP / POP3 / inbox-scan /\n    Memory Review / embedding / vector / Composio / TrustClaw\n    imports in any PAS171 file.\n  * Worker is still OFF by default\n    (``_ENV_FLAG_ENABLED_LITERAL = "true"`` literal intact).\n  * FastAPI lifespan in ``app/main.py`` does NOT auto-start\n    the worker.\n  * Docs carry the required clauses.\n  * Operator checklist carries the required clauses\n    (env-var enumeration, migration order, Cal.com probe,\n    rollback path).\n  * Supports ``--summary-only`` / ``--json``.\n  * Exits 0 ready, 1 blockers, 2 bad args.\n  * Never reads ``.env``.\n  * Never touches production data.\n')
               STORE_NAME               0 (__doc__)

  54           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  56           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  57           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (json)
               STORE_NAME               4 (json)

  58           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (os)
               STORE_NAME               5 (os)

  59           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (sys)
               STORE_NAME               6 (sys)

  60           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              7 (datetime)
               IMPORT_FROM              7 (datetime)
               STORE_NAME               7 (datetime)
               IMPORT_FROM              8 (timezone)
               STORE_NAME               8 (timezone)
               POP_TOP

  61           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Path',))
               IMPORT_NAME              9 (pathlib)
               IMPORT_FROM             10 (Path)
               STORE_NAME              10 (Path)
               POP_TOP

  62           LOAD_SMALL_INT           0
               LOAD_CONST               5 (('List', 'Optional'))
               IMPORT_NAME             11 (typing)
               IMPORT_FROM             12 (List)
               STORE_NAME              12 (List)
               IMPORT_FROM             13 (Optional)
               STORE_NAME              13 (Optional)
               POP_TOP

  65           LOAD_NAME                6 (sys)
               LOAD_ATTR               28 (stdout)
               LOAD_NAME                6 (sys)
               LOAD_ATTR               30 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              16 (_stream)

  66           NOP

  67   L2:     LOAD_NAME               16 (_stream)
               LOAD_ATTR               35 (reconfigure + NULL|self)
               LOAD_CONST               6 ('utf-8')
               LOAD_CONST               7 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  65   L4:     END_FOR
               POP_ITER

  72           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               41 (abspath + NULL|self)

  73           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               43 (join + NULL|self)
               LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               45 (dirname + NULL|self)
               LOAD_NAME               23 (__file__)
               CALL                     1
               LOAD_CONST               8 ('..')
               CALL                     2

  72           CALL                     1
               STORE_NAME              24 (_REPO_ROOT_DEFAULT)

  77           LOAD_CONST               9 ('READY')
               STORE_NAME              25 (VERDICT_READY)

  78           LOAD_CONST              10 ('NOT_READY')
               STORE_NAME              26 (VERDICT_NOT_READY)

  80           LOAD_CONST              11 ('BLOCK')
               STORE_NAME              27 (SEVERITY_BLOCK)

  81           LOAD_CONST              12 ('INFO')
               STORE_NAME              28 (SEVERITY_INFO)

  88           LOAD_CONST              72 (('scripts/migrate_v18_pending_call_dedupe.sql', 'scripts/migrate_v19_callback_schedule.sql', 'app/services/ingestion/pending_call_dedupe_store.py', 'app/services/callbacks/callback_schedule_store.py', 'scripts/pas171_external_pilot_readiness_check.py', 'docs/pas171_external_pilot_hardening.md', 'docs/orvn_external_pilot_operator_checklist.md', 'tests/mvp/test_pas171_external_pilot_hardening.py'))
               STORE_NAME              29 (REQUIRED_FILES)

  99           LOAD_CONST              73 (('scripts/pas160_mvp_sequence_check.py', 'scripts/pas161_lead_ingestion_readiness_check.py', 'scripts/pas162_pending_calls_readiness_check.py', 'scripts/pas163_candidate_pipeline_readiness_check.py', 'scripts/pas164_email_ingestion_readiness_check.py', 'scripts/pas165_email_auth_dedupe_readiness_check.py', 'scripts/pas166_email_dedupe_policy_readiness_check.py', 'scripts/pas167_email_secret_reaper_readiness_check.py', 'scripts/pas168_email_secret_rotation_readiness_check.py', 'scripts/pas169_crypto_roundtrip_check.py', 'scripts/pas169_launch_readiness_check.py', 'scripts/pas_launch_integrity_check.py', 'scripts/pas170_operator_survival_readiness_check.py'))
               STORE_NAME              30 (PRIOR_PHASE_FILES)

 115           LOAD_CONST              74 (('app/services/memory/review.py', 'app/services/memory/review_stats.py', 'app/services/memory/review_export.py', 'app/services/memory/review_actors.py', 'app/services/memory/review_alerts.py', 'app/services/memory/operator_console.py'))
               STORE_NAME              31 (MEMORY_REVIEW_FILES)

 125           LOAD_CONST              75 (('def durable_pending_call_dedupe_enabled(', 'def register_durable_pending_call_dedupe(', 'def is_duplicate_durable_pending_call_dedupe(', 'def mark_durable_pending_call_duplicate_seen(', '_TABLE = "pas_pending_call_dedupe"', 'durable_pending_call_dedupe_unavailable'))
               STORE_NAME              32 (REQUIRED_DEDUPE_STORE_TOKENS)

 134           LOAD_CONST              76 (('def durable_callback_schedule_enabled(', 'def register_durable_callback(', 'def list_durable_callbacks(', 'def durable_reminder_report(', 'def mark_durable_callback_reminded(', 'def mark_durable_callback_completed(', 'def mark_durable_callback_overdue(', 'def mark_durable_callback_cancelled(', 'def mark_durable_callback_failed(', 'DURABLE_CALLBACK_STATUSES', '_TABLE = "pas_callback_schedule"', 'durable_callback_schedule_unavailable'))
               STORE_NAME              33 (REQUIRED_CALLBACK_STORE_TOKENS)

 149           LOAD_CONST              77 (('def send_pilot_alert_to_slack(', 'def emit_worker_liveness_heartbeat(', 'def emit_pilot_fallback_notice(', '_PILOT_ALERT_ID_ALLOWED_PREFIXES', '_PILOT_ALERT_DEDUPE_SECONDS', '_PILOT_FORBIDDEN_BODY_TOKENS', 'pilot_alert_id_not_in_allow_list', 'pilot_alert_rate_limited', 'pilot_body_forbidden_token'))
               STORE_NAME              34 (REQUIRED_SLACK_PILOT_TOKENS)

 162           LOAD_CONST              78 (('pending_call.stale_detected', 'pending_call.recovered', 'pending_call.duplicate_suppressed', 'callback.schedule.proposed', 'callback.reminder.due', 'alert.slack.sent', 'alert.slack.failed', 'provider.failure_storm.detected', 'worker.liveness.missing', 'pending_call.dedupe.durable_registered', 'pending_call.dedupe.durable_duplicate', 'pending_call.dedupe.fallback_process_local', 'callback.schedule.durable_registered', 'callback.schedule.durable_duplicate', 'callback.schedule.fallback_process_local', 'external_pilot.heartbeat', 'external_pilot.dedupe_fallback', 'external_pilot.callback_schedule_fallback', 'external_pilot.cal_com_sanity_failed', 'external_pilot.cal_com_sanity_ok'))
               STORE_NAME              35 (REQUIRED_EVENT_TYPES)

 190           LOAD_CONST              79 (('import gmail', 'from gmail', 'import googleapiclient', 'from googleapiclient', 'import google.oauth2', 'from google.oauth2', 'from google.auth', 'import google.auth', 'from google_auth_oauthlib', 'import imaplib', 'from imaplib', 'import poplib', 'from poplib', 'import composio', 'from composio', 'import trustclaw', 'from trustclaw', 'import chromadb', 'from chromadb', 'import pinecone', 'from pinecone', 'import langchain', 'from langchain', 'import numpy', 'import faiss', 'import pgvector', 'from pgvector', 'from openai import embeddings', 'from openai.embeddings', 'from app.services.memory', 'import app.services.memory'))
               STORE_NAME              36 (FORBIDDEN_IMPORT_LINE_PREFIXES)

 212           LOAD_CONST              80 (('imaplib', 'poplib', 'fetch_inbox', 'gmail_oauth', 'gmail_token', 'users().messages'))
               STORE_NAME              37 (FORBIDDEN_INBOX_TOKENS)

 223           LOAD_CONST              81 (('block_actions', 'view_submission', 'interactivity', 'slash_command_callback'))
               STORE_NAME              38 (FORBIDDEN_SLACK_INTERACTIVE_TOKENS)

 235           LOAD_CONST              13 ('severity')

 237           LOAD_NAME               27 (SEVERITY_BLOCK)

 235           LOAD_CONST              14 ('detail')

 237           LOAD_CONST              15 ('')

 235           BUILD_MAP                2
               LOAD_CONST              16 (<code object __annotate__ at 0x0000018C18026230, file "scripts\pas171_external_pilot_readiness_check.py", line 235>)
               MAKE_FUNCTION
               LOAD_CONST              17 (<code object _check at 0x0000018C17FA3B40, file "scripts\pas171_external_pilot_readiness_check.py", line 235>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              39 (_check)

 248           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA34B0, file "scripts\pas171_external_pilot_readiness_check.py", line 248>)
               MAKE_FUNCTION
               LOAD_CONST              19 (<code object _now_iso at 0x0000018C18038B70, file "scripts\pas171_external_pilot_readiness_check.py", line 248>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              40 (_now_iso)

 252           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA3A50, file "scripts\pas171_external_pilot_readiness_check.py", line 252>)
               MAKE_FUNCTION
               LOAD_CONST              21 (<code object _read_text at 0x0000018C18053510, file "scripts\pas171_external_pilot_readiness_check.py", line 252>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              41 (_read_text)

 259           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA31E0, file "scripts\pas171_external_pilot_readiness_check.py", line 259>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object _strip_python_comments_and_strings at 0x0000018C18395BA0, file "scripts\pas171_external_pilot_readiness_check.py", line 259>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              42 (_strip_python_comments_and_strings)

 298           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA3E10, file "scripts\pas171_external_pilot_readiness_check.py", line 298>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object check_files_present at 0x0000018C18061470, file "scripts\pas171_external_pilot_readiness_check.py", line 298>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              43 (check_files_present)

 312           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA3960, file "scripts\pas171_external_pilot_readiness_check.py", line 312>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object check_prior_phases_intact at 0x0000018C180606F0, file "scripts\pas171_external_pilot_readiness_check.py", line 312>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              44 (check_prior_phases_intact)

 326           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA3C30, file "scripts\pas171_external_pilot_readiness_check.py", line 326>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object check_memory_review_intact at 0x0000018C18061110, file "scripts\pas171_external_pilot_readiness_check.py", line 326>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              45 (check_memory_review_intact)

 340           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C18114120, file "scripts\pas171_external_pilot_readiness_check.py", line 340>)
               MAKE_FUNCTION
               LOAD_CONST              31 (<code object check_worker_off_by_default at 0x0000018C1801C410, file "scripts\pas171_external_pilot_readiness_check.py", line 340>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              46 (check_worker_off_by_default)

 358           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C18114210, file "scripts\pas171_external_pilot_readiness_check.py", line 358>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object check_no_startup_worker at 0x0000018C17EA3D00, file "scripts\pas171_external_pilot_readiness_check.py", line 358>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              47 (check_no_startup_worker)

 382           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C181143F0, file "scripts\pas171_external_pilot_readiness_check.py", line 382>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object check_dedupe_store_tokens at 0x0000018C17F003E0, file "scripts\pas171_external_pilot_readiness_check.py", line 382>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              48 (check_dedupe_store_tokens)

 399           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C181144E0, file "scripts\pas171_external_pilot_readiness_check.py", line 399>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object check_callback_store_tokens at 0x0000018C17F00E30, file "scripts\pas171_external_pilot_readiness_check.py", line 399>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              49 (check_callback_store_tokens)

 416           LOAD_CONST              38 (<code object __annotate__ at 0x0000018C181145D0, file "scripts\pas171_external_pilot_readiness_check.py", line 416>)
               MAKE_FUNCTION
               LOAD_CONST              39 (<code object check_dedupe_v18_sql at 0x0000018C17EF9A30, file "scripts\pas171_external_pilot_readiness_check.py", line 416>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              50 (check_dedupe_v18_sql)

 472           LOAD_CONST              40 (<code object __annotate__ at 0x0000018C181146C0, file "scripts\pas171_external_pilot_readiness_check.py", line 472>)
               MAKE_FUNCTION
               LOAD_CONST              41 (<code object check_callback_v19_sql at 0x0000018C17D4D050, file "scripts\pas171_external_pilot_readiness_check.py", line 472>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              51 (check_callback_v19_sql)

 548           LOAD_CONST              42 (<code object __annotate__ at 0x0000018C181147B0, file "scripts\pas171_external_pilot_readiness_check.py", line 548>)
               MAKE_FUNCTION
               LOAD_CONST              43 (<code object check_slack_pilot_hardening at 0x0000018C17D88C40, file "scripts\pas171_external_pilot_readiness_check.py", line 548>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              52 (check_slack_pilot_hardening)

 599           LOAD_CONST              44 (<code object __annotate__ at 0x0000018C181148A0, file "scripts\pas171_external_pilot_readiness_check.py", line 599>)
               MAKE_FUNCTION
               LOAD_CONST              45 (<code object check_event_contract at 0x0000018C17FEE430, file "scripts\pas171_external_pilot_readiness_check.py", line 599>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              53 (check_event_contract)

 615           LOAD_CONST              46 (<code object __annotate__ at 0x0000018C18114990, file "scripts\pas171_external_pilot_readiness_check.py", line 615>)
               MAKE_FUNCTION
               LOAD_CONST              47 (<code object check_no_forbidden_imports at 0x0000018C17EA7670, file "scripts\pas171_external_pilot_readiness_check.py", line 615>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              54 (check_no_forbidden_imports)

 646           LOAD_CONST              48 (<code object __annotate__ at 0x0000018C18114A80, file "scripts\pas171_external_pilot_readiness_check.py", line 646>)
               MAKE_FUNCTION
               LOAD_CONST              49 (<code object check_no_inbox_scan_tokens at 0x0000018C17CD0F70, file "scripts\pas171_external_pilot_readiness_check.py", line 646>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              55 (check_no_inbox_scan_tokens)

 674           LOAD_CONST              50 (<code object __annotate__ at 0x0000018C18114C60, file "scripts\pas171_external_pilot_readiness_check.py", line 674>)
               MAKE_FUNCTION
               LOAD_CONST              51 (<code object check_doc_required_clauses at 0x0000018C17D8BC70, file "scripts\pas171_external_pilot_readiness_check.py", line 674>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              56 (check_doc_required_clauses)

 714           LOAD_CONST              52 (<code object __annotate__ at 0x0000018C18114D50, file "scripts\pas171_external_pilot_readiness_check.py", line 714>)
               MAKE_FUNCTION
               LOAD_CONST              53 (<code object check_operator_checklist_clauses at 0x0000018C17D8AF50, file "scripts\pas171_external_pilot_readiness_check.py", line 714>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              57 (check_operator_checklist_clauses)

 748           LOAD_CONST              54 (<code object __annotate__ at 0x0000018C18114E40, file "scripts\pas171_external_pilot_readiness_check.py", line 748>)
               MAKE_FUNCTION
               LOAD_CONST              55 (<code object check_self_no_env_or_db at 0x0000018C17D89750, file "scripts\pas171_external_pilot_readiness_check.py", line 748>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              58 (check_self_no_env_or_db)

 782           LOAD_CONST              56 (<code object __annotate__ at 0x0000018C18114F30, file "scripts\pas171_external_pilot_readiness_check.py", line 782>)
               MAKE_FUNCTION
               LOAD_CONST              57 (<code object _aggregate at 0x0000018C17EC44A0, file "scripts\pas171_external_pilot_readiness_check.py", line 782>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              59 (_aggregate)

 798           LOAD_CONST              58 (<code object __annotate__ at 0x0000018C18115020, file "scripts\pas171_external_pilot_readiness_check.py", line 798>)
               MAKE_FUNCTION
               LOAD_CONST              59 (<code object _operator_actions at 0x0000018C18048730, file "scripts\pas171_external_pilot_readiness_check.py", line 798>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              60 (_operator_actions)

 808           LOAD_CONST              60 (<code object __annotate__ at 0x0000018C18115110, file "scripts\pas171_external_pilot_readiness_check.py", line 808>)
               MAKE_FUNCTION
               LOAD_CONST              61 (<code object evaluate at 0x0000018C17F62BD0, file "scripts\pas171_external_pilot_readiness_check.py", line 808>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              61 (evaluate)

 843           LOAD_CONST              62 ('pas171_external_pilot_readiness_report.json')
               STORE_NAME              62 (REPORT_FILENAME)

 846           LOAD_CONST              63 (<code object __annotate__ at 0x0000018C181152F0, file "scripts\pas171_external_pilot_readiness_check.py", line 846>)
               MAKE_FUNCTION
               LOAD_CONST              64 (<code object _build_parser at 0x0000018C1801D1A0, file "scripts\pas171_external_pilot_readiness_check.py", line 846>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              63 (_build_parser)

 880           LOAD_CONST              65 (<code object __annotate__ at 0x0000018C181153E0, file "scripts\pas171_external_pilot_readiness_check.py", line 880>)
               MAKE_FUNCTION
               LOAD_CONST              66 (<code object _print_summary at 0x0000018C17D8D460, file "scripts\pas171_external_pilot_readiness_check.py", line 880>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              64 (_print_summary)

 898           LOAD_CONST              67 (<code object __annotate__ at 0x0000018C18024E30, file "scripts\pas171_external_pilot_readiness_check.py", line 898>)
               MAKE_FUNCTION
               LOAD_CONST              68 (<code object _write_report at 0x0000018C180FC5D0, file "scripts\pas171_external_pilot_readiness_check.py", line 898>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              65 (_write_report)

 912           LOAD_CONST              82 ((None,))
               LOAD_CONST              69 (<code object __annotate__ at 0x0000018C181154D0, file "scripts\pas171_external_pilot_readiness_check.py", line 912>)
               MAKE_FUNCTION
               LOAD_CONST              70 (<code object main at 0x0000018C17D87D80, file "scripts\pas171_external_pilot_readiness_check.py", line 912>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              66 (main)

 940           LOAD_NAME               67 (__name__)
               LOAD_CONST              71 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 941           LOAD_NAME                6 (sys)
               LOAD_ATTR              136 (exit)
               PUSH_NULL
               LOAD_NAME               66 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 940   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  68           LOAD_NAME               18 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  69   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          349 (to L1)

  68   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026230, file "scripts\pas171_external_pilot_readiness_check.py", line 235>:
235           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('check_id')

236           LOAD_CONST               2 ('str')

235           LOAD_CONST               3 ('status')

236           LOAD_CONST               2 ('str')

235           LOAD_CONST               4 ('label')

236           LOAD_CONST               2 ('str')

235           LOAD_CONST               5 ('severity')

237           LOAD_CONST               2 ('str')

235           LOAD_CONST               6 ('detail')

237           LOAD_CONST               2 ('str')

235           LOAD_CONST               7 ('return')

238           LOAD_CONST               8 ('dict')

235           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _check at 0x0000018C17FA3B40, file "scripts\pas171_external_pilot_readiness_check.py", line 235>:
235           RESUME                   0

240           LOAD_CONST               0 ('id')
              LOAD_FAST_BORROW         0 (check_id)

241           LOAD_CONST               1 ('status')
              LOAD_FAST_BORROW         1 (status)

242           LOAD_CONST               2 ('label')
              LOAD_FAST_BORROW         2 (label)

243           LOAD_CONST               3 ('severity')
              LOAD_FAST_BORROW         3 (severity)

244           LOAD_CONST               4 ('detail')
              LOAD_FAST_BORROW         4 (detail)

239           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "scripts\pas171_external_pilot_readiness_check.py", line 248>:
248           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038B70, file "scripts\pas171_external_pilot_readiness_check.py", line 248>:
248           RESUME                   0

249           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "scripts\pas171_external_pilot_readiness_check.py", line 252>:
252           RESUME                   0
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

Disassembly of <code object _read_text at 0x0000018C18053510, file "scripts\pas171_external_pilot_readiness_check.py", line 252>:
 252           RESUME                   0

 253           NOP

 254   L1:     LOAD_FAST_BORROW         0 (path)
               LOAD_ATTR                1 (read_text + NULL|self)
               LOAD_CONST               0 ('utf-8')
               LOAD_CONST               1 ('replace')
               LOAD_CONST               2 (('encoding', 'errors'))
               CALL_KW                  2
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 255           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 256   L4:     POP_EXCEPT
               LOAD_CONST               3 (None)
               RETURN_VALUE

 255   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "scripts\pas171_external_pilot_readiness_check.py", line 259>:
259           RESUME                   0
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

Disassembly of <code object _strip_python_comments_and_strings at 0x0000018C18395BA0, file "scripts\pas171_external_pilot_readiness_check.py", line 259>:
259            RESUME                   0

260            BUILD_LIST               0
               STORE_FAST               1 (out)

261            LOAD_SMALL_INT           0
               LOAD_GLOBAL              1 (len + NULL)
               LOAD_FAST_BORROW         0 (src)
               CALL                     1
               STORE_FAST_STORE_FAST   50 (n, i)

262    L1:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (i, n)
               COMPARE_OP              18 (bool(<))
               EXTENDED_ARG             1
               POP_JUMP_IF_FALSE      282 (to L13)
               NOT_TAKEN

263            LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               BINARY_OP               26 ([])
               STORE_FAST               4 (ch)

264            LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               1 ('#')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       38 (to L3)
               NOT_TAKEN

265            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_CONST               2 ('\n')
               LOAD_FAST_BORROW         2 (i)
               CALL                     2
               STORE_FAST               5 (j)

266            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L2)
               NOT_TAKEN

267            JUMP_FORWARD           240 (to L13)

268    L2:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

269            JUMP_BACKWARD           59 (to L1)

270    L3:     LOAD_FAST_BORROW         0 (src)
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

271    L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               BINARY_SLICE
               STORE_FAST               6 (quote)

272            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 98 (quote, i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               CALL                     2
               STORE_FAST               7 (end)

273            LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L5)
               NOT_TAKEN

274            JUMP_FORWARD           138 (to L13)

275    L5:     LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

276            JUMP_BACKWARD          161 (to L1)

277    L6:     LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               7 (('"', "'"))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       92 (to L12)
               NOT_TAKEN

278            LOAD_FAST                4 (ch)
               STORE_FAST               6 (quote)

279            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               5 (j)

280    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (j, n)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       63 (to L11)
               NOT_TAKEN

281            LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
               BINARY_OP               26 ([])
               LOAD_CONST               5 ('\\')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       12 (to L8)
               NOT_TAKEN

282            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           2
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)

283            JUMP_BACKWARD           30 (to L7)

284    L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
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

285    L9:     JUMP_FORWARD            11 (to L11)

286   L10:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)
               JUMP_BACKWARD           68 (to L7)

287   L11:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

288            EXTENDED_ARG             1
               JUMP_BACKWARD          259 (to L1)

289   L12:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (ch)
               CALL                     1
               POP_TOP

290            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               2 (i)
               EXTENDED_ARG             1
               JUMP_BACKWARD          288 (to L1)

291   L13:     LOAD_CONST               6 ('')
               LOAD_ATTR                9 (join + NULL|self)
               LOAD_FAST_BORROW         1 (out)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "scripts\pas171_external_pilot_readiness_check.py", line 298>:
298           RESUME                   0
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

Disassembly of <code object check_files_present at 0x0000018C18061470, file "scripts\pas171_external_pilot_readiness_check.py", line 298>:
298           RESUME                   0

299           BUILD_LIST               0
              STORE_FAST               1 (out)

300           LOAD_GLOBAL              0 (REQUIRED_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

301           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

302           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

303           LOAD_CONST               0 ('file:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

304           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

305   L3:     LOAD_CONST               3 ('Required PAS171 file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

306           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

307           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing')

302   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

300   L6:     END_FOR
              POP_ITER

309           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "scripts\pas171_external_pilot_readiness_check.py", line 312>:
312           RESUME                   0
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

Disassembly of <code object check_prior_phases_intact at 0x0000018C180606F0, file "scripts\pas171_external_pilot_readiness_check.py", line 312>:
312           RESUME                   0

313           BUILD_LIST               0
              STORE_FAST               1 (out)

314           LOAD_GLOBAL              0 (PRIOR_PHASE_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

315           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

316           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

317           LOAD_CONST               0 ('prior_phase:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

318           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

319   L3:     LOAD_CONST               3 ('Prior-phase readiness script intact: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

320           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

321           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing — PAS171 must not delete')

316   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

314   L6:     END_FOR
              POP_ITER

323           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "scripts\pas171_external_pilot_readiness_check.py", line 326>:
326           RESUME                   0
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

Disassembly of <code object check_memory_review_intact at 0x0000018C18061110, file "scripts\pas171_external_pilot_readiness_check.py", line 326>:
326           RESUME                   0

327           BUILD_LIST               0
              STORE_FAST               1 (out)

328           LOAD_GLOBAL              0 (MEMORY_REVIEW_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

329           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

330           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

331           LOAD_CONST               0 ('memory_review:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

332           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

333   L3:     LOAD_CONST               3 ('Memory Review file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

334           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

335           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('Memory Review file deleted — PAS171 must not touch')

330   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

328   L6:     END_FOR
              POP_ITER

337           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114120, file "scripts\pas171_external_pilot_readiness_check.py", line 340>:
340           RESUME                   0
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

Disassembly of <code object check_worker_off_by_default at 0x0000018C1801C410, file "scripts\pas171_external_pilot_readiness_check.py", line 340>:
340           RESUME                   0

341           BUILD_LIST               0
              STORE_FAST               1 (out)

342           LOAD_GLOBAL              1 (Path + NULL)
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

343           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

345           LOAD_CONST               5 ('_ENV_FLAG_ENABLED_LITERAL = "true"')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         6 (to L2)
              NOT_TAKEN
              POP_TOP

346           LOAD_CONST               6 ("_ENV_FLAG_ENABLED_LITERAL = 'true'")
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)

344   L2:     STORE_FAST               4 (literal_ok)

348           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

349           LOAD_CONST               7 ('worker:off_by_default')

350           LOAD_FAST_BORROW         4 (literal_ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               8 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               9 ('FAIL')

351   L4:     LOAD_CONST              10 ('Pending-call worker is OFF by default (strict env literal)')

352           LOAD_GLOBAL              8 (SEVERITY_BLOCK)

353           LOAD_FAST_BORROW         4 (literal_ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST              11 ('missing strict enable-literal constant')

348   L6:     LOAD_CONST              12 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP

355           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114210, file "scripts\pas171_external_pilot_readiness_check.py", line 358>:
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

Disassembly of <code object check_no_startup_worker at 0x0000018C17EA3D00, file "scripts\pas171_external_pilot_readiness_check.py", line 358>:
358           RESUME                   0

359           BUILD_LIST               0
              STORE_FAST               1 (out)

360           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('main.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

361           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               2 ('')
      L1:     STORE_FAST               3 (src)

362           LOAD_GLOBAL              5 (_strip_python_comments_and_strings + NULL)
              LOAD_FAST_BORROW         3 (src)
              CALL                     1
              STORE_FAST               4 (executable)

363           BUILD_LIST               0
              STORE_FAST               5 (bad)

364           LOAD_CONST               3 ('from app.services.ingestion.worker')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L2)
              NOT_TAKEN

365           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               4 ('from app.services.ingestion.worker import …')
              CALL                     1
              POP_TOP

366   L2:     LOAD_CONST               5 ('import app.services.ingestion.worker')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L3)
              NOT_TAKEN

367           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               5 ('import app.services.ingestion.worker')
              CALL                     1
              POP_TOP

368   L3:     LOAD_CONST               6 ('run_worker_loop')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L4)
              NOT_TAKEN

369           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               7 ('run_worker_loop reference')
              CALL                     1
              POP_TOP

370   L4:     LOAD_CONST               8 ('process_pending_call(')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L5)
              NOT_TAKEN

371           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               9 ('process_pending_call call')
              CALL                     1
              POP_TOP

372   L5:     LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

373           LOAD_CONST              10 ('main:no_startup_worker')

374           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L6)
              NOT_TAKEN
              LOAD_CONST              11 ('FAIL')
              JUMP_FORWARD             1 (to L7)
      L6:     LOAD_CONST              12 ('PASS')

375   L7:     LOAD_CONST              13 ('FastAPI lifespan does not auto-start the pending-call worker')

376           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

377           LOAD_FAST_BORROW         5 (bad)
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

372   L9:     LOAD_CONST              16 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP

379           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181143F0, file "scripts\pas171_external_pilot_readiness_check.py", line 382>:
382           RESUME                   0
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

Disassembly of <code object check_dedupe_store_tokens at 0x0000018C17F003E0, file "scripts\pas171_external_pilot_readiness_check.py", line 382>:
382           RESUME                   0

383           BUILD_LIST               0
              STORE_FAST               1 (out)

384           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('services')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('ingestion')
              BINARY_OP               11 (/)

385           LOAD_CONST               3 ('pending_call_dedupe_store.py')

384           BINARY_OP               11 (/)
              STORE_FAST               2 (p)

386           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

387           LOAD_GLOBAL              4 (REQUIRED_DEDUPE_STORE_TOKENS)
              GET_ITER
      L2:     FOR_ITER                78 (to L7)
              STORE_FAST               4 (tok)

388           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

389           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

390           LOAD_CONST               5 ('dedupe_store_token:')
              LOAD_FAST_BORROW         4 (tok)
              LOAD_CONST               6 (slice(None, 48, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

391           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               7 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               8 ('FAIL')

392   L4:     LOAD_CONST               9 ('Durable pending-call dedupe store token: ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

393           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

394           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             4 (to L6)
      L5:     LOAD_CONST              10 ('missing token ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

389   L6:     LOAD_CONST              11 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           80 (to L2)

387   L7:     END_FOR
              POP_ITER

396           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181144E0, file "scripts\pas171_external_pilot_readiness_check.py", line 399>:
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

Disassembly of <code object check_callback_store_tokens at 0x0000018C17F00E30, file "scripts\pas171_external_pilot_readiness_check.py", line 399>:
399           RESUME                   0

400           BUILD_LIST               0
              STORE_FAST               1 (out)

401           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('services')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('callbacks')
              BINARY_OP               11 (/)

402           LOAD_CONST               3 ('callback_schedule_store.py')

401           BINARY_OP               11 (/)
              STORE_FAST               2 (p)

403           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

404           LOAD_GLOBAL              4 (REQUIRED_CALLBACK_STORE_TOKENS)
              GET_ITER
      L2:     FOR_ITER                78 (to L7)
              STORE_FAST               4 (tok)

405           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

406           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

407           LOAD_CONST               5 ('callback_store_token:')
              LOAD_FAST_BORROW         4 (tok)
              LOAD_CONST               6 (slice(None, 48, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

408           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               7 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               8 ('FAIL')

409   L4:     LOAD_CONST               9 ('Durable callback schedule store token: ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

410           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

411           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             4 (to L6)
      L5:     LOAD_CONST              10 ('missing token ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

406   L6:     LOAD_CONST              11 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           80 (to L2)

404   L7:     END_FOR
              POP_ITER

413           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181145D0, file "scripts\pas171_external_pilot_readiness_check.py", line 416>:
416           RESUME                   0
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

Disassembly of <code object check_dedupe_v18_sql at 0x0000018C17EF9A30, file "scripts\pas171_external_pilot_readiness_check.py", line 416>:
416            RESUME                   0

417            BUILD_LIST               0
               STORE_FAST               1 (out)

418            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('scripts')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('migrate_v18_pending_call_dedupe.sql')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

419            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               2 ('')
       L1:     STORE_FAST               3 (src)

420            LOAD_FAST_BORROW         3 (src)
               LOAD_ATTR                5 (lower + NULL|self)
               CALL                     0
               STORE_FAST               4 (lower)

421            LOAD_CONST               3 ('proposal only')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (proposal_ok)

422            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

423            LOAD_CONST               4 ('dedupe_v18_sql:proposal_only')

424            LOAD_FAST_BORROW         5 (proposal_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L2)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L3)
       L2:     LOAD_CONST               6 ('FAIL')

425    L3:     LOAD_CONST               7 ("v18 dedupe SQL carries 'PROPOSAL ONLY' guardrail")

426            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

427            LOAD_FAST_BORROW         5 (proposal_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L5)
       L4:     LOAD_CONST               8 ("missing 'PROPOSAL ONLY' label")

422    L5:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

429            LOAD_CONST              10 ('do not execute')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)
               STORE_FAST               6 (do_not_exec)

430            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

431            LOAD_CONST              11 ('dedupe_v18_sql:do_not_execute')

432            LOAD_FAST_BORROW         6 (do_not_exec)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L6)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L7)
       L6:     LOAD_CONST               6 ('FAIL')

433    L7:     LOAD_CONST              12 ("v18 dedupe SQL carries 'DO NOT EXECUTE' trailer")

434            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

435            LOAD_FAST_BORROW         6 (do_not_exec)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST              13 ('missing trailer')

430    L9:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

440            LOAD_CONST              14 ('pas_pending_call_dedupe_tenant_no_insert')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L10)
               NOT_TAKEN
               POP_TOP

441            LOAD_CONST              15 ('with check (false)')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)

439   L10:     STORE_FAST               7 (tenant_no_write)

443            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

444            LOAD_CONST              16 ('dedupe_v18_sql:tenant_no_write')

445            LOAD_FAST_BORROW         7 (tenant_no_write)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               6 ('FAIL')

446   L12:     LOAD_CONST              17 ('v18 dedupe SQL denies tenant write')

447            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

448            LOAD_FAST_BORROW         7 (tenant_no_write)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L13)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L14)
      L13:     LOAD_CONST              18 ('missing tenant-write denial')

443   L14:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

451            LOAD_CONST              19 ('[0-9a-f]{64}')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               STORE_FAST               8 (shape_ok)

452            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

453            LOAD_CONST              20 ('dedupe_v18_sql:sha256_shape')

454            LOAD_FAST_BORROW         8 (shape_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L15)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L16)
      L15:     LOAD_CONST               6 ('FAIL')

455   L16:     LOAD_CONST              21 ('v18 dedupe SQL pins the dedupe_key shape to sha256 hex')

456            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

457            LOAD_FAST_BORROW         8 (shape_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L17)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L18)
      L17:     LOAD_CONST              22 ('missing sha256 shape CHECK constraint')

452   L18:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

460            LOAD_CONST              23 ('for delete')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)
               STORE_FAST               9 (no_delete)

461            LOAD_FAST                9 (no_delete)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        6 (to L19)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              24 ('no_delete')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)
      L19:     STORE_FAST              10 (delete_only_denial)

462            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

463            LOAD_CONST              25 ('dedupe_v18_sql:no_delete_grant')

464            LOAD_FAST_BORROW        10 (delete_only_denial)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L20)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L21)
      L20:     LOAD_CONST               6 ('FAIL')

465   L21:     LOAD_CONST              26 ('v18 dedupe SQL has no DELETE grant (delete only present as a denial)')

466            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

467            LOAD_FAST_BORROW        10 (delete_only_denial)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L22)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L23)
      L22:     LOAD_CONST              27 ('DELETE appears outside denial policy')

462   L23:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

469            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181146C0, file "scripts\pas171_external_pilot_readiness_check.py", line 472>:
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

Disassembly of <code object check_callback_v19_sql at 0x0000018C17D4D050, file "scripts\pas171_external_pilot_readiness_check.py", line 472>:
472            RESUME                   0

473            BUILD_LIST               0
               STORE_FAST               1 (out)

474            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('scripts')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('migrate_v19_callback_schedule.sql')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

475            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               2 ('')
       L1:     STORE_FAST               3 (src)

476            LOAD_FAST_BORROW         3 (src)
               LOAD_ATTR                5 (lower + NULL|self)
               CALL                     0
               STORE_FAST               4 (lower)

477            LOAD_CONST               3 ('proposal only')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (proposal_ok)

478            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

479            LOAD_CONST               4 ('callback_v19_sql:proposal_only')

480            LOAD_FAST_BORROW         5 (proposal_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L2)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L3)
       L2:     LOAD_CONST               6 ('FAIL')

481    L3:     LOAD_CONST               7 ("v19 callback SQL carries 'PROPOSAL ONLY' guardrail")

482            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

483            LOAD_FAST_BORROW         5 (proposal_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L5)
       L4:     LOAD_CONST               8 ("missing 'PROPOSAL ONLY' label")

478    L5:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

485            LOAD_CONST              10 ('do not execute')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)
               STORE_FAST               6 (do_not_exec)

486            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

487            LOAD_CONST              11 ('callback_v19_sql:do_not_execute')

488            LOAD_FAST_BORROW         6 (do_not_exec)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L6)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L7)
       L6:     LOAD_CONST               6 ('FAIL')

489    L7:     LOAD_CONST              12 ("v19 callback SQL carries 'DO NOT EXECUTE' trailer")

490            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

491            LOAD_FAST_BORROW         6 (do_not_exec)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST              13 ('missing trailer')

486    L9:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

494            LOAD_CONST              14 ('pas_callback_schedule_tenant_no_insert')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L10)
               NOT_TAKEN
               POP_TOP

495            LOAD_CONST              15 ('with check (false)')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)

493   L10:     STORE_FAST               7 (tenant_no_write)

497            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

498            LOAD_CONST              16 ('callback_v19_sql:tenant_no_write')

499            LOAD_FAST_BORROW         7 (tenant_no_write)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               6 ('FAIL')

500   L12:     LOAD_CONST              17 ('v19 callback SQL denies tenant write')

501            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

502            LOAD_FAST_BORROW         7 (tenant_no_write)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L13)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L14)
      L13:     LOAD_CONST              18 ('missing tenant-write denial')

497   L14:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

506            LOAD_CONST              19 ("'pending'")
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       58 (to L15)
               NOT_TAKEN
               POP_TOP

507            LOAD_CONST              20 ("'reminded'")
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)

506            COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       45 (to L15)
               NOT_TAKEN
               POP_TOP

508            LOAD_CONST              21 ("'completed'")
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)

506            COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       32 (to L15)
               NOT_TAKEN
               POP_TOP

509            LOAD_CONST              22 ("'overdue'")
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)

506            COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       19 (to L15)
               NOT_TAKEN
               POP_TOP

510            LOAD_CONST              23 ("'cancelled'")
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)

506            COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        6 (to L15)
               NOT_TAKEN
               POP_TOP

511            LOAD_CONST              24 ("'failed'")
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)

505   L15:     STORE_FAST               8 (status_ok)

513            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

514            LOAD_CONST              25 ('callback_v19_sql:lower_case_status_enum')

515            LOAD_FAST_BORROW         8 (status_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L16)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L17)
      L16:     LOAD_CONST               6 ('FAIL')

516   L17:     LOAD_CONST              26 ('v19 callback SQL carries lower-case closed status enum')

517            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

518            LOAD_FAST_BORROW         8 (status_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L18)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L19)
      L18:     LOAD_CONST              27 ('missing one or more lower-case status literals')

513   L19:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

523            LOAD_CONST              28 ('create unique index')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        6 (to L20)
               NOT_TAKEN
               POP_TOP

524            LOAD_CONST              29 ("where status in ('pending', 'reminded')")
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)

522   L20:     STORE_FAST               9 (partial_unique_ok)

526            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

527            LOAD_CONST              30 ('callback_v19_sql:partial_unique_active')

528            LOAD_FAST_BORROW         9 (partial_unique_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L21)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L22)
      L21:     LOAD_CONST               6 ('FAIL')

529   L22:     LOAD_CONST              31 ('v19 callback SQL has a partial unique index on active rows')

530            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

531            LOAD_FAST_BORROW         9 (partial_unique_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L23)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L24)

532   L23:     LOAD_CONST              32 ("expected CREATE UNIQUE INDEX … WHERE status IN ('pending', 'reminded')")

526   L24:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

536            LOAD_CONST              33 ('for delete')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)
               STORE_FAST              10 (no_delete)

537            LOAD_FAST               10 (no_delete)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        6 (to L25)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              34 ('no_delete')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)
      L25:     STORE_FAST              11 (delete_only_denial)

538            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

539            LOAD_CONST              35 ('callback_v19_sql:no_delete_grant')

540            LOAD_FAST_BORROW        11 (delete_only_denial)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L26)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L27)
      L26:     LOAD_CONST               6 ('FAIL')

541   L27:     LOAD_CONST              36 ('v19 callback SQL has no DELETE grant (delete only present as a denial)')

542            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

543            LOAD_FAST_BORROW        11 (delete_only_denial)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L28)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L29)
      L28:     LOAD_CONST              37 ('DELETE appears outside denial policy')

538   L29:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

545            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181147B0, file "scripts\pas171_external_pilot_readiness_check.py", line 548>:
548           RESUME                   0
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

Disassembly of <code object check_slack_pilot_hardening at 0x0000018C17D88C40, file "scripts\pas171_external_pilot_readiness_check.py", line 548>:
548            RESUME                   0

549            BUILD_LIST               0
               STORE_FAST               1 (out)

550            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('services')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('monitoring')
               BINARY_OP               11 (/)

551            LOAD_CONST               3 ('slack_alert_transport.py')

550            BINARY_OP               11 (/)
               STORE_FAST               2 (p)

552            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')
       L1:     STORE_FAST               3 (src)

553            LOAD_GLOBAL              4 (REQUIRED_SLACK_PILOT_TOKENS)
               GET_ITER
       L2:     FOR_ITER                78 (to L7)
               STORE_FAST               4 (tok)

554            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

555            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

556            LOAD_CONST               5 ('slack_pilot_token:')
               LOAD_FAST_BORROW         4 (tok)
               LOAD_CONST               6 (slice(None, 48, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

557            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               8 ('FAIL')

558    L4:     LOAD_CONST               9 ('Slack pilot transport token: ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

559            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

560            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST              10 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

555    L6:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           80 (to L2)

553    L7:     END_FOR
               POP_ITER

563            LOAD_GLOBAL             13 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               6 (executable)

564            BUILD_LIST               0
               STORE_FAST               7 (bad_interactive)

565            LOAD_GLOBAL             14 (FORBIDDEN_SLACK_INTERACTIVE_TOKENS)
               GET_ITER
       L8:     FOR_ITER                28 (to L10)
               STORE_FAST               4 (tok)

566            LOAD_FAST_BORROW_LOAD_FAST_BORROW 70 (tok, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L9)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L8)

567    L9:     LOAD_FAST_BORROW         7 (bad_interactive)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (tok)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L8)

565   L10:     END_FOR
               POP_ITER

568            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

569            LOAD_CONST              12 ('slack:no_interactive_components')

570            LOAD_FAST_BORROW         7 (bad_interactive)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               8 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               7 ('PASS')

571   L12:     LOAD_CONST              13 ('Slack pilot transport has no interactive components')

572            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

575            LOAD_FAST_BORROW         7 (bad_interactive)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L13)
               NOT_TAKEN

573            LOAD_CONST              14 ('interactive tokens present: ')

574            LOAD_CONST              15 (', ')
               LOAD_ATTR               17 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad_interactive)
               CALL                     1

573            BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L14)

575   L13:     LOAD_CONST               4 ('')

568   L14:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

583            LOAD_CONST              16 ('_PILOT_ALERT_ID_ALLOWED_PREFIXES = (')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               STORE_FAST               8 (declared_ok)

584            LOAD_CONST              17 ('worker.liveness.missing:')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               STORE_FAST               9 (sample_ok)

585            LOAD_FAST                8 (declared_ok)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L15)
               NOT_TAKEN
               POP_TOP
               LOAD_FAST                9 (sample_ok)
      L15:     STORE_FAST              10 (closed_ok)

586            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

587            LOAD_CONST              18 ('slack:pilot_alert_allow_list_closed')

588            LOAD_FAST_BORROW        10 (closed_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L16)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L17)
      L16:     LOAD_CONST               8 ('FAIL')

589   L17:     LOAD_CONST              19 ('Pilot alert id allow-list is a closed literal tuple')

590            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

591            LOAD_FAST_BORROW        10 (closed_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L18)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L19)

592   L18:     LOAD_CONST              20 ('expected literal tuple declaration + the canonical worker.liveness.missing: prefix')

586   L19:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

596            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181148A0, file "scripts\pas171_external_pilot_readiness_check.py", line 599>:
599           RESUME                   0
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

Disassembly of <code object check_event_contract at 0x0000018C17FEE430, file "scripts\pas171_external_pilot_readiness_check.py", line 599>:
599           RESUME                   0

600           BUILD_LIST               0
              STORE_FAST               1 (out)

601           LOAD_GLOBAL              1 (Path + NULL)
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

602           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

603           LOAD_GLOBAL              4 (REQUIRED_EVENT_TYPES)
              GET_ITER
      L2:     FOR_ITER                72 (to L7)
              STORE_FAST               4 (required)

604           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (required, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

605           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

606           LOAD_CONST               5 ('events:')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

607           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               6 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               7 ('FAIL')

608   L4:     LOAD_CONST               8 ('Event contract registers ')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

609           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

610           LOAD_FAST_BORROW         5 (ok)
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

605   L6:     LOAD_CONST              10 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           74 (to L2)

603   L7:     END_FOR
              POP_ITER

612           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114990, file "scripts\pas171_external_pilot_readiness_check.py", line 615>:
615           RESUME                   0
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

Disassembly of <code object check_no_forbidden_imports at 0x0000018C17EA7670, file "scripts\pas171_external_pilot_readiness_check.py", line 615>:
615            RESUME                   0

616            BUILD_LIST               0
               STORE_FAST               1 (out)

617            LOAD_CONST              10 (('app/services/ingestion/pending_call_dedupe_store.py', 'app/services/callbacks/callback_schedule_store.py', 'scripts/pas171_external_pilot_readiness_check.py'))
               STORE_FAST               2 (files)

622            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     EXTENDED_ARG             1
               FOR_ITER               297 (to L15)
               STORE_FAST               3 (relpath)

623            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

624            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

625            JUMP_BACKWARD           46 (to L1)

626    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

627            BUILD_LIST               0
               STORE_FAST               6 (bad)

628            LOAD_FAST_BORROW         5 (src)
               LOAD_ATTR                7 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L4:     FOR_ITER               107 (to L10)
               STORE_FAST               7 (line)

629            LOAD_FAST_BORROW         7 (line)
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               STORE_FAST               8 (stripped)

630            LOAD_FAST_BORROW         8 (stripped)
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

631    L5:     JUMP_BACKWARD           52 (to L4)

632    L6:     LOAD_GLOBAL             12 (FORBIDDEN_IMPORT_LINE_PREFIXES)
               GET_ITER
       L7:     FOR_ITER                45 (to L9)
               STORE_FAST               9 (prefix)

633            LOAD_FAST_BORROW         8 (stripped)
               LOAD_ATTR               11 (startswith + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD           28 (to L7)

634    L8:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           47 (to L7)

632    L9:     END_FOR
               POP_ITER
               JUMP_BACKWARD          109 (to L4)

628   L10:     END_FOR
               POP_ITER

635            LOAD_FAST                1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             17 (_check + NULL)

636            LOAD_CONST               3 ('forbidden_import:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

637            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               4 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               5 ('PASS')

638   L12:     LOAD_CONST               6 ('No forbidden imports: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

639            LOAD_GLOBAL             18 (SEVERITY_BLOCK)

641            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       43 (to L13)
               NOT_TAKEN

640            LOAD_CONST               7 ('forbidden import prefixes: ')
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

641   L13:     LOAD_CONST               1 ('')

635   L14:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          300 (to L1)

622   L15:     END_FOR
               POP_ITER

643            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114A80, file "scripts\pas171_external_pilot_readiness_check.py", line 646>:
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

Disassembly of <code object check_no_inbox_scan_tokens at 0x0000018C17CD0F70, file "scripts\pas171_external_pilot_readiness_check.py", line 646>:
646            RESUME                   0

647            BUILD_LIST               0
               STORE_FAST               1 (out)

648            LOAD_CONST               9 (('app/services/ingestion/pending_call_dedupe_store.py', 'app/services/callbacks/callback_schedule_store.py', 'scripts/pas171_external_pilot_readiness_check.py'))
               STORE_FAST               2 (files)

653            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               200 (to L11)
               STORE_FAST               3 (relpath)

654            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

655            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

656            JUMP_BACKWARD           45 (to L1)

657    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

658            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         5 (src)
               CALL                     1
               STORE_FAST               6 (executable)

659            BUILD_LIST               0
               STORE_FAST               7 (bad)

660            LOAD_GLOBAL              8 (FORBIDDEN_INBOX_TOKENS)
               GET_ITER
       L4:     FOR_ITER                28 (to L6)
               STORE_FAST               8 (token)

661            LOAD_FAST_BORROW_LOAD_FAST_BORROW 134 (token, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L4)

662    L5:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_FAST_BORROW         8 (token)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L4)

660    L6:     END_FOR
               POP_ITER

663            LOAD_FAST                1 (out)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_GLOBAL             13 (_check + NULL)

664            LOAD_CONST               2 ('no_inbox_scan:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

665            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L7)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L8)
       L7:     LOAD_CONST               4 ('PASS')

666    L8:     LOAD_CONST               5 ('No inbox-scanning tokens: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

667            LOAD_GLOBAL             14 (SEVERITY_BLOCK)

669            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L9)
               NOT_TAKEN

668            LOAD_CONST               6 ('inbox-scan tokens present: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               17 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L10)

669    L9:     LOAD_CONST               1 ('')

663   L10:     LOAD_CONST               8 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          202 (to L1)

653   L11:     END_FOR
               POP_ITER

671            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114C60, file "scripts\pas171_external_pilot_readiness_check.py", line 674>:
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

Disassembly of <code object check_doc_required_clauses at 0x0000018C17D8BC70, file "scripts\pas171_external_pilot_readiness_check.py", line 674>:
  --            MAKE_CELL                8 (lower)

 674            RESUME                   0

 675            BUILD_LIST               0
                STORE_FAST               1 (out)

 676            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('docs')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('pas171_external_pilot_hardening.md')
                BINARY_OP               11 (/)
                STORE_FAST               2 (doc)

 677            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (doc)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L1:     STORE_FAST               3 (src)

 678            LOAD_FAST_BORROW         3 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_DEREF              8 (lower)

 679            LOAD_CONST              13 ((('purpose', ('purpose',)), ('durable-dedupe', ('durable pending-call dedupe', 'pending call dedupe store')), ('durable-callback', ('durable callback schedule', 'callback schedule store')), ('slack-hardening', ('pilot outbound', 'pilot alert', 'outbound notification')), ('operator-checklist', ('operator checklist', 'pilot operator checklist')), ('no-auto-enable', ('off by default', 'operator-driven', 'operator driven')), ('no-gmail', ('no gmail',)), ('not-built', ('intentionally not built', 'deliberately not', 'what is intentionally not')), ('brokerage-pilot', ('brokerage pilot', 'external pilot', 'trusted pilot')), ('limitations', ('limitation',)), ('rollback', ('rollback', 'fall back', 'fallback'))))
                STORE_FAST               4 (required_phrases)

 701            LOAD_FAST_BORROW         4 (required_phrases)
                GET_ITER
        L2:     FOR_ITER               146 (to L12)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   86 (name, phrases)

 702            LOAD_GLOBAL              6 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         8 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18025F30, file "scripts\pas171_external_pilot_readiness_check.py", line 702>)
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
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18025F30, file "scripts\pas171_external_pilot_readiness_check.py", line 702>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         6 (phrases)
                GET_ITER
                CALL                     0
                CALL                     1
        L7:     STORE_FAST               7 (present)

 703            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 704            LOAD_CONST               6 ('docs:phrase:')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 705            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               8 ('FAIL')

 706    L9:     LOAD_CONST               9 ('Hardening doc carries clause: ')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 707            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 709            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L10)
                NOT_TAKEN

 708            LOAD_CONST              10 ('expected one of: ')
                LOAD_CONST              11 (' | ')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_FAST_BORROW         6 (phrases)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L11)

 709   L10:     LOAD_CONST               2 ('')

 703   L11:     LOAD_CONST              12 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          148 (to L2)

 701   L12:     END_FOR
                POP_ITER

 711            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18025F30, file "scripts\pas171_external_pilot_readiness_check.py", line 702>:
  --           COPY_FREE_VARS           1

 702           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C18114D50, file "scripts\pas171_external_pilot_readiness_check.py", line 714>:
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

Disassembly of <code object check_operator_checklist_clauses at 0x0000018C17D8AF50, file "scripts\pas171_external_pilot_readiness_check.py", line 714>:
  --            MAKE_CELL                8 (lower)

 714            RESUME                   0

 715            BUILD_LIST               0
                STORE_FAST               1 (out)

 716            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('docs')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('orvn_external_pilot_operator_checklist.md')
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

 719            LOAD_CONST              13 ((('env-vars', ('pas_alert_slack_webhook_url', 'pending_calls_worker_enabled')), ('migration-order', ('migration order', 'promote', 'migrate_v')), ('calcom-probe', ('cal.com', 'calcom', '/slots')), ('rollback-path', ('rollback', 'fallback', 'process-local')), ('worker-off', ('worker', 'off by default', 'operator-driven', 'operator driven')), ('no-gmail', ('no gmail',)), ('dedupe-restart', ('dedupe', 'restart', 'durable')), ('escalation', ('escalation', 'page', 'on-call', 'oncall'))))
                STORE_FAST               4 (required_phrases)

 735            LOAD_FAST_BORROW         4 (required_phrases)
                GET_ITER
        L2:     FOR_ITER               146 (to L12)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   86 (name, phrases)

 736            LOAD_GLOBAL              6 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         8 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18025730, file "scripts\pas171_external_pilot_readiness_check.py", line 736>)
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
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18025730, file "scripts\pas171_external_pilot_readiness_check.py", line 736>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         6 (phrases)
                GET_ITER
                CALL                     0
                CALL                     1
        L7:     STORE_FAST               7 (present)

 737            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 738            LOAD_CONST               6 ('operator_checklist:phrase:')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 739            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               8 ('FAIL')

 740    L9:     LOAD_CONST               9 ('Operator checklist carries clause: ')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 741            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 743            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L10)
                NOT_TAKEN

 742            LOAD_CONST              10 ('expected one of: ')
                LOAD_CONST              11 (' | ')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_FAST_BORROW         6 (phrases)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L11)

 743   L10:     LOAD_CONST               2 ('')

 737   L11:     LOAD_CONST              12 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          148 (to L2)

 735   L12:     END_FOR
                POP_ITER

 745            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18025730, file "scripts\pas171_external_pilot_readiness_check.py", line 736>:
  --           COPY_FREE_VARS           1

 736           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C18114E40, file "scripts\pas171_external_pilot_readiness_check.py", line 748>:
748           RESUME                   0
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

Disassembly of <code object check_self_no_env_or_db at 0x0000018C17D89750, file "scripts\pas171_external_pilot_readiness_check.py", line 748>:
748            RESUME                   0

749            BUILD_LIST               0
               STORE_FAST               1 (out)

750            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_GLOBAL              2 (__file__)
               CALL                     1
               LOAD_ATTR                5 (resolve + NULL|self)
               CALL                     0
               STORE_FAST               2 (self_path)

751            LOAD_GLOBAL              7 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (self_path)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L1:     STORE_FAST               3 (src)

752            LOAD_GLOBAL              9 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               4 (executable)

753            BUILD_LIST               0
               STORE_FAST               5 (bad)

754            LOAD_FAST_BORROW         4 (executable)
               LOAD_ATTR               11 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L2:     FOR_ITER               199 (to L9)
               STORE_FAST               6 (raw_line)

755            LOAD_FAST_BORROW         6 (raw_line)
               LOAD_ATTR               13 (strip + NULL|self)
               CALL                     0
               STORE_FAST               7 (stripped)

756            LOAD_FAST_BORROW         7 (stripped)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN

757            JUMP_BACKWARD           29 (to L2)

758    L3:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              15 (('import dotenv', 'from dotenv'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L4)
               NOT_TAKEN

759            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               1 ('dotenv import')
               CALL                     1
               POP_TOP

760    L4:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              16 (('import supabase', 'from supabase'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L5)
               NOT_TAKEN

761            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               2 ('supabase import')
               CALL                     1
               POP_TOP

762    L5:     LOAD_CONST               3 ('load_dotenv()')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       18 (to L6)
               NOT_TAKEN

763            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               4 ('load_dotenv() call')
               CALL                     1
               POP_TOP

764    L6:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              17 (('os.environ[', 'getenv('))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L7)
               NOT_TAKEN

765            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               5 ('environ read')
               CALL                     1
               POP_TOP

766    L7:     LOAD_CONST               6 ('get_supabase')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD          182 (to L2)

767    L8:     LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               7 ('supabase client call')
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          201 (to L2)

754    L9:     END_FOR
               POP_ITER

768            LOAD_FAST                1 (out)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_GLOBAL             19 (_check + NULL)

769            LOAD_CONST               8 ('self_check:no_env_or_db')

770            LOAD_FAST_BORROW         5 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST               9 ('FAIL')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST              10 ('PASS')

771   L11:     LOAD_CONST              11 ('PAS171 readiness checker never reads .env / touches DB')

772            LOAD_GLOBAL             20 (SEVERITY_BLOCK)

773            LOAD_FAST_BORROW         5 (bad)
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

768   L13:     LOAD_CONST              14 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

775            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114F30, file "scripts\pas171_external_pilot_readiness_check.py", line 782>:
782           RESUME                   0
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

Disassembly of <code object _aggregate at 0x0000018C17EC44A0, file "scripts\pas171_external_pilot_readiness_check.py", line 782>:
 782            RESUME                   0

 784            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 783            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2

 784    L2:     FOR_ITER                49 (to L7)
                STORE_FAST               1 (c)

 785            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 784    L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L2)

 785    L4:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              2 (SEVERITY_BLOCK)
                COMPARE_OP              88 (bool(==))

 784    L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L2)
        L6:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L2)
        L7:     END_FOR
                POP_ITER

 783    L8:     STORE_FAST               2 (blockers)
                STORE_FAST               1 (c)

 788            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 787            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L9:     BUILD_LIST               0
                SWAP                     2

 788   L10:     FOR_ITER                49 (to L15)
                STORE_FAST               1 (c)

 789            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 788   L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L10)

 789   L12:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              4 (SEVERITY_INFO)
                COMPARE_OP              88 (bool(==))

 788   L13:     POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L10)
       L14:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L10)
       L15:     END_FOR
                POP_ITER

 787   L16:     STORE_FAST               3 (info)
                STORE_FAST               1 (c)

 792            LOAD_CONST               3 ('verdict')
                LOAD_FAST_BORROW         2 (blockers)
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L17)
                NOT_TAKEN
                LOAD_GLOBAL              6 (VERDICT_NOT_READY)
                JUMP_FORWARD             5 (to L18)
       L17:     LOAD_GLOBAL              8 (VERDICT_READY)

 793   L18:     LOAD_CONST               4 ('blockers')
                LOAD_FAST_BORROW         2 (blockers)

 794            LOAD_CONST               5 ('info')
                LOAD_FAST_BORROW         3 (info)

 791            BUILD_MAP                3
                RETURN_VALUE

  --   L19:     SWAP                     2
                POP_TOP

 783            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0

  --   L20:     SWAP                     2
                POP_TOP

 787            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L19 [2]
  L4 to L5 -> L19 [2]
  L6 to L8 -> L19 [2]
  L9 to L11 -> L20 [2]
  L12 to L13 -> L20 [2]
  L14 to L16 -> L20 [2]

Disassembly of <code object __annotate__ at 0x0000018C18115020, file "scripts\pas171_external_pilot_readiness_check.py", line 798>:
798           RESUME                   0
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

Disassembly of <code object _operator_actions at 0x0000018C18048730, file "scripts\pas171_external_pilot_readiness_check.py", line 798>:
798           RESUME                   0

799           BUILD_LIST               0
              STORE_FAST               1 (out)

800           LOAD_FAST_BORROW         0 (checks)
              GET_ITER
      L1:     FOR_ITER               109 (to L5)
              STORE_FAST               2 (c)

801           LOAD_FAST_BORROW         2 (c)
              LOAD_CONST               0 ('status')
              BINARY_OP               26 ([])
              LOAD_CONST               1 ('FAIL')
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

802           JUMP_BACKWARD           19 (to L1)

803   L2:     LOAD_FAST_BORROW         2 (c)
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

804           LOAD_FAST                1 (out)
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

800   L5:     END_FOR
              POP_ITER

805           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18115110, file "scripts\pas171_external_pilot_readiness_check.py", line 808>:
808           RESUME                   0
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

Disassembly of <code object evaluate at 0x0000018C17F62BD0, file "scripts\pas171_external_pilot_readiness_check.py", line 808>:
808           RESUME                   0

809           BUILD_LIST               0
              STORE_FAST               1 (checks)

810           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              3 (check_files_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

811           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              5 (check_prior_phases_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

812           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              7 (check_memory_review_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

813           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              9 (check_worker_off_by_default + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

814           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             11 (check_no_startup_worker + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

815           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             13 (check_dedupe_store_tokens + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

816           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             15 (check_callback_store_tokens + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

817           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             17 (check_dedupe_v18_sql + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

818           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             19 (check_callback_v19_sql + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

819           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             21 (check_slack_pilot_hardening + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

820           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             23 (check_event_contract + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

821           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             25 (check_no_forbidden_imports + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

822           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             27 (check_no_inbox_scan_tokens + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

823           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             29 (check_doc_required_clauses + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

824           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             31 (check_operator_checklist_clauses + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

825           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             33 (check_self_no_env_or_db + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

827           LOAD_GLOBAL             35 (_aggregate + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1
              STORE_FAST               2 (agg)

829           LOAD_CONST               0 ('phase')
              LOAD_CONST               1 ('PAS171')

830           LOAD_CONST               2 ('generated_at')
              LOAD_GLOBAL             37 (_now_iso + NULL)
              CALL                     0

831           LOAD_CONST               3 ('verdict')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])

832           LOAD_CONST               4 ('ready')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])
              LOAD_GLOBAL             38 (VERDICT_READY)
              COMPARE_OP              72 (==)

833           LOAD_CONST               5 ('blocker_count')
              LOAD_GLOBAL             41 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               6 ('blockers')
              BINARY_OP               26 ([])
              CALL                     1

834           LOAD_CONST               7 ('info_count')
              LOAD_GLOBAL             41 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               8 ('info')
              BINARY_OP               26 ([])
              CALL                     1

835           LOAD_CONST               9 ('check_count')
              LOAD_GLOBAL             41 (len + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

836           LOAD_CONST              10 ('pass_count')
              LOAD_GLOBAL             43 (sum + NULL)
              LOAD_CONST              11 (<code object <genexpr> at 0x0000018C18053E10, file "scripts\pas171_external_pilot_readiness_check.py", line 836>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

837           LOAD_CONST              12 ('fail_count')
              LOAD_GLOBAL             43 (sum + NULL)
              LOAD_CONST              13 (<code object <genexpr> at 0x0000018C18053990, file "scripts\pas171_external_pilot_readiness_check.py", line 837>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

838           LOAD_CONST              14 ('checks')
              LOAD_FAST_BORROW         1 (checks)

839           LOAD_CONST              15 ('operator_actions')
              LOAD_GLOBAL             45 (_operator_actions + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

828           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18053E10, file "scripts\pas171_external_pilot_readiness_check.py", line 836>:
 836           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C18053990, file "scripts\pas171_external_pilot_readiness_check.py", line 837>:
 837           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C181152F0, file "scripts\pas171_external_pilot_readiness_check.py", line 846>:
846           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C1801D1A0, file "scripts\pas171_external_pilot_readiness_check.py", line 846>:
846           RESUME                   0

847           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

848           LOAD_CONST               0 ('pas171_external_pilot_readiness_check')

850           LOAD_CONST               1 ('PAS171 — Evaluate external pilot hardening (durable pending-call dedupe + durable callback schedule + pilot Slack hardening + operator checklist). Read-only — never reads .env, never touches Supabase, never runs a migration.')

847           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

857           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

858           LOAD_CONST               3 ('--repo-root')
              LOAD_GLOBAL              6 (_REPO_ROOT_DEFAULT)

859           LOAD_CONST               4 ('Repo root (default: parent of this script).')

857           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

861           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

862           LOAD_CONST               6 ('--output')
              LOAD_GLOBAL              8 (REPORT_FILENAME)

863           LOAD_CONST               7 ('Where to write the JSON report (default ./')
              LOAD_GLOBAL              8 (REPORT_FILENAME)
              FORMAT_SIMPLE
              LOAD_CONST               8 (').')
              BUILD_STRING             3

861           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

865           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

866           LOAD_CONST               9 ('--json')
              LOAD_CONST              10 ('store_true')

867           LOAD_CONST              11 ('Emit JSON on stdout in addition to the summary.')

865           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

869           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

870           LOAD_CONST              13 ('--summary-only')
              LOAD_CONST              10 ('store_true')

871           LOAD_CONST              14 ('Skip writing the JSON report file.')

869           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

873           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

874           LOAD_CONST              15 ('--strict')
              LOAD_CONST              10 ('store_true')

875           LOAD_CONST              16 ('Exit 1 unless verdict == READY (default policy is the same).')

873           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

877           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181153E0, file "scripts\pas171_external_pilot_readiness_check.py", line 880>:
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

Disassembly of <code object _print_summary at 0x0000018C17D8D460, file "scripts\pas171_external_pilot_readiness_check.py", line 880>:
880           RESUME                   0

881           LOAD_GLOBAL              1 (print + NULL)

882           LOAD_CONST               0 ('[PAS171] verdict=')
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
              LOAD_CONST              13 ('[PAS171] operator actions:')
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

Disassembly of <code object __annotate__ at 0x0000018C18024E30, file "scripts\pas171_external_pilot_readiness_check.py", line 898>:
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

Disassembly of <code object _write_report at 0x0000018C180FC5D0, file "scripts\pas171_external_pilot_readiness_check.py", line 898>:
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

Disassembly of <code object __annotate__ at 0x0000018C181154D0, file "scripts\pas171_external_pilot_readiness_check.py", line 912>:
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

Disassembly of <code object main at 0x0000018C17D87D80, file "scripts\pas171_external_pilot_readiness_check.py", line 912>:
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

 922            LOAD_CONST               2 ('error: --repo-root not a directory: ')
                LOAD_FAST                4 (repo_root)
                FORMAT_SIMPLE
                BUILD_STRING             2

 923            LOAD_GLOBAL             24 (sys)
                LOAD_ATTR               26 (stderr)

 921            LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

 925            LOAD_SMALL_INT           2
                RETURN_VALUE

 927    L4:     LOAD_GLOBAL             29 (evaluate + NULL)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                STORE_FAST               5 (report)

 929            LOAD_FAST                2 (args)
                LOAD_ATTR               30 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L5)
                NOT_TAKEN

 930            LOAD_GLOBAL             33 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               34 (output)
                LOAD_FAST                5 (report)
                CALL                     2
                POP_TOP

 932    L5:     LOAD_GLOBAL             37 (_print_summary + NULL)
                LOAD_FAST                5 (report)
                CALL                     1
                POP_TOP

 934            LOAD_FAST                2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L6)
                NOT_TAKEN

 935            LOAD_GLOBAL             23 (print + NULL)
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

 937    L6:     LOAD_FAST                5 (report)
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
