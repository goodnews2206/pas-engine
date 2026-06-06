# routes/tenant_incidents

- **pyc:** `app\routes\__pycache__\tenant_incidents.cpython-314.pyc`
- **expected source path (absent):** `app\routes/tenant_incidents.py`
- **co_filename (from bytecode):** `app\routes\tenant_incidents.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** routes

## Module docstring

```
PAS189 — Tenant-facing incident routes (read-only).

X-API-Key authenticated. Admin X-Admin-Key is REJECTED
here — operator-side incidents are out of scope for the
tenant surface.

Routes (mounted under ``/tenant``):

  GET  /tenant/incidents
  GET  /tenant/incidents/{incident_id}

Doctrine:

* **Tenant X-API-Key only.** Admin key is rejected.
  brokerage_id resolves from the authenticated record;
  the tenant cannot supply a brokerage_id parameter.
* **Read-only.** No mutation surface.
* **Safe projection.** Returns only the explicit
  PAS189 tenant allow-list (incident_id, severity,
  status, opened_at, resolved_at, resolution_code).
* **No cross-brokerage leakage.** Projection filters
  the DB query by brokerage_id from the auth record,
  and a defensive recheck drops any row whose
  brokerage_id does not match.
* **No PII.** Forbidden-token scanner is the last
  defence.
```

## Imports

`APIRouter`, `Any`, `Depends`, `Dict`, `HTTPException`, `Header`, `Optional`, `Path`, `Query`, `__future__`, `annotations`, `app.db.brokerage_store`, `app.db.event_logger`, `app.services.tenant.tenant_incident_projection`, `fastapi`, `get_brokerage_by_api_key`, `get_tenant_incident_for_brokerage`, `list_tenant_incidents_for_brokerage`, `log_event_bg`, `logging`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_emit_tenant_event`, `get_tenant_incident`, `list_tenant_incidents`, `require_brokerage`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS189 — Tenant-facing incident routes (read-only).\n\nX-API-Key authenticated. Admin X-Admin-Key is REJECTED\nhere — operator-side incidents are out of scope for the\ntenant surface.\n\nRoutes (mounted under ``/tenant``):\n\n  GET  /tenant/incidents\n  GET  /tenant/incidents/{incident_id}\n\nDoctrine:\n\n* **Tenant X-API-Key only.** Admin key is rejected.\n  brokerage_id resolves from the authenticated record;\n  the tenant cannot supply a brokerage_id parameter.\n* **Read-only.** No mutation surface.\n* **Safe projection.** Returns only the explicit\n  PAS189 tenant allow-list (incident_id, severity,\n  status, opened_at, resolved_at, resolution_code).\n* **No cross-brokerage leakage.** Projection filters\n  the DB query by brokerage_id from the auth record,\n  and a defensive recheck drops any row whose\n  brokerage_id does not match.\n* **No PII.** Forbidden-token scanner is the last\n  defence.\n'
- 'pas.tenant.incidents'
- 'X-API-Key'
- 'X-Admin-Key'
- '/incidents'
- '/incidents/{incident_id}'
- 'x_api_key'
- 'Optional[str]'
- 'x_admin_key'
- 'return'
- 'Dict[str, Any]'
- 'Admin key not accepted on tenant surface'
- 'Missing X-API-Key'
- 'demo'
- 'Invalid API key'
- 'event_type'
- 'str'
- 'payload'
- 'None'
- 'severity'
- 'status'
- 'limit'
- 'int'
- 'offset'
- 'date_from'
- 'date_to'
- 'brokerage'
- 'filter_count'
- 'tenant.incident.filtered_viewed'
- 'brokerage_id'
- 'route'
- 'list_tenant_incidents'
- 'action_required'
- 'none'
- 'error_code'
- 'tenant.incident.viewed'
- 'incident_id'
- 'invalid_incident_id'
- 'get_tenant_incident'
- 'failed'
- 'incident_not_found'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS189 — Tenant-facing incident routes (read-only).\n\nX-API-Key authenticated. Admin X-Admin-Key is REJECTED\nhere — operator-side incidents are out of scope for the\ntenant surface.\n\nRoutes (mounted under ``/tenant``):\n\n  GET  /tenant/incidents\n  GET  /tenant/incidents/{incident_id}\n\nDoctrine:\n\n* **Tenant X-API-Key only.** Admin key is rejected.\n  brokerage_id resolves from the authenticated record;\n  the tenant cannot supply a brokerage_id parameter.\n* **Read-only.** No mutation surface.\n* **Safe projection.** Returns only the explicit\n  PAS189 tenant allow-list (incident_id, severity,\n  status, opened_at, resolved_at, resolution_code).\n* **No cross-brokerage leakage.** Projection filters\n  the DB query by brokerage_id from the auth record,\n  and a defensive recheck drops any row whose\n  brokerage_id does not match.\n* **No PII.** Forbidden-token scanner is the last\n  defence.\n')
              STORE_NAME               0 (__doc__)

 30           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 32           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 33           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('Any', 'Dict', 'Optional'))
              IMPORT_NAME              4 (typing)
              IMPORT_FROM              5 (Any)
              STORE_NAME               5 (Any)
              IMPORT_FROM              6 (Dict)
              STORE_NAME               6 (Dict)
              IMPORT_FROM              7 (Optional)
              STORE_NAME               7 (Optional)
              POP_TOP

 35           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('APIRouter', 'Depends', 'Header', 'HTTPException', 'Path', 'Query'))
              IMPORT_NAME              8 (fastapi)
              IMPORT_FROM              9 (APIRouter)
              STORE_NAME               9 (APIRouter)
              IMPORT_FROM             10 (Depends)
              STORE_NAME              10 (Depends)
              IMPORT_FROM             11 (Header)
              STORE_NAME              11 (Header)
              IMPORT_FROM             12 (HTTPException)
              STORE_NAME              12 (HTTPException)
              IMPORT_FROM             13 (Path)
              STORE_NAME              13 (Path)
              IMPORT_FROM             14 (Query)
              STORE_NAME              14 (Query)
              POP_TOP

 37           LOAD_SMALL_INT           0
              LOAD_CONST               5 (('get_brokerage_by_api_key',))
              IMPORT_NAME             15 (app.db.brokerage_store)
              IMPORT_FROM             16 (get_brokerage_by_api_key)
              STORE_NAME              16 (get_brokerage_by_api_key)
              POP_TOP

 40           LOAD_NAME                9 (APIRouter)
              PUSH_NULL
              CALL                     0
              STORE_NAME              17 (router)

 41           LOAD_NAME                3 (logging)
              LOAD_ATTR               36 (getLogger)
              PUSH_NULL
              LOAD_CONST               6 ('pas.tenant.incidents')
              CALL                     1
              STORE_NAME              19 (logger)

 49           LOAD_NAME               11 (Header)
              PUSH_NULL
              LOAD_CONST               2 (None)
              LOAD_CONST               7 ('X-API-Key')
              LOAD_CONST               8 (('alias',))
              CALL_KW                  2

 50           LOAD_NAME               11 (Header)
              PUSH_NULL
              LOAD_CONST               2 (None)
              LOAD_CONST               9 ('X-Admin-Key')
              LOAD_CONST               8 (('alias',))
              CALL_KW                  2

 48           BUILD_TUPLE              2
              LOAD_CONST              10 (<code object __annotate__ at 0x0000018C18024C30, file "app\routes\tenant_incidents.py", line 48>)
              MAKE_FUNCTION
              LOAD_CONST              11 (<code object require_brokerage at 0x0000018C1796DBD0, file "app\routes\tenant_incidents.py", line 48>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              20 (require_brokerage)

 71           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C18025730, file "app\routes\tenant_incidents.py", line 71>)
              MAKE_FUNCTION
              LOAD_CONST              13 (<code object _emit_tenant_event at 0x0000018C18038670, file "app\routes\tenant_incidents.py", line 71>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              21 (_emit_tenant_event)

 86           LOAD_NAME               17 (router)
              LOAD_ATTR               45 (get + NULL|self)
              LOAD_CONST              14 ('/incidents')
              CALL                     1

 88           LOAD_NAME               14 (Query)
              PUSH_NULL
              LOAD_CONST               2 (None)
              LOAD_SMALL_INT           8
              LOAD_CONST              15 (('max_length',))
              CALL_KW                  2

 89           LOAD_NAME               14 (Query)
              PUSH_NULL
              LOAD_CONST               2 (None)
              LOAD_SMALL_INT          32
              LOAD_CONST              15 (('max_length',))
              CALL_KW                  2

 90           LOAD_NAME               14 (Query)
              PUSH_NULL
              LOAD_SMALL_INT          25
              CALL                     1

 91           LOAD_NAME               14 (Query)
              PUSH_NULL
              LOAD_SMALL_INT           0
              CALL                     1

 92           LOAD_NAME               14 (Query)
              PUSH_NULL
              LOAD_CONST               2 (None)
              LOAD_SMALL_INT          64
              LOAD_CONST              15 (('max_length',))
              CALL_KW                  2

 93           LOAD_NAME               14 (Query)
              PUSH_NULL
              LOAD_CONST               2 (None)
              LOAD_SMALL_INT          64
              LOAD_CONST              15 (('max_length',))
              CALL_KW                  2

 94           LOAD_NAME               10 (Depends)
              PUSH_NULL
              LOAD_NAME               20 (require_brokerage)
              CALL                     1

 87           BUILD_TUPLE              7
              LOAD_CONST              16 (<code object __annotate__ at 0x0000018C180E8030, file "app\routes\tenant_incidents.py", line 87>)
              MAKE_FUNCTION
              LOAD_CONST              17 (<code object list_tenant_incidents at 0x0000018C17E94610, file "app\routes\tenant_incidents.py", line 86>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

 86           CALL                     0

 87           STORE_NAME              23 (list_tenant_incidents)

132           LOAD_NAME               17 (router)
              LOAD_ATTR               45 (get + NULL|self)
              LOAD_CONST              18 ('/incidents/{incident_id}')
              CALL                     1

134           LOAD_NAME               13 (Path)
              PUSH_NULL
              LOAD_CONST              19 (Ellipsis)
              LOAD_SMALL_INT          64
              LOAD_CONST              15 (('max_length',))
              CALL_KW                  2

135           LOAD_NAME               10 (Depends)
              PUSH_NULL
              LOAD_NAME               20 (require_brokerage)
              CALL                     1

133           BUILD_TUPLE              2
              LOAD_CONST              20 (<code object __annotate__ at 0x0000018C18026130, file "app\routes\tenant_incidents.py", line 133>)
              MAKE_FUNCTION
              LOAD_CONST              21 (<code object get_tenant_incident at 0x0000018C17D8E300, file "app\routes\tenant_incidents.py", line 132>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

132           CALL                     0

133           STORE_NAME              24 (get_tenant_incident)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "app\routes\tenant_incidents.py", line 48>:
 48           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('x_api_key')

 49           LOAD_CONST               2 ('Optional[str]')

 48           LOAD_CONST               3 ('x_admin_key')

 50           LOAD_CONST               2 ('Optional[str]')

 48           LOAD_CONST               4 ('return')

 51           LOAD_CONST               5 ('Dict[str, Any]')

 48           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object require_brokerage at 0x0000018C1796DBD0, file "app\routes\tenant_incidents.py", line 48>:
 48           RESUME                   0

 54           LOAD_FAST_BORROW         1 (x_admin_key)
              TO_BOOL
              POP_JUMP_IF_FALSE       14 (to L1)
              NOT_TAKEN

 55           LOAD_GLOBAL              1 (HTTPException + NULL)

 56           LOAD_CONST               0 (401)

 57           LOAD_CONST               1 ('Admin key not accepted on tenant surface')

 55           LOAD_CONST               2 (('status_code', 'detail'))
              CALL_KW                  2
              RAISE_VARARGS            1

 59   L1:     LOAD_FAST_BORROW         0 (x_api_key)
              TO_BOOL
              POP_JUMP_IF_TRUE        14 (to L2)
              NOT_TAKEN

 60           LOAD_GLOBAL              1 (HTTPException + NULL)
              LOAD_CONST               0 (401)
              LOAD_CONST               3 ('Missing X-API-Key')
              LOAD_CONST               2 (('status_code', 'detail'))
              CALL_KW                  2
              RAISE_VARARGS            1

 61   L2:     LOAD_GLOBAL              3 (get_brokerage_by_api_key + NULL)
              LOAD_FAST_BORROW         0 (x_api_key)
              CALL                     1
              STORE_FAST               2 (brokerage)

 62           LOAD_FAST_BORROW         2 (brokerage)
              TO_BOOL
              POP_JUMP_IF_FALSE       23 (to L3)
              NOT_TAKEN
              LOAD_FAST_BORROW         2 (brokerage)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               4 ('id')
              CALL                     1
              LOAD_CONST               5 ('demo')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE       14 (to L4)
              NOT_TAKEN

 63   L3:     LOAD_GLOBAL              1 (HTTPException + NULL)
              LOAD_CONST               0 (401)
              LOAD_CONST               6 ('Invalid API key')
              LOAD_CONST               2 (('status_code', 'detail'))
              CALL_KW                  2
              RAISE_VARARGS            1

 64   L4:     LOAD_FAST_BORROW         2 (brokerage)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025730, file "app\routes\tenant_incidents.py", line 71>:
 71           RESUME                   0
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

Disassembly of <code object _emit_tenant_event at 0x0000018C18038670, file "app\routes\tenant_incidents.py", line 71>:
  71            RESUME                   0

  72            NOP

  73    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               1 (('log_event_bg',))
                IMPORT_NAME              0 (app.db.event_logger)
                IMPORT_FROM              1 (log_event_bg)
                STORE_FAST               2 (log_event_bg)
                POP_TOP

  76    L2:     NOP

  77    L3:     LOAD_FAST                2 (log_event_bg)
                PUSH_NULL
                LOAD_FAST_LOAD_FAST      1 (event_type, payload)
                CALL                     2
                POP_TOP
        L4:     LOAD_CONST               2 (None)
                RETURN_VALUE

  --    L5:     PUSH_EXC_INFO

  74            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L7)
                NOT_TAKEN
                POP_TOP

  75    L6:     POP_EXCEPT
                LOAD_CONST               2 (None)
                RETURN_VALUE

  74    L7:     RERAISE                  0

  --    L8:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
        L9:     PUSH_EXC_INFO

  78            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L11)
                NOT_TAKEN
                POP_TOP

  79   L10:     POP_EXCEPT
                LOAD_CONST               2 (None)
                RETURN_VALUE

  78   L11:     RERAISE                  0

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

Disassembly of <code object __annotate__ at 0x0000018C180E8030, file "app\routes\tenant_incidents.py", line 87>:
 87           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('severity')

 88           LOAD_CONST               2 ('Optional[str]')

 87           LOAD_CONST               3 ('status')

 89           LOAD_CONST               2 ('Optional[str]')

 87           LOAD_CONST               4 ('limit')

 90           LOAD_CONST               5 ('int')

 87           LOAD_CONST               6 ('offset')

 91           LOAD_CONST               5 ('int')

 87           LOAD_CONST               7 ('date_from')

 92           LOAD_CONST               2 ('Optional[str]')

 87           LOAD_CONST               8 ('date_to')

 93           LOAD_CONST               2 ('Optional[str]')

 87           LOAD_CONST               9 ('brokerage')

 94           LOAD_CONST              10 ('Dict[str, Any]')

 87           LOAD_CONST              11 ('return')

 95           LOAD_CONST              10 ('Dict[str, Any]')

 87           BUILD_MAP                8
              RETURN_VALUE

Disassembly of <code object list_tenant_incidents at 0x0000018C17E94610, file "app\routes\tenant_incidents.py", line 86>:
  86           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0

  96           LOAD_FAST_BORROW         6 (brokerage)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('id')
               CALL                     1
               STORE_FAST               7 (bid)

  97           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('list_tenant_incidents_for_brokerage',))
               IMPORT_NAME              1 (app.services.tenant.tenant_incident_projection)
               IMPORT_FROM              2 (list_tenant_incidents_for_brokerage)
               STORE_FAST               8 (list_tenant_incidents_for_brokerage)
               POP_TOP

 100           LOAD_FAST_BORROW         8 (list_tenant_incidents_for_brokerage)
               PUSH_NULL

 101           LOAD_FAST_BORROW         7 (bid)

 102           LOAD_FAST_BORROW         0 (severity)

 103           LOAD_FAST_BORROW         1 (status)

 104           LOAD_FAST_BORROW         2 (limit)

 105           LOAD_FAST_BORROW         3 (offset)

 106           LOAD_FAST_BORROW         4 (date_from)

 107           LOAD_FAST_BORROW         5 (date_to)

 100           LOAD_CONST               2 (('severity', 'status', 'limit', 'offset', 'date_from', 'date_to'))
               CALL_KW                  7
               STORE_FAST               9 (env)

 112           LOAD_GLOBAL              7 (int + NULL)
               LOAD_FAST_BORROW         9 (env)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               3 ('filter_count')
               LOAD_SMALL_INT           0
               CALL                     2
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               LOAD_SMALL_INT           0
       L2:     CALL                     1
               STORE_FAST              10 (fcount)

 113           LOAD_FAST_BORROW        10 (fcount)
               LOAD_SMALL_INT           0
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE       55 (to L3)
               NOT_TAKEN

 114           LOAD_GLOBAL              9 (_emit_tenant_event + NULL)
               LOAD_CONST               4 ('tenant.incident.filtered_viewed')

 115           LOAD_CONST               5 ('brokerage_id')
               LOAD_FAST_BORROW         7 (bid)

 116           LOAD_CONST               6 ('status')
               LOAD_FAST_BORROW         9 (env)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               6 ('status')
               CALL                     1

 117           LOAD_CONST               7 ('route')
               LOAD_CONST               8 ('list_tenant_incidents')

 118           LOAD_CONST               3 ('filter_count')
               LOAD_FAST_BORROW        10 (fcount)

 119           LOAD_CONST               9 ('action_required')
               LOAD_CONST              10 ('none')

 120           LOAD_CONST              11 ('error_code')
               LOAD_FAST_BORROW         9 (env)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST              11 ('error_code')
               CALL                     1

 114           BUILD_MAP                6
               CALL                     2
               POP_TOP

 122   L3:     LOAD_GLOBAL              9 (_emit_tenant_event + NULL)
               LOAD_CONST              12 ('tenant.incident.viewed')

 123           LOAD_CONST               5 ('brokerage_id')
               LOAD_FAST_BORROW         7 (bid)

 124           LOAD_CONST               6 ('status')
               LOAD_FAST_BORROW         9 (env)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               6 ('status')
               CALL                     1

 125           LOAD_CONST               7 ('route')
               LOAD_CONST               8 ('list_tenant_incidents')

 126           LOAD_CONST               9 ('action_required')
               LOAD_CONST              10 ('none')

 127           LOAD_CONST              11 ('error_code')
               LOAD_FAST_BORROW         9 (env)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST              11 ('error_code')
               CALL                     1

 122           BUILD_MAP                5
               CALL                     2
               POP_TOP

 129           LOAD_FAST_BORROW         9 (env)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026130, file "app\routes\tenant_incidents.py", line 133>:
133           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('incident_id')

134           LOAD_CONST               2 ('str')

133           LOAD_CONST               3 ('brokerage')

135           LOAD_CONST               4 ('Dict[str, Any]')

133           LOAD_CONST               5 ('return')

136           LOAD_CONST               4 ('Dict[str, Any]')

133           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object get_tenant_incident at 0x0000018C17D8E300, file "app\routes\tenant_incidents.py", line 132>:
 132           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0

 137           LOAD_FAST_BORROW         1 (brokerage)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('id')
               CALL                     1
               STORE_FAST               2 (bid)

 138           LOAD_FAST                0 (incident_id)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L2:     LOAD_ATTR                3 (strip + NULL|self)
               CALL                     0
               STORE_FAST               3 (iid)

 139           LOAD_FAST_BORROW         3 (iid)
               TO_BOOL
               POP_JUMP_IF_TRUE        14 (to L5)
       L3:     NOT_TAKEN

 140   L4:     LOAD_GLOBAL              5 (HTTPException + NULL)
               LOAD_CONST               2 (400)
               LOAD_CONST               3 ('invalid_incident_id')
               LOAD_CONST               4 (('status_code', 'detail'))
               CALL_KW                  2
               RAISE_VARARGS            1

 141   L5:     LOAD_SMALL_INT           0
               LOAD_CONST               5 (('get_tenant_incident_for_brokerage',))
               IMPORT_NAME              3 (app.services.tenant.tenant_incident_projection)
               IMPORT_FROM              4 (get_tenant_incident_for_brokerage)
               STORE_FAST               4 (get_tenant_incident_for_brokerage)
               POP_TOP

 144           LOAD_FAST_BORROW         4 (get_tenant_incident_for_brokerage)
               PUSH_NULL

 145           LOAD_FAST_BORROW         2 (bid)

 146           LOAD_FAST_BORROW         3 (iid)

 144           LOAD_CONST               6 (('brokerage_id', 'incident_id'))
               CALL_KW                  2
               STORE_FAST               5 (env)

 148           LOAD_GLOBAL             11 (_emit_tenant_event + NULL)
               LOAD_CONST               7 ('tenant.incident.viewed')

 149           LOAD_CONST               8 ('brokerage_id')
               LOAD_FAST_BORROW         2 (bid)

 150           LOAD_CONST               9 ('incident_id')
               LOAD_FAST_BORROW         3 (iid)

 151           LOAD_CONST              10 ('status')
               LOAD_FAST_BORROW         5 (env)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST              10 ('status')
               CALL                     1

 152           LOAD_CONST              11 ('route')
               LOAD_CONST              12 ('get_tenant_incident')

 153           LOAD_CONST              13 ('action_required')
               LOAD_CONST              14 ('none')

 154           LOAD_CONST              15 ('error_code')
               LOAD_FAST_BORROW         5 (env)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST              15 ('error_code')
               CALL                     1

 148           BUILD_MAP                6
               CALL                     2
               POP_TOP

 156           LOAD_FAST_BORROW         5 (env)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST              10 ('status')
               CALL                     1
               LOAD_CONST              16 ('failed')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       36 (to L6)
               NOT_TAKEN
               LOAD_FAST_BORROW         5 (env)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST              15 ('error_code')
               CALL                     1
               LOAD_CONST              17 ('incident_not_found')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       14 (to L6)
               NOT_TAKEN

 157           LOAD_GLOBAL              5 (HTTPException + NULL)
               LOAD_CONST              18 (404)
               LOAD_CONST              17 ('incident_not_found')
               LOAD_CONST               4 (('status_code', 'detail'))
               CALL_KW                  2
               RAISE_VARARGS            1

 158   L6:     LOAD_FAST_BORROW         5 (env)
               RETURN_VALUE

  --   L7:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L7 [0] lasti
  L4 to L7 -> L7 [0] lasti
```
