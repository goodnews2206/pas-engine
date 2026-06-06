# scripts_readiness/pas168_email_secret_rotation_readiness_check

- **pyc:** `scripts\__pycache__\pas168_email_secret_rotation_readiness_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/pas168_email_secret_rotation_readiness_check.py`
- **co_filename (from bytecode):** `scripts\pas168_email_secret_rotation_readiness_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS168 — Real crypto dependency + operator secret rotation
readiness gate.

Deterministic, non-mutating evaluator for "is the PAS168
rotation tool wired correctly, the kid-aware crypto seam
real, and PAS164 / PAS165 / PAS166 / PAS167 doctrine
preserved?".

Walks the repo and verifies:

  * ``cryptography>=42`` is declared in ``requirements.txt``.
  * ``app/services/ingestion/email_forwarder_secret_store.py``
    supports kid-aware encryption / decryption.
  * The secret store has no fake-encryption path — it still
    returns ``crypto_unavailable`` when the import fails.
  * ``scripts/rotate_email_forwarder_secret.py`` exists, is
    dry-run by default, requires ``--execute`` for any write,
    and clamps ``--limit`` to ``[1, 1000]``.
  * The rotation script's executable surface never references
    the plaintext, the ciphertext, or the key material under
    a string-stripped scan.
  * The rotation script does NOT delete the plaintext column.
  * Event contract registers the three new rotation event
    types.
  * The route's event-payload allow-list excludes the PAS168
    forbidden keys (key / key_material) and the prior-phase
    forbidden keys.
  * No Gmail / Google / IMAP / POP3 / inbox-scan tokens.
  * No embedding / vector / vendor (other than cryptography)
    imports.
  * Memory Review UI files are intact.
  * Prior-phase readiness scripts (PAS160 / PAS161 / PAS162 /
    PAS163 / PAS164 / PAS165 / PAS166 / PAS167) still exist.
  * Supports ``--summary-only`` and ``--json``.
  * Exits 0 ready, 1 blockers, 2 bad args.
  * Never reads .env.
  * Never touches production data.

Usage:
  python scripts/pas168_email_secret_rotation_readiness_check.py
  python scripts/pas168_email_secret_rotation_readiness_check.py --json
  python scripts/pas168_email_secret_rotation_readiness_check.py --summary-only
  python scripts/pas168_email_secret_rotation_readiness_check.py --strict

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

`__annotate__`, `_aggregate`, `_build_parser`, `_check`, `_now_iso`, `_operator_actions`, `_print_summary`, `_read_text`, `_strip_python_comments_and_strings`, `_write_report`, `check_docs_required_doctrine`, `check_event_contract`, `check_files_present`, `check_memory_review_intact`, `check_no_forbidden_imports`, `check_no_inbox_scanning`, `check_prior_phases_intact`, `check_requirements`, `check_rotation_script`, `check_route_allowlist`, `check_secret_store_kid_aware`, `check_self_no_env_or_vendor`, `evaluate`, `main`

## Env-key candidates

`BLOCK`, `FAIL`, `INFO`, `NOT_READY`, `PAS168`, `PASS`, `READY`

## String constants (redacted where noted)

- '\nPAS168 — Real crypto dependency + operator secret rotation\nreadiness gate.\n\nDeterministic, non-mutating evaluator for "is the PAS168\nrotation tool wired correctly, the kid-aware crypto seam\nreal, and PAS164 / PAS165 / PAS166 / PAS167 doctrine\npreserved?".\n\nWalks the repo and verifies:\n\n  * ``cryptography>=42`` is declared in ``requirements.txt``.\n  * ``app/services/ingestion/email_forwarder_secret_store.py``\n    supports kid-aware encryption / decryption.\n  * The secret store has no fake-encryption path — it still\n    returns ``crypto_unavailable`` when the import fails.\n  * ``scripts/rotate_email_forwarder_secret.py`` exists, is\n    dry-run by default, requires ``--execute`` for any write,\n    and clamps ``--limit`` to ``[1, 1000]``.\n  * The rotation script\'s executable surface never references\n    the plaintext, the ciphertext, or the key material under\n    a string-stripped scan.\n  * The rotation script does NOT delete the plaintext column.\n  * Event contract registers the three new rotation event\n    types.\n  * The route\'s event-payload allow-list excludes the PAS168\n    forbidden keys (key / key_material) and the prior-phase\n    forbidden keys.\n  * No Gmail / Google / IMAP / POP3 / inbox-scan tokens.\n  * No embedding / vector / vendor (other than cryptography)\n    imports.\n  * Memory Review UI files are intact.\n  * Prior-phase readiness scripts (PAS160 / PAS161 / PAS162 /\n    PAS163 / PAS164 / PAS165 / PAS166 / PAS167) still exist.\n  * Supports ``--summary-only`` and ``--json``.\n  * Exits 0 ready, 1 blockers, 2 bad args.\n  * Never reads .env.\n  * Never touches production data.\n\nUsage:\n  python scripts/pas168_email_secret_rotation_readiness_check.py\n  python scripts/pas168_email_secret_rotation_readiness_check.py --json\n  python scripts/pas168_email_secret_rotation_readiness_check.py --summary-only\n  python scripts/pas168_email_secret_rotation_readiness_check.py --strict\n\nExit codes:\n    0  — READY  (verdict == READY)\n    1  — NOT_READY\n    2  — bad CLI arguments\n'
- 'utf-8'
- 'READY'
- 'NOT_READY'
- 'BLOCK'
- 'INFO'
- 'severity'
- 'detail'
- 'pas168_email_secret_rotation_readiness_report.json'
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
- 'Required PAS168 file present: '
- 'missing'
- 'prior_phase:'
- 'Prior-phase readiness script intact: '
- 'missing — PAS168 must not delete'
- 'memory_review_file:'
- 'Memory Review file present (PAS168 must not delete): '
- 'PAS168 must not delete Memory Review files'
- 'requirements.txt'
- 'cryptography'
- 'requirements:cryptography'
- 'requirements.txt declares cryptography'
- 'cryptography dependency missing'
- 'app'
- 'services'
- 'ingestion'
- 'email_forwarder_secret_store.py'
- 'store_token:'
- 'Secret-store carries kid-aware token: '
- 'missing token '
- 'from cryptography.fernet import Fernet'
- 'store:imports_fernet'
- 'Secret-store imports Fernet from cryptography'
- 'Fernet import missing'
- 'crypto_unavailable'
- 'store:no_fake_encryption'
- 'Secret-store fails closed when crypto unavailable'
- 'missing crypto_unavailable branch'
- '_ENVELOPE_RE'
- 'wrap_envelope'
- 'store:kid_envelope'
- 'Secret-store implements <kid>:<token> envelope'
- 'missing envelope helper'
- 'scripts'
- 'rotate_email_forwarder_secret.py'
- 'rotation_token:'
- 'Rotation script declares CLI / mode token: '
- '"--execute"'
- 'action="store_true"'
- 'rotation:dry_run_by_default'
- 'Rotation script is dry-run by default'
- '--execute store_true missing'
- '_MIN_LIMIT'
- '_MAX_LIMIT'
- '1000'
- 'rotation:limit_clamp_1_1000'
- 'Rotation script clamps --limit to [1, 1000]'
- 'missing clamp constants'
- '"email_forwarder_secret":'
- "'email_forwarder_secret':"
- 'rotation:no_plaintext_overwrite'
- 'Rotation script does not overwrite the plaintext column'
- "'email_forwarder_secret' written as dict-key"
- 'rotation:no_forbidden_executable_token:'
- 'Rotation executable excludes '
- 'forbidden token '
- ' present'
- 'return 0'
- 'return 1'
- 'return 2'
- 'rotation:exit_codes'
- 'Rotation script declares exit codes 0/1/2'
- 'missing return 0/1/2 branches'
- 'events'
- 'contract.py'
- 'events:'
- 'Event contract registers '
- 'missing event type '
- 'routes'
- 'email_ingestion.py'
- '_EVENT_PAYLOAD_ALLOWED'
- 'route:event_allowlist_excludes:'
- 'Event payload allow-list excludes forbidden key: '
- 'forbidden key '
- ' present in allow-list'
- 'app/services/ingestion/email_forwarder_secret_store.py'
- 'forbidden_import:'
- 'No forbidden imports: '
- 'forbidden import prefixes: '
- 'no_inbox_scan:'
- 'No inbox-scanning tokens: '
- 'inbox-scan tokens present: '
- 'docs'
- 'pas168_email_secret_rotation.md'
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
- 'PAS168 readiness checker never reads .env, calls Supabase, or imports vendor / Google / embedding libs'
- 'disqualifying code-line patterns: '
- 'checks'
- 'verdict'
- 'blockers'
- 'info'
- 'List[str]'
- ' — '
- 'see report'
- 'phase'
- 'PAS168'
- 'generated_at'
- 'ready'
- 'blocker_count'
- 'info_count'
- 'check_count'
- 'pass_count'
- 'fail_count'
- 'operator_actions'
- 'argparse.ArgumentParser'
- 'pas168_email_secret_rotation_readiness_check'
- 'PAS168 — Evaluate the kid-aware crypto seam + operator secret-rotation script for structural correctness, no fake encryption, no Gmail / inbox / vendor / embedding imports, and no plaintext deletion in this phase. Read-only. Does not touch Supabase, .env, or tenant data.'
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
- '[PAS168] verdict='
- ' blockers='
- ' info='
- ' checks='
- ' pass='
- ' fail='
- '[PAS168] operator actions:'
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

   1           LOAD_CONST               0 ('\nPAS168 — Real crypto dependency + operator secret rotation\nreadiness gate.\n\nDeterministic, non-mutating evaluator for "is the PAS168\nrotation tool wired correctly, the kid-aware crypto seam\nreal, and PAS164 / PAS165 / PAS166 / PAS167 doctrine\npreserved?".\n\nWalks the repo and verifies:\n\n  * ``cryptography>=42`` is declared in ``requirements.txt``.\n  * ``app/services/ingestion/email_forwarder_secret_store.py``\n    supports kid-aware encryption / decryption.\n  * The secret store has no fake-encryption path — it still\n    returns ``crypto_unavailable`` when the import fails.\n  * ``scripts/rotate_email_forwarder_secret.py`` exists, is\n    dry-run by default, requires ``--execute`` for any write,\n    and clamps ``--limit`` to ``[1, 1000]``.\n  * The rotation script\'s executable surface never references\n    the plaintext, the ciphertext, or the key material under\n    a string-stripped scan.\n  * The rotation script does NOT delete the plaintext column.\n  * Event contract registers the three new rotation event\n    types.\n  * The route\'s event-payload allow-list excludes the PAS168\n    forbidden keys (key / key_material) and the prior-phase\n    forbidden keys.\n  * No Gmail / Google / IMAP / POP3 / inbox-scan tokens.\n  * No embedding / vector / vendor (other than cryptography)\n    imports.\n  * Memory Review UI files are intact.\n  * Prior-phase readiness scripts (PAS160 / PAS161 / PAS162 /\n    PAS163 / PAS164 / PAS165 / PAS166 / PAS167) still exist.\n  * Supports ``--summary-only`` and ``--json``.\n  * Exits 0 ready, 1 blockers, 2 bad args.\n  * Never reads .env.\n  * Never touches production data.\n\nUsage:\n  python scripts/pas168_email_secret_rotation_readiness_check.py\n  python scripts/pas168_email_secret_rotation_readiness_check.py --json\n  python scripts/pas168_email_secret_rotation_readiness_check.py --summary-only\n  python scripts/pas168_email_secret_rotation_readiness_check.py --strict\n\nExit codes:\n    0  — READY  (verdict == READY)\n    1  — NOT_READY\n    2  — bad CLI arguments\n')
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

  86           LOAD_CONST              64 (('requirements.txt', 'app/services/ingestion/email_forwarder_secret_store.py', 'scripts/rotate_email_forwarder_secret.py', 'app/routes/email_ingestion.py', 'scripts/pas168_email_secret_rotation_readiness_check.py', 'docs/pas168_email_secret_rotation.md', 'tests/mvp/test_pas168_email_secret_rotation.py'))
               STORE_NAME              29 (REQUIRED_FILES)

  96           LOAD_CONST              65 (('scripts/pas160_mvp_sequence_check.py', 'scripts/pas161_lead_ingestion_readiness_check.py', 'scripts/pas162_pending_calls_readiness_check.py', 'scripts/pas163_candidate_pipeline_readiness_check.py', 'scripts/pas164_email_ingestion_readiness_check.py', 'scripts/pas165_email_auth_dedupe_readiness_check.py', 'scripts/pas166_email_dedupe_policy_readiness_check.py', 'scripts/pas167_email_secret_reaper_readiness_check.py'))
               STORE_NAME              30 (PRIOR_PHASE_FILES)

 107           LOAD_CONST              66 (('app/services/memory/review.py', 'app/services/memory/review_stats.py', 'app/services/memory/review_export.py', 'app/services/memory/review_actors.py', 'app/services/memory/review_alerts.py', 'app/services/memory/operator_console.py'))
               STORE_NAME              31 (MEMORY_REVIEW_FILES)

 120           LOAD_CONST              67 (('_resolve_active_kid', '_key_material_for_kid', '_wrap_envelope', '_split_envelope', 'PAS_EMAIL_FORWARDER_SECRET_ACTIVE_KID', 'PAS_EMAIL_FORWARDER_SECRET_FERNET_KEY_', 'missing_active_kid', 'crypto_unavailable', 'crypto_key_missing', 'forwarder_secret_decrypt_failed', 'plaintext_forwarder_secret_fallback'))
               STORE_NAME              32 (REQUIRED_STORE_TOKENS)

 135           LOAD_CONST              68 (('--execute', '--brokerage-id', '--limit', '--kid', '--json', 'dry-run', 'execute', 'rotated_count', 'skipped_count', 'failed_count'))
               STORE_NAME              33 (REQUIRED_ROTATION_TOKENS)

 149           LOAD_CONST              69 (('email.forwarder.secret.rotation_dry_run', 'email.forwarder.secret.rotated', 'email.forwarder.secret.rotation_failed'))
               STORE_NAME              34 (REQUIRED_EVENT_TYPES)

 156           LOAD_CONST              70 (('secret', 'encrypted_secret', 'key', 'key_material', 'signature', 'dedupe_key', 'phone', 'email', 'name', 'subject', 'sender', 'body', 'raw_email', 'raw_body', 'property_address', 'notes', 'transcript'))
               STORE_NAME              35 (FORBIDDEN_EVENT_PAYLOAD_KEYS)

 177           LOAD_CONST              71 (('import googleapiclient', 'from googleapiclient', 'import google.oauth2', 'from google.oauth2', 'from google.auth', 'import google.auth', 'from google_auth_oauthlib', 'import composio', 'from composio', 'import trustclaw', 'from trustclaw', 'import openai', 'from openai', 'import anthropic', 'from anthropic', 'import numpy', 'import faiss', 'import pgvector', 'from pgvector', 'from openai import embeddings', 'from openai.embeddings', 'from app.services.memory', 'import app.services.memory', 'import imaplib', 'from imaplib', 'import poplib', 'from poplib'))
               STORE_NAME              36 (FORBIDDEN_IMPORT_LINE_PREFIXES)

 207           LOAD_CONST              72 (('imaplib', 'poplib', 'fetch_inbox', 'gmail_oauth', 'gmail_token', 'users().messages'))
               STORE_NAME              37 (FORBIDDEN_INBOX_TOKENS)

 221           LOAD_CONST              73 (('key_material',))
               STORE_NAME              38 (ROTATION_FORBIDDEN_EXECUTABLE_TOKENS)

 235           LOAD_CONST              13 ('severity')

 237           LOAD_NAME               27 (SEVERITY_BLOCK)

 235           LOAD_CONST              14 ('detail')

 237           LOAD_CONST              15 ('')

 235           BUILD_MAP                2
               LOAD_CONST              16 (<code object __annotate__ at 0x0000018C18025A30, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 235>)
               MAKE_FUNCTION
               LOAD_CONST              17 (<code object _check at 0x0000018C17FA34B0, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 235>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              39 (_check)

 248           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA3B40, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 248>)
               MAKE_FUNCTION
               LOAD_CONST              19 (<code object _now_iso at 0x0000018C18038CB0, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 248>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              40 (_now_iso)

 252           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA2F10, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 252>)
               MAKE_FUNCTION
               LOAD_CONST              21 (<code object _read_text at 0x0000018C180531B0, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 252>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              41 (_read_text)

 259           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA2970, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 259>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object _strip_python_comments_and_strings at 0x0000018C17E59E70, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 259>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              42 (_strip_python_comments_and_strings)

 298           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA33C0, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 298>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object check_files_present at 0x0000018C180608A0, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 298>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              43 (check_files_present)

 312           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA35A0, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 312>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object check_prior_phases_intact at 0x0000018C18060A50, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 312>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              44 (check_prior_phases_intact)

 326           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA3D20, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 326>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object check_memory_review_intact at 0x0000018C18060C00, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 326>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              45 (check_memory_review_intact)

 340           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA1D40, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 340>)
               MAKE_FUNCTION
               LOAD_CONST              31 (<code object check_requirements at 0x0000018C17ECF940, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 340>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              46 (check_requirements)

 360           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA2880, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 360>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object check_secret_store_kid_aware at 0x0000018C17EDA280, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 360>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              47 (check_secret_store_kid_aware)

 405           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA2B50, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 405>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object check_rotation_script at 0x0000018C181A0B80, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 405>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              48 (check_rotation_script)

 488           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C17FA32D0, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 488>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object check_event_contract at 0x0000018C17FEDA30, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 488>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              49 (check_event_contract)

 504           LOAD_CONST              38 (<code object __annotate__ at 0x0000018C17FA3780, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 504>)
               MAKE_FUNCTION
               LOAD_CONST              39 (<code object check_route_allowlist at 0x0000018C17ECEB60, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 504>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              50 (check_route_allowlist)

 524           LOAD_CONST              40 (<code object __annotate__ at 0x0000018C17FA2E20, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 524>)
               MAKE_FUNCTION
               LOAD_CONST              41 (<code object check_no_forbidden_imports at 0x0000018C17D8A270, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 524>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              51 (check_no_forbidden_imports)

 551           LOAD_CONST              42 (<code object __annotate__ at 0x0000018C17FA21F0, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 551>)
               MAKE_FUNCTION
               LOAD_CONST              43 (<code object check_no_inbox_scanning at 0x0000018C17CC2960, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 551>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              52 (check_no_inbox_scanning)

 576           LOAD_CONST              44 (<code object __annotate__ at 0x0000018C17FA26A0, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 576>)
               MAKE_FUNCTION
               LOAD_CONST              45 (<code object check_docs_required_doctrine at 0x0000018C17F74430, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 576>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              53 (check_docs_required_doctrine)

 617           LOAD_CONST              46 (<code object __annotate__ at 0x0000018C17FA2790, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 617>)
               MAKE_FUNCTION
               LOAD_CONST              47 (<code object check_self_no_env_or_vendor at 0x0000018C17E93990, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 617>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              54 (check_self_no_env_or_vendor)

 667           LOAD_CONST              48 (<code object __annotate__ at 0x0000018C180FC030, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 667>)
               MAKE_FUNCTION
               LOAD_CONST              49 (<code object _aggregate at 0x0000018C17EC46C0, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 667>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              55 (_aggregate)

 683           LOAD_CONST              50 (<code object __annotate__ at 0x0000018C180FC6C0, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 683>)
               MAKE_FUNCTION
               LOAD_CONST              51 (<code object _operator_actions at 0x0000018C180483B0, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 683>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              56 (_operator_actions)

 693           LOAD_CONST              52 (<code object __annotate__ at 0x0000018C180FC7B0, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 693>)
               MAKE_FUNCTION
               LOAD_CONST              53 (<code object evaluate at 0x0000018C17E93E10, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 693>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              57 (evaluate)

 724           LOAD_CONST              54 ('pas168_email_secret_rotation_readiness_report.json')
               STORE_NAME              58 (REPORT_FILENAME)

 727           LOAD_CONST              55 (<code object __annotate__ at 0x0000018C180FC8A0, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 727>)
               MAKE_FUNCTION
               LOAD_CONST              56 (<code object _build_parser at 0x0000018C1801CDC0, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 727>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              59 (_build_parser)

 762           LOAD_CONST              57 (<code object __annotate__ at 0x0000018C180FC990, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 762>)
               MAKE_FUNCTION
               LOAD_CONST              58 (<code object _print_summary at 0x0000018C17D8C830, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 762>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              60 (_print_summary)

 780           LOAD_CONST              59 (<code object __annotate__ at 0x0000018C18025130, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 780>)
               MAKE_FUNCTION
               LOAD_CONST              60 (<code object _write_report at 0x0000018C179C3C30, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 780>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              61 (_write_report)

 794           LOAD_CONST              74 ((None,))
               LOAD_CONST              61 (<code object __annotate__ at 0x0000018C180FC5D0, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 794>)
               MAKE_FUNCTION
               LOAD_CONST              62 (<code object main at 0x0000018C17F83B80, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 794>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              62 (main)

 822           LOAD_NAME               63 (__name__)
               LOAD_CONST              63 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 823           LOAD_NAME                6 (sys)
               LOAD_ATTR              128 (exit)
               PUSH_NULL
               LOAD_NAME               62 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 822   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  66           LOAD_NAME               18 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  67   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          325 (to L1)

  66   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025A30, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 235>:
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

Disassembly of <code object _check at 0x0000018C17FA34B0, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 235>:
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 248>:
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

Disassembly of <code object _now_iso at 0x0000018C18038CB0, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 248>:
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 252>:
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

Disassembly of <code object _read_text at 0x0000018C180531B0, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 252>:
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 259>:
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

Disassembly of <code object _strip_python_comments_and_strings at 0x0000018C17E59E70, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 259>:
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

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 298>:
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

Disassembly of <code object check_files_present at 0x0000018C180608A0, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 298>:
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

305   L3:     LOAD_CONST               3 ('Required PAS168 file present: ')
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

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 312>:
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

Disassembly of <code object check_prior_phases_intact at 0x0000018C18060A50, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 312>:
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
      L4:     LOAD_CONST               5 ('missing — PAS168 must not delete')

316   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

314   L6:     END_FOR
              POP_ITER

323           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3D20, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 326>:
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

Disassembly of <code object check_memory_review_intact at 0x0000018C18060C00, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 326>:
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

331           LOAD_CONST               0 ('memory_review_file:')
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

333   L3:     LOAD_CONST               3 ('Memory Review file present (PAS168 must not delete): ')
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
      L4:     LOAD_CONST               5 ('PAS168 must not delete Memory Review files')

330   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

328   L6:     END_FOR
              POP_ITER

337           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1D40, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 340>:
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

Disassembly of <code object check_requirements at 0x0000018C17ECF940, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 340>:
340           RESUME                   0

341           BUILD_LIST               0
              STORE_FAST               1 (out)

342           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('requirements.txt')
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
              LOAD_CONST               1 ('')
      L1:     STORE_FAST               3 (src)

344           LOAD_CONST               2 (False)
              STORE_FAST               4 (has_crypto)

345           LOAD_FAST_BORROW         3 (src)
              LOAD_ATTR                5 (splitlines + NULL|self)
              CALL                     0
              GET_ITER
      L2:     FOR_ITER                60 (to L4)
              STORE_FAST               5 (line)

346           LOAD_FAST_BORROW         5 (line)
              LOAD_ATTR                7 (strip + NULL|self)
              CALL                     0
              LOAD_ATTR                9 (lower + NULL|self)
              CALL                     0
              STORE_FAST               6 (stripped)

347           LOAD_FAST_BORROW         6 (stripped)
              LOAD_ATTR               11 (startswith + NULL|self)
              LOAD_CONST               3 ('cryptography')
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           58 (to L2)

348   L3:     LOAD_CONST               4 (True)
              STORE_FAST               4 (has_crypto)

349           POP_TOP
              JUMP_FORWARD             2 (to L5)

345   L4:     END_FOR
              POP_ITER

350   L5:     LOAD_FAST                1 (out)
              LOAD_ATTR               13 (append + NULL|self)
              LOAD_GLOBAL             15 (_check + NULL)

351           LOAD_CONST               5 ('requirements:cryptography')

352           LOAD_FAST_BORROW         4 (has_crypto)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L6)
              NOT_TAKEN
              LOAD_CONST               6 ('PASS')
              JUMP_FORWARD             1 (to L7)
      L6:     LOAD_CONST               7 ('FAIL')

353   L7:     LOAD_CONST               8 ('requirements.txt declares cryptography')

354           LOAD_GLOBAL             16 (SEVERITY_BLOCK)

355           LOAD_FAST_BORROW         4 (has_crypto)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L8)
              NOT_TAKEN
              LOAD_CONST               1 ('')
              JUMP_FORWARD             1 (to L9)
      L8:     LOAD_CONST               9 ('cryptography dependency missing')

350   L9:     LOAD_CONST              10 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP

357           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 360>:
360           RESUME                   0
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

Disassembly of <code object check_secret_store_kid_aware at 0x0000018C17EDA280, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 360>:
360            RESUME                   0

361            BUILD_LIST               0
               STORE_FAST               1 (out)

362            LOAD_GLOBAL              1 (Path + NULL)
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

363            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')
       L1:     STORE_FAST               3 (src)

364            LOAD_GLOBAL              4 (REQUIRED_STORE_TOKENS)
               GET_ITER
       L2:     FOR_ITER                71 (to L7)
               STORE_FAST               4 (tok)

365            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

366            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

367            LOAD_CONST               5 ('store_token:')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

368            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               6 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               7 ('FAIL')

369    L4:     LOAD_CONST               8 ('Secret-store carries kid-aware token: ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

370            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

371            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST               9 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

366    L6:     LOAD_CONST              10 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           73 (to L2)

364    L7:     END_FOR
               POP_ITER

375            LOAD_CONST              11 ('from cryptography.fernet import Fernet')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               STORE_FAST               6 (fernet_ref)

376            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

377            LOAD_CONST              12 ('store:imports_fernet')

378            LOAD_FAST_BORROW         6 (fernet_ref)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN
               LOAD_CONST               6 ('PASS')
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST               7 ('FAIL')

379    L9:     LOAD_CONST              13 ('Secret-store imports Fernet from cryptography')

380            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

381            LOAD_FAST_BORROW         6 (fernet_ref)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST              14 ('Fernet import missing')

376   L11:     LOAD_CONST              10 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

383            LOAD_CONST              15 ('crypto_unavailable')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               STORE_FAST               7 (crypto_unavail)

384            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

385            LOAD_CONST              16 ('store:no_fake_encryption')

386            LOAD_FAST_BORROW         7 (crypto_unavail)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L12)
               NOT_TAKEN
               LOAD_CONST               6 ('PASS')
               JUMP_FORWARD             1 (to L13)
      L12:     LOAD_CONST               7 ('FAIL')

387   L13:     LOAD_CONST              17 ('Secret-store fails closed when crypto unavailable')

388            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

389            LOAD_FAST_BORROW         7 (crypto_unavail)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L14)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L15)
      L14:     LOAD_CONST              18 ('missing crypto_unavailable branch')

384   L15:     LOAD_CONST              10 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

393            LOAD_CONST              19 ('_ENVELOPE_RE')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L16)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              20 ('wrap_envelope')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

392   L16:     STORE_FAST               8 (envelope_ref)

395            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

396            LOAD_CONST              21 ('store:kid_envelope')

397            LOAD_FAST_BORROW         8 (envelope_ref)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L17)
               NOT_TAKEN
               LOAD_CONST               6 ('PASS')
               JUMP_FORWARD             1 (to L18)
      L17:     LOAD_CONST               7 ('FAIL')

398   L18:     LOAD_CONST              22 ('Secret-store implements <kid>:<token> envelope')

399            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

400            LOAD_FAST_BORROW         8 (envelope_ref)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L19)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L20)
      L19:     LOAD_CONST              23 ('missing envelope helper')

395   L20:     LOAD_CONST              10 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

402            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 405>:
405           RESUME                   0
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

Disassembly of <code object check_rotation_script at 0x0000018C181A0B80, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 405>:
405            RESUME                   0

406            BUILD_LIST               0
               STORE_FAST               1 (out)

407            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('scripts')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('rotate_email_forwarder_secret.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

408            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               2 ('')
       L1:     STORE_FAST               3 (src)

409            LOAD_GLOBAL              4 (REQUIRED_ROTATION_TOKENS)
               GET_ITER
       L2:     FOR_ITER                71 (to L7)
               STORE_FAST               4 (tok)

410            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

411            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

412            LOAD_CONST               3 ('rotation_token:')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

413            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               4 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               5 ('FAIL')

414    L4:     LOAD_CONST               6 ('Rotation script declares CLI / mode token: ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

415            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

416            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST               7 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

411    L6:     LOAD_CONST               8 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           73 (to L2)

409    L7:     END_FOR
               POP_ITER

420            LOAD_CONST               9 ('"--execute"')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

421            LOAD_CONST              10 ('action="store_true"')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

419    L8:     STORE_FAST               6 (dry_default)

423            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

424            LOAD_CONST              11 ('rotation:dry_run_by_default')

425            LOAD_FAST_BORROW         6 (dry_default)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN
               LOAD_CONST               4 ('PASS')
               JUMP_FORWARD             1 (to L10)
       L9:     LOAD_CONST               5 ('FAIL')

426   L10:     LOAD_CONST              12 ('Rotation script is dry-run by default')

427            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

428            LOAD_FAST_BORROW         6 (dry_default)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST              13 ('--execute store_true missing')

423   L12:     LOAD_CONST               8 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

432            LOAD_CONST              14 ('_MIN_LIMIT')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       19 (to L13)
               NOT_TAKEN
               POP_TOP

433            LOAD_CONST              15 ('_MAX_LIMIT')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

432            COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        6 (to L13)
               NOT_TAKEN
               POP_TOP

434            LOAD_CONST              16 ('1000')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

431   L13:     STORE_FAST               7 (clamp_ok)

436            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

437            LOAD_CONST              17 ('rotation:limit_clamp_1_1000')

438            LOAD_FAST_BORROW         7 (clamp_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L14)
               NOT_TAKEN
               LOAD_CONST               4 ('PASS')
               JUMP_FORWARD             1 (to L15)
      L14:     LOAD_CONST               5 ('FAIL')

439   L15:     LOAD_CONST              18 ('Rotation script clamps --limit to [1, 1000]')

440            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

441            LOAD_FAST_BORROW         7 (clamp_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L16)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L17)
      L16:     LOAD_CONST              19 ('missing clamp constants')

436   L17:     LOAD_CONST               8 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

448            LOAD_GLOBAL             13 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               8 (executable)

450            LOAD_CONST              20 ('"email_forwarder_secret":')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L18)
               NOT_TAKEN
               POP_TOP

451            LOAD_CONST              21 ("'email_forwarder_secret':")
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

449   L18:     STORE_FAST               9 (plaintext_overwrite)

453            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

454            LOAD_CONST              22 ('rotation:no_plaintext_overwrite')

455            LOAD_FAST_BORROW         9 (plaintext_overwrite)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L19)
               NOT_TAKEN
               LOAD_CONST               5 ('FAIL')
               JUMP_FORWARD             1 (to L20)
      L19:     LOAD_CONST               4 ('PASS')

456   L20:     LOAD_CONST              23 ('Rotation script does not overwrite the plaintext column')

457            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

459            LOAD_FAST_BORROW         9 (plaintext_overwrite)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L21)
               NOT_TAKEN

458            LOAD_CONST              24 ("'email_forwarder_secret' written as dict-key")
               JUMP_FORWARD             1 (to L22)

459   L21:     LOAD_CONST               2 ('')

453   L22:     LOAD_CONST               8 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

462            LOAD_GLOBAL             14 (ROTATION_FORBIDDEN_EXECUTABLE_TOKENS)
               GET_ITER
      L23:     FOR_ITER                73 (to L28)
               STORE_FAST               4 (tok)

463            LOAD_FAST_BORROW_LOAD_FAST_BORROW 72 (tok, executable)
               CONTAINS_OP              0 (in)
               STORE_FAST              10 (present)

464            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

465            LOAD_CONST              25 ('rotation:no_forbidden_executable_token:')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

466            LOAD_FAST_BORROW        10 (present)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L24)
               NOT_TAKEN
               LOAD_CONST               5 ('FAIL')
               JUMP_FORWARD             1 (to L25)
      L24:     LOAD_CONST               4 ('PASS')

467   L25:     LOAD_CONST              26 ('Rotation executable excludes ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

468            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

470            LOAD_FAST_BORROW        10 (present)
               TO_BOOL
               POP_JUMP_IF_FALSE        8 (to L26)
               NOT_TAKEN

469            LOAD_CONST              27 ('forbidden token ')
               LOAD_FAST_BORROW         4 (tok)
               CONVERT_VALUE            2 (repr)
               FORMAT_SIMPLE
               LOAD_CONST              28 (' present')
               BUILD_STRING             3
               JUMP_FORWARD             1 (to L27)

470   L26:     LOAD_CONST               2 ('')

464   L27:     LOAD_CONST               8 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           75 (to L23)

462   L28:     END_FOR
               POP_ITER

474            LOAD_CONST              29 ('return 0')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       19 (to L29)
               NOT_TAKEN
               POP_TOP

475            LOAD_CONST              30 ('return 1')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

474            COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        6 (to L29)
               NOT_TAKEN
               POP_TOP

476            LOAD_CONST              31 ('return 2')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

473   L29:     STORE_FAST              11 (has_exit_codes)

478            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

479            LOAD_CONST              32 ('rotation:exit_codes')

480            LOAD_FAST_BORROW        11 (has_exit_codes)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L30)
               NOT_TAKEN
               LOAD_CONST               4 ('PASS')
               JUMP_FORWARD             1 (to L31)
      L30:     LOAD_CONST               5 ('FAIL')

481   L31:     LOAD_CONST              33 ('Rotation script declares exit codes 0/1/2')

482            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

483            LOAD_FAST_BORROW        11 (has_exit_codes)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L32)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L33)
      L32:     LOAD_CONST              34 ('missing return 0/1/2 branches')

478   L33:     LOAD_CONST               8 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

485            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA32D0, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 488>:
488           RESUME                   0
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

Disassembly of <code object check_event_contract at 0x0000018C17FEDA30, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 488>:
488           RESUME                   0

489           BUILD_LIST               0
              STORE_FAST               1 (out)

490           LOAD_GLOBAL              1 (Path + NULL)
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

491           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

492           LOAD_GLOBAL              4 (REQUIRED_EVENT_TYPES)
              GET_ITER
      L2:     FOR_ITER                72 (to L7)
              STORE_FAST               4 (required)

493           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (required, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

494           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

495           LOAD_CONST               5 ('events:')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

496           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               6 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               7 ('FAIL')

497   L4:     LOAD_CONST               8 ('Event contract registers ')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

498           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

499           LOAD_FAST_BORROW         5 (ok)
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

494   L6:     LOAD_CONST              10 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           74 (to L2)

492   L7:     END_FOR
              POP_ITER

501           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 504>:
504           RESUME                   0
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

Disassembly of <code object check_route_allowlist at 0x0000018C17ECEB60, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 504>:
504           RESUME                   0

505           BUILD_LIST               0
              STORE_FAST               1 (out)

506           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('routes')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('email_ingestion.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

507           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               3 ('')
      L1:     STORE_FAST               3 (src)

508           LOAD_FAST_BORROW         3 (src)
              LOAD_ATTR                5 (find + NULL|self)
              LOAD_CONST               4 ('_EVENT_PAYLOAD_ALLOWED')
              CALL                     1
              STORE_FAST               4 (allow_idx)

509           LOAD_FAST_BORROW         4 (allow_idx)
              LOAD_SMALL_INT           0
              COMPARE_OP             188 (bool(>=))
              POP_JUMP_IF_FALSE       12 (to L2)
              NOT_TAKEN
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (src, allow_idx)
              LOAD_FAST_BORROW         4 (allow_idx)
              LOAD_CONST               5 (1024)
              BINARY_OP                0 (+)
              BINARY_SLICE
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               3 ('')
      L3:     STORE_FAST               5 (allow_window)

510           LOAD_GLOBAL              6 (FORBIDDEN_EVENT_PAYLOAD_KEYS)
              GET_ITER
      L4:     FOR_ITER                79 (to L9)
              STORE_FAST               6 (forbidden)

511           LOAD_CONST               6 ('"')
              LOAD_FAST_BORROW         6 (forbidden)
              FORMAT_SIMPLE
              LOAD_CONST               6 ('"')
              BUILD_STRING             3
              STORE_FAST               7 (candidate)

512           LOAD_FAST_BORROW_LOAD_FAST_BORROW 117 (candidate, allow_window)
              CONTAINS_OP              0 (in)
              STORE_FAST               8 (present)

513           LOAD_FAST                1 (out)
              LOAD_ATTR                9 (append + NULL|self)
              LOAD_GLOBAL             11 (_check + NULL)

514           LOAD_CONST               7 ('route:event_allowlist_excludes:')
              LOAD_FAST_BORROW         6 (forbidden)
              FORMAT_SIMPLE
              BUILD_STRING             2

515           LOAD_FAST_BORROW         8 (present)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               8 ('FAIL')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               9 ('PASS')

516   L6:     LOAD_CONST              10 ('Event payload allow-list excludes forbidden key: ')
              LOAD_FAST_BORROW         6 (forbidden)
              FORMAT_SIMPLE
              BUILD_STRING             2

517           LOAD_GLOBAL             12 (SEVERITY_BLOCK)

519           LOAD_FAST_BORROW         8 (present)
              TO_BOOL
              POP_JUMP_IF_FALSE        8 (to L7)
              NOT_TAKEN

518           LOAD_CONST              11 ('forbidden key ')
              LOAD_FAST_BORROW         6 (forbidden)
              CONVERT_VALUE            2 (repr)
              FORMAT_SIMPLE
              LOAD_CONST              12 (' present in allow-list')
              BUILD_STRING             3
              JUMP_FORWARD             1 (to L8)

519   L7:     LOAD_CONST               3 ('')

513   L8:     LOAD_CONST              13 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           81 (to L4)

510   L9:     END_FOR
              POP_ITER

521           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 524>:
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

Disassembly of <code object check_no_forbidden_imports at 0x0000018C17D8A270, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 524>:
524            RESUME                   0

525            BUILD_LIST               0
               STORE_FAST               1 (out)

526            LOAD_CONST               9 (('app/services/ingestion/email_forwarder_secret_store.py', 'scripts/rotate_email_forwarder_secret.py', 'scripts/pas168_email_secret_rotation_readiness_check.py'))
               STORE_FAST               2 (files)

531            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               241 (to L12)
               STORE_FAST               3 (relpath)

532            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

533            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L2:     STORE_FAST               5 (src)

534            BUILD_LIST               0
               STORE_FAST               6 (bad)

535            LOAD_FAST_BORROW         5 (src)
               LOAD_ATTR                5 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L3:     FOR_ITER                74 (to L7)
               STORE_FAST               7 (line)

536            LOAD_FAST_BORROW         7 (line)
               LOAD_ATTR                7 (strip + NULL|self)
               CALL                     0
               STORE_FAST               8 (stripped)

537            LOAD_GLOBAL              8 (FORBIDDEN_IMPORT_LINE_PREFIXES)
               GET_ITER
       L4:     FOR_ITER                45 (to L6)
               STORE_FAST               9 (prefix)

538            LOAD_FAST_BORROW         8 (stripped)
               LOAD_ATTR               11 (startswith + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           28 (to L4)

539    L5:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR               13 (append + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           47 (to L4)

537    L6:     END_FOR
               POP_ITER
               JUMP_BACKWARD           76 (to L3)

535    L7:     END_FOR
               POP_ITER

540            LOAD_FAST                1 (out)
               LOAD_ATTR               13 (append + NULL|self)
               LOAD_GLOBAL             15 (_check + NULL)

541            LOAD_CONST               2 ('forbidden_import:')
               LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR               16 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

542            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST               4 ('PASS')

543    L9:     LOAD_CONST               5 ('No forbidden imports: ')
               LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR               16 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

544            LOAD_GLOBAL             18 (SEVERITY_BLOCK)

546            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L10)
               NOT_TAKEN

545            LOAD_CONST               6 ('forbidden import prefixes: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               21 (join + NULL|self)
               LOAD_FAST_BORROW         6 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L11)

546   L10:     LOAD_CONST               1 ('')

540   L11:     LOAD_CONST               8 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          243 (to L1)

531   L12:     END_FOR
               POP_ITER

548            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 551>:
551           RESUME                   0
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

Disassembly of <code object check_no_inbox_scanning at 0x0000018C17CC2960, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 551>:
551            RESUME                   0

552            BUILD_LIST               0
               STORE_FAST               1 (out)

553            LOAD_CONST               9 (('app/services/ingestion/email_forwarder_secret_store.py', 'scripts/rotate_email_forwarder_secret.py'))
               STORE_FAST               2 (files)

557            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               196 (to L10)
               STORE_FAST               3 (relpath)

558            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

559            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L2:     STORE_FAST               5 (src)

560            LOAD_GLOBAL              5 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         5 (src)
               CALL                     1
               STORE_FAST               6 (executable)

561            BUILD_LIST               0
               STORE_FAST               7 (bad)

562            LOAD_GLOBAL              6 (FORBIDDEN_INBOX_TOKENS)
               GET_ITER
       L3:     FOR_ITER                28 (to L5)
               STORE_FAST               8 (token)

563            LOAD_FAST_BORROW_LOAD_FAST_BORROW 134 (token, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L3)

564    L4:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_FAST_BORROW         8 (token)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L3)

562    L5:     END_FOR
               POP_ITER

565            LOAD_FAST                1 (out)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_GLOBAL             11 (_check + NULL)

566            LOAD_CONST               2 ('no_inbox_scan:')
               LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR               12 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

567            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L6)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L7)
       L6:     LOAD_CONST               4 ('PASS')

568    L7:     LOAD_CONST               5 ('No inbox-scanning tokens: ')
               LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR               12 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

569            LOAD_GLOBAL             14 (SEVERITY_BLOCK)

571            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L8)
               NOT_TAKEN

570            LOAD_CONST               6 ('inbox-scan tokens present: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               17 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L9)

571    L8:     LOAD_CONST               1 ('')

565    L9:     LOAD_CONST               8 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          198 (to L1)

557   L10:     END_FOR
               POP_ITER

573            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA26A0, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 576>:
576           RESUME                   0
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

Disassembly of <code object check_docs_required_doctrine at 0x0000018C17F74430, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 576>:
  --            MAKE_CELL                8 (lower)

 576            RESUME                   0

 577            BUILD_LIST               0
                STORE_FAST               1 (out)

 578            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('docs')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('pas168_email_secret_rotation.md')
                BINARY_OP               11 (/)
                STORE_FAST               2 (doc)

 579            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (doc)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L1:     STORE_FAST               3 (src)

 580            LOAD_FAST_BORROW         3 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_DEREF              8 (lower)

 581            LOAD_CONST              13 ((('purpose', ('purpose',)), ('pas167', ('pas167',)), ('cryptography-dep', ('cryptography>=42', 'cryptography ')), ('kid-model', ('kid model', 'key id', 'key-id')), ('active-kid', ('active kid',)), ('rotation-script', ('rotation script', 'rotation tool')), ('dry-run', ('dry-run', 'dry run')), ('no-plaintext-del', ('no plaintext deletion', 'does not delete plaintext', 'plaintext column is intentionally')), ('no-fake-encrypt', ('no fake encryption', 'fake encryption')), ('event-safety', ('event payload safety', 'event payload', 'allow-list')), ('no-gmail', ('no gmail oauth', 'no gmail')), ('no-inbox', ('no inbox scanning', 'no inbox')), ('not-built', ('intentionally not built', 'deliberately not', 'what is intentionally')), ('brokerage-pilot', ('brokerage pilot', 'real brokerage', 'brokerage pilots')), ('limitations', ('limitation', 'limitations'))))
                STORE_FAST               4 (required_phrases)

 604            LOAD_FAST_BORROW         4 (required_phrases)
                GET_ITER
        L2:     FOR_ITER               146 (to L12)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   86 (name, phrases)

 605            LOAD_GLOBAL              6 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         8 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18026130, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 605>)
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
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18026130, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 605>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         6 (phrases)
                GET_ITER
                CALL                     0
                CALL                     1
        L7:     STORE_FAST               7 (present)

 606            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 607            LOAD_CONST               6 ('docs:phrase:')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 608            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               8 ('FAIL')

 609    L9:     LOAD_CONST               9 ('Doc carries clause: ')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 610            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 612            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L10)
                NOT_TAKEN

 611            LOAD_CONST              10 ('expected one of: ')
                LOAD_CONST              11 (' | ')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_FAST_BORROW         6 (phrases)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L11)

 612   L10:     LOAD_CONST               2 ('')

 606   L11:     LOAD_CONST              12 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          148 (to L2)

 604   L12:     END_FOR
                POP_ITER

 614            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18026130, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 605>:
  --           COPY_FREE_VARS           1

 605           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2790, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 617>:
617           RESUME                   0
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

Disassembly of <code object check_self_no_env_or_vendor at 0x0000018C17E93990, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 617>:
617            RESUME                   0

618            BUILD_LIST               0
               STORE_FAST               1 (out)

619            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_GLOBAL              2 (__file__)
               CALL                     1
               LOAD_ATTR                5 (resolve + NULL|self)
               CALL                     0
               STORE_FAST               2 (self_path)

620            LOAD_GLOBAL              7 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (self_path)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L1:     STORE_FAST               3 (src)

621            BUILD_LIST               0
               STORE_FAST               4 (bad)

622            LOAD_FAST_BORROW         3 (src)
               LOAD_ATTR                9 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L2:     EXTENDED_ARG             1
               FOR_ITER               311 (to L11)
               STORE_FAST               5 (raw_line)

623            LOAD_FAST_BORROW         5 (raw_line)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0
               STORE_FAST               6 (stripped)

624            LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST               1 ('#')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

625            JUMP_BACKWARD           45 (to L2)

626    L3:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              16 (('import dotenv', 'from dotenv'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L4)
               NOT_TAKEN

627            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               2 ('dotenv import')
               CALL                     1
               POP_TOP

628    L4:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              17 (('import supabase', 'from supabase'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L5)
               NOT_TAKEN

629            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               3 ('supabase import')
               CALL                     1
               POP_TOP

630    L5:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              18 (('import composio', 'from composio', 'import trustclaw', 'from trustclaw', 'import openai', 'from openai', 'import anthropic', 'from anthropic', 'import googleapiclient', 'from googleapiclient', 'import google.oauth2', 'from google.oauth2'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L6)
               NOT_TAKEN

638            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               4 ('external-vendor / google import')
               CALL                     1
               POP_TOP

639    L6:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              19 (('import numpy', 'import faiss', 'import pgvector', 'from pgvector', 'from openai import embeddings', 'from openai.embeddings'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L7)
               NOT_TAKEN

645            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               5 ('embedding / vector import')
               CALL                     1
               POP_TOP

646    L7:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST               6 ('load_dotenv()')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        24 (to L8)
               NOT_TAKEN

647            LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               17 (endswith + NULL|self)
               LOAD_CONST               6 ('load_dotenv()')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L9)
               NOT_TAKEN

648    L8:     LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               7 ('load_dotenv() call')
               CALL                     1
               POP_TOP

649    L9:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              20 (('os.environ[', 'os.getenv(', 'getenv('))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         4 (to L10)
               NOT_TAKEN
               EXTENDED_ARG             1
               JUMP_BACKWARD          294 (to L2)

650   L10:     LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               8 ('environ read')
               CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          314 (to L2)

622   L11:     END_FOR
               POP_ITER

651            LOAD_FAST                1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             19 (_check + NULL)

652            LOAD_CONST               9 ('self_check:no_env_or_vendor')

653            LOAD_FAST_BORROW         4 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L12)
               NOT_TAKEN
               LOAD_CONST              10 ('FAIL')
               JUMP_FORWARD             1 (to L13)
      L12:     LOAD_CONST              11 ('PASS')

654   L13:     LOAD_CONST              12 ('PAS168 readiness checker never reads .env, calls Supabase, or imports vendor / Google / embedding libs')

656            LOAD_GLOBAL             20 (SEVERITY_BLOCK)

658            LOAD_FAST_BORROW         4 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L14)
               NOT_TAKEN

657            LOAD_CONST              13 ('disqualifying code-line patterns: ')
               LOAD_CONST              14 (', ')
               LOAD_ATTR               23 (join + NULL|self)
               LOAD_FAST_BORROW         4 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L15)

658   L14:     LOAD_CONST               0 ('')

651   L15:     LOAD_CONST              15 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

660            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180FC030, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 667>:
667           RESUME                   0
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

Disassembly of <code object _aggregate at 0x0000018C17EC46C0, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 667>:
 667            RESUME                   0

 669            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 668            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2

 669    L2:     FOR_ITER                49 (to L7)
                STORE_FAST               1 (c)

 670            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 669    L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L2)

 670    L4:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              2 (SEVERITY_BLOCK)
                COMPARE_OP              88 (bool(==))

 669    L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L2)
        L6:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L2)
        L7:     END_FOR
                POP_ITER

 668    L8:     STORE_FAST               2 (blockers)
                STORE_FAST               1 (c)

 673            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 672            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L9:     BUILD_LIST               0
                SWAP                     2

 673   L10:     FOR_ITER                49 (to L15)
                STORE_FAST               1 (c)

 674            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 673   L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L10)

 674   L12:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              4 (SEVERITY_INFO)
                COMPARE_OP              88 (bool(==))

 673   L13:     POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L10)
       L14:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L10)
       L15:     END_FOR
                POP_ITER

 672   L16:     STORE_FAST               3 (info)
                STORE_FAST               1 (c)

 677            LOAD_CONST               3 ('verdict')
                LOAD_FAST_BORROW         2 (blockers)
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L17)
                NOT_TAKEN
                LOAD_GLOBAL              6 (VERDICT_NOT_READY)
                JUMP_FORWARD             5 (to L18)
       L17:     LOAD_GLOBAL              8 (VERDICT_READY)

 678   L18:     LOAD_CONST               4 ('blockers')
                LOAD_FAST_BORROW         2 (blockers)

 679            LOAD_CONST               5 ('info')
                LOAD_FAST_BORROW         3 (info)

 676            BUILD_MAP                3
                RETURN_VALUE

  --   L19:     SWAP                     2
                POP_TOP

 668            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0

  --   L20:     SWAP                     2
                POP_TOP

 672            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L19 [2]
  L4 to L5 -> L19 [2]
  L6 to L8 -> L19 [2]
  L9 to L11 -> L20 [2]
  L12 to L13 -> L20 [2]
  L14 to L16 -> L20 [2]

Disassembly of <code object __annotate__ at 0x0000018C180FC6C0, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 683>:
683           RESUME                   0
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

Disassembly of <code object _operator_actions at 0x0000018C180483B0, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 683>:
683           RESUME                   0

684           BUILD_LIST               0
              STORE_FAST               1 (out)

685           LOAD_FAST_BORROW         0 (checks)
              GET_ITER
      L1:     FOR_ITER               109 (to L5)
              STORE_FAST               2 (c)

686           LOAD_FAST_BORROW         2 (c)
              LOAD_CONST               0 ('status')
              BINARY_OP               26 ([])
              LOAD_CONST               1 ('FAIL')
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

687           JUMP_BACKWARD           19 (to L1)

688   L2:     LOAD_FAST_BORROW         2 (c)
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

689           LOAD_FAST                1 (out)
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

685   L5:     END_FOR
              POP_ITER

690           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180FC7B0, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 693>:
693           RESUME                   0
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

Disassembly of <code object evaluate at 0x0000018C17E93E10, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 693>:
693           RESUME                   0

694           BUILD_LIST               0
              STORE_FAST               1 (checks)

695           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              3 (check_files_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

696           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              5 (check_prior_phases_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

697           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              7 (check_memory_review_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

698           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              9 (check_requirements + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

699           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             11 (check_secret_store_kid_aware + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

700           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             13 (check_rotation_script + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

701           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             15 (check_event_contract + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

702           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             17 (check_route_allowlist + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

703           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             19 (check_no_forbidden_imports + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

704           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             21 (check_no_inbox_scanning + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

705           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             23 (check_docs_required_doctrine + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

706           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             25 (check_self_no_env_or_vendor + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

708           LOAD_GLOBAL             27 (_aggregate + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1
              STORE_FAST               2 (agg)

710           LOAD_CONST               0 ('phase')
              LOAD_CONST               1 ('PAS168')

711           LOAD_CONST               2 ('generated_at')
              LOAD_GLOBAL             29 (_now_iso + NULL)
              CALL                     0

712           LOAD_CONST               3 ('verdict')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])

713           LOAD_CONST               4 ('ready')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])
              LOAD_GLOBAL             30 (VERDICT_READY)
              COMPARE_OP              72 (==)

714           LOAD_CONST               5 ('blocker_count')
              LOAD_GLOBAL             33 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               6 ('blockers')
              BINARY_OP               26 ([])
              CALL                     1

715           LOAD_CONST               7 ('info_count')
              LOAD_GLOBAL             33 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               8 ('info')
              BINARY_OP               26 ([])
              CALL                     1

716           LOAD_CONST               9 ('check_count')
              LOAD_GLOBAL             33 (len + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

717           LOAD_CONST              10 ('pass_count')
              LOAD_GLOBAL             35 (sum + NULL)
              LOAD_CONST              11 (<code object <genexpr> at 0x0000018C18052F70, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 717>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

718           LOAD_CONST              12 ('fail_count')
              LOAD_GLOBAL             35 (sum + NULL)
              LOAD_CONST              13 (<code object <genexpr> at 0x0000018C18053750, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 718>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

719           LOAD_CONST              14 ('checks')
              LOAD_FAST_BORROW         1 (checks)

720           LOAD_CONST              15 ('operator_actions')
              LOAD_GLOBAL             37 (_operator_actions + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

709           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18052F70, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 717>:
 717           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C18053750, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 718>:
 718           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C180FC8A0, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 727>:
727           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C1801CDC0, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 727>:
727           RESUME                   0

728           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

729           LOAD_CONST               0 ('pas168_email_secret_rotation_readiness_check')

731           LOAD_CONST               1 ('PAS168 — Evaluate the kid-aware crypto seam + operator secret-rotation script for structural correctness, no fake encryption, no Gmail / inbox / vendor / embedding imports, and no plaintext deletion in this phase. Read-only. Does not touch Supabase, .env, or tenant data.')

728           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

739           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

740           LOAD_CONST               3 ('--repo-root')
              LOAD_GLOBAL              6 (_REPO_ROOT_DEFAULT)

741           LOAD_CONST               4 ('Repo root to evaluate (default: parent of this script).')

739           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

743           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

744           LOAD_CONST               6 ('--output')
              LOAD_GLOBAL              8 (REPORT_FILENAME)

745           LOAD_CONST               7 ('Where to write the JSON report (default ./')
              LOAD_GLOBAL              8 (REPORT_FILENAME)
              FORMAT_SIMPLE
              LOAD_CONST               8 (').')
              BUILD_STRING             3

743           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

747           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

748           LOAD_CONST               9 ('--json')
              LOAD_CONST              10 ('store_true')

749           LOAD_CONST              11 ('Emit the report JSON on stdout in addition to the file.')

747           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

751           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

752           LOAD_CONST              13 ('--summary-only')
              LOAD_CONST              10 ('store_true')

753           LOAD_CONST              14 ('Skip writing the full report file; print verdict only.')

751           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

755           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

756           LOAD_CONST              15 ('--strict')
              LOAD_CONST              10 ('store_true')

757           LOAD_CONST              16 ('Exit 1 unless verdict == READY (default policy is the same).')

755           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

759           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180FC990, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 762>:
762           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C17D8C830, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 762>:
762           RESUME                   0

763           LOAD_GLOBAL              1 (print + NULL)

764           LOAD_CONST               0 ('[PAS168] verdict=')
              LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               1 ('verdict')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               2 (' blockers=')

765           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               3 ('blocker_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' info=')

766           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               5 ('info_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' checks=')

767           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               7 ('check_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' pass=')

768           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               9 ('pass_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              10 (' fail=')

769           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              11 ('fail_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE

764           BUILD_STRING            12

763           CALL                     1
              POP_TOP

771           LOAD_FAST_BORROW         0 (report)
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

772           LOAD_FAST_BORROW         1 (actions)
              TO_BOOL
              POP_JUMP_IF_FALSE       93 (to L5)
              NOT_TAKEN

773           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              13 ('[PAS168] operator actions:')
              CALL                     1
              POP_TOP

774           LOAD_FAST_BORROW         1 (actions)
              LOAD_CONST              14 (slice(None, 25, None))
              BINARY_OP               26 ([])
              GET_ITER
      L2:     FOR_ITER                17 (to L3)
              STORE_FAST               2 (a)

775           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              15 ('  - ')
              LOAD_FAST_BORROW         2 (a)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L2)

774   L3:     END_FOR
              POP_ITER

776           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         1 (actions)
              CALL                     1
              LOAD_SMALL_INT          25
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       34 (to L4)
              NOT_TAKEN

777           LOAD_GLOBAL              1 (print + NULL)
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

776   L4:     LOAD_CONST              18 (None)
              RETURN_VALUE

772   L5:     LOAD_CONST              18 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025130, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 780>:
780           RESUME                   0
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

Disassembly of <code object _write_report at 0x0000018C179C3C30, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 780>:
 780           RESUME                   0

 781           NOP

 782   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

 783           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

 784           LOAD_CONST               3 ('utf-8')

 782           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 786           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

 787   L4:     LOAD_GLOBAL             11 (print + NULL)

 788           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

 789           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

 788           BUILD_STRING             4

 790           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

 787           LOAD_CONST               7 (('file',))
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

 786   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C180FC5D0, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 794>:
794           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17F83B80, file "scripts\pas168_email_secret_rotation_readiness_check.py", line 794>:
 794            RESUME                   0

 795            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 796            NOP

 797    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 801    L2:     LOAD_GLOBAL             10 (os)
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

 802            LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               21 (isdir + NULL|self)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L4)
                NOT_TAKEN

 803            LOAD_GLOBAL             23 (print + NULL)

 804            LOAD_CONST               2 ('error: --repo-root not a directory: ')
                LOAD_FAST                4 (repo_root)
                FORMAT_SIMPLE
                BUILD_STRING             2

 805            LOAD_GLOBAL             24 (sys)
                LOAD_ATTR               26 (stderr)

 803            LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

 807            LOAD_SMALL_INT           2
                RETURN_VALUE

 809    L4:     LOAD_GLOBAL             29 (evaluate + NULL)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                STORE_FAST               5 (report)

 811            LOAD_FAST                2 (args)
                LOAD_ATTR               30 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L5)
                NOT_TAKEN

 812            LOAD_GLOBAL             33 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               34 (output)
                LOAD_FAST                5 (report)
                CALL                     2
                POP_TOP

 814    L5:     LOAD_GLOBAL             37 (_print_summary + NULL)
                LOAD_FAST                5 (report)
                CALL                     1
                POP_TOP

 816            LOAD_FAST                2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L6)
                NOT_TAKEN

 817            LOAD_GLOBAL             23 (print + NULL)
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

 819    L6:     LOAD_FAST                5 (report)
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

 798            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L17)
                NOT_TAKEN
                STORE_FAST               3 (e)

 799    L9:     LOAD_FAST                3 (e)
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

 798   L17:     RERAISE                  0

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
