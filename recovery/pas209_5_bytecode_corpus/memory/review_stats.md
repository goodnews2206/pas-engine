# memory/review_stats

- **pyc:** `app\services\memory\__pycache__\review_stats.cpython-314.pyc`
- **expected source path (absent):** `app\services\memory/review_stats.py`
- **co_filename (from bytecode):** `app\services\memory\review_stats.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** memory

## Module docstring

```
PAS150 — Memory review stats (read-only, structural).

Pure + thinly-wrapped summariser layered over the PAS144C
``pas_memory_review_events`` audit table. Gives operators visibility
into *who is acting on memory candidates and how* before higher-blast-
radius surfaces (per-record expire / quarantine UI, bulk actions) are
considered.

Hard contract:
  * **Tenant-scoped.** Every public helper that touches Supabase
    requires ``brokerage_id``. There is no unscoped path.
  * **Bounded.** ``review_stats_for_brokerage`` caps the row fetch
    via ``_MAX_STATS_LIMIT`` (default 500). The query has both a
    ``brokerage_id`` equality and an ``ORDER BY created_at DESC
    LIMIT n`` — NOT a full-table scan.
  * **Structural output only.** Counts, rates, actor ids, status
    tokens. Reason text, metadata JSONB, evidence, transcript, raw
    prompts and lineage are NEVER referenced or surfaced. The
    summariser physically does not read those keys.
  * **Fail-closed.** Bad input, reader failure, malformed event row —
    every path returns a structured warning. Nothing in this module
    raises.

Public surface:
  - summarize_review_events(events)                    -> dict
  - review_stats_for_brokerage(brokerage_id, since=None, limit=500) -> dict
  - ALLOWED_TO_STATUSES, ALLOWED_ACTOR_TYPES,
    HIGH_RATE_THRESHOLD, HIGH_RATE_MIN_DECISIONS,
    _MAX_STATS_LIMIT
```

## Imports

`Any`, `Dict`, `Iterable`, `List`, `Optional`, `Tuple`, `__future__`, `annotations`, `app.db.supabase_client`, `date`, `datetime`, `get_supabase`, `logging`, `timedelta`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_clamp_days`, `_clamp_limit`, `_coerce_since`, `_empty_day_bucket`, `_empty_summary`, `_get_db`, `_list_review_events_for_brokerage`, `_now_day`, `_parse_iso_day`, `_round_rate`, `_safe_str`, `bucket_review_events_by_day`, `review_stats_for_brokerage`, `summarize_review_events`

## Env-key candidates

`APPROVED`, `EXPIRED`, `QUARANTINED`, `REJECTED`, `UNKNOWN`

## String constants (redacted where noted)

- '\nPAS150 — Memory review stats (read-only, structural).\n\nPure + thinly-wrapped summariser layered over the PAS144C\n``pas_memory_review_events`` audit table. Gives operators visibility\ninto *who is acting on memory candidates and how* before higher-blast-\nradius surfaces (per-record expire / quarantine UI, bulk actions) are\nconsidered.\n\nHard contract:\n  * **Tenant-scoped.** Every public helper that touches Supabase\n    requires ``brokerage_id``. There is no unscoped path.\n  * **Bounded.** ``review_stats_for_brokerage`` caps the row fetch\n    via ``_MAX_STATS_LIMIT`` (default 500). The query has both a\n    ``brokerage_id`` equality and an ``ORDER BY created_at DESC\n    LIMIT n`` — NOT a full-table scan.\n  * **Structural output only.** Counts, rates, actor ids, status\n    tokens. Reason text, metadata JSONB, evidence, transcript, raw\n    prompts and lineage are NEVER referenced or surfaced. The\n    summariser physically does not read those keys.\n  * **Fail-closed.** Bad input, reader failure, malformed event row —\n    every path returns a structured warning. Nothing in this module\n    raises.\n\nPublic surface:\n  - summarize_review_events(events)                    -> dict\n  - review_stats_for_brokerage(brokerage_id, since=None, limit=500) -> dict\n  - ALLOWED_TO_STATUSES, ALLOWED_ACTOR_TYPES,\n    HIGH_RATE_THRESHOLD, HIGH_RATE_MIN_DECISIONS,\n    _MAX_STATS_LIMIT\n'
- 'pas.memory.review_stats'
- 'pas_memory_review_events'
- 'days'
- 'now'
- 'since'
- 'limit'
- 'return'
- 'Dict[str, Any]'
- 'total_events'
- 'by_to_status'
- 'by_actor'
- 'warnings'
- 'val'
- 'Any'
- 'Optional[str]'
- 'Return a trimmed string for non-empty ``val`` or None.'
- 'num'
- 'int'
- 'denom'
- 'float'
- 'Return a 4-decimal rate (denom > 0 by caller invariant).'
- 'events'
- 'Project a list of audit-event rows into a closed structural\nsummary. Pure — no I/O, no logging, no raises.\n\nEach row is read for ONLY these keys: ``to_status``, ``actor_type``,\n``actor_id``. ``review_id``, ``memory_id``, ``brokerage_id``,\n``from_status``, ``reason``, ``created_at``, and any other column\non the row (notably ``metadata``) are ignored on purpose — the\noperator-facing stats surface never echoes them.\n\nReturns:\n    {\n        "total_events": int,\n        "by_to_status": {APPROVED, REJECTED, EXPIRED, QUARANTINED: int},\n        "by_actor": [\n            {\n                "actor_id":    str,\n                "actor_type":  str,\n                "total":       int,\n                "approved":    int,\n                "rejected":    int,\n                "expired":     int,\n                "quarantined": int,\n                "approve_rate": float,\n                "reject_rate":  float,\n                "warning":      None | "high_approve_rate"\n                                     | "high_reject_rate",\n            },\n            ...\n        ],\n        "warnings": list[str],\n    }\n\nOrdering: by total descending, then actor_id ascending. Stable for\ntest pinning.\n'
- 'unexpected_events_shape'
- 'to_status'
- 'actor_type'
- 'UNKNOWN'
- 'actor_id'
- 'unknown'
- 'approved'
- 'rejected'
- 'expired'
- 'quarantined'
- 'APPROVED'
- 'REJECTED'
- 'EXPIRED'
- 'QUARANTINED'
- 'unknown_status_events_ignored:'
- 'high_approve_rate'
- 'high_reject_rate'
- 'total'
- 'approve_rate'
- 'reject_rate'
- 'warning'
- 'value'
- 'Coerce a caller-supplied days window; clamp to [_DAYS_MIN, _DAYS_MAX].'
- "Extract the YYYY-MM-DD prefix from an ISO-8601 timestamp string.\n\nReturns the validated day token or None on any malformed input.\nIntentionally structural — we do NOT parse timezone offsets here.\nThe audit table stores ``created_at`` as ``timestamptz`` and\nSupabase returns UTC by default, so slicing the first 10 chars\ngives the UTC calendar day. Anything more elaborate is the\ndatabase's job.\n"
- 'str'
- "Resolve the 'today' anchor for the day axis.\n\n``now`` overrides the system clock for tests. Anything malformed\nfalls back to ``datetime.now(timezone.utc)``.\n"
- '%Y-%m-%d'
- 'day'
- 'Project audit-event rows into per-day terminal-status counters.\n\nPure deterministic helper. Reads ONLY ``created_at`` and\n``to_status`` per row. Every other field on the row — including\n``reason``, ``metadata``, ``evidence``, ``transcript``,\n``memory_id``, ``actor_id`` — is ignored on purpose: the\ntime-series surface never echoes them.\n\nArgs:\n    events: list of dicts. Anything else is treated as "no events"\n        with an ``unexpected_events_shape`` warning.\n    days:   integer length of the day window. Clamped to\n        ``[_DAYS_MIN, _DAYS_MAX]``. Defaults to ``_DAYS_DEFAULT``.\n    now:    optional ISO-8601 day/timestamp override for the\n        "today" anchor. Defaults to ``datetime.now(timezone.utc)``.\n\nReturns:\n    {\n        "days":     int,                # clamped\n        "buckets":  [                   # oldest -> newest, zero-filled\n            {\n                "day":         "YYYY-MM-DD",\n                "approved":    int,\n                "rejected":    int,\n                "expired":     int,\n                "quarantined": int,\n                "total":       int,\n            },\n            ...\n        ],\n        "warnings": list[str],\n    }\n'
- 'buckets'
- 'created_at'
- 'malformed_created_at_ignored:'
- 'Coerce a caller-supplied limit; clamp to [1, _MAX_STATS_LIMIT].'
- 'Tuple[Optional[str], Optional[str]]'
- 'Coerce a caller-supplied ``since`` ISO-8601 string.\n\nReturns (cleaned_value, warning_token_or_None). Non-string or\nblank inputs yield (None, None) — i.e. "no filter, no warning".\nStrings that don\'t structurally look ISO-8601 yield (None, token)\nso the route surfaces a warning to the operator.\n\nDeliberately structural — we don\'t parse the timestamp with\ndatetime.fromisoformat here because we want to be permissive with\ntimezone offsets (\'Z\' vs \'+00:00\') without pulling extra deps.\n'
- 'Lazy Supabase resolver. Mirrors review.py.'
- 'brokerage_id'
- 'Tuple[List[Dict[str, Any]], List[str]]'
- 'Tenant-scoped, bounded fetch of audit-event rows.\n\nMirrors the doctrine of ``review.list_memory_review_events`` but\nqueries by ``brokerage_id`` alone (no per-memory filter). The\nquery is bounded by ``limit`` (clamped to ``_MAX_STATS_LIMIT``)\nand ordered newest-first, so it is NOT a full-table scan.\n\nReturns (rows, warnings). Never raises. Returns ([], [token]) on\nany Supabase failure.\n'
- 'review_id, to_status, actor_type, actor_id, created_at'
- 'data'
- 'review_stats reader failed (non-critical) | brokerage='
- ' | error_type='
- 'reader_failed:'
- 'unexpected_reader_shape'
- 'result_truncated_at_limit'
- 'Return the closed-shape stats summary for one tenant.\n\n``brokerage_id`` is REQUIRED. There is no path through this helper\nthat omits the tenant filter or falls back to a cross-tenant scan.\n\nResponse (always 200 from the route caller\'s perspective):\n    {\n        "status":       "ok" | "failed",\n        "brokerage_id": "<id>",\n        "since":        "<iso-8601 or null>",\n        "limit":        <int>,\n        "total_events": <int>,\n        "by_to_status": {APPROVED, REJECTED, EXPIRED, QUARANTINED},\n        "by_actor":     [<actor row>, ...],\n        "by_day":       {"days": <int>, "buckets": [...]},  # PAS151\n        "warnings":     [<str>, ...],\n    }\n'
- 'status'
- 'failed'
- 'errors'
- 'missing_brokerage_id'
- 'by_day'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS150 — Memory review stats (read-only, structural).\n\nPure + thinly-wrapped summariser layered over the PAS144C\n``pas_memory_review_events`` audit table. Gives operators visibility\ninto *who is acting on memory candidates and how* before higher-blast-\nradius surfaces (per-record expire / quarantine UI, bulk actions) are\nconsidered.\n\nHard contract:\n  * **Tenant-scoped.** Every public helper that touches Supabase\n    requires ``brokerage_id``. There is no unscoped path.\n  * **Bounded.** ``review_stats_for_brokerage`` caps the row fetch\n    via ``_MAX_STATS_LIMIT`` (default 500). The query has both a\n    ``brokerage_id`` equality and an ``ORDER BY created_at DESC\n    LIMIT n`` — NOT a full-table scan.\n  * **Structural output only.** Counts, rates, actor ids, status\n    tokens. Reason text, metadata JSONB, evidence, transcript, raw\n    prompts and lineage are NEVER referenced or surfaced. The\n    summariser physically does not read those keys.\n  * **Fail-closed.** Bad input, reader failure, malformed event row —\n    every path returns a structured warning. Nothing in this module\n    raises.\n\nPublic surface:\n  - summarize_review_events(events)                    -> dict\n  - review_stats_for_brokerage(brokerage_id, since=None, limit=500) -> dict\n  - ALLOWED_TO_STATUSES, ALLOWED_ACTOR_TYPES,\n    HIGH_RATE_THRESHOLD, HIGH_RATE_MIN_DECISIONS,\n    _MAX_STATS_LIMIT\n')
              STORE_NAME               0 (__doc__)

 33           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 35           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 36           LOAD_SMALL_INT           0
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

 37           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('Any', 'Dict', 'Iterable', 'List', 'Optional', 'Tuple'))
              IMPORT_NAME              8 (typing)
              IMPORT_FROM              9 (Any)
              STORE_NAME               9 (Any)
              IMPORT_FROM             10 (Dict)
              STORE_NAME              10 (Dict)
              IMPORT_FROM             11 (Iterable)
              STORE_NAME              11 (Iterable)
              IMPORT_FROM             12 (List)
              STORE_NAME              12 (List)
              IMPORT_FROM             13 (Optional)
              STORE_NAME              13 (Optional)
              IMPORT_FROM             14 (Tuple)
              STORE_NAME              14 (Tuple)
              POP_TOP

 39           LOAD_NAME                3 (logging)
              LOAD_ATTR               30 (getLogger)
              PUSH_NULL
              LOAD_CONST               5 ('pas.memory.review_stats')
              CALL                     1
              STORE_NAME              16 (logger)

 45           LOAD_CONST              40 (('APPROVED', 'REJECTED', 'EXPIRED', 'QUARANTINED'))
              STORE_NAME              17 (ALLOWED_TO_STATUSES)

 46           LOAD_CONST              41 (('OPERATOR', 'SYSTEM', 'ADMIN', 'SECURITY'))
              STORE_NAME              18 (ALLOWED_ACTOR_TYPES)

 52           LOAD_CONST               6 (0.9)
              STORE_NAME              19 (HIGH_RATE_THRESHOLD)

 53           LOAD_SMALL_INT          10
              STORE_NAME              20 (HIGH_RATE_MIN_DECISIONS)

 58           LOAD_CONST               7 (500)
              STORE_NAME              21 (_MAX_STATS_LIMIT)

 59           LOAD_CONST               7 (500)
              STORE_NAME              22 (_DEFAULT_STATS_LIMIT)

 61           LOAD_CONST               8 ('pas_memory_review_events')
              STORE_NAME              23 (_TABLE_REVIEW)

 69           LOAD_SMALL_INT           1
              STORE_NAME              24 (_DAYS_MIN)

 70           LOAD_SMALL_INT          30
              STORE_NAME              25 (_DAYS_MAX)

 71           LOAD_SMALL_INT          14
              STORE_NAME              26 (_DAYS_DEFAULT)

 78           LOAD_CONST               9 (<code object __annotate__ at 0x0000018C17FA3870, file "app\services\memory\review_stats.py", line 78>)
              MAKE_FUNCTION
              LOAD_CONST              10 (<code object _empty_summary at 0x0000018C18053090, file "app\services\memory\review_stats.py", line 78>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              27 (_empty_summary)

 87           LOAD_CONST              11 (<code object __annotate__ at 0x0000018C17FA34B0, file "app\services\memory\review_stats.py", line 87>)
              MAKE_FUNCTION
              LOAD_CONST              12 (<code object _safe_str at 0x0000018C18038B70, file "app\services\memory\review_stats.py", line 87>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              28 (_safe_str)

 95           LOAD_CONST              13 (<code object __annotate__ at 0x0000018C18024D30, file "app\services\memory\review_stats.py", line 95>)
              MAKE_FUNCTION
              LOAD_CONST              14 (<code object _round_rate at 0x0000018C17FBFEE0, file "app\services\memory\review_stats.py", line 95>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              29 (_round_rate)

102           LOAD_CONST              15 (<code object __annotate__ at 0x0000018C17FA2B50, file "app\services\memory\review_stats.py", line 102>)
              MAKE_FUNCTION
              LOAD_CONST              16 (<code object summarize_review_events at 0x0000018C181D9F20, file "app\services\memory\review_stats.py", line 102>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              30 (summarize_review_events)

231           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C17FA2C40, file "app\services\memory\review_stats.py", line 231>)
              MAKE_FUNCTION
              LOAD_CONST              18 (<code object _clamp_days at 0x0000018C17FF0C30, file "app\services\memory\review_stats.py", line 231>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              31 (_clamp_days)

246           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA2100, file "app\services\memory\review_stats.py", line 246>)
              MAKE_FUNCTION
              LOAD_CONST              20 (<code object _parse_iso_day at 0x0000018C17E8ACC0, file "app\services\memory\review_stats.py", line 246>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              32 (_parse_iso_day)

274           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA21F0, file "app\services\memory\review_stats.py", line 274>)
              MAKE_FUNCTION
              LOAD_CONST              22 (<code object _now_day at 0x0000018C1800B230, file "app\services\memory\review_stats.py", line 274>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              33 (_now_day)

287           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA30F0, file "app\services\memory\review_stats.py", line 287>)
              MAKE_FUNCTION
              LOAD_CONST              24 (<code object _empty_day_bucket at 0x0000018C17FA31E0, file "app\services\memory\review_stats.py", line 287>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              34 (_empty_day_bucket)

298           LOAD_CONST              25 ('days')

301           LOAD_NAME               26 (_DAYS_DEFAULT)

298           LOAD_CONST              26 ('now')

302           LOAD_CONST               2 (None)

298           BUILD_MAP                2
              LOAD_CONST              27 (<code object __annotate__ at 0x0000018C18024B30, file "app\services\memory\review_stats.py", line 298>)
              MAKE_FUNCTION
              LOAD_CONST              28 (<code object bucket_review_events_by_day at 0x0000018C181DAF20, file "app\services\memory\review_stats.py", line 298>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              35 (bucket_review_events_by_day)

407           LOAD_CONST              29 (<code object __annotate__ at 0x0000018C17FA1D40, file "app\services\memory\review_stats.py", line 407>)
              MAKE_FUNCTION
              LOAD_CONST              30 (<code object _clamp_limit at 0x0000018C17FF1230, file "app\services\memory\review_stats.py", line 407>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              36 (_clamp_limit)

420           LOAD_CONST              31 (<code object __annotate__ at 0x0000018C17FA2970, file "app\services\memory\review_stats.py", line 420>)
              MAKE_FUNCTION
              LOAD_CONST              32 (<code object _coerce_since at 0x0000018C1794EBB0, file "app\services\memory\review_stats.py", line 420>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              37 (_coerce_since)

447           LOAD_CONST              33 (<code object _get_db at 0x0000018C17FA23D0, file "app\services\memory\review_stats.py", line 447>)
              MAKE_FUNCTION
              STORE_NAME              38 (_get_db)

453           LOAD_CONST              34 ('since')

456           LOAD_CONST               2 (None)

453           LOAD_CONST              35 ('limit')

457           LOAD_NAME               22 (_DEFAULT_STATS_LIMIT)

453           BUILD_MAP                2
              LOAD_CONST              36 (<code object __annotate__ at 0x0000018C18024E30, file "app\services\memory\review_stats.py", line 453>)
              MAKE_FUNCTION
              LOAD_CONST              37 (<code object _list_review_events_for_brokerage at 0x0000018C17D79E90, file "app\services\memory\review_stats.py", line 453>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              39 (_list_review_events_for_brokerage)

503           LOAD_CONST               2 (None)

504           LOAD_NAME               22 (_DEFAULT_STATS_LIMIT)

505           LOAD_NAME               26 (_DAYS_DEFAULT)

501           BUILD_TUPLE              3
              LOAD_CONST              38 (<code object __annotate__ at 0x0000018C18025930, file "app\services\memory\review_stats.py", line 501>)
              MAKE_FUNCTION
              LOAD_CONST              39 (<code object review_stats_for_brokerage at 0x0000018C181DB7D0, file "app\services\memory\review_stats.py", line 501>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              40 (review_stats_for_brokerage)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "app\services\memory\review_stats.py", line 78>:
 78           RESUME                   0
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

Disassembly of <code object _empty_summary at 0x0000018C18053090, file "app\services\memory\review_stats.py", line 78>:
  78           RESUME                   0

  80           LOAD_CONST               0 ('total_events')
               LOAD_SMALL_INT           0

  81           LOAD_CONST               1 ('by_to_status')
               LOAD_GLOBAL              0 (ALLOWED_TO_STATUSES)
               GET_ITER
               LOAD_FAST_AND_CLEAR      0 (s)
               SWAP                     2
       L1:     BUILD_MAP                0
               SWAP                     2
       L2:     FOR_ITER                 5 (to L3)
               STORE_FAST_LOAD_FAST     0 (s, s)
               LOAD_SMALL_INT           0
               MAP_ADD                  2
               JUMP_BACKWARD            7 (to L2)
       L3:     END_FOR
               POP_ITER
       L4:     SWAP                     2
               STORE_FAST               0 (s)

  82           LOAD_CONST               2 ('by_actor')
               BUILD_LIST               0

  83           LOAD_CONST               3 ('warnings')
               BUILD_LIST               0

  79           BUILD_MAP                4
               RETURN_VALUE

  --   L5:     SWAP                     2
               POP_TOP

  81           SWAP                     2
               STORE_FAST               0 (s)
               RERAISE                  0
ExceptionTable:
  L1 to L4 -> L5 [5]

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "app\services\memory\review_stats.py", line 87>:
 87           RESUME                   0
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

Disassembly of <code object _safe_str at 0x0000018C18038B70, file "app\services\memory\review_stats.py", line 87>:
 87           RESUME                   0

 89           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (val)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

 90           LOAD_CONST               1 (None)
              RETURN_VALUE

 91   L1:     LOAD_FAST_BORROW         0 (val)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

 92           LOAD_FAST                1 (s)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 (None)
      L2:     RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024D30, file "app\services\memory\review_stats.py", line 95>:
 95           RESUME                   0
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

Disassembly of <code object _round_rate at 0x0000018C17FBFEE0, file "app\services\memory\review_stats.py", line 95>:
 95           RESUME                   0

 97           LOAD_FAST_BORROW         1 (denom)
              LOAD_SMALL_INT           0
              COMPARE_OP              58 (bool(<=))
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN

 98           LOAD_CONST               1 (0.0)
              RETURN_VALUE

 99   L1:     LOAD_GLOBAL              1 (round + NULL)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (num, denom)
              BINARY_OP               11 (/)
              LOAD_SMALL_INT           4
              CALL                     2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "app\services\memory\review_stats.py", line 102>:
102           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('events')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object summarize_review_events at 0x0000018C181D9F20, file "app\services\memory\review_stats.py", line 102>:
102            RESUME                   0

138            LOAD_GLOBAL              1 (_empty_summary + NULL)
               CALL                     0
               STORE_FAST               1 (summary)

139            LOAD_GLOBAL              3 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (events)
               LOAD_GLOBAL              4 (list)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        27 (to L1)
               NOT_TAKEN

140            LOAD_FAST_BORROW         1 (summary)
               LOAD_CONST               1 ('warnings')
               BINARY_OP               26 ([])
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_CONST               2 ('unexpected_events_shape')
               CALL                     1
               POP_TOP

141            LOAD_FAST_BORROW         1 (summary)
               RETURN_VALUE

145    L1:     BUILD_MAP                0
               STORE_FAST               2 (buckets)

147            LOAD_SMALL_INT           0
               STORE_FAST               3 (unknown_statuses_seen)

149            LOAD_FAST_BORROW         0 (events)
               GET_ITER
       L2:     EXTENDED_ARG             1
               FOR_ITER               368 (to L12)
               STORE_FAST               4 (raw)

150            LOAD_GLOBAL              3 (isinstance + NULL)
               LOAD_FAST_BORROW         4 (raw)
               LOAD_GLOBAL              8 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        12 (to L3)
               NOT_TAKEN

151            LOAD_FAST_BORROW         3 (unknown_statuses_seen)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               3 (unknown_statuses_seen)

152            JUMP_BACKWARD           37 (to L2)

154    L3:     LOAD_GLOBAL             11 (_safe_str + NULL)
               LOAD_FAST_BORROW         4 (raw)
               LOAD_ATTR               13 (get + NULL|self)
               LOAD_CONST               3 ('to_status')
               CALL                     1
               CALL                     1
               STORE_FAST               5 (to_status)

155            LOAD_FAST_BORROW         5 (to_status)
               LOAD_GLOBAL             14 (ALLOWED_TO_STATUSES)
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_FALSE       12 (to L4)
               NOT_TAKEN

157            LOAD_FAST_BORROW         3 (unknown_statuses_seen)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               3 (unknown_statuses_seen)

158            JUMP_BACKWARD           85 (to L2)

160    L4:     LOAD_GLOBAL             11 (_safe_str + NULL)
               LOAD_FAST_BORROW         4 (raw)
               LOAD_ATTR               13 (get + NULL|self)
               LOAD_CONST               4 ('actor_type')
               CALL                     1
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               5 ('UNKNOWN')
       L5:     STORE_FAST               6 (actor_type)

161            LOAD_GLOBAL             11 (_safe_str + NULL)
               LOAD_FAST_BORROW         4 (raw)
               LOAD_ATTR               13 (get + NULL|self)
               LOAD_CONST               6 ('actor_id')
               CALL                     1
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L6)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               7 ('unknown')
       L6:     STORE_FAST               7 (actor_id)

163            LOAD_FAST_BORROW         1 (summary)
               LOAD_CONST               8 ('by_to_status')
               BINARY_OP               26 ([])
               LOAD_FAST_BORROW         5 (to_status)
               COPY                     2
               COPY                     2
               BINARY_OP               26 ([])
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               SWAP                     3
               SWAP                     2
               STORE_SUBSCR

164            LOAD_FAST_BORROW         1 (summary)
               LOAD_CONST               9 ('total_events')
               COPY                     2
               COPY                     2
               BINARY_OP               26 ([])
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               SWAP                     3
               SWAP                     2
               STORE_SUBSCR

166            LOAD_FAST_BORROW_LOAD_FAST_BORROW 118 (actor_id, actor_type)
               BUILD_TUPLE              2
               STORE_FAST               8 (key)

167            LOAD_FAST_BORROW         2 (buckets)
               LOAD_ATTR               13 (get + NULL|self)
               LOAD_FAST_BORROW         8 (key)
               CALL                     1
               STORE_FAST               9 (bucket)

168            LOAD_FAST_BORROW         9 (bucket)
               POP_JUMP_IF_NOT_NONE    15 (to L7)
               NOT_TAKEN

170            LOAD_CONST              11 ('approved')
               LOAD_SMALL_INT           0

171            LOAD_CONST              12 ('rejected')
               LOAD_SMALL_INT           0

172            LOAD_CONST              13 ('expired')
               LOAD_SMALL_INT           0

173            LOAD_CONST              14 ('quarantined')
               LOAD_SMALL_INT           0

169            BUILD_MAP                4
               STORE_FAST               9 (bucket)

175            LOAD_FAST_BORROW_LOAD_FAST_BORROW 146 (bucket, buckets)
               LOAD_FAST_BORROW         8 (key)
               STORE_SUBSCR

176    L7:     LOAD_FAST_BORROW         5 (to_status)
               LOAD_CONST              15 ('APPROVED')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       25 (to L8)
               NOT_TAKEN

177            LOAD_FAST_BORROW         9 (bucket)
               LOAD_CONST              11 ('approved')
               COPY                     2
               COPY                     2
               BINARY_OP               26 ([])
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               SWAP                     3
               SWAP                     2
               STORE_SUBSCR
               EXTENDED_ARG             1
               JUMP_BACKWARD          275 (to L2)

178    L8:     LOAD_FAST_BORROW         5 (to_status)
               LOAD_CONST              16 ('REJECTED')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       25 (to L9)
               NOT_TAKEN

179            LOAD_FAST_BORROW         9 (bucket)
               LOAD_CONST              12 ('rejected')
               COPY                     2
               COPY                     2
               BINARY_OP               26 ([])
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               SWAP                     3
               SWAP                     2
               STORE_SUBSCR
               EXTENDED_ARG             1
               JUMP_BACKWARD          306 (to L2)

180    L9:     LOAD_FAST_BORROW         5 (to_status)
               LOAD_CONST              17 ('EXPIRED')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       25 (to L10)
               NOT_TAKEN

181            LOAD_FAST_BORROW         9 (bucket)
               LOAD_CONST              13 ('expired')
               COPY                     2
               COPY                     2
               BINARY_OP               26 ([])
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               SWAP                     3
               SWAP                     2
               STORE_SUBSCR
               EXTENDED_ARG             1
               JUMP_BACKWARD          337 (to L2)

182   L10:     LOAD_FAST_BORROW         5 (to_status)
               LOAD_CONST              18 ('QUARANTINED')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_TRUE         4 (to L11)
               NOT_TAKEN
               EXTENDED_ARG             1
               JUMP_BACKWARD          347 (to L2)

183   L11:     LOAD_FAST_BORROW         9 (bucket)
               LOAD_CONST              14 ('quarantined')
               COPY                     2
               COPY                     2
               BINARY_OP               26 ([])
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               SWAP                     3
               SWAP                     2
               STORE_SUBSCR
               EXTENDED_ARG             1
               JUMP_BACKWARD          371 (to L2)

149   L12:     END_FOR
               POP_ITER

185            LOAD_FAST_BORROW         3 (unknown_statuses_seen)
               TO_BOOL
               POP_JUMP_IF_FALSE       28 (to L13)
               NOT_TAKEN

186            LOAD_FAST_BORROW         1 (summary)
               LOAD_CONST               1 ('warnings')
               BINARY_OP               26 ([])
               LOAD_ATTR                7 (append + NULL|self)

187            LOAD_CONST              19 ('unknown_status_events_ignored:')
               LOAD_FAST_BORROW         3 (unknown_statuses_seen)
               FORMAT_SIMPLE
               BUILD_STRING             2

186            CALL                     1
               POP_TOP

190   L13:     BUILD_LIST               0
               STORE_FAST              10 (actor_rows)

191            LOAD_FAST_BORROW         2 (buckets)
               LOAD_ATTR               17 (items + NULL|self)
               CALL                     0
               GET_ITER
      L14:     FOR_ITER               202 (to L17)
               UNPACK_SEQUENCE          2
               UNPACK_SEQUENCE          2
               STORE_FAST_STORE_FAST  118 (actor_id, actor_type)
               STORE_FAST              11 (counts)

193            LOAD_FAST_BORROW        11 (counts)
               LOAD_CONST              11 ('approved')
               BINARY_OP               26 ([])

194            LOAD_FAST_BORROW        11 (counts)
               LOAD_CONST              12 ('rejected')
               BINARY_OP               26 ([])

193            BINARY_OP                0 (+)

195            LOAD_FAST_BORROW        11 (counts)
               LOAD_CONST              13 ('expired')
               BINARY_OP               26 ([])

193            BINARY_OP                0 (+)

196            LOAD_FAST_BORROW        11 (counts)
               LOAD_CONST              14 ('quarantined')
               BINARY_OP               26 ([])

193            BINARY_OP                0 (+)

192            STORE_FAST              12 (total)

198            LOAD_GLOBAL             19 (_round_rate + NULL)
               LOAD_FAST_BORROW        11 (counts)
               LOAD_CONST              11 ('approved')
               BINARY_OP               26 ([])
               LOAD_FAST_BORROW        12 (total)
               CALL                     2
               STORE_FAST              13 (approve_rate)

199            LOAD_GLOBAL             19 (_round_rate + NULL)
               LOAD_FAST_BORROW        11 (counts)
               LOAD_CONST              12 ('rejected')
               BINARY_OP               26 ([])
               LOAD_FAST_BORROW        12 (total)
               CALL                     2
               STORE_FAST              14 (reject_rate)

201            LOAD_CONST              10 (None)
               STORE_FAST              15 (warning)

202            LOAD_FAST_BORROW        12 (total)
               LOAD_GLOBAL             20 (HIGH_RATE_MIN_DECISIONS)
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE       28 (to L16)
               NOT_TAKEN

203            LOAD_FAST_BORROW        13 (approve_rate)
               LOAD_GLOBAL             22 (HIGH_RATE_THRESHOLD)
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE        4 (to L15)
               NOT_TAKEN

204            LOAD_CONST              20 ('high_approve_rate')
               STORE_FAST              15 (warning)
               JUMP_FORWARD            13 (to L16)

205   L15:     LOAD_FAST_BORROW        14 (reject_rate)
               LOAD_GLOBAL             22 (HIGH_RATE_THRESHOLD)
               COMPARE_OP             188 (bool(>=))
               POP_JUMP_IF_FALSE        3 (to L16)
               NOT_TAKEN

206            LOAD_CONST              21 ('high_reject_rate')
               STORE_FAST              15 (warning)

208   L16:     LOAD_FAST_BORROW        10 (actor_rows)
               LOAD_ATTR                7 (append + NULL|self)

209            LOAD_CONST               6 ('actor_id')
               LOAD_FAST_BORROW         7 (actor_id)

210            LOAD_CONST               4 ('actor_type')
               LOAD_FAST_BORROW         6 (actor_type)

211            LOAD_CONST              22 ('total')
               LOAD_FAST_BORROW        12 (total)

212            LOAD_CONST              11 ('approved')
               LOAD_FAST_BORROW        11 (counts)
               LOAD_CONST              11 ('approved')
               BINARY_OP               26 ([])

213            LOAD_CONST              12 ('rejected')
               LOAD_FAST_BORROW        11 (counts)
               LOAD_CONST              12 ('rejected')
               BINARY_OP               26 ([])

214            LOAD_CONST              13 ('expired')
               LOAD_FAST_BORROW        11 (counts)
               LOAD_CONST              13 ('expired')
               BINARY_OP               26 ([])

215            LOAD_CONST              14 ('quarantined')
               LOAD_FAST_BORROW        11 (counts)
               LOAD_CONST              14 ('quarantined')
               BINARY_OP               26 ([])

216            LOAD_CONST              23 ('approve_rate')
               LOAD_FAST_BORROW        13 (approve_rate)

217            LOAD_CONST              24 ('reject_rate')
               LOAD_FAST_BORROW        14 (reject_rate)

218            LOAD_CONST              25 ('warning')
               LOAD_FAST_BORROW        15 (warning)

208            BUILD_MAP               10
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          204 (to L14)

191   L17:     END_FOR
               POP_ITER

222            LOAD_FAST_BORROW        10 (actor_rows)
               LOAD_ATTR               25 (sort + NULL|self)
               LOAD_CONST              26 (<code object <lambda> at 0x0000018C18025230, file "app\services\memory\review_stats.py", line 222>)
               MAKE_FUNCTION
               LOAD_CONST              27 (('key',))
               CALL_KW                  1
               POP_TOP

223            LOAD_FAST_BORROW_LOAD_FAST_BORROW 161 (actor_rows, summary)
               LOAD_CONST              28 ('by_actor')
               STORE_SUBSCR

224            LOAD_FAST_BORROW         1 (summary)
               RETURN_VALUE

Disassembly of <code object <lambda> at 0x0000018C18025230, file "app\services\memory\review_stats.py", line 222>:
222           RESUME                   0
              LOAD_FAST_BORROW         0 (r)
              LOAD_CONST               0 ('total')
              BINARY_OP               26 ([])
              UNARY_NEGATIVE
              LOAD_FAST_BORROW         0 (r)
              LOAD_CONST               1 ('actor_id')
              BINARY_OP               26 ([])
              BUILD_TUPLE              2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "app\services\memory\review_stats.py", line 231>:
231           RESUME                   0
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

Disassembly of <code object _clamp_days at 0x0000018C17FF0C30, file "app\services\memory\review_stats.py", line 231>:
 231           RESUME                   0

 233           LOAD_FAST_BORROW         0 (value)
               POP_JUMP_IF_NOT_NONE     7 (to L1)
               NOT_TAKEN

 234           LOAD_GLOBAL              0 (_DAYS_DEFAULT)
               RETURN_VALUE

 235   L1:     NOP

 236   L2:     LOAD_GLOBAL              3 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               1 (n)

 239   L3:     LOAD_FAST                1 (n)
               LOAD_GLOBAL              8 (_DAYS_MIN)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        7 (to L4)
               NOT_TAKEN

 240           LOAD_GLOBAL              8 (_DAYS_MIN)
               RETURN_VALUE

 241   L4:     LOAD_FAST                1 (n)
               LOAD_GLOBAL             10 (_DAYS_MAX)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        7 (to L5)
               NOT_TAKEN

 242           LOAD_GLOBAL             10 (_DAYS_MAX)
               RETURN_VALUE

 243   L5:     LOAD_FAST                1 (n)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

 237           LOAD_GLOBAL              4 (TypeError)
               LOAD_GLOBAL              6 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       10 (to L8)
               NOT_TAKEN
               POP_TOP

 238           LOAD_GLOBAL              0 (_DAYS_DEFAULT)
               SWAP                     2
       L7:     POP_EXCEPT
               RETURN_VALUE

 237   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [0]
  L6 to L7 -> L9 [1] lasti
  L8 to L9 -> L9 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "app\services\memory\review_stats.py", line 246>:
246           RESUME                   0
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

Disassembly of <code object _parse_iso_day at 0x0000018C17E8ACC0, file "app\services\memory\review_stats.py", line 246>:
 246            RESUME                   0

 256            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (value)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN

 257            LOAD_CONST               1 (None)
                RETURN_VALUE

 258    L1:     LOAD_FAST_BORROW         0 (value)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                STORE_FAST               1 (s)

 259            LOAD_GLOBAL              7 (len + NULL)
                LOAD_FAST_BORROW         1 (s)
                CALL                     1
                LOAD_SMALL_INT          10
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        3 (to L2)
                NOT_TAKEN

 260            LOAD_CONST               1 (None)
                RETURN_VALUE

 261    L2:     LOAD_FAST_BORROW         1 (s)
                LOAD_CONST               2 (slice(None, 10, None))
                BINARY_OP               26 ([])
                STORE_FAST               2 (head)

 262            LOAD_FAST_BORROW         2 (head)
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

 263    L3:     LOAD_CONST               1 (None)
                RETURN_VALUE

 264    L4:     NOP

 265    L5:     LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST_BORROW         2 (head)
                LOAD_CONST               4 (slice(0, 4, None))
                BINARY_OP               26 ([])
                CALL                     1
                STORE_FAST               3 (y)

 266            LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST_BORROW         2 (head)
                LOAD_CONST               5 (slice(5, 7, None))
                BINARY_OP               26 ([])
                CALL                     1
                STORE_FAST               4 (m)

 267            LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST_BORROW         2 (head)
                LOAD_CONST               6 (slice(8, 10, None))
                BINARY_OP               26 ([])
                CALL                     1
                STORE_FAST               5 (d)

 268            LOAD_GLOBAL             11 (date + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (y, m)
                LOAD_FAST_BORROW         5 (d)
                CALL                     3
                POP_TOP

 271    L6:     LOAD_FAST_BORROW         2 (head)
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

 269            LOAD_GLOBAL             12 (ValueError)
                LOAD_GLOBAL             14 (TypeError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L9)
                NOT_TAKEN
                POP_TOP

 270    L8:     POP_EXCEPT
                LOAD_CONST               1 (None)
                RETURN_VALUE

 269    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L5 to L6 -> L7 [0]
  L7 to L8 -> L10 [1] lasti
  L9 to L10 -> L10 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "app\services\memory\review_stats.py", line 274>:
274           RESUME                   0
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

Disassembly of <code object _now_day at 0x0000018C1800B230, file "app\services\memory\review_stats.py", line 274>:
274           RESUME                   0

280           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (now)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       22 (to L1)
              NOT_TAKEN

281           LOAD_GLOBAL              5 (_parse_iso_day + NULL)
              LOAD_FAST_BORROW         0 (now)
              CALL                     1
              STORE_FAST               1 (parsed)

282           LOAD_FAST_BORROW         1 (parsed)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN

283           LOAD_FAST_BORROW         1 (parsed)
              RETURN_VALUE

284   L1:     LOAD_GLOBAL              6 (datetime)
              LOAD_ATTR                8 (now)
              PUSH_NULL
              LOAD_GLOBAL             10 (timezone)
              LOAD_ATTR               12 (utc)
              CALL                     1
              LOAD_ATTR               15 (strftime + NULL|self)
              LOAD_CONST               1 ('%Y-%m-%d')
              CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA30F0, file "app\services\memory\review_stats.py", line 287>:
287           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('day')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _empty_day_bucket at 0x0000018C17FA31E0, file "app\services\memory\review_stats.py", line 287>:
287           RESUME                   0

289           LOAD_CONST               0 ('day')
              LOAD_FAST_BORROW         0 (day)

290           LOAD_CONST               1 ('approved')
              LOAD_SMALL_INT           0

291           LOAD_CONST               2 ('rejected')
              LOAD_SMALL_INT           0

292           LOAD_CONST               3 ('expired')
              LOAD_SMALL_INT           0

293           LOAD_CONST               4 ('quarantined')
              LOAD_SMALL_INT           0

294           LOAD_CONST               5 ('total')
              LOAD_SMALL_INT           0

288           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024B30, file "app\services\memory\review_stats.py", line 298>:
298           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('events')

299           LOAD_CONST               2 ('Any')

298           LOAD_CONST               3 ('days')

301           LOAD_CONST               2 ('Any')

298           LOAD_CONST               4 ('now')

302           LOAD_CONST               5 ('Optional[str]')

298           LOAD_CONST               6 ('return')

303           LOAD_CONST               7 ('Dict[str, Any]')

298           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object bucket_review_events_by_day at 0x0000018C181DAF20, file "app\services\memory\review_stats.py", line 298>:
 298            RESUME                   0

 337            LOAD_GLOBAL              1 (_clamp_days + NULL)
                LOAD_FAST_BORROW         1 (days)
                CALL                     1
                STORE_FAST               3 (n_days)

 338            LOAD_GLOBAL              3 (_now_day + NULL)
                LOAD_FAST_BORROW         2 (now)
                CALL                     1
                STORE_FAST               4 (today_token)

 340            LOAD_GLOBAL              5 (date + NULL)

 341            LOAD_GLOBAL              7 (int + NULL)
                LOAD_FAST_BORROW         4 (today_token)
                LOAD_CONST               1 (slice(0, 4, None))
                BINARY_OP               26 ([])
                CALL                     1

 342            LOAD_GLOBAL              7 (int + NULL)
                LOAD_FAST_BORROW         4 (today_token)
                LOAD_CONST               2 (slice(5, 7, None))
                BINARY_OP               26 ([])
                CALL                     1

 343            LOAD_GLOBAL              7 (int + NULL)
                LOAD_FAST_BORROW         4 (today_token)
                LOAD_CONST               3 (slice(8, 10, None))
                BINARY_OP               26 ([])
                CALL                     1

 340            CALL                     3
                STORE_FAST               5 (today)

 347            BUILD_LIST               0
                STORE_FAST               6 (day_keys)

 348            LOAD_GLOBAL              9 (range + NULL)
                LOAD_FAST_BORROW         3 (n_days)
                LOAD_SMALL_INT           1
                BINARY_OP               10 (-)
                LOAD_CONST              23 (-1)
                LOAD_CONST              23 (-1)
                CALL                     3
                GET_ITER
        L1:     FOR_ITER                52 (to L2)
                STORE_FAST               7 (i)

 349            LOAD_FAST_BORROW         6 (day_keys)
                LOAD_ATTR               11 (append + NULL|self)
                LOAD_FAST_BORROW         5 (today)
                LOAD_GLOBAL             13 (timedelta + NULL)
                LOAD_FAST_BORROW         7 (i)
                LOAD_CONST               4 (('days',))
                CALL_KW                  1
                BINARY_OP               10 (-)
                LOAD_ATTR               15 (strftime + NULL|self)
                LOAD_CONST               5 ('%Y-%m-%d')
                CALL                     1
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           54 (to L1)

 348    L2:     END_FOR
                POP_ITER

 351            LOAD_FAST_BORROW         6 (day_keys)
                GET_ITER
                LOAD_FAST_AND_CLEAR      8 (k)
                SWAP                     2
        L3:     BUILD_MAP                0
                SWAP                     2
        L4:     FOR_ITER                14 (to L5)
                STORE_FAST_LOAD_FAST   136 (k, k)
                LOAD_GLOBAL             17 (_empty_day_bucket + NULL)
                LOAD_FAST_BORROW         8 (k)
                CALL                     1
                MAP_ADD                  2
                JUMP_BACKWARD           16 (to L4)
        L5:     END_FOR
                POP_ITER
        L6:     STORE_FAST               9 (buckets)
                STORE_FAST               8 (k)

 353            BUILD_LIST               0
                STORE_FAST              10 (warnings)

 355            LOAD_GLOBAL             19 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (events)
                LOAD_GLOBAL             20 (list)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        32 (to L11)
                NOT_TAKEN

 357            LOAD_CONST               6 ('days')
                LOAD_FAST                3 (n_days)

 358            LOAD_CONST               7 ('buckets')
                LOAD_FAST_BORROW         6 (day_keys)
                GET_ITER
                LOAD_FAST_AND_CLEAR      8 (k)
                SWAP                     2
        L7:     BUILD_LIST               0
                SWAP                     2
        L8:     FOR_ITER                11 (to L9)
                STORE_FAST_LOAD_FAST   137 (k, buckets)
                LOAD_FAST_BORROW         8 (k)
                BINARY_OP               26 ([])
                LIST_APPEND              2
                JUMP_BACKWARD           13 (to L8)
        L9:     END_FOR
                POP_ITER
       L10:     SWAP                     2
                STORE_FAST               8 (k)

 359            LOAD_CONST               8 ('warnings')
                LOAD_CONST               9 ('unexpected_events_shape')
                BUILD_LIST               1

 356            BUILD_MAP                3
                RETURN_VALUE

 362   L11:     LOAD_SMALL_INT           0
                STORE_FAST              11 (unknown_status_seen)

 363            LOAD_SMALL_INT           0
                STORE_FAST              12 (bad_date_seen)

 365            LOAD_FAST_BORROW         0 (events)
                GET_ITER
       L12:     EXTENDED_ARG             1
                FOR_ITER               285 (to L21)
                STORE_FAST              13 (raw)

 366            LOAD_GLOBAL             19 (isinstance + NULL)
                LOAD_FAST_BORROW        13 (raw)
                LOAD_GLOBAL             22 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        12 (to L13)
                NOT_TAKEN

 367            LOAD_FAST_BORROW        11 (unknown_status_seen)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST              11 (unknown_status_seen)

 368            JUMP_BACKWARD           37 (to L12)

 369   L13:     LOAD_GLOBAL             25 (_safe_str + NULL)
                LOAD_FAST_BORROW        13 (raw)
                LOAD_ATTR               27 (get + NULL|self)
                LOAD_CONST              10 ('to_status')
                CALL                     1
                CALL                     1
                STORE_FAST              14 (to_status)

 370            LOAD_FAST_BORROW        14 (to_status)
                LOAD_GLOBAL             28 (ALLOWED_TO_STATUSES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       12 (to L14)
                NOT_TAKEN

 371            LOAD_FAST_BORROW        11 (unknown_status_seen)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST              11 (unknown_status_seen)

 372            JUMP_BACKWARD           85 (to L12)

 373   L14:     LOAD_GLOBAL             31 (_parse_iso_day + NULL)
                LOAD_FAST_BORROW        13 (raw)
                LOAD_ATTR               27 (get + NULL|self)
                LOAD_CONST              11 ('created_at')
                CALL                     1
                CALL                     1
                STORE_FAST              15 (day_key)

 374            LOAD_FAST_BORROW        15 (day_key)
                POP_JUMP_IF_NOT_NONE    12 (to L15)
                NOT_TAKEN

 375            LOAD_FAST_BORROW        12 (bad_date_seen)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST              12 (bad_date_seen)

 376            JUMP_BACKWARD          126 (to L12)

 377   L15:     LOAD_FAST_BORROW         9 (buckets)
                LOAD_ATTR               27 (get + NULL|self)
                LOAD_FAST_BORROW        15 (day_key)
                CALL                     1
                STORE_FAST              16 (bucket)

 378            LOAD_FAST_BORROW        16 (bucket)
                POP_JUMP_IF_NOT_NONE     3 (to L16)
                NOT_TAKEN

 380            JUMP_BACKWARD          149 (to L12)

 381   L16:     LOAD_FAST_BORROW        14 (to_status)
                LOAD_CONST              12 ('APPROVED')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       23 (to L17)
                NOT_TAKEN

 382            LOAD_FAST_BORROW        16 (bucket)
                LOAD_CONST              13 ('approved')
                COPY                     2
                COPY                     2
                BINARY_OP               26 ([])
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                SWAP                     3
                SWAP                     2
                STORE_SUBSCR
                JUMP_FORWARD            86 (to L20)

 383   L17:     LOAD_FAST_BORROW        14 (to_status)
                LOAD_CONST              14 ('REJECTED')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       23 (to L18)
                NOT_TAKEN

 384            LOAD_FAST_BORROW        16 (bucket)
                LOAD_CONST              15 ('rejected')
                COPY                     2
                COPY                     2
                BINARY_OP               26 ([])
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                SWAP                     3
                SWAP                     2
                STORE_SUBSCR
                JUMP_FORWARD            57 (to L20)

 385   L18:     LOAD_FAST_BORROW        14 (to_status)
                LOAD_CONST              16 ('EXPIRED')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       23 (to L19)
                NOT_TAKEN

 386            LOAD_FAST_BORROW        16 (bucket)
                LOAD_CONST              17 ('expired')
                COPY                     2
                COPY                     2
                BINARY_OP               26 ([])
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                SWAP                     3
                SWAP                     2
                STORE_SUBSCR
                JUMP_FORWARD            28 (to L20)

 387   L19:     LOAD_FAST_BORROW        14 (to_status)
                LOAD_CONST              18 ('QUARANTINED')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       22 (to L20)
                NOT_TAKEN

 388            LOAD_FAST_BORROW        16 (bucket)
                LOAD_CONST              19 ('quarantined')
                COPY                     2
                COPY                     2
                BINARY_OP               26 ([])
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                SWAP                     3
                SWAP                     2
                STORE_SUBSCR

 389   L20:     LOAD_FAST_BORROW        16 (bucket)
                LOAD_CONST              20 ('total')
                COPY                     2
                COPY                     2
                BINARY_OP               26 ([])
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                SWAP                     3
                SWAP                     2
                STORE_SUBSCR
                EXTENDED_ARG             1
                JUMP_BACKWARD          288 (to L12)

 365   L21:     END_FOR
                POP_ITER

 391            LOAD_FAST_BORROW        11 (unknown_status_seen)
                TO_BOOL
                POP_JUMP_IF_FALSE       21 (to L22)
                NOT_TAKEN

 392            LOAD_FAST_BORROW        10 (warnings)
                LOAD_ATTR               11 (append + NULL|self)
                LOAD_CONST              21 ('unknown_status_events_ignored:')
                LOAD_FAST_BORROW        11 (unknown_status_seen)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 393   L22:     LOAD_FAST_BORROW        12 (bad_date_seen)
                TO_BOOL
                POP_JUMP_IF_FALSE       21 (to L23)
                NOT_TAKEN

 394            LOAD_FAST_BORROW        10 (warnings)
                LOAD_ATTR               11 (append + NULL|self)
                LOAD_CONST              22 ('malformed_created_at_ignored:')
                LOAD_FAST_BORROW        12 (bad_date_seen)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 397   L23:     LOAD_CONST               6 ('days')
                LOAD_FAST                3 (n_days)

 398            LOAD_CONST               7 ('buckets')
                LOAD_FAST_BORROW         6 (day_keys)
                GET_ITER
                LOAD_FAST_AND_CLEAR      8 (k)
                SWAP                     2
       L24:     BUILD_LIST               0
                SWAP                     2
       L25:     FOR_ITER                11 (to L26)
                STORE_FAST_LOAD_FAST   137 (k, buckets)
                LOAD_FAST_BORROW         8 (k)
                BINARY_OP               26 ([])
                LIST_APPEND              2
                JUMP_BACKWARD           13 (to L25)
       L26:     END_FOR
                POP_ITER
       L27:     SWAP                     2
                STORE_FAST               8 (k)

 399            LOAD_CONST               8 ('warnings')
                LOAD_FAST_BORROW        10 (warnings)

 396            BUILD_MAP                3
                RETURN_VALUE

  --   L28:     SWAP                     2
                POP_TOP

 351            SWAP                     2
                STORE_FAST               8 (k)
                RERAISE                  0

  --   L29:     SWAP                     2
                POP_TOP

 358            SWAP                     2
                STORE_FAST               8 (k)
                RERAISE                  0

  --   L30:     SWAP                     2
                POP_TOP

 398            SWAP                     2
                STORE_FAST               8 (k)
                RERAISE                  0
ExceptionTable:
  L3 to L6 -> L28 [2]
  L7 to L10 -> L29 [5]
  L24 to L27 -> L30 [5]

Disassembly of <code object __annotate__ at 0x0000018C17FA1D40, file "app\services\memory\review_stats.py", line 407>:
407           RESUME                   0
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

Disassembly of <code object _clamp_limit at 0x0000018C17FF1230, file "app\services\memory\review_stats.py", line 407>:
 407           RESUME                   0

 409           LOAD_FAST_BORROW         0 (value)
               POP_JUMP_IF_NOT_NONE     7 (to L1)
               NOT_TAKEN

 410           LOAD_GLOBAL              0 (_DEFAULT_STATS_LIMIT)
               RETURN_VALUE

 411   L1:     NOP

 412   L2:     LOAD_GLOBAL              3 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               1 (n)

 415   L3:     LOAD_FAST                1 (n)
               LOAD_SMALL_INT           0
               COMPARE_OP              58 (bool(<=))
               POP_JUMP_IF_FALSE        7 (to L4)
               NOT_TAKEN

 416           LOAD_GLOBAL              0 (_DEFAULT_STATS_LIMIT)
               RETURN_VALUE

 417   L4:     LOAD_GLOBAL              9 (min + NULL)
               LOAD_FAST                1 (n)
               LOAD_GLOBAL             10 (_MAX_STATS_LIMIT)
               CALL                     2
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 413           LOAD_GLOBAL              4 (TypeError)
               LOAD_GLOBAL              6 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       10 (to L7)
               NOT_TAKEN
               POP_TOP

 414           LOAD_GLOBAL              0 (_DEFAULT_STATS_LIMIT)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

 413   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "app\services\memory\review_stats.py", line 420>:
420           RESUME                   0
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

Disassembly of <code object _coerce_since at 0x0000018C1794EBB0, file "app\services\memory\review_stats.py", line 420>:
420           RESUME                   0

432           LOAD_FAST_BORROW         0 (value)
              POP_JUMP_IF_NOT_NONE     3 (to L1)
              NOT_TAKEN

433           LOAD_CONST               4 ((None, None))
              RETURN_VALUE

434   L1:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

435           LOAD_CONST               5 ((None, 'since_ignored_non_string'))
              RETURN_VALUE

436   L2:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

437           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN

438           LOAD_CONST               4 ((None, None))
              RETURN_VALUE

442   L3:     LOAD_GLOBAL              7 (len + NULL)
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

443   L4:     LOAD_CONST               6 ((None, 'since_ignored_invalid_format'))
              RETURN_VALUE

444   L5:     LOAD_FAST_BORROW         1 (s)
              LOAD_CONST               1 (None)
              BUILD_TUPLE              2
              RETURN_VALUE

Disassembly of <code object _get_db at 0x0000018C17FA23D0, file "app\services\memory\review_stats.py", line 447>:
447           RESUME                   0

449           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('get_supabase',))
              IMPORT_NAME              0 (app.db.supabase_client)
              IMPORT_FROM              1 (get_supabase)
              STORE_FAST               0 (get_supabase)
              POP_TOP

450           LOAD_FAST_BORROW         0 (get_supabase)
              PUSH_NULL
              CALL                     0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024E30, file "app\services\memory\review_stats.py", line 453>:
453           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

454           LOAD_CONST               2 ('str')

453           LOAD_CONST               3 ('since')

456           LOAD_CONST               4 ('Optional[str]')

453           LOAD_CONST               5 ('limit')

457           LOAD_CONST               6 ('int')

453           LOAD_CONST               7 ('return')

458           LOAD_CONST               8 ('Tuple[List[Dict[str, Any]], List[str]]')

453           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object _list_review_events_for_brokerage at 0x0000018C17D79E90, file "app\services\memory\review_stats.py", line 453>:
 453            RESUME                   0

 469            BUILD_LIST               0
                STORE_FAST               3 (warnings)

 470            NOP

 471    L1:     LOAD_GLOBAL              1 (_get_db + NULL)
                CALL                     0
                STORE_FAST               4 (db)

 473            LOAD_FAST_BORROW         4 (db)
                LOAD_ATTR                3 (table + NULL|self)
                LOAD_GLOBAL              4 (_TABLE_REVIEW)
                CALL                     1

 474            LOAD_ATTR                7 (select + NULL|self)
                LOAD_CONST               1 ('review_id, to_status, actor_type, actor_id, created_at')
                CALL                     1

 475            LOAD_ATTR                9 (eq + NULL|self)
                LOAD_CONST               2 ('brokerage_id')
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     2

 476            LOAD_ATTR               11 (order + NULL|self)
                LOAD_CONST               3 ('created_at')
                LOAD_CONST               4 (True)
                LOAD_CONST               5 (('desc',))
                CALL_KW                  2

 477            LOAD_ATTR               13 (limit + NULL|self)
                LOAD_FAST_BORROW         2 (limit)
                CALL                     1

 472            STORE_FAST               5 (query)

 479            LOAD_FAST_BORROW         1 (since)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L2)
                NOT_TAKEN

 480            LOAD_FAST_BORROW         5 (query)
                LOAD_ATTR               15 (gte + NULL|self)
                LOAD_CONST               3 ('created_at')
                LOAD_FAST_BORROW         1 (since)
                CALL                     2
                STORE_FAST               5 (query)

 481    L2:     LOAD_FAST_BORROW         5 (query)
                LOAD_ATTR               17 (execute + NULL|self)
                CALL                     0
                STORE_FAST               6 (result)

 482            LOAD_GLOBAL             19 (list + NULL)
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

 490    L6:     LOAD_GLOBAL             33 (isinstance + NULL)
                LOAD_FAST                7 (rows)
                LOAD_GLOBAL             18 (list)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         6 (to L7)
                NOT_TAKEN

 491            BUILD_LIST               0
                LOAD_CONST              11 ('unexpected_reader_shape')
                BUILD_LIST               1
                BUILD_TUPLE              2
                RETURN_VALUE

 492    L7:     LOAD_GLOBAL             35 (len + NULL)
                LOAD_FAST                7 (rows)
                CALL                     1
                LOAD_FAST                2 (limit)
                COMPARE_OP             188 (bool(>=))
                POP_JUMP_IF_FALSE       18 (to L8)
                NOT_TAKEN

 493            LOAD_FAST                3 (warnings)
                LOAD_ATTR               37 (append + NULL|self)
                LOAD_CONST              12 ('result_truncated_at_limit')
                CALL                     1
                POP_TOP

 494    L8:     LOAD_FAST_LOAD_FAST    115 (rows, warnings)
                BUILD_TUPLE              2
                RETURN_VALUE

  --    L9:     PUSH_EXC_INFO

 483            LOAD_GLOBAL             22 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       84 (to L14)
                NOT_TAKEN
                STORE_FAST               8 (e)

 484   L10:     LOAD_GLOBAL             24 (logger)
                LOAD_ATTR               27 (warning + NULL|self)

 485            LOAD_CONST               8 ('review_stats reader failed (non-critical) | brokerage=')

 486            LOAD_FAST                0 (brokerage_id)
                FORMAT_SIMPLE
                LOAD_CONST               9 (' | error_type=')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE

 485            BUILD_STRING             4

 484            CALL                     1
                POP_TOP

 488            BUILD_LIST               0
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

 483   L14:     RERAISE                  0

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

Disassembly of <code object __annotate__ at 0x0000018C18025930, file "app\services\memory\review_stats.py", line 501>:
501           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

502           LOAD_CONST               2 ('Any')

501           LOAD_CONST               3 ('since')

503           LOAD_CONST               2 ('Any')

501           LOAD_CONST               4 ('limit')

504           LOAD_CONST               2 ('Any')

501           LOAD_CONST               5 ('days')

505           LOAD_CONST               2 ('Any')

501           LOAD_CONST               6 ('return')

506           LOAD_CONST               7 ('Dict[str, Any]')

501           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object review_stats_for_brokerage at 0x0000018C181DB7D0, file "app\services\memory\review_stats.py", line 501>:
501           RESUME                   0

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
              POP_JUMP_IF_TRUE         8 (to L2)
              NOT_TAKEN

527   L1:     LOAD_CONST               1 ('status')
              LOAD_CONST               2 ('failed')

528           LOAD_CONST               3 ('errors')
              LOAD_CONST               4 ('missing_brokerage_id')
              BUILD_LIST               1

526           BUILD_MAP                2
              RETURN_VALUE

530   L2:     LOAD_FAST_BORROW         0 (brokerage_id)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               0 (brokerage_id)

532           LOAD_GLOBAL              7 (_coerce_since + NULL)
              LOAD_FAST_BORROW         1 (since)
              CALL                     1
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST   69 (cleaned_since, since_warning)

533           LOAD_GLOBAL              9 (_clamp_limit + NULL)
              LOAD_FAST_BORROW         2 (limit)
              CALL                     1
              STORE_FAST               6 (capped)

534           LOAD_GLOBAL             11 (_clamp_days + NULL)
              LOAD_FAST_BORROW         3 (days)
              CALL                     1
              STORE_FAST               7 (capped_days)

536           LOAD_GLOBAL             13 (_list_review_events_for_brokerage + NULL)

537           LOAD_FAST_BORROW_LOAD_FAST_BORROW 4 (brokerage_id, cleaned_since)
              LOAD_FAST_BORROW         6 (capped)

536           LOAD_CONST               5 (('since', 'limit'))
              CALL_KW                  3
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST  137 (rows, reader_warnings)

540           LOAD_GLOBAL             15 (summarize_review_events + NULL)
              LOAD_FAST_BORROW         8 (rows)
              CALL                     1
              STORE_FAST              10 (summary)

543           LOAD_GLOBAL             17 (bucket_review_events_by_day + NULL)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 135 (rows, capped_days)
              LOAD_CONST               6 (('days',))
              CALL_KW                  2
              STORE_FAST              11 (by_day)

546           LOAD_CONST               1 ('status')
              LOAD_CONST               7 ('ok')

547           LOAD_CONST               8 ('brokerage_id')
              LOAD_FAST_BORROW         0 (brokerage_id)

548           LOAD_CONST               9 ('since')
              LOAD_FAST_BORROW         4 (cleaned_since)

549           LOAD_CONST              10 ('limit')
              LOAD_FAST_BORROW         6 (capped)

550           LOAD_CONST              11 ('total_events')
              LOAD_FAST_BORROW        10 (summary)
              LOAD_CONST              11 ('total_events')
              BINARY_OP               26 ([])

551           LOAD_CONST              12 ('by_to_status')
              LOAD_FAST_BORROW        10 (summary)
              LOAD_CONST              12 ('by_to_status')
              BINARY_OP               26 ([])

552           LOAD_CONST              13 ('by_actor')
              LOAD_FAST_BORROW        10 (summary)
              LOAD_CONST              13 ('by_actor')
              BINARY_OP               26 ([])

553           LOAD_CONST              14 ('by_day')
              LOAD_FAST_BORROW        11 (by_day)

554           LOAD_CONST              15 ('warnings')
              LOAD_GLOBAL             19 (list + NULL)
              LOAD_FAST_BORROW        10 (summary)
              LOAD_CONST              15 ('warnings')
              BINARY_OP               26 ([])
              CALL                     1

545           BUILD_MAP                9
              STORE_FAST              12 (out)

556           LOAD_FAST_BORROW         5 (since_warning)
              TO_BOOL
              POP_JUMP_IF_FALSE       25 (to L3)
              NOT_TAKEN

557           LOAD_FAST_BORROW        12 (out)
              LOAD_CONST              15 ('warnings')
              BINARY_OP               26 ([])
              LOAD_ATTR               21 (append + NULL|self)
              LOAD_FAST_BORROW         5 (since_warning)
              CALL                     1
              POP_TOP

558   L3:     LOAD_FAST_BORROW        12 (out)
              LOAD_CONST              15 ('warnings')
              BINARY_OP               26 ([])
              LOAD_ATTR               23 (extend + NULL|self)
              LOAD_FAST_BORROW         9 (reader_warnings)
              CALL                     1
              POP_TOP

562           LOAD_FAST_BORROW        11 (by_day)
              LOAD_ATTR               25 (get + NULL|self)
              LOAD_CONST              15 ('warnings')
              BUILD_LIST               0
              CALL                     2
              GET_ITER
      L4:     FOR_ITER                42 (to L6)
              STORE_FAST              13 (w)

563           LOAD_FAST_BORROW_LOAD_FAST_BORROW 220 (w, out)
              LOAD_CONST              15 ('warnings')
              BINARY_OP               26 ([])
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              JUMP_BACKWARD           18 (to L4)

564   L5:     LOAD_FAST_BORROW        12 (out)
              LOAD_CONST              15 ('warnings')
              BINARY_OP               26 ([])
              LOAD_ATTR               21 (append + NULL|self)
              LOAD_FAST_BORROW        13 (w)
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           44 (to L4)

562   L6:     END_FOR
              POP_ITER

565           LOAD_FAST_BORROW        12 (out)
              RETURN_VALUE
```
