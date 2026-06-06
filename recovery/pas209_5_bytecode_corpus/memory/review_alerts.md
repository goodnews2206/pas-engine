# memory/review_alerts

- **pyc:** `app\services\memory\__pycache__\review_alerts.cpython-314.pyc`
- **expected source path (absent):** `app\services\memory/review_alerts.py`
- **co_filename (from bytecode):** `app\services\memory\review_alerts.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** memory

## Module docstring

```
PAS155 — Memory review operator drift alerts (read-only, structural).

Layered over the same bounded, tenant-scoped reader pattern that
PAS150 / PAS151 / PAS152 / PAS153 / PAS154 use. Produces a closed-
shape list of *attention-directing signals* over the PAS144C
``pas_memory_review_events`` audit table — high approve/reject
rates, inactive actors, low decision volume, unknown actor
activity, and actor-type drift — so operators see WHERE to look
without first having to crunch the raw stats themselves.

Hard contract:
  * **Tenant-scoped.** Every public helper that touches Supabase
    requires ``brokerage_id``. There is no unscoped path.
  * **Bounded.** ``review_alerts_for_brokerage`` caps the row
    fetch at ``_MAX_ALERTS_LIMIT`` (500, mirrors PAS150 / PAS152 /
    PAS154). The query is ``WHERE brokerage_id = ? ORDER BY
    created_at DESC LIMIT n`` — NOT a full-table scan.
  * **Structural output only.** Each alert is a closed-shape
    dictionary with eight fixed fields (alert_type, severity,
    actor_id, actor_type, metric, value, threshold, message).
    Reason text, metadata JSONB, evidence, transcript, raw
    prompts and lineage are NEVER read or surfaced. The
    summariser physically does not look at those keys.
  * **No freeform messages.** Every ``message`` value is a fixed
    template string. Operator input never reaches the message.
  * **Fail-closed.** Bad input, reader failure, malformed event
    row — every path returns a structured envelope. Nothing in
    this module raises.
  * **Observability-only.** Alerts trigger no automatic action.
    The route never writes, the service never writes, the UI
    never wires an action handler off an alert.

Public surface:
  - summarize_review_alerts(events, *, now=None)        -> dict
  - review_alerts_for_brokerage(brokerage_id,
                                 since=None,
                                 limit=500)             -> dict
  - ALLOWED_ALERT_TYPES, ALLOWED_SEVERITIES,
    HIGH_RATE_THRESHOLD, HIGH_RATE_MIN_DECISIONS,
    LOW_VOLUME_THRESHOLD, INACTIVE_DAYS_THRESHOLD,
    _MAX_ALERTS_LIMIT
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `Tuple`, `__future__`, `annotations`, `app.db.supabase_client`, `date`, `datetime`, `get_supabase`, `logging`, `timedelta`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_clamp_limit`, `_coerce_since`, `_get_db`, `_list_review_events_for_brokerage`, `_make_alert`, `_parse_iso_day`, `_resolve_now_day`, `_round_rate`, `_safe_str`, `review_alerts_for_brokerage`, `summarize_review_alerts`

## Env-key candidates

`APPROVED`, `EXPIRED`, `QUARANTINED`, `REJECTED`, `UNKNOWN`

## String constants (redacted where noted)

- '\nPAS155 — Memory review operator drift alerts (read-only, structural).\n\nLayered over the same bounded, tenant-scoped reader pattern that\nPAS150 / PAS151 / PAS152 / PAS153 / PAS154 use. Produces a closed-\nshape list of *attention-directing signals* over the PAS144C\n``pas_memory_review_events`` audit table — high approve/reject\nrates, inactive actors, low decision volume, unknown actor\nactivity, and actor-type drift — so operators see WHERE to look\nwithout first having to crunch the raw stats themselves.\n\nHard contract:\n  * **Tenant-scoped.** Every public helper that touches Supabase\n    requires ``brokerage_id``. There is no unscoped path.\n  * **Bounded.** ``review_alerts_for_brokerage`` caps the row\n    fetch at ``_MAX_ALERTS_LIMIT`` (500, mirrors PAS150 / PAS152 /\n    PAS154). The query is ``WHERE brokerage_id = ? ORDER BY\n    created_at DESC LIMIT n`` — NOT a full-table scan.\n  * **Structural output only.** Each alert is a closed-shape\n    dictionary with eight fixed fields (alert_type, severity,\n    actor_id, actor_type, metric, value, threshold, message).\n    Reason text, metadata JSONB, evidence, transcript, raw\n    prompts and lineage are NEVER read or surfaced. The\n    summariser physically does not look at those keys.\n  * **No freeform messages.** Every ``message`` value is a fixed\n    template string. Operator input never reaches the message.\n  * **Fail-closed.** Bad input, reader failure, malformed event\n    row — every path returns a structured envelope. Nothing in\n    this module raises.\n  * **Observability-only.** Alerts trigger no automatic action.\n    The route never writes, the service never writes, the UI\n    never wires an action handler off an alert.\n\nPublic surface:\n  - summarize_review_alerts(events, *, now=None)        -> dict\n  - review_alerts_for_brokerage(brokerage_id,\n                                 since=None,\n                                 limit=500)             -> dict\n  - ALLOWED_ALERT_TYPES, ALLOWED_SEVERITIES,\n    HIGH_RATE_THRESHOLD, HIGH_RATE_MIN_DECISIONS,\n    LOW_VOLUME_THRESHOLD, INACTIVE_DAYS_THRESHOLD,\n    _MAX_ALERTS_LIMIT\n'
- 'pas.memory.review_alerts'
- 'warning'
- 'info'
- 'pas_memory_review_events'
- 'now'
- 'since'
- 'limit'
- 'val'
- 'Any'
- 'return'
- 'Optional[str]'
- 'Return a trimmed string for non-empty ``val`` or None.'
- 'num'
- 'int'
- 'denom'
- 'float'
- 'Return a 4-decimal rate (denom > 0 by caller invariant).'
- 'value'
- 'Extract the YYYY-MM-DD prefix from an ISO-8601 timestamp.\n\nReturns the validated day token or None on any malformed\ninput. Structural — does not handle timezone offsets; audit\nrows are stored UTC by Supabase contract.\n'
- 'str'
- "Resolve the 'today' anchor for the inactive-actor check.\n\n``now`` overrides the system clock for tests. Anything\nmalformed falls back to ``datetime.now(timezone.utc)``.\n"
- '%Y-%m-%d'
- 'Coerce a caller-supplied limit; clamp to [1, _MAX_ALERTS_LIMIT].'
- 'Tuple[Optional[str], Optional[str]]'
- 'Coerce caller-supplied ``since``. Mirrors review_stats /\nreview_export / review_actors.'
- 'alert_type'
- 'severity'
- 'actor_id'
- 'actor_type'
- 'metric'
- 'threshold'
- 'message'
- 'Dict[str, Any]'
- 'Construct a closed-shape alert dict.\n\nThe eight fields are fixed; the renderer in the UI and the\nJSON serialiser both rely on this shape. ``message`` is a\nfixed-template string — never a raw exception or freeform\noperator note. Pure, never raises.\n'
- 'events'
- 'Project a list of audit-event rows into a closed-shape\ndrift-alert envelope. Pure — no I/O, no logging, no raises.\n\nEach row is read for ONLY these keys: ``actor_id``,\n``actor_type``, ``to_status``, ``created_at``. Every other\nfield — ``reason``, ``metadata``, ``evidence``, ``transcript``,\n``review_id``, ``memory_id``, ``brokerage_id``, ``from_status``\n— is ignored on purpose.\n\nArgs:\n    events: list of audit-event row dicts.\n    now:    optional ISO-8601 day/timestamp override for the\n        inactive-actor cutoff. Defaults to\n        ``datetime.now(timezone.utc)``.\n\nReturns:\n    {\n        "status":      "ok",\n        "alert_count": <int>,\n        "alerts":      [<alert>, ...],\n        "warnings":    list[str],\n    }\n\nAlert ordering: severity desc (warning before info), then\n``alert_type`` asc, then ``actor_id`` asc. Stable for test\npinning.\n'
- 'status'
- 'alert_count'
- 'alerts'
- 'warnings'
- 'unexpected_events_shape'
- 'to_status'
- 'unknown'
- 'UNKNOWN'
- 'created_at'
- 'approved'
- 'rejected'
- 'expired'
- 'quarantined'
- 'total_decisions'
- 'last_seen'
- 'APPROVED'
- 'REJECTED'
- 'EXPIRED'
- 'QUARANTINED'
- 'unknown_status_events_ignored:'
- 'high_approve_rate'
- 'approve_rate'
- 'actor approve rate exceeds threshold'
- 'high_reject_rate'
- 'reject_rate'
- 'actor reject rate exceeds threshold'
- 'inactive_actor'
- 'actor inactive beyond threshold window'
- 'unknown_actor_activity'
- 'decisions logged under unknown actor identifier'
- 'actor_type_shift'
- 'distinct_actor_types'
- 'actor seen under multiple actor_type values'
- 'low_decision_volume'
- 'brokerage total decisions below threshold'
- 'Lazy Supabase resolver. Mirrors the other review_* modules.'
- 'brokerage_id'
- 'Tuple[List[Dict[str, Any]], List[str]]'
- 'Tenant-scoped, bounded fetch of audit-event rows.\n\nSELECT projection is exactly the four columns the summariser\nneeds (``actor_id, actor_type, to_status, created_at``). It\nexplicitly excludes ``metadata``, ``reason``, ``from_status``,\n``memory_id``, ``review_id``, ``brokerage_id``, ``evidence``,\n``transcript``, ``lineage``, ``memory_content``.\n\nReturns (rows, warnings). Never raises. Returns ([], [token])\non any Supabase failure.\n'
- 'actor_id, actor_type, to_status, created_at'
- 'data'
- 'review_alerts reader failed (non-critical) | brokerage='
- ' | error_type='
- 'reader_failed:'
- 'unexpected_reader_shape'
- 'result_truncated_at_limit'
- 'Return the closed-shape alert envelope for one tenant.\n\n``brokerage_id`` is REQUIRED. There is no path through this\nhelper that omits the tenant filter or falls back to a cross-\ntenant scan.\n\nResponse (always 200 from the route caller\'s perspective):\n    {\n        "status":       "ok" | "failed",\n        "brokerage_id": "<id>",\n        "since":        "<iso-8601 or null>",\n        "limit":        <int>,\n        "alert_count":  <int>,\n        "alerts":       [<alert row>, ...],\n        "warnings":     [<str>, ...],\n    }\n'
- 'failed'
- 'errors'
- 'missing_brokerage_id'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS155 — Memory review operator drift alerts (read-only, structural).\n\nLayered over the same bounded, tenant-scoped reader pattern that\nPAS150 / PAS151 / PAS152 / PAS153 / PAS154 use. Produces a closed-\nshape list of *attention-directing signals* over the PAS144C\n``pas_memory_review_events`` audit table — high approve/reject\nrates, inactive actors, low decision volume, unknown actor\nactivity, and actor-type drift — so operators see WHERE to look\nwithout first having to crunch the raw stats themselves.\n\nHard contract:\n  * **Tenant-scoped.** Every public helper that touches Supabase\n    requires ``brokerage_id``. There is no unscoped path.\n  * **Bounded.** ``review_alerts_for_brokerage`` caps the row\n    fetch at ``_MAX_ALERTS_LIMIT`` (500, mirrors PAS150 / PAS152 /\n    PAS154). The query is ``WHERE brokerage_id = ? ORDER BY\n    created_at DESC LIMIT n`` — NOT a full-table scan.\n  * **Structural output only.** Each alert is a closed-shape\n    dictionary with eight fixed fields (alert_type, severity,\n    actor_id, actor_type, metric, value, threshold, message).\n    Reason text, metadata JSONB, evidence, transcript, raw\n    prompts and lineage are NEVER read or surfaced. The\n    summariser physically does not look at those keys.\n  * **No freeform messages.** Every ``message`` value is a fixed\n    template string. Operator input never reaches the message.\n  * **Fail-closed.** Bad input, reader failure, malformed event\n    row — every path returns a structured envelope. Nothing in\n    this module raises.\n  * **Observability-only.** Alerts trigger no automatic action.\n    The route never writes, the service never writes, the UI\n    never wires an action handler off an alert.\n\nPublic surface:\n  - summarize_review_alerts(events, *, now=None)        -> dict\n  - review_alerts_for_brokerage(brokerage_id,\n                                 since=None,\n                                 limit=500)             -> dict\n  - ALLOWED_ALERT_TYPES, ALLOWED_SEVERITIES,\n    HIGH_RATE_THRESHOLD, HIGH_RATE_MIN_DECISIONS,\n    LOW_VOLUME_THRESHOLD, INACTIVE_DAYS_THRESHOLD,\n    _MAX_ALERTS_LIMIT\n')
              STORE_NAME               0 (__doc__)

 45           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 47           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 48           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('date', 'datetime', 'timedelta', 'timezone'))
              IMPORT_NAME              4 (datetime)
              IMPORT_FROM              5 (date)
              STORE_NAME               5 (date)
              IMPORT_FROM              4 (datetime)
              STORE_NAME               4 (datetime)
              IMPORT_FROM              6 (timedelta)
              STORE_NAME               6 (timedelta)
              IMPORT_FROM              7 (timezone)
              STORE_NAME               7 (timezone)
              POP_TOP

 49           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('Any', 'Dict', 'List', 'Optional', 'Tuple'))
              IMPORT_NAME              8 (typing)
              IMPORT_FROM              9 (Any)
              STORE_NAME               9 (Any)
              IMPORT_FROM             10 (Dict)
              STORE_NAME              10 (Dict)
              IMPORT_FROM             11 (List)
              STORE_NAME              11 (List)
              IMPORT_FROM             12 (Optional)
              STORE_NAME              12 (Optional)
              IMPORT_FROM             13 (Tuple)
              STORE_NAME              13 (Tuple)
              POP_TOP

 51           LOAD_NAME                3 (logging)
              LOAD_ATTR               28 (getLogger)
              PUSH_NULL
              LOAD_CONST               5 ('pas.memory.review_alerts')
              CALL                     1
              STORE_NAME              15 (logger)

 55           LOAD_CONST              35 (('APPROVED', 'REJECTED', 'EXPIRED', 'QUARANTINED'))
              STORE_NAME              16 (ALLOWED_TO_STATUSES)

 56           LOAD_CONST              36 (('OPERATOR', 'SYSTEM', 'ADMIN', 'SECURITY'))
              STORE_NAME              17 (ALLOWED_ACTOR_TYPES)

 61           LOAD_CONST              37 (('high_approve_rate', 'high_reject_rate', 'inactive_actor', 'low_decision_volume', 'unknown_actor_activity', 'actor_type_shift'))
              STORE_NAME              18 (ALLOWED_ALERT_TYPES)

 72           LOAD_CONST              38 (('warning', 'info'))
              STORE_NAME              19 (ALLOWED_SEVERITIES)

 76           LOAD_CONST               8 (0.9)
              STORE_NAME              20 (HIGH_RATE_THRESHOLD)

 77           LOAD_SMALL_INT          10
              STORE_NAME              21 (HIGH_RATE_MIN_DECISIONS)

 78           LOAD_SMALL_INT           3
              STORE_NAME              22 (LOW_VOLUME_THRESHOLD)

 79           LOAD_SMALL_INT           7
              STORE_NAME              23 (INACTIVE_DAYS_THRESHOLD)

 84           LOAD_CONST               9 (500)
              STORE_NAME              24 (_MAX_ALERTS_LIMIT)

 85           LOAD_CONST               9 (500)
              STORE_NAME              25 (_DEFAULT_ALERTS_LIMIT)

 87           LOAD_CONST              10 ('pas_memory_review_events')
              STORE_NAME              26 (_TABLE_REVIEW)

 91           LOAD_CONST               6 ('warning')
              LOAD_SMALL_INT           0
              LOAD_CONST               7 ('info')
              LOAD_SMALL_INT           1
              BUILD_MAP                2
              STORE_NAME              27 (_SEVERITY_RANK)

101           LOAD_CONST              11 (<code object __annotate__ at 0x0000018C17FA3870, file "app\services\memory\review_alerts.py", line 101>)
              MAKE_FUNCTION
              LOAD_CONST              12 (<code object _safe_str at 0x0000018C18038DF0, file "app\services\memory\review_alerts.py", line 101>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              28 (_safe_str)

109           LOAD_CONST              13 (<code object __annotate__ at 0x0000018C18024D30, file "app\services\memory\review_alerts.py", line 109>)
              MAKE_FUNCTION
              LOAD_CONST              14 (<code object _round_rate at 0x0000018C17FBFEE0, file "app\services\memory\review_alerts.py", line 109>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              29 (_round_rate)

116           LOAD_CONST              15 (<code object __annotate__ at 0x0000018C17FA2E20, file "app\services\memory\review_alerts.py", line 116>)
              MAKE_FUNCTION
              LOAD_CONST              16 (<code object _parse_iso_day at 0x0000018C17E89C20, file "app\services\memory\review_alerts.py", line 116>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              30 (_parse_iso_day)

141           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C17FA34B0, file "app\services\memory\review_alerts.py", line 141>)
              MAKE_FUNCTION
              LOAD_CONST              18 (<code object _resolve_now_day at 0x0000018C17FA92F0, file "app\services\memory\review_alerts.py", line 141>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              31 (_resolve_now_day)

154           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA2B50, file "app\services\memory\review_alerts.py", line 154>)
              MAKE_FUNCTION
              LOAD_CONST              20 (<code object _clamp_limit at 0x0000018C17FF0DB0, file "app\services\memory\review_alerts.py", line 154>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              32 (_clamp_limit)

167           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA2C40, file "app\services\memory\review_alerts.py", line 167>)
              MAKE_FUNCTION
              LOAD_CONST              22 (<code object _coerce_since at 0x0000018C1794EBB0, file "app\services\memory\review_alerts.py", line 167>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              33 (_coerce_since)

182           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C180C4250, file "app\services\memory\review_alerts.py", line 182>)
              MAKE_FUNCTION
              LOAD_CONST              24 (<code object _make_alert at 0x0000018C18025230, file "app\services\memory\review_alerts.py", line 182>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              34 (_make_alert)

216           LOAD_CONST              25 ('now')

219           LOAD_CONST               2 (None)

216           BUILD_MAP                1
              LOAD_CONST              26 (<code object __annotate__ at 0x0000018C18024B30, file "app\services\memory\review_alerts.py", line 216>)
              MAKE_FUNCTION
              LOAD_CONST              27 (<code object summarize_review_alerts at 0x0000018C17D7CF40, file "app\services\memory\review_alerts.py", line 216>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              35 (summarize_review_alerts)

448           LOAD_CONST              28 (<code object _get_db at 0x0000018C17FA21F0, file "app\services\memory\review_alerts.py", line 448>)
              MAKE_FUNCTION
              STORE_NAME              36 (_get_db)

454           LOAD_CONST              29 ('since')

457           LOAD_CONST               2 (None)

454           LOAD_CONST              30 ('limit')

458           LOAD_NAME               25 (_DEFAULT_ALERTS_LIMIT)

454           BUILD_MAP                2
              LOAD_CONST              31 (<code object __annotate__ at 0x0000018C18024E30, file "app\services\memory\review_alerts.py", line 454>)
              MAKE_FUNCTION
              LOAD_CONST              32 (<code object _list_review_events_for_brokerage at 0x0000018C17D78680, file "app\services\memory\review_alerts.py", line 454>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              37 (_list_review_events_for_brokerage)

505           LOAD_CONST               2 (None)

506           LOAD_NAME               25 (_DEFAULT_ALERTS_LIMIT)

503           BUILD_TUPLE              2
              LOAD_CONST              33 (<code object __annotate__ at 0x0000018C18025930, file "app\services\memory\review_alerts.py", line 503>)
              MAKE_FUNCTION
              LOAD_CONST              34 (<code object review_alerts_for_brokerage at 0x0000018C17D6DFC0, file "app\services\memory\review_alerts.py", line 503>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              38 (review_alerts_for_brokerage)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "app\services\memory\review_alerts.py", line 101>:
101           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('val')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _safe_str at 0x0000018C18038DF0, file "app\services\memory\review_alerts.py", line 101>:
101           RESUME                   0

103           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (val)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

104           LOAD_CONST               1 (None)
              RETURN_VALUE

105   L1:     LOAD_FAST_BORROW         0 (val)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

106           LOAD_FAST                1 (s)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 (None)
      L2:     RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024D30, file "app\services\memory\review_alerts.py", line 109>:
109           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('num')
              LOAD_CONST               2 ('int')
              LOAD_CONST               3 ('denom')
              LOAD_CONST               2 ('int')
              LOAD_CONST               4 ('return')
              LOAD_CONST               5 ('float')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _round_rate at 0x0000018C17FBFEE0, file "app\services\memory\review_alerts.py", line 109>:
109           RESUME                   0

111           LOAD_FAST_BORROW         1 (denom)
              LOAD_SMALL_INT           0
              COMPARE_OP              58 (bool(<=))
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN

112           LOAD_CONST               1 (0.0)
              RETURN_VALUE

113   L1:     LOAD_GLOBAL              1 (round + NULL)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (num, denom)
              BINARY_OP               11 (/)
              LOAD_SMALL_INT           4
              CALL                     2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "app\services\memory\review_alerts.py", line 116>:
116           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('value')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _parse_iso_day at 0x0000018C17E89C20, file "app\services\memory\review_alerts.py", line 116>:
 116            RESUME                   0

 123            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (value)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN

 124            LOAD_CONST               1 (None)
                RETURN_VALUE

 125    L1:     LOAD_FAST_BORROW         0 (value)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                STORE_FAST               1 (s)

 126            LOAD_GLOBAL              7 (len + NULL)
                LOAD_FAST_BORROW         1 (s)
                CALL                     1
                LOAD_SMALL_INT          10
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        3 (to L2)
                NOT_TAKEN

 127            LOAD_CONST               1 (None)
                RETURN_VALUE

 128    L2:     LOAD_FAST_BORROW         1 (s)
                LOAD_CONST               2 (slice(None, 10, None))
                BINARY_OP               26 ([])
                STORE_FAST               2 (head)

 129            LOAD_FAST_BORROW         2 (head)
                LOAD_SMALL_INT           4
                BINARY_OP               26 ([])
                LOAD_CONST               3 ('-')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_TRUE        15 (to L3)
                NOT_TAKEN
                LOAD_FAST_BORROW         2 (head)
                LOAD_SMALL_INT           7
                BINARY_OP               26 ([])
                LOAD_CONST               3 ('-')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE        3 (to L4)
                NOT_TAKEN

 130    L3:     LOAD_CONST               1 (None)
                RETURN_VALUE

 131    L4:     NOP

 132    L5:     LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST_BORROW         2 (head)
                LOAD_CONST               4 (slice(0, 4, None))
                BINARY_OP               26 ([])
                CALL                     1
                STORE_FAST               3 (y)

 133            LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST_BORROW         2 (head)
                LOAD_CONST               5 (slice(5, 7, None))
                BINARY_OP               26 ([])
                CALL                     1
                STORE_FAST               4 (m)

 134            LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST_BORROW         2 (head)
                LOAD_CONST               6 (slice(8, 10, None))
                BINARY_OP               26 ([])
                CALL                     1
                STORE_FAST               5 (d)

 135            LOAD_GLOBAL             11 (date + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (y, m)
                LOAD_FAST_BORROW         5 (d)
                CALL                     3
                POP_TOP

 138    L6:     LOAD_FAST_BORROW         2 (head)
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

 136            LOAD_GLOBAL             12 (ValueError)
                LOAD_GLOBAL             14 (TypeError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L9)
                NOT_TAKEN
                POP_TOP

 137    L8:     POP_EXCEPT
                LOAD_CONST               1 (None)
                RETURN_VALUE

 136    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L5 to L6 -> L7 [0]
  L7 to L8 -> L10 [1] lasti
  L9 to L10 -> L10 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "app\services\memory\review_alerts.py", line 141>:
141           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('now')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _resolve_now_day at 0x0000018C17FA92F0, file "app\services\memory\review_alerts.py", line 141>:
141           RESUME                   0

147           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (now)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       22 (to L1)
              NOT_TAKEN

148           LOAD_GLOBAL              5 (_parse_iso_day + NULL)
              LOAD_FAST_BORROW         0 (now)
              CALL                     1
              STORE_FAST               1 (parsed)

149           LOAD_FAST_BORROW         1 (parsed)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN

150           LOAD_FAST_BORROW         1 (parsed)
              RETURN_VALUE

151   L1:     LOAD_GLOBAL              6 (datetime)
              LOAD_ATTR                8 (now)
              PUSH_NULL
              LOAD_GLOBAL             10 (timezone)
              LOAD_ATTR               12 (utc)
              CALL                     1
              LOAD_ATTR               15 (strftime + NULL|self)
              LOAD_CONST               1 ('%Y-%m-%d')
              CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "app\services\memory\review_alerts.py", line 154>:
154           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('value')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('int')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _clamp_limit at 0x0000018C17FF0DB0, file "app\services\memory\review_alerts.py", line 154>:
 154           RESUME                   0

 156           LOAD_FAST_BORROW         0 (value)
               POP_JUMP_IF_NOT_NONE     7 (to L1)
               NOT_TAKEN

 157           LOAD_GLOBAL              0 (_DEFAULT_ALERTS_LIMIT)
               RETURN_VALUE

 158   L1:     NOP

 159   L2:     LOAD_GLOBAL              3 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               1 (n)

 162   L3:     LOAD_FAST                1 (n)
               LOAD_SMALL_INT           0
               COMPARE_OP              58 (bool(<=))
               POP_JUMP_IF_FALSE        7 (to L4)
               NOT_TAKEN

 163           LOAD_GLOBAL              0 (_DEFAULT_ALERTS_LIMIT)
               RETURN_VALUE

 164   L4:     LOAD_GLOBAL              9 (min + NULL)
               LOAD_FAST                1 (n)
               LOAD_GLOBAL             10 (_MAX_ALERTS_LIMIT)
               CALL                     2
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 160           LOAD_GLOBAL              4 (TypeError)
               LOAD_GLOBAL              6 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       10 (to L7)
               NOT_TAKEN
               POP_TOP

 161           LOAD_GLOBAL              0 (_DEFAULT_ALERTS_LIMIT)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

 160   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "app\services\memory\review_alerts.py", line 167>:
167           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('value')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Tuple[Optional[str], Optional[str]]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _coerce_since at 0x0000018C1794EBB0, file "app\services\memory\review_alerts.py", line 167>:
167           RESUME                   0

170           LOAD_FAST_BORROW         0 (value)
              POP_JUMP_IF_NOT_NONE     3 (to L1)
              NOT_TAKEN

171           LOAD_CONST               4 ((None, None))
              RETURN_VALUE

172   L1:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

173           LOAD_CONST               5 ((None, 'since_ignored_non_string'))
              RETURN_VALUE

174   L2:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

175           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN

176           LOAD_CONST               4 ((None, None))
              RETURN_VALUE

177   L3:     LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         1 (s)
              CALL                     1
              LOAD_SMALL_INT          10
              COMPARE_OP              18 (bool(<))
              POP_JUMP_IF_TRUE        44 (to L4)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (s)
              LOAD_CONST               2 (slice(None, 4, None))
              BINARY_OP               26 ([])
              LOAD_ATTR                9 (isdigit + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_FALSE       15 (to L4)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (s)
              LOAD_SMALL_INT           4
              BINARY_OP               26 ([])
              LOAD_CONST               3 ('-')
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN

178   L4:     LOAD_CONST               6 ((None, 'since_ignored_invalid_format'))
              RETURN_VALUE

179   L5:     LOAD_FAST_BORROW         1 (s)
              LOAD_CONST               1 (None)
              BUILD_TUPLE              2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180C4250, file "app\services\memory\review_alerts.py", line 182>:
182           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('alert_type')

184           LOAD_CONST               2 ('str')

182           LOAD_CONST               3 ('severity')

185           LOAD_CONST               2 ('str')

182           LOAD_CONST               4 ('actor_id')

186           LOAD_CONST               2 ('str')

182           LOAD_CONST               5 ('actor_type')

187           LOAD_CONST               2 ('str')

182           LOAD_CONST               6 ('metric')

188           LOAD_CONST               2 ('str')

182           LOAD_CONST               7 ('value')

189           LOAD_CONST               8 ('Any')

182           LOAD_CONST               9 ('threshold')

190           LOAD_CONST               8 ('Any')

182           LOAD_CONST              10 ('message')

191           LOAD_CONST               2 ('str')

182           LOAD_CONST              11 ('return')

192           LOAD_CONST              12 ('Dict[str, Any]')

182           BUILD_MAP                9
              RETURN_VALUE

Disassembly of <code object _make_alert at 0x0000018C18025230, file "app\services\memory\review_alerts.py", line 182>:
182           RESUME                   0

201           LOAD_CONST               1 ('alert_type')
              LOAD_FAST_BORROW         0 (alert_type)

202           LOAD_CONST               2 ('severity')
              LOAD_FAST_BORROW         1 (severity)

203           LOAD_CONST               3 ('actor_id')
              LOAD_FAST_BORROW         2 (actor_id)

204           LOAD_CONST               4 ('actor_type')
              LOAD_FAST_BORROW         3 (actor_type)

205           LOAD_CONST               5 ('metric')
              LOAD_FAST_BORROW         4 (metric)

206           LOAD_CONST               6 ('value')
              LOAD_FAST_BORROW         5 (value)

207           LOAD_CONST               7 ('threshold')
              LOAD_FAST_BORROW         6 (threshold)

208           LOAD_CONST               8 ('message')
              LOAD_FAST_BORROW         7 (message)

200           BUILD_MAP                8
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024B30, file "app\services\memory\review_alerts.py", line 216>:
216           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('events')

217           LOAD_CONST               2 ('Any')

216           LOAD_CONST               3 ('now')

219           LOAD_CONST               4 ('Optional[str]')

216           LOAD_CONST               5 ('return')

220           LOAD_CONST               6 ('Dict[str, Any]')

216           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object summarize_review_alerts at 0x0000018C17D7CF40, file "app\services\memory\review_alerts.py", line 216>:
216            RESUME                   0

249            LOAD_CONST               1 ('status')
               LOAD_CONST               2 ('ok')

250            LOAD_CONST               3 ('alert_count')
               LOAD_SMALL_INT           0

251            LOAD_CONST               4 ('alerts')
               BUILD_LIST               0

252            LOAD_CONST               5 ('warnings')
               BUILD_LIST               0

248            BUILD_MAP                4
               STORE_FAST               2 (summary)

255            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (events)
               LOAD_GLOBAL              2 (list)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        27 (to L1)
               NOT_TAKEN

256            LOAD_FAST_BORROW         2 (summary)
               LOAD_CONST               5 ('warnings')
               BINARY_OP               26 ([])
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_CONST               6 ('unexpected_events_shape')
               CALL                     1
               POP_TOP

257            LOAD_FAST_BORROW         2 (summary)
               RETURN_VALUE

260    L1:     LOAD_GLOBAL              7 (_resolve_now_day + NULL)
               LOAD_FAST_BORROW         1 (now)
               CALL                     1
               STORE_FAST               3 (now_day_token)

261            LOAD_GLOBAL              9 (date + NULL)

262            LOAD_GLOBAL             11 (int + NULL)
               LOAD_FAST_BORROW         3 (now_day_token)
               LOAD_CONST               7 (slice(0, 4, None))
               BINARY_OP               26 ([])
               CALL                     1

263            LOAD_GLOBAL             11 (int + NULL)
               LOAD_FAST_BORROW         3 (now_day_token)
               LOAD_CONST               8 (slice(5, 7, None))
               BINARY_OP               26 ([])
               CALL                     1

264            LOAD_GLOBAL             11 (int + NULL)
               LOAD_FAST_BORROW         3 (now_day_token)
               LOAD_CONST               9 (slice(8, 10, None))
               BINARY_OP               26 ([])
               CALL                     1

261            CALL                     3
               STORE_FAST               4 (today)

266            LOAD_FAST_BORROW         4 (today)
               LOAD_GLOBAL             13 (timedelta + NULL)
               LOAD_GLOBAL             14 (INACTIVE_DAYS_THRESHOLD)
               LOAD_CONST              10 (('days',))
               CALL_KW                  1
               BINARY_OP               10 (-)
               LOAD_ATTR               17 (strftime + NULL|self)
               LOAD_CONST              11 ('%Y-%m-%d')
               CALL                     1
               STORE_FAST               5 (cutoff_day)

271            BUILD_MAP                0
               STORE_FAST               6 (buckets)

275            BUILD_MAP                0
               STORE_FAST               7 (actor_types_seen)

277            LOAD_SMALL_INT           0
               STORE_FAST               8 (unknown_statuses_seen)

279            LOAD_FAST_BORROW         0 (events)
               GET_ITER
       L2:     EXTENDED_ARG             1
               FOR_ITER               451 (to L15)
               STORE_FAST               9 (raw)

280            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         9 (raw)
               LOAD_GLOBAL             18 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        12 (to L3)
               NOT_TAKEN

281            LOAD_FAST_BORROW         8 (unknown_statuses_seen)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               8 (unknown_statuses_seen)

282            JUMP_BACKWARD           37 (to L2)

283    L3:     LOAD_GLOBAL             21 (_safe_str + NULL)
               LOAD_FAST_BORROW         9 (raw)
               LOAD_ATTR               23 (get + NULL|self)
               LOAD_CONST              12 ('to_status')
               CALL                     1
               CALL                     1
               STORE_FAST              10 (to_status)

284            LOAD_FAST_BORROW        10 (to_status)
               LOAD_GLOBAL             24 (ALLOWED_TO_STATUSES)
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_FALSE       12 (to L4)
               NOT_TAKEN

285            LOAD_FAST_BORROW         8 (unknown_statuses_seen)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               8 (unknown_statuses_seen)

286            JUMP_BACKWARD           85 (to L2)

288    L4:     LOAD_GLOBAL             21 (_safe_str + NULL)
               LOAD_FAST_BORROW         9 (raw)
               LOAD_ATTR               23 (get + NULL|self)
               LOAD_CONST              13 ('actor_id')
               CALL                     1
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              14 ('unknown')
       L5:     STORE_FAST              11 (actor_id)

289            LOAD_GLOBAL             21 (_safe_str + NULL)
               LOAD_FAST_BORROW         9 (raw)
               LOAD_ATTR               23 (get + NULL|self)
               LOAD_CONST              15 ('actor_type')
               CALL                     1
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L6)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              16 ('UNKNOWN')
       L6:     STORE_FAST              12 (actor_type)

290            LOAD_GLOBAL             21 (_safe_str + NULL)
               LOAD_FAST_BORROW         9 (raw)
               LOAD_ATTR               23 (get + NULL|self)
               LOAD_CONST              17 ('created_at')
               CALL                     1
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L7)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              18 ('')
       L7:     STORE_FAST              13 (created_at)

292            LOAD_FAST_BORROW_LOAD_FAST_BORROW 188 (actor_id, actor_type)
               BUILD_TUPLE              2
               STORE_FAST              14 (key)

293            LOAD_FAST_BORROW         6 (buckets)
               LOAD_ATTR               23 (get + NULL|self)
               LOAD_FAST_BORROW        14 (key)
               CALL                     1
               STORE_FAST              15 (bucket)

294            LOAD_FAST_BORROW        15 (bucket)
               POP_JUMP_IF_NOT_NONE    23 (to L8)
               NOT_TAKEN

296            LOAD_CONST              13 ('actor_id')
               LOAD_FAST_BORROW        11 (actor_id)

297            LOAD_CONST              15 ('actor_type')
               LOAD_FAST_BORROW        12 (actor_type)

298            LOAD_CONST              20 ('approved')
               LOAD_SMALL_INT           0

299            LOAD_CONST              21 ('rejected')
               LOAD_SMALL_INT           0

300            LOAD_CONST              22 ('expired')
               LOAD_SMALL_INT           0

301            LOAD_CONST              23 ('quarantined')
               LOAD_SMALL_INT           0

302            LOAD_CONST              24 ('total_decisions')
               LOAD_SMALL_INT           0

303            LOAD_CONST              25 ('last_seen')
               LOAD_CONST              18 ('')

295            BUILD_MAP                8
               STORE_FAST              15 (bucket)

305            LOAD_FAST_BORROW_LOAD_FAST_BORROW 246 (bucket, buckets)
               LOAD_FAST_BORROW        14 (key)
               STORE_SUBSCR

307    L8:     LOAD_FAST_BORROW        10 (to_status)
               LOAD_CONST              26 ('APPROVED')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       23 (to L9)
               NOT_TAKEN

308            LOAD_FAST_BORROW        15 (bucket)
               LOAD_CONST              20 ('approved')
               COPY                     2
               COPY                     2
               BINARY_OP               26 ([])
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               SWAP                     3
               SWAP                     2
               STORE_SUBSCR
               JUMP_FORWARD            86 (to L12)

309    L9:     LOAD_FAST_BORROW        10 (to_status)
               LOAD_CONST              27 ('REJECTED')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       23 (to L10)
               NOT_TAKEN

310            LOAD_FAST_BORROW        15 (bucket)
               LOAD_CONST              21 ('rejected')
               COPY                     2
               COPY                     2
               BINARY_OP               26 ([])
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               SWAP                     3
               SWAP                     2
               STORE_SUBSCR
               JUMP_FORWARD            57 (to L12)

311   L10:     LOAD_FAST_BORROW        10 (to_status)
               LOAD_CONST              28 ('EXPIRED')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       23 (to L11)
               NOT_TAKEN

312            LOAD_FAST_BORROW        15 (bucket)
               LOAD_CONST              22 ('expired')
               COPY                     2
               COPY                     2
               BINARY_OP               26 ([])
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               SWAP                     3
               SWAP                     2
               STORE_SUBSCR
               JUMP_FORWARD            28 (to L12)

313   L11:     LOAD_FAST_BORROW        10 (to_status)
               LOAD_CONST              29 ('QUARANTINED')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       22 (to L12)
               NOT_TAKEN

314            LOAD_FAST_BORROW        15 (bucket)
               LOAD_CONST              23 ('quarantined')
               COPY                     2
               COPY                     2
               BINARY_OP               26 ([])
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               SWAP                     3
               SWAP                     2
               STORE_SUBSCR

315   L12:     LOAD_FAST_BORROW        15 (bucket)
               LOAD_CONST              24 ('total_decisions')
               COPY                     2
               COPY                     2
               BINARY_OP               26 ([])
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               SWAP                     3
               SWAP                     2
               STORE_SUBSCR

320            LOAD_FAST_BORROW        13 (created_at)
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L13)
               NOT_TAKEN
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 223 (created_at, bucket)
               LOAD_CONST              25 ('last_seen')
               BINARY_OP               26 ([])
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        5 (to L13)
               NOT_TAKEN

321            LOAD_FAST_BORROW_LOAD_FAST_BORROW 223 (created_at, bucket)
               LOAD_CONST              25 ('last_seen')
               STORE_SUBSCR

326   L13:     LOAD_FAST_BORROW        11 (actor_id)
               LOAD_CONST              14 ('unknown')
               COMPARE_OP             119 (bool(!=))
               POP_JUMP_IF_TRUE         4 (to L14)
               NOT_TAKEN
               EXTENDED_ARG             1
               JUMP_BACKWARD          410 (to L2)

327   L14:     LOAD_FAST_BORROW         7 (actor_types_seen)
               LOAD_ATTR               27 (setdefault + NULL|self)
               LOAD_FAST_BORROW        11 (actor_id)
               LOAD_GLOBAL             29 (set + NULL)
               CALL                     0
               CALL                     2
               LOAD_ATTR               31 (add + NULL|self)
               LOAD_FAST_BORROW        12 (actor_type)
               CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          454 (to L2)

279   L15:     END_FOR
               POP_ITER

329            LOAD_FAST_BORROW         8 (unknown_statuses_seen)
               TO_BOOL
               POP_JUMP_IF_FALSE       28 (to L16)
               NOT_TAKEN

330            LOAD_FAST_BORROW         2 (summary)
               LOAD_CONST               5 ('warnings')
               BINARY_OP               26 ([])
               LOAD_ATTR                5 (append + NULL|self)

331            LOAD_CONST              30 ('unknown_status_events_ignored:')
               LOAD_FAST_BORROW         8 (unknown_statuses_seen)
               FORMAT_SIMPLE
               BUILD_STRING             2

330            CALL                     1
               POP_TOP

334   L16:     LOAD_GLOBAL             33 (sum + NULL)
               LOAD_CONST              31 (<code object <genexpr> at 0x0000018C180C4580, file "app\services\memory\review_alerts.py", line 334>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         6 (buckets)
               LOAD_ATTR               35 (values + NULL|self)
               CALL                     0
               GET_ITER
               CALL                     0
               CALL                     1
               STORE_FAST              16 (total_events)

336            BUILD_LIST               0
               STORE_FAST              17 (alerts)

339            LOAD_FAST_BORROW         6 (buckets)
               LOAD_ATTR               35 (values + NULL|self)
               CALL                     0
               GET_ITER
      L17:     EXTENDED_ARG             1
               FOR_ITER               345 (to L22)
               STORE_FAST              15 (bucket)

340            LOAD_FAST_BORROW        15 (bucket)
               LOAD_CONST              24 ('total_decisions')
               BINARY_OP               26 ([])
               STORE_FAST              18 (total)

343            LOAD_FAST_BORROW        18 (total)
               LOAD_GLOBAL             36 (HIGH_RATE_MIN_DECISIONS)
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE      166 (to L19)
               NOT_TAKEN

344            LOAD_GLOBAL             39 (_round_rate + NULL)
               LOAD_FAST_BORROW        15 (bucket)
               LOAD_CONST              20 ('approved')
               BINARY_OP               26 ([])
               LOAD_FAST_BORROW        18 (total)
               CALL                     2
               STORE_FAST              19 (approve_rate)

345            LOAD_GLOBAL             39 (_round_rate + NULL)
               LOAD_FAST_BORROW        15 (bucket)
               LOAD_CONST              21 ('rejected')
               BINARY_OP               26 ([])
               LOAD_FAST_BORROW        18 (total)
               CALL                     2
               STORE_FAST              20 (reject_rate)

346            LOAD_FAST_BORROW        19 (approve_rate)
               LOAD_GLOBAL             40 (HIGH_RATE_THRESHOLD)
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE       54 (to L18)
               NOT_TAKEN

347            LOAD_FAST_BORROW        17 (alerts)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_GLOBAL             43 (_make_alert + NULL)

348            LOAD_CONST              32 ('high_approve_rate')

349            LOAD_CONST              33 ('warning')

350            LOAD_FAST_BORROW        15 (bucket)
               LOAD_CONST              13 ('actor_id')
               BINARY_OP               26 ([])

351            LOAD_FAST_BORROW        15 (bucket)
               LOAD_CONST              15 ('actor_type')
               BINARY_OP               26 ([])

352            LOAD_CONST              34 ('approve_rate')

353            LOAD_FAST_BORROW        19 (approve_rate)

354            LOAD_GLOBAL             40 (HIGH_RATE_THRESHOLD)

355            LOAD_CONST              35 ('actor approve rate exceeds threshold')

347            LOAD_CONST              36 (('alert_type', 'severity', 'actor_id', 'actor_type', 'metric', 'value', 'threshold', 'message'))
               CALL_KW                  8
               CALL                     1
               POP_TOP
               JUMP_FORWARD            63 (to L19)

357   L18:     LOAD_FAST_BORROW        20 (reject_rate)
               LOAD_GLOBAL             40 (HIGH_RATE_THRESHOLD)
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE       53 (to L19)
               NOT_TAKEN

358            LOAD_FAST_BORROW        17 (alerts)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_GLOBAL             43 (_make_alert + NULL)

359            LOAD_CONST              37 ('high_reject_rate')

360            LOAD_CONST              33 ('warning')

361            LOAD_FAST_BORROW        15 (bucket)
               LOAD_CONST              13 ('actor_id')
               BINARY_OP               26 ([])

362            LOAD_FAST_BORROW        15 (bucket)
               LOAD_CONST              15 ('actor_type')
               BINARY_OP               26 ([])

363            LOAD_CONST              38 ('reject_rate')

364            LOAD_FAST_BORROW        20 (reject_rate)

365            LOAD_GLOBAL             40 (HIGH_RATE_THRESHOLD)

366            LOAD_CONST              39 ('actor reject rate exceeds threshold')

358            LOAD_CONST              36 (('alert_type', 'severity', 'actor_id', 'actor_type', 'metric', 'value', 'threshold', 'message'))
               CALL_KW                  8
               CALL                     1
               POP_TOP

371   L19:     LOAD_GLOBAL             45 (_parse_iso_day + NULL)
               LOAD_FAST_BORROW        15 (bucket)
               LOAD_CONST              25 ('last_seen')
               BINARY_OP               26 ([])
               CALL                     1
               STORE_FAST              21 (last_seen_day)

372            LOAD_FAST_BORROW        21 (last_seen_day)
               POP_JUMP_IF_NONE        56 (to L20)
               NOT_TAKEN
               LOAD_FAST_BORROW        21 (last_seen_day)
               LOAD_FAST_BORROW         5 (cutoff_day)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       49 (to L20)
               NOT_TAKEN

373            LOAD_FAST_BORROW        17 (alerts)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_GLOBAL             43 (_make_alert + NULL)

374            LOAD_CONST              40 ('inactive_actor')

375            LOAD_CONST              41 ('info')

376            LOAD_FAST_BORROW        15 (bucket)
               LOAD_CONST              13 ('actor_id')
               BINARY_OP               26 ([])

377            LOAD_FAST_BORROW        15 (bucket)
               LOAD_CONST              15 ('actor_type')
               BINARY_OP               26 ([])

378            LOAD_CONST              25 ('last_seen')

379            LOAD_FAST_BORROW        21 (last_seen_day)

380            LOAD_FAST_BORROW         5 (cutoff_day)

381            LOAD_CONST              42 ('actor inactive beyond threshold window')

373            LOAD_CONST              36 (('alert_type', 'severity', 'actor_id', 'actor_type', 'metric', 'value', 'threshold', 'message'))
               CALL_KW                  8
               CALL                     1
               POP_TOP

386   L20:     LOAD_FAST_BORROW        15 (bucket)
               LOAD_CONST              13 ('actor_id')
               BINARY_OP               26 ([])
               LOAD_CONST              14 ('unknown')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_TRUE        18 (to L21)
               NOT_TAKEN
               LOAD_FAST_BORROW        15 (bucket)
               LOAD_CONST              15 ('actor_type')
               BINARY_OP               26 ([])
               LOAD_CONST              16 ('UNKNOWN')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_TRUE         4 (to L21)
               NOT_TAKEN
               EXTENDED_ARG             1
               JUMP_BACKWARD          297 (to L17)

387   L21:     LOAD_FAST_BORROW        17 (alerts)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_GLOBAL             43 (_make_alert + NULL)

388            LOAD_CONST              43 ('unknown_actor_activity')

389            LOAD_CONST              33 ('warning')

390            LOAD_FAST_BORROW        15 (bucket)
               LOAD_CONST              13 ('actor_id')
               BINARY_OP               26 ([])

391            LOAD_FAST_BORROW        15 (bucket)
               LOAD_CONST              15 ('actor_type')
               BINARY_OP               26 ([])

392            LOAD_CONST              24 ('total_decisions')

393            LOAD_FAST_BORROW        18 (total)

394            LOAD_CONST              19 (None)

395            LOAD_CONST              44 ('decisions logged under unknown actor identifier')

387            LOAD_CONST              36 (('alert_type', 'severity', 'actor_id', 'actor_type', 'metric', 'value', 'threshold', 'message'))
               CALL_KW                  8
               CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          348 (to L17)

339   L22:     END_FOR
               POP_ITER

402            LOAD_FAST_BORROW         7 (actor_types_seen)
               LOAD_ATTR               47 (items + NULL|self)
               CALL                     0
               GET_ITER
      L23:     FOR_ITER                67 (to L25)
               UNPACK_SEQUENCE          2
               STORE_FAST              11 (actor_id)
               STORE_FAST              22 (types)

403            LOAD_GLOBAL             49 (len + NULL)
               LOAD_FAST_BORROW        22 (types)
               CALL                     1
               LOAD_SMALL_INT           1
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_TRUE         3 (to L24)
               NOT_TAKEN
               JUMP_BACKWARD           24 (to L23)

404   L24:     LOAD_FAST_BORROW        17 (alerts)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_GLOBAL             43 (_make_alert + NULL)

405            LOAD_CONST              45 ('actor_type_shift')

406            LOAD_CONST              33 ('warning')

407            LOAD_FAST_BORROW        11 (actor_id)

408            LOAD_CONST              18 ('')

409            LOAD_CONST              46 ('distinct_actor_types')

410            LOAD_GLOBAL             49 (len + NULL)
               LOAD_FAST_BORROW        22 (types)
               CALL                     1

411            LOAD_SMALL_INT           1

412            LOAD_CONST              47 ('actor seen under multiple actor_type values')

404            LOAD_CONST              36 (('alert_type', 'severity', 'actor_id', 'actor_type', 'metric', 'value', 'threshold', 'message'))
               CALL_KW                  8
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           69 (to L23)

402   L25:     END_FOR
               POP_ITER

419            LOAD_SMALL_INT           0
               LOAD_FAST               16 (total_events)
               SWAP                     2
               COPY                     2
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       12 (to L26)
               NOT_TAKEN
               LOAD_GLOBAL             50 (LOW_VOLUME_THRESHOLD)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       42 (to L28)
               NOT_TAKEN
               JUMP_FORWARD             2 (to L27)
      L26:     POP_TOP
               JUMP_FORWARD            38 (to L28)

420   L27:     LOAD_FAST_BORROW        17 (alerts)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_GLOBAL             43 (_make_alert + NULL)

421            LOAD_CONST              48 ('low_decision_volume')

422            LOAD_CONST              41 ('info')

423            LOAD_CONST              18 ('')

424            LOAD_CONST              18 ('')

425            LOAD_CONST              24 ('total_decisions')

426            LOAD_FAST_BORROW        16 (total_events)

427            LOAD_GLOBAL             50 (LOW_VOLUME_THRESHOLD)

428            LOAD_CONST              49 ('brokerage total decisions below threshold')

420            LOAD_CONST              36 (('alert_type', 'severity', 'actor_id', 'actor_type', 'metric', 'value', 'threshold', 'message'))
               CALL_KW                  8
               CALL                     1
               POP_TOP

433   L28:     LOAD_FAST_BORROW        17 (alerts)
               LOAD_ATTR               53 (sort + NULL|self)
               LOAD_CONST              50 (<code object <lambda> at 0x0000018C17C49B80, file "app\services\memory\review_alerts.py", line 433>)
               MAKE_FUNCTION
               LOAD_CONST              51 (('key',))
               CALL_KW                  1
               POP_TOP

439            LOAD_FAST_BORROW        17 (alerts)
               LOAD_FAST_BORROW         2 (summary)
               LOAD_CONST               4 ('alerts')
               STORE_SUBSCR

440            LOAD_GLOBAL             49 (len + NULL)
               LOAD_FAST_BORROW        17 (alerts)
               CALL                     1
               LOAD_FAST_BORROW         2 (summary)
               LOAD_CONST               3 ('alert_count')
               STORE_SUBSCR

441            LOAD_FAST_BORROW         2 (summary)
               RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C180C4580, file "app\services\memory\review_alerts.py", line 334>:
 334           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                13 (to L3)
               STORE_FAST_LOAD_FAST    17 (b, b)
               LOAD_CONST               0 ('total_decisions')
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

Disassembly of <code object <lambda> at 0x0000018C17C49B80, file "app\services\memory\review_alerts.py", line 433>:
433           RESUME                   0

434           LOAD_GLOBAL              0 (_SEVERITY_RANK)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_FAST_BORROW         0 (a)
              LOAD_CONST               0 ('severity')
              BINARY_OP               26 ([])
              LOAD_SMALL_INT          99
              CALL                     2

435           LOAD_FAST_BORROW         0 (a)
              LOAD_CONST               1 ('alert_type')
              BINARY_OP               26 ([])

436           LOAD_FAST_BORROW         0 (a)
              LOAD_CONST               2 ('actor_id')
              BINARY_OP               26 ([])

433           BUILD_TUPLE              3
              RETURN_VALUE

Disassembly of <code object _get_db at 0x0000018C17FA21F0, file "app\services\memory\review_alerts.py", line 448>:
448           RESUME                   0

450           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('get_supabase',))
              IMPORT_NAME              0 (app.db.supabase_client)
              IMPORT_FROM              1 (get_supabase)
              STORE_FAST               0 (get_supabase)
              POP_TOP

451           LOAD_FAST_BORROW         0 (get_supabase)
              PUSH_NULL
              CALL                     0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024E30, file "app\services\memory\review_alerts.py", line 454>:
454           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

455           LOAD_CONST               2 ('str')

454           LOAD_CONST               3 ('since')

457           LOAD_CONST               4 ('Optional[str]')

454           LOAD_CONST               5 ('limit')

458           LOAD_CONST               6 ('int')

454           LOAD_CONST               7 ('return')

459           LOAD_CONST               8 ('Tuple[List[Dict[str, Any]], List[str]]')

454           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object _list_review_events_for_brokerage at 0x0000018C17D78680, file "app\services\memory\review_alerts.py", line 454>:
 454            RESUME                   0

 471            BUILD_LIST               0
                STORE_FAST               3 (warnings)

 472            NOP

 473    L1:     LOAD_GLOBAL              1 (_get_db + NULL)
                CALL                     0
                STORE_FAST               4 (db)

 475            LOAD_FAST_BORROW         4 (db)
                LOAD_ATTR                3 (table + NULL|self)
                LOAD_GLOBAL              4 (_TABLE_REVIEW)
                CALL                     1

 476            LOAD_ATTR                7 (select + NULL|self)
                LOAD_CONST               1 ('actor_id, actor_type, to_status, created_at')
                CALL                     1

 477            LOAD_ATTR                9 (eq + NULL|self)
                LOAD_CONST               2 ('brokerage_id')
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     2

 478            LOAD_ATTR               11 (order + NULL|self)
                LOAD_CONST               3 ('created_at')
                LOAD_CONST               4 (True)
                LOAD_CONST               5 (('desc',))
                CALL_KW                  2

 479            LOAD_ATTR               13 (limit + NULL|self)
                LOAD_FAST_BORROW         2 (limit)
                CALL                     1

 474            STORE_FAST               5 (query)

 481            LOAD_FAST_BORROW         1 (since)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L2)
                NOT_TAKEN

 482            LOAD_FAST_BORROW         5 (query)
                LOAD_ATTR               15 (gte + NULL|self)
                LOAD_CONST               3 ('created_at')
                LOAD_FAST_BORROW         1 (since)
                CALL                     2
                STORE_FAST               5 (query)

 483    L2:     LOAD_FAST_BORROW         5 (query)
                LOAD_ATTR               17 (execute + NULL|self)
                CALL                     0
                STORE_FAST               6 (result)

 484            LOAD_GLOBAL             19 (list + NULL)
                LOAD_GLOBAL             21 (getattr + NULL)
                LOAD_FAST_BORROW         6 (result)
                LOAD_CONST               6 ('data')
                LOAD_CONST               7 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
        L3:     NOT_TAKEN
        L4:     POP_TOP
                BUILD_LIST               0
        L5:     CALL                     1
                STORE_FAST               7 (rows)

 492    L6:     LOAD_GLOBAL             33 (isinstance + NULL)
                LOAD_FAST                7 (rows)
                LOAD_GLOBAL             18 (list)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         6 (to L7)
                NOT_TAKEN

 493            BUILD_LIST               0
                LOAD_CONST              11 ('unexpected_reader_shape')
                BUILD_LIST               1
                BUILD_TUPLE              2
                RETURN_VALUE

 494    L7:     LOAD_GLOBAL             35 (len + NULL)
                LOAD_FAST                7 (rows)
                CALL                     1
                LOAD_FAST                2 (limit)
                COMPARE_OP             188 (bool(>=))
                POP_JUMP_IF_FALSE       18 (to L8)
                NOT_TAKEN

 495            LOAD_FAST                3 (warnings)
                LOAD_ATTR               37 (append + NULL|self)
                LOAD_CONST              12 ('result_truncated_at_limit')
                CALL                     1
                POP_TOP

 496    L8:     LOAD_FAST_LOAD_FAST    115 (rows, warnings)
                BUILD_TUPLE              2
                RETURN_VALUE

  --    L9:     PUSH_EXC_INFO

 485            LOAD_GLOBAL             22 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       84 (to L14)
                NOT_TAKEN
                STORE_FAST               8 (e)

 486   L10:     LOAD_GLOBAL             24 (logger)
                LOAD_ATTR               27 (warning + NULL|self)

 487            LOAD_CONST               8 ('review_alerts reader failed (non-critical) | brokerage=')

 488            LOAD_FAST                0 (brokerage_id)
                FORMAT_SIMPLE
                LOAD_CONST               9 (' | error_type=')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE

 487            BUILD_STRING             4

 486            CALL                     1
                POP_TOP

 490            BUILD_LIST               0
                LOAD_CONST              10 ('reader_failed:')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1
                BUILD_TUPLE              2
       L11:     SWAP                     2
       L12:     POP_EXCEPT
                LOAD_CONST               7 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RETURN_VALUE

  --   L13:     LOAD_CONST               7 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RERAISE                  1

 485   L14:     RERAISE                  0

  --   L15:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L3 -> L9 [0]
  L4 to L6 -> L9 [0]
  L9 to L10 -> L15 [1] lasti
  L10 to L11 -> L13 [1] lasti
  L11 to L12 -> L15 [1] lasti
  L13 to L15 -> L15 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025930, file "app\services\memory\review_alerts.py", line 503>:
503           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

504           LOAD_CONST               2 ('Any')

503           LOAD_CONST               3 ('since')

505           LOAD_CONST               2 ('Any')

503           LOAD_CONST               4 ('limit')

506           LOAD_CONST               2 ('Any')

503           LOAD_CONST               5 ('return')

507           LOAD_CONST               6 ('Dict[str, Any]')

503           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object review_alerts_for_brokerage at 0x0000018C17D6DFC0, file "app\services\memory\review_alerts.py", line 503>:
503           RESUME                   0

525           LOAD_GLOBAL              1 (isinstance + NULL)
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
              POP_JUMP_IF_TRUE        15 (to L2)
              NOT_TAKEN

527   L1:     LOAD_CONST               1 ('status')
              LOAD_CONST               2 ('failed')

528           LOAD_CONST               3 ('errors')
              LOAD_CONST               4 ('missing_brokerage_id')
              BUILD_LIST               1

529           LOAD_CONST               5 ('alerts')
              BUILD_LIST               0

530           LOAD_CONST               6 ('alert_count')
              LOAD_SMALL_INT           0

531           LOAD_CONST               7 ('warnings')
              LOAD_CONST               4 ('missing_brokerage_id')
              BUILD_LIST               1

526           BUILD_MAP                5
              RETURN_VALUE

533   L2:     LOAD_FAST_BORROW         0 (brokerage_id)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               0 (brokerage_id)

535           LOAD_GLOBAL              7 (_coerce_since + NULL)
              LOAD_FAST_BORROW         1 (since)
              CALL                     1
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST   52 (cleaned_since, since_warning)

536           LOAD_GLOBAL              9 (_clamp_limit + NULL)
              LOAD_FAST_BORROW         2 (limit)
              CALL                     1
              STORE_FAST               5 (capped)

538           LOAD_GLOBAL             11 (_list_review_events_for_brokerage + NULL)

539           LOAD_FAST_BORROW_LOAD_FAST_BORROW 3 (brokerage_id, cleaned_since)
              LOAD_FAST_BORROW         5 (capped)

538           LOAD_CONST               8 (('since', 'limit'))
              CALL_KW                  3
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST  103 (rows, reader_warnings)

542           LOAD_GLOBAL             13 (summarize_review_alerts + NULL)
              LOAD_FAST_BORROW         6 (rows)
              CALL                     1
              STORE_FAST               8 (summary)

545           LOAD_CONST               1 ('status')
              LOAD_CONST               9 ('ok')

546           LOAD_CONST              10 ('brokerage_id')
              LOAD_FAST_BORROW         0 (brokerage_id)

547           LOAD_CONST              11 ('since')
              LOAD_FAST_BORROW         3 (cleaned_since)

548           LOAD_CONST              12 ('limit')
              LOAD_FAST_BORROW         5 (capped)

549           LOAD_CONST               6 ('alert_count')
              LOAD_FAST_BORROW         8 (summary)
              LOAD_CONST               6 ('alert_count')
              BINARY_OP               26 ([])

550           LOAD_CONST               5 ('alerts')
              LOAD_FAST_BORROW         8 (summary)
              LOAD_CONST               5 ('alerts')
              BINARY_OP               26 ([])

551           LOAD_CONST               7 ('warnings')
              LOAD_GLOBAL             15 (list + NULL)
              LOAD_FAST_BORROW         8 (summary)
              LOAD_CONST               7 ('warnings')
              BINARY_OP               26 ([])
              CALL                     1

544           BUILD_MAP                7
              STORE_FAST               9 (out)

553           LOAD_FAST_BORROW         4 (since_warning)
              TO_BOOL
              POP_JUMP_IF_FALSE       25 (to L3)
              NOT_TAKEN

554           LOAD_FAST_BORROW         9 (out)
              LOAD_CONST               7 ('warnings')
              BINARY_OP               26 ([])
              LOAD_ATTR               17 (append + NULL|self)
              LOAD_FAST_BORROW         4 (since_warning)
              CALL                     1
              POP_TOP

555   L3:     LOAD_FAST_BORROW         9 (out)
              LOAD_CONST               7 ('warnings')
              BINARY_OP               26 ([])
              LOAD_ATTR               19 (extend + NULL|self)
              LOAD_FAST_BORROW         7 (reader_warnings)
              CALL                     1
              POP_TOP

556           LOAD_FAST_BORROW         9 (out)
              RETURN_VALUE
```
