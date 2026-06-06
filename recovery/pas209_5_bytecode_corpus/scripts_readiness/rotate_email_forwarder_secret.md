# scripts_readiness/rotate_email_forwarder_secret

- **pyc:** `scripts\__pycache__\rotate_email_forwarder_secret.cpython-314.pyc`
- **expected source path (absent):** `scripts/rotate_email_forwarder_secret.py`
- **co_filename (from bytecode):** `scripts\rotate_email_forwarder_secret.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS168 — Email forwarder secret rotation (operator-only).

Encrypts brokerages' plaintext ``email_forwarder_secret`` into
the PAS167 ``email_forwarder_secret_encrypted`` column using
the PAS168 kid-aware encryption helper.

Doctrine:

* **Dry-run by default.** No row is written unless
  ``--execute`` is supplied. Dry-run prints structural counts
  only (how many rows are eligible / would skip / already
  encrypted).
* **No secret echo.** The script NEVER prints the plaintext
  secret, NEVER prints the encrypted ciphertext, NEVER prints
  the key material, NEVER prints the kid value beyond the
  structural ``--kid`` filter.
* **No plaintext deletion.** PAS168 is intentionally non-
  destructive. The plaintext column is read but never
  overwritten or cleared. A separate follow-on phase handles
  the destructive cutover once every brokerage row has
  ``migration_status='encrypted'``.
* **No exception escapes.** Every error path produces a
  structural report and a documented exit code.
* **No .env read.** Crypto keys + active kid come from env
  vars (resolved via the secret-store helper); a missing key
  surfaces as a structural ``crypto_key_missing`` per-row
  failure and contributes to the failed count.
* **No Gmail / OAuth / inbox-scan / IMAP / POP3 / vendor /
  embedding import.**

Usage:
  python scripts/rotate_email_forwarder_secret.py
      [--brokerage-id BID]
      [--limit N]              (default 100, clamped 1..1000)
      [--kid KID]              (overrides the env-bound active kid)
      [--json]
      [--execute]              (REQUIRED to write)

Exit codes:
    0  — ok / skipped (DB unavailable, crypto unavailable)
    1  — failed (DB error during a real write)
    2  — bad CLI arguments
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.db.supabase_client`, `app.services.ingestion.email_forwarder_secret_store`, `argparse`, `datetime`, `encrypt_email_forwarder_secret`, `get_supabase`, `json`, `logging`, `os`, `sys`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_build_parser`, `_clamp`, `_get_db_safe`, `_now_iso`, `_print_summary`, `_select_rotation_candidates`, `_update_row_encrypted`, `main`, `rotate`

## Env-key candidates

_none_

## String constants (redacted where noted)

- "\nPAS168 — Email forwarder secret rotation (operator-only).\n\nEncrypts brokerages' plaintext ``email_forwarder_secret`` into\nthe PAS167 ``email_forwarder_secret_encrypted`` column using\nthe PAS168 kid-aware encryption helper.\n\nDoctrine:\n\n* **Dry-run by default.** No row is written unless\n  ``--execute`` is supplied. Dry-run prints structural counts\n  only (how many rows are eligible / would skip / already\n  encrypted).\n* **No secret echo.** The script NEVER prints the plaintext\n  secret, NEVER prints the encrypted ciphertext, NEVER prints\n  the key material, NEVER prints the kid value beyond the\n  structural ``--kid`` filter.\n* **No plaintext deletion.** PAS168 is intentionally non-\n  destructive. The plaintext column is read but never\n  overwritten or cleared. A separate follow-on phase handles\n  the destructive cutover once every brokerage row has\n  ``migration_status='encrypted'``.\n* **No exception escapes.** Every error path produces a\n  structural report and a documented exit code.\n* **No .env read.** Crypto keys + active kid come from env\n  vars (resolved via the secret-store helper); a missing key\n  surfaces as a structural ``crypto_key_missing`` per-row\n  failure and contributes to the failed count.\n* **No Gmail / OAuth / inbox-scan / IMAP / POP3 / vendor /\n  embedding import.**\n\nUsage:\n  python scripts/rotate_email_forwarder_secret.py\n      [--brokerage-id BID]\n      [--limit N]              (default 100, clamped 1..1000)\n      [--kid KID]              (overrides the env-bound active kid)\n      [--json]\n      [--execute]              (REQUIRED to write)\n\nExit codes:\n    0  — ok / skipped (DB unavailable, crypto unavailable)\n    1  — failed (DB error during a real write)\n    2  — bad CLI arguments\n"
- 'utf-8'
- 'pas.scripts.rotate_email_forwarder_secret'
- 'brokerages'
- 'return'
- 'str'
- 'seconds'
- 'value'
- 'Any'
- 'int'
- 'default'
- 'Lazy Supabase client resolver. Returns the client OR\n``None`` on failure. NEVER raises.'
- 'rotate_email_forwarder_secret db client unavailable type='
- 'brokerage_id'
- 'Optional[str]'
- 'limit'
- 'Dict[str, Any]'
- 'Fetch brokerage rows that NEED rotation:\n\n  * have a non-empty plaintext ``email_forwarder_secret``;\n  * AND have NO encrypted column value yet (NULL or empty).\n\nThe query selects ONLY the structural columns the rotation\nscript needs (``id``, plaintext flag, encrypted column,\nmigration_status). The plaintext column value itself is\nfetched only so the encryption helper can transform it —\nit is NEVER printed.\n\nReturns a structural envelope. NEVER raises.\n'
- 'id, email_forwarder_secret, email_forwarder_secret_encrypted, email_forwarder_secret_migration_status'
- 'email_forwarder_secret'
- 'null'
- 'email_forwarder_secret_encrypted'
- 'data'
- 'status'
- 'rows'
- '_select_rotation_candidates db error type='
- 'failed'
- 'error_code'
- 'db_read_failed:'
- 'ciphertext'
- 'kid'
- "Persist the encrypted column + kid + updated_at + flip\nmigration_status to 'encrypted'. NEVER raises. Does NOT\ntouch the plaintext column."
- 'email_forwarder_secret_kid'
- 'email_forwarder_secret_updated_at'
- 'email_forwarder_secret_migration_status'
- 'encrypted'
- 'rotation_update_returned_no_rows'
- '_update_row_encrypted db error type='
- 'db_write_failed:'
- 'execute'
- 'bool'
- 'Main rotation entrypoint. Returns a structural report.\n\nThe report shape (closed)::\n\n    {\n      "status":             "ok" | "skipped" | "failed",\n      "mode":               "dry-run" | "execute",\n      "limit":              int,\n      "kid":                Optional[str],\n      "candidate_count":    int,\n      "rotated_count":      int,\n      "skipped_count":      int,\n      "failed_count":       int,\n      "warnings":           [<structural tokens>],\n      "error_code":         None | "<structural token>",\n    }\n\nThe script NEVER includes the plaintext secret, the\nciphertext, the key material, or any PII field in the\nreport.\n'
- 'durable_email_dedupe_unavailable'
- 'skipped'
- 'mode'
- 'dry-run'
- 'candidate_count'
- 'rotated_count'
- 'skipped_count'
- 'failed_count'
- 'warnings'
- 'db_read_failed'
- 'rotation_encrypt_failed'
- 'key_id'
- 'rotation_update_failed'
- 'rotation_partial_failure'
- 'argparse.ArgumentParser'
- 'rotate_email_forwarder_secret'
- "PAS168 — Operator-only secret rotation tool. Encrypts brokerages' plaintext email_forwarder_secret into the encrypted column using the PAS168 kid-aware helper. Dry-run by default; --execute is required to write. NEVER prints the plaintext secret, the ciphertext, or the key material. NEVER deletes the plaintext column."
- '--brokerage-id'
- 'Optional brokerage scope.'
- '--limit'
- 'Cap on candidates per run. Clamped to ['
- ']. Default '
- '--kid'
- 'Optional kid override. When unset the env-bound active kid (PAS_EMAIL_FORWARDER_SECRET_ACTIVE_KID) is used.'
- '--json'
- 'store_true'
- 'Emit the structural report as JSON on stdout.'
- '--execute'
- 'Actually encrypt + write. Without this flag the rotation runs in dry-run mode and prints counts only.'
- 'report'
- 'None'
- '[PAS168-rotate] status='
- ' mode='
- ' limit='
- ' candidates='
- ' rotated='
- ' skipped='
- ' failed='
- '  warning: '
- '  error_code: '
- 'argv'
- 'Optional[List[str]]'

## Disassembly

```
   0           RESUME                   0

   1           LOAD_CONST               0 ("\nPAS168 — Email forwarder secret rotation (operator-only).\n\nEncrypts brokerages' plaintext ``email_forwarder_secret`` into\nthe PAS167 ``email_forwarder_secret_encrypted`` column using\nthe PAS168 kid-aware encryption helper.\n\nDoctrine:\n\n* **Dry-run by default.** No row is written unless\n  ``--execute`` is supplied. Dry-run prints structural counts\n  only (how many rows are eligible / would skip / already\n  encrypted).\n* **No secret echo.** The script NEVER prints the plaintext\n  secret, NEVER prints the encrypted ciphertext, NEVER prints\n  the key material, NEVER prints the kid value beyond the\n  structural ``--kid`` filter.\n* **No plaintext deletion.** PAS168 is intentionally non-\n  destructive. The plaintext column is read but never\n  overwritten or cleared. A separate follow-on phase handles\n  the destructive cutover once every brokerage row has\n  ``migration_status='encrypted'``.\n* **No exception escapes.** Every error path produces a\n  structural report and a documented exit code.\n* **No .env read.** Crypto keys + active kid come from env\n  vars (resolved via the secret-store helper); a missing key\n  surfaces as a structural ``crypto_key_missing`` per-row\n  failure and contributes to the failed count.\n* **No Gmail / OAuth / inbox-scan / IMAP / POP3 / vendor /\n  embedding import.**\n\nUsage:\n  python scripts/rotate_email_forwarder_secret.py\n      [--brokerage-id BID]\n      [--limit N]              (default 100, clamped 1..1000)\n      [--kid KID]              (overrides the env-bound active kid)\n      [--json]\n      [--execute]              (REQUIRED to write)\n\nExit codes:\n    0  — ok / skipped (DB unavailable, crypto unavailable)\n    1  — failed (DB error during a real write)\n    2  — bad CLI arguments\n")
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
               IMPORT_NAME              5 (logging)
               STORE_NAME               5 (logging)

  51           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (os)
               STORE_NAME               6 (os)

  52           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              7 (sys)
               STORE_NAME               7 (sys)

  53           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              8 (datetime)
               IMPORT_FROM              8 (datetime)
               STORE_NAME               8 (datetime)
               IMPORT_FROM              9 (timezone)
               STORE_NAME               9 (timezone)
               POP_TOP

  54           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Any', 'Dict', 'List', 'Optional'))
               IMPORT_NAME             10 (typing)
               IMPORT_FROM             11 (Any)
               STORE_NAME              11 (Any)
               IMPORT_FROM             12 (Dict)
               STORE_NAME              12 (Dict)
               IMPORT_FROM             13 (List)
               STORE_NAME              13 (List)
               IMPORT_FROM             14 (Optional)
               STORE_NAME              14 (Optional)
               POP_TOP

  57           LOAD_NAME                7 (sys)
               LOAD_ATTR               30 (stdout)
               LOAD_NAME                7 (sys)
               LOAD_ATTR               32 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              17 (_stream)

  58           NOP

  59   L2:     LOAD_NAME               17 (_stream)
               LOAD_ATTR               37 (reconfigure + NULL|self)
               LOAD_CONST               5 ('utf-8')
               LOAD_CONST               6 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  57   L4:     END_FOR
               POP_ITER

  64           LOAD_NAME                7 (sys)
               LOAD_ATTR               40 (path)
               LOAD_ATTR               43 (insert + NULL|self)

  65           LOAD_SMALL_INT           0

  66           LOAD_NAME                6 (os)
               LOAD_ATTR               40 (path)
               LOAD_ATTR               45 (abspath + NULL|self)
               LOAD_NAME                6 (os)
               LOAD_ATTR               40 (path)
               LOAD_ATTR               47 (join + NULL|self)
               LOAD_NAME                6 (os)
               LOAD_ATTR               40 (path)
               LOAD_ATTR               49 (dirname + NULL|self)
               LOAD_NAME               25 (__file__)
               CALL                     1
               LOAD_CONST               7 ('..')
               CALL                     2
               CALL                     1

  64           CALL                     2
               POP_TOP

  69           LOAD_SMALL_INT           0
               LOAD_CONST               8 (('encrypt_email_forwarder_secret',))
               IMPORT_NAME             26 (app.services.ingestion.email_forwarder_secret_store)
               IMPORT_FROM             27 (encrypt_email_forwarder_secret)
               STORE_NAME              27 (encrypt_email_forwarder_secret)
               POP_TOP

  74           LOAD_NAME                5 (logging)
               LOAD_ATTR               56 (getLogger)
               PUSH_NULL
               LOAD_CONST               9 ('pas.scripts.rotate_email_forwarder_secret')
               CALL                     1
               STORE_NAME              29 (logger)

  77           LOAD_CONST              10 ('brokerages')
               STORE_NAME              30 (_TABLE)

  80           LOAD_SMALL_INT         100
               STORE_NAME              31 (_DEFAULT_LIMIT)

  81           LOAD_SMALL_INT           1
               STORE_NAME              32 (_MIN_LIMIT)

  82           LOAD_CONST              11 (1000)
               STORE_NAME              33 (_MAX_LIMIT)

  89           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA31E0, file "scripts\rotate_email_forwarder_secret.py", line 89>)
               MAKE_FUNCTION
               LOAD_CONST              13 (<code object _now_iso at 0x0000018C18038170, file "scripts\rotate_email_forwarder_secret.py", line 89>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              34 (_now_iso)

  93           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C18026130, file "scripts\rotate_email_forwarder_secret.py", line 93>)
               MAKE_FUNCTION
               LOAD_CONST              15 (<code object _clamp at 0x0000018C180396B0, file "scripts\rotate_email_forwarder_secret.py", line 93>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              35 (_clamp)

 105           LOAD_CONST              16 (<code object _get_db_safe at 0x0000018C17FF13B0, file "scripts\rotate_email_forwarder_secret.py", line 105>)
               MAKE_FUNCTION
               STORE_NAME              36 (_get_db_safe)

 123           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C18025130, file "scripts\rotate_email_forwarder_secret.py", line 123>)
               MAKE_FUNCTION
               LOAD_CONST              18 (<code object _select_rotation_candidates at 0x0000018C17F807B0, file "scripts\rotate_email_forwarder_secret.py", line 123>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              37 (_select_rotation_candidates)

 170           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C18024930, file "scripts\rotate_email_forwarder_secret.py", line 170>)
               MAKE_FUNCTION
               LOAD_CONST              20 (<code object _update_row_encrypted at 0x0000018C182E3620, file "scripts\rotate_email_forwarder_secret.py", line 170>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              38 (_update_row_encrypted)

 210           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C18024F30, file "scripts\rotate_email_forwarder_secret.py", line 210>)
               MAKE_FUNCTION
               LOAD_CONST              22 (<code object rotate at 0x0000018C17E053C0, file "scripts\rotate_email_forwarder_secret.py", line 210>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              39 (rotate)

 381           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA3780, file "scripts\rotate_email_forwarder_secret.py", line 381>)
               MAKE_FUNCTION
               LOAD_CONST              24 (<code object _build_parser at 0x0000018C17EC5380, file "scripts\rotate_email_forwarder_secret.py", line 381>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              40 (_build_parser)

 429           LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA2E20, file "scripts\rotate_email_forwarder_secret.py", line 429>)
               MAKE_FUNCTION
               LOAD_CONST              26 (<code object _print_summary at 0x0000018C17ECDD80, file "scripts\rotate_email_forwarder_secret.py", line 429>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              41 (_print_summary)

 446           LOAD_CONST              30 ((None,))
               LOAD_CONST              27 (<code object __annotate__ at 0x0000018C17FA21F0, file "scripts\rotate_email_forwarder_secret.py", line 446>)
               MAKE_FUNCTION
               LOAD_CONST              28 (<code object main at 0x0000018C18645DE0, file "scripts\rotate_email_forwarder_secret.py", line 446>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              42 (main)

 473           LOAD_NAME               43 (__name__)
               LOAD_CONST              29 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 474           LOAD_NAME                7 (sys)
               LOAD_ATTR               88 (exit)
               PUSH_NULL
               LOAD_NAME               42 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 473   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  60           LOAD_NAME               19 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  61   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          260 (to L1)

  60   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "scripts\rotate_email_forwarder_secret.py", line 89>:
 89           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038170, file "scripts\rotate_email_forwarder_secret.py", line 89>:
 89           RESUME                   0

 90           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C18026130, file "scripts\rotate_email_forwarder_secret.py", line 93>:
 93           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('value')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('lo')
              LOAD_CONST               4 ('int')
              LOAD_CONST               5 ('hi')
              LOAD_CONST               4 ('int')
              LOAD_CONST               6 ('default')
              LOAD_CONST               4 ('int')
              LOAD_CONST               7 ('return')
              LOAD_CONST               4 ('int')
              BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _clamp at 0x0000018C180396B0, file "scripts\rotate_email_forwarder_secret.py", line 93>:
  93           RESUME                   0

  94           NOP

  95   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               4 (v)

  98   L2:     LOAD_FAST_LOAD_FAST     65 (v, lo)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

  99           LOAD_FAST                1 (lo)
               RETURN_VALUE

 100   L3:     LOAD_FAST_LOAD_FAST     66 (v, hi)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN

 101           LOAD_FAST                2 (hi)
               RETURN_VALUE

 102   L4:     LOAD_FAST                4 (v)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

  96           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L7)
               NOT_TAKEN
               POP_TOP

  97           LOAD_FAST                3 (default)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

  96   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object _get_db_safe at 0x0000018C17FF13B0, file "scripts\rotate_email_forwarder_secret.py", line 105>:
 105           RESUME                   0

 108           NOP

 109   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('get_supabase',))
               IMPORT_NAME              0 (app.db.supabase_client)
               IMPORT_FROM              1 (get_supabase)
               STORE_FAST               0 (get_supabase)
               POP_TOP

 110           LOAD_FAST_BORROW         0 (get_supabase)
               PUSH_NULL
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 111           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       55 (to L7)
               NOT_TAKEN
               STORE_FAST               1 (e)

 112   L4:     LOAD_GLOBAL              6 (logger)
               LOAD_ATTR                9 (warning + NULL|self)

 113           LOAD_CONST               2 ('rotate_email_forwarder_secret db client unavailable type=')

 114           LOAD_GLOBAL             11 (type + NULL)
               LOAD_FAST                1 (e)
               CALL                     1
               LOAD_ATTR               12 (__name__)
               FORMAT_SIMPLE

 113           BUILD_STRING             2

 112           CALL                     1
               POP_TOP

 116   L5:     POP_EXCEPT
               LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               LOAD_CONST               3 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               RERAISE                  1

 111   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025130, file "scripts\rotate_email_forwarder_secret.py", line 123>:
123           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

126           LOAD_CONST               2 ('Optional[str]')

123           LOAD_CONST               3 ('limit')

127           LOAD_CONST               4 ('int')

123           LOAD_CONST               5 ('return')

128           LOAD_CONST               6 ('Dict[str, Any]')

123           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _select_rotation_candidates at 0x0000018C17F807B0, file "scripts\rotate_email_forwarder_secret.py", line 123>:
 123            RESUME                   0

 142            NOP

 144    L1:     LOAD_FAST_BORROW         0 (db)
                LOAD_ATTR                1 (table + NULL|self)
                LOAD_GLOBAL              2 (_TABLE)
                CALL                     1

 145            LOAD_ATTR                5 (select + NULL|self)

 146            LOAD_CONST               1 ('id, email_forwarder_secret, email_forwarder_secret_encrypted, email_forwarder_secret_migration_status')

 145            CALL                     1

 150            LOAD_ATTR                6 (not_)
                LOAD_ATTR                9 (is_ + NULL|self)
                LOAD_CONST               2 ('email_forwarder_secret')
                LOAD_CONST               3 ('null')
                CALL                     2

 151            LOAD_ATTR                9 (is_ + NULL|self)
                LOAD_CONST               4 ('email_forwarder_secret_encrypted')
                LOAD_CONST               3 ('null')
                CALL                     2

 152            LOAD_ATTR               11 (limit + NULL|self)
                LOAD_FAST_BORROW         2 (limit)
                CALL                     1

 143            STORE_FAST               3 (query)

 154            LOAD_FAST_BORROW         1 (brokerage_id)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L4)
        L2:     NOT_TAKEN

 155    L3:     LOAD_FAST_BORROW         3 (query)
                LOAD_ATTR               13 (eq + NULL|self)
                LOAD_CONST               5 ('id')
                LOAD_FAST_BORROW         1 (brokerage_id)
                CALL                     2
                STORE_FAST               3 (query)

 156    L4:     LOAD_FAST_BORROW         3 (query)
                LOAD_ATTR               15 (execute + NULL|self)
                CALL                     0
                STORE_FAST               4 (result)

 157            LOAD_GLOBAL             17 (list + NULL)
                LOAD_GLOBAL             19 (getattr + NULL)
                LOAD_FAST_BORROW         4 (result)
                LOAD_CONST               6 ('data')
                LOAD_CONST               7 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
        L5:     NOT_TAKEN
        L6:     POP_TOP
                BUILD_LIST               0
        L7:     CALL                     1
                STORE_FAST               5 (rows)

 158            LOAD_CONST               8 ('status')
                LOAD_CONST               9 ('ok')
                LOAD_CONST              10 ('rows')
                LOAD_FAST_BORROW         5 (rows)
                BUILD_MAP                2
        L8:     RETURN_VALUE

  --    L9:     PUSH_EXC_INFO

 159            LOAD_GLOBAL             20 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       84 (to L14)
                NOT_TAKEN
                STORE_FAST               6 (e)

 160   L10:     LOAD_GLOBAL             22 (logger)
                LOAD_ATTR               25 (warning + NULL|self)

 161            LOAD_CONST              11 ('_select_rotation_candidates db error type=')
                LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 160            CALL                     1
                POP_TOP

 164            LOAD_CONST               8 ('status')
                LOAD_CONST              12 ('failed')

 165            LOAD_CONST              10 ('rows')
                BUILD_LIST               0

 166            LOAD_CONST              13 ('error_code')
                LOAD_CONST              14 ('db_read_failed:')
                LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 163            BUILD_MAP                3
       L11:     SWAP                     2
       L12:     POP_EXCEPT
                LOAD_CONST               7 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RETURN_VALUE

  --   L13:     LOAD_CONST               7 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

 159   L14:     RERAISE                  0

  --   L15:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L9 [0]
  L3 to L5 -> L9 [0]
  L6 to L8 -> L9 [0]
  L9 to L10 -> L15 [1] lasti
  L10 to L11 -> L13 [1] lasti
  L11 to L12 -> L15 [1] lasti
  L13 to L15 -> L15 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024930, file "scripts\rotate_email_forwarder_secret.py", line 170>:
170           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

173           LOAD_CONST               2 ('str')

170           LOAD_CONST               3 ('ciphertext')

174           LOAD_CONST               2 ('str')

170           LOAD_CONST               4 ('kid')

175           LOAD_CONST               2 ('str')

170           LOAD_CONST               5 ('return')

176           LOAD_CONST               6 ('Dict[str, Any]')

170           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object _update_row_encrypted at 0x0000018C182E3620, file "scripts\rotate_email_forwarder_secret.py", line 170>:
 170            RESUME                   0

 181            LOAD_CONST               1 ('email_forwarder_secret_encrypted')
                LOAD_FAST_BORROW         2 (ciphertext)

 182            LOAD_CONST               2 ('email_forwarder_secret_kid')
                LOAD_FAST_BORROW         3 (kid)

 183            LOAD_CONST               3 ('email_forwarder_secret_updated_at')
                LOAD_GLOBAL              1 (_now_iso + NULL)
                CALL                     0

 184            LOAD_CONST               4 ('email_forwarder_secret_migration_status')
                LOAD_CONST               5 ('encrypted')

 180            BUILD_MAP                4
                STORE_FAST               4 (patch)

 186            NOP

 188    L1:     LOAD_FAST_BORROW         0 (db)
                LOAD_ATTR                3 (table + NULL|self)
                LOAD_GLOBAL              4 (_TABLE)
                CALL                     1

 189            LOAD_ATTR                7 (update + NULL|self)
                LOAD_FAST_BORROW         4 (patch)
                CALL                     1

 190            LOAD_ATTR                9 (eq + NULL|self)
                LOAD_CONST               6 ('id')
                LOAD_FAST_BORROW         1 (brokerage_id)
                CALL                     2

 191            LOAD_ATTR               11 (execute + NULL|self)
                CALL                     0

 187            STORE_FAST               5 (result)

 193            LOAD_GLOBAL             13 (list + NULL)
                LOAD_GLOBAL             15 (getattr + NULL)
                LOAD_FAST_BORROW         5 (result)
                LOAD_CONST               7 ('data')
                LOAD_CONST               8 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L2)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
        L2:     CALL                     1
                STORE_FAST               6 (rows)

 194            LOAD_FAST_BORROW         6 (rows)
                TO_BOOL
                POP_JUMP_IF_TRUE         7 (to L6)
        L3:     NOT_TAKEN

 196    L4:     LOAD_CONST               9 ('status')
                LOAD_CONST              10 ('failed')

 197            LOAD_CONST              11 ('error_code')
                LOAD_CONST              12 ('rotation_update_returned_no_rows')

 195            BUILD_MAP                2
        L5:     RETURN_VALUE

 199    L6:     LOAD_CONST               9 ('status')
                LOAD_CONST              13 ('ok')
                BUILD_MAP                1
        L7:     RETURN_VALUE

  --    L8:     PUSH_EXC_INFO

 200            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       82 (to L13)
                NOT_TAKEN
                STORE_FAST               7 (e)

 201    L9:     LOAD_GLOBAL             18 (logger)
                LOAD_ATTR               21 (warning + NULL|self)

 202            LOAD_CONST              14 ('_update_row_encrypted db error type=')
                LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 201            CALL                     1
                POP_TOP

 205            LOAD_CONST               9 ('status')
                LOAD_CONST              10 ('failed')

 206            LOAD_CONST              11 ('error_code')
                LOAD_CONST              15 ('db_write_failed:')
                LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 204            BUILD_MAP                2
       L10:     SWAP                     2
       L11:     POP_EXCEPT
                LOAD_CONST               8 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RETURN_VALUE

  --   L12:     LOAD_CONST               8 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RERAISE                  1

 200   L13:     RERAISE                  0

  --   L14:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L3 -> L8 [0]
  L4 to L5 -> L8 [0]
  L6 to L7 -> L8 [0]
  L8 to L9 -> L14 [1] lasti
  L9 to L10 -> L12 [1] lasti
  L10 to L11 -> L14 [1] lasti
  L12 to L14 -> L14 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024F30, file "scripts\rotate_email_forwarder_secret.py", line 210>:
210           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

212           LOAD_CONST               2 ('Optional[str]')

210           LOAD_CONST               3 ('limit')

213           LOAD_CONST               4 ('int')

210           LOAD_CONST               5 ('kid')

214           LOAD_CONST               2 ('Optional[str]')

210           LOAD_CONST               6 ('execute')

215           LOAD_CONST               7 ('bool')

210           LOAD_CONST               8 ('return')

216           LOAD_CONST               9 ('Dict[str, Any]')

210           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object rotate at 0x0000018C17E053C0, file "scripts\rotate_email_forwarder_secret.py", line 210>:
210            RESUME                   0

238            LOAD_GLOBAL              1 (_clamp + NULL)
               LOAD_FAST_BORROW         1 (limit)
               LOAD_GLOBAL              2 (_MIN_LIMIT)
               LOAD_GLOBAL              4 (_MAX_LIMIT)
               LOAD_GLOBAL              6 (_DEFAULT_LIMIT)
               CALL                     4
               STORE_FAST               1 (limit)

241            LOAD_GLOBAL              9 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (brokerage_id)
               LOAD_GLOBAL             10 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       39 (to L1)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (brokerage_id)
               LOAD_ATTR               13 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_FALSE       17 (to L1)
               NOT_TAKEN

240            LOAD_FAST_BORROW         0 (brokerage_id)
               LOAD_ATTR               13 (strip + NULL|self)
               CALL                     0
               JUMP_FORWARD             1 (to L2)

242    L1:     LOAD_CONST               1 (None)

239    L2:     STORE_FAST               4 (bid)

246            LOAD_GLOBAL              9 (isinstance + NULL)
               LOAD_FAST_BORROW         2 (kid)
               LOAD_GLOBAL             10 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       39 (to L3)
               NOT_TAKEN
               LOAD_FAST_BORROW         2 (kid)
               LOAD_ATTR               13 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_FALSE       17 (to L3)
               NOT_TAKEN

245            LOAD_FAST_BORROW         2 (kid)
               LOAD_ATTR               13 (strip + NULL|self)
               CALL                     0
               JUMP_FORWARD             1 (to L4)

247    L3:     LOAD_CONST               1 (None)

244    L4:     STORE_FAST               5 (kid_arg)

249            BUILD_LIST               0
               STORE_FAST               6 (warnings)

251            LOAD_GLOBAL             15 (_get_db_safe + NULL)
               CALL                     0
               STORE_FAST               7 (db)

252            LOAD_FAST_BORROW         7 (db)
               POP_JUMP_IF_NOT_NONE    50 (to L7)
               NOT_TAKEN

253            LOAD_FAST_BORROW         6 (warnings)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               2 ('durable_email_dedupe_unavailable')
               CALL                     1
               POP_TOP

255            LOAD_CONST               3 ('status')
               LOAD_CONST               4 ('skipped')

256            LOAD_CONST               5 ('mode')
               LOAD_FAST_BORROW         3 (execute)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               6 ('execute')
               JUMP_FORWARD             1 (to L6)
       L5:     LOAD_CONST               7 ('dry-run')

257    L6:     LOAD_CONST               8 ('limit')
               LOAD_FAST_BORROW         1 (limit)

258            LOAD_CONST               9 ('kid')
               LOAD_FAST_BORROW         5 (kid_arg)

259            LOAD_CONST              10 ('candidate_count')
               LOAD_SMALL_INT           0

260            LOAD_CONST              11 ('rotated_count')
               LOAD_SMALL_INT           0

261            LOAD_CONST              12 ('skipped_count')
               LOAD_SMALL_INT           0

262            LOAD_CONST              13 ('failed_count')
               LOAD_SMALL_INT           0

263            LOAD_CONST              14 ('warnings')
               LOAD_FAST_BORROW         6 (warnings)

264            LOAD_CONST              15 ('error_code')
               LOAD_CONST               1 (None)

254            BUILD_MAP               10
               RETURN_VALUE

267    L7:     LOAD_GLOBAL             19 (_select_rotation_candidates + NULL)

268            LOAD_FAST_BORROW_LOAD_FAST_BORROW 116 (db, bid)
               LOAD_FAST_BORROW         1 (limit)

267            LOAD_CONST              16 (('brokerage_id', 'limit'))
               CALL_KW                  3
               STORE_FAST               8 (listing)

270            LOAD_FAST_BORROW         8 (listing)
               LOAD_CONST               3 ('status')
               BINARY_OP               26 ([])
               LOAD_CONST              17 ('ok')
               COMPARE_OP             119 (bool(!=))
               POP_JUMP_IF_FALSE       58 (to L11)
               NOT_TAKEN

272            LOAD_CONST               3 ('status')
               LOAD_CONST              18 ('failed')

273            LOAD_CONST               5 ('mode')
               LOAD_FAST_BORROW         3 (execute)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN
               LOAD_CONST               6 ('execute')
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST               7 ('dry-run')

274    L9:     LOAD_CONST               8 ('limit')
               LOAD_FAST                1 (limit)

275            LOAD_CONST               9 ('kid')
               LOAD_FAST                5 (kid_arg)

276            LOAD_CONST              10 ('candidate_count')
               LOAD_SMALL_INT           0

277            LOAD_CONST              11 ('rotated_count')
               LOAD_SMALL_INT           0

278            LOAD_CONST              12 ('skipped_count')
               LOAD_SMALL_INT           0

279            LOAD_CONST              13 ('failed_count')
               LOAD_SMALL_INT           0

280            LOAD_CONST              14 ('warnings')
               LOAD_FAST                6 (warnings)

281            LOAD_CONST              15 ('error_code')
               LOAD_FAST_BORROW         8 (listing)
               LOAD_ATTR               21 (get + NULL|self)
               LOAD_CONST              15 ('error_code')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L10)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              19 ('db_read_failed')

271   L10:     BUILD_MAP               10
               RETURN_VALUE

283   L11:     LOAD_FAST_BORROW         8 (listing)
               LOAD_CONST              20 ('rows')
               BINARY_OP               26 ([])
               STORE_FAST               9 (rows)

284            LOAD_GLOBAL             23 (len + NULL)
               LOAD_FAST_BORROW         9 (rows)
               CALL                     1
               STORE_FAST              10 (candidate_count)

286            LOAD_FAST_BORROW         3 (execute)
               TO_BOOL
               POP_JUMP_IF_TRUE        23 (to L12)
               NOT_TAKEN

293            LOAD_CONST               3 ('status')
               LOAD_CONST              17 ('ok')

294            LOAD_CONST               5 ('mode')
               LOAD_CONST               7 ('dry-run')

295            LOAD_CONST               8 ('limit')
               LOAD_FAST_BORROW         1 (limit)

296            LOAD_CONST               9 ('kid')
               LOAD_FAST_BORROW         5 (kid_arg)

297            LOAD_CONST              10 ('candidate_count')
               LOAD_FAST_BORROW        10 (candidate_count)

298            LOAD_CONST              11 ('rotated_count')
               LOAD_SMALL_INT           0

299            LOAD_CONST              12 ('skipped_count')
               LOAD_SMALL_INT           0

300            LOAD_CONST              13 ('failed_count')
               LOAD_SMALL_INT           0

301            LOAD_CONST              14 ('warnings')
               LOAD_FAST_BORROW         6 (warnings)

302            LOAD_CONST              15 ('error_code')
               LOAD_CONST               1 (None)

292            BUILD_MAP               10
               RETURN_VALUE

306   L12:     LOAD_SMALL_INT           0
               STORE_FAST              11 (rotated_count)

307            LOAD_SMALL_INT           0
               STORE_FAST              12 (skipped_count)

308            LOAD_SMALL_INT           0
               STORE_FAST              13 (failed_count)

310            LOAD_FAST_BORROW         9 (rows)
               GET_ITER
      L13:     EXTENDED_ARG             2
               FOR_ITER               526 (to L28)
               STORE_FAST              14 (row)

311            LOAD_GLOBAL              9 (isinstance + NULL)
               LOAD_FAST_BORROW        14 (row)
               LOAD_GLOBAL             24 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        12 (to L14)
               NOT_TAKEN

312            LOAD_FAST_BORROW        12 (skipped_count)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST              12 (skipped_count)

313            JUMP_BACKWARD           37 (to L13)

314   L14:     LOAD_FAST_BORROW        14 (row)
               LOAD_ATTR               21 (get + NULL|self)
               LOAD_CONST              21 ('id')
               CALL                     1
               STORE_FAST              15 (row_id)

315            LOAD_FAST_BORROW        14 (row)
               LOAD_ATTR               21 (get + NULL|self)
               LOAD_CONST              22 ('email_forwarder_secret')
               CALL                     1
               STORE_FAST              16 (plaintext)

316            LOAD_GLOBAL              9 (isinstance + NULL)
               LOAD_FAST_BORROW        15 (row_id)
               LOAD_GLOBAL             10 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L15)
               NOT_TAKEN
               LOAD_FAST_BORROW        15 (row_id)
               LOAD_ATTR               13 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE        12 (to L16)
               NOT_TAKEN

317   L15:     LOAD_FAST_BORROW        12 (skipped_count)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST              12 (skipped_count)

318            JUMP_BACKWARD          126 (to L13)

319   L16:     LOAD_GLOBAL              9 (isinstance + NULL)
               LOAD_FAST_BORROW        16 (plaintext)
               LOAD_GLOBAL             10 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L17)
               NOT_TAKEN
               LOAD_FAST_BORROW        16 (plaintext)
               LOAD_ATTR               13 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE        12 (to L18)
               NOT_TAKEN

320   L17:     LOAD_FAST_BORROW        12 (skipped_count)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST              12 (skipped_count)

321            JUMP_BACKWARD          181 (to L13)

325   L18:     LOAD_FAST_BORROW        14 (row)
               LOAD_ATTR               21 (get + NULL|self)
               LOAD_CONST              23 ('email_forwarder_secret_encrypted')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       12 (to L19)
               NOT_TAKEN

326            LOAD_FAST_BORROW        12 (skipped_count)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST              12 (skipped_count)

327            JUMP_BACKWARD          215 (to L13)

329   L19:     LOAD_GLOBAL             27 (encrypt_email_forwarder_secret + NULL)

330            LOAD_FAST_BORROW        16 (plaintext)

331            LOAD_FAST_BORROW         5 (kid_arg)

329            LOAD_CONST              24 (('key_id',))
               CALL_KW                  2
               STORE_FAST              17 (enc)

333            LOAD_FAST_BORROW        17 (enc)
               LOAD_ATTR               21 (get + NULL|self)
               LOAD_CONST               3 ('status')
               CALL                     1
               LOAD_CONST              17 ('ok')
               COMPARE_OP             119 (bool(!=))
               POP_JUMP_IF_FALSE       64 (to L22)
               NOT_TAKEN

334            LOAD_FAST_BORROW        13 (failed_count)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST              13 (failed_count)

336            LOAD_FAST_BORROW        17 (enc)
               LOAD_ATTR               21 (get + NULL|self)
               LOAD_CONST              15 ('error_code')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L20)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              25 ('rotation_encrypt_failed')
      L20:     STORE_FAST              18 (code)

337            LOAD_FAST_BORROW        18 (code)
               LOAD_FAST_BORROW         6 (warnings)
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_FALSE       18 (to L21)
               NOT_TAKEN

338            LOAD_FAST_BORROW         6 (warnings)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_FAST_BORROW        18 (code)
               CALL                     1
               POP_TOP

339   L21:     EXTENDED_ARG             1
               JUMP_BACKWARD          313 (to L13)

341   L22:     LOAD_FAST_BORROW        17 (enc)
               LOAD_ATTR               21 (get + NULL|self)
               LOAD_CONST              26 ('encrypted')
               CALL                     1
               STORE_FAST              19 (encrypted)

342            LOAD_FAST_BORROW        17 (enc)
               LOAD_ATTR               21 (get + NULL|self)
               LOAD_CONST              27 ('key_id')
               CALL                     1
               STORE_FAST              20 (used_kid)

343            LOAD_GLOBAL              9 (isinstance + NULL)
               LOAD_FAST_BORROW        19 (encrypted)
               LOAD_GLOBAL             10 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L23)
               NOT_TAKEN
               LOAD_GLOBAL              9 (isinstance + NULL)
               LOAD_FAST_BORROW        20 (used_kid)
               LOAD_GLOBAL             10 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        13 (to L24)
               NOT_TAKEN

344   L23:     LOAD_FAST_BORROW        13 (failed_count)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST              13 (failed_count)

345            EXTENDED_ARG             1
               JUMP_BACKWARD          403 (to L13)

347   L24:     LOAD_GLOBAL             29 (_update_row_encrypted + NULL)

348            LOAD_FAST_BORROW         7 (db)

349            LOAD_FAST_BORROW        15 (row_id)
               LOAD_ATTR               13 (strip + NULL|self)
               CALL                     0

350            LOAD_FAST_BORROW        19 (encrypted)

351            LOAD_FAST_BORROW        20 (used_kid)

347            LOAD_CONST              28 (('brokerage_id', 'ciphertext', 'kid'))
               CALL_KW                  4
               STORE_FAST              21 (upd)

353            LOAD_FAST_BORROW        21 (upd)
               LOAD_ATTR               21 (get + NULL|self)
               LOAD_CONST               3 ('status')
               CALL                     1
               LOAD_CONST              17 ('ok')
               COMPARE_OP             119 (bool(!=))
               POP_JUMP_IF_FALSE       64 (to L27)
               NOT_TAKEN

354            LOAD_FAST_BORROW        13 (failed_count)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST              13 (failed_count)

355            LOAD_FAST_BORROW        21 (upd)
               LOAD_ATTR               21 (get + NULL|self)
               LOAD_CONST              15 ('error_code')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L25)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              29 ('rotation_update_failed')
      L25:     STORE_FAST              18 (code)

356            LOAD_FAST_BORROW        18 (code)
               LOAD_FAST_BORROW         6 (warnings)
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_FALSE       18 (to L26)
               NOT_TAKEN

357            LOAD_FAST_BORROW         6 (warnings)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_FAST_BORROW        18 (code)
               CALL                     1
               POP_TOP

358   L26:     EXTENDED_ARG             2
               JUMP_BACKWARD          517 (to L13)

360   L27:     LOAD_FAST_BORROW        11 (rotated_count)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST              11 (rotated_count)
               EXTENDED_ARG             2
               JUMP_BACKWARD          529 (to L13)

310   L28:     END_FOR
               POP_ITER

362            LOAD_FAST_BORROW        13 (failed_count)
               LOAD_SMALL_INT           0
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE        3 (to L29)
               NOT_TAKEN
               LOAD_CONST              17 ('ok')
               JUMP_FORWARD             1 (to L30)
      L29:     LOAD_CONST              18 ('failed')
      L30:     STORE_FAST              22 (status)

364            LOAD_CONST               3 ('status')
               LOAD_FAST               22 (status)

365            LOAD_CONST               5 ('mode')
               LOAD_CONST               6 ('execute')

366            LOAD_CONST               8 ('limit')
               LOAD_FAST                1 (limit)

367            LOAD_CONST               9 ('kid')
               LOAD_FAST                5 (kid_arg)

368            LOAD_CONST              10 ('candidate_count')
               LOAD_FAST               10 (candidate_count)

369            LOAD_CONST              11 ('rotated_count')
               LOAD_FAST               11 (rotated_count)

370            LOAD_CONST              12 ('skipped_count')
               LOAD_FAST               12 (skipped_count)

371            LOAD_CONST              13 ('failed_count')
               LOAD_FAST               13 (failed_count)

372            LOAD_CONST              14 ('warnings')
               LOAD_FAST                6 (warnings)

373            LOAD_CONST              15 ('error_code')
               LOAD_FAST_BORROW        22 (status)
               LOAD_CONST              17 ('ok')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE        4 (to L31)
               NOT_TAKEN
               LOAD_CONST               1 (None)

363            BUILD_MAP               10
               RETURN_VALUE

373   L31:     LOAD_CONST              30 ('rotation_partial_failure')

363            BUILD_MAP               10
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "scripts\rotate_email_forwarder_secret.py", line 381>:
381           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C17EC5380, file "scripts\rotate_email_forwarder_secret.py", line 381>:
381           RESUME                   0

382           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

383           LOAD_CONST               0 ('rotate_email_forwarder_secret')

385           LOAD_CONST               1 ("PAS168 — Operator-only secret rotation tool. Encrypts brokerages' plaintext email_forwarder_secret into the encrypted column using the PAS168 kid-aware helper. Dry-run by default; --execute is required to write. NEVER prints the plaintext secret, the ciphertext, or the key material. NEVER deletes the plaintext column.")

382           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

395           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

396           LOAD_CONST               3 ('--brokerage-id')
              LOAD_CONST               4 (None)

397           LOAD_CONST               5 ('Optional brokerage scope.')

395           LOAD_CONST               6 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

399           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

400           LOAD_CONST               7 ('--limit')
              LOAD_GLOBAL              6 (int)
              LOAD_GLOBAL              8 (_DEFAULT_LIMIT)

402           LOAD_CONST               8 ('Cap on candidates per run. Clamped to [')

403           LOAD_GLOBAL             10 (_MIN_LIMIT)
              FORMAT_SIMPLE
              LOAD_CONST               9 (', ')
              LOAD_GLOBAL             12 (_MAX_LIMIT)
              FORMAT_SIMPLE
              LOAD_CONST              10 (']. Default ')
              LOAD_GLOBAL              8 (_DEFAULT_LIMIT)
              FORMAT_SIMPLE
              LOAD_CONST              11 ('.')

402           BUILD_STRING             7

399           LOAD_CONST              12 (('type', 'default', 'help'))
              CALL_KW                  4
              POP_TOP

406           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

407           LOAD_CONST              13 ('--kid')
              LOAD_CONST               4 (None)

409           LOAD_CONST              14 ('Optional kid override. When unset the env-bound active kid (PAS_EMAIL_FORWARDER_SECRET_ACTIVE_KID) is used.')

406           LOAD_CONST               6 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

414           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

415           LOAD_CONST              15 ('--json')
              LOAD_CONST              16 ('store_true')

416           LOAD_CONST              17 ('Emit the structural report as JSON on stdout.')

414           LOAD_CONST              18 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

418           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

419           LOAD_CONST              19 ('--execute')
              LOAD_CONST              16 ('store_true')

421           LOAD_CONST              20 ('Actually encrypt + write. Without this flag the rotation runs in dry-run mode and prints counts only.')

418           LOAD_CONST              18 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

426           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "scripts\rotate_email_forwarder_secret.py", line 429>:
429           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('report')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('None')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _print_summary at 0x0000018C17ECDD80, file "scripts\rotate_email_forwarder_secret.py", line 429>:
429           RESUME                   0

430           LOAD_GLOBAL              1 (print + NULL)

431           LOAD_CONST               0 ('[PAS168-rotate] status=')
              LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               1 ('status')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               2 (' mode=')

432           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               3 ('mode')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' limit=')

433           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               5 ('limit')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' candidates=')

434           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               7 ('candidate_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' rotated=')

435           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               9 ('rotated_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              10 (' skipped=')

436           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              11 ('skipped_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              12 (' failed=')

437           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              13 ('failed_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE

431           BUILD_STRING            14

430           CALL                     1
              POP_TOP

439           LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST              14 ('warnings')
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       31 (to L3)
              NOT_TAKEN

440           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              14 ('warnings')
              BINARY_OP               26 ([])
              GET_ITER
      L1:     FOR_ITER                17 (to L2)
              STORE_FAST               1 (w)

441           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              15 ('  warning: ')
              LOAD_FAST_BORROW         1 (w)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L1)

440   L2:     END_FOR
              POP_ITER

442   L3:     LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST              16 ('error_code')
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       24 (to L4)
              NOT_TAKEN

443           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              17 ('  error_code: ')
              LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              16 ('error_code')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              LOAD_CONST              18 (None)
              RETURN_VALUE

442   L4:     LOAD_CONST              18 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "scripts\rotate_email_forwarder_secret.py", line 446>:
446           RESUME                   0
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

Disassembly of <code object main at 0x0000018C18645DE0, file "scripts\rotate_email_forwarder_secret.py", line 446>:
 446            RESUME                   0

 447            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 448            NOP

 449    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 453    L2:     LOAD_GLOBAL             11 (rotate + NULL)

 454            LOAD_FAST                2 (args)
                LOAD_ATTR               12 (brokerage_id)

 455            LOAD_FAST                2 (args)
                LOAD_ATTR               14 (limit)

 456            LOAD_FAST                2 (args)
                LOAD_ATTR               16 (kid)

 457            LOAD_GLOBAL             19 (bool + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               20 (execute)
                CALL                     1

 453            LOAD_CONST               2 (('brokerage_id', 'limit', 'kid', 'execute'))
                CALL_KW                  4
                STORE_FAST               4 (report)

 460            LOAD_FAST                2 (args)
                LOAD_ATTR               22 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       36 (to L3)
                NOT_TAKEN

 461            LOAD_GLOBAL             25 (print + NULL)
                LOAD_GLOBAL             22 (json)
                LOAD_ATTR               26 (dumps)
                PUSH_NULL
                LOAD_FAST                4 (report)
                LOAD_SMALL_INT           2
                LOAD_CONST               3 (True)
                LOAD_CONST               4 (('indent', 'sort_keys'))
                CALL_KW                  3
                CALL                     1
                POP_TOP
                JUMP_FORWARD            11 (to L4)

 463    L3:     LOAD_GLOBAL             29 (_print_summary + NULL)
                LOAD_FAST                4 (report)
                CALL                     1
                POP_TOP

 465    L4:     LOAD_FAST                4 (report)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST               5 ('status')
                CALL                     1
                STORE_FAST               5 (status)

 466            LOAD_FAST                5 (status)
                LOAD_CONST               8 (('ok', 'skipped'))
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN

 467            LOAD_SMALL_INT           0
                RETURN_VALUE

 468    L5:     LOAD_FAST                5 (status)
                LOAD_CONST               6 ('failed')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN

 469            LOAD_SMALL_INT           1
                RETURN_VALUE

 470    L6:     LOAD_SMALL_INT           1
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

 450            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L16)
                NOT_TAKEN
                STORE_FAST               3 (e)

 451    L8:     LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                LOAD_CONST               7 ((0, None))
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE        3 (to L9)
                NOT_TAKEN
                LOAD_SMALL_INT           2
                JUMP_FORWARD            30 (to L13)
        L9:     LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L12)
       L10:     NOT_TAKEN
       L11:     POP_TOP
                LOAD_SMALL_INT           0
       L12:     CALL                     1
       L13:     SWAP                     2
       L14:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RETURN_VALUE

  --   L15:     LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 450   L16:     RERAISE                  0

  --   L17:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L7 [0]
  L7 to L8 -> L17 [1] lasti
  L8 to L10 -> L15 [1] lasti
  L11 to L13 -> L15 [1] lasti
  L13 to L14 -> L17 [1] lasti
  L15 to L17 -> L17 [1] lasti
```
