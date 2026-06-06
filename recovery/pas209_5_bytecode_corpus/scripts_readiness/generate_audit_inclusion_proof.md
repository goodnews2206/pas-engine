# scripts_readiness/generate_audit_inclusion_proof

- **pyc:** `scripts\__pycache__\generate_audit_inclusion_proof.cpython-314.pyc`
- **expected source path (absent):** `scripts/generate_audit_inclusion_proof.py`
- **co_filename (from bytecode):** `scripts\generate_audit_inclusion_proof.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS177 — Operator-runnable audit-entry inclusion proof CLI.

Generates a Merkle inclusion proof for a specific audit row
against the most-recent Merkle root window that contains it
(or against an explicit ``--merkle-root-id``). Read-only.
NEVER writes. NEVER echoes PII / secrets.

Doctrine:

* **Read-only.** The script does not INSERT, UPDATE, or
  DELETE anywhere. The output is a structural proof envelope.
* **Operator-driven.** No scheduler / cron / startup hook.
* **No PII.** Output carries only sha256 hex digests +
  structural indices + window timestamps. NEVER an
  action_id-tied audit row payload.
* **NEVER raises.**
* **DB unavailable → exit 0** with skipped envelope.
* **Bad args → exit 2.**

Usage:

    # Most recent root that covers the entry.
    python scripts/generate_audit_inclusion_proof.py \
        --brokerage-id brk-1 --audit-entry-id <UUID> --json

    # Explicit Merkle root.
    python scripts/generate_audit_inclusion_proof.py \
        --brokerage-id brk-1 --audit-entry-id <UUID> \
        --merkle-root-id <UUID> --json

Exit codes:
    0  — ok or skipped
    1  — failed (e.g. audit entry not found)
    2  — bad CLI arguments
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.services.operator.merkle_inclusion_proofs`, `argparse`, `datetime`, `json`, `logging`, `os`, `proof_for_audit_entry`, `sys`, `timezone`, `typing`, `verify_inclusion_proof`

## Classes

_none_

## Functions / methods

`__annotate__`, `_build_parser`, `_now_iso`, `_print_summary`, `_safe_envelope`, `generate`, `main`

## Env-key candidates

`PAS177`

## String constants (redacted where noted)

- '\nPAS177 — Operator-runnable audit-entry inclusion proof CLI.\n\nGenerates a Merkle inclusion proof for a specific audit row\nagainst the most-recent Merkle root window that contains it\n(or against an explicit ``--merkle-root-id``). Read-only.\nNEVER writes. NEVER echoes PII / secrets.\n\nDoctrine:\n\n* **Read-only.** The script does not INSERT, UPDATE, or\n  DELETE anywhere. The output is a structural proof envelope.\n* **Operator-driven.** No scheduler / cron / startup hook.\n* **No PII.** Output carries only sha256 hex digests +\n  structural indices + window timestamps. NEVER an\n  action_id-tied audit row payload.\n* **NEVER raises.**\n* **DB unavailable → exit 0** with skipped envelope.\n* **Bad args → exit 2.**\n\nUsage:\n\n    # Most recent root that covers the entry.\n    python scripts/generate_audit_inclusion_proof.py \\\n        --brokerage-id brk-1 --audit-entry-id <UUID> --json\n\n    # Explicit Merkle root.\n    python scripts/generate_audit_inclusion_proof.py \\\n        --brokerage-id brk-1 --audit-entry-id <UUID> \\\n        --merkle-root-id <UUID> --json\n\nExit codes:\n    0  — ok or skipped\n    1  — failed (e.g. audit entry not found)\n    2  — bad CLI arguments\n'
- 'utf-8'
- 'pas.scripts.generate_audit_inclusion_proof'
- 'proof'
- 'window_start'
- 'window_end'
- 'warnings'
- 'error_code'
- 'merkle_root_id'
- 'return'
- 'str'
- 'seconds'
- 'status'
- 'brokerage_id'
- 'Optional[str]'
- 'audit_entry_id'
- 'Optional[Dict[str, Any]]'
- 'Optional[List[str]]'
- 'Dict[str, Any]'
- 'phase'
- 'PAS177'
- 'tool'
- 'generate_audit_inclusion_proof'
- 'generated_at'
- 'Read-only proof generation. NEVER raises.'
- 'failed'
- 'valid'
- 'self_verification'
- 'argparse.ArgumentParser'
- 'PAS177 — Generate a Merkle inclusion proof for an audit entry. Read-only; never writes; never echoes PII / secrets / raw payloads.'
- '--brokerage-id'
- 'Brokerage scope. NEVER an email / phone.'
- '--audit-entry-id'
- 'The action_id of the audit row to prove inclusion for.'
- '--merkle-root-id'
- 'Optional explicit Merkle root row id. Default: most-recent root covering the entry.'
- '--json'
- 'store_true'
- 'Emit JSON on stdout instead of the human summary.'
- 'env'
- 'None'
- '[PAS177/generate_audit_inclusion_proof] status='
- ' brokerage_id='
- ' audit_entry_id='
- ' merkle_root_id='
- ' window_start='
- ' window_end='
- '  leaf_index='
- 'leaf_index'
- ' leaf_count='
- 'leaf_count'
- ' merkle_root_prefix='
- 'merkle_root'
- '... self_verification.valid='
- '  warn: '
- 'argv'
- 'int'
- 'skipped'

## Disassembly

```
   0           RESUME                   0

   1           LOAD_CONST               0 ('\nPAS177 — Operator-runnable audit-entry inclusion proof CLI.\n\nGenerates a Merkle inclusion proof for a specific audit row\nagainst the most-recent Merkle root window that contains it\n(or against an explicit ``--merkle-root-id``). Read-only.\nNEVER writes. NEVER echoes PII / secrets.\n\nDoctrine:\n\n* **Read-only.** The script does not INSERT, UPDATE, or\n  DELETE anywhere. The output is a structural proof envelope.\n* **Operator-driven.** No scheduler / cron / startup hook.\n* **No PII.** Output carries only sha256 hex digests +\n  structural indices + window timestamps. NEVER an\n  action_id-tied audit row payload.\n* **NEVER raises.**\n* **DB unavailable → exit 0** with skipped envelope.\n* **Bad args → exit 2.**\n\nUsage:\n\n    # Most recent root that covers the entry.\n    python scripts/generate_audit_inclusion_proof.py \\\n        --brokerage-id brk-1 --audit-entry-id <UUID> --json\n\n    # Explicit Merkle root.\n    python scripts/generate_audit_inclusion_proof.py \\\n        --brokerage-id brk-1 --audit-entry-id <UUID> \\\n        --merkle-root-id <UUID> --json\n\nExit codes:\n    0  — ok or skipped\n    1  — failed (e.g. audit entry not found)\n    2  — bad CLI arguments\n')
               STORE_NAME               0 (__doc__)

  38           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  40           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  41           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (json)
               STORE_NAME               4 (json)

  42           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (logging)
               STORE_NAME               5 (logging)

  43           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (os)
               STORE_NAME               6 (os)

  44           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              7 (sys)
               STORE_NAME               7 (sys)

  45           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              8 (datetime)
               IMPORT_FROM              8 (datetime)
               STORE_NAME               8 (datetime)
               IMPORT_FROM              9 (timezone)
               STORE_NAME               9 (timezone)
               POP_TOP

  46           LOAD_SMALL_INT           0
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

  49           LOAD_NAME                7 (sys)
               LOAD_ATTR               30 (stdout)
               LOAD_NAME                7 (sys)
               LOAD_ATTR               32 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              17 (_stream)

  50           NOP

  51   L2:     LOAD_NAME               17 (_stream)
               LOAD_ATTR               37 (reconfigure + NULL|self)
               LOAD_CONST               5 ('utf-8')
               LOAD_CONST               6 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  49   L4:     END_FOR
               POP_ITER

  56           LOAD_NAME                7 (sys)
               LOAD_ATTR               40 (path)
               LOAD_ATTR               43 (insert + NULL|self)
               LOAD_SMALL_INT           0
               LOAD_NAME                6 (os)
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
               CALL                     2
               POP_TOP

  59           LOAD_NAME                5 (logging)
               LOAD_ATTR               52 (getLogger)
               PUSH_NULL
               LOAD_CONST               8 ('pas.scripts.generate_audit_inclusion_proof')
               CALL                     1
               STORE_NAME              27 (logger)

  62           LOAD_CONST               9 (<code object __annotate__ at 0x0000018C17FA3960, file "scripts\generate_audit_inclusion_proof.py", line 62>)
               MAKE_FUNCTION
               LOAD_CONST              10 (<code object _now_iso at 0x0000018C18038DF0, file "scripts\generate_audit_inclusion_proof.py", line 62>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              28 (_now_iso)

  66           LOAD_CONST              11 ('proof')

  72           LOAD_CONST               2 (None)

  66           LOAD_CONST              12 ('window_start')

  73           LOAD_CONST               2 (None)

  66           LOAD_CONST              13 ('window_end')

  74           LOAD_CONST               2 (None)

  66           LOAD_CONST              14 ('warnings')

  75           LOAD_CONST               2 (None)

  66           LOAD_CONST              15 ('error_code')

  76           LOAD_CONST               2 (None)

  66           BUILD_MAP                5
               LOAD_CONST              16 (<code object __annotate__ at 0x0000018C180F4250, file "scripts\generate_audit_inclusion_proof.py", line 66>)
               MAKE_FUNCTION
               LOAD_CONST              17 (<code object _safe_envelope at 0x0000018C18038B70, file "scripts\generate_audit_inclusion_proof.py", line 66>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              29 (_safe_envelope)

  94           LOAD_CONST              18 ('merkle_root_id')

  98           LOAD_CONST               2 (None)

  94           BUILD_MAP                1
               LOAD_CONST              19 (<code object __annotate__ at 0x0000018C18024C30, file "scripts\generate_audit_inclusion_proof.py", line 94>)
               MAKE_FUNCTION
               LOAD_CONST              20 (<code object generate at 0x0000018C17D81580, file "scripts\generate_audit_inclusion_proof.py", line 94>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              30 (generate)

 141           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA34B0, file "scripts\generate_audit_inclusion_proof.py", line 141>)
               MAKE_FUNCTION
               LOAD_CONST              22 (<code object _build_parser at 0x0000018C180606F0, file "scripts\generate_audit_inclusion_proof.py", line 141>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              31 (_build_parser)

 169           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA3B40, file "scripts\generate_audit_inclusion_proof.py", line 169>)
               MAKE_FUNCTION
               LOAD_CONST              24 (<code object _print_summary at 0x0000018C17D8BF50, file "scripts\generate_audit_inclusion_proof.py", line 169>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              32 (_print_summary)

 192           LOAD_CONST              28 ((None,))
               LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA2970, file "scripts\generate_audit_inclusion_proof.py", line 192>)
               MAKE_FUNCTION
               LOAD_CONST              26 (<code object main at 0x0000018C17D50FF0, file "scripts\generate_audit_inclusion_proof.py", line 192>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              33 (main)

 216           LOAD_NAME               34 (__name__)
               LOAD_CONST              27 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 217           LOAD_NAME                7 (sys)
               LOAD_ATTR               70 (exit)
               PUSH_NULL
               LOAD_NAME               33 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 216   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  52           LOAD_NAME               19 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L8)
               NOT_TAKEN
               POP_TOP

  53   L7:     POP_EXCEPT
               JUMP_BACKWARD          246 (to L1)

  52   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "scripts\generate_audit_inclusion_proof.py", line 62>:
 62           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038DF0, file "scripts\generate_audit_inclusion_proof.py", line 62>:
 62           RESUME                   0

 63           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C180F4250, file "scripts\generate_audit_inclusion_proof.py", line 66>:
 66           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')

 68           LOAD_CONST               2 ('str')

 66           LOAD_CONST               3 ('brokerage_id')

 69           LOAD_CONST               4 ('Optional[str]')

 66           LOAD_CONST               5 ('audit_entry_id')

 70           LOAD_CONST               4 ('Optional[str]')

 66           LOAD_CONST               6 ('merkle_root_id')

 71           LOAD_CONST               4 ('Optional[str]')

 66           LOAD_CONST               7 ('proof')

 72           LOAD_CONST               8 ('Optional[Dict[str, Any]]')

 66           LOAD_CONST               9 ('window_start')

 73           LOAD_CONST               4 ('Optional[str]')

 66           LOAD_CONST              10 ('window_end')

 74           LOAD_CONST               4 ('Optional[str]')

 66           LOAD_CONST              11 ('warnings')

 75           LOAD_CONST              12 ('Optional[List[str]]')

 66           LOAD_CONST              13 ('error_code')

 76           LOAD_CONST               4 ('Optional[str]')

 66           LOAD_CONST              14 ('return')

 77           LOAD_CONST              15 ('Dict[str, Any]')

 66           BUILD_MAP               10
              RETURN_VALUE

Disassembly of <code object _safe_envelope at 0x0000018C18038B70, file "scripts\generate_audit_inclusion_proof.py", line 66>:
 66           RESUME                   0

 79           LOAD_CONST               0 ('phase')
              LOAD_CONST               1 ('PAS177')

 80           LOAD_CONST               2 ('tool')
              LOAD_CONST               3 ('generate_audit_inclusion_proof')

 81           LOAD_CONST               4 ('status')
              LOAD_FAST                0 (status)

 82           LOAD_CONST               5 ('brokerage_id')
              LOAD_FAST                1 (brokerage_id)

 83           LOAD_CONST               6 ('audit_entry_id')
              LOAD_FAST                2 (audit_entry_id)

 84           LOAD_CONST               7 ('merkle_root_id')
              LOAD_FAST                3 (merkle_root_id)

 85           LOAD_CONST               8 ('proof')
              LOAD_FAST                4 (proof)

 86           LOAD_CONST               9 ('window_start')
              LOAD_FAST                5 (window_start)

 87           LOAD_CONST              10 ('window_end')
              LOAD_FAST                6 (window_end)

 88           LOAD_CONST              11 ('warnings')
              LOAD_GLOBAL              1 (list + NULL)
              LOAD_FAST                7 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

 89           LOAD_CONST              12 ('error_code')
              LOAD_FAST_BORROW         8 (error_code)

 90           LOAD_CONST              13 ('generated_at')
              LOAD_GLOBAL              3 (_now_iso + NULL)
              CALL                     0

 78           BUILD_MAP               12
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "scripts\generate_audit_inclusion_proof.py", line 94>:
 94           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

 96           LOAD_CONST               2 ('str')

 94           LOAD_CONST               3 ('audit_entry_id')

 97           LOAD_CONST               2 ('str')

 94           LOAD_CONST               4 ('merkle_root_id')

 98           LOAD_CONST               5 ('Optional[str]')

 94           LOAD_CONST               6 ('return')

 99           LOAD_CONST               7 ('Dict[str, Any]')

 94           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object generate at 0x0000018C17D81580, file "scripts\generate_audit_inclusion_proof.py", line 94>:
 94           RESUME                   0

101           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('proof_for_audit_entry', 'verify_inclusion_proof'))
              IMPORT_NAME              0 (app.services.operator.merkle_inclusion_proofs)
              IMPORT_FROM              1 (proof_for_audit_entry)
              STORE_FAST               3 (proof_for_audit_entry)
              IMPORT_FROM              2 (verify_inclusion_proof)
              STORE_FAST               4 (verify_inclusion_proof)
              POP_TOP

105           LOAD_FAST_BORROW         3 (proof_for_audit_entry)
              PUSH_NULL

106           LOAD_FAST_BORROW         0 (brokerage_id)

107           LOAD_FAST_BORROW         1 (audit_entry_id)

108           LOAD_FAST_BORROW         2 (merkle_root_id)

105           LOAD_CONST               2 (('brokerage_id', 'audit_entry_id', 'merkle_root_id'))
              CALL_KW                  3
              STORE_FAST               5 (res)

110           LOAD_FAST_BORROW         5 (res)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               3 ('status')
              CALL                     1
              LOAD_CONST               4 ('ok')
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE       92 (to L3)
              NOT_TAKEN

111           LOAD_GLOBAL              9 (_safe_envelope + NULL)

112           LOAD_FAST_BORROW         5 (res)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               3 ('status')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               5 ('failed')

113   L1:     LOAD_FAST                0 (brokerage_id)

114           LOAD_FAST                1 (audit_entry_id)

115           LOAD_FAST                2 (merkle_root_id)

116           LOAD_GLOBAL             11 (list + NULL)
              LOAD_FAST_BORROW         5 (res)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               6 ('warnings')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L2:     CALL                     1

117           LOAD_FAST_BORROW         5 (res)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               7 ('error_code')
              CALL                     1

111           LOAD_CONST               8 (('status', 'brokerage_id', 'audit_entry_id', 'merkle_root_id', 'warnings', 'error_code'))
              CALL_KW                  6
              RETURN_VALUE

119   L3:     LOAD_FAST_BORROW         5 (res)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               9 ('proof')
              CALL                     1
              STORE_FAST               6 (proof)

123           LOAD_GLOBAL             13 (isinstance + NULL)
              LOAD_FAST_BORROW         6 (proof)
              LOAD_GLOBAL             14 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE        9 (to L4)
              NOT_TAKEN
              LOAD_FAST_BORROW         4 (verify_inclusion_proof)
              PUSH_NULL
              LOAD_FAST_BORROW         6 (proof)
              CALL                     1
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST              10 (None)
      L5:     STORE_FAST               7 (verdict)

124           LOAD_GLOBAL             13 (isinstance + NULL)
              LOAD_FAST_BORROW         6 (proof)
              LOAD_GLOBAL             14 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       12 (to L6)
              NOT_TAKEN
              LOAD_GLOBAL             15 (dict + NULL)
              LOAD_FAST_BORROW         6 (proof)
              CALL                     1
              JUMP_FORWARD             1 (to L7)
      L6:     LOAD_CONST              10 (None)
      L7:     STORE_FAST               8 (out_proof)

125           LOAD_FAST_BORROW         7 (verdict)
              TO_BOOL
              POP_JUMP_IF_FALSE       49 (to L8)
              NOT_TAKEN

127           LOAD_CONST              11 ('valid')
              LOAD_GLOBAL             17 (bool + NULL)
              LOAD_FAST_BORROW         7 (verdict)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST              11 ('valid')
              CALL                     1
              CALL                     1

128           LOAD_CONST               7 ('error_code')
              LOAD_FAST_BORROW         7 (verdict)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               7 ('error_code')
              CALL                     1

126           BUILD_MAP                2
              LOAD_FAST_BORROW         8 (out_proof)
              LOAD_CONST              12 ('self_verification')
              STORE_SUBSCR

130   L8:     LOAD_GLOBAL              9 (_safe_envelope + NULL)

131           LOAD_CONST               4 ('ok')

132           LOAD_FAST_BORROW         0 (brokerage_id)

133           LOAD_FAST_BORROW         1 (audit_entry_id)

134           LOAD_FAST_BORROW         5 (res)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST              13 ('merkle_root_id')
              CALL                     1

135           LOAD_FAST_BORROW         8 (out_proof)

136           LOAD_FAST_BORROW         5 (res)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST              14 ('window_start')
              CALL                     1

137           LOAD_FAST_BORROW         5 (res)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST              15 ('window_end')
              CALL                     1

130           LOAD_CONST              16 (('status', 'brokerage_id', 'audit_entry_id', 'merkle_root_id', 'proof', 'window_start', 'window_end'))
              CALL_KW                  7
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "scripts\generate_audit_inclusion_proof.py", line 141>:
141           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C180606F0, file "scripts\generate_audit_inclusion_proof.py", line 141>:
141           RESUME                   0

142           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

143           LOAD_CONST               0 ('generate_audit_inclusion_proof')

145           LOAD_CONST               1 ('PAS177 — Generate a Merkle inclusion proof for an audit entry. Read-only; never writes; never echoes PII / secrets / raw payloads.')

142           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

150           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

151           LOAD_CONST               3 ('--brokerage-id')
              LOAD_CONST               4 (True)

152           LOAD_CONST               5 ('Brokerage scope. NEVER an email / phone.')

150           LOAD_CONST               6 (('required', 'help'))
              CALL_KW                  3
              POP_TOP

154           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

155           LOAD_CONST               7 ('--audit-entry-id')
              LOAD_CONST               4 (True)

156           LOAD_CONST               8 ('The action_id of the audit row to prove inclusion for.')

154           LOAD_CONST               6 (('required', 'help'))
              CALL_KW                  3
              POP_TOP

158           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

159           LOAD_CONST               9 ('--merkle-root-id')
              LOAD_CONST              10 (None)

160           LOAD_CONST              11 ('Optional explicit Merkle root row id. Default: most-recent root covering the entry.')

158           LOAD_CONST              12 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

162           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

163           LOAD_CONST              13 ('--json')
              LOAD_CONST              14 ('store_true')

164           LOAD_CONST              15 ('Emit JSON on stdout instead of the human summary.')

162           LOAD_CONST              16 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

166           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "scripts\generate_audit_inclusion_proof.py", line 169>:
169           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('env')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('None')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _print_summary at 0x0000018C17D8BF50, file "scripts\generate_audit_inclusion_proof.py", line 169>:
169           RESUME                   0

170           LOAD_GLOBAL              1 (print + NULL)

171           LOAD_CONST               0 ('[PAS177/generate_audit_inclusion_proof] status=')

172           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST               1 ('status')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               2 (' brokerage_id=')

173           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST               3 ('brokerage_id')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' audit_entry_id=')

174           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST               5 ('audit_entry_id')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' merkle_root_id=')

175           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST               7 ('merkle_root_id')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' window_start=')

176           LOAD_FAST_BORROW         0 (env)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               9 ('window_start')
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST              10 (' window_end=')

177           LOAD_FAST_BORROW         0 (env)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST              11 ('window_end')
              CALL                     1
              FORMAT_SIMPLE

171           BUILD_STRING            12

170           CALL                     1
              POP_TOP

179           LOAD_FAST_BORROW         0 (env)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST              12 ('proof')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L1:     STORE_FAST               1 (p)

180           LOAD_GLOBAL              5 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (p)
              LOAD_GLOBAL              6 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE      128 (to L4)
              NOT_TAKEN

181           LOAD_FAST_BORROW         1 (p)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST              13 ('self_verification')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L2:     STORE_FAST               2 (sv)

182           LOAD_GLOBAL              1 (print + NULL)

183           LOAD_CONST              14 ('  leaf_index=')
              LOAD_FAST_BORROW         1 (p)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST              15 ('leaf_index')
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST              16 (' leaf_count=')

184           LOAD_FAST_BORROW         1 (p)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST              17 ('leaf_count')
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST              18 (' merkle_root_prefix=')

185           LOAD_FAST_BORROW         1 (p)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST              19 ('merkle_root')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST              20 ('')
      L3:     LOAD_CONST              21 (slice(None, 12, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              22 ('... self_verification.valid=')

186           LOAD_FAST_BORROW         2 (sv)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST              23 ('valid')
              CALL                     1
              FORMAT_SIMPLE

183           BUILD_STRING             8

182           CALL                     1
              POP_TOP

188   L4:     LOAD_FAST_BORROW         0 (env)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST              24 ('warnings')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L5:     LOAD_CONST              25 (slice(None, 10, None))
              BINARY_OP               26 ([])
              GET_ITER
      L6:     FOR_ITER                17 (to L7)
              STORE_FAST               3 (w)

189           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              26 ('  warn: ')
              LOAD_FAST_BORROW         3 (w)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L6)

188   L7:     END_FOR
              POP_ITER
              LOAD_CONST              27 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "scripts\generate_audit_inclusion_proof.py", line 192>:
192           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17D50FF0, file "scripts\generate_audit_inclusion_proof.py", line 192>:
 192            RESUME                   0

 193            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 194            NOP

 195    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 199    L2:     LOAD_GLOBAL             11 (generate + NULL)

 200            LOAD_FAST                2 (args)
                LOAD_ATTR               12 (brokerage_id)

 201            LOAD_FAST                2 (args)
                LOAD_ATTR               14 (audit_entry_id)

 202            LOAD_FAST                2 (args)
                LOAD_ATTR               16 (merkle_root_id)

 199            LOAD_CONST               2 (('brokerage_id', 'audit_entry_id', 'merkle_root_id'))
                CALL_KW                  3
                STORE_FAST               4 (env)

 205            LOAD_FAST                2 (args)
                LOAD_ATTR               18 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       36 (to L3)
                NOT_TAKEN

 206            LOAD_GLOBAL             21 (print + NULL)
                LOAD_GLOBAL             18 (json)
                LOAD_ATTR               22 (dumps)
                PUSH_NULL
                LOAD_FAST                4 (env)
                LOAD_SMALL_INT           2
                LOAD_CONST               3 (True)
                LOAD_CONST               4 (('indent', 'sort_keys'))
                CALL_KW                  3
                CALL                     1
                POP_TOP
                JUMP_FORWARD            11 (to L4)

 208    L3:     LOAD_GLOBAL             25 (_print_summary + NULL)
                LOAD_FAST                4 (env)
                CALL                     1
                POP_TOP

 210    L4:     LOAD_FAST                4 (env)
                LOAD_ATTR               27 (get + NULL|self)
                LOAD_CONST               5 ('status')
                CALL                     1
                STORE_FAST               5 (status)

 211            LOAD_FAST                5 (status)
                LOAD_CONST               6 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_TRUE         8 (to L5)
                NOT_TAKEN
                LOAD_FAST                5 (status)
                LOAD_CONST               7 ('skipped')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN

 212    L5:     LOAD_SMALL_INT           0
                RETURN_VALUE

 213    L6:     LOAD_SMALL_INT           1
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

 196            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L16)
                NOT_TAKEN
                STORE_FAST               3 (e)

 197    L8:     LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                LOAD_CONST               8 ((0, None))
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

 196   L16:     RERAISE                  0

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
