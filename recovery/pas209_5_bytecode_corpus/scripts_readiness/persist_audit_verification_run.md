# scripts_readiness/persist_audit_verification_run

- **pyc:** `scripts\__pycache__\persist_audit_verification_run.cpython-314.pyc`
- **expected source path (absent):** `scripts/persist_audit_verification_run.py`
- **co_filename (from bytecode):** `scripts/persist_audit_verification_run.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS178 — Operator-runnable verification-run persistence CLI.

Wraps :func:`app.services.operator.audit_verification_runs.
build_verification_run_record` and ``persist_verification_run``
into a single operator-facing command. Dry-run by default;
``--execute`` is required to actually INSERT into the v27
``pas_audit_verification_runs`` table.

Doctrine:

* **Dry-run by default.** ``--execute`` required to write.
* **Append-only.** This script ONLY ever issues INSERTs against
  the v27 table. It never UPDATEs or DELETEs. The underlying
  service exposes no mutation helpers, and the v27 SQL policy
  rejects UPDATE/DELETE at the row-level-security layer too.
* **No PII / no secrets.** The envelope emitted to stdout
  contains only the structural fields projected by the service
  layer's closed allow-list.
* **NEVER raises.**
* **DB unavailable → exit 0** with skipped envelope.
* **Bad args → exit 2.**
* **No auto-remediation.** The script does NOT trigger any
  downstream verification; it only persists the run record
  the operator has constructed from a prior verification.

Usage:

    # Dry-run; show the record that WOULD be persisted.
    python scripts/persist_audit_verification_run.py         --verification-type CROSS_WINDOW_CHAIN         --status PASSED

    # Same, scoped to a single brokerage.
    python scripts/persist_audit_verification_run.py         --brokerage-id brk-1         --verification-type CROSS_WINDOW_CHAIN         --status PASSED

    # Actually persist a FAILED run.
    python scripts/persist_audit_verification_run.py         --brokerage-id brk-1         --verification-type CROSS_WINDOW_CHAIN         --status FAILED         --broken-chain-count 1         --warning-count 1         --error-code audit_window_chain_broken         --execute

Exit codes:
    0  — ok or skipped
    1  — failed (record build failed or persist failed)
    2  — bad CLI arguments
```

## Imports

`ALLOWED_RUN_STATUSES`, `ALLOWED_VERIFICATION_TYPES`, `Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.services.operator.audit_verification_runs`, `argparse`, `build_verification_run_record`, `datetime`, `json`, `logging`, `os`, `persist_verification_run`, `sys`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_build_parser`, `_now_iso`, `_print_summary`, `_safe_envelope`, `main`, `persist`

## Env-key candidates

`OPERATOR`, `PAS178`

## String constants (redacted where noted)

- "\nPAS178 — Operator-runnable verification-run persistence CLI.\n\nWraps :func:`app.services.operator.audit_verification_runs.\nbuild_verification_run_record` and ``persist_verification_run``\ninto a single operator-facing command. Dry-run by default;\n``--execute`` is required to actually INSERT into the v27\n``pas_audit_verification_runs`` table.\n\nDoctrine:\n\n* **Dry-run by default.** ``--execute`` required to write.\n* **Append-only.** This script ONLY ever issues INSERTs against\n  the v27 table. It never UPDATEs or DELETEs. The underlying\n  service exposes no mutation helpers, and the v27 SQL policy\n  rejects UPDATE/DELETE at the row-level-security layer too.\n* **No PII / no secrets.** The envelope emitted to stdout\n  contains only the structural fields projected by the service\n  layer's closed allow-list.\n* **NEVER raises.**\n* **DB unavailable → exit 0** with skipped envelope.\n* **Bad args → exit 2.**\n* **No auto-remediation.** The script does NOT trigger any\n  downstream verification; it only persists the run record\n  the operator has constructed from a prior verification.\n\nUsage:\n\n    # Dry-run; show the record that WOULD be persisted.\n    python scripts/persist_audit_verification_run.py         --verification-type CROSS_WINDOW_CHAIN         --status PASSED\n\n    # Same, scoped to a single brokerage.\n    python scripts/persist_audit_verification_run.py         --brokerage-id brk-1         --verification-type CROSS_WINDOW_CHAIN         --status PASSED\n\n    # Actually persist a FAILED run.\n    python scripts/persist_audit_verification_run.py         --brokerage-id brk-1         --verification-type CROSS_WINDOW_CHAIN         --status FAILED         --broken-chain-count 1         --warning-count 1         --error-code audit_window_chain_broken         --execute\n\nExit codes:\n    0  — ok or skipped\n    1  — failed (record build failed or persist failed)\n    2  — bad CLI arguments\n"
- 'utf-8'
- 'pas.scripts.persist_audit_verification_run'
- 'record'
- 'run_row'
- 'warnings'
- 'error_code'
- 'checked_window_count'
- 'checked_audit_row_count'
- 'broken_chain_count'
- 'warning_count'
- 'actor_id'
- 'dry_run'
- 'return'
- 'str'
- 'seconds'
- 'status'
- 'bool'
- 'brokerage_id'
- 'Optional[str]'
- 'verification_type'
- 'run_status'
- 'Optional[Dict[str, Any]]'
- 'Optional[List[str]]'
- 'Dict[str, Any]'
- 'phase'
- 'PAS178'
- 'tool'
- 'persist_audit_verification_run'
- 'generated_at'
- 'int'
- 'Build + (optionally) persist a verification-run record.\nNEVER raises.'
- 'OPERATOR'
- 'operator_command'
- 'persist_audit_verification_run build error type='
- 'failed'
- 'unexpected:'
- 'persist_audit_verification_run insert error type='
- 'skipped'
- 'argparse.ArgumentParser'
- 'PAS178 — Append-only persistence of an operator-driven audit verification run. Dry-run by default; --execute required to actually INSERT into the v27 table.'
- '--brokerage-id'
- 'Scope the run to a single brokerage. Omit for operator-wide run.'
- '--verification-type'
- 'Closed enum of verification-run types.'
- '--status'
- 'Closed enum of run statuses.'
- '--checked-window-count'
- "Number of Merkle windows the operator's verification covered."
- '--checked-audit-row-count'
- "Number of audit rows the operator's verification covered."
- '--broken-chain-count'
- 'Number of chain breaks discovered.'
- '--warning-count'
- 'Structural warnings emitted by the verification.'
- '--error-code'
- 'Closed structural error code, e.g. audit_window_chain_broken.'
- '--actor-id'
- 'Operator actor token. Bounded to [A-Za-z0-9_-]+.'
- '--execute'
- 'store_true'
- 'Actually INSERT. Without this flag the script runs in dry-run mode.'
- '--json'
- 'Emit JSON on stdout instead of the human summary.'
- 'env'
- 'None'
- '[PAS178/persist_audit_verification_run] status='
- ' dry_run='
- ' brokerage_id='
- ' verification_type='
- ' run_status='
- ' record_id='
- 'verification_run_id'
- ' row_id='
- '  error_code='
- '  warn: '
- 'argv'

## Disassembly

```
   0           RESUME                   0

   1           LOAD_CONST               0 ("\nPAS178 — Operator-runnable verification-run persistence CLI.\n\nWraps :func:`app.services.operator.audit_verification_runs.\nbuild_verification_run_record` and ``persist_verification_run``\ninto a single operator-facing command. Dry-run by default;\n``--execute`` is required to actually INSERT into the v27\n``pas_audit_verification_runs`` table.\n\nDoctrine:\n\n* **Dry-run by default.** ``--execute`` required to write.\n* **Append-only.** This script ONLY ever issues INSERTs against\n  the v27 table. It never UPDATEs or DELETEs. The underlying\n  service exposes no mutation helpers, and the v27 SQL policy\n  rejects UPDATE/DELETE at the row-level-security layer too.\n* **No PII / no secrets.** The envelope emitted to stdout\n  contains only the structural fields projected by the service\n  layer's closed allow-list.\n* **NEVER raises.**\n* **DB unavailable → exit 0** with skipped envelope.\n* **Bad args → exit 2.**\n* **No auto-remediation.** The script does NOT trigger any\n  downstream verification; it only persists the run record\n  the operator has constructed from a prior verification.\n\nUsage:\n\n    # Dry-run; show the record that WOULD be persisted.\n    python scripts/persist_audit_verification_run.py         --verification-type CROSS_WINDOW_CHAIN         --status PASSED\n\n    # Same, scoped to a single brokerage.\n    python scripts/persist_audit_verification_run.py         --brokerage-id brk-1         --verification-type CROSS_WINDOW_CHAIN         --status PASSED\n\n    # Actually persist a FAILED run.\n    python scripts/persist_audit_verification_run.py         --brokerage-id brk-1         --verification-type CROSS_WINDOW_CHAIN         --status FAILED         --broken-chain-count 1         --warning-count 1         --error-code audit_window_chain_broken         --execute\n\nExit codes:\n    0  — ok or skipped\n    1  — failed (record build failed or persist failed)\n    2  — bad CLI arguments\n")
               STORE_NAME               0 (__doc__)

  56           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  58           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  59           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (json)
               STORE_NAME               4 (json)

  60           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (logging)
               STORE_NAME               5 (logging)

  61           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (os)
               STORE_NAME               6 (os)

  62           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              7 (sys)
               STORE_NAME               7 (sys)

  63           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              8 (datetime)
               IMPORT_FROM              8 (datetime)
               STORE_NAME               8 (datetime)
               IMPORT_FROM              9 (timezone)
               STORE_NAME               9 (timezone)
               POP_TOP

  64           LOAD_SMALL_INT           0
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

  67           LOAD_NAME                7 (sys)
               LOAD_ATTR               30 (stdout)
               LOAD_NAME                7 (sys)
               LOAD_ATTR               32 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              17 (_stream)

  68           NOP

  69   L2:     LOAD_NAME               17 (_stream)
               LOAD_ATTR               37 (reconfigure + NULL|self)
               LOAD_CONST               5 ('utf-8')
               LOAD_CONST               6 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  67   L4:     END_FOR
               POP_ITER

  74           LOAD_NAME                7 (sys)
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

  77           LOAD_NAME                5 (logging)
               LOAD_ATTR               52 (getLogger)
               PUSH_NULL
               LOAD_CONST               8 ('pas.scripts.persist_audit_verification_run')
               CALL                     1
               STORE_NAME              27 (logger)

  80           LOAD_CONST               9 (<code object __annotate__ at 0x0000018C17FA31E0, file "scripts/persist_audit_verification_run.py", line 80>)
               MAKE_FUNCTION
               LOAD_CONST              10 (<code object _now_iso at 0x0000018C18038DF0, file "scripts/persist_audit_verification_run.py", line 80>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              28 (_now_iso)

  84           LOAD_CONST              11 ('record')

  91           LOAD_CONST               2 (None)

  84           LOAD_CONST              12 ('run_row')

  92           LOAD_CONST               2 (None)

  84           LOAD_CONST              13 ('warnings')

  93           LOAD_CONST               2 (None)

  84           LOAD_CONST              14 ('error_code')

  94           LOAD_CONST               2 (None)

  84           BUILD_MAP                4
               LOAD_CONST              15 (<code object __annotate__ at 0x0000018C1812C140, file "scripts/persist_audit_verification_run.py", line 84>)
               MAKE_FUNCTION
               LOAD_CONST              16 (<code object _safe_envelope at 0x0000018C17FE13E0, file "scripts/persist_audit_verification_run.py", line 84>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              29 (_safe_envelope)

 112           LOAD_CONST              17 ('checked_window_count')

 117           LOAD_SMALL_INT           0

 112           LOAD_CONST              18 ('checked_audit_row_count')

 118           LOAD_SMALL_INT           0

 112           LOAD_CONST              19 ('broken_chain_count')

 119           LOAD_SMALL_INT           0

 112           LOAD_CONST              20 ('warning_count')

 120           LOAD_SMALL_INT           0

 112           LOAD_CONST              14 ('error_code')

 121           LOAD_CONST               2 (None)

 112           LOAD_CONST              21 ('actor_id')

 122           LOAD_CONST               2 (None)

 112           LOAD_CONST              22 ('dry_run')

 123           LOAD_CONST              23 (True)

 112           BUILD_MAP                7
               LOAD_CONST              24 (<code object __annotate__ at 0x0000018C180533F0, file "scripts/persist_audit_verification_run.py", line 112>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object persist at 0x0000018C17ED2840, file "scripts/persist_audit_verification_run.py", line 112>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              30 (persist)

 219           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA3E10, file "scripts/persist_audit_verification_run.py", line 219>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object _build_parser at 0x0000018C17F84C80, file "scripts/persist_audit_verification_run.py", line 219>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              31 (_build_parser)

 281           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA3960, file "scripts/persist_audit_verification_run.py", line 281>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object _print_summary at 0x0000018C18644F20, file "scripts/persist_audit_verification_run.py", line 281>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              32 (_print_summary)

 300           LOAD_CONST              33 ((None,))
               LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA3C30, file "scripts/persist_audit_verification_run.py", line 300>)
               MAKE_FUNCTION
               LOAD_CONST              31 (<code object main at 0x0000018C17D6DFC0, file "scripts/persist_audit_verification_run.py", line 300>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              33 (main)

 331           LOAD_NAME               34 (__name__)
               LOAD_CONST              32 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 332           LOAD_NAME                7 (sys)
               LOAD_ATTR               70 (exit)
               PUSH_NULL
               LOAD_NAME               33 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 331   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  70           LOAD_NAME               19 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  71   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          257 (to L1)

  70   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "scripts/persist_audit_verification_run.py", line 80>:
 80           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038DF0, file "scripts/persist_audit_verification_run.py", line 80>:
 80           RESUME                   0

 81           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C1812C140, file "scripts/persist_audit_verification_run.py", line 84>:
 84           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')

 86           LOAD_CONST               2 ('str')

 84           LOAD_CONST               3 ('dry_run')

 87           LOAD_CONST               4 ('bool')

 84           LOAD_CONST               5 ('brokerage_id')

 88           LOAD_CONST               6 ('Optional[str]')

 84           LOAD_CONST               7 ('verification_type')

 89           LOAD_CONST               6 ('Optional[str]')

 84           LOAD_CONST               8 ('run_status')

 90           LOAD_CONST               6 ('Optional[str]')

 84           LOAD_CONST               9 ('record')

 91           LOAD_CONST              10 ('Optional[Dict[str, Any]]')

 84           LOAD_CONST              11 ('run_row')

 92           LOAD_CONST              10 ('Optional[Dict[str, Any]]')

 84           LOAD_CONST              12 ('warnings')

 93           LOAD_CONST              13 ('Optional[List[str]]')

 84           LOAD_CONST              14 ('error_code')

 94           LOAD_CONST               6 ('Optional[str]')

 84           LOAD_CONST              15 ('return')

 95           LOAD_CONST              16 ('Dict[str, Any]')

 84           BUILD_MAP               10
              RETURN_VALUE

Disassembly of <code object _safe_envelope at 0x0000018C17FE13E0, file "scripts/persist_audit_verification_run.py", line 84>:
 84           RESUME                   0

 97           LOAD_CONST               0 ('phase')
              LOAD_CONST               1 ('PAS178')

 98           LOAD_CONST               2 ('tool')
              LOAD_CONST               3 ('persist_audit_verification_run')

 99           LOAD_CONST               4 ('status')
              LOAD_FAST                0 (status)

100           LOAD_CONST               5 ('dry_run')
              LOAD_GLOBAL              1 (bool + NULL)
              LOAD_FAST_BORROW         1 (dry_run)
              CALL                     1

101           LOAD_CONST               6 ('brokerage_id')
              LOAD_FAST                2 (brokerage_id)

102           LOAD_CONST               7 ('verification_type')
              LOAD_FAST                3 (verification_type)

103           LOAD_CONST               8 ('run_status')
              LOAD_FAST                4 (run_status)

104           LOAD_CONST               9 ('record')
              LOAD_FAST                5 (record)

105           LOAD_CONST              10 ('run_row')
              LOAD_FAST                6 (run_row)

106           LOAD_CONST              11 ('warnings')
              LOAD_GLOBAL              3 (list + NULL)
              LOAD_FAST                7 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

107           LOAD_CONST              12 ('error_code')
              LOAD_FAST_BORROW         8 (error_code)

108           LOAD_CONST              13 ('generated_at')
              LOAD_GLOBAL              5 (_now_iso + NULL)
              CALL                     0

 96           BUILD_MAP               12
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180533F0, file "scripts/persist_audit_verification_run.py", line 112>:
112           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

114           LOAD_CONST               2 ('Optional[str]')

112           LOAD_CONST               3 ('verification_type')

115           LOAD_CONST               4 ('str')

112           LOAD_CONST               5 ('run_status')

116           LOAD_CONST               4 ('str')

112           LOAD_CONST               6 ('checked_window_count')

117           LOAD_CONST               7 ('int')

112           LOAD_CONST               8 ('checked_audit_row_count')

118           LOAD_CONST               7 ('int')

112           LOAD_CONST               9 ('broken_chain_count')

119           LOAD_CONST               7 ('int')

112           LOAD_CONST              10 ('warning_count')

120           LOAD_CONST               7 ('int')

112           LOAD_CONST              11 ('error_code')

121           LOAD_CONST               2 ('Optional[str]')

112           LOAD_CONST              12 ('actor_id')

122           LOAD_CONST               2 ('Optional[str]')

112           LOAD_CONST              13 ('dry_run')

123           LOAD_CONST              14 ('bool')

112           LOAD_CONST              15 ('return')

124           LOAD_CONST              16 ('Dict[str, Any]')

112           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object persist at 0x0000018C17ED2840, file "scripts/persist_audit_verification_run.py", line 112>:
 112            RESUME                   0

 127            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('build_verification_run_record', 'persist_verification_run'))
                IMPORT_NAME              0 (app.services.operator.audit_verification_runs)
                IMPORT_FROM              1 (build_verification_run_record)
                STORE_FAST              10 (build_verification_run_record)
                IMPORT_FROM              2 (persist_verification_run)
                STORE_FAST              11 (persist_verification_run)
                POP_TOP

 131            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_GLOBAL              8 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       39 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR               11 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR               11 (strip + NULL|self)
                CALL                     0
                JUMP_FORWARD             1 (to L2)
        L1:     LOAD_CONST               2 (None)
        L2:     STORE_FAST              12 (bid)

 132            LOAD_GLOBAL             13 (_now_iso + NULL)
                CALL                     0
                STORE_FAST              13 (started)

 133            NOP

 134    L3:     LOAD_FAST_BORROW        10 (build_verification_run_record)
                PUSH_NULL

 135            LOAD_FAST_BORROW        12 (bid)

 136            LOAD_FAST_BORROW         1 (verification_type)

 137            LOAD_FAST_BORROW         2 (run_status)

 138            LOAD_FAST_BORROW        13 (started)

 139            LOAD_FAST_BORROW        13 (started)

 140            LOAD_FAST_BORROW         3 (checked_window_count)

 141            LOAD_FAST_BORROW         4 (checked_audit_row_count)

 142            LOAD_FAST_BORROW         5 (broken_chain_count)

 143            LOAD_FAST_BORROW         6 (warning_count)

 144            LOAD_FAST_BORROW         7 (error_code)

 145            LOAD_CONST               3 ('OPERATOR')

 146            LOAD_FAST_BORROW         8 (actor_id)

 147            LOAD_CONST               4 ('operator_command')
                LOAD_CONST               5 ('persist_audit_verification_run')
                BUILD_MAP                1

 134            LOAD_CONST               6 (('brokerage_id', 'verification_type', 'status', 'started_at', 'completed_at', 'checked_window_count', 'checked_audit_row_count', 'broken_chain_count', 'warning_count', 'error_code', 'generated_by_actor_type', 'generated_by_actor_id', 'metadata'))
                CALL_KW                 13
                STORE_FAST              14 (built)

 164    L4:     LOAD_FAST               14 (built)
                LOAD_ATTR               27 (get + NULL|self)
                LOAD_CONST              11 ('status')
                CALL                     1
                LOAD_CONST              12 ('ok')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       69 (to L6)
                NOT_TAKEN

 165            LOAD_GLOBAL             25 (_safe_envelope + NULL)

 166            LOAD_CONST               8 ('failed')

 167            LOAD_FAST                9 (dry_run)

 168            LOAD_FAST               12 (bid)

 169            LOAD_FAST                1 (verification_type)

 170            LOAD_FAST                2 (run_status)

 171            LOAD_CONST               2 (None)

 172            LOAD_GLOBAL             29 (list + NULL)
                LOAD_FAST               14 (built)
                LOAD_ATTR               27 (get + NULL|self)
                LOAD_CONST              13 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
        L5:     CALL                     1

 173            LOAD_FAST               14 (built)
                LOAD_ATTR               27 (get + NULL|self)
                LOAD_CONST              14 ('error_code')
                CALL                     1

 165            LOAD_CONST              15 (('status', 'dry_run', 'brokerage_id', 'verification_type', 'run_status', 'record', 'warnings', 'error_code'))
                CALL_KW                  8
                RETURN_VALUE

 176    L6:     LOAD_FAST               14 (built)
                LOAD_ATTR               27 (get + NULL|self)
                LOAD_CONST              16 ('record')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
        L7:     STORE_FAST              16 (record)

 178            LOAD_FAST                9 (dry_run)
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L8)
                NOT_TAKEN

 179            LOAD_GLOBAL             25 (_safe_envelope + NULL)

 180            LOAD_CONST              12 ('ok')

 181            LOAD_CONST              17 (True)

 182            LOAD_FAST               12 (bid)

 183            LOAD_FAST                1 (verification_type)

 184            LOAD_FAST                2 (run_status)

 185            LOAD_FAST               16 (record)

 179            LOAD_CONST              18 (('status', 'dry_run', 'brokerage_id', 'verification_type', 'run_status', 'record'))
                CALL_KW                  6
                RETURN_VALUE

 188    L8:     NOP

 189    L9:     LOAD_FAST               11 (persist_verification_run)
                PUSH_NULL
                LOAD_FAST               16 (record)
                CALL                     1
                STORE_FAST              17 (ins)

 206   L10:     LOAD_GLOBAL             25 (_safe_envelope + NULL)

 207            LOAD_FAST               17 (ins)
                LOAD_ATTR               27 (get + NULL|self)
                LOAD_CONST              11 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L11)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              21 ('skipped')

 208   L11:     LOAD_CONST              20 (False)

 209            LOAD_FAST               12 (bid)

 210            LOAD_FAST                1 (verification_type)

 211            LOAD_FAST                2 (run_status)

 212            LOAD_FAST               16 (record)

 213            LOAD_FAST               17 (ins)
                LOAD_ATTR               27 (get + NULL|self)
                LOAD_CONST              22 ('run_row')
                CALL                     1

 214            LOAD_GLOBAL             29 (list + NULL)
                LOAD_FAST               17 (ins)
                LOAD_ATTR               27 (get + NULL|self)
                LOAD_CONST              13 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
       L12:     CALL                     1

 215            LOAD_FAST               17 (ins)
                LOAD_ATTR               27 (get + NULL|self)
                LOAD_CONST              14 ('error_code')
                CALL                     1

 206            LOAD_CONST              23 (('status', 'dry_run', 'brokerage_id', 'verification_type', 'run_status', 'record', 'run_row', 'warnings', 'error_code'))
                CALL_KW                  9
                RETURN_VALUE

  --   L13:     PUSH_EXC_INFO

 149            LOAD_GLOBAL             14 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      117 (to L18)
                NOT_TAKEN
                STORE_FAST              15 (e)

 150   L14:     LOAD_GLOBAL             16 (logger)
                LOAD_ATTR               19 (warning + NULL|self)

 151            LOAD_CONST               7 ('persist_audit_verification_run build error type=')

 152            LOAD_GLOBAL             21 (type + NULL)
                LOAD_FAST               15 (e)
                CALL                     1
                LOAD_ATTR               22 (__name__)
                FORMAT_SIMPLE

 151            BUILD_STRING             2

 150            CALL                     1
                POP_TOP

 154            LOAD_GLOBAL             25 (_safe_envelope + NULL)

 155            LOAD_CONST               8 ('failed')

 156            LOAD_FAST                9 (dry_run)

 157            LOAD_FAST               12 (bid)

 158            LOAD_FAST                1 (verification_type)

 159            LOAD_FAST                2 (run_status)

 160            LOAD_CONST               9 ('unexpected:')
                LOAD_GLOBAL             21 (type + NULL)
                LOAD_FAST               15 (e)
                CALL                     1
                LOAD_ATTR               22 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 161            LOAD_CONST               9 ('unexpected:')
                LOAD_GLOBAL             21 (type + NULL)
                LOAD_FAST               15 (e)
                CALL                     1
                LOAD_ATTR               22 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 154            LOAD_CONST              10 (('status', 'dry_run', 'brokerage_id', 'verification_type', 'run_status', 'warnings', 'error_code'))
                CALL_KW                  7
       L15:     SWAP                     2
       L16:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST              15 (e)
                DELETE_FAST             15 (e)
                RETURN_VALUE

  --   L17:     LOAD_CONST               2 (None)
                STORE_FAST              15 (e)
                DELETE_FAST             15 (e)
                RERAISE                  1

 149   L18:     RERAISE                  0

  --   L19:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L20:     PUSH_EXC_INFO

 190            LOAD_GLOBAL             14 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      118 (to L25)
                NOT_TAKEN
                STORE_FAST              15 (e)

 191   L21:     LOAD_GLOBAL             16 (logger)
                LOAD_ATTR               19 (warning + NULL|self)

 192            LOAD_CONST              19 ('persist_audit_verification_run insert error type=')

 193            LOAD_GLOBAL             21 (type + NULL)
                LOAD_FAST               15 (e)
                CALL                     1
                LOAD_ATTR               22 (__name__)
                FORMAT_SIMPLE

 192            BUILD_STRING             2

 191            CALL                     1
                POP_TOP

 195            LOAD_GLOBAL             25 (_safe_envelope + NULL)

 196            LOAD_CONST               8 ('failed')

 197            LOAD_CONST              20 (False)

 198            LOAD_FAST               12 (bid)

 199            LOAD_FAST                1 (verification_type)

 200            LOAD_FAST                2 (run_status)

 201            LOAD_FAST               16 (record)

 202            LOAD_CONST               9 ('unexpected:')
                LOAD_GLOBAL             21 (type + NULL)
                LOAD_FAST               15 (e)
                CALL                     1
                LOAD_ATTR               22 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 203            LOAD_CONST               9 ('unexpected:')
                LOAD_GLOBAL             21 (type + NULL)
                LOAD_FAST               15 (e)
                CALL                     1
                LOAD_ATTR               22 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 195            LOAD_CONST              15 (('status', 'dry_run', 'brokerage_id', 'verification_type', 'run_status', 'record', 'warnings', 'error_code'))
                CALL_KW                  8
       L22:     SWAP                     2
       L23:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST              15 (e)
                DELETE_FAST             15 (e)
                RETURN_VALUE

  --   L24:     LOAD_CONST               2 (None)
                STORE_FAST              15 (e)
                DELETE_FAST             15 (e)
                RERAISE                  1

 190   L25:     RERAISE                  0

  --   L26:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L13 [0]
  L9 to L10 -> L20 [0]
  L13 to L14 -> L19 [1] lasti
  L14 to L15 -> L17 [1] lasti
  L15 to L16 -> L19 [1] lasti
  L17 to L19 -> L19 [1] lasti
  L20 to L21 -> L26 [1] lasti
  L21 to L22 -> L24 [1] lasti
  L22 to L23 -> L26 [1] lasti
  L24 to L26 -> L26 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "scripts/persist_audit_verification_run.py", line 219>:
219           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C17F84C80, file "scripts/persist_audit_verification_run.py", line 219>:
219           RESUME                   0

220           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('ALLOWED_VERIFICATION_TYPES', 'ALLOWED_RUN_STATUSES'))
              IMPORT_NAME              0 (app.services.operator.audit_verification_runs)
              IMPORT_FROM              1 (ALLOWED_VERIFICATION_TYPES)
              STORE_FAST               0 (ALLOWED_VERIFICATION_TYPES)
              IMPORT_FROM              2 (ALLOWED_RUN_STATUSES)
              STORE_FAST               1 (ALLOWED_RUN_STATUSES)
              POP_TOP

224           LOAD_GLOBAL              6 (argparse)
              LOAD_ATTR                8 (ArgumentParser)
              PUSH_NULL

225           LOAD_CONST               2 ('persist_audit_verification_run')

227           LOAD_CONST               3 ('PAS178 — Append-only persistence of an operator-driven audit verification run. Dry-run by default; --execute required to actually INSERT into the v27 table.')

224           LOAD_CONST               4 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               2 (p)

232           LOAD_FAST_BORROW         2 (p)
              LOAD_ATTR               11 (add_argument + NULL|self)

233           LOAD_CONST               5 ('--brokerage-id')
              LOAD_CONST               6 (None)

234           LOAD_CONST               7 ('Scope the run to a single brokerage. Omit for operator-wide run.')

232           LOAD_CONST               8 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

236           LOAD_FAST_BORROW         2 (p)
              LOAD_ATTR               11 (add_argument + NULL|self)

237           LOAD_CONST               9 ('--verification-type')
              LOAD_CONST              10 (True)

238           LOAD_GLOBAL             13 (list + NULL)
              LOAD_FAST_BORROW         0 (ALLOWED_VERIFICATION_TYPES)
              CALL                     1

239           LOAD_CONST              11 ('Closed enum of verification-run types.')

236           LOAD_CONST              12 (('required', 'choices', 'help'))
              CALL_KW                  4
              POP_TOP

241           LOAD_FAST_BORROW         2 (p)
              LOAD_ATTR               11 (add_argument + NULL|self)

242           LOAD_CONST              13 ('--status')
              LOAD_CONST              10 (True)

243           LOAD_GLOBAL             13 (list + NULL)
              LOAD_FAST_BORROW         1 (ALLOWED_RUN_STATUSES)
              CALL                     1

244           LOAD_CONST              14 ('Closed enum of run statuses.')

241           LOAD_CONST              12 (('required', 'choices', 'help'))
              CALL_KW                  4
              POP_TOP

246           LOAD_FAST_BORROW         2 (p)
              LOAD_ATTR               11 (add_argument + NULL|self)

247           LOAD_CONST              15 ('--checked-window-count')
              LOAD_GLOBAL             14 (int)
              LOAD_SMALL_INT           0

248           LOAD_CONST              16 ("Number of Merkle windows the operator's verification covered.")

246           LOAD_CONST              17 (('type', 'default', 'help'))
              CALL_KW                  4
              POP_TOP

250           LOAD_FAST_BORROW         2 (p)
              LOAD_ATTR               11 (add_argument + NULL|self)

251           LOAD_CONST              18 ('--checked-audit-row-count')
              LOAD_GLOBAL             14 (int)
              LOAD_SMALL_INT           0

252           LOAD_CONST              19 ("Number of audit rows the operator's verification covered.")

250           LOAD_CONST              17 (('type', 'default', 'help'))
              CALL_KW                  4
              POP_TOP

254           LOAD_FAST_BORROW         2 (p)
              LOAD_ATTR               11 (add_argument + NULL|self)

255           LOAD_CONST              20 ('--broken-chain-count')
              LOAD_GLOBAL             14 (int)
              LOAD_SMALL_INT           0

256           LOAD_CONST              21 ('Number of chain breaks discovered.')

254           LOAD_CONST              17 (('type', 'default', 'help'))
              CALL_KW                  4
              POP_TOP

258           LOAD_FAST_BORROW         2 (p)
              LOAD_ATTR               11 (add_argument + NULL|self)

259           LOAD_CONST              22 ('--warning-count')
              LOAD_GLOBAL             14 (int)
              LOAD_SMALL_INT           0

260           LOAD_CONST              23 ('Structural warnings emitted by the verification.')

258           LOAD_CONST              17 (('type', 'default', 'help'))
              CALL_KW                  4
              POP_TOP

262           LOAD_FAST_BORROW         2 (p)
              LOAD_ATTR               11 (add_argument + NULL|self)

263           LOAD_CONST              24 ('--error-code')
              LOAD_CONST               6 (None)

264           LOAD_CONST              25 ('Closed structural error code, e.g. audit_window_chain_broken.')

262           LOAD_CONST               8 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

266           LOAD_FAST_BORROW         2 (p)
              LOAD_ATTR               11 (add_argument + NULL|self)

267           LOAD_CONST              26 ('--actor-id')
              LOAD_CONST               6 (None)

268           LOAD_CONST              27 ('Operator actor token. Bounded to [A-Za-z0-9_-]+.')

266           LOAD_CONST               8 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

270           LOAD_FAST_BORROW         2 (p)
              LOAD_ATTR               11 (add_argument + NULL|self)

271           LOAD_CONST              28 ('--execute')
              LOAD_CONST              29 ('store_true')

272           LOAD_CONST              30 ('Actually INSERT. Without this flag the script runs in dry-run mode.')

270           LOAD_CONST              31 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

274           LOAD_FAST_BORROW         2 (p)
              LOAD_ATTR               11 (add_argument + NULL|self)

275           LOAD_CONST              32 ('--json')
              LOAD_CONST              29 ('store_true')

276           LOAD_CONST              33 ('Emit JSON on stdout instead of the human summary.')

274           LOAD_CONST              31 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

278           LOAD_FAST_BORROW         2 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "scripts/persist_audit_verification_run.py", line 281>:
281           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C18644F20, file "scripts/persist_audit_verification_run.py", line 281>:
281           RESUME                   0

282           LOAD_FAST_BORROW         0 (env)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               0 ('record')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L1:     STORE_FAST               1 (rec)

283           LOAD_FAST_BORROW         0 (env)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               1 ('run_row')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L2:     STORE_FAST               2 (row)

284           LOAD_GLOBAL              3 (print + NULL)

285           LOAD_CONST               2 ('[PAS178/persist_audit_verification_run] status=')

286           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST               3 ('status')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' dry_run=')

287           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST               5 ('dry_run')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' brokerage_id=')

288           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST               7 ('brokerage_id')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' verification_type=')

289           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST               9 ('verification_type')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              10 (' run_status=')

290           LOAD_FAST_BORROW         0 (env)
              LOAD_CONST              11 ('run_status')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              12 (' record_id=')

291           LOAD_FAST_BORROW         1 (rec)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              13 ('verification_run_id')
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST              14 (' row_id=')

292           LOAD_FAST_BORROW         2 (row)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              13 ('verification_run_id')
              CALL                     1
              FORMAT_SIMPLE

285           BUILD_STRING            14

284           CALL                     1
              POP_TOP

294           LOAD_FAST_BORROW         0 (env)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              15 ('error_code')
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       22 (to L3)
              NOT_TAKEN

295           LOAD_GLOBAL              3 (print + NULL)
              LOAD_CONST              16 ('  error_code=')
              LOAD_FAST_BORROW         0 (env)
              LOAD_CONST              15 ('error_code')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP

296   L3:     LOAD_FAST_BORROW         0 (env)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              17 ('warnings')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L4:     LOAD_CONST              18 (slice(None, 10, None))
              BINARY_OP               26 ([])
              GET_ITER
      L5:     FOR_ITER                17 (to L6)
              STORE_FAST               3 (w)

297           LOAD_GLOBAL              3 (print + NULL)
              LOAD_CONST              19 ('  warn: ')
              LOAD_FAST_BORROW         3 (w)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L5)

296   L6:     END_FOR
              POP_ITER
              LOAD_CONST              20 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "scripts/persist_audit_verification_run.py", line 300>:
300           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17D6DFC0, file "scripts/persist_audit_verification_run.py", line 300>:
 300            RESUME                   0

 301            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 302            NOP

 303    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 307    L2:     LOAD_GLOBAL             11 (persist + NULL)

 308            LOAD_FAST                2 (args)
                LOAD_ATTR               12 (brokerage_id)

 309            LOAD_FAST                2 (args)
                LOAD_ATTR               14 (verification_type)

 310            LOAD_FAST                2 (args)
                LOAD_ATTR               16 (status)

 311            LOAD_FAST                2 (args)
                LOAD_ATTR               18 (checked_window_count)

 312            LOAD_FAST                2 (args)
                LOAD_ATTR               20 (checked_audit_row_count)

 313            LOAD_FAST                2 (args)
                LOAD_ATTR               22 (broken_chain_count)

 314            LOAD_FAST                2 (args)
                LOAD_ATTR               24 (warning_count)

 315            LOAD_FAST                2 (args)
                LOAD_ATTR               26 (error_code)

 316            LOAD_FAST                2 (args)
                LOAD_ATTR               28 (actor_id)

 317            LOAD_FAST                2 (args)
                LOAD_ATTR               30 (execute)
                TO_BOOL
                UNARY_NOT

 307            LOAD_CONST               2 (('brokerage_id', 'verification_type', 'run_status', 'checked_window_count', 'checked_audit_row_count', 'broken_chain_count', 'warning_count', 'error_code', 'actor_id', 'dry_run'))
                CALL_KW                 10
                STORE_FAST               4 (env)

 320            LOAD_FAST                2 (args)
                LOAD_ATTR               32 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       36 (to L3)
                NOT_TAKEN

 321            LOAD_GLOBAL             35 (print + NULL)
                LOAD_GLOBAL             32 (json)
                LOAD_ATTR               36 (dumps)
                PUSH_NULL
                LOAD_FAST                4 (env)
                LOAD_SMALL_INT           2
                LOAD_CONST               3 (True)
                LOAD_CONST               4 (('indent', 'sort_keys'))
                CALL_KW                  3
                CALL                     1
                POP_TOP
                JUMP_FORWARD            11 (to L4)

 323    L3:     LOAD_GLOBAL             39 (_print_summary + NULL)
                LOAD_FAST                4 (env)
                CALL                     1
                POP_TOP

 325    L4:     LOAD_FAST                4 (env)
                LOAD_ATTR               41 (get + NULL|self)
                LOAD_CONST               5 ('status')
                CALL                     1
                STORE_FAST               5 (status)

 326            LOAD_FAST                5 (status)
                LOAD_CONST               7 (('ok', 'skipped'))
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN

 327            LOAD_SMALL_INT           0
                RETURN_VALUE

 328    L5:     LOAD_SMALL_INT           1
                RETURN_VALUE

  --    L6:     PUSH_EXC_INFO

 304            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L15)
                NOT_TAKEN
                STORE_FAST               3 (e)

 305    L7:     LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                LOAD_CONST               6 ((0, None))
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_SMALL_INT           2
                JUMP_FORWARD            30 (to L12)
        L8:     LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L11)
        L9:     NOT_TAKEN
       L10:     POP_TOP
                LOAD_SMALL_INT           0
       L11:     CALL                     1
       L12:     SWAP                     2
       L13:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RETURN_VALUE

  --   L14:     LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 304   L15:     RERAISE                  0

  --   L16:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L6 [0]
  L6 to L7 -> L16 [1] lasti
  L7 to L9 -> L14 [1] lasti
  L10 to L12 -> L14 [1] lasti
  L12 to L13 -> L16 [1] lasti
  L14 to L16 -> L16 [1] lasti
```
