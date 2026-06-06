# scripts_readiness/verify_operator_audit_chain

- **pyc:** `scripts\__pycache__\verify_operator_audit_chain.cpython-314.pyc`
- **expected source path (absent):** `scripts/verify_operator_audit_chain.py`
- **co_filename (from bytecode):** `scripts\verify_operator_audit_chain.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS176 — Operator-runnable audit chain verifier CLI.

Verifies the PAS174 operator audit chain over a time window,
optionally persists the Merkle root to the v24 table, and
optionally emits a structural Slack chain-break alert via
the PAS171 pilot transport. Read-only by default; `--execute`
required to persist + alert.

Doctrine:

* **Dry-run by default.** Without ``--execute`` the script
  only reads + prints; nothing is persisted, no Slack alert
  fires.
* **Operator-driven.** No scheduler / cron. The script is
  meant for manual or operator-scripted invocation.
* **Read-only on the audit log itself.** The script never
  updates / deletes audit rows. It writes only to
  ``pas_audit_merkle_roots`` (and only when ``--execute``).
* **No autonomous remediation.** On a detected break the
  script surfaces the structural verdict + optionally
  POSTs to Slack. It does NOT attempt to fix anything.
* **Bounded.** Window-hours clamped to ``[1, 720]`` (30
  days). Listing is hard-capped by the underlying
  verifier service.
* **NEVER raises.**
* **DB unavailable → exit 0** with skipped envelope.
* **Bad args → exit 2.**

Usage:

    # Dry-run, default 24-hour window, no Slack alert.
    python scripts/verify_operator_audit_chain.py

    # Persist Merkle root + emit Slack alert on break.
    python scripts/verify_operator_audit_chain.py --execute

    # Per-brokerage window.
    python scripts/verify_operator_audit_chain.py \
        --brokerage-id brk-pilot --window-hours 12 --execute
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.services.operator.audit_chain_verifier`, `argparse`, `datetime`, `emit_chain_break_alert`, `json`, `logging`, `os`, `persist_merkle_root`, `sys`, `timezone`, `typing`, `verify_window`

## Classes

_none_

## Functions / methods

`__annotate__`, `_build_parser`, `_clamp`, `_now_iso`, `_print_summary`, `_safe_envelope`, `main`, `verify`

## Env-key candidates

`PAS176`

## String constants (redacted where noted)

- '\nPAS176 — Operator-runnable audit chain verifier CLI.\n\nVerifies the PAS174 operator audit chain over a time window,\noptionally persists the Merkle root to the v24 table, and\noptionally emits a structural Slack chain-break alert via\nthe PAS171 pilot transport. Read-only by default; `--execute`\nrequired to persist + alert.\n\nDoctrine:\n\n* **Dry-run by default.** Without ``--execute`` the script\n  only reads + prints; nothing is persisted, no Slack alert\n  fires.\n* **Operator-driven.** No scheduler / cron. The script is\n  meant for manual or operator-scripted invocation.\n* **Read-only on the audit log itself.** The script never\n  updates / deletes audit rows. It writes only to\n  ``pas_audit_merkle_roots`` (and only when ``--execute``).\n* **No autonomous remediation.** On a detected break the\n  script surfaces the structural verdict + optionally\n  POSTs to Slack. It does NOT attempt to fix anything.\n* **Bounded.** Window-hours clamped to ``[1, 720]`` (30\n  days). Listing is hard-capped by the underlying\n  verifier service.\n* **NEVER raises.**\n* **DB unavailable → exit 0** with skipped envelope.\n* **Bad args → exit 2.**\n\nUsage:\n\n    # Dry-run, default 24-hour window, no Slack alert.\n    python scripts/verify_operator_audit_chain.py\n\n    # Persist Merkle root + emit Slack alert on break.\n    python scripts/verify_operator_audit_chain.py --execute\n\n    # Per-brokerage window.\n    python scripts/verify_operator_audit_chain.py \\\n        --brokerage-id brk-pilot --window-hours 12 --execute\n'
- 'utf-8'
- 'pas.scripts.verify_operator_audit_chain'
- 'verification'
- 'merkle_persist'
- 'slack_alert'
- 'warnings'
- 'error_code'
- 'brokerage_id'
- 'window_hours'
- 'dry_run'
- 'generated_by'
- 'return'
- 'str'
- 'seconds'
- 'value'
- 'Any'
- 'int'
- 'default'
- 'status'
- 'bool'
- 'Optional[str]'
- 'Optional[Dict[str, Any]]'
- 'Optional[List[str]]'
- 'Dict[str, Any]'
- 'phase'
- 'PAS176'
- 'verifier'
- 'operator_audit_chain'
- 'generated_at'
- 'Run the chain verifier over the given window and\noptionally persist + alert. NEVER raises.'
- 'argparse.ArgumentParser'
- 'verify_operator_audit_chain'
- 'PAS176 — Verify the operator audit chain over a time window. Read-only by default; --execute persists the Merkle root AND emits a Slack chain-break alert when the chain is degraded. Never modifies audit rows themselves.'
- '--brokerage-id'
- 'Scope verification to a single brokerage. Default: cross-tenant operator window.'
- '--window-hours'
- 'Window length in hours (clamped to ['
- '], default '
- '--execute'
- 'store_true'
- 'Persist the Merkle root + emit Slack chain-break alert. Without this flag the script is read-only.'
- '--generated-by'
- 'Operator identifier for the audit trail (bounded ≤200 chars). NEVER an email or phone.'
- '--json'
- 'Emit JSON on stdout instead of the human summary.'
- 'env'
- 'None'
- '[PAS176/verify_operator_audit_chain] status='
- ' dry_run='
- ' brokerage_id='
- ' window_hours='
- ' chain_status='
- 'chain_status'
- ' rows_in_window='
- 'rows_in_window'
- ' breaks_count='
- 'breaks_count'
- ' merkle_root='
- 'merkle_root'
- '...'
- '  merkle_persist='
- '  slack_alert='
- '  warn: '
- 'argv'

## Disassembly

```
   0           RESUME                   0

   1           LOAD_CONST               0 ('\nPAS176 — Operator-runnable audit chain verifier CLI.\n\nVerifies the PAS174 operator audit chain over a time window,\noptionally persists the Merkle root to the v24 table, and\noptionally emits a structural Slack chain-break alert via\nthe PAS171 pilot transport. Read-only by default; `--execute`\nrequired to persist + alert.\n\nDoctrine:\n\n* **Dry-run by default.** Without ``--execute`` the script\n  only reads + prints; nothing is persisted, no Slack alert\n  fires.\n* **Operator-driven.** No scheduler / cron. The script is\n  meant for manual or operator-scripted invocation.\n* **Read-only on the audit log itself.** The script never\n  updates / deletes audit rows. It writes only to\n  ``pas_audit_merkle_roots`` (and only when ``--execute``).\n* **No autonomous remediation.** On a detected break the\n  script surfaces the structural verdict + optionally\n  POSTs to Slack. It does NOT attempt to fix anything.\n* **Bounded.** Window-hours clamped to ``[1, 720]`` (30\n  days). Listing is hard-capped by the underlying\n  verifier service.\n* **NEVER raises.**\n* **DB unavailable → exit 0** with skipped envelope.\n* **Bad args → exit 2.**\n\nUsage:\n\n    # Dry-run, default 24-hour window, no Slack alert.\n    python scripts/verify_operator_audit_chain.py\n\n    # Persist Merkle root + emit Slack alert on break.\n    python scripts/verify_operator_audit_chain.py --execute\n\n    # Per-brokerage window.\n    python scripts/verify_operator_audit_chain.py \\\n        --brokerage-id brk-pilot --window-hours 12 --execute\n')
               STORE_NAME               0 (__doc__)

  43           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  45           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  46           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (json)
               STORE_NAME               4 (json)

  47           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (logging)
               STORE_NAME               5 (logging)

  48           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (os)
               STORE_NAME               6 (os)

  49           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              7 (sys)
               STORE_NAME               7 (sys)

  50           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              8 (datetime)
               IMPORT_FROM              8 (datetime)
               STORE_NAME               8 (datetime)
               IMPORT_FROM              9 (timezone)
               STORE_NAME               9 (timezone)
               POP_TOP

  51           LOAD_SMALL_INT           0
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

  54           LOAD_NAME                7 (sys)
               LOAD_ATTR               30 (stdout)
               LOAD_NAME                7 (sys)
               LOAD_ATTR               32 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              17 (_stream)

  55           NOP

  56   L2:     LOAD_NAME               17 (_stream)
               LOAD_ATTR               37 (reconfigure + NULL|self)
               LOAD_CONST               5 ('utf-8')
               LOAD_CONST               6 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  54   L4:     END_FOR
               POP_ITER

  61           LOAD_NAME                7 (sys)
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

  64           LOAD_NAME                5 (logging)
               LOAD_ATTR               52 (getLogger)
               PUSH_NULL
               LOAD_CONST               8 ('pas.scripts.verify_operator_audit_chain')
               CALL                     1
               STORE_NAME              27 (logger)

  67           LOAD_SMALL_INT          24
               STORE_NAME              28 (_DEFAULT_WINDOW_HOURS)

  68           LOAD_SMALL_INT           1
               STORE_NAME              29 (_MIN_WINDOW_HOURS)

  69           LOAD_CONST              34 (720)
               STORE_NAME              30 (_MAX_WINDOW_HOURS)

  72           LOAD_CONST               9 (<code object __annotate__ at 0x0000018C17FA1E30, file "scripts\verify_operator_audit_chain.py", line 72>)
               MAKE_FUNCTION
               LOAD_CONST              10 (<code object _now_iso at 0x0000018C180392F0, file "scripts\verify_operator_audit_chain.py", line 72>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              31 (_now_iso)

  76           LOAD_CONST              11 (<code object __annotate__ at 0x0000018C18025C30, file "scripts\verify_operator_audit_chain.py", line 76>)
               MAKE_FUNCTION
               LOAD_CONST              12 (<code object _clamp at 0x0000018C18038670, file "scripts\verify_operator_audit_chain.py", line 76>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              32 (_clamp)

  88           LOAD_CONST              13 ('verification')

  94           LOAD_CONST               2 (None)

  88           LOAD_CONST              14 ('merkle_persist')

  95           LOAD_CONST               2 (None)

  88           LOAD_CONST              15 ('slack_alert')

  96           LOAD_CONST               2 (None)

  88           LOAD_CONST              16 ('warnings')

  97           LOAD_CONST               2 (None)

  88           LOAD_CONST              17 ('error_code')

  98           LOAD_CONST               2 (None)

  88           BUILD_MAP                5
               LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FBFEE0, file "scripts\verify_operator_audit_chain.py", line 88>)
               MAKE_FUNCTION
               LOAD_CONST              19 (<code object _safe_envelope at 0x0000018C17FE1530, file "scripts\verify_operator_audit_chain.py", line 88>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              33 (_safe_envelope)

 116           LOAD_CONST              20 ('brokerage_id')

 118           LOAD_CONST               2 (None)

 116           LOAD_CONST              21 ('window_hours')

 119           LOAD_NAME               28 (_DEFAULT_WINDOW_HOURS)

 116           LOAD_CONST              22 ('dry_run')

 120           LOAD_CONST              23 (True)

 116           LOAD_CONST              24 ('generated_by')

 121           LOAD_CONST               2 (None)

 116           BUILD_MAP                4
               LOAD_CONST              25 (<code object __annotate__ at 0x0000018C18026430, file "scripts\verify_operator_audit_chain.py", line 116>)
               MAKE_FUNCTION
               LOAD_CONST              26 (<code object verify at 0x0000018C182E2600, file "scripts\verify_operator_audit_chain.py", line 116>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              34 (verify)

 159           LOAD_CONST              27 (<code object __annotate__ at 0x0000018C17FA21F0, file "scripts\verify_operator_audit_chain.py", line 159>)
               MAKE_FUNCTION
               LOAD_CONST              28 (<code object _build_parser at 0x0000018C17EC4280, file "scripts\verify_operator_audit_chain.py", line 159>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              35 (_build_parser)

 193           LOAD_CONST              29 (<code object __annotate__ at 0x0000018C17FA2E20, file "scripts\verify_operator_audit_chain.py", line 193>)
               MAKE_FUNCTION
               LOAD_CONST              30 (<code object _print_summary at 0x0000018C18646C00, file "scripts\verify_operator_audit_chain.py", line 193>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              36 (_print_summary)

 216           LOAD_CONST              35 ((None,))
               LOAD_CONST              31 (<code object __annotate__ at 0x0000018C17FA2970, file "scripts\verify_operator_audit_chain.py", line 216>)
               MAKE_FUNCTION
               LOAD_CONST              32 (<code object main at 0x0000018C181B2930, file "scripts\verify_operator_audit_chain.py", line 216>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              37 (main)

 238           LOAD_NAME               38 (__name__)
               LOAD_CONST              33 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 239           LOAD_NAME                7 (sys)
               LOAD_ATTR               78 (exit)
               PUSH_NULL
               LOAD_NAME               37 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 238   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  57           LOAD_NAME               19 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  58   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          265 (to L1)

  57   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "scripts\verify_operator_audit_chain.py", line 72>:
 72           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C180392F0, file "scripts\verify_operator_audit_chain.py", line 72>:
 72           RESUME                   0

 73           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C18025C30, file "scripts\verify_operator_audit_chain.py", line 76>:
 76           RESUME                   0
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

Disassembly of <code object _clamp at 0x0000018C18038670, file "scripts\verify_operator_audit_chain.py", line 76>:
  76           RESUME                   0

  77           NOP

  78   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               4 (v)

  81   L2:     LOAD_FAST_LOAD_FAST     65 (v, lo)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

  82           LOAD_FAST                1 (lo)
               RETURN_VALUE

  83   L3:     LOAD_FAST_LOAD_FAST     66 (v, hi)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN

  84           LOAD_FAST                2 (hi)
               RETURN_VALUE

  85   L4:     LOAD_FAST                4 (v)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

  79           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L7)
               NOT_TAKEN
               POP_TOP

  80           LOAD_FAST                3 (default)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

  79   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FBFEE0, file "scripts\verify_operator_audit_chain.py", line 88>:
 88           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')

 90           LOAD_CONST               2 ('str')

 88           LOAD_CONST               3 ('dry_run')

 91           LOAD_CONST               4 ('bool')

 88           LOAD_CONST               5 ('brokerage_id')

 92           LOAD_CONST               6 ('Optional[str]')

 88           LOAD_CONST               7 ('window_hours')

 93           LOAD_CONST               8 ('int')

 88           LOAD_CONST               9 ('verification')

 94           LOAD_CONST              10 ('Optional[Dict[str, Any]]')

 88           LOAD_CONST              11 ('merkle_persist')

 95           LOAD_CONST              10 ('Optional[Dict[str, Any]]')

 88           LOAD_CONST              12 ('slack_alert')

 96           LOAD_CONST              10 ('Optional[Dict[str, Any]]')

 88           LOAD_CONST              13 ('warnings')

 97           LOAD_CONST              14 ('Optional[List[str]]')

 88           LOAD_CONST              15 ('error_code')

 98           LOAD_CONST               6 ('Optional[str]')

 88           LOAD_CONST              16 ('return')

 99           LOAD_CONST              17 ('Dict[str, Any]')

 88           BUILD_MAP               10
              RETURN_VALUE

Disassembly of <code object _safe_envelope at 0x0000018C17FE1530, file "scripts\verify_operator_audit_chain.py", line 88>:
 88           RESUME                   0

101           LOAD_CONST               0 ('phase')
              LOAD_CONST               1 ('PAS176')

102           LOAD_CONST               2 ('verifier')
              LOAD_CONST               3 ('operator_audit_chain')

103           LOAD_CONST               4 ('status')
              LOAD_FAST                0 (status)

104           LOAD_CONST               5 ('dry_run')
              LOAD_GLOBAL              1 (bool + NULL)
              LOAD_FAST_BORROW         1 (dry_run)
              CALL                     1

105           LOAD_CONST               6 ('brokerage_id')
              LOAD_FAST                2 (brokerage_id)

106           LOAD_CONST               7 ('window_hours')
              LOAD_FAST                3 (window_hours)

107           LOAD_CONST               8 ('verification')
              LOAD_FAST                4 (verification)

108           LOAD_CONST               9 ('merkle_persist')
              LOAD_FAST                5 (merkle_persist)

109           LOAD_CONST              10 ('slack_alert')
              LOAD_FAST                6 (slack_alert)

110           LOAD_CONST              11 ('warnings')
              LOAD_GLOBAL              3 (list + NULL)
              LOAD_FAST                7 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

111           LOAD_CONST              12 ('error_code')
              LOAD_FAST_BORROW         8 (error_code)

112           LOAD_CONST              13 ('generated_at')
              LOAD_GLOBAL              5 (_now_iso + NULL)
              CALL                     0

100           BUILD_MAP               12
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026430, file "scripts\verify_operator_audit_chain.py", line 116>:
116           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

118           LOAD_CONST               2 ('Optional[str]')

116           LOAD_CONST               3 ('window_hours')

119           LOAD_CONST               4 ('int')

116           LOAD_CONST               5 ('dry_run')

120           LOAD_CONST               6 ('bool')

116           LOAD_CONST               7 ('generated_by')

121           LOAD_CONST               2 ('Optional[str]')

116           LOAD_CONST               8 ('return')

122           LOAD_CONST               9 ('Dict[str, Any]')

116           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object verify at 0x0000018C182E2600, file "scripts\verify_operator_audit_chain.py", line 116>:
116           RESUME                   0

125           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('verify_window', 'persist_merkle_root', 'emit_chain_break_alert'))
              IMPORT_NAME              0 (app.services.operator.audit_chain_verifier)
              IMPORT_FROM              1 (verify_window)
              STORE_FAST               4 (verify_window)
              IMPORT_FROM              2 (persist_merkle_root)
              STORE_FAST               5 (persist_merkle_root)
              IMPORT_FROM              3 (emit_chain_break_alert)
              STORE_FAST               6 (emit_chain_break_alert)
              POP_TOP

130           LOAD_GLOBAL              9 (_clamp + NULL)
              LOAD_FAST_BORROW         1 (window_hours)
              LOAD_GLOBAL             10 (_MIN_WINDOW_HOURS)
              LOAD_GLOBAL             12 (_MAX_WINDOW_HOURS)
              LOAD_GLOBAL             14 (_DEFAULT_WINDOW_HOURS)
              CALL                     4
              STORE_FAST               7 (hours)

131           LOAD_GLOBAL             17 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (brokerage_id)
              LOAD_GLOBAL             18 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       39 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         0 (brokerage_id)
              LOAD_ATTR               21 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_FALSE       17 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         0 (brokerage_id)
              LOAD_ATTR               21 (strip + NULL|self)
              CALL                     0
              JUMP_FORWARD             1 (to L2)
      L1:     LOAD_CONST               2 (None)
      L2:     STORE_FAST               8 (bid)

133           LOAD_FAST_BORROW         4 (verify_window)
              PUSH_NULL
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 135 (bid, hours)
              LOAD_CONST               3 (('brokerage_id', 'window_hours'))
              CALL_KW                  2
              STORE_FAST               9 (verification)

134           LOAD_CONST               2 (None)
              STORE_FAST              10 (persist_env)

135           LOAD_CONST               2 (None)
              STORE_FAST              11 (alert_env)

137           LOAD_FAST_BORROW         2 (dry_run)
              TO_BOOL
              POP_JUMP_IF_TRUE        18 (to L3)
              NOT_TAKEN

140           LOAD_FAST_BORROW         5 (persist_merkle_root)
              PUSH_NULL

141           LOAD_FAST_BORROW_LOAD_FAST_BORROW 147 (verification, generated_by)

140           LOAD_CONST               4 (('generated_by',))
              CALL_KW                  2
              STORE_FAST              10 (persist_env)

143           LOAD_FAST_BORROW         6 (emit_chain_break_alert)
              PUSH_NULL
              LOAD_FAST_BORROW         9 (verification)
              CALL                     1
              STORE_FAST              11 (alert_env)

145   L3:     LOAD_FAST_BORROW         9 (verification)
              LOAD_ATTR               23 (get + NULL|self)
              LOAD_CONST               5 ('status')
              CALL                     1
              LOAD_CONST               6 ('ok')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               6 ('ok')
              JUMP_FORWARD            16 (to L5)
      L4:     LOAD_FAST_BORROW         9 (verification)
              LOAD_ATTR               23 (get + NULL|self)
              LOAD_CONST               5 ('status')
              CALL                     1
      L5:     STORE_FAST              12 (overall_status)

146           LOAD_GLOBAL             25 (_safe_envelope + NULL)

147           LOAD_FAST               12 (overall_status)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L6)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               6 ('ok')

148   L6:     LOAD_FAST                2 (dry_run)

149           LOAD_FAST                8 (bid)

150           LOAD_FAST                7 (hours)

151           LOAD_FAST                9 (verification)

152           LOAD_FAST               10 (persist_env)

153           LOAD_FAST               11 (alert_env)

154           LOAD_GLOBAL             27 (list + NULL)
              LOAD_FAST_BORROW         9 (verification)
              LOAD_ATTR               23 (get + NULL|self)
              LOAD_CONST               7 ('warnings')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L7)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L7:     CALL                     1

155           LOAD_FAST_BORROW         9 (verification)
              LOAD_ATTR               23 (get + NULL|self)
              LOAD_CONST               8 ('error_code')
              CALL                     1

146           LOAD_CONST               9 (('status', 'dry_run', 'brokerage_id', 'window_hours', 'verification', 'merkle_persist', 'slack_alert', 'warnings', 'error_code'))
              CALL_KW                  9
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "scripts\verify_operator_audit_chain.py", line 159>:
159           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C17EC4280, file "scripts\verify_operator_audit_chain.py", line 159>:
159           RESUME                   0

160           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

161           LOAD_CONST               0 ('verify_operator_audit_chain')

163           LOAD_CONST               1 ('PAS176 — Verify the operator audit chain over a time window. Read-only by default; --execute persists the Merkle root AND emits a Slack chain-break alert when the chain is degraded. Never modifies audit rows themselves.')

160           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

170           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

171           LOAD_CONST               3 ('--brokerage-id')
              LOAD_CONST               4 (None)

172           LOAD_CONST               5 ('Scope verification to a single brokerage. Default: cross-tenant operator window.')

170           LOAD_CONST               6 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

174           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

175           LOAD_CONST               7 ('--window-hours')
              LOAD_GLOBAL              6 (int)
              LOAD_GLOBAL              8 (_DEFAULT_WINDOW_HOURS)

176           LOAD_CONST               8 ('Window length in hours (clamped to [')
              LOAD_GLOBAL             10 (_MIN_WINDOW_HOURS)
              FORMAT_SIMPLE
              LOAD_CONST               9 (',')
              LOAD_GLOBAL             12 (_MAX_WINDOW_HOURS)
              FORMAT_SIMPLE
              LOAD_CONST              10 ('], default ')
              LOAD_GLOBAL              8 (_DEFAULT_WINDOW_HOURS)
              FORMAT_SIMPLE
              LOAD_CONST              11 (').')
              BUILD_STRING             7

174           LOAD_CONST              12 (('type', 'default', 'help'))
              CALL_KW                  4
              POP_TOP

178           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

179           LOAD_CONST              13 ('--execute')
              LOAD_CONST              14 ('store_true')

180           LOAD_CONST              15 ('Persist the Merkle root + emit Slack chain-break alert. Without this flag the script is read-only.')

178           LOAD_CONST              16 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

182           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

183           LOAD_CONST              17 ('--generated-by')
              LOAD_CONST               4 (None)

184           LOAD_CONST              18 ('Operator identifier for the audit trail (bounded ≤200 chars). NEVER an email or phone.')

182           LOAD_CONST               6 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

186           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

187           LOAD_CONST              19 ('--json')
              LOAD_CONST              14 ('store_true')

188           LOAD_CONST              20 ('Emit JSON on stdout instead of the human summary.')

186           LOAD_CONST              16 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

190           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "scripts\verify_operator_audit_chain.py", line 193>:
193           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C18646C00, file "scripts\verify_operator_audit_chain.py", line 193>:
193           RESUME                   0

194           LOAD_FAST_BORROW         0 (env)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               0 ('verification')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L1:     STORE_FAST               1 (v)

195           LOAD_FAST_BORROW         0 (env)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               1 ('merkle_persist')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L2:     STORE_FAST               2 (p)

196           LOAD_FAST_BORROW         0 (env)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               2 ('slack_alert')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L3:     STORE_FAST               3 (a)

197           LOAD_GLOBAL              3 (print + NULL)

198           LOAD_CONST               3 ('[PAS176/verify_operator_audit_chain] status=')

199           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST               4 ('status')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               5 (' dry_run=')

200           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST               6 ('dry_run')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               7 (' brokerage_id=')

201           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST               8 ('brokerage_id')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               9 (' window_hours=')

202           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST              10 ('window_hours')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              11 (' chain_status=')

203           LOAD_FAST_BORROW         1 (v)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              12 ('chain_status')
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST              13 (' rows_in_window=')

204           LOAD_FAST_BORROW         1 (v)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              14 ('rows_in_window')
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST              15 (' breaks_count=')

205           LOAD_FAST_BORROW         1 (v)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              16 ('breaks_count')
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST              17 (' merkle_root=')

206           LOAD_FAST_BORROW         1 (v)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              18 ('merkle_root')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST              19 ('')
      L4:     LOAD_CONST              20 (slice(None, 12, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              21 ('...')

198           BUILD_STRING            17

197           CALL                     1
              POP_TOP

208           LOAD_FAST_BORROW         2 (p)
              TO_BOOL
              POP_JUMP_IF_FALSE       30 (to L5)
              NOT_TAKEN

209           LOAD_GLOBAL              3 (print + NULL)
              LOAD_CONST              22 ('  merkle_persist=')
              LOAD_FAST_BORROW         2 (p)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               4 ('status')
              CALL                     1
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP

210   L5:     LOAD_FAST_BORROW         3 (a)
              TO_BOOL
              POP_JUMP_IF_FALSE       30 (to L6)
              NOT_TAKEN

211           LOAD_GLOBAL              3 (print + NULL)
              LOAD_CONST              23 ('  slack_alert=')
              LOAD_FAST_BORROW         3 (a)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               4 ('status')
              CALL                     1
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP

212   L6:     LOAD_FAST_BORROW         0 (env)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              24 ('warnings')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L7)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L7:     LOAD_CONST              25 (slice(None, 10, None))
              BINARY_OP               26 ([])
              GET_ITER
      L8:     FOR_ITER                17 (to L9)
              STORE_FAST               4 (w)

213           LOAD_GLOBAL              3 (print + NULL)
              LOAD_CONST              26 ('  warn: ')
              LOAD_FAST_BORROW         4 (w)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L8)

212   L9:     END_FOR
              POP_ITER
              LOAD_CONST              27 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "scripts\verify_operator_audit_chain.py", line 216>:
216           RESUME                   0
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

Disassembly of <code object main at 0x0000018C181B2930, file "scripts\verify_operator_audit_chain.py", line 216>:
 216            RESUME                   0

 217            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 218            NOP

 219    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 223    L2:     LOAD_GLOBAL             11 (verify + NULL)

 224            LOAD_FAST                2 (args)
                LOAD_ATTR               12 (brokerage_id)

 225            LOAD_FAST                2 (args)
                LOAD_ATTR               14 (window_hours)

 226            LOAD_FAST                2 (args)
                LOAD_ATTR               16 (execute)
                TO_BOOL
                UNARY_NOT

 227            LOAD_FAST                2 (args)
                LOAD_ATTR               18 (generated_by)

 223            LOAD_CONST               2 (('brokerage_id', 'window_hours', 'dry_run', 'generated_by'))
                CALL_KW                  4
                STORE_FAST               4 (env)

 230            LOAD_FAST                2 (args)
                LOAD_ATTR               20 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       37 (to L3)
                NOT_TAKEN

 231            LOAD_GLOBAL             23 (print + NULL)
                LOAD_GLOBAL             20 (json)
                LOAD_ATTR               24 (dumps)
                PUSH_NULL
                LOAD_FAST                4 (env)
                LOAD_SMALL_INT           2
                LOAD_CONST               3 (True)
                LOAD_CONST               4 (('indent', 'sort_keys'))
                CALL_KW                  3
                CALL                     1
                POP_TOP

 235            LOAD_SMALL_INT           0
                RETURN_VALUE

 233    L3:     LOAD_GLOBAL             27 (_print_summary + NULL)
                LOAD_FAST                4 (env)
                CALL                     1
                POP_TOP

 235            LOAD_SMALL_INT           0
                RETURN_VALUE

  --    L4:     PUSH_EXC_INFO

 220            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L13)
                NOT_TAKEN
                STORE_FAST               3 (e)

 221    L5:     LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                LOAD_CONST               5 ((0, None))
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN
                LOAD_SMALL_INT           2
                JUMP_FORWARD            30 (to L10)
        L6:     LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
        L7:     NOT_TAKEN
        L8:     POP_TOP
                LOAD_SMALL_INT           0
        L9:     CALL                     1
       L10:     SWAP                     2
       L11:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RETURN_VALUE

  --   L12:     LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 220   L13:     RERAISE                  0

  --   L14:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L4 [0]
  L4 to L5 -> L14 [1] lasti
  L5 to L7 -> L12 [1] lasti
  L8 to L10 -> L12 [1] lasti
  L10 to L11 -> L14 [1] lasti
  L12 to L14 -> L14 [1] lasti
```
