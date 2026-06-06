# scripts_readiness/pas169_launch_readiness_check

- **pyc:** `scripts\__pycache__\pas169_launch_readiness_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/pas169_launch_readiness_check.py`
- **co_filename (from bytecode):** `scripts\pas169_launch_readiness_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS169 — Launch readiness gate.

Aggregates the PAS160 → PAS168 structural posture plus the
PAS169 crypto-roundtrip status into a single yes/no verdict
for the pilot launch. Read-only, no DB writes, no migrations,
no ``.env`` reads.

What this checker verifies:

  * cryptography is declared in ``requirements.txt``.
  * cryptography is importable in this runtime (NOT just
    declared — actually loadable).
  * The PAS169 crypto roundtrip script exists.
  * The PAS160 → PAS168 readiness scripts all exist.
  * The email ingestion route uses the secret-store helper
    (no direct ``brokerage["email_forwarder_secret"]`` reads).
  * No Gmail / Google / IMAP / POP3 / inbox-scan tokens in
    the email subsystem.
  * No embedding / vector / vendor (other than the already-
    pinned dependencies) imports.
  * No Memory Review modification.
  * No migration execution references in the launch scripts.
  * The plaintext-drop migration does NOT exist yet (PAS168
    is intentionally non-destructive; PAS169 must not invent
    one).
  * The PAS169 docs exist.

What this checker does NOT do:

  * Touch the database, run any migration, or read any
    ``.env`` file.
  * Print key material, plaintext secrets, or ciphertext.
  * Insert any events. Logging stays structural-on-stdout
    only.

Usage:
  python scripts/pas169_launch_readiness_check.py
  python scripts/pas169_launch_readiness_check.py --json
  python scripts/pas169_launch_readiness_check.py --summary-only
  python scripts/pas169_launch_readiness_check.py --strict

Exit codes:
    0  — READY  (verdict == READY)
    1  — NOT_READY
    2  — bad CLI arguments
```

## Imports

`List`, `Optional`, `Path`, `__future__`, `annotations`, `argparse`, `datetime`, `importlib.util`, `json`, `os`, `pathlib`, `sys`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_aggregate`, `_build_parser`, `_check`, `_now_iso`, `_operator_actions`, `_print_summary`, `_read_text`, `_strip_python_comments_and_strings`, `_write_report`, `check_crypto_importable`, `check_docs_required_doctrine`, `check_files_present`, `check_memory_review_intact`, `check_no_forbidden_future_files`, `check_no_forbidden_imports`, `check_no_inbox_scanning`, `check_no_migration_execution`, `check_prior_phases_intact`, `check_requirements`, `check_route_uses_secret_helper`, `check_self_no_env_or_db`, `evaluate`, `main`

## Env-key candidates

`BLOCK`, `FAIL`, `INFO`, `NOT_READY`, `PAS169`, `PASS`, `READY`

## String constants (redacted where noted)

- '\nPAS169 — Launch readiness gate.\n\nAggregates the PAS160 → PAS168 structural posture plus the\nPAS169 crypto-roundtrip status into a single yes/no verdict\nfor the pilot launch. Read-only, no DB writes, no migrations,\nno ``.env`` reads.\n\nWhat this checker verifies:\n\n  * cryptography is declared in ``requirements.txt``.\n  * cryptography is importable in this runtime (NOT just\n    declared — actually loadable).\n  * The PAS169 crypto roundtrip script exists.\n  * The PAS160 → PAS168 readiness scripts all exist.\n  * The email ingestion route uses the secret-store helper\n    (no direct ``brokerage["email_forwarder_secret"]`` reads).\n  * No Gmail / Google / IMAP / POP3 / inbox-scan tokens in\n    the email subsystem.\n  * No embedding / vector / vendor (other than the already-\n    pinned dependencies) imports.\n  * No Memory Review modification.\n  * No migration execution references in the launch scripts.\n  * The plaintext-drop migration does NOT exist yet (PAS168\n    is intentionally non-destructive; PAS169 must not invent\n    one).\n  * The PAS169 docs exist.\n\nWhat this checker does NOT do:\n\n  * Touch the database, run any migration, or read any\n    ``.env`` file.\n  * Print key material, plaintext secrets, or ciphertext.\n  * Insert any events. Logging stays structural-on-stdout\n    only.\n\nUsage:\n  python scripts/pas169_launch_readiness_check.py\n  python scripts/pas169_launch_readiness_check.py --json\n  python scripts/pas169_launch_readiness_check.py --summary-only\n  python scripts/pas169_launch_readiness_check.py --strict\n\nExit codes:\n    0  — READY  (verdict == READY)\n    1  — NOT_READY\n    2  — bad CLI arguments\n'
- 'utf-8'
- 'READY'
- 'NOT_READY'
- 'BLOCK'
- 'INFO'
- 'severity'
- 'detail'
- 'pas169_launch_readiness_report.json'
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
- 'Required PAS169 file present: '
- 'missing'
- 'prior_phase:'
- 'Prior-phase readiness script intact: '
- 'missing — PAS169 must not delete'
- 'memory_review_file:'
- 'Memory Review file present: '
- 'Memory Review file deleted'
- 'future_file_absent:'
- 'PAS169 must NOT invent: '
- 'file '
- ' present — PAS169 may not ship the destructive plaintext-drop migration'
- 'requirements.txt'
- 'cryptography'
- 'requirements:cryptography_declared'
- 'requirements.txt declares cryptography'
- 'cryptography missing from requirements.txt'
- 'Verify that cryptography is ACTUALLY importable in the\ncurrent Python environment — declaring it in\nrequirements.txt is necessary but not sufficient. This is\nthe deployment-risk knot PAS169 is built to catch.'
- 'cryptography.fernet'
- 'crypto:importable'
- 'cryptography.fernet is importable'
- 'find_spec raised '
- 'cryptography package is declared in requirements.txt but is NOT installed in this Python environment. Run `pip install -r requirements.txt` before launch.'
- 'app'
- 'routes'
- 'email_ingestion.py'
- 'get_email_forwarder_secret'
- 'route:uses_secret_helper'
- 'Email-ingestion route uses get_email_forwarder_secret'
- 'secret-helper reference missing'
- 'brokerage["email_forwarder_secret"]'
- "brokerage['email_forwarder_secret']"
- 'route:no_direct_plaintext_read'
- 'Route does not directly read email_forwarder_secret'
- 'direct plaintext read present — must go via helper'
- 'scripts/pas169_crypto_roundtrip_check.py'
- 'forbidden_import:'
- 'No forbidden imports: '
- 'forbidden import prefixes: '
- 'no_inbox_scan:'
- 'No inbox-scanning tokens: '
- 'inbox-scan tokens present: '
- 'no_migration_execute:'
- 'No migration-execution tokens: '
- 'migration-execute tokens present: '
- 'docs'
- 'pas169_crypto_roundtrip_launch_gate.md'
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
- 'PAS169 launch checker never reads .env or touches DB'
- 'disqualifying code-line patterns: '
- 'checks'
- 'verdict'
- 'blockers'
- 'info'
- 'List[str]'
- ' — '
- 'see report'
- 'phase'
- 'PAS169'
- 'generated_at'
- 'ready'
- 'blocker_count'
- 'info_count'
- 'check_count'
- 'pass_count'
- 'fail_count'
- 'operator_actions'
- 'argparse.ArgumentParser'
- 'pas169_launch_readiness_check'
- 'PAS169 — Aggregate launch readiness gate. Verifies cryptography is BOTH declared AND actually importable, PAS160 → PAS168 scripts exist, the email route uses the secret-store helper, no migration execution is wired into the launch scripts, and the PAS169 docs carry the required doctrine. Read-only — never reads .env, never writes to the DB, never runs a migration.'
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
- '[PAS169-launch] verdict='
- ' blockers='
- ' info='
- ' checks='
- ' pass='
- ' fail='
- '[PAS169-launch] operator actions:'
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

   1           LOAD_CONST               0 ('\nPAS169 — Launch readiness gate.\n\nAggregates the PAS160 → PAS168 structural posture plus the\nPAS169 crypto-roundtrip status into a single yes/no verdict\nfor the pilot launch. Read-only, no DB writes, no migrations,\nno ``.env`` reads.\n\nWhat this checker verifies:\n\n  * cryptography is declared in ``requirements.txt``.\n  * cryptography is importable in this runtime (NOT just\n    declared — actually loadable).\n  * The PAS169 crypto roundtrip script exists.\n  * The PAS160 → PAS168 readiness scripts all exist.\n  * The email ingestion route uses the secret-store helper\n    (no direct ``brokerage["email_forwarder_secret"]`` reads).\n  * No Gmail / Google / IMAP / POP3 / inbox-scan tokens in\n    the email subsystem.\n  * No embedding / vector / vendor (other than the already-\n    pinned dependencies) imports.\n  * No Memory Review modification.\n  * No migration execution references in the launch scripts.\n  * The plaintext-drop migration does NOT exist yet (PAS168\n    is intentionally non-destructive; PAS169 must not invent\n    one).\n  * The PAS169 docs exist.\n\nWhat this checker does NOT do:\n\n  * Touch the database, run any migration, or read any\n    ``.env`` file.\n  * Print key material, plaintext secrets, or ciphertext.\n  * Insert any events. Logging stays structural-on-stdout\n    only.\n\nUsage:\n  python scripts/pas169_launch_readiness_check.py\n  python scripts/pas169_launch_readiness_check.py --json\n  python scripts/pas169_launch_readiness_check.py --summary-only\n  python scripts/pas169_launch_readiness_check.py --strict\n\nExit codes:\n    0  — READY  (verdict == READY)\n    1  — NOT_READY\n    2  — bad CLI arguments\n')
               STORE_NAME               0 (__doc__)

  49           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  51           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  52           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (importlib.util)
               STORE_NAME               5 (importlib)

  53           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (json)
               STORE_NAME               6 (json)

  54           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              7 (os)
               STORE_NAME               7 (os)

  55           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              8 (sys)
               STORE_NAME               8 (sys)

  56           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              9 (datetime)
               IMPORT_FROM              9 (datetime)
               STORE_NAME               9 (datetime)
               IMPORT_FROM             10 (timezone)
               STORE_NAME              10 (timezone)
               POP_TOP

  57           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Path',))
               IMPORT_NAME             11 (pathlib)
               IMPORT_FROM             12 (Path)
               STORE_NAME              12 (Path)
               POP_TOP

  58           LOAD_SMALL_INT           0
               LOAD_CONST               5 (('List', 'Optional'))
               IMPORT_NAME             13 (typing)
               IMPORT_FROM             14 (List)
               STORE_NAME              14 (List)
               IMPORT_FROM             15 (Optional)
               STORE_NAME              15 (Optional)
               POP_TOP

  61           LOAD_NAME                8 (sys)
               LOAD_ATTR               32 (stdout)
               LOAD_NAME                8 (sys)
               LOAD_ATTR               34 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              18 (_stream)

  62           NOP

  63   L2:     LOAD_NAME               18 (_stream)
               LOAD_ATTR               39 (reconfigure + NULL|self)
               LOAD_CONST               6 ('utf-8')
               LOAD_CONST               7 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  61   L4:     END_FOR
               POP_ITER

  68           LOAD_NAME                7 (os)
               LOAD_ATTR               42 (path)
               LOAD_ATTR               45 (abspath + NULL|self)

  69           LOAD_NAME                7 (os)
               LOAD_ATTR               42 (path)
               LOAD_ATTR               47 (join + NULL|self)
               LOAD_NAME                7 (os)
               LOAD_ATTR               42 (path)
               LOAD_ATTR               49 (dirname + NULL|self)
               LOAD_NAME               25 (__file__)
               CALL                     1
               LOAD_CONST               8 ('..')
               CALL                     2

  68           CALL                     1
               STORE_NAME              26 (_REPO_ROOT_DEFAULT)

  73           LOAD_CONST               9 ('READY')
               STORE_NAME              27 (VERDICT_READY)

  74           LOAD_CONST              10 ('NOT_READY')
               STORE_NAME              28 (VERDICT_NOT_READY)

  76           LOAD_CONST              11 ('BLOCK')
               STORE_NAME              29 (SEVERITY_BLOCK)

  77           LOAD_CONST              12 ('INFO')
               STORE_NAME              30 (SEVERITY_INFO)

  84           LOAD_CONST              64 (('requirements.txt', 'scripts/pas169_crypto_roundtrip_check.py', 'scripts/pas169_launch_readiness_check.py', 'docs/pas169_crypto_roundtrip_launch_gate.md', 'tests/mvp/test_pas169_crypto_roundtrip_gate.py', 'app/services/ingestion/email_forwarder_secret_store.py', 'app/routes/email_ingestion.py'))
               STORE_NAME              31 (REQUIRED_FILES)

  94           LOAD_CONST              65 (('scripts/pas160_mvp_sequence_check.py', 'scripts/pas161_lead_ingestion_readiness_check.py', 'scripts/pas162_pending_calls_readiness_check.py', 'scripts/pas163_candidate_pipeline_readiness_check.py', 'scripts/pas164_email_ingestion_readiness_check.py', 'scripts/pas165_email_auth_dedupe_readiness_check.py', 'scripts/pas166_email_dedupe_policy_readiness_check.py', 'scripts/pas167_email_secret_reaper_readiness_check.py', 'scripts/pas168_email_secret_rotation_readiness_check.py'))
               STORE_NAME              32 (PRIOR_PHASE_FILES)

 106           LOAD_CONST              66 (('app/services/memory/review.py', 'app/services/memory/review_stats.py', 'app/services/memory/review_export.py', 'app/services/memory/review_actors.py', 'app/services/memory/review_alerts.py', 'app/services/memory/operator_console.py'))
               STORE_NAME              33 (MEMORY_REVIEW_FILES)

 118           LOAD_CONST              67 (('scripts/migrate_v17_drop_plaintext_email_forwarder_secret.sql',))
               STORE_NAME              34 (FORBIDDEN_FUTURE_FILES)

 125           LOAD_CONST              68 (('import googleapiclient', 'from googleapiclient', 'import google.oauth2', 'from google.oauth2', 'from google.auth', 'import google.auth', 'from google_auth_oauthlib', 'import composio', 'from composio', 'import trustclaw', 'from trustclaw', 'import numpy', 'import faiss', 'import pgvector', 'from pgvector', 'from openai import embeddings', 'from openai.embeddings', 'from app.services.memory', 'import app.services.memory', 'import imaplib', 'from imaplib', 'import poplib', 'from poplib'))
               STORE_NAME              35 (FORBIDDEN_IMPORT_LINE_PREFIXES)

 151           LOAD_CONST              69 (('imaplib', 'poplib', 'fetch_inbox', 'gmail_oauth', 'gmail_token', 'users().messages'))
               STORE_NAME              36 (FORBIDDEN_INBOX_TOKENS)

 164           LOAD_CONST              70 (('alembic.command.upgrade', 'subprocess.run(["alembic"', 'subprocess.Popen(["alembic"', 'db.execute(', '.sql.execute('))
               STORE_NAME              37 (MIGRATION_EXECUTE_TOKENS)

 177           LOAD_CONST              13 ('severity')

 179           LOAD_NAME               29 (SEVERITY_BLOCK)

 177           LOAD_CONST              14 ('detail')

 179           LOAD_CONST              15 ('')

 177           BUILD_MAP                2
               LOAD_CONST              16 (<code object __annotate__ at 0x0000018C18024C30, file "scripts\pas169_launch_readiness_check.py", line 177>)
               MAKE_FUNCTION
               LOAD_CONST              17 (<code object _check at 0x0000018C17FA2F10, file "scripts\pas169_launch_readiness_check.py", line 177>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              38 (_check)

 190           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA2970, file "scripts\pas169_launch_readiness_check.py", line 190>)
               MAKE_FUNCTION
               LOAD_CONST              19 (<code object _now_iso at 0x0000018C18038CB0, file "scripts\pas169_launch_readiness_check.py", line 190>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              39 (_now_iso)

 194           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA33C0, file "scripts\pas169_launch_readiness_check.py", line 194>)
               MAKE_FUNCTION
               LOAD_CONST              21 (<code object _read_text at 0x0000018C18053E10, file "scripts\pas169_launch_readiness_check.py", line 194>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              40 (_read_text)

 201           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA35A0, file "scripts\pas169_launch_readiness_check.py", line 201>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object _strip_python_comments_and_strings at 0x0000018C17D81580, file "scripts\pas169_launch_readiness_check.py", line 201>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              41 (_strip_python_comments_and_strings)

 240           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA3D20, file "scripts\pas169_launch_readiness_check.py", line 240>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object check_files_present at 0x0000018C180608A0, file "scripts\pas169_launch_readiness_check.py", line 240>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              42 (check_files_present)

 254           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA1D40, file "scripts\pas169_launch_readiness_check.py", line 254>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object check_prior_phases_intact at 0x0000018C18060A50, file "scripts\pas169_launch_readiness_check.py", line 254>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              43 (check_prior_phases_intact)

 268           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA2880, file "scripts\pas169_launch_readiness_check.py", line 268>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object check_memory_review_intact at 0x0000018C18060C00, file "scripts\pas169_launch_readiness_check.py", line 268>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              44 (check_memory_review_intact)

 282           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA2100, file "scripts\pas169_launch_readiness_check.py", line 282>)
               MAKE_FUNCTION
               LOAD_CONST              31 (<code object check_no_forbidden_future_files at 0x0000018C180483B0, file "scripts\pas169_launch_readiness_check.py", line 282>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              45 (check_no_forbidden_future_files)

 298           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA2B50, file "scripts\pas169_launch_readiness_check.py", line 298>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object check_requirements at 0x0000018C17D76C00, file "scripts\pas169_launch_readiness_check.py", line 298>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              46 (check_requirements)

 317           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA32D0, file "scripts\pas169_launch_readiness_check.py", line 317>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object check_crypto_importable at 0x0000018C17F733B0, file "scripts\pas169_launch_readiness_check.py", line 317>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              47 (check_crypto_importable)

 356           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C17FA1E30, file "scripts\pas169_launch_readiness_check.py", line 356>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object check_route_uses_secret_helper at 0x0000018C17F72C90, file "scripts\pas169_launch_readiness_check.py", line 356>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              48 (check_route_uses_secret_helper)

 385           LOAD_CONST              38 (<code object __annotate__ at 0x0000018C17FA2E20, file "scripts\pas169_launch_readiness_check.py", line 385>)
               MAKE_FUNCTION
               LOAD_CONST              39 (<code object check_no_forbidden_imports at 0x0000018C17D86EB0, file "scripts\pas169_launch_readiness_check.py", line 385>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              49 (check_no_forbidden_imports)

 413           LOAD_CONST              40 (<code object __annotate__ at 0x0000018C17FA21F0, file "scripts\pas169_launch_readiness_check.py", line 413>)
               MAKE_FUNCTION
               LOAD_CONST              41 (<code object check_no_inbox_scanning at 0x0000018C17CC1F60, file "scripts\pas169_launch_readiness_check.py", line 413>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              50 (check_no_inbox_scanning)

 438           LOAD_CONST              42 (<code object __annotate__ at 0x0000018C17FA26A0, file "scripts\pas169_launch_readiness_check.py", line 438>)
               MAKE_FUNCTION
               LOAD_CONST              43 (<code object check_no_migration_execution at 0x0000018C17CC2460, file "scripts\pas169_launch_readiness_check.py", line 438>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              51 (check_no_migration_execution)

 463           LOAD_CONST              44 (<code object __annotate__ at 0x0000018C17FA2790, file "scripts\pas169_launch_readiness_check.py", line 463>)
               MAKE_FUNCTION
               LOAD_CONST              45 (<code object check_docs_required_doctrine at 0x0000018C17D8A4D0, file "scripts\pas169_launch_readiness_check.py", line 463>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              52 (check_docs_required_doctrine)

 501           LOAD_CONST              46 (<code object __annotate__ at 0x0000018C17FA22E0, file "scripts\pas169_launch_readiness_check.py", line 501>)
               MAKE_FUNCTION
               LOAD_CONST              47 (<code object check_self_no_env_or_db at 0x0000018C17D88C40, file "scripts\pas169_launch_readiness_check.py", line 501>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              53 (check_self_no_env_or_db)

 539           LOAD_CONST              48 (<code object __annotate__ at 0x0000018C17FA24C0, file "scripts\pas169_launch_readiness_check.py", line 539>)
               MAKE_FUNCTION
               LOAD_CONST              49 (<code object _aggregate at 0x0000018C17EC4280, file "scripts\pas169_launch_readiness_check.py", line 539>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              54 (_aggregate)

 555           LOAD_CONST              50 (<code object __annotate__ at 0x0000018C17FA25B0, file "scripts\pas169_launch_readiness_check.py", line 555>)
               MAKE_FUNCTION
               LOAD_CONST              51 (<code object _operator_actions at 0x0000018C18048730, file "scripts\pas169_launch_readiness_check.py", line 555>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              55 (_operator_actions)

 565           LOAD_CONST              52 (<code object __annotate__ at 0x0000018C17FA23D0, file "scripts\pas169_launch_readiness_check.py", line 565>)
               MAKE_FUNCTION
               LOAD_CONST              53 (<code object evaluate at 0x0000018C17EA77F0, file "scripts\pas169_launch_readiness_check.py", line 565>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              56 (evaluate)

 596           LOAD_CONST              54 ('pas169_launch_readiness_report.json')
               STORE_NAME              57 (REPORT_FILENAME)

 599           LOAD_CONST              55 (<code object __annotate__ at 0x0000018C17FA2D30, file "scripts\pas169_launch_readiness_check.py", line 599>)
               MAKE_FUNCTION
               LOAD_CONST              56 (<code object _build_parser at 0x0000018C179A7290, file "scripts\pas169_launch_readiness_check.py", line 599>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              58 (_build_parser)

 637           LOAD_CONST              57 (<code object __annotate__ at 0x0000018C17FA2A60, file "scripts\pas169_launch_readiness_check.py", line 637>)
               MAKE_FUNCTION
               LOAD_CONST              58 (<code object _print_summary at 0x0000018C17D8CD10, file "scripts\pas169_launch_readiness_check.py", line 637>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              59 (_print_summary)

 655           LOAD_CONST              59 (<code object __annotate__ at 0x0000018C18025130, file "scripts\pas169_launch_readiness_check.py", line 655>)
               MAKE_FUNCTION
               LOAD_CONST              60 (<code object _write_report at 0x0000018C180FC030, file "scripts\pas169_launch_readiness_check.py", line 655>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              60 (_write_report)

 669           LOAD_CONST              71 ((None,))
               LOAD_CONST              61 (<code object __annotate__ at 0x0000018C17FA2C40, file "scripts\pas169_launch_readiness_check.py", line 669>)
               MAKE_FUNCTION
               LOAD_CONST              62 (<code object main at 0x0000018C17D88FF0, file "scripts\pas169_launch_readiness_check.py", line 669>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              61 (main)

 697           LOAD_NAME               62 (__name__)
               LOAD_CONST              63 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 698           LOAD_NAME                8 (sys)
               LOAD_ATTR              126 (exit)
               PUSH_NULL
               LOAD_NAME               61 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 697   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  64           LOAD_NAME               20 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  65   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          319 (to L1)

  64   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "scripts\pas169_launch_readiness_check.py", line 177>:
177           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('check_id')

178           LOAD_CONST               2 ('str')

177           LOAD_CONST               3 ('status')

178           LOAD_CONST               2 ('str')

177           LOAD_CONST               4 ('label')

178           LOAD_CONST               2 ('str')

177           LOAD_CONST               5 ('severity')

179           LOAD_CONST               2 ('str')

177           LOAD_CONST               6 ('detail')

179           LOAD_CONST               2 ('str')

177           LOAD_CONST               7 ('return')

180           LOAD_CONST               8 ('dict')

177           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _check at 0x0000018C17FA2F10, file "scripts\pas169_launch_readiness_check.py", line 177>:
177           RESUME                   0

182           LOAD_CONST               0 ('id')
              LOAD_FAST_BORROW         0 (check_id)

183           LOAD_CONST               1 ('status')
              LOAD_FAST_BORROW         1 (status)

184           LOAD_CONST               2 ('label')
              LOAD_FAST_BORROW         2 (label)

185           LOAD_CONST               3 ('severity')
              LOAD_FAST_BORROW         3 (severity)

186           LOAD_CONST               4 ('detail')
              LOAD_FAST_BORROW         4 (detail)

181           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "scripts\pas169_launch_readiness_check.py", line 190>:
190           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038CB0, file "scripts\pas169_launch_readiness_check.py", line 190>:
190           RESUME                   0

191           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "scripts\pas169_launch_readiness_check.py", line 194>:
194           RESUME                   0
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

Disassembly of <code object _read_text at 0x0000018C18053E10, file "scripts\pas169_launch_readiness_check.py", line 194>:
 194           RESUME                   0

 195           NOP

 196   L1:     LOAD_FAST_BORROW         0 (path)
               LOAD_ATTR                1 (read_text + NULL|self)
               LOAD_CONST               0 ('utf-8')
               LOAD_CONST               1 ('replace')
               LOAD_CONST               2 (('encoding', 'errors'))
               CALL_KW                  2
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 197           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 198   L4:     POP_EXCEPT
               LOAD_CONST               3 (None)
               RETURN_VALUE

 197   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "scripts\pas169_launch_readiness_check.py", line 201>:
201           RESUME                   0
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

Disassembly of <code object _strip_python_comments_and_strings at 0x0000018C17D81580, file "scripts\pas169_launch_readiness_check.py", line 201>:
201            RESUME                   0

202            BUILD_LIST               0
               STORE_FAST               1 (out)

203            LOAD_SMALL_INT           0
               LOAD_GLOBAL              1 (len + NULL)
               LOAD_FAST_BORROW         0 (src)
               CALL                     1
               STORE_FAST_STORE_FAST   50 (n, i)

204    L1:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (i, n)
               COMPARE_OP              18 (bool(<))
               EXTENDED_ARG             1
               POP_JUMP_IF_FALSE      282 (to L13)
               NOT_TAKEN

205            LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               BINARY_OP               26 ([])
               STORE_FAST               4 (ch)

206            LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               1 ('#')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       38 (to L3)
               NOT_TAKEN

207            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_CONST               2 ('\n')
               LOAD_FAST_BORROW         2 (i)
               CALL                     2
               STORE_FAST               5 (j)

208            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L2)
               NOT_TAKEN

209            JUMP_FORWARD           240 (to L13)

210    L2:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

211            JUMP_BACKWARD           59 (to L1)

212    L3:     LOAD_FAST_BORROW         0 (src)
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

213    L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               BINARY_SLICE
               STORE_FAST               6 (quote)

214            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 98 (quote, i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               CALL                     2
               STORE_FAST               7 (end)

215            LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L5)
               NOT_TAKEN

216            JUMP_FORWARD           138 (to L13)

217    L5:     LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

218            JUMP_BACKWARD          161 (to L1)

219    L6:     LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               7 (('"', "'"))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       92 (to L12)
               NOT_TAKEN

220            LOAD_FAST                4 (ch)
               STORE_FAST               6 (quote)

221            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               5 (j)

222    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (j, n)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       63 (to L11)
               NOT_TAKEN

223            LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
               BINARY_OP               26 ([])
               LOAD_CONST               5 ('\\')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       12 (to L8)
               NOT_TAKEN

224            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           2
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)

225            JUMP_BACKWARD           30 (to L7)

226    L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
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

227    L9:     JUMP_FORWARD            11 (to L11)

228   L10:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)
               JUMP_BACKWARD           68 (to L7)

229   L11:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

230            EXTENDED_ARG             1
               JUMP_BACKWARD          259 (to L1)

231   L12:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (ch)
               CALL                     1
               POP_TOP

232            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               2 (i)
               EXTENDED_ARG             1
               JUMP_BACKWARD          288 (to L1)

233   L13:     LOAD_CONST               6 ('')
               LOAD_ATTR                9 (join + NULL|self)
               LOAD_FAST_BORROW         1 (out)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3D20, file "scripts\pas169_launch_readiness_check.py", line 240>:
240           RESUME                   0
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

Disassembly of <code object check_files_present at 0x0000018C180608A0, file "scripts\pas169_launch_readiness_check.py", line 240>:
240           RESUME                   0

241           BUILD_LIST               0
              STORE_FAST               1 (out)

242           LOAD_GLOBAL              0 (REQUIRED_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

243           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

244           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

245           LOAD_CONST               0 ('file:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

246           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

247   L3:     LOAD_CONST               3 ('Required PAS169 file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

248           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

249           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing')

244   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

242   L6:     END_FOR
              POP_ITER

251           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1D40, file "scripts\pas169_launch_readiness_check.py", line 254>:
254           RESUME                   0
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

Disassembly of <code object check_prior_phases_intact at 0x0000018C18060A50, file "scripts\pas169_launch_readiness_check.py", line 254>:
254           RESUME                   0

255           BUILD_LIST               0
              STORE_FAST               1 (out)

256           LOAD_GLOBAL              0 (PRIOR_PHASE_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

257           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

258           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

259           LOAD_CONST               0 ('prior_phase:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

260           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

261   L3:     LOAD_CONST               3 ('Prior-phase readiness script intact: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

262           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

263           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing — PAS169 must not delete')

258   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

256   L6:     END_FOR
              POP_ITER

265           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "scripts\pas169_launch_readiness_check.py", line 268>:
268           RESUME                   0
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

Disassembly of <code object check_memory_review_intact at 0x0000018C18060C00, file "scripts\pas169_launch_readiness_check.py", line 268>:
268           RESUME                   0

269           BUILD_LIST               0
              STORE_FAST               1 (out)

270           LOAD_GLOBAL              0 (MEMORY_REVIEW_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

271           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

272           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

273           LOAD_CONST               0 ('memory_review_file:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

274           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

275   L3:     LOAD_CONST               3 ('Memory Review file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

276           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

277           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('Memory Review file deleted')

272   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

270   L6:     END_FOR
              POP_ITER

279           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "scripts\pas169_launch_readiness_check.py", line 282>:
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

Disassembly of <code object check_no_forbidden_future_files at 0x0000018C180483B0, file "scripts\pas169_launch_readiness_check.py", line 282>:
282           RESUME                   0

283           BUILD_LIST               0
              STORE_FAST               1 (out)

284           LOAD_GLOBAL              0 (FORBIDDEN_FUTURE_FILES)
              GET_ITER
      L1:     FOR_ITER               100 (to L6)
              STORE_FAST               2 (p)

285           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (exists + NULL|self)
              CALL                     0
              STORE_FAST               3 (present)

286           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

287           LOAD_CONST               0 ('future_file_absent:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

288           LOAD_FAST_BORROW         3 (present)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('FAIL')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('PASS')

289   L3:     LOAD_CONST               3 ('PAS169 must NOT invent: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

290           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

293           LOAD_FAST_BORROW         3 (present)
              TO_BOOL
              POP_JUMP_IF_FALSE        7 (to L4)
              NOT_TAKEN

291           LOAD_CONST               4 ('file ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              LOAD_CONST               5 (' present — PAS169 may not ship the destructive plaintext-drop migration')
              BUILD_STRING             3
              JUMP_FORWARD             1 (to L5)

293   L4:     LOAD_CONST               6 ('')

286   L5:     LOAD_CONST               7 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD          102 (to L1)

284   L6:     END_FOR
              POP_ITER

295           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "scripts\pas169_launch_readiness_check.py", line 298>:
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

Disassembly of <code object check_requirements at 0x0000018C17D76C00, file "scripts\pas169_launch_readiness_check.py", line 298>:
298           RESUME                   0

299           BUILD_LIST               0
              STORE_FAST               1 (out)

300           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('requirements.txt')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

301           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 ('')
      L1:     STORE_FAST               3 (src)

302           LOAD_CONST               2 (False)
              STORE_FAST               4 (has_crypto)

303           LOAD_FAST_BORROW         3 (src)
              LOAD_ATTR                5 (splitlines + NULL|self)
              CALL                     0
              GET_ITER
      L2:     FOR_ITER                58 (to L4)
              STORE_FAST               5 (line)

304           LOAD_FAST_BORROW         5 (line)
              LOAD_ATTR                7 (strip + NULL|self)
              CALL                     0
              LOAD_ATTR                9 (lower + NULL|self)
              CALL                     0
              LOAD_ATTR               11 (startswith + NULL|self)
              LOAD_CONST               3 ('cryptography')
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           56 (to L2)

305   L3:     LOAD_CONST               4 (True)
              STORE_FAST               4 (has_crypto)

306           POP_TOP
              JUMP_FORWARD             2 (to L5)

303   L4:     END_FOR
              POP_ITER

307   L5:     LOAD_FAST                1 (out)
              LOAD_ATTR               13 (append + NULL|self)
              LOAD_GLOBAL             15 (_check + NULL)

308           LOAD_CONST               5 ('requirements:cryptography_declared')

309           LOAD_FAST_BORROW         4 (has_crypto)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L6)
              NOT_TAKEN
              LOAD_CONST               6 ('PASS')
              JUMP_FORWARD             1 (to L7)
      L6:     LOAD_CONST               7 ('FAIL')

310   L7:     LOAD_CONST               8 ('requirements.txt declares cryptography')

311           LOAD_GLOBAL             16 (SEVERITY_BLOCK)

312           LOAD_FAST_BORROW         4 (has_crypto)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L8)
              NOT_TAKEN
              LOAD_CONST               1 ('')
              JUMP_FORWARD             1 (to L9)
      L8:     LOAD_CONST               9 ('cryptography missing from requirements.txt')

307   L9:     LOAD_CONST              10 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP

314           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA32D0, file "scripts\pas169_launch_readiness_check.py", line 317>:
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

Disassembly of <code object check_crypto_importable at 0x0000018C17F733B0, file "scripts\pas169_launch_readiness_check.py", line 317>:
 317            RESUME                   0

 322            BUILD_LIST               0
                STORE_FAST               1 (out)

 323            NOP

 324    L1:     LOAD_GLOBAL              0 (importlib)
                LOAD_ATTR                2 (util)
                LOAD_ATTR                5 (find_spec + NULL|self)
                LOAD_CONST               1 ('cryptography.fernet')
                CALL                     1
                STORE_FAST               2 (spec)

 334    L2:     LOAD_FAST                2 (spec)
                POP_JUMP_IF_NOT_NONE    38 (to L3)
                NOT_TAKEN

 335            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 336            LOAD_CONST               2 ('crypto:importable')

 337            LOAD_CONST               3 ('FAIL')

 338            LOAD_CONST               4 ('cryptography.fernet is importable')

 339            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 341            LOAD_CONST               8 ('cryptography package is declared in requirements.txt but is NOT installed in this Python environment. Run `pip install -r requirements.txt` before launch.')

 335            LOAD_CONST               6 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 346            LOAD_FAST                1 (out)
                RETURN_VALUE

 347    L3:     LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 348            LOAD_CONST               2 ('crypto:importable')

 349            LOAD_CONST               9 ('PASS')

 350            LOAD_CONST               4 ('cryptography.fernet is importable')

 351            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 347            LOAD_CONST              10 (('severity',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 353            LOAD_FAST                1 (out)
                RETURN_VALUE

  --    L4:     PUSH_EXC_INFO

 325            LOAD_GLOBAL              6 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       70 (to L9)
                NOT_TAKEN
                STORE_FAST               3 (e)

 326    L5:     LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 327            LOAD_CONST               2 ('crypto:importable')

 328            LOAD_CONST               3 ('FAIL')

 329            LOAD_CONST               4 ('cryptography.fernet is importable')

 330            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 331            LOAD_CONST               5 ('find_spec raised ')
                LOAD_GLOBAL             15 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR               16 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 326            LOAD_CONST               6 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 333            LOAD_FAST                1 (out)
        L6:     SWAP                     2
        L7:     POP_EXCEPT
                LOAD_CONST               7 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RETURN_VALUE

  --    L8:     LOAD_CONST               7 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 325    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L4 [0]
  L4 to L5 -> L10 [1] lasti
  L5 to L6 -> L8 [1] lasti
  L6 to L7 -> L10 [1] lasti
  L8 to L10 -> L10 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "scripts\pas169_launch_readiness_check.py", line 356>:
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

Disassembly of <code object check_route_uses_secret_helper at 0x0000018C17F72C90, file "scripts\pas169_launch_readiness_check.py", line 356>:
356            RESUME                   0

357            BUILD_LIST               0
               STORE_FAST               1 (out)

358            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('routes')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('email_ingestion.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

359            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               3 ('')
       L1:     STORE_FAST               3 (src)

360            LOAD_CONST               4 ('get_email_forwarder_secret')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               STORE_FAST               4 (uses_helper)

361            LOAD_FAST                1 (out)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_GLOBAL              7 (_check + NULL)

362            LOAD_CONST               5 ('route:uses_secret_helper')

363            LOAD_FAST_BORROW         4 (uses_helper)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L2)
               NOT_TAKEN
               LOAD_CONST               6 ('PASS')
               JUMP_FORWARD             1 (to L3)
       L2:     LOAD_CONST               7 ('FAIL')

364    L3:     LOAD_CONST               8 ('Email-ingestion route uses get_email_forwarder_secret')

365            LOAD_GLOBAL              8 (SEVERITY_BLOCK)

366            LOAD_FAST_BORROW         4 (uses_helper)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN
               LOAD_CONST               3 ('')
               JUMP_FORWARD             1 (to L5)
       L4:     LOAD_CONST               9 ('secret-helper reference missing')

361    L5:     LOAD_CONST              10 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

371            LOAD_CONST              11 ('brokerage["email_forwarder_secret"]')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L6)
               NOT_TAKEN
               POP_TOP

372            LOAD_CONST              12 ("brokerage['email_forwarder_secret']")
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

370    L6:     STORE_FAST               5 (direct_read)

374            LOAD_FAST                1 (out)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_GLOBAL              7 (_check + NULL)

375            LOAD_CONST              13 ('route:no_direct_plaintext_read')

376            LOAD_FAST_BORROW         5 (direct_read)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L7)
               NOT_TAKEN
               LOAD_CONST               7 ('FAIL')
               JUMP_FORWARD             1 (to L8)
       L7:     LOAD_CONST               6 ('PASS')

377    L8:     LOAD_CONST              14 ('Route does not directly read email_forwarder_secret')

378            LOAD_GLOBAL              8 (SEVERITY_BLOCK)

380            LOAD_FAST_BORROW         5 (direct_read)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN

379            LOAD_CONST              15 ('direct plaintext read present — must go via helper')
               JUMP_FORWARD             1 (to L10)

380    L9:     LOAD_CONST               3 ('')

374   L10:     LOAD_CONST              10 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

382            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "scripts\pas169_launch_readiness_check.py", line 385>:
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

Disassembly of <code object check_no_forbidden_imports at 0x0000018C17D86EB0, file "scripts\pas169_launch_readiness_check.py", line 385>:
385            RESUME                   0

386            BUILD_LIST               0
               STORE_FAST               1 (out)

387            LOAD_CONST               9 (('scripts/pas169_crypto_roundtrip_check.py', 'scripts/pas169_launch_readiness_check.py', 'app/services/ingestion/email_forwarder_secret_store.py', 'app/routes/email_ingestion.py'))
               STORE_FAST               2 (files)

393            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               241 (to L12)
               STORE_FAST               3 (relpath)

394            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

395            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L2:     STORE_FAST               5 (src)

396            BUILD_LIST               0
               STORE_FAST               6 (bad)

397            LOAD_FAST_BORROW         5 (src)
               LOAD_ATTR                5 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L3:     FOR_ITER                74 (to L7)
               STORE_FAST               7 (line)

398            LOAD_FAST_BORROW         7 (line)
               LOAD_ATTR                7 (strip + NULL|self)
               CALL                     0
               STORE_FAST               8 (stripped)

399            LOAD_GLOBAL              8 (FORBIDDEN_IMPORT_LINE_PREFIXES)
               GET_ITER
       L4:     FOR_ITER                45 (to L6)
               STORE_FAST               9 (prefix)

400            LOAD_FAST_BORROW         8 (stripped)
               LOAD_ATTR               11 (startswith + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           28 (to L4)

401    L5:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR               13 (append + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           47 (to L4)

399    L6:     END_FOR
               POP_ITER
               JUMP_BACKWARD           76 (to L3)

397    L7:     END_FOR
               POP_ITER

402            LOAD_FAST                1 (out)
               LOAD_ATTR               13 (append + NULL|self)
               LOAD_GLOBAL             15 (_check + NULL)

403            LOAD_CONST               2 ('forbidden_import:')
               LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR               16 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

404            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST               4 ('PASS')

405    L9:     LOAD_CONST               5 ('No forbidden imports: ')
               LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR               16 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

406            LOAD_GLOBAL             18 (SEVERITY_BLOCK)

408            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L10)
               NOT_TAKEN

407            LOAD_CONST               6 ('forbidden import prefixes: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               21 (join + NULL|self)
               LOAD_FAST_BORROW         6 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L11)

408   L10:     LOAD_CONST               1 ('')

402   L11:     LOAD_CONST               8 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          243 (to L1)

393   L12:     END_FOR
               POP_ITER

410            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "scripts\pas169_launch_readiness_check.py", line 413>:
413           RESUME                   0
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

Disassembly of <code object check_no_inbox_scanning at 0x0000018C17CC1F60, file "scripts\pas169_launch_readiness_check.py", line 413>:
413            RESUME                   0

414            BUILD_LIST               0
               STORE_FAST               1 (out)

415            LOAD_CONST               9 (('scripts/pas169_crypto_roundtrip_check.py', 'scripts/pas169_launch_readiness_check.py'))
               STORE_FAST               2 (files)

419            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               196 (to L10)
               STORE_FAST               3 (relpath)

420            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

421            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L2:     STORE_FAST               5 (src)

422            LOAD_GLOBAL              5 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         5 (src)
               CALL                     1
               STORE_FAST               6 (executable)

423            BUILD_LIST               0
               STORE_FAST               7 (bad)

424            LOAD_GLOBAL              6 (FORBIDDEN_INBOX_TOKENS)
               GET_ITER
       L3:     FOR_ITER                28 (to L5)
               STORE_FAST               8 (token)

425            LOAD_FAST_BORROW_LOAD_FAST_BORROW 134 (token, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L3)

426    L4:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_FAST_BORROW         8 (token)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L3)

424    L5:     END_FOR
               POP_ITER

427            LOAD_FAST                1 (out)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_GLOBAL             11 (_check + NULL)

428            LOAD_CONST               2 ('no_inbox_scan:')
               LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR               12 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

429            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L6)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L7)
       L6:     LOAD_CONST               4 ('PASS')

430    L7:     LOAD_CONST               5 ('No inbox-scanning tokens: ')
               LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR               12 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

431            LOAD_GLOBAL             14 (SEVERITY_BLOCK)

433            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L8)
               NOT_TAKEN

432            LOAD_CONST               6 ('inbox-scan tokens present: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               17 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L9)

433    L8:     LOAD_CONST               1 ('')

427    L9:     LOAD_CONST               8 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          198 (to L1)

419   L10:     END_FOR
               POP_ITER

435            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA26A0, file "scripts\pas169_launch_readiness_check.py", line 438>:
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

Disassembly of <code object check_no_migration_execution at 0x0000018C17CC2460, file "scripts\pas169_launch_readiness_check.py", line 438>:
438            RESUME                   0

439            BUILD_LIST               0
               STORE_FAST               1 (out)

440            LOAD_CONST               9 (('scripts/pas169_crypto_roundtrip_check.py', 'scripts/pas169_launch_readiness_check.py'))
               STORE_FAST               2 (files)

444            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               196 (to L10)
               STORE_FAST               3 (relpath)

445            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

446            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L2:     STORE_FAST               5 (src)

447            LOAD_GLOBAL              5 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         5 (src)
               CALL                     1
               STORE_FAST               6 (executable)

448            BUILD_LIST               0
               STORE_FAST               7 (bad)

449            LOAD_GLOBAL              6 (MIGRATION_EXECUTE_TOKENS)
               GET_ITER
       L3:     FOR_ITER                28 (to L5)
               STORE_FAST               8 (token)

450            LOAD_FAST_BORROW_LOAD_FAST_BORROW 134 (token, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L3)

451    L4:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_FAST_BORROW         8 (token)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L3)

449    L5:     END_FOR
               POP_ITER

452            LOAD_FAST                1 (out)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_GLOBAL             11 (_check + NULL)

453            LOAD_CONST               2 ('no_migration_execute:')
               LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR               12 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

454            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L6)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L7)
       L6:     LOAD_CONST               4 ('PASS')

455    L7:     LOAD_CONST               5 ('No migration-execution tokens: ')
               LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR               12 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

456            LOAD_GLOBAL             14 (SEVERITY_BLOCK)

458            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L8)
               NOT_TAKEN

457            LOAD_CONST               6 ('migration-execute tokens present: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               17 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L9)

458    L8:     LOAD_CONST               1 ('')

452    L9:     LOAD_CONST               8 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          198 (to L1)

444   L10:     END_FOR
               POP_ITER

460            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2790, file "scripts\pas169_launch_readiness_check.py", line 463>:
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

Disassembly of <code object check_docs_required_doctrine at 0x0000018C17D8A4D0, file "scripts\pas169_launch_readiness_check.py", line 463>:
  --            MAKE_CELL                8 (lower)

 463            RESUME                   0

 464            BUILD_LIST               0
                STORE_FAST               1 (out)

 465            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('docs')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('pas169_crypto_roundtrip_launch_gate.md')
                BINARY_OP               11 (/)
                STORE_FAST               2 (doc)

 466            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (doc)
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
                STORE_DEREF              8 (lower)

 468            LOAD_CONST              13 ((('purpose', ('purpose',)), ('pas168', ('pas168',)), ('crypto-import', ('cryptography import', 'real crypto', 'actually installed')), ('local-run', ('local',)), ('ci-prod-run', ('ci', 'production', '--use-env-key')), ('no-key-material', ('no key material', 'never prints', 'never echo')), ('no-db-writes', ('no db writes', 'no database', 'read-only', 'no db write')), ('no-migration', ('no migration', 'no migration execution', 'does not run a migration')), ('launch-checklist', ('launch checklist', 'pre-launch', 'checklist')), ('limitations', ('limitation', 'limitations')), ('not-built', ('intentionally not built', 'deliberately not', 'what is intentionally'))))
                STORE_FAST               4 (required_phrases)

 488            LOAD_FAST_BORROW         4 (required_phrases)
                GET_ITER
        L2:     FOR_ITER               146 (to L12)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   86 (name, phrases)

 489            LOAD_GLOBAL              6 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         8 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18026130, file "scripts\pas169_launch_readiness_check.py", line 489>)
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
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18026130, file "scripts\pas169_launch_readiness_check.py", line 489>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         6 (phrases)
                GET_ITER
                CALL                     0
                CALL                     1
        L7:     STORE_FAST               7 (present)

 490            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 491            LOAD_CONST               6 ('docs:phrase:')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 492            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               8 ('FAIL')

 493    L9:     LOAD_CONST               9 ('Doc carries clause: ')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 494            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 496            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L10)
                NOT_TAKEN

 495            LOAD_CONST              10 ('expected one of: ')
                LOAD_CONST              11 (' | ')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_FAST_BORROW         6 (phrases)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L11)

 496   L10:     LOAD_CONST               2 ('')

 490   L11:     LOAD_CONST              12 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          148 (to L2)

 488   L12:     END_FOR
                POP_ITER

 498            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18026130, file "scripts\pas169_launch_readiness_check.py", line 489>:
  --           COPY_FREE_VARS           1

 489           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA22E0, file "scripts\pas169_launch_readiness_check.py", line 501>:
501           RESUME                   0
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

Disassembly of <code object check_self_no_env_or_db at 0x0000018C17D88C40, file "scripts\pas169_launch_readiness_check.py", line 501>:
501            RESUME                   0

502            BUILD_LIST               0
               STORE_FAST               1 (out)

503            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_GLOBAL              2 (__file__)
               CALL                     1
               LOAD_ATTR                5 (resolve + NULL|self)
               CALL                     0
               STORE_FAST               2 (self_path)

504            LOAD_GLOBAL              7 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (self_path)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L1:     STORE_FAST               3 (src)

508            LOAD_GLOBAL              9 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               4 (executable)

509            BUILD_LIST               0
               STORE_FAST               5 (bad)

510            LOAD_FAST_BORROW         4 (executable)
               LOAD_ATTR               11 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L2:     FOR_ITER               199 (to L9)
               STORE_FAST               6 (raw_line)

511            LOAD_FAST_BORROW         6 (raw_line)
               LOAD_ATTR               13 (strip + NULL|self)
               CALL                     0
               STORE_FAST               7 (stripped)

512            LOAD_FAST_BORROW         7 (stripped)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN

513            JUMP_BACKWARD           29 (to L2)

514    L3:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              15 (('import dotenv', 'from dotenv'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L4)
               NOT_TAKEN

515            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               1 ('dotenv import')
               CALL                     1
               POP_TOP

516    L4:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              16 (('import supabase', 'from supabase'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L5)
               NOT_TAKEN

517            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               2 ('supabase import')
               CALL                     1
               POP_TOP

518    L5:     LOAD_CONST               3 ('load_dotenv()')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       18 (to L6)
               NOT_TAKEN

519            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               4 ('load_dotenv() call')
               CALL                     1
               POP_TOP

520    L6:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              17 (('os.environ[', 'getenv('))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L7)
               NOT_TAKEN

521            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               5 ('environ read')
               CALL                     1
               POP_TOP

522    L7:     LOAD_CONST               6 ('get_supabase')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD          182 (to L2)

523    L8:     LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               7 ('supabase client call')
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          201 (to L2)

510    L9:     END_FOR
               POP_ITER

524            LOAD_FAST                1 (out)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_GLOBAL             19 (_check + NULL)

525            LOAD_CONST               8 ('self_check:no_env_or_db')

526            LOAD_FAST_BORROW         5 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST               9 ('FAIL')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST              10 ('PASS')

527   L11:     LOAD_CONST              11 ('PAS169 launch checker never reads .env or touches DB')

528            LOAD_GLOBAL             20 (SEVERITY_BLOCK)

530            LOAD_FAST_BORROW         5 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L12)
               NOT_TAKEN

529            LOAD_CONST              12 ('disqualifying code-line patterns: ')
               LOAD_CONST              13 (', ')
               LOAD_ATTR               23 (join + NULL|self)
               LOAD_FAST_BORROW         5 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L13)

530   L12:     LOAD_CONST               0 ('')

524   L13:     LOAD_CONST              14 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

532            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA24C0, file "scripts\pas169_launch_readiness_check.py", line 539>:
539           RESUME                   0
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

Disassembly of <code object _aggregate at 0x0000018C17EC4280, file "scripts\pas169_launch_readiness_check.py", line 539>:
 539            RESUME                   0

 541            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 540            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2

 541    L2:     FOR_ITER                49 (to L7)
                STORE_FAST               1 (c)

 542            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 541    L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L2)

 542    L4:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              2 (SEVERITY_BLOCK)
                COMPARE_OP              88 (bool(==))

 541    L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L2)
        L6:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L2)
        L7:     END_FOR
                POP_ITER

 540    L8:     STORE_FAST               2 (blockers)
                STORE_FAST               1 (c)

 545            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 544            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L9:     BUILD_LIST               0
                SWAP                     2

 545   L10:     FOR_ITER                49 (to L15)
                STORE_FAST               1 (c)

 546            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 545   L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L10)

 546   L12:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              4 (SEVERITY_INFO)
                COMPARE_OP              88 (bool(==))

 545   L13:     POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L10)
       L14:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L10)
       L15:     END_FOR
                POP_ITER

 544   L16:     STORE_FAST               3 (info)
                STORE_FAST               1 (c)

 549            LOAD_CONST               3 ('verdict')
                LOAD_FAST_BORROW         2 (blockers)
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L17)
                NOT_TAKEN
                LOAD_GLOBAL              6 (VERDICT_NOT_READY)
                JUMP_FORWARD             5 (to L18)
       L17:     LOAD_GLOBAL              8 (VERDICT_READY)

 550   L18:     LOAD_CONST               4 ('blockers')
                LOAD_FAST_BORROW         2 (blockers)

 551            LOAD_CONST               5 ('info')
                LOAD_FAST_BORROW         3 (info)

 548            BUILD_MAP                3
                RETURN_VALUE

  --   L19:     SWAP                     2
                POP_TOP

 540            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0

  --   L20:     SWAP                     2
                POP_TOP

 544            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L19 [2]
  L4 to L5 -> L19 [2]
  L6 to L8 -> L19 [2]
  L9 to L11 -> L20 [2]
  L12 to L13 -> L20 [2]
  L14 to L16 -> L20 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA25B0, file "scripts\pas169_launch_readiness_check.py", line 555>:
555           RESUME                   0
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

Disassembly of <code object _operator_actions at 0x0000018C18048730, file "scripts\pas169_launch_readiness_check.py", line 555>:
555           RESUME                   0

556           BUILD_LIST               0
              STORE_FAST               1 (out)

557           LOAD_FAST_BORROW         0 (checks)
              GET_ITER
      L1:     FOR_ITER               109 (to L5)
              STORE_FAST               2 (c)

558           LOAD_FAST_BORROW         2 (c)
              LOAD_CONST               0 ('status')
              BINARY_OP               26 ([])
              LOAD_CONST               1 ('FAIL')
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

559           JUMP_BACKWARD           19 (to L1)

560   L2:     LOAD_FAST_BORROW         2 (c)
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

561           LOAD_FAST                1 (out)
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

557   L5:     END_FOR
              POP_ITER

562           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "scripts\pas169_launch_readiness_check.py", line 565>:
565           RESUME                   0
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

Disassembly of <code object evaluate at 0x0000018C17EA77F0, file "scripts\pas169_launch_readiness_check.py", line 565>:
565           RESUME                   0

566           BUILD_LIST               0
              STORE_FAST               1 (checks)

567           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              3 (check_files_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

568           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              5 (check_prior_phases_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

569           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              7 (check_memory_review_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

570           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              9 (check_no_forbidden_future_files + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

571           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             11 (check_requirements + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

572           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             13 (check_crypto_importable + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

573           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             15 (check_route_uses_secret_helper + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

574           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             17 (check_no_forbidden_imports + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

575           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             19 (check_no_inbox_scanning + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

576           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             21 (check_no_migration_execution + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

577           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             23 (check_docs_required_doctrine + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

578           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             25 (check_self_no_env_or_db + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

580           LOAD_GLOBAL             27 (_aggregate + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1
              STORE_FAST               2 (agg)

582           LOAD_CONST               0 ('phase')
              LOAD_CONST               1 ('PAS169')

583           LOAD_CONST               2 ('generated_at')
              LOAD_GLOBAL             29 (_now_iso + NULL)
              CALL                     0

584           LOAD_CONST               3 ('verdict')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])

585           LOAD_CONST               4 ('ready')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])
              LOAD_GLOBAL             30 (VERDICT_READY)
              COMPARE_OP              72 (==)

586           LOAD_CONST               5 ('blocker_count')
              LOAD_GLOBAL             33 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               6 ('blockers')
              BINARY_OP               26 ([])
              CALL                     1

587           LOAD_CONST               7 ('info_count')
              LOAD_GLOBAL             33 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               8 ('info')
              BINARY_OP               26 ([])
              CALL                     1

588           LOAD_CONST               9 ('check_count')
              LOAD_GLOBAL             33 (len + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

589           LOAD_CONST              10 ('pass_count')
              LOAD_GLOBAL             35 (sum + NULL)
              LOAD_CONST              11 (<code object <genexpr> at 0x0000018C18053090, file "scripts\pas169_launch_readiness_check.py", line 589>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

590           LOAD_CONST              12 ('fail_count')
              LOAD_GLOBAL             35 (sum + NULL)
              LOAD_CONST              13 (<code object <genexpr> at 0x0000018C18053750, file "scripts\pas169_launch_readiness_check.py", line 590>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

591           LOAD_CONST              14 ('checks')
              LOAD_FAST_BORROW         1 (checks)

592           LOAD_CONST              15 ('operator_actions')
              LOAD_GLOBAL             37 (_operator_actions + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

581           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18053090, file "scripts\pas169_launch_readiness_check.py", line 589>:
 589           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C18053750, file "scripts\pas169_launch_readiness_check.py", line 590>:
 590           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "scripts\pas169_launch_readiness_check.py", line 599>:
599           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C179A7290, file "scripts\pas169_launch_readiness_check.py", line 599>:
599           RESUME                   0

600           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

601           LOAD_CONST               0 ('pas169_launch_readiness_check')

603           LOAD_CONST               1 ('PAS169 — Aggregate launch readiness gate. Verifies cryptography is BOTH declared AND actually importable, PAS160 → PAS168 scripts exist, the email route uses the secret-store helper, no migration execution is wired into the launch scripts, and the PAS169 docs carry the required doctrine. Read-only — never reads .env, never writes to the DB, never runs a migration.')

600           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

614           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

615           LOAD_CONST               3 ('--repo-root')
              LOAD_GLOBAL              6 (_REPO_ROOT_DEFAULT)

616           LOAD_CONST               4 ('Repo root to evaluate (default: parent of this script).')

614           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

618           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

619           LOAD_CONST               6 ('--output')
              LOAD_GLOBAL              8 (REPORT_FILENAME)

620           LOAD_CONST               7 ('Where to write the JSON report (default ./')
              LOAD_GLOBAL              8 (REPORT_FILENAME)
              FORMAT_SIMPLE
              LOAD_CONST               8 (').')
              BUILD_STRING             3

618           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

622           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

623           LOAD_CONST               9 ('--json')
              LOAD_CONST              10 ('store_true')

624           LOAD_CONST              11 ('Emit the report JSON on stdout in addition to the file.')

622           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

626           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

627           LOAD_CONST              13 ('--summary-only')
              LOAD_CONST              10 ('store_true')

628           LOAD_CONST              14 ('Skip writing the full report file; print verdict only.')

626           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

630           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

631           LOAD_CONST              15 ('--strict')
              LOAD_CONST              10 ('store_true')

632           LOAD_CONST              16 ('Exit 1 unless verdict == READY (default policy is the same).')

630           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

634           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "scripts\pas169_launch_readiness_check.py", line 637>:
637           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C17D8CD10, file "scripts\pas169_launch_readiness_check.py", line 637>:
637           RESUME                   0

638           LOAD_GLOBAL              1 (print + NULL)

639           LOAD_CONST               0 ('[PAS169-launch] verdict=')
              LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               1 ('verdict')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               2 (' blockers=')

640           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               3 ('blocker_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' info=')

641           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               5 ('info_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' checks=')

642           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               7 ('check_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' pass=')

643           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               9 ('pass_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              10 (' fail=')

644           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              11 ('fail_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE

639           BUILD_STRING            12

638           CALL                     1
              POP_TOP

646           LOAD_FAST_BORROW         0 (report)
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

647           LOAD_FAST_BORROW         1 (actions)
              TO_BOOL
              POP_JUMP_IF_FALSE       93 (to L5)
              NOT_TAKEN

648           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              13 ('[PAS169-launch] operator actions:')
              CALL                     1
              POP_TOP

649           LOAD_FAST_BORROW         1 (actions)
              LOAD_CONST              14 (slice(None, 25, None))
              BINARY_OP               26 ([])
              GET_ITER
      L2:     FOR_ITER                17 (to L3)
              STORE_FAST               2 (a)

650           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              15 ('  - ')
              LOAD_FAST_BORROW         2 (a)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L2)

649   L3:     END_FOR
              POP_ITER

651           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         1 (actions)
              CALL                     1
              LOAD_SMALL_INT          25
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       34 (to L4)
              NOT_TAKEN

652           LOAD_GLOBAL              1 (print + NULL)
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

651   L4:     LOAD_CONST              18 (None)
              RETURN_VALUE

647   L5:     LOAD_CONST              18 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025130, file "scripts\pas169_launch_readiness_check.py", line 655>:
655           RESUME                   0
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

Disassembly of <code object _write_report at 0x0000018C180FC030, file "scripts\pas169_launch_readiness_check.py", line 655>:
 655           RESUME                   0

 656           NOP

 657   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

 658           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

 659           LOAD_CONST               3 ('utf-8')

 657           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 661           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

 662   L4:     LOAD_GLOBAL             11 (print + NULL)

 663           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

 664           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

 663           BUILD_STRING             4

 665           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

 662           LOAD_CONST               7 (('file',))
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

 661   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "scripts\pas169_launch_readiness_check.py", line 669>:
669           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17D88FF0, file "scripts\pas169_launch_readiness_check.py", line 669>:
 669            RESUME                   0

 670            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 671            NOP

 672    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 676    L2:     LOAD_GLOBAL             10 (os)
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

 677            LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               21 (isdir + NULL|self)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L4)
                NOT_TAKEN

 678            LOAD_GLOBAL             23 (print + NULL)

 679            LOAD_CONST               2 ('error: --repo-root not a directory: ')
                LOAD_FAST                4 (repo_root)
                FORMAT_SIMPLE
                BUILD_STRING             2

 680            LOAD_GLOBAL             24 (sys)
                LOAD_ATTR               26 (stderr)

 678            LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

 682            LOAD_SMALL_INT           2
                RETURN_VALUE

 684    L4:     LOAD_GLOBAL             29 (evaluate + NULL)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                STORE_FAST               5 (report)

 686            LOAD_FAST                2 (args)
                LOAD_ATTR               30 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L5)
                NOT_TAKEN

 687            LOAD_GLOBAL             33 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               34 (output)
                LOAD_FAST                5 (report)
                CALL                     2
                POP_TOP

 689    L5:     LOAD_GLOBAL             37 (_print_summary + NULL)
                LOAD_FAST                5 (report)
                CALL                     1
                POP_TOP

 691            LOAD_FAST                2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L6)
                NOT_TAKEN

 692            LOAD_GLOBAL             23 (print + NULL)
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

 694    L6:     LOAD_FAST                5 (report)
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

 673            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L17)
                NOT_TAKEN
                STORE_FAST               3 (e)

 674    L9:     LOAD_FAST                3 (e)
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

 673   L17:     RERAISE                  0

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
