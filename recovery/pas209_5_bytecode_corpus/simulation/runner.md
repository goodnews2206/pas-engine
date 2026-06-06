# simulation/runner

- **pyc:** `app\services\simulation\__pycache__\runner.cpython-314.pyc`
- **expected source path (absent):** `app\services\simulation/runner.py`
- **co_filename (from bytecode):** `app\services\simulation\runner.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** simulation

## Module docstring

```
PAS142 — Scenario runner.

Drives a SimulationScenario through the real PASEngine while:
  - capturing every emitted event into an in-memory list
  - stubbing book_appointment + handle_objection so no external
    APIs (Cal.com, Anthropic) are required
  - emitting synthetic call.started / call.ended events to mirror the
    /simulate-call route's lifecycle (which lives outside PASEngine)
  - feeding the captured event stream through PAS141's normalizer +
    reconstructor + evaluator

run_scenario is intentionally synchronous; the engine's async parts
are wrapped in asyncio.run internally so callers (CLI, tests) don't
have to manage an event loop.
```

## Imports

`ESCALATION_INJECTION_TEXT`, `Optional`, `ScenarioStep`, `SimulationScenario`, `TRIGGER_THRESHOLD`, `advance_behavior_state`, `app.engine`, `app.services.replay.evaluator`, `app.services.replay.event_reader`, `app.services.replay.reconstruction`, `asyncio`, `behavior`, `compute_behavioral_modifiers`, `datetime`, `evaluate_reconstruction`, `get_personality`, `normalize_event`, `reconstruct_call`, `scenarios`, `state_machine`, `time`, `timezone`, `typing`, `uuid`

## Classes

_none_

## Functions / methods

`__annotate__`, `_clamp01`, `_classify_event_for_behavior`, `_error_result`, `_fake_book_appointment_factory`, `_fake_handle_objection_factory`, `_make_call_sid`, `_now_iso`, `run_scenario`

## Env-key candidates

`BOOKING`

## String constants (redacted where noted)

- "\nPAS142 — Scenario runner.\n\nDrives a SimulationScenario through the real PASEngine while:\n  - capturing every emitted event into an in-memory list\n  - stubbing book_appointment + handle_objection so no external\n    APIs (Cal.com, Anthropic) are required\n  - emitting synthetic call.started / call.ended events to mirror the\n    /simulate-call route's lifecycle (which lives outside PASEngine)\n  - feeding the captured event stream through PAS141's normalizer +\n    reconstructor + evaluator\n\nrun_scenario is intentionally synchronous; the engine's async parts\nare wrapped in asyncio.run internally so callers (CLI, tests) don't\nhave to manage an event loop.\n"
- 'brokerage_id'
- 'demo'
- 'brokerage_overrides'
- 'strategy_id'
- 'scenario_id'
- 'return'
- "Use the SIM- prefix so source_from_call_sid resolves to 'simulated'."
- 'SIM-'
- 'Deterministic stand-in for app.services.llm.claude_client.handle_objection.\nAlways returns the same short rebuttal so test outputs are stable.'
- 'I understand. Could we still try a quick chat?'
- 'state'
- '\nDeterministic stand-in for booking.calcom_client.book_appointment.\n\nPAS143B — accepts a *mutable* state dict (`{"should_succeed": bool}`)\nso the runner can flip the booking decision mid-scenario when\nbehavioural divergence triggers a refusal at booking. PAS142\ncallers that don\'t touch behaviour see identical behaviour.\n'
- 'should_succeed'
- 'success'
- 'slot'
- '2026-05-12T10:00:00+00:00'
- 'booking_id'
- 'sim-booking-1'
- 'error'
- 'simulated personality-driven decline'
- 'captured_events'
- 'idx_at_start'
- '\nReturn a single representative event type for the turn just processed.\nWalks events appended since `idx_at_start` and prefers signals in\ndescending behavioural-impact order: objection > callback > extracted >\nbooking > lead.uttered (default).\n'
- 'event_type'
- 'lead.uttered'
- 'scenario'
- "\nExecute one scenario end-to-end. Returns a dict with:\n  scenario_id, scenario_title, scenario_category, scenario_tags,\n  expected_outcome, actual_outcome, passed,\n  events_count, transcript, reconstruction, evaluation, duration_ms,\n  personality_id, personality_name, final_behavior_state,\n  trust_score, frustration_score, divergence_triggered,\n  divergence_actions.\n\nPure in-process; never raises (errors are captured in the result).\n\nPAS143A — `brokerage_overrides` (optional dict) is shallow-merged\ninto the brokerage config before PASEngine instantiation. Unknown\nkeys are forwarded verbatim — PASEngine ignores anything it\ndoesn't read.\n\nPAS143B — when both `strategy_id` and `scenario.personality_id`\nare supplied, the runner consults app/services/simulation/behavior.py\nto track conversational state (trust / frustration / behavior_state)\nand may take *deterministic* divergent actions:\n  - drop the lead early (skip remaining steps),\n  - inject a hostile objection that terminates the call,\n  - flip the in-flight booking stub to fail.\nAll three are deterministic functions of (personality, strategy,\nprogression) — no randomness. When either input is missing the\nrunner is byte-equivalent to PAS142, preserving every existing test.\n"
- 'scenario was None'
- 'neutral'
- 'call.started'
- 'call'
- 'call_logger'
- 'source'
- 'simulated'
- 'system'
- 'lead_received'
- 'name'
- 'Simulated Brokerage'
- 'pas'
- 'call.ended'
- 'simulate'
- 'value'
- 'outcome'
- 'duration_seconds'
- 'final_state'
- 'states_visited'
- 'is_outbound'
- 'objections_detected'
- 'completed'
- 'transferred'
- 'scenario_title'
- 'scenario_category'
- 'scenario_tags'
- 'call_sid'
- 'expected_outcome'
- 'actual_outcome'
- 'passed'
- 'events_count'
- 'transcript'
- 'reconstruction'
- 'evaluation'
- 'duration_ms'
- 'personality_id'
- 'personality_name'
- 'final_behavior_state'
- 'trust_score'
- 'frustration_score'
- 'divergence_triggered'
- 'divergence_actions'
- 'created_at'
- 'lead'
- 'drop_risk'
- 'turn'
- 'action'
- 'lead_dropped'
- 'dropping'
- 'booking_failure_risk'
- 'BOOKING'
- 'booking_will_fail'
- 'risk'
- 'escalation_risk'
- 'lead_escalated'
- 'next_state'
- 'trust_delta'
- 'recovery_delta'
- 'frustration_delta'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ("\nPAS142 — Scenario runner.\n\nDrives a SimulationScenario through the real PASEngine while:\n  - capturing every emitted event into an in-memory list\n  - stubbing book_appointment + handle_objection so no external\n    APIs (Cal.com, Anthropic) are required\n  - emitting synthetic call.started / call.ended events to mirror the\n    /simulate-call route's lifecycle (which lives outside PASEngine)\n  - feeding the captured event stream through PAS141's normalizer +\n    reconstructor + evaluator\n\nrun_scenario is intentionally synchronous; the engine's async parts\nare wrapped in asyncio.run internally so callers (CLI, tests) don't\nhave to manage an event loop.\n")
              STORE_NAME               0 (__doc__)

 18           LOAD_SMALL_INT           0
              LOAD_CONST               1 (None)
              IMPORT_NAME              1 (asyncio)
              STORE_NAME               1 (asyncio)

 19           LOAD_SMALL_INT           0
              LOAD_CONST               1 (None)
              IMPORT_NAME              2 (time)
              STORE_NAME               2 (time)

 20           LOAD_SMALL_INT           0
              LOAD_CONST               1 (None)
              IMPORT_NAME              3 (uuid)
              STORE_NAME               3 (uuid)

 21           LOAD_SMALL_INT           0
              LOAD_CONST               2 (('datetime', 'timezone'))
              IMPORT_NAME              4 (datetime)
              IMPORT_FROM              4 (datetime)
              STORE_NAME               4 (datetime)
              IMPORT_FROM              5 (timezone)
              STORE_NAME               5 (timezone)
              POP_TOP

 22           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('Optional',))
              IMPORT_NAME              6 (typing)
              IMPORT_FROM              7 (Optional)
              STORE_NAME               7 (Optional)
              POP_TOP

 24           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('state_machine',))
              IMPORT_NAME              8 (app.engine)
              IMPORT_FROM              9 (state_machine)
              STORE_NAME              10 (sm)
              POP_TOP

 25           LOAD_SMALL_INT           0
              LOAD_CONST               5 (('normalize_event',))
              IMPORT_NAME             11 (app.services.replay.event_reader)
              IMPORT_FROM             12 (normalize_event)
              STORE_NAME              12 (normalize_event)
              POP_TOP

 26           LOAD_SMALL_INT           0
              LOAD_CONST               6 (('reconstruct_call',))
              IMPORT_NAME             13 (app.services.replay.reconstruction)
              IMPORT_FROM             14 (reconstruct_call)
              STORE_NAME              14 (reconstruct_call)
              POP_TOP

 27           LOAD_SMALL_INT           0
              LOAD_CONST               7 (('evaluate_reconstruction',))
              IMPORT_NAME             15 (app.services.replay.evaluator)
              IMPORT_FROM             16 (evaluate_reconstruction)
              STORE_NAME              16 (evaluate_reconstruction)
              POP_TOP

 29           LOAD_SMALL_INT           1
              LOAD_CONST               8 (('ESCALATION_INJECTION_TEXT', 'TRIGGER_THRESHOLD', 'advance_behavior_state', 'compute_behavioral_modifiers', 'get_personality'))
              IMPORT_NAME             17 (behavior)
              IMPORT_FROM             18 (ESCALATION_INJECTION_TEXT)
              STORE_NAME              18 (ESCALATION_INJECTION_TEXT)
              IMPORT_FROM             19 (TRIGGER_THRESHOLD)
              STORE_NAME              19 (TRIGGER_THRESHOLD)
              IMPORT_FROM             20 (advance_behavior_state)
              STORE_NAME              20 (advance_behavior_state)
              IMPORT_FROM             21 (compute_behavioral_modifiers)
              STORE_NAME              21 (compute_behavioral_modifiers)
              IMPORT_FROM             22 (get_personality)
              STORE_NAME              22 (get_personality)
              POP_TOP

 36           LOAD_SMALL_INT           1
              LOAD_CONST               9 (('SimulationScenario', 'ScenarioStep'))
              IMPORT_NAME             23 (scenarios)
              IMPORT_FROM             24 (SimulationScenario)
              STORE_NAME              24 (SimulationScenario)
              IMPORT_FROM             25 (ScenarioStep)
              STORE_NAME              25 (ScenarioStep)
              POP_TOP

 41           LOAD_CONST              10 (<code object __annotate__ at 0x0000018C18025F30, file "app\services\simulation\runner.py", line 41>)
              MAKE_FUNCTION
              LOAD_CONST              11 (<code object _make_call_sid at 0x0000018C17F96420, file "app\services\simulation\runner.py", line 41>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              26 (_make_call_sid)

 47           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C18026630, file "app\services\simulation\runner.py", line 47>)
              MAKE_FUNCTION
              LOAD_CONST              13 (<code object _now_iso at 0x0000018C18038A30, file "app\services\simulation\runner.py", line 47>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              27 (_now_iso)

 51           LOAD_CONST              14 (<code object _fake_handle_objection_factory at 0x0000018C18068B90, file "app\services\simulation\runner.py", line 51>)
              MAKE_FUNCTION
              STORE_NAME              28 (_fake_handle_objection_factory)

 59           LOAD_CONST              15 (<code object __annotate__ at 0x0000018C18025730, file "app\services\simulation\runner.py", line 59>)
              MAKE_FUNCTION
              LOAD_CONST              16 (<code object _fake_book_appointment_factory at 0x0000018C17FA3A50, file "app\services\simulation\runner.py", line 59>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              29 (_fake_book_appointment_factory)

 79           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C18025D30, file "app\services\simulation\runner.py", line 79>)
              MAKE_FUNCTION
              LOAD_CONST              18 (<code object _clamp01 at 0x0000018C18025230, file "app\services\simulation\runner.py", line 79>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              30 (_clamp01)

 87           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C18128030, file "app\services\simulation\runner.py", line 87>)
              MAKE_FUNCTION
              LOAD_CONST              20 (<code object _classify_event_for_behavior at 0x0000018C17FE1530, file "app\services\simulation\runner.py", line 87>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              31 (_classify_event_for_behavior)

111           LOAD_CONST              21 ('brokerage_id')

114           LOAD_CONST              22 ('demo')

111           LOAD_CONST              23 ('brokerage_overrides')

115           LOAD_CONST               1 (None)

111           LOAD_CONST              24 ('strategy_id')

116           LOAD_CONST               1 (None)

111           BUILD_MAP                3
              LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FE1290, file "app\services\simulation\runner.py", line 111>)
              MAKE_FUNCTION
              LOAD_CONST              26 (<code object run_scenario at 0x0000018C17EAADE0, file "app\services\simulation\runner.py", line 111>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              32 (run_scenario)

400           LOAD_CONST              27 (<code object __annotate__ at 0x0000018C18025C30, file "app\services\simulation\runner.py", line 400>)
              MAKE_FUNCTION
              LOAD_CONST              28 (<code object _error_result at 0x0000018C18060F60, file "app\services\simulation\runner.py", line 400>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              33 (_error_result)
              LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025F30, file "app\services\simulation\runner.py", line 41>:
 41           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('scenario_id')
              LOAD_GLOBAL              0 (str)
              LOAD_CONST               2 ('return')
              LOAD_GLOBAL              0 (str)
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _make_call_sid at 0x0000018C17F96420, file "app\services\simulation\runner.py", line 41>:
 41           RESUME                   0

 43           LOAD_GLOBAL              0 (uuid)
              LOAD_ATTR                2 (uuid4)
              PUSH_NULL
              CALL                     0
              LOAD_ATTR                4 (hex)
              LOAD_CONST               1 (slice(None, 8, None))
              BINARY_OP               26 ([])
              LOAD_ATTR                7 (upper + NULL|self)
              CALL                     0
              STORE_FAST               1 (short)

 44           LOAD_CONST               2 ('SIM-')
              LOAD_FAST_BORROW         0 (scenario_id)
              LOAD_ATTR                7 (upper + NULL|self)
              CALL                     0
              FORMAT_SIMPLE
              LOAD_CONST               3 ('-')
              LOAD_FAST_BORROW         1 (short)
              FORMAT_SIMPLE
              BUILD_STRING             4
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026630, file "app\services\simulation\runner.py", line 47>:
 47           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_GLOBAL              0 (str)
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _now_iso at 0x0000018C18038A30, file "app\services\simulation\runner.py", line 47>:
 47           RESUME                   0

 48           LOAD_GLOBAL              0 (datetime)
              LOAD_ATTR                2 (now)
              PUSH_NULL
              LOAD_GLOBAL              4 (timezone)
              LOAD_ATTR                6 (utc)
              CALL                     1
              LOAD_ATTR                9 (isoformat + NULL|self)
              CALL                     0
              RETURN_VALUE

Disassembly of <code object _fake_handle_objection_factory at 0x0000018C18068B90, file "app\services\simulation\runner.py", line 51>:
 51           RESUME                   0

 54           LOAD_CONST               1 (<code object _fake at 0x0000018C18068C70, file "app\services\simulation\runner.py", line 54>)
              MAKE_FUNCTION
              STORE_FAST               0 (_fake)

 56           LOAD_FAST_BORROW         0 (_fake)
              RETURN_VALUE

Disassembly of <code object _fake at 0x0000018C18068C70, file "app\services\simulation\runner.py", line 54>:
  54           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0

  55           LOAD_CONST               0 ('I understand. Could we still try a quick chat?')
               RETURN_VALUE

  --   L2:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L2 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025730, file "app\services\simulation\runner.py", line 59>:
 59           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('state')
              LOAD_GLOBAL              0 (dict)
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _fake_book_appointment_factory at 0x0000018C17FA3A50, file "app\services\simulation\runner.py", line 59>:
  --           MAKE_CELL                0 (state)

  59           RESUME                   0

  68           LOAD_FAST_BORROW         0 (state)
               BUILD_TUPLE              1
               LOAD_CONST               1 (<code object _fake at 0x0000018C1802C750, file "app\services\simulation\runner.py", line 68>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               STORE_FAST               1 (_fake)

  76           LOAD_FAST_BORROW         1 (_fake)
               RETURN_VALUE

Disassembly of <code object _fake at 0x0000018C1802C750, file "app\services\simulation\runner.py", line 68>:
  --           COPY_FREE_VARS           1

  68           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0

  69           LOAD_DEREF               1 (state)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('should_succeed')
               LOAD_CONST               1 (True)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE        9 (to L2)
               NOT_TAKEN

  71           LOAD_CONST               2 ('success')
               LOAD_CONST               1 (True)

  72           LOAD_CONST               3 ('slot')
               LOAD_CONST               4 ('2026-05-12T10:00:00+00:00')

  73           LOAD_CONST               5 ('booking_id')
               LOAD_CONST               6 ('sim-booking-1')

  70           BUILD_MAP                3
               RETURN_VALUE

  75   L2:     LOAD_CONST               2 ('success')
               LOAD_CONST               7 (False)
               LOAD_CONST               8 ('error')
               LOAD_CONST               9 ('simulated personality-driven decline')
               BUILD_MAP                2
               RETURN_VALUE

  --   L3:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L3 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025D30, file "app\services\simulation\runner.py", line 79>:
 79           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('v')
              LOAD_GLOBAL              0 (float)
              LOAD_CONST               2 ('return')
              LOAD_GLOBAL              0 (float)
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _clamp01 at 0x0000018C18025230, file "app\services\simulation\runner.py", line 79>:
 79           RESUME                   0

 80           LOAD_FAST_BORROW         0 (v)
              LOAD_CONST               0 (0.0)
              COMPARE_OP              18 (bool(<))
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN

 81           LOAD_CONST               0 (0.0)
              RETURN_VALUE

 82   L1:     LOAD_FAST_BORROW         0 (v)
              LOAD_CONST               1 (1.0)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

 83           LOAD_CONST               1 (1.0)
              RETURN_VALUE

 84   L2:     LOAD_FAST_BORROW         0 (v)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18128030, file "app\services\simulation\runner.py", line 87>:
 87           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('captured_events')
              LOAD_GLOBAL              0 (list)
              LOAD_CONST               2 ('idx_at_start')
              LOAD_GLOBAL              2 (int)
              LOAD_CONST               3 ('return')
              LOAD_GLOBAL              4 (str)
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _classify_event_for_behavior at 0x0000018C17FE1530, file "app\services\simulation\runner.py", line 87>:
  87           RESUME                   0

  94           LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (captured_events, idx_at_start)
               LOAD_CONST               1 (None)
               BINARY_SLICE
               STORE_FAST               2 (new)

  95           LOAD_FAST_BORROW         2 (new)
               GET_ITER
               LOAD_FAST_AND_CLEAR      3 (e)
               SWAP                     2
       L1:     BUILD_LIST               0
               SWAP                     2
       L2:     FOR_ITER                19 (to L3)
               STORE_FAST_LOAD_FAST    51 (e, e)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               2 ('event_type')
               CALL                     1
               LIST_APPEND              2
               JUMP_BACKWARD           21 (to L2)
       L3:     END_FOR
               POP_ITER
       L4:     STORE_FAST               4 (types)
               STORE_FAST               3 (e)

  96           LOAD_CONST               4 (('objection.detected', 'callback.requested', 'lead.extracted', 'booking.attempted', 'booking.confirmed', 'booking.failed'))
               GET_ITER
       L5:     FOR_ITER                13 (to L7)
               STORE_FAST               5 (preferred)

 104           LOAD_FAST_BORROW_LOAD_FAST_BORROW 84 (preferred, types)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L6)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L5)

 105   L6:     LOAD_FAST_BORROW         5 (preferred)
               SWAP                     2
               POP_TOP
               RETURN_VALUE

  96   L7:     END_FOR
               POP_ITER

 106           LOAD_CONST               3 ('lead.uttered')
               RETURN_VALUE

  --   L8:     SWAP                     2
               POP_TOP

  95           SWAP                     2
               STORE_FAST               3 (e)
               RERAISE                  0
ExceptionTable:
  L1 to L4 -> L8 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FE1290, file "app\services\simulation\runner.py", line 111>:
111           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('scenario')

112           LOAD_GLOBAL              0 (SimulationScenario)

111           LOAD_CONST               2 ('brokerage_id')

114           LOAD_GLOBAL              2 (str)

111           LOAD_CONST               3 ('brokerage_overrides')

115           LOAD_GLOBAL              4 (Optional)
              LOAD_GLOBAL              6 (dict)
              BINARY_OP               26 ([])

111           LOAD_CONST               4 ('strategy_id')

116           LOAD_GLOBAL              4 (Optional)
              LOAD_GLOBAL              2 (str)
              BINARY_OP               26 ([])

111           LOAD_CONST               5 ('return')

117           LOAD_GLOBAL              6 (dict)

111           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object run_scenario at 0x0000018C17EAADE0, file "app\services\simulation\runner.py", line 111>:
  --            MAKE_CELL                0 (scenario)
                MAKE_CELL                3 (strategy_id)
                MAKE_CELL               23 (behavior_state)
                MAKE_CELL               24 (behaviour_active)
                MAKE_CELL               25 (booking_state)
                MAKE_CELL               26 (divergence_actions)
                MAKE_CELL               27 (divergence_triggered)
                MAKE_CELL               28 (engine)
                MAKE_CELL               29 (events)
                MAKE_CELL               30 (frustration_score)
                MAKE_CELL               31 (personality)
                MAKE_CELL               32 (trust_score)

 111            RESUME                   0

 145            LOAD_DEREF               0 (scenario)
                POP_JUMP_IF_NOT_NONE    14 (to L1)
                NOT_TAKEN

 146            LOAD_GLOBAL              1 (_error_result + NULL)
                LOAD_CONST               1 (None)
                LOAD_FAST_BORROW         1 (brokerage_id)
                LOAD_CONST               2 ('scenario was None')
                CALL                     3
                RETURN_VALUE

 148    L1:     LOAD_GLOBAL              2 (time)
                LOAD_ATTR                4 (perf_counter)
                PUSH_NULL
                CALL                     0
                STORE_FAST               4 (started)

 149            LOAD_GLOBAL              7 (_make_call_sid + NULL)
                LOAD_DEREF               0 (scenario)
                LOAD_ATTR                8 (id)
                CALL                     1
                STORE_FAST               5 (call_sid)

 150            BUILD_LIST               0
                STORE_DEREF             29 (events)

 153            LOAD_GLOBAL             11 (get_personality + NULL)
                LOAD_DEREF               0 (scenario)
                LOAD_ATTR               12 (personality_id)
                CALL                     1
                STORE_DEREF             31 (personality)

 154            LOAD_DEREF              31 (personality)
                LOAD_CONST               1 (None)
                IS_OP                    1 (is not)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       12 (to L2)
                NOT_TAKEN
                POP_TOP
                LOAD_GLOBAL             15 (bool + NULL)
                LOAD_DEREF               3 (strategy_id)
                CALL                     1
        L2:     STORE_DEREF             24 (behaviour_active)

 155            LOAD_CONST               3 ('neutral')
                STORE_DEREF             23 (behavior_state)

 156            LOAD_CONST               4 (0.5)
                STORE_DEREF             32 (trust_score)

 157            LOAD_CONST               5 (0.0)
                STORE_DEREF             30 (frustration_score)

 158            LOAD_CONST               6 (False)
                STORE_DEREF             27 (divergence_triggered)

 159            BUILD_LIST               0
                STORE_DEREF             26 (divergence_actions)

 164            LOAD_FAST_BORROW        29 (events)
                BUILD_TUPLE              1
                LOAD_CONST               7 (<code object _capture at 0x0000018C17FE1A70, file "app\services\simulation\runner.py", line 164>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                STORE_FAST               6 (_capture)

 172            LOAD_GLOBAL             16 (sm)
                LOAD_ATTR               18 (log_event_bg)
                STORE_FAST               7 (original_log_event_bg)

 173            LOAD_GLOBAL             16 (sm)
                LOAD_ATTR               20 (book_appointment)
                STORE_FAST               8 (original_book_appointment)

 174            LOAD_GLOBAL             16 (sm)
                LOAD_ATTR               22 (handle_objection)
                STORE_FAST               9 (original_handle_objection)

 179            LOAD_CONST               8 ('should_succeed')
                LOAD_DEREF               0 (scenario)
                LOAD_ATTR               24 (booking_should_succeed)
                BUILD_MAP                1
                STORE_DEREF             25 (booking_state)

 180            LOAD_FAST_BORROW         6 (_capture)
                LOAD_GLOBAL             16 (sm)
                STORE_ATTR               9 (log_event_bg)

 181            LOAD_GLOBAL             27 (_fake_book_appointment_factory + NULL)
                LOAD_DEREF              25 (booking_state)
                CALL                     1
                LOAD_GLOBAL             16 (sm)
                STORE_ATTR              10 (book_appointment)

 182            LOAD_GLOBAL             29 (_fake_handle_objection_factory + NULL)
                CALL                     0
                LOAD_GLOBAL             16 (sm)
                STORE_ATTR              11 (handle_objection)

 184            LOAD_CONST               1 (None)
                STORE_FAST              10 (error)

 185            NOP

 187    L3:     LOAD_FAST_BORROW         6 (_capture)
                PUSH_NULL

 188            LOAD_CONST               9 ('call.started')

 189            LOAD_FAST_BORROW         1 (brokerage_id)

 190            LOAD_FAST_BORROW         5 (call_sid)

 191            LOAD_CONST              10 ('call')

 192            LOAD_CONST              11 ('call_logger')

 193            LOAD_CONST              12 ('source')
                LOAD_CONST              13 ('simulated')
                BUILD_MAP                1

 194            LOAD_CONST              14 ('system')

 195            LOAD_CONST              15 ('lead_received')

 196            LOAD_CONST              13 ('simulated')

 187            LOAD_CONST              16 (('brokerage_id', 'call_id', 'event_category', 'event_source', 'payload', 'actor', 'workflow_stage', 'source'))
                CALL_KW                  9
                POP_TOP

 199            LOAD_CONST              17 ('id')
                LOAD_FAST_BORROW         1 (brokerage_id)
                LOAD_CONST              18 ('name')
                LOAD_CONST              19 ('Simulated Brokerage')
                BUILD_MAP                2
                STORE_FAST              11 (brokerage_cfg)

 200            LOAD_FAST_BORROW         2 (brokerage_overrides)
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L4)
                NOT_TAKEN

 201            BUILD_MAP                0
                LOAD_FAST_BORROW        11 (brokerage_cfg)
                DICT_UPDATE              1
                LOAD_FAST_BORROW         2 (brokerage_overrides)
                DICT_UPDATE              1
                STORE_FAST              11 (brokerage_cfg)

 203    L4:     LOAD_GLOBAL             16 (sm)
                LOAD_ATTR               30 (PASEngine)
                PUSH_NULL

 204            LOAD_FAST                5 (call_sid)

 205            LOAD_DEREF               0 (scenario)
                LOAD_ATTR               32 (lead_profile)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
        L5:     NOT_TAKEN
        L6:     POP_TOP
                LOAD_CONST               1 (None)

 206    L7:     LOAD_FAST_BORROW        11 (brokerage_cfg)

 203            LOAD_CONST              20 (('call_sid', 'lead_context', 'brokerage'))
                CALL_KW                  3
                STORE_DEREF             28 (engine)

 212            LOAD_DEREF              28 (engine)
                LOAD_ATTR               35 (get_greeting + NULL|self)
                CALL                     0
                STORE_FAST              12 (greeting)

 213            LOAD_DEREF              28 (engine)
                LOAD_ATTR               37 (_log + NULL|self)
                LOAD_CONST              21 ('pas')
                LOAD_FAST_BORROW        12 (greeting)
                CALL                     2
                POP_TOP

 223            LOAD_FAST_BORROW        23 (behavior_state)
                LOAD_FAST_BORROW        24 (behaviour_active)
                LOAD_FAST_BORROW        25 (booking_state)
                LOAD_FAST_BORROW        26 (divergence_actions)
                LOAD_FAST_BORROW        27 (divergence_triggered)
                LOAD_FAST_BORROW        28 (engine)
                LOAD_FAST_BORROW        29 (events)
                LOAD_FAST_BORROW        30 (frustration_score)
                LOAD_FAST_BORROW        31 (personality)
                LOAD_FAST_BORROW         0 (scenario)
                LOAD_FAST_BORROW         3 (strategy_id)
                LOAD_FAST_BORROW        32 (trust_score)
                BUILD_TUPLE             12
                LOAD_CONST              22 (<code object _drive at 0x0000018C18247F80, file "app\services\simulation\runner.py", line 223>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                STORE_FAST              13 (_drive)

 318            LOAD_GLOBAL             38 (asyncio)
                LOAD_ATTR               40 (run)
                PUSH_NULL
                LOAD_FAST_BORROW        13 (_drive)
                PUSH_NULL
                CALL                     0
                CALL                     1
                POP_TOP

 323            LOAD_FAST_BORROW         6 (_capture)
                PUSH_NULL

 324            LOAD_CONST              23 ('call.ended')

 325            LOAD_FAST_BORROW         1 (brokerage_id)

 326            LOAD_FAST_BORROW         5 (call_sid)

 327            LOAD_CONST              10 ('call')

 328            LOAD_CONST              24 ('simulate')

 329            LOAD_GLOBAL             43 (getattr + NULL)
                LOAD_DEREF              28 (engine)
                LOAD_ATTR               44 (state)
                LOAD_ATTR               46 (current)
                LOAD_CONST              25 ('value')
                LOAD_CONST               1 (None)
                CALL                     3

 331            LOAD_CONST              26 ('outcome')
                LOAD_DEREF              28 (engine)
                LOAD_ATTR               49 (get_outcome + NULL|self)
                CALL                     0

 332            LOAD_CONST              27 ('duration_seconds')
                LOAD_SMALL_INT           0

 333            LOAD_CONST              28 ('final_state')
                LOAD_GLOBAL             43 (getattr + NULL)
                LOAD_DEREF              28 (engine)
                LOAD_ATTR               44 (state)
                LOAD_ATTR               46 (current)
                LOAD_CONST              25 ('value')
                LOAD_CONST               1 (None)
                CALL                     3

 334            LOAD_CONST              29 ('states_visited')
                LOAD_GLOBAL             51 (list + NULL)
                LOAD_DEREF              28 (engine)
                LOAD_ATTR               44 (state)
                LOAD_ATTR               52 (states_visited)
                CALL                     1

 335            LOAD_CONST              30 ('is_outbound')
                LOAD_DEREF              28 (engine)
                LOAD_ATTR               54 (is_outbound)

 336            LOAD_CONST              31 ('objections_detected')
                LOAD_GLOBAL             57 (sum + NULL)
                LOAD_DEREF              28 (engine)
                LOAD_ATTR               44 (state)
                LOAD_ATTR               58 (objection_count)
                LOAD_ATTR               61 (values + NULL|self)
                CALL                     0
                CALL                     1

 337            LOAD_CONST              12 ('source')
                LOAD_CONST              13 ('simulated')

 330            BUILD_MAP                7

 339            LOAD_CONST              14 ('system')

 340            LOAD_CONST              32 ('completed')

 341            LOAD_DEREF              28 (engine)
                LOAD_ATTR               49 (get_outcome + NULL|self)
                CALL                     0

 342            LOAD_CONST              13 ('simulated')

 323            LOAD_CONST              33 (('brokerage_id', 'call_id', 'event_category', 'event_source', 'state', 'payload', 'actor', 'workflow_stage', 'outcome_state', 'source'))
                CALL_KW                 11
                POP_TOP

 345            LOAD_DEREF              28 (engine)
                LOAD_ATTR               49 (get_outcome + NULL|self)
                CALL                     0
                STORE_FAST              14 (actual_outcome)

 348            LOAD_DEREF              28 (engine)
                LOAD_ATTR               62 (pending_transfer)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN

 349            LOAD_CONST              34 ('transferred')
                STORE_FAST              14 (actual_outcome)

 351    L8:     LOAD_DEREF              28 (engine)
                LOAD_ATTR               44 (state)
                LOAD_ATTR               64 (transcript_log)
                GET_ITER
                LOAD_FAST_AND_CLEAR     15 (t)
                SWAP                     2
        L9:     BUILD_LIST               0
                SWAP                     2
       L10:     FOR_ITER                14 (to L11)
                STORE_FAST              15 (t)
                LOAD_GLOBAL             67 (dict + NULL)
                LOAD_FAST_BORROW        15 (t)
                CALL                     1
                LIST_APPEND              2
                JUMP_BACKWARD           16 (to L10)
       L11:     END_FOR
                POP_ITER
       L12:     STORE_FAST              16 (transcript)
                STORE_FAST              15 (t)

 353            LOAD_FAST_BORROW        16 (transcript)
                GET_ITER
       L13:     FOR_ITER                36 (to L14)
                STORE_FAST              15 (t)

 354            LOAD_FAST_BORROW        15 (t)
                LOAD_ATTR               69 (get + NULL|self)
                LOAD_CONST              35 ('state')
                CALL                     1
                STORE_FAST              17 (st)

 355            LOAD_GLOBAL             43 (getattr + NULL)
                LOAD_FAST_BORROW        17 (st)
                LOAD_CONST              25 ('value')
                LOAD_FAST_BORROW        17 (st)
                CALL                     3
                LOAD_FAST_BORROW        15 (t)
                LOAD_CONST              35 ('state')
                STORE_SUBSCR
                JUMP_BACKWARD           38 (to L13)

 353   L14:     END_FOR
                POP_ITER

 362   L15:     LOAD_FAST_BORROW         7 (original_log_event_bg)
                LOAD_GLOBAL             16 (sm)
                STORE_ATTR               9 (log_event_bg)

 363            LOAD_FAST_BORROW         8 (original_book_appointment)
                LOAD_GLOBAL             16 (sm)
                STORE_ATTR              10 (book_appointment)

 364            LOAD_FAST_BORROW         9 (original_handle_objection)
                LOAD_GLOBAL             16 (sm)
                STORE_ATTR              11 (handle_objection)

 367            LOAD_DEREF              29 (events)
                GET_ITER
                LOAD_FAST_AND_CLEAR     18 (e)
                SWAP                     2
       L16:     BUILD_LIST               0
                SWAP                     2
       L17:     FOR_ITER                14 (to L18)
                STORE_FAST              18 (e)
                LOAD_GLOBAL             77 (normalize_event + NULL)
                LOAD_FAST_BORROW        18 (e)
                CALL                     1
                LIST_APPEND              2
                JUMP_BACKWARD           16 (to L17)
       L18:     END_FOR
                POP_ITER
       L19:     STORE_FAST              19 (normalized)
                STORE_FAST              18 (e)

 368            LOAD_GLOBAL             79 (reconstruct_call + NULL)
                LOAD_FAST_BORROW        19 (normalized)
                CALL                     1
                STORE_FAST              20 (reconstruction)

 369            LOAD_GLOBAL             81 (evaluate_reconstruction + NULL)
                LOAD_FAST_BORROW        20 (reconstruction)
                CALL                     1
                STORE_FAST              21 (evaluation)

 371            LOAD_GLOBAL             83 (int + NULL)
                LOAD_GLOBAL              2 (time)
                LOAD_ATTR                4 (perf_counter)
                PUSH_NULL
                CALL                     0
                LOAD_FAST_BORROW         4 (started)
                BINARY_OP               10 (-)
                LOAD_CONST              38 (1000)
                BINARY_OP                5 (*)
                CALL                     1
                STORE_FAST              22 (duration_ms)

 373            BUILD_MAP                0

 374            LOAD_CONST              39 ('scenario_id')
                LOAD_DEREF               0 (scenario)
                LOAD_ATTR                8 (id)

 373            MAP_ADD                  1

 375            LOAD_CONST              40 ('scenario_title')
                LOAD_DEREF               0 (scenario)
                LOAD_ATTR               84 (title)

 373            MAP_ADD                  1

 376            LOAD_CONST              41 ('scenario_category')
                LOAD_DEREF               0 (scenario)
                LOAD_ATTR               86 (category)

 373            MAP_ADD                  1

 377            LOAD_CONST              42 ('scenario_tags')
                LOAD_GLOBAL             51 (list + NULL)
                LOAD_DEREF               0 (scenario)
                LOAD_ATTR               88 (tags)
                CALL                     1

 373            MAP_ADD                  1

 378            LOAD_CONST              43 ('call_sid')
                LOAD_FAST_BORROW         5 (call_sid)

 373            MAP_ADD                  1

 379            LOAD_CONST              44 ('brokerage_id')
                LOAD_FAST_BORROW         1 (brokerage_id)

 373            MAP_ADD                  1

 380            LOAD_CONST              45 ('expected_outcome')
                LOAD_DEREF               0 (scenario)
                LOAD_ATTR               90 (expected_outcome)

 373            MAP_ADD                  1

 381            LOAD_CONST              46 ('actual_outcome')
                LOAD_FAST_BORROW        14 (actual_outcome)

 373            MAP_ADD                  1

 382            LOAD_CONST              47 ('passed')
                LOAD_FAST_BORROW        14 (actual_outcome)
                LOAD_DEREF               0 (scenario)
                LOAD_ATTR               90 (expected_outcome)
                COMPARE_OP              72 (==)

 373            MAP_ADD                  1

 383            LOAD_CONST              48 ('events_count')
                LOAD_GLOBAL             93 (len + NULL)
                LOAD_DEREF              29 (events)
                CALL                     1

 373            MAP_ADD                  1

 384            LOAD_CONST              49 ('transcript')
                LOAD_FAST_BORROW        16 (transcript)

 373            MAP_ADD                  1

 385            LOAD_CONST              50 ('reconstruction')
                LOAD_FAST_BORROW        20 (reconstruction)

 373            MAP_ADD                  1

 386            LOAD_CONST              51 ('evaluation')
                LOAD_FAST_BORROW        21 (evaluation)

 373            MAP_ADD                  1

 387            LOAD_CONST              52 ('duration_ms')
                LOAD_FAST_BORROW        22 (duration_ms)

 373            MAP_ADD                  1

 388            LOAD_CONST              37 ('error')
                LOAD_FAST_BORROW        10 (error)

 373            MAP_ADD                  1

 390            LOAD_CONST              53 ('personality_id')
                LOAD_DEREF               0 (scenario)
                LOAD_ATTR               12 (personality_id)

 373            MAP_ADD                  1

 391            LOAD_CONST              54 ('personality_name')
                LOAD_DEREF              31 (personality)
                TO_BOOL
                POP_JUMP_IF_FALSE       13 (to L20)
                NOT_TAKEN
                LOAD_DEREF              31 (personality)
                LOAD_ATTR               94 (name)
                JUMP_FORWARD             1 (to L21)
       L20:     LOAD_CONST               1 (None)

 373   L21:     MAP_ADD                  1

 392            LOAD_CONST              55 ('final_behavior_state')
                LOAD_DEREF              23 (behavior_state)

 393            LOAD_CONST              56 ('trust_score')
                LOAD_GLOBAL             97 (round + NULL)
                LOAD_DEREF              32 (trust_score)
                LOAD_SMALL_INT           4
                CALL                     2

 394            LOAD_CONST              57 ('frustration_score')
                LOAD_GLOBAL             97 (round + NULL)
                LOAD_DEREF              30 (frustration_score)
                LOAD_SMALL_INT           4
                CALL                     2

 395            LOAD_CONST              58 ('divergence_triggered')
                LOAD_DEREF              27 (divergence_triggered)

 396            LOAD_CONST              59 ('divergence_actions')
                LOAD_DEREF              26 (divergence_actions)

 373            BUILD_MAP                5
                DICT_UPDATE              1
                RETURN_VALUE

  --   L22:     SWAP                     2
                POP_TOP

 351            SWAP                     2
                STORE_FAST              15 (t)
                RERAISE                  0

  --   L23:     PUSH_EXC_INFO

 357            LOAD_GLOBAL             70 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       42 (to L27)
                NOT_TAKEN
                STORE_FAST              18 (e)

 358   L24:     LOAD_GLOBAL             73 (type + NULL)
                LOAD_FAST               18 (e)
                CALL                     1
                LOAD_ATTR               74 (__name__)
                FORMAT_SIMPLE
                LOAD_CONST              36 (': ')
                LOAD_FAST               18 (e)
                FORMAT_SIMPLE
                BUILD_STRING             3
                STORE_FAST              10 (error)

 359            LOAD_CONST              37 ('error')
                STORE_FAST              14 (actual_outcome)

 360            BUILD_LIST               0
                STORE_FAST              16 (transcript)
       L25:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              18 (e)
                DELETE_FAST             18 (e)
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 373 (to L15)

  --   L26:     LOAD_CONST               1 (None)
                STORE_FAST              18 (e)
                DELETE_FAST             18 (e)
                RERAISE                  1

 357   L27:     RERAISE                  0

  --   L28:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L29:     PUSH_EXC_INFO

 362            LOAD_FAST                7 (original_log_event_bg)
                LOAD_GLOBAL             16 (sm)
                STORE_ATTR               9 (log_event_bg)

 363            LOAD_FAST                8 (original_book_appointment)
                LOAD_GLOBAL             16 (sm)
                STORE_ATTR              10 (book_appointment)

 364            LOAD_FAST                9 (original_handle_objection)
                LOAD_GLOBAL             16 (sm)
                STORE_ATTR              11 (handle_objection)
                RERAISE                  0

  --   L30:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L31:     SWAP                     2
                POP_TOP

 367            SWAP                     2
                STORE_FAST              18 (e)
                RERAISE                  0
ExceptionTable:
  L3 to L5 -> L23 [0]
  L6 to L9 -> L23 [0]
  L9 to L12 -> L22 [2]
  L12 to L15 -> L23 [0]
  L16 to L19 -> L31 [2]
  L22 to L23 -> L23 [0]
  L23 to L24 -> L28 [1] lasti
  L24 to L25 -> L26 [1] lasti
  L25 to L26 -> L29 [0]
  L26 to L28 -> L28 [1] lasti
  L28 to L29 -> L29 [0]
  L29 to L30 -> L30 [1] lasti

Disassembly of <code object _capture at 0x0000018C17FE1A70, file "app\services\simulation\runner.py", line 164>:
  --           COPY_FREE_VARS           1

 164           RESUME                   0

 165           LOAD_CONST               0 ('event_type')
               LOAD_FAST_BORROW         0 (event_type)
               LOAD_CONST               1 ('created_at')
               LOAD_GLOBAL              1 (_now_iso + NULL)
               CALL                     0
               BUILD_MAP                2
               STORE_FAST               2 (row)

 167           LOAD_FAST_BORROW         1 (kw)
               LOAD_ATTR                3 (items + NULL|self)
               CALL                     0
               GET_ITER
       L1:     FOR_ITER                 9 (to L2)
               UNPACK_SEQUENCE          2
               STORE_FAST_STORE_FAST   52 (k, v)

 168           LOAD_FAST_BORROW_LOAD_FAST_BORROW 66 (v, row)
               LOAD_FAST_BORROW         3 (k)
               STORE_SUBSCR
               JUMP_BACKWARD           11 (to L1)

 167   L2:     END_FOR
               POP_ITER

 169           LOAD_DEREF               5 (events)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_FAST_BORROW         2 (row)
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object _drive at 0x0000018C18247F80, file "app\services\simulation\runner.py", line 223>:
  --            COPY_FREE_VARS          12

 223            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 227            LOAD_SMALL_INT           0
                STORE_FAST               0 (turn_idx)

 228            LOAD_DEREF              20 (scenario)
                LOAD_ATTR                0 (steps)
                GET_ITER
        L2:     EXTENDED_ARG             2
                FOR_ITER               575 (to L20)
                STORE_FAST               1 (step)

 229            LOAD_FAST_BORROW         1 (step)
                LOAD_ATTR                2 (speaker)
                LOAD_CONST               1 ('lead')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE        3 (to L3)
                NOT_TAKEN

 230            JUMP_BACKWARD           23 (to L2)

 231    L3:     LOAD_FAST_BORROW         0 (turn_idx)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST               0 (turn_idx)

 232            LOAD_FAST_BORROW         1 (step)
                LOAD_ATTR                4 (text)
                STORE_FAST               2 (step_text)

 234            LOAD_DEREF              12 (behaviour_active)
                TO_BOOL
                EXTENDED_ARG             1
                POP_JUMP_IF_FALSE      301 (to L10)
        L4:     NOT_TAKEN

 235    L5:     LOAD_GLOBAL              7 (getattr + NULL)
                LOAD_DEREF              16 (engine)
                LOAD_ATTR                8 (state)
                LOAD_ATTR               10 (current)
                LOAD_CONST               2 ('value')
                LOAD_CONST               3 (None)
                CALL                     3
                STORE_FAST               3 (engine_state_str)

 236            LOAD_GLOBAL             13 (sum + NULL)
                LOAD_DEREF              16 (engine)
                LOAD_ATTR                8 (state)
                LOAD_ATTR               14 (objection_count)
                LOAD_ATTR               17 (values + NULL|self)
                CALL                     0
                CALL                     1
                STORE_FAST               4 (objection_total)

 237            LOAD_GLOBAL             19 (compute_behavioral_modifiers + NULL)

 238            LOAD_DEREF              21 (strategy_id)

 239            LOAD_DEREF              19 (personality)

 240            LOAD_DEREF              11 (behavior_state)

 241            LOAD_FAST_BORROW         0 (turn_idx)

 242            LOAD_FAST_BORROW         4 (objection_total)

 243            LOAD_FAST_BORROW         3 (engine_state_str)

 237            LOAD_CONST               4 (('strategy_id', 'lead_personality', 'behavior_state', 'turn_count', 'objection_count', 'engine_state'))
                CALL_KW                  6
                STORE_FAST               5 (modifiers)

 247            LOAD_FAST_BORROW         5 (modifiers)
                LOAD_CONST               5 ('drop_risk')
                BINARY_OP               26 ([])
                LOAD_GLOBAL             20 (TRIGGER_THRESHOLD)
                COMPARE_OP             188 (bool(>=))
                POP_JUMP_IF_FALSE       38 (to L6)
                NOT_TAKEN

 248            LOAD_CONST               6 (True)
                STORE_DEREF             15 (divergence_triggered)

 249            LOAD_DEREF              14 (divergence_actions)
                LOAD_ATTR               23 (append + NULL|self)

 250            LOAD_CONST               7 ('turn')
                LOAD_FAST_BORROW         0 (turn_idx)

 251            LOAD_CONST               8 ('action')
                LOAD_CONST               9 ('lead_dropped')

 252            LOAD_CONST               5 ('drop_risk')
                LOAD_FAST_BORROW         5 (modifiers)
                LOAD_CONST               5 ('drop_risk')
                BINARY_OP               26 ([])

 249            BUILD_MAP                3
                CALL                     1
                POP_TOP

 254            LOAD_CONST              10 ('dropping')
                STORE_DEREF             11 (behavior_state)

 258            POP_TOP
                LOAD_CONST               3 (None)
                RETURN_VALUE

 262    L6:     LOAD_FAST_BORROW         5 (modifiers)
                LOAD_CONST              11 ('booking_failure_risk')
                BINARY_OP               26 ([])
                LOAD_GLOBAL             20 (TRIGGER_THRESHOLD)
                COMPARE_OP             188 (bool(>=))
                POP_JUMP_IF_FALSE       70 (to L9)
                NOT_TAKEN

 263            LOAD_FAST_BORROW         3 (engine_state_str)
                LOAD_CONST              12 ('BOOKING')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       63 (to L9)
                NOT_TAKEN

 264            LOAD_DEREF              13 (booking_state)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST              13 ('should_succeed')
                LOAD_CONST               6 (True)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       39 (to L9)
        L7:     NOT_TAKEN

 266    L8:     LOAD_CONST              14 (False)
                LOAD_DEREF              13 (booking_state)
                LOAD_CONST              13 ('should_succeed')
                STORE_SUBSCR

 267            LOAD_CONST               6 (True)
                STORE_DEREF             15 (divergence_triggered)

 268            LOAD_DEREF              14 (divergence_actions)
                LOAD_ATTR               23 (append + NULL|self)

 269            LOAD_CONST               7 ('turn')
                LOAD_FAST_BORROW         0 (turn_idx)

 270            LOAD_CONST               8 ('action')
                LOAD_CONST              15 ('booking_will_fail')

 271            LOAD_CONST              16 ('risk')
                LOAD_FAST_BORROW         5 (modifiers)
                LOAD_CONST              11 ('booking_failure_risk')
                BINARY_OP               26 ([])

 268            BUILD_MAP                3
                CALL                     1
                POP_TOP
                JUMP_FORWARD            63 (to L10)

 278    L9:     LOAD_FAST_BORROW         5 (modifiers)
                LOAD_CONST              17 ('escalation_risk')
                BINARY_OP               26 ([])
                LOAD_GLOBAL             20 (TRIGGER_THRESHOLD)
                COMPARE_OP             188 (bool(>=))
                POP_JUMP_IF_FALSE       46 (to L10)
                NOT_TAKEN

 279            LOAD_FAST_BORROW         0 (turn_idx)
                LOAD_SMALL_INT           2
                COMPARE_OP             188 (bool(>=))
                POP_JUMP_IF_FALSE       39 (to L10)
                NOT_TAKEN

 281            LOAD_GLOBAL             26 (ESCALATION_INJECTION_TEXT)
                STORE_FAST               2 (step_text)

 282            LOAD_CONST               6 (True)
                STORE_DEREF             15 (divergence_triggered)

 283            LOAD_DEREF              14 (divergence_actions)
                LOAD_ATTR               23 (append + NULL|self)

 284            LOAD_CONST               7 ('turn')
                LOAD_FAST_BORROW         0 (turn_idx)

 285            LOAD_CONST               8 ('action')
                LOAD_CONST              18 ('lead_escalated')

 286            LOAD_CONST              16 ('risk')
                LOAD_FAST_BORROW         5 (modifiers)
                LOAD_CONST              17 ('escalation_risk')
                BINARY_OP               26 ([])

 283            BUILD_MAP                3
                CALL                     1
                POP_TOP

 290   L10:     LOAD_GLOBAL             29 (len + NULL)
                LOAD_DEREF              17 (events)
                CALL                     1
                STORE_FAST               6 (events_before)

 292            LOAD_DEREF              16 (engine)
                LOAD_ATTR               31 (process_input + NULL|self)
                LOAD_FAST_BORROW         2 (step_text)
                CALL                     1
                GET_AWAITABLE            0
                LOAD_CONST               3 (None)
       L11:     SEND                     3 (to L14)
       L12:     YIELD_VALUE              1
       L13:     RESUME                   3
                JUMP_BACKWARD_NO_INTERRUPT 5 (to L11)
       L14:     END_SEND
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST  120 (response, done)

 294            LOAD_DEREF              12 (behaviour_active)
                TO_BOOL
                POP_JUMP_IF_FALSE      148 (to L15)
                NOT_TAKEN

 295            LOAD_GLOBAL             33 (_classify_event_for_behavior + NULL)
                LOAD_DEREF              17 (events)
                LOAD_FAST_BORROW         6 (events_before)
                CALL                     2
                STORE_FAST               9 (classified)

 296            LOAD_GLOBAL             13 (sum + NULL)
                LOAD_DEREF              16 (engine)
                LOAD_ATTR                8 (state)
                LOAD_ATTR               14 (objection_count)
                LOAD_ATTR               17 (values + NULL|self)
                CALL                     0
                CALL                     1
                STORE_FAST               4 (objection_total)

 297            LOAD_GLOBAL             35 (advance_behavior_state + NULL)

 298            LOAD_DEREF              11 (behavior_state)

 299            LOAD_DEREF              21 (strategy_id)

 300            LOAD_DEREF              19 (personality)

 301            LOAD_FAST_BORROW         9 (classified)

 302            LOAD_FAST_BORROW         4 (objection_total)

 303            LOAD_FAST_BORROW         0 (turn_idx)

 297            LOAD_CONST              19 (('current_state', 'strategy_id', 'lead_personality', 'event_type', 'objection_count', 'turn_count'))
                CALL_KW                  6
                STORE_FAST              10 (transition)

 305            LOAD_FAST_BORROW        10 (transition)
                LOAD_CONST              20 ('next_state')
                BINARY_OP               26 ([])
                STORE_DEREF             11 (behavior_state)

 306            LOAD_GLOBAL             37 (_clamp01 + NULL)

 307            LOAD_DEREF              22 (trust_score)

 308            LOAD_FAST_BORROW        10 (transition)
                LOAD_CONST              21 ('trust_delta')
                BINARY_OP               26 ([])

 307            BINARY_OP                0 (+)

 309            LOAD_FAST_BORROW        10 (transition)
                LOAD_CONST              22 ('recovery_delta')
                BINARY_OP               26 ([])

 307            BINARY_OP                0 (+)

 306            CALL                     1
                STORE_DEREF             22 (trust_score)

 311            LOAD_GLOBAL             37 (_clamp01 + NULL)

 312            LOAD_DEREF              18 (frustration_score)
                LOAD_FAST_BORROW        10 (transition)
                LOAD_CONST              23 ('frustration_delta')
                BINARY_OP               26 ([])
                BINARY_OP                0 (+)

 311            CALL                     1
                STORE_DEREF             18 (frustration_score)

 315   L15:     LOAD_FAST_BORROW         8 (done)
                TO_BOOL
                POP_JUMP_IF_TRUE        22 (to L19)
       L16:     NOT_TAKEN
       L17:     LOAD_DEREF              16 (engine)
                LOAD_ATTR               38 (pending_transfer)
                TO_BOOL
       L18:     POP_JUMP_IF_TRUE         4 (to L19)
                NOT_TAKEN
                EXTENDED_ARG             2
                JUMP_BACKWARD          575 (to L2)

 316   L19:     POP_TOP
                LOAD_CONST               3 (None)
                RETURN_VALUE

 228   L20:     END_FOR
                POP_ITER
                LOAD_CONST               3 (None)
                RETURN_VALUE

 292   L21:     CLEANUP_THROW
       L22:     JUMP_BACKWARD_NO_INTERRUPT 197 (to L14)

  --   L23:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L4 -> L23 [0] lasti
  L5 to L7 -> L23 [0] lasti
  L8 to L12 -> L23 [0] lasti
  L12 to L13 -> L21 [3]
  L13 to L16 -> L23 [0] lasti
  L17 to L18 -> L23 [0] lasti
  L19 to L22 -> L23 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025C30, file "app\services\simulation\runner.py", line 400>:
400           RESUME                   0
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

Disassembly of <code object _error_result at 0x0000018C18060F60, file "app\services\simulation\runner.py", line 400>:
400           RESUME                   0

401           LOAD_FAST_BORROW         0 (scenario)
              POP_JUMP_IF_NONE        13 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         0 (scenario)
              LOAD_ATTR                0 (id)
              JUMP_FORWARD             1 (to L2)
      L1:     LOAD_CONST               0 (None)
      L2:     STORE_FAST               3 (sid)

402           BUILD_MAP                0

403           LOAD_CONST               1 ('scenario_id')
              LOAD_FAST_BORROW         3 (sid)

402           MAP_ADD                  1

404           LOAD_CONST               2 ('scenario_title')
              LOAD_CONST               0 (None)

402           MAP_ADD                  1

405           LOAD_CONST               3 ('scenario_category')
              LOAD_CONST               0 (None)

402           MAP_ADD                  1

406           LOAD_CONST               4 ('scenario_tags')
              BUILD_LIST               0

402           MAP_ADD                  1

407           LOAD_CONST               5 ('call_sid')
              LOAD_CONST               0 (None)

402           MAP_ADD                  1

408           LOAD_CONST               6 ('brokerage_id')
              LOAD_FAST_BORROW         1 (brokerage_id)

402           MAP_ADD                  1

409           LOAD_CONST               7 ('expected_outcome')
              LOAD_CONST               0 (None)

402           MAP_ADD                  1

410           LOAD_CONST               8 ('actual_outcome')
              LOAD_CONST               9 ('error')

402           MAP_ADD                  1

411           LOAD_CONST              10 ('passed')
              LOAD_CONST              11 (False)

402           MAP_ADD                  1

412           LOAD_CONST              12 ('events_count')
              LOAD_SMALL_INT           0

402           MAP_ADD                  1

413           LOAD_CONST              13 ('transcript')
              BUILD_LIST               0

402           MAP_ADD                  1

414           LOAD_CONST              14 ('reconstruction')
              LOAD_GLOBAL              3 (reconstruct_call + NULL)
              BUILD_LIST               0
              CALL                     1

402           MAP_ADD                  1

415           LOAD_CONST              15 ('evaluation')
              LOAD_GLOBAL              5 (evaluate_reconstruction + NULL)
              LOAD_GLOBAL              3 (reconstruct_call + NULL)
              BUILD_LIST               0
              CALL                     1
              CALL                     1

402           MAP_ADD                  1

416           LOAD_CONST              16 ('duration_ms')
              LOAD_SMALL_INT           0

402           MAP_ADD                  1

417           LOAD_CONST               9 ('error')
              LOAD_FAST_BORROW         2 (msg)

402           MAP_ADD                  1

419           LOAD_CONST              17 ('personality_id')
              LOAD_CONST               0 (None)

402           MAP_ADD                  1

420           LOAD_CONST              18 ('personality_name')
              LOAD_CONST               0 (None)

402           MAP_ADD                  1

421           LOAD_CONST              19 ('final_behavior_state')
              LOAD_CONST              20 ('neutral')

422           LOAD_CONST              21 ('trust_score')
              LOAD_CONST              22 (0.5)

423           LOAD_CONST              23 ('frustration_score')
              LOAD_CONST              24 (0.0)

424           LOAD_CONST              25 ('divergence_triggered')
              LOAD_CONST              11 (False)

425           LOAD_CONST              26 ('divergence_actions')
              BUILD_LIST               0

402           BUILD_MAP                5
              DICT_UPDATE              1
              RETURN_VALUE
```
