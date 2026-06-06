# routes/operator_incidents

- **pyc:** `app\routes\__pycache__\operator_incidents.cpython-314.pyc`
- **expected source path (absent):** `app\routes/operator_incidents.py`
- **co_filename (from bytecode):** `app\routes\operator_incidents.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** routes

## Module docstring

```
PAS188 — Operator incidents + circuit-breaker routes
(bounded mutation, admin auth).

All routes require ``X-Admin-Key`` (PAS-SECURITY-04
``surface="admin"`` rate-limit applied). Mutations are
scoped to the closed incident-log + circuit-breaker
flows. No tenant mutation surface.

Routes (mounted under ``/ops``):

  Incidents (append-only on the row):
    GET  /ops/incidents
    GET  /ops/incidents/{incident_id}
    POST /ops/incidents/open
    POST /ops/incidents/{incident_id}/status
    POST /ops/incidents/{incident_id}/resolve

  Circuit breakers (operator-driven flag):
    GET  /ops/circuit-breakers
    GET  /ops/circuit-breakers/{brokerage_id}
    POST /ops/circuit-breakers/{brokerage_id}/trip
    POST /ops/circuit-breakers/{brokerage_id}/reset

Doctrine:

* Admin auth required + operator rate-limit (PAS-SECURITY-04).
* Read-only routes never raise — service layer collapses
  to ``status="skipped"`` on DB unavailable.
* Mutation routes are bounded: they edit only the rows
  defined in v37 / v38. The breaker routes do NOT mutate
  Twilio / Cal.com / the worker. The incident routes do
  NOT auto-trip a breaker or auto-open another incident.
* Every mutation emits a ``log_event_bg`` audit event.
* No PII / no raw payload / no secret in any envelope —
  enforced by the service-layer forbidden-token scanner.
```

## Imports

`APIRouter`, `Any`, `Body`, `Depends`, `Dict`, `HTTPException`, `Header`, `Optional`, `Path`, `Query`, `__future__`, `annotations`, `app.config`, `app.services.operator.cache_invalidation`, `app.services.operator.circuit_breaker`, `app.services.operator.incident_log`, `app.services.security.rate_limit`, `check_rate_limit`, `current_breaker_state`, `fastapi`, `get_incident`, `get_settings`, `invalidate_fleet_status_all`, `invalidate_fleet_status_for_brokerage`, `list_breakers`, `list_incidents`, `logging`, `open_incident`, `reset_breaker`, `resolve_incident`, `trip_breaker`, `typing`, `update_incident_status`

## Classes

_none_

## Functions / methods

`__annotate__`, `_extract_actor`, `_invalidate_cache_for`, `_safe_brokerage_path`, `_safe_incident_id_path`, `get_circuit_breaker`, `get_incident`, `list_circuit_breakers`, `list_incidents`, `open_incident`, `require_admin`, `reset_circuit_breaker`, `resolve_incident`, `trip_circuit_breaker`, `update_incident_status`

## Env-key candidates

`ADMIN`

## String constants (redacted where noted)

- '\nPAS188 — Operator incidents + circuit-breaker routes\n(bounded mutation, admin auth).\n\nAll routes require ``X-Admin-Key`` (PAS-SECURITY-04\n``surface="admin"`` rate-limit applied). Mutations are\nscoped to the closed incident-log + circuit-breaker\nflows. No tenant mutation surface.\n\nRoutes (mounted under ``/ops``):\n\n  Incidents (append-only on the row):\n    GET  /ops/incidents\n    GET  /ops/incidents/{incident_id}\n    POST /ops/incidents/open\n    POST /ops/incidents/{incident_id}/status\n    POST /ops/incidents/{incident_id}/resolve\n\n  Circuit breakers (operator-driven flag):\n    GET  /ops/circuit-breakers\n    GET  /ops/circuit-breakers/{brokerage_id}\n    POST /ops/circuit-breakers/{brokerage_id}/trip\n    POST /ops/circuit-breakers/{brokerage_id}/reset\n\nDoctrine:\n\n* Admin auth required + operator rate-limit (PAS-SECURITY-04).\n* Read-only routes never raise — service layer collapses\n  to ``status="skipped"`` on DB unavailable.\n* Mutation routes are bounded: they edit only the rows\n  defined in v37 / v38. The breaker routes do NOT mutate\n  Twilio / Cal.com / the worker. The incident routes do\n  NOT auto-trip a breaker or auto-open another incident.\n* Every mutation emits a ``log_event_bg`` audit event.\n* No PII / no raw payload / no secret in any envelope —\n  enforced by the service-layer forbidden-token scanner.\n'
- 'pas.ops.incidents'
- '/incidents'
- '/incidents/{incident_id}'
- '/incidents/open'
- '/incidents/{incident_id}/status'
- '/incidents/{incident_id}/resolve'
- '/circuit-breakers'
- '/circuit-breakers/{brokerage_id}'
- '/circuit-breakers/{brokerage_id}/trip'
- '/circuit-breakers/{brokerage_id}/reset'
- 'x_admin_key'
- 'str'
- 'return'
- 'bool'
- 'Invalid admin key'
- 'admin'
- 'ADMIN'
- 'allowed'
- 'Operator rate limit exceeded. Retry after the current window.'
- 'body'
- 'Optional[Dict[str, Any]]'
- 'Dict[str, Any]'
- 'actor_type'
- 'actor_id'
- 'actor_type and actor_id required'
- 'brokerage_id'
- 'invalid brokerage_id'
- 'incident_id'
- 'invalid incident_id'
- 'Optional[str]'
- 'reason'
- 'None'
- 'severity'
- 'status'
- 'limit'
- 'int'
- 'failed'
- 'error_code'
- 'incident_not_found'
- 'summary'
- 'incident_opened'
- 'resolution_code'
- 'resolution_text'
- 'incident_resolved'
- 'reason_code'
- 'rationale'
- 'circuit_breaker_tripped'
- 'circuit_breaker_reset'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS188 — Operator incidents + circuit-breaker routes\n(bounded mutation, admin auth).\n\nAll routes require ``X-Admin-Key`` (PAS-SECURITY-04\n``surface="admin"`` rate-limit applied). Mutations are\nscoped to the closed incident-log + circuit-breaker\nflows. No tenant mutation surface.\n\nRoutes (mounted under ``/ops``):\n\n  Incidents (append-only on the row):\n    GET  /ops/incidents\n    GET  /ops/incidents/{incident_id}\n    POST /ops/incidents/open\n    POST /ops/incidents/{incident_id}/status\n    POST /ops/incidents/{incident_id}/resolve\n\n  Circuit breakers (operator-driven flag):\n    GET  /ops/circuit-breakers\n    GET  /ops/circuit-breakers/{brokerage_id}\n    POST /ops/circuit-breakers/{brokerage_id}/trip\n    POST /ops/circuit-breakers/{brokerage_id}/reset\n\nDoctrine:\n\n* Admin auth required + operator rate-limit (PAS-SECURITY-04).\n* Read-only routes never raise — service layer collapses\n  to ``status="skipped"`` on DB unavailable.\n* Mutation routes are bounded: they edit only the rows\n  defined in v37 / v38. The breaker routes do NOT mutate\n  Twilio / Cal.com / the worker. The incident routes do\n  NOT auto-trip a breaker or auto-open another incident.\n* Every mutation emits a ``log_event_bg`` audit event.\n* No PII / no raw payload / no secret in any envelope —\n  enforced by the service-layer forbidden-token scanner.\n')
              STORE_NAME               0 (__doc__)

 39           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 41           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 42           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('Any', 'Dict', 'Optional'))
              IMPORT_NAME              4 (typing)
              IMPORT_FROM              5 (Any)
              STORE_NAME               5 (Any)
              IMPORT_FROM              6 (Dict)
              STORE_NAME               6 (Dict)
              IMPORT_FROM              7 (Optional)
              STORE_NAME               7 (Optional)
              POP_TOP

 44           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('APIRouter', 'Body', 'Depends', 'Header', 'HTTPException', 'Path', 'Query'))
              IMPORT_NAME              8 (fastapi)
              IMPORT_FROM              9 (APIRouter)
              STORE_NAME               9 (APIRouter)
              IMPORT_FROM             10 (Body)
              STORE_NAME              10 (Body)
              IMPORT_FROM             11 (Depends)
              STORE_NAME              11 (Depends)
              IMPORT_FROM             12 (Header)
              STORE_NAME              12 (Header)
              IMPORT_FROM             13 (HTTPException)
              STORE_NAME              13 (HTTPException)
              IMPORT_FROM             14 (Path)
              STORE_NAME              14 (Path)
              IMPORT_FROM             15 (Query)
              STORE_NAME              15 (Query)
              POP_TOP

 46           LOAD_SMALL_INT           0
              LOAD_CONST               5 (('get_settings',))
              IMPORT_NAME             16 (app.config)
              IMPORT_FROM             17 (get_settings)
              STORE_NAME              17 (get_settings)
              POP_TOP

 49           LOAD_NAME                9 (APIRouter)
              PUSH_NULL
              CALL                     0
              STORE_NAME              18 (router)

 50           LOAD_NAME                3 (logging)
              LOAD_ATTR               38 (getLogger)
              PUSH_NULL
              LOAD_CONST               6 ('pas.ops.incidents')
              CALL                     1
              STORE_NAME              20 (logger)

 57           LOAD_NAME               12 (Header)
              PUSH_NULL
              LOAD_CONST               7 (Ellipsis)
              CALL                     1
              BUILD_TUPLE              1
              LOAD_CONST               8 (<code object __annotate__ at 0x0000018C17FA3A50, file "app\routes\operator_incidents.py", line 57>)
              MAKE_FUNCTION
              LOAD_CONST               9 (<code object require_admin at 0x0000018C1801C410, file "app\routes\operator_incidents.py", line 57>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              21 (require_admin)

 84           LOAD_SMALL_INT         200
              STORE_NAME              22 (_BROKERAGE_ID_MAX_LEN)

 85           LOAD_SMALL_INT         200
              STORE_NAME              23 (_ACTOR_ID_MAX_LEN)

 88           LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA2A60, file "app\routes\operator_incidents.py", line 88>)
              MAKE_FUNCTION
              LOAD_CONST              11 (<code object _extract_actor at 0x0000018C17FEDC30, file "app\routes\operator_incidents.py", line 88>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              24 (_extract_actor)

103           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA3000, file "app\routes\operator_incidents.py", line 103>)
              MAKE_FUNCTION
              LOAD_CONST              13 (<code object _safe_brokerage_path at 0x0000018C18010B30, file "app\routes\operator_incidents.py", line 103>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              25 (_safe_brokerage_path)

110           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C17FA33C0, file "app\routes\operator_incidents.py", line 110>)
              MAKE_FUNCTION
              LOAD_CONST              15 (<code object _safe_incident_id_path at 0x0000018C180110B0, file "app\routes\operator_incidents.py", line 110>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              26 (_safe_incident_id_path)

117           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C18025030, file "app\routes\operator_incidents.py", line 117>)
              MAKE_FUNCTION
              LOAD_CONST              17 (<code object _invalidate_cache_for at 0x0000018C1802CAE0, file "app\routes\operator_incidents.py", line 117>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              27 (_invalidate_cache_for)

138           LOAD_NAME               18 (router)
              LOAD_ATTR               57 (get + NULL|self)
              LOAD_CONST              18 ('/incidents')
              CALL                     1

140           LOAD_NAME               15 (Query)
              PUSH_NULL
              LOAD_CONST               2 (None)
              LOAD_NAME               22 (_BROKERAGE_ID_MAX_LEN)
              LOAD_CONST              19 (('max_length',))
              CALL_KW                  2

141           LOAD_NAME               15 (Query)
              PUSH_NULL
              LOAD_CONST               2 (None)
              LOAD_SMALL_INT           8
              LOAD_CONST              19 (('max_length',))
              CALL_KW                  2

142           LOAD_NAME               15 (Query)
              PUSH_NULL
              LOAD_CONST               2 (None)
              LOAD_SMALL_INT          32
              LOAD_CONST              19 (('max_length',))
              CALL_KW                  2

143           LOAD_NAME               15 (Query)
              PUSH_NULL
              LOAD_SMALL_INT          50
              CALL                     1

144           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               21 (require_admin)
              CALL                     1

139           BUILD_TUPLE              5
              LOAD_CONST              20 (<code object __annotate__ at 0x0000018C18026130, file "app\routes\operator_incidents.py", line 139>)
              MAKE_FUNCTION
              LOAD_CONST              21 (<code object list_incidents at 0x0000018C18025730, file "app\routes\operator_incidents.py", line 138>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

138           CALL                     0

139           STORE_NAME              29 (list_incidents)

155           LOAD_NAME               18 (router)
              LOAD_ATTR               57 (get + NULL|self)
              LOAD_CONST              22 ('/incidents/{incident_id}')
              CALL                     1

157           LOAD_NAME               14 (Path)
              PUSH_NULL
              LOAD_CONST               7 (Ellipsis)
              LOAD_SMALL_INT          64
              LOAD_CONST              19 (('max_length',))
              CALL_KW                  2

158           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               21 (require_admin)
              CALL                     1

156           BUILD_TUPLE              2
              LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA35A0, file "app\routes\operator_incidents.py", line 156>)
              MAKE_FUNCTION
              LOAD_CONST              24 (<code object get_incident at 0x0000018C17FA92F0, file "app\routes\operator_incidents.py", line 155>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

155           CALL                     0

156           STORE_NAME              30 (get_incident)

168           LOAD_NAME               18 (router)
              LOAD_ATTR               63 (post + NULL|self)
              LOAD_CONST              25 ('/incidents/open')
              CALL                     1

170           LOAD_NAME               10 (Body)
              PUSH_NULL
              BUILD_MAP                0
              LOAD_CONST              26 (('default',))
              CALL_KW                  1

171           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               21 (require_admin)
              CALL                     1

169           BUILD_TUPLE              2
              LOAD_CONST              27 (<code object __annotate__ at 0x0000018C17FA2880, file "app\routes\operator_incidents.py", line 169>)
              MAKE_FUNCTION
              LOAD_CONST              28 (<code object open_incident at 0x0000018C17CD4970, file "app\routes\operator_incidents.py", line 168>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

168           CALL                     0

169           STORE_NAME              32 (open_incident)

195           LOAD_NAME               18 (router)
              LOAD_ATTR               63 (post + NULL|self)
              LOAD_CONST              29 ('/incidents/{incident_id}/status')
              CALL                     1

197           LOAD_NAME               14 (Path)
              PUSH_NULL
              LOAD_CONST               7 (Ellipsis)
              LOAD_SMALL_INT          64
              LOAD_CONST              19 (('max_length',))
              CALL_KW                  2

198           LOAD_NAME               10 (Body)
              PUSH_NULL
              BUILD_MAP                0
              LOAD_CONST              26 (('default',))
              CALL_KW                  1

199           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               21 (require_admin)
              CALL                     1

196           BUILD_TUPLE              3
              LOAD_CONST              30 (<code object __annotate__ at 0x0000018C18025E30, file "app\routes\operator_incidents.py", line 196>)
              MAKE_FUNCTION
              LOAD_CONST              31 (<code object update_incident_status at 0x0000018C179C3A50, file "app\routes\operator_incidents.py", line 195>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

195           CALL                     0

196           STORE_NAME              33 (update_incident_status)

217           LOAD_NAME               18 (router)
              LOAD_ATTR               63 (post + NULL|self)
              LOAD_CONST              32 ('/incidents/{incident_id}/resolve')
              CALL                     1

219           LOAD_NAME               14 (Path)
              PUSH_NULL
              LOAD_CONST               7 (Ellipsis)
              LOAD_SMALL_INT          64
              LOAD_CONST              19 (('max_length',))
              CALL_KW                  2

220           LOAD_NAME               10 (Body)
              PUSH_NULL
              BUILD_MAP                0
              LOAD_CONST              26 (('default',))
              CALL_KW                  1

221           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               21 (require_admin)
              CALL                     1

218           BUILD_TUPLE              3
              LOAD_CONST              33 (<code object __annotate__ at 0x0000018C18025D30, file "app\routes\operator_incidents.py", line 218>)
              MAKE_FUNCTION
              LOAD_CONST              34 (<code object resolve_incident at 0x0000018C17CC1F60, file "app\routes\operator_incidents.py", line 217>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

217           CALL                     0

218           STORE_NAME              34 (resolve_incident)

257           LOAD_NAME               18 (router)
              LOAD_ATTR               57 (get + NULL|self)
              LOAD_CONST              35 ('/circuit-breakers')
              CALL                     1

259           LOAD_NAME               15 (Query)
              PUSH_NULL
              LOAD_CONST               2 (None)
              LOAD_SMALL_INT          32
              LOAD_CONST              19 (('max_length',))
              CALL_KW                  2

260           LOAD_NAME               15 (Query)
              PUSH_NULL
              LOAD_SMALL_INT         100
              CALL                     1

261           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               21 (require_admin)
              CALL                     1

258           BUILD_TUPLE              3
              LOAD_CONST              36 (<code object __annotate__ at 0x0000018C18025130, file "app\routes\operator_incidents.py", line 258>)
              MAKE_FUNCTION
              LOAD_CONST              37 (<code object list_circuit_breakers at 0x0000018C18024930, file "app\routes\operator_incidents.py", line 257>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

257           CALL                     0

258           STORE_NAME              35 (list_circuit_breakers)

267           LOAD_NAME               18 (router)
              LOAD_ATTR               57 (get + NULL|self)
              LOAD_CONST              38 ('/circuit-breakers/{brokerage_id}')
              CALL                     1

269           LOAD_NAME               14 (Path)
              PUSH_NULL
              LOAD_CONST               7 (Ellipsis)
              LOAD_NAME               22 (_BROKERAGE_ID_MAX_LEN)
              LOAD_CONST              19 (('max_length',))
              CALL_KW                  2

270           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               21 (require_admin)
              CALL                     1

268           BUILD_TUPLE              2
              LOAD_CONST              39 (<code object __annotate__ at 0x0000018C17FA2B50, file "app\routes\operator_incidents.py", line 268>)
              MAKE_FUNCTION
              LOAD_CONST              40 (<code object get_circuit_breaker at 0x0000018C17FBFEE0, file "app\routes\operator_incidents.py", line 267>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

267           CALL                     0

268           STORE_NAME              36 (get_circuit_breaker)

277           LOAD_NAME               18 (router)
              LOAD_ATTR               63 (post + NULL|self)
              LOAD_CONST              41 ('/circuit-breakers/{brokerage_id}/trip')
              CALL                     1

279           LOAD_NAME               14 (Path)
              PUSH_NULL
              LOAD_CONST               7 (Ellipsis)
              LOAD_NAME               22 (_BROKERAGE_ID_MAX_LEN)
              LOAD_CONST              19 (('max_length',))
              CALL_KW                  2

280           LOAD_NAME               10 (Body)
              PUSH_NULL
              BUILD_MAP                0
              LOAD_CONST              26 (('default',))
              CALL_KW                  1

281           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               21 (require_admin)
              CALL                     1

278           BUILD_TUPLE              3
              LOAD_CONST              42 (<code object __annotate__ at 0x0000018C18026530, file "app\routes\operator_incidents.py", line 278>)
              MAKE_FUNCTION
              LOAD_CONST              43 (<code object trip_circuit_breaker at 0x0000018C17ECE6C0, file "app\routes\operator_incidents.py", line 277>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

277           CALL                     0

278           STORE_NAME              37 (trip_circuit_breaker)

304           LOAD_NAME               18 (router)
              LOAD_ATTR               63 (post + NULL|self)
              LOAD_CONST              44 ('/circuit-breakers/{brokerage_id}/reset')
              CALL                     1

306           LOAD_NAME               14 (Path)
              PUSH_NULL
              LOAD_CONST               7 (Ellipsis)
              LOAD_NAME               22 (_BROKERAGE_ID_MAX_LEN)
              LOAD_CONST              19 (('max_length',))
              CALL_KW                  2

307           LOAD_NAME               10 (Body)
              PUSH_NULL
              BUILD_MAP                0
              LOAD_CONST              26 (('default',))
              CALL_KW                  1

308           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               21 (require_admin)
              CALL                     1

305           BUILD_TUPLE              3
              LOAD_CONST              45 (<code object __annotate__ at 0x0000018C18026230, file "app\routes\operator_incidents.py", line 305>)
              MAKE_FUNCTION
              LOAD_CONST              46 (<code object reset_circuit_breaker at 0x0000018C17E94550, file "app\routes\operator_incidents.py", line 304>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

304           CALL                     0

305           STORE_NAME              38 (reset_circuit_breaker)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "app\routes\operator_incidents.py", line 57>:
 57           RESUME                   0
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

Disassembly of <code object require_admin at 0x0000018C1801C410, file "app\routes\operator_incidents.py", line 57>:
  57            RESUME                   0

  58            LOAD_GLOBAL              1 (get_settings + NULL)
                CALL                     0
                STORE_FAST               1 (settings)

  59            LOAD_FAST_BORROW         1 (settings)
                LOAD_ATTR                2 (ADMIN_API_KEY)
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (x_admin_key, settings)
                LOAD_ATTR                2 (ADMIN_API_KEY)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       14 (to L2)
                NOT_TAKEN

  60    L1:     LOAD_GLOBAL              5 (HTTPException + NULL)
                LOAD_CONST               0 (401)
                LOAD_CONST               1 ('Invalid admin key')
                LOAD_CONST               2 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

  61    L2:     NOP

  62    L3:     LOAD_SMALL_INT           0
                LOAD_CONST               3 (('check_rate_limit',))
                IMPORT_NAME              3 (app.services.security.rate_limit)
                IMPORT_FROM              4 (check_rate_limit)
                STORE_FAST               2 (check_rate_limit)
                POP_TOP

  63            LOAD_FAST_BORROW         2 (check_rate_limit)
                PUSH_NULL

  64            LOAD_CONST               4 ('admin')

  65            LOAD_CONST               5 ('ADMIN')

  66            LOAD_FAST_BORROW         0 (x_admin_key)

  63            LOAD_CONST               6 (('surface', 'actor_type', 'actor_token'))
                CALL_KW                  3
                STORE_FAST               3 (_rl_verdict)

  68            LOAD_FAST_BORROW         3 (_rl_verdict)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               7 ('allowed')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        14 (to L6)
        L4:     NOT_TAKEN

  69    L5:     LOAD_GLOBAL              5 (HTTPException + NULL)

  70            LOAD_CONST               8 (429)

  71            LOAD_CONST               9 ('Operator rate limit exceeded. Retry after the current window.')

  69            LOAD_CONST               2 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

  68    L6:     NOP

  77            LOAD_CONST              10 (True)
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

  73            LOAD_GLOBAL              4 (HTTPException)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                POP_TOP

  74            RAISE_VARARGS            0

  75    L8:     LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L12)
        L9:     NOT_TAKEN
       L10:     POP_TOP

  76   L11:     POP_EXCEPT

  77            LOAD_CONST              10 (True)
                RETURN_VALUE

  75   L12:     RERAISE                  0

  --   L13:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L7 [0]
  L5 to L6 -> L7 [0]
  L7 to L9 -> L13 [1] lasti
  L10 to L11 -> L13 [1] lasti
  L12 to L13 -> L13 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "app\routes\operator_incidents.py", line 88>:
 88           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('body')
              LOAD_CONST               2 ('Optional[Dict[str, Any]]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _extract_actor at 0x0000018C17FEDC30, file "app\routes\operator_incidents.py", line 88>:
 88           RESUME                   0

 89           LOAD_FAST                0 (body)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L1:     STORE_FAST               0 (body)

 90           LOAD_FAST_BORROW         0 (body)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               0 ('actor_type')
              CALL                     1
              STORE_FAST               1 (actor_type)

 91           LOAD_FAST_BORROW         0 (body)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               1 ('actor_id')
              CALL                     1
              STORE_FAST               2 (actor_id)

 92           LOAD_GLOBAL              3 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (actor_type)
              LOAD_GLOBAL              4 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       23 (to L2)
              NOT_TAKEN
              LOAD_GLOBAL              3 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (actor_id)
              LOAD_GLOBAL              4 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE        14 (to L3)
              NOT_TAKEN

 93   L2:     LOAD_GLOBAL              7 (HTTPException + NULL)

 94           LOAD_CONST               2 (400)

 95           LOAD_CONST               3 ('actor_type and actor_id required')

 93           LOAD_CONST               4 (('status_code', 'detail'))
              CALL_KW                  2
              RAISE_VARARGS            1

 98   L3:     LOAD_CONST               0 ('actor_type')
              LOAD_FAST_BORROW         1 (actor_type)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              LOAD_CONST               5 (slice(None, 32, None))
              BINARY_OP               26 ([])

 99           LOAD_CONST               1 ('actor_id')
              LOAD_FAST_BORROW         2 (actor_id)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              LOAD_CONST               6 (None)
              LOAD_GLOBAL             10 (_ACTOR_ID_MAX_LEN)
              BINARY_SLICE

 97           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3000, file "app\routes\operator_incidents.py", line 103>:
103           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               2 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _safe_brokerage_path at 0x0000018C18010B30, file "app\routes\operator_incidents.py", line 103>:
103           RESUME                   0

104           LOAD_FAST                0 (brokerage_id)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               0 ('')
      L1:     LOAD_ATTR                1 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

105           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_FALSE       21 (to L2)
              NOT_TAKEN
              LOAD_GLOBAL              3 (len + NULL)
              LOAD_FAST_BORROW         1 (s)
              CALL                     1
              LOAD_GLOBAL              4 (_BROKERAGE_ID_MAX_LEN)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       14 (to L3)
              NOT_TAKEN

106   L2:     LOAD_GLOBAL              7 (HTTPException + NULL)
              LOAD_CONST               1 (400)
              LOAD_CONST               2 ('invalid brokerage_id')
              LOAD_CONST               3 (('status_code', 'detail'))
              CALL_KW                  2
              RAISE_VARARGS            1

107   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "app\routes\operator_incidents.py", line 110>:
110           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('incident_id')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               2 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _safe_incident_id_path at 0x0000018C180110B0, file "app\routes\operator_incidents.py", line 110>:
110           RESUME                   0

111           LOAD_FAST                0 (incident_id)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               0 ('')
      L1:     LOAD_ATTR                1 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

112           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_FALSE       17 (to L2)
              NOT_TAKEN
              LOAD_GLOBAL              3 (len + NULL)
              LOAD_FAST_BORROW         1 (s)
              CALL                     1
              LOAD_SMALL_INT          64
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       14 (to L3)
              NOT_TAKEN

113   L2:     LOAD_GLOBAL              5 (HTTPException + NULL)
              LOAD_CONST               1 (400)
              LOAD_CONST               2 ('invalid incident_id')
              LOAD_CONST               3 (('status_code', 'detail'))
              CALL_KW                  2
              RAISE_VARARGS            1

114   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025030, file "app\routes\operator_incidents.py", line 117>:
117           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')
              LOAD_CONST               2 ('Optional[str]')
              LOAD_CONST               3 ('reason')
              LOAD_CONST               4 ('str')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('None')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _invalidate_cache_for at 0x0000018C1802CAE0, file "app\routes\operator_incidents.py", line 117>:
 117           RESUME                   0

 121           LOAD_FAST_BORROW         0 (brokerage_id)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN

 122           LOAD_CONST               0 (None)
               RETURN_VALUE

 123   L1:     NOP

 124   L2:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('invalidate_fleet_status_for_brokerage',))
               IMPORT_NAME              0 (app.services.operator.cache_invalidation)
               IMPORT_FROM              1 (invalidate_fleet_status_for_brokerage)
               STORE_FAST               2 (invalidate_fleet_status_for_brokerage)
               POP_TOP

 127           LOAD_FAST_BORROW         2 (invalidate_fleet_status_for_brokerage)
               PUSH_NULL

 128           LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (brokerage_id, reason)

 127           LOAD_CONST               2 (('reason',))
               CALL_KW                  2
               POP_TOP
       L3:     LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     PUSH_EXC_INFO

 130           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L6)
               NOT_TAKEN
               POP_TOP

 131   L5:     POP_EXCEPT
               LOAD_CONST               0 (None)
               RETURN_VALUE

 130   L6:     RERAISE                  0

  --   L7:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L4 [0]
  L4 to L5 -> L7 [1] lasti
  L6 to L7 -> L7 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026130, file "app\routes\operator_incidents.py", line 139>:
139           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

140           LOAD_CONST               2 ('Optional[str]')

139           LOAD_CONST               3 ('severity')

141           LOAD_CONST               2 ('Optional[str]')

139           LOAD_CONST               4 ('status')

142           LOAD_CONST               2 ('Optional[str]')

139           LOAD_CONST               5 ('limit')

143           LOAD_CONST               6 ('int')

139           LOAD_CONST               7 ('return')

145           LOAD_CONST               8 ('Dict[str, Any]')

139           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object list_incidents at 0x0000018C18025730, file "app\routes\operator_incidents.py", line 138>:
 138           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0

 146           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('list_incidents',))
               IMPORT_NAME              0 (app.services.operator.incident_log)
               IMPORT_FROM              1 (list_incidents)
               STORE_FAST               5 (svc_list)
               POP_TOP

 147           LOAD_FAST_BORROW         5 (svc_list)
               PUSH_NULL

 148           LOAD_FAST_BORROW         0 (brokerage_id)

 149           LOAD_FAST_BORROW         1 (severity)

 150           LOAD_FAST_BORROW         2 (status)

 151           LOAD_FAST_BORROW         3 (limit)

 147           LOAD_CONST               2 (('brokerage_id', 'severity', 'status', 'limit'))
               CALL_KW                  4
               RETURN_VALUE

  --   L2:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L2 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "app\routes\operator_incidents.py", line 156>:
156           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('incident_id')

157           LOAD_CONST               2 ('str')

156           LOAD_CONST               3 ('return')

159           LOAD_CONST               4 ('Dict[str, Any]')

156           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object get_incident at 0x0000018C17FA92F0, file "app\routes\operator_incidents.py", line 155>:
 155           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0

 160           LOAD_GLOBAL              1 (_safe_incident_id_path + NULL)
               LOAD_FAST_BORROW         0 (incident_id)
               CALL                     1
               STORE_FAST               2 (iid)

 161           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('get_incident',))
               IMPORT_NAME              1 (app.services.operator.incident_log)
               IMPORT_FROM              2 (get_incident)
               STORE_FAST               3 (svc_get)
               POP_TOP

 162           LOAD_FAST_BORROW         3 (svc_get)
               PUSH_NULL
               LOAD_FAST_BORROW         2 (iid)
               LOAD_CONST               2 (('incident_id',))
               CALL_KW                  1
               STORE_FAST               4 (env)

 163           LOAD_FAST_BORROW         4 (env)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_CONST               3 ('status')
               CALL                     1
               LOAD_CONST               4 ('failed')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       36 (to L2)
               NOT_TAKEN
               LOAD_FAST_BORROW         4 (env)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_CONST               5 ('error_code')
               CALL                     1
               LOAD_CONST               6 ('incident_not_found')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       14 (to L2)
               NOT_TAKEN

 164           LOAD_GLOBAL              9 (HTTPException + NULL)
               LOAD_CONST               7 (404)
               LOAD_CONST               6 ('incident_not_found')
               LOAD_CONST               8 (('status_code', 'detail'))
               CALL_KW                  2
               RAISE_VARARGS            1

 165   L2:     LOAD_FAST_BORROW         4 (env)
               RETURN_VALUE

  --   L3:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L3 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "app\routes\operator_incidents.py", line 169>:
169           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('body')

170           LOAD_CONST               2 ('Dict[str, Any]')

169           LOAD_CONST               3 ('return')

172           LOAD_CONST               2 ('Dict[str, Any]')

169           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object open_incident at 0x0000018C17CD4970, file "app\routes\operator_incidents.py", line 168>:
 168           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0

 173           LOAD_GLOBAL              1 (_extract_actor + NULL)
               LOAD_FAST_BORROW         0 (body)
               CALL                     1
               STORE_FAST               2 (actor)

 174           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('open_incident',))
               IMPORT_NAME              1 (app.services.operator.incident_log)
               IMPORT_FROM              2 (open_incident)
               STORE_FAST               3 (svc_open)
               POP_TOP

 175           LOAD_FAST_BORROW         3 (svc_open)
               PUSH_NULL

 176           LOAD_FAST_BORROW         0 (body)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_CONST               2 ('brokerage_id')
               CALL                     1

 177           LOAD_FAST_BORROW         0 (body)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_CONST               3 ('severity')
               CALL                     1

 178           LOAD_FAST_BORROW         0 (body)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_CONST               4 ('summary')
               CALL                     1

 179           LOAD_FAST_BORROW         2 (actor)
               LOAD_CONST               5 ('actor_type')
               BINARY_OP               26 ([])

 180           LOAD_FAST_BORROW         2 (actor)
               LOAD_CONST               6 ('actor_id')
               BINARY_OP               26 ([])

 175           LOAD_CONST               7 (('brokerage_id', 'severity', 'summary', 'actor_type', 'actor_id'))
               CALL_KW                  5
               STORE_FAST               4 (env)

 182           LOAD_FAST_BORROW         4 (env)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_CONST               8 ('status')
               CALL                     1
               LOAD_CONST               9 ('failed')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       38 (to L2)
               NOT_TAKEN

 183           LOAD_FAST_BORROW         4 (env)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_CONST              10 ('error_code')
               CALL                     1
               STORE_FAST               5 (code)

 184           LOAD_FAST_BORROW         5 (code)
               LOAD_CONST              16 (('invalid_severity', 'invalid_summary', 'invalid_actor_type'))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       14 (to L2)
               NOT_TAKEN

 186           LOAD_GLOBAL              9 (HTTPException + NULL)
               LOAD_CONST              11 (400)
               LOAD_FAST_BORROW         5 (code)
               LOAD_CONST              12 (('status_code', 'detail'))
               CALL_KW                  2
               RAISE_VARARGS            1

 189   L2:     LOAD_FAST_BORROW         4 (env)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_CONST               8 ('status')
               CALL                     1
               LOAD_CONST              13 ('ok')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       54 (to L5)
               NOT_TAKEN

 190           LOAD_GLOBAL             11 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (body)
               LOAD_GLOBAL             12 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L3)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (body)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_CONST               2 ('brokerage_id')
               CALL                     1
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST              14 (None)
       L4:     STORE_FAST               6 (bid_from_body)

 191           LOAD_GLOBAL             15 (_invalidate_cache_for + NULL)
               LOAD_FAST_BORROW         6 (bid_from_body)
               LOAD_CONST              15 ('incident_opened')
               CALL                     2
               POP_TOP

 192   L5:     LOAD_FAST_BORROW         4 (env)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L6 -> L6 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025E30, file "app\routes\operator_incidents.py", line 196>:
196           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('incident_id')

197           LOAD_CONST               2 ('str')

196           LOAD_CONST               3 ('body')

198           LOAD_CONST               4 ('Dict[str, Any]')

196           LOAD_CONST               5 ('return')

200           LOAD_CONST               4 ('Dict[str, Any]')

196           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object update_incident_status at 0x0000018C179C3A50, file "app\routes\operator_incidents.py", line 195>:
 195           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0

 201           LOAD_GLOBAL              1 (_safe_incident_id_path + NULL)
               LOAD_FAST_BORROW         0 (incident_id)
               CALL                     1
               STORE_FAST               3 (iid)

 202           LOAD_GLOBAL              3 (_extract_actor + NULL)
               LOAD_FAST_BORROW         1 (body)
               CALL                     1
               STORE_FAST               4 (actor)

 203           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('update_incident_status',))
               IMPORT_NAME              2 (app.services.operator.incident_log)
               IMPORT_FROM              3 (update_incident_status)
               STORE_FAST               5 (svc_update)
               POP_TOP

 204           LOAD_FAST_BORROW         5 (svc_update)
               PUSH_NULL

 205           LOAD_FAST_BORROW         3 (iid)

 206           LOAD_FAST_BORROW         1 (body)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST               2 ('status')
               CALL                     1

 207           LOAD_FAST_BORROW         4 (actor)
               LOAD_CONST               3 ('actor_type')
               BINARY_OP               26 ([])

 208           LOAD_FAST_BORROW         4 (actor)
               LOAD_CONST               4 ('actor_id')
               BINARY_OP               26 ([])

 204           LOAD_CONST               5 (('incident_id', 'status', 'actor_type', 'actor_id'))
               CALL_KW                  4
               STORE_FAST               6 (env)

 210           LOAD_FAST_BORROW         6 (env)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST               2 ('status')
               CALL                     1
               LOAD_CONST               6 ('failed')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       38 (to L2)
               NOT_TAKEN

 211           LOAD_FAST_BORROW         6 (env)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST               7 ('error_code')
               CALL                     1
               STORE_FAST               7 (code)

 212           LOAD_FAST_BORROW         7 (code)
               LOAD_CONST              10 (('invalid_arguments', 'invalid_status'))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       14 (to L2)
               NOT_TAKEN

 213           LOAD_GLOBAL             11 (HTTPException + NULL)
               LOAD_CONST               8 (400)
               LOAD_FAST_BORROW         7 (code)
               LOAD_CONST               9 (('status_code', 'detail'))
               CALL_KW                  2
               RAISE_VARARGS            1

 214   L2:     LOAD_FAST_BORROW         6 (env)
               RETURN_VALUE

  --   L3:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L3 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025D30, file "app\routes\operator_incidents.py", line 218>:
218           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('incident_id')

219           LOAD_CONST               2 ('str')

218           LOAD_CONST               3 ('body')

220           LOAD_CONST               4 ('Dict[str, Any]')

218           LOAD_CONST               5 ('return')

222           LOAD_CONST               4 ('Dict[str, Any]')

218           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object resolve_incident at 0x0000018C17CC1F60, file "app\routes\operator_incidents.py", line 217>:
 217            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 223            LOAD_GLOBAL              1 (_safe_incident_id_path + NULL)
                LOAD_FAST_BORROW         0 (incident_id)
                CALL                     1
                STORE_FAST               3 (iid)

 224            LOAD_GLOBAL              3 (_extract_actor + NULL)
                LOAD_FAST_BORROW         1 (body)
                CALL                     1
                STORE_FAST               4 (actor)

 225            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('resolve_incident',))
                IMPORT_NAME              2 (app.services.operator.incident_log)
                IMPORT_FROM              3 (resolve_incident)
                STORE_FAST               5 (svc_resolve)
                POP_TOP

 226            LOAD_FAST_BORROW         5 (svc_resolve)
                PUSH_NULL

 227            LOAD_FAST_BORROW         3 (iid)

 228            LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               2 ('resolution_code')
                CALL                     1

 229            LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               3 ('resolution_text')
                CALL                     1

 230            LOAD_FAST_BORROW         4 (actor)
                LOAD_CONST               4 ('actor_type')
                BINARY_OP               26 ([])

 231            LOAD_FAST_BORROW         4 (actor)
                LOAD_CONST               5 ('actor_id')
                BINARY_OP               26 ([])

 226            LOAD_CONST               6 (('incident_id', 'resolution_code', 'resolution_text', 'actor_type', 'actor_id'))
                CALL_KW                  5
                STORE_FAST               6 (env)

 233            LOAD_FAST_BORROW         6 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               7 ('status')
                CALL                     1
                LOAD_CONST               8 ('failed')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       38 (to L2)
                NOT_TAKEN

 234            LOAD_FAST_BORROW         6 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               9 ('error_code')
                CALL                     1
                STORE_FAST               7 (code)

 235            LOAD_FAST_BORROW         7 (code)
                LOAD_CONST              16 (('invalid_arguments',))
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       14 (to L2)
                NOT_TAKEN

 236            LOAD_GLOBAL             11 (HTTPException + NULL)
                LOAD_CONST              10 (400)
                LOAD_FAST_BORROW         7 (code)
                LOAD_CONST              11 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

 242    L2:     LOAD_FAST_BORROW         6 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               7 ('status')
                CALL                     1
                LOAD_CONST              12 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       19 (to L6)
                NOT_TAKEN

 243    L3:     NOP

 244    L4:     LOAD_SMALL_INT           0
                LOAD_CONST              13 (('invalidate_fleet_status_all',))
                IMPORT_NAME              6 (app.services.operator.cache_invalidation)
                IMPORT_FROM              7 (invalidate_fleet_status_all)
                STORE_FAST               8 (invalidate_fleet_status_all)
                POP_TOP

 247            LOAD_FAST_BORROW         8 (invalidate_fleet_status_all)
                PUSH_NULL
                LOAD_CONST              14 ('incident_resolved')
                LOAD_CONST              15 (('reason',))
                CALL_KW                  1
                POP_TOP

 250    L5:     LOAD_FAST_BORROW         6 (env)
                RETURN_VALUE
        L6:     LOAD_FAST_BORROW         6 (env)
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

 248            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L9)
                NOT_TAKEN
                POP_TOP

 249    L8:     POP_EXCEPT

 250            LOAD_FAST                6 (env)
                RETURN_VALUE

 248    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L11:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L3 -> L11 [0] lasti
  L4 to L5 -> L7 [0]
  L5 to L7 -> L11 [0] lasti
  L7 to L8 -> L10 [1] lasti
  L8 to L9 -> L11 [0] lasti
  L9 to L10 -> L10 [1] lasti
  L10 to L11 -> L11 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025130, file "app\routes\operator_incidents.py", line 258>:
258           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')

259           LOAD_CONST               2 ('Optional[str]')

258           LOAD_CONST               3 ('limit')

260           LOAD_CONST               4 ('int')

258           LOAD_CONST               5 ('return')

262           LOAD_CONST               6 ('Dict[str, Any]')

258           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object list_circuit_breakers at 0x0000018C18024930, file "app\routes\operator_incidents.py", line 257>:
 257           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0

 263           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('list_breakers',))
               IMPORT_NAME              0 (app.services.operator.circuit_breaker)
               IMPORT_FROM              1 (list_breakers)
               STORE_FAST               3 (list_breakers)
               POP_TOP

 264           LOAD_FAST_BORROW         3 (list_breakers)
               PUSH_NULL
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (status, limit)
               LOAD_CONST               2 (('status', 'limit'))
               CALL_KW                  2
               RETURN_VALUE

  --   L2:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L2 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "app\routes\operator_incidents.py", line 268>:
268           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

269           LOAD_CONST               2 ('str')

268           LOAD_CONST               3 ('return')

271           LOAD_CONST               4 ('Dict[str, Any]')

268           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object get_circuit_breaker at 0x0000018C17FBFEE0, file "app\routes\operator_incidents.py", line 267>:
 267           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0

 272           LOAD_GLOBAL              1 (_safe_brokerage_path + NULL)
               LOAD_FAST_BORROW         0 (brokerage_id)
               CALL                     1
               STORE_FAST               2 (bid)

 273           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('current_breaker_state',))
               IMPORT_NAME              1 (app.services.operator.circuit_breaker)
               IMPORT_FROM              2 (current_breaker_state)
               STORE_FAST               3 (current_breaker_state)
               POP_TOP

 274           LOAD_FAST_BORROW         3 (current_breaker_state)
               PUSH_NULL
               LOAD_FAST_BORROW         2 (bid)
               LOAD_CONST               2 (('brokerage_id',))
               CALL_KW                  1
               RETURN_VALUE

  --   L2:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L2 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026530, file "app\routes\operator_incidents.py", line 278>:
278           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

279           LOAD_CONST               2 ('str')

278           LOAD_CONST               3 ('body')

280           LOAD_CONST               4 ('Dict[str, Any]')

278           LOAD_CONST               5 ('return')

282           LOAD_CONST               4 ('Dict[str, Any]')

278           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object trip_circuit_breaker at 0x0000018C17ECE6C0, file "app\routes\operator_incidents.py", line 277>:
 277           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0

 283           LOAD_GLOBAL              1 (_safe_brokerage_path + NULL)
               LOAD_FAST_BORROW         0 (brokerage_id)
               CALL                     1
               STORE_FAST               3 (bid)

 284           LOAD_GLOBAL              3 (_extract_actor + NULL)
               LOAD_FAST_BORROW         1 (body)
               CALL                     1
               STORE_FAST               4 (actor)

 285           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('trip_breaker',))
               IMPORT_NAME              2 (app.services.operator.circuit_breaker)
               IMPORT_FROM              3 (trip_breaker)
               STORE_FAST               5 (trip_breaker)
               POP_TOP

 286           LOAD_FAST_BORROW         5 (trip_breaker)
               PUSH_NULL

 287           LOAD_FAST_BORROW         3 (bid)

 288           LOAD_FAST_BORROW         1 (body)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST               2 ('reason_code')
               CALL                     1

 289           LOAD_FAST_BORROW         4 (actor)
               LOAD_CONST               3 ('actor_type')
               BINARY_OP               26 ([])

 290           LOAD_FAST_BORROW         4 (actor)
               LOAD_CONST               4 ('actor_id')
               BINARY_OP               26 ([])

 291           LOAD_FAST_BORROW         1 (body)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST               5 ('rationale')
               CALL                     1

 286           LOAD_CONST               6 (('brokerage_id', 'reason_code', 'actor_type', 'actor_id', 'rationale'))
               CALL_KW                  5
               STORE_FAST               6 (env)

 293           LOAD_FAST_BORROW         6 (env)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST               7 ('status')
               CALL                     1
               LOAD_CONST               8 ('failed')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       38 (to L2)
               NOT_TAKEN

 294           LOAD_FAST_BORROW         6 (env)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST               9 ('error_code')
               CALL                     1
               STORE_FAST               7 (code)

 295           LOAD_FAST_BORROW         7 (code)
               LOAD_CONST              14 (('invalid_brokerage_id', 'invalid_reason_code', 'invalid_actor'))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       14 (to L2)
               NOT_TAKEN

 297           LOAD_GLOBAL             11 (HTTPException + NULL)
               LOAD_CONST              10 (400)
               LOAD_FAST_BORROW         7 (code)
               LOAD_CONST              11 (('status_code', 'detail'))
               CALL_KW                  2
               RAISE_VARARGS            1

 299   L2:     LOAD_FAST_BORROW         6 (env)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST               7 ('status')
               CALL                     1
               LOAD_CONST              12 ('ok')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       13 (to L3)
               NOT_TAKEN

 300           LOAD_GLOBAL             13 (_invalidate_cache_for + NULL)
               LOAD_FAST_BORROW         3 (bid)
               LOAD_CONST              13 ('circuit_breaker_tripped')
               CALL                     2
               POP_TOP

 301   L3:     LOAD_FAST_BORROW         6 (env)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026230, file "app\routes\operator_incidents.py", line 305>:
305           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

306           LOAD_CONST               2 ('str')

305           LOAD_CONST               3 ('body')

307           LOAD_CONST               4 ('Dict[str, Any]')

305           LOAD_CONST               5 ('return')

309           LOAD_CONST               4 ('Dict[str, Any]')

305           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object reset_circuit_breaker at 0x0000018C17E94550, file "app\routes\operator_incidents.py", line 304>:
 304           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0

 310           LOAD_GLOBAL              1 (_safe_brokerage_path + NULL)
               LOAD_FAST_BORROW         0 (brokerage_id)
               CALL                     1
               STORE_FAST               3 (bid)

 311           LOAD_GLOBAL              3 (_extract_actor + NULL)
               LOAD_FAST_BORROW         1 (body)
               CALL                     1
               STORE_FAST               4 (actor)

 312           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('reset_breaker',))
               IMPORT_NAME              2 (app.services.operator.circuit_breaker)
               IMPORT_FROM              3 (reset_breaker)
               STORE_FAST               5 (reset_breaker)
               POP_TOP

 313           LOAD_FAST_BORROW         5 (reset_breaker)
               PUSH_NULL

 314           LOAD_FAST_BORROW         3 (bid)

 315           LOAD_FAST_BORROW         4 (actor)
               LOAD_CONST               2 ('actor_type')
               BINARY_OP               26 ([])

 316           LOAD_FAST_BORROW         4 (actor)
               LOAD_CONST               3 ('actor_id')
               BINARY_OP               26 ([])

 317           LOAD_FAST_BORROW         1 (body)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST               4 ('rationale')
               CALL                     1

 313           LOAD_CONST               5 (('brokerage_id', 'actor_type', 'actor_id', 'rationale'))
               CALL_KW                  4
               STORE_FAST               6 (env)

 319           LOAD_FAST_BORROW         6 (env)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST               6 ('status')
               CALL                     1
               LOAD_CONST               7 ('failed')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       38 (to L2)
               NOT_TAKEN

 320           LOAD_FAST_BORROW         6 (env)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST               8 ('error_code')
               CALL                     1
               STORE_FAST               7 (code)

 321           LOAD_FAST_BORROW         7 (code)
               LOAD_CONST              13 (('invalid_brokerage_id', 'invalid_actor'))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       14 (to L2)
               NOT_TAKEN

 322           LOAD_GLOBAL             11 (HTTPException + NULL)
               LOAD_CONST               9 (400)
               LOAD_FAST_BORROW         7 (code)
               LOAD_CONST              10 (('status_code', 'detail'))
               CALL_KW                  2
               RAISE_VARARGS            1

 324   L2:     LOAD_FAST_BORROW         6 (env)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST               6 ('status')
               CALL                     1
               LOAD_CONST              11 ('ok')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       13 (to L3)
               NOT_TAKEN

 325           LOAD_GLOBAL             13 (_invalidate_cache_for + NULL)
               LOAD_FAST_BORROW         3 (bid)
               LOAD_CONST              12 ('circuit_breaker_reset')
               CALL                     2
               POP_TOP

 326   L3:     LOAD_FAST_BORROW         6 (env)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti
```
