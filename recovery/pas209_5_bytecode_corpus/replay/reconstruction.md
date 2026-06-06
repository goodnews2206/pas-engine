# replay/reconstruction

- **pyc:** `app\services\replay\__pycache__\reconstruction.cpython-314.pyc`
- **expected source path (absent):** `app\services\replay/reconstruction.py`
- **co_filename (from bytecode):** `C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\replay\reconstruction.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** replay

## Module docstring

```
PAS141 — Conversation + lifecycle reconstruction from normalized events.

Pure function: takes a chronologically-ordered list of normalized events
(see event_reader.normalize_event) and folds them into a structured
replay object. No I/O, no LLMs, no state mutation.

Lifecycle steps evaluated:
  - lead_received        any of: call.started, lead.received, or
                         workflow_stage='lead_received'
  - pas_responded        any pas.uttered, OR a state.transition with
                         actor='pas' (legacy emit pattern proves PAS engaged)
  - lead_responded       any lead.uttered, OR an objection.detected /
                         callback.requested with actor='lead'
  - intent_captured      lead.extracted with extracted_field='intent'
  - budget_captured      lead.extracted with extracted_field='budget'
  - timeline_captured    lead.extracted with extracted_field='timeline'
  - qualified            all three of intent / budget / timeline captured
  - booking_or_callback  booking.attempted/confirmed/failed OR
                         callback.requested OR call.ended_with_callback
  - completed            call.ended OR call.ended_with_callback OR call.failed
```

## Imports

`Iterable`, `List`, `Optional`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_empty_replay`, `_is_turn_event`, `_short`, `_summary_for`, `_terminal_outcome`, `reconstruct_call`

## Env-key candidates

_none_

## String constants (redacted where noted)

- "\nPAS141 — Conversation + lifecycle reconstruction from normalized events.\n\nPure function: takes a chronologically-ordered list of normalized events\n(see event_reader.normalize_event) and folds them into a structured\nreplay object. No I/O, no LLMs, no state mutation.\n\nLifecycle steps evaluated:\n  - lead_received        any of: call.started, lead.received, or\n                         workflow_stage='lead_received'\n  - pas_responded        any pas.uttered, OR a state.transition with\n                         actor='pas' (legacy emit pattern proves PAS engaged)\n  - lead_responded       any lead.uttered, OR an objection.detected /\n                         callback.requested with actor='lead'\n  - intent_captured      lead.extracted with extracted_field='intent'\n  - budget_captured      lead.extracted with extracted_field='budget'\n  - timeline_captured    lead.extracted with extracted_field='timeline'\n  - qualified            all three of intent / budget / timeline captured\n  - booking_or_callback  booking.attempted/confirmed/failed OR\n                         callback.requested OR call.ended_with_callback\n  - completed            call.ended OR call.ended_with_callback OR call.failed\n"
- 'lead.uttered'
- 'return'
- 'One-line human-readable summary for the timeline view.'
- 'event_type'
- 'actor'
- 'workflow_stage'
- 'actor='
- 'stage='
- 'lead.extracted'
- 'extracted_field'
- 'extracted_value'
- 'objection.detected'
- 'payload'
- 'category'
- 'category='
- 'state.transition'
- 'from'
- 'outcome_state'
- 'outcome'
- 'outcome='
- ' | '
- 'events'
- 'Last-write-wins across the three terminal event types.'
- 'call.failed'
- 'failed'
- '\nFold a normalized event stream into a structured replay object.\n\nRequired keys on each event dict — produced by\nevent_reader.normalize_event:\n  event_type, actor, workflow_stage, input_text, output_text,\n  extracted_field, extracted_value, confidence_score,\n  outcome_state, source, state, payload, created_at,\n  brokerage_id, call_id, lead_id, event_id\n\nOutput shape:\n  {\n    "call_id":                 str | None,\n    "brokerage_id":            str | None,\n    "timeline":                [{ts, event_type, summary}, ...],\n    "turns":                   [{ts, speaker, text, state, source_event_type}, ...],\n    "extracted_fields":        {field: {value, confidence, ts, source_event_type}},\n    "objections":              [{ts, category, text, actor}, ...],\n    "bookings":                [{ts, status, slot, error, booking_id}, ...],\n    "callbacks":               [{ts, kind, text, normalized_time, confirmed}, ...],\n    "final_outcome":           str | None,\n    "workflow_stages_seen":    [stage, ...],   # ordered by first appearance\n    "missing_lifecycle_steps": [step, ...],\n    "events_count":            int,\n  }\n\nNever raises. An empty/None input returns the same shape with\nzeros / empty lists / None.\n'
- 'created_at'
- 'summary'
- 'input_text'
- 'excerpt'
- 'speaker'
- 'lead'
- 'text'
- 'state'
- 'source_event_type'
- 'lead_responded'
- 'pas.uttered'
- 'output_text'
- 'pas'
- 'pas_responded'
- 'value'
- 'confidence'
- 'confidence_score'
- 'intent'
- 'intent_captured'
- 'budget'
- 'budget_captured'
- 'timeline'
- 'timeline_captured'
- 'status'
- 'slot'
- 'booking_id'
- 'error'
- 'booking_or_callback'
- 'callback.requested'
- 'kind'
- 'requested'
- 'trigger_excerpt'
- 'normalized_time'
- 'confirmed'
- 'call.ended_with_callback'
- 'finalized'
- 'callback_reason_excerpt'
- 'preferred_time_normalized'
- 'callback_confirmed'
- 'call.started'
- 'lead_received'
- 'completed'
- 'qualified'
- 'call_id'
- 'brokerage_id'
- 'turns'
- 'extracted_fields'
- 'objections'
- 'bookings'
- 'callbacks'
- 'final_outcome'
- 'workflow_stages_seen'
- 'missing_lifecycle_steps'
- 'events_count'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ("\nPAS141 — Conversation + lifecycle reconstruction from normalized events.\n\nPure function: takes a chronologically-ordered list of normalized events\n(see event_reader.normalize_event) and folds them into a structured\nreplay object. No I/O, no LLMs, no state mutation.\n\nLifecycle steps evaluated:\n  - lead_received        any of: call.started, lead.received, or\n                         workflow_stage='lead_received'\n  - pas_responded        any pas.uttered, OR a state.transition with\n                         actor='pas' (legacy emit pattern proves PAS engaged)\n  - lead_responded       any lead.uttered, OR an objection.detected /\n                         callback.requested with actor='lead'\n  - intent_captured      lead.extracted with extracted_field='intent'\n  - budget_captured      lead.extracted with extracted_field='budget'\n  - timeline_captured    lead.extracted with extracted_field='timeline'\n  - qualified            all three of intent / budget / timeline captured\n  - booking_or_callback  booking.attempted/confirmed/failed OR\n                         callback.requested OR call.ended_with_callback\n  - completed            call.ended OR call.ended_with_callback OR call.failed\n")
              STORE_NAME               0 (__doc__)

 24           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('Iterable', 'List', 'Optional'))
              IMPORT_NAME              1 (typing)
              IMPORT_FROM              2 (Iterable)
              STORE_NAME               2 (Iterable)
              IMPORT_FROM              3 (List)
              STORE_NAME               3 (List)
              IMPORT_FROM              4 (Optional)
              STORE_NAME               4 (Optional)
              POP_TOP

 27           LOAD_CONST              13 (('lead_received', 'pas_responded', 'lead_responded', 'intent_captured', 'budget_captured', 'timeline_captured', 'qualified', 'booking_or_callback', 'completed'))
              STORE_NAME               5 (_LIFECYCLE_STEPS)

 40           LOAD_CONST              14 ((160,))
              LOAD_CONST               2 (<code object _short at 0x0000018C17C49B80, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\replay\reconstruction.py", line 40>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME               6 (_short)

 47           LOAD_CONST               3 (<code object _is_turn_event at 0x0000018C180689D0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\replay\reconstruction.py", line 47>)
              MAKE_FUNCTION
              STORE_NAME               7 (_is_turn_event)

 51           LOAD_CONST               4 (<code object __annotate__ at 0x0000018C18025E30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\replay\reconstruction.py", line 51>)
              MAKE_FUNCTION
              LOAD_CONST               5 (<code object _summary_for at 0x0000018C17E7FED0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\replay\reconstruction.py", line 51>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME               8 (_summary_for)

 80           LOAD_CONST               6 (<code object __annotate__ at 0x0000018C1802C880, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\replay\reconstruction.py", line 80>)
              MAKE_FUNCTION
              LOAD_CONST               7 (<code object _terminal_outcome at 0x0000018C17E949B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\replay\reconstruction.py", line 80>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME               9 (_terminal_outcome)

 94           LOAD_CONST               8 (<code object __annotate__ at 0x0000018C18053630, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\replay\reconstruction.py", line 94>)
              MAKE_FUNCTION
              LOAD_CONST               9 (<code object reconstruct_call at 0x0000018C17ED88D0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\replay\reconstruction.py", line 94>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              10 (reconstruct_call)

285           LOAD_CONST              10 (<code object __annotate__ at 0x0000018C18025530, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\replay\reconstruction.py", line 285>)
              MAKE_FUNCTION
              LOAD_CONST              11 (<code object _empty_replay at 0x0000018C18053E10, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\replay\reconstruction.py", line 285>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              11 (_empty_replay)
              LOAD_CONST              12 (None)
              RETURN_VALUE

Disassembly of <code object _short at 0x0000018C17C49B80, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\replay\reconstruction.py", line 40>:
 40           RESUME                   0

 41           LOAD_FAST_BORROW         0 (text)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

 42           LOAD_CONST               0 ('')
              RETURN_VALUE

 43   L1:     LOAD_GLOBAL              1 (str + NULL)
              LOAD_FAST_BORROW         0 (text)
              CALL                     1
              STORE_FAST               2 (s)

 44           LOAD_GLOBAL              3 (len + NULL)
              LOAD_FAST_BORROW         2 (s)
              CALL                     1
              LOAD_FAST_BORROW         1 (n)
              COMPARE_OP              58 (bool(<=))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_FAST_BORROW         2 (s)
              RETURN_VALUE
      L2:     LOAD_FAST_BORROW         2 (s)
              LOAD_CONST               1 (None)
              LOAD_FAST_BORROW         1 (n)
              BINARY_SLICE
              RETURN_VALUE

Disassembly of <code object _is_turn_event at 0x0000018C180689D0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\replay\reconstruction.py", line 47>:
 47           RESUME                   0

 48           LOAD_FAST_BORROW         0 (et)
              LOAD_CONST               1 (('lead.uttered', 'pas.uttered'))
              CONTAINS_OP              0 (in)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025E30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\replay\reconstruction.py", line 51>:
 51           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('ev')
              LOAD_GLOBAL              0 (dict)
              LOAD_CONST               2 ('return')
              LOAD_GLOBAL              2 (str)
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _summary_for at 0x0000018C17E7FED0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\replay\reconstruction.py", line 51>:
  51            RESUME                   0

  53            LOAD_FAST_BORROW         0 (ev)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               1 ('event_type')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('?')
        L1:     STORE_FAST               1 (et)

  54            LOAD_FAST_BORROW         0 (ev)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               3 ('actor')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L2)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               4 ('')
        L2:     STORE_FAST               2 (actor)

  55            LOAD_FAST_BORROW         0 (ev)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               5 ('workflow_stage')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L3)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               4 ('')
        L3:     STORE_FAST               3 (stage)

  56            LOAD_FAST_BORROW         1 (et)
                BUILD_LIST               1
                STORE_FAST               4 (bits)

  57            LOAD_FAST_BORROW         2 (actor)
                TO_BOOL
                POP_JUMP_IF_FALSE       21 (to L4)
                NOT_TAKEN

  58            LOAD_FAST_BORROW         4 (bits)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_CONST               6 ('actor=')
                LOAD_FAST_BORROW         2 (actor)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

  59    L4:     LOAD_FAST_BORROW         3 (stage)
                TO_BOOL
                POP_JUMP_IF_FALSE       27 (to L5)
                NOT_TAKEN
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (stage, actor)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       21 (to L5)
                NOT_TAKEN

  60            LOAD_FAST_BORROW         4 (bits)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_CONST               7 ('stage=')
                LOAD_FAST_BORROW         3 (stage)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

  61    L5:     LOAD_FAST_BORROW         1 (et)
                LOAD_CONST               8 ('lead.extracted')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       76 (to L7)
                NOT_TAKEN

  62            LOAD_FAST_BORROW         0 (ev)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               9 ('extracted_field')
                CALL                     1
                LOAD_FAST_BORROW         0 (ev)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST              10 ('extracted_value')
                CALL                     1
                STORE_FAST_STORE_FAST  101 (v, f)

  63            LOAD_FAST_BORROW         5 (f)
                TO_BOOL
                POP_JUMP_IF_FALSE       33 (to L6)
                NOT_TAKEN

  64            LOAD_FAST_BORROW         4 (bits)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_FAST_BORROW         5 (f)
                FORMAT_SIMPLE
                LOAD_CONST              11 ('=')
                LOAD_GLOBAL              5 (_short + NULL)
                LOAD_FAST_BORROW         6 (v)
                LOAD_SMALL_INT          60
                CALL                     2
                FORMAT_SIMPLE
                BUILD_STRING             3
                CALL                     1
                POP_TOP

  --    L6:     EXTENDED_ARG             1
                JUMP_FORWARD           313 (to L17)

  65    L7:     LOAD_FAST_BORROW         1 (et)
                LOAD_CONST              12 ('objection.detected')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       72 (to L10)
                NOT_TAKEN

  66            LOAD_FAST_BORROW         0 (ev)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST              13 ('payload')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
        L8:     LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST              14 ('category')
                CALL                     1
                STORE_FAST               7 (cat)

  67            LOAD_FAST_BORROW         7 (cat)
                TO_BOOL
                POP_JUMP_IF_FALSE       21 (to L9)
                NOT_TAKEN

  68            LOAD_FAST_BORROW         4 (bits)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_CONST              15 ('category=')
                LOAD_FAST_BORROW         7 (cat)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

  --    L9:     JUMP_FORWARD           235 (to L17)

  69   L10:     LOAD_FAST_BORROW         1 (et)
                LOAD_CONST              16 ('state.transition')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE      127 (to L14)
                NOT_TAKEN

  70            LOAD_FAST_BORROW         0 (ev)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST              13 ('payload')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L11)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
       L11:     STORE_FAST               8 (p)

  71            LOAD_FAST_BORROW         8 (p)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST              17 ('from')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        24 (to L12)
                NOT_TAKEN
                LOAD_FAST_BORROW         8 (p)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST              18 ('to')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       53 (to L13)
                NOT_TAKEN

  72   L12:     LOAD_FAST_BORROW         4 (bits)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_FAST_BORROW         8 (p)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST              17 ('from')
                CALL                     1
                FORMAT_SIMPLE
                LOAD_CONST              19 ('->')
                LOAD_FAST_BORROW         8 (p)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST              18 ('to')
                CALL                     1
                FORMAT_SIMPLE
                BUILD_STRING             3
                CALL                     1
                POP_TOP

  --   L13:     JUMP_FORWARD           102 (to L17)

  73   L14:     LOAD_FAST_BORROW         1 (et)
                LOAD_CONST              24 (('call.ended', 'call.ended_with_callback', 'call.failed'))
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       96 (to L17)
                NOT_TAKEN

  74            LOAD_FAST_BORROW         0 (ev)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST              20 ('outcome_state')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        43 (to L16)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         0 (ev)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST              13 ('payload')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L15)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
       L15:     LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST              21 ('outcome')
                CALL                     1
       L16:     STORE_FAST               9 (oc)

  75            LOAD_FAST_BORROW         9 (oc)
                TO_BOOL
                POP_JUMP_IF_FALSE       21 (to L17)
                NOT_TAKEN

  76            LOAD_FAST_BORROW         4 (bits)
                LOAD_ATTR                3 (append + NULL|self)
                LOAD_CONST              22 ('outcome=')
                LOAD_FAST_BORROW         9 (oc)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

  77   L17:     LOAD_CONST              23 (' | ')
                LOAD_ATTR                7 (join + NULL|self)
                LOAD_FAST_BORROW         4 (bits)
                CALL                     1
                RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C1802C880, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\replay\reconstruction.py", line 80>:
 80           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('events')
              LOAD_GLOBAL              0 (Iterable)
              LOAD_GLOBAL              2 (dict)
              BINARY_OP               26 ([])
              LOAD_CONST               2 ('return')
              LOAD_GLOBAL              4 (Optional)
              LOAD_GLOBAL              6 (str)
              BINARY_OP               26 ([])
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _terminal_outcome at 0x0000018C17E949B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\replay\reconstruction.py", line 80>:
 80           RESUME                   0

 82           LOAD_CONST               1 (None)
              STORE_FAST               1 (last)

 83           LOAD_FAST_BORROW         0 (events)
              GET_ITER
      L1:     FOR_ITER               154 (to L8)
              STORE_FAST               2 (ev)

 84           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (ev)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

 85           JUMP_BACKWARD           27 (to L1)

 86   L2:     LOAD_FAST_BORROW         2 (ev)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               2 ('event_type')
              CALL                     1
              LOAD_CONST               8 (('call.ended', 'call.ended_with_callback', 'call.failed'))
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           51 (to L1)

 87   L3:     LOAD_FAST_BORROW         2 (ev)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               4 ('outcome_state')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE        43 (to L5)
              NOT_TAKEN
              POP_TOP
              LOAD_FAST_BORROW         2 (ev)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               5 ('payload')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L4:     LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               6 ('outcome')
              CALL                     1
      L5:     STORE_FAST               3 (oc)

 90           LOAD_FAST                3 (oc)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE        27 (to L7)
              NOT_TAKEN
              POP_TOP
              LOAD_FAST_BORROW         2 (ev)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               2 ('event_type')
              CALL                     1
              LOAD_CONST               3 ('call.failed')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        3 (to L6)
              NOT_TAKEN
              LOAD_CONST               7 ('failed')
              JUMP_FORWARD             1 (to L7)
      L6:     LOAD_FAST                1 (last)
      L7:     STORE_FAST               1 (last)
              JUMP_BACKWARD          156 (to L1)

 83   L8:     END_FOR
              POP_ITER

 91           LOAD_FAST_BORROW         1 (last)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18053630, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\replay\reconstruction.py", line 94>:
 94           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('events')
              LOAD_GLOBAL              0 (List)
              LOAD_GLOBAL              2 (dict)
              BINARY_OP               26 ([])
              LOAD_CONST               2 ('return')
              LOAD_GLOBAL              2 (dict)
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object reconstruct_call at 0x0000018C17ED88D0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\replay\reconstruction.py", line 94>:
  94            RESUME                   0

 124            LOAD_FAST_BORROW         0 (events)
                TO_BOOL
                POP_JUMP_IF_TRUE        13 (to L1)
                NOT_TAKEN

 125            LOAD_GLOBAL              1 (_empty_replay + NULL)
                LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                CALL                     2
                RETURN_VALUE

 130    L1:     LOAD_FAST_BORROW         0 (events)
                GET_ITER
                LOAD_FAST_AND_CLEAR      1 (e)
                SWAP                     2
        L2:     BUILD_LIST               0
                SWAP                     2
        L3:     FOR_ITER                29 (to L6)
                STORE_FAST               1 (e)
                LOAD_GLOBAL              3 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (e)
                LOAD_GLOBAL              4 (dict)
                CALL                     2
                TO_BOOL
        L4:     POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN
                JUMP_BACKWARD           27 (to L3)
        L5:     LOAD_FAST_BORROW         1 (e)
                LIST_APPEND              2
                JUMP_BACKWARD           31 (to L3)
        L6:     END_FOR
                POP_ITER
        L7:     STORE_FAST               2 (dict_events)
                STORE_FAST               1 (e)

 131            LOAD_GLOBAL              7 (next + NULL)
                LOAD_CONST               2 (<code object <genexpr> at 0x0000018C17FE1920, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\replay\reconstruction.py", line 131>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         2 (dict_events)
                GET_ITER
                CALL                     0
                LOAD_CONST               1 (None)
                CALL                     2
                STORE_FAST               3 (call_id)

 132            LOAD_GLOBAL              7 (next + NULL)
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C17FE13E0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\replay\reconstruction.py", line 132>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         2 (dict_events)
                GET_ITER
                CALL                     0
                LOAD_CONST               1 (None)
                CALL                     2
                STORE_FAST               4 (brokerage_id)

 134            BUILD_LIST               0
                STORE_FAST               5 (timeline)

 135            BUILD_LIST               0
                STORE_FAST               6 (turns)

 136            BUILD_MAP                0
                STORE_FAST               7 (extracted_fields)

 137            BUILD_LIST               0
                STORE_FAST               8 (objections)

 138            BUILD_LIST               0
                STORE_FAST               9 (bookings)

 139            BUILD_LIST               0
                STORE_FAST              10 (callbacks)

 140            BUILD_LIST               0
                STORE_FAST              11 (stages_seen)

 141            LOAD_GLOBAL              9 (set + NULL)
                CALL                     0
                STORE_FAST              12 (stages_seen_set)

 142            LOAD_GLOBAL              9 (set + NULL)
                CALL                     0
                STORE_FAST              13 (steps_present)

 144            LOAD_FAST_BORROW         0 (events)
                GET_ITER
        L8:     EXTENDED_ARG             4
                FOR_ITER              1163 (to L33)
                STORE_FAST              14 (ev)

 145            LOAD_GLOBAL              3 (isinstance + NULL)
                LOAD_FAST_BORROW        14 (ev)
                LOAD_GLOBAL              4 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN

 146            JUMP_BACKWARD           28 (to L8)

 147    L9:     LOAD_FAST_BORROW        14 (ev)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               4 ('event_type')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               5 ('')
       L10:     STORE_FAST              15 (et)

 148            LOAD_FAST_BORROW        14 (ev)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               6 ('created_at')
                CALL                     1
                STORE_FAST              16 (ts)

 149            LOAD_FAST_BORROW        14 (ev)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               7 ('actor')
                CALL                     1
                STORE_FAST              17 (actor)

 150            LOAD_FAST_BORROW        14 (ev)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               8 ('workflow_stage')
                CALL                     1
                STORE_FAST              18 (stage)

 151            LOAD_GLOBAL              3 (isinstance + NULL)
                LOAD_FAST_BORROW        14 (ev)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               9 ('payload')
                CALL                     1
                LOAD_GLOBAL              4 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L11)
                NOT_TAKEN
                LOAD_FAST_BORROW        14 (ev)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               9 ('payload')
                CALL                     1
                JUMP_FORWARD             1 (to L12)
       L11:     BUILD_MAP                0
       L12:     STORE_FAST              19 (payload)

 154            LOAD_FAST_BORROW        18 (stage)
                TO_BOOL
                POP_JUMP_IF_FALSE       42 (to L13)
                NOT_TAKEN
                LOAD_FAST_BORROW        18 (stage)
                LOAD_FAST_BORROW        12 (stages_seen_set)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       35 (to L13)
                NOT_TAKEN

 155            LOAD_FAST_BORROW        11 (stages_seen)
                LOAD_ATTR               13 (append + NULL|self)
                LOAD_FAST_BORROW        18 (stage)
                CALL                     1
                POP_TOP

 156            LOAD_FAST_BORROW        12 (stages_seen_set)
                LOAD_ATTR               15 (add + NULL|self)
                LOAD_FAST_BORROW        18 (stage)
                CALL                     1
                POP_TOP

 159   L13:     LOAD_FAST_BORROW         5 (timeline)
                LOAD_ATTR               13 (append + NULL|self)

 160            LOAD_CONST              10 ('ts')
                LOAD_FAST_BORROW        16 (ts)

 161            LOAD_CONST               4 ('event_type')
                LOAD_FAST_BORROW        15 (et)

 162            LOAD_CONST              11 ('summary')
                LOAD_GLOBAL             17 (_summary_for + NULL)
                LOAD_FAST_BORROW        14 (ev)
                CALL                     1

 159            BUILD_MAP                3
                CALL                     1
                POP_TOP

 166            LOAD_FAST_BORROW        15 (et)
                LOAD_CONST              12 ('lead.uttered')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE      113 (to L15)
                NOT_TAKEN

 167            LOAD_FAST_BORROW        14 (ev)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              13 ('input_text')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        28 (to L14)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW        19 (payload)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              14 ('excerpt')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               5 ('')
       L14:     STORE_FAST              20 (text)

 168            LOAD_FAST_BORROW         6 (turns)
                LOAD_ATTR               13 (append + NULL|self)

 169            LOAD_CONST              10 ('ts')
                LOAD_FAST_BORROW        16 (ts)

 170            LOAD_CONST              15 ('speaker')
                LOAD_CONST              16 ('lead')

 171            LOAD_CONST              17 ('text')
                LOAD_FAST_BORROW        20 (text)

 172            LOAD_CONST              18 ('state')
                LOAD_FAST_BORROW        14 (ev)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              18 ('state')
                CALL                     1

 173            LOAD_CONST              19 ('source_event_type')
                LOAD_FAST_BORROW        15 (et)

 168            BUILD_MAP                5
                CALL                     1
                POP_TOP

 175            LOAD_FAST_BORROW        13 (steps_present)
                LOAD_ATTR               15 (add + NULL|self)
                LOAD_CONST              20 ('lead_responded')
                CALL                     1
                POP_TOP
                JUMP_FORWARD           118 (to L17)

 176   L15:     LOAD_FAST_BORROW        15 (et)
                LOAD_CONST              21 ('pas.uttered')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE      112 (to L17)
                NOT_TAKEN

 177            LOAD_FAST_BORROW        14 (ev)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              22 ('output_text')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        28 (to L16)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW        19 (payload)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              14 ('excerpt')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L16)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               5 ('')
       L16:     STORE_FAST              20 (text)

 178            LOAD_FAST_BORROW         6 (turns)
                LOAD_ATTR               13 (append + NULL|self)

 179            LOAD_CONST              10 ('ts')
                LOAD_FAST_BORROW        16 (ts)

 180            LOAD_CONST              15 ('speaker')
                LOAD_CONST              23 ('pas')

 181            LOAD_CONST              17 ('text')
                LOAD_FAST_BORROW        20 (text)

 182            LOAD_CONST              18 ('state')
                LOAD_FAST_BORROW        14 (ev)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              18 ('state')
                CALL                     1

 183            LOAD_CONST              19 ('source_event_type')
                LOAD_FAST_BORROW        15 (et)

 178            BUILD_MAP                5
                CALL                     1
                POP_TOP

 185            LOAD_FAST_BORROW        13 (steps_present)
                LOAD_ATTR               15 (add + NULL|self)
                LOAD_CONST              24 ('pas_responded')
                CALL                     1
                POP_TOP

 188   L17:     LOAD_FAST_BORROW        15 (et)
                LOAD_CONST              25 ('lead.extracted')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE      145 (to L20)
                NOT_TAKEN

 189            LOAD_FAST_BORROW        14 (ev)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              26 ('extracted_field')
                CALL                     1
                STORE_FAST              21 (field)

 190            LOAD_FAST_BORROW        14 (ev)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              27 ('extracted_value')
                CALL                     1
                STORE_FAST              22 (value)

 191            LOAD_FAST_BORROW        21 (field)
                TO_BOOL
                POP_JUMP_IF_FALSE      103 (to L20)
                NOT_TAKEN

 193            LOAD_CONST              28 ('value')
                LOAD_FAST_BORROW        22 (value)

 194            LOAD_CONST              29 ('confidence')
                LOAD_FAST_BORROW        14 (ev)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              30 ('confidence_score')
                CALL                     1

 195            LOAD_CONST              10 ('ts')
                LOAD_FAST_BORROW        16 (ts)

 196            LOAD_CONST              19 ('source_event_type')
                LOAD_FAST_BORROW        15 (et)

 192            BUILD_MAP                4
                LOAD_FAST_BORROW         7 (extracted_fields)
                LOAD_FAST_BORROW        21 (field)
                STORE_SUBSCR

 198            LOAD_FAST_BORROW        21 (field)
                LOAD_CONST              31 ('intent')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       19 (to L18)
                NOT_TAKEN

 199            LOAD_FAST_BORROW        13 (steps_present)
                LOAD_ATTR               15 (add + NULL|self)
                LOAD_CONST              32 ('intent_captured')
                CALL                     1
                POP_TOP
                JUMP_FORWARD            49 (to L20)

 200   L18:     LOAD_FAST_BORROW        21 (field)
                LOAD_CONST              33 ('budget')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       19 (to L19)
                NOT_TAKEN

 201            LOAD_FAST_BORROW        13 (steps_present)
                LOAD_ATTR               15 (add + NULL|self)
                LOAD_CONST              34 ('budget_captured')
                CALL                     1
                POP_TOP
                JUMP_FORWARD            24 (to L20)

 202   L19:     LOAD_FAST_BORROW        21 (field)
                LOAD_CONST              35 ('timeline')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       18 (to L20)
                NOT_TAKEN

 203            LOAD_FAST_BORROW        13 (steps_present)
                LOAD_ATTR               15 (add + NULL|self)
                LOAD_CONST              36 ('timeline_captured')
                CALL                     1
                POP_TOP

 206   L20:     LOAD_FAST_BORROW        15 (et)
                LOAD_CONST              37 ('objection.detected')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE      108 (to L23)
                NOT_TAKEN

 207            LOAD_FAST                8 (objections)
                LOAD_ATTR               13 (append + NULL|self)

 208            LOAD_CONST              10 ('ts')
                LOAD_FAST               16 (ts)

 209            LOAD_CONST              38 ('category')
                LOAD_FAST_BORROW        19 (payload)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              38 ('category')
                CALL                     1

 210            LOAD_CONST              17 ('text')
                LOAD_FAST_BORROW        14 (ev)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              13 ('input_text')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L21)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW        19 (payload)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              17 ('text')
                CALL                     1

 211   L21:     LOAD_CONST               7 ('actor')
                LOAD_FAST               17 (actor)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L22)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              16 ('lead')

 207   L22:     BUILD_MAP                4
                CALL                     1
                POP_TOP

 213            LOAD_FAST_BORROW        13 (steps_present)
                LOAD_ATTR               15 (add + NULL|self)
                LOAD_CONST              20 ('lead_responded')
                CALL                     1
                POP_TOP

 216   L23:     LOAD_FAST_BORROW        15 (et)
                LOAD_CONST              72 (('booking.attempted', 'booking.confirmed', 'booking.failed'))
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE      114 (to L24)
                NOT_TAKEN

 217            LOAD_FAST_BORROW        15 (et)
                LOAD_ATTR               19 (split + NULL|self)
                LOAD_CONST              39 ('.')
                CALL                     1
                LOAD_CONST              73 (-1)
                BINARY_OP               26 ([])
                STORE_FAST              23 (status)

 218            LOAD_FAST_BORROW         9 (bookings)
                LOAD_ATTR               13 (append + NULL|self)

 219            LOAD_CONST              10 ('ts')
                LOAD_FAST_BORROW        16 (ts)

 220            LOAD_CONST              40 ('status')
                LOAD_FAST_BORROW        23 (status)

 221            LOAD_CONST              41 ('slot')
                LOAD_FAST_BORROW        19 (payload)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              41 ('slot')
                CALL                     1

 222            LOAD_CONST              42 ('booking_id')
                LOAD_FAST_BORROW        19 (payload)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              42 ('booking_id')
                CALL                     1

 223            LOAD_CONST              43 ('error')
                LOAD_FAST_BORROW        19 (payload)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              43 ('error')
                CALL                     1

 218            BUILD_MAP                5
                CALL                     1
                POP_TOP

 225            LOAD_FAST_BORROW        13 (steps_present)
                LOAD_ATTR               15 (add + NULL|self)
                LOAD_CONST              44 ('booking_or_callback')
                CALL                     1
                POP_TOP

 228   L24:     LOAD_FAST_BORROW        15 (et)
                LOAD_CONST              45 ('callback.requested')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE      103 (to L26)
                NOT_TAKEN

 229            LOAD_FAST               10 (callbacks)
                LOAD_ATTR               13 (append + NULL|self)

 230            LOAD_CONST              10 ('ts')
                LOAD_FAST               16 (ts)

 231            LOAD_CONST              46 ('kind')
                LOAD_CONST              47 ('requested')

 232            LOAD_CONST              17 ('text')
                LOAD_FAST_BORROW        14 (ev)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              13 ('input_text')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L25)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW        19 (payload)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              48 ('trigger_excerpt')
                CALL                     1

 233   L25:     LOAD_CONST              49 ('normalized_time')
                LOAD_CONST               1 (None)

 234            LOAD_CONST              50 ('confirmed')
                LOAD_CONST               1 (None)

 229            BUILD_MAP                5
                CALL                     1
                POP_TOP

 236            LOAD_FAST_BORROW        13 (steps_present)
                LOAD_ATTR               15 (add + NULL|self)
                LOAD_CONST              44 ('booking_or_callback')
                CALL                     1
                POP_TOP

 237            LOAD_FAST_BORROW        13 (steps_present)
                LOAD_ATTR               15 (add + NULL|self)
                LOAD_CONST              20 ('lead_responded')
                CALL                     1
                POP_TOP
                JUMP_FORWARD            96 (to L27)

 238   L26:     LOAD_FAST_BORROW        15 (et)
                LOAD_CONST              51 ('call.ended_with_callback')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       90 (to L27)
                NOT_TAKEN

 239            LOAD_FAST_BORROW        10 (callbacks)
                LOAD_ATTR               13 (append + NULL|self)

 240            LOAD_CONST              10 ('ts')
                LOAD_FAST_BORROW        16 (ts)

 241            LOAD_CONST              46 ('kind')
                LOAD_CONST              52 ('finalized')

 242            LOAD_CONST              17 ('text')
                LOAD_FAST_BORROW        19 (payload)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              53 ('callback_reason_excerpt')
                CALL                     1

 243            LOAD_CONST              49 ('normalized_time')
                LOAD_FAST_BORROW        19 (payload)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              54 ('preferred_time_normalized')
                CALL                     1

 244            LOAD_CONST              50 ('confirmed')
                LOAD_FAST_BORROW        19 (payload)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              55 ('callback_confirmed')
                CALL                     1

 239            BUILD_MAP                5
                CALL                     1
                POP_TOP

 246            LOAD_FAST_BORROW        13 (steps_present)
                LOAD_ATTR               15 (add + NULL|self)
                LOAD_CONST              44 ('booking_or_callback')
                CALL                     1
                POP_TOP

 249   L27:     LOAD_FAST_BORROW        15 (et)
                LOAD_CONST              56 ('call.started')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_TRUE         8 (to L28)
                NOT_TAKEN
                LOAD_FAST_BORROW        18 (stage)
                LOAD_CONST              57 ('lead_received')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       18 (to L29)
                NOT_TAKEN

 250   L28:     LOAD_FAST_BORROW        13 (steps_present)
                LOAD_ATTR               15 (add + NULL|self)
                LOAD_CONST              57 ('lead_received')
                CALL                     1
                POP_TOP

 255   L29:     LOAD_FAST_BORROW        15 (et)
                LOAD_CONST              58 ('state.transition')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       29 (to L31)
                NOT_TAKEN
                LOAD_FAST_BORROW        17 (actor)
                LOAD_CONST              23 ('pas')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_TRUE         5 (to L30)
                NOT_TAKEN
                LOAD_FAST_BORROW        17 (actor)
                POP_JUMP_IF_NOT_NONE    18 (to L31)
                NOT_TAKEN

 256   L30:     LOAD_FAST_BORROW        13 (steps_present)
                LOAD_ATTR               15 (add + NULL|self)
                LOAD_CONST              24 ('pas_responded')
                CALL                     1
                POP_TOP

 259   L31:     LOAD_FAST_BORROW        15 (et)
                LOAD_CONST              74 (('call.ended', 'call.ended_with_callback', 'call.failed'))
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_TRUE         4 (to L32)
                NOT_TAKEN
                EXTENDED_ARG             4
                JUMP_BACKWARD         1146 (to L8)

 260   L32:     LOAD_FAST_BORROW        13 (steps_present)
                LOAD_ATTR               15 (add + NULL|self)
                LOAD_CONST              59 ('completed')
                CALL                     1
                POP_TOP
                EXTENDED_ARG             4
                JUMP_BACKWARD         1166 (to L8)

 144   L33:     END_FOR
                POP_ITER

 263            BUILD_SET                0
                LOAD_CONST              75 (frozenset({'timeline_captured', 'intent_captured', 'budget_captured'}))
                SET_UPDATE               1
                LOAD_FAST_BORROW        13 (steps_present)
                COMPARE_OP              58 (bool(<=))
                POP_JUMP_IF_FALSE       18 (to L34)
                NOT_TAKEN

 264            LOAD_FAST_BORROW        13 (steps_present)
                LOAD_ATTR               15 (add + NULL|self)
                LOAD_CONST              60 ('qualified')
                CALL                     1
                POP_TOP

 266   L34:     LOAD_GLOBAL             21 (_terminal_outcome + NULL)
                LOAD_FAST_BORROW         0 (events)
                CALL                     1
                STORE_FAST              24 (final_outcome)

 267            LOAD_GLOBAL             22 (_LIFECYCLE_STEPS)
                GET_ITER
                LOAD_FAST_AND_CLEAR     25 (s)
                SWAP                     2
       L35:     BUILD_LIST               0
                SWAP                     2
       L36:     FOR_ITER                14 (to L39)
                STORE_FAST              25 (s)
                LOAD_FAST_BORROW        25 (s)
                LOAD_FAST_BORROW        13 (steps_present)
                CONTAINS_OP              1 (not in)
       L37:     POP_JUMP_IF_TRUE         3 (to L38)
                NOT_TAKEN
                JUMP_BACKWARD           12 (to L36)
       L38:     LOAD_FAST_BORROW        25 (s)
                LIST_APPEND              2
                JUMP_BACKWARD           16 (to L36)
       L39:     END_FOR
                POP_ITER
       L40:     STORE_FAST              26 (missing)
                STORE_FAST              25 (s)

 270            LOAD_CONST              61 ('call_id')
                LOAD_FAST_BORROW         3 (call_id)

 271            LOAD_CONST              62 ('brokerage_id')
                LOAD_FAST_BORROW         4 (brokerage_id)

 272            LOAD_CONST              35 ('timeline')
                LOAD_FAST_BORROW         5 (timeline)

 273            LOAD_CONST              63 ('turns')
                LOAD_FAST_BORROW         6 (turns)

 274            LOAD_CONST              64 ('extracted_fields')
                LOAD_FAST_BORROW         7 (extracted_fields)

 275            LOAD_CONST              65 ('objections')
                LOAD_FAST_BORROW         8 (objections)

 276            LOAD_CONST              66 ('bookings')
                LOAD_FAST_BORROW         9 (bookings)

 277            LOAD_CONST              67 ('callbacks')
                LOAD_FAST_BORROW        10 (callbacks)

 278            LOAD_CONST              68 ('final_outcome')
                LOAD_FAST_BORROW        24 (final_outcome)

 279            LOAD_CONST              69 ('workflow_stages_seen')
                LOAD_FAST_BORROW        11 (stages_seen)

 280            LOAD_CONST              70 ('missing_lifecycle_steps')
                LOAD_FAST_BORROW        26 (missing)

 281            LOAD_CONST              71 ('events_count')
                LOAD_GLOBAL             25 (len + NULL)
                LOAD_FAST_BORROW         0 (events)
                CALL                     1

 269            BUILD_MAP               12
                RETURN_VALUE

  --   L41:     SWAP                     2
                POP_TOP

 130            SWAP                     2
                STORE_FAST               1 (e)
                RERAISE                  0

  --   L42:     SWAP                     2
                POP_TOP

 267            SWAP                     2
                STORE_FAST              25 (s)
                RERAISE                  0
ExceptionTable:
  L2 to L4 -> L41 [2]
  L5 to L7 -> L41 [2]
  L35 to L37 -> L42 [2]
  L38 to L40 -> L42 [2]

Disassembly of <code object <genexpr> at 0x0000018C17FE1920, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\replay\reconstruction.py", line 131>:
 131           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                46 (to L5)
               STORE_FAST_LOAD_FAST    17 (e, e)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('call_id')
               CALL                     1
               TO_BOOL
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           27 (to L2)
       L4:     LOAD_FAST_BORROW         1 (e)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('call_id')
               CALL                     1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           48 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C17FE13E0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\replay\reconstruction.py", line 132>:
 132           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                46 (to L5)
               STORE_FAST_LOAD_FAST    17 (e, e)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('brokerage_id')
               CALL                     1
               TO_BOOL
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           27 (to L2)
       L4:     LOAD_FAST_BORROW         1 (e)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('brokerage_id')
               CALL                     1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           48 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025530, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\replay\reconstruction.py", line 285>:
285           RESUME                   0
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

Disassembly of <code object _empty_replay at 0x0000018C18053E10, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\replay\reconstruction.py", line 285>:
285           RESUME                   0

287           LOAD_CONST               0 ('call_id')
              LOAD_FAST_BORROW         0 (call_id)

288           LOAD_CONST               1 ('brokerage_id')
              LOAD_FAST_BORROW         1 (brokerage_id)

289           LOAD_CONST               2 ('timeline')
              BUILD_LIST               0

290           LOAD_CONST               3 ('turns')
              BUILD_LIST               0

291           LOAD_CONST               4 ('extracted_fields')
              BUILD_MAP                0

292           LOAD_CONST               5 ('objections')
              BUILD_LIST               0

293           LOAD_CONST               6 ('bookings')
              BUILD_LIST               0

294           LOAD_CONST               7 ('callbacks')
              BUILD_LIST               0

295           LOAD_CONST               8 ('final_outcome')
              LOAD_CONST               9 (None)

296           LOAD_CONST              10 ('workflow_stages_seen')
              BUILD_LIST               0

297           LOAD_CONST              11 ('missing_lifecycle_steps')
              LOAD_GLOBAL              1 (list + NULL)
              LOAD_GLOBAL              2 (_LIFECYCLE_STEPS)
              CALL                     1

298           LOAD_CONST              12 ('events_count')
              LOAD_SMALL_INT           0

286           BUILD_MAP               12
              RETURN_VALUE
```
