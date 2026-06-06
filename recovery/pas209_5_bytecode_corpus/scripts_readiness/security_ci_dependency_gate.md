# scripts_readiness/security_ci_dependency_gate

- **pyc:** `scripts\__pycache__\security_ci_dependency_gate.cpython-314.pyc`
- **expected source path (absent):** `scripts/security_ci_dependency_gate.py`
- **co_filename (from bytecode):** `scripts/security_ci_dependency_gate.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS-SECURITY-03 — CI dependency scanner gate.

Wraps the PAS-SECURITY-02 ``security_dependency_audit``
report-only scanner for use as a CI gate. Designed to run on
every PR / merge in a Github Actions or Railway-equivalent
workflow.

Doctrine:

* **Report-only.** No auto-fix, no upgrades, no
  `pip install`, no `npm install`, no lockfile mutation.
* **CI-aware exit codes.** In CI mode (default), a scanner
  failure or vulnerability finding above the configured
  severity threshold exits 1. Local mode (``--local``)
  always exits 0 with a structural warning.
* **Scanner-unavailable handling.** CI mode without
  ``--allow-missing-scanner`` treats a missing scanner as a
  hard failure (exit 1). With the flag, scanner-missing is
  surfaced as a warning + exit 0.
* **No new dependency added** — operator installs
  ``pip-audit`` in the CI container; this script wraps the
  PAS-SECURITY-02 service helpers as-is.
* **No secrets / env values printed.** Stdout carries only
  the bounded structural envelope.
* **NEVER raises.** All exceptions become structural
  ``failed`` envelopes.

Usage:

    # CI mode (default) — fail build on any finding.
    python scripts/security_ci_dependency_gate.py

    # CI mode — fail only on high+ severity findings.
    python scripts/security_ci_dependency_gate.py --fail-on-high

    # CI mode — fail only on critical findings.
    python scripts/security_ci_dependency_gate.py --fail-on-critical

    # CI mode — allow missing scanner (e.g. early bootstrap).
    python scripts/security_ci_dependency_gate.py --allow-missing-scanner

    # Local mode — never blocks; always exits 0.
    python scripts/security_ci_dependency_gate.py --local

    # Emit JSON envelope on stdout.
    python scripts/security_ci_dependency_gate.py --json

Exit codes:
    0  — ok / warning (in local mode) / scanner-missing-allowed
    1  — blocker vulnerabilities / scanner required but missing
    2  — bad CLI arguments
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.services.security.dependency_scanner`, `argparse`, `datetime`, `json`, `logging`, `os`, `scan_node_dependencies`, `scan_python_dependencies`, `sys`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_build_parser`, `_now_iso`, `_print_summary`, `_resolve_threshold`, `_scanner_failed`, `_scanner_missing`, `_scanner_result_blocks`, `main`

## Env-key candidates

`CRITICAL`, `HIGH`, `LOW`, `MEDIUM`, `UNKNOWN`

## String constants (redacted where noted)

- '\nPAS-SECURITY-03 — CI dependency scanner gate.\n\nWraps the PAS-SECURITY-02 ``security_dependency_audit``\nreport-only scanner for use as a CI gate. Designed to run on\nevery PR / merge in a Github Actions or Railway-equivalent\nworkflow.\n\nDoctrine:\n\n* **Report-only.** No auto-fix, no upgrades, no\n  `pip install`, no `npm install`, no lockfile mutation.\n* **CI-aware exit codes.** In CI mode (default), a scanner\n  failure or vulnerability finding above the configured\n  severity threshold exits 1. Local mode (``--local``)\n  always exits 0 with a structural warning.\n* **Scanner-unavailable handling.** CI mode without\n  ``--allow-missing-scanner`` treats a missing scanner as a\n  hard failure (exit 1). With the flag, scanner-missing is\n  surfaced as a warning + exit 0.\n* **No new dependency added** — operator installs\n  ``pip-audit`` in the CI container; this script wraps the\n  PAS-SECURITY-02 service helpers as-is.\n* **No secrets / env values printed.** Stdout carries only\n  the bounded structural envelope.\n* **NEVER raises.** All exceptions become structural\n  ``failed`` envelopes.\n\nUsage:\n\n    # CI mode (default) — fail build on any finding.\n    python scripts/security_ci_dependency_gate.py\n\n    # CI mode — fail only on high+ severity findings.\n    python scripts/security_ci_dependency_gate.py --fail-on-high\n\n    # CI mode — fail only on critical findings.\n    python scripts/security_ci_dependency_gate.py --fail-on-critical\n\n    # CI mode — allow missing scanner (e.g. early bootstrap).\n    python scripts/security_ci_dependency_gate.py --allow-missing-scanner\n\n    # Local mode — never blocks; always exits 0.\n    python scripts/security_ci_dependency_gate.py --local\n\n    # Emit JSON envelope on stdout.\n    python scripts/security_ci_dependency_gate.py --json\n\nExit codes:\n    0  — ok / warning (in local mode) / scanner-missing-allowed\n    1  — blocker vulnerabilities / scanner required but missing\n    2  — bad CLI arguments\n'
- 'utf-8'
- 'pas.scripts.security_ci_dependency_gate'
- 'return'
- 'str'
- 'seconds'
- 'argparse.ArgumentParser'
- 'security_ci_dependency_gate'
- 'PAS-SECURITY-03 — CI gate for the PAS-SECURITY-02 dependency scanner. Report-only — NEVER auto-fixes, NEVER installs / upgrades packages.'
- '--repo-root'
- "Repo root to scan. Defaults to script's parent dir."
- '--local'
- 'store_true'
- 'Local mode — never blocks; always exits 0 with a structural warning.'
- '--ci'
- 'CI mode (default). Fail build on any finding.'
- '--fail-on-medium'
- 'Fail when scanner reports MEDIUM+ severity findings.'
- '--fail-on-high'
- 'Fail when scanner reports HIGH+ severity findings.'
- '--fail-on-critical'
- 'Fail only when scanner reports CRITICAL severity findings.'
- '--allow-missing-scanner'
- 'In CI mode, treat scanner-missing as a warning (exit 0) instead of a hard fail.'
- '--python-only'
- 'Skip npm audit even when package.json is present.'
- '--node-only'
- 'Skip pip-audit. Useful when only the frontend is in scope.'
- '--json'
- 'Emit JSON envelope on stdout instead of the human summary.'
- 'args'
- 'argparse.Namespace'
- 'Returns the closed severity-tier token.'
- 'critical'
- 'high'
- 'medium'
- 'any'
- 'scanner_env'
- 'Dict[str, Any]'
- 'threshold'
- 'bool'
- 'Decide whether the scanner\'s envelope counts as a blocker\ngiven the configured threshold.\n\nPAS-SECURITY-04 reads the closed ``severities`` dict produced\nby the scanner (LOW / MEDIUM / HIGH / CRITICAL / UNKNOWN\ncounts) and maps the threshold:\n\n  * threshold="any"      — any vulnerability_count > 0 blocks.\n  * threshold="medium"   — MEDIUM + HIGH + CRITICAL block.\n  * threshold="high"     — HIGH + CRITICAL block.\n  * threshold="critical" — CRITICAL only blocks.\n\nUNKNOWN-severity findings ALWAYS block (conservative). The\nPAS-SECURITY-02 fallback shape (no ``severities`` key) is\nstill honored via the legacy ``vulnerability_count`` path.\n'
- 'severities'
- 'CRITICAL'
- 'HIGH'
- 'MEDIUM'
- 'LOW'
- 'UNKNOWN'
- 'vulnerability_count'
- 'tier'
- 'int'
- 'status'
- 'scanner_unavailable'
- 'failed'
- 'env'
- 'None'
- 'python'
- 'node'
- '[PAS-SECURITY-03/ci_gate] verdict='
- 'verdict'
- ' exit='
- 'exit_code'
- ' ci_mode='
- 'ci_mode'
- ' threshold='
- ' python.status='
- ' python.vulns='
- ' node.status='
- ' node.vulns='
- 'warnings'
- '  warn: '
- 'argv'
- 'Optional[List[str]]'
- 'error: --repo-root not a directory: '
- 'security_ci_dependency_gate import error type='
- 'import_failed:'
- 'error_code'
- 'import_failed'
- 'generated_at'
- 'scanner'
- 'pip-audit'
- 'lockfile'
- 'dependency_count'
- 'skipped_by_node_only_flag'
- 'npm'
- 'skipped_by_python_only_flag'
- 'blocker'
- 'vulnerabilities_present'
- 'vulnerabilities_present_local_mode'
- 'scanner_missing'
- 'warning'
- 'scanner_missing_allowed'
- 'scanner_subprocess_failed'

## Disassembly

```
   0           RESUME                   0

   1           LOAD_CONST               0 ('\nPAS-SECURITY-03 — CI dependency scanner gate.\n\nWraps the PAS-SECURITY-02 ``security_dependency_audit``\nreport-only scanner for use as a CI gate. Designed to run on\nevery PR / merge in a Github Actions or Railway-equivalent\nworkflow.\n\nDoctrine:\n\n* **Report-only.** No auto-fix, no upgrades, no\n  `pip install`, no `npm install`, no lockfile mutation.\n* **CI-aware exit codes.** In CI mode (default), a scanner\n  failure or vulnerability finding above the configured\n  severity threshold exits 1. Local mode (``--local``)\n  always exits 0 with a structural warning.\n* **Scanner-unavailable handling.** CI mode without\n  ``--allow-missing-scanner`` treats a missing scanner as a\n  hard failure (exit 1). With the flag, scanner-missing is\n  surfaced as a warning + exit 0.\n* **No new dependency added** — operator installs\n  ``pip-audit`` in the CI container; this script wraps the\n  PAS-SECURITY-02 service helpers as-is.\n* **No secrets / env values printed.** Stdout carries only\n  the bounded structural envelope.\n* **NEVER raises.** All exceptions become structural\n  ``failed`` envelopes.\n\nUsage:\n\n    # CI mode (default) — fail build on any finding.\n    python scripts/security_ci_dependency_gate.py\n\n    # CI mode — fail only on high+ severity findings.\n    python scripts/security_ci_dependency_gate.py --fail-on-high\n\n    # CI mode — fail only on critical findings.\n    python scripts/security_ci_dependency_gate.py --fail-on-critical\n\n    # CI mode — allow missing scanner (e.g. early bootstrap).\n    python scripts/security_ci_dependency_gate.py --allow-missing-scanner\n\n    # Local mode — never blocks; always exits 0.\n    python scripts/security_ci_dependency_gate.py --local\n\n    # Emit JSON envelope on stdout.\n    python scripts/security_ci_dependency_gate.py --json\n\nExit codes:\n    0  — ok / warning (in local mode) / scanner-missing-allowed\n    1  — blocker vulnerabilities / scanner required but missing\n    2  — bad CLI arguments\n')
               STORE_NAME               0 (__doc__)

  55           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  57           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  58           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (json)
               STORE_NAME               4 (json)

  59           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (logging)
               STORE_NAME               5 (logging)

  60           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (os)
               STORE_NAME               6 (os)

  61           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              7 (sys)
               STORE_NAME               7 (sys)

  62           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              8 (datetime)
               IMPORT_FROM              8 (datetime)
               STORE_NAME               8 (datetime)
               IMPORT_FROM              9 (timezone)
               STORE_NAME               9 (timezone)
               POP_TOP

  63           LOAD_SMALL_INT           0
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

  66           LOAD_NAME                7 (sys)
               LOAD_ATTR               30 (stdout)
               LOAD_NAME                7 (sys)
               LOAD_ATTR               32 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              17 (_stream)

  67           NOP

  68   L2:     LOAD_NAME               17 (_stream)
               LOAD_ATTR               37 (reconfigure + NULL|self)
               LOAD_CONST               5 ('utf-8')
               LOAD_CONST               6 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  66   L4:     END_FOR
               POP_ITER

  73           LOAD_NAME                7 (sys)
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

  76           LOAD_NAME                5 (logging)
               LOAD_ATTR               52 (getLogger)
               PUSH_NULL
               LOAD_CONST               8 ('pas.scripts.security_ci_dependency_gate')
               CALL                     1
               STORE_NAME              27 (logger)

  83           LOAD_CONST              26 (('any', 'medium', 'high', 'critical'))
               STORE_NAME              28 (_SEVERITY_TIERS)

  86           LOAD_CONST               9 (<code object __annotate__ at 0x0000018C17FA2F10, file "scripts/security_ci_dependency_gate.py", line 86>)
               MAKE_FUNCTION
               LOAD_CONST              10 (<code object _now_iso at 0x0000018C18038670, file "scripts/security_ci_dependency_gate.py", line 86>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              29 (_now_iso)

  90           LOAD_CONST              11 (<code object __annotate__ at 0x0000018C17FA32D0, file "scripts/security_ci_dependency_gate.py", line 90>)
               MAKE_FUNCTION
               LOAD_CONST              12 (<code object _build_parser at 0x0000018C17ED8EA0, file "scripts/security_ci_dependency_gate.py", line 90>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              30 (_build_parser)

 144           LOAD_CONST              13 (<code object __annotate__ at 0x0000018C17FA1E30, file "scripts/security_ci_dependency_gate.py", line 144>)
               MAKE_FUNCTION
               LOAD_CONST              14 (<code object _resolve_threshold at 0x0000018C17FE13E0, file "scripts/security_ci_dependency_gate.py", line 144>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              31 (_resolve_threshold)

 155           LOAD_CONST              15 (<code object __annotate__ at 0x0000018C18026130, file "scripts/security_ci_dependency_gate.py", line 155>)
               MAKE_FUNCTION
               LOAD_CONST              16 (<code object _scanner_result_blocks at 0x0000018C17D8BD40, file "scripts/security_ci_dependency_gate.py", line 155>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              32 (_scanner_result_blocks)

 216           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C17FA3A50, file "scripts/security_ci_dependency_gate.py", line 216>)
               MAKE_FUNCTION
               LOAD_CONST              18 (<code object _scanner_missing at 0x0000018C17C49B80, file "scripts/security_ci_dependency_gate.py", line 216>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              33 (_scanner_missing)

 223           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA3690, file "scripts/security_ci_dependency_gate.py", line 223>)
               MAKE_FUNCTION
               LOAD_CONST              20 (<code object _scanner_failed at 0x0000018C1802C9B0, file "scripts/security_ci_dependency_gate.py", line 223>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              34 (_scanner_failed)

 230           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA30F0, file "scripts/security_ci_dependency_gate.py", line 230>)
               MAKE_FUNCTION
               LOAD_CONST              22 (<code object _print_summary at 0x0000018C17F63D60, file "scripts/security_ci_dependency_gate.py", line 230>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              35 (_print_summary)

 248           LOAD_CONST              27 ((None,))
               LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA3F00, file "scripts/security_ci_dependency_gate.py", line 248>)
               MAKE_FUNCTION
               LOAD_CONST              24 (<code object main at 0x0000018C17F5BE50, file "scripts/security_ci_dependency_gate.py", line 248>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              36 (main)

 368           LOAD_NAME               37 (__name__)
               LOAD_CONST              25 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 369           LOAD_NAME                7 (sys)
               LOAD_ATTR               76 (exit)
               PUSH_NULL
               LOAD_NAME               36 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 368   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  69           LOAD_NAME               19 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L8)
               NOT_TAKEN
               POP_TOP

  70   L7:     POP_EXCEPT
               JUMP_BACKWARD          244 (to L1)

  69   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "scripts/security_ci_dependency_gate.py", line 86>:
 86           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038670, file "scripts/security_ci_dependency_gate.py", line 86>:
 86           RESUME                   0

 87           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA32D0, file "scripts/security_ci_dependency_gate.py", line 90>:
 90           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C17ED8EA0, file "scripts/security_ci_dependency_gate.py", line 90>:
 90           RESUME                   0

 91           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

 92           LOAD_CONST               0 ('security_ci_dependency_gate')

 94           LOAD_CONST               1 ('PAS-SECURITY-03 — CI gate for the PAS-SECURITY-02 dependency scanner. Report-only — NEVER auto-fixes, NEVER installs / upgrades packages.')

 91           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

 99           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

100           LOAD_CONST               3 ('--repo-root')
              LOAD_CONST               4 (None)

101           LOAD_CONST               5 ("Repo root to scan. Defaults to script's parent dir.")

 99           LOAD_CONST               6 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

103           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                7 (add_mutually_exclusive_group + NULL|self)
              CALL                     0
              STORE_FAST               1 (mode_group)

104           LOAD_FAST_BORROW         1 (mode_group)
              LOAD_ATTR                5 (add_argument + NULL|self)

105           LOAD_CONST               7 ('--local')
              LOAD_CONST               8 ('store_true')

106           LOAD_CONST               9 ('Local mode — never blocks; always exits 0 with a structural warning.')

104           LOAD_CONST              10 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

108           LOAD_FAST_BORROW         1 (mode_group)
              LOAD_ATTR                5 (add_argument + NULL|self)

109           LOAD_CONST              11 ('--ci')
              LOAD_CONST               8 ('store_true')

110           LOAD_CONST              12 ('CI mode (default). Fail build on any finding.')

108           LOAD_CONST              10 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

112           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

113           LOAD_CONST              13 ('--fail-on-medium')
              LOAD_CONST               8 ('store_true')

114           LOAD_CONST              14 ('Fail when scanner reports MEDIUM+ severity findings.')

112           LOAD_CONST              10 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

116           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

117           LOAD_CONST              15 ('--fail-on-high')
              LOAD_CONST               8 ('store_true')

118           LOAD_CONST              16 ('Fail when scanner reports HIGH+ severity findings.')

116           LOAD_CONST              10 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

120           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

121           LOAD_CONST              17 ('--fail-on-critical')
              LOAD_CONST               8 ('store_true')

122           LOAD_CONST              18 ('Fail only when scanner reports CRITICAL severity findings.')

120           LOAD_CONST              10 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

124           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

125           LOAD_CONST              19 ('--allow-missing-scanner')
              LOAD_CONST               8 ('store_true')

126           LOAD_CONST              20 ('In CI mode, treat scanner-missing as a warning (exit 0) instead of a hard fail.')

124           LOAD_CONST              10 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

129           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

130           LOAD_CONST              21 ('--python-only')
              LOAD_CONST               8 ('store_true')

131           LOAD_CONST              22 ('Skip npm audit even when package.json is present.')

129           LOAD_CONST              10 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

133           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

134           LOAD_CONST              23 ('--node-only')
              LOAD_CONST               8 ('store_true')

135           LOAD_CONST              24 ('Skip pip-audit. Useful when only the frontend is in scope.')

133           LOAD_CONST              10 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

137           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

138           LOAD_CONST              25 ('--json')
              LOAD_CONST               8 ('store_true')

139           LOAD_CONST              26 ('Emit JSON envelope on stdout instead of the human summary.')

137           LOAD_CONST              10 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

141           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "scripts/security_ci_dependency_gate.py", line 144>:
144           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('args')
              LOAD_CONST               2 ('argparse.Namespace')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _resolve_threshold at 0x0000018C17FE13E0, file "scripts/security_ci_dependency_gate.py", line 144>:
144           RESUME                   0

146           LOAD_FAST_BORROW         0 (args)
              LOAD_ATTR                0 (fail_on_critical)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN

147           LOAD_CONST               1 ('critical')
              RETURN_VALUE

148   L1:     LOAD_FAST_BORROW         0 (args)
              LOAD_ATTR                2 (fail_on_high)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

149           LOAD_CONST               2 ('high')
              RETURN_VALUE

150   L2:     LOAD_FAST_BORROW         0 (args)
              LOAD_ATTR                4 (fail_on_medium)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

151           LOAD_CONST               3 ('medium')
              RETURN_VALUE

152   L3:     LOAD_CONST               4 ('any')
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026130, file "scripts/security_ci_dependency_gate.py", line 155>:
155           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('scanner_env')

157           LOAD_CONST               2 ('Dict[str, Any]')

155           LOAD_CONST               3 ('threshold')

158           LOAD_CONST               4 ('str')

155           LOAD_CONST               5 ('return')

159           LOAD_CONST               6 ('bool')

155           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _scanner_result_blocks at 0x0000018C17D8BD40, file "scripts/security_ci_dependency_gate.py", line 155>:
  --            MAKE_CELL                9 (severities)

 155            RESUME                   0

 176            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (scanner_env)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN

 177            LOAD_CONST               1 (False)
                RETURN_VALUE

 178    L1:     LOAD_FAST_BORROW         0 (scanner_env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               2 ('severities')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L2)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
        L2:     STORE_DEREF              9 (severities)

 179            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_DEREF               9 (severities)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L3)
                NOT_TAKEN

 180            BUILD_MAP                0
                STORE_DEREF              9 (severities)

 182    L3:     LOAD_CONST               3 (<code object __annotate__ at 0x0000018C17FA21F0, file "scripts/security_ci_dependency_gate.py", line 182>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         9 (severities)
                BUILD_TUPLE              1
                LOAD_CONST               4 (<code object _count at 0x0000018C17F95FD0, file "scripts/security_ci_dependency_gate.py", line 182>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_FAST               2 (_count)

 188            LOAD_FAST_BORROW         2 (_count)
                PUSH_NULL
                LOAD_CONST               5 ('CRITICAL')
                CALL                     1
                STORE_FAST               3 (crit_n)

 189            LOAD_FAST_BORROW         2 (_count)
                PUSH_NULL
                LOAD_CONST               6 ('HIGH')
                CALL                     1
                STORE_FAST               4 (high_n)

 190            LOAD_FAST_BORROW         2 (_count)
                PUSH_NULL
                LOAD_CONST               7 ('MEDIUM')
                CALL                     1
                STORE_FAST               5 (med_n)

 191            LOAD_FAST_BORROW         2 (_count)
                PUSH_NULL
                LOAD_CONST               8 ('LOW')
                CALL                     1
                STORE_FAST               6 (low_n)

 192            LOAD_FAST_BORROW         2 (_count)
                PUSH_NULL
                LOAD_CONST               9 ('UNKNOWN')
                CALL                     1
                STORE_FAST               7 (unk_n)

 196            LOAD_FAST_BORROW         7 (unk_n)
                LOAD_SMALL_INT           0
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE       10 (to L4)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (threshold)
                LOAD_CONST              10 ('critical')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE        3 (to L4)
                NOT_TAKEN

 197            LOAD_CONST              11 (True)
                RETURN_VALUE

 199    L4:     LOAD_FAST_BORROW         1 (threshold)
                LOAD_CONST              10 ('critical')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        6 (to L5)
                NOT_TAKEN

 200            LOAD_FAST_BORROW         3 (crit_n)
                LOAD_SMALL_INT           0
                COMPARE_OP             132 (>)
                RETURN_VALUE

 201    L5:     LOAD_FAST_BORROW         1 (threshold)
                LOAD_CONST              12 ('high')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       19 (to L7)
                NOT_TAKEN

 202            LOAD_FAST_BORROW         3 (crit_n)
                LOAD_SMALL_INT           0
                COMPARE_OP             132 (>)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         6 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         4 (high_n)
                LOAD_SMALL_INT           0
                COMPARE_OP             132 (>)
        L6:     RETURN_VALUE

 203    L7:     LOAD_FAST_BORROW         1 (threshold)
                LOAD_CONST              13 ('medium')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       32 (to L9)
                NOT_TAKEN

 204            LOAD_FAST_BORROW         3 (crit_n)
                LOAD_SMALL_INT           0
                COMPARE_OP             132 (>)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        19 (to L8)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         4 (high_n)
                LOAD_SMALL_INT           0
                COMPARE_OP             132 (>)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         6 (to L8)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         5 (med_n)
                LOAD_SMALL_INT           0
                COMPARE_OP             132 (>)
        L8:     RETURN_VALUE

 208    L9:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (crit_n, high_n)
                BINARY_OP                0 (+)
                LOAD_FAST_BORROW         5 (med_n)
                BINARY_OP                0 (+)
                LOAD_FAST_BORROW         6 (low_n)
                BINARY_OP                0 (+)
                LOAD_FAST_BORROW         7 (unk_n)
                BINARY_OP                0 (+)
                STORE_FAST               8 (total)

 209            LOAD_FAST_BORROW         8 (total)
                LOAD_SMALL_INT           0
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN

 210            LOAD_CONST              11 (True)
                RETURN_VALUE

 211   L10:     LOAD_GLOBAL              7 (int + NULL)
                LOAD_FAST_BORROW         0 (scanner_env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST              14 ('vulnerability_count')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L11)
                NOT_TAKEN
                POP_TOP
                LOAD_SMALL_INT           0
       L11:     CALL                     1
                LOAD_SMALL_INT           0
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE        3 (to L12)
                NOT_TAKEN

 212            LOAD_CONST              11 (True)
                RETURN_VALUE

 213   L12:     LOAD_CONST               1 (False)
                RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "scripts/security_ci_dependency_gate.py", line 182>:
182           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('tier')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('int')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _count at 0x0000018C17F95FD0, file "scripts/security_ci_dependency_gate.py", line 182>:
  --           COPY_FREE_VARS           1

 182           RESUME                   0

 183           NOP

 184   L1:     LOAD_GLOBAL              1 (max + NULL)
               LOAD_SMALL_INT           0
               LOAD_GLOBAL              3 (int + NULL)
               LOAD_DEREF               1 (severities)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_FAST_BORROW         0 (tier)
               LOAD_SMALL_INT           0
               CALL                     2
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L4)
       L2:     NOT_TAKEN
       L3:     POP_TOP
               LOAD_SMALL_INT           0
       L4:     CALL                     1
               CALL                     2
       L5:     RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

 185           LOAD_GLOBAL              6 (TypeError)
               LOAD_GLOBAL              8 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L8)
               NOT_TAKEN
               POP_TOP

 186   L7:     POP_EXCEPT
               LOAD_SMALL_INT           0
               RETURN_VALUE

 185   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L6 [0]
  L3 to L5 -> L6 [0]
  L6 to L7 -> L9 [1] lasti
  L8 to L9 -> L9 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "scripts/security_ci_dependency_gate.py", line 216>:
216           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('scanner_env')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _scanner_missing at 0x0000018C17C49B80, file "scripts/security_ci_dependency_gate.py", line 216>:
216           RESUME                   0

218           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (scanner_env)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       21 (to L1)
              NOT_TAKEN
              POP_TOP

219           LOAD_FAST_BORROW         0 (scanner_env)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               0 ('status')
              CALL                     1
              LOAD_CONST               1 ('scanner_unavailable')
              COMPARE_OP              72 (==)

217   L1:     RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "scripts/security_ci_dependency_gate.py", line 223>:
223           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('scanner_env')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _scanner_failed at 0x0000018C1802C9B0, file "scripts/security_ci_dependency_gate.py", line 223>:
223           RESUME                   0

225           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (scanner_env)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       21 (to L1)
              NOT_TAKEN
              POP_TOP

226           LOAD_FAST_BORROW         0 (scanner_env)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               0 ('status')
              CALL                     1
              LOAD_CONST               1 ('failed')
              COMPARE_OP              72 (==)

224   L1:     RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA30F0, file "scripts/security_ci_dependency_gate.py", line 230>:
230           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C17F63D60, file "scripts/security_ci_dependency_gate.py", line 230>:
230           RESUME                   0

231           LOAD_FAST_BORROW         0 (env)
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

232           LOAD_FAST_BORROW         0 (env)
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

233           LOAD_GLOBAL              3 (print + NULL)

234           LOAD_CONST               2 ('[PAS-SECURITY-03/ci_gate] verdict=')

235           LOAD_FAST_BORROW         0 (env)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               3 ('verdict')
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST               4 (' exit=')

236           LOAD_FAST_BORROW         0 (env)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               5 ('exit_code')
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST               6 (' ci_mode=')

237           LOAD_FAST_BORROW         0 (env)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               7 ('ci_mode')
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST               8 (' threshold=')

238           LOAD_FAST_BORROW         0 (env)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               9 ('threshold')
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST              10 (' python.status=')

239           LOAD_FAST_BORROW         1 (py)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              11 ('status')
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST              12 (' python.vulns=')

240           LOAD_FAST_BORROW         1 (py)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              13 ('vulnerability_count')
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST              14 (' node.status=')

241           LOAD_FAST_BORROW         2 (nd)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              11 ('status')
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST              15 (' node.vulns=')

242           LOAD_FAST_BORROW         2 (nd)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              13 ('vulnerability_count')
              CALL                     1
              FORMAT_SIMPLE

234           BUILD_STRING            16

233           CALL                     1
              POP_TOP

244           LOAD_FAST_BORROW         0 (env)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              16 ('warnings')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L3:     LOAD_CONST              17 (slice(None, 10, None))
              BINARY_OP               26 ([])
              GET_ITER
      L4:     FOR_ITER                17 (to L5)
              STORE_FAST               3 (w)

245           LOAD_GLOBAL              3 (print + NULL)
              LOAD_CONST              18 ('  warn: ')
              LOAD_FAST_BORROW         3 (w)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L4)

244   L5:     END_FOR
              POP_ITER
              LOAD_CONST              19 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3F00, file "scripts/security_ci_dependency_gate.py", line 248>:
248           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17F5BE50, file "scripts/security_ci_dependency_gate.py", line 248>:
 248            RESUME                   0

 249            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 250            NOP

 251    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 255    L2:     LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               15 (abspath + NULL|self)

 256            LOAD_FAST                2 (args)
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

 255    L3:     CALL                     1
                STORE_FAST               4 (repo_root)

 258            LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               25 (isdir + NULL|self)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L4)
                NOT_TAKEN

 259            LOAD_GLOBAL             27 (print + NULL)
                LOAD_CONST               3 ('error: --repo-root not a directory: ')
                LOAD_FAST                4 (repo_root)
                FORMAT_SIMPLE
                BUILD_STRING             2
                LOAD_GLOBAL             28 (sys)
                LOAD_ATTR               30 (stderr)
                LOAD_CONST               4 (('file',))
                CALL_KW                  2
                POP_TOP

 260            LOAD_SMALL_INT           2
                RETURN_VALUE

 262    L4:     LOAD_FAST                2 (args)
                LOAD_ATTR               32 (local)
                TO_BOOL
                UNARY_NOT
                STORE_FAST               5 (ci_mode)

 263            LOAD_GLOBAL             35 (_resolve_threshold + NULL)
                LOAD_FAST                2 (args)
                CALL                     1
                STORE_FAST               6 (threshold)

 264            BUILD_LIST               0
                STORE_FAST               7 (warnings)

 266            NOP

 267    L5:     LOAD_SMALL_INT           0
                LOAD_CONST               5 (('scan_python_dependencies', 'scan_node_dependencies'))
                IMPORT_NAME             18 (app.services.security.dependency_scanner)
                IMPORT_FROM             19 (scan_python_dependencies)
                STORE_FAST               8 (scan_python_dependencies)
                IMPORT_FROM             20 (scan_node_dependencies)
                STORE_FAST               9 (scan_node_dependencies)
                POP_TOP

 293    L6:     LOAD_FAST                2 (args)
                LOAD_ATTR               60 (node_only)
                TO_BOOL
                POP_JUMP_IF_TRUE         9 (to L7)
                NOT_TAKEN

 292            LOAD_FAST                8 (scan_python_dependencies)
                PUSH_NULL
                LOAD_FAST                4 (repo_root)
                CALL                     1
                JUMP_FORWARD            16 (to L8)

 295    L7:     LOAD_CONST              21 ('scanner')
                LOAD_CONST              22 ('pip-audit')
                LOAD_CONST              23 ('status')
                LOAD_CONST              24 ('scanner_unavailable')

 296            LOAD_CONST              25 ('lockfile')
                LOAD_CONST               1 (None)
                LOAD_CONST              26 ('dependency_count')
                LOAD_SMALL_INT           0

 297            LOAD_CONST              27 ('vulnerability_count')
                LOAD_SMALL_INT           0

 298            LOAD_CONST              13 ('warnings')
                LOAD_CONST              28 ('skipped_by_node_only_flag')
                BUILD_LIST               1

 299            LOAD_CONST              15 ('error_code')
                LOAD_CONST              28 ('skipped_by_node_only_flag')

 294            BUILD_MAP                7

 291    L8:     STORE_FAST              11 (py)

 304            LOAD_FAST                2 (args)
                LOAD_ATTR               62 (python_only)
                TO_BOOL
                POP_JUMP_IF_TRUE         9 (to L9)
                NOT_TAKEN

 303            LOAD_FAST                9 (scan_node_dependencies)
                PUSH_NULL
                LOAD_FAST                4 (repo_root)
                CALL                     1
                JUMP_FORWARD            16 (to L10)

 306    L9:     LOAD_CONST              21 ('scanner')
                LOAD_CONST              29 ('npm')
                LOAD_CONST              23 ('status')
                LOAD_CONST              24 ('scanner_unavailable')

 307            LOAD_CONST              25 ('lockfile')
                LOAD_CONST               1 (None)
                LOAD_CONST              26 ('dependency_count')
                LOAD_SMALL_INT           0

 308            LOAD_CONST              27 ('vulnerability_count')
                LOAD_SMALL_INT           0

 309            LOAD_CONST              13 ('warnings')
                LOAD_CONST              30 ('skipped_by_python_only_flag')
                BUILD_LIST               1

 310            LOAD_CONST              15 ('error_code')
                LOAD_CONST              30 ('skipped_by_python_only_flag')

 305            BUILD_MAP                7

 302   L10:     STORE_FAST              12 (nd)

 315            LOAD_GLOBAL             65 (_scanner_result_blocks + NULL)
                LOAD_FAST_LOAD_FAST    182 (py, threshold)
                LOAD_CONST              31 (('scanner_env', 'threshold'))
                CALL_KW                  2
                STORE_FAST              13 (py_blocks)

 316            LOAD_GLOBAL             65 (_scanner_result_blocks + NULL)
                LOAD_FAST_LOAD_FAST    198 (nd, threshold)
                LOAD_CONST              31 (('scanner_env', 'threshold'))
                CALL_KW                  2
                STORE_FAST              14 (nd_blocks)

 317            LOAD_GLOBAL             67 (_scanner_missing + NULL)
                LOAD_FAST               11 (py)
                CALL                     1
                STORE_FAST              15 (py_missing)

 318            LOAD_GLOBAL             67 (_scanner_missing + NULL)
                LOAD_FAST               12 (nd)
                CALL                     1
                STORE_FAST              16 (nd_missing)

 319            LOAD_GLOBAL             69 (_scanner_failed + NULL)
                LOAD_FAST               11 (py)
                CALL                     1
                STORE_FAST              17 (py_failed)

 320            LOAD_GLOBAL             69 (_scanner_failed + NULL)
                LOAD_FAST               12 (nd)
                CALL                     1
                STORE_FAST              18 (nd_failed)

 322            LOAD_CONST              32 ('ok')
                STORE_FAST              19 (verdict)

 323            LOAD_SMALL_INT           0
                STORE_FAST              20 (exit_code)

 324            LOAD_CONST               1 (None)
                STORE_FAST              21 (error_code)

 326            LOAD_FAST               13 (py_blocks)
                TO_BOOL
                POP_JUMP_IF_TRUE         9 (to L11)
                NOT_TAKEN
                LOAD_FAST               14 (nd_blocks)
                TO_BOOL
                POP_JUMP_IF_FALSE       34 (to L13)
                NOT_TAKEN

 327   L11:     LOAD_CONST              33 ('blocker')
                STORE_FAST              19 (verdict)

 328            LOAD_FAST                5 (ci_mode)
                TO_BOOL
                POP_JUMP_IF_FALSE        6 (to L12)
                NOT_TAKEN

 329            LOAD_SMALL_INT           1
                STORE_FAST              20 (exit_code)

 330            LOAD_CONST              34 ('vulnerabilities_present')
                STORE_FAST              21 (error_code)
                JUMP_FORWARD           122 (to L18)

 332   L12:     LOAD_FAST                7 (warnings)
                LOAD_ATTR               71 (append + NULL|self)
                LOAD_CONST              35 ('vulnerabilities_present_local_mode')
                CALL                     1
                POP_TOP
                JUMP_FORWARD           104 (to L18)

 333   L13:     LOAD_FAST               15 (py_missing)
                TO_BOOL
                POP_JUMP_IF_TRUE         9 (to L14)
                NOT_TAKEN
                LOAD_FAST               16 (nd_missing)
                TO_BOOL
                POP_JUMP_IF_FALSE       54 (to L16)
                NOT_TAKEN

 334   L14:     LOAD_FAST                5 (ci_mode)
                TO_BOOL
                POP_JUMP_IF_FALSE       26 (to L15)
                NOT_TAKEN
                LOAD_FAST                2 (args)
                LOAD_ATTR               72 (allow_missing_scanner)
                TO_BOOL
                POP_JUMP_IF_TRUE         8 (to L15)
                NOT_TAKEN

 335            LOAD_CONST              33 ('blocker')
                STORE_FAST              19 (verdict)

 336            LOAD_SMALL_INT           1
                STORE_FAST              20 (exit_code)

 337            LOAD_CONST              36 ('scanner_missing')
                STORE_FAST              21 (error_code)
                JUMP_FORWARD            55 (to L18)

 339   L15:     LOAD_CONST              37 ('warning')
                STORE_FAST              19 (verdict)

 340            LOAD_FAST                7 (warnings)
                LOAD_ATTR               71 (append + NULL|self)
                LOAD_CONST              38 ('scanner_missing_allowed')
                CALL                     1
                POP_TOP
                JUMP_FORWARD            35 (to L18)

 341   L16:     LOAD_FAST               17 (py_failed)
                TO_BOOL
                POP_JUMP_IF_TRUE         9 (to L17)
                NOT_TAKEN
                LOAD_FAST               18 (nd_failed)
                TO_BOOL
                POP_JUMP_IF_FALSE       20 (to L18)
                NOT_TAKEN

 342   L17:     LOAD_CONST              37 ('warning')
                STORE_FAST              19 (verdict)

 343            LOAD_FAST                7 (warnings)
                LOAD_ATTR               71 (append + NULL|self)
                LOAD_CONST              39 ('scanner_subprocess_failed')
                CALL                     1
                POP_TOP

 349   L18:     LOAD_CONST               7 ('verdict')
                LOAD_FAST               19 (verdict)

 350            LOAD_CONST               9 ('ci_mode')
                LOAD_FAST                5 (ci_mode)

 351            LOAD_CONST              10 ('threshold')
                LOAD_FAST                6 (threshold)

 352            LOAD_CONST              11 ('python')
                LOAD_FAST               11 (py)

 353            LOAD_CONST              12 ('node')
                LOAD_FAST               12 (nd)

 354            LOAD_CONST              13 ('warnings')
                LOAD_GLOBAL             75 (list + NULL)
                LOAD_GLOBAL             77 (set + NULL)
                LOAD_FAST                7 (warnings)
                LOAD_GLOBAL             75 (list + NULL)
                LOAD_FAST               11 (py)
                LOAD_ATTR               79 (get + NULL|self)
                LOAD_CONST              13 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L19)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
       L19:     CALL                     1
                BINARY_OP                0 (+)
                LOAD_GLOBAL             75 (list + NULL)
                LOAD_FAST               12 (nd)
                LOAD_ATTR               79 (get + NULL|self)
                LOAD_CONST              13 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L20)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
       L20:     CALL                     1
                BINARY_OP                0 (+)
                CALL                     1
                CALL                     1

 355            LOAD_CONST              15 ('error_code')
                LOAD_FAST               21 (error_code)

 356            LOAD_CONST              17 ('exit_code')
                LOAD_FAST               20 (exit_code)

 357            LOAD_CONST              18 ('generated_at')
                LOAD_GLOBAL             53 (_now_iso + NULL)
                CALL                     0

 348            BUILD_MAP                9
                STORE_FAST              10 (env)

 360            LOAD_FAST                2 (args)
                LOAD_ATTR               54 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       37 (to L21)
                NOT_TAKEN

 361            LOAD_GLOBAL             27 (print + NULL)
                LOAD_GLOBAL             54 (json)
                LOAD_ATTR               56 (dumps)
                PUSH_NULL
                LOAD_FAST               10 (env)
                LOAD_SMALL_INT           2
                LOAD_CONST              19 (True)
                LOAD_CONST              20 (('indent', 'sort_keys'))
                CALL_KW                  3
                CALL                     1
                POP_TOP

 365            LOAD_FAST               20 (exit_code)
                RETURN_VALUE

 363   L21:     LOAD_GLOBAL             59 (_print_summary + NULL)
                LOAD_FAST               10 (env)
                CALL                     1
                POP_TOP

 365            LOAD_FAST               20 (exit_code)
                RETURN_VALUE

  --   L22:     PUSH_EXC_INFO

 252            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L31)
                NOT_TAKEN
                STORE_FAST               3 (e)

 253   L23:     LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                LOAD_CONST              40 ((0, None))
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE        3 (to L24)
                NOT_TAKEN
                LOAD_SMALL_INT           2
                JUMP_FORWARD            30 (to L28)
       L24:     LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L27)
       L25:     NOT_TAKEN
       L26:     POP_TOP
                LOAD_SMALL_INT           0
       L27:     CALL                     1
       L28:     SWAP                     2
       L29:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RETURN_VALUE

  --   L30:     LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 252   L31:     RERAISE                  0

  --   L32:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L33:     PUSH_EXC_INFO

 270            LOAD_GLOBAL             42 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      170 (to L38)
                NOT_TAKEN
                STORE_FAST               3 (e)

 271   L34:     LOAD_GLOBAL             44 (logger)
                LOAD_ATTR               47 (warning + NULL|self)

 272            LOAD_CONST               6 ('security_ci_dependency_gate import error type=')
                LOAD_GLOBAL             49 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR               50 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 271            CALL                     1
                POP_TOP

 275            LOAD_CONST               7 ('verdict')
                LOAD_CONST               8 ('failed')

 276            LOAD_CONST               9 ('ci_mode')
                LOAD_FAST                5 (ci_mode)

 277            LOAD_CONST              10 ('threshold')
                LOAD_FAST                6 (threshold)

 278            LOAD_CONST              11 ('python')
                LOAD_CONST               1 (None)

 279            LOAD_CONST              12 ('node')
                LOAD_CONST               1 (None)

 280            LOAD_CONST              13 ('warnings')
                LOAD_CONST              14 ('import_failed:')
                LOAD_GLOBAL             49 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR               50 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 281            LOAD_CONST              15 ('error_code')
                LOAD_CONST              16 ('import_failed')

 282            LOAD_CONST              17 ('exit_code')
                LOAD_SMALL_INT           1

 283            LOAD_CONST              18 ('generated_at')
                LOAD_GLOBAL             53 (_now_iso + NULL)
                CALL                     0

 274            BUILD_MAP                9
                STORE_FAST              10 (env)

 285            LOAD_FAST                2 (args)
                LOAD_ATTR               54 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       36 (to L35)
                NOT_TAKEN

 286            LOAD_GLOBAL             27 (print + NULL)
                LOAD_GLOBAL             54 (json)
                LOAD_ATTR               56 (dumps)
                PUSH_NULL
                LOAD_FAST               10 (env)
                LOAD_SMALL_INT           2
                LOAD_CONST              19 (True)
                LOAD_CONST              20 (('indent', 'sort_keys'))
                CALL_KW                  3
                CALL                     1
                POP_TOP
                JUMP_FORWARD            11 (to L36)

 288   L35:     LOAD_GLOBAL             59 (_print_summary + NULL)
                LOAD_FAST               10 (env)
                CALL                     1
                POP_TOP

 289   L36:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                LOAD_SMALL_INT           1
                RETURN_VALUE

  --   L37:     LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 270   L38:     RERAISE                  0

  --   L39:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L22 [0]
  L5 to L6 -> L33 [0]
  L22 to L23 -> L32 [1] lasti
  L23 to L25 -> L30 [1] lasti
  L26 to L28 -> L30 [1] lasti
  L28 to L29 -> L32 [1] lasti
  L30 to L32 -> L32 [1] lasti
  L33 to L34 -> L39 [1] lasti
  L34 to L36 -> L37 [1] lasti
  L37 to L39 -> L39 [1] lasti
```
