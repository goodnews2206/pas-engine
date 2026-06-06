# memory/impact

- **pyc:** `app\services\memory\__pycache__\impact.cpython-314.pyc`
- **expected source path (absent):** `app\services\memory/impact.py`
- **co_filename (from bytecode):** `app\services\memory\impact.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** memory

## Module docstring

```
PAS144J — Memory-injection impact correlation + rollout guardrails.

Pure / read-only helpers that group ``pas_events`` rows by ``call_id``
and compare two natural cohorts:

  * **with_memory**  — calls where ``memory.injection.succeeded`` fired
    (i.e. an approved-memory block was injected into the LLM prompt);
  * **without_memory** — calls where no ``memory.injection.attempted``
    ever fired (the clean baseline; flag was off or the gate was never
    reached).

A third implicit bucket — calls where the gate ran but bailed before
injection ("attempted_but_skipped") — is counted toward
``memory_attempted_calls`` but **excluded** from the comparison
cohorts, because it represents neither a clean baseline nor an actual
memory-influenced outcome.

Hard contract:
  * brokerage helper REQUIRES ``brokerage_id`` (fails closed). There
    is NO unscoped brokerage variant. The codebase exposes
    ``recent_events_unscoped`` for operator-side cross-tenant reads;
    impact.py deliberately does not reuse it.
  * the summarizer is pure — accepts any iterable of dicts, tolerates
    malformed rows, never raises;
  * **structural metrics only**: ``call_id`` + ``event_type`` are the
    only row fields read. ``payload`` content is never inspected so
    raw memory / prompt / transcript values cannot leak;
  * statistical conservatism: under-powered cohorts (< 5 calls per
    side) collapse to ``rollout_recommendation="hold"`` and
    ``health_status="inconclusive"``;
  * **no runtime behaviour changes**: nothing here flips a feature
    flag, retunes retrieval weights, or writes back to
    ``pas_memory_records``. PAS144K may build the adaptive loop on
    top.

Public surface (deliberately small):
  - TRACKED_EVENT_TYPES                                    (tuple[str])
  - summarize_memory_impact(events)                         -> dict
  - compare_memory_vs_baseline(events)                      -> dict
  - memory_impact_for_brokerage(brokerage_id, since=None,
        limit=1000)                                          -> dict
```

## Imports

`Any`, `Dict`, `Iterable`, `List`, `MAX_LIMIT`, `Optional`, `Tuple`, `__future__`, `annotations`, `app.services.intelligence.queries`, `datetime`, `logging`, `recent_events`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_bucket_events_by_call`, `_clamp_brokerage_limit`, `_coerce_since`, `_compute_recommendation`, `_failure_rate`, `_fetch_brokerage_events`, `_objection_rate`, `_per_call_template`, `_rate`, `_round4`, `compare_memory_vs_baseline`, `memory_impact_for_brokerage`, `summarize_memory_impact`

## Env-key candidates

`TRACKED_EVENT_TYPES`

## String constants (redacted where noted)

- '\nPAS144J — Memory-injection impact correlation + rollout guardrails.\n\nPure / read-only helpers that group ``pas_events`` rows by ``call_id``\nand compare two natural cohorts:\n\n  * **with_memory**  — calls where ``memory.injection.succeeded`` fired\n    (i.e. an approved-memory block was injected into the LLM prompt);\n  * **without_memory** — calls where no ``memory.injection.attempted``\n    ever fired (the clean baseline; flag was off or the gate was never\n    reached).\n\nA third implicit bucket — calls where the gate ran but bailed before\ninjection ("attempted_but_skipped") — is counted toward\n``memory_attempted_calls`` but **excluded** from the comparison\ncohorts, because it represents neither a clean baseline nor an actual\nmemory-influenced outcome.\n\nHard contract:\n  * brokerage helper REQUIRES ``brokerage_id`` (fails closed). There\n    is NO unscoped brokerage variant. The codebase exposes\n    ``recent_events_unscoped`` for operator-side cross-tenant reads;\n    impact.py deliberately does not reuse it.\n  * the summarizer is pure — accepts any iterable of dicts, tolerates\n    malformed rows, never raises;\n  * **structural metrics only**: ``call_id`` + ``event_type`` are the\n    only row fields read. ``payload`` content is never inspected so\n    raw memory / prompt / transcript values cannot leak;\n  * statistical conservatism: under-powered cohorts (< 5 calls per\n    side) collapse to ``rollout_recommendation="hold"`` and\n    ``health_status="inconclusive"``;\n  * **no runtime behaviour changes**: nothing here flips a feature\n    flag, retunes retrieval weights, or writes back to\n    ``pas_memory_records``. PAS144K may build the adaptive loop on\n    top.\n\nPublic surface (deliberately small):\n  - TRACKED_EVENT_TYPES                                    (tuple[str])\n  - summarize_memory_impact(events)                         -> dict\n  - compare_memory_vs_baseline(events)                      -> dict\n  - memory_impact_for_brokerage(brokerage_id, since=None,\n        limit=1000)                                          -> dict\n'
- 'pas.memory.impact'
- 'Tuple[str, ...]'
- 'TRACKED_EVENT_TYPES'
- 'since'
- 'limit'
- 'value'
- 'float'
- 'return'
- 'Diagnostic rounding — keeps the JSON report compact.'
- 'group'
- 'List[Dict[str, Any]]'
- 'key'
- 'str'
- 'objections'
- 'provider_failed'
- 'system_error'
- 'Dict[str, Any]'
- 'memory_attempted'
- 'memory_succeeded'
- 'booked'
- 'callback'
- 'booking_failed'
- 'events'
- 'Optional[Iterable[Any]]'
- 'Dict[str, Dict[str, Any]]'
- 'Group ``pas_events`` rows by ``call_id``. Tolerates malformed\nrows; never raises. Reads only ``call_id`` + ``event_type`` —\npayload content is never inspected here, which is the load-bearing\nsafety invariant for this module.'
- 'call_id'
- 'event_type'
- 'memory.injection.attempted'
- 'memory.injection.succeeded'
- 'booking.confirmed'
- 'booking.failed'
- 'provider.failed'
- 'system.error'
- 'objection.detected'
- 'with_n'
- 'int'
- 'without_n'
- 'booking_with'
- 'booking_without'
- 'failure_with'
- 'Tuple[str, str, List[str]]'
- 'Return ``(health_status, rollout_recommendation, notes)``.\n\nDeterministic. Tuned conservatively:\n\n  * sample size < MIN_SAMPLE_PER_SIDE on either cohort → "hold"\n    with status "inconclusive";\n  * failure rate (provider + system) on the memory cohort >=\n    HIGH_FAILURE_THRESHOLD → "disable_for_now" + status "failing";\n  * booking rate drops by MATERIAL_BOOKING_DROP or more vs.\n    baseline → "investigate" + status "concerning";\n  * booking rate climbs by MATERIAL_BOOKING_LIFT or more AND\n    memory failure rate < LOW_FAILURE_THRESHOLD → "expand_cautiously"\n    + status "promising";\n  * else → "hold" + status "neutral".\n'
- 'small_sample'
- 'inconclusive'
- 'hold'
- 'memory_failure_rate_high'
- 'failing'
- 'disable_for_now'
- 'booking_underperforms'
- 'concerning'
- 'investigate'
- 'booking_improves_and_low_failure'
- 'promising'
- 'expand_cautiously'
- 'neutral'
- 'Group rows by ``call_id`` and emit the full impact summary.\n\nPure: only ``call_id`` + ``event_type`` are read. Payload values\n(memory content, prompts, transcripts, evidence) are never\ninspected and therefore cannot leak into the summary.\n\nTolerates malformed input. Returns a stable dict shape so callers\n(CLI, future PAS144K controller) can rely on every key being\npresent.\n'
- 'total_calls'
- 'memory_attempted_calls'
- 'memory_succeeded_calls'
- 'non_memory_calls'
- 'booked_with_memory'
- 'booked_without_memory'
- 'callback_with_memory'
- 'callback_without_memory'
- 'failed_with_memory'
- 'failed_without_memory'
- 'booking_rate_with_memory'
- 'booking_rate_without_memory'
- 'callback_rate_with_memory'
- 'callback_rate_without_memory'
- 'objection_rate_with_memory'
- 'objection_rate_without_memory'
- 'provider_failure_rate_with_memory'
- 'provider_failure_rate_without_memory'
- 'lift_booking_rate'
- 'lift_callback_rate'
- 'health_status'
- 'rollout_recommendation'
- 'notes'
- 'Cohort-comparison view of ``summarize_memory_impact``.\n\nReturns the lift-focused subset of the full summary: cohort\nsample sizes, rates per side, lift per metric, and the verdict.\nUseful for callers that only need the A/B comparison numbers\nwithout the per-cohort raw counts (the CLI uses the full\nsummary; future PAS144K controller can prefer this leaner shape).\n'
- 'with_memory_n'
- 'without_memory_n'
- 'failure_rate_with_memory'
- 'failure_rate_without_memory'
- 'lift_failure_rate'
- 'lift_objection_rate'
- 'Any'
- 'Optional[str]'
- 'brokerage_id'
- 'since_iso'
- 'total_cap'
- 'Pull up to ``total_cap`` rows across the tracked event types\nfor a tenant. Uses the audited ``recent_events`` helper and\npaginates via ``offset`` since each call caps at\n``_EVENT_QUERY_MAX_LIMIT`` rows.'
- 'impact.brokerage page failed (non-critical) | brokerage=%s | event_type=%s | offset=%d | error_type=%s'
- 'Return the impact summary for one tenant.\n\nFails closed when ``brokerage_id`` is missing — there is no\nunscoped brokerage variant of this helper.\n\nNever raises. Supabase failures degrade the inner reader to\n``[]`` and the summary collapses to ``"inconclusive" / "hold"``.\n'
- 'scope'
- 'brokerage'
- 'error'
- 'missing_brokerage_id'
- 'summary'
- 'events_read'

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS144J — Memory-injection impact correlation + rollout guardrails.\n\nPure / read-only helpers that group ``pas_events`` rows by ``call_id``\nand compare two natural cohorts:\n\n  * **with_memory**  — calls where ``memory.injection.succeeded`` fired\n    (i.e. an approved-memory block was injected into the LLM prompt);\n  * **without_memory** — calls where no ``memory.injection.attempted``\n    ever fired (the clean baseline; flag was off or the gate was never\n    reached).\n\nA third implicit bucket — calls where the gate ran but bailed before\ninjection ("attempted_but_skipped") — is counted toward\n``memory_attempted_calls`` but **excluded** from the comparison\ncohorts, because it represents neither a clean baseline nor an actual\nmemory-influenced outcome.\n\nHard contract:\n  * brokerage helper REQUIRES ``brokerage_id`` (fails closed). There\n    is NO unscoped brokerage variant. The codebase exposes\n    ``recent_events_unscoped`` for operator-side cross-tenant reads;\n    impact.py deliberately does not reuse it.\n  * the summarizer is pure — accepts any iterable of dicts, tolerates\n    malformed rows, never raises;\n  * **structural metrics only**: ``call_id`` + ``event_type`` are the\n    only row fields read. ``payload`` content is never inspected so\n    raw memory / prompt / transcript values cannot leak;\n  * statistical conservatism: under-powered cohorts (< 5 calls per\n    side) collapse to ``rollout_recommendation="hold"`` and\n    ``health_status="inconclusive"``;\n  * **no runtime behaviour changes**: nothing here flips a feature\n    flag, retunes retrieval weights, or writes back to\n    ``pas_memory_records``. PAS144K may build the adaptive loop on\n    top.\n\nPublic surface (deliberately small):\n  - TRACKED_EVENT_TYPES                                    (tuple[str])\n  - summarize_memory_impact(events)                         -> dict\n  - compare_memory_vs_baseline(events)                      -> dict\n  - memory_impact_for_brokerage(brokerage_id, since=None,\n        limit=1000)                                          -> dict\n')
               STORE_NAME               1 (__doc__)

  45           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  47           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (logging)
               STORE_NAME               4 (logging)

  48           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime',))
               IMPORT_NAME              5 (datetime)
               IMPORT_FROM              5 (datetime)
               STORE_NAME               5 (datetime)
               POP_TOP

  49           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Any', 'Dict', 'Iterable', 'List', 'Optional', 'Tuple'))
               IMPORT_NAME              6 (typing)
               IMPORT_FROM              7 (Any)
               STORE_NAME               7 (Any)
               IMPORT_FROM              8 (Dict)
               STORE_NAME               8 (Dict)
               IMPORT_FROM              9 (Iterable)
               STORE_NAME               9 (Iterable)
               IMPORT_FROM             10 (List)
               STORE_NAME              10 (List)
               IMPORT_FROM             11 (Optional)
               STORE_NAME              11 (Optional)
               IMPORT_FROM             12 (Tuple)
               STORE_NAME              12 (Tuple)
               POP_TOP

  51           LOAD_SMALL_INT           0
               LOAD_CONST               5 (('MAX_LIMIT', 'recent_events'))
               IMPORT_NAME             13 (app.services.intelligence.queries)
               IMPORT_FROM             14 (MAX_LIMIT)
               STORE_NAME              15 (_EVENT_QUERY_MAX_LIMIT)
               IMPORT_FROM             16 (recent_events)
               STORE_NAME              16 (recent_events)
               POP_TOP

  56           LOAD_NAME                4 (logging)
               LOAD_ATTR               34 (getLogger)
               PUSH_NULL
               LOAD_CONST               6 ('pas.memory.impact')
               CALL                     1
               STORE_NAME              18 (logger)

  66           LOAD_CONST              42 (('memory.injection.attempted', 'memory.injection.succeeded', 'memory.injection.failed', 'memory.injection.skipped', 'booking.confirmed', 'booking.failed', 'callback.requested', 'call.ended', 'call.ended_with_callback', 'lead.extracted', 'objection.detected', 'provider.failed', 'system.error'))
               STORE_NAME              19 (TRACKED_EVENT_TYPES)
               LOAD_CONST               7 ('Tuple[str, ...]')
               LOAD_NAME               20 (__annotations__)
               LOAD_CONST               8 ('TRACKED_EVENT_TYPES')
               STORE_SUBSCR

  88           LOAD_SMALL_INT           5
               STORE_NAME              21 (MIN_SAMPLE_PER_SIDE)

  89           LOAD_CONST               9 (0.25)
               STORE_NAME              22 (HIGH_FAILURE_THRESHOLD)

  90           LOAD_CONST              10 (0.1)
               STORE_NAME              23 (LOW_FAILURE_THRESHOLD)

  91           LOAD_CONST              11 (0.05)
               STORE_NAME              24 (MATERIAL_BOOKING_LIFT)

  92           LOAD_CONST              11 (0.05)
               STORE_NAME              25 (MATERIAL_BOOKING_DROP)

  94           LOAD_CONST              12 (1000)
               STORE_NAME              26 (DEFAULT_BROKERAGE_LIMIT)

  95           LOAD_CONST              13 (5000)
               STORE_NAME              27 (MAX_BROKERAGE_LIMIT)

 102           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C17FA3960, file "app\services\memory\impact.py", line 102>)
               MAKE_FUNCTION
               LOAD_CONST              15 (<code object _round4 at 0x0000018C18038B70, file "app\services\memory\impact.py", line 102>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              28 (_round4)

 112           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C18024E30, file "app\services\memory\impact.py", line 112>)
               MAKE_FUNCTION
               LOAD_CONST              17 (<code object _rate at 0x0000018C17FE1920, file "app\services\memory\impact.py", line 112>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              29 (_rate)

 118           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA2D30, file "app\services\memory\impact.py", line 118>)
               MAKE_FUNCTION
               LOAD_CONST              19 (<code object _objection_rate at 0x0000018C18038F30, file "app\services\memory\impact.py", line 118>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              30 (_objection_rate)

 124           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA33C0, file "app\services\memory\impact.py", line 124>)
               MAKE_FUNCTION
               LOAD_CONST              21 (<code object _failure_rate at 0x0000018C18038670, file "app\services\memory\impact.py", line 124>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              31 (_failure_rate)

 133           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA3690, file "app\services\memory\impact.py", line 133>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object _per_call_template at 0x0000018C18025230, file "app\services\memory\impact.py", line 133>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              32 (_per_call_template)

 146           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA35A0, file "app\services\memory\impact.py", line 146>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object _bucket_events_by_call at 0x0000018C17F84BB0, file "app\services\memory\impact.py", line 146>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              33 (_bucket_events_by_call)

 202           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C18024B30, file "app\services\memory\impact.py", line 202>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object _compute_recommendation at 0x0000018C17ED6350, file "app\services\memory\impact.py", line 202>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              34 (_compute_recommendation)

 254           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA2C40, file "app\services\memory\impact.py", line 254>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object summarize_memory_impact at 0x0000018C17ED78B0, file "app\services\memory\impact.py", line 254>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              35 (summarize_memory_impact)

 341           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA2100, file "app\services\memory\impact.py", line 341>)
               MAKE_FUNCTION
               LOAD_CONST              31 (<code object compare_memory_vs_baseline at 0x0000018C17CD4970, file "app\services\memory\impact.py", line 341>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              36 (compare_memory_vs_baseline)

 385           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA2880, file "app\services\memory\impact.py", line 385>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object _coerce_since at 0x0000018C18060A50, file "app\services\memory\impact.py", line 385>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              37 (_coerce_since)

 395           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA3C30, file "app\services\memory\impact.py", line 395>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object _clamp_brokerage_limit at 0x0000018C18010DF0, file "app\services\memory\impact.py", line 395>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              38 (_clamp_brokerage_limit)

 405           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C18025930, file "app\services\memory\impact.py", line 405>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object _fetch_brokerage_events at 0x0000018C17F75FD0, file "app\services\memory\impact.py", line 405>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              39 (_fetch_brokerage_events)

 464           LOAD_CONST              38 ('since')

 467           LOAD_CONST               2 (None)

 464           LOAD_CONST              39 ('limit')

 468           LOAD_NAME               26 (DEFAULT_BROKERAGE_LIMIT)

 464           BUILD_MAP                2
               LOAD_CONST              40 (<code object __annotate__ at 0x0000018C18025D30, file "app\services\memory\impact.py", line 464>)
               MAKE_FUNCTION
               LOAD_CONST              41 (<code object memory_impact_for_brokerage at 0x0000018C17F005F0, file "app\services\memory\impact.py", line 464>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              40 (memory_impact_for_brokerage)
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "app\services\memory\impact.py", line 102>:
102           RESUME                   0
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

Disassembly of <code object _round4 at 0x0000018C18038B70, file "app\services\memory\impact.py", line 102>:
 102           RESUME                   0

 104           NOP

 105   L1:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 0 (value, value)
               COMPARE_OP             119 (bool(!=))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 106   L2:     LOAD_CONST               1 (0.0)
               RETURN_VALUE

 105   L3:     NOP

 109           LOAD_GLOBAL              3 (round + NULL)
               LOAD_GLOBAL              5 (float + NULL)
               LOAD_FAST                0 (value)
               CALL                     1
               LOAD_SMALL_INT           4
               CALL                     2
               RETURN_VALUE

  --   L4:     PUSH_EXC_INFO

 107           LOAD_GLOBAL              0 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L6)
               NOT_TAKEN
               POP_TOP

 108   L5:     POP_EXCEPT
               LOAD_CONST               1 (0.0)
               RETURN_VALUE

 107   L6:     RERAISE                  0

  --   L7:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L4 [0]
  L4 to L5 -> L7 [1] lasti
  L6 to L7 -> L7 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024E30, file "app\services\memory\impact.py", line 112>:
112           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('group')
              LOAD_CONST               2 ('List[Dict[str, Any]]')
              LOAD_CONST               3 ('key')
              LOAD_CONST               4 ('str')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('float')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _rate at 0x0000018C17FE1920, file "app\services\memory\impact.py", line 112>:
  --           MAKE_CELL                1 (key)

 112           RESUME                   0

 113           LOAD_FAST_BORROW         0 (group)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN

 114           LOAD_CONST               0 (0.0)
               RETURN_VALUE

 115   L1:     LOAD_GLOBAL              1 (_round4 + NULL)
               LOAD_GLOBAL              3 (sum + NULL)
               LOAD_FAST_BORROW         1 (key)
               BUILD_TUPLE              1
               LOAD_CONST               1 (<code object <genexpr> at 0x0000018C1802C750, file "app\services\memory\impact.py", line 115>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               LOAD_FAST_BORROW         0 (group)
               GET_ITER
               CALL                     0
               CALL                     1
               LOAD_GLOBAL              5 (len + NULL)
               LOAD_FAST_BORROW         0 (group)
               CALL                     1
               BINARY_OP               11 (/)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C1802C750, file "app\services\memory\impact.py", line 115>:
  --           COPY_FREE_VARS           1

 115           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                31 (to L5)
               STORE_FAST_LOAD_FAST    17 (c, c)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_DEREF               2 (key)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "app\services\memory\impact.py", line 118>:
118           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('group')
              LOAD_CONST               2 ('List[Dict[str, Any]]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('float')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _objection_rate at 0x0000018C18038F30, file "app\services\memory\impact.py", line 118>:
118           RESUME                   0

119           LOAD_FAST_BORROW         0 (group)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

120           LOAD_CONST               0 (0.0)
              RETURN_VALUE

121   L1:     LOAD_GLOBAL              1 (_round4 + NULL)
              LOAD_GLOBAL              3 (sum + NULL)
              LOAD_CONST               1 (<code object <genexpr> at 0x0000018C1802C4F0, file "app\services\memory\impact.py", line 121>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         0 (group)
              GET_ITER
              CALL                     0
              CALL                     1
              LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         0 (group)
              CALL                     1
              BINARY_OP               11 (/)
              CALL                     1
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C1802C4F0, file "app\services\memory\impact.py", line 121>:
 121           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                32 (to L3)
               STORE_FAST               1 (c)
               LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         1 (c)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST               0 ('objections')
               LOAD_SMALL_INT           0
               CALL                     2
               CALL                     1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           34 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "app\services\memory\impact.py", line 124>:
124           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('group')
              LOAD_CONST               2 ('List[Dict[str, Any]]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('float')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _failure_rate at 0x0000018C18038670, file "app\services\memory\impact.py", line 124>:
124           RESUME                   0

125           LOAD_FAST_BORROW         0 (group)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

126           LOAD_CONST               0 (0.0)
              RETURN_VALUE

127   L1:     LOAD_GLOBAL              1 (_round4 + NULL)
              LOAD_GLOBAL              3 (sum + NULL)
              LOAD_CONST               1 (<code object <genexpr> at 0x0000018C17972550, file "app\services\memory\impact.py", line 127>)
              MAKE_FUNCTION

128           LOAD_FAST_BORROW         0 (group)
              GET_ITER

127           CALL                     0
              CALL                     1

130           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         0 (group)
              CALL                     1

127           BINARY_OP               11 (/)
              CALL                     1
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C17972550, file "app\services\memory\impact.py", line 127>:
 127           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 128   L2:     FOR_ITER                55 (to L7)
               STORE_FAST               1 (c)

 129           LOAD_FAST_BORROW         1 (c)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('provider_failed')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        26 (to L6)
       L3:     NOT_TAKEN
       L4:     LOAD_FAST_BORROW         1 (c)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               1 ('system_error')
               CALL                     1
               TO_BOOL

 128   L5:     POP_JUMP_IF_TRUE         3 (to L6)
               NOT_TAKEN
               JUMP_BACKWARD           51 (to L2)
       L6:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           57 (to L2)
       L7:     END_FOR
               POP_ITER
               LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L8:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L8 [0] lasti
  L4 to L5 -> L8 [0] lasti
  L6 to L8 -> L8 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "app\services\memory\impact.py", line 133>:
133           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('Dict[str, Any]')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _per_call_template at 0x0000018C18025230, file "app\services\memory\impact.py", line 133>:
133           RESUME                   0

135           LOAD_CONST               0 ('memory_attempted')
              LOAD_CONST               1 (False)

136           LOAD_CONST               2 ('memory_succeeded')
              LOAD_CONST               1 (False)

137           LOAD_CONST               3 ('booked')
              LOAD_CONST               1 (False)

138           LOAD_CONST               4 ('callback')
              LOAD_CONST               1 (False)

139           LOAD_CONST               5 ('booking_failed')
              LOAD_CONST               1 (False)

140           LOAD_CONST               6 ('provider_failed')
              LOAD_CONST               1 (False)

141           LOAD_CONST               7 ('system_error')
              LOAD_CONST               1 (False)

142           LOAD_CONST               8 ('objections')
              LOAD_SMALL_INT           0

134           BUILD_MAP                8
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "app\services\memory\impact.py", line 146>:
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

148           LOAD_CONST               4 ('Dict[str, Dict[str, Any]]')

146           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _bucket_events_by_call at 0x0000018C17F84BB0, file "app\services\memory\impact.py", line 146>:
 146            RESUME                   0

 153            BUILD_MAP                0
                STORE_FAST               1 (calls)

 154            LOAD_FAST_BORROW         0 (events)
                POP_JUMP_IF_NOT_NONE     3 (to L1)
                NOT_TAKEN

 155            LOAD_FAST_BORROW         1 (calls)
                RETURN_VALUE

 156    L1:     NOP

 157    L2:     LOAD_GLOBAL              1 (list + NULL)
                LOAD_FAST_BORROW         0 (events)
                CALL                     1
                STORE_FAST               2 (rows)

 161    L3:     LOAD_FAST                2 (rows)
                GET_ITER
        L4:     EXTENDED_ARG             1
                FOR_ITER               338 (to L18)
                STORE_FAST               3 (row)

 162            LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST                3 (row)
                LOAD_GLOBAL              6 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN

 163            JUMP_BACKWARD           28 (to L4)

 164    L5:     LOAD_FAST                3 (row)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               1 ('call_id')
                CALL                     1
                STORE_FAST               4 (cid)

 165            LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST                4 (cid)
                LOAD_GLOBAL             10 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L6)
                NOT_TAKEN
                LOAD_FAST                4 (cid)
                LOAD_ATTR               13 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN

 166    L6:     JUMP_BACKWARD           91 (to L4)

 167    L7:     LOAD_FAST                3 (row)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               2 ('event_type')
                CALL                     1
                STORE_FAST               5 (et)

 168            LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST                5 (et)
                LOAD_GLOBAL             10 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       12 (to L8)
                NOT_TAKEN
                LOAD_FAST                5 (et)
                LOAD_GLOBAL             14 (TRACKED_EVENT_TYPES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE        3 (to L9)
                NOT_TAKEN

 169    L8:     JUMP_BACKWARD          143 (to L4)

 171    L9:     LOAD_FAST                4 (cid)
                LOAD_ATTR               13 (strip + NULL|self)
                CALL                     0
                STORE_FAST               4 (cid)

 172            LOAD_FAST                1 (calls)
                LOAD_ATTR               17 (setdefault + NULL|self)
                LOAD_FAST                4 (cid)
                LOAD_GLOBAL             19 (_per_call_template + NULL)
                CALL                     0
                CALL                     2
                STORE_FAST               6 (c)

 174            LOAD_FAST                5 (et)
                LOAD_CONST               3 ('memory.injection.attempted')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        8 (to L10)
                NOT_TAKEN

 175            LOAD_CONST               4 (True)
                LOAD_FAST                6 (c)
                LOAD_CONST               5 ('memory_attempted')
                STORE_SUBSCR
                JUMP_BACKWARD          199 (to L4)

 176   L10:     LOAD_FAST                5 (et)
                LOAD_CONST               6 ('memory.injection.succeeded')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       13 (to L11)
                NOT_TAKEN

 180            LOAD_CONST               4 (True)
                LOAD_FAST                6 (c)
                LOAD_CONST               5 ('memory_attempted')
                STORE_SUBSCR

 181            LOAD_CONST               4 (True)
                LOAD_FAST                6 (c)
                LOAD_CONST               7 ('memory_succeeded')
                STORE_SUBSCR
                JUMP_BACKWARD          218 (to L4)

 182   L11:     LOAD_FAST                5 (et)
                LOAD_CONST               8 ('booking.confirmed')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        8 (to L12)
                NOT_TAKEN

 183            LOAD_CONST               4 (True)
                LOAD_FAST                6 (c)
                LOAD_CONST               9 ('booked')
                STORE_SUBSCR
                JUMP_BACKWARD          232 (to L4)

 184   L12:     LOAD_FAST                5 (et)
                LOAD_CONST              10 ('booking.failed')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        8 (to L13)
                NOT_TAKEN

 185            LOAD_CONST               4 (True)
                LOAD_FAST                6 (c)
                LOAD_CONST              11 ('booking_failed')
                STORE_SUBSCR
                JUMP_BACKWARD          246 (to L4)

 186   L13:     LOAD_FAST                5 (et)
                LOAD_CONST              19 (('callback.requested', 'call.ended_with_callback'))
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        9 (to L14)
                NOT_TAKEN

 187            LOAD_CONST               4 (True)
                LOAD_FAST                6 (c)
                LOAD_CONST              12 ('callback')
                STORE_SUBSCR
                EXTENDED_ARG             1
                JUMP_BACKWARD          261 (to L4)

 188   L14:     LOAD_FAST                5 (et)
                LOAD_CONST              13 ('provider.failed')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        9 (to L15)
                NOT_TAKEN

 189            LOAD_CONST               4 (True)
                LOAD_FAST                6 (c)
                LOAD_CONST              14 ('provider_failed')
                STORE_SUBSCR
                EXTENDED_ARG             1
                JUMP_BACKWARD          276 (to L4)

 190   L15:     LOAD_FAST                5 (et)
                LOAD_CONST              15 ('system.error')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        9 (to L16)
                NOT_TAKEN

 191            LOAD_CONST               4 (True)
                LOAD_FAST                6 (c)
                LOAD_CONST              16 ('system_error')
                STORE_SUBSCR
                EXTENDED_ARG             1
                JUMP_BACKWARD          291 (to L4)

 192   L16:     LOAD_FAST                5 (et)
                LOAD_CONST              17 ('objection.detected')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_TRUE         4 (to L17)
                NOT_TAKEN
                EXTENDED_ARG             1
                JUMP_BACKWARD          301 (to L4)

 193   L17:     LOAD_GLOBAL             21 (int + NULL)
                LOAD_FAST                6 (c)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              18 ('objections')
                LOAD_SMALL_INT           0
                CALL                     2
                CALL                     1
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_FAST                6 (c)
                LOAD_CONST              18 ('objections')
                STORE_SUBSCR
                EXTENDED_ARG             1
                JUMP_BACKWARD          341 (to L4)

 161   L18:     END_FOR
                POP_ITER

 199            LOAD_FAST                1 (calls)
                RETURN_VALUE

  --   L19:     PUSH_EXC_INFO

 158            LOAD_GLOBAL              2 (TypeError)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L21)
                NOT_TAKEN
                POP_TOP

 159            LOAD_FAST                1 (calls)
                SWAP                     2
       L20:     POP_EXCEPT
                RETURN_VALUE

 158   L21:     RERAISE                  0

  --   L22:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L19 [0]
  L19 to L20 -> L22 [1] lasti
  L21 to L22 -> L22 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024B30, file "app\services\memory\impact.py", line 202>:
202           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('with_n')

204           LOAD_CONST               2 ('int')

202           LOAD_CONST               3 ('without_n')

205           LOAD_CONST               2 ('int')

202           LOAD_CONST               4 ('booking_with')

206           LOAD_CONST               5 ('float')

202           LOAD_CONST               6 ('booking_without')

207           LOAD_CONST               5 ('float')

202           LOAD_CONST               7 ('failure_with')

208           LOAD_CONST               5 ('float')

202           LOAD_CONST               8 ('return')

209           LOAD_CONST               9 ('Tuple[str, str, List[str]]')

202           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _compute_recommendation at 0x0000018C17ED6350, file "app\services\memory\impact.py", line 202>:
202           RESUME                   0

225           BUILD_LIST               0
              STORE_FAST               5 (notes)

227           LOAD_FAST_BORROW         0 (with_n)
              LOAD_GLOBAL              0 (MIN_SAMPLE_PER_SIDE)
              COMPARE_OP              18 (bool(<))
              POP_JUMP_IF_TRUE        12 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (without_n)
              LOAD_GLOBAL              0 (MIN_SAMPLE_PER_SIDE)
              COMPARE_OP              18 (bool(<))
              POP_JUMP_IF_FALSE       23 (to L2)
              NOT_TAKEN

228   L1:     LOAD_FAST_BORROW         5 (notes)
              LOAD_ATTR                3 (append + NULL|self)
              LOAD_CONST               1 ('small_sample')
              CALL                     1
              POP_TOP

229           LOAD_CONST               2 ('inconclusive')
              LOAD_CONST               3 ('hold')
              LOAD_FAST_BORROW         5 (notes)
              BUILD_TUPLE              3
              RETURN_VALUE

231   L2:     LOAD_FAST_BORROW         4 (failure_with)
              LOAD_GLOBAL              4 (HIGH_FAILURE_THRESHOLD)
              COMPARE_OP             188 (bool(>=))
              POP_JUMP_IF_FALSE       23 (to L3)
              NOT_TAKEN

232           LOAD_FAST_BORROW         5 (notes)
              LOAD_ATTR                3 (append + NULL|self)
              LOAD_CONST               4 ('memory_failure_rate_high')
              CALL                     1
              POP_TOP

233           LOAD_CONST               5 ('failing')
              LOAD_CONST               6 ('disable_for_now')
              LOAD_FAST_BORROW         5 (notes)
              BUILD_TUPLE              3
              RETURN_VALUE

235   L3:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (booking_with, booking_without)
              BINARY_OP               10 (-)
              STORE_FAST               6 (booking_lift)

236           LOAD_FAST_BORROW         6 (booking_lift)
              LOAD_GLOBAL              6 (MATERIAL_BOOKING_DROP)
              UNARY_NEGATIVE
              COMPARE_OP              58 (bool(<=))
              POP_JUMP_IF_FALSE       23 (to L4)
              NOT_TAKEN

237           LOAD_FAST_BORROW         5 (notes)
              LOAD_ATTR                3 (append + NULL|self)
              LOAD_CONST               7 ('booking_underperforms')
              CALL                     1
              POP_TOP

238           LOAD_CONST               8 ('concerning')
              LOAD_CONST               9 ('investigate')
              LOAD_FAST_BORROW         5 (notes)
              BUILD_TUPLE              3
              RETURN_VALUE

241   L4:     LOAD_FAST_BORROW         6 (booking_lift)
              LOAD_GLOBAL              8 (MATERIAL_BOOKING_LIFT)
              COMPARE_OP             188 (bool(>=))
              POP_JUMP_IF_FALSE       34 (to L5)
              NOT_TAKEN

242           LOAD_FAST_BORROW         4 (failure_with)
              LOAD_GLOBAL             10 (LOW_FAILURE_THRESHOLD)
              COMPARE_OP              18 (bool(<))
              POP_JUMP_IF_FALSE       23 (to L5)
              NOT_TAKEN

244           LOAD_FAST_BORROW         5 (notes)
              LOAD_ATTR                3 (append + NULL|self)
              LOAD_CONST              10 ('booking_improves_and_low_failure')
              CALL                     1
              POP_TOP

245           LOAD_CONST              11 ('promising')
              LOAD_CONST              12 ('expand_cautiously')
              LOAD_FAST_BORROW         5 (notes)
              BUILD_TUPLE              3
              RETURN_VALUE

247   L5:     LOAD_CONST              13 ('neutral')
              LOAD_CONST               3 ('hold')
              LOAD_FAST_BORROW         5 (notes)
              BUILD_TUPLE              3
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "app\services\memory\impact.py", line 254>:
254           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('events')

255           LOAD_CONST               2 ('Optional[Iterable[Any]]')

254           LOAD_CONST               3 ('return')

256           LOAD_CONST               4 ('Dict[str, Any]')

254           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object summarize_memory_impact at 0x0000018C17ED78B0, file "app\services\memory\impact.py", line 254>:
 254            RESUME                   0

 267            LOAD_GLOBAL              1 (_bucket_events_by_call + NULL)
                LOAD_FAST_BORROW         0 (events)
                CALL                     1
                STORE_FAST               1 (calls)

 269            LOAD_FAST_BORROW         1 (calls)
                LOAD_ATTR                3 (values + NULL|self)
                CALL                     0
                GET_ITER
                LOAD_FAST_AND_CLEAR      2 (c)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2
        L2:     FOR_ITER                21 (to L5)
                STORE_FAST_LOAD_FAST    34 (c, c)
                LOAD_CONST               1 ('memory_succeeded')
                BINARY_OP               26 ([])
                TO_BOOL
        L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L2)
        L4:     LOAD_FAST_BORROW         2 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           23 (to L2)
        L5:     END_FOR
                POP_ITER
        L6:     STORE_FAST               3 (with_memory)
                STORE_FAST               2 (c)

 270            LOAD_FAST_BORROW         1 (calls)
                LOAD_ATTR                3 (values + NULL|self)
                CALL                     0
                GET_ITER
                LOAD_FAST_AND_CLEAR      2 (c)
                SWAP                     2
        L7:     BUILD_LIST               0
                SWAP                     2
        L8:     FOR_ITER                21 (to L11)
                STORE_FAST_LOAD_FAST    34 (c, c)
                LOAD_CONST               2 ('memory_attempted')
                BINARY_OP               26 ([])
                TO_BOOL
        L9:     POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L8)
       L10:     LOAD_FAST_BORROW         2 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           23 (to L8)
       L11:     END_FOR
                POP_ITER
       L12:     STORE_FAST               4 (without_memory)
                STORE_FAST               2 (c)

 271            LOAD_FAST_BORROW         1 (calls)
                LOAD_ATTR                3 (values + NULL|self)
                CALL                     0
                GET_ITER
                LOAD_FAST_AND_CLEAR      2 (c)
                SWAP                     2
       L13:     BUILD_LIST               0
                SWAP                     2
       L14:     FOR_ITER                21 (to L17)
                STORE_FAST_LOAD_FAST    34 (c, c)
                LOAD_CONST               2 ('memory_attempted')
                BINARY_OP               26 ([])
                TO_BOOL
       L15:     POP_JUMP_IF_TRUE         3 (to L16)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L14)
       L16:     LOAD_FAST_BORROW         2 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           23 (to L14)
       L17:     END_FOR
                POP_ITER
       L18:     STORE_FAST               5 (memory_attempt)
                STORE_FAST               2 (c)

 273            LOAD_GLOBAL              5 (sum + NULL)
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18052F70, file "app\services\memory\impact.py", line 273>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         3 (with_memory)
                GET_ITER
                CALL                     0
                CALL                     1
                STORE_FAST               6 (booked_with)

 274            LOAD_GLOBAL              5 (sum + NULL)
                LOAD_CONST               4 (<code object <genexpr> at 0x0000018C18053630, file "app\services\memory\impact.py", line 274>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         4 (without_memory)
                GET_ITER
                CALL                     0
                CALL                     1
                STORE_FAST               7 (booked_without)

 275            LOAD_GLOBAL              5 (sum + NULL)
                LOAD_CONST               5 (<code object <genexpr> at 0x0000018C18053090, file "app\services\memory\impact.py", line 275>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         3 (with_memory)
                GET_ITER
                CALL                     0
                CALL                     1
                STORE_FAST               8 (callback_with)

 276            LOAD_GLOBAL              5 (sum + NULL)
                LOAD_CONST               6 (<code object <genexpr> at 0x0000018C18053CF0, file "app\services\memory\impact.py", line 276>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         4 (without_memory)
                GET_ITER
                CALL                     0
                CALL                     1
                STORE_FAST               9 (callback_without)

 277            LOAD_GLOBAL              5 (sum + NULL)
                LOAD_CONST               7 (<code object <genexpr> at 0x0000018C18039070, file "app\services\memory\impact.py", line 277>)
                MAKE_FUNCTION

 278            LOAD_FAST_BORROW         3 (with_memory)
                GET_ITER

 277            CALL                     0
                CALL                     1
                STORE_FAST              10 (failed_with)

 281            LOAD_GLOBAL              5 (sum + NULL)
                LOAD_CONST               8 (<code object <genexpr> at 0x0000018C18038170, file "app\services\memory\impact.py", line 281>)
                MAKE_FUNCTION

 282            LOAD_FAST_BORROW         4 (without_memory)
                GET_ITER

 281            CALL                     0
                CALL                     1
                STORE_FAST              11 (failed_without)

 286            LOAD_GLOBAL              7 (_rate + NULL)
                LOAD_FAST_BORROW         3 (with_memory)
                LOAD_CONST               9 ('booked')
                CALL                     2
                STORE_FAST              12 (booking_rate_with)

 287            LOAD_GLOBAL              7 (_rate + NULL)
                LOAD_FAST_BORROW         4 (without_memory)
                LOAD_CONST               9 ('booked')
                CALL                     2
                STORE_FAST              13 (booking_rate_without)

 288            LOAD_GLOBAL              7 (_rate + NULL)
                LOAD_FAST_BORROW         3 (with_memory)
                LOAD_CONST              10 ('callback')
                CALL                     2
                STORE_FAST              14 (callback_rate_with)

 289            LOAD_GLOBAL              7 (_rate + NULL)
                LOAD_FAST_BORROW         4 (without_memory)
                LOAD_CONST              10 ('callback')
                CALL                     2
                STORE_FAST              15 (callback_rate_without)

 290            LOAD_GLOBAL              9 (_objection_rate + NULL)
                LOAD_FAST_BORROW         3 (with_memory)
                CALL                     1
                STORE_FAST              16 (objection_rate_with)

 291            LOAD_GLOBAL              9 (_objection_rate + NULL)
                LOAD_FAST_BORROW         4 (without_memory)
                CALL                     1
                STORE_FAST              17 (objection_rate_without)

 292            LOAD_GLOBAL             11 (_failure_rate + NULL)
                LOAD_FAST_BORROW         3 (with_memory)
                CALL                     1
                STORE_FAST              18 (failure_rate_with)

 293            LOAD_GLOBAL             11 (_failure_rate + NULL)
                LOAD_FAST_BORROW         4 (without_memory)
                CALL                     1
                STORE_FAST              19 (failure_rate_without)

 295            LOAD_GLOBAL             13 (_round4 + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 205 (booking_rate_with, booking_rate_without)
                BINARY_OP               10 (-)
                CALL                     1
                STORE_FAST              20 (lift_booking)

 296            LOAD_GLOBAL             13 (_round4 + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 239 (callback_rate_with, callback_rate_without)
                BINARY_OP               10 (-)
                CALL                     1
                STORE_FAST              21 (lift_callback)

 298            LOAD_GLOBAL             15 (_compute_recommendation + NULL)

 299            LOAD_GLOBAL             17 (len + NULL)
                LOAD_FAST_BORROW         3 (with_memory)
                CALL                     1

 300            LOAD_GLOBAL             17 (len + NULL)
                LOAD_FAST_BORROW         4 (without_memory)
                CALL                     1

 301            LOAD_FAST_BORROW        12 (booking_rate_with)

 302            LOAD_FAST_BORROW        13 (booking_rate_without)

 303            LOAD_FAST_BORROW        18 (failure_rate_with)

 298            LOAD_CONST              11 (('with_n', 'without_n', 'booking_with', 'booking_without', 'failure_with'))
                CALL_KW                  5
                UNPACK_SEQUENCE          3
                STORE_FAST              22 (health_status)
                STORE_FAST              23 (rollout_recommendation)
                STORE_FAST              24 (notes)

 306            BUILD_MAP                0

 307            LOAD_CONST              12 ('total_calls')
                LOAD_GLOBAL             17 (len + NULL)
                LOAD_FAST_BORROW         1 (calls)
                CALL                     1

 306            MAP_ADD                  1

 308            LOAD_CONST              13 ('memory_attempted_calls')
                LOAD_GLOBAL             17 (len + NULL)
                LOAD_FAST_BORROW         5 (memory_attempt)
                CALL                     1

 306            MAP_ADD                  1

 309            LOAD_CONST              14 ('memory_succeeded_calls')
                LOAD_GLOBAL             17 (len + NULL)
                LOAD_FAST_BORROW         3 (with_memory)
                CALL                     1

 306            MAP_ADD                  1

 310            LOAD_CONST              15 ('non_memory_calls')
                LOAD_GLOBAL             17 (len + NULL)
                LOAD_FAST_BORROW         4 (without_memory)
                CALL                     1

 306            MAP_ADD                  1

 312            LOAD_CONST              16 ('booked_with_memory')
                LOAD_FAST_BORROW         6 (booked_with)

 306            MAP_ADD                  1

 313            LOAD_CONST              17 ('booked_without_memory')
                LOAD_FAST_BORROW         7 (booked_without)

 306            MAP_ADD                  1

 314            LOAD_CONST              18 ('callback_with_memory')
                LOAD_FAST_BORROW         8 (callback_with)

 306            MAP_ADD                  1

 315            LOAD_CONST              19 ('callback_without_memory')
                LOAD_FAST_BORROW         9 (callback_without)

 306            MAP_ADD                  1

 316            LOAD_CONST              20 ('failed_with_memory')
                LOAD_FAST_BORROW        10 (failed_with)

 306            MAP_ADD                  1

 317            LOAD_CONST              21 ('failed_without_memory')
                LOAD_FAST_BORROW        11 (failed_without)

 306            MAP_ADD                  1

 319            LOAD_CONST              22 ('booking_rate_with_memory')
                LOAD_FAST_BORROW        12 (booking_rate_with)

 306            MAP_ADD                  1

 320            LOAD_CONST              23 ('booking_rate_without_memory')
                LOAD_FAST_BORROW        13 (booking_rate_without)

 306            MAP_ADD                  1

 321            LOAD_CONST              24 ('callback_rate_with_memory')
                LOAD_FAST_BORROW        14 (callback_rate_with)

 306            MAP_ADD                  1

 322            LOAD_CONST              25 ('callback_rate_without_memory')
                LOAD_FAST_BORROW        15 (callback_rate_without)

 306            MAP_ADD                  1

 323            LOAD_CONST              26 ('objection_rate_with_memory')
                LOAD_FAST_BORROW        16 (objection_rate_with)

 306            MAP_ADD                  1

 324            LOAD_CONST              27 ('objection_rate_without_memory')
                LOAD_FAST_BORROW        17 (objection_rate_without)

 306            MAP_ADD                  1

 325            LOAD_CONST              28 ('provider_failure_rate_with_memory')
                LOAD_FAST_BORROW        18 (failure_rate_with)

 306            MAP_ADD                  1

 326            LOAD_CONST              29 ('provider_failure_rate_without_memory')
                LOAD_FAST_BORROW        19 (failure_rate_without)

 328            LOAD_CONST              30 ('lift_booking_rate')
                LOAD_FAST_BORROW        20 (lift_booking)

 329            LOAD_CONST              31 ('lift_callback_rate')
                LOAD_FAST_BORROW        21 (lift_callback)

 331            LOAD_CONST              32 ('health_status')
                LOAD_FAST_BORROW        22 (health_status)

 332            LOAD_CONST              33 ('rollout_recommendation')
                LOAD_FAST_BORROW        23 (rollout_recommendation)

 333            LOAD_CONST              34 ('notes')
                LOAD_FAST_BORROW        24 (notes)

 306            BUILD_MAP                6
                DICT_UPDATE              1
                RETURN_VALUE

  --   L19:     SWAP                     2
                POP_TOP

 269            SWAP                     2
                STORE_FAST               2 (c)
                RERAISE                  0

  --   L20:     SWAP                     2
                POP_TOP

 270            SWAP                     2
                STORE_FAST               2 (c)
                RERAISE                  0

  --   L21:     SWAP                     2
                POP_TOP

 271            SWAP                     2
                STORE_FAST               2 (c)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L19 [2]
  L4 to L6 -> L19 [2]
  L7 to L9 -> L20 [2]
  L10 to L12 -> L20 [2]
  L13 to L15 -> L21 [2]
  L16 to L18 -> L21 [2]

Disassembly of <code object <genexpr> at 0x0000018C18052F70, file "app\services\memory\impact.py", line 273>:
 273           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                23 (to L5)
               STORE_FAST_LOAD_FAST    17 (c, c)
               LOAD_CONST               0 ('booked')
               BINARY_OP               26 ([])
               TO_BOOL
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           19 (to L2)
       L4:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           25 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C18053630, file "app\services\memory\impact.py", line 274>:
 274           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                23 (to L5)
               STORE_FAST_LOAD_FAST    17 (c, c)
               LOAD_CONST               0 ('booked')
               BINARY_OP               26 ([])
               TO_BOOL
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           19 (to L2)
       L4:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           25 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C18053090, file "app\services\memory\impact.py", line 275>:
 275           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                23 (to L5)
               STORE_FAST_LOAD_FAST    17 (c, c)
               LOAD_CONST               0 ('callback')
               BINARY_OP               26 ([])
               TO_BOOL
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           19 (to L2)
       L4:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           25 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C18053CF0, file "app\services\memory\impact.py", line 276>:
 276           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                23 (to L5)
               STORE_FAST_LOAD_FAST    17 (c, c)
               LOAD_CONST               0 ('callback')
               BINARY_OP               26 ([])
               TO_BOOL
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           19 (to L2)
       L4:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           25 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C18039070, file "app\services\memory\impact.py", line 277>:
 277           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 278   L2:     FOR_ITER                39 (to L7)
               STORE_FAST               1 (c)

 279           LOAD_FAST_BORROW         1 (c)
               LOAD_CONST               0 ('provider_failed')
               BINARY_OP               26 ([])
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L6)
       L3:     NOT_TAKEN
       L4:     LOAD_FAST_BORROW         1 (c)
               LOAD_CONST               1 ('system_error')
               BINARY_OP               26 ([])
               TO_BOOL

 278   L5:     POP_JUMP_IF_TRUE         3 (to L6)
               NOT_TAKEN
               JUMP_BACKWARD           35 (to L2)
       L6:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           41 (to L2)
       L7:     END_FOR
               POP_ITER
               LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L8:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L8 [0] lasti
  L4 to L5 -> L8 [0] lasti
  L6 to L8 -> L8 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C18038170, file "app\services\memory\impact.py", line 281>:
 281           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 282   L2:     FOR_ITER                39 (to L7)
               STORE_FAST               1 (c)

 283           LOAD_FAST_BORROW         1 (c)
               LOAD_CONST               0 ('provider_failed')
               BINARY_OP               26 ([])
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L6)
       L3:     NOT_TAKEN
       L4:     LOAD_FAST_BORROW         1 (c)
               LOAD_CONST               1 ('system_error')
               BINARY_OP               26 ([])
               TO_BOOL

 282   L5:     POP_JUMP_IF_TRUE         3 (to L6)
               NOT_TAKEN
               JUMP_BACKWARD           35 (to L2)
       L6:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           41 (to L2)
       L7:     END_FOR
               POP_ITER
               LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L8:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L8 [0] lasti
  L4 to L5 -> L8 [0] lasti
  L6 to L8 -> L8 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "app\services\memory\impact.py", line 341>:
341           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('events')

342           LOAD_CONST               2 ('Optional[Iterable[Any]]')

341           LOAD_CONST               3 ('return')

343           LOAD_CONST               4 ('Dict[str, Any]')

341           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object compare_memory_vs_baseline at 0x0000018C17CD4970, file "app\services\memory\impact.py", line 341>:
341           RESUME                   0

352           LOAD_GLOBAL              1 (summarize_memory_impact + NULL)
              LOAD_FAST_BORROW         0 (events)
              CALL                     1
              STORE_FAST               1 (s)

354           BUILD_MAP                0

355           LOAD_CONST               1 ('with_memory_n')
              LOAD_FAST_BORROW         1 (s)
              LOAD_CONST               2 ('memory_succeeded_calls')
              BINARY_OP               26 ([])

354           MAP_ADD                  1

356           LOAD_CONST               3 ('without_memory_n')
              LOAD_FAST_BORROW         1 (s)
              LOAD_CONST               4 ('non_memory_calls')
              BINARY_OP               26 ([])

354           MAP_ADD                  1

357           LOAD_CONST               5 ('booking_rate_with_memory')
              LOAD_FAST_BORROW         1 (s)
              LOAD_CONST               5 ('booking_rate_with_memory')
              BINARY_OP               26 ([])

354           MAP_ADD                  1

358           LOAD_CONST               6 ('booking_rate_without_memory')
              LOAD_FAST_BORROW         1 (s)
              LOAD_CONST               6 ('booking_rate_without_memory')
              BINARY_OP               26 ([])

354           MAP_ADD                  1

359           LOAD_CONST               7 ('callback_rate_with_memory')
              LOAD_FAST_BORROW         1 (s)
              LOAD_CONST               7 ('callback_rate_with_memory')
              BINARY_OP               26 ([])

354           MAP_ADD                  1

360           LOAD_CONST               8 ('callback_rate_without_memory')
              LOAD_FAST_BORROW         1 (s)
              LOAD_CONST               8 ('callback_rate_without_memory')
              BINARY_OP               26 ([])

354           MAP_ADD                  1

361           LOAD_CONST               9 ('failure_rate_with_memory')
              LOAD_FAST_BORROW         1 (s)
              LOAD_CONST              10 ('provider_failure_rate_with_memory')
              BINARY_OP               26 ([])

354           MAP_ADD                  1

362           LOAD_CONST              11 ('failure_rate_without_memory')
              LOAD_FAST_BORROW         1 (s)
              LOAD_CONST              12 ('provider_failure_rate_without_memory')
              BINARY_OP               26 ([])

354           MAP_ADD                  1

363           LOAD_CONST              13 ('objection_rate_with_memory')
              LOAD_FAST_BORROW         1 (s)
              LOAD_CONST              13 ('objection_rate_with_memory')
              BINARY_OP               26 ([])

354           MAP_ADD                  1

364           LOAD_CONST              14 ('objection_rate_without_memory')
              LOAD_FAST_BORROW         1 (s)
              LOAD_CONST              14 ('objection_rate_without_memory')
              BINARY_OP               26 ([])

354           MAP_ADD                  1

365           LOAD_CONST              15 ('lift_booking_rate')
              LOAD_FAST_BORROW         1 (s)
              LOAD_CONST              15 ('lift_booking_rate')
              BINARY_OP               26 ([])

354           MAP_ADD                  1

366           LOAD_CONST              16 ('lift_callback_rate')
              LOAD_FAST_BORROW         1 (s)
              LOAD_CONST              16 ('lift_callback_rate')
              BINARY_OP               26 ([])

354           MAP_ADD                  1

367           LOAD_CONST              17 ('lift_failure_rate')
              LOAD_GLOBAL              3 (_round4 + NULL)

368           LOAD_FAST_BORROW         1 (s)
              LOAD_CONST              10 ('provider_failure_rate_with_memory')
              BINARY_OP               26 ([])

369           LOAD_FAST_BORROW         1 (s)
              LOAD_CONST              12 ('provider_failure_rate_without_memory')
              BINARY_OP               26 ([])

368           BINARY_OP               10 (-)

367           CALL                     1

354           MAP_ADD                  1

371           LOAD_CONST              18 ('lift_objection_rate')
              LOAD_GLOBAL              3 (_round4 + NULL)

372           LOAD_FAST_BORROW         1 (s)
              LOAD_CONST              13 ('objection_rate_with_memory')
              BINARY_OP               26 ([])

373           LOAD_FAST_BORROW         1 (s)
              LOAD_CONST              14 ('objection_rate_without_memory')
              BINARY_OP               26 ([])

372           BINARY_OP               10 (-)

371           CALL                     1

354           MAP_ADD                  1

375           LOAD_CONST              19 ('health_status')
              LOAD_FAST_BORROW         1 (s)
              LOAD_CONST              19 ('health_status')
              BINARY_OP               26 ([])

354           MAP_ADD                  1

376           LOAD_CONST              20 ('rollout_recommendation')
              LOAD_FAST_BORROW         1 (s)
              LOAD_CONST              20 ('rollout_recommendation')
              BINARY_OP               26 ([])

354           MAP_ADD                  1

377           LOAD_CONST              21 ('notes')
              LOAD_GLOBAL              5 (list + NULL)
              LOAD_FAST_BORROW         1 (s)
              LOAD_CONST              21 ('notes')
              BINARY_OP               26 ([])
              CALL                     1

354           MAP_ADD                  1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "app\services\memory\impact.py", line 385>:
385           RESUME                   0
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

Disassembly of <code object _coerce_since at 0x0000018C18060A50, file "app\services\memory\impact.py", line 385>:
385           RESUME                   0

386           LOAD_FAST_BORROW         0 (since)
              POP_JUMP_IF_NOT_NONE     3 (to L1)
              NOT_TAKEN

387           LOAD_CONST               0 (None)
              RETURN_VALUE

388   L1:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (since)
              LOAD_GLOBAL              2 (datetime)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       17 (to L2)
              NOT_TAKEN

389           LOAD_FAST_BORROW         0 (since)
              LOAD_ATTR                5 (isoformat + NULL|self)
              CALL                     0
              RETURN_VALUE

390   L2:     LOAD_GLOBAL              1 (isinstance + NULL)
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

391           LOAD_FAST_BORROW         0 (since)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              RETURN_VALUE

392   L3:     LOAD_CONST               0 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "app\services\memory\impact.py", line 395>:
395           RESUME                   0
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

Disassembly of <code object _clamp_brokerage_limit at 0x0000018C18010DF0, file "app\services\memory\impact.py", line 395>:
 395           RESUME                   0

 396           NOP

 397   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (limit)
               CALL                     1
               STORE_FAST               1 (n)

 400   L2:     LOAD_FAST                1 (n)
               LOAD_SMALL_INT           0
               COMPARE_OP              58 (bool(<=))
               POP_JUMP_IF_FALSE        7 (to L3)
               NOT_TAKEN

 401           LOAD_GLOBAL              6 (DEFAULT_BROKERAGE_LIMIT)
               RETURN_VALUE

 402   L3:     LOAD_GLOBAL              9 (min + NULL)
               LOAD_FAST                1 (n)
               LOAD_GLOBAL             10 (MAX_BROKERAGE_LIMIT)
               CALL                     2
               RETURN_VALUE

  --   L4:     PUSH_EXC_INFO

 398           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       10 (to L6)
               NOT_TAKEN
               POP_TOP

 399           LOAD_GLOBAL              6 (DEFAULT_BROKERAGE_LIMIT)
               SWAP                     2
       L5:     POP_EXCEPT
               RETURN_VALUE

 398   L6:     RERAISE                  0

  --   L7:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L4 [0]
  L4 to L5 -> L7 [1] lasti
  L6 to L7 -> L7 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025930, file "app\services\memory\impact.py", line 405>:
405           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

406           LOAD_CONST               2 ('str')

405           LOAD_CONST               3 ('since_iso')

408           LOAD_CONST               4 ('Optional[str]')

405           LOAD_CONST               5 ('total_cap')

409           LOAD_CONST               6 ('int')

405           LOAD_CONST               7 ('return')

410           LOAD_CONST               8 ('List[Dict[str, Any]]')

405           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object _fetch_brokerage_events at 0x0000018C17F75FD0, file "app\services\memory\impact.py", line 405>:
 405            RESUME                   0

 415            LOAD_FAST_BORROW         2 (total_cap)
                LOAD_SMALL_INT           0
                COMPARE_OP              58 (bool(<=))
                POP_JUMP_IF_FALSE        3 (to L1)
                NOT_TAKEN

 416            BUILD_LIST               0
                RETURN_VALUE

 418    L1:     BUILD_LIST               0
                STORE_FAST               3 (out)

 419            LOAD_GLOBAL              1 (max + NULL)

 420            LOAD_SMALL_INT           1

 421            LOAD_FAST_BORROW         2 (total_cap)
                LOAD_GLOBAL              3 (len + NULL)
                LOAD_GLOBAL              4 (TRACKED_EVENT_TYPES)
                CALL                     1
                BINARY_OP                0 (+)
                LOAD_SMALL_INT           1
                BINARY_OP               10 (-)
                LOAD_GLOBAL              3 (len + NULL)
                LOAD_GLOBAL              4 (TRACKED_EVENT_TYPES)
                CALL                     1
                BINARY_OP                2 (//)

 419            CALL                     2
                STORE_FAST               4 (per_type_cap)

 424            LOAD_GLOBAL              4 (TRACKED_EVENT_TYPES)
                GET_ITER
        L2:     FOR_ITER               163 (to L11)
                STORE_FAST               5 (event_type)

 425            LOAD_FAST                4 (per_type_cap)
                STORE_FAST               6 (remaining)

 426            LOAD_SMALL_INT           0
                STORE_FAST               7 (offset)

 427    L3:     LOAD_FAST_BORROW         6 (remaining)
                LOAD_SMALL_INT           0
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE      132 (to L9)
                NOT_TAKEN

 428            LOAD_GLOBAL              7 (min + NULL)
                LOAD_GLOBAL              8 (_EVENT_QUERY_MAX_LIMIT)
                LOAD_FAST_BORROW         6 (remaining)
                CALL                     2
                STORE_FAST               8 (page_size)

 429            NOP

 430    L4:     LOAD_GLOBAL             11 (recent_events + NULL)

 431            LOAD_FAST_BORROW         0 (brokerage_id)

 432            LOAD_FAST_BORROW         5 (event_type)

 433            LOAD_FAST_BORROW         1 (since_iso)

 434            LOAD_FAST_BORROW         8 (page_size)

 435            LOAD_FAST_BORROW         7 (offset)

 430            LOAD_CONST               1 (('brokerage_id', 'event_type', 'since_iso', 'limit', 'offset'))
                CALL_KW                  5
                STORE_FAST               9 (page)

 445    L5:     LOAD_FAST                9 (page)
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L6)
                NOT_TAKEN

 446            JUMP_FORWARD            89 (to L9)

 447    L6:     LOAD_FAST                3 (out)
                LOAD_ATTR               23 (extend + NULL|self)
                LOAD_FAST                9 (page)
                CALL                     1
                POP_TOP

 448            LOAD_FAST                7 (offset)
                LOAD_GLOBAL              3 (len + NULL)
                LOAD_FAST                9 (page)
                CALL                     1
                BINARY_OP               13 (+=)
                STORE_FAST               7 (offset)

 449            LOAD_FAST                6 (remaining)
                LOAD_GLOBAL              3 (len + NULL)
                LOAD_FAST                9 (page)
                CALL                     1
                BINARY_OP               23 (-=)
                STORE_FAST               6 (remaining)

 450            LOAD_GLOBAL              3 (len + NULL)
                LOAD_FAST                9 (page)
                CALL                     1
                LOAD_FAST                8 (page_size)
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        2 (to L7)
                NOT_TAKEN

 451            JUMP_FORWARD            19 (to L9)

 452    L7:     LOAD_GLOBAL              3 (len + NULL)
                LOAD_FAST                3 (out)
                CALL                     1
                LOAD_FAST                2 (total_cap)
                COMPARE_OP             188 (bool(>=))
                POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN
                JUMP_BACKWARD          137 (to L3)

 453    L8:     NOP

 454    L9:     LOAD_GLOBAL              3 (len + NULL)
                LOAD_FAST_BORROW         3 (out)
                CALL                     1
                LOAD_FAST_BORROW         2 (total_cap)
                COMPARE_OP             188 (bool(>=))
                POP_JUMP_IF_TRUE         3 (to L10)
                NOT_TAKEN
                JUMP_BACKWARD          163 (to L2)

 455   L10:     POP_TOP
                JUMP_FORWARD             2 (to L12)

 424   L11:     END_FOR
                POP_ITER

 457   L12:     LOAD_FAST_BORROW         3 (out)
                LOAD_CONST               3 (None)
                LOAD_FAST_BORROW         2 (total_cap)
                BINARY_SLICE
                RETURN_VALUE

  --   L13:     PUSH_EXC_INFO

 437            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       55 (to L17)
                NOT_TAKEN
                STORE_FAST              10 (e)

 438   L14:     LOAD_GLOBAL             14 (logger)
                LOAD_ATTR               17 (warning + NULL|self)

 439            LOAD_CONST               2 ('impact.brokerage page failed (non-critical) | brokerage=%s | event_type=%s | offset=%d | error_type=%s')

 442            LOAD_FAST_LOAD_FAST      5 (brokerage_id, event_type)
                LOAD_FAST                7 (offset)
                LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)

 438            CALL                     5
                POP_TOP

 444   L15:     POP_EXCEPT
                LOAD_CONST               3 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                JUMP_BACKWARD           87 (to L9)

  --   L16:     LOAD_CONST               3 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RERAISE                  1

 437   L17:     RERAISE                  0

  --   L18:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L4 to L5 -> L13 [1]
  L13 to L14 -> L18 [2] lasti
  L14 to L15 -> L16 [2] lasti
  L16 to L18 -> L18 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025D30, file "app\services\memory\impact.py", line 464>:
464           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

465           LOAD_CONST               2 ('str')

464           LOAD_CONST               3 ('since')

467           LOAD_CONST               4 ('Any')

464           LOAD_CONST               5 ('limit')

468           LOAD_CONST               6 ('int')

464           LOAD_CONST               7 ('return')

469           LOAD_CONST               8 ('Dict[str, Any]')

464           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object memory_impact_for_brokerage at 0x0000018C17F005F0, file "app\services\memory\impact.py", line 464>:
464           RESUME                   0

478           LOAD_GLOBAL              1 (isinstance + NULL)
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

480   L1:     LOAD_CONST               1 ('scope')
              LOAD_CONST               2 ('brokerage')

481           LOAD_CONST               3 ('brokerage_id')
              LOAD_CONST               4 ('')

482           LOAD_CONST               5 ('since')
              LOAD_CONST               6 (None)

483           LOAD_CONST               7 ('limit')
              LOAD_SMALL_INT           0

484           LOAD_CONST               8 ('error')
              LOAD_CONST               9 ('missing_brokerage_id')

485           LOAD_CONST              10 ('summary')
              LOAD_GLOBAL              7 (summarize_memory_impact + NULL)
              BUILD_LIST               0
              CALL                     1

479           BUILD_MAP                6
              RETURN_VALUE

488   L2:     LOAD_FAST_BORROW         0 (brokerage_id)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               3 (bid)

489           LOAD_GLOBAL              9 (_clamp_brokerage_limit + NULL)
              LOAD_FAST_BORROW         2 (limit)
              CALL                     1
              STORE_FAST               4 (capped)

490           LOAD_GLOBAL             11 (_coerce_since + NULL)
              LOAD_FAST_BORROW         1 (since)
              CALL                     1
              STORE_FAST               5 (since_iso)

492           LOAD_GLOBAL             13 (_fetch_brokerage_events + NULL)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 53 (bid, since_iso)
              LOAD_FAST_BORROW         4 (capped)
              LOAD_CONST              11 (('since_iso', 'total_cap'))
              CALL_KW                  3
              STORE_FAST               6 (rows)

493           LOAD_GLOBAL              7 (summarize_memory_impact + NULL)
              LOAD_FAST_BORROW         6 (rows)
              CALL                     1
              STORE_FAST               7 (summary)

496           LOAD_CONST               1 ('scope')
              LOAD_CONST               2 ('brokerage')

497           LOAD_CONST               3 ('brokerage_id')
              LOAD_FAST_BORROW         3 (bid)

498           LOAD_CONST               5 ('since')
              LOAD_FAST_BORROW         5 (since_iso)

499           LOAD_CONST               7 ('limit')
              LOAD_FAST_BORROW         4 (capped)

500           LOAD_CONST              12 ('events_read')
              LOAD_GLOBAL             15 (len + NULL)
              LOAD_FAST_BORROW         6 (rows)
              CALL                     1

501           LOAD_CONST              10 ('summary')
              LOAD_FAST_BORROW         7 (summary)

495           BUILD_MAP                6
              RETURN_VALUE
```
