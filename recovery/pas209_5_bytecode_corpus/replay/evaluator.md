# replay/evaluator

- **pyc:** `app\services\replay\__pycache__\evaluator.cpython-314.pyc`
- **expected source path (absent):** `app\services\replay/evaluator.py`
- **co_filename (from bytecode):** `app\services\replay\evaluator.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** replay

## Module docstring

```
PAS141 — Deterministic evaluation of a reconstructed call.

Pure function — no LLMs, no provider calls, no I/O. Given the dict
returned by `reconstruction.reconstruct_call`, compute a replay score
and a human-readable summary that flags missing lifecycle data.

The score is intentionally a simple weighted coverage of lifecycle
steps so the result is stable across days and easy to reason about.
PAS142 (the evaluation framework proper) will layer richer scoring
on top of this — but the *signals* it consumes are what this module
emits.
```

## Imports

`List`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_collect_warnings`, `_summary_text`, `_zero_result`, `evaluate_reconstruction`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS141 — Deterministic evaluation of a reconstructed call.\n\nPure function — no LLMs, no provider calls, no I/O. Given the dict\nreturned by `reconstruction.reconstruct_call`, compute a replay score\nand a human-readable summary that flags missing lifecycle data.\n\nThe score is intentionally a simple weighted coverage of lifecycle\nsteps so the result is stable across days and easy to reason about.\nPAS142 (the evaluation framework proper) will layer richer scoring\non top of this — but the *signals* it consumes are what this module\nemits.\n'
- 'lead_received'
- 'pas_responded'
- 'lead_responded'
- 'intent_captured'
- 'budget_captured'
- 'timeline_captured'
- 'qualified'
- 'booking_or_callback'
- 'completed'
- 'step weights must sum to 100'
- 'reconstruction'
- 'return'
- '\nScore a reconstruction object. Returns:\n  {\n    "replay_score":   int (0..100),\n    "is_replayable":  bool,\n    "missing_steps":  [step, ...],     # subset of _STEP_WEIGHTS keys\n    "warnings":       [str, ...],      # plain-English diagnostics\n    "summary":        str,             # one-paragraph human summary\n  }\n\nNever raises. None / malformed input collapses to a zero score.\n'
- 'reconstruction was not a dict'
- 'missing_lifecycle_steps'
- 'replay_score'
- 'is_replayable'
- 'missing_steps'
- 'warnings'
- 'summary'
- 'rec'
- 'missing'
- 'present'
- 'turns'
- 'No turn-level events recorded — lead.uttered/pas.uttered missing or PAS_EVENT_TURN_LOGGING was off.'
- 'No lead turns recorded; only PAS-side speech captured.'
- 'No PAS turns recorded; only lead-side speech captured.'
- 'call.started event missing — lead arrival not anchored.'
- 'No terminal event (call.ended / call.ended_with_callback / call.failed).'
- 'Lead only partially qualified — '
- '/3 fields captured.'
- 'Call terminated without a booking attempt or callback request.'
- 'events_count'
- 'No events at all for this call_id — query returned empty.'
- 'speaker'
- 'lead'
- 'pas'
- 'score'
- 'replayable'
- 'call_id'
- 'unknown'
- 'extracted_fields'
- 'final_outcome'
- 'no terminal outcome recorded'
- 'workflow_stages_seen'
- 'Call '
- ': no events found. Replay impossible.'
- ' reconstructed from '
- ' events ('
- ' turns, '
- ' extracted fields, '
- ' workflow stage(s)). Final outcome: '
- '. Replay score '
- '/100, '
- 'NOT replayable'
- ' Missing lifecycle steps: '
- 'Reconstruction was empty or malformed; nothing to evaluate.'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS141 — Deterministic evaluation of a reconstructed call.\n\nPure function — no LLMs, no provider calls, no I/O. Given the dict\nreturned by `reconstruction.reconstruct_call`, compute a replay score\nand a human-readable summary that flags missing lifecycle data.\n\nThe score is intentionally a simple weighted coverage of lifecycle\nsteps so the result is stable across days and easy to reason about.\nPAS142 (the evaluation framework proper) will layer richer scoring\non top of this — but the *signals* it consumes are what this module\nemits.\n')
              STORE_NAME               0 (__doc__)

 15           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('List',))
              IMPORT_NAME              1 (typing)
              IMPORT_FROM              2 (List)
              STORE_NAME               2 (List)
              POP_TOP

 28           LOAD_CONST               2 ('lead_received')
              LOAD_SMALL_INT          15

 29           LOAD_CONST               3 ('pas_responded')
              LOAD_SMALL_INT          15

 30           LOAD_CONST               4 ('lead_responded')
              LOAD_SMALL_INT          15

 31           LOAD_CONST               5 ('intent_captured')
              LOAD_SMALL_INT          10

 32           LOAD_CONST               6 ('budget_captured')
              LOAD_SMALL_INT          10

 33           LOAD_CONST               7 ('timeline_captured')
              LOAD_SMALL_INT          10

 34           LOAD_CONST               8 ('qualified')
              LOAD_SMALL_INT           5

 35           LOAD_CONST               9 ('booking_or_callback')
              LOAD_SMALL_INT          15

 36           LOAD_CONST              10 ('completed')
              LOAD_SMALL_INT           5

 27           BUILD_MAP                9
              STORE_NAME               3 (_STEP_WEIGHTS)

 38           LOAD_NAME                4 (sum)
              PUSH_NULL
              LOAD_NAME                3 (_STEP_WEIGHTS)
              LOAD_ATTR               11 (values + NULL|self)
              CALL                     0
              CALL                     1
              LOAD_SMALL_INT         100
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_TRUE         8 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     0 (AssertionError)
              LOAD_CONST              11 ('step weights must sum to 100')
              CALL                     0
              RAISE_VARARGS            1

 44   L1:     BUILD_SET                0
              LOAD_CONST              20 (frozenset({'completed', 'lead_responded', 'pas_responded'}))
              SET_UPDATE               1
              STORE_NAME               6 (_REPLAYABLE_REQUIREMENTS)

 47           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C18025030, file "app\services\replay\evaluator.py", line 47>)
              MAKE_FUNCTION
              LOAD_CONST              13 (<code object evaluate_reconstruction at 0x0000018C17E93990, file "app\services\replay\evaluator.py", line 47>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME               7 (evaluate_reconstruction)

 82           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C1802C880, file "app\services\replay\evaluator.py", line 82>)
              MAKE_FUNCTION
              LOAD_CONST              15 (<code object _collect_warnings at 0x0000018C17D6DFC0, file "app\services\replay\evaluator.py", line 82>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME               8 (_collect_warnings)

119           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C1802C4F0, file "app\services\replay\evaluator.py", line 119>)
              MAKE_FUNCTION
              LOAD_CONST              17 (<code object _summary_text at 0x0000018C17D8BF50, file "app\services\replay\evaluator.py", line 119>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME               9 (_summary_text)

143           LOAD_CONST              18 (<code object _zero_result at 0x0000018C18053630, file "app\services\replay\evaluator.py", line 143>)
              MAKE_FUNCTION
              STORE_NAME              10 (_zero_result)
              LOAD_CONST              19 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025030, file "app\services\replay\evaluator.py", line 47>:
 47           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('reconstruction')
              LOAD_GLOBAL              0 (dict)
              LOAD_CONST               2 ('return')
              LOAD_GLOBAL              0 (dict)
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object evaluate_reconstruction at 0x0000018C17E93990, file "app\services\replay\evaluator.py", line 47>:
  47           RESUME                   0

  60           LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (reconstruction)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        13 (to L1)
               NOT_TAKEN

  61           LOAD_GLOBAL              5 (_zero_result + NULL)
               LOAD_CONST               1 ('reconstruction was not a dict')
               BUILD_LIST               1
               CALL                     1
               RETURN_VALUE

  63   L1:     LOAD_GLOBAL              7 (list + NULL)
               LOAD_FAST_BORROW         0 (reconstruction)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST               2 ('missing_lifecycle_steps')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               BUILD_LIST               0
       L2:     CALL                     1
               STORE_FAST               1 (missing)

  64           LOAD_GLOBAL             11 (set + NULL)
               LOAD_GLOBAL             12 (_STEP_WEIGHTS)
               CALL                     1
               LOAD_GLOBAL             11 (set + NULL)
               LOAD_FAST_BORROW         1 (missing)
               CALL                     1
               BINARY_OP               10 (-)
               STORE_FAST               2 (present)

  66           LOAD_GLOBAL             15 (sum + NULL)
               LOAD_CONST               3 (<code object <genexpr> at 0x0000018C17C49B80, file "app\services\replay\evaluator.py", line 66>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         2 (present)
               GET_ITER
               CALL                     0
               CALL                     1
               STORE_FAST               3 (score)

  67           LOAD_GLOBAL             17 (max + NULL)
               LOAD_SMALL_INT           0
               LOAD_GLOBAL             19 (min + NULL)
               LOAD_SMALL_INT         100
               LOAD_FAST_BORROW         3 (score)
               CALL                     2
               CALL                     2
               STORE_FAST               3 (score)

  68           LOAD_GLOBAL             20 (_REPLAYABLE_REQUIREMENTS)
               LOAD_ATTR               23 (issubset + NULL|self)
               LOAD_FAST_BORROW         2 (present)
               CALL                     1
               STORE_FAST               4 (is_replayable)

  70           LOAD_GLOBAL             25 (_collect_warnings + NULL)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (reconstruction, missing)
               LOAD_FAST_BORROW         2 (present)
               CALL                     3
               STORE_FAST               5 (warnings)

  71           LOAD_GLOBAL             27 (_summary_text + NULL)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (reconstruction, present)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 19 (missing, score)
               LOAD_FAST_BORROW         4 (is_replayable)
               CALL                     5
               STORE_FAST               6 (summary)

  74           LOAD_CONST               4 ('replay_score')
               LOAD_FAST                3 (score)

  75           LOAD_CONST               5 ('is_replayable')
               LOAD_FAST                4 (is_replayable)

  76           LOAD_CONST               6 ('missing_steps')
               LOAD_GLOBAL             12 (_STEP_WEIGHTS)
               GET_ITER
               LOAD_FAST_AND_CLEAR      7 (s)
               SWAP                     2
       L3:     BUILD_LIST               0
               SWAP                     2
       L4:     FOR_ITER                13 (to L7)
               STORE_FAST_LOAD_FAST   119 (s, s)
               LOAD_FAST_BORROW         1 (missing)
               CONTAINS_OP              0 (in)
       L5:     POP_JUMP_IF_TRUE         3 (to L6)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L4)
       L6:     LOAD_FAST_BORROW         7 (s)
               LIST_APPEND              2
               JUMP_BACKWARD           15 (to L4)
       L7:     END_FOR
               POP_ITER
       L8:     SWAP                     2
               STORE_FAST               7 (s)

  77           LOAD_CONST               7 ('warnings')
               LOAD_FAST_BORROW         5 (warnings)

  78           LOAD_CONST               8 ('summary')
               LOAD_FAST_BORROW         6 (summary)

  73           BUILD_MAP                5
               RETURN_VALUE

  --   L9:     SWAP                     2
               POP_TOP

  76           SWAP                     2
               STORE_FAST               7 (s)
               RERAISE                  0
ExceptionTable:
  L3 to L5 -> L9 [7]
  L6 to L8 -> L9 [7]

Disassembly of <code object <genexpr> at 0x0000018C17C49B80, file "app\services\replay\evaluator.py", line 66>:
  66           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                30 (to L5)
               STORE_FAST_LOAD_FAST    17 (s, s)
               LOAD_GLOBAL              0 (_STEP_WEIGHTS)
               CONTAINS_OP              0 (in)
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           15 (to L2)
       L4:     LOAD_GLOBAL              0 (_STEP_WEIGHTS)
               LOAD_FAST_BORROW         1 (s)
               BINARY_OP               26 ([])
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           32 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C1802C880, file "app\services\replay\evaluator.py", line 82>:
 82           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('rec')
              LOAD_GLOBAL              0 (dict)
              LOAD_CONST               2 ('missing')
              LOAD_GLOBAL              2 (list)
              LOAD_CONST               3 ('present')
              LOAD_GLOBAL              4 (set)
              LOAD_CONST               4 ('return')
              LOAD_GLOBAL              6 (List)
              LOAD_GLOBAL              8 (str)
              BINARY_OP               26 ([])
              BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object _collect_warnings at 0x0000018C17D6DFC0, file "app\services\replay\evaluator.py", line 82>:
  --           MAKE_CELL                2 (present)

  82           RESUME                   0

  83           BUILD_LIST               0
               STORE_FAST               3 (w)

  85           LOAD_FAST_BORROW         0 (rec)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('turns')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               BUILD_LIST               0
       L1:     STORE_FAST               4 (turns)

  86           LOAD_GLOBAL              3 (sum + NULL)
               LOAD_CONST               1 (<code object <genexpr> at 0x0000018C1802CC10, file "app\services\replay\evaluator.py", line 86>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         4 (turns)
               GET_ITER
               CALL                     0
               CALL                     1
               STORE_FAST               5 (n_lead)

  87           LOAD_GLOBAL              3 (sum + NULL)
               LOAD_CONST               2 (<code object <genexpr> at 0x0000018C1802C9B0, file "app\services\replay\evaluator.py", line 87>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         4 (turns)
               GET_ITER
               CALL                     0
               CALL                     1
               STORE_FAST               6 (n_pas)

  89           LOAD_FAST_BORROW         4 (turns)
               TO_BOOL
               POP_JUMP_IF_TRUE        19 (to L2)
               NOT_TAKEN

  90           LOAD_FAST_BORROW         3 (w)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_CONST               3 ('No turn-level events recorded — lead.uttered/pas.uttered missing or PAS_EVENT_TURN_LOGGING was off.')
               CALL                     1
               POP_TOP
               JUMP_FORWARD            48 (to L4)

  92   L2:     LOAD_FAST_BORROW         5 (n_lead)
               LOAD_SMALL_INT           0
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       18 (to L3)
               NOT_TAKEN

  93           LOAD_FAST_BORROW         3 (w)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_CONST               4 ('No lead turns recorded; only PAS-side speech captured.')
               CALL                     1
               POP_TOP

  94   L3:     LOAD_FAST_BORROW         6 (n_pas)
               LOAD_SMALL_INT           0
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       18 (to L4)
               NOT_TAKEN

  95           LOAD_FAST_BORROW         3 (w)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_CONST               5 ('No PAS turns recorded; only lead-side speech captured.')
               CALL                     1
               POP_TOP

  97   L4:     LOAD_CONST               6 ('lead_received')
               LOAD_FAST_BORROW         1 (missing)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       18 (to L5)
               NOT_TAKEN

  98           LOAD_FAST_BORROW         3 (w)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_CONST               7 ('call.started event missing — lead arrival not anchored.')
               CALL                     1
               POP_TOP

  99   L5:     LOAD_CONST               8 ('completed')
               LOAD_FAST_BORROW         1 (missing)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       18 (to L6)
               NOT_TAKEN

 100           LOAD_FAST_BORROW         3 (w)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_CONST               9 ('No terminal event (call.ended / call.ended_with_callback / call.failed).')
               CALL                     1
               POP_TOP

 101   L6:     LOAD_CONST              10 ('qualified')
               LOAD_FAST_BORROW         1 (missing)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       50 (to L7)
               NOT_TAKEN

 103           LOAD_GLOBAL              3 (sum + NULL)
               LOAD_FAST_BORROW         2 (present)
               BUILD_TUPLE              1
               LOAD_CONST              11 (<code object <genexpr> at 0x0000018C180E4030, file "app\services\replay\evaluator.py", line 103>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)

 104           LOAD_CONST              18 (('intent_captured', 'budget_captured', 'timeline_captured'))
               GET_ITER

 103           CALL                     0
               CALL                     1
               STORE_FAST               7 (captured)

 107           LOAD_FAST_BORROW         7 (captured)
               LOAD_SMALL_INT           0
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE       22 (to L7)
               NOT_TAKEN

 108           LOAD_FAST_BORROW         3 (w)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_CONST              12 ('Lead only partially qualified — ')
               LOAD_FAST_BORROW         7 (captured)
               FORMAT_SIMPLE
               LOAD_CONST              13 ('/3 fields captured.')
               BUILD_STRING             3
               CALL                     1
               POP_TOP

 110   L7:     LOAD_CONST              14 ('booking_or_callback')
               LOAD_FAST_BORROW         1 (missing)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       25 (to L8)
               NOT_TAKEN
               LOAD_CONST               8 ('completed')
               LOAD_DEREF               2 (present)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       18 (to L8)
               NOT_TAKEN

 111           LOAD_FAST_BORROW         3 (w)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_CONST              15 ('Call terminated without a booking attempt or callback request.')
               CALL                     1
               POP_TOP

 113   L8:     LOAD_FAST_BORROW         0 (rec)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST              16 ('events_count')
               LOAD_SMALL_INT           0
               CALL                     2
               LOAD_SMALL_INT           0
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       18 (to L9)
               NOT_TAKEN

 114           LOAD_FAST_BORROW         3 (w)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_CONST              17 ('No events at all for this call_id — query returned empty.')
               CALL                     1
               POP_TOP

 116   L9:     LOAD_FAST_BORROW         3 (w)
               RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C1802CC10, file "app\services\replay\evaluator.py", line 86>:
  86           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                30 (to L5)
               STORE_FAST_LOAD_FAST    17 (t, t)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('speaker')
               CALL                     1
               LOAD_CONST               1 ('lead')
               COMPARE_OP              88 (bool(==))
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           26 (to L2)
       L4:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           32 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C1802C9B0, file "app\services\replay\evaluator.py", line 87>:
  87           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                30 (to L5)
               STORE_FAST_LOAD_FAST    17 (t, t)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('speaker')
               CALL                     1
               LOAD_CONST               1 ('pas')
               COMPARE_OP              88 (bool(==))
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           26 (to L2)
       L4:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           32 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C180E4030, file "app\services\replay\evaluator.py", line 103>:
  --           COPY_FREE_VARS           1

 103           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 104   L2:     FOR_ITER                16 (to L5)
               STORE_FAST               1 (s)

 105           LOAD_FAST_BORROW         1 (s)
               LOAD_DEREF               2 (present)
               CONTAINS_OP              0 (in)

 104   L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           12 (to L2)
       L4:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           18 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C1802C4F0, file "app\services\replay\evaluator.py", line 119>:
119           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('rec')
              LOAD_GLOBAL              0 (dict)
              LOAD_CONST               2 ('present')
              LOAD_GLOBAL              2 (set)
              LOAD_CONST               3 ('missing')
              LOAD_GLOBAL              4 (list)
              LOAD_CONST               4 ('score')
              LOAD_GLOBAL              6 (int)
              LOAD_CONST               5 ('replayable')
              LOAD_GLOBAL              8 (bool)
              LOAD_CONST               6 ('return')
              LOAD_GLOBAL             10 (str)
              BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _summary_text at 0x0000018C17D8BF50, file "app\services\replay\evaluator.py", line 119>:
119           RESUME                   0

120           LOAD_FAST_BORROW         0 (rec)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               0 ('call_id')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 ('unknown')
      L1:     STORE_FAST               5 (call_id)

121           LOAD_FAST_BORROW         0 (rec)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               2 ('events_count')
              LOAD_SMALL_INT           0
              CALL                     2
              STORE_FAST               6 (n_events)

122           LOAD_GLOBAL              3 (len + NULL)
              LOAD_FAST_BORROW         0 (rec)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               3 ('turns')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L2:     CALL                     1
              STORE_FAST               7 (n_turns)

123           LOAD_GLOBAL              3 (len + NULL)
              LOAD_FAST_BORROW         0 (rec)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               4 ('extracted_fields')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L3:     CALL                     1
              STORE_FAST               8 (n_extracted)

124           LOAD_FAST_BORROW         0 (rec)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               5 ('final_outcome')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               6 ('no terminal outcome recorded')
      L4:     STORE_FAST               9 (outcome)

125           LOAD_FAST_BORROW         0 (rec)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               7 ('workflow_stages_seen')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L5:     STORE_FAST              10 (stages)

127           LOAD_FAST_BORROW         6 (n_events)
              LOAD_SMALL_INT           0
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        7 (to L6)
              NOT_TAKEN

128           LOAD_CONST               8 ('Call ')
              LOAD_FAST_BORROW         5 (call_id)
              FORMAT_SIMPLE
              LOAD_CONST               9 (': no events found. Replay impossible.')
              BUILD_STRING             3
              RETURN_VALUE

131   L6:     LOAD_CONST               8 ('Call ')
              LOAD_FAST                5 (call_id)
              FORMAT_SIMPLE
              LOAD_CONST              10 (' reconstructed from ')
              LOAD_FAST                6 (n_events)
              FORMAT_SIMPLE
              LOAD_CONST              11 (' events (')

132           LOAD_FAST                7 (n_turns)
              FORMAT_SIMPLE
              LOAD_CONST              12 (' turns, ')
              LOAD_FAST                8 (n_extracted)
              FORMAT_SIMPLE
              LOAD_CONST              13 (' extracted fields, ')

133           LOAD_GLOBAL              3 (len + NULL)
              LOAD_FAST_BORROW        10 (stages)
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST              14 (' workflow stage(s)). Final outcome: ')

134           LOAD_FAST                9 (outcome)
              FORMAT_SIMPLE
              LOAD_CONST              15 ('. Replay score ')

135           LOAD_FAST                3 (score)
              FORMAT_SIMPLE
              LOAD_CONST              16 ('/100, ')

136           LOAD_FAST_BORROW         4 (replayable)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L7)
              NOT_TAKEN
              LOAD_CONST              17 ('replayable')
              JUMP_FORWARD             1 (to L8)
      L7:     LOAD_CONST              18 ('NOT replayable')
      L8:     FORMAT_SIMPLE
              LOAD_CONST              19 ('.')

131           BUILD_STRING            17

130           STORE_FAST              11 (base)

138           LOAD_FAST_BORROW         2 (missing)
              TO_BOOL
              POP_JUMP_IF_FALSE       29 (to L9)
              NOT_TAKEN

139           LOAD_FAST_BORROW        11 (base)
              LOAD_CONST              20 (' Missing lifecycle steps: ')
              LOAD_CONST              21 (', ')
              LOAD_ATTR                5 (join + NULL|self)
              LOAD_FAST_BORROW         2 (missing)
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST              19 ('.')
              BUILD_STRING             3
              BINARY_OP               13 (+=)
              STORE_FAST              11 (base)

140   L9:     LOAD_FAST_BORROW        11 (base)
              RETURN_VALUE

Disassembly of <code object _zero_result at 0x0000018C18053630, file "app\services\replay\evaluator.py", line 143>:
143           RESUME                   0

145           LOAD_CONST               0 ('replay_score')
              LOAD_SMALL_INT           0

146           LOAD_CONST               1 ('is_replayable')
              LOAD_CONST               2 (False)

147           LOAD_CONST               3 ('missing_steps')
              LOAD_GLOBAL              1 (list + NULL)
              LOAD_GLOBAL              2 (_STEP_WEIGHTS)
              CALL                     1

148           LOAD_CONST               4 ('warnings')
              LOAD_GLOBAL              1 (list + NULL)
              LOAD_FAST_BORROW         0 (warnings)
              CALL                     1

149           LOAD_CONST               5 ('summary')
              LOAD_CONST               6 ('Reconstruction was empty or malformed; nothing to evaluate.')

144           BUILD_MAP                5
              RETURN_VALUE
```
