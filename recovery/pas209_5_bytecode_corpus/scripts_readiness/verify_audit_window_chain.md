# scripts_readiness/verify_audit_window_chain

- **pyc:** `scripts\__pycache__\verify_audit_window_chain.cpython-314.pyc`
- **expected source path (absent):** `scripts/verify_audit_window_chain.py`
- **co_filename (from bytecode):** `scripts/verify_audit_window_chain.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS178 — Operator-runnable cross-window chain verifier CLI.

Read-only by default; ``--alert`` explicitly opts in to firing
a Slack chain-break alert via PAS171's pilot transport. NEVER
writes to any audit / Merkle / chain table. NEVER auto-
remediates.

Doctrine:

* **Read-only.** No DB writes. Verification result emitted to
  stdout as a structural envelope.
* **No auto-alert.** Slack alert fires ONLY when ``--alert``
  is passed AND the chain is degraded AND the operator has
  configured ``PAS_ALERT_SLACK_WEBHOOK_URL``.
* **No auto-repair.** A break is surfaced; the operator
  decides whether to file a P0.
* **NEVER raises.**
* **DB unavailable → exit 0** with skipped envelope.
* **Bad args → exit 2.**

Usage:

    # Cross-tenant chain (operator-wide).
    python scripts/verify_audit_window_chain.py --json

    # Per-brokerage chain.
    python scripts/verify_audit_window_chain.py --brokerage-id brk-1 --json

    # Same as above + emit Slack alert on degraded chain.
    python scripts/verify_audit_window_chain.py --brokerage-id brk-1 --alert --json

Exit codes:
    0  — ok or skipped
    1  — failed (chain degraded)
    2  — bad CLI arguments
```

## Imports

`Alert`, `Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.services.monitoring.contracts`, `app.services.monitoring.slack_alert_transport`, `app.services.operator.audit_window_chain`, `argparse`, `datetime`, `json`, `logging`, `os`, `send_pilot_alert_to_slack`, `sys`, `timezone`, `typing`, `verify_audit_window_chain`

## Classes

_none_

## Functions / methods

`__annotate__`, `_build_parser`, `_now_iso`, `_print_summary`, `_safe_envelope`, `main`, `verify`

## Env-key candidates

`HIGH`, `INTEGRITY`, `PAS178`

## String constants (redacted where noted)

- "\nPAS178 — Operator-runnable cross-window chain verifier CLI.\n\nRead-only by default; ``--alert`` explicitly opts in to firing\na Slack chain-break alert via PAS171's pilot transport. NEVER\nwrites to any audit / Merkle / chain table. NEVER auto-\nremediates.\n\nDoctrine:\n\n* **Read-only.** No DB writes. Verification result emitted to\n  stdout as a structural envelope.\n* **No auto-alert.** Slack alert fires ONLY when ``--alert``\n  is passed AND the chain is degraded AND the operator has\n  configured ``PAS_ALERT_SLACK_WEBHOOK_URL``.\n* **No auto-repair.** A break is surfaced; the operator\n  decides whether to file a P0.\n* **NEVER raises.**\n* **DB unavailable → exit 0** with skipped envelope.\n* **Bad args → exit 2.**\n\nUsage:\n\n    # Cross-tenant chain (operator-wide).\n    python scripts/verify_audit_window_chain.py --json\n\n    # Per-brokerage chain.\n    python scripts/verify_audit_window_chain.py --brokerage-id brk-1 --json\n\n    # Same as above + emit Slack alert on degraded chain.\n    python scripts/verify_audit_window_chain.py --brokerage-id brk-1 --alert --json\n\nExit codes:\n    0  — ok or skipped\n    1  — failed (chain degraded)\n    2  — bad CLI arguments\n"
- 'utf-8'
- 'pas.scripts.verify_audit_window_chain'
- 'verification'
- 'slack_alert'
- 'warnings'
- 'error_code'
- 'brokerage_id'
- 'window_start'
- 'window_end'
- 'alert'
- 'return'
- 'str'
- 'seconds'
- 'status'
- 'Optional[str]'
- 'Optional[Dict[str, Any]]'
- 'Optional[List[str]]'
- 'Dict[str, Any]'
- 'phase'
- 'PAS178'
- 'tool'
- 'verify_audit_window_chain'
- 'generated_at'
- 'bool'
- 'Read-only cross-window chain verification. NEVER raises.'
- 'verify_audit_window_chain error type='
- 'skipped'
- 'unexpected:'
- 'chain_status'
- 'degraded'
- 'audit.chain.broken:'
- 'global'
- 'INTEGRITY'
- 'HIGH'
- 'PAS cross-window audit chain integrity break'
- 'Cross-window verification detected '
- 'breaks_count'
- ' break(s). Operator must investigate; no autonomous remediation has been performed.'
- 'scripts.verify_audit_window_chain'
- 'warning_count'
- 'audit_window_chain_broken'
- 'severity'
- 'verify_audit_window_chain Slack alert error type='
- 'failed'
- 'argparse.ArgumentParser'
- 'PAS178 — Read-only cross-window chain verifier. --alert opts in to a Slack chain-break alert; without it the script only emits the structural verdict.'
- '--brokerage-id'
- 'Scope verification to a single brokerage.'
- '--window-start'
- 'Reserved for future window-scoped filtering.'
- '--window-end'
- '--alert'
- 'store_true'
- 'On degraded chain, emit Slack alert via PAS171 pilot transport.'
- '--json'
- 'Emit JSON on stdout instead of the human summary.'
- 'env'
- 'None'
- '[PAS178/verify_audit_window_chain] status='
- ' brokerage_id='
- ' chain_status='
- ' entries_checked='
- 'entries_checked'
- ' breaks_count='
- '  slack_alert='
- '  warn: '
- 'argv'
- 'int'

## Disassembly

```
   0           RESUME                   0

   1           LOAD_CONST               0 ("\nPAS178 — Operator-runnable cross-window chain verifier CLI.\n\nRead-only by default; ``--alert`` explicitly opts in to firing\na Slack chain-break alert via PAS171's pilot transport. NEVER\nwrites to any audit / Merkle / chain table. NEVER auto-\nremediates.\n\nDoctrine:\n\n* **Read-only.** No DB writes. Verification result emitted to\n  stdout as a structural envelope.\n* **No auto-alert.** Slack alert fires ONLY when ``--alert``\n  is passed AND the chain is degraded AND the operator has\n  configured ``PAS_ALERT_SLACK_WEBHOOK_URL``.\n* **No auto-repair.** A break is surfaced; the operator\n  decides whether to file a P0.\n* **NEVER raises.**\n* **DB unavailable → exit 0** with skipped envelope.\n* **Bad args → exit 2.**\n\nUsage:\n\n    # Cross-tenant chain (operator-wide).\n    python scripts/verify_audit_window_chain.py --json\n\n    # Per-brokerage chain.\n    python scripts/verify_audit_window_chain.py --brokerage-id brk-1 --json\n\n    # Same as above + emit Slack alert on degraded chain.\n    python scripts/verify_audit_window_chain.py --brokerage-id brk-1 --alert --json\n\nExit codes:\n    0  — ok or skipped\n    1  — failed (chain degraded)\n    2  — bad CLI arguments\n")
               STORE_NAME               0 (__doc__)

  39           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  41           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  42           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (json)
               STORE_NAME               4 (json)

  43           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (logging)
               STORE_NAME               5 (logging)

  44           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (os)
               STORE_NAME               6 (os)

  45           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              7 (sys)
               STORE_NAME               7 (sys)

  46           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              8 (datetime)
               IMPORT_FROM              8 (datetime)
               STORE_NAME               8 (datetime)
               IMPORT_FROM              9 (timezone)
               STORE_NAME               9 (timezone)
               POP_TOP

  47           LOAD_SMALL_INT           0
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

  50           LOAD_NAME                7 (sys)
               LOAD_ATTR               30 (stdout)
               LOAD_NAME                7 (sys)
               LOAD_ATTR               32 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              17 (_stream)

  51           NOP

  52   L2:     LOAD_NAME               17 (_stream)
               LOAD_ATTR               37 (reconfigure + NULL|self)
               LOAD_CONST               5 ('utf-8')
               LOAD_CONST               6 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  50   L4:     END_FOR
               POP_ITER

  57           LOAD_NAME                7 (sys)
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

  60           LOAD_NAME                5 (logging)
               LOAD_ATTR               52 (getLogger)
               PUSH_NULL
               LOAD_CONST               8 ('pas.scripts.verify_audit_window_chain')
               CALL                     1
               STORE_NAME              27 (logger)

  63           LOAD_CONST               9 (<code object __annotate__ at 0x0000018C17FA32D0, file "scripts/verify_audit_window_chain.py", line 63>)
               MAKE_FUNCTION
               LOAD_CONST              10 (<code object _now_iso at 0x0000018C180392F0, file "scripts/verify_audit_window_chain.py", line 63>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              28 (_now_iso)

  67           LOAD_CONST              11 ('verification')

  73           LOAD_CONST               2 (None)

  67           LOAD_CONST              12 ('slack_alert')

  74           LOAD_CONST               2 (None)

  67           LOAD_CONST              13 ('warnings')

  75           LOAD_CONST               2 (None)

  67           LOAD_CONST              14 ('error_code')

  76           LOAD_CONST               2 (None)

  67           BUILD_MAP                4
               LOAD_CONST              15 (<code object __annotate__ at 0x0000018C17FBFEE0, file "scripts/verify_audit_window_chain.py", line 67>)
               MAKE_FUNCTION
               LOAD_CONST              16 (<code object _safe_envelope at 0x0000018C180396B0, file "scripts/verify_audit_window_chain.py", line 67>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              29 (_safe_envelope)

  93           LOAD_CONST              17 ('brokerage_id')

  95           LOAD_CONST               2 (None)

  93           LOAD_CONST              18 ('window_start')

  96           LOAD_CONST               2 (None)

  93           LOAD_CONST              19 ('window_end')

  97           LOAD_CONST               2 (None)

  93           LOAD_CONST              20 ('alert')

  98           LOAD_CONST              21 (False)

  93           BUILD_MAP                4
               LOAD_CONST              22 (<code object __annotate__ at 0x0000018C18026430, file "scripts/verify_audit_window_chain.py", line 93>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object verify at 0x0000018C17F763E0, file "scripts/verify_audit_window_chain.py", line 93>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              30 (verify)

 173           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA21F0, file "scripts/verify_audit_window_chain.py", line 173>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object _build_parser at 0x0000018C1794EBB0, file "scripts/verify_audit_window_chain.py", line 173>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              31 (_build_parser)

 206           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA3690, file "scripts/verify_audit_window_chain.py", line 206>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object _print_summary at 0x0000018C182E38D0, file "scripts/verify_audit_window_chain.py", line 206>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              32 (_print_summary)

 223           LOAD_CONST              31 ((None,))
               LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA30F0, file "scripts/verify_audit_window_chain.py", line 223>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object main at 0x0000018C18646C00, file "scripts/verify_audit_window_chain.py", line 223>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              33 (main)

 252           LOAD_NAME               34 (__name__)
               LOAD_CONST              30 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 253           LOAD_NAME                7 (sys)
               LOAD_ATTR               70 (exit)
               PUSH_NULL
               LOAD_NAME               33 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 252   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  53           LOAD_NAME               19 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L8)
               NOT_TAKEN
               POP_TOP

  54   L7:     POP_EXCEPT
               JUMP_BACKWARD          250 (to L1)

  53   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA32D0, file "scripts/verify_audit_window_chain.py", line 63>:
 63           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C180392F0, file "scripts/verify_audit_window_chain.py", line 63>:
 63           RESUME                   0

 64           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C17FBFEE0, file "scripts/verify_audit_window_chain.py", line 67>:
 67           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')

 69           LOAD_CONST               2 ('str')

 67           LOAD_CONST               3 ('brokerage_id')

 70           LOAD_CONST               4 ('Optional[str]')

 67           LOAD_CONST               5 ('window_start')

 71           LOAD_CONST               4 ('Optional[str]')

 67           LOAD_CONST               6 ('window_end')

 72           LOAD_CONST               4 ('Optional[str]')

 67           LOAD_CONST               7 ('verification')

 73           LOAD_CONST               8 ('Optional[Dict[str, Any]]')

 67           LOAD_CONST               9 ('slack_alert')

 74           LOAD_CONST               8 ('Optional[Dict[str, Any]]')

 67           LOAD_CONST              10 ('warnings')

 75           LOAD_CONST              11 ('Optional[List[str]]')

 67           LOAD_CONST              12 ('error_code')

 76           LOAD_CONST               4 ('Optional[str]')

 67           LOAD_CONST              13 ('return')

 77           LOAD_CONST              14 ('Dict[str, Any]')

 67           BUILD_MAP                9
              RETURN_VALUE

Disassembly of <code object _safe_envelope at 0x0000018C180396B0, file "scripts/verify_audit_window_chain.py", line 67>:
 67           RESUME                   0

 79           LOAD_CONST               0 ('phase')
              LOAD_CONST               1 ('PAS178')

 80           LOAD_CONST               2 ('tool')
              LOAD_CONST               3 ('verify_audit_window_chain')

 81           LOAD_CONST               4 ('status')
              LOAD_FAST                0 (status)

 82           LOAD_CONST               5 ('brokerage_id')
              LOAD_FAST                1 (brokerage_id)

 83           LOAD_CONST               6 ('window_start')
              LOAD_FAST                2 (window_start)

 84           LOAD_CONST               7 ('window_end')
              LOAD_FAST                3 (window_end)

 85           LOAD_CONST               8 ('verification')
              LOAD_FAST                4 (verification)

 86           LOAD_CONST               9 ('slack_alert')
              LOAD_FAST                5 (slack_alert)

 87           LOAD_CONST              10 ('warnings')
              LOAD_GLOBAL              1 (list + NULL)
              LOAD_FAST                6 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

 88           LOAD_CONST              11 ('error_code')
              LOAD_FAST_BORROW         7 (error_code)

 89           LOAD_CONST              12 ('generated_at')
              LOAD_GLOBAL              3 (_now_iso + NULL)
              CALL                     0

 78           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026430, file "scripts/verify_audit_window_chain.py", line 93>:
 93           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

 95           LOAD_CONST               2 ('Optional[str]')

 93           LOAD_CONST               3 ('window_start')

 96           LOAD_CONST               2 ('Optional[str]')

 93           LOAD_CONST               4 ('window_end')

 97           LOAD_CONST               2 ('Optional[str]')

 93           LOAD_CONST               5 ('alert')

 98           LOAD_CONST               6 ('bool')

 93           LOAD_CONST               7 ('return')

 99           LOAD_CONST               8 ('Dict[str, Any]')

 93           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object verify at 0x0000018C17F763E0, file "scripts/verify_audit_window_chain.py", line 93>:
  93            RESUME                   0

 101            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('verify_audit_window_chain',))
                IMPORT_NAME              0 (app.services.operator.audit_window_chain)
                IMPORT_FROM              1 (verify_audit_window_chain)
                STORE_FAST               4 (verify_audit_window_chain)
                POP_TOP

 102            LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       39 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR                9 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR                9 (strip + NULL|self)
                CALL                     0
                JUMP_FORWARD             1 (to L2)
        L1:     LOAD_CONST               2 (None)
        L2:     STORE_FAST               5 (bid)

 103            NOP

 104    L3:     LOAD_FAST_BORROW         4 (verify_audit_window_chain)
                PUSH_NULL
                LOAD_FAST_BORROW         5 (bid)
                LOAD_CONST               3 (('brokerage_id',))
                CALL_KW                  1
                STORE_FAST               6 (env)

 117    L4:     LOAD_CONST               2 (None)
                STORE_FAST               8 (slack_env)

 118            LOAD_FAST                3 (alert)
                TO_BOOL
                POP_JUMP_IF_FALSE      197 (to L12)
                NOT_TAKEN
                LOAD_FAST                6 (env)
                LOAD_ATTR               23 (get + NULL|self)
                LOAD_CONST               8 ('chain_status')
                CALL                     1
                LOAD_CONST               9 ('degraded')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE      175 (to L12)
                NOT_TAKEN

 123            NOP

 124    L5:     LOAD_SMALL_INT           0
                LOAD_CONST              10 (('Alert',))
                IMPORT_NAME             12 (app.services.monitoring.contracts)
                IMPORT_FROM             13 (Alert)
                STORE_FAST               9 (Alert)
                POP_TOP

 125            LOAD_SMALL_INT           0
                LOAD_CONST              11 (('send_pilot_alert_to_slack',))
                IMPORT_NAME             14 (app.services.monitoring.slack_alert_transport)
                IMPORT_FROM             15 (send_pilot_alert_to_slack)
                STORE_FAST              10 (send_pilot_alert_to_slack)
                POP_TOP

 128            LOAD_GLOBAL             33 (int + NULL)
                LOAD_GLOBAL             34 (datetime)
                LOAD_ATTR               36 (now)
                PUSH_NULL
                LOAD_GLOBAL             38 (timezone)
                LOAD_ATTR               40 (utc)
                CALL                     1
                LOAD_ATTR               43 (timestamp + NULL|self)
                CALL                     0
                CALL                     1
                STORE_FAST              11 (ts)

 129            LOAD_CONST              12 ('audit.chain.broken:')
                LOAD_FAST                5 (bid)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
        L6:     NOT_TAKEN
        L7:     POP_TOP
                LOAD_CONST              13 ('global')
        L8:     FORMAT_SIMPLE
                LOAD_CONST              14 (':')
                LOAD_FAST               11 (ts)
                FORMAT_SIMPLE
                BUILD_STRING             4
                STORE_FAST              12 (alert_id)

 130            LOAD_FAST                9 (Alert)
                PUSH_NULL

 131            LOAD_FAST               12 (alert_id)

 132            LOAD_CONST              15 ('INTEGRITY')

 133            LOAD_CONST              16 ('HIGH')

 134            LOAD_CONST              17 ('PAS cross-window audit chain integrity break')

 136            LOAD_CONST              18 ('Cross-window verification detected ')

 137            LOAD_FAST                6 (env)
                LOAD_ATTR               23 (get + NULL|self)
                LOAD_CONST              19 ('breaks_count')
                LOAD_SMALL_INT           0
                CALL                     2
                FORMAT_SIMPLE
                LOAD_CONST              20 (' break(s). Operator must investigate; no autonomous remediation has been performed.')

 136            BUILD_STRING             3

 141            LOAD_CONST              21 ('scripts.verify_audit_window_chain')

 142            LOAD_FAST                5 (bid)

 144            LOAD_CONST              22 ('warning_count')
                LOAD_GLOBAL             33 (int + NULL)
                LOAD_FAST                6 (env)
                LOAD_ATTR               23 (get + NULL|self)
                LOAD_CONST              19 ('breaks_count')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L11)
        L9:     NOT_TAKEN
       L10:     POP_TOP
                LOAD_SMALL_INT           0
       L11:     CALL                     1

 145            LOAD_CONST              23 ('error_code')
                LOAD_CONST              24 ('audit_window_chain_broken')

 146            LOAD_CONST              25 ('severity')
                LOAD_CONST              16 ('HIGH')

 143            BUILD_MAP                3

 130            LOAD_CONST              26 (('id', 'category', 'severity', 'title', 'description', 'source', 'affected_brokerage', 'metadata'))
                CALL_KW                  8
                STORE_FAST              13 (structural_alert)

 149            LOAD_FAST               10 (send_pilot_alert_to_slack)
                PUSH_NULL
                LOAD_FAST               13 (structural_alert)
                CALL                     1
                STORE_FAST               8 (slack_env)

 161   L12:     LOAD_FAST                6 (env)
                LOAD_ATTR               23 (get + NULL|self)
                LOAD_CONST              28 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              31 ('ok')
       L13:     STORE_FAST              14 (overall_status)

 162            LOAD_GLOBAL             21 (_safe_envelope + NULL)

 163            LOAD_FAST               14 (overall_status)

 164            LOAD_FAST                5 (bid)

 165            LOAD_FAST_LOAD_FAST     18 (window_start, window_end)

 166            LOAD_FAST                6 (env)

 167            LOAD_FAST                8 (slack_env)

 168            LOAD_GLOBAL             45 (list + NULL)
                LOAD_FAST                6 (env)
                LOAD_ATTR               23 (get + NULL|self)
                LOAD_CONST              30 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
       L14:     CALL                     1

 169            LOAD_FAST                6 (env)
                LOAD_ATTR               23 (get + NULL|self)
                LOAD_CONST              23 ('error_code')
                CALL                     1

 162            LOAD_CONST              32 (('status', 'brokerage_id', 'window_start', 'window_end', 'verification', 'slack_alert', 'warnings', 'error_code'))
                CALL_KW                  8
                RETURN_VALUE

  --   L15:     PUSH_EXC_INFO

 105            LOAD_GLOBAL             10 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      115 (to L20)
                NOT_TAKEN
                STORE_FAST               7 (e)

 106   L16:     LOAD_GLOBAL             12 (logger)
                LOAD_ATTR               15 (warning + NULL|self)

 107            LOAD_CONST               4 ('verify_audit_window_chain error type=')
                LOAD_GLOBAL             17 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               18 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 106            CALL                     1
                POP_TOP

 109            LOAD_GLOBAL             21 (_safe_envelope + NULL)

 110            LOAD_CONST               5 ('skipped')

 111            LOAD_FAST                5 (bid)

 112            LOAD_FAST_LOAD_FAST     18 (window_start, window_end)

 113            LOAD_CONST               6 ('unexpected:')
                LOAD_GLOBAL             17 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               18 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 114            LOAD_CONST               6 ('unexpected:')
                LOAD_GLOBAL             17 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               18 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 109            LOAD_CONST               7 (('status', 'brokerage_id', 'window_start', 'window_end', 'warnings', 'error_code'))
                CALL_KW                  6
       L17:     SWAP                     2
       L18:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RETURN_VALUE

  --   L19:     LOAD_CONST               2 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RERAISE                  1

 105   L20:     RERAISE                  0

  --   L21:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L22:     PUSH_EXC_INFO

 150            LOAD_GLOBAL             10 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      108 (to L26)
                NOT_TAKEN
                STORE_FAST               7 (e)

 151   L23:     LOAD_GLOBAL             12 (logger)
                LOAD_ATTR               15 (warning + NULL|self)

 152            LOAD_CONST              27 ('verify_audit_window_chain Slack alert error type=')

 153            LOAD_GLOBAL             17 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               18 (__name__)
                FORMAT_SIMPLE

 152            BUILD_STRING             2

 151            CALL                     1
                POP_TOP

 156            LOAD_CONST              28 ('status')
                LOAD_CONST              29 ('failed')

 157            LOAD_CONST              30 ('warnings')
                LOAD_CONST               6 ('unexpected:')
                LOAD_GLOBAL             17 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               18 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 158            LOAD_CONST              23 ('error_code')
                LOAD_CONST               6 ('unexpected:')
                LOAD_GLOBAL             17 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               18 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 155            BUILD_MAP                3
                STORE_FAST               8 (slack_env)
       L24:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 335 (to L12)

  --   L25:     LOAD_CONST               2 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RERAISE                  1

 150   L26:     RERAISE                  0

  --   L27:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L15 [0]
  L5 to L6 -> L22 [0]
  L7 to L9 -> L22 [0]
  L10 to L12 -> L22 [0]
  L15 to L16 -> L21 [1] lasti
  L16 to L17 -> L19 [1] lasti
  L17 to L18 -> L21 [1] lasti
  L19 to L21 -> L21 [1] lasti
  L22 to L23 -> L27 [1] lasti
  L23 to L24 -> L25 [1] lasti
  L25 to L27 -> L27 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "scripts/verify_audit_window_chain.py", line 173>:
173           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C1794EBB0, file "scripts/verify_audit_window_chain.py", line 173>:
173           RESUME                   0

174           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

175           LOAD_CONST               0 ('verify_audit_window_chain')

177           LOAD_CONST               1 ('PAS178 — Read-only cross-window chain verifier. --alert opts in to a Slack chain-break alert; without it the script only emits the structural verdict.')

174           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

183           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

184           LOAD_CONST               3 ('--brokerage-id')
              LOAD_CONST               4 (None)

185           LOAD_CONST               5 ('Scope verification to a single brokerage.')

183           LOAD_CONST               6 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

187           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

188           LOAD_CONST               7 ('--window-start')
              LOAD_CONST               4 (None)

189           LOAD_CONST               8 ('Reserved for future window-scoped filtering.')

187           LOAD_CONST               6 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

191           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

192           LOAD_CONST               9 ('--window-end')
              LOAD_CONST               4 (None)

193           LOAD_CONST               8 ('Reserved for future window-scoped filtering.')

191           LOAD_CONST               6 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

195           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

196           LOAD_CONST              10 ('--alert')
              LOAD_CONST              11 ('store_true')

197           LOAD_CONST              12 ('On degraded chain, emit Slack alert via PAS171 pilot transport.')

195           LOAD_CONST              13 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

199           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

200           LOAD_CONST              14 ('--json')
              LOAD_CONST              11 ('store_true')

201           LOAD_CONST              15 ('Emit JSON on stdout instead of the human summary.')

199           LOAD_CONST              13 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

203           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "scripts/verify_audit_window_chain.py", line 206>:
206           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C182E38D0, file "scripts/verify_audit_window_chain.py", line 206>:
206           RESUME                   0

207           LOAD_FAST_BORROW         0 (env)
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

208           LOAD_FAST_BORROW         0 (env)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               1 ('slack_alert')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L2:     STORE_FAST               2 (a)

209           LOAD_GLOBAL              3 (print + NULL)

210           LOAD_CONST               2 ('[PAS178/verify_audit_window_chain] status=')

211           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST               3 ('status')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' brokerage_id=')

212           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST               5 ('brokerage_id')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' chain_status=')

213           LOAD_FAST_BORROW         1 (v)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               7 ('chain_status')
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST               8 (' entries_checked=')

214           LOAD_FAST_BORROW         1 (v)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               9 ('entries_checked')
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST              10 (' breaks_count=')

215           LOAD_FAST_BORROW         1 (v)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              11 ('breaks_count')
              CALL                     1
              FORMAT_SIMPLE

210           BUILD_STRING            10

209           CALL                     1
              POP_TOP

217           LOAD_FAST_BORROW         2 (a)
              TO_BOOL
              POP_JUMP_IF_FALSE       30 (to L3)
              NOT_TAKEN

218           LOAD_GLOBAL              3 (print + NULL)
              LOAD_CONST              12 ('  slack_alert=')
              LOAD_FAST_BORROW         2 (a)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               3 ('status')
              CALL                     1
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP

219   L3:     LOAD_FAST_BORROW         0 (env)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              13 ('warnings')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L4:     LOAD_CONST              14 (slice(None, 10, None))
              BINARY_OP               26 ([])
              GET_ITER
      L5:     FOR_ITER                17 (to L6)
              STORE_FAST               3 (w)

220           LOAD_GLOBAL              3 (print + NULL)
              LOAD_CONST              15 ('  warn: ')
              LOAD_FAST_BORROW         3 (w)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L5)

219   L6:     END_FOR
              POP_ITER
              LOAD_CONST              16 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA30F0, file "scripts/verify_audit_window_chain.py", line 223>:
223           RESUME                   0
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

Disassembly of <code object main at 0x0000018C18646C00, file "scripts/verify_audit_window_chain.py", line 223>:
 223            RESUME                   0

 224            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 225            NOP

 226    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 230    L2:     LOAD_GLOBAL             11 (verify + NULL)

 231            LOAD_FAST                2 (args)
                LOAD_ATTR               12 (brokerage_id)

 232            LOAD_FAST                2 (args)
                LOAD_ATTR               14 (window_start)

 233            LOAD_FAST                2 (args)
                LOAD_ATTR               16 (window_end)

 234            LOAD_FAST                2 (args)
                LOAD_ATTR               18 (alert)

 230            LOAD_CONST               2 (('brokerage_id', 'window_start', 'window_end', 'alert'))
                CALL_KW                  4
                STORE_FAST               4 (env)

 237            LOAD_FAST                2 (args)
                LOAD_ATTR               20 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       36 (to L3)
                NOT_TAKEN

 238            LOAD_GLOBAL             23 (print + NULL)
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
                JUMP_FORWARD            11 (to L4)

 240    L3:     LOAD_GLOBAL             27 (_print_summary + NULL)
                LOAD_FAST                4 (env)
                CALL                     1
                POP_TOP

 242    L4:     LOAD_FAST                4 (env)
                LOAD_ATTR               29 (get + NULL|self)
                LOAD_CONST               5 ('status')
                CALL                     1
                STORE_FAST               5 (status)

 243            LOAD_FAST                5 (status)
                LOAD_CONST               6 ('skipped')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_TRUE         8 (to L5)
                NOT_TAKEN
                LOAD_FAST                5 (status)
                LOAD_CONST               7 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       56 (to L8)
                NOT_TAKEN

 244    L5:     LOAD_FAST                4 (env)
                LOAD_ATTR               29 (get + NULL|self)
                LOAD_CONST               8 ('verification')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
        L6:     STORE_FAST               6 (v)

 245            LOAD_FAST                6 (v)
                LOAD_ATTR               29 (get + NULL|self)
                LOAD_CONST               9 ('chain_status')
                CALL                     1
                STORE_FAST               7 (chain)

 246            LOAD_FAST                7 (chain)
                LOAD_CONST              10 ('degraded')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L7)
                NOT_TAKEN

 247            LOAD_SMALL_INT           1
                RETURN_VALUE

 248    L7:     LOAD_SMALL_INT           0
                RETURN_VALUE

 249    L8:     LOAD_SMALL_INT           1
                RETURN_VALUE

  --    L9:     PUSH_EXC_INFO

 227            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L18)
                NOT_TAKEN
                STORE_FAST               3 (e)

 228   L10:     LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                LOAD_CONST              11 ((0, None))
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE        3 (to L11)
                NOT_TAKEN
                LOAD_SMALL_INT           2
                JUMP_FORWARD            30 (to L15)
       L11:     LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L14)
       L12:     NOT_TAKEN
       L13:     POP_TOP
                LOAD_SMALL_INT           0
       L14:     CALL                     1
       L15:     SWAP                     2
       L16:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RETURN_VALUE

  --   L17:     LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 227   L18:     RERAISE                  0

  --   L19:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L9 [0]
  L9 to L10 -> L19 [1] lasti
  L10 to L12 -> L17 [1] lasti
  L13 to L15 -> L17 [1] lasti
  L15 to L16 -> L19 [1] lasti
  L17 to L19 -> L19 [1] lasti
```
