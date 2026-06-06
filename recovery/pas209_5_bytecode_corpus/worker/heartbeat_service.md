# worker/heartbeat_service

- **pyc:** `app\services\worker\__pycache__\heartbeat_service.cpython-314.pyc`
- **expected source path (absent):** `app\services\worker/heartbeat_service.py`
- **co_filename (from bytecode):** `app/services/worker\heartbeat_service.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** worker

## Module docstring

```
PAS172 — Worker heartbeat service (Supabase-backed v1).

Operator-facing minimum viable surface for "is the worker
alive?". The PAS162 pending-call worker (and any future
worker — callback reminder, operator reaper, monitoring
dispatcher) may opt-in to heartbeat writes via:

    register_worker_heartbeat(worker_id=..., worker_type=...)
    update_worker_heartbeat(worker_id=..., metadata={...})
    mark_worker_stopped(worker_id=...)

Doctrine carried by every helper here:

* **Writes are opt-in.** The PAS162 worker default-OFF
  doctrine is unchanged — even when the worker IS started,
  heartbeat writes only fire if the worker calls the helpers
  explicitly. There is no auto-fire from any startup hook.
* **No PII anywhere.** No phone / email / name / transcript /
  raw_payload / summary / signature / dedupe_key. The
  metadata dict is projected against a closed allow-list at
  insert / update time; anything outside the list is
  dropped.
* **Closed-shape envelopes.** Every helper returns
  ``{status, worker_id, warnings, error_code}``; reads add
  ``rows`` / ``stale`` counters. NEVER raises.
* **DB unavailable falls back to a structural ``status="skipped"``**
  envelope so the worker continues running even when the
  durable store is unreachable. This is the same
  fallback-safe pattern as PAS166 / PAS171.
* **Closed worker_type enum** mirroring the v20 SQL
  CHECK constraint.
* **Closed status enum** ``STARTING / RUNNING / DEGRADED /
  STOPPED``.

Public surface:

  * ``register_worker_heartbeat(...)``
  * ``update_worker_heartbeat(...)``
  * ``mark_worker_stopped(...)``
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.db.supabase_client`, `datetime`, `get_supabase`, `logging`, `os`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_bound_str`, `_get_db_safe`, `_is_unique_violation`, `_iso`, `_now_dt`, `_project_metadata`, `_project_row`, `_safe_envelope`, `_validate_status`, `_validate_worker_id`, `_validate_worker_type`, `mark_worker_stopped`, `register_worker_heartbeat`, `update_worker_heartbeat`

## Env-key candidates

`RUNNING`, `STARTING`, `STOPPED`

## String constants (redacted where noted)

- '\nPAS172 — Worker heartbeat service (Supabase-backed v1).\n\nOperator-facing minimum viable surface for "is the worker\nalive?". The PAS162 pending-call worker (and any future\nworker — callback reminder, operator reaper, monitoring\ndispatcher) may opt-in to heartbeat writes via:\n\n    register_worker_heartbeat(worker_id=..., worker_type=...)\n    update_worker_heartbeat(worker_id=..., metadata={...})\n    mark_worker_stopped(worker_id=...)\n\nDoctrine carried by every helper here:\n\n* **Writes are opt-in.** The PAS162 worker default-OFF\n  doctrine is unchanged — even when the worker IS started,\n  heartbeat writes only fire if the worker calls the helpers\n  explicitly. There is no auto-fire from any startup hook.\n* **No PII anywhere.** No phone / email / name / transcript /\n  raw_payload / summary / signature / dedupe_key. The\n  metadata dict is projected against a closed allow-list at\n  insert / update time; anything outside the list is\n  dropped.\n* **Closed-shape envelopes.** Every helper returns\n  ``{status, worker_id, warnings, error_code}``; reads add\n  ``rows`` / ``stale`` counters. NEVER raises.\n* **DB unavailable falls back to a structural ``status="skipped"``**\n  envelope so the worker continues running even when the\n  durable store is unreachable. This is the same\n  fallback-safe pattern as PAS166 / PAS171.\n* **Closed worker_type enum** mirroring the v20 SQL\n  CHECK constraint.\n* **Closed status enum** ``STARTING / RUNNING / DEGRADED /\n  STOPPED``.\n\nPublic surface:\n\n  * ``register_worker_heartbeat(...)``\n  * ``update_worker_heartbeat(...)``\n  * ``mark_worker_stopped(...)``\n'
- 'pas.worker.heartbeat_service'
- 'pas_worker_heartbeats'
- 'STARTING'
- 'RUNNING'
- 'error_code'
- 'worker_id'
- 'warnings'
- 'row'
- 'hostname'
- 'pid'
- 'status'
- 'metadata'
- 'now'
- 'Any'
- 'return'
- 'datetime'
- '+00:00'
- 'str'
- 'seconds'
- 'Lazy resolver for the Supabase client. NEVER raises.'
- 'heartbeat_service db client unavailable type='
- 'Dict[str, Any]'
- "Project arbitrary metadata down to the closed allow-list.\nNon-dict input collapses to {}. Any value that isn't a\nJSON-friendly scalar (int / float / str / bool / None) is\ndropped. NEVER raises."
- 'value'
- 'max_len'
- 'int'
- 'Optional[str]'
- 'missing_worker_id'
- 'worker_id_too_long'
- 'worker_type'
- 'invalid_worker_type'
- 'invalid_status'
- 'Optional[List[str]]'
- 'Optional[Dict[str, Any]]'
- 'Project a DB row into the structural envelope shape.\nNEVER returns columns outside the allow-list.'
- 'Optional[int]'
- 'Register a new worker heartbeat row. If the worker_id\nalready exists, the row is updated (idempotent).\n\nReturns a structural envelope. NEVER raises. NEVER returns\nraw metadata; values outside the allow-list are dropped.\n'
- 'failed'
- 'skipped'
- 'heartbeat_store_unavailable'
- 'started_at'
- 'last_heartbeat_at'
- 'data'
- 'register_worker_heartbeat update error type='
- 'db_write_failed:'
- 'register_worker_heartbeat insert error type='
- 'Stamp ``last_heartbeat_at`` and (optionally) update the\nstatus + metadata. Returns a structural envelope. NEVER\nraises.\n\nWorkers should call this on every tick of their loop (or\nevery N ticks, operator-tunable). The PAS162 worker calls\nit opt-in only.\n'
- 'heartbeat_row_not_found'
- 'update_worker_heartbeat db error type='
- 'Transition a worker to ``STOPPED``. Idempotent — calling\ntwice is safe. NEVER raises.\n\nWorkers should call this from a SIGTERM / KeyboardInterrupt\nhandler so the heartbeat row reflects an orderly shutdown.\n'
- 'STOPPED'
- 'exc'
- 'BaseException'
- 'bool'
- '23505'
- 'duplicate key value violates unique constraint'
- 'already exists'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS172 — Worker heartbeat service (Supabase-backed v1).\n\nOperator-facing minimum viable surface for "is the worker\nalive?". The PAS162 pending-call worker (and any future\nworker — callback reminder, operator reaper, monitoring\ndispatcher) may opt-in to heartbeat writes via:\n\n    register_worker_heartbeat(worker_id=..., worker_type=...)\n    update_worker_heartbeat(worker_id=..., metadata={...})\n    mark_worker_stopped(worker_id=...)\n\nDoctrine carried by every helper here:\n\n* **Writes are opt-in.** The PAS162 worker default-OFF\n  doctrine is unchanged — even when the worker IS started,\n  heartbeat writes only fire if the worker calls the helpers\n  explicitly. There is no auto-fire from any startup hook.\n* **No PII anywhere.** No phone / email / name / transcript /\n  raw_payload / summary / signature / dedupe_key. The\n  metadata dict is projected against a closed allow-list at\n  insert / update time; anything outside the list is\n  dropped.\n* **Closed-shape envelopes.** Every helper returns\n  ``{status, worker_id, warnings, error_code}``; reads add\n  ``rows`` / ``stale`` counters. NEVER raises.\n* **DB unavailable falls back to a structural ``status="skipped"``**\n  envelope so the worker continues running even when the\n  durable store is unreachable. This is the same\n  fallback-safe pattern as PAS166 / PAS171.\n* **Closed worker_type enum** mirroring the v20 SQL\n  CHECK constraint.\n* **Closed status enum** ``STARTING / RUNNING / DEGRADED /\n  STOPPED``.\n\nPublic surface:\n\n  * ``register_worker_heartbeat(...)``\n  * ``update_worker_heartbeat(...)``\n  * ``mark_worker_stopped(...)``\n')
              STORE_NAME               0 (__doc__)

 43           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 45           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 46           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              4 (os)
              STORE_NAME               4 (os)

 47           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('datetime', 'timezone'))
              IMPORT_NAME              5 (datetime)
              IMPORT_FROM              5 (datetime)
              STORE_NAME               5 (datetime)
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
              LOAD_CONST               5 ('pas.worker.heartbeat_service')
              CALL                     1
              STORE_NAME              13 (logger)

 54           LOAD_CONST               6 ('pas_worker_heartbeats')
              STORE_NAME              14 (_TABLE)

 56           LOAD_CONST              45 (('pending_call_worker', 'callback_reminder_worker', 'operator_reaper', 'monitoring_dispatcher'))
              STORE_NAME              15 (ALLOWED_WORKER_TYPES)

 63           LOAD_CONST              46 (('STARTING', 'RUNNING', 'DEGRADED', 'STOPPED'))
              STORE_NAME              16 (ALLOWED_STATUSES)

 72           LOAD_CONST              47 (('queue_depth', 'recovered_count', 'callback_due_count', 'warning_count', 'error_code', 'iteration_count', 'consecutive_failures'))
              STORE_NAME              17 (ALLOWED_METADATA_KEYS)

 83           LOAD_SMALL_INT         200
              STORE_NAME              18 (_WORKER_ID_MAX_LEN)

 84           LOAD_SMALL_INT         200
              STORE_NAME              19 (_HOSTNAME_MAX_LEN)

 91           LOAD_CONST              48 ((None,))
              LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA23D0, file "app/services/worker\heartbeat_service.py", line 91>)
              MAKE_FUNCTION
              LOAD_CONST              11 (<code object _now_dt at 0x0000018C17F7AEA0, file "app/services/worker\heartbeat_service.py", line 91>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              20 (_now_dt)

107           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA1E30, file "app/services/worker\heartbeat_service.py", line 107>)
              MAKE_FUNCTION
              LOAD_CONST              13 (<code object _iso at 0x0000018C18025F30, file "app/services/worker\heartbeat_service.py", line 107>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              21 (_iso)

111           LOAD_CONST              14 (<code object _get_db_safe at 0x0000018C17FF1230, file "app/services/worker\heartbeat_service.py", line 111>)
              MAKE_FUNCTION
              STORE_NAME              22 (_get_db_safe)

124           LOAD_CONST              15 (<code object __annotate__ at 0x0000018C17FA32D0, file "app/services/worker\heartbeat_service.py", line 124>)
              MAKE_FUNCTION
              LOAD_CONST              16 (<code object _project_metadata at 0x0000018C18060C00, file "app/services/worker\heartbeat_service.py", line 124>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              23 (_project_metadata)

141           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C18025930, file "app/services/worker\heartbeat_service.py", line 141>)
              MAKE_FUNCTION
              LOAD_CONST              18 (<code object _bound_str at 0x0000018C17972D90, file "app/services/worker\heartbeat_service.py", line 141>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              24 (_bound_str)

152           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA3A50, file "app/services/worker\heartbeat_service.py", line 152>)
              MAKE_FUNCTION
              LOAD_CONST              20 (<code object _validate_worker_id at 0x0000018C17972550, file "app/services/worker\heartbeat_service.py", line 152>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              25 (_validate_worker_id)

160           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA30F0, file "app/services/worker\heartbeat_service.py", line 160>)
              MAKE_FUNCTION
              LOAD_CONST              22 (<code object _validate_worker_type at 0x0000018C17FA33C0, file "app/services/worker\heartbeat_service.py", line 160>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              26 (_validate_worker_type)

166           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA1D40, file "app/services/worker\heartbeat_service.py", line 166>)
              MAKE_FUNCTION
              LOAD_CONST              24 (<code object _validate_status at 0x0000018C17FA3C30, file "app/services/worker\heartbeat_service.py", line 166>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              27 (_validate_status)

172           LOAD_CONST              25 ('worker_id')

175           LOAD_CONST               2 (None)

172           LOAD_CONST              26 ('warnings')

176           LOAD_CONST               2 (None)

172           LOAD_CONST               9 ('error_code')

177           LOAD_CONST               2 (None)

172           LOAD_CONST              27 ('row')

178           LOAD_CONST               2 (None)

172           BUILD_MAP                4
              LOAD_CONST              28 (<code object __annotate__ at 0x0000018C18025B30, file "app/services/worker\heartbeat_service.py", line 172>)
              MAKE_FUNCTION
              LOAD_CONST              29 (<code object _safe_envelope at 0x0000018C18053AB0, file "app/services/worker\heartbeat_service.py", line 172>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              28 (_safe_envelope)

191           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA21F0, file "app/services/worker\heartbeat_service.py", line 191>)
              MAKE_FUNCTION
              LOAD_CONST              31 (<code object _project_row at 0x0000018C1794E810, file "app/services/worker\heartbeat_service.py", line 191>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              29 (_project_row)

212           LOAD_CONST              32 ('hostname')

216           LOAD_CONST               2 (None)

212           LOAD_CONST              33 ('pid')

217           LOAD_CONST               2 (None)

212           LOAD_CONST              34 ('status')

218           LOAD_CONST               7 ('STARTING')

212           LOAD_CONST              35 ('metadata')

219           LOAD_CONST               2 (None)

212           LOAD_CONST              36 ('now')

220           LOAD_CONST               2 (None)

212           BUILD_MAP                5
              LOAD_CONST              37 (<code object __annotate__ at 0x0000018C18128690, file "app/services/worker\heartbeat_service.py", line 212>)
              MAKE_FUNCTION
              LOAD_CONST              38 (<code object register_worker_heartbeat at 0x0000018C181B3920, file "app/services/worker\heartbeat_service.py", line 212>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              30 (register_worker_heartbeat)

327           LOAD_CONST              34 ('status')

330           LOAD_CONST               8 ('RUNNING')

327           LOAD_CONST              35 ('metadata')

331           LOAD_CONST               2 (None)

327           LOAD_CONST              36 ('now')

332           LOAD_CONST               2 (None)

327           BUILD_MAP                3
              LOAD_CONST              39 (<code object __annotate__ at 0x0000018C18025830, file "app/services/worker\heartbeat_service.py", line 327>)
              MAKE_FUNCTION
              LOAD_CONST              40 (<code object update_worker_heartbeat at 0x0000018C182E4030, file "app/services/worker\heartbeat_service.py", line 327>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              31 (update_worker_heartbeat)

401           LOAD_CONST              35 ('metadata')

404           LOAD_CONST               2 (None)

401           LOAD_CONST              36 ('now')

405           LOAD_CONST               2 (None)

401           BUILD_MAP                2
              LOAD_CONST              41 (<code object __annotate__ at 0x0000018C18025530, file "app/services/worker\heartbeat_service.py", line 401>)
              MAKE_FUNCTION
              LOAD_CONST              42 (<code object mark_worker_stopped at 0x0000018C17FA3960, file "app/services/worker\heartbeat_service.py", line 401>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              32 (mark_worker_stopped)

423           LOAD_CONST              43 (<code object __annotate__ at 0x0000018C17FA2E20, file "app/services/worker\heartbeat_service.py", line 423>)
              MAKE_FUNCTION
              LOAD_CONST              44 (<code object _is_unique_violation at 0x0000018C17F96140, file "app/services/worker\heartbeat_service.py", line 423>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              33 (_is_unique_violation)

437           BUILD_LIST               0
              LOAD_CONST              49 (('ALLOWED_WORKER_TYPES', 'ALLOWED_STATUSES', 'ALLOWED_METADATA_KEYS', 'register_worker_heartbeat', 'update_worker_heartbeat', 'mark_worker_stopped'))
              LIST_EXTEND              1
              STORE_NAME              34 (__all__)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "app/services/worker\heartbeat_service.py", line 91>:
 91           RESUME                   0
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

Disassembly of <code object _now_dt at 0x0000018C17F7AEA0, file "app/services/worker\heartbeat_service.py", line 91>:
  91            RESUME                   0

  92            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (now)
                LOAD_GLOBAL              2 (datetime)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       78 (to L2)
                NOT_TAKEN

  93            LOAD_FAST_BORROW         0 (now)
                LOAD_ATTR                4 (tzinfo)
                POP_JUMP_IF_NOT_NONE    33 (to L1)
                NOT_TAKEN

  94            LOAD_FAST_BORROW         0 (now)
                LOAD_ATTR                7 (replace + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                LOAD_CONST               1 (('tzinfo',))
                CALL_KW                  1
                RETURN_VALUE

  95    L1:     LOAD_FAST_BORROW         0 (now)
                LOAD_ATTR               13 (astimezone + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                CALL                     1
                RETURN_VALUE

  96    L2:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (now)
                LOAD_GLOBAL             14 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      117 (to L6)
                NOT_TAKEN

  97            NOP

  98    L3:     LOAD_GLOBAL              2 (datetime)
                LOAD_ATTR               16 (fromisoformat)
                PUSH_NULL
                LOAD_FAST_BORROW         0 (now)
                LOAD_ATTR                7 (replace + NULL|self)
                LOAD_CONST               2 ('Z')
                LOAD_CONST               3 ('+00:00')
                CALL                     2
                CALL                     1
                STORE_FAST               1 (dt)

  99            LOAD_FAST_BORROW         1 (dt)
                LOAD_ATTR                4 (tzinfo)
                POP_JUMP_IF_NOT_NONE    33 (to L4)
                NOT_TAKEN

 100            LOAD_FAST_BORROW         1 (dt)
                LOAD_ATTR                7 (replace + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                LOAD_CONST               1 (('tzinfo',))
                CALL_KW                  1
                STORE_FAST               1 (dt)

 101    L4:     LOAD_FAST_BORROW         1 (dt)
                LOAD_ATTR               13 (astimezone + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                CALL                     1
        L5:     RETURN_VALUE

 104    L6:     LOAD_GLOBAL              2 (datetime)
                LOAD_ATTR               20 (now)
                PUSH_NULL
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                CALL                     1
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

 102            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        4 (to L9)
                NOT_TAKEN
                POP_TOP

 103    L8:     POP_EXCEPT
                JUMP_BACKWARD_NO_INTERRUPT 49 (to L6)

 102    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L5 -> L7 [0]
  L7 to L8 -> L10 [1] lasti
  L9 to L10 -> L10 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "app/services/worker\heartbeat_service.py", line 107>:
107           RESUME                   0
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

Disassembly of <code object _iso at 0x0000018C18025F30, file "app/services/worker\heartbeat_service.py", line 107>:
107           RESUME                   0

108           LOAD_FAST_BORROW         0 (dt)
              LOAD_ATTR                1 (isoformat + NULL|self)
              LOAD_CONST               0 ('seconds')
              LOAD_CONST               1 (('timespec',))
              CALL_KW                  1
              RETURN_VALUE

Disassembly of <code object _get_db_safe at 0x0000018C17FF1230, file "app/services/worker\heartbeat_service.py", line 111>:
 111           RESUME                   0

 113           NOP

 114   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('get_supabase',))
               IMPORT_NAME              0 (app.db.supabase_client)
               IMPORT_FROM              1 (get_supabase)
               STORE_FAST               0 (get_supabase)
               POP_TOP

 115           LOAD_FAST_BORROW         0 (get_supabase)
               PUSH_NULL
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 116           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       55 (to L7)
               NOT_TAKEN
               STORE_FAST               1 (e)

 117   L4:     LOAD_GLOBAL              6 (logger)
               LOAD_ATTR                9 (warning + NULL|self)

 118           LOAD_CONST               2 ('heartbeat_service db client unavailable type=')

 119           LOAD_GLOBAL             11 (type + NULL)
               LOAD_FAST                1 (e)
               CALL                     1
               LOAD_ATTR               12 (__name__)
               FORMAT_SIMPLE

 118           BUILD_STRING             2

 117           CALL                     1
               POP_TOP

 121   L5:     POP_EXCEPT
               LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               LOAD_CONST               3 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               RERAISE                  1

 116   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA32D0, file "app/services/worker\heartbeat_service.py", line 124>:
124           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('metadata')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _project_metadata at 0x0000018C18060C00, file "app/services/worker\heartbeat_service.py", line 124>:
124           RESUME                   0

129           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (metadata)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

130           BUILD_MAP                0
              RETURN_VALUE

131   L1:     BUILD_MAP                0
              STORE_FAST               1 (out)

132           LOAD_GLOBAL              4 (ALLOWED_METADATA_KEYS)
              GET_ITER
      L2:     FOR_ITER                67 (to L5)
              STORE_FAST               2 (key)

133           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (key, metadata)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

134           JUMP_BACKWARD           11 (to L2)

135   L3:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (metadata, key)
              BINARY_OP               26 ([])
              STORE_FAST               3 (val)

136           LOAD_FAST_BORROW         3 (val)
              POP_JUMP_IF_NONE        41 (to L4)
              NOT_TAKEN
              LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         3 (val)
              LOAD_GLOBAL              6 (int)
              LOAD_GLOBAL              8 (float)
              LOAD_GLOBAL             10 (str)
              LOAD_GLOBAL             12 (bool)
              BUILD_TUPLE              4
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN
              JUMP_BACKWARD           63 (to L2)

137   L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (val, out)
              LOAD_FAST_BORROW         2 (key)
              STORE_SUBSCR
              JUMP_BACKWARD           69 (to L2)

132   L5:     END_FOR
              POP_ITER

138           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025930, file "app/services/worker\heartbeat_service.py", line 141>:
141           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('value')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('max_len')
              LOAD_CONST               4 ('int')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('Optional[str]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _bound_str at 0x0000018C17972D90, file "app/services/worker\heartbeat_service.py", line 141>:
141           RESUME                   0

142           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

143           LOAD_CONST               0 (None)
              RETURN_VALUE

144   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               2 (s)

145           LOAD_FAST_BORROW         2 (s)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

146           LOAD_CONST               0 (None)
              RETURN_VALUE

147   L2:     LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         2 (s)
              CALL                     1
              LOAD_FAST_BORROW         1 (max_len)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

148           LOAD_CONST               0 (None)
              RETURN_VALUE

149   L3:     LOAD_FAST_BORROW         2 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "app/services/worker\heartbeat_service.py", line 152>:
152           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('worker_id')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _validate_worker_id at 0x0000018C17972550, file "app/services/worker\heartbeat_service.py", line 152>:
152           RESUME                   0

153           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (worker_id)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       23 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         0 (worker_id)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

154   L1:     LOAD_CONST               0 ('missing_worker_id')
              RETURN_VALUE

155   L2:     LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         0 (worker_id)
              CALL                     1
              LOAD_GLOBAL              8 (_WORKER_ID_MAX_LEN)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

156           LOAD_CONST               1 ('worker_id_too_long')
              RETURN_VALUE

157   L3:     LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA30F0, file "app/services/worker\heartbeat_service.py", line 160>:
160           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('worker_type')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _validate_worker_type at 0x0000018C17FA33C0, file "app/services/worker\heartbeat_service.py", line 160>:
160           RESUME                   0

161           LOAD_FAST_BORROW         0 (worker_type)
              LOAD_GLOBAL              0 (ALLOWED_WORKER_TYPES)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN

162           LOAD_CONST               0 ('invalid_worker_type')
              RETURN_VALUE

163   L1:     LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1D40, file "app/services/worker\heartbeat_service.py", line 166>:
166           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _validate_status at 0x0000018C17FA3C30, file "app/services/worker\heartbeat_service.py", line 166>:
166           RESUME                   0

167           LOAD_FAST_BORROW         0 (status)
              LOAD_GLOBAL              0 (ALLOWED_STATUSES)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN

168           LOAD_CONST               0 ('invalid_status')
              RETURN_VALUE

169   L1:     LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025B30, file "app/services/worker\heartbeat_service.py", line 172>:
172           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')

174           LOAD_CONST               2 ('str')

172           LOAD_CONST               3 ('worker_id')

175           LOAD_CONST               4 ('Optional[str]')

172           LOAD_CONST               5 ('warnings')

176           LOAD_CONST               6 ('Optional[List[str]]')

172           LOAD_CONST               7 ('error_code')

177           LOAD_CONST               4 ('Optional[str]')

172           LOAD_CONST               8 ('row')

178           LOAD_CONST               9 ('Optional[Dict[str, Any]]')

172           LOAD_CONST              10 ('return')

179           LOAD_CONST              11 ('Dict[str, Any]')

172           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _safe_envelope at 0x0000018C18053AB0, file "app/services/worker\heartbeat_service.py", line 172>:
172           RESUME                   0

181           LOAD_CONST               0 ('status')
              LOAD_FAST                0 (status)

182           LOAD_CONST               1 ('worker_id')
              LOAD_FAST                1 (worker_id)

183           LOAD_CONST               2 ('warnings')
              LOAD_GLOBAL              1 (list + NULL)
              LOAD_FAST                2 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

184           LOAD_CONST               3 ('error_code')
              LOAD_FAST_BORROW         3 (error_code)

180           BUILD_MAP                4
              STORE_FAST               5 (env)

186           LOAD_FAST_BORROW         4 (row)
              POP_JUMP_IF_NONE         5 (to L2)
              NOT_TAKEN

187           LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (row, env)
              LOAD_CONST               4 ('row')
              STORE_SUBSCR

188   L2:     LOAD_FAST_BORROW         5 (env)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "app/services/worker\heartbeat_service.py", line 191>:
191           RESUME                   0
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
              LOAD_CONST               4 ('Optional[Dict[str, Any]]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _project_row at 0x0000018C1794E810, file "app/services/worker\heartbeat_service.py", line 191>:
191           RESUME                   0

194           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (row)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

195           LOAD_CONST               1 (None)
              RETURN_VALUE

196   L1:     BUILD_MAP                0
              STORE_FAST               1 (out)

197           LOAD_CONST               3 (('worker_id', 'worker_type', 'hostname', 'pid', 'started_at', 'last_heartbeat_at', 'status'))
              GET_ITER
      L2:     FOR_ITER                21 (to L4)
              STORE_FAST               2 (col)

201           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (col, row)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

202   L3:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (row, col)
              BINARY_OP               26 ([])
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (out, col)
              STORE_SUBSCR
              JUMP_BACKWARD           23 (to L2)

197   L4:     END_FOR
              POP_ITER

203           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (row)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               2 ('metadata')
              CALL                     1
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       18 (to L5)
              NOT_TAKEN
              LOAD_FAST_BORROW         0 (row)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               2 ('metadata')
              CALL                     1
              JUMP_FORWARD             1 (to L6)
      L5:     BUILD_MAP                0
      L6:     STORE_FAST               3 (md)

204           LOAD_GLOBAL              7 (_project_metadata + NULL)
              LOAD_FAST_BORROW         3 (md)
              CALL                     1
              LOAD_FAST_BORROW         1 (out)
              LOAD_CONST               2 ('metadata')
              STORE_SUBSCR

205           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18128690, file "app/services/worker\heartbeat_service.py", line 212>:
212           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('worker_id')

214           LOAD_CONST               2 ('str')

212           LOAD_CONST               3 ('worker_type')

215           LOAD_CONST               2 ('str')

212           LOAD_CONST               4 ('hostname')

216           LOAD_CONST               5 ('Optional[str]')

212           LOAD_CONST               6 ('pid')

217           LOAD_CONST               7 ('Optional[int]')

212           LOAD_CONST               8 ('status')

218           LOAD_CONST               2 ('str')

212           LOAD_CONST               9 ('metadata')

219           LOAD_CONST              10 ('Optional[Dict[str, Any]]')

212           LOAD_CONST              11 ('now')

220           LOAD_CONST              12 ('Any')

212           LOAD_CONST              13 ('return')

221           LOAD_CONST              14 ('Dict[str, Any]')

212           BUILD_MAP                8
              RETURN_VALUE

Disassembly of <code object register_worker_heartbeat at 0x0000018C181B3920, file "app/services/worker\heartbeat_service.py", line 212>:
 212            RESUME                   0

 229            LOAD_GLOBAL              1 (_validate_worker_id + NULL)
                LOAD_FAST_BORROW         0 (worker_id)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        31 (to L1)
                NOT_TAKEN
                POP_TOP

 230            LOAD_GLOBAL              3 (_validate_worker_type + NULL)
                LOAD_FAST_BORROW         1 (worker_type)
                CALL                     1

 229            COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        12 (to L1)
                NOT_TAKEN
                POP_TOP

 231            LOAD_GLOBAL              5 (_validate_status + NULL)
                LOAD_FAST_BORROW         4 (status)
                CALL                     1

 228    L1:     STORE_FAST               7 (err)

 233            LOAD_FAST_BORROW         7 (err)
                POP_JUMP_IF_NONE        45 (to L3)
                NOT_TAKEN

 234            LOAD_GLOBAL              7 (_safe_envelope + NULL)

 235            LOAD_CONST               2 ('failed')

 236            LOAD_GLOBAL              9 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (worker_id)
                LOAD_GLOBAL             10 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        9 (to L2)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (worker_id)

 237            LOAD_FAST_BORROW         7 (err)

 234            LOAD_CONST               3 (('status', 'worker_id', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 236    L2:     LOAD_CONST               1 (None)

 237            LOAD_FAST_BORROW         7 (err)

 234            LOAD_CONST               3 (('status', 'worker_id', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 240    L3:     LOAD_FAST_BORROW         0 (worker_id)
                LOAD_ATTR               13 (strip + NULL|self)
                CALL                     0
                STORE_FAST               8 (wid)

 241            LOAD_GLOBAL             15 (_bound_str + NULL)
                LOAD_FAST_BORROW         2 (hostname)
                LOAD_GLOBAL             16 (_HOSTNAME_MAX_LEN)
                CALL                     2
                STORE_FAST               9 (host)

 242            NOP

 243    L4:     LOAD_FAST_BORROW         3 (pid)
                POP_JUMP_IF_NONE        12 (to L5)
                NOT_TAKEN
                LOAD_GLOBAL             19 (int + NULL)
                LOAD_FAST_BORROW         3 (pid)
                CALL                     1
                JUMP_FORWARD             1 (to L6)
        L5:     LOAD_CONST               1 (None)
        L6:     STORE_FAST              10 (pid_i)

 244            LOAD_FAST_BORROW        10 (pid_i)
                POP_JUMP_IF_NONE        10 (to L7)
                NOT_TAKEN
                LOAD_FAST_BORROW        10 (pid_i)
                LOAD_SMALL_INT           0
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        3 (to L7)
                NOT_TAKEN

 245            LOAD_CONST               1 (None)
                STORE_FAST              10 (pid_i)

 248    L7:     LOAD_GLOBAL             25 (_now_dt + NULL)
                LOAD_FAST                6 (now)
                CALL                     1
                STORE_FAST              11 (now_dt)

 249            LOAD_GLOBAL             27 (_iso + NULL)
                LOAD_FAST               11 (now_dt)
                CALL                     1
                STORE_FAST              12 (iso_now)

 251            LOAD_GLOBAL             29 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST              13 (db)

 252            LOAD_FAST               13 (db)
                POP_JUMP_IF_NOT_NONE    17 (to L8)
                NOT_TAKEN

 253            LOAD_GLOBAL              7 (_safe_envelope + NULL)

 254            LOAD_CONST               4 ('skipped')

 255            LOAD_FAST                8 (wid)

 256            LOAD_CONST               5 ('heartbeat_store_unavailable')
                BUILD_LIST               1

 257            LOAD_CONST               5 ('heartbeat_store_unavailable')

 253            LOAD_CONST               6 (('status', 'worker_id', 'warnings', 'error_code'))
                CALL_KW                  4
                RETURN_VALUE

 261    L8:     LOAD_CONST               7 ('worker_id')
                LOAD_FAST                8 (wid)

 262            LOAD_CONST               8 ('worker_type')
                LOAD_FAST                1 (worker_type)

 263            LOAD_CONST               9 ('hostname')
                LOAD_FAST                9 (host)

 264            LOAD_CONST              10 ('pid')
                LOAD_FAST               10 (pid_i)

 265            LOAD_CONST              11 ('started_at')
                LOAD_FAST               12 (iso_now)

 266            LOAD_CONST              12 ('last_heartbeat_at')
                LOAD_FAST               12 (iso_now)

 267            LOAD_CONST              13 ('status')
                LOAD_FAST                4 (status)

 268            LOAD_CONST              14 ('metadata')
                LOAD_GLOBAL             31 (_project_metadata + NULL)
                LOAD_FAST                5 (metadata)
                CALL                     1

 260            BUILD_MAP                8
                STORE_FAST              14 (row)

 273            NOP

 274    L9:     LOAD_FAST               13 (db)
                LOAD_ATTR               33 (table + NULL|self)
                LOAD_GLOBAL             34 (_TABLE)
                CALL                     1
                LOAD_ATTR               37 (insert + NULL|self)
                LOAD_FAST               14 (row)
                CALL                     1
                LOAD_ATTR               39 (execute + NULL|self)
                CALL                     0
                STORE_FAST              15 (result)

 275            LOAD_GLOBAL             41 (list + NULL)
                LOAD_GLOBAL             43 (getattr + NULL)
                LOAD_FAST               15 (result)
                LOAD_CONST              15 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
       L10:     CALL                     1
                STORE_FAST              16 (inserted)

 276            LOAD_FAST               16 (inserted)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L13)
       L11:     NOT_TAKEN
       L12:     LOAD_GLOBAL             45 (_project_row + NULL)
                LOAD_FAST               16 (inserted)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                CALL                     1
                JUMP_FORWARD            10 (to L14)
       L13:     LOAD_GLOBAL             45 (_project_row + NULL)
                LOAD_FAST               14 (row)
                CALL                     1
       L14:     STORE_FAST              17 (proj)

 277            LOAD_GLOBAL              7 (_safe_envelope + NULL)

 278            LOAD_CONST              16 ('ok')
                LOAD_FAST                8 (wid)
                LOAD_FAST               17 (proj)

 277            LOAD_CONST              17 (('status', 'worker_id', 'row'))
                CALL_KW                  3
       L15:     RETURN_VALUE

  --   L16:     PUSH_EXC_INFO

 246            LOAD_GLOBAL             20 (TypeError)
                LOAD_GLOBAL             22 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L18)
                NOT_TAKEN
                POP_TOP

 247            LOAD_CONST               1 (None)
                STORE_FAST              10 (pid_i)
       L17:     POP_EXCEPT
                JUMP_BACKWARD_NO_INTERRUPT 234 (to L7)

 246   L18:     RERAISE                  0

  --   L19:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L20:     PUSH_EXC_INFO

 280            LOAD_GLOBAL             46 (Exception)
                CHECK_EXC_MATCH
                EXTENDED_ARG             1
                POP_JUMP_IF_FALSE      389 (to L44)
                NOT_TAKEN
                STORE_FAST              18 (e)

 281   L21:     LOAD_GLOBAL             49 (_is_unique_violation + NULL)
                LOAD_FAST               18 (e)
                CALL                     1
                TO_BOOL
                EXTENDED_ARG             1
                POP_JUMP_IF_FALSE      280 (to L40)
                NOT_TAKEN

 285            LOAD_CONST               8 ('worker_type')
                LOAD_FAST                1 (worker_type)

 286            LOAD_CONST               9 ('hostname')
                LOAD_FAST                9 (host)

 287            LOAD_CONST              10 ('pid')
                LOAD_FAST               10 (pid_i)

 288            LOAD_CONST              12 ('last_heartbeat_at')
                LOAD_FAST               12 (iso_now)

 289            LOAD_CONST              13 ('status')
                LOAD_FAST                4 (status)

 290            LOAD_CONST              14 ('metadata')
                LOAD_GLOBAL             31 (_project_metadata + NULL)
                LOAD_FAST                5 (metadata)
                CALL                     1

 284            BUILD_MAP                6
                STORE_FAST              19 (patch)

 292   L22:     NOP

 294   L23:     LOAD_FAST               13 (db)
                LOAD_ATTR               33 (table + NULL|self)
                LOAD_GLOBAL             34 (_TABLE)
                CALL                     1

 295            LOAD_ATTR               51 (update + NULL|self)
                LOAD_FAST               19 (patch)
                CALL                     1

 296            LOAD_ATTR               53 (eq + NULL|self)
                LOAD_CONST               7 ('worker_id')
                LOAD_FAST                8 (wid)
                CALL                     2

 297            LOAD_ATTR               39 (execute + NULL|self)
                CALL                     0

 293            STORE_FAST              15 (result)

 299            LOAD_GLOBAL             41 (list + NULL)
                LOAD_GLOBAL             43 (getattr + NULL)
                LOAD_FAST               15 (result)
                LOAD_CONST              15 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L24)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
       L24:     CALL                     1
                STORE_FAST              20 (updated)

 300            LOAD_FAST               20 (updated)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L27)
       L25:     NOT_TAKEN
       L26:     LOAD_GLOBAL             45 (_project_row + NULL)
                LOAD_FAST               20 (updated)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                CALL                     1
                JUMP_FORWARD             1 (to L28)
       L27:     LOAD_CONST               1 (None)
       L28:     STORE_FAST              17 (proj)

 301            LOAD_GLOBAL              7 (_safe_envelope + NULL)

 302            LOAD_CONST              16 ('ok')
                LOAD_FAST                8 (wid)
                LOAD_FAST               17 (proj)

 301            LOAD_CONST              17 (('status', 'worker_id', 'row'))
                CALL_KW                  3
       L29:     SWAP                     2
       L30:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              18 (e)
                DELETE_FAST             18 (e)
                RETURN_VALUE

  --   L31:     PUSH_EXC_INFO

 304            LOAD_GLOBAL             46 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       97 (to L38)
                NOT_TAKEN
                STORE_FAST              21 (e2)

 305   L32:     LOAD_GLOBAL             54 (logger)
                LOAD_ATTR               57 (warning + NULL|self)

 306            LOAD_CONST              18 ('register_worker_heartbeat update error type=')

 307            LOAD_GLOBAL             59 (type + NULL)
                LOAD_FAST               21 (e2)
                CALL                     1
                LOAD_ATTR               60 (__name__)
                FORMAT_SIMPLE

 306            BUILD_STRING             2

 305            CALL                     1
                POP_TOP

 309            LOAD_GLOBAL              7 (_safe_envelope + NULL)

 310            LOAD_CONST               4 ('skipped')

 311            LOAD_FAST                8 (wid)

 312            LOAD_CONST              19 ('db_write_failed:')
                LOAD_GLOBAL             59 (type + NULL)
                LOAD_FAST               21 (e2)
                CALL                     1
                LOAD_ATTR               60 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 313            LOAD_CONST               5 ('heartbeat_store_unavailable')

 309            LOAD_CONST               6 (('status', 'worker_id', 'warnings', 'error_code'))
                CALL_KW                  4
       L33:     SWAP                     2
       L34:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              21 (e2)
                DELETE_FAST             21 (e2)
       L35:     SWAP                     2
       L36:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              18 (e)
                DELETE_FAST             18 (e)
                RETURN_VALUE

  --   L37:     LOAD_CONST               1 (None)
                STORE_FAST              21 (e2)
                DELETE_FAST             21 (e2)
                RERAISE                  1

 304   L38:     RERAISE                  0

  --   L39:     COPY                     3
                POP_EXCEPT
                RERAISE                  1

 315   L40:     LOAD_GLOBAL             54 (logger)
                LOAD_ATTR               57 (warning + NULL|self)

 316            LOAD_CONST              20 ('register_worker_heartbeat insert error type=')

 317            LOAD_GLOBAL             59 (type + NULL)
                LOAD_FAST               18 (e)
                CALL                     1
                LOAD_ATTR               60 (__name__)
                FORMAT_SIMPLE

 316            BUILD_STRING             2

 315            CALL                     1
                POP_TOP

 319            LOAD_GLOBAL              7 (_safe_envelope + NULL)

 320            LOAD_CONST               4 ('skipped')

 321            LOAD_FAST                8 (wid)

 322            LOAD_CONST              19 ('db_write_failed:')
                LOAD_GLOBAL             59 (type + NULL)
                LOAD_FAST               18 (e)
                CALL                     1
                LOAD_ATTR               60 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 323            LOAD_CONST               5 ('heartbeat_store_unavailable')

 319            LOAD_CONST               6 (('status', 'worker_id', 'warnings', 'error_code'))
                CALL_KW                  4
       L41:     SWAP                     2
       L42:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              18 (e)
                DELETE_FAST             18 (e)
                RETURN_VALUE

  --   L43:     LOAD_CONST               1 (None)
                STORE_FAST              18 (e)
                DELETE_FAST             18 (e)
                RERAISE                  1

 280   L44:     RERAISE                  0

  --   L45:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L4 to L7 -> L16 [0]
  L9 to L11 -> L20 [0]
  L12 to L15 -> L20 [0]
  L16 to L17 -> L19 [1] lasti
  L18 to L19 -> L19 [1] lasti
  L20 to L21 -> L45 [1] lasti
  L21 to L22 -> L43 [1] lasti
  L23 to L25 -> L31 [1]
  L26 to L29 -> L31 [1]
  L29 to L30 -> L45 [1] lasti
  L31 to L32 -> L39 [2] lasti
  L32 to L33 -> L37 [2] lasti
  L33 to L34 -> L39 [2] lasti
  L34 to L35 -> L43 [1] lasti
  L35 to L36 -> L45 [1] lasti
  L37 to L39 -> L39 [2] lasti
  L39 to L41 -> L43 [1] lasti
  L41 to L42 -> L45 [1] lasti
  L43 to L45 -> L45 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025830, file "app/services/worker\heartbeat_service.py", line 327>:
327           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('worker_id')

329           LOAD_CONST               2 ('str')

327           LOAD_CONST               3 ('status')

330           LOAD_CONST               2 ('str')

327           LOAD_CONST               4 ('metadata')

331           LOAD_CONST               5 ('Optional[Dict[str, Any]]')

327           LOAD_CONST               6 ('now')

332           LOAD_CONST               7 ('Any')

327           LOAD_CONST               8 ('return')

333           LOAD_CONST               9 ('Dict[str, Any]')

327           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object update_worker_heartbeat at 0x0000018C182E4030, file "app/services/worker\heartbeat_service.py", line 327>:
 327            RESUME                   0

 342            LOAD_GLOBAL              1 (_validate_worker_id + NULL)
                LOAD_FAST_BORROW         0 (worker_id)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        12 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_GLOBAL              3 (_validate_status + NULL)
                LOAD_FAST_BORROW         1 (status)
                CALL                     1
        L1:     STORE_FAST               4 (err)

 343            LOAD_FAST_BORROW         4 (err)
                POP_JUMP_IF_NONE        45 (to L3)
                NOT_TAKEN

 344            LOAD_GLOBAL              5 (_safe_envelope + NULL)

 345            LOAD_CONST               2 ('failed')

 346            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (worker_id)
                LOAD_GLOBAL              8 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        9 (to L2)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (worker_id)

 347            LOAD_FAST_BORROW         4 (err)

 344            LOAD_CONST               3 (('status', 'worker_id', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 346    L2:     LOAD_CONST               1 (None)

 347            LOAD_FAST_BORROW         4 (err)

 344            LOAD_CONST               3 (('status', 'worker_id', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 350    L3:     LOAD_FAST_BORROW         0 (worker_id)
                LOAD_ATTR               11 (strip + NULL|self)
                CALL                     0
                STORE_FAST               5 (wid)

 351            LOAD_GLOBAL             13 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               6 (db)

 352            LOAD_FAST_BORROW         6 (db)
                POP_JUMP_IF_NOT_NONE    17 (to L4)
                NOT_TAKEN

 353            LOAD_GLOBAL              5 (_safe_envelope + NULL)

 354            LOAD_CONST               4 ('skipped')

 355            LOAD_FAST_BORROW         5 (wid)

 356            LOAD_CONST               5 ('heartbeat_store_unavailable')
                BUILD_LIST               1

 357            LOAD_CONST               5 ('heartbeat_store_unavailable')

 353            LOAD_CONST               6 (('status', 'worker_id', 'warnings', 'error_code'))
                CALL_KW                  4
                RETURN_VALUE

 360    L4:     LOAD_GLOBAL             15 (_iso + NULL)
                LOAD_GLOBAL             17 (_now_dt + NULL)
                LOAD_FAST_BORROW         3 (now)
                CALL                     1
                CALL                     1
                STORE_FAST               7 (iso_now)

 362            LOAD_CONST               7 ('status')
                LOAD_FAST_BORROW         1 (status)

 363            LOAD_CONST               8 ('last_heartbeat_at')
                LOAD_FAST_BORROW         7 (iso_now)

 361            BUILD_MAP                2
                STORE_FAST               8 (patch)

 365            LOAD_GLOBAL             19 (_project_metadata + NULL)
                LOAD_FAST_BORROW         2 (metadata)
                CALL                     1
                STORE_FAST               9 (projected_md)

 366            LOAD_FAST_BORROW         9 (projected_md)
                TO_BOOL
                POP_JUMP_IF_FALSE        5 (to L5)
                NOT_TAKEN

 367            LOAD_FAST_BORROW_LOAD_FAST_BORROW 152 (projected_md, patch)
                LOAD_CONST               9 ('metadata')
                STORE_SUBSCR

 369    L5:     NOP

 371    L6:     LOAD_FAST_BORROW         6 (db)
                LOAD_ATTR               21 (table + NULL|self)
                LOAD_GLOBAL             22 (_TABLE)
                CALL                     1

 372            LOAD_ATTR               25 (update + NULL|self)
                LOAD_FAST_BORROW         8 (patch)
                CALL                     1

 373            LOAD_ATTR               27 (eq + NULL|self)
                LOAD_CONST              10 ('worker_id')
                LOAD_FAST_BORROW         5 (wid)
                CALL                     2

 374            LOAD_ATTR               29 (execute + NULL|self)
                CALL                     0

 370            STORE_FAST              10 (result)

 376            LOAD_GLOBAL             31 (list + NULL)
                LOAD_GLOBAL             33 (getattr + NULL)
                LOAD_FAST_BORROW        10 (result)
                LOAD_CONST              11 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
        L7:     NOT_TAKEN
        L8:     POP_TOP
                BUILD_LIST               0
        L9:     CALL                     1
                STORE_FAST              11 (updated)

 377            LOAD_FAST_BORROW        11 (updated)
                TO_BOOL
                POP_JUMP_IF_TRUE        17 (to L13)
       L10:     NOT_TAKEN

 378   L11:     LOAD_GLOBAL              5 (_safe_envelope + NULL)

 379            LOAD_CONST               4 ('skipped')

 380            LOAD_FAST_BORROW         5 (wid)

 381            LOAD_CONST              12 ('heartbeat_row_not_found')
                BUILD_LIST               1

 382            LOAD_CONST              12 ('heartbeat_row_not_found')

 378            LOAD_CONST               6 (('status', 'worker_id', 'warnings', 'error_code'))
                CALL_KW                  4
       L12:     RETURN_VALUE

 384   L13:     LOAD_GLOBAL              5 (_safe_envelope + NULL)

 385            LOAD_CONST              13 ('ok')

 386            LOAD_FAST_BORROW         5 (wid)

 387            LOAD_GLOBAL             35 (_project_row + NULL)
                LOAD_FAST_BORROW        11 (updated)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                CALL                     1

 384            LOAD_CONST              14 (('status', 'worker_id', 'row'))
                CALL_KW                  3
       L14:     RETURN_VALUE

  --   L15:     PUSH_EXC_INFO

 389            LOAD_GLOBAL             36 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       92 (to L20)
                NOT_TAKEN
                STORE_FAST              12 (e)

 390   L16:     LOAD_GLOBAL             38 (logger)
                LOAD_ATTR               41 (warning + NULL|self)

 391            LOAD_CONST              15 ('update_worker_heartbeat db error type=')
                LOAD_GLOBAL             43 (type + NULL)
                LOAD_FAST               12 (e)
                CALL                     1
                LOAD_ATTR               44 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 390            CALL                     1
                POP_TOP

 393            LOAD_GLOBAL              5 (_safe_envelope + NULL)

 394            LOAD_CONST               4 ('skipped')

 395            LOAD_FAST                5 (wid)

 396            LOAD_CONST              16 ('db_write_failed:')
                LOAD_GLOBAL             43 (type + NULL)
                LOAD_FAST               12 (e)
                CALL                     1
                LOAD_ATTR               44 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 397            LOAD_CONST               5 ('heartbeat_store_unavailable')

 393            LOAD_CONST               6 (('status', 'worker_id', 'warnings', 'error_code'))
                CALL_KW                  4
       L17:     SWAP                     2
       L18:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              12 (e)
                DELETE_FAST             12 (e)
                RETURN_VALUE

  --   L19:     LOAD_CONST               1 (None)
                STORE_FAST              12 (e)
                DELETE_FAST             12 (e)
                RERAISE                  1

 389   L20:     RERAISE                  0

  --   L21:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L6 to L7 -> L15 [0]
  L8 to L10 -> L15 [0]
  L11 to L12 -> L15 [0]
  L13 to L14 -> L15 [0]
  L15 to L16 -> L21 [1] lasti
  L16 to L17 -> L19 [1] lasti
  L17 to L18 -> L21 [1] lasti
  L19 to L21 -> L21 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025530, file "app/services/worker\heartbeat_service.py", line 401>:
401           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('worker_id')

403           LOAD_CONST               2 ('str')

401           LOAD_CONST               3 ('metadata')

404           LOAD_CONST               4 ('Optional[Dict[str, Any]]')

401           LOAD_CONST               5 ('now')

405           LOAD_CONST               6 ('Any')

401           LOAD_CONST               7 ('return')

406           LOAD_CONST               8 ('Dict[str, Any]')

401           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object mark_worker_stopped at 0x0000018C17FA3960, file "app/services/worker\heartbeat_service.py", line 401>:
401           RESUME                   0

413           LOAD_GLOBAL              1 (update_worker_heartbeat + NULL)

414           LOAD_FAST_BORROW         0 (worker_id)
              LOAD_CONST               1 ('STOPPED')

415           LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (metadata, now)

413           LOAD_CONST               2 (('worker_id', 'status', 'metadata', 'now'))
              CALL_KW                  4
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "app/services/worker\heartbeat_service.py", line 423>:
423           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('exc')
              LOAD_CONST               2 ('BaseException')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _is_unique_violation at 0x0000018C17F96140, file "app/services/worker\heartbeat_service.py", line 423>:
 423           RESUME                   0

 424           NOP

 425   L1:     LOAD_GLOBAL              1 (repr + NULL)
               LOAD_FAST_BORROW         0 (exc)
               CALL                     1
               STORE_FAST               1 (s)

 428   L2:     LOAD_CONST               1 ('23505')
               LOAD_FAST                1 (s)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 429           LOAD_CONST               2 (True)
               RETURN_VALUE

 430   L3:     LOAD_FAST                1 (s)
               LOAD_ATTR                5 (lower + NULL|self)
               CALL                     0
               STORE_FAST               2 (lowered)

 432           LOAD_CONST               3 ('duplicate key value violates unique constraint')
               LOAD_FAST                2 (lowered)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L4)
               NOT_TAKEN
               POP_TOP

 433           LOAD_CONST               4 ('already exists')
               LOAD_FAST                2 (lowered)
               CONTAINS_OP              0 (in)

 431   L4:     RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 426           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L7)
               NOT_TAKEN
               POP_TOP

 427   L6:     POP_EXCEPT
               LOAD_CONST               0 (False)
               RETURN_VALUE

 426   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti
```
