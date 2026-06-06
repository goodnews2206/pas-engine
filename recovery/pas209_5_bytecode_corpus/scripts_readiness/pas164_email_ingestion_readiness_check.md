# scripts_readiness/pas164_email_ingestion_readiness_check

- **pyc:** `scripts\__pycache__\pas164_email_ingestion_readiness_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/pas164_email_ingestion_readiness_check.py`
- **co_filename (from bytecode):** `scripts\pas164_email_ingestion_readiness_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS164 — Email lead ingestion readiness gate.

Deterministic, non-mutating evaluator for "is the email lead
ingestion subsystem wired correctly, structurally safe, and
free of Gmail / OAuth / inbox / raw-body regressions?".

Walks the repo and verifies:

  * email_parser.py exists and exports the required helpers;
  * email_ingestion.py service exists and exports the required
    helper;
  * the email-ingestion route module exists and declares both
    /parse and /ingest;
  * the FastAPI router is wired into app/main.py;
  * the docs file exists and carries the doctrine clauses;
  * the test file exists;
  * supported sources are listed in the parser;
  * no Gmail / google / OAuth / inbox / Composio / TrustClaw /
    embedding / vector imports;
  * no raw_email / raw_body / full_email / raw_payload /
    transcript keys appear in the parser/service/route output
    contract;
  * no phone / email / name / subject / body in the route's
    event payload allow-list;
  * Memory Review UI files are intact;
  * prior-phase readiness scripts (PAS160 / PAS161 / PAS162 /
    PAS163) still exist;
  * supports --summary-only and --json;
  * exits 0 ready, 1 blockers, 2 bad args;
  * never reads .env;
  * never touches production data.

Usage:
  python scripts/pas164_email_ingestion_readiness_check.py
  python scripts/pas164_email_ingestion_readiness_check.py --json
  python scripts/pas164_email_ingestion_readiness_check.py --summary-only
  python scripts/pas164_email_ingestion_readiness_check.py --strict

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

`__annotate__`, `_aggregate`, `_build_parser`, `_check`, `_now_iso`, `_operator_actions`, `_print_summary`, `_read_text`, `_strip_python_comments_and_strings`, `_write_report`, `check_docs_required_doctrine`, `check_event_contract`, `check_files_present`, `check_main_wiring`, `check_memory_review_intact`, `check_no_forbidden_imports`, `check_no_inbox_scanning`, `check_parser`, `check_prior_phases_intact`, `check_routes`, `check_self_no_env_or_vendor`, `check_service`, `evaluate`, `main`

## Env-key candidates

`BLOCK`, `FAIL`, `INFO`, `NOT_READY`, `PAS164`, `PASS`, `READY`

## String constants (redacted where noted)

- '\nPAS164 — Email lead ingestion readiness gate.\n\nDeterministic, non-mutating evaluator for "is the email lead\ningestion subsystem wired correctly, structurally safe, and\nfree of Gmail / OAuth / inbox / raw-body regressions?".\n\nWalks the repo and verifies:\n\n  * email_parser.py exists and exports the required helpers;\n  * email_ingestion.py service exists and exports the required\n    helper;\n  * the email-ingestion route module exists and declares both\n    /parse and /ingest;\n  * the FastAPI router is wired into app/main.py;\n  * the docs file exists and carries the doctrine clauses;\n  * the test file exists;\n  * supported sources are listed in the parser;\n  * no Gmail / google / OAuth / inbox / Composio / TrustClaw /\n    embedding / vector imports;\n  * no raw_email / raw_body / full_email / raw_payload /\n    transcript keys appear in the parser/service/route output\n    contract;\n  * no phone / email / name / subject / body in the route\'s\n    event payload allow-list;\n  * Memory Review UI files are intact;\n  * prior-phase readiness scripts (PAS160 / PAS161 / PAS162 /\n    PAS163) still exist;\n  * supports --summary-only and --json;\n  * exits 0 ready, 1 blockers, 2 bad args;\n  * never reads .env;\n  * never touches production data.\n\nUsage:\n  python scripts/pas164_email_ingestion_readiness_check.py\n  python scripts/pas164_email_ingestion_readiness_check.py --json\n  python scripts/pas164_email_ingestion_readiness_check.py --summary-only\n  python scripts/pas164_email_ingestion_readiness_check.py --strict\n\nExit codes:\n    0  — READY  (verdict == READY)\n    1  — NOT_READY\n    2  — bad CLI arguments\n'
- 'utf-8'
- 'READY'
- 'NOT_READY'
- 'BLOCK'
- 'INFO'
- 'severity'
- 'detail'
- 'pas164_email_ingestion_readiness_report.json'
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
- 'Required PAS164 file present: '
- 'missing'
- 'prior_phase:'
- 'Prior-phase readiness script intact: '
- 'missing — PAS164 must not delete'
- 'memory_review_file:'
- 'Memory Review file present (PAS164 must not delete): '
- 'PAS164 must not delete Memory Review files'
- 'app'
- 'services'
- 'ingestion'
- 'email_parser.py'
- 'parser_fn:'
- 'Parser function present: '
- 'missing def: '
- 'parser_source:'
- 'Parser declares supported source: '
- 'source label '
- ' not declared'
- 'parser:no_forbidden_output_key:'
- 'Parser excludes forbidden output key: '
- 'forbidden output key '
- ' present as dict-key'
- 'email_ingestion.py'
- 'service_fn:'
- 'Service function present: '
- 'missing_brokerage_id'
- 'service:requires_brokerage_id'
- 'Service rejects calls without brokerage_id'
- 'missing_brokerage_id token not found'
- 'create_pending_call'
- 'service:hands_off_to_pas162'
- 'Service hands off to PAS162 create_pending_call'
- 'create_pending_call reference missing'
- 'service:no_forbidden_output_key:'
- 'Service excludes forbidden output key: '
- 'routes'
- 'route_decl:'
- 'Route declaration present: '
- 'missing decl: '
- 'require_admin'
- 'route:auth:require_admin'
- 'Route uses require_admin for /parse'
- 'require_admin reference missing'
- 'require_brokerage'
- 'route:auth:require_brokerage'
- 'Route uses require_brokerage for /ingest'
- 'require_brokerage reference missing'
- 'route:no_body_trust:'
- 'Route never reads brokerage_id from body: '
- 'body-trust pattern '
- ' present'
- '_EVENT_PAYLOAD_ALLOWED'
- 'route:event_allowlist_excludes:'
- 'Event payload allow-list excludes forbidden key: '
- 'forbidden allow-list key '
- 'main.py'
- 'main_wiring:'
- 'main.py wiring present: '
- 'missing wiring: '
- 'events'
- 'contract.py'
- 'events:'
- 'Event contract registers '
- 'missing event type '
- 'app/services/ingestion/email_parser.py'
- 'forbidden_import:'
- 'No forbidden imports: '
- 'forbidden import prefixes: '
- 'no_inbox_scan:'
- 'No inbox-scanning tokens: '
- 'inbox-scan tokens present: '
- 'docs'
- 'pas164_email_lead_ingestion.md'
- 'docs:phrase:'
- 'Doc carries clause: '
- 'expected one of: '
- ' | '
- 'dotenv import'
- 'supabase import'
- 'external-vendor / google import'
- 'embedding / vector import'
- 'load_dotenv()'
- 'load_dotenv() call'
- 'environ read'
- 'self_check:no_env_or_vendor'
- 'PAS164 readiness checker never reads .env, calls Supabase, or imports vendor / Google / embedding libs'
- 'disqualifying code-line patterns: '
- 'checks'
- 'verdict'
- 'blockers'
- 'info'
- 'List[str]'
- ' — '
- 'see report'
- 'phase'
- 'PAS164'
- 'generated_at'
- 'ready'
- 'blocker_count'
- 'info_count'
- 'check_count'
- 'pass_count'
- 'fail_count'
- 'operator_actions'
- 'argparse.ArgumentParser'
- 'pas164_email_ingestion_readiness_check'
- 'PAS164 — Evaluate the email-ingestion subsystem for structural correctness, no-Gmail-OAuth doctrine, no inbox scanning, and absence of raw-body / identifying field leakage. Read-only. Does not touch Supabase, .env, or any tenant data.'
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
- '[PAS164] verdict='
- ' blockers='
- ' info='
- ' checks='
- ' pass='
- ' fail='
- '[PAS164] operator actions:'
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

   1           LOAD_CONST               0 ('\nPAS164 — Email lead ingestion readiness gate.\n\nDeterministic, non-mutating evaluator for "is the email lead\ningestion subsystem wired correctly, structurally safe, and\nfree of Gmail / OAuth / inbox / raw-body regressions?".\n\nWalks the repo and verifies:\n\n  * email_parser.py exists and exports the required helpers;\n  * email_ingestion.py service exists and exports the required\n    helper;\n  * the email-ingestion route module exists and declares both\n    /parse and /ingest;\n  * the FastAPI router is wired into app/main.py;\n  * the docs file exists and carries the doctrine clauses;\n  * the test file exists;\n  * supported sources are listed in the parser;\n  * no Gmail / google / OAuth / inbox / Composio / TrustClaw /\n    embedding / vector imports;\n  * no raw_email / raw_body / full_email / raw_payload /\n    transcript keys appear in the parser/service/route output\n    contract;\n  * no phone / email / name / subject / body in the route\'s\n    event payload allow-list;\n  * Memory Review UI files are intact;\n  * prior-phase readiness scripts (PAS160 / PAS161 / PAS162 /\n    PAS163) still exist;\n  * supports --summary-only and --json;\n  * exits 0 ready, 1 blockers, 2 bad args;\n  * never reads .env;\n  * never touches production data.\n\nUsage:\n  python scripts/pas164_email_ingestion_readiness_check.py\n  python scripts/pas164_email_ingestion_readiness_check.py --json\n  python scripts/pas164_email_ingestion_readiness_check.py --summary-only\n  python scripts/pas164_email_ingestion_readiness_check.py --strict\n\nExit codes:\n    0  — READY  (verdict == READY)\n    1  — NOT_READY\n    2  — bad CLI arguments\n')
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

  80           LOAD_CONST              64 (('app/services/ingestion/email_parser.py', 'app/services/ingestion/email_ingestion.py', 'app/routes/email_ingestion.py', 'scripts/pas164_email_ingestion_readiness_check.py', 'docs/pas164_email_lead_ingestion.md', 'tests/mvp/test_pas164_email_lead_ingestion.py'))
               STORE_NAME              29 (REQUIRED_FILES)

  89           LOAD_CONST              65 (('scripts/pas160_mvp_sequence_check.py', 'scripts/pas161_lead_ingestion_readiness_check.py', 'scripts/pas162_pending_calls_readiness_check.py', 'scripts/pas163_candidate_pipeline_readiness_check.py'))
               STORE_NAME              30 (PRIOR_PHASE_FILES)

  97           LOAD_CONST              66 (('app/services/memory/review.py', 'app/services/memory/review_stats.py', 'app/services/memory/review_export.py', 'app/services/memory/review_actors.py', 'app/services/memory/review_alerts.py', 'app/services/memory/operator_console.py'))
               STORE_NAME              31 (MEMORY_REVIEW_FILES)

 107           LOAD_CONST              67 (('def parse_email_lead(', 'def detect_email_lead_source(', 'def extract_lead_fields_from_email('))
               STORE_NAME              32 (REQUIRED_PARSER_FUNCTIONS)

 113           LOAD_CONST              68 (('zillow', 'realtor', 'facebook', 'website', 'generic_email'))
               STORE_NAME              33 (REQUIRED_PARSER_SOURCES)

 121           LOAD_CONST              69 (('def ingest_email_lead(',))
               STORE_NAME              34 (REQUIRED_SERVICE_FUNCTIONS)

 127           LOAD_CONST              70 ((('@router.post("/parse")',), ('@router.post("/ingest")',)))
               STORE_NAME              35 (REQUIRED_ROUTE_DECLS)

 133           LOAD_CONST              71 (('from app.routes.email_ingestion import router as email_ingestion_router', 'app.include_router(email_ingestion_router, prefix="/email-ingestion"'))
               STORE_NAME              36 (REQUIRED_MAIN_WIRING)

 140           LOAD_CONST              72 (('email.lead.parsed', 'email.lead.ingested', 'email.lead.failed', 'email.lead.not_call_eligible'))
               STORE_NAME              37 (REQUIRED_EVENT_TYPES)

 150           LOAD_CONST              73 (('raw_email', 'raw_body', 'full_email', 'raw_payload', 'full_payload', 'transcript', 'raw_transcript', 'full_transcript'))
               STORE_NAME              38 (FORBIDDEN_PARSER_OUTPUT_KEYS)

 162           LOAD_CONST              74 (('phone', 'email', 'name', 'subject', 'sender', 'body', 'notes', 'property_address', 'transcript', 'raw_payload'))
               STORE_NAME              39 (FORBIDDEN_EVENT_PAYLOAD_KEYS)

 176           LOAD_CONST              75 (('import googleapiclient', 'from googleapiclient', 'import google.oauth2', 'from google.oauth2', 'from google.auth', 'import google.auth', 'from google_auth_oauthlib', 'from google.api_core', 'import composio', 'from composio', 'import trustclaw', 'from trustclaw', 'import openai', 'from openai', 'import anthropic', 'from anthropic', 'import numpy', 'import faiss', 'import pgvector', 'from pgvector', 'from openai import embeddings', 'from openai.embeddings', 'from app.services.memory', 'import app.services.memory'))
               STORE_NAME              40 (FORBIDDEN_IMPORT_LINE_PREFIXES)

 209           LOAD_CONST              76 (('imaplib', 'poplib', 'fetch_inbox', 'gmail_oauth', 'gmail_token', 'list_messages', 'users().messages'))
               STORE_NAME              41 (FORBIDDEN_INBOX_TOKENS)

 224           LOAD_CONST              13 ('severity')

 226           LOAD_NAME               27 (SEVERITY_BLOCK)

 224           LOAD_CONST              14 ('detail')

 226           LOAD_CONST              15 ('')

 224           BUILD_MAP                2
               LOAD_CONST              16 (<code object __annotate__ at 0x0000018C18025C30, file "scripts\pas164_email_ingestion_readiness_check.py", line 224>)
               MAKE_FUNCTION
               LOAD_CONST              17 (<code object _check at 0x0000018C17FA34B0, file "scripts\pas164_email_ingestion_readiness_check.py", line 224>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              42 (_check)

 237           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA2F10, file "scripts\pas164_email_ingestion_readiness_check.py", line 237>)
               MAKE_FUNCTION
               LOAD_CONST              19 (<code object _now_iso at 0x0000018C18038670, file "scripts\pas164_email_ingestion_readiness_check.py", line 237>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              43 (_now_iso)

 241           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA3B40, file "scripts\pas164_email_ingestion_readiness_check.py", line 241>)
               MAKE_FUNCTION
               LOAD_CONST              21 (<code object _read_text at 0x0000018C18053E10, file "scripts\pas164_email_ingestion_readiness_check.py", line 241>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              44 (_read_text)

 248           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA2970, file "scripts\pas164_email_ingestion_readiness_check.py", line 248>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object _strip_python_comments_and_strings at 0x0000018C17D6DFC0, file "scripts\pas164_email_ingestion_readiness_check.py", line 248>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              45 (_strip_python_comments_and_strings)

 287           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA33C0, file "scripts\pas164_email_ingestion_readiness_check.py", line 287>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object check_files_present at 0x0000018C180608A0, file "scripts\pas164_email_ingestion_readiness_check.py", line 287>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              46 (check_files_present)

 301           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA35A0, file "scripts\pas164_email_ingestion_readiness_check.py", line 301>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object check_prior_phases_intact at 0x0000018C18060A50, file "scripts\pas164_email_ingestion_readiness_check.py", line 301>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              47 (check_prior_phases_intact)

 315           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA3D20, file "scripts\pas164_email_ingestion_readiness_check.py", line 315>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object check_memory_review_intact at 0x0000018C18060C00, file "scripts\pas164_email_ingestion_readiness_check.py", line 315>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              48 (check_memory_review_intact)

 329           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA1D40, file "scripts\pas164_email_ingestion_readiness_check.py", line 329>)
               MAKE_FUNCTION
               LOAD_CONST              31 (<code object check_parser at 0x0000018C183F0B40, file "scripts\pas164_email_ingestion_readiness_check.py", line 329>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              49 (check_parser)

 372           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA2880, file "scripts\pas164_email_ingestion_readiness_check.py", line 372>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object check_service at 0x0000018C17EA49F0, file "scripts\pas164_email_ingestion_readiness_check.py", line 372>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              50 (check_service)

 419           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA2100, file "scripts\pas164_email_ingestion_readiness_check.py", line 419>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object check_routes at 0x0000018C17E93990, file "scripts\pas164_email_ingestion_readiness_check.py", line 419>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              51 (check_routes)

 498           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C17FA2B50, file "scripts\pas164_email_ingestion_readiness_check.py", line 498>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object check_main_wiring at 0x0000018C17FEDA30, file "scripts\pas164_email_ingestion_readiness_check.py", line 498>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              52 (check_main_wiring)

 514           LOAD_CONST              38 (<code object __annotate__ at 0x0000018C17FA32D0, file "scripts\pas164_email_ingestion_readiness_check.py", line 514>)
               MAKE_FUNCTION
               LOAD_CONST              39 (<code object check_event_contract at 0x0000018C17FED830, file "scripts\pas164_email_ingestion_readiness_check.py", line 514>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              53 (check_event_contract)

 530           LOAD_CONST              40 (<code object __annotate__ at 0x0000018C17FA3780, file "scripts\pas164_email_ingestion_readiness_check.py", line 530>)
               MAKE_FUNCTION
               LOAD_CONST              41 (<code object check_no_forbidden_imports at 0x0000018C17D8B970, file "scripts\pas164_email_ingestion_readiness_check.py", line 530>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              54 (check_no_forbidden_imports)

 558           LOAD_CONST              42 (<code object __annotate__ at 0x0000018C17FA1E30, file "scripts\pas164_email_ingestion_readiness_check.py", line 558>)
               MAKE_FUNCTION
               LOAD_CONST              43 (<code object check_no_inbox_scanning at 0x0000018C17CC2460, file "scripts\pas164_email_ingestion_readiness_check.py", line 558>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              55 (check_no_inbox_scanning)

 584           LOAD_CONST              44 (<code object __annotate__ at 0x0000018C17FA2E20, file "scripts\pas164_email_ingestion_readiness_check.py", line 584>)
               MAKE_FUNCTION
               LOAD_CONST              45 (<code object check_docs_required_doctrine at 0x0000018C17F74970, file "scripts\pas164_email_ingestion_readiness_check.py", line 584>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              56 (check_docs_required_doctrine)

 619           LOAD_CONST              46 (<code object __annotate__ at 0x0000018C17FA21F0, file "scripts\pas164_email_ingestion_readiness_check.py", line 619>)
               MAKE_FUNCTION
               LOAD_CONST              47 (<code object check_self_no_env_or_vendor at 0x0000018C17E93F70, file "scripts\pas164_email_ingestion_readiness_check.py", line 619>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              57 (check_self_no_env_or_vendor)

 669           LOAD_CONST              48 (<code object __annotate__ at 0x0000018C17FA26A0, file "scripts\pas164_email_ingestion_readiness_check.py", line 669>)
               MAKE_FUNCTION
               LOAD_CONST              49 (<code object _aggregate at 0x0000018C17EC4280, file "scripts\pas164_email_ingestion_readiness_check.py", line 669>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              58 (_aggregate)

 685           LOAD_CONST              50 (<code object __annotate__ at 0x0000018C17FA2790, file "scripts\pas164_email_ingestion_readiness_check.py", line 685>)
               MAKE_FUNCTION
               LOAD_CONST              51 (<code object _operator_actions at 0x0000018C18048C70, file "scripts\pas164_email_ingestion_readiness_check.py", line 685>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              59 (_operator_actions)

 695           LOAD_CONST              52 (<code object __annotate__ at 0x0000018C180FC030, file "scripts\pas164_email_ingestion_readiness_check.py", line 695>)
               MAKE_FUNCTION
               LOAD_CONST              53 (<code object evaluate at 0x0000018C17EA5CC0, file "scripts\pas164_email_ingestion_readiness_check.py", line 695>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              60 (evaluate)

 726           LOAD_CONST              54 ('pas164_email_ingestion_readiness_report.json')
               STORE_NAME              61 (REPORT_FILENAME)

 729           LOAD_CONST              55 (<code object __annotate__ at 0x0000018C180FC6C0, file "scripts\pas164_email_ingestion_readiness_check.py", line 729>)
               MAKE_FUNCTION
               LOAD_CONST              56 (<code object _build_parser at 0x0000018C1801C410, file "scripts\pas164_email_ingestion_readiness_check.py", line 729>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              62 (_build_parser)

 763           LOAD_CONST              57 (<code object __annotate__ at 0x0000018C180FC7B0, file "scripts\pas164_email_ingestion_readiness_check.py", line 763>)
               MAKE_FUNCTION
               LOAD_CONST              58 (<code object _print_summary at 0x0000018C17D8D460, file "scripts\pas164_email_ingestion_readiness_check.py", line 763>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              63 (_print_summary)

 781           LOAD_CONST              59 (<code object __annotate__ at 0x0000018C18024E30, file "scripts\pas164_email_ingestion_readiness_check.py", line 781>)
               MAKE_FUNCTION
               LOAD_CONST              60 (<code object _write_report at 0x0000018C179C3E10, file "scripts\pas164_email_ingestion_readiness_check.py", line 781>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              64 (_write_report)

 795           LOAD_CONST              77 ((None,))
               LOAD_CONST              61 (<code object __annotate__ at 0x0000018C180FC8A0, file "scripts\pas164_email_ingestion_readiness_check.py", line 795>)
               MAKE_FUNCTION
               LOAD_CONST              62 (<code object main at 0x0000018C17F83B80, file "scripts\pas164_email_ingestion_readiness_check.py", line 795>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              65 (main)

 823           LOAD_NAME               66 (__name__)
               LOAD_CONST              63 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 824           LOAD_NAME                6 (sys)
               LOAD_ATTR              134 (exit)
               PUSH_NULL
               LOAD_NAME               65 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 823   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  60           LOAD_NAME               18 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  61   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          331 (to L1)

  60   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025C30, file "scripts\pas164_email_ingestion_readiness_check.py", line 224>:
224           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('check_id')

225           LOAD_CONST               2 ('str')

224           LOAD_CONST               3 ('status')

225           LOAD_CONST               2 ('str')

224           LOAD_CONST               4 ('label')

225           LOAD_CONST               2 ('str')

224           LOAD_CONST               5 ('severity')

226           LOAD_CONST               2 ('str')

224           LOAD_CONST               6 ('detail')

226           LOAD_CONST               2 ('str')

224           LOAD_CONST               7 ('return')

227           LOAD_CONST               8 ('dict')

224           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _check at 0x0000018C17FA34B0, file "scripts\pas164_email_ingestion_readiness_check.py", line 224>:
224           RESUME                   0

229           LOAD_CONST               0 ('id')
              LOAD_FAST_BORROW         0 (check_id)

230           LOAD_CONST               1 ('status')
              LOAD_FAST_BORROW         1 (status)

231           LOAD_CONST               2 ('label')
              LOAD_FAST_BORROW         2 (label)

232           LOAD_CONST               3 ('severity')
              LOAD_FAST_BORROW         3 (severity)

233           LOAD_CONST               4 ('detail')
              LOAD_FAST_BORROW         4 (detail)

228           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "scripts\pas164_email_ingestion_readiness_check.py", line 237>:
237           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038670, file "scripts\pas164_email_ingestion_readiness_check.py", line 237>:
237           RESUME                   0

238           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "scripts\pas164_email_ingestion_readiness_check.py", line 241>:
241           RESUME                   0
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

Disassembly of <code object _read_text at 0x0000018C18053E10, file "scripts\pas164_email_ingestion_readiness_check.py", line 241>:
 241           RESUME                   0

 242           NOP

 243   L1:     LOAD_FAST_BORROW         0 (path)
               LOAD_ATTR                1 (read_text + NULL|self)
               LOAD_CONST               0 ('utf-8')
               LOAD_CONST               1 ('replace')
               LOAD_CONST               2 (('encoding', 'errors'))
               CALL_KW                  2
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 244           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 245   L4:     POP_EXCEPT
               LOAD_CONST               3 (None)
               RETURN_VALUE

 244   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "scripts\pas164_email_ingestion_readiness_check.py", line 248>:
248           RESUME                   0
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

Disassembly of <code object _strip_python_comments_and_strings at 0x0000018C17D6DFC0, file "scripts\pas164_email_ingestion_readiness_check.py", line 248>:
248            RESUME                   0

249            BUILD_LIST               0
               STORE_FAST               1 (out)

250            LOAD_SMALL_INT           0
               LOAD_GLOBAL              1 (len + NULL)
               LOAD_FAST_BORROW         0 (src)
               CALL                     1
               STORE_FAST_STORE_FAST   50 (n, i)

251    L1:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (i, n)
               COMPARE_OP              18 (bool(<))
               EXTENDED_ARG             1
               POP_JUMP_IF_FALSE      282 (to L13)
               NOT_TAKEN

252            LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               BINARY_OP               26 ([])
               STORE_FAST               4 (ch)

253            LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               1 ('#')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       38 (to L3)
               NOT_TAKEN

254            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_CONST               2 ('\n')
               LOAD_FAST_BORROW         2 (i)
               CALL                     2
               STORE_FAST               5 (j)

255            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L2)
               NOT_TAKEN

256            JUMP_FORWARD           240 (to L13)

257    L2:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

258            JUMP_BACKWARD           59 (to L1)

259    L3:     LOAD_FAST_BORROW         0 (src)
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

260    L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               BINARY_SLICE
               STORE_FAST               6 (quote)

261            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 98 (quote, i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               CALL                     2
               STORE_FAST               7 (end)

262            LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L5)
               NOT_TAKEN

263            JUMP_FORWARD           138 (to L13)

264    L5:     LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

265            JUMP_BACKWARD          161 (to L1)

266    L6:     LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               7 (('"', "'"))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       92 (to L12)
               NOT_TAKEN

267            LOAD_FAST                4 (ch)
               STORE_FAST               6 (quote)

268            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               5 (j)

269    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (j, n)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       63 (to L11)
               NOT_TAKEN

270            LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
               BINARY_OP               26 ([])
               LOAD_CONST               5 ('\\')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       12 (to L8)
               NOT_TAKEN

271            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           2
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)

272            JUMP_BACKWARD           30 (to L7)

273    L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
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

274    L9:     JUMP_FORWARD            11 (to L11)

275   L10:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)
               JUMP_BACKWARD           68 (to L7)

276   L11:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

277            EXTENDED_ARG             1
               JUMP_BACKWARD          259 (to L1)

278   L12:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (ch)
               CALL                     1
               POP_TOP

279            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               2 (i)
               EXTENDED_ARG             1
               JUMP_BACKWARD          288 (to L1)

280   L13:     LOAD_CONST               6 ('')
               LOAD_ATTR                9 (join + NULL|self)
               LOAD_FAST_BORROW         1 (out)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "scripts\pas164_email_ingestion_readiness_check.py", line 287>:
287           RESUME                   0
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

Disassembly of <code object check_files_present at 0x0000018C180608A0, file "scripts\pas164_email_ingestion_readiness_check.py", line 287>:
287           RESUME                   0

288           BUILD_LIST               0
              STORE_FAST               1 (out)

289           LOAD_GLOBAL              0 (REQUIRED_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

290           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

291           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

292           LOAD_CONST               0 ('file:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

293           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

294   L3:     LOAD_CONST               3 ('Required PAS164 file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

295           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

296           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing')

291   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

289   L6:     END_FOR
              POP_ITER

298           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "scripts\pas164_email_ingestion_readiness_check.py", line 301>:
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

Disassembly of <code object check_prior_phases_intact at 0x0000018C18060A50, file "scripts\pas164_email_ingestion_readiness_check.py", line 301>:
301           RESUME                   0

302           BUILD_LIST               0
              STORE_FAST               1 (out)

303           LOAD_GLOBAL              0 (PRIOR_PHASE_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
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

306           LOAD_CONST               0 ('prior_phase:')
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

308   L3:     LOAD_CONST               3 ('Prior-phase readiness script intact: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

309           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

310           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing — PAS164 must not delete')

305   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

303   L6:     END_FOR
              POP_ITER

312           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3D20, file "scripts\pas164_email_ingestion_readiness_check.py", line 315>:
315           RESUME                   0
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

Disassembly of <code object check_memory_review_intact at 0x0000018C18060C00, file "scripts\pas164_email_ingestion_readiness_check.py", line 315>:
315           RESUME                   0

316           BUILD_LIST               0
              STORE_FAST               1 (out)

317           LOAD_GLOBAL              0 (MEMORY_REVIEW_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

318           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

319           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

320           LOAD_CONST               0 ('memory_review_file:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

321           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

322   L3:     LOAD_CONST               3 ('Memory Review file present (PAS164 must not delete): ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

323           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

324           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('PAS164 must not delete Memory Review files')

319   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

317   L6:     END_FOR
              POP_ITER

326           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1D40, file "scripts\pas164_email_ingestion_readiness_check.py", line 329>:
329           RESUME                   0
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

Disassembly of <code object check_parser at 0x0000018C183F0B40, file "scripts\pas164_email_ingestion_readiness_check.py", line 329>:
  --            MAKE_CELL                9 (src)

 329            RESUME                   0

 330            BUILD_LIST               0
                STORE_FAST               1 (out)

 331            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('app')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('services')
                BINARY_OP               11 (/)
                LOAD_CONST               2 ('ingestion')
                BINARY_OP               11 (/)
                LOAD_CONST               3 ('email_parser.py')
                BINARY_OP               11 (/)
                STORE_FAST               2 (p)

 332            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (p)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               4 ('')
        L1:     STORE_DEREF              9 (src)

 333            LOAD_GLOBAL              4 (REQUIRED_PARSER_FUNCTIONS)
                GET_ITER
        L2:     FOR_ITER                93 (to L7)
                STORE_FAST               3 (needle)

 334            LOAD_FAST_BORROW         3 (needle)
                LOAD_DEREF               9 (src)
                CONTAINS_OP              0 (in)
                STORE_FAST               4 (ok)

 335            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 336            LOAD_CONST               5 ('parser_fn:')
                LOAD_FAST_BORROW         3 (needle)
                LOAD_CONST               6 (slice(None, 40, None))
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                BUILD_STRING             2

 337            LOAD_FAST_BORROW         4 (ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L3)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L4)
        L3:     LOAD_CONST               8 ('FAIL')

 338    L4:     LOAD_CONST               9 ('Parser function present: ')
                LOAD_FAST_BORROW         3 (needle)
                LOAD_ATTR               11 (strip + NULL|self)
                CALL                     0
                FORMAT_SIMPLE
                BUILD_STRING             2

 339            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 340            LOAD_FAST_BORROW         4 (ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN
                LOAD_CONST               4 ('')
                JUMP_FORWARD             4 (to L6)
        L5:     LOAD_CONST              10 ('missing def: ')
                LOAD_FAST_BORROW         3 (needle)
                FORMAT_SIMPLE
                BUILD_STRING             2

 335    L6:     LOAD_CONST              11 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           95 (to L2)

 333    L7:     END_FOR
                POP_ITER

 342            LOAD_GLOBAL             14 (REQUIRED_PARSER_SOURCES)
                GET_ITER
        L8:     FOR_ITER                74 (to L13)
                STORE_FAST               5 (source)

 343            LOAD_FAST_BORROW         5 (source)
                LOAD_DEREF               9 (src)
                CONTAINS_OP              0 (in)
                STORE_FAST               4 (ok)

 344            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 345            LOAD_CONST              12 ('parser_source:')
                LOAD_FAST_BORROW         5 (source)
                FORMAT_SIMPLE
                BUILD_STRING             2

 346            LOAD_FAST_BORROW         4 (ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L9)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L10)
        L9:     LOAD_CONST               8 ('FAIL')

 347   L10:     LOAD_CONST              13 ('Parser declares supported source: ')
                LOAD_FAST_BORROW         5 (source)
                FORMAT_SIMPLE
                BUILD_STRING             2

 348            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 349            LOAD_FAST_BORROW         4 (ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L11)
                NOT_TAKEN
                LOAD_CONST               4 ('')
                JUMP_FORWARD             6 (to L12)
       L11:     LOAD_CONST              14 ('source label ')
                LOAD_FAST_BORROW         5 (source)
                CONVERT_VALUE            2 (repr)
                FORMAT_SIMPLE
                LOAD_CONST              15 (' not declared')
                BUILD_STRING             3

 344   L12:     LOAD_CONST              11 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           76 (to L8)

 342   L13:     END_FOR
                POP_ITER

 358            LOAD_GLOBAL             16 (FORBIDDEN_PARSER_OUTPUT_KEYS)
                GET_ITER
       L14:     FOR_ITER               139 (to L24)
                STORE_FAST               6 (forbidden)

 359            LOAD_CONST              16 ('"')
                LOAD_FAST_BORROW         6 (forbidden)
                FORMAT_SIMPLE
                LOAD_CONST              17 ('":')
                BUILD_STRING             3
                LOAD_CONST              18 ("'")
                LOAD_FAST_BORROW         6 (forbidden)
                FORMAT_SIMPLE
                LOAD_CONST              19 ("':")
                BUILD_STRING             3
                BUILD_TUPLE              2
                STORE_FAST               7 (bad_shapes)

 360            LOAD_GLOBAL             18 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L18)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         9 (src)
                BUILD_TUPLE              1
                LOAD_CONST              20 (<code object <genexpr> at 0x0000018C18026230, file "scripts\pas164_email_ingestion_readiness_check.py", line 360>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         7 (bad_shapes)
                GET_ITER
                CALL                     0
       L15:     FOR_ITER                12 (to L17)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L16)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L15)
       L16:     POP_ITER
                LOAD_CONST              21 (True)
                JUMP_FORWARD            20 (to L19)
       L17:     END_FOR
                POP_ITER
                LOAD_CONST              22 (False)
                JUMP_FORWARD            16 (to L19)
       L18:     PUSH_NULL
                LOAD_FAST_BORROW         9 (src)
                BUILD_TUPLE              1
                LOAD_CONST              20 (<code object <genexpr> at 0x0000018C18026230, file "scripts\pas164_email_ingestion_readiness_check.py", line 360>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         7 (bad_shapes)
                GET_ITER
                CALL                     0
                CALL                     1
       L19:     STORE_FAST               8 (present)

 361            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 362            LOAD_CONST              23 ('parser:no_forbidden_output_key:')
                LOAD_FAST_BORROW         6 (forbidden)
                FORMAT_SIMPLE
                BUILD_STRING             2

 363            LOAD_FAST_BORROW         8 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L20)
                NOT_TAKEN
                LOAD_CONST               8 ('FAIL')
                JUMP_FORWARD             1 (to L21)
       L20:     LOAD_CONST               7 ('PASS')

 364   L21:     LOAD_CONST              24 ('Parser excludes forbidden output key: ')
                LOAD_FAST_BORROW         6 (forbidden)
                FORMAT_SIMPLE
                BUILD_STRING             2

 365            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 367            LOAD_FAST_BORROW         8 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        8 (to L22)
                NOT_TAKEN

 366            LOAD_CONST              25 ('forbidden output key ')
                LOAD_FAST_BORROW         6 (forbidden)
                CONVERT_VALUE            2 (repr)
                FORMAT_SIMPLE
                LOAD_CONST              26 (' present as dict-key')
                BUILD_STRING             3
                JUMP_FORWARD             1 (to L23)

 367   L22:     LOAD_CONST               4 ('')

 361   L23:     LOAD_CONST              11 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          141 (to L14)

 358   L24:     END_FOR
                POP_ITER

 369            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18026230, file "scripts\pas164_email_ingestion_readiness_check.py", line 360>:
  --           COPY_FREE_VARS           1

 360           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                 9 (to L3)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "scripts\pas164_email_ingestion_readiness_check.py", line 372>:
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

Disassembly of <code object check_service at 0x0000018C17EA49F0, file "scripts\pas164_email_ingestion_readiness_check.py", line 372>:
  --            MAKE_CELL               10 (src)

 372            RESUME                   0

 373            BUILD_LIST               0
                STORE_FAST               1 (out)

 374            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('app')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('services')
                BINARY_OP               11 (/)
                LOAD_CONST               2 ('ingestion')
                BINARY_OP               11 (/)
                LOAD_CONST               3 ('email_ingestion.py')
                BINARY_OP               11 (/)
                STORE_FAST               2 (p)

 375            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (p)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               4 ('')
        L1:     STORE_DEREF             10 (src)

 376            LOAD_GLOBAL              4 (REQUIRED_SERVICE_FUNCTIONS)
                GET_ITER
        L2:     FOR_ITER                93 (to L7)
                STORE_FAST               3 (needle)

 377            LOAD_FAST_BORROW         3 (needle)
                LOAD_DEREF              10 (src)
                CONTAINS_OP              0 (in)
                STORE_FAST               4 (ok)

 378            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 379            LOAD_CONST               5 ('service_fn:')
                LOAD_FAST_BORROW         3 (needle)
                LOAD_CONST               6 (slice(None, 40, None))
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                BUILD_STRING             2

 380            LOAD_FAST_BORROW         4 (ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L3)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L4)
        L3:     LOAD_CONST               8 ('FAIL')

 381    L4:     LOAD_CONST               9 ('Service function present: ')
                LOAD_FAST_BORROW         3 (needle)
                LOAD_ATTR               11 (strip + NULL|self)
                CALL                     0
                FORMAT_SIMPLE
                BUILD_STRING             2

 382            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 383            LOAD_FAST_BORROW         4 (ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN
                LOAD_CONST               4 ('')
                JUMP_FORWARD             4 (to L6)
        L5:     LOAD_CONST              10 ('missing def: ')
                LOAD_FAST_BORROW         3 (needle)
                FORMAT_SIMPLE
                BUILD_STRING             2

 378    L6:     LOAD_CONST              11 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           95 (to L2)

 376    L7:     END_FOR
                POP_ITER

 386            LOAD_CONST              12 ('missing_brokerage_id')
                LOAD_DEREF              10 (src)
                CONTAINS_OP              0 (in)
                STORE_FAST               5 (bid_ok)

 387            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 388            LOAD_CONST              13 ('service:requires_brokerage_id')

 389            LOAD_FAST_BORROW         5 (bid_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               8 ('FAIL')

 390    L9:     LOAD_CONST              14 ('Service rejects calls without brokerage_id')

 391            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 392            LOAD_FAST_BORROW         5 (bid_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN
                LOAD_CONST               4 ('')
                JUMP_FORWARD             1 (to L11)
       L10:     LOAD_CONST              15 ('missing_brokerage_id token not found')

 387   L11:     LOAD_CONST              11 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 395            LOAD_CONST              16 ('create_pending_call')
                LOAD_DEREF              10 (src)
                CONTAINS_OP              0 (in)
                STORE_FAST               6 (handoff_ok)

 396            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 397            LOAD_CONST              17 ('service:hands_off_to_pas162')

 398            LOAD_FAST_BORROW         6 (handoff_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L12)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L13)
       L12:     LOAD_CONST               8 ('FAIL')

 399   L13:     LOAD_CONST              18 ('Service hands off to PAS162 create_pending_call')

 400            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 401            LOAD_FAST_BORROW         6 (handoff_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L14)
                NOT_TAKEN
                LOAD_CONST               4 ('')
                JUMP_FORWARD             1 (to L15)
       L14:     LOAD_CONST              19 ('create_pending_call reference missing')

 396   L15:     LOAD_CONST              11 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 405            LOAD_GLOBAL             14 (FORBIDDEN_PARSER_OUTPUT_KEYS)
                GET_ITER
       L16:     FOR_ITER               139 (to L26)
                STORE_FAST               7 (forbidden)

 406            LOAD_CONST              20 ('"')
                LOAD_FAST_BORROW         7 (forbidden)
                FORMAT_SIMPLE
                LOAD_CONST              21 ('":')
                BUILD_STRING             3
                LOAD_CONST              22 ("'")
                LOAD_FAST_BORROW         7 (forbidden)
                FORMAT_SIMPLE
                LOAD_CONST              23 ("':")
                BUILD_STRING             3
                BUILD_TUPLE              2
                STORE_FAST               8 (bad_shapes)

 407            LOAD_GLOBAL             16 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L20)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW        10 (src)
                BUILD_TUPLE              1
                LOAD_CONST              24 (<code object <genexpr> at 0x0000018C18024F30, file "scripts\pas164_email_ingestion_readiness_check.py", line 407>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         8 (bad_shapes)
                GET_ITER
                CALL                     0
       L17:     FOR_ITER                12 (to L19)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L18)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L17)
       L18:     POP_ITER
                LOAD_CONST              25 (True)
                JUMP_FORWARD            20 (to L21)
       L19:     END_FOR
                POP_ITER
                LOAD_CONST              26 (False)
                JUMP_FORWARD            16 (to L21)
       L20:     PUSH_NULL
                LOAD_FAST_BORROW        10 (src)
                BUILD_TUPLE              1
                LOAD_CONST              24 (<code object <genexpr> at 0x0000018C18024F30, file "scripts\pas164_email_ingestion_readiness_check.py", line 407>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         8 (bad_shapes)
                GET_ITER
                CALL                     0
                CALL                     1
       L21:     STORE_FAST               9 (present)

 408            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 409            LOAD_CONST              27 ('service:no_forbidden_output_key:')
                LOAD_FAST_BORROW         7 (forbidden)
                FORMAT_SIMPLE
                BUILD_STRING             2

 410            LOAD_FAST_BORROW         9 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L22)
                NOT_TAKEN
                LOAD_CONST               8 ('FAIL')
                JUMP_FORWARD             1 (to L23)
       L22:     LOAD_CONST               7 ('PASS')

 411   L23:     LOAD_CONST              28 ('Service excludes forbidden output key: ')
                LOAD_FAST_BORROW         7 (forbidden)
                FORMAT_SIMPLE
                BUILD_STRING             2

 412            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 414            LOAD_FAST_BORROW         9 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        8 (to L24)
                NOT_TAKEN

 413            LOAD_CONST              29 ('forbidden output key ')
                LOAD_FAST_BORROW         7 (forbidden)
                CONVERT_VALUE            2 (repr)
                FORMAT_SIMPLE
                LOAD_CONST              30 (' present as dict-key')
                BUILD_STRING             3
                JUMP_FORWARD             1 (to L25)

 414   L24:     LOAD_CONST               4 ('')

 408   L25:     LOAD_CONST              11 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          141 (to L16)

 405   L26:     END_FOR
                POP_ITER

 416            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18024F30, file "scripts\pas164_email_ingestion_readiness_check.py", line 407>:
  --           COPY_FREE_VARS           1

 407           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                 9 (to L3)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "scripts\pas164_email_ingestion_readiness_check.py", line 419>:
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

Disassembly of <code object check_routes at 0x0000018C17E93990, file "scripts\pas164_email_ingestion_readiness_check.py", line 419>:
  --            MAKE_CELL               12 (src)

 419            RESUME                   0

 420            BUILD_LIST               0
                STORE_FAST               1 (out)

 421            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('app')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('routes')
                BINARY_OP               11 (/)
                LOAD_CONST               2 ('email_ingestion.py')
                BINARY_OP               11 (/)
                STORE_FAST               2 (p)

 422            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (p)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               3 ('')
        L1:     STORE_DEREF             12 (src)

 423            LOAD_GLOBAL              4 (REQUIRED_ROUTE_DECLS)
                GET_ITER
        L2:     FOR_ITER               146 (to L12)
                STORE_FAST               3 (decl_group)

 424            LOAD_GLOBAL              6 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW        12 (src)
                BUILD_TUPLE              1
                LOAD_CONST               4 (<code object <genexpr> at 0x0000018C18024B30, file "scripts\pas164_email_ingestion_readiness_check.py", line 424>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         3 (decl_group)
                GET_ITER
                CALL                     0
        L3:     FOR_ITER                12 (to L5)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L3)
        L4:     POP_ITER
                LOAD_CONST               5 (True)
                JUMP_FORWARD            20 (to L7)
        L5:     END_FOR
                POP_ITER
                LOAD_CONST               6 (False)
                JUMP_FORWARD            16 (to L7)
        L6:     PUSH_NULL
                LOAD_FAST_BORROW        12 (src)
                BUILD_TUPLE              1
                LOAD_CONST               4 (<code object <genexpr> at 0x0000018C18024B30, file "scripts\pas164_email_ingestion_readiness_check.py", line 424>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         3 (decl_group)
                GET_ITER
                CALL                     0
                CALL                     1
        L7:     STORE_FAST               4 (present)

 425            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 426            LOAD_CONST               7 ('route_decl:')
                LOAD_FAST_BORROW         3 (decl_group)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                BUILD_STRING             2

 427            LOAD_FAST_BORROW         4 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               8 ('PASS')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               9 ('FAIL')

 428    L9:     LOAD_CONST              10 ('Route declaration present: ')
                LOAD_FAST_BORROW         3 (decl_group)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                BUILD_STRING             2

 429            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 430            LOAD_FAST_BORROW         4 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN
                LOAD_CONST               3 ('')
                JUMP_FORWARD            11 (to L11)
       L10:     LOAD_CONST              11 ('missing decl: ')
                LOAD_FAST_BORROW         3 (decl_group)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                BUILD_STRING             2

 425   L11:     LOAD_CONST              12 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          148 (to L2)

 423   L12:     END_FOR
                POP_ITER

 433            LOAD_CONST              13 ('require_admin')
                LOAD_DEREF              12 (src)
                CONTAINS_OP              0 (in)
                STORE_FAST               5 (admin_ok)

 434            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 435            LOAD_CONST              14 ('route:auth:require_admin')

 436            LOAD_FAST_BORROW         5 (admin_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L13)
                NOT_TAKEN
                LOAD_CONST               8 ('PASS')
                JUMP_FORWARD             1 (to L14)
       L13:     LOAD_CONST               9 ('FAIL')

 437   L14:     LOAD_CONST              15 ('Route uses require_admin for /parse')

 438            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 439            LOAD_FAST_BORROW         5 (admin_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L15)
                NOT_TAKEN
                LOAD_CONST               3 ('')
                JUMP_FORWARD             1 (to L16)
       L15:     LOAD_CONST              16 ('require_admin reference missing')

 434   L16:     LOAD_CONST              12 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 441            LOAD_CONST              17 ('require_brokerage')
                LOAD_DEREF              12 (src)
                CONTAINS_OP              0 (in)
                STORE_FAST               6 (broker_ok)

 442            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 443            LOAD_CONST              18 ('route:auth:require_brokerage')

 444            LOAD_FAST_BORROW         6 (broker_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L17)
                NOT_TAKEN
                LOAD_CONST               8 ('PASS')
                JUMP_FORWARD             1 (to L18)
       L17:     LOAD_CONST               9 ('FAIL')

 445   L18:     LOAD_CONST              19 ('Route uses require_brokerage for /ingest')

 446            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 447            LOAD_FAST_BORROW         6 (broker_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L19)
                NOT_TAKEN
                LOAD_CONST               3 ('')
                JUMP_FORWARD             1 (to L20)
       L19:     LOAD_CONST              20 ('require_brokerage reference missing')

 442   L20:     LOAD_CONST              12 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 451            LOAD_GLOBAL             15 (_strip_python_comments_and_strings + NULL)
                LOAD_DEREF              12 (src)
                CALL                     1
                STORE_FAST               7 (executable)

 452            LOAD_CONST              32 (('body.brokerage_id', 'body["brokerage_id"]', "body['brokerage_id']"))
                GET_ITER
       L21:     FOR_ITER                80 (to L26)
                STORE_FAST               8 (bad_pattern)

 457            LOAD_FAST_BORROW_LOAD_FAST_BORROW 135 (bad_pattern, executable)
                CONTAINS_OP              0 (in)
                STORE_FAST               4 (present)

 458            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 459            LOAD_CONST              21 ('route:no_body_trust:')
                LOAD_FAST_BORROW         8 (bad_pattern)
                LOAD_CONST              22 (slice(None, 40, None))
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                BUILD_STRING             2

 460            LOAD_FAST_BORROW         4 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L22)
                NOT_TAKEN
                LOAD_CONST               9 ('FAIL')
                JUMP_FORWARD             1 (to L23)
       L22:     LOAD_CONST               8 ('PASS')

 461   L23:     LOAD_CONST              23 ('Route never reads brokerage_id from body: ')
                LOAD_FAST_BORROW         8 (bad_pattern)
                FORMAT_SIMPLE
                BUILD_STRING             2

 462            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 464            LOAD_FAST_BORROW         4 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        8 (to L24)
                NOT_TAKEN

 463            LOAD_CONST              24 ('body-trust pattern ')
                LOAD_FAST_BORROW         8 (bad_pattern)
                CONVERT_VALUE            2 (repr)
                FORMAT_SIMPLE
                LOAD_CONST              25 (' present')
                BUILD_STRING             3
                JUMP_FORWARD             1 (to L25)

 464   L24:     LOAD_CONST               3 ('')

 458   L25:     LOAD_CONST              12 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           82 (to L21)

 452   L26:     END_FOR
                POP_ITER

 467            LOAD_GLOBAL             16 (FORBIDDEN_EVENT_PAYLOAD_KEYS)
                GET_ITER
       L27:     FOR_ITER               202 (to L33)
                STORE_FAST               9 (forbidden)

 474            LOAD_CONST              26 ('"')
                LOAD_FAST_BORROW         9 (forbidden)
                FORMAT_SIMPLE
                LOAD_CONST              26 ('"')
                BUILD_STRING             3
                STORE_FAST              10 (candidate)

 476            LOAD_FAST_BORROW        10 (candidate)
                LOAD_DEREF              12 (src)
                CONTAINS_OP              0 (in)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE      115 (to L28)
                NOT_TAKEN
                POP_TOP

 477            LOAD_CONST              27 ('_EVENT_PAYLOAD_ALLOWED')
                LOAD_DEREF              12 (src)
                CONTAINS_OP              0 (in)

 476            COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE      102 (to L28)
                NOT_TAKEN
                POP_TOP

 481            LOAD_DEREF              12 (src)
                LOAD_ATTR               19 (find + NULL|self)
                LOAD_FAST_BORROW        10 (candidate)
                CALL                     1
                LOAD_DEREF              12 (src)
                LOAD_ATTR               19 (find + NULL|self)
                LOAD_CONST              27 ('_EVENT_PAYLOAD_ALLOWED')
                CALL                     1
                COMPARE_OP             132 (>)

 476            COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       59 (to L28)
                NOT_TAKEN
                POP_TOP

 482            LOAD_DEREF              12 (src)
                LOAD_ATTR               19 (find + NULL|self)
                LOAD_FAST_BORROW        10 (candidate)
                CALL                     1

 483            LOAD_DEREF              12 (src)
                LOAD_ATTR               19 (find + NULL|self)
                LOAD_CONST              27 ('_EVENT_PAYLOAD_ALLOWED')
                CALL                     1

 484            LOAD_GLOBAL             21 (len + NULL)
                LOAD_CONST              27 ('_EVENT_PAYLOAD_ALLOWED')
                CALL                     1

 483            BINARY_OP                0 (+)

 484            LOAD_CONST              28 (1024)

 483            BINARY_OP                0 (+)

 482            COMPARE_OP               2 (<)

 475   L28:     STORE_FAST              11 (present_in_allowed)

 487            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 488            LOAD_CONST              29 ('route:event_allowlist_excludes:')
                LOAD_FAST_BORROW         9 (forbidden)
                FORMAT_SIMPLE
                BUILD_STRING             2

 489            LOAD_FAST_BORROW        11 (present_in_allowed)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L29)
                NOT_TAKEN
                LOAD_CONST               9 ('FAIL')
                JUMP_FORWARD             1 (to L30)
       L29:     LOAD_CONST               8 ('PASS')

 490   L30:     LOAD_CONST              30 ('Event payload allow-list excludes forbidden key: ')
                LOAD_FAST_BORROW         9 (forbidden)
                FORMAT_SIMPLE
                BUILD_STRING             2

 491            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 493            LOAD_FAST_BORROW        11 (present_in_allowed)
                TO_BOOL
                POP_JUMP_IF_FALSE        8 (to L31)
                NOT_TAKEN

 492            LOAD_CONST              31 ('forbidden allow-list key ')
                LOAD_FAST_BORROW         9 (forbidden)
                CONVERT_VALUE            2 (repr)
                FORMAT_SIMPLE
                LOAD_CONST              25 (' present')
                BUILD_STRING             3
                JUMP_FORWARD             1 (to L32)

 493   L31:     LOAD_CONST               3 ('')

 487   L32:     LOAD_CONST              12 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          204 (to L27)

 467   L33:     END_FOR
                POP_ITER

 495            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18024B30, file "scripts\pas164_email_ingestion_readiness_check.py", line 424>:
  --           COPY_FREE_VARS           1

 424           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                 9 (to L3)
               STORE_FAST_LOAD_FAST    17 (d, d)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "scripts\pas164_email_ingestion_readiness_check.py", line 498>:
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

Disassembly of <code object check_main_wiring at 0x0000018C17FEDA30, file "scripts\pas164_email_ingestion_readiness_check.py", line 498>:
498           RESUME                   0

499           BUILD_LIST               0
              STORE_FAST               1 (out)

500           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('main.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

501           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               2 ('')
      L1:     STORE_FAST               3 (src)

502           LOAD_GLOBAL              4 (REQUIRED_MAIN_WIRING)
              GET_ITER
      L2:     FOR_ITER                85 (to L7)
              STORE_FAST               4 (needle)

503           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (needle, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

504           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

505           LOAD_CONST               3 ('main_wiring:')
              LOAD_FAST_BORROW         4 (needle)
              LOAD_CONST               4 (slice(None, 48, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

506           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               5 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               6 ('FAIL')

507   L4:     LOAD_CONST               7 ('main.py wiring present: ')
              LOAD_FAST_BORROW         4 (needle)
              LOAD_CONST               4 (slice(None, 48, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

508           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

509           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               2 ('')
              JUMP_FORWARD             4 (to L6)
      L5:     LOAD_CONST               8 ('missing wiring: ')
              LOAD_FAST_BORROW         4 (needle)
              FORMAT_SIMPLE
              BUILD_STRING             2

504   L6:     LOAD_CONST               9 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           87 (to L2)

502   L7:     END_FOR
              POP_ITER

511           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA32D0, file "scripts\pas164_email_ingestion_readiness_check.py", line 514>:
514           RESUME                   0
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

Disassembly of <code object check_event_contract at 0x0000018C17FED830, file "scripts\pas164_email_ingestion_readiness_check.py", line 514>:
514           RESUME                   0

515           BUILD_LIST               0
              STORE_FAST               1 (out)

516           LOAD_GLOBAL              1 (Path + NULL)
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

517           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

518           LOAD_GLOBAL              4 (REQUIRED_EVENT_TYPES)
              GET_ITER
      L2:     FOR_ITER                72 (to L7)
              STORE_FAST               4 (required)

519           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (required, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

520           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

521           LOAD_CONST               5 ('events:')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

522           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               6 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               7 ('FAIL')

523   L4:     LOAD_CONST               8 ('Event contract registers ')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

524           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

525           LOAD_FAST_BORROW         5 (ok)
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

520   L6:     LOAD_CONST              10 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           74 (to L2)

518   L7:     END_FOR
              POP_ITER

527           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "scripts\pas164_email_ingestion_readiness_check.py", line 530>:
530           RESUME                   0
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

Disassembly of <code object check_no_forbidden_imports at 0x0000018C17D8B970, file "scripts\pas164_email_ingestion_readiness_check.py", line 530>:
530            RESUME                   0

531            BUILD_LIST               0
               STORE_FAST               1 (out)

532            LOAD_CONST               9 (('app/services/ingestion/email_parser.py', 'app/services/ingestion/email_ingestion.py', 'app/routes/email_ingestion.py', 'scripts/pas164_email_ingestion_readiness_check.py'))
               STORE_FAST               2 (files)

538            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               241 (to L12)
               STORE_FAST               3 (relpath)

539            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

540            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L2:     STORE_FAST               5 (src)

541            BUILD_LIST               0
               STORE_FAST               6 (bad)

542            LOAD_FAST_BORROW         5 (src)
               LOAD_ATTR                5 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L3:     FOR_ITER                74 (to L7)
               STORE_FAST               7 (line)

543            LOAD_FAST_BORROW         7 (line)
               LOAD_ATTR                7 (strip + NULL|self)
               CALL                     0
               STORE_FAST               8 (stripped)

544            LOAD_GLOBAL              8 (FORBIDDEN_IMPORT_LINE_PREFIXES)
               GET_ITER
       L4:     FOR_ITER                45 (to L6)
               STORE_FAST               9 (prefix)

545            LOAD_FAST_BORROW         8 (stripped)
               LOAD_ATTR               11 (startswith + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           28 (to L4)

546    L5:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR               13 (append + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           47 (to L4)

544    L6:     END_FOR
               POP_ITER
               JUMP_BACKWARD           76 (to L3)

542    L7:     END_FOR
               POP_ITER

547            LOAD_FAST                1 (out)
               LOAD_ATTR               13 (append + NULL|self)
               LOAD_GLOBAL             15 (_check + NULL)

548            LOAD_CONST               2 ('forbidden_import:')
               LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR               16 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

549            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST               4 ('PASS')

550    L9:     LOAD_CONST               5 ('No forbidden imports: ')
               LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR               16 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

551            LOAD_GLOBAL             18 (SEVERITY_BLOCK)

553            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L10)
               NOT_TAKEN

552            LOAD_CONST               6 ('forbidden import prefixes: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               21 (join + NULL|self)
               LOAD_FAST_BORROW         6 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L11)

553   L10:     LOAD_CONST               1 ('')

547   L11:     LOAD_CONST               8 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          243 (to L1)

538   L12:     END_FOR
               POP_ITER

555            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "scripts\pas164_email_ingestion_readiness_check.py", line 558>:
558           RESUME                   0
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

Disassembly of <code object check_no_inbox_scanning at 0x0000018C17CC2460, file "scripts\pas164_email_ingestion_readiness_check.py", line 558>:
558            RESUME                   0

559            BUILD_LIST               0
               STORE_FAST               1 (out)

560            LOAD_CONST               9 (('app/services/ingestion/email_parser.py', 'app/services/ingestion/email_ingestion.py', 'app/routes/email_ingestion.py'))
               STORE_FAST               2 (files)

565            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               196 (to L10)
               STORE_FAST               3 (relpath)

566            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

567            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L2:     STORE_FAST               5 (src)

568            LOAD_GLOBAL              5 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         5 (src)
               CALL                     1
               STORE_FAST               6 (executable)

569            BUILD_LIST               0
               STORE_FAST               7 (bad)

570            LOAD_GLOBAL              6 (FORBIDDEN_INBOX_TOKENS)
               GET_ITER
       L3:     FOR_ITER                28 (to L5)
               STORE_FAST               8 (token)

571            LOAD_FAST_BORROW_LOAD_FAST_BORROW 134 (token, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L3)

572    L4:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_FAST_BORROW         8 (token)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L3)

570    L5:     END_FOR
               POP_ITER

573            LOAD_FAST                1 (out)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_GLOBAL             11 (_check + NULL)

574            LOAD_CONST               2 ('no_inbox_scan:')
               LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR               12 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

575            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L6)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L7)
       L6:     LOAD_CONST               4 ('PASS')

576    L7:     LOAD_CONST               5 ('No inbox-scanning tokens: ')
               LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR               12 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

577            LOAD_GLOBAL             14 (SEVERITY_BLOCK)

579            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L8)
               NOT_TAKEN

578            LOAD_CONST               6 ('inbox-scan tokens present: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               17 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L9)

579    L8:     LOAD_CONST               1 ('')

573    L9:     LOAD_CONST               8 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          198 (to L1)

565   L10:     END_FOR
               POP_ITER

581            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "scripts\pas164_email_ingestion_readiness_check.py", line 584>:
584           RESUME                   0
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

Disassembly of <code object check_docs_required_doctrine at 0x0000018C17F74970, file "scripts\pas164_email_ingestion_readiness_check.py", line 584>:
  --            MAKE_CELL                8 (lower)

 584            RESUME                   0

 585            BUILD_LIST               0
                STORE_FAST               1 (out)

 586            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('docs')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('pas164_email_lead_ingestion.md')
                BINARY_OP               11 (/)
                STORE_FAST               2 (doc)

 587            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (doc)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L1:     STORE_FAST               3 (src)

 588            LOAD_FAST_BORROW         3 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_DEREF              8 (lower)

 589            LOAD_CONST              13 ((('purpose', ('purpose',)), ('supported-sources', ('supported', 'zillow', 'realtor', 'facebook')), ('parse-endpoint', ('/parse',)), ('ingest-endpoint', ('/ingest',)), ('auth-model', ('auth', 'x-admin-key', 'x-api-key')), ('no-gmail-oauth', ('no gmail oauth', 'no gmail')), ('no-inbox-scan', ('no inbox scanning', 'no inbox', 'no inbox scan')), ('no-raw-email', ('no raw email', 'raw email body', 'no raw body')), ('normalized-mapping', ('normalizedlead', 'normalized lead')), ('pending-call-behavior', ('pending call', 'pending_call')), ('not-built', ('intentionally not built', 'what is intentionally not built', 'deliberately not')), ('brokerage-demos', ('brokerage demo', 'brokerage demos'))))
                STORE_FAST               4 (required_phrases)

 606            LOAD_FAST_BORROW         4 (required_phrases)
                GET_ITER
        L2:     FOR_ITER               146 (to L12)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   86 (name, phrases)

 607            LOAD_GLOBAL              6 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         8 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18025730, file "scripts\pas164_email_ingestion_readiness_check.py", line 607>)
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
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18025730, file "scripts\pas164_email_ingestion_readiness_check.py", line 607>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         6 (phrases)
                GET_ITER
                CALL                     0
                CALL                     1
        L7:     STORE_FAST               7 (present)

 608            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 609            LOAD_CONST               6 ('docs:phrase:')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 610            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               8 ('FAIL')

 611    L9:     LOAD_CONST               9 ('Doc carries clause: ')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 612            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 614            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L10)
                NOT_TAKEN

 613            LOAD_CONST              10 ('expected one of: ')
                LOAD_CONST              11 (' | ')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_FAST_BORROW         6 (phrases)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L11)

 614   L10:     LOAD_CONST               2 ('')

 608   L11:     LOAD_CONST              12 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          148 (to L2)

 606   L12:     END_FOR
                POP_ITER

 616            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18025730, file "scripts\pas164_email_ingestion_readiness_check.py", line 607>:
  --           COPY_FREE_VARS           1

 607           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "scripts\pas164_email_ingestion_readiness_check.py", line 619>:
619           RESUME                   0
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

Disassembly of <code object check_self_no_env_or_vendor at 0x0000018C17E93F70, file "scripts\pas164_email_ingestion_readiness_check.py", line 619>:
619            RESUME                   0

620            BUILD_LIST               0
               STORE_FAST               1 (out)

621            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_GLOBAL              2 (__file__)
               CALL                     1
               LOAD_ATTR                5 (resolve + NULL|self)
               CALL                     0
               STORE_FAST               2 (self_path)

622            LOAD_GLOBAL              7 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (self_path)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L1:     STORE_FAST               3 (src)

623            BUILD_LIST               0
               STORE_FAST               4 (bad)

624            LOAD_FAST_BORROW         3 (src)
               LOAD_ATTR                9 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L2:     EXTENDED_ARG             1
               FOR_ITER               311 (to L11)
               STORE_FAST               5 (raw_line)

625            LOAD_FAST_BORROW         5 (raw_line)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0
               STORE_FAST               6 (stripped)

626            LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST               1 ('#')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

627            JUMP_BACKWARD           45 (to L2)

628    L3:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              16 (('import dotenv', 'from dotenv'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L4)
               NOT_TAKEN

629            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               2 ('dotenv import')
               CALL                     1
               POP_TOP

630    L4:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              17 (('import supabase', 'from supabase'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L5)
               NOT_TAKEN

631            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               3 ('supabase import')
               CALL                     1
               POP_TOP

632    L5:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              18 (('import composio', 'from composio', 'import trustclaw', 'from trustclaw', 'import openai', 'from openai', 'import anthropic', 'from anthropic', 'import googleapiclient', 'from googleapiclient', 'import google.oauth2', 'from google.oauth2'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L6)
               NOT_TAKEN

640            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               4 ('external-vendor / google import')
               CALL                     1
               POP_TOP

641    L6:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              19 (('import numpy', 'import faiss', 'import pgvector', 'from pgvector', 'from openai import embeddings', 'from openai.embeddings'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L7)
               NOT_TAKEN

647            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               5 ('embedding / vector import')
               CALL                     1
               POP_TOP

648    L7:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST               6 ('load_dotenv()')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        24 (to L8)
               NOT_TAKEN

649            LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               17 (endswith + NULL|self)
               LOAD_CONST               6 ('load_dotenv()')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L9)
               NOT_TAKEN

650    L8:     LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               7 ('load_dotenv() call')
               CALL                     1
               POP_TOP

651    L9:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              20 (('os.environ[', 'os.getenv(', 'getenv('))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         4 (to L10)
               NOT_TAKEN
               EXTENDED_ARG             1
               JUMP_BACKWARD          294 (to L2)

652   L10:     LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               8 ('environ read')
               CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          314 (to L2)

624   L11:     END_FOR
               POP_ITER

653            LOAD_FAST                1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             19 (_check + NULL)

654            LOAD_CONST               9 ('self_check:no_env_or_vendor')

655            LOAD_FAST_BORROW         4 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L12)
               NOT_TAKEN
               LOAD_CONST              10 ('FAIL')
               JUMP_FORWARD             1 (to L13)
      L12:     LOAD_CONST              11 ('PASS')

656   L13:     LOAD_CONST              12 ('PAS164 readiness checker never reads .env, calls Supabase, or imports vendor / Google / embedding libs')

658            LOAD_GLOBAL             20 (SEVERITY_BLOCK)

660            LOAD_FAST_BORROW         4 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L14)
               NOT_TAKEN

659            LOAD_CONST              13 ('disqualifying code-line patterns: ')
               LOAD_CONST              14 (', ')
               LOAD_ATTR               23 (join + NULL|self)
               LOAD_FAST_BORROW         4 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L15)

660   L14:     LOAD_CONST               0 ('')

653   L15:     LOAD_CONST              15 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

662            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA26A0, file "scripts\pas164_email_ingestion_readiness_check.py", line 669>:
669           RESUME                   0
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

Disassembly of <code object _aggregate at 0x0000018C17EC4280, file "scripts\pas164_email_ingestion_readiness_check.py", line 669>:
 669            RESUME                   0

 671            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 670            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2

 671    L2:     FOR_ITER                49 (to L7)
                STORE_FAST               1 (c)

 672            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 671    L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L2)

 672    L4:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              2 (SEVERITY_BLOCK)
                COMPARE_OP              88 (bool(==))

 671    L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L2)
        L6:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L2)
        L7:     END_FOR
                POP_ITER

 670    L8:     STORE_FAST               2 (blockers)
                STORE_FAST               1 (c)

 675            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 674            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L9:     BUILD_LIST               0
                SWAP                     2

 675   L10:     FOR_ITER                49 (to L15)
                STORE_FAST               1 (c)

 676            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 675   L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L10)

 676   L12:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              4 (SEVERITY_INFO)
                COMPARE_OP              88 (bool(==))

 675   L13:     POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L10)
       L14:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L10)
       L15:     END_FOR
                POP_ITER

 674   L16:     STORE_FAST               3 (info)
                STORE_FAST               1 (c)

 679            LOAD_CONST               3 ('verdict')
                LOAD_FAST_BORROW         2 (blockers)
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L17)
                NOT_TAKEN
                LOAD_GLOBAL              6 (VERDICT_NOT_READY)
                JUMP_FORWARD             5 (to L18)
       L17:     LOAD_GLOBAL              8 (VERDICT_READY)

 680   L18:     LOAD_CONST               4 ('blockers')
                LOAD_FAST_BORROW         2 (blockers)

 681            LOAD_CONST               5 ('info')
                LOAD_FAST_BORROW         3 (info)

 678            BUILD_MAP                3
                RETURN_VALUE

  --   L19:     SWAP                     2
                POP_TOP

 670            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0

  --   L20:     SWAP                     2
                POP_TOP

 674            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L19 [2]
  L4 to L5 -> L19 [2]
  L6 to L8 -> L19 [2]
  L9 to L11 -> L20 [2]
  L12 to L13 -> L20 [2]
  L14 to L16 -> L20 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA2790, file "scripts\pas164_email_ingestion_readiness_check.py", line 685>:
685           RESUME                   0
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

Disassembly of <code object _operator_actions at 0x0000018C18048C70, file "scripts\pas164_email_ingestion_readiness_check.py", line 685>:
685           RESUME                   0

686           BUILD_LIST               0
              STORE_FAST               1 (out)

687           LOAD_FAST_BORROW         0 (checks)
              GET_ITER
      L1:     FOR_ITER               109 (to L5)
              STORE_FAST               2 (c)

688           LOAD_FAST_BORROW         2 (c)
              LOAD_CONST               0 ('status')
              BINARY_OP               26 ([])
              LOAD_CONST               1 ('FAIL')
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

689           JUMP_BACKWARD           19 (to L1)

690   L2:     LOAD_FAST_BORROW         2 (c)
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

691           LOAD_FAST                1 (out)
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

687   L5:     END_FOR
              POP_ITER

692           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180FC030, file "scripts\pas164_email_ingestion_readiness_check.py", line 695>:
695           RESUME                   0
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

Disassembly of <code object evaluate at 0x0000018C17EA5CC0, file "scripts\pas164_email_ingestion_readiness_check.py", line 695>:
695           RESUME                   0

696           BUILD_LIST               0
              STORE_FAST               1 (checks)

697           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              3 (check_files_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

698           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              5 (check_prior_phases_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

699           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              7 (check_memory_review_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

700           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              9 (check_parser + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

701           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             11 (check_service + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

702           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             13 (check_routes + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

703           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             15 (check_main_wiring + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

704           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             17 (check_event_contract + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

705           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             19 (check_no_forbidden_imports + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

706           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             21 (check_no_inbox_scanning + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

707           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             23 (check_docs_required_doctrine + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

708           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             25 (check_self_no_env_or_vendor + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

710           LOAD_GLOBAL             27 (_aggregate + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1
              STORE_FAST               2 (agg)

712           LOAD_CONST               0 ('phase')
              LOAD_CONST               1 ('PAS164')

713           LOAD_CONST               2 ('generated_at')
              LOAD_GLOBAL             29 (_now_iso + NULL)
              CALL                     0

714           LOAD_CONST               3 ('verdict')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])

715           LOAD_CONST               4 ('ready')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])
              LOAD_GLOBAL             30 (VERDICT_READY)
              COMPARE_OP              72 (==)

716           LOAD_CONST               5 ('blocker_count')
              LOAD_GLOBAL             33 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               6 ('blockers')
              BINARY_OP               26 ([])
              CALL                     1

717           LOAD_CONST               7 ('info_count')
              LOAD_GLOBAL             33 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               8 ('info')
              BINARY_OP               26 ([])
              CALL                     1

718           LOAD_CONST               9 ('check_count')
              LOAD_GLOBAL             33 (len + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

719           LOAD_CONST              10 ('pass_count')
              LOAD_GLOBAL             35 (sum + NULL)
              LOAD_CONST              11 (<code object <genexpr> at 0x0000018C18053510, file "scripts\pas164_email_ingestion_readiness_check.py", line 719>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

720           LOAD_CONST              12 ('fail_count')
              LOAD_GLOBAL             35 (sum + NULL)
              LOAD_CONST              13 (<code object <genexpr> at 0x0000018C18053750, file "scripts\pas164_email_ingestion_readiness_check.py", line 720>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

721           LOAD_CONST              14 ('checks')
              LOAD_FAST_BORROW         1 (checks)

722           LOAD_CONST              15 ('operator_actions')
              LOAD_GLOBAL             37 (_operator_actions + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

711           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18053510, file "scripts\pas164_email_ingestion_readiness_check.py", line 719>:
 719           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C18053750, file "scripts\pas164_email_ingestion_readiness_check.py", line 720>:
 720           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C180FC6C0, file "scripts\pas164_email_ingestion_readiness_check.py", line 729>:
729           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C1801C410, file "scripts\pas164_email_ingestion_readiness_check.py", line 729>:
729           RESUME                   0

730           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

731           LOAD_CONST               0 ('pas164_email_ingestion_readiness_check')

733           LOAD_CONST               1 ('PAS164 — Evaluate the email-ingestion subsystem for structural correctness, no-Gmail-OAuth doctrine, no inbox scanning, and absence of raw-body / identifying field leakage. Read-only. Does not touch Supabase, .env, or any tenant data.')

730           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

740           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

741           LOAD_CONST               3 ('--repo-root')
              LOAD_GLOBAL              6 (_REPO_ROOT_DEFAULT)

742           LOAD_CONST               4 ('Repo root to evaluate (default: parent of this script).')

740           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

744           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

745           LOAD_CONST               6 ('--output')
              LOAD_GLOBAL              8 (REPORT_FILENAME)

746           LOAD_CONST               7 ('Where to write the JSON report (default ./')
              LOAD_GLOBAL              8 (REPORT_FILENAME)
              FORMAT_SIMPLE
              LOAD_CONST               8 (').')
              BUILD_STRING             3

744           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

748           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

749           LOAD_CONST               9 ('--json')
              LOAD_CONST              10 ('store_true')

750           LOAD_CONST              11 ('Emit the report JSON on stdout in addition to the file.')

748           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

752           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

753           LOAD_CONST              13 ('--summary-only')
              LOAD_CONST              10 ('store_true')

754           LOAD_CONST              14 ('Skip writing the full report file; print verdict only.')

752           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

756           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

757           LOAD_CONST              15 ('--strict')
              LOAD_CONST              10 ('store_true')

758           LOAD_CONST              16 ('Exit 1 unless verdict == READY (default policy is the same).')

756           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

760           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180FC7B0, file "scripts\pas164_email_ingestion_readiness_check.py", line 763>:
763           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C17D8D460, file "scripts\pas164_email_ingestion_readiness_check.py", line 763>:
763           RESUME                   0

764           LOAD_GLOBAL              1 (print + NULL)

765           LOAD_CONST               0 ('[PAS164] verdict=')
              LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               1 ('verdict')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               2 (' blockers=')

766           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               3 ('blocker_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' info=')

767           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               5 ('info_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' checks=')

768           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               7 ('check_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' pass=')

769           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               9 ('pass_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              10 (' fail=')

770           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              11 ('fail_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE

765           BUILD_STRING            12

764           CALL                     1
              POP_TOP

772           LOAD_FAST_BORROW         0 (report)
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

773           LOAD_FAST_BORROW         1 (actions)
              TO_BOOL
              POP_JUMP_IF_FALSE       93 (to L5)
              NOT_TAKEN

774           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              13 ('[PAS164] operator actions:')
              CALL                     1
              POP_TOP

775           LOAD_FAST_BORROW         1 (actions)
              LOAD_CONST              14 (slice(None, 25, None))
              BINARY_OP               26 ([])
              GET_ITER
      L2:     FOR_ITER                17 (to L3)
              STORE_FAST               2 (a)

776           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              15 ('  - ')
              LOAD_FAST_BORROW         2 (a)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L2)

775   L3:     END_FOR
              POP_ITER

777           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         1 (actions)
              CALL                     1
              LOAD_SMALL_INT          25
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       34 (to L4)
              NOT_TAKEN

778           LOAD_GLOBAL              1 (print + NULL)
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

777   L4:     LOAD_CONST              18 (None)
              RETURN_VALUE

773   L5:     LOAD_CONST              18 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024E30, file "scripts\pas164_email_ingestion_readiness_check.py", line 781>:
781           RESUME                   0
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

Disassembly of <code object _write_report at 0x0000018C179C3E10, file "scripts\pas164_email_ingestion_readiness_check.py", line 781>:
 781           RESUME                   0

 782           NOP

 783   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

 784           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

 785           LOAD_CONST               3 ('utf-8')

 783           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 787           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

 788   L4:     LOAD_GLOBAL             11 (print + NULL)

 789           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

 790           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

 789           BUILD_STRING             4

 791           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

 788           LOAD_CONST               7 (('file',))
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

 787   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C180FC8A0, file "scripts\pas164_email_ingestion_readiness_check.py", line 795>:
795           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17F83B80, file "scripts\pas164_email_ingestion_readiness_check.py", line 795>:
 795            RESUME                   0

 796            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 797            NOP

 798    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 802    L2:     LOAD_GLOBAL             10 (os)
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

 803            LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               21 (isdir + NULL|self)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L4)
                NOT_TAKEN

 804            LOAD_GLOBAL             23 (print + NULL)

 805            LOAD_CONST               2 ('error: --repo-root not a directory: ')
                LOAD_FAST                4 (repo_root)
                FORMAT_SIMPLE
                BUILD_STRING             2

 806            LOAD_GLOBAL             24 (sys)
                LOAD_ATTR               26 (stderr)

 804            LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

 808            LOAD_SMALL_INT           2
                RETURN_VALUE

 810    L4:     LOAD_GLOBAL             29 (evaluate + NULL)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                STORE_FAST               5 (report)

 812            LOAD_FAST                2 (args)
                LOAD_ATTR               30 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L5)
                NOT_TAKEN

 813            LOAD_GLOBAL             33 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               34 (output)
                LOAD_FAST                5 (report)
                CALL                     2
                POP_TOP

 815    L5:     LOAD_GLOBAL             37 (_print_summary + NULL)
                LOAD_FAST                5 (report)
                CALL                     1
                POP_TOP

 817            LOAD_FAST                2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L6)
                NOT_TAKEN

 818            LOAD_GLOBAL             23 (print + NULL)
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

 820    L6:     LOAD_FAST                5 (report)
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

 799            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L17)
                NOT_TAKEN
                STORE_FAST               3 (e)

 800    L9:     LOAD_FAST                3 (e)
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

 799   L17:     RERAISE                  0

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
