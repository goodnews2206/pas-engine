# scripts_readiness/security_dependency_audit

- **pyc:** `scripts\__pycache__\security_dependency_audit.cpython-314.pyc`
- **expected source path (absent):** `scripts/security_dependency_audit.py`
- **co_filename (from bytecode):** `scripts/security_dependency_audit.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS-SECURITY-02 — Operator-runnable dependency audit CLI.

Report-only wrapper around
``app.services.security.dependency_scanner``. Runs
``pip-audit`` and/or ``npm audit`` if locally available; emits
a bounded structural envelope.

Doctrine:

* **Report-only.** No auto-fix, no upgrades, no lockfile
  modification.
* **Scanner-unavailable is NOT a failure.** Operators see a
  structural warning so they can install / wire the scanner
  out-of-band.
* **No secrets.** Subprocess env is stripped to PATH + locale.
  Stdout is parsed for bounded counts only — the raw report
  is NEVER returned.
* **NEVER raises.**

Usage:

    python scripts/security_dependency_audit.py
    python scripts/security_dependency_audit.py --json
    python scripts/security_dependency_audit.py --python-only
    python scripts/security_dependency_audit.py --node-only

Exit codes:
    0 — ok / warning / scanner_unavailable
    1 — failed
    2 — bad CLI arguments
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.services.security.dependency_scanner`, `argparse`, `json`, `logging`, `os`, `scan_node_dependencies`, `scan_python_dependencies`, `sys`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_build_parser`, `_print_summary`, `main`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS-SECURITY-02 — Operator-runnable dependency audit CLI.\n\nReport-only wrapper around\n``app.services.security.dependency_scanner``. Runs\n``pip-audit`` and/or ``npm audit`` if locally available; emits\na bounded structural envelope.\n\nDoctrine:\n\n* **Report-only.** No auto-fix, no upgrades, no lockfile\n  modification.\n* **Scanner-unavailable is NOT a failure.** Operators see a\n  structural warning so they can install / wire the scanner\n  out-of-band.\n* **No secrets.** Subprocess env is stripped to PATH + locale.\n  Stdout is parsed for bounded counts only — the raw report\n  is NEVER returned.\n* **NEVER raises.**\n\nUsage:\n\n    python scripts/security_dependency_audit.py\n    python scripts/security_dependency_audit.py --json\n    python scripts/security_dependency_audit.py --python-only\n    python scripts/security_dependency_audit.py --node-only\n\nExit codes:\n    0 — ok / warning / scanner_unavailable\n    1 — failed\n    2 — bad CLI arguments\n'
- 'utf-8'
- 'pas.scripts.security_dependency_audit'
- 'return'
- 'argparse.ArgumentParser'
- 'security_dependency_audit'
- 'PAS-SECURITY-02 — Report-only dependency audit. Detects pip-audit + npm audit availability locally and runs them if present. NEVER auto-fixes / NEVER upgrades / NEVER modifies lockfiles.'
- '--repo-root'
- "Repo root to scan. Defaults to script's parent dir."
- '--python-only'
- 'store_true'
- 'Skip npm audit even when package.json is present.'
- '--node-only'
- 'Skip pip-audit. Useful when only the frontend is in scope.'
- '--json'
- 'Emit JSON on stdout instead of the human summary.'
- 'env'
- 'Dict[str, Any]'
- 'None'
- 'python'
- 'node'
- '[PAS-SECURITY-02/dependency_audit] status='
- 'status'
- ' python.status='
- ' python.deps='
- 'dependency_count'
- ' python.vulns='
- 'vulnerability_count'
- ' node.status='
- ' node.deps='
- ' node.vulns='
- 'warnings'
- '  warn: '
- 'argv'
- 'Optional[List[str]]'
- 'int'
- 'error: --repo-root not a directory: '
- 'security_dependency_audit import error type='
- 'failed'
- 'import_failed:'
- 'error_code'
- 'import_failed'
- 'scanner'
- 'pip-audit'
- 'scanner_unavailable'
- 'lockfile'
- 'skipped_by_node_only_flag'
- 'npm'
- 'skipped_by_python_only_flag'
- 'warning'

## Disassembly

```
   0           RESUME                   0

   1           LOAD_CONST               0 ('\nPAS-SECURITY-02 — Operator-runnable dependency audit CLI.\n\nReport-only wrapper around\n``app.services.security.dependency_scanner``. Runs\n``pip-audit`` and/or ``npm audit`` if locally available; emits\na bounded structural envelope.\n\nDoctrine:\n\n* **Report-only.** No auto-fix, no upgrades, no lockfile\n  modification.\n* **Scanner-unavailable is NOT a failure.** Operators see a\n  structural warning so they can install / wire the scanner\n  out-of-band.\n* **No secrets.** Subprocess env is stripped to PATH + locale.\n  Stdout is parsed for bounded counts only — the raw report\n  is NEVER returned.\n* **NEVER raises.**\n\nUsage:\n\n    python scripts/security_dependency_audit.py\n    python scripts/security_dependency_audit.py --json\n    python scripts/security_dependency_audit.py --python-only\n    python scripts/security_dependency_audit.py --node-only\n\nExit codes:\n    0 — ok / warning / scanner_unavailable\n    1 — failed\n    2 — bad CLI arguments\n')
               STORE_NAME               0 (__doc__)

  34           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  36           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  37           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (json)
               STORE_NAME               4 (json)

  38           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (logging)
               STORE_NAME               5 (logging)

  39           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (os)
               STORE_NAME               6 (os)

  40           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              7 (sys)
               STORE_NAME               7 (sys)

  41           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('Any', 'Dict', 'List', 'Optional'))
               IMPORT_NAME              8 (typing)
               IMPORT_FROM              9 (Any)
               STORE_NAME               9 (Any)
               IMPORT_FROM             10 (Dict)
               STORE_NAME              10 (Dict)
               IMPORT_FROM             11 (List)
               STORE_NAME              11 (List)
               IMPORT_FROM             12 (Optional)
               STORE_NAME              12 (Optional)
               POP_TOP

  44           LOAD_NAME                7 (sys)
               LOAD_ATTR               26 (stdout)
               LOAD_NAME                7 (sys)
               LOAD_ATTR               28 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              15 (_stream)

  45           NOP

  46   L2:     LOAD_NAME               15 (_stream)
               LOAD_ATTR               33 (reconfigure + NULL|self)
               LOAD_CONST               4 ('utf-8')
               LOAD_CONST               5 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  44   L4:     END_FOR
               POP_ITER

  51           LOAD_NAME                7 (sys)
               LOAD_ATTR               36 (path)
               LOAD_ATTR               39 (insert + NULL|self)
               LOAD_SMALL_INT           0
               LOAD_NAME                6 (os)
               LOAD_ATTR               36 (path)
               LOAD_ATTR               41 (abspath + NULL|self)
               LOAD_NAME                6 (os)
               LOAD_ATTR               36 (path)
               LOAD_ATTR               43 (join + NULL|self)
               LOAD_NAME                6 (os)
               LOAD_ATTR               36 (path)
               LOAD_ATTR               45 (dirname + NULL|self)
               LOAD_NAME               23 (__file__)
               CALL                     1
               LOAD_CONST               6 ('..')
               CALL                     2
               CALL                     1
               CALL                     2
               POP_TOP

  54           LOAD_NAME                5 (logging)
               LOAD_ATTR               48 (getLogger)
               PUSH_NULL
               LOAD_CONST               7 ('pas.scripts.security_dependency_audit')
               CALL                     1
               STORE_NAME              25 (logger)

  57           LOAD_CONST               8 (<code object __annotate__ at 0x0000018C17FA31E0, file "scripts/security_dependency_audit.py", line 57>)
               MAKE_FUNCTION
               LOAD_CONST               9 (<code object _build_parser at 0x0000018C18060F60, file "scripts/security_dependency_audit.py", line 57>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              26 (_build_parser)

  86           LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA3780, file "scripts/security_dependency_audit.py", line 86>)
               MAKE_FUNCTION
               LOAD_CONST              11 (<code object _print_summary at 0x0000018C17CD4970, file "scripts/security_dependency_audit.py", line 86>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              27 (_print_summary)

 103           LOAD_CONST              15 ((None,))
               LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA3E10, file "scripts/security_dependency_audit.py", line 103>)
               MAKE_FUNCTION
               LOAD_CONST              13 (<code object main at 0x0000018C17EA5230, file "scripts/security_dependency_audit.py", line 103>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              28 (main)

 178           LOAD_NAME               29 (__name__)
               LOAD_CONST              14 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 179           LOAD_NAME                7 (sys)
               LOAD_ATTR               60 (exit)
               PUSH_NULL
               LOAD_NAME               28 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 178   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  47           LOAD_NAME               17 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L8)
               NOT_TAKEN
               POP_TOP

  48   L7:     POP_EXCEPT
               JUMP_BACKWARD          212 (to L1)

  47   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "scripts/security_dependency_audit.py", line 57>:
 57           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C18060F60, file "scripts/security_dependency_audit.py", line 57>:
 57           RESUME                   0

 58           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

 59           LOAD_CONST               0 ('security_dependency_audit')

 61           LOAD_CONST               1 ('PAS-SECURITY-02 — Report-only dependency audit. Detects pip-audit + npm audit availability locally and runs them if present. NEVER auto-fixes / NEVER upgrades / NEVER modifies lockfiles.')

 58           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

 67           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

 68           LOAD_CONST               3 ('--repo-root')
              LOAD_CONST               4 (None)

 69           LOAD_CONST               5 ("Repo root to scan. Defaults to script's parent dir.")

 67           LOAD_CONST               6 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

 71           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

 72           LOAD_CONST               7 ('--python-only')
              LOAD_CONST               8 ('store_true')

 73           LOAD_CONST               9 ('Skip npm audit even when package.json is present.')

 71           LOAD_CONST              10 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

 75           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

 76           LOAD_CONST              11 ('--node-only')
              LOAD_CONST               8 ('store_true')

 77           LOAD_CONST              12 ('Skip pip-audit. Useful when only the frontend is in scope.')

 75           LOAD_CONST              10 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

 79           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

 80           LOAD_CONST              13 ('--json')
              LOAD_CONST               8 ('store_true')

 81           LOAD_CONST              14 ('Emit JSON on stdout instead of the human summary.')

 79           LOAD_CONST              10 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

 83           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "scripts/security_dependency_audit.py", line 86>:
 86           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C17CD4970, file "scripts/security_dependency_audit.py", line 86>:
 86           RESUME                   0

 87           LOAD_FAST_BORROW         0 (env)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               0 ('python')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L1:     STORE_FAST               1 (py)

 88           LOAD_FAST_BORROW         0 (env)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               1 ('node')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L2:     STORE_FAST               2 (nd)

 89           LOAD_GLOBAL              3 (print + NULL)

 90           LOAD_CONST               2 ('[PAS-SECURITY-02/dependency_audit] status=')

 91           LOAD_FAST_BORROW         0 (env)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               3 ('status')
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST               4 (' python.status=')

 92           LOAD_FAST_BORROW         1 (py)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               3 ('status')
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST               5 (' python.deps=')

 93           LOAD_FAST_BORROW         1 (py)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               6 ('dependency_count')
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST               7 (' python.vulns=')

 94           LOAD_FAST_BORROW         1 (py)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               8 ('vulnerability_count')
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST               9 (' node.status=')

 95           LOAD_FAST_BORROW         2 (nd)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               3 ('status')
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST              10 (' node.deps=')

 96           LOAD_FAST_BORROW         2 (nd)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               6 ('dependency_count')
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST              11 (' node.vulns=')

 97           LOAD_FAST_BORROW         2 (nd)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               8 ('vulnerability_count')
              CALL                     1
              FORMAT_SIMPLE

 90           BUILD_STRING            14

 89           CALL                     1
              POP_TOP

 99           LOAD_FAST_BORROW         0 (env)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              12 ('warnings')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L3:     LOAD_CONST              13 (slice(None, 10, None))
              BINARY_OP               26 ([])
              GET_ITER
      L4:     FOR_ITER                17 (to L5)
              STORE_FAST               3 (w)

100           LOAD_GLOBAL              3 (print + NULL)
              LOAD_CONST              14 ('  warn: ')
              LOAD_FAST_BORROW         3 (w)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L4)

 99   L5:     END_FOR
              POP_ITER
              LOAD_CONST              15 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "scripts/security_dependency_audit.py", line 103>:
103           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17EA5230, file "scripts/security_dependency_audit.py", line 103>:
 103            RESUME                   0

 104            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 105            NOP

 106    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 110    L2:     LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               15 (abspath + NULL|self)

 111            LOAD_FAST                2 (args)
                LOAD_ATTR               16 (repo_root)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        66 (to L3)
                NOT_TAKEN
                POP_TOP
                LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               19 (join + NULL|self)
                LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               21 (dirname + NULL|self)
                LOAD_GLOBAL             22 (__file__)
                CALL                     1
                LOAD_CONST               2 ('..')
                CALL                     2

 110    L3:     CALL                     1
                STORE_FAST               4 (repo_root)

 113            LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               25 (isdir + NULL|self)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L4)
                NOT_TAKEN

 114            LOAD_GLOBAL             27 (print + NULL)
                LOAD_CONST               3 ('error: --repo-root not a directory: ')
                LOAD_FAST                4 (repo_root)
                FORMAT_SIMPLE
                BUILD_STRING             2
                LOAD_GLOBAL             28 (sys)
                LOAD_ATTR               30 (stderr)
                LOAD_CONST               4 (('file',))
                CALL_KW                  2
                POP_TOP

 115            LOAD_SMALL_INT           2
                RETURN_VALUE

 117    L4:     NOP

 118    L5:     LOAD_SMALL_INT           0
                LOAD_CONST               5 (('scan_python_dependencies', 'scan_node_dependencies'))
                IMPORT_NAME             16 (app.services.security.dependency_scanner)
                IMPORT_FROM             17 (scan_python_dependencies)
                STORE_FAST               5 (scan_python_dependencies)
                IMPORT_FROM             18 (scan_node_dependencies)
                STORE_FAST               6 (scan_node_dependencies)
                POP_TOP

 140    L6:     LOAD_FAST                2 (args)
                LOAD_ATTR               54 (node_only)
                TO_BOOL
                POP_JUMP_IF_TRUE         9 (to L7)
                NOT_TAKEN

 139            LOAD_FAST                5 (scan_python_dependencies)
                PUSH_NULL
                LOAD_FAST                4 (repo_root)
                CALL                     1
                JUMP_FORWARD            16 (to L8)

 141    L7:     LOAD_CONST              17 ('scanner')
                LOAD_CONST              18 ('pip-audit')
                LOAD_CONST               7 ('status')
                LOAD_CONST              19 ('scanner_unavailable')

 142            LOAD_CONST              20 ('lockfile')
                LOAD_CONST               1 (None)
                LOAD_CONST              21 ('dependency_count')
                LOAD_SMALL_INT           0

 143            LOAD_CONST              22 ('vulnerability_count')
                LOAD_SMALL_INT           0
                LOAD_CONST              11 ('warnings')
                LOAD_CONST              23 ('skipped_by_node_only_flag')
                BUILD_LIST               1

 144            LOAD_CONST              13 ('error_code')
                LOAD_CONST              23 ('skipped_by_node_only_flag')

 141            BUILD_MAP                7

 138    L8:     STORE_FAST               8 (py)

 148            LOAD_FAST                2 (args)
                LOAD_ATTR               56 (python_only)
                TO_BOOL
                POP_JUMP_IF_TRUE         9 (to L9)
                NOT_TAKEN

 147            LOAD_FAST                6 (scan_node_dependencies)
                PUSH_NULL
                LOAD_FAST                4 (repo_root)
                CALL                     1
                JUMP_FORWARD            16 (to L10)

 149    L9:     LOAD_CONST              17 ('scanner')
                LOAD_CONST              24 ('npm')
                LOAD_CONST               7 ('status')
                LOAD_CONST              19 ('scanner_unavailable')

 150            LOAD_CONST              20 ('lockfile')
                LOAD_CONST               1 (None)
                LOAD_CONST              21 ('dependency_count')
                LOAD_SMALL_INT           0

 151            LOAD_CONST              22 ('vulnerability_count')
                LOAD_SMALL_INT           0
                LOAD_CONST              11 ('warnings')
                LOAD_CONST              25 ('skipped_by_python_only_flag')
                BUILD_LIST               1

 152            LOAD_CONST              13 ('error_code')
                LOAD_CONST              25 ('skipped_by_python_only_flag')

 149            BUILD_MAP                7

 146   L10:     STORE_FAST               9 (nd)

 155            LOAD_CONST              26 ('ok')
                STORE_FAST              10 (overall)

 156            LOAD_FAST                8 (py)
                LOAD_ATTR               59 (get + NULL|self)
                LOAD_CONST               7 ('status')
                CALL                     1
                LOAD_CONST              27 ('warning')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_TRUE        23 (to L11)
                NOT_TAKEN
                LOAD_FAST                9 (nd)
                LOAD_ATTR               59 (get + NULL|self)
                LOAD_CONST               7 ('status')
                CALL                     1
                LOAD_CONST              27 ('warning')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L12)
                NOT_TAKEN

 157   L11:     LOAD_CONST              27 ('warning')
                STORE_FAST              10 (overall)

 158   L12:     LOAD_FAST                8 (py)
                LOAD_ATTR               59 (get + NULL|self)
                LOAD_CONST               7 ('status')
                CALL                     1
                LOAD_CONST               8 ('failed')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_TRUE        23 (to L13)
                NOT_TAKEN
                LOAD_FAST                9 (nd)
                LOAD_ATTR               59 (get + NULL|self)
                LOAD_CONST               7 ('status')
                CALL                     1
                LOAD_CONST               8 ('failed')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L14)
                NOT_TAKEN

 159   L13:     LOAD_CONST              27 ('warning')
                STORE_FAST              10 (overall)

 162   L14:     LOAD_CONST               7 ('status')
                LOAD_FAST               10 (overall)

 163            LOAD_CONST               9 ('python')
                LOAD_FAST                8 (py)

 164            LOAD_CONST              10 ('node')
                LOAD_FAST                9 (nd)

 165            LOAD_CONST              11 ('warnings')
                LOAD_GLOBAL             61 (list + NULL)
                LOAD_FAST                8 (py)
                LOAD_ATTR               59 (get + NULL|self)
                LOAD_CONST              11 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L15)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
       L15:     CALL                     1
                LOAD_GLOBAL             61 (list + NULL)
                LOAD_FAST                9 (nd)
                LOAD_ATTR               59 (get + NULL|self)
                LOAD_CONST              11 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L16)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
       L16:     CALL                     1
                BINARY_OP                0 (+)

 161            BUILD_MAP                4
                STORE_FAST               7 (env)

 168            LOAD_FAST                2 (args)
                LOAD_ATTR               48 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       37 (to L17)
                NOT_TAKEN

 169            LOAD_GLOBAL             27 (print + NULL)
                LOAD_GLOBAL             48 (json)
                LOAD_ATTR               50 (dumps)
                PUSH_NULL
                LOAD_FAST                7 (env)
                LOAD_SMALL_INT           2
                LOAD_CONST              15 (True)
                LOAD_CONST              16 (('indent', 'sort_keys'))
                CALL_KW                  3
                CALL                     1
                POP_TOP

 175            LOAD_SMALL_INT           0
                RETURN_VALUE

 171   L17:     LOAD_GLOBAL             53 (_print_summary + NULL)
                LOAD_FAST                7 (env)
                CALL                     1
                POP_TOP

 175            LOAD_SMALL_INT           0
                RETURN_VALUE

  --   L18:     PUSH_EXC_INFO

 107            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L27)
                NOT_TAKEN
                STORE_FAST               3 (e)

 108   L19:     LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                LOAD_CONST              28 ((0, None))
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE        3 (to L20)
                NOT_TAKEN
                LOAD_SMALL_INT           2
                JUMP_FORWARD            30 (to L24)
       L20:     LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L23)
       L21:     NOT_TAKEN
       L22:     POP_TOP
                LOAD_SMALL_INT           0
       L23:     CALL                     1
       L24:     SWAP                     2
       L25:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RETURN_VALUE

  --   L26:     LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 107   L27:     RERAISE                  0

  --   L28:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L29:     PUSH_EXC_INFO

 121            LOAD_GLOBAL             38 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      154 (to L34)
                NOT_TAKEN
                STORE_FAST               3 (e)

 122   L30:     LOAD_GLOBAL             40 (logger)
                LOAD_ATTR               43 (warning + NULL|self)

 123            LOAD_CONST               6 ('security_dependency_audit import error type=')
                LOAD_GLOBAL             45 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR               46 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 122            CALL                     1
                POP_TOP

 126            LOAD_CONST               7 ('status')
                LOAD_CONST               8 ('failed')

 127            LOAD_CONST               9 ('python')
                LOAD_CONST               1 (None)

 128            LOAD_CONST              10 ('node')
                LOAD_CONST               1 (None)

 129            LOAD_CONST              11 ('warnings')
                LOAD_CONST              12 ('import_failed:')
                LOAD_GLOBAL             45 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR               46 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 130            LOAD_CONST              13 ('error_code')
                LOAD_CONST              14 ('import_failed')

 125            BUILD_MAP                5
                STORE_FAST               7 (env)

 132            LOAD_FAST                2 (args)
                LOAD_ATTR               48 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       36 (to L31)
                NOT_TAKEN

 133            LOAD_GLOBAL             27 (print + NULL)
                LOAD_GLOBAL             48 (json)
                LOAD_ATTR               50 (dumps)
                PUSH_NULL
                LOAD_FAST                7 (env)
                LOAD_SMALL_INT           2
                LOAD_CONST              15 (True)
                LOAD_CONST              16 (('indent', 'sort_keys'))
                CALL_KW                  3
                CALL                     1
                POP_TOP
                JUMP_FORWARD            11 (to L32)

 135   L31:     LOAD_GLOBAL             53 (_print_summary + NULL)
                LOAD_FAST                7 (env)
                CALL                     1
                POP_TOP

 136   L32:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                LOAD_SMALL_INT           1
                RETURN_VALUE

  --   L33:     LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 121   L34:     RERAISE                  0

  --   L35:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L18 [0]
  L5 to L6 -> L29 [0]
  L18 to L19 -> L28 [1] lasti
  L19 to L21 -> L26 [1] lasti
  L22 to L24 -> L26 [1] lasti
  L24 to L25 -> L28 [1] lasti
  L26 to L28 -> L28 [1] lasti
  L29 to L30 -> L35 [1] lasti
  L30 to L32 -> L33 [1] lasti
  L33 to L35 -> L35 [1] lasti
```
