# routes/operator_brokerages

- **pyc:** `app\routes\__pycache__\operator_brokerages.cpython-314.pyc`
- **expected source path (absent):** `app\routes/operator_brokerages.py`
- **co_filename (from bytecode):** `app/routes/operator_brokerages.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** routes

## Module docstring

```
PAS173 — Multi-brokerage operator routes.

Admin-only surfaces for the brokerage operator system. Mounted
at ``/ops/brokerages`` (alongside PAS172's ``/ops/*`` namespace).
Auth: X-Admin-Key header against ``settings.ADMIN_API_KEY`` —
same model as ``app/routes/admin.py`` and
``app/routes/operator_ops.py``.

Doctrine:

* **Tenant exposure: NONE.** Every route requires the admin key.
* **No PII.** Every envelope is the structural shape produced by
  the underlying service layer (profile_service /
  config_validator / operator_actions / onboarding_templates).
  Routes run a defensive forbidden-token scan on every response.
* **Pagination caps clamped server-side.**
* **Closed action allow-list.** The POST /actions endpoint
  delegates to ``operator_actions.execute_action`` which
  refuses anything outside the closed allow-list — there is
  no arbitrary mutation surface.
* **Never raises.** All routes catch and project; failures
  flip the envelope to ``status="failed"`` / ``"skipped"``.

Routes:

    GET  /ops/brokerages
    GET  /ops/brokerages/{brokerage_id}
    GET  /ops/brokerages/{brokerage_id}/health
    GET  /ops/brokerages/{brokerage_id}/launch-readiness
    POST /ops/brokerages/{brokerage_id}/actions
    GET  /ops/brokerages/{brokerage_id}/onboarding-checklist
```

## Imports

`APIRouter`, `Any`, `BaseModel`, `Depends`, `Dict`, `Field`, `HTTPException`, `Header`, `Optional`, `Query`, `__future__`, `annotations`, `app.config`, `app.db.brokerage_store`, `app.services.brokerage.config_validator`, `app.services.brokerage.onboarding_templates`, `app.services.brokerage.profile_service`, `app.services.ingestion.pending_call_recovery`, `app.services.operator.audit_verification_runs`, `app.services.operator.audit_window_chain`, `app.services.operator.operator_actions`, `app.services.security.rate_limit`, `app.services.worker.heartbeat_monitor`, `brokerage_chain_badge`, `brokerage_onboarding_checklist`, `chain_status_report`, `check_rate_limit`, `configuration_warning_report`, `execute_action`, `fastapi`, `get_brokerage_by_id`, `get_profile`, `get_settings`, `heartbeat_monitor_report`, `launch_checklist`, `list_profiles`, `list_verification_runs`, `logging`, `pilot_expansion_checklist`, `pydantic`, `queue_status_report`, `rollback_checklist`, `smoke_test_template`, `typing`, `validate_brokerage_launch_ready`, `verification_run_summary`

## Classes

`OperatorActionRequest`

## Functions / methods

`__annotate__`, `_clamp_int`, `_final_envelope`, `_safe_brokerage`, `_scan_for_forbidden`, `get_brokerage_audit_chain_status`, `get_brokerage_health`, `get_brokerage_route`, `get_brokerage_verification_runs`, `get_launch_readiness`, `get_onboarding_checklist`, `list_brokerages_route`, `post_brokerage_action`, `require_admin`

## Env-key candidates

`ADMIN`

## String constants (redacted where noted)

- '\nPAS173 — Multi-brokerage operator routes.\n\nAdmin-only surfaces for the brokerage operator system. Mounted\nat ``/ops/brokerages`` (alongside PAS172\'s ``/ops/*`` namespace).\nAuth: X-Admin-Key header against ``settings.ADMIN_API_KEY`` —\nsame model as ``app/routes/admin.py`` and\n``app/routes/operator_ops.py``.\n\nDoctrine:\n\n* **Tenant exposure: NONE.** Every route requires the admin key.\n* **No PII.** Every envelope is the structural shape produced by\n  the underlying service layer (profile_service /\n  config_validator / operator_actions / onboarding_templates).\n  Routes run a defensive forbidden-token scan on every response.\n* **Pagination caps clamped server-side.**\n* **Closed action allow-list.** The POST /actions endpoint\n  delegates to ``operator_actions.execute_action`` which\n  refuses anything outside the closed allow-list — there is\n  no arbitrary mutation surface.\n* **Never raises.** All routes catch and project; failures\n  flip the envelope to ``status="failed"`` / ``"skipped"``.\n\nRoutes:\n\n    GET  /ops/brokerages\n    GET  /ops/brokerages/{brokerage_id}\n    GET  /ops/brokerages/{brokerage_id}/health\n    GET  /ops/brokerages/{brokerage_id}/launch-readiness\n    POST /ops/brokerages/{brokerage_id}/actions\n    GET  /ops/brokerages/{brokerage_id}/onboarding-checklist\n'
- 'pas.ops.brokerages'
- '/{brokerage_id}'
- '/{brokerage_id}/health'
- '/{brokerage_id}/launch-readiness'
- '/{brokerage_id}/onboarding-checklist'
- 'onboarding'
- '/{brokerage_id}/audit-chain-status'
- '/{brokerage_id}/verification-runs'
- 'OperatorActionRequest'
- '/{brokerage_id}/actions'
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
- 'obj'
- 'env'
- 'Dict[str, Any]'
- 'surface'
- 'operator_brokerages surface='
- ' collapsed — forbidden token leaked'
- 'status'
- 'failed'
- 'error_code'
- 'ops_envelope_forbidden_token'
- 'warnings'
- 'value'
- 'int'
- 'default'
- 'onboarding_status'
- 'pilot_stage'
- 'limit'
- 'Multi-brokerage operator view. Reads the PAS173 profile\ntable only; never joins back to the brokerages credential\ntable.'
- 'ops.brokerages.list'
- 'list'
- 'operator_brokerages list error type='
- 'unexpected:'
- 'brokerage_id'
- 'invalid brokerage_id'
- 'ops.brokerages.get'
- 'profile'
- 'operator_brokerages get error type='
- 'Combined per-brokerage health snapshot. Wraps the\nconfig_validator + the PAS170 queue + the PAS172 heartbeat\nsummary into a single structural envelope.'
- 'get_brokerage_health brokerage read error type='
- 'active'
- 'ops.brokerages.health'
- 'config'
- 'errors'
- 'warning_count'
- 'error_count'
- 'queue'
- 'total'
- 'by_status'
- 'oldest_age_seconds'
- 'heartbeat'
- 'operator_brokerages health error type='
- 'required_pilot_stage'
- 'get_launch_readiness brokerage read error type='
- 'ops.brokerages.launch_readiness'
- 'launch_ready'
- 'profile_present'
- 'operator_brokerages launch_readiness error type='
- 'template'
- 'launch'
- 'rollback'
- 'smoke'
- 'pilot_expansion'
- 'ops.brokerages.onboarding_checklist'
- 'invalid_template'
- 'checklist'
- 'operator_brokerages onboarding_checklist error type='
- 'PAS178 — Per-brokerage cross-window chain-status badge\nfor the multi-brokerage operator console. Read-only;\nNEVER mutates anything.'
- 'skipped'
- 'ops.brokerages.audit_chain_status'
- 'badge'
- 'summary'
- 'latest_entry'
- 'operator_brokerages audit_chain_status error type='
- 'verification_type'
- 'PAS178 — Per-brokerage durable verification-run history\nfor the operator console. Read-only.'
- 'ops.brokerages.verification_runs'
- 'runs'
- 'by_type'
- 'latest_run'
- 'operator_brokerages verification_runs error type='
- 'action'
- 'actor_id'
- 'operator'
- 'actor_type'
- 'payload'
- 'body'
- 'ops.brokerages.actions'
- 'result'
- 'operator_brokerages actions error type='

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS173 — Multi-brokerage operator routes.\n\nAdmin-only surfaces for the brokerage operator system. Mounted\nat ``/ops/brokerages`` (alongside PAS172\'s ``/ops/*`` namespace).\nAuth: X-Admin-Key header against ``settings.ADMIN_API_KEY`` —\nsame model as ``app/routes/admin.py`` and\n``app/routes/operator_ops.py``.\n\nDoctrine:\n\n* **Tenant exposure: NONE.** Every route requires the admin key.\n* **No PII.** Every envelope is the structural shape produced by\n  the underlying service layer (profile_service /\n  config_validator / operator_actions / onboarding_templates).\n  Routes run a defensive forbidden-token scan on every response.\n* **Pagination caps clamped server-side.**\n* **Closed action allow-list.** The POST /actions endpoint\n  delegates to ``operator_actions.execute_action`` which\n  refuses anything outside the closed allow-list — there is\n  no arbitrary mutation surface.\n* **Never raises.** All routes catch and project; failures\n  flip the envelope to ``status="failed"`` / ``"skipped"``.\n\nRoutes:\n\n    GET  /ops/brokerages\n    GET  /ops/brokerages/{brokerage_id}\n    GET  /ops/brokerages/{brokerage_id}/health\n    GET  /ops/brokerages/{brokerage_id}/launch-readiness\n    POST /ops/brokerages/{brokerage_id}/actions\n    GET  /ops/brokerages/{brokerage_id}/onboarding-checklist\n')
              STORE_NAME               0 (__doc__)

 35           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 37           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 38           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('Any', 'Dict', 'Optional'))
              IMPORT_NAME              4 (typing)
              IMPORT_FROM              5 (Any)
              STORE_NAME               5 (Any)
              IMPORT_FROM              6 (Dict)
              STORE_NAME               6 (Dict)
              IMPORT_FROM              7 (Optional)
              STORE_NAME               7 (Optional)
              POP_TOP

 40           LOAD_SMALL_INT           0
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

 41           LOAD_SMALL_INT           0
              LOAD_CONST               5 (('BaseModel', 'Field'))
              IMPORT_NAME             14 (pydantic)
              IMPORT_FROM             15 (BaseModel)
              STORE_NAME              15 (BaseModel)
              IMPORT_FROM             16 (Field)
              STORE_NAME              16 (Field)
              POP_TOP

 43           LOAD_SMALL_INT           0
              LOAD_CONST               6 (('get_settings',))
              IMPORT_NAME             17 (app.config)
              IMPORT_FROM             18 (get_settings)
              STORE_NAME              18 (get_settings)
              POP_TOP

 46           LOAD_NAME                9 (APIRouter)
              PUSH_NULL
              CALL                     0
              STORE_NAME              19 (router)

 47           LOAD_NAME                3 (logging)
              LOAD_ATTR               40 (getLogger)
              PUSH_NULL
              LOAD_CONST               7 ('pas.ops.brokerages')
              CALL                     1
              STORE_NAME              21 (logger)

 50           LOAD_NAME               12 (Header)
              PUSH_NULL
              LOAD_CONST               8 (Ellipsis)
              CALL                     1
              BUILD_TUPLE              1
              LOAD_CONST               9 (<code object __annotate__ at 0x0000018C17FA3A50, file "app/routes/operator_brokerages.py", line 50>)
              MAKE_FUNCTION
              LOAD_CONST              10 (<code object require_admin at 0x0000018C1801C410, file "app/routes/operator_brokerages.py", line 50>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              22 (require_admin)

 79           LOAD_SMALL_INT         200
              STORE_NAME              23 (_BROKERAGE_ID_MAX_LEN)

 80           LOAD_SMALL_INT          50
              STORE_NAME              24 (_LIST_LIMIT_DEFAULT)

 81           LOAD_CONST              11 (500)
              STORE_NAME              25 (_LIST_LIMIT_MAX)

 83           LOAD_CONST              48 (('phone', 'email', 'name_token', 'transcript', 'summary_text', 'raw_payload', 'raw_email', 'raw_body', 'secret', 'signature', 'dedupe_key', 'callback_notes'))
              STORE_NAME              26 (_FORBIDDEN_RESPONSE_TOKENS)

 90           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA2A60, file "app/routes/operator_brokerages.py", line 90>)
              MAKE_FUNCTION
              LOAD_CONST              13 (<code object _scan_for_forbidden at 0x0000018C18025E30, file "app/routes/operator_brokerages.py", line 90>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              27 (_scan_for_forbidden)

114           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C18025730, file "app/routes/operator_brokerages.py", line 114>)
              MAKE_FUNCTION
              LOAD_CONST              15 (<code object _final_envelope at 0x0000018C17FE1680, file "app/routes/operator_brokerages.py", line 114>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              28 (_final_envelope)

130           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C17FA33C0, file "app/routes/operator_brokerages.py", line 130>)
              MAKE_FUNCTION
              LOAD_CONST              17 (<code object _safe_brokerage at 0x0000018C17F96420, file "app/routes/operator_brokerages.py", line 130>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              29 (_safe_brokerage)

141           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C18025D30, file "app/routes/operator_brokerages.py", line 141>)
              MAKE_FUNCTION
              LOAD_CONST              19 (<code object _clamp_int at 0x0000018C18038DF0, file "app/routes/operator_brokerages.py", line 141>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              30 (_clamp_int)

157           LOAD_NAME               19 (router)
              LOAD_ATTR               63 (get + NULL|self)
              LOAD_CONST              20 ('')
              CALL                     1

159           LOAD_NAME               13 (Query)
              PUSH_NULL
              LOAD_CONST               2 (None)
              LOAD_SMALL_INT          64
              LOAD_CONST              21 (('max_length',))
              CALL_KW                  2

160           LOAD_NAME               13 (Query)
              PUSH_NULL
              LOAD_CONST               2 (None)
              LOAD_SMALL_INT          64
              LOAD_CONST              21 (('max_length',))
              CALL_KW                  2

161           LOAD_NAME               13 (Query)
              PUSH_NULL
              LOAD_NAME               24 (_LIST_LIMIT_DEFAULT)
              CALL                     1

162           LOAD_NAME               10 (Depends)
              PUSH_NULL
              LOAD_NAME               22 (require_admin)
              CALL                     1

158           BUILD_TUPLE              4
              LOAD_CONST              22 (<code object __annotate__ at 0x0000018C18025530, file "app/routes/operator_brokerages.py", line 158>)
              MAKE_FUNCTION
              LOAD_CONST              23 (<code object list_brokerages_route at 0x0000018C17D77E00, file "app/routes/operator_brokerages.py", line 157>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

157           CALL                     0

158           STORE_NAME              32 (list_brokerages_route)

193           LOAD_NAME               19 (router)
              LOAD_ATTR               63 (get + NULL|self)
              LOAD_CONST              24 ('/{brokerage_id}')
              CALL                     1

196           LOAD_NAME               10 (Depends)
              PUSH_NULL
              LOAD_NAME               22 (require_admin)
              CALL                     1

194           BUILD_TUPLE              1
              LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA2880, file "app/routes/operator_brokerages.py", line 194>)
              MAKE_FUNCTION
              LOAD_CONST              26 (<code object get_brokerage_route at 0x0000018C17CD4970, file "app/routes/operator_brokerages.py", line 193>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

193           CALL                     0

194           STORE_NAME              33 (get_brokerage_route)

224           LOAD_NAME               19 (router)
              LOAD_ATTR               63 (get + NULL|self)
              LOAD_CONST              27 ('/{brokerage_id}/health')
              CALL                     1

227           LOAD_NAME               10 (Depends)
              PUSH_NULL
              LOAD_NAME               22 (require_admin)
              CALL                     1

225           BUILD_TUPLE              1
              LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA2100, file "app/routes/operator_brokerages.py", line 225>)
              MAKE_FUNCTION
              LOAD_CONST              29 (<code object get_brokerage_health at 0x0000018C17E94C50, file "app/routes/operator_brokerages.py", line 224>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

224           CALL                     0

225           STORE_NAME              34 (get_brokerage_health)

297           LOAD_NAME               19 (router)
              LOAD_ATTR               63 (get + NULL|self)
              LOAD_CONST              30 ('/{brokerage_id}/launch-readiness')
              CALL                     1

300           LOAD_NAME               13 (Query)
              PUSH_NULL
              LOAD_CONST               2 (None)
              LOAD_SMALL_INT          64
              LOAD_CONST              21 (('max_length',))
              CALL_KW                  2

301           LOAD_NAME               10 (Depends)
              PUSH_NULL
              LOAD_NAME               22 (require_admin)
              CALL                     1

298           BUILD_TUPLE              2
              LOAD_CONST              31 (<code object __annotate__ at 0x0000018C18025130, file "app/routes/operator_brokerages.py", line 298>)
              MAKE_FUNCTION
              LOAD_CONST              32 (<code object get_launch_readiness at 0x0000018C17E951B0, file "app/routes/operator_brokerages.py", line 297>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

297           CALL                     0

298           STORE_NAME              35 (get_launch_readiness)

350           LOAD_NAME               19 (router)
              LOAD_ATTR               63 (get + NULL|self)
              LOAD_CONST              33 ('/{brokerage_id}/onboarding-checklist')
              CALL                     1

353           LOAD_NAME               13 (Query)
              PUSH_NULL
              LOAD_CONST              34 ('onboarding')
              LOAD_SMALL_INT          64
              LOAD_CONST              21 (('max_length',))
              CALL_KW                  2

354           LOAD_NAME               10 (Depends)
              PUSH_NULL
              LOAD_NAME               22 (require_admin)
              CALL                     1

351           BUILD_TUPLE              2
              LOAD_CONST              35 (<code object __annotate__ at 0x0000018C18024930, file "app/routes/operator_brokerages.py", line 351>)
              MAKE_FUNCTION
              LOAD_CONST              36 (<code object get_onboarding_checklist at 0x0000018C17E955D0, file "app/routes/operator_brokerages.py", line 350>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

350           CALL                     0

351           STORE_NAME              36 (get_onboarding_checklist)

403           LOAD_NAME               19 (router)
              LOAD_ATTR               63 (get + NULL|self)
              LOAD_CONST              37 ('/{brokerage_id}/audit-chain-status')
              CALL                     1

406           LOAD_NAME               10 (Depends)
              PUSH_NULL
              LOAD_NAME               22 (require_admin)
              CALL                     1

404           BUILD_TUPLE              1
              LOAD_CONST              38 (<code object __annotate__ at 0x0000018C17FA1D40, file "app/routes/operator_brokerages.py", line 404>)
              MAKE_FUNCTION
              LOAD_CONST              39 (<code object get_brokerage_audit_chain_status at 0x0000018C17D51290, file "app/routes/operator_brokerages.py", line 403>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

403           CALL                     0

404           STORE_NAME              37 (get_brokerage_audit_chain_status)

447           LOAD_NAME               19 (router)
              LOAD_ATTR               63 (get + NULL|self)
              LOAD_CONST              40 ('/{brokerage_id}/verification-runs')
              CALL                     1

450           LOAD_NAME               13 (Query)
              PUSH_NULL
              LOAD_CONST               2 (None)
              LOAD_SMALL_INT          64
              LOAD_CONST              21 (('max_length',))
              CALL_KW                  2

451           LOAD_NAME               13 (Query)
              PUSH_NULL
              LOAD_NAME               24 (_LIST_LIMIT_DEFAULT)
              CALL                     1

452           LOAD_NAME               10 (Depends)
              PUSH_NULL
              LOAD_NAME               22 (require_admin)
              CALL                     1

448           BUILD_TUPLE              3
              LOAD_CONST              41 (<code object __annotate__ at 0x0000018C18026530, file "app/routes/operator_brokerages.py", line 448>)
              MAKE_FUNCTION
              LOAD_CONST              42 (<code object get_brokerage_verification_runs at 0x0000018C17D515E0, file "app/routes/operator_brokerages.py", line 447>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

447           CALL                     0

448           STORE_NAME              38 (get_brokerage_verification_runs)

502           LOAD_BUILD_CLASS
              PUSH_NULL
              LOAD_CONST              43 (<code object OperatorActionRequest at 0x0000018C18011210, file "app/routes/operator_brokerages.py", line 502>)
              MAKE_FUNCTION
              LOAD_CONST              44 ('OperatorActionRequest')
              LOAD_NAME               15 (BaseModel)
              CALL                     3
              STORE_NAME              39 (OperatorActionRequest)

509           LOAD_NAME               19 (router)
              LOAD_ATTR               81 (post + NULL|self)
              LOAD_CONST              45 ('/{brokerage_id}/actions')
              CALL                     1

513           LOAD_NAME               10 (Depends)
              PUSH_NULL
              LOAD_NAME               22 (require_admin)
              CALL                     1

510           BUILD_TUPLE              1
              LOAD_CONST              46 (<code object __annotate__ at 0x0000018C18026230, file "app/routes/operator_brokerages.py", line 510>)
              MAKE_FUNCTION
              LOAD_CONST              47 (<code object post_brokerage_action at 0x0000018C17D51980, file "app/routes/operator_brokerages.py", line 509>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

509           CALL                     0

510           STORE_NAME              41 (post_brokerage_action)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "app/routes/operator_brokerages.py", line 50>:
 50           RESUME                   0
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

Disassembly of <code object require_admin at 0x0000018C1801C410, file "app/routes/operator_brokerages.py", line 50>:
  50            RESUME                   0

  51            LOAD_GLOBAL              1 (get_settings + NULL)
                CALL                     0
                STORE_FAST               1 (settings)

  52            LOAD_FAST_BORROW         1 (settings)
                LOAD_ATTR                2 (ADMIN_API_KEY)
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (x_admin_key, settings)
                LOAD_ATTR                2 (ADMIN_API_KEY)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       14 (to L2)
                NOT_TAKEN

  53    L1:     LOAD_GLOBAL              5 (HTTPException + NULL)
                LOAD_CONST               0 (401)
                LOAD_CONST               1 ('Invalid admin key')
                LOAD_CONST               2 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

  56    L2:     NOP

  57    L3:     LOAD_SMALL_INT           0
                LOAD_CONST               3 (('check_rate_limit',))
                IMPORT_NAME              3 (app.services.security.rate_limit)
                IMPORT_FROM              4 (check_rate_limit)
                STORE_FAST               2 (check_rate_limit)
                POP_TOP

  58            LOAD_FAST_BORROW         2 (check_rate_limit)
                PUSH_NULL

  59            LOAD_CONST               4 ('admin')

  60            LOAD_CONST               5 ('ADMIN')

  61            LOAD_FAST_BORROW         0 (x_admin_key)

  58            LOAD_CONST               6 (('surface', 'actor_type', 'actor_token'))
                CALL_KW                  3
                STORE_FAST               3 (_rl_verdict)

  63            LOAD_FAST_BORROW         3 (_rl_verdict)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               7 ('allowed')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        14 (to L6)
        L4:     NOT_TAKEN

  64    L5:     LOAD_GLOBAL              5 (HTTPException + NULL)

  65            LOAD_CONST               8 (429)

  66            LOAD_CONST               9 ('Operator rate limit exceeded. Retry after the current window.')

  64            LOAD_CONST               2 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

  63    L6:     NOP

  72            LOAD_CONST              10 (True)
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

  68            LOAD_GLOBAL              4 (HTTPException)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                POP_TOP

  69            RAISE_VARARGS            0

  70    L8:     LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L12)
        L9:     NOT_TAKEN
       L10:     POP_TOP

  71   L11:     POP_EXCEPT

  72            LOAD_CONST              10 (True)
                RETURN_VALUE

  70   L12:     RERAISE                  0

  --   L13:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L7 [0]
  L5 to L6 -> L7 [0]
  L7 to L9 -> L13 [1] lasti
  L10 to L11 -> L13 [1] lasti
  L12 to L13 -> L13 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "app/routes/operator_brokerages.py", line 90>:
 90           RESUME                   0
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

Disassembly of <code object _scan_for_forbidden at 0x0000018C18025E30, file "app/routes/operator_brokerages.py", line 90>:
  --           MAKE_CELL                1 (walk)

  90           RESUME                   0

  91           LOAD_CONST               0 (<code object __annotate__ at 0x0000018C17FA3000, file "app/routes/operator_brokerages.py", line 91>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         1 (walk)
               BUILD_TUPLE              1
               LOAD_CONST               1 (<code object walk at 0x0000018C17CC1F60, file "app/routes/operator_brokerages.py", line 91>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_DEREF              1 (walk)

 111           LOAD_DEREF               1 (walk)
               PUSH_NULL
               LOAD_FAST_BORROW         0 (envelope)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3000, file "app/routes/operator_brokerages.py", line 91>:
 91           RESUME                   0
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

Disassembly of <code object walk at 0x0000018C17CC1F60, file "app/routes/operator_brokerages.py", line 91>:
  --            COPY_FREE_VARS           1

  91            RESUME                   0

  92            NOP

  93    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      111 (to L16)
        L2:     NOT_TAKEN

  94    L3:     LOAD_FAST_BORROW         0 (obj)
                LOAD_ATTR                5 (items + NULL|self)
                CALL                     0
                GET_ITER
        L4:     FOR_ITER                88 (to L14)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   18 (k, v)

  95            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (k)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       42 (to L10)
                NOT_TAKEN

  96            LOAD_FAST_BORROW         1 (k)
                LOAD_ATTR                9 (lower + NULL|self)
                CALL                     0
                STORE_FAST               3 (kl)

  97            LOAD_GLOBAL             10 (_FORBIDDEN_RESPONSE_TOKENS)
                GET_ITER
        L5:     FOR_ITER                15 (to L9)
                STORE_FAST               4 (tok)

  98            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, kl)
                CONTAINS_OP              0 (in)
        L6:     POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L5)

  99    L7:     LOAD_FAST_BORROW         4 (tok)
                SWAP                     2
                POP_TOP
                SWAP                     2
                POP_TOP
        L8:     RETURN_VALUE

  97    L9:     END_FOR
                POP_ITER

 100   L10:     LOAD_DEREF               6 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                STORE_FAST               5 (sub)

 101            LOAD_FAST_BORROW         5 (sub)
                TO_BOOL
       L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           86 (to L4)

 102   L12:     LOAD_FAST_BORROW         5 (sub)
                SWAP                     2
                POP_TOP
       L13:     RETURN_VALUE

  94   L14:     END_FOR
                POP_ITER

 110   L15:     LOAD_CONST               0 (None)
                RETURN_VALUE

 103   L16:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL             12 (list)
                LOAD_GLOBAL             14 (tuple)
                BUILD_TUPLE              2
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       30 (to L22)
                NOT_TAKEN

 104            LOAD_FAST_BORROW         0 (obj)
                GET_ITER
       L17:     FOR_ITER                23 (to L21)
                STORE_FAST               2 (v)

 105            LOAD_DEREF               6 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                STORE_FAST               5 (sub)

 106            LOAD_FAST_BORROW         5 (sub)
                TO_BOOL
       L18:     POP_JUMP_IF_TRUE         3 (to L19)
                NOT_TAKEN
                JUMP_BACKWARD           21 (to L17)

 107   L19:     LOAD_FAST_BORROW         5 (sub)
                SWAP                     2
                POP_TOP
       L20:     RETURN_VALUE

 104   L21:     END_FOR
                POP_ITER

 110   L22:     LOAD_CONST               0 (None)
                RETURN_VALUE

  --   L23:     PUSH_EXC_INFO

 108            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L25)
                NOT_TAKEN
                POP_TOP

 109   L24:     POP_EXCEPT
                LOAD_CONST               0 (None)
                RETURN_VALUE

 108   L25:     RERAISE                  0

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

Disassembly of <code object __annotate__ at 0x0000018C18025730, file "app/routes/operator_brokerages.py", line 114>:
114           RESUME                   0
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

Disassembly of <code object _final_envelope at 0x0000018C17FE1680, file "app/routes/operator_brokerages.py", line 114>:
114           RESUME                   0

115           LOAD_GLOBAL              1 (_scan_for_forbidden + NULL)
              LOAD_FAST_BORROW         0 (env)
              CALL                     1
              STORE_FAST               2 (leak)

116           LOAD_FAST_BORROW         2 (leak)
              TO_BOOL
              POP_JUMP_IF_FALSE       37 (to L1)
              NOT_TAKEN

117           LOAD_GLOBAL              2 (logger)
              LOAD_ATTR                5 (warning + NULL|self)

118           LOAD_CONST               0 ('operator_brokerages surface=')
              LOAD_FAST_BORROW         1 (surface)
              FORMAT_SIMPLE
              LOAD_CONST               1 (' collapsed — forbidden token leaked')
              BUILD_STRING             3

117           CALL                     1
              POP_TOP

122           LOAD_CONST               2 ('status')
              LOAD_CONST               3 ('failed')

123           LOAD_CONST               4 ('surface')
              LOAD_FAST_BORROW         1 (surface)

124           LOAD_CONST               5 ('error_code')
              LOAD_CONST               6 ('ops_envelope_forbidden_token')

125           LOAD_CONST               7 ('warnings')
              LOAD_CONST               6 ('ops_envelope_forbidden_token')
              BUILD_LIST               1

121           BUILD_MAP                4
              RETURN_VALUE

127   L1:     LOAD_FAST_BORROW         0 (env)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "app/routes/operator_brokerages.py", line 130>:
130           RESUME                   0
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

Disassembly of <code object _safe_brokerage at 0x0000018C17F96420, file "app/routes/operator_brokerages.py", line 130>:
130           RESUME                   0

131           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

132           LOAD_CONST               0 (None)
              RETURN_VALUE

133   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

134           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

135           LOAD_CONST               0 (None)
              RETURN_VALUE

136   L2:     LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         1 (s)
              CALL                     1
              LOAD_GLOBAL              8 (_BROKERAGE_ID_MAX_LEN)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

137           LOAD_CONST               0 (None)
              RETURN_VALUE

138   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025D30, file "app/routes/operator_brokerages.py", line 141>:
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

Disassembly of <code object _clamp_int at 0x0000018C18038DF0, file "app/routes/operator_brokerages.py", line 141>:
 141           RESUME                   0

 142           NOP

 143   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               4 (v)

 146   L2:     LOAD_FAST_LOAD_FAST     65 (v, lo)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 147           LOAD_FAST                1 (lo)
               RETURN_VALUE

 148   L3:     LOAD_FAST_LOAD_FAST     66 (v, hi)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN

 149           LOAD_FAST                2 (hi)
               RETURN_VALUE

 150   L4:     LOAD_FAST                4 (v)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 144           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L7)
               NOT_TAKEN
               POP_TOP

 145           LOAD_FAST                3 (default)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

 144   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025530, file "app/routes/operator_brokerages.py", line 158>:
158           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('onboarding_status')

159           LOAD_CONST               2 ('Optional[str]')

158           LOAD_CONST               3 ('pilot_stage')

160           LOAD_CONST               2 ('Optional[str]')

158           LOAD_CONST               4 ('limit')

161           LOAD_CONST               5 ('int')

158           LOAD_CONST               6 ('return')

163           LOAD_CONST               7 ('Dict[str, Any]')

158           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object list_brokerages_route at 0x0000018C17D77E00, file "app/routes/operator_brokerages.py", line 157>:
 157            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 167            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('list_profiles',))
                IMPORT_NAME              0 (app.services.brokerage.profile_service)
                IMPORT_FROM              1 (list_profiles)
                STORE_FAST               4 (list_profiles)
                POP_TOP

 168            LOAD_GLOBAL              5 (_clamp_int + NULL)
                LOAD_FAST_BORROW         2 (limit)
                LOAD_SMALL_INT           1
                LOAD_GLOBAL              6 (_LIST_LIMIT_MAX)
                LOAD_GLOBAL              8 (_LIST_LIMIT_DEFAULT)
                CALL                     4
                STORE_FAST               5 (capped_limit)

 169    L2:     NOP

 170    L3:     LOAD_FAST_BORROW         4 (list_profiles)
                PUSH_NULL

 171            LOAD_FAST_BORROW         0 (onboarding_status)

 172            LOAD_FAST_BORROW         1 (pilot_stage)

 173            LOAD_FAST_BORROW         5 (capped_limit)

 170            LOAD_CONST               2 (('filter_status', 'filter_stage', 'limit'))
                CALL_KW                  3
                STORE_FAST               6 (report)

 176            LOAD_CONST               3 ('status')
                LOAD_FAST_BORROW         6 (report)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               3 ('status')
                CALL                     1

 177            LOAD_CONST               4 ('surface')
                LOAD_CONST               5 ('ops.brokerages.list')

 178            LOAD_CONST               6 ('list')
                LOAD_FAST_BORROW         6 (report)

 175            BUILD_MAP                3
                STORE_FAST               7 (env)

 190    L4:     LOAD_GLOBAL             23 (_final_envelope + NULL)
                LOAD_FAST_BORROW         7 (env)
                LOAD_CONST               5 ('ops.brokerages.list')
                LOAD_CONST              13 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --    L5:     PUSH_EXC_INFO

 180            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L9)
                NOT_TAKEN
                STORE_FAST               8 (e)

 181    L6:     LOAD_GLOBAL             14 (logger)
                LOAD_ATTR               17 (warning + NULL|self)

 182            LOAD_CONST               7 ('operator_brokerages list error type=')
                LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 181            CALL                     1
                POP_TOP

 185            LOAD_CONST               3 ('status')
                LOAD_CONST               8 ('failed')

 186            LOAD_CONST               4 ('surface')
                LOAD_CONST               5 ('ops.brokerages.list')

 187            LOAD_CONST               9 ('error_code')
                LOAD_CONST              10 ('unexpected:')
                LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 188            LOAD_CONST              11 ('warnings')
                BUILD_LIST               0

 184            BUILD_MAP                4
                STORE_FAST               7 (env)
        L7:     POP_EXCEPT
                LOAD_CONST              12 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                JUMP_BACKWARD_NO_INTERRUPT 104 (to L4)

  --    L8:     LOAD_CONST              12 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RERAISE                  1

 180    L9:     RERAISE                  0

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

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "app/routes/operator_brokerages.py", line 194>:
194           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

195           LOAD_CONST               2 ('str')

194           LOAD_CONST               3 ('return')

197           LOAD_CONST               4 ('Dict[str, Any]')

194           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object get_brokerage_route at 0x0000018C17CD4970, file "app/routes/operator_brokerages.py", line 193>:
 193            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 198            LOAD_GLOBAL              1 (_safe_brokerage + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                STORE_FAST               2 (bid)

 199            LOAD_FAST_BORROW         2 (bid)
                POP_JUMP_IF_NOT_NONE    14 (to L2)
                NOT_TAKEN

 200            LOAD_GLOBAL              3 (HTTPException + NULL)
                LOAD_CONST               1 (400)
                LOAD_CONST               2 ('invalid brokerage_id')
                LOAD_CONST               3 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

 201    L2:     LOAD_SMALL_INT           0
                LOAD_CONST               4 (('get_profile',))
                IMPORT_NAME              2 (app.services.brokerage.profile_service)
                IMPORT_FROM              3 (get_profile)
                STORE_FAST               3 (get_profile)
                POP_TOP

 202    L3:     NOP

 203    L4:     LOAD_FAST_BORROW         3 (get_profile)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (bid)
                CALL                     1
                STORE_FAST               4 (report)

 205            LOAD_CONST               5 ('status')
                LOAD_FAST_BORROW         4 (report)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               5 ('status')
                CALL                     1

 206            LOAD_CONST               6 ('surface')
                LOAD_CONST               7 ('ops.brokerages.get')

 207            LOAD_CONST               8 ('profile')
                LOAD_FAST_BORROW         4 (report)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               8 ('profile')
                CALL                     1

 208            LOAD_CONST               9 ('warnings')
                LOAD_FAST_BORROW         4 (report)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               9 ('warnings')
                CALL                     1

 209            LOAD_CONST              10 ('error_code')
                LOAD_FAST_BORROW         4 (report)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              10 ('error_code')
                CALL                     1

 204            BUILD_MAP                5
                STORE_FAST               5 (env)

 221    L5:     LOAD_GLOBAL             21 (_final_envelope + NULL)
                LOAD_FAST_BORROW         5 (env)
                LOAD_CONST               7 ('ops.brokerages.get')
                LOAD_CONST              14 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --    L6:     PUSH_EXC_INFO

 211            LOAD_GLOBAL             10 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L10)
                NOT_TAKEN
                STORE_FAST               6 (e)

 212    L7:     LOAD_GLOBAL             12 (logger)
                LOAD_ATTR               15 (warning + NULL|self)

 213            LOAD_CONST              11 ('operator_brokerages get error type=')
                LOAD_GLOBAL             17 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               18 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 212            CALL                     1
                POP_TOP

 216            LOAD_CONST               5 ('status')
                LOAD_CONST              12 ('failed')

 217            LOAD_CONST               6 ('surface')
                LOAD_CONST               7 ('ops.brokerages.get')

 218            LOAD_CONST              10 ('error_code')
                LOAD_CONST              13 ('unexpected:')
                LOAD_GLOBAL             17 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               18 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 219            LOAD_CONST               9 ('warnings')
                BUILD_LIST               0

 215            BUILD_MAP                4
                STORE_FAST               5 (env)
        L8:     POP_EXCEPT
                LOAD_CONST               0 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                JUMP_BACKWARD_NO_INTERRUPT 104 (to L5)

  --    L9:     LOAD_CONST               0 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

 211   L10:     RERAISE                  0

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

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "app/routes/operator_brokerages.py", line 225>:
225           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

226           LOAD_CONST               2 ('str')

225           LOAD_CONST               3 ('return')

228           LOAD_CONST               4 ('Dict[str, Any]')

225           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object get_brokerage_health at 0x0000018C17E94C50, file "app/routes/operator_brokerages.py", line 224>:
 224            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 232            LOAD_GLOBAL              1 (_safe_brokerage + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                STORE_FAST               2 (bid)

 233            LOAD_FAST_BORROW         2 (bid)
                POP_JUMP_IF_NOT_NONE    14 (to L2)
                NOT_TAKEN

 234            LOAD_GLOBAL              3 (HTTPException + NULL)
                LOAD_CONST               2 (400)
                LOAD_CONST               3 ('invalid brokerage_id')
                LOAD_CONST               4 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

 235    L2:     LOAD_SMALL_INT           0
                LOAD_CONST               5 (('get_brokerage_by_id',))
                IMPORT_NAME              2 (app.db.brokerage_store)
                IMPORT_FROM              3 (get_brokerage_by_id)
                STORE_FAST               3 (get_brokerage_by_id)
                POP_TOP

 236            LOAD_SMALL_INT           0
                LOAD_CONST               6 (('get_profile',))
                IMPORT_NAME              4 (app.services.brokerage.profile_service)
                IMPORT_FROM              5 (get_profile)
                STORE_FAST               4 (get_profile)
                POP_TOP

 237            LOAD_SMALL_INT           0
                LOAD_CONST               7 (('configuration_warning_report',))
                IMPORT_NAME              6 (app.services.brokerage.config_validator)
                IMPORT_FROM              7 (configuration_warning_report)
                STORE_FAST               5 (configuration_warning_report)
                POP_TOP

 240            LOAD_SMALL_INT           0
                LOAD_CONST               8 (('queue_status_report',))
                IMPORT_NAME              8 (app.services.ingestion.pending_call_recovery)
                IMPORT_FROM              9 (queue_status_report)
                STORE_FAST               6 (queue_status_report)
                POP_TOP

 243            LOAD_SMALL_INT           0
                LOAD_CONST               9 (('heartbeat_monitor_report',))
                IMPORT_NAME             10 (app.services.worker.heartbeat_monitor)
                IMPORT_FROM             11 (heartbeat_monitor_report)
                STORE_FAST               7 (heartbeat_monitor_report)
                POP_TOP

 246    L3:     NOP

 247            NOP

 248    L4:     LOAD_FAST_BORROW         3 (get_brokerage_by_id)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (bid)
                CALL                     1
                STORE_FAST               8 (brokerage)

 255    L5:     LOAD_FAST_BORROW         4 (get_profile)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (bid)
                CALL                     1
                STORE_FAST              10 (profile_env)

 256            LOAD_GLOBAL             35 (isinstance + NULL)
                LOAD_FAST_BORROW        10 (profile_env)
                LOAD_GLOBAL             36 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L6)
                NOT_TAKEN
                LOAD_FAST_BORROW        10 (profile_env)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST              14 ('profile')
                CALL                     1
                JUMP_FORWARD             1 (to L7)
        L6:     LOAD_CONST               1 (None)
        L7:     STORE_FAST              11 (profile)

 257            LOAD_FAST_BORROW         5 (configuration_warning_report)
                PUSH_NULL
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 139 (brokerage, profile)
                LOAD_CONST              15 (('profile',))
                CALL_KW                  2
                STORE_FAST              12 (config)

 258            LOAD_FAST_BORROW         6 (queue_status_report)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (bid)
                LOAD_CONST              16 (('brokerage_id',))
                CALL_KW                  1
                STORE_FAST              13 (queue)

 259            LOAD_FAST_BORROW         7 (heartbeat_monitor_report)
                PUSH_NULL
                LOAD_SMALL_INT          50
                LOAD_CONST              17 (('limit',))
                CALL_KW                  1
                STORE_FAST              14 (hb)

 261            LOAD_CONST              18 ('status')
                LOAD_CONST              19 ('ok')

 262            LOAD_CONST              20 ('surface')
                LOAD_CONST              21 ('ops.brokerages.health')

 263            LOAD_CONST              14 ('profile')
                LOAD_FAST_BORROW        11 (profile)

 264            LOAD_CONST              22 ('config')

 265            LOAD_CONST              18 ('status')
                LOAD_FAST_BORROW        12 (config)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST              18 ('status')
                CALL                     1

 266            LOAD_CONST              23 ('warnings')
                LOAD_FAST_BORROW        12 (config)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST              23 ('warnings')
                BUILD_LIST               0
                CALL                     2

 267            LOAD_CONST              24 ('errors')
                LOAD_FAST_BORROW        12 (config)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST              24 ('errors')
                BUILD_LIST               0
                CALL                     2

 268            LOAD_CONST              25 ('warning_count')
                LOAD_FAST_BORROW        12 (config)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST              25 ('warning_count')
                LOAD_SMALL_INT           0
                CALL                     2

 269            LOAD_CONST              26 ('error_count')
                LOAD_FAST_BORROW        12 (config)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST              26 ('error_count')
                LOAD_SMALL_INT           0
                CALL                     2

 264            BUILD_MAP                5

 271            LOAD_CONST              27 ('queue')

 272            LOAD_CONST              18 ('status')
                LOAD_FAST_BORROW        13 (queue)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST              18 ('status')
                CALL                     1

 273            LOAD_CONST              28 ('total')
                LOAD_FAST_BORROW        13 (queue)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST              28 ('total')
                LOAD_SMALL_INT           0
                CALL                     2

 274            LOAD_CONST              29 ('by_status')
                LOAD_FAST_BORROW        13 (queue)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST              29 ('by_status')
                BUILD_MAP                0
                CALL                     2

 275            LOAD_CONST              30 ('oldest_age_seconds')
                LOAD_FAST_BORROW        13 (queue)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST              30 ('oldest_age_seconds')
                CALL                     1

 271            BUILD_MAP                4

 277            LOAD_CONST              31 ('heartbeat')

 278            LOAD_CONST              18 ('status')
                LOAD_FAST_BORROW        14 (hb)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST              18 ('status')
                CALL                     1

 279            LOAD_CONST              28 ('total')
                LOAD_FAST_BORROW        14 (hb)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST              28 ('total')
                LOAD_SMALL_INT           0
                CALL                     2

 280            LOAD_CONST              29 ('by_status')
                LOAD_FAST_BORROW        14 (hb)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST              29 ('by_status')
                BUILD_MAP                0
                CALL                     2

 281            LOAD_CONST              30 ('oldest_age_seconds')
                LOAD_FAST_BORROW        14 (hb)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST              30 ('oldest_age_seconds')
                CALL                     1

 277            BUILD_MAP                4

 260            BUILD_MAP                6
                STORE_FAST              15 (env)

 294    L8:     LOAD_GLOBAL             41 (_final_envelope + NULL)
                LOAD_FAST_BORROW        15 (env)
                LOAD_CONST              21 ('ops.brokerages.health')
                LOAD_CONST              36 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --    L9:     PUSH_EXC_INFO

 249            LOAD_GLOBAL             24 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L13)
                NOT_TAKEN
                STORE_FAST               9 (e)

 250   L10:     LOAD_GLOBAL             26 (logger)
                LOAD_ATTR               29 (warning + NULL|self)

 251            LOAD_CONST              10 ('get_brokerage_health brokerage read error type=')

 252            LOAD_GLOBAL             31 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               32 (__name__)
                FORMAT_SIMPLE

 251            BUILD_STRING             2

 250            CALL                     1
                POP_TOP

 254            LOAD_CONST              11 ('id')
                LOAD_FAST                2 (bid)
                LOAD_CONST              12 ('active')
                LOAD_CONST              13 (False)
                BUILD_MAP                2
                STORE_FAST               8 (brokerage)
       L11:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 398 (to L5)

  --   L12:     LOAD_CONST               1 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RERAISE                  1

 249   L13:     RERAISE                  0

  --   L14:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L15:     PUSH_EXC_INFO

 284            LOAD_GLOBAL             24 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L19)
                NOT_TAKEN
                STORE_FAST               9 (e)

 285   L16:     LOAD_GLOBAL             26 (logger)
                LOAD_ATTR               29 (warning + NULL|self)

 286            LOAD_CONST              32 ('operator_brokerages health error type=')
                LOAD_GLOBAL             31 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               32 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 285            CALL                     1
                POP_TOP

 289            LOAD_CONST              18 ('status')
                LOAD_CONST              33 ('failed')

 290            LOAD_CONST              20 ('surface')
                LOAD_CONST              21 ('ops.brokerages.health')

 291            LOAD_CONST              34 ('error_code')
                LOAD_CONST              35 ('unexpected:')
                LOAD_GLOBAL             31 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               32 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 292            LOAD_CONST              23 ('warnings')
                BUILD_LIST               0

 288            BUILD_MAP                4
                STORE_FAST              15 (env)
       L17:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                JUMP_BACKWARD_NO_INTERRUPT 178 (to L8)

  --   L18:     LOAD_CONST               1 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RERAISE                  1

 284   L19:     RERAISE                  0

  --   L20:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L21:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L3 -> L21 [0] lasti
  L4 to L5 -> L9 [0]
  L5 to L8 -> L15 [0]
  L8 to L9 -> L21 [0] lasti
  L9 to L10 -> L14 [1] lasti
  L10 to L11 -> L12 [1] lasti
  L11 to L12 -> L15 [0]
  L12 to L14 -> L14 [1] lasti
  L14 to L15 -> L15 [0]
  L15 to L16 -> L20 [1] lasti
  L16 to L17 -> L18 [1] lasti
  L17 to L18 -> L21 [0] lasti
  L18 to L20 -> L20 [1] lasti
  L20 to L21 -> L21 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025130, file "app/routes/operator_brokerages.py", line 298>:
298           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

299           LOAD_CONST               2 ('str')

298           LOAD_CONST               3 ('required_pilot_stage')

300           LOAD_CONST               4 ('Optional[str]')

298           LOAD_CONST               5 ('return')

302           LOAD_CONST               6 ('Dict[str, Any]')

298           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object get_launch_readiness at 0x0000018C17E951B0, file "app/routes/operator_brokerages.py", line 297>:
 297            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 303            LOAD_GLOBAL              1 (_safe_brokerage + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                STORE_FAST               3 (bid)

 304            LOAD_FAST_BORROW         3 (bid)
                POP_JUMP_IF_NOT_NONE    14 (to L2)
                NOT_TAKEN

 305            LOAD_GLOBAL              3 (HTTPException + NULL)
                LOAD_CONST               1 (400)
                LOAD_CONST               2 ('invalid brokerage_id')
                LOAD_CONST               3 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

 306    L2:     LOAD_SMALL_INT           0
                LOAD_CONST               4 (('get_brokerage_by_id',))
                IMPORT_NAME              2 (app.db.brokerage_store)
                IMPORT_FROM              3 (get_brokerage_by_id)
                STORE_FAST               4 (get_brokerage_by_id)
                POP_TOP

 307            LOAD_SMALL_INT           0
                LOAD_CONST               5 (('get_profile',))
                IMPORT_NAME              4 (app.services.brokerage.profile_service)
                IMPORT_FROM              5 (get_profile)
                STORE_FAST               5 (get_profile)
                POP_TOP

 308            LOAD_SMALL_INT           0
                LOAD_CONST               6 (('validate_brokerage_launch_ready',))
                IMPORT_NAME              6 (app.services.brokerage.config_validator)
                IMPORT_FROM              7 (validate_brokerage_launch_ready)
                STORE_FAST               6 (validate_brokerage_launch_ready)
                POP_TOP

 311    L3:     NOP

 312            NOP

 313    L4:     LOAD_FAST_BORROW         4 (get_brokerage_by_id)
                PUSH_NULL
                LOAD_FAST_BORROW         3 (bid)
                CALL                     1
                STORE_FAST               7 (brokerage)

 320    L5:     LOAD_FAST_BORROW         5 (get_profile)
                PUSH_NULL
                LOAD_FAST_BORROW         3 (bid)
                CALL                     1
                STORE_FAST               9 (profile_env)

 321            LOAD_GLOBAL             27 (isinstance + NULL)
                LOAD_FAST_BORROW         9 (profile_env)
                LOAD_GLOBAL             28 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L6)
                NOT_TAKEN
                LOAD_FAST_BORROW         9 (profile_env)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST              11 ('profile')
                CALL                     1
                JUMP_FORWARD             1 (to L7)
        L6:     LOAD_CONST               0 (None)
        L7:     STORE_FAST              10 (profile)

 322            LOAD_FAST_BORROW         6 (validate_brokerage_launch_ready)
                PUSH_NULL

 323            LOAD_FAST_BORROW_LOAD_FAST_BORROW 122 (brokerage, profile)

 324            LOAD_FAST_BORROW         1 (required_pilot_stage)

 322            LOAD_CONST              12 (('profile', 'required_pilot_stage'))
                CALL_KW                  3
                STORE_FAST              11 (result)

 327            LOAD_CONST              13 ('status')
                LOAD_CONST              14 ('ok')

 328            LOAD_CONST              15 ('surface')
                LOAD_CONST              16 ('ops.brokerages.launch_readiness')

 329            LOAD_CONST              17 ('launch_ready')
                LOAD_GLOBAL             33 (bool + NULL)
                LOAD_FAST_BORROW        11 (result)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST              17 ('launch_ready')
                CALL                     1
                CALL                     1

 330            LOAD_CONST              18 ('warnings')
                LOAD_FAST_BORROW        11 (result)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST              18 ('warnings')
                BUILD_LIST               0
                CALL                     2

 331            LOAD_CONST              19 ('errors')
                LOAD_FAST_BORROW        11 (result)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST              19 ('errors')
                BUILD_LIST               0
                CALL                     2

 332            LOAD_CONST              20 ('warning_count')
                LOAD_FAST_BORROW        11 (result)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST              20 ('warning_count')
                LOAD_SMALL_INT           0
                CALL                     2

 333            LOAD_CONST              21 ('error_count')
                LOAD_FAST_BORROW        11 (result)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST              21 ('error_count')
                LOAD_SMALL_INT           0
                CALL                     2

 334            LOAD_CONST              22 ('profile_present')
                LOAD_FAST_BORROW        10 (profile)
                LOAD_CONST               0 (None)
                IS_OP                    1 (is not)

 326            BUILD_MAP                8
                STORE_FAST              12 (env)

 347    L8:     LOAD_GLOBAL             35 (_final_envelope + NULL)
                LOAD_FAST_BORROW        12 (env)
                LOAD_CONST              16 ('ops.brokerages.launch_readiness')
                LOAD_CONST              27 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --    L9:     PUSH_EXC_INFO

 314            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       60 (to L13)
                NOT_TAKEN
                STORE_FAST               8 (e)

 315   L10:     LOAD_GLOBAL             18 (logger)
                LOAD_ATTR               21 (warning + NULL|self)

 316            LOAD_CONST               7 ('get_launch_readiness brokerage read error type=')

 317            LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE

 316            BUILD_STRING             2

 315            CALL                     1
                POP_TOP

 319            LOAD_CONST               8 ('id')
                LOAD_FAST                3 (bid)
                LOAD_CONST               9 ('active')
                LOAD_CONST              10 (False)
                BUILD_MAP                2
                STORE_FAST               7 (brokerage)
       L11:     POP_EXCEPT
                LOAD_CONST               0 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                JUMP_BACKWARD_NO_INTERRUPT 245 (to L5)

  --   L12:     LOAD_CONST               0 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RERAISE                  1

 314   L13:     RERAISE                  0

  --   L14:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L15:     PUSH_EXC_INFO

 336            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L19)
                NOT_TAKEN
                STORE_FAST               8 (e)

 337   L16:     LOAD_GLOBAL             18 (logger)
                LOAD_ATTR               21 (warning + NULL|self)

 338            LOAD_CONST              23 ('operator_brokerages launch_readiness error type=')

 339            LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE

 338            BUILD_STRING             2

 337            CALL                     1
                POP_TOP

 342            LOAD_CONST              13 ('status')
                LOAD_CONST              24 ('failed')

 343            LOAD_CONST              15 ('surface')
                LOAD_CONST              16 ('ops.brokerages.launch_readiness')

 344            LOAD_CONST              25 ('error_code')
                LOAD_CONST              26 ('unexpected:')
                LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 345            LOAD_CONST              18 ('warnings')
                BUILD_LIST               0

 341            BUILD_MAP                4
                STORE_FAST              12 (env)
       L17:     POP_EXCEPT
                LOAD_CONST               0 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                JUMP_BACKWARD_NO_INTERRUPT 177 (to L8)

  --   L18:     LOAD_CONST               0 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RERAISE                  1

 336   L19:     RERAISE                  0

  --   L20:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L21:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L3 -> L21 [0] lasti
  L4 to L5 -> L9 [0]
  L5 to L8 -> L15 [0]
  L8 to L9 -> L21 [0] lasti
  L9 to L10 -> L14 [1] lasti
  L10 to L11 -> L12 [1] lasti
  L11 to L12 -> L15 [0]
  L12 to L14 -> L14 [1] lasti
  L14 to L15 -> L15 [0]
  L15 to L16 -> L20 [1] lasti
  L16 to L17 -> L18 [1] lasti
  L17 to L18 -> L21 [0] lasti
  L18 to L20 -> L20 [1] lasti
  L20 to L21 -> L21 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024930, file "app/routes/operator_brokerages.py", line 351>:
351           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

352           LOAD_CONST               2 ('str')

351           LOAD_CONST               3 ('template')

353           LOAD_CONST               2 ('str')

351           LOAD_CONST               4 ('return')

355           LOAD_CONST               5 ('Dict[str, Any]')

351           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object get_onboarding_checklist at 0x0000018C17E955D0, file "app/routes/operator_brokerages.py", line 350>:
 350            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 356            LOAD_GLOBAL              1 (_safe_brokerage + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                STORE_FAST               3 (bid)

 357            LOAD_FAST_BORROW         3 (bid)
                POP_JUMP_IF_NOT_NONE    14 (to L2)
                NOT_TAKEN

 358            LOAD_GLOBAL              3 (HTTPException + NULL)
                LOAD_CONST               1 (400)
                LOAD_CONST               2 ('invalid brokerage_id')
                LOAD_CONST               3 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

 359    L2:     LOAD_SMALL_INT           0
                LOAD_CONST               4 (('brokerage_onboarding_checklist', 'launch_checklist', 'rollback_checklist', 'smoke_test_template', 'pilot_expansion_checklist'))
                IMPORT_NAME              2 (app.services.brokerage.onboarding_templates)
                IMPORT_FROM              3 (brokerage_onboarding_checklist)
                STORE_FAST               4 (brokerage_onboarding_checklist)
                IMPORT_FROM              4 (launch_checklist)
                STORE_FAST               5 (launch_checklist)
                IMPORT_FROM              5 (rollback_checklist)
                STORE_FAST               6 (rollback_checklist)
                IMPORT_FROM              6 (smoke_test_template)
                STORE_FAST               7 (smoke_test_template)
                IMPORT_FROM              7 (pilot_expansion_checklist)
                STORE_FAST               8 (pilot_expansion_checklist)
                POP_TOP

 367            LOAD_CONST               5 ('onboarding')
                LOAD_FAST_BORROW         4 (brokerage_onboarding_checklist)

 368            LOAD_CONST               6 ('launch')
                LOAD_FAST_BORROW         5 (launch_checklist)

 369            LOAD_CONST               7 ('rollback')
                LOAD_FAST_BORROW         6 (rollback_checklist)

 370            LOAD_CONST               8 ('smoke')
                LOAD_FAST_BORROW         7 (smoke_test_template)

 371            LOAD_CONST               9 ('pilot_expansion')
                LOAD_FAST_BORROW         8 (pilot_expansion_checklist)

 366            BUILD_MAP                5
                STORE_FAST               9 (mapping)

 373            LOAD_FAST_BORROW         9 (mapping)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_FAST_BORROW         1 (template)
                CALL                     1
                STORE_FAST              10 (fn)

 374            LOAD_FAST_BORROW        10 (fn)
                POP_JUMP_IF_NOT_NONE    22 (to L3)
                NOT_TAKEN

 375            LOAD_GLOBAL             19 (_final_envelope + NULL)

 376            LOAD_CONST              10 ('status')
                LOAD_CONST              11 ('failed')

 377            LOAD_CONST              12 ('surface')
                LOAD_CONST              13 ('ops.brokerages.onboarding_checklist')

 378            LOAD_CONST              14 ('error_code')
                LOAD_CONST              15 ('invalid_template')

 379            LOAD_CONST              16 ('warnings')
                BUILD_LIST               0

 375            BUILD_MAP                4

 380            LOAD_CONST              13 ('ops.brokerages.onboarding_checklist')

 375            LOAD_CONST              17 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

 381    L3:     NOP

 382    L4:     LOAD_FAST_BORROW        10 (fn)
                PUSH_NULL
                LOAD_FAST_BORROW         3 (bid)
                LOAD_CONST              18 (('brokerage_id',))
                CALL_KW                  1
                STORE_FAST              11 (payload)

 384            LOAD_CONST              10 ('status')
                LOAD_CONST              19 ('ok')

 385            LOAD_CONST              12 ('surface')
                LOAD_CONST              13 ('ops.brokerages.onboarding_checklist')

 386            LOAD_CONST              20 ('template')
                LOAD_FAST_BORROW         1 (template)

 387            LOAD_CONST              21 ('checklist')
                LOAD_FAST_BORROW        11 (payload)

 383            BUILD_MAP                4
                STORE_FAST              12 (env)

 400    L5:     LOAD_GLOBAL             19 (_final_envelope + NULL)
                LOAD_FAST_BORROW        12 (env)
                LOAD_CONST              13 ('ops.brokerages.onboarding_checklist')
                LOAD_CONST              17 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --    L6:     PUSH_EXC_INFO

 389            LOAD_GLOBAL             20 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L10)
                NOT_TAKEN
                STORE_FAST              13 (e)

 390    L7:     LOAD_GLOBAL             22 (logger)
                LOAD_ATTR               25 (warning + NULL|self)

 391            LOAD_CONST              22 ('operator_brokerages onboarding_checklist error type=')

 392            LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST               13 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE

 391            BUILD_STRING             2

 390            CALL                     1
                POP_TOP

 395            LOAD_CONST              10 ('status')
                LOAD_CONST              11 ('failed')

 396            LOAD_CONST              12 ('surface')
                LOAD_CONST              13 ('ops.brokerages.onboarding_checklist')

 397            LOAD_CONST              14 ('error_code')
                LOAD_CONST              23 ('unexpected:')
                LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST               13 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 398            LOAD_CONST              16 ('warnings')
                BUILD_LIST               0

 394            BUILD_MAP                4
                STORE_FAST              12 (env)
        L8:     POP_EXCEPT
                LOAD_CONST               0 (None)
                STORE_FAST              13 (e)
                DELETE_FAST             13 (e)
                JUMP_BACKWARD_NO_INTERRUPT 104 (to L5)

  --    L9:     LOAD_CONST               0 (None)
                STORE_FAST              13 (e)
                DELETE_FAST             13 (e)
                RERAISE                  1

 389   L10:     RERAISE                  0

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

Disassembly of <code object __annotate__ at 0x0000018C17FA1D40, file "app/routes/operator_brokerages.py", line 404>:
404           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

405           LOAD_CONST               2 ('str')

404           LOAD_CONST               3 ('return')

407           LOAD_CONST               4 ('Dict[str, Any]')

404           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object get_brokerage_audit_chain_status at 0x0000018C17D51290, file "app/routes/operator_brokerages.py", line 403>:
 403            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 411            LOAD_GLOBAL              1 (_safe_brokerage + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                STORE_FAST               2 (bid)

 412            LOAD_FAST_BORROW         2 (bid)
                POP_JUMP_IF_NOT_NONE    14 (to L2)
                NOT_TAKEN

 413            LOAD_GLOBAL              3 (HTTPException + NULL)
                LOAD_CONST               2 (400)
                LOAD_CONST               3 ('invalid brokerage_id')
                LOAD_CONST               4 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

 414    L2:     LOAD_SMALL_INT           0
                LOAD_CONST               5 (('brokerage_chain_badge', 'chain_status_report'))
                IMPORT_NAME              2 (app.services.operator.audit_window_chain)
                IMPORT_FROM              3 (brokerage_chain_badge)
                STORE_FAST               3 (brokerage_chain_badge)
                IMPORT_FROM              4 (chain_status_report)
                STORE_FAST               4 (chain_status_report)
                POP_TOP

 418    L3:     NOP

 419    L4:     LOAD_FAST_BORROW         3 (brokerage_chain_badge)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (bid)
                CALL                     1
                STORE_FAST               5 (badge)

 420            LOAD_FAST_BORROW         4 (chain_status_report)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (bid)
                LOAD_SMALL_INT          50
                LOAD_CONST               6 (('brokerage_id', 'limit'))
                CALL_KW                  2
                STORE_FAST               6 (report)

 422            LOAD_CONST               7 ('status')
                LOAD_FAST_BORROW         5 (badge)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               7 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
        L5:     NOT_TAKEN
        L6:     POP_TOP
                LOAD_CONST               8 ('skipped')

 423    L7:     LOAD_CONST               9 ('surface')
                LOAD_CONST              10 ('ops.brokerages.audit_chain_status')

 424            LOAD_CONST              11 ('badge')
                LOAD_FAST                5 (badge)

 425            LOAD_CONST              12 ('summary')

 426            LOAD_CONST              13 ('total')
                LOAD_FAST_BORROW         6 (report)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              13 ('total')
                LOAD_SMALL_INT           0
                CALL                     2

 427            LOAD_CONST              14 ('by_status')
                LOAD_FAST_BORROW         6 (report)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              14 ('by_status')
                BUILD_MAP                0
                CALL                     2

 428            LOAD_CONST              15 ('latest_entry')
                LOAD_FAST_BORROW         6 (report)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              15 ('latest_entry')
                CALL                     1

 425            BUILD_MAP                3

 430            LOAD_CONST              16 ('warnings')
                LOAD_GLOBAL             13 (list + NULL)
                LOAD_FAST_BORROW         5 (badge)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              16 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
        L8:     NOT_TAKEN
        L9:     POP_TOP
                BUILD_LIST               0
       L10:     CALL                     1

 431            LOAD_CONST              17 ('error_code')
                LOAD_FAST_BORROW         5 (badge)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              17 ('error_code')
                CALL                     1

 421            BUILD_MAP                6
                STORE_FAST               7 (env)

 444   L11:     LOAD_GLOBAL             25 (_final_envelope + NULL)
                LOAD_FAST_BORROW         7 (env)
                LOAD_CONST              10 ('ops.brokerages.audit_chain_status')
                LOAD_CONST              21 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --   L12:     PUSH_EXC_INFO

 433            LOAD_GLOBAL             14 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L16)
                NOT_TAKEN
                STORE_FAST               8 (e)

 434   L13:     LOAD_GLOBAL             16 (logger)
                LOAD_ATTR               19 (warning + NULL|self)

 435            LOAD_CONST              18 ('operator_brokerages audit_chain_status error type=')

 436            LOAD_GLOBAL             21 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               22 (__name__)
                FORMAT_SIMPLE

 435            BUILD_STRING             2

 434            CALL                     1
                POP_TOP

 439            LOAD_CONST               7 ('status')
                LOAD_CONST              19 ('failed')

 440            LOAD_CONST               9 ('surface')
                LOAD_CONST              10 ('ops.brokerages.audit_chain_status')

 441            LOAD_CONST              17 ('error_code')
                LOAD_CONST              20 ('unexpected:')
                LOAD_GLOBAL             21 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               22 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 442            LOAD_CONST              16 ('warnings')
                BUILD_LIST               0

 438            BUILD_MAP                4
                STORE_FAST               7 (env)
       L14:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                JUMP_BACKWARD_NO_INTERRUPT 104 (to L11)

  --   L15:     LOAD_CONST               1 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RERAISE                  1

 433   L16:     RERAISE                  0

  --   L17:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L18:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L3 -> L18 [0] lasti
  L4 to L5 -> L12 [0]
  L6 to L8 -> L12 [0]
  L9 to L11 -> L12 [0]
  L11 to L12 -> L18 [0] lasti
  L12 to L13 -> L17 [1] lasti
  L13 to L14 -> L15 [1] lasti
  L14 to L15 -> L18 [0] lasti
  L15 to L17 -> L17 [1] lasti
  L17 to L18 -> L18 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026530, file "app/routes/operator_brokerages.py", line 448>:
448           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

449           LOAD_CONST               2 ('str')

448           LOAD_CONST               3 ('verification_type')

450           LOAD_CONST               4 ('Optional[str]')

448           LOAD_CONST               5 ('limit')

451           LOAD_CONST               6 ('int')

448           LOAD_CONST               7 ('return')

453           LOAD_CONST               8 ('Dict[str, Any]')

448           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object get_brokerage_verification_runs at 0x0000018C17D515E0, file "app/routes/operator_brokerages.py", line 447>:
 447            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 456            LOAD_GLOBAL              1 (_safe_brokerage + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                STORE_FAST               4 (bid)

 457            LOAD_FAST_BORROW         4 (bid)
                POP_JUMP_IF_NOT_NONE    14 (to L2)
                NOT_TAKEN

 458            LOAD_GLOBAL              3 (HTTPException + NULL)
                LOAD_CONST               2 (400)
                LOAD_CONST               3 ('invalid brokerage_id')
                LOAD_CONST               4 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

 459    L2:     LOAD_SMALL_INT           0
                LOAD_CONST               5 (('list_verification_runs', 'verification_run_summary'))
                IMPORT_NAME              2 (app.services.operator.audit_verification_runs)
                IMPORT_FROM              3 (list_verification_runs)
                STORE_FAST               5 (list_verification_runs)
                IMPORT_FROM              4 (verification_run_summary)
                STORE_FAST               6 (verification_run_summary)
                POP_TOP

 463            LOAD_GLOBAL             11 (_clamp_int + NULL)
                LOAD_FAST_BORROW         2 (limit)
                LOAD_SMALL_INT           1
                LOAD_GLOBAL             12 (_LIST_LIMIT_MAX)
                LOAD_GLOBAL             14 (_LIST_LIMIT_DEFAULT)
                CALL                     4
                STORE_FAST               7 (capped_limit)

 464    L3:     NOP

 465    L4:     LOAD_FAST_BORROW         5 (list_verification_runs)
                PUSH_NULL

 466            LOAD_FAST_BORROW         4 (bid)

 467            LOAD_FAST_BORROW         1 (verification_type)

 468            LOAD_FAST_BORROW         7 (capped_limit)

 465            LOAD_CONST               6 (('brokerage_id', 'verification_type', 'limit'))
                CALL_KW                  3
                STORE_FAST               8 (runs)

 470            LOAD_FAST_BORROW         6 (verification_run_summary)
                PUSH_NULL
                LOAD_FAST_BORROW         4 (bid)
                LOAD_CONST               7 (('brokerage_id',))
                CALL_KW                  1
                STORE_FAST               9 (summary)

 472            LOAD_CONST               8 ('status')
                LOAD_FAST_BORROW         8 (runs)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST               8 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
        L5:     NOT_TAKEN
        L6:     POP_TOP
                LOAD_CONST               9 ('skipped')

 473    L7:     LOAD_CONST              10 ('surface')
                LOAD_CONST              11 ('ops.brokerages.verification_runs')

 474            LOAD_CONST              12 ('runs')
                LOAD_FAST                8 (runs)

 475            LOAD_CONST              13 ('summary')

 476            LOAD_CONST              14 ('total')
                LOAD_FAST_BORROW         9 (summary)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              14 ('total')
                LOAD_SMALL_INT           0
                CALL                     2

 477            LOAD_CONST              15 ('by_status')
                LOAD_FAST_BORROW         9 (summary)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              15 ('by_status')
                BUILD_MAP                0
                CALL                     2

 478            LOAD_CONST              16 ('by_type')
                LOAD_FAST_BORROW         9 (summary)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              16 ('by_type')
                BUILD_MAP                0
                CALL                     2

 479            LOAD_CONST              17 ('latest_run')
                LOAD_FAST_BORROW         9 (summary)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              17 ('latest_run')
                CALL                     1

 475            BUILD_MAP                4

 481            LOAD_CONST              18 ('warnings')
                LOAD_GLOBAL             19 (list + NULL)
                LOAD_FAST_BORROW         8 (runs)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              18 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
        L8:     NOT_TAKEN
        L9:     POP_TOP
                BUILD_LIST               0
       L10:     CALL                     1

 482            LOAD_CONST              19 ('error_code')
                LOAD_FAST_BORROW         8 (runs)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              19 ('error_code')
                CALL                     1

 471            BUILD_MAP                6
                STORE_FAST              10 (env)

 495   L11:     LOAD_GLOBAL             31 (_final_envelope + NULL)
                LOAD_FAST_BORROW        10 (env)
                LOAD_CONST              11 ('ops.brokerages.verification_runs')
                LOAD_CONST              23 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --   L12:     PUSH_EXC_INFO

 484            LOAD_GLOBAL             20 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L16)
                NOT_TAKEN
                STORE_FAST              11 (e)

 485   L13:     LOAD_GLOBAL             22 (logger)
                LOAD_ATTR               25 (warning + NULL|self)

 486            LOAD_CONST              20 ('operator_brokerages verification_runs error type=')

 487            LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE

 486            BUILD_STRING             2

 485            CALL                     1
                POP_TOP

 490            LOAD_CONST               8 ('status')
                LOAD_CONST              21 ('failed')

 491            LOAD_CONST              10 ('surface')
                LOAD_CONST              11 ('ops.brokerages.verification_runs')

 492            LOAD_CONST              19 ('error_code')
                LOAD_CONST              22 ('unexpected:')
                LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 493            LOAD_CONST              18 ('warnings')
                BUILD_LIST               0

 489            BUILD_MAP                4
                STORE_FAST              10 (env)
       L14:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                JUMP_BACKWARD_NO_INTERRUPT 104 (to L11)

  --   L15:     LOAD_CONST               1 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RERAISE                  1

 484   L16:     RERAISE                  0

  --   L17:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L18:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L3 -> L18 [0] lasti
  L4 to L5 -> L12 [0]
  L6 to L8 -> L12 [0]
  L9 to L11 -> L12 [0]
  L11 to L12 -> L18 [0] lasti
  L12 to L13 -> L17 [1] lasti
  L13 to L14 -> L15 [1] lasti
  L14 to L15 -> L18 [0] lasti
  L15 to L17 -> L17 [1] lasti
  L17 to L18 -> L18 [0] lasti

Disassembly of <code object OperatorActionRequest at 0x0000018C18011210, file "app/routes/operator_brokerages.py", line 502>:
502           RESUME                   0
              LOAD_NAME                0 (__name__)
              STORE_NAME               1 (__module__)
              LOAD_CONST               0 ('OperatorActionRequest')
              STORE_NAME               2 (__qualname__)
              LOAD_CONST               1 (502)
              STORE_NAME               3 (__firstlineno__)
              SETUP_ANNOTATIONS

503           LOAD_NAME                4 (Field)
              PUSH_NULL
              LOAD_CONST               2 (Ellipsis)
              LOAD_SMALL_INT          64
              LOAD_CONST               3 (('max_length',))
              CALL_KW                  2
              STORE_NAME               5 (action)
              LOAD_CONST               4 ('str')
              LOAD_NAME                6 (__annotations__)
              LOAD_CONST               5 ('action')
              STORE_SUBSCR

504           LOAD_NAME                4 (Field)
              PUSH_NULL
              LOAD_CONST               2 (Ellipsis)
              LOAD_SMALL_INT         200
              LOAD_CONST               3 (('max_length',))
              CALL_KW                  2
              STORE_NAME               7 (actor_id)
              LOAD_CONST               4 ('str')
              LOAD_NAME                6 (__annotations__)
              LOAD_CONST               6 ('actor_id')
              STORE_SUBSCR

505           LOAD_NAME                4 (Field)
              PUSH_NULL
              LOAD_CONST               7 ('operator')
              LOAD_SMALL_INT          32
              LOAD_CONST               3 (('max_length',))
              CALL_KW                  2
              STORE_NAME               8 (actor_type)
              LOAD_CONST               4 ('str')
              LOAD_NAME                6 (__annotations__)
              LOAD_CONST               8 ('actor_type')
              STORE_SUBSCR

506           LOAD_NAME                4 (Field)
              PUSH_NULL
              LOAD_NAME                9 (dict)
              LOAD_CONST               9 (('default_factory',))
              CALL_KW                  1
              STORE_NAME              10 (payload)
              LOAD_CONST              10 ('Dict[str, Any]')
              LOAD_NAME                6 (__annotations__)
              LOAD_CONST              11 ('payload')
              STORE_SUBSCR
              LOAD_CONST              12 (())
              STORE_NAME              11 (__static_attributes__)
              LOAD_CONST              13 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026230, file "app/routes/operator_brokerages.py", line 510>:
510           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

511           LOAD_CONST               2 ('str')

510           LOAD_CONST               3 ('body')

512           LOAD_CONST               4 ('OperatorActionRequest')

510           LOAD_CONST               5 ('return')

514           LOAD_CONST               6 ('Dict[str, Any]')

510           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object post_brokerage_action at 0x0000018C17D51980, file "app/routes/operator_brokerages.py", line 509>:
 509            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 515            LOAD_GLOBAL              1 (_safe_brokerage + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                STORE_FAST               3 (bid)

 516            LOAD_FAST_BORROW         3 (bid)
                POP_JUMP_IF_NOT_NONE    14 (to L2)
                NOT_TAKEN

 517            LOAD_GLOBAL              3 (HTTPException + NULL)
                LOAD_CONST               1 (400)
                LOAD_CONST               2 ('invalid brokerage_id')
                LOAD_CONST               3 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

 518    L2:     LOAD_SMALL_INT           0
                LOAD_CONST               4 (('execute_action',))
                IMPORT_NAME              2 (app.services.operator.operator_actions)
                IMPORT_FROM              3 (execute_action)
                STORE_FAST               4 (execute_action)
                POP_TOP

 519    L3:     NOP

 520    L4:     LOAD_FAST_BORROW         4 (execute_action)
                PUSH_NULL

 521            LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR                8 (action)

 522            LOAD_FAST_BORROW         3 (bid)

 523            LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR               10 (actor_type)

 524            LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR               12 (actor_id)

 525            LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR               14 (payload)

 520            LOAD_CONST               5 (('action', 'brokerage_id', 'actor_type', 'actor_id', 'payload'))
                CALL_KW                  5
                STORE_FAST               5 (result)

 528            LOAD_CONST               6 ('status')
                LOAD_FAST_BORROW         5 (result)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST               6 ('status')
                CALL                     1

 529            LOAD_CONST               7 ('surface')
                LOAD_CONST               8 ('ops.brokerages.actions')

 530            LOAD_CONST               9 ('result')
                LOAD_FAST_BORROW         5 (result)

 527            BUILD_MAP                3
                STORE_FAST               6 (env)

 542    L5:     LOAD_GLOBAL             29 (_final_envelope + NULL)
                LOAD_FAST_BORROW         6 (env)
                LOAD_CONST               8 ('ops.brokerages.actions')
                LOAD_CONST              15 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --    L6:     PUSH_EXC_INFO

 532            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L10)
                NOT_TAKEN
                STORE_FAST               7 (e)

 533    L7:     LOAD_GLOBAL             20 (logger)
                LOAD_ATTR               23 (warning + NULL|self)

 534            LOAD_CONST              10 ('operator_brokerages actions error type=')
                LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 533            CALL                     1
                POP_TOP

 537            LOAD_CONST               6 ('status')
                LOAD_CONST              11 ('failed')

 538            LOAD_CONST               7 ('surface')
                LOAD_CONST               8 ('ops.brokerages.actions')

 539            LOAD_CONST              12 ('error_code')
                LOAD_CONST              13 ('unexpected:')
                LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 540            LOAD_CONST              14 ('warnings')
                BUILD_LIST               0

 536            BUILD_MAP                4
                STORE_FAST               6 (env)
        L8:     POP_EXCEPT
                LOAD_CONST               0 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                JUMP_BACKWARD_NO_INTERRUPT 104 (to L5)

  --    L9:     LOAD_CONST               0 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RERAISE                  1

 532   L10:     RERAISE                  0

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
```
