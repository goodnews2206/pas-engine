# scripts_readiness/pas166_email_dedupe_policy_readiness_check

- **pyc:** `scripts\__pycache__\pas166_email_dedupe_policy_readiness_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/pas166_email_dedupe_policy_readiness_check.py`
- **co_filename (from bytecode):** `scripts\pas166_email_dedupe_policy_readiness_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS166 — Durable email dedupe + signature-required policy
readiness gate.

Deterministic, non-mutating evaluator for "is the PAS166
durable email-dedupe + signature-required policy layer wired
correctly, structurally safe, and free of regression vs
PAS164 / PAS165 doctrine?".

Walks the repo and verifies:

  * scripts/migrate_v15_email_dedupe.sql exists as a proposal
    (NOT executed in PAS166);
  * the SQL declares the required columns + closed source
    enum + RLS + tenant write-denial;
  * the SQL declares NO raw body / subject / sender / phone /
    email columns;
  * app/services/ingestion/email_dedupe_store.py exists and
    exports the required helpers;
  * the durable store has no DB exception escape and surfaces
    ``durable_email_dedupe_unavailable`` on failure;
  * the dedupe store NEVER reads brokerage_id from a payload;
  * the email-ingestion service exposes the new kwargs +
    response fields (``forwarder_required``,
    ``dedupe_durable``);
  * the signature-required policy helper is strict-literal-True
    (the helper never matches a string ``"true"`` / int ``1``);
  * the route exposes the new fields and reads the brokerage
    row only as the source of truth for the required flag;
  * the event allow-list excludes phone / email / name /
    subject / sender / body / signature / dedupe_key / secret /
    raw_email / raw_body / property_address / notes /
    transcript;
  * no Gmail / Google / IMAP / POP3 / inbox-scan tokens;
  * no embedding / vector / vendor imports;
  * Memory Review UI files are intact;
  * prior-phase readiness scripts (PAS160 / PAS161 / PAS162 /
    PAS163 / PAS164 / PAS165) still exist;
  * supports --summary-only and --json;
  * exits 0 ready, 1 blockers, 2 bad args;
  * never reads .env;
  * never touches production data.

Usage:
  python scripts/pas166_email_dedupe_policy_readiness_check.py
  python scripts/pas166_email_dedupe_policy_readiness_check.py --json
  python scripts/pas166_email_dedupe_policy_readiness_check.py --summary-only
  python scripts/pas166_email_dedupe_policy_readiness_check.py --strict

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

`__annotate__`, `_aggregate`, `_build_parser`, `_check`, `_now_iso`, `_operator_actions`, `_print_summary`, `_read_text`, `_strip_python_comments_and_strings`, `_strip_sql_comments`, `_write_report`, `check_dedupe_store`, `check_docs_required_doctrine`, `check_event_contract`, `check_files_present`, `check_memory_review_intact`, `check_migration_proposal`, `check_no_forbidden_imports`, `check_no_inbox_scanning`, `check_prior_phases_intact`, `check_route_integration`, `check_self_no_env_or_vendor`, `check_service_integration`, `evaluate`, `main`

## Env-key candidates

`BLOCK`, `FAIL`, `INFO`, `NOT_READY`, `PAS166`, `PASS`, `READY`

## String constants (redacted where noted)

- '\nPAS166 — Durable email dedupe + signature-required policy\nreadiness gate.\n\nDeterministic, non-mutating evaluator for "is the PAS166\ndurable email-dedupe + signature-required policy layer wired\ncorrectly, structurally safe, and free of regression vs\nPAS164 / PAS165 doctrine?".\n\nWalks the repo and verifies:\n\n  * scripts/migrate_v15_email_dedupe.sql exists as a proposal\n    (NOT executed in PAS166);\n  * the SQL declares the required columns + closed source\n    enum + RLS + tenant write-denial;\n  * the SQL declares NO raw body / subject / sender / phone /\n    email columns;\n  * app/services/ingestion/email_dedupe_store.py exists and\n    exports the required helpers;\n  * the durable store has no DB exception escape and surfaces\n    ``durable_email_dedupe_unavailable`` on failure;\n  * the dedupe store NEVER reads brokerage_id from a payload;\n  * the email-ingestion service exposes the new kwargs +\n    response fields (``forwarder_required``,\n    ``dedupe_durable``);\n  * the signature-required policy helper is strict-literal-True\n    (the helper never matches a string ``"true"`` / int ``1``);\n  * the route exposes the new fields and reads the brokerage\n    row only as the source of truth for the required flag;\n  * the event allow-list excludes phone / email / name /\n    subject / sender / body / signature / dedupe_key / secret /\n    raw_email / raw_body / property_address / notes /\n    transcript;\n  * no Gmail / Google / IMAP / POP3 / inbox-scan tokens;\n  * no embedding / vector / vendor imports;\n  * Memory Review UI files are intact;\n  * prior-phase readiness scripts (PAS160 / PAS161 / PAS162 /\n    PAS163 / PAS164 / PAS165) still exist;\n  * supports --summary-only and --json;\n  * exits 0 ready, 1 blockers, 2 bad args;\n  * never reads .env;\n  * never touches production data.\n\nUsage:\n  python scripts/pas166_email_dedupe_policy_readiness_check.py\n  python scripts/pas166_email_dedupe_policy_readiness_check.py --json\n  python scripts/pas166_email_dedupe_policy_readiness_check.py --summary-only\n  python scripts/pas166_email_dedupe_policy_readiness_check.py --strict\n\nExit codes:\n    0  — READY  (verdict == READY)\n    1  — NOT_READY\n    2  — bad CLI arguments\n'
- 'utf-8'
- 'READY'
- 'NOT_READY'
- 'BLOCK'
- 'INFO'
- 'severity'
- 'detail'
- 'pas166_email_dedupe_policy_readiness_report.json'
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
- 'Strip ``-- ...`` SQL line comments. Preserves block-\nquoted text unchanged.'
- 'repo_root'
- 'List[dict]'
- 'file:'
- 'PASS'
- 'FAIL'
- 'Required PAS166 file present: '
- 'missing'
- 'prior_phase:'
- 'Prior-phase readiness script intact: '
- 'missing — PAS166 must not delete'
- 'memory_review_file:'
- 'Memory Review file present (PAS166 must not delete): '
- 'PAS166 must not delete Memory Review files'
- 'scripts'
- 'migrate_v15_email_dedupe.sql'
- 'pas_email_dedupe_keys'
- 'migration:table_name'
- 'Migration declares pas_email_dedupe_keys'
- 'table not declared'
- 'migration:col:'
- 'Migration declares column '
- 'column '
- ' missing'
- 'migration:source_enum:'
- 'Migration source enum carries '
- 'source enum missing '
- 'row level security'
- 'row-level security'
- 'migration:rls_enabled'
- 'Migration enables row-level security'
- 'ALTER TABLE ... ENABLE ROW LEVEL SECURITY missing'
- 'tenant_no_insert'
- 'tenant_no_update'
- 'tenant_no_delete'
- 'migration:tenant_write_denied'
- 'Migration explicitly denies tenant INSERT/UPDATE/DELETE'
- 'tenant write-denial policy missing'
- 'proposal only'
- 'migration:proposal_only'
- "Migration carries 'PROPOSAL ONLY' guardrail"
- "missing 'PROPOSAL ONLY' label"
- 'do not execute'
- 'migration:do_not_execute'
- "Migration carries 'DO NOT EXECUTE' trailer"
- "missing 'DO NOT EXECUTE' trailer"
- 'migration:no_identifying_columns'
- 'Migration declares no raw / identifying columns'
- 'forbidden column tokens present: '
- 'brokerage_id, expires_at'
- 'brokerage_id, source, created_at'
- 'migration:tenant_leading_index'
- 'Migration creates tenant-leading index'
- 'expected (brokerage_id, ...) index'
- 'app'
- 'services'
- 'ingestion'
- 'email_dedupe_store.py'
- 'store_fn:'
- 'Dedupe store function present: '
- 'missing def: '
- 'durable_email_dedupe_unavailable'
- 'store:soft_fail_token'
- 'Dedupe store surfaces durable_email_dedupe_unavailable'
- 'structural soft-fail token missing'
- 'missing_brokerage_id'
- 'store:requires_brokerage_id'
- 'Dedupe store rejects calls without brokerage_id'
- 'missing_brokerage_id token not found'
- 'store:no_forbidden_response_key:'
- 'Dedupe store excludes forbidden response key: '
- 'forbidden response key '
- ' present'
- '_MIN_TTL_HOURS'
- '_MAX_TTL_HOURS'
- '168'
- 'store:ttl_bounds_1_168'
- 'Dedupe store clamps TTL to [1, 168] hours'
- 'expected _MIN_TTL_HOURS / _MAX_TTL_HOURS 1..168'
- 'email_ingestion.py'
- 'service_token:'
- 'Service references '
- 'missing token '
- 'brokerage:'
- 'brokerage='
- 'service:accepts_brokerage_kwarg'
- 'Service accepts brokerage kwarg'
- 'service does not accept brokerage kwarg'
- 'service:response_field:'
- 'Service response includes field: '
- 'missing response key '
- 'register_email_lead_dedupe'
- 'service:process_local_fallback_present'
- 'Service retains PAS165 process-local dedupe fallback'
- 'process-local fallback not referenced'
- 'is True'
- 'email_forwarder_signature_required'
- 'service:strict_literal_true_policy'
- "Signature-required policy uses 'is True' (strict literal)"
- "expected an 'is True' comparison in the required-policy helper"
- 'service:no_forbidden_response_key:'
- 'Service excludes forbidden response key: '
- 'routes'
- 'route_decl:'
- 'Route declaration present: '
- 'missing decl: '
- 'brokerage=brokerage'
- 'route:passes_brokerage_row'
- 'Route passes full brokerage row to ingest_email_lead'
- 'missing brokerage=brokerage kwarg'
- 'route:no_body_trust:'
- 'Route never reads brokerage_id from body: '
- 'body-trust pattern '
- '_EVENT_PAYLOAD_ALLOWED'
- 'route:event_allowlist_excludes:'
- 'Event payload allow-list excludes forbidden key: '
- 'forbidden allow-list key '
- 'events'
- 'contract.py'
- 'events:'
- 'Event contract registers '
- 'missing event type '
- 'app/services/ingestion/email_dedupe_store.py'
- 'forbidden_import:'
- 'No forbidden imports: '
- 'forbidden import prefixes: '
- 'no_inbox_scan:'
- 'No inbox-scanning tokens: '
- 'inbox-scan tokens present: '
- 'docs'
- 'pas166_durable_email_dedupe_and_signature_policy.md'
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
- 'PAS166 readiness checker never reads .env, calls Supabase, or imports vendor / Google / embedding libs'
- 'disqualifying code-line patterns: '
- 'checks'
- 'verdict'
- 'blockers'
- 'info'
- 'List[str]'
- ' — '
- 'see report'
- 'phase'
- 'PAS166'
- 'generated_at'
- 'ready'
- 'blocker_count'
- 'info_count'
- 'check_count'
- 'pass_count'
- 'fail_count'
- 'operator_actions'
- 'argparse.ArgumentParser'
- 'pas166_email_dedupe_policy_readiness_check'
- 'PAS166 — Evaluate the durable email dedupe + signature-required policy layer for structural correctness, no-Gmail-OAuth doctrine, no inbox scanning, no raw-body / signature / dedupe-key / secret leakage. Read-only. Does not touch Supabase, .env, or any tenant data.'
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
- '[PAS166] verdict='
- ' blockers='
- ' info='
- ' checks='
- ' pass='
- ' fail='
- '[PAS166] operator actions:'
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

   1           LOAD_CONST               0 ('\nPAS166 — Durable email dedupe + signature-required policy\nreadiness gate.\n\nDeterministic, non-mutating evaluator for "is the PAS166\ndurable email-dedupe + signature-required policy layer wired\ncorrectly, structurally safe, and free of regression vs\nPAS164 / PAS165 doctrine?".\n\nWalks the repo and verifies:\n\n  * scripts/migrate_v15_email_dedupe.sql exists as a proposal\n    (NOT executed in PAS166);\n  * the SQL declares the required columns + closed source\n    enum + RLS + tenant write-denial;\n  * the SQL declares NO raw body / subject / sender / phone /\n    email columns;\n  * app/services/ingestion/email_dedupe_store.py exists and\n    exports the required helpers;\n  * the durable store has no DB exception escape and surfaces\n    ``durable_email_dedupe_unavailable`` on failure;\n  * the dedupe store NEVER reads brokerage_id from a payload;\n  * the email-ingestion service exposes the new kwargs +\n    response fields (``forwarder_required``,\n    ``dedupe_durable``);\n  * the signature-required policy helper is strict-literal-True\n    (the helper never matches a string ``"true"`` / int ``1``);\n  * the route exposes the new fields and reads the brokerage\n    row only as the source of truth for the required flag;\n  * the event allow-list excludes phone / email / name /\n    subject / sender / body / signature / dedupe_key / secret /\n    raw_email / raw_body / property_address / notes /\n    transcript;\n  * no Gmail / Google / IMAP / POP3 / inbox-scan tokens;\n  * no embedding / vector / vendor imports;\n  * Memory Review UI files are intact;\n  * prior-phase readiness scripts (PAS160 / PAS161 / PAS162 /\n    PAS163 / PAS164 / PAS165) still exist;\n  * supports --summary-only and --json;\n  * exits 0 ready, 1 blockers, 2 bad args;\n  * never reads .env;\n  * never touches production data.\n\nUsage:\n  python scripts/pas166_email_dedupe_policy_readiness_check.py\n  python scripts/pas166_email_dedupe_policy_readiness_check.py --json\n  python scripts/pas166_email_dedupe_policy_readiness_check.py --summary-only\n  python scripts/pas166_email_dedupe_policy_readiness_check.py --strict\n\nExit codes:\n    0  — READY  (verdict == READY)\n    1  — NOT_READY\n    2  — bad CLI arguments\n')
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

  90           LOAD_CONST              66 (('scripts/migrate_v15_email_dedupe.sql', 'app/services/ingestion/email_dedupe_store.py', 'app/services/ingestion/email_ingestion.py', 'app/routes/email_ingestion.py', 'scripts/pas166_email_dedupe_policy_readiness_check.py', 'docs/pas166_durable_email_dedupe_and_signature_policy.md', 'tests/mvp/test_pas166_email_dedupe_policy.py'))
               STORE_NAME              29 (REQUIRED_FILES)

 100           LOAD_CONST              67 (('scripts/pas160_mvp_sequence_check.py', 'scripts/pas161_lead_ingestion_readiness_check.py', 'scripts/pas162_pending_calls_readiness_check.py', 'scripts/pas163_candidate_pipeline_readiness_check.py', 'scripts/pas164_email_ingestion_readiness_check.py', 'scripts/pas165_email_auth_dedupe_readiness_check.py'))
               STORE_NAME              30 (PRIOR_PHASE_FILES)

 110           LOAD_CONST              68 (('app/services/memory/review.py', 'app/services/memory/review_stats.py', 'app/services/memory/review_export.py', 'app/services/memory/review_actors.py', 'app/services/memory/review_alerts.py', 'app/services/memory/operator_console.py'))
               STORE_NAME              31 (MEMORY_REVIEW_FILES)

 120           LOAD_CONST              69 (('def durable_email_dedupe_enabled(', 'def register_email_dedupe_key(', 'def is_duplicate_email_dedupe_key(', 'def mark_email_duplicate_seen('))
               STORE_NAME              32 (REQUIRED_STORE_FUNCTIONS)

 128           LOAD_CONST              70 (('forwarder_required', 'dedupe_durable', 'email_forwarder_signature_required', 'register_email_dedupe_key', 'register_email_lead_dedupe'))
               STORE_NAME              33 (REQUIRED_SERVICE_TOKENS)

 136           LOAD_CONST              71 (('forwarder_required', 'dedupe_durable'))
               STORE_NAME              34 (REQUIRED_RESPONSE_FIELDS)

 141           LOAD_CONST              72 (('@router.post("/parse")', '@router.post("/ingest")'))
               STORE_NAME              35 (REQUIRED_ROUTE_DECLS)

 147           LOAD_CONST              73 (('email.dedupe.durable_registered', 'email.dedupe.durable_duplicate', 'email.dedupe.fallback_process_local', 'email.forwarder.signature_required_missing', 'email.forwarder.secret_missing'))
               STORE_NAME              36 (REQUIRED_EVENT_TYPES)

 156           LOAD_CONST              74 (('dedupe_key', 'brokerage_id', 'source', 'created_at', 'expires_at', 'first_seen_pending_call_id', 'duplicate_count', 'last_duplicate_at'))
               STORE_NAME              37 (REQUIRED_SQL_COLUMNS)

 168           LOAD_CONST              75 (('zillow', 'realtor', 'facebook', 'website', 'generic_email', 'manual'))
               STORE_NAME              38 (REQUIRED_SQL_SOURCE_VALUES)

 176           LOAD_CONST              76 ((' phone ', ' phone\n', 'lead_phone', ' email ', ' email\n', 'lead_email', ' name ', ' name\n', 'lead_name', 'subject ', 'subject\n', 'sender ', 'sender\n', ' body ', ' body\n', 'raw_body', 'raw_email', 'property_address', ' notes ', ' notes\n', 'transcript'))
               STORE_NAME              39 (FORBIDDEN_SQL_COLUMN_TOKENS)

 190           LOAD_CONST              77 (('raw_email', 'raw_body', 'full_email', 'raw_payload', 'transcript'))
               STORE_NAME              40 (FORBIDDEN_RESPONSE_KEYS)

 200           LOAD_CONST              78 (('phone', 'email', 'name', 'subject', 'sender', 'body', 'signature', 'dedupe_key', 'secret', 'raw_email', 'raw_body', 'property_address', 'notes', 'transcript'))
               STORE_NAME              41 (FORBIDDEN_EVENT_PAYLOAD_KEYS)

 218           LOAD_CONST              79 (('import googleapiclient', 'from googleapiclient', 'import google.oauth2', 'from google.oauth2', 'from google.auth', 'import google.auth', 'from google_auth_oauthlib', 'import composio', 'from composio', 'import trustclaw', 'from trustclaw', 'import openai', 'from openai', 'import anthropic', 'from anthropic', 'import numpy', 'import faiss', 'import pgvector', 'from pgvector', 'from openai import embeddings', 'from openai.embeddings', 'from app.services.memory', 'import app.services.memory', 'import imaplib', 'from imaplib', 'import poplib', 'from poplib'))
               STORE_NAME              42 (FORBIDDEN_IMPORT_LINE_PREFIXES)

 248           LOAD_CONST              80 (('imaplib', 'poplib', 'fetch_inbox', 'gmail_oauth', 'gmail_token', 'users().messages'))
               STORE_NAME              43 (FORBIDDEN_INBOX_TOKENS)

 262           LOAD_CONST              13 ('severity')

 264           LOAD_NAME               27 (SEVERITY_BLOCK)

 262           LOAD_CONST              14 ('detail')

 264           LOAD_CONST              15 ('')

 262           BUILD_MAP                2
               LOAD_CONST              16 (<code object __annotate__ at 0x0000018C18026230, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 262>)
               MAKE_FUNCTION
               LOAD_CONST              17 (<code object _check at 0x0000018C17FA2F10, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 262>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              44 (_check)

 275           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA34B0, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 275>)
               MAKE_FUNCTION
               LOAD_CONST              19 (<code object _now_iso at 0x0000018C18038F30, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 275>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              45 (_now_iso)

 279           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA3B40, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 279>)
               MAKE_FUNCTION
               LOAD_CONST              21 (<code object _read_text at 0x0000018C18053510, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 279>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              46 (_read_text)

 286           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA2970, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 286>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object _strip_python_comments_and_strings at 0x0000018C17D52150, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 286>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              47 (_strip_python_comments_and_strings)

 321           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA33C0, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 321>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object _strip_sql_comments at 0x0000018C17FA92F0, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 321>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              48 (_strip_sql_comments)

 337           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA35A0, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 337>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object check_files_present at 0x0000018C180608A0, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 337>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              49 (check_files_present)

 351           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA3D20, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 351>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object check_prior_phases_intact at 0x0000018C18060A50, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 351>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              50 (check_prior_phases_intact)

 365           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA1D40, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 365>)
               MAKE_FUNCTION
               LOAD_CONST              31 (<code object check_memory_review_intact at 0x0000018C18060C00, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 365>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              51 (check_memory_review_intact)

 379           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA2880, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 379>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object check_migration_proposal at 0x0000018C17F79D20, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 379>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              52 (check_migration_proposal)

 480           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA2100, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 480>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object check_dedupe_store at 0x0000018C17ED93C0, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 480>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              53 (check_dedupe_store)

 539           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C17FA2B50, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 539>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object check_service_integration at 0x0000018C17F7A440, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 539>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              54 (check_service_integration)

 613           LOAD_CONST              38 (<code object __annotate__ at 0x0000018C17FA32D0, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 613>)
               MAKE_FUNCTION
               LOAD_CONST              39 (<code object check_route_integration at 0x0000018C17E95410, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 613>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              55 (check_route_integration)

 668           LOAD_CONST              40 (<code object __annotate__ at 0x0000018C17FA3780, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 668>)
               MAKE_FUNCTION
               LOAD_CONST              41 (<code object check_event_contract at 0x0000018C17FEDA30, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 668>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              56 (check_event_contract)

 684           LOAD_CONST              42 (<code object __annotate__ at 0x0000018C17FA1E30, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 684>)
               MAKE_FUNCTION
               LOAD_CONST              43 (<code object check_no_forbidden_imports at 0x0000018C17D8B970, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 684>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              57 (check_no_forbidden_imports)

 712           LOAD_CONST              44 (<code object __annotate__ at 0x0000018C17FA2E20, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 712>)
               MAKE_FUNCTION
               LOAD_CONST              45 (<code object check_no_inbox_scanning at 0x0000018C17CC2460, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 712>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              58 (check_no_inbox_scanning)

 738           LOAD_CONST              46 (<code object __annotate__ at 0x0000018C17FA21F0, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 738>)
               MAKE_FUNCTION
               LOAD_CONST              47 (<code object check_docs_required_doctrine at 0x0000018C17F739B0, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 738>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              59 (check_docs_required_doctrine)

 781           LOAD_CONST              48 (<code object __annotate__ at 0x0000018C17FA26A0, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 781>)
               MAKE_FUNCTION
               LOAD_CONST              49 (<code object check_self_no_env_or_vendor at 0x0000018C17F699C0, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 781>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              60 (check_self_no_env_or_vendor)

 831           LOAD_CONST              50 (<code object __annotate__ at 0x0000018C17FA2790, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 831>)
               MAKE_FUNCTION
               LOAD_CONST              51 (<code object _aggregate at 0x0000018C17EC4280, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 831>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              61 (_aggregate)

 847           LOAD_CONST              52 (<code object __annotate__ at 0x0000018C180FC030, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 847>)
               MAKE_FUNCTION
               LOAD_CONST              53 (<code object _operator_actions at 0x0000018C18048C70, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 847>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              62 (_operator_actions)

 857           LOAD_CONST              54 (<code object __annotate__ at 0x0000018C180FC6C0, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 857>)
               MAKE_FUNCTION
               LOAD_CONST              55 (<code object evaluate at 0x0000018C17F69E40, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 857>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              63 (evaluate)

 888           LOAD_CONST              56 ('pas166_email_dedupe_policy_readiness_report.json')
               STORE_NAME              64 (REPORT_FILENAME)

 891           LOAD_CONST              57 (<code object __annotate__ at 0x0000018C180FC7B0, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 891>)
               MAKE_FUNCTION
               LOAD_CONST              58 (<code object _build_parser at 0x0000018C1801CDC0, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 891>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              65 (_build_parser)

 926           LOAD_CONST              59 (<code object __annotate__ at 0x0000018C180FC8A0, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 926>)
               MAKE_FUNCTION
               LOAD_CONST              60 (<code object _print_summary at 0x0000018C17D8C5C0, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 926>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              66 (_print_summary)

 944           LOAD_CONST              61 (<code object __annotate__ at 0x0000018C18025530, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 944>)
               MAKE_FUNCTION
               LOAD_CONST              62 (<code object _write_report at 0x0000018C18104030, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 944>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              67 (_write_report)

 958           LOAD_CONST              81 ((None,))
               LOAD_CONST              63 (<code object __annotate__ at 0x0000018C180FC990, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 958>)
               MAKE_FUNCTION
               LOAD_CONST              64 (<code object main at 0x0000018C17F84690, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 958>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              68 (main)

 986           LOAD_NAME               69 (__name__)
               LOAD_CONST              65 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 987           LOAD_NAME                6 (sys)
               LOAD_ATTR              140 (exit)
               PUSH_NULL
               LOAD_NAME               68 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 986   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  70           LOAD_NAME               18 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  71   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          341 (to L1)

  70   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026230, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 262>:
262           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('check_id')

263           LOAD_CONST               2 ('str')

262           LOAD_CONST               3 ('status')

263           LOAD_CONST               2 ('str')

262           LOAD_CONST               4 ('label')

263           LOAD_CONST               2 ('str')

262           LOAD_CONST               5 ('severity')

264           LOAD_CONST               2 ('str')

262           LOAD_CONST               6 ('detail')

264           LOAD_CONST               2 ('str')

262           LOAD_CONST               7 ('return')

265           LOAD_CONST               8 ('dict')

262           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _check at 0x0000018C17FA2F10, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 262>:
262           RESUME                   0

267           LOAD_CONST               0 ('id')
              LOAD_FAST_BORROW         0 (check_id)

268           LOAD_CONST               1 ('status')
              LOAD_FAST_BORROW         1 (status)

269           LOAD_CONST               2 ('label')
              LOAD_FAST_BORROW         2 (label)

270           LOAD_CONST               3 ('severity')
              LOAD_FAST_BORROW         3 (severity)

271           LOAD_CONST               4 ('detail')
              LOAD_FAST_BORROW         4 (detail)

266           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 275>:
275           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038F30, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 275>:
275           RESUME                   0

276           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 279>:
279           RESUME                   0
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

Disassembly of <code object _read_text at 0x0000018C18053510, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 279>:
 279           RESUME                   0

 280           NOP

 281   L1:     LOAD_FAST_BORROW         0 (path)
               LOAD_ATTR                1 (read_text + NULL|self)
               LOAD_CONST               0 ('utf-8')
               LOAD_CONST               1 ('replace')
               LOAD_CONST               2 (('encoding', 'errors'))
               CALL_KW                  2
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 282           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 283   L4:     POP_EXCEPT
               LOAD_CONST               3 (None)
               RETURN_VALUE

 282   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 286>:
286           RESUME                   0
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

Disassembly of <code object _strip_python_comments_and_strings at 0x0000018C17D52150, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 286>:
286            RESUME                   0

287            BUILD_LIST               0
               STORE_FAST               1 (out)

288            LOAD_SMALL_INT           0
               LOAD_GLOBAL              1 (len + NULL)
               LOAD_FAST_BORROW         0 (src)
               CALL                     1
               STORE_FAST_STORE_FAST   50 (n, i)

289    L1:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (i, n)
               COMPARE_OP              18 (bool(<))
               EXTENDED_ARG             1
               POP_JUMP_IF_FALSE      282 (to L13)
               NOT_TAKEN

290            LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               BINARY_OP               26 ([])
               STORE_FAST               4 (ch)

291            LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               1 ('#')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       38 (to L3)
               NOT_TAKEN

292            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_CONST               2 ('\n')
               LOAD_FAST_BORROW         2 (i)
               CALL                     2
               STORE_FAST               5 (j)

293            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L2)
               NOT_TAKEN

294            JUMP_FORWARD           240 (to L13)

295    L2:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

296            JUMP_BACKWARD           59 (to L1)

297    L3:     LOAD_FAST_BORROW         0 (src)
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

298    L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               BINARY_SLICE
               STORE_FAST               6 (quote)

299            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 98 (quote, i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               CALL                     2
               STORE_FAST               7 (end)

300            LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L5)
               NOT_TAKEN

301            JUMP_FORWARD           138 (to L13)

302    L5:     LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

303            JUMP_BACKWARD          161 (to L1)

304    L6:     LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               7 (('"', "'"))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       92 (to L12)
               NOT_TAKEN

305            LOAD_FAST                4 (ch)
               STORE_FAST               6 (quote)

306            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               5 (j)

307    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (j, n)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       63 (to L11)
               NOT_TAKEN

308            LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
               BINARY_OP               26 ([])
               LOAD_CONST               5 ('\\')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       12 (to L8)
               NOT_TAKEN

309            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           2
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)

310            JUMP_BACKWARD           30 (to L7)

311    L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
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

312    L9:     JUMP_FORWARD            11 (to L11)

313   L10:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)
               JUMP_BACKWARD           68 (to L7)

314   L11:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

315            EXTENDED_ARG             1
               JUMP_BACKWARD          259 (to L1)

316   L12:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (ch)
               CALL                     1
               POP_TOP

317            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               2 (i)
               EXTENDED_ARG             1
               JUMP_BACKWARD          288 (to L1)

318   L13:     LOAD_CONST               6 ('')
               LOAD_ATTR                9 (join + NULL|self)
               LOAD_FAST_BORROW         1 (out)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 321>:
321           RESUME                   0
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

Disassembly of <code object _strip_sql_comments at 0x0000018C17FA92F0, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 321>:
321           RESUME                   0

324           BUILD_LIST               0
              STORE_FAST               1 (out)

325           LOAD_FAST_BORROW         0 (src)
              LOAD_ATTR                1 (splitlines + NULL|self)
              CALL                     0
              GET_ITER
      L1:     FOR_ITER                49 (to L3)
              STORE_FAST               2 (line)

326           LOAD_FAST_BORROW         2 (line)
              LOAD_ATTR                3 (find + NULL|self)
              LOAD_CONST               1 ('--')
              CALL                     1
              STORE_FAST               3 (idx)

327           LOAD_FAST_BORROW         3 (idx)
              LOAD_SMALL_INT           0
              COMPARE_OP             188 (bool(>=))
              POP_JUMP_IF_FALSE        6 (to L2)
              NOT_TAKEN

328           LOAD_FAST_BORROW         2 (line)
              LOAD_CONST               2 (None)
              LOAD_FAST_BORROW         3 (idx)
              BINARY_SLICE
              STORE_FAST               2 (line)

329   L2:     LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_FAST_BORROW         2 (line)
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           51 (to L1)

325   L3:     END_FOR
              POP_ITER

330           LOAD_CONST               3 ('\n')
              LOAD_ATTR                7 (join + NULL|self)
              LOAD_FAST_BORROW         1 (out)
              CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 337>:
337           RESUME                   0
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

Disassembly of <code object check_files_present at 0x0000018C180608A0, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 337>:
337           RESUME                   0

338           BUILD_LIST               0
              STORE_FAST               1 (out)

339           LOAD_GLOBAL              0 (REQUIRED_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

340           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

341           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

342           LOAD_CONST               0 ('file:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

343           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

344   L3:     LOAD_CONST               3 ('Required PAS166 file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

345           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

346           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing')

341   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

339   L6:     END_FOR
              POP_ITER

348           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3D20, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 351>:
351           RESUME                   0
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

Disassembly of <code object check_prior_phases_intact at 0x0000018C18060A50, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 351>:
351           RESUME                   0

352           BUILD_LIST               0
              STORE_FAST               1 (out)

353           LOAD_GLOBAL              0 (PRIOR_PHASE_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

354           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

355           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

356           LOAD_CONST               0 ('prior_phase:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

357           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

358   L3:     LOAD_CONST               3 ('Prior-phase readiness script intact: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

359           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

360           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing — PAS166 must not delete')

355   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

353   L6:     END_FOR
              POP_ITER

362           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1D40, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 365>:
365           RESUME                   0
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

Disassembly of <code object check_memory_review_intact at 0x0000018C18060C00, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 365>:
365           RESUME                   0

366           BUILD_LIST               0
              STORE_FAST               1 (out)

367           LOAD_GLOBAL              0 (MEMORY_REVIEW_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

368           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

369           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

370           LOAD_CONST               0 ('memory_review_file:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

371           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

372   L3:     LOAD_CONST               3 ('Memory Review file present (PAS166 must not delete): ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

373           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

374           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('PAS166 must not delete Memory Review files')

369   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

367   L6:     END_FOR
              POP_ITER

376           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 379>:
379           RESUME                   0
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

Disassembly of <code object check_migration_proposal at 0x0000018C17F79D20, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 379>:
379            RESUME                   0

380            BUILD_LIST               0
               STORE_FAST               1 (out)

381            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('scripts')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('migrate_v15_email_dedupe.sql')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

382            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               2 ('')
       L1:     STORE_FAST               3 (src)

383            LOAD_FAST_BORROW         3 (src)
               LOAD_ATTR                5 (lower + NULL|self)
               CALL                     0
               STORE_FAST               4 (lower)

385            LOAD_CONST               3 ('pas_email_dedupe_keys')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (table_present)

386            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

387            LOAD_CONST               4 ('migration:table_name')

388            LOAD_FAST_BORROW         5 (table_present)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L2)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L3)
       L2:     LOAD_CONST               6 ('FAIL')

389    L3:     LOAD_CONST               7 ('Migration declares pas_email_dedupe_keys')

390            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

391            LOAD_FAST_BORROW         5 (table_present)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L5)
       L4:     LOAD_CONST               8 ('table not declared')

386    L5:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

394            LOAD_GLOBAL             12 (REQUIRED_SQL_COLUMNS)
               GET_ITER
       L6:     FOR_ITER                72 (to L11)
               STORE_FAST               6 (col)

395            LOAD_FAST_BORROW_LOAD_FAST_BORROW 100 (col, lower)
               CONTAINS_OP              0 (in)
               STORE_FAST               7 (ok)

396            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

397            LOAD_CONST              10 ('migration:col:')
               LOAD_FAST_BORROW         6 (col)
               FORMAT_SIMPLE
               BUILD_STRING             2

398            LOAD_FAST_BORROW         7 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L7)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L8)
       L7:     LOAD_CONST               6 ('FAIL')

399    L8:     LOAD_CONST              11 ('Migration declares column ')
               LOAD_FAST_BORROW         6 (col)
               FORMAT_SIMPLE
               BUILD_STRING             2

400            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

401            LOAD_FAST_BORROW         7 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             5 (to L10)
       L9:     LOAD_CONST              12 ('column ')
               LOAD_FAST_BORROW         6 (col)
               FORMAT_SIMPLE
               LOAD_CONST              13 (' missing')
               BUILD_STRING             3

396   L10:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           74 (to L6)

394   L11:     END_FOR
               POP_ITER

404            LOAD_GLOBAL             14 (REQUIRED_SQL_SOURCE_VALUES)
               GET_ITER
      L12:     FOR_ITER                71 (to L17)
               STORE_FAST               8 (val)

405            LOAD_FAST_BORROW_LOAD_FAST_BORROW 132 (val, lower)
               CONTAINS_OP              0 (in)
               STORE_FAST               7 (ok)

406            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

407            LOAD_CONST              14 ('migration:source_enum:')
               LOAD_FAST_BORROW         8 (val)
               FORMAT_SIMPLE
               BUILD_STRING             2

408            LOAD_FAST_BORROW         7 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L13)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L14)
      L13:     LOAD_CONST               6 ('FAIL')

409   L14:     LOAD_CONST              15 ('Migration source enum carries ')
               LOAD_FAST_BORROW         8 (val)
               FORMAT_SIMPLE
               BUILD_STRING             2

410            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

411            LOAD_FAST_BORROW         7 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L15)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             4 (to L16)
      L15:     LOAD_CONST              16 ('source enum missing ')
               LOAD_FAST_BORROW         8 (val)
               FORMAT_SIMPLE
               BUILD_STRING             2

406   L16:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           73 (to L12)

404   L17:     END_FOR
               POP_ITER

414            LOAD_CONST              17 ('row level security')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L18)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              18 ('row-level security')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)
      L18:     STORE_FAST               9 (rls_ok)

415            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

416            LOAD_CONST              19 ('migration:rls_enabled')

417            LOAD_FAST_BORROW         9 (rls_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L19)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L20)
      L19:     LOAD_CONST               6 ('FAIL')

418   L20:     LOAD_CONST              20 ('Migration enables row-level security')

419            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

420            LOAD_FAST_BORROW         9 (rls_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L21)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L22)
      L21:     LOAD_CONST              21 ('ALTER TABLE ... ENABLE ROW LEVEL SECURITY missing')

415   L22:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

423            LOAD_CONST              22 ('tenant_no_insert')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       19 (to L23)
               NOT_TAKEN
               POP_TOP

424            LOAD_CONST              23 ('tenant_no_update')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)

423            COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        6 (to L23)
               NOT_TAKEN
               POP_TOP

425            LOAD_CONST              24 ('tenant_no_delete')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)

422   L23:     STORE_FAST              10 (write_denied)

427            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

428            LOAD_CONST              25 ('migration:tenant_write_denied')

429            LOAD_FAST_BORROW        10 (write_denied)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L24)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L25)
      L24:     LOAD_CONST               6 ('FAIL')

430   L25:     LOAD_CONST              26 ('Migration explicitly denies tenant INSERT/UPDATE/DELETE')

431            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

432            LOAD_FAST_BORROW        10 (write_denied)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L26)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L27)
      L26:     LOAD_CONST              27 ('tenant write-denial policy missing')

427   L27:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

435            LOAD_CONST              28 ('proposal only')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)
               STORE_FAST              11 (proposal_ok)

436            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

437            LOAD_CONST              29 ('migration:proposal_only')

438            LOAD_FAST_BORROW        11 (proposal_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L28)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L29)
      L28:     LOAD_CONST               6 ('FAIL')

439   L29:     LOAD_CONST              30 ("Migration carries 'PROPOSAL ONLY' guardrail")

440            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

441            LOAD_FAST_BORROW        11 (proposal_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L30)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L31)
      L30:     LOAD_CONST              31 ("missing 'PROPOSAL ONLY' label")

436   L31:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

443            LOAD_CONST              32 ('do not execute')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)
               STORE_FAST              12 (do_not_exec)

444            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

445            LOAD_CONST              33 ('migration:do_not_execute')

446            LOAD_FAST_BORROW        12 (do_not_exec)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L32)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L33)
      L32:     LOAD_CONST               6 ('FAIL')

447   L33:     LOAD_CONST              34 ("Migration carries 'DO NOT EXECUTE' trailer")

448            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

449            LOAD_FAST_BORROW        12 (do_not_exec)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L34)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L35)
      L34:     LOAD_CONST              35 ("missing 'DO NOT EXECUTE' trailer")

444   L35:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

452            LOAD_GLOBAL             17 (_strip_sql_comments + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               LOAD_ATTR                5 (lower + NULL|self)
               CALL                     0
               STORE_FAST              13 (stripped)

453            BUILD_LIST               0
               STORE_FAST              14 (bad)

454            LOAD_GLOBAL             18 (FORBIDDEN_SQL_COLUMN_TOKENS)
               GET_ITER
      L36:     FOR_ITER                42 (to L38)
               STORE_FAST              15 (token)

455            LOAD_FAST_BORROW_LOAD_FAST_BORROW 253 (token, stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L37)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L36)

456   L37:     LOAD_FAST_BORROW        14 (bad)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW        15 (token)
               LOAD_ATTR               21 (strip + NULL|self)
               CALL                     0
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           44 (to L36)

454   L38:     END_FOR
               POP_ITER

457            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

458            LOAD_CONST              36 ('migration:no_identifying_columns')

459            LOAD_FAST_BORROW        14 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L39)
               NOT_TAKEN
               LOAD_CONST               6 ('FAIL')
               JUMP_FORWARD             1 (to L40)
      L39:     LOAD_CONST               5 ('PASS')

460   L40:     LOAD_CONST              37 ('Migration declares no raw / identifying columns')

461            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

463            LOAD_FAST_BORROW        14 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L41)
               NOT_TAKEN

462            LOAD_CONST              38 ('forbidden column tokens present: ')
               LOAD_CONST              39 (', ')
               LOAD_ATTR               23 (join + NULL|self)
               LOAD_FAST_BORROW        14 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L42)

463   L41:     LOAD_CONST               2 ('')

457   L42:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

467            LOAD_CONST              40 ('brokerage_id, expires_at')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L43)
               NOT_TAKEN
               POP_TOP

468            LOAD_CONST              41 ('brokerage_id, source, created_at')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)

466   L43:     STORE_FAST              16 (tenant_idx)

470            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

471            LOAD_CONST              42 ('migration:tenant_leading_index')

472            LOAD_FAST_BORROW        16 (tenant_idx)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L44)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L45)
      L44:     LOAD_CONST               6 ('FAIL')

473   L45:     LOAD_CONST              43 ('Migration creates tenant-leading index')

474            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

475            LOAD_FAST_BORROW        16 (tenant_idx)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L46)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L47)
      L46:     LOAD_CONST              44 ('expected (brokerage_id, ...) index')

470   L47:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

477            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 480>:
480           RESUME                   0
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

Disassembly of <code object check_dedupe_store at 0x0000018C17ED93C0, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 480>:
  --            MAKE_CELL               11 (src)

 480            RESUME                   0

 481            BUILD_LIST               0
                STORE_FAST               1 (out)

 482            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('app')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('services')
                BINARY_OP               11 (/)
                LOAD_CONST               2 ('ingestion')
                BINARY_OP               11 (/)
                LOAD_CONST               3 ('email_dedupe_store.py')
                BINARY_OP               11 (/)
                STORE_FAST               2 (p)

 483            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (p)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               4 ('')
        L1:     STORE_DEREF             11 (src)

 484            LOAD_GLOBAL              4 (REQUIRED_STORE_FUNCTIONS)
                GET_ITER
        L2:     FOR_ITER                93 (to L7)
                STORE_FAST               3 (needle)

 485            LOAD_FAST_BORROW         3 (needle)
                LOAD_DEREF              11 (src)
                CONTAINS_OP              0 (in)
                STORE_FAST               4 (ok)

 486            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 487            LOAD_CONST               5 ('store_fn:')
                LOAD_FAST_BORROW         3 (needle)
                LOAD_CONST               6 (slice(None, 40, None))
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                BUILD_STRING             2

 488            LOAD_FAST_BORROW         4 (ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L3)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L4)
        L3:     LOAD_CONST               8 ('FAIL')

 489    L4:     LOAD_CONST               9 ('Dedupe store function present: ')
                LOAD_FAST_BORROW         3 (needle)
                LOAD_ATTR               11 (strip + NULL|self)
                CALL                     0
                FORMAT_SIMPLE
                BUILD_STRING             2

 490            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 491            LOAD_FAST_BORROW         4 (ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN
                LOAD_CONST               4 ('')
                JUMP_FORWARD             4 (to L6)
        L5:     LOAD_CONST              10 ('missing def: ')
                LOAD_FAST_BORROW         3 (needle)
                FORMAT_SIMPLE
                BUILD_STRING             2

 486    L6:     LOAD_CONST              11 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           95 (to L2)

 484    L7:     END_FOR
                POP_ITER

 494            LOAD_CONST              12 ('durable_email_dedupe_unavailable')
                LOAD_DEREF              11 (src)
                CONTAINS_OP              0 (in)
                STORE_FAST               5 (soft_ok)

 495            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 496            LOAD_CONST              13 ('store:soft_fail_token')

 497            LOAD_FAST_BORROW         5 (soft_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               8 ('FAIL')

 498    L9:     LOAD_CONST              14 ('Dedupe store surfaces durable_email_dedupe_unavailable')

 499            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 500            LOAD_FAST_BORROW         5 (soft_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN
                LOAD_CONST               4 ('')
                JUMP_FORWARD             1 (to L11)
       L10:     LOAD_CONST              15 ('structural soft-fail token missing')

 495   L11:     LOAD_CONST              11 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 503            LOAD_CONST              16 ('missing_brokerage_id')
                LOAD_DEREF              11 (src)
                CONTAINS_OP              0 (in)
                STORE_FAST               6 (bid_ok)

 504            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 505            LOAD_CONST              17 ('store:requires_brokerage_id')

 506            LOAD_FAST_BORROW         6 (bid_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L12)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L13)
       L12:     LOAD_CONST               8 ('FAIL')

 507   L13:     LOAD_CONST              18 ('Dedupe store rejects calls without brokerage_id')

 508            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 509            LOAD_FAST_BORROW         6 (bid_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L14)
                NOT_TAKEN
                LOAD_CONST               4 ('')
                JUMP_FORWARD             1 (to L15)
       L14:     LOAD_CONST              19 ('missing_brokerage_id token not found')

 504   L15:     LOAD_CONST              11 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 512            LOAD_GLOBAL             14 (FORBIDDEN_RESPONSE_KEYS)
                GET_ITER
       L16:     FOR_ITER               139 (to L26)
                STORE_FAST               7 (forbidden)

 513            LOAD_CONST              20 ('"')
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

 514            LOAD_GLOBAL             16 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L20)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW        11 (src)
                BUILD_TUPLE              1
                LOAD_CONST              24 (<code object <genexpr> at 0x0000018C18025A30, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 514>)
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
                LOAD_FAST_BORROW        11 (src)
                BUILD_TUPLE              1
                LOAD_CONST              24 (<code object <genexpr> at 0x0000018C18025A30, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 514>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         8 (bad_shapes)
                GET_ITER
                CALL                     0
                CALL                     1
       L21:     STORE_FAST               9 (present)

 515            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 516            LOAD_CONST              27 ('store:no_forbidden_response_key:')
                LOAD_FAST_BORROW         7 (forbidden)
                FORMAT_SIMPLE
                BUILD_STRING             2

 517            LOAD_FAST_BORROW         9 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L22)
                NOT_TAKEN
                LOAD_CONST               8 ('FAIL')
                JUMP_FORWARD             1 (to L23)
       L22:     LOAD_CONST               7 ('PASS')

 518   L23:     LOAD_CONST              28 ('Dedupe store excludes forbidden response key: ')
                LOAD_FAST_BORROW         7 (forbidden)
                FORMAT_SIMPLE
                BUILD_STRING             2

 519            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 521            LOAD_FAST_BORROW         9 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        8 (to L24)
                NOT_TAKEN

 520            LOAD_CONST              29 ('forbidden response key ')
                LOAD_FAST_BORROW         7 (forbidden)
                CONVERT_VALUE            2 (repr)
                FORMAT_SIMPLE
                LOAD_CONST              30 (' present')
                BUILD_STRING             3
                JUMP_FORWARD             1 (to L25)

 521   L24:     LOAD_CONST               4 ('')

 515   L25:     LOAD_CONST              11 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          141 (to L16)

 512   L26:     END_FOR
                POP_ITER

 525            LOAD_CONST              31 ('_MIN_TTL_HOURS')
                LOAD_DEREF              11 (src)
                CONTAINS_OP              0 (in)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L27)
                NOT_TAKEN
                POP_TOP

 526            LOAD_CONST              32 ('_MAX_TTL_HOURS')
                LOAD_DEREF              11 (src)
                CONTAINS_OP              0 (in)

 525            COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        6 (to L27)
                NOT_TAKEN
                POP_TOP

 527            LOAD_CONST              33 ('168')
                LOAD_DEREF              11 (src)
                CONTAINS_OP              0 (in)

 524   L27:     STORE_FAST              10 (ttl_ok)

 529            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 530            LOAD_CONST              34 ('store:ttl_bounds_1_168')

 531            LOAD_FAST_BORROW        10 (ttl_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L28)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L29)
       L28:     LOAD_CONST               8 ('FAIL')

 532   L29:     LOAD_CONST              35 ('Dedupe store clamps TTL to [1, 168] hours')

 533            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 534            LOAD_FAST_BORROW        10 (ttl_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L30)
                NOT_TAKEN
                LOAD_CONST               4 ('')
                JUMP_FORWARD             1 (to L31)
       L30:     LOAD_CONST              36 ('expected _MIN_TTL_HOURS / _MAX_TTL_HOURS 1..168')

 529   L31:     LOAD_CONST              11 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 536            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18025A30, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 514>:
  --           COPY_FREE_VARS           1

 514           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 539>:
539           RESUME                   0
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

Disassembly of <code object check_service_integration at 0x0000018C17F7A440, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 539>:
  --            MAKE_CELL               12 (src)

 539            RESUME                   0

 540            BUILD_LIST               0
                STORE_FAST               1 (out)

 541            LOAD_GLOBAL              1 (Path + NULL)
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

 542            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (p)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               4 ('')
        L1:     STORE_DEREF             12 (src)

 543            LOAD_GLOBAL              4 (REQUIRED_SERVICE_TOKENS)
                GET_ITER
        L2:     FOR_ITER                72 (to L7)
                STORE_FAST               3 (tok)

 544            LOAD_FAST_BORROW         3 (tok)
                LOAD_DEREF              12 (src)
                CONTAINS_OP              0 (in)
                STORE_FAST               4 (ok)

 545            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 546            LOAD_CONST               5 ('service_token:')
                LOAD_FAST_BORROW         3 (tok)
                FORMAT_SIMPLE
                BUILD_STRING             2

 547            LOAD_FAST_BORROW         4 (ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L3)
                NOT_TAKEN
                LOAD_CONST               6 ('PASS')
                JUMP_FORWARD             1 (to L4)
        L3:     LOAD_CONST               7 ('FAIL')

 548    L4:     LOAD_CONST               8 ('Service references ')
                LOAD_FAST_BORROW         3 (tok)
                FORMAT_SIMPLE
                BUILD_STRING             2

 549            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 550            LOAD_FAST_BORROW         4 (ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN
                LOAD_CONST               4 ('')
                JUMP_FORWARD             4 (to L6)
        L5:     LOAD_CONST               9 ('missing token ')
                LOAD_FAST_BORROW         3 (tok)
                FORMAT_SIMPLE
                BUILD_STRING             2

 545    L6:     LOAD_CONST              10 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           74 (to L2)

 543    L7:     END_FOR
                POP_ITER

 553            LOAD_CONST              11 ('brokerage:')
                LOAD_DEREF              12 (src)
                CONTAINS_OP              0 (in)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         6 (to L8)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              12 ('brokerage=')
                LOAD_DEREF              12 (src)
                CONTAINS_OP              0 (in)
        L8:     STORE_FAST               5 (bk_ok)

 554            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 555            LOAD_CONST              13 ('service:accepts_brokerage_kwarg')

 556            LOAD_FAST_BORROW         5 (bk_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L9)
                NOT_TAKEN
                LOAD_CONST               6 ('PASS')
                JUMP_FORWARD             1 (to L10)
        L9:     LOAD_CONST               7 ('FAIL')

 557   L10:     LOAD_CONST              14 ('Service accepts brokerage kwarg')

 558            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 559            LOAD_FAST_BORROW         5 (bk_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L11)
                NOT_TAKEN
                LOAD_CONST               4 ('')
                JUMP_FORWARD             1 (to L12)
       L11:     LOAD_CONST              15 ('service does not accept brokerage kwarg')

 554   L12:     LOAD_CONST              10 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 562            LOAD_GLOBAL             12 (REQUIRED_RESPONSE_FIELDS)
                GET_ITER
       L13:     FOR_ITER               138 (to L23)
                STORE_FAST               6 (field)

 563            LOAD_CONST              16 ('"')
                LOAD_FAST_BORROW         6 (field)
                FORMAT_SIMPLE
                LOAD_CONST              17 ('":')
                BUILD_STRING             3
                LOAD_CONST              18 ("'")
                LOAD_FAST_BORROW         6 (field)
                FORMAT_SIMPLE
                LOAD_CONST              19 ("':")
                BUILD_STRING             3
                BUILD_TUPLE              2
                STORE_FAST               7 (bad_shapes)

 564            LOAD_GLOBAL             14 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L17)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW        12 (src)
                BUILD_TUPLE              1
                LOAD_CONST              20 (<code object <genexpr> at 0x0000018C18025730, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 564>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         7 (bad_shapes)
                GET_ITER
                CALL                     0
       L14:     FOR_ITER                12 (to L16)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L15)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L14)
       L15:     POP_ITER
                LOAD_CONST              21 (True)
                JUMP_FORWARD            20 (to L18)
       L16:     END_FOR
                POP_ITER
                LOAD_CONST              22 (False)
                JUMP_FORWARD            16 (to L18)
       L17:     PUSH_NULL
                LOAD_FAST_BORROW        12 (src)
                BUILD_TUPLE              1
                LOAD_CONST              20 (<code object <genexpr> at 0x0000018C18025730, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 564>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         7 (bad_shapes)
                GET_ITER
                CALL                     0
                CALL                     1
       L18:     STORE_FAST               8 (present)

 565            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 566            LOAD_CONST              23 ('service:response_field:')
                LOAD_FAST_BORROW         6 (field)
                FORMAT_SIMPLE
                BUILD_STRING             2

 567            LOAD_FAST_BORROW         8 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L19)
                NOT_TAKEN
                LOAD_CONST               6 ('PASS')
                JUMP_FORWARD             1 (to L20)
       L19:     LOAD_CONST               7 ('FAIL')

 568   L20:     LOAD_CONST              24 ('Service response includes field: ')
                LOAD_FAST_BORROW         6 (field)
                FORMAT_SIMPLE
                BUILD_STRING             2

 569            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 570            LOAD_FAST_BORROW         8 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L21)
                NOT_TAKEN
                LOAD_CONST               4 ('')
                JUMP_FORWARD             5 (to L22)
       L21:     LOAD_CONST              25 ('missing response key ')
                LOAD_FAST_BORROW         6 (field)
                CONVERT_VALUE            2 (repr)
                FORMAT_SIMPLE
                BUILD_STRING             2

 565   L22:     LOAD_CONST              10 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          140 (to L13)

 562   L23:     END_FOR
                POP_ITER

 574            LOAD_CONST              26 ('register_email_lead_dedupe')
                LOAD_DEREF              12 (src)
                CONTAINS_OP              0 (in)
                STORE_FAST               9 (fallback_ok)

 575            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 576            LOAD_CONST              27 ('service:process_local_fallback_present')

 577            LOAD_FAST_BORROW         9 (fallback_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L24)
                NOT_TAKEN
                LOAD_CONST               6 ('PASS')
                JUMP_FORWARD             1 (to L25)
       L24:     LOAD_CONST               7 ('FAIL')

 578   L25:     LOAD_CONST              28 ('Service retains PAS165 process-local dedupe fallback')

 579            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 580            LOAD_FAST_BORROW         9 (fallback_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L26)
                NOT_TAKEN
                LOAD_CONST               4 ('')
                JUMP_FORWARD             1 (to L27)
       L26:     LOAD_CONST              29 ('process-local fallback not referenced')

 575   L27:     LOAD_CONST              10 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 587            LOAD_CONST              30 ('is True')
                LOAD_DEREF              12 (src)
                CONTAINS_OP              0 (in)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        6 (to L28)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              31 ('email_forwarder_signature_required')
                LOAD_DEREF              12 (src)
                CONTAINS_OP              0 (in)

 586   L28:     STORE_FAST              10 (strict_true)

 589            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 590            LOAD_CONST              32 ('service:strict_literal_true_policy')

 591            LOAD_FAST_BORROW        10 (strict_true)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L29)
                NOT_TAKEN
                LOAD_CONST               6 ('PASS')
                JUMP_FORWARD             1 (to L30)
       L29:     LOAD_CONST               7 ('FAIL')

 592   L30:     LOAD_CONST              33 ("Signature-required policy uses 'is True' (strict literal)")

 593            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 594            LOAD_FAST_BORROW        10 (strict_true)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L31)
                NOT_TAKEN
                LOAD_CONST               4 ('')
                JUMP_FORWARD             1 (to L32)

 595   L31:     LOAD_CONST              34 ("expected an 'is True' comparison in the required-policy helper")

 589   L32:     LOAD_CONST              10 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 599            LOAD_GLOBAL             16 (FORBIDDEN_RESPONSE_KEYS)
                GET_ITER
       L33:     FOR_ITER               139 (to L43)
                STORE_FAST              11 (forbidden)

 600            LOAD_CONST              16 ('"')
                LOAD_FAST_BORROW        11 (forbidden)
                FORMAT_SIMPLE
                LOAD_CONST              17 ('":')
                BUILD_STRING             3
                LOAD_CONST              18 ("'")
                LOAD_FAST_BORROW        11 (forbidden)
                FORMAT_SIMPLE
                LOAD_CONST              19 ("':")
                BUILD_STRING             3
                BUILD_TUPLE              2
                STORE_FAST               7 (bad_shapes)

 601            LOAD_GLOBAL             14 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L37)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW        12 (src)
                BUILD_TUPLE              1
                LOAD_CONST              35 (<code object <genexpr> at 0x0000018C18024E30, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 601>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         7 (bad_shapes)
                GET_ITER
                CALL                     0
       L34:     FOR_ITER                12 (to L36)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L35)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L34)
       L35:     POP_ITER
                LOAD_CONST              21 (True)
                JUMP_FORWARD            20 (to L38)
       L36:     END_FOR
                POP_ITER
                LOAD_CONST              22 (False)
                JUMP_FORWARD            16 (to L38)
       L37:     PUSH_NULL
                LOAD_FAST_BORROW        12 (src)
                BUILD_TUPLE              1
                LOAD_CONST              35 (<code object <genexpr> at 0x0000018C18024E30, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 601>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         7 (bad_shapes)
                GET_ITER
                CALL                     0
                CALL                     1
       L38:     STORE_FAST               8 (present)

 602            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 603            LOAD_CONST              36 ('service:no_forbidden_response_key:')
                LOAD_FAST_BORROW        11 (forbidden)
                FORMAT_SIMPLE
                BUILD_STRING             2

 604            LOAD_FAST_BORROW         8 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L39)
                NOT_TAKEN
                LOAD_CONST               7 ('FAIL')
                JUMP_FORWARD             1 (to L40)
       L39:     LOAD_CONST               6 ('PASS')

 605   L40:     LOAD_CONST              37 ('Service excludes forbidden response key: ')
                LOAD_FAST_BORROW        11 (forbidden)
                FORMAT_SIMPLE
                BUILD_STRING             2

 606            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 608            LOAD_FAST_BORROW         8 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        8 (to L41)
                NOT_TAKEN

 607            LOAD_CONST              38 ('forbidden response key ')
                LOAD_FAST_BORROW        11 (forbidden)
                CONVERT_VALUE            2 (repr)
                FORMAT_SIMPLE
                LOAD_CONST              39 (' present')
                BUILD_STRING             3
                JUMP_FORWARD             1 (to L42)

 608   L41:     LOAD_CONST               4 ('')

 602   L42:     LOAD_CONST              10 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          141 (to L33)

 599   L43:     END_FOR
                POP_ITER

 610            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18025730, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 564>:
  --           COPY_FREE_VARS           1

 564           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C18024E30, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 601>:
  --           COPY_FREE_VARS           1

 601           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA32D0, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 613>:
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

Disassembly of <code object check_route_integration at 0x0000018C17E95410, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 613>:
613            RESUME                   0

614            BUILD_LIST               0
               STORE_FAST               1 (out)

615            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('routes')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('email_ingestion.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

616            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               3 ('')
       L1:     STORE_FAST               3 (src)

617            LOAD_GLOBAL              4 (REQUIRED_ROUTE_DECLS)
               GET_ITER
       L2:     FOR_ITER                71 (to L7)
               STORE_FAST               4 (decl)

618            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (decl, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (present)

619            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

620            LOAD_CONST               4 ('route_decl:')
               LOAD_FAST_BORROW         4 (decl)
               FORMAT_SIMPLE
               BUILD_STRING             2

621            LOAD_FAST_BORROW         5 (present)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               6 ('FAIL')

622    L4:     LOAD_CONST               7 ('Route declaration present: ')
               LOAD_FAST_BORROW         4 (decl)
               FORMAT_SIMPLE
               BUILD_STRING             2

623            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

624            LOAD_FAST_BORROW         5 (present)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               3 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST               8 ('missing decl: ')
               LOAD_FAST_BORROW         4 (decl)
               FORMAT_SIMPLE
               BUILD_STRING             2

619    L6:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           73 (to L2)

617    L7:     END_FOR
               POP_ITER

627            LOAD_CONST              10 ('brokerage=brokerage')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               STORE_FAST               6 (pass_ok)

628            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

629            LOAD_CONST              11 ('route:passes_brokerage_row')

630            LOAD_FAST_BORROW         6 (pass_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST               6 ('FAIL')

631    L9:     LOAD_CONST              12 ('Route passes full brokerage row to ingest_email_lead')

632            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

633            LOAD_FAST_BORROW         6 (pass_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST               3 ('')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST              13 ('missing brokerage=brokerage kwarg')

628   L11:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

636            LOAD_GLOBAL             13 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               7 (executable)

637            LOAD_CONST              25 (('body.brokerage_id', 'body["brokerage_id"]', "body['brokerage_id']"))
               GET_ITER
      L12:     FOR_ITER                80 (to L17)
               STORE_FAST               8 (bad_pattern)

642            LOAD_FAST_BORROW_LOAD_FAST_BORROW 135 (bad_pattern, executable)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (present)

643            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

644            LOAD_CONST              14 ('route:no_body_trust:')
               LOAD_FAST_BORROW         8 (bad_pattern)
               LOAD_CONST              15 (slice(None, 40, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

645            LOAD_FAST_BORROW         5 (present)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L13)
               NOT_TAKEN
               LOAD_CONST               6 ('FAIL')
               JUMP_FORWARD             1 (to L14)
      L13:     LOAD_CONST               5 ('PASS')

646   L14:     LOAD_CONST              16 ('Route never reads brokerage_id from body: ')
               LOAD_FAST_BORROW         8 (bad_pattern)
               FORMAT_SIMPLE
               BUILD_STRING             2

647            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

649            LOAD_FAST_BORROW         5 (present)
               TO_BOOL
               POP_JUMP_IF_FALSE        8 (to L15)
               NOT_TAKEN

648            LOAD_CONST              17 ('body-trust pattern ')
               LOAD_FAST_BORROW         8 (bad_pattern)
               CONVERT_VALUE            2 (repr)
               FORMAT_SIMPLE
               LOAD_CONST              18 (' present')
               BUILD_STRING             3
               JUMP_FORWARD             1 (to L16)

649   L15:     LOAD_CONST               3 ('')

643   L16:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           82 (to L12)

637   L17:     END_FOR
               POP_ITER

652            LOAD_FAST_BORROW         3 (src)
               LOAD_ATTR               15 (find + NULL|self)
               LOAD_CONST              19 ('_EVENT_PAYLOAD_ALLOWED')
               CALL                     1
               STORE_FAST               9 (allow_idx)

653            LOAD_FAST_BORROW         9 (allow_idx)
               LOAD_SMALL_INT           0
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE       12 (to L18)
               NOT_TAKEN
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 57 (src, allow_idx)
               LOAD_FAST_BORROW         9 (allow_idx)
               LOAD_CONST              20 (1024)
               BINARY_OP                0 (+)
               BINARY_SLICE
               JUMP_FORWARD             1 (to L19)
      L18:     LOAD_CONST               3 ('')
      L19:     STORE_FAST              10 (allow_window)

654            LOAD_GLOBAL             16 (FORBIDDEN_EVENT_PAYLOAD_KEYS)
               GET_ITER
      L20:     FOR_ITER                79 (to L25)
               STORE_FAST              11 (forbidden)

655            LOAD_CONST              21 ('"')
               LOAD_FAST_BORROW        11 (forbidden)
               FORMAT_SIMPLE
               LOAD_CONST              21 ('"')
               BUILD_STRING             3
               STORE_FAST              12 (candidate)

656            LOAD_FAST_BORROW_LOAD_FAST_BORROW 202 (candidate, allow_window)
               CONTAINS_OP              0 (in)
               STORE_FAST              13 (present_in_allowed)

657            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

658            LOAD_CONST              22 ('route:event_allowlist_excludes:')
               LOAD_FAST_BORROW        11 (forbidden)
               FORMAT_SIMPLE
               BUILD_STRING             2

659            LOAD_FAST_BORROW        13 (present_in_allowed)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L21)
               NOT_TAKEN
               LOAD_CONST               6 ('FAIL')
               JUMP_FORWARD             1 (to L22)
      L21:     LOAD_CONST               5 ('PASS')

660   L22:     LOAD_CONST              23 ('Event payload allow-list excludes forbidden key: ')
               LOAD_FAST_BORROW        11 (forbidden)
               FORMAT_SIMPLE
               BUILD_STRING             2

661            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

663            LOAD_FAST_BORROW        13 (present_in_allowed)
               TO_BOOL
               POP_JUMP_IF_FALSE        8 (to L23)
               NOT_TAKEN

662            LOAD_CONST              24 ('forbidden allow-list key ')
               LOAD_FAST_BORROW        11 (forbidden)
               CONVERT_VALUE            2 (repr)
               FORMAT_SIMPLE
               LOAD_CONST              18 (' present')
               BUILD_STRING             3
               JUMP_FORWARD             1 (to L24)

663   L23:     LOAD_CONST               3 ('')

657   L24:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           81 (to L20)

654   L25:     END_FOR
               POP_ITER

665            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 668>:
668           RESUME                   0
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

Disassembly of <code object check_event_contract at 0x0000018C17FEDA30, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 668>:
668           RESUME                   0

669           BUILD_LIST               0
              STORE_FAST               1 (out)

670           LOAD_GLOBAL              1 (Path + NULL)
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

671           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

672           LOAD_GLOBAL              4 (REQUIRED_EVENT_TYPES)
              GET_ITER
      L2:     FOR_ITER                72 (to L7)
              STORE_FAST               4 (required)

673           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (required, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

674           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

675           LOAD_CONST               5 ('events:')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

676           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               6 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               7 ('FAIL')

677   L4:     LOAD_CONST               8 ('Event contract registers ')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

678           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

679           LOAD_FAST_BORROW         5 (ok)
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

674   L6:     LOAD_CONST              10 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           74 (to L2)

672   L7:     END_FOR
              POP_ITER

681           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 684>:
684           RESUME                   0
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

Disassembly of <code object check_no_forbidden_imports at 0x0000018C17D8B970, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 684>:
684            RESUME                   0

685            BUILD_LIST               0
               STORE_FAST               1 (out)

686            LOAD_CONST               9 (('app/services/ingestion/email_dedupe_store.py', 'app/services/ingestion/email_ingestion.py', 'app/routes/email_ingestion.py', 'scripts/pas166_email_dedupe_policy_readiness_check.py'))
               STORE_FAST               2 (files)

692            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               241 (to L12)
               STORE_FAST               3 (relpath)

693            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

694            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L2:     STORE_FAST               5 (src)

695            BUILD_LIST               0
               STORE_FAST               6 (bad)

696            LOAD_FAST_BORROW         5 (src)
               LOAD_ATTR                5 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L3:     FOR_ITER                74 (to L7)
               STORE_FAST               7 (line)

697            LOAD_FAST_BORROW         7 (line)
               LOAD_ATTR                7 (strip + NULL|self)
               CALL                     0
               STORE_FAST               8 (stripped)

698            LOAD_GLOBAL              8 (FORBIDDEN_IMPORT_LINE_PREFIXES)
               GET_ITER
       L4:     FOR_ITER                45 (to L6)
               STORE_FAST               9 (prefix)

699            LOAD_FAST_BORROW         8 (stripped)
               LOAD_ATTR               11 (startswith + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           28 (to L4)

700    L5:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR               13 (append + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           47 (to L4)

698    L6:     END_FOR
               POP_ITER
               JUMP_BACKWARD           76 (to L3)

696    L7:     END_FOR
               POP_ITER

701            LOAD_FAST                1 (out)
               LOAD_ATTR               13 (append + NULL|self)
               LOAD_GLOBAL             15 (_check + NULL)

702            LOAD_CONST               2 ('forbidden_import:')
               LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR               16 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

703            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST               4 ('PASS')

704    L9:     LOAD_CONST               5 ('No forbidden imports: ')
               LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR               16 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

705            LOAD_GLOBAL             18 (SEVERITY_BLOCK)

707            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L10)
               NOT_TAKEN

706            LOAD_CONST               6 ('forbidden import prefixes: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               21 (join + NULL|self)
               LOAD_FAST_BORROW         6 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L11)

707   L10:     LOAD_CONST               1 ('')

701   L11:     LOAD_CONST               8 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          243 (to L1)

692   L12:     END_FOR
               POP_ITER

709            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 712>:
712           RESUME                   0
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

Disassembly of <code object check_no_inbox_scanning at 0x0000018C17CC2460, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 712>:
712            RESUME                   0

713            BUILD_LIST               0
               STORE_FAST               1 (out)

714            LOAD_CONST               9 (('app/services/ingestion/email_dedupe_store.py', 'app/services/ingestion/email_ingestion.py', 'app/routes/email_ingestion.py'))
               STORE_FAST               2 (files)

719            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               196 (to L10)
               STORE_FAST               3 (relpath)

720            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

721            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L2:     STORE_FAST               5 (src)

722            LOAD_GLOBAL              5 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         5 (src)
               CALL                     1
               STORE_FAST               6 (executable)

723            BUILD_LIST               0
               STORE_FAST               7 (bad)

724            LOAD_GLOBAL              6 (FORBIDDEN_INBOX_TOKENS)
               GET_ITER
       L3:     FOR_ITER                28 (to L5)
               STORE_FAST               8 (token)

725            LOAD_FAST_BORROW_LOAD_FAST_BORROW 134 (token, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L3)

726    L4:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_FAST_BORROW         8 (token)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L3)

724    L5:     END_FOR
               POP_ITER

727            LOAD_FAST                1 (out)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_GLOBAL             11 (_check + NULL)

728            LOAD_CONST               2 ('no_inbox_scan:')
               LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR               12 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

729            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L6)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L7)
       L6:     LOAD_CONST               4 ('PASS')

730    L7:     LOAD_CONST               5 ('No inbox-scanning tokens: ')
               LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR               12 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

731            LOAD_GLOBAL             14 (SEVERITY_BLOCK)

733            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L8)
               NOT_TAKEN

732            LOAD_CONST               6 ('inbox-scan tokens present: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               17 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L9)

733    L8:     LOAD_CONST               1 ('')

727    L9:     LOAD_CONST               8 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          198 (to L1)

719   L10:     END_FOR
               POP_ITER

735            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 738>:
738           RESUME                   0
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

Disassembly of <code object check_docs_required_doctrine at 0x0000018C17F739B0, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 738>:
  --            MAKE_CELL                8 (lower)

 738            RESUME                   0

 739            BUILD_LIST               0
                STORE_FAST               1 (out)

 740            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('docs')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('pas166_durable_email_dedupe_and_signature_policy.md')
                BINARY_OP               11 (/)
                STORE_FAST               2 (doc)

 741            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (doc)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L1:     STORE_FAST               3 (src)

 742            LOAD_FAST_BORROW         3 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_DEREF              8 (lower)

 743            LOAD_CONST              13 ((('purpose', ('purpose',)), ('relationship-prior', ('pas164', 'pas165')), ('why-durable', ('restart', 'multi-replica', 'durable dedupe')), ('migration-proposal', ('migration', 'proposal')), ('durable-vs-fallback', ('fallback', 'process-local')), ('signature-required', ('signature-required', 'signature required', 'required policy')), ('strict-literal-true', ('strict-literal', 'literal true', 'strict literal')), ('response-shape', ('response shape', 'forwarder_required', 'dedupe_durable')), ('event-safety', ('event payload safety', 'event payload', 'allow-list')), ('no-raw-storage', ('no raw email', 'raw email body', 'no raw body')), ('no-gmail', ('no gmail oauth', 'no gmail')), ('no-inbox-scan', ('no inbox scanning', 'no inbox')), ('not-built', ('intentionally not built', 'deliberately not', 'what is intentionally')), ('brokerage-pilot', ('brokerage pilot', 'real brokerage', 'brokerage pilots')), ('limitations', ('limitation', 'limitations'))))
                STORE_FAST               4 (required_phrases)

 768            LOAD_FAST_BORROW         4 (required_phrases)
                GET_ITER
        L2:     FOR_ITER               146 (to L12)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   86 (name, phrases)

 769            LOAD_GLOBAL              6 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         8 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18025130, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 769>)
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
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18025130, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 769>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         6 (phrases)
                GET_ITER
                CALL                     0
                CALL                     1
        L7:     STORE_FAST               7 (present)

 770            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 771            LOAD_CONST               6 ('docs:phrase:')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 772            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               8 ('FAIL')

 773    L9:     LOAD_CONST               9 ('Doc carries clause: ')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 774            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 776            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L10)
                NOT_TAKEN

 775            LOAD_CONST              10 ('expected one of: ')
                LOAD_CONST              11 (' | ')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_FAST_BORROW         6 (phrases)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L11)

 776   L10:     LOAD_CONST               2 ('')

 770   L11:     LOAD_CONST              12 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          148 (to L2)

 768   L12:     END_FOR
                POP_ITER

 778            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18025130, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 769>:
  --           COPY_FREE_VARS           1

 769           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA26A0, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 781>:
781           RESUME                   0
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

Disassembly of <code object check_self_no_env_or_vendor at 0x0000018C17F699C0, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 781>:
781            RESUME                   0

782            BUILD_LIST               0
               STORE_FAST               1 (out)

783            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_GLOBAL              2 (__file__)
               CALL                     1
               LOAD_ATTR                5 (resolve + NULL|self)
               CALL                     0
               STORE_FAST               2 (self_path)

784            LOAD_GLOBAL              7 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (self_path)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L1:     STORE_FAST               3 (src)

785            BUILD_LIST               0
               STORE_FAST               4 (bad)

786            LOAD_FAST_BORROW         3 (src)
               LOAD_ATTR                9 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L2:     EXTENDED_ARG             1
               FOR_ITER               311 (to L11)
               STORE_FAST               5 (raw_line)

787            LOAD_FAST_BORROW         5 (raw_line)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0
               STORE_FAST               6 (stripped)

788            LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST               1 ('#')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

789            JUMP_BACKWARD           45 (to L2)

790    L3:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              16 (('import dotenv', 'from dotenv'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L4)
               NOT_TAKEN

791            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               2 ('dotenv import')
               CALL                     1
               POP_TOP

792    L4:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              17 (('import supabase', 'from supabase'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L5)
               NOT_TAKEN

793            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               3 ('supabase import')
               CALL                     1
               POP_TOP

794    L5:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              18 (('import composio', 'from composio', 'import trustclaw', 'from trustclaw', 'import openai', 'from openai', 'import anthropic', 'from anthropic', 'import googleapiclient', 'from googleapiclient', 'import google.oauth2', 'from google.oauth2'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L6)
               NOT_TAKEN

802            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               4 ('external-vendor / google import')
               CALL                     1
               POP_TOP

803    L6:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              19 (('import numpy', 'import faiss', 'import pgvector', 'from pgvector', 'from openai import embeddings', 'from openai.embeddings'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L7)
               NOT_TAKEN

809            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               5 ('embedding / vector import')
               CALL                     1
               POP_TOP

810    L7:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST               6 ('load_dotenv()')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        24 (to L8)
               NOT_TAKEN

811            LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               17 (endswith + NULL|self)
               LOAD_CONST               6 ('load_dotenv()')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L9)
               NOT_TAKEN

812    L8:     LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               7 ('load_dotenv() call')
               CALL                     1
               POP_TOP

813    L9:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              20 (('os.environ[', 'os.getenv(', 'getenv('))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         4 (to L10)
               NOT_TAKEN
               EXTENDED_ARG             1
               JUMP_BACKWARD          294 (to L2)

814   L10:     LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               8 ('environ read')
               CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          314 (to L2)

786   L11:     END_FOR
               POP_ITER

815            LOAD_FAST                1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             19 (_check + NULL)

816            LOAD_CONST               9 ('self_check:no_env_or_vendor')

817            LOAD_FAST_BORROW         4 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L12)
               NOT_TAKEN
               LOAD_CONST              10 ('FAIL')
               JUMP_FORWARD             1 (to L13)
      L12:     LOAD_CONST              11 ('PASS')

818   L13:     LOAD_CONST              12 ('PAS166 readiness checker never reads .env, calls Supabase, or imports vendor / Google / embedding libs')

820            LOAD_GLOBAL             20 (SEVERITY_BLOCK)

822            LOAD_FAST_BORROW         4 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L14)
               NOT_TAKEN

821            LOAD_CONST              13 ('disqualifying code-line patterns: ')
               LOAD_CONST              14 (', ')
               LOAD_ATTR               23 (join + NULL|self)
               LOAD_FAST_BORROW         4 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L15)

822   L14:     LOAD_CONST               0 ('')

815   L15:     LOAD_CONST              15 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

824            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2790, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 831>:
831           RESUME                   0
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

Disassembly of <code object _aggregate at 0x0000018C17EC4280, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 831>:
 831            RESUME                   0

 833            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 832            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2

 833    L2:     FOR_ITER                49 (to L7)
                STORE_FAST               1 (c)

 834            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 833    L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L2)

 834    L4:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              2 (SEVERITY_BLOCK)
                COMPARE_OP              88 (bool(==))

 833    L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L2)
        L6:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L2)
        L7:     END_FOR
                POP_ITER

 832    L8:     STORE_FAST               2 (blockers)
                STORE_FAST               1 (c)

 837            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 836            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L9:     BUILD_LIST               0
                SWAP                     2

 837   L10:     FOR_ITER                49 (to L15)
                STORE_FAST               1 (c)

 838            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 837   L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L10)

 838   L12:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              4 (SEVERITY_INFO)
                COMPARE_OP              88 (bool(==))

 837   L13:     POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L10)
       L14:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L10)
       L15:     END_FOR
                POP_ITER

 836   L16:     STORE_FAST               3 (info)
                STORE_FAST               1 (c)

 841            LOAD_CONST               3 ('verdict')
                LOAD_FAST_BORROW         2 (blockers)
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L17)
                NOT_TAKEN
                LOAD_GLOBAL              6 (VERDICT_NOT_READY)
                JUMP_FORWARD             5 (to L18)
       L17:     LOAD_GLOBAL              8 (VERDICT_READY)

 842   L18:     LOAD_CONST               4 ('blockers')
                LOAD_FAST_BORROW         2 (blockers)

 843            LOAD_CONST               5 ('info')
                LOAD_FAST_BORROW         3 (info)

 840            BUILD_MAP                3
                RETURN_VALUE

  --   L19:     SWAP                     2
                POP_TOP

 832            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0

  --   L20:     SWAP                     2
                POP_TOP

 836            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L19 [2]
  L4 to L5 -> L19 [2]
  L6 to L8 -> L19 [2]
  L9 to L11 -> L20 [2]
  L12 to L13 -> L20 [2]
  L14 to L16 -> L20 [2]

Disassembly of <code object __annotate__ at 0x0000018C180FC030, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 847>:
847           RESUME                   0
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

Disassembly of <code object _operator_actions at 0x0000018C18048C70, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 847>:
847           RESUME                   0

848           BUILD_LIST               0
              STORE_FAST               1 (out)

849           LOAD_FAST_BORROW         0 (checks)
              GET_ITER
      L1:     FOR_ITER               109 (to L5)
              STORE_FAST               2 (c)

850           LOAD_FAST_BORROW         2 (c)
              LOAD_CONST               0 ('status')
              BINARY_OP               26 ([])
              LOAD_CONST               1 ('FAIL')
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

851           JUMP_BACKWARD           19 (to L1)

852   L2:     LOAD_FAST_BORROW         2 (c)
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

853           LOAD_FAST                1 (out)
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

849   L5:     END_FOR
              POP_ITER

854           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180FC6C0, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 857>:
857           RESUME                   0
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

Disassembly of <code object evaluate at 0x0000018C17F69E40, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 857>:
857           RESUME                   0

858           BUILD_LIST               0
              STORE_FAST               1 (checks)

859           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              3 (check_files_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

860           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              5 (check_prior_phases_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

861           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              7 (check_memory_review_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

862           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              9 (check_migration_proposal + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

863           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             11 (check_dedupe_store + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

864           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             13 (check_service_integration + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

865           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             15 (check_route_integration + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

866           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             17 (check_event_contract + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

867           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             19 (check_no_forbidden_imports + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

868           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             21 (check_no_inbox_scanning + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

869           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             23 (check_docs_required_doctrine + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

870           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             25 (check_self_no_env_or_vendor + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

872           LOAD_GLOBAL             27 (_aggregate + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1
              STORE_FAST               2 (agg)

874           LOAD_CONST               0 ('phase')
              LOAD_CONST               1 ('PAS166')

875           LOAD_CONST               2 ('generated_at')
              LOAD_GLOBAL             29 (_now_iso + NULL)
              CALL                     0

876           LOAD_CONST               3 ('verdict')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])

877           LOAD_CONST               4 ('ready')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])
              LOAD_GLOBAL             30 (VERDICT_READY)
              COMPARE_OP              72 (==)

878           LOAD_CONST               5 ('blocker_count')
              LOAD_GLOBAL             33 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               6 ('blockers')
              BINARY_OP               26 ([])
              CALL                     1

879           LOAD_CONST               7 ('info_count')
              LOAD_GLOBAL             33 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               8 ('info')
              BINARY_OP               26 ([])
              CALL                     1

880           LOAD_CONST               9 ('check_count')
              LOAD_GLOBAL             33 (len + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

881           LOAD_CONST              10 ('pass_count')
              LOAD_GLOBAL             35 (sum + NULL)
              LOAD_CONST              11 (<code object <genexpr> at 0x0000018C180531B0, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 881>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

882           LOAD_CONST              12 ('fail_count')
              LOAD_GLOBAL             35 (sum + NULL)
              LOAD_CONST              13 (<code object <genexpr> at 0x0000018C18053750, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 882>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

883           LOAD_CONST              14 ('checks')
              LOAD_FAST_BORROW         1 (checks)

884           LOAD_CONST              15 ('operator_actions')
              LOAD_GLOBAL             37 (_operator_actions + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

873           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C180531B0, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 881>:
 881           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C18053750, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 882>:
 882           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C180FC7B0, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 891>:
891           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C1801CDC0, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 891>:
891           RESUME                   0

892           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

893           LOAD_CONST               0 ('pas166_email_dedupe_policy_readiness_check')

895           LOAD_CONST               1 ('PAS166 — Evaluate the durable email dedupe + signature-required policy layer for structural correctness, no-Gmail-OAuth doctrine, no inbox scanning, no raw-body / signature / dedupe-key / secret leakage. Read-only. Does not touch Supabase, .env, or any tenant data.')

892           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

903           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

904           LOAD_CONST               3 ('--repo-root')
              LOAD_GLOBAL              6 (_REPO_ROOT_DEFAULT)

905           LOAD_CONST               4 ('Repo root to evaluate (default: parent of this script).')

903           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

907           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

908           LOAD_CONST               6 ('--output')
              LOAD_GLOBAL              8 (REPORT_FILENAME)

909           LOAD_CONST               7 ('Where to write the JSON report (default ./')
              LOAD_GLOBAL              8 (REPORT_FILENAME)
              FORMAT_SIMPLE
              LOAD_CONST               8 (').')
              BUILD_STRING             3

907           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

911           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

912           LOAD_CONST               9 ('--json')
              LOAD_CONST              10 ('store_true')

913           LOAD_CONST              11 ('Emit the report JSON on stdout in addition to the file.')

911           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

915           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

916           LOAD_CONST              13 ('--summary-only')
              LOAD_CONST              10 ('store_true')

917           LOAD_CONST              14 ('Skip writing the full report file; print verdict only.')

915           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

919           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

920           LOAD_CONST              15 ('--strict')
              LOAD_CONST              10 ('store_true')

921           LOAD_CONST              16 ('Exit 1 unless verdict == READY (default policy is the same).')

919           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

923           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180FC8A0, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 926>:
926           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C17D8C5C0, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 926>:
926           RESUME                   0

927           LOAD_GLOBAL              1 (print + NULL)

928           LOAD_CONST               0 ('[PAS166] verdict=')
              LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               1 ('verdict')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               2 (' blockers=')

929           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               3 ('blocker_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' info=')

930           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               5 ('info_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' checks=')

931           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               7 ('check_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' pass=')

932           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               9 ('pass_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              10 (' fail=')

933           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              11 ('fail_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE

928           BUILD_STRING            12

927           CALL                     1
              POP_TOP

935           LOAD_FAST_BORROW         0 (report)
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

936           LOAD_FAST_BORROW         1 (actions)
              TO_BOOL
              POP_JUMP_IF_FALSE       93 (to L5)
              NOT_TAKEN

937           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              13 ('[PAS166] operator actions:')
              CALL                     1
              POP_TOP

938           LOAD_FAST_BORROW         1 (actions)
              LOAD_CONST              14 (slice(None, 25, None))
              BINARY_OP               26 ([])
              GET_ITER
      L2:     FOR_ITER                17 (to L3)
              STORE_FAST               2 (a)

939           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              15 ('  - ')
              LOAD_FAST_BORROW         2 (a)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L2)

938   L3:     END_FOR
              POP_ITER

940           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         1 (actions)
              CALL                     1
              LOAD_SMALL_INT          25
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       34 (to L4)
              NOT_TAKEN

941           LOAD_GLOBAL              1 (print + NULL)
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

940   L4:     LOAD_CONST              18 (None)
              RETURN_VALUE

936   L5:     LOAD_CONST              18 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025530, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 944>:
944           RESUME                   0
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

Disassembly of <code object _write_report at 0x0000018C18104030, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 944>:
 944           RESUME                   0

 945           NOP

 946   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

 947           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

 948           LOAD_CONST               3 ('utf-8')

 946           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 950           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

 951   L4:     LOAD_GLOBAL             11 (print + NULL)

 952           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

 953           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

 952           BUILD_STRING             4

 954           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

 951           LOAD_CONST               7 (('file',))
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

 950   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C180FC990, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 958>:
958           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17F84690, file "scripts\pas166_email_dedupe_policy_readiness_check.py", line 958>:
 958            RESUME                   0

 959            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 960            NOP

 961    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 965    L2:     LOAD_GLOBAL             10 (os)
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

 966            LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               21 (isdir + NULL|self)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L4)
                NOT_TAKEN

 967            LOAD_GLOBAL             23 (print + NULL)

 968            LOAD_CONST               2 ('error: --repo-root not a directory: ')
                LOAD_FAST                4 (repo_root)
                FORMAT_SIMPLE
                BUILD_STRING             2

 969            LOAD_GLOBAL             24 (sys)
                LOAD_ATTR               26 (stderr)

 967            LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

 971            LOAD_SMALL_INT           2
                RETURN_VALUE

 973    L4:     LOAD_GLOBAL             29 (evaluate + NULL)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                STORE_FAST               5 (report)

 975            LOAD_FAST                2 (args)
                LOAD_ATTR               30 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L5)
                NOT_TAKEN

 976            LOAD_GLOBAL             33 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               34 (output)
                LOAD_FAST                5 (report)
                CALL                     2
                POP_TOP

 978    L5:     LOAD_GLOBAL             37 (_print_summary + NULL)
                LOAD_FAST                5 (report)
                CALL                     1
                POP_TOP

 980            LOAD_FAST                2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L6)
                NOT_TAKEN

 981            LOAD_GLOBAL             23 (print + NULL)
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

 983    L6:     LOAD_FAST                5 (report)
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

 962            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L17)
                NOT_TAKEN
                STORE_FAST               3 (e)

 963    L9:     LOAD_FAST                3 (e)
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

 962   L17:     RERAISE                  0

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
