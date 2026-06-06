# scripts_readiness/memory_impact_report

- **pyc:** `scripts\__pycache__\memory_impact_report.cpython-314.pyc`
- **expected source path (absent):** `scripts/memory_impact_report.py`
- **co_filename (from bytecode):** `scripts\memory_impact_report.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS144J — Memory-injection impact report CLI.

Wraps :mod:`app.services.memory.impact` and writes a structural
``memory_impact_report.json`` describing how the memory-injected
cohort compares against the no-memory baseline for one tenant.

Hard contract:
  * ``--brokerage-id`` is required.
  * the report is structural only — never carries memory content,
    prompts, transcripts, evidence values, or any payload field
    other than the documented summary keys.
  * exit code policy:
      0 — rollout_recommendation in {hold, expand_cautiously}
      1 — rollout_recommendation in {investigate, disable_for_now}
      2 — bad CLI arguments

Usage:
  python scripts/memory_impact_report.py --brokerage-id brk-1
  python scripts/memory_impact_report.py --brokerage-id brk-1 \
        --since 2026-05-01T00:00:00Z --limit 2000
  python scripts/memory_impact_report.py --brokerage-id brk-1 --json
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `Path`, `__future__`, `annotations`, `app.services.memory`, `argparse`, `datetime`, `impact`, `json`, `os`, `pathlib`, `sys`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_build_parser`, `_exit_code`, `_print_summary`, `_safe_envelope`, `_safe_summary`, `_write_report`, `main`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS144J — Memory-injection impact report CLI.\n\nWraps :mod:`app.services.memory.impact` and writes a structural\n``memory_impact_report.json`` describing how the memory-injected\ncohort compares against the no-memory baseline for one tenant.\n\nHard contract:\n  * ``--brokerage-id`` is required.\n  * the report is structural only — never carries memory content,\n    prompts, transcripts, evidence values, or any payload field\n    other than the documented summary keys.\n  * exit code policy:\n      0 — rollout_recommendation in {hold, expand_cautiously}\n      1 — rollout_recommendation in {investigate, disable_for_now}\n      2 — bad CLI arguments\n\nUsage:\n  python scripts/memory_impact_report.py --brokerage-id brk-1\n  python scripts/memory_impact_report.py --brokerage-id brk-1 \\\n        --since 2026-05-01T00:00:00Z --limit 2000\n  python scripts/memory_impact_report.py --brokerage-id brk-1 --json\n'
- 'utf-8'
- 'memory_impact_report.json'
- 'investigate'
- 'disable_for_now'
- 'summary'
- 'Optional[Dict[str, Any]]'
- 'return'
- 'Dict[str, Any]'
- 'report'
- 'scope'
- 'argparse.ArgumentParser'
- 'memory_impact_report'
- 'PAS144J — Compare memory-injected calls vs the no-memory baseline for one tenant. Tenant-scoped only.'
- '--brokerage-id'
- 'Required tenant identifier. There is no unscoped mode.'
- '--since'
- 'ISO-8601 lower bound on event timestamps.'
- '--limit'
- 'Maximum events to consider. Clamped to '
- '--json'
- 'store_true'
- 'Emit the report JSON on stdout in addition to the file.'
- '--output'
- 'Where to write the structural report. Defaults to ./'
- 'None'
- 'rollout_recommendation'
- 'hold'
- 'health_status'
- 'inconclusive'
- 'total_calls'
- 'memory_succeeded_calls'
- 'non_memory_calls'
- 'booking_rate_with_memory'
- 'booking_rate_without_memory'
- 'provider_failure_rate_with_memory'
- 'brokerage_id'
- '[brokerage='
- '] recommendation='
- ' status='
- ' total_calls='
- ' with_memory='
- ' without_memory='
- ' booking_with='
- '.4f'
- ' booking_without='
- ' failure_with='
- 'path'
- 'str'
- 'payload'
- '  [warn] failed to write report at '
- 'int'
- 'argv'
- 'Optional[List[str]]'
- 'error: --brokerage-id must be a non-empty string'
- 'generated_at'

## Disassembly

```
   0            RESUME                   0

   1            LOAD_CONST               0 ('\nPAS144J — Memory-injection impact report CLI.\n\nWraps :mod:`app.services.memory.impact` and writes a structural\n``memory_impact_report.json`` describing how the memory-injected\ncohort compares against the no-memory baseline for one tenant.\n\nHard contract:\n  * ``--brokerage-id`` is required.\n  * the report is structural only — never carries memory content,\n    prompts, transcripts, evidence values, or any payload field\n    other than the documented summary keys.\n  * exit code policy:\n      0 — rollout_recommendation in {hold, expand_cautiously}\n      1 — rollout_recommendation in {investigate, disable_for_now}\n      2 — bad CLI arguments\n\nUsage:\n  python scripts/memory_impact_report.py --brokerage-id brk-1\n  python scripts/memory_impact_report.py --brokerage-id brk-1 \\\n        --since 2026-05-01T00:00:00Z --limit 2000\n  python scripts/memory_impact_report.py --brokerage-id brk-1 --json\n')
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
                LOAD_CONST               3 (('datetime', 'timezone'))
                IMPORT_NAME              7 (datetime)
                IMPORT_FROM              7 (datetime)
                STORE_NAME               7 (datetime)
                IMPORT_FROM              8 (timezone)
                STORE_NAME               8 (timezone)
                POP_TOP

  32            LOAD_SMALL_INT           0
                LOAD_CONST               4 (('Path',))
                IMPORT_NAME              9 (pathlib)
                IMPORT_FROM             10 (Path)
                STORE_NAME              10 (Path)
                POP_TOP

  33            LOAD_SMALL_INT           0
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

  36            LOAD_NAME                6 (sys)
                LOAD_ATTR               32 (stdout)
                LOAD_NAME                6 (sys)
                LOAD_ATTR               34 (stderr)
                BUILD_TUPLE              2
                GET_ITER
        L1:     FOR_ITER                22 (to L4)
                STORE_NAME              18 (_stream)

  37            NOP

  38    L2:     LOAD_NAME               18 (_stream)
                LOAD_ATTR               39 (reconfigure + NULL|self)
                LOAD_CONST               6 ('utf-8')
                LOAD_CONST               7 (('encoding',))
                CALL_KW                  1
                POP_TOP
        L3:     JUMP_BACKWARD           24 (to L1)

  36    L4:     END_FOR
                POP_ITER

  43            LOAD_NAME                5 (os)
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

  44            LOAD_NAME               26 (_REPO_ROOT)
                LOAD_NAME                6 (sys)
                LOAD_ATTR               42 (path)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       29 (to L5)
                NOT_TAKEN

  45            LOAD_NAME                6 (sys)
                LOAD_ATTR               42 (path)
                LOAD_ATTR               55 (insert + NULL|self)
                LOAD_SMALL_INT           0
                LOAD_NAME               26 (_REPO_ROOT)
                CALL                     2
                POP_TOP

  48    L5:     LOAD_SMALL_INT           0
                LOAD_CONST               9 (('impact',))
                IMPORT_NAME             28 (app.services.memory)
                IMPORT_FROM             29 (impact)
                STORE_NAME              30 (impact_mod)
                POP_TOP

  51            LOAD_CONST              10 ('memory_impact_report.json')
                STORE_NAME              31 (REPORT_FILENAME)

  57            LOAD_CONST              28 (('total_calls', 'memory_attempted_calls', 'memory_succeeded_calls', 'non_memory_calls', 'booked_with_memory', 'booked_without_memory', 'callback_with_memory', 'callback_without_memory', 'failed_with_memory', 'failed_without_memory', 'booking_rate_with_memory', 'booking_rate_without_memory', 'callback_rate_with_memory', 'callback_rate_without_memory', 'objection_rate_with_memory', 'objection_rate_without_memory', 'provider_failure_rate_with_memory', 'provider_failure_rate_without_memory', 'lift_booking_rate', 'lift_callback_rate', 'health_status', 'rollout_recommendation', 'notes'))
                STORE_NAME              32 (_SAFE_SUMMARY_FIELDS)

  83            LOAD_NAME               33 (frozenset)
                PUSH_NULL
                LOAD_CONST              11 ('investigate')
                LOAD_CONST              12 ('disable_for_now')
                BUILD_SET                2
                CALL                     1
                STORE_NAME              34 (_NON_ZERO_EXIT_RECOMMENDATIONS)

  86            LOAD_CONST              13 (<code object __annotate__ at 0x0000018C17FA3A50, file "scripts\memory_impact_report.py", line 86>)
                MAKE_FUNCTION
                LOAD_CONST              14 (<code object _safe_summary at 0x0000018C17F96140, file "scripts\memory_impact_report.py", line 86>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              35 (_safe_summary)

  92            LOAD_CONST              15 (<code object __annotate__ at 0x0000018C17FA3E10, file "scripts\memory_impact_report.py", line 92>)
                MAKE_FUNCTION
                LOAD_CONST              16 (<code object _safe_envelope at 0x0000018C17FF13B0, file "scripts\memory_impact_report.py", line 92>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              36 (_safe_envelope)

 104            LOAD_CONST              17 (<code object __annotate__ at 0x0000018C17FA2F10, file "scripts\memory_impact_report.py", line 104>)
                MAKE_FUNCTION
                LOAD_CONST              18 (<code object _build_parser at 0x0000018C17D77E00, file "scripts\memory_impact_report.py", line 104>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              37 (_build_parser)

 147            LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA3960, file "scripts\memory_impact_report.py", line 147>)
                MAKE_FUNCTION
                LOAD_CONST              20 (<code object _print_summary at 0x0000018C17D7D240, file "scripts\memory_impact_report.py", line 147>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              38 (_print_summary)

 166            LOAD_CONST              21 (<code object __annotate__ at 0x0000018C18025F30, file "scripts\memory_impact_report.py", line 166>)
                MAKE_FUNCTION
                LOAD_CONST              22 (<code object _write_report at 0x0000018C179C3A50, file "scripts\memory_impact_report.py", line 166>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              39 (_write_report)

 180            LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA34B0, file "scripts\memory_impact_report.py", line 180>)
                MAKE_FUNCTION
                LOAD_CONST              24 (<code object _exit_code at 0x0000018C17FE1290, file "scripts\memory_impact_report.py", line 180>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              40 (_exit_code)

 188            LOAD_CONST              29 ((None,))
                LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA3B40, file "scripts\memory_impact_report.py", line 188>)
                MAKE_FUNCTION
                LOAD_CONST              26 (<code object main at 0x0000018C17EF9A30, file "scripts\memory_impact_report.py", line 188>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                SET_FUNCTION_ATTRIBUTE   1 (defaults)
                STORE_NAME              41 (main)

 219            LOAD_NAME               42 (__name__)
                LOAD_CONST              27 ('__main__')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       26 (to L6)
                NOT_TAKEN

 220            LOAD_NAME                6 (sys)
                LOAD_ATTR               86 (exit)
                PUSH_NULL
                LOAD_NAME               41 (main)
                PUSH_NULL
                CALL                     0
                CALL                     1
                POP_TOP
                LOAD_CONST               2 (None)
                RETURN_VALUE

 219    L6:     LOAD_CONST               2 (None)
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

  39            LOAD_NAME               20 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L9)
                NOT_TAKEN
                POP_TOP

  40    L8:     POP_EXCEPT
                EXTENDED_ARG             1
                JUMP_BACKWARD          258 (to L1)

  39    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L7 [1]
  L7 to L8 -> L10 [2] lasti
  L9 to L10 -> L10 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "scripts\memory_impact_report.py", line 86>:
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

Disassembly of <code object _safe_summary at 0x0000018C17F96140, file "scripts\memory_impact_report.py", line 86>:
  86           RESUME                   0

  87           LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (summary)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN

  88           BUILD_MAP                0
               RETURN_VALUE

  89   L1:     LOAD_GLOBAL              4 (_SAFE_SUMMARY_FIELDS)
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

  89           SWAP                     2
               STORE_FAST               1 (k)
               RERAISE                  0
ExceptionTable:
  L2 to L4 -> L8 [2]
  L5 to L7 -> L8 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "scripts\memory_impact_report.py", line 92>:
 92           RESUME                   0
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

Disassembly of <code object _safe_envelope at 0x0000018C17FF13B0, file "scripts\memory_impact_report.py", line 92>:
 92           RESUME                   0

 93           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (report)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

 94           BUILD_MAP                0
              RETURN_VALUE

 95   L1:     BUILD_MAP                0
              STORE_FAST               1 (out)

 96           LOAD_CONST               2 (('scope', 'brokerage_id', 'since', 'limit', 'events_read', 'error'))
              GET_ITER
      L2:     FOR_ITER                21 (to L4)
              STORE_FAST               2 (key)

 98           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (key, report)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

 99   L3:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (report, key)
              BINARY_OP               26 ([])
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (out, key)
              STORE_SUBSCR
              JUMP_BACKWARD           23 (to L2)

 96   L4:     END_FOR
              POP_ITER

100           LOAD_GLOBAL              5 (_safe_summary + NULL)
              LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               1 ('summary')
              CALL                     1
              CALL                     1
              LOAD_FAST_BORROW         1 (out)
              LOAD_CONST               1 ('summary')
              STORE_SUBSCR

101           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "scripts\memory_impact_report.py", line 104>:
104           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C17D77E00, file "scripts\memory_impact_report.py", line 104>:
104           RESUME                   0

105           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

106           LOAD_CONST               0 ('memory_impact_report')

108           LOAD_CONST               1 ('PAS144J — Compare memory-injected calls vs the no-memory baseline for one tenant. Tenant-scoped only.')

105           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

112           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

113           LOAD_CONST               3 ('--brokerage-id')

114           LOAD_CONST               4 (True)

115           LOAD_CONST               5 ('Required tenant identifier. There is no unscoped mode.')

112           LOAD_CONST               6 (('required', 'help'))
              CALL_KW                  3
              POP_TOP

117           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

118           LOAD_CONST               7 ('--since')

119           LOAD_CONST               8 (None)

120           LOAD_CONST               9 ('ISO-8601 lower bound on event timestamps.')

117           LOAD_CONST              10 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

122           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

123           LOAD_CONST              11 ('--limit')

124           LOAD_GLOBAL              6 (int)

125           LOAD_GLOBAL              8 (impact_mod)
              LOAD_ATTR               10 (DEFAULT_BROKERAGE_LIMIT)

127           LOAD_CONST              12 ('Maximum events to consider. Clamped to ')

128           LOAD_GLOBAL              8 (impact_mod)
              LOAD_ATTR               12 (MAX_BROKERAGE_LIMIT)
              FORMAT_SIMPLE
              LOAD_CONST              13 ('.')

127           BUILD_STRING             3

122           LOAD_CONST              14 (('type', 'default', 'help'))
              CALL_KW                  4
              POP_TOP

131           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

132           LOAD_CONST              15 ('--json')

133           LOAD_CONST              16 ('store_true')

134           LOAD_CONST              17 ('Emit the report JSON on stdout in addition to the file.')

131           LOAD_CONST              18 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

136           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

137           LOAD_CONST              19 ('--output')

138           LOAD_GLOBAL             14 (REPORT_FILENAME)

140           LOAD_CONST              20 ('Where to write the structural report. Defaults to ./')

141           LOAD_GLOBAL             14 (REPORT_FILENAME)
              FORMAT_SIMPLE
              LOAD_CONST              13 ('.')

140           BUILD_STRING             3

136           LOAD_CONST              10 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

144           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "scripts\memory_impact_report.py", line 147>:
147           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C17D7D240, file "scripts\memory_impact_report.py", line 147>:
147           RESUME                   0

148           LOAD_FAST_BORROW         0 (report)
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

149           LOAD_FAST_BORROW         1 (summary)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               1 ('rollout_recommendation')
              LOAD_CONST               2 ('hold')
              CALL                     2
              STORE_FAST               2 (rec)

150           LOAD_FAST_BORROW         1 (summary)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               3 ('health_status')
              LOAD_CONST               4 ('inconclusive')
              CALL                     2
              STORE_FAST               3 (status)

151           LOAD_FAST_BORROW         1 (summary)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               5 ('total_calls')
              LOAD_SMALL_INT           0
              CALL                     2
              STORE_FAST               4 (total)

152           LOAD_FAST_BORROW         1 (summary)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               6 ('memory_succeeded_calls')
              LOAD_SMALL_INT           0
              CALL                     2
              STORE_FAST               5 (with_n)

153           LOAD_FAST_BORROW         1 (summary)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               7 ('non_memory_calls')
              LOAD_SMALL_INT           0
              CALL                     2
              STORE_FAST               6 (without_n)

154           LOAD_FAST_BORROW         1 (summary)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               8 ('booking_rate_with_memory')
              LOAD_CONST               9 (0.0)
              CALL                     2
              STORE_FAST               7 (book_with)

155           LOAD_FAST_BORROW         1 (summary)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              10 ('booking_rate_without_memory')
              LOAD_CONST               9 (0.0)
              CALL                     2
              STORE_FAST               8 (book_without)

156           LOAD_FAST_BORROW         1 (summary)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              11 ('provider_failure_rate_with_memory')
              LOAD_CONST               9 (0.0)
              CALL                     2
              STORE_FAST               9 (fail_with)

157           LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              12 ('brokerage_id')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST              13 ('')
      L2:     STORE_FAST              10 (bid)

158           LOAD_GLOBAL              3 (print + NULL)

159           LOAD_CONST              14 ('[brokerage=')
              LOAD_FAST_BORROW        10 (bid)
              FORMAT_SIMPLE
              LOAD_CONST              15 ('] recommendation=')
              LOAD_FAST_BORROW         2 (rec)
              FORMAT_SIMPLE
              LOAD_CONST              16 (' status=')
              LOAD_FAST_BORROW         3 (status)
              FORMAT_SIMPLE
              LOAD_CONST              17 (' total_calls=')

160           LOAD_FAST_BORROW         4 (total)
              FORMAT_SIMPLE
              LOAD_CONST              18 (' with_memory=')
              LOAD_FAST_BORROW         5 (with_n)
              FORMAT_SIMPLE
              LOAD_CONST              19 (' without_memory=')
              LOAD_FAST_BORROW         6 (without_n)
              FORMAT_SIMPLE
              LOAD_CONST              20 (' booking_with=')

161           LOAD_FAST_BORROW         7 (book_with)
              LOAD_CONST              21 ('.4f')
              FORMAT_WITH_SPEC
              LOAD_CONST              22 (' booking_without=')
              LOAD_FAST_BORROW         8 (book_without)
              LOAD_CONST              21 ('.4f')
              FORMAT_WITH_SPEC
              LOAD_CONST              23 (' failure_with=')

162           LOAD_FAST_BORROW         9 (fail_with)
              LOAD_CONST              21 ('.4f')
              FORMAT_WITH_SPEC

159           BUILD_STRING            18

158           CALL                     1
              POP_TOP
              LOAD_CONST              24 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025F30, file "scripts\memory_impact_report.py", line 166>:
166           RESUME                   0
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

Disassembly of <code object _write_report at 0x0000018C179C3A50, file "scripts\memory_impact_report.py", line 166>:
 166           RESUME                   0

 167           NOP

 168   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

 169           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

 170           LOAD_CONST               3 ('utf-8')

 168           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 172           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

 173   L4:     LOAD_GLOBAL             11 (print + NULL)

 174           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

 175           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

 174           BUILD_STRING             4

 176           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

 173           LOAD_CONST               7 (('file',))
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

 172   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "scripts\memory_impact_report.py", line 180>:
180           RESUME                   0
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

Disassembly of <code object _exit_code at 0x0000018C17FE1290, file "scripts\memory_impact_report.py", line 180>:
180           RESUME                   0

181           LOAD_FAST_BORROW         0 (report)
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

182           LOAD_FAST_BORROW         1 (summary)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               1 ('rollout_recommendation')
              LOAD_CONST               2 ('hold')
              CALL                     2
              STORE_FAST               2 (rec)

183           LOAD_FAST_BORROW         2 (rec)
              LOAD_GLOBAL              2 (_NON_ZERO_EXIT_RECOMMENDATIONS)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

184           LOAD_SMALL_INT           1
              RETURN_VALUE

185   L2:     LOAD_SMALL_INT           0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "scripts\memory_impact_report.py", line 188>:
188           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17EF9A30, file "scripts\memory_impact_report.py", line 188>:
 188            RESUME                   0

 189            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 190            NOP

 191    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 195    L2:     LOAD_FAST                2 (args)
                LOAD_ATTR               10 (brokerage_id)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L3)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L3:     LOAD_ATTR               13 (strip + NULL|self)
                CALL                     0
                STORE_FAST               4 (bid)

 196            LOAD_FAST                4 (bid)
                TO_BOOL
                POP_JUMP_IF_TRUE        30 (to L4)
                NOT_TAKEN

 197            LOAD_GLOBAL             15 (print + NULL)

 198            LOAD_CONST               3 ('error: --brokerage-id must be a non-empty string')

 199            LOAD_GLOBAL             16 (sys)
                LOAD_ATTR               18 (stderr)

 197            LOAD_CONST               4 (('file',))
                CALL_KW                  2
                POP_TOP

 201            LOAD_SMALL_INT           2
                RETURN_VALUE

 203    L4:     LOAD_GLOBAL             20 (impact_mod)
                LOAD_ATTR               22 (memory_impact_for_brokerage)
                PUSH_NULL

 204            LOAD_FAST_LOAD_FAST     66 (bid, args)
                LOAD_ATTR               24 (since)
                LOAD_FAST                2 (args)
                LOAD_ATTR               26 (limit)

 203            LOAD_CONST               5 (('since', 'limit'))
                CALL_KW                  3
                STORE_FAST               5 (raw)

 207            LOAD_GLOBAL             29 (_safe_envelope + NULL)
                LOAD_FAST                5 (raw)
                CALL                     1
                STORE_FAST               6 (safe)

 208            LOAD_FAST                6 (safe)
                LOAD_ATTR               31 (setdefault + NULL|self)
                LOAD_CONST               6 ('generated_at')
                LOAD_GLOBAL             32 (datetime)
                LOAD_ATTR               34 (now)
                PUSH_NULL
                LOAD_GLOBAL             36 (timezone)
                LOAD_ATTR               38 (utc)
                CALL                     1
                LOAD_ATTR               41 (isoformat + NULL|self)
                CALL                     0
                CALL                     2
                POP_TOP

 210            LOAD_GLOBAL             43 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               44 (output)
                LOAD_FAST                6 (safe)
                CALL                     2
                POP_TOP

 211            LOAD_GLOBAL             47 (_print_summary + NULL)
                LOAD_FAST                6 (safe)
                CALL                     1
                POP_TOP

 213            LOAD_FAST                2 (args)
                LOAD_ATTR               48 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L5)
                NOT_TAKEN

 214            LOAD_GLOBAL             15 (print + NULL)
                LOAD_GLOBAL             48 (json)
                LOAD_ATTR               50 (dumps)
                PUSH_NULL
                LOAD_FAST                6 (safe)
                LOAD_SMALL_INT           2
                LOAD_CONST               7 (True)
                LOAD_CONST               8 (('indent', 'sort_keys'))
                CALL_KW                  3
                CALL                     1
                POP_TOP

 216    L5:     LOAD_GLOBAL             53 (_exit_code + NULL)
                LOAD_FAST                6 (safe)
                CALL                     1
                RETURN_VALUE

  --    L6:     PUSH_EXC_INFO

 192            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L15)
                NOT_TAKEN
                STORE_FAST               3 (e)

 193    L7:     LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                LOAD_CONST               9 ((0, None))
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

 192   L15:     RERAISE                  0

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
