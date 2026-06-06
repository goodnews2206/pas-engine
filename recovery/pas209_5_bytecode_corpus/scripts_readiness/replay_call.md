# scripts_readiness/replay_call

- **pyc:** `scripts\__pycache__\replay_call.cpython-314.pyc`
- **expected source path (absent):** `scripts/replay_call.py`
- **co_filename (from bytecode):** `scripts\replay_call.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS141 — CLI: replay one call from pas_events.

Usage:
    python scripts/replay_call.py CALL_ID
    python scripts/replay_call.py CALL_ID --brokerage-id demo
    python scripts/replay_call.py CALL_ID --json

Exit codes:
    0   reconstruction produced a non-empty timeline
    1   no events / unknown call
    2   bad CLI arguments
```

## Imports

`Optional`, `__future__`, `annotations`, `app.services.replay.evaluator`, `app.services.replay.event_reader`, `app.services.replay.reconstruction`, `argparse`, `evaluate_reconstruction`, `json`, `load_call_events_unscoped`, `os`, `reconstruct_call`, `sys`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_format_human`, `main`

## Env-key candidates

`SUMMARY`, `WARNINGS`

## String constants (redacted where noted)

- '\nPAS141 — CLI: replay one call from pas_events.\n\nUsage:\n    python scripts/replay_call.py CALL_ID\n    python scripts/replay_call.py CALL_ID --brokerage-id demo\n    python scripts/replay_call.py CALL_ID --json\n\nExit codes:\n    0   reconstruction produced a non-empty timeline\n    1   no events / unknown call\n    2   bad CLI arguments\n'
- 'rec'
- 'dict'
- 'eval_'
- 'return'
- 'str'
- 'CALL '
- 'call_id'
- '<unknown>'
- '  brokerage:       '
- 'brokerage_id'
- '  events:          '
- 'events_count'
- '  turns:           '
- 'turns'
- '  final_outcome:   '
- 'final_outcome'
- '<none>'
- '  replay_score:    '
- 'replay_score'
- '/100'
- '  is_replayable:   '
- 'is_replayable'
- 'extracted_fields'
- 'EXTRACTED FIELDS'
- '  - '
- 'value'
- ' (confidence='
- 'confidence'
- 'workflow_stages_seen'
- 'WORKFLOW STAGES SEEN (in order)'
- 'missing_steps'
- 'MISSING LIFECYCLE STEPS'
- 'warnings'
- 'WARNINGS'
- '  ! '
- 'timeline'
- 'KEY TIMELINE (first '
- ' of '
- 'summary'
- 'SUMMARY'
- '========================================================================'
- 'argv'
- 'Optional[list]'
- 'int'
- 'replay_call'
- 'Reconstruct + evaluate one PAS call from pas_events.'
- 'The call_id (Twilio CA... or sim SIM-...).'
- '--brokerage-id'
- 'Optional brokerage_id filter for tenant-scoped reads.'
- '--json'
- 'store_true'
- 'Emit the full reconstruction + evaluation as JSON.'
- 'reconstruction'
- 'evaluation'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS141 — CLI: replay one call from pas_events.\n\nUsage:\n    python scripts/replay_call.py CALL_ID\n    python scripts/replay_call.py CALL_ID --brokerage-id demo\n    python scripts/replay_call.py CALL_ID --json\n\nExit codes:\n    0   reconstruction produced a non-empty timeline\n    1   no events / unknown call\n    2   bad CLI arguments\n')
              STORE_NAME               0 (__doc__)

 15           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 17           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (argparse)
              STORE_NAME               3 (argparse)

 18           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              4 (json)
              STORE_NAME               4 (json)

 19           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              5 (os)
              STORE_NAME               5 (os)

 20           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              6 (sys)
              STORE_NAME               6 (sys)

 21           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('Optional',))
              IMPORT_NAME              7 (typing)
              IMPORT_FROM              8 (Optional)
              STORE_NAME               8 (Optional)
              POP_TOP

 26           LOAD_NAME                5 (os)
              LOAD_ATTR               18 (path)
              LOAD_ATTR               21 (abspath + NULL|self)
              LOAD_NAME                5 (os)
              LOAD_ATTR               18 (path)
              LOAD_ATTR               23 (join + NULL|self)
              LOAD_NAME                5 (os)
              LOAD_ATTR               18 (path)
              LOAD_ATTR               25 (dirname + NULL|self)
              LOAD_NAME               13 (__file__)
              CALL                     1
              LOAD_CONST               4 ('..')
              CALL                     2
              CALL                     1
              STORE_NAME              14 (_REPO_ROOT)

 27           LOAD_NAME               14 (_REPO_ROOT)
              LOAD_NAME                6 (sys)
              LOAD_ATTR               18 (path)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE       29 (to L1)
              NOT_TAKEN

 28           LOAD_NAME                6 (sys)
              LOAD_ATTR               18 (path)
              LOAD_ATTR               31 (insert + NULL|self)
              LOAD_SMALL_INT           0
              LOAD_NAME               14 (_REPO_ROOT)
              CALL                     2
              POP_TOP

 31   L1:     LOAD_SMALL_INT           0
              LOAD_CONST               5 (('load_call_events_unscoped',))
              IMPORT_NAME             16 (app.services.replay.event_reader)
              IMPORT_FROM             17 (load_call_events_unscoped)
              STORE_NAME              18 (load_call_events)
              POP_TOP

 37           LOAD_SMALL_INT           0
              LOAD_CONST               6 (('reconstruct_call',))
              IMPORT_NAME             19 (app.services.replay.reconstruction)
              IMPORT_FROM             20 (reconstruct_call)
              STORE_NAME              20 (reconstruct_call)
              POP_TOP

 38           LOAD_SMALL_INT           0
              LOAD_CONST               7 (('evaluate_reconstruction',))
              IMPORT_NAME             21 (app.services.replay.evaluator)
              IMPORT_FROM             22 (evaluate_reconstruction)
              STORE_NAME              22 (evaluate_reconstruction)
              POP_TOP

 41           LOAD_CONST               8 (<code object __annotate__ at 0x0000018C18026130, file "scripts\replay_call.py", line 41>)
              MAKE_FUNCTION
              LOAD_CONST               9 (<code object _format_human at 0x0000018C17ED1780, file "scripts\replay_call.py", line 41>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              23 (_format_human)

 98           LOAD_CONST              13 ((None,))
              LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA31E0, file "scripts\replay_call.py", line 98>)
              MAKE_FUNCTION
              LOAD_CONST              11 (<code object main at 0x0000018C17D88940, file "scripts\replay_call.py", line 98>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              24 (main)

129           LOAD_NAME               25 (__name__)
              LOAD_CONST              12 ('__main__')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE       14 (to L2)
              NOT_TAKEN

130           LOAD_NAME               26 (SystemExit)
              PUSH_NULL
              LOAD_NAME               24 (main)
              PUSH_NULL
              CALL                     0
              CALL                     1
              RAISE_VARARGS            1

129   L2:     LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026130, file "scripts\replay_call.py", line 41>:
 41           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('rec')
              LOAD_CONST               2 ('dict')
              LOAD_CONST               3 ('eval_')
              LOAD_CONST               2 ('dict')
              LOAD_CONST               4 ('return')
              LOAD_CONST               5 ('str')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _format_human at 0x0000018C17ED1780, file "scripts\replay_call.py", line 41>:
 41            RESUME                   0

 42            BUILD_LIST               0
               STORE_FAST               2 (lines)

 43            LOAD_FAST_BORROW         2 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              43 ('========================================================================')
               CALL                     1
               POP_TOP

 44            LOAD_FAST                2 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST               1 ('CALL ')
               LOAD_FAST_BORROW         0 (rec)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST               2 ('call_id')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               3 ('<unknown>')
       L1:     FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

 45            LOAD_FAST                2 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST               4 ('  brokerage:       ')
               LOAD_FAST_BORROW         0 (rec)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST               5 ('brokerage_id')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               3 ('<unknown>')
       L2:     FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

 46            LOAD_FAST_BORROW         2 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST               6 ('  events:          ')
               LOAD_FAST_BORROW         0 (rec)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST               7 ('events_count')
               LOAD_SMALL_INT           0
               CALL                     2
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

 47            LOAD_FAST                2 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST               8 ('  turns:           ')
               LOAD_GLOBAL              5 (len + NULL)
               LOAD_FAST_BORROW         0 (rec)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST               9 ('turns')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               BUILD_LIST               0
       L3:     CALL                     1
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

 48            LOAD_FAST                2 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              10 ('  final_outcome:   ')
               LOAD_FAST_BORROW         0 (rec)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              11 ('final_outcome')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              12 ('<none>')
       L4:     FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

 49            LOAD_FAST_BORROW         2 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              13 ('  replay_score:    ')
               LOAD_FAST_BORROW         1 (eval_)
               LOAD_CONST              14 ('replay_score')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               LOAD_CONST              15 ('/100')
               BUILD_STRING             3
               CALL                     1
               POP_TOP

 50            LOAD_FAST_BORROW         2 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              16 ('  is_replayable:   ')
               LOAD_FAST_BORROW         1 (eval_)
               LOAD_CONST              17 ('is_replayable')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

 51            LOAD_FAST_BORROW         2 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              18 ('')
               CALL                     1
               POP_TOP

 53            LOAD_FAST_BORROW         0 (rec)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              19 ('extracted_fields')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               POP_TOP
               BUILD_MAP                0
       L5:     STORE_FAST               3 (fields)

 54            LOAD_FAST_BORROW         3 (fields)
               TO_BOOL
               POP_JUMP_IF_FALSE      117 (to L8)
               NOT_TAKEN

 55            LOAD_FAST_BORROW         2 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              20 ('EXTRACTED FIELDS')
               CALL                     1
               POP_TOP

 56            LOAD_FAST_BORROW         3 (fields)
               LOAD_ATTR                7 (items + NULL|self)
               CALL                     0
               GET_ITER
       L6:     FOR_ITER                62 (to L7)
               UNPACK_SEQUENCE          2
               STORE_FAST_STORE_FAST   69 (name, info)

 57            LOAD_FAST_BORROW         2 (lines)
               LOAD_ATTR                1 (append + NULL|self)

 58            LOAD_CONST              21 ('  - ')
               LOAD_FAST_BORROW         4 (name)
               FORMAT_SIMPLE
               LOAD_CONST              22 (': ')
               LOAD_FAST_BORROW         5 (info)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              23 ('value')
               CALL                     1
               FORMAT_SIMPLE
               LOAD_CONST              24 (' (confidence=')

 59            LOAD_FAST_BORROW         5 (info)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              25 ('confidence')
               CALL                     1
               FORMAT_SIMPLE
               LOAD_CONST              26 (')')

 58            BUILD_STRING             7

 57            CALL                     1
               POP_TOP
               JUMP_BACKWARD           64 (to L6)

 56    L7:     END_FOR
               POP_ITER

 61            LOAD_FAST_BORROW         2 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              18 ('')
               CALL                     1
               POP_TOP

 63    L8:     LOAD_FAST_BORROW         0 (rec)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              27 ('workflow_stages_seen')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L9)
               NOT_TAKEN
               POP_TOP
               BUILD_LIST               0
       L9:     STORE_FAST               6 (stages)

 64            LOAD_FAST_BORROW         6 (stages)
               TO_BOOL
               POP_JUMP_IF_FALSE       64 (to L12)
               NOT_TAKEN

 65            LOAD_FAST_BORROW         2 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              28 ('WORKFLOW STAGES SEEN (in order)')
               CALL                     1
               POP_TOP

 66            LOAD_FAST_BORROW         6 (stages)
               GET_ITER
      L10:     FOR_ITER                23 (to L11)
               STORE_FAST               7 (s)

 67            LOAD_FAST_BORROW         2 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              21 ('  - ')
               LOAD_FAST_BORROW         7 (s)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           25 (to L10)

 66   L11:     END_FOR
               POP_ITER

 68            LOAD_FAST_BORROW         2 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              18 ('')
               CALL                     1
               POP_TOP

 70   L12:     LOAD_FAST_BORROW         1 (eval_)
               LOAD_CONST              29 ('missing_steps')
               BINARY_OP               26 ([])
               TO_BOOL
               POP_JUMP_IF_FALSE       71 (to L15)
               NOT_TAKEN

 71            LOAD_FAST_BORROW         2 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              30 ('MISSING LIFECYCLE STEPS')
               CALL                     1
               POP_TOP

 72            LOAD_FAST_BORROW         1 (eval_)
               LOAD_CONST              29 ('missing_steps')
               BINARY_OP               26 ([])
               GET_ITER
      L13:     FOR_ITER                23 (to L14)
               STORE_FAST               7 (s)

 73            LOAD_FAST_BORROW         2 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              21 ('  - ')
               LOAD_FAST_BORROW         7 (s)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           25 (to L13)

 72   L14:     END_FOR
               POP_ITER

 74            LOAD_FAST_BORROW         2 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              18 ('')
               CALL                     1
               POP_TOP

 76   L15:     LOAD_FAST_BORROW         1 (eval_)
               LOAD_CONST              31 ('warnings')
               BINARY_OP               26 ([])
               TO_BOOL
               POP_JUMP_IF_FALSE       71 (to L18)
               NOT_TAKEN

 77            LOAD_FAST_BORROW         2 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              32 ('WARNINGS')
               CALL                     1
               POP_TOP

 78            LOAD_FAST_BORROW         1 (eval_)
               LOAD_CONST              31 ('warnings')
               BINARY_OP               26 ([])
               GET_ITER
      L16:     FOR_ITER                23 (to L17)
               STORE_FAST               8 (w)

 79            LOAD_FAST_BORROW         2 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              33 ('  ! ')
               LOAD_FAST_BORROW         8 (w)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           25 (to L16)

 78   L17:     END_FOR
               POP_ITER

 80            LOAD_FAST_BORROW         2 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              18 ('')
               CALL                     1
               POP_TOP

 82   L18:     LOAD_FAST_BORROW         0 (rec)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              34 ('timeline')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L19)
               NOT_TAKEN
               POP_TOP
               BUILD_LIST               0
      L19:     STORE_FAST               9 (timeline)

 83            LOAD_FAST_BORROW         9 (timeline)
               TO_BOOL
               POP_JUMP_IF_FALSE      149 (to L23)
               NOT_TAKEN

 85            LOAD_SMALL_INT          30
               STORE_FAST              10 (cap)

 86            LOAD_FAST_BORROW         2 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              35 ('KEY TIMELINE (first ')
               LOAD_GLOBAL              9 (min + NULL)
               LOAD_FAST_BORROW        10 (cap)
               LOAD_GLOBAL              5 (len + NULL)
               LOAD_FAST_BORROW         9 (timeline)
               CALL                     1
               CALL                     2
               FORMAT_SIMPLE
               LOAD_CONST              36 (' of ')
               LOAD_GLOBAL              5 (len + NULL)
               LOAD_FAST_BORROW         9 (timeline)
               CALL                     1
               FORMAT_SIMPLE
               LOAD_CONST              26 (')')
               BUILD_STRING             5
               CALL                     1
               POP_TOP

 87            LOAD_FAST_BORROW         9 (timeline)
               LOAD_CONST              37 (None)
               LOAD_FAST_BORROW        10 (cap)
               BINARY_SLICE
               GET_ITER
      L20:     FOR_ITER                68 (to L22)
               STORE_FAST              11 (entry)

 88            LOAD_FAST_BORROW        11 (entry)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              38 ('ts')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L21)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              18 ('')
      L21:     STORE_FAST              12 (ts)

 89            LOAD_FAST_BORROW         2 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              39 ('  ')
               LOAD_FAST_BORROW        12 (ts)
               FORMAT_SIMPLE
               LOAD_CONST              39 ('  ')
               LOAD_FAST_BORROW        11 (entry)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              40 ('summary')
               CALL                     1
               FORMAT_SIMPLE
               BUILD_STRING             4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           70 (to L20)

 87   L22:     END_FOR
               POP_ITER

 90            LOAD_FAST_BORROW         2 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              18 ('')
               CALL                     1
               POP_TOP

 92   L23:     LOAD_FAST_BORROW         2 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              41 ('SUMMARY')
               CALL                     1
               POP_TOP

 93            LOAD_FAST_BORROW         2 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              39 ('  ')
               LOAD_FAST_BORROW         1 (eval_)
               LOAD_CONST              40 ('summary')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

 94            LOAD_FAST_BORROW         2 (lines)
               LOAD_ATTR                1 (append + NULL|self)
               LOAD_CONST              43 ('========================================================================')
               CALL                     1
               POP_TOP

 95            LOAD_CONST              42 ('\n')
               LOAD_ATTR               11 (join + NULL|self)
               LOAD_FAST_BORROW         2 (lines)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "scripts\replay_call.py", line 98>:
 98           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17D88940, file "scripts\replay_call.py", line 98>:
 98           RESUME                   0

 99           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

100           LOAD_CONST               0 ('replay_call')

101           LOAD_CONST               1 ('Reconstruct + evaluate one PAS call from pas_events.')

 99           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               1 (parser)

103           LOAD_FAST_BORROW         1 (parser)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               3 ('call_id')
              LOAD_CONST               4 ('The call_id (Twilio CA... or sim SIM-...).')
              LOAD_CONST               5 (('help',))
              CALL_KW                  2
              POP_TOP

104           LOAD_FAST_BORROW         1 (parser)
              LOAD_ATTR                5 (add_argument + NULL|self)

105           LOAD_CONST               6 ('--brokerage-id')

106           LOAD_CONST               7 (None)

107           LOAD_CONST               8 ('Optional brokerage_id filter for tenant-scoped reads.')

104           LOAD_CONST               9 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

109           LOAD_FAST_BORROW         1 (parser)
              LOAD_ATTR                5 (add_argument + NULL|self)

110           LOAD_CONST              10 ('--json')

111           LOAD_CONST              11 ('store_true')

112           LOAD_CONST              12 ('Emit the full reconstruction + evaluation as JSON.')

109           LOAD_CONST              13 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

114           LOAD_FAST_BORROW         1 (parser)
              LOAD_ATTR                7 (parse_args + NULL|self)
              LOAD_FAST_BORROW         0 (argv)
              CALL                     1
              STORE_FAST               2 (args)

116           LOAD_GLOBAL              9 (load_call_events + NULL)
              LOAD_FAST_BORROW         2 (args)
              LOAD_ATTR               10 (call_id)
              LOAD_FAST_BORROW         2 (args)
              LOAD_ATTR               12 (brokerage_id)
              LOAD_CONST              14 (('brokerage_id',))
              CALL_KW                  2
              STORE_FAST               3 (events)

117           LOAD_GLOBAL             15 (reconstruct_call + NULL)
              LOAD_FAST_BORROW         3 (events)
              CALL                     1
              STORE_FAST               4 (rec)

118           LOAD_GLOBAL             17 (evaluate_reconstruction + NULL)
              LOAD_FAST_BORROW         4 (rec)
              CALL                     1
              STORE_FAST               5 (ev)

120           LOAD_FAST_BORROW         2 (args)
              LOAD_ATTR               18 (json)
              TO_BOOL
              POP_JUMP_IF_FALSE       46 (to L1)
              NOT_TAKEN

121           LOAD_CONST              15 ('reconstruction')
              LOAD_FAST_BORROW         4 (rec)
              LOAD_CONST              16 ('evaluation')
              LOAD_FAST_BORROW         5 (ev)
              BUILD_MAP                2
              STORE_FAST               6 (out)

122           LOAD_GLOBAL             21 (print + NULL)
              LOAD_GLOBAL             18 (json)
              LOAD_ATTR               22 (dumps)
              PUSH_NULL
              LOAD_FAST_BORROW         6 (out)
              LOAD_GLOBAL             24 (str)
              LOAD_SMALL_INT           2
              LOAD_CONST              17 (('default', 'indent'))
              CALL_KW                  3
              CALL                     1
              POP_TOP
              JUMP_FORWARD            20 (to L2)

124   L1:     LOAD_GLOBAL             21 (print + NULL)
              LOAD_GLOBAL             27 (_format_human + NULL)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (rec, ev)
              CALL                     2
              CALL                     1
              POP_TOP

126   L2:     LOAD_FAST_BORROW         4 (rec)
              LOAD_ATTR               29 (get + NULL|self)
              LOAD_CONST              18 ('events_count')
              LOAD_SMALL_INT           0
              CALL                     2
              LOAD_SMALL_INT           0
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_SMALL_INT           0
              RETURN_VALUE
      L3:     LOAD_SMALL_INT           1
              RETURN_VALUE
```
