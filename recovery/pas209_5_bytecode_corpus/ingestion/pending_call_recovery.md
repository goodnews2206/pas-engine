# ingestion/pending_call_recovery

- **pyc:** `app\services\ingestion\__pycache__\pending_call_recovery.cpython-314.pyc`
- **expected source path (absent):** `app\services\ingestion/pending_call_recovery.py`
- **co_filename (from bytecode):** `app\services\ingestion\pending_call_recovery.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** ingestion

## Module docstring

```
PAS170 — Pending-call queue visibility + stale DIALING
recovery (operator-only).

Closes two PAS-AUDIT-01 gaps:

* **C3 — Worker process killed mid-dial.** Row stays
  ``DIALING`` forever. PAS170 ships a stale-lock detector
  + an explicit operator-driven recovery helper that flips
  the row back to ``PENDING`` so the worker can re-attempt
  on its next drain.
* **No queue visibility.** Operators have no quick way to
  ask "how deep is the pending-call queue right now? how
  old is the oldest item?". PAS170 ships a structural
  ``queue_status_report`` plus an age histogram.

Hard doctrine:

* No phone / email / name / notes / property in any report.
  The queue endpoint surfaces only ``brokerage_id``,
  ``source``, ``status``, ``count``, ``age_seconds``.
* Recovery is operator-driven. PAS170 does NOT auto-recover
  on the worker's next tick — the operator must invoke
  ``recover_stale_dialing_rows()`` explicitly (or run the
  smoke-plan script). This mirrors the PAS162 worker-OFF-
  by-default doctrine.
* Default stale threshold is conservative (15 minutes). The
  operator can pass ``stale_after_seconds`` to tighten /
  loosen.
* No exception escape. DB unavailable / table missing → the
  helper returns a structural ``status="skipped"`` envelope
  and exits 0.
* No raw payload storage anywhere in this module.

Public surface:
  * ``queue_status_report(*, brokerage_id=None, now=None)``
  * ``detect_stale_dialing_rows(*, brokerage_id=None,
        stale_after_seconds=900, limit=200, now=None)``
  * ``recover_stale_dialing_rows(*, brokerage_id=None,
        stale_after_seconds=900, limit=50, now=None,
        dry_run=True, worker_id_hint=None)``
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.db.supabase_client`, `datetime`, `get_supabase`, `logging`, `timedelta`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_age_seconds`, `_bucket_for`, `_clamp`, `_empty_status_report`, `_get_db_safe`, `_iso`, `_now_dt`, `detect_stale_dialing_rows`, `queue_status_report`, `recover_stale_dialing_rows`

## Env-key candidates

`DIALING`, `PENDING`

## String constants (redacted where noted)

- '\nPAS170 — Pending-call queue visibility + stale DIALING\nrecovery (operator-only).\n\nCloses two PAS-AUDIT-01 gaps:\n\n* **C3 — Worker process killed mid-dial.** Row stays\n  ``DIALING`` forever. PAS170 ships a stale-lock detector\n  + an explicit operator-driven recovery helper that flips\n  the row back to ``PENDING`` so the worker can re-attempt\n  on its next drain.\n* **No queue visibility.** Operators have no quick way to\n  ask "how deep is the pending-call queue right now? how\n  old is the oldest item?". PAS170 ships a structural\n  ``queue_status_report`` plus an age histogram.\n\nHard doctrine:\n\n* No phone / email / name / notes / property in any report.\n  The queue endpoint surfaces only ``brokerage_id``,\n  ``source``, ``status``, ``count``, ``age_seconds``.\n* Recovery is operator-driven. PAS170 does NOT auto-recover\n  on the worker\'s next tick — the operator must invoke\n  ``recover_stale_dialing_rows()`` explicitly (or run the\n  smoke-plan script). This mirrors the PAS162 worker-OFF-\n  by-default doctrine.\n* Default stale threshold is conservative (15 minutes). The\n  operator can pass ``stale_after_seconds`` to tighten /\n  loosen.\n* No exception escape. DB unavailable / table missing → the\n  helper returns a structural ``status="skipped"`` envelope\n  and exits 0.\n* No raw payload storage anywhere in this module.\n\nPublic surface:\n  * ``queue_status_report(*, brokerage_id=None, now=None)``\n  * ``detect_stale_dialing_rows(*, brokerage_id=None,\n        stale_after_seconds=900, limit=200, now=None)``\n  * ``recover_stale_dialing_rows(*, brokerage_id=None,\n        stale_after_seconds=900, limit=50, now=None,\n        dry_run=True, worker_id_hint=None)``\n'
- 'pas.ingestion.pending_call_recovery'
- 'pas_pending_calls'
- 'warnings'
- 'error_code'
- 'brokerage_id'
- 'now'
- 'stale_after_seconds'
- 'limit'
- 'dry_run'
- 'worker_id_hint'
- 'Any'
- 'return'
- 'datetime'
- '+00:00'
- 'str'
- 'seconds'
- 'now_dt'
- 'ts_str'
- 'Optional[int]'
- 'value'
- 'int'
- 'default'
- 'pending_call_recovery db client unavailable type='
- 'age_secs'
- 'unknown'
- 'Optional[str]'
- 'Optional[List[str]]'
- 'Dict[str, Any]'
- 'status'
- 'skipped'
- 'total'
- 'by_status'
- 'by_age'
- 'oldest_age_seconds'
- 'Return a structural snapshot of the pending-call queue.\n\nReturns a closed-shape envelope — operator endpoints can\npaste it into a dashboard without scrubbing.\n\nNEVER returns phone / email / name / notes / property /\ntranscript / raw_payload. Per-row PII is intentionally\nNOT fetched.\n\nNEVER raises. On DB unavailable returns ``status="skipped"``\n+ warning ``pending_call_queue_store_unavailable``.\n'
- 'pending_call_queue_store_unavailable'
- 'brokerage_id, source, status, created_at, locked_at'
- 'data'
- 'queue_status_report db error type='
- 'db_read_failed:'
- 'created_at'
- 'List pending-call rows whose ``status=\'DIALING\'`` and\nwhose ``locked_at`` is older than ``stale_after_seconds``.\n\nReturns a structural envelope. NEVER returns phone /\nemail / name. Each row entry carries only\n``pending_call_id``, ``brokerage_id``, ``source``,\n``locked_by``, ``locked_at``, ``age_seconds``.\n\nNEVER raises. On DB unavailable returns\n``status="skipped"``.\n'
- 'count'
- 'rows'
- 'pending_call_id, brokerage_id, source, locked_by, locked_at'
- 'DIALING'
- 'locked_at'
- 'detect_stale_dialing_rows db error type='
- 'pending_call_id'
- 'source'
- 'locked_by'
- 'age_seconds'
- 'bool'
- 'Operator-driven recovery: revert stale ``DIALING`` rows\nback to ``PENDING`` so the worker can re-attempt them.\n\n**Dry-run by default.** ``dry_run=False`` is required to\nactually update rows. Mirrors the PAS167 reaper + PAS168\nrotation script doctrine.\n\nReturns a structural envelope::\n\n    {\n      "status":              "ok" | "skipped" | "failed",\n      "mode":                "dry-run" | "execute",\n      "brokerage_id":        Optional[str],\n      "stale_after_seconds": int,\n      "limit":               int,\n      "candidate_count":     int,\n      "recovered_count":     int,\n      "skipped_count":       int,\n      "failed_count":        int,\n      "warnings":            [<structural tokens>],\n      "error_code":          None | "<structural token>",\n    }\n\nNEVER raises. NEVER returns phone / email / name / per-\nrow identifying fields.\n'
- 'pas170-recovery'
- 'mode'
- 'execute'
- 'dry-run'
- 'candidate_count'
- 'recovered_count'
- 'skipped_count'
- 'failed_count'
- 'PENDING'
- 'last_error_code'
- 'pas170_recovered_from_stale_dialing'
- 'last_error_at'
- 'db_write_failed:'
- 'recover_stale_dialing_rows update error id='
- ' type='
- 'failed'
- 'stale_recovery_partial_failure'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS170 — Pending-call queue visibility + stale DIALING\nrecovery (operator-only).\n\nCloses two PAS-AUDIT-01 gaps:\n\n* **C3 — Worker process killed mid-dial.** Row stays\n  ``DIALING`` forever. PAS170 ships a stale-lock detector\n  + an explicit operator-driven recovery helper that flips\n  the row back to ``PENDING`` so the worker can re-attempt\n  on its next drain.\n* **No queue visibility.** Operators have no quick way to\n  ask "how deep is the pending-call queue right now? how\n  old is the oldest item?". PAS170 ships a structural\n  ``queue_status_report`` plus an age histogram.\n\nHard doctrine:\n\n* No phone / email / name / notes / property in any report.\n  The queue endpoint surfaces only ``brokerage_id``,\n  ``source``, ``status``, ``count``, ``age_seconds``.\n* Recovery is operator-driven. PAS170 does NOT auto-recover\n  on the worker\'s next tick — the operator must invoke\n  ``recover_stale_dialing_rows()`` explicitly (or run the\n  smoke-plan script). This mirrors the PAS162 worker-OFF-\n  by-default doctrine.\n* Default stale threshold is conservative (15 minutes). The\n  operator can pass ``stale_after_seconds`` to tighten /\n  loosen.\n* No exception escape. DB unavailable / table missing → the\n  helper returns a structural ``status="skipped"`` envelope\n  and exits 0.\n* No raw payload storage anywhere in this module.\n\nPublic surface:\n  * ``queue_status_report(*, brokerage_id=None, now=None)``\n  * ``detect_stale_dialing_rows(*, brokerage_id=None,\n        stale_after_seconds=900, limit=200, now=None)``\n  * ``recover_stale_dialing_rows(*, brokerage_id=None,\n        stale_after_seconds=900, limit=50, now=None,\n        dry_run=True, worker_id_hint=None)``\n')
              STORE_NAME               0 (__doc__)

 44           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 46           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 47           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('datetime', 'timedelta', 'timezone'))
              IMPORT_NAME              4 (datetime)
              IMPORT_FROM              4 (datetime)
              STORE_NAME               4 (datetime)
              IMPORT_FROM              5 (timedelta)
              STORE_NAME               5 (timedelta)
              IMPORT_FROM              6 (timezone)
              STORE_NAME               6 (timezone)
              POP_TOP

 48           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('Any', 'Dict', 'List', 'Optional'))
              IMPORT_NAME              7 (typing)
              IMPORT_FROM              8 (Any)
              STORE_NAME               8 (Any)
              IMPORT_FROM              9 (Dict)
              STORE_NAME               9 (Dict)
              IMPORT_FROM             10 (List)
              STORE_NAME              10 (List)
              IMPORT_FROM             11 (Optional)
              STORE_NAME              11 (Optional)
              POP_TOP

 51           LOAD_NAME                3 (logging)
              LOAD_ATTR               24 (getLogger)
              PUSH_NULL
              LOAD_CONST               5 ('pas.ingestion.pending_call_recovery')
              CALL                     1
              STORE_NAME              13 (logger)

 54           LOAD_CONST               6 ('pas_pending_calls')
              STORE_NAME              14 (_TABLE)

 57           LOAD_CONST              37 (('PENDING', 'LOCKED', 'DIALING', 'DIALED', 'FAILED', 'CANCELLED'))
              STORE_NAME              15 (_PENDING_STATUSES)

 66           LOAD_CONST              17 (900)
              STORE_NAME              16 (DEFAULT_STALE_AFTER_SECONDS)

 69           LOAD_CONST               7 (1000)
              STORE_NAME              17 (_LIST_HARD_CAP)

 70           LOAD_SMALL_INT         200
              STORE_NAME              18 (_RECOVER_HARD_CAP)

 77           LOAD_CONST              38 ((None,))
              LOAD_CONST               8 (<code object __annotate__ at 0x0000018C17FA35A0, file "app\services\ingestion\pending_call_recovery.py", line 77>)
              MAKE_FUNCTION
              LOAD_CONST               9 (<code object _now_dt at 0x0000018C17F83C10, file "app\services\ingestion\pending_call_recovery.py", line 77>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              19 (_now_dt)

 93           LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA3B40, file "app\services\ingestion\pending_call_recovery.py", line 93>)
              MAKE_FUNCTION
              LOAD_CONST              11 (<code object _iso at 0x0000018C18025E30, file "app\services\ingestion\pending_call_recovery.py", line 93>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              20 (_iso)

 97           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C18025D30, file "app\services\ingestion\pending_call_recovery.py", line 97>)
              MAKE_FUNCTION
              LOAD_CONST              13 (<code object _age_seconds at 0x0000018C17F0C960, file "app\services\ingestion\pending_call_recovery.py", line 97>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              21 (_age_seconds)

111           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C18024930, file "app\services\ingestion\pending_call_recovery.py", line 111>)
              MAKE_FUNCTION
              LOAD_CONST              15 (<code object _clamp at 0x0000018C18038B70, file "app\services\ingestion\pending_call_recovery.py", line 111>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              22 (_clamp)

123           LOAD_CONST              16 (<code object _get_db_safe at 0x0000018C17FF1230, file "app\services\ingestion\pending_call_recovery.py", line 123>)
              MAKE_FUNCTION
              STORE_NAME              23 (_get_db_safe)

141           LOAD_CONST              39 ((('lt_60s', 0, 60), ('lt_5m', 60, 300), ('lt_15m', 300, 900), ('lt_1h', 900, 3600), ('lt_6h', 3600, 21600), ('lt_24h', 21600, 86400), ('ge_24h', 86400, None)))
              STORE_NAME              24 (_AGE_BUCKETS)

152           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA3C30, file "app\services\ingestion\pending_call_recovery.py", line 152>)
              MAKE_FUNCTION
              LOAD_CONST              19 (<code object _bucket_for at 0x0000018C17F96420, file "app\services\ingestion\pending_call_recovery.py", line 152>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              25 (_bucket_for)

163           LOAD_CONST              20 ('warnings')

166           LOAD_CONST               2 (None)

163           LOAD_CONST              21 ('error_code')

167           LOAD_CONST               2 (None)

163           BUILD_MAP                2
              LOAD_CONST              22 (<code object __annotate__ at 0x0000018C18025730, file "app\services\ingestion\pending_call_recovery.py", line 163>)
              MAKE_FUNCTION
              LOAD_CONST              23 (<code object _empty_status_report at 0x0000018C180483B0, file "app\services\ingestion\pending_call_recovery.py", line 163>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              26 (_empty_status_report)

181           LOAD_CONST              24 ('brokerage_id')

183           LOAD_CONST               2 (None)

181           LOAD_CONST              25 ('now')

184           LOAD_CONST               2 (None)

181           BUILD_MAP                2
              LOAD_CONST              26 (<code object __annotate__ at 0x0000018C18025330, file "app\services\ingestion\pending_call_recovery.py", line 181>)
              MAKE_FUNCTION
              LOAD_CONST              27 (<code object queue_status_report at 0x0000018C17EDA850, file "app\services\ingestion\pending_call_recovery.py", line 181>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              27 (queue_status_report)

273           LOAD_CONST              24 ('brokerage_id')

275           LOAD_CONST               2 (None)

273           LOAD_CONST              28 ('stale_after_seconds')

276           LOAD_NAME               16 (DEFAULT_STALE_AFTER_SECONDS)

273           LOAD_CONST              29 ('limit')

277           LOAD_SMALL_INT         200

273           LOAD_CONST              25 ('now')

278           LOAD_CONST               2 (None)

273           BUILD_MAP                4
              LOAD_CONST              30 (<code object __annotate__ at 0x0000018C18024C30, file "app\services\ingestion\pending_call_recovery.py", line 273>)
              MAKE_FUNCTION
              LOAD_CONST              31 (<code object detect_stale_dialing_rows at 0x0000018C17ED26C0, file "app\services\ingestion\pending_call_recovery.py", line 273>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              28 (detect_stale_dialing_rows)

378           LOAD_CONST              24 ('brokerage_id')

380           LOAD_CONST               2 (None)

378           LOAD_CONST              28 ('stale_after_seconds')

381           LOAD_NAME               16 (DEFAULT_STALE_AFTER_SECONDS)

378           LOAD_CONST              29 ('limit')

382           LOAD_SMALL_INT          50

378           LOAD_CONST              25 ('now')

383           LOAD_CONST               2 (None)

378           LOAD_CONST              32 ('dry_run')

384           LOAD_CONST              33 (True)

378           LOAD_CONST              34 ('worker_id_hint')

385           LOAD_CONST               2 (None)

378           BUILD_MAP                6
              LOAD_CONST              35 (<code object __annotate__ at 0x0000018C18090140, file "app\services\ingestion\pending_call_recovery.py", line 378>)
              MAKE_FUNCTION
              LOAD_CONST              36 (<code object recover_stale_dialing_rows at 0x0000018C17F78810, file "app\services\ingestion\pending_call_recovery.py", line 378>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              29 (recover_stale_dialing_rows)

550           BUILD_LIST               0
              LOAD_CONST              40 (('DEFAULT_STALE_AFTER_SECONDS', 'queue_status_report', 'detect_stale_dialing_rows', 'recover_stale_dialing_rows'))
              LIST_EXTEND              1
              STORE_NAME              30 (__all__)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "app\services\ingestion\pending_call_recovery.py", line 77>:
 77           RESUME                   0
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
              LOAD_CONST               4 ('datetime')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _now_dt at 0x0000018C17F83C10, file "app\services\ingestion\pending_call_recovery.py", line 77>:
  77            RESUME                   0

  78            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (now)
                LOAD_GLOBAL              2 (datetime)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       78 (to L2)
                NOT_TAKEN

  79            LOAD_FAST_BORROW         0 (now)
                LOAD_ATTR                4 (tzinfo)
                POP_JUMP_IF_NOT_NONE    33 (to L1)
                NOT_TAKEN

  80            LOAD_FAST_BORROW         0 (now)
                LOAD_ATTR                7 (replace + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                LOAD_CONST               1 (('tzinfo',))
                CALL_KW                  1
                RETURN_VALUE

  81    L1:     LOAD_FAST_BORROW         0 (now)
                LOAD_ATTR               13 (astimezone + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                CALL                     1
                RETURN_VALUE

  82    L2:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (now)
                LOAD_GLOBAL             14 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      117 (to L6)
                NOT_TAKEN

  83            NOP

  84    L3:     LOAD_GLOBAL              2 (datetime)
                LOAD_ATTR               16 (fromisoformat)
                PUSH_NULL
                LOAD_FAST_BORROW         0 (now)
                LOAD_ATTR                7 (replace + NULL|self)
                LOAD_CONST               2 ('Z')
                LOAD_CONST               3 ('+00:00')
                CALL                     2
                CALL                     1
                STORE_FAST               1 (dt)

  85            LOAD_FAST_BORROW         1 (dt)
                LOAD_ATTR                4 (tzinfo)
                POP_JUMP_IF_NOT_NONE    33 (to L4)
                NOT_TAKEN

  86            LOAD_FAST_BORROW         1 (dt)
                LOAD_ATTR                7 (replace + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                LOAD_CONST               1 (('tzinfo',))
                CALL_KW                  1
                STORE_FAST               1 (dt)

  87    L4:     LOAD_FAST_BORROW         1 (dt)
                LOAD_ATTR               13 (astimezone + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                CALL                     1
        L5:     RETURN_VALUE

  90    L6:     LOAD_GLOBAL              2 (datetime)
                LOAD_ATTR               20 (now)
                PUSH_NULL
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                CALL                     1
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

  88            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        4 (to L9)
                NOT_TAKEN
                POP_TOP

  89    L8:     POP_EXCEPT
                JUMP_BACKWARD_NO_INTERRUPT 49 (to L6)

  88    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L5 -> L7 [0]
  L7 to L8 -> L10 [1] lasti
  L9 to L10 -> L10 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "app\services\ingestion\pending_call_recovery.py", line 93>:
 93           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('dt')
              LOAD_CONST               2 ('datetime')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _iso at 0x0000018C18025E30, file "app\services\ingestion\pending_call_recovery.py", line 93>:
 93           RESUME                   0

 94           LOAD_FAST_BORROW         0 (dt)
              LOAD_ATTR                1 (isoformat + NULL|self)
              LOAD_CONST               0 ('seconds')
              LOAD_CONST               1 (('timespec',))
              CALL_KW                  1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025D30, file "app\services\ingestion\pending_call_recovery.py", line 97>:
 97           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('now_dt')
              LOAD_CONST               2 ('datetime')
              LOAD_CONST               3 ('ts_str')
              LOAD_CONST               4 ('Any')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('Optional[int]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _age_seconds at 0x0000018C17F0C960, file "app\services\ingestion\pending_call_recovery.py", line 97>:
  97            RESUME                   0

  98            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (ts_str)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (ts_str)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L2)
                NOT_TAKEN

  99    L1:     LOAD_CONST               0 (None)
                RETURN_VALUE

 100    L2:     NOP

 101    L3:     LOAD_GLOBAL              6 (datetime)
                LOAD_ATTR                8 (fromisoformat)
                PUSH_NULL
                LOAD_FAST_BORROW         1 (ts_str)
                LOAD_ATTR               11 (replace + NULL|self)
                LOAD_CONST               1 ('Z')
                LOAD_CONST               2 ('+00:00')
                CALL                     2
                CALL                     1
                STORE_FAST               2 (dt)

 104    L4:     LOAD_FAST                2 (dt)
                LOAD_ATTR               14 (tzinfo)
                POP_JUMP_IF_NOT_NONE    33 (to L5)
                NOT_TAKEN

 105            LOAD_FAST                2 (dt)
                LOAD_ATTR               11 (replace + NULL|self)
                LOAD_GLOBAL             16 (timezone)
                LOAD_ATTR               18 (utc)
                LOAD_CONST               3 (('tzinfo',))
                CALL_KW                  1
                STORE_FAST               2 (dt)

 106    L5:     LOAD_FAST_LOAD_FAST      2 (now_dt, dt)
                BINARY_OP               10 (-)
                STORE_FAST               3 (delta)

 107            LOAD_GLOBAL             21 (int + NULL)
                LOAD_FAST                3 (delta)
                LOAD_ATTR               23 (total_seconds + NULL|self)
                CALL                     0
                CALL                     1
                STORE_FAST               4 (secs)

 108            LOAD_FAST                4 (secs)
                LOAD_SMALL_INT           0
                COMPARE_OP             188 (bool(>=))
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN
                LOAD_FAST                4 (secs)
                RETURN_VALUE
        L6:     LOAD_SMALL_INT           0
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

 102            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L9)
                NOT_TAKEN
                POP_TOP

 103    L8:     POP_EXCEPT
                LOAD_CONST               0 (None)
                RETURN_VALUE

 102    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L7 [0]
  L7 to L8 -> L10 [1] lasti
  L9 to L10 -> L10 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024930, file "app\services\ingestion\pending_call_recovery.py", line 111>:
111           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('value')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('lo')
              LOAD_CONST               4 ('int')
              LOAD_CONST               5 ('hi')
              LOAD_CONST               4 ('int')
              LOAD_CONST               6 ('default')
              LOAD_CONST               4 ('int')
              LOAD_CONST               7 ('return')
              LOAD_CONST               4 ('int')
              BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _clamp at 0x0000018C18038B70, file "app\services\ingestion\pending_call_recovery.py", line 111>:
 111           RESUME                   0

 112           NOP

 113   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               4 (v)

 116   L2:     LOAD_FAST_LOAD_FAST     65 (v, lo)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 117           LOAD_FAST                1 (lo)
               RETURN_VALUE

 118   L3:     LOAD_FAST_LOAD_FAST     66 (v, hi)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN

 119           LOAD_FAST                2 (hi)
               RETURN_VALUE

 120   L4:     LOAD_FAST                4 (v)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 114           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L7)
               NOT_TAKEN
               POP_TOP

 115           LOAD_FAST                3 (default)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

 114   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object _get_db_safe at 0x0000018C17FF1230, file "app\services\ingestion\pending_call_recovery.py", line 123>:
 123           RESUME                   0

 124           NOP

 125   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('get_supabase',))
               IMPORT_NAME              0 (app.db.supabase_client)
               IMPORT_FROM              1 (get_supabase)
               STORE_FAST               0 (get_supabase)
               POP_TOP

 126           LOAD_FAST_BORROW         0 (get_supabase)
               PUSH_NULL
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 127           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       55 (to L7)
               NOT_TAKEN
               STORE_FAST               1 (e)

 128   L4:     LOAD_GLOBAL              6 (logger)
               LOAD_ATTR                9 (warning + NULL|self)

 129           LOAD_CONST               2 ('pending_call_recovery db client unavailable type=')

 130           LOAD_GLOBAL             11 (type + NULL)
               LOAD_FAST                1 (e)
               CALL                     1
               LOAD_ATTR               12 (__name__)
               FORMAT_SIMPLE

 129           BUILD_STRING             2

 128           CALL                     1
               POP_TOP

 132   L5:     POP_EXCEPT
               LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               LOAD_CONST               3 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               RERAISE                  1

 127   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "app\services\ingestion\pending_call_recovery.py", line 152>:
152           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('age_secs')
              LOAD_CONST               2 ('Optional[int]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _bucket_for at 0x0000018C17F96420, file "app\services\ingestion\pending_call_recovery.py", line 152>:
152           RESUME                   0

153           LOAD_FAST_BORROW         0 (age_secs)
              POP_JUMP_IF_NONE         8 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         0 (age_secs)
              LOAD_SMALL_INT           0
              COMPARE_OP              18 (bool(<))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

154   L1:     LOAD_CONST               1 ('unknown')
              RETURN_VALUE

155   L2:     LOAD_GLOBAL              0 (_AGE_BUCKETS)
              GET_ITER
      L3:     FOR_ITER                48 (to L8)
              UNPACK_SEQUENCE          3
              STORE_FAST_STORE_FAST   18 (label, lo)
              STORE_FAST               3 (hi)

156           LOAD_FAST_BORROW         3 (hi)
              POP_JUMP_IF_NOT_NONE    11 (to L4)
              NOT_TAKEN
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (age_secs, lo)
              COMPARE_OP             188 (bool(>=))
              POP_JUMP_IF_FALSE        5 (to L4)
              NOT_TAKEN

157           LOAD_FAST_BORROW         1 (label)
              SWAP                     2
              POP_TOP
              RETURN_VALUE

158   L4:     LOAD_FAST_BORROW         3 (hi)
              POP_JUMP_IF_NOT_NONE     3 (to L5)
              NOT_TAKEN
              JUMP_BACKWARD           26 (to L3)
      L5:     LOAD_FAST_LOAD_FAST     32 (lo, age_secs)
              SWAP                     2
              COPY                     2
              COMPARE_OP              58 (bool(<=))
              POP_JUMP_IF_FALSE       14 (to L7)
              NOT_TAKEN
              LOAD_FAST_BORROW         3 (hi)
              COMPARE_OP              18 (bool(<))
              POP_JUMP_IF_TRUE         3 (to L6)
              NOT_TAKEN
              JUMP_BACKWARD           42 (to L3)
      L6:     NOP

159           LOAD_FAST_BORROW         1 (label)
              SWAP                     2
              POP_TOP
              RETURN_VALUE

158   L7:     POP_TOP
              JUMP_BACKWARD           50 (to L3)

155   L8:     END_FOR
              POP_ITER

160           LOAD_CONST               1 ('unknown')
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025730, file "app\services\ingestion\pending_call_recovery.py", line 163>:
163           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

165           LOAD_CONST               2 ('Optional[str]')

163           LOAD_CONST               3 ('warnings')

166           LOAD_CONST               4 ('Optional[List[str]]')

163           LOAD_CONST               5 ('error_code')

167           LOAD_CONST               2 ('Optional[str]')

163           LOAD_CONST               6 ('return')

168           LOAD_CONST               7 ('Dict[str, Any]')

163           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object _empty_status_report at 0x0000018C180483B0, file "app\services\ingestion\pending_call_recovery.py", line 163>:
 163            RESUME                   0

 170            LOAD_CONST               0 ('status')
                LOAD_FAST_BORROW         2 (error_code)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                LOAD_CONST               1 ('ok')
                JUMP_FORWARD             1 (to L2)
        L1:     LOAD_CONST               2 ('skipped')

 171    L2:     LOAD_CONST               3 ('brokerage_id')
                LOAD_FAST                0 (brokerage_id)

 172            LOAD_CONST               4 ('total')
                LOAD_SMALL_INT           0

 173            LOAD_CONST               5 ('by_status')
                LOAD_GLOBAL              0 (_PENDING_STATUSES)
                GET_ITER
                LOAD_FAST_AND_CLEAR      3 (s)
                SWAP                     2
        L3:     BUILD_MAP                0
                SWAP                     2
        L4:     FOR_ITER                 5 (to L5)
                STORE_FAST_LOAD_FAST    51 (s, s)
                LOAD_SMALL_INT           0
                MAP_ADD                  2
                JUMP_BACKWARD            7 (to L4)
        L5:     END_FOR
                POP_ITER
        L6:     SWAP                     2
                STORE_FAST               3 (s)

 174            LOAD_CONST               6 ('by_age')
                LOAD_GLOBAL              2 (_AGE_BUCKETS)
                GET_ITER
                LOAD_FAST_AND_CLEAR      4 (b)
                SWAP                     2
        L7:     BUILD_MAP                0
                SWAP                     2
        L8:     FOR_ITER                12 (to L9)
                STORE_FAST_LOAD_FAST    68 (b, b)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                LOAD_SMALL_INT           0
                MAP_ADD                  2
                JUMP_BACKWARD           14 (to L8)
        L9:     END_FOR
                POP_ITER
       L10:     SWAP                     2
                STORE_FAST               4 (b)
                LOAD_CONST               7 ('unknown')
                LOAD_SMALL_INT           0
                BUILD_MAP                1
                BINARY_OP                7 (|)

 175            LOAD_CONST               8 ('oldest_age_seconds')
                LOAD_CONST               9 (None)

 176            LOAD_CONST              10 ('warnings')
                LOAD_GLOBAL              5 (list + NULL)
                LOAD_FAST                1 (warnings)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L11)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
       L11:     CALL                     1

 177            LOAD_CONST              11 ('error_code')
                LOAD_FAST_BORROW         2 (error_code)

 169            BUILD_MAP                8
                RETURN_VALUE

  --   L12:     SWAP                     2
                POP_TOP

 173            SWAP                     2
                STORE_FAST               3 (s)
                RERAISE                  0

  --   L13:     SWAP                     2
                POP_TOP

 174            SWAP                     2
                STORE_FAST               4 (b)
                RERAISE                  0
ExceptionTable:
  L3 to L6 -> L12 [9]
  L7 to L10 -> L13 [11]

Disassembly of <code object __annotate__ at 0x0000018C18025330, file "app\services\ingestion\pending_call_recovery.py", line 181>:
181           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

183           LOAD_CONST               2 ('Optional[str]')

181           LOAD_CONST               3 ('now')

184           LOAD_CONST               4 ('Any')

181           LOAD_CONST               5 ('return')

185           LOAD_CONST               6 ('Dict[str, Any]')

181           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object queue_status_report at 0x0000018C17EDA850, file "app\services\ingestion\pending_call_recovery.py", line 181>:
 181            RESUME                   0

 200            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       39 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L1)
                NOT_TAKEN

 199            LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                JUMP_FORWARD             1 (to L2)

 201    L1:     LOAD_CONST               1 (None)

 198    L2:     STORE_FAST               2 (bid)

 203            LOAD_GLOBAL              7 (_now_dt + NULL)
                LOAD_FAST_BORROW         1 (now)
                CALL                     1
                STORE_FAST               3 (now_dt)

 205            LOAD_GLOBAL              9 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               4 (db)

 206            LOAD_FAST_BORROW         4 (db)
                POP_JUMP_IF_NOT_NONE    16 (to L3)
                NOT_TAKEN

 207            LOAD_GLOBAL             11 (_empty_status_report + NULL)

 208            LOAD_FAST_BORROW         2 (bid)

 209            LOAD_CONST               2 ('pending_call_queue_store_unavailable')
                BUILD_LIST               1

 210            LOAD_CONST               2 ('pending_call_queue_store_unavailable')

 207            LOAD_CONST               3 (('brokerage_id', 'warnings', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 213    L3:     NOP

 218    L4:     LOAD_FAST_BORROW         4 (db)
                LOAD_ATTR               13 (table + NULL|self)
                LOAD_GLOBAL             14 (_TABLE)
                CALL                     1

 219            LOAD_ATTR               17 (select + NULL|self)

 220            LOAD_CONST               4 ('brokerage_id, source, status, created_at, locked_at')

 219            CALL                     1

 223            LOAD_ATTR               19 (limit + NULL|self)
                LOAD_GLOBAL             20 (_LIST_HARD_CAP)
                CALL                     1

 217            STORE_FAST               5 (query)

 225            LOAD_FAST_BORROW         2 (bid)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L7)
        L5:     NOT_TAKEN

 226    L6:     LOAD_FAST_BORROW         5 (query)
                LOAD_ATTR               23 (eq + NULL|self)
                LOAD_CONST               5 ('brokerage_id')
                LOAD_FAST_BORROW         2 (bid)
                CALL                     2
                STORE_FAST               5 (query)

 227    L7:     LOAD_FAST_BORROW         5 (query)
                LOAD_ATTR               25 (execute + NULL|self)
                CALL                     0
                STORE_FAST               6 (result)

 228            LOAD_GLOBAL             27 (list + NULL)
                LOAD_GLOBAL             29 (getattr + NULL)
                LOAD_FAST_BORROW         6 (result)
                LOAD_CONST               6 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
        L8:     NOT_TAKEN
        L9:     POP_TOP
                BUILD_LIST               0
       L10:     CALL                     1
                STORE_FAST               7 (rows)

 239   L11:     LOAD_GLOBAL             40 (_PENDING_STATUSES)
                GET_ITER
                LOAD_FAST_AND_CLEAR      9 (s)
                SWAP                     2
       L12:     BUILD_MAP                0
                SWAP                     2
       L13:     FOR_ITER                 5 (to L14)
                STORE_FAST_LOAD_FAST   153 (s, s)
                LOAD_SMALL_INT           0
                MAP_ADD                  2
                JUMP_BACKWARD            7 (to L13)
       L14:     END_FOR
                POP_ITER
       L15:     STORE_FAST              10 (by_status)
                STORE_FAST               9 (s)

 240            LOAD_GLOBAL             42 (_AGE_BUCKETS)
                GET_ITER
                LOAD_FAST_AND_CLEAR     11 (b)
                SWAP                     2
       L16:     BUILD_MAP                0
                SWAP                     2
       L17:     FOR_ITER                12 (to L18)
                STORE_FAST_LOAD_FAST   187 (b, b)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                LOAD_SMALL_INT           0
                MAP_ADD                  2
                JUMP_BACKWARD           14 (to L17)
       L18:     END_FOR
                POP_ITER
       L19:     STORE_FAST              12 (by_age)
                STORE_FAST              11 (b)

 241            LOAD_SMALL_INT           0
                LOAD_FAST               12 (by_age)
                LOAD_CONST               9 ('unknown')
                STORE_SUBSCR

 242            LOAD_CONST               1 (None)
                STORE_FAST              13 (oldest_age)

 244            LOAD_FAST                7 (rows)
                GET_ITER
       L20:     FOR_ITER               193 (to L27)
                STORE_FAST              14 (row)

 245            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST               14 (row)
                LOAD_GLOBAL             44 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L21)
                NOT_TAKEN

 246            JUMP_BACKWARD           27 (to L20)

 247   L21:     LOAD_FAST               14 (row)
                LOAD_ATTR               47 (get + NULL|self)
                LOAD_CONST              10 ('status')
                CALL                     1
                LOAD_GLOBAL             40 (_PENDING_STATUSES)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       18 (to L22)
                NOT_TAKEN
                LOAD_FAST               14 (row)
                LOAD_ATTR               47 (get + NULL|self)
                LOAD_CONST              10 ('status')
                CALL                     1
                JUMP_FORWARD             1 (to L23)
       L22:     LOAD_CONST               1 (None)
       L23:     STORE_FAST              15 (status)

 248            LOAD_FAST               15 (status)
                TO_BOOL
                POP_JUMP_IF_FALSE       28 (to L24)
                NOT_TAKEN

 249            LOAD_FAST               10 (by_status)
                LOAD_ATTR               47 (get + NULL|self)
                LOAD_FAST               15 (status)
                LOAD_SMALL_INT           0
                CALL                     2
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_FAST_LOAD_FAST    175 (by_status, status)
                STORE_SUBSCR

 251   L24:     LOAD_GLOBAL             49 (_age_seconds + NULL)
                LOAD_FAST_LOAD_FAST     62 (now_dt, row)
                LOAD_ATTR               47 (get + NULL|self)
                LOAD_CONST              11 ('created_at')
                CALL                     1
                CALL                     2
                STORE_FAST              16 (age)

 252            LOAD_GLOBAL             51 (_bucket_for + NULL)
                LOAD_FAST               16 (age)
                CALL                     1
                STORE_FAST              17 (bucket)

 253            LOAD_FAST               12 (by_age)
                LOAD_ATTR               47 (get + NULL|self)
                LOAD_FAST               17 (bucket)
                LOAD_SMALL_INT           0
                CALL                     2
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_FAST               12 (by_age)
                LOAD_FAST               17 (bucket)
                STORE_SUBSCR

 254            LOAD_FAST               16 (age)
                POP_JUMP_IF_NOT_NONE     3 (to L25)
                NOT_TAKEN
                JUMP_BACKWARD          178 (to L20)
       L25:     LOAD_FAST               13 (oldest_age)
                POP_JUMP_IF_NONE        10 (to L26)
                NOT_TAKEN
                LOAD_FAST               16 (age)
                LOAD_FAST               13 (oldest_age)
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_TRUE         3 (to L26)
                NOT_TAKEN
                JUMP_BACKWARD          191 (to L20)

 255   L26:     LOAD_FAST               16 (age)
                STORE_FAST              13 (oldest_age)
                JUMP_BACKWARD          195 (to L20)

 244   L27:     END_FOR
                POP_ITER

 258            LOAD_CONST              10 ('status')
                LOAD_CONST              12 ('ok')

 259            LOAD_CONST               5 ('brokerage_id')
                LOAD_FAST                2 (bid)

 260            LOAD_CONST              13 ('total')
                LOAD_GLOBAL             53 (len + NULL)
                LOAD_FAST                7 (rows)
                CALL                     1

 261            LOAD_CONST              14 ('by_status')
                LOAD_FAST               10 (by_status)

 262            LOAD_CONST              15 ('by_age')
                LOAD_FAST               12 (by_age)

 263            LOAD_CONST              16 ('oldest_age_seconds')
                LOAD_FAST               13 (oldest_age)

 264            LOAD_CONST              17 ('warnings')
                BUILD_LIST               0

 265            LOAD_CONST              18 ('error_code')
                LOAD_CONST               1 (None)

 257            BUILD_MAP                8
                RETURN_VALUE

  --   L28:     PUSH_EXC_INFO

 229            LOAD_GLOBAL             30 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      113 (to L33)
                NOT_TAKEN
                STORE_FAST               8 (e)

 230   L29:     LOAD_GLOBAL             32 (logger)
                LOAD_ATTR               35 (warning + NULL|self)

 231            LOAD_CONST               7 ('queue_status_report db error type=')
                LOAD_GLOBAL             37 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               38 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 230            CALL                     1
                POP_TOP

 233            LOAD_GLOBAL             11 (_empty_status_report + NULL)

 234            LOAD_FAST                2 (bid)

 235            LOAD_CONST               8 ('db_read_failed:')
                LOAD_GLOBAL             37 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               38 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 236            LOAD_CONST               8 ('db_read_failed:')
                LOAD_GLOBAL             37 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               38 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 233            LOAD_CONST               3 (('brokerage_id', 'warnings', 'error_code'))
                CALL_KW                  3
       L30:     SWAP                     2
       L31:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RETURN_VALUE

  --   L32:     LOAD_CONST               1 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RERAISE                  1

 229   L33:     RERAISE                  0

  --   L34:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L35:     SWAP                     2
                POP_TOP

 239            SWAP                     2
                STORE_FAST               9 (s)
                RERAISE                  0

  --   L36:     SWAP                     2
                POP_TOP

 240            SWAP                     2
                STORE_FAST              11 (b)
                RERAISE                  0
ExceptionTable:
  L4 to L5 -> L28 [0]
  L6 to L8 -> L28 [0]
  L9 to L11 -> L28 [0]
  L12 to L15 -> L35 [2]
  L16 to L19 -> L36 [2]
  L28 to L29 -> L34 [1] lasti
  L29 to L30 -> L32 [1] lasti
  L30 to L31 -> L34 [1] lasti
  L32 to L34 -> L34 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "app\services\ingestion\pending_call_recovery.py", line 273>:
273           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

275           LOAD_CONST               2 ('Optional[str]')

273           LOAD_CONST               3 ('stale_after_seconds')

276           LOAD_CONST               4 ('int')

273           LOAD_CONST               5 ('limit')

277           LOAD_CONST               4 ('int')

273           LOAD_CONST               6 ('now')

278           LOAD_CONST               7 ('Any')

273           LOAD_CONST               8 ('return')

279           LOAD_CONST               9 ('Dict[str, Any]')

273           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object detect_stale_dialing_rows at 0x0000018C17ED26C0, file "app\services\ingestion\pending_call_recovery.py", line 273>:
 273            RESUME                   0

 291            LOAD_GLOBAL              1 (_clamp + NULL)

 292            LOAD_FAST_BORROW         1 (stale_after_seconds)
                LOAD_SMALL_INT          60
                LOAD_CONST              26 (86400)

 293            LOAD_GLOBAL              2 (DEFAULT_STALE_AFTER_SECONDS)

 291            CALL                     4
                STORE_FAST               4 (threshold_secs)

 295            LOAD_GLOBAL              1 (_clamp + NULL)
                LOAD_FAST_BORROW         2 (limit)
                LOAD_SMALL_INT           1
                LOAD_GLOBAL              4 (_LIST_HARD_CAP)
                LOAD_SMALL_INT         200
                CALL                     4
                STORE_FAST               5 (capped_limit)

 298            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_GLOBAL              8 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       39 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR               11 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L1)
                NOT_TAKEN

 297            LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR               11 (strip + NULL|self)
                CALL                     0
                JUMP_FORWARD             1 (to L2)

 299    L1:     LOAD_CONST               1 (None)

 296    L2:     STORE_FAST               6 (bid)

 301            LOAD_GLOBAL             13 (_now_dt + NULL)
                LOAD_FAST_BORROW         3 (now)
                CALL                     1
                STORE_FAST               7 (now_dt)

 302            LOAD_GLOBAL             15 (_iso + NULL)
                LOAD_FAST_BORROW         7 (now_dt)
                LOAD_GLOBAL             17 (timedelta + NULL)
                LOAD_FAST_BORROW         4 (threshold_secs)
                LOAD_CONST               2 (('seconds',))
                CALL_KW                  1
                BINARY_OP               10 (-)
                CALL                     1
                STORE_FAST               8 (cutoff_iso)

 304            LOAD_GLOBAL             19 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               9 (db)

 305            LOAD_FAST_BORROW         9 (db)
                POP_JUMP_IF_NOT_NONE    20 (to L3)
                NOT_TAKEN

 307            LOAD_CONST               3 ('status')
                LOAD_CONST               4 ('skipped')

 308            LOAD_CONST               5 ('brokerage_id')
                LOAD_FAST_BORROW         6 (bid)

 309            LOAD_CONST               6 ('stale_after_seconds')
                LOAD_FAST_BORROW         4 (threshold_secs)

 310            LOAD_CONST               7 ('limit')
                LOAD_FAST_BORROW         5 (capped_limit)

 311            LOAD_CONST               8 ('count')
                LOAD_SMALL_INT           0

 312            LOAD_CONST               9 ('rows')
                BUILD_LIST               0

 313            LOAD_CONST              10 ('warnings')
                LOAD_CONST              11 ('pending_call_queue_store_unavailable')
                BUILD_LIST               1

 314            LOAD_CONST              12 ('error_code')
                LOAD_CONST              11 ('pending_call_queue_store_unavailable')

 306            BUILD_MAP                8
                RETURN_VALUE

 317    L3:     NOP

 319    L4:     LOAD_FAST_BORROW         9 (db)
                LOAD_ATTR               21 (table + NULL|self)
                LOAD_GLOBAL             22 (_TABLE)
                CALL                     1

 320            LOAD_ATTR               25 (select + NULL|self)

 321            LOAD_CONST              13 ('pending_call_id, brokerage_id, source, locked_by, locked_at')

 320            CALL                     1

 324            LOAD_ATTR               27 (eq + NULL|self)
                LOAD_CONST               3 ('status')
                LOAD_CONST              14 ('DIALING')
                CALL                     2

 325            LOAD_ATTR               29 (lt + NULL|self)
                LOAD_CONST              15 ('locked_at')
                LOAD_FAST_BORROW         8 (cutoff_iso)
                CALL                     2

 326            LOAD_ATTR               31 (order + NULL|self)
                LOAD_CONST              15 ('locked_at')
                LOAD_CONST              16 (False)
                LOAD_CONST              17 (('desc',))
                CALL_KW                  2

 327            LOAD_ATTR               33 (limit + NULL|self)
                LOAD_FAST_BORROW         5 (capped_limit)
                CALL                     1

 318            STORE_FAST              10 (query)

 329            LOAD_FAST_BORROW         6 (bid)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L7)
        L5:     NOT_TAKEN

 330    L6:     LOAD_FAST_BORROW        10 (query)
                LOAD_ATTR               27 (eq + NULL|self)
                LOAD_CONST               5 ('brokerage_id')
                LOAD_FAST_BORROW         6 (bid)
                CALL                     2
                STORE_FAST              10 (query)

 331    L7:     LOAD_FAST_BORROW        10 (query)
                LOAD_ATTR               35 (execute + NULL|self)
                CALL                     0
                STORE_FAST              11 (result)

 332            LOAD_GLOBAL             37 (list + NULL)
                LOAD_GLOBAL             39 (getattr + NULL)
                LOAD_FAST_BORROW        11 (result)
                LOAD_CONST              18 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
        L8:     NOT_TAKEN
        L9:     POP_TOP
                BUILD_LIST               0
       L10:     CALL                     1
                STORE_FAST              12 (rows)

 348   L11:     BUILD_LIST               0
                STORE_FAST              14 (enriched)

 349            LOAD_FAST               12 (rows)
                GET_ITER
       L12:     FOR_ITER               157 (to L14)
                STORE_FAST              15 (row)

 350            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST               15 (row)
                LOAD_GLOBAL             50 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
                NOT_TAKEN

 351            JUMP_BACKWARD           27 (to L12)

 352   L13:     LOAD_GLOBAL             53 (_age_seconds + NULL)
                LOAD_FAST_LOAD_FAST    127 (now_dt, row)
                LOAD_ATTR               55 (get + NULL|self)
                LOAD_CONST              15 ('locked_at')
                CALL                     1
                CALL                     2
                STORE_FAST              16 (age)

 353            LOAD_FAST               14 (enriched)
                LOAD_ATTR               57 (append + NULL|self)

 354            LOAD_CONST              21 ('pending_call_id')
                LOAD_FAST               15 (row)
                LOAD_ATTR               55 (get + NULL|self)
                LOAD_CONST              21 ('pending_call_id')
                CALL                     1

 355            LOAD_CONST               5 ('brokerage_id')
                LOAD_FAST               15 (row)
                LOAD_ATTR               55 (get + NULL|self)
                LOAD_CONST               5 ('brokerage_id')
                CALL                     1

 356            LOAD_CONST              22 ('source')
                LOAD_FAST               15 (row)
                LOAD_ATTR               55 (get + NULL|self)
                LOAD_CONST              22 ('source')
                CALL                     1

 357            LOAD_CONST              23 ('locked_by')
                LOAD_FAST               15 (row)
                LOAD_ATTR               55 (get + NULL|self)
                LOAD_CONST              23 ('locked_by')
                CALL                     1

 358            LOAD_CONST              15 ('locked_at')
                LOAD_FAST               15 (row)
                LOAD_ATTR               55 (get + NULL|self)
                LOAD_CONST              15 ('locked_at')
                CALL                     1

 359            LOAD_CONST              24 ('age_seconds')
                LOAD_FAST               16 (age)

 353            BUILD_MAP                6
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          159 (to L12)

 349   L14:     END_FOR
                POP_ITER

 363            LOAD_CONST               3 ('status')
                LOAD_CONST              25 ('ok')

 364            LOAD_CONST               5 ('brokerage_id')
                LOAD_FAST                6 (bid)

 365            LOAD_CONST               6 ('stale_after_seconds')
                LOAD_FAST                4 (threshold_secs)

 366            LOAD_CONST               7 ('limit')
                LOAD_FAST                5 (capped_limit)

 367            LOAD_CONST               8 ('count')
                LOAD_GLOBAL             59 (len + NULL)
                LOAD_FAST               14 (enriched)
                CALL                     1

 368            LOAD_CONST               9 ('rows')
                LOAD_FAST               14 (enriched)

 369            LOAD_CONST              10 ('warnings')
                BUILD_LIST               0

 370            LOAD_CONST              12 ('error_code')
                LOAD_CONST               1 (None)

 362            BUILD_MAP                8
                RETURN_VALUE

  --   L15:     PUSH_EXC_INFO

 333            LOAD_GLOBAL             40 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      117 (to L20)
                NOT_TAKEN
                STORE_FAST              13 (e)

 334   L16:     LOAD_GLOBAL             42 (logger)
                LOAD_ATTR               45 (warning + NULL|self)

 335            LOAD_CONST              19 ('detect_stale_dialing_rows db error type=')
                LOAD_GLOBAL             47 (type + NULL)
                LOAD_FAST               13 (e)
                CALL                     1
                LOAD_ATTR               48 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 334            CALL                     1
                POP_TOP

 338            LOAD_CONST               3 ('status')
                LOAD_CONST               4 ('skipped')

 339            LOAD_CONST               5 ('brokerage_id')
                LOAD_FAST                6 (bid)

 340            LOAD_CONST               6 ('stale_after_seconds')
                LOAD_FAST                4 (threshold_secs)

 341            LOAD_CONST               7 ('limit')
                LOAD_FAST                5 (capped_limit)

 342            LOAD_CONST               8 ('count')
                LOAD_SMALL_INT           0

 343            LOAD_CONST               9 ('rows')
                BUILD_LIST               0

 344            LOAD_CONST              10 ('warnings')
                LOAD_CONST              20 ('db_read_failed:')
                LOAD_GLOBAL             47 (type + NULL)
                LOAD_FAST               13 (e)
                CALL                     1
                LOAD_ATTR               48 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 345            LOAD_CONST              12 ('error_code')
                LOAD_CONST              20 ('db_read_failed:')
                LOAD_GLOBAL             47 (type + NULL)
                LOAD_FAST               13 (e)
                CALL                     1
                LOAD_ATTR               48 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 337            BUILD_MAP                8
       L17:     SWAP                     2
       L18:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              13 (e)
                DELETE_FAST             13 (e)
                RETURN_VALUE

  --   L19:     LOAD_CONST               1 (None)
                STORE_FAST              13 (e)
                DELETE_FAST             13 (e)
                RERAISE                  1

 333   L20:     RERAISE                  0

  --   L21:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L4 to L5 -> L15 [0]
  L6 to L8 -> L15 [0]
  L9 to L11 -> L15 [0]
  L15 to L16 -> L21 [1] lasti
  L16 to L17 -> L19 [1] lasti
  L17 to L18 -> L21 [1] lasti
  L19 to L21 -> L21 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18090140, file "app\services\ingestion\pending_call_recovery.py", line 378>:
378           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

380           LOAD_CONST               2 ('Optional[str]')

378           LOAD_CONST               3 ('stale_after_seconds')

381           LOAD_CONST               4 ('int')

378           LOAD_CONST               5 ('limit')

382           LOAD_CONST               4 ('int')

378           LOAD_CONST               6 ('now')

383           LOAD_CONST               7 ('Any')

378           LOAD_CONST               8 ('dry_run')

384           LOAD_CONST               9 ('bool')

378           LOAD_CONST              10 ('worker_id_hint')

385           LOAD_CONST               2 ('Optional[str]')

378           LOAD_CONST              11 ('return')

386           LOAD_CONST              12 ('Dict[str, Any]')

378           BUILD_MAP                7
              RETURN_VALUE

Disassembly of <code object recover_stale_dialing_rows at 0x0000018C17F78810, file "app\services\ingestion\pending_call_recovery.py", line 378>:
 378            RESUME                   0

 413            LOAD_GLOBAL              1 (_clamp + NULL)

 414            LOAD_FAST_BORROW         1 (stale_after_seconds)
                LOAD_SMALL_INT          60
                LOAD_CONST              35 (86400)

 415            LOAD_GLOBAL              2 (DEFAULT_STALE_AFTER_SECONDS)

 413            CALL                     4
                STORE_FAST               6 (threshold_secs)

 417            LOAD_GLOBAL              1 (_clamp + NULL)
                LOAD_FAST_BORROW         2 (limit)
                LOAD_SMALL_INT           1
                LOAD_GLOBAL              4 (_RECOVER_HARD_CAP)
                LOAD_SMALL_INT          50
                CALL                     4
                STORE_FAST               7 (capped_limit)

 420            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_GLOBAL              8 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       39 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR               11 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L1)
                NOT_TAKEN

 419            LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR               11 (strip + NULL|self)
                CALL                     0
                JUMP_FORWARD             1 (to L2)

 421    L1:     LOAD_CONST               1 (None)

 418    L2:     STORE_FAST               8 (bid)

 425            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW         5 (worker_id_hint)
                LOAD_GLOBAL              8 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       39 (to L3)
                NOT_TAKEN
                LOAD_FAST_BORROW         5 (worker_id_hint)
                LOAD_ATTR               11 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L3)
                NOT_TAKEN

 424            LOAD_FAST_BORROW         5 (worker_id_hint)
                LOAD_ATTR               11 (strip + NULL|self)
                CALL                     0
                JUMP_FORWARD             1 (to L4)

 426    L3:     LOAD_CONST               2 ('pas170-recovery')

 423    L4:     STORE_FAST               9 (worker_hint)

 428            LOAD_GLOBAL             13 (detect_stale_dialing_rows + NULL)

 429            LOAD_FAST_BORROW         8 (bid)

 430            LOAD_FAST_BORROW         6 (threshold_secs)

 431            LOAD_FAST_BORROW         7 (capped_limit)

 432            LOAD_FAST_BORROW         3 (now)

 428            LOAD_CONST               3 (('brokerage_id', 'stale_after_seconds', 'limit', 'now'))
                CALL_KW                  4
                STORE_FAST              10 (detection)

 434            LOAD_FAST_BORROW        10 (detection)
                LOAD_CONST               4 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               5 ('ok')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       84 (to L8)
                NOT_TAKEN

 436            LOAD_CONST               4 ('status')
                LOAD_CONST               6 ('skipped')

 437            LOAD_CONST               7 ('mode')
                LOAD_FAST_BORROW         4 (dry_run)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN
                LOAD_CONST               8 ('execute')
                JUMP_FORWARD             1 (to L6)
        L5:     LOAD_CONST               9 ('dry-run')

 438    L6:     LOAD_CONST              10 ('brokerage_id')
                LOAD_FAST                8 (bid)

 439            LOAD_CONST              11 ('stale_after_seconds')
                LOAD_FAST                6 (threshold_secs)

 440            LOAD_CONST              12 ('limit')
                LOAD_FAST                7 (capped_limit)

 441            LOAD_CONST              13 ('candidate_count')
                LOAD_SMALL_INT           0

 442            LOAD_CONST              14 ('recovered_count')
                LOAD_SMALL_INT           0

 443            LOAD_CONST              15 ('skipped_count')
                LOAD_SMALL_INT           0

 444            LOAD_CONST              16 ('failed_count')
                LOAD_SMALL_INT           0

 445            LOAD_CONST              17 ('warnings')
                LOAD_GLOBAL             15 (list + NULL)
                LOAD_FAST_BORROW        10 (detection)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              17 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
        L7:     CALL                     1

 446            LOAD_CONST              18 ('error_code')
                LOAD_FAST_BORROW        10 (detection)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              18 ('error_code')
                CALL                     1

 435            BUILD_MAP               11
                RETURN_VALUE

 448    L8:     LOAD_FAST_BORROW        10 (detection)
                LOAD_CONST              19 ('rows')
                BINARY_OP               26 ([])
                STORE_FAST              11 (candidates)

 449            LOAD_GLOBAL             19 (len + NULL)
                LOAD_FAST_BORROW        11 (candidates)
                CALL                     1
                STORE_FAST              12 (candidate_count)

 451            LOAD_FAST_BORROW         4 (dry_run)
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L9)
                NOT_TAKEN

 453            LOAD_CONST               4 ('status')
                LOAD_CONST               5 ('ok')

 454            LOAD_CONST               7 ('mode')
                LOAD_CONST               9 ('dry-run')

 455            LOAD_CONST              10 ('brokerage_id')
                LOAD_FAST_BORROW         8 (bid)

 456            LOAD_CONST              11 ('stale_after_seconds')
                LOAD_FAST_BORROW         6 (threshold_secs)

 457            LOAD_CONST              12 ('limit')
                LOAD_FAST_BORROW         7 (capped_limit)

 458            LOAD_CONST              13 ('candidate_count')
                LOAD_FAST_BORROW        12 (candidate_count)

 459            LOAD_CONST              14 ('recovered_count')
                LOAD_SMALL_INT           0

 460            LOAD_CONST              15 ('skipped_count')
                LOAD_SMALL_INT           0

 461            LOAD_CONST              16 ('failed_count')
                LOAD_SMALL_INT           0

 462            LOAD_CONST              17 ('warnings')
                BUILD_LIST               0

 463            LOAD_CONST              18 ('error_code')
                LOAD_CONST               1 (None)

 452            BUILD_MAP               11
                RETURN_VALUE

 466    L9:     LOAD_GLOBAL             21 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST              13 (db)

 467            LOAD_FAST_BORROW        13 (db)
                POP_JUMP_IF_NOT_NONE    26 (to L10)
                NOT_TAKEN

 469            LOAD_CONST               4 ('status')
                LOAD_CONST               6 ('skipped')

 470            LOAD_CONST               7 ('mode')
                LOAD_CONST               8 ('execute')

 471            LOAD_CONST              10 ('brokerage_id')
                LOAD_FAST_BORROW         8 (bid)

 472            LOAD_CONST              11 ('stale_after_seconds')
                LOAD_FAST_BORROW         6 (threshold_secs)

 473            LOAD_CONST              12 ('limit')
                LOAD_FAST_BORROW         7 (capped_limit)

 474            LOAD_CONST              13 ('candidate_count')
                LOAD_FAST_BORROW        12 (candidate_count)

 475            LOAD_CONST              14 ('recovered_count')
                LOAD_SMALL_INT           0

 476            LOAD_CONST              15 ('skipped_count')
                LOAD_SMALL_INT           0

 477            LOAD_CONST              16 ('failed_count')
                LOAD_SMALL_INT           0

 478            LOAD_CONST              17 ('warnings')
                LOAD_CONST              20 ('pending_call_queue_store_unavailable')
                BUILD_LIST               1

 479            LOAD_CONST              18 ('error_code')
                LOAD_CONST              20 ('pending_call_queue_store_unavailable')

 468            BUILD_MAP               11
                RETURN_VALUE

 482   L10:     LOAD_SMALL_INT           0
                STORE_FAST              14 (recovered)

 483            LOAD_SMALL_INT           0
                STORE_FAST              15 (skipped)

 484            LOAD_SMALL_INT           0
                STORE_FAST              16 (failed)

 485            BUILD_LIST               0
                STORE_FAST              17 (warnings)

 487            LOAD_FAST_BORROW        11 (candidates)
                GET_ITER
       L11:     EXTENDED_ARG             1
                FOR_ITER               316 (to L22)
                STORE_FAST              18 (row)

 488            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW        18 (row)
                LOAD_GLOBAL             22 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        12 (to L12)
                NOT_TAKEN

 489            LOAD_FAST_BORROW        15 (skipped)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST              15 (skipped)

 490            JUMP_BACKWARD           37 (to L11)

 491   L12:     LOAD_FAST_BORROW        18 (row)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              21 ('pending_call_id')
                CALL                     1
                STORE_FAST              19 (pending_call_id)

 492            LOAD_FAST_BORROW        18 (row)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              10 ('brokerage_id')
                CALL                     1
                STORE_FAST              20 (row_bid)

 493            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW        19 (pending_call_id)
                LOAD_GLOBAL              8 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L13)
                NOT_TAKEN
                LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW        20 (row_bid)
                LOAD_GLOBAL              8 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        12 (to L14)
                NOT_TAKEN

 494   L13:     LOAD_FAST_BORROW        15 (skipped)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST              15 (skipped)

 495            JUMP_BACKWARD          126 (to L11)

 501   L14:     LOAD_CONST               4 ('status')
                LOAD_CONST              22 ('PENDING')

 502            LOAD_CONST              23 ('locked_at')
                LOAD_CONST               1 (None)

 503            LOAD_CONST              24 ('locked_by')
                LOAD_CONST               1 (None)

 504            LOAD_CONST              25 ('last_error_code')
                LOAD_CONST              26 ('pas170_recovered_from_stale_dialing')

 505            LOAD_CONST              27 ('last_error_at')
                LOAD_GLOBAL             25 (_iso + NULL)
                LOAD_GLOBAL             27 (_now_dt + NULL)
                LOAD_FAST_BORROW         3 (now)
                CALL                     1
                CALL                     1

 500            BUILD_MAP                5
                STORE_FAST              21 (patch)

 507            NOP

 509   L15:     LOAD_FAST_BORROW        13 (db)
                LOAD_ATTR               29 (table + NULL|self)
                LOAD_GLOBAL             30 (_TABLE)
                CALL                     1

 510            LOAD_ATTR               33 (update + NULL|self)
                LOAD_FAST_BORROW        21 (patch)
                CALL                     1

 511            LOAD_ATTR               35 (eq + NULL|self)
                LOAD_CONST              21 ('pending_call_id')
                LOAD_FAST_BORROW        19 (pending_call_id)
                CALL                     2

 512            LOAD_ATTR               35 (eq + NULL|self)
                LOAD_CONST              10 ('brokerage_id')
                LOAD_FAST_BORROW        20 (row_bid)
                CALL                     2

 513            LOAD_ATTR               35 (eq + NULL|self)
                LOAD_CONST               4 ('status')
                LOAD_CONST              28 ('DIALING')
                CALL                     2

 514            LOAD_ATTR               37 (execute + NULL|self)
                CALL                     0

 508            STORE_FAST              22 (update_result)

 516            LOAD_GLOBAL             15 (list + NULL)
                LOAD_GLOBAL             39 (getattr + NULL)
                LOAD_FAST_BORROW        22 (update_result)
                LOAD_CONST              29 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L16)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
       L16:     CALL                     1
                STORE_FAST              23 (updated_rows)

 517            LOAD_FAST_BORROW        23 (updated_rows)
                TO_BOOL
                POP_JUMP_IF_FALSE       13 (to L20)
       L17:     NOT_TAKEN

 518   L18:     LOAD_FAST_BORROW        14 (recovered)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST              14 (recovered)
       L19:     EXTENDED_ARG             1
                JUMP_BACKWARD          307 (to L11)

 523   L20:     LOAD_FAST_BORROW        15 (skipped)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST              15 (skipped)
       L21:     EXTENDED_ARG             1
                JUMP_BACKWARD          319 (to L11)

 487   L22:     END_FOR
                POP_ITER

 534            LOAD_FAST_BORROW        16 (failed)
                LOAD_SMALL_INT           0
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L23)
                NOT_TAKEN
                LOAD_CONST               5 ('ok')
                JUMP_FORWARD             1 (to L24)
       L23:     LOAD_CONST              33 ('failed')
       L24:     STORE_FAST              26 (status)

 536            LOAD_CONST               4 ('status')
                LOAD_FAST               26 (status)

 537            LOAD_CONST               7 ('mode')
                LOAD_CONST               8 ('execute')

 538            LOAD_CONST              10 ('brokerage_id')
                LOAD_FAST                8 (bid)

 539            LOAD_CONST              11 ('stale_after_seconds')
                LOAD_FAST                6 (threshold_secs)

 540            LOAD_CONST              12 ('limit')
                LOAD_FAST                7 (capped_limit)

 541            LOAD_CONST              13 ('candidate_count')
                LOAD_FAST               12 (candidate_count)

 542            LOAD_CONST              14 ('recovered_count')
                LOAD_FAST               14 (recovered)

 543            LOAD_CONST              15 ('skipped_count')
                LOAD_FAST               15 (skipped)

 544            LOAD_CONST              16 ('failed_count')
                LOAD_FAST               16 (failed)

 545            LOAD_CONST              17 ('warnings')
                LOAD_FAST               17 (warnings)

 546            LOAD_CONST              18 ('error_code')
                LOAD_FAST_BORROW        26 (status)
                LOAD_CONST               5 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        4 (to L25)
                NOT_TAKEN
                LOAD_CONST               1 (None)

 535            BUILD_MAP               11
                RETURN_VALUE

 546   L25:     LOAD_CONST              34 ('stale_recovery_partial_failure')

 535            BUILD_MAP               11
                RETURN_VALUE

  --   L26:     PUSH_EXC_INFO

 524            LOAD_GLOBAL             40 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      116 (to L31)
                NOT_TAKEN
                STORE_FAST              24 (e)

 525   L27:     LOAD_FAST               16 (failed)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST              16 (failed)

 526            LOAD_CONST              30 ('db_write_failed:')
                LOAD_GLOBAL             43 (type + NULL)
                LOAD_FAST               24 (e)
                CALL                     1
                LOAD_ATTR               44 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                STORE_FAST              25 (code)

 527            LOAD_FAST               25 (code)
                LOAD_FAST               17 (warnings)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       18 (to L28)
                NOT_TAKEN

 528            LOAD_FAST               17 (warnings)
                LOAD_ATTR               47 (append + NULL|self)
                LOAD_FAST               25 (code)
                CALL                     1
                POP_TOP

 529   L28:     LOAD_GLOBAL             48 (logger)
                LOAD_ATTR               51 (warning + NULL|self)

 530            LOAD_CONST              31 ('recover_stale_dialing_rows update error id=')

 531            LOAD_FAST               19 (pending_call_id)
                FORMAT_SIMPLE
                LOAD_CONST              32 (' type=')
                LOAD_GLOBAL             43 (type + NULL)
                LOAD_FAST               24 (e)
                CALL                     1
                LOAD_ATTR               44 (__name__)
                FORMAT_SIMPLE

 530            BUILD_STRING             4

 529            CALL                     1
                POP_TOP
       L29:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              24 (e)
                DELETE_FAST             24 (e)
                EXTENDED_ARG             1
                JUMP_BACKWARD          487 (to L11)

  --   L30:     LOAD_CONST               1 (None)
                STORE_FAST              24 (e)
                DELETE_FAST             24 (e)
                RERAISE                  1

 524   L31:     RERAISE                  0

  --   L32:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L15 to L17 -> L26 [1]
  L18 to L19 -> L26 [1]
  L20 to L21 -> L26 [1]
  L26 to L27 -> L32 [2] lasti
  L27 to L29 -> L30 [2] lasti
  L30 to L32 -> L32 [2] lasti
```
