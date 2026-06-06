# memory/review_actors

- **pyc:** `app\services\memory\__pycache__\review_actors.cpython-314.pyc`
- **expected source path (absent):** `app\services\memory/review_actors.py`
- **co_filename (from bytecode):** `app\services\memory\review_actors.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** memory

## Module docstring

```
PAS154 — Memory review actor catalog (read-only, structural).

Bounded, tenant-scoped read of the PAS144C ``pas_memory_review_
events`` audit table that PAS150 / PAS151 / PAS152 / PAS153 already
project. Returns a structural catalog of *known actors* for a
brokerage — ``actor_id`` plus terminal-status counters plus a
``last_seen`` timestamp — so the PAS153 ``actor_id`` filter input
can offer operators a dropdown of seen identifiers rather than
freeform typing.

Hard contract:
  * **Tenant-scoped.** Every public helper that touches Supabase
    requires ``brokerage_id``. There is no unscoped path.
  * **Bounded.** ``review_actors_for_brokerage`` caps the row fetch
    at ``_MAX_ACTORS_LIMIT`` (500, mirrors PAS150 / PAS152). The
    query is ``WHERE brokerage_id = ? ORDER BY created_at DESC
    LIMIT n`` — NOT a full-table scan.
  * **Structural output only.** Counts, status tokens, an
    ``actor_id`` identifier, and a single ``last_seen`` timestamp.
    Reason text, metadata JSONB, evidence, transcript, raw prompts
    and lineage are NEVER read or surfaced. The summariser
    physically does not look at those keys.
  * **Fail-closed.** Bad input, reader failure, malformed event row
    — every path returns a structured envelope. Nothing in this
    module raises.

Public surface:
  - summarize_review_actors(events)                      -> dict
  - review_actors_for_brokerage(brokerage_id,
                                 since=None,
                                 limit=500)              -> dict
  - ALLOWED_TO_STATUSES, ALLOWED_ACTOR_TYPES,
    _MAX_ACTORS_LIMIT
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `Tuple`, `__future__`, `annotations`, `app.db.supabase_client`, `get_supabase`, `logging`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_clamp_limit`, `_coerce_since`, `_get_db`, `_list_review_events_for_brokerage`, `_safe_str`, `review_actors_for_brokerage`, `summarize_review_actors`

## Env-key candidates

`APPROVED`, `EXPIRED`, `QUARANTINED`, `REJECTED`, `UNKNOWN`

## String constants (redacted where noted)

- '\nPAS154 — Memory review actor catalog (read-only, structural).\n\nBounded, tenant-scoped read of the PAS144C ``pas_memory_review_\nevents`` audit table that PAS150 / PAS151 / PAS152 / PAS153 already\nproject. Returns a structural catalog of *known actors* for a\nbrokerage — ``actor_id`` plus terminal-status counters plus a\n``last_seen`` timestamp — so the PAS153 ``actor_id`` filter input\ncan offer operators a dropdown of seen identifiers rather than\nfreeform typing.\n\nHard contract:\n  * **Tenant-scoped.** Every public helper that touches Supabase\n    requires ``brokerage_id``. There is no unscoped path.\n  * **Bounded.** ``review_actors_for_brokerage`` caps the row fetch\n    at ``_MAX_ACTORS_LIMIT`` (500, mirrors PAS150 / PAS152). The\n    query is ``WHERE brokerage_id = ? ORDER BY created_at DESC\n    LIMIT n`` — NOT a full-table scan.\n  * **Structural output only.** Counts, status tokens, an\n    ``actor_id`` identifier, and a single ``last_seen`` timestamp.\n    Reason text, metadata JSONB, evidence, transcript, raw prompts\n    and lineage are NEVER read or surfaced. The summariser\n    physically does not look at those keys.\n  * **Fail-closed.** Bad input, reader failure, malformed event row\n    — every path returns a structured envelope. Nothing in this\n    module raises.\n\nPublic surface:\n  - summarize_review_actors(events)                      -> dict\n  - review_actors_for_brokerage(brokerage_id,\n                                 since=None,\n                                 limit=500)              -> dict\n  - ALLOWED_TO_STATUSES, ALLOWED_ACTOR_TYPES,\n    _MAX_ACTORS_LIMIT\n'
- 'pas.memory.review_actors'
- 'pas_memory_review_events'
- 'since'
- 'limit'
- 'val'
- 'Any'
- 'return'
- 'Optional[str]'
- 'Return a trimmed string for non-empty ``val`` or None.'
- 'value'
- 'int'
- 'Coerce a caller-supplied limit; clamp to [1, _MAX_ACTORS_LIMIT].'
- 'Tuple[Optional[str], Optional[str]]'
- 'Coerce caller-supplied ``since``. Mirrors the helpers in\nreview_stats / review_export so a future widening over there\ncannot silently affect the actor-catalog surface.'
- 'events'
- 'Dict[str, Any]'
- 'Project a list of audit-event rows into a structural actor\ncatalog. Pure — no I/O, no logging, no raises.\n\nEach row is read for ONLY these keys: ``actor_id``,\n``actor_type``, ``to_status``, ``created_at``. Every other key\non the row — including ``reason``, ``metadata``, ``evidence``,\n``transcript``, ``review_id``, ``memory_id``, ``brokerage_id``,\n``from_status`` — is ignored on purpose.\n\nReturns:\n    {\n        "status":       "ok",\n        "actor_count":  <int>,\n        "actors": [\n            {\n                "actor_id":         str,\n                "actor_type":       str,   # closed enum or UNKNOWN\n                "total_decisions":  int,\n                "approved":         int,\n                "rejected":         int,\n                "expired":          int,\n                "quarantined":      int,\n                "last_seen":        str,   # max created_at for actor\n            },\n            ...\n        ],\n        "warnings":     list[str],\n    }\n\nGrouping: by ``(actor_id, actor_type)`` — the same actor_id seen\nunder two different actor_types is split into two rows so a\nregressed writer cannot silently merge them.\n\nOrdering: total_decisions descending, then actor_id ascending.\nStable for test pinning and operator UX.\n\nFailure semantics:\n    * Non-list input → empty catalog + ``unexpected_events_\n      shape`` warning.\n    * Unknown ``to_status`` → row dropped silently, aggregate\n      ``unknown_status_events_ignored:<n>`` warning surfaced.\n    * Missing / non-string ``actor_id`` → bucketed as\n      ``"unknown"``.\n    * Missing / non-string ``actor_type`` → bucketed as\n      ``"UNKNOWN"``.\n'
- 'status'
- 'actor_count'
- 'actors'
- 'warnings'
- 'unexpected_events_shape'
- 'to_status'
- 'actor_id'
- 'unknown'
- 'actor_type'
- 'UNKNOWN'
- 'created_at'
- 'total_decisions'
- 'approved'
- 'rejected'
- 'expired'
- 'quarantined'
- 'last_seen'
- 'APPROVED'
- 'REJECTED'
- 'EXPIRED'
- 'QUARANTINED'
- 'unknown_status_events_ignored:'
- 'Lazy Supabase resolver. Mirrors review_stats / review_export.'
- 'brokerage_id'
- 'str'
- 'Tuple[List[Dict[str, Any]], List[str]]'
- 'Tenant-scoped, bounded fetch of audit-event rows.\n\nSELECT projection is exactly the four columns the actor-\nsummariser needs (``actor_id, actor_type, to_status,\ncreated_at``). It explicitly excludes ``metadata``, ``reason``,\n``from_status``, ``memory_id``, ``review_id``, ``brokerage_id``,\n``evidence``, ``transcript``, ``lineage``, ``memory_content``\nfrom the projection.\n\nReturns (rows, warnings). Never raises. Returns ([], [token])\non any Supabase failure.\n'
- 'actor_id, actor_type, to_status, created_at'
- 'data'
- 'review_actors reader failed (non-critical) | brokerage='
- ' | error_type='
- 'reader_failed:'
- 'unexpected_reader_shape'
- 'result_truncated_at_limit'
- 'Return the closed-shape actor catalog for one tenant.\n\n``brokerage_id`` is REQUIRED. There is no path through this\nhelper that omits the tenant filter or falls back to a cross-\ntenant scan.\n\nResponse (always 200 from the route caller\'s perspective):\n    {\n        "status":       "ok" | "failed",\n        "brokerage_id": "<id>",\n        "since":        "<iso-8601 or null>",\n        "limit":        <int>,\n        "actor_count":  <int>,\n        "actors":       [<actor row>, ...],\n        "warnings":     [<str>, ...],\n    }\n'
- 'failed'
- 'errors'
- 'missing_brokerage_id'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS154 — Memory review actor catalog (read-only, structural).\n\nBounded, tenant-scoped read of the PAS144C ``pas_memory_review_\nevents`` audit table that PAS150 / PAS151 / PAS152 / PAS153 already\nproject. Returns a structural catalog of *known actors* for a\nbrokerage — ``actor_id`` plus terminal-status counters plus a\n``last_seen`` timestamp — so the PAS153 ``actor_id`` filter input\ncan offer operators a dropdown of seen identifiers rather than\nfreeform typing.\n\nHard contract:\n  * **Tenant-scoped.** Every public helper that touches Supabase\n    requires ``brokerage_id``. There is no unscoped path.\n  * **Bounded.** ``review_actors_for_brokerage`` caps the row fetch\n    at ``_MAX_ACTORS_LIMIT`` (500, mirrors PAS150 / PAS152). The\n    query is ``WHERE brokerage_id = ? ORDER BY created_at DESC\n    LIMIT n`` — NOT a full-table scan.\n  * **Structural output only.** Counts, status tokens, an\n    ``actor_id`` identifier, and a single ``last_seen`` timestamp.\n    Reason text, metadata JSONB, evidence, transcript, raw prompts\n    and lineage are NEVER read or surfaced. The summariser\n    physically does not look at those keys.\n  * **Fail-closed.** Bad input, reader failure, malformed event row\n    — every path returns a structured envelope. Nothing in this\n    module raises.\n\nPublic surface:\n  - summarize_review_actors(events)                      -> dict\n  - review_actors_for_brokerage(brokerage_id,\n                                 since=None,\n                                 limit=500)              -> dict\n  - ALLOWED_TO_STATUSES, ALLOWED_ACTOR_TYPES,\n    _MAX_ACTORS_LIMIT\n')
              STORE_NAME               0 (__doc__)

 37           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 39           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 40           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('Any', 'Dict', 'List', 'Optional', 'Tuple'))
              IMPORT_NAME              4 (typing)
              IMPORT_FROM              5 (Any)
              STORE_NAME               5 (Any)
              IMPORT_FROM              6 (Dict)
              STORE_NAME               6 (Dict)
              IMPORT_FROM              7 (List)
              STORE_NAME               7 (List)
              IMPORT_FROM              8 (Optional)
              STORE_NAME               8 (Optional)
              IMPORT_FROM              9 (Tuple)
              STORE_NAME               9 (Tuple)
              POP_TOP

 42           LOAD_NAME                3 (logging)
              LOAD_ATTR               20 (getLogger)
              PUSH_NULL
              LOAD_CONST               4 ('pas.memory.review_actors')
              CALL                     1
              STORE_NAME              11 (logger)

 46           LOAD_CONST              22 (('APPROVED', 'REJECTED', 'EXPIRED', 'QUARANTINED'))
              STORE_NAME              12 (ALLOWED_TO_STATUSES)

 47           LOAD_CONST              23 (('OPERATOR', 'SYSTEM', 'ADMIN', 'SECURITY'))
              STORE_NAME              13 (ALLOWED_ACTOR_TYPES)

 51           LOAD_CONST               5 (500)
              STORE_NAME              14 (_MAX_ACTORS_LIMIT)

 52           LOAD_CONST               5 (500)
              STORE_NAME              15 (_DEFAULT_ACTORS_LIMIT)

 54           LOAD_CONST               6 ('pas_memory_review_events')
              STORE_NAME              16 (_TABLE_REVIEW)

 63           LOAD_CONST               7 (<code object __annotate__ at 0x0000018C17FA2D30, file "app\services\memory\review_actors.py", line 63>)
              MAKE_FUNCTION
              LOAD_CONST               8 (<code object _safe_str at 0x0000018C18038F30, file "app\services\memory\review_actors.py", line 63>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              17 (_safe_str)

 71           LOAD_CONST               9 (<code object __annotate__ at 0x0000018C17FA2A60, file "app\services\memory\review_actors.py", line 71>)
              MAKE_FUNCTION
              LOAD_CONST              10 (<code object _clamp_limit at 0x0000018C17FF10B0, file "app\services\memory\review_actors.py", line 71>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              18 (_clamp_limit)

 84           LOAD_CONST              11 (<code object __annotate__ at 0x0000018C17FA3690, file "app\services\memory\review_actors.py", line 84>)
              MAKE_FUNCTION
              LOAD_CONST              12 (<code object _coerce_since at 0x0000018C1794E810, file "app\services\memory\review_actors.py", line 84>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              19 (_coerce_since)

104           LOAD_CONST              13 (<code object __annotate__ at 0x0000018C17FA35A0, file "app\services\memory\review_actors.py", line 104>)
              MAKE_FUNCTION
              LOAD_CONST              14 (<code object summarize_review_actors at 0x0000018C17E93810, file "app\services\memory\review_actors.py", line 104>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              20 (summarize_review_actors)

233           LOAD_CONST              15 (<code object _get_db at 0x0000018C17FA3780, file "app\services\memory\review_actors.py", line 233>)
              MAKE_FUNCTION
              STORE_NAME              21 (_get_db)

239           LOAD_CONST              16 ('since')

242           LOAD_CONST               2 (None)

239           LOAD_CONST              17 ('limit')

243           LOAD_NAME               15 (_DEFAULT_ACTORS_LIMIT)

239           BUILD_MAP                2
              LOAD_CONST              18 (<code object __annotate__ at 0x0000018C18025C30, file "app\services\memory\review_actors.py", line 239>)
              MAKE_FUNCTION
              LOAD_CONST              19 (<code object _list_review_events_for_brokerage at 0x0000018C17D79E90, file "app\services\memory\review_actors.py", line 239>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              22 (_list_review_events_for_brokerage)

291           LOAD_CONST               2 (None)

292           LOAD_NAME               15 (_DEFAULT_ACTORS_LIMIT)

289           BUILD_TUPLE              2
              LOAD_CONST              20 (<code object __annotate__ at 0x0000018C18024930, file "app\services\memory\review_actors.py", line 289>)
              MAKE_FUNCTION
              LOAD_CONST              21 (<code object review_actors_for_brokerage at 0x0000018C17E93D70, file "app\services\memory\review_actors.py", line 289>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              23 (review_actors_for_brokerage)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "app\services\memory\review_actors.py", line 63>:
 63           RESUME                   0
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

Disassembly of <code object _safe_str at 0x0000018C18038F30, file "app\services\memory\review_actors.py", line 63>:
 63           RESUME                   0

 65           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (val)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

 66           LOAD_CONST               1 (None)
              RETURN_VALUE

 67   L1:     LOAD_FAST_BORROW         0 (val)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

 68           LOAD_FAST                1 (s)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 (None)
      L2:     RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "app\services\memory\review_actors.py", line 71>:
 71           RESUME                   0
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

Disassembly of <code object _clamp_limit at 0x0000018C17FF10B0, file "app\services\memory\review_actors.py", line 71>:
  71           RESUME                   0

  73           LOAD_FAST_BORROW         0 (value)
               POP_JUMP_IF_NOT_NONE     7 (to L1)
               NOT_TAKEN

  74           LOAD_GLOBAL              0 (_DEFAULT_ACTORS_LIMIT)
               RETURN_VALUE

  75   L1:     NOP

  76   L2:     LOAD_GLOBAL              3 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               1 (n)

  79   L3:     LOAD_FAST                1 (n)
               LOAD_SMALL_INT           0
               COMPARE_OP              58 (bool(<=))
               POP_JUMP_IF_FALSE        7 (to L4)
               NOT_TAKEN

  80           LOAD_GLOBAL              0 (_DEFAULT_ACTORS_LIMIT)
               RETURN_VALUE

  81   L4:     LOAD_GLOBAL              9 (min + NULL)
               LOAD_FAST                1 (n)
               LOAD_GLOBAL             10 (_MAX_ACTORS_LIMIT)
               CALL                     2
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

  77           LOAD_GLOBAL              4 (TypeError)
               LOAD_GLOBAL              6 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       10 (to L7)
               NOT_TAKEN
               POP_TOP

  78           LOAD_GLOBAL              0 (_DEFAULT_ACTORS_LIMIT)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

  77   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "app\services\memory\review_actors.py", line 84>:
 84           RESUME                   0
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

Disassembly of <code object _coerce_since at 0x0000018C1794E810, file "app\services\memory\review_actors.py", line 84>:
 84           RESUME                   0

 88           LOAD_FAST_BORROW         0 (value)
              POP_JUMP_IF_NOT_NONE     3 (to L1)
              NOT_TAKEN

 89           LOAD_CONST               4 ((None, None))
              RETURN_VALUE

 90   L1:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

 91           LOAD_CONST               5 ((None, 'since_ignored_non_string'))
              RETURN_VALUE

 92   L2:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

 93           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN

 94           LOAD_CONST               4 ((None, None))
              RETURN_VALUE

 95   L3:     LOAD_GLOBAL              7 (len + NULL)
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

 96   L4:     LOAD_CONST               6 ((None, 'since_ignored_invalid_format'))
              RETURN_VALUE

 97   L5:     LOAD_FAST_BORROW         1 (s)
              LOAD_CONST               1 (None)
              BUILD_TUPLE              2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "app\services\memory\review_actors.py", line 104>:
104           RESUME                   0
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

Disassembly of <code object summarize_review_actors at 0x0000018C17E93810, file "app\services\memory\review_actors.py", line 104>:
104            RESUME                   0

152            LOAD_CONST               1 ('status')
               LOAD_CONST               2 ('ok')

153            LOAD_CONST               3 ('actor_count')
               LOAD_SMALL_INT           0

154            LOAD_CONST               4 ('actors')
               BUILD_LIST               0

155            LOAD_CONST               5 ('warnings')
               BUILD_LIST               0

151            BUILD_MAP                4
               STORE_FAST               1 (summary)

158            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (events)
               LOAD_GLOBAL              2 (list)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        27 (to L1)
               NOT_TAKEN

159            LOAD_FAST_BORROW         1 (summary)
               LOAD_CONST               5 ('warnings')
               BINARY_OP               26 ([])
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_CONST               6 ('unexpected_events_shape')
               CALL                     1
               POP_TOP

160            LOAD_FAST_BORROW         1 (summary)
               RETURN_VALUE

164    L1:     BUILD_MAP                0
               STORE_FAST               2 (buckets)

166            LOAD_SMALL_INT           0
               STORE_FAST               3 (unknown_statuses_seen)

168            LOAD_FAST_BORROW         0 (events)
               GET_ITER
       L2:     EXTENDED_ARG             1
               FOR_ITER               406 (to L15)
               STORE_FAST               4 (raw)

169            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         4 (raw)
               LOAD_GLOBAL              6 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        12 (to L3)
               NOT_TAKEN

170            LOAD_FAST_BORROW         3 (unknown_statuses_seen)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               3 (unknown_statuses_seen)

171            JUMP_BACKWARD           37 (to L2)

172    L3:     LOAD_GLOBAL              9 (_safe_str + NULL)
               LOAD_FAST_BORROW         4 (raw)
               LOAD_ATTR               11 (get + NULL|self)
               LOAD_CONST               7 ('to_status')
               CALL                     1
               CALL                     1
               STORE_FAST               5 (to_status)

173            LOAD_FAST_BORROW         5 (to_status)
               LOAD_GLOBAL             12 (ALLOWED_TO_STATUSES)
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_FALSE       12 (to L4)
               NOT_TAKEN

174            LOAD_FAST_BORROW         3 (unknown_statuses_seen)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               3 (unknown_statuses_seen)

175            JUMP_BACKWARD           85 (to L2)

177    L4:     LOAD_GLOBAL              9 (_safe_str + NULL)
               LOAD_FAST_BORROW         4 (raw)
               LOAD_ATTR               11 (get + NULL|self)
               LOAD_CONST               8 ('actor_id')
               CALL                     1
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               9 ('unknown')
       L5:     STORE_FAST               6 (actor_id)

178            LOAD_GLOBAL              9 (_safe_str + NULL)
               LOAD_FAST_BORROW         4 (raw)
               LOAD_ATTR               11 (get + NULL|self)
               LOAD_CONST              10 ('actor_type')
               CALL                     1
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L6)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              11 ('UNKNOWN')
       L6:     STORE_FAST               7 (actor_type)

179            LOAD_GLOBAL              9 (_safe_str + NULL)
               LOAD_FAST_BORROW         4 (raw)
               LOAD_ATTR               11 (get + NULL|self)
               LOAD_CONST              12 ('created_at')
               CALL                     1
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L7)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              13 ('')
       L7:     STORE_FAST               8 (created_at)

181            LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (actor_id, actor_type)
               BUILD_TUPLE              2
               STORE_FAST               9 (key)

182            LOAD_FAST_BORROW         2 (buckets)
               LOAD_ATTR               11 (get + NULL|self)
               LOAD_FAST_BORROW         9 (key)
               CALL                     1
               STORE_FAST              10 (bucket)

183            LOAD_FAST_BORROW        10 (bucket)
               POP_JUMP_IF_NOT_NONE    23 (to L8)
               NOT_TAKEN

185            LOAD_CONST               8 ('actor_id')
               LOAD_FAST_BORROW         6 (actor_id)

186            LOAD_CONST              10 ('actor_type')
               LOAD_FAST_BORROW         7 (actor_type)

187            LOAD_CONST              14 ('total_decisions')
               LOAD_SMALL_INT           0

188            LOAD_CONST              15 ('approved')
               LOAD_SMALL_INT           0

189            LOAD_CONST              16 ('rejected')
               LOAD_SMALL_INT           0

190            LOAD_CONST              17 ('expired')
               LOAD_SMALL_INT           0

191            LOAD_CONST              18 ('quarantined')
               LOAD_SMALL_INT           0

192            LOAD_CONST              19 ('last_seen')
               LOAD_CONST              13 ('')

184            BUILD_MAP                8
               STORE_FAST              10 (bucket)

194            LOAD_FAST_BORROW_LOAD_FAST_BORROW 162 (bucket, buckets)
               LOAD_FAST_BORROW         9 (key)
               STORE_SUBSCR

196    L8:     LOAD_FAST_BORROW         5 (to_status)
               LOAD_CONST              20 ('APPROVED')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       23 (to L9)
               NOT_TAKEN

197            LOAD_FAST_BORROW        10 (bucket)
               LOAD_CONST              15 ('approved')
               COPY                     2
               COPY                     2
               BINARY_OP               26 ([])
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               SWAP                     3
               SWAP                     2
               STORE_SUBSCR
               JUMP_FORWARD            86 (to L12)

198    L9:     LOAD_FAST_BORROW         5 (to_status)
               LOAD_CONST              21 ('REJECTED')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       23 (to L10)
               NOT_TAKEN

199            LOAD_FAST_BORROW        10 (bucket)
               LOAD_CONST              16 ('rejected')
               COPY                     2
               COPY                     2
               BINARY_OP               26 ([])
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               SWAP                     3
               SWAP                     2
               STORE_SUBSCR
               JUMP_FORWARD            57 (to L12)

200   L10:     LOAD_FAST_BORROW         5 (to_status)
               LOAD_CONST              22 ('EXPIRED')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       23 (to L11)
               NOT_TAKEN

201            LOAD_FAST_BORROW        10 (bucket)
               LOAD_CONST              17 ('expired')
               COPY                     2
               COPY                     2
               BINARY_OP               26 ([])
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               SWAP                     3
               SWAP                     2
               STORE_SUBSCR
               JUMP_FORWARD            28 (to L12)

202   L11:     LOAD_FAST_BORROW         5 (to_status)
               LOAD_CONST              23 ('QUARANTINED')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       22 (to L12)
               NOT_TAKEN

203            LOAD_FAST_BORROW        10 (bucket)
               LOAD_CONST              18 ('quarantined')
               COPY                     2
               COPY                     2
               BINARY_OP               26 ([])
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               SWAP                     3
               SWAP                     2
               STORE_SUBSCR

204   L12:     LOAD_FAST_BORROW        10 (bucket)
               LOAD_CONST              14 ('total_decisions')
               COPY                     2
               COPY                     2
               BINARY_OP               26 ([])
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               SWAP                     3
               SWAP                     2
               STORE_SUBSCR

213            LOAD_FAST_BORROW         8 (created_at)
               TO_BOOL
               POP_JUMP_IF_TRUE         4 (to L13)
               NOT_TAKEN
               EXTENDED_ARG             1
               JUMP_BACKWARD          386 (to L2)
      L13:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 138 (created_at, bucket)
               LOAD_CONST              19 ('last_seen')
               BINARY_OP               26 ([])
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_TRUE         4 (to L14)
               NOT_TAKEN
               EXTENDED_ARG             1
               JUMP_BACKWARD          402 (to L2)

214   L14:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 138 (created_at, bucket)
               LOAD_CONST              19 ('last_seen')
               STORE_SUBSCR
               EXTENDED_ARG             1
               JUMP_BACKWARD          409 (to L2)

168   L15:     END_FOR
               POP_ITER

216            LOAD_FAST_BORROW         3 (unknown_statuses_seen)
               TO_BOOL
               POP_JUMP_IF_FALSE       28 (to L16)
               NOT_TAKEN

217            LOAD_FAST_BORROW         1 (summary)
               LOAD_CONST               5 ('warnings')
               BINARY_OP               26 ([])
               LOAD_ATTR                5 (append + NULL|self)

218            LOAD_CONST              24 ('unknown_status_events_ignored:')
               LOAD_FAST_BORROW         3 (unknown_statuses_seen)
               FORMAT_SIMPLE
               BUILD_STRING             2

217            CALL                     1
               POP_TOP

221   L16:     LOAD_GLOBAL              3 (list + NULL)
               LOAD_FAST_BORROW         2 (buckets)
               LOAD_ATTR               15 (values + NULL|self)
               CALL                     0
               CALL                     1
               STORE_FAST              11 (actor_rows)

223            LOAD_FAST_BORROW        11 (actor_rows)
               LOAD_ATTR               17 (sort + NULL|self)
               LOAD_CONST              25 (<code object <lambda> at 0x0000018C18025E30, file "app\services\memory\review_actors.py", line 223>)
               MAKE_FUNCTION
               LOAD_CONST              26 (('key',))
               CALL_KW                  1
               POP_TOP

224            LOAD_FAST_BORROW_LOAD_FAST_BORROW 177 (actor_rows, summary)
               LOAD_CONST               4 ('actors')
               STORE_SUBSCR

225            LOAD_GLOBAL             19 (len + NULL)
               LOAD_FAST_BORROW        11 (actor_rows)
               CALL                     1
               LOAD_FAST_BORROW         1 (summary)
               LOAD_CONST               3 ('actor_count')
               STORE_SUBSCR

226            LOAD_FAST_BORROW         1 (summary)
               RETURN_VALUE

Disassembly of <code object <lambda> at 0x0000018C18025E30, file "app\services\memory\review_actors.py", line 223>:
223           RESUME                   0
              LOAD_FAST_BORROW         0 (r)
              LOAD_CONST               0 ('total_decisions')
              BINARY_OP               26 ([])
              UNARY_NEGATIVE
              LOAD_FAST_BORROW         0 (r)
              LOAD_CONST               1 ('actor_id')
              BINARY_OP               26 ([])
              BUILD_TUPLE              2
              RETURN_VALUE

Disassembly of <code object _get_db at 0x0000018C17FA3780, file "app\services\memory\review_actors.py", line 233>:
233           RESUME                   0

235           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('get_supabase',))
              IMPORT_NAME              0 (app.db.supabase_client)
              IMPORT_FROM              1 (get_supabase)
              STORE_FAST               0 (get_supabase)
              POP_TOP

236           LOAD_FAST_BORROW         0 (get_supabase)
              PUSH_NULL
              CALL                     0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025C30, file "app\services\memory\review_actors.py", line 239>:
239           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

240           LOAD_CONST               2 ('str')

239           LOAD_CONST               3 ('since')

242           LOAD_CONST               4 ('Optional[str]')

239           LOAD_CONST               5 ('limit')

243           LOAD_CONST               6 ('int')

239           LOAD_CONST               7 ('return')

244           LOAD_CONST               8 ('Tuple[List[Dict[str, Any]], List[str]]')

239           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object _list_review_events_for_brokerage at 0x0000018C17D79E90, file "app\services\memory\review_actors.py", line 239>:
 239            RESUME                   0

 257            BUILD_LIST               0
                STORE_FAST               3 (warnings)

 258            NOP

 259    L1:     LOAD_GLOBAL              1 (_get_db + NULL)
                CALL                     0
                STORE_FAST               4 (db)

 261            LOAD_FAST_BORROW         4 (db)
                LOAD_ATTR                3 (table + NULL|self)
                LOAD_GLOBAL              4 (_TABLE_REVIEW)
                CALL                     1

 262            LOAD_ATTR                7 (select + NULL|self)
                LOAD_CONST               1 ('actor_id, actor_type, to_status, created_at')
                CALL                     1

 263            LOAD_ATTR                9 (eq + NULL|self)
                LOAD_CONST               2 ('brokerage_id')
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     2

 264            LOAD_ATTR               11 (order + NULL|self)
                LOAD_CONST               3 ('created_at')
                LOAD_CONST               4 (True)
                LOAD_CONST               5 (('desc',))
                CALL_KW                  2

 265            LOAD_ATTR               13 (limit + NULL|self)
                LOAD_FAST_BORROW         2 (limit)
                CALL                     1

 260            STORE_FAST               5 (query)

 267            LOAD_FAST_BORROW         1 (since)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L2)
                NOT_TAKEN

 268            LOAD_FAST_BORROW         5 (query)
                LOAD_ATTR               15 (gte + NULL|self)
                LOAD_CONST               3 ('created_at')
                LOAD_FAST_BORROW         1 (since)
                CALL                     2
                STORE_FAST               5 (query)

 269    L2:     LOAD_FAST_BORROW         5 (query)
                LOAD_ATTR               17 (execute + NULL|self)
                CALL                     0
                STORE_FAST               6 (result)

 270            LOAD_GLOBAL             19 (list + NULL)
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

 278    L6:     LOAD_GLOBAL             33 (isinstance + NULL)
                LOAD_FAST                7 (rows)
                LOAD_GLOBAL             18 (list)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         6 (to L7)
                NOT_TAKEN

 279            BUILD_LIST               0
                LOAD_CONST              11 ('unexpected_reader_shape')
                BUILD_LIST               1
                BUILD_TUPLE              2
                RETURN_VALUE

 280    L7:     LOAD_GLOBAL             35 (len + NULL)
                LOAD_FAST                7 (rows)
                CALL                     1
                LOAD_FAST                2 (limit)
                COMPARE_OP             188 (bool(>=))
                POP_JUMP_IF_FALSE       18 (to L8)
                NOT_TAKEN

 281            LOAD_FAST                3 (warnings)
                LOAD_ATTR               37 (append + NULL|self)
                LOAD_CONST              12 ('result_truncated_at_limit')
                CALL                     1
                POP_TOP

 282    L8:     LOAD_FAST_LOAD_FAST    115 (rows, warnings)
                BUILD_TUPLE              2
                RETURN_VALUE

  --    L9:     PUSH_EXC_INFO

 271            LOAD_GLOBAL             22 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       84 (to L14)
                NOT_TAKEN
                STORE_FAST               8 (e)

 272   L10:     LOAD_GLOBAL             24 (logger)
                LOAD_ATTR               27 (warning + NULL|self)

 273            LOAD_CONST               8 ('review_actors reader failed (non-critical) | brokerage=')

 274            LOAD_FAST                0 (brokerage_id)
                FORMAT_SIMPLE
                LOAD_CONST               9 (' | error_type=')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE

 273            BUILD_STRING             4

 272            CALL                     1
                POP_TOP

 276            BUILD_LIST               0
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

 271   L14:     RERAISE                  0

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

Disassembly of <code object __annotate__ at 0x0000018C18024930, file "app\services\memory\review_actors.py", line 289>:
289           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

290           LOAD_CONST               2 ('Any')

289           LOAD_CONST               3 ('since')

291           LOAD_CONST               2 ('Any')

289           LOAD_CONST               4 ('limit')

292           LOAD_CONST               2 ('Any')

289           LOAD_CONST               5 ('return')

293           LOAD_CONST               6 ('Dict[str, Any]')

289           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object review_actors_for_brokerage at 0x0000018C17E93D70, file "app\services\memory\review_actors.py", line 289>:
289           RESUME                   0

311           LOAD_GLOBAL              1 (isinstance + NULL)
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

313   L1:     LOAD_CONST               1 ('status')
              LOAD_CONST               2 ('failed')

314           LOAD_CONST               3 ('errors')
              LOAD_CONST               4 ('missing_brokerage_id')
              BUILD_LIST               1

315           LOAD_CONST               5 ('actors')
              BUILD_LIST               0

316           LOAD_CONST               6 ('actor_count')
              LOAD_SMALL_INT           0

317           LOAD_CONST               7 ('warnings')
              LOAD_CONST               4 ('missing_brokerage_id')
              BUILD_LIST               1

312           BUILD_MAP                5
              RETURN_VALUE

319   L2:     LOAD_FAST_BORROW         0 (brokerage_id)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               0 (brokerage_id)

321           LOAD_GLOBAL              7 (_coerce_since + NULL)
              LOAD_FAST_BORROW         1 (since)
              CALL                     1
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST   52 (cleaned_since, since_warning)

322           LOAD_GLOBAL              9 (_clamp_limit + NULL)
              LOAD_FAST_BORROW         2 (limit)
              CALL                     1
              STORE_FAST               5 (capped)

324           LOAD_GLOBAL             11 (_list_review_events_for_brokerage + NULL)

325           LOAD_FAST_BORROW_LOAD_FAST_BORROW 3 (brokerage_id, cleaned_since)
              LOAD_FAST_BORROW         5 (capped)

324           LOAD_CONST               8 (('since', 'limit'))
              CALL_KW                  3
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST  103 (rows, reader_warnings)

328           LOAD_GLOBAL             13 (summarize_review_actors + NULL)
              LOAD_FAST_BORROW         6 (rows)
              CALL                     1
              STORE_FAST               8 (summary)

331           LOAD_CONST               1 ('status')
              LOAD_CONST               9 ('ok')

332           LOAD_CONST              10 ('brokerage_id')
              LOAD_FAST_BORROW         0 (brokerage_id)

333           LOAD_CONST              11 ('since')
              LOAD_FAST_BORROW         3 (cleaned_since)

334           LOAD_CONST              12 ('limit')
              LOAD_FAST_BORROW         5 (capped)

335           LOAD_CONST               6 ('actor_count')
              LOAD_FAST_BORROW         8 (summary)
              LOAD_CONST               6 ('actor_count')
              BINARY_OP               26 ([])

336           LOAD_CONST               5 ('actors')
              LOAD_FAST_BORROW         8 (summary)
              LOAD_CONST               5 ('actors')
              BINARY_OP               26 ([])

337           LOAD_CONST               7 ('warnings')
              LOAD_GLOBAL             15 (list + NULL)
              LOAD_FAST_BORROW         8 (summary)
              LOAD_CONST               7 ('warnings')
              BINARY_OP               26 ([])
              CALL                     1

330           BUILD_MAP                7
              STORE_FAST               9 (out)

339           LOAD_FAST_BORROW         4 (since_warning)
              TO_BOOL
              POP_JUMP_IF_FALSE       25 (to L3)
              NOT_TAKEN

340           LOAD_FAST_BORROW         9 (out)
              LOAD_CONST               7 ('warnings')
              BINARY_OP               26 ([])
              LOAD_ATTR               17 (append + NULL|self)
              LOAD_FAST_BORROW         4 (since_warning)
              CALL                     1
              POP_TOP

341   L3:     LOAD_FAST_BORROW         9 (out)
              LOAD_CONST               7 ('warnings')
              BINARY_OP               26 ([])
              LOAD_ATTR               19 (extend + NULL|self)
              LOAD_FAST_BORROW         7 (reader_warnings)
              CALL                     1
              POP_TOP

342           LOAD_FAST_BORROW         9 (out)
              RETURN_VALUE
```
