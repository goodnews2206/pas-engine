# routes/tenant_portal

- **pyc:** `app\routes\__pycache__\tenant_portal.cpython-314.pyc`
- **expected source path (absent):** `app\routes/tenant_portal.py`
- **co_filename (from bytecode):** `app\routes\tenant_portal.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** routes

## Module docstring

```
PAS174 — Tenant visibility routes.

Bounded, brokerage-scoped read surfaces for the tenant-side
portal. Mounted at ``/tenant`` (distinct from the existing
``/portal`` surface so the addition is auditable). Auth:
X-API-Key header → ``require_brokerage`` (same model as
``app/routes/portal.py``).

Doctrine:

* **Tenant-auth only.** No admin path here; admins use
  ``/admin`` and ``/ops``.
* **Brokerage-scoped only.** Every helper unpacks the
  brokerage_id from the resolved brokerage dict; there is no
  query-string `brokerage_id` parameter, so cross-brokerage
  leakage is structurally impossible.
* **No cross-tenant visibility.** Even a tenant who guesses
  another brokerage's id cannot reach the surface — the
  query takes the brokerage from auth, not from the URL.
* **Bounded responses.** Closed-shape envelopes, presence-
  only booleans, count surfaces. No transcripts, no raw
  payloads, no audit-log internals, no operator notes.
* **Defensive forbidden-field scan.** Every response is
  walked for any forbidden field key; any leak collapses
  to a structural error.
* **NEVER raises.** Failures flip the envelope to
  ``status="failed"`` / ``"skipped"``.

Routes (all GET):

    GET /tenant/status
    GET /tenant/launch-readiness
    GET /tenant/integrations
    GET /tenant/callback-summary
```

## Imports

`APIRouter`, `Any`, `BaseModel`, `Depends`, `Dict`, `Field`, `HTTPException`, `Header`, `Optional`, `__future__`, `acknowledge_tenant_audit_entry`, `annotations`, `app.db.brokerage_store`, `app.services.operator.merkle_inclusion_proofs`, `app.services.tenant.tenant_audit_ack_store`, `app.services.tenant.tenant_audit_dashboard`, `app.services.tenant.tenant_visibility_service`, `fastapi`, `get_brokerage_by_api_key`, `list_tenant_audit_acknowledgements`, `logging`, `proof_for_audit_entry`, `pydantic`, `record_tenant_audit_acknowledgement`, `tenant_audit_dashboard_summary`, `tenant_audit_history`, `tenant_callback_summary`, `tenant_chain_status_summary`, `tenant_integration_posture`, `tenant_launch_readiness`, `tenant_status`, `tenant_verification_history_summary`, `typing`, `verify_inclusion_proof`

## Classes

`TenantAuditAcknowledgeRequest`

## Functions / methods

`__annotate__`, `_final_envelope`, `_scan_for_forbidden`, `require_brokerage`, `tenant_audit_acknowledge_route`, `tenant_audit_acknowledgements_route`, `tenant_audit_chain_status_route`, `tenant_audit_dashboard_route`, `tenant_audit_proof_route`, `tenant_audit_route`, `tenant_audit_verification_history_route`, `tenant_audit_window_acknowledge_route`, `tenant_callback_summary_route`, `tenant_integrations_route`, `tenant_launch_readiness_route`, `tenant_status_route`

## Env-key candidates

`MERKLE_ROOT_ACKNOWLEDGED`, `TENANT`

## String constants (redacted where noted)

- '\nPAS174 — Tenant visibility routes.\n\nBounded, brokerage-scoped read surfaces for the tenant-side\nportal. Mounted at ``/tenant`` (distinct from the existing\n``/portal`` surface so the addition is auditable). Auth:\nX-API-Key header → ``require_brokerage`` (same model as\n``app/routes/portal.py``).\n\nDoctrine:\n\n* **Tenant-auth only.** No admin path here; admins use\n  ``/admin`` and ``/ops``.\n* **Brokerage-scoped only.** Every helper unpacks the\n  brokerage_id from the resolved brokerage dict; there is no\n  query-string `brokerage_id` parameter, so cross-brokerage\n  leakage is structurally impossible.\n* **No cross-tenant visibility.** Even a tenant who guesses\n  another brokerage\'s id cannot reach the surface — the\n  query takes the brokerage from auth, not from the URL.\n* **Bounded responses.** Closed-shape envelopes, presence-\n  only booleans, count surfaces. No transcripts, no raw\n  payloads, no audit-log internals, no operator notes.\n* **Defensive forbidden-field scan.** Every response is\n  walked for any forbidden field key; any leak collapses\n  to a structural error.\n* **NEVER raises.** Failures flip the envelope to\n  ``status="failed"`` / ``"skipped"``.\n\nRoutes (all GET):\n\n    GET /tenant/status\n    GET /tenant/launch-readiness\n    GET /tenant/integrations\n    GET /tenant/callback-summary\n'
- 'pas.tenant.portal'
- '/status'
- '/launch-readiness'
- '/integrations'
- 'TenantAuditAcknowledgeRequest'
- '/audit/{entry_id}/acknowledge'
- '/audit/dashboard'
- '/audit/chain-status'
- '/audit/verification-history'
- '/audit/acknowledgements'
- '/audit/windows/{merkle_root_id}/acknowledge'
- '/audit/{entry_id}/proof'
- '/audit'
- '/callback-summary'
- 'x_api_key'
- 'str'
- 'Authenticate a brokerage client by API key. Returns the\nfull brokerage record. Rejects the demo brokerage.'
- 'demo'
- 'Invalid API key'
- 'envelope'
- 'Any'
- 'return'
- 'Optional[str]'
- 'obj'
- 'env'
- 'Dict[str, Any]'
- 'surface'
- 'tenant_portal surface='
- ' collapsed — forbidden field key leaked'
- 'status'
- 'failed'
- 'error_code'
- 'tenant_envelope_forbidden_field'
- 'warnings'
- 'Tenant-safe profile snapshot — onboarding_status +\npilot_stage + structural profile fields.'
- 'tenant.status'
- 'brokerage_id'
- 'payload'
- 'tenant_status_route error type='
- 'unexpected:'
- 'Tenant-safe launch-readiness summary — booleans + counts\nonly. NEVER returns the warning / error tokens themselves.'
- 'tenant.launch_readiness'
- 'tenant_launch_readiness_route error type='
- 'Tenant-safe integration posture — Twilio / Slack / Cal.com /\nencryption posture summary.'
- 'tenant.integrations'
- 'tenant_integrations_route error type='
- 'PAS176 — bounded payload for the tenant audit ack endpoint.\n\nAll fields optional except as noted. NEVER carries PII —\nnotes_token is a structural identifier (alphanumeric + dash\n+ underscore) up to 200 characters; the service layer\nrejects anything else.'
- 'actor_token'
- 'notes_token'
- 'entry_id'
- 'body'
- 'Optional[TenantAuditAcknowledgeRequest]'
- 'PAS176 — Tenant-side acknowledgement of an audit entry.\n\nBounded write: the tenant records that they SAW the audit\nstate. The audit row itself is NEVER mutated; the tenant\nCANNOT mark the chain valid manually; the tenant CANNOT\nwrite into ``pas_operator_actions_log``. This endpoint\nwrites to a separate process-local registry (durable\nbacking deferred to PAS177).\n'
- 'tenant.audit_acknowledge'
- 'tenant_audit_acknowledge_route error type='
- 'PAS178 — Tenant-safe audit dashboard summary.\n\nCombines chain status + verification history + ack counts +\nMerkle window count into a single bounded envelope. Closed\nallow-list of fields; ``action_required`` flag tells the\ntenant whether the operator owes them attention.\n'
- 'tenant.audit_dashboard'
- 'tenant_audit_dashboard_route error type='
- 'PAS178 — Tenant-safe chain status summary.'
- 'tenant.audit_chain_status'
- 'tenant_audit_chain_status_route error type='
- 'PAS178 — Tenant-safe verification history summary.'
- 'tenant.audit_verification_history'
- 'tenant_audit_verification_history_route error type='
- 'limit'
- 'int'
- 'acknowledgement_type'
- "PAS177 — Tenant-safe read-only list of the brokerage's\ndurable audit acknowledgements. Brokerage-scoped via auth.\n\nReturns the closed-shape envelope from the\n``tenant_audit_ack_store.list_tenant_audit_acknowledgements``\nhelper, structurally projected; the route's defensive\nforbidden-key scan runs as the final guard."
- 'rows'
- 'acknowledgement_id'
- 'audit_entry_id'
- 'merkle_root_id'
- 'acknowledged_at'
- 'actor_id'
- 'tenant.audit_acknowledgements'
- 'count'
- 'filter_ack_type'
- 'tenant_audit_acknowledgements_route error type='
- 'PAS177 — Tenant-side acknowledgement of a Merkle root\nwindow. Records that the tenant saw the audit chain state\nfor the given window without mutating any audit row.\n\nBounded payload mirrors the per-entry ack endpoint.\nBrokerage-scoped via auth. Append-only at the durable\nstore layer; idempotent on repeated submit.'
- 'MERKLE_ROOT_ACKNOWLEDGED'
- 'TENANT'
- 'ack_row'
- 'tenant.audit_window_acknowledge'
- 'duplicate'
- 'tenant_audit_window_acknowledge_route error type='
- 'PAS177 — Tenant-safe Merkle inclusion proof for a\nspecific audit entry. Returns the structural proof + a\ndeterministic self-verification verdict.\n\nRead-only. NEVER mutates audit rows. NEVER returns PII /\nsecrets / raw payload.'
- 'tenant.audit_proof'
- 'proof'
- 'window_start'
- 'window_end'
- 'self_verification'
- 'valid'
- 'tenant_audit_proof_route error type='
- "PAS175 — Tenant-safe read-only audit history. Returns\nthe brokerage's own audit rows projected against the\ntenant allow-list (entry_id, occurred_at, action, status,\ntarget_type, structural metadata). NEVER returns actor_id,\noperator notes, or operator-side metadata internals.\n\nRead-only. No POST / PATCH / DELETE counterpart exists."
- 'tenant.audit_history'
- 'tenant_audit_route error type='
- 'Tenant-safe callback summary — due / overdue / pending\ncounts only. NEVER returns callback_ids or per-row payload.'
- 'tenant.callback_summary'
- 'tenant_callback_summary_route error type='

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS174 — Tenant visibility routes.\n\nBounded, brokerage-scoped read surfaces for the tenant-side\nportal. Mounted at ``/tenant`` (distinct from the existing\n``/portal`` surface so the addition is auditable). Auth:\nX-API-Key header → ``require_brokerage`` (same model as\n``app/routes/portal.py``).\n\nDoctrine:\n\n* **Tenant-auth only.** No admin path here; admins use\n  ``/admin`` and ``/ops``.\n* **Brokerage-scoped only.** Every helper unpacks the\n  brokerage_id from the resolved brokerage dict; there is no\n  query-string `brokerage_id` parameter, so cross-brokerage\n  leakage is structurally impossible.\n* **No cross-tenant visibility.** Even a tenant who guesses\n  another brokerage\'s id cannot reach the surface — the\n  query takes the brokerage from auth, not from the URL.\n* **Bounded responses.** Closed-shape envelopes, presence-\n  only booleans, count surfaces. No transcripts, no raw\n  payloads, no audit-log internals, no operator notes.\n* **Defensive forbidden-field scan.** Every response is\n  walked for any forbidden field key; any leak collapses\n  to a structural error.\n* **NEVER raises.** Failures flip the envelope to\n  ``status="failed"`` / ``"skipped"``.\n\nRoutes (all GET):\n\n    GET /tenant/status\n    GET /tenant/launch-readiness\n    GET /tenant/integrations\n    GET /tenant/callback-summary\n')
              STORE_NAME               0 (__doc__)

 38           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 40           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 41           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('Any', 'Dict', 'Optional'))
              IMPORT_NAME              4 (typing)
              IMPORT_FROM              5 (Any)
              STORE_NAME               5 (Any)
              IMPORT_FROM              6 (Dict)
              STORE_NAME               6 (Dict)
              IMPORT_FROM              7 (Optional)
              STORE_NAME               7 (Optional)
              POP_TOP

 43           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('APIRouter', 'Depends', 'HTTPException', 'Header'))
              IMPORT_NAME              8 (fastapi)
              IMPORT_FROM              9 (APIRouter)
              STORE_NAME               9 (APIRouter)
              IMPORT_FROM             10 (Depends)
              STORE_NAME              10 (Depends)
              IMPORT_FROM             11 (HTTPException)
              STORE_NAME              11 (HTTPException)
              IMPORT_FROM             12 (Header)
              STORE_NAME              12 (Header)
              POP_TOP

 45           LOAD_SMALL_INT           0
              LOAD_CONST               5 (('get_brokerage_by_api_key',))
              IMPORT_NAME             13 (app.db.brokerage_store)
              IMPORT_FROM             14 (get_brokerage_by_api_key)
              STORE_NAME              14 (get_brokerage_by_api_key)
              POP_TOP

 48           LOAD_NAME                9 (APIRouter)
              PUSH_NULL
              CALL                     0
              STORE_NAME              15 (router)

 49           LOAD_NAME                3 (logging)
              LOAD_ATTR               32 (getLogger)
              PUSH_NULL
              LOAD_CONST               6 ('pas.tenant.portal')
              CALL                     1
              STORE_NAME              17 (logger)

 56           LOAD_NAME               12 (Header)
              PUSH_NULL
              LOAD_CONST               7 (Ellipsis)
              CALL                     1
              BUILD_TUPLE              1
              LOAD_CONST               8 (<code object __annotate__ at 0x0000018C17FA2D30, file "app\routes\tenant_portal.py", line 56>)
              MAKE_FUNCTION
              LOAD_CONST               9 (<code object require_brokerage at 0x0000018C17FE1A70, file "app\routes\tenant_portal.py", line 56>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              18 (require_brokerage)

 69           LOAD_CONST              53 (('phone', 'email', 'name_token', 'raw_payload', 'raw_email', 'raw_body', 'transcript', 'summary_text', 'secret', 'signature', 'dedupe_key', 'callback_notes', 'operator_notes', 'audit', 'action_id', 'actor_id', 'env_value', 'env_values', 'slack_internal', 'memory_candidate'))
              STORE_NAME              19 (_FORBIDDEN_TENANT_FIELDS)

 82           LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA3A50, file "app\routes\tenant_portal.py", line 82>)
              MAKE_FUNCTION
              LOAD_CONST              11 (<code object _scan_for_forbidden at 0x0000018C18025C30, file "app\routes\tenant_portal.py", line 82>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              20 (_scan_for_forbidden)

106           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C18025030, file "app\routes\tenant_portal.py", line 106>)
              MAKE_FUNCTION
              LOAD_CONST              13 (<code object _final_envelope at 0x0000018C17FE1290, file "app\routes\tenant_portal.py", line 106>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              21 (_final_envelope)

126           LOAD_NAME               15 (router)
              LOAD_ATTR               45 (get + NULL|self)
              LOAD_CONST              14 ('/status')
              CALL                     1

128           LOAD_NAME               10 (Depends)
              PUSH_NULL
              LOAD_NAME               18 (require_brokerage)
              CALL                     1

127           BUILD_TUPLE              1
              LOAD_CONST              15 (<code object __annotate__ at 0x0000018C17FA3000, file "app\routes\tenant_portal.py", line 127>)
              MAKE_FUNCTION
              LOAD_CONST              16 (<code object tenant_status_route at 0x0000018C17F84C80, file "app\routes\tenant_portal.py", line 126>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

126           CALL                     0

127           STORE_NAME              23 (tenant_status_route)

156           LOAD_NAME               15 (router)
              LOAD_ATTR               45 (get + NULL|self)
              LOAD_CONST              17 ('/launch-readiness')
              CALL                     1

158           LOAD_NAME               10 (Depends)
              PUSH_NULL
              LOAD_NAME               18 (require_brokerage)
              CALL                     1

157           BUILD_TUPLE              1
              LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA2C40, file "app\routes\tenant_portal.py", line 157>)
              MAKE_FUNCTION
              LOAD_CONST              19 (<code object tenant_launch_readiness_route at 0x0000018C17D81580, file "app\routes\tenant_portal.py", line 156>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

156           CALL                     0

157           STORE_NAME              24 (tenant_launch_readiness_route)

189           LOAD_NAME               15 (router)
              LOAD_ATTR               45 (get + NULL|self)
              LOAD_CONST              20 ('/integrations')
              CALL                     1

191           LOAD_NAME               10 (Depends)
              PUSH_NULL
              LOAD_NAME               18 (require_brokerage)
              CALL                     1

190           BUILD_TUPLE              1
              LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA3C30, file "app\routes\tenant_portal.py", line 190>)
              MAKE_FUNCTION
              LOAD_CONST              22 (<code object tenant_integrations_route at 0x0000018C17D6DFC0, file "app\routes\tenant_portal.py", line 189>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

189           CALL                     0

190           STORE_NAME              25 (tenant_integrations_route)

221           LOAD_SMALL_INT           0
              LOAD_CONST              23 (('BaseModel', 'Field'))
              IMPORT_NAME             26 (pydantic)
              IMPORT_FROM             27 (BaseModel)
              STORE_NAME              27 (BaseModel)
              IMPORT_FROM             28 (Field)
              STORE_NAME              29 (_PydField)
              POP_TOP

224           LOAD_BUILD_CLASS
              PUSH_NULL
              LOAD_CONST              24 (<code object TenantAuditAcknowledgeRequest at 0x0000018C1802C620, file "app\routes\tenant_portal.py", line 224>)
              MAKE_FUNCTION
              LOAD_CONST              25 ('TenantAuditAcknowledgeRequest')
              LOAD_NAME               27 (BaseModel)
              CALL                     3
              STORE_NAME              30 (TenantAuditAcknowledgeRequest)

235           LOAD_NAME               15 (router)
              LOAD_ATTR               63 (post + NULL|self)
              LOAD_CONST              26 ('/audit/{entry_id}/acknowledge')
              CALL                     1

238           LOAD_CONST               2 (None)

239           LOAD_NAME               10 (Depends)
              PUSH_NULL
              LOAD_NAME               18 (require_brokerage)
              CALL                     1

236           BUILD_TUPLE              2
              LOAD_CONST              27 (<code object __annotate__ at 0x0000018C18026430, file "app\routes\tenant_portal.py", line 236>)
              MAKE_FUNCTION
              LOAD_CONST              28 (<code object tenant_audit_acknowledge_route at 0x0000018C17F77850, file "app\routes\tenant_portal.py", line 235>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

235           CALL                     0

236           STORE_NAME              32 (tenant_audit_acknowledge_route)

282           LOAD_NAME               15 (router)
              LOAD_ATTR               45 (get + NULL|self)
              LOAD_CONST              29 ('/audit/dashboard')
              CALL                     1

284           LOAD_NAME               10 (Depends)
              PUSH_NULL
              LOAD_NAME               18 (require_brokerage)
              CALL                     1

283           BUILD_TUPLE              1
              LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA3690, file "app\routes\tenant_portal.py", line 283>)
              MAKE_FUNCTION
              LOAD_CONST              31 (<code object tenant_audit_dashboard_route at 0x0000018C17ED9360, file "app\routes\tenant_portal.py", line 282>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

282           CALL                     0

283           STORE_NAME              33 (tenant_audit_dashboard_route)

319           LOAD_NAME               15 (router)
              LOAD_ATTR               45 (get + NULL|self)
              LOAD_CONST              32 ('/audit/chain-status')
              CALL                     1

321           LOAD_NAME               10 (Depends)
              PUSH_NULL
              LOAD_NAME               18 (require_brokerage)
              CALL                     1

320           BUILD_TUPLE              1
              LOAD_CONST              33 (<code object __annotate__ at 0x0000018C17FA3870, file "app\routes\tenant_portal.py", line 320>)
              MAKE_FUNCTION
              LOAD_CONST              34 (<code object tenant_audit_chain_status_route at 0x0000018C17ED9600, file "app\routes\tenant_portal.py", line 319>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

319           CALL                     0

320           STORE_NAME              34 (tenant_audit_chain_status_route)

350           LOAD_NAME               15 (router)
              LOAD_ATTR               45 (get + NULL|self)
              LOAD_CONST              35 ('/audit/verification-history')
              CALL                     1

352           LOAD_NAME               10 (Depends)
              PUSH_NULL
              LOAD_NAME               18 (require_brokerage)
              CALL                     1

351           BUILD_TUPLE              1
              LOAD_CONST              36 (<code object __annotate__ at 0x0000018C17FA33C0, file "app\routes\tenant_portal.py", line 351>)
              MAKE_FUNCTION
              LOAD_CONST              37 (<code object tenant_audit_verification_history_route at 0x0000018C17D7C5B0, file "app\routes\tenant_portal.py", line 350>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

350           CALL                     0

351           STORE_NAME              35 (tenant_audit_verification_history_route)

382           LOAD_NAME               15 (router)
              LOAD_ATTR               45 (get + NULL|self)
              LOAD_CONST              38 ('/audit/acknowledgements')
              CALL                     1

384           LOAD_SMALL_INT          50

385           LOAD_CONST               2 (None)

386           LOAD_NAME               10 (Depends)
              PUSH_NULL
              LOAD_NAME               18 (require_brokerage)
              CALL                     1

383           BUILD_TUPLE              3
              LOAD_CONST              39 (<code object __annotate__ at 0x0000018C18026230, file "app\routes\tenant_portal.py", line 383>)
              MAKE_FUNCTION
              LOAD_CONST              40 (<code object tenant_audit_acknowledgements_route at 0x0000018C17E953A0, file "app\routes\tenant_portal.py", line 382>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

382           CALL                     0

383           STORE_NAME              36 (tenant_audit_acknowledgements_route)

450           LOAD_NAME               15 (router)
              LOAD_ATTR               63 (post + NULL|self)
              LOAD_CONST              41 ('/audit/windows/{merkle_root_id}/acknowledge')
              CALL                     1

453           LOAD_CONST               2 (None)

454           LOAD_NAME               10 (Depends)
              PUSH_NULL
              LOAD_NAME               18 (require_brokerage)
              CALL                     1

451           BUILD_TUPLE              2
              LOAD_CONST              42 (<code object __annotate__ at 0x0000018C18025D30, file "app\routes\tenant_portal.py", line 451>)
              MAKE_FUNCTION
              LOAD_CONST              43 (<code object tenant_audit_window_acknowledge_route at 0x0000018C17D51630, file "app\routes\tenant_portal.py", line 450>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

450           CALL                     0

451           STORE_NAME              37 (tenant_audit_window_acknowledge_route)

507           LOAD_NAME               15 (router)
              LOAD_ATTR               45 (get + NULL|self)
              LOAD_CONST              44 ('/audit/{entry_id}/proof')
              CALL                     1

510           LOAD_NAME               10 (Depends)
              PUSH_NULL
              LOAD_NAME               18 (require_brokerage)
              CALL                     1

508           BUILD_TUPLE              1
              LOAD_CONST              45 (<code object __annotate__ at 0x0000018C17FA35A0, file "app\routes\tenant_portal.py", line 508>)
              MAKE_FUNCTION
              LOAD_CONST              46 (<code object tenant_audit_proof_route at 0x0000018C17D51ED0, file "app\routes\tenant_portal.py", line 507>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

507           CALL                     0

508           STORE_NAME              38 (tenant_audit_proof_route)

576           LOAD_NAME               15 (router)
              LOAD_ATTR               45 (get + NULL|self)
              LOAD_CONST              47 ('/audit')
              CALL                     1

578           LOAD_SMALL_INT          50

579           LOAD_NAME               10 (Depends)
              PUSH_NULL
              LOAD_NAME               18 (require_brokerage)
              CALL                     1

577           BUILD_TUPLE              2
              LOAD_CONST              48 (<code object __annotate__ at 0x0000018C17FA3D20, file "app\routes\tenant_portal.py", line 577>)
              MAKE_FUNCTION
              LOAD_CONST              49 (<code object tenant_audit_route at 0x0000018C17EE1CC0, file "app\routes\tenant_portal.py", line 576>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

576           CALL                     0

577           STORE_NAME              39 (tenant_audit_route)

624           LOAD_NAME               15 (router)
              LOAD_ATTR               45 (get + NULL|self)
              LOAD_CONST              50 ('/callback-summary')
              CALL                     1

626           LOAD_NAME               10 (Depends)
              PUSH_NULL
              LOAD_NAME               18 (require_brokerage)
              CALL                     1

625           BUILD_TUPLE              1
              LOAD_CONST              51 (<code object __annotate__ at 0x0000018C17FA1D40, file "app\routes\tenant_portal.py", line 625>)
              MAKE_FUNCTION
              LOAD_CONST              52 (<code object tenant_callback_summary_route at 0x0000018C17D7CD90, file "app\routes\tenant_portal.py", line 624>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)

624           CALL                     0

625           STORE_NAME              40 (tenant_callback_summary_route)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "app\routes\tenant_portal.py", line 56>:
 56           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('x_api_key')
              LOAD_CONST               2 ('str')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object require_brokerage at 0x0000018C17FE1A70, file "app\routes\tenant_portal.py", line 56>:
 56           RESUME                   0

 59           LOAD_GLOBAL              1 (get_brokerage_by_api_key + NULL)
              LOAD_FAST_BORROW         0 (x_api_key)
              CALL                     1
              STORE_FAST               1 (brokerage)

 60           LOAD_FAST_BORROW         1 (brokerage)
              TO_BOOL
              POP_JUMP_IF_FALSE       23 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (brokerage)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               1 ('id')
              CALL                     1
              LOAD_CONST               2 ('demo')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE       14 (to L2)
              NOT_TAKEN

 61   L1:     LOAD_GLOBAL              5 (HTTPException + NULL)
              LOAD_CONST               3 (401)
              LOAD_CONST               4 ('Invalid API key')
              LOAD_CONST               5 (('status_code', 'detail'))
              CALL_KW                  2
              RAISE_VARARGS            1

 62   L2:     LOAD_FAST_BORROW         1 (brokerage)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "app\routes\tenant_portal.py", line 82>:
 82           RESUME                   0
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

Disassembly of <code object _scan_for_forbidden at 0x0000018C18025C30, file "app\routes\tenant_portal.py", line 82>:
  --           MAKE_CELL                1 (walk)

  82           RESUME                   0

  83           LOAD_CONST               0 (<code object __annotate__ at 0x0000018C17FA2A60, file "app\routes\tenant_portal.py", line 83>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         1 (walk)
               BUILD_TUPLE              1
               LOAD_CONST               1 (<code object walk at 0x0000018C17CC2460, file "app\routes\tenant_portal.py", line 83>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_DEREF              1 (walk)

 103           LOAD_DEREF               1 (walk)
               PUSH_NULL
               LOAD_FAST_BORROW         0 (envelope)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "app\routes\tenant_portal.py", line 83>:
 83           RESUME                   0
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

Disassembly of <code object walk at 0x0000018C17CC2460, file "app\routes\tenant_portal.py", line 83>:
  --            COPY_FREE_VARS           1

  83            RESUME                   0

  84            NOP

  85    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      111 (to L16)
        L2:     NOT_TAKEN

  86    L3:     LOAD_FAST_BORROW         0 (obj)
                LOAD_ATTR                5 (items + NULL|self)
                CALL                     0
                GET_ITER
        L4:     FOR_ITER                88 (to L14)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   18 (k, v)

  87            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (k)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       42 (to L10)
                NOT_TAKEN

  88            LOAD_FAST_BORROW         1 (k)
                LOAD_ATTR                9 (lower + NULL|self)
                CALL                     0
                STORE_FAST               3 (kl)

  89            LOAD_GLOBAL             10 (_FORBIDDEN_TENANT_FIELDS)
                GET_ITER
        L5:     FOR_ITER                15 (to L9)
                STORE_FAST               4 (tok)

  90            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, kl)
                CONTAINS_OP              0 (in)
        L6:     POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L5)

  91    L7:     LOAD_FAST_BORROW         4 (tok)
                SWAP                     2
                POP_TOP
                SWAP                     2
                POP_TOP
        L8:     RETURN_VALUE

  89    L9:     END_FOR
                POP_ITER

  92   L10:     LOAD_DEREF               6 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                STORE_FAST               5 (sub)

  93            LOAD_FAST_BORROW         5 (sub)
                TO_BOOL
       L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           86 (to L4)

  94   L12:     LOAD_FAST_BORROW         5 (sub)
                SWAP                     2
                POP_TOP
       L13:     RETURN_VALUE

  86   L14:     END_FOR
                POP_ITER

 102   L15:     LOAD_CONST               0 (None)
                RETURN_VALUE

  95   L16:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL             12 (list)
                LOAD_GLOBAL             14 (tuple)
                BUILD_TUPLE              2
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       30 (to L22)
                NOT_TAKEN

  96            LOAD_FAST_BORROW         0 (obj)
                GET_ITER
       L17:     FOR_ITER                23 (to L21)
                STORE_FAST               2 (v)

  97            LOAD_DEREF               6 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                STORE_FAST               5 (sub)

  98            LOAD_FAST_BORROW         5 (sub)
                TO_BOOL
       L18:     POP_JUMP_IF_TRUE         3 (to L19)
                NOT_TAKEN
                JUMP_BACKWARD           21 (to L17)

  99   L19:     LOAD_FAST_BORROW         5 (sub)
                SWAP                     2
                POP_TOP
       L20:     RETURN_VALUE

  96   L21:     END_FOR
                POP_ITER

 102   L22:     LOAD_CONST               0 (None)
                RETURN_VALUE

  --   L23:     PUSH_EXC_INFO

 100            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L25)
                NOT_TAKEN
                POP_TOP

 101   L24:     POP_EXCEPT
                LOAD_CONST               0 (None)
                RETURN_VALUE

 100   L25:     RERAISE                  0

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

Disassembly of <code object __annotate__ at 0x0000018C18025030, file "app\routes\tenant_portal.py", line 106>:
106           RESUME                   0
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

Disassembly of <code object _final_envelope at 0x0000018C17FE1290, file "app\routes\tenant_portal.py", line 106>:
106           RESUME                   0

107           LOAD_GLOBAL              1 (_scan_for_forbidden + NULL)
              LOAD_FAST_BORROW         0 (env)
              CALL                     1
              STORE_FAST               2 (leak)

108           LOAD_FAST_BORROW         2 (leak)
              TO_BOOL
              POP_JUMP_IF_FALSE       37 (to L1)
              NOT_TAKEN

109           LOAD_GLOBAL              2 (logger)
              LOAD_ATTR                5 (warning + NULL|self)

110           LOAD_CONST               0 ('tenant_portal surface=')
              LOAD_FAST_BORROW         1 (surface)
              FORMAT_SIMPLE
              LOAD_CONST               1 (' collapsed — forbidden field key leaked')
              BUILD_STRING             3

109           CALL                     1
              POP_TOP

114           LOAD_CONST               2 ('status')
              LOAD_CONST               3 ('failed')

115           LOAD_CONST               4 ('surface')
              LOAD_FAST_BORROW         1 (surface)

116           LOAD_CONST               5 ('error_code')
              LOAD_CONST               6 ('tenant_envelope_forbidden_field')

117           LOAD_CONST               7 ('warnings')
              LOAD_CONST               6 ('tenant_envelope_forbidden_field')
              BUILD_LIST               1

113           BUILD_MAP                4
              RETURN_VALUE

119   L1:     LOAD_FAST_BORROW         0 (env)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3000, file "app\routes\tenant_portal.py", line 127>:
127           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')

129           LOAD_CONST               2 ('Dict[str, Any]')

127           BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object tenant_status_route at 0x0000018C17F84C80, file "app\routes\tenant_portal.py", line 126>:
 126            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 132            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('tenant_status',))
                IMPORT_NAME              0 (app.services.tenant.tenant_visibility_service)
                IMPORT_FROM              1 (tenant_status)
                STORE_FAST               1 (tenant_status)
                POP_TOP

 133    L2:     NOP

 134    L3:     LOAD_FAST_BORROW         1 (tenant_status)
                PUSH_NULL
                LOAD_FAST_BORROW         0 (brokerage)
                CALL                     1
                STORE_FAST               2 (env)

 136            LOAD_CONST               2 ('status')
                LOAD_FAST_BORROW         2 (env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               2 ('status')
                CALL                     1

 137            LOAD_CONST               3 ('surface')
                LOAD_CONST               4 ('tenant.status')

 138            LOAD_CONST               5 ('brokerage_id')
                LOAD_FAST_BORROW         2 (env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               5 ('brokerage_id')
                CALL                     1

 139            LOAD_CONST               6 ('payload')
                LOAD_FAST_BORROW         2 (env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               6 ('payload')
                CALL                     1

 140            LOAD_CONST               7 ('warnings')
                LOAD_FAST_BORROW         2 (env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               7 ('warnings')
                CALL                     1

 141            LOAD_CONST               8 ('error_code')
                LOAD_FAST_BORROW         2 (env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               8 ('error_code')
                CALL                     1

 135            BUILD_MAP                6
                STORE_FAST               3 (out)

 153    L4:     LOAD_GLOBAL             17 (_final_envelope + NULL)
                LOAD_FAST_BORROW         3 (out)
                LOAD_CONST               4 ('tenant.status')
                LOAD_CONST              13 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --    L5:     PUSH_EXC_INFO

 143            LOAD_GLOBAL              6 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L9)
                NOT_TAKEN
                STORE_FAST               4 (e)

 144    L6:     LOAD_GLOBAL              8 (logger)
                LOAD_ATTR               11 (warning + NULL|self)

 145            LOAD_CONST               9 ('tenant_status_route error type=')
                LOAD_GLOBAL             13 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               14 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 144            CALL                     1
                POP_TOP

 148            LOAD_CONST               2 ('status')
                LOAD_CONST              10 ('failed')

 149            LOAD_CONST               3 ('surface')
                LOAD_CONST               4 ('tenant.status')

 150            LOAD_CONST               8 ('error_code')
                LOAD_CONST              11 ('unexpected:')
                LOAD_GLOBAL             13 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               14 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 151            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 147            BUILD_MAP                4
                STORE_FAST               3 (out)
        L7:     POP_EXCEPT
                LOAD_CONST              12 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                JUMP_BACKWARD_NO_INTERRUPT 104 (to L4)

  --    L8:     LOAD_CONST              12 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RERAISE                  1

 143    L9:     RERAISE                  0

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

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "app\routes\tenant_portal.py", line 157>:
157           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')

159           LOAD_CONST               2 ('Dict[str, Any]')

157           BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object tenant_launch_readiness_route at 0x0000018C17D81580, file "app\routes\tenant_portal.py", line 156>:
 156            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 162            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('tenant_launch_readiness',))
                IMPORT_NAME              0 (app.services.tenant.tenant_visibility_service)
                IMPORT_FROM              1 (tenant_launch_readiness)
                STORE_FAST               1 (tenant_launch_readiness)
                POP_TOP

 165    L2:     NOP

 166    L3:     LOAD_FAST_BORROW         1 (tenant_launch_readiness)
                PUSH_NULL
                LOAD_FAST_BORROW         0 (brokerage)
                CALL                     1
                STORE_FAST               2 (env)

 168            LOAD_CONST               2 ('status')
                LOAD_FAST_BORROW         2 (env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               2 ('status')
                CALL                     1

 169            LOAD_CONST               3 ('surface')
                LOAD_CONST               4 ('tenant.launch_readiness')

 170            LOAD_CONST               5 ('brokerage_id')
                LOAD_FAST_BORROW         2 (env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               5 ('brokerage_id')
                CALL                     1

 171            LOAD_CONST               6 ('payload')
                LOAD_FAST_BORROW         2 (env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               6 ('payload')
                CALL                     1

 172            LOAD_CONST               7 ('warnings')
                LOAD_FAST_BORROW         2 (env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               7 ('warnings')
                CALL                     1

 173            LOAD_CONST               8 ('error_code')
                LOAD_FAST_BORROW         2 (env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               8 ('error_code')
                CALL                     1

 167            BUILD_MAP                6
                STORE_FAST               3 (out)

 186    L4:     LOAD_GLOBAL             17 (_final_envelope + NULL)
                LOAD_FAST_BORROW         3 (out)
                LOAD_CONST               4 ('tenant.launch_readiness')
                LOAD_CONST              13 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --    L5:     PUSH_EXC_INFO

 175            LOAD_GLOBAL              6 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L9)
                NOT_TAKEN
                STORE_FAST               4 (e)

 176    L6:     LOAD_GLOBAL              8 (logger)
                LOAD_ATTR               11 (warning + NULL|self)

 177            LOAD_CONST               9 ('tenant_launch_readiness_route error type=')

 178            LOAD_GLOBAL             13 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               14 (__name__)
                FORMAT_SIMPLE

 177            BUILD_STRING             2

 176            CALL                     1
                POP_TOP

 181            LOAD_CONST               2 ('status')
                LOAD_CONST              10 ('failed')

 182            LOAD_CONST               3 ('surface')
                LOAD_CONST               4 ('tenant.launch_readiness')

 183            LOAD_CONST               8 ('error_code')
                LOAD_CONST              11 ('unexpected:')
                LOAD_GLOBAL             13 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               14 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 184            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 180            BUILD_MAP                4
                STORE_FAST               3 (out)
        L7:     POP_EXCEPT
                LOAD_CONST              12 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                JUMP_BACKWARD_NO_INTERRUPT 104 (to L4)

  --    L8:     LOAD_CONST              12 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RERAISE                  1

 175    L9:     RERAISE                  0

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

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "app\routes\tenant_portal.py", line 190>:
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

Disassembly of <code object tenant_integrations_route at 0x0000018C17D6DFC0, file "app\routes\tenant_portal.py", line 189>:
 189            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 195            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('tenant_integration_posture',))
                IMPORT_NAME              0 (app.services.tenant.tenant_visibility_service)
                IMPORT_FROM              1 (tenant_integration_posture)
                STORE_FAST               1 (tenant_integration_posture)
                POP_TOP

 198    L2:     NOP

 199    L3:     LOAD_FAST_BORROW         1 (tenant_integration_posture)
                PUSH_NULL
                LOAD_FAST_BORROW         0 (brokerage)
                CALL                     1
                STORE_FAST               2 (env)

 201            LOAD_CONST               2 ('status')
                LOAD_FAST_BORROW         2 (env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               2 ('status')
                CALL                     1

 202            LOAD_CONST               3 ('surface')
                LOAD_CONST               4 ('tenant.integrations')

 203            LOAD_CONST               5 ('brokerage_id')
                LOAD_FAST_BORROW         2 (env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               5 ('brokerage_id')
                CALL                     1

 204            LOAD_CONST               6 ('payload')
                LOAD_FAST_BORROW         2 (env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               6 ('payload')
                CALL                     1

 205            LOAD_CONST               7 ('warnings')
                LOAD_FAST_BORROW         2 (env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               7 ('warnings')
                CALL                     1

 206            LOAD_CONST               8 ('error_code')
                LOAD_FAST_BORROW         2 (env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               8 ('error_code')
                CALL                     1

 200            BUILD_MAP                6
                STORE_FAST               3 (out)

 218    L4:     LOAD_GLOBAL             17 (_final_envelope + NULL)
                LOAD_FAST_BORROW         3 (out)
                LOAD_CONST               4 ('tenant.integrations')
                LOAD_CONST              13 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --    L5:     PUSH_EXC_INFO

 208            LOAD_GLOBAL              6 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L9)
                NOT_TAKEN
                STORE_FAST               4 (e)

 209    L6:     LOAD_GLOBAL              8 (logger)
                LOAD_ATTR               11 (warning + NULL|self)

 210            LOAD_CONST               9 ('tenant_integrations_route error type=')
                LOAD_GLOBAL             13 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               14 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 209            CALL                     1
                POP_TOP

 213            LOAD_CONST               2 ('status')
                LOAD_CONST              10 ('failed')

 214            LOAD_CONST               3 ('surface')
                LOAD_CONST               4 ('tenant.integrations')

 215            LOAD_CONST               8 ('error_code')
                LOAD_CONST              11 ('unexpected:')
                LOAD_GLOBAL             13 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               14 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 216            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 212            BUILD_MAP                4
                STORE_FAST               3 (out)
        L7:     POP_EXCEPT
                LOAD_CONST              12 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                JUMP_BACKWARD_NO_INTERRUPT 104 (to L4)

  --    L8:     LOAD_CONST              12 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RERAISE                  1

 208    L9:     RERAISE                  0

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

Disassembly of <code object TenantAuditAcknowledgeRequest at 0x0000018C1802C620, file "app\routes\tenant_portal.py", line 224>:
224           RESUME                   0
              LOAD_NAME                0 (__name__)
              STORE_NAME               1 (__module__)
              LOAD_CONST               0 ('TenantAuditAcknowledgeRequest')
              STORE_NAME               2 (__qualname__)
              LOAD_SMALL_INT         224
              STORE_NAME               3 (__firstlineno__)
              SETUP_ANNOTATIONS

225           LOAD_CONST               1 ('PAS176 — bounded payload for the tenant audit ack endpoint.\n\nAll fields optional except as noted. NEVER carries PII —\nnotes_token is a structural identifier (alphanumeric + dash\n+ underscore) up to 200 characters; the service layer\nrejects anything else.')
              STORE_NAME               4 (__doc__)

231           LOAD_NAME                5 (_PydField)
              PUSH_NULL
              LOAD_CONST               2 (None)
              LOAD_SMALL_INT         200
              LOAD_CONST               3 (('default', 'max_length'))
              CALL_KW                  2
              STORE_NAME               6 (actor_token)
              LOAD_CONST               4 ('Optional[str]')
              LOAD_NAME                7 (__annotations__)
              LOAD_CONST               5 ('actor_token')
              STORE_SUBSCR

232           LOAD_NAME                5 (_PydField)
              PUSH_NULL
              LOAD_CONST               2 (None)
              LOAD_SMALL_INT         200
              LOAD_CONST               3 (('default', 'max_length'))
              CALL_KW                  2
              STORE_NAME               8 (notes_token)
              LOAD_CONST               4 ('Optional[str]')
              LOAD_NAME                7 (__annotations__)
              LOAD_CONST               6 ('notes_token')
              STORE_SUBSCR
              LOAD_CONST               7 (())
              STORE_NAME               9 (__static_attributes__)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026430, file "app\routes\tenant_portal.py", line 236>:
236           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('entry_id')

237           LOAD_CONST               2 ('str')

236           LOAD_CONST               3 ('body')

238           LOAD_CONST               4 ('Optional[TenantAuditAcknowledgeRequest]')

236           LOAD_CONST               5 ('return')

240           LOAD_CONST               6 ('Dict[str, Any]')

236           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object tenant_audit_acknowledge_route at 0x0000018C17F77850, file "app\routes\tenant_portal.py", line 235>:
 235            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 250            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('acknowledge_tenant_audit_entry',))
                IMPORT_NAME              0 (app.services.tenant.tenant_visibility_service)
                IMPORT_FROM              1 (acknowledge_tenant_audit_entry)
                STORE_FAST               3 (acknowledge_tenant_audit_entry)
                POP_TOP

 253            LOAD_FAST_BORROW         1 (body)
                TO_BOOL
                POP_JUMP_IF_FALSE       13 (to L2)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR                4 (actor_token)
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               2 (None)
        L3:     STORE_FAST               4 (actor_token)

 254            LOAD_FAST_BORROW         1 (body)
                TO_BOOL
                POP_JUMP_IF_FALSE       13 (to L6)
        L4:     NOT_TAKEN
        L5:     LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR                6 (notes_token)
                JUMP_FORWARD             1 (to L7)
        L6:     LOAD_CONST               2 (None)
        L7:     STORE_FAST               5 (notes_token)

 255    L8:     NOP

 256    L9:     LOAD_FAST_BORROW         3 (acknowledge_tenant_audit_entry)
                PUSH_NULL

 257            LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (brokerage, entry_id)

 258            LOAD_FAST_BORROW         4 (actor_token)

 259            LOAD_FAST_BORROW         5 (notes_token)

 256            LOAD_CONST               3 (('actor_token', 'notes_token'))
                CALL_KW                  4
                STORE_FAST               6 (env)

 262            LOAD_CONST               4 ('status')
                LOAD_FAST_BORROW         6 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               4 ('status')
                CALL                     1

 263            LOAD_CONST               5 ('surface')
                LOAD_CONST               6 ('tenant.audit_acknowledge')

 264            LOAD_CONST               7 ('brokerage_id')
                LOAD_FAST_BORROW         6 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               7 ('brokerage_id')
                CALL                     1

 265            LOAD_CONST               8 ('payload')
                LOAD_FAST_BORROW         6 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               8 ('payload')
                CALL                     1

 266            LOAD_CONST               9 ('warnings')
                LOAD_FAST_BORROW         6 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               9 ('warnings')
                CALL                     1

 267            LOAD_CONST              10 ('error_code')
                LOAD_FAST_BORROW         6 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              10 ('error_code')
                CALL                     1

 261            BUILD_MAP                6
                STORE_FAST               7 (out)

 279   L10:     LOAD_GLOBAL             21 (_final_envelope + NULL)
                LOAD_FAST_BORROW         7 (out)
                LOAD_CONST               6 ('tenant.audit_acknowledge')
                LOAD_CONST              14 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --   L11:     PUSH_EXC_INFO

 269            LOAD_GLOBAL             10 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L15)
                NOT_TAKEN
                STORE_FAST               8 (e)

 270   L12:     LOAD_GLOBAL             12 (logger)
                LOAD_ATTR               15 (warning + NULL|self)

 271            LOAD_CONST              11 ('tenant_audit_acknowledge_route error type=')
                LOAD_GLOBAL             17 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               18 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 270            CALL                     1
                POP_TOP

 274            LOAD_CONST               4 ('status')
                LOAD_CONST              12 ('failed')

 275            LOAD_CONST               5 ('surface')
                LOAD_CONST               6 ('tenant.audit_acknowledge')

 276            LOAD_CONST              10 ('error_code')
                LOAD_CONST              13 ('unexpected:')
                LOAD_GLOBAL             17 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               18 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 277            LOAD_CONST               9 ('warnings')
                BUILD_LIST               0

 273            BUILD_MAP                4
                STORE_FAST               7 (out)
       L13:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                JUMP_BACKWARD_NO_INTERRUPT 104 (to L10)

  --   L14:     LOAD_CONST               2 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RERAISE                  1

 269   L15:     RERAISE                  0

  --   L16:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L17:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L4 -> L17 [0] lasti
  L5 to L8 -> L17 [0] lasti
  L9 to L10 -> L11 [0]
  L10 to L11 -> L17 [0] lasti
  L11 to L12 -> L16 [1] lasti
  L12 to L13 -> L14 [1] lasti
  L13 to L14 -> L17 [0] lasti
  L14 to L16 -> L16 [1] lasti
  L16 to L17 -> L17 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "app\routes\tenant_portal.py", line 283>:
283           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')

285           LOAD_CONST               2 ('Dict[str, Any]')

283           BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object tenant_audit_dashboard_route at 0x0000018C17ED9360, file "app\routes\tenant_portal.py", line 282>:
 282            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 293            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('tenant_audit_dashboard_summary',))
                IMPORT_NAME              0 (app.services.tenant.tenant_audit_dashboard)
                IMPORT_FROM              1 (tenant_audit_dashboard_summary)
                STORE_FAST               1 (tenant_audit_dashboard_summary)
                POP_TOP

 296    L2:     NOP

 297    L3:     LOAD_FAST_BORROW         1 (tenant_audit_dashboard_summary)
                PUSH_NULL
                LOAD_FAST_BORROW         0 (brokerage)
                CALL                     1
                STORE_FAST               2 (env)

 299            LOAD_CONST               2 ('status')
                LOAD_FAST_BORROW         2 (env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               2 ('status')
                CALL                     1

 300            LOAD_CONST               3 ('surface')
                LOAD_CONST               4 ('tenant.audit_dashboard')

 301            LOAD_CONST               5 ('brokerage_id')
                LOAD_FAST_BORROW         2 (env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               5 ('brokerage_id')
                CALL                     1

 302            LOAD_CONST               6 ('payload')
                LOAD_FAST_BORROW         2 (env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               6 ('payload')
                CALL                     1

 303            LOAD_CONST               7 ('warnings')
                LOAD_FAST_BORROW         2 (env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               7 ('warnings')
                CALL                     1

 304            LOAD_CONST               8 ('error_code')
                LOAD_FAST_BORROW         2 (env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               8 ('error_code')
                CALL                     1

 298            BUILD_MAP                6
                STORE_FAST               3 (out)

 316    L4:     LOAD_GLOBAL             17 (_final_envelope + NULL)
                LOAD_FAST_BORROW         3 (out)
                LOAD_CONST               4 ('tenant.audit_dashboard')
                LOAD_CONST              13 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --    L5:     PUSH_EXC_INFO

 306            LOAD_GLOBAL              6 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L9)
                NOT_TAKEN
                STORE_FAST               4 (e)

 307    L6:     LOAD_GLOBAL              8 (logger)
                LOAD_ATTR               11 (warning + NULL|self)

 308            LOAD_CONST               9 ('tenant_audit_dashboard_route error type=')
                LOAD_GLOBAL             13 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               14 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 307            CALL                     1
                POP_TOP

 311            LOAD_CONST               2 ('status')
                LOAD_CONST              10 ('failed')

 312            LOAD_CONST               3 ('surface')
                LOAD_CONST               4 ('tenant.audit_dashboard')

 313            LOAD_CONST               8 ('error_code')
                LOAD_CONST              11 ('unexpected:')
                LOAD_GLOBAL             13 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               14 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 314            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 310            BUILD_MAP                4
                STORE_FAST               3 (out)
        L7:     POP_EXCEPT
                LOAD_CONST              12 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                JUMP_BACKWARD_NO_INTERRUPT 104 (to L4)

  --    L8:     LOAD_CONST              12 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RERAISE                  1

 306    L9:     RERAISE                  0

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

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "app\routes\tenant_portal.py", line 320>:
320           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')

322           LOAD_CONST               2 ('Dict[str, Any]')

320           BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object tenant_audit_chain_status_route at 0x0000018C17ED9600, file "app\routes\tenant_portal.py", line 319>:
 319            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 324            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('tenant_chain_status_summary',))
                IMPORT_NAME              0 (app.services.tenant.tenant_audit_dashboard)
                IMPORT_FROM              1 (tenant_chain_status_summary)
                STORE_FAST               1 (tenant_chain_status_summary)
                POP_TOP

 327    L2:     NOP

 328    L3:     LOAD_FAST_BORROW         1 (tenant_chain_status_summary)
                PUSH_NULL
                LOAD_FAST_BORROW         0 (brokerage)
                CALL                     1
                STORE_FAST               2 (env)

 330            LOAD_CONST               2 ('status')
                LOAD_FAST_BORROW         2 (env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               2 ('status')
                CALL                     1

 331            LOAD_CONST               3 ('surface')
                LOAD_CONST               4 ('tenant.audit_chain_status')

 332            LOAD_CONST               5 ('brokerage_id')
                LOAD_FAST_BORROW         2 (env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               5 ('brokerage_id')
                CALL                     1

 333            LOAD_CONST               6 ('payload')
                LOAD_FAST_BORROW         2 (env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               6 ('payload')
                CALL                     1

 334            LOAD_CONST               7 ('warnings')
                LOAD_FAST_BORROW         2 (env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               7 ('warnings')
                CALL                     1

 335            LOAD_CONST               8 ('error_code')
                LOAD_FAST_BORROW         2 (env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               8 ('error_code')
                CALL                     1

 329            BUILD_MAP                6
                STORE_FAST               3 (out)

 347    L4:     LOAD_GLOBAL             17 (_final_envelope + NULL)
                LOAD_FAST_BORROW         3 (out)
                LOAD_CONST               4 ('tenant.audit_chain_status')
                LOAD_CONST              13 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --    L5:     PUSH_EXC_INFO

 337            LOAD_GLOBAL              6 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L9)
                NOT_TAKEN
                STORE_FAST               4 (e)

 338    L6:     LOAD_GLOBAL              8 (logger)
                LOAD_ATTR               11 (warning + NULL|self)

 339            LOAD_CONST               9 ('tenant_audit_chain_status_route error type=')
                LOAD_GLOBAL             13 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               14 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 338            CALL                     1
                POP_TOP

 342            LOAD_CONST               2 ('status')
                LOAD_CONST              10 ('failed')

 343            LOAD_CONST               3 ('surface')
                LOAD_CONST               4 ('tenant.audit_chain_status')

 344            LOAD_CONST               8 ('error_code')
                LOAD_CONST              11 ('unexpected:')
                LOAD_GLOBAL             13 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               14 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 345            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 341            BUILD_MAP                4
                STORE_FAST               3 (out)
        L7:     POP_EXCEPT
                LOAD_CONST              12 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                JUMP_BACKWARD_NO_INTERRUPT 104 (to L4)

  --    L8:     LOAD_CONST              12 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RERAISE                  1

 337    L9:     RERAISE                  0

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

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "app\routes\tenant_portal.py", line 351>:
351           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')

353           LOAD_CONST               2 ('Dict[str, Any]')

351           BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object tenant_audit_verification_history_route at 0x0000018C17D7C5B0, file "app\routes\tenant_portal.py", line 350>:
 350            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 355            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('tenant_verification_history_summary',))
                IMPORT_NAME              0 (app.services.tenant.tenant_audit_dashboard)
                IMPORT_FROM              1 (tenant_verification_history_summary)
                STORE_FAST               1 (tenant_verification_history_summary)
                POP_TOP

 358    L2:     NOP

 359    L3:     LOAD_FAST_BORROW         1 (tenant_verification_history_summary)
                PUSH_NULL
                LOAD_FAST_BORROW         0 (brokerage)
                CALL                     1
                STORE_FAST               2 (env)

 361            LOAD_CONST               2 ('status')
                LOAD_FAST_BORROW         2 (env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               2 ('status')
                CALL                     1

 362            LOAD_CONST               3 ('surface')
                LOAD_CONST               4 ('tenant.audit_verification_history')

 363            LOAD_CONST               5 ('brokerage_id')
                LOAD_FAST_BORROW         2 (env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               5 ('brokerage_id')
                CALL                     1

 364            LOAD_CONST               6 ('payload')
                LOAD_FAST_BORROW         2 (env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               6 ('payload')
                CALL                     1

 365            LOAD_CONST               7 ('warnings')
                LOAD_FAST_BORROW         2 (env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               7 ('warnings')
                CALL                     1

 366            LOAD_CONST               8 ('error_code')
                LOAD_FAST_BORROW         2 (env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               8 ('error_code')
                CALL                     1

 360            BUILD_MAP                6
                STORE_FAST               3 (out)

 379    L4:     LOAD_GLOBAL             17 (_final_envelope + NULL)
                LOAD_FAST_BORROW         3 (out)
                LOAD_CONST               4 ('tenant.audit_verification_history')
                LOAD_CONST              13 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --    L5:     PUSH_EXC_INFO

 368            LOAD_GLOBAL              6 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L9)
                NOT_TAKEN
                STORE_FAST               4 (e)

 369    L6:     LOAD_GLOBAL              8 (logger)
                LOAD_ATTR               11 (warning + NULL|self)

 370            LOAD_CONST               9 ('tenant_audit_verification_history_route error type=')

 371            LOAD_GLOBAL             13 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               14 (__name__)
                FORMAT_SIMPLE

 370            BUILD_STRING             2

 369            CALL                     1
                POP_TOP

 374            LOAD_CONST               2 ('status')
                LOAD_CONST              10 ('failed')

 375            LOAD_CONST               3 ('surface')
                LOAD_CONST               4 ('tenant.audit_verification_history')

 376            LOAD_CONST               8 ('error_code')
                LOAD_CONST              11 ('unexpected:')
                LOAD_GLOBAL             13 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               14 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 377            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 373            BUILD_MAP                4
                STORE_FAST               3 (out)
        L7:     POP_EXCEPT
                LOAD_CONST              12 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                JUMP_BACKWARD_NO_INTERRUPT 104 (to L4)

  --    L8:     LOAD_CONST              12 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RERAISE                  1

 368    L9:     RERAISE                  0

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

Disassembly of <code object __annotate__ at 0x0000018C18026230, file "app\routes\tenant_portal.py", line 383>:
383           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('limit')

384           LOAD_CONST               2 ('int')

383           LOAD_CONST               3 ('acknowledgement_type')

385           LOAD_CONST               4 ('Optional[str]')

383           LOAD_CONST               5 ('return')

387           LOAD_CONST               6 ('Dict[str, Any]')

383           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object tenant_audit_acknowledgements_route at 0x0000018C17E953A0, file "app\routes\tenant_portal.py", line 382>:
 382            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 395            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('list_tenant_audit_acknowledgements',))
                IMPORT_NAME              0 (app.services.tenant.tenant_audit_ack_store)
                IMPORT_FROM              1 (list_tenant_audit_acknowledgements)
                STORE_FAST               3 (list_tenant_audit_acknowledgements)
                POP_TOP

 398    L2:     NOP

 399    L3:     LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST_BORROW         2 (brokerage)
                LOAD_GLOBAL              6 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L4)
                NOT_TAKEN
                LOAD_FAST_BORROW         2 (brokerage)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               2 ('id')
                CALL                     1
                JUMP_FORWARD             1 (to L5)
        L4:     LOAD_CONST               3 (None)
        L5:     STORE_FAST               4 (bid)

 400            LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (limit)
                LOAD_GLOBAL             10 (int)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       12 (to L6)
                NOT_TAKEN
                LOAD_GLOBAL             11 (int + NULL)
                LOAD_FAST_BORROW         0 (limit)
                CALL                     1
                JUMP_FORWARD             1 (to L7)
        L6:     LOAD_SMALL_INT          50
        L7:     STORE_FAST               5 (capped)

 401            LOAD_FAST_BORROW         5 (capped)
                LOAD_SMALL_INT           1
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN

 402            LOAD_SMALL_INT           1
                STORE_FAST               5 (capped)

 403    L8:     LOAD_FAST_BORROW         5 (capped)
                LOAD_SMALL_INT         200
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE        3 (to L9)
                NOT_TAKEN

 404            LOAD_SMALL_INT         200
                STORE_FAST               5 (capped)

 405    L9:     LOAD_FAST_BORROW         3 (list_tenant_audit_acknowledgements)
                PUSH_NULL

 406            LOAD_FAST_BORROW_LOAD_FAST_BORROW 65 (bid, acknowledgement_type)
                LOAD_FAST_BORROW         5 (capped)

 405            LOAD_CONST               4 (('acknowledgement_type', 'limit'))
                CALL_KW                  3
                STORE_FAST               6 (env)

 411            BUILD_LIST               0
                STORE_FAST               7 (rows)

 412            LOAD_FAST_BORROW         6 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               5 ('rows')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L12)
       L10:     NOT_TAKEN
       L11:     POP_TOP
                BUILD_LIST               0
       L12:     GET_ITER
       L13:     FOR_ITER               163 (to L15)
                STORE_FAST               8 (r)

 413            LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST_BORROW         8 (r)
                LOAD_GLOBAL              6 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN

 414            JUMP_BACKWARD           27 (to L13)

 415   L14:     LOAD_FAST_BORROW         7 (rows)
                LOAD_ATTR               13 (append + NULL|self)

 416            LOAD_CONST               6 ('acknowledgement_id')
                LOAD_FAST_BORROW         8 (r)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               6 ('acknowledgement_id')
                CALL                     1

 417            LOAD_CONST               7 ('entry_id')
                LOAD_FAST_BORROW         8 (r)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               8 ('audit_entry_id')
                CALL                     1

 418            LOAD_CONST               9 ('merkle_root_id')
                LOAD_FAST_BORROW         8 (r)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               9 ('merkle_root_id')
                CALL                     1

 419            LOAD_CONST              10 ('acknowledged_at')
                LOAD_FAST_BORROW         8 (r)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              10 ('acknowledged_at')
                CALL                     1

 420            LOAD_CONST              11 ('acknowledgement_type')
                LOAD_FAST_BORROW         8 (r)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              11 ('acknowledgement_type')
                CALL                     1

 421            LOAD_CONST              12 ('actor_token')
                LOAD_FAST_BORROW         8 (r)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              13 ('actor_id')
                CALL                     1

 422            LOAD_CONST              14 ('notes_token')
                LOAD_FAST_BORROW         8 (r)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              14 ('notes_token')
                CALL                     1

 415            BUILD_MAP                7
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          165 (to L13)

 412   L15:     END_FOR
                POP_ITER

 425            LOAD_CONST              15 ('status')
                LOAD_FAST_BORROW         6 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              15 ('status')
                CALL                     1

 426            LOAD_CONST              16 ('surface')
                LOAD_CONST              17 ('tenant.audit_acknowledgements')

 427            LOAD_CONST              18 ('brokerage_id')
                LOAD_FAST_BORROW         6 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              18 ('brokerage_id')
                CALL                     1

 428            LOAD_CONST              19 ('payload')

 429            LOAD_CONST               5 ('rows')
                LOAD_FAST_BORROW         7 (rows)

 430            LOAD_CONST              20 ('count')
                LOAD_FAST_BORROW         6 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              20 ('count')
                LOAD_SMALL_INT           0
                CALL                     2

 431            LOAD_CONST              21 ('limit')
                LOAD_FAST_BORROW         6 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              21 ('limit')
                LOAD_FAST_BORROW         5 (capped)
                CALL                     2

 432            LOAD_CONST              22 ('filter_ack_type')
                LOAD_FAST_BORROW         6 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              22 ('filter_ack_type')
                CALL                     1

 428            BUILD_MAP                4

 434            LOAD_CONST              23 ('warnings')
                LOAD_FAST_BORROW         6 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              23 ('warnings')
                CALL                     1

 435            LOAD_CONST              24 ('error_code')
                LOAD_FAST_BORROW         6 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              24 ('error_code')
                CALL                     1

 424            BUILD_MAP                6
                STORE_FAST               9 (out)

 447   L16:     LOAD_GLOBAL             25 (_final_envelope + NULL)
                LOAD_FAST_BORROW         9 (out)
                LOAD_CONST              17 ('tenant.audit_acknowledgements')
                LOAD_CONST              28 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --   L17:     PUSH_EXC_INFO

 437            LOAD_GLOBAL             14 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L21)
                NOT_TAKEN
                STORE_FAST              10 (e)

 438   L18:     LOAD_GLOBAL             16 (logger)
                LOAD_ATTR               19 (warning + NULL|self)

 439            LOAD_CONST              25 ('tenant_audit_acknowledgements_route error type=')
                LOAD_GLOBAL             21 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               22 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 438            CALL                     1
                POP_TOP

 442            LOAD_CONST              15 ('status')
                LOAD_CONST              26 ('failed')

 443            LOAD_CONST              16 ('surface')
                LOAD_CONST              17 ('tenant.audit_acknowledgements')

 444            LOAD_CONST              24 ('error_code')
                LOAD_CONST              27 ('unexpected:')
                LOAD_GLOBAL             21 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               22 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 445            LOAD_CONST              23 ('warnings')
                BUILD_LIST               0

 441            BUILD_MAP                4
                STORE_FAST               9 (out)
       L19:     POP_EXCEPT
                LOAD_CONST               3 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                JUMP_BACKWARD_NO_INTERRUPT 104 (to L16)

  --   L20:     LOAD_CONST               3 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RERAISE                  1

 437   L21:     RERAISE                  0

  --   L22:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L23:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L23 [0] lasti
  L3 to L10 -> L17 [0]
  L11 to L16 -> L17 [0]
  L16 to L17 -> L23 [0] lasti
  L17 to L18 -> L22 [1] lasti
  L18 to L19 -> L20 [1] lasti
  L19 to L20 -> L23 [0] lasti
  L20 to L22 -> L22 [1] lasti
  L22 to L23 -> L23 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025D30, file "app\routes\tenant_portal.py", line 451>:
451           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('merkle_root_id')

452           LOAD_CONST               2 ('str')

451           LOAD_CONST               3 ('body')

453           LOAD_CONST               4 ('Optional[TenantAuditAcknowledgeRequest]')

451           LOAD_CONST               5 ('return')

455           LOAD_CONST               6 ('Dict[str, Any]')

451           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object tenant_audit_window_acknowledge_route at 0x0000018C17D51630, file "app\routes\tenant_portal.py", line 450>:
 450            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 463            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('record_tenant_audit_acknowledgement',))
                IMPORT_NAME              0 (app.services.tenant.tenant_audit_ack_store)
                IMPORT_FROM              1 (record_tenant_audit_acknowledgement)
                STORE_FAST               3 (record_tenant_audit_acknowledgement)
                POP_TOP

 466            LOAD_FAST_BORROW         1 (body)
                TO_BOOL
                POP_JUMP_IF_FALSE       13 (to L2)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR                4 (actor_token)
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               2 (None)
        L3:     STORE_FAST               4 (actor_token)

 467            LOAD_FAST_BORROW         1 (body)
                TO_BOOL
                POP_JUMP_IF_FALSE       13 (to L6)
        L4:     NOT_TAKEN
        L5:     LOAD_FAST_BORROW         1 (body)
                LOAD_ATTR                6 (notes_token)
                JUMP_FORWARD             1 (to L7)
        L6:     LOAD_CONST               2 (None)
        L7:     STORE_FAST               5 (notes_token)

 468    L8:     NOP

 469    L9:     LOAD_GLOBAL              9 (isinstance + NULL)
                LOAD_FAST_BORROW         2 (brokerage)
                LOAD_GLOBAL             10 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L10)
                NOT_TAKEN
                LOAD_FAST_BORROW         2 (brokerage)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               3 ('id')
                CALL                     1
                JUMP_FORWARD             1 (to L11)
       L10:     LOAD_CONST               2 (None)
       L11:     STORE_FAST               6 (bid)

 470            LOAD_FAST_BORROW         3 (record_tenant_audit_acknowledgement)
                PUSH_NULL

 471            LOAD_FAST_BORROW         6 (bid)

 472            LOAD_CONST               4 ('MERKLE_ROOT_ACKNOWLEDGED')

 473            LOAD_CONST               5 ('TENANT')

 474            LOAD_FAST_BORROW         4 (actor_token)

 475            LOAD_FAST_BORROW         0 (merkle_root_id)

 476            LOAD_FAST_BORROW         5 (notes_token)

 470            LOAD_CONST               6 (('brokerage_id', 'acknowledgement_type', 'actor_type', 'actor_id', 'merkle_root_id', 'notes_token'))
                CALL_KW                  6
                STORE_FAST               7 (env)

 478            LOAD_FAST_BORROW         7 (env)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               7 ('ack_row')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L14)
       L12:     NOT_TAKEN
       L13:     POP_TOP
                BUILD_MAP                0
       L14:     STORE_FAST               8 (row)

 480            LOAD_CONST               8 ('status')
                LOAD_FAST_BORROW         7 (env)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               8 ('status')
                CALL                     1

 481            LOAD_CONST               9 ('surface')
                LOAD_CONST              10 ('tenant.audit_window_acknowledge')

 482            LOAD_CONST              11 ('brokerage_id')
                LOAD_FAST_BORROW         6 (bid)

 483            LOAD_CONST              12 ('payload')

 484            LOAD_CONST              13 ('acknowledgement_id')
                LOAD_FAST_BORROW         8 (row)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              13 ('acknowledgement_id')
                CALL                     1

 485            LOAD_CONST              14 ('merkle_root_id')
                LOAD_FAST_BORROW         8 (row)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              14 ('merkle_root_id')
                CALL                     1

 486            LOAD_CONST              15 ('duplicate')
                LOAD_GLOBAL             15 (bool + NULL)
                LOAD_FAST_BORROW         7 (env)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              15 ('duplicate')
                CALL                     1
                CALL                     1

 487            LOAD_CONST              16 ('acknowledged_at')
                LOAD_FAST_BORROW         8 (row)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              16 ('acknowledged_at')
                CALL                     1

 488            LOAD_CONST              17 ('notes_token')
                LOAD_FAST_BORROW         8 (row)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              17 ('notes_token')
                CALL                     1

 489            LOAD_CONST              18 ('acknowledgement_type')
                LOAD_FAST_BORROW         8 (row)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              18 ('acknowledgement_type')
                CALL                     1

 483            BUILD_MAP                6

 491            LOAD_CONST              19 ('warnings')
                LOAD_FAST_BORROW         7 (env)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              19 ('warnings')
                CALL                     1

 492            LOAD_CONST              20 ('error_code')
                LOAD_FAST_BORROW         7 (env)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              20 ('error_code')
                CALL                     1

 479            BUILD_MAP                6
                STORE_FAST               9 (out)

 504   L15:     LOAD_GLOBAL             27 (_final_envelope + NULL)
                LOAD_FAST_BORROW         9 (out)
                LOAD_CONST              10 ('tenant.audit_window_acknowledge')
                LOAD_CONST              24 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --   L16:     PUSH_EXC_INFO

 494            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L20)
                NOT_TAKEN
                STORE_FAST              10 (e)

 495   L17:     LOAD_GLOBAL             18 (logger)
                LOAD_ATTR               21 (warning + NULL|self)

 496            LOAD_CONST              21 ('tenant_audit_window_acknowledge_route error type=')
                LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 495            CALL                     1
                POP_TOP

 499            LOAD_CONST               8 ('status')
                LOAD_CONST              22 ('failed')

 500            LOAD_CONST               9 ('surface')
                LOAD_CONST              10 ('tenant.audit_window_acknowledge')

 501            LOAD_CONST              20 ('error_code')
                LOAD_CONST              23 ('unexpected:')
                LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 502            LOAD_CONST              19 ('warnings')
                BUILD_LIST               0

 498            BUILD_MAP                4
                STORE_FAST               9 (out)
       L18:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                JUMP_BACKWARD_NO_INTERRUPT 104 (to L15)

  --   L19:     LOAD_CONST               2 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RERAISE                  1

 494   L20:     RERAISE                  0

  --   L21:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L22:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L4 -> L22 [0] lasti
  L5 to L8 -> L22 [0] lasti
  L9 to L12 -> L16 [0]
  L13 to L15 -> L16 [0]
  L15 to L16 -> L22 [0] lasti
  L16 to L17 -> L21 [1] lasti
  L17 to L18 -> L19 [1] lasti
  L18 to L19 -> L22 [0] lasti
  L19 to L21 -> L21 [1] lasti
  L21 to L22 -> L22 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "app\routes\tenant_portal.py", line 508>:
508           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('entry_id')

509           LOAD_CONST               2 ('str')

508           LOAD_CONST               3 ('return')

511           LOAD_CONST               4 ('Dict[str, Any]')

508           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object tenant_audit_proof_route at 0x0000018C17D51ED0, file "app\routes\tenant_portal.py", line 507>:
 507            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 518            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('proof_for_audit_entry', 'verify_inclusion_proof'))
                IMPORT_NAME              0 (app.services.operator.merkle_inclusion_proofs)
                IMPORT_FROM              1 (proof_for_audit_entry)
                STORE_FAST               2 (proof_for_audit_entry)
                IMPORT_FROM              2 (verify_inclusion_proof)
                STORE_FAST               3 (verify_inclusion_proof)
                POP_TOP

 522    L2:     NOP

 523    L3:     LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (brokerage)
                LOAD_GLOBAL              8 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L4)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (brokerage)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               2 ('id')
                CALL                     1
                JUMP_FORWARD             1 (to L5)
        L4:     LOAD_CONST               3 (None)
        L5:     STORE_FAST               4 (bid)

 524            LOAD_FAST_BORROW         2 (proof_for_audit_entry)
                PUSH_NULL

 525            LOAD_FAST_BORROW_LOAD_FAST_BORROW 64 (bid, entry_id)

 524            LOAD_CONST               4 (('brokerage_id', 'audit_entry_id'))
                CALL_KW                  2
                STORE_FAST               5 (res)

 527            LOAD_FAST_BORROW         5 (res)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               5 ('status')
                CALL                     1
                LOAD_CONST               6 ('ok')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE      102 (to L13)
                NOT_TAKEN

 529            LOAD_CONST               5 ('status')
                LOAD_FAST_BORROW         5 (res)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               5 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
        L6:     NOT_TAKEN
        L7:     POP_TOP
                LOAD_CONST               7 ('failed')

 530    L8:     LOAD_CONST               8 ('surface')
                LOAD_CONST               9 ('tenant.audit_proof')

 531            LOAD_CONST              10 ('brokerage_id')
                LOAD_FAST                4 (bid)

 532            LOAD_CONST              11 ('payload')
                LOAD_CONST               3 (None)

 533            LOAD_CONST              12 ('warnings')
                LOAD_GLOBAL             13 (list + NULL)
                LOAD_FAST_BORROW         5 (res)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              12 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L11)
        L9:     NOT_TAKEN
       L10:     POP_TOP
                BUILD_LIST               0
       L11:     CALL                     1

 534            LOAD_CONST              13 ('error_code')
                LOAD_FAST_BORROW         5 (res)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              13 ('error_code')
                CALL                     1

 528            BUILD_MAP                6
                STORE_FAST               6 (out)

 536            LOAD_GLOBAL             15 (_final_envelope + NULL)
                LOAD_FAST_BORROW         6 (out)
                LOAD_CONST               9 ('tenant.audit_proof')
                LOAD_CONST              14 (('surface',))
                CALL_KW                  2
       L12:     RETURN_VALUE

 537   L13:     LOAD_FAST_BORROW         5 (res)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              15 ('proof')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L16)
       L14:     NOT_TAKEN
       L15:     POP_TOP
                BUILD_MAP                0
       L16:     STORE_FAST               7 (proof)

 538            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW         7 (proof)
                LOAD_GLOBAL              8 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        9 (to L17)
                NOT_TAKEN
                LOAD_FAST_BORROW         3 (verify_inclusion_proof)
                PUSH_NULL
                LOAD_FAST_BORROW         7 (proof)
                CALL                     1
                JUMP_FORWARD             1 (to L18)
       L17:     BUILD_MAP                0
       L18:     STORE_FAST               8 (verdict)

 544            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW         7 (proof)
                LOAD_GLOBAL              8 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       12 (to L19)
                NOT_TAKEN
                LOAD_GLOBAL              9 (dict + NULL)
                LOAD_FAST_BORROW         7 (proof)
                CALL                     1
                JUMP_FORWARD             1 (to L20)
       L19:     BUILD_MAP                0
       L20:     STORE_FAST               9 (out_proof)

 546            LOAD_CONST               5 ('status')
                LOAD_CONST               6 ('ok')

 547            LOAD_CONST               8 ('surface')
                LOAD_CONST               9 ('tenant.audit_proof')

 548            LOAD_CONST              10 ('brokerage_id')
                LOAD_FAST                4 (bid)

 549            LOAD_CONST              11 ('payload')

 550            LOAD_CONST              16 ('entry_id')
                LOAD_FAST                0 (entry_id)

 551            LOAD_CONST              17 ('merkle_root_id')
                LOAD_FAST_BORROW         5 (res)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              17 ('merkle_root_id')
                CALL                     1

 552            LOAD_CONST              18 ('window_start')
                LOAD_FAST_BORROW         5 (res)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              18 ('window_start')
                CALL                     1

 553            LOAD_CONST              19 ('window_end')
                LOAD_FAST_BORROW         5 (res)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              19 ('window_end')
                CALL                     1

 554            LOAD_CONST              15 ('proof')
                LOAD_FAST                9 (out_proof)

 555            LOAD_CONST              20 ('self_verification')

 556            LOAD_CONST              21 ('valid')
                LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW         8 (verdict)
                LOAD_GLOBAL              8 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       27 (to L21)
                NOT_TAKEN
                LOAD_GLOBAL             17 (bool + NULL)
                LOAD_FAST_BORROW         8 (verdict)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              21 ('valid')
                CALL                     1
                CALL                     1
                JUMP_FORWARD             1 (to L22)
       L21:     LOAD_CONST              22 (False)

 557   L22:     LOAD_CONST              13 ('error_code')
                LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW         8 (verdict)
                LOAD_GLOBAL              8 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L23)
                NOT_TAKEN
                LOAD_FAST_BORROW         8 (verdict)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              13 ('error_code')
                CALL                     1
                JUMP_FORWARD             1 (to L24)
       L23:     LOAD_CONST               3 (None)

 555   L24:     BUILD_MAP                2

 549            BUILD_MAP                6

 560            LOAD_CONST              12 ('warnings')
                BUILD_LIST               0

 561            LOAD_CONST              13 ('error_code')
                LOAD_CONST               3 (None)

 545            BUILD_MAP                6
                STORE_FAST               6 (out)

 573   L25:     LOAD_GLOBAL             15 (_final_envelope + NULL)
                LOAD_FAST_BORROW         6 (out)
                LOAD_CONST               9 ('tenant.audit_proof')
                LOAD_CONST              14 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --   L26:     PUSH_EXC_INFO

 563            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L30)
                NOT_TAKEN
                STORE_FAST              10 (e)

 564   L27:     LOAD_GLOBAL             20 (logger)
                LOAD_ATTR               23 (warning + NULL|self)

 565            LOAD_CONST              23 ('tenant_audit_proof_route error type=')
                LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 564            CALL                     1
                POP_TOP

 568            LOAD_CONST               5 ('status')
                LOAD_CONST               7 ('failed')

 569            LOAD_CONST               8 ('surface')
                LOAD_CONST               9 ('tenant.audit_proof')

 570            LOAD_CONST              13 ('error_code')
                LOAD_CONST              24 ('unexpected:')
                LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 571            LOAD_CONST              12 ('warnings')
                BUILD_LIST               0

 567            BUILD_MAP                4
                STORE_FAST               6 (out)
       L28:     POP_EXCEPT
                LOAD_CONST               3 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                JUMP_BACKWARD_NO_INTERRUPT 104 (to L25)

  --   L29:     LOAD_CONST               3 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RERAISE                  1

 563   L30:     RERAISE                  0

  --   L31:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L32:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L32 [0] lasti
  L3 to L6 -> L26 [0]
  L7 to L9 -> L26 [0]
  L10 to L12 -> L26 [0]
  L12 to L13 -> L32 [0] lasti
  L13 to L14 -> L26 [0]
  L15 to L25 -> L26 [0]
  L25 to L26 -> L32 [0] lasti
  L26 to L27 -> L31 [1] lasti
  L27 to L28 -> L29 [1] lasti
  L28 to L29 -> L32 [0] lasti
  L29 to L31 -> L31 [1] lasti
  L31 to L32 -> L32 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3D20, file "app\routes\tenant_portal.py", line 577>:
577           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('limit')

578           LOAD_CONST               2 ('int')

577           LOAD_CONST               3 ('return')

580           LOAD_CONST               4 ('Dict[str, Any]')

577           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object tenant_audit_route at 0x0000018C17EE1CC0, file "app\routes\tenant_portal.py", line 576>:
 576            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 588            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('tenant_audit_history',))
                IMPORT_NAME              0 (app.services.tenant.tenant_visibility_service)
                IMPORT_FROM              1 (tenant_audit_history)
                STORE_FAST               2 (tenant_audit_history)
                POP_TOP

 593    L2:     NOP

 594    L3:     LOAD_GLOBAL              5 (int + NULL)
                LOAD_FAST_BORROW         0 (limit)
                CALL                     1
                STORE_FAST               3 (capped)

 597    L4:     LOAD_FAST_BORROW         3 (capped)
                LOAD_SMALL_INT           1
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN

 598            LOAD_SMALL_INT           1
                STORE_FAST               3 (capped)

 599    L5:     LOAD_FAST_BORROW         3 (capped)
                LOAD_SMALL_INT         200
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN

 600            LOAD_SMALL_INT         200
                STORE_FAST               3 (capped)

 601    L6:     NOP

 602    L7:     LOAD_FAST_BORROW         2 (tenant_audit_history)
                PUSH_NULL
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 19 (brokerage, capped)
                LOAD_CONST               2 (('limit',))
                CALL_KW                  2
                STORE_FAST               4 (env)

 604            LOAD_CONST               3 ('status')
                LOAD_FAST_BORROW         4 (env)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               3 ('status')
                CALL                     1

 605            LOAD_CONST               4 ('surface')
                LOAD_CONST               5 ('tenant.audit_history')

 606            LOAD_CONST               6 ('brokerage_id')
                LOAD_FAST_BORROW         4 (env)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               6 ('brokerage_id')
                CALL                     1

 607            LOAD_CONST               7 ('payload')
                LOAD_FAST_BORROW         4 (env)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               7 ('payload')
                CALL                     1

 608            LOAD_CONST               8 ('warnings')
                LOAD_FAST_BORROW         4 (env)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               8 ('warnings')
                CALL                     1

 609            LOAD_CONST               9 ('error_code')
                LOAD_FAST_BORROW         4 (env)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               9 ('error_code')
                CALL                     1

 603            BUILD_MAP                6
                STORE_FAST               5 (out)

 621    L8:     LOAD_GLOBAL             23 (_final_envelope + NULL)
                LOAD_FAST_BORROW         5 (out)
                LOAD_CONST               5 ('tenant.audit_history')
                LOAD_CONST              14 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --    L9:     PUSH_EXC_INFO

 595            LOAD_GLOBAL              6 (TypeError)
                LOAD_GLOBAL              8 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L11)
                NOT_TAKEN
                POP_TOP

 596            LOAD_SMALL_INT          50
                STORE_FAST               3 (capped)
       L10:     POP_EXCEPT
                JUMP_BACKWARD_NO_INTERRUPT 151 (to L4)

 595   L11:     RERAISE                  0

  --   L12:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L13:     PUSH_EXC_INFO

 611            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L17)
                NOT_TAKEN
                STORE_FAST               6 (e)

 612   L14:     LOAD_GLOBAL             14 (logger)
                LOAD_ATTR               17 (warning + NULL|self)

 613            LOAD_CONST              10 ('tenant_audit_route error type=')
                LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 612            CALL                     1
                POP_TOP

 616            LOAD_CONST               3 ('status')
                LOAD_CONST              11 ('failed')

 617            LOAD_CONST               4 ('surface')
                LOAD_CONST               5 ('tenant.audit_history')

 618            LOAD_CONST               9 ('error_code')
                LOAD_CONST              12 ('unexpected:')
                LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 619            LOAD_CONST               8 ('warnings')
                BUILD_LIST               0

 615            BUILD_MAP                4
                STORE_FAST               5 (out)
       L15:     POP_EXCEPT
                LOAD_CONST              13 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                JUMP_BACKWARD_NO_INTERRUPT 129 (to L8)

  --   L16:     LOAD_CONST              13 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

 611   L17:     RERAISE                  0

  --   L18:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L19:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L19 [0] lasti
  L3 to L4 -> L9 [0]
  L4 to L6 -> L19 [0] lasti
  L7 to L8 -> L13 [0]
  L8 to L9 -> L19 [0] lasti
  L9 to L10 -> L12 [1] lasti
  L10 to L11 -> L19 [0] lasti
  L11 to L12 -> L12 [1] lasti
  L12 to L13 -> L19 [0] lasti
  L13 to L14 -> L18 [1] lasti
  L14 to L15 -> L16 [1] lasti
  L15 to L16 -> L19 [0] lasti
  L16 to L18 -> L18 [1] lasti
  L18 to L19 -> L19 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA1D40, file "app\routes\tenant_portal.py", line 625>:
625           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')

627           LOAD_CONST               2 ('Dict[str, Any]')

625           BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object tenant_callback_summary_route at 0x0000018C17D7CD90, file "app\routes\tenant_portal.py", line 624>:
 624            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0

 630            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('tenant_callback_summary',))
                IMPORT_NAME              0 (app.services.tenant.tenant_visibility_service)
                IMPORT_FROM              1 (tenant_callback_summary)
                STORE_FAST               1 (tenant_callback_summary)
                POP_TOP

 633    L2:     NOP

 634    L3:     LOAD_FAST_BORROW         1 (tenant_callback_summary)
                PUSH_NULL
                LOAD_FAST_BORROW         0 (brokerage)
                CALL                     1
                STORE_FAST               2 (env)

 636            LOAD_CONST               2 ('status')
                LOAD_FAST_BORROW         2 (env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               2 ('status')
                CALL                     1

 637            LOAD_CONST               3 ('surface')
                LOAD_CONST               4 ('tenant.callback_summary')

 638            LOAD_CONST               5 ('brokerage_id')
                LOAD_FAST_BORROW         2 (env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               5 ('brokerage_id')
                CALL                     1

 639            LOAD_CONST               6 ('payload')
                LOAD_FAST_BORROW         2 (env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               6 ('payload')
                CALL                     1

 640            LOAD_CONST               7 ('warnings')
                LOAD_FAST_BORROW         2 (env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               7 ('warnings')
                CALL                     1

 641            LOAD_CONST               8 ('error_code')
                LOAD_FAST_BORROW         2 (env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               8 ('error_code')
                CALL                     1

 635            BUILD_MAP                6
                STORE_FAST               3 (out)

 653    L4:     LOAD_GLOBAL             17 (_final_envelope + NULL)
                LOAD_FAST_BORROW         3 (out)
                LOAD_CONST               4 ('tenant.callback_summary')
                LOAD_CONST              13 (('surface',))
                CALL_KW                  2
                RETURN_VALUE

  --    L5:     PUSH_EXC_INFO

 643            LOAD_GLOBAL              6 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L9)
                NOT_TAKEN
                STORE_FAST               4 (e)

 644    L6:     LOAD_GLOBAL              8 (logger)
                LOAD_ATTR               11 (warning + NULL|self)

 645            LOAD_CONST               9 ('tenant_callback_summary_route error type=')
                LOAD_GLOBAL             13 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               14 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 644            CALL                     1
                POP_TOP

 648            LOAD_CONST               2 ('status')
                LOAD_CONST              10 ('failed')

 649            LOAD_CONST               3 ('surface')
                LOAD_CONST               4 ('tenant.callback_summary')

 650            LOAD_CONST               8 ('error_code')
                LOAD_CONST              11 ('unexpected:')
                LOAD_GLOBAL             13 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               14 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 651            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 647            BUILD_MAP                4
                STORE_FAST               3 (out)
        L7:     POP_EXCEPT
                LOAD_CONST              12 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                JUMP_BACKWARD_NO_INTERRUPT 104 (to L4)

  --    L8:     LOAD_CONST              12 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RERAISE                  1

 643    L9:     RERAISE                  0

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
