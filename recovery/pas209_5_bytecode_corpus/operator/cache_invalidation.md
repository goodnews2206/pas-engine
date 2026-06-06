# operator/cache_invalidation

- **pyc:** `app\services\operator\__pycache__\cache_invalidation.cpython-314.pyc`
- **expected source path (absent):** `app\services\operator/cache_invalidation.py`
- **co_filename (from bytecode):** `app\services\operator\cache_invalidation.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** operator

## Module docstring

```
PAS189 — Operator-only fleet-status cache invalidation
hooks.

Thin wrappers around PAS188's
``fleet_status_cache.invalidate``. The point of this
module is to give upstream routes a single, well-named
entry point to call when an operator-driven mutation
should expire the cached fleet-status entries that
mention the brokerage.

Doctrine:

* **Operator-only.** Routes that call these hooks are
  admin-authenticated (PAS-SECURITY-04). PAS189 does
  NOT install any background invalidation thread, NO
  scheduler, NO autonomous loop.
* **No exceptions escape.** PAS188 cache invalidation
  is itself fail-safe; PAS189 wraps it with one more
  try/except for belt-and-braces.
* **No PII / no production data touch.** The hooks
  read no DB; they only touch in-process cache state
  via PAS188.
* **Bounded.** Currently the only invalidation
  granularity is "whole surface" (PAS188 keys by
  brokerage-id tuple); per-row invalidation is a
  PAS190 candidate. The hook accepts ``brokerage_id``
  so PAS190 can add per-row invalidation without
  changing call sites.

Public surface:

  * ``invalidate_fleet_status_for_brokerage(brokerage_id, *, reason="")``
  * ``invalidate_fleet_status_all(*, reason="")``
  * ``cache_invalidation_report()``
```

## Imports

`Any`, `Dict`, `Optional`, `__future__`, `annotations`, `app.db.event_logger`, `app.services.operator.fleet_status_cache`, `invalidate`, `invalidate_for_brokerage`, `log_event_bg`, `logging`, `threading`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_do_invalidate`, `_emit_event`, `_safe_brokerage`, `_safe_reason`, `cache_invalidation_report`, `invalidate_fleet_status_all`, `invalidate_fleet_status_for_breaker`, `invalidate_fleet_status_for_brokerage`, `invalidate_fleet_status_for_cutover`, `invalidate_fleet_status_for_incident`, `invalidate_fleet_status_row`, `invalidate_fleet_status_rows`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS189 — Operator-only fleet-status cache invalidation\nhooks.\n\nThin wrappers around PAS188\'s\n``fleet_status_cache.invalidate``. The point of this\nmodule is to give upstream routes a single, well-named\nentry point to call when an operator-driven mutation\nshould expire the cached fleet-status entries that\nmention the brokerage.\n\nDoctrine:\n\n* **Operator-only.** Routes that call these hooks are\n  admin-authenticated (PAS-SECURITY-04). PAS189 does\n  NOT install any background invalidation thread, NO\n  scheduler, NO autonomous loop.\n* **No exceptions escape.** PAS188 cache invalidation\n  is itself fail-safe; PAS189 wraps it with one more\n  try/except for belt-and-braces.\n* **No PII / no production data touch.** The hooks\n  read no DB; they only touch in-process cache state\n  via PAS188.\n* **Bounded.** Currently the only invalidation\n  granularity is "whole surface" (PAS188 keys by\n  brokerage-id tuple); per-row invalidation is a\n  PAS190 candidate. The hook accepts ``brokerage_id``\n  so PAS190 can add per-row invalidation without\n  changing call sites.\n\nPublic surface:\n\n  * ``invalidate_fleet_status_for_brokerage(brokerage_id, *, reason="")``\n  * ``invalidate_fleet_status_all(*, reason="")``\n  * ``cache_invalidation_report()``\n'
- 'pas.operator.cache_invalidation'
- 'per_brokerage'
- 'all'
- 'errors'
- 'Dict[str, int]'
- '_STATS'
- 'reason'
- 'incident_state_change'
- 'cutover_state_change'
- 'breaker_state_change'
- 'value'
- 'Any'
- 'return'
- 'str'
- 'Optional[str]'
- 'event_type'
- 'payload'
- 'Dict[str, Any]'
- 'None'
- 'Fire-and-forget audit event. Never raises.'
- 'scope'
- "Call PAS188's invalidate. Returns the PAS188\nenvelope or a fail-safe envelope on import / call\nfailure."
- 'cache_invalidation import-failure type='
- 'status'
- 'skipped'
- 'cleared'
- 'error_code'
- 'cache_module_unavailable'
- 'invalidate_returned_non_dict'
- 'cache_invalidation invalidate-error type='
- 'unexpected:'
- 'brokerage_id'
- 'Invalidate cached fleet-status entries that mention\n``brokerage_id``. Today PAS188 cache keying is by tuple\nof brokerage IDs; this hook conservatively clears the\nwhole brokerage_health surface so the next dashboard\nrefresh sees fresh data. Per-row granularity is a\nPAS190 candidate.\n\nNEVER raises. Returns a structural envelope.'
- 'failed'
- 'surface'
- 'ops.cache.invalidate.per_brokerage'
- 'invalid_brokerage_id'
- 'warnings'
- 'fleet.brokerage_health'
- 'fleet.cache.invalidated'
- 'warning_count'
- 'action_required'
- 'none'
- 'invalidate_fleet_status_for_brokerage error type='
- 'Clear every PAS188 cache entry. Operator-callable;\nuse when a system-wide event (rollout-stage change,\nfleet-wide migration) should expire all entries.'
- 'ops.cache.invalidate.all'
- 'invalidate_fleet_status_all error type='
- 'PAS190 — per-row cache invalidation. Scans the cache\nand drops any entry whose key mentions ``brokerage_id``,\nleaving entries that do not mention it untouched. Falls\nback to the PAS189 whole-surface invalidation only if\nthe row-level helper is unavailable.'
- 'ops.cache.invalidate.row'
- 'invalidate_fleet_status_row underlying error type='
- 'fleet.cache.row_invalidated'
- 'brokerage:'
- 'invalidate_fleet_status_row error type='
- 'brokerage_ids'
- 'PAS190 — multi-row invalidation. Bounded; iterates over\nthe supplied IDs and calls ``invalidate_fleet_status_row``\nfor each. Returns a roll-up envelope.'
- 'ops.cache.invalidate.rows'
- 'no_brokerage_ids'
- 'brokerage_ids_not_iterable'
- 'no_valid_brokerage_ids'
- 'count'
- 'rows'
- 'invalidate_fleet_status_rows error type='
- 'PAS190 — semantic wrapper. If a brokerage_id is given,\ninvalidate that row; otherwise fall back to the whole\nfleet (an incident with no brokerage is fleet-wide).'
- 'PAS190 — semantic wrapper. Cutover state changes are\nalways brokerage-scoped.'
- 'PAS190 — semantic wrapper. Breaker trip / reset is\nalways brokerage-scoped.'
- 'Snapshot of wrapper-level invalidation stats. Read-\nonly; does NOT mutate counters.'
- 'ops.cache.invalidation.report'

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS189 — Operator-only fleet-status cache invalidation\nhooks.\n\nThin wrappers around PAS188\'s\n``fleet_status_cache.invalidate``. The point of this\nmodule is to give upstream routes a single, well-named\nentry point to call when an operator-driven mutation\nshould expire the cached fleet-status entries that\nmention the brokerage.\n\nDoctrine:\n\n* **Operator-only.** Routes that call these hooks are\n  admin-authenticated (PAS-SECURITY-04). PAS189 does\n  NOT install any background invalidation thread, NO\n  scheduler, NO autonomous loop.\n* **No exceptions escape.** PAS188 cache invalidation\n  is itself fail-safe; PAS189 wraps it with one more\n  try/except for belt-and-braces.\n* **No PII / no production data touch.** The hooks\n  read no DB; they only touch in-process cache state\n  via PAS188.\n* **Bounded.** Currently the only invalidation\n  granularity is "whole surface" (PAS188 keys by\n  brokerage-id tuple); per-row invalidation is a\n  PAS190 candidate. The hook accepts ``brokerage_id``\n  so PAS190 can add per-row invalidation without\n  changing call sites.\n\nPublic surface:\n\n  * ``invalidate_fleet_status_for_brokerage(brokerage_id, *, reason="")``\n  * ``invalidate_fleet_status_all(*, reason="")``\n  * ``cache_invalidation_report()``\n')
               STORE_NAME               1 (__doc__)

  38           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  40           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (logging)
               STORE_NAME               4 (logging)

  41           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (threading)
               STORE_NAME               5 (threading)

  42           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('Any', 'Dict', 'Optional'))
               IMPORT_NAME              6 (typing)
               IMPORT_FROM              7 (Any)
               STORE_NAME               7 (Any)
               IMPORT_FROM              8 (Dict)
               STORE_NAME               8 (Dict)
               IMPORT_FROM              9 (Optional)
               STORE_NAME               9 (Optional)
               POP_TOP

  45           LOAD_NAME                4 (logging)
               LOAD_ATTR               20 (getLogger)
               PUSH_NULL
               LOAD_CONST               4 ('pas.operator.cache_invalidation')
               CALL                     1
               STORE_NAME              11 (logger)

  52           LOAD_NAME                5 (threading)
               LOAD_ATTR               24 (RLock)
               PUSH_NULL
               CALL                     0
               STORE_NAME              13 (_LOCK)

  54           LOAD_CONST               5 ('per_brokerage')
               LOAD_SMALL_INT           0

  55           LOAD_CONST               6 ('all')
               LOAD_SMALL_INT           0

  56           LOAD_CONST               7 ('errors')
               LOAD_SMALL_INT           0

  53           BUILD_MAP                3
               STORE_NAME              14 (_STATS)
               LOAD_CONST               8 ('Dict[str, int]')
               LOAD_NAME               15 (__annotations__)
               LOAD_CONST               9 ('_STATS')
               STORE_SUBSCR

  64           LOAD_SMALL_INT          64
               STORE_NAME              16 (_REASON_MAX_LEN)

  67           LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA3960, file "app\services\operator\cache_invalidation.py", line 67>)
               MAKE_FUNCTION
               LOAD_CONST              11 (<code object _safe_reason at 0x0000018C17FF1530, file "app\services\operator\cache_invalidation.py", line 67>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              17 (_safe_reason)

  78           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA1D40, file "app\services\operator\cache_invalidation.py", line 78>)
               MAKE_FUNCTION
               LOAD_CONST              13 (<code object _safe_brokerage at 0x0000018C17972D90, file "app\services\operator\cache_invalidation.py", line 78>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              18 (_safe_brokerage)

  87           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C18025130, file "app\services\operator\cache_invalidation.py", line 87>)
               MAKE_FUNCTION
               LOAD_CONST              15 (<code object _emit_event at 0x0000018C18038DF0, file "app\services\operator\cache_invalidation.py", line 87>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              19 (_emit_event)

  99           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C17FA3870, file "app\services\operator\cache_invalidation.py", line 99>)
               MAKE_FUNCTION
               LOAD_CONST              17 (<code object _do_invalidate at 0x0000018C17CD4970, file "app\services\operator\cache_invalidation.py", line 99>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              20 (_do_invalidate)

 135           LOAD_CONST              18 ('reason')

 138           LOAD_CONST              19 ('')

 135           BUILD_MAP                1
               LOAD_CONST              20 (<code object __annotate__ at 0x0000018C18025A30, file "app\services\operator\cache_invalidation.py", line 135>)
               MAKE_FUNCTION
               LOAD_CONST              21 (<code object invalidate_fleet_status_for_brokerage at 0x0000018C17D801D0, file "app\services\operator\cache_invalidation.py", line 135>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              21 (invalidate_fleet_status_for_brokerage)

 197           LOAD_CONST              18 ('reason')
               LOAD_CONST              19 ('')
               BUILD_MAP                1
               LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA2A60, file "app\services\operator\cache_invalidation.py", line 197>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object invalidate_fleet_status_all at 0x0000018C17EDA3D0, file "app\services\operator\cache_invalidation.py", line 197>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              22 (invalidate_fleet_status_all)

 238           LOAD_CONST              18 ('reason')

 241           LOAD_CONST              19 ('')

 238           BUILD_MAP                1
               LOAD_CONST              24 (<code object __annotate__ at 0x0000018C18025230, file "app\services\operator\cache_invalidation.py", line 238>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object invalidate_fleet_status_row at 0x0000018C17E8A580, file "app\services\operator\cache_invalidation.py", line 238>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              23 (invalidate_fleet_status_row)

 318           LOAD_CONST              18 ('reason')

 321           LOAD_CONST              19 ('')

 318           BUILD_MAP                1
               LOAD_CONST              26 (<code object __annotate__ at 0x0000018C18025930, file "app\services\operator\cache_invalidation.py", line 318>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object invalidate_fleet_status_rows at 0x0000018C17D7CD30, file "app\services\operator\cache_invalidation.py", line 318>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              24 (invalidate_fleet_status_rows)

 391           LOAD_CONST              39 ((None,))
               LOAD_CONST              18 ('reason')

 394           LOAD_CONST              28 ('incident_state_change')

 391           BUILD_MAP                1
               LOAD_CONST              29 (<code object __annotate__ at 0x0000018C18025330, file "app\services\operator\cache_invalidation.py", line 391>)
               MAKE_FUNCTION
               LOAD_CONST              30 (<code object invalidate_fleet_status_for_incident at 0x0000018C18010B30, file "app\services\operator\cache_invalidation.py", line 391>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              25 (invalidate_fleet_status_for_incident)

 405           LOAD_CONST              18 ('reason')

 408           LOAD_CONST              31 ('cutover_state_change')

 405           BUILD_MAP                1
               LOAD_CONST              32 (<code object __annotate__ at 0x0000018C18025B30, file "app\services\operator\cache_invalidation.py", line 405>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object invalidate_fleet_status_for_cutover at 0x0000018C18025630, file "app\services\operator\cache_invalidation.py", line 405>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              26 (invalidate_fleet_status_for_cutover)

 415           LOAD_CONST              18 ('reason')

 418           LOAD_CONST              34 ('breaker_state_change')

 415           BUILD_MAP                1
               LOAD_CONST              35 (<code object __annotate__ at 0x0000018C18024F30, file "app\services\operator\cache_invalidation.py", line 415>)
               MAKE_FUNCTION
               LOAD_CONST              36 (<code object invalidate_fleet_status_for_breaker at 0x0000018C18025030, file "app\services\operator\cache_invalidation.py", line 415>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              27 (invalidate_fleet_status_for_breaker)

 425           LOAD_CONST              37 (<code object __annotate__ at 0x0000018C17FA3780, file "app\services\operator\cache_invalidation.py", line 425>)
               MAKE_FUNCTION
               LOAD_CONST              38 (<code object cache_invalidation_report at 0x0000018C1794E9E0, file "app\services\operator\cache_invalidation.py", line 425>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              28 (cache_invalidation_report)
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "app\services\operator\cache_invalidation.py", line 67>:
 67           RESUME                   0
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
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _safe_reason at 0x0000018C17FF1530, file "app\services\operator\cache_invalidation.py", line 67>:
 67           RESUME                   0

 68           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

 69           LOAD_CONST               0 ('')
              RETURN_VALUE

 70   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

 71           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

 72           LOAD_CONST               0 ('')
              RETURN_VALUE

 73   L2:     LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         1 (s)
              CALL                     1
              LOAD_GLOBAL              8 (_REASON_MAX_LEN)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       10 (to L3)
              NOT_TAKEN

 74           LOAD_FAST_BORROW         1 (s)
              LOAD_CONST               1 (None)
              LOAD_GLOBAL              8 (_REASON_MAX_LEN)
              BINARY_SLICE
              STORE_FAST               1 (s)

 75   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1D40, file "app\services\operator\cache_invalidation.py", line 78>:
 78           RESUME                   0
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

Disassembly of <code object _safe_brokerage at 0x0000018C17972D90, file "app\services\operator\cache_invalidation.py", line 78>:
 78           RESUME                   0

 79           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

 80           LOAD_CONST               0 (None)
              RETURN_VALUE

 81   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

 82           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_FALSE       17 (to L2)
              NOT_TAKEN
              LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         1 (s)
              CALL                     1
              LOAD_SMALL_INT         200
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

 83   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

 84   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025130, file "app\services\operator\cache_invalidation.py", line 87>:
 87           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('event_type')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('payload')
              LOAD_CONST               4 ('Dict[str, Any]')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('None')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _emit_event at 0x0000018C18038DF0, file "app\services\operator\cache_invalidation.py", line 87>:
  87            RESUME                   0

  89            NOP

  90    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               1 (('log_event_bg',))
                IMPORT_NAME              0 (app.db.event_logger)
                IMPORT_FROM              1 (log_event_bg)
                STORE_FAST               2 (log_event_bg)
                POP_TOP

  93    L2:     NOP

  94    L3:     LOAD_FAST                2 (log_event_bg)
                PUSH_NULL
                LOAD_FAST_LOAD_FAST      1 (event_type, payload)
                CALL                     2
                POP_TOP
        L4:     LOAD_CONST               2 (None)
                RETURN_VALUE

  --    L5:     PUSH_EXC_INFO

  91            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L7)
                NOT_TAKEN
                POP_TOP

  92    L6:     POP_EXCEPT
                LOAD_CONST               2 (None)
                RETURN_VALUE

  91    L7:     RERAISE                  0

  --    L8:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
        L9:     PUSH_EXC_INFO

  95            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L11)
                NOT_TAKEN
                POP_TOP

  96   L10:     POP_EXCEPT
                LOAD_CONST               2 (None)
                RETURN_VALUE

  95   L11:     RERAISE                  0

  --   L12:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L3 to L4 -> L9 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti
  L9 to L10 -> L12 [1] lasti
  L11 to L12 -> L12 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "app\services\operator\cache_invalidation.py", line 99>:
 99           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('scope')
              LOAD_CONST               2 ('Optional[str]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _do_invalidate at 0x0000018C17CD4970, file "app\services\operator\cache_invalidation.py", line 99>:
  99            RESUME                   0

 103            NOP

 104    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               1 (('invalidate',))
                IMPORT_NAME              0 (app.services.operator.fleet_status_cache)
                IMPORT_FROM              1 (invalidate)
                STORE_FAST               1 (invalidate)
                POP_TOP

 113    L2:     NOP

 114    L3:     LOAD_FAST                0 (scope)
                TO_BOOL
                POP_JUMP_IF_FALSE       11 (to L6)
        L4:     NOT_TAKEN

 115    L5:     LOAD_FAST                1 (invalidate)
                PUSH_NULL
                LOAD_FAST                0 (scope)
                LOAD_CONST              11 (('surface',))
                CALL_KW                  1
                STORE_FAST               3 (res)
                JUMP_FORWARD             7 (to L7)

 117    L6:     LOAD_FAST                1 (invalidate)
                PUSH_NULL
                CALL                     0
                STORE_FAST               3 (res)

 118    L7:     LOAD_GLOBAL             15 (isinstance + NULL)
                LOAD_FAST                3 (res)
                LOAD_GLOBAL             16 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        21 (to L12)
                NOT_TAKEN

 119            LOAD_CONST               3 ('status')
                LOAD_CONST               4 ('skipped')
                LOAD_CONST               5 ('cleared')
                LOAD_SMALL_INT           0

 120            LOAD_CONST               6 ('scope')
                LOAD_FAST                0 (scope)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
        L8:     NOT_TAKEN
        L9:     POP_TOP
                LOAD_CONST               7 ('all')

 121   L10:     LOAD_CONST               8 ('error_code')
                LOAD_CONST              12 ('invalidate_returned_non_dict')

 119            BUILD_MAP                4
       L11:     RETURN_VALUE

 122   L12:     LOAD_FAST                3 (res)
       L13:     RETURN_VALUE

  --   L14:     PUSH_EXC_INFO

 107            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       74 (to L20)
                NOT_TAKEN
                STORE_FAST               2 (e)

 108   L15:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 109            LOAD_CONST               2 ('cache_invalidation import-failure type=')
                LOAD_GLOBAL             11 (type + NULL)
                LOAD_FAST                2 (e)
                CALL                     1
                LOAD_ATTR               12 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 108            CALL                     1
                POP_TOP

 111            LOAD_CONST               3 ('status')
                LOAD_CONST               4 ('skipped')
                LOAD_CONST               5 ('cleared')
                LOAD_SMALL_INT           0
                LOAD_CONST               6 ('scope')
                LOAD_FAST                0 (scope)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L16)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               7 ('all')

 112   L16:     LOAD_CONST               8 ('error_code')
                LOAD_CONST               9 ('cache_module_unavailable')

 111            BUILD_MAP                4
       L17:     SWAP                     2
       L18:     POP_EXCEPT
                LOAD_CONST              10 (None)
                STORE_FAST               2 (e)
                DELETE_FAST              2 (e)
                RETURN_VALUE

  --   L19:     LOAD_CONST              10 (None)
                STORE_FAST               2 (e)
                DELETE_FAST              2 (e)
                RERAISE                  1

 107   L20:     RERAISE                  0

  --   L21:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L22:     PUSH_EXC_INFO

 123            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       96 (to L28)
                NOT_TAKEN
                STORE_FAST               2 (e)

 124   L23:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 125            LOAD_CONST              13 ('cache_invalidation invalidate-error type=')
                LOAD_GLOBAL             11 (type + NULL)
                LOAD_FAST                2 (e)
                CALL                     1
                LOAD_ATTR               12 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 124            CALL                     1
                POP_TOP

 127            LOAD_CONST               3 ('status')
                LOAD_CONST               4 ('skipped')
                LOAD_CONST               5 ('cleared')
                LOAD_SMALL_INT           0
                LOAD_CONST               6 ('scope')
                LOAD_FAST                0 (scope)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L24)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               7 ('all')

 128   L24:     LOAD_CONST               8 ('error_code')
                LOAD_CONST              14 ('unexpected:')
                LOAD_GLOBAL             11 (type + NULL)
                LOAD_FAST                2 (e)
                CALL                     1
                LOAD_ATTR               12 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 127            BUILD_MAP                4
       L25:     SWAP                     2
       L26:     POP_EXCEPT
                LOAD_CONST              10 (None)
                STORE_FAST               2 (e)
                DELETE_FAST              2 (e)
                RETURN_VALUE

  --   L27:     LOAD_CONST              10 (None)
                STORE_FAST               2 (e)
                DELETE_FAST              2 (e)
                RERAISE                  1

 123   L28:     RERAISE                  0

  --   L29:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L14 [0]
  L3 to L4 -> L22 [0]
  L5 to L8 -> L22 [0]
  L9 to L11 -> L22 [0]
  L12 to L13 -> L22 [0]
  L14 to L15 -> L21 [1] lasti
  L15 to L17 -> L19 [1] lasti
  L17 to L18 -> L21 [1] lasti
  L19 to L21 -> L21 [1] lasti
  L22 to L23 -> L29 [1] lasti
  L23 to L25 -> L27 [1] lasti
  L25 to L26 -> L29 [1] lasti
  L27 to L29 -> L29 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025A30, file "app\services\operator\cache_invalidation.py", line 135>:
135           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

136           LOAD_CONST               2 ('Any')

135           LOAD_CONST               3 ('reason')

138           LOAD_CONST               2 ('Any')

135           LOAD_CONST               4 ('return')

139           LOAD_CONST               5 ('Dict[str, Any]')

135           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object invalidate_fleet_status_for_brokerage at 0x0000018C17D801D0, file "app\services\operator\cache_invalidation.py", line 135>:
 135            RESUME                   0

 148            NOP

 149    L1:     LOAD_GLOBAL              1 (_safe_brokerage + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                STORE_FAST               2 (bid)

 150            LOAD_GLOBAL              3 (_safe_reason + NULL)
                LOAD_FAST_BORROW         1 (reason)
                CALL                     1
                STORE_FAST               3 (r)

 151            LOAD_FAST_BORROW         2 (bid)
                TO_BOOL
                POP_JUMP_IF_TRUE        12 (to L3)
                NOT_TAKEN

 153            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 154            LOAD_CONST               3 ('surface')
                LOAD_CONST               4 ('ops.cache.invalidate.per_brokerage')

 155            LOAD_CONST               5 ('error_code')
                LOAD_CONST               6 ('invalid_brokerage_id')

 156            LOAD_CONST               7 ('warnings')
                LOAD_CONST               6 ('invalid_brokerage_id')
                BUILD_LIST               1

 152            BUILD_MAP                4
        L2:     RETURN_VALUE

 160    L3:     LOAD_GLOBAL              5 (_do_invalidate + NULL)
                LOAD_CONST               8 ('fleet.brokerage_health')
                CALL                     1
                STORE_FAST               4 (result)

 161            LOAD_GLOBAL              6 (_LOCK)
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
        L4:     POP_TOP

 162            LOAD_GLOBAL              9 (int + NULL)
                LOAD_GLOBAL             10 (_STATS)
                LOAD_CONST               9 ('per_brokerage')
                BINARY_OP               26 ([])
                CALL                     1
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_GLOBAL             10 (_STATS)
                LOAD_CONST               9 ('per_brokerage')
                STORE_SUBSCR

 163            LOAD_FAST_BORROW         4 (result)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               1 ('status')
                CALL                     1
                LOAD_CONST              10 ('ok')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       37 (to L5)
                NOT_TAKEN

 164            LOAD_GLOBAL              9 (int + NULL)
                LOAD_GLOBAL             10 (_STATS)
                LOAD_CONST              11 ('errors')
                BINARY_OP               26 ([])
                CALL                     1
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_GLOBAL             10 (_STATS)
                LOAD_CONST              11 ('errors')
                STORE_SUBSCR

 161    L5:     LOAD_CONST              12 (None)
                LOAD_CONST              12 (None)
                LOAD_CONST              12 (None)
                CALL                     3
                POP_TOP

 165    L6:     LOAD_GLOBAL             15 (_emit_event + NULL)
                LOAD_CONST              13 ('fleet.cache.invalidated')

 166            LOAD_CONST              14 ('brokerage_id')
                LOAD_FAST                2 (bid)

 167            LOAD_CONST               1 ('status')
                LOAD_FAST_BORROW         4 (result)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               1 ('status')
                LOAD_CONST              15 ('skipped')
                CALL                     2

 168            LOAD_CONST              16 ('warning_count')
                LOAD_FAST_BORROW         4 (result)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               1 ('status')
                CALL                     1
                LOAD_CONST              10 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L7)
                NOT_TAKEN
                LOAD_SMALL_INT           0
                JUMP_FORWARD             1 (to L8)
        L7:     LOAD_SMALL_INT           1

 169    L8:     LOAD_CONST              17 ('action_required')
                LOAD_CONST              18 ('none')

 170            LOAD_CONST               5 ('error_code')
                LOAD_FAST_BORROW         4 (result)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               5 ('error_code')
                CALL                     1

 165            BUILD_MAP                5
                CALL                     2
                POP_TOP

 173            LOAD_CONST               1 ('status')
                LOAD_FAST_BORROW         4 (result)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               1 ('status')
                LOAD_CONST              15 ('skipped')
                CALL                     2

 174            LOAD_CONST               3 ('surface')
                LOAD_CONST               4 ('ops.cache.invalidate.per_brokerage')

 175            LOAD_CONST              14 ('brokerage_id')
                LOAD_FAST_BORROW         2 (bid)

 176            LOAD_CONST              19 ('scope')
                LOAD_FAST_BORROW         4 (result)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              19 ('scope')
                LOAD_CONST               8 ('fleet.brokerage_health')
                CALL                     2

 177            LOAD_CONST              20 ('cleared')
                LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST_BORROW         4 (result)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              20 ('cleared')
                LOAD_SMALL_INT           0
                CALL                     2
                CALL                     1

 178            LOAD_CONST              21 ('reason')
                LOAD_FAST_BORROW         3 (r)

 179            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 180            LOAD_CONST               5 ('error_code')
                LOAD_FAST_BORROW         4 (result)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               5 ('error_code')
                CALL                     1

 172            BUILD_MAP                8
        L9:     RETURN_VALUE

 161   L10:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L11)
                NOT_TAKEN
                RERAISE                  2
       L11:     POP_TOP
       L12:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
                JUMP_BACKWARD_NO_INTERRUPT 183 (to L6)

  --   L13:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L14:     PUSH_EXC_INFO

 182            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      165 (to L26)
                NOT_TAKEN
                STORE_FAST               5 (e)

 183   L15:     LOAD_GLOBAL             18 (logger)
                LOAD_ATTR               21 (warning + NULL|self)

 184            LOAD_CONST              22 ('invalidate_fleet_status_for_brokerage error type=')

 185            LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE

 184            BUILD_STRING             2

 183            CALL                     1
                POP_TOP

 187            LOAD_GLOBAL              6 (_LOCK)
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
       L16:     POP_TOP

 188            LOAD_GLOBAL              9 (int + NULL)
                LOAD_GLOBAL             10 (_STATS)
                LOAD_CONST              11 ('errors')
                BINARY_OP               26 ([])
                CALL                     1
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_GLOBAL             10 (_STATS)
                LOAD_CONST              11 ('errors')
                STORE_SUBSCR

 187   L17:     LOAD_CONST              12 (None)
                LOAD_CONST              12 (None)
                LOAD_CONST              12 (None)
                CALL                     3
                POP_TOP
                JUMP_FORWARD            19 (to L22)
       L18:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L19)
                NOT_TAKEN
                RERAISE                  2
       L19:     POP_TOP
       L20:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
                JUMP_FORWARD             3 (to L22)

  --   L21:     COPY                     3
                POP_EXCEPT
                RERAISE                  1

 190   L22:     LOAD_CONST               1 ('status')
                LOAD_CONST              15 ('skipped')

 191            LOAD_CONST               3 ('surface')
                LOAD_CONST               4 ('ops.cache.invalidate.per_brokerage')

 192            LOAD_CONST               5 ('error_code')
                LOAD_CONST              23 ('unexpected:')
                LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 193            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 189            BUILD_MAP                4
       L23:     SWAP                     2
       L24:     POP_EXCEPT
                LOAD_CONST              12 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RETURN_VALUE

  --   L25:     LOAD_CONST              12 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RERAISE                  1

 182   L26:     RERAISE                  0

  --   L27:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L14 [0]
  L3 to L4 -> L14 [0]
  L4 to L5 -> L10 [2] lasti
  L5 to L9 -> L14 [0]
  L10 to L12 -> L13 [4] lasti
  L12 to L14 -> L14 [0]
  L14 to L15 -> L27 [1] lasti
  L15 to L16 -> L25 [1] lasti
  L16 to L17 -> L18 [3] lasti
  L17 to L18 -> L25 [1] lasti
  L18 to L20 -> L21 [5] lasti
  L20 to L23 -> L25 [1] lasti
  L23 to L24 -> L27 [1] lasti
  L25 to L27 -> L27 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "app\services\operator\cache_invalidation.py", line 197>:
197           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('reason')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object invalidate_fleet_status_all at 0x0000018C17EDA3D0, file "app\services\operator\cache_invalidation.py", line 197>:
 197            RESUME                   0

 201            NOP

 202    L1:     LOAD_GLOBAL              1 (_safe_reason + NULL)
                LOAD_FAST_BORROW         0 (reason)
                CALL                     1
                STORE_FAST               1 (r)

 203            LOAD_GLOBAL              3 (_do_invalidate + NULL)
                LOAD_CONST               1 (None)
                CALL                     1
                STORE_FAST               2 (result)

 204            LOAD_GLOBAL              4 (_LOCK)
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
        L2:     POP_TOP

 205            LOAD_GLOBAL              7 (int + NULL)
                LOAD_GLOBAL              8 (_STATS)
                LOAD_CONST               2 ('all')
                BINARY_OP               26 ([])
                CALL                     1
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_GLOBAL              8 (_STATS)
                LOAD_CONST               2 ('all')
                STORE_SUBSCR

 206            LOAD_FAST_BORROW         2 (result)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               3 ('status')
                CALL                     1
                LOAD_CONST               4 ('ok')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       37 (to L3)
                NOT_TAKEN

 207            LOAD_GLOBAL              7 (int + NULL)
                LOAD_GLOBAL              8 (_STATS)
                LOAD_CONST               5 ('errors')
                BINARY_OP               26 ([])
                CALL                     1
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_GLOBAL              8 (_STATS)
                LOAD_CONST               5 ('errors')
                STORE_SUBSCR

 204    L3:     LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                CALL                     3
                POP_TOP

 208    L4:     LOAD_GLOBAL             13 (_emit_event + NULL)
                LOAD_CONST               6 ('fleet.cache.invalidated')

 209            LOAD_CONST               7 ('brokerage_id')
                LOAD_CONST               1 (None)

 210            LOAD_CONST               3 ('status')
                LOAD_FAST_BORROW         2 (result)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               3 ('status')
                LOAD_CONST               8 ('skipped')
                CALL                     2

 211            LOAD_CONST               9 ('warning_count')
                LOAD_FAST_BORROW         2 (result)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               3 ('status')
                CALL                     1
                LOAD_CONST               4 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN
                LOAD_SMALL_INT           0
                JUMP_FORWARD             1 (to L6)
        L5:     LOAD_SMALL_INT           1

 212    L6:     LOAD_CONST              10 ('action_required')
                LOAD_CONST              11 ('none')

 213            LOAD_CONST              12 ('error_code')
                LOAD_FAST_BORROW         2 (result)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              12 ('error_code')
                CALL                     1

 208            BUILD_MAP                5
                CALL                     2
                POP_TOP

 216            LOAD_CONST               3 ('status')
                LOAD_FAST_BORROW         2 (result)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               3 ('status')
                LOAD_CONST               8 ('skipped')
                CALL                     2

 217            LOAD_CONST              13 ('surface')
                LOAD_CONST              14 ('ops.cache.invalidate.all')

 218            LOAD_CONST              15 ('scope')
                LOAD_FAST_BORROW         2 (result)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              15 ('scope')
                LOAD_CONST               2 ('all')
                CALL                     2

 219            LOAD_CONST              16 ('cleared')
                LOAD_GLOBAL              7 (int + NULL)
                LOAD_FAST_BORROW         2 (result)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              16 ('cleared')
                LOAD_SMALL_INT           0
                CALL                     2
                CALL                     1

 220            LOAD_CONST              17 ('reason')
                LOAD_FAST_BORROW         1 (r)

 221            LOAD_CONST              18 ('warnings')
                BUILD_LIST               0

 222            LOAD_CONST              12 ('error_code')
                LOAD_FAST_BORROW         2 (result)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              12 ('error_code')
                CALL                     1

 215            BUILD_MAP                7
        L7:     RETURN_VALUE

 204    L8:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L9)
                NOT_TAKEN
                RERAISE                  2
        L9:     POP_TOP
       L10:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
                JUMP_BACKWARD_NO_INTERRUPT 181 (to L4)

  --   L11:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L12:     PUSH_EXC_INFO

 224            LOAD_GLOBAL             14 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      165 (to L24)
                NOT_TAKEN
                STORE_FAST               3 (e)

 225   L13:     LOAD_GLOBAL             16 (logger)
                LOAD_ATTR               19 (warning + NULL|self)

 226            LOAD_CONST              19 ('invalidate_fleet_status_all error type=')
                LOAD_GLOBAL             21 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR               22 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 225            CALL                     1
                POP_TOP

 228            LOAD_GLOBAL              4 (_LOCK)
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
       L14:     POP_TOP

 229            LOAD_GLOBAL              7 (int + NULL)
                LOAD_GLOBAL              8 (_STATS)
                LOAD_CONST               5 ('errors')
                BINARY_OP               26 ([])
                CALL                     1
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_GLOBAL              8 (_STATS)
                LOAD_CONST               5 ('errors')
                STORE_SUBSCR

 228   L15:     LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                CALL                     3
                POP_TOP
                JUMP_FORWARD            19 (to L20)
       L16:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L17)
                NOT_TAKEN
                RERAISE                  2
       L17:     POP_TOP
       L18:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
                JUMP_FORWARD             3 (to L20)

  --   L19:     COPY                     3
                POP_EXCEPT
                RERAISE                  1

 231   L20:     LOAD_CONST               3 ('status')
                LOAD_CONST               8 ('skipped')

 232            LOAD_CONST              13 ('surface')
                LOAD_CONST              14 ('ops.cache.invalidate.all')

 233            LOAD_CONST              12 ('error_code')
                LOAD_CONST              20 ('unexpected:')
                LOAD_GLOBAL             21 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR               22 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 234            LOAD_CONST              18 ('warnings')
                BUILD_LIST               0

 230            BUILD_MAP                4
       L21:     SWAP                     2
       L22:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RETURN_VALUE

  --   L23:     LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 224   L24:     RERAISE                  0

  --   L25:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L12 [0]
  L2 to L3 -> L8 [2] lasti
  L3 to L7 -> L12 [0]
  L8 to L10 -> L11 [4] lasti
  L10 to L12 -> L12 [0]
  L12 to L13 -> L25 [1] lasti
  L13 to L14 -> L23 [1] lasti
  L14 to L15 -> L16 [3] lasti
  L15 to L16 -> L23 [1] lasti
  L16 to L18 -> L19 [5] lasti
  L18 to L21 -> L23 [1] lasti
  L21 to L22 -> L25 [1] lasti
  L23 to L25 -> L25 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025230, file "app\services\operator\cache_invalidation.py", line 238>:
238           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

239           LOAD_CONST               2 ('Any')

238           LOAD_CONST               3 ('reason')

241           LOAD_CONST               2 ('Any')

238           LOAD_CONST               4 ('return')

242           LOAD_CONST               5 ('Dict[str, Any]')

238           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object invalidate_fleet_status_row at 0x0000018C17E8A580, file "app\services\operator\cache_invalidation.py", line 238>:
 238            RESUME                   0

 248            NOP

 249    L1:     LOAD_GLOBAL              1 (_safe_brokerage + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                STORE_FAST               2 (bid)

 250            LOAD_GLOBAL              3 (_safe_reason + NULL)
                LOAD_FAST_BORROW         1 (reason)
                CALL                     1
                STORE_FAST               3 (r)

 251            LOAD_FAST_BORROW         2 (bid)
                TO_BOOL
                POP_JUMP_IF_TRUE        12 (to L3)
                NOT_TAKEN

 253            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 254            LOAD_CONST               3 ('surface')
                LOAD_CONST               4 ('ops.cache.invalidate.row')

 255            LOAD_CONST               5 ('error_code')
                LOAD_CONST               6 ('invalid_brokerage_id')

 256            LOAD_CONST               7 ('warnings')
                LOAD_CONST               6 ('invalid_brokerage_id')
                BUILD_LIST               1

 252            BUILD_MAP                4
        L2:     RETURN_VALUE

 258    L3:     NOP

 259    L4:     LOAD_SMALL_INT           0
                LOAD_CONST               8 (('invalidate_for_brokerage',))
                IMPORT_NAME              2 (app.services.operator.fleet_status_cache)
                IMPORT_FROM              3 (invalidate_for_brokerage)
                STORE_FAST               4 (invalidate_for_brokerage)
                POP_TOP

 265    L5:     NOP

 266    L6:     LOAD_FAST                4 (invalidate_for_brokerage)
                PUSH_NULL
                LOAD_FAST                2 (bid)
                CALL                     1
                STORE_FAST               5 (result)

 280    L7:     LOAD_GLOBAL             27 (isinstance + NULL)
                LOAD_FAST                5 (result)
                LOAD_GLOBAL             28 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         9 (to L8)
                NOT_TAKEN

 281            LOAD_CONST               1 ('status')
                LOAD_CONST              13 ('skipped')
                LOAD_CONST              15 ('cleared')
                LOAD_SMALL_INT           0

 282            LOAD_CONST              16 ('scope')
                LOAD_CONST              17 ('per_brokerage')

 281            BUILD_MAP                3
                STORE_FAST               5 (result)

 283    L8:     LOAD_GLOBAL             20 (_LOCK)
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
        L9:     POP_TOP

 284            LOAD_GLOBAL             23 (int + NULL)
                LOAD_GLOBAL             24 (_STATS)
                LOAD_CONST              17 ('per_brokerage')
                BINARY_OP               26 ([])
                CALL                     1
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_GLOBAL             24 (_STATS)
                LOAD_CONST              17 ('per_brokerage')
                STORE_SUBSCR

 285            LOAD_FAST                5 (result)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST               1 ('status')
                CALL                     1
                LOAD_CONST              18 ('ok')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       37 (to L10)
                NOT_TAKEN

 286            LOAD_GLOBAL             23 (int + NULL)
                LOAD_GLOBAL             24 (_STATS)
                LOAD_CONST              11 ('errors')
                BINARY_OP               26 ([])
                CALL                     1
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_GLOBAL             24 (_STATS)
                LOAD_CONST              11 ('errors')
                STORE_SUBSCR

 283   L10:     LOAD_CONST              12 (None)
                LOAD_CONST              12 (None)
                LOAD_CONST              12 (None)
                CALL                     3
                POP_TOP

 287   L11:     LOAD_GLOBAL             33 (_emit_event + NULL)
                LOAD_CONST              19 ('fleet.cache.row_invalidated')

 288            LOAD_CONST              20 ('brokerage_id')
                LOAD_FAST                2 (bid)

 289            LOAD_CONST               1 ('status')
                LOAD_FAST                5 (result)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST               1 ('status')
                LOAD_CONST              13 ('skipped')
                CALL                     2

 290            LOAD_CONST              21 ('warning_count')
                LOAD_FAST                5 (result)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST               1 ('status')
                CALL                     1
                LOAD_CONST              18 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L12)
                NOT_TAKEN
                LOAD_SMALL_INT           0
                JUMP_FORWARD             1 (to L13)
       L12:     LOAD_SMALL_INT           1

 291   L13:     LOAD_CONST              22 ('action_required')
                LOAD_CONST              23 ('none')

 292            LOAD_CONST               5 ('error_code')
                LOAD_FAST                5 (result)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST               5 ('error_code')
                CALL                     1

 287            BUILD_MAP                5
                CALL                     2
                POP_TOP

 295            LOAD_CONST               1 ('status')
                LOAD_FAST                5 (result)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST               1 ('status')
                LOAD_CONST              13 ('skipped')
                CALL                     2

 296            LOAD_CONST               3 ('surface')
                LOAD_CONST               4 ('ops.cache.invalidate.row')

 297            LOAD_CONST              20 ('brokerage_id')
                LOAD_FAST                2 (bid)

 298            LOAD_CONST              16 ('scope')
                LOAD_FAST                5 (result)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST              16 ('scope')
                LOAD_CONST              24 ('brokerage:')
                LOAD_FAST                2 (bid)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     2

 299            LOAD_CONST              15 ('cleared')
                LOAD_GLOBAL             23 (int + NULL)
                LOAD_FAST                5 (result)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST              15 ('cleared')
                LOAD_SMALL_INT           0
                CALL                     2
                CALL                     1

 300            LOAD_CONST              25 ('reason')
                LOAD_FAST                3 (r)

 301            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 302            LOAD_CONST               5 ('error_code')
                LOAD_FAST                5 (result)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST               5 ('error_code')
                CALL                     1

 294            BUILD_MAP                8
       L14:     RETURN_VALUE

  --   L15:     PUSH_EXC_INFO

 262            LOAD_GLOBAL              8 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       16 (to L18)
                NOT_TAKEN
                POP_TOP

 264            LOAD_GLOBAL             11 (invalidate_fleet_status_for_brokerage + NULL)
                LOAD_FAST_LOAD_FAST     35 (bid, r)
                LOAD_CONST               9 (('reason',))
                CALL_KW                  2
                SWAP                     2
       L16:     POP_EXCEPT
       L17:     RETURN_VALUE

 262   L18:     RERAISE                  0

  --   L19:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L20:     PUSH_EXC_INFO

 267            LOAD_GLOBAL              8 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      165 (to L33)
                NOT_TAKEN
                STORE_FAST               6 (e)

 268   L21:     LOAD_GLOBAL             12 (logger)
                LOAD_ATTR               15 (warning + NULL|self)

 269            LOAD_CONST              10 ('invalidate_fleet_status_row underlying error type=')

 270            LOAD_GLOBAL             17 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               18 (__name__)
                FORMAT_SIMPLE

 269            BUILD_STRING             2

 268            CALL                     1
                POP_TOP

 272            LOAD_GLOBAL             20 (_LOCK)
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
       L22:     POP_TOP

 273            LOAD_GLOBAL             23 (int + NULL)
                LOAD_GLOBAL             24 (_STATS)
                LOAD_CONST              11 ('errors')
                BINARY_OP               26 ([])
                CALL                     1
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_GLOBAL             24 (_STATS)
                LOAD_CONST              11 ('errors')
                STORE_SUBSCR

 272   L23:     LOAD_CONST              12 (None)
                LOAD_CONST              12 (None)
                LOAD_CONST              12 (None)
                CALL                     3
                POP_TOP
                JUMP_FORWARD            19 (to L28)
       L24:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L25)
                NOT_TAKEN
                RERAISE                  2
       L25:     POP_TOP
       L26:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
                JUMP_FORWARD             3 (to L28)

  --   L27:     COPY                     3
                POP_EXCEPT
                RERAISE                  1

 275   L28:     LOAD_CONST               1 ('status')
                LOAD_CONST              13 ('skipped')

 276            LOAD_CONST               3 ('surface')
                LOAD_CONST               4 ('ops.cache.invalidate.row')

 277            LOAD_CONST               5 ('error_code')
                LOAD_CONST              14 ('unexpected:')
                LOAD_GLOBAL             17 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               18 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 278            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 274            BUILD_MAP                4
       L29:     SWAP                     2
       L30:     POP_EXCEPT
                LOAD_CONST              12 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
       L31:     RETURN_VALUE

  --   L32:     LOAD_CONST              12 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

 267   L33:     RERAISE                  0

  --   L34:     COPY                     3
                POP_EXCEPT
                RERAISE                  1

 283   L35:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L36)
                NOT_TAKEN
                RERAISE                  2
       L36:     POP_TOP
       L37:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 394 (to L11)

  --   L38:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L39:     PUSH_EXC_INFO

 304            LOAD_GLOBAL              8 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      165 (to L51)
                NOT_TAKEN
                STORE_FAST               6 (e)

 305   L40:     LOAD_GLOBAL             12 (logger)
                LOAD_ATTR               15 (warning + NULL|self)

 306            LOAD_CONST              26 ('invalidate_fleet_status_row error type=')
                LOAD_GLOBAL             17 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               18 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 305            CALL                     1
                POP_TOP

 308            LOAD_GLOBAL             20 (_LOCK)
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
       L41:     POP_TOP

 309            LOAD_GLOBAL             23 (int + NULL)
                LOAD_GLOBAL             24 (_STATS)
                LOAD_CONST              11 ('errors')
                BINARY_OP               26 ([])
                CALL                     1
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_GLOBAL             24 (_STATS)
                LOAD_CONST              11 ('errors')
                STORE_SUBSCR

 308   L42:     LOAD_CONST              12 (None)
                LOAD_CONST              12 (None)
                LOAD_CONST              12 (None)
                CALL                     3
                POP_TOP
                JUMP_FORWARD            19 (to L47)
       L43:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L44)
                NOT_TAKEN
                RERAISE                  2
       L44:     POP_TOP
       L45:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
                JUMP_FORWARD             3 (to L47)

  --   L46:     COPY                     3
                POP_EXCEPT
                RERAISE                  1

 311   L47:     LOAD_CONST               1 ('status')
                LOAD_CONST              13 ('skipped')

 312            LOAD_CONST               3 ('surface')
                LOAD_CONST               4 ('ops.cache.invalidate.row')

 313            LOAD_CONST               5 ('error_code')
                LOAD_CONST              14 ('unexpected:')
                LOAD_GLOBAL             17 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               18 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 314            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 310            BUILD_MAP                4
       L48:     SWAP                     2
       L49:     POP_EXCEPT
                LOAD_CONST              12 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RETURN_VALUE

  --   L50:     LOAD_CONST              12 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

 304   L51:     RERAISE                  0

  --   L52:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L39 [0]
  L4 to L5 -> L15 [0]
  L6 to L7 -> L20 [0]
  L7 to L9 -> L39 [0]
  L9 to L10 -> L35 [2] lasti
  L10 to L14 -> L39 [0]
  L15 to L16 -> L19 [1] lasti
  L16 to L17 -> L39 [0]
  L18 to L19 -> L19 [1] lasti
  L19 to L20 -> L39 [0]
  L20 to L21 -> L34 [1] lasti
  L21 to L22 -> L32 [1] lasti
  L22 to L23 -> L24 [3] lasti
  L23 to L24 -> L32 [1] lasti
  L24 to L26 -> L27 [5] lasti
  L26 to L29 -> L32 [1] lasti
  L29 to L30 -> L34 [1] lasti
  L30 to L31 -> L39 [0]
  L32 to L34 -> L34 [1] lasti
  L34 to L35 -> L39 [0]
  L35 to L37 -> L38 [4] lasti
  L37 to L39 -> L39 [0]
  L39 to L40 -> L52 [1] lasti
  L40 to L41 -> L50 [1] lasti
  L41 to L42 -> L43 [3] lasti
  L42 to L43 -> L50 [1] lasti
  L43 to L45 -> L46 [5] lasti
  L45 to L48 -> L50 [1] lasti
  L48 to L49 -> L52 [1] lasti
  L50 to L52 -> L52 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025930, file "app\services\operator\cache_invalidation.py", line 318>:
318           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_ids')

319           LOAD_CONST               2 ('Any')

318           LOAD_CONST               3 ('reason')

321           LOAD_CONST               2 ('Any')

318           LOAD_CONST               4 ('return')

322           LOAD_CONST               5 ('Dict[str, Any]')

318           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object invalidate_fleet_status_rows at 0x0000018C17D7CD30, file "app\services\operator\cache_invalidation.py", line 318>:
 318            RESUME                   0

 326            NOP

 327    L1:     LOAD_GLOBAL              1 (_safe_reason + NULL)
                LOAD_FAST_BORROW         1 (reason)
                CALL                     1
                STORE_FAST               2 (r)

 328            LOAD_FAST_BORROW         0 (brokerage_ids)
                TO_BOOL
                POP_JUMP_IF_TRUE        12 (to L3)
                NOT_TAKEN

 330            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 331            LOAD_CONST               3 ('surface')
                LOAD_CONST               4 ('ops.cache.invalidate.rows')

 332            LOAD_CONST               5 ('error_code')
                LOAD_CONST               6 ('no_brokerage_ids')

 333            LOAD_CONST               7 ('warnings')
                LOAD_CONST               6 ('no_brokerage_ids')
                BUILD_LIST               1

 329            BUILD_MAP                4
        L2:     RETURN_VALUE

 335    L3:     BUILD_LIST               0
                STORE_FAST               3 (ids)

 336    L4:     NOP

 337    L5:     LOAD_FAST_BORROW         0 (brokerage_ids)
                GET_ITER
        L6:     FOR_ITER                63 (to L11)
                STORE_FAST               4 (v)

 338            LOAD_GLOBAL              3 (_safe_brokerage + NULL)
                LOAD_FAST_BORROW         4 (v)
                CALL                     1
                STORE_FAST               5 (s)

 339            LOAD_FAST_BORROW         5 (s)
                TO_BOOL
                POP_JUMP_IF_FALSE       24 (to L7)
                NOT_TAKEN
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (s, ids)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       18 (to L7)
                NOT_TAKEN

 340            LOAD_FAST_BORROW         3 (ids)
                LOAD_ATTR                5 (append + NULL|self)
                LOAD_FAST_BORROW         5 (s)
                CALL                     1
                POP_TOP

 341    L7:     LOAD_GLOBAL              7 (len + NULL)
                LOAD_FAST_BORROW         3 (ids)
                CALL                     1
                LOAD_SMALL_INT         200
                COMPARE_OP             188 (bool(>=))
        L8:     POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN
                JUMP_BACKWARD           63 (to L6)

 342    L9:     POP_TOP
       L10:     JUMP_FORWARD             3 (to L13)

 337   L11:     END_FOR
                POP_ITER
       L12:     NOP

 350   L13:     LOAD_FAST_BORROW         3 (ids)
                TO_BOOL
                POP_JUMP_IF_TRUE        12 (to L17)
       L14:     NOT_TAKEN

 352   L15:     LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 353            LOAD_CONST               3 ('surface')
                LOAD_CONST               4 ('ops.cache.invalidate.rows')

 354            LOAD_CONST               5 ('error_code')
                LOAD_CONST               9 ('no_valid_brokerage_ids')

 355            LOAD_CONST               7 ('warnings')
                LOAD_CONST               9 ('no_valid_brokerage_ids')
                BUILD_LIST               1

 351            BUILD_MAP                4
       L16:     RETURN_VALUE

 357   L17:     LOAD_SMALL_INT           0
                STORE_FAST               6 (cleared_total)

 358            BUILD_LIST               0
                STORE_FAST               7 (per)

 359            LOAD_FAST_BORROW         3 (ids)
                GET_ITER
       L18:     FOR_ITER               132 (to L23)
                STORE_FAST               8 (bid)

 360            LOAD_GLOBAL             11 (invalidate_fleet_status_row + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 130 (bid, r)
                LOAD_CONST              10 (('reason',))
                CALL_KW                  2
                STORE_FAST               9 (env)

 361            LOAD_FAST                6 (cleared_total)
                LOAD_GLOBAL             13 (int + NULL)
                LOAD_FAST_BORROW         9 (env)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              11 ('cleared')
                LOAD_SMALL_INT           0
                CALL                     2
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L19)
                NOT_TAKEN
                POP_TOP
                LOAD_SMALL_INT           0
       L19:     CALL                     1
                BINARY_OP               13 (+=)
                STORE_FAST               6 (cleared_total)

 362            LOAD_FAST                7 (per)
                LOAD_ATTR                5 (append + NULL|self)

 363            LOAD_CONST              12 ('brokerage_id')
                LOAD_FAST                8 (bid)

 364            LOAD_CONST               1 ('status')
                LOAD_FAST_BORROW         9 (env)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST               1 ('status')
                CALL                     1

 365            LOAD_CONST              11 ('cleared')
                LOAD_GLOBAL             13 (int + NULL)
                LOAD_FAST_BORROW         9 (env)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              11 ('cleared')
                LOAD_SMALL_INT           0
                CALL                     2
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L22)
       L20:     NOT_TAKEN
       L21:     POP_TOP
                LOAD_SMALL_INT           0
       L22:     CALL                     1

 362            BUILD_MAP                3
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          134 (to L18)

 359   L23:     END_FOR
                POP_ITER

 368            LOAD_CONST               1 ('status')
                LOAD_CONST              13 ('ok')

 369            LOAD_CONST               3 ('surface')
                LOAD_CONST               4 ('ops.cache.invalidate.rows')

 370            LOAD_CONST              14 ('count')
                LOAD_GLOBAL              7 (len + NULL)
                LOAD_FAST_BORROW         3 (ids)
                CALL                     1

 371            LOAD_CONST              11 ('cleared')
                LOAD_FAST_BORROW         6 (cleared_total)

 372            LOAD_CONST              15 ('rows')
                LOAD_FAST_BORROW         7 (per)

 373            LOAD_CONST              16 ('reason')
                LOAD_FAST_BORROW         2 (r)

 374            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 375            LOAD_CONST               5 ('error_code')
                LOAD_CONST              17 (None)

 367            BUILD_MAP                8
       L24:     RETURN_VALUE

  --   L25:     PUSH_EXC_INFO

 343            LOAD_GLOBAL              8 (TypeError)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       15 (to L28)
                NOT_TAKEN
                POP_TOP

 345            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 346            LOAD_CONST               3 ('surface')
                LOAD_CONST               4 ('ops.cache.invalidate.rows')

 347            LOAD_CONST               5 ('error_code')
                LOAD_CONST               8 ('brokerage_ids_not_iterable')

 348            LOAD_CONST               7 ('warnings')
                LOAD_CONST               8 ('brokerage_ids_not_iterable')
                BUILD_LIST               1

 344            BUILD_MAP                4
                SWAP                     2
       L26:     POP_EXCEPT
       L27:     RETURN_VALUE

 343   L28:     RERAISE                  0

  --   L29:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L30:     PUSH_EXC_INFO

 377            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      165 (to L42)
                NOT_TAKEN
                STORE_FAST              10 (e)

 378   L31:     LOAD_GLOBAL             18 (logger)
                LOAD_ATTR               21 (warning + NULL|self)

 379            LOAD_CONST              18 ('invalidate_fleet_status_rows error type=')
                LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 378            CALL                     1
                POP_TOP

 381            LOAD_GLOBAL             26 (_LOCK)
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
       L32:     POP_TOP

 382            LOAD_GLOBAL             13 (int + NULL)
                LOAD_GLOBAL             28 (_STATS)
                LOAD_CONST              19 ('errors')
                BINARY_OP               26 ([])
                CALL                     1
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_GLOBAL             28 (_STATS)
                LOAD_CONST              19 ('errors')
                STORE_SUBSCR

 381   L33:     LOAD_CONST              17 (None)
                LOAD_CONST              17 (None)
                LOAD_CONST              17 (None)
                CALL                     3
                POP_TOP
                JUMP_FORWARD            19 (to L38)
       L34:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L35)
                NOT_TAKEN
                RERAISE                  2
       L35:     POP_TOP
       L36:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
                JUMP_FORWARD             3 (to L38)

  --   L37:     COPY                     3
                POP_EXCEPT
                RERAISE                  1

 384   L38:     LOAD_CONST               1 ('status')
                LOAD_CONST              20 ('skipped')

 385            LOAD_CONST               3 ('surface')
                LOAD_CONST               4 ('ops.cache.invalidate.rows')

 386            LOAD_CONST               5 ('error_code')
                LOAD_CONST              21 ('unexpected:')
                LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 387            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 383            BUILD_MAP                4
       L39:     SWAP                     2
       L40:     POP_EXCEPT
                LOAD_CONST              17 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RETURN_VALUE

  --   L41:     LOAD_CONST              17 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RERAISE                  1

 377   L42:     RERAISE                  0

  --   L43:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L30 [0]
  L3 to L4 -> L30 [0]
  L5 to L8 -> L25 [0]
  L9 to L10 -> L25 [0]
  L10 to L11 -> L30 [0]
  L11 to L12 -> L25 [0]
  L12 to L14 -> L30 [0]
  L15 to L16 -> L30 [0]
  L17 to L20 -> L30 [0]
  L21 to L24 -> L30 [0]
  L25 to L26 -> L29 [1] lasti
  L26 to L27 -> L30 [0]
  L28 to L29 -> L29 [1] lasti
  L29 to L30 -> L30 [0]
  L30 to L31 -> L43 [1] lasti
  L31 to L32 -> L41 [1] lasti
  L32 to L33 -> L34 [3] lasti
  L33 to L34 -> L41 [1] lasti
  L34 to L36 -> L37 [5] lasti
  L36 to L39 -> L41 [1] lasti
  L39 to L40 -> L43 [1] lasti
  L41 to L43 -> L43 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025330, file "app\services\operator\cache_invalidation.py", line 391>:
391           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

392           LOAD_CONST               2 ('Any')

391           LOAD_CONST               3 ('reason')

394           LOAD_CONST               2 ('Any')

391           LOAD_CONST               4 ('return')

395           LOAD_CONST               5 ('Dict[str, Any]')

391           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object invalidate_fleet_status_for_incident at 0x0000018C18010B30, file "app\services\operator\cache_invalidation.py", line 391>:
391           RESUME                   0

399           LOAD_FAST_BORROW         0 (brokerage_id)
              POP_JUMP_IF_NONE        12 (to L1)
              NOT_TAKEN
              LOAD_GLOBAL              1 (_safe_brokerage + NULL)
              LOAD_FAST_BORROW         0 (brokerage_id)
              CALL                     1
              JUMP_FORWARD             1 (to L2)
      L1:     LOAD_CONST               1 (None)
      L2:     STORE_FAST               2 (bid)

400           LOAD_FAST_BORROW         2 (bid)
              TO_BOOL
              POP_JUMP_IF_FALSE       23 (to L3)
              NOT_TAKEN

401           LOAD_GLOBAL              3 (invalidate_fleet_status_row + NULL)
              LOAD_FAST_BORROW         2 (bid)
              LOAD_GLOBAL              5 (_safe_reason + NULL)
              LOAD_FAST_BORROW         1 (reason)
              CALL                     1
              LOAD_CONST               2 (('reason',))
              CALL_KW                  2
              RETURN_VALUE

402   L3:     LOAD_GLOBAL              7 (invalidate_fleet_status_all + NULL)
              LOAD_GLOBAL              5 (_safe_reason + NULL)
              LOAD_FAST_BORROW         1 (reason)
              CALL                     1
              LOAD_CONST               2 (('reason',))
              CALL_KW                  1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025B30, file "app\services\operator\cache_invalidation.py", line 405>:
405           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

406           LOAD_CONST               2 ('Any')

405           LOAD_CONST               3 ('reason')

408           LOAD_CONST               2 ('Any')

405           LOAD_CONST               4 ('return')

409           LOAD_CONST               5 ('Dict[str, Any]')

405           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object invalidate_fleet_status_for_cutover at 0x0000018C18025630, file "app\services\operator\cache_invalidation.py", line 405>:
405           RESUME                   0

412           LOAD_GLOBAL              1 (invalidate_fleet_status_row + NULL)
              LOAD_FAST_BORROW         0 (brokerage_id)
              LOAD_GLOBAL              3 (_safe_reason + NULL)
              LOAD_FAST_BORROW         1 (reason)
              CALL                     1
              LOAD_CONST               1 (('reason',))
              CALL_KW                  2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024F30, file "app\services\operator\cache_invalidation.py", line 415>:
415           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

416           LOAD_CONST               2 ('Any')

415           LOAD_CONST               3 ('reason')

418           LOAD_CONST               2 ('Any')

415           LOAD_CONST               4 ('return')

419           LOAD_CONST               5 ('Dict[str, Any]')

415           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object invalidate_fleet_status_for_breaker at 0x0000018C18025030, file "app\services\operator\cache_invalidation.py", line 415>:
415           RESUME                   0

422           LOAD_GLOBAL              1 (invalidate_fleet_status_row + NULL)
              LOAD_FAST_BORROW         0 (brokerage_id)
              LOAD_GLOBAL              3 (_safe_reason + NULL)
              LOAD_FAST_BORROW         1 (reason)
              CALL                     1
              LOAD_CONST               1 (('reason',))
              CALL_KW                  2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "app\services\operator\cache_invalidation.py", line 425>:
425           RESUME                   0
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

Disassembly of <code object cache_invalidation_report at 0x0000018C1794E9E0, file "app\services\operator\cache_invalidation.py", line 425>:
 425           RESUME                   0

 428           LOAD_GLOBAL              0 (_LOCK)
               COPY                     1
               LOAD_SPECIAL             1 (__exit__)
               SWAP                     2
               SWAP                     3
               LOAD_SPECIAL             0 (__enter__)
               CALL                     0
       L1:     POP_TOP

 430           LOAD_CONST               1 ('status')
               LOAD_CONST               2 ('ok')

 431           LOAD_CONST               3 ('surface')
               LOAD_CONST               4 ('ops.cache.invalidation.report')

 432           LOAD_CONST               5 ('per_brokerage')
               LOAD_GLOBAL              3 (int + NULL)
               LOAD_GLOBAL              4 (_STATS)
               LOAD_CONST               5 ('per_brokerage')
               BINARY_OP               26 ([])
               CALL                     1

 433           LOAD_CONST               6 ('all')
               LOAD_GLOBAL              3 (int + NULL)
               LOAD_GLOBAL              4 (_STATS)
               LOAD_CONST               6 ('all')
               BINARY_OP               26 ([])
               CALL                     1

 434           LOAD_CONST               7 ('errors')
               LOAD_GLOBAL              3 (int + NULL)
               LOAD_GLOBAL              4 (_STATS)
               LOAD_CONST               7 ('errors')
               BINARY_OP               26 ([])
               CALL                     1

 435           LOAD_CONST               8 ('warnings')
               BUILD_LIST               0

 436           LOAD_CONST               9 ('error_code')
               LOAD_CONST              10 (None)

 429           BUILD_MAP                7

 428   L2:     SWAP                     3
               SWAP                     2
               LOAD_CONST              10 (None)
               LOAD_CONST              10 (None)
               LOAD_CONST              10 (None)
               CALL                     3
               POP_TOP
               RETURN_VALUE
       L3:     PUSH_EXC_INFO
               WITH_EXCEPT_START
               TO_BOOL
               POP_JUMP_IF_TRUE         2 (to L4)
               NOT_TAKEN
               RERAISE                  2
       L4:     POP_TOP
       L5:     POP_EXCEPT
               POP_TOP
               POP_TOP
               POP_TOP
               LOAD_CONST              10 (None)
               RETURN_VALUE

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [2] lasti
  L3 to L5 -> L6 [4] lasti
```
