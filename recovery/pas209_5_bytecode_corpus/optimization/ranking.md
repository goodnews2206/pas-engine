# optimization/ranking

- **pyc:** `app\services\optimization\__pycache__\ranking.cpython-314.pyc`
- **expected source path (absent):** `app\services\optimization/ranking.py`
- **co_filename (from bytecode):** `app\services\optimization\ranking.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** optimization

## Module docstring

```
PAS143A — Deterministic strategy ranking.

Pure function over `compute_matrix_metrics(matrix).by_strategy`.
The score is a transparent weighted sum so every change in a
component metric maps clearly to a change in rank — no black-box
heuristics, no LLMs.

  score = pass_rate * 40                 # 0..40
        + avg_replay_score * 0.30        # 0..30
        + booked_rate * 20               # 0..20
        + callback_rate * 10             # 0..10
        - error_count * 2                # penalty
  → tie-break: lower avg_turns wins (efficiency)
  → final tie-break: alphabetical strategy_id (deterministic)

Max ideal score = 100. Errors deduct without bound (so a strategy
that crashes on every cell can land negative — caught by the report).
```

## Imports

`Dict`, `List`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_score`, `_summary_text`, `_swot`, `rank_strategies`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS143A — Deterministic strategy ranking.\n\nPure function over `compute_matrix_metrics(matrix).by_strategy`.\nThe score is a transparent weighted sum so every change in a\ncomponent metric maps clearly to a change in rank — no black-box\nheuristics, no LLMs.\n\n  score = pass_rate * 40                 # 0..40\n        + avg_replay_score * 0.30        # 0..30\n        + booked_rate * 20               # 0..20\n        + callback_rate * 10             # 0..10\n        - error_count * 2                # penalty\n  → tie-break: lower avg_turns wins (efficiency)\n  → final tie-break: alphabetical strategy_id (deterministic)\n\nMax ideal score = 100. Errors deduct without bound (so a strategy\nthat crashes on every cell can land negative — caught by the report).\n'
- 'metrics'
- 'return'
- '\nReturns a list of dicts ranked best-to-worst:\n  {\n    "strategy_id":  str,\n    "rank":         int (1-based),\n    "score":        float,\n    "components":   {pass_rate, avg_replay_score, booked_rate,\n                     callback_rate, error_count, avg_turns,\n                     effective},\n    "strengths":    [str, ...],\n    "weaknesses":   [str, ...],\n    "summary":      str,\n  }\n\nEmpty / malformed input returns []. Never raises.\n'
- 'by_strategy'
- 'pass_rate'
- 'avg_replay_score'
- 'booked_rate'
- 'callback_rate'
- 'error_count'
- 'errors'
- 'avg_turns'
- 'effective'
- 'strategy_id'
- 'rank'
- 'score'
- 'components'
- 'strengths'
- 'weaknesses'
- 'summary'
- 'entry'
- 'high pass rate ('
- '.0%'
- 'low pass rate ('
- 'strong replay quality ('
- '/100)'
- 'thin replay coverage ('
- 'booked '
- ' of cells'
- 'converted '
- ' of cells to callbacks'
- ' cell error(s)'
- 'no engine-observable overrides yet'
- 'sid'
- 'rank_idx'
- 'infrastructure-only'
- ': score '
- '.1f'
- ' — pass '
- ', replay avg '
- ', booked '
- ', callback '
- ', avg turns '

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS143A — Deterministic strategy ranking.\n\nPure function over `compute_matrix_metrics(matrix).by_strategy`.\nThe score is a transparent weighted sum so every change in a\ncomponent metric maps clearly to a change in rank — no black-box\nheuristics, no LLMs.\n\n  score = pass_rate * 40                 # 0..40\n        + avg_replay_score * 0.30        # 0..30\n        + booked_rate * 20               # 0..20\n        + callback_rate * 10             # 0..10\n        - error_count * 2                # penalty\n  → tie-break: lower avg_turns wins (efficiency)\n  → final tie-break: alphabetical strategy_id (deterministic)\n\nMax ideal score = 100. Errors deduct without bound (so a strategy\nthat crashes on every cell can land negative — caught by the report).\n')
              STORE_NAME               0 (__doc__)

 21           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('Dict', 'List'))
              IMPORT_NAME              1 (typing)
              IMPORT_FROM              2 (Dict)
              STORE_NAME               2 (Dict)
              IMPORT_FROM              3 (List)
              STORE_NAME               3 (List)
              POP_TOP

 24           LOAD_CONST               2 (40.0)
              STORE_NAME               4 (_W_PASS)

 25           LOAD_CONST               3 (0.3)
              STORE_NAME               5 (_W_REPLAY)

 26           LOAD_CONST               4 (20.0)
              STORE_NAME               6 (_W_BOOKED)

 27           LOAD_CONST               5 (10.0)
              STORE_NAME               7 (_W_CALLBACK)

 28           LOAD_CONST               6 (2.0)
              STORE_NAME               8 (_PEN_ERROR)

 31           LOAD_CONST               7 (<code object __annotate__ at 0x0000018C180532D0, file "app\services\optimization\ranking.py", line 31>)
              MAKE_FUNCTION
              LOAD_CONST               8 (<code object rank_strategies at 0x0000018C18325330, file "app\services\optimization\ranking.py", line 31>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME               9 (rank_strategies)

 92           LOAD_CONST               9 (<code object __annotate__ at 0x0000018C18024C30, file "app\services\optimization\ranking.py", line 92>)
              MAKE_FUNCTION
              LOAD_CONST              10 (<code object _score at 0x0000018C17EDA5E0, file "app\services\optimization\ranking.py", line 92>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              10 (_score)

108           LOAD_CONST              11 (<code object __annotate__ at 0x0000018C18025530, file "app\services\optimization\ranking.py", line 108>)
              MAKE_FUNCTION
              LOAD_CONST              12 (<code object _swot at 0x0000018C17D8BF50, file "app\services\optimization\ranking.py", line 108>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              11 (_swot)

136           LOAD_CONST              13 (<code object __annotate__ at 0x0000018C17C49B80, file "app\services\optimization\ranking.py", line 136>)
              MAKE_FUNCTION
              LOAD_CONST              14 (<code object _summary_text at 0x0000018C1800AD80, file "app\services\optimization\ranking.py", line 136>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              12 (_summary_text)
              LOAD_CONST              15 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180532D0, file "app\services\optimization\ranking.py", line 31>:
 31           RESUME                   0
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
              LOAD_GLOBAL              2 (List)
              LOAD_GLOBAL              0 (dict)
              BINARY_OP               26 ([])
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object rank_strategies at 0x0000018C18325330, file "app\services\optimization\ranking.py", line 31>:
 31           RESUME                   0

 48           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (metrics)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

 49           BUILD_LIST               0
              RETURN_VALUE

 50   L1:     LOAD_FAST_BORROW         0 (metrics)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               1 ('by_strategy')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L2:     STORE_FAST               1 (by_strategy)

 51           LOAD_FAST_BORROW         1 (by_strategy)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN

 52           BUILD_LIST               0
              RETURN_VALUE

 54   L3:     BUILD_LIST               0
              STORE_FAST               2 (enriched)

 55           LOAD_FAST_BORROW         1 (by_strategy)
              LOAD_ATTR                7 (items + NULL|self)
              CALL                     0
              GET_ITER
      L4:     FOR_ITER                35 (to L5)
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST   52 (sid, entry)

 56           LOAD_GLOBAL              9 (_score + NULL)
              LOAD_FAST_BORROW         4 (entry)
              CALL                     1
              STORE_FAST               5 (score)

 57           LOAD_FAST_BORROW         2 (enriched)
              LOAD_ATTR               11 (append + NULL|self)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (sid, entry)
              LOAD_FAST_BORROW         5 (score)
              BUILD_TUPLE              3
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           37 (to L4)

 55   L5:     END_FOR
              POP_ITER

 60           LOAD_FAST_BORROW         2 (enriched)
              LOAD_ATTR               13 (sort + NULL|self)

 61           LOAD_CONST               2 (<code object <lambda> at 0x0000018C17FE13E0, file "app\services\optimization\ranking.py", line 61>)
              MAKE_FUNCTION

 60           LOAD_CONST               3 (('key',))
              CALL_KW                  1
              POP_TOP

 68           BUILD_LIST               0
              STORE_FAST               6 (out)

 69           LOAD_GLOBAL             15 (enumerate + NULL)
              LOAD_FAST_BORROW         2 (enriched)
              LOAD_SMALL_INT           1
              LOAD_CONST               4 (('start',))
              CALL_KW                  2
              GET_ITER
      L6:     FOR_ITER               210 (to L7)
              UNPACK_SEQUENCE          2
              STORE_FAST               7 (rank_idx)
              UNPACK_SEQUENCE          3
              STORE_FAST_STORE_FAST   52 (sid, entry)
              STORE_FAST               5 (score)

 71           LOAD_CONST               5 ('pass_rate')
              LOAD_FAST_BORROW         4 (entry)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               5 ('pass_rate')
              LOAD_CONST               6 (0.0)
              CALL                     2

 72           LOAD_CONST               7 ('avg_replay_score')
              LOAD_FAST_BORROW         4 (entry)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               7 ('avg_replay_score')
              LOAD_CONST               6 (0.0)
              CALL                     2

 73           LOAD_CONST               8 ('booked_rate')
              LOAD_FAST_BORROW         4 (entry)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               8 ('booked_rate')
              LOAD_CONST               6 (0.0)
              CALL                     2

 74           LOAD_CONST               9 ('callback_rate')
              LOAD_FAST_BORROW         4 (entry)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               9 ('callback_rate')
              LOAD_CONST               6 (0.0)
              CALL                     2

 75           LOAD_CONST              10 ('error_count')
              LOAD_FAST_BORROW         4 (entry)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST              11 ('errors')
              LOAD_SMALL_INT           0
              CALL                     2

 76           LOAD_CONST              12 ('avg_turns')
              LOAD_FAST_BORROW         4 (entry)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST              12 ('avg_turns')
              LOAD_CONST               6 (0.0)
              CALL                     2

 77           LOAD_CONST              13 ('effective')
              LOAD_GLOBAL             17 (bool + NULL)
              LOAD_FAST_BORROW         4 (entry)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST              13 ('effective')
              LOAD_CONST              14 (False)
              CALL                     2
              CALL                     1

 70           BUILD_MAP                7
              STORE_FAST               8 (components)

 79           LOAD_GLOBAL             19 (_swot + NULL)
              LOAD_FAST_BORROW         8 (components)
              CALL                     1
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST  154 (strengths, weaknesses)

 80           LOAD_FAST_BORROW         6 (out)
              LOAD_ATTR               11 (append + NULL|self)

 81           LOAD_CONST              15 ('strategy_id')
              LOAD_FAST_BORROW         3 (sid)

 82           LOAD_CONST              16 ('rank')
              LOAD_FAST_BORROW         7 (rank_idx)

 83           LOAD_CONST              17 ('score')
              LOAD_GLOBAL             21 (round + NULL)
              LOAD_FAST_BORROW         5 (score)
              LOAD_SMALL_INT           2
              CALL                     2

 84           LOAD_CONST              18 ('components')
              LOAD_FAST_BORROW         8 (components)

 85           LOAD_CONST              19 ('strengths')
              LOAD_FAST_BORROW         9 (strengths)

 86           LOAD_CONST              20 ('weaknesses')
              LOAD_FAST_BORROW        10 (weaknesses)

 87           LOAD_CONST              21 ('summary')
              LOAD_GLOBAL             23 (_summary_text + NULL)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 55 (sid, rank_idx)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 133 (components, score)
              CALL                     4

 80           BUILD_MAP                7
              CALL                     1
              POP_TOP
              JUMP_BACKWARD          212 (to L6)

 69   L7:     END_FOR
              POP_ITER

 89           LOAD_FAST_BORROW         6 (out)
              RETURN_VALUE

Disassembly of <code object <lambda> at 0x0000018C17FE13E0, file "app\services\optimization\ranking.py", line 61>:
 61           RESUME                   0

 62           LOAD_FAST_BORROW         0 (t)
              LOAD_SMALL_INT           2
              BINARY_OP               26 ([])
              UNARY_NEGATIVE

 63           LOAD_FAST_BORROW         0 (t)
              LOAD_SMALL_INT           1
              BINARY_OP               26 ([])
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               1 ('avg_turns')
              LOAD_SMALL_INT           0
              CALL                     2
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_SMALL_INT           0

 64   L1:     LOAD_FAST_BORROW         0 (t)
              LOAD_SMALL_INT           0
              BINARY_OP               26 ([])
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               2 ('')

 61   L2:     BUILD_TUPLE              3
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "app\services\optimization\ranking.py", line 92>:
 92           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('entry')
              LOAD_GLOBAL              0 (dict)
              LOAD_CONST               2 ('return')
              LOAD_GLOBAL              2 (float)
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _score at 0x0000018C17EDA5E0, file "app\services\optimization\ranking.py", line 92>:
 92           RESUME                   0

 93           LOAD_GLOBAL              1 (float + NULL)
              LOAD_FAST_BORROW         0 (entry)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               0 ('pass_rate')
              LOAD_SMALL_INT           0
              CALL                     2
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_SMALL_INT           0
      L1:     CALL                     1
              STORE_FAST               1 (pass_rate)

 94           LOAD_GLOBAL              1 (float + NULL)
              LOAD_FAST_BORROW         0 (entry)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               1 ('avg_replay_score')
              LOAD_SMALL_INT           0
              CALL                     2
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              LOAD_SMALL_INT           0
      L2:     CALL                     1
              STORE_FAST               2 (avg_replay)

 95           LOAD_GLOBAL              1 (float + NULL)
              LOAD_FAST_BORROW         0 (entry)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               2 ('booked_rate')
              LOAD_SMALL_INT           0
              CALL                     2
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              POP_TOP
              LOAD_SMALL_INT           0
      L3:     CALL                     1
              STORE_FAST               3 (booked)

 96           LOAD_GLOBAL              1 (float + NULL)
              LOAD_FAST_BORROW         0 (entry)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               3 ('callback_rate')
              LOAD_SMALL_INT           0
              CALL                     2
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN
              POP_TOP
              LOAD_SMALL_INT           0
      L4:     CALL                     1
              STORE_FAST               4 (callback)

 97           LOAD_GLOBAL              5 (int + NULL)
              LOAD_FAST_BORROW         0 (entry)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               4 ('errors')
              LOAD_SMALL_INT           0
              CALL                     2
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              POP_TOP
              LOAD_SMALL_INT           0
      L5:     CALL                     1
              STORE_FAST               5 (errors)

 99           LOAD_FAST_BORROW         1 (pass_rate)
              LOAD_GLOBAL              6 (_W_PASS)
              BINARY_OP                5 (*)

100           LOAD_FAST_BORROW         2 (avg_replay)
              LOAD_GLOBAL              8 (_W_REPLAY)
              BINARY_OP                5 (*)

 99           BINARY_OP                0 (+)

101           LOAD_FAST_BORROW         3 (booked)
              LOAD_GLOBAL             10 (_W_BOOKED)
              BINARY_OP                5 (*)

 99           BINARY_OP                0 (+)

102           LOAD_FAST_BORROW         4 (callback)
              LOAD_GLOBAL             12 (_W_CALLBACK)
              BINARY_OP                5 (*)

 99           BINARY_OP                0 (+)

103           LOAD_FAST_BORROW         5 (errors)
              LOAD_GLOBAL             14 (_PEN_ERROR)
              BINARY_OP                5 (*)

 99           BINARY_OP               10 (-)

 98           STORE_FAST               6 (score)

105           LOAD_FAST_BORROW         6 (score)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025530, file "app\services\optimization\ranking.py", line 108>:
108           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('c')
              LOAD_GLOBAL              0 (dict)
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _swot at 0x0000018C17D8BF50, file "app\services\optimization\ranking.py", line 108>:
108           RESUME                   0

109           BUILD_LIST               0
              STORE_FAST               1 (strengths)

110           BUILD_LIST               0
              STORE_FAST               2 (weaknesses)

112           LOAD_FAST_BORROW         0 (c)
              LOAD_CONST               0 ('pass_rate')
              BINARY_OP               26 ([])
              LOAD_CONST               1 (0.9)
              COMPARE_OP             188 (bool(>=))
              POP_JUMP_IF_FALSE       31 (to L1)
              NOT_TAKEN

113           LOAD_FAST_BORROW         1 (strengths)
              LOAD_ATTR                1 (append + NULL|self)
              LOAD_CONST               2 ('high pass rate (')
              LOAD_FAST_BORROW         0 (c)
              LOAD_CONST               0 ('pass_rate')
              BINARY_OP               26 ([])
              LOAD_CONST               3 ('.0%')
              FORMAT_WITH_SPEC
              LOAD_CONST               4 (')')
              BUILD_STRING             3
              CALL                     1
              POP_TOP
              JUMP_FORWARD            43 (to L2)

114   L1:     LOAD_FAST_BORROW         0 (c)
              LOAD_CONST               0 ('pass_rate')
              BINARY_OP               26 ([])
              LOAD_CONST               5 (0.5)
              COMPARE_OP              18 (bool(<))
              POP_JUMP_IF_FALSE       30 (to L2)
              NOT_TAKEN

115           LOAD_FAST_BORROW         2 (weaknesses)
              LOAD_ATTR                1 (append + NULL|self)
              LOAD_CONST               6 ('low pass rate (')
              LOAD_FAST_BORROW         0 (c)
              LOAD_CONST               0 ('pass_rate')
              BINARY_OP               26 ([])
              LOAD_CONST               3 ('.0%')
              FORMAT_WITH_SPEC
              LOAD_CONST               4 (')')
              BUILD_STRING             3
              CALL                     1
              POP_TOP

117   L2:     LOAD_FAST_BORROW         0 (c)
              LOAD_CONST               7 ('avg_replay_score')
              BINARY_OP               26 ([])
              LOAD_SMALL_INT          80
              COMPARE_OP             188 (bool(>=))
              POP_JUMP_IF_FALSE       30 (to L3)
              NOT_TAKEN

118           LOAD_FAST_BORROW         1 (strengths)
              LOAD_ATTR                1 (append + NULL|self)
              LOAD_CONST               8 ('strong replay quality (')
              LOAD_FAST_BORROW         0 (c)
              LOAD_CONST               7 ('avg_replay_score')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               9 ('/100)')
              BUILD_STRING             3
              CALL                     1
              POP_TOP
              JUMP_FORWARD            42 (to L4)

119   L3:     LOAD_FAST_BORROW         0 (c)
              LOAD_CONST               7 ('avg_replay_score')
              BINARY_OP               26 ([])
              LOAD_SMALL_INT          50
              COMPARE_OP              18 (bool(<))
              POP_JUMP_IF_FALSE       29 (to L4)
              NOT_TAKEN

120           LOAD_FAST_BORROW         2 (weaknesses)
              LOAD_ATTR                1 (append + NULL|self)
              LOAD_CONST              10 ('thin replay coverage (')
              LOAD_FAST_BORROW         0 (c)
              LOAD_CONST               7 ('avg_replay_score')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               9 ('/100)')
              BUILD_STRING             3
              CALL                     1
              POP_TOP

122   L4:     LOAD_FAST_BORROW         0 (c)
              LOAD_CONST              11 ('booked_rate')
              BINARY_OP               26 ([])
              LOAD_CONST              12 (0.4)
              COMPARE_OP             188 (bool(>=))
              POP_JUMP_IF_FALSE       30 (to L5)
              NOT_TAKEN

123           LOAD_FAST_BORROW         1 (strengths)
              LOAD_ATTR                1 (append + NULL|self)
              LOAD_CONST              13 ('booked ')
              LOAD_FAST_BORROW         0 (c)
              LOAD_CONST              11 ('booked_rate')
              BINARY_OP               26 ([])
              LOAD_CONST               3 ('.0%')
              FORMAT_WITH_SPEC
              LOAD_CONST              14 (' of cells')
              BUILD_STRING             3
              CALL                     1
              POP_TOP

124   L5:     LOAD_FAST_BORROW         0 (c)
              LOAD_CONST              15 ('callback_rate')
              BINARY_OP               26 ([])
              LOAD_CONST              16 (0.3)
              COMPARE_OP             188 (bool(>=))
              POP_JUMP_IF_FALSE       30 (to L6)
              NOT_TAKEN

125           LOAD_FAST_BORROW         1 (strengths)
              LOAD_ATTR                1 (append + NULL|self)
              LOAD_CONST              17 ('converted ')
              LOAD_FAST_BORROW         0 (c)
              LOAD_CONST              15 ('callback_rate')
              BINARY_OP               26 ([])
              LOAD_CONST               3 ('.0%')
              FORMAT_WITH_SPEC
              LOAD_CONST              18 (' of cells to callbacks')
              BUILD_STRING             3
              CALL                     1
              POP_TOP

127   L6:     LOAD_FAST_BORROW         0 (c)
              LOAD_CONST              19 ('error_count')
              BINARY_OP               26 ([])
              LOAD_SMALL_INT           0
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       28 (to L7)
              NOT_TAKEN

128           LOAD_FAST_BORROW         2 (weaknesses)
              LOAD_ATTR                1 (append + NULL|self)
              LOAD_FAST_BORROW         0 (c)
              LOAD_CONST              19 ('error_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              20 (' cell error(s)')
              BUILD_STRING             2
              CALL                     1
              POP_TOP

130   L7:     LOAD_FAST_BORROW         0 (c)
              LOAD_CONST              21 ('effective')
              BINARY_OP               26 ([])
              TO_BOOL
              POP_JUMP_IF_TRUE        18 (to L8)
              NOT_TAKEN

131           LOAD_FAST_BORROW         2 (weaknesses)
              LOAD_ATTR                1 (append + NULL|self)
              LOAD_CONST              22 ('no engine-observable overrides yet')
              CALL                     1
              POP_TOP

133   L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (strengths, weaknesses)
              BUILD_TUPLE              2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17C49B80, file "app\services\optimization\ranking.py", line 136>:
136           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('sid')
              LOAD_GLOBAL              0 (str)
              LOAD_CONST               2 ('rank_idx')
              LOAD_GLOBAL              2 (int)
              LOAD_CONST               3 ('c')
              LOAD_GLOBAL              4 (dict)
              LOAD_CONST               4 ('score')
              LOAD_GLOBAL              6 (float)
              LOAD_CONST               5 ('return')
              LOAD_GLOBAL              0 (str)
              BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _summary_text at 0x0000018C1800AD80, file "app\services\optimization\ranking.py", line 136>:
136           RESUME                   0

137           LOAD_FAST_BORROW         2 (c)
              LOAD_CONST               0 ('effective')
              BINARY_OP               26 ([])
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_CONST               0 ('effective')
              JUMP_FORWARD             1 (to L2)
      L1:     LOAD_CONST               1 ('infrastructure-only')
      L2:     STORE_FAST               4 (eff)

139           LOAD_CONST               2 ('#')
              LOAD_FAST_BORROW         1 (rank_idx)
              FORMAT_SIMPLE
              LOAD_CONST               3 (' ')
              LOAD_FAST_BORROW         0 (sid)
              FORMAT_SIMPLE
              LOAD_CONST               4 (': score ')
              LOAD_FAST_BORROW         3 (score)
              LOAD_CONST               5 ('.1f')
              FORMAT_WITH_SPEC
              LOAD_CONST               6 (' — pass ')

140           LOAD_FAST_BORROW         2 (c)
              LOAD_CONST               7 ('pass_rate')
              BINARY_OP               26 ([])
              LOAD_CONST               8 ('.0%')
              FORMAT_WITH_SPEC
              LOAD_CONST               9 (', replay avg ')
              LOAD_FAST_BORROW         2 (c)
              LOAD_CONST              10 ('avg_replay_score')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              11 (', booked ')

141           LOAD_FAST_BORROW         2 (c)
              LOAD_CONST              12 ('booked_rate')
              BINARY_OP               26 ([])
              LOAD_CONST               8 ('.0%')
              FORMAT_WITH_SPEC
              LOAD_CONST              13 (', callback ')
              LOAD_FAST_BORROW         2 (c)
              LOAD_CONST              14 ('callback_rate')
              BINARY_OP               26 ([])
              LOAD_CONST               8 ('.0%')
              FORMAT_WITH_SPEC
              LOAD_CONST              15 (', avg turns ')

142           LOAD_FAST_BORROW         2 (c)
              LOAD_CONST              16 ('avg_turns')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              17 (', ')
              LOAD_FAST_BORROW         4 (eff)
              FORMAT_SIMPLE
              LOAD_CONST              18 ('.')

139           BUILD_STRING            19

138           RETURN_VALUE
```
