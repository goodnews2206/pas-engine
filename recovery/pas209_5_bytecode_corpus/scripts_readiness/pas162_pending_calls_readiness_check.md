# scripts_readiness/pas162_pending_calls_readiness_check

- **pyc:** `scripts\__pycache__\pas162_pending_calls_readiness_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/pas162_pending_calls_readiness_check.py`
- **co_filename (from bytecode):** `scripts\pas162_pending_calls_readiness_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS162 — Durable pending-calls + auto-dial worker readiness gate.

Deterministic, non-mutating evaluator for "is the durable
pending-call layer wired correctly, structurally safe, and
free of background-automation regressions?".

Walks the repo and verifies:
  * the v14 migration proposal exists with the expected
    structure (no raw_payload / transcript / evidence columns;
    closed status enum; RLS enabled);
  * the pending_calls service exposes the PAS162 DB-backed
    helpers (create / list-due / mark-dialing / mark-dialed /
    mark-failed / cancel);
  * the worker module exists and is OFF by default
    (``pending_calls_worker_enabled`` requires the literal
    ``True`` / ``"true"`` form);
  * the operator CLI exists;
  * the lead-ingestion route uses ``create_pending_call`` and
    includes ``pending_call_id`` in its response shape;
  * the FastAPI app does NOT register a startup background
    worker (PAS162 worker is CLI-only);
  * the event-logger payload allow-list excludes phone /
    email / name;
  * no Memory Review file is touched or imported;
  * no external vendor / embedding / vector libraries.

Emits a verdict (READY / NOT_READY) plus a machine-readable
``pas162_pending_calls_readiness_report.json``.

This script never:
  * modifies files,
  * calls Supabase,
  * reads .env / secrets,
  * imports external vendors,
  * imports embedding / vector libraries,
  * touches the off-limits
    ``scripts/combined_supabase_migration.sql``.

Usage:
  python scripts/pas162_pending_calls_readiness_check.py
  python scripts/pas162_pending_calls_readiness_check.py --json
  python scripts/pas162_pending_calls_readiness_check.py --summary-only
  python scripts/pas162_pending_calls_readiness_check.py --strict

Exit codes:
    0  — READY  (verdict == READY)
    1  — NOT_READY
    2  — bad CLI arguments
```

## Imports

`List`, `Optional`, `Path`, `__future__`, `annotations`, `argparse`, `datetime`, `json`, `os`, `pathlib`, `sys`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_aggregate`, `_build_parser`, `_check`, `_now_iso`, `_operator_actions`, `_print_summary`, `_read_text`, `_strip_python_comments_and_strings`, `_strip_sql_comments`, `_write_report`, `check_cli_script`, `check_docs_required_doctrine`, `check_files_present`, `check_memory_review_intact`, `check_migration_proposal`, `check_no_forbidden_imports`, `check_no_startup_worker`, `check_offlimits_present`, `check_pending_calls_service`, `check_route_uses_create_pending_call`, `check_self_no_env_or_vendor`, `check_worker_module`, `evaluate`, `main`

## Env-key candidates

`BLOCK`, `FAIL`, `INFO`, `NOT_READY`, `PAS162`, `PASS`, `READY`

## String constants (redacted where noted)

- '\nPAS162 — Durable pending-calls + auto-dial worker readiness gate.\n\nDeterministic, non-mutating evaluator for "is the durable\npending-call layer wired correctly, structurally safe, and\nfree of background-automation regressions?".\n\nWalks the repo and verifies:\n  * the v14 migration proposal exists with the expected\n    structure (no raw_payload / transcript / evidence columns;\n    closed status enum; RLS enabled);\n  * the pending_calls service exposes the PAS162 DB-backed\n    helpers (create / list-due / mark-dialing / mark-dialed /\n    mark-failed / cancel);\n  * the worker module exists and is OFF by default\n    (``pending_calls_worker_enabled`` requires the literal\n    ``True`` / ``"true"`` form);\n  * the operator CLI exists;\n  * the lead-ingestion route uses ``create_pending_call`` and\n    includes ``pending_call_id`` in its response shape;\n  * the FastAPI app does NOT register a startup background\n    worker (PAS162 worker is CLI-only);\n  * the event-logger payload allow-list excludes phone /\n    email / name;\n  * no Memory Review file is touched or imported;\n  * no external vendor / embedding / vector libraries.\n\nEmits a verdict (READY / NOT_READY) plus a machine-readable\n``pas162_pending_calls_readiness_report.json``.\n\nThis script never:\n  * modifies files,\n  * calls Supabase,\n  * reads .env / secrets,\n  * imports external vendors,\n  * imports embedding / vector libraries,\n  * touches the off-limits\n    ``scripts/combined_supabase_migration.sql``.\n\nUsage:\n  python scripts/pas162_pending_calls_readiness_check.py\n  python scripts/pas162_pending_calls_readiness_check.py --json\n  python scripts/pas162_pending_calls_readiness_check.py --summary-only\n  python scripts/pas162_pending_calls_readiness_check.py --strict\n\nExit codes:\n    0  — READY  (verdict == READY)\n    1  — NOT_READY\n    2  — bad CLI arguments\n'
- 'utf-8'
- 'READY'
- 'NOT_READY'
- 'BLOCK'
- 'INFO'
- 'severity'
- 'detail'
- 'pas162_pending_calls_readiness_report.json'
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
- 'Required PAS162 file present: '
- 'missing'
- 'offlimits:'
- 'Off-limits file present (do not modify): '
- 'missing — restore from git history'
- 'memory_review_file:'
- 'Memory Review file present (PAS162 must not delete): '
- 'PAS162 must not delete Memory Review files'
- 'Drop SQL line comments (``-- …``) so doctrine prose\ncan discuss forbidden columns by name without tripping the\nstructural scan.'
- 'scripts'
- 'migrate_v14_pending_calls.sql'
- 'sql:'
- 'Migration proposal contains required fragment: '
- 'missing fragment: '
- 'sql:no_forbidden_column:'
- 'Migration proposal excludes forbidden column: '
- 'forbidden column '
- ' present in executable SQL'
- 'sql:no_destructive:'
- 'Migration proposal excludes destructive SQL: '
- 'destructive SQL '
- ' present'
- 'app'
- 'services'
- 'ingestion'
- 'pending_calls.py'
- 'pending_calls_fn:'
- 'Service function present: '
- 'missing def: '
- '.eq("pending_call_id"'
- ".eq('pending_call_id'"
- '.eq("brokerage_id"'
- ".eq('brokerage_id'"
- 'pending_calls_fn:update_tenant_pin'
- 'Update helpers pin both pending_call_id AND brokerage_id'
- 'missing .eq pinning in service module'
- 'pending_calls_fn:no_forbidden:'
- 'Service excludes forbidden field '
- 'forbidden field '
- ' in executable'
- 'worker.py'
- 'worker_fn:'
- 'Worker function present: '
- '_ENV_FLAG_ENABLED_LITERAL = "true"'
- "_ENV_FLAG_ENABLED_LITERAL = 'true'"
- 'worker_fn:strict_enable_literal'
- "Worker enable flag is the strict literal lower-case 'true'"
- 'enable literal constant not found'
- 'outbound_dial_adapter_missing'
- 'worker_fn:no_fake_success'
- "Worker emits structural 'outbound_dial_adapter_missing'"
- "missing 'outbound_dial_adapter_missing' token in worker"
- 'run_pending_calls_worker.py'
- 'cli:'
- 'CLI contains required token: '
- 'missing token: '
- 'routes'
- 'lead_ingestion.py'
- 'route:create_pending_call_imported'
- 'create_pending_call'
- 'Route imports create_pending_call'
- 'create_pending_call not referenced in route executable'
- 'route:no_body_brokerage_id_trust'
- 'Route does not read brokerage_id from the body'
- 'forbidden patterns: '
- 'route:response_includes_pending_call_id'
- '"pending_call_id"'
- 'Route response shape includes pending_call_id'
- 'pending_call_id missing from route response builder'
- '_EVENT_PAYLOAD_ALLOWED'
- 'route:event_payload_allow_list'
- 'Route declares _EVENT_PAYLOAD_ALLOWED with safe keys'
- 'allow-list constant or required keys missing'
- 'route:event_payload_excludes:'
- '_EVENT_PAYLOAD_ALLOWED excludes forbidden key '
- ' present in allow-list constant'
- 'The FastAPI app must NOT auto-run the worker. Search\nmain.py for startup-hook + worker call patterns.'
- 'main.py'
- 'main:no_startup_worker'
- 'FastAPI app does not auto-run pending-call worker on startup'
- 'forbidden tokens in main.py executable: '
- 'app/services/ingestion/pending_calls.py'
- 'forbidden_import:'
- 'No forbidden imports: '
- 'forbidden import prefixes: '
- 'docs'
- 'pas162_pending_calls_worker.md'
- 'docs:phrase:'
- 'Doc carries clause: '
- 'expected one of: '
- ' | '
- 'dotenv import'
- 'supabase import'
- 'external-vendor import'
- 'embedding / vector import'
- 'load_dotenv()'
- 'load_dotenv() call'
- 'environ read'
- 'self_check:no_env_or_vendor'
- 'PAS162 readiness checker never reads .env, calls Supabase, or imports vendor / embedding libs'
- 'disqualifying code-line patterns: '
- 'checks'
- 'verdict'
- 'blockers'
- 'info'
- 'List[str]'
- ' — '
- 'see report'
- 'phase'
- 'PAS162'
- 'generated_at'
- 'ready'
- 'blocker_count'
- 'info_count'
- 'check_count'
- 'pass_count'
- 'fail_count'
- 'operator_actions'
- 'argparse.ArgumentParser'
- 'pas162_pending_calls_readiness_check'
- 'PAS162 — Evaluate the durable pending-call + worker subsystem for structural correctness, doctrine compliance, and absence of background automation. Read-only. Does not touch Supabase, .env, or any tenant data.'
- '--repo-root'
- 'Repo root to evaluate (default: parent of this script).'
- '--output'
- 'Where to write the JSON report (default ./'
- '--json'
- 'store_true'
- 'Emit the report JSON on stdout in addition to the file.'
- '--summary-only'
- 'Skip writing the full report file; print verdict only.'
- '--strict'
- 'Exit 1 unless verdict == READY (default policy is the same).'
- 'report'
- 'None'
- '[PAS162] verdict='
- ' blockers='
- ' info='
- ' checks='
- ' pass='
- ' fail='
- '[PAS162] operator actions:'
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

   1           LOAD_CONST               0 ('\nPAS162 — Durable pending-calls + auto-dial worker readiness gate.\n\nDeterministic, non-mutating evaluator for "is the durable\npending-call layer wired correctly, structurally safe, and\nfree of background-automation regressions?".\n\nWalks the repo and verifies:\n  * the v14 migration proposal exists with the expected\n    structure (no raw_payload / transcript / evidence columns;\n    closed status enum; RLS enabled);\n  * the pending_calls service exposes the PAS162 DB-backed\n    helpers (create / list-due / mark-dialing / mark-dialed /\n    mark-failed / cancel);\n  * the worker module exists and is OFF by default\n    (``pending_calls_worker_enabled`` requires the literal\n    ``True`` / ``"true"`` form);\n  * the operator CLI exists;\n  * the lead-ingestion route uses ``create_pending_call`` and\n    includes ``pending_call_id`` in its response shape;\n  * the FastAPI app does NOT register a startup background\n    worker (PAS162 worker is CLI-only);\n  * the event-logger payload allow-list excludes phone /\n    email / name;\n  * no Memory Review file is touched or imported;\n  * no external vendor / embedding / vector libraries.\n\nEmits a verdict (READY / NOT_READY) plus a machine-readable\n``pas162_pending_calls_readiness_report.json``.\n\nThis script never:\n  * modifies files,\n  * calls Supabase,\n  * reads .env / secrets,\n  * imports external vendors,\n  * imports embedding / vector libraries,\n  * touches the off-limits\n    ``scripts/combined_supabase_migration.sql``.\n\nUsage:\n  python scripts/pas162_pending_calls_readiness_check.py\n  python scripts/pas162_pending_calls_readiness_check.py --json\n  python scripts/pas162_pending_calls_readiness_check.py --summary-only\n  python scripts/pas162_pending_calls_readiness_check.py --strict\n\nExit codes:\n    0  — READY  (verdict == READY)\n    1  — NOT_READY\n    2  — bad CLI arguments\n')
               STORE_NAME               0 (__doc__)

  52           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  54           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  55           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (json)
               STORE_NAME               4 (json)

  56           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (os)
               STORE_NAME               5 (os)

  57           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (sys)
               STORE_NAME               6 (sys)

  58           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              7 (datetime)
               IMPORT_FROM              7 (datetime)
               STORE_NAME               7 (datetime)
               IMPORT_FROM              8 (timezone)
               STORE_NAME               8 (timezone)
               POP_TOP

  59           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Path',))
               IMPORT_NAME              9 (pathlib)
               IMPORT_FROM             10 (Path)
               STORE_NAME              10 (Path)
               POP_TOP

  60           LOAD_SMALL_INT           0
               LOAD_CONST               5 (('List', 'Optional'))
               IMPORT_NAME             11 (typing)
               IMPORT_FROM             12 (List)
               STORE_NAME              12 (List)
               IMPORT_FROM             13 (Optional)
               STORE_NAME              13 (Optional)
               POP_TOP

  63           LOAD_NAME                6 (sys)
               LOAD_ATTR               28 (stdout)
               LOAD_NAME                6 (sys)
               LOAD_ATTR               30 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              16 (_stream)

  64           NOP

  65   L2:     LOAD_NAME               16 (_stream)
               LOAD_ATTR               35 (reconfigure + NULL|self)
               LOAD_CONST               6 ('utf-8')
               LOAD_CONST               7 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  63   L4:     END_FOR
               POP_ITER

  70           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               41 (abspath + NULL|self)

  71           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               43 (join + NULL|self)
               LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               45 (dirname + NULL|self)
               LOAD_NAME               23 (__file__)
               CALL                     1
               LOAD_CONST               8 ('..')
               CALL                     2

  70           CALL                     1
               STORE_NAME              24 (_REPO_ROOT_DEFAULT)

  75           LOAD_CONST               9 ('READY')
               STORE_NAME              25 (VERDICT_READY)

  76           LOAD_CONST              10 ('NOT_READY')
               STORE_NAME              26 (VERDICT_NOT_READY)

  78           LOAD_CONST              11 ('BLOCK')
               STORE_NAME              27 (SEVERITY_BLOCK)

  79           LOAD_CONST              12 ('INFO')
               STORE_NAME              28 (SEVERITY_INFO)

  86           LOAD_CONST              66 (('scripts/migrate_v14_pending_calls.sql', 'app/services/ingestion/pending_calls.py', 'app/services/ingestion/worker.py', 'app/routes/lead_ingestion.py', 'scripts/run_pending_calls_worker.py', 'docs/pas162_pending_calls_worker.md', 'tests/mvp/test_pas162_pending_calls_worker.py'))
               STORE_NAME              29 (REQUIRED_FILES)

  96           LOAD_CONST              67 (('scripts/combined_supabase_migration.sql',))
               STORE_NAME              30 (OFFLIMITS_FILES)

 100           LOAD_CONST              68 (('app/services/memory/review.py', 'app/services/memory/review_stats.py', 'app/services/memory/review_export.py', 'app/services/memory/review_actors.py', 'app/services/memory/review_alerts.py', 'app/services/memory/operator_console.py'))
               STORE_NAME              31 (MEMORY_REVIEW_FILES)

 111           LOAD_CONST              69 (('def pending_call_row_from_normalized_lead(', 'def validate_pending_call_row(', 'def create_pending_call(', 'def list_due_pending_calls(', 'def mark_pending_call_dialing(', 'def mark_pending_call_dialed(', 'def mark_pending_call_failed(', 'def cancel_pending_call('))
               STORE_NAME              32 (REQUIRED_PENDING_CALL_FUNCTIONS)

 124           LOAD_CONST              70 (('def pending_calls_worker_enabled(', 'def build_outbound_call_payload(', 'def process_pending_call(', 'def run_pending_calls_once('))
               STORE_NAME              33 (REQUIRED_WORKER_FUNCTIONS)

 133           LOAD_CONST              71 ((('table', 'CREATE TABLE IF NOT EXISTS pas_pending_calls'), ('brokerage', 'brokerage_id'), ('status', "status            text        NOT NULL DEFAULT 'PENDING'"), ('phone', 'lead_phone        text        NOT NULL'), ('status_chk', 'CONSTRAINT pas_pending_calls_status_chk\n        CHECK (status IN ('), ('source_chk', 'CONSTRAINT pas_pending_calls_source_chk\n        CHECK (source IN ('), ('rls', 'ENABLE ROW LEVEL SECURITY'), ('index_due', 'pas_pending_calls_brokerage_status_due_idx'), ('policy_select_tenant', 'FOR SELECT\n    TO authenticated\n    USING (brokerage_id ='), ('policy_no_tenant_update', 'FOR UPDATE\n    TO authenticated\n    USING (false)')))
               STORE_NAME              34 (REQUIRED_SQL_FRAGMENTS)

 154           LOAD_CONST              72 (('raw_payload', 'transcript', 'evidence', 'metadata_blob', 'memory_content', 'raw_text', 'raw_prompt', 'injected_prompt', 'messages', 'utterances'))
               STORE_NAME              35 (FORBIDDEN_SQL_COLUMNS)

 171           LOAD_CONST              73 (('DROP TABLE pas_', 'TRUNCATE', 'DELETE FROM pas_pending_calls'))
               STORE_NAME              36 (DESTRUCTIVE_SQL_KEYWORDS)

 179           LOAD_CONST              74 (('source', 'lead_id', 'has_email', 'has_budget', 'has_timeline', 'call_queued', 'warning_count'))
               STORE_NAME              37 (EVENT_PAYLOAD_ALLOWED)

 186           LOAD_CONST              75 (('phone', 'email', 'name', 'notes', 'transcript', 'raw_payload', 'full_payload', 'address', 'metadata', 'evidence'))
               STORE_NAME              38 (EVENT_PAYLOAD_FORBIDDEN)

 194           LOAD_CONST              76 (('from app.services.memory', 'import app.services.memory', 'import composio', 'from composio', 'import trustclaw', 'from trustclaw', 'import numpy', 'import faiss', 'import pgvector', 'from pgvector', 'from openai import embeddings', 'from openai.embeddings'))
               STORE_NAME              39 (FORBIDDEN_IMPORT_LINE_PREFIXES)

 217           LOAD_CONST              77 (('run_pending_calls_once', 'pending_calls_worker_enabled', 'dry_run_pending_calls', 'from app.services.ingestion.worker', 'import app.services.ingestion.worker'))
               STORE_NAME              40 (FORBIDDEN_STARTUP_WORKER_TOKENS)

 230           LOAD_CONST              13 ('severity')

 232           LOAD_NAME               27 (SEVERITY_BLOCK)

 230           LOAD_CONST              14 ('detail')

 232           LOAD_CONST              15 ('')

 230           BUILD_MAP                2
               LOAD_CONST              16 (<code object __annotate__ at 0x0000018C18026030, file "scripts\pas162_pending_calls_readiness_check.py", line 230>)
               MAKE_FUNCTION
               LOAD_CONST              17 (<code object _check at 0x0000018C17FA34B0, file "scripts\pas162_pending_calls_readiness_check.py", line 230>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              41 (_check)

 243           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA2F10, file "scripts\pas162_pending_calls_readiness_check.py", line 243>)
               MAKE_FUNCTION
               LOAD_CONST              19 (<code object _now_iso at 0x0000018C18038B70, file "scripts\pas162_pending_calls_readiness_check.py", line 243>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              42 (_now_iso)

 247           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA3B40, file "scripts\pas162_pending_calls_readiness_check.py", line 247>)
               MAKE_FUNCTION
               LOAD_CONST              21 (<code object _read_text at 0x0000018C180533F0, file "scripts\pas162_pending_calls_readiness_check.py", line 247>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              43 (_read_text)

 254           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA2970, file "scripts\pas162_pending_calls_readiness_check.py", line 254>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object _strip_python_comments_and_strings at 0x0000018C17E95410, file "scripts\pas162_pending_calls_readiness_check.py", line 254>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              44 (_strip_python_comments_and_strings)

 293           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA33C0, file "scripts\pas162_pending_calls_readiness_check.py", line 293>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object check_files_present at 0x0000018C180608A0, file "scripts\pas162_pending_calls_readiness_check.py", line 293>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              45 (check_files_present)

 307           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA35A0, file "scripts\pas162_pending_calls_readiness_check.py", line 307>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object check_offlimits_present at 0x0000018C18060A50, file "scripts\pas162_pending_calls_readiness_check.py", line 307>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              46 (check_offlimits_present)

 321           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA3D20, file "scripts\pas162_pending_calls_readiness_check.py", line 321>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object check_memory_review_intact at 0x0000018C18060C00, file "scripts\pas162_pending_calls_readiness_check.py", line 321>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              47 (check_memory_review_intact)

 335           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA1D40, file "scripts\pas162_pending_calls_readiness_check.py", line 335>)
               MAKE_FUNCTION
               LOAD_CONST              31 (<code object _strip_sql_comments at 0x0000018C1800B230, file "scripts\pas162_pending_calls_readiness_check.py", line 335>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              48 (_strip_sql_comments)

 346           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA2880, file "scripts\pas162_pending_calls_readiness_check.py", line 346>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object check_migration_proposal at 0x0000018C17D789F0, file "scripts\pas162_pending_calls_readiness_check.py", line 346>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              49 (check_migration_proposal)

 388           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA2100, file "scripts\pas162_pending_calls_readiness_check.py", line 388>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object check_pending_calls_service at 0x0000018C17D8BF50, file "scripts\pas162_pending_calls_readiness_check.py", line 388>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              50 (check_pending_calls_service)

 438           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C17FA32D0, file "scripts\pas162_pending_calls_readiness_check.py", line 438>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object check_worker_module at 0x0000018C17E93990, file "scripts\pas162_pending_calls_readiness_check.py", line 438>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              51 (check_worker_module)

 479           LOAD_CONST              38 (<code object __annotate__ at 0x0000018C17FA3780, file "scripts\pas162_pending_calls_readiness_check.py", line 479>)
               MAKE_FUNCTION
               LOAD_CONST              39 (<code object check_cli_script at 0x0000018C179C3A50, file "scripts\pas162_pending_calls_readiness_check.py", line 479>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              52 (check_cli_script)

 498           LOAD_CONST              40 (<code object __annotate__ at 0x0000018C17FA1E30, file "scripts\pas162_pending_calls_readiness_check.py", line 498>)
               MAKE_FUNCTION
               LOAD_CONST              41 (<code object check_route_uses_create_pending_call at 0x0000018C177AE550, file "scripts\pas162_pending_calls_readiness_check.py", line 498>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              53 (check_route_uses_create_pending_call)

 573           LOAD_CONST              42 (<code object __annotate__ at 0x0000018C17FA2E20, file "scripts\pas162_pending_calls_readiness_check.py", line 573>)
               MAKE_FUNCTION
               LOAD_CONST              43 (<code object check_no_startup_worker at 0x0000018C17D77E00, file "scripts\pas162_pending_calls_readiness_check.py", line 573>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              54 (check_no_startup_worker)

 595           LOAD_CONST              44 (<code object __annotate__ at 0x0000018C17FA21F0, file "scripts\pas162_pending_calls_readiness_check.py", line 595>)
               MAKE_FUNCTION
               LOAD_CONST              45 (<code object check_no_forbidden_imports at 0x0000018C17D8A550, file "scripts\pas162_pending_calls_readiness_check.py", line 595>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              55 (check_no_forbidden_imports)

 627           LOAD_CONST              46 (<code object __annotate__ at 0x0000018C17FA26A0, file "scripts\pas162_pending_calls_readiness_check.py", line 627>)
               MAKE_FUNCTION
               LOAD_CONST              47 (<code object check_docs_required_doctrine at 0x0000018C17F731D0, file "scripts\pas162_pending_calls_readiness_check.py", line 627>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              56 (check_docs_required_doctrine)

 661           LOAD_CONST              48 (<code object __annotate__ at 0x0000018C17FA2790, file "scripts\pas162_pending_calls_readiness_check.py", line 661>)
               MAKE_FUNCTION
               LOAD_CONST              49 (<code object check_self_no_env_or_vendor at 0x0000018C17E93CC0, file "scripts\pas162_pending_calls_readiness_check.py", line 661>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              57 (check_self_no_env_or_vendor)

 709           LOAD_CONST              50 (<code object __annotate__ at 0x0000018C180FC030, file "scripts\pas162_pending_calls_readiness_check.py", line 709>)
               MAKE_FUNCTION
               LOAD_CONST              51 (<code object _aggregate at 0x0000018C17EC4280, file "scripts\pas162_pending_calls_readiness_check.py", line 709>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              58 (_aggregate)

 725           LOAD_CONST              52 (<code object __annotate__ at 0x0000018C180FC6C0, file "scripts\pas162_pending_calls_readiness_check.py", line 725>)
               MAKE_FUNCTION
               LOAD_CONST              53 (<code object _operator_actions at 0x0000018C180483B0, file "scripts\pas162_pending_calls_readiness_check.py", line 725>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              59 (_operator_actions)

 735           LOAD_CONST              54 (<code object __annotate__ at 0x0000018C180FC7B0, file "scripts\pas162_pending_calls_readiness_check.py", line 735>)
               MAKE_FUNCTION
               LOAD_CONST              55 (<code object evaluate at 0x0000018C17E56380, file "scripts\pas162_pending_calls_readiness_check.py", line 735>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              60 (evaluate)

 766           LOAD_CONST              56 ('pas162_pending_calls_readiness_report.json')
               STORE_NAME              61 (REPORT_FILENAME)

 769           LOAD_CONST              57 (<code object __annotate__ at 0x0000018C180FC8A0, file "scripts\pas162_pending_calls_readiness_check.py", line 769>)
               MAKE_FUNCTION
               LOAD_CONST              58 (<code object _build_parser at 0x0000018C1801C9E0, file "scripts\pas162_pending_calls_readiness_check.py", line 769>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              62 (_build_parser)

 803           LOAD_CONST              59 (<code object __annotate__ at 0x0000018C180FC990, file "scripts\pas162_pending_calls_readiness_check.py", line 803>)
               MAKE_FUNCTION
               LOAD_CONST              60 (<code object _print_summary at 0x0000018C17D8E300, file "scripts\pas162_pending_calls_readiness_check.py", line 803>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              63 (_print_summary)

 821           LOAD_CONST              61 (<code object __annotate__ at 0x0000018C18026230, file "scripts\pas162_pending_calls_readiness_check.py", line 821>)
               MAKE_FUNCTION
               LOAD_CONST              62 (<code object _write_report at 0x0000018C18104030, file "scripts\pas162_pending_calls_readiness_check.py", line 821>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              64 (_write_report)

 835           LOAD_CONST              78 ((None,))
               LOAD_CONST              63 (<code object __annotate__ at 0x0000018C180FCA80, file "scripts\pas162_pending_calls_readiness_check.py", line 835>)
               MAKE_FUNCTION
               LOAD_CONST              64 (<code object main at 0x0000018C17F837D0, file "scripts\pas162_pending_calls_readiness_check.py", line 835>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              65 (main)

 863           LOAD_NAME               66 (__name__)
               LOAD_CONST              65 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 864           LOAD_NAME                6 (sys)
               LOAD_ATTR              134 (exit)
               PUSH_NULL
               LOAD_NAME               65 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 863   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  66           LOAD_NAME               18 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  67   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          335 (to L1)

  66   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026030, file "scripts\pas162_pending_calls_readiness_check.py", line 230>:
230           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('check_id')

231           LOAD_CONST               2 ('str')

230           LOAD_CONST               3 ('status')

231           LOAD_CONST               2 ('str')

230           LOAD_CONST               4 ('label')

231           LOAD_CONST               2 ('str')

230           LOAD_CONST               5 ('severity')

232           LOAD_CONST               2 ('str')

230           LOAD_CONST               6 ('detail')

232           LOAD_CONST               2 ('str')

230           LOAD_CONST               7 ('return')

233           LOAD_CONST               8 ('dict')

230           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _check at 0x0000018C17FA34B0, file "scripts\pas162_pending_calls_readiness_check.py", line 230>:
230           RESUME                   0

235           LOAD_CONST               0 ('id')
              LOAD_FAST_BORROW         0 (check_id)

236           LOAD_CONST               1 ('status')
              LOAD_FAST_BORROW         1 (status)

237           LOAD_CONST               2 ('label')
              LOAD_FAST_BORROW         2 (label)

238           LOAD_CONST               3 ('severity')
              LOAD_FAST_BORROW         3 (severity)

239           LOAD_CONST               4 ('detail')
              LOAD_FAST_BORROW         4 (detail)

234           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "scripts\pas162_pending_calls_readiness_check.py", line 243>:
243           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038B70, file "scripts\pas162_pending_calls_readiness_check.py", line 243>:
243           RESUME                   0

244           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "scripts\pas162_pending_calls_readiness_check.py", line 247>:
247           RESUME                   0
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

Disassembly of <code object _read_text at 0x0000018C180533F0, file "scripts\pas162_pending_calls_readiness_check.py", line 247>:
 247           RESUME                   0

 248           NOP

 249   L1:     LOAD_FAST_BORROW         0 (path)
               LOAD_ATTR                1 (read_text + NULL|self)
               LOAD_CONST               0 ('utf-8')
               LOAD_CONST               1 ('replace')
               LOAD_CONST               2 (('encoding', 'errors'))
               CALL_KW                  2
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 250           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 251   L4:     POP_EXCEPT
               LOAD_CONST               3 (None)
               RETURN_VALUE

 250   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "scripts\pas162_pending_calls_readiness_check.py", line 254>:
254           RESUME                   0
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

Disassembly of <code object _strip_python_comments_and_strings at 0x0000018C17E95410, file "scripts\pas162_pending_calls_readiness_check.py", line 254>:
254            RESUME                   0

255            BUILD_LIST               0
               STORE_FAST               1 (out)

256            LOAD_SMALL_INT           0
               LOAD_GLOBAL              1 (len + NULL)
               LOAD_FAST_BORROW         0 (src)
               CALL                     1
               STORE_FAST_STORE_FAST   50 (n, i)

257    L1:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (i, n)
               COMPARE_OP              18 (bool(<))
               EXTENDED_ARG             1
               POP_JUMP_IF_FALSE      282 (to L13)
               NOT_TAKEN

258            LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               BINARY_OP               26 ([])
               STORE_FAST               4 (ch)

259            LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               1 ('#')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       38 (to L3)
               NOT_TAKEN

260            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_CONST               2 ('\n')
               LOAD_FAST_BORROW         2 (i)
               CALL                     2
               STORE_FAST               5 (j)

261            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L2)
               NOT_TAKEN

262            JUMP_FORWARD           240 (to L13)

263    L2:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

264            JUMP_BACKWARD           59 (to L1)

265    L3:     LOAD_FAST_BORROW         0 (src)
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

266    L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               BINARY_SLICE
               STORE_FAST               6 (quote)

267            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 98 (quote, i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               CALL                     2
               STORE_FAST               7 (end)

268            LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L5)
               NOT_TAKEN

269            JUMP_FORWARD           138 (to L13)

270    L5:     LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

271            JUMP_BACKWARD          161 (to L1)

272    L6:     LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               7 (('"', "'"))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       92 (to L12)
               NOT_TAKEN

273            LOAD_FAST                4 (ch)
               STORE_FAST               6 (quote)

274            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               5 (j)

275    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (j, n)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       63 (to L11)
               NOT_TAKEN

276            LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
               BINARY_OP               26 ([])
               LOAD_CONST               5 ('\\')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       12 (to L8)
               NOT_TAKEN

277            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           2
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)

278            JUMP_BACKWARD           30 (to L7)

279    L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
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

280    L9:     JUMP_FORWARD            11 (to L11)

281   L10:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)
               JUMP_BACKWARD           68 (to L7)

282   L11:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

283            EXTENDED_ARG             1
               JUMP_BACKWARD          259 (to L1)

284   L12:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (ch)
               CALL                     1
               POP_TOP

285            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               2 (i)
               EXTENDED_ARG             1
               JUMP_BACKWARD          288 (to L1)

286   L13:     LOAD_CONST               6 ('')
               LOAD_ATTR                9 (join + NULL|self)
               LOAD_FAST_BORROW         1 (out)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "scripts\pas162_pending_calls_readiness_check.py", line 293>:
293           RESUME                   0
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

Disassembly of <code object check_files_present at 0x0000018C180608A0, file "scripts\pas162_pending_calls_readiness_check.py", line 293>:
293           RESUME                   0

294           BUILD_LIST               0
              STORE_FAST               1 (out)

295           LOAD_GLOBAL              0 (REQUIRED_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

296           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

297           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

298           LOAD_CONST               0 ('file:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

299           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

300   L3:     LOAD_CONST               3 ('Required PAS162 file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

301           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

302           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing')

297   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

295   L6:     END_FOR
              POP_ITER

304           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "scripts\pas162_pending_calls_readiness_check.py", line 307>:
307           RESUME                   0
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

Disassembly of <code object check_offlimits_present at 0x0000018C18060A50, file "scripts\pas162_pending_calls_readiness_check.py", line 307>:
307           RESUME                   0

308           BUILD_LIST               0
              STORE_FAST               1 (out)

309           LOAD_GLOBAL              0 (OFFLIMITS_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

310           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

311           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

312           LOAD_CONST               0 ('offlimits:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

313           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

314   L3:     LOAD_CONST               3 ('Off-limits file present (do not modify): ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

315           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

316           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing — restore from git history')

311   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

309   L6:     END_FOR
              POP_ITER

318           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3D20, file "scripts\pas162_pending_calls_readiness_check.py", line 321>:
321           RESUME                   0
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

Disassembly of <code object check_memory_review_intact at 0x0000018C18060C00, file "scripts\pas162_pending_calls_readiness_check.py", line 321>:
321           RESUME                   0

322           BUILD_LIST               0
              STORE_FAST               1 (out)

323           LOAD_GLOBAL              0 (MEMORY_REVIEW_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

324           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

325           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

326           LOAD_CONST               0 ('memory_review_file:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

327           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

328   L3:     LOAD_CONST               3 ('Memory Review file present (PAS162 must not delete): ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

329           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

330           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('PAS162 must not delete Memory Review files')

325   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

323   L6:     END_FOR
              POP_ITER

332           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1D40, file "scripts\pas162_pending_calls_readiness_check.py", line 335>:
335           RESUME                   0
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

Disassembly of <code object _strip_sql_comments at 0x0000018C1800B230, file "scripts\pas162_pending_calls_readiness_check.py", line 335>:
335           RESUME                   0

339           BUILD_LIST               0
              STORE_FAST               1 (out_lines)

340           LOAD_FAST_BORROW         0 (src)
              LOAD_ATTR                1 (splitlines + NULL|self)
              CALL                     0
              GET_ITER
      L1:     FOR_ITER                49 (to L4)
              STORE_FAST               2 (raw_line)

341           LOAD_FAST_BORROW         2 (raw_line)
              LOAD_ATTR                3 (find + NULL|self)
              LOAD_CONST               1 ('--')
              CALL                     1
              STORE_FAST               3 (idx)

342           LOAD_FAST                1 (out_lines)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_FAST_BORROW         3 (idx)
              LOAD_SMALL_INT           0
              COMPARE_OP              18 (bool(<))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_FAST                2 (raw_line)
              JUMP_FORWARD             4 (to L3)
      L2:     LOAD_FAST_BORROW         2 (raw_line)
              LOAD_CONST               2 (None)
              LOAD_FAST_BORROW         3 (idx)
              BINARY_SLICE
      L3:     CALL                     1
              POP_TOP
              JUMP_BACKWARD           51 (to L1)

340   L4:     END_FOR
              POP_ITER

343           LOAD_CONST               3 ('\n')
              LOAD_ATTR                7 (join + NULL|self)
              LOAD_FAST_BORROW         1 (out_lines)
              CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "scripts\pas162_pending_calls_readiness_check.py", line 346>:
346           RESUME                   0
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

Disassembly of <code object check_migration_proposal at 0x0000018C17D789F0, file "scripts\pas162_pending_calls_readiness_check.py", line 346>:
346            RESUME                   0

347            BUILD_LIST               0
               STORE_FAST               1 (out)

348            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('scripts')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('migrate_v14_pending_calls.sql')
               BINARY_OP               11 (/)
               STORE_FAST               2 (sql_path)

349            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (sql_path)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               2 ('')
       L1:     STORE_FAST               3 (src)

352            LOAD_GLOBAL              4 (REQUIRED_SQL_FRAGMENTS)
               GET_ITER
       L2:     FOR_ITER                80 (to L7)
               UNPACK_SEQUENCE          2
               STORE_FAST_STORE_FAST   69 (name, needle)

353            LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (needle, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               6 (ok)

354            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

355            LOAD_CONST               3 ('sql:')
               LOAD_FAST_BORROW         4 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

356            LOAD_FAST_BORROW         6 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               4 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               5 ('FAIL')

357    L4:     LOAD_CONST               6 ('Migration proposal contains required fragment: ')
               LOAD_FAST_BORROW         4 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

358            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

359            LOAD_FAST_BORROW         6 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD            11 (to L6)
       L5:     LOAD_CONST               7 ('missing fragment: ')
               LOAD_FAST_BORROW         5 (needle)
               LOAD_CONST               8 (slice(None, 60, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

354    L6:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           82 (to L2)

352    L7:     END_FOR
               POP_ITER

364            LOAD_GLOBAL             13 (_strip_sql_comments + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               7 (executable_sql)

365            LOAD_GLOBAL             14 (FORBIDDEN_SQL_COLUMNS)
               GET_ITER
       L8:     FOR_ITER                73 (to L13)
               STORE_FAST               8 (col)

366            LOAD_FAST_BORROW_LOAD_FAST_BORROW 135 (col, executable_sql)
               CONTAINS_OP              0 (in)
               STORE_FAST               9 (present)

367            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

368            LOAD_CONST              10 ('sql:no_forbidden_column:')
               LOAD_FAST_BORROW         8 (col)
               FORMAT_SIMPLE
               BUILD_STRING             2

369            LOAD_FAST_BORROW         9 (present)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN
               LOAD_CONST               5 ('FAIL')
               JUMP_FORWARD             1 (to L10)
       L9:     LOAD_CONST               4 ('PASS')

370   L10:     LOAD_CONST              11 ('Migration proposal excludes forbidden column: ')
               LOAD_FAST_BORROW         8 (col)
               FORMAT_SIMPLE
               BUILD_STRING             2

371            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

373            LOAD_FAST_BORROW         9 (present)
               TO_BOOL
               POP_JUMP_IF_FALSE        8 (to L11)
               NOT_TAKEN

372            LOAD_CONST              12 ('forbidden column ')
               LOAD_FAST_BORROW         8 (col)
               CONVERT_VALUE            2 (repr)
               FORMAT_SIMPLE
               LOAD_CONST              13 (' present in executable SQL')
               BUILD_STRING             3
               JUMP_FORWARD             1 (to L12)

373   L11:     LOAD_CONST               2 ('')

367   L12:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           75 (to L8)

365   L13:     END_FOR
               POP_ITER

376            LOAD_GLOBAL             16 (DESTRUCTIVE_SQL_KEYWORDS)
               GET_ITER
      L14:     FOR_ITER                87 (to L19)
               STORE_FAST              10 (kw)

377            LOAD_FAST_BORROW_LOAD_FAST_BORROW 163 (kw, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               9 (present)

378            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

379            LOAD_CONST              14 ('sql:no_destructive:')
               LOAD_FAST_BORROW        10 (kw)
               LOAD_CONST              15 (slice(None, 20, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

380            LOAD_FAST_BORROW         9 (present)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L15)
               NOT_TAKEN
               LOAD_CONST               5 ('FAIL')
               JUMP_FORWARD             1 (to L16)
      L15:     LOAD_CONST               4 ('PASS')

381   L16:     LOAD_CONST              16 ('Migration proposal excludes destructive SQL: ')
               LOAD_FAST_BORROW        10 (kw)
               LOAD_CONST              17 (slice(None, 30, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

382            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

383            LOAD_FAST_BORROW         9 (present)
               TO_BOOL
               POP_JUMP_IF_FALSE        8 (to L17)
               NOT_TAKEN
               LOAD_CONST              18 ('destructive SQL ')
               LOAD_FAST_BORROW        10 (kw)
               CONVERT_VALUE            2 (repr)
               FORMAT_SIMPLE
               LOAD_CONST              19 (' present')
               BUILD_STRING             3
               JUMP_FORWARD             1 (to L18)
      L17:     LOAD_CONST               2 ('')

378   L18:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           89 (to L14)

376   L19:     END_FOR
               POP_ITER

385            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "scripts\pas162_pending_calls_readiness_check.py", line 388>:
388           RESUME                   0
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

Disassembly of <code object check_pending_calls_service at 0x0000018C17D8BF50, file "scripts\pas162_pending_calls_readiness_check.py", line 388>:
388            RESUME                   0

389            BUILD_LIST               0
               STORE_FAST               1 (out)

390            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('services')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('ingestion')
               BINARY_OP               11 (/)
               LOAD_CONST               3 ('pending_calls.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

391            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')
       L1:     STORE_FAST               3 (src)

392            LOAD_GLOBAL              4 (REQUIRED_PENDING_CALL_FUNCTIONS)
               GET_ITER
       L2:     FOR_ITER                92 (to L7)
               STORE_FAST               4 (needle)

393            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (needle, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

394            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

395            LOAD_CONST               5 ('pending_calls_fn:')
               LOAD_FAST_BORROW         4 (needle)
               LOAD_CONST               6 (slice(None, 40, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

396            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               8 ('FAIL')

397    L4:     LOAD_CONST               9 ('Service function present: ')
               LOAD_FAST_BORROW         4 (needle)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0
               FORMAT_SIMPLE
               BUILD_STRING             2

398            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

399            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST              10 ('missing def: ')
               LOAD_FAST_BORROW         4 (needle)
               FORMAT_SIMPLE
               BUILD_STRING             2

394    L6:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           94 (to L2)

392    L7:     END_FOR
               POP_ITER

406            LOAD_CONST              12 ('.eq("pending_call_id"')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L8)
               NOT_TAKEN
               POP_TOP

407            LOAD_CONST              13 (".eq('pending_call_id'")
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

405    L8:     STORE_FAST               6 (eq_pcid_ok)

410            LOAD_CONST              14 ('.eq("brokerage_id"')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L9)
               NOT_TAKEN
               POP_TOP

411            LOAD_CONST              15 (".eq('brokerage_id'")
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

409    L9:     STORE_FAST               7 (eq_bid_ok)

413            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

414            LOAD_CONST              16 ('pending_calls_fn:update_tenant_pin')

415            LOAD_FAST_BORROW         6 (eq_pcid_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE       11 (to L10)
               NOT_TAKEN
               LOAD_FAST_BORROW         7 (eq_bid_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST               8 ('FAIL')

416   L11:     LOAD_CONST              17 ('Update helpers pin both pending_call_id AND brokerage_id')

417            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

418            LOAD_FAST_BORROW         6 (eq_pcid_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE       11 (to L12)
               NOT_TAKEN
               LOAD_FAST_BORROW         7 (eq_bid_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L12)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L13)

419   L12:     LOAD_CONST              18 ('missing .eq pinning in service module')

413   L13:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

423            LOAD_GLOBAL             15 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               8 (executable)

424            LOAD_CONST              23 (('raw_payload', 'full_payload', 'transcript', 'evidence', 'metadata_blob', 'memory_content'))
               GET_ITER
      L14:     FOR_ITER                74 (to L19)
               STORE_FAST               9 (forbidden)

426            LOAD_FAST_BORROW_LOAD_FAST_BORROW 152 (forbidden, executable)
               CONTAINS_OP              0 (in)
               STORE_FAST              10 (present)

427            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

428            LOAD_CONST              19 ('pending_calls_fn:no_forbidden:')
               LOAD_FAST_BORROW         9 (forbidden)
               FORMAT_SIMPLE
               BUILD_STRING             2

429            LOAD_FAST_BORROW        10 (present)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L15)
               NOT_TAKEN
               LOAD_CONST               8 ('FAIL')
               JUMP_FORWARD             1 (to L16)
      L15:     LOAD_CONST               7 ('PASS')

430   L16:     LOAD_CONST              20 ('Service excludes forbidden field ')
               LOAD_FAST_BORROW         9 (forbidden)
               CONVERT_VALUE            2 (repr)
               FORMAT_SIMPLE
               BUILD_STRING             2

431            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

433            LOAD_FAST_BORROW        10 (present)
               TO_BOOL
               POP_JUMP_IF_FALSE        8 (to L17)
               NOT_TAKEN

432            LOAD_CONST              21 ('forbidden field ')
               LOAD_FAST_BORROW         9 (forbidden)
               CONVERT_VALUE            2 (repr)
               FORMAT_SIMPLE
               LOAD_CONST              22 (' in executable')
               BUILD_STRING             3
               JUMP_FORWARD             1 (to L18)

433   L17:     LOAD_CONST               4 ('')

427   L18:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           76 (to L14)

424   L19:     END_FOR
               POP_ITER

435            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA32D0, file "scripts\pas162_pending_calls_readiness_check.py", line 438>:
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

Disassembly of <code object check_worker_module at 0x0000018C17E93990, file "scripts\pas162_pending_calls_readiness_check.py", line 438>:
438            RESUME                   0

439            BUILD_LIST               0
               STORE_FAST               1 (out)

440            LOAD_GLOBAL              1 (Path + NULL)
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

441            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')
       L1:     STORE_FAST               3 (src)

442            LOAD_GLOBAL              4 (REQUIRED_WORKER_FUNCTIONS)
               GET_ITER
       L2:     FOR_ITER                92 (to L7)
               STORE_FAST               4 (needle)

443            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (needle, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

444            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

445            LOAD_CONST               5 ('worker_fn:')
               LOAD_FAST_BORROW         4 (needle)
               LOAD_CONST               6 (slice(None, 40, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

446            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               8 ('FAIL')

447    L4:     LOAD_CONST               9 ('Worker function present: ')
               LOAD_FAST_BORROW         4 (needle)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0
               FORMAT_SIMPLE
               BUILD_STRING             2

448            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

449            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST              10 ('missing def: ')
               LOAD_FAST_BORROW         4 (needle)
               FORMAT_SIMPLE
               BUILD_STRING             2

444    L6:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           94 (to L2)

442    L7:     END_FOR
               POP_ITER

454            LOAD_CONST              12 ('_ENV_FLAG_ENABLED_LITERAL = "true"')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L8)
               NOT_TAKEN
               POP_TOP

455            LOAD_CONST              13 ("_ENV_FLAG_ENABLED_LITERAL = 'true'")
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

453    L8:     STORE_FAST               6 (flag_ok)

457            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

458            LOAD_CONST              14 ('worker_fn:strict_enable_literal')

459            LOAD_FAST_BORROW         6 (flag_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L10)
       L9:     LOAD_CONST               8 ('FAIL')

460   L10:     LOAD_CONST              15 ("Worker enable flag is the strict literal lower-case 'true'")

461            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

462            LOAD_FAST_BORROW         6 (flag_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST              16 ('enable literal constant not found')

457   L12:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

466            LOAD_CONST              17 ('outbound_dial_adapter_missing')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               STORE_FAST               7 (adapter_missing_ok)

467            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

468            LOAD_CONST              18 ('worker_fn:no_fake_success')

469            LOAD_FAST_BORROW         7 (adapter_missing_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L13)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L14)
      L13:     LOAD_CONST               8 ('FAIL')

470   L14:     LOAD_CONST              19 ("Worker emits structural 'outbound_dial_adapter_missing'")

471            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

472            LOAD_FAST_BORROW         7 (adapter_missing_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L15)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L16)

473   L15:     LOAD_CONST              20 ("missing 'outbound_dial_adapter_missing' token in worker")

467   L16:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

476            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "scripts\pas162_pending_calls_readiness_check.py", line 479>:
479           RESUME                   0
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

Disassembly of <code object check_cli_script at 0x0000018C179C3A50, file "scripts\pas162_pending_calls_readiness_check.py", line 479>:
479           RESUME                   0

480           BUILD_LIST               0
              STORE_FAST               1 (out)

481           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('scripts')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('run_pending_calls_worker.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

482           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               2 ('')
      L1:     STORE_FAST               3 (src)

483           LOAD_CONST              10 (('--once', '--dry-run', '--limit', '--json', 'argparse.ArgumentParser(', 'dry_run_pending_calls', 'run_pending_calls_once'))
              GET_ITER
      L2:     FOR_ITER                78 (to L7)
              STORE_FAST               4 (required)

487           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (required, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

488           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

489           LOAD_CONST               3 ('cli:')
              LOAD_FAST_BORROW         4 (required)
              LOAD_CONST               4 (slice(None, 40, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

490           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               5 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               6 ('FAIL')

491   L4:     LOAD_CONST               7 ('CLI contains required token: ')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

492           LOAD_GLOBAL              8 (SEVERITY_BLOCK)

493           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               2 ('')
              JUMP_FORWARD             4 (to L6)
      L5:     LOAD_CONST               8 ('missing token: ')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

488   L6:     LOAD_CONST               9 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           80 (to L2)

483   L7:     END_FOR
              POP_ITER

495           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "scripts\pas162_pending_calls_readiness_check.py", line 498>:
498           RESUME                   0
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

Disassembly of <code object check_route_uses_create_pending_call at 0x0000018C177AE550, file "scripts\pas162_pending_calls_readiness_check.py", line 498>:
  --            MAKE_CELL               13 (src)

 498            RESUME                   0

 499            BUILD_LIST               0
                STORE_FAST               1 (out)

 500            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('app')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('routes')
                BINARY_OP               11 (/)
                LOAD_CONST               2 ('lead_ingestion.py')
                BINARY_OP               11 (/)
                STORE_FAST               2 (p)

 501            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (p)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               3 ('')
        L1:     STORE_DEREF             13 (src)

 502            LOAD_GLOBAL              5 (_strip_python_comments_and_strings + NULL)
                LOAD_DEREF              13 (src)
                CALL                     1
                STORE_FAST               3 (executable)

 504            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 505            LOAD_CONST               4 ('route:create_pending_call_imported')

 506            LOAD_CONST               5 ('create_pending_call')
                LOAD_FAST_BORROW         3 (executable)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L2)
                NOT_TAKEN
                LOAD_CONST               6 ('PASS')
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               7 ('FAIL')

 507    L3:     LOAD_CONST               8 ('Route imports create_pending_call')

 508            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 509            LOAD_CONST               5 ('create_pending_call')
                LOAD_FAST_BORROW         3 (executable)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L4)
                NOT_TAKEN
                LOAD_CONST               3 ('')
                JUMP_FORWARD             1 (to L5)

 510    L4:     LOAD_CONST               9 ('create_pending_call not referenced in route executable')

 504    L5:     LOAD_CONST              10 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 514            LOAD_CONST              32 (('body["brokerage_id"]', "body['brokerage_id']", 'body.get(brokerage_id', 'payload.brokerage_id', 'LeadPayload('))
                STORE_FAST               4 (forbidden_body_brokerage)

 521            LOAD_FAST_BORROW         4 (forbidden_body_brokerage)
                GET_ITER
                LOAD_FAST_AND_CLEAR      5 (t)
                SWAP                     2
        L6:     BUILD_LIST               0
                SWAP                     2
        L7:     FOR_ITER                13 (to L10)
                STORE_FAST_LOAD_FAST    85 (t, t)
                LOAD_FAST_BORROW         3 (executable)
                CONTAINS_OP              0 (in)
        L8:     POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L7)
        L9:     LOAD_FAST_BORROW         5 (t)
                LIST_APPEND              2
                JUMP_BACKWARD           15 (to L7)
       L10:     END_FOR
                POP_ITER
       L11:     STORE_FAST               6 (bad)
                STORE_FAST               5 (t)

 522            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 523            LOAD_CONST              11 ('route:no_body_brokerage_id_trust')

 524            LOAD_FAST_BORROW         6 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L12)
                NOT_TAKEN
                LOAD_CONST               7 ('FAIL')
                JUMP_FORWARD             1 (to L13)
       L12:     LOAD_CONST               6 ('PASS')

 525   L13:     LOAD_CONST              12 ('Route does not read brokerage_id from the body')

 526            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 528            LOAD_FAST_BORROW         6 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L14)
                NOT_TAKEN

 527            LOAD_CONST              13 ('forbidden patterns: ')
                LOAD_CONST              14 (', ')
                LOAD_ATTR               13 (join + NULL|self)
                LOAD_FAST_BORROW         6 (bad)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L15)

 528   L14:     LOAD_CONST               3 ('')

 522   L15:     LOAD_CONST              10 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 531            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 532            LOAD_CONST              15 ('route:response_includes_pending_call_id')

 533            LOAD_CONST              16 ('"pending_call_id"')
                LOAD_DEREF              13 (src)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L16)
                NOT_TAKEN
                LOAD_CONST               6 ('PASS')
                JUMP_FORWARD             1 (to L17)
       L16:     LOAD_CONST               7 ('FAIL')

 534   L17:     LOAD_CONST              17 ('Route response shape includes pending_call_id')

 535            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 536            LOAD_CONST              16 ('"pending_call_id"')
                LOAD_DEREF              13 (src)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L18)
                NOT_TAKEN
                LOAD_CONST               3 ('')
                JUMP_FORWARD             1 (to L19)

 537   L18:     LOAD_CONST              18 ('pending_call_id missing from route response builder')

 531   L19:     LOAD_CONST              10 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 542            LOAD_CONST              19 ('_EVENT_PAYLOAD_ALLOWED')
                LOAD_DEREF              13 (src)
                CONTAINS_OP              0 (in)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       67 (to L24)
                NOT_TAKEN
                POP_TOP

 543            LOAD_GLOBAL             14 (all)
                COPY                     1
                LOAD_COMMON_CONSTANT     3 (<built-in function all>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       35 (to L23)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW        13 (src)
                BUILD_TUPLE              1
                LOAD_CONST              20 (<code object <genexpr> at 0x0000018C18025C30, file "scripts\pas162_pending_calls_readiness_check.py", line 543>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_GLOBAL             16 (EVENT_PAYLOAD_ALLOWED)
                GET_ITER
                CALL                     0
       L20:     FOR_ITER                12 (to L22)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L21)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L20)
       L21:     POP_ITER
                LOAD_CONST              21 (False)
                JUMP_FORWARD            24 (to L24)
       L22:     END_FOR
                POP_ITER
                LOAD_CONST              22 (True)
                JUMP_FORWARD            20 (to L24)
       L23:     PUSH_NULL
                LOAD_FAST_BORROW        13 (src)
                BUILD_TUPLE              1
                LOAD_CONST              20 (<code object <genexpr> at 0x0000018C18025C30, file "scripts\pas162_pending_calls_readiness_check.py", line 543>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_GLOBAL             16 (EVENT_PAYLOAD_ALLOWED)
                GET_ITER
                CALL                     0
                CALL                     1

 541   L24:     STORE_FAST               7 (allow_list_match)

 545            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 546            LOAD_CONST              23 ('route:event_payload_allow_list')

 547            LOAD_FAST_BORROW         7 (allow_list_match)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L25)
                NOT_TAKEN
                LOAD_CONST               6 ('PASS')
                JUMP_FORWARD             1 (to L26)
       L25:     LOAD_CONST               7 ('FAIL')

 548   L26:     LOAD_CONST              24 ('Route declares _EVENT_PAYLOAD_ALLOWED with safe keys')

 549            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 550            LOAD_FAST_BORROW         7 (allow_list_match)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L27)
                NOT_TAKEN
                LOAD_CONST               3 ('')
                JUMP_FORWARD             1 (to L28)

 551   L27:     LOAD_CONST              25 ('allow-list constant or required keys missing')

 545   L28:     LOAD_CONST              10 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 556            LOAD_DEREF              13 (src)
                LOAD_ATTR               19 (find + NULL|self)
                LOAD_CONST              19 ('_EVENT_PAYLOAD_ALLOWED')
                CALL                     1
                STORE_FAST               8 (idx)

 557            LOAD_FAST_BORROW         8 (idx)
                LOAD_SMALL_INT           0
                COMPARE_OP             188 (bool(>=))
                POP_JUMP_IF_FALSE      143 (to L38)
                NOT_TAKEN

 558            LOAD_DEREF              13 (src)
                LOAD_ATTR               19 (find + NULL|self)
                LOAD_CONST              26 (')')
                LOAD_FAST_BORROW         8 (idx)
                CALL                     2
                STORE_FAST               9 (close)

 559            LOAD_FAST_BORROW_LOAD_FAST_BORROW 152 (close, idx)
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE       12 (to L29)
                NOT_TAKEN
                LOAD_DEREF              13 (src)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 137 (idx, close)
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                BINARY_SLICE
                JUMP_FORWARD             1 (to L30)
       L29:     LOAD_CONST               3 ('')
       L30:     STORE_FAST              10 (tup)

 560            LOAD_GLOBAL             20 (EVENT_PAYLOAD_FORBIDDEN)
                GET_ITER
       L31:     FOR_ITER                95 (to L37)
                STORE_FAST              11 (k)

 561            LOAD_CONST              27 ('"')
                LOAD_FAST_BORROW        11 (k)
                FORMAT_SIMPLE
                LOAD_CONST              27 ('"')
                BUILD_STRING             3
                LOAD_FAST_BORROW        10 (tup)
                CONTAINS_OP              0 (in)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        10 (to L32)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              28 ("'")
                LOAD_FAST_BORROW        11 (k)
                FORMAT_SIMPLE
                LOAD_CONST              28 ("'")
                BUILD_STRING             3
                LOAD_FAST_BORROW        10 (tup)
                CONTAINS_OP              0 (in)
       L32:     STORE_FAST              12 (present)

 562            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 563            LOAD_CONST              29 ('route:event_payload_excludes:')
                LOAD_FAST_BORROW        11 (k)
                FORMAT_SIMPLE
                BUILD_STRING             2

 564            LOAD_FAST_BORROW        12 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L33)
                NOT_TAKEN
                LOAD_CONST               7 ('FAIL')
                JUMP_FORWARD             1 (to L34)
       L33:     LOAD_CONST               6 ('PASS')

 565   L34:     LOAD_CONST              30 ('_EVENT_PAYLOAD_ALLOWED excludes forbidden key ')
                LOAD_FAST_BORROW        11 (k)
                CONVERT_VALUE            2 (repr)
                FORMAT_SIMPLE
                BUILD_STRING             2

 566            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 568            LOAD_FAST_BORROW        12 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L35)
                NOT_TAKEN

 567            LOAD_FAST_BORROW        11 (k)
                CONVERT_VALUE            2 (repr)
                FORMAT_SIMPLE
                LOAD_CONST              31 (' present in allow-list constant')
                BUILD_STRING             2
                JUMP_FORWARD             1 (to L36)

 568   L35:     LOAD_CONST               3 ('')

 562   L36:     LOAD_CONST              10 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           97 (to L31)

 560   L37:     END_FOR
                POP_ITER

 570   L38:     LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L39:     SWAP                     2
                POP_TOP

 521            SWAP                     2
                STORE_FAST               5 (t)
                RERAISE                  0
ExceptionTable:
  L6 to L8 -> L39 [2]
  L9 to L11 -> L39 [2]

Disassembly of <code object <genexpr> at 0x0000018C18025C30, file "scripts\pas162_pending_calls_readiness_check.py", line 543>:
  --           COPY_FREE_VARS           1

 543           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                 9 (to L3)
               STORE_FAST_LOAD_FAST    17 (k, k)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "scripts\pas162_pending_calls_readiness_check.py", line 573>:
573           RESUME                   0
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

Disassembly of <code object check_no_startup_worker at 0x0000018C17D77E00, file "scripts\pas162_pending_calls_readiness_check.py", line 573>:
573           RESUME                   0

576           BUILD_LIST               0
              STORE_FAST               1 (out)

577           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               1 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('main.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (main_path)

578           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (main_path)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               3 ('')
      L1:     STORE_FAST               3 (src)

579           LOAD_GLOBAL              5 (_strip_python_comments_and_strings + NULL)
              LOAD_FAST_BORROW         3 (src)
              CALL                     1
              STORE_FAST               4 (executable)

580           BUILD_LIST               0
              STORE_FAST               5 (bad)

581           LOAD_GLOBAL              6 (FORBIDDEN_STARTUP_WORKER_TOKENS)
              GET_ITER
      L2:     FOR_ITER                28 (to L4)
              STORE_FAST               6 (tok)

582           LOAD_FAST_BORROW_LOAD_FAST_BORROW 100 (tok, executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

583   L3:     LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                9 (append + NULL|self)
              LOAD_FAST_BORROW         6 (tok)
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           30 (to L2)

581   L4:     END_FOR
              POP_ITER

584           LOAD_FAST                1 (out)
              LOAD_ATTR                9 (append + NULL|self)
              LOAD_GLOBAL             11 (_check + NULL)

585           LOAD_CONST               4 ('main:no_startup_worker')

586           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               5 ('FAIL')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               6 ('PASS')

587   L6:     LOAD_CONST               7 ('FastAPI app does not auto-run pending-call worker on startup')

588           LOAD_GLOBAL             12 (SEVERITY_BLOCK)

590           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE       25 (to L7)
              NOT_TAKEN

589           LOAD_CONST               8 ('forbidden tokens in main.py executable: ')

590           LOAD_CONST               9 (', ')
              LOAD_ATTR               15 (join + NULL|self)
              LOAD_FAST_BORROW         5 (bad)
              CALL                     1

589           BINARY_OP                0 (+)
              JUMP_FORWARD             1 (to L8)

590   L7:     LOAD_CONST               3 ('')

584   L8:     LOAD_CONST              10 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP

592           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "scripts\pas162_pending_calls_readiness_check.py", line 595>:
595           RESUME                   0
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

Disassembly of <code object check_no_forbidden_imports at 0x0000018C17D8A550, file "scripts\pas162_pending_calls_readiness_check.py", line 595>:
595            RESUME                   0

596            BUILD_LIST               0
               STORE_FAST               1 (out)

597            LOAD_CONST               9 (('app/services/ingestion/pending_calls.py', 'app/services/ingestion/worker.py', 'app/services/ingestion/contracts.py', 'app/services/ingestion/normalizers.py', 'app/services/ingestion/security.py', 'app/routes/lead_ingestion.py', 'scripts/run_pending_calls_worker.py', 'scripts/pas162_pending_calls_readiness_check.py'))
               STORE_FAST               2 (files)

607            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               241 (to L12)
               STORE_FAST               3 (relpath)

608            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

609            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L2:     STORE_FAST               5 (src)

610            BUILD_LIST               0
               STORE_FAST               6 (bad)

611            LOAD_FAST_BORROW         5 (src)
               LOAD_ATTR                5 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L3:     FOR_ITER                74 (to L7)
               STORE_FAST               7 (line)

612            LOAD_FAST_BORROW         7 (line)
               LOAD_ATTR                7 (strip + NULL|self)
               CALL                     0
               STORE_FAST               8 (stripped)

613            LOAD_GLOBAL              8 (FORBIDDEN_IMPORT_LINE_PREFIXES)
               GET_ITER
       L4:     FOR_ITER                45 (to L6)
               STORE_FAST               9 (prefix)

614            LOAD_FAST_BORROW         8 (stripped)
               LOAD_ATTR               11 (startswith + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           28 (to L4)

615    L5:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR               13 (append + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           47 (to L4)

613    L6:     END_FOR
               POP_ITER
               JUMP_BACKWARD           76 (to L3)

611    L7:     END_FOR
               POP_ITER

616            LOAD_FAST                1 (out)
               LOAD_ATTR               13 (append + NULL|self)
               LOAD_GLOBAL             15 (_check + NULL)

617            LOAD_CONST               2 ('forbidden_import:')
               LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR               16 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

618            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST               4 ('PASS')

619    L9:     LOAD_CONST               5 ('No forbidden imports: ')
               LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR               16 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

620            LOAD_GLOBAL             18 (SEVERITY_BLOCK)

622            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L10)
               NOT_TAKEN

621            LOAD_CONST               6 ('forbidden import prefixes: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               21 (join + NULL|self)
               LOAD_FAST_BORROW         6 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L11)

622   L10:     LOAD_CONST               1 ('')

616   L11:     LOAD_CONST               8 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          243 (to L1)

607   L12:     END_FOR
               POP_ITER

624            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA26A0, file "scripts\pas162_pending_calls_readiness_check.py", line 627>:
627           RESUME                   0
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

Disassembly of <code object check_docs_required_doctrine at 0x0000018C17F731D0, file "scripts\pas162_pending_calls_readiness_check.py", line 627>:
  --            MAKE_CELL                8 (lower)

 627            RESUME                   0

 628            BUILD_LIST               0
                STORE_FAST               1 (out)

 629            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('docs')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('pas162_pending_calls_worker.md')
                BINARY_OP               11 (/)
                STORE_FAST               2 (doc)

 630            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (doc)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L1:     STORE_FAST               3 (src)

 631            LOAD_FAST_BORROW         3 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_DEREF              8 (lower)

 632            LOAD_CONST              13 ((('lifecycle', ('lifecycle',)), ('feature-flag', ('pending_calls_worker_enabled', 'feature flag')), ('safety', ('safety', 'fail-closed', 'fail closed')), ('no-raw-payload', ('no raw payload', 'raw payload')), ('cli-only', ('cli-only', 'cli only', 'operator-run cli')), ('unblocks-pas163', ('pas163', 'candidate generation', 'memory candidate')), ('migration-proposal', ('migrate_v14_pending_calls', 'migration proposal'))))
                STORE_FAST               4 (required_phrases)

 648            LOAD_FAST_BORROW         4 (required_phrases)
                GET_ITER
        L2:     FOR_ITER               146 (to L12)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   86 (name, phrases)

 649            LOAD_GLOBAL              6 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         8 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18026630, file "scripts\pas162_pending_calls_readiness_check.py", line 649>)
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
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18026630, file "scripts\pas162_pending_calls_readiness_check.py", line 649>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         6 (phrases)
                GET_ITER
                CALL                     0
                CALL                     1
        L7:     STORE_FAST               7 (present)

 650            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 651            LOAD_CONST               6 ('docs:phrase:')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 652            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               8 ('FAIL')

 653    L9:     LOAD_CONST               9 ('Doc carries clause: ')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 654            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 656            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L10)
                NOT_TAKEN

 655            LOAD_CONST              10 ('expected one of: ')
                LOAD_CONST              11 (' | ')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_FAST_BORROW         6 (phrases)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L11)

 656   L10:     LOAD_CONST               2 ('')

 650   L11:     LOAD_CONST              12 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          148 (to L2)

 648   L12:     END_FOR
                POP_ITER

 658            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18026630, file "scripts\pas162_pending_calls_readiness_check.py", line 649>:
  --           COPY_FREE_VARS           1

 649           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2790, file "scripts\pas162_pending_calls_readiness_check.py", line 661>:
661           RESUME                   0
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

Disassembly of <code object check_self_no_env_or_vendor at 0x0000018C17E93CC0, file "scripts\pas162_pending_calls_readiness_check.py", line 661>:
661            RESUME                   0

662            BUILD_LIST               0
               STORE_FAST               1 (out)

663            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_GLOBAL              2 (__file__)
               CALL                     1
               LOAD_ATTR                5 (resolve + NULL|self)
               CALL                     0
               STORE_FAST               2 (self_path)

664            LOAD_GLOBAL              7 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (self_path)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L1:     STORE_FAST               3 (src)

665            BUILD_LIST               0
               STORE_FAST               4 (bad)

666            LOAD_FAST_BORROW         3 (src)
               LOAD_ATTR                9 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L2:     EXTENDED_ARG             1
               FOR_ITER               311 (to L11)
               STORE_FAST               5 (raw_line)

667            LOAD_FAST_BORROW         5 (raw_line)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0
               STORE_FAST               6 (stripped)

668            LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST               1 ('#')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

669            JUMP_BACKWARD           45 (to L2)

670    L3:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              16 (('import dotenv', 'from dotenv'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L4)
               NOT_TAKEN

671            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               2 ('dotenv import')
               CALL                     1
               POP_TOP

672    L4:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              17 (('import supabase', 'from supabase'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L5)
               NOT_TAKEN

673            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               3 ('supabase import')
               CALL                     1
               POP_TOP

674    L5:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              18 (('import composio', 'from composio', 'import trustclaw', 'from trustclaw', 'import openai', 'from openai', 'import anthropic', 'from anthropic'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L6)
               NOT_TAKEN

680            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               4 ('external-vendor import')
               CALL                     1
               POP_TOP

681    L6:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              19 (('import numpy', 'import faiss', 'import pgvector', 'from pgvector', 'from openai import embeddings', 'from openai.embeddings'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L7)
               NOT_TAKEN

687            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               5 ('embedding / vector import')
               CALL                     1
               POP_TOP

688    L7:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST               6 ('load_dotenv()')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        24 (to L8)
               NOT_TAKEN

689            LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               17 (endswith + NULL|self)
               LOAD_CONST               6 ('load_dotenv()')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L9)
               NOT_TAKEN

690    L8:     LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               7 ('load_dotenv() call')
               CALL                     1
               POP_TOP

691    L9:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              20 (('os.environ[', 'os.getenv(', 'getenv('))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         4 (to L10)
               NOT_TAKEN
               EXTENDED_ARG             1
               JUMP_BACKWARD          294 (to L2)

692   L10:     LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               8 ('environ read')
               CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          314 (to L2)

666   L11:     END_FOR
               POP_ITER

693            LOAD_FAST                1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             19 (_check + NULL)

694            LOAD_CONST               9 ('self_check:no_env_or_vendor')

695            LOAD_FAST_BORROW         4 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L12)
               NOT_TAKEN
               LOAD_CONST              10 ('FAIL')
               JUMP_FORWARD             1 (to L13)
      L12:     LOAD_CONST              11 ('PASS')

696   L13:     LOAD_CONST              12 ('PAS162 readiness checker never reads .env, calls Supabase, or imports vendor / embedding libs')

698            LOAD_GLOBAL             20 (SEVERITY_BLOCK)

700            LOAD_FAST_BORROW         4 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L14)
               NOT_TAKEN

699            LOAD_CONST              13 ('disqualifying code-line patterns: ')
               LOAD_CONST              14 (', ')
               LOAD_ATTR               23 (join + NULL|self)
               LOAD_FAST_BORROW         4 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L15)

700   L14:     LOAD_CONST               0 ('')

693   L15:     LOAD_CONST              15 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

702            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180FC030, file "scripts\pas162_pending_calls_readiness_check.py", line 709>:
709           RESUME                   0
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

Disassembly of <code object _aggregate at 0x0000018C17EC4280, file "scripts\pas162_pending_calls_readiness_check.py", line 709>:
 709            RESUME                   0

 711            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 710            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2

 711    L2:     FOR_ITER                49 (to L7)
                STORE_FAST               1 (c)

 712            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 711    L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L2)

 712    L4:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              2 (SEVERITY_BLOCK)
                COMPARE_OP              88 (bool(==))

 711    L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L2)
        L6:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L2)
        L7:     END_FOR
                POP_ITER

 710    L8:     STORE_FAST               2 (blockers)
                STORE_FAST               1 (c)

 715            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 714            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L9:     BUILD_LIST               0
                SWAP                     2

 715   L10:     FOR_ITER                49 (to L15)
                STORE_FAST               1 (c)

 716            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 715   L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L10)

 716   L12:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              4 (SEVERITY_INFO)
                COMPARE_OP              88 (bool(==))

 715   L13:     POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L10)
       L14:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L10)
       L15:     END_FOR
                POP_ITER

 714   L16:     STORE_FAST               3 (info)
                STORE_FAST               1 (c)

 719            LOAD_CONST               3 ('verdict')
                LOAD_FAST_BORROW         2 (blockers)
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L17)
                NOT_TAKEN
                LOAD_GLOBAL              6 (VERDICT_NOT_READY)
                JUMP_FORWARD             5 (to L18)
       L17:     LOAD_GLOBAL              8 (VERDICT_READY)

 720   L18:     LOAD_CONST               4 ('blockers')
                LOAD_FAST_BORROW         2 (blockers)

 721            LOAD_CONST               5 ('info')
                LOAD_FAST_BORROW         3 (info)

 718            BUILD_MAP                3
                RETURN_VALUE

  --   L19:     SWAP                     2
                POP_TOP

 710            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0

  --   L20:     SWAP                     2
                POP_TOP

 714            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L19 [2]
  L4 to L5 -> L19 [2]
  L6 to L8 -> L19 [2]
  L9 to L11 -> L20 [2]
  L12 to L13 -> L20 [2]
  L14 to L16 -> L20 [2]

Disassembly of <code object __annotate__ at 0x0000018C180FC6C0, file "scripts\pas162_pending_calls_readiness_check.py", line 725>:
725           RESUME                   0
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

Disassembly of <code object _operator_actions at 0x0000018C180483B0, file "scripts\pas162_pending_calls_readiness_check.py", line 725>:
725           RESUME                   0

726           BUILD_LIST               0
              STORE_FAST               1 (out)

727           LOAD_FAST_BORROW         0 (checks)
              GET_ITER
      L1:     FOR_ITER               109 (to L5)
              STORE_FAST               2 (c)

728           LOAD_FAST_BORROW         2 (c)
              LOAD_CONST               0 ('status')
              BINARY_OP               26 ([])
              LOAD_CONST               1 ('FAIL')
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

729           JUMP_BACKWARD           19 (to L1)

730   L2:     LOAD_FAST_BORROW         2 (c)
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

731           LOAD_FAST                1 (out)
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

727   L5:     END_FOR
              POP_ITER

732           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180FC7B0, file "scripts\pas162_pending_calls_readiness_check.py", line 735>:
735           RESUME                   0
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

Disassembly of <code object evaluate at 0x0000018C17E56380, file "scripts\pas162_pending_calls_readiness_check.py", line 735>:
735           RESUME                   0

736           BUILD_LIST               0
              STORE_FAST               1 (checks)

737           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              3 (check_files_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

738           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              5 (check_offlimits_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

739           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              7 (check_memory_review_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

740           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              9 (check_migration_proposal + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

741           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             11 (check_pending_calls_service + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

742           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             13 (check_worker_module + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

743           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             15 (check_cli_script + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

744           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             17 (check_route_uses_create_pending_call + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

745           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             19 (check_no_startup_worker + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

746           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             21 (check_no_forbidden_imports + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

747           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             23 (check_docs_required_doctrine + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

748           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             25 (check_self_no_env_or_vendor + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

750           LOAD_GLOBAL             27 (_aggregate + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1
              STORE_FAST               2 (agg)

752           LOAD_CONST               0 ('phase')
              LOAD_CONST               1 ('PAS162')

753           LOAD_CONST               2 ('generated_at')
              LOAD_GLOBAL             29 (_now_iso + NULL)
              CALL                     0

754           LOAD_CONST               3 ('verdict')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])

755           LOAD_CONST               4 ('ready')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])
              LOAD_GLOBAL             30 (VERDICT_READY)
              COMPARE_OP              72 (==)

756           LOAD_CONST               5 ('blocker_count')
              LOAD_GLOBAL             33 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               6 ('blockers')
              BINARY_OP               26 ([])
              CALL                     1

757           LOAD_CONST               7 ('info_count')
              LOAD_GLOBAL             33 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               8 ('info')
              BINARY_OP               26 ([])
              CALL                     1

758           LOAD_CONST               9 ('check_count')
              LOAD_GLOBAL             33 (len + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

759           LOAD_CONST              10 ('pass_count')
              LOAD_GLOBAL             35 (sum + NULL)
              LOAD_CONST              11 (<code object <genexpr> at 0x0000018C18053E10, file "scripts\pas162_pending_calls_readiness_check.py", line 759>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

760           LOAD_CONST              12 ('fail_count')
              LOAD_GLOBAL             35 (sum + NULL)
              LOAD_CONST              13 (<code object <genexpr> at 0x0000018C18053750, file "scripts\pas162_pending_calls_readiness_check.py", line 760>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

761           LOAD_CONST              14 ('checks')
              LOAD_FAST_BORROW         1 (checks)

762           LOAD_CONST              15 ('operator_actions')
              LOAD_GLOBAL             37 (_operator_actions + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

751           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18053E10, file "scripts\pas162_pending_calls_readiness_check.py", line 759>:
 759           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C18053750, file "scripts\pas162_pending_calls_readiness_check.py", line 760>:
 760           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C180FC8A0, file "scripts\pas162_pending_calls_readiness_check.py", line 769>:
769           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C1801C9E0, file "scripts\pas162_pending_calls_readiness_check.py", line 769>:
769           RESUME                   0

770           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

771           LOAD_CONST               0 ('pas162_pending_calls_readiness_check')

773           LOAD_CONST               1 ('PAS162 — Evaluate the durable pending-call + worker subsystem for structural correctness, doctrine compliance, and absence of background automation. Read-only. Does not touch Supabase, .env, or any tenant data.')

770           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

780           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

781           LOAD_CONST               3 ('--repo-root')
              LOAD_GLOBAL              6 (_REPO_ROOT_DEFAULT)

782           LOAD_CONST               4 ('Repo root to evaluate (default: parent of this script).')

780           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

784           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

785           LOAD_CONST               6 ('--output')
              LOAD_GLOBAL              8 (REPORT_FILENAME)

786           LOAD_CONST               7 ('Where to write the JSON report (default ./')
              LOAD_GLOBAL              8 (REPORT_FILENAME)
              FORMAT_SIMPLE
              LOAD_CONST               8 (').')
              BUILD_STRING             3

784           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

788           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

789           LOAD_CONST               9 ('--json')
              LOAD_CONST              10 ('store_true')

790           LOAD_CONST              11 ('Emit the report JSON on stdout in addition to the file.')

788           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

792           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

793           LOAD_CONST              13 ('--summary-only')
              LOAD_CONST              10 ('store_true')

794           LOAD_CONST              14 ('Skip writing the full report file; print verdict only.')

792           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

796           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

797           LOAD_CONST              15 ('--strict')
              LOAD_CONST              10 ('store_true')

798           LOAD_CONST              16 ('Exit 1 unless verdict == READY (default policy is the same).')

796           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

800           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180FC990, file "scripts\pas162_pending_calls_readiness_check.py", line 803>:
803           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C17D8E300, file "scripts\pas162_pending_calls_readiness_check.py", line 803>:
803           RESUME                   0

804           LOAD_GLOBAL              1 (print + NULL)

805           LOAD_CONST               0 ('[PAS162] verdict=')
              LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               1 ('verdict')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               2 (' blockers=')

806           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               3 ('blocker_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' info=')

807           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               5 ('info_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' checks=')

808           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               7 ('check_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' pass=')

809           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               9 ('pass_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              10 (' fail=')

810           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              11 ('fail_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE

805           BUILD_STRING            12

804           CALL                     1
              POP_TOP

812           LOAD_FAST_BORROW         0 (report)
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

813           LOAD_FAST_BORROW         1 (actions)
              TO_BOOL
              POP_JUMP_IF_FALSE       93 (to L5)
              NOT_TAKEN

814           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              13 ('[PAS162] operator actions:')
              CALL                     1
              POP_TOP

815           LOAD_FAST_BORROW         1 (actions)
              LOAD_CONST              14 (slice(None, 25, None))
              BINARY_OP               26 ([])
              GET_ITER
      L2:     FOR_ITER                17 (to L3)
              STORE_FAST               2 (a)

816           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              15 ('  - ')
              LOAD_FAST_BORROW         2 (a)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L2)

815   L3:     END_FOR
              POP_ITER

817           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         1 (actions)
              CALL                     1
              LOAD_SMALL_INT          25
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       34 (to L4)
              NOT_TAKEN

818           LOAD_GLOBAL              1 (print + NULL)
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

817   L4:     LOAD_CONST              18 (None)
              RETURN_VALUE

813   L5:     LOAD_CONST              18 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026230, file "scripts\pas162_pending_calls_readiness_check.py", line 821>:
821           RESUME                   0
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

Disassembly of <code object _write_report at 0x0000018C18104030, file "scripts\pas162_pending_calls_readiness_check.py", line 821>:
 821           RESUME                   0

 822           NOP

 823   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

 824           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

 825           LOAD_CONST               3 ('utf-8')

 823           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 827           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

 828   L4:     LOAD_GLOBAL             11 (print + NULL)

 829           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

 830           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

 829           BUILD_STRING             4

 831           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

 828           LOAD_CONST               7 (('file',))
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

 827   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C180FCA80, file "scripts\pas162_pending_calls_readiness_check.py", line 835>:
835           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17F837D0, file "scripts\pas162_pending_calls_readiness_check.py", line 835>:
 835            RESUME                   0

 836            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 837            NOP

 838    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 842    L2:     LOAD_GLOBAL             10 (os)
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

 843            LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               21 (isdir + NULL|self)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L4)
                NOT_TAKEN

 844            LOAD_GLOBAL             23 (print + NULL)

 845            LOAD_CONST               2 ('error: --repo-root not a directory: ')
                LOAD_FAST                4 (repo_root)
                FORMAT_SIMPLE
                BUILD_STRING             2

 846            LOAD_GLOBAL             24 (sys)
                LOAD_ATTR               26 (stderr)

 844            LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

 848            LOAD_SMALL_INT           2
                RETURN_VALUE

 850    L4:     LOAD_GLOBAL             29 (evaluate + NULL)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                STORE_FAST               5 (report)

 852            LOAD_FAST                2 (args)
                LOAD_ATTR               30 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L5)
                NOT_TAKEN

 853            LOAD_GLOBAL             33 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               34 (output)
                LOAD_FAST                5 (report)
                CALL                     2
                POP_TOP

 855    L5:     LOAD_GLOBAL             37 (_print_summary + NULL)
                LOAD_FAST                5 (report)
                CALL                     1
                POP_TOP

 857            LOAD_FAST                2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L6)
                NOT_TAKEN

 858            LOAD_GLOBAL             23 (print + NULL)
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

 860    L6:     LOAD_FAST                5 (report)
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

 839            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L17)
                NOT_TAKEN
                STORE_FAST               3 (e)

 840    L9:     LOAD_FAST                3 (e)
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

 839   L17:     RERAISE                  0

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
