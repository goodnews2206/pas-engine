# scripts_readiness/memory_diagnostics

- **pyc:** `scripts\__pycache__\memory_diagnostics.cpython-314.pyc`
- **expected source path (absent):** `scripts/memory_diagnostics.py`
- **co_filename (from bytecode):** `scripts\memory_diagnostics.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS144I — Memory-injection diagnostics CLI.

Operator-facing tool that wraps :mod:`app.services.memory.diagnostics`
and writes a structural report describing the memory-runtime health
for one brokerage and / or one call.

Hard contract:

  * either ``--brokerage-id`` or ``--call-id`` is required (or both).
  * the report is **structural only** — never contains memory
    content, prompts, transcripts, evidence values, or formatted
    memory text. The diagnostics module already guarantees this; the
    CLI re-projects the output through a closed allow-list as a
    defence-in-depth.
  * exit code policy:
      0 — health is ``healthy`` / ``inactive`` / ``inactive_or_disabled``
      1 — health is ``failing`` or ``degraded``
      2 — bad CLI arguments
  * the CLI is idempotent and read-only: no DB writes, no migrations.

Usage:
  python scripts/memory_diagnostics.py --brokerage-id brk-1
  python scripts/memory_diagnostics.py --call-id CA_xxx --brokerage-id brk-1
  python scripts/memory_diagnostics.py --brokerage-id brk-1 --since 2026-05-01T00:00:00Z
  python scripts/memory_diagnostics.py --brokerage-id brk-1 --json
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `Path`, `__future__`, `annotations`, `app.services.memory`, `argparse`, `datetime`, `diagnostics`, `json`, `os`, `pathlib`, `sys`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_build_parser`, `_exit_code`, `_print_summary`, `_safe_envelope`, `_safe_summary`, `_write_report`, `main`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS144I — Memory-injection diagnostics CLI.\n\nOperator-facing tool that wraps :mod:`app.services.memory.diagnostics`\nand writes a structural report describing the memory-runtime health\nfor one brokerage and / or one call.\n\nHard contract:\n\n  * either ``--brokerage-id`` or ``--call-id`` is required (or both).\n  * the report is **structural only** — never contains memory\n    content, prompts, transcripts, evidence values, or formatted\n    memory text. The diagnostics module already guarantees this; the\n    CLI re-projects the output through a closed allow-list as a\n    defence-in-depth.\n  * exit code policy:\n      0 — health is ``healthy`` / ``inactive`` / ``inactive_or_disabled``\n      1 — health is ``failing`` or ``degraded``\n      2 — bad CLI arguments\n  * the CLI is idempotent and read-only: no DB writes, no migrations.\n\nUsage:\n  python scripts/memory_diagnostics.py --brokerage-id brk-1\n  python scripts/memory_diagnostics.py --call-id CA_xxx --brokerage-id brk-1\n  python scripts/memory_diagnostics.py --brokerage-id brk-1 --since 2026-05-01T00:00:00Z\n  python scripts/memory_diagnostics.py --brokerage-id brk-1 --json\n'
- 'utf-8'
- 'memory_diagnostics_report.json'
- 'failing'
- 'degraded'
- 'summary'
- 'Optional[Dict[str, Any]]'
- 'return'
- 'Dict[str, Any]'
- 'Project the diagnostics summary through the closed allow-list.'
- 'report'
- 'Project the diagnostics envelope (scope + summary) through the\nsame allow-list discipline.'
- 'argparse.ArgumentParser'
- 'memory_diagnostics'
- 'PAS144I — Operator diagnostics over memory.injection.* events. Tenant-scoped by default; call-scoped when --call-id is supplied.'
- '--brokerage-id'
- 'Tenant identifier. Required when --call-id is omitted; applied as an extra filter when --call-id is supplied.'
- '--call-id'
- 'Specific call SID. When supplied, the diagnostics run in call-scope mode (with optional brokerage filter).'
- '--since'
- 'ISO-8601 lower bound for brokerage-scoped queries.'
- '--limit'
- 'Maximum events to consider for brokerage-scoped queries. Clamped to '
- '--json'
- 'store_true'
- 'Emit the report JSON on stdout in addition to the file.'
- '--output'
- 'Path where the structural report is written. Defaults to ./'
- 'None'
- 'One-line summary for an operator scanning logs.'
- 'health_status'
- 'inactive'
- 'total_events'
- 'attempted'
- 'failed'
- 'skipped'
- 'scope'
- 'brokerage_id'
- 'call_id'
- 'call='
- 'brokerage='
- ' status='
- ' total='
- ' attempted='
- ' failed='
- ' skipped='
- 'path'
- 'str'
- 'payload'
- '  [warn] failed to write report at '
- 'int'
- 'argv'
- 'Optional[List[str]]'
- 'error: at least one of --brokerage-id or --call-id is required'
- 'generated_at'

## Disassembly

```
   0            RESUME                   0

   1            LOAD_CONST               0 ('\nPAS144I — Memory-injection diagnostics CLI.\n\nOperator-facing tool that wraps :mod:`app.services.memory.diagnostics`\nand writes a structural report describing the memory-runtime health\nfor one brokerage and / or one call.\n\nHard contract:\n\n  * either ``--brokerage-id`` or ``--call-id`` is required (or both).\n  * the report is **structural only** — never contains memory\n    content, prompts, transcripts, evidence values, or formatted\n    memory text. The diagnostics module already guarantees this; the\n    CLI re-projects the output through a closed allow-list as a\n    defence-in-depth.\n  * exit code policy:\n      0 — health is ``healthy`` / ``inactive`` / ``inactive_or_disabled``\n      1 — health is ``failing`` or ``degraded``\n      2 — bad CLI arguments\n  * the CLI is idempotent and read-only: no DB writes, no migrations.\n\nUsage:\n  python scripts/memory_diagnostics.py --brokerage-id brk-1\n  python scripts/memory_diagnostics.py --call-id CA_xxx --brokerage-id brk-1\n  python scripts/memory_diagnostics.py --brokerage-id brk-1 --since 2026-05-01T00:00:00Z\n  python scripts/memory_diagnostics.py --brokerage-id brk-1 --json\n')
                STORE_NAME               0 (__doc__)

  29            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('annotations',))
                IMPORT_NAME              1 (__future__)
                IMPORT_FROM              2 (annotations)
                STORE_NAME               2 (annotations)
                POP_TOP

  31            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              3 (argparse)
                STORE_NAME               3 (argparse)

  32            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              4 (json)
                STORE_NAME               4 (json)

  33            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              5 (os)
                STORE_NAME               5 (os)

  34            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              6 (sys)
                STORE_NAME               6 (sys)

  35            LOAD_SMALL_INT           0
                LOAD_CONST               3 (('datetime', 'timezone'))
                IMPORT_NAME              7 (datetime)
                IMPORT_FROM              7 (datetime)
                STORE_NAME               7 (datetime)
                IMPORT_FROM              8 (timezone)
                STORE_NAME               8 (timezone)
                POP_TOP

  36            LOAD_SMALL_INT           0
                LOAD_CONST               4 (('Path',))
                IMPORT_NAME              9 (pathlib)
                IMPORT_FROM             10 (Path)
                STORE_NAME              10 (Path)
                POP_TOP

  37            LOAD_SMALL_INT           0
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

  41            LOAD_NAME                6 (sys)
                LOAD_ATTR               32 (stdout)
                LOAD_NAME                6 (sys)
                LOAD_ATTR               34 (stderr)
                BUILD_TUPLE              2
                GET_ITER
        L1:     FOR_ITER                22 (to L4)
                STORE_NAME              18 (_stream)

  42            NOP

  43    L2:     LOAD_NAME               18 (_stream)
                LOAD_ATTR               39 (reconfigure + NULL|self)
                LOAD_CONST               6 ('utf-8')
                LOAD_CONST               7 (('encoding',))
                CALL_KW                  1
                POP_TOP
        L3:     JUMP_BACKWARD           24 (to L1)

  41    L4:     END_FOR
                POP_ITER

  48            LOAD_NAME                5 (os)
                LOAD_ATTR               42 (path)
                LOAD_ATTR               45 (abspath + NULL|self)
                LOAD_NAME                5 (os)
                LOAD_ATTR               42 (path)
                LOAD_ATTR               47 (join + NULL|self)
                LOAD_NAME                5 (os)
                LOAD_ATTR               42 (path)
                LOAD_ATTR               49 (dirname + NULL|self)
                LOAD_NAME               25 (__file__)
                CALL                     1
                LOAD_CONST               8 ('..')
                CALL                     2
                CALL                     1
                STORE_NAME              26 (_REPO_ROOT)

  49            LOAD_NAME               26 (_REPO_ROOT)
                LOAD_NAME                6 (sys)
                LOAD_ATTR               42 (path)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       29 (to L5)
                NOT_TAKEN

  50            LOAD_NAME                6 (sys)
                LOAD_ATTR               42 (path)
                LOAD_ATTR               55 (insert + NULL|self)
                LOAD_SMALL_INT           0
                LOAD_NAME               26 (_REPO_ROOT)
                CALL                     2
                POP_TOP

  53    L5:     LOAD_SMALL_INT           0
                LOAD_CONST               9 (('diagnostics',))
                IMPORT_NAME             28 (app.services.memory)
                IMPORT_FROM             29 (diagnostics)
                STORE_NAME              30 (diag_mod)
                POP_TOP

  56            LOAD_CONST              10 ('memory_diagnostics_report.json')
                STORE_NAME              31 (REPORT_FILENAME)

  62            LOAD_CONST              28 (('total_events', 'attempted', 'succeeded', 'failed', 'skipped', 'success_rate', 'failure_rate', 'skip_rate', 'reasons', 'warning_count_total', 'average_memory_count', 'average_formatted_chars', 'calls_touched', 'states_seen', 'severity_breakdown', 'health_status', 'notes'))
                STORE_NAME              32 (_SAFE_SUMMARY_FIELDS)

  83            LOAD_NAME               33 (frozenset)
                PUSH_NULL
                LOAD_CONST              11 ('failing')
                LOAD_CONST              12 ('degraded')
                BUILD_SET                2
                CALL                     1
                STORE_NAME              34 (_NON_ZERO_EXIT_STATUSES)

  86            LOAD_CONST              13 (<code object __annotate__ at 0x0000018C17FA3E10, file "scripts\memory_diagnostics.py", line 86>)
                MAKE_FUNCTION
                LOAD_CONST              14 (<code object _safe_summary at 0x0000018C17F95E60, file "scripts\memory_diagnostics.py", line 86>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              35 (_safe_summary)

  93            LOAD_CONST              15 (<code object __annotate__ at 0x0000018C17FA2F10, file "scripts\memory_diagnostics.py", line 93>)
                MAKE_FUNCTION
                LOAD_CONST              16 (<code object _safe_envelope at 0x0000018C17FF1230, file "scripts\memory_diagnostics.py", line 93>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              36 (_safe_envelope)

 107            LOAD_CONST              17 (<code object __annotate__ at 0x0000018C17FA3960, file "scripts\memory_diagnostics.py", line 107>)
                MAKE_FUNCTION
                LOAD_CONST              18 (<code object _build_parser at 0x0000018C17EA5000, file "scripts\memory_diagnostics.py", line 107>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              37 (_build_parser)

 162            LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA34B0, file "scripts\memory_diagnostics.py", line 162>)
                MAKE_FUNCTION
                LOAD_CONST              20 (<code object _print_summary at 0x0000018C17F84C80, file "scripts\memory_diagnostics.py", line 162>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              38 (_print_summary)

 181            LOAD_CONST              21 (<code object __annotate__ at 0x0000018C18024C30, file "scripts\memory_diagnostics.py", line 181>)
                MAKE_FUNCTION
                LOAD_CONST              22 (<code object _write_report at 0x0000018C179C3A50, file "scripts\memory_diagnostics.py", line 181>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              39 (_write_report)

 195            LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA3B40, file "scripts\memory_diagnostics.py", line 195>)
                MAKE_FUNCTION
                LOAD_CONST              24 (<code object _exit_code at 0x0000018C17FE1920, file "scripts\memory_diagnostics.py", line 195>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              40 (_exit_code)

 203            LOAD_CONST              29 ((None,))
                LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA2970, file "scripts\memory_diagnostics.py", line 203>)
                MAKE_FUNCTION
                LOAD_CONST              26 (<code object main at 0x0000018C177883D0, file "scripts\memory_diagnostics.py", line 203>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                SET_FUNCTION_ATTRIBUTE   1 (defaults)
                STORE_NAME              41 (main)

 243            LOAD_NAME               42 (__name__)
                LOAD_CONST              27 ('__main__')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       26 (to L6)
                NOT_TAKEN

 244            LOAD_NAME                6 (sys)
                LOAD_ATTR               86 (exit)
                PUSH_NULL
                LOAD_NAME               41 (main)
                PUSH_NULL
                CALL                     0
                CALL                     1
                POP_TOP
                LOAD_CONST               2 (None)
                RETURN_VALUE

 243    L6:     LOAD_CONST               2 (None)
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

  44            LOAD_NAME               20 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L9)
                NOT_TAKEN
                POP_TOP

  45    L8:     POP_EXCEPT
                EXTENDED_ARG             1
                JUMP_BACKWARD          258 (to L1)

  44    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L7 [1]
  L7 to L8 -> L10 [2] lasti
  L9 to L10 -> L10 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "scripts\memory_diagnostics.py", line 86>:
 86           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('summary')
              LOAD_CONST               2 ('Optional[Dict[str, Any]]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _safe_summary at 0x0000018C17F95E60, file "scripts\memory_diagnostics.py", line 86>:
  86           RESUME                   0

  88           LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (summary)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN

  89           BUILD_MAP                0
               RETURN_VALUE

  90   L1:     LOAD_GLOBAL              4 (_SAFE_SUMMARY_FIELDS)
               GET_ITER
               LOAD_FAST_AND_CLEAR      1 (k)
               SWAP                     2
       L2:     BUILD_MAP                0
               SWAP                     2
       L3:     FOR_ITER                28 (to L6)
               STORE_FAST_LOAD_FAST    17 (k, k)
               LOAD_FAST_BORROW         0 (summary)
               CONTAINS_OP              0 (in)
       L4:     POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L3)
       L5:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 16 (k, summary)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_FAST_BORROW         1 (k)
               CALL                     1
               MAP_ADD                  2
               JUMP_BACKWARD           30 (to L3)
       L6:     END_FOR
               POP_ITER
       L7:     SWAP                     2
               STORE_FAST               1 (k)
               RETURN_VALUE

  --   L8:     SWAP                     2
               POP_TOP

  90           SWAP                     2
               STORE_FAST               1 (k)
               RERAISE                  0
ExceptionTable:
  L2 to L4 -> L8 [2]
  L5 to L7 -> L8 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "scripts\memory_diagnostics.py", line 93>:
 93           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('report')
              LOAD_CONST               2 ('Optional[Dict[str, Any]]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _safe_envelope at 0x0000018C17FF1230, file "scripts\memory_diagnostics.py", line 93>:
 93           RESUME                   0

 96           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (report)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

 97           BUILD_MAP                0
              RETURN_VALUE

 98   L1:     BUILD_MAP                0
              STORE_FAST               1 (out)

 99           LOAD_CONST               2 (('scope', 'brokerage_id', 'call_id', 'since', 'limit', 'events_read', 'error'))
              GET_ITER
      L2:     FOR_ITER                21 (to L4)
              STORE_FAST               2 (key)

101           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (key, report)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

102   L3:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (report, key)
              BINARY_OP               26 ([])
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (out, key)
              STORE_SUBSCR
              JUMP_BACKWARD           23 (to L2)

 99   L4:     END_FOR
              POP_ITER

103           LOAD_GLOBAL              5 (_safe_summary + NULL)
              LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               1 ('summary')
              CALL                     1
              CALL                     1
              LOAD_FAST_BORROW         1 (out)
              LOAD_CONST               1 ('summary')
              STORE_SUBSCR

104           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "scripts\memory_diagnostics.py", line 107>:
107           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C17EA5000, file "scripts\memory_diagnostics.py", line 107>:
107           RESUME                   0

108           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

109           LOAD_CONST               0 ('memory_diagnostics')

111           LOAD_CONST               1 ('PAS144I — Operator diagnostics over memory.injection.* events. Tenant-scoped by default; call-scoped when --call-id is supplied.')

108           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

116           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

117           LOAD_CONST               3 ('--brokerage-id')

118           LOAD_CONST               4 (None)

120           LOAD_CONST               5 ('Tenant identifier. Required when --call-id is omitted; applied as an extra filter when --call-id is supplied.')

116           LOAD_CONST               6 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

124           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

125           LOAD_CONST               7 ('--call-id')

126           LOAD_CONST               4 (None)

128           LOAD_CONST               8 ('Specific call SID. When supplied, the diagnostics run in call-scope mode (with optional brokerage filter).')

124           LOAD_CONST               6 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

132           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

133           LOAD_CONST               9 ('--since')

134           LOAD_CONST               4 (None)

135           LOAD_CONST              10 ('ISO-8601 lower bound for brokerage-scoped queries.')

132           LOAD_CONST               6 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

137           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

138           LOAD_CONST              11 ('--limit')

139           LOAD_GLOBAL              6 (int)

140           LOAD_GLOBAL              8 (diag_mod)
              LOAD_ATTR               10 (DEFAULT_BROKERAGE_LIMIT)

142           LOAD_CONST              12 ('Maximum events to consider for brokerage-scoped queries. Clamped to ')

143           LOAD_GLOBAL              8 (diag_mod)
              LOAD_ATTR               12 (MAX_BROKERAGE_LIMIT)
              FORMAT_SIMPLE
              LOAD_CONST              13 ('.')

142           BUILD_STRING             3

137           LOAD_CONST              14 (('type', 'default', 'help'))
              CALL_KW                  4
              POP_TOP

146           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

147           LOAD_CONST              15 ('--json')

148           LOAD_CONST              16 ('store_true')

149           LOAD_CONST              17 ('Emit the report JSON on stdout in addition to the file.')

146           LOAD_CONST              18 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

151           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

152           LOAD_CONST              19 ('--output')

153           LOAD_GLOBAL             14 (REPORT_FILENAME)

155           LOAD_CONST              20 ('Path where the structural report is written. Defaults to ./')

156           LOAD_GLOBAL             14 (REPORT_FILENAME)
              FORMAT_SIMPLE
              LOAD_CONST              13 ('.')

155           BUILD_STRING             3

151           LOAD_CONST               6 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

159           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "scripts\memory_diagnostics.py", line 162>:
162           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C17F84C80, file "scripts\memory_diagnostics.py", line 162>:
162           RESUME                   0

164           LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               1 ('summary')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L1:     STORE_FAST               1 (summary)

165           LOAD_FAST_BORROW         1 (summary)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               2 ('health_status')
              LOAD_CONST               3 ('inactive')
              CALL                     2
              STORE_FAST               2 (status)

166           LOAD_FAST_BORROW         1 (summary)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               4 ('total_events')
              LOAD_SMALL_INT           0
              CALL                     2
              STORE_FAST               3 (total)

167           LOAD_FAST_BORROW         1 (summary)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               5 ('attempted')
              LOAD_SMALL_INT           0
              CALL                     2
              STORE_FAST               4 (attempted)

168           LOAD_FAST_BORROW         1 (summary)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               6 ('failed')
              LOAD_SMALL_INT           0
              CALL                     2
              STORE_FAST               5 (failed)

169           LOAD_FAST_BORROW         1 (summary)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               7 ('skipped')
              LOAD_SMALL_INT           0
              CALL                     2
              STORE_FAST               6 (skipped)

170           LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               8 ('scope')
              LOAD_CONST               9 ('')
              CALL                     2
              STORE_FAST               7 (scope)

171           LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              10 ('brokerage_id')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               9 ('')
      L2:     STORE_FAST               8 (bid)

172           LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              11 ('call_id')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               9 ('')
      L3:     STORE_FAST               9 (cid)

173           LOAD_FAST_BORROW         9 (cid)
              TO_BOOL
              POP_JUMP_IF_FALSE        6 (to L4)
              NOT_TAKEN
              LOAD_CONST              12 ('call=')
              LOAD_FAST_BORROW         9 (cid)
              FORMAT_SIMPLE
              BUILD_STRING             2
              JUMP_FORWARD             4 (to L5)
      L4:     LOAD_CONST              13 ('brokerage=')
              LOAD_FAST_BORROW         8 (bid)
              FORMAT_SIMPLE
              BUILD_STRING             2
      L5:     STORE_FAST              10 (target)

174           LOAD_GLOBAL              3 (print + NULL)

175           LOAD_CONST              14 ('[')
              LOAD_FAST_BORROW         7 (scope)
              FORMAT_SIMPLE
              LOAD_CONST              15 ('] ')
              LOAD_FAST_BORROW        10 (target)
              FORMAT_SIMPLE
              LOAD_CONST              16 (' status=')
              LOAD_FAST_BORROW         2 (status)
              FORMAT_SIMPLE
              LOAD_CONST              17 (' total=')

176           LOAD_FAST_BORROW         3 (total)
              FORMAT_SIMPLE
              LOAD_CONST              18 (' attempted=')
              LOAD_FAST_BORROW         4 (attempted)
              FORMAT_SIMPLE
              LOAD_CONST              19 (' failed=')

177           LOAD_FAST_BORROW         5 (failed)
              FORMAT_SIMPLE
              LOAD_CONST              20 (' skipped=')
              LOAD_FAST_BORROW         6 (skipped)
              FORMAT_SIMPLE

175           BUILD_STRING            14

174           CALL                     1
              POP_TOP
              LOAD_CONST              21 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "scripts\memory_diagnostics.py", line 181>:
181           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('path')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('payload')
              LOAD_CONST               4 ('Dict[str, Any]')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('None')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _write_report at 0x0000018C179C3A50, file "scripts\memory_diagnostics.py", line 181>:
 181           RESUME                   0

 182           NOP

 183   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

 184           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

 185           LOAD_CONST               3 ('utf-8')

 183           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 187           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

 188   L4:     LOAD_GLOBAL             11 (print + NULL)

 189           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

 190           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

 189           BUILD_STRING             4

 191           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

 188           LOAD_CONST               7 (('file',))
               CALL_KW                  2
               POP_TOP
       L5:     POP_EXCEPT
               LOAD_CONST               8 (None)
               STORE_FAST               2 (e)
               DELETE_FAST              2 (e)
               LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               8 (None)
               STORE_FAST               2 (e)
               DELETE_FAST              2 (e)
               RERAISE                  1

 187   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "scripts\memory_diagnostics.py", line 195>:
195           RESUME                   0
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
              LOAD_CONST               4 ('int')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _exit_code at 0x0000018C17FE1920, file "scripts\memory_diagnostics.py", line 195>:
195           RESUME                   0

196           LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               0 ('summary')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L1:     STORE_FAST               1 (summary)

197           LOAD_FAST_BORROW         1 (summary)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               1 ('health_status')
              LOAD_CONST               2 ('inactive')
              CALL                     2
              STORE_FAST               2 (status)

198           LOAD_FAST_BORROW         2 (status)
              LOAD_GLOBAL              2 (_NON_ZERO_EXIT_STATUSES)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

199           LOAD_SMALL_INT           1
              RETURN_VALUE

200   L2:     LOAD_SMALL_INT           0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "scripts\memory_diagnostics.py", line 203>:
203           RESUME                   0
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

Disassembly of <code object main at 0x0000018C177883D0, file "scripts\memory_diagnostics.py", line 203>:
 203            RESUME                   0

 204            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 205            NOP

 206    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 210    L2:     LOAD_FAST                2 (args)
                LOAD_ATTR               10 (brokerage_id)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L3)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L3:     LOAD_ATTR               13 (strip + NULL|self)
                CALL                     0
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               1 (None)
        L4:     STORE_FAST               4 (brokerage_id)

 211            LOAD_FAST                2 (args)
                LOAD_ATTR               14 (call_id)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L5:     LOAD_ATTR               13 (strip + NULL|self)
                CALL                     0
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               1 (None)
        L6:     STORE_FAST               5 (call_id)

 213            LOAD_FAST                4 (brokerage_id)
                TO_BOOL
                POP_JUMP_IF_TRUE        38 (to L7)
                NOT_TAKEN
                LOAD_FAST                5 (call_id)
                TO_BOOL
                POP_JUMP_IF_TRUE        30 (to L7)
                NOT_TAKEN

 214            LOAD_GLOBAL             17 (print + NULL)

 215            LOAD_CONST               3 ('error: at least one of --brokerage-id or --call-id is required')

 216            LOAD_GLOBAL             18 (sys)
                LOAD_ATTR               20 (stderr)

 214            LOAD_CONST               4 (('file',))
                CALL_KW                  2
                POP_TOP

 218            LOAD_SMALL_INT           2
                RETURN_VALUE

 220    L7:     LOAD_FAST                5 (call_id)
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L8)
                NOT_TAKEN

 221            LOAD_GLOBAL             22 (diag_mod)
                LOAD_ATTR               24 (memory_injection_health_for_call)
                PUSH_NULL

 222            LOAD_FAST_LOAD_FAST     84 (call_id, brokerage_id)

 221            LOAD_CONST               5 (('brokerage_id',))
                CALL_KW                  2
                STORE_FAST               6 (raw)
                JUMP_FORWARD            44 (to L9)

 225    L8:     LOAD_GLOBAL             22 (diag_mod)
                LOAD_ATTR               26 (memory_injection_health_for_brokerage)
                PUSH_NULL

 226            LOAD_FAST_LOAD_FAST     66 (brokerage_id, args)
                LOAD_ATTR               28 (since)
                LOAD_FAST                2 (args)
                LOAD_ATTR               30 (limit)

 225            LOAD_CONST               6 (('since', 'limit'))
                CALL_KW                  3
                STORE_FAST               6 (raw)

 229    L9:     LOAD_GLOBAL             33 (_safe_envelope + NULL)
                LOAD_FAST                6 (raw)
                CALL                     1
                STORE_FAST               7 (safe)

 230            LOAD_FAST                7 (safe)
                LOAD_ATTR               35 (setdefault + NULL|self)
                LOAD_CONST               7 ('generated_at')
                LOAD_GLOBAL             36 (datetime)
                LOAD_ATTR               38 (now)
                PUSH_NULL
                LOAD_GLOBAL             40 (timezone)
                LOAD_ATTR               42 (utc)
                CALL                     1
                LOAD_ATTR               45 (isoformat + NULL|self)
                CALL                     0
                CALL                     2
                POP_TOP

 232            LOAD_GLOBAL             47 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               48 (output)
                LOAD_FAST                7 (safe)
                CALL                     2
                POP_TOP

 233            LOAD_GLOBAL             51 (_print_summary + NULL)
                LOAD_FAST                7 (safe)
                CALL                     1
                POP_TOP

 235            LOAD_FAST                2 (args)
                LOAD_ATTR               52 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L10)
                NOT_TAKEN

 238            LOAD_GLOBAL             17 (print + NULL)
                LOAD_GLOBAL             52 (json)
                LOAD_ATTR               54 (dumps)
                PUSH_NULL
                LOAD_FAST                7 (safe)
                LOAD_SMALL_INT           2
                LOAD_CONST               8 (True)
                LOAD_CONST               9 (('indent', 'sort_keys'))
                CALL_KW                  3
                CALL                     1
                POP_TOP

 240   L10:     LOAD_GLOBAL             57 (_exit_code + NULL)
                LOAD_FAST                7 (safe)
                CALL                     1
                RETURN_VALUE

  --   L11:     PUSH_EXC_INFO

 207            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L20)
                NOT_TAKEN
                STORE_FAST               3 (e)

 208   L12:     LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                LOAD_CONST              10 ((0, None))
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE        3 (to L13)
                NOT_TAKEN
                LOAD_SMALL_INT           2
                JUMP_FORWARD            30 (to L17)
       L13:     LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L16)
       L14:     NOT_TAKEN
       L15:     POP_TOP
                LOAD_SMALL_INT           0
       L16:     CALL                     1
       L17:     SWAP                     2
       L18:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RETURN_VALUE

  --   L19:     LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 207   L20:     RERAISE                  0

  --   L21:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L11 [0]
  L11 to L12 -> L21 [1] lasti
  L12 to L14 -> L19 [1] lasti
  L15 to L17 -> L19 [1] lasti
  L17 to L18 -> L21 [1] lasti
  L19 to L21 -> L21 [1] lasti
```
