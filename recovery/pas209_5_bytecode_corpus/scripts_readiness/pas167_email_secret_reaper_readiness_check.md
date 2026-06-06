# scripts_readiness/pas167_email_secret_reaper_readiness_check

- **pyc:** `scripts\__pycache__\pas167_email_secret_reaper_readiness_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/pas167_email_secret_reaper_readiness_check.py`
- **co_filename (from bytecode):** `scripts\pas167_email_secret_reaper_readiness_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS167 — Email forwarder secret-at-rest encryption + dedupe
reaper readiness gate.

Deterministic, non-mutating evaluator for "is the PAS167
secret-store seam wired correctly, the reaper script
operator-safe, and PAS164 / PAS165 / PAS166 doctrine
preserved?".

Walks the repo and verifies:

  * scripts/migrate_v16_email_secret_encryption.sql exists as
    a proposal (NOT executed in PAS167);
  * the migration adds the four nullable encrypted columns
    + the closed migration_status enum;
  * the migration does NOT drop the existing plaintext
    column;
  * app/services/ingestion/email_forwarder_secret_store.py
    exists and exports the required helpers;
  * the secret store has no fake-encryption path — it returns
    ``crypto_unavailable`` when the cryptography package
    isn't importable;
  * the secret store has a plaintext fallback that surfaces
    the structural ``plaintext_forwarder_secret_fallback``
    warning;
  * the email-ingestion route uses the secret-store helper
    rather than reading ``email_forwarder_secret`` directly;
  * scripts/reap_email_dedupe.py exists and is dry-run-by-
    default (the ``--execute`` flag is required for any
    delete);
  * the reaper never prints the dedupe key;
  * the event allow-list excludes secret / encrypted_secret /
    signature / dedupe_key / phone / email / name / subject /
    sender / body / raw_* / property_address / notes /
    transcript;
  * no Gmail / Google / IMAP / POP3 / inbox-scan tokens;
  * no embedding / vector / vendor imports;
  * Memory Review UI files are intact;
  * prior-phase readiness scripts (PAS160 / PAS161 / PAS162 /
    PAS163 / PAS164 / PAS165 / PAS166) still exist;
  * supports --summary-only and --json;
  * exits 0 ready, 1 blockers, 2 bad args;
  * never reads .env;
  * never touches production data.

Usage:
  python scripts/pas167_email_secret_reaper_readiness_check.py
  python scripts/pas167_email_secret_reaper_readiness_check.py --json
  python scripts/pas167_email_secret_reaper_readiness_check.py --summary-only
  python scripts/pas167_email_secret_reaper_readiness_check.py --strict

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

`__annotate__`, `_aggregate`, `_build_parser`, `_check`, `_now_iso`, `_operator_actions`, `_print_summary`, `_read_text`, `_strip_python_comments_and_strings`, `_write_report`, `check_docs_required_doctrine`, `check_event_contract`, `check_files_present`, `check_memory_review_intact`, `check_migration_proposal`, `check_no_forbidden_imports`, `check_no_inbox_scanning`, `check_prior_phases_intact`, `check_reaper`, `check_route_uses_helper`, `check_secret_store`, `check_self_no_env_or_vendor`, `evaluate`, `main`

## Env-key candidates

`BLOCK`, `FAIL`, `INFO`, `NOT_READY`, `PAS167`, `PASS`, `READY`

## String constants (redacted where noted)

- '\nPAS167 — Email forwarder secret-at-rest encryption + dedupe\nreaper readiness gate.\n\nDeterministic, non-mutating evaluator for "is the PAS167\nsecret-store seam wired correctly, the reaper script\noperator-safe, and PAS164 / PAS165 / PAS166 doctrine\npreserved?".\n\nWalks the repo and verifies:\n\n  * scripts/migrate_v16_email_secret_encryption.sql exists as\n    a proposal (NOT executed in PAS167);\n  * the migration adds the four nullable encrypted columns\n    + the closed migration_status enum;\n  * the migration does NOT drop the existing plaintext\n    column;\n  * app/services/ingestion/email_forwarder_secret_store.py\n    exists and exports the required helpers;\n  * the secret store has no fake-encryption path — it returns\n    ``crypto_unavailable`` when the cryptography package\n    isn\'t importable;\n  * the secret store has a plaintext fallback that surfaces\n    the structural ``plaintext_forwarder_secret_fallback``\n    warning;\n  * the email-ingestion route uses the secret-store helper\n    rather than reading ``email_forwarder_secret`` directly;\n  * scripts/reap_email_dedupe.py exists and is dry-run-by-\n    default (the ``--execute`` flag is required for any\n    delete);\n  * the reaper never prints the dedupe key;\n  * the event allow-list excludes secret / encrypted_secret /\n    signature / dedupe_key / phone / email / name / subject /\n    sender / body / raw_* / property_address / notes /\n    transcript;\n  * no Gmail / Google / IMAP / POP3 / inbox-scan tokens;\n  * no embedding / vector / vendor imports;\n  * Memory Review UI files are intact;\n  * prior-phase readiness scripts (PAS160 / PAS161 / PAS162 /\n    PAS163 / PAS164 / PAS165 / PAS166) still exist;\n  * supports --summary-only and --json;\n  * exits 0 ready, 1 blockers, 2 bad args;\n  * never reads .env;\n  * never touches production data.\n\nUsage:\n  python scripts/pas167_email_secret_reaper_readiness_check.py\n  python scripts/pas167_email_secret_reaper_readiness_check.py --json\n  python scripts/pas167_email_secret_reaper_readiness_check.py --summary-only\n  python scripts/pas167_email_secret_reaper_readiness_check.py --strict\n\nExit codes:\n    0  — READY  (verdict == READY)\n    1  — NOT_READY\n    2  — bad CLI arguments\n'
- 'utf-8'
- 'READY'
- 'NOT_READY'
- 'BLOCK'
- 'INFO'
- 'severity'
- 'detail'
- 'pas167_email_secret_reaper_readiness_report.json'
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
- 'Required PAS167 file present: '
- 'missing'
- 'prior_phase:'
- 'Prior-phase readiness script intact: '
- 'missing — PAS167 must not delete'
- 'memory_review_file:'
- 'Memory Review file present (PAS167 must not delete): '
- 'PAS167 must not delete Memory Review files'
- 'scripts'
- 'migrate_v16_email_secret_encryption.sql'
- 'proposal only'
- 'migration:proposal_only'
- "Migration carries 'PROPOSAL ONLY' guardrail"
- "missing 'PROPOSAL ONLY' label"
- 'do not execute'
- 'migration:do_not_execute'
- "Migration carries 'DO NOT EXECUTE' trailer"
- 'missing trailer'
- 'migration:col:'
- 'Migration adds '
- 'column '
- ' missing'
- 'migration:status_enum:'
- 'Migration migration_status enum carries '
- 'enum value '
- 'drop column email_forwarder_secret '
- 'drop column email_forwarder_secret\n'
- 'drop column email_forwarder_secret;'
- 'migration:plaintext_column_not_dropped'
- 'Migration does not drop the plaintext column'
- 'ALTER TABLE ... DROP COLUMN email_forwarder_secret present'
- 'revoke select'
- 'email_forwarder_secret_encrypted'
- 'migration:revoke_tenant_select_encrypted'
- 'Migration revokes tenant SELECT on encrypted columns'
- 'REVOKE SELECT on encrypted columns missing'
- 'revoke update'
- 'migration:revoke_tenant_update_encrypted'
- 'Migration revokes tenant UPDATE on encrypted columns'
- 'REVOKE UPDATE on encrypted columns missing'
- 'grant select'
- 'service_role'
- 'migration:grant_service_role'
- 'Migration grants service_role on encrypted columns'
- 'service_role grant missing'
- 'app'
- 'services'
- 'ingestion'
- 'email_forwarder_secret_store.py'
- 'store_fn:'
- 'Secret-store function present: '
- 'missing def: '
- 'store_token:'
- 'Secret-store carries structural token: '
- 'missing token '
- 'from cryptography.fernet'
- 'cryptography.fernet'
- 'Fernet'
- 'store:references_real_crypto_primitive'
- 'Secret-store references the cryptography Fernet primitive'
- 'no real crypto primitive referenced'
- 'crypto_unavailable'
- 'store:no_fake_encryption'
- 'Secret-store fails closed when crypto is unavailable'
- 'missing crypto_unavailable branch'
- 'is True'
- 'email_forwarder_secret_encryption_enabled'
- 'lower() == _ENV_TRUE_LITERAL'
- 'store:strict_literal_true'
- 'Encryption-enabled flag uses strict literal True'
- "expected 'is True' or _ENV_TRUE_LITERAL comparison"
- 'plaintext_forwarder_secret_fallback'
- 'store:plaintext_fallback_present'
- 'Secret-store retains plaintext-fallback path'
- 'missing plaintext_forwarder_secret_fallback'
- 'store:no_forbidden_response_key:'
- 'Secret-store excludes forbidden response key: '
- 'forbidden key '
- ' present as dict-key'
- 'routes'
- 'email_ingestion.py'
- 'get_email_forwarder_secret'
- 'route:uses_secret_store_helper'
- 'Route uses get_email_forwarder_secret helper'
- 'secret-store helper not referenced'
- 'route:no_body_trust:'
- 'Route never reads brokerage_id from body: '
- 'body-trust pattern '
- ' present'
- '_EVENT_PAYLOAD_ALLOWED'
- 'route:event_allowlist_excludes:'
- 'Event payload allow-list excludes forbidden key: '
- 'forbidden allow-list key '
- 'reap_email_dedupe.py'
- 'reaper_token:'
- 'Reaper declares CLI / mode token: '
- '"--execute"'
- 'action="store_true"'
- 'reaper:dry_run_by_default'
- 'Reaper is dry-run by default'
- 'expected --execute store_true'
- 'dedupe_key'
- 'reaper:no_dedupe_key_in_executable'
- 'Reaper executable does not reference the dedupe key'
- "'dedupe_key' present in reaper executable"
- 'return 0'
- 'return 1'
- 'return 2'
- 'reaper:exit_codes_present'
- 'Reaper declares exit codes 0/1/2'
- 'expected return 0/1/2 branches'
- 'events'
- 'contract.py'
- 'events:'
- 'Event contract registers '
- 'missing event type '
- 'app/services/ingestion/email_forwarder_secret_store.py'
- 'forbidden_import:'
- 'No forbidden imports: '
- 'forbidden import prefixes: '
- 'no_inbox_scan:'
- 'No inbox-scanning tokens: '
- 'inbox-scan tokens present: '
- 'docs'
- 'pas167_email_secret_encryption_and_dedupe_reaper.md'
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
- 'PAS167 readiness checker never reads .env, calls Supabase, or imports vendor / Google / embedding libs'
- 'disqualifying code-line patterns: '
- 'checks'
- 'verdict'
- 'blockers'
- 'info'
- 'List[str]'
- ' — '
- 'see report'
- 'phase'
- 'PAS167'
- 'generated_at'
- 'ready'
- 'blocker_count'
- 'info_count'
- 'check_count'
- 'pass_count'
- 'fail_count'
- 'operator_actions'
- 'argparse.ArgumentParser'
- 'pas167_email_secret_reaper_readiness_check'
- 'PAS167 — Evaluate the email forwarder secret-at-rest encryption seam + the dedupe reaper for structural correctness, no fake encryption, no Gmail / inbox / vendor imports, and no PII leakage from the reaper. Read-only. Does not touch Supabase, .env, or tenant data.'
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
- '[PAS167] verdict='
- ' blockers='
- ' info='
- ' checks='
- ' pass='
- ' fail='
- '[PAS167] operator actions:'
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

   1           LOAD_CONST               0 ('\nPAS167 — Email forwarder secret-at-rest encryption + dedupe\nreaper readiness gate.\n\nDeterministic, non-mutating evaluator for "is the PAS167\nsecret-store seam wired correctly, the reaper script\noperator-safe, and PAS164 / PAS165 / PAS166 doctrine\npreserved?".\n\nWalks the repo and verifies:\n\n  * scripts/migrate_v16_email_secret_encryption.sql exists as\n    a proposal (NOT executed in PAS167);\n  * the migration adds the four nullable encrypted columns\n    + the closed migration_status enum;\n  * the migration does NOT drop the existing plaintext\n    column;\n  * app/services/ingestion/email_forwarder_secret_store.py\n    exists and exports the required helpers;\n  * the secret store has no fake-encryption path — it returns\n    ``crypto_unavailable`` when the cryptography package\n    isn\'t importable;\n  * the secret store has a plaintext fallback that surfaces\n    the structural ``plaintext_forwarder_secret_fallback``\n    warning;\n  * the email-ingestion route uses the secret-store helper\n    rather than reading ``email_forwarder_secret`` directly;\n  * scripts/reap_email_dedupe.py exists and is dry-run-by-\n    default (the ``--execute`` flag is required for any\n    delete);\n  * the reaper never prints the dedupe key;\n  * the event allow-list excludes secret / encrypted_secret /\n    signature / dedupe_key / phone / email / name / subject /\n    sender / body / raw_* / property_address / notes /\n    transcript;\n  * no Gmail / Google / IMAP / POP3 / inbox-scan tokens;\n  * no embedding / vector / vendor imports;\n  * Memory Review UI files are intact;\n  * prior-phase readiness scripts (PAS160 / PAS161 / PAS162 /\n    PAS163 / PAS164 / PAS165 / PAS166) still exist;\n  * supports --summary-only and --json;\n  * exits 0 ready, 1 blockers, 2 bad args;\n  * never reads .env;\n  * never touches production data.\n\nUsage:\n  python scripts/pas167_email_secret_reaper_readiness_check.py\n  python scripts/pas167_email_secret_reaper_readiness_check.py --json\n  python scripts/pas167_email_secret_reaper_readiness_check.py --summary-only\n  python scripts/pas167_email_secret_reaper_readiness_check.py --strict\n\nExit codes:\n    0  — READY  (verdict == READY)\n    1  — NOT_READY\n    2  — bad CLI arguments\n')
               STORE_NAME               0 (__doc__)

  58           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  60           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  61           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (json)
               STORE_NAME               4 (json)

  62           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (os)
               STORE_NAME               5 (os)

  63           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (sys)
               STORE_NAME               6 (sys)

  64           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              7 (datetime)
               IMPORT_FROM              7 (datetime)
               STORE_NAME               7 (datetime)
               IMPORT_FROM              8 (timezone)
               STORE_NAME               8 (timezone)
               POP_TOP

  65           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Path',))
               IMPORT_NAME              9 (pathlib)
               IMPORT_FROM             10 (Path)
               STORE_NAME              10 (Path)
               POP_TOP

  66           LOAD_SMALL_INT           0
               LOAD_CONST               5 (('List', 'Optional'))
               IMPORT_NAME             11 (typing)
               IMPORT_FROM             12 (List)
               STORE_NAME              12 (List)
               IMPORT_FROM             13 (Optional)
               STORE_NAME              13 (Optional)
               POP_TOP

  69           LOAD_NAME                6 (sys)
               LOAD_ATTR               28 (stdout)
               LOAD_NAME                6 (sys)
               LOAD_ATTR               30 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              16 (_stream)

  70           NOP

  71   L2:     LOAD_NAME               16 (_stream)
               LOAD_ATTR               35 (reconfigure + NULL|self)
               LOAD_CONST               6 ('utf-8')
               LOAD_CONST               7 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  69   L4:     END_FOR
               POP_ITER

  76           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               41 (abspath + NULL|self)

  77           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               43 (join + NULL|self)
               LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               45 (dirname + NULL|self)
               LOAD_NAME               23 (__file__)
               CALL                     1
               LOAD_CONST               8 ('..')
               CALL                     2

  76           CALL                     1
               STORE_NAME              24 (_REPO_ROOT_DEFAULT)

  81           LOAD_CONST               9 ('READY')
               STORE_NAME              25 (VERDICT_READY)

  82           LOAD_CONST              10 ('NOT_READY')
               STORE_NAME              26 (VERDICT_NOT_READY)

  84           LOAD_CONST              11 ('BLOCK')
               STORE_NAME              27 (SEVERITY_BLOCK)

  85           LOAD_CONST              12 ('INFO')
               STORE_NAME              28 (SEVERITY_INFO)

  92           LOAD_CONST              64 (('scripts/migrate_v16_email_secret_encryption.sql', 'app/services/ingestion/email_forwarder_secret_store.py', 'scripts/reap_email_dedupe.py', 'app/routes/email_ingestion.py', 'scripts/pas167_email_secret_reaper_readiness_check.py', 'docs/pas167_email_secret_encryption_and_dedupe_reaper.md', 'tests/mvp/test_pas167_email_secret_reaper.py'))
               STORE_NAME              29 (REQUIRED_FILES)

 102           LOAD_CONST              65 (('scripts/pas160_mvp_sequence_check.py', 'scripts/pas161_lead_ingestion_readiness_check.py', 'scripts/pas162_pending_calls_readiness_check.py', 'scripts/pas163_candidate_pipeline_readiness_check.py', 'scripts/pas164_email_ingestion_readiness_check.py', 'scripts/pas165_email_auth_dedupe_readiness_check.py', 'scripts/pas166_email_dedupe_policy_readiness_check.py'))
               STORE_NAME              30 (PRIOR_PHASE_FILES)

 112           LOAD_CONST              66 (('app/services/memory/review.py', 'app/services/memory/review_stats.py', 'app/services/memory/review_export.py', 'app/services/memory/review_actors.py', 'app/services/memory/review_alerts.py', 'app/services/memory/operator_console.py'))
               STORE_NAME              31 (MEMORY_REVIEW_FILES)

 122           LOAD_CONST              67 (('def email_forwarder_secret_encryption_enabled(', 'def get_email_forwarder_secret(', 'def encrypt_email_forwarder_secret(', 'def decrypt_email_forwarder_secret(', 'def redact_secret_for_log('))
               STORE_NAME              32 (REQUIRED_STORE_FUNCTIONS)

 130           LOAD_CONST              68 (('crypto_unavailable', 'crypto_key_missing', 'forwarder_secret_decrypt_failed', 'plaintext_forwarder_secret_fallback'))
               STORE_NAME              33 (REQUIRED_STORE_TOKENS)

 137           LOAD_CONST              69 (('--execute', '--brokerage-id', '--source', '--older-than-hours', '--limit', '--json', 'dry-run', 'execute'))
               STORE_NAME              34 (REQUIRED_REAPER_TOKENS)

 148           LOAD_CONST              70 (('email.dedupe.reaper.dry_run', 'email.dedupe.reaper.deleted', 'email.forwarder.secret.encrypted', 'email.forwarder.secret.decrypt_failed', 'email.forwarder.secret.plaintext_fallback'))
               STORE_NAME              35 (REQUIRED_EVENT_TYPES)

 158           LOAD_CONST              71 (('email_forwarder_secret_encrypted', 'email_forwarder_secret_kid', 'email_forwarder_secret_updated_at', 'email_forwarder_secret_migration_status'))
               STORE_NAME              36 (REQUIRED_MIGRATION_COLUMNS)

 165           LOAD_CONST              72 (('plaintext', 'encrypted', 'rotation_required', 'disabled'))
               STORE_NAME              37 (REQUIRED_MIGRATION_STATUS_VALUES)

 171           LOAD_CONST              73 (('secret', 'encrypted_secret', 'signature', 'dedupe_key', 'phone', 'email', 'name', 'subject', 'sender', 'body', 'raw_email', 'raw_body', 'property_address', 'notes', 'transcript'))
               STORE_NAME              38 (FORBIDDEN_EVENT_PAYLOAD_KEYS)

 190           LOAD_CONST              74 (('import googleapiclient', 'from googleapiclient', 'import google.oauth2', 'from google.oauth2', 'from google.auth', 'import google.auth', 'from google_auth_oauthlib', 'import composio', 'from composio', 'import trustclaw', 'from trustclaw', 'import openai', 'from openai', 'import anthropic', 'from anthropic', 'import numpy', 'import faiss', 'import pgvector', 'from pgvector', 'from openai import embeddings', 'from openai.embeddings', 'from app.services.memory', 'import app.services.memory', 'import imaplib', 'from imaplib', 'import poplib', 'from poplib'))
               STORE_NAME              39 (FORBIDDEN_IMPORT_LINE_PREFIXES)

 220           LOAD_CONST              75 (('imaplib', 'poplib', 'fetch_inbox', 'gmail_oauth', 'gmail_token', 'users().messages'))
               STORE_NAME              40 (FORBIDDEN_INBOX_TOKENS)

 234           LOAD_CONST              13 ('severity')

 236           LOAD_NAME               27 (SEVERITY_BLOCK)

 234           LOAD_CONST              14 ('detail')

 236           LOAD_CONST              15 ('')

 234           BUILD_MAP                2
               LOAD_CONST              16 (<code object __annotate__ at 0x0000018C18024C30, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 234>)
               MAKE_FUNCTION
               LOAD_CONST              17 (<code object _check at 0x0000018C17FA31E0, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 234>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              41 (_check)

 247           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA3E10, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 247>)
               MAKE_FUNCTION
               LOAD_CONST              19 (<code object _now_iso at 0x0000018C18038B70, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 247>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              42 (_now_iso)

 251           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA3960, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 251>)
               MAKE_FUNCTION
               LOAD_CONST              21 (<code object _read_text at 0x0000018C18053E10, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 251>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              43 (_read_text)

 258           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA3C30, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 258>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object _strip_python_comments_and_strings at 0x0000018C17D8BF50, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 258>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              44 (_strip_python_comments_and_strings)

 297           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA3A50, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 297>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object check_files_present at 0x0000018C180606F0, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 297>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              45 (check_files_present)

 311           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA30F0, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 311>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object check_prior_phases_intact at 0x0000018C18061110, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 311>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              46 (check_prior_phases_intact)

 325           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA3F00, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 325>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object check_memory_review_intact at 0x0000018C18060DB0, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 325>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              47 (check_memory_review_intact)

 339           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA2010, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 339>)
               MAKE_FUNCTION
               LOAD_CONST              31 (<code object check_migration_proposal at 0x0000018C17D57890, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 339>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              48 (check_migration_proposal)

 429           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA22E0, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 429>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object check_secret_store at 0x0000018C177C69F0, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 429>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              49 (check_secret_store)

 512           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA24C0, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 512>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object check_route_uses_helper at 0x0000018C17E8A0E0, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 512>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              50 (check_route_uses_helper)

 557           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C17FA23D0, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 557>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object check_reaper at 0x0000018C17F837D0, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 557>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              51 (check_reaper)

 613           LOAD_CONST              38 (<code object __annotate__ at 0x0000018C17FA2A60, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 613>)
               MAKE_FUNCTION
               LOAD_CONST              39 (<code object check_event_contract at 0x0000018C17FEDC30, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 613>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              52 (check_event_contract)

 629           LOAD_CONST              40 (<code object __annotate__ at 0x0000018C17FA2C40, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 629>)
               MAKE_FUNCTION
               LOAD_CONST              41 (<code object check_no_forbidden_imports at 0x0000018C17D8B3B0, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 629>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              53 (check_no_forbidden_imports)

 657           LOAD_CONST              42 (<code object __annotate__ at 0x0000018C17FA3690, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 657>)
               MAKE_FUNCTION
               LOAD_CONST              43 (<code object check_no_inbox_scanning at 0x0000018C17CC1CE0, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 657>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              54 (check_no_inbox_scanning)

 683           LOAD_CONST              44 (<code object __annotate__ at 0x0000018C17FA3870, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 683>)
               MAKE_FUNCTION
               LOAD_CONST              45 (<code object check_docs_required_doctrine at 0x0000018C17F73EF0, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 683>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              55 (check_docs_required_doctrine)

 723           LOAD_CONST              46 (<code object __annotate__ at 0x0000018C17FA3000, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 723>)
               MAKE_FUNCTION
               LOAD_CONST              47 (<code object check_self_no_env_or_vendor at 0x0000018C17E56380, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 723>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              56 (check_self_no_env_or_vendor)

 773           LOAD_CONST              48 (<code object __annotate__ at 0x0000018C180FC210, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 773>)
               MAKE_FUNCTION
               LOAD_CONST              49 (<code object _aggregate at 0x0000018C17EC57C0, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 773>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              57 (_aggregate)

 789           LOAD_CONST              50 (<code object __annotate__ at 0x0000018C180FC120, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 789>)
               MAKE_FUNCTION
               LOAD_CONST              51 (<code object _operator_actions at 0x0000018C18048730, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 789>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              58 (_operator_actions)

 799           LOAD_CONST              52 (<code object __annotate__ at 0x0000018C180FC300, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 799>)
               MAKE_FUNCTION
               LOAD_CONST              53 (<code object evaluate at 0x0000018C17E56800, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 799>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              59 (evaluate)

 830           LOAD_CONST              54 ('pas167_email_secret_reaper_readiness_report.json')
               STORE_NAME              60 (REPORT_FILENAME)

 833           LOAD_CONST              55 (<code object __annotate__ at 0x0000018C180FCA80, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 833>)
               MAKE_FUNCTION
               LOAD_CONST              56 (<code object _build_parser at 0x0000018C179A7290, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 833>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              61 (_build_parser)

 868           LOAD_CONST              57 (<code object __annotate__ at 0x0000018C180FC3F0, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 868>)
               MAKE_FUNCTION
               LOAD_CONST              58 (<code object _print_summary at 0x0000018C17D8E300, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 868>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              62 (_print_summary)

 886           LOAD_CONST              59 (<code object __annotate__ at 0x0000018C18024F30, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 886>)
               MAKE_FUNCTION
               LOAD_CONST              60 (<code object _write_report at 0x0000018C18104210, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 886>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              63 (_write_report)

 900           LOAD_CONST              76 ((None,))
               LOAD_CONST              61 (<code object __annotate__ at 0x0000018C180FC4E0, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 900>)
               MAKE_FUNCTION
               LOAD_CONST              62 (<code object main at 0x0000018C17F842E0, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 900>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              64 (main)

 928           LOAD_NAME               65 (__name__)
               LOAD_CONST              63 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 929           LOAD_NAME                6 (sys)
               LOAD_ATTR              132 (exit)
               PUSH_NULL
               LOAD_NAME               64 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 928   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  72           LOAD_NAME               18 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  73   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          329 (to L1)

  72   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 234>:
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

Disassembly of <code object _check at 0x0000018C17FA31E0, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 234>:
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 247>:
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

Disassembly of <code object _now_iso at 0x0000018C18038B70, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 247>:
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 251>:
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

Disassembly of <code object _read_text at 0x0000018C18053E10, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 251>:
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 258>:
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

Disassembly of <code object _strip_python_comments_and_strings at 0x0000018C17D8BF50, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 258>:
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 297>:
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

Disassembly of <code object check_files_present at 0x0000018C180606F0, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 297>:
297           RESUME                   0

298           BUILD_LIST               0
              STORE_FAST               1 (out)

299           LOAD_GLOBAL              0 (REQUIRED_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
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

304   L3:     LOAD_CONST               3 ('Required PAS167 file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

305           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

306           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing')

301   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

299   L6:     END_FOR
              POP_ITER

308           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA30F0, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 311>:
311           RESUME                   0
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

Disassembly of <code object check_prior_phases_intact at 0x0000018C18061110, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 311>:
311           RESUME                   0

312           BUILD_LIST               0
              STORE_FAST               1 (out)

313           LOAD_GLOBAL              0 (PRIOR_PHASE_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

314           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

315           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

316           LOAD_CONST               0 ('prior_phase:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

317           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

318   L3:     LOAD_CONST               3 ('Prior-phase readiness script intact: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

319           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

320           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing — PAS167 must not delete')

315   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

313   L6:     END_FOR
              POP_ITER

322           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3F00, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 325>:
325           RESUME                   0
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

Disassembly of <code object check_memory_review_intact at 0x0000018C18060DB0, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 325>:
325           RESUME                   0

326           BUILD_LIST               0
              STORE_FAST               1 (out)

327           LOAD_GLOBAL              0 (MEMORY_REVIEW_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

328           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

329           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

330           LOAD_CONST               0 ('memory_review_file:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

331           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

332   L3:     LOAD_CONST               3 ('Memory Review file present (PAS167 must not delete): ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

333           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

334           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('PAS167 must not delete Memory Review files')

329   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

327   L6:     END_FOR
              POP_ITER

336           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2010, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 339>:
339           RESUME                   0
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

Disassembly of <code object check_migration_proposal at 0x0000018C17D57890, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 339>:
339            RESUME                   0

340            BUILD_LIST               0
               STORE_FAST               1 (out)

341            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('scripts')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('migrate_v16_email_secret_encryption.sql')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

342            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               2 ('')
       L1:     STORE_FAST               3 (src)

343            LOAD_FAST_BORROW         3 (src)
               LOAD_ATTR                5 (lower + NULL|self)
               CALL                     0
               STORE_FAST               4 (lower)

344            LOAD_CONST               3 ('proposal only')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (proposal_ok)

345            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

346            LOAD_CONST               4 ('migration:proposal_only')

347            LOAD_FAST_BORROW         5 (proposal_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L2)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L3)
       L2:     LOAD_CONST               6 ('FAIL')

348    L3:     LOAD_CONST               7 ("Migration carries 'PROPOSAL ONLY' guardrail")

349            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

350            LOAD_FAST_BORROW         5 (proposal_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L5)
       L4:     LOAD_CONST               8 ("missing 'PROPOSAL ONLY' label")

345    L5:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

352            LOAD_CONST              10 ('do not execute')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)
               STORE_FAST               6 (do_not_exec)

353            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

354            LOAD_CONST              11 ('migration:do_not_execute')

355            LOAD_FAST_BORROW         6 (do_not_exec)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L6)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L7)
       L6:     LOAD_CONST               6 ('FAIL')

356    L7:     LOAD_CONST              12 ("Migration carries 'DO NOT EXECUTE' trailer")

357            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

358            LOAD_FAST_BORROW         6 (do_not_exec)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST              13 ('missing trailer')

353    L9:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

360            LOAD_GLOBAL             12 (REQUIRED_MIGRATION_COLUMNS)
               GET_ITER
      L10:     FOR_ITER                72 (to L15)
               STORE_FAST               7 (col)

361            LOAD_FAST_BORROW_LOAD_FAST_BORROW 116 (col, lower)
               CONTAINS_OP              0 (in)
               STORE_FAST               8 (ok)

362            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

363            LOAD_CONST              14 ('migration:col:')
               LOAD_FAST_BORROW         7 (col)
               FORMAT_SIMPLE
               BUILD_STRING             2

364            LOAD_FAST_BORROW         8 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               6 ('FAIL')

365   L12:     LOAD_CONST              15 ('Migration adds ')
               LOAD_FAST_BORROW         7 (col)
               FORMAT_SIMPLE
               BUILD_STRING             2

366            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

367            LOAD_FAST_BORROW         8 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L13)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             5 (to L14)
      L13:     LOAD_CONST              16 ('column ')
               LOAD_FAST_BORROW         7 (col)
               FORMAT_SIMPLE
               LOAD_CONST              17 (' missing')
               BUILD_STRING             3

362   L14:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           74 (to L10)

360   L15:     END_FOR
               POP_ITER

369            LOAD_GLOBAL             14 (REQUIRED_MIGRATION_STATUS_VALUES)
               GET_ITER
      L16:     FOR_ITER                72 (to L21)
               STORE_FAST               9 (v)

370            LOAD_FAST_BORROW_LOAD_FAST_BORROW 148 (v, lower)
               CONTAINS_OP              0 (in)
               STORE_FAST               8 (ok)

371            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

372            LOAD_CONST              18 ('migration:status_enum:')
               LOAD_FAST_BORROW         9 (v)
               FORMAT_SIMPLE
               BUILD_STRING             2

373            LOAD_FAST_BORROW         8 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L17)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L18)
      L17:     LOAD_CONST               6 ('FAIL')

374   L18:     LOAD_CONST              19 ('Migration migration_status enum carries ')
               LOAD_FAST_BORROW         9 (v)
               FORMAT_SIMPLE
               BUILD_STRING             2

375            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

376            LOAD_FAST_BORROW         8 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L19)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             5 (to L20)
      L19:     LOAD_CONST              20 ('enum value ')
               LOAD_FAST_BORROW         9 (v)
               FORMAT_SIMPLE
               LOAD_CONST              17 (' missing')
               BUILD_STRING             3

371   L20:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           74 (to L16)

369   L21:     END_FOR
               POP_ITER

380            LOAD_CONST              21 ('drop column email_forwarder_secret ')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        19 (to L22)
               NOT_TAKEN
               POP_TOP

381            LOAD_CONST              22 ('drop column email_forwarder_secret\n')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)

380            COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L22)
               NOT_TAKEN
               POP_TOP

382            LOAD_CONST              23 ('drop column email_forwarder_secret;')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)

379   L22:     STORE_FAST              10 (drop_present)

384            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

385            LOAD_CONST              24 ('migration:plaintext_column_not_dropped')

386            LOAD_FAST_BORROW        10 (drop_present)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L23)
               NOT_TAKEN
               LOAD_CONST               6 ('FAIL')
               JUMP_FORWARD             1 (to L24)
      L23:     LOAD_CONST               5 ('PASS')

387   L24:     LOAD_CONST              25 ('Migration does not drop the plaintext column')

388            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

390            LOAD_FAST_BORROW        10 (drop_present)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L25)
               NOT_TAKEN

389            LOAD_CONST              26 ('ALTER TABLE ... DROP COLUMN email_forwarder_secret present')
               JUMP_FORWARD             1 (to L26)

390   L25:     LOAD_CONST               2 ('')

384   L26:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

394            LOAD_CONST              27 ('revoke select')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        6 (to L27)
               NOT_TAKEN
               POP_TOP

395            LOAD_CONST              28 ('email_forwarder_secret_encrypted')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)

393   L27:     STORE_FAST              11 (revoke_select)

397            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

398            LOAD_CONST              29 ('migration:revoke_tenant_select_encrypted')

399            LOAD_FAST_BORROW        11 (revoke_select)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L28)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L29)
      L28:     LOAD_CONST               6 ('FAIL')

400   L29:     LOAD_CONST              30 ('Migration revokes tenant SELECT on encrypted columns')

401            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

402            LOAD_FAST_BORROW        11 (revoke_select)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L30)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L31)
      L30:     LOAD_CONST              31 ('REVOKE SELECT on encrypted columns missing')

397   L31:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

405            LOAD_CONST              32 ('revoke update')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        6 (to L32)
               NOT_TAKEN
               POP_TOP

406            LOAD_CONST              28 ('email_forwarder_secret_encrypted')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)

404   L32:     STORE_FAST              12 (revoke_update)

408            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

409            LOAD_CONST              33 ('migration:revoke_tenant_update_encrypted')

410            LOAD_FAST_BORROW        12 (revoke_update)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L33)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L34)
      L33:     LOAD_CONST               6 ('FAIL')

411   L34:     LOAD_CONST              34 ('Migration revokes tenant UPDATE on encrypted columns')

412            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

413            LOAD_FAST_BORROW        12 (revoke_update)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L35)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L36)
      L35:     LOAD_CONST              35 ('REVOKE UPDATE on encrypted columns missing')

408   L36:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

416            LOAD_CONST              36 ('grant select')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        6 (to L37)
               NOT_TAKEN
               POP_TOP

417            LOAD_CONST              37 ('service_role')
               LOAD_FAST_BORROW         4 (lower)
               CONTAINS_OP              0 (in)

415   L37:     STORE_FAST              13 (grant_service)

419            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

420            LOAD_CONST              38 ('migration:grant_service_role')

421            LOAD_FAST_BORROW        13 (grant_service)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L38)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L39)
      L38:     LOAD_CONST               6 ('FAIL')

422   L39:     LOAD_CONST              39 ('Migration grants service_role on encrypted columns')

423            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

424            LOAD_FAST_BORROW        13 (grant_service)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L40)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L41)
      L40:     LOAD_CONST              40 ('service_role grant missing')

419   L41:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

426            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA22E0, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 429>:
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

Disassembly of <code object check_secret_store at 0x0000018C177C69F0, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 429>:
  --            MAKE_CELL               13 (src)

 429            RESUME                   0

 430            BUILD_LIST               0
                STORE_FAST               1 (out)

 431            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('app')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('services')
                BINARY_OP               11 (/)
                LOAD_CONST               2 ('ingestion')
                BINARY_OP               11 (/)
                LOAD_CONST               3 ('email_forwarder_secret_store.py')
                BINARY_OP               11 (/)
                STORE_FAST               2 (p)

 432            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (p)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               4 ('')
        L1:     STORE_DEREF             13 (src)

 433            LOAD_GLOBAL              4 (REQUIRED_STORE_FUNCTIONS)
                GET_ITER
        L2:     FOR_ITER                93 (to L7)
                STORE_FAST               3 (needle)

 434            LOAD_FAST_BORROW         3 (needle)
                LOAD_DEREF              13 (src)
                CONTAINS_OP              0 (in)
                STORE_FAST               4 (ok)

 435            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 436            LOAD_CONST               5 ('store_fn:')
                LOAD_FAST_BORROW         3 (needle)
                LOAD_CONST               6 (slice(None, 40, None))
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                BUILD_STRING             2

 437            LOAD_FAST_BORROW         4 (ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L3)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L4)
        L3:     LOAD_CONST               8 ('FAIL')

 438    L4:     LOAD_CONST               9 ('Secret-store function present: ')
                LOAD_FAST_BORROW         3 (needle)
                LOAD_ATTR               11 (strip + NULL|self)
                CALL                     0
                FORMAT_SIMPLE
                BUILD_STRING             2

 439            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 440            LOAD_FAST_BORROW         4 (ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN
                LOAD_CONST               4 ('')
                JUMP_FORWARD             4 (to L6)
        L5:     LOAD_CONST              10 ('missing def: ')
                LOAD_FAST_BORROW         3 (needle)
                FORMAT_SIMPLE
                BUILD_STRING             2

 435    L6:     LOAD_CONST              11 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           95 (to L2)

 433    L7:     END_FOR
                POP_ITER

 442            LOAD_GLOBAL             14 (REQUIRED_STORE_TOKENS)
                GET_ITER
        L8:     FOR_ITER                72 (to L13)
                STORE_FAST               5 (tok)

 443            LOAD_FAST_BORROW         5 (tok)
                LOAD_DEREF              13 (src)
                CONTAINS_OP              0 (in)
                STORE_FAST               4 (ok)

 444            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 445            LOAD_CONST              12 ('store_token:')
                LOAD_FAST_BORROW         5 (tok)
                FORMAT_SIMPLE
                BUILD_STRING             2

 446            LOAD_FAST_BORROW         4 (ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L9)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L10)
        L9:     LOAD_CONST               8 ('FAIL')

 447   L10:     LOAD_CONST              13 ('Secret-store carries structural token: ')
                LOAD_FAST_BORROW         5 (tok)
                FORMAT_SIMPLE
                BUILD_STRING             2

 448            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 449            LOAD_FAST_BORROW         4 (ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L11)
                NOT_TAKEN
                LOAD_CONST               4 ('')
                JUMP_FORWARD             4 (to L12)
       L11:     LOAD_CONST              14 ('missing token ')
                LOAD_FAST_BORROW         5 (tok)
                FORMAT_SIMPLE
                BUILD_STRING             2

 444   L12:     LOAD_CONST              11 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           74 (to L8)

 442   L13:     END_FOR
                POP_ITER

 454            LOAD_CONST              15 ('from cryptography.fernet')
                LOAD_DEREF              13 (src)
                CONTAINS_OP              0 (in)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        19 (to L14)
                NOT_TAKEN
                POP_TOP

 455            LOAD_CONST              16 ('cryptography.fernet')
                LOAD_DEREF              13 (src)
                CONTAINS_OP              0 (in)

 454            COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         6 (to L14)
                NOT_TAKEN
                POP_TOP

 456            LOAD_CONST              17 ('Fernet')
                LOAD_DEREF              13 (src)
                CONTAINS_OP              0 (in)

 453   L14:     STORE_FAST               6 (fernet_ref)

 458            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 459            LOAD_CONST              18 ('store:references_real_crypto_primitive')

 460            LOAD_FAST_BORROW         6 (fernet_ref)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L15)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L16)
       L15:     LOAD_CONST               8 ('FAIL')

 461   L16:     LOAD_CONST              19 ('Secret-store references the cryptography Fernet primitive')

 462            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 463            LOAD_FAST_BORROW         6 (fernet_ref)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L17)
                NOT_TAKEN
                LOAD_CONST               4 ('')
                JUMP_FORWARD             1 (to L18)
       L17:     LOAD_CONST              20 ('no real crypto primitive referenced')

 458   L18:     LOAD_CONST              11 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 465            LOAD_CONST              21 ('crypto_unavailable')
                LOAD_DEREF              13 (src)
                CONTAINS_OP              0 (in)
                STORE_FAST               7 (crypto_unavailable_branch)

 466            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 467            LOAD_CONST              22 ('store:no_fake_encryption')

 468            LOAD_FAST_BORROW         7 (crypto_unavailable_branch)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L19)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L20)
       L19:     LOAD_CONST               8 ('FAIL')

 469   L20:     LOAD_CONST              23 ('Secret-store fails closed when crypto is unavailable')

 470            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 471            LOAD_FAST_BORROW         7 (crypto_unavailable_branch)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L21)
                NOT_TAKEN
                LOAD_CONST               4 ('')
                JUMP_FORWARD             1 (to L22)
       L21:     LOAD_CONST              24 ('missing crypto_unavailable branch')

 466   L22:     LOAD_CONST              11 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 475            LOAD_CONST              25 ('is True')
                LOAD_DEREF              13 (src)
                CONTAINS_OP              0 (in)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       14 (to L23)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              26 ('email_forwarder_secret_encryption_enabled')
                LOAD_DEREF              13 (src)
                CONTAINS_OP              0 (in)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         6 (to L24)
                NOT_TAKEN
       L23:     POP_TOP

 476            LOAD_CONST              27 ('lower() == _ENV_TRUE_LITERAL')
                LOAD_DEREF              13 (src)
                CONTAINS_OP              0 (in)

 474   L24:     STORE_FAST               8 (strict_true)

 478            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 479            LOAD_CONST              28 ('store:strict_literal_true')

 480            LOAD_FAST_BORROW         8 (strict_true)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L25)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L26)
       L25:     LOAD_CONST               8 ('FAIL')

 481   L26:     LOAD_CONST              29 ('Encryption-enabled flag uses strict literal True')

 482            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 483            LOAD_FAST_BORROW         8 (strict_true)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L27)
                NOT_TAKEN
                LOAD_CONST               4 ('')
                JUMP_FORWARD             1 (to L28)
       L27:     LOAD_CONST              30 ("expected 'is True' or _ENV_TRUE_LITERAL comparison")

 478   L28:     LOAD_CONST              11 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 486            LOAD_CONST              31 ('plaintext_forwarder_secret_fallback')
                LOAD_DEREF              13 (src)
                CONTAINS_OP              0 (in)
                STORE_FAST               9 (fallback_ok)

 487            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 488            LOAD_CONST              32 ('store:plaintext_fallback_present')

 489            LOAD_FAST_BORROW         9 (fallback_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L29)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L30)
       L29:     LOAD_CONST               8 ('FAIL')

 490   L30:     LOAD_CONST              33 ('Secret-store retains plaintext-fallback path')

 491            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 492            LOAD_FAST_BORROW         9 (fallback_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L31)
                NOT_TAKEN
                LOAD_CONST               4 ('')
                JUMP_FORWARD             1 (to L32)
       L31:     LOAD_CONST              34 ('missing plaintext_forwarder_secret_fallback')

 487   L32:     LOAD_CONST              11 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 495            LOAD_CONST              46 (('encrypted_secret', 'raw_email', 'raw_body'))
                GET_ITER
       L33:     FOR_ITER               139 (to L43)
                STORE_FAST              10 (forbidden)

 499            LOAD_CONST              35 ('"')
                LOAD_FAST_BORROW        10 (forbidden)
                FORMAT_SIMPLE
                LOAD_CONST              36 ('":')
                BUILD_STRING             3
                LOAD_CONST              37 ("'")
                LOAD_FAST_BORROW        10 (forbidden)
                FORMAT_SIMPLE
                LOAD_CONST              38 ("':")
                BUILD_STRING             3
                BUILD_TUPLE              2
                STORE_FAST              11 (bad_shapes)

 500            LOAD_GLOBAL             16 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L37)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW        13 (src)
                BUILD_TUPLE              1
                LOAD_CONST              39 (<code object <genexpr> at 0x0000018C18026430, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 500>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW        11 (bad_shapes)
                GET_ITER
                CALL                     0
       L34:     FOR_ITER                12 (to L36)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L35)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L34)
       L35:     POP_ITER
                LOAD_CONST              40 (True)
                JUMP_FORWARD            20 (to L38)
       L36:     END_FOR
                POP_ITER
                LOAD_CONST              41 (False)
                JUMP_FORWARD            16 (to L38)
       L37:     PUSH_NULL
                LOAD_FAST_BORROW        13 (src)
                BUILD_TUPLE              1
                LOAD_CONST              39 (<code object <genexpr> at 0x0000018C18026430, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 500>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW        11 (bad_shapes)
                GET_ITER
                CALL                     0
                CALL                     1
       L38:     STORE_FAST              12 (present)

 501            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 502            LOAD_CONST              42 ('store:no_forbidden_response_key:')
                LOAD_FAST_BORROW        10 (forbidden)
                FORMAT_SIMPLE
                BUILD_STRING             2

 503            LOAD_FAST_BORROW        12 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L39)
                NOT_TAKEN
                LOAD_CONST               8 ('FAIL')
                JUMP_FORWARD             1 (to L40)
       L39:     LOAD_CONST               7 ('PASS')

 504   L40:     LOAD_CONST              43 ('Secret-store excludes forbidden response key: ')
                LOAD_FAST_BORROW        10 (forbidden)
                FORMAT_SIMPLE
                BUILD_STRING             2

 505            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 507            LOAD_FAST_BORROW        12 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        8 (to L41)
                NOT_TAKEN

 506            LOAD_CONST              44 ('forbidden key ')
                LOAD_FAST_BORROW        10 (forbidden)
                CONVERT_VALUE            2 (repr)
                FORMAT_SIMPLE
                LOAD_CONST              45 (' present as dict-key')
                BUILD_STRING             3
                JUMP_FORWARD             1 (to L42)

 507   L41:     LOAD_CONST               4 ('')

 501   L42:     LOAD_CONST              11 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          141 (to L33)

 495   L43:     END_FOR
                POP_ITER

 509            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18026430, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 500>:
  --           COPY_FREE_VARS           1

 500           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA24C0, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 512>:
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

Disassembly of <code object check_route_uses_helper at 0x0000018C17E8A0E0, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 512>:
512            RESUME                   0

513            BUILD_LIST               0
               STORE_FAST               1 (out)

514            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('routes')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('email_ingestion.py')
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
               LOAD_CONST               3 ('')
       L1:     STORE_FAST               3 (src)

516            LOAD_CONST               4 ('get_email_forwarder_secret')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               STORE_FAST               4 (helper_ref)

517            LOAD_FAST                1 (out)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_GLOBAL              7 (_check + NULL)

518            LOAD_CONST               5 ('route:uses_secret_store_helper')

519            LOAD_FAST_BORROW         4 (helper_ref)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L2)
               NOT_TAKEN
               LOAD_CONST               6 ('PASS')
               JUMP_FORWARD             1 (to L3)
       L2:     LOAD_CONST               7 ('FAIL')

520    L3:     LOAD_CONST               8 ('Route uses get_email_forwarder_secret helper')

521            LOAD_GLOBAL              8 (SEVERITY_BLOCK)

522            LOAD_FAST_BORROW         4 (helper_ref)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN
               LOAD_CONST               3 ('')
               JUMP_FORWARD             1 (to L5)
       L4:     LOAD_CONST               9 ('secret-store helper not referenced')

517    L5:     LOAD_CONST              10 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

525            LOAD_GLOBAL             11 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               5 (executable)

526            LOAD_CONST              22 (('body.brokerage_id', 'body["brokerage_id"]', "body['brokerage_id']"))
               GET_ITER
       L6:     FOR_ITER                80 (to L11)
               STORE_FAST               6 (bad_pattern)

531            LOAD_FAST_BORROW_LOAD_FAST_BORROW 101 (bad_pattern, executable)
               CONTAINS_OP              0 (in)
               STORE_FAST               7 (present)

532            LOAD_FAST                1 (out)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_GLOBAL              7 (_check + NULL)

533            LOAD_CONST              11 ('route:no_body_trust:')
               LOAD_FAST_BORROW         6 (bad_pattern)
               LOAD_CONST              12 (slice(None, 40, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

534            LOAD_FAST_BORROW         7 (present)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L7)
               NOT_TAKEN
               LOAD_CONST               7 ('FAIL')
               JUMP_FORWARD             1 (to L8)
       L7:     LOAD_CONST               6 ('PASS')

535    L8:     LOAD_CONST              13 ('Route never reads brokerage_id from body: ')
               LOAD_FAST_BORROW         6 (bad_pattern)
               FORMAT_SIMPLE
               BUILD_STRING             2

536            LOAD_GLOBAL              8 (SEVERITY_BLOCK)

538            LOAD_FAST_BORROW         7 (present)
               TO_BOOL
               POP_JUMP_IF_FALSE        8 (to L9)
               NOT_TAKEN

537            LOAD_CONST              14 ('body-trust pattern ')
               LOAD_FAST_BORROW         6 (bad_pattern)
               CONVERT_VALUE            2 (repr)
               FORMAT_SIMPLE
               LOAD_CONST              15 (' present')
               BUILD_STRING             3
               JUMP_FORWARD             1 (to L10)

538    L9:     LOAD_CONST               3 ('')

532   L10:     LOAD_CONST              10 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           82 (to L6)

526   L11:     END_FOR
               POP_ITER

541            LOAD_FAST_BORROW         3 (src)
               LOAD_ATTR               13 (find + NULL|self)
               LOAD_CONST              16 ('_EVENT_PAYLOAD_ALLOWED')
               CALL                     1
               STORE_FAST               8 (allow_idx)

542            LOAD_FAST_BORROW         8 (allow_idx)
               LOAD_SMALL_INT           0
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE       12 (to L12)
               NOT_TAKEN
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 56 (src, allow_idx)
               LOAD_FAST_BORROW         8 (allow_idx)
               LOAD_CONST              17 (1024)
               BINARY_OP                0 (+)
               BINARY_SLICE
               JUMP_FORWARD             1 (to L13)
      L12:     LOAD_CONST               3 ('')
      L13:     STORE_FAST               9 (allow_window)

543            LOAD_GLOBAL             14 (FORBIDDEN_EVENT_PAYLOAD_KEYS)
               GET_ITER
      L14:     FOR_ITER                79 (to L19)
               STORE_FAST              10 (forbidden)

544            LOAD_CONST              18 ('"')
               LOAD_FAST_BORROW        10 (forbidden)
               FORMAT_SIMPLE
               LOAD_CONST              18 ('"')
               BUILD_STRING             3
               STORE_FAST              11 (candidate)

545            LOAD_FAST_BORROW_LOAD_FAST_BORROW 185 (candidate, allow_window)
               CONTAINS_OP              0 (in)
               STORE_FAST              12 (present_in_allowed)

546            LOAD_FAST                1 (out)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_GLOBAL              7 (_check + NULL)

547            LOAD_CONST              19 ('route:event_allowlist_excludes:')
               LOAD_FAST_BORROW        10 (forbidden)
               FORMAT_SIMPLE
               BUILD_STRING             2

548            LOAD_FAST_BORROW        12 (present_in_allowed)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L15)
               NOT_TAKEN
               LOAD_CONST               7 ('FAIL')
               JUMP_FORWARD             1 (to L16)
      L15:     LOAD_CONST               6 ('PASS')

549   L16:     LOAD_CONST              20 ('Event payload allow-list excludes forbidden key: ')
               LOAD_FAST_BORROW        10 (forbidden)
               FORMAT_SIMPLE
               BUILD_STRING             2

550            LOAD_GLOBAL              8 (SEVERITY_BLOCK)

552            LOAD_FAST_BORROW        12 (present_in_allowed)
               TO_BOOL
               POP_JUMP_IF_FALSE        8 (to L17)
               NOT_TAKEN

551            LOAD_CONST              21 ('forbidden allow-list key ')
               LOAD_FAST_BORROW        10 (forbidden)
               CONVERT_VALUE            2 (repr)
               FORMAT_SIMPLE
               LOAD_CONST              15 (' present')
               BUILD_STRING             3
               JUMP_FORWARD             1 (to L18)

552   L17:     LOAD_CONST               3 ('')

546   L18:     LOAD_CONST              10 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           81 (to L14)

543   L19:     END_FOR
               POP_ITER

554            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 557>:
557           RESUME                   0
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

Disassembly of <code object check_reaper at 0x0000018C17F837D0, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 557>:
557            RESUME                   0

558            BUILD_LIST               0
               STORE_FAST               1 (out)

559            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('scripts')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('reap_email_dedupe.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

560            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               2 ('')
       L1:     STORE_FAST               3 (src)

561            LOAD_GLOBAL              4 (REQUIRED_REAPER_TOKENS)
               GET_ITER
       L2:     FOR_ITER                71 (to L7)
               STORE_FAST               4 (tok)

562            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

563            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

564            LOAD_CONST               3 ('reaper_token:')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

565            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               4 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               5 ('FAIL')

566    L4:     LOAD_CONST               6 ('Reaper declares CLI / mode token: ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

567            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

568            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST               7 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

563    L6:     LOAD_CONST               8 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           73 (to L2)

561    L7:     END_FOR
               POP_ITER

573            LOAD_CONST               9 ('"--execute"')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

574            LOAD_CONST              10 ('action="store_true"')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

572    L8:     STORE_FAST               6 (dry_run_default)

576            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

577            LOAD_CONST              11 ('reaper:dry_run_by_default')

578            LOAD_FAST_BORROW         6 (dry_run_default)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN
               LOAD_CONST               4 ('PASS')
               JUMP_FORWARD             1 (to L10)
       L9:     LOAD_CONST               5 ('FAIL')

579   L10:     LOAD_CONST              12 ('Reaper is dry-run by default')

580            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

581            LOAD_FAST_BORROW         6 (dry_run_default)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST              13 ('expected --execute store_true')

576   L12:     LOAD_CONST               8 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

585            LOAD_GLOBAL             13 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               7 (executable)

587            LOAD_CONST              14 ('dedupe_key')
               LOAD_FAST_BORROW         7 (executable)
               CONTAINS_OP              1 (not in)

586            STORE_FAST               8 (no_print_dedupe_key)

589            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

590            LOAD_CONST              15 ('reaper:no_dedupe_key_in_executable')

591            LOAD_FAST_BORROW         8 (no_print_dedupe_key)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L13)
               NOT_TAKEN
               LOAD_CONST               4 ('PASS')
               JUMP_FORWARD             1 (to L14)
      L13:     LOAD_CONST               5 ('FAIL')

592   L14:     LOAD_CONST              16 ('Reaper executable does not reference the dedupe key')

593            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

595            LOAD_FAST_BORROW         8 (no_print_dedupe_key)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L15)
               NOT_TAKEN

594            LOAD_CONST              17 ("'dedupe_key' present in reaper executable")
               JUMP_FORWARD             1 (to L16)

595   L15:     LOAD_CONST               2 ('')

589   L16:     LOAD_CONST               8 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

599            LOAD_CONST              18 ('return 0')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       19 (to L17)
               NOT_TAKEN
               POP_TOP

600            LOAD_CONST              19 ('return 1')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

599            COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        6 (to L17)
               NOT_TAKEN
               POP_TOP

601            LOAD_CONST              20 ('return 2')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

598   L17:     STORE_FAST               9 (has_exit_codes)

603            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

604            LOAD_CONST              21 ('reaper:exit_codes_present')

605            LOAD_FAST_BORROW         9 (has_exit_codes)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L18)
               NOT_TAKEN
               LOAD_CONST               4 ('PASS')
               JUMP_FORWARD             1 (to L19)
      L18:     LOAD_CONST               5 ('FAIL')

606   L19:     LOAD_CONST              22 ('Reaper declares exit codes 0/1/2')

607            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

608            LOAD_FAST_BORROW         9 (has_exit_codes)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L20)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L21)
      L20:     LOAD_CONST              23 ('expected return 0/1/2 branches')

603   L21:     LOAD_CONST               8 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

610            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 613>:
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

Disassembly of <code object check_event_contract at 0x0000018C17FEDC30, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 613>:
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 629>:
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

Disassembly of <code object check_no_forbidden_imports at 0x0000018C17D8B3B0, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 629>:
629            RESUME                   0

630            BUILD_LIST               0
               STORE_FAST               1 (out)

631            LOAD_CONST               9 (('app/services/ingestion/email_forwarder_secret_store.py', 'app/routes/email_ingestion.py', 'scripts/reap_email_dedupe.py', 'scripts/pas167_email_secret_reaper_readiness_check.py'))
               STORE_FAST               2 (files)

637            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               241 (to L12)
               STORE_FAST               3 (relpath)

638            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

639            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L2:     STORE_FAST               5 (src)

640            BUILD_LIST               0
               STORE_FAST               6 (bad)

641            LOAD_FAST_BORROW         5 (src)
               LOAD_ATTR                5 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L3:     FOR_ITER                74 (to L7)
               STORE_FAST               7 (line)

642            LOAD_FAST_BORROW         7 (line)
               LOAD_ATTR                7 (strip + NULL|self)
               CALL                     0
               STORE_FAST               8 (stripped)

643            LOAD_GLOBAL              8 (FORBIDDEN_IMPORT_LINE_PREFIXES)
               GET_ITER
       L4:     FOR_ITER                45 (to L6)
               STORE_FAST               9 (prefix)

644            LOAD_FAST_BORROW         8 (stripped)
               LOAD_ATTR               11 (startswith + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           28 (to L4)

645    L5:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR               13 (append + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           47 (to L4)

643    L6:     END_FOR
               POP_ITER
               JUMP_BACKWARD           76 (to L3)

641    L7:     END_FOR
               POP_ITER

646            LOAD_FAST                1 (out)
               LOAD_ATTR               13 (append + NULL|self)
               LOAD_GLOBAL             15 (_check + NULL)

647            LOAD_CONST               2 ('forbidden_import:')
               LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR               16 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

648            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST               4 ('PASS')

649    L9:     LOAD_CONST               5 ('No forbidden imports: ')
               LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR               16 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

650            LOAD_GLOBAL             18 (SEVERITY_BLOCK)

652            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L10)
               NOT_TAKEN

651            LOAD_CONST               6 ('forbidden import prefixes: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               21 (join + NULL|self)
               LOAD_FAST_BORROW         6 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L11)

652   L10:     LOAD_CONST               1 ('')

646   L11:     LOAD_CONST               8 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          243 (to L1)

637   L12:     END_FOR
               POP_ITER

654            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 657>:
657           RESUME                   0
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

Disassembly of <code object check_no_inbox_scanning at 0x0000018C17CC1CE0, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 657>:
657            RESUME                   0

658            BUILD_LIST               0
               STORE_FAST               1 (out)

659            LOAD_CONST               9 (('app/services/ingestion/email_forwarder_secret_store.py', 'app/routes/email_ingestion.py', 'scripts/reap_email_dedupe.py'))
               STORE_FAST               2 (files)

664            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               196 (to L10)
               STORE_FAST               3 (relpath)

665            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

666            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L2:     STORE_FAST               5 (src)

667            LOAD_GLOBAL              5 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         5 (src)
               CALL                     1
               STORE_FAST               6 (executable)

668            BUILD_LIST               0
               STORE_FAST               7 (bad)

669            LOAD_GLOBAL              6 (FORBIDDEN_INBOX_TOKENS)
               GET_ITER
       L3:     FOR_ITER                28 (to L5)
               STORE_FAST               8 (token)

670            LOAD_FAST_BORROW_LOAD_FAST_BORROW 134 (token, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L3)

671    L4:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_FAST_BORROW         8 (token)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L3)

669    L5:     END_FOR
               POP_ITER

672            LOAD_FAST                1 (out)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_GLOBAL             11 (_check + NULL)

673            LOAD_CONST               2 ('no_inbox_scan:')
               LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR               12 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

674            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L6)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L7)
       L6:     LOAD_CONST               4 ('PASS')

675    L7:     LOAD_CONST               5 ('No inbox-scanning tokens: ')
               LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR               12 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

676            LOAD_GLOBAL             14 (SEVERITY_BLOCK)

678            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L8)
               NOT_TAKEN

677            LOAD_CONST               6 ('inbox-scan tokens present: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               17 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L9)

678    L8:     LOAD_CONST               1 ('')

672    L9:     LOAD_CONST               8 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          198 (to L1)

664   L10:     END_FOR
               POP_ITER

680            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 683>:
683           RESUME                   0
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

Disassembly of <code object check_docs_required_doctrine at 0x0000018C17F73EF0, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 683>:
  --            MAKE_CELL                8 (lower)

 683            RESUME                   0

 684            BUILD_LIST               0
                STORE_FAST               1 (out)

 685            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('docs')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('pas167_email_secret_encryption_and_dedupe_reaper.md')
                BINARY_OP               11 (/)
                STORE_FAST               2 (doc)

 686            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (doc)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L1:     STORE_FAST               3 (src)

 687            LOAD_FAST_BORROW         3 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_DEREF              8 (lower)

 688            LOAD_CONST              13 ((('purpose', ('purpose',)), ('relationship-prior', ('pas164', 'pas165', 'pas166')), ('why-secret-encrypt', ('at rest', 'at-rest', 'encryption matters')), ('migration-proposal', ('migration', 'proposal')), ('encryption-flag', ('encryption', 'enabled')), ('plaintext-fallback', ('plaintext fallback', 'plaintext_forwarder_secret_fallback')), ('no-fake-encryption', ('no fake encryption', 'fake encryption')), ('reaper', ('reaper', 'dry-run', 'dry run')), ('event-safety', ('event payload safety', 'event payload', 'allow-list')), ('no-raw-storage', ('no raw email', 'raw email body', 'no raw body')), ('no-gmail', ('no gmail oauth', 'no gmail')), ('no-inbox-scan', ('no inbox scanning', 'no inbox')), ('not-built', ('intentionally not built', 'deliberately not', 'what is intentionally')), ('brokerage-pilot', ('brokerage pilot', 'brokerage pilots', 'real brokerage')), ('limitations', ('limitation', 'limitations'))))
                STORE_FAST               4 (required_phrases)

 710            LOAD_FAST_BORROW         4 (required_phrases)
                GET_ITER
        L2:     FOR_ITER               146 (to L12)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   86 (name, phrases)

 711            LOAD_GLOBAL              6 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         8 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18025E30, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 711>)
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
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18025E30, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 711>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         6 (phrases)
                GET_ITER
                CALL                     0
                CALL                     1
        L7:     STORE_FAST               7 (present)

 712            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 713            LOAD_CONST               6 ('docs:phrase:')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 714            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               8 ('FAIL')

 715    L9:     LOAD_CONST               9 ('Doc carries clause: ')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 716            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 718            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L10)
                NOT_TAKEN

 717            LOAD_CONST              10 ('expected one of: ')
                LOAD_CONST              11 (' | ')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_FAST_BORROW         6 (phrases)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L11)

 718   L10:     LOAD_CONST               2 ('')

 712   L11:     LOAD_CONST              12 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          148 (to L2)

 710   L12:     END_FOR
                POP_ITER

 720            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18025E30, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 711>:
  --           COPY_FREE_VARS           1

 711           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3000, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 723>:
723           RESUME                   0
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

Disassembly of <code object check_self_no_env_or_vendor at 0x0000018C17E56380, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 723>:
723            RESUME                   0

724            BUILD_LIST               0
               STORE_FAST               1 (out)

725            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_GLOBAL              2 (__file__)
               CALL                     1
               LOAD_ATTR                5 (resolve + NULL|self)
               CALL                     0
               STORE_FAST               2 (self_path)

726            LOAD_GLOBAL              7 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (self_path)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L1:     STORE_FAST               3 (src)

727            BUILD_LIST               0
               STORE_FAST               4 (bad)

728            LOAD_FAST_BORROW         3 (src)
               LOAD_ATTR                9 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L2:     EXTENDED_ARG             1
               FOR_ITER               311 (to L11)
               STORE_FAST               5 (raw_line)

729            LOAD_FAST_BORROW         5 (raw_line)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0
               STORE_FAST               6 (stripped)

730            LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST               1 ('#')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

731            JUMP_BACKWARD           45 (to L2)

732    L3:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              16 (('import dotenv', 'from dotenv'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L4)
               NOT_TAKEN

733            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               2 ('dotenv import')
               CALL                     1
               POP_TOP

734    L4:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              17 (('import supabase', 'from supabase'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L5)
               NOT_TAKEN

735            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               3 ('supabase import')
               CALL                     1
               POP_TOP

736    L5:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              18 (('import composio', 'from composio', 'import trustclaw', 'from trustclaw', 'import openai', 'from openai', 'import anthropic', 'from anthropic', 'import googleapiclient', 'from googleapiclient', 'import google.oauth2', 'from google.oauth2'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L6)
               NOT_TAKEN

744            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               4 ('external-vendor / google import')
               CALL                     1
               POP_TOP

745    L6:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              19 (('import numpy', 'import faiss', 'import pgvector', 'from pgvector', 'from openai import embeddings', 'from openai.embeddings'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L7)
               NOT_TAKEN

751            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               5 ('embedding / vector import')
               CALL                     1
               POP_TOP

752    L7:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST               6 ('load_dotenv()')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        24 (to L8)
               NOT_TAKEN

753            LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               17 (endswith + NULL|self)
               LOAD_CONST               6 ('load_dotenv()')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L9)
               NOT_TAKEN

754    L8:     LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               7 ('load_dotenv() call')
               CALL                     1
               POP_TOP

755    L9:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              20 (('os.environ[', 'os.getenv(', 'getenv('))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         4 (to L10)
               NOT_TAKEN
               EXTENDED_ARG             1
               JUMP_BACKWARD          294 (to L2)

756   L10:     LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               8 ('environ read')
               CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          314 (to L2)

728   L11:     END_FOR
               POP_ITER

757            LOAD_FAST                1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             19 (_check + NULL)

758            LOAD_CONST               9 ('self_check:no_env_or_vendor')

759            LOAD_FAST_BORROW         4 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L12)
               NOT_TAKEN
               LOAD_CONST              10 ('FAIL')
               JUMP_FORWARD             1 (to L13)
      L12:     LOAD_CONST              11 ('PASS')

760   L13:     LOAD_CONST              12 ('PAS167 readiness checker never reads .env, calls Supabase, or imports vendor / Google / embedding libs')

762            LOAD_GLOBAL             20 (SEVERITY_BLOCK)

764            LOAD_FAST_BORROW         4 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L14)
               NOT_TAKEN

763            LOAD_CONST              13 ('disqualifying code-line patterns: ')
               LOAD_CONST              14 (', ')
               LOAD_ATTR               23 (join + NULL|self)
               LOAD_FAST_BORROW         4 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L15)

764   L14:     LOAD_CONST               0 ('')

757   L15:     LOAD_CONST              15 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

766            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180FC210, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 773>:
773           RESUME                   0
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

Disassembly of <code object _aggregate at 0x0000018C17EC57C0, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 773>:
 773            RESUME                   0

 775            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 774            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2

 775    L2:     FOR_ITER                49 (to L7)
                STORE_FAST               1 (c)

 776            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 775    L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L2)

 776    L4:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              2 (SEVERITY_BLOCK)
                COMPARE_OP              88 (bool(==))

 775    L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L2)
        L6:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L2)
        L7:     END_FOR
                POP_ITER

 774    L8:     STORE_FAST               2 (blockers)
                STORE_FAST               1 (c)

 779            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 778            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L9:     BUILD_LIST               0
                SWAP                     2

 779   L10:     FOR_ITER                49 (to L15)
                STORE_FAST               1 (c)

 780            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 779   L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L10)

 780   L12:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              4 (SEVERITY_INFO)
                COMPARE_OP              88 (bool(==))

 779   L13:     POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L10)
       L14:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L10)
       L15:     END_FOR
                POP_ITER

 778   L16:     STORE_FAST               3 (info)
                STORE_FAST               1 (c)

 783            LOAD_CONST               3 ('verdict')
                LOAD_FAST_BORROW         2 (blockers)
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L17)
                NOT_TAKEN
                LOAD_GLOBAL              6 (VERDICT_NOT_READY)
                JUMP_FORWARD             5 (to L18)
       L17:     LOAD_GLOBAL              8 (VERDICT_READY)

 784   L18:     LOAD_CONST               4 ('blockers')
                LOAD_FAST_BORROW         2 (blockers)

 785            LOAD_CONST               5 ('info')
                LOAD_FAST_BORROW         3 (info)

 782            BUILD_MAP                3
                RETURN_VALUE

  --   L19:     SWAP                     2
                POP_TOP

 774            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0

  --   L20:     SWAP                     2
                POP_TOP

 778            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L19 [2]
  L4 to L5 -> L19 [2]
  L6 to L8 -> L19 [2]
  L9 to L11 -> L20 [2]
  L12 to L13 -> L20 [2]
  L14 to L16 -> L20 [2]

Disassembly of <code object __annotate__ at 0x0000018C180FC120, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 789>:
789           RESUME                   0
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

Disassembly of <code object _operator_actions at 0x0000018C18048730, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 789>:
789           RESUME                   0

790           BUILD_LIST               0
              STORE_FAST               1 (out)

791           LOAD_FAST_BORROW         0 (checks)
              GET_ITER
      L1:     FOR_ITER               109 (to L5)
              STORE_FAST               2 (c)

792           LOAD_FAST_BORROW         2 (c)
              LOAD_CONST               0 ('status')
              BINARY_OP               26 ([])
              LOAD_CONST               1 ('FAIL')
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

793           JUMP_BACKWARD           19 (to L1)

794   L2:     LOAD_FAST_BORROW         2 (c)
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

795           LOAD_FAST                1 (out)
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

791   L5:     END_FOR
              POP_ITER

796           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180FC300, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 799>:
799           RESUME                   0
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

Disassembly of <code object evaluate at 0x0000018C17E56800, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 799>:
799           RESUME                   0

800           BUILD_LIST               0
              STORE_FAST               1 (checks)

801           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              3 (check_files_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

802           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              5 (check_prior_phases_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

803           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              7 (check_memory_review_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

804           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              9 (check_migration_proposal + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

805           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             11 (check_secret_store + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

806           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             13 (check_route_uses_helper + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

807           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             15 (check_reaper + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

808           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             17 (check_event_contract + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

809           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             19 (check_no_forbidden_imports + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

810           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             21 (check_no_inbox_scanning + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

811           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             23 (check_docs_required_doctrine + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

812           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             25 (check_self_no_env_or_vendor + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

814           LOAD_GLOBAL             27 (_aggregate + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1
              STORE_FAST               2 (agg)

816           LOAD_CONST               0 ('phase')
              LOAD_CONST               1 ('PAS167')

817           LOAD_CONST               2 ('generated_at')
              LOAD_GLOBAL             29 (_now_iso + NULL)
              CALL                     0

818           LOAD_CONST               3 ('verdict')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])

819           LOAD_CONST               4 ('ready')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])
              LOAD_GLOBAL             30 (VERDICT_READY)
              COMPARE_OP              72 (==)

820           LOAD_CONST               5 ('blocker_count')
              LOAD_GLOBAL             33 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               6 ('blockers')
              BINARY_OP               26 ([])
              CALL                     1

821           LOAD_CONST               7 ('info_count')
              LOAD_GLOBAL             33 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               8 ('info')
              BINARY_OP               26 ([])
              CALL                     1

822           LOAD_CONST               9 ('check_count')
              LOAD_GLOBAL             33 (len + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

823           LOAD_CONST              10 ('pass_count')
              LOAD_GLOBAL             35 (sum + NULL)
              LOAD_CONST              11 (<code object <genexpr> at 0x0000018C18053AB0, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 823>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

824           LOAD_CONST              12 ('fail_count')
              LOAD_GLOBAL             35 (sum + NULL)
              LOAD_CONST              13 (<code object <genexpr> at 0x0000018C18053CF0, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 824>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

825           LOAD_CONST              14 ('checks')
              LOAD_FAST_BORROW         1 (checks)

826           LOAD_CONST              15 ('operator_actions')
              LOAD_GLOBAL             37 (_operator_actions + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

815           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18053AB0, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 823>:
 823           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C18053CF0, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 824>:
 824           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C180FCA80, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 833>:
833           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C179A7290, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 833>:
833           RESUME                   0

834           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

835           LOAD_CONST               0 ('pas167_email_secret_reaper_readiness_check')

837           LOAD_CONST               1 ('PAS167 — Evaluate the email forwarder secret-at-rest encryption seam + the dedupe reaper for structural correctness, no fake encryption, no Gmail / inbox / vendor imports, and no PII leakage from the reaper. Read-only. Does not touch Supabase, .env, or tenant data.')

834           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

845           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

846           LOAD_CONST               3 ('--repo-root')
              LOAD_GLOBAL              6 (_REPO_ROOT_DEFAULT)

847           LOAD_CONST               4 ('Repo root to evaluate (default: parent of this script).')

845           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

849           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

850           LOAD_CONST               6 ('--output')
              LOAD_GLOBAL              8 (REPORT_FILENAME)

851           LOAD_CONST               7 ('Where to write the JSON report (default ./')
              LOAD_GLOBAL              8 (REPORT_FILENAME)
              FORMAT_SIMPLE
              LOAD_CONST               8 (').')
              BUILD_STRING             3

849           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

853           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

854           LOAD_CONST               9 ('--json')
              LOAD_CONST              10 ('store_true')

855           LOAD_CONST              11 ('Emit the report JSON on stdout in addition to the file.')

853           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

857           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

858           LOAD_CONST              13 ('--summary-only')
              LOAD_CONST              10 ('store_true')

859           LOAD_CONST              14 ('Skip writing the full report file; print verdict only.')

857           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

861           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

862           LOAD_CONST              15 ('--strict')
              LOAD_CONST              10 ('store_true')

863           LOAD_CONST              16 ('Exit 1 unless verdict == READY (default policy is the same).')

861           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

865           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180FC3F0, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 868>:
868           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C17D8E300, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 868>:
868           RESUME                   0

869           LOAD_GLOBAL              1 (print + NULL)

870           LOAD_CONST               0 ('[PAS167] verdict=')
              LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               1 ('verdict')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               2 (' blockers=')

871           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               3 ('blocker_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' info=')

872           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               5 ('info_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' checks=')

873           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               7 ('check_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' pass=')

874           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               9 ('pass_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              10 (' fail=')

875           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              11 ('fail_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE

870           BUILD_STRING            12

869           CALL                     1
              POP_TOP

877           LOAD_FAST_BORROW         0 (report)
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

878           LOAD_FAST_BORROW         1 (actions)
              TO_BOOL
              POP_JUMP_IF_FALSE       93 (to L5)
              NOT_TAKEN

879           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              13 ('[PAS167] operator actions:')
              CALL                     1
              POP_TOP

880           LOAD_FAST_BORROW         1 (actions)
              LOAD_CONST              14 (slice(None, 25, None))
              BINARY_OP               26 ([])
              GET_ITER
      L2:     FOR_ITER                17 (to L3)
              STORE_FAST               2 (a)

881           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              15 ('  - ')
              LOAD_FAST_BORROW         2 (a)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L2)

880   L3:     END_FOR
              POP_ITER

882           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         1 (actions)
              CALL                     1
              LOAD_SMALL_INT          25
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       34 (to L4)
              NOT_TAKEN

883           LOAD_GLOBAL              1 (print + NULL)
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

882   L4:     LOAD_CONST              18 (None)
              RETURN_VALUE

878   L5:     LOAD_CONST              18 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024F30, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 886>:
886           RESUME                   0
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

Disassembly of <code object _write_report at 0x0000018C18104210, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 886>:
 886           RESUME                   0

 887           NOP

 888   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

 889           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

 890           LOAD_CONST               3 ('utf-8')

 888           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 892           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

 893   L4:     LOAD_GLOBAL             11 (print + NULL)

 894           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

 895           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

 894           BUILD_STRING             4

 896           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

 893           LOAD_CONST               7 (('file',))
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

 892   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C180FC4E0, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 900>:
900           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17F842E0, file "scripts\pas167_email_secret_reaper_readiness_check.py", line 900>:
 900            RESUME                   0

 901            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 902            NOP

 903    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 907    L2:     LOAD_GLOBAL             10 (os)
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

 908            LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               21 (isdir + NULL|self)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L4)
                NOT_TAKEN

 909            LOAD_GLOBAL             23 (print + NULL)

 910            LOAD_CONST               2 ('error: --repo-root not a directory: ')
                LOAD_FAST                4 (repo_root)
                FORMAT_SIMPLE
                BUILD_STRING             2

 911            LOAD_GLOBAL             24 (sys)
                LOAD_ATTR               26 (stderr)

 909            LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

 913            LOAD_SMALL_INT           2
                RETURN_VALUE

 915    L4:     LOAD_GLOBAL             29 (evaluate + NULL)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                STORE_FAST               5 (report)

 917            LOAD_FAST                2 (args)
                LOAD_ATTR               30 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L5)
                NOT_TAKEN

 918            LOAD_GLOBAL             33 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               34 (output)
                LOAD_FAST                5 (report)
                CALL                     2
                POP_TOP

 920    L5:     LOAD_GLOBAL             37 (_print_summary + NULL)
                LOAD_FAST                5 (report)
                CALL                     1
                POP_TOP

 922            LOAD_FAST                2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L6)
                NOT_TAKEN

 923            LOAD_GLOBAL             23 (print + NULL)
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

 925    L6:     LOAD_FAST                5 (report)
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

 904            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L17)
                NOT_TAKEN
                STORE_FAST               3 (e)

 905    L9:     LOAD_FAST                3 (e)
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

 904   L17:     RERAISE                  0

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
