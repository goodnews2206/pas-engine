# scripts_readiness/run_monitoring_check

- **pyc:** `scripts\__pycache__\run_monitoring_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/run_monitoring_check.py`
- **co_filename (from bytecode):** `scripts\run_monitoring_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS143F2 — Monitoring CLI.

Reads upstream report files (security audit, integrity check, backup
verification), runs detectors against them, and emits
`monitoring_report.json` plus a human-readable summary.

In-process only. No external dispatch. PAS143G will add transport.

Usage:
  python scripts/run_monitoring_check.py
  python scripts/run_monitoring_check.py --strict
  python scripts/run_monitoring_check.py --json
  python scripts/run_monitoring_check.py \
      --security-report security_audit_report.json \
      --integrity-report integrity_check_report.json \
      --backup-report backups/20260509_141500/verification_report.json

Exit codes:
  0   no CRITICAL/HIGH alerts (or --strict not passed)
  1   --strict and any CRITICAL/HIGH alert (or safe_to_continue=False)
  2   bad CLI arguments
```

## Imports

`List`, `Optional`, `Path`, `__future__`, `annotations`, `app.services.monitoring.detectors`, `app.services.monitoring.report`, `argparse`, `detect_backup_verification`, `detect_integrity_findings`, `detect_restore_drill_failures`, `detect_security_findings`, `generate_monitoring_report`, `json`, `os`, `pathlib`, `summarize_monitoring_report`, `sys`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_autodiscover`, `_safe_read_json`, `main`

## Env-key candidates

`CRITICAL`, `HIGH`

## String constants (redacted where noted)

- '\nPAS143F2 — Monitoring CLI.\n\nReads upstream report files (security audit, integrity check, backup\nverification), runs detectors against them, and emits\n`monitoring_report.json` plus a human-readable summary.\n\nIn-process only. No external dispatch. PAS143G will add transport.\n\nUsage:\n  python scripts/run_monitoring_check.py\n  python scripts/run_monitoring_check.py --strict\n  python scripts/run_monitoring_check.py --json\n  python scripts/run_monitoring_check.py \\\n      --security-report security_audit_report.json \\\n      --integrity-report integrity_check_report.json \\\n      --backup-report backups/20260509_141500/verification_report.json\n\nExit codes:\n  0   no CRITICAL/HIGH alerts (or --strict not passed)\n  1   --strict and any CRITICAL/HIGH alert (or safe_to_continue=False)\n  2   bad CLI arguments\n'
- 'utf-8'
- 'path'
- 'Optional[str]'
- 'label'
- 'str'
- 'return'
- 'Optional[dict]'
- '\nLoad JSON from disk; never raise. Returns None when path is\nabsent / unreadable / not JSON. Prints an operator hint on failure.\n'
- '  [warn] '
- ': not found at '
- ': unreadable ('
- 'name'
- 'Look for a sibling report in CWD; returns its path if present.'
- 'argv'
- 'Optional[list]'
- 'int'
- 'run_monitoring_check'
- 'PAS143F2 — aggregate audit / integrity / backup outputs into an operator-facing monitoring report.'
- '--security-report'
- 'Path to security_audit_report.json (default: auto-discover in CWD).'
- '--integrity-report'
- 'Path to integrity_check_report.json (default: auto-discover in CWD).'
- '--backup-report'
- 'Path to a verify_backup verification_report.json. No default.'
- '--restore-report'
- 'PAS143G — path to a restore_drill_report.json. No default.'
- '--json'
- 'store_true'
- 'Emit the monitoring report as JSON instead of the human view.'
- '--strict'
- 'Exit 1 if any CRITICAL or HIGH alert is present.'
- 'security_audit_report.json'
- 'integrity_check_report.json'
- 'security report'
- 'integrity report'
- 'backup verification report'
- 'restore drill report'
- 'monitoring_report.json'
- '  [warn] could not write monitoring_report.json: '
- 'Inputs consumed:'
- '  security:  '
- '(none)'
- '  integrity: '
- '  backup:    '
- '  restore:   '
- '  report: '
- 'by_severity'
- 'CRITICAL'
- 'HIGH'
- 'safe_to_continue'

## Disassembly

```
   0            RESUME                   0

   1            LOAD_CONST               0 ('\nPAS143F2 — Monitoring CLI.\n\nReads upstream report files (security audit, integrity check, backup\nverification), runs detectors against them, and emits\n`monitoring_report.json` plus a human-readable summary.\n\nIn-process only. No external dispatch. PAS143G will add transport.\n\nUsage:\n  python scripts/run_monitoring_check.py\n  python scripts/run_monitoring_check.py --strict\n  python scripts/run_monitoring_check.py --json\n  python scripts/run_monitoring_check.py \\\n      --security-report security_audit_report.json \\\n      --integrity-report integrity_check_report.json \\\n      --backup-report backups/20260509_141500/verification_report.json\n\nExit codes:\n  0   no CRITICAL/HIGH alerts (or --strict not passed)\n  1   --strict and any CRITICAL/HIGH alert (or safe_to_continue=False)\n  2   bad CLI arguments\n')
                STORE_NAME               0 (__doc__)

  25            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('annotations',))
                IMPORT_NAME              1 (__future__)
                IMPORT_FROM              2 (annotations)
                STORE_NAME               2 (annotations)
                POP_TOP

  27            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              3 (argparse)
                STORE_NAME               3 (argparse)

  28            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              4 (json)
                STORE_NAME               4 (json)

  29            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              5 (os)
                STORE_NAME               5 (os)

  30            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              6 (sys)
                STORE_NAME               6 (sys)

  31            LOAD_SMALL_INT           0
                LOAD_CONST               3 (('Path',))
                IMPORT_NAME              7 (pathlib)
                IMPORT_FROM              8 (Path)
                STORE_NAME               8 (Path)
                POP_TOP

  32            LOAD_SMALL_INT           0
                LOAD_CONST               4 (('List', 'Optional'))
                IMPORT_NAME              9 (typing)
                IMPORT_FROM             10 (List)
                STORE_NAME              10 (List)
                IMPORT_FROM             11 (Optional)
                STORE_NAME              11 (Optional)
                POP_TOP

  36            LOAD_NAME                6 (sys)
                LOAD_ATTR               24 (stdout)
                LOAD_NAME                6 (sys)
                LOAD_ATTR               26 (stderr)
                BUILD_TUPLE              2
                GET_ITER
        L1:     FOR_ITER                22 (to L4)
                STORE_NAME              14 (_stream)

  37            NOP

  38    L2:     LOAD_NAME               14 (_stream)
                LOAD_ATTR               31 (reconfigure + NULL|self)
                LOAD_CONST               5 ('utf-8')
                LOAD_CONST               6 (('encoding',))
                CALL_KW                  1
                POP_TOP
        L3:     JUMP_BACKWARD           24 (to L1)

  36    L4:     END_FOR
                POP_ITER

  43            LOAD_NAME                5 (os)
                LOAD_ATTR               34 (path)
                LOAD_ATTR               37 (abspath + NULL|self)
                LOAD_NAME                5 (os)
                LOAD_ATTR               34 (path)
                LOAD_ATTR               39 (join + NULL|self)
                LOAD_NAME                5 (os)
                LOAD_ATTR               34 (path)
                LOAD_ATTR               41 (dirname + NULL|self)
                LOAD_NAME               21 (__file__)
                CALL                     1
                LOAD_CONST               7 ('..')
                CALL                     2
                CALL                     1
                STORE_NAME              22 (_REPO_ROOT)

  44            LOAD_NAME               22 (_REPO_ROOT)
                LOAD_NAME                6 (sys)
                LOAD_ATTR               34 (path)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       29 (to L5)
                NOT_TAKEN

  45            LOAD_NAME                6 (sys)
                LOAD_ATTR               34 (path)
                LOAD_ATTR               47 (insert + NULL|self)
                LOAD_SMALL_INT           0
                LOAD_NAME               22 (_REPO_ROOT)
                CALL                     2
                POP_TOP

  48    L5:     LOAD_SMALL_INT           0
                LOAD_CONST               8 (('detect_backup_verification', 'detect_integrity_findings', 'detect_restore_drill_failures', 'detect_security_findings'))
                IMPORT_NAME             24 (app.services.monitoring.detectors)
                IMPORT_FROM             25 (detect_backup_verification)
                STORE_NAME              25 (detect_backup_verification)
                IMPORT_FROM             26 (detect_integrity_findings)
                STORE_NAME              26 (detect_integrity_findings)
                IMPORT_FROM             27 (detect_restore_drill_failures)
                STORE_NAME              27 (detect_restore_drill_failures)
                IMPORT_FROM             28 (detect_security_findings)
                STORE_NAME              28 (detect_security_findings)
                POP_TOP

  54            LOAD_SMALL_INT           0
                LOAD_CONST               9 (('generate_monitoring_report', 'summarize_monitoring_report'))
                IMPORT_NAME             29 (app.services.monitoring.report)
                IMPORT_FROM             30 (generate_monitoring_report)
                STORE_NAME              30 (generate_monitoring_report)
                IMPORT_FROM             31 (summarize_monitoring_report)
                STORE_NAME              31 (summarize_monitoring_report)
                POP_TOP

  64            LOAD_CONST              10 (<code object __annotate__ at 0x0000018C18024C30, file "scripts\run_monitoring_check.py", line 64>)
                MAKE_FUNCTION
                LOAD_CONST              11 (<code object _safe_read_json at 0x0000018C17F7CFB0, file "scripts\run_monitoring_check.py", line 64>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              32 (_safe_read_json)

  82            LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA3780, file "scripts\run_monitoring_check.py", line 82>)
                MAKE_FUNCTION
                LOAD_CONST              13 (<code object _autodiscover at 0x0000018C17FE13E0, file "scripts\run_monitoring_check.py", line 82>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              33 (_autodiscover)

  92            LOAD_CONST              17 ((None,))
                LOAD_CONST              14 (<code object __annotate__ at 0x0000018C17FA2F10, file "scripts\run_monitoring_check.py", line 92>)
                MAKE_FUNCTION
                LOAD_CONST              15 (<code object main at 0x0000018C17E809D0, file "scripts\run_monitoring_check.py", line 92>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                SET_FUNCTION_ATTRIBUTE   1 (defaults)
                STORE_NAME              34 (main)

 186            LOAD_NAME               35 (__name__)
                LOAD_CONST              16 ('__main__')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       14 (to L6)
                NOT_TAKEN

 187            LOAD_NAME               36 (SystemExit)
                PUSH_NULL
                LOAD_NAME               34 (main)
                PUSH_NULL
                CALL                     0
                CALL                     1
                RAISE_VARARGS            1

 186    L6:     LOAD_CONST               2 (None)
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

  39            LOAD_NAME               16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L9)
                NOT_TAKEN
                POP_TOP

  40    L8:     POP_EXCEPT
                JUMP_BACKWARD          221 (to L1)

  39    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L7 [1]
  L7 to L8 -> L10 [2] lasti
  L9 to L10 -> L10 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "scripts\run_monitoring_check.py", line 64>:
 64           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('path')
              LOAD_CONST               2 ('Optional[str]')
              LOAD_CONST               3 ('label')
              LOAD_CONST               4 ('str')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('Optional[dict]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _safe_read_json at 0x0000018C17F7CFB0, file "scripts\run_monitoring_check.py", line 64>:
  64            RESUME                   0

  69            LOAD_FAST_BORROW         0 (path)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN

  70            LOAD_CONST               1 (None)
                RETURN_VALUE

  71    L1:     LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (path)
                CALL                     1
                STORE_FAST               2 (p)

  72            LOAD_FAST_BORROW         2 (p)
                LOAD_ATTR                3 (exists + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        36 (to L2)
                NOT_TAKEN

  73            LOAD_GLOBAL              5 (print + NULL)
                LOAD_CONST               2 ('  [warn] ')
                LOAD_FAST_BORROW         1 (label)
                FORMAT_SIMPLE
                LOAD_CONST               3 (': not found at ')
                LOAD_FAST_BORROW         0 (path)
                FORMAT_SIMPLE
                BUILD_STRING             4
                LOAD_GLOBAL              6 (sys)
                LOAD_ATTR                8 (stderr)
                LOAD_CONST               4 (('file',))
                CALL_KW                  2
                POP_TOP

  74            LOAD_CONST               1 (None)
                RETURN_VALUE

  75    L2:     NOP

  76    L3:     LOAD_GLOBAL             10 (json)
                LOAD_ATTR               12 (loads)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (p)
                LOAD_ATTR               15 (read_text + NULL|self)
                LOAD_CONST               5 ('utf-8')
                LOAD_CONST               6 (('encoding',))
                CALL_KW                  1
                CALL                     1
        L4:     RETURN_VALUE

  --    L5:     PUSH_EXC_INFO

  77            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       65 (to L9)
                NOT_TAKEN
                STORE_FAST               3 (e)

  78    L6:     LOAD_GLOBAL              5 (print + NULL)
                LOAD_CONST               2 ('  [warn] ')
                LOAD_FAST                1 (label)
                FORMAT_SIMPLE
                LOAD_CONST               7 (': unreadable (')
                LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE
                LOAD_CONST               8 (')')
                BUILD_STRING             5
                LOAD_GLOBAL              6 (sys)
                LOAD_ATTR                8 (stderr)
                LOAD_CONST               4 (('file',))
                CALL_KW                  2
                POP_TOP

  79    L7:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                LOAD_CONST               1 (None)
                RETURN_VALUE

  --    L8:     LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

  77    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L5 [0]
  L5 to L6 -> L10 [1] lasti
  L6 to L7 -> L8 [1] lasti
  L8 to L10 -> L10 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "scripts\run_monitoring_check.py", line 82>:
 82           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('name')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _autodiscover at 0x0000018C17FE13E0, file "scripts\run_monitoring_check.py", line 82>:
 82           RESUME                   0

 84           LOAD_GLOBAL              0 (Path)
              LOAD_ATTR                2 (cwd)
              PUSH_NULL
              CALL                     0
              LOAD_FAST_BORROW         0 (name)
              BINARY_OP               11 (/)
              STORE_FAST               1 (candidate)

 85           LOAD_FAST_BORROW         1 (candidate)
              LOAD_ATTR                5 (exists + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_FALSE       12 (to L1)
              NOT_TAKEN
              LOAD_GLOBAL              7 (str + NULL)
              LOAD_FAST_BORROW         1 (candidate)
              CALL                     1
              RETURN_VALUE
      L1:     LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "scripts\run_monitoring_check.py", line 92>:
 92           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('argv')
              LOAD_CONST               2 ('Optional[list]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('int')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object main at 0x0000018C17E809D0, file "scripts\run_monitoring_check.py", line 92>:
  92            RESUME                   0

  93            LOAD_GLOBAL              0 (argparse)
                LOAD_ATTR                2 (ArgumentParser)
                PUSH_NULL

  94            LOAD_CONST               0 ('run_monitoring_check')

  95            LOAD_CONST               1 ('PAS143F2 — aggregate audit / integrity / backup outputs into an operator-facing monitoring report.')

  93            LOAD_CONST               2 (('prog', 'description'))
                CALL_KW                  2
                STORE_FAST               1 (parser)

  98            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)

  99            LOAD_CONST               3 ('--security-report')

 100            LOAD_CONST               4 (None)

 101            LOAD_CONST               5 ('Path to security_audit_report.json (default: auto-discover in CWD).')

  98            LOAD_CONST               6 (('default', 'help'))
                CALL_KW                  3
                POP_TOP

 103            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)

 104            LOAD_CONST               7 ('--integrity-report')

 105            LOAD_CONST               4 (None)

 106            LOAD_CONST               8 ('Path to integrity_check_report.json (default: auto-discover in CWD).')

 103            LOAD_CONST               6 (('default', 'help'))
                CALL_KW                  3
                POP_TOP

 108            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)

 109            LOAD_CONST               9 ('--backup-report')

 110            LOAD_CONST               4 (None)

 111            LOAD_CONST              10 ('Path to a verify_backup verification_report.json. No default.')

 108            LOAD_CONST               6 (('default', 'help'))
                CALL_KW                  3
                POP_TOP

 113            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)

 114            LOAD_CONST              11 ('--restore-report')

 115            LOAD_CONST               4 (None)

 116            LOAD_CONST              12 ('PAS143G — path to a restore_drill_report.json. No default.')

 113            LOAD_CONST               6 (('default', 'help'))
                CALL_KW                  3
                POP_TOP

 118            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)

 119            LOAD_CONST              13 ('--json')

 120            LOAD_CONST              14 ('store_true')

 121            LOAD_CONST              15 ('Emit the monitoring report as JSON instead of the human view.')

 118            LOAD_CONST              16 (('action', 'help'))
                CALL_KW                  3
                POP_TOP

 123            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)

 124            LOAD_CONST              17 ('--strict')

 125            LOAD_CONST              14 ('store_true')

 126            LOAD_CONST              18 ('Exit 1 if any CRITICAL or HIGH alert is present.')

 123            LOAD_CONST              16 (('action', 'help'))
                CALL_KW                  3
                POP_TOP

 128            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                7 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 131            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR                8 (security_report)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        12 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_GLOBAL             11 (_autodiscover + NULL)
                LOAD_CONST              19 ('security_audit_report.json')
                CALL                     1
        L1:     STORE_FAST               3 (sec_path)

 132            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               12 (integrity_report)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        12 (to L2)
                NOT_TAKEN
                POP_TOP
                LOAD_GLOBAL             11 (_autodiscover + NULL)
                LOAD_CONST              20 ('integrity_check_report.json')
                CALL                     1
        L2:     STORE_FAST               4 (int_path)

 133            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               14 (backup_report)
                STORE_FAST               5 (bak_path)

 135            BUILD_LIST               0
                STORE_FAST               6 (alerts)

 137            LOAD_GLOBAL             17 (_safe_read_json + NULL)
                LOAD_FAST_BORROW         3 (sec_path)
                LOAD_CONST              21 ('security report')
                CALL                     2
                STORE_FAST               7 (sec)

 138            LOAD_FAST_BORROW         7 (sec)
                POP_JUMP_IF_NONE        27 (to L3)
                NOT_TAKEN

 139            LOAD_FAST_BORROW         6 (alerts)
                LOAD_ATTR               19 (extend + NULL|self)
                LOAD_GLOBAL             21 (detect_security_findings + NULL)
                LOAD_FAST_BORROW         7 (sec)
                CALL                     1
                CALL                     1
                POP_TOP

 141    L3:     LOAD_GLOBAL             17 (_safe_read_json + NULL)
                LOAD_FAST_BORROW         4 (int_path)
                LOAD_CONST              22 ('integrity report')
                CALL                     2
                STORE_FAST               8 (integ)

 142            LOAD_FAST_BORROW         8 (integ)
                POP_JUMP_IF_NONE        27 (to L4)
                NOT_TAKEN

 143            LOAD_FAST_BORROW         6 (alerts)
                LOAD_ATTR               19 (extend + NULL|self)
                LOAD_GLOBAL             23 (detect_integrity_findings + NULL)
                LOAD_FAST_BORROW         8 (integ)
                CALL                     1
                CALL                     1
                POP_TOP

 145    L4:     LOAD_GLOBAL             17 (_safe_read_json + NULL)
                LOAD_FAST_BORROW         5 (bak_path)
                LOAD_CONST              23 ('backup verification report')
                CALL                     2
                STORE_FAST               9 (bak)

 146            LOAD_FAST_BORROW         9 (bak)
                POP_JUMP_IF_NONE        27 (to L5)
                NOT_TAKEN

 147            LOAD_FAST_BORROW         6 (alerts)
                LOAD_ATTR               19 (extend + NULL|self)
                LOAD_GLOBAL             25 (detect_backup_verification + NULL)
                LOAD_FAST_BORROW         9 (bak)
                CALL                     1
                CALL                     1
                POP_TOP

 150    L5:     LOAD_GLOBAL             17 (_safe_read_json + NULL)
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               26 (restore_report)
                LOAD_CONST              24 ('restore drill report')
                CALL                     2
                STORE_FAST              10 (drill)

 151            LOAD_FAST_BORROW        10 (drill)
                POP_JUMP_IF_NONE        27 (to L6)
                NOT_TAKEN

 152            LOAD_FAST_BORROW         6 (alerts)
                LOAD_ATTR               19 (extend + NULL|self)
                LOAD_GLOBAL             29 (detect_restore_drill_failures + NULL)
                LOAD_FAST_BORROW        10 (drill)
                CALL                     1
                CALL                     1
                POP_TOP

 154    L6:     LOAD_GLOBAL             31 (generate_monitoring_report + NULL)
                LOAD_FAST_BORROW         6 (alerts)
                CALL                     1
                STORE_FAST              11 (report)

 157            LOAD_GLOBAL             32 (Path)
                LOAD_ATTR               34 (cwd)
                PUSH_NULL
                CALL                     0
                LOAD_CONST              25 ('monitoring_report.json')
                BINARY_OP               11 (/)
                STORE_FAST              12 (out_path)

 158            NOP

 159    L7:     LOAD_FAST_BORROW        12 (out_path)
                LOAD_ATTR               37 (write_text + NULL|self)
                LOAD_GLOBAL             38 (json)
                LOAD_ATTR               40 (dumps)
                PUSH_NULL
                LOAD_FAST_BORROW        11 (report)
                LOAD_SMALL_INT           2
                LOAD_CONST              26 (('indent',))
                CALL_KW                  2
                LOAD_CONST              27 ('utf-8')
                LOAD_CONST              28 (('encoding',))
                CALL_KW                  2
                POP_TOP

 163    L8:     LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L9)
                NOT_TAKEN

 164            LOAD_GLOBAL             45 (print + NULL)
                LOAD_GLOBAL             38 (json)
                LOAD_ATTR               40 (dumps)
                PUSH_NULL
                LOAD_FAST_BORROW        11 (report)
                LOAD_SMALL_INT           2
                LOAD_CONST              26 (('indent',))
                CALL_KW                  2
                CALL                     1
                POP_TOP
                JUMP_FORWARD           171 (to L14)

 168    L9:     LOAD_GLOBAL             45 (print + NULL)
                CALL                     0
                POP_TOP

 169            LOAD_GLOBAL             45 (print + NULL)
                LOAD_CONST              31 ('Inputs consumed:')
                CALL                     1
                POP_TOP

 170            LOAD_GLOBAL             45 (print + NULL)
                LOAD_CONST              32 ('  security:  ')
                LOAD_FAST                3 (sec_path)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              33 ('(none)')
       L10:     FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 171            LOAD_GLOBAL             45 (print + NULL)
                LOAD_CONST              34 ('  integrity: ')
                LOAD_FAST                4 (int_path)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L11)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              33 ('(none)')
       L11:     FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 172            LOAD_GLOBAL             45 (print + NULL)
                LOAD_CONST              35 ('  backup:    ')
                LOAD_FAST                5 (bak_path)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              33 ('(none)')
       L12:     FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 173            LOAD_GLOBAL             45 (print + NULL)
                LOAD_CONST              36 ('  restore:   ')
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               26 (restore_report)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              33 ('(none)')
       L13:     FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 174            LOAD_GLOBAL             45 (print + NULL)
                CALL                     0
                POP_TOP

 175            LOAD_GLOBAL             45 (print + NULL)
                LOAD_GLOBAL             51 (summarize_monitoring_report + NULL)
                LOAD_FAST_BORROW        11 (report)
                CALL                     1
                CALL                     1
                POP_TOP

 176            LOAD_GLOBAL             45 (print + NULL)
                LOAD_CONST              37 ('  report: ')
                LOAD_FAST_BORROW        12 (out_path)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 178   L14:     LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               52 (strict)
                TO_BOOL
                POP_JUMP_IF_FALSE      125 (to L18)
                NOT_TAKEN

 179            LOAD_FAST_BORROW        11 (report)
                LOAD_ATTR               55 (get + NULL|self)
                LOAD_CONST              38 ('by_severity')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L15)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
       L15:     LOAD_ATTR               55 (get + NULL|self)
                LOAD_CONST              39 ('CRITICAL')
                LOAD_SMALL_INT           0
                CALL                     2
                STORE_FAST              14 (crit)

 180            LOAD_FAST_BORROW        11 (report)
                LOAD_ATTR               55 (get + NULL|self)
                LOAD_CONST              38 ('by_severity')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L16)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
       L16:     LOAD_ATTR               55 (get + NULL|self)
                LOAD_CONST              40 ('HIGH')
                LOAD_SMALL_INT           0
                CALL                     2
                STORE_FAST              15 (high)

 181            LOAD_FAST_BORROW        11 (report)
                LOAD_ATTR               55 (get + NULL|self)
                LOAD_CONST              41 ('safe_to_continue')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       14 (to L17)
                NOT_TAKEN
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 239 (crit, high)
                BINARY_OP                0 (+)
                LOAD_SMALL_INT           0
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE        3 (to L18)
                NOT_TAKEN

 182   L17:     LOAD_SMALL_INT           1
                RETURN_VALUE

 183   L18:     LOAD_SMALL_INT           0
                RETURN_VALUE

  --   L19:     PUSH_EXC_INFO

 160            LOAD_GLOBAL             42 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       42 (to L23)
                NOT_TAKEN
                STORE_FAST              13 (e)

 161   L20:     LOAD_GLOBAL             45 (print + NULL)
                LOAD_CONST              29 ('  [warn] could not write monitoring_report.json: ')
                LOAD_FAST               13 (e)
                FORMAT_SIMPLE
                BUILD_STRING             2
                LOAD_GLOBAL             46 (sys)
                LOAD_ATTR               48 (stderr)
                LOAD_CONST              30 (('file',))
                CALL_KW                  2
                POP_TOP
       L21:     POP_EXCEPT
                LOAD_CONST               4 (None)
                STORE_FAST              13 (e)
                DELETE_FAST             13 (e)
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 414 (to L8)

  --   L22:     LOAD_CONST               4 (None)
                STORE_FAST              13 (e)
                DELETE_FAST             13 (e)
                RERAISE                  1

 160   L23:     RERAISE                  0

  --   L24:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L7 to L8 -> L19 [0]
  L19 to L20 -> L24 [1] lasti
  L20 to L21 -> L22 [1] lasti
  L22 to L24 -> L24 [1] lasti
```
