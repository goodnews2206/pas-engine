# scripts_readiness/run_simulations

- **pyc:** `scripts\__pycache__\run_simulations.cpython-314.pyc`
- **expected source path (absent):** `scripts/run_simulations.py`
- **co_filename (from bytecode):** `scripts\run_simulations.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS142 — CLI: run PAS simulation scenarios in-process.

Usage:
    python scripts/run_simulations.py
    python scripts/run_simulations.py --scenario callback_request
    python scripts/run_simulations.py --json
    python scripts/run_simulations.py --limit 5
    python scripts/run_simulations.py --brokerage-id demo

Exit codes:
    0   all scenarios ran (regardless of pass/fail)
    1   no scenarios were executed (bad filter or empty registry)
    2   bad CLI arguments
```

## Imports

`List`, `Optional`, `SCENARIOS`, `__future__`, `annotations`, `app.services.simulation.report`, `app.services.simulation.runner`, `app.services.simulation.scenarios`, `argparse`, `generate_simulation_report`, `get_scenario`, `json`, `os`, `run_scenario`, `sys`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_human_per_scenario`, `_human_summary`, `main`

## Env-key candidates

`FAIL`, `PASS`

## String constants (redacted where noted)

- '\nPAS142 — CLI: run PAS simulation scenarios in-process.\n\nUsage:\n    python scripts/run_simulations.py\n    python scripts/run_simulations.py --scenario callback_request\n    python scripts/run_simulations.py --json\n    python scripts/run_simulations.py --limit 5\n    python scripts/run_simulations.py --brokerage-id demo\n\nExit codes:\n    0   all scenarios ran (regardless of pass/fail)\n    1   no scenarios were executed (bad filter or empty registry)\n    2   bad CLI arguments\n'
- 'utf-8'
- 'dict'
- 'return'
- 'str'
- 'passed'
- 'PASS'
- 'FAIL'
- 'error'
- 'evaluation'
- 'replay_score'
- 'missing_steps'
- 'transcript'
- '  ['
- 'scenario_id'
- ' — '
- 'scenario_title'
- '        expected='
- 'expected_outcome'
- '  actual='
- 'actual_outcome'
- '        score='
- '/100  turns='
- '  events='
- 'events_count'
- '        missing: '
- '        ERROR: '
- 'report'
- 'BATCH SUMMARY  '
- 'total_scenarios'
- ' passed ('
- 'pass_rate'
- '.0%'
- '  avg replay score: '
- 'average_replay_score'
- '/100   avg turns: '
- 'average_turns'
- '   avg events: '
- 'average_events'
- 'outcome_breakdown'
- '  outcome breakdown:'
- '    - '
- 'by_category'
- '  by category:'
- ' pass (score avg '
- 'avg_replay_score'
- 'missing_lifecycle_frequency'
- '  most-missed lifecycle steps:'
- 'weakest_scenarios'
- '  weakest scenarios:'
- ' (score '
- 'warnings'
- '  warnings:'
- '    ! '
- '========================================================================'
- 'argv'
- 'Optional[list]'
- 'int'
- 'run_simulations'
- 'Run PAS scenario simulations in-process and report results.'
- '--scenario'
- 'Run a single scenario by id (otherwise the full registry).'
- '--limit'
- 'Cap the number of scenarios executed (after --scenario filter).'
- '--brokerage-id'
- 'demo'
- 'Brokerage id to attribute to simulated calls (default: demo).'
- '--json'
- 'store_true'
- 'Emit per-scenario results + report as JSON.'
- 'Unknown scenario id: '
- 'No scenarios to run.'
- 'results'
- 'Running '
- " scenario(s) against brokerage='"
- '------------------------------------------------------------------------'

## Disassembly

```
   0            RESUME                   0

   1            LOAD_CONST               0 ('\nPAS142 — CLI: run PAS simulation scenarios in-process.\n\nUsage:\n    python scripts/run_simulations.py\n    python scripts/run_simulations.py --scenario callback_request\n    python scripts/run_simulations.py --json\n    python scripts/run_simulations.py --limit 5\n    python scripts/run_simulations.py --brokerage-id demo\n\nExit codes:\n    0   all scenarios ran (regardless of pass/fail)\n    1   no scenarios were executed (bad filter or empty registry)\n    2   bad CLI arguments\n')
                STORE_NAME               0 (__doc__)

  17            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('annotations',))
                IMPORT_NAME              1 (__future__)
                IMPORT_FROM              2 (annotations)
                STORE_NAME               2 (annotations)
                POP_TOP

  19            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              3 (argparse)
                STORE_NAME               3 (argparse)

  20            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              4 (json)
                STORE_NAME               4 (json)

  21            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              5 (os)
                STORE_NAME               5 (os)

  22            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              6 (sys)
                STORE_NAME               6 (sys)

  23            LOAD_SMALL_INT           0
                LOAD_CONST               3 (('List', 'Optional'))
                IMPORT_NAME              7 (typing)
                IMPORT_FROM              8 (List)
                STORE_NAME               8 (List)
                IMPORT_FROM              9 (Optional)
                STORE_NAME               9 (Optional)
                POP_TOP

  26            LOAD_NAME                5 (os)
                LOAD_ATTR               20 (path)
                LOAD_ATTR               23 (abspath + NULL|self)
                LOAD_NAME                5 (os)
                LOAD_ATTR               20 (path)
                LOAD_ATTR               25 (join + NULL|self)
                LOAD_NAME                5 (os)
                LOAD_ATTR               20 (path)
                LOAD_ATTR               27 (dirname + NULL|self)
                LOAD_NAME               14 (__file__)
                CALL                     1
                LOAD_CONST               4 ('..')
                CALL                     2
                CALL                     1
                STORE_NAME              15 (_REPO_ROOT)

  27            LOAD_NAME               15 (_REPO_ROOT)
                LOAD_NAME                6 (sys)
                LOAD_ATTR               20 (path)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       29 (to L1)
                NOT_TAKEN

  28            LOAD_NAME                6 (sys)
                LOAD_ATTR               20 (path)
                LOAD_ATTR               33 (insert + NULL|self)
                LOAD_SMALL_INT           0
                LOAD_NAME               15 (_REPO_ROOT)
                CALL                     2
                POP_TOP

  33    L1:     LOAD_NAME                6 (sys)
                LOAD_ATTR               34 (stdout)
                LOAD_NAME                6 (sys)
                LOAD_ATTR               36 (stderr)
                BUILD_TUPLE              2
                GET_ITER
        L2:     FOR_ITER                22 (to L5)
                STORE_NAME              19 (_stream)

  34            NOP

  35    L3:     LOAD_NAME               19 (_stream)
                LOAD_ATTR               41 (reconfigure + NULL|self)
                LOAD_CONST               5 ('utf-8')
                LOAD_CONST               6 (('encoding',))
                CALL_KW                  1
                POP_TOP
        L4:     JUMP_BACKWARD           24 (to L2)

  33    L5:     END_FOR
                POP_ITER

  40            LOAD_SMALL_INT           0
                LOAD_CONST               7 (('SCENARIOS', 'get_scenario'))
                IMPORT_NAME             22 (app.services.simulation.scenarios)
                IMPORT_FROM             23 (SCENARIOS)
                STORE_NAME              23 (SCENARIOS)
                IMPORT_FROM             24 (get_scenario)
                STORE_NAME              24 (get_scenario)
                POP_TOP

  41            LOAD_SMALL_INT           0
                LOAD_CONST               8 (('run_scenario',))
                IMPORT_NAME             25 (app.services.simulation.runner)
                IMPORT_FROM             26 (run_scenario)
                STORE_NAME              26 (run_scenario)
                POP_TOP

  42            LOAD_SMALL_INT           0
                LOAD_CONST               9 (('generate_simulation_report',))
                IMPORT_NAME             27 (app.services.simulation.report)
                IMPORT_FROM             28 (generate_simulation_report)
                STORE_NAME              28 (generate_simulation_report)
                POP_TOP

  45            LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA31E0, file "scripts\run_simulations.py", line 45>)
                MAKE_FUNCTION
                LOAD_CONST              11 (<code object _human_per_scenario at 0x0000018C17F75BE0, file "scripts\run_simulations.py", line 45>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              29 (_human_per_scenario)

  63            LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA21F0, file "scripts\run_simulations.py", line 63>)
                MAKE_FUNCTION
                LOAD_CONST              13 (<code object _human_summary at 0x0000018C17F41160, file "scripts\run_simulations.py", line 63>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              30 (_human_summary)

 114            LOAD_CONST              17 ((None,))
                LOAD_CONST              14 (<code object __annotate__ at 0x0000018C17FA3960, file "scripts\run_simulations.py", line 114>)
                MAKE_FUNCTION
                LOAD_CONST              15 (<code object main at 0x0000018C17ED9FB0, file "scripts\run_simulations.py", line 114>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                SET_FUNCTION_ATTRIBUTE   1 (defaults)
                STORE_NAME              31 (main)

 177            LOAD_NAME               32 (__name__)
                LOAD_CONST              16 ('__main__')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       14 (to L6)
                NOT_TAKEN

 178            LOAD_NAME               33 (SystemExit)
                PUSH_NULL
                LOAD_NAME               31 (main)
                PUSH_NULL
                CALL                     0
                CALL                     1
                RAISE_VARARGS            1

 177    L6:     LOAD_CONST               2 (None)
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

  36            LOAD_NAME               21 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L9)
                NOT_TAKEN
                POP_TOP

  37    L8:     POP_EXCEPT
                JUMP_BACKWARD           98 (to L2)

  36    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L7 [1]
  L7 to L8 -> L10 [2] lasti
  L9 to L10 -> L10 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "scripts\run_simulations.py", line 45>:
 45           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('r')
              LOAD_CONST               2 ('dict')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _human_per_scenario at 0x0000018C17F75BE0, file "scripts\run_simulations.py", line 45>:
 45           RESUME                   0

 46           LOAD_FAST_BORROW         0 (r)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               0 ('passed')
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L2)
      L1:     LOAD_CONST               2 ('FAIL')
      L2:     STORE_FAST               1 (pass_str)

 47           LOAD_FAST_BORROW         0 (r)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               3 ('error')
              CALL                     1
              STORE_FAST               2 (err)

 48           LOAD_FAST_BORROW         0 (r)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               4 ('evaluation')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L3:     LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               5 ('replay_score')
              LOAD_CONST               6 ('?')
              CALL                     2
              STORE_FAST               3 (score)

 49           LOAD_FAST_BORROW         0 (r)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               4 ('evaluation')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L4:     LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               7 ('missing_steps')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L5:     STORE_FAST               4 (missing)

 50           LOAD_GLOBAL              3 (len + NULL)
              LOAD_FAST_BORROW         0 (r)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               8 ('transcript')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L6)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L6:     CALL                     1
              STORE_FAST               5 (n_turns)

 52           LOAD_CONST               9 ('  [')
              LOAD_FAST                1 (pass_str)
              FORMAT_SIMPLE
              LOAD_CONST              10 ('] ')
              LOAD_FAST_BORROW         0 (r)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              11 ('scenario_id')
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST              12 (' — ')
              LOAD_FAST_BORROW         0 (r)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              13 ('scenario_title')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L7)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST              14 ('')
      L7:     FORMAT_SIMPLE
              BUILD_STRING             6

 53           LOAD_CONST              15 ('        expected=')
              LOAD_FAST_BORROW         0 (r)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              16 ('expected_outcome')
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST              17 ('  actual=')
              LOAD_FAST_BORROW         0 (r)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              18 ('actual_outcome')
              CALL                     1
              FORMAT_SIMPLE
              BUILD_STRING             4

 54           LOAD_CONST              19 ('        score=')
              LOAD_FAST_BORROW         3 (score)
              FORMAT_SIMPLE
              LOAD_CONST              20 ('/100  turns=')
              LOAD_FAST_BORROW         5 (n_turns)
              FORMAT_SIMPLE
              LOAD_CONST              21 ('  events=')
              LOAD_FAST_BORROW         0 (r)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              22 ('events_count')
              LOAD_SMALL_INT           0
              CALL                     2
              FORMAT_SIMPLE
              BUILD_STRING             6

 51           BUILD_LIST               3
              STORE_FAST               6 (bits)

 56           LOAD_FAST_BORROW         4 (missing)
              TO_BOOL
              POP_JUMP_IF_FALSE       36 (to L8)
              NOT_TAKEN

 57           LOAD_FAST_BORROW         6 (bits)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_CONST              23 ('        missing: ')
              LOAD_CONST              24 (', ')
              LOAD_ATTR                7 (join + NULL|self)
              LOAD_FAST_BORROW         4 (missing)
              CALL                     1
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP

 58   L8:     LOAD_FAST_BORROW         2 (err)
              TO_BOOL
              POP_JUMP_IF_FALSE       21 (to L9)
              NOT_TAKEN

 59           LOAD_FAST_BORROW         6 (bits)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_CONST              25 ('        ERROR: ')
              LOAD_FAST_BORROW         2 (err)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP

 60   L9:     LOAD_CONST              26 ('\n')
              LOAD_ATTR                7 (join + NULL|self)
              LOAD_FAST_BORROW         6 (bits)
              CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "scripts\run_simulations.py", line 63>:
 63           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('report')
              LOAD_CONST               2 ('dict')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _human_summary at 0x0000018C17F41160, file "scripts\run_simulations.py", line 63>:
  --            MAKE_CELL               10 (missing)

  63            RESUME                   0

  64            BUILD_LIST               0
                STORE_FAST               1 (lines)

  65            LOAD_FAST_BORROW         1 (lines)
                LOAD_ATTR                1 (append + NULL|self)
                LOAD_CONST              37 ('========================================================================')
                CALL                     1
                POP_TOP

  66            LOAD_FAST_BORROW         1 (lines)
                LOAD_ATTR                1 (append + NULL|self)

  67            LOAD_CONST               1 ('BATCH SUMMARY  ')
                LOAD_FAST_BORROW         0 (report)
                LOAD_ATTR                3 (get + NULL|self)
                LOAD_CONST               2 ('passed')
                LOAD_SMALL_INT           0
                CALL                     2
                FORMAT_SIMPLE
                LOAD_CONST               3 ('/')
                LOAD_FAST_BORROW         0 (report)
                LOAD_ATTR                3 (get + NULL|self)
                LOAD_CONST               4 ('total_scenarios')
                LOAD_SMALL_INT           0
                CALL                     2
                FORMAT_SIMPLE
                LOAD_CONST               5 (' passed (')

  68            LOAD_FAST_BORROW         0 (report)
                LOAD_ATTR                3 (get + NULL|self)
                LOAD_CONST               6 ('pass_rate')
                LOAD_SMALL_INT           0
                CALL                     2
                LOAD_CONST               7 ('.0%')
                FORMAT_WITH_SPEC
                LOAD_CONST               8 (')')

  67            BUILD_STRING             7

  66            CALL                     1
                POP_TOP

  70            LOAD_FAST_BORROW         1 (lines)
                LOAD_ATTR                1 (append + NULL|self)

  71            LOAD_CONST               9 ('  avg replay score: ')
                LOAD_FAST_BORROW         0 (report)
                LOAD_ATTR                3 (get + NULL|self)
                LOAD_CONST              10 ('average_replay_score')
                CALL                     1
                FORMAT_SIMPLE
                LOAD_CONST              11 ('/100   avg turns: ')

  72            LOAD_FAST_BORROW         0 (report)
                LOAD_ATTR                3 (get + NULL|self)
                LOAD_CONST              12 ('average_turns')
                CALL                     1
                FORMAT_SIMPLE
                LOAD_CONST              13 ('   avg events: ')

  73            LOAD_FAST_BORROW         0 (report)
                LOAD_ATTR                3 (get + NULL|self)
                LOAD_CONST              14 ('average_events')
                CALL                     1
                FORMAT_SIMPLE

  71            BUILD_STRING             6

  70            CALL                     1
                POP_TOP

  76            LOAD_FAST_BORROW         0 (report)
                LOAD_ATTR                3 (get + NULL|self)
                LOAD_CONST              15 ('outcome_breakdown')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
        L1:     STORE_FAST               2 (outcomes)

  77            LOAD_FAST_BORROW         2 (outcomes)
                TO_BOOL
                POP_JUMP_IF_FALSE       65 (to L4)
                NOT_TAKEN

  78            LOAD_FAST_BORROW         1 (lines)
                LOAD_ATTR                1 (append + NULL|self)
                LOAD_CONST              16 ('  outcome breakdown:')
                CALL                     1
                POP_TOP

  79            LOAD_GLOBAL              5 (sorted + NULL)
                LOAD_FAST_BORROW         2 (outcomes)
                CALL                     1
                GET_ITER
        L2:     FOR_ITER                32 (to L3)
                STORE_FAST               3 (k)

  80            LOAD_FAST_BORROW         1 (lines)
                LOAD_ATTR                1 (append + NULL|self)
                LOAD_CONST              17 ('    - ')
                LOAD_FAST_BORROW         3 (k)
                FORMAT_SIMPLE
                LOAD_CONST              18 (': ')
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (outcomes, k)
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                BUILD_STRING             4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           34 (to L2)

  79    L3:     END_FOR
                POP_ITER

  82    L4:     LOAD_FAST_BORROW         0 (report)
                LOAD_ATTR                3 (get + NULL|self)
                LOAD_CONST              19 ('by_category')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
        L5:     STORE_FAST               4 (by_cat)

  83            LOAD_FAST_BORROW         4 (by_cat)
                TO_BOOL
                POP_JUMP_IF_FALSE      119 (to L8)
                NOT_TAKEN

  84            LOAD_FAST_BORROW         1 (lines)
                LOAD_ATTR                1 (append + NULL|self)
                LOAD_CONST              20 ('  by category:')
                CALL                     1
                POP_TOP

  85            LOAD_GLOBAL              5 (sorted + NULL)
                LOAD_FAST_BORROW         4 (by_cat)
                CALL                     1
                GET_ITER
        L6:     FOR_ITER                86 (to L7)
                STORE_FAST               5 (cat)

  86            LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (by_cat, cat)
                BINARY_OP               26 ([])
                STORE_FAST               6 (c)

  87            LOAD_FAST_BORROW         1 (lines)
                LOAD_ATTR                1 (append + NULL|self)

  88            LOAD_CONST              17 ('    - ')
                LOAD_FAST_BORROW         5 (cat)
                FORMAT_SIMPLE
                LOAD_CONST              18 (': ')
                LOAD_FAST_BORROW         6 (c)
                LOAD_ATTR                3 (get + NULL|self)
                LOAD_CONST               2 ('passed')
                CALL                     1
                FORMAT_SIMPLE
                LOAD_CONST               3 ('/')
                LOAD_FAST_BORROW         6 (c)
                LOAD_ATTR                3 (get + NULL|self)
                LOAD_CONST              21 ('n')
                CALL                     1
                FORMAT_SIMPLE
                LOAD_CONST              22 (' pass (score avg ')

  89            LOAD_FAST_BORROW         6 (c)
                LOAD_ATTR                3 (get + NULL|self)
                LOAD_CONST              23 ('avg_replay_score')
                CALL                     1
                FORMAT_SIMPLE
                LOAD_CONST               8 (')')

  88            BUILD_STRING             9

  87            CALL                     1
                POP_TOP
                JUMP_BACKWARD           88 (to L6)

  85    L7:     END_FOR
                POP_ITER

  92    L8:     LOAD_FAST_BORROW         0 (report)
                LOAD_ATTR                3 (get + NULL|self)
                LOAD_CONST              24 ('missing_lifecycle_frequency')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
        L9:     STORE_DEREF             10 (missing)

  93            LOAD_DEREF              10 (missing)
                TO_BOOL
                POP_JUMP_IF_FALSE       72 (to L12)
                NOT_TAKEN

  94            LOAD_FAST_BORROW         1 (lines)
                LOAD_ATTR                1 (append + NULL|self)
                LOAD_CONST              25 ('  most-missed lifecycle steps:')
                CALL                     1
                POP_TOP

  95            LOAD_GLOBAL              5 (sorted + NULL)
                LOAD_DEREF              10 (missing)
                LOAD_FAST_BORROW        10 (missing)
                BUILD_TUPLE              1
                LOAD_CONST              26 (<code object <lambda> at 0x0000018C17FA3E10, file "scripts\run_simulations.py", line 95>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_CONST              27 (('key',))
                CALL_KW                  2
                GET_ITER
       L10:     FOR_ITER                33 (to L11)
                STORE_FAST               3 (k)

  96            LOAD_FAST_BORROW         1 (lines)
                LOAD_ATTR                1 (append + NULL|self)
                LOAD_CONST              17 ('    - ')
                LOAD_FAST_BORROW         3 (k)
                FORMAT_SIMPLE
                LOAD_CONST              18 (': ')
                LOAD_DEREF              10 (missing)
                LOAD_FAST_BORROW         3 (k)
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                BUILD_STRING             4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           35 (to L10)

  95   L11:     END_FOR
                POP_ITER

  98   L12:     LOAD_FAST_BORROW         0 (report)
                LOAD_ATTR                3 (get + NULL|self)
                LOAD_CONST              28 ('weakest_scenarios')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
       L13:     STORE_FAST               7 (weakest)

  99            LOAD_FAST_BORROW         7 (weakest)
                TO_BOOL
                POP_JUMP_IF_FALSE       81 (to L16)
                NOT_TAKEN

 100            LOAD_FAST_BORROW         1 (lines)
                LOAD_ATTR                1 (append + NULL|self)
                LOAD_CONST              29 ('  weakest scenarios:')
                CALL                     1
                POP_TOP

 101            LOAD_FAST_BORROW         7 (weakest)
                GET_ITER
       L14:     FOR_ITER                57 (to L15)
                STORE_FAST               8 (w)

 102            LOAD_FAST_BORROW         1 (lines)
                LOAD_ATTR                1 (append + NULL|self)
                LOAD_CONST              17 ('    - ')
                LOAD_FAST_BORROW         8 (w)
                LOAD_ATTR                3 (get + NULL|self)
                LOAD_CONST              30 ('id')
                CALL                     1
                FORMAT_SIMPLE
                LOAD_CONST              31 (' (score ')
                LOAD_FAST_BORROW         8 (w)
                LOAD_ATTR                3 (get + NULL|self)
                LOAD_CONST              32 ('replay_score')
                CALL                     1
                FORMAT_SIMPLE
                LOAD_CONST               8 (')')
                BUILD_STRING             5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           59 (to L14)

 101   L15:     END_FOR
                POP_ITER

 104   L16:     LOAD_FAST_BORROW         0 (report)
                LOAD_ATTR                3 (get + NULL|self)
                LOAD_CONST              33 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L17)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
       L17:     STORE_FAST               9 (warnings)

 105            LOAD_FAST_BORROW         9 (warnings)
                TO_BOOL
                POP_JUMP_IF_FALSE       47 (to L20)
                NOT_TAKEN

 106            LOAD_FAST_BORROW         1 (lines)
                LOAD_ATTR                1 (append + NULL|self)
                LOAD_CONST              34 ('  warnings:')
                CALL                     1
                POP_TOP

 107            LOAD_FAST_BORROW         9 (warnings)
                GET_ITER
       L18:     FOR_ITER                23 (to L19)
                STORE_FAST               8 (w)

 108            LOAD_FAST_BORROW         1 (lines)
                LOAD_ATTR                1 (append + NULL|self)
                LOAD_CONST              35 ('    ! ')
                LOAD_FAST_BORROW         8 (w)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           25 (to L18)

 107   L19:     END_FOR
                POP_ITER

 110   L20:     LOAD_FAST_BORROW         1 (lines)
                LOAD_ATTR                1 (append + NULL|self)
                LOAD_CONST              37 ('========================================================================')
                CALL                     1
                POP_TOP

 111            LOAD_CONST              36 ('\n')
                LOAD_ATTR                7 (join + NULL|self)
                LOAD_FAST_BORROW         1 (lines)
                CALL                     1
                RETURN_VALUE

Disassembly of <code object <lambda> at 0x0000018C17FA3E10, file "scripts\run_simulations.py", line 95>:
  --           COPY_FREE_VARS           1

  95           RESUME                   0
               LOAD_DEREF               1 (missing)
               LOAD_FAST_BORROW         0 (s)
               BINARY_OP               26 ([])
               UNARY_NEGATIVE
               LOAD_FAST_BORROW         0 (s)
               BUILD_TUPLE              2
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "scripts\run_simulations.py", line 114>:
114           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17ED9FB0, file "scripts\run_simulations.py", line 114>:
 114            RESUME                   0

 115            LOAD_GLOBAL              0 (argparse)
                LOAD_ATTR                2 (ArgumentParser)
                PUSH_NULL

 116            LOAD_CONST               0 ('run_simulations')

 117            LOAD_CONST               1 ('Run PAS scenario simulations in-process and report results.')

 115            LOAD_CONST               2 (('prog', 'description'))
                CALL_KW                  2
                STORE_FAST               1 (parser)

 119            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)

 120            LOAD_CONST               3 ('--scenario')

 121            LOAD_CONST               4 (None)

 122            LOAD_CONST               5 ('Run a single scenario by id (otherwise the full registry).')

 119            LOAD_CONST               6 (('default', 'help'))
                CALL_KW                  3
                POP_TOP

 124            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)

 125            LOAD_CONST               7 ('--limit')

 126            LOAD_GLOBAL              6 (int)

 127            LOAD_CONST               4 (None)

 128            LOAD_CONST               8 ('Cap the number of scenarios executed (after --scenario filter).')

 124            LOAD_CONST               9 (('type', 'default', 'help'))
                CALL_KW                  4
                POP_TOP

 130            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)

 131            LOAD_CONST              10 ('--brokerage-id')

 132            LOAD_CONST              11 ('demo')

 133            LOAD_CONST              12 ('Brokerage id to attribute to simulated calls (default: demo).')

 130            LOAD_CONST               6 (('default', 'help'))
                CALL_KW                  3
                POP_TOP

 135            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)

 136            LOAD_CONST              13 ('--json')

 137            LOAD_CONST              14 ('store_true')

 138            LOAD_CONST              15 ('Emit per-scenario results + report as JSON.')

 135            LOAD_CONST              16 (('action', 'help'))
                CALL_KW                  3
                POP_TOP

 140            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                9 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 143            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               10 (scenario)
                TO_BOOL
                POP_JUMP_IF_FALSE       72 (to L2)
                NOT_TAKEN

 144            LOAD_GLOBAL             13 (get_scenario + NULL)
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               10 (scenario)
                CALL                     1
                STORE_FAST               3 (s)

 145            LOAD_FAST_BORROW         3 (s)
                POP_JUMP_IF_NOT_NONE    43 (to L1)
                NOT_TAKEN

 146            LOAD_GLOBAL             15 (print + NULL)
                LOAD_CONST              17 ('Unknown scenario id: ')
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               10 (scenario)
                FORMAT_SIMPLE
                BUILD_STRING             2
                LOAD_GLOBAL             16 (sys)
                LOAD_ATTR               18 (stderr)
                LOAD_CONST              18 (('file',))
                CALL_KW                  2
                POP_TOP

 147            LOAD_SMALL_INT           1
                RETURN_VALUE

 148    L1:     LOAD_FAST_BORROW         3 (s)
                BUILD_LIST               1
                STORE_FAST               4 (scenarios)
                JUMP_FORWARD            15 (to L3)

 150    L2:     LOAD_GLOBAL             21 (list + NULL)
                LOAD_GLOBAL             22 (SCENARIOS)
                CALL                     1
                STORE_FAST               4 (scenarios)

 152    L3:     LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               24 (limit)
                POP_JUMP_IF_NONE        33 (to L4)
                NOT_TAKEN
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               24 (limit)
                LOAD_SMALL_INT           0
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE       16 (to L4)
                NOT_TAKEN

 153            LOAD_FAST_BORROW         4 (scenarios)
                LOAD_CONST               4 (None)
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               24 (limit)
                BINARY_SLICE
                STORE_FAST               4 (scenarios)

 155    L4:     LOAD_FAST_BORROW         4 (scenarios)
                TO_BOOL
                POP_JUMP_IF_TRUE        30 (to L5)
                NOT_TAKEN

 156            LOAD_GLOBAL             15 (print + NULL)
                LOAD_CONST              19 ('No scenarios to run.')
                LOAD_GLOBAL             16 (sys)
                LOAD_ATTR               18 (stderr)
                LOAD_CONST              18 (('file',))
                CALL_KW                  2
                POP_TOP

 157            LOAD_SMALL_INT           1
                RETURN_VALUE

 159    L5:     LOAD_FAST_BORROW         4 (scenarios)
                GET_ITER
                LOAD_FAST_AND_CLEAR      3 (s)
                SWAP                     2
        L6:     BUILD_LIST               0
                SWAP                     2
        L7:     FOR_ITER                25 (to L8)
                STORE_FAST               3 (s)
                LOAD_GLOBAL             27 (run_scenario + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (s, args)
                LOAD_ATTR               28 (brokerage_id)
                LOAD_CONST              20 (('brokerage_id',))
                CALL_KW                  2
                LIST_APPEND              2
                JUMP_BACKWARD           27 (to L7)
        L8:     END_FOR
                POP_ITER
        L9:     STORE_FAST               5 (results)
                STORE_FAST               3 (s)

 160            LOAD_GLOBAL             31 (generate_simulation_report + NULL)
                LOAD_FAST_BORROW         5 (results)
                CALL                     1
                STORE_FAST               6 (report)

 162            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               32 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       47 (to L10)
                NOT_TAKEN

 163            LOAD_CONST              21 ('results')
                LOAD_FAST_BORROW         5 (results)
                LOAD_CONST              22 ('report')
                LOAD_FAST_BORROW         6 (report)
                BUILD_MAP                2
                STORE_FAST               7 (out)

 164            LOAD_GLOBAL             15 (print + NULL)
                LOAD_GLOBAL             32 (json)
                LOAD_ATTR               34 (dumps)
                PUSH_NULL
                LOAD_FAST_BORROW         7 (out)
                LOAD_GLOBAL             36 (str)
                LOAD_SMALL_INT           2
                LOAD_CONST              23 (('default', 'indent'))
                CALL_KW                  3
                CALL                     1
                POP_TOP

 174            LOAD_SMALL_INT           0
                RETURN_VALUE

 166   L10:     LOAD_GLOBAL             15 (print + NULL)
                CALL                     0
                POP_TOP

 167            LOAD_GLOBAL             15 (print + NULL)
                LOAD_CONST              24 ('Running ')
                LOAD_GLOBAL             39 (len + NULL)
                LOAD_FAST_BORROW         4 (scenarios)
                CALL                     1
                FORMAT_SIMPLE
                LOAD_CONST              25 (" scenario(s) against brokerage='")
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               28 (brokerage_id)
                FORMAT_SIMPLE
                LOAD_CONST              26 ("'")
                BUILD_STRING             5
                CALL                     1
                POP_TOP

 168            LOAD_GLOBAL             15 (print + NULL)
                LOAD_CONST              27 ('------------------------------------------------------------------------')
                CALL                     1
                POP_TOP

 169            LOAD_FAST_BORROW         5 (results)
                GET_ITER
       L11:     FOR_ITER                23 (to L12)
                STORE_FAST               8 (r)

 170            LOAD_GLOBAL             15 (print + NULL)
                LOAD_GLOBAL             41 (_human_per_scenario + NULL)
                LOAD_FAST_BORROW         8 (r)
                CALL                     1
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           25 (to L11)

 169   L12:     END_FOR
                POP_ITER

 171            LOAD_GLOBAL             15 (print + NULL)
                CALL                     0
                POP_TOP

 172            LOAD_GLOBAL             15 (print + NULL)
                LOAD_GLOBAL             43 (_human_summary + NULL)
                LOAD_FAST_BORROW         6 (report)
                CALL                     1
                CALL                     1
                POP_TOP

 174            LOAD_SMALL_INT           0
                RETURN_VALUE

  --   L13:     SWAP                     2
                POP_TOP

 159            SWAP                     2
                STORE_FAST               3 (s)
                RERAISE                  0
ExceptionTable:
  L6 to L9 -> L13 [2]
```
