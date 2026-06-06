# worker/heartbeat_monitor

- **pyc:** `app\services\worker\__pycache__\heartbeat_monitor.cpython-314.pyc`
- **expected source path (absent):** `app\services\worker/heartbeat_monitor.py`
- **co_filename (from bytecode):** `app/services/worker\heartbeat_monitor.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** worker

## Module docstring

```
PAS172 — Worker heartbeat monitor (read-only).

Operator-facing reader for the durable worker-heartbeat table.
Produces structural reports that the PAS172 Slack employee-mode
block builders and the operator ops routes consume.

Doctrine carried by every helper here:

* **Read-only.** No writes; no DELETEs; no state transitions.
* **No exception escapes.** DB unreachable → ``status="skipped"``
  envelope with the structural warning. Never raises.
* **No PII.** Workers don't carry PII (their schema forbids
  it), but the monitor still scrubs the metadata projection
  defensively.
* **Closed-shape envelopes.** Every helper returns the
  documented shape; callers can paste the output into a
  dashboard without scrubbing.
* **Hard caps.** Operator typo cannot table-scan the world.

Public surface:

  * ``stale_worker_report(*, worker_type=None,
        stale_after_seconds=300, limit=200, now=None)``
  * ``heartbeat_monitor_report(*, worker_type=None,
        limit=200, now=None)``
```

## Imports

`ALLOWED_WORKER_TYPES`, `Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.db.supabase_client`, `app.services.worker.heartbeat_service`, `datetime`, `get_supabase`, `logging`, `timedelta`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_age_seconds`, `_clamp`, `_get_db_safe`, `_iso`, `_now_dt`, `_project_metadata`, `_project_row`, `_validate_worker_type_filter`, `heartbeat_monitor_report`, `stale_worker_report`

## Env-key candidates

`STOPPED`

## String constants (redacted where noted)

- '\nPAS172 — Worker heartbeat monitor (read-only).\n\nOperator-facing reader for the durable worker-heartbeat table.\nProduces structural reports that the PAS172 Slack employee-mode\nblock builders and the operator ops routes consume.\n\nDoctrine carried by every helper here:\n\n* **Read-only.** No writes; no DELETEs; no state transitions.\n* **No exception escapes.** DB unreachable → ``status="skipped"``\n  envelope with the structural warning. Never raises.\n* **No PII.** Workers don\'t carry PII (their schema forbids\n  it), but the monitor still scrubs the metadata projection\n  defensively.\n* **Closed-shape envelopes.** Every helper returns the\n  documented shape; callers can paste the output into a\n  dashboard without scrubbing.\n* **Hard caps.** Operator typo cannot table-scan the world.\n\nPublic surface:\n\n  * ``stale_worker_report(*, worker_type=None,\n        stale_after_seconds=300, limit=200, now=None)``\n  * ``heartbeat_monitor_report(*, worker_type=None,\n        limit=200, now=None)``\n'
- 'pas.worker.heartbeat_monitor'
- 'pas_worker_heartbeats'
- 'worker_type'
- 'stale_after_seconds'
- 'limit'
- 'now'
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
- 'metadata'
- 'Dict[str, Any]'
- 'row'
- 'Optional[Dict[str, Any]]'
- 'last_heartbeat_at'
- 'worker_id'
- 'hostname'
- 'pid'
- 'started_at'
- 'status'
- 'age_seconds'
- 'heartbeat_monitor db client unavailable type='
- 'Optional[str]'
- 'invalid_worker_type'
- 'List worker heartbeat rows whose ``last_heartbeat_at``\nis older than ``stale_after_seconds`` AND whose status is\nNOT already ``STOPPED``.\n\nReturns a structural envelope. NEVER raises. NEVER returns\nPII.\n'
- 'failed'
- 'stale_count'
- 'rows'
- 'warnings'
- 'error_code'
- 'skipped'
- 'heartbeat_store_unavailable'
- 'worker_id, worker_type, hostname, pid, started_at, last_heartbeat_at, status, metadata'
- 'data'
- 'stale_worker_report db error type='
- 'db_read_failed:'
- 'STOPPED'
- 'Structural snapshot of the heartbeat table: row count,\ncount by status, count by worker_type, age of the oldest\nrow.\n\nReturns a closed-shape envelope. NEVER raises. NEVER\nreturns PII.\n'
- 'total'
- 'by_status'
- 'by_worker_type'
- 'oldest_age_seconds'
- 'heartbeat_monitor_report db error type='

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS172 — Worker heartbeat monitor (read-only).\n\nOperator-facing reader for the durable worker-heartbeat table.\nProduces structural reports that the PAS172 Slack employee-mode\nblock builders and the operator ops routes consume.\n\nDoctrine carried by every helper here:\n\n* **Read-only.** No writes; no DELETEs; no state transitions.\n* **No exception escapes.** DB unreachable → ``status="skipped"``\n  envelope with the structural warning. Never raises.\n* **No PII.** Workers don\'t carry PII (their schema forbids\n  it), but the monitor still scrubs the metadata projection\n  defensively.\n* **Closed-shape envelopes.** Every helper returns the\n  documented shape; callers can paste the output into a\n  dashboard without scrubbing.\n* **Hard caps.** Operator typo cannot table-scan the world.\n\nPublic surface:\n\n  * ``stale_worker_report(*, worker_type=None,\n        stale_after_seconds=300, limit=200, now=None)``\n  * ``heartbeat_monitor_report(*, worker_type=None,\n        limit=200, now=None)``\n')
              STORE_NAME               0 (__doc__)

 29           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 31           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 32           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('datetime', 'timedelta', 'timezone'))
              IMPORT_NAME              4 (datetime)
              IMPORT_FROM              4 (datetime)
              STORE_NAME               4 (datetime)
              IMPORT_FROM              5 (timedelta)
              STORE_NAME               5 (timedelta)
              IMPORT_FROM              6 (timezone)
              STORE_NAME               6 (timezone)
              POP_TOP

 33           LOAD_SMALL_INT           0
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

 36           LOAD_NAME                3 (logging)
              LOAD_ATTR               24 (getLogger)
              PUSH_NULL
              LOAD_CONST               5 ('pas.worker.heartbeat_monitor')
              CALL                     1
              STORE_NAME              13 (logger)

 39           LOAD_CONST               6 ('pas_worker_heartbeats')
              STORE_NAME              14 (_TABLE)

 44           LOAD_CONST              31 (300)
              STORE_NAME              15 (DEFAULT_STALE_AFTER_SECONDS)

 47           LOAD_CONST               7 (1000)
              STORE_NAME              16 (_LIST_HARD_CAP)

 48           LOAD_SMALL_INT         200
              STORE_NAME              17 (_DEFAULT_LIMIT)

 51           LOAD_CONST              32 (('queue_depth', 'recovered_count', 'callback_due_count', 'warning_count', 'error_code', 'iteration_count', 'consecutive_failures'))
              STORE_NAME              18 (_ALLOWED_METADATA_KEYS)

 66           LOAD_CONST              33 ((None,))
              LOAD_CONST               8 (<code object __annotate__ at 0x0000018C17FA2F10, file "app/services/worker\heartbeat_monitor.py", line 66>)
              MAKE_FUNCTION
              LOAD_CONST               9 (<code object _now_dt at 0x0000018C17F7A220, file "app/services/worker\heartbeat_monitor.py", line 66>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              19 (_now_dt)

 82           LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA35A0, file "app/services/worker\heartbeat_monitor.py", line 82>)
              MAKE_FUNCTION
              LOAD_CONST              11 (<code object _iso at 0x0000018C18024E30, file "app/services/worker\heartbeat_monitor.py", line 82>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              20 (_iso)

 86           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C18026430, file "app/services/worker\heartbeat_monitor.py", line 86>)
              MAKE_FUNCTION
              LOAD_CONST              13 (<code object _age_seconds at 0x0000018C186455C0, file "app/services/worker\heartbeat_monitor.py", line 86>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              21 (_age_seconds)

100           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C18024C30, file "app/services/worker\heartbeat_monitor.py", line 100>)
              MAKE_FUNCTION
              LOAD_CONST              15 (<code object _clamp at 0x0000018C180392F0, file "app/services/worker\heartbeat_monitor.py", line 100>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              22 (_clamp)

112           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C17FA3780, file "app/services/worker\heartbeat_monitor.py", line 112>)
              MAKE_FUNCTION
              LOAD_CONST              17 (<code object _project_metadata at 0x0000018C18060F60, file "app/services/worker\heartbeat_monitor.py", line 112>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              23 (_project_metadata)

125           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C18025730, file "app/services/worker\heartbeat_monitor.py", line 125>)
              MAKE_FUNCTION
              LOAD_CONST              19 (<code object _project_row at 0x0000018C17ECE6C0, file "app/services/worker\heartbeat_monitor.py", line 125>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              24 (_project_row)

143           LOAD_CONST              20 (<code object _get_db_safe at 0x0000018C17FF0DB0, file "app/services/worker\heartbeat_monitor.py", line 143>)
              MAKE_FUNCTION
              STORE_NAME              25 (_get_db_safe)

155           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA2A60, file "app/services/worker\heartbeat_monitor.py", line 155>)
              MAKE_FUNCTION
              LOAD_CONST              22 (<code object _validate_worker_type_filter at 0x0000018C17C49B80, file "app/services/worker\heartbeat_monitor.py", line 155>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              26 (_validate_worker_type_filter)

168           LOAD_CONST              23 ('worker_type')

170           LOAD_CONST               2 (None)

168           LOAD_CONST              24 ('stale_after_seconds')

171           LOAD_NAME               15 (DEFAULT_STALE_AFTER_SECONDS)

168           LOAD_CONST              25 ('limit')

172           LOAD_NAME               17 (_DEFAULT_LIMIT)

168           LOAD_CONST              26 ('now')

173           LOAD_CONST               2 (None)

168           BUILD_MAP                4
              LOAD_CONST              27 (<code object __annotate__ at 0x0000018C18025D30, file "app/services/worker\heartbeat_monitor.py", line 168>)
              MAKE_FUNCTION
              LOAD_CONST              28 (<code object stale_worker_report at 0x0000018C17E929A0, file "app/services/worker\heartbeat_monitor.py", line 168>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              27 (stale_worker_report)

269           LOAD_CONST              23 ('worker_type')

271           LOAD_CONST               2 (None)

269           LOAD_CONST              25 ('limit')

272           LOAD_NAME               17 (_DEFAULT_LIMIT)

269           LOAD_CONST              26 ('now')

273           LOAD_CONST               2 (None)

269           BUILD_MAP                3
              LOAD_CONST              29 (<code object __annotate__ at 0x0000018C18025E30, file "app/services/worker\heartbeat_monitor.py", line 269>)
              MAKE_FUNCTION
              LOAD_CONST              30 (<code object heartbeat_monitor_report at 0x0000018C17F41160, file "app/services/worker\heartbeat_monitor.py", line 269>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              28 (heartbeat_monitor_report)

380           BUILD_LIST               0
              LOAD_CONST              34 (('DEFAULT_STALE_AFTER_SECONDS', 'stale_worker_report', 'heartbeat_monitor_report'))
              LIST_EXTEND              1
              STORE_NAME              29 (__all__)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "app/services/worker\heartbeat_monitor.py", line 66>:
 66           RESUME                   0
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

Disassembly of <code object _now_dt at 0x0000018C17F7A220, file "app/services/worker\heartbeat_monitor.py", line 66>:
  66            RESUME                   0

  67            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (now)
                LOAD_GLOBAL              2 (datetime)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       78 (to L2)
                NOT_TAKEN

  68            LOAD_FAST_BORROW         0 (now)
                LOAD_ATTR                4 (tzinfo)
                POP_JUMP_IF_NOT_NONE    33 (to L1)
                NOT_TAKEN

  69            LOAD_FAST_BORROW         0 (now)
                LOAD_ATTR                7 (replace + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                LOAD_CONST               1 (('tzinfo',))
                CALL_KW                  1
                RETURN_VALUE

  70    L1:     LOAD_FAST_BORROW         0 (now)
                LOAD_ATTR               13 (astimezone + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                CALL                     1
                RETURN_VALUE

  71    L2:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (now)
                LOAD_GLOBAL             14 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      117 (to L6)
                NOT_TAKEN

  72            NOP

  73    L3:     LOAD_GLOBAL              2 (datetime)
                LOAD_ATTR               16 (fromisoformat)
                PUSH_NULL
                LOAD_FAST_BORROW         0 (now)
                LOAD_ATTR                7 (replace + NULL|self)
                LOAD_CONST               2 ('Z')
                LOAD_CONST               3 ('+00:00')
                CALL                     2
                CALL                     1
                STORE_FAST               1 (dt)

  74            LOAD_FAST_BORROW         1 (dt)
                LOAD_ATTR                4 (tzinfo)
                POP_JUMP_IF_NOT_NONE    33 (to L4)
                NOT_TAKEN

  75            LOAD_FAST_BORROW         1 (dt)
                LOAD_ATTR                7 (replace + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                LOAD_CONST               1 (('tzinfo',))
                CALL_KW                  1
                STORE_FAST               1 (dt)

  76    L4:     LOAD_FAST_BORROW         1 (dt)
                LOAD_ATTR               13 (astimezone + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                CALL                     1
        L5:     RETURN_VALUE

  79    L6:     LOAD_GLOBAL              2 (datetime)
                LOAD_ATTR               20 (now)
                PUSH_NULL
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                CALL                     1
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

  77            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        4 (to L9)
                NOT_TAKEN
                POP_TOP

  78    L8:     POP_EXCEPT
                JUMP_BACKWARD_NO_INTERRUPT 49 (to L6)

  77    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L5 -> L7 [0]
  L7 to L8 -> L10 [1] lasti
  L9 to L10 -> L10 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "app/services/worker\heartbeat_monitor.py", line 82>:
 82           RESUME                   0
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

Disassembly of <code object _iso at 0x0000018C18024E30, file "app/services/worker\heartbeat_monitor.py", line 82>:
 82           RESUME                   0

 83           LOAD_FAST_BORROW         0 (dt)
              LOAD_ATTR                1 (isoformat + NULL|self)
              LOAD_CONST               0 ('seconds')
              LOAD_CONST               1 (('timespec',))
              CALL_KW                  1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026430, file "app/services/worker\heartbeat_monitor.py", line 86>:
 86           RESUME                   0
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

Disassembly of <code object _age_seconds at 0x0000018C186455C0, file "app/services/worker\heartbeat_monitor.py", line 86>:
  86            RESUME                   0

  87            LOAD_GLOBAL              1 (isinstance + NULL)
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

  88    L1:     LOAD_CONST               0 (None)
                RETURN_VALUE

  89    L2:     NOP

  90    L3:     LOAD_GLOBAL              6 (datetime)
                LOAD_ATTR                8 (fromisoformat)
                PUSH_NULL
                LOAD_FAST_BORROW         1 (ts_str)
                LOAD_ATTR               11 (replace + NULL|self)
                LOAD_CONST               1 ('Z')
                LOAD_CONST               2 ('+00:00')
                CALL                     2
                CALL                     1
                STORE_FAST               2 (dt)

  93    L4:     LOAD_FAST                2 (dt)
                LOAD_ATTR               14 (tzinfo)
                POP_JUMP_IF_NOT_NONE    33 (to L5)
                NOT_TAKEN

  94            LOAD_FAST                2 (dt)
                LOAD_ATTR               11 (replace + NULL|self)
                LOAD_GLOBAL             16 (timezone)
                LOAD_ATTR               18 (utc)
                LOAD_CONST               3 (('tzinfo',))
                CALL_KW                  1
                STORE_FAST               2 (dt)

  95    L5:     LOAD_FAST_LOAD_FAST      2 (now_dt, dt)
                BINARY_OP               10 (-)
                STORE_FAST               3 (delta)

  96            LOAD_GLOBAL             21 (int + NULL)
                LOAD_FAST                3 (delta)
                LOAD_ATTR               23 (total_seconds + NULL|self)
                CALL                     0
                CALL                     1
                STORE_FAST               4 (secs)

  97            LOAD_FAST                4 (secs)
                LOAD_SMALL_INT           0
                COMPARE_OP             188 (bool(>=))
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN
                LOAD_FAST                4 (secs)
                RETURN_VALUE
        L6:     LOAD_SMALL_INT           0
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

  91            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L9)
                NOT_TAKEN
                POP_TOP

  92    L8:     POP_EXCEPT
                LOAD_CONST               0 (None)
                RETURN_VALUE

  91    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L7 [0]
  L7 to L8 -> L10 [1] lasti
  L9 to L10 -> L10 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "app/services/worker\heartbeat_monitor.py", line 100>:
100           RESUME                   0
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

Disassembly of <code object _clamp at 0x0000018C180392F0, file "app/services/worker\heartbeat_monitor.py", line 100>:
 100           RESUME                   0

 101           NOP

 102   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               4 (v)

 105   L2:     LOAD_FAST_LOAD_FAST     65 (v, lo)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 106           LOAD_FAST                1 (lo)
               RETURN_VALUE

 107   L3:     LOAD_FAST_LOAD_FAST     66 (v, hi)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN

 108           LOAD_FAST                2 (hi)
               RETURN_VALUE

 109   L4:     LOAD_FAST                4 (v)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 103           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L7)
               NOT_TAKEN
               POP_TOP

 104           LOAD_FAST                3 (default)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

 103   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "app/services/worker\heartbeat_monitor.py", line 112>:
112           RESUME                   0
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

Disassembly of <code object _project_metadata at 0x0000018C18060F60, file "app/services/worker\heartbeat_monitor.py", line 112>:
112           RESUME                   0

113           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (metadata)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

114           BUILD_MAP                0
              RETURN_VALUE

115   L1:     BUILD_MAP                0
              STORE_FAST               1 (out)

116           LOAD_GLOBAL              4 (_ALLOWED_METADATA_KEYS)
              GET_ITER
      L2:     FOR_ITER                67 (to L5)
              STORE_FAST               2 (key)

117           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (key, metadata)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

118           JUMP_BACKWARD           11 (to L2)

119   L3:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (metadata, key)
              BINARY_OP               26 ([])
              STORE_FAST               3 (val)

120           LOAD_FAST_BORROW         3 (val)
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

121   L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (val, out)
              LOAD_FAST_BORROW         2 (key)
              STORE_SUBSCR
              JUMP_BACKWARD           69 (to L2)

116   L5:     END_FOR
              POP_ITER

122           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025730, file "app/services/worker\heartbeat_monitor.py", line 125>:
125           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('row')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('now_dt')
              LOAD_CONST               4 ('datetime')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('Optional[Dict[str, Any]]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _project_row at 0x0000018C17ECE6C0, file "app/services/worker\heartbeat_monitor.py", line 125>:
125           RESUME                   0

126           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (row)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

127           LOAD_CONST               0 (None)
              RETURN_VALUE

128   L1:     LOAD_FAST_BORROW         0 (row)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               1 ('last_heartbeat_at')
              CALL                     1
              STORE_FAST               2 (last)

129           LOAD_GLOBAL              7 (_age_seconds + NULL)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (now_dt, last)
              CALL                     2
              STORE_FAST               3 (age)

131           LOAD_CONST               2 ('worker_id')
              LOAD_FAST_BORROW         0 (row)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               2 ('worker_id')
              CALL                     1

132           LOAD_CONST               3 ('worker_type')
              LOAD_FAST_BORROW         0 (row)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               3 ('worker_type')
              CALL                     1

133           LOAD_CONST               4 ('hostname')
              LOAD_FAST_BORROW         0 (row)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               4 ('hostname')
              CALL                     1

134           LOAD_CONST               5 ('pid')
              LOAD_FAST_BORROW         0 (row)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               5 ('pid')
              CALL                     1

135           LOAD_CONST               6 ('started_at')
              LOAD_FAST_BORROW         0 (row)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               6 ('started_at')
              CALL                     1

136           LOAD_CONST               1 ('last_heartbeat_at')
              LOAD_FAST_BORROW         2 (last)

137           LOAD_CONST               7 ('status')
              LOAD_FAST_BORROW         0 (row)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               7 ('status')
              CALL                     1

138           LOAD_CONST               8 ('age_seconds')
              LOAD_FAST_BORROW         3 (age)

139           LOAD_CONST               9 ('metadata')
              LOAD_GLOBAL              9 (_project_metadata + NULL)
              LOAD_FAST_BORROW         0 (row)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               9 ('metadata')
              CALL                     1
              CALL                     1

130           BUILD_MAP                9
              RETURN_VALUE

Disassembly of <code object _get_db_safe at 0x0000018C17FF0DB0, file "app/services/worker\heartbeat_monitor.py", line 143>:
 143           RESUME                   0

 144           NOP

 145   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('get_supabase',))
               IMPORT_NAME              0 (app.db.supabase_client)
               IMPORT_FROM              1 (get_supabase)
               STORE_FAST               0 (get_supabase)
               POP_TOP

 146           LOAD_FAST_BORROW         0 (get_supabase)
               PUSH_NULL
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 147           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       55 (to L7)
               NOT_TAKEN
               STORE_FAST               1 (e)

 148   L4:     LOAD_GLOBAL              6 (logger)
               LOAD_ATTR                9 (warning + NULL|self)

 149           LOAD_CONST               2 ('heartbeat_monitor db client unavailable type=')

 150           LOAD_GLOBAL             11 (type + NULL)
               LOAD_FAST                1 (e)
               CALL                     1
               LOAD_ATTR               12 (__name__)
               FORMAT_SIMPLE

 149           BUILD_STRING             2

 148           CALL                     1
               POP_TOP

 152   L5:     POP_EXCEPT
               LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               LOAD_CONST               3 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               RERAISE                  1

 147   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "app/services/worker\heartbeat_monitor.py", line 155>:
155           RESUME                   0
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

Disassembly of <code object _validate_worker_type_filter at 0x0000018C17C49B80, file "app/services/worker\heartbeat_monitor.py", line 155>:
155           RESUME                   0

156           LOAD_FAST_BORROW         0 (worker_type)
              POP_JUMP_IF_NOT_NONE     3 (to L1)
              NOT_TAKEN

157           LOAD_CONST               0 (None)
              RETURN_VALUE

158   L1:     LOAD_SMALL_INT           0
              LOAD_CONST               1 (('ALLOWED_WORKER_TYPES',))
              IMPORT_NAME              0 (app.services.worker.heartbeat_service)
              IMPORT_FROM              1 (ALLOWED_WORKER_TYPES)
              STORE_FAST               1 (ALLOWED_WORKER_TYPES)
              POP_TOP

159           LOAD_GLOBAL              5 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (worker_type)
              LOAD_GLOBAL              6 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE        7 (to L2)
              NOT_TAKEN
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (worker_type, ALLOWED_WORKER_TYPES)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

160   L2:     LOAD_CONST               2 ('invalid_worker_type')
              RETURN_VALUE

161   L3:     LOAD_CONST               0 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025D30, file "app/services/worker\heartbeat_monitor.py", line 168>:
168           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('worker_type')

170           LOAD_CONST               2 ('Optional[str]')

168           LOAD_CONST               3 ('stale_after_seconds')

171           LOAD_CONST               4 ('int')

168           LOAD_CONST               5 ('limit')

172           LOAD_CONST               4 ('int')

168           LOAD_CONST               6 ('now')

173           LOAD_CONST               7 ('Any')

168           LOAD_CONST               8 ('return')

174           LOAD_CONST               9 ('Dict[str, Any]')

168           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object stale_worker_report at 0x0000018C17E929A0, file "app/services/worker\heartbeat_monitor.py", line 168>:
  --            MAKE_CELL               17 (now_dt)

 168            RESUME                   0

 182            LOAD_GLOBAL              1 (_validate_worker_type_filter + NULL)
                LOAD_FAST_BORROW         0 (worker_type)
                CALL                     1
                STORE_FAST               4 (err)

 183            LOAD_FAST_BORROW         4 (err)
                POP_JUMP_IF_NONE        19 (to L1)
                NOT_TAKEN

 185            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 186            LOAD_CONST               4 ('worker_type')
                LOAD_FAST_BORROW         0 (worker_type)

 187            LOAD_CONST               5 ('stale_after_seconds')
                LOAD_FAST_BORROW         1 (stale_after_seconds)

 188            LOAD_CONST               6 ('limit')
                LOAD_FAST_BORROW         2 (limit)

 189            LOAD_CONST               7 ('stale_count')
                LOAD_SMALL_INT           0

 190            LOAD_CONST               8 ('rows')
                BUILD_LIST               0

 191            LOAD_CONST               9 ('warnings')
                BUILD_LIST               0

 192            LOAD_CONST              10 ('error_code')
                LOAD_FAST_BORROW         4 (err)

 184            BUILD_MAP                8
                RETURN_VALUE

 195    L1:     LOAD_GLOBAL              3 (_clamp + NULL)

 196            LOAD_FAST_BORROW         1 (stale_after_seconds)
                LOAD_SMALL_INT          30
                LOAD_CONST              24 (86400)

 197            LOAD_GLOBAL              4 (DEFAULT_STALE_AFTER_SECONDS)

 195            CALL                     4
                STORE_FAST               5 (threshold_secs)

 199            LOAD_GLOBAL              3 (_clamp + NULL)
                LOAD_FAST_BORROW         2 (limit)
                LOAD_SMALL_INT           1
                LOAD_GLOBAL              6 (_LIST_HARD_CAP)
                LOAD_GLOBAL              8 (_DEFAULT_LIMIT)
                CALL                     4
                STORE_FAST               6 (capped_limit)

 200            LOAD_GLOBAL             11 (_now_dt + NULL)
                LOAD_FAST_BORROW         3 (now)
                CALL                     1
                STORE_DEREF             17 (now_dt)

 201            LOAD_GLOBAL             13 (_iso + NULL)
                LOAD_DEREF              17 (now_dt)
                LOAD_GLOBAL             15 (timedelta + NULL)
                LOAD_FAST_BORROW         5 (threshold_secs)
                LOAD_CONST              11 (('seconds',))
                CALL_KW                  1
                BINARY_OP               10 (-)
                CALL                     1
                STORE_FAST               7 (cutoff_iso)

 203            LOAD_GLOBAL             17 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               8 (db)

 204            LOAD_FAST_BORROW         8 (db)
                POP_JUMP_IF_NOT_NONE    20 (to L2)
                NOT_TAKEN

 206            LOAD_CONST               2 ('status')
                LOAD_CONST              12 ('skipped')

 207            LOAD_CONST               4 ('worker_type')
                LOAD_FAST_BORROW         0 (worker_type)

 208            LOAD_CONST               5 ('stale_after_seconds')
                LOAD_FAST_BORROW         5 (threshold_secs)

 209            LOAD_CONST               6 ('limit')
                LOAD_FAST_BORROW         6 (capped_limit)

 210            LOAD_CONST               7 ('stale_count')
                LOAD_SMALL_INT           0

 211            LOAD_CONST               8 ('rows')
                BUILD_LIST               0

 212            LOAD_CONST               9 ('warnings')
                LOAD_CONST              13 ('heartbeat_store_unavailable')
                BUILD_LIST               1

 213            LOAD_CONST              10 ('error_code')
                LOAD_CONST              13 ('heartbeat_store_unavailable')

 205            BUILD_MAP                8
                RETURN_VALUE

 216    L2:     NOP

 222    L3:     LOAD_FAST_BORROW         8 (db)
                LOAD_ATTR               19 (table + NULL|self)
                LOAD_GLOBAL             20 (_TABLE)
                CALL                     1

 223            LOAD_ATTR               23 (select + NULL|self)

 224            LOAD_CONST              14 ('worker_id, worker_type, hostname, pid, started_at, last_heartbeat_at, status, metadata')

 223            CALL                     1

 227            LOAD_ATTR               25 (lt + NULL|self)
                LOAD_CONST              15 ('last_heartbeat_at')
                LOAD_FAST_BORROW         7 (cutoff_iso)
                CALL                     2

 228            LOAD_ATTR               27 (order + NULL|self)
                LOAD_CONST              15 ('last_heartbeat_at')
                LOAD_CONST              16 (False)
                LOAD_CONST              17 (('desc',))
                CALL_KW                  2

 229            LOAD_ATTR               29 (limit + NULL|self)
                LOAD_FAST_BORROW         6 (capped_limit)
                CALL                     1

 221            STORE_FAST               9 (query)

 231            LOAD_FAST_BORROW         0 (worker_type)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L6)
        L4:     NOT_TAKEN

 232    L5:     LOAD_FAST_BORROW         9 (query)
                LOAD_ATTR               31 (eq + NULL|self)
                LOAD_CONST               4 ('worker_type')
                LOAD_FAST_BORROW         0 (worker_type)
                CALL                     2
                STORE_FAST               9 (query)

 233    L6:     LOAD_FAST_BORROW         9 (query)
                LOAD_ATTR               33 (execute + NULL|self)
                CALL                     0
                STORE_FAST              10 (result)

 234            LOAD_GLOBAL             35 (list + NULL)
                LOAD_GLOBAL             37 (getattr + NULL)
                LOAD_FAST_BORROW        10 (result)
                LOAD_CONST              18 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
        L7:     NOT_TAKEN
        L8:     POP_TOP
                BUILD_LIST               0
        L9:     CALL                     1
                STORE_FAST              11 (rows)

 254   L10:     LOAD_FAST               11 (rows)
                GET_ITER
                LOAD_FAST_AND_CLEAR     13 (r)
                SWAP                     2
       L11:     BUILD_LIST               0
                SWAP                     2
       L12:     FOR_ITER                53 (to L17)
                STORE_FAST              13 (r)

 255            LOAD_GLOBAL             49 (isinstance + NULL)
                LOAD_FAST               13 (r)
                LOAD_GLOBAL             50 (dict)
                CALL                     2
                TO_BOOL

 254   L13:     POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN
                JUMP_BACKWARD           27 (to L12)

 255   L14:     LOAD_FAST               13 (r)
                LOAD_ATTR               53 (get + NULL|self)
                LOAD_CONST               2 ('status')
                CALL                     1
                LOAD_CONST              21 ('STOPPED')
                COMPARE_OP             119 (bool(!=))

 254   L15:     POP_JUMP_IF_TRUE         3 (to L16)
                NOT_TAKEN
                JUMP_BACKWARD           51 (to L12)
       L16:     LOAD_FAST               13 (r)
                LIST_APPEND              2
                JUMP_BACKWARD           55 (to L12)
       L17:     END_FOR
                POP_ITER
       L18:     STORE_FAST              14 (active)
                STORE_FAST              13 (r)

 256            LOAD_FAST               17 (now_dt)
                BUILD_TUPLE              1
                LOAD_CONST              22 (<code object <genexpr> at 0x0000018C17FBFEE0, file "app/services/worker\heartbeat_monitor.py", line 256>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST               14 (active)
                GET_ITER
                CALL                     0
                GET_ITER
                LOAD_FAST_AND_CLEAR     15 (p)
                SWAP                     2
       L19:     BUILD_LIST               0
                SWAP                     2
       L20:     FOR_ITER                10 (to L23)
                STORE_FAST_LOAD_FAST   255 (p, p)
       L21:     POP_JUMP_IF_NOT_NONE     3 (to L22)
                NOT_TAKEN
                JUMP_BACKWARD            8 (to L20)
       L22:     LOAD_FAST               15 (p)
                LIST_APPEND              2
                JUMP_BACKWARD           12 (to L20)
       L23:     END_FOR
                POP_ITER
       L24:     STORE_FAST              16 (projected)
                STORE_FAST              15 (p)

 258            LOAD_CONST               2 ('status')
                LOAD_CONST              23 ('ok')

 259            LOAD_CONST               4 ('worker_type')
                LOAD_FAST                0 (worker_type)

 260            LOAD_CONST               5 ('stale_after_seconds')
                LOAD_FAST                5 (threshold_secs)

 261            LOAD_CONST               6 ('limit')
                LOAD_FAST                6 (capped_limit)

 262            LOAD_CONST               7 ('stale_count')
                LOAD_GLOBAL             55 (len + NULL)
                LOAD_FAST               16 (projected)
                CALL                     1

 263            LOAD_CONST               8 ('rows')
                LOAD_FAST               16 (projected)

 264            LOAD_CONST               9 ('warnings')
                BUILD_LIST               0

 265            LOAD_CONST              10 ('error_code')
                LOAD_CONST               1 (None)

 257            BUILD_MAP                8
                RETURN_VALUE

  --   L25:     PUSH_EXC_INFO

 235            LOAD_GLOBAL             38 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       95 (to L30)
                NOT_TAKEN
                STORE_FAST              12 (e)

 236   L26:     LOAD_GLOBAL             40 (logger)
                LOAD_ATTR               43 (warning + NULL|self)

 237            LOAD_CONST              19 ('stale_worker_report db error type=')
                LOAD_GLOBAL             45 (type + NULL)
                LOAD_FAST               12 (e)
                CALL                     1
                LOAD_ATTR               46 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 236            CALL                     1
                POP_TOP

 240            LOAD_CONST               2 ('status')
                LOAD_CONST              12 ('skipped')

 241            LOAD_CONST               4 ('worker_type')
                LOAD_FAST                0 (worker_type)

 242            LOAD_CONST               5 ('stale_after_seconds')
                LOAD_FAST                5 (threshold_secs)

 243            LOAD_CONST               6 ('limit')
                LOAD_FAST                6 (capped_limit)

 244            LOAD_CONST               7 ('stale_count')
                LOAD_SMALL_INT           0

 245            LOAD_CONST               8 ('rows')
                BUILD_LIST               0

 246            LOAD_CONST               9 ('warnings')
                LOAD_CONST              20 ('db_read_failed:')
                LOAD_GLOBAL             45 (type + NULL)
                LOAD_FAST               12 (e)
                CALL                     1
                LOAD_ATTR               46 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 247            LOAD_CONST              10 ('error_code')
                LOAD_CONST              13 ('heartbeat_store_unavailable')

 239            BUILD_MAP                8
       L27:     SWAP                     2
       L28:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              12 (e)
                DELETE_FAST             12 (e)
                RETURN_VALUE

  --   L29:     LOAD_CONST               1 (None)
                STORE_FAST              12 (e)
                DELETE_FAST             12 (e)
                RERAISE                  1

 235   L30:     RERAISE                  0

  --   L31:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L32:     SWAP                     2
                POP_TOP

 254            SWAP                     2
                STORE_FAST              13 (r)
                RERAISE                  0

  --   L33:     SWAP                     2
                POP_TOP

 256            SWAP                     2
                STORE_FAST              15 (p)
                RERAISE                  0
ExceptionTable:
  L3 to L4 -> L25 [0]
  L5 to L7 -> L25 [0]
  L8 to L10 -> L25 [0]
  L11 to L13 -> L32 [2]
  L14 to L15 -> L32 [2]
  L16 to L18 -> L32 [2]
  L19 to L21 -> L33 [2]
  L22 to L24 -> L33 [2]
  L25 to L26 -> L31 [1] lasti
  L26 to L27 -> L29 [1] lasti
  L27 to L28 -> L31 [1] lasti
  L29 to L31 -> L31 [1] lasti

Disassembly of <code object <genexpr> at 0x0000018C17FBFEE0, file "app/services/worker\heartbeat_monitor.py", line 256>:
  --           COPY_FREE_VARS           1

 256           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                18 (to L3)
               STORE_FAST               1 (r)
               LOAD_GLOBAL              1 (_project_row + NULL)
               LOAD_FAST_BORROW         1 (r)
               LOAD_DEREF               2 (now_dt)
               LOAD_CONST               0 (('now_dt',))
               CALL_KW                  2
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           20 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025E30, file "app/services/worker\heartbeat_monitor.py", line 269>:
269           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('worker_type')

271           LOAD_CONST               2 ('Optional[str]')

269           LOAD_CONST               3 ('limit')

272           LOAD_CONST               4 ('int')

269           LOAD_CONST               5 ('now')

273           LOAD_CONST               6 ('Any')

269           LOAD_CONST               7 ('return')

274           LOAD_CONST               8 ('Dict[str, Any]')

269           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object heartbeat_monitor_report at 0x0000018C17F41160, file "app/services/worker\heartbeat_monitor.py", line 269>:
 269            RESUME                   0

 282            LOAD_GLOBAL              1 (_validate_worker_type_filter + NULL)
                LOAD_FAST_BORROW         0 (worker_type)
                CALL                     1
                STORE_FAST               3 (err)

 283            LOAD_FAST_BORROW         3 (err)
                POP_JUMP_IF_NONE        23 (to L1)
                NOT_TAKEN

 285            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 286            LOAD_CONST               4 ('worker_type')
                LOAD_FAST_BORROW         0 (worker_type)

 287            LOAD_CONST               5 ('limit')
                LOAD_FAST_BORROW         1 (limit)

 288            LOAD_CONST               6 ('total')
                LOAD_SMALL_INT           0

 289            LOAD_CONST               7 ('by_status')
                BUILD_MAP                0

 290            LOAD_CONST               8 ('by_worker_type')
                BUILD_MAP                0

 291            LOAD_CONST               9 ('oldest_age_seconds')
                LOAD_CONST               1 (None)

 292            LOAD_CONST              10 ('rows')
                BUILD_LIST               0

 293            LOAD_CONST              11 ('warnings')
                BUILD_LIST               0

 294            LOAD_CONST              12 ('error_code')
                LOAD_FAST_BORROW         3 (err)

 284            BUILD_MAP               10
                RETURN_VALUE

 297    L1:     LOAD_GLOBAL              3 (_clamp + NULL)
                LOAD_FAST_BORROW         1 (limit)
                LOAD_SMALL_INT           1
                LOAD_GLOBAL              4 (_LIST_HARD_CAP)
                LOAD_GLOBAL              6 (_DEFAULT_LIMIT)
                CALL                     4
                STORE_FAST               4 (capped_limit)

 298            LOAD_GLOBAL              9 (_now_dt + NULL)
                LOAD_FAST_BORROW         2 (now)
                CALL                     1
                STORE_FAST               5 (now_dt)

 300            LOAD_GLOBAL             11 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               6 (db)

 301            LOAD_FAST_BORROW         6 (db)
                POP_JUMP_IF_NOT_NONE    24 (to L2)
                NOT_TAKEN

 303            LOAD_CONST               2 ('status')
                LOAD_CONST              13 ('skipped')

 304            LOAD_CONST               4 ('worker_type')
                LOAD_FAST_BORROW         0 (worker_type)

 305            LOAD_CONST               5 ('limit')
                LOAD_FAST_BORROW         4 (capped_limit)

 306            LOAD_CONST               6 ('total')
                LOAD_SMALL_INT           0

 307            LOAD_CONST               7 ('by_status')
                BUILD_MAP                0

 308            LOAD_CONST               8 ('by_worker_type')
                BUILD_MAP                0

 309            LOAD_CONST               9 ('oldest_age_seconds')
                LOAD_CONST               1 (None)

 310            LOAD_CONST              10 ('rows')
                BUILD_LIST               0

 311            LOAD_CONST              11 ('warnings')
                LOAD_CONST              14 ('heartbeat_store_unavailable')
                BUILD_LIST               1

 312            LOAD_CONST              12 ('error_code')
                LOAD_CONST              14 ('heartbeat_store_unavailable')

 302            BUILD_MAP               10
                RETURN_VALUE

 315    L2:     NOP

 317    L3:     LOAD_FAST_BORROW         6 (db)
                LOAD_ATTR               13 (table + NULL|self)
                LOAD_GLOBAL             14 (_TABLE)
                CALL                     1

 318            LOAD_ATTR               17 (select + NULL|self)

 319            LOAD_CONST              15 ('worker_id, worker_type, hostname, pid, started_at, last_heartbeat_at, status, metadata')

 318            CALL                     1

 322            LOAD_ATTR               19 (order + NULL|self)
                LOAD_CONST              16 ('last_heartbeat_at')
                LOAD_CONST              17 (True)
                LOAD_CONST              18 (('desc',))
                CALL_KW                  2

 323            LOAD_ATTR               21 (limit + NULL|self)
                LOAD_FAST_BORROW         4 (capped_limit)
                CALL                     1

 316            STORE_FAST               7 (query)

 325            LOAD_FAST_BORROW         0 (worker_type)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L6)
        L4:     NOT_TAKEN

 326    L5:     LOAD_FAST_BORROW         7 (query)
                LOAD_ATTR               23 (eq + NULL|self)
                LOAD_CONST               4 ('worker_type')
                LOAD_FAST_BORROW         0 (worker_type)
                CALL                     2
                STORE_FAST               7 (query)

 327    L6:     LOAD_FAST_BORROW         7 (query)
                LOAD_ATTR               25 (execute + NULL|self)
                CALL                     0
                STORE_FAST               8 (result)

 328            LOAD_GLOBAL             27 (list + NULL)
                LOAD_GLOBAL             29 (getattr + NULL)
                LOAD_FAST_BORROW         8 (result)
                LOAD_CONST              19 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
        L7:     NOT_TAKEN
        L8:     POP_TOP
                BUILD_LIST               0
        L9:     CALL                     1
                STORE_FAST               9 (rows)

 346   L10:     BUILD_MAP                0
                STORE_FAST              11 (by_status)

 347            BUILD_MAP                0
                STORE_FAST              12 (by_worker_type)

 348            LOAD_CONST               1 (None)
                STORE_FAST              13 (oldest_age)

 349            BUILD_LIST               0
                STORE_FAST              14 (projected)

 350            LOAD_FAST                9 (rows)
                GET_ITER
       L11:     EXTENDED_ARG             1
                FOR_ITER               299 (to L22)
                STORE_FAST              15 (row)

 351            LOAD_GLOBAL             41 (isinstance + NULL)
                LOAD_FAST               15 (row)
                LOAD_GLOBAL             42 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN

 352            JUMP_BACKWARD           28 (to L11)

 353   L12:     LOAD_GLOBAL             41 (isinstance + NULL)
                LOAD_FAST               15 (row)
                LOAD_ATTR               45 (get + NULL|self)
                LOAD_CONST               2 ('status')
                CALL                     1
                LOAD_GLOBAL             46 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L13)
                NOT_TAKEN
                LOAD_FAST               15 (row)
                LOAD_ATTR               45 (get + NULL|self)
                LOAD_CONST               2 ('status')
                CALL                     1
                JUMP_FORWARD             1 (to L14)
       L13:     LOAD_CONST               1 (None)
       L14:     STORE_FAST              16 (st)

 354            LOAD_FAST               16 (st)
                TO_BOOL
                POP_JUMP_IF_FALSE       29 (to L15)
                NOT_TAKEN

 355            LOAD_FAST               11 (by_status)
                LOAD_ATTR               45 (get + NULL|self)
                LOAD_FAST               16 (st)
                LOAD_SMALL_INT           0
                CALL                     2
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_FAST               11 (by_status)
                LOAD_FAST               16 (st)
                STORE_SUBSCR

 356   L15:     LOAD_GLOBAL             41 (isinstance + NULL)
                LOAD_FAST               15 (row)
                LOAD_ATTR               45 (get + NULL|self)
                LOAD_CONST               4 ('worker_type')
                CALL                     1
                LOAD_GLOBAL             46 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L16)
                NOT_TAKEN
                LOAD_FAST               15 (row)
                LOAD_ATTR               45 (get + NULL|self)
                LOAD_CONST               4 ('worker_type')
                CALL                     1
                JUMP_FORWARD             1 (to L17)
       L16:     LOAD_CONST               1 (None)
       L17:     STORE_FAST              17 (wt)

 357            LOAD_FAST               17 (wt)
                TO_BOOL
                POP_JUMP_IF_FALSE       29 (to L18)
                NOT_TAKEN

 358            LOAD_FAST               12 (by_worker_type)
                LOAD_ATTR               45 (get + NULL|self)
                LOAD_FAST               17 (wt)
                LOAD_SMALL_INT           0
                CALL                     2
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_FAST               12 (by_worker_type)
                LOAD_FAST               17 (wt)
                STORE_SUBSCR

 359   L18:     LOAD_GLOBAL             49 (_project_row + NULL)
                LOAD_FAST_LOAD_FAST    245 (row, now_dt)
                LOAD_CONST              22 (('now_dt',))
                CALL_KW                  2
                STORE_FAST              18 (proj)

 360            LOAD_FAST               18 (proj)
                POP_JUMP_IF_NOT_NONE     3 (to L19)
                NOT_TAKEN
                JUMP_BACKWARD          230 (to L11)

 361   L19:     LOAD_FAST               18 (proj)
                LOAD_ATTR               45 (get + NULL|self)
                LOAD_CONST              23 ('age_seconds')
                CALL                     1
                STORE_FAST              19 (age)

 362            LOAD_GLOBAL             41 (isinstance + NULL)
                LOAD_FAST               19 (age)
                LOAD_GLOBAL             50 (int)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       14 (to L21)
                NOT_TAKEN
                LOAD_FAST               13 (oldest_age)
                POP_JUMP_IF_NONE         8 (to L20)
                NOT_TAKEN
                LOAD_FAST               19 (age)
                LOAD_FAST               13 (oldest_age)
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE        3 (to L21)
                NOT_TAKEN

 363   L20:     LOAD_FAST               19 (age)
                STORE_FAST              13 (oldest_age)

 364   L21:     LOAD_FAST               14 (projected)
                LOAD_ATTR               53 (append + NULL|self)
                LOAD_FAST               18 (proj)
                CALL                     1
                POP_TOP
                EXTENDED_ARG             1
                JUMP_BACKWARD          302 (to L11)

 350   L22:     END_FOR
                POP_ITER

 367            LOAD_CONST               2 ('status')
                LOAD_CONST              24 ('ok')

 368            LOAD_CONST               4 ('worker_type')
                LOAD_FAST                0 (worker_type)

 369            LOAD_CONST               5 ('limit')
                LOAD_FAST                4 (capped_limit)

 370            LOAD_CONST               6 ('total')
                LOAD_GLOBAL             55 (len + NULL)
                LOAD_FAST               14 (projected)
                CALL                     1

 371            LOAD_CONST               7 ('by_status')
                LOAD_FAST               11 (by_status)

 372            LOAD_CONST               8 ('by_worker_type')
                LOAD_FAST               12 (by_worker_type)

 373            LOAD_CONST               9 ('oldest_age_seconds')
                LOAD_FAST               13 (oldest_age)

 374            LOAD_CONST              10 ('rows')
                LOAD_FAST               14 (projected)

 375            LOAD_CONST              11 ('warnings')
                BUILD_LIST               0

 376            LOAD_CONST              12 ('error_code')
                LOAD_CONST               1 (None)

 366            BUILD_MAP               10
                RETURN_VALUE

  --   L23:     PUSH_EXC_INFO

 329            LOAD_GLOBAL             30 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       99 (to L28)
                NOT_TAKEN
                STORE_FAST              10 (e)

 330   L24:     LOAD_GLOBAL             32 (logger)
                LOAD_ATTR               35 (warning + NULL|self)

 331            LOAD_CONST              20 ('heartbeat_monitor_report db error type=')
                LOAD_GLOBAL             37 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               38 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 330            CALL                     1
                POP_TOP

 334            LOAD_CONST               2 ('status')
                LOAD_CONST              13 ('skipped')

 335            LOAD_CONST               4 ('worker_type')
                LOAD_FAST                0 (worker_type)

 336            LOAD_CONST               5 ('limit')
                LOAD_FAST                4 (capped_limit)

 337            LOAD_CONST               6 ('total')
                LOAD_SMALL_INT           0

 338            LOAD_CONST               7 ('by_status')
                BUILD_MAP                0

 339            LOAD_CONST               8 ('by_worker_type')
                BUILD_MAP                0

 340            LOAD_CONST               9 ('oldest_age_seconds')
                LOAD_CONST               1 (None)

 341            LOAD_CONST              10 ('rows')
                BUILD_LIST               0

 342            LOAD_CONST              11 ('warnings')
                LOAD_CONST              21 ('db_read_failed:')
                LOAD_GLOBAL             37 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               38 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 343            LOAD_CONST              12 ('error_code')
                LOAD_CONST              14 ('heartbeat_store_unavailable')

 333            BUILD_MAP               10
       L25:     SWAP                     2
       L26:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RETURN_VALUE

  --   L27:     LOAD_CONST               1 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RERAISE                  1

 329   L28:     RERAISE                  0

  --   L29:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L23 [0]
  L5 to L7 -> L23 [0]
  L8 to L10 -> L23 [0]
  L23 to L24 -> L29 [1] lasti
  L24 to L25 -> L27 [1] lasti
  L25 to L26 -> L29 [1] lasti
  L27 to L29 -> L29 [1] lasti
```
