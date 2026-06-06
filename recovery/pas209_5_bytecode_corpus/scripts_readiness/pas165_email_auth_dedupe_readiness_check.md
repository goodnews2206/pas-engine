# scripts_readiness/pas165_email_auth_dedupe_readiness_check

- **pyc:** `scripts\__pycache__\pas165_email_auth_dedupe_readiness_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/pas165_email_auth_dedupe_readiness_check.py`
- **co_filename (from bytecode):** `scripts\pas165_email_auth_dedupe_readiness_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS165 — Email forwarder authentication + dedupe readiness gate.

Deterministic, non-mutating evaluator for "is the PAS165
forwarder-signature + dedupe layer wired correctly,
structurally safe, and free of Gmail / OAuth / inbox /
raw-body regressions?".

Walks the repo and verifies:

  * email_auth.py exists and exports the signing / verifying
    helpers;
  * email_dedupe.py exists and exports the key builder /
    registrar / TTL constant;
  * the email-ingestion route accepts ``X-Forwarder-Signature``;
  * ingest_email_lead accepts ``forwarder_signature`` and
    ``forwarder_secret`` keyword args;
  * the response contract carries ``duplicate`` and
    ``forwarder_verified``;
  * the signature verifier uses a constant-time compare
    (``hmac.compare_digest``);
  * the canonical payload hashes the body BEFORE inclusion
    (so the body cap is enforced before signing);
  * the dedupe TTL is 24 hours (``24 * 60 * 60``);
  * the dedupe registry is process-local + RLock-protected;
  * the dedupe key is NEVER returned in the route response;
  * the signature is NEVER returned in the route response;
  * the event allow-list excludes phone / email / name /
    subject / sender / body / signature / dedupe_key /
    raw_email / raw_body / property_address / notes /
    transcript;
  * no Gmail / Google / IMAP / POP3 / inbox-scan tokens;
  * no embedding / vector / vendor imports;
  * Memory Review UI files are intact;
  * prior-phase readiness scripts (PAS160 / PAS161 / PAS162 /
    PAS163 / PAS164) still exist;
  * supports --summary-only and --json;
  * exits 0 ready, 1 blockers, 2 bad args;
  * never reads .env;
  * never touches production data.

Usage:
  python scripts/pas165_email_auth_dedupe_readiness_check.py
  python scripts/pas165_email_auth_dedupe_readiness_check.py --json
  python scripts/pas165_email_auth_dedupe_readiness_check.py --summary-only
  python scripts/pas165_email_auth_dedupe_readiness_check.py --strict

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

`__annotate__`, `_aggregate`, `_build_parser`, `_check`, `_now_iso`, `_operator_actions`, `_print_summary`, `_read_text`, `_strip_python_comments_and_strings`, `_write_report`, `check_docs_required_doctrine`, `check_email_auth`, `check_email_dedupe`, `check_event_contract`, `check_files_present`, `check_memory_review_intact`, `check_no_forbidden_imports`, `check_no_inbox_scanning`, `check_prior_phases_intact`, `check_route_signature_header`, `check_self_no_env_or_vendor`, `check_service_signature_kwargs`, `evaluate`, `main`

## Env-key candidates

`BLOCK`, `FAIL`, `INFO`, `NOT_READY`, `PAS165`, `PASS`, `READY`

## String constants (redacted where noted)

- '\nPAS165 — Email forwarder authentication + dedupe readiness gate.\n\nDeterministic, non-mutating evaluator for "is the PAS165\nforwarder-signature + dedupe layer wired correctly,\nstructurally safe, and free of Gmail / OAuth / inbox /\nraw-body regressions?".\n\nWalks the repo and verifies:\n\n  * email_auth.py exists and exports the signing / verifying\n    helpers;\n  * email_dedupe.py exists and exports the key builder /\n    registrar / TTL constant;\n  * the email-ingestion route accepts ``X-Forwarder-Signature``;\n  * ingest_email_lead accepts ``forwarder_signature`` and\n    ``forwarder_secret`` keyword args;\n  * the response contract carries ``duplicate`` and\n    ``forwarder_verified``;\n  * the signature verifier uses a constant-time compare\n    (``hmac.compare_digest``);\n  * the canonical payload hashes the body BEFORE inclusion\n    (so the body cap is enforced before signing);\n  * the dedupe TTL is 24 hours (``24 * 60 * 60``);\n  * the dedupe registry is process-local + RLock-protected;\n  * the dedupe key is NEVER returned in the route response;\n  * the signature is NEVER returned in the route response;\n  * the event allow-list excludes phone / email / name /\n    subject / sender / body / signature / dedupe_key /\n    raw_email / raw_body / property_address / notes /\n    transcript;\n  * no Gmail / Google / IMAP / POP3 / inbox-scan tokens;\n  * no embedding / vector / vendor imports;\n  * Memory Review UI files are intact;\n  * prior-phase readiness scripts (PAS160 / PAS161 / PAS162 /\n    PAS163 / PAS164) still exist;\n  * supports --summary-only and --json;\n  * exits 0 ready, 1 blockers, 2 bad args;\n  * never reads .env;\n  * never touches production data.\n\nUsage:\n  python scripts/pas165_email_auth_dedupe_readiness_check.py\n  python scripts/pas165_email_auth_dedupe_readiness_check.py --json\n  python scripts/pas165_email_auth_dedupe_readiness_check.py --summary-only\n  python scripts/pas165_email_auth_dedupe_readiness_check.py --strict\n\nExit codes:\n    0  — READY  (verdict == READY)\n    1  — NOT_READY\n    2  — bad CLI arguments\n'
- 'utf-8'
- 'READY'
- 'NOT_READY'
- 'BLOCK'
- 'INFO'
- 'severity'
- 'detail'
- 'pas165_email_auth_dedupe_readiness_report.json'
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
- 'Required PAS165 file present: '
- 'missing'
- 'prior_phase:'
- 'Prior-phase readiness script intact: '
- 'missing — PAS165 must not delete'
- 'memory_review_file:'
- 'Memory Review file present (PAS165 must not delete): '
- 'PAS165 must not delete Memory Review files'
- 'app'
- 'services'
- 'ingestion'
- 'email_auth.py'
- 'auth_fn:'
- 'Email auth function present: '
- 'missing def: '
- 'hmac.compare_digest'
- 'compare_digest'
- 'auth:constant_time_compare'
- 'Email auth uses constant-time signature compare'
- 'missing hmac.compare_digest'
- 'hashlib.sha256('
- 'sha256('
- 'body'
- 'auth:canonical_hashes_body'
- 'Canonical payload hashes the body before inclusion'
- 'expected sha256(body) in canonical builder'
- '_BODY_HASH_CAP_BYTES'
- '65536'
- '64 * 1024'
- 'auth:body_cap_present'
- 'Email auth caps body before hashing'
- 'expected body cap constant'
- 'forwarder_signature_unconfigured'
- 'forwarder_signature_missing'
- 'forwarder_signature_invalid'
- 'forwarder_signature_malformed'
- 'auth:soft_rollout_tokens'
- 'Email auth surfaces structural soft-rollout tokens'
- 'expected forwarder_signature_(unconfigured|missing|invalid|malformed)'
- 'email_dedupe.py'
- 'dedupe_fn:'
- 'Email dedupe function present: '
- 'DEDUPE_TTL_SECONDS = 24 * 60 * 60'
- 'DEDUPE_TTL_SECONDS = 86400'
- 'dedupe:ttl_24_hours'
- 'Dedupe TTL is 24 hours'
- 'DEDUPE_TTL_SECONDS != 24*60*60'
- '_DEDUPE_REGISTRY'
- 'RLock'
- 'threading.RLock'
- 'dedupe:process_local_registry'
- 'Dedupe registry is process-local'
- 'missing _DEDUPE_REGISTRY'
- 'dedupe:rlock_protected'
- 'Dedupe registry uses RLock for thread-safety'
- 'missing threading.RLock'
- 'brokerage_id'
- 'dedupe:no_brokerage_id_in_key'
- 'Dedupe key derivation never includes brokerage_id'
- 'brokerage_id appears in dedupe executable'
- 'email_ingestion.py'
- 'service_kw:'
- 'ingest_email_lead accepts '
- 'missing kwarg '
- 'verify_forwarder_signature'
- 'from app.services.ingestion.email_auth'
- 'service:uses_email_auth'
- 'Service references email_auth.verify_forwarder_signature'
- 'verify_forwarder_signature not referenced'
- 'build_email_dedupe_key'
- 'register_email_lead_dedupe'
- 'service:uses_email_dedupe'
- 'Service references email_dedupe build/register helpers'
- 'dedupe helpers not referenced'
- 'service:response_field:'
- 'Service response includes field: '
- 'missing response key '
- 'service:no_forbidden_response_key:'
- 'Service excludes forbidden response key: '
- 'forbidden response key '
- ' present'
- 'routes'
- 'route_decl:'
- 'Route declaration present: '
- 'missing decl: '
- 'X-Forwarder-Signature'
- 'route:accepts_forwarder_signature_header'
- 'Route accepts X-Forwarder-Signature header'
- 'missing X-Forwarder-Signature reference'
- 'forwarder_signature='
- 'forwarder_secret='
- 'route:passes_forwarder_signature'
- 'Route passes forwarder_signature kwarg to service'
- 'forwarder_signature= not passed to service'
- 'route:passes_forwarder_secret'
- 'Route passes forwarder_secret kwarg to service'
- 🔒 '<REDACTED:secret-bearing literal>'
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
- 'app/services/ingestion/email_auth.py'
- 'forbidden_import:'
- 'No forbidden imports: '
- 'forbidden import prefixes: '
- 'no_inbox_scan:'
- 'No inbox-scanning tokens: '
- 'inbox-scan tokens present: '
- 'docs'
- 'pas165_email_forwarder_auth_and_dedupe.md'
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
- 'PAS165 readiness checker never reads .env, calls Supabase, or imports vendor / Google / embedding libs'
- 'disqualifying code-line patterns: '
- 'checks'
- 'verdict'
- 'blockers'
- 'info'
- 'List[str]'
- ' — '
- 'see report'
- 'phase'
- 'PAS165'
- 'generated_at'
- 'ready'
- 'blocker_count'
- 'info_count'
- 'check_count'
- 'pass_count'
- 'fail_count'
- 'operator_actions'
- 'argparse.ArgumentParser'
- 'pas165_email_auth_dedupe_readiness_check'
- 'PAS165 — Evaluate the email forwarder authentication and dedupe layer for structural correctness, no-Gmail-OAuth doctrine, no inbox scanning, no raw-body / signature / dedupe-key leakage. Read-only. Does not touch Supabase, .env, or any tenant data.'
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
- '[PAS165] verdict='
- ' blockers='
- ' info='
- ' checks='
- ' pass='
- ' fail='
- '[PAS165] operator actions:'
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

   1           LOAD_CONST               0 ('\nPAS165 — Email forwarder authentication + dedupe readiness gate.\n\nDeterministic, non-mutating evaluator for "is the PAS165\nforwarder-signature + dedupe layer wired correctly,\nstructurally safe, and free of Gmail / OAuth / inbox /\nraw-body regressions?".\n\nWalks the repo and verifies:\n\n  * email_auth.py exists and exports the signing / verifying\n    helpers;\n  * email_dedupe.py exists and exports the key builder /\n    registrar / TTL constant;\n  * the email-ingestion route accepts ``X-Forwarder-Signature``;\n  * ingest_email_lead accepts ``forwarder_signature`` and\n    ``forwarder_secret`` keyword args;\n  * the response contract carries ``duplicate`` and\n    ``forwarder_verified``;\n  * the signature verifier uses a constant-time compare\n    (``hmac.compare_digest``);\n  * the canonical payload hashes the body BEFORE inclusion\n    (so the body cap is enforced before signing);\n  * the dedupe TTL is 24 hours (``24 * 60 * 60``);\n  * the dedupe registry is process-local + RLock-protected;\n  * the dedupe key is NEVER returned in the route response;\n  * the signature is NEVER returned in the route response;\n  * the event allow-list excludes phone / email / name /\n    subject / sender / body / signature / dedupe_key /\n    raw_email / raw_body / property_address / notes /\n    transcript;\n  * no Gmail / Google / IMAP / POP3 / inbox-scan tokens;\n  * no embedding / vector / vendor imports;\n  * Memory Review UI files are intact;\n  * prior-phase readiness scripts (PAS160 / PAS161 / PAS162 /\n    PAS163 / PAS164) still exist;\n  * supports --summary-only and --json;\n  * exits 0 ready, 1 blockers, 2 bad args;\n  * never reads .env;\n  * never touches production data.\n\nUsage:\n  python scripts/pas165_email_auth_dedupe_readiness_check.py\n  python scripts/pas165_email_auth_dedupe_readiness_check.py --json\n  python scripts/pas165_email_auth_dedupe_readiness_check.py --summary-only\n  python scripts/pas165_email_auth_dedupe_readiness_check.py --strict\n\nExit codes:\n    0  — READY  (verdict == READY)\n    1  — NOT_READY\n    2  — bad CLI arguments\n')
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

  88           LOAD_CONST              64 (('app/services/ingestion/email_auth.py', 'app/services/ingestion/email_dedupe.py', 'app/services/ingestion/email_ingestion.py', 'app/routes/email_ingestion.py', 'scripts/pas165_email_auth_dedupe_readiness_check.py', 'docs/pas165_email_forwarder_auth_and_dedupe.md', 'tests/mvp/test_pas165_email_auth_dedupe.py'))
               STORE_NAME              29 (REQUIRED_FILES)

  98           LOAD_CONST              65 (('scripts/pas160_mvp_sequence_check.py', 'scripts/pas161_lead_ingestion_readiness_check.py', 'scripts/pas162_pending_calls_readiness_check.py', 'scripts/pas163_candidate_pipeline_readiness_check.py', 'scripts/pas164_email_ingestion_readiness_check.py'))
               STORE_NAME              30 (PRIOR_PHASE_FILES)

 106           LOAD_CONST              66 (('app/services/memory/review.py', 'app/services/memory/review_stats.py', 'app/services/memory/review_export.py', 'app/services/memory/review_actors.py', 'app/services/memory/review_alerts.py', 'app/services/memory/operator_console.py'))
               STORE_NAME              31 (MEMORY_REVIEW_FILES)

 116           LOAD_CONST              67 (('def canonical_forward_payload(', 'def sign_forward_payload(', 'def verify_forwarder_signature('))
               STORE_NAME              32 (REQUIRED_AUTH_FUNCTIONS)

 122           LOAD_CONST              68 (('def build_email_dedupe_key(', 'def is_duplicate_email_lead(', 'def register_email_lead_dedupe(', 'def cleanup_expired_dedupe_entries(', 'def reset_email_dedupe_registry_for_tests('))
               STORE_NAME              33 (REQUIRED_DEDUPE_FUNCTIONS)

 131           LOAD_CONST              69 (('forwarder_signature', 'forwarder_secret'))
               STORE_NAME              34 (REQUIRED_SERVICE_SIGNATURE_TOKENS)

 137           LOAD_CONST              70 (('duplicate', 'forwarder_verified'))
               STORE_NAME              35 (REQUIRED_RESPONSE_FIELDS)

 143           LOAD_CONST              71 (('@router.post("/parse")', '@router.post("/ingest")'))
               STORE_NAME              36 (REQUIRED_ROUTE_DECLS)

 149           LOAD_CONST              72 (('email.lead.duplicate', 'email.forwarder.signature_invalid', 'email.forwarder.signature_missing', 'email.forwarder.signature_unconfigured', 'email.forwarder.verified'))
               STORE_NAME              37 (REQUIRED_EVENT_TYPES)

 159           LOAD_CONST              73 (('raw_email', 'raw_body', 'full_email', 'raw_payload', 'transcript'))
               STORE_NAME              38 (FORBIDDEN_RESPONSE_KEYS)

 169           LOAD_CONST              74 (('phone', 'email', 'name', 'subject', 'sender', 'body', 'signature', 'dedupe_key', 'raw_email', 'raw_body', 'property_address', 'notes', 'transcript'))
               STORE_NAME              39 (FORBIDDEN_EVENT_PAYLOAD_KEYS)

 186           LOAD_CONST              75 (('import googleapiclient', 'from googleapiclient', 'import google.oauth2', 'from google.oauth2', 'from google.auth', 'import google.auth', 'from google_auth_oauthlib', 'import composio', 'from composio', 'import trustclaw', 'from trustclaw', 'import openai', 'from openai', 'import anthropic', 'from anthropic', 'import numpy', 'import faiss', 'import pgvector', 'from pgvector', 'from openai import embeddings', 'from openai.embeddings', 'from app.services.memory', 'import app.services.memory'))
               STORE_NAME              40 (FORBIDDEN_IMPORT_LINE_PREFIXES)

 212           LOAD_CONST              76 (('imaplib', 'poplib', 'fetch_inbox', 'gmail_oauth', 'gmail_token', 'users().messages'))
               STORE_NAME              41 (FORBIDDEN_INBOX_TOKENS)

 226           LOAD_CONST              13 ('severity')

 228           LOAD_NAME               27 (SEVERITY_BLOCK)

 226           LOAD_CONST              14 ('detail')

 228           LOAD_CONST              15 ('')

 226           BUILD_MAP                2
               LOAD_CONST              16 (<code object __annotate__ at 0x0000018C18026530, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 226>)
               MAKE_FUNCTION
               LOAD_CONST              17 (<code object _check at 0x0000018C17FA3E10, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 226>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              42 (_check)

 239           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA3960, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 239>)
               MAKE_FUNCTION
               LOAD_CONST              19 (<code object _now_iso at 0x0000018C18038DF0, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 239>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              43 (_now_iso)

 243           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA31E0, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 243>)
               MAKE_FUNCTION
               LOAD_CONST              21 (<code object _read_text at 0x0000018C180533F0, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 243>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              44 (_read_text)

 250           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA3C30, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 250>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object _strip_python_comments_and_strings at 0x0000018C17D8C200, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 250>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              45 (_strip_python_comments_and_strings)

 289           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA3A50, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 289>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object check_files_present at 0x0000018C180606F0, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 289>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              46 (check_files_present)

 303           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA30F0, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 303>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object check_prior_phases_intact at 0x0000018C18061110, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 303>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              47 (check_prior_phases_intact)

 317           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA3F00, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 317>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object check_memory_review_intact at 0x0000018C18060DB0, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 317>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              48 (check_memory_review_intact)

 331           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA2010, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 331>)
               MAKE_FUNCTION
               LOAD_CONST              31 (<code object check_email_auth at 0x0000018C17ED9FB0, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 331>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              49 (check_email_auth)

 400           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA22E0, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 400>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object check_email_dedupe at 0x0000018C17EA3D00, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 400>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              50 (check_email_dedupe)

 456           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA24C0, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 456>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object check_service_signature_kwargs at 0x0000018C17E56850, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 456>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              51 (check_service_signature_kwargs)

 521           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C17FA25B0, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 521>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object check_route_signature_header at 0x0000018C17EA71A0, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 521>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              52 (check_route_signature_header)

 597           LOAD_CONST              38 (<code object __annotate__ at 0x0000018C17FA23D0, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 597>)
               MAKE_FUNCTION
               LOAD_CONST              39 (<code object check_event_contract at 0x0000018C17FEDC30, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 597>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              53 (check_event_contract)

 613           LOAD_CONST              40 (<code object __annotate__ at 0x0000018C17FA2D30, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 613>)
               MAKE_FUNCTION
               LOAD_CONST              41 (<code object check_no_forbidden_imports at 0x0000018C17D8BC50, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 613>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              54 (check_no_forbidden_imports)

 642           LOAD_CONST              42 (<code object __annotate__ at 0x0000018C17FA2A60, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 642>)
               MAKE_FUNCTION
               LOAD_CONST              43 (<code object check_no_inbox_scanning at 0x0000018C17CC2960, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 642>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              55 (check_no_inbox_scanning)

 669           LOAD_CONST              44 (<code object __annotate__ at 0x0000018C17FA2C40, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 669>)
               MAKE_FUNCTION
               LOAD_CONST              45 (<code object check_docs_required_doctrine at 0x0000018C17F746D0, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 669>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              56 (check_docs_required_doctrine)

 716           LOAD_CONST              46 (<code object __annotate__ at 0x0000018C17FA3690, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 716>)
               MAKE_FUNCTION
               LOAD_CONST              47 (<code object check_self_no_env_or_vendor at 0x0000018C17EA76C0, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 716>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              57 (check_self_no_env_or_vendor)

 766           LOAD_CONST              48 (<code object __annotate__ at 0x0000018C17FA3870, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 766>)
               MAKE_FUNCTION
               LOAD_CONST              49 (<code object _aggregate at 0x0000018C17EC57C0, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 766>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              58 (_aggregate)

 782           LOAD_CONST              50 (<code object __annotate__ at 0x0000018C17FA3000, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 782>)
               MAKE_FUNCTION
               LOAD_CONST              51 (<code object _operator_actions at 0x0000018C180483B0, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 782>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              59 (_operator_actions)

 792           LOAD_CONST              52 (<code object __annotate__ at 0x0000018C180FC210, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 792>)
               MAKE_FUNCTION
               LOAD_CONST              53 (<code object evaluate at 0x0000018C17ED88D0, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 792>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              60 (evaluate)

 823           LOAD_CONST              54 ('pas165_email_auth_dedupe_readiness_report.json')
               STORE_NAME              61 (REPORT_FILENAME)

 826           LOAD_CONST              55 (<code object __annotate__ at 0x0000018C180FC120, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 826>)
               MAKE_FUNCTION
               LOAD_CONST              56 (<code object _build_parser at 0x0000018C179A7290, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 826>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              62 (_build_parser)

 861           LOAD_CONST              57 (<code object __annotate__ at 0x0000018C180FC300, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 861>)
               MAKE_FUNCTION
               LOAD_CONST              58 (<code object _print_summary at 0x0000018C17D8E300, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 861>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              63 (_print_summary)

 879           LOAD_CONST              59 (<code object __annotate__ at 0x0000018C18025D30, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 879>)
               MAKE_FUNCTION
               LOAD_CONST              60 (<code object _write_report at 0x0000018C18104210, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 879>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              64 (_write_report)

 893           LOAD_CONST              77 ((None,))
               LOAD_CONST              61 (<code object __annotate__ at 0x0000018C180FCA80, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 893>)
               MAKE_FUNCTION
               LOAD_CONST              62 (<code object main at 0x0000018C17F83070, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 893>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              65 (main)

 921           LOAD_NAME               66 (__name__)
               LOAD_CONST              63 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 922           LOAD_NAME                6 (sys)
               LOAD_ATTR              134 (exit)
               PUSH_NULL
               LOAD_NAME               65 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 921   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  68           LOAD_NAME               18 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  69   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          331 (to L1)

  68   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026530, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 226>:
226           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('check_id')

227           LOAD_CONST               2 ('str')

226           LOAD_CONST               3 ('status')

227           LOAD_CONST               2 ('str')

226           LOAD_CONST               4 ('label')

227           LOAD_CONST               2 ('str')

226           LOAD_CONST               5 ('severity')

228           LOAD_CONST               2 ('str')

226           LOAD_CONST               6 ('detail')

228           LOAD_CONST               2 ('str')

226           LOAD_CONST               7 ('return')

229           LOAD_CONST               8 ('dict')

226           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _check at 0x0000018C17FA3E10, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 226>:
226           RESUME                   0

231           LOAD_CONST               0 ('id')
              LOAD_FAST_BORROW         0 (check_id)

232           LOAD_CONST               1 ('status')
              LOAD_FAST_BORROW         1 (status)

233           LOAD_CONST               2 ('label')
              LOAD_FAST_BORROW         2 (label)

234           LOAD_CONST               3 ('severity')
              LOAD_FAST_BORROW         3 (severity)

235           LOAD_CONST               4 ('detail')
              LOAD_FAST_BORROW         4 (detail)

230           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 239>:
239           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038DF0, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 239>:
239           RESUME                   0

240           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 243>:
243           RESUME                   0
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

Disassembly of <code object _read_text at 0x0000018C180533F0, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 243>:
 243           RESUME                   0

 244           NOP

 245   L1:     LOAD_FAST_BORROW         0 (path)
               LOAD_ATTR                1 (read_text + NULL|self)
               LOAD_CONST               0 ('utf-8')
               LOAD_CONST               1 ('replace')
               LOAD_CONST               2 (('encoding', 'errors'))
               CALL_KW                  2
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 246           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 247   L4:     POP_EXCEPT
               LOAD_CONST               3 (None)
               RETURN_VALUE

 246   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 250>:
250           RESUME                   0
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

Disassembly of <code object _strip_python_comments_and_strings at 0x0000018C17D8C200, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 250>:
250            RESUME                   0

251            BUILD_LIST               0
               STORE_FAST               1 (out)

252            LOAD_SMALL_INT           0
               LOAD_GLOBAL              1 (len + NULL)
               LOAD_FAST_BORROW         0 (src)
               CALL                     1
               STORE_FAST_STORE_FAST   50 (n, i)

253    L1:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (i, n)
               COMPARE_OP              18 (bool(<))
               EXTENDED_ARG             1
               POP_JUMP_IF_FALSE      282 (to L13)
               NOT_TAKEN

254            LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               BINARY_OP               26 ([])
               STORE_FAST               4 (ch)

255            LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               1 ('#')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       38 (to L3)
               NOT_TAKEN

256            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_CONST               2 ('\n')
               LOAD_FAST_BORROW         2 (i)
               CALL                     2
               STORE_FAST               5 (j)

257            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L2)
               NOT_TAKEN

258            JUMP_FORWARD           240 (to L13)

259    L2:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

260            JUMP_BACKWARD           59 (to L1)

261    L3:     LOAD_FAST_BORROW         0 (src)
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

262    L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               BINARY_SLICE
               STORE_FAST               6 (quote)

263            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 98 (quote, i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               CALL                     2
               STORE_FAST               7 (end)

264            LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L5)
               NOT_TAKEN

265            JUMP_FORWARD           138 (to L13)

266    L5:     LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

267            JUMP_BACKWARD          161 (to L1)

268    L6:     LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               7 (('"', "'"))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       92 (to L12)
               NOT_TAKEN

269            LOAD_FAST                4 (ch)
               STORE_FAST               6 (quote)

270            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               5 (j)

271    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (j, n)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       63 (to L11)
               NOT_TAKEN

272            LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
               BINARY_OP               26 ([])
               LOAD_CONST               5 ('\\')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       12 (to L8)
               NOT_TAKEN

273            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           2
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)

274            JUMP_BACKWARD           30 (to L7)

275    L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
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

276    L9:     JUMP_FORWARD            11 (to L11)

277   L10:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)
               JUMP_BACKWARD           68 (to L7)

278   L11:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

279            EXTENDED_ARG             1
               JUMP_BACKWARD          259 (to L1)

280   L12:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (ch)
               CALL                     1
               POP_TOP

281            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               2 (i)
               EXTENDED_ARG             1
               JUMP_BACKWARD          288 (to L1)

282   L13:     LOAD_CONST               6 ('')
               LOAD_ATTR                9 (join + NULL|self)
               LOAD_FAST_BORROW         1 (out)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 289>:
289           RESUME                   0
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

Disassembly of <code object check_files_present at 0x0000018C180606F0, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 289>:
289           RESUME                   0

290           BUILD_LIST               0
              STORE_FAST               1 (out)

291           LOAD_GLOBAL              0 (REQUIRED_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

292           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

293           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

294           LOAD_CONST               0 ('file:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

295           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

296   L3:     LOAD_CONST               3 ('Required PAS165 file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

297           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

298           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing')

293   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

291   L6:     END_FOR
              POP_ITER

300           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA30F0, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 303>:
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

Disassembly of <code object check_prior_phases_intact at 0x0000018C18061110, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 303>:
303           RESUME                   0

304           BUILD_LIST               0
              STORE_FAST               1 (out)

305           LOAD_GLOBAL              0 (PRIOR_PHASE_FILES)
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

308           LOAD_CONST               0 ('prior_phase:')
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

310   L3:     LOAD_CONST               3 ('Prior-phase readiness script intact: ')
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
      L4:     LOAD_CONST               5 ('missing — PAS165 must not delete')

307   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

305   L6:     END_FOR
              POP_ITER

314           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3F00, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 317>:
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

Disassembly of <code object check_memory_review_intact at 0x0000018C18060DB0, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 317>:
317           RESUME                   0

318           BUILD_LIST               0
              STORE_FAST               1 (out)

319           LOAD_GLOBAL              0 (MEMORY_REVIEW_FILES)
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

322           LOAD_CONST               0 ('memory_review_file:')
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

324   L3:     LOAD_CONST               3 ('Memory Review file present (PAS165 must not delete): ')
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
      L4:     LOAD_CONST               5 ('PAS165 must not delete Memory Review files')

321   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

319   L6:     END_FOR
              POP_ITER

328           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2010, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 331>:
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

Disassembly of <code object check_email_auth at 0x0000018C17ED9FB0, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 331>:
331            RESUME                   0

332            BUILD_LIST               0
               STORE_FAST               1 (out)

333            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('services')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('ingestion')
               BINARY_OP               11 (/)
               LOAD_CONST               3 ('email_auth.py')
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
               LOAD_CONST               4 ('')
       L1:     STORE_FAST               3 (src)

335            LOAD_GLOBAL              4 (REQUIRED_AUTH_FUNCTIONS)
               GET_ITER
       L2:     FOR_ITER                92 (to L7)
               STORE_FAST               4 (needle)

336            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (needle, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

337            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

338            LOAD_CONST               5 ('auth_fn:')
               LOAD_FAST_BORROW         4 (needle)
               LOAD_CONST               6 (slice(None, 40, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

339            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               8 ('FAIL')

340    L4:     LOAD_CONST               9 ('Email auth function present: ')
               LOAD_FAST_BORROW         4 (needle)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0
               FORMAT_SIMPLE
               BUILD_STRING             2

341            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

342            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST              10 ('missing def: ')
               LOAD_FAST_BORROW         4 (needle)
               FORMAT_SIMPLE
               BUILD_STRING             2

337    L6:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           94 (to L2)

335    L7:     END_FOR
               POP_ITER

345            LOAD_CONST              12 ('hmac.compare_digest')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L8)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              13 ('compare_digest')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
       L8:     STORE_FAST               6 (ct_ok)

346            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

347            LOAD_CONST              14 ('auth:constant_time_compare')

348            LOAD_FAST_BORROW         6 (ct_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L10)
       L9:     LOAD_CONST               8 ('FAIL')

349   L10:     LOAD_CONST              15 ('Email auth uses constant-time signature compare')

350            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

351            LOAD_FAST_BORROW         6 (ct_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST              16 ('missing hmac.compare_digest')

346   L12:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

357            LOAD_CONST              17 ('hashlib.sha256(')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        14 (to L13)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              18 ('sha256(')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        6 (to L14)
               NOT_TAKEN
      L13:     POP_TOP

358            LOAD_CONST              19 ('body')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

356   L14:     STORE_FAST               7 (hashes_body)

360            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

361            LOAD_CONST              20 ('auth:canonical_hashes_body')

362            LOAD_FAST_BORROW         7 (hashes_body)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L15)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L16)
      L15:     LOAD_CONST               8 ('FAIL')

363   L16:     LOAD_CONST              21 ('Canonical payload hashes the body before inclusion')

364            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

365            LOAD_FAST_BORROW         7 (hashes_body)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L17)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L18)
      L17:     LOAD_CONST              22 ('expected sha256(body) in canonical builder')

360   L18:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

369            LOAD_CONST              23 ('_BODY_HASH_CAP_BYTES')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        19 (to L19)
               NOT_TAKEN
               POP_TOP

370            LOAD_CONST              24 ('65536')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

369            COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L19)
               NOT_TAKEN
               POP_TOP

371            LOAD_CONST              25 ('64 * 1024')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

368   L19:     STORE_FAST               8 (cap_ok)

373            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

374            LOAD_CONST              26 ('auth:body_cap_present')

375            LOAD_FAST_BORROW         8 (cap_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L20)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L21)
      L20:     LOAD_CONST               8 ('FAIL')

376   L21:     LOAD_CONST              27 ('Email auth caps body before hashing')

377            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

378            LOAD_FAST_BORROW         8 (cap_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L22)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L23)
      L22:     LOAD_CONST              28 ('expected body cap constant')

373   L23:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

382            LOAD_CONST              29 ('forwarder_signature_unconfigured')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       32 (to L24)
               NOT_TAKEN
               POP_TOP

383            LOAD_CONST              30 ('forwarder_signature_missing')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

382            COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       19 (to L24)
               NOT_TAKEN
               POP_TOP

384            LOAD_CONST              31 ('forwarder_signature_invalid')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

382            COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        6 (to L24)
               NOT_TAKEN
               POP_TOP

385            LOAD_CONST              32 ('forwarder_signature_malformed')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

381   L24:     STORE_FAST               9 (soft_tokens)

387            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

388            LOAD_CONST              33 ('auth:soft_rollout_tokens')

389            LOAD_FAST_BORROW         9 (soft_tokens)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L25)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L26)
      L25:     LOAD_CONST               8 ('FAIL')

390   L26:     LOAD_CONST              34 ('Email auth surfaces structural soft-rollout tokens')

391            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

392            LOAD_FAST_BORROW         9 (soft_tokens)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L27)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L28)

393   L27:     LOAD_CONST              35 ('expected forwarder_signature_(unconfigured|missing|invalid|malformed)')

387   L28:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

397            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA22E0, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 400>:
400           RESUME                   0
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

Disassembly of <code object check_email_dedupe at 0x0000018C17EA3D00, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 400>:
400            RESUME                   0

401            BUILD_LIST               0
               STORE_FAST               1 (out)

402            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('services')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('ingestion')
               BINARY_OP               11 (/)
               LOAD_CONST               3 ('email_dedupe.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

403            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')
       L1:     STORE_FAST               3 (src)

404            LOAD_GLOBAL              4 (REQUIRED_DEDUPE_FUNCTIONS)
               GET_ITER
       L2:     FOR_ITER                92 (to L7)
               STORE_FAST               4 (needle)

405            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (needle, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

406            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

407            LOAD_CONST               5 ('dedupe_fn:')
               LOAD_FAST_BORROW         4 (needle)
               LOAD_CONST               6 (slice(None, 40, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

408            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               8 ('FAIL')

409    L4:     LOAD_CONST               9 ('Email dedupe function present: ')
               LOAD_FAST_BORROW         4 (needle)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0
               FORMAT_SIMPLE
               BUILD_STRING             2

410            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

411            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST              10 ('missing def: ')
               LOAD_FAST_BORROW         4 (needle)
               FORMAT_SIMPLE
               BUILD_STRING             2

406    L6:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           94 (to L2)

404    L7:     END_FOR
               POP_ITER

415            LOAD_CONST              12 ('DEDUPE_TTL_SECONDS = 24 * 60 * 60')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L8)
               NOT_TAKEN
               POP_TOP

416            LOAD_CONST              13 ('DEDUPE_TTL_SECONDS = 86400')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

414    L8:     STORE_FAST               6 (ttl_ok)

418            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

419            LOAD_CONST              14 ('dedupe:ttl_24_hours')

420            LOAD_FAST_BORROW         6 (ttl_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L10)
       L9:     LOAD_CONST               8 ('FAIL')

421   L10:     LOAD_CONST              15 ('Dedupe TTL is 24 hours')

422            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

423            LOAD_FAST_BORROW         6 (ttl_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST              16 ('DEDUPE_TTL_SECONDS != 24*60*60')

418   L12:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

426            LOAD_CONST              17 ('_DEDUPE_REGISTRY')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               STORE_FAST               7 (registry_ok)

427            LOAD_CONST              18 ('RLock')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L13)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              19 ('threading.RLock')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
      L13:     STORE_FAST               8 (lock_ok)

428            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

429            LOAD_CONST              20 ('dedupe:process_local_registry')

430            LOAD_FAST_BORROW         7 (registry_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L14)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L15)
      L14:     LOAD_CONST               8 ('FAIL')

431   L15:     LOAD_CONST              21 ('Dedupe registry is process-local')

432            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

433            LOAD_FAST_BORROW         7 (registry_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L16)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L17)
      L16:     LOAD_CONST              22 ('missing _DEDUPE_REGISTRY')

428   L17:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

435            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

436            LOAD_CONST              23 ('dedupe:rlock_protected')

437            LOAD_FAST_BORROW         8 (lock_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L18)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L19)
      L18:     LOAD_CONST               8 ('FAIL')

438   L19:     LOAD_CONST              24 ('Dedupe registry uses RLock for thread-safety')

439            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

440            LOAD_FAST_BORROW         8 (lock_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L20)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L21)
      L20:     LOAD_CONST              25 ('missing threading.RLock')

435   L21:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

443            LOAD_GLOBAL             15 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               9 (executable)

444            LOAD_CONST              26 ('brokerage_id')
               LOAD_FAST_BORROW         9 (executable)
               CONTAINS_OP              0 (in)
               STORE_FAST              10 (bid_in_key)

445            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

446            LOAD_CONST              27 ('dedupe:no_brokerage_id_in_key')

447            LOAD_FAST_BORROW        10 (bid_in_key)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L22)
               NOT_TAKEN
               LOAD_CONST               8 ('FAIL')
               JUMP_FORWARD             1 (to L23)
      L22:     LOAD_CONST               7 ('PASS')

448   L23:     LOAD_CONST              28 ('Dedupe key derivation never includes brokerage_id')

449            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

451            LOAD_FAST_BORROW        10 (bid_in_key)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L24)
               NOT_TAKEN

450            LOAD_CONST              29 ('brokerage_id appears in dedupe executable')
               JUMP_FORWARD             1 (to L25)

451   L24:     LOAD_CONST               4 ('')

445   L25:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

453            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA24C0, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 456>:
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

Disassembly of <code object check_service_signature_kwargs at 0x0000018C17E56850, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 456>:
  --            MAKE_CELL               11 (src)

 456            RESUME                   0

 457            BUILD_LIST               0
                STORE_FAST               1 (out)

 458            LOAD_GLOBAL              1 (Path + NULL)
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

 459            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (p)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               4 ('')
        L1:     STORE_DEREF             11 (src)

 461            LOAD_GLOBAL              4 (REQUIRED_SERVICE_SIGNATURE_TOKENS)
                GET_ITER
        L2:     FOR_ITER                72 (to L7)
                STORE_FAST               3 (kw)

 462            LOAD_FAST_BORROW         3 (kw)
                LOAD_DEREF              11 (src)
                CONTAINS_OP              0 (in)
                STORE_FAST               4 (ok)

 463            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 464            LOAD_CONST               5 ('service_kw:')
                LOAD_FAST_BORROW         3 (kw)
                FORMAT_SIMPLE
                BUILD_STRING             2

 465            LOAD_FAST_BORROW         4 (ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L3)
                NOT_TAKEN
                LOAD_CONST               6 ('PASS')
                JUMP_FORWARD             1 (to L4)
        L3:     LOAD_CONST               7 ('FAIL')

 466    L4:     LOAD_CONST               8 ('ingest_email_lead accepts ')
                LOAD_FAST_BORROW         3 (kw)
                FORMAT_SIMPLE
                BUILD_STRING             2

 467            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 468            LOAD_FAST_BORROW         4 (ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN
                LOAD_CONST               4 ('')
                JUMP_FORWARD             4 (to L6)
        L5:     LOAD_CONST               9 ('missing kwarg ')
                LOAD_FAST_BORROW         3 (kw)
                FORMAT_SIMPLE
                BUILD_STRING             2

 463    L6:     LOAD_CONST              10 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           74 (to L2)

 461    L7:     END_FOR
                POP_ITER

 472            LOAD_CONST              11 ('verify_forwarder_signature')
                LOAD_DEREF              11 (src)
                CONTAINS_OP              0 (in)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         6 (to L8)
                NOT_TAKEN
                POP_TOP

 473            LOAD_CONST              12 ('from app.services.ingestion.email_auth')
                LOAD_DEREF              11 (src)
                CONTAINS_OP              0 (in)

 471    L8:     STORE_FAST               5 (auth_ref)

 475            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 476            LOAD_CONST              13 ('service:uses_email_auth')

 477            LOAD_FAST_BORROW         5 (auth_ref)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L9)
                NOT_TAKEN
                LOAD_CONST               6 ('PASS')
                JUMP_FORWARD             1 (to L10)
        L9:     LOAD_CONST               7 ('FAIL')

 478   L10:     LOAD_CONST              14 ('Service references email_auth.verify_forwarder_signature')

 479            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 480            LOAD_FAST_BORROW         5 (auth_ref)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L11)
                NOT_TAKEN
                LOAD_CONST               4 ('')
                JUMP_FORWARD             1 (to L12)
       L11:     LOAD_CONST              15 ('verify_forwarder_signature not referenced')

 475   L12:     LOAD_CONST              10 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 484            LOAD_CONST              16 ('build_email_dedupe_key')
                LOAD_DEREF              11 (src)
                CONTAINS_OP              0 (in)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        6 (to L13)
                NOT_TAKEN
                POP_TOP

 485            LOAD_CONST              17 ('register_email_lead_dedupe')
                LOAD_DEREF              11 (src)
                CONTAINS_OP              0 (in)

 483   L13:     STORE_FAST               6 (dedupe_ref)

 487            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 488            LOAD_CONST              18 ('service:uses_email_dedupe')

 489            LOAD_FAST_BORROW         6 (dedupe_ref)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L14)
                NOT_TAKEN
                LOAD_CONST               6 ('PASS')
                JUMP_FORWARD             1 (to L15)
       L14:     LOAD_CONST               7 ('FAIL')

 490   L15:     LOAD_CONST              19 ('Service references email_dedupe build/register helpers')

 491            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 492            LOAD_FAST_BORROW         6 (dedupe_ref)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L16)
                NOT_TAKEN
                LOAD_CONST               4 ('')
                JUMP_FORWARD             1 (to L17)
       L16:     LOAD_CONST              20 ('dedupe helpers not referenced')

 487   L17:     LOAD_CONST              10 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 495            LOAD_GLOBAL             12 (REQUIRED_RESPONSE_FIELDS)
                GET_ITER
       L18:     FOR_ITER               138 (to L28)
                STORE_FAST               7 (field)

 497            LOAD_CONST              21 ('"')
                LOAD_FAST_BORROW         7 (field)
                FORMAT_SIMPLE
                LOAD_CONST              22 ('":')
                BUILD_STRING             3
                LOAD_CONST              23 ("'")
                LOAD_FAST_BORROW         7 (field)
                FORMAT_SIMPLE
                LOAD_CONST              24 ("':")
                BUILD_STRING             3
                BUILD_TUPLE              2
                STORE_FAST               8 (bad_shapes)

 498            LOAD_GLOBAL             14 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L22)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW        11 (src)
                BUILD_TUPLE              1
                LOAD_CONST              25 (<code object <genexpr> at 0x0000018C18024C30, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 498>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         8 (bad_shapes)
                GET_ITER
                CALL                     0
       L19:     FOR_ITER                12 (to L21)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L20)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L19)
       L20:     POP_ITER
                LOAD_CONST              26 (True)
                JUMP_FORWARD            20 (to L23)
       L21:     END_FOR
                POP_ITER
                LOAD_CONST              27 (False)
                JUMP_FORWARD            16 (to L23)
       L22:     PUSH_NULL
                LOAD_FAST_BORROW        11 (src)
                BUILD_TUPLE              1
                LOAD_CONST              25 (<code object <genexpr> at 0x0000018C18024C30, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 498>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         8 (bad_shapes)
                GET_ITER
                CALL                     0
                CALL                     1
       L23:     STORE_FAST               9 (present)

 499            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 500            LOAD_CONST              28 ('service:response_field:')
                LOAD_FAST_BORROW         7 (field)
                FORMAT_SIMPLE
                BUILD_STRING             2

 501            LOAD_FAST_BORROW         9 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L24)
                NOT_TAKEN
                LOAD_CONST               6 ('PASS')
                JUMP_FORWARD             1 (to L25)
       L24:     LOAD_CONST               7 ('FAIL')

 502   L25:     LOAD_CONST              29 ('Service response includes field: ')
                LOAD_FAST_BORROW         7 (field)
                FORMAT_SIMPLE
                BUILD_STRING             2

 503            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 504            LOAD_FAST_BORROW         9 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L26)
                NOT_TAKEN
                LOAD_CONST               4 ('')
                JUMP_FORWARD             5 (to L27)
       L26:     LOAD_CONST              30 ('missing response key ')
                LOAD_FAST_BORROW         7 (field)
                CONVERT_VALUE            2 (repr)
                FORMAT_SIMPLE
                BUILD_STRING             2

 499   L27:     LOAD_CONST              10 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          140 (to L18)

 495   L28:     END_FOR
                POP_ITER

 507            LOAD_GLOBAL             16 (FORBIDDEN_RESPONSE_KEYS)
                GET_ITER
       L29:     FOR_ITER               139 (to L39)
                STORE_FAST              10 (forbidden)

 508            LOAD_CONST              21 ('"')
                LOAD_FAST_BORROW        10 (forbidden)
                FORMAT_SIMPLE
                LOAD_CONST              22 ('":')
                BUILD_STRING             3
                LOAD_CONST              23 ("'")
                LOAD_FAST_BORROW        10 (forbidden)
                FORMAT_SIMPLE
                LOAD_CONST              24 ("':")
                BUILD_STRING             3
                BUILD_TUPLE              2
                STORE_FAST               8 (bad_shapes)

 509            LOAD_GLOBAL             14 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L33)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW        11 (src)
                BUILD_TUPLE              1
                LOAD_CONST              31 (<code object <genexpr> at 0x0000018C18024930, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 509>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         8 (bad_shapes)
                GET_ITER
                CALL                     0
       L30:     FOR_ITER                12 (to L32)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L31)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L30)
       L31:     POP_ITER
                LOAD_CONST              26 (True)
                JUMP_FORWARD            20 (to L34)
       L32:     END_FOR
                POP_ITER
                LOAD_CONST              27 (False)
                JUMP_FORWARD            16 (to L34)
       L33:     PUSH_NULL
                LOAD_FAST_BORROW        11 (src)
                BUILD_TUPLE              1
                LOAD_CONST              31 (<code object <genexpr> at 0x0000018C18024930, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 509>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         8 (bad_shapes)
                GET_ITER
                CALL                     0
                CALL                     1
       L34:     STORE_FAST               9 (present)

 510            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 511            LOAD_CONST              32 ('service:no_forbidden_response_key:')
                LOAD_FAST_BORROW        10 (forbidden)
                FORMAT_SIMPLE
                BUILD_STRING             2

 512            LOAD_FAST_BORROW         9 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L35)
                NOT_TAKEN
                LOAD_CONST               7 ('FAIL')
                JUMP_FORWARD             1 (to L36)
       L35:     LOAD_CONST               6 ('PASS')

 513   L36:     LOAD_CONST              33 ('Service excludes forbidden response key: ')
                LOAD_FAST_BORROW        10 (forbidden)
                FORMAT_SIMPLE
                BUILD_STRING             2

 514            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 516            LOAD_FAST_BORROW         9 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        8 (to L37)
                NOT_TAKEN

 515            LOAD_CONST              34 ('forbidden response key ')
                LOAD_FAST_BORROW        10 (forbidden)
                CONVERT_VALUE            2 (repr)
                FORMAT_SIMPLE
                LOAD_CONST              35 (' present')
                BUILD_STRING             3
                JUMP_FORWARD             1 (to L38)

 516   L37:     LOAD_CONST               4 ('')

 510   L38:     LOAD_CONST              10 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          141 (to L29)

 507   L39:     END_FOR
                POP_ITER

 518            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18024C30, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 498>:
  --           COPY_FREE_VARS           1

 498           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C18024930, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 509>:
  --           COPY_FREE_VARS           1

 509           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA25B0, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 521>:
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

Disassembly of <code object check_route_signature_header at 0x0000018C17EA71A0, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 521>:
521            RESUME                   0

522            BUILD_LIST               0
               STORE_FAST               1 (out)

523            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('routes')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('email_ingestion.py')
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
               LOAD_CONST               3 ('')
       L1:     STORE_FAST               3 (src)

526            LOAD_GLOBAL              4 (REQUIRED_ROUTE_DECLS)
               GET_ITER
       L2:     FOR_ITER                71 (to L7)
               STORE_FAST               4 (decl)

527            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (decl, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (present)

528            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

529            LOAD_CONST               4 ('route_decl:')
               LOAD_FAST_BORROW         4 (decl)
               FORMAT_SIMPLE
               BUILD_STRING             2

530            LOAD_FAST_BORROW         5 (present)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               6 ('FAIL')

531    L4:     LOAD_CONST               7 ('Route declaration present: ')
               LOAD_FAST_BORROW         4 (decl)
               FORMAT_SIMPLE
               BUILD_STRING             2

532            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

533            LOAD_FAST_BORROW         5 (present)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               3 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST               8 ('missing decl: ')
               LOAD_FAST_BORROW         4 (decl)
               FORMAT_SIMPLE
               BUILD_STRING             2

528    L6:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           73 (to L2)

526    L7:     END_FOR
               POP_ITER

536            LOAD_CONST              10 ('X-Forwarder-Signature')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               STORE_FAST               6 (header_ok)

537            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

538            LOAD_CONST              11 ('route:accepts_forwarder_signature_header')

539            LOAD_FAST_BORROW         6 (header_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST               6 ('FAIL')

540    L9:     LOAD_CONST              12 ('Route accepts X-Forwarder-Signature header')

541            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

542            LOAD_FAST_BORROW         6 (header_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST               3 ('')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST              13 ('missing X-Forwarder-Signature reference')

537   L11:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

545            LOAD_CONST              14 ('forwarder_signature=')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               STORE_FAST               7 (fwd_sig)

546            LOAD_CONST              15 ('forwarder_secret=')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               STORE_FAST               8 (fwd_sec)

547            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

548            LOAD_CONST              16 ('route:passes_forwarder_signature')

549            LOAD_FAST_BORROW         7 (fwd_sig)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L12)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L13)
      L12:     LOAD_CONST               6 ('FAIL')

550   L13:     LOAD_CONST              17 ('Route passes forwarder_signature kwarg to service')

551            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

552            LOAD_FAST_BORROW         7 (fwd_sig)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L14)
               NOT_TAKEN
               LOAD_CONST               3 ('')
               JUMP_FORWARD             1 (to L15)
      L14:     LOAD_CONST              18 ('forwarder_signature= not passed to service')

547   L15:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

554            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

555            LOAD_CONST              19 ('route:passes_forwarder_secret')

556            LOAD_FAST_BORROW         8 (fwd_sec)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L16)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L17)
      L16:     LOAD_CONST               6 ('FAIL')

557   L17:     LOAD_CONST              20 ('Route passes forwarder_secret kwarg to service')

558            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

559            LOAD_FAST_BORROW         8 (fwd_sec)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L18)
               NOT_TAKEN
               LOAD_CONST               3 ('')
               JUMP_FORWARD             1 (to L19)
      L18:     LOAD_CONST              21 ('forwarder_secret= not passed to service')

554   L19:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

562            LOAD_GLOBAL             13 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               9 (executable)

563            LOAD_CONST              33 (('body.brokerage_id', 'body["brokerage_id"]', "body['brokerage_id']"))
               GET_ITER
      L20:     FOR_ITER                80 (to L25)
               STORE_FAST              10 (bad_pattern)

568            LOAD_FAST_BORROW_LOAD_FAST_BORROW 169 (bad_pattern, executable)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (present)

569            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

570            LOAD_CONST              22 ('route:no_body_trust:')
               LOAD_FAST_BORROW        10 (bad_pattern)
               LOAD_CONST              23 (slice(None, 40, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

571            LOAD_FAST_BORROW         5 (present)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L21)
               NOT_TAKEN
               LOAD_CONST               6 ('FAIL')
               JUMP_FORWARD             1 (to L22)
      L21:     LOAD_CONST               5 ('PASS')

572   L22:     LOAD_CONST              24 ('Route never reads brokerage_id from body: ')
               LOAD_FAST_BORROW        10 (bad_pattern)
               FORMAT_SIMPLE
               BUILD_STRING             2

573            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

575            LOAD_FAST_BORROW         5 (present)
               TO_BOOL
               POP_JUMP_IF_FALSE        8 (to L23)
               NOT_TAKEN

574            LOAD_CONST              25 ('body-trust pattern ')
               LOAD_FAST_BORROW        10 (bad_pattern)
               CONVERT_VALUE            2 (repr)
               FORMAT_SIMPLE
               LOAD_CONST              26 (' present')
               BUILD_STRING             3
               JUMP_FORWARD             1 (to L24)

575   L23:     LOAD_CONST               3 ('')

569   L24:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           82 (to L20)

563   L25:     END_FOR
               POP_ITER

578            LOAD_FAST_BORROW         3 (src)
               LOAD_ATTR               15 (find + NULL|self)
               LOAD_CONST              27 ('_EVENT_PAYLOAD_ALLOWED')
               CALL                     1
               STORE_FAST              11 (allow_list_idx)

579            LOAD_FAST_BORROW        11 (allow_list_idx)
               LOAD_SMALL_INT           0
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE       13 (to L26)
               NOT_TAKEN

580            LOAD_FAST_BORROW_LOAD_FAST_BORROW 59 (src, allow_list_idx)
               LOAD_FAST_BORROW        11 (allow_list_idx)
               LOAD_CONST              28 (1024)
               BINARY_OP                0 (+)
               BINARY_SLICE
               STORE_FAST              12 (allow_window)
               JUMP_FORWARD             2 (to L27)

582   L26:     LOAD_CONST               3 ('')
               STORE_FAST              12 (allow_window)

583   L27:     LOAD_GLOBAL             16 (FORBIDDEN_EVENT_PAYLOAD_KEYS)
               GET_ITER
      L28:     FOR_ITER                79 (to L33)
               STORE_FAST              13 (forbidden)

584            LOAD_CONST              29 ('"')
               LOAD_FAST_BORROW        13 (forbidden)
               FORMAT_SIMPLE
               LOAD_CONST              29 ('"')
               BUILD_STRING             3
               STORE_FAST              14 (candidate)

585            LOAD_FAST_BORROW_LOAD_FAST_BORROW 236 (candidate, allow_window)
               CONTAINS_OP              0 (in)
               STORE_FAST              15 (present_in_allowed)

586            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

587            LOAD_CONST              30 ('route:event_allowlist_excludes:')
               LOAD_FAST_BORROW        13 (forbidden)
               FORMAT_SIMPLE
               BUILD_STRING             2

588            LOAD_FAST_BORROW        15 (present_in_allowed)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L29)
               NOT_TAKEN
               LOAD_CONST               6 ('FAIL')
               JUMP_FORWARD             1 (to L30)
      L29:     LOAD_CONST               5 ('PASS')

589   L30:     LOAD_CONST              31 ('Event payload allow-list excludes forbidden key: ')
               LOAD_FAST_BORROW        13 (forbidden)
               FORMAT_SIMPLE
               BUILD_STRING             2

590            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

592            LOAD_FAST_BORROW        15 (present_in_allowed)
               TO_BOOL
               POP_JUMP_IF_FALSE        8 (to L31)
               NOT_TAKEN

591            LOAD_CONST              32 ('forbidden allow-list key ')
               LOAD_FAST_BORROW        13 (forbidden)
               CONVERT_VALUE            2 (repr)
               FORMAT_SIMPLE
               LOAD_CONST              26 (' present')
               BUILD_STRING             3
               JUMP_FORWARD             1 (to L32)

592   L31:     LOAD_CONST               3 ('')

586   L32:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           81 (to L28)

583   L33:     END_FOR
               POP_ITER

594            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 597>:
597           RESUME                   0
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

Disassembly of <code object check_event_contract at 0x0000018C17FEDC30, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 597>:
597           RESUME                   0

598           BUILD_LIST               0
              STORE_FAST               1 (out)

599           LOAD_GLOBAL              1 (Path + NULL)
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

600           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

601           LOAD_GLOBAL              4 (REQUIRED_EVENT_TYPES)
              GET_ITER
      L2:     FOR_ITER                72 (to L7)
              STORE_FAST               4 (required)

602           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (required, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

603           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

604           LOAD_CONST               5 ('events:')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

605           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               6 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               7 ('FAIL')

606   L4:     LOAD_CONST               8 ('Event contract registers ')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

607           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

608           LOAD_FAST_BORROW         5 (ok)
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

603   L6:     LOAD_CONST              10 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           74 (to L2)

601   L7:     END_FOR
              POP_ITER

610           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 613>:
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

Disassembly of <code object check_no_forbidden_imports at 0x0000018C17D8BC50, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 613>:
613            RESUME                   0

614            BUILD_LIST               0
               STORE_FAST               1 (out)

615            LOAD_CONST               9 (('app/services/ingestion/email_auth.py', 'app/services/ingestion/email_dedupe.py', 'app/services/ingestion/email_ingestion.py', 'app/routes/email_ingestion.py', 'scripts/pas165_email_auth_dedupe_readiness_check.py'))
               STORE_FAST               2 (files)

622            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               241 (to L12)
               STORE_FAST               3 (relpath)

623            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

624            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L2:     STORE_FAST               5 (src)

625            BUILD_LIST               0
               STORE_FAST               6 (bad)

626            LOAD_FAST_BORROW         5 (src)
               LOAD_ATTR                5 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L3:     FOR_ITER                74 (to L7)
               STORE_FAST               7 (line)

627            LOAD_FAST_BORROW         7 (line)
               LOAD_ATTR                7 (strip + NULL|self)
               CALL                     0
               STORE_FAST               8 (stripped)

628            LOAD_GLOBAL              8 (FORBIDDEN_IMPORT_LINE_PREFIXES)
               GET_ITER
       L4:     FOR_ITER                45 (to L6)
               STORE_FAST               9 (prefix)

629            LOAD_FAST_BORROW         8 (stripped)
               LOAD_ATTR               11 (startswith + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           28 (to L4)

630    L5:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR               13 (append + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           47 (to L4)

628    L6:     END_FOR
               POP_ITER
               JUMP_BACKWARD           76 (to L3)

626    L7:     END_FOR
               POP_ITER

631            LOAD_FAST                1 (out)
               LOAD_ATTR               13 (append + NULL|self)
               LOAD_GLOBAL             15 (_check + NULL)

632            LOAD_CONST               2 ('forbidden_import:')
               LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR               16 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

633            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST               4 ('PASS')

634    L9:     LOAD_CONST               5 ('No forbidden imports: ')
               LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR               16 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

635            LOAD_GLOBAL             18 (SEVERITY_BLOCK)

637            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L10)
               NOT_TAKEN

636            LOAD_CONST               6 ('forbidden import prefixes: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               21 (join + NULL|self)
               LOAD_FAST_BORROW         6 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L11)

637   L10:     LOAD_CONST               1 ('')

631   L11:     LOAD_CONST               8 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          243 (to L1)

622   L12:     END_FOR
               POP_ITER

639            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 642>:
642           RESUME                   0
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

Disassembly of <code object check_no_inbox_scanning at 0x0000018C17CC2960, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 642>:
642            RESUME                   0

643            BUILD_LIST               0
               STORE_FAST               1 (out)

644            LOAD_CONST               9 (('app/services/ingestion/email_auth.py', 'app/services/ingestion/email_dedupe.py', 'app/services/ingestion/email_ingestion.py', 'app/routes/email_ingestion.py'))
               STORE_FAST               2 (files)

650            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               196 (to L10)
               STORE_FAST               3 (relpath)

651            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

652            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L2:     STORE_FAST               5 (src)

653            LOAD_GLOBAL              5 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         5 (src)
               CALL                     1
               STORE_FAST               6 (executable)

654            BUILD_LIST               0
               STORE_FAST               7 (bad)

655            LOAD_GLOBAL              6 (FORBIDDEN_INBOX_TOKENS)
               GET_ITER
       L3:     FOR_ITER                28 (to L5)
               STORE_FAST               8 (token)

656            LOAD_FAST_BORROW_LOAD_FAST_BORROW 134 (token, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L3)

657    L4:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_FAST_BORROW         8 (token)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L3)

655    L5:     END_FOR
               POP_ITER

658            LOAD_FAST                1 (out)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_GLOBAL             11 (_check + NULL)

659            LOAD_CONST               2 ('no_inbox_scan:')
               LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR               12 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

660            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L6)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L7)
       L6:     LOAD_CONST               4 ('PASS')

661    L7:     LOAD_CONST               5 ('No inbox-scanning tokens: ')
               LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR               12 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

662            LOAD_GLOBAL             14 (SEVERITY_BLOCK)

664            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L8)
               NOT_TAKEN

663            LOAD_CONST               6 ('inbox-scan tokens present: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               17 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L9)

664    L8:     LOAD_CONST               1 ('')

658    L9:     LOAD_CONST               8 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          198 (to L1)

650   L10:     END_FOR
               POP_ITER

666            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 669>:
669           RESUME                   0
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

Disassembly of <code object check_docs_required_doctrine at 0x0000018C17F746D0, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 669>:
  --            MAKE_CELL                8 (lower)

 669            RESUME                   0

 670            BUILD_LIST               0
                STORE_FAST               1 (out)

 671            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('docs')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('pas165_email_forwarder_auth_and_dedupe.md')
                BINARY_OP               11 (/)
                STORE_FAST               2 (doc)

 672            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (doc)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L1:     STORE_FAST               3 (src)

 673            LOAD_FAST_BORROW         3 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_DEREF              8 (lower)

 674            LOAD_CONST              13 ((('purpose', ('purpose',)), ('relationship-pas164', ('pas164',)), ('why-dedupe', ('why dedupe', 'duplicate', 'dedupe matters')), ('why-auth', ('forwarder auth', 'signature', 'signing')), ('signing-algorithm', ('sha256', 'hmac')), ('canonical-payload', ('canonical payload',)), ('header-format', ('x-forwarder-signature', 'sha256=')), ('soft-rollout', ('soft-rollout', 'soft rollout', 'soft pass', 'ingestion still allowed')), ('invalid-rejected', ('invalid signature', 'rejected', 'hard fail', 'forwarder_signature_invalid')), ('dedupe-algorithm', ('dedupe key', 'dedupe algorithm', 'build_email_dedupe_key')), ('ttl', ('ttl', '24 hour', '24-hour')), ('process-local', ('process-local', 'process local', 'in-memory', 'not durable')), ('response-shape', ('response shape', 'response', 'duplicate', 'forwarder_verified')), ('event-safety', ('event payload safety', 'event payload')), ('no-raw-storage', ('no raw email', 'raw email body', 'no raw body')), ('no-gmail', ('no gmail oauth', 'no gmail')), ('no-inbox-scan', ('no inbox scanning', 'no inbox')), ('not-built', ('intentionally not built', 'deliberately not', 'what is intentionally')), ('brokerage-pilots', ('brokerage pilot', 'real brokerage', 'brokerage demos'))))
                STORE_FAST               4 (required_phrases)

 703            LOAD_FAST_BORROW         4 (required_phrases)
                GET_ITER
        L2:     FOR_ITER               146 (to L12)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   86 (name, phrases)

 704            LOAD_GLOBAL              6 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         8 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18026430, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 704>)
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
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18026430, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 704>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         6 (phrases)
                GET_ITER
                CALL                     0
                CALL                     1
        L7:     STORE_FAST               7 (present)

 705            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 706            LOAD_CONST               6 ('docs:phrase:')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 707            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               8 ('FAIL')

 708    L9:     LOAD_CONST               9 ('Doc carries clause: ')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 709            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 711            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L10)
                NOT_TAKEN

 710            LOAD_CONST              10 ('expected one of: ')
                LOAD_CONST              11 (' | ')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_FAST_BORROW         6 (phrases)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L11)

 711   L10:     LOAD_CONST               2 ('')

 705   L11:     LOAD_CONST              12 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          148 (to L2)

 703   L12:     END_FOR
                POP_ITER

 713            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18026430, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 704>:
  --           COPY_FREE_VARS           1

 704           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 716>:
716           RESUME                   0
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

Disassembly of <code object check_self_no_env_or_vendor at 0x0000018C17EA76C0, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 716>:
716            RESUME                   0

717            BUILD_LIST               0
               STORE_FAST               1 (out)

718            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_GLOBAL              2 (__file__)
               CALL                     1
               LOAD_ATTR                5 (resolve + NULL|self)
               CALL                     0
               STORE_FAST               2 (self_path)

719            LOAD_GLOBAL              7 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (self_path)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L1:     STORE_FAST               3 (src)

720            BUILD_LIST               0
               STORE_FAST               4 (bad)

721            LOAD_FAST_BORROW         3 (src)
               LOAD_ATTR                9 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L2:     EXTENDED_ARG             1
               FOR_ITER               311 (to L11)
               STORE_FAST               5 (raw_line)

722            LOAD_FAST_BORROW         5 (raw_line)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0
               STORE_FAST               6 (stripped)

723            LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST               1 ('#')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

724            JUMP_BACKWARD           45 (to L2)

725    L3:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              16 (('import dotenv', 'from dotenv'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L4)
               NOT_TAKEN

726            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               2 ('dotenv import')
               CALL                     1
               POP_TOP

727    L4:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              17 (('import supabase', 'from supabase'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L5)
               NOT_TAKEN

728            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               3 ('supabase import')
               CALL                     1
               POP_TOP

729    L5:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              18 (('import composio', 'from composio', 'import trustclaw', 'from trustclaw', 'import openai', 'from openai', 'import anthropic', 'from anthropic', 'import googleapiclient', 'from googleapiclient', 'import google.oauth2', 'from google.oauth2'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L6)
               NOT_TAKEN

737            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               4 ('external-vendor / google import')
               CALL                     1
               POP_TOP

738    L6:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              19 (('import numpy', 'import faiss', 'import pgvector', 'from pgvector', 'from openai import embeddings', 'from openai.embeddings'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L7)
               NOT_TAKEN

744            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               5 ('embedding / vector import')
               CALL                     1
               POP_TOP

745    L7:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST               6 ('load_dotenv()')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        24 (to L8)
               NOT_TAKEN

746            LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               17 (endswith + NULL|self)
               LOAD_CONST               6 ('load_dotenv()')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L9)
               NOT_TAKEN

747    L8:     LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               7 ('load_dotenv() call')
               CALL                     1
               POP_TOP

748    L9:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              20 (('os.environ[', 'os.getenv(', 'getenv('))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         4 (to L10)
               NOT_TAKEN
               EXTENDED_ARG             1
               JUMP_BACKWARD          294 (to L2)

749   L10:     LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               8 ('environ read')
               CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          314 (to L2)

721   L11:     END_FOR
               POP_ITER

750            LOAD_FAST                1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             19 (_check + NULL)

751            LOAD_CONST               9 ('self_check:no_env_or_vendor')

752            LOAD_FAST_BORROW         4 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L12)
               NOT_TAKEN
               LOAD_CONST              10 ('FAIL')
               JUMP_FORWARD             1 (to L13)
      L12:     LOAD_CONST              11 ('PASS')

753   L13:     LOAD_CONST              12 ('PAS165 readiness checker never reads .env, calls Supabase, or imports vendor / Google / embedding libs')

755            LOAD_GLOBAL             20 (SEVERITY_BLOCK)

757            LOAD_FAST_BORROW         4 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L14)
               NOT_TAKEN

756            LOAD_CONST              13 ('disqualifying code-line patterns: ')
               LOAD_CONST              14 (', ')
               LOAD_ATTR               23 (join + NULL|self)
               LOAD_FAST_BORROW         4 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L15)

757   L14:     LOAD_CONST               0 ('')

750   L15:     LOAD_CONST              15 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

759            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 766>:
766           RESUME                   0
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

Disassembly of <code object _aggregate at 0x0000018C17EC57C0, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 766>:
 766            RESUME                   0

 768            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 767            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2

 768    L2:     FOR_ITER                49 (to L7)
                STORE_FAST               1 (c)

 769            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 768    L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L2)

 769    L4:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              2 (SEVERITY_BLOCK)
                COMPARE_OP              88 (bool(==))

 768    L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L2)
        L6:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L2)
        L7:     END_FOR
                POP_ITER

 767    L8:     STORE_FAST               2 (blockers)
                STORE_FAST               1 (c)

 772            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 771            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L9:     BUILD_LIST               0
                SWAP                     2

 772   L10:     FOR_ITER                49 (to L15)
                STORE_FAST               1 (c)

 773            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 772   L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L10)

 773   L12:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              4 (SEVERITY_INFO)
                COMPARE_OP              88 (bool(==))

 772   L13:     POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L10)
       L14:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L10)
       L15:     END_FOR
                POP_ITER

 771   L16:     STORE_FAST               3 (info)
                STORE_FAST               1 (c)

 776            LOAD_CONST               3 ('verdict')
                LOAD_FAST_BORROW         2 (blockers)
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L17)
                NOT_TAKEN
                LOAD_GLOBAL              6 (VERDICT_NOT_READY)
                JUMP_FORWARD             5 (to L18)
       L17:     LOAD_GLOBAL              8 (VERDICT_READY)

 777   L18:     LOAD_CONST               4 ('blockers')
                LOAD_FAST_BORROW         2 (blockers)

 778            LOAD_CONST               5 ('info')
                LOAD_FAST_BORROW         3 (info)

 775            BUILD_MAP                3
                RETURN_VALUE

  --   L19:     SWAP                     2
                POP_TOP

 767            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0

  --   L20:     SWAP                     2
                POP_TOP

 771            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L19 [2]
  L4 to L5 -> L19 [2]
  L6 to L8 -> L19 [2]
  L9 to L11 -> L20 [2]
  L12 to L13 -> L20 [2]
  L14 to L16 -> L20 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA3000, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 782>:
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
              LOAD_CONST               4 ('List[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _operator_actions at 0x0000018C180483B0, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 782>:
782           RESUME                   0

783           BUILD_LIST               0
              STORE_FAST               1 (out)

784           LOAD_FAST_BORROW         0 (checks)
              GET_ITER
      L1:     FOR_ITER               109 (to L5)
              STORE_FAST               2 (c)

785           LOAD_FAST_BORROW         2 (c)
              LOAD_CONST               0 ('status')
              BINARY_OP               26 ([])
              LOAD_CONST               1 ('FAIL')
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

786           JUMP_BACKWARD           19 (to L1)

787   L2:     LOAD_FAST_BORROW         2 (c)
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

788           LOAD_FAST                1 (out)
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

784   L5:     END_FOR
              POP_ITER

789           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180FC210, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 792>:
792           RESUME                   0
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

Disassembly of <code object evaluate at 0x0000018C17ED88D0, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 792>:
792           RESUME                   0

793           BUILD_LIST               0
              STORE_FAST               1 (checks)

794           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              3 (check_files_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

795           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              5 (check_prior_phases_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

796           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              7 (check_memory_review_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

797           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              9 (check_email_auth + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

798           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             11 (check_email_dedupe + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

799           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             13 (check_service_signature_kwargs + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

800           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             15 (check_route_signature_header + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

801           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             17 (check_event_contract + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

802           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             19 (check_no_forbidden_imports + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

803           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             21 (check_no_inbox_scanning + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

804           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             23 (check_docs_required_doctrine + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

805           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             25 (check_self_no_env_or_vendor + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

807           LOAD_GLOBAL             27 (_aggregate + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1
              STORE_FAST               2 (agg)

809           LOAD_CONST               0 ('phase')
              LOAD_CONST               1 ('PAS165')

810           LOAD_CONST               2 ('generated_at')
              LOAD_GLOBAL             29 (_now_iso + NULL)
              CALL                     0

811           LOAD_CONST               3 ('verdict')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])

812           LOAD_CONST               4 ('ready')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])
              LOAD_GLOBAL             30 (VERDICT_READY)
              COMPARE_OP              72 (==)

813           LOAD_CONST               5 ('blocker_count')
              LOAD_GLOBAL             33 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               6 ('blockers')
              BINARY_OP               26 ([])
              CALL                     1

814           LOAD_CONST               7 ('info_count')
              LOAD_GLOBAL             33 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               8 ('info')
              BINARY_OP               26 ([])
              CALL                     1

815           LOAD_CONST               9 ('check_count')
              LOAD_GLOBAL             33 (len + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

816           LOAD_CONST              10 ('pass_count')
              LOAD_GLOBAL             35 (sum + NULL)
              LOAD_CONST              11 (<code object <genexpr> at 0x0000018C18053CF0, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 816>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

817           LOAD_CONST              12 ('fail_count')
              LOAD_GLOBAL             35 (sum + NULL)
              LOAD_CONST              13 (<code object <genexpr> at 0x0000018C18052F70, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 817>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

818           LOAD_CONST              14 ('checks')
              LOAD_FAST_BORROW         1 (checks)

819           LOAD_CONST              15 ('operator_actions')
              LOAD_GLOBAL             37 (_operator_actions + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

808           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18053CF0, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 816>:
 816           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C18052F70, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 817>:
 817           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C180FC120, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 826>:
826           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C179A7290, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 826>:
826           RESUME                   0

827           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

828           LOAD_CONST               0 ('pas165_email_auth_dedupe_readiness_check')

830           LOAD_CONST               1 ('PAS165 — Evaluate the email forwarder authentication and dedupe layer for structural correctness, no-Gmail-OAuth doctrine, no inbox scanning, no raw-body / signature / dedupe-key leakage. Read-only. Does not touch Supabase, .env, or any tenant data.')

827           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

838           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

839           LOAD_CONST               3 ('--repo-root')
              LOAD_GLOBAL              6 (_REPO_ROOT_DEFAULT)

840           LOAD_CONST               4 ('Repo root to evaluate (default: parent of this script).')

838           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

842           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

843           LOAD_CONST               6 ('--output')
              LOAD_GLOBAL              8 (REPORT_FILENAME)

844           LOAD_CONST               7 ('Where to write the JSON report (default ./')
              LOAD_GLOBAL              8 (REPORT_FILENAME)
              FORMAT_SIMPLE
              LOAD_CONST               8 (').')
              BUILD_STRING             3

842           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

846           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

847           LOAD_CONST               9 ('--json')
              LOAD_CONST              10 ('store_true')

848           LOAD_CONST              11 ('Emit the report JSON on stdout in addition to the file.')

846           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

850           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

851           LOAD_CONST              13 ('--summary-only')
              LOAD_CONST              10 ('store_true')

852           LOAD_CONST              14 ('Skip writing the full report file; print verdict only.')

850           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

854           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

855           LOAD_CONST              15 ('--strict')
              LOAD_CONST              10 ('store_true')

856           LOAD_CONST              16 ('Exit 1 unless verdict == READY (default policy is the same).')

854           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

858           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180FC300, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 861>:
861           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C17D8E300, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 861>:
861           RESUME                   0

862           LOAD_GLOBAL              1 (print + NULL)

863           LOAD_CONST               0 ('[PAS165] verdict=')
              LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               1 ('verdict')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               2 (' blockers=')

864           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               3 ('blocker_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' info=')

865           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               5 ('info_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' checks=')

866           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               7 ('check_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' pass=')

867           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               9 ('pass_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              10 (' fail=')

868           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              11 ('fail_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE

863           BUILD_STRING            12

862           CALL                     1
              POP_TOP

870           LOAD_FAST_BORROW         0 (report)
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

871           LOAD_FAST_BORROW         1 (actions)
              TO_BOOL
              POP_JUMP_IF_FALSE       93 (to L5)
              NOT_TAKEN

872           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              13 ('[PAS165] operator actions:')
              CALL                     1
              POP_TOP

873           LOAD_FAST_BORROW         1 (actions)
              LOAD_CONST              14 (slice(None, 25, None))
              BINARY_OP               26 ([])
              GET_ITER
      L2:     FOR_ITER                17 (to L3)
              STORE_FAST               2 (a)

874           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              15 ('  - ')
              LOAD_FAST_BORROW         2 (a)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L2)

873   L3:     END_FOR
              POP_ITER

875           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         1 (actions)
              CALL                     1
              LOAD_SMALL_INT          25
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       34 (to L4)
              NOT_TAKEN

876           LOAD_GLOBAL              1 (print + NULL)
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

875   L4:     LOAD_CONST              18 (None)
              RETURN_VALUE

871   L5:     LOAD_CONST              18 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025D30, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 879>:
879           RESUME                   0
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

Disassembly of <code object _write_report at 0x0000018C18104210, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 879>:
 879           RESUME                   0

 880           NOP

 881   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

 882           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

 883           LOAD_CONST               3 ('utf-8')

 881           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 885           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

 886   L4:     LOAD_GLOBAL             11 (print + NULL)

 887           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

 888           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

 887           BUILD_STRING             4

 889           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

 886           LOAD_CONST               7 (('file',))
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

 885   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C180FCA80, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 893>:
893           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17F83070, file "scripts\pas165_email_auth_dedupe_readiness_check.py", line 893>:
 893            RESUME                   0

 894            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 895            NOP

 896    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 900    L2:     LOAD_GLOBAL             10 (os)
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

 901            LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               21 (isdir + NULL|self)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L4)
                NOT_TAKEN

 902            LOAD_GLOBAL             23 (print + NULL)

 903            LOAD_CONST               2 ('error: --repo-root not a directory: ')
                LOAD_FAST                4 (repo_root)
                FORMAT_SIMPLE
                BUILD_STRING             2

 904            LOAD_GLOBAL             24 (sys)
                LOAD_ATTR               26 (stderr)

 902            LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

 906            LOAD_SMALL_INT           2
                RETURN_VALUE

 908    L4:     LOAD_GLOBAL             29 (evaluate + NULL)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                STORE_FAST               5 (report)

 910            LOAD_FAST                2 (args)
                LOAD_ATTR               30 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L5)
                NOT_TAKEN

 911            LOAD_GLOBAL             33 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               34 (output)
                LOAD_FAST                5 (report)
                CALL                     2
                POP_TOP

 913    L5:     LOAD_GLOBAL             37 (_print_summary + NULL)
                LOAD_FAST                5 (report)
                CALL                     1
                POP_TOP

 915            LOAD_FAST                2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L6)
                NOT_TAKEN

 916            LOAD_GLOBAL             23 (print + NULL)
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

 918    L6:     LOAD_FAST                5 (report)
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

 897            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L17)
                NOT_TAKEN
                STORE_FAST               3 (e)

 898    L9:     LOAD_FAST                3 (e)
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

 897   L17:     RERAISE                  0

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
