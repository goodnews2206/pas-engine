# optimization/report

- **pyc:** `app\services\optimization\__pycache__\report.cpython-314.pyc`
- **expected source path (absent):** `app\services\optimization/report.py`
- **co_filename (from bytecode):** `app\services\optimization\report.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** optimization

## Module docstring

```
PAS143A — One-shot optimization report.

Combines metrics + ranking into a CLI/dashboard-ready dict. Honest
about whether strategy overrides actually exercised any engine seam.
Pure deterministic — no LLMs, no I/O.
```

## Imports

`List`, `Optional`, `compute_matrix_metrics`, `datetime`, `metrics`, `rank_strategies`, `ranking`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_behavior_summary`, `_headline`, `_personality_insights`, `_recommendations`, `_warnings`, `generate_optimization_report`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS143A — One-shot optimization report.\n\nCombines metrics + ranking into a CLI/dashboard-ready dict. Honest\nabout whether strategy overrides actually exercised any engine seam.\nPure deterministic — no LLMs, no I/O.\n'
- 'matrix_result'
- 'return'
- '\nReturns:\n  {\n    "headline":             str,\n    "total_runs":           int,\n    "winning_strategy":     {strategy_id, score, ...} | None,\n    "ranked_strategies":    [...],\n    "metrics":              compute_matrix_metrics output,\n    "warnings":             [str, ...],\n    "recommendations":      [str, ...],\n    "any_strategy_effective": bool,\n    "personality_insights":   {strategy_id: {best_personality, worst_personality, ...}},\n    "behavior_summary":       {avg_trust, avg_frustration, divergence_rate,\n                               escalation_rate, dropoff_rate, recovery_rate,\n                               highest_dropoff_strategy, best_recovery_strategy},\n    "generated_at":         ISO timestamp,\n  }\n\nEmpty / malformed matrix produces a coherent zero-shape report.\n'
- 'total_runs'
- 'by_strategy'
- 'headline'
- 'winning_strategy'
- 'ranked_strategies'
- 'metrics'
- 'warnings'
- 'recommendations'
- 'any_strategy_effective'
- 'personality_insights'
- 'behavior_summary'
- 'generated_at'
- 'effective'
- '\nFor each strategy with cross-tab data, identify the personality it\npairs best with (highest pass rate, ties broken by booked rate)\nand the personality it does worst against. Returns {} when no\nstrategy×personality data is available.\n'
- 'by_strategy_personality'
- 'best_personality'
- 'best_pass_rate'
- 'pass_rate'
- 'best_booked_rate'
- 'booked_rate'
- 'worst_personality'
- 'worst_pass_rate'
- 'worst_booked_rate'
- 'personalities_evaluated'
- 'avg_trust'
- 'average_trust_score'
- 'avg_frustration'
- 'average_frustration_score'
- 'divergence_rate'
- 'escalation_rate'
- 'dropoff_rate'
- 'recovery_rate'
- 'highest_divergence_strategy'
- 'best_trust_strategy'
- 'divergence_count'
- 'trust_avg'
- 'n_strategies'
- 'any_effective'
- 'No matrix runs to report.'
- ' runs across '
- ' strategies'
- '. No ranked winner.'
- '. Ranked winner: '
- 'strategy_id'
- ' (score '
- 'score'
- '.1f'
- ') — but no strategy yet alters PASEngine; rankings are infrastructure-only.'
- 'components'
- 'infrastructure-only'
- '. Winner: '
- 'ranked'
- 'No runs in matrix — nothing to compare.'
- 'Strategy variants are being measured through the matrix, but engine behaviour is not yet altered by strategy overrides.'
- 'error_count'
- ' cell(s) errored — investigate `cell_error` before trusting rankings.'
- 'Matrix-wide pass rate '
- '.0%'
- ' below 50%.'
- 'average_replay_score'
- 'Average replay score '
- ' below 70 — lifecycle coverage thin across strategies.'
- 'Top score tied across: '
- 'High frustration accumulation detected across the matrix (avg '
- "Strategy '"
- "' performs poorly against '"
- "' leads (pass "
- 'Add an engine seam (e.g. callback prompt copy) so callback strategies produce observable differences in the simulation.'
- 'Top strategy still scores below 60 — add scenarios that exercise the lifecycle steps currently most-missed.'
- 'Consider retiring: '
- ' (score < half of winner).'
- 'missing_lifecycle_frequency'
- "Most-missed lifecycle step across the matrix: '"
- "' ("
- ' cells). Target a scenario or engine seam that closes it.'
- "Winner '"
- "' performs best against '"
- "); weakest against '"
- "' (pass "

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS143A — One-shot optimization report.\n\nCombines metrics + ranking into a CLI/dashboard-ready dict. Honest\nabout whether strategy overrides actually exercised any engine seam.\nPure deterministic — no LLMs, no I/O.\n')
              STORE_NAME               0 (__doc__)

  9           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('datetime', 'timezone'))
              IMPORT_NAME              1 (datetime)
              IMPORT_FROM              1 (datetime)
              STORE_NAME               1 (datetime)
              IMPORT_FROM              2 (timezone)
              STORE_NAME               2 (timezone)
              POP_TOP

 10           LOAD_SMALL_INT           0
              LOAD_CONST               2 (('List', 'Optional'))
              IMPORT_NAME              3 (typing)
              IMPORT_FROM              4 (List)
              STORE_NAME               4 (List)
              IMPORT_FROM              5 (Optional)
              STORE_NAME               5 (Optional)
              POP_TOP

 12           LOAD_SMALL_INT           1
              LOAD_CONST               3 (('compute_matrix_metrics',))
              IMPORT_NAME              6 (metrics)
              IMPORT_FROM              7 (compute_matrix_metrics)
              STORE_NAME               7 (compute_matrix_metrics)
              POP_TOP

 13           LOAD_SMALL_INT           1
              LOAD_CONST               4 (('rank_strategies',))
              IMPORT_NAME              8 (ranking)
              IMPORT_FROM              9 (rank_strategies)
              STORE_NAME               9 (rank_strategies)
              POP_TOP

 16           LOAD_CONST               5 (<code object __annotate__ at 0x0000018C18024C30, file "app\services\optimization\report.py", line 16>)
              MAKE_FUNCTION
              LOAD_CONST               6 (<code object generate_optimization_report at 0x0000018C17ED1F60, file "app\services\optimization\report.py", line 16>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              10 (generate_optimization_report)

 68           LOAD_CONST               7 (<code object __annotate__ at 0x0000018C18025530, file "app\services\optimization\report.py", line 68>)
              MAKE_FUNCTION
              LOAD_CONST               8 (<code object _personality_insights at 0x0000018C17D8C2A0, file "app\services\optimization\report.py", line 68>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              11 (_personality_insights)

102           LOAD_CONST               9 (<code object __annotate__ at 0x0000018C18025C30, file "app\services\optimization\report.py", line 102>)
              MAKE_FUNCTION
              LOAD_CONST              10 (<code object _behavior_summary at 0x0000018C17EE1CC0, file "app\services\optimization\report.py", line 102>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              12 (_behavior_summary)

131           LOAD_CONST              11 (<code object __annotate__ at 0x0000018C18053870, file "app\services\optimization\report.py", line 131>)
              MAKE_FUNCTION
              LOAD_CONST              12 (<code object _headline at 0x0000018C1794ED80, file "app\services\optimization\report.py", line 131>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              13 (_headline)

148           LOAD_CONST              18 ((None,))
              LOAD_CONST              14 (<code object __annotate__ at 0x0000018C17F96590, file "app\services\optimization\report.py", line 148>)
              MAKE_FUNCTION
              LOAD_CONST              15 (<code object _warnings at 0x0000018C17D50FF0, file "app\services\optimization\report.py", line 148>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              14 (_warnings)

208           LOAD_CONST              18 ((None,))
              LOAD_CONST              16 (<code object __annotate__ at 0x0000018C17F96420, file "app\services\optimization\report.py", line 208>)
              MAKE_FUNCTION
              LOAD_CONST              17 (<code object _recommendations at 0x0000018C17F691C0, file "app\services\optimization\report.py", line 208>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              15 (_recommendations)
              LOAD_CONST              13 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "app\services\optimization\report.py", line 16>:
 16           RESUME                   0
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

Disassembly of <code object generate_optimization_report at 0x0000018C17ED1F60, file "app\services\optimization\report.py", line 16>:
 16           RESUME                   0

 37           LOAD_GLOBAL              1 (compute_matrix_metrics + NULL)
              LOAD_FAST_BORROW         0 (matrix_result)
              CALL                     1
              STORE_FAST               1 (metrics)

 38           LOAD_GLOBAL              3 (rank_strategies + NULL)
              LOAD_FAST_BORROW         1 (metrics)
              CALL                     1
              STORE_FAST               2 (ranked)

 40           LOAD_FAST_BORROW         1 (metrics)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               1 ('total_runs')
              LOAD_SMALL_INT           0
              CALL                     2
              STORE_FAST               3 (total_runs)

 41           LOAD_FAST_BORROW         1 (metrics)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               2 ('by_strategy')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L1:     STORE_FAST               4 (by_strategy)

 42           LOAD_GLOBAL              6 (any)
              COPY                     1
              LOAD_COMMON_CONSTANT     4 (<built-in function any>)
              IS_OP                    0 (is)
              POP_JUMP_IF_FALSE       42 (to L5)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18053E10, file "app\services\optimization\report.py", line 42>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         4 (by_strategy)
              LOAD_ATTR                9 (values + NULL|self)
              CALL                     0
              GET_ITER
              CALL                     0
      L2:     FOR_ITER                12 (to L4)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)
      L3:     POP_ITER
              LOAD_CONST               4 (True)
              JUMP_FORWARD            31 (to L6)
      L4:     END_FOR
              POP_ITER
              LOAD_CONST               5 (False)
              JUMP_FORWARD            27 (to L6)
      L5:     PUSH_NULL
              LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18053E10, file "app\services\optimization\report.py", line 42>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         4 (by_strategy)
              LOAD_ATTR                9 (values + NULL|self)
              CALL                     0
              GET_ITER
              CALL                     0
              CALL                     1
      L6:     STORE_FAST               5 (any_effective)

 44           LOAD_FAST_BORROW         2 (ranked)
              TO_BOOL
              POP_JUMP_IF_FALSE       10 (to L7)
              NOT_TAKEN
              LOAD_FAST_BORROW         2 (ranked)
              LOAD_SMALL_INT           0
              BINARY_OP               26 ([])
              JUMP_FORWARD             1 (to L8)
      L7:     LOAD_CONST               6 (None)
      L8:     STORE_FAST               6 (winner)

 45           LOAD_GLOBAL             11 (_headline + NULL)
              LOAD_FAST_BORROW         3 (total_runs)
              LOAD_GLOBAL             13 (len + NULL)
              LOAD_FAST_BORROW         4 (by_strategy)
              CALL                     1
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 101 (winner, any_effective)
              CALL                     4
              STORE_FAST               7 (headline)

 47           LOAD_GLOBAL             15 (_personality_insights + NULL)
              LOAD_FAST_BORROW         1 (metrics)
              CALL                     1
              STORE_FAST               8 (personality_insights)

 48           LOAD_GLOBAL             17 (_behavior_summary + NULL)
              LOAD_FAST_BORROW         1 (metrics)
              CALL                     1
              STORE_FAST               9 (behavior_summary)

 50           LOAD_GLOBAL             19 (_warnings + NULL)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (metrics, ranked)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 88 (any_effective, personality_insights)
              CALL                     4
              STORE_FAST              10 (warnings)

 51           LOAD_GLOBAL             21 (_recommendations + NULL)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (metrics, ranked)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 88 (any_effective, personality_insights)
              CALL                     4
              STORE_FAST              11 (recommendations)

 54           LOAD_CONST               7 ('headline')
              LOAD_FAST_BORROW         7 (headline)

 55           LOAD_CONST               1 ('total_runs')
              LOAD_FAST_BORROW         3 (total_runs)

 56           LOAD_CONST               8 ('winning_strategy')
              LOAD_FAST_BORROW         6 (winner)

 57           LOAD_CONST               9 ('ranked_strategies')
              LOAD_FAST_BORROW         2 (ranked)

 58           LOAD_CONST              10 ('metrics')
              LOAD_FAST_BORROW         1 (metrics)

 59           LOAD_CONST              11 ('warnings')
              LOAD_FAST_BORROW        10 (warnings)

 60           LOAD_CONST              12 ('recommendations')
              LOAD_FAST_BORROW        11 (recommendations)

 61           LOAD_CONST              13 ('any_strategy_effective')
              LOAD_FAST_BORROW         5 (any_effective)

 62           LOAD_CONST              14 ('personality_insights')
              LOAD_FAST_BORROW         8 (personality_insights)

 63           LOAD_CONST              15 ('behavior_summary')
              LOAD_FAST_BORROW         9 (behavior_summary)

 64           LOAD_CONST              16 ('generated_at')
              LOAD_GLOBAL             22 (datetime)
              LOAD_ATTR               24 (now)
              PUSH_NULL
              LOAD_GLOBAL             26 (timezone)
              LOAD_ATTR               28 (utc)
              CALL                     1
              LOAD_ATTR               31 (isoformat + NULL|self)
              CALL                     0

 53           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18053E10, file "app\services\optimization\report.py", line 42>:
  42           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                21 (to L3)
               STORE_FAST_LOAD_FAST    17 (entry, entry)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('effective')
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

Disassembly of <code object __annotate__ at 0x0000018C18025530, file "app\services\optimization\report.py", line 68>:
 68           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('metrics')
              LOAD_GLOBAL              0 (dict)
              LOAD_CONST               2 ('return')
              LOAD_GLOBAL              0 (dict)
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _personality_insights at 0x0000018C17D8C2A0, file "app\services\optimization\report.py", line 68>:
 68           RESUME                   0

 75           LOAD_FAST_BORROW         0 (metrics)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               1 ('by_strategy_personality')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L1:     STORE_FAST               1 (cross)

 76           BUILD_MAP                0
              STORE_FAST               2 (out)

 77           LOAD_FAST_BORROW         1 (cross)
              LOAD_ATTR                3 (items + NULL|self)
              CALL                     0
              GET_ITER
      L2:     FOR_ITER               171 (to L4)
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST   52 (sid, by_p)

 78           LOAD_FAST_BORROW         4 (by_p)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN

 79           JUMP_BACKWARD           15 (to L2)

 81   L3:     LOAD_GLOBAL              5 (sorted + NULL)

 82           LOAD_FAST_BORROW         4 (by_p)
              LOAD_ATTR                3 (items + NULL|self)
              CALL                     0

 83           LOAD_CONST               2 (<code object <lambda> at 0x0000018C17FE13E0, file "app\services\optimization\report.py", line 83>)
              MAKE_FUNCTION

 86           LOAD_CONST               3 (True)

 81           LOAD_CONST               4 (('key', 'reverse'))
              CALL_KW                  3
              STORE_FAST               5 (ranked_pcells)

 88           LOAD_FAST_BORROW         5 (ranked_pcells)
              LOAD_SMALL_INT           0
              BINARY_OP               26 ([])
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST  103 (best_pid, best_cell)

 89           LOAD_FAST_BORROW         5 (ranked_pcells)
              LOAD_CONST              15 (-1)
              BINARY_OP               26 ([])
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST  137 (worst_pid, worst_cell)

 91           LOAD_CONST               5 ('best_personality')
              LOAD_FAST_BORROW         6 (best_pid)

 92           LOAD_CONST               6 ('best_pass_rate')
              LOAD_FAST_BORROW         7 (best_cell)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               7 ('pass_rate')
              LOAD_CONST               8 (0.0)
              CALL                     2

 93           LOAD_CONST               9 ('best_booked_rate')
              LOAD_FAST_BORROW         7 (best_cell)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              10 ('booked_rate')
              LOAD_CONST               8 (0.0)
              CALL                     2

 94           LOAD_CONST              11 ('worst_personality')
              LOAD_FAST_BORROW         8 (worst_pid)

 95           LOAD_CONST              12 ('worst_pass_rate')
              LOAD_FAST_BORROW         9 (worst_cell)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               7 ('pass_rate')
              LOAD_CONST               8 (0.0)
              CALL                     2

 96           LOAD_CONST              13 ('worst_booked_rate')
              LOAD_FAST_BORROW         9 (worst_cell)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              10 ('booked_rate')
              LOAD_CONST               8 (0.0)
              CALL                     2

 97           LOAD_CONST              14 ('personalities_evaluated')
              LOAD_GLOBAL              7 (list + NULL)
              LOAD_FAST_BORROW         4 (by_p)
              LOAD_ATTR                9 (keys + NULL|self)
              CALL                     0
              CALL                     1

 90           BUILD_MAP                7
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (out, sid)
              STORE_SUBSCR
              JUMP_BACKWARD          173 (to L2)

 77   L4:     END_FOR
              POP_ITER

 99           LOAD_FAST_BORROW         2 (out)
              RETURN_VALUE

Disassembly of <code object <lambda> at 0x0000018C17FE13E0, file "app\services\optimization\report.py", line 83>:
 83           RESUME                   0
              LOAD_FAST_BORROW         0 (kv)
              LOAD_SMALL_INT           1
              BINARY_OP               26 ([])
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               1 ('pass_rate')
              LOAD_CONST               2 (0.0)
              CALL                     2

 84           LOAD_FAST_BORROW         0 (kv)
              LOAD_SMALL_INT           1
              BINARY_OP               26 ([])
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               3 ('booked_rate')
              LOAD_CONST               2 (0.0)
              CALL                     2

 85           LOAD_FAST_BORROW         0 (kv)
              LOAD_SMALL_INT           0
              BINARY_OP               26 ([])

 83           BUILD_TUPLE              3
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025C30, file "app\services\optimization\report.py", line 102>:
102           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('metrics')
              LOAD_GLOBAL              0 (dict)
              LOAD_CONST               2 ('return')
              LOAD_GLOBAL              0 (dict)
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _behavior_summary at 0x0000018C17EE1CC0, file "app\services\optimization\report.py", line 102>:
  --           MAKE_CELL                5 (_div)
               MAKE_CELL                6 (_trust_score)

 102           RESUME                   0

 103           LOAD_FAST_BORROW         0 (metrics)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('by_strategy')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               BUILD_MAP                0
       L1:     STORE_FAST               1 (by_strategy)

 106           LOAD_GLOBAL              3 (list + NULL)
               LOAD_FAST_BORROW         1 (by_strategy)
               LOAD_ATTR                5 (items + NULL|self)
               CALL                     0
               CALL                     1
               STORE_FAST               2 (items)

 108           LOAD_CONST               1 (<code object _div at 0x0000018C18024930, file "app\services\optimization\report.py", line 108>)
               MAKE_FUNCTION
               STORE_DEREF              5 (_div)

 111           LOAD_CONST               2 (<code object _trust_score at 0x0000018C18025730, file "app\services\optimization\report.py", line 111>)
               MAKE_FUNCTION
               STORE_DEREF              6 (_trust_score)

 114           LOAD_FAST_BORROW         2 (items)
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L2)
               NOT_TAKEN
               LOAD_GLOBAL              7 (sorted + NULL)
               LOAD_FAST_BORROW         2 (items)
               LOAD_FAST_BORROW         5 (_div)
               BUILD_TUPLE              1
               LOAD_CONST               3 (<code object <lambda> at 0x0000018C17FBFEE0, file "app\services\optimization\report.py", line 114>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               LOAD_CONST               4 (('key',))
               CALL_KW                  2
               JUMP_FORWARD             1 (to L3)
       L2:     BUILD_LIST               0
       L3:     STORE_FAST               3 (highest_div)

 115           LOAD_FAST_BORROW         2 (items)
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L4)
               NOT_TAKEN
               LOAD_GLOBAL              7 (sorted + NULL)
               LOAD_FAST_BORROW         2 (items)
               LOAD_FAST_BORROW         6 (_trust_score)
               BUILD_TUPLE              1
               LOAD_CONST               5 (<code object <lambda> at 0x0000018C180E88B0, file "app\services\optimization\report.py", line 115>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               LOAD_CONST               4 (('key',))
               CALL_KW                  2
               JUMP_FORWARD             1 (to L5)
       L4:     BUILD_LIST               0
       L5:     STORE_FAST               4 (highest_trust)

 118           LOAD_CONST               6 ('avg_trust')
               LOAD_FAST_BORROW         0 (metrics)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               7 ('average_trust_score')
               LOAD_CONST               8 (0.5)
               CALL                     2

 119           LOAD_CONST               9 ('avg_frustration')
               LOAD_FAST_BORROW         0 (metrics)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST              10 ('average_frustration_score')
               LOAD_CONST              11 (0.0)
               CALL                     2

 120           LOAD_CONST              12 ('divergence_rate')
               LOAD_FAST_BORROW         0 (metrics)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST              12 ('divergence_rate')
               LOAD_CONST              11 (0.0)
               CALL                     2

 121           LOAD_CONST              13 ('escalation_rate')
               LOAD_FAST_BORROW         0 (metrics)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST              13 ('escalation_rate')
               LOAD_CONST              11 (0.0)
               CALL                     2

 122           LOAD_CONST              14 ('dropoff_rate')
               LOAD_FAST_BORROW         0 (metrics)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST              14 ('dropoff_rate')
               LOAD_CONST              11 (0.0)
               CALL                     2

 123           LOAD_CONST              15 ('recovery_rate')
               LOAD_FAST_BORROW         0 (metrics)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST              15 ('recovery_rate')
               LOAD_CONST              11 (0.0)
               CALL                     2

 124           LOAD_CONST              16 ('highest_divergence_strategy')
               LOAD_FAST_BORROW         3 (highest_div)
               TO_BOOL
               POP_JUMP_IF_FALSE       17 (to L6)
               NOT_TAKEN
               LOAD_FAST_BORROW         3 (highest_div)
               LOAD_SMALL_INT           0
               BINARY_OP               26 ([])
               LOAD_SMALL_INT           0
               BINARY_OP               26 ([])
               JUMP_FORWARD             1 (to L7)
       L6:     LOAD_CONST              17 (None)

 125   L7:     LOAD_CONST              18 ('best_trust_strategy')
               LOAD_FAST_BORROW         4 (highest_trust)
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L8)
               NOT_TAKEN
               LOAD_FAST_BORROW         4 (highest_trust)
               LOAD_SMALL_INT           0
               BINARY_OP               26 ([])
               LOAD_SMALL_INT           0
               BINARY_OP               26 ([])

 117           BUILD_MAP                8
               RETURN_VALUE

 125   L8:     LOAD_CONST              17 (None)

 117           BUILD_MAP                8
               RETURN_VALUE

Disassembly of <code object _div at 0x0000018C18024930, file "app\services\optimization\report.py", line 108>:
108           RESUME                   0

109           LOAD_FAST_BORROW         0 (entry)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               0 ('divergence_count')
              LOAD_SMALL_INT           0
              CALL                     2
              RETURN_VALUE

Disassembly of <code object _trust_score at 0x0000018C18025730, file "app\services\optimization\report.py", line 111>:
111           RESUME                   0

112           LOAD_FAST_BORROW         0 (entry)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               0 ('trust_avg')
              LOAD_CONST               1 (0.5)
              CALL                     2
              RETURN_VALUE

Disassembly of <code object <lambda> at 0x0000018C17FBFEE0, file "app\services\optimization\report.py", line 114>:
  --           COPY_FREE_VARS           1

 114           RESUME                   0
               LOAD_DEREF               1 (_div)
               PUSH_NULL
               LOAD_FAST_BORROW         0 (kv)
               LOAD_SMALL_INT           1
               BINARY_OP               26 ([])
               CALL                     1
               UNARY_NEGATIVE
               LOAD_FAST_BORROW         0 (kv)
               LOAD_SMALL_INT           0
               BINARY_OP               26 ([])
               BUILD_TUPLE              2
               RETURN_VALUE

Disassembly of <code object <lambda> at 0x0000018C180E88B0, file "app\services\optimization\report.py", line 115>:
  --           COPY_FREE_VARS           1

 115           RESUME                   0
               LOAD_DEREF               1 (_trust_score)
               PUSH_NULL
               LOAD_FAST_BORROW         0 (kv)
               LOAD_SMALL_INT           1
               BINARY_OP               26 ([])
               CALL                     1
               UNARY_NEGATIVE
               LOAD_FAST_BORROW         0 (kv)
               LOAD_SMALL_INT           0
               BINARY_OP               26 ([])
               BUILD_TUPLE              2
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18053870, file "app\services\optimization\report.py", line 131>:
131           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('total_runs')
              LOAD_GLOBAL              0 (int)
              LOAD_CONST               2 ('n_strategies')
              LOAD_GLOBAL              0 (int)
              LOAD_CONST               3 ('any_effective')
              LOAD_GLOBAL              2 (bool)
              LOAD_CONST               4 ('return')
              LOAD_GLOBAL              4 (str)
              BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object _headline at 0x0000018C1794ED80, file "app\services\optimization\report.py", line 131>:
131           RESUME                   0

132           LOAD_FAST_BORROW         0 (total_runs)
              LOAD_SMALL_INT           0
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN

133           LOAD_CONST               1 ('No matrix runs to report.')
              RETURN_VALUE

134   L1:     LOAD_FAST_BORROW         0 (total_runs)
              FORMAT_SIMPLE
              LOAD_CONST               2 (' runs across ')
              LOAD_FAST_BORROW         1 (n_strategies)
              FORMAT_SIMPLE
              LOAD_CONST               3 (' strategies')
              BUILD_STRING             4
              STORE_FAST               4 (base)

135           LOAD_FAST_BORROW         2 (winner)
              POP_JUMP_IF_NOT_NONE     6 (to L2)
              NOT_TAKEN

136           LOAD_FAST_BORROW         4 (base)
              FORMAT_SIMPLE
              LOAD_CONST               4 ('. No ranked winner.')
              BUILD_STRING             2
              RETURN_VALUE

137   L2:     LOAD_FAST_BORROW         3 (any_effective)
              TO_BOOL
              POP_JUMP_IF_TRUE        27 (to L3)
              NOT_TAKEN

139           LOAD_FAST_BORROW         4 (base)
              FORMAT_SIMPLE
              LOAD_CONST               5 ('. Ranked winner: ')
              LOAD_FAST_BORROW         2 (winner)
              LOAD_CONST               6 ('strategy_id')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               7 (' (score ')
              LOAD_FAST_BORROW         2 (winner)
              LOAD_CONST               8 ('score')
              BINARY_OP               26 ([])
              LOAD_CONST               9 ('.1f')
              FORMAT_WITH_SPEC
              LOAD_CONST              10 (') — but no strategy yet alters PASEngine; rankings are infrastructure-only.')
              BUILD_STRING             6

138           RETURN_VALUE

142   L3:     LOAD_FAST_BORROW         2 (winner)
              LOAD_CONST              11 ('components')
              BINARY_OP               26 ([])
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              12 ('effective')
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST              12 ('effective')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST              13 ('infrastructure-only')
      L5:     STORE_FAST               5 (eff)

144           LOAD_FAST_BORROW         4 (base)
              FORMAT_SIMPLE
              LOAD_CONST              14 ('. Winner: ')
              LOAD_FAST_BORROW         2 (winner)
              LOAD_CONST               6 ('strategy_id')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               7 (' (score ')
              LOAD_FAST_BORROW         2 (winner)
              LOAD_CONST               8 ('score')
              BINARY_OP               26 ([])
              LOAD_CONST               9 ('.1f')
              FORMAT_WITH_SPEC
              LOAD_CONST              15 (', ')
              LOAD_FAST_BORROW         5 (eff)
              FORMAT_SIMPLE
              LOAD_CONST              16 (').')
              BUILD_STRING             8

143           RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17F96590, file "app\services\optimization\report.py", line 148>:
148           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('metrics')

149           LOAD_GLOBAL              0 (dict)

148           LOAD_CONST               2 ('ranked')

150           LOAD_GLOBAL              2 (List)
              LOAD_GLOBAL              0 (dict)
              BINARY_OP               26 ([])

148           LOAD_CONST               3 ('any_effective')

151           LOAD_GLOBAL              4 (bool)

148           LOAD_CONST               4 ('personality_insights')

152           LOAD_GLOBAL              6 (Optional)
              LOAD_GLOBAL              0 (dict)
              BINARY_OP               26 ([])

148           LOAD_CONST               5 ('return')

153           LOAD_GLOBAL              2 (List)
              LOAD_GLOBAL              8 (str)
              BINARY_OP               26 ([])

148           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _warnings at 0x0000018C17D50FF0, file "app\services\optimization\report.py", line 148>:
 148            RESUME                   0

 154            BUILD_LIST               0
                STORE_FAST               4 (w)

 156            LOAD_FAST_BORROW         0 (metrics)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               0 ('total_runs')
                LOAD_SMALL_INT           0
                CALL                     2
                LOAD_SMALL_INT           0
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       20 (to L1)
                NOT_TAKEN

 157            LOAD_FAST_BORROW         4 (w)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_CONST               1 ('No runs in matrix — nothing to compare.')
                CALL                     1
                POP_TOP

 158            LOAD_FAST_BORROW         4 (w)
                RETURN_VALUE

 160    L1:     LOAD_FAST_BORROW         2 (any_effective)
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L2)
                NOT_TAKEN

 163            LOAD_FAST_BORROW         4 (w)
                LOAD_ATTR                3 (append + NULL|self)

 164            LOAD_CONST               2 ('Strategy variants are being measured through the matrix, but engine behaviour is not yet altered by strategy overrides.')

 163            CALL                     1
                POP_TOP

 168    L2:     LOAD_FAST_BORROW         0 (metrics)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               3 ('error_count')
                LOAD_SMALL_INT           0
                CALL                     2
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L3)
                NOT_TAKEN
                POP_TOP
                LOAD_SMALL_INT           0
        L3:     STORE_FAST               5 (err)

 169            LOAD_FAST_BORROW         5 (err)
                TO_BOOL
                POP_JUMP_IF_FALSE       21 (to L4)
                NOT_TAKEN

 170            LOAD_FAST_BORROW         4 (w)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_FAST_BORROW         5 (err)
                FORMAT_SIMPLE
                LOAD_CONST               4 (' cell(s) errored — investigate `cell_error` before trusting rankings.')
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 172    L4:     LOAD_FAST_BORROW         0 (metrics)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               5 ('pass_rate')
                LOAD_CONST               6 (0.0)
                CALL                     2
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               6 (0.0)
        L5:     STORE_FAST               6 (pr)

 173            LOAD_FAST_BORROW         6 (pr)
                LOAD_CONST               7 (0.5)
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE       23 (to L6)
                NOT_TAKEN

 174            LOAD_FAST_BORROW         4 (w)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_CONST               8 ('Matrix-wide pass rate ')
                LOAD_FAST_BORROW         6 (pr)
                LOAD_CONST               9 ('.0%')
                FORMAT_WITH_SPEC
                LOAD_CONST              10 (' below 50%.')
                BUILD_STRING             3
                CALL                     1
                POP_TOP

 176    L6:     LOAD_FAST_BORROW         0 (metrics)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST              11 ('average_replay_score')
                LOAD_CONST               6 (0.0)
                CALL                     2
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               6 (0.0)
        L7:     STORE_FAST               7 (avg)

 177            LOAD_FAST_BORROW         7 (avg)
                LOAD_SMALL_INT          70
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE       22 (to L8)
                NOT_TAKEN

 178            LOAD_FAST_BORROW         4 (w)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_CONST              12 ('Average replay score ')
                LOAD_FAST_BORROW         7 (avg)
                FORMAT_SIMPLE
                LOAD_CONST              13 (' below 70 — lifecycle coverage thin across strategies.')
                BUILD_STRING             3
                CALL                     1
                POP_TOP

 181    L8:     LOAD_GLOBAL              5 (len + NULL)
                LOAD_FAST_BORROW         1 (ranked)
                CALL                     1
                LOAD_SMALL_INT           2
                COMPARE_OP             188 (bool(>=))
                POP_JUMP_IF_FALSE      174 (to L15)
                NOT_TAKEN
                LOAD_GLOBAL              7 (abs + NULL)
                LOAD_FAST_BORROW         1 (ranked)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                LOAD_CONST              14 ('score')
                BINARY_OP               26 ([])
                LOAD_FAST_BORROW         1 (ranked)
                LOAD_SMALL_INT           1
                BINARY_OP               26 ([])
                LOAD_CONST              14 ('score')
                BINARY_OP               26 ([])
                BINARY_OP               10 (-)
                CALL                     1
                LOAD_CONST              15 (1e-06)
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE      123 (to L15)
                NOT_TAKEN

 182            LOAD_FAST_BORROW         1 (ranked)
                GET_ITER
                LOAD_FAST_AND_CLEAR      8 (r)
                SWAP                     2
        L9:     BUILD_LIST               0
                SWAP                     2
       L10:     FOR_ITER                58 (to L13)
                STORE_FAST               8 (r)
                LOAD_GLOBAL              7 (abs + NULL)
                LOAD_FAST_BORROW         8 (r)
                LOAD_CONST              14 ('score')
                BINARY_OP               26 ([])
                LOAD_FAST_BORROW         1 (ranked)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                LOAD_CONST              14 ('score')
                BINARY_OP               26 ([])
                BINARY_OP               10 (-)
                CALL                     1
                LOAD_CONST              15 (1e-06)
                COMPARE_OP              18 (bool(<))
       L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           49 (to L10)
       L12:     LOAD_FAST_BORROW         8 (r)
                LOAD_CONST              16 ('strategy_id')
                BINARY_OP               26 ([])
                LIST_APPEND              2
                JUMP_BACKWARD           60 (to L10)
       L13:     END_FOR
                POP_ITER
       L14:     STORE_FAST               9 (tied_ids)
                STORE_FAST               8 (r)

 183            LOAD_GLOBAL              5 (len + NULL)
                LOAD_FAST_BORROW         9 (tied_ids)
                CALL                     1
                LOAD_SMALL_INT           2
                COMPARE_OP             188 (bool(>=))
                POP_JUMP_IF_FALSE       37 (to L15)
                NOT_TAKEN

 184            LOAD_FAST_BORROW         4 (w)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_CONST              17 ('Top score tied across: ')
                LOAD_CONST              18 (', ')
                LOAD_ATTR                9 (join + NULL|self)
                LOAD_FAST_BORROW         9 (tied_ids)
                CALL                     1
                FORMAT_SIMPLE
                LOAD_CONST              19 ('.')
                BUILD_STRING             3
                CALL                     1
                POP_TOP

 187   L15:     LOAD_FAST_BORROW         0 (metrics)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST              20 ('average_frustration_score')
                LOAD_CONST               6 (0.0)
                CALL                     2
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L16)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               6 (0.0)
       L16:     STORE_FAST              10 (avg_frust)

 188            LOAD_FAST_BORROW        10 (avg_frust)
                LOAD_CONST               7 (0.5)
                COMPARE_OP             188 (bool(>=))
                POP_JUMP_IF_FALSE       22 (to L17)
                NOT_TAKEN

 189            LOAD_FAST_BORROW         4 (w)
                LOAD_ATTR                3 (append + NULL|self)

 190            LOAD_CONST              21 ('High frustration accumulation detected across the matrix (avg ')

 191            LOAD_FAST_BORROW        10 (avg_frust)
                FORMAT_SIMPLE
                LOAD_CONST              22 (').')

 190            BUILD_STRING             3

 189            CALL                     1
                POP_TOP

 195   L17:     LOAD_FAST                3 (personality_insights)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L18)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
       L18:     STORE_FAST              11 (pi)

 196            LOAD_FAST_BORROW        11 (pi)
                LOAD_ATTR               11 (items + NULL|self)
                CALL                     0
                GET_ITER
       L19:     FOR_ITER                75 (to L21)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST  205 (sid, info)

 197            LOAD_FAST_BORROW        13 (info)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST              23 ('worst_pass_rate')
                LOAD_CONST              24 (1.0)
                CALL                     2
                STORE_FAST              14 (worst_pass)

 198            LOAD_FAST_BORROW        14 (worst_pass)
                LOAD_CONST               6 (0.0)
                COMPARE_OP              58 (bool(<=))
                POP_JUMP_IF_TRUE         3 (to L20)
                NOT_TAKEN
                JUMP_BACKWARD           32 (to L19)

 199   L20:     LOAD_FAST_BORROW         4 (w)
                LOAD_ATTR                3 (append + NULL|self)

 200            LOAD_CONST              25 ("Strategy '")
                LOAD_FAST_BORROW        12 (sid)
                FORMAT_SIMPLE
                LOAD_CONST              26 ("' performs poorly against '")

 201            LOAD_FAST_BORROW        13 (info)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST              27 ('worst_personality')
                CALL                     1
                FORMAT_SIMPLE
                LOAD_CONST              28 ("' leads (pass ")

 202            LOAD_FAST_BORROW        14 (worst_pass)
                LOAD_CONST               9 ('.0%')
                FORMAT_WITH_SPEC
                LOAD_CONST              22 (').')

 200            BUILD_STRING             7

 199            CALL                     1
                POP_TOP
                JUMP_BACKWARD           77 (to L19)

 196   L21:     END_FOR
                POP_ITER

 205            LOAD_FAST_BORROW         4 (w)
                RETURN_VALUE

  --   L22:     SWAP                     2
                POP_TOP

 182            SWAP                     2
                STORE_FAST               8 (r)
                RERAISE                  0
ExceptionTable:
  L9 to L11 -> L22 [2]
  L12 to L14 -> L22 [2]

Disassembly of <code object __annotate__ at 0x0000018C17F96420, file "app\services\optimization\report.py", line 208>:
208           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('metrics')

209           LOAD_GLOBAL              0 (dict)

208           LOAD_CONST               2 ('ranked')

210           LOAD_GLOBAL              2 (List)
              LOAD_GLOBAL              0 (dict)
              BINARY_OP               26 ([])

208           LOAD_CONST               3 ('any_effective')

211           LOAD_GLOBAL              4 (bool)

208           LOAD_CONST               4 ('personality_insights')

212           LOAD_GLOBAL              6 (Optional)
              LOAD_GLOBAL              0 (dict)
              BINARY_OP               26 ([])

208           LOAD_CONST               5 ('return')

213           LOAD_GLOBAL              2 (List)
              LOAD_GLOBAL              8 (str)
              BINARY_OP               26 ([])

208           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _recommendations at 0x0000018C17F691C0, file "app\services\optimization\report.py", line 208>:
 208            RESUME                   0

 214            BUILD_LIST               0
                STORE_FAST               4 (recs)

 216            LOAD_FAST_BORROW         2 (any_effective)
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L1)
                NOT_TAKEN

 217            LOAD_FAST_BORROW         4 (recs)
                LOAD_ATTR                1 (append + NULL|self)

 218            LOAD_CONST               0 ('Add an engine seam (e.g. callback prompt copy) so callback strategies produce observable differences in the simulation.')

 217            CALL                     1
                POP_TOP

 222    L1:     LOAD_FAST_BORROW         1 (ranked)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L2)
                NOT_TAKEN

 223            LOAD_FAST_BORROW         4 (recs)
                RETURN_VALUE

 225    L2:     LOAD_FAST_BORROW         1 (ranked)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                STORE_FAST               5 (winner)

 226            LOAD_FAST_BORROW         5 (winner)
                LOAD_CONST               1 ('score')
                BINARY_OP               26 ([])
                LOAD_SMALL_INT          60
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE       18 (to L3)
                NOT_TAKEN

 227            LOAD_FAST_BORROW         4 (recs)
                LOAD_ATTR                1 (append + NULL|self)

 228            LOAD_CONST               2 ('Top strategy still scores below 60 — add scenarios that exercise the lifecycle steps currently most-missed.')

 227            CALL                     1
                POP_TOP

 233    L3:     LOAD_FAST_BORROW         1 (ranked)
                GET_ITER
                LOAD_FAST_AND_CLEAR      6 (r)
                SWAP                     2
        L4:     BUILD_LIST               0
                SWAP                     2
        L5:     FOR_ITER                34 (to L8)
                STORE_FAST_LOAD_FAST   102 (r, r)
                LOAD_CONST               1 ('score')
                BINARY_OP               26 ([])
                LOAD_FAST_BORROW         5 (winner)
                LOAD_CONST               1 ('score')
                BINARY_OP               26 ([])
                LOAD_SMALL_INT           2
                BINARY_OP               11 (/)
                COMPARE_OP              18 (bool(<))
        L6:     POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                JUMP_BACKWARD           32 (to L5)
        L7:     LOAD_FAST_BORROW         6 (r)
                LIST_APPEND              2
                JUMP_BACKWARD           36 (to L5)
        L8:     END_FOR
                POP_ITER
        L9:     STORE_FAST               7 (weak)
                STORE_FAST               6 (r)

 234            LOAD_FAST_BORROW         7 (weak)
                TO_BOOL
                POP_JUMP_IF_FALSE       69 (to L10)
                NOT_TAKEN
                LOAD_GLOBAL              3 (len + NULL)
                LOAD_FAST_BORROW         1 (ranked)
                CALL                     1
                LOAD_SMALL_INT           2
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE       53 (to L10)
                NOT_TAKEN

 235            LOAD_CONST               3 (', ')
                LOAD_ATTR                5 (join + NULL|self)
                LOAD_CONST               4 (<code object <genexpr> at 0x0000018C180E89C0, file "app\services\optimization\report.py", line 235>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         7 (weak)
                LOAD_CONST               5 (slice(None, 3, None))
                BINARY_OP               26 ([])
                GET_ITER
                CALL                     0
                CALL                     1
                STORE_FAST               8 (ids)

 236            LOAD_FAST_BORROW         4 (recs)
                LOAD_ATTR                1 (append + NULL|self)
                LOAD_CONST               6 ('Consider retiring: ')
                LOAD_FAST_BORROW         8 (ids)
                FORMAT_SIMPLE
                LOAD_CONST               7 (' (score < half of winner).')
                BUILD_STRING             3
                CALL                     1
                POP_TOP

 239   L10:     LOAD_FAST_BORROW         0 (metrics)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               8 ('missing_lifecycle_frequency')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L11)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
       L11:     STORE_FAST               9 (miss_freq)

 240            LOAD_FAST_BORROW         9 (miss_freq)
                TO_BOOL
                POP_JUMP_IF_FALSE       67 (to L12)
                NOT_TAKEN

 241            LOAD_GLOBAL              9 (max + NULL)
                LOAD_FAST_BORROW         9 (miss_freq)
                LOAD_ATTR               11 (items + NULL|self)
                CALL                     0
                LOAD_CONST               9 (<code object <lambda> at 0x0000018C17FA23D0, file "app\services\optimization\report.py", line 241>)
                MAKE_FUNCTION
                LOAD_CONST              10 (('key',))
                CALL_KW                  2
                STORE_FAST              10 (worst)

 242            LOAD_FAST_BORROW         4 (recs)
                LOAD_ATTR                1 (append + NULL|self)

 243            LOAD_CONST              11 ("Most-missed lifecycle step across the matrix: '")
                LOAD_FAST_BORROW        10 (worst)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                LOAD_CONST              12 ("' (")

 244            LOAD_FAST_BORROW        10 (worst)
                LOAD_SMALL_INT           1
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                LOAD_CONST              13 (' cells). Target a scenario or engine seam that closes it.')

 243            BUILD_STRING             5

 242            CALL                     1
                POP_TOP

 248   L12:     LOAD_FAST                3 (personality_insights)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
       L13:     STORE_FAST              11 (pi)

 249            LOAD_FAST_BORROW        11 (pi)
                TO_BOOL
                POP_JUMP_IF_FALSE      145 (to L14)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (ranked)
                TO_BOOL
                POP_JUMP_IF_FALSE      137 (to L14)
                NOT_TAKEN

 250            LOAD_FAST_BORROW         1 (ranked)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                LOAD_CONST              14 ('strategy_id')
                BINARY_OP               26 ([])
                STORE_FAST              12 (winner_id)

 251            LOAD_FAST_BORROW        11 (pi)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_FAST_BORROW        12 (winner_id)
                CALL                     1
                STORE_FAST              13 (winner_info)

 252            LOAD_FAST_BORROW        13 (winner_info)
                TO_BOOL
                POP_JUMP_IF_FALSE       96 (to L14)
                NOT_TAKEN

 253            LOAD_FAST_BORROW         4 (recs)
                LOAD_ATTR                1 (append + NULL|self)

 254            LOAD_CONST              15 ("Winner '")
                LOAD_FAST_BORROW        12 (winner_id)
                FORMAT_SIMPLE
                LOAD_CONST              16 ("' performs best against '")

 255            LOAD_FAST_BORROW        13 (winner_info)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST              17 ('best_personality')
                CALL                     1
                FORMAT_SIMPLE
                LOAD_CONST              18 ("' leads (pass ")

 256            LOAD_FAST_BORROW        13 (winner_info)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST              19 ('best_pass_rate')
                CALL                     1
                LOAD_CONST              20 ('.0%')
                FORMAT_WITH_SPEC
                LOAD_CONST              21 ("); weakest against '")

 257            LOAD_FAST_BORROW        13 (winner_info)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST              22 ('worst_personality')
                CALL                     1
                FORMAT_SIMPLE
                LOAD_CONST              23 ("' (pass ")

 258            LOAD_FAST_BORROW        13 (winner_info)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST              24 ('worst_pass_rate')
                CALL                     1
                LOAD_CONST              20 ('.0%')
                FORMAT_WITH_SPEC
                LOAD_CONST              25 (').')

 254            BUILD_STRING            11

 253            CALL                     1
                POP_TOP

 261   L14:     LOAD_FAST_BORROW         4 (recs)
                RETURN_VALUE

  --   L15:     SWAP                     2
                POP_TOP

 233            SWAP                     2
                STORE_FAST               6 (r)
                RERAISE                  0
ExceptionTable:
  L4 to L6 -> L15 [2]
  L7 to L9 -> L15 [2]

Disassembly of <code object <genexpr> at 0x0000018C180E89C0, file "app\services\optimization\report.py", line 235>:
 235           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                13 (to L3)
               STORE_FAST_LOAD_FAST    17 (r, r)
               LOAD_CONST               0 ('strategy_id')
               BINARY_OP               26 ([])
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           15 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object <lambda> at 0x0000018C17FA23D0, file "app\services\optimization\report.py", line 241>:
241           RESUME                   0
              LOAD_FAST_BORROW         0 (kv)
              LOAD_SMALL_INT           1
              BINARY_OP               26 ([])
              RETURN_VALUE
```
