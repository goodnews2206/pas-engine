# optimization/matrix_runner

- **pyc:** `app\services\optimization\__pycache__\matrix_runner.cpython-314.pyc`
- **expected source path (absent):** `app\services\optimization/matrix_runner.py`
- **co_filename (from bytecode):** `app\services\optimization\matrix_runner.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** optimization

## Module docstring

```
PAS143A — Scenario × Strategy matrix runner.

For every (scenario, strategy) pair we invoke PAS142's run_scenario
with the strategy's engine_overrides spliced into the brokerage dict.
A failure in one cell never aborts the matrix — the per-cell `error`
field captures the message, and the rest of the grid still runs.
```

## Imports

`Iterable`, `List`, `Optional`, `StrategyVariant`, `app.services.simulation.runner`, `datetime`, `is_strategy_observable`, `run_scenario`, `strategies`, `time`, `timezone`, `typing`, `uuid`

## Classes

_none_

## Functions / methods

`__annotate__`, `_empty_sim_result`, `_run_cell`, `run_strategy_matrix`

## Env-key candidates

_none_

## String constants (redacted where noted)

- "\nPAS143A — Scenario × Strategy matrix runner.\n\nFor every (scenario, strategy) pair we invoke PAS142's run_scenario\nwith the strategy's engine_overrides spliced into the brokerage dict.\nA failure in one cell never aborts the matrix — the per-cell `error`\nfield captures the message, and the rest of the grid still runs.\n"
- 'brokerage_id'
- 'demo'
- 'scenarios'
- 'strategies'
- 'return'
- '\nExecute every scenario × strategy combination in-process.\n\nReturns:\n  {\n    "matrix_id":         "MTX-...",\n    "total_runs":        int,\n    "scenarios_count":   int,\n    "strategies_count":  int,\n    "brokerage_id":      str,\n    "results":           [run_scenario_result + strategy metadata, ...],\n    "started_at":        ISO,\n    "generated_at":      ISO,\n    "duration_ms":       int,\n  }\n\nEach result row carries:\n  - all PAS142 run_scenario keys\n  - strategy_id, strategy_name, strategy_category\n  - strategy_overrides (the dict actually applied)\n  - strategy_effective (bool — see is_strategy_observable)\n  - cell_error (str | None) — set when run_scenario itself raised\n    rather than returning an error result; defensive belt-and-braces.\n'
- 'matrix_id'
- 'MTX-'
- 'total_runs'
- 'scenarios_count'
- 'strategies_count'
- 'results'
- 'started_at'
- 'generated_at'
- 'duration_ms'
- 'strategy'
- 'One scenario × strategy execution. Always returns a dict.'
- 'strategy_id'
- 'strategy_name'
- 'strategy_category'
- 'strategy_overrides'
- 'strategy_effective'
- 'cell_error'
- 'error'
- "Stand-in for run_scenario's shape when the call itself raised."
- 'scenario_id'
- 'scenario_title'
- 'title'
- 'scenario_category'
- 'category'
- 'scenario_tags'
- 'tags'
- 'call_sid'
- 'expected_outcome'
- 'actual_outcome'
- 'passed'
- 'events_count'
- 'transcript'
- 'reconstruction'
- 'evaluation'
- 'replay_score'
- 'missing_steps'
- 'warnings'
- 'summary'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ("\nPAS143A — Scenario × Strategy matrix runner.\n\nFor every (scenario, strategy) pair we invoke PAS142's run_scenario\nwith the strategy's engine_overrides spliced into the brokerage dict.\nA failure in one cell never aborts the matrix — the per-cell `error`\nfield captures the message, and the rest of the grid still runs.\n")
              STORE_NAME               0 (__doc__)

 10           LOAD_SMALL_INT           0
              LOAD_CONST               1 (None)
              IMPORT_NAME              1 (time)
              STORE_NAME               1 (time)

 11           LOAD_SMALL_INT           0
              LOAD_CONST               1 (None)
              IMPORT_NAME              2 (uuid)
              STORE_NAME               2 (uuid)

 12           LOAD_SMALL_INT           0
              LOAD_CONST               2 (('datetime', 'timezone'))
              IMPORT_NAME              3 (datetime)
              IMPORT_FROM              3 (datetime)
              STORE_NAME               3 (datetime)
              IMPORT_FROM              4 (timezone)
              STORE_NAME               4 (timezone)
              POP_TOP

 13           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('Iterable', 'List', 'Optional'))
              IMPORT_NAME              5 (typing)
              IMPORT_FROM              6 (Iterable)
              STORE_NAME               6 (Iterable)
              IMPORT_FROM              7 (List)
              STORE_NAME               7 (List)
              IMPORT_FROM              8 (Optional)
              STORE_NAME               8 (Optional)
              POP_TOP

 15           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('run_scenario',))
              IMPORT_NAME              9 (app.services.simulation.runner)
              IMPORT_FROM             10 (run_scenario)
              STORE_NAME              10 (run_scenario)
              POP_TOP

 17           LOAD_SMALL_INT           1
              LOAD_CONST               5 (('StrategyVariant', 'is_strategy_observable'))
              IMPORT_NAME             11 (strategies)
              IMPORT_FROM             12 (StrategyVariant)
              STORE_NAME              12 (StrategyVariant)
              IMPORT_FROM             13 (is_strategy_observable)
              STORE_NAME              13 (is_strategy_observable)
              POP_TOP

 20           LOAD_CONST               6 ('brokerage_id')

 24           LOAD_CONST               7 ('demo')

 20           BUILD_MAP                1
              LOAD_CONST               8 (<code object __annotate__ at 0x0000018C180531B0, file "app\services\optimization\matrix_runner.py", line 20>)
              MAKE_FUNCTION
              LOAD_CONST               9 (<code object run_strategy_matrix at 0x0000018C17D6DFC0, file "app\services\optimization\matrix_runner.py", line 20>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              14 (run_strategy_matrix)

 77           LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17C49B80, file "app\services\optimization\matrix_runner.py", line 77>)
              MAKE_FUNCTION
              LOAD_CONST              11 (<code object _run_cell at 0x0000018C17ED1260, file "app\services\optimization\matrix_runner.py", line 77>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              15 (_run_cell)

111           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C18024C30, file "app\services\optimization\matrix_runner.py", line 111>)
              MAKE_FUNCTION
              LOAD_CONST              13 (<code object _empty_sim_result at 0x0000018C18048730, file "app\services\optimization\matrix_runner.py", line 111>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              16 (_empty_sim_result)
              LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180531B0, file "app\services\optimization\matrix_runner.py", line 20>:
 20           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('scenarios')

 21           LOAD_GLOBAL              0 (Iterable)

 20           LOAD_CONST               2 ('strategies')

 22           LOAD_GLOBAL              0 (Iterable)

 20           LOAD_CONST               3 ('brokerage_id')

 24           LOAD_GLOBAL              2 (str)

 20           LOAD_CONST               4 ('return')

 25           LOAD_GLOBAL              4 (dict)

 20           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object run_strategy_matrix at 0x0000018C17D6DFC0, file "app\services\optimization\matrix_runner.py", line 20>:
 20           RESUME                   0

 50           LOAD_GLOBAL              0 (time)
              LOAD_ATTR                2 (perf_counter)
              PUSH_NULL
              CALL                     0
              STORE_FAST               3 (started_perf)

 51           LOAD_GLOBAL              4 (datetime)
              LOAD_ATTR                6 (now)
              PUSH_NULL
              LOAD_GLOBAL              8 (timezone)
              LOAD_ATTR               10 (utc)
              CALL                     1
              LOAD_ATTR               13 (isoformat + NULL|self)
              CALL                     0
              STORE_FAST               4 (started_iso)

 53           LOAD_GLOBAL             15 (list + NULL)
              LOAD_FAST                0 (scenarios)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1
              STORE_FAST               0 (scenarios)

 54           LOAD_GLOBAL             15 (list + NULL)
              LOAD_FAST                1 (strategies)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L2:     CALL                     1
              STORE_FAST               1 (strategies)

 56           BUILD_LIST               0
              STORE_FAST               5 (results)

 58           LOAD_FAST_BORROW         0 (scenarios)
              GET_ITER
      L3:     FOR_ITER                39 (to L6)
              STORE_FAST               6 (scenario)

 59           LOAD_FAST_BORROW         1 (strategies)
              GET_ITER
      L4:     FOR_ITER                30 (to L5)
              STORE_FAST               7 (strategy)

 60           LOAD_FAST_BORROW         5 (results)
              LOAD_ATTR               17 (append + NULL|self)
              LOAD_GLOBAL             19 (_run_cell + NULL)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (scenario, strategy)
              LOAD_FAST_BORROW         2 (brokerage_id)
              CALL                     3
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           32 (to L4)

 59   L5:     END_FOR
              POP_ITER
              JUMP_BACKWARD           41 (to L3)

 58   L6:     END_FOR
              POP_ITER

 62           LOAD_GLOBAL             21 (int + NULL)
              LOAD_GLOBAL              0 (time)
              LOAD_ATTR                2 (perf_counter)
              PUSH_NULL
              CALL                     0
              LOAD_FAST_BORROW         3 (started_perf)
              BINARY_OP               10 (-)
              LOAD_CONST               1 (1000)
              BINARY_OP                5 (*)
              CALL                     1
              STORE_FAST               8 (duration_ms)

 65           LOAD_CONST               2 ('matrix_id')
              LOAD_CONST               3 ('MTX-')
              LOAD_GLOBAL             22 (uuid)
              LOAD_ATTR               24 (uuid4)
              PUSH_NULL
              CALL                     0
              LOAD_ATTR               26 (hex)
              LOAD_CONST               4 (slice(None, 10, None))
              BINARY_OP               26 ([])
              LOAD_ATTR               29 (upper + NULL|self)
              CALL                     0
              FORMAT_SIMPLE
              BUILD_STRING             2

 66           LOAD_CONST               5 ('total_runs')
              LOAD_GLOBAL             31 (len + NULL)
              LOAD_FAST_BORROW         5 (results)
              CALL                     1

 67           LOAD_CONST               6 ('scenarios_count')
              LOAD_GLOBAL             31 (len + NULL)
              LOAD_FAST_BORROW         0 (scenarios)
              CALL                     1

 68           LOAD_CONST               7 ('strategies_count')
              LOAD_GLOBAL             31 (len + NULL)
              LOAD_FAST_BORROW         1 (strategies)
              CALL                     1

 69           LOAD_CONST               8 ('brokerage_id')
              LOAD_FAST_BORROW         2 (brokerage_id)

 70           LOAD_CONST               9 ('results')
              LOAD_FAST_BORROW         5 (results)

 71           LOAD_CONST              10 ('started_at')
              LOAD_FAST_BORROW         4 (started_iso)

 72           LOAD_CONST              11 ('generated_at')
              LOAD_GLOBAL              4 (datetime)
              LOAD_ATTR                6 (now)
              PUSH_NULL
              LOAD_GLOBAL              8 (timezone)
              LOAD_ATTR               10 (utc)
              CALL                     1
              LOAD_ATTR               13 (isoformat + NULL|self)
              CALL                     0

 73           LOAD_CONST              12 ('duration_ms')
              LOAD_FAST_BORROW         8 (duration_ms)

 64           BUILD_MAP                9
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17C49B80, file "app\services\optimization\matrix_runner.py", line 77>:
 77           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('strategy')
              LOAD_GLOBAL              0 (Optional)
              LOAD_GLOBAL              2 (StrategyVariant)
              BINARY_OP               26 ([])
              LOAD_CONST               2 ('brokerage_id')
              LOAD_GLOBAL              4 (str)
              LOAD_CONST               3 ('return')
              LOAD_GLOBAL              6 (dict)
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _run_cell at 0x0000018C17ED1260, file "app\services\optimization\matrix_runner.py", line 77>:
  77            RESUME                   0

  81            LOAD_FAST_BORROW         1 (strategy)
                POP_JUMP_IF_NONE        54 (to L1)
                NOT_TAKEN
                LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (strategy)
                LOAD_ATTR                2 (engine_overrides)
                LOAD_GLOBAL              4 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       22 (to L1)
                NOT_TAKEN

  80            LOAD_GLOBAL              5 (dict + NULL)
                LOAD_FAST_BORROW         1 (strategy)
                LOAD_ATTR                2 (engine_overrides)
                CALL                     1
                JUMP_FORWARD             1 (to L2)

  82    L1:     BUILD_MAP                0

  79    L2:     STORE_FAST               3 (overrides)

  84            LOAD_CONST               1 (None)
                STORE_FAST               4 (cell_error)

  85            NOP

  90    L3:     LOAD_GLOBAL              7 (run_scenario + NULL)

  91            LOAD_FAST                0 (scenario)

  92            LOAD_FAST                2 (brokerage_id)

  93            LOAD_FAST                3 (overrides)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
        L4:     NOT_TAKEN
        L5:     POP_TOP
                LOAD_CONST               1 (None)

  94    L6:     LOAD_FAST_BORROW         1 (strategy)
                TO_BOOL
                POP_JUMP_IF_FALSE       13 (to L9)
        L7:     NOT_TAKEN
        L8:     LOAD_FAST_BORROW         1 (strategy)
                LOAD_ATTR                8 (id)
                JUMP_FORWARD             1 (to L10)
        L9:     LOAD_CONST               1 (None)

  90   L10:     LOAD_CONST               2 (('brokerage_id', 'brokerage_overrides', 'strategy_id'))
                CALL_KW                  4
                STORE_FAST               5 (sim_result)

 100   L11:     BUILD_MAP                0

 101            LOAD_FAST_BORROW         5 (sim_result)

 100            DICT_UPDATE              1

 102            LOAD_CONST               4 ('strategy_id')
                LOAD_FAST_BORROW         1 (strategy)
                TO_BOOL
                POP_JUMP_IF_FALSE       13 (to L12)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (strategy)
                LOAD_ATTR                8 (id)
                JUMP_FORWARD             1 (to L13)
       L12:     LOAD_CONST               1 (None)

 103   L13:     LOAD_CONST               5 ('strategy_name')
                LOAD_FAST_BORROW         1 (strategy)
                TO_BOOL
                POP_JUMP_IF_FALSE       13 (to L14)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (strategy)
                LOAD_ATTR               18 (name)
                JUMP_FORWARD             1 (to L15)
       L14:     LOAD_CONST               1 (None)

 104   L15:     LOAD_CONST               6 ('strategy_category')
                LOAD_FAST_BORROW         1 (strategy)
                TO_BOOL
                POP_JUMP_IF_FALSE       13 (to L16)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (strategy)
                LOAD_ATTR               20 (category)
                JUMP_FORWARD             1 (to L17)
       L16:     LOAD_CONST               1 (None)

 105   L17:     LOAD_CONST               7 ('strategy_overrides')
                LOAD_FAST                3 (overrides)

 106            LOAD_CONST               8 ('strategy_effective')
                LOAD_GLOBAL             23 (bool + NULL)
                LOAD_FAST                1 (strategy)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       12 (to L18)
                NOT_TAKEN
                POP_TOP
                LOAD_GLOBAL             25 (is_strategy_observable + NULL)
                LOAD_FAST_BORROW         1 (strategy)
                CALL                     1
       L18:     CALL                     1

 107            LOAD_CONST               9 ('cell_error')
                LOAD_FAST                4 (cell_error)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L19)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         5 (sim_result)
                LOAD_ATTR               27 (get + NULL|self)
                LOAD_CONST              10 ('error')
                CALL                     1

 100   L19:     BUILD_MAP                6
                DICT_UPDATE              1
                RETURN_VALUE

  --   L20:     PUSH_EXC_INFO

  96            LOAD_GLOBAL             10 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       49 (to L24)
                NOT_TAKEN
                STORE_FAST               6 (e)

  97   L21:     LOAD_GLOBAL             13 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               14 (__name__)
                FORMAT_SIMPLE
                LOAD_CONST               3 (': ')
                LOAD_FAST                6 (e)
                FORMAT_SIMPLE
                BUILD_STRING             3
                STORE_FAST               4 (cell_error)

  98            LOAD_GLOBAL             17 (_empty_sim_result + NULL)
                LOAD_FAST_LOAD_FAST      2 (scenario, brokerage_id)
                LOAD_FAST                4 (cell_error)
                CALL                     3
                STORE_FAST               5 (sim_result)
       L22:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                JUMP_BACKWARD_NO_INTERRUPT 185 (to L11)

  --   L23:     LOAD_CONST               1 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

  96   L24:     RERAISE                  0

  --   L25:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L20 [0]
  L5 to L7 -> L20 [0]
  L8 to L11 -> L20 [0]
  L20 to L21 -> L25 [1] lasti
  L21 to L22 -> L23 [1] lasti
  L23 to L25 -> L25 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "app\services\optimization\matrix_runner.py", line 111>:
111           RESUME                   0
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

Disassembly of <code object _empty_sim_result at 0x0000018C18048730, file "app\services\optimization\matrix_runner.py", line 111>:
111           RESUME                   0

113           LOAD_GLOBAL              1 (getattr + NULL)
              LOAD_FAST_BORROW         0 (scenario)
              LOAD_CONST               1 ('id')
              LOAD_CONST               2 (None)
              CALL                     3
              STORE_FAST               3 (sid)

115           LOAD_CONST               3 ('scenario_id')
              LOAD_FAST                3 (sid)

116           LOAD_CONST               4 ('scenario_title')
              LOAD_GLOBAL              1 (getattr + NULL)
              LOAD_FAST_BORROW         0 (scenario)
              LOAD_CONST               5 ('title')
              LOAD_CONST               2 (None)
              CALL                     3

117           LOAD_CONST               6 ('scenario_category')
              LOAD_GLOBAL              1 (getattr + NULL)
              LOAD_FAST_BORROW         0 (scenario)
              LOAD_CONST               7 ('category')
              LOAD_CONST               2 (None)
              CALL                     3

118           LOAD_CONST               8 ('scenario_tags')
              LOAD_GLOBAL              3 (list + NULL)
              LOAD_GLOBAL              1 (getattr + NULL)
              LOAD_FAST_BORROW         0 (scenario)
              LOAD_CONST               9 ('tags')
              BUILD_LIST               0
              CALL                     3
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

119           LOAD_CONST              10 ('call_sid')
              LOAD_CONST               2 (None)

120           LOAD_CONST              11 ('brokerage_id')
              LOAD_FAST_BORROW         1 (brokerage_id)

121           LOAD_CONST              12 ('expected_outcome')
              LOAD_GLOBAL              1 (getattr + NULL)
              LOAD_FAST_BORROW         0 (scenario)
              LOAD_CONST              12 ('expected_outcome')
              LOAD_CONST               2 (None)
              CALL                     3

122           LOAD_CONST              13 ('actual_outcome')
              LOAD_CONST              14 ('error')

123           LOAD_CONST              15 ('passed')
              LOAD_CONST              16 (False)

124           LOAD_CONST              17 ('events_count')
              LOAD_SMALL_INT           0

125           LOAD_CONST              18 ('transcript')
              BUILD_LIST               0

126           LOAD_CONST              19 ('reconstruction')
              BUILD_MAP                0

127           LOAD_CONST              20 ('evaluation')
              LOAD_CONST              21 ('replay_score')
              LOAD_SMALL_INT           0
              LOAD_CONST              22 ('missing_steps')
              BUILD_LIST               0
              LOAD_CONST              23 ('warnings')
              LOAD_FAST_BORROW         2 (error_msg)
              BUILD_LIST               1
              LOAD_CONST              24 ('summary')
              LOAD_FAST_BORROW         2 (error_msg)
              BUILD_MAP                4

128           LOAD_CONST              25 ('duration_ms')
              LOAD_SMALL_INT           0

129           LOAD_CONST              14 ('error')
              LOAD_FAST_BORROW         2 (error_msg)

114           BUILD_MAP               15
              RETURN_VALUE
```
