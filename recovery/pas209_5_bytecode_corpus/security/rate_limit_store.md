# security/rate_limit_store

- **pyc:** `app\services\security\__pycache__\rate_limit_store.cpython-314.pyc`
- **expected source path (absent):** `app\services\security/rate_limit_store.py`
- **co_filename (from bytecode):** `app/services/security/rate_limit_store.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** security

## Module docstring

```
PAS-SECURITY-02 — Rate-limit counter store (DB-backed + fallback).

Bucket-keyed counter store for the rate-limit service. Tries
the v31 ``pas_rate_limit_counters`` table first; falls back
to a process-local dict when the table is unavailable. The
fallback is *deliberately conservative* — counts do not
survive process restart and do not aggregate across workers.
The PAS-SECURITY-02 doctrine documents this as a known gap.

Doctrine:

* **DB-backed when available.** ``get_supabase()`` succeeds →
  read/write counter row keyed by ``bucket_key``.
* **Process-local fallback** when DB unavailable. The
  fallback emits a structural warning so callers can surface
  ``store="process_local"`` in their envelopes.
* **NEVER raises.** All helpers return structural envelopes.
* **No PII / no secrets.** ``bucket_key`` is a sha256 hex
  fingerprint over canonical (surface, brokerage, actor)
  fields; the table never stores raw IP / user-agent / API
  key / signature / token / env value.
* **Atomic increment best-effort.** SELECT-then-UPDATE; under
  contention the count may be off by 1 (acceptable for rate-
  limit semantics). A future PAS-SECURITY-03 pass can swap in
  an `INCREMENT` RPC for true atomicity.

Public surface:

  * ``ALLOWED_STORE_BACKENDS``                     — closed enum.
  * ``ALLOWED_COUNTER_METADATA_KEYS``              — closed allow-list.
  * ``read_counter(bucket_key)``                   — envelope.
  * ``increment_counter(bucket, request_count_delta, blocked_delta, ...)``
                                                   — envelope.
  * ``reset_process_local_store_for_tests()``      — test hook.
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `Tuple`, `__future__`, `annotations`, `app.db.supabase_client`, `datetime`, `get_supabase`, `logging`, `threading`, `time`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_bound_str`, `_get_db_safe`, `_iso`, `_now_dt`, `_project_metadata`, `_project_row`, `increment_counter`, `read_counter`, `reset_process_local_store_for_tests`

## Env-key candidates

`ALLOWED_COUNTER_METADATA_KEYS`, `ALLOWED_STORE_BACKENDS`

## String constants (redacted where noted)

- '\nPAS-SECURITY-02 — Rate-limit counter store (DB-backed + fallback).\n\nBucket-keyed counter store for the rate-limit service. Tries\nthe v31 ``pas_rate_limit_counters`` table first; falls back\nto a process-local dict when the table is unavailable. The\nfallback is *deliberately conservative* — counts do not\nsurvive process restart and do not aggregate across workers.\nThe PAS-SECURITY-02 doctrine documents this as a known gap.\n\nDoctrine:\n\n* **DB-backed when available.** ``get_supabase()`` succeeds →\n  read/write counter row keyed by ``bucket_key``.\n* **Process-local fallback** when DB unavailable. The\n  fallback emits a structural warning so callers can surface\n  ``store="process_local"`` in their envelopes.\n* **NEVER raises.** All helpers return structural envelopes.\n* **No PII / no secrets.** ``bucket_key`` is a sha256 hex\n  fingerprint over canonical (surface, brokerage, actor)\n  fields; the table never stores raw IP / user-agent / API\n  key / signature / token / env value.\n* **Atomic increment best-effort.** SELECT-then-UPDATE; under\n  contention the count may be off by 1 (acceptable for rate-\n  limit semantics). A future PAS-SECURITY-03 pass can swap in\n  an `INCREMENT` RPC for true atomicity.\n\nPublic surface:\n\n  * ``ALLOWED_STORE_BACKENDS``                     — closed enum.\n  * ``ALLOWED_COUNTER_METADATA_KEYS``              — closed allow-list.\n  * ``read_counter(bucket_key)``                   — envelope.\n  * ``increment_counter(bucket, request_count_delta, blocked_delta, ...)``\n                                                   — envelope.\n  * ``reset_process_local_store_for_tests()``      — test hook.\n'
- 'pas.security.rate_limit_store'
- 'pas_rate_limit_counters'
- 'Tuple[str, ...]'
- 'ALLOWED_STORE_BACKENDS'
- 'ALLOWED_COUNTER_METADATA_KEYS'
- 'brokerage_id'
- 'actor_type'
- 'actor_id'
- 'metadata'
- 'Dict[str, Dict[str, Any]]'
- '_local_store'
- 'request_count_delta'
- 'blocked_delta'
- 'return'
- 'None'
- 'Test-only hook to clear the in-memory fallback.'
- 'datetime'
- 'str'
- 'seconds'
- 'rate_limit_store db client unavailable type='
- 'value'
- 'Any'
- 'max_len'
- 'int'
- 'Optional[str]'
- 'Dict[str, Any]'
- 'row'
- 'Optional[Dict[str, Any]]'
- 'bucket_key'
- 'Read the current counter row. NEVER raises.\n\nOutcomes:\n  * ``status="ok"`` + ``backend="db"``           — counter found in DB.\n  * ``status="ok"`` + ``backend="process_local"`` — DB unavailable, found in fallback.\n  * ``status="empty"`` + ``backend=...``         — no counter row yet.\n'
- 'status'
- 'failed'
- 'backend'
- 'counter'
- 'warnings'
- 'error_code'
- 'invalid_bucket_key'
- 'data'
- 'empty'
- 'read_counter db error type='
- 'process_local'
- 'rate_limit_store_process_local'
- 'surface'
- 'window_start'
- 'window_end'
- 'Atomically (best-effort) increment the counter for the\ngiven window. Creates the row if missing. NEVER raises.'
- 'invalid_surface'
- 'invalid_actor_type'
- 'request_count'
- 'blocked_count'
- 'last_request_at'
- 'increment_counter db error type='

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS-SECURITY-02 — Rate-limit counter store (DB-backed + fallback).\n\nBucket-keyed counter store for the rate-limit service. Tries\nthe v31 ``pas_rate_limit_counters`` table first; falls back\nto a process-local dict when the table is unavailable. The\nfallback is *deliberately conservative* — counts do not\nsurvive process restart and do not aggregate across workers.\nThe PAS-SECURITY-02 doctrine documents this as a known gap.\n\nDoctrine:\n\n* **DB-backed when available.** ``get_supabase()`` succeeds →\n  read/write counter row keyed by ``bucket_key``.\n* **Process-local fallback** when DB unavailable. The\n  fallback emits a structural warning so callers can surface\n  ``store="process_local"`` in their envelopes.\n* **NEVER raises.** All helpers return structural envelopes.\n* **No PII / no secrets.** ``bucket_key`` is a sha256 hex\n  fingerprint over canonical (surface, brokerage, actor)\n  fields; the table never stores raw IP / user-agent / API\n  key / signature / token / env value.\n* **Atomic increment best-effort.** SELECT-then-UPDATE; under\n  contention the count may be off by 1 (acceptable for rate-\n  limit semantics). A future PAS-SECURITY-03 pass can swap in\n  an `INCREMENT` RPC for true atomicity.\n\nPublic surface:\n\n  * ``ALLOWED_STORE_BACKENDS``                     — closed enum.\n  * ``ALLOWED_COUNTER_METADATA_KEYS``              — closed allow-list.\n  * ``read_counter(bucket_key)``                   — envelope.\n  * ``increment_counter(bucket, request_count_delta, blocked_delta, ...)``\n                                                   — envelope.\n  * ``reset_process_local_store_for_tests()``      — test hook.\n')
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
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (time)
               STORE_NAME               6 (time)

  43           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              7 (datetime)
               IMPORT_FROM              7 (datetime)
               STORE_NAME               7 (datetime)
               IMPORT_FROM              8 (timezone)
               STORE_NAME               8 (timezone)
               POP_TOP

  44           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Any', 'Dict', 'List', 'Optional', 'Tuple'))
               IMPORT_NAME              9 (typing)
               IMPORT_FROM             10 (Any)
               STORE_NAME              10 (Any)
               IMPORT_FROM             11 (Dict)
               STORE_NAME              11 (Dict)
               IMPORT_FROM             12 (List)
               STORE_NAME              12 (List)
               IMPORT_FROM             13 (Optional)
               STORE_NAME              13 (Optional)
               IMPORT_FROM             14 (Tuple)
               STORE_NAME              14 (Tuple)
               POP_TOP

  47           LOAD_NAME                4 (logging)
               LOAD_ATTR               30 (getLogger)
               PUSH_NULL
               LOAD_CONST               5 ('pas.security.rate_limit_store')
               CALL                     1
               STORE_NAME              16 (logger)

  50           LOAD_CONST               6 ('pas_rate_limit_counters')
               STORE_NAME              17 (_TABLE)

  54           LOAD_CONST              35 (('db', 'process_local'))
               STORE_NAME              18 (ALLOWED_STORE_BACKENDS)
               LOAD_CONST               7 ('Tuple[str, ...]')
               LOAD_NAME               19 (__annotations__)
               LOAD_CONST               8 ('ALLOWED_STORE_BACKENDS')
               STORE_SUBSCR

  58           LOAD_CONST              36 (('actor_fingerprint', 'policy_token', 'warning_count', 'event'))
               STORE_NAME              20 (ALLOWED_COUNTER_METADATA_KEYS)
               LOAD_CONST               7 ('Tuple[str, ...]')
               LOAD_NAME               19 (__annotations__)
               LOAD_CONST               9 ('ALLOWED_COUNTER_METADATA_KEYS')
               STORE_SUBSCR

  67           LOAD_SMALL_INT         200
               STORE_NAME              21 (_BUCKET_KEY_MAX_LEN)

  68           LOAD_SMALL_INT         200
               STORE_NAME              22 (_BROKERAGE_ID_MAX_LEN)

  69           LOAD_SMALL_INT         200
               STORE_NAME              23 (_ACTOR_ID_MAX_LEN)

  73           LOAD_CONST              37 (('TENANT', 'OPERATOR', 'ADMIN', 'SYSTEM', 'ANON'))
               STORE_NAME              24 (_ALLOWED_ACTOR_TYPES)

  76           LOAD_CONST              38 (('email_ingestion', 'slack_command', 'admin', 'tenant_api', 'api_key_rotation', 'webhook_generic', 'webhook_followupboss', 'webhook_gohighlevel', 'webhook_zapier'))
               STORE_NAME              25 (_ALLOWED_SURFACES)

  89           LOAD_CONST              39 (('bucket_key', 'brokerage_id', 'surface', 'actor_type', 'actor_id', 'window_start', 'window_end', 'request_count', 'blocked_count', 'last_request_at', 'metadata'))
               STORE_NAME              26 (_STRUCTURAL_COLUMNS)

 109           BUILD_MAP                0
               STORE_NAME              27 (_local_store)
               LOAD_CONST              14 ('Dict[str, Dict[str, Any]]')
               LOAD_NAME               19 (__annotations__)
               LOAD_CONST              15 ('_local_store')
               STORE_SUBSCR

 110           LOAD_NAME                5 (threading)
               LOAD_ATTR               56 (Lock)
               PUSH_NULL
               CALL                     0
               STORE_NAME              29 (_local_lock)

 113           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C17FA3E10, file "app/services/security/rate_limit_store.py", line 113>)
               MAKE_FUNCTION
               LOAD_CONST              17 (<code object reset_process_local_store_for_tests at 0x0000018C17972550, file "app/services/security/rate_limit_store.py", line 113>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              30 (reset_process_local_store_for_tests)

 119           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA21F0, file "app/services/security/rate_limit_store.py", line 119>)
               MAKE_FUNCTION
               LOAD_CONST              19 (<code object _now_dt at 0x0000018C18053750, file "app/services/security/rate_limit_store.py", line 119>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              31 (_now_dt)

 123           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA2F10, file "app/services/security/rate_limit_store.py", line 123>)
               MAKE_FUNCTION
               LOAD_CONST              21 (<code object _iso at 0x0000018C18026630, file "app/services/security/rate_limit_store.py", line 123>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              32 (_iso)

 127           LOAD_CONST              22 (<code object _get_db_safe at 0x0000018C17FF0DB0, file "app/services/security/rate_limit_store.py", line 127>)
               MAKE_FUNCTION
               STORE_NAME              33 (_get_db_safe)

 139           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C18026430, file "app/services/security/rate_limit_store.py", line 139>)
               MAKE_FUNCTION
               LOAD_CONST              24 (<code object _bound_str at 0x0000018C180110B0, file "app/services/security/rate_limit_store.py", line 139>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              34 (_bound_str)

 148           LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA31E0, file "app/services/security/rate_limit_store.py", line 148>)
               MAKE_FUNCTION
               LOAD_CONST              26 (<code object _project_metadata at 0x0000018C17FEE030, file "app/services/security/rate_limit_store.py", line 148>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              35 (_project_metadata)

 163           LOAD_CONST              27 (<code object __annotate__ at 0x0000018C17FA3690, file "app/services/security/rate_limit_store.py", line 163>)
               MAKE_FUNCTION
               LOAD_CONST              28 (<code object _project_row at 0x0000018C1804D3B0, file "app/services/security/rate_limit_store.py", line 163>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              36 (_project_row)

 178           LOAD_CONST              29 (<code object __annotate__ at 0x0000018C17FA2E20, file "app/services/security/rate_limit_store.py", line 178>)
               MAKE_FUNCTION
               LOAD_CONST              30 (<code object read_counter at 0x0000018C17D814D0, file "app/services/security/rate_limit_store.py", line 178>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              37 (read_counter)

 253           LOAD_CONST              10 ('brokerage_id')

 259           LOAD_CONST               2 (None)

 253           LOAD_CONST              11 ('actor_type')

 260           LOAD_CONST               2 (None)

 253           LOAD_CONST              12 ('actor_id')

 261           LOAD_CONST               2 (None)

 253           LOAD_CONST              31 ('request_count_delta')

 262           LOAD_SMALL_INT           1

 253           LOAD_CONST              32 ('blocked_delta')

 263           LOAD_SMALL_INT           0

 253           LOAD_CONST              13 ('metadata')

 264           LOAD_CONST               2 (None)

 253           BUILD_MAP                6
               LOAD_CONST              33 (<code object __annotate__ at 0x0000018C18053630, file "app/services/security/rate_limit_store.py", line 253>)
               MAKE_FUNCTION
               LOAD_CONST              34 (<code object increment_counter at 0x0000018C17D51990, file "app/services/security/rate_limit_store.py", line 253>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              38 (increment_counter)

 409           BUILD_LIST               0
               LOAD_CONST              40 (('ALLOWED_STORE_BACKENDS', 'ALLOWED_COUNTER_METADATA_KEYS', 'read_counter', 'increment_counter', 'reset_process_local_store_for_tests'))
               LIST_EXTEND              1
               STORE_NAME              39 (__all__)
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "app/services/security/rate_limit_store.py", line 113>:
113           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('None')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object reset_process_local_store_for_tests at 0x0000018C17972550, file "app/services/security/rate_limit_store.py", line 113>:
 113           RESUME                   0

 115           LOAD_GLOBAL              0 (_local_lock)
               COPY                     1
               LOAD_SPECIAL             1 (__exit__)
               SWAP                     2
               SWAP                     3
               LOAD_SPECIAL             0 (__enter__)
               CALL                     0
       L1:     POP_TOP

 116           LOAD_GLOBAL              2 (_local_store)
               LOAD_ATTR                5 (clear + NULL|self)
               CALL                     0
               POP_TOP

 115   L2:     LOAD_CONST               1 (None)
               LOAD_CONST               1 (None)
               LOAD_CONST               1 (None)
               CALL                     3
               POP_TOP
               LOAD_CONST               1 (None)
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
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [2] lasti
  L3 to L5 -> L6 [4] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "app/services/security/rate_limit_store.py", line 119>:
119           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('datetime')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _now_dt at 0x0000018C18053750, file "app/services/security/rate_limit_store.py", line 119>:
119           RESUME                   0

120           LOAD_GLOBAL              0 (datetime)
              LOAD_ATTR                2 (now)
              PUSH_NULL
              LOAD_GLOBAL              4 (timezone)
              LOAD_ATTR                6 (utc)
              CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "app/services/security/rate_limit_store.py", line 123>:
123           RESUME                   0
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

Disassembly of <code object _iso at 0x0000018C18026630, file "app/services/security/rate_limit_store.py", line 123>:
123           RESUME                   0

124           LOAD_FAST_BORROW         0 (dt)
              LOAD_ATTR                1 (isoformat + NULL|self)
              LOAD_CONST               0 ('seconds')
              LOAD_CONST               1 (('timespec',))
              CALL_KW                  1
              RETURN_VALUE

Disassembly of <code object _get_db_safe at 0x0000018C17FF0DB0, file "app/services/security/rate_limit_store.py", line 127>:
 127           RESUME                   0

 128           NOP

 129   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('get_supabase',))
               IMPORT_NAME              0 (app.db.supabase_client)
               IMPORT_FROM              1 (get_supabase)
               STORE_FAST               0 (get_supabase)
               POP_TOP

 130           LOAD_FAST_BORROW         0 (get_supabase)
               PUSH_NULL
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 131           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       55 (to L7)
               NOT_TAKEN
               STORE_FAST               1 (e)

 132   L4:     LOAD_GLOBAL              6 (logger)
               LOAD_ATTR                9 (warning + NULL|self)

 133           LOAD_CONST               2 ('rate_limit_store db client unavailable type=')

 134           LOAD_GLOBAL             11 (type + NULL)
               LOAD_FAST                1 (e)
               CALL                     1
               LOAD_ATTR               12 (__name__)
               FORMAT_SIMPLE

 133           BUILD_STRING             2

 132           CALL                     1
               POP_TOP

 136   L5:     POP_EXCEPT
               LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               LOAD_CONST               3 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               RERAISE                  1

 131   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026430, file "app/services/security/rate_limit_store.py", line 139>:
139           RESUME                   0
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

Disassembly of <code object _bound_str at 0x0000018C180110B0, file "app/services/security/rate_limit_store.py", line 139>:
139           RESUME                   0

140           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

141           LOAD_CONST               0 (None)
              RETURN_VALUE

142   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               2 (s)

143           LOAD_FAST_BORROW         2 (s)
              TO_BOOL
              POP_JUMP_IF_FALSE       17 (to L2)
              NOT_TAKEN
              LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         2 (s)
              CALL                     1
              LOAD_FAST_BORROW         1 (max_len)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

144   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

145   L3:     LOAD_FAST_BORROW         2 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "app/services/security/rate_limit_store.py", line 148>:
148           RESUME                   0
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

Disassembly of <code object _project_metadata at 0x0000018C17FEE030, file "app/services/security/rate_limit_store.py", line 148>:
148           RESUME                   0

149           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (metadata)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

150           BUILD_MAP                0
              RETURN_VALUE

151   L1:     BUILD_MAP                0
              STORE_FAST               1 (out)

152           LOAD_GLOBAL              4 (ALLOWED_COUNTER_METADATA_KEYS)
              GET_ITER
      L2:     FOR_ITER               108 (to L8)
              STORE_FAST               2 (k)

153           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (k, metadata)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

154           JUMP_BACKWARD           11 (to L2)

155   L3:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (metadata, k)
              BINARY_OP               26 ([])
              STORE_FAST               3 (v)

156           LOAD_FAST_BORROW         3 (v)
              POP_JUMP_IF_NONE        34 (to L4)
              NOT_TAKEN
              LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         3 (v)
              LOAD_GLOBAL              6 (bool)
              LOAD_GLOBAL              8 (int)
              LOAD_GLOBAL             10 (float)
              BUILD_TUPLE              3
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE        7 (to L5)
              NOT_TAKEN

157   L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (v, out)
              LOAD_FAST_BORROW         2 (k)
              STORE_SUBSCR
              JUMP_BACKWARD           62 (to L2)

158   L5:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         3 (v)
              LOAD_GLOBAL             12 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L6)
              NOT_TAKEN
              JUMP_BACKWARD           86 (to L2)
      L6:     LOAD_GLOBAL             15 (len + NULL)
              LOAD_FAST_BORROW         3 (v)
              CALL                     1
              LOAD_SMALL_INT         200
              COMPARE_OP              58 (bool(<=))
              POP_JUMP_IF_TRUE         3 (to L7)
              NOT_TAKEN
              JUMP_BACKWARD          104 (to L2)

159   L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (v, out)
              LOAD_FAST_BORROW         2 (k)
              STORE_SUBSCR
              JUMP_BACKWARD          110 (to L2)

152   L8:     END_FOR
              POP_ITER

160           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "app/services/security/rate_limit_store.py", line 163>:
163           RESUME                   0
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

Disassembly of <code object _project_row at 0x0000018C1804D3B0, file "app/services/security/rate_limit_store.py", line 163>:
163           RESUME                   0

164           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (row)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

165           LOAD_CONST               0 (None)
              RETURN_VALUE

166   L1:     BUILD_MAP                0
              STORE_FAST               1 (out)

167           LOAD_GLOBAL              4 (_STRUCTURAL_COLUMNS)
              GET_ITER
      L2:     FOR_ITER                21 (to L4)
              STORE_FAST               2 (col)

168           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (col, row)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

169   L3:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (row, col)
              BINARY_OP               26 ([])
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (out, col)
              STORE_SUBSCR
              JUMP_BACKWARD           23 (to L2)

167   L4:     END_FOR
              POP_ITER

170           LOAD_GLOBAL              7 (_project_metadata + NULL)
              LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               1 ('metadata')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L5:     CALL                     1
              LOAD_FAST_BORROW         1 (out)
              LOAD_CONST               1 ('metadata')
              STORE_SUBSCR

171           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "app/services/security/rate_limit_store.py", line 178>:
178           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('bucket_key')

180           LOAD_CONST               2 ('str')

178           LOAD_CONST               3 ('return')

181           LOAD_CONST               4 ('Dict[str, Any]')

178           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object read_counter at 0x0000018C17D814D0, file "app/services/security/rate_limit_store.py", line 178>:
 178            RESUME                   0

 189            LOAD_GLOBAL              1 (_bound_str + NULL)
                LOAD_FAST_BORROW         0 (bucket_key)
                LOAD_GLOBAL              2 (_BUCKET_KEY_MAX_LEN)
                CALL                     2
                STORE_FAST               1 (bk)

 190            LOAD_FAST_BORROW         1 (bk)
                POP_JUMP_IF_NOT_NONE    13 (to L1)
                NOT_TAKEN

 192            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 193            LOAD_CONST               4 ('backend')
                LOAD_CONST               1 (None)

 194            LOAD_CONST               5 ('counter')
                LOAD_CONST               1 (None)

 195            LOAD_CONST               6 ('warnings')
                BUILD_LIST               0

 196            LOAD_CONST               7 ('error_code')
                LOAD_CONST               8 ('invalid_bucket_key')

 191            BUILD_MAP                5
                RETURN_VALUE

 198    L1:     LOAD_GLOBAL              5 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               2 (db)

 199            LOAD_FAST_BORROW         2 (db)
                POP_JUMP_IF_NONE       182 (to L11)
                NOT_TAKEN

 200            NOP

 202    L2:     LOAD_FAST_BORROW         2 (db)
                LOAD_ATTR                7 (table + NULL|self)
                LOAD_GLOBAL              8 (_TABLE)
                CALL                     1

 203            LOAD_ATTR               11 (select + NULL|self)
                LOAD_CONST               9 (',')
                LOAD_ATTR               13 (join + NULL|self)
                LOAD_GLOBAL             14 (_STRUCTURAL_COLUMNS)
                CALL                     1
                CALL                     1

 204            LOAD_ATTR               17 (eq + NULL|self)
                LOAD_CONST              10 ('bucket_key')
                LOAD_FAST_BORROW         1 (bk)
                CALL                     2

 205            LOAD_ATTR               19 (limit + NULL|self)
                LOAD_SMALL_INT           2
                CALL                     1

 206            LOAD_ATTR               21 (execute + NULL|self)
                CALL                     0

 201            STORE_FAST               3 (result)

 208            LOAD_GLOBAL             23 (list + NULL)
                LOAD_GLOBAL             25 (getattr + NULL)
                LOAD_FAST_BORROW         3 (result)
                LOAD_CONST              11 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
        L3:     NOT_TAKEN
        L4:     POP_TOP
                BUILD_LIST               0
        L5:     CALL                     1
                STORE_FAST               4 (rows)

 209            LOAD_FAST_BORROW         4 (rows)
                TO_BOOL
                POP_JUMP_IF_FALSE       29 (to L9)
        L6:     NOT_TAKEN

 211    L7:     LOAD_CONST               2 ('status')
                LOAD_CONST              12 ('ok')

 212            LOAD_CONST               4 ('backend')
                LOAD_CONST              13 ('db')

 213            LOAD_CONST               5 ('counter')
                LOAD_GLOBAL             27 (_project_row + NULL)
                LOAD_FAST_BORROW         4 (rows)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                CALL                     1

 214            LOAD_CONST               6 ('warnings')
                BUILD_LIST               0

 215            LOAD_CONST               7 ('error_code')
                LOAD_CONST               1 (None)

 210            BUILD_MAP                5
        L8:     RETURN_VALUE

 218    L9:     LOAD_CONST               2 ('status')
                LOAD_CONST              14 ('empty')

 219            LOAD_CONST               4 ('backend')
                LOAD_CONST              13 ('db')

 220            LOAD_CONST               5 ('counter')
                LOAD_CONST               1 (None)

 221            LOAD_CONST               6 ('warnings')
                BUILD_LIST               0

 222            LOAD_CONST               7 ('error_code')
                LOAD_CONST               1 (None)

 217            BUILD_MAP                5
       L10:     RETURN_VALUE

 230   L11:     LOAD_GLOBAL             38 (_local_lock)
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
       L12:     POP_TOP

 231            LOAD_GLOBAL             41 (dict + NULL)
                LOAD_GLOBAL             42 (_local_store)
                LOAD_ATTR               45 (get + NULL|self)
                LOAD_FAST_BORROW         1 (bk)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
       L13:     CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L16)
       L14:     NOT_TAKEN
       L15:     POP_TOP
                LOAD_CONST               1 (None)
       L16:     STORE_FAST               6 (row)

 230   L17:     LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                CALL                     3
                POP_TOP

 232   L18:     LOAD_FAST_CHECK          6 (row)
                TO_BOOL
                POP_JUMP_IF_TRUE        14 (to L19)
                NOT_TAKEN

 234            LOAD_CONST               2 ('status')
                LOAD_CONST              14 ('empty')

 235            LOAD_CONST               4 ('backend')
                LOAD_CONST              16 ('process_local')

 236            LOAD_CONST               5 ('counter')
                LOAD_CONST               1 (None)

 237            LOAD_CONST               6 ('warnings')
                LOAD_CONST              17 ('rate_limit_store_process_local')
                BUILD_LIST               1

 238            LOAD_CONST               7 ('error_code')
                LOAD_CONST               1 (None)

 233            BUILD_MAP                5
                RETURN_VALUE

 241   L19:     LOAD_CONST               2 ('status')
                LOAD_CONST              12 ('ok')

 242            LOAD_CONST               4 ('backend')
                LOAD_CONST              16 ('process_local')

 243            LOAD_CONST               5 ('counter')
                LOAD_GLOBAL             27 (_project_row + NULL)
                LOAD_FAST_BORROW         6 (row)
                CALL                     1

 244            LOAD_CONST               6 ('warnings')
                LOAD_CONST              17 ('rate_limit_store_process_local')
                BUILD_LIST               1

 245            LOAD_CONST               7 ('error_code')
                LOAD_CONST               1 (None)

 240            BUILD_MAP                5
                RETURN_VALUE

  --   L20:     PUSH_EXC_INFO

 224            LOAD_GLOBAL             28 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       54 (to L24)
                NOT_TAKEN
                STORE_FAST               5 (e)

 225   L21:     LOAD_GLOBAL             30 (logger)
                LOAD_ATTR               33 (warning + NULL|self)

 226            LOAD_CONST              15 ('read_counter db error type=')
                LOAD_GLOBAL             35 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               36 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 225            CALL                     1
                POP_TOP
       L22:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                JUMP_BACKWARD_NO_INTERRUPT 175 (to L11)

  --   L23:     LOAD_CONST               1 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RERAISE                  1

 224   L24:     RERAISE                  0

  --   L25:     COPY                     3
                POP_EXCEPT
                RERAISE                  1

 230   L26:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L27)
                NOT_TAKEN
                RERAISE                  2
       L27:     POP_TOP
       L28:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
                JUMP_BACKWARD_NO_INTERRUPT 126 (to L18)

  --   L29:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L20 [0]
  L4 to L6 -> L20 [0]
  L7 to L8 -> L20 [0]
  L9 to L10 -> L20 [0]
  L12 to L14 -> L26 [2] lasti
  L15 to L17 -> L26 [2] lasti
  L20 to L21 -> L25 [1] lasti
  L21 to L22 -> L23 [1] lasti
  L23 to L25 -> L25 [1] lasti
  L26 to L28 -> L29 [4] lasti

Disassembly of <code object __annotate__ at 0x0000018C18053630, file "app/services/security/rate_limit_store.py", line 253>:
253           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('bucket_key')

255           LOAD_CONST               2 ('str')

253           LOAD_CONST               3 ('surface')

256           LOAD_CONST               2 ('str')

253           LOAD_CONST               4 ('window_start')

257           LOAD_CONST               5 ('Any')

253           LOAD_CONST               6 ('window_end')

258           LOAD_CONST               5 ('Any')

253           LOAD_CONST               7 ('brokerage_id')

259           LOAD_CONST               8 ('Optional[str]')

253           LOAD_CONST               9 ('actor_type')

260           LOAD_CONST               8 ('Optional[str]')

253           LOAD_CONST              10 ('actor_id')

261           LOAD_CONST               8 ('Optional[str]')

253           LOAD_CONST              11 ('request_count_delta')

262           LOAD_CONST              12 ('int')

253           LOAD_CONST              13 ('blocked_delta')

263           LOAD_CONST              12 ('int')

253           LOAD_CONST              14 ('metadata')

264           LOAD_CONST              15 ('Optional[Dict[str, Any]]')

253           LOAD_CONST              16 ('return')

265           LOAD_CONST              17 ('Dict[str, Any]')

253           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object increment_counter at 0x0000018C17D51990, file "app/services/security/rate_limit_store.py", line 253>:
 253            RESUME                   0

 268            LOAD_GLOBAL              1 (_bound_str + NULL)
                LOAD_FAST_BORROW         0 (bucket_key)
                LOAD_GLOBAL              2 (_BUCKET_KEY_MAX_LEN)
                CALL                     2
                STORE_FAST              10 (bk)

 269            LOAD_FAST_BORROW        10 (bk)
                POP_JUMP_IF_NOT_NONE    13 (to L1)
                NOT_TAKEN

 271            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 272            LOAD_CONST               4 ('backend')
                LOAD_CONST               1 (None)

 273            LOAD_CONST               5 ('counter')
                LOAD_CONST               1 (None)

 274            LOAD_CONST               6 ('warnings')
                BUILD_LIST               0

 275            LOAD_CONST               7 ('error_code')
                LOAD_CONST               8 ('invalid_bucket_key')

 270            BUILD_MAP                5
                RETURN_VALUE

 277    L1:     LOAD_FAST_BORROW         1 (surface)
                LOAD_GLOBAL              4 (_ALLOWED_SURFACES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       13 (to L2)
                NOT_TAKEN

 279            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 280            LOAD_CONST               4 ('backend')
                LOAD_CONST               1 (None)

 281            LOAD_CONST               5 ('counter')
                LOAD_CONST               1 (None)

 282            LOAD_CONST               6 ('warnings')
                BUILD_LIST               0

 283            LOAD_CONST               7 ('error_code')
                LOAD_CONST               9 ('invalid_surface')

 278            BUILD_MAP                5
                RETURN_VALUE

 285    L2:     LOAD_FAST_BORROW         5 (actor_type)
                POP_JUMP_IF_NONE        24 (to L3)
                NOT_TAKEN
                LOAD_FAST_BORROW         5 (actor_type)
                LOAD_GLOBAL              6 (_ALLOWED_ACTOR_TYPES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       13 (to L3)
                NOT_TAKEN

 287            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 288            LOAD_CONST               4 ('backend')
                LOAD_CONST               1 (None)

 289            LOAD_CONST               5 ('counter')
                LOAD_CONST               1 (None)

 290            LOAD_CONST               6 ('warnings')
                BUILD_LIST               0

 291            LOAD_CONST               7 ('error_code')
                LOAD_CONST              10 ('invalid_actor_type')

 286            BUILD_MAP                5
                RETURN_VALUE

 293    L3:     LOAD_FAST_BORROW         4 (brokerage_id)
                POP_JUMP_IF_NONE        17 (to L4)
                NOT_TAKEN
                LOAD_GLOBAL              1 (_bound_str + NULL)
                LOAD_FAST_BORROW         4 (brokerage_id)
                LOAD_GLOBAL              8 (_BROKERAGE_ID_MAX_LEN)
                CALL                     2
                JUMP_FORWARD             1 (to L5)
        L4:     LOAD_CONST               1 (None)
        L5:     STORE_FAST              11 (bid)

 294            LOAD_FAST_BORROW         6 (actor_id)
                POP_JUMP_IF_NONE        17 (to L6)
                NOT_TAKEN
                LOAD_GLOBAL              1 (_bound_str + NULL)
                LOAD_FAST_BORROW         6 (actor_id)
                LOAD_GLOBAL             10 (_ACTOR_ID_MAX_LEN)
                CALL                     2
                JUMP_FORWARD             1 (to L7)
        L6:     LOAD_CONST               1 (None)
        L7:     STORE_FAST              12 (actor)

 295            LOAD_GLOBAL             13 (_project_metadata + NULL)
                LOAD_FAST_BORROW         9 (metadata)
                CALL                     1
                STORE_FAST              13 (md)

 297            LOAD_GLOBAL             15 (isinstance + NULL)
                LOAD_FAST_BORROW         2 (window_start)
                LOAD_GLOBAL             16 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_FAST                2 (window_start)
                JUMP_FORWARD            18 (to L9)
        L8:     LOAD_GLOBAL             19 (_iso + NULL)
                LOAD_GLOBAL             21 (_now_dt + NULL)
                CALL                     0
                CALL                     1
        L9:     STORE_FAST              14 (ws)

 298            LOAD_GLOBAL             15 (isinstance + NULL)
                LOAD_FAST_BORROW         3 (window_end)
                LOAD_GLOBAL             16 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN
                LOAD_FAST                3 (window_end)
                JUMP_FORWARD            18 (to L11)
       L10:     LOAD_GLOBAL             19 (_iso + NULL)
                LOAD_GLOBAL             21 (_now_dt + NULL)
                CALL                     0
                CALL                     1
       L11:     STORE_FAST              15 (we)

 300            NOP

 301   L12:     LOAD_GLOBAL             23 (max + NULL)
                LOAD_SMALL_INT           0
                LOAD_GLOBAL             25 (int + NULL)
                LOAD_FAST_BORROW         7 (request_count_delta)
                CALL                     1
                CALL                     2
                STORE_FAST              16 (req_delta)

 304   L13:     NOP

 305   L14:     LOAD_GLOBAL             23 (max + NULL)
                LOAD_SMALL_INT           0
                LOAD_GLOBAL             25 (int + NULL)
                LOAD_FAST_BORROW         8 (blocked_delta)
                CALL                     1
                CALL                     2
                STORE_FAST              17 (blk_delta)

 309   L15:     LOAD_GLOBAL             19 (_iso + NULL)
                LOAD_GLOBAL             21 (_now_dt + NULL)
                CALL                     0
                CALL                     1
                STORE_FAST              18 (now_iso)

 311            LOAD_GLOBAL             31 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST              19 (db)

 312            LOAD_FAST_BORROW        19 (db)
                EXTENDED_ARG             2
                POP_JUMP_IF_NONE       558 (to L46)
                NOT_TAKEN

 313            NOP

 315   L16:     LOAD_FAST_BORROW        19 (db)
                LOAD_ATTR               33 (table + NULL|self)
                LOAD_GLOBAL             34 (_TABLE)
                CALL                     1

 316            LOAD_ATTR               37 (select + NULL|self)
                LOAD_CONST              11 (',')
                LOAD_ATTR               39 (join + NULL|self)
                LOAD_GLOBAL             40 (_STRUCTURAL_COLUMNS)
                CALL                     1
                CALL                     1

 317            LOAD_ATTR               43 (eq + NULL|self)
                LOAD_CONST              12 ('bucket_key')
                LOAD_FAST_BORROW        10 (bk)
                CALL                     2

 318            LOAD_ATTR               45 (limit + NULL|self)
                LOAD_SMALL_INT           2
                CALL                     1

 319            LOAD_ATTR               47 (execute + NULL|self)
                CALL                     0

 314            STORE_FAST              20 (existing)

 321            LOAD_GLOBAL             49 (list + NULL)
                LOAD_GLOBAL             51 (getattr + NULL)
                LOAD_FAST_BORROW        20 (existing)
                LOAD_CONST              13 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L19)
       L17:     NOT_TAKEN
       L18:     POP_TOP
                BUILD_LIST               0
       L19:     CALL                     1
                STORE_FAST              21 (rows)

 322            LOAD_FAST_BORROW        21 (rows)
                TO_BOOL
                EXTENDED_ARG             1
                POP_JUMP_IF_FALSE      261 (to L37)
       L20:     NOT_TAKEN

 323   L21:     LOAD_FAST_BORROW        21 (rows)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                STORE_FAST              22 (row)

 324            LOAD_GLOBAL             25 (int + NULL)
                LOAD_FAST_BORROW        22 (row)
                LOAD_ATTR               53 (get + NULL|self)
                LOAD_CONST              14 ('request_count')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L24)
       L22:     NOT_TAKEN
       L23:     POP_TOP
                LOAD_SMALL_INT           0
       L24:     CALL                     1
                LOAD_FAST_BORROW        16 (req_delta)
                BINARY_OP                0 (+)
                STORE_FAST              23 (new_req)

 325            LOAD_GLOBAL             25 (int + NULL)
                LOAD_FAST_BORROW        22 (row)
                LOAD_ATTR               53 (get + NULL|self)
                LOAD_CONST              15 ('blocked_count')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L27)
       L25:     NOT_TAKEN
       L26:     POP_TOP
                LOAD_SMALL_INT           0
       L27:     CALL                     1
                LOAD_FAST_BORROW        17 (blk_delta)
                BINARY_OP                0 (+)
                STORE_FAST              24 (new_blk)

 327            LOAD_CONST              14 ('request_count')
                LOAD_FAST_BORROW        23 (new_req)

 328            LOAD_CONST              15 ('blocked_count')
                LOAD_FAST_BORROW        24 (new_blk)

 329            LOAD_CONST              16 ('last_request_at')
                LOAD_FAST_BORROW        18 (now_iso)

 326            BUILD_MAP                3
                STORE_FAST              25 (patch)

 332            LOAD_FAST_BORROW        19 (db)
                LOAD_ATTR               33 (table + NULL|self)
                LOAD_GLOBAL             34 (_TABLE)
                CALL                     1

 333            LOAD_ATTR               55 (update + NULL|self)
                LOAD_FAST_BORROW        25 (patch)
                CALL                     1

 334            LOAD_ATTR               43 (eq + NULL|self)
                LOAD_CONST              12 ('bucket_key')
                LOAD_FAST_BORROW        10 (bk)
                CALL                     2

 335            LOAD_ATTR               47 (execute + NULL|self)
                CALL                     0

 331            STORE_FAST              26 (upd)

 337            LOAD_GLOBAL             49 (list + NULL)
                LOAD_GLOBAL             51 (getattr + NULL)
                LOAD_FAST_BORROW        26 (upd)
                LOAD_CONST              13 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L30)
       L28:     NOT_TAKEN
       L29:     POP_TOP
                BUILD_LIST               0
       L30:     CALL                     1
                STORE_FAST              27 (rows_after)

 338            LOAD_FAST_BORROW        27 (rows_after)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L33)
       L31:     NOT_TAKEN
       L32:     LOAD_GLOBAL             57 (_project_row + NULL)
                LOAD_FAST_BORROW        27 (rows_after)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                CALL                     1
                JUMP_FORWARD             1 (to L34)
       L33:     LOAD_CONST               1 (None)
       L34:     STORE_FAST              28 (proj)

 339            LOAD_FAST_BORROW        28 (proj)
                POP_JUMP_IF_NOT_NONE    16 (to L35)
                NOT_TAKEN

 342            LOAD_GLOBAL             57 (_project_row + NULL)
                BUILD_MAP                0
                LOAD_FAST_BORROW        22 (row)
                DICT_UPDATE              1
                LOAD_FAST_BORROW        25 (patch)
                DICT_UPDATE              1
                CALL                     1
                STORE_FAST              28 (proj)

 344   L35:     LOAD_CONST               2 ('status')
                LOAD_CONST              17 ('ok')

 345            LOAD_CONST               4 ('backend')
                LOAD_CONST              18 ('db')

 346            LOAD_CONST               5 ('counter')
                LOAD_FAST_BORROW        28 (proj)

 347            LOAD_CONST               6 ('warnings')
                BUILD_LIST               0

 348            LOAD_CONST               7 ('error_code')
                LOAD_CONST               1 (None)

 343            BUILD_MAP                5
       L36:     RETURN_VALUE

 352   L37:     LOAD_CONST              12 ('bucket_key')
                LOAD_FAST_BORROW        10 (bk)

 353            LOAD_CONST              19 ('brokerage_id')
                LOAD_FAST_BORROW        11 (bid)

 354            LOAD_CONST              20 ('surface')
                LOAD_FAST_BORROW         1 (surface)

 355            LOAD_CONST              21 ('actor_type')
                LOAD_FAST_BORROW         5 (actor_type)

 356            LOAD_CONST              22 ('actor_id')
                LOAD_FAST_BORROW        12 (actor)

 357            LOAD_CONST              23 ('window_start')
                LOAD_FAST_BORROW        14 (ws)

 358            LOAD_CONST              24 ('window_end')
                LOAD_FAST_BORROW        15 (we)

 359            LOAD_CONST              14 ('request_count')
                LOAD_FAST_BORROW        16 (req_delta)

 360            LOAD_CONST              15 ('blocked_count')
                LOAD_FAST_BORROW        17 (blk_delta)

 361            LOAD_CONST              16 ('last_request_at')
                LOAD_FAST_BORROW        18 (now_iso)

 362            LOAD_CONST              25 ('metadata')
                LOAD_FAST_BORROW        13 (md)

 351            BUILD_MAP               11
                STORE_FAST              22 (row)

 364            LOAD_FAST_BORROW        19 (db)
                LOAD_ATTR               33 (table + NULL|self)
                LOAD_GLOBAL             34 (_TABLE)
                CALL                     1
                LOAD_ATTR               59 (insert + NULL|self)
                LOAD_FAST_BORROW        22 (row)
                CALL                     1
                LOAD_ATTR               47 (execute + NULL|self)
                CALL                     0
                STORE_FAST              29 (ins)

 365            LOAD_GLOBAL             49 (list + NULL)
                LOAD_GLOBAL             51 (getattr + NULL)
                LOAD_FAST_BORROW        29 (ins)
                LOAD_CONST              13 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L40)
       L38:     NOT_TAKEN
       L39:     POP_TOP
                BUILD_LIST               0
       L40:     CALL                     1
                STORE_FAST              27 (rows_after)

 366            LOAD_FAST_BORROW        27 (rows_after)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L43)
       L41:     NOT_TAKEN
       L42:     LOAD_GLOBAL             57 (_project_row + NULL)
                LOAD_FAST_BORROW        27 (rows_after)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                CALL                     1
                JUMP_FORWARD            10 (to L44)
       L43:     LOAD_GLOBAL             57 (_project_row + NULL)
                LOAD_FAST_BORROW        22 (row)
                CALL                     1
       L44:     STORE_FAST              28 (proj)

 368            LOAD_CONST               2 ('status')
                LOAD_CONST              17 ('ok')

 369            LOAD_CONST               4 ('backend')
                LOAD_CONST              18 ('db')

 370            LOAD_CONST               5 ('counter')
                LOAD_FAST_BORROW        28 (proj)

 371            LOAD_CONST               6 ('warnings')
                BUILD_LIST               0

 372            LOAD_CONST               7 ('error_code')
                LOAD_CONST               1 (None)

 367            BUILD_MAP                5
       L45:     RETURN_VALUE

 380   L46:     LOAD_GLOBAL             70 (_local_lock)
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
       L47:     POP_TOP

 381            LOAD_GLOBAL             73 (dict + NULL)
                LOAD_GLOBAL             74 (_local_store)
                LOAD_ATTR               53 (get + NULL|self)
                LOAD_FAST_BORROW        10 (bk)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L48)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
       L48:     CALL                     1
                STORE_FAST              31 (cur)

 382            LOAD_FAST_BORROW        31 (cur)
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L51)
       L49:     NOT_TAKEN

 384   L50:     LOAD_CONST              12 ('bucket_key')
                LOAD_FAST_BORROW        10 (bk)

 385            LOAD_CONST              19 ('brokerage_id')
                LOAD_FAST_BORROW        11 (bid)

 386            LOAD_CONST              20 ('surface')
                LOAD_FAST_BORROW         1 (surface)

 387            LOAD_CONST              21 ('actor_type')
                LOAD_FAST_BORROW         5 (actor_type)

 388            LOAD_CONST              22 ('actor_id')
                LOAD_FAST_BORROW        12 (actor)

 389            LOAD_CONST              23 ('window_start')
                LOAD_FAST_BORROW        14 (ws)

 390            LOAD_CONST              24 ('window_end')
                LOAD_FAST_BORROW        15 (we)

 391            LOAD_CONST              14 ('request_count')
                LOAD_SMALL_INT           0

 392            LOAD_CONST              15 ('blocked_count')
                LOAD_SMALL_INT           0

 393            LOAD_CONST              16 ('last_request_at')
                LOAD_FAST_BORROW        18 (now_iso)

 394            LOAD_CONST              25 ('metadata')
                LOAD_FAST_BORROW        13 (md)

 383            BUILD_MAP               11
                STORE_FAST              31 (cur)

 396   L51:     LOAD_GLOBAL             25 (int + NULL)
                LOAD_FAST_BORROW        31 (cur)
                LOAD_ATTR               53 (get + NULL|self)
                LOAD_CONST              14 ('request_count')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L54)
       L52:     NOT_TAKEN
       L53:     POP_TOP
                LOAD_SMALL_INT           0
       L54:     CALL                     1
                LOAD_FAST_BORROW        16 (req_delta)
                BINARY_OP                0 (+)
                LOAD_FAST_BORROW        31 (cur)
                LOAD_CONST              14 ('request_count')
                STORE_SUBSCR

 397            LOAD_GLOBAL             25 (int + NULL)
                LOAD_FAST_BORROW        31 (cur)
                LOAD_ATTR               53 (get + NULL|self)
                LOAD_CONST              15 ('blocked_count')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L57)
       L55:     NOT_TAKEN
       L56:     POP_TOP
                LOAD_SMALL_INT           0
       L57:     CALL                     1
                LOAD_FAST_BORROW        17 (blk_delta)
                BINARY_OP                0 (+)
                LOAD_FAST_BORROW        31 (cur)
                LOAD_CONST              15 ('blocked_count')
                STORE_SUBSCR

 398            LOAD_FAST_BORROW        18 (now_iso)
                LOAD_FAST_BORROW        31 (cur)
                LOAD_CONST              16 ('last_request_at')
                STORE_SUBSCR

 399            LOAD_FAST_BORROW        31 (cur)
                LOAD_GLOBAL             74 (_local_store)
                LOAD_FAST_BORROW        10 (bk)
                STORE_SUBSCR

 380   L58:     LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                CALL                     3
                POP_TOP

 401   L59:     LOAD_CONST               2 ('status')
                LOAD_CONST              17 ('ok')

 402            LOAD_CONST               4 ('backend')
                LOAD_CONST              27 ('process_local')

 403            LOAD_CONST               5 ('counter')
                LOAD_GLOBAL             57 (_project_row + NULL)
                LOAD_FAST_CHECK         31 (cur)
                CALL                     1

 404            LOAD_CONST               6 ('warnings')
                LOAD_CONST              28 ('rate_limit_store_process_local')
                BUILD_LIST               1

 405            LOAD_CONST               7 ('error_code')
                LOAD_CONST               1 (None)

 400            BUILD_MAP                5
                RETURN_VALUE

  --   L60:     PUSH_EXC_INFO

 302            LOAD_GLOBAL             26 (TypeError)
                LOAD_GLOBAL             28 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        7 (to L62)
                NOT_TAKEN
                POP_TOP

 303            LOAD_SMALL_INT           0
                STORE_FAST              16 (req_delta)
       L61:     POP_EXCEPT
                EXTENDED_ARG             3
                JUMP_BACKWARD_NO_INTERRUPT 858 (to L13)

 302   L62:     RERAISE                  0

  --   L63:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L64:     PUSH_EXC_INFO

 306            LOAD_GLOBAL             26 (TypeError)
                LOAD_GLOBAL             28 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        7 (to L66)
                NOT_TAKEN
                POP_TOP

 307            LOAD_SMALL_INT           0
                STORE_FAST              17 (blk_delta)
       L65:     POP_EXCEPT
                EXTENDED_ARG             3
                JUMP_BACKWARD_NO_INTERRUPT 862 (to L15)

 306   L66:     RERAISE                  0

  --   L67:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L68:     PUSH_EXC_INFO

 374            LOAD_GLOBAL             60 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       55 (to L72)
                NOT_TAKEN
                STORE_FAST              30 (e)

 375   L69:     LOAD_GLOBAL             62 (logger)
                LOAD_ATTR               65 (warning + NULL|self)

 376            LOAD_CONST              26 ('increment_counter db error type=')
                LOAD_GLOBAL             67 (type + NULL)
                LOAD_FAST               30 (e)
                CALL                     1
                LOAD_ATTR               68 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 375            CALL                     1
                POP_TOP
       L70:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              30 (e)
                DELETE_FAST             30 (e)
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 335 (to L46)

  --   L71:     LOAD_CONST               1 (None)
                STORE_FAST              30 (e)
                DELETE_FAST             30 (e)
                RERAISE                  1

 374   L72:     RERAISE                  0

  --   L73:     COPY                     3
                POP_EXCEPT
                RERAISE                  1

 380   L74:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L75)
                NOT_TAKEN
                RERAISE                  2
       L75:     POP_TOP
       L76:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
                JUMP_BACKWARD_NO_INTERRUPT 158 (to L59)

  --   L77:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L12 to L13 -> L60 [0]
  L14 to L15 -> L64 [0]
  L16 to L17 -> L68 [0]
  L18 to L20 -> L68 [0]
  L21 to L22 -> L68 [0]
  L23 to L25 -> L68 [0]
  L26 to L28 -> L68 [0]
  L29 to L31 -> L68 [0]
  L32 to L36 -> L68 [0]
  L37 to L38 -> L68 [0]
  L39 to L41 -> L68 [0]
  L42 to L45 -> L68 [0]
  L47 to L49 -> L74 [2] lasti
  L50 to L52 -> L74 [2] lasti
  L53 to L55 -> L74 [2] lasti
  L56 to L58 -> L74 [2] lasti
  L60 to L61 -> L63 [1] lasti
  L62 to L63 -> L63 [1] lasti
  L64 to L65 -> L67 [1] lasti
  L66 to L67 -> L67 [1] lasti
  L68 to L69 -> L73 [1] lasti
  L69 to L70 -> L71 [1] lasti
  L71 to L73 -> L73 [1] lasti
  L74 to L76 -> L77 [4] lasti
```
