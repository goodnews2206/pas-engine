# security/dependency_scanner

- **pyc:** `app\services\security\__pycache__\dependency_scanner.cpython-314.pyc`
- **expected source path (absent):** `app\services\security/dependency_scanner.py`
- **co_filename (from bytecode):** `app/services/security/dependency_scanner.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** security

## Module docstring

```
PAS-SECURITY-02 — Report-only dependency scanner.

Detects whether out-of-band vulnerability scanners are
available locally (``pip-audit``, ``npm audit``) and, when
they are, runs them in *report-only* mode. PAS-SECURITY-02
**NEVER** applies fixes, **NEVER** upgrades packages, and
**NEVER** writes to the lockfile.

Doctrine:

* **Report-only.** No auto-fix. No package upgrades. No
  `pip install`. No `npm install`. No `npm audit fix`. No
  lockfile modification.
* **No network requirement.** When the scanner binary is
  absent or fails, the helper returns
  ``status="scanner_unavailable"`` with a structural warning
  — not a synthetic pass.
* **No secret echo.** Scanner stdout/stderr is parsed for
  *bounded structural counts only*: dependency count,
  vulnerability count, scanner name, exit code. The
  freeform scanner report itself is NOT returned in the
  envelope.
* **NEVER raises.** All helpers return structural envelopes.
* **No fake passes.** ``status`` is one of:
    * ``"ok"``                — scanner ran and found 0 vulnerabilities.
    * ``"warning"``           — scanner ran and found ≥1.
    * ``"scanner_unavailable"`` — scanner binary not found / unrunnable.
    * ``"failed"``            — scanner ran but returned an error.

Public surface:

  * ``ALLOWED_SCANNERS``                                  — closed enum.
  * ``detect_python_lockfile(repo_root)``                 — bool.
  * ``detect_node_lockfile(repo_root)``                   — bool.
  * ``scan_python_dependencies(repo_root)``               — envelope.
  * ``scan_node_dependencies(repo_root)``                 — envelope.
  * ``scan_all(repo_root)``                               — combined envelope.
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `Path`, `Tuple`, `__future__`, `annotations`, `datetime`, `json`, `logging`, `os`, `pathlib`, `shutil`, `subprocess`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_classify_severity`, `_count_requirements_txt_lines`, `_cvss_to_tier`, `_has_package_json`, `_label_to_tier`, `_now_iso`, `_redacted_env`, `_safe_envelope`, `detect_node_lockfile`, `detect_python_lockfile`, `scan_all`, `scan_node_dependencies`, `scan_python_dependencies`

## Env-key candidates

`ALLOWED_SCANNERS`, `ALLOWED_SEVERITY_TIERS`, `CRITICAL`, `HIGH`, `LOW`, `MEDIUM`, `UNKNOWN`

## String constants (redacted where noted)

- '\nPAS-SECURITY-02 — Report-only dependency scanner.\n\nDetects whether out-of-band vulnerability scanners are\navailable locally (``pip-audit``, ``npm audit``) and, when\nthey are, runs them in *report-only* mode. PAS-SECURITY-02\n**NEVER** applies fixes, **NEVER** upgrades packages, and\n**NEVER** writes to the lockfile.\n\nDoctrine:\n\n* **Report-only.** No auto-fix. No package upgrades. No\n  `pip install`. No `npm install`. No `npm audit fix`. No\n  lockfile modification.\n* **No network requirement.** When the scanner binary is\n  absent or fails, the helper returns\n  ``status="scanner_unavailable"`` with a structural warning\n  — not a synthetic pass.\n* **No secret echo.** Scanner stdout/stderr is parsed for\n  *bounded structural counts only*: dependency count,\n  vulnerability count, scanner name, exit code. The\n  freeform scanner report itself is NOT returned in the\n  envelope.\n* **NEVER raises.** All helpers return structural envelopes.\n* **No fake passes.** ``status`` is one of:\n    * ``"ok"``                — scanner ran and found 0 vulnerabilities.\n    * ``"warning"``           — scanner ran and found ≥1.\n    * ``"scanner_unavailable"`` — scanner binary not found / unrunnable.\n    * ``"failed"``            — scanner ran but returned an error.\n\nPublic surface:\n\n  * ``ALLOWED_SCANNERS``                                  — closed enum.\n  * ``detect_python_lockfile(repo_root)``                 — bool.\n  * ``detect_node_lockfile(repo_root)``                   — bool.\n  * ``scan_python_dependencies(repo_root)``               — envelope.\n  * ``scan_node_dependencies(repo_root)``                 — envelope.\n  * ``scan_all(repo_root)``                               — combined envelope.\n'
- 'pas.security.dependency_scanner'
- 'Tuple[str, ...]'
- 'ALLOWED_SCANNERS'
- 'dependency_count'
- 'vulnerability_count'
- 'severities'
- 'warnings'
- 'error_code'
- 'raw_exit_code'
- 'ALLOWED_SEVERITY_TIERS'
- 'return'
- 'str'
- 'seconds'
- 'repo_root'
- 'Optional[str]'
- 'Returns the lockfile path (relative to repo_root) or None.'
- 'detect_python_lockfile error type='
- 'package-lock.json'
- 'detect_node_lockfile error type='
- 'bool'
- 'package.json'
- 'Dict[str, str]'
- 'Return a stripped subprocess env that retains only PATH\n+ locale variables. NEVER passes through ANTHROPIC_API_KEY,\nSUPABASE_*, TWILIO_*, etc.'
- 'scanner'
- 'status'
- 'lockfile'
- 'int'
- 'Optional[Dict[str, int]]'
- 'Optional[List[str]]'
- 'Optional[int]'
- 'Dict[str, Any]'
- 'LOW'
- 'MEDIUM'
- 'HIGH'
- 'CRITICAL'
- 'UNKNOWN'
- 'generated_at'
- 'severity_field'
- 'Any'
- 'Normalise a pip-audit / npm-audit severity field to the\nclosed enum. NEVER raises.\n\nAccepted shapes:\n  * string label ("low" / "moderate" / "high" / "critical")\n  * CVSS numeric score (float or string)\n  * list of strings — pick the highest tier\n  * list of dicts with ``severity`` / ``score`` keys\n  * None / missing — "UNKNOWN"\n'
- 'score'
- 'float'
- 'CVSS v3 standard mapping. NEVER raises.'
- 'label'
- 'path'
- 'Path'
- 'utf-8'
- 'replace'
- 'Run ``pip-audit --requirement <lockfile> --format json``\nif pip-audit is on PATH. Report-only. NEVER raises.'
- 'pip-audit'
- 'scanner_unavailable'
- 'python_lockfile_not_found'
- 'requirements.txt'
- 'pip_audit_not_on_path'
- 'scanner_not_on_path'
- '--strict'
- '--format=json'
- 'failed'
- 'scanner_timeout'
- 'scan_python_dependencies subprocess error type='
- 'scanner_subprocess:'
- 'scanner_subprocess_failed'
- 'vulnerabilities'
- 'dependencies'
- 'vulns'
- 'scan_python_dependencies parse error type='
- 'scanner_parse_failed:'
- 'scanner_parse_failed'
- 'warning'
- 'vulnerabilities:'
- 'scan_python_dependencies error type='
- 'unexpected:'
- 'vuln_item'
- 'None'
- 'severity'
- 'cvss_score'
- 'Run ``npm audit --json`` if package.json + npm are\navailable. Report-only. NEVER raises.'
- 'npm'
- 'package_json_not_found'
- 'npm_not_on_path'
- 'audit'
- '--json'
- 'scan_node_dependencies subprocess error type='
- 'metadata'
- 'total'
- 'low'
- 'moderate'
- 'high'
- 'critical'
- 'info'
- 'advisories'
- 'scan_node_dependencies parse error type='
- 'scan_node_dependencies error type='
- 'Run both scanners and return a combined envelope.\nNEVER raises.'
- 'python'
- 'node'

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS-SECURITY-02 — Report-only dependency scanner.\n\nDetects whether out-of-band vulnerability scanners are\navailable locally (``pip-audit``, ``npm audit``) and, when\nthey are, runs them in *report-only* mode. PAS-SECURITY-02\n**NEVER** applies fixes, **NEVER** upgrades packages, and\n**NEVER** writes to the lockfile.\n\nDoctrine:\n\n* **Report-only.** No auto-fix. No package upgrades. No\n  `pip install`. No `npm install`. No `npm audit fix`. No\n  lockfile modification.\n* **No network requirement.** When the scanner binary is\n  absent or fails, the helper returns\n  ``status="scanner_unavailable"`` with a structural warning\n  — not a synthetic pass.\n* **No secret echo.** Scanner stdout/stderr is parsed for\n  *bounded structural counts only*: dependency count,\n  vulnerability count, scanner name, exit code. The\n  freeform scanner report itself is NOT returned in the\n  envelope.\n* **NEVER raises.** All helpers return structural envelopes.\n* **No fake passes.** ``status`` is one of:\n    * ``"ok"``                — scanner ran and found 0 vulnerabilities.\n    * ``"warning"``           — scanner ran and found ≥1.\n    * ``"scanner_unavailable"`` — scanner binary not found / unrunnable.\n    * ``"failed"``            — scanner ran but returned an error.\n\nPublic surface:\n\n  * ``ALLOWED_SCANNERS``                                  — closed enum.\n  * ``detect_python_lockfile(repo_root)``                 — bool.\n  * ``detect_node_lockfile(repo_root)``                   — bool.\n  * ``scan_python_dependencies(repo_root)``               — envelope.\n  * ``scan_node_dependencies(repo_root)``                 — envelope.\n  * ``scan_all(repo_root)``                               — combined envelope.\n')
               STORE_NAME               1 (__doc__)

  41           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  43           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (json)
               STORE_NAME               4 (json)

  44           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (logging)
               STORE_NAME               5 (logging)

  45           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (os)
               STORE_NAME               6 (os)

  46           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              7 (shutil)
               STORE_NAME               7 (shutil)

  47           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              8 (subprocess)
               STORE_NAME               8 (subprocess)

  48           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              9 (datetime)
               IMPORT_FROM              9 (datetime)
               STORE_NAME               9 (datetime)
               IMPORT_FROM             10 (timezone)
               STORE_NAME              10 (timezone)
               POP_TOP

  49           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Path',))
               IMPORT_NAME             11 (pathlib)
               IMPORT_FROM             12 (Path)
               STORE_NAME              12 (Path)
               POP_TOP

  50           LOAD_SMALL_INT           0
               LOAD_CONST               5 (('Any', 'Dict', 'List', 'Optional', 'Tuple'))
               IMPORT_NAME             13 (typing)
               IMPORT_FROM             14 (Any)
               STORE_NAME              14 (Any)
               IMPORT_FROM             15 (Dict)
               STORE_NAME              15 (Dict)
               IMPORT_FROM             16 (List)
               STORE_NAME              16 (List)
               IMPORT_FROM             17 (Optional)
               STORE_NAME              17 (Optional)
               IMPORT_FROM             18 (Tuple)
               STORE_NAME              18 (Tuple)
               POP_TOP

  53           LOAD_NAME                5 (logging)
               LOAD_ATTR               38 (getLogger)
               PUSH_NULL
               LOAD_CONST               6 ('pas.security.dependency_scanner')
               CALL                     1
               STORE_NAME              20 (logger)

  57           LOAD_CONST              42 (('pip-audit', 'npm'))
               STORE_NAME              21 (ALLOWED_SCANNERS)
               LOAD_CONST               7 ('Tuple[str, ...]')
               LOAD_NAME               22 (__annotations__)
               LOAD_CONST               8 ('ALLOWED_SCANNERS')
               STORE_SUBSCR

  61           LOAD_SMALL_INT          60
               STORE_NAME              23 (_SCAN_TIMEOUT_SECONDS)

  64           LOAD_CONST               9 (<code object __annotate__ at 0x0000018C17FA31E0, file "app/services/security/dependency_scanner.py", line 64>)
               MAKE_FUNCTION
               LOAD_CONST              10 (<code object _now_iso at 0x0000018C18038A30, file "app/services/security/dependency_scanner.py", line 64>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              24 (_now_iso)

  72           LOAD_CONST              11 (<code object __annotate__ at 0x0000018C17FA3690, file "app/services/security/dependency_scanner.py", line 72>)
               MAKE_FUNCTION
               LOAD_CONST              12 (<code object detect_python_lockfile at 0x0000018C1794ED80, file "app/services/security/dependency_scanner.py", line 72>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              25 (detect_python_lockfile)

  87           LOAD_CONST              13 (<code object __annotate__ at 0x0000018C17FA3E10, file "app/services/security/dependency_scanner.py", line 87>)
               MAKE_FUNCTION
               LOAD_CONST              14 (<code object detect_node_lockfile at 0x0000018C1794E810, file "app/services/security/dependency_scanner.py", line 87>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              26 (detect_node_lockfile)

 103           LOAD_CONST              15 (<code object __annotate__ at 0x0000018C17FA2F10, file "app/services/security/dependency_scanner.py", line 103>)
               MAKE_FUNCTION
               LOAD_CONST              16 (<code object _has_package_json at 0x0000018C18038170, file "app/services/security/dependency_scanner.py", line 103>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              27 (_has_package_json)

 114           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C17FA3A50, file "app/services/security/dependency_scanner.py", line 114>)
               MAKE_FUNCTION
               LOAD_CONST              18 (<code object _redacted_env at 0x0000018C17FA92F0, file "app/services/security/dependency_scanner.py", line 114>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              28 (_redacted_env)

 135           LOAD_CONST              19 ('dependency_count')

 140           LOAD_SMALL_INT           0

 135           LOAD_CONST              20 ('vulnerability_count')

 141           LOAD_SMALL_INT           0

 135           LOAD_CONST              21 ('severities')

 142           LOAD_CONST               2 (None)

 135           LOAD_CONST              22 ('warnings')

 143           LOAD_CONST               2 (None)

 135           LOAD_CONST              23 ('error_code')

 144           LOAD_CONST               2 (None)

 135           LOAD_CONST              24 ('raw_exit_code')

 145           LOAD_CONST               2 (None)

 135           BUILD_MAP                6
               LOAD_CONST              25 (<code object __annotate__ at 0x0000018C1812C030, file "app/services/security/dependency_scanner.py", line 135>)
               MAKE_FUNCTION
               LOAD_CONST              26 (<code object _safe_envelope at 0x0000018C17D86490, file "app/services/security/dependency_scanner.py", line 135>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              29 (_safe_envelope)

 175           LOAD_CONST              43 (('LOW', 'MEDIUM', 'HIGH', 'CRITICAL', 'UNKNOWN'))
               STORE_NAME              30 (ALLOWED_SEVERITY_TIERS)
               LOAD_CONST               7 ('Tuple[str, ...]')
               LOAD_NAME               22 (__annotations__)
               LOAD_CONST              27 ('ALLOWED_SEVERITY_TIERS')
               STORE_SUBSCR

 180           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA3960, file "app/services/security/dependency_scanner.py", line 180>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object _classify_severity at 0x0000018C17F796F0, file "app/services/security/dependency_scanner.py", line 180>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              31 (_classify_severity)

 225           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA32D0, file "app/services/security/dependency_scanner.py", line 225>)
               MAKE_FUNCTION
               LOAD_CONST              31 (<code object _cvss_to_tier at 0x0000018C17FF10B0, file "app/services/security/dependency_scanner.py", line 225>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              32 (_cvss_to_tier)

 244           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA3C30, file "app/services/security/dependency_scanner.py", line 244>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object _label_to_tier at 0x0000018C17F96140, file "app/services/security/dependency_scanner.py", line 244>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              33 (_label_to_tier)

 259           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA3780, file "app/services/security/dependency_scanner.py", line 259>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object _count_requirements_txt_lines at 0x0000018C17FEE030, file "app/services/security/dependency_scanner.py", line 259>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              34 (_count_requirements_txt_lines)

 273           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C17FA2A60, file "app/services/security/dependency_scanner.py", line 273>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object scan_python_dependencies at 0x0000018C17EAB7F0, file "app/services/security/dependency_scanner.py", line 273>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              35 (scan_python_dependencies)

 439           LOAD_CONST              38 (<code object __annotate__ at 0x0000018C17FA3D20, file "app/services/security/dependency_scanner.py", line 439>)
               MAKE_FUNCTION
               LOAD_CONST              39 (<code object scan_node_dependencies at 0x0000018C182FFB50, file "app/services/security/dependency_scanner.py", line 439>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              36 (scan_node_dependencies)

 577           LOAD_CONST              40 (<code object __annotate__ at 0x0000018C17FA23D0, file "app/services/security/dependency_scanner.py", line 577>)
               MAKE_FUNCTION
               LOAD_CONST              41 (<code object scan_all at 0x0000018C17CC1CE0, file "app/services/security/dependency_scanner.py", line 577>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              37 (scan_all)

 596           BUILD_LIST               0
               LOAD_CONST              44 (('ALLOWED_SCANNERS', 'ALLOWED_SEVERITY_TIERS', 'detect_python_lockfile', 'detect_node_lockfile', 'scan_python_dependencies', 'scan_node_dependencies', 'scan_all'))
               LIST_EXTEND              1
               STORE_NAME              38 (__all__)
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "app/services/security/dependency_scanner.py", line 64>:
 64           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038A30, file "app/services/security/dependency_scanner.py", line 64>:
 64           RESUME                   0

 65           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "app/services/security/dependency_scanner.py", line 72>:
 72           RESUME                   0
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
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object detect_python_lockfile at 0x0000018C1794ED80, file "app/services/security/dependency_scanner.py", line 72>:
  72            RESUME                   0

  74            NOP

  75    L1:     LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                STORE_FAST               1 (root)

  76            LOAD_CONST               3 (('requirements.txt', 'Pipfile.lock', 'poetry.lock'))
                GET_ITER
        L2:     FOR_ITER                37 (to L6)
                STORE_FAST               2 (candidate)

  77            LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (root, candidate)
                BINARY_OP               11 (/)
                STORE_FAST               3 (p)

  78            LOAD_FAST_BORROW         3 (p)
                LOAD_ATTR                3 (is_file + NULL|self)
                CALL                     0
                TO_BOOL
        L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           35 (to L2)

  79    L4:     LOAD_FAST_BORROW         2 (candidate)
                SWAP                     2
                POP_TOP
        L5:     RETURN_VALUE

  76    L6:     END_FOR
                POP_ITER

  84    L7:     LOAD_CONST               2 (None)
                RETURN_VALUE

  --    L8:     PUSH_EXC_INFO

  80            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       55 (to L12)
                NOT_TAKEN
                STORE_FAST               4 (e)

  81    L9:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

  82            LOAD_CONST               1 ('detect_python_lockfile error type=')
                LOAD_GLOBAL             11 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               12 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

  81            CALL                     1
                POP_TOP
       L10:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)

  84            LOAD_CONST               2 (None)
                RETURN_VALUE

  --   L11:     LOAD_CONST               2 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RERAISE                  1

  80   L12:     RERAISE                  0

  --   L13:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L3 -> L8 [0]
  L4 to L5 -> L8 [0]
  L6 to L7 -> L8 [0]
  L8 to L9 -> L13 [1] lasti
  L9 to L10 -> L11 [1] lasti
  L11 to L13 -> L13 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "app/services/security/dependency_scanner.py", line 87>:
 87           RESUME                   0
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
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object detect_node_lockfile at 0x0000018C1794E810, file "app/services/security/dependency_scanner.py", line 87>:
  87            RESUME                   0

  88            NOP

  89    L1:     LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                STORE_FAST               1 (root)

  90            LOAD_CONST               3 (('package-lock.json', 'yarn.lock', 'pnpm-lock.yaml'))
                GET_ITER
        L2:     FOR_ITER                37 (to L6)
                STORE_FAST               2 (candidate)

  91            LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (root, candidate)
                BINARY_OP               11 (/)
                STORE_FAST               3 (p)

  92            LOAD_FAST_BORROW         3 (p)
                LOAD_ATTR                3 (is_file + NULL|self)
                CALL                     0
                TO_BOOL
        L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           35 (to L2)

  93    L4:     LOAD_FAST_BORROW         2 (candidate)
                SWAP                     2
                POP_TOP
        L5:     RETURN_VALUE

  90    L6:     END_FOR
                POP_ITER

 100    L7:     LOAD_CONST               2 (None)
                RETURN_VALUE

  --    L8:     PUSH_EXC_INFO

  96            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       55 (to L12)
                NOT_TAKEN
                STORE_FAST               4 (e)

  97    L9:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

  98            LOAD_CONST               1 ('detect_node_lockfile error type=')
                LOAD_GLOBAL             11 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               12 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

  97            CALL                     1
                POP_TOP
       L10:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)

 100            LOAD_CONST               2 (None)
                RETURN_VALUE

  --   L11:     LOAD_CONST               2 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RERAISE                  1

  96   L12:     RERAISE                  0

  --   L13:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L3 -> L8 [0]
  L4 to L5 -> L8 [0]
  L6 to L7 -> L8 [0]
  L8 to L9 -> L13 [1] lasti
  L9 to L10 -> L11 [1] lasti
  L11 to L13 -> L13 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "app/services/security/dependency_scanner.py", line 103>:
103           RESUME                   0
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
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _has_package_json at 0x0000018C18038170, file "app/services/security/dependency_scanner.py", line 103>:
 103           RESUME                   0

 104           NOP

 105   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('package.json')
               BINARY_OP               11 (/)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 106           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 107   L4:     POP_EXCEPT
               LOAD_CONST               1 (False)
               RETURN_VALUE

 106   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "app/services/security/dependency_scanner.py", line 114>:
114           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('Dict[str, str]')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _redacted_env at 0x0000018C17FA92F0, file "app/services/security/dependency_scanner.py", line 114>:
 114            RESUME                   0

 118            LOAD_CONST               1 (('PATH', 'LANG', 'LC_ALL', 'LC_CTYPE', 'HOME', 'USERPROFILE', 'TMP', 'TEMP'))
                STORE_FAST               0 (keep)

 119            BUILD_MAP                0
                STORE_FAST               1 (safe)

 120            NOP

 121    L1:     LOAD_GLOBAL              0 (os)
                LOAD_ATTR                2 (environ)
                STORE_FAST               2 (env)

 122            LOAD_FAST_BORROW         0 (keep)
                GET_ITER
        L2:     FOR_ITER                48 (to L5)
                STORE_FAST               3 (k)

 123            LOAD_FAST_BORROW         2 (env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_FAST_BORROW         3 (k)
                CALL                     1
                STORE_FAST               4 (v)

 124            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW         4 (v)
                LOAD_GLOBAL              8 (str)
                CALL                     2
                TO_BOOL
        L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           44 (to L2)

 125    L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 65 (v, safe)
                LOAD_FAST_BORROW         3 (k)
                STORE_SUBSCR
                JUMP_BACKWARD           50 (to L2)

 122    L5:     END_FOR
                POP_ITER

 128    L6:     LOAD_FAST_BORROW         1 (safe)
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

 126            LOAD_GLOBAL             10 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L9)
                NOT_TAKEN
                POP_TOP

 127    L8:     POP_EXCEPT

 128            LOAD_FAST                1 (safe)
                RETURN_VALUE

 126    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L3 -> L7 [0]
  L4 to L6 -> L7 [0]
  L7 to L8 -> L10 [1] lasti
  L9 to L10 -> L10 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C1812C030, file "app/services/security/dependency_scanner.py", line 135>:
135           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('scanner')

137           LOAD_CONST               2 ('Optional[str]')

135           LOAD_CONST               3 ('status')

138           LOAD_CONST               4 ('str')

135           LOAD_CONST               5 ('lockfile')

139           LOAD_CONST               2 ('Optional[str]')

135           LOAD_CONST               6 ('dependency_count')

140           LOAD_CONST               7 ('int')

135           LOAD_CONST               8 ('vulnerability_count')

141           LOAD_CONST               7 ('int')

135           LOAD_CONST               9 ('severities')

142           LOAD_CONST              10 ('Optional[Dict[str, int]]')

135           LOAD_CONST              11 ('warnings')

143           LOAD_CONST              12 ('Optional[List[str]]')

135           LOAD_CONST              13 ('error_code')

144           LOAD_CONST               2 ('Optional[str]')

135           LOAD_CONST              14 ('raw_exit_code')

145           LOAD_CONST              15 ('Optional[int]')

135           LOAD_CONST              16 ('return')

146           LOAD_CONST              17 ('Dict[str, Any]')

135           BUILD_MAP               10
              RETURN_VALUE

Disassembly of <code object _safe_envelope at 0x0000018C17D86490, file "app/services/security/dependency_scanner.py", line 135>:
 135            RESUME                   0

 150            LOAD_CONST               0 ('LOW')
                LOAD_SMALL_INT           0
                LOAD_CONST               1 ('MEDIUM')
                LOAD_SMALL_INT           0
                LOAD_CONST               2 ('HIGH')
                LOAD_SMALL_INT           0
                LOAD_CONST               3 ('CRITICAL')
                LOAD_SMALL_INT           0
                LOAD_CONST               4 ('UNKNOWN')
                LOAD_SMALL_INT           0
                BUILD_MAP                5
                STORE_FAST               9 (counts)

 151            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         5 (severities)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       60 (to L6)
                NOT_TAKEN

 152            LOAD_FAST_BORROW         9 (counts)
                GET_ITER
        L1:     FOR_ITER                53 (to L5)
                STORE_FAST              10 (k)

 153            NOP

 154    L2:     LOAD_GLOBAL              5 (max + NULL)
                LOAD_SMALL_INT           0
                LOAD_GLOBAL              7 (int + NULL)
                LOAD_FAST_BORROW         5 (severities)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_FAST_BORROW        10 (k)
                LOAD_SMALL_INT           0
                CALL                     2
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L3)
                NOT_TAKEN
                POP_TOP
                LOAD_SMALL_INT           0
        L3:     CALL                     1
                CALL                     2
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 154 (counts, k)
                STORE_SUBSCR
        L4:     JUMP_BACKWARD           55 (to L1)

 152    L5:     END_FOR
                POP_ITER

 158    L6:     LOAD_CONST               5 ('scanner')
                LOAD_FAST                0 (scanner)

 159            LOAD_CONST               6 ('status')
                LOAD_FAST                1 (status)

 160            LOAD_CONST               7 ('lockfile')
                LOAD_FAST                2 (lockfile)

 161            LOAD_CONST               8 ('dependency_count')
                LOAD_GLOBAL              7 (int + NULL)
                LOAD_FAST_BORROW         3 (dependency_count)
                CALL                     1

 162            LOAD_CONST               9 ('vulnerability_count')
                LOAD_GLOBAL              7 (int + NULL)
                LOAD_FAST_BORROW         4 (vulnerability_count)
                CALL                     1

 163            LOAD_CONST              10 ('severities')
                LOAD_FAST                9 (counts)

 164            LOAD_CONST              11 ('warnings')
                LOAD_GLOBAL             15 (list + NULL)
                LOAD_FAST                6 (warnings)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
        L7:     CALL                     1

 165            LOAD_CONST              12 ('error_code')
                LOAD_FAST_BORROW         7 (error_code)

 166            LOAD_CONST              13 ('raw_exit_code')
                LOAD_FAST_BORROW         8 (raw_exit_code)

 167            LOAD_CONST              14 ('generated_at')
                LOAD_GLOBAL             17 (_now_iso + NULL)
                CALL                     0

 157            BUILD_MAP               10
                RETURN_VALUE

  --    L8:     PUSH_EXC_INFO

 155            LOAD_GLOBAL             10 (TypeError)
                LOAD_GLOBAL             12 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        9 (to L10)
                NOT_TAKEN
                POP_TOP

 156            LOAD_SMALL_INT           0
                LOAD_FAST_LOAD_FAST    154 (counts, k)
                STORE_SUBSCR
        L9:     POP_EXCEPT
                JUMP_BACKWARD          148 (to L1)

 155   L10:     RERAISE                  0

  --   L11:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L4 -> L8 [1]
  L8 to L9 -> L11 [2] lasti
  L10 to L11 -> L11 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "app/services/security/dependency_scanner.py", line 180>:
180           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('severity_field')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _classify_severity at 0x0000018C17F796F0, file "app/services/security/dependency_scanner.py", line 180>:
 180            RESUME                   0

 191            NOP

 192    L1:     LOAD_FAST_BORROW         0 (severity_field)
                POP_JUMP_IF_NOT_NONE     3 (to L3)
                NOT_TAKEN

 193    L2:     LOAD_CONST               1 ('UNKNOWN')
                RETURN_VALUE

 194    L3:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (severity_field)
                LOAD_GLOBAL              2 (int)
                LOAD_GLOBAL              4 (float)
                BUILD_TUPLE              2
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       21 (to L5)
                NOT_TAKEN

 195            LOAD_GLOBAL              7 (_cvss_to_tier + NULL)
                LOAD_GLOBAL              5 (float + NULL)
                LOAD_FAST_BORROW         0 (severity_field)
                CALL                     1
                CALL                     1
        L4:     RETURN_VALUE

 196    L5:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (severity_field)
                LOAD_GLOBAL              8 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       12 (to L7)
                NOT_TAKEN

 197            LOAD_GLOBAL             11 (_label_to_tier + NULL)
                LOAD_FAST_BORROW         0 (severity_field)
                CALL                     1
        L6:     RETURN_VALUE

 198    L7:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (severity_field)
                LOAD_GLOBAL             12 (list)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       80 (to L13)
                NOT_TAKEN

 199            LOAD_CONST               1 ('UNKNOWN')
                STORE_FAST               1 (best)

 200            LOAD_CONST               2 ('LOW')
                LOAD_SMALL_INT           1
                LOAD_CONST               3 ('MEDIUM')
                LOAD_SMALL_INT           2
                LOAD_CONST               4 ('HIGH')
                LOAD_SMALL_INT           3
                LOAD_CONST               5 ('CRITICAL')
                LOAD_SMALL_INT           4
                LOAD_CONST               1 ('UNKNOWN')
                LOAD_SMALL_INT           0
                BUILD_MAP                5
                STORE_FAST               2 (rank)

 201            LOAD_FAST_BORROW         0 (severity_field)
                GET_ITER
        L8:     FOR_ITER                57 (to L11)
                STORE_FAST               3 (item)

 202            LOAD_GLOBAL             15 (_classify_severity + NULL)
                LOAD_FAST_BORROW         3 (item)
                CALL                     1
                STORE_FAST               4 (t)

 203            LOAD_FAST_BORROW         2 (rank)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_FAST_BORROW         4 (t)
                LOAD_SMALL_INT           0
                CALL                     2
                LOAD_FAST_BORROW         2 (rank)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_FAST_BORROW         1 (best)
                LOAD_SMALL_INT           0
                CALL                     2
                COMPARE_OP             148 (bool(>))
        L9:     POP_JUMP_IF_TRUE         3 (to L10)
                NOT_TAKEN
                JUMP_BACKWARD           55 (to L8)

 204   L10:     LOAD_FAST                4 (t)
                STORE_FAST               1 (best)
                JUMP_BACKWARD           59 (to L8)

 201   L11:     END_FOR
                POP_ITER

 205            LOAD_FAST_BORROW         1 (best)
       L12:     RETURN_VALUE

 206   L13:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (severity_field)
                LOAD_GLOBAL             18 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       99 (to L27)
                NOT_TAKEN

 208            LOAD_CONST               6 (('severity', 'level', 'label'))
                GET_ITER
       L14:     FOR_ITER                37 (to L18)
                STORE_FAST               5 (key)

 209            LOAD_FAST_BORROW         0 (severity_field)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_FAST_BORROW         5 (key)
                CALL                     1
                STORE_FAST               6 (v)

 210            LOAD_FAST_BORROW         6 (v)
       L15:     POP_JUMP_IF_NOT_NONE     3 (to L16)
                NOT_TAKEN
                JUMP_BACKWARD           26 (to L14)

 211   L16:     LOAD_GLOBAL             15 (_classify_severity + NULL)
                LOAD_FAST_BORROW         6 (v)
                CALL                     1
                SWAP                     2
                POP_TOP
       L17:     RETURN_VALUE

 208   L18:     END_FOR
                POP_ITER

 212            LOAD_CONST               7 (('score', 'cvss_score', 'cvss'))
                GET_ITER
       L19:     FOR_ITER                47 (to L25)
                STORE_FAST               5 (key)

 213            LOAD_FAST_BORROW         0 (severity_field)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_FAST_BORROW         5 (key)
                CALL                     1
                STORE_FAST               6 (v)

 214            LOAD_FAST_BORROW         6 (v)
       L20:     POP_JUMP_IF_NOT_NONE     3 (to L21)
                NOT_TAKEN
                JUMP_BACKWARD           26 (to L19)

 215   L21:     NOP

 216   L22:     LOAD_GLOBAL              7 (_cvss_to_tier + NULL)
                LOAD_GLOBAL              5 (float + NULL)
                LOAD_FAST_BORROW         6 (v)
                CALL                     1
                CALL                     1
       L23:     SWAP                     2
                POP_TOP
       L24:     RETURN_VALUE

 212   L25:     END_FOR
                POP_ITER

 219   L26:     LOAD_CONST               1 ('UNKNOWN')
                RETURN_VALUE

 206   L27:     NOP

 222            LOAD_CONST               1 ('UNKNOWN')
                RETURN_VALUE

  --   L28:     PUSH_EXC_INFO

 217            LOAD_GLOBAL             20 (TypeError)
                LOAD_GLOBAL             22 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L30)
                NOT_TAKEN
                POP_TOP

 218   L29:     POP_EXCEPT
                JUMP_BACKWARD           76 (to L19)

 217   L30:     RERAISE                  0

  --   L31:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L32:     PUSH_EXC_INFO

 220            LOAD_GLOBAL             24 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L34)
                NOT_TAKEN
                POP_TOP

 221   L33:     POP_EXCEPT
                LOAD_CONST               1 ('UNKNOWN')
                RETURN_VALUE

 220   L34:     RERAISE                  0

  --   L35:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L32 [0]
  L3 to L4 -> L32 [0]
  L5 to L6 -> L32 [0]
  L7 to L9 -> L32 [0]
  L10 to L12 -> L32 [0]
  L13 to L15 -> L32 [0]
  L16 to L17 -> L32 [0]
  L18 to L20 -> L32 [0]
  L22 to L23 -> L28 [1]
  L23 to L24 -> L32 [0]
  L25 to L26 -> L32 [0]
  L28 to L29 -> L31 [2] lasti
  L29 to L30 -> L32 [0]
  L30 to L31 -> L31 [2] lasti
  L31 to L32 -> L32 [0]
  L32 to L33 -> L35 [1] lasti
  L34 to L35 -> L35 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA32D0, file "app/services/security/dependency_scanner.py", line 225>:
225           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('score')
              LOAD_CONST               2 ('float')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _cvss_to_tier at 0x0000018C17FF10B0, file "app/services/security/dependency_scanner.py", line 225>:
 225            RESUME                   0

 227            NOP

 228    L1:     LOAD_GLOBAL              1 (float + NULL)
                LOAD_FAST_BORROW         0 (score)
                CALL                     1
                STORE_FAST               1 (s)

 231    L2:     LOAD_FAST_LOAD_FAST     17 (s, s)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE        3 (to L3)
                NOT_TAKEN

 232            LOAD_CONST               1 ('UNKNOWN')
                RETURN_VALUE

 233    L3:     LOAD_FAST                1 (s)
                LOAD_CONST               2 (0.0)
                COMPARE_OP              58 (bool(<=))
                POP_JUMP_IF_FALSE        3 (to L4)
                NOT_TAKEN

 234            LOAD_CONST               1 ('UNKNOWN')
                RETURN_VALUE

 235    L4:     LOAD_FAST                1 (s)
                LOAD_CONST               3 (4.0)
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN

 236            LOAD_CONST               4 ('LOW')
                RETURN_VALUE

 237    L5:     LOAD_FAST                1 (s)
                LOAD_CONST               5 (7.0)
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN

 238            LOAD_CONST               6 ('MEDIUM')
                RETURN_VALUE

 239    L6:     LOAD_FAST                1 (s)
                LOAD_CONST               7 (9.0)
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        3 (to L7)
                NOT_TAKEN

 240            LOAD_CONST               8 ('HIGH')
                RETURN_VALUE

 241    L7:     LOAD_CONST               9 ('CRITICAL')
                RETURN_VALUE

  --    L8:     PUSH_EXC_INFO

 229            LOAD_GLOBAL              2 (TypeError)
                LOAD_GLOBAL              4 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L10)
                NOT_TAKEN
                POP_TOP

 230    L9:     POP_EXCEPT
                LOAD_CONST               1 ('UNKNOWN')
                RETURN_VALUE

 229   L10:     RERAISE                  0

  --   L11:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L8 [0]
  L8 to L9 -> L11 [1] lasti
  L10 to L11 -> L11 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "app/services/security/dependency_scanner.py", line 244>:
244           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('label')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               2 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _label_to_tier at 0x0000018C17F96140, file "app/services/security/dependency_scanner.py", line 244>:
244           RESUME                   0

245           LOAD_FAST_BORROW         0 (label)
              LOAD_ATTR                1 (strip + NULL|self)
              CALL                     0
              LOAD_ATTR                3 (lower + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

246           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

247           LOAD_CONST               0 ('UNKNOWN')
              RETURN_VALUE

248   L1:     LOAD_FAST_BORROW         1 (s)
              LOAD_CONST               5 (('low', 'negligible', 'informational', 'info'))
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

249           LOAD_CONST               1 ('LOW')
              RETURN_VALUE

250   L2:     LOAD_FAST_BORROW         1 (s)
              LOAD_CONST               6 (('moderate', 'medium', 'med'))
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

251           LOAD_CONST               2 ('MEDIUM')
              RETURN_VALUE

252   L3:     LOAD_FAST_BORROW         1 (s)
              LOAD_CONST               7 (('high', 'important'))
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN

253           LOAD_CONST               3 ('HIGH')
              RETURN_VALUE

254   L4:     LOAD_FAST_BORROW         1 (s)
              LOAD_CONST               8 (('critical', 'severe'))
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN

255           LOAD_CONST               4 ('CRITICAL')
              RETURN_VALUE

256   L5:     LOAD_CONST               0 ('UNKNOWN')
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "app/services/security/dependency_scanner.py", line 259>:
259           RESUME                   0
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
              LOAD_CONST               4 ('int')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _count_requirements_txt_lines at 0x0000018C17FEE030, file "app/services/security/dependency_scanner.py", line 259>:
 259            RESUME                   0

 260            NOP

 261    L1:     LOAD_FAST_BORROW         0 (path)
                LOAD_ATTR                1 (read_text + NULL|self)
                LOAD_CONST               0 ('utf-8')
                LOAD_CONST               1 ('replace')
                LOAD_CONST               2 (('encoding', 'errors'))
                CALL_KW                  2
                STORE_FAST               1 (src)

 264    L2:     LOAD_SMALL_INT           0
                STORE_FAST               2 (count)

 265            LOAD_FAST                1 (src)
                LOAD_ATTR                5 (splitlines + NULL|self)
                CALL                     0
                GET_ITER
        L3:     FOR_ITER                84 (to L6)
                STORE_FAST               3 (raw_line)

 266            LOAD_FAST                3 (raw_line)
                LOAD_ATTR                7 (strip + NULL|self)
                CALL                     0
                STORE_FAST               4 (line)

 267            LOAD_FAST                4 (line)
                TO_BOOL
                POP_JUMP_IF_FALSE       47 (to L4)
                NOT_TAKEN
                LOAD_FAST                4 (line)
                LOAD_ATTR                9 (startswith + NULL|self)
                LOAD_CONST               3 ('#')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        24 (to L4)
                NOT_TAKEN
                LOAD_FAST                4 (line)
                LOAD_ATTR                9 (startswith + NULL|self)
                LOAD_CONST               4 ('--')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN

 268    L4:     JUMP_BACKWARD           75 (to L3)

 269    L5:     LOAD_FAST                2 (count)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST               2 (count)
                JUMP_BACKWARD           86 (to L3)

 265    L6:     END_FOR
                POP_ITER

 270            LOAD_FAST                2 (count)
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

 262            LOAD_GLOBAL              2 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L9)
                NOT_TAKEN
                POP_TOP

 263    L8:     POP_EXCEPT
                LOAD_SMALL_INT           0
                RETURN_VALUE

 262    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L7 [0]
  L7 to L8 -> L10 [1] lasti
  L9 to L10 -> L10 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "app/services/security/dependency_scanner.py", line 273>:
273           RESUME                   0
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
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object scan_python_dependencies at 0x0000018C17EAB7F0, file "app/services/security/dependency_scanner.py", line 273>:
  --            MAKE_CELL               13 (sev_counts)

 273            RESUME                   0

 276            NOP

 277    L1:     LOAD_GLOBAL              1 (detect_python_lockfile + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                STORE_FAST               1 (lockfile)

 278            LOAD_FAST_BORROW         1 (lockfile)
                POP_JUMP_IF_NOT_NONE    18 (to L3)
                NOT_TAKEN

 279            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 280            LOAD_CONST               2 ('pip-audit')

 281            LOAD_CONST               3 ('scanner_unavailable')

 282            LOAD_CONST               1 (None)

 283            LOAD_CONST               4 ('python_lockfile_not_found')
                BUILD_LIST               1

 284            LOAD_CONST               4 ('python_lockfile_not_found')

 279            LOAD_CONST               5 (('scanner', 'status', 'lockfile', 'warnings', 'error_code'))
                CALL_KW                  5
        L2:     RETURN_VALUE

 286    L3:     LOAD_SMALL_INT           0
                STORE_FAST               2 (dep_count)

 287    L4:     NOP

 288    L5:     LOAD_FAST_BORROW         1 (lockfile)
                LOAD_CONST               6 ('requirements.txt')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       28 (to L6)
                NOT_TAKEN
                LOAD_GLOBAL              5 (_count_requirements_txt_lines + NULL)
                LOAD_GLOBAL              7 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_FAST_BORROW         1 (lockfile)
                BINARY_OP               11 (/)
                CALL                     1
                JUMP_FORWARD             1 (to L7)
        L6:     LOAD_SMALL_INT           0
        L7:     STORE_FAST               2 (dep_count)

 292    L8:     LOAD_GLOBAL             10 (shutil)
                LOAD_ATTR               12 (which)
                PUSH_NULL
                LOAD_CONST               2 ('pip-audit')
                CALL                     1
                STORE_FAST               3 (binary)

 293            LOAD_FAST_BORROW         3 (binary)
                POP_JUMP_IF_NOT_NONE    19 (to L10)
                NOT_TAKEN

 294            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 295            LOAD_CONST               2 ('pip-audit')

 296            LOAD_CONST               3 ('scanner_unavailable')

 297            LOAD_FAST_BORROW         1 (lockfile)

 298            LOAD_FAST_BORROW         2 (dep_count)

 299            LOAD_CONST               7 ('pip_audit_not_on_path')
                BUILD_LIST               1

 300            LOAD_CONST               8 ('scanner_not_on_path')

 294            LOAD_CONST               9 (('scanner', 'status', 'lockfile', 'dependency_count', 'warnings', 'error_code'))
                CALL_KW                  6
        L9:     RETURN_VALUE

 302   L10:     NOP

 303   L11:     LOAD_FAST_BORROW         3 (binary)
                LOAD_CONST              10 ('--strict')
                LOAD_CONST              11 ('--format=json')
                BUILD_LIST               3
                STORE_FAST               4 (cmd)

 304            LOAD_FAST_BORROW         1 (lockfile)
                LOAD_CONST               6 ('requirements.txt')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       37 (to L12)
                NOT_TAKEN

 305            LOAD_FAST_BORROW         4 (cmd)
                LOAD_CONST              12 ('-r')
                LOAD_GLOBAL             15 (str + NULL)
                LOAD_GLOBAL              7 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               6 ('requirements.txt')
                BINARY_OP               11 (/)
                CALL                     1
                BUILD_LIST               2
                BINARY_OP               13 (+=)
                STORE_FAST               4 (cmd)

 306   L12:     LOAD_GLOBAL             16 (subprocess)
                LOAD_ATTR               18 (run)
                PUSH_NULL

 307            LOAD_FAST_BORROW         4 (cmd)

 308            LOAD_CONST              13 (True)

 309            LOAD_CONST              13 (True)

 310            LOAD_GLOBAL             20 (_SCAN_TIMEOUT_SECONDS)

 311            LOAD_GLOBAL             15 (str + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1

 312            LOAD_GLOBAL             23 (_redacted_env + NULL)
                CALL                     0

 313            LOAD_CONST              14 (False)

 306            LOAD_CONST              15 (('capture_output', 'text', 'timeout', 'cwd', 'env', 'check'))
                CALL_KW                  7
                STORE_FAST               5 (proc)

 338   L13:     LOAD_SMALL_INT           0
                STORE_FAST               7 (vuln_count)

 340            LOAD_CONST              21 ('LOW')
                LOAD_SMALL_INT           0
                LOAD_CONST              22 ('MEDIUM')
                LOAD_SMALL_INT           0
                LOAD_CONST              23 ('HIGH')
                LOAD_SMALL_INT           0
                LOAD_CONST              24 ('CRITICAL')
                LOAD_SMALL_INT           0
                LOAD_CONST              25 ('UNKNOWN')
                LOAD_SMALL_INT           0

 339            BUILD_MAP                5
                STORE_DEREF             13 (sev_counts)

 343   L14:     NOP

 344   L15:     LOAD_GLOBAL             34 (json)
                LOAD_ATTR               36 (loads)
                PUSH_NULL
                LOAD_FAST                5 (proc)
                LOAD_ATTR               38 (stdout)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L18)
       L16:     NOT_TAKEN
       L17:     POP_TOP
                LOAD_CONST              26 ('{}')
       L18:     CALL                     1
                STORE_FAST               8 (data)

 348            LOAD_CONST              27 (<code object __annotate__ at 0x0000018C17FA2970, file "app/services/security/dependency_scanner.py", line 348>)
                MAKE_FUNCTION
                LOAD_FAST               13 (sev_counts)
                BUILD_TUPLE              1
                LOAD_CONST              28 (<code object _bump at 0x0000018C17E7E6C0, file "app/services/security/dependency_scanner.py", line 348>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_FAST               9 (_bump)

 361            LOAD_GLOBAL             41 (isinstance + NULL)
                LOAD_FAST                8 (data)
                LOAD_GLOBAL             42 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      218 (to L31)
                NOT_TAKEN

 362            LOAD_GLOBAL             41 (isinstance + NULL)
                LOAD_FAST                8 (data)
                LOAD_ATTR               45 (get + NULL|self)
                LOAD_CONST              29 ('vulnerabilities')
                CALL                     1
                LOAD_GLOBAL             46 (list)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       36 (to L22)
                NOT_TAKEN

 363            LOAD_FAST                8 (data)
                LOAD_CONST              29 ('vulnerabilities')
                BINARY_OP               26 ([])
                GET_ITER
       L19:     FOR_ITER                20 (to L20)
                STORE_FAST              10 (v)

 364            LOAD_FAST                7 (vuln_count)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST               7 (vuln_count)

 365            LOAD_FAST                9 (_bump)
                PUSH_NULL
                LOAD_FAST               10 (v)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           22 (to L19)

 363   L20:     END_FOR
                POP_ITER
       L21:     EXTENDED_ARG             1
                JUMP_FORWARD           267 (to L40)

 366   L22:     LOAD_GLOBAL             41 (isinstance + NULL)
                LOAD_FAST                8 (data)
                LOAD_ATTR               45 (get + NULL|self)
                LOAD_CONST              30 ('dependencies')
                CALL                     1
                LOAD_GLOBAL             46 (list)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      108 (to L30)
                NOT_TAKEN

 367            LOAD_FAST                8 (data)
                LOAD_CONST              30 ('dependencies')
                BINARY_OP               26 ([])
                GET_ITER
       L23:     FOR_ITER                94 (to L29)
                STORE_FAST              11 (d)

 368            LOAD_GLOBAL             41 (isinstance + NULL)
                LOAD_FAST               11 (d)
                LOAD_GLOBAL             42 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L24)
                NOT_TAKEN

 369            JUMP_BACKWARD           27 (to L23)

 370   L24:     LOAD_FAST               11 (d)
                LOAD_ATTR               45 (get + NULL|self)
                LOAD_CONST              31 ('vulns')
                CALL                     1
                STORE_FAST              12 (vulns)

 371            LOAD_GLOBAL             41 (isinstance + NULL)
                LOAD_FAST               12 (vulns)
                LOAD_GLOBAL             46 (list)
                CALL                     2
                TO_BOOL
       L25:     POP_JUMP_IF_TRUE         3 (to L26)
                NOT_TAKEN
                JUMP_BACKWARD           68 (to L23)

 372   L26:     LOAD_FAST               12 (vulns)
                GET_ITER
       L27:     FOR_ITER                20 (to L28)
                STORE_FAST              10 (v)

 373            LOAD_FAST                7 (vuln_count)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST               7 (vuln_count)

 374            LOAD_FAST                9 (_bump)
                PUSH_NULL
                LOAD_FAST               10 (v)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           22 (to L27)

 372   L28:     END_FOR
                POP_ITER
                JUMP_BACKWARD           96 (to L23)

 367   L29:     END_FOR
                POP_ITER

  --   L30:     JUMP_FORWARD           122 (to L40)

 375   L31:     LOAD_GLOBAL             41 (isinstance + NULL)
                LOAD_FAST                8 (data)
                LOAD_GLOBAL             46 (list)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      101 (to L40)
                NOT_TAKEN

 378            LOAD_FAST                8 (data)
                GET_ITER
       L32:     FOR_ITER                94 (to L39)
                STORE_FAST              11 (d)

 379            LOAD_GLOBAL             41 (isinstance + NULL)
                LOAD_FAST               11 (d)
                LOAD_GLOBAL             42 (dict)
                CALL                     2
                TO_BOOL
       L33:     POP_JUMP_IF_TRUE         3 (to L34)
                NOT_TAKEN
                JUMP_BACKWARD           27 (to L32)

 380   L34:     LOAD_FAST               11 (d)
                LOAD_ATTR               45 (get + NULL|self)
                LOAD_CONST              31 ('vulns')
                CALL                     1
                STORE_FAST              12 (vulns)

 381            LOAD_GLOBAL             41 (isinstance + NULL)
                LOAD_FAST               12 (vulns)
                LOAD_GLOBAL             46 (list)
                CALL                     2
                TO_BOOL
       L35:     POP_JUMP_IF_TRUE         3 (to L36)
                NOT_TAKEN
                JUMP_BACKWARD           68 (to L32)

 382   L36:     LOAD_FAST               12 (vulns)
                GET_ITER
       L37:     FOR_ITER                20 (to L38)
                STORE_FAST              10 (v)

 383            LOAD_FAST                7 (vuln_count)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST               7 (vuln_count)

 384            LOAD_FAST                9 (_bump)
                PUSH_NULL
                LOAD_FAST               10 (v)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           22 (to L37)

 382   L38:     END_FOR
                POP_ITER
                JUMP_BACKWARD           96 (to L32)

 378   L39:     END_FOR
                POP_ITER

 402   L40:     LOAD_FAST                7 (vuln_count)
                LOAD_SMALL_INT           0
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE       34 (to L42)
                NOT_TAKEN

 403            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 404            LOAD_CONST               2 ('pip-audit')

 405            LOAD_CONST              36 ('warning')

 406            LOAD_FAST                1 (lockfile)

 407            LOAD_FAST                2 (dep_count)

 408            LOAD_FAST                7 (vuln_count)

 409            LOAD_DEREF              13 (sev_counts)

 410            LOAD_CONST              37 ('vulnerabilities:')
                LOAD_FAST                7 (vuln_count)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 411            LOAD_FAST                5 (proc)
                LOAD_ATTR               48 (returncode)

 403            LOAD_CONST              38 (('scanner', 'status', 'lockfile', 'dependency_count', 'vulnerability_count', 'severities', 'warnings', 'raw_exit_code'))
                CALL_KW                  8
       L41:     RETURN_VALUE

 413   L42:     LOAD_GLOBAL              3 (_safe_envelope + NULL)

 414            LOAD_CONST               2 ('pip-audit')

 415            LOAD_CONST              39 ('ok')

 416            LOAD_FAST                1 (lockfile)

 417            LOAD_FAST                2 (dep_count)

 418            LOAD_SMALL_INT           0

 419            LOAD_DEREF              13 (sev_counts)

 420            LOAD_FAST                5 (proc)
                LOAD_ATTR               48 (returncode)

 413            LOAD_CONST              40 (('scanner', 'status', 'lockfile', 'dependency_count', 'vulnerability_count', 'severities', 'raw_exit_code'))
                CALL_KW                  7
       L43:     RETURN_VALUE

  --   L44:     PUSH_EXC_INFO

 289            LOAD_GLOBAL              8 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        7 (to L46)
                NOT_TAKEN
                POP_TOP

 290            LOAD_SMALL_INT           0
                STORE_FAST               2 (dep_count)
       L45:     POP_EXCEPT
                EXTENDED_ARG             2
                JUMP_BACKWARD_NO_INTERRUPT 654 (to L8)

 289   L46:     RERAISE                  0

  --   L47:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L48:     PUSH_EXC_INFO

 315            LOAD_GLOBAL             16 (subprocess)
                LOAD_ATTR               24 (TimeoutExpired)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       22 (to L51)
                NOT_TAKEN
                POP_TOP

 316            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 317            LOAD_CONST               2 ('pip-audit')

 318            LOAD_CONST              16 ('failed')

 319            LOAD_FAST                1 (lockfile)

 320            LOAD_FAST                2 (dep_count)

 321            LOAD_CONST              17 ('scanner_timeout')
                BUILD_LIST               1

 322            LOAD_CONST              17 ('scanner_timeout')

 316            LOAD_CONST               9 (('scanner', 'status', 'lockfile', 'dependency_count', 'warnings', 'error_code'))
                CALL_KW                  6
                SWAP                     2
       L49:     POP_EXCEPT
       L50:     RETURN_VALUE

 324   L51:     LOAD_GLOBAL              8 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       94 (to L59)
       L52:     NOT_TAKEN
       L53:     STORE_FAST               6 (e)

 325   L54:     LOAD_GLOBAL             26 (logger)
                LOAD_ATTR               29 (warning + NULL|self)

 326            LOAD_CONST              18 ('scan_python_dependencies subprocess error type=')

 327            LOAD_GLOBAL             31 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               32 (__name__)
                FORMAT_SIMPLE

 326            BUILD_STRING             2

 325            CALL                     1
                POP_TOP

 329            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 330            LOAD_CONST               2 ('pip-audit')

 331            LOAD_CONST              16 ('failed')

 332            LOAD_FAST                1 (lockfile)

 333            LOAD_FAST                2 (dep_count)

 334            LOAD_CONST              19 ('scanner_subprocess:')
                LOAD_GLOBAL             31 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               32 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 335            LOAD_CONST              20 ('scanner_subprocess_failed')

 329            LOAD_CONST               9 (('scanner', 'status', 'lockfile', 'dependency_count', 'warnings', 'error_code'))
                CALL_KW                  6
       L55:     SWAP                     2
       L56:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
       L57:     RETURN_VALUE

  --   L58:     LOAD_CONST               1 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

 324   L59:     RERAISE                  0

  --   L60:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L61:     PUSH_EXC_INFO

 385            LOAD_GLOBAL              8 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      105 (to L67)
                NOT_TAKEN
                STORE_FAST               6 (e)

 386   L62:     LOAD_GLOBAL             26 (logger)
                LOAD_ATTR               29 (warning + NULL|self)

 387            LOAD_CONST              32 ('scan_python_dependencies parse error type=')

 388            LOAD_GLOBAL             31 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               32 (__name__)
                FORMAT_SIMPLE

 387            BUILD_STRING             2

 386            CALL                     1
                POP_TOP

 392            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 393            LOAD_CONST               2 ('pip-audit')

 394            LOAD_CONST              16 ('failed')

 395            LOAD_FAST                1 (lockfile)

 396            LOAD_FAST                2 (dep_count)

 397            LOAD_CONST              33 ('scanner_parse_failed:')
                LOAD_GLOBAL             31 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               32 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 398            LOAD_CONST              34 ('scanner_parse_failed')

 399            LOAD_FAST                5 (proc)
                LOAD_ATTR               48 (returncode)

 392            LOAD_CONST              35 (('scanner', 'status', 'lockfile', 'dependency_count', 'warnings', 'error_code', 'raw_exit_code'))
                CALL_KW                  7
       L63:     SWAP                     2
       L64:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
       L65:     RETURN_VALUE

  --   L66:     LOAD_CONST               1 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

 385   L67:     RERAISE                  0

  --   L68:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L69:     PUSH_EXC_INFO

 422            LOAD_GLOBAL              8 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      115 (to L74)
                NOT_TAKEN
                STORE_FAST               6 (e)

 423   L70:     LOAD_GLOBAL             26 (logger)
                LOAD_ATTR               29 (warning + NULL|self)

 424            LOAD_CONST              41 ('scan_python_dependencies error type=')
                LOAD_GLOBAL             31 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               32 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 423            CALL                     1
                POP_TOP

 426            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 427            LOAD_CONST               2 ('pip-audit')

 428            LOAD_CONST              16 ('failed')

 429            LOAD_CONST               1 (None)

 430            LOAD_CONST              42 ('unexpected:')
                LOAD_GLOBAL             31 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               32 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 431            LOAD_CONST              42 ('unexpected:')
                LOAD_GLOBAL             31 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               32 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 426            LOAD_CONST               5 (('scanner', 'status', 'lockfile', 'warnings', 'error_code'))
                CALL_KW                  5
       L71:     SWAP                     2
       L72:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RETURN_VALUE

  --   L73:     LOAD_CONST               1 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

 422   L74:     RERAISE                  0

  --   L75:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L69 [0]
  L3 to L4 -> L69 [0]
  L5 to L8 -> L44 [0]
  L8 to L9 -> L69 [0]
  L11 to L13 -> L48 [0]
  L13 to L14 -> L69 [0]
  L15 to L16 -> L61 [0]
  L17 to L21 -> L61 [0]
  L21 to L22 -> L69 [0]
  L22 to L25 -> L61 [0]
  L26 to L30 -> L61 [0]
  L30 to L31 -> L69 [0]
  L31 to L33 -> L61 [0]
  L34 to L35 -> L61 [0]
  L36 to L40 -> L61 [0]
  L40 to L41 -> L69 [0]
  L42 to L43 -> L69 [0]
  L44 to L45 -> L47 [1] lasti
  L45 to L46 -> L69 [0]
  L46 to L47 -> L47 [1] lasti
  L47 to L48 -> L69 [0]
  L48 to L49 -> L60 [1] lasti
  L49 to L50 -> L69 [0]
  L51 to L52 -> L60 [1] lasti
  L53 to L54 -> L60 [1] lasti
  L54 to L55 -> L58 [1] lasti
  L55 to L56 -> L60 [1] lasti
  L56 to L57 -> L69 [0]
  L58 to L60 -> L60 [1] lasti
  L60 to L61 -> L69 [0]
  L61 to L62 -> L68 [1] lasti
  L62 to L63 -> L66 [1] lasti
  L63 to L64 -> L68 [1] lasti
  L64 to L65 -> L69 [0]
  L66 to L68 -> L68 [1] lasti
  L68 to L69 -> L69 [0]
  L69 to L70 -> L75 [1] lasti
  L70 to L71 -> L73 [1] lasti
  L71 to L72 -> L75 [1] lasti
  L73 to L75 -> L75 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "app/services/security/dependency_scanner.py", line 348>:
348           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('vuln_item')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('None')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _bump at 0x0000018C17E7E6C0, file "app/services/security/dependency_scanner.py", line 348>:
  --           COPY_FREE_VARS           1

 348           RESUME                   0

 350           LOAD_CONST               0 ('UNKNOWN')
               STORE_FAST               1 (tier)

 351           LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (vuln_item)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE      102 (to L2)
               NOT_TAKEN

 352           LOAD_GLOBAL              5 (_classify_severity + NULL)

 353           LOAD_FAST_BORROW         0 (vuln_item)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_CONST               1 ('severity')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        68 (to L1)
               NOT_TAKEN
               POP_TOP

 354           LOAD_FAST_BORROW         0 (vuln_item)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_CONST               2 ('severities')
               CALL                     1

 353           COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        43 (to L1)
               NOT_TAKEN
               POP_TOP

 355           LOAD_FAST_BORROW         0 (vuln_item)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_CONST               3 ('cvss_score')
               CALL                     1

 353           COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L1)
               NOT_TAKEN
               POP_TOP

 356           LOAD_FAST_BORROW         0 (vuln_item)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_CONST               4 ('score')
               CALL                     1

 352   L1:     CALL                     1
               STORE_FAST               1 (tier)

 358   L2:     LOAD_FAST_BORROW         1 (tier)
               LOAD_DEREF               2 (sev_counts)
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 359           LOAD_CONST               0 ('UNKNOWN')
               STORE_FAST               1 (tier)

 360   L3:     LOAD_DEREF               2 (sev_counts)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_FAST_BORROW         1 (tier)
               LOAD_SMALL_INT           0
               CALL                     2
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               LOAD_DEREF               2 (sev_counts)
               LOAD_FAST_BORROW         1 (tier)
               STORE_SUBSCR
               LOAD_CONST               5 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3D20, file "app/services/security/dependency_scanner.py", line 439>:
439           RESUME                   0
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
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object scan_node_dependencies at 0x0000018C182FFB50, file "app/services/security/dependency_scanner.py", line 439>:
 439            RESUME                   0

 442            NOP

 443    L1:     LOAD_GLOBAL              1 (_has_package_json + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L3)
                NOT_TAKEN

 444            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 445            LOAD_CONST               1 ('npm')

 446            LOAD_CONST               2 ('scanner_unavailable')

 447            LOAD_CONST               3 (None)

 448            LOAD_CONST               4 ('package_json_not_found')
                BUILD_LIST               1

 449            LOAD_CONST               4 ('package_json_not_found')

 444            LOAD_CONST               5 (('scanner', 'status', 'lockfile', 'warnings', 'error_code'))
                CALL_KW                  5
        L2:     RETURN_VALUE

 451    L3:     LOAD_GLOBAL              5 (detect_node_lockfile + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                STORE_FAST               1 (lockfile)

 452            LOAD_GLOBAL              6 (shutil)
                LOAD_ATTR                8 (which)
                PUSH_NULL
                LOAD_CONST               1 ('npm')
                CALL                     1
                STORE_FAST               2 (binary)

 453            LOAD_FAST_BORROW         2 (binary)
                POP_JUMP_IF_NOT_NONE    18 (to L5)
                NOT_TAKEN

 454            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 455            LOAD_CONST               1 ('npm')

 456            LOAD_CONST               2 ('scanner_unavailable')

 457            LOAD_FAST_BORROW         1 (lockfile)

 458            LOAD_CONST               6 ('npm_not_on_path')
                BUILD_LIST               1

 459            LOAD_CONST               7 ('scanner_not_on_path')

 454            LOAD_CONST               5 (('scanner', 'status', 'lockfile', 'warnings', 'error_code'))
                CALL_KW                  5
        L4:     RETURN_VALUE

 461    L5:     NOP

 462    L6:     LOAD_GLOBAL             10 (subprocess)
                LOAD_ATTR               12 (run)
                PUSH_NULL

 463            LOAD_FAST_BORROW         2 (binary)
                LOAD_CONST               8 ('audit')
                LOAD_CONST               9 ('--json')
                BUILD_LIST               3

 464            LOAD_CONST              10 (True)

 465            LOAD_CONST              10 (True)

 466            LOAD_GLOBAL             14 (_SCAN_TIMEOUT_SECONDS)

 467            LOAD_GLOBAL             17 (str + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1

 468            LOAD_GLOBAL             19 (_redacted_env + NULL)
                CALL                     0

 469            LOAD_CONST              11 (False)

 462            LOAD_CONST              12 (('capture_output', 'text', 'timeout', 'cwd', 'env', 'check'))
                CALL_KW                  7
                STORE_FAST               3 (proc)

 492    L7:     LOAD_SMALL_INT           0
                STORE_FAST               5 (vuln_count)

 493            LOAD_SMALL_INT           0
                STORE_FAST               6 (dep_count)

 495            LOAD_CONST              18 ('LOW')
                LOAD_SMALL_INT           0
                LOAD_CONST              19 ('MEDIUM')
                LOAD_SMALL_INT           0
                LOAD_CONST              20 ('HIGH')
                LOAD_SMALL_INT           0
                LOAD_CONST              21 ('CRITICAL')
                LOAD_SMALL_INT           0
                LOAD_CONST              22 ('UNKNOWN')
                LOAD_SMALL_INT           0

 494            BUILD_MAP                5
                STORE_FAST               7 (sev_counts)

 497    L8:     NOP

 498    L9:     LOAD_GLOBAL             32 (json)
                LOAD_ATTR               34 (loads)
                PUSH_NULL
                LOAD_FAST                3 (proc)
                LOAD_ATTR               36 (stdout)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L12)
       L10:     NOT_TAKEN
       L11:     POP_TOP
                LOAD_CONST              23 ('{}')
       L12:     CALL                     1
                STORE_FAST               8 (data)

 499            LOAD_GLOBAL             39 (isinstance + NULL)
                LOAD_FAST                8 (data)
                LOAD_GLOBAL             40 (dict)
                CALL                     2
                TO_BOOL
                EXTENDED_ARG             2
                POP_JUMP_IF_FALSE      565 (to L50)
                NOT_TAKEN

 507            LOAD_FAST                8 (data)
                LOAD_ATTR               43 (get + NULL|self)
                LOAD_CONST              24 ('metadata')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L15)
       L13:     NOT_TAKEN
       L14:     POP_TOP
                BUILD_MAP                0
       L15:     STORE_FAST               9 (meta)

 508            LOAD_FAST                9 (meta)
                LOAD_ATTR               43 (get + NULL|self)
                LOAD_CONST              25 ('vulnerabilities')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L18)
       L16:     NOT_TAKEN
       L17:     POP_TOP
                BUILD_MAP                0
       L18:     STORE_FAST              10 (v)

 509            LOAD_FAST                9 (meta)
                LOAD_ATTR               43 (get + NULL|self)
                LOAD_CONST              26 ('dependencies')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L21)
       L19:     NOT_TAKEN
       L20:     POP_TOP
                BUILD_MAP                0
       L21:     STORE_FAST              11 (d)

 510            LOAD_GLOBAL             39 (isinstance + NULL)
                LOAD_FAST               10 (v)
                LOAD_GLOBAL             40 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      232 (to L40)
                NOT_TAKEN

 511            LOAD_GLOBAL             45 (int + NULL)
                LOAD_FAST               10 (v)
                LOAD_ATTR               43 (get + NULL|self)
                LOAD_CONST              27 ('total')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L24)
       L22:     NOT_TAKEN
       L23:     POP_TOP
                LOAD_SMALL_INT           0
       L24:     CALL                     1
                STORE_FAST               5 (vuln_count)

 513            LOAD_GLOBAL             45 (int + NULL)
                LOAD_FAST               10 (v)
                LOAD_ATTR               43 (get + NULL|self)
                LOAD_CONST              28 ('low')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L27)
       L25:     NOT_TAKEN
       L26:     POP_TOP
                LOAD_SMALL_INT           0
       L27:     CALL                     1
                LOAD_FAST                7 (sev_counts)
                LOAD_CONST              18 ('LOW')
                STORE_SUBSCR

 514            LOAD_GLOBAL             45 (int + NULL)
                LOAD_FAST               10 (v)
                LOAD_ATTR               43 (get + NULL|self)
                LOAD_CONST              29 ('moderate')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L30)
       L28:     NOT_TAKEN
       L29:     POP_TOP
                LOAD_SMALL_INT           0
       L30:     CALL                     1
                LOAD_FAST                7 (sev_counts)
                LOAD_CONST              19 ('MEDIUM')
                STORE_SUBSCR

 515            LOAD_GLOBAL             45 (int + NULL)
                LOAD_FAST               10 (v)
                LOAD_ATTR               43 (get + NULL|self)
                LOAD_CONST              30 ('high')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L33)
       L31:     NOT_TAKEN
       L32:     POP_TOP
                LOAD_SMALL_INT           0
       L33:     CALL                     1
                LOAD_FAST                7 (sev_counts)
                LOAD_CONST              20 ('HIGH')
                STORE_SUBSCR

 516            LOAD_GLOBAL             45 (int + NULL)
                LOAD_FAST               10 (v)
                LOAD_ATTR               43 (get + NULL|self)
                LOAD_CONST              31 ('critical')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L36)
       L34:     NOT_TAKEN
       L35:     POP_TOP
                LOAD_SMALL_INT           0
       L36:     CALL                     1
                LOAD_FAST                7 (sev_counts)
                LOAD_CONST              21 ('CRITICAL')
                STORE_SUBSCR

 517            LOAD_GLOBAL             45 (int + NULL)
                LOAD_FAST               10 (v)
                LOAD_ATTR               43 (get + NULL|self)
                LOAD_CONST              32 ('info')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L39)
       L37:     NOT_TAKEN
       L38:     POP_TOP
                LOAD_SMALL_INT           0
       L39:     CALL                     1
                LOAD_FAST                7 (sev_counts)
                LOAD_CONST              22 ('UNKNOWN')
                STORE_SUBSCR

 518   L40:     LOAD_GLOBAL             39 (isinstance + NULL)
                LOAD_FAST               11 (d)
                LOAD_GLOBAL             40 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       37 (to L44)
                NOT_TAKEN

 519            LOAD_GLOBAL             45 (int + NULL)
                LOAD_FAST               11 (d)
                LOAD_ATTR               43 (get + NULL|self)
                LOAD_CONST              27 ('total')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L43)
       L41:     NOT_TAKEN
       L42:     POP_TOP
                LOAD_SMALL_INT           0
       L43:     CALL                     1
                STORE_FAST               6 (dep_count)

 520   L44:     LOAD_FAST                5 (vuln_count)
                LOAD_SMALL_INT           0
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE      166 (to L50)
                NOT_TAKEN
                LOAD_GLOBAL             39 (isinstance + NULL)
                LOAD_FAST                8 (data)
                LOAD_ATTR               43 (get + NULL|self)
                LOAD_CONST              33 ('advisories')
                CALL                     1
                LOAD_GLOBAL             40 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      129 (to L50)
                NOT_TAKEN

 522            LOAD_FAST                8 (data)
                LOAD_CONST              33 ('advisories')
                BINARY_OP               26 ([])
                STORE_FAST              12 (advisories)

 523            LOAD_GLOBAL             47 (len + NULL)
                LOAD_FAST               12 (advisories)
                CALL                     1
                STORE_FAST               5 (vuln_count)

 524            LOAD_FAST               12 (advisories)
                LOAD_ATTR               49 (values + NULL|self)
                CALL                     0
                GET_ITER
       L45:     FOR_ITER                88 (to L49)
                STORE_FAST              13 (adv)

 525            LOAD_GLOBAL             39 (isinstance + NULL)
                LOAD_FAST               13 (adv)
                LOAD_GLOBAL             40 (dict)
                CALL                     2
                TO_BOOL
       L46:     POP_JUMP_IF_TRUE         3 (to L47)
                NOT_TAKEN
                JUMP_BACKWARD           27 (to L45)

 526   L47:     LOAD_GLOBAL             51 (_classify_severity + NULL)
                LOAD_FAST               13 (adv)
                LOAD_ATTR               43 (get + NULL|self)
                LOAD_CONST              34 ('severity')
                CALL                     1
                CALL                     1
                STORE_FAST              14 (t)

 527            LOAD_FAST_LOAD_FAST    231 (t, sev_counts)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE        3 (to L48)
                NOT_TAKEN

 528            LOAD_CONST              22 ('UNKNOWN')
                STORE_FAST              14 (t)

 529   L48:     LOAD_FAST                7 (sev_counts)
                LOAD_ATTR               43 (get + NULL|self)
                LOAD_FAST               14 (t)
                LOAD_SMALL_INT           0
                CALL                     2
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_FAST_LOAD_FAST    126 (sev_counts, t)
                STORE_SUBSCR
                JUMP_BACKWARD           90 (to L45)

 524   L49:     END_FOR
                POP_ITER

 544   L50:     LOAD_FAST                5 (vuln_count)
                LOAD_SMALL_INT           0
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE       34 (to L52)
                NOT_TAKEN

 545            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 546            LOAD_CONST               1 ('npm')

 547            LOAD_CONST              39 ('warning')

 548            LOAD_FAST                1 (lockfile)

 549            LOAD_FAST                6 (dep_count)

 550            LOAD_FAST                5 (vuln_count)

 551            LOAD_FAST                7 (sev_counts)

 552            LOAD_CONST              40 ('vulnerabilities:')
                LOAD_FAST                5 (vuln_count)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 553            LOAD_FAST                3 (proc)
                LOAD_ATTR               52 (returncode)

 545            LOAD_CONST              41 (('scanner', 'status', 'lockfile', 'dependency_count', 'vulnerability_count', 'severities', 'warnings', 'raw_exit_code'))
                CALL_KW                  8
       L51:     RETURN_VALUE

 555   L52:     LOAD_GLOBAL              3 (_safe_envelope + NULL)

 556            LOAD_CONST               1 ('npm')

 557            LOAD_CONST              42 ('ok')

 558            LOAD_FAST                1 (lockfile)

 559            LOAD_FAST                6 (dep_count)

 560            LOAD_SMALL_INT           0

 561            LOAD_FAST                7 (sev_counts)

 562            LOAD_FAST                3 (proc)
                LOAD_ATTR               52 (returncode)

 555            LOAD_CONST              43 (('scanner', 'status', 'lockfile', 'dependency_count', 'vulnerability_count', 'severities', 'raw_exit_code'))
                CALL_KW                  7
       L53:     RETURN_VALUE

  --   L54:     PUSH_EXC_INFO

 471            LOAD_GLOBAL             10 (subprocess)
                LOAD_ATTR               20 (TimeoutExpired)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       21 (to L57)
                NOT_TAKEN
                POP_TOP

 472            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 473            LOAD_CONST               1 ('npm')

 474            LOAD_CONST              13 ('failed')

 475            LOAD_FAST                1 (lockfile)

 476            LOAD_CONST              14 ('scanner_timeout')
                BUILD_LIST               1

 477            LOAD_CONST              14 ('scanner_timeout')

 472            LOAD_CONST               5 (('scanner', 'status', 'lockfile', 'warnings', 'error_code'))
                CALL_KW                  5
                SWAP                     2
       L55:     POP_EXCEPT
       L56:     RETURN_VALUE

 479   L57:     LOAD_GLOBAL             22 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       93 (to L65)
       L58:     NOT_TAKEN
       L59:     STORE_FAST               4 (e)

 480   L60:     LOAD_GLOBAL             24 (logger)
                LOAD_ATTR               27 (warning + NULL|self)

 481            LOAD_CONST              15 ('scan_node_dependencies subprocess error type=')

 482            LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE

 481            BUILD_STRING             2

 480            CALL                     1
                POP_TOP

 484            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 485            LOAD_CONST               1 ('npm')

 486            LOAD_CONST              13 ('failed')

 487            LOAD_FAST                1 (lockfile)

 488            LOAD_CONST              16 ('scanner_subprocess:')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 489            LOAD_CONST              17 ('scanner_subprocess_failed')

 484            LOAD_CONST               5 (('scanner', 'status', 'lockfile', 'warnings', 'error_code'))
                CALL_KW                  5
       L61:     SWAP                     2
       L62:     POP_EXCEPT
                LOAD_CONST               3 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
       L63:     RETURN_VALUE

  --   L64:     LOAD_CONST               3 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RERAISE                  1

 479   L65:     RERAISE                  0

  --   L66:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L67:     PUSH_EXC_INFO

 530            LOAD_GLOBAL             22 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      104 (to L73)
                NOT_TAKEN
                STORE_FAST               4 (e)

 531   L68:     LOAD_GLOBAL             24 (logger)
                LOAD_ATTR               27 (warning + NULL|self)

 532            LOAD_CONST              35 ('scan_node_dependencies parse error type=')

 533            LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE

 532            BUILD_STRING             2

 531            CALL                     1
                POP_TOP

 535            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 536            LOAD_CONST               1 ('npm')

 537            LOAD_CONST              13 ('failed')

 538            LOAD_FAST                1 (lockfile)

 539            LOAD_CONST              36 ('scanner_parse_failed:')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 540            LOAD_CONST              37 ('scanner_parse_failed')

 541            LOAD_FAST                3 (proc)
                LOAD_ATTR               52 (returncode)

 535            LOAD_CONST              38 (('scanner', 'status', 'lockfile', 'warnings', 'error_code', 'raw_exit_code'))
                CALL_KW                  6
       L69:     SWAP                     2
       L70:     POP_EXCEPT
                LOAD_CONST               3 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
       L71:     RETURN_VALUE

  --   L72:     LOAD_CONST               3 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RERAISE                  1

 530   L73:     RERAISE                  0

  --   L74:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L75:     PUSH_EXC_INFO

 564            LOAD_GLOBAL             22 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      115 (to L80)
                NOT_TAKEN
                STORE_FAST               4 (e)

 565   L76:     LOAD_GLOBAL             24 (logger)
                LOAD_ATTR               27 (warning + NULL|self)

 566            LOAD_CONST              44 ('scan_node_dependencies error type=')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 565            CALL                     1
                POP_TOP

 568            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 569            LOAD_CONST               1 ('npm')

 570            LOAD_CONST              13 ('failed')

 571            LOAD_CONST               3 (None)

 572            LOAD_CONST              45 ('unexpected:')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 573            LOAD_CONST              45 ('unexpected:')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 568            LOAD_CONST               5 (('scanner', 'status', 'lockfile', 'warnings', 'error_code'))
                CALL_KW                  5
       L77:     SWAP                     2
       L78:     POP_EXCEPT
                LOAD_CONST               3 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RETURN_VALUE

  --   L79:     LOAD_CONST               3 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RERAISE                  1

 564   L80:     RERAISE                  0

  --   L81:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L75 [0]
  L3 to L4 -> L75 [0]
  L6 to L7 -> L54 [0]
  L7 to L8 -> L75 [0]
  L9 to L10 -> L67 [0]
  L11 to L13 -> L67 [0]
  L14 to L16 -> L67 [0]
  L17 to L19 -> L67 [0]
  L20 to L22 -> L67 [0]
  L23 to L25 -> L67 [0]
  L26 to L28 -> L67 [0]
  L29 to L31 -> L67 [0]
  L32 to L34 -> L67 [0]
  L35 to L37 -> L67 [0]
  L38 to L41 -> L67 [0]
  L42 to L46 -> L67 [0]
  L47 to L50 -> L67 [0]
  L50 to L51 -> L75 [0]
  L52 to L53 -> L75 [0]
  L54 to L55 -> L66 [1] lasti
  L55 to L56 -> L75 [0]
  L57 to L58 -> L66 [1] lasti
  L59 to L60 -> L66 [1] lasti
  L60 to L61 -> L64 [1] lasti
  L61 to L62 -> L66 [1] lasti
  L62 to L63 -> L75 [0]
  L64 to L66 -> L66 [1] lasti
  L66 to L67 -> L75 [0]
  L67 to L68 -> L74 [1] lasti
  L68 to L69 -> L72 [1] lasti
  L69 to L70 -> L74 [1] lasti
  L70 to L71 -> L75 [0]
  L72 to L74 -> L74 [1] lasti
  L74 to L75 -> L75 [0]
  L75 to L76 -> L81 [1] lasti
  L76 to L77 -> L79 [1] lasti
  L77 to L78 -> L81 [1] lasti
  L79 to L81 -> L81 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "app/services/security/dependency_scanner.py", line 577>:
577           RESUME                   0
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
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object scan_all at 0x0000018C17CC1CE0, file "app/services/security/dependency_scanner.py", line 577>:
577           RESUME                   0

580           LOAD_GLOBAL              1 (scan_python_dependencies + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              STORE_FAST               1 (py)

581           LOAD_GLOBAL              3 (scan_node_dependencies + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              STORE_FAST               2 (nd)

582           LOAD_CONST               1 ('ok')
              STORE_FAST               3 (overall_status)

583           LOAD_FAST_BORROW         1 (py)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               2 ('status')
              CALL                     1
              LOAD_CONST               3 ('warning')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_TRUE        23 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         2 (nd)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               2 ('status')
              CALL                     1
              LOAD_CONST               3 ('warning')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

584   L1:     LOAD_CONST               3 ('warning')
              STORE_FAST               3 (overall_status)

585   L2:     LOAD_FAST_BORROW         1 (py)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               2 ('status')
              CALL                     1
              LOAD_CONST               4 ('failed')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_TRUE        23 (to L3)
              NOT_TAKEN
              LOAD_FAST_BORROW         2 (nd)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               2 ('status')
              CALL                     1
              LOAD_CONST               4 ('failed')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN

586   L3:     LOAD_CONST               3 ('warning')
              STORE_FAST               3 (overall_status)

588   L4:     LOAD_CONST               2 ('status')
              LOAD_FAST                3 (overall_status)

589           LOAD_CONST               5 ('python')
              LOAD_FAST                1 (py)

590           LOAD_CONST               6 ('node')
              LOAD_FAST                2 (nd)

591           LOAD_CONST               7 ('warnings')
              LOAD_GLOBAL              7 (list + NULL)
              LOAD_FAST_BORROW         1 (py)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               7 ('warnings')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L5:     CALL                     1
              LOAD_GLOBAL              7 (list + NULL)
              LOAD_FAST_BORROW         2 (nd)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               7 ('warnings')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L6)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L6:     CALL                     1
              BINARY_OP                0 (+)

592           LOAD_CONST               8 ('generated_at')
              LOAD_GLOBAL              9 (_now_iso + NULL)
              CALL                     0

587           BUILD_MAP                5
              RETURN_VALUE
```
