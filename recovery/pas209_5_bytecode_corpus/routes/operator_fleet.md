# routes/operator_fleet

- **pyc:** `app\routes\__pycache__\operator_fleet.cpython-314.pyc`
- **expected source path (absent):** `app\routes/operator_fleet.py`
- **co_filename (from bytecode):** `app\routes\operator_fleet.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** routes

## Module docstring

```
PAS187 — Operator fleet observability + two-person cutover
+ daily ops checklist routes (read + bounded mutation).

All routes require ``X-Admin-Key`` (PAS-SECURITY-04
``surface="admin"`` rate-limit applied). Mutations are
scoped to the closed cutover-approval + checklist
attestation flow. No tenant mutation surface.

Routes (mounted under ``/ops``):

  Fleet observability (read-only):
    GET  /ops/fleet/status
    GET  /ops/fleet/rollout-readiness
    GET  /ops/fleet/exceptions

  Two-person cutover (bounded mutation):
    GET  /ops/cutovers
    POST /ops/cutovers/{brokerage_id}/request
    POST /ops/cutovers/{cutover_id}/approve-first
    POST /ops/cutovers/{cutover_id}/approve-second
    POST /ops/cutovers/{cutover_id}/reject

  Daily ops checklist (bounded mutation):
    GET  /ops/daily-checklists
    POST /ops/daily-checklists/{brokerage_id}/complete

Doctrine:

* Admin auth required + operator rate-limit (PAS-SECURITY-04).
* Read-only routes never raise — service layer collapses to
  ``status="skipped"`` on DB unavailable.
* Mutation routes are bounded: they edit only the rows /
  attestation columns defined in v35 / v36. They do NOT
  flip a brokerage's pilot stage; that remains a separate
  PAS173 operator action.
* Every mutation emits a ``log_event_bg`` audit event with
  closed payload keys.
* No PII / no raw payload / no secret in any envelope —
  enforced by the service-layer forbidden-token scanner.
```

## Imports

`APIRouter`, `Any`, `Body`, `Depends`, `Dict`, `HTTPException`, `Header`, `Optional`, `Path`, `Query`, `__future__`, `annotations`, `app.config`, `app.db.event_logger`, `app.services.operator.cache_invalidation`, `app.services.operator.cutover_approval`, `app.services.operator.daily_ops_checklist`, `app.services.operator.fleet_status`, `app.services.operator.fleet_status_cache`, `app.services.operator.operator_policy_report`, `app.services.security.rate_limit`, `approve_cutover_first`, `approve_cutover_second`, `brokerage_policy_report`, `cache_stats`, `check_rate_limit`, `complete_daily_ops_checklist`, `cutover_status_report`, `daily_ops_checklist_report`, `fastapi`, `fleet_exception_report`, `fleet_rollout_readiness_summary`, `get_fleet_brokerage_health_summary`, `get_settings`, `invalidate`, `invalidate_fleet_status_for_brokerage`, `log_event_bg`, `logging`, `operator_policy_report`, `reject_cutover`, `request_cutover_approval`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_extract_actor`, `_invalidate_cache_for`, `_safe_brokerage_path`, `_safe_cutover_id_path`, `approve_first`, `approve_second`, `complete_checklist`, `get_brokerage_policy_report`, `get_fleet_cache_stats`, `get_fleet_exceptions`, `get_fleet_policy_report`, `get_fleet_rollout_readiness`, `get_fleet_status`, `list_cutovers`, `list_daily_checklists`, `post_fleet_cache_invalidate`, `reject`, `request_cutover`, `require_admin`

## Env-key candidates

`ADMIN`

## String constants (redacted where noted)

- '\nPAS187 — Operator fleet observability + two-person cutover\n+ daily ops checklist routes (read + bounded mutation).\n\nAll routes require ``X-Admin-Key`` (PAS-SECURITY-04\n``surface="admin"`` rate-limit applied). Mutations are\nscoped to the closed cutover-approval + checklist\nattestation flow. No tenant mutation surface.\n\nRoutes (mounted under ``/ops``):\n\n  Fleet observability (read-only):\n    GET  /ops/fleet/status\n    GET  /ops/fleet/rollout-readiness\n    GET  /ops/fleet/exceptions\n\n  Two-person cutover (bounded mutation):\n    GET  /ops/cutovers\n    POST /ops/cutovers/{brokerage_id}/request\n    POST /ops/cutovers/{cutover_id}/approve-first\n    POST /ops/cutovers/{cutover_id}/approve-second\n    POST /ops/cutovers/{cutover_id}/reject\n\n  Daily ops checklist (bounded mutation):\n    GET  /ops/daily-checklists\n    POST /ops/daily-checklists/{brokerage_id}/complete\n\nDoctrine:\n\n* Admin auth required + operator rate-limit (PAS-SECURITY-04).\n* Read-only routes never raise — service layer collapses to\n  ``status="skipped"`` on DB unavailable.\n* Mutation routes are bounded: they edit only the rows /\n  attestation columns defined in v35 / v36. They do NOT\n  flip a brokerage\'s pilot stage; that remains a separate\n  PAS173 operator action.\n* Every mutation emits a ``log_event_bg`` audit event with\n  closed payload keys.\n* No PII / no raw payload / no secret in any envelope —\n  enforced by the service-layer forbidden-token scanner.\n'
- 'pas.ops.fleet'
- '/fleet/status'
- '/fleet/cache-stats'
- '/fleet/policy-report'
- '/fleet/policy-report/{brokerage_id}'
- '/fleet/cache-invalidate'
- '/fleet/rollout-readiness'
- '/fleet/exceptions'
- '/cutovers'
- '/cutovers/{brokerage_id}/request'
- '/cutovers/{cutover_id}/approve-first'
- '/cutovers/{cutover_id}/approve-second'
- '/cutovers/{cutover_id}/reject'
- '/daily-checklists'
- '/daily-checklists/{brokerage_id}/complete'
- 'x_admin_key'
- 'str'
- 'return'
- 'bool'
- 'Invalid admin key'
- 'admin'
- 'ADMIN'
- 'allowed'
- 'Operator rate limit exceeded. Retry after the current window.'
- 'brokerage_id'
- 'invalid brokerage_id'
- 'cutover_id'
- 'invalid cutover_id'
- 'body'
- 'Optional[Dict[str, Any]]'
- 'Dict[str, Any]'
- 'actor_type'
- 'actor_id'
- 'actor_type and actor_id required'
- 'Optional[str]'
- 'reason'
- 'None'
- 'limit'
- 'int'
- 'offset'
- 'rows'
- 'count'
- 'total_in_window'
- 'brokerage_ids'
- 'operator.policy_report.generated'
- 'status'
- 'route'
- 'get_fleet_policy_report'
- 'warning_count'
- 'action_required'
- 'review_non_ok_sections'
- 'none'
- 'get_brokerage_policy_report'
- 'surface'
- 'target_stage'
- 'rationale'
- 'failed'
- 'error_code'
- 'cutover_requested'
- 'cutover_not_found'
- 'row'
- 'cutover_first_approved'
- 'self_second_approval_forbidden'
- 'cutover_second_approved'
- 'cutover_rejected'
- 'run_date'
- 'queue_checked'
- 'callbacks_checked'
- 'bookings_checked'
- 'audit_checked'
- 'learning_checked'
- 'security_checked'
- 'incident_count'
- 'notes'
- 'invalid_actor'
- 'daily_checklist_completed'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS187 — Operator fleet observability + two-person cutover\n+ daily ops checklist routes (read + bounded mutation).\n\nAll routes require ``X-Admin-Key`` (PAS-SECURITY-04\n``surface="admin"`` rate-limit applied). Mutations are\nscoped to the closed cutover-approval + checklist\nattestation flow. No tenant mutation surface.\n\nRoutes (mounted under ``/ops``):\n\n  Fleet observability (read-only):\n    GET  /ops/fleet/status\n    GET  /ops/fleet/rollout-readiness\n    GET  /ops/fleet/exceptions\n\n  Two-person cutover (bounded mutation):\n    GET  /ops/cutovers\n    POST /ops/cutovers/{brokerage_id}/request\n    POST /ops/cutovers/{cutover_id}/approve-first\n    POST /ops/cutovers/{cutover_id}/approve-second\n    POST /ops/cutovers/{cutover_id}/reject\n\n  Daily ops checklist (bounded mutation):\n    GET  /ops/daily-checklists\n    POST /ops/daily-checklists/{brokerage_id}/complete\n\nDoctrine:\n\n* Admin auth required + operator rate-limit (PAS-SECURITY-04).\n* Read-only routes never raise — service layer collapses to\n  ``status="skipped"`` on DB unavailable.\n* Mutation routes are bounded: they edit only the rows /\n  attestation columns defined in v35 / v36. They do NOT\n  flip a brokerage\'s pilot stage; that remains a separate\n  PAS173 operator action.\n* Every mutation emits a ``log_event_bg`` audit event with\n  closed payload keys.\n* No PII / no raw payload / no secret in any envelope —\n  enforced by the service-layer forbidden-token scanner.\n')
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
              LOAD_CONST               3 (('Any', 'Dict', 'Optional'))
              IMPORT_NAME              4 (typing)
              IMPORT_FROM              5 (Any)
              STORE_NAME               5 (Any)
              IMPORT_FROM              6 (Dict)
              STORE_NAME               6 (Dict)
              IMPORT_FROM              7 (Optional)
              STORE_NAME               7 (Optional)
              POP_TOP

 48           LOAD_SMALL_INT           0
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

 50           LOAD_SMALL_INT           0
              LOAD_CONST               5 (('get_settings',))
              IMPORT_NAME             16 (app.config)
              IMPORT_FROM             17 (get_settings)
              STORE_NAME              17 (get_settings)
              POP_TOP

 53           LOAD_NAME                9 (APIRouter)
              PUSH_NULL
              CALL                     0
              STORE_NAME              18 (router)

 54           LOAD_NAME                3 (logging)
              LOAD_ATTR               38 (getLogger)
              PUSH_NULL
              LOAD_CONST               6 ('pas.ops.fleet')
              CALL                     1
              STORE_NAME              20 (logger)

 61           LOAD_NAME               12 (Header)
              PUSH_NULL
              LOAD_CONST               7 (Ellipsis)
              CALL                     1
              BUILD_TUPLE              1
              LOAD_CONST               8 (<code object __annotate__ at 0x0000018C17FA2C40, file "app\routes\operator_fleet.py", line 61>)
              MAKE_FUNCTION
              LOAD_CONST               9 (<code object require_admin at 0x0000018C1801C9E0, file "app\routes\operator_fleet.py", line 61>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              21 (require_admin)

 90           LOAD_SMALL_INT         200
              STORE_NAME              22 (_BROKERAGE_ID_MAX_LEN)

 91           LOAD_SMALL_INT         200
              STORE_NAME              23 (_ACTOR_ID_MAX_LEN)

 94           LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA34B0, file "app\routes\operator_fleet.py", line 94>)
              MAKE_FUNCTION
              LOAD_CONST              11 (<code object _safe_brokerage_path at 0x0000018C17972D90, file "app\routes\operator_fleet.py", line 94>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              24 (_safe_brokerage_path)

101           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA3B40, file "app\routes\operator_fleet.py", line 101>)
              MAKE_FUNCTION
              LOAD_CONST              13 (<code object _safe_cutover_id_path at 0x0000018C18011370, file "app\routes\operator_fleet.py", line 101>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              25 (_safe_cutover_id_path)

108           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C17FA3960, file "app\routes\operator_fleet.py", line 108>)
              MAKE_FUNCTION
              LOAD_CONST              15 (<code object _extract_actor at 0x0000018C17FED630, file "app\routes\operator_fleet.py", line 108>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              26 (_extract_actor)

123           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C18025C30, file "app\routes\operator_fleet.py", line 123>)
              MAKE_FUNCTION
              LOAD_CONST              17 (<code object _invalidate_cache_for at 0x0000018C17C49B80, file "app\routes\operator_fleet.py", line 123>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              27 (_invalidate_cache_for)

142           LOAD_NAME               18 (router)
              LOAD_ATTR               57 (get + NULL|self)
              LOAD_CONST              18 ('/fleet/status')
              CALL                     1

144           LOAD_NAME               15 (Query)
              PUSH_NULL
              LOAD_SMALL_INT          50
              CALL                     1

145           LOAD_NAME               15 (Query)
              PUSH_NULL
              LOAD_SMALL_INT           0
              CALL                     1

146           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               21 (require_admin)
              CALL                     1

143           BUILD_TUPLE              3
              LOAD_CONST              19 (<code object __annotate__ at 0x0000018C18025A30, file "app\routes\operator_fleet.py", line 143>)
              MAKE_FUNCTION
              LOAD_CONST              20 (<code object get_fleet_status at 0x0000018C17D81580, file "app\routes\operator_fleet.py", line 142>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

142           CALL                     0

143           STORE_NAME              29 (get_fleet_status)

189           LOAD_NAME               18 (router)
              LOAD_ATTR               57 (get + NULL|self)
              LOAD_CONST              21 ('/fleet/cache-stats')
              CALL                     1

191           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               21 (require_admin)
              CALL                     1

190           BUILD_TUPLE              1
              LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA2970, file "app\routes\operator_fleet.py", line 190>)
              MAKE_FUNCTION
              LOAD_CONST              23 (<code object get_fleet_cache_stats at 0x0000018C18024C30, file "app\routes\operator_fleet.py", line 189>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

189           CALL                     0

190           STORE_NAME              30 (get_fleet_cache_stats)

198           LOAD_NAME               18 (router)
              LOAD_ATTR               57 (get + NULL|self)
              LOAD_CONST              24 ('/fleet/policy-report')
              CALL                     1

200           LOAD_NAME               15 (Query)
              PUSH_NULL
              LOAD_CONST               2 (None)
              LOAD_CONST              25 (4096)
              LOAD_CONST              26 (('max_length',))
              CALL_KW                  2

201           LOAD_NAME               15 (Query)
              PUSH_NULL
              LOAD_SMALL_INT          50
              CALL                     1

202           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               21 (require_admin)
              CALL                     1

199           BUILD_TUPLE              3
              LOAD_CONST              27 (<code object __annotate__ at 0x0000018C18026330, file "app\routes\operator_fleet.py", line 199>)
              MAKE_FUNCTION
              LOAD_CONST              28 (<code object get_fleet_policy_report at 0x0000018C17CC2960, file "app\routes\operator_fleet.py", line 198>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

198           CALL                     0

199           STORE_NAME              31 (get_fleet_policy_report)

227           LOAD_NAME               18 (router)
              LOAD_ATTR               57 (get + NULL|self)
              LOAD_CONST              29 ('/fleet/policy-report/{brokerage_id}')
              CALL                     1

229           LOAD_NAME               14 (Path)
              PUSH_NULL
              LOAD_CONST               7 (Ellipsis)
              LOAD_NAME               22 (_BROKERAGE_ID_MAX_LEN)
              LOAD_CONST              26 (('max_length',))
              CALL_KW                  2

230           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               21 (require_admin)
              CALL                     1

228           BUILD_TUPLE              2
              LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA23D0, file "app\routes\operator_fleet.py", line 228>)
              MAKE_FUNCTION
              LOAD_CONST              31 (<code object get_brokerage_policy_report at 0x0000018C1801CBD0, file "app\routes\operator_fleet.py", line 227>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

227           CALL                     0

228           STORE_NAME              32 (get_brokerage_policy_report)

252           LOAD_NAME               18 (router)
              LOAD_ATTR               67 (post + NULL|self)
              LOAD_CONST              32 ('/fleet/cache-invalidate')
              CALL                     1

254           LOAD_NAME               10 (Body)
              PUSH_NULL
              BUILD_MAP                0
              LOAD_CONST              33 (('default',))
              CALL_KW                  1

255           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               21 (require_admin)
              CALL                     1

253           BUILD_TUPLE              2
              LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA3C30, file "app\routes\operator_fleet.py", line 253>)
              MAKE_FUNCTION
              LOAD_CONST              35 (<code object post_fleet_cache_invalidate at 0x0000018C1802C880, file "app\routes\operator_fleet.py", line 252>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

252           CALL                     0

253           STORE_NAME              34 (post_fleet_cache_invalidate)

263           LOAD_NAME               18 (router)
              LOAD_ATTR               57 (get + NULL|self)
              LOAD_CONST              36 ('/fleet/rollout-readiness')
              CALL                     1

265           LOAD_NAME               15 (Query)
              PUSH_NULL
              LOAD_SMALL_INT          50
              CALL                     1

266           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               21 (require_admin)
              CALL                     1

264           BUILD_TUPLE              2
              LOAD_CONST              37 (<code object __annotate__ at 0x0000018C17FA3D20, file "app\routes\operator_fleet.py", line 264>)
              MAKE_FUNCTION
              LOAD_CONST              38 (<code object get_fleet_rollout_readiness at 0x0000018C18026630, file "app\routes\operator_fleet.py", line 263>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

263           CALL                     0

264           STORE_NAME              35 (get_fleet_rollout_readiness)

274           LOAD_NAME               18 (router)
              LOAD_ATTR               57 (get + NULL|self)
              LOAD_CONST              39 ('/fleet/exceptions')
              CALL                     1

276           LOAD_NAME               15 (Query)
              PUSH_NULL
              LOAD_SMALL_INT          50
              CALL                     1

277           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               21 (require_admin)
              CALL                     1

275           BUILD_TUPLE              2
              LOAD_CONST              40 (<code object __annotate__ at 0x0000018C17FA2D30, file "app\routes\operator_fleet.py", line 275>)
              MAKE_FUNCTION
              LOAD_CONST              41 (<code object get_fleet_exceptions at 0x0000018C18026430, file "app\routes\operator_fleet.py", line 274>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

274           CALL                     0

275           STORE_NAME              36 (get_fleet_exceptions)

289           LOAD_NAME               18 (router)
              LOAD_ATTR               57 (get + NULL|self)
              LOAD_CONST              42 ('/cutovers')
              CALL                     1

291           LOAD_NAME               15 (Query)
              PUSH_NULL
              LOAD_CONST               2 (None)
              LOAD_NAME               22 (_BROKERAGE_ID_MAX_LEN)
              LOAD_CONST              26 (('max_length',))
              CALL_KW                  2

292           LOAD_NAME               15 (Query)
              PUSH_NULL
              LOAD_CONST               2 (None)
              LOAD_SMALL_INT          32
              LOAD_CONST              26 (('max_length',))
              CALL_KW                  2

293           LOAD_NAME               15 (Query)
              PUSH_NULL
              LOAD_SMALL_INT          50
              CALL                     1

294           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               21 (require_admin)
              CALL                     1

290           BUILD_TUPLE              4
              LOAD_CONST              43 (<code object __annotate__ at 0x0000018C18025830, file "app\routes\operator_fleet.py", line 290>)
              MAKE_FUNCTION
              LOAD_CONST              44 (<code object list_cutovers at 0x0000018C18025F30, file "app\routes\operator_fleet.py", line 289>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

289           CALL                     0

290           STORE_NAME              37 (list_cutovers)

304           LOAD_NAME               18 (router)
              LOAD_ATTR               67 (post + NULL|self)
              LOAD_CONST              45 ('/cutovers/{brokerage_id}/request')
              CALL                     1

306           LOAD_NAME               14 (Path)
              PUSH_NULL
              LOAD_CONST               7 (Ellipsis)
              LOAD_NAME               22 (_BROKERAGE_ID_MAX_LEN)
              LOAD_CONST              26 (('max_length',))
              CALL_KW                  2

307           LOAD_NAME               10 (Body)
              PUSH_NULL
              BUILD_MAP                0
              LOAD_CONST              33 (('default',))
              CALL_KW                  1

308           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               21 (require_admin)
              CALL                     1

305           BUILD_TUPLE              3
              LOAD_CONST              46 (<code object __annotate__ at 0x0000018C18024F30, file "app\routes\operator_fleet.py", line 305>)
              MAKE_FUNCTION
              LOAD_CONST              47 (<code object request_cutover at 0x0000018C17D8D460, file "app\routes\operator_fleet.py", line 304>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

304           CALL                     0

305           STORE_NAME              38 (request_cutover)

339           LOAD_NAME               18 (router)
              LOAD_ATTR               67 (post + NULL|self)
              LOAD_CONST              48 ('/cutovers/{cutover_id}/approve-first')
              CALL                     1

341           LOAD_NAME               14 (Path)
              PUSH_NULL
              LOAD_CONST               7 (Ellipsis)
              LOAD_SMALL_INT          64
              LOAD_CONST              26 (('max_length',))
              CALL_KW                  2

342           LOAD_NAME               10 (Body)
              PUSH_NULL
              BUILD_MAP                0
              LOAD_CONST              33 (('default',))
              CALL_KW                  1

343           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               21 (require_admin)
              CALL                     1

340           BUILD_TUPLE              3
              LOAD_CONST              49 (<code object __annotate__ at 0x0000018C18024E30, file "app\routes\operator_fleet.py", line 340>)
              MAKE_FUNCTION
              LOAD_CONST              50 (<code object approve_first at 0x0000018C17CD2160, file "app\routes\operator_fleet.py", line 339>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

339           CALL                     0

340           STORE_NAME              39 (approve_first)

366           LOAD_NAME               18 (router)
              LOAD_ATTR               67 (post + NULL|self)
              LOAD_CONST              51 ('/cutovers/{cutover_id}/approve-second')
              CALL                     1

368           LOAD_NAME               14 (Path)
              PUSH_NULL
              LOAD_CONST               7 (Ellipsis)
              LOAD_SMALL_INT          64
              LOAD_CONST              26 (('max_length',))
              CALL_KW                  2

369           LOAD_NAME               10 (Body)
              PUSH_NULL
              BUILD_MAP                0
              LOAD_CONST              33 (('default',))
              CALL_KW                  1

370           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               21 (require_admin)
              CALL                     1

367           BUILD_TUPLE              3
              LOAD_CONST              52 (<code object __annotate__ at 0x0000018C18026030, file "app\routes\operator_fleet.py", line 367>)
              MAKE_FUNCTION
              LOAD_CONST              53 (<code object approve_second at 0x0000018C17E93990, file "app\routes\operator_fleet.py", line 366>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

366           CALL                     0

367           STORE_NAME              40 (approve_second)

395           LOAD_NAME               18 (router)
              LOAD_ATTR               67 (post + NULL|self)
              LOAD_CONST              54 ('/cutovers/{cutover_id}/reject')
              CALL                     1

397           LOAD_NAME               14 (Path)
              PUSH_NULL
              LOAD_CONST               7 (Ellipsis)
              LOAD_SMALL_INT          64
              LOAD_CONST              26 (('max_length',))
              CALL_KW                  2

398           LOAD_NAME               10 (Body)
              PUSH_NULL
              BUILD_MAP                0
              LOAD_CONST              33 (('default',))
              CALL_KW                  1

399           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               21 (require_admin)
              CALL                     1

396           BUILD_TUPLE              3
              LOAD_CONST              55 (<code object __annotate__ at 0x0000018C18025930, file "app\routes\operator_fleet.py", line 396>)
              MAKE_FUNCTION
              LOAD_CONST              56 (<code object reject at 0x0000018C17D520B0, file "app\routes\operator_fleet.py", line 395>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

395           CALL                     0

396           STORE_NAME              41 (reject)

428           LOAD_NAME               18 (router)
              LOAD_ATTR               57 (get + NULL|self)
              LOAD_CONST              57 ('/daily-checklists')
              CALL                     1

430           LOAD_NAME               15 (Query)
              PUSH_NULL
              LOAD_CONST               2 (None)
              LOAD_NAME               22 (_BROKERAGE_ID_MAX_LEN)
              LOAD_CONST              26 (('max_length',))
              CALL_KW                  2

431           LOAD_NAME               15 (Query)
              PUSH_NULL
              LOAD_SMALL_INT          30
              CALL                     1

432           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               21 (require_admin)
              CALL                     1

429           BUILD_TUPLE              3
              LOAD_CONST              58 (<code object __annotate__ at 0x0000018C18025330, file "app\routes\operator_fleet.py", line 429>)
              MAKE_FUNCTION
              LOAD_CONST              59 (<code object list_daily_checklists at 0x0000018C18025630, file "app\routes\operator_fleet.py", line 428>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

428           CALL                     0

429           STORE_NAME              42 (list_daily_checklists)

443           LOAD_NAME               18 (router)
              LOAD_ATTR               67 (post + NULL|self)
              LOAD_CONST              60 ('/daily-checklists/{brokerage_id}/complete')
              CALL                     1

445           LOAD_NAME               14 (Path)
              PUSH_NULL
              LOAD_CONST               7 (Ellipsis)
              LOAD_NAME               22 (_BROKERAGE_ID_MAX_LEN)
              LOAD_CONST              26 (('max_length',))
              CALL_KW                  2

446           LOAD_NAME               10 (Body)
              PUSH_NULL
              BUILD_MAP                0
              LOAD_CONST              33 (('default',))
              CALL_KW                  1

447           LOAD_NAME               11 (Depends)
              PUSH_NULL
              LOAD_NAME               21 (require_admin)
              CALL                     1

444           BUILD_TUPLE              3
              LOAD_CONST              61 (<code object __annotate__ at 0x0000018C18026730, file "app\routes\operator_fleet.py", line 444>)
              MAKE_FUNCTION
              LOAD_CONST              62 (<code object complete_checklist at 0x0000018C17D8C200, file "app\routes\operator_fleet.py", line 443>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

443           CALL                     0

444           STORE_NAME              43 (complete_checklist)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "app\routes\operator_fleet.py", line 61>:
 61           RESUME                   0
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

Disassembly of <code object require_admin at 0x0000018C1801C9E0, file "app\routes\operator_fleet.py", line 61>:
  61            RESUME                   0

  62            LOAD_GLOBAL              1 (get_settings + NULL)
                CALL                     0
                STORE_FAST               1 (settings)

  63            LOAD_FAST_BORROW         1 (settings)
                LOAD_ATTR                2 (ADMIN_API_KEY)
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (x_admin_key, settings)
                LOAD_ATTR                2 (ADMIN_API_KEY)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       14 (to L2)
                NOT_TAKEN

  64    L1:     LOAD_GLOBAL              5 (HTTPException + NULL)
                LOAD_CONST               0 (401)
                LOAD_CONST               1 ('Invalid admin key')
                LOAD_CONST               2 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

  67    L2:     NOP

  68    L3:     LOAD_SMALL_INT           0
                LOAD_CONST               3 (('check_rate_limit',))
                IMPORT_NAME              3 (app.services.security.rate_limit)
                IMPORT_FROM              4 (check_rate_limit)
                STORE_FAST               2 (check_rate_limit)
                POP_TOP

  69            LOAD_FAST_BORROW         2 (check_rate_limit)
                PUSH_NULL

  70            LOAD_CONST               4 ('admin')

  71            LOAD_CONST               5 ('ADMIN')

  72            LOAD_FAST_BORROW         0 (x_admin_key)

  69            LOAD_CONST               6 (('surface', 'actor_type', 'actor_token'))
                CALL_KW                  3
                STORE_FAST               3 (_rl_verdict)

  74            LOAD_FAST_BORROW         3 (_rl_verdict)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               7 ('allowed')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        14 (to L6)
        L4:     NOT_TAKEN

  75    L5:     LOAD_GLOBAL              5 (HTTPException + NULL)

  76            LOAD_CONST               8 (429)

  77            LOAD_CONST               9 ('Operator rate limit exceeded. Retry after the current window.')

  75            LOAD_CONST               2 (('status_code', 'detail'))
                CALL_KW                  2
                RAISE_VARARGS            1

  74    L6:     NOP

  83            LOAD_CONST              10 (True)
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

  79            LOAD_GLOBAL              4 (HTTPException)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                POP_TOP

  80            RAISE_VARARGS            0

  81    L8:     LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L12)
        L9:     NOT_TAKEN
       L10:     POP_TOP

  82   L11:     POP_EXCEPT

  83            LOAD_CONST              10 (True)
                RETURN_VALUE

  81   L12:     RERAISE                  0

  --   L13:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L7 [0]
  L5 to L6 -> L7 [0]
  L7 to L9 -> L13 [1] lasti
  L10 to L11 -> L13 [1] lasti
  L12 to L13 -> L13 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "app\routes\operator_fleet.py", line 94>:
 94           RESUME                   0
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

Disassembly of <code object _safe_brokerage_path at 0x0000018C17972D90, file "app\routes\operator_fleet.py", line 94>:
 94           RESUME                   0

 95           LOAD_FAST                0 (brokerage_id)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               0 ('')
      L1:     LOAD_ATTR                1 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

 96           LOAD_FAST_BORROW         1 (s)
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

 97   L2:     LOAD_GLOBAL              7 (HTTPException + NULL)
              LOAD_CONST               1 (400)
              LOAD_CONST               2 ('invalid brokerage_id')
              LOAD_CONST               3 (('status_code', 'detail'))
              CALL_KW                  2
              RAISE_VARARGS            1

 98   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "app\routes\operator_fleet.py", line 101>:
101           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('cutover_id')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               2 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _safe_cutover_id_path at 0x0000018C18011370, file "app\routes\operator_fleet.py", line 101>:
101           RESUME                   0

102           LOAD_FAST                0 (cutover_id)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               0 ('')
      L1:     LOAD_ATTR                1 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

103           LOAD_FAST_BORROW         1 (s)
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

104   L2:     LOAD_GLOBAL              5 (HTTPException + NULL)
              LOAD_CONST               1 (400)
              LOAD_CONST               2 ('invalid cutover_id')
              LOAD_CONST               3 (('status_code', 'detail'))
              CALL_KW                  2
              RAISE_VARARGS            1

105   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "app\routes\operator_fleet.py", line 108>:
108           RESUME                   0
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

Disassembly of <code object _extract_actor at 0x0000018C17FED630, file "app\routes\operator_fleet.py", line 108>:
108           RESUME                   0

109           LOAD_FAST                0 (body)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L1:     STORE_FAST               0 (body)

110           LOAD_FAST_BORROW         0 (body)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               0 ('actor_type')
              CALL                     1
              STORE_FAST               1 (actor_type)

111           LOAD_FAST_BORROW         0 (body)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               1 ('actor_id')
              CALL                     1
              STORE_FAST               2 (actor_id)

112           LOAD_GLOBAL              3 (isinstance + NULL)
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

113   L2:     LOAD_GLOBAL              7 (HTTPException + NULL)

114           LOAD_CONST               2 (400)

115           LOAD_CONST               3 ('actor_type and actor_id required')

113           LOAD_CONST               4 (('status_code', 'detail'))
              CALL_KW                  2
              RAISE_VARARGS            1

118   L3:     LOAD_CONST               0 ('actor_type')
              LOAD_FAST_BORROW         1 (actor_type)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              LOAD_CONST               5 (slice(None, 32, None))
              BINARY_OP               26 ([])

119           LOAD_CONST               1 ('actor_id')
              LOAD_FAST_BORROW         2 (actor_id)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              LOAD_CONST               6 (None)
              LOAD_GLOBAL             10 (_ACTOR_ID_MAX_LEN)
              BINARY_SLICE

117           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025C30, file "app\routes\operator_fleet.py", line 123>:
123           RESUME                   0
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

Disassembly of <code object _invalidate_cache_for at 0x0000018C17C49B80, file "app\routes\operator_fleet.py", line 123>:
 123           RESUME                   0

 127           LOAD_FAST_BORROW         0 (brokerage_id)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN

 128           LOAD_CONST               0 (None)
               RETURN_VALUE

 129   L1:     NOP

 130   L2:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('invalidate_fleet_status_for_brokerage',))
               IMPORT_NAME              0 (app.services.operator.cache_invalidation)
               IMPORT_FROM              1 (invalidate_fleet_status_for_brokerage)
               STORE_FAST               2 (invalidate_fleet_status_for_brokerage)
               POP_TOP

 133           LOAD_FAST_BORROW         2 (invalidate_fleet_status_for_brokerage)
               PUSH_NULL
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (brokerage_id, reason)
               LOAD_CONST               2 (('reason',))
               CALL_KW                  2
               POP_TOP
       L3:     LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     PUSH_EXC_INFO

 134           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L6)
               NOT_TAKEN
               POP_TOP

 135   L5:     POP_EXCEPT
               LOAD_CONST               0 (None)
               RETURN_VALUE

 134   L6:     RERAISE                  0

  --   L7:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L4 [0]
  L4 to L5 -> L7 [1] lasti
  L6 to L7 -> L7 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025A30, file "app\routes\operator_fleet.py", line 143>:
143           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('limit')

144           LOAD_CONST               2 ('int')

143           LOAD_CONST               3 ('offset')

145           LOAD_CONST               2 ('int')

143           LOAD_CONST               4 ('return')

147           LOAD_CONST               5 ('Dict[str, Any]')

143           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object get_fleet_status at 0x0000018C17D81580, file "app\routes\operator_fleet.py", line 142>:
 142            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 155            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('get_fleet_brokerage_health_summary',))
                IMPORT_NAME              0 (app.services.operator.fleet_status_cache)
                IMPORT_FROM              1 (get_fleet_brokerage_health_summary)
                STORE_FAST               3 (get_fleet_brokerage_health_summary)
                POP_TOP

 159    L2:     NOP

 160    L3:     LOAD_GLOBAL              5 (int + NULL)
                LOAD_FAST_BORROW         1 (offset)
                CALL                     1
                STORE_FAST               4 (off)

 163    L4:     LOAD_FAST_BORROW         4 (off)
                LOAD_SMALL_INT           0
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN

 164            LOAD_SMALL_INT           0
                STORE_FAST               4 (off)

 165    L5:     LOAD_FAST_BORROW         4 (off)
                LOAD_CONST               2 (5000)
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN

 166            LOAD_CONST               2 (5000)
                STORE_FAST               4 (off)

 167    L6:     NOP

 168    L7:     LOAD_GLOBAL              5 (int + NULL)
                LOAD_FAST_BORROW         0 (limit)
                CALL                     1
                STORE_FAST               5 (lim)

 171    L8:     LOAD_FAST_BORROW         5 (lim)
                LOAD_SMALL_INT           1
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        3 (to L9)
                NOT_TAKEN

 172            LOAD_SMALL_INT           1
                STORE_FAST               5 (lim)

 173    L9:     LOAD_FAST_BORROW         5 (lim)
                LOAD_SMALL_INT         200
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN

 174            LOAD_SMALL_INT         200
                STORE_FAST               5 (lim)

 175   L10:     LOAD_GLOBAL             11 (min + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 84 (lim, off)
                BINARY_OP                0 (+)
                LOAD_SMALL_INT         200
                CALL                     2
                STORE_FAST               6 (fetch_lim)

 176            LOAD_FAST_BORROW         3 (get_fleet_brokerage_health_summary)
                PUSH_NULL
                LOAD_FAST_BORROW         6 (fetch_lim)
                LOAD_CONST               3 (('limit',))
                CALL_KW                  1
                STORE_FAST               7 (env)

 177            LOAD_FAST_BORROW         7 (env)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               4 ('rows')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
       L11:     NOT_TAKEN
       L12:     POP_TOP
                BUILD_LIST               0
       L13:     STORE_FAST               8 (rows)

 178            LOAD_FAST_BORROW_LOAD_FAST_BORROW 132 (rows, off)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (off, lim)
                BINARY_OP                0 (+)
                BINARY_SLICE
                STORE_FAST               9 (sliced)

 180            LOAD_GLOBAL             15 (dict + NULL)
                LOAD_FAST_BORROW         7 (env)
                CALL                     1
                STORE_FAST              10 (out)

 181            LOAD_FAST_BORROW_LOAD_FAST_BORROW 154 (sliced, out)
                LOAD_CONST               4 ('rows')
                STORE_SUBSCR

 182            LOAD_GLOBAL             17 (len + NULL)
                LOAD_FAST_BORROW         9 (sliced)
                CALL                     1
                LOAD_FAST_BORROW        10 (out)
                LOAD_CONST               5 ('count')
                STORE_SUBSCR

 183            LOAD_FAST_BORROW_LOAD_FAST_BORROW 90 (lim, out)
                LOAD_CONST               6 ('limit')
                STORE_SUBSCR

 184            LOAD_FAST_BORROW_LOAD_FAST_BORROW 74 (off, out)
                LOAD_CONST               7 ('offset')
                STORE_SUBSCR

 185            LOAD_GLOBAL             17 (len + NULL)
                LOAD_FAST_BORROW         8 (rows)
                CALL                     1
                LOAD_FAST_BORROW        10 (out)
                LOAD_CONST               8 ('total_in_window')
                STORE_SUBSCR

 186            LOAD_FAST_BORROW        10 (out)
                RETURN_VALUE

  --   L14:     PUSH_EXC_INFO

 161            LOAD_GLOBAL              6 (TypeError)
                LOAD_GLOBAL              8 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L16)
                NOT_TAKEN
                POP_TOP

 162            LOAD_SMALL_INT           0
                STORE_FAST               4 (off)
       L15:     POP_EXCEPT
                JUMP_BACKWARD_NO_INTERRUPT 186 (to L4)

 161   L16:     RERAISE                  0

  --   L17:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L18:     PUSH_EXC_INFO

 169            LOAD_GLOBAL              6 (TypeError)
                LOAD_GLOBAL              8 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L20)
                NOT_TAKEN
                POP_TOP

 170            LOAD_SMALL_INT          50
                STORE_FAST               5 (lim)
       L19:     POP_EXCEPT
                JUMP_BACKWARD_NO_INTERRUPT 181 (to L8)

 169   L20:     RERAISE                  0

  --   L21:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L22:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L22 [0] lasti
  L3 to L4 -> L14 [0]
  L4 to L6 -> L22 [0] lasti
  L7 to L8 -> L18 [0]
  L8 to L11 -> L22 [0] lasti
  L12 to L14 -> L22 [0] lasti
  L14 to L15 -> L17 [1] lasti
  L15 to L16 -> L22 [0] lasti
  L16 to L17 -> L17 [1] lasti
  L17 to L18 -> L22 [0] lasti
  L18 to L19 -> L21 [1] lasti
  L19 to L20 -> L22 [0] lasti
  L20 to L21 -> L21 [1] lasti
  L21 to L22 -> L22 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "app\routes\operator_fleet.py", line 190>:
190           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')

192           LOAD_CONST               2 ('Dict[str, Any]')

190           BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object get_fleet_cache_stats at 0x0000018C18024C30, file "app\routes\operator_fleet.py", line 189>:
 189           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0

 194           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('cache_stats',))
               IMPORT_NAME              0 (app.services.operator.fleet_status_cache)
               IMPORT_FROM              1 (cache_stats)
               STORE_FAST               1 (cache_stats)
               POP_TOP

 195           LOAD_FAST_BORROW         1 (cache_stats)
               PUSH_NULL
               CALL                     0
               RETURN_VALUE

  --   L2:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L2 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026330, file "app\routes\operator_fleet.py", line 199>:
199           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_ids')

200           LOAD_CONST               2 ('Optional[str]')

199           LOAD_CONST               3 ('limit')

201           LOAD_CONST               4 ('int')

199           LOAD_CONST               5 ('return')

203           LOAD_CONST               6 ('Dict[str, Any]')

199           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object get_fleet_policy_report at 0x0000018C17CC2960, file "app\routes\operator_fleet.py", line 198>:
 198            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 205            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('operator_policy_report',))
                IMPORT_NAME              0 (app.services.operator.operator_policy_report)
                IMPORT_FROM              1 (operator_policy_report)
                STORE_FAST               3 (operator_policy_report)
                POP_TOP

 208            LOAD_CONST               2 (None)
                STORE_FAST               4 (ids)

 209            LOAD_FAST_BORROW         0 (brokerage_ids)
                TO_BOOL
                POP_JUMP_IF_FALSE       70 (to L8)
                NOT_TAKEN

 210            LOAD_FAST_BORROW         0 (brokerage_ids)
                LOAD_ATTR                5 (split + NULL|self)
                LOAD_CONST               3 (',')
                CALL                     1
                GET_ITER
                LOAD_FAST_AND_CLEAR      5 (s)
                SWAP                     2
        L2:     BUILD_LIST               0
                SWAP                     2
        L3:     FOR_ITER                42 (to L6)
                STORE_FAST_LOAD_FAST    85 (s, s)
                LOAD_ATTR                7 (strip + NULL|self)
                CALL                     0
                TO_BOOL
        L4:     POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN
                JUMP_BACKWARD           26 (to L3)
        L5:     LOAD_FAST_BORROW         5 (s)
                LOAD_ATTR                7 (strip + NULL|self)
                CALL                     0
                LIST_APPEND              2
                JUMP_BACKWARD           44 (to L3)
        L6:     END_FOR
                POP_ITER
        L7:     STORE_FAST               4 (ids)
                STORE_FAST               5 (s)

 211    L8:     LOAD_FAST                3 (operator_policy_report)
                PUSH_NULL
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 65 (ids, limit)
                LOAD_CONST               4 (('brokerage_ids', 'limit'))
                CALL_KW                  2
                STORE_FAST               6 (env)

 213    L9:     NOP

 214   L10:     LOAD_SMALL_INT           0
                LOAD_CONST               5 (('log_event_bg',))
                IMPORT_NAME              4 (app.db.event_logger)
                IMPORT_FROM              5 (log_event_bg)
                STORE_FAST               7 (log_event_bg)
                POP_TOP

 215            LOAD_FAST                7 (log_event_bg)
                PUSH_NULL
                LOAD_CONST               6 ('operator.policy_report.generated')

 216            LOAD_CONST               7 ('status')
                LOAD_FAST_BORROW         6 (env)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               7 ('status')
                CALL                     1

 217            LOAD_CONST               8 ('route')
                LOAD_CONST               9 ('get_fleet_policy_report')

 218            LOAD_CONST              10 ('warning_count')
                LOAD_FAST_BORROW         6 (env)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               7 ('status')
                CALL                     1
                LOAD_CONST              11 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L11)
                NOT_TAKEN
                LOAD_SMALL_INT           0
                JUMP_FORWARD             1 (to L12)
       L11:     LOAD_SMALL_INT           1

 219   L12:     LOAD_CONST              12 ('action_required')

 220            LOAD_FAST_BORROW         6 (env)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               7 ('status')
                CALL                     1
                LOAD_CONST              11 ('ok')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE        3 (to L13)
                NOT_TAKEN

 219            LOAD_CONST              13 ('review_non_ok_sections')
                JUMP_FORWARD             1 (to L14)

 220   L13:     LOAD_CONST              14 ('none')

 215   L14:     BUILD_MAP                4
                CALL                     2
                POP_TOP

 224   L15:     LOAD_FAST_BORROW         6 (env)
                RETURN_VALUE

  --   L16:     SWAP                     2
                POP_TOP

 210            SWAP                     2
                STORE_FAST               5 (s)
                RERAISE                  0

  --   L17:     PUSH_EXC_INFO

 222            LOAD_GLOBAL             14 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L19)
                NOT_TAKEN
                POP_TOP

 223   L18:     POP_EXCEPT

 224            LOAD_FAST                6 (env)
                RETURN_VALUE

 222   L19:     RERAISE                  0

  --   L20:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L21:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L21 [0] lasti
  L2 to L4 -> L16 [2]
  L5 to L7 -> L16 [2]
  L7 to L9 -> L21 [0] lasti
  L10 to L15 -> L17 [0]
  L15 to L17 -> L21 [0] lasti
  L17 to L18 -> L20 [1] lasti
  L18 to L19 -> L21 [0] lasti
  L19 to L20 -> L20 [1] lasti
  L20 to L21 -> L21 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "app\routes\operator_fleet.py", line 228>:
228           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

229           LOAD_CONST               2 ('str')

228           LOAD_CONST               3 ('return')

231           LOAD_CONST               4 ('Dict[str, Any]')

228           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object get_brokerage_policy_report at 0x0000018C1801CBD0, file "app\routes\operator_fleet.py", line 227>:
 227            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 232            LOAD_GLOBAL              1 (_safe_brokerage_path + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                STORE_FAST               2 (bid)

 233            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('brokerage_policy_report',))
                IMPORT_NAME              1 (app.services.operator.operator_policy_report)
                IMPORT_FROM              2 (brokerage_policy_report)
                STORE_FAST               3 (brokerage_policy_report)
                POP_TOP

 236            LOAD_FAST_BORROW         3 (brokerage_policy_report)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (bid)
                CALL                     1
                STORE_FAST               4 (env)

 237    L2:     NOP

 238    L3:     LOAD_SMALL_INT           0
                LOAD_CONST               2 (('log_event_bg',))
                IMPORT_NAME              3 (app.db.event_logger)
                IMPORT_FROM              4 (log_event_bg)
                STORE_FAST               5 (log_event_bg)
                POP_TOP

 239            LOAD_FAST                5 (log_event_bg)
                PUSH_NULL
                LOAD_CONST               3 ('operator.policy_report.generated')

 240            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST                2 (bid)

 241            LOAD_CONST               5 ('status')
                LOAD_FAST_BORROW         4 (env)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               5 ('status')
                CALL                     1

 242            LOAD_CONST               6 ('route')
                LOAD_CONST               7 ('get_brokerage_policy_report')

 243            LOAD_CONST               8 ('warning_count')
                LOAD_FAST_BORROW         4 (env)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               5 ('status')
                CALL                     1
                LOAD_CONST               9 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L4)
                NOT_TAKEN
                LOAD_SMALL_INT           0
                JUMP_FORWARD             1 (to L5)
        L4:     LOAD_SMALL_INT           1

 244    L5:     LOAD_CONST              10 ('action_required')

 245            LOAD_FAST_BORROW         4 (env)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               5 ('status')
                CALL                     1
                LOAD_CONST               9 ('ok')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN

 244            LOAD_CONST              11 ('review_non_ok_sections')
                JUMP_FORWARD             1 (to L7)

 245    L6:     LOAD_CONST              12 ('none')

 239    L7:     BUILD_MAP                5
                CALL                     2
                POP_TOP

 249    L8:     LOAD_FAST_BORROW         4 (env)
                RETURN_VALUE

  --    L9:     PUSH_EXC_INFO

 247            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L11)
                NOT_TAKEN
                POP_TOP

 248   L10:     POP_EXCEPT

 249            LOAD_FAST                4 (env)
                RETURN_VALUE

 247   L11:     RERAISE                  0

  --   L12:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L13:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L13 [0] lasti
  L3 to L8 -> L9 [0]
  L8 to L9 -> L13 [0] lasti
  L9 to L10 -> L12 [1] lasti
  L10 to L11 -> L13 [0] lasti
  L11 to L12 -> L12 [1] lasti
  L12 to L13 -> L13 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "app\routes\operator_fleet.py", line 253>:
253           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('body')

254           LOAD_CONST               2 ('Dict[str, Any]')

253           LOAD_CONST               3 ('return')

256           LOAD_CONST               2 ('Dict[str, Any]')

253           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object post_fleet_cache_invalidate at 0x0000018C1802C880, file "app\routes\operator_fleet.py", line 252>:
 252           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0

 259           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('invalidate',))
               IMPORT_NAME              0 (app.services.operator.fleet_status_cache)
               IMPORT_FROM              1 (invalidate)
               STORE_FAST               2 (invalidate)
               POP_TOP

 260           LOAD_FAST                2 (invalidate)
               PUSH_NULL
               LOAD_FAST                0 (body)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               BUILD_MAP                0
       L2:     LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               2 ('surface')
               CALL                     1
               LOAD_CONST               3 (('surface',))
               CALL_KW                  1
               RETURN_VALUE

  --   L3:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L3 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3D20, file "app\routes\operator_fleet.py", line 264>:
264           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('limit')

265           LOAD_CONST               2 ('int')

264           LOAD_CONST               3 ('return')

267           LOAD_CONST               4 ('Dict[str, Any]')

264           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object get_fleet_rollout_readiness at 0x0000018C18026630, file "app\routes\operator_fleet.py", line 263>:
 263           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0

 268           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('fleet_rollout_readiness_summary',))
               IMPORT_NAME              0 (app.services.operator.fleet_status)
               IMPORT_FROM              1 (fleet_rollout_readiness_summary)
               STORE_FAST               2 (fleet_rollout_readiness_summary)
               POP_TOP

 271           LOAD_FAST_BORROW         2 (fleet_rollout_readiness_summary)
               PUSH_NULL
               LOAD_FAST_BORROW         0 (limit)
               LOAD_CONST               2 (('limit',))
               CALL_KW                  1
               RETURN_VALUE

  --   L2:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L2 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "app\routes\operator_fleet.py", line 275>:
275           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('limit')

276           LOAD_CONST               2 ('int')

275           LOAD_CONST               3 ('return')

278           LOAD_CONST               4 ('Dict[str, Any]')

275           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object get_fleet_exceptions at 0x0000018C18026430, file "app\routes\operator_fleet.py", line 274>:
 274           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0

 279           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('fleet_exception_report',))
               IMPORT_NAME              0 (app.services.operator.fleet_status)
               IMPORT_FROM              1 (fleet_exception_report)
               STORE_FAST               2 (fleet_exception_report)
               POP_TOP

 282           LOAD_FAST_BORROW         2 (fleet_exception_report)
               PUSH_NULL
               LOAD_FAST_BORROW         0 (limit)
               LOAD_CONST               2 (('limit',))
               CALL_KW                  1
               RETURN_VALUE

  --   L2:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L2 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025830, file "app\routes\operator_fleet.py", line 290>:
290           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

291           LOAD_CONST               2 ('Optional[str]')

290           LOAD_CONST               3 ('status')

292           LOAD_CONST               2 ('Optional[str]')

290           LOAD_CONST               4 ('limit')

293           LOAD_CONST               5 ('int')

290           LOAD_CONST               6 ('return')

295           LOAD_CONST               7 ('Dict[str, Any]')

290           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object list_cutovers at 0x0000018C18025F30, file "app\routes\operator_fleet.py", line 289>:
 289           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0

 296           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('cutover_status_report',))
               IMPORT_NAME              0 (app.services.operator.cutover_approval)
               IMPORT_FROM              1 (cutover_status_report)
               STORE_FAST               4 (cutover_status_report)
               POP_TOP

 297           LOAD_FAST_BORROW         4 (cutover_status_report)
               PUSH_NULL

 298           LOAD_FAST_BORROW         0 (brokerage_id)

 299           LOAD_FAST_BORROW         1 (status)

 300           LOAD_FAST_BORROW         2 (limit)

 297           LOAD_CONST               2 (('brokerage_id', 'status', 'limit'))
               CALL_KW                  3
               RETURN_VALUE

  --   L2:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L2 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024F30, file "app\routes\operator_fleet.py", line 305>:
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

Disassembly of <code object request_cutover at 0x0000018C17D8D460, file "app\routes\operator_fleet.py", line 304>:
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

 312           LOAD_FAST_BORROW         1 (body)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               0 ('target_stage')
               CALL                     1
               STORE_FAST               5 (target_stage)

 313           LOAD_FAST_BORROW         1 (body)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               1 ('rationale')
               CALL                     1
               STORE_FAST               6 (rationale)

 314           LOAD_SMALL_INT           0
               LOAD_CONST               2 (('request_cutover_approval',))
               IMPORT_NAME              3 (app.services.operator.cutover_approval)
               IMPORT_FROM              4 (request_cutover_approval)
               STORE_FAST               7 (request_cutover_approval)
               POP_TOP

 317           LOAD_FAST_BORROW         7 (request_cutover_approval)
               PUSH_NULL

 318           LOAD_FAST_BORROW         3 (bid)

 319           LOAD_FAST_BORROW         5 (target_stage)

 320           LOAD_FAST_BORROW         4 (actor)
               LOAD_CONST               3 ('actor_type')
               BINARY_OP               26 ([])

 321           LOAD_FAST_BORROW         4 (actor)
               LOAD_CONST               4 ('actor_id')
               BINARY_OP               26 ([])

 322           LOAD_FAST_BORROW         6 (rationale)

 317           LOAD_CONST               5 (('brokerage_id', 'target_stage', 'actor_type', 'actor_id', 'rationale'))
               CALL_KW                  5
               STORE_FAST               8 (env)

 324           LOAD_FAST_BORROW         8 (env)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               6 ('status')
               CALL                     1
               LOAD_CONST               7 ('failed')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       51 (to L2)
               NOT_TAKEN

 327           LOAD_FAST_BORROW         8 (env)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               8 ('error_code')
               CALL                     1
               LOAD_CONST              13 (('invalid_brokerage_id', 'invalid_target_stage', 'invalid_actor_type'))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       29 (to L2)
               NOT_TAKEN

 332           LOAD_GLOBAL             11 (HTTPException + NULL)
               LOAD_CONST               9 (400)
               LOAD_FAST_BORROW         8 (env)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               8 ('error_code')
               CALL                     1
               LOAD_CONST              10 (('status_code', 'detail'))
               CALL_KW                  2
               RAISE_VARARGS            1

 334   L2:     LOAD_FAST_BORROW         8 (env)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               6 ('status')
               CALL                     1
               LOAD_CONST              11 ('ok')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       13 (to L3)
               NOT_TAKEN

 335           LOAD_GLOBAL             13 (_invalidate_cache_for + NULL)
               LOAD_FAST_BORROW         3 (bid)
               LOAD_CONST              12 ('cutover_requested')
               CALL                     2
               POP_TOP

 336   L3:     LOAD_FAST_BORROW         8 (env)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024E30, file "app\routes\operator_fleet.py", line 340>:
340           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('cutover_id')

341           LOAD_CONST               2 ('str')

340           LOAD_CONST               3 ('body')

342           LOAD_CONST               4 ('Dict[str, Any]')

340           LOAD_CONST               5 ('return')

344           LOAD_CONST               4 ('Dict[str, Any]')

340           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object approve_first at 0x0000018C17CD2160, file "app\routes\operator_fleet.py", line 339>:
 339           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0

 345           LOAD_GLOBAL              1 (_safe_cutover_id_path + NULL)
               LOAD_FAST_BORROW         0 (cutover_id)
               CALL                     1
               STORE_FAST               3 (cid)

 346           LOAD_GLOBAL              3 (_extract_actor + NULL)
               LOAD_FAST_BORROW         1 (body)
               CALL                     1
               STORE_FAST               4 (actor)

 347           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('approve_cutover_first',))
               IMPORT_NAME              2 (app.services.operator.cutover_approval)
               IMPORT_FROM              3 (approve_cutover_first)
               STORE_FAST               5 (approve_cutover_first)
               POP_TOP

 348           LOAD_FAST_BORROW         5 (approve_cutover_first)
               PUSH_NULL

 349           LOAD_FAST_BORROW         3 (cid)

 350           LOAD_FAST_BORROW         4 (actor)
               LOAD_CONST               2 ('actor_type')
               BINARY_OP               26 ([])

 351           LOAD_FAST_BORROW         4 (actor)
               LOAD_CONST               3 ('actor_id')
               BINARY_OP               26 ([])

 348           LOAD_CONST               4 (('cutover_id', 'actor_type', 'actor_id'))
               CALL_KW                  3
               STORE_FAST               6 (env)

 353           LOAD_FAST_BORROW         6 (env)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST               5 ('status')
               CALL                     1
               LOAD_CONST               6 ('failed')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       58 (to L3)
               NOT_TAKEN

 354           LOAD_FAST_BORROW         6 (env)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST               7 ('error_code')
               CALL                     1
               STORE_FAST               7 (code)

 355           LOAD_FAST_BORROW         7 (code)
               LOAD_CONST               8 ('cutover_not_found')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       14 (to L2)
               NOT_TAKEN

 356           LOAD_GLOBAL             11 (HTTPException + NULL)
               LOAD_CONST               9 (404)
               LOAD_FAST_BORROW         7 (code)
               LOAD_CONST              10 (('status_code', 'detail'))
               CALL_KW                  2
               RAISE_VARARGS            1

 357   L2:     LOAD_FAST_BORROW         7 (code)
               LOAD_CONST              16 (('invalid_arguments', 'invalid_status_transition'))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       14 (to L3)
               NOT_TAKEN

 358           LOAD_GLOBAL             11 (HTTPException + NULL)
               LOAD_CONST              11 (400)
               LOAD_FAST_BORROW         7 (code)
               LOAD_CONST              10 (('status_code', 'detail'))
               CALL_KW                  2
               RAISE_VARARGS            1

 360   L3:     LOAD_FAST_BORROW         6 (env)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST               5 ('status')
               CALL                     1
               LOAD_CONST              12 ('ok')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       55 (to L7)
               NOT_TAKEN

 361           LOAD_FAST_BORROW         6 (env)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST              13 ('row')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L6)
       L4:     NOT_TAKEN
       L5:     POP_TOP
               BUILD_MAP                0
       L6:     STORE_FAST               8 (row)

 362           LOAD_GLOBAL             13 (_invalidate_cache_for + NULL)
               LOAD_FAST_BORROW         8 (row)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST              14 ('brokerage_id')
               CALL                     1
               LOAD_CONST              15 ('cutover_first_approved')
               CALL                     2
               POP_TOP

 363   L7:     LOAD_FAST_BORROW         6 (env)
               RETURN_VALUE

  --   L8:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L8 [0] lasti
  L5 to L8 -> L8 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026030, file "app\routes\operator_fleet.py", line 367>:
367           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('cutover_id')

368           LOAD_CONST               2 ('str')

367           LOAD_CONST               3 ('body')

369           LOAD_CONST               4 ('Dict[str, Any]')

367           LOAD_CONST               5 ('return')

371           LOAD_CONST               4 ('Dict[str, Any]')

367           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object approve_second at 0x0000018C17E93990, file "app\routes\operator_fleet.py", line 366>:
 366           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0

 372           LOAD_GLOBAL              1 (_safe_cutover_id_path + NULL)
               LOAD_FAST_BORROW         0 (cutover_id)
               CALL                     1
               STORE_FAST               3 (cid)

 373           LOAD_GLOBAL              3 (_extract_actor + NULL)
               LOAD_FAST_BORROW         1 (body)
               CALL                     1
               STORE_FAST               4 (actor)

 374           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('approve_cutover_second',))
               IMPORT_NAME              2 (app.services.operator.cutover_approval)
               IMPORT_FROM              3 (approve_cutover_second)
               STORE_FAST               5 (approve_cutover_second)
               POP_TOP

 375           LOAD_FAST_BORROW         5 (approve_cutover_second)
               PUSH_NULL

 376           LOAD_FAST_BORROW         3 (cid)

 377           LOAD_FAST_BORROW         4 (actor)
               LOAD_CONST               2 ('actor_type')
               BINARY_OP               26 ([])

 378           LOAD_FAST_BORROW         4 (actor)
               LOAD_CONST               3 ('actor_id')
               BINARY_OP               26 ([])

 375           LOAD_CONST               4 (('cutover_id', 'actor_type', 'actor_id'))
               CALL_KW                  3
               STORE_FAST               6 (env)

 380           LOAD_FAST_BORROW         6 (env)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST               5 ('status')
               CALL                     1
               LOAD_CONST               6 ('failed')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       78 (to L4)
               NOT_TAKEN

 381           LOAD_FAST_BORROW         6 (env)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST               7 ('error_code')
               CALL                     1
               STORE_FAST               7 (code)

 382           LOAD_FAST_BORROW         7 (code)
               LOAD_CONST               8 ('cutover_not_found')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       14 (to L2)
               NOT_TAKEN

 383           LOAD_GLOBAL             11 (HTTPException + NULL)
               LOAD_CONST               9 (404)
               LOAD_FAST_BORROW         7 (code)
               LOAD_CONST              10 (('status_code', 'detail'))
               CALL_KW                  2
               RAISE_VARARGS            1

 384   L2:     LOAD_FAST_BORROW         7 (code)
               LOAD_CONST              11 ('self_second_approval_forbidden')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       14 (to L3)
               NOT_TAKEN

 385           LOAD_GLOBAL             11 (HTTPException + NULL)
               LOAD_CONST              12 (409)
               LOAD_FAST_BORROW         7 (code)
               LOAD_CONST              10 (('status_code', 'detail'))
               CALL_KW                  2
               RAISE_VARARGS            1

 386   L3:     LOAD_FAST_BORROW         7 (code)
               LOAD_CONST              18 (('invalid_arguments', 'invalid_status_transition'))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       14 (to L4)
               NOT_TAKEN

 387           LOAD_GLOBAL             11 (HTTPException + NULL)
               LOAD_CONST              13 (400)
               LOAD_FAST_BORROW         7 (code)
               LOAD_CONST              10 (('status_code', 'detail'))
               CALL_KW                  2
               RAISE_VARARGS            1

 389   L4:     LOAD_FAST_BORROW         6 (env)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST               5 ('status')
               CALL                     1
               LOAD_CONST              14 ('ok')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       55 (to L8)
               NOT_TAKEN

 390           LOAD_FAST_BORROW         6 (env)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST              15 ('row')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L7)
       L5:     NOT_TAKEN
       L6:     POP_TOP
               BUILD_MAP                0
       L7:     STORE_FAST               8 (row)

 391           LOAD_GLOBAL             13 (_invalidate_cache_for + NULL)
               LOAD_FAST_BORROW         8 (row)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST              16 ('brokerage_id')
               CALL                     1
               LOAD_CONST              17 ('cutover_second_approved')
               CALL                     2
               POP_TOP

 392   L8:     LOAD_FAST_BORROW         6 (env)
               RETURN_VALUE

  --   L9:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L5 -> L9 [0] lasti
  L6 to L9 -> L9 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025930, file "app\routes\operator_fleet.py", line 396>:
396           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('cutover_id')

397           LOAD_CONST               2 ('str')

396           LOAD_CONST               3 ('body')

398           LOAD_CONST               4 ('Dict[str, Any]')

396           LOAD_CONST               5 ('return')

400           LOAD_CONST               4 ('Dict[str, Any]')

396           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object reject at 0x0000018C17D520B0, file "app\routes\operator_fleet.py", line 395>:
 395           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0

 401           LOAD_GLOBAL              1 (_safe_cutover_id_path + NULL)
               LOAD_FAST_BORROW         0 (cutover_id)
               CALL                     1
               STORE_FAST               3 (cid)

 402           LOAD_GLOBAL              3 (_extract_actor + NULL)
               LOAD_FAST_BORROW         1 (body)
               CALL                     1
               STORE_FAST               4 (actor)

 403           LOAD_FAST_BORROW         1 (body)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               0 ('rationale')
               CALL                     1
               STORE_FAST               5 (rationale)

 404           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('reject_cutover',))
               IMPORT_NAME              3 (app.services.operator.cutover_approval)
               IMPORT_FROM              4 (reject_cutover)
               STORE_FAST               6 (reject_cutover)
               POP_TOP

 405           LOAD_FAST_BORROW         6 (reject_cutover)
               PUSH_NULL

 406           LOAD_FAST_BORROW         3 (cid)

 407           LOAD_FAST_BORROW         4 (actor)
               LOAD_CONST               2 ('actor_type')
               BINARY_OP               26 ([])

 408           LOAD_FAST_BORROW         4 (actor)
               LOAD_CONST               3 ('actor_id')
               BINARY_OP               26 ([])

 409           LOAD_FAST_BORROW         5 (rationale)

 405           LOAD_CONST               4 (('cutover_id', 'actor_type', 'actor_id', 'rationale'))
               CALL_KW                  4
               STORE_FAST               7 (env)

 411           LOAD_FAST_BORROW         7 (env)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               5 ('status')
               CALL                     1
               LOAD_CONST               6 ('failed')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       58 (to L3)
               NOT_TAKEN

 412           LOAD_FAST_BORROW         7 (env)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               7 ('error_code')
               CALL                     1
               STORE_FAST               8 (code)

 413           LOAD_FAST_BORROW         8 (code)
               LOAD_CONST               8 ('cutover_not_found')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       14 (to L2)
               NOT_TAKEN

 414           LOAD_GLOBAL             11 (HTTPException + NULL)
               LOAD_CONST               9 (404)
               LOAD_FAST_BORROW         8 (code)
               LOAD_CONST              10 (('status_code', 'detail'))
               CALL_KW                  2
               RAISE_VARARGS            1

 415   L2:     LOAD_FAST_BORROW         8 (code)
               LOAD_CONST              16 (('invalid_arguments', 'invalid_status_transition'))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       14 (to L3)
               NOT_TAKEN

 416           LOAD_GLOBAL             11 (HTTPException + NULL)
               LOAD_CONST              11 (400)
               LOAD_FAST_BORROW         8 (code)
               LOAD_CONST              10 (('status_code', 'detail'))
               CALL_KW                  2
               RAISE_VARARGS            1

 418   L3:     LOAD_FAST_BORROW         7 (env)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               5 ('status')
               CALL                     1
               LOAD_CONST              12 ('ok')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       55 (to L7)
               NOT_TAKEN

 419           LOAD_FAST_BORROW         7 (env)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              13 ('row')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L6)
       L4:     NOT_TAKEN
       L5:     POP_TOP
               BUILD_MAP                0
       L6:     STORE_FAST               9 (row)

 420           LOAD_GLOBAL             13 (_invalidate_cache_for + NULL)
               LOAD_FAST_BORROW         9 (row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              14 ('brokerage_id')
               CALL                     1
               LOAD_CONST              15 ('cutover_rejected')
               CALL                     2
               POP_TOP

 421   L7:     LOAD_FAST_BORROW         7 (env)
               RETURN_VALUE

  --   L8:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L8 [0] lasti
  L5 to L8 -> L8 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025330, file "app\routes\operator_fleet.py", line 429>:
429           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

430           LOAD_CONST               2 ('Optional[str]')

429           LOAD_CONST               3 ('limit')

431           LOAD_CONST               4 ('int')

429           LOAD_CONST               5 ('return')

433           LOAD_CONST               6 ('Dict[str, Any]')

429           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object list_daily_checklists at 0x0000018C18025630, file "app\routes\operator_fleet.py", line 428>:
 428           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0

 434           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('daily_ops_checklist_report',))
               IMPORT_NAME              0 (app.services.operator.daily_ops_checklist)
               IMPORT_FROM              1 (daily_ops_checklist_report)
               STORE_FAST               3 (daily_ops_checklist_report)
               POP_TOP

 437           LOAD_FAST_BORROW         3 (daily_ops_checklist_report)
               PUSH_NULL

 438           LOAD_FAST_BORROW         0 (brokerage_id)

 439           LOAD_FAST_BORROW         1 (limit)

 437           LOAD_CONST               2 (('brokerage_id', 'limit'))
               CALL_KW                  2
               RETURN_VALUE

  --   L2:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L2 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026730, file "app\routes\operator_fleet.py", line 444>:
444           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

445           LOAD_CONST               2 ('str')

444           LOAD_CONST               3 ('body')

446           LOAD_CONST               4 ('Dict[str, Any]')

444           LOAD_CONST               5 ('return')

448           LOAD_CONST               4 ('Dict[str, Any]')

444           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object complete_checklist at 0x0000018C17D8C200, file "app\routes\operator_fleet.py", line 443>:
 443           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0

 449           LOAD_GLOBAL              1 (_safe_brokerage_path + NULL)
               LOAD_FAST_BORROW         0 (brokerage_id)
               CALL                     1
               STORE_FAST               3 (bid)

 450           LOAD_GLOBAL              3 (_extract_actor + NULL)
               LOAD_FAST_BORROW         1 (body)
               CALL                     1
               STORE_FAST               4 (actor)

 451           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('complete_daily_ops_checklist',))
               IMPORT_NAME              2 (app.services.operator.daily_ops_checklist)
               IMPORT_FROM              3 (complete_daily_ops_checklist)
               STORE_FAST               5 (complete_daily_ops_checklist)
               POP_TOP

 454           LOAD_FAST_BORROW         5 (complete_daily_ops_checklist)
               PUSH_NULL

 455           LOAD_FAST_BORROW         3 (bid)

 456           LOAD_FAST_BORROW         1 (body)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST               2 ('run_date')
               CALL                     1

 457           LOAD_FAST_BORROW         4 (actor)
               LOAD_CONST               3 ('actor_type')
               BINARY_OP               26 ([])

 458           LOAD_FAST_BORROW         4 (actor)
               LOAD_CONST               4 ('actor_id')
               BINARY_OP               26 ([])

 459           LOAD_FAST_BORROW         1 (body)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST               5 ('queue_checked')
               LOAD_CONST               6 (False)
               CALL                     2

 460           LOAD_FAST_BORROW         1 (body)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST               7 ('callbacks_checked')
               LOAD_CONST               6 (False)
               CALL                     2

 461           LOAD_FAST_BORROW         1 (body)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST               8 ('bookings_checked')
               LOAD_CONST               6 (False)
               CALL                     2

 462           LOAD_FAST_BORROW         1 (body)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST               9 ('audit_checked')
               LOAD_CONST               6 (False)
               CALL                     2

 463           LOAD_FAST_BORROW         1 (body)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST              10 ('learning_checked')
               LOAD_CONST               6 (False)
               CALL                     2

 464           LOAD_FAST_BORROW         1 (body)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST              11 ('security_checked')
               LOAD_CONST               6 (False)
               CALL                     2

 465           LOAD_FAST_BORROW         1 (body)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST              12 ('incident_count')
               LOAD_SMALL_INT           0
               CALL                     2

 466           LOAD_FAST_BORROW         1 (body)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST              13 ('warning_count')
               LOAD_SMALL_INT           0
               CALL                     2

 467           LOAD_FAST_BORROW         1 (body)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST              14 ('notes')
               CALL                     1

 454           LOAD_CONST              15 (('brokerage_id', 'run_date', 'actor_type', 'actor_id', 'queue_checked', 'callbacks_checked', 'bookings_checked', 'audit_checked', 'learning_checked', 'security_checked', 'incident_count', 'warning_count', 'notes'))
               CALL_KW                 13
               STORE_FAST               6 (env)

 469           LOAD_FAST_BORROW         6 (env)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST              16 ('status')
               CALL                     1
               LOAD_CONST              17 ('failed')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       38 (to L2)
               NOT_TAKEN

 470           LOAD_FAST_BORROW         6 (env)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST              18 ('error_code')
               CALL                     1
               STORE_FAST               7 (code)

 471           LOAD_FAST_BORROW         7 (code)
               LOAD_CONST              19 ('invalid_actor')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       14 (to L2)
               NOT_TAKEN

 472           LOAD_GLOBAL             11 (HTTPException + NULL)
               LOAD_CONST              20 (400)
               LOAD_FAST_BORROW         7 (code)
               LOAD_CONST              21 (('status_code', 'detail'))
               CALL_KW                  2
               RAISE_VARARGS            1

 474   L2:     LOAD_FAST_BORROW         6 (env)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST              16 ('status')
               CALL                     1
               LOAD_CONST              22 ('ok')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       13 (to L3)
               NOT_TAKEN

 475           LOAD_GLOBAL             13 (_invalidate_cache_for + NULL)
               LOAD_FAST_BORROW         3 (bid)
               LOAD_CONST              23 ('daily_checklist_completed')
               CALL                     2
               POP_TOP

 476   L3:     LOAD_FAST_BORROW         6 (env)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti
```
