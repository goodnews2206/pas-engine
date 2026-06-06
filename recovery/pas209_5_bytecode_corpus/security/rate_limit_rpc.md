# security/rate_limit_rpc

- **pyc:** `app\services\security\__pycache__\rate_limit_rpc.cpython-314.pyc`
- **expected source path (absent):** `app\services\security/rate_limit_rpc.py`
- **co_filename (from bytecode):** `app/services/security/rate_limit_rpc.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** security

## Module docstring

```
PAS-SECURITY-03 — Atomic rate-limit RPC service.

Wraps the v33 ``pas_increment_rate_limit_counter`` RPC with a
safe fallback to the PAS-SECURITY-02
``rate_limit_store.increment_counter`` SELECT+UPDATE path.

Doctrine:

* **Prefer atomic RPC.** When the v33 function is promoted in
  Supabase, every increment is a single round-trip UPSERT —
  no race window.
* **Fallback when RPC unavailable.** A pre-v33 deployment
  collapses to the PAS-SECURITY-02 store. The fallback emits
  a structural warning so callers can surface ``backend="store"``
  / ``rpc_available=False``.
* **NEVER raises.** All helpers return structural envelopes.
* **No raw IP / user-agent / API key / signature** stored or
  returned. Bucket key + actor_id columns are sha256
  fingerprints. The RPC's parameters are bounded by v31 +
  v33 CHECK constraints.

Public surface:

  * ``ALLOWED_RPC_BACKENDS``                        — closed enum.
  * ``atomic_rate_limit_available()``               — bool.
  * ``increment_rate_limit_counter_atomic(...)``    — envelope.
  * ``atomic_rate_limit_report(...)``               — diagnostic envelope.
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `Tuple`, `__future__`, `annotations`, `app.db.supabase_client`, `app.services.security.rate_limit_store`, `datetime`, `get_supabase`, `increment_counter`, `logging`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_get_db_safe`, `_now_iso`, `_safe_envelope`, `atomic_rate_limit_available`, `atomic_rate_limit_report`, `increment_rate_limit_counter_atomic`

## Env-key candidates

`ALLOWED_RPC_BACKENDS`, `SYSTEM`

## String constants (redacted where noted)

- '\nPAS-SECURITY-03 — Atomic rate-limit RPC service.\n\nWraps the v33 ``pas_increment_rate_limit_counter`` RPC with a\nsafe fallback to the PAS-SECURITY-02\n``rate_limit_store.increment_counter`` SELECT+UPDATE path.\n\nDoctrine:\n\n* **Prefer atomic RPC.** When the v33 function is promoted in\n  Supabase, every increment is a single round-trip UPSERT —\n  no race window.\n* **Fallback when RPC unavailable.** A pre-v33 deployment\n  collapses to the PAS-SECURITY-02 store. The fallback emits\n  a structural warning so callers can surface ``backend="store"``\n  / ``rpc_available=False``.\n* **NEVER raises.** All helpers return structural envelopes.\n* **No raw IP / user-agent / API key / signature** stored or\n  returned. Bucket key + actor_id columns are sha256\n  fingerprints. The RPC\'s parameters are bounded by v31 +\n  v33 CHECK constraints.\n\nPublic surface:\n\n  * ``ALLOWED_RPC_BACKENDS``                        — closed enum.\n  * ``atomic_rate_limit_available()``               — bool.\n  * ``increment_rate_limit_counter_atomic(...)``    — envelope.\n  * ``atomic_rate_limit_report(...)``               — diagnostic envelope.\n'
- 'pas.security.rate_limit_rpc'
- 'pas_increment_rate_limit_counter'
- 'Tuple[str, ...]'
- 'ALLOWED_RPC_BACKENDS'
- 'request_count'
- 'blocked_count'
- 'window_start'
- 'window_end'
- 'rpc_available'
- 'warnings'
- 'error_code'
- 'brokerage_id'
- 'actor_type'
- 'actor_id'
- 'request_count_delta'
- 'blocked_delta'
- 'return'
- 'str'
- 'seconds'
- 'rate_limit_rpc db client unavailable type='
- 'bool'
- "Best-effort detection of the v33 RPC's availability.\nNEVER raises. Returns True only when a smoke-test RPC call\nsucceeds; returns False otherwise (caller falls back to the\nPAS-SECURITY-02 store).\n\nThe smoke test uses a no-op bucket key with\n``p_request_delta=0`` and ``p_blocked_delta=0`` so the\ncounter table is not mutated by the probe itself."
- 'p_bucket_key'
- 'rpc_smoke_probe_pas_security_03'
- 'p_surface'
- 'tenant_api'
- 'p_brokerage_id'
- 'p_actor_type'
- 'SYSTEM'
- 'p_actor_id'
- 'p_window_start'
- 'p_window_end'
- 'p_max_requests'
- 'p_request_delta'
- 'p_blocked_delta'
- 'data'
- 'atomic_rate_limit_available smoke probe failed type='
- 'backend'
- 'Optional[str]'
- 'allowed'
- 'int'
- 'Optional[List[str]]'
- 'Dict[str, Any]'
- 'bucket_key'
- 'surface'
- 'max_requests'
- 'Atomically increment via the v33 RPC. NEVER raises.\n\nOutcomes:\n  * ``backend="rpc"``           — RPC executed; structural verdict.\n  * ``backend="store"``          — fallback to PAS-SECURITY-02 SELECT+UPDATE.\n  * ``backend="process_local"`` — DB unavailable, in-memory dict.\n'
- 'invalid_bucket_key'
- 'invalid_surface'
- 'invalid_actor_type'
- 'rpc'
- 'warning_code'
- 'increment_rate_limit_counter_atomic RPC returned empty data; falling back to PAS-SECURITY-02 store.'
- 'increment_rate_limit_counter_atomic RPC error type='
- '; falling back to store'
- 'event'
- 'security.rate_limit.rpc_unavailable'
- 'counter'
- 'store'
- 'rate_limit_rpc_unavailable'
- 'increment_rate_limit_counter_atomic fallback error type='
- 'rate_limit_rpc_fallback_unexpected:'
- 'rate_limit_rpc_unexpected'
- 'Diagnostic envelope describing the current backend\navailability. NEVER raises. NEVER returns secrets.'
- 'atomic_rate_limit_report error type='
- 'rpc_name'

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS-SECURITY-03 — Atomic rate-limit RPC service.\n\nWraps the v33 ``pas_increment_rate_limit_counter`` RPC with a\nsafe fallback to the PAS-SECURITY-02\n``rate_limit_store.increment_counter`` SELECT+UPDATE path.\n\nDoctrine:\n\n* **Prefer atomic RPC.** When the v33 function is promoted in\n  Supabase, every increment is a single round-trip UPSERT —\n  no race window.\n* **Fallback when RPC unavailable.** A pre-v33 deployment\n  collapses to the PAS-SECURITY-02 store. The fallback emits\n  a structural warning so callers can surface ``backend="store"``\n  / ``rpc_available=False``.\n* **NEVER raises.** All helpers return structural envelopes.\n* **No raw IP / user-agent / API key / signature** stored or\n  returned. Bucket key + actor_id columns are sha256\n  fingerprints. The RPC\'s parameters are bounded by v31 +\n  v33 CHECK constraints.\n\nPublic surface:\n\n  * ``ALLOWED_RPC_BACKENDS``                        — closed enum.\n  * ``atomic_rate_limit_available()``               — bool.\n  * ``increment_rate_limit_counter_atomic(...)``    — envelope.\n  * ``atomic_rate_limit_report(...)``               — diagnostic envelope.\n')
               STORE_NAME               1 (__doc__)

  31           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  33           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (logging)
               STORE_NAME               4 (logging)

  34           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              5 (datetime)
               IMPORT_FROM              5 (datetime)
               STORE_NAME               5 (datetime)
               IMPORT_FROM              6 (timezone)
               STORE_NAME               6 (timezone)
               POP_TOP

  35           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Any', 'Dict', 'List', 'Optional', 'Tuple'))
               IMPORT_NAME              7 (typing)
               IMPORT_FROM              8 (Any)
               STORE_NAME               8 (Any)
               IMPORT_FROM              9 (Dict)
               STORE_NAME               9 (Dict)
               IMPORT_FROM             10 (List)
               STORE_NAME              10 (List)
               IMPORT_FROM             11 (Optional)
               STORE_NAME              11 (Optional)
               IMPORT_FROM             12 (Tuple)
               STORE_NAME              12 (Tuple)
               POP_TOP

  38           LOAD_NAME                4 (logging)
               LOAD_ATTR               26 (getLogger)
               PUSH_NULL
               LOAD_CONST               5 ('pas.security.rate_limit_rpc')
               CALL                     1
               STORE_NAME              14 (logger)

  41           LOAD_CONST               6 ('pas_increment_rate_limit_counter')
               STORE_NAME              15 (_RPC_NAME)

  45           LOAD_CONST              33 (('rpc', 'store', 'process_local'))
               STORE_NAME              16 (ALLOWED_RPC_BACKENDS)
               LOAD_CONST               7 ('Tuple[str, ...]')
               LOAD_NAME               17 (__annotations__)
               LOAD_CONST               8 ('ALLOWED_RPC_BACKENDS')
               STORE_SUBSCR

  49           LOAD_CONST              34 (('email_ingestion', 'slack_command', 'admin', 'tenant_api', 'api_key_rotation', 'webhook_generic', 'webhook_followupboss', 'webhook_gohighlevel', 'webhook_zapier'))
               STORE_NAME              18 (_ALLOWED_SURFACES)

  61           LOAD_CONST              35 (('TENANT', 'OPERATOR', 'ADMIN', 'SYSTEM', 'ANON'))
               STORE_NAME              19 (_ALLOWED_ACTOR_TYPES)

  64           LOAD_CONST               9 (<code object __annotate__ at 0x0000018C17FA3960, file "app/services/security/rate_limit_rpc.py", line 64>)
               MAKE_FUNCTION
               LOAD_CONST              10 (<code object _now_iso at 0x0000018C180392F0, file "app/services/security/rate_limit_rpc.py", line 64>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              20 (_now_iso)

  68           LOAD_CONST              11 (<code object _get_db_safe at 0x0000018C17FF10B0, file "app/services/security/rate_limit_rpc.py", line 68>)
               MAKE_FUNCTION
               STORE_NAME              21 (_get_db_safe)

  79           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA30F0, file "app/services/security/rate_limit_rpc.py", line 79>)
               MAKE_FUNCTION
               LOAD_CONST              13 (<code object atomic_rate_limit_available at 0x0000018C17D76780, file "app/services/security/rate_limit_rpc.py", line 79>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              22 (atomic_rate_limit_available)

 119           LOAD_CONST              14 ('request_count')

 123           LOAD_SMALL_INT           0

 119           LOAD_CONST              15 ('blocked_count')

 124           LOAD_SMALL_INT           0

 119           LOAD_CONST              16 ('window_start')

 125           LOAD_CONST               2 (None)

 119           LOAD_CONST              17 ('window_end')

 126           LOAD_CONST               2 (None)

 119           LOAD_CONST              18 ('rpc_available')

 127           LOAD_CONST              19 (False)

 119           LOAD_CONST              20 ('warnings')

 128           LOAD_CONST               2 (None)

 119           LOAD_CONST              21 ('error_code')

 129           LOAD_CONST               2 (None)

 119           BUILD_MAP                7
               LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FBFEE0, file "app/services/security/rate_limit_rpc.py", line 119>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object _safe_envelope at 0x0000018C17F95E60, file "app/services/security/rate_limit_rpc.py", line 119>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              23 (_safe_envelope)

 144           LOAD_CONST              24 ('brokerage_id')

 151           LOAD_CONST               2 (None)

 144           LOAD_CONST              25 ('actor_type')

 152           LOAD_CONST               2 (None)

 144           LOAD_CONST              26 ('actor_id')

 153           LOAD_CONST               2 (None)

 144           LOAD_CONST              27 ('request_count_delta')

 154           LOAD_SMALL_INT           1

 144           LOAD_CONST              28 ('blocked_delta')

 155           LOAD_SMALL_INT           0

 144           BUILD_MAP                5
               LOAD_CONST              29 (<code object __annotate__ at 0x0000018C18053510, file "app/services/security/rate_limit_rpc.py", line 144>)
               MAKE_FUNCTION
               LOAD_CONST              30 (<code object increment_rate_limit_counter_atomic at 0x0000018C17EAB7F0, file "app/services/security/rate_limit_rpc.py", line 144>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              24 (increment_rate_limit_counter_atomic)

 306           LOAD_CONST              31 (<code object __annotate__ at 0x0000018C17FA33C0, file "app/services/security/rate_limit_rpc.py", line 306>)
               MAKE_FUNCTION
               LOAD_CONST              32 (<code object atomic_rate_limit_report at 0x0000018C1794ED80, file "app/services/security/rate_limit_rpc.py", line 306>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              25 (atomic_rate_limit_report)

 324           BUILD_LIST               0
               LOAD_CONST              36 (('ALLOWED_RPC_BACKENDS', 'atomic_rate_limit_available', 'increment_rate_limit_counter_atomic', 'atomic_rate_limit_report'))
               LIST_EXTEND              1
               STORE_NAME              26 (__all__)
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "app/services/security/rate_limit_rpc.py", line 64>:
 64           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('str')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _now_iso at 0x0000018C180392F0, file "app/services/security/rate_limit_rpc.py", line 64>:
 64           RESUME                   0

 65           LOAD_GLOBAL              0 (datetime)
              LOAD_ATTR                2 (now)
              PUSH_NULL
              LOAD_GLOBAL              4 (timezone)
              LOAD_ATTR                6 (utc)
              CALL                     1
              LOAD_ATTR                9 (isoformat + NULL|self)
              LOAD_CONST               0 ('seconds')
              LOAD_CONST               1 (('timespec',))
              CALL_KW                  1
              RETURN_VALUE

Disassembly of <code object _get_db_safe at 0x0000018C17FF10B0, file "app/services/security/rate_limit_rpc.py", line 68>:
  68           RESUME                   0

  69           NOP

  70   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('get_supabase',))
               IMPORT_NAME              0 (app.db.supabase_client)
               IMPORT_FROM              1 (get_supabase)
               STORE_FAST               0 (get_supabase)
               POP_TOP

  71           LOAD_FAST_BORROW         0 (get_supabase)
               PUSH_NULL
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

  72           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       55 (to L7)
               NOT_TAKEN
               STORE_FAST               1 (e)

  73   L4:     LOAD_GLOBAL              6 (logger)
               LOAD_ATTR                9 (warning + NULL|self)

  74           LOAD_CONST               2 ('rate_limit_rpc db client unavailable type=')
               LOAD_GLOBAL             11 (type + NULL)
               LOAD_FAST                1 (e)
               CALL                     1
               LOAD_ATTR               12 (__name__)
               FORMAT_SIMPLE
               BUILD_STRING             2

  73           CALL                     1
               POP_TOP

  76   L5:     POP_EXCEPT
               LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               LOAD_CONST               3 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               RERAISE                  1

  72   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA30F0, file "app/services/security/rate_limit_rpc.py", line 79>:
 79           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('bool')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object atomic_rate_limit_available at 0x0000018C17D76780, file "app/services/security/rate_limit_rpc.py", line 79>:
  79           RESUME                   0

  88           LOAD_GLOBAL              1 (_get_db_safe + NULL)
               CALL                     0
               STORE_FAST               0 (db)

  89           LOAD_FAST_BORROW         0 (db)
               POP_JUMP_IF_NOT_NONE     3 (to L1)
               NOT_TAKEN

  90           LOAD_CONST               2 (False)
               RETURN_VALUE

  91   L1:     NOP

  93   L2:     LOAD_CONST               3 ('p_bucket_key')
               LOAD_CONST               4 ('rpc_smoke_probe_pas_security_03')

  94           LOAD_CONST               5 ('p_surface')
               LOAD_CONST               6 ('tenant_api')

  95           LOAD_CONST               7 ('p_brokerage_id')
               LOAD_CONST               1 (None)

  96           LOAD_CONST               8 ('p_actor_type')
               LOAD_CONST               9 ('SYSTEM')

  97           LOAD_CONST              10 ('p_actor_id')
               LOAD_CONST               1 (None)

  98           LOAD_CONST              11 ('p_window_start')
               LOAD_GLOBAL              3 (_now_iso + NULL)
               CALL                     0

  99           LOAD_CONST              12 ('p_window_end')
               LOAD_GLOBAL              3 (_now_iso + NULL)
               CALL                     0

 100           LOAD_CONST              13 ('p_max_requests')
               LOAD_SMALL_INT           1

 101           LOAD_CONST              14 ('p_request_delta')
               LOAD_SMALL_INT           0

 102           LOAD_CONST              15 ('p_blocked_delta')
               LOAD_SMALL_INT           0

  92           BUILD_MAP               10
               STORE_FAST               1 (smoke_args)

 104           LOAD_FAST_BORROW         0 (db)
               LOAD_ATTR                5 (rpc + NULL|self)
               LOAD_GLOBAL              6 (_RPC_NAME)
               LOAD_FAST_BORROW         1 (smoke_args)
               CALL                     2
               LOAD_ATTR                9 (execute + NULL|self)
               CALL                     0
               STORE_FAST               2 (result)

 109           LOAD_GLOBAL             11 (getattr + NULL)
               LOAD_FAST_BORROW         2 (result)
               LOAD_CONST              16 ('data')
               LOAD_CONST               1 (None)
               CALL                     3
               STORE_FAST               3 (_)

 110   L3:     LOAD_CONST              17 (True)
               RETURN_VALUE

  --   L4:     PUSH_EXC_INFO

 111           LOAD_GLOBAL             12 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       55 (to L8)
               NOT_TAKEN
               STORE_FAST               4 (e)

 112   L5:     LOAD_GLOBAL             14 (logger)
               LOAD_ATTR               17 (warning + NULL|self)

 113           LOAD_CONST              18 ('atomic_rate_limit_available smoke probe failed type=')

 114           LOAD_GLOBAL             19 (type + NULL)
               LOAD_FAST                4 (e)
               CALL                     1
               LOAD_ATTR               20 (__name__)
               FORMAT_SIMPLE

 113           BUILD_STRING             2

 112           CALL                     1
               POP_TOP

 116   L6:     POP_EXCEPT
               LOAD_CONST               1 (None)
               STORE_FAST               4 (e)
               DELETE_FAST              4 (e)
               LOAD_CONST               2 (False)
               RETURN_VALUE

  --   L7:     LOAD_CONST               1 (None)
               STORE_FAST               4 (e)
               DELETE_FAST              4 (e)
               RERAISE                  1

 111   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L4 [0]
  L4 to L5 -> L9 [1] lasti
  L5 to L6 -> L7 [1] lasti
  L7 to L9 -> L9 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FBFEE0, file "app/services/security/rate_limit_rpc.py", line 119>:
119           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('backend')

121           LOAD_CONST               2 ('Optional[str]')

119           LOAD_CONST               3 ('allowed')

122           LOAD_CONST               4 ('bool')

119           LOAD_CONST               5 ('request_count')

123           LOAD_CONST               6 ('int')

119           LOAD_CONST               7 ('blocked_count')

124           LOAD_CONST               6 ('int')

119           LOAD_CONST               8 ('window_start')

125           LOAD_CONST               2 ('Optional[str]')

119           LOAD_CONST               9 ('window_end')

126           LOAD_CONST               2 ('Optional[str]')

119           LOAD_CONST              10 ('rpc_available')

127           LOAD_CONST               4 ('bool')

119           LOAD_CONST              11 ('warnings')

128           LOAD_CONST              12 ('Optional[List[str]]')

119           LOAD_CONST              13 ('error_code')

129           LOAD_CONST               2 ('Optional[str]')

119           LOAD_CONST              14 ('return')

130           LOAD_CONST              15 ('Dict[str, Any]')

119           BUILD_MAP               10
              RETURN_VALUE

Disassembly of <code object _safe_envelope at 0x0000018C17F95E60, file "app/services/security/rate_limit_rpc.py", line 119>:
119           RESUME                   0

132           LOAD_CONST               0 ('backend')
              LOAD_FAST                0 (backend)

133           LOAD_CONST               1 ('allowed')
              LOAD_GLOBAL              1 (bool + NULL)
              LOAD_FAST_BORROW         1 (allowed)
              CALL                     1

134           LOAD_CONST               2 ('request_count')
              LOAD_GLOBAL              3 (int + NULL)
              LOAD_FAST_BORROW         2 (request_count)
              CALL                     1

135           LOAD_CONST               3 ('blocked_count')
              LOAD_GLOBAL              3 (int + NULL)
              LOAD_FAST_BORROW         3 (blocked_count)
              CALL                     1

136           LOAD_CONST               4 ('window_start')
              LOAD_FAST                4 (window_start)

137           LOAD_CONST               5 ('window_end')
              LOAD_FAST                5 (window_end)

138           LOAD_CONST               6 ('rpc_available')
              LOAD_GLOBAL              1 (bool + NULL)
              LOAD_FAST_BORROW         6 (rpc_available)
              CALL                     1

139           LOAD_CONST               7 ('warnings')
              LOAD_GLOBAL              5 (list + NULL)
              LOAD_FAST                7 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

140           LOAD_CONST               8 ('error_code')
              LOAD_FAST_BORROW         8 (error_code)

131           BUILD_MAP                9
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18053510, file "app/services/security/rate_limit_rpc.py", line 144>:
144           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('bucket_key')

146           LOAD_CONST               2 ('str')

144           LOAD_CONST               3 ('surface')

147           LOAD_CONST               2 ('str')

144           LOAD_CONST               4 ('window_start')

148           LOAD_CONST               2 ('str')

144           LOAD_CONST               5 ('window_end')

149           LOAD_CONST               2 ('str')

144           LOAD_CONST               6 ('max_requests')

150           LOAD_CONST               7 ('int')

144           LOAD_CONST               8 ('brokerage_id')

151           LOAD_CONST               9 ('Optional[str]')

144           LOAD_CONST              10 ('actor_type')

152           LOAD_CONST               9 ('Optional[str]')

144           LOAD_CONST              11 ('actor_id')

153           LOAD_CONST               9 ('Optional[str]')

144           LOAD_CONST              12 ('request_count_delta')

154           LOAD_CONST               7 ('int')

144           LOAD_CONST              13 ('blocked_delta')

155           LOAD_CONST               7 ('int')

144           LOAD_CONST              14 ('return')

156           LOAD_CONST              15 ('Dict[str, Any]')

144           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object increment_rate_limit_counter_atomic at 0x0000018C17EAB7F0, file "app/services/security/rate_limit_rpc.py", line 144>:
 144            RESUME                   0

 168            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (bucket_key)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       39 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (bucket_key)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L1)
                NOT_TAKEN
                LOAD_GLOBAL              7 (len + NULL)
                LOAD_FAST_BORROW         0 (bucket_key)
                CALL                     1
                LOAD_SMALL_INT         200
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE       17 (to L2)
                NOT_TAKEN

 169    L1:     LOAD_GLOBAL              9 (_safe_envelope + NULL)

 170            LOAD_CONST               1 (None)

 171            LOAD_CONST               2 (True)

 172            LOAD_CONST               3 ('invalid_bucket_key')
                BUILD_LIST               1

 173            LOAD_CONST               3 ('invalid_bucket_key')

 169            LOAD_CONST               4 (('backend', 'allowed', 'warnings', 'error_code'))
                CALL_KW                  4
                RETURN_VALUE

 175    L2:     LOAD_FAST_BORROW         1 (surface)
                LOAD_GLOBAL             10 (_ALLOWED_SURFACES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       17 (to L3)
                NOT_TAKEN

 176            LOAD_GLOBAL              9 (_safe_envelope + NULL)

 177            LOAD_CONST               1 (None)

 178            LOAD_CONST               2 (True)

 179            LOAD_CONST               5 ('invalid_surface')
                BUILD_LIST               1

 180            LOAD_CONST               5 ('invalid_surface')

 176            LOAD_CONST               4 (('backend', 'allowed', 'warnings', 'error_code'))
                CALL_KW                  4
                RETURN_VALUE

 182    L3:     LOAD_FAST_BORROW         6 (actor_type)
                POP_JUMP_IF_NONE        28 (to L4)
                NOT_TAKEN
                LOAD_FAST_BORROW         6 (actor_type)
                LOAD_GLOBAL             12 (_ALLOWED_ACTOR_TYPES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       17 (to L4)
                NOT_TAKEN

 183            LOAD_GLOBAL              9 (_safe_envelope + NULL)

 184            LOAD_CONST               1 (None)

 185            LOAD_CONST               2 (True)

 186            LOAD_CONST               6 ('invalid_actor_type')
                BUILD_LIST               1

 187            LOAD_CONST               6 ('invalid_actor_type')

 183            LOAD_CONST               4 (('backend', 'allowed', 'warnings', 'error_code'))
                CALL_KW                  4
                RETURN_VALUE

 189    L4:     NOP

 190    L5:     LOAD_GLOBAL             15 (int + NULL)
                LOAD_FAST_BORROW         4 (max_requests)
                CALL                     1
                STORE_FAST              10 (max_req)

 191            LOAD_FAST_BORROW        10 (max_req)
                LOAD_SMALL_INT           0
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN

 192            LOAD_SMALL_INT           0
                STORE_FAST              10 (max_req)

 195    L6:     NOP

 196    L7:     LOAD_GLOBAL             21 (max + NULL)
                LOAD_SMALL_INT           0
                LOAD_GLOBAL             15 (int + NULL)
                LOAD_FAST                8 (request_count_delta)
                CALL                     1
                CALL                     2
                STORE_FAST              11 (req_delta)

 199    L8:     NOP

 200    L9:     LOAD_GLOBAL             21 (max + NULL)
                LOAD_SMALL_INT           0
                LOAD_GLOBAL             15 (int + NULL)
                LOAD_FAST                9 (blocked_delta)
                CALL                     1
                CALL                     2
                STORE_FAST              12 (blk_delta)

 204   L10:     LOAD_GLOBAL             23 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST              13 (db)

 205            LOAD_FAST               13 (db)
                EXTENDED_ARG             1
                POP_JUMP_IF_NONE       429 (to L32)
                NOT_TAKEN

 207            NOP

 209   L11:     LOAD_CONST               7 ('p_bucket_key')
                LOAD_FAST                0 (bucket_key)

 210            LOAD_CONST               8 ('p_surface')
                LOAD_FAST                1 (surface)

 211            LOAD_CONST               9 ('p_brokerage_id')
                LOAD_FAST                5 (brokerage_id)

 212            LOAD_CONST              10 ('p_actor_type')
                LOAD_FAST                6 (actor_type)

 213            LOAD_CONST              11 ('p_actor_id')
                LOAD_FAST                7 (actor_id)

 214            LOAD_CONST              12 ('p_window_start')
                LOAD_FAST                2 (window_start)

 215            LOAD_CONST              13 ('p_window_end')
                LOAD_FAST                3 (window_end)

 216            LOAD_CONST              14 ('p_max_requests')
                LOAD_FAST               10 (max_req)

 217            LOAD_CONST              15 ('p_request_delta')
                LOAD_FAST               11 (req_delta)

 218            LOAD_CONST              16 ('p_blocked_delta')
                LOAD_FAST               12 (blk_delta)

 208            BUILD_MAP               10
                STORE_FAST              14 (args)

 220            LOAD_FAST               13 (db)
                LOAD_ATTR               25 (rpc + NULL|self)
                LOAD_GLOBAL             26 (_RPC_NAME)
                LOAD_FAST               14 (args)
                CALL                     2
                LOAD_ATTR               29 (execute + NULL|self)
                CALL                     0
                STORE_FAST              15 (result)

 221            LOAD_GLOBAL             31 (getattr + NULL)
                LOAD_FAST               15 (result)
                LOAD_CONST              17 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                STORE_FAST              16 (data)

 224            LOAD_CONST               1 (None)
                STORE_FAST              17 (row)

 225            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST               16 (data)
                LOAD_GLOBAL             32 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        4 (to L12)
                NOT_TAKEN

 226            LOAD_FAST               16 (data)
                STORE_FAST              17 (row)
                JUMP_FORWARD            68 (to L15)

 227   L12:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST               16 (data)
                LOAD_GLOBAL             34 (list)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       47 (to L15)
                NOT_TAKEN
                LOAD_FAST               16 (data)
                TO_BOOL
                POP_JUMP_IF_FALSE       39 (to L15)
       L13:     NOT_TAKEN

 228   L14:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST               16 (data)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                LOAD_GLOBAL             32 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       10 (to L15)
                NOT_TAKEN

 229            LOAD_FAST               16 (data)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                STORE_FAST              17 (row)

 230   L15:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST               17 (row)
                LOAD_GLOBAL             32 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      219 (to L31)
                NOT_TAKEN

 231            LOAD_GLOBAL              9 (_safe_envelope + NULL)

 232            LOAD_CONST              18 ('rpc')

 233            LOAD_GLOBAL             37 (bool + NULL)
                LOAD_FAST               17 (row)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST              19 ('allowed')
                CALL                     1
                CALL                     1

 234            LOAD_GLOBAL             15 (int + NULL)
                LOAD_FAST               17 (row)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST              20 ('request_count')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L16)
                NOT_TAKEN
                POP_TOP
                LOAD_SMALL_INT           0
       L16:     CALL                     1

 235            LOAD_GLOBAL             15 (int + NULL)
                LOAD_FAST               17 (row)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST              21 ('blocked_count')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L19)
       L17:     NOT_TAKEN
       L18:     POP_TOP
                LOAD_SMALL_INT           0
       L19:     CALL                     1

 236            LOAD_FAST               17 (row)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST              22 ('window_start')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L22)
       L20:     NOT_TAKEN
       L21:     POP_TOP
                LOAD_FAST                2 (window_start)

 237   L22:     LOAD_FAST               17 (row)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST              23 ('window_end')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L25)
       L23:     NOT_TAKEN
       L24:     POP_TOP
                LOAD_FAST                3 (window_end)

 238   L25:     LOAD_CONST               2 (True)

 241            LOAD_FAST               17 (row)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST              24 ('warning_code')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L28)
       L26:     NOT_TAKEN

 240   L27:     LOAD_FAST               17 (row)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST              24 ('warning_code')
                CALL                     1
                BUILD_LIST               1
                JUMP_FORWARD             1 (to L29)

 241   L28:     BUILD_LIST               0

 243   L29:     LOAD_FAST               17 (row)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST              25 ('error_code')
                CALL                     1

 231            LOAD_CONST              26 (('backend', 'allowed', 'request_count', 'blocked_count', 'window_start', 'window_end', 'rpc_available', 'warnings', 'error_code'))
                CALL_KW                  9
       L30:     RETURN_VALUE

 247   L31:     LOAD_GLOBAL             40 (logger)
                LOAD_ATTR               43 (warning + NULL|self)

 248            LOAD_CONST              27 ('increment_rate_limit_counter_atomic RPC returned empty data; falling back to PAS-SECURITY-02 store.')

 247            CALL                     1
                POP_TOP

 260   L32:     NOP

 261   L33:     LOAD_SMALL_INT           0
                LOAD_CONST              30 (('increment_counter',))
                IMPORT_NAME             25 (app.services.security.rate_limit_store)
                IMPORT_FROM             26 (increment_counter)
                STORE_FAST              19 (increment_counter)
                POP_TOP

 262            LOAD_FAST               19 (increment_counter)
                PUSH_NULL

 263            LOAD_FAST                0 (bucket_key)

 264            LOAD_FAST                1 (surface)

 265            LOAD_FAST                2 (window_start)

 266            LOAD_FAST                3 (window_end)

 267            LOAD_FAST                5 (brokerage_id)

 268            LOAD_FAST                6 (actor_type)

 269            LOAD_FAST                7 (actor_id)

 270            LOAD_FAST               11 (req_delta)

 271            LOAD_FAST               12 (blk_delta)

 272            LOAD_CONST              31 ('event')
                LOAD_CONST              32 ('security.rate_limit.rpc_unavailable')
                BUILD_MAP                1

 262            LOAD_CONST              33 (('bucket_key', 'surface', 'window_start', 'window_end', 'brokerage_id', 'actor_type', 'actor_id', 'request_count_delta', 'blocked_delta', 'metadata'))
                CALL_KW                 10
                STORE_FAST              20 (env)

 274            LOAD_FAST               20 (env)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST              34 ('counter')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L36)
       L34:     NOT_TAKEN
       L35:     POP_TOP
                BUILD_MAP                0
       L36:     STORE_FAST              21 (counter)

 275            LOAD_FAST               20 (env)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST              35 ('backend')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L39)
       L37:     NOT_TAKEN
       L38:     POP_TOP
                LOAD_CONST              36 ('store')
       L39:     STORE_FAST              22 (store_backend)

 276            LOAD_GLOBAL             15 (int + NULL)
                LOAD_FAST               21 (counter)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST              20 ('request_count')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L42)
       L40:     NOT_TAKEN
       L41:     POP_TOP
                LOAD_SMALL_INT           0
       L42:     CALL                     1
                STORE_FAST              23 (req_count)

 277            LOAD_GLOBAL             15 (int + NULL)
                LOAD_FAST               21 (counter)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST              21 ('blocked_count')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L45)
       L43:     NOT_TAKEN
       L44:     POP_TOP
                LOAD_SMALL_INT           0
       L45:     CALL                     1
                STORE_FAST              24 (blk_count)

 278            LOAD_GLOBAL              9 (_safe_envelope + NULL)

 279            LOAD_FAST               22 (store_backend)

 280            LOAD_FAST               23 (req_count)
                LOAD_FAST               10 (max_req)
                COMPARE_OP              42 (<=)

 281            LOAD_FAST               23 (req_count)

 282            LOAD_FAST               24 (blk_count)

 283            LOAD_FAST                2 (window_start)

 284            LOAD_FAST                3 (window_end)

 285            LOAD_CONST              37 (False)

 286            LOAD_GLOBAL             35 (list + NULL)
                LOAD_FAST               20 (env)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST              38 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L48)
       L46:     NOT_TAKEN
       L47:     POP_TOP
                BUILD_LIST               0
       L48:     CALL                     1
                LOAD_CONST              39 ('rate_limit_rpc_unavailable')
                BUILD_LIST               1
                BINARY_OP                0 (+)

 287            LOAD_FAST               20 (env)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST              25 ('error_code')
                CALL                     1

 278            LOAD_CONST              26 (('backend', 'allowed', 'request_count', 'blocked_count', 'window_start', 'window_end', 'rpc_available', 'warnings', 'error_code'))
                CALL_KW                  9
       L49:     RETURN_VALUE

  --   L50:     PUSH_EXC_INFO

 193            LOAD_GLOBAL             16 (TypeError)
                LOAD_GLOBAL             18 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        7 (to L52)
                NOT_TAKEN
                POP_TOP

 194            LOAD_SMALL_INT           0
                STORE_FAST              10 (max_req)
       L51:     POP_EXCEPT
                EXTENDED_ARG             2
                JUMP_BACKWARD_NO_INTERRUPT 742 (to L6)

 193   L52:     RERAISE                  0

  --   L53:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L54:     PUSH_EXC_INFO

 197            LOAD_GLOBAL             16 (TypeError)
                LOAD_GLOBAL             18 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        7 (to L56)
                NOT_TAKEN
                POP_TOP

 198            LOAD_SMALL_INT           0
                STORE_FAST              11 (req_delta)
       L55:     POP_EXCEPT
                EXTENDED_ARG             2
                JUMP_BACKWARD_NO_INTERRUPT 746 (to L8)

 197   L56:     RERAISE                  0

  --   L57:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L58:     PUSH_EXC_INFO

 201            LOAD_GLOBAL             16 (TypeError)
                LOAD_GLOBAL             18 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        7 (to L60)
                NOT_TAKEN
                POP_TOP

 202            LOAD_SMALL_INT           0
                STORE_FAST              12 (blk_delta)
       L59:     POP_EXCEPT
                EXTENDED_ARG             2
                JUMP_BACKWARD_NO_INTERRUPT 750 (to L10)

 201   L60:     RERAISE                  0

  --   L61:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L62:     PUSH_EXC_INFO

 251            LOAD_GLOBAL             44 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       56 (to L66)
                NOT_TAKEN
                STORE_FAST              18 (e)

 252   L63:     LOAD_GLOBAL             40 (logger)
                LOAD_ATTR               43 (warning + NULL|self)

 253            LOAD_CONST              28 ('increment_rate_limit_counter_atomic RPC error type=')

 254            LOAD_GLOBAL             47 (type + NULL)
                LOAD_FAST               18 (e)
                CALL                     1
                LOAD_ATTR               48 (__name__)
                FORMAT_SIMPLE
                LOAD_CONST              29 ('; falling back to store')

 253            BUILD_STRING             3

 252            CALL                     1
                POP_TOP
       L64:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              18 (e)
                DELETE_FAST             18 (e)
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 372 (to L32)

  --   L65:     LOAD_CONST               1 (None)
                STORE_FAST              18 (e)
                DELETE_FAST             18 (e)
                RERAISE                  1

 251   L66:     RERAISE                  0

  --   L67:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L68:     PUSH_EXC_INFO

 289            LOAD_GLOBAL             44 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       95 (to L73)
                NOT_TAKEN
                STORE_FAST              18 (e)

 290   L69:     LOAD_GLOBAL             40 (logger)
                LOAD_ATTR               43 (warning + NULL|self)

 291            LOAD_CONST              40 ('increment_rate_limit_counter_atomic fallback error type=')

 292            LOAD_GLOBAL             47 (type + NULL)
                LOAD_FAST               18 (e)
                CALL                     1
                LOAD_ATTR               48 (__name__)
                FORMAT_SIMPLE

 291            BUILD_STRING             2

 290            CALL                     1
                POP_TOP

 295            LOAD_GLOBAL              9 (_safe_envelope + NULL)

 296            LOAD_CONST               1 (None)

 297            LOAD_CONST               2 (True)

 298            LOAD_FAST                2 (window_start)

 299            LOAD_FAST                3 (window_end)

 300            LOAD_CONST              37 (False)

 301            LOAD_CONST              41 ('rate_limit_rpc_fallback_unexpected:')
                LOAD_GLOBAL             47 (type + NULL)
                LOAD_FAST               18 (e)
                CALL                     1
                LOAD_ATTR               48 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 302            LOAD_CONST              42 ('rate_limit_rpc_unexpected')

 295            LOAD_CONST              43 (('backend', 'allowed', 'window_start', 'window_end', 'rpc_available', 'warnings', 'error_code'))
                CALL_KW                  7
       L70:     SWAP                     2
       L71:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              18 (e)
                DELETE_FAST             18 (e)
                RETURN_VALUE

  --   L72:     LOAD_CONST               1 (None)
                STORE_FAST              18 (e)
                DELETE_FAST             18 (e)
                RERAISE                  1

 289   L73:     RERAISE                  0

  --   L74:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L5 to L6 -> L50 [0]
  L7 to L8 -> L54 [0]
  L9 to L10 -> L58 [0]
  L11 to L13 -> L62 [0]
  L14 to L17 -> L62 [0]
  L18 to L20 -> L62 [0]
  L21 to L23 -> L62 [0]
  L24 to L26 -> L62 [0]
  L27 to L30 -> L62 [0]
  L31 to L32 -> L62 [0]
  L33 to L34 -> L68 [0]
  L35 to L37 -> L68 [0]
  L38 to L40 -> L68 [0]
  L41 to L43 -> L68 [0]
  L44 to L46 -> L68 [0]
  L47 to L49 -> L68 [0]
  L50 to L51 -> L53 [1] lasti
  L52 to L53 -> L53 [1] lasti
  L54 to L55 -> L57 [1] lasti
  L56 to L57 -> L57 [1] lasti
  L58 to L59 -> L61 [1] lasti
  L60 to L61 -> L61 [1] lasti
  L62 to L63 -> L67 [1] lasti
  L63 to L64 -> L65 [1] lasti
  L65 to L67 -> L67 [1] lasti
  L68 to L69 -> L74 [1] lasti
  L69 to L70 -> L72 [1] lasti
  L70 to L71 -> L74 [1] lasti
  L72 to L74 -> L74 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "app/services/security/rate_limit_rpc.py", line 306>:
306           RESUME                   0
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

Disassembly of <code object atomic_rate_limit_report at 0x0000018C1794ED80, file "app/services/security/rate_limit_rpc.py", line 306>:
 306            RESUME                   0

 309            NOP

 310    L1:     LOAD_GLOBAL              1 (atomic_rate_limit_available + NULL)
                CALL                     0
                STORE_FAST               0 (available)

 317    L2:     LOAD_CONST               4 ('rpc_name')
                LOAD_GLOBAL             12 (_RPC_NAME)

 318            LOAD_CONST               5 ('rpc_available')
                LOAD_GLOBAL             15 (bool + NULL)
                LOAD_FAST_BORROW         0 (available)
                CALL                     1

 319            LOAD_CONST               6 ('backend')
                LOAD_FAST_BORROW         0 (available)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L3)
                NOT_TAKEN
                LOAD_CONST               7 ('rpc')
                JUMP_FORWARD             1 (to L4)
        L3:     LOAD_CONST               8 ('store')

 320    L4:     LOAD_CONST               9 ('warnings')
                LOAD_FAST_BORROW         0 (available)
                TO_BOOL
                POP_JUMP_IF_FALSE        4 (to L5)
                NOT_TAKEN
                BUILD_LIST               0

 316            BUILD_MAP                4
                RETURN_VALUE

 320    L5:     LOAD_CONST              10 ('rate_limit_rpc_unavailable')
                BUILD_LIST               1

 316            BUILD_MAP                4
                RETURN_VALUE

  --    L6:     PUSH_EXC_INFO

 311            LOAD_GLOBAL              2 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       56 (to L10)
                NOT_TAKEN
                STORE_FAST               1 (e)

 312    L7:     LOAD_GLOBAL              4 (logger)
                LOAD_ATTR                7 (warning + NULL|self)

 313            LOAD_CONST               1 ('atomic_rate_limit_report error type=')
                LOAD_GLOBAL              9 (type + NULL)
                LOAD_FAST                1 (e)
                CALL                     1
                LOAD_ATTR               10 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 312            CALL                     1
                POP_TOP

 315            LOAD_CONST               2 (False)
                STORE_FAST               0 (available)
        L8:     POP_EXCEPT
                LOAD_CONST               3 (None)
                STORE_FAST               1 (e)
                DELETE_FAST              1 (e)
                JUMP_BACKWARD_NO_INTERRUPT 106 (to L2)

  --    L9:     LOAD_CONST               3 (None)
                STORE_FAST               1 (e)
                DELETE_FAST              1 (e)
                RERAISE                  1

 311   L10:     RERAISE                  0

  --   L11:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L6 [0]
  L6 to L7 -> L11 [1] lasti
  L7 to L8 -> L9 [1] lasti
  L9 to L11 -> L11 [1] lasti
```
