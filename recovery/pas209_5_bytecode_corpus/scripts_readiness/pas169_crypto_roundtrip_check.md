# scripts_readiness/pas169_crypto_roundtrip_check

- **pyc:** `scripts\__pycache__\pas169_crypto_roundtrip_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/pas169_crypto_roundtrip_check.py`
- **co_filename (from bytecode):** `scripts\pas169_crypto_roundtrip_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS169 — Crypto roundtrip checker.

Verifies that the PAS168 kid-aware encrypt / decrypt path
works in the actual runtime environment. Catches the "we
declared cryptography in requirements.txt but the deployment
never actually installed it" deployment-risk knot before
pilot launch.

Doctrine:

* **Read-only.** No DB writes, no migration execution, no
  ``.env`` read, no production data touched.
* **No key material printed.** The checker generates an
  in-memory Fernet key, uses it for the roundtrip, and never
  echoes it (or the plaintext, or the ciphertext) on stdout
  or in the JSON report. The report is structural-only.
* **No silent success.** Every assertion in the roundtrip
  must hold; the first failure produces a structural error
  and a non-zero exit code.
* **No fake fallback.** If ``cryptography.fernet`` is not
  importable, the checker exits 1 with a structural
  ``crypto_unavailable`` blocker. It NEVER pretends the
  roundtrip succeeded.

Usage:
  python scripts/pas169_crypto_roundtrip_check.py
  python scripts/pas169_crypto_roundtrip_check.py --json
  python scripts/pas169_crypto_roundtrip_check.py --summary-only
  python scripts/pas169_crypto_roundtrip_check.py --use-env-key

The ``--use-env-key`` flag tells the checker to NOT generate
its own Fernet key — it instead expects the operator to have
configured a real ``PAS_EMAIL_FORWARDER_SECRET_FERNET_KEY_<KID>``
env var. This is the CI / production verification mode. The
default invocation is the local-developer-friendly mode
(in-memory key, no env read).

Exit codes:
    0  — READY  (all assertions held)
    1  — NOT_READY (one or more assertions failed)
    2  — bad CLI arguments
```

## Imports

`Any`, `Dict`, `Fernet`, `List`, `Optional`, `Path`, `__future__`, `annotations`, `app.services.ingestion.email_forwarder_secret_store`, `argparse`, `cryptography.fernet`, `datetime`, `decrypt_email_forwarder_secret`, `encrypt_email_forwarder_secret`, `get_email_forwarder_secret`, `json`, `os`, `pathlib`, `sys`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_build_parser`, `_check`, `_load_fernet`, `_now_iso`, `_print_summary`, `_redact`, `_run_roundtrip`, `main`

## Env-key candidates

`DUMMY_PLAINTEXT_NEVER_RETURNED`, `FAIL`, `NOT_READY`, `PAS169`, `PASS`, `PAS_EMAIL_FORWARDER_SECRET_FERNET_KEY_`, `READY`

## String constants (redacted where noted)

- '\nPAS169 — Crypto roundtrip checker.\n\nVerifies that the PAS168 kid-aware encrypt / decrypt path\nworks in the actual runtime environment. Catches the "we\ndeclared cryptography in requirements.txt but the deployment\nnever actually installed it" deployment-risk knot before\npilot launch.\n\nDoctrine:\n\n* **Read-only.** No DB writes, no migration execution, no\n  ``.env`` read, no production data touched.\n* **No key material printed.** The checker generates an\n  in-memory Fernet key, uses it for the roundtrip, and never\n  echoes it (or the plaintext, or the ciphertext) on stdout\n  or in the JSON report. The report is structural-only.\n* **No silent success.** Every assertion in the roundtrip\n  must hold; the first failure produces a structural error\n  and a non-zero exit code.\n* **No fake fallback.** If ``cryptography.fernet`` is not\n  importable, the checker exits 1 with a structural\n  ``crypto_unavailable`` blocker. It NEVER pretends the\n  roundtrip succeeded.\n\nUsage:\n  python scripts/pas169_crypto_roundtrip_check.py\n  python scripts/pas169_crypto_roundtrip_check.py --json\n  python scripts/pas169_crypto_roundtrip_check.py --summary-only\n  python scripts/pas169_crypto_roundtrip_check.py --use-env-key\n\nThe ``--use-env-key`` flag tells the checker to NOT generate\nits own Fernet key — it instead expects the operator to have\nconfigured a real ``PAS_EMAIL_FORWARDER_SECRET_FERNET_KEY_<KID>``\nenv var. This is the CI / production verification mode. The\ndefault invocation is the local-developer-friendly mode\n(in-memory key, no env read).\n\nExit codes:\n    0  — READY  (all assertions held)\n    1  — NOT_READY (one or more assertions failed)\n    2  — bad CLI arguments\n'
- 'utf-8'
- 'pas169-test'
- 'detail'
- 'check_id'
- 'str'
- 'status'
- 'label'
- 'return'
- 'Dict[str, Any]'
- 'seconds'
- "Try to import the ``cryptography.fernet.Fernet``\nprimitive. Returns the class on success, ``None`` if the\npackage isn't importable. NEVER raises."
- 'Constant used in every report field where a real value\ncould otherwise leak. The checker NEVER substitutes a\nreal key / plaintext / ciphertext into the report.'
- '<redacted>'
- 'use_env_key'
- 'bool'
- 'Execute the roundtrip + the negative-path assertions.\n\nReturns a structural report with one entry per assertion.\nNEVER includes the key, the plaintext, or the ciphertext\nin the report.\n'
- 'crypto:importable'
- 'FAIL'
- 'cryptography.fernet.Fernet is importable'
- 'ImportError on cryptography.fernet'
- 'phase'
- 'PAS169'
- 'generated_at'
- 'mode'
- 'use-env-key'
- 'in-memory-key'
- 'kid'
- 'ready'
- 'verdict'
- 'NOT_READY'
- 'blocker_count'
- 'check_count'
- 'pass_count'
- 'fail_count'
- 'checks'
- 'operator_actions'
- '[BLOCK] crypto:importable — install cryptography>=42 (see requirements.txt). Verify with: python -c "from cryptography.fernet import Fernet".'
- 'PASS'
- 'PAS_EMAIL_FORWARDER_SECRET_FERNET_KEY_'
- 'crypto:env_key_set'
- 'Env var '
- ' is configured'
- 'operator must export the per-kid key before running --use-env-key mode'
- '[BLOCK] crypto:env_key_set — export '
- ' before running --use-env-key.'
- 'crypto:keygen'
- 'Fernet.generate_key() succeeded'
- '[BLOCK] crypto:keygen — Fernet.generate_key() raised.'
- 'email_forwarder_secret_encryption_enabled'
- 'email_forwarder_secret_active_kid'
- 'email_forwarder_secret_keys'
- 'store:importable'
- 'email_forwarder_secret_store helpers are importable'
- '[BLOCK] store:importable — import failure: '
- 'PAS169-ROUNDTRIP-INPUT'
- 'roundtrip:encrypt_ok'
- 'encrypt_email_forwarder_secret returns status=ok'
- 'error_code'
- 'non-dict-return'
- 'encrypted'
- 'roundtrip:kid_prefix'
- "Envelope starts with '"
- ":' kid prefix"
- 'missing kid prefix on envelope'
- 'key_id'
- 'roundtrip:encrypt_returns_kid'
- 'encrypt envelope key_id matches active kid'
- 'key_id mismatch'
- 'failed'
- 'no_ciphertext'
- 'roundtrip:decrypt_ok'
- 'decrypt_email_forwarder_secret returns status=ok'
- 'unknown'
- 'secret'
- 'roundtrip:plaintext_equals_input'
- 'Decrypted plaintext equals original input'
- 'plaintext mismatch (values redacted)'
- ':not-a-real-token'
- 'forwarder_secret_decrypt_failed'
- 'roundtrip:malformed_fails'
- 'Malformed ciphertext returns forwarder_secret_decrypt_failed'
- 'got status='
- ', error_code='
- 'pas169-unknown-kid:'
- 'pas169-unknown-kid:bogus'
- 'crypto_key_missing'
- 'roundtrip:unknown_kid_fails'
- 'Unknown kid returns crypto_key_missing'
- 'pas169-test-row'
- 'email_forwarder_secret'
- 'DUMMY_PLAINTEXT_NEVER_RETURNED'
- 'email_forwarder_secret_encrypted'
- 'plaintext_fallback'
- 'roundtrip:no_plaintext_fallback_on_decrypt_failure'
- 'Encrypted-present decrypt failure does NOT fall back to plaintext'
- ', plaintext_fallback='
- 'get_email_forwarder_secret raised: '
- '[BLOCK] '
- ' — '
- 'see check label'
- 'READY'
- 'argparse.ArgumentParser'
- 'pas169_crypto_roundtrip_check'
- 'PAS169 — Verify that the PAS168 kid-aware Fernet encrypt / decrypt path works in this runtime environment. In-memory key by default; operator may pass --use-env-key to verify a real per-kid env var instead. NEVER prints the key, plaintext, or ciphertext. NEVER writes to the DB, runs a migration, or reads .env.'
- '--summary-only'
- 'store_true'
- 'Print verdict only; skip the JSON dump.'
- '--json'
- 'Emit the report JSON on stdout in addition to the summary.'
- '--use-env-key'
- 'Use the per-kid env var PAS_EMAIL_FORWARDER_SECRET_FERNET_KEY_PAS169_TEST instead of an in-memory generated key. The env var must already be exported (the checker NEVER reads .env).'
- 'report'
- 'None'
- '[PAS169-roundtrip] verdict='
- ' mode='
- ' kid='
- ' checks='
- ' pass='
- ' fail='
- '  - '
- 'argv'
- 'Optional[List[str]]'
- 'int'

## Disassembly

```
   0           RESUME                   0

   1           LOAD_CONST               0 ('\nPAS169 — Crypto roundtrip checker.\n\nVerifies that the PAS168 kid-aware encrypt / decrypt path\nworks in the actual runtime environment. Catches the "we\ndeclared cryptography in requirements.txt but the deployment\nnever actually installed it" deployment-risk knot before\npilot launch.\n\nDoctrine:\n\n* **Read-only.** No DB writes, no migration execution, no\n  ``.env`` read, no production data touched.\n* **No key material printed.** The checker generates an\n  in-memory Fernet key, uses it for the roundtrip, and never\n  echoes it (or the plaintext, or the ciphertext) on stdout\n  or in the JSON report. The report is structural-only.\n* **No silent success.** Every assertion in the roundtrip\n  must hold; the first failure produces a structural error\n  and a non-zero exit code.\n* **No fake fallback.** If ``cryptography.fernet`` is not\n  importable, the checker exits 1 with a structural\n  ``crypto_unavailable`` blocker. It NEVER pretends the\n  roundtrip succeeded.\n\nUsage:\n  python scripts/pas169_crypto_roundtrip_check.py\n  python scripts/pas169_crypto_roundtrip_check.py --json\n  python scripts/pas169_crypto_roundtrip_check.py --summary-only\n  python scripts/pas169_crypto_roundtrip_check.py --use-env-key\n\nThe ``--use-env-key`` flag tells the checker to NOT generate\nits own Fernet key — it instead expects the operator to have\nconfigured a real ``PAS_EMAIL_FORWARDER_SECRET_FERNET_KEY_<KID>``\nenv var. This is the CI / production verification mode. The\ndefault invocation is the local-developer-friendly mode\n(in-memory key, no env read).\n\nExit codes:\n    0  — READY  (all assertions held)\n    1  — NOT_READY (one or more assertions failed)\n    2  — bad CLI arguments\n')
               STORE_NAME               0 (__doc__)

  45           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  47           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  48           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (json)
               STORE_NAME               4 (json)

  49           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (os)
               STORE_NAME               5 (os)

  50           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (sys)
               STORE_NAME               6 (sys)

  51           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              7 (datetime)
               IMPORT_FROM              7 (datetime)
               STORE_NAME               7 (datetime)
               IMPORT_FROM              8 (timezone)
               STORE_NAME               8 (timezone)
               POP_TOP

  52           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Path',))
               IMPORT_NAME              9 (pathlib)
               IMPORT_FROM             10 (Path)
               STORE_NAME              10 (Path)
               POP_TOP

  53           LOAD_SMALL_INT           0
               LOAD_CONST               5 (('Any', 'Dict', 'List', 'Optional'))
               IMPORT_NAME             11 (typing)
               IMPORT_FROM             12 (Any)
               STORE_NAME              12 (Any)
               IMPORT_FROM             13 (Dict)
               STORE_NAME              13 (Dict)
               IMPORT_FROM             14 (List)
               STORE_NAME              14 (List)
               IMPORT_FROM             15 (Optional)
               STORE_NAME              15 (Optional)
               POP_TOP

  56           LOAD_NAME                6 (sys)
               LOAD_ATTR               32 (stdout)
               LOAD_NAME                6 (sys)
               LOAD_ATTR               34 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              18 (_stream)

  57           NOP

  58   L2:     LOAD_NAME               18 (_stream)
               LOAD_ATTR               39 (reconfigure + NULL|self)
               LOAD_CONST               6 ('utf-8')
               LOAD_CONST               7 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  56   L4:     END_FOR
               POP_ITER

  65           LOAD_NAME                5 (os)
               LOAD_ATTR               42 (path)
               LOAD_ATTR               45 (abspath + NULL|self)

  66           LOAD_NAME                5 (os)
               LOAD_ATTR               42 (path)
               LOAD_ATTR               47 (join + NULL|self)
               LOAD_NAME                5 (os)
               LOAD_ATTR               42 (path)
               LOAD_ATTR               49 (dirname + NULL|self)
               LOAD_NAME               25 (__file__)
               CALL                     1
               LOAD_CONST               8 ('..')
               CALL                     2

  65           CALL                     1
               STORE_NAME              26 (_REPO_ROOT_DEFAULT)

  68           LOAD_NAME                6 (sys)
               LOAD_ATTR               42 (path)
               LOAD_ATTR               55 (insert + NULL|self)
               LOAD_SMALL_INT           0
               LOAD_NAME               26 (_REPO_ROOT_DEFAULT)
               CALL                     2
               POP_TOP

  75           LOAD_CONST               9 ('pas169-test')
               STORE_NAME              28 (_TEST_KID)

  82           LOAD_CONST              10 ('detail')

  87           LOAD_CONST              11 ('')

  82           BUILD_MAP                1
               LOAD_CONST              12 (<code object __annotate__ at 0x0000018C18026430, file "scripts\pas169_crypto_roundtrip_check.py", line 82>)
               MAKE_FUNCTION
               LOAD_CONST              13 (<code object _check at 0x0000018C17FA31E0, file "scripts\pas169_crypto_roundtrip_check.py", line 82>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              29 (_check)

  97           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C17FA3E10, file "scripts\pas169_crypto_roundtrip_check.py", line 97>)
               MAKE_FUNCTION
               LOAD_CONST              15 (<code object _now_iso at 0x0000018C18038F30, file "scripts\pas169_crypto_roundtrip_check.py", line 97>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              30 (_now_iso)

 101           LOAD_CONST              16 (<code object _load_fernet at 0x0000018C17FBFEE0, file "scripts\pas169_crypto_roundtrip_check.py", line 101>)
               MAKE_FUNCTION
               STORE_NAME              31 (_load_fernet)

 112           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C17FA3960, file "scripts\pas169_crypto_roundtrip_check.py", line 112>)
               MAKE_FUNCTION
               LOAD_CONST              18 (<code object _redact at 0x0000018C18068D50, file "scripts\pas169_crypto_roundtrip_check.py", line 112>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              32 (_redact)

 123           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA3C30, file "scripts\pas169_crypto_roundtrip_check.py", line 123>)
               MAKE_FUNCTION
               LOAD_CONST              20 (<code object _run_roundtrip at 0x0000018C17F80C70, file "scripts\pas169_crypto_roundtrip_check.py", line 123>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              33 (_run_roundtrip)

 487           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA30F0, file "scripts\pas169_crypto_roundtrip_check.py", line 487>)
               MAKE_FUNCTION
               LOAD_CONST              22 (<code object _build_parser at 0x0000018C17FF10B0, file "scripts\pas169_crypto_roundtrip_check.py", line 487>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              34 (_build_parser)

 521           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA3F00, file "scripts\pas169_crypto_roundtrip_check.py", line 521>)
               MAKE_FUNCTION
               LOAD_CONST              24 (<code object _print_summary at 0x0000018C18048C70, file "scripts\pas169_crypto_roundtrip_check.py", line 521>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              35 (_print_summary)

 534           LOAD_CONST              28 ((None,))
               LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA2010, file "scripts\pas169_crypto_roundtrip_check.py", line 534>)
               MAKE_FUNCTION
               LOAD_CONST              26 (<code object main at 0x0000018C17CD0A50, file "scripts\pas169_crypto_roundtrip_check.py", line 534>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              36 (main)

 551           LOAD_NAME               37 (__name__)
               LOAD_CONST              27 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 552           LOAD_NAME                6 (sys)
               LOAD_ATTR               76 (exit)
               PUSH_NULL
               LOAD_NAME               36 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 551   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  59           LOAD_NAME               20 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L8)
               NOT_TAKEN
               POP_TOP

  60   L7:     POP_EXCEPT
               JUMP_BACKWARD          229 (to L1)

  59   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026430, file "scripts\pas169_crypto_roundtrip_check.py", line 82>:
 82           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('check_id')

 83           LOAD_CONST               2 ('str')

 82           LOAD_CONST               3 ('status')

 84           LOAD_CONST               2 ('str')

 82           LOAD_CONST               4 ('label')

 85           LOAD_CONST               2 ('str')

 82           LOAD_CONST               5 ('detail')

 87           LOAD_CONST               2 ('str')

 82           LOAD_CONST               6 ('return')

 88           LOAD_CONST               7 ('Dict[str, Any]')

 82           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _check at 0x0000018C17FA31E0, file "scripts\pas169_crypto_roundtrip_check.py", line 82>:
 82           RESUME                   0

 90           LOAD_CONST               0 ('id')
              LOAD_FAST_BORROW         0 (check_id)

 91           LOAD_CONST               1 ('status')
              LOAD_FAST_BORROW         1 (status)

 92           LOAD_CONST               2 ('label')
              LOAD_FAST_BORROW         2 (label)

 93           LOAD_CONST               3 ('detail')
              LOAD_FAST_BORROW         3 (detail)

 89           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "scripts\pas169_crypto_roundtrip_check.py", line 97>:
 97           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038F30, file "scripts\pas169_crypto_roundtrip_check.py", line 97>:
 97           RESUME                   0

 98           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object _load_fernet at 0x0000018C17FBFEE0, file "scripts\pas169_crypto_roundtrip_check.py", line 101>:
 101           RESUME                   0

 105           NOP

 106   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('Fernet',))
               IMPORT_NAME              0 (cryptography.fernet)
               IMPORT_FROM              1 (Fernet)
               STORE_FAST               0 (Fernet)
               POP_TOP

 107           LOAD_FAST_BORROW         0 (Fernet)
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 108           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 109   L4:     POP_EXCEPT
               LOAD_CONST               2 (None)
               RETURN_VALUE

 108   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "scripts\pas169_crypto_roundtrip_check.py", line 112>:
112           RESUME                   0
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

Disassembly of <code object _redact at 0x0000018C18068D50, file "scripts\pas169_crypto_roundtrip_check.py", line 112>:
112           RESUME                   0

116           LOAD_CONST               1 ('<redacted>')
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "scripts\pas169_crypto_roundtrip_check.py", line 123>:
123           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('use_env_key')

125           LOAD_CONST               2 ('bool')

123           LOAD_CONST               3 ('return')

126           LOAD_CONST               4 ('Dict[str, Any]')

123           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _run_roundtrip at 0x0000018C17F80C70, file "scripts\pas169_crypto_roundtrip_check.py", line 123>:
 123            RESUME                   0

 133            BUILD_LIST               0
                STORE_FAST               1 (checks)

 135            LOAD_GLOBAL              1 (_load_fernet + NULL)
                CALL                     0
                STORE_FAST               2 (Fernet)

 136            LOAD_FAST_BORROW         2 (Fernet)
                POP_JUMP_IF_NOT_NONE    80 (to L3)
                NOT_TAKEN

 137            LOAD_FAST_BORROW         1 (checks)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_GLOBAL              5 (_check + NULL)

 138            LOAD_CONST               2 ('crypto:importable')

 139            LOAD_CONST               3 ('FAIL')

 140            LOAD_CONST               4 ('cryptography.fernet.Fernet is importable')

 141            LOAD_CONST               5 ('ImportError on cryptography.fernet')

 137            LOAD_CONST               6 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 144            LOAD_CONST               7 ('phase')
                LOAD_CONST               8 ('PAS169')

 145            LOAD_CONST               9 ('generated_at')
                LOAD_GLOBAL              7 (_now_iso + NULL)
                CALL                     0

 146            LOAD_CONST              10 ('mode')
                LOAD_FAST_BORROW         0 (use_env_key)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L1)
                NOT_TAKEN
                LOAD_CONST              11 ('use-env-key')
                JUMP_FORWARD             1 (to L2)
        L1:     LOAD_CONST              12 ('in-memory-key')

 147    L2:     LOAD_CONST              13 ('kid')
                LOAD_GLOBAL              8 (_TEST_KID)

 148            LOAD_CONST              14 ('ready')
                LOAD_CONST              15 (False)

 149            LOAD_CONST              16 ('verdict')
                LOAD_CONST              17 ('NOT_READY')

 150            LOAD_CONST              18 ('blocker_count')
                LOAD_SMALL_INT           1

 151            LOAD_CONST              19 ('check_count')
                LOAD_SMALL_INT           1

 152            LOAD_CONST              20 ('pass_count')
                LOAD_SMALL_INT           0

 153            LOAD_CONST              21 ('fail_count')
                LOAD_SMALL_INT           1

 154            LOAD_CONST              22 ('checks')
                LOAD_FAST_BORROW         1 (checks)

 155            LOAD_CONST              23 ('operator_actions')

 156            LOAD_CONST              24 ('[BLOCK] crypto:importable — install cryptography>=42 (see requirements.txt). Verify with: python -c "from cryptography.fernet import Fernet".')

 155            BUILD_LIST               1

 143            BUILD_MAP               12
                RETURN_VALUE

 161    L3:     LOAD_FAST_BORROW         1 (checks)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_GLOBAL              5 (_check + NULL)

 162            LOAD_CONST               2 ('crypto:importable')

 163            LOAD_CONST              25 ('PASS')

 164            LOAD_CONST               4 ('cryptography.fernet.Fernet is importable')

 161            CALL                     3
                CALL                     1
                POP_TOP

 169            LOAD_CONST              26 ('PAS_EMAIL_FORWARDER_SECRET_FERNET_KEY_')

 170            LOAD_GLOBAL              8 (_TEST_KID)
                LOAD_ATTR               11 (upper + NULL|self)
                CALL                     0
                LOAD_ATTR               13 (replace + NULL|self)
                LOAD_CONST              27 ('-')
                LOAD_CONST              28 ('_')
                CALL                     2
                LOAD_ATTR               13 (replace + NULL|self)
                LOAD_CONST              29 ('.')
                LOAD_CONST              28 ('_')
                CALL                     2

 169            BINARY_OP                0 (+)

 168            STORE_FAST               3 (env_var)

 173            LOAD_FAST_BORROW         0 (use_env_key)
                TO_BOOL
                POP_JUMP_IF_FALSE      215 (to L6)
                NOT_TAKEN

 177            LOAD_GLOBAL             14 (os)
                LOAD_ATTR               16 (environ)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_FAST_BORROW         3 (env_var)
                CALL                     1
                STORE_FAST               4 (env_key)

 178            LOAD_FAST_BORROW         4 (env_key)
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L4)
                NOT_TAKEN
                LOAD_FAST_BORROW         4 (env_key)
                LOAD_ATTR               21 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE       119 (to L5)
                NOT_TAKEN

 179    L4:     LOAD_FAST_BORROW         1 (checks)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_GLOBAL              5 (_check + NULL)

 180            LOAD_CONST              30 ('crypto:env_key_set')

 181            LOAD_CONST               3 ('FAIL')

 182            LOAD_CONST              31 ('Env var ')
                LOAD_FAST_BORROW         3 (env_var)
                FORMAT_SIMPLE
                LOAD_CONST              32 (' is configured')
                BUILD_STRING             3

 184            LOAD_CONST              33 ('operator must export the per-kid key before running --use-env-key mode')

 179            LOAD_CONST               6 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 189            LOAD_CONST               7 ('phase')
                LOAD_CONST               8 ('PAS169')

 190            LOAD_CONST               9 ('generated_at')
                LOAD_GLOBAL              7 (_now_iso + NULL)
                CALL                     0

 191            LOAD_CONST              10 ('mode')
                LOAD_CONST              11 ('use-env-key')

 192            LOAD_CONST              13 ('kid')
                LOAD_GLOBAL              8 (_TEST_KID)

 193            LOAD_CONST              14 ('ready')
                LOAD_CONST              15 (False)

 194            LOAD_CONST              16 ('verdict')
                LOAD_CONST              17 ('NOT_READY')

 195            LOAD_CONST              18 ('blocker_count')
                LOAD_SMALL_INT           1

 196            LOAD_CONST              19 ('check_count')
                LOAD_GLOBAL             23 (len + NULL)
                LOAD_FAST_BORROW         1 (checks)
                CALL                     1

 197            LOAD_CONST              20 ('pass_count')
                LOAD_GLOBAL             25 (sum + NULL)
                LOAD_CONST              34 (<code object <genexpr> at 0x0000018C18053510, file "scripts\pas169_crypto_roundtrip_check.py", line 197>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         1 (checks)
                GET_ITER
                CALL                     0
                CALL                     1

 198            LOAD_CONST              21 ('fail_count')
                LOAD_GLOBAL             25 (sum + NULL)
                LOAD_CONST              35 (<code object <genexpr> at 0x0000018C18053630, file "scripts\pas169_crypto_roundtrip_check.py", line 198>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         1 (checks)
                GET_ITER
                CALL                     0
                CALL                     1

 199            LOAD_CONST              22 ('checks')
                LOAD_FAST_BORROW         1 (checks)

 200            LOAD_CONST              23 ('operator_actions')

 201            LOAD_CONST              36 ('[BLOCK] crypto:env_key_set — export ')

 202            LOAD_FAST_BORROW         3 (env_var)
                FORMAT_SIMPLE
                LOAD_CONST              37 (' before running --use-env-key.')

 201            BUILD_STRING             3

 200            BUILD_LIST               1

 188            BUILD_MAP               12
                RETURN_VALUE

 205    L5:     LOAD_CONST               1 (None)
                STORE_FAST               5 (config_or_env)

 206            LOAD_FAST_BORROW         1 (checks)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_GLOBAL              5 (_check + NULL)

 207            LOAD_CONST              30 ('crypto:env_key_set')

 208            LOAD_CONST              25 ('PASS')

 209            LOAD_CONST              31 ('Env var ')
                LOAD_FAST_BORROW         3 (env_var)
                FORMAT_SIMPLE
                LOAD_CONST              32 (' is configured')
                BUILD_STRING             3

 206            CALL                     3
                CALL                     1
                POP_TOP
                JUMP_FORWARD            78 (to L9)

 217    L6:     NOP

 218    L7:     LOAD_FAST_BORROW         2 (Fernet)
                LOAD_ATTR               27 (generate_key + NULL|self)
                CALL                     0
                STORE_FAST               6 (key_bytes)

 242    L8:     LOAD_FAST                1 (checks)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_GLOBAL              5 (_check + NULL)

 243            LOAD_CONST              38 ('crypto:keygen')

 244            LOAD_CONST              25 ('PASS')

 245            LOAD_CONST              39 ('Fernet.generate_key() succeeded')

 242            CALL                     3
                CALL                     1
                POP_TOP

 248            LOAD_CONST              43 ('email_forwarder_secret_encryption_enabled')
                LOAD_CONST              44 (True)

 249            LOAD_CONST              45 ('email_forwarder_secret_active_kid')
                LOAD_GLOBAL              8 (_TEST_KID)

 250            LOAD_CONST              46 ('email_forwarder_secret_keys')

 251            LOAD_GLOBAL              8 (_TEST_KID)
                LOAD_FAST                6 (key_bytes)
                LOAD_ATTR               35 (decode + NULL|self)
                LOAD_CONST              47 ('utf-8')
                CALL                     1

 250            BUILD_MAP                1

 247            BUILD_MAP                3
                STORE_FAST               5 (config_or_env)

 259    L9:     NOP

 260   L10:     LOAD_SMALL_INT           0
                LOAD_CONST              48 (('encrypt_email_forwarder_secret', 'decrypt_email_forwarder_secret'))
                IMPORT_NAME             18 (app.services.ingestion.email_forwarder_secret_store)
                IMPORT_FROM             19 (encrypt_email_forwarder_secret)
                STORE_FAST               8 (encrypt_email_forwarder_secret)
                IMPORT_FROM             20 (decrypt_email_forwarder_secret)
                STORE_FAST               9 (decrypt_email_forwarder_secret)
                POP_TOP

 288   L11:     LOAD_FAST                1 (checks)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_GLOBAL              5 (_check + NULL)

 289            LOAD_CONST              49 ('store:importable')

 290            LOAD_CONST              25 ('PASS')

 291            LOAD_CONST              50 ('email_forwarder_secret_store helpers are importable')

 288            CALL                     3
                CALL                     1
                POP_TOP

 295            LOAD_CONST              54 ('PAS169-ROUNDTRIP-INPUT')
                STORE_FAST              10 (test_plaintext)

 296            LOAD_FAST                8 (encrypt_email_forwarder_secret)
                PUSH_NULL

 297            LOAD_FAST               10 (test_plaintext)

 298            LOAD_GLOBAL              8 (_TEST_KID)

 299            LOAD_FAST                5 (config_or_env)

 296            LOAD_CONST              55 (('key_id', 'config_or_env'))
                CALL_KW                  3
                STORE_FAST              11 (enc)

 301            LOAD_GLOBAL             43 (isinstance + NULL)
                LOAD_FAST               11 (enc)
                LOAD_GLOBAL             44 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L12)
                NOT_TAKEN
                LOAD_FAST               11 (enc)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              56 ('status')
                CALL                     1
                LOAD_CONST              57 ('ok')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       71 (to L15)
                NOT_TAKEN

 302   L12:     LOAD_FAST                1 (checks)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_GLOBAL              5 (_check + NULL)

 303            LOAD_CONST              58 ('roundtrip:encrypt_ok')

 304            LOAD_CONST               3 ('FAIL')

 305            LOAD_CONST              59 ('encrypt_email_forwarder_secret returns status=ok')

 307            LOAD_GLOBAL             43 (isinstance + NULL)
                LOAD_FAST               11 (enc)
                LOAD_GLOBAL             44 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L13)
                NOT_TAKEN
                LOAD_FAST               11 (enc)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              60 ('error_code')
                CALL                     1
                JUMP_FORWARD             1 (to L14)

 308   L13:     LOAD_CONST              61 ('non-dict-return')

 302   L14:     LOAD_CONST               6 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
                JUMP_FORWARD            28 (to L16)

 312   L15:     LOAD_FAST                1 (checks)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_GLOBAL              5 (_check + NULL)

 313            LOAD_CONST              58 ('roundtrip:encrypt_ok')

 314            LOAD_CONST              25 ('PASS')

 315            LOAD_CONST              59 ('encrypt_email_forwarder_secret returns status=ok')

 312            CALL                     3
                CALL                     1
                POP_TOP

 318   L16:     LOAD_GLOBAL             43 (isinstance + NULL)
                LOAD_FAST               11 (enc)
                LOAD_GLOBAL             44 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L17)
                NOT_TAKEN
                LOAD_FAST               11 (enc)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              62 ('encrypted')
                CALL                     1
                JUMP_FORWARD             1 (to L18)
       L17:     LOAD_CONST               1 (None)
       L18:     STORE_FAST              12 (ciphertext)

 320            LOAD_GLOBAL             43 (isinstance + NULL)
                LOAD_FAST               12 (ciphertext)
                LOAD_GLOBAL             46 (str)
                CALL                     2
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       29 (to L19)
                NOT_TAKEN
                POP_TOP

 321            LOAD_FAST               12 (ciphertext)
                LOAD_ATTR               49 (startswith + NULL|self)
                LOAD_GLOBAL              8 (_TEST_KID)
                LOAD_CONST              63 (':')
                BINARY_OP                0 (+)
                CALL                     1

 319   L19:     STORE_FAST              13 (has_kid_prefix)

 323            LOAD_FAST                1 (checks)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_GLOBAL              5 (_check + NULL)

 324            LOAD_CONST              64 ('roundtrip:kid_prefix')

 325            LOAD_FAST               13 (has_kid_prefix)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L20)
                NOT_TAKEN
                LOAD_CONST              25 ('PASS')
                JUMP_FORWARD             1 (to L21)
       L20:     LOAD_CONST               3 ('FAIL')

 326   L21:     LOAD_CONST              65 ("Envelope starts with '")
                LOAD_GLOBAL              8 (_TEST_KID)
                FORMAT_SIMPLE
                LOAD_CONST              66 (":' kid prefix")
                BUILD_STRING             3

 327            LOAD_FAST               13 (has_kid_prefix)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L22)
                NOT_TAKEN
                LOAD_CONST              67 ('')
                JUMP_FORWARD             1 (to L23)
       L22:     LOAD_CONST              68 ('missing kid prefix on envelope')

 323   L23:     LOAD_CONST               6 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 330            LOAD_GLOBAL             43 (isinstance + NULL)
                LOAD_FAST               11 (enc)
                LOAD_GLOBAL             44 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L24)
                NOT_TAKEN
                LOAD_FAST               11 (enc)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              69 ('key_id')
                CALL                     1
                JUMP_FORWARD             1 (to L25)
       L24:     LOAD_CONST               1 (None)
       L25:     STORE_FAST              14 (returned_kid)

 331            LOAD_FAST               14 (returned_kid)
                LOAD_GLOBAL              8 (_TEST_KID)
                COMPARE_OP              72 (==)
                STORE_FAST              15 (kid_matches)

 332            LOAD_FAST                1 (checks)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_GLOBAL              5 (_check + NULL)

 333            LOAD_CONST              70 ('roundtrip:encrypt_returns_kid')

 334            LOAD_FAST               15 (kid_matches)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L26)
                NOT_TAKEN
                LOAD_CONST              25 ('PASS')
                JUMP_FORWARD             1 (to L27)
       L26:     LOAD_CONST               3 ('FAIL')

 335   L27:     LOAD_CONST              71 ('encrypt envelope key_id matches active kid')

 336            LOAD_FAST               15 (kid_matches)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L28)
                NOT_TAKEN
                LOAD_CONST              67 ('')
                JUMP_FORWARD             1 (to L29)
       L28:     LOAD_CONST              72 ('key_id mismatch')

 332   L29:     LOAD_CONST               6 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 340            LOAD_GLOBAL             43 (isinstance + NULL)
                LOAD_FAST               12 (ciphertext)
                LOAD_GLOBAL             46 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       11 (to L30)
                NOT_TAKEN

 341            LOAD_FAST                9 (decrypt_email_forwarder_secret)
                PUSH_NULL

 342            LOAD_FAST_LOAD_FAST    197 (ciphertext, config_or_env)

 341            LOAD_CONST              73 (('config_or_env',))
                CALL_KW                  2
                STORE_FAST              16 (dec)
                JUMP_FORWARD             6 (to L31)

 345   L30:     LOAD_CONST              56 ('status')
                LOAD_CONST              74 ('failed')
                LOAD_CONST              60 ('error_code')
                LOAD_CONST              75 ('no_ciphertext')
                BUILD_MAP                2
                STORE_FAST              16 (dec)

 346   L31:     LOAD_FAST               16 (dec)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              56 ('status')
                CALL                     1
                LOAD_CONST              57 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       30 (to L32)
                NOT_TAKEN

 347            LOAD_FAST                1 (checks)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_GLOBAL              5 (_check + NULL)

 348            LOAD_CONST              76 ('roundtrip:decrypt_ok')

 349            LOAD_CONST              25 ('PASS')

 350            LOAD_CONST              77 ('decrypt_email_forwarder_secret returns status=ok')

 347            CALL                     3
                CALL                     1
                POP_TOP
                JUMP_FORWARD            64 (to L34)

 353   L32:     LOAD_FAST                1 (checks)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_GLOBAL              5 (_check + NULL)

 354            LOAD_CONST              76 ('roundtrip:decrypt_ok')

 355            LOAD_CONST               3 ('FAIL')

 356            LOAD_CONST              77 ('decrypt_email_forwarder_secret returns status=ok')

 357            LOAD_GLOBAL             47 (str + NULL)
                LOAD_FAST               16 (dec)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              60 ('error_code')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L33)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              78 ('unknown')
       L33:     CALL                     1

 353            LOAD_CONST               6 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 363   L34:     LOAD_FAST               16 (dec)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              79 ('secret')
                CALL                     1
                LOAD_FAST               10 (test_plaintext)
                COMPARE_OP              72 (==)
                STORE_FAST              17 (plain_match)

 364            LOAD_FAST                1 (checks)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_GLOBAL              5 (_check + NULL)

 365            LOAD_CONST              80 ('roundtrip:plaintext_equals_input')

 366            LOAD_FAST               17 (plain_match)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L35)
                NOT_TAKEN
                LOAD_CONST              25 ('PASS')
                JUMP_FORWARD             1 (to L36)
       L35:     LOAD_CONST               3 ('FAIL')

 367   L36:     LOAD_CONST              81 ('Decrypted plaintext equals original input')

 368            LOAD_FAST               17 (plain_match)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L37)
                NOT_TAKEN
                LOAD_CONST              67 ('')
                JUMP_FORWARD             1 (to L38)
       L37:     LOAD_CONST              82 ('plaintext mismatch (values redacted)')

 364   L38:     LOAD_CONST               6 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 372            LOAD_FAST                9 (decrypt_email_forwarder_secret)
                PUSH_NULL

 373            LOAD_GLOBAL              8 (_TEST_KID)
                LOAD_CONST              83 (':not-a-real-token')
                BINARY_OP                0 (+)

 374            LOAD_FAST                5 (config_or_env)

 372            LOAD_CONST              73 (('config_or_env',))
                CALL_KW                  2
                STORE_FAST              18 (dec_malformed)

 377            LOAD_FAST               18 (dec_malformed)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              56 ('status')
                CALL                     1
                LOAD_CONST              74 ('failed')
                COMPARE_OP              72 (==)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       21 (to L39)
                NOT_TAKEN
                POP_TOP

 378            LOAD_FAST               18 (dec_malformed)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              60 ('error_code')
                CALL                     1
                LOAD_CONST              84 ('forwarder_secret_decrypt_failed')
                COMPARE_OP              72 (==)

 376   L39:     STORE_FAST              19 (malformed_fails)

 380            LOAD_FAST                1 (checks)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_GLOBAL              5 (_check + NULL)

 381            LOAD_CONST              85 ('roundtrip:malformed_fails')

 382            LOAD_FAST               19 (malformed_fails)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L40)
                NOT_TAKEN
                LOAD_CONST              25 ('PASS')
                JUMP_FORWARD             1 (to L41)
       L40:     LOAD_CONST               3 ('FAIL')

 383   L41:     LOAD_CONST              86 ('Malformed ciphertext returns forwarder_secret_decrypt_failed')

 385            LOAD_FAST               19 (malformed_fails)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L42)
                NOT_TAKEN
                LOAD_CONST              67 ('')
                JUMP_FORWARD            37 (to L43)

 386   L42:     LOAD_CONST              87 ('got status=')
                LOAD_FAST               18 (dec_malformed)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              56 ('status')
                CALL                     1
                FORMAT_SIMPLE
                LOAD_CONST              88 (', error_code=')

 387            LOAD_FAST               18 (dec_malformed)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              60 ('error_code')
                CALL                     1
                FORMAT_SIMPLE

 386            BUILD_STRING             4

 380   L43:     LOAD_CONST               6 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 394            LOAD_GLOBAL             43 (isinstance + NULL)
                LOAD_FAST               12 (ciphertext)
                LOAD_GLOBAL             46 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       43 (to L44)
                NOT_TAKEN
                LOAD_CONST              63 (':')
                LOAD_FAST               12 (ciphertext)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       36 (to L44)
                NOT_TAKEN

 395            LOAD_FAST               12 (ciphertext)
                LOAD_ATTR               51 (split + NULL|self)
                LOAD_CONST              63 (':')
                LOAD_SMALL_INT           1
                CALL                     2
                LOAD_SMALL_INT           1
                BINARY_OP               26 ([])
                STORE_FAST              20 (token_only)

 396            LOAD_CONST              89 ('pas169-unknown-kid:')
                LOAD_FAST               20 (token_only)
                BINARY_OP                0 (+)
                STORE_FAST              21 (forged)
                JUMP_FORWARD             2 (to L45)

 398   L44:     LOAD_CONST              90 ('pas169-unknown-kid:bogus')
                STORE_FAST              21 (forged)

 399   L45:     LOAD_FAST                9 (decrypt_email_forwarder_secret)
                PUSH_NULL

 400            LOAD_FAST               21 (forged)
                LOAD_FAST                5 (config_or_env)

 399            LOAD_CONST              73 (('config_or_env',))
                CALL_KW                  2
                STORE_FAST              22 (dec_unknown)

 403            LOAD_FAST               22 (dec_unknown)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              56 ('status')
                CALL                     1
                LOAD_CONST              74 ('failed')
                COMPARE_OP              72 (==)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       21 (to L46)
                NOT_TAKEN
                POP_TOP

 404            LOAD_FAST               22 (dec_unknown)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              60 ('error_code')
                CALL                     1
                LOAD_CONST              91 ('crypto_key_missing')
                COMPARE_OP              72 (==)

 402   L46:     STORE_FAST              23 (unknown_fails)

 406            LOAD_FAST                1 (checks)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_GLOBAL              5 (_check + NULL)

 407            LOAD_CONST              92 ('roundtrip:unknown_kid_fails')

 408            LOAD_FAST               23 (unknown_fails)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L47)
                NOT_TAKEN
                LOAD_CONST              25 ('PASS')
                JUMP_FORWARD             1 (to L48)
       L47:     LOAD_CONST               3 ('FAIL')

 409   L48:     LOAD_CONST              93 ('Unknown kid returns crypto_key_missing')

 411            LOAD_FAST               23 (unknown_fails)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L49)
                NOT_TAKEN
                LOAD_CONST              67 ('')
                JUMP_FORWARD            37 (to L50)

 412   L49:     LOAD_CONST              87 ('got status=')
                LOAD_FAST               22 (dec_unknown)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              56 ('status')
                CALL                     1
                FORMAT_SIMPLE
                LOAD_CONST              88 (', error_code=')

 413            LOAD_FAST               22 (dec_unknown)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              60 ('error_code')
                CALL                     1
                FORMAT_SIMPLE

 412            BUILD_STRING             4

 406   L50:     LOAD_CONST               6 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 420            NOP

 421   L51:     LOAD_SMALL_INT           0
                LOAD_CONST              94 (('get_email_forwarder_secret',))
                IMPORT_NAME             18 (app.services.ingestion.email_forwarder_secret_store)
                IMPORT_FROM             26 (get_email_forwarder_secret)
                STORE_FAST              24 (get_email_forwarder_secret)
                POP_TOP

 424            LOAD_FAST               24 (get_email_forwarder_secret)
                PUSH_NULL

 426            LOAD_CONST              95 ('id')
                LOAD_CONST              96 ('pas169-test-row')

 427            LOAD_CONST              97 ('email_forwarder_secret')
                LOAD_CONST              98 ('DUMMY_PLAINTEXT_NEVER_RETURNED')

 428            LOAD_CONST              99 ('email_forwarder_secret_encrypted')
                LOAD_CONST              90 ('pas169-unknown-kid:bogus')

 425            BUILD_MAP                3

 430            LOAD_FAST                5 (config_or_env)

 424            LOAD_CONST              73 (('config_or_env',))
                CALL_KW                  2
                STORE_FAST              25 (env)

 433            LOAD_FAST               25 (env)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              56 ('status')
                CALL                     1
                LOAD_CONST              74 ('failed')
                COMPARE_OP              72 (==)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       47 (to L56)
       L52:     NOT_TAKEN
       L53:     POP_TOP

 434            LOAD_FAST               25 (env)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST             100 ('plaintext_fallback')
                CALL                     1
                LOAD_CONST              15 (False)
                IS_OP                    0 (is)

 433            COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       20 (to L56)
       L54:     NOT_TAKEN
       L55:     POP_TOP

 435            LOAD_FAST               25 (env)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              79 ('secret')
                CALL                     1
                LOAD_CONST               1 (None)
                IS_OP                    0 (is)

 432   L56:     STORE_FAST              26 (no_fallback)

 437            LOAD_FAST                1 (checks)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_GLOBAL              5 (_check + NULL)

 438            LOAD_CONST             101 ('roundtrip:no_plaintext_fallback_on_decrypt_failure')

 439            LOAD_FAST               26 (no_fallback)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L57)
                NOT_TAKEN
                LOAD_CONST              25 ('PASS')
                JUMP_FORWARD             1 (to L58)
       L57:     LOAD_CONST               3 ('FAIL')

 440   L58:     LOAD_CONST             102 ('Encrypted-present decrypt failure does NOT fall back to plaintext')

 442            LOAD_FAST               26 (no_fallback)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L61)
       L59:     NOT_TAKEN
       L60:     LOAD_CONST              67 ('')
                JUMP_FORWARD            37 (to L62)

 443   L61:     LOAD_CONST              87 ('got status=')
                LOAD_FAST               25 (env)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              56 ('status')
                CALL                     1
                FORMAT_SIMPLE
                LOAD_CONST             103 (', plaintext_fallback=')

 444            LOAD_FAST               25 (env)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST             100 ('plaintext_fallback')
                CALL                     1
                FORMAT_SIMPLE

 443            BUILD_STRING             4

 437   L62:     LOAD_CONST               6 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 455   L63:     LOAD_GLOBAL             25 (sum + NULL)
                LOAD_CONST             105 (<code object <genexpr> at 0x0000018C18053870, file "scripts\pas169_crypto_roundtrip_check.py", line 455>)
                MAKE_FUNCTION
                LOAD_FAST                1 (checks)
                GET_ITER
                CALL                     0
                CALL                     1
                STORE_FAST              27 (pass_count)

 456            LOAD_GLOBAL             25 (sum + NULL)
                LOAD_CONST             106 (<code object <genexpr> at 0x0000018C18053990, file "scripts\pas169_crypto_roundtrip_check.py", line 456>)
                MAKE_FUNCTION
                LOAD_FAST                1 (checks)
                GET_ITER
                CALL                     0
                CALL                     1
                STORE_FAST              28 (fail_count)

 457            LOAD_FAST               28 (fail_count)
                STORE_FAST              29 (blocker_count)

 458            LOAD_FAST               29 (blocker_count)
                LOAD_SMALL_INT           0
                COMPARE_OP              72 (==)
                STORE_FAST              30 (ready)

 460            BUILD_LIST               0
                STORE_FAST              31 (operator_actions)

 461            LOAD_FAST                1 (checks)
                GET_ITER
       L64:     FOR_ITER                75 (to L67)
                STORE_FAST              32 (c)

 462            LOAD_FAST               32 (c)
                LOAD_CONST              56 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               3 ('FAIL')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_TRUE         3 (to L65)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L64)

 463   L65:     LOAD_FAST               31 (operator_actions)
                LOAD_ATTR                3 (append + NULL|self)

 464            LOAD_CONST             107 ('[BLOCK] ')
                LOAD_FAST               32 (c)
                LOAD_CONST              95 ('id')
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                LOAD_CONST             108 (' — ')
                LOAD_FAST               32 (c)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST             109 ('detail')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L66)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST             110 ('see check label')
       L66:     FORMAT_SIMPLE
                LOAD_CONST              29 ('.')
                BUILD_STRING             5

 463            CALL                     1
                POP_TOP
                JUMP_BACKWARD           77 (to L64)

 461   L67:     END_FOR
                POP_ITER

 468            LOAD_CONST               7 ('phase')
                LOAD_CONST               8 ('PAS169')

 469            LOAD_CONST               9 ('generated_at')
                LOAD_GLOBAL              7 (_now_iso + NULL)
                CALL                     0

 470            LOAD_CONST              10 ('mode')
                LOAD_FAST                0 (use_env_key)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L68)
                NOT_TAKEN
                LOAD_CONST              11 ('use-env-key')
                JUMP_FORWARD             1 (to L69)
       L68:     LOAD_CONST              12 ('in-memory-key')

 471   L69:     LOAD_CONST              13 ('kid')
                LOAD_GLOBAL              8 (_TEST_KID)

 472            LOAD_CONST              14 ('ready')
                LOAD_FAST               30 (ready)

 473            LOAD_CONST              16 ('verdict')
                LOAD_FAST               30 (ready)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L70)
                NOT_TAKEN
                LOAD_CONST             111 ('READY')
                JUMP_FORWARD             1 (to L71)
       L70:     LOAD_CONST              17 ('NOT_READY')

 474   L71:     LOAD_CONST              18 ('blocker_count')
                LOAD_FAST               29 (blocker_count)

 475            LOAD_CONST              19 ('check_count')
                LOAD_GLOBAL             23 (len + NULL)
                LOAD_FAST                1 (checks)
                CALL                     1

 476            LOAD_CONST              20 ('pass_count')
                LOAD_FAST               27 (pass_count)

 477            LOAD_CONST              21 ('fail_count')
                LOAD_FAST               28 (fail_count)

 478            LOAD_CONST              22 ('checks')
                LOAD_FAST                1 (checks)

 479            LOAD_CONST              23 ('operator_actions')
                LOAD_FAST               31 (operator_actions)

 467            BUILD_MAP               12
                RETURN_VALUE

  --   L72:     PUSH_EXC_INFO

 219            LOAD_GLOBAL             28 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      140 (to L77)
                NOT_TAKEN
                STORE_FAST               7 (e)

 220   L73:     LOAD_FAST                1 (checks)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_GLOBAL              5 (_check + NULL)

 221            LOAD_CONST              38 ('crypto:keygen')

 222            LOAD_CONST               3 ('FAIL')

 223            LOAD_CONST              39 ('Fernet.generate_key() succeeded')

 224            LOAD_GLOBAL             31 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               32 (__name__)

 220            LOAD_CONST               6 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 227            LOAD_CONST               7 ('phase')
                LOAD_CONST               8 ('PAS169')

 228            LOAD_CONST               9 ('generated_at')
                LOAD_GLOBAL              7 (_now_iso + NULL)
                CALL                     0

 229            LOAD_CONST              10 ('mode')
                LOAD_CONST              12 ('in-memory-key')

 230            LOAD_CONST              13 ('kid')
                LOAD_GLOBAL              8 (_TEST_KID)

 231            LOAD_CONST              14 ('ready')
                LOAD_CONST              15 (False)

 232            LOAD_CONST              16 ('verdict')
                LOAD_CONST              17 ('NOT_READY')

 233            LOAD_CONST              18 ('blocker_count')
                LOAD_SMALL_INT           1

 234            LOAD_CONST              19 ('check_count')
                LOAD_GLOBAL             23 (len + NULL)
                LOAD_FAST                1 (checks)
                CALL                     1

 235            LOAD_CONST              20 ('pass_count')
                LOAD_GLOBAL             25 (sum + NULL)
                LOAD_CONST              40 (<code object <genexpr> at 0x0000018C18053CF0, file "scripts\pas169_crypto_roundtrip_check.py", line 235>)
                MAKE_FUNCTION
                LOAD_FAST                1 (checks)
                GET_ITER
                CALL                     0
                CALL                     1

 236            LOAD_CONST              21 ('fail_count')
                LOAD_GLOBAL             25 (sum + NULL)
                LOAD_CONST              41 (<code object <genexpr> at 0x0000018C180533F0, file "scripts\pas169_crypto_roundtrip_check.py", line 236>)
                MAKE_FUNCTION
                LOAD_FAST                1 (checks)
                GET_ITER
                CALL                     0
                CALL                     1

 237            LOAD_CONST              22 ('checks')
                LOAD_FAST                1 (checks)

 238            LOAD_CONST              23 ('operator_actions')

 239            LOAD_CONST              42 ('[BLOCK] crypto:keygen — Fernet.generate_key() raised.')

 238            BUILD_LIST               1

 226            BUILD_MAP               12
       L74:     SWAP                     2
       L75:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RETURN_VALUE

  --   L76:     LOAD_CONST               1 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RERAISE                  1

 219   L77:     RERAISE                  0

  --   L78:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L79:     PUSH_EXC_INFO

 264            LOAD_GLOBAL             28 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      172 (to L86)
                NOT_TAKEN
                STORE_FAST               7 (e)

 265   L80:     LOAD_FAST                1 (checks)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_GLOBAL              5 (_check + NULL)

 266            LOAD_CONST              49 ('store:importable')

 267            LOAD_CONST               3 ('FAIL')

 268            LOAD_CONST              50 ('email_forwarder_secret_store helpers are importable')

 269            LOAD_GLOBAL             31 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               32 (__name__)

 265            LOAD_CONST               6 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 272            LOAD_CONST               7 ('phase')
                LOAD_CONST               8 ('PAS169')

 273            LOAD_CONST               9 ('generated_at')
                LOAD_GLOBAL              7 (_now_iso + NULL)
                CALL                     0

 274            LOAD_CONST              10 ('mode')
                LOAD_FAST                0 (use_env_key)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L81)
                NOT_TAKEN
                LOAD_CONST              11 ('use-env-key')
                JUMP_FORWARD             1 (to L82)
       L81:     LOAD_CONST              12 ('in-memory-key')

 275   L82:     LOAD_CONST              13 ('kid')
                LOAD_GLOBAL              8 (_TEST_KID)

 276            LOAD_CONST              14 ('ready')
                LOAD_CONST              15 (False)

 277            LOAD_CONST              16 ('verdict')
                LOAD_CONST              17 ('NOT_READY')

 278            LOAD_CONST              18 ('blocker_count')
                LOAD_SMALL_INT           1

 279            LOAD_CONST              19 ('check_count')
                LOAD_GLOBAL             23 (len + NULL)
                LOAD_FAST                1 (checks)
                CALL                     1

 280            LOAD_CONST              20 ('pass_count')
                LOAD_GLOBAL             25 (sum + NULL)
                LOAD_CONST              51 (<code object <genexpr> at 0x0000018C180532D0, file "scripts\pas169_crypto_roundtrip_check.py", line 280>)
                MAKE_FUNCTION
                LOAD_FAST                1 (checks)
                GET_ITER
                CALL                     0
                CALL                     1

 281            LOAD_CONST              21 ('fail_count')
                LOAD_GLOBAL             25 (sum + NULL)
                LOAD_CONST              52 (<code object <genexpr> at 0x0000018C18053BD0, file "scripts\pas169_crypto_roundtrip_check.py", line 281>)
                MAKE_FUNCTION
                LOAD_FAST                1 (checks)
                GET_ITER
                CALL                     0
                CALL                     1

 282            LOAD_CONST              22 ('checks')
                LOAD_FAST                1 (checks)

 283            LOAD_CONST              23 ('operator_actions')

 284            LOAD_CONST              53 ('[BLOCK] store:importable — import failure: ')

 285            LOAD_GLOBAL             31 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               32 (__name__)
                FORMAT_SIMPLE

 284            BUILD_STRING             2

 283            BUILD_LIST               1

 271            BUILD_MAP               12
       L83:     SWAP                     2
       L84:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RETURN_VALUE

  --   L85:     LOAD_CONST               1 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RERAISE                  1

 264   L86:     RERAISE                  0

  --   L87:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L88:     PUSH_EXC_INFO

 447            LOAD_GLOBAL             28 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       64 (to L92)
                NOT_TAKEN
                STORE_FAST               7 (e)

 448   L89:     LOAD_FAST                1 (checks)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_GLOBAL              5 (_check + NULL)

 449            LOAD_CONST             101 ('roundtrip:no_plaintext_fallback_on_decrypt_failure')

 450            LOAD_CONST               3 ('FAIL')

 451            LOAD_CONST             102 ('Encrypted-present decrypt failure does NOT fall back to plaintext')

 452            LOAD_CONST             104 ('get_email_forwarder_secret raised: ')
                LOAD_GLOBAL             31 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               32 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 448            LOAD_CONST               6 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
       L90:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                EXTENDED_ARG             2
                JUMP_BACKWARD_NO_INTERRUPT 600 (to L63)

  --   L91:     LOAD_CONST               1 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RERAISE                  1

 447   L92:     RERAISE                  0

  --   L93:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L7 to L8 -> L72 [0]
  L10 to L11 -> L79 [0]
  L51 to L52 -> L88 [0]
  L53 to L54 -> L88 [0]
  L55 to L59 -> L88 [0]
  L60 to L63 -> L88 [0]
  L72 to L73 -> L78 [1] lasti
  L73 to L74 -> L76 [1] lasti
  L74 to L75 -> L78 [1] lasti
  L76 to L78 -> L78 [1] lasti
  L79 to L80 -> L87 [1] lasti
  L80 to L83 -> L85 [1] lasti
  L83 to L84 -> L87 [1] lasti
  L85 to L87 -> L87 [1] lasti
  L88 to L89 -> L93 [1] lasti
  L89 to L90 -> L91 [1] lasti
  L91 to L93 -> L93 [1] lasti

Disassembly of <code object <genexpr> at 0x0000018C18053510, file "scripts\pas169_crypto_roundtrip_check.py", line 197>:
 197           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C18053630, file "scripts\pas169_crypto_roundtrip_check.py", line 198>:
 198           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C18053CF0, file "scripts\pas169_crypto_roundtrip_check.py", line 235>:
 235           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C180533F0, file "scripts\pas169_crypto_roundtrip_check.py", line 236>:
 236           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C180532D0, file "scripts\pas169_crypto_roundtrip_check.py", line 280>:
 280           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C18053BD0, file "scripts\pas169_crypto_roundtrip_check.py", line 281>:
 281           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C18053870, file "scripts\pas169_crypto_roundtrip_check.py", line 455>:
 455           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C18053990, file "scripts\pas169_crypto_roundtrip_check.py", line 456>:
 456           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA30F0, file "scripts\pas169_crypto_roundtrip_check.py", line 487>:
487           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C17FF10B0, file "scripts\pas169_crypto_roundtrip_check.py", line 487>:
487           RESUME                   0

488           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

489           LOAD_CONST               0 ('pas169_crypto_roundtrip_check')

491           LOAD_CONST               1 ('PAS169 — Verify that the PAS168 kid-aware Fernet encrypt / decrypt path works in this runtime environment. In-memory key by default; operator may pass --use-env-key to verify a real per-kid env var instead. NEVER prints the key, plaintext, or ciphertext. NEVER writes to the DB, runs a migration, or reads .env.')

488           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

500           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

501           LOAD_CONST               3 ('--summary-only')
              LOAD_CONST               4 ('store_true')

502           LOAD_CONST               5 ('Print verdict only; skip the JSON dump.')

500           LOAD_CONST               6 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

504           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

505           LOAD_CONST               7 ('--json')
              LOAD_CONST               4 ('store_true')

506           LOAD_CONST               8 ('Emit the report JSON on stdout in addition to the summary.')

504           LOAD_CONST               6 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

508           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

509           LOAD_CONST               9 ('--use-env-key')
              LOAD_CONST               4 ('store_true')

511           LOAD_CONST              10 ('Use the per-kid env var PAS_EMAIL_FORWARDER_SECRET_FERNET_KEY_PAS169_TEST instead of an in-memory generated key. The env var must already be exported (the checker NEVER reads .env).')

508           LOAD_CONST               6 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

518           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3F00, file "scripts\pas169_crypto_roundtrip_check.py", line 521>:
521           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C18048C70, file "scripts\pas169_crypto_roundtrip_check.py", line 521>:
521           RESUME                   0

522           LOAD_GLOBAL              1 (print + NULL)

523           LOAD_CONST               0 ('[PAS169-roundtrip] verdict=')
              LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               1 ('verdict')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               2 (' mode=')

524           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               3 ('mode')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' kid=')

525           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               5 ('kid')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' checks=')

526           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               7 ('check_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' pass=')

527           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               9 ('pass_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              10 (' fail=')

528           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              11 ('fail_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE

523           BUILD_STRING            12

522           CALL                     1
              POP_TOP

530           LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST              12 ('operator_actions')
              BUILD_LIST               0
              CALL                     2
              LOAD_CONST              13 (slice(None, 25, None))
              BINARY_OP               26 ([])
              GET_ITER
      L1:     FOR_ITER                17 (to L2)
              STORE_FAST               1 (a)

531           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              14 ('  - ')
              LOAD_FAST_BORROW         1 (a)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L1)

530   L2:     END_FOR
              POP_ITER
              LOAD_CONST              15 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2010, file "scripts\pas169_crypto_roundtrip_check.py", line 534>:
534           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17CD0A50, file "scripts\pas169_crypto_roundtrip_check.py", line 534>:
 534            RESUME                   0

 535            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 536            NOP

 537    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 541    L2:     LOAD_GLOBAL             11 (_run_roundtrip + NULL)
                LOAD_GLOBAL             13 (bool + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               14 (use_env_key)
                CALL                     1
                LOAD_CONST               2 (('use_env_key',))
                CALL_KW                  1
                STORE_FAST               4 (report)

 543            LOAD_GLOBAL             17 (_print_summary + NULL)
                LOAD_FAST                4 (report)
                CALL                     1
                POP_TOP

 545            LOAD_FAST                2 (args)
                LOAD_ATTR               18 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L3)
                NOT_TAKEN

 546            LOAD_GLOBAL             21 (print + NULL)
                LOAD_GLOBAL             18 (json)
                LOAD_ATTR               22 (dumps)
                PUSH_NULL
                LOAD_FAST                4 (report)
                LOAD_SMALL_INT           2
                LOAD_CONST               3 (True)
                LOAD_CONST               4 (('indent', 'sort_keys'))
                CALL_KW                  3
                CALL                     1
                POP_TOP

 548    L3:     LOAD_FAST                4 (report)
                LOAD_CONST               5 ('ready')
                BINARY_OP               26 ([])
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L4)
                NOT_TAKEN
                LOAD_SMALL_INT           0
                RETURN_VALUE
        L4:     LOAD_SMALL_INT           1
                RETURN_VALUE

  --    L5:     PUSH_EXC_INFO

 538            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L14)
                NOT_TAKEN
                STORE_FAST               3 (e)

 539    L6:     LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                LOAD_CONST               6 ((0, None))
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE        3 (to L7)
                NOT_TAKEN
                LOAD_SMALL_INT           2
                JUMP_FORWARD            30 (to L11)
        L7:     LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
        L8:     NOT_TAKEN
        L9:     POP_TOP
                LOAD_SMALL_INT           0
       L10:     CALL                     1
       L11:     SWAP                     2
       L12:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RETURN_VALUE

  --   L13:     LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 538   L14:     RERAISE                  0

  --   L15:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L15 [1] lasti
  L6 to L8 -> L13 [1] lasti
  L9 to L11 -> L13 [1] lasti
  L11 to L12 -> L15 [1] lasti
  L13 to L15 -> L15 [1] lasti
```
