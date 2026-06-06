# routes/operator_ops

- **pyc:** `app\routes\__pycache__\operator_ops.cpython-314.pyc`
- **expected source path (absent):** `app\routes/operator_ops.py`
- **co_filename (from bytecode):** `app/routes/operator_ops.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** routes

## Module docstring

```
PAS172 — Operator Ops routes.

Admin-only read surfaces for the pilot operations control layer.
Mounted at ``/ops`` (see ``app/main.py``). Auth: X-Admin-Key
header against ``settings.ADMIN_API_KEY`` — same model as
``app/routes/admin.py``.

Doctrine:

* **GET-only.** No POST / PATCH / DELETE in this module. PAS172
  is a read-only operator visibility layer; transitions
  (recover stale, schedule callback) stay in their original
  routes / scripts.
* **Tenant exposure: NONE.** Every route requires the admin
  key. There is no portal / brokerage tenant surface here.
* **Structural responses only.** Every envelope is the closed
  shape produced by the underlying service layer
  (`queue_status_report`, `reminder_report`,
  `detect_stale_dialing_rows`, `heartbeat_monitor_report`).
  No PII. No raw payloads. No transcripts. No dedupe keys.
* **Pagination caps clamped server-side.** Operator typos
  cannot table-scan.
* **Never raises.** All four routes catch and project; on
  failure the envelope status flips to ``skipped`` /
  ``failed``.

Routes (all GET):

    GET /ops/workers/status
        Wraps ``heartbeat_monitor_report``. Optional
        ``worker_type`` + ``limit`` query params.
        Also returns the stale-worker list at the configured
        ``stale_after_seconds`` threshold so a single round
        trip answers "are any workers stale right now?".

    GET /ops/pending-calls/queue
        Wraps ``queue_status_report``. Optional
        ``brokerage_id`` query param.

    GET /ops/callbacks/pending
        Wraps ``reminder_report``. Required
        ``brokerage_id`` query param. Optional
        ``lookahead_minutes``.

    GET /ops/recovery/stale-dialing
        Wraps ``detect_stale_dialing_rows`` (read-only — does
        NOT execute recovery). Optional ``brokerage_id`` +
        ``stale_after_seconds`` + ``limit``.

This module is mounted from ``app/main.py``; the mount itself
is intentionally minimal so it cannot accidentally pull in
worker-startup wiring (PAS162 / PAS170 doctrine).
```

## Imports

`APIRouter`, `Any`, `Depends`, `Dict`, `HTTPException`, `Header`, `Optional`, `Query`, `__future__`, `annotations`, `app.config`, `app.services.callbacks.callback_schedule`, `app.services.ingestion.pending_call_recovery`, `app.services.security.rate_limit`, `app.services.worker.heartbeat_monitor`, `check_rate_limit`, `detect_stale_dialing_rows`, `fastapi`, `get_settings`, `heartbeat_monitor_report`, `list_pending_callbacks`, `logging`, `queue_status_report`, `reminder_report`, `stale_worker_report`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_clamp_int`, `_final_envelope`, `_safe_brokerage`, `_scan_for_forbidden`, `get_callbacks_pending`, `get_pending_calls_queue`, `get_recovery_stale_dialing`, `get_workers_status`, `require_admin`

## Env-key candidates

`ADMIN`, `PENDING`

## String constants (redacted where noted)

- '\nPAS172 — Operator Ops routes.\n\nAdmin-only read surfaces for the pilot operations control layer.\nMounted at ``/ops`` (see ``app/main.py``). Auth: X-Admin-Key\nheader against ``settings.ADMIN_API_KEY`` — same model as\n``app/routes/admin.py``.\n\nDoctrine:\n\n* **GET-only.** No POST / PATCH / DELETE in this module. PAS172\n  is a read-only operator visibility layer; transitions\n  (recover stale, schedule callback) stay in their original\n  routes / scripts.\n* **Tenant exposure: NONE.** Every route requires the admin\n  key. There is no portal / brokerage tenant surface here.\n* **Structural responses only.** Every envelope is the closed\n  shape produced by the underlying service layer\n  (`queue_status_report`, `reminder_report`,\n  `detect_stale_dialing_rows`, `heartbeat_monitor_report`).\n  No PII. No raw payloads. No transcripts. No dedupe keys.\n* **Pagination caps clamped server-side.** Operator typos\n  cannot table-scan.\n* **Never raises.** All four routes catch and project; on\n  failure the envelope status flips to ``skipped`` /\n  ``failed``.\n\nRoutes (all GET):\n\n    GET /ops/workers/status\n        Wraps ``heartbeat_monitor_report``. Optional\n        ``worker_type`` + ``limit`` query params.\n        Also returns the stale-worker list at the configured\n        ``stale_after_seconds`` threshold so a single round\n        trip answers "are any workers stale right now?".\n\n    GET /ops/pending-calls/queue\n        Wraps ``queue_status_report``. Optional\n        ``brokerage_id`` query param.\n\n    GET /ops/callbacks/pending\n        Wraps ``reminder_report``. Required\n        ``brokerage_id`` query param. Optional\n        ``lookahead_minutes``.\n\n    GET /ops/recovery/stale-dialing\n        Wraps ``detect_stale_dialing_rows`` (read-only — does\n        NOT execute recovery). Optional ``brokerage_id`` +\n        ``stale_after_seconds`` + ``limit``.\n\nThis module is mounted from ``app/main.py``; the mount itself\nis intentionally minimal so it cannot accidentally pull in\nworker-startup wiring (PAS162 / PAS170 doctrine).\n'
- 'pas.ops'
- '/workers/status'
- '/pending-calls/queue'
- '/callbacks/pending'
- '/recovery/stale-dialing'
- 'x_admin_key'
- 'str'
- 'return'
- 'bool'
- 'Invalid admin key'
- 'admin'
- 'ADMIN'
- 'allowed'
- 'Operator rate limit exceeded. Retry after the current window.'
- 'envelope'
- 'Any'
- 'Optional[str]'
- 'Defensive — walk the envelope and return the first\nforbidden token found, or None. NEVER raises.'
- 'obj'
- 'env'
- 'Dict[str, Any]'
- 'surface'
- 'Last-line defence: if the envelope smuggled a forbidden\ntoken, collapse to a structural error so the route never\nleaks PII even when the underlying service regresses.'
- 'operator_ops surface='
- ' collapsed — forbidden token leaked'
- 'status'
- 'failed'
- 'error_code'
- 'ops_envelope_forbidden_token'
- 'warnings'
- 'value'
- 'int'
- 'default'
- 'worker_type'
- 'limit'
- 'stale_after_seconds'
- 'Combined worker-heartbeat snapshot + stale-worker list.'
- 'ops.workers.status'
- 'snapshot'
- 'stale'
- 'operator_ops workers_status error type='
- 'unexpected:'
- 'brokerage_id'
- 'ops.pending_calls.queue'
- 'queue'
- 'operator_ops pending_calls_queue error type='
- 'lookahead_minutes'
- 'brokerage_id required'
- 'PENDING'
- 'ops.callbacks.pending'
- 'due_count'
- 'overdue_count'
- 'pending'
- 'reminder'
- 'operator_ops callbacks_pending error type='
- 'Read-only stale-DIALING detection. The operator must\nstill execute recovery via the\n``recover_stale_dialing_rows(..., dry_run=False)`` script\nseam; this route does NOT execute any transition.'
- 'ops.recovery.stale_dialing'
- 'operator_ops recovery_stale_dialing error type='

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS172 — Operator Ops routes.\n\nAdmin-only read surfaces for the pilot operations control layer.\nMounted at ``/ops`` (see ``app/main.py``). Auth: X-Admin-Key\nheader against ``settings.ADMIN_API_KEY`` — same model as\n``app/routes/admin.py``.\n\nDoctrine:\n\n* **GET-only.** No POST / PATCH / DELETE in this module. PAS172\n  is a read-only operator visibility layer; transitions\n  (recover stale, schedule callback) stay in their original\n  routes / scripts.\n* **Tenant exposure: NONE.** Every route requires the admin\n  key. There is no portal / brokerage tenant surface here.\n* **Structural responses only.** Every envelope is the closed\n  shape produced by the underlying service layer\n  (`queue_status_report`, `reminder_report`,\n  `detect_stale_dialing_rows`, `heartbeat_monitor_report`).\n  No PII. No raw payloads. No transcripts. No dedupe keys.\n* **Pagination caps clamped server-side.** Operator typos\n  cannot table-scan.\n* **Never raises.** All four routes catch and project; on\n  failure the envelope status flips to ``skipped`` /\n  ``failed``.\n\nRoutes (all GET):\n\n    GET /ops/workers/status\n        Wraps ``heartbeat_monitor_report``. Optional\n        ``worker_type`` + ``limit`` query params.\n        Also returns the stale-worker list at the configured\n        ``stale_after_seconds`` threshold so a single round\n        trip answers "are any workers stale right now?".\n\n    GET /ops/pending-calls/queue\n        Wraps ``queue_status_report``. Optional\n        ``brokerage_id`` query param.\n\n    GET /ops/callbacks/pending\n        Wraps ``reminder_report``. Required\n        ``brokerage_id`` query param. Optional\n        ``lookahead_minutes``.\n\n    GET /ops/recovery/stale-dialing\n        Wraps ``detect_stale_dialing_rows`` (read-only — does\n        NOT execute recovery). Optional ``brokerage_id`` +\n        ``stale_after_seconds`` + ``limit``.\n\nThis module is mounted from ``app/main.py``; the mount itself\nis intentionally minimal so it cannot accidentally pull in\nworker-startup wiring (PAS162 / PAS170 doctrine).\n')
              STORE_NAME               0 (__doc__)

 56           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 58           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 59           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('Any', 'Dict', 'Optional'))
              IMPORT_NAME              4 (typing)
              IMPORT_FROM              5 (Any)
              STORE_NAME               5 (Any)
              IMPORT_FROM              6 (Dict)
              STORE_NAME               6 (Dict)
              IMPORT_FROM              7 (Optional)
              STORE_NAME               7 (Optional)
              POP_TOP

 61           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('APIRouter', 'Depends', 'HTTPException', 'Header', 'Query'))
              IMPORT_NAME              8 (fastapi)
              IMPORT_FROM              9 (APIRouter)
              STORE_NAME               9 (APIRouter)
              IMPORT_FROM             10 (Depends)
              STORE_NAME              10 (Depends)
              IMPORT_FROM             11 (HTTPException)
              STORE_NAME              11 (HTTPException)
              IMPORT_FROM             12 (Header)
              STORE_NAME              12 (Header)
              IMPORT_FROM             13 (Query)
              STORE_NAME              13 (Query)
              POP_TOP

 63           LOAD_SMALL_INT           0
              LOAD_CONST               5 (('get_settings',))
              IMPORT_NAME             14 (app.config)
              IMPORT_FROM             15 (get_settings)
              STORE_NAME              15 (get_settings)
              POP_TOP

 66           LOAD_NAME                9 (APIRouter)
              PUSH_NULL
              CALL                     0
              STORE_NAME              16 (router)

 67           LOAD_NAME                3 (logging)
              LOAD_ATTR               34 (getLogger)
              PUSH_NULL
              LOAD_CONST               6 ('pas.ops')
              CALL                     1
              STORE_NAME              18 (logger)

 74           LOAD_NAME               12 (Header)
              PUSH_NULL
              LOAD_CONST               7 (Ellipsis)
              CALL                     1
              BUILD_TUPLE              1
              LOAD_CONST               8 (<code object __annotate__ at 0x0000018C17FA3A50, file "app/routes/operator_ops.py", line 74>)
              MAKE_FUNCTION
              LOAD_CONST               9 (<code object require_admin at 0x0000018C1801C9E0, file "app/routes/operator_ops.py", line 74>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              19 (require_admin)

103           LOAD_CONST              10 (500)
              STORE_NAME              20 (_HEARTBEAT_LIMIT_MAX)

104           LOAD_SMALL_INT         100
              STORE_NAME              21 (_HEARTBEAT_LIMIT_DEFAULT)

106           LOAD_SMALL_INT         200
              STORE_NAME              22 (_QUEUE_BROKERAGE_LEN_MAX)

107           LOAD_CONST              10 (500)
              STORE_NAME              23 (_CALLBACK_LIMIT_MAX)

108           LOAD_SMALL_INT          50
              STORE_NAME              24 (_CALLBACK_LIMIT_DEFAULT)

109           LOAD_CONST              10 (500)
              STORE_NAME              25 (_RECOVERY_LIMIT_MAX)

110           LOAD_SMALL_INT         100
              STORE_NAME              26 (_RECOVERY_LIMIT_DEFAULT)

112           LOAD_SMALL_INT          60
              STORE_NAME              27 (_STALE_AFTER_MIN)

113           LOAD_CONST              32 (86400)
              STORE_NAME              28 (_STALE_AFTER_MAX)

120           LOAD_CONST              33 (('phone', 'email', 'name', 'transcript', 'summary_text', 'raw_payload', 'raw_email', 'raw_body', 'secret', 'signature', 'dedupe_key', 'callback_notes'))
              STORE_NAME              29 (_FORBIDDEN_RESPONSE_TOKENS)

127           LOAD_CONST              11 (<code object __annotate__ at 0x0000018C17FA2A60, file "app/routes/operator_ops.py", line 127>)
              MAKE_FUNCTION
              LOAD_CONST              12 (<code object _scan_for_forbidden at 0x0000018C18026130, file "app/routes/operator_ops.py", line 127>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              30 (_scan_for_forbidden)

153           LOAD_CONST              13 (<code object __annotate__ at 0x0000018C18025730, file "app/routes/operator_ops.py", line 153>)
              MAKE_FUNCTION
              LOAD_CONST              14 (<code object _final_envelope at 0x0000018C17FE1A70, file "app/routes/operator_ops.py", line 153>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              31 (_final_envelope)

172           LOAD_CONST              15 (<code object __annotate__ at 0x0000018C18025E30, file "app/routes/operator_ops.py", line 172>)
              MAKE_FUNCTION
              LOAD_CONST              16 (<code object _clamp_int at 0x0000018C18038B70, file "app/routes/operator_ops.py", line 172>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              32 (_clamp_int)

184           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C17FA33C0, file "app/routes/operator_ops.py", line 184>)
              MAKE_FUNCTION
              LOAD_CONST              18 (<code object _safe_brokerage at 0x0000018C17F95E60, file "app/routes/operator_ops.py", line 184>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              33 (_safe_brokerage)

199           LOAD_NAME               16 (router)
              LOAD_ATTR               69 (get + NULL|self)
              LOAD_CONST              19 ('/workers/status')
              CALL                     1

201           LOAD_NAME               13 (Query)
              PUSH_NULL
              LOAD_CONST               2 (None)
              LOAD_SMALL_INT          64
              LOAD_CONST              20 (('max_length',))
              CALL_KW                  2

202           LOAD_NAME               13 (Query)
              PUSH_NULL
              LOAD_NAME               21 (_HEARTBEAT_LIMIT_DEFAULT)
              CALL                     1

203           LOAD_NAME               13 (Query)
              PUSH_NULL
              LOAD_CONST              34 (300)
              CALL                     1

204           LOAD_NAME               10 (Depends)
              PUSH_NULL
              LOAD_NAME               19 (require_admin)
              CALL                     1

200           BUILD_TUPLE              4
              LOAD_CONST              21 (<code object __annotate__ at 0x0000018C18025D30, file "app/routes/operator_ops.py", line 200>)
              MAKE_FUNCTION
              LOAD_CONST              22 (<code object get_workers_status at 0x0000018C17D81580, file "app/routes/operator_ops.py", line 199>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

199           CALL                     0

200           STORE_NAME              35 (get_workers_status)

245           LOAD_NAME               16 (router)
              LOAD_ATTR               69 (get + NULL|self)
              LOAD_CONST              23 ('/pending-calls/queue')
              CALL                     1

247           LOAD_NAME               13 (Query)
              PUSH_NULL
              LOAD_CONST               2 (None)
              LOAD_NAME               22 (_QUEUE_BROKERAGE_LEN_MAX)
              LOAD_CONST              20 (('max_length',))
              CALL_KW                  2

248           LOAD_NAME               10 (Depends)
              PUSH_NULL
              LOAD_NAME               19 (require_admin)
              CALL                     1

246           BUILD_TUPLE              2
              LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA35A0, file "app/routes/operator_ops.py", line 246>)
              MAKE_FUNCTION
              LOAD_CONST              25 (<code object get_pending_calls_queue at 0x0000018C17F6A300, file "app/routes/operator_ops.py", line 245>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

245           CALL                     0

246           STORE_NAME              36 (get_pending_calls_queue)

272           LOAD_NAME               16 (router)
              LOAD_ATTR               69 (get + NULL|self)
              LOAD_CONST              26 ('/callbacks/pending')
              CALL                     1

274           LOAD_NAME               13 (Query)
              PUSH_NULL
              LOAD_CONST               7 (Ellipsis)
              LOAD_NAME               22 (_QUEUE_BROKERAGE_LEN_MAX)
              LOAD_CONST              20 (('max_length',))
              CALL_KW                  2

275           LOAD_NAME               13 (Query)
              PUSH_NULL
              LOAD_SMALL_INT          60
              CALL                     1

276           LOAD_NAME               10 (Depends)
              PUSH_NULL
              LOAD_NAME               19 (require_admin)
              CALL                     1

273           BUILD_TUPLE              3
              LOAD_CONST              27 (<code object __annotate__ at 0x0000018C18025530, file "app/routes/operator_ops.py", line 273>)
              MAKE_FUNCTION
              LOAD_CONST              28 (<code object get_callbacks_pending at 0x0000018C181D50F0, file "app/routes/operator_ops.py", line 272>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

272           CALL                     0

273           STORE_NAME              37 (get_callbacks_pending)

314           LOAD_NAME               16 (router)
              LOAD_ATTR               69 (get + NULL|self)
              LOAD_CONST              29 ('/recovery/stale-dialing')
              CALL                     1

316           LOAD_NAME               13 (Query)
              PUSH_NULL
              LOAD_CONST               2 (None)
              LOAD_NAME               22 (_QUEUE_BROKERAGE_LEN_MAX)
              LOAD_CONST              20 (('max_length',))
              CALL_KW                  2

317           LOAD_NAME               13 (Query)
              PUSH_NULL
              LOAD_CONST              35 (900)
              CALL                     1

318           LOAD_NAME               13 (Query)
              PUSH_NULL
              LOAD_NAME               26 (_RECOVERY_LIMIT_DEFAULT)
              CALL                     1

319           LOAD_NAME               10 (Depends)
              PUSH_NULL
              LOAD_NAME               19 (require_admin)
              CALL                     1

315           BUILD_TUPLE              4
              LOAD_CONST              30 (<code object __annotate__ at 0x0000018C18025830, file "app/routes/operator_ops.py", line 315>)
              MAKE_FUNCTION
              LOAD_CONST              31 (<code object get_recovery_stale_dialing at 0x0000018C17CD0F70, file "app/routes/operator_ops.py", line 314>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

314           CALL                     0

315           STORE_NAME              38 (get_recovery_stale_dialing)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "app/routes/operator_ops.py", line 74>:
 74           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('x_admin_key')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object require_admin at 0x0000018C1801C9E0, file "app/routes/operator_ops.py", line 74>:
  74            RESUME                   0

  75            LOAD_GLOBAL              1 (get_settings + NULL)
                CALL                     0
                STORE_FAST               1 (settings)

  76            LOAD_FAST_BORROW         1 (settings)
                LOAD_ATTR                2 (ADMIN_API_KEY)
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (x_admin_key, settings)
                LOAD_ATTR                2 (ADMIN_API_KEY)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       14 (to L2)
                NOT_TAKEN

  77    L1:     LOAD_GLOBAL              5 (HTTPException + NULL)
                LOAD_CONST               0 (401)
                LOAD_CONST               1 ('Invalid admin key')
                LOAD_CONST               2 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

  80    L2:     NOP

  81    L3:     LOAD_SMALL_INT           0
                LOAD_CONST               3 (('check_rate_limit',))
                IMPORT_NAME              3 (app.services.security.rate_limit)
                IMPORT_FROM              4 (check_rate_limit)
                STORE_FAST               2 (check_rate_limit)
                POP_TOP

  82            LOAD_FAST_BORROW         2 (check_rate_limit)
                PUSH_NULL

  83            LOAD_CONST               4 ('admin')

  84            LOAD_CONST               5 ('ADMIN')

  85            LOAD_FAST_BORROW         0 (x_admin_key)

  82            LOAD_CONST               6 (('surface', 'actor_type', 'actor_token'))
                CALL_KW                  3
                STORE_FAST               3 (_rl_verdict)

  87            LOAD_FAST_BORROW         3 (_rl_verdict)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               7 ('allowed')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        14 (to L6)
        L4:     NOT_TAKEN

  88    L5:     LOAD_GLOBAL              5 (HTTPException + NULL)

  89            LOAD_CONST               8 (429)

  90            LOAD_CONST               9 ('Operator rate limit exceeded. Retry after the current window.')

  88            LOAD_CONST               2 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

  87    L6:     NOP

  96            LOAD_CONST              10 (True)
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

  92            LOAD_GLOBAL              4 (HTTPException)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                POP_TOP

  93            RAISE_VARARGS            0

  94    L8:     LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L12)
        L9:     NOT_TAKEN
       L10:     POP_TOP

  95   L11:     POP_EXCEPT

  96            LOAD_CONST              10 (True)
                RETURN_VALUE

  94   L12:     RERAISE                  0

  --   L13:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L7 [0]
  L5 to L6 -> L7 [0]
  L7 to L9 -> L13 [1] lasti
  L10 to L11 -> L13 [1] lasti
  L12 to L13 -> L13 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "app/routes/operator_ops.py", line 127>:
127           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('envelope')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _scan_for_forbidden at 0x0000018C18026130, file "app/routes/operator_ops.py", line 127>:
  --           MAKE_CELL                1 (walk)

 127           RESUME                   0

 130           LOAD_CONST               1 (<code object __annotate__ at 0x0000018C17FA3000, file "app/routes/operator_ops.py", line 130>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         1 (walk)
               BUILD_TUPLE              1
               LOAD_CONST               2 (<code object walk at 0x0000018C17CC2960, file "app/routes/operator_ops.py", line 130>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_DEREF              1 (walk)

 150           LOAD_DEREF               1 (walk)
               PUSH_NULL
               LOAD_FAST_BORROW         0 (envelope)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3000, file "app/routes/operator_ops.py", line 130>:
130           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('obj')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object walk at 0x0000018C17CC2960, file "app/routes/operator_ops.py", line 130>:
  --            COPY_FREE_VARS           1

 130            RESUME                   0

 131            NOP

 132    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      111 (to L16)
        L2:     NOT_TAKEN

 133    L3:     LOAD_FAST_BORROW         0 (obj)
                LOAD_ATTR                5 (items + NULL|self)
                CALL                     0
                GET_ITER
        L4:     FOR_ITER                88 (to L14)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   18 (k, v)

 134            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (k)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       42 (to L10)
                NOT_TAKEN

 135            LOAD_FAST_BORROW         1 (k)
                LOAD_ATTR                9 (lower + NULL|self)
                CALL                     0
                STORE_FAST               3 (kl)

 136            LOAD_GLOBAL             10 (_FORBIDDEN_RESPONSE_TOKENS)
                GET_ITER
        L5:     FOR_ITER                15 (to L9)
                STORE_FAST               4 (tok)

 137            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, kl)
                CONTAINS_OP              0 (in)
        L6:     POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L5)

 138    L7:     LOAD_FAST_BORROW         4 (tok)
                SWAP                     2
                POP_TOP
                SWAP                     2
                POP_TOP
        L8:     RETURN_VALUE

 136    L9:     END_FOR
                POP_ITER

 139   L10:     LOAD_DEREF               6 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                STORE_FAST               5 (sub)

 140            LOAD_FAST_BORROW         5 (sub)
                TO_BOOL
       L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           86 (to L4)

 141   L12:     LOAD_FAST_BORROW         5 (sub)
                SWAP                     2
                POP_TOP
       L13:     RETURN_VALUE

 133   L14:     END_FOR
                POP_ITER

 149   L15:     LOAD_CONST               0 (None)
                RETURN_VALUE

 142   L16:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL             12 (list)
                LOAD_GLOBAL             14 (tuple)
                BUILD_TUPLE              2
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       30 (to L22)
                NOT_TAKEN

 143            LOAD_FAST_BORROW         0 (obj)
                GET_ITER
       L17:     FOR_ITER                23 (to L21)
                STORE_FAST               2 (v)

 144            LOAD_DEREF               6 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                STORE_FAST               5 (sub)

 145            LOAD_FAST_BORROW         5 (sub)
                TO_BOOL
       L18:     POP_JUMP_IF_TRUE         3 (to L19)
                NOT_TAKEN
                JUMP_BACKWARD           21 (to L17)

 146   L19:     LOAD_FAST_BORROW         5 (sub)
                SWAP                     2
                POP_TOP
       L20:     RETURN_VALUE

 143   L21:     END_FOR
                POP_ITER

 149   L22:     LOAD_CONST               0 (None)
                RETURN_VALUE

  --   L23:     PUSH_EXC_INFO

 147            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L25)
                NOT_TAKEN
                POP_TOP

 148   L24:     POP_EXCEPT
                LOAD_CONST               0 (None)
                RETURN_VALUE

 147   L25:     RERAISE                  0

  --   L26:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L23 [0]
  L3 to L6 -> L23 [0]
  L7 to L8 -> L23 [0]
  L9 to L11 -> L23 [0]
  L12 to L13 -> L23 [0]
  L14 to L15 -> L23 [0]
  L16 to L18 -> L23 [0]
  L19 to L20 -> L23 [0]
  L21 to L22 -> L23 [0]
  L23 to L24 -> L26 [1] lasti
  L25 to L26 -> L26 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025730, file "app/routes/operator_ops.py", line 153>:
153           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('env')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('surface')
              LOAD_CONST               4 ('str')
              LOAD_CONST               5 ('return')
              LOAD_CONST               2 ('Dict[str, Any]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _final_envelope at 0x0000018C17FE1A70, file "app/routes/operator_ops.py", line 153>:
153           RESUME                   0

157           LOAD_GLOBAL              1 (_scan_for_forbidden + NULL)
              LOAD_FAST_BORROW         0 (env)
              CALL                     1
              STORE_FAST               2 (leak)

158           LOAD_FAST_BORROW         2 (leak)
              TO_BOOL
              POP_JUMP_IF_FALSE       37 (to L1)
              NOT_TAKEN

159           LOAD_GLOBAL              2 (logger)
              LOAD_ATTR                5 (warning + NULL|self)

160           LOAD_CONST               1 ('operator_ops surface=')
              LOAD_FAST_BORROW         1 (surface)
              FORMAT_SIMPLE
              LOAD_CONST               2 (' collapsed — forbidden token leaked')
              BUILD_STRING             3

159           CALL                     1
              POP_TOP

164           LOAD_CONST               3 ('status')
              LOAD_CONST               4 ('failed')

165           LOAD_CONST               5 ('surface')
              LOAD_FAST_BORROW         1 (surface)

166           LOAD_CONST               6 ('error_code')
              LOAD_CONST               7 ('ops_envelope_forbidden_token')

167           LOAD_CONST               8 ('warnings')
              LOAD_CONST               7 ('ops_envelope_forbidden_token')
              BUILD_LIST               1

163           BUILD_MAP                4
              RETURN_VALUE

169   L1:     LOAD_FAST_BORROW         0 (env)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025E30, file "app/routes/operator_ops.py", line 172>:
172           RESUME                   0
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

Disassembly of <code object _clamp_int at 0x0000018C18038B70, file "app/routes/operator_ops.py", line 172>:
 172           RESUME                   0

 173           NOP

 174   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               4 (v)

 177   L2:     LOAD_FAST_LOAD_FAST     65 (v, lo)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 178           LOAD_FAST                1 (lo)
               RETURN_VALUE

 179   L3:     LOAD_FAST_LOAD_FAST     66 (v, hi)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN

 180           LOAD_FAST                2 (hi)
               RETURN_VALUE

 181   L4:     LOAD_FAST                4 (v)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 175           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L7)
               NOT_TAKEN
               POP_TOP

 176           LOAD_FAST                3 (default)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

 175   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "app/routes/operator_ops.py", line 184>:
184           RESUME                   0
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

Disassembly of <code object _safe_brokerage at 0x0000018C17F95E60, file "app/routes/operator_ops.py", line 184>:
184           RESUME                   0

185           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

186           LOAD_CONST               0 (None)
              RETURN_VALUE

187   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

188           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

189           LOAD_CONST               0 (None)
              RETURN_VALUE

190   L2:     LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         1 (s)
              CALL                     1
              LOAD_GLOBAL              8 (_QUEUE_BROKERAGE_LEN_MAX)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

191           LOAD_CONST               0 (None)
              RETURN_VALUE

192   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025D30, file "app/routes/operator_ops.py", line 200>:
200           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('worker_type')

201           LOAD_CONST               2 ('Optional[str]')

200           LOAD_CONST               3 ('limit')

202           LOAD_CONST               4 ('int')

200           LOAD_CONST               5 ('stale_after_seconds')

203           LOAD_CONST               4 ('int')

200           LOAD_CONST               6 ('return')

205           LOAD_CONST               7 ('Dict[str, Any]')

200           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object get_workers_status at 0x0000018C17D81580, file "app/routes/operator_ops.py", line 199>:
 199            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 207            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('heartbeat_monitor_report', 'stale_worker_report'))
                IMPORT_NAME              0 (app.services.worker.heartbeat_monitor)
                IMPORT_FROM              1 (heartbeat_monitor_report)
                STORE_FAST               4 (heartbeat_monitor_report)
                IMPORT_FROM              2 (stale_worker_report)
                STORE_FAST               5 (stale_worker_report)
                POP_TOP

 211    L2:     NOP

 212    L3:     LOAD_GLOBAL              7 (_clamp_int + NULL)

 213            LOAD_FAST_BORROW         1 (limit)
                LOAD_SMALL_INT           1
                LOAD_GLOBAL              8 (_HEARTBEAT_LIMIT_MAX)
                LOAD_GLOBAL             10 (_HEARTBEAT_LIMIT_DEFAULT)

 212            CALL                     4
                STORE_FAST               6 (capped_limit)

 215            LOAD_GLOBAL              7 (_clamp_int + NULL)

 216            LOAD_FAST_BORROW         2 (stale_after_seconds)
                LOAD_GLOBAL             12 (_STALE_AFTER_MIN)
                LOAD_GLOBAL             14 (_STALE_AFTER_MAX)
                LOAD_CONST              17 (300)

 215            CALL                     4
                STORE_FAST               7 (capped_stale)

 218            LOAD_FAST_BORROW         4 (heartbeat_monitor_report)
                PUSH_NULL

 219            LOAD_FAST_BORROW_LOAD_FAST_BORROW 6 (worker_type, capped_limit)

 218            LOAD_CONST               2 (('worker_type', 'limit'))
                CALL_KW                  2
                STORE_FAST               8 (snapshot)

 221            LOAD_FAST_BORROW         5 (stale_worker_report)
                PUSH_NULL

 222            LOAD_FAST_BORROW         0 (worker_type)

 223            LOAD_FAST_BORROW         7 (capped_stale)

 224            LOAD_FAST_BORROW         6 (capped_limit)

 221            LOAD_CONST               3 (('worker_type', 'stale_after_seconds', 'limit'))
                CALL_KW                  3
                STORE_FAST               9 (stale)

 227            LOAD_CONST               4 ('status')
                LOAD_FAST_BORROW         8 (snapshot)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST               4 ('status')
                CALL                     1
                LOAD_CONST               5 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L4)
                NOT_TAKEN
                LOAD_CONST               5 ('ok')
                JUMP_FORWARD            16 (to L5)
        L4:     LOAD_FAST_BORROW         8 (snapshot)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST               4 ('status')
                CALL                     1

 228    L5:     LOAD_CONST               6 ('surface')
                LOAD_CONST               7 ('ops.workers.status')

 229            LOAD_CONST               8 ('snapshot')
                LOAD_FAST_BORROW         8 (snapshot)

 230            LOAD_CONST               9 ('stale')
                LOAD_FAST_BORROW         9 (stale)

 226            BUILD_MAP                4
                STORE_FAST              10 (env)

 242    L6:     LOAD_GLOBAL             29 (_final_envelope + NULL)
                LOAD_FAST_BORROW        10 (env)
                LOAD_CONST               7 ('ops.workers.status')
                LOAD_CONST              16 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

 232            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L11)
                NOT_TAKEN
                STORE_FAST              11 (e)

 233    L8:     LOAD_GLOBAL             20 (logger)
                LOAD_ATTR               23 (warning + NULL|self)

 234            LOAD_CONST              10 ('operator_ops workers_status error type=')
                LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 233            CALL                     1
                POP_TOP

 237            LOAD_CONST               4 ('status')
                LOAD_CONST              11 ('failed')

 238            LOAD_CONST               6 ('surface')
                LOAD_CONST               7 ('ops.workers.status')

 239            LOAD_CONST              12 ('error_code')
                LOAD_CONST              13 ('unexpected:')
                LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 240            LOAD_CONST              14 ('warnings')
                BUILD_LIST               0

 236            BUILD_MAP                4
                STORE_FAST              10 (env)
        L9:     POP_EXCEPT
                LOAD_CONST              15 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                JUMP_BACKWARD_NO_INTERRUPT 104 (to L6)

  --   L10:     LOAD_CONST              15 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RERAISE                  1

 232   L11:     RERAISE                  0

  --   L12:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L13:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L13 [0] lasti
  L3 to L6 -> L7 [0]
  L6 to L7 -> L13 [0] lasti
  L7 to L8 -> L12 [1] lasti
  L8 to L9 -> L10 [1] lasti
  L9 to L10 -> L13 [0] lasti
  L10 to L12 -> L12 [1] lasti
  L12 to L13 -> L13 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "app/routes/operator_ops.py", line 246>:
246           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

247           LOAD_CONST               2 ('Optional[str]')

246           LOAD_CONST               3 ('return')

249           LOAD_CONST               4 ('Dict[str, Any]')

246           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object get_pending_calls_queue at 0x0000018C17F6A300, file "app/routes/operator_ops.py", line 245>:
 245            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 250            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('queue_status_report',))
                IMPORT_NAME              0 (app.services.ingestion.pending_call_recovery)
                IMPORT_FROM              1 (queue_status_report)
                STORE_FAST               2 (queue_status_report)
                POP_TOP

 251            LOAD_GLOBAL              5 (_safe_brokerage + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                STORE_FAST               3 (bid)

 252    L2:     NOP

 253    L3:     LOAD_FAST_BORROW         2 (queue_status_report)
                PUSH_NULL
                LOAD_FAST_BORROW         3 (bid)
                LOAD_CONST               2 (('brokerage_id',))
                CALL_KW                  1
                STORE_FAST               4 (report)

 255            LOAD_CONST               3 ('status')
                LOAD_FAST_BORROW         4 (report)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               3 ('status')
                CALL                     1

 256            LOAD_CONST               4 ('surface')
                LOAD_CONST               5 ('ops.pending_calls.queue')

 257            LOAD_CONST               6 ('queue')
                LOAD_FAST_BORROW         4 (report)

 254            BUILD_MAP                3
                STORE_FAST               5 (env)

 269    L4:     LOAD_GLOBAL             19 (_final_envelope + NULL)
                LOAD_FAST_BORROW         5 (env)
                LOAD_CONST               5 ('ops.pending_calls.queue')
                LOAD_CONST              13 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --    L5:     PUSH_EXC_INFO

 259            LOAD_GLOBAL              8 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L9)
                NOT_TAKEN
                STORE_FAST               6 (e)

 260    L6:     LOAD_GLOBAL             10 (logger)
                LOAD_ATTR               13 (warning + NULL|self)

 261            LOAD_CONST               7 ('operator_ops pending_calls_queue error type=')
                LOAD_GLOBAL             15 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               16 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 260            CALL                     1
                POP_TOP

 264            LOAD_CONST               3 ('status')
                LOAD_CONST               8 ('failed')

 265            LOAD_CONST               4 ('surface')
                LOAD_CONST               5 ('ops.pending_calls.queue')

 266            LOAD_CONST               9 ('error_code')
                LOAD_CONST              10 ('unexpected:')
                LOAD_GLOBAL             15 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               16 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 267            LOAD_CONST              11 ('warnings')
                BUILD_LIST               0

 263            BUILD_MAP                4
                STORE_FAST               5 (env)
        L7:     POP_EXCEPT
                LOAD_CONST              12 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                JUMP_BACKWARD_NO_INTERRUPT 104 (to L4)

  --    L8:     LOAD_CONST              12 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

 259    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L11:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L11 [0] lasti
  L3 to L4 -> L5 [0]
  L4 to L5 -> L11 [0] lasti
  L5 to L6 -> L10 [1] lasti
  L6 to L7 -> L8 [1] lasti
  L7 to L8 -> L11 [0] lasti
  L8 to L10 -> L10 [1] lasti
  L10 to L11 -> L11 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025530, file "app/routes/operator_ops.py", line 273>:
273           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

274           LOAD_CONST               2 ('str')

273           LOAD_CONST               3 ('lookahead_minutes')

275           LOAD_CONST               4 ('int')

273           LOAD_CONST               5 ('return')

277           LOAD_CONST               6 ('Dict[str, Any]')

273           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object get_callbacks_pending at 0x0000018C181D50F0, file "app/routes/operator_ops.py", line 272>:
 272            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 278            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('reminder_report', 'list_pending_callbacks'))
                IMPORT_NAME              0 (app.services.callbacks.callback_schedule)
                IMPORT_FROM              1 (reminder_report)
                STORE_FAST               3 (reminder_report)
                IMPORT_FROM              2 (list_pending_callbacks)
                STORE_FAST               4 (list_pending_callbacks)
                POP_TOP

 281            LOAD_GLOBAL              7 (_safe_brokerage + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                STORE_FAST               5 (bid)

 282            LOAD_FAST_BORROW         5 (bid)
                TO_BOOL
                POP_JUMP_IF_TRUE        14 (to L2)
                NOT_TAKEN

 283            LOAD_GLOBAL              9 (HTTPException + NULL)
                LOAD_CONST               2 (400)
                LOAD_CONST               3 ('brokerage_id required')
                LOAD_CONST               4 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

 284    L2:     LOAD_GLOBAL             11 (_clamp_int + NULL)

 285            LOAD_FAST_BORROW         1 (lookahead_minutes)
                LOAD_SMALL_INT           1
                LOAD_CONST              23 (1440)
                LOAD_SMALL_INT          60

 284            CALL                     4
                STORE_FAST               6 (capped_lookahead)

 287    L3:     NOP

 288    L4:     LOAD_FAST_BORROW         3 (reminder_report)
                PUSH_NULL
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (bid, capped_lookahead)
                LOAD_CONST               5 (('lookahead_minutes',))
                CALL_KW                  2
                STORE_FAST               7 (report)

 289            LOAD_FAST_BORROW         4 (list_pending_callbacks)
                PUSH_NULL

 290            LOAD_FAST_BORROW         5 (bid)
                LOAD_CONST               6 ('PENDING')
                LOAD_GLOBAL             12 (_CALLBACK_LIMIT_DEFAULT)

 289            LOAD_CONST               7 (('status', 'limit'))
                CALL_KW                  3
                STORE_FAST               8 (listed)

 293            LOAD_CONST               8 ('status')
                LOAD_FAST_BORROW         7 (report)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST               8 ('status')
                CALL                     1

 294            LOAD_CONST               9 ('surface')
                LOAD_CONST              10 ('ops.callbacks.pending')

 295            LOAD_CONST              11 ('lookahead_minutes')
                LOAD_FAST_BORROW         6 (capped_lookahead)

 296            LOAD_CONST              12 ('due_count')
                LOAD_FAST_BORROW         7 (report)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              12 ('due_count')
                LOAD_SMALL_INT           0
                CALL                     2

 297            LOAD_CONST              13 ('overdue_count')
                LOAD_FAST_BORROW         7 (report)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              13 ('overdue_count')
                LOAD_SMALL_INT           0
                CALL                     2

 298            LOAD_CONST              14 ('pending')
                LOAD_FAST_BORROW         8 (listed)

 299            LOAD_CONST              15 ('reminder')
                LOAD_FAST_BORROW         7 (report)

 292            BUILD_MAP                7
                STORE_FAST               9 (env)

 311    L5:     LOAD_GLOBAL             27 (_final_envelope + NULL)
                LOAD_FAST_BORROW         9 (env)
                LOAD_CONST              10 ('ops.callbacks.pending')
                LOAD_CONST              22 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --    L6:     PUSH_EXC_INFO

 301            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L10)
                NOT_TAKEN
                STORE_FAST              10 (e)

 302    L7:     LOAD_GLOBAL             18 (logger)
                LOAD_ATTR               21 (warning + NULL|self)

 303            LOAD_CONST              16 ('operator_ops callbacks_pending error type=')
                LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 302            CALL                     1
                POP_TOP

 306            LOAD_CONST               8 ('status')
                LOAD_CONST              17 ('failed')

 307            LOAD_CONST               9 ('surface')
                LOAD_CONST              10 ('ops.callbacks.pending')

 308            LOAD_CONST              18 ('error_code')
                LOAD_CONST              19 ('unexpected:')
                LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 309            LOAD_CONST              20 ('warnings')
                BUILD_LIST               0

 305            BUILD_MAP                4
                STORE_FAST               9 (env)
        L8:     POP_EXCEPT
                LOAD_CONST              21 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                JUMP_BACKWARD_NO_INTERRUPT 104 (to L5)

  --    L9:     LOAD_CONST              21 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RERAISE                  1

 301   L10:     RERAISE                  0

  --   L11:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L12:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L3 -> L12 [0] lasti
  L4 to L5 -> L6 [0]
  L5 to L6 -> L12 [0] lasti
  L6 to L7 -> L11 [1] lasti
  L7 to L8 -> L9 [1] lasti
  L8 to L9 -> L12 [0] lasti
  L9 to L11 -> L11 [1] lasti
  L11 to L12 -> L12 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025830, file "app/routes/operator_ops.py", line 315>:
315           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

316           LOAD_CONST               2 ('Optional[str]')

315           LOAD_CONST               3 ('stale_after_seconds')

317           LOAD_CONST               4 ('int')

315           LOAD_CONST               5 ('limit')

318           LOAD_CONST               4 ('int')

315           LOAD_CONST               6 ('return')

320           LOAD_CONST               7 ('Dict[str, Any]')

315           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object get_recovery_stale_dialing at 0x0000018C17CD0F70, file "app/routes/operator_ops.py", line 314>:
 314            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 325            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('detect_stale_dialing_rows',))
                IMPORT_NAME              0 (app.services.ingestion.pending_call_recovery)
                IMPORT_FROM              1 (detect_stale_dialing_rows)
                STORE_FAST               4 (detect_stale_dialing_rows)
                POP_TOP

 328            LOAD_GLOBAL              5 (_safe_brokerage + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                STORE_FAST               5 (bid)

 329            LOAD_GLOBAL              7 (_clamp_int + NULL)

 330            LOAD_FAST_BORROW         1 (stale_after_seconds)
                LOAD_GLOBAL              8 (_STALE_AFTER_MIN)
                LOAD_GLOBAL             10 (_STALE_AFTER_MAX)
                LOAD_CONST              16 (900)

 329            CALL                     4
                STORE_FAST               6 (capped_stale)

 332            LOAD_GLOBAL              7 (_clamp_int + NULL)

 333            LOAD_FAST_BORROW         2 (limit)
                LOAD_SMALL_INT           1
                LOAD_GLOBAL             12 (_RECOVERY_LIMIT_MAX)
                LOAD_GLOBAL             14 (_RECOVERY_LIMIT_DEFAULT)

 332            CALL                     4
                STORE_FAST               7 (capped_limit)

 335    L2:     NOP

 336    L3:     LOAD_FAST_BORROW         4 (detect_stale_dialing_rows)
                PUSH_NULL

 337            LOAD_FAST_BORROW         5 (bid)

 338            LOAD_FAST_BORROW         6 (capped_stale)

 339            LOAD_FAST_BORROW         7 (capped_limit)

 336            LOAD_CONST               2 (('brokerage_id', 'stale_after_seconds', 'limit'))
                CALL_KW                  3
                STORE_FAST               8 (report)

 342            LOAD_CONST               3 ('status')
                LOAD_FAST_BORROW         8 (report)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST               3 ('status')
                CALL                     1

 343            LOAD_CONST               4 ('surface')
                LOAD_CONST               5 ('ops.recovery.stale_dialing')

 344            LOAD_CONST               6 ('stale_after_seconds')
                LOAD_FAST_BORROW         6 (capped_stale)

 345            LOAD_CONST               7 ('limit')
                LOAD_FAST_BORROW         7 (capped_limit)

 346            LOAD_CONST               8 ('stale')
                LOAD_FAST_BORROW         8 (report)

 341            BUILD_MAP                5
                STORE_FAST               9 (env)

 358    L4:     LOAD_GLOBAL             29 (_final_envelope + NULL)
                LOAD_FAST_BORROW         9 (env)
                LOAD_CONST               5 ('ops.recovery.stale_dialing')
                LOAD_CONST              15 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --    L5:     PUSH_EXC_INFO

 348            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L9)
                NOT_TAKEN
                STORE_FAST              10 (e)

 349    L6:     LOAD_GLOBAL             20 (logger)
                LOAD_ATTR               23 (warning + NULL|self)

 350            LOAD_CONST               9 ('operator_ops recovery_stale_dialing error type=')
                LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 349            CALL                     1
                POP_TOP

 353            LOAD_CONST               3 ('status')
                LOAD_CONST              10 ('failed')

 354            LOAD_CONST               4 ('surface')
                LOAD_CONST               5 ('ops.recovery.stale_dialing')

 355            LOAD_CONST              11 ('error_code')
                LOAD_CONST              12 ('unexpected:')
                LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 356            LOAD_CONST              13 ('warnings')
                BUILD_LIST               0

 352            BUILD_MAP                4
                STORE_FAST               9 (env)
        L7:     POP_EXCEPT
                LOAD_CONST              14 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                JUMP_BACKWARD_NO_INTERRUPT 104 (to L4)

  --    L8:     LOAD_CONST              14 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RERAISE                  1

 348    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L11:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L11 [0] lasti
  L3 to L4 -> L5 [0]
  L4 to L5 -> L11 [0] lasti
  L5 to L6 -> L10 [1] lasti
  L6 to L7 -> L8 [1] lasti
  L7 to L8 -> L11 [0] lasti
  L8 to L10 -> L10 [1] lasti
  L10 to L11 -> L11 [0] lasti
```
