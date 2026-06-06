# scripts_readiness/pas_launch_integrity_check

- **pyc:** `scripts\__pycache__\pas_launch_integrity_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/pas_launch_integrity_check.py`
- **co_filename (from bytecode):** `C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS-LAUNCH-01 — Final deployment integrity gate.

Single aggregate gate that closes every remaining deployment
-integrity knot before pilot launch. **Not a feature phase.**
No new product functionality is introduced; the checker only
verifies posture across the existing PAS160 → PAS169
artefacts.

What this gate verifies (every check is a BLOCK unless
noted):

  * cryptography is declared in ``requirements.txt`` AND
    importable in the active Python env.
  * PAS169 crypto-roundtrip + launch-readiness scripts exist
    and are invokable.
  * PAS160 → PAS169 readiness scripts all exist (PAS160 has
    one INFO-only carryover that we tolerate here).
  * No migration script is auto-executed anywhere in the
    repo. Migrations remain operator-driven.
  * The pending-call worker remains OFF by default
    (``_ENV_FLAG_ENABLED_LITERAL = "true"`` invariant).
  * No FastAPI startup hook auto-starts the worker. The
    FastAPI lifespan in ``app/main.py`` must not import or
    schedule the worker loop.
  * Email-ingestion routes remain auth-scoped
    (``require_admin`` on /parse, ``require_brokerage`` on
    /ingest).
  * No body-trust ``brokerage_id`` paths exist in the
    ingestion code.
  * No plaintext-drop migration has been added yet — PAS167
    /PAS168 are intentionally non-destructive.
  * No forbidden imports anywhere in ``app/`` or
    ``scripts/``:
      Gmail, googleapiclient, google.oauth2, imaplib,
      poplib, composio, trustclaw, chromadb, pinecone,
      langchain, numpy, faiss, pgvector.
  * No inbox-scan tokens in any ingestion or launch script.
  * No raw email / raw transcript persistence paths in the
    email-ingestion subsystem.
  * No localhost / 127.0.0.1 HTTP self-call in the
    production code path (outbound dial adapter +
    ingestion). Config defaults and PAS163 forbidden-token
    lists are excluded.
  * The PAS169 launch docs exist.

What this gate does **NOT** do:

  * Read ``.env``.
  * Touch the database.
  * Execute any migration.
  * Call any external API.
  * Print key material, plaintext, ciphertext, or PII.

Usage:
  python scripts/pas_launch_integrity_check.py
  python scripts/pas_launch_integrity_check.py --json
  python scripts/pas_launch_integrity_check.py --summary-only
  python scripts/pas_launch_integrity_check.py --strict

Exit codes:
    0  — READY
    1  — NOT_READY
    2  — bad CLI arguments
```

## Imports

`Iterable`, `List`, `Optional`, `Path`, `Tuple`, `__future__`, `annotations`, `argparse`, `datetime`, `importlib.util`, `json`, `os`, `pathlib`, `sys`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_aggregate`, `_build_parser`, `_check`, `_now_iso`, `_operator_actions`, `_print_summary`, `_read_text`, `_strip_python_comments_and_strings`, `_walk_python_files`, `_write_report`, `check_crypto_importable`, `check_email_routes_auth_scoped`, `check_memory_review_intact`, `check_no_body_trust`, `check_no_forbidden_future_files`, `check_no_forbidden_imports`, `check_no_inbox_scan_tokens`, `check_no_localhost_self_call`, `check_no_migration_execution`, `check_no_raw_payload_persistence`, `check_no_startup_worker`, `check_pas169_doc_present`, `check_required_files`, `check_requirements_cryptography`, `check_self_no_env_or_db`, `check_worker_off_by_default`, `evaluate`, `main`

## Env-key candidates

`BLOCK`, `FAIL`, `INFO`, `NOT_READY`, `PASS`, `READY`

## String constants (redacted where noted)

- '\nPAS-LAUNCH-01 — Final deployment integrity gate.\n\nSingle aggregate gate that closes every remaining deployment\n-integrity knot before pilot launch. **Not a feature phase.**\nNo new product functionality is introduced; the checker only\nverifies posture across the existing PAS160 → PAS169\nartefacts.\n\nWhat this gate verifies (every check is a BLOCK unless\nnoted):\n\n  * cryptography is declared in ``requirements.txt`` AND\n    importable in the active Python env.\n  * PAS169 crypto-roundtrip + launch-readiness scripts exist\n    and are invokable.\n  * PAS160 → PAS169 readiness scripts all exist (PAS160 has\n    one INFO-only carryover that we tolerate here).\n  * No migration script is auto-executed anywhere in the\n    repo. Migrations remain operator-driven.\n  * The pending-call worker remains OFF by default\n    (``_ENV_FLAG_ENABLED_LITERAL = "true"`` invariant).\n  * No FastAPI startup hook auto-starts the worker. The\n    FastAPI lifespan in ``app/main.py`` must not import or\n    schedule the worker loop.\n  * Email-ingestion routes remain auth-scoped\n    (``require_admin`` on /parse, ``require_brokerage`` on\n    /ingest).\n  * No body-trust ``brokerage_id`` paths exist in the\n    ingestion code.\n  * No plaintext-drop migration has been added yet — PAS167\n    /PAS168 are intentionally non-destructive.\n  * No forbidden imports anywhere in ``app/`` or\n    ``scripts/``:\n      Gmail, googleapiclient, google.oauth2, imaplib,\n      poplib, composio, trustclaw, chromadb, pinecone,\n      langchain, numpy, faiss, pgvector.\n  * No inbox-scan tokens in any ingestion or launch script.\n  * No raw email / raw transcript persistence paths in the\n    email-ingestion subsystem.\n  * No localhost / 127.0.0.1 HTTP self-call in the\n    production code path (outbound dial adapter +\n    ingestion). Config defaults and PAS163 forbidden-token\n    lists are excluded.\n  * The PAS169 launch docs exist.\n\nWhat this gate does **NOT** do:\n\n  * Read ``.env``.\n  * Touch the database.\n  * Execute any migration.\n  * Call any external API.\n  * Print key material, plaintext, ciphertext, or PII.\n\nUsage:\n  python scripts/pas_launch_integrity_check.py\n  python scripts/pas_launch_integrity_check.py --json\n  python scripts/pas_launch_integrity_check.py --summary-only\n  python scripts/pas_launch_integrity_check.py --strict\n\nExit codes:\n    0  — READY\n    1  — NOT_READY\n    2  — bad CLI arguments\n'
- 'utf-8'
- 'READY'
- 'NOT_READY'
- 'BLOCK'
- 'INFO'
- 'severity'
- 'detail'
- 'pas_launch_integrity_report.json'
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
- 'root'
- 'subdirs'
- 'Iterable[str]'
- 'List[Path]'
- 'Walk Python files under each named subdir. Skips\n``__pycache__`` directories. Sorted for stable output.'
- '*.py'
- 'repo_root'
- 'List[dict]'
- 'required_file:'
- 'PASS'
- 'FAIL'
- 'Required PAS-LAUNCH-01 artefact present: '
- 'missing'
- 'memory_review_file:'
- 'Memory Review file present: '
- 'Memory Review file deleted'
- 'forbidden_future_file:'
- 'Plaintext-drop migration absent: '
- 'file '
- ' present — destructive cutover NOT in scope'
- 'requirements.txt'
- 'cryptography'
- '>=42'
- '==42'
- '~=42'
- '>=43'
- '>=44'
- 'requirements:cryptography_ge_42'
- 'requirements.txt declares cryptography>=42'
- 'cryptography>=42 not found in requirements.txt'
- ' Run `pip install -r requirements.txt` in this Python environment before launch.'
- 'cryptography.fernet'
- 'crypto:importable'
- 'cryptography.fernet is importable'
- 'find_spec raised '
- ' — cryptography is not importable in this Python environment.'
- 'cryptography is declared in requirements.txt but is NOT installed in this Python environment. Run `pip install -r requirements.txt` before launch.'
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
- 'routes'
- 'email_ingestion.py'
- '@router.post("'
- "@router.post('"
- 'route_auth:'
- 'Route '
- ' is auth-scoped via '
- 'missing route decl'
- 'missing '
- ' reference'
- 'app/routes/email_ingestion.py'
- 'body_trust:'
- 'No body-trust brokerage_id paths: '
- 'body-trust patterns present: '
- 'Scan every .py file under ``app/`` for forbidden\nimport lines. The ``scripts/`` tree is excluded from this\nscan because PAS readiness checkers legitimately list\nthese tokens in FORBIDDEN string tuples — string literals\nwould not match ``startswith`` import patterns but the\nline-start check on import statements gives us cleaner\nresults when we limit to ``app/``.\n\nFor ``scripts/`` we run a tighter scan: only the launch-\nintegrity + roundtrip + launch-readiness scripts must be\nclean. Prior-phase readiness scripts are exempt because\nthey are read-only static-text walkers (the strings live\nin tuples, never in executable import lines).'
- 'scripts'
- 'pas_launch_integrity_check.py'
- 'pas169_crypto_roundtrip_check.py'
- 'pas169_launch_readiness_check.py'
- 'forbidden_import:'
- 'No forbidden imports in '
- 'forbidden import prefixes: '
- 'forbidden_import:scan'
- ' scanned app/+launch-script files'
- 'app/services/ingestion/email_parser.py'
- 'no_inbox_scan:'
- 'No inbox-scanning tokens: '
- 'inbox-scan tokens present: '
- 'scripts/pas_launch_integrity_check.py'
- 'no_migration_execute:'
- 'No migration-execution tokens: '
- 'migration-execute tokens present: '
- 'Scan the email-ingestion subsystem for raw-email /\nraw-body / raw-transcript persistence paths.\n\nThe intent is to catch dict-key assignments + JSON-shape\nkeys that would persist the raw payload — NOT parameter\nnames. The PAS164+ parser legitimately accepts\n``raw_email`` as the public function parameter name\n(the spec mandates that signature). What it must never\ndo is write a key ``"raw_email"`` into any returned\ndict or persisted row.\n\nWe look for dict-key shapes (``"raw_email":`` /\n``\'raw_email\':``) in the raw source — those are the\npersistence shape we forbid. String literals inside\nFORBIDDEN denylist tuples are explicitly allowed (they\nare the parser\'s own self-enforcement). We rely on the\nPAS164/PAS165/PAS167 readiness checkers to enforce\ndeny-list completeness; this integrity gate only\ncatches a *positive* persistence regression.\n'
- 'no_raw_persistence:'
- 'No raw-payload persistence path: '
- 'forbidden dict-key shapes present: '
- 'Scan production code paths for ``http://localhost`` /\n``http://127.0.0.1`` HTTP self-call patterns. Config\ndefaults and forbidden-token lists are exempt via\n``LOCALHOST_SCAN_EXEMPT_FILES``.'
- 'localhost_self_call:'
- 'No localhost HTTP self-call in production: '
- 'localhost tokens: '
- 'localhost_self_call:scan'
- 'No localhost HTTP self-call in production code'
- 'PAS169 launch doc must exist (already checked in\n``check_required_files`` — this is an explicit second\nblock-level assertion for operator clarity).'
- 'docs'
- 'pas169_crypto_roundtrip_launch_gate.md'
- 'pas169_doc:present'
- 'PAS169 launch doc is present'
- 'docs/pas169_crypto_roundtrip_launch_gate.md missing'
- 'Self-check: this script never reads .env, never calls\nSupabase, never imports vendor SDKs.'
- 'dotenv import'
- 'supabase import'
- 'load_dotenv()'
- 'load_dotenv() call'
- 'environ read'
- 'get_supabase'
- 'supabase client call'
- 'self_check:no_env_or_db'
- 'Launch integrity checker never reads .env / touches DB'
- 'disqualifying code-line patterns: '
- 'checks'
- 'verdict'
- 'blockers'
- 'info'
- 'List[str]'
- ' — '
- 'see report'
- 'phase'
- 'PAS-LAUNCH-01'
- 'generated_at'
- 'ready'
- 'blocker_count'
- 'info_count'
- 'check_count'
- 'pass_count'
- 'fail_count'
- 'operator_actions'
- 'argparse.ArgumentParser'
- 'pas_launch_integrity_check'
- 'PAS-LAUNCH-01 — Single aggregate launch gate. Verifies crypto installability, worker safety, migration posture, route integrity, raw-payload absence, and forbidden-import absence before pilot launch. Read-only — never reads .env, never writes to the DB, never executes a migration, never calls any external API.'
- '--repo-root'
- 'Repo root to evaluate (default: parent of this script).'
- '--output'
- 'Where to write the JSON report (default ./'
- '--json'
- 'store_true'
- 'Emit the report JSON on stdout in addition to the summary.'
- '--summary-only'
- 'Skip writing the full report file; print verdict only.'
- '--strict'
- 'Exit 1 unless verdict == READY (default policy is the same).'
- 'report'
- 'None'
- '[PAS-LAUNCH-01] verdict='
- ' blockers='
- ' info='
- ' checks='
- ' pass='
- ' fail='
- '[PAS-LAUNCH-01] operator actions:'
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

   1           LOAD_CONST               0 ('\nPAS-LAUNCH-01 — Final deployment integrity gate.\n\nSingle aggregate gate that closes every remaining deployment\n-integrity knot before pilot launch. **Not a feature phase.**\nNo new product functionality is introduced; the checker only\nverifies posture across the existing PAS160 → PAS169\nartefacts.\n\nWhat this gate verifies (every check is a BLOCK unless\nnoted):\n\n  * cryptography is declared in ``requirements.txt`` AND\n    importable in the active Python env.\n  * PAS169 crypto-roundtrip + launch-readiness scripts exist\n    and are invokable.\n  * PAS160 → PAS169 readiness scripts all exist (PAS160 has\n    one INFO-only carryover that we tolerate here).\n  * No migration script is auto-executed anywhere in the\n    repo. Migrations remain operator-driven.\n  * The pending-call worker remains OFF by default\n    (``_ENV_FLAG_ENABLED_LITERAL = "true"`` invariant).\n  * No FastAPI startup hook auto-starts the worker. The\n    FastAPI lifespan in ``app/main.py`` must not import or\n    schedule the worker loop.\n  * Email-ingestion routes remain auth-scoped\n    (``require_admin`` on /parse, ``require_brokerage`` on\n    /ingest).\n  * No body-trust ``brokerage_id`` paths exist in the\n    ingestion code.\n  * No plaintext-drop migration has been added yet — PAS167\n    /PAS168 are intentionally non-destructive.\n  * No forbidden imports anywhere in ``app/`` or\n    ``scripts/``:\n      Gmail, googleapiclient, google.oauth2, imaplib,\n      poplib, composio, trustclaw, chromadb, pinecone,\n      langchain, numpy, faiss, pgvector.\n  * No inbox-scan tokens in any ingestion or launch script.\n  * No raw email / raw transcript persistence paths in the\n    email-ingestion subsystem.\n  * No localhost / 127.0.0.1 HTTP self-call in the\n    production code path (outbound dial adapter +\n    ingestion). Config defaults and PAS163 forbidden-token\n    lists are excluded.\n  * The PAS169 launch docs exist.\n\nWhat this gate does **NOT** do:\n\n  * Read ``.env``.\n  * Touch the database.\n  * Execute any migration.\n  * Call any external API.\n  * Print key material, plaintext, ciphertext, or PII.\n\nUsage:\n  python scripts/pas_launch_integrity_check.py\n  python scripts/pas_launch_integrity_check.py --json\n  python scripts/pas_launch_integrity_check.py --summary-only\n  python scripts/pas_launch_integrity_check.py --strict\n\nExit codes:\n    0  — READY\n    1  — NOT_READY\n    2  — bad CLI arguments\n')
               STORE_NAME               0 (__doc__)

  67           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  69           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  70           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (importlib.util)
               STORE_NAME               5 (importlib)

  71           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (json)
               STORE_NAME               6 (json)

  72           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              7 (os)
               STORE_NAME               7 (os)

  73           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              8 (sys)
               STORE_NAME               8 (sys)

  74           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              9 (datetime)
               IMPORT_FROM              9 (datetime)
               STORE_NAME               9 (datetime)
               IMPORT_FROM             10 (timezone)
               STORE_NAME              10 (timezone)
               POP_TOP

  75           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Path',))
               IMPORT_NAME             11 (pathlib)
               IMPORT_FROM             12 (Path)
               STORE_NAME              12 (Path)
               POP_TOP

  76           LOAD_SMALL_INT           0
               LOAD_CONST               5 (('Iterable', 'List', 'Optional', 'Tuple'))
               IMPORT_NAME             13 (typing)
               IMPORT_FROM             14 (Iterable)
               STORE_NAME              14 (Iterable)
               IMPORT_FROM             15 (List)
               STORE_NAME              15 (List)
               IMPORT_FROM             16 (Optional)
               STORE_NAME              16 (Optional)
               IMPORT_FROM             17 (Tuple)
               STORE_NAME              17 (Tuple)
               POP_TOP

  79           LOAD_NAME                8 (sys)
               LOAD_ATTR               36 (stdout)
               LOAD_NAME                8 (sys)
               LOAD_ATTR               38 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              20 (_stream)

  80           NOP

  81   L2:     LOAD_NAME               20 (_stream)
               LOAD_ATTR               43 (reconfigure + NULL|self)
               LOAD_CONST               6 ('utf-8')
               LOAD_CONST               7 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  79   L4:     END_FOR
               POP_ITER

  86           LOAD_NAME                7 (os)
               LOAD_ATTR               46 (path)
               LOAD_ATTR               49 (abspath + NULL|self)

  87           LOAD_NAME                7 (os)
               LOAD_ATTR               46 (path)
               LOAD_ATTR               51 (join + NULL|self)
               LOAD_NAME                7 (os)
               LOAD_ATTR               46 (path)
               LOAD_ATTR               53 (dirname + NULL|self)
               LOAD_NAME               27 (__file__)
               CALL                     1
               LOAD_CONST               8 ('..')
               CALL                     2

  86           CALL                     1
               STORE_NAME              28 (_REPO_ROOT_DEFAULT)

  91           LOAD_CONST               9 ('READY')
               STORE_NAME              29 (VERDICT_READY)

  92           LOAD_CONST              10 ('NOT_READY')
               STORE_NAME              30 (VERDICT_NOT_READY)

  94           LOAD_CONST              11 ('BLOCK')
               STORE_NAME              31 (SEVERITY_BLOCK)

  95           LOAD_CONST              12 ('INFO')
               STORE_NAME              32 (SEVERITY_INFO)

 102           LOAD_CONST              74 (('scripts/pas160_mvp_sequence_check.py', 'scripts/pas161_lead_ingestion_readiness_check.py', 'scripts/pas162_pending_calls_readiness_check.py', 'scripts/pas163_candidate_pipeline_readiness_check.py', 'scripts/pas164_email_ingestion_readiness_check.py', 'scripts/pas165_email_auth_dedupe_readiness_check.py', 'scripts/pas166_email_dedupe_policy_readiness_check.py', 'scripts/pas167_email_secret_reaper_readiness_check.py', 'scripts/pas168_email_secret_rotation_readiness_check.py', 'scripts/pas169_crypto_roundtrip_check.py', 'scripts/pas169_launch_readiness_check.py'))
               STORE_NAME              33 (REQUIRED_PAS_SCRIPTS)

 116           LOAD_CONST              75 (('docs/pas169_crypto_roundtrip_launch_gate.md', 'docs/pas_launch_integrity_gate.md'))
               STORE_NAME              34 (REQUIRED_DOCS)

 121           LOAD_CONST              76 (('app/services/memory/review.py', 'app/services/memory/review_stats.py', 'app/services/memory/review_export.py', 'app/services/memory/review_actors.py', 'app/services/memory/review_alerts.py', 'app/services/memory/operator_console.py'))
               STORE_NAME              35 (MEMORY_REVIEW_FILES)

 133           LOAD_CONST              77 (('scripts/migrate_v17_drop_plaintext_email_forwarder_secret.sql', 'scripts/migrate_drop_plaintext_email_forwarder_secret.sql'))
               STORE_NAME              36 (FORBIDDEN_FUTURE_FILES)

 144           LOAD_CONST              78 (('import gmail', 'from gmail', 'import googleapiclient', 'from googleapiclient', 'import google.oauth2', 'from google.oauth2', 'from google.auth', 'import google.auth', 'from google_auth_oauthlib', 'import imaplib', 'from imaplib', 'import poplib', 'from poplib', 'import composio', 'from composio', 'import trustclaw', 'from trustclaw', 'import chromadb', 'from chromadb', 'import pinecone', 'from pinecone', 'import langchain', 'from langchain', 'import numpy', 'import faiss', 'import pgvector', 'from pgvector', 'from openai import embeddings', 'from openai.embeddings'))
               STORE_NAME              37 (FORBIDDEN_IMPORT_PREFIXES)

 167           LOAD_CONST              79 (('imaplib', 'poplib', 'fetch_inbox', 'gmail_oauth', 'gmail_token', 'users().messages'))
               STORE_NAME              38 (FORBIDDEN_INBOX_TOKENS)

 181           LOAD_CONST              80 (('alembic.command.upgrade', 'alembic.command.downgrade', 'subprocess.run(["alembic"', 'subprocess.Popen(["alembic"'))
               STORE_NAME              39 (MIGRATION_EXECUTE_TOKENS)

 192           LOAD_CONST              81 (('body.brokerage_id', 'body["brokerage_id"]', "body['brokerage_id']"))
               STORE_NAME              40 (FORBIDDEN_ROUTE_BODY_TRUST)

 206           LOAD_CONST              82 (('raw_email', 'raw_body', 'raw_transcript', 'full_transcript'))
               STORE_NAME              41 (EMAIL_INGESTION_FORBIDDEN_PAYLOAD_TOKENS)

 221           LOAD_CONST              83 (('http://localhost', 'http://127.0.0.1'))
               STORE_NAME              42 (LOCALHOST_SELF_CALL_TOKENS)

 232           LOAD_CONST              84 (('scripts/pas163_candidate_pipeline_readiness_check.py', 'scripts/pas_launch_integrity_check.py', 'scripts/testing/security_verify.py', 'app/config.py'))
               STORE_NAME              43 (LOCALHOST_SCAN_EXEMPT_FILES)

 242           LOAD_CONST              85 (('app/services/ingestion/email_parser.py', 'app/services/ingestion/email_ingestion.py', 'app/services/ingestion/email_auth.py', 'app/services/ingestion/email_dedupe.py', 'app/services/ingestion/email_dedupe_store.py', 'app/services/ingestion/email_forwarder_secret_store.py', 'app/routes/email_ingestion.py'))
               STORE_NAME              44 (EMAIL_INGESTION_SOURCE_FILES)

 254           LOAD_CONST              86 ((('/parse', 'require_admin'), ('/ingest', 'require_brokerage')))
               STORE_NAME              45 (ROUTE_AUTH_REQUIREMENTS)

 264           LOAD_CONST              13 ('severity')

 266           LOAD_NAME               31 (SEVERITY_BLOCK)

 264           LOAD_CONST              14 ('detail')

 266           LOAD_CONST              15 ('')

 264           BUILD_MAP                2
               LOAD_CONST              16 (<code object __annotate__ at 0x0000018C18025530, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 264>)
               MAKE_FUNCTION
               LOAD_CONST              17 (<code object _check at 0x0000018C17FA2970, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 264>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              46 (_check)

 277           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA23D0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 277>)
               MAKE_FUNCTION
               LOAD_CONST              19 (<code object _now_iso at 0x0000018C18038CB0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 277>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              47 (_now_iso)

 281           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA3B40, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 281>)
               MAKE_FUNCTION
               LOAD_CONST              21 (<code object _read_text at 0x0000018C18053AB0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 281>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              48 (_read_text)

 288           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA2F10, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 288>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object _strip_python_comments_and_strings at 0x0000018C17D81580, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 288>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              49 (_strip_python_comments_and_strings)

 323           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C18026430, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 323>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object _walk_python_files at 0x0000018C180483B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 323>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              50 (_walk_python_files)

 342           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA33C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 342>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object check_required_files at 0x0000018C1794ED80, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 342>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              51 (check_required_files)

 356           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA35A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 356>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object check_memory_review_intact at 0x0000018C180612C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 356>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              52 (check_memory_review_intact)

 370           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA3D20, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 370>)
               MAKE_FUNCTION
               LOAD_CONST              31 (<code object check_no_forbidden_future_files at 0x0000018C180488F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 370>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              53 (check_no_forbidden_future_files)

 385           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA1D40, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 385>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object check_requirements_cryptography at 0x0000018C182DA5E0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 385>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              54 (check_requirements_cryptography)

 419           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA2880, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 419>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object check_crypto_importable at 0x0000018C17F62AC0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 419>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              55 (check_crypto_importable)

 461           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C17FA2100, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 461>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object check_worker_off_by_default at 0x0000018C1801D1A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 461>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              56 (check_worker_off_by_default)

 482           LOAD_CONST              38 (<code object __annotate__ at 0x0000018C17FA2B50, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 482>)
               MAKE_FUNCTION
               LOAD_CONST              39 (<code object check_no_startup_worker at 0x0000018C17F79A70, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 482>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              57 (check_no_startup_worker)

 509           LOAD_CONST              40 (<code object __annotate__ at 0x0000018C17FA3780, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 509>)
               MAKE_FUNCTION
               LOAD_CONST              41 (<code object check_email_routes_auth_scoped at 0x0000018C17F61C80, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 509>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              58 (check_email_routes_auth_scoped)

 540           LOAD_CONST              42 (<code object __annotate__ at 0x0000018C17FA1E30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 540>)
               MAKE_FUNCTION
               LOAD_CONST              43 (<code object check_no_body_trust at 0x0000018C17D85D70, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 540>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              59 (check_no_body_trust)

 567           LOAD_CONST              44 (<code object __annotate__ at 0x0000018C17FA21F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 567>)
               MAKE_FUNCTION
               LOAD_CONST              45 (<code object check_no_forbidden_imports at 0x0000018C182DA010, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 567>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              60 (check_no_forbidden_imports)

 630           LOAD_CONST              46 (<code object __annotate__ at 0x0000018C17FA26A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 630>)
               MAKE_FUNCTION
               LOAD_CONST              47 (<code object check_no_inbox_scan_tokens at 0x0000018C17D875A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 630>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              61 (check_no_inbox_scan_tokens)

 665           LOAD_CONST              48 (<code object __annotate__ at 0x0000018C17FA22E0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 665>)
               MAKE_FUNCTION
               LOAD_CONST              49 (<code object check_no_migration_execution at 0x0000018C17D86830, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 665>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              62 (check_no_migration_execution)

 696           LOAD_CONST              50 (<code object __annotate__ at 0x0000018C17FA25B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 696>)
               MAKE_FUNCTION
               LOAD_CONST              51 (<code object check_no_raw_payload_persistence at 0x0000018C17F781B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 696>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              63 (check_no_raw_payload_persistence)

 741           LOAD_CONST              52 (<code object __annotate__ at 0x0000018C17FA2D30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 741>)
               MAKE_FUNCTION
               LOAD_CONST              53 (<code object check_no_localhost_self_call at 0x0000018C17F7FF70, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 741>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              64 (check_no_localhost_self_call)

 781           LOAD_CONST              54 (<code object __annotate__ at 0x0000018C17FA2C40, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 781>)
               MAKE_FUNCTION
               LOAD_CONST              55 (<code object check_pas169_doc_present at 0x0000018C1804D550, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 781>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              65 (check_pas169_doc_present)

 798           LOAD_CONST              56 (<code object __annotate__ at 0x0000018C181153E0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 798>)
               MAKE_FUNCTION
               LOAD_CONST              57 (<code object check_self_no_env_or_db at 0x0000018C17D88130, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 798>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              66 (check_self_no_env_or_db)

 835           LOAD_CONST              58 (<code object __annotate__ at 0x0000018C181154D0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 835>)
               MAKE_FUNCTION
               LOAD_CONST              59 (<code object _aggregate at 0x0000018C17EC44A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 835>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              67 (_aggregate)

 851           LOAD_CONST              60 (<code object __annotate__ at 0x0000018C181155C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 851>)
               MAKE_FUNCTION
               LOAD_CONST              61 (<code object _operator_actions at 0x0000018C18048AB0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 851>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              68 (_operator_actions)

 861           LOAD_CONST              62 (<code object __annotate__ at 0x0000018C18115980, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 861>)
               MAKE_FUNCTION
               LOAD_CONST              63 (<code object evaluate at 0x0000018C182E58B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 861>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              69 (evaluate)

 896           LOAD_CONST              64 ('pas_launch_integrity_report.json')
               STORE_NAME              70 (REPORT_FILENAME)

 899           LOAD_CONST              65 (<code object __annotate__ at 0x0000018C18115110, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 899>)
               MAKE_FUNCTION
               LOAD_CONST              66 (<code object _build_parser at 0x0000018C1801C410, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 899>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              71 (_build_parser)

 935           LOAD_CONST              67 (<code object __annotate__ at 0x0000018C18115200, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 935>)
               MAKE_FUNCTION
               LOAD_CONST              68 (<code object _print_summary at 0x0000018C17D8CD10, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 935>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              72 (_print_summary)

 953           LOAD_CONST              69 (<code object __annotate__ at 0x0000018C18025030, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 953>)
               MAKE_FUNCTION
               LOAD_CONST              70 (<code object _write_report at 0x0000018C179C3E10, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 953>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              73 (_write_report)

 967           LOAD_CONST              87 ((None,))
               LOAD_CONST              71 (<code object __annotate__ at 0x0000018C18115B60, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 967>)
               MAKE_FUNCTION
               LOAD_CONST              72 (<code object main at 0x0000018C17D88FF0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 967>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              74 (main)

 995           LOAD_NAME               75 (__name__)
               LOAD_CONST              73 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 996           LOAD_NAME                8 (sys)
               LOAD_ATTR              152 (exit)
               PUSH_NULL
               LOAD_NAME               74 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 995   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  82           LOAD_NAME               22 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  83   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          361 (to L1)

  82   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025530, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 264>:
264           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('check_id')

265           LOAD_CONST               2 ('str')

264           LOAD_CONST               3 ('status')

265           LOAD_CONST               2 ('str')

264           LOAD_CONST               4 ('label')

265           LOAD_CONST               2 ('str')

264           LOAD_CONST               5 ('severity')

266           LOAD_CONST               2 ('str')

264           LOAD_CONST               6 ('detail')

266           LOAD_CONST               2 ('str')

264           LOAD_CONST               7 ('return')

267           LOAD_CONST               8 ('dict')

264           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _check at 0x0000018C17FA2970, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 264>:
264           RESUME                   0

269           LOAD_CONST               0 ('id')
              LOAD_FAST_BORROW         0 (check_id)

270           LOAD_CONST               1 ('status')
              LOAD_FAST_BORROW         1 (status)

271           LOAD_CONST               2 ('label')
              LOAD_FAST_BORROW         2 (label)

272           LOAD_CONST               3 ('severity')
              LOAD_FAST_BORROW         3 (severity)

273           LOAD_CONST               4 ('detail')
              LOAD_FAST_BORROW         4 (detail)

268           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 277>:
277           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038CB0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 277>:
277           RESUME                   0

278           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 281>:
281           RESUME                   0
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

Disassembly of <code object _read_text at 0x0000018C18053AB0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 281>:
 281           RESUME                   0

 282           NOP

 283   L1:     LOAD_FAST_BORROW         0 (path)
               LOAD_ATTR                1 (read_text + NULL|self)
               LOAD_CONST               0 ('utf-8')
               LOAD_CONST               1 ('replace')
               LOAD_CONST               2 (('encoding', 'errors'))
               CALL_KW                  2
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 284           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 285   L4:     POP_EXCEPT
               LOAD_CONST               3 (None)
               RETURN_VALUE

 284   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 288>:
288           RESUME                   0
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

Disassembly of <code object _strip_python_comments_and_strings at 0x0000018C17D81580, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 288>:
288            RESUME                   0

289            BUILD_LIST               0
               STORE_FAST               1 (out)

290            LOAD_SMALL_INT           0
               LOAD_GLOBAL              1 (len + NULL)
               LOAD_FAST_BORROW         0 (src)
               CALL                     1
               STORE_FAST_STORE_FAST   50 (n, i)

291    L1:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (i, n)
               COMPARE_OP              18 (bool(<))
               EXTENDED_ARG             1
               POP_JUMP_IF_FALSE      282 (to L13)
               NOT_TAKEN

292            LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               BINARY_OP               26 ([])
               STORE_FAST               4 (ch)

293            LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               1 ('#')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       38 (to L3)
               NOT_TAKEN

294            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_CONST               2 ('\n')
               LOAD_FAST_BORROW         2 (i)
               CALL                     2
               STORE_FAST               5 (j)

295            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L2)
               NOT_TAKEN

296            JUMP_FORWARD           240 (to L13)

297    L2:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

298            JUMP_BACKWARD           59 (to L1)

299    L3:     LOAD_FAST_BORROW         0 (src)
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

300    L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               BINARY_SLICE
               STORE_FAST               6 (quote)

301            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 98 (quote, i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               CALL                     2
               STORE_FAST               7 (end)

302            LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L5)
               NOT_TAKEN

303            JUMP_FORWARD           138 (to L13)

304    L5:     LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

305            JUMP_BACKWARD          161 (to L1)

306    L6:     LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               7 (('"', "'"))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       92 (to L12)
               NOT_TAKEN

307            LOAD_FAST                4 (ch)
               STORE_FAST               6 (quote)

308            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               5 (j)

309    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (j, n)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       63 (to L11)
               NOT_TAKEN

310            LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
               BINARY_OP               26 ([])
               LOAD_CONST               5 ('\\')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       12 (to L8)
               NOT_TAKEN

311            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           2
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)

312            JUMP_BACKWARD           30 (to L7)

313    L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
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

314    L9:     JUMP_FORWARD            11 (to L11)

315   L10:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)
               JUMP_BACKWARD           68 (to L7)

316   L11:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

317            EXTENDED_ARG             1
               JUMP_BACKWARD          259 (to L1)

318   L12:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (ch)
               CALL                     1
               POP_TOP

319            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               2 (i)
               EXTENDED_ARG             1
               JUMP_BACKWARD          288 (to L1)

320   L13:     LOAD_CONST               6 ('')
               LOAD_ATTR                9 (join + NULL|self)
               LOAD_FAST_BORROW         1 (out)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026430, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 323>:
323           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('root')
              LOAD_CONST               2 ('Path')
              LOAD_CONST               3 ('subdirs')
              LOAD_CONST               4 ('Iterable[str]')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('List[Path]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _walk_python_files at 0x0000018C180483B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 323>:
323           RESUME                   0

326           BUILD_LIST               0
              STORE_FAST               2 (out)

327           LOAD_FAST_BORROW         1 (subdirs)
              GET_ITER
      L1:     FOR_ITER               104 (to L6)
              STORE_FAST               3 (sd)

328           LOAD_FAST_BORROW_LOAD_FAST_BORROW 3 (root, sd)
              BINARY_OP               11 (/)
              STORE_FAST               4 (base)

329           LOAD_FAST_BORROW         4 (base)
              LOAD_ATTR                1 (is_dir + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

330           JUMP_BACKWARD           35 (to L1)

331   L2:     LOAD_GLOBAL              3 (sorted + NULL)
              LOAD_FAST_BORROW         4 (base)
              LOAD_ATTR                5 (rglob + NULL|self)
              LOAD_CONST               1 ('*.py')
              CALL                     1
              CALL                     1
              GET_ITER
      L3:     FOR_ITER                39 (to L5)
              STORE_FAST               5 (p)

332           LOAD_CONST               2 ('__pycache__')
              LOAD_FAST_BORROW         5 (p)
              LOAD_ATTR                6 (parts)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN

333           JUMP_BACKWARD           22 (to L3)

334   L4:     LOAD_FAST_BORROW         2 (out)
              LOAD_ATTR                9 (append + NULL|self)
              LOAD_FAST_BORROW         5 (p)
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           41 (to L3)

331   L5:     END_FOR
              POP_ITER
              JUMP_BACKWARD          106 (to L1)

327   L6:     END_FOR
              POP_ITER

335           LOAD_FAST_BORROW         2 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 342>:
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

Disassembly of <code object check_required_files at 0x0000018C1794ED80, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 342>:
342           RESUME                   0

343           BUILD_LIST               0
              STORE_FAST               1 (out)

344           LOAD_GLOBAL              0 (REQUIRED_PAS_SCRIPTS)
              LOAD_GLOBAL              2 (REQUIRED_DOCS)
              BINARY_OP                0 (+)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

345           LOAD_GLOBAL              5 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                7 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

346           LOAD_FAST                1 (out)
              LOAD_ATTR                9 (append + NULL|self)
              LOAD_GLOBAL             11 (_check + NULL)

347           LOAD_CONST               0 ('required_file:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

348           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

349   L3:     LOAD_CONST               3 ('Required PAS-LAUNCH-01 artefact present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

350           LOAD_GLOBAL             12 (SEVERITY_BLOCK)

351           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing')

346   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

344   L6:     END_FOR
              POP_ITER

353           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 356>:
356           RESUME                   0
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

Disassembly of <code object check_memory_review_intact at 0x0000018C180612C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 356>:
356           RESUME                   0

357           BUILD_LIST               0
              STORE_FAST               1 (out)

358           LOAD_GLOBAL              0 (MEMORY_REVIEW_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

359           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

360           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

361           LOAD_CONST               0 ('memory_review_file:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

362           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

363   L3:     LOAD_CONST               3 ('Memory Review file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

364           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

365           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('Memory Review file deleted')

360   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

358   L6:     END_FOR
              POP_ITER

367           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3D20, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 370>:
370           RESUME                   0
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

Disassembly of <code object check_no_forbidden_future_files at 0x0000018C180488F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 370>:
370           RESUME                   0

371           BUILD_LIST               0
              STORE_FAST               1 (out)

372           LOAD_GLOBAL              0 (FORBIDDEN_FUTURE_FILES)
              GET_ITER
      L1:     FOR_ITER               100 (to L6)
              STORE_FAST               2 (p)

373           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (exists + NULL|self)
              CALL                     0
              STORE_FAST               3 (present)

374           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

375           LOAD_CONST               0 ('forbidden_future_file:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

376           LOAD_FAST_BORROW         3 (present)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('FAIL')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('PASS')

377   L3:     LOAD_CONST               3 ('Plaintext-drop migration absent: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

378           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

380           LOAD_FAST_BORROW         3 (present)
              TO_BOOL
              POP_JUMP_IF_FALSE        7 (to L4)
              NOT_TAKEN

379           LOAD_CONST               4 ('file ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              LOAD_CONST               5 (' present — destructive cutover NOT in scope')
              BUILD_STRING             3
              JUMP_FORWARD             1 (to L5)

380   L4:     LOAD_CONST               6 ('')

374   L5:     LOAD_CONST               7 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD          102 (to L1)

372   L6:     END_FOR
              POP_ITER

382           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1D40, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 385>:
385           RESUME                   0
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

Disassembly of <code object check_requirements_cryptography at 0x0000018C182DA5E0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 385>:
385            RESUME                   0

386            BUILD_LIST               0
               STORE_FAST               1 (out)

387            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('requirements.txt')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

388            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L1:     STORE_FAST               3 (src)

389            LOAD_CONST               2 (False)
               STORE_FAST               4 (has_crypto_42)

390            LOAD_FAST_BORROW         3 (src)
               LOAD_ATTR                5 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L2:     FOR_ITER               141 (to L11)
               STORE_FAST               5 (line)

391            LOAD_FAST_BORROW         5 (line)
               LOAD_ATTR                7 (strip + NULL|self)
               CALL                     0
               LOAD_ATTR                9 (lower + NULL|self)
               CALL                     0
               STORE_FAST               6 (stripped)

392            LOAD_FAST_BORROW         6 (stripped)
               TO_BOOL
               POP_JUMP_IF_FALSE       24 (to L3)
               NOT_TAKEN
               LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               11 (startswith + NULL|self)
               LOAD_CONST               3 ('#')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN

393    L3:     JUMP_BACKWARD           66 (to L2)

394    L4:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               11 (startswith + NULL|self)
               LOAD_CONST               4 ('cryptography')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           91 (to L2)

399    L5:     LOAD_CONST               5 ('>=42')
               LOAD_FAST_BORROW         6 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE        15 (to L6)
               NOT_TAKEN
               LOAD_CONST               6 ('==42')
               LOAD_FAST_BORROW         6 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         8 (to L6)
               NOT_TAKEN
               LOAD_CONST               7 ('~=42')
               LOAD_FAST_BORROW         6 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        4 (to L7)
               NOT_TAKEN

400    L6:     LOAD_CONST               8 (True)
               STORE_FAST               4 (has_crypto_42)
               JUMP_FORWARD            26 (to L10)

401    L7:     LOAD_CONST               9 ('>=43')
               LOAD_FAST_BORROW         6 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         8 (to L8)
               NOT_TAKEN
               LOAD_CONST              10 ('>=44')
               LOAD_FAST_BORROW         6 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        4 (to L9)
               NOT_TAKEN

402    L8:     LOAD_CONST               8 (True)
               STORE_FAST               4 (has_crypto_42)
               JUMP_FORWARD             9 (to L10)

403    L9:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_CONST               4 ('cryptography')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN

405            LOAD_CONST               8 (True)
               STORE_FAST               4 (has_crypto_42)

406   L10:     POP_TOP
               JUMP_FORWARD             2 (to L12)

390   L11:     END_FOR
               POP_ITER

407   L12:     LOAD_FAST                1 (out)
               LOAD_ATTR               13 (append + NULL|self)
               LOAD_GLOBAL             15 (_check + NULL)

408            LOAD_CONST              11 ('requirements:cryptography_ge_42')

409            LOAD_FAST_BORROW         4 (has_crypto_42)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L13)
               NOT_TAKEN
               LOAD_CONST              12 ('PASS')
               JUMP_FORWARD             1 (to L14)
      L13:     LOAD_CONST              13 ('FAIL')

410   L14:     LOAD_CONST              14 ('requirements.txt declares cryptography>=42')

411            LOAD_GLOBAL             16 (SEVERITY_BLOCK)

412            LOAD_FAST_BORROW         4 (has_crypto_42)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L15)
               NOT_TAKEN
               LOAD_CONST               1 ('')
               JUMP_FORWARD             1 (to L16)

413   L15:     LOAD_CONST              15 ('cryptography>=42 not found in requirements.txt')

407   L16:     LOAD_CONST              16 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

416            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 419>:
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

Disassembly of <code object check_crypto_importable at 0x0000018C17F62AC0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 419>:
 419            RESUME                   0

 420            BUILD_LIST               0
                STORE_FAST               1 (out)

 422            LOAD_CONST               0 (' Run `pip install -r requirements.txt` in this Python environment before launch.')

 421            STORE_FAST               2 (install_hint)

 425            NOP

 426    L1:     LOAD_GLOBAL              0 (importlib)
                LOAD_ATTR                2 (util)
                LOAD_ATTR                5 (find_spec + NULL|self)
                LOAD_CONST               1 ('cryptography.fernet')
                CALL                     1
                STORE_FAST               3 (spec)

 440    L2:     LOAD_FAST                3 (spec)
                POP_JUMP_IF_NOT_NONE    38 (to L3)
                NOT_TAKEN

 441            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 442            LOAD_CONST               2 ('crypto:importable')

 443            LOAD_CONST               3 ('FAIL')

 444            LOAD_CONST               4 ('cryptography.fernet is importable')

 445            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 447            LOAD_CONST               9 ('cryptography is declared in requirements.txt but is NOT installed in this Python environment. Run `pip install -r requirements.txt` before launch.')

 441            LOAD_CONST               7 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 452            LOAD_FAST                1 (out)
                RETURN_VALUE

 453    L3:     LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 454            LOAD_CONST               2 ('crypto:importable')

 455            LOAD_CONST              10 ('PASS')

 456            LOAD_CONST               4 ('cryptography.fernet is importable')

 453            CALL                     3
                CALL                     1
                POP_TOP

 458            LOAD_FAST                1 (out)
                RETURN_VALUE

  --    L4:     PUSH_EXC_INFO

 427            LOAD_GLOBAL              6 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       73 (to L9)
                NOT_TAKEN
                STORE_FAST               4 (e)

 428    L5:     LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 429            LOAD_CONST               2 ('crypto:importable')

 430            LOAD_CONST               3 ('FAIL')

 431            LOAD_CONST               4 ('cryptography.fernet is importable')

 432            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 434            LOAD_CONST               5 ('find_spec raised ')
                LOAD_GLOBAL             15 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               16 (__name__)
                FORMAT_SIMPLE
                LOAD_CONST               6 (' — cryptography is not importable in this Python environment.')

 436            LOAD_FAST                2 (install_hint)
                FORMAT_SIMPLE

 434            BUILD_STRING             4

 428            LOAD_CONST               7 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 439            LOAD_FAST                1 (out)
        L6:     SWAP                     2
        L7:     POP_EXCEPT
                LOAD_CONST               8 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RETURN_VALUE

  --    L8:     LOAD_CONST               8 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RERAISE                  1

 427    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L4 [0]
  L4 to L5 -> L10 [1] lasti
  L5 to L6 -> L8 [1] lasti
  L6 to L7 -> L10 [1] lasti
  L8 to L10 -> L10 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 461>:
461           RESUME                   0
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

Disassembly of <code object check_worker_off_by_default at 0x0000018C1801D1A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 461>:
461           RESUME                   0

462           BUILD_LIST               0
              STORE_FAST               1 (out)

463           LOAD_GLOBAL              1 (Path + NULL)
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

464           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

469           LOAD_CONST               5 ('_ENV_FLAG_ENABLED_LITERAL = "true"')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         6 (to L2)
              NOT_TAKEN
              POP_TOP

470           LOAD_CONST               6 ("_ENV_FLAG_ENABLED_LITERAL = 'true'")
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)

468   L2:     STORE_FAST               4 (literal_ok)

472           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

473           LOAD_CONST               7 ('worker:off_by_default')

474           LOAD_FAST_BORROW         4 (literal_ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               8 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               9 ('FAIL')

475   L4:     LOAD_CONST              10 ('Pending-call worker is OFF by default (strict env literal)')

476           LOAD_GLOBAL              8 (SEVERITY_BLOCK)

477           LOAD_FAST_BORROW         4 (literal_ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST              11 ('missing strict enable-literal constant')

472   L6:     LOAD_CONST              12 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP

479           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 482>:
482           RESUME                   0
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

Disassembly of <code object check_no_startup_worker at 0x0000018C17F79A70, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 482>:
482           RESUME                   0

483           BUILD_LIST               0
              STORE_FAST               1 (out)

484           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('main.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

485           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               2 ('')
      L1:     STORE_FAST               3 (src)

486           LOAD_GLOBAL              5 (_strip_python_comments_and_strings + NULL)
              LOAD_FAST_BORROW         3 (src)
              CALL                     1
              STORE_FAST               4 (executable)

490           BUILD_LIST               0
              STORE_FAST               5 (bad)

491           LOAD_CONST               3 ('from app.services.ingestion.worker')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L2)
              NOT_TAKEN

492           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               4 ('from app.services.ingestion.worker import …')
              CALL                     1
              POP_TOP

493   L2:     LOAD_CONST               5 ('import app.services.ingestion.worker')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L3)
              NOT_TAKEN

494           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               5 ('import app.services.ingestion.worker')
              CALL                     1
              POP_TOP

495   L3:     LOAD_CONST               6 ('run_worker_loop')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L4)
              NOT_TAKEN

496           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               7 ('run_worker_loop reference')
              CALL                     1
              POP_TOP

497   L4:     LOAD_CONST               8 ('process_pending_call(')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L5)
              NOT_TAKEN

498           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               9 ('process_pending_call call')
              CALL                     1
              POP_TOP

499   L5:     LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

500           LOAD_CONST              10 ('main:no_startup_worker')

501           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L6)
              NOT_TAKEN
              LOAD_CONST              11 ('FAIL')
              JUMP_FORWARD             1 (to L7)
      L6:     LOAD_CONST              12 ('PASS')

502   L7:     LOAD_CONST              13 ('FastAPI lifespan does not auto-start the pending-call worker')

503           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

504           LOAD_FAST_BORROW         5 (bad)
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

499   L9:     LOAD_CONST              16 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP

506           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 509>:
509           RESUME                   0
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

Disassembly of <code object check_email_routes_auth_scoped at 0x0000018C17F61C80, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 509>:
509            RESUME                   0

510            BUILD_LIST               0
               STORE_FAST               1 (out)

511            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('routes')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('email_ingestion.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

512            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               3 ('')
       L1:     STORE_FAST               3 (src)

513            LOAD_GLOBAL              4 (ROUTE_AUTH_REQUIREMENTS)
               GET_ITER
       L2:     FOR_ITER               128 (to L10)
               UNPACK_SEQUENCE          2
               STORE_FAST_STORE_FAST   69 (path_str, dep)

519            LOAD_CONST               4 ('@router.post("')
               LOAD_FAST_BORROW         4 (path_str)
               FORMAT_SIMPLE
               LOAD_CONST               5 ('")')
               BUILD_STRING             3
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        10 (to L3)
               NOT_TAKEN
               POP_TOP

520            LOAD_CONST               6 ("@router.post('")
               LOAD_FAST_BORROW         4 (path_str)
               FORMAT_SIMPLE
               LOAD_CONST               7 ("')")
               BUILD_STRING             3
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

518    L3:     STORE_FAST               6 (decl_present)

522            LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (dep, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               7 (dep_present)

523            LOAD_FAST                6 (decl_present)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN
               POP_TOP
               LOAD_FAST                7 (dep_present)
       L4:     STORE_FAST               8 (ok)

524            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

525            LOAD_CONST               8 ('route_auth:')
               LOAD_FAST_BORROW         4 (path_str)
               FORMAT_SIMPLE
               LOAD_CONST               9 (':')
               LOAD_FAST_BORROW         5 (dep)
               FORMAT_SIMPLE
               BUILD_STRING             4

526            LOAD_FAST_BORROW         8 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST              10 ('PASS')
               JUMP_FORWARD             1 (to L6)
       L5:     LOAD_CONST              11 ('FAIL')

527    L6:     LOAD_CONST              12 ('Route ')
               LOAD_FAST_BORROW         4 (path_str)
               FORMAT_SIMPLE
               LOAD_CONST              13 (' is auth-scoped via ')
               LOAD_FAST_BORROW         5 (dep)
               FORMAT_SIMPLE
               BUILD_STRING             4

528            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

530            LOAD_FAST_BORROW         8 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L7)
               NOT_TAKEN
               LOAD_CONST               3 ('')
               JUMP_FORWARD            15 (to L9)

532    L7:     LOAD_FAST_BORROW         6 (decl_present)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               LOAD_CONST              14 ('missing route decl')
               JUMP_FORWARD             5 (to L9)

533    L8:     LOAD_CONST              15 ('missing ')
               LOAD_FAST_BORROW         5 (dep)
               FORMAT_SIMPLE
               LOAD_CONST              16 (' reference')
               BUILD_STRING             3

524    L9:     LOAD_CONST              17 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          130 (to L2)

513   L10:     END_FOR
               POP_ITER

537            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 540>:
540           RESUME                   0
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

Disassembly of <code object check_no_body_trust at 0x0000018C17D85D70, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 540>:
540            RESUME                   0

541            BUILD_LIST               0
               STORE_FAST               1 (out)

542            LOAD_CONST               9 (('app/routes/email_ingestion.py', 'app/routes/lead_ingestion.py', 'app/services/ingestion/email_ingestion.py'))
               GET_ITER
       L1:     FOR_ITER               220 (to L11)
               STORE_FAST               2 (relpath)

547            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         2 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               3 (p)

548            LOAD_FAST_BORROW         3 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

549            JUMP_BACKWARD           45 (to L1)

550    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         3 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               4 (src)

551            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         4 (src)
               CALL                     1
               STORE_FAST               5 (executable)

552            BUILD_LIST               0
               STORE_FAST               6 (bad)

553            LOAD_GLOBAL              8 (FORBIDDEN_ROUTE_BODY_TRUST)
               GET_ITER
       L4:     FOR_ITER                28 (to L6)
               STORE_FAST               7 (pattern)

554            LOAD_FAST_BORROW_LOAD_FAST_BORROW 117 (pattern, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L4)

555    L5:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_FAST_BORROW         7 (pattern)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L4)

553    L6:     END_FOR
               POP_ITER

556            LOAD_FAST                1 (out)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_GLOBAL             13 (_check + NULL)

557            LOAD_CONST               2 ('body_trust:')
               LOAD_FAST_BORROW         3 (p)
               LOAD_ATTR               14 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

558            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L7)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L8)
       L7:     LOAD_CONST               4 ('PASS')

559    L8:     LOAD_CONST               5 ('No body-trust brokerage_id paths: ')
               LOAD_FAST_BORROW         3 (p)
               LOAD_ATTR               14 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

560            LOAD_GLOBAL             16 (SEVERITY_BLOCK)

562            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L9)
               NOT_TAKEN

561            LOAD_CONST               6 ('body-trust patterns present: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               19 (join + NULL|self)
               LOAD_FAST_BORROW         6 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L10)

562    L9:     LOAD_CONST               1 ('')

556   L10:     LOAD_CONST               8 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          222 (to L1)

542   L11:     END_FOR
               POP_ITER

564            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 567>:
567           RESUME                   0
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

Disassembly of <code object check_no_forbidden_imports at 0x0000018C182DA010, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 567>:
 567            RESUME                   0

 581            BUILD_LIST               0
                STORE_FAST               1 (out)

 582            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                STORE_FAST               2 (repo)

 584            LOAD_GLOBAL              3 (_walk_python_files + NULL)
                LOAD_FAST_BORROW         2 (repo)
                LOAD_CONST               1 ('app')
                BUILD_LIST               1
                LOAD_CONST               2 (('subdirs',))
                CALL_KW                  2
                STORE_FAST               3 (app_files)

 586            LOAD_FAST_BORROW         2 (repo)
                LOAD_CONST               3 ('scripts')
                BINARY_OP               11 (/)
                LOAD_CONST               4 ('pas_launch_integrity_check.py')
                BINARY_OP               11 (/)

 587            LOAD_FAST_BORROW         2 (repo)
                LOAD_CONST               3 ('scripts')
                BINARY_OP               11 (/)
                LOAD_CONST               5 ('pas169_crypto_roundtrip_check.py')
                BINARY_OP               11 (/)

 588            LOAD_FAST_BORROW         2 (repo)
                LOAD_CONST               3 ('scripts')
                BINARY_OP               11 (/)
                LOAD_CONST               6 ('pas169_launch_readiness_check.py')
                BINARY_OP               11 (/)

 585            BUILD_LIST               3
                STORE_FAST               4 (pas_launch_scripts)

 591            LOAD_FAST_LOAD_FAST     52 (app_files, pas_launch_scripts)
                GET_ITER
                LOAD_FAST_AND_CLEAR      5 (p)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2
        L2:     FOR_ITER                28 (to L5)
                STORE_FAST_LOAD_FAST    85 (p, p)
                LOAD_ATTR                5 (is_file + NULL|self)
                CALL                     0
                TO_BOOL
        L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           26 (to L2)
        L4:     LOAD_FAST_BORROW         5 (p)
                LIST_APPEND              2
                JUMP_BACKWARD           30 (to L2)
        L5:     END_FOR
                POP_ITER
        L6:     SWAP                     2
                STORE_FAST               5 (p)
                BINARY_OP                0 (+)
                STORE_FAST               6 (files_to_scan)

 592            BUILD_LIST               0
                STORE_FAST               7 (bad_by_file)

 593            LOAD_FAST_BORROW         6 (files_to_scan)
                GET_ITER
        L7:     FOR_ITER               181 (to L17)
                STORE_FAST               5 (p)

 594            LOAD_GLOBAL              7 (_read_text + NULL)
                LOAD_FAST_BORROW         5 (p)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               7 ('')
        L8:     STORE_FAST               8 (src)

 595            BUILD_LIST               0
                STORE_FAST               9 (offenders)

 596            LOAD_FAST_BORROW         8 (src)
                LOAD_ATTR                9 (splitlines + NULL|self)
                CALL                     0
                GET_ITER
        L9:     FOR_ITER               107 (to L15)
                STORE_FAST              10 (line)

 597            LOAD_FAST_BORROW        10 (line)
                LOAD_ATTR               11 (strip + NULL|self)
                CALL                     0
                STORE_FAST              11 (stripped)

 598            LOAD_FAST_BORROW        11 (stripped)
                TO_BOOL
                POP_JUMP_IF_FALSE       24 (to L10)
                NOT_TAKEN
                LOAD_FAST_BORROW        11 (stripped)
                LOAD_ATTR               13 (startswith + NULL|self)
                LOAD_CONST               8 ('#')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L11)
                NOT_TAKEN

 599   L10:     JUMP_BACKWARD           52 (to L9)

 600   L11:     LOAD_GLOBAL             14 (FORBIDDEN_IMPORT_PREFIXES)
                GET_ITER
       L12:     FOR_ITER                45 (to L14)
                STORE_FAST              12 (prefix)

 601            LOAD_FAST_BORROW        11 (stripped)
                LOAD_ATTR               13 (startswith + NULL|self)
                LOAD_FAST_BORROW        12 (prefix)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
                NOT_TAKEN
                JUMP_BACKWARD           28 (to L12)

 602   L13:     LOAD_FAST_BORROW         9 (offenders)
                LOAD_ATTR               17 (append + NULL|self)
                LOAD_FAST_BORROW        12 (prefix)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           47 (to L12)

 600   L14:     END_FOR
                POP_ITER
                JUMP_BACKWARD          109 (to L9)

 596   L15:     END_FOR
                POP_ITER

 603            LOAD_FAST_BORROW         9 (offenders)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L16)
                NOT_TAKEN
                JUMP_BACKWARD          163 (to L7)

 604   L16:     LOAD_FAST_BORROW         7 (bad_by_file)
                LOAD_ATTR               17 (append + NULL|self)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 89 (p, offenders)
                BUILD_TUPLE              2
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          183 (to L7)

 593   L17:     END_FOR
                POP_ITER

 606            LOAD_FAST_BORROW         7 (bad_by_file)
                TO_BOOL
                POP_JUMP_IF_FALSE      137 (to L20)
                NOT_TAKEN

 607            LOAD_FAST_BORROW         7 (bad_by_file)
                GET_ITER
       L18:     FOR_ITER               128 (to L19)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   89 (p, offenders)

 608            LOAD_GLOBAL             19 (str + NULL)
                LOAD_FAST_BORROW         5 (p)
                LOAD_ATTR               21 (relative_to + NULL|self)
                LOAD_FAST_BORROW         2 (repo)
                CALL                     1
                CALL                     1
                LOAD_ATTR               23 (replace + NULL|self)
                LOAD_CONST               9 ('\\')
                LOAD_CONST              10 ('/')
                CALL                     2
                STORE_FAST              13 (rel)

 609            LOAD_FAST_BORROW         1 (out)
                LOAD_ATTR               17 (append + NULL|self)
                LOAD_GLOBAL             25 (_check + NULL)

 610            LOAD_CONST              11 ('forbidden_import:')
                LOAD_FAST_BORROW        13 (rel)
                FORMAT_SIMPLE
                BUILD_STRING             2

 611            LOAD_CONST              12 ('FAIL')

 612            LOAD_CONST              13 ('No forbidden imports in ')
                LOAD_FAST_BORROW        13 (rel)
                FORMAT_SIMPLE
                BUILD_STRING             2

 613            LOAD_GLOBAL             26 (SEVERITY_BLOCK)

 614            LOAD_CONST              14 ('forbidden import prefixes: ')
                LOAD_CONST              15 (', ')
                LOAD_ATTR               29 (join + NULL|self)

 615            LOAD_GLOBAL             31 (sorted + NULL)
                LOAD_GLOBAL             33 (set + NULL)
                LOAD_FAST_BORROW         9 (offenders)
                CALL                     1
                CALL                     1

 614            CALL                     1
                BINARY_OP                0 (+)

 609            LOAD_CONST              16 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          130 (to L18)

 607   L19:     END_FOR
                POP_ITER

 627            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

 619   L20:     LOAD_FAST_BORROW         1 (out)
                LOAD_ATTR               17 (append + NULL|self)
                LOAD_GLOBAL             25 (_check + NULL)

 620            LOAD_CONST              17 ('forbidden_import:scan')

 621            LOAD_CONST              18 ('PASS')

 623            LOAD_CONST              13 ('No forbidden imports in ')
                LOAD_GLOBAL             35 (len + NULL)
                LOAD_FAST_BORROW         6 (files_to_scan)
                CALL                     1
                FORMAT_SIMPLE
                LOAD_CONST              19 (' scanned app/+launch-script files')
                BUILD_STRING             3

 619            CALL                     3
                CALL                     1
                POP_TOP

 627            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L21:     SWAP                     2
                POP_TOP

 591            SWAP                     2
                STORE_FAST               5 (p)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L21 [3]
  L4 to L6 -> L21 [3]

Disassembly of <code object __annotate__ at 0x0000018C17FA26A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 630>:
630           RESUME                   0
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

Disassembly of <code object check_no_inbox_scan_tokens at 0x0000018C17D875A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 630>:
630            RESUME                   0

631            BUILD_LIST               0
               STORE_FAST               1 (out)

632            LOAD_CONST               9 (('app/services/ingestion/email_parser.py', 'app/services/ingestion/email_ingestion.py', 'app/services/ingestion/email_auth.py', 'app/services/ingestion/email_dedupe.py', 'app/services/ingestion/email_dedupe_store.py', 'app/services/ingestion/email_forwarder_secret_store.py', 'app/routes/email_ingestion.py', 'scripts/pas169_crypto_roundtrip_check.py', 'scripts/pas169_launch_readiness_check.py', 'scripts/pas_launch_integrity_check.py'))
               STORE_FAST               2 (files)

644            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               220 (to L11)
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
               LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR               14 (name)
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
               LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR               14 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

658            LOAD_GLOBAL             16 (SEVERITY_BLOCK)

660            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L9)
               NOT_TAKEN

659            LOAD_CONST               6 ('inbox-scan tokens present: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               19 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L10)

660    L9:     LOAD_CONST               1 ('')

654   L10:     LOAD_CONST               8 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          222 (to L1)

644   L11:     END_FOR
               POP_ITER

662            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA22E0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 665>:
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

Disassembly of <code object check_no_migration_execution at 0x0000018C17D86830, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 665>:
665            RESUME                   0

666            BUILD_LIST               0
               STORE_FAST               1 (out)

667            LOAD_CONST               9 (('scripts/pas_launch_integrity_check.py', 'scripts/pas169_crypto_roundtrip_check.py', 'scripts/pas169_launch_readiness_check.py', 'scripts/rotate_email_forwarder_secret.py', 'scripts/reap_email_dedupe.py', 'app/main.py'))
               STORE_FAST               2 (files)

675            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               220 (to L11)
               STORE_FAST               3 (relpath)

676            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

677            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

678            JUMP_BACKWARD           45 (to L1)

679    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

680            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         5 (src)
               CALL                     1
               STORE_FAST               6 (executable)

681            BUILD_LIST               0
               STORE_FAST               7 (bad)

682            LOAD_GLOBAL              8 (MIGRATION_EXECUTE_TOKENS)
               GET_ITER
       L4:     FOR_ITER                28 (to L6)
               STORE_FAST               8 (token)

683            LOAD_FAST_BORROW_LOAD_FAST_BORROW 134 (token, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L4)

684    L5:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_FAST_BORROW         8 (token)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L4)

682    L6:     END_FOR
               POP_ITER

685            LOAD_FAST                1 (out)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_GLOBAL             13 (_check + NULL)

686            LOAD_CONST               2 ('no_migration_execute:')
               LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR               14 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

687            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L7)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L8)
       L7:     LOAD_CONST               4 ('PASS')

688    L8:     LOAD_CONST               5 ('No migration-execution tokens: ')
               LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR               14 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

689            LOAD_GLOBAL             16 (SEVERITY_BLOCK)

691            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L9)
               NOT_TAKEN

690            LOAD_CONST               6 ('migration-execute tokens present: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               19 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L10)

691    L9:     LOAD_CONST               1 ('')

685   L10:     LOAD_CONST               8 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          222 (to L1)

675   L11:     END_FOR
               POP_ITER

693            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA25B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 696>:
696           RESUME                   0
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

Disassembly of <code object check_no_raw_payload_persistence at 0x0000018C17F781B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 696>:
696            RESUME                   0

717            BUILD_LIST               0
               STORE_FAST               1 (out)

718            LOAD_GLOBAL              0 (EMAIL_INGESTION_SOURCE_FILES)
               GET_ITER
       L1:     FOR_ITER               229 (to L13)
               STORE_FAST               2 (relpath)

719            LOAD_GLOBAL              3 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         2 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               3 (p)

720            LOAD_FAST_BORROW         3 (p)
               LOAD_ATTR                5 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

721            JUMP_BACKWARD           45 (to L1)

722    L2:     LOAD_GLOBAL              7 (_read_text + NULL)
               LOAD_FAST_BORROW         3 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               4 (src)

723            BUILD_LIST               0
               STORE_FAST               5 (bad)

724            LOAD_GLOBAL              8 (EMAIL_INGESTION_FORBIDDEN_PAYLOAD_TOKENS)
               GET_ITER
       L4:     FOR_ITER                48 (to L8)
               STORE_FAST               6 (token)

725            LOAD_CONST               2 ('"')
               LOAD_FAST_BORROW         6 (token)
               FORMAT_SIMPLE
               LOAD_CONST               3 ('":')
               BUILD_STRING             3
               LOAD_CONST               4 ("'")
               LOAD_FAST_BORROW         6 (token)
               FORMAT_SIMPLE
               LOAD_CONST               5 ("':")
               BUILD_STRING             3
               BUILD_TUPLE              2
               GET_ITER
       L5:     FOR_ITER                29 (to L7)
               STORE_FAST               7 (dict_shape)

726            LOAD_FAST_BORROW_LOAD_FAST_BORROW 116 (dict_shape, src)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L6)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L5)

727    L6:     LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_FAST_BORROW         6 (token)
               CALL                     1
               POP_TOP

728            POP_TOP
               JUMP_BACKWARD           46 (to L4)

725    L7:     END_FOR
               POP_ITER
               JUMP_BACKWARD           50 (to L4)

724    L8:     END_FOR
               POP_ITER

729            LOAD_FAST                1 (out)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_GLOBAL             13 (_check + NULL)

730            LOAD_CONST               6 ('no_raw_persistence:')
               LOAD_FAST_BORROW         3 (p)
               LOAD_ATTR               14 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

731            LOAD_FAST_BORROW         5 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN
               LOAD_CONST               7 ('FAIL')
               JUMP_FORWARD             1 (to L10)
       L9:     LOAD_CONST               8 ('PASS')

732   L10:     LOAD_CONST               9 ('No raw-payload persistence path: ')
               LOAD_FAST_BORROW         3 (p)
               LOAD_ATTR               14 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

733            LOAD_GLOBAL             16 (SEVERITY_BLOCK)

736            LOAD_FAST_BORROW         5 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L11)
               NOT_TAKEN

734            LOAD_CONST              10 ('forbidden dict-key shapes present: ')

735            LOAD_CONST              11 (', ')
               LOAD_ATTR               19 (join + NULL|self)
               LOAD_FAST_BORROW         5 (bad)
               CALL                     1

734            BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L12)

736   L11:     LOAD_CONST               1 ('')

729   L12:     LOAD_CONST              12 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          231 (to L1)

718   L13:     END_FOR
               POP_ITER

738            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 741>:
741           RESUME                   0
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

Disassembly of <code object check_no_localhost_self_call at 0x0000018C17F7FF70, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 741>:
741            RESUME                   0

746            BUILD_LIST               0
               STORE_FAST               1 (out)

747            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               STORE_FAST               2 (repo)

748            LOAD_GLOBAL              3 (_walk_python_files + NULL)
               LOAD_FAST_BORROW         2 (repo)
               LOAD_CONST               1 ('app')
               BUILD_LIST               1
               LOAD_CONST               2 (('subdirs',))
               CALL_KW                  2
               STORE_FAST               3 (files)

749            BUILD_LIST               0
               STORE_FAST               4 (bad_by_file)

750            LOAD_FAST_BORROW         3 (files)
               GET_ITER
       L1:     FOR_ITER               158 (to L8)
               STORE_FAST               5 (p)

751            LOAD_GLOBAL              5 (str + NULL)
               LOAD_FAST_BORROW         5 (p)
               LOAD_ATTR                7 (relative_to + NULL|self)
               LOAD_FAST_BORROW         2 (repo)
               CALL                     1
               CALL                     1
               LOAD_ATTR                9 (replace + NULL|self)
               LOAD_CONST               3 ('\\')
               LOAD_CONST               4 ('/')
               CALL                     2
               STORE_FAST               6 (rel)

752            LOAD_FAST_BORROW         6 (rel)
               LOAD_GLOBAL             10 (LOCALHOST_SCAN_EXEMPT_FILES)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        3 (to L2)
               NOT_TAKEN

753            JUMP_BACKWARD           58 (to L1)

754    L2:     LOAD_GLOBAL             13 (_read_text + NULL)
               LOAD_FAST_BORROW         5 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               5 ('')
       L3:     STORE_FAST               7 (src)

755            LOAD_GLOBAL             15 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         7 (src)
               CALL                     1
               STORE_FAST               8 (executable)

756            BUILD_LIST               0
               STORE_FAST               9 (offenders)

757            LOAD_GLOBAL             16 (LOCALHOST_SELF_CALL_TOKENS)
               GET_ITER
       L4:     FOR_ITER                28 (to L6)
               STORE_FAST              10 (token)

758            LOAD_FAST_BORROW_LOAD_FAST_BORROW 168 (token, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L4)

759    L5:     LOAD_FAST_BORROW         9 (offenders)
               LOAD_ATTR               19 (append + NULL|self)
               LOAD_FAST_BORROW        10 (token)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L4)

757    L6:     END_FOR
               POP_ITER

760            LOAD_FAST_BORROW         9 (offenders)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L7)
               NOT_TAKEN
               JUMP_BACKWARD          140 (to L1)

761    L7:     LOAD_FAST_BORROW         4 (bad_by_file)
               LOAD_ATTR               19 (append + NULL|self)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 89 (p, offenders)
               BUILD_TUPLE              2
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          160 (to L1)

750    L8:     END_FOR
               POP_ITER

762            LOAD_FAST_BORROW         4 (bad_by_file)
               TO_BOOL
               POP_JUMP_IF_FALSE      137 (to L11)
               NOT_TAKEN

763            LOAD_FAST_BORROW         4 (bad_by_file)
               GET_ITER
       L9:     FOR_ITER               128 (to L10)
               UNPACK_SEQUENCE          2
               STORE_FAST_STORE_FAST   89 (p, offenders)

764            LOAD_GLOBAL              5 (str + NULL)
               LOAD_FAST_BORROW         5 (p)
               LOAD_ATTR                7 (relative_to + NULL|self)
               LOAD_FAST_BORROW         2 (repo)
               CALL                     1
               CALL                     1
               LOAD_ATTR                9 (replace + NULL|self)
               LOAD_CONST               3 ('\\')
               LOAD_CONST               4 ('/')
               CALL                     2
               STORE_FAST               6 (rel)

765            LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR               19 (append + NULL|self)
               LOAD_GLOBAL             21 (_check + NULL)

766            LOAD_CONST               6 ('localhost_self_call:')
               LOAD_FAST_BORROW         6 (rel)
               FORMAT_SIMPLE
               BUILD_STRING             2

767            LOAD_CONST               7 ('FAIL')

768            LOAD_CONST               8 ('No localhost HTTP self-call in production: ')
               LOAD_FAST_BORROW         6 (rel)
               FORMAT_SIMPLE
               BUILD_STRING             2

769            LOAD_GLOBAL             22 (SEVERITY_BLOCK)

770            LOAD_CONST               9 ('localhost tokens: ')
               LOAD_CONST              10 (', ')
               LOAD_ATTR               25 (join + NULL|self)
               LOAD_GLOBAL             27 (sorted + NULL)
               LOAD_GLOBAL             29 (set + NULL)
               LOAD_FAST_BORROW         9 (offenders)
               CALL                     1
               CALL                     1
               CALL                     1
               BINARY_OP                0 (+)

765            LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          130 (to L9)

763   L10:     END_FOR
               POP_ITER

778            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

773   L11:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR               19 (append + NULL|self)
               LOAD_GLOBAL             21 (_check + NULL)

774            LOAD_CONST              12 ('localhost_self_call:scan')

775            LOAD_CONST              13 ('PASS')

776            LOAD_CONST              14 ('No localhost HTTP self-call in production code')

773            CALL                     3
               CALL                     1
               POP_TOP

778            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 781>:
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

Disassembly of <code object check_pas169_doc_present at 0x0000018C1804D550, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 781>:
781           RESUME                   0

785           BUILD_LIST               0
              STORE_FAST               1 (out)

786           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               1 ('docs')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('pas169_crypto_roundtrip_launch_gate.md')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

787           LOAD_FAST_BORROW         2 (p)
              LOAD_ATTR                3 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

788           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

789           LOAD_CONST               3 ('pas169_doc:present')

790           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_CONST               4 ('PASS')
              JUMP_FORWARD             1 (to L2)
      L1:     LOAD_CONST               5 ('FAIL')

791   L2:     LOAD_CONST               6 ('PAS169 launch doc is present')

792           LOAD_GLOBAL              8 (SEVERITY_BLOCK)

793           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               7 ('')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               8 ('docs/pas169_crypto_roundtrip_launch_gate.md missing')

788   L4:     LOAD_CONST               9 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP

795           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181153E0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 798>:
798           RESUME                   0
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

Disassembly of <code object check_self_no_env_or_db at 0x0000018C17D88130, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 798>:
798            RESUME                   0

801            BUILD_LIST               0
               STORE_FAST               1 (out)

802            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_GLOBAL              2 (__file__)
               CALL                     1
               LOAD_ATTR                5 (resolve + NULL|self)
               CALL                     0
               STORE_FAST               2 (self_path)

803            LOAD_GLOBAL              7 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (self_path)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L1:     STORE_FAST               3 (src)

804            LOAD_GLOBAL              9 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               4 (executable)

805            BUILD_LIST               0
               STORE_FAST               5 (bad)

806            LOAD_FAST_BORROW         4 (executable)
               LOAD_ATTR               11 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L2:     FOR_ITER               199 (to L9)
               STORE_FAST               6 (line)

807            LOAD_FAST_BORROW         6 (line)
               LOAD_ATTR               13 (strip + NULL|self)
               CALL                     0
               STORE_FAST               7 (stripped)

808            LOAD_FAST_BORROW         7 (stripped)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN

809            JUMP_BACKWARD           29 (to L2)

810    L3:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              16 (('import dotenv', 'from dotenv'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L4)
               NOT_TAKEN

811            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               2 ('dotenv import')
               CALL                     1
               POP_TOP

812    L4:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              17 (('import supabase', 'from supabase'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L5)
               NOT_TAKEN

813            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               3 ('supabase import')
               CALL                     1
               POP_TOP

814    L5:     LOAD_CONST               4 ('load_dotenv()')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       18 (to L6)
               NOT_TAKEN

815            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               5 ('load_dotenv() call')
               CALL                     1
               POP_TOP

816    L6:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              18 (('os.environ[', 'getenv('))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L7)
               NOT_TAKEN

817            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               6 ('environ read')
               CALL                     1
               POP_TOP

818    L7:     LOAD_CONST               7 ('get_supabase')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD          182 (to L2)

819    L8:     LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               8 ('supabase client call')
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          201 (to L2)

806    L9:     END_FOR
               POP_ITER

820            LOAD_FAST                1 (out)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_GLOBAL             19 (_check + NULL)

821            LOAD_CONST               9 ('self_check:no_env_or_db')

822            LOAD_FAST_BORROW         5 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST              10 ('FAIL')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST              11 ('PASS')

823   L11:     LOAD_CONST              12 ('Launch integrity checker never reads .env / touches DB')

824            LOAD_GLOBAL             20 (SEVERITY_BLOCK)

826            LOAD_FAST_BORROW         5 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L12)
               NOT_TAKEN

825            LOAD_CONST              13 ('disqualifying code-line patterns: ')
               LOAD_CONST              14 (', ')
               LOAD_ATTR               23 (join + NULL|self)
               LOAD_FAST_BORROW         5 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L13)

826   L12:     LOAD_CONST               1 ('')

820   L13:     LOAD_CONST              15 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

828            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181154D0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 835>:
835           RESUME                   0
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

Disassembly of <code object _aggregate at 0x0000018C17EC44A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 835>:
 835            RESUME                   0

 837            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 836            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2

 837    L2:     FOR_ITER                49 (to L7)
                STORE_FAST               1 (c)

 838            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 837    L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L2)

 838    L4:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              2 (SEVERITY_BLOCK)
                COMPARE_OP              88 (bool(==))

 837    L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L2)
        L6:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L2)
        L7:     END_FOR
                POP_ITER

 836    L8:     STORE_FAST               2 (blockers)
                STORE_FAST               1 (c)

 841            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 840            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L9:     BUILD_LIST               0
                SWAP                     2

 841   L10:     FOR_ITER                49 (to L15)
                STORE_FAST               1 (c)

 842            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 841   L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L10)

 842   L12:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              4 (SEVERITY_INFO)
                COMPARE_OP              88 (bool(==))

 841   L13:     POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L10)
       L14:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L10)
       L15:     END_FOR
                POP_ITER

 840   L16:     STORE_FAST               3 (info)
                STORE_FAST               1 (c)

 845            LOAD_CONST               3 ('verdict')
                LOAD_FAST_BORROW         2 (blockers)
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L17)
                NOT_TAKEN
                LOAD_GLOBAL              6 (VERDICT_NOT_READY)
                JUMP_FORWARD             5 (to L18)
       L17:     LOAD_GLOBAL              8 (VERDICT_READY)

 846   L18:     LOAD_CONST               4 ('blockers')
                LOAD_FAST_BORROW         2 (blockers)

 847            LOAD_CONST               5 ('info')
                LOAD_FAST_BORROW         3 (info)

 844            BUILD_MAP                3
                RETURN_VALUE

  --   L19:     SWAP                     2
                POP_TOP

 836            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0

  --   L20:     SWAP                     2
                POP_TOP

 840            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L19 [2]
  L4 to L5 -> L19 [2]
  L6 to L8 -> L19 [2]
  L9 to L11 -> L20 [2]
  L12 to L13 -> L20 [2]
  L14 to L16 -> L20 [2]

Disassembly of <code object __annotate__ at 0x0000018C181155C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 851>:
851           RESUME                   0
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

Disassembly of <code object _operator_actions at 0x0000018C18048AB0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 851>:
851           RESUME                   0

852           BUILD_LIST               0
              STORE_FAST               1 (out)

853           LOAD_FAST_BORROW         0 (checks)
              GET_ITER
      L1:     FOR_ITER               109 (to L5)
              STORE_FAST               2 (c)

854           LOAD_FAST_BORROW         2 (c)
              LOAD_CONST               0 ('status')
              BINARY_OP               26 ([])
              LOAD_CONST               1 ('FAIL')
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

855           JUMP_BACKWARD           19 (to L1)

856   L2:     LOAD_FAST_BORROW         2 (c)
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

857           LOAD_FAST                1 (out)
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

853   L5:     END_FOR
              POP_ITER

858           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18115980, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 861>:
861           RESUME                   0
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

Disassembly of <code object evaluate at 0x0000018C182E58B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 861>:
861           RESUME                   0

862           BUILD_LIST               0
              STORE_FAST               1 (checks)

863           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              3 (check_required_files + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

864           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              5 (check_memory_review_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

865           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              7 (check_no_forbidden_future_files + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

866           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              9 (check_requirements_cryptography + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

867           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             11 (check_crypto_importable + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

868           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             13 (check_worker_off_by_default + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

869           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             15 (check_no_startup_worker + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

870           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             17 (check_email_routes_auth_scoped + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

871           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             19 (check_no_body_trust + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

872           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             21 (check_no_forbidden_imports + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

873           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             23 (check_no_inbox_scan_tokens + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

874           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             25 (check_no_migration_execution + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

875           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             27 (check_no_raw_payload_persistence + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

876           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             29 (check_no_localhost_self_call + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

877           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             31 (check_pas169_doc_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

878           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             33 (check_self_no_env_or_db + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

880           LOAD_GLOBAL             35 (_aggregate + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1
              STORE_FAST               2 (agg)

882           LOAD_CONST               0 ('phase')
              LOAD_CONST               1 ('PAS-LAUNCH-01')

883           LOAD_CONST               2 ('generated_at')
              LOAD_GLOBAL             37 (_now_iso + NULL)
              CALL                     0

884           LOAD_CONST               3 ('verdict')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])

885           LOAD_CONST               4 ('ready')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])
              LOAD_GLOBAL             38 (VERDICT_READY)
              COMPARE_OP              72 (==)

886           LOAD_CONST               5 ('blocker_count')
              LOAD_GLOBAL             41 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               6 ('blockers')
              BINARY_OP               26 ([])
              CALL                     1

887           LOAD_CONST               7 ('info_count')
              LOAD_GLOBAL             41 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               8 ('info')
              BINARY_OP               26 ([])
              CALL                     1

888           LOAD_CONST               9 ('check_count')
              LOAD_GLOBAL             41 (len + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

889           LOAD_CONST              10 ('pass_count')
              LOAD_GLOBAL             43 (sum + NULL)
              LOAD_CONST              11 (<code object <genexpr> at 0x0000018C180533F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 889>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

890           LOAD_CONST              12 ('fail_count')
              LOAD_GLOBAL             43 (sum + NULL)
              LOAD_CONST              13 (<code object <genexpr> at 0x0000018C18053990, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 890>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

891           LOAD_CONST              14 ('checks')
              LOAD_FAST_BORROW         1 (checks)

892           LOAD_CONST              15 ('operator_actions')
              LOAD_GLOBAL             45 (_operator_actions + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

881           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C180533F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 889>:
 889           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C18053990, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 890>:
 890           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C18115110, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 899>:
899           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C1801C410, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 899>:
899           RESUME                   0

900           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

901           LOAD_CONST               0 ('pas_launch_integrity_check')

903           LOAD_CONST               1 ('PAS-LAUNCH-01 — Single aggregate launch gate. Verifies crypto installability, worker safety, migration posture, route integrity, raw-payload absence, and forbidden-import absence before pilot launch. Read-only — never reads .env, never writes to the DB, never executes a migration, never calls any external API.')

900           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

912           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

913           LOAD_CONST               3 ('--repo-root')
              LOAD_GLOBAL              6 (_REPO_ROOT_DEFAULT)

914           LOAD_CONST               4 ('Repo root to evaluate (default: parent of this script).')

912           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

916           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

917           LOAD_CONST               6 ('--output')
              LOAD_GLOBAL              8 (REPORT_FILENAME)

918           LOAD_CONST               7 ('Where to write the JSON report (default ./')
              LOAD_GLOBAL              8 (REPORT_FILENAME)
              FORMAT_SIMPLE
              LOAD_CONST               8 (').')
              BUILD_STRING             3

916           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

920           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

921           LOAD_CONST               9 ('--json')
              LOAD_CONST              10 ('store_true')

922           LOAD_CONST              11 ('Emit the report JSON on stdout in addition to the summary.')

920           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

924           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

925           LOAD_CONST              13 ('--summary-only')
              LOAD_CONST              10 ('store_true')

926           LOAD_CONST              14 ('Skip writing the full report file; print verdict only.')

924           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

928           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

929           LOAD_CONST              15 ('--strict')
              LOAD_CONST              10 ('store_true')

930           LOAD_CONST              16 ('Exit 1 unless verdict == READY (default policy is the same).')

928           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

932           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18115200, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 935>:
935           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C17D8CD10, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 935>:
935           RESUME                   0

936           LOAD_GLOBAL              1 (print + NULL)

937           LOAD_CONST               0 ('[PAS-LAUNCH-01] verdict=')
              LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               1 ('verdict')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               2 (' blockers=')

938           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               3 ('blocker_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' info=')

939           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               5 ('info_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' checks=')

940           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               7 ('check_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' pass=')

941           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               9 ('pass_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              10 (' fail=')

942           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              11 ('fail_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE

937           BUILD_STRING            12

936           CALL                     1
              POP_TOP

944           LOAD_FAST_BORROW         0 (report)
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

945           LOAD_FAST_BORROW         1 (actions)
              TO_BOOL
              POP_JUMP_IF_FALSE       93 (to L5)
              NOT_TAKEN

946           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              13 ('[PAS-LAUNCH-01] operator actions:')
              CALL                     1
              POP_TOP

947           LOAD_FAST_BORROW         1 (actions)
              LOAD_CONST              14 (slice(None, 25, None))
              BINARY_OP               26 ([])
              GET_ITER
      L2:     FOR_ITER                17 (to L3)
              STORE_FAST               2 (a)

948           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              15 ('  - ')
              LOAD_FAST_BORROW         2 (a)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L2)

947   L3:     END_FOR
              POP_ITER

949           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         1 (actions)
              CALL                     1
              LOAD_SMALL_INT          25
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       34 (to L4)
              NOT_TAKEN

950           LOAD_GLOBAL              1 (print + NULL)
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

949   L4:     LOAD_CONST              18 (None)
              RETURN_VALUE

945   L5:     LOAD_CONST              18 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025030, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 953>:
953           RESUME                   0
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

Disassembly of <code object _write_report at 0x0000018C179C3E10, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 953>:
 953           RESUME                   0

 954           NOP

 955   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

 956           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

 957           LOAD_CONST               3 ('utf-8')

 955           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 959           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

 960   L4:     LOAD_GLOBAL             11 (print + NULL)

 961           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

 962           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

 961           BUILD_STRING             4

 963           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

 960           LOAD_CONST               7 (('file',))
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

 959   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18115B60, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 967>:
967           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17D88FF0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\scripts\pas_launch_integrity_check.py", line 967>:
 967            RESUME                   0

 968            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 969            NOP

 970    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 974    L2:     LOAD_GLOBAL             10 (os)
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

 975            LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               21 (isdir + NULL|self)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L4)
                NOT_TAKEN

 976            LOAD_GLOBAL             23 (print + NULL)

 977            LOAD_CONST               2 ('error: --repo-root not a directory: ')
                LOAD_FAST                4 (repo_root)
                FORMAT_SIMPLE
                BUILD_STRING             2

 978            LOAD_GLOBAL             24 (sys)
                LOAD_ATTR               26 (stderr)

 976            LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

 980            LOAD_SMALL_INT           2
                RETURN_VALUE

 982    L4:     LOAD_GLOBAL             29 (evaluate + NULL)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                STORE_FAST               5 (report)

 984            LOAD_FAST                2 (args)
                LOAD_ATTR               30 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L5)
                NOT_TAKEN

 985            LOAD_GLOBAL             33 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               34 (output)
                LOAD_FAST                5 (report)
                CALL                     2
                POP_TOP

 987    L5:     LOAD_GLOBAL             37 (_print_summary + NULL)
                LOAD_FAST                5 (report)
                CALL                     1
                POP_TOP

 989            LOAD_FAST                2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L6)
                NOT_TAKEN

 990            LOAD_GLOBAL             23 (print + NULL)
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

 992    L6:     LOAD_FAST                5 (report)
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

 971            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L17)
                NOT_TAKEN
                STORE_FAST               3 (e)

 972    L9:     LOAD_FAST                3 (e)
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

 971   L17:     RERAISE                  0

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
