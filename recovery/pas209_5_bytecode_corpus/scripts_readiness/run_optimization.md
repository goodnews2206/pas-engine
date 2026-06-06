# scripts_readiness/run_optimization

- **pyc:** `scripts\__pycache__\run_optimization.cpython-314.pyc`
- **expected source path (absent):** `scripts/run_optimization.py`
- **co_filename (from bytecode):** `scripts\run_optimization.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS143A — CLI: run the strategy × scenario matrix and report rankings.

Usage:
    python scripts/run_optimization.py
    python scripts/run_optimization.py --scenario already_has_agent
    python scripts/run_optimization.py --strategy consultative_redirect
    python scripts/run_optimization.py --json
    python scripts/run_optimization.py --limit-scenarios 5
    python scripts/run_optimization.py --limit-strategies 3
    python scripts/run_optimization.py --brokerage-id demo

Exit codes:
    0   matrix executed (regardless of pass/fail)
    1   no scenarios or strategies after filters
    2   bad CLI arguments
```

## Imports

`List`, `Optional`, `SCENARIOS`, `STRATEGIES`, `__future__`, `annotations`, `app.services.optimization.matrix_runner`, `app.services.optimization.recommendations`, `app.services.optimization.report`, `app.services.optimization.strategies`, `app.services.simulation.scenarios`, `argparse`, `generate_optimization_report`, `generate_recommendations`, `get_scenario`, `get_strategy`, `json`, `os`, `run_strategy_matrix`, `summarize_recommendations`, `sys`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_human_summary`, `main`

## Env-key candidates

`RECOMMENDATIONS`, `WARNINGS`

## String constants (redacted where noted)

- '\nPAS143A — CLI: run the strategy × scenario matrix and report rankings.\n\nUsage:\n    python scripts/run_optimization.py\n    python scripts/run_optimization.py --scenario already_has_agent\n    python scripts/run_optimization.py --strategy consultative_redirect\n    python scripts/run_optimization.py --json\n    python scripts/run_optimization.py --limit-scenarios 5\n    python scripts/run_optimization.py --limit-strategies 3\n    python scripts/run_optimization.py --brokerage-id demo\n\nExit codes:\n    0   matrix executed (regardless of pass/fail)\n    1   no scenarios or strategies after filters\n    2   bad CLI arguments\n'
- 'utf-8'
- 'matrix'
- 'show_divergence'
- 'report'
- 'dict'
- 'Optional[dict]'
- 'bool'
- 'return'
- 'str'
- 'OPTIMIZATION REPORT'
- 'headline'
- 'metrics'
- 'MATRIX METRICS'
- '  total runs:        '
- 'total_runs'
- '  pass rate:         '
- 'pass_rate'
- '.0%'
- '  avg replay score:  '
- 'average_replay_score'
- '/100'
- '  avg turns:         '
- 'average_turns'
- '  errors:            '
- 'error_count'
- 'behavior_summary'
- 'BEHAVIOURAL SUMMARY'
- '  avg trust:         '
- 'avg_trust'
- '  avg frustration:   '
- 'avg_frustration'
- '  divergence rate:   '
- 'divergence_rate'
- '  escalation rate:   '
- 'escalation_rate'
- '  drop-off rate:     '
- 'dropoff_rate'
- '  recovery rate:     '
- 'recovery_rate'
- 'ranked_strategies'
- 'RANKED STRATEGIES (best → worst)'
- 'components'
- 'effective'
- '[eff]'
- '[infra]'
- '  #'
- 'rank'
- 'strategy_id'
- '<25'
- '  score='
- 'score'
- '6.2f'
- 'strengths'
- '        + '
- 'weaknesses'
- '        - '
- 'by_strategy'
- 'PER-STRATEGY OUTCOME RATES'
- '  - '
- ': booked='
- 'booked_rate'
- ' callback='
- 'callback_rate'
- ' not_booked='
- 'not_booked_rate'
- ' transferred='
- 'transferred_rate'
- 'personality_insights'
- 'STRATEGY ↔ PERSONALITY FIT'
- ': best='
- 'best_personality'
- ' (pass '
- 'best_pass_rate'
- '), worst='
- 'worst_personality'
- 'worst_pass_rate'
- 'results'
- 'divergence_triggered'
- 'DIVERGENT CELLS'
- 'scenario_id'
- ' × '
- ': outcome='
- 'actual_outcome'
- ' trust='
- 'trust_score'
- ' frust='
- 'frustration_score'
- ' state='
- 'final_behavior_state'
- 'divergence_actions'
- '        · turn '
- 'turn'
- 'action'
- '  (no divergence in this matrix)'
- 'warnings'
- 'WARNINGS'
- '  ! '
- 'recommendations'
- 'RECOMMENDATIONS'
- '  • '
- '=============================================================================='
- 'argv'
- 'Optional[list]'
- 'int'
- 'run_optimization'
- 'Run the strategy × scenario matrix and rank strategy variants.'
- '--scenario'
- 'Restrict matrix to one scenario id.'
- '--strategy'
- 'Restrict matrix to one strategy id.'
- '--limit-scenarios'
- 'Cap scenarios after --scenario filter.'
- '--limit-strategies'
- 'Cap strategies after --strategy filter.'
- '--brokerage-id'
- 'demo'
- 'Brokerage id attributed to simulated calls (default: demo).'
- '--personality'
- 'PAS143B — restrict matrix to scenarios with this personality_id.'
- '--show-divergence'
- 'store_true'
- 'PAS143B — print per-cell divergence actions (drops / escalations / booking flips) in the human view.'
- '--recommendations'
- 'PAS143C — print plain-English recommendations (the broker-facing summary) at the end of the human view.'
- '--json'
- 'Emit matrix + report + recommendations as JSON instead of the human view.'
- 'Unknown scenario id: '
- 'No scenarios match personality_id='
- 'Unknown strategy id: '
- 'Empty matrix after filters — nothing to run.'
- 'Running '
- ' scenario(s) × '
- ' strategy(ies) = '
- " cell(s) against brokerage='"

## Disassembly

```
   0            RESUME                   0

   1            LOAD_CONST               0 ('\nPAS143A — CLI: run the strategy × scenario matrix and report rankings.\n\nUsage:\n    python scripts/run_optimization.py\n    python scripts/run_optimization.py --scenario already_has_agent\n    python scripts/run_optimization.py --strategy consultative_redirect\n    python scripts/run_optimization.py --json\n    python scripts/run_optimization.py --limit-scenarios 5\n    python scripts/run_optimization.py --limit-strategies 3\n    python scripts/run_optimization.py --brokerage-id demo\n\nExit codes:\n    0   matrix executed (regardless of pass/fail)\n    1   no scenarios or strategies after filters\n    2   bad CLI arguments\n')
                STORE_NAME               0 (__doc__)

  19            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('annotations',))
                IMPORT_NAME              1 (__future__)
                IMPORT_FROM              2 (annotations)
                STORE_NAME               2 (annotations)
                POP_TOP

  21            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              3 (argparse)
                STORE_NAME               3 (argparse)

  22            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              4 (json)
                STORE_NAME               4 (json)

  23            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              5 (os)
                STORE_NAME               5 (os)

  24            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              6 (sys)
                STORE_NAME               6 (sys)

  25            LOAD_SMALL_INT           0
                LOAD_CONST               3 (('List', 'Optional'))
                IMPORT_NAME              7 (typing)
                IMPORT_FROM              8 (List)
                STORE_NAME               8 (List)
                IMPORT_FROM              9 (Optional)
                STORE_NAME               9 (Optional)
                POP_TOP

  28            LOAD_NAME                5 (os)
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

  29            LOAD_NAME               15 (_REPO_ROOT)
                LOAD_NAME                6 (sys)
                LOAD_ATTR               20 (path)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       29 (to L1)
                NOT_TAKEN

  30            LOAD_NAME                6 (sys)
                LOAD_ATTR               20 (path)
                LOAD_ATTR               33 (insert + NULL|self)
                LOAD_SMALL_INT           0
                LOAD_NAME               15 (_REPO_ROOT)
                CALL                     2
                POP_TOP

  34    L1:     LOAD_NAME                6 (sys)
                LOAD_ATTR               34 (stdout)
                LOAD_NAME                6 (sys)
                LOAD_ATTR               36 (stderr)
                BUILD_TUPLE              2
                GET_ITER
        L2:     FOR_ITER                22 (to L5)
                STORE_NAME              19 (_stream)

  35            NOP

  36    L3:     LOAD_NAME               19 (_stream)
                LOAD_ATTR               41 (reconfigure + NULL|self)
                LOAD_CONST               5 ('utf-8')
                LOAD_CONST               6 (('encoding',))
                CALL_KW                  1
                POP_TOP
        L4:     JUMP_BACKWARD           24 (to L2)

  34    L5:     END_FOR
                POP_ITER

  41            LOAD_SMALL_INT           0
                LOAD_CONST               7 (('SCENARIOS', 'get_scenario'))
                IMPORT_NAME             22 (app.services.simulation.scenarios)
                IMPORT_FROM             23 (SCENARIOS)
                STORE_NAME              23 (SCENARIOS)
                IMPORT_FROM             24 (get_scenario)
                STORE_NAME              24 (get_scenario)
                POP_TOP

  42            LOAD_SMALL_INT           0
                LOAD_CONST               8 (('STRATEGIES', 'get_strategy'))
                IMPORT_NAME             25 (app.services.optimization.strategies)
                IMPORT_FROM             26 (STRATEGIES)
                STORE_NAME              26 (STRATEGIES)
                IMPORT_FROM             27 (get_strategy)
                STORE_NAME              27 (get_strategy)
                POP_TOP

  46            LOAD_SMALL_INT           0
                LOAD_CONST               9 (('run_strategy_matrix',))
                IMPORT_NAME             28 (app.services.optimization.matrix_runner)
                IMPORT_FROM             29 (run_strategy_matrix)
                STORE_NAME              29 (run_strategy_matrix)
                POP_TOP

  47            LOAD_SMALL_INT           0
                LOAD_CONST              10 (('generate_optimization_report',))
                IMPORT_NAME             30 (app.services.optimization.report)
                IMPORT_FROM             31 (generate_optimization_report)
                STORE_NAME              31 (generate_optimization_report)
                POP_TOP

  48            LOAD_SMALL_INT           0
                LOAD_CONST              11 (('generate_recommendations', 'summarize_recommendations'))
                IMPORT_NAME             32 (app.services.optimization.recommendations)
                IMPORT_FROM             33 (generate_recommendations)
                STORE_NAME              33 (generate_recommendations)
                IMPORT_FROM             34 (summarize_recommendations)
                STORE_NAME              34 (summarize_recommendations)
                POP_TOP

  54            LOAD_CONST              12 ('matrix')
                LOAD_CONST               2 (None)
                LOAD_CONST              13 ('show_divergence')
                LOAD_CONST              14 (False)
                BUILD_MAP                2
                LOAD_CONST              15 (<code object __annotate__ at 0x0000018C18026130, file "scripts\run_optimization.py", line 54>)
                MAKE_FUNCTION
                LOAD_CONST              16 (<code object _human_summary at 0x0000018C17F2FDA0, file "scripts\run_optimization.py", line 54>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
                STORE_NAME              35 (_human_summary)

 166            LOAD_CONST              20 ((None,))
                LOAD_CONST              17 (<code object __annotate__ at 0x0000018C17FA31E0, file "scripts\run_optimization.py", line 166>)
                MAKE_FUNCTION
                LOAD_CONST              18 (<code object main at 0x0000018C181B0890, file "scripts\run_optimization.py", line 166>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                SET_FUNCTION_ATTRIBUTE   1 (defaults)
                STORE_NAME              36 (main)

 292            LOAD_NAME               37 (__name__)
                LOAD_CONST              19 ('__main__')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       14 (to L6)
                NOT_TAKEN

 293            LOAD_NAME               38 (SystemExit)
                PUSH_NULL
                LOAD_NAME               36 (main)
                PUSH_NULL
                CALL                     0
                CALL                     1
                RAISE_VARARGS            1

 292    L6:     LOAD_CONST               2 (None)
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

  37            LOAD_NAME               21 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L9)
                NOT_TAKEN
                POP_TOP

  38    L8:     POP_EXCEPT
                JUMP_BACKWARD          114 (to L2)

  37    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L7 [1]
  L7 to L8 -> L10 [2] lasti
  L9 to L10 -> L10 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026130, file "scripts\run_optimization.py", line 54>:
 54           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('report')
              LOAD_CONST               2 ('dict')
              LOAD_CONST               3 ('matrix')
              LOAD_CONST               4 ('Optional[dict]')
              LOAD_CONST               5 ('show_divergence')
              LOAD_CONST               6 ('bool')
              LOAD_CONST               7 ('return')
              LOAD_CONST               8 ('str')
              BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object _human_summary at 0x0000018C17F2FDA0, file "scripts\run_optimization.py", line 54>:
 54            RESUME                   0

 55            BUILD_LIST               0
               STORE_FAST               3 (lines)

 56            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              98 ('==============================================================================')
               CALL                     1
               POP_TOP

 57            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST               1 ('OPTIMIZATION REPORT')
               CALL                     1
               POP_TOP

 58            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST               2 ('  ')
               LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST               3 ('headline')
               CALL                     1
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

 59            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST               4 ('')
               CALL                     1
               POP_TOP

 61            LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST               5 ('metrics')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               BUILD_MAP                0
       L1:     STORE_FAST               4 (metrics)

 62            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST               6 ('MATRIX METRICS')
               CALL                     1
               POP_TOP

 63            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST               7 ('  total runs:        ')
               LOAD_FAST_BORROW         4 (metrics)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST               8 ('total_runs')
               LOAD_SMALL_INT           0
               CALL                     2
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

 64            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST               9 ('  pass rate:         ')
               LOAD_FAST_BORROW         4 (metrics)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              10 ('pass_rate')
               LOAD_SMALL_INT           0
               CALL                     2
               LOAD_CONST              11 ('.0%')
               FORMAT_WITH_SPEC
               BUILD_STRING             2
               CALL                     1
               POP_TOP

 65            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              12 ('  avg replay score:  ')
               LOAD_FAST_BORROW         4 (metrics)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              13 ('average_replay_score')
               LOAD_SMALL_INT           0
               CALL                     2
               FORMAT_SIMPLE
               LOAD_CONST              14 ('/100')
               BUILD_STRING             3
               CALL                     1
               POP_TOP

 66            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              15 ('  avg turns:         ')
               LOAD_FAST_BORROW         4 (metrics)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              16 ('average_turns')
               LOAD_SMALL_INT           0
               CALL                     2
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

 67            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              17 ('  errors:            ')
               LOAD_FAST_BORROW         4 (metrics)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              18 ('error_count')
               LOAD_SMALL_INT           0
               CALL                     2
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

 68            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST               4 ('')
               CALL                     1
               POP_TOP

 71            LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              19 ('behavior_summary')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               BUILD_MAP                0
       L2:     STORE_FAST               5 (bs)

 72            LOAD_FAST_BORROW         5 (bs)
               TO_BOOL
               POP_JUMP_IF_FALSE      253 (to L3)
               NOT_TAKEN

 73            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              20 ('BEHAVIOURAL SUMMARY')
               CALL                     1
               POP_TOP

 74            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              21 ('  avg trust:         ')
               LOAD_FAST_BORROW         5 (bs)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              22 ('avg_trust')
               CALL                     1
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

 75            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              23 ('  avg frustration:   ')
               LOAD_FAST_BORROW         5 (bs)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              24 ('avg_frustration')
               CALL                     1
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

 76            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              25 ('  divergence rate:   ')
               LOAD_FAST_BORROW         5 (bs)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              26 ('divergence_rate')
               LOAD_SMALL_INT           0
               CALL                     2
               LOAD_CONST              11 ('.0%')
               FORMAT_WITH_SPEC
               BUILD_STRING             2
               CALL                     1
               POP_TOP

 77            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              27 ('  escalation rate:   ')
               LOAD_FAST_BORROW         5 (bs)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              28 ('escalation_rate')
               LOAD_SMALL_INT           0
               CALL                     2
               LOAD_CONST              11 ('.0%')
               FORMAT_WITH_SPEC
               BUILD_STRING             2
               CALL                     1
               POP_TOP

 78            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              29 ('  drop-off rate:     ')
               LOAD_FAST_BORROW         5 (bs)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              30 ('dropoff_rate')
               LOAD_SMALL_INT           0
               CALL                     2
               LOAD_CONST              11 ('.0%')
               FORMAT_WITH_SPEC
               BUILD_STRING             2
               CALL                     1
               POP_TOP

 79            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              31 ('  recovery rate:     ')
               LOAD_FAST_BORROW         5 (bs)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              32 ('recovery_rate')
               LOAD_SMALL_INT           0
               CALL                     2
               LOAD_CONST              11 ('.0%')
               FORMAT_WITH_SPEC
               BUILD_STRING             2
               CALL                     1
               POP_TOP

 80            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST               4 ('')
               CALL                     1
               POP_TOP

 82    L3:     LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              33 ('ranked_strategies')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               POP_TOP
               BUILD_LIST               0
       L4:     STORE_FAST               6 (ranked)

 83            LOAD_FAST_BORROW         6 (ranked)
               TO_BOOL
               POP_JUMP_IF_FALSE      202 (to L13)
               NOT_TAKEN

 84            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              34 ('RANKED STRATEGIES (best → worst)')
               CALL                     1
               POP_TOP

 85            LOAD_FAST_BORROW         6 (ranked)
               GET_ITER
       L5:     FOR_ITER               161 (to L12)
               STORE_FAST               7 (r)

 86            LOAD_FAST_BORROW         7 (r)
               LOAD_CONST              35 ('components')
               BINARY_OP               26 ([])
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              36 ('effective')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L6)
               NOT_TAKEN
               LOAD_CONST              37 ('[eff]')
               JUMP_FORWARD             1 (to L7)
       L6:     LOAD_CONST              38 ('[infra]')
       L7:     STORE_FAST               8 (tag)

 87            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)

 88            LOAD_CONST              39 ('  #')
               LOAD_FAST_BORROW         7 (r)
               LOAD_CONST              40 ('rank')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               LOAD_CONST              41 (' ')
               LOAD_FAST_BORROW         7 (r)
               LOAD_CONST              42 ('strategy_id')
               BINARY_OP               26 ([])
               LOAD_CONST              43 ('<25')
               FORMAT_WITH_SPEC
               LOAD_CONST              44 ('  score=')

 89            LOAD_FAST_BORROW         7 (r)
               LOAD_CONST              45 ('score')
               BINARY_OP               26 ([])
               LOAD_CONST              46 ('6.2f')
               FORMAT_WITH_SPEC
               LOAD_CONST               2 ('  ')
               LOAD_FAST_BORROW         8 (tag)
               FORMAT_SIMPLE

 88            BUILD_STRING             8

 87            CALL                     1
               POP_TOP

 91            LOAD_FAST_BORROW         7 (r)
               LOAD_CONST              47 ('strengths')
               BINARY_OP               26 ([])
               GET_ITER
       L8:     FOR_ITER                23 (to L9)
               STORE_FAST               9 (s)

 92            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              48 ('        + ')
               LOAD_FAST_BORROW         9 (s)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           25 (to L8)

 91    L9:     END_FOR
               POP_ITER

 93            LOAD_FAST_BORROW         7 (r)
               LOAD_CONST              49 ('weaknesses')
               BINARY_OP               26 ([])
               GET_ITER
      L10:     FOR_ITER                23 (to L11)
               STORE_FAST              10 (w)

 94            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              50 ('        - ')
               LOAD_FAST_BORROW        10 (w)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           25 (to L10)

 93   L11:     END_FOR
               POP_ITER
               JUMP_BACKWARD          163 (to L5)

 85   L12:     END_FOR
               POP_ITER

 95            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST               4 ('')
               CALL                     1
               POP_TOP

 97   L13:     LOAD_FAST_BORROW         4 (metrics)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              51 ('by_strategy')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L14)
               NOT_TAKEN
               POP_TOP
               BUILD_MAP                0
      L14:     STORE_FAST              11 (by_strategy)

 98            LOAD_FAST_BORROW        11 (by_strategy)
               TO_BOOL
               POP_JUMP_IF_FALSE      161 (to L17)
               NOT_TAKEN

 99            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              52 ('PER-STRATEGY OUTCOME RATES')
               CALL                     1
               POP_TOP

100            LOAD_GLOBAL              5 (sorted + NULL)
               LOAD_FAST_BORROW        11 (by_strategy)
               CALL                     1
               GET_ITER
      L15:     FOR_ITER               111 (to L16)
               STORE_FAST              12 (sid)

101            LOAD_FAST_BORROW_LOAD_FAST_BORROW 188 (by_strategy, sid)
               BINARY_OP               26 ([])
               STORE_FAST              13 (entry)

102            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)

103            LOAD_CONST              53 ('  - ')
               LOAD_FAST_BORROW        12 (sid)
               FORMAT_SIMPLE
               LOAD_CONST              54 (': booked=')
               LOAD_FAST_BORROW        13 (entry)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              55 ('booked_rate')
               LOAD_SMALL_INT           0
               CALL                     2
               LOAD_CONST              11 ('.0%')
               FORMAT_WITH_SPEC
               LOAD_CONST              56 (' callback=')

104            LOAD_FAST_BORROW        13 (entry)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              57 ('callback_rate')
               LOAD_SMALL_INT           0
               CALL                     2
               LOAD_CONST              11 ('.0%')
               FORMAT_WITH_SPEC
               LOAD_CONST              58 (' not_booked=')

105            LOAD_FAST_BORROW        13 (entry)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              59 ('not_booked_rate')
               LOAD_SMALL_INT           0
               CALL                     2
               LOAD_CONST              11 ('.0%')
               FORMAT_WITH_SPEC
               LOAD_CONST              60 (' transferred=')

106            LOAD_FAST_BORROW        13 (entry)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              61 ('transferred_rate')
               LOAD_SMALL_INT           0
               CALL                     2
               LOAD_CONST              11 ('.0%')
               FORMAT_WITH_SPEC

103            BUILD_STRING            10

102            CALL                     1
               POP_TOP
               JUMP_BACKWARD          113 (to L15)

100   L16:     END_FOR
               POP_ITER

108            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST               4 ('')
               CALL                     1
               POP_TOP

111   L17:     LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              62 ('personality_insights')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L18)
               NOT_TAKEN
               POP_TOP
               BUILD_MAP                0
      L18:     STORE_FAST              14 (pi)

112            LOAD_FAST_BORROW        14 (pi)
               TO_BOOL
               POP_JUMP_IF_FALSE      156 (to L21)
               NOT_TAKEN

113            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              63 ('STRATEGY ↔ PERSONALITY FIT')
               CALL                     1
               POP_TOP

114            LOAD_GLOBAL              5 (sorted + NULL)
               LOAD_FAST_BORROW        14 (pi)
               CALL                     1
               GET_ITER
      L19:     FOR_ITER               106 (to L20)
               STORE_FAST              12 (sid)

115            LOAD_FAST_BORROW_LOAD_FAST_BORROW 236 (pi, sid)
               BINARY_OP               26 ([])
               STORE_FAST              15 (info)

116            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)

117            LOAD_CONST              53 ('  - ')
               LOAD_FAST_BORROW        12 (sid)
               FORMAT_SIMPLE
               LOAD_CONST              64 (': best=')
               LOAD_FAST_BORROW        15 (info)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              65 ('best_personality')
               CALL                     1
               FORMAT_SIMPLE
               LOAD_CONST              66 (' (pass ')

118            LOAD_FAST_BORROW        15 (info)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              67 ('best_pass_rate')
               CALL                     1
               LOAD_CONST              11 ('.0%')
               FORMAT_WITH_SPEC
               LOAD_CONST              68 ('), worst=')

119            LOAD_FAST_BORROW        15 (info)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              69 ('worst_personality')
               CALL                     1
               FORMAT_SIMPLE
               LOAD_CONST              66 (' (pass ')

120            LOAD_FAST_BORROW        15 (info)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              70 ('worst_pass_rate')
               CALL                     1
               LOAD_CONST              11 ('.0%')
               FORMAT_WITH_SPEC
               LOAD_CONST              71 (')')

117            BUILD_STRING            11

116            CALL                     1
               POP_TOP
               JUMP_BACKWARD          108 (to L19)

114   L20:     END_FOR
               POP_ITER

122            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST               4 ('')
               CALL                     1
               POP_TOP

125   L21:     LOAD_FAST_BORROW         2 (show_divergence)
               TO_BOOL
               EXTENDED_ARG             1
               POP_JUMP_IF_FALSE      404 (to L32)
               NOT_TAKEN
               LOAD_FAST_BORROW         1 (matrix)
               TO_BOOL
               EXTENDED_ARG             1
               POP_JUMP_IF_FALSE      395 (to L32)
               NOT_TAKEN

126            BUILD_LIST               0
               STORE_FAST              16 (actions)

127            LOAD_FAST_BORROW         1 (matrix)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              72 ('results')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L22)
               NOT_TAKEN
               POP_TOP
               BUILD_LIST               0
      L22:     GET_ITER
      L23:     FOR_ITER                45 (to L25)
               STORE_FAST               7 (r)

128            LOAD_FAST_BORROW         7 (r)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              73 ('divergence_triggered')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L24)
               NOT_TAKEN
               JUMP_BACKWARD           28 (to L23)

129   L24:     LOAD_FAST_BORROW        16 (actions)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_FAST_BORROW         7 (r)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           47 (to L23)

127   L25:     END_FOR
               POP_ITER

130            LOAD_FAST_BORROW        16 (actions)
               TO_BOOL
               EXTENDED_ARG             1
               POP_JUMP_IF_FALSE      257 (to L31)
               NOT_TAKEN

131            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              74 ('DIVERGENT CELLS')
               CALL                     1
               POP_TOP

132            LOAD_FAST_BORROW        16 (actions)
               GET_ITER
      L26:     FOR_ITER               215 (to L30)
               STORE_FAST               7 (r)

133            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)

134            LOAD_CONST              53 ('  - ')
               LOAD_FAST_BORROW         7 (r)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              75 ('scenario_id')
               CALL                     1
               FORMAT_SIMPLE
               LOAD_CONST              76 (' × ')
               LOAD_FAST_BORROW         7 (r)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              42 ('strategy_id')
               CALL                     1
               FORMAT_SIMPLE
               LOAD_CONST              77 (': outcome=')

135            LOAD_FAST_BORROW         7 (r)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              78 ('actual_outcome')
               CALL                     1
               FORMAT_SIMPLE
               LOAD_CONST              79 (' trust=')

136            LOAD_FAST_BORROW         7 (r)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              80 ('trust_score')
               CALL                     1
               FORMAT_SIMPLE
               LOAD_CONST              81 (' frust=')

137            LOAD_FAST_BORROW         7 (r)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              82 ('frustration_score')
               CALL                     1
               FORMAT_SIMPLE
               LOAD_CONST              83 (' state=')

138            LOAD_FAST_BORROW         7 (r)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              84 ('final_behavior_state')
               CALL                     1
               FORMAT_SIMPLE

134            BUILD_STRING            12

133            CALL                     1
               POP_TOP

140            LOAD_FAST_BORROW         7 (r)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              85 ('divergence_actions')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L27)
               NOT_TAKEN
               POP_TOP
               BUILD_LIST               0
      L27:     GET_ITER
      L28:     FOR_ITER                56 (to L29)
               STORE_FAST              17 (a)

141            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              86 ('        · turn ')
               LOAD_FAST_BORROW        17 (a)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              87 ('turn')
               CALL                     1
               FORMAT_SIMPLE
               LOAD_CONST              88 (': ')
               LOAD_FAST_BORROW        17 (a)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              89 ('action')
               CALL                     1
               FORMAT_SIMPLE
               BUILD_STRING             4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           58 (to L28)

140   L29:     END_FOR
               POP_ITER
               JUMP_BACKWARD          217 (to L26)

132   L30:     END_FOR
               POP_ITER

142            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST               4 ('')
               CALL                     1
               POP_TOP
               JUMP_FORWARD            51 (to L32)

144   L31:     LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              74 ('DIVERGENT CELLS')
               CALL                     1
               POP_TOP

145            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              90 ('  (no divergence in this matrix)')
               CALL                     1
               POP_TOP

146            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST               4 ('')
               CALL                     1
               POP_TOP

148   L32:     LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              91 ('warnings')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L33)
               NOT_TAKEN
               POP_TOP
               BUILD_LIST               0
      L33:     STORE_FAST              18 (warnings)

149            LOAD_FAST_BORROW        18 (warnings)
               TO_BOOL
               POP_JUMP_IF_FALSE       64 (to L36)
               NOT_TAKEN

150            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              92 ('WARNINGS')
               CALL                     1
               POP_TOP

151            LOAD_FAST_BORROW        18 (warnings)
               GET_ITER
      L34:     FOR_ITER                23 (to L35)
               STORE_FAST              10 (w)

152            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              93 ('  ! ')
               LOAD_FAST_BORROW        10 (w)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           25 (to L34)

151   L35:     END_FOR
               POP_ITER

153            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST               4 ('')
               CALL                     1
               POP_TOP

155   L36:     LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              94 ('recommendations')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L37)
               NOT_TAKEN
               POP_TOP
               BUILD_LIST               0
      L37:     STORE_FAST              19 (recs)

156            LOAD_FAST_BORROW        19 (recs)
               TO_BOOL
               POP_JUMP_IF_FALSE       64 (to L40)
               NOT_TAKEN

157            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              95 ('RECOMMENDATIONS')
               CALL                     1
               POP_TOP

158            LOAD_FAST_BORROW        19 (recs)
               GET_ITER
      L38:     FOR_ITER                23 (to L39)
               STORE_FAST               7 (r)

159            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              96 ('  • ')
               LOAD_FAST_BORROW         7 (r)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           25 (to L38)

158   L39:     END_FOR
               POP_ITER

160            LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST               4 ('')
               CALL                     1
               POP_TOP

162   L40:     LOAD_FAST_BORROW         3 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              98 ('==============================================================================')
               CALL                     1
               POP_TOP

163            LOAD_CONST              97 ('\n')
               LOAD_ATTR                7 (join + NULL|self)
               LOAD_FAST_BORROW         3 (lines)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "scripts\run_optimization.py", line 166>:
166           RESUME                   0
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

Disassembly of <code object main at 0x0000018C181B0890, file "scripts\run_optimization.py", line 166>:
 166            RESUME                   0

 167            LOAD_GLOBAL              0 (argparse)
                LOAD_ATTR                2 (ArgumentParser)
                PUSH_NULL

 168            LOAD_CONST               0 ('run_optimization')

 169            LOAD_CONST               1 ('Run the strategy × scenario matrix and rank strategy variants.')

 167            LOAD_CONST               2 (('prog', 'description'))
                CALL_KW                  2
                STORE_FAST               1 (parser)

 171            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)

 172            LOAD_CONST               3 ('--scenario')

 173            LOAD_CONST               4 (None)

 174            LOAD_CONST               5 ('Restrict matrix to one scenario id.')

 171            LOAD_CONST               6 (('default', 'help'))
                CALL_KW                  3
                POP_TOP

 176            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)

 177            LOAD_CONST               7 ('--strategy')

 178            LOAD_CONST               4 (None)

 179            LOAD_CONST               8 ('Restrict matrix to one strategy id.')

 176            LOAD_CONST               6 (('default', 'help'))
                CALL_KW                  3
                POP_TOP

 181            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)

 182            LOAD_CONST               9 ('--limit-scenarios')

 183            LOAD_GLOBAL              6 (int)

 184            LOAD_CONST               4 (None)

 185            LOAD_CONST              10 ('Cap scenarios after --scenario filter.')

 181            LOAD_CONST              11 (('type', 'default', 'help'))
                CALL_KW                  4
                POP_TOP

 187            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)

 188            LOAD_CONST              12 ('--limit-strategies')

 189            LOAD_GLOBAL              6 (int)

 190            LOAD_CONST               4 (None)

 191            LOAD_CONST              13 ('Cap strategies after --strategy filter.')

 187            LOAD_CONST              11 (('type', 'default', 'help'))
                CALL_KW                  4
                POP_TOP

 193            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)

 194            LOAD_CONST              14 ('--brokerage-id')

 195            LOAD_CONST              15 ('demo')

 196            LOAD_CONST              16 ('Brokerage id attributed to simulated calls (default: demo).')

 193            LOAD_CONST               6 (('default', 'help'))
                CALL_KW                  3
                POP_TOP

 198            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)

 199            LOAD_CONST              17 ('--personality')

 200            LOAD_CONST               4 (None)

 201            LOAD_CONST              18 ('PAS143B — restrict matrix to scenarios with this personality_id.')

 198            LOAD_CONST               6 (('default', 'help'))
                CALL_KW                  3
                POP_TOP

 203            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)

 204            LOAD_CONST              19 ('--show-divergence')

 205            LOAD_CONST              20 ('store_true')

 206            LOAD_CONST              21 ('PAS143B — print per-cell divergence actions (drops / escalations / booking flips) in the human view.')

 203            LOAD_CONST              22 (('action', 'help'))
                CALL_KW                  3
                POP_TOP

 209            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)

 210            LOAD_CONST              23 ('--recommendations')

 211            LOAD_CONST              20 ('store_true')

 212            LOAD_CONST              24 ('PAS143C — print plain-English recommendations (the broker-facing summary) at the end of the human view.')

 209            LOAD_CONST              22 (('action', 'help'))
                CALL_KW                  3
                POP_TOP

 215            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)

 216            LOAD_CONST              25 ('--json')

 217            LOAD_CONST              20 ('store_true')

 218            LOAD_CONST              26 ('Emit matrix + report + recommendations as JSON instead of the human view.')

 215            LOAD_CONST              22 (('action', 'help'))
                CALL_KW                  3
                POP_TOP

 220            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                9 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 223            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               10 (scenario)
                TO_BOOL
                POP_JUMP_IF_FALSE       72 (to L2)
                NOT_TAKEN

 224            LOAD_GLOBAL             13 (get_scenario + NULL)
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               10 (scenario)
                CALL                     1
                STORE_FAST               3 (s)

 225            LOAD_FAST_BORROW         3 (s)
                POP_JUMP_IF_NOT_NONE    43 (to L1)
                NOT_TAKEN

 226            LOAD_GLOBAL             15 (print + NULL)
                LOAD_CONST              27 ('Unknown scenario id: ')
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               10 (scenario)
                FORMAT_SIMPLE
                BUILD_STRING             2
                LOAD_GLOBAL             16 (sys)
                LOAD_ATTR               18 (stderr)
                LOAD_CONST              28 (('file',))
                CALL_KW                  2
                POP_TOP

 227            LOAD_SMALL_INT           1
                RETURN_VALUE

 228    L1:     LOAD_FAST_BORROW         3 (s)
                BUILD_LIST               1
                STORE_FAST               4 (scenarios)
                JUMP_FORWARD            15 (to L3)

 230    L2:     LOAD_GLOBAL             21 (list + NULL)
                LOAD_GLOBAL             22 (SCENARIOS)
                CALL                     1
                STORE_FAST               4 (scenarios)

 232    L3:     LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               24 (personality)
                TO_BOOL
                POP_JUMP_IF_FALSE       98 (to L10)
                NOT_TAKEN

 233            LOAD_FAST_BORROW         4 (scenarios)
                GET_ITER
                LOAD_FAST_AND_CLEAR      3 (s)
                SWAP                     2
        L4:     BUILD_LIST               0
                SWAP                     2
        L5:     FOR_ITER                33 (to L8)
                STORE_FAST_LOAD_FAST    51 (s, s)
                LOAD_ATTR               26 (personality_id)
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               24 (personality)
                COMPARE_OP              88 (bool(==))
        L6:     POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                JUMP_BACKWARD           31 (to L5)
        L7:     LOAD_FAST_BORROW         3 (s)
                LIST_APPEND              2
                JUMP_BACKWARD           35 (to L5)
        L8:     END_FOR
                POP_ITER
        L9:     STORE_FAST               4 (scenarios)
                STORE_FAST               3 (s)

 234            LOAD_FAST_BORROW         4 (scenarios)
                TO_BOOL
                POP_JUMP_IF_TRUE        45 (to L10)
                NOT_TAKEN

 235            LOAD_GLOBAL             15 (print + NULL)

 236            LOAD_CONST              29 ('No scenarios match personality_id=')
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               24 (personality)
                CONVERT_VALUE            2 (repr)
                FORMAT_SIMPLE
                LOAD_CONST              30 ('.')
                BUILD_STRING             3

 237            LOAD_GLOBAL             16 (sys)
                LOAD_ATTR               18 (stderr)

 235            LOAD_CONST              28 (('file',))
                CALL_KW                  2
                POP_TOP

 239            LOAD_SMALL_INT           1
                RETURN_VALUE

 240   L10:     LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               28 (limit_scenarios)
                POP_JUMP_IF_NONE        33 (to L11)
                NOT_TAKEN
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               28 (limit_scenarios)
                LOAD_SMALL_INT           0
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE       16 (to L11)
                NOT_TAKEN

 241            LOAD_FAST_BORROW         4 (scenarios)
                LOAD_CONST               4 (None)
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               28 (limit_scenarios)
                BINARY_SLICE
                STORE_FAST               4 (scenarios)

 244   L11:     LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               30 (strategy)
                TO_BOOL
                POP_JUMP_IF_FALSE       72 (to L13)
                NOT_TAKEN

 245            LOAD_GLOBAL             33 (get_strategy + NULL)
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               30 (strategy)
                CALL                     1
                STORE_FAST               5 (st)

 246            LOAD_FAST_BORROW         5 (st)
                POP_JUMP_IF_NOT_NONE    43 (to L12)
                NOT_TAKEN

 247            LOAD_GLOBAL             15 (print + NULL)
                LOAD_CONST              31 ('Unknown strategy id: ')
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               30 (strategy)
                FORMAT_SIMPLE
                BUILD_STRING             2
                LOAD_GLOBAL             16 (sys)
                LOAD_ATTR               18 (stderr)
                LOAD_CONST              28 (('file',))
                CALL_KW                  2
                POP_TOP

 248            LOAD_SMALL_INT           1
                RETURN_VALUE

 249   L12:     LOAD_FAST_BORROW         5 (st)
                BUILD_LIST               1
                STORE_FAST               6 (strategies)
                JUMP_FORWARD            15 (to L14)

 251   L13:     LOAD_GLOBAL             21 (list + NULL)
                LOAD_GLOBAL             34 (STRATEGIES)
                CALL                     1
                STORE_FAST               6 (strategies)

 252   L14:     LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               36 (limit_strategies)
                POP_JUMP_IF_NONE        33 (to L15)
                NOT_TAKEN
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               36 (limit_strategies)
                LOAD_SMALL_INT           0
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE       16 (to L15)
                NOT_TAKEN

 253            LOAD_FAST_BORROW         6 (strategies)
                LOAD_CONST               4 (None)
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               36 (limit_strategies)
                BINARY_SLICE
                STORE_FAST               6 (strategies)

 255   L15:     LOAD_FAST_BORROW         4 (scenarios)
                TO_BOOL
                POP_JUMP_IF_FALSE        9 (to L16)
                NOT_TAKEN
                LOAD_FAST_BORROW         6 (strategies)
                TO_BOOL
                POP_JUMP_IF_TRUE        30 (to L17)
                NOT_TAKEN

 256   L16:     LOAD_GLOBAL             15 (print + NULL)
                LOAD_CONST              32 ('Empty matrix after filters — nothing to run.')
                LOAD_GLOBAL             16 (sys)
                LOAD_ATTR               18 (stderr)
                LOAD_CONST              28 (('file',))
                CALL_KW                  2
                POP_TOP

 257            LOAD_SMALL_INT           1
                RETURN_VALUE

 259   L17:     LOAD_GLOBAL             39 (run_strategy_matrix + NULL)

 260            LOAD_FAST_BORROW_LOAD_FAST_BORROW 70 (scenarios, strategies)

 261            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               40 (brokerage_id)

 259            LOAD_CONST              33 (('brokerage_id',))
                CALL_KW                  3
                STORE_FAST               7 (matrix)

 263            LOAD_GLOBAL             43 (generate_optimization_report + NULL)
                LOAD_FAST_BORROW         7 (matrix)
                CALL                     1
                STORE_FAST               8 (report)

 267            LOAD_GLOBAL             45 (generate_recommendations + NULL)
                LOAD_FAST_BORROW         8 (report)
                CALL                     1
                STORE_FAST               9 (recommendations)

 269            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               46 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       49 (to L18)
                NOT_TAKEN

 271            LOAD_CONST              34 ('matrix')
                LOAD_FAST_BORROW         7 (matrix)

 272            LOAD_CONST              35 ('report')
                LOAD_FAST_BORROW         8 (report)

 273            LOAD_CONST              36 ('recommendations')
                LOAD_FAST_BORROW         9 (recommendations)

 270            BUILD_MAP                3
                STORE_FAST              10 (out)

 275            LOAD_GLOBAL             15 (print + NULL)
                LOAD_GLOBAL             46 (json)
                LOAD_ATTR               48 (dumps)
                PUSH_NULL
                LOAD_FAST_BORROW        10 (out)
                LOAD_GLOBAL             50 (str)
                LOAD_SMALL_INT           2
                LOAD_CONST              37 (('default', 'indent'))
                CALL_KW                  3
                CALL                     1
                POP_TOP

 289            LOAD_SMALL_INT           0
                RETURN_VALUE

 277   L18:     LOAD_GLOBAL             15 (print + NULL)
                CALL                     0
                POP_TOP

 278            LOAD_GLOBAL             15 (print + NULL)

 279            LOAD_CONST              38 ('Running ')
                LOAD_GLOBAL             53 (len + NULL)
                LOAD_FAST_BORROW         4 (scenarios)
                CALL                     1
                FORMAT_SIMPLE
                LOAD_CONST              39 (' scenario(s) × ')
                LOAD_GLOBAL             53 (len + NULL)
                LOAD_FAST_BORROW         6 (strategies)
                CALL                     1
                FORMAT_SIMPLE
                LOAD_CONST              40 (' strategy(ies) = ')

 280            LOAD_FAST_BORROW         7 (matrix)
                LOAD_ATTR               55 (get + NULL|self)
                LOAD_CONST              41 ('total_runs')
                LOAD_SMALL_INT           0
                CALL                     2
                FORMAT_SIMPLE
                LOAD_CONST              42 (" cell(s) against brokerage='")

 281            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               40 (brokerage_id)
                FORMAT_SIMPLE
                LOAD_CONST              43 ("'")

 279            BUILD_STRING             9

 278            CALL                     1
                POP_TOP

 283            LOAD_GLOBAL             15 (print + NULL)
                LOAD_GLOBAL             57 (_human_summary + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 135 (report, matrix)
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               58 (show_divergence)
                LOAD_CONST              44 (('matrix', 'show_divergence'))
                CALL_KW                  3
                CALL                     1
                POP_TOP

 284            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               60 (recommendations)
                TO_BOOL
                POP_JUMP_IF_FALSE       42 (to L19)
                NOT_TAKEN

 285            LOAD_GLOBAL             15 (print + NULL)
                CALL                     0
                POP_TOP

 286            LOAD_GLOBAL             15 (print + NULL)
                LOAD_CONST              45 ('RECOMMENDATIONS')
                CALL                     1
                POP_TOP

 287            LOAD_GLOBAL             15 (print + NULL)
                LOAD_GLOBAL             63 (summarize_recommendations + NULL)
                LOAD_FAST_BORROW         9 (recommendations)
                CALL                     1
                CALL                     1
                POP_TOP

 289   L19:     LOAD_SMALL_INT           0
                RETURN_VALUE

  --   L20:     SWAP                     2
                POP_TOP

 233            SWAP                     2
                STORE_FAST               3 (s)
                RERAISE                  0
ExceptionTable:
  L4 to L6 -> L20 [2]
  L7 to L9 -> L20 [2]
```
