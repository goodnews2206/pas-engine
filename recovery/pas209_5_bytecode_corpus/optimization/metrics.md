# optimization/metrics

- **pyc:** `app\services\optimization\__pycache__\metrics.cpython-314.pyc`
- **expected source path (absent):** `app\services\optimization/metrics.py`
- **co_filename (from bytecode):** `app\services\optimization\metrics.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** optimization

## Module docstring

```
PAS143A — Pure aggregation over a matrix of scenario × strategy results.

No I/O, no LLMs, no randomness. Same input always produces the same
output dict — feeds ranking.py and report.py.
```

## Imports

`Counter`, `Dict`, `List`, `collections`, `mean`, `statistics`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_bucket`, `_by_scenario`, `_by_strategy`, `_by_strategy_personality`, `_empty_metrics`, `_frust`, `_score`, `_strategy_outcome_rates`, `_trust`, `compute_matrix_metrics`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS143A — Pure aggregation over a matrix of scenario × strategy results.\n\nNo I/O, no LLMs, no randomness. Same input always produces the same\noutput dict — feeds ranking.py and report.py.\n'
- 'matrix_result'
- 'return'
- '\nAggregate a `run_strategy_matrix` result. Returns the legacy\nPAS143A keys plus PAS143B behavioural rollups:\n\n  legacy:\n    total_runs, pass_rate, average_replay_score, average_turns,\n    outcome_breakdown, by_strategy, by_scenario,\n    strategy_outcome_rates, missing_lifecycle_frequency, error_count\n\n  PAS143B:\n    average_trust_score, average_frustration_score,\n    divergence_rate, escalation_rate, dropoff_rate, recovery_rate,\n    by_strategy[*].trust_avg, frustration_avg, divergence_count,\n    by_strategy_personality:\n      { strategy_id: { personality_id: {n, passed, booked, replay_avg,\n                                        divergence_count} } }\n\nNever raises. Empty / malformed input collapses to a zero shape.\n'
- 'results'
- 'transcript'
- 'evaluation'
- 'missing_steps'
- 'personality_id'
- 'total_runs'
- 'pass_rate'
- 'average_replay_score'
- 'average_turns'
- 'outcome_breakdown'
- 'by_strategy'
- 'by_scenario'
- 'strategy_outcome_rates'
- 'missing_lifecycle_frequency'
- 'error_count'
- 'average_trust_score'
- 'average_frustration_score'
- 'divergence_rate'
- 'escalation_rate'
- 'dropoff_rate'
- 'recovery_rate'
- 'by_strategy_personality'
- 'passed'
- 'cell_error'
- 'error'
- 'actual_outcome'
- 'divergence_triggered'
- 'divergence_actions'
- 'action'
- 'lead_escalated'
- 'lead_dropped'
- 'final_behavior_state'
- 'engaged'
- 'trust_score'
- 'replay_score'
- 'rows'
- 'strategy_id'
- 'booked'
- 'callback_requested'
- 'qualified_callback_requested'
- 'not_booked'
- 'transferred'
- 'avg_replay_score'
- 'avg_turns'
- 'errors'
- 'outcome_counts'
- 'booked_rate'
- 'callback_rate'
- 'not_booked_rate'
- 'transferred_rate'
- 'effective'
- 'trust_avg'
- 'frustration_avg'
- 'divergence_count'
- 'strategy_effective'
- '\nCross-tab strategy × personality. Drives the report\'s\n"best/worst personality per strategy" insight.\n'
- 'replay_total'
- 'replay_avg'
- 'frustration_score'
- 'scenario_id'
- 'Per-strategy outcome → rate (0..1) projection. Useful for heatmaps.'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS143A — Pure aggregation over a matrix of scenario × strategy results.\n\nNo I/O, no LLMs, no randomness. Same input always produces the same\noutput dict — feeds ranking.py and report.py.\n')
              STORE_NAME               0 (__doc__)

  8           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('Counter',))
              IMPORT_NAME              1 (collections)
              IMPORT_FROM              2 (Counter)
              STORE_NAME               2 (Counter)
              POP_TOP

  9           LOAD_SMALL_INT           0
              LOAD_CONST               2 (('mean',))
              IMPORT_NAME              3 (statistics)
              IMPORT_FROM              4 (mean)
              STORE_NAME               4 (mean)
              POP_TOP

 10           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('Dict', 'List'))
              IMPORT_NAME              5 (typing)
              IMPORT_FROM              6 (Dict)
              STORE_NAME               6 (Dict)
              IMPORT_FROM              7 (List)
              STORE_NAME               7 (List)
              POP_TOP

 13           LOAD_CONST               4 (<code object __annotate__ at 0x0000018C18025130, file "app\services\optimization\metrics.py", line 13>)
              MAKE_FUNCTION
              LOAD_CONST               5 (<code object compute_matrix_metrics at 0x0000018C181A2E40, file "app\services\optimization\metrics.py", line 13>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME               8 (compute_matrix_metrics)

113           LOAD_CONST               6 (<code object __annotate__ at 0x0000018C18026130, file "app\services\optimization\metrics.py", line 113>)
              MAKE_FUNCTION
              LOAD_CONST               7 (<code object _score at 0x0000018C17F96420, file "app\services\optimization\metrics.py", line 113>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME               9 (_score)

118           LOAD_CONST               8 (<code object _bucket at 0x0000018C18010DF0, file "app\services\optimization\metrics.py", line 118>)
              MAKE_FUNCTION
              STORE_NAME              10 (_bucket)

128           LOAD_CONST               9 (<code object __annotate__ at 0x0000018C18053630, file "app\services\optimization\metrics.py", line 128>)
              MAKE_FUNCTION
              LOAD_CONST              10 (<code object _by_strategy at 0x0000018C17D7CA60, file "app\services\optimization\metrics.py", line 128>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              11 (_by_strategy)

175           LOAD_CONST              11 (<code object __annotate__ at 0x0000018C18053BD0, file "app\services\optimization\metrics.py", line 175>)
              MAKE_FUNCTION
              LOAD_CONST              12 (<code object _by_strategy_personality at 0x0000018C17D7EE90, file "app\services\optimization\metrics.py", line 175>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              12 (_by_strategy_personality)

212           LOAD_CONST              13 (<code object __annotate__ at 0x0000018C18026230, file "app\services\optimization\metrics.py", line 212>)
              MAKE_FUNCTION
              LOAD_CONST              14 (<code object _trust at 0x0000018C18038B70, file "app\services\optimization\metrics.py", line 212>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              13 (_trust)

217           LOAD_CONST              15 (<code object __annotate__ at 0x0000018C18025A30, file "app\services\optimization\metrics.py", line 217>)
              MAKE_FUNCTION
              LOAD_CONST              16 (<code object _frust at 0x0000018C180388F0, file "app\services\optimization\metrics.py", line 217>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              14 (_frust)

222           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C180533F0, file "app\services\optimization\metrics.py", line 222>)
              MAKE_FUNCTION
              LOAD_CONST              18 (<code object _by_scenario at 0x0000018C17ECE910, file "app\services\optimization\metrics.py", line 222>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              15 (_by_scenario)

240           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C18024B30, file "app\services\optimization\metrics.py", line 240>)
              MAKE_FUNCTION
              LOAD_CONST              20 (<code object _strategy_outcome_rates at 0x0000018C17EC4280, file "app\services\optimization\metrics.py", line 240>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              16 (_strategy_outcome_rates)

253           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C18026330, file "app\services\optimization\metrics.py", line 253>)
              MAKE_FUNCTION
              LOAD_CONST              22 (<code object _empty_metrics at 0x0000018C18039070, file "app\services\optimization\metrics.py", line 253>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              17 (_empty_metrics)
              LOAD_CONST              23 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025130, file "app\services\optimization\metrics.py", line 13>:
 13           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('matrix_result')
              LOAD_GLOBAL              0 (dict)
              LOAD_CONST               2 ('return')
              LOAD_GLOBAL              0 (dict)
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object compute_matrix_metrics at 0x0000018C181A2E40, file "app\services\optimization\metrics.py", line 13>:
  13            RESUME                   0

  33            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (matrix_result)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        11 (to L1)
                NOT_TAKEN

  34            LOAD_GLOBAL              5 (_empty_metrics + NULL)
                CALL                     0
                RETURN_VALUE

  36    L1:     LOAD_FAST_BORROW         0 (matrix_result)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               1 ('results')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L2)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
        L2:     STORE_FAST               1 (rows)

  37            LOAD_FAST_BORROW         1 (rows)
                GET_ITER
                LOAD_FAST_AND_CLEAR      2 (r)
                SWAP                     2
        L3:     BUILD_LIST               0
                SWAP                     2
        L4:     FOR_ITER                29 (to L7)
                STORE_FAST               2 (r)
                LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         2 (r)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
        L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           27 (to L4)
        L6:     LOAD_FAST_BORROW         2 (r)
                LIST_APPEND              2
                JUMP_BACKWARD           31 (to L4)
        L7:     END_FOR
                POP_ITER
        L8:     STORE_FAST               1 (rows)
                STORE_FAST               2 (r)

  38            LOAD_GLOBAL              9 (len + NULL)
                LOAD_FAST_BORROW         1 (rows)
                CALL                     1
                STORE_FAST               3 (total)

  39            LOAD_FAST_BORROW         3 (total)
                LOAD_SMALL_INT           0
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       11 (to L9)
                NOT_TAKEN

  40            LOAD_GLOBAL              5 (_empty_metrics + NULL)
                CALL                     0
                RETURN_VALUE

  42    L9:     LOAD_GLOBAL             11 (sum + NULL)
                LOAD_CONST               2 (<code object <genexpr> at 0x0000018C1802C9B0, file "app\services\optimization\metrics.py", line 42>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         1 (rows)
                GET_ITER
                CALL                     0
                CALL                     1
                STORE_FAST               4 (passed)

  43            LOAD_GLOBAL             11 (sum + NULL)
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C17972550, file "app\services\optimization\metrics.py", line 43>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         1 (rows)
                GET_ITER
                CALL                     0
                CALL                     1
                STORE_FAST               5 (error_count)

  44            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (passed, total)
                BINARY_OP               11 (/)
                STORE_FAST               6 (pass_rate)

  46            LOAD_FAST_BORROW         1 (rows)
                GET_ITER
                LOAD_FAST_AND_CLEAR      2 (r)
                SWAP                     2
       L10:     BUILD_LIST               0
                SWAP                     2
       L11:     FOR_ITER                14 (to L12)
                STORE_FAST               2 (r)
                LOAD_GLOBAL             13 (_score + NULL)
                LOAD_FAST_BORROW         2 (r)
                CALL                     1
                LIST_APPEND              2
                JUMP_BACKWARD           16 (to L11)
       L12:     END_FOR
                POP_ITER
       L13:     STORE_FAST               7 (replay_scores)
                STORE_FAST               2 (r)

  47            LOAD_FAST_BORROW         7 (replay_scores)
                TO_BOOL
                POP_JUMP_IF_FALSE       22 (to L14)
                NOT_TAKEN
                LOAD_GLOBAL             15 (round + NULL)
                LOAD_GLOBAL             17 (mean + NULL)
                LOAD_FAST_BORROW         7 (replay_scores)
                CALL                     1
                LOAD_SMALL_INT           2
                CALL                     2
                JUMP_FORWARD             1 (to L15)
       L14:     LOAD_CONST               4 (0.0)
       L15:     STORE_FAST               8 (avg_replay)

  48            LOAD_FAST_BORROW         1 (rows)
                GET_ITER
                LOAD_FAST_AND_CLEAR      2 (r)
                SWAP                     2
       L16:     BUILD_LIST               0
                SWAP                     2
       L17:     FOR_ITER                39 (to L21)
                STORE_FAST               2 (r)
                LOAD_GLOBAL              9 (len + NULL)
                LOAD_FAST_BORROW         2 (r)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               5 ('transcript')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L20)
       L18:     NOT_TAKEN
       L19:     POP_TOP
                BUILD_LIST               0
       L20:     CALL                     1
                LIST_APPEND              2
                JUMP_BACKWARD           41 (to L17)
       L21:     END_FOR
                POP_ITER
       L22:     STORE_FAST               9 (turns)
                STORE_FAST               2 (r)

  49            LOAD_FAST_BORROW         9 (turns)
                TO_BOOL
                POP_JUMP_IF_FALSE       22 (to L23)
                NOT_TAKEN
                LOAD_GLOBAL             15 (round + NULL)
                LOAD_GLOBAL             17 (mean + NULL)
                LOAD_FAST_BORROW         9 (turns)
                CALL                     1
                LOAD_SMALL_INT           2
                CALL                     2
                JUMP_FORWARD             1 (to L24)
       L23:     LOAD_CONST               4 (0.0)
       L24:     STORE_FAST              10 (avg_turns)

  51            LOAD_GLOBAL              3 (dict + NULL)
                LOAD_GLOBAL             19 (Counter + NULL)
                LOAD_CONST               6 (<code object <genexpr> at 0x0000018C18052F70, file "app\services\optimization\metrics.py", line 51>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         1 (rows)
                GET_ITER
                CALL                     0
                CALL                     1
                CALL                     1
                STORE_FAST              11 (outcome_breakdown)

  53            LOAD_GLOBAL             19 (Counter + NULL)
                CALL                     0
                STORE_FAST              12 (missing_freq)

  54            LOAD_FAST_BORROW         1 (rows)
                GET_ITER
       L25:     FOR_ITER                72 (to L28)
                STORE_FAST               2 (r)

  55            LOAD_FAST_BORROW         2 (r)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               7 ('evaluation')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L26)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
       L26:     LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               8 ('missing_steps')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L27)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
       L27:     STORE_FAST              13 (missing)

  56            LOAD_FAST_BORROW        12 (missing_freq)
                LOAD_ATTR               21 (update + NULL|self)
                LOAD_FAST_BORROW        13 (missing)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           74 (to L25)

  54   L28:     END_FOR
                POP_ITER

  58            LOAD_GLOBAL             23 (_by_strategy + NULL)
                LOAD_FAST_BORROW         1 (rows)
                CALL                     1
                STORE_FAST              14 (by_strategy)

  59            LOAD_GLOBAL             25 (_by_scenario + NULL)
                LOAD_FAST_BORROW         1 (rows)
                CALL                     1
                STORE_FAST              15 (by_scenario)

  60            LOAD_GLOBAL             27 (_strategy_outcome_rates + NULL)
                LOAD_FAST_BORROW        14 (by_strategy)
                CALL                     1
                STORE_FAST              16 (strategy_outcome_rates)

  63            LOAD_FAST_BORROW         1 (rows)
                GET_ITER
                LOAD_FAST_AND_CLEAR      2 (r)
                SWAP                     2
       L29:     BUILD_LIST               0
                SWAP                     2
       L30:     FOR_ITER                29 (to L33)
                STORE_FAST_LOAD_FAST    34 (r, r)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               9 ('personality_id')
                CALL                     1
                TO_BOOL
       L31:     POP_JUMP_IF_TRUE         3 (to L32)
                NOT_TAKEN
                JUMP_BACKWARD           27 (to L30)
       L32:     LOAD_FAST_BORROW         2 (r)
                LIST_APPEND              2
                JUMP_BACKWARD           31 (to L30)
       L33:     END_FOR
                POP_ITER
       L34:     STORE_FAST              17 (behaviour_rows)
                STORE_FAST               2 (r)

  64            LOAD_FAST_BORROW        17 (behaviour_rows)
                TO_BOOL
                POP_JUMP_IF_FALSE       58 (to L35)
                NOT_TAKEN

  65            LOAD_GLOBAL             15 (round + NULL)
                LOAD_GLOBAL             17 (mean + NULL)
                LOAD_CONST              10 (<code object <genexpr> at 0x0000018C180C4360, file "app\services\optimization\metrics.py", line 65>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW        17 (behaviour_rows)
                GET_ITER
                CALL                     0
                CALL                     1
                LOAD_SMALL_INT           4
                CALL                     2
                STORE_FAST              18 (avg_trust)

  66            LOAD_GLOBAL             15 (round + NULL)
                LOAD_GLOBAL             17 (mean + NULL)
                LOAD_CONST              11 (<code object <genexpr> at 0x0000018C180C4690, file "app\services\optimization\metrics.py", line 66>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW        17 (behaviour_rows)
                GET_ITER
                CALL                     0
                CALL                     1
                LOAD_SMALL_INT           4
                CALL                     2
                STORE_FAST              19 (avg_frust)
                JUMP_FORWARD             4 (to L36)

  68   L35:     LOAD_CONST              12 (0.5)
                STORE_FAST              18 (avg_trust)

  69            LOAD_CONST               4 (0.0)
                STORE_FAST              19 (avg_frust)

  71   L36:     LOAD_GLOBAL             11 (sum + NULL)
                LOAD_CONST              13 (<code object <genexpr> at 0x0000018C1802C4F0, file "app\services\optimization\metrics.py", line 71>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         1 (rows)
                GET_ITER
                CALL                     0
                CALL                     1
                STORE_FAST              20 (divergence_count)

  72            LOAD_GLOBAL             11 (sum + NULL)
                LOAD_CONST              14 (<code object <genexpr> at 0x0000018C1804D070, file "app\services\optimization\metrics.py", line 72>)
                MAKE_FUNCTION

  73            LOAD_FAST_BORROW         1 (rows)
                GET_ITER

  72            CALL                     0
                CALL                     1
                STORE_FAST              21 (escalation_count)

  77            LOAD_GLOBAL             11 (sum + NULL)
                LOAD_CONST              15 (<code object <genexpr> at 0x0000018C1804CD30, file "app\services\optimization\metrics.py", line 77>)
                MAKE_FUNCTION

  78            LOAD_FAST_BORROW         1 (rows)
                GET_ITER

  77            CALL                     0
                CALL                     1
                STORE_FAST              22 (dropoff_count)

  82            LOAD_GLOBAL             11 (sum + NULL)
                LOAD_CONST              16 (<code object <genexpr> at 0x0000018C17F96590, file "app\services\optimization\metrics.py", line 82>)
                MAKE_FUNCTION

  83            LOAD_FAST_BORROW         1 (rows)
                GET_ITER

  82            CALL                     0
                CALL                     1
                STORE_FAST              23 (recovery_count)

  87            LOAD_GLOBAL             29 (_by_strategy_personality + NULL)
                LOAD_FAST_BORROW         1 (rows)
                CALL                     1
                STORE_FAST              24 (by_strategy_personality)

  89            BUILD_MAP                0

  90            LOAD_CONST              17 ('total_runs')
                LOAD_FAST_BORROW         3 (total)

  89            MAP_ADD                  1

  91            LOAD_CONST              18 ('pass_rate')
                LOAD_GLOBAL             15 (round + NULL)
                LOAD_FAST_BORROW         6 (pass_rate)
                LOAD_SMALL_INT           4
                CALL                     2

  89            MAP_ADD                  1

  92            LOAD_CONST              19 ('average_replay_score')
                LOAD_FAST_BORROW         8 (avg_replay)

  89            MAP_ADD                  1

  93            LOAD_CONST              20 ('average_turns')
                LOAD_FAST_BORROW        10 (avg_turns)

  89            MAP_ADD                  1

  94            LOAD_CONST              21 ('outcome_breakdown')
                LOAD_FAST_BORROW        11 (outcome_breakdown)

  89            MAP_ADD                  1

  95            LOAD_CONST              22 ('by_strategy')
                LOAD_FAST_BORROW        14 (by_strategy)

  89            MAP_ADD                  1

  96            LOAD_CONST              23 ('by_scenario')
                LOAD_FAST_BORROW        15 (by_scenario)

  89            MAP_ADD                  1

  97            LOAD_CONST              24 ('strategy_outcome_rates')
                LOAD_FAST_BORROW        16 (strategy_outcome_rates)

  89            MAP_ADD                  1

  98            LOAD_CONST              25 ('missing_lifecycle_frequency')
                LOAD_GLOBAL              3 (dict + NULL)
                LOAD_FAST_BORROW        12 (missing_freq)
                CALL                     1

  89            MAP_ADD                  1

  99            LOAD_CONST              26 ('error_count')
                LOAD_FAST_BORROW         5 (error_count)

  89            MAP_ADD                  1

 101            LOAD_CONST              27 ('average_trust_score')
                LOAD_FAST_BORROW        18 (avg_trust)

  89            MAP_ADD                  1

 102            LOAD_CONST              28 ('average_frustration_score')
                LOAD_FAST_BORROW        19 (avg_frust)

  89            MAP_ADD                  1

 103            LOAD_CONST              29 ('divergence_rate')
                LOAD_FAST_BORROW         3 (total)
                TO_BOOL
                POP_JUMP_IF_FALSE       20 (to L37)
                NOT_TAKEN
                LOAD_GLOBAL             15 (round + NULL)
                LOAD_FAST_BORROW        20 (divergence_count)
                LOAD_FAST_BORROW         3 (total)
                BINARY_OP               11 (/)
                LOAD_SMALL_INT           4
                CALL                     2
                JUMP_FORWARD             1 (to L38)
       L37:     LOAD_CONST               4 (0.0)

  89   L38:     MAP_ADD                  1

 104            LOAD_CONST              30 ('escalation_rate')
                LOAD_FAST_BORROW         3 (total)
                TO_BOOL
                POP_JUMP_IF_FALSE       20 (to L39)
                NOT_TAKEN
                LOAD_GLOBAL             15 (round + NULL)
                LOAD_FAST_BORROW        21 (escalation_count)
                LOAD_FAST_BORROW         3 (total)
                BINARY_OP               11 (/)
                LOAD_SMALL_INT           4
                CALL                     2
                JUMP_FORWARD             1 (to L40)
       L39:     LOAD_CONST               4 (0.0)

  89   L40:     MAP_ADD                  1

 105            LOAD_CONST              31 ('dropoff_rate')
                LOAD_FAST_BORROW         3 (total)
                TO_BOOL
                POP_JUMP_IF_FALSE       20 (to L41)
                NOT_TAKEN
                LOAD_GLOBAL             15 (round + NULL)
                LOAD_FAST_BORROW        22 (dropoff_count)
                LOAD_FAST_BORROW         3 (total)
                BINARY_OP               11 (/)
                LOAD_SMALL_INT           4
                CALL                     2
                JUMP_FORWARD             1 (to L42)
       L41:     LOAD_CONST               4 (0.0)

  89   L42:     MAP_ADD                  1

 106            LOAD_CONST              32 ('recovery_rate')
                LOAD_FAST_BORROW         3 (total)
                TO_BOOL
                POP_JUMP_IF_FALSE       20 (to L43)
                NOT_TAKEN
                LOAD_GLOBAL             15 (round + NULL)
                LOAD_FAST_BORROW        23 (recovery_count)
                LOAD_FAST_BORROW         3 (total)
                BINARY_OP               11 (/)
                LOAD_SMALL_INT           4
                CALL                     2
                JUMP_FORWARD             1 (to L44)
       L43:     LOAD_CONST               4 (0.0)

  89   L44:     MAP_ADD                  1

 107            LOAD_CONST              33 ('by_strategy_personality')
                LOAD_FAST_BORROW        24 (by_strategy_personality)

  89            MAP_ADD                  1
                RETURN_VALUE

  --   L45:     SWAP                     2
                POP_TOP

  37            SWAP                     2
                STORE_FAST               2 (r)
                RERAISE                  0

  --   L46:     SWAP                     2
                POP_TOP

  46            SWAP                     2
                STORE_FAST               2 (r)
                RERAISE                  0

  --   L47:     SWAP                     2
                POP_TOP

  48            SWAP                     2
                STORE_FAST               2 (r)
                RERAISE                  0

  --   L48:     SWAP                     2
                POP_TOP

  63            SWAP                     2
                STORE_FAST               2 (r)
                RERAISE                  0
ExceptionTable:
  L3 to L5 -> L45 [2]
  L6 to L8 -> L45 [2]
  L10 to L13 -> L46 [2]
  L16 to L18 -> L47 [2]
  L19 to L22 -> L47 [2]
  L29 to L31 -> L48 [2]
  L32 to L34 -> L48 [2]

Disassembly of <code object <genexpr> at 0x0000018C1802C9B0, file "app\services\optimization\metrics.py", line 42>:
  42           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                31 (to L5)
               STORE_FAST_LOAD_FAST    17 (r, r)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('passed')
               CALL                     1
               TO_BOOL
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           27 (to L2)
       L4:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           33 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C17972550, file "app\services\optimization\metrics.py", line 43>:
  43           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                54 (to L5)
               STORE_FAST_LOAD_FAST    17 (r, r)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('cell_error')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        26 (to L4)
               NOT_TAKEN
               LOAD_FAST_BORROW         1 (r)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               1 ('error')
               CALL                     1
               TO_BOOL
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           50 (to L2)
       L4:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           56 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C18052F70, file "app\services\optimization\metrics.py", line 51>:
  51           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                21 (to L3)
               STORE_FAST_LOAD_FAST    17 (r, r)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('actual_outcome')
               CALL                     1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           23 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C180C4360, file "app\services\optimization\metrics.py", line 65>:
  65           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                16 (to L3)
               STORE_FAST               1 (r)
               LOAD_GLOBAL              1 (_trust + NULL)
               LOAD_FAST_BORROW         1 (r)
               CALL                     1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           18 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C180C4690, file "app\services\optimization\metrics.py", line 66>:
  66           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                16 (to L3)
               STORE_FAST               1 (r)
               LOAD_GLOBAL              1 (_frust + NULL)
               LOAD_FAST_BORROW         1 (r)
               CALL                     1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           18 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C1802C4F0, file "app\services\optimization\metrics.py", line 71>:
  71           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                31 (to L5)
               STORE_FAST_LOAD_FAST    17 (r, r)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('divergence_triggered')
               CALL                     1
               TO_BOOL
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           27 (to L2)
       L4:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           33 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C1804D070, file "app\services\optimization\metrics.py", line 72>:
  72            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0
                LOAD_FAST                0 (.0)

  73    L2:     FOR_ITER                89 (to L12)
                STORE_FAST               1 (r)

  74            LOAD_FAST_BORROW         1 (r)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               0 ('divergence_actions')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
        L3:     NOT_TAKEN
        L4:     POP_TOP
                BUILD_LIST               0
        L5:     GET_ITER
        L6:     FOR_ITER                55 (to L11)
                STORE_FAST               2 (a)

  75            LOAD_GLOBAL              3 (isinstance + NULL)
                LOAD_FAST_BORROW         2 (a)
                LOAD_GLOBAL              4 (dict)
                CALL                     2
                TO_BOOL

  73    L7:     POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN
                JUMP_BACKWARD           27 (to L6)

  75    L8:     LOAD_FAST_BORROW         2 (a)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               1 ('action')
                CALL                     1
                LOAD_CONST               2 ('lead_escalated')
                COMPARE_OP              88 (bool(==))

  73    L9:     POP_JUMP_IF_TRUE         3 (to L10)
                NOT_TAKEN
                JUMP_BACKWARD           51 (to L6)
       L10:     LOAD_SMALL_INT           1
                YIELD_VALUE              0
                RESUME                   5
                POP_TOP
                JUMP_BACKWARD           57 (to L6)

  74   L11:     END_FOR
                POP_ITER

  73            JUMP_BACKWARD           91 (to L2)
       L12:     END_FOR
                POP_ITER
                LOAD_CONST               3 (None)
                RETURN_VALUE

  --   L13:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L3 -> L13 [0] lasti
  L4 to L7 -> L13 [0] lasti
  L8 to L9 -> L13 [0] lasti
  L10 to L13 -> L13 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C1804CD30, file "app\services\optimization\metrics.py", line 77>:
  77            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0
                LOAD_FAST                0 (.0)

  78    L2:     FOR_ITER                89 (to L12)
                STORE_FAST               1 (r)

  79            LOAD_FAST_BORROW         1 (r)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               0 ('divergence_actions')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
        L3:     NOT_TAKEN
        L4:     POP_TOP
                BUILD_LIST               0
        L5:     GET_ITER
        L6:     FOR_ITER                55 (to L11)
                STORE_FAST               2 (a)

  80            LOAD_GLOBAL              3 (isinstance + NULL)
                LOAD_FAST_BORROW         2 (a)
                LOAD_GLOBAL              4 (dict)
                CALL                     2
                TO_BOOL

  78    L7:     POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN
                JUMP_BACKWARD           27 (to L6)

  80    L8:     LOAD_FAST_BORROW         2 (a)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               1 ('action')
                CALL                     1
                LOAD_CONST               2 ('lead_dropped')
                COMPARE_OP              88 (bool(==))

  78    L9:     POP_JUMP_IF_TRUE         3 (to L10)
                NOT_TAKEN
                JUMP_BACKWARD           51 (to L6)
       L10:     LOAD_SMALL_INT           1
                YIELD_VALUE              0
                RESUME                   5
                POP_TOP
                JUMP_BACKWARD           57 (to L6)

  79   L11:     END_FOR
                POP_ITER

  78            JUMP_BACKWARD           91 (to L2)
       L12:     END_FOR
                POP_ITER
                LOAD_CONST               3 (None)
                RETURN_VALUE

  --   L13:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L3 -> L13 [0] lasti
  L4 to L7 -> L13 [0] lasti
  L8 to L9 -> L13 [0] lasti
  L10 to L13 -> L13 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C17F96590, file "app\services\optimization\metrics.py", line 82>:
  82            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0
                LOAD_FAST                0 (.0)

  83    L2:     FOR_ITER                65 (to L10)
                STORE_FAST               1 (r)

  84            LOAD_FAST_BORROW         1 (r)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               0 ('final_behavior_state')
                CALL                     1
                LOAD_CONST               1 ('engaged')
                COMPARE_OP              88 (bool(==))

  83    L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           27 (to L2)

  84    L4:     LOAD_FAST_BORROW         1 (r)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('trust_score')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
        L5:     NOT_TAKEN
        L6:     POP_TOP
                LOAD_SMALL_INT           0
        L7:     LOAD_CONST               3 (0.6)
                COMPARE_OP             188 (bool(>=))

  83    L8:     POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN
                JUMP_BACKWARD           61 (to L2)
        L9:     LOAD_SMALL_INT           1
                YIELD_VALUE              0
                RESUME                   5
                POP_TOP
                JUMP_BACKWARD           67 (to L2)
       L10:     END_FOR
                POP_ITER
                LOAD_CONST               4 (None)
                RETURN_VALUE

  --   L11:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L3 -> L11 [0] lasti
  L4 to L5 -> L11 [0] lasti
  L6 to L8 -> L11 [0] lasti
  L9 to L11 -> L11 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026130, file "app\services\optimization\metrics.py", line 113>:
113           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('r')
              LOAD_GLOBAL              0 (dict)
              LOAD_CONST               2 ('return')
              LOAD_GLOBAL              2 (int)
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _score at 0x0000018C17F96420, file "app\services\optimization\metrics.py", line 113>:
113           RESUME                   0

114           LOAD_FAST_BORROW         0 (r)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               0 ('evaluation')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L1:     LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               1 ('replay_score')
              LOAD_SMALL_INT           0
              CALL                     2
              STORE_FAST               1 (s)

115           LOAD_GLOBAL              3 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (s)
              LOAD_GLOBAL              4 (int)
              LOAD_GLOBAL              6 (float)
              BUILD_TUPLE              2
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE
      L2:     LOAD_SMALL_INT           0
              RETURN_VALUE

Disassembly of <code object _bucket at 0x0000018C18010DF0, file "app\services\optimization\metrics.py", line 118>:
118           RESUME                   0

119           BUILD_MAP                0
              STORE_FAST               2 (out)

120           LOAD_FAST_BORROW         0 (rows)
              GET_ITER
      L1:     FOR_ITER                59 (to L3)
              STORE_FAST               3 (r)

121           LOAD_FAST_BORROW         3 (r)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_FAST_BORROW         1 (key)
              CALL                     1
              STORE_FAST               4 (k)

122           LOAD_FAST_BORROW         4 (k)
              POP_JUMP_IF_NOT_NONE     3 (to L2)
              NOT_TAKEN

123           JUMP_BACKWARD           26 (to L1)

124   L2:     LOAD_FAST_BORROW         2 (out)
              LOAD_ATTR                3 (setdefault + NULL|self)
              LOAD_FAST_BORROW         4 (k)
              BUILD_LIST               0
              CALL                     2
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_FAST_BORROW         3 (r)
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           61 (to L1)

120   L3:     END_FOR
              POP_ITER

125           LOAD_FAST_BORROW         2 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18053630, file "app\services\optimization\metrics.py", line 128>:
128           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('rows')
              LOAD_GLOBAL              0 (List)
              LOAD_GLOBAL              2 (dict)
              BINARY_OP               26 ([])
              LOAD_CONST               2 ('return')
              LOAD_GLOBAL              2 (dict)
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _by_strategy at 0x0000018C17D7CA60, file "app\services\optimization\metrics.py", line 128>:
 128            RESUME                   0

 129            LOAD_GLOBAL              1 (_bucket + NULL)
                LOAD_FAST_BORROW         0 (rows)
                LOAD_CONST               0 ('strategy_id')
                CALL                     2
                STORE_FAST               1 (grouped)

 130            BUILD_MAP                0
                STORE_FAST               2 (out)

 131            LOAD_FAST_BORROW         1 (grouped)
                LOAD_ATTR                3 (items + NULL|self)
                CALL                     0
                GET_ITER
        L1:     EXTENDED_ARG             2
                FOR_ITER               576 (to L25)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   52 (sid, items)

 132            LOAD_GLOBAL              5 (len + NULL)
                LOAD_FAST_BORROW         4 (items)
                CALL                     1
                STORE_FAST               5 (n)

 133            LOAD_GLOBAL              7 (sum + NULL)
                LOAD_CONST               1 (<code object <genexpr> at 0x0000018C1802C880, file "app\services\optimization\metrics.py", line 133>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         4 (items)
                GET_ITER
                CALL                     0
                CALL                     1
                STORE_FAST               6 (passed)

 134            LOAD_GLOBAL              7 (sum + NULL)
                LOAD_CONST               2 (<code object <genexpr> at 0x0000018C18011210, file "app\services\optimization\metrics.py", line 134>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         4 (items)
                GET_ITER
                CALL                     0
                CALL                     1
                STORE_FAST               7 (errors)

 135            LOAD_GLOBAL              9 (dict + NULL)
                LOAD_GLOBAL             11 (Counter + NULL)
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18053CF0, file "app\services\optimization\metrics.py", line 135>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         4 (items)
                GET_ITER
                CALL                     0
                CALL                     1
                CALL                     1
                STORE_FAST               8 (outcomes)

 137            LOAD_FAST_BORROW         5 (n)
                TO_BOOL
                POP_JUMP_IF_FALSE       36 (to L2)
                NOT_TAKEN
                LOAD_GLOBAL             13 (round + NULL)
                LOAD_FAST_BORROW         8 (outcomes)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST               4 ('booked')
                LOAD_SMALL_INT           0
                CALL                     2
                LOAD_FAST_BORROW         5 (n)
                BINARY_OP               11 (/)
                LOAD_SMALL_INT           4
                CALL                     2
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               5 (0.0)
        L3:     STORE_FAST               9 (booked_rate)

 138            LOAD_FAST_BORROW         8 (outcomes)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST               6 ('callback_requested')
                LOAD_SMALL_INT           0
                CALL                     2
                LOAD_FAST_BORROW         8 (outcomes)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST               7 ('qualified_callback_requested')
                LOAD_SMALL_INT           0
                CALL                     2
                BINARY_OP                0 (+)
                STORE_FAST              10 (cb_count)

 139            LOAD_FAST_BORROW         5 (n)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L4)
                NOT_TAKEN
                LOAD_GLOBAL             13 (round + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 165 (cb_count, n)
                BINARY_OP               11 (/)
                LOAD_SMALL_INT           4
                CALL                     2
                JUMP_FORWARD             1 (to L5)
        L4:     LOAD_CONST               5 (0.0)
        L5:     STORE_FAST              11 (callback_rate)

 140            LOAD_FAST_BORROW         5 (n)
                TO_BOOL
                POP_JUMP_IF_FALSE       36 (to L6)
                NOT_TAKEN
                LOAD_GLOBAL             13 (round + NULL)
                LOAD_FAST_BORROW         8 (outcomes)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST               8 ('not_booked')
                LOAD_SMALL_INT           0
                CALL                     2
                LOAD_FAST_BORROW         5 (n)
                BINARY_OP               11 (/)
                LOAD_SMALL_INT           4
                CALL                     2
                JUMP_FORWARD             1 (to L7)
        L6:     LOAD_CONST               5 (0.0)
        L7:     STORE_FAST              12 (not_booked)

 141            LOAD_FAST_BORROW         5 (n)
                TO_BOOL
                POP_JUMP_IF_FALSE       36 (to L8)
                NOT_TAKEN
                LOAD_GLOBAL             13 (round + NULL)
                LOAD_FAST_BORROW         8 (outcomes)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST               9 ('transferred')
                LOAD_SMALL_INT           0
                CALL                     2
                LOAD_FAST_BORROW         5 (n)
                BINARY_OP               11 (/)
                LOAD_SMALL_INT           4
                CALL                     2
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               5 (0.0)
        L9:     STORE_FAST              13 (transferred_r)

 142            LOAD_GLOBAL             16 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       28 (to L13)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              10 (<code object <genexpr> at 0x0000018C18053750, file "app\services\optimization\metrics.py", line 142>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         4 (items)
                GET_ITER
                CALL                     0
       L10:     FOR_ITER                12 (to L12)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L11)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L10)
       L11:     POP_ITER
                LOAD_CONST              11 (True)
                JUMP_FORWARD            17 (to L14)
       L12:     END_FOR
                POP_ITER
                LOAD_CONST              12 (False)
                JUMP_FORWARD            13 (to L14)
       L13:     PUSH_NULL
                LOAD_CONST              10 (<code object <genexpr> at 0x0000018C18053750, file "app\services\optimization\metrics.py", line 142>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         4 (items)
                GET_ITER
                CALL                     0
                CALL                     1
       L14:     STORE_FAST              14 (effective)

 145            LOAD_FAST_BORROW         4 (items)
                GET_ITER
                LOAD_FAST_AND_CLEAR     15 (r)
                SWAP                     2
       L15:     BUILD_LIST               0
                SWAP                     2
       L16:     FOR_ITER                29 (to L19)
                STORE_FAST_LOAD_FAST   255 (r, r)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              13 ('personality_id')
                CALL                     1
                TO_BOOL
       L17:     POP_JUMP_IF_TRUE         3 (to L18)
                NOT_TAKEN
                JUMP_BACKWARD           27 (to L16)
       L18:     LOAD_FAST_BORROW        15 (r)
                LIST_APPEND              2
                JUMP_BACKWARD           31 (to L16)
       L19:     END_FOR
                POP_ITER
       L20:     STORE_FAST              16 (behaviour_items)
                STORE_FAST              15 (r)

 146            LOAD_FAST_BORROW        16 (behaviour_items)
                TO_BOOL
                POP_JUMP_IF_FALSE       58 (to L21)
                NOT_TAKEN

 147            LOAD_GLOBAL             13 (round + NULL)
                LOAD_GLOBAL             19 (mean + NULL)
                LOAD_CONST              14 (<code object <genexpr> at 0x0000018C180C4470, file "app\services\optimization\metrics.py", line 147>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW        16 (behaviour_items)
                GET_ITER
                CALL                     0
                CALL                     1
                LOAD_SMALL_INT           4
                CALL                     2
                STORE_FAST              17 (trust_avg)

 148            LOAD_GLOBAL             13 (round + NULL)
                LOAD_GLOBAL             19 (mean + NULL)
                LOAD_CONST              15 (<code object <genexpr> at 0x0000018C180C47A0, file "app\services\optimization\metrics.py", line 148>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW        16 (behaviour_items)
                GET_ITER
                CALL                     0
                CALL                     1
                LOAD_SMALL_INT           4
                CALL                     2
                STORE_FAST              18 (frust_avg)
                JUMP_FORWARD             4 (to L22)

 150   L21:     LOAD_CONST              16 (0.5)
                STORE_FAST              17 (trust_avg)

 151            LOAD_CONST               5 (0.0)
                STORE_FAST              18 (frust_avg)

 152   L22:     LOAD_GLOBAL              7 (sum + NULL)
                LOAD_CONST              17 (<code object <genexpr> at 0x0000018C1802CAE0, file "app\services\optimization\metrics.py", line 152>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         4 (items)
                GET_ITER
                CALL                     0
                CALL                     1
                STORE_FAST              19 (divergence_count)

 155            LOAD_CONST              18 ('n')
                LOAD_FAST                5 (n)

 156            LOAD_CONST              19 ('passed')
                LOAD_FAST                6 (passed)

 157            LOAD_CONST              20 ('pass_rate')
                LOAD_FAST_BORROW         5 (n)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L23)
                NOT_TAKEN
                LOAD_GLOBAL             13 (round + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 101 (passed, n)
                BINARY_OP               11 (/)
                LOAD_SMALL_INT           4
                CALL                     2
                JUMP_FORWARD             1 (to L24)
       L23:     LOAD_CONST               5 (0.0)

 158   L24:     LOAD_CONST              21 ('avg_replay_score')
                LOAD_GLOBAL             13 (round + NULL)
                LOAD_GLOBAL             19 (mean + NULL)
                LOAD_CONST              22 (<code object <genexpr> at 0x0000018C180C4580, file "app\services\optimization\metrics.py", line 158>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         4 (items)
                GET_ITER
                CALL                     0
                CALL                     1
                LOAD_SMALL_INT           2
                CALL                     2

 159            LOAD_CONST              23 ('avg_turns')
                LOAD_GLOBAL             13 (round + NULL)
                LOAD_GLOBAL             19 (mean + NULL)
                LOAD_CONST              24 (<code object <genexpr> at 0x0000018C18038170, file "app\services\optimization\metrics.py", line 159>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         4 (items)
                GET_ITER
                CALL                     0
                CALL                     1
                LOAD_SMALL_INT           2
                CALL                     2

 160            LOAD_CONST              25 ('errors')
                LOAD_FAST_BORROW         7 (errors)

 161            LOAD_CONST              26 ('outcome_counts')
                LOAD_FAST_BORROW         8 (outcomes)

 162            LOAD_CONST              27 ('booked_rate')
                LOAD_FAST_BORROW         9 (booked_rate)

 163            LOAD_CONST              28 ('callback_rate')
                LOAD_FAST_BORROW        11 (callback_rate)

 164            LOAD_CONST              29 ('not_booked_rate')
                LOAD_FAST_BORROW        12 (not_booked)

 165            LOAD_CONST              30 ('transferred_rate')
                LOAD_FAST_BORROW        13 (transferred_r)

 166            LOAD_CONST              31 ('effective')
                LOAD_FAST_BORROW        14 (effective)

 168            LOAD_CONST              32 ('trust_avg')
                LOAD_FAST_BORROW        17 (trust_avg)

 169            LOAD_CONST              33 ('frustration_avg')
                LOAD_FAST_BORROW        18 (frust_avg)

 170            LOAD_CONST              34 ('divergence_count')
                LOAD_FAST_BORROW        19 (divergence_count)

 154            BUILD_MAP               15
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (out, sid)
                STORE_SUBSCR
                EXTENDED_ARG             2
                JUMP_BACKWARD          579 (to L1)

 131   L25:     END_FOR
                POP_ITER

 172            LOAD_FAST_BORROW         2 (out)
                RETURN_VALUE

  --   L26:     SWAP                     2
                POP_TOP

 145            SWAP                     2
                STORE_FAST              15 (r)
                RERAISE                  0
ExceptionTable:
  L15 to L17 -> L26 [3]
  L18 to L20 -> L26 [3]

Disassembly of <code object <genexpr> at 0x0000018C1802C880, file "app\services\optimization\metrics.py", line 133>:
 133           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                31 (to L5)
               STORE_FAST_LOAD_FAST    17 (r, r)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('passed')
               CALL                     1
               TO_BOOL
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           27 (to L2)
       L4:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           33 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C18011210, file "app\services\optimization\metrics.py", line 134>:
 134           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                54 (to L5)
               STORE_FAST_LOAD_FAST    17 (r, r)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('cell_error')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        26 (to L4)
               NOT_TAKEN
               LOAD_FAST_BORROW         1 (r)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               1 ('error')
               CALL                     1
               TO_BOOL
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           50 (to L2)
       L4:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           56 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C18053CF0, file "app\services\optimization\metrics.py", line 135>:
 135           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                21 (to L3)
               STORE_FAST_LOAD_FAST    17 (r, r)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('actual_outcome')
               CALL                     1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           23 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C18053750, file "app\services\optimization\metrics.py", line 142>:
 142           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                21 (to L3)
               STORE_FAST_LOAD_FAST    17 (r, r)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('strategy_effective')
               CALL                     1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           23 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C180C4470, file "app\services\optimization\metrics.py", line 147>:
 147           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                16 (to L3)
               STORE_FAST               1 (r)
               LOAD_GLOBAL              1 (_trust + NULL)
               LOAD_FAST_BORROW         1 (r)
               CALL                     1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           18 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C180C47A0, file "app\services\optimization\metrics.py", line 148>:
 148           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                16 (to L3)
               STORE_FAST               1 (r)
               LOAD_GLOBAL              1 (_frust + NULL)
               LOAD_FAST_BORROW         1 (r)
               CALL                     1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           18 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C1802CAE0, file "app\services\optimization\metrics.py", line 152>:
 152           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                31 (to L5)
               STORE_FAST_LOAD_FAST    17 (r, r)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('divergence_triggered')
               CALL                     1
               TO_BOOL
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           27 (to L2)
       L4:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           33 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C180C4580, file "app\services\optimization\metrics.py", line 158>:
 158           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                16 (to L3)
               STORE_FAST               1 (r)
               LOAD_GLOBAL              1 (_score + NULL)
               LOAD_FAST_BORROW         1 (r)
               CALL                     1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           18 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C18038170, file "app\services\optimization\metrics.py", line 159>:
 159           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                41 (to L6)
               STORE_FAST               1 (r)
               LOAD_GLOBAL              1 (len + NULL)
               LOAD_FAST_BORROW         1 (r)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST               0 ('transcript')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L5)
       L3:     NOT_TAKEN
       L4:     POP_TOP
               BUILD_LIST               0
       L5:     CALL                     1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           43 (to L2)
       L6:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L7:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L7 [0] lasti
  L4 to L7 -> L7 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18053BD0, file "app\services\optimization\metrics.py", line 175>:
175           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('rows')
              LOAD_GLOBAL              0 (List)
              LOAD_GLOBAL              2 (dict)
              BINARY_OP               26 ([])
              LOAD_CONST               2 ('return')
              LOAD_GLOBAL              2 (dict)
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _by_strategy_personality at 0x0000018C17D7EE90, file "app\services\optimization\metrics.py", line 175>:
175            RESUME                   0

180            BUILD_MAP                0
               STORE_FAST               1 (out)

181            LOAD_FAST_BORROW         0 (rows)
               GET_ITER
       L1:     EXTENDED_ARG             1
               FOR_ITER               285 (to L7)
               STORE_FAST               2 (r)

182            LOAD_FAST_BORROW         2 (r)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               1 ('strategy_id')
               CALL                     1
               STORE_FAST               3 (sid)

183            LOAD_FAST_BORROW         2 (r)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               2 ('personality_id')
               CALL                     1
               STORE_FAST               4 (pid)

184            LOAD_FAST_BORROW         3 (sid)
               TO_BOOL
               POP_JUMP_IF_FALSE        9 (to L2)
               NOT_TAKEN
               LOAD_FAST_BORROW         4 (pid)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN

185    L2:     JUMP_BACKWARD           56 (to L1)

186    L3:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                3 (setdefault + NULL|self)
               LOAD_FAST_BORROW         3 (sid)
               BUILD_MAP                0
               CALL                     2
               LOAD_ATTR                3 (setdefault + NULL|self)
               LOAD_FAST_BORROW         4 (pid)

187            LOAD_CONST               3 ('n')
               LOAD_SMALL_INT           0

188            LOAD_CONST               4 ('passed')
               LOAD_SMALL_INT           0

189            LOAD_CONST               5 ('booked')
               LOAD_SMALL_INT           0

190            LOAD_CONST               6 ('replay_total')
               LOAD_SMALL_INT           0

191            LOAD_CONST               7 ('divergence_count')
               LOAD_SMALL_INT           0

186            BUILD_MAP                5
               CALL                     2
               STORE_FAST               5 (cell)

193            LOAD_FAST_BORROW         5 (cell)
               LOAD_CONST               3 ('n')
               COPY                     2
               COPY                     2
               BINARY_OP               26 ([])
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               SWAP                     3
               SWAP                     2
               STORE_SUBSCR

194            LOAD_FAST_BORROW         2 (r)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               4 ('passed')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       22 (to L4)
               NOT_TAKEN

195            LOAD_FAST_BORROW         5 (cell)
               LOAD_CONST               4 ('passed')
               COPY                     2
               COPY                     2
               BINARY_OP               26 ([])
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               SWAP                     3
               SWAP                     2
               STORE_SUBSCR

196    L4:     LOAD_FAST_BORROW         2 (r)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               8 ('actual_outcome')
               CALL                     1
               LOAD_CONST               5 ('booked')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       22 (to L5)
               NOT_TAKEN

197            LOAD_FAST_BORROW         5 (cell)
               LOAD_CONST               5 ('booked')
               COPY                     2
               COPY                     2
               BINARY_OP               26 ([])
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               SWAP                     3
               SWAP                     2
               STORE_SUBSCR

198    L5:     LOAD_FAST_BORROW         5 (cell)
               LOAD_CONST               6 ('replay_total')
               COPY                     2
               COPY                     2
               BINARY_OP               26 ([])
               LOAD_GLOBAL              5 (_score + NULL)
               LOAD_FAST_BORROW         2 (r)
               CALL                     1
               BINARY_OP               13 (+=)
               SWAP                     3
               SWAP                     2
               STORE_SUBSCR

199            LOAD_FAST_BORROW         2 (r)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               9 ('divergence_triggered')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         4 (to L6)
               NOT_TAKEN
               EXTENDED_ARG             1
               JUMP_BACKWARD          264 (to L1)

200    L6:     LOAD_FAST_BORROW         5 (cell)
               LOAD_CONST               7 ('divergence_count')
               COPY                     2
               COPY                     2
               BINARY_OP               26 ([])
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               SWAP                     3
               SWAP                     2
               STORE_SUBSCR
               EXTENDED_ARG             1
               JUMP_BACKWARD          288 (to L1)

181    L7:     END_FOR
               POP_ITER

202            LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (items + NULL|self)
               CALL                     0
               GET_ITER
       L8:     FOR_ITER               139 (to L12)
               UNPACK_SEQUENCE          2
               STORE_FAST_STORE_FAST   54 (sid, by_p)

203            LOAD_FAST_BORROW         6 (by_p)
               LOAD_ATTR                7 (items + NULL|self)
               CALL                     0
               GET_ITER
       L9:     FOR_ITER               114 (to L11)
               UNPACK_SEQUENCE          2
               STORE_FAST_STORE_FAST   69 (pid, cell)

204            LOAD_FAST_BORROW         5 (cell)
               LOAD_CONST               3 ('n')
               BINARY_OP               26 ([])
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L10)
               NOT_TAKEN
               POP_TOP
               LOAD_SMALL_INT           1
      L10:     STORE_FAST               7 (n)

205            LOAD_GLOBAL              9 (round + NULL)
               LOAD_FAST_BORROW         5 (cell)
               LOAD_CONST               4 ('passed')
               BINARY_OP               26 ([])
               LOAD_FAST_BORROW         7 (n)
               BINARY_OP               11 (/)
               LOAD_SMALL_INT           4
               CALL                     2
               LOAD_FAST_BORROW         5 (cell)
               LOAD_CONST              10 ('pass_rate')
               STORE_SUBSCR

206            LOAD_GLOBAL              9 (round + NULL)
               LOAD_FAST_BORROW         5 (cell)
               LOAD_CONST               5 ('booked')
               BINARY_OP               26 ([])
               LOAD_FAST_BORROW         7 (n)
               BINARY_OP               11 (/)
               LOAD_SMALL_INT           4
               CALL                     2
               LOAD_FAST_BORROW         5 (cell)
               LOAD_CONST              11 ('booked_rate')
               STORE_SUBSCR

207            LOAD_GLOBAL              9 (round + NULL)
               LOAD_FAST_BORROW         5 (cell)
               LOAD_CONST               6 ('replay_total')
               BINARY_OP               26 ([])
               LOAD_FAST_BORROW         7 (n)
               BINARY_OP               11 (/)
               LOAD_SMALL_INT           2
               CALL                     2
               LOAD_FAST_BORROW         5 (cell)
               LOAD_CONST              12 ('replay_avg')
               STORE_SUBSCR

208            LOAD_FAST_BORROW         5 (cell)
               LOAD_CONST               6 ('replay_total')
               DELETE_SUBSCR
               JUMP_BACKWARD          116 (to L9)

203   L11:     END_FOR
               POP_ITER
               JUMP_BACKWARD          141 (to L8)

202   L12:     END_FOR
               POP_ITER

209            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026230, file "app\services\optimization\metrics.py", line 212>:
212           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('r')
              LOAD_GLOBAL              0 (dict)
              LOAD_CONST               2 ('return')
              LOAD_GLOBAL              2 (float)
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _trust at 0x0000018C18038B70, file "app\services\optimization\metrics.py", line 212>:
212           RESUME                   0

213           LOAD_FAST_BORROW         0 (r)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               0 ('trust_score')
              LOAD_CONST               1 (0.5)
              CALL                     2
              STORE_FAST               1 (v)

214           LOAD_GLOBAL              3 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (v)
              LOAD_GLOBAL              4 (int)
              LOAD_GLOBAL              6 (float)
              BUILD_TUPLE              2
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (v)
              RETURN_VALUE
      L1:     LOAD_CONST               1 (0.5)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025A30, file "app\services\optimization\metrics.py", line 217>:
217           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('r')
              LOAD_GLOBAL              0 (dict)
              LOAD_CONST               2 ('return')
              LOAD_GLOBAL              2 (float)
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _frust at 0x0000018C180388F0, file "app\services\optimization\metrics.py", line 217>:
217           RESUME                   0

218           LOAD_FAST_BORROW         0 (r)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               0 ('frustration_score')
              LOAD_CONST               1 (0.0)
              CALL                     2
              STORE_FAST               1 (v)

219           LOAD_GLOBAL              3 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (v)
              LOAD_GLOBAL              4 (int)
              LOAD_GLOBAL              6 (float)
              BUILD_TUPLE              2
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (v)
              RETURN_VALUE
      L1:     LOAD_CONST               1 (0.0)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180533F0, file "app\services\optimization\metrics.py", line 222>:
222           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('rows')
              LOAD_GLOBAL              0 (List)
              LOAD_GLOBAL              2 (dict)
              BINARY_OP               26 ([])
              LOAD_CONST               2 ('return')
              LOAD_GLOBAL              2 (dict)
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _by_scenario at 0x0000018C17ECE910, file "app\services\optimization\metrics.py", line 222>:
222           RESUME                   0

223           LOAD_GLOBAL              1 (_bucket + NULL)
              LOAD_FAST_BORROW         0 (rows)
              LOAD_CONST               0 ('scenario_id')
              CALL                     2
              STORE_FAST               1 (grouped)

224           BUILD_MAP                0
              STORE_FAST               2 (out)

225           LOAD_FAST_BORROW         1 (grouped)
              LOAD_ATTR                3 (items + NULL|self)
              CALL                     0
              GET_ITER
      L1:     FOR_ITER               146 (to L4)
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST   52 (sid, items)

226           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         4 (items)
              CALL                     1
              STORE_FAST               5 (n)

227           LOAD_GLOBAL              7 (sum + NULL)
              LOAD_CONST               1 (<code object <genexpr> at 0x0000018C1802C750, file "app\services\optimization\metrics.py", line 227>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         4 (items)
              GET_ITER
              CALL                     0
              CALL                     1
              STORE_FAST               6 (passed)

228           LOAD_GLOBAL              7 (sum + NULL)
              LOAD_CONST               2 (<code object <genexpr> at 0x0000018C18011370, file "app\services\optimization\metrics.py", line 228>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         4 (items)
              GET_ITER
              CALL                     0
              CALL                     1
              STORE_FAST               7 (errors)

230           LOAD_CONST               3 ('n')
              LOAD_FAST                5 (n)

231           LOAD_CONST               4 ('passed')
              LOAD_FAST                6 (passed)

232           LOAD_CONST               5 ('pass_rate')
              LOAD_FAST_BORROW         5 (n)
              TO_BOOL
              POP_JUMP_IF_FALSE       19 (to L2)
              NOT_TAKEN
              LOAD_GLOBAL              9 (round + NULL)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 101 (passed, n)
              BINARY_OP               11 (/)
              LOAD_SMALL_INT           4
              CALL                     2
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               6 (0.0)

233   L3:     LOAD_CONST               7 ('avg_replay_score')
              LOAD_GLOBAL              9 (round + NULL)
              LOAD_GLOBAL             11 (mean + NULL)
              LOAD_CONST               8 (<code object <genexpr> at 0x0000018C180C4140, file "app\services\optimization\metrics.py", line 233>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         4 (items)
              GET_ITER
              CALL                     0
              CALL                     1
              LOAD_SMALL_INT           2
              CALL                     2

234           LOAD_CONST               9 ('avg_turns')
              LOAD_GLOBAL              9 (round + NULL)
              LOAD_GLOBAL             11 (mean + NULL)
              LOAD_CONST              10 (<code object <genexpr> at 0x0000018C18038DF0, file "app\services\optimization\metrics.py", line 234>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         4 (items)
              GET_ITER
              CALL                     0
              CALL                     1
              LOAD_SMALL_INT           2
              CALL                     2

235           LOAD_CONST              11 ('errors')
              LOAD_FAST_BORROW         7 (errors)

229           BUILD_MAP                6
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (out, sid)
              STORE_SUBSCR
              JUMP_BACKWARD          148 (to L1)

225   L4:     END_FOR
              POP_ITER

237           LOAD_FAST_BORROW         2 (out)
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C1802C750, file "app\services\optimization\metrics.py", line 227>:
 227           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                31 (to L5)
               STORE_FAST_LOAD_FAST    17 (r, r)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('passed')
               CALL                     1
               TO_BOOL
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           27 (to L2)
       L4:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           33 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C18011370, file "app\services\optimization\metrics.py", line 228>:
 228           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                54 (to L5)
               STORE_FAST_LOAD_FAST    17 (r, r)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('cell_error')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        26 (to L4)
               NOT_TAKEN
               LOAD_FAST_BORROW         1 (r)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               1 ('error')
               CALL                     1
               TO_BOOL
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           50 (to L2)
       L4:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           56 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C180C4140, file "app\services\optimization\metrics.py", line 233>:
 233           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                16 (to L3)
               STORE_FAST               1 (r)
               LOAD_GLOBAL              1 (_score + NULL)
               LOAD_FAST_BORROW         1 (r)
               CALL                     1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           18 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C18038DF0, file "app\services\optimization\metrics.py", line 234>:
 234           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                41 (to L6)
               STORE_FAST               1 (r)
               LOAD_GLOBAL              1 (len + NULL)
               LOAD_FAST_BORROW         1 (r)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST               0 ('transcript')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L5)
       L3:     NOT_TAKEN
       L4:     POP_TOP
               BUILD_LIST               0
       L5:     CALL                     1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           43 (to L2)
       L6:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L7:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L7 [0] lasti
  L4 to L7 -> L7 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024B30, file "app\services\optimization\metrics.py", line 240>:
240           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('by_strategy')
              LOAD_GLOBAL              0 (dict)
              LOAD_CONST               2 ('return')
              LOAD_GLOBAL              0 (dict)
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _strategy_outcome_rates at 0x0000018C17EC4280, file "app\services\optimization\metrics.py", line 240>:
 240            RESUME                   0

 242            BUILD_MAP                0
                STORE_FAST               1 (out)

 243            LOAD_FAST_BORROW         0 (by_strategy)
                LOAD_ATTR                1 (items + NULL|self)
                CALL                     0
                GET_ITER
        L1:     FOR_ITER               128 (to L9)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   35 (sid, entry)

 244            LOAD_FAST_BORROW         3 (entry)
                LOAD_ATTR                3 (get + NULL|self)
                LOAD_CONST               1 ('n')
                LOAD_SMALL_INT           0
                CALL                     2
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L2)
                NOT_TAKEN
                POP_TOP
                LOAD_SMALL_INT           0
        L2:     STORE_FAST               4 (n)

 245            LOAD_FAST_BORROW         3 (entry)
                LOAD_ATTR                3 (get + NULL|self)
                LOAD_CONST               2 ('outcome_counts')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L3)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
        L3:     STORE_FAST               5 (counts)

 246            LOAD_FAST_BORROW         4 (n)
                LOAD_SMALL_INT           0
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        7 (to L4)
                NOT_TAKEN

 247            BUILD_MAP                0
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (out, sid)
                STORE_SUBSCR

 248            JUMP_BACKWARD           73 (to L1)

 249    L4:     LOAD_FAST_BORROW         5 (counts)
                LOAD_ATTR                1 (items + NULL|self)
                CALL                     0
                GET_ITER
                LOAD_FAST_AND_CLEAR      6 (oc)
                LOAD_FAST_AND_CLEAR      7 (c)
                SWAP                     3
        L5:     BUILD_MAP                0
                SWAP                     2
        L6:     FOR_ITER                24 (to L7)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST  103 (oc, c)
                LOAD_FAST_BORROW         6 (oc)
                LOAD_GLOBAL              5 (round + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 116 (c, n)
                BINARY_OP               11 (/)
                LOAD_SMALL_INT           4
                CALL                     2
                MAP_ADD                  2
                JUMP_BACKWARD           26 (to L6)
        L7:     END_FOR
                POP_ITER
        L8:     SWAP                     3
                STORE_FAST               7 (c)
                STORE_FAST               6 (oc)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (out, sid)
                STORE_SUBSCR
                JUMP_BACKWARD          130 (to L1)

 243    L9:     END_FOR
                POP_ITER

 250            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L10:     SWAP                     2
                POP_TOP

 249            SWAP                     3
                STORE_FAST               7 (c)
                STORE_FAST               6 (oc)
                RERAISE                  0
ExceptionTable:
  L5 to L8 -> L10 [4]

Disassembly of <code object __annotate__ at 0x0000018C18026330, file "app\services\optimization\metrics.py", line 253>:
253           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_GLOBAL              0 (dict)
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _empty_metrics at 0x0000018C18039070, file "app\services\optimization\metrics.py", line 253>:
253           RESUME                   0

254           BUILD_MAP                0

255           LOAD_CONST               0 ('total_runs')
              LOAD_SMALL_INT           0

254           MAP_ADD                  1

256           LOAD_CONST               1 ('pass_rate')
              LOAD_CONST               2 (0.0)

254           MAP_ADD                  1

257           LOAD_CONST               3 ('average_replay_score')
              LOAD_CONST               2 (0.0)

254           MAP_ADD                  1

258           LOAD_CONST               4 ('average_turns')
              LOAD_CONST               2 (0.0)

254           MAP_ADD                  1

259           LOAD_CONST               5 ('outcome_breakdown')
              BUILD_MAP                0

254           MAP_ADD                  1

260           LOAD_CONST               6 ('by_strategy')
              BUILD_MAP                0

254           MAP_ADD                  1

261           LOAD_CONST               7 ('by_scenario')
              BUILD_MAP                0

254           MAP_ADD                  1

262           LOAD_CONST               8 ('strategy_outcome_rates')
              BUILD_MAP                0

254           MAP_ADD                  1

263           LOAD_CONST               9 ('missing_lifecycle_frequency')
              BUILD_MAP                0

254           MAP_ADD                  1

264           LOAD_CONST              10 ('error_count')
              LOAD_SMALL_INT           0

254           MAP_ADD                  1

266           LOAD_CONST              11 ('average_trust_score')
              LOAD_CONST              12 (0.5)

254           MAP_ADD                  1

267           LOAD_CONST              13 ('average_frustration_score')
              LOAD_CONST               2 (0.0)

254           MAP_ADD                  1

268           LOAD_CONST              14 ('divergence_rate')
              LOAD_CONST               2 (0.0)

254           MAP_ADD                  1

269           LOAD_CONST              15 ('escalation_rate')
              LOAD_CONST               2 (0.0)

254           MAP_ADD                  1

270           LOAD_CONST              16 ('dropoff_rate')
              LOAD_CONST               2 (0.0)

254           MAP_ADD                  1

271           LOAD_CONST              17 ('recovery_rate')
              LOAD_CONST               2 (0.0)

254           MAP_ADD                  1

272           LOAD_CONST              18 ('by_strategy_personality')
              BUILD_MAP                0

254           MAP_ADD                  1
              RETURN_VALUE
```
