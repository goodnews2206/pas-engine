# memory/diagnostics

- **pyc:** `app\services\memory\__pycache__\diagnostics.cpython-314.pyc`
- **expected source path (absent):** `app\services\memory/diagnostics.py`
- **co_filename (from bytecode):** `app\services\memory\diagnostics.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** memory

## Module docstring

```
PAS144I — Memory-injection runtime diagnostics.

Read-only, deterministic helpers that summarise the structural
``memory.injection.*`` events emitted by PAS144H. Operator-facing
view of memory-runtime health without surfacing memory content,
prompts, or transcripts.

Hard contract:
  * every public helper is read-only — no writes, no transitions,
    no LLM, no embeddings;
  * brokerage helper REQUIRES ``brokerage_id`` (fails closed); there
    is no unscoped brokerage variant;
  * call helper accepts ``brokerage_id`` as a defence-in-depth
    filter when the operator knows the tenant; when omitted, the
    explicit ``events_for_call_unscoped`` path is used so the
    cross-tenant intent is loud at the call site;
  * the summarizer is pure — accepts any iterable of dicts, tolerates
    malformed rows, never raises;
  * payload values *never* leak through diagnostics: only the
    five structural payload keys emitted by PAS144H
    (``reason / memory_count / formatted_chars / warning_count /
    enabled``) are read. Any other field on the row is ignored.

Public surface (deliberately small):
  - MEMORY_INJECTION_EVENT_TYPES                        (tuple[str])
  - summarize_memory_injection_events(events)           -> dict
  - memory_injection_health_for_brokerage(brokerage_id,
        since=None, limit=500)                           -> dict
  - memory_injection_health_for_call(call_id,
        brokerage_id=None)                               -> dict
```

## Imports

`Any`, `Dict`, `Iterable`, `List`, `MAX_LIMIT`, `Optional`, `__future__`, `annotations`, `app.services.intelligence.queries`, `datetime`, `events_for_call`, `events_for_call_unscoped`, `logging`, `recent_events`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_bucket_from_event_type`, `_clamp_brokerage_limit`, `_coerce_since`, `_compute_health_status`, `_fetch_brokerage_events`, `_round4`, `_safe_payload`, `memory_injection_health_for_brokerage`, `memory_injection_health_for_call`, `summarize_memory_injection_events`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS144I — Memory-injection runtime diagnostics.\n\nRead-only, deterministic helpers that summarise the structural\n``memory.injection.*`` events emitted by PAS144H. Operator-facing\nview of memory-runtime health without surfacing memory content,\nprompts, or transcripts.\n\nHard contract:\n  * every public helper is read-only — no writes, no transitions,\n    no LLM, no embeddings;\n  * brokerage helper REQUIRES ``brokerage_id`` (fails closed); there\n    is no unscoped brokerage variant;\n  * call helper accepts ``brokerage_id`` as a defence-in-depth\n    filter when the operator knows the tenant; when omitted, the\n    explicit ``events_for_call_unscoped`` path is used so the\n    cross-tenant intent is loud at the call site;\n  * the summarizer is pure — accepts any iterable of dicts, tolerates\n    malformed rows, never raises;\n  * payload values *never* leak through diagnostics: only the\n    five structural payload keys emitted by PAS144H\n    (``reason / memory_count / formatted_chars / warning_count /\n    enabled``) are read. Any other field on the row is ignored.\n\nPublic surface (deliberately small):\n  - MEMORY_INJECTION_EVENT_TYPES                        (tuple[str])\n  - summarize_memory_injection_events(events)           -> dict\n  - memory_injection_health_for_brokerage(brokerage_id,\n        since=None, limit=500)                           -> dict\n  - memory_injection_health_for_call(call_id,\n        brokerage_id=None)                               -> dict\n'
- 'pas.memory.diagnostics'
- 'since'
- 'limit'
- 'event_type'
- 'Any'
- 'return'
- 'Optional[str]'
- 'Map a memory.injection.* event_type string to the trailing\nbucket name. Returns None for any non-memory event.'
- 'memory.injection.'
- 'row'
- 'Dict[str, Any]'
- "Return row['payload'] coerced to a plain dict."
- 'payload'
- 'value'
- 'float'
- 'Diagnostic-friendly rounding — keeps the JSON report small.'
- 'total'
- 'int'
- 'attempted'
- 'failed'
- 'reasons'
- 'Dict[str, int]'
- 'str'
- 'Deterministic health label.\n\n* inactive             — no events at all\n* inactive_or_disabled — every event was a feature_disabled skip\n                         (engine is honouring the flag; no actual\n                         attempts)\n* healthy              — attempts > 0 AND failure_rate == 0\n* degraded             — attempts > 0 AND 0 < failure_rate < 0.25\n* failing              — attempts > 0 AND failure_rate >= 0.25\n'
- 'inactive'
- 'feature_disabled'
- 'inactive_or_disabled'
- 'healthy'
- 'degraded'
- 'failing'
- 'events'
- 'Optional[Iterable[Any]]'
- 'Aggregate a list of ``pas_events`` rows into a structural health\nsummary.\n\nPure: reads only the structural payload keys emitted by PAS144H\n(``reason``, ``memory_count``, ``formatted_chars``,\n``warning_count``, ``enabled``). Any other field on the row is\nignored — diagnostics never echo memory content, prompts, or\ntranscripts.\n\nTolerates malformed input:\n  * ``None`` and non-iterable input → an empty summary;\n  * non-dict rows are skipped;\n  * non-string ``event_type`` values are skipped;\n  * non-int / negative counts are ignored.\nNever raises.\n'
- 'total_events'
- 'succeeded'
- 'skipped'
- 'success_rate'
- 'failure_rate'
- 'skip_rate'
- 'warning_count_total'
- 'average_memory_count'
- 'average_formatted_chars'
- 'calls_touched'
- 'states_seen'
- 'severity_breakdown'
- 'health_status'
- 'notes'
- 'reason'
- 'warning_count'
- 'memory_count'
- 'formatted_chars'
- 'call_id'
- 'state'
- 'severity'
- 'feature_disabled_dominant'
- 'warnings_present_despite_success'
- 'Coerce ``since`` to an ISO-8601 string suitable for ``since_iso``.'
- 'brokerage_id'
- 'since_iso'
- 'total_cap'
- 'List[Dict[str, Any]]'
- 'Pull up to ``total_cap`` memory.injection.* events for the\ntenant. Uses the audited ``recent_events`` helper. Paginates via\n``offset`` since the underlying helper caps each call at\n``MAX_LIMIT`` rows.\n'
- 'diagnostics.brokerage page failed (non-critical) | brokerage=%s | event_type=%s | offset=%d | error_type=%s'
- 'Return the memory-injection health summary for one tenant.\n\nFails closed when ``brokerage_id`` is missing — there is NO\nunscoped brokerage variant of this helper. (The codebase exposes\n``recent_events_unscoped`` for cross-tenant operator reads; that\npath is deliberately not reused here so this surface cannot\naccidentally widen.)\n\nNever raises. On any Supabase failure, the inner readers return\n``[]`` and the summary degrades to ``health_status="inactive"``.\n'
- 'scope'
- 'brokerage'
- 'error'
- 'missing_brokerage_id'
- 'summary'
- 'events_read'
- 'Return the memory-injection health summary for a single call.\n\nBehaviour:\n  * ``brokerage_id`` provided → uses the tenant-scoped\n    ``events_for_call`` (defence-in-depth against call_id\n    collisions across tenants).\n  * ``brokerage_id`` omitted   → uses the explicitly-named\n    ``events_for_call_unscoped`` so the cross-tenant intent is\n    loud at the call site (mirrors the PAS143F1 pattern).\n\nNever raises. Empty / unknown call_id returns an inactive\nsummary.\n'
- 'call'
- 'missing_call_id'
- 'diagnostics.call failed (non-critical) | call_id=%s | brokerage=%s | error_type=%s'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS144I — Memory-injection runtime diagnostics.\n\nRead-only, deterministic helpers that summarise the structural\n``memory.injection.*`` events emitted by PAS144H. Operator-facing\nview of memory-runtime health without surfacing memory content,\nprompts, or transcripts.\n\nHard contract:\n  * every public helper is read-only — no writes, no transitions,\n    no LLM, no embeddings;\n  * brokerage helper REQUIRES ``brokerage_id`` (fails closed); there\n    is no unscoped brokerage variant;\n  * call helper accepts ``brokerage_id`` as a defence-in-depth\n    filter when the operator knows the tenant; when omitted, the\n    explicit ``events_for_call_unscoped`` path is used so the\n    cross-tenant intent is loud at the call site;\n  * the summarizer is pure — accepts any iterable of dicts, tolerates\n    malformed rows, never raises;\n  * payload values *never* leak through diagnostics: only the\n    five structural payload keys emitted by PAS144H\n    (``reason / memory_count / formatted_chars / warning_count /\n    enabled``) are read. Any other field on the row is ignored.\n\nPublic surface (deliberately small):\n  - MEMORY_INJECTION_EVENT_TYPES                        (tuple[str])\n  - summarize_memory_injection_events(events)           -> dict\n  - memory_injection_health_for_brokerage(brokerage_id,\n        since=None, limit=500)                           -> dict\n  - memory_injection_health_for_call(call_id,\n        brokerage_id=None)                               -> dict\n')
              STORE_NAME               0 (__doc__)

 34           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 36           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 37           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('datetime',))
              IMPORT_NAME              4 (datetime)
              IMPORT_FROM              4 (datetime)
              STORE_NAME               4 (datetime)
              POP_TOP

 38           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('Any', 'Dict', 'Iterable', 'List', 'Optional'))
              IMPORT_NAME              5 (typing)
              IMPORT_FROM              6 (Any)
              STORE_NAME               6 (Any)
              IMPORT_FROM              7 (Dict)
              STORE_NAME               7 (Dict)
              IMPORT_FROM              8 (Iterable)
              STORE_NAME               8 (Iterable)
              IMPORT_FROM              9 (List)
              STORE_NAME               9 (List)
              IMPORT_FROM             10 (Optional)
              STORE_NAME              10 (Optional)
              POP_TOP

 40           LOAD_SMALL_INT           0
              LOAD_CONST               5 (('MAX_LIMIT', 'events_for_call', 'events_for_call_unscoped', 'recent_events'))
              IMPORT_NAME             11 (app.services.intelligence.queries)
              IMPORT_FROM             12 (MAX_LIMIT)
              STORE_NAME              13 (_EVENT_QUERY_MAX_LIMIT)
              IMPORT_FROM             14 (events_for_call)
              STORE_NAME              14 (events_for_call)
              IMPORT_FROM             15 (events_for_call_unscoped)
              STORE_NAME              15 (events_for_call_unscoped)
              IMPORT_FROM             16 (recent_events)
              STORE_NAME              16 (recent_events)
              POP_TOP

 47           LOAD_NAME                3 (logging)
              LOAD_ATTR               34 (getLogger)
              PUSH_NULL
              LOAD_CONST               6 ('pas.memory.diagnostics')
              CALL                     1
              STORE_NAME              18 (logger)

 52           LOAD_CONST              32 (('memory.injection.skipped', 'memory.injection.attempted', 'memory.injection.succeeded', 'memory.injection.failed'))
              STORE_NAME              19 (MEMORY_INJECTION_EVENT_TYPES)

 62           LOAD_CONST               7 (0.25)
              STORE_NAME              20 (FAILING_RATE_THRESHOLD)

 67           LOAD_CONST               8 (500)
              STORE_NAME              21 (DEFAULT_BROKERAGE_LIMIT)

 68           LOAD_CONST               9 (2000)
              STORE_NAME              22 (MAX_BROKERAGE_LIMIT)

 75           LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA3690, file "app\services\memory\diagnostics.py", line 75>)
              MAKE_FUNCTION
              LOAD_CONST              11 (<code object _bucket_from_event_type at 0x0000018C17FF0F30, file "app\services\memory\diagnostics.py", line 75>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              23 (_bucket_from_event_type)

 88           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA2B50, file "app\services\memory\diagnostics.py", line 88>)
              MAKE_FUNCTION
              LOAD_CONST              13 (<code object _safe_payload at 0x0000018C17972D90, file "app\services\memory\diagnostics.py", line 88>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              24 (_safe_payload)

 96           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C17FA3870, file "app\services\memory\diagnostics.py", line 96>)
              MAKE_FUNCTION
              LOAD_CONST              15 (<code object _round4 at 0x0000018C17F96420, file "app\services\memory\diagnostics.py", line 96>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              25 (_round4)

108           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C18025730, file "app\services\memory\diagnostics.py", line 108>)
              MAKE_FUNCTION
              LOAD_CONST              17 (<code object _compute_health_status at 0x0000018C180608A0, file "app\services\memory\diagnostics.py", line 108>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              26 (_compute_health_status)

146           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA2E20, file "app\services\memory\diagnostics.py", line 146>)
              MAKE_FUNCTION
              LOAD_CONST              19 (<code object summarize_memory_injection_events at 0x0000018C17E92850, file "app\services\memory\diagnostics.py", line 146>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              27 (summarize_memory_injection_events)

295           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA3B40, file "app\services\memory\diagnostics.py", line 295>)
              MAKE_FUNCTION
              LOAD_CONST              21 (<code object _coerce_since at 0x0000018C18060390, file "app\services\memory\diagnostics.py", line 295>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              28 (_coerce_since)

306           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA21F0, file "app\services\memory\diagnostics.py", line 306>)
              MAKE_FUNCTION
              LOAD_CONST              23 (<code object _clamp_brokerage_limit at 0x0000018C18010B30, file "app\services\memory\diagnostics.py", line 306>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              29 (_clamp_brokerage_limit)

316           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C18024F30, file "app\services\memory\diagnostics.py", line 316>)
              MAKE_FUNCTION
              LOAD_CONST              25 (<code object _fetch_brokerage_events at 0x0000018C17E932B0, file "app\services\memory\diagnostics.py", line 316>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              30 (_fetch_brokerage_events)

378           LOAD_CONST              26 ('since')

381           LOAD_CONST               2 (None)

378           LOAD_CONST              27 ('limit')

382           LOAD_NAME               21 (DEFAULT_BROKERAGE_LIMIT)

378           BUILD_MAP                2
              LOAD_CONST              28 (<code object __annotate__ at 0x0000018C18025930, file "app\services\memory\diagnostics.py", line 378>)
              MAKE_FUNCTION
              LOAD_CONST              29 (<code object memory_injection_health_for_brokerage at 0x0000018C17F01460, file "app\services\memory\diagnostics.py", line 378>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              31 (memory_injection_health_for_brokerage)

426           LOAD_CONST              33 ((None,))
              LOAD_CONST              30 (<code object __annotate__ at 0x0000018C18024C30, file "app\services\memory\diagnostics.py", line 426>)
              MAKE_FUNCTION
              LOAD_CONST              31 (<code object memory_injection_health_for_call at 0x0000018C17F72C80, file "app\services\memory\diagnostics.py", line 426>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              32 (memory_injection_health_for_call)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "app\services\memory\diagnostics.py", line 75>:
 75           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('event_type')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _bucket_from_event_type at 0x0000018C17FF0F30, file "app\services\memory\diagnostics.py", line 75>:
 75           RESUME                   0

 78           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (event_type)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

 79           LOAD_CONST               1 (None)
              RETURN_VALUE

 80   L1:     LOAD_FAST_BORROW         0 (event_type)
              LOAD_ATTR                5 (startswith + NULL|self)
              LOAD_CONST               2 ('memory.injection.')
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

 81           LOAD_CONST               1 (None)
              RETURN_VALUE

 82   L2:     LOAD_FAST_BORROW         0 (event_type)
              LOAD_ATTR                7 (rsplit + NULL|self)
              LOAD_CONST               3 ('.')
              LOAD_SMALL_INT           1
              CALL                     2
              LOAD_CONST               4 (-1)
              BINARY_OP               26 ([])
              STORE_FAST               1 (tail)

 83           LOAD_FAST_BORROW         1 (tail)
              LOAD_CONST               5 (('skipped', 'attempted', 'succeeded', 'failed'))
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

 84           LOAD_FAST_BORROW         1 (tail)
              RETURN_VALUE

 85   L3:     LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "app\services\memory\diagnostics.py", line 88>:
 88           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('row')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _safe_payload at 0x0000018C17972D90, file "app\services\memory\diagnostics.py", line 88>:
 88           RESUME                   0

 90           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (row)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

 91           BUILD_MAP                0
              RETURN_VALUE

 92   L1:     LOAD_FAST_BORROW         0 (row)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               1 ('payload')
              CALL                     1
              STORE_FAST               1 (p)

 93           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (p)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (p)
              RETURN_VALUE
      L2:     BUILD_MAP                0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "app\services\memory\diagnostics.py", line 96>:
 96           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('value')
              LOAD_CONST               2 ('float')
              LOAD_CONST               3 ('return')
              LOAD_CONST               2 ('float')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _round4 at 0x0000018C17F96420, file "app\services\memory\diagnostics.py", line 96>:
  96           RESUME                   0

  98           LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (value)
               LOAD_GLOBAL              2 (int)
               LOAD_GLOBAL              4 (float)
               BUILD_TUPLE              2
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN

  99           LOAD_CONST               1 (0.0)
               RETURN_VALUE

 100   L1:     NOP

 101   L2:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 0 (value, value)
               COMPARE_OP             119 (bool(!=))
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN

 102   L3:     LOAD_CONST               1 (0.0)
               RETURN_VALUE

 101   L4:     NOP

 105           LOAD_GLOBAL              9 (round + NULL)
               LOAD_GLOBAL              5 (float + NULL)
               LOAD_FAST                0 (value)
               CALL                     1
               LOAD_SMALL_INT           4
               CALL                     2
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 103           LOAD_GLOBAL              6 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L7)
               NOT_TAKEN
               POP_TOP

 104   L6:     POP_EXCEPT
               LOAD_CONST               1 (0.0)
               RETURN_VALUE

 103   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025730, file "app\services\memory\diagnostics.py", line 108>:
108           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('total')

110           LOAD_CONST               2 ('int')

108           LOAD_CONST               3 ('attempted')

111           LOAD_CONST               2 ('int')

108           LOAD_CONST               4 ('failed')

112           LOAD_CONST               2 ('int')

108           LOAD_CONST               5 ('reasons')

113           LOAD_CONST               6 ('Dict[str, int]')

108           LOAD_CONST               7 ('return')

114           LOAD_CONST               8 ('str')

108           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _compute_health_status at 0x0000018C180608A0, file "app\services\memory\diagnostics.py", line 108>:
 108            RESUME                   0

 125            LOAD_FAST_BORROW         0 (total)
                LOAD_SMALL_INT           0
                COMPARE_OP              58 (bool(<=))
                POP_JUMP_IF_FALSE        3 (to L1)
                NOT_TAKEN

 126            LOAD_CONST               1 ('inactive')
                RETURN_VALUE

 127    L1:     LOAD_FAST_BORROW         1 (attempted)
                LOAD_SMALL_INT           0
                COMPARE_OP              58 (bool(<=))
                POP_JUMP_IF_FALSE       57 (to L9)
                NOT_TAKEN

 130            LOAD_FAST_BORROW         3 (reasons)
                LOAD_ATTR                1 (items + NULL|self)
                CALL                     0
                GET_ITER
                LOAD_FAST_AND_CLEAR      4 (r)
                LOAD_FAST_AND_CLEAR      5 (c)
                SWAP                     3
        L2:     BUILD_MAP                0
                SWAP                     2
        L3:     FOR_ITER                16 (to L6)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   69 (r, c)
                LOAD_FAST_BORROW         4 (r)
                LOAD_CONST               2 ('feature_disabled')
                COMPARE_OP             119 (bool(!=))
        L4:     POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN
                JUMP_BACKWARD           14 (to L3)
        L5:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (r, c)
                MAP_ADD                  2
                JUMP_BACKWARD           18 (to L3)
        L6:     END_FOR
                POP_ITER
        L7:     STORE_FAST               6 (non_disabled)
                STORE_FAST               4 (r)
                STORE_FAST               5 (c)

 131            LOAD_FAST_BORROW         6 (non_disabled)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN

 132            LOAD_CONST               3 ('inactive_or_disabled')
                RETURN_VALUE

 133    L8:     LOAD_CONST               1 ('inactive')
                RETURN_VALUE

 134    L9:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 33 (failed, attempted)
                BINARY_OP               11 (/)
                STORE_FAST               7 (rate)

 135            LOAD_FAST_BORROW         7 (rate)
                LOAD_CONST               4 (0.0)
                COMPARE_OP              58 (bool(<=))
                POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN

 136            LOAD_CONST               5 ('healthy')
                RETURN_VALUE

 137   L10:     LOAD_FAST_BORROW         7 (rate)
                LOAD_GLOBAL              2 (FAILING_RATE_THRESHOLD)
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        3 (to L11)
                NOT_TAKEN

 138            LOAD_CONST               6 ('degraded')
                RETURN_VALUE

 139   L11:     LOAD_CONST               7 ('failing')
                RETURN_VALUE

  --   L12:     SWAP                     2
                POP_TOP

 130            SWAP                     3
                STORE_FAST               5 (c)
                STORE_FAST               4 (r)
                RERAISE                  0
ExceptionTable:
  L2 to L4 -> L12 [3]
  L5 to L7 -> L12 [3]

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "app\services\memory\diagnostics.py", line 146>:
146           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('events')

147           LOAD_CONST               2 ('Optional[Iterable[Any]]')

146           LOAD_CONST               3 ('return')

148           LOAD_CONST               4 ('Dict[str, Any]')

146           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object summarize_memory_injection_events at 0x0000018C17E92850, file "app\services\memory\diagnostics.py", line 146>:
 146            RESUME                   0

 165            BUILD_MAP                0

 166            LOAD_CONST               1 ('total_events')
                LOAD_SMALL_INT           0

 165            MAP_ADD                  1

 167            LOAD_CONST               2 ('attempted')
                LOAD_SMALL_INT           0

 165            MAP_ADD                  1

 168            LOAD_CONST               3 ('succeeded')
                LOAD_SMALL_INT           0

 165            MAP_ADD                  1

 169            LOAD_CONST               4 ('failed')
                LOAD_SMALL_INT           0

 165            MAP_ADD                  1

 170            LOAD_CONST               5 ('skipped')
                LOAD_SMALL_INT           0

 165            MAP_ADD                  1

 171            LOAD_CONST               6 ('success_rate')
                LOAD_CONST               7 (0.0)

 165            MAP_ADD                  1

 172            LOAD_CONST               8 ('failure_rate')
                LOAD_CONST               7 (0.0)

 165            MAP_ADD                  1

 173            LOAD_CONST               9 ('skip_rate')
                LOAD_CONST               7 (0.0)

 165            MAP_ADD                  1

 174            LOAD_CONST              10 ('reasons')
                BUILD_MAP                0

 165            MAP_ADD                  1

 175            LOAD_CONST              11 ('warning_count_total')
                LOAD_SMALL_INT           0

 165            MAP_ADD                  1

 176            LOAD_CONST              12 ('average_memory_count')
                LOAD_CONST               7 (0.0)

 165            MAP_ADD                  1

 177            LOAD_CONST              13 ('average_formatted_chars')
                LOAD_CONST               7 (0.0)

 165            MAP_ADD                  1

 178            LOAD_CONST              14 ('calls_touched')
                LOAD_SMALL_INT           0

 165            MAP_ADD                  1

 179            LOAD_CONST              15 ('states_seen')
                BUILD_LIST               0

 165            MAP_ADD                  1

 180            LOAD_CONST              16 ('severity_breakdown')
                BUILD_MAP                0

 165            MAP_ADD                  1

 181            LOAD_CONST              17 ('health_status')
                LOAD_CONST              18 ('inactive')

 165            MAP_ADD                  1

 182            LOAD_CONST              19 ('notes')
                BUILD_LIST               0

 165            MAP_ADD                  1
                STORE_FAST               1 (summary)

 185            LOAD_FAST_BORROW         0 (events)
                POP_JUMP_IF_NOT_NONE     3 (to L1)
                NOT_TAKEN

 186            LOAD_FAST_BORROW         1 (summary)
                RETURN_VALUE

 187    L1:     NOP

 188    L2:     LOAD_GLOBAL              1 (list + NULL)
                LOAD_FAST_BORROW         0 (events)
                CALL                     1
                STORE_FAST               2 (rows)

 191    L3:     LOAD_FAST                2 (rows)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN

 192            LOAD_FAST                1 (summary)
                RETURN_VALUE

 194    L4:     LOAD_CONST               2 ('attempted')
                LOAD_SMALL_INT           0
                LOAD_CONST               3 ('succeeded')
                LOAD_SMALL_INT           0
                LOAD_CONST               4 ('failed')
                LOAD_SMALL_INT           0
                LOAD_CONST               5 ('skipped')
                LOAD_SMALL_INT           0
                BUILD_MAP                4
                STORE_FAST               3 (counts)

 195            BUILD_MAP                0
                STORE_FAST               4 (reasons)

 196            LOAD_SMALL_INT           0
                STORE_FAST               5 (warning_count_total)

 197            BUILD_LIST               0
                STORE_FAST               6 (memory_counts)

 198            BUILD_LIST               0
                STORE_FAST               7 (formatted_chars)

 199            LOAD_GLOBAL              5 (set + NULL)
                CALL                     0
                STORE_FAST               8 (calls)

 200            LOAD_GLOBAL              5 (set + NULL)
                CALL                     0
                STORE_FAST               9 (states)

 201            BUILD_MAP                0
                STORE_FAST              10 (severities)

 203            LOAD_FAST                2 (rows)
                GET_ITER
        L5:     EXTENDED_ARG             2
                FOR_ITER               638 (to L16)
                STORE_FAST              11 (row)

 204            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST               11 (row)
                LOAD_GLOBAL              8 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN

 205            JUMP_BACKWARD           28 (to L5)

 206    L6:     LOAD_GLOBAL             11 (_bucket_from_event_type + NULL)
                LOAD_FAST               11 (row)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              20 ('event_type')
                CALL                     1
                CALL                     1
                STORE_FAST              12 (bucket)

 207            LOAD_FAST               12 (bucket)
                POP_JUMP_IF_NOT_NONE     3 (to L7)
                NOT_TAKEN

 208            JUMP_BACKWARD           60 (to L5)

 209    L7:     LOAD_FAST_LOAD_FAST     60 (counts, bucket)
                COPY                     2
                COPY                     2
                BINARY_OP               26 ([])
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                SWAP                     3
                SWAP                     2
                STORE_SUBSCR

 211            LOAD_GLOBAL             15 (_safe_payload + NULL)
                LOAD_FAST               11 (row)
                CALL                     1
                STORE_FAST              13 (payload)

 216            LOAD_FAST               13 (payload)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              21 ('reason')
                CALL                     1
                STORE_FAST              14 (reason)

 217            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST               14 (reason)
                LOAD_GLOBAL             16 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       50 (to L8)
                NOT_TAKEN
                LOAD_FAST               14 (reason)
                LOAD_ATTR               19 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       28 (to L8)
                NOT_TAKEN

 218            LOAD_FAST                4 (reasons)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_FAST               14 (reason)
                LOAD_SMALL_INT           0
                CALL                     2
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_FAST_LOAD_FAST     78 (reasons, reason)
                STORE_SUBSCR

 220    L8:     LOAD_FAST               13 (payload)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              22 ('warning_count')
                CALL                     1
                STORE_FAST              15 (wc)

 221            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST               15 (wc)
                LOAD_GLOBAL             20 (int)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       16 (to L9)
                NOT_TAKEN
                LOAD_FAST               15 (wc)
                LOAD_SMALL_INT           0
                COMPARE_OP             188 (bool(>=))
                POP_JUMP_IF_FALSE        9 (to L9)
                NOT_TAKEN

 222            LOAD_FAST_LOAD_FAST     95 (warning_count_total, wc)
                BINARY_OP               13 (+=)
                STORE_FAST               5 (warning_count_total)

 224    L9:     LOAD_FAST               13 (payload)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              23 ('memory_count')
                CALL                     1
                STORE_FAST              16 (mc)

 225            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST               16 (mc)
                LOAD_GLOBAL             20 (int)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L10)
                NOT_TAKEN
                LOAD_FAST               16 (mc)
                LOAD_SMALL_INT           0
                COMPARE_OP             188 (bool(>=))
                POP_JUMP_IF_FALSE       18 (to L10)
                NOT_TAKEN

 226            LOAD_FAST                6 (memory_counts)
                LOAD_ATTR               23 (append + NULL|self)
                LOAD_FAST               16 (mc)
                CALL                     1
                POP_TOP

 228   L10:     LOAD_FAST               13 (payload)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              24 ('formatted_chars')
                CALL                     1
                STORE_FAST              17 (fc)

 229            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST               17 (fc)
                LOAD_GLOBAL             20 (int)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L11)
                NOT_TAKEN
                LOAD_FAST               17 (fc)
                LOAD_SMALL_INT           0
                COMPARE_OP             188 (bool(>=))
                POP_JUMP_IF_FALSE       18 (to L11)
                NOT_TAKEN

 230            LOAD_FAST                7 (formatted_chars)
                LOAD_ATTR               23 (append + NULL|self)
                LOAD_FAST               17 (fc)
                CALL                     1
                POP_TOP

 232   L11:     LOAD_FAST               11 (row)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              25 ('call_id')
                CALL                     1
                STORE_FAST              18 (cid)

 233            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST               18 (cid)
                LOAD_GLOBAL             16 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       54 (to L12)
                NOT_TAKEN
                LOAD_FAST               18 (cid)
                LOAD_ATTR               19 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       32 (to L12)
                NOT_TAKEN

 234            LOAD_FAST                8 (calls)
                LOAD_ATTR               25 (add + NULL|self)
                LOAD_FAST               18 (cid)
                LOAD_ATTR               19 (strip + NULL|self)
                CALL                     0
                CALL                     1
                POP_TOP

 236   L12:     LOAD_FAST               11 (row)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              26 ('state')
                CALL                     1
                STORE_FAST              19 (st)

 237            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST               19 (st)
                LOAD_GLOBAL             16 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       54 (to L13)
                NOT_TAKEN
                LOAD_FAST               19 (st)
                LOAD_ATTR               19 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       32 (to L13)
                NOT_TAKEN

 238            LOAD_FAST                9 (states)
                LOAD_ATTR               25 (add + NULL|self)
                LOAD_FAST               19 (st)
                LOAD_ATTR               19 (strip + NULL|self)
                CALL                     0
                CALL                     1
                POP_TOP

 240   L13:     LOAD_FAST               11 (row)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              27 ('severity')
                CALL                     1
                STORE_FAST              20 (sev)

 241            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST               20 (sev)
                LOAD_GLOBAL             16 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         4 (to L14)
                NOT_TAKEN
                EXTENDED_ARG             2
                JUMP_BACKWARD          585 (to L5)
       L14:     LOAD_FAST               20 (sev)
                LOAD_ATTR               19 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE         4 (to L15)
                NOT_TAKEN
                EXTENDED_ARG             2
                JUMP_BACKWARD          610 (to L5)

 242   L15:     LOAD_FAST               10 (severities)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_FAST               20 (sev)
                LOAD_SMALL_INT           0
                CALL                     2
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_FAST               10 (severities)
                LOAD_FAST               20 (sev)
                STORE_SUBSCR
                EXTENDED_ARG             2
                JUMP_BACKWARD          641 (to L5)

 203   L16:     END_FOR
                POP_ITER

 244            LOAD_GLOBAL             27 (sum + NULL)
                LOAD_FAST                3 (counts)
                LOAD_ATTR               29 (values + NULL|self)
                CALL                     0
                CALL                     1
                STORE_FAST              21 (total)

 245            LOAD_FAST                3 (counts)
                LOAD_CONST               2 ('attempted')
                BINARY_OP               26 ([])
                STORE_FAST              22 (attempted)

 246            LOAD_FAST                3 (counts)
                LOAD_CONST               3 ('succeeded')
                BINARY_OP               26 ([])
                STORE_FAST              23 (succeeded)

 247            LOAD_FAST                3 (counts)
                LOAD_CONST               4 ('failed')
                BINARY_OP               26 ([])
                STORE_FAST              24 (failed)

 248            LOAD_FAST                3 (counts)
                LOAD_CONST               5 ('skipped')
                BINARY_OP               26 ([])
                STORE_FAST              25 (skipped)

 250            LOAD_FAST               21 (total)
                LOAD_FAST                1 (summary)
                LOAD_CONST               1 ('total_events')
                STORE_SUBSCR

 251            LOAD_FAST               22 (attempted)
                LOAD_FAST                1 (summary)
                LOAD_CONST               2 ('attempted')
                STORE_SUBSCR

 252            LOAD_FAST               23 (succeeded)
                LOAD_FAST                1 (summary)
                LOAD_CONST               3 ('succeeded')
                STORE_SUBSCR

 253            LOAD_FAST               24 (failed)
                LOAD_FAST                1 (summary)
                LOAD_CONST               4 ('failed')
                STORE_SUBSCR

 254            LOAD_FAST               25 (skipped)
                LOAD_FAST                1 (summary)
                LOAD_CONST               5 ('skipped')
                STORE_SUBSCR

 256            LOAD_FAST               22 (attempted)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L17)
                NOT_TAKEN
                LOAD_GLOBAL             31 (_round4 + NULL)
                LOAD_FAST               23 (succeeded)
                LOAD_FAST               22 (attempted)
                BINARY_OP               11 (/)
                CALL                     1
                JUMP_FORWARD             1 (to L18)
       L17:     LOAD_CONST               7 (0.0)
       L18:     LOAD_FAST                1 (summary)
                LOAD_CONST               6 ('success_rate')
                STORE_SUBSCR

 257            LOAD_FAST               22 (attempted)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L19)
                NOT_TAKEN
                LOAD_GLOBAL             31 (_round4 + NULL)
                LOAD_FAST               24 (failed)
                LOAD_FAST               22 (attempted)
                BINARY_OP               11 (/)
                CALL                     1
                JUMP_FORWARD             1 (to L20)
       L19:     LOAD_CONST               7 (0.0)
       L20:     LOAD_FAST                1 (summary)
                LOAD_CONST               8 ('failure_rate')
                STORE_SUBSCR

 258            LOAD_FAST               21 (total)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L21)
                NOT_TAKEN
                LOAD_GLOBAL             31 (_round4 + NULL)
                LOAD_FAST               25 (skipped)
                LOAD_FAST               21 (total)
                BINARY_OP               11 (/)
                CALL                     1
                JUMP_FORWARD             1 (to L22)
       L21:     LOAD_CONST               7 (0.0)
       L22:     LOAD_FAST                1 (summary)
                LOAD_CONST               9 ('skip_rate')
                STORE_SUBSCR

 260            LOAD_GLOBAL              9 (dict + NULL)
                LOAD_FAST                4 (reasons)
                CALL                     1
                LOAD_FAST                1 (summary)
                LOAD_CONST              10 ('reasons')
                STORE_SUBSCR

 261            LOAD_FAST_LOAD_FAST     81 (warning_count_total, summary)
                LOAD_CONST              11 ('warning_count_total')
                STORE_SUBSCR

 263            LOAD_FAST                6 (memory_counts)
                TO_BOOL
                POP_JUMP_IF_FALSE       40 (to L23)
                NOT_TAKEN

 264            LOAD_GLOBAL             31 (_round4 + NULL)

 265            LOAD_GLOBAL             27 (sum + NULL)
                LOAD_FAST                6 (memory_counts)
                CALL                     1
                LOAD_GLOBAL             33 (len + NULL)
                LOAD_FAST                6 (memory_counts)
                CALL                     1
                BINARY_OP               11 (/)

 264            CALL                     1
                LOAD_FAST                1 (summary)
                LOAD_CONST              12 ('average_memory_count')
                STORE_SUBSCR

 267   L23:     LOAD_FAST                7 (formatted_chars)
                TO_BOOL
                POP_JUMP_IF_FALSE       40 (to L24)
                NOT_TAKEN

 268            LOAD_GLOBAL             31 (_round4 + NULL)

 269            LOAD_GLOBAL             27 (sum + NULL)
                LOAD_FAST                7 (formatted_chars)
                CALL                     1
                LOAD_GLOBAL             33 (len + NULL)
                LOAD_FAST                7 (formatted_chars)
                CALL                     1
                BINARY_OP               11 (/)

 268            CALL                     1
                LOAD_FAST                1 (summary)
                LOAD_CONST              13 ('average_formatted_chars')
                STORE_SUBSCR

 272   L24:     LOAD_GLOBAL             33 (len + NULL)
                LOAD_FAST                8 (calls)
                CALL                     1
                LOAD_FAST                1 (summary)
                LOAD_CONST              14 ('calls_touched')
                STORE_SUBSCR

 273            LOAD_GLOBAL             35 (sorted + NULL)
                LOAD_FAST                9 (states)
                CALL                     1
                LOAD_FAST                1 (summary)
                LOAD_CONST              15 ('states_seen')
                STORE_SUBSCR

 274            LOAD_GLOBAL              9 (dict + NULL)
                LOAD_FAST               10 (severities)
                CALL                     1
                LOAD_FAST                1 (summary)
                LOAD_CONST              16 ('severity_breakdown')
                STORE_SUBSCR

 275            LOAD_GLOBAL             37 (_compute_health_status + NULL)

 276            LOAD_FAST               21 (total)
                LOAD_FAST               22 (attempted)
                LOAD_FAST               24 (failed)
                LOAD_FAST                4 (reasons)

 275            LOAD_CONST              28 (('total', 'attempted', 'failed', 'reasons'))
                CALL_KW                  4
                LOAD_FAST                1 (summary)
                LOAD_CONST              17 ('health_status')
                STORE_SUBSCR

 279            BUILD_LIST               0
                STORE_FAST              26 (notes)

 280            LOAD_FAST                1 (summary)
                LOAD_CONST              17 ('health_status')
                BINARY_OP               26 ([])
                LOAD_CONST              29 ('inactive_or_disabled')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       18 (to L25)
                NOT_TAKEN

 281            LOAD_FAST               26 (notes)
                LOAD_ATTR               23 (append + NULL|self)
                LOAD_CONST              30 ('feature_disabled_dominant')
                CALL                     1
                POP_TOP

 282   L25:     LOAD_FAST                5 (warning_count_total)
                LOAD_SMALL_INT           0
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE       32 (to L26)
                NOT_TAKEN
                LOAD_FAST               22 (attempted)
                LOAD_SMALL_INT           0
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE       25 (to L26)
                NOT_TAKEN
                LOAD_FAST               24 (failed)
                LOAD_SMALL_INT           0
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       18 (to L26)
                NOT_TAKEN

 285            LOAD_FAST               26 (notes)
                LOAD_ATTR               23 (append + NULL|self)
                LOAD_CONST              31 ('warnings_present_despite_success')
                CALL                     1
                POP_TOP

 286   L26:     LOAD_FAST               26 (notes)
                LOAD_FAST                1 (summary)
                LOAD_CONST              19 ('notes')
                STORE_SUBSCR

 288            LOAD_FAST                1 (summary)
                RETURN_VALUE

  --   L27:     PUSH_EXC_INFO

 189            LOAD_GLOBAL              2 (TypeError)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L29)
                NOT_TAKEN
                POP_TOP

 190            LOAD_FAST                1 (summary)
                SWAP                     2
       L28:     POP_EXCEPT
                RETURN_VALUE

 189   L29:     RERAISE                  0

  --   L30:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L27 [0]
  L27 to L28 -> L30 [1] lasti
  L29 to L30 -> L30 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "app\services\memory\diagnostics.py", line 295>:
295           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('since')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _coerce_since at 0x0000018C18060390, file "app\services\memory\diagnostics.py", line 295>:
295           RESUME                   0

297           LOAD_FAST_BORROW         0 (since)
              POP_JUMP_IF_NOT_NONE     3 (to L1)
              NOT_TAKEN

298           LOAD_CONST               1 (None)
              RETURN_VALUE

299   L1:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (since)
              LOAD_GLOBAL              2 (datetime)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       17 (to L2)
              NOT_TAKEN

300           LOAD_FAST_BORROW         0 (since)
              LOAD_ATTR                5 (isoformat + NULL|self)
              CALL                     0
              RETURN_VALUE

301   L2:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (since)
              LOAD_GLOBAL              6 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       39 (to L3)
              NOT_TAKEN
              LOAD_FAST_BORROW         0 (since)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_FALSE       17 (to L3)
              NOT_TAKEN

302           LOAD_FAST_BORROW         0 (since)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              RETURN_VALUE

303   L3:     LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "app\services\memory\diagnostics.py", line 306>:
306           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('limit')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('int')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _clamp_brokerage_limit at 0x0000018C18010B30, file "app\services\memory\diagnostics.py", line 306>:
 306           RESUME                   0

 307           NOP

 308   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (limit)
               CALL                     1
               STORE_FAST               1 (n)

 311   L2:     LOAD_FAST                1 (n)
               LOAD_SMALL_INT           0
               COMPARE_OP              58 (bool(<=))
               POP_JUMP_IF_FALSE        7 (to L3)
               NOT_TAKEN

 312           LOAD_GLOBAL              6 (DEFAULT_BROKERAGE_LIMIT)
               RETURN_VALUE

 313   L3:     LOAD_GLOBAL              9 (min + NULL)
               LOAD_FAST                1 (n)
               LOAD_GLOBAL             10 (MAX_BROKERAGE_LIMIT)
               CALL                     2
               RETURN_VALUE

  --   L4:     PUSH_EXC_INFO

 309           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       10 (to L6)
               NOT_TAKEN
               POP_TOP

 310           LOAD_GLOBAL              6 (DEFAULT_BROKERAGE_LIMIT)
               SWAP                     2
       L5:     POP_EXCEPT
               RETURN_VALUE

 309   L6:     RERAISE                  0

  --   L7:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L4 [0]
  L4 to L5 -> L7 [1] lasti
  L6 to L7 -> L7 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024F30, file "app\services\memory\diagnostics.py", line 316>:
316           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

317           LOAD_CONST               2 ('str')

316           LOAD_CONST               3 ('since_iso')

319           LOAD_CONST               4 ('Optional[str]')

316           LOAD_CONST               5 ('total_cap')

320           LOAD_CONST               6 ('int')

316           LOAD_CONST               7 ('return')

321           LOAD_CONST               8 ('List[Dict[str, Any]]')

316           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object _fetch_brokerage_events at 0x0000018C17E932B0, file "app\services\memory\diagnostics.py", line 316>:
 316            RESUME                   0

 327            LOAD_FAST_BORROW         2 (total_cap)
                LOAD_SMALL_INT           0
                COMPARE_OP              58 (bool(<=))
                POP_JUMP_IF_FALSE        3 (to L1)
                NOT_TAKEN

 328            BUILD_LIST               0
                RETURN_VALUE

 330    L1:     BUILD_LIST               0
                STORE_FAST               3 (out)

 333            LOAD_GLOBAL              1 (max + NULL)
                LOAD_SMALL_INT           1
                LOAD_FAST_BORROW         2 (total_cap)
                LOAD_GLOBAL              3 (len + NULL)
                LOAD_GLOBAL              4 (MEMORY_INJECTION_EVENT_TYPES)
                CALL                     1
                BINARY_OP                0 (+)
                LOAD_SMALL_INT           1
                BINARY_OP               10 (-)

 334            LOAD_GLOBAL              3 (len + NULL)
                LOAD_GLOBAL              4 (MEMORY_INJECTION_EVENT_TYPES)
                CALL                     1

 333            BINARY_OP                2 (//)
                CALL                     2
                STORE_FAST               4 (per_type_cap)

 336            LOAD_GLOBAL              4 (MEMORY_INJECTION_EVENT_TYPES)
                GET_ITER
        L2:     FOR_ITER               163 (to L11)
                STORE_FAST               5 (event_type)

 337            LOAD_FAST                4 (per_type_cap)
                STORE_FAST               6 (remaining)

 338            LOAD_SMALL_INT           0
                STORE_FAST               7 (offset)

 339    L3:     LOAD_FAST_BORROW         6 (remaining)
                LOAD_SMALL_INT           0
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE      132 (to L9)
                NOT_TAKEN

 340            LOAD_GLOBAL              7 (min + NULL)
                LOAD_GLOBAL              8 (_EVENT_QUERY_MAX_LIMIT)
                LOAD_FAST_BORROW         6 (remaining)
                CALL                     2
                STORE_FAST               8 (page_size)

 341            NOP

 342    L4:     LOAD_GLOBAL             11 (recent_events + NULL)

 343            LOAD_FAST_BORROW         0 (brokerage_id)

 344            LOAD_FAST_BORROW         5 (event_type)

 345            LOAD_FAST_BORROW         1 (since_iso)

 346            LOAD_FAST_BORROW         8 (page_size)

 347            LOAD_FAST_BORROW         7 (offset)

 342            LOAD_CONST               1 (('brokerage_id', 'event_type', 'since_iso', 'limit', 'offset'))
                CALL_KW                  5
                STORE_FAST               9 (page)

 357    L5:     LOAD_FAST                9 (page)
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L6)
                NOT_TAKEN

 358            JUMP_FORWARD            89 (to L9)

 359    L6:     LOAD_FAST                3 (out)
                LOAD_ATTR               23 (extend + NULL|self)
                LOAD_FAST                9 (page)
                CALL                     1
                POP_TOP

 360            LOAD_FAST                7 (offset)
                LOAD_GLOBAL              3 (len + NULL)
                LOAD_FAST                9 (page)
                CALL                     1
                BINARY_OP               13 (+=)
                STORE_FAST               7 (offset)

 361            LOAD_FAST                6 (remaining)
                LOAD_GLOBAL              3 (len + NULL)
                LOAD_FAST                9 (page)
                CALL                     1
                BINARY_OP               23 (-=)
                STORE_FAST               6 (remaining)

 362            LOAD_GLOBAL              3 (len + NULL)
                LOAD_FAST                9 (page)
                CALL                     1
                LOAD_FAST                8 (page_size)
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        2 (to L7)
                NOT_TAKEN

 364            JUMP_FORWARD            19 (to L9)

 365    L7:     LOAD_GLOBAL              3 (len + NULL)
                LOAD_FAST                3 (out)
                CALL                     1
                LOAD_FAST                2 (total_cap)
                COMPARE_OP             188 (bool(>=))
                POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN
                JUMP_BACKWARD          137 (to L3)

 367    L8:     NOP

 368    L9:     LOAD_GLOBAL              3 (len + NULL)
                LOAD_FAST_BORROW         3 (out)
                CALL                     1
                LOAD_FAST_BORROW         2 (total_cap)
                COMPARE_OP             188 (bool(>=))
                POP_JUMP_IF_TRUE         3 (to L10)
                NOT_TAKEN
                JUMP_BACKWARD          163 (to L2)

 369   L10:     POP_TOP
                JUMP_FORWARD             2 (to L12)

 336   L11:     END_FOR
                POP_ITER

 371   L12:     LOAD_FAST_BORROW         3 (out)
                LOAD_CONST               3 (None)
                LOAD_FAST_BORROW         2 (total_cap)
                BINARY_SLICE
                RETURN_VALUE

  --   L13:     PUSH_EXC_INFO

 349            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       55 (to L17)
                NOT_TAKEN
                STORE_FAST              10 (e)

 350   L14:     LOAD_GLOBAL             14 (logger)
                LOAD_ATTR               17 (warning + NULL|self)

 351            LOAD_CONST               2 ('diagnostics.brokerage page failed (non-critical) | brokerage=%s | event_type=%s | offset=%d | error_type=%s')

 354            LOAD_FAST_LOAD_FAST      5 (brokerage_id, event_type)
                LOAD_FAST                7 (offset)
                LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)

 350            CALL                     5
                POP_TOP

 356   L15:     POP_EXCEPT
                LOAD_CONST               3 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                JUMP_BACKWARD           87 (to L9)

  --   L16:     LOAD_CONST               3 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RERAISE                  1

 349   L17:     RERAISE                  0

  --   L18:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L4 to L5 -> L13 [1]
  L13 to L14 -> L18 [2] lasti
  L14 to L15 -> L16 [2] lasti
  L16 to L18 -> L18 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025930, file "app\services\memory\diagnostics.py", line 378>:
378           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

379           LOAD_CONST               2 ('str')

378           LOAD_CONST               3 ('since')

381           LOAD_CONST               4 ('Any')

378           LOAD_CONST               5 ('limit')

382           LOAD_CONST               6 ('int')

378           LOAD_CONST               7 ('return')

383           LOAD_CONST               8 ('Dict[str, Any]')

378           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object memory_injection_health_for_brokerage at 0x0000018C17F01460, file "app\services\memory\diagnostics.py", line 378>:
378           RESUME                   0

395           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (brokerage_id)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       23 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         0 (brokerage_id)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_TRUE        24 (to L2)
              NOT_TAKEN

397   L1:     LOAD_CONST               1 ('scope')
              LOAD_CONST               2 ('brokerage')

398           LOAD_CONST               3 ('brokerage_id')
              LOAD_CONST               4 ('')

399           LOAD_CONST               5 ('since')
              LOAD_CONST               6 (None)

400           LOAD_CONST               7 ('limit')
              LOAD_SMALL_INT           0

401           LOAD_CONST               8 ('error')
              LOAD_CONST               9 ('missing_brokerage_id')

402           LOAD_CONST              10 ('summary')
              LOAD_GLOBAL              7 (summarize_memory_injection_events + NULL)
              BUILD_LIST               0
              CALL                     1

396           BUILD_MAP                6
              RETURN_VALUE

405   L2:     LOAD_FAST_BORROW         0 (brokerage_id)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               3 (bid)

406           LOAD_GLOBAL              9 (_clamp_brokerage_limit + NULL)
              LOAD_FAST_BORROW         2 (limit)
              CALL                     1
              STORE_FAST               4 (capped)

407           LOAD_GLOBAL             11 (_coerce_since + NULL)
              LOAD_FAST_BORROW         1 (since)
              CALL                     1
              STORE_FAST               5 (since_iso)

409           LOAD_GLOBAL             13 (_fetch_brokerage_events + NULL)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 53 (bid, since_iso)
              LOAD_FAST_BORROW         4 (capped)
              LOAD_CONST              11 (('since_iso', 'total_cap'))
              CALL_KW                  3
              STORE_FAST               6 (rows)

410           LOAD_GLOBAL              7 (summarize_memory_injection_events + NULL)
              LOAD_FAST_BORROW         6 (rows)
              CALL                     1
              STORE_FAST               7 (summary)

413           LOAD_CONST               1 ('scope')
              LOAD_CONST               2 ('brokerage')

414           LOAD_CONST               3 ('brokerage_id')
              LOAD_FAST_BORROW         3 (bid)

415           LOAD_CONST               5 ('since')
              LOAD_FAST_BORROW         5 (since_iso)

416           LOAD_CONST               7 ('limit')
              LOAD_FAST_BORROW         4 (capped)

417           LOAD_CONST              12 ('events_read')
              LOAD_GLOBAL             15 (len + NULL)
              LOAD_FAST_BORROW         6 (rows)
              CALL                     1

418           LOAD_CONST              10 ('summary')
              LOAD_FAST_BORROW         7 (summary)

412           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "app\services\memory\diagnostics.py", line 426>:
426           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('call_id')

427           LOAD_CONST               2 ('str')

426           LOAD_CONST               3 ('brokerage_id')

428           LOAD_CONST               4 ('Optional[str]')

426           LOAD_CONST               5 ('return')

429           LOAD_CONST               6 ('Dict[str, Any]')

426           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object memory_injection_health_for_call at 0x0000018C17F72C80, file "app\services\memory\diagnostics.py", line 426>:
 426            RESUME                   0

 443            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (call_id)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (call_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        32 (to L3)
                NOT_TAKEN

 445    L1:     LOAD_CONST               1 ('scope')
                LOAD_CONST               2 ('call')

 446            LOAD_CONST               3 ('call_id')
                LOAD_CONST               4 ('')

 447            LOAD_CONST               5 ('brokerage_id')
                LOAD_FAST                1 (brokerage_id)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L2)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               6 (None)

 448    L2:     LOAD_CONST               7 ('error')
                LOAD_CONST               8 ('missing_call_id')

 449            LOAD_CONST               9 ('summary')
                LOAD_GLOBAL              7 (summarize_memory_injection_events + NULL)
                BUILD_LIST               0
                CALL                     1

 444            BUILD_MAP                5
                RETURN_VALUE

 452    L3:     LOAD_FAST_BORROW         0 (call_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                STORE_FAST               2 (cid)

 453            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (brokerage_id)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       39 (to L4)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L4)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                JUMP_FORWARD             1 (to L5)
        L4:     LOAD_CONST               6 (None)
        L5:     STORE_FAST               3 (bid)

 455            NOP

 456    L6:     LOAD_FAST_BORROW         3 (bid)
                TO_BOOL
                POP_JUMP_IF_FALSE       14 (to L10)
        L7:     NOT_TAKEN

 457    L8:     LOAD_GLOBAL              9 (events_for_call + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (cid, bid)
                LOAD_CONST              10 (('brokerage_id',))
                CALL_KW                  2
                STORE_FAST               4 (rows)
        L9:     JUMP_FORWARD            12 (to L12)

 459   L10:     LOAD_GLOBAL             11 (events_for_call_unscoped + NULL)
                LOAD_FAST_BORROW         2 (cid)
                CALL                     1
                STORE_FAST               4 (rows)
       L11:     NOP

 472   L12:     LOAD_FAST                4 (rows)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
       L13:     GET_ITER

 471            LOAD_FAST_AND_CLEAR      6 (r)
                SWAP                     2
       L14:     BUILD_LIST               0
                SWAP                     2

 472   L15:     FOR_ITER                59 (to L20)
                STORE_FAST               6 (r)

 473            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         6 (r)
                LOAD_GLOBAL             22 (dict)
                CALL                     2
                TO_BOOL

 472   L16:     POP_JUMP_IF_TRUE         3 (to L17)
                NOT_TAKEN
                JUMP_BACKWARD           27 (to L15)

 474   L17:     LOAD_GLOBAL             25 (_bucket_from_event_type + NULL)
                LOAD_FAST_BORROW         6 (r)
                LOAD_ATTR               27 (get + NULL|self)
                LOAD_CONST              12 ('event_type')
                CALL                     1
                CALL                     1

 472   L18:     POP_JUMP_IF_NOT_NONE     3 (to L19)
                NOT_TAKEN
                JUMP_BACKWARD           57 (to L15)
       L19:     LOAD_FAST_BORROW         6 (r)
                LIST_APPEND              2
                JUMP_BACKWARD           61 (to L15)
       L20:     END_FOR
                POP_ITER

 471   L21:     STORE_FAST               7 (mem_rows)
                STORE_FAST               6 (r)

 476            LOAD_GLOBAL              7 (summarize_memory_injection_events + NULL)
                LOAD_FAST_BORROW         7 (mem_rows)
                CALL                     1
                STORE_FAST               8 (summary)

 479            LOAD_CONST               1 ('scope')
                LOAD_CONST               2 ('call')

 480            LOAD_CONST               3 ('call_id')
                LOAD_FAST_BORROW         2 (cid)

 481            LOAD_CONST               5 ('brokerage_id')
                LOAD_FAST_BORROW         3 (bid)

 482            LOAD_CONST              13 ('events_read')
                LOAD_GLOBAL             29 (len + NULL)
                LOAD_FAST_BORROW         7 (mem_rows)
                CALL                     1

 483            LOAD_CONST               9 ('summary')
                LOAD_FAST_BORROW         8 (summary)

 478            BUILD_MAP                5
                RETURN_VALUE

  --   L22:     PUSH_EXC_INFO

 460            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       65 (to L27)
                NOT_TAKEN
                STORE_FAST               5 (e)

 461   L23:     LOAD_GLOBAL             14 (logger)
                LOAD_ATTR               17 (warning + NULL|self)

 462            LOAD_CONST              11 ('diagnostics.call failed (non-critical) | call_id=%s | brokerage=%s | error_type=%s')

 464            LOAD_FAST_LOAD_FAST     35 (cid, bid)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L24)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               4 ('')
       L24:     LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)

 461            CALL                     4
                POP_TOP

 466            BUILD_LIST               0
                STORE_FAST               4 (rows)
       L25:     POP_EXCEPT
                LOAD_CONST               6 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                JUMP_BACKWARD_NO_INTERRUPT 183 (to L12)

  --   L26:     LOAD_CONST               6 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RERAISE                  1

 460   L27:     RERAISE                  0

  --   L28:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L29:     SWAP                     2
                POP_TOP

 471            SWAP                     2
                STORE_FAST               6 (r)
                RERAISE                  0
ExceptionTable:
  L6 to L7 -> L22 [0]
  L8 to L9 -> L22 [0]
  L10 to L11 -> L22 [0]
  L14 to L16 -> L29 [2]
  L17 to L18 -> L29 [2]
  L19 to L21 -> L29 [2]
  L22 to L23 -> L28 [1] lasti
  L23 to L25 -> L26 [1] lasti
  L26 to L28 -> L28 [1] lasti
```
