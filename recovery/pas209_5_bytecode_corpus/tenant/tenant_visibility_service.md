# tenant/tenant_visibility_service

- **pyc:** `app\services\tenant\__pycache__\tenant_visibility_service.cpython-314.pyc`
- **expected source path (absent):** `app\services\tenant/tenant_visibility_service.py`
- **co_filename (from bytecode):** `app\services\tenant\tenant_visibility_service.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** tenant

## Module docstring

```
PAS174 — Tenant visibility service.

Bounded, brokerage-scoped read surfaces for the tenant-side
``/tenant/*`` portal. Every helper takes a tenant brokerage
record (returned by ``require_brokerage`` at the route layer)
and returns a structural envelope scoped to that brokerage
ONLY.

Doctrine carried by every helper:

* **Brokerage-scoped only.** Every helper requires the resolved
  brokerage_id (from the route's auth layer) and refuses to
  read anything outside that scope. There is no
  ``brokerage_id`` kwarg — the value is unpacked from the
  brokerage dict to make cross-brokerage leakage
  structurally impossible.
* **Read-only.** No writes. No mutations.
* **No PII / no secrets / no operator notes / no transcripts
  / no raw payloads / no audit-log internals.** Every
  envelope is a closed-shape projection.
* **Bounded counts.** Where the underlying service surface
  returns rows, the tenant helper returns counts + a small
  number of structural row tokens, NEVER the row payload.
* **NEVER raises.** DB-unavailable or downstream-service
  failures collapse to a structural ``status="skipped"``
  envelope.
* **Closed allow-list for fields surfaced.** The route layer
  scans the envelope before returning; any leak collapses
  to a structural error.

Public surface:

  * ``tenant_status(brokerage)``
  * ``tenant_launch_readiness(brokerage)``
  * ``tenant_integration_posture(brokerage)``
  * ``tenant_callback_summary(brokerage)``
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.services.brokerage.config_validator`, `app.services.brokerage.profile_service`, `app.services.callbacks.callback_schedule`, `app.services.operator.audit_service`, `app.services.operator.connectivity_probes`, `app.services.tenant.tenant_audit_ack_store`, `brokerage_action_history`, `datetime`, `get_profile`, `list_pending_callbacks`, `logging`, `probe_calcom_configuration`, `probe_encryption_posture`, `probe_slack_webhook`, `probe_twilio_configuration`, `record_tenant_audit_acknowledgement`, `reminder_report`, `threading`, `timezone`, `typing`, `validate_brokerage_launch_ready`

## Classes

_none_

## Functions / methods

`__annotate__`, `_bound_entry_id`, `_bound_notes_token`, `_peek_tenant_audit_ack_registry_for_tests`, `_project_profile`, `_project_tenant_audit_row`, `_resolve_brokerage_id`, `_safe_envelope`, `_scan_for_forbidden`, `acknowledge_tenant_audit_entry`, `reset_tenant_audit_ack_registry_for_tests`, `tenant_audit_history`, `tenant_callback_summary`, `tenant_integration_posture`, `tenant_launch_readiness`, `tenant_status`

## Env-key candidates

`AUDIT_ENTRY_VIEWED`, `PENDING`, `TENANT`

## String constants (redacted where noted)

- '\nPAS174 — Tenant visibility service.\n\nBounded, brokerage-scoped read surfaces for the tenant-side\n``/tenant/*`` portal. Every helper takes a tenant brokerage\nrecord (returned by ``require_brokerage`` at the route layer)\nand returns a structural envelope scoped to that brokerage\nONLY.\n\nDoctrine carried by every helper:\n\n* **Brokerage-scoped only.** Every helper requires the resolved\n  brokerage_id (from the route\'s auth layer) and refuses to\n  read anything outside that scope. There is no\n  ``brokerage_id`` kwarg — the value is unpacked from the\n  brokerage dict to make cross-brokerage leakage\n  structurally impossible.\n* **Read-only.** No writes. No mutations.\n* **No PII / no secrets / no operator notes / no transcripts\n  / no raw payloads / no audit-log internals.** Every\n  envelope is a closed-shape projection.\n* **Bounded counts.** Where the underlying service surface\n  returns rows, the tenant helper returns counts + a small\n  number of structural row tokens, NEVER the row payload.\n* **NEVER raises.** DB-unavailable or downstream-service\n  failures collapse to a structural ``status="skipped"``\n  envelope.\n* **Closed allow-list for fields surfaced.** The route layer\n  scans the envelope before returning; any leak collapses\n  to a structural error.\n\nPublic surface:\n\n  * ``tenant_status(brokerage)``\n  * ``tenant_launch_readiness(brokerage)``\n  * ``tenant_integration_posture(brokerage)``\n  * ``tenant_callback_summary(brokerage)``\n'
- 'pas.tenant.visibility_service'
- 'action_id'
- 'payload'
- 'warnings'
- 'error_code'
- 'entry_id'
- 'limit'
- 🔒 '<REDACTED:high-entropy blob, len=64>'
- 'Dict[str, Dict[str, Any]]'
- '_TENANT_ACK_REGISTRY'
- 'actor_token'
- 'notes_token'
- 'now'
- 'brokerage'
- 'Any'
- 'return'
- 'Optional[str]'
- 'profile'
- 'Optional[Dict[str, Any]]'
- 'status'
- 'str'
- 'brokerage_id'
- 'Optional[List[str]]'
- 'Dict[str, Any]'
- 'envelope'
- 'Defensive — walk the envelope and return the first\nforbidden field substring found in any KEY (we only scan\nkeys, not string values; tenant payloads do not include\narbitrary string content). NEVER raises.'
- 'obj'
- "Return the brokerage's PAS173 profile snapshot (status +\nstage + timestamps). NEVER raises."
- 'failed'
- 'missing_brokerage_id'
- 'skipped'
- 'onboarding_status'
- 'pilot_stage'
- 'profile_present'
- 'tenant_status error type='
- 'unexpected:'
- 'tenant_status_unavailable'
- 'Tenant-safe projection of the PAS173 launch-readiness\nsurface. Returns warning + error COUNTS (not the\nstructural tokens themselves — the tokens belong to the\noperator surface). NEVER raises.'
- 'launch_ready'
- 'warning_count'
- 'error_count'
- 'tenant_launch_readiness error type='
- 'tenant_launch_readiness_unavailable'
- 'Tenant-safe projection of the integration posture\n(Twilio / Slack / Cal.com / encryption). Returns\npresence-only booleans + structural warning counts. NEVER\nechoes any secret or env value.'
- 'twilio_phone'
- 'timezone'
- 'twilio'
- 'brokerage_twilio_phone_present'
- 'summary'
- 'slack_webhook'
- 'calcom'
- 'brokerage_timezone_present'
- 'encryption_posture'
- 'encryption_enabled'
- 'tenant_integration_posture error type='
- 'tenant_integrations_unavailable'
- 'Tenant-safe callback summary. Returns COUNTS only\n(due / overdue / pending). NEVER returns callback_ids,\nsource_call_ids, or any per-row payload.'
- 'PENDING'
- 'due_count'
- 'overdue_count'
- 'pending_count'
- 'count'
- 'tenant_callback_summary error type='
- 'tenant_callbacks_unavailable'
- 'row'
- 'metadata'
- "Tenant-safe audit visibility. Returns the brokerage's\nown audit rows projected against the closed tenant\nallow-list. NEVER raises. NEVER exposes actor_id,\noperator notes, or operator-side metadata internals."
- 'rows'
- 'tenant_audit_history error type='
- 'tenant_audit_unavailable'
- 'value'
- 'Tenant-side acknowledgement of an audit entry.\n\n**PAS177**: this helper now consults the durable\n``tenant_audit_ack_store`` first. On any failure path\n(DB unavailable / validation rejected at the durable\nlayer) it falls back to the PAS176 process-local\nregistry. The public surface is unchanged.\n\nReturns a structural envelope. NEVER raises. NEVER\nmodifies the audit row. NEVER stores PII.\n'
- 'missing_or_invalid_entry_id'
- 'invalid_notes_token'
- 'AUDIT_ENTRY_VIEWED'
- 'TENANT'
- 'ack_row'
- 'duplicate'
- 'acknowledged_at'
- 'tenant_audit_ack_store_is_durable'
- 'acknowledge_tenant_audit_entry durable layer error type='
- 'seconds'
- 'tenant_audit_ack_store_is_process_local'
- 'None'
- 'Test-only helper to flush the in-memory registry.'

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS174 — Tenant visibility service.\n\nBounded, brokerage-scoped read surfaces for the tenant-side\n``/tenant/*`` portal. Every helper takes a tenant brokerage\nrecord (returned by ``require_brokerage`` at the route layer)\nand returns a structural envelope scoped to that brokerage\nONLY.\n\nDoctrine carried by every helper:\n\n* **Brokerage-scoped only.** Every helper requires the resolved\n  brokerage_id (from the route\'s auth layer) and refuses to\n  read anything outside that scope. There is no\n  ``brokerage_id`` kwarg — the value is unpacked from the\n  brokerage dict to make cross-brokerage leakage\n  structurally impossible.\n* **Read-only.** No writes. No mutations.\n* **No PII / no secrets / no operator notes / no transcripts\n  / no raw payloads / no audit-log internals.** Every\n  envelope is a closed-shape projection.\n* **Bounded counts.** Where the underlying service surface\n  returns rows, the tenant helper returns counts + a small\n  number of structural row tokens, NEVER the row payload.\n* **NEVER raises.** DB-unavailable or downstream-service\n  failures collapse to a structural ``status="skipped"``\n  envelope.\n* **Closed allow-list for fields surfaced.** The route layer\n  scans the envelope before returning; any leak collapses\n  to a structural error.\n\nPublic surface:\n\n  * ``tenant_status(brokerage)``\n  * ``tenant_launch_readiness(brokerage)``\n  * ``tenant_integration_posture(brokerage)``\n  * ``tenant_callback_summary(brokerage)``\n')
               STORE_NAME               1 (__doc__)

  40           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  42           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (logging)
               STORE_NAME               4 (logging)

  43           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('Any', 'Dict', 'List', 'Optional'))
               IMPORT_NAME              5 (typing)
               IMPORT_FROM              6 (Any)
               STORE_NAME               6 (Any)
               IMPORT_FROM              7 (Dict)
               STORE_NAME               7 (Dict)
               IMPORT_FROM              8 (List)
               STORE_NAME               8 (List)
               IMPORT_FROM              9 (Optional)
               STORE_NAME               9 (Optional)
               POP_TOP

  46           LOAD_NAME                4 (logging)
               LOAD_ATTR               20 (getLogger)
               PUSH_NULL
               LOAD_CONST               4 ('pas.tenant.visibility_service')
               CALL                     1
               STORE_NAME              11 (logger)

  57           LOAD_CONST              47 (('brokerage_id', 'brokerage_name', 'timezone', 'market', 'onboarding_status', 'pilot_stage', 'onboarding_completed_at', 'config_version', 'created_at', 'updated_at'))
               STORE_NAME              12 (_TENANT_PROFILE_FIELDS)

  72           LOAD_CONST              48 (('phone', 'email', 'name_token', 'raw_payload', 'raw_email', 'raw_body', 'transcript', 'summary_text', 'secret', 'signature', 'dedupe_key', 'callback_notes', 'operator_notes', 'audit', 'action_id', 'actor_id', 'env_value', 'env_values', 'slack_internal', 'memory_candidate'))
               STORE_NAME              13 (_FORBIDDEN_TENANT_FIELDS)

  89           LOAD_CONST               6 (<code object __annotate__ at 0x0000018C17FA3780, file "app\services\tenant\tenant_visibility_service.py", line 89>)
               MAKE_FUNCTION
               LOAD_CONST               7 (<code object _resolve_brokerage_id at 0x0000018C1796DBD0, file "app\services\tenant\tenant_visibility_service.py", line 89>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              14 (_resolve_brokerage_id)

  98           LOAD_CONST               8 (<code object __annotate__ at 0x0000018C17FA2A60, file "app\services\tenant\tenant_visibility_service.py", line 98>)
               MAKE_FUNCTION
               LOAD_CONST               9 (<code object _project_profile at 0x0000018C17FE13E0, file "app\services\tenant\tenant_visibility_service.py", line 98>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              15 (_project_profile)

 108           LOAD_CONST              10 ('payload')

 112           LOAD_CONST               2 (None)

 108           LOAD_CONST              11 ('warnings')

 113           LOAD_CONST               2 (None)

 108           LOAD_CONST              12 ('error_code')

 114           LOAD_CONST               2 (None)

 108           BUILD_MAP                3
               LOAD_CONST              13 (<code object __annotate__ at 0x0000018C18025A30, file "app\services\tenant\tenant_visibility_service.py", line 108>)
               MAKE_FUNCTION
               LOAD_CONST              14 (<code object _safe_envelope at 0x0000018C17FBFEE0, file "app\services\tenant\tenant_visibility_service.py", line 108>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              16 (_safe_envelope)

 125           LOAD_CONST              15 (<code object __annotate__ at 0x0000018C17FA2970, file "app\services\tenant\tenant_visibility_service.py", line 125>)
               MAKE_FUNCTION
               LOAD_CONST              16 (<code object _scan_for_forbidden at 0x0000018C18025730, file "app\services\tenant\tenant_visibility_service.py", line 125>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              17 (_scan_for_forbidden)

 157           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C17FA23D0, file "app\services\tenant\tenant_visibility_service.py", line 157>)
               MAKE_FUNCTION
               LOAD_CONST              18 (<code object tenant_status at 0x0000018C182FEA10, file "app\services\tenant\tenant_visibility_service.py", line 157>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              18 (tenant_status)

 205           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA3B40, file "app\services\tenant\tenant_visibility_service.py", line 205>)
               MAKE_FUNCTION
               LOAD_CONST              20 (<code object tenant_launch_readiness at 0x0000018C17ED2060, file "app\services\tenant\tenant_visibility_service.py", line 205>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              19 (tenant_launch_readiness)

 246           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA34B0, file "app\services\tenant\tenant_visibility_service.py", line 246>)
               MAKE_FUNCTION
               LOAD_CONST              22 (<code object tenant_integration_posture at 0x0000018C17E8F9D0, file "app\services\tenant\tenant_visibility_service.py", line 246>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              20 (tenant_integration_posture)

 325           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA1E30, file "app\services\tenant\tenant_visibility_service.py", line 325>)
               MAKE_FUNCTION
               LOAD_CONST              24 (<code object tenant_callback_summary at 0x0000018C17F76FD0, file "app\services\tenant\tenant_visibility_service.py", line 325>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              21 (tenant_callback_summary)

 375           LOAD_CONST              49 (('action_id', 'occurred_at', 'action', 'status', 'target_type'))
               STORE_NAME              22 (_TENANT_AUDIT_FIELDS_SOURCE)

 388           LOAD_CONST               5 ('action_id')
               LOAD_CONST              25 ('entry_id')

 387           BUILD_MAP                1
               STORE_NAME              23 (_TENANT_AUDIT_FIELD_RENAME)

 394           LOAD_CONST              50 (('stage', 'target_status', 'onboarding_status', 'pilot_stage', 'launch_ready'))
               STORE_NAME              24 (_TENANT_AUDIT_METADATA_KEYS)

 403           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA32D0, file "app\services\tenant\tenant_visibility_service.py", line 403>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object _project_tenant_audit_row at 0x0000018C17F64050, file "app\services\tenant\tenant_visibility_service.py", line 403>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              25 (_project_tenant_audit_row)

 426           LOAD_CONST              28 ('limit')

 429           LOAD_SMALL_INT          50

 426           BUILD_MAP                1
               LOAD_CONST              29 (<code object __annotate__ at 0x0000018C18025230, file "app\services\tenant\tenant_visibility_service.py", line 426>)
               MAKE_FUNCTION
               LOAD_CONST              30 (<code object tenant_audit_history at 0x0000018C18646C00, file "app\services\tenant\tenant_visibility_service.py", line 426>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              26 (tenant_audit_history)

 505           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME             27 (threading)
               STORE_NAME              28 (_ack_threading)

 509           LOAD_CONST              31 ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_')

 508           STORE_NAME              29 (_ALLOWED_NOTES_TOKEN_CHARS)

 514           BUILD_MAP                0
               STORE_NAME              30 (_TENANT_ACK_REGISTRY)
               LOAD_CONST              32 ('Dict[str, Dict[str, Any]]')
               LOAD_NAME               31 (__annotations__)
               LOAD_CONST              33 ('_TENANT_ACK_REGISTRY')
               STORE_SUBSCR

 515           LOAD_NAME               28 (_ack_threading)
               LOAD_ATTR               64 (RLock)
               PUSH_NULL
               CALL                     0
               STORE_NAME              33 (_TENANT_ACK_LOCK)

 518           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA3E10, file "app\services\tenant\tenant_visibility_service.py", line 518>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object _bound_entry_id at 0x0000018C18010B30, file "app\services\tenant\tenant_visibility_service.py", line 518>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              34 (_bound_entry_id)

 527           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C17FA3A50, file "app\services\tenant\tenant_visibility_service.py", line 527>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object _bound_notes_token at 0x0000018C1801C410, file "app\services\tenant\tenant_visibility_service.py", line 527>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              35 (_bound_notes_token)

 542           LOAD_CONST              38 ('actor_token')

 546           LOAD_CONST               2 (None)

 542           LOAD_CONST              39 ('notes_token')

 547           LOAD_CONST               2 (None)

 542           LOAD_CONST              40 ('now')

 548           LOAD_CONST               2 (None)

 542           BUILD_MAP                3
               LOAD_CONST              41 (<code object __annotate__ at 0x0000018C18026230, file "app\services\tenant\tenant_visibility_service.py", line 542>)
               MAKE_FUNCTION
               LOAD_CONST              42 (<code object acknowledge_tenant_audit_entry at 0x0000018C17F7B2B0, file "app\services\tenant\tenant_visibility_service.py", line 542>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              36 (acknowledge_tenant_audit_entry)

 672           LOAD_CONST              43 (<code object __annotate__ at 0x0000018C17FA33C0, file "app\services\tenant\tenant_visibility_service.py", line 672>)
               MAKE_FUNCTION
               LOAD_CONST              44 (<code object reset_tenant_audit_ack_registry_for_tests at 0x0000018C18011370, file "app\services\tenant\tenant_visibility_service.py", line 672>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              37 (reset_tenant_audit_ack_registry_for_tests)

 678           LOAD_CONST              45 (<code object __annotate__ at 0x0000018C17FA1D40, file "app\services\tenant\tenant_visibility_service.py", line 678>)
               MAKE_FUNCTION
               LOAD_CONST              46 (<code object _peek_tenant_audit_ack_registry_for_tests at 0x0000018C1804D3B0, file "app\services\tenant\tenant_visibility_service.py", line 678>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              38 (_peek_tenant_audit_ack_registry_for_tests)

 683           BUILD_LIST               0
               LOAD_CONST              51 (('tenant_status', 'tenant_launch_readiness', 'tenant_integration_posture', 'tenant_callback_summary', 'tenant_audit_history', 'acknowledge_tenant_audit_entry', 'reset_tenant_audit_ack_registry_for_tests'))
               LIST_EXTEND              1
               STORE_NAME              39 (__all__)
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "app\services\tenant\tenant_visibility_service.py", line 89>:
 89           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _resolve_brokerage_id at 0x0000018C1796DBD0, file "app\services\tenant\tenant_visibility_service.py", line 89>:
 89           RESUME                   0

 90           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (brokerage)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

 91           LOAD_CONST               0 (None)
              RETURN_VALUE

 92   L1:     LOAD_FAST_BORROW         0 (brokerage)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               1 ('id')
              CALL                     1
              STORE_FAST               1 (bid)

 93           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (bid)
              LOAD_GLOBAL              6 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       23 (to L2)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (bid)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN

 94   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

 95   L3:     LOAD_FAST_BORROW         1 (bid)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "app\services\tenant\tenant_visibility_service.py", line 98>:
 98           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('profile')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[Dict[str, Any]]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _project_profile at 0x0000018C17FE13E0, file "app\services\tenant\tenant_visibility_service.py", line 98>:
 98           RESUME                   0

 99           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (profile)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

100           LOAD_CONST               0 (None)
              RETURN_VALUE

101   L1:     BUILD_MAP                0
              STORE_FAST               1 (out)

102           LOAD_GLOBAL              4 (_TENANT_PROFILE_FIELDS)
              GET_ITER
      L2:     FOR_ITER                21 (to L4)
              STORE_FAST               2 (col)

103           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (col, profile)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

104   L3:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (profile, col)
              BINARY_OP               26 ([])
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (out, col)
              STORE_SUBSCR
              JUMP_BACKWARD           23 (to L2)

102   L4:     END_FOR
              POP_ITER

105           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025A30, file "app\services\tenant\tenant_visibility_service.py", line 108>:
108           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')

110           LOAD_CONST               2 ('str')

108           LOAD_CONST               3 ('brokerage_id')

111           LOAD_CONST               4 ('Optional[str]')

108           LOAD_CONST               5 ('payload')

112           LOAD_CONST               6 ('Optional[Dict[str, Any]]')

108           LOAD_CONST               7 ('warnings')

113           LOAD_CONST               8 ('Optional[List[str]]')

108           LOAD_CONST               9 ('error_code')

114           LOAD_CONST               4 ('Optional[str]')

108           LOAD_CONST              10 ('return')

115           LOAD_CONST              11 ('Dict[str, Any]')

108           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _safe_envelope at 0x0000018C17FBFEE0, file "app\services\tenant\tenant_visibility_service.py", line 108>:
108           RESUME                   0

117           LOAD_CONST               0 ('status')
              LOAD_FAST                0 (status)

118           LOAD_CONST               1 ('brokerage_id')
              LOAD_FAST                1 (brokerage_id)

119           LOAD_CONST               2 ('payload')
              LOAD_FAST                2 (payload)

120           LOAD_CONST               3 ('warnings')
              LOAD_GLOBAL              1 (list + NULL)
              LOAD_FAST                3 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

121           LOAD_CONST               4 ('error_code')
              LOAD_FAST_BORROW         4 (error_code)

116           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "app\services\tenant\tenant_visibility_service.py", line 125>:
125           RESUME                   0
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

Disassembly of <code object _scan_for_forbidden at 0x0000018C18025730, file "app\services\tenant\tenant_visibility_service.py", line 125>:
  --           MAKE_CELL                1 (walk)

 125           RESUME                   0

 130           LOAD_CONST               1 (<code object __annotate__ at 0x0000018C17FA3D20, file "app\services\tenant\tenant_visibility_service.py", line 130>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         1 (walk)
               BUILD_TUPLE              1
               LOAD_CONST               2 (<code object walk at 0x0000018C17CC1CE0, file "app\services\tenant\tenant_visibility_service.py", line 130>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_DEREF              1 (walk)

 150           LOAD_DEREF               1 (walk)
               PUSH_NULL
               LOAD_FAST_BORROW         0 (envelope)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3D20, file "app\services\tenant\tenant_visibility_service.py", line 130>:
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

Disassembly of <code object walk at 0x0000018C17CC1CE0, file "app\services\tenant\tenant_visibility_service.py", line 130>:
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

 136            LOAD_GLOBAL             10 (_FORBIDDEN_TENANT_FIELDS)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "app\services\tenant\tenant_visibility_service.py", line 157>:
157           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object tenant_status at 0x0000018C182FEA10, file "app\services\tenant\tenant_visibility_service.py", line 157>:
 157            RESUME                   0

 160            LOAD_GLOBAL              1 (_resolve_brokerage_id + NULL)
                LOAD_FAST_BORROW         0 (brokerage)
                CALL                     1
                STORE_FAST               1 (bid)

 161            LOAD_FAST_BORROW         1 (bid)
                POP_JUMP_IF_NOT_NONE    15 (to L1)
                NOT_TAKEN

 162            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 163            LOAD_CONST               2 ('failed')

 164            LOAD_CONST               1 (None)

 165            LOAD_CONST               3 ('missing_brokerage_id')

 162            LOAD_CONST               4 (('status', 'brokerage_id', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 167    L1:     NOP

 168    L2:     LOAD_SMALL_INT           0
                LOAD_CONST               5 (('get_profile',))
                IMPORT_NAME              2 (app.services.brokerage.profile_service)
                IMPORT_FROM              3 (get_profile)
                STORE_FAST               2 (get_profile)
                POP_TOP

 169            LOAD_FAST_BORROW         2 (get_profile)
                PUSH_NULL
                LOAD_FAST_BORROW         1 (bid)
                CALL                     1
                STORE_FAST               3 (env)

 170            LOAD_FAST_BORROW         3 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               6 ('status')
                CALL                     1
                LOAD_CONST               7 ('ok')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       97 (to L10)
                NOT_TAKEN

 171            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 172            LOAD_FAST_BORROW         3 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               6 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
        L3:     NOT_TAKEN
        L4:     POP_TOP
                LOAD_CONST               8 ('skipped')

 173    L5:     LOAD_FAST                1 (bid)

 175            LOAD_CONST               9 ('onboarding_status')
                LOAD_CONST               1 (None)

 176            LOAD_CONST              10 ('pilot_stage')
                LOAD_CONST               1 (None)

 177            LOAD_CONST              11 ('profile_present')
                LOAD_CONST              12 (False)

 174            BUILD_MAP                3

 179            LOAD_GLOBAL             11 (list + NULL)
                LOAD_FAST_BORROW         3 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              13 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
        L6:     NOT_TAKEN
        L7:     POP_TOP
                BUILD_LIST               0
        L8:     CALL                     1

 180            LOAD_FAST_BORROW         3 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              14 ('error_code')
                CALL                     1

 171            LOAD_CONST              15 (('status', 'brokerage_id', 'payload', 'warnings', 'error_code'))
                CALL_KW                  5
        L9:     RETURN_VALUE

 182   L10:     LOAD_GLOBAL             13 (_project_profile + NULL)
                LOAD_FAST_BORROW         3 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              16 ('profile')
                CALL                     1
                CALL                     1
                STORE_FAST               4 (proj)

 183            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 184            LOAD_CONST               7 ('ok')

 185            LOAD_FAST                1 (bid)

 187            LOAD_CONST               9 ('onboarding_status')
                LOAD_FAST                4 (proj)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
       L11:     NOT_TAKEN
       L12:     POP_TOP
                BUILD_MAP                0
       L13:     LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               9 ('onboarding_status')
                CALL                     1

 188            LOAD_CONST              10 ('pilot_stage')
                LOAD_FAST                4 (proj)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L16)
       L14:     NOT_TAKEN
       L15:     POP_TOP
                BUILD_MAP                0
       L16:     LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              10 ('pilot_stage')
                CALL                     1

 189            LOAD_CONST              16 ('profile')
                LOAD_FAST_BORROW         4 (proj)

 190            LOAD_CONST              11 ('profile_present')
                LOAD_FAST_BORROW         4 (proj)
                LOAD_CONST               1 (None)
                IS_OP                    1 (is not)

 186            BUILD_MAP                4

 183            LOAD_CONST              17 (('status', 'brokerage_id', 'payload'))
                CALL_KW                  3
       L17:     RETURN_VALUE

  --   L18:     PUSH_EXC_INFO

 193            LOAD_GLOBAL             14 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       92 (to L23)
                NOT_TAKEN
                STORE_FAST               5 (e)

 194   L19:     LOAD_GLOBAL             16 (logger)
                LOAD_ATTR               19 (warning + NULL|self)

 195            LOAD_CONST              18 ('tenant_status error type=')
                LOAD_GLOBAL             21 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               22 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 194            CALL                     1
                POP_TOP

 197            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 198            LOAD_CONST               8 ('skipped')

 199            LOAD_FAST                1 (bid)

 200            LOAD_CONST              19 ('unexpected:')
                LOAD_GLOBAL             21 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               22 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 201            LOAD_CONST              20 ('tenant_status_unavailable')

 197            LOAD_CONST              21 (('status', 'brokerage_id', 'warnings', 'error_code'))
                CALL_KW                  4
       L20:     SWAP                     2
       L21:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RETURN_VALUE

  --   L22:     LOAD_CONST               1 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RERAISE                  1

 193   L23:     RERAISE                  0

  --   L24:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L18 [0]
  L4 to L6 -> L18 [0]
  L7 to L9 -> L18 [0]
  L10 to L11 -> L18 [0]
  L12 to L14 -> L18 [0]
  L15 to L17 -> L18 [0]
  L18 to L19 -> L24 [1] lasti
  L19 to L20 -> L22 [1] lasti
  L20 to L21 -> L24 [1] lasti
  L22 to L24 -> L24 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "app\services\tenant\tenant_visibility_service.py", line 205>:
205           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object tenant_launch_readiness at 0x0000018C17ED2060, file "app\services\tenant\tenant_visibility_service.py", line 205>:
 205            RESUME                   0

 210            LOAD_GLOBAL              1 (_resolve_brokerage_id + NULL)
                LOAD_FAST_BORROW         0 (brokerage)
                CALL                     1
                STORE_FAST               1 (bid)

 211            LOAD_FAST_BORROW         1 (bid)
                POP_JUMP_IF_NOT_NONE    15 (to L1)
                NOT_TAKEN

 212            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 213            LOAD_CONST               2 ('failed')

 214            LOAD_CONST               1 (None)

 215            LOAD_CONST               3 ('missing_brokerage_id')

 212            LOAD_CONST               4 (('status', 'brokerage_id', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 217    L1:     NOP

 218    L2:     LOAD_SMALL_INT           0
                LOAD_CONST               5 (('get_profile',))
                IMPORT_NAME              2 (app.services.brokerage.profile_service)
                IMPORT_FROM              3 (get_profile)
                STORE_FAST               2 (get_profile)
                POP_TOP

 219            LOAD_SMALL_INT           0
                LOAD_CONST               6 (('validate_brokerage_launch_ready',))
                IMPORT_NAME              4 (app.services.brokerage.config_validator)
                IMPORT_FROM              5 (validate_brokerage_launch_ready)
                STORE_FAST               3 (validate_brokerage_launch_ready)
                POP_TOP

 222            LOAD_FAST_BORROW         2 (get_profile)
                PUSH_NULL
                LOAD_FAST_BORROW         1 (bid)
                CALL                     1
                STORE_FAST               4 (profile_env)

 223            LOAD_GLOBAL             13 (isinstance + NULL)
                LOAD_FAST_BORROW         4 (profile_env)
                LOAD_GLOBAL             14 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L3)
                NOT_TAKEN
                LOAD_FAST_BORROW         4 (profile_env)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST               7 ('profile')
                CALL                     1
                JUMP_FORWARD             1 (to L4)
        L3:     LOAD_CONST               1 (None)
        L4:     STORE_FAST               5 (profile)

 224            LOAD_FAST_BORROW         3 (validate_brokerage_launch_ready)
                PUSH_NULL
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (brokerage, profile)
                LOAD_CONST               8 (('profile',))
                CALL_KW                  2
                STORE_FAST               6 (env)

 226            LOAD_CONST               9 ('launch_ready')
                LOAD_GLOBAL             19 (bool + NULL)
                LOAD_FAST_BORROW         6 (env)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST               9 ('launch_ready')
                CALL                     1
                CALL                     1

 227            LOAD_CONST              10 ('warning_count')
                LOAD_GLOBAL             21 (int + NULL)
                LOAD_FAST_BORROW         6 (env)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              10 ('warning_count')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN
                POP_TOP
                LOAD_SMALL_INT           0
        L5:     CALL                     1

 228            LOAD_CONST              11 ('error_count')
                LOAD_GLOBAL             21 (int + NULL)
                LOAD_FAST_BORROW         6 (env)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              11 ('error_count')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
        L6:     NOT_TAKEN
        L7:     POP_TOP
                LOAD_SMALL_INT           0
        L8:     CALL                     1

 229            LOAD_CONST              12 ('profile_present')
                LOAD_FAST_BORROW         5 (profile)
                LOAD_CONST               1 (None)
                IS_OP                    1 (is not)

 225            BUILD_MAP                4
                STORE_FAST               7 (payload)

 231            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 232            LOAD_CONST              13 ('ok')
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 23 (bid, payload)

 231            LOAD_CONST              14 (('status', 'brokerage_id', 'payload'))
                CALL_KW                  3
        L9:     RETURN_VALUE

  --   L10:     PUSH_EXC_INFO

 234            LOAD_GLOBAL             22 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       92 (to L15)
                NOT_TAKEN
                STORE_FAST               8 (e)

 235   L11:     LOAD_GLOBAL             24 (logger)
                LOAD_ATTR               27 (warning + NULL|self)

 236            LOAD_CONST              15 ('tenant_launch_readiness error type=')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 235            CALL                     1
                POP_TOP

 238            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 239            LOAD_CONST              16 ('skipped')

 240            LOAD_FAST                1 (bid)

 241            LOAD_CONST              17 ('unexpected:')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 242            LOAD_CONST              18 ('tenant_launch_readiness_unavailable')

 238            LOAD_CONST              19 (('status', 'brokerage_id', 'warnings', 'error_code'))
                CALL_KW                  4
       L12:     SWAP                     2
       L13:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RETURN_VALUE

  --   L14:     LOAD_CONST               1 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RERAISE                  1

 234   L15:     RERAISE                  0

  --   L16:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L6 -> L10 [0]
  L7 to L9 -> L10 [0]
  L10 to L11 -> L16 [1] lasti
  L11 to L12 -> L14 [1] lasti
  L12 to L13 -> L16 [1] lasti
  L14 to L16 -> L16 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "app\services\tenant\tenant_visibility_service.py", line 246>:
246           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object tenant_integration_posture at 0x0000018C17E8F9D0, file "app\services\tenant\tenant_visibility_service.py", line 246>:
 246            RESUME                   0

 251            LOAD_GLOBAL              1 (_resolve_brokerage_id + NULL)
                LOAD_FAST_BORROW         0 (brokerage)
                CALL                     1
                STORE_FAST               1 (bid)

 252            LOAD_FAST_BORROW         1 (bid)
                POP_JUMP_IF_NOT_NONE    15 (to L1)
                NOT_TAKEN

 253            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 254            LOAD_CONST               2 ('failed')

 255            LOAD_CONST               1 (None)

 256            LOAD_CONST               3 ('missing_brokerage_id')

 253            LOAD_CONST               4 (('status', 'brokerage_id', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 258    L1:     NOP

 259    L2:     LOAD_SMALL_INT           0
                LOAD_CONST               5 (('probe_twilio_configuration', 'probe_slack_webhook', 'probe_calcom_configuration', 'probe_encryption_posture'))
                IMPORT_NAME              2 (app.services.operator.connectivity_probes)
                IMPORT_FROM              3 (probe_twilio_configuration)
                STORE_FAST               2 (probe_twilio_configuration)
                IMPORT_FROM              4 (probe_slack_webhook)
                STORE_FAST               3 (probe_slack_webhook)
                IMPORT_FROM              5 (probe_calcom_configuration)
                STORE_FAST               4 (probe_calcom_configuration)
                IMPORT_FROM              6 (probe_encryption_posture)
                STORE_FAST               5 (probe_encryption_posture)
                POP_TOP

 273            LOAD_CONST               6 ('id')
                LOAD_FAST                1 (bid)

 274            LOAD_CONST               7 ('twilio_phone')

 275            LOAD_GLOBAL             15 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (brokerage)
                LOAD_GLOBAL             16 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L3)
                NOT_TAKEN

 274            LOAD_FAST_BORROW         0 (brokerage)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST               7 ('twilio_phone')
                CALL                     1
                JUMP_FORWARD             1 (to L4)

 275    L3:     LOAD_CONST               1 (None)

 276    L4:     LOAD_CONST               8 ('timezone')

 277            LOAD_GLOBAL             15 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (brokerage)
                LOAD_GLOBAL             16 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L5)
                NOT_TAKEN

 276            LOAD_FAST_BORROW         0 (brokerage)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST               8 ('timezone')
                CALL                     1
                JUMP_FORWARD             1 (to L6)

 277    L5:     LOAD_CONST               1 (None)

 272    L6:     BUILD_MAP                3
                STORE_FAST               6 (tenant_view)

 282            LOAD_FAST_BORROW         2 (probe_twilio_configuration)
                PUSH_NULL
                LOAD_FAST_BORROW         6 (tenant_view)
                LOAD_CONST               9 (('brokerage',))
                CALL_KW                  1
                STORE_FAST               7 (twilio)

 283            LOAD_FAST_BORROW         3 (probe_slack_webhook)
                PUSH_NULL
                LOAD_CONST               1 (None)
                LOAD_CONST               9 (('brokerage',))
                CALL_KW                  1
                STORE_FAST               8 (slack)

 284            LOAD_FAST_BORROW         4 (probe_calcom_configuration)
                PUSH_NULL
                LOAD_FAST_BORROW         6 (tenant_view)
                LOAD_CONST               9 (('brokerage',))
                CALL_KW                  1
                STORE_FAST               9 (calcom)

 285            LOAD_FAST_BORROW         5 (probe_encryption_posture)
                PUSH_NULL
                CALL                     0
                STORE_FAST              10 (enc)

 288            LOAD_CONST              10 ('twilio')

 289            LOAD_CONST              11 ('status')
                LOAD_FAST_BORROW         7 (twilio)
                LOAD_CONST              11 ('status')
                BINARY_OP               26 ([])

 290            LOAD_CONST              12 ('warning_count')
                LOAD_GLOBAL             21 (len + NULL)
                LOAD_FAST_BORROW         7 (twilio)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              13 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
        L7:     NOT_TAKEN
        L8:     POP_TOP
                BUILD_LIST               0
        L9:     CALL                     1

 291            LOAD_CONST              14 ('brokerage_twilio_phone_present')

 292            LOAD_FAST_BORROW         7 (twilio)
                LOAD_CONST              15 ('summary')
                BINARY_OP               26 ([])
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              14 ('brokerage_twilio_phone_present')
                LOAD_CONST              16 (False)
                CALL                     2

 288            BUILD_MAP                3

 294            LOAD_CONST              17 ('slack_webhook')

 295            LOAD_CONST              11 ('status')
                LOAD_FAST_BORROW         8 (slack)
                LOAD_CONST              11 ('status')
                BINARY_OP               26 ([])

 296            LOAD_CONST              12 ('warning_count')
                LOAD_GLOBAL             21 (len + NULL)
                LOAD_FAST_BORROW         8 (slack)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              13 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L12)
       L10:     NOT_TAKEN
       L11:     POP_TOP
                BUILD_LIST               0
       L12:     CALL                     1

 294            BUILD_MAP                2

 298            LOAD_CONST              18 ('calcom')

 299            LOAD_CONST              11 ('status')
                LOAD_FAST_BORROW         9 (calcom)
                LOAD_CONST              11 ('status')
                BINARY_OP               26 ([])

 300            LOAD_CONST              12 ('warning_count')
                LOAD_GLOBAL             21 (len + NULL)
                LOAD_FAST_BORROW         9 (calcom)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              13 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L15)
       L13:     NOT_TAKEN
       L14:     POP_TOP
                BUILD_LIST               0
       L15:     CALL                     1

 301            LOAD_CONST              19 ('brokerage_timezone_present')

 302            LOAD_FAST_BORROW         9 (calcom)
                LOAD_CONST              15 ('summary')
                BINARY_OP               26 ([])
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              19 ('brokerage_timezone_present')
                LOAD_CONST              16 (False)
                CALL                     2

 298            BUILD_MAP                3

 304            LOAD_CONST              20 ('encryption_posture')

 305            LOAD_CONST              11 ('status')
                LOAD_FAST_BORROW        10 (enc)
                LOAD_CONST              11 ('status')
                BINARY_OP               26 ([])

 306            LOAD_CONST              21 ('encryption_enabled')
                LOAD_GLOBAL             23 (bool + NULL)
                LOAD_FAST_BORROW        10 (enc)
                LOAD_CONST              15 ('summary')
                BINARY_OP               26 ([])
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              21 ('encryption_enabled')
                CALL                     1
                CALL                     1

 307            LOAD_CONST              12 ('warning_count')
                LOAD_GLOBAL             21 (len + NULL)
                LOAD_FAST_BORROW        10 (enc)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              13 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L18)
       L16:     NOT_TAKEN
       L17:     POP_TOP
                BUILD_LIST               0
       L18:     CALL                     1

 304            BUILD_MAP                3

 287            BUILD_MAP                4
                STORE_FAST              11 (payload)

 310            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 311            LOAD_CONST              22 ('ok')
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 27 (bid, payload)

 310            LOAD_CONST              23 (('status', 'brokerage_id', 'payload'))
                CALL_KW                  3
       L19:     RETURN_VALUE

  --   L20:     PUSH_EXC_INFO

 313            LOAD_GLOBAL             24 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       92 (to L25)
                NOT_TAKEN
                STORE_FAST              12 (e)

 314   L21:     LOAD_GLOBAL             26 (logger)
                LOAD_ATTR               29 (warning + NULL|self)

 315            LOAD_CONST              24 ('tenant_integration_posture error type=')
                LOAD_GLOBAL             31 (type + NULL)
                LOAD_FAST               12 (e)
                CALL                     1
                LOAD_ATTR               32 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 314            CALL                     1
                POP_TOP

 317            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 318            LOAD_CONST              25 ('skipped')

 319            LOAD_FAST                1 (bid)

 320            LOAD_CONST              26 ('unexpected:')
                LOAD_GLOBAL             31 (type + NULL)
                LOAD_FAST               12 (e)
                CALL                     1
                LOAD_ATTR               32 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 321            LOAD_CONST              27 ('tenant_integrations_unavailable')

 317            LOAD_CONST              28 (('status', 'brokerage_id', 'warnings', 'error_code'))
                CALL_KW                  4
       L22:     SWAP                     2
       L23:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              12 (e)
                DELETE_FAST             12 (e)
                RETURN_VALUE

  --   L24:     LOAD_CONST               1 (None)
                STORE_FAST              12 (e)
                DELETE_FAST             12 (e)
                RERAISE                  1

 313   L25:     RERAISE                  0

  --   L26:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L7 -> L20 [0]
  L8 to L10 -> L20 [0]
  L11 to L13 -> L20 [0]
  L14 to L16 -> L20 [0]
  L17 to L19 -> L20 [0]
  L20 to L21 -> L26 [1] lasti
  L21 to L22 -> L24 [1] lasti
  L22 to L23 -> L26 [1] lasti
  L24 to L26 -> L26 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "app\services\tenant\tenant_visibility_service.py", line 325>:
325           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object tenant_callback_summary at 0x0000018C17F76FD0, file "app\services\tenant\tenant_visibility_service.py", line 325>:
 325            RESUME                   0

 329            LOAD_GLOBAL              1 (_resolve_brokerage_id + NULL)
                LOAD_FAST_BORROW         0 (brokerage)
                CALL                     1
                STORE_FAST               1 (bid)

 330            LOAD_FAST_BORROW         1 (bid)
                POP_JUMP_IF_NOT_NONE    15 (to L1)
                NOT_TAKEN

 331            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 332            LOAD_CONST               2 ('failed')

 333            LOAD_CONST               1 (None)

 334            LOAD_CONST               3 ('missing_brokerage_id')

 331            LOAD_CONST               4 (('status', 'brokerage_id', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 336    L1:     NOP

 337    L2:     LOAD_SMALL_INT           0
                LOAD_CONST               5 (('reminder_report', 'list_pending_callbacks'))
                IMPORT_NAME              2 (app.services.callbacks.callback_schedule)
                IMPORT_FROM              3 (reminder_report)
                STORE_FAST               2 (reminder_report)
                IMPORT_FROM              4 (list_pending_callbacks)
                STORE_FAST               3 (list_pending_callbacks)
                POP_TOP

 341            LOAD_FAST_BORROW         2 (reminder_report)
                PUSH_NULL
                LOAD_FAST_BORROW         1 (bid)
                LOAD_SMALL_INT          60
                LOAD_CONST               6 (('lookahead_minutes',))
                CALL_KW                  2
                STORE_FAST               4 (rr)

 342            LOAD_FAST_BORROW         3 (list_pending_callbacks)
                PUSH_NULL
                LOAD_FAST_BORROW         1 (bid)
                LOAD_CONST               7 ('PENDING')
                LOAD_SMALL_INT         200
                LOAD_CONST               8 (('status', 'limit'))
                CALL_KW                  3
                STORE_FAST               5 (listed)

 344            LOAD_CONST               9 ('due_count')
                LOAD_GLOBAL             11 (int + NULL)
                LOAD_FAST_BORROW         4 (rr)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               9 ('due_count')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
        L3:     NOT_TAKEN
        L4:     POP_TOP
                LOAD_SMALL_INT           0
        L5:     CALL                     1

 345            LOAD_CONST              10 ('overdue_count')
                LOAD_GLOBAL             11 (int + NULL)
                LOAD_FAST_BORROW         4 (rr)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              10 ('overdue_count')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
        L6:     NOT_TAKEN
        L7:     POP_TOP
                LOAD_SMALL_INT           0
        L8:     CALL                     1

 346            LOAD_CONST              11 ('pending_count')
                LOAD_GLOBAL             11 (int + NULL)
                LOAD_FAST_BORROW         5 (listed)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              12 ('count')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L11)
        L9:     NOT_TAKEN
       L10:     POP_TOP
                LOAD_SMALL_INT           0
       L11:     CALL                     1

 343            BUILD_MAP                3
                STORE_FAST               6 (payload)

 348            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 349            LOAD_CONST              13 ('ok')
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 22 (bid, payload)

 348            LOAD_CONST              14 (('status', 'brokerage_id', 'payload'))
                CALL_KW                  3
       L12:     RETURN_VALUE

  --   L13:     PUSH_EXC_INFO

 351            LOAD_GLOBAL             14 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       92 (to L18)
                NOT_TAKEN
                STORE_FAST               7 (e)

 352   L14:     LOAD_GLOBAL             16 (logger)
                LOAD_ATTR               19 (warning + NULL|self)

 353            LOAD_CONST              15 ('tenant_callback_summary error type=')
                LOAD_GLOBAL             21 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               22 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 352            CALL                     1
                POP_TOP

 355            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 356            LOAD_CONST              16 ('skipped')

 357            LOAD_FAST                1 (bid)

 358            LOAD_CONST              17 ('unexpected:')
                LOAD_GLOBAL             21 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               22 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 359            LOAD_CONST              18 ('tenant_callbacks_unavailable')

 355            LOAD_CONST              19 (('status', 'brokerage_id', 'warnings', 'error_code'))
                CALL_KW                  4
       L15:     SWAP                     2
       L16:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RETURN_VALUE

  --   L17:     LOAD_CONST               1 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RERAISE                  1

 351   L18:     RERAISE                  0

  --   L19:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L13 [0]
  L4 to L6 -> L13 [0]
  L7 to L9 -> L13 [0]
  L10 to L12 -> L13 [0]
  L13 to L14 -> L19 [1] lasti
  L14 to L15 -> L17 [1] lasti
  L15 to L16 -> L19 [1] lasti
  L17 to L19 -> L19 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA32D0, file "app\services\tenant\tenant_visibility_service.py", line 403>:
403           RESUME                   0
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

Disassembly of <code object _project_tenant_audit_row at 0x0000018C17F64050, file "app\services\tenant\tenant_visibility_service.py", line 403>:
403            RESUME                   0

404            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (row)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN

405            LOAD_CONST               0 (None)
               RETURN_VALUE

406    L1:     BUILD_MAP                0
               STORE_FAST               1 (out)

407            LOAD_GLOBAL              4 (_TENANT_AUDIT_FIELDS_SOURCE)
               GET_ITER
       L2:     FOR_ITER                42 (to L4)
               STORE_FAST               2 (col)

408            LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (col, row)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L2)

409    L3:     LOAD_GLOBAL              6 (_TENANT_AUDIT_FIELD_RENAME)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 34 (col, col)
               CALL                     2
               STORE_FAST               3 (target_key)

410            LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (row, col)
               BINARY_OP               26 ([])
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 19 (out, target_key)
               STORE_SUBSCR
               JUMP_BACKWARD           44 (to L2)

407    L4:     END_FOR
               POP_ITER

411            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (row)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST               1 ('metadata')
               CALL                     1
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L5)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (row)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST               1 ('metadata')
               CALL                     1
               JUMP_FORWARD             1 (to L6)
       L5:     BUILD_MAP                0
       L6:     STORE_FAST               4 (md)

412            BUILD_MAP                0
               STORE_FAST               5 (projected_md)

413            LOAD_GLOBAL             10 (_TENANT_AUDIT_METADATA_KEYS)
               GET_ITER
       L7:     FOR_ITER               108 (to L13)
               STORE_FAST               6 (k)

414            LOAD_FAST_BORROW_LOAD_FAST_BORROW 100 (k, md)
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN

415            JUMP_BACKWARD           11 (to L7)

416    L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 70 (md, k)
               BINARY_OP               26 ([])
               STORE_FAST               7 (v)

417            LOAD_FAST_BORROW         7 (v)
               POP_JUMP_IF_NONE        34 (to L9)
               NOT_TAKEN
               LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         7 (v)
               LOAD_GLOBAL             12 (int)
               LOAD_GLOBAL             14 (float)
               LOAD_GLOBAL             16 (bool)
               BUILD_TUPLE              3
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE        7 (to L10)
               NOT_TAKEN

418    L9:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 117 (v, projected_md)
               LOAD_FAST_BORROW         6 (k)
               STORE_SUBSCR
               JUMP_BACKWARD           62 (to L7)

419   L10:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         7 (v)
               LOAD_GLOBAL             18 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L11)
               NOT_TAKEN
               JUMP_BACKWARD           86 (to L7)

420   L11:     LOAD_GLOBAL             21 (len + NULL)
               LOAD_FAST_BORROW         7 (v)
               CALL                     1
               LOAD_SMALL_INT         200
               COMPARE_OP              58 (bool(<=))
               POP_JUMP_IF_TRUE         3 (to L12)
               NOT_TAKEN
               JUMP_BACKWARD          104 (to L7)

421   L12:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 117 (v, projected_md)
               LOAD_FAST_BORROW         6 (k)
               STORE_SUBSCR
               JUMP_BACKWARD          110 (to L7)

413   L13:     END_FOR
               POP_ITER

422            LOAD_FAST_BORROW_LOAD_FAST_BORROW 81 (projected_md, out)
               LOAD_CONST               1 ('metadata')
               STORE_SUBSCR

423            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025230, file "app\services\tenant\tenant_visibility_service.py", line 426>:
426           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage')

427           LOAD_CONST               2 ('Any')

426           LOAD_CONST               3 ('limit')

429           LOAD_CONST               2 ('Any')

426           LOAD_CONST               4 ('return')

430           LOAD_CONST               5 ('Dict[str, Any]')

426           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object tenant_audit_history at 0x0000018C18646C00, file "app\services\tenant\tenant_visibility_service.py", line 426>:
 426            RESUME                   0

 435            LOAD_GLOBAL              1 (_resolve_brokerage_id + NULL)
                LOAD_FAST_BORROW         0 (brokerage)
                CALL                     1
                STORE_FAST               2 (bid)

 436            LOAD_FAST_BORROW         2 (bid)
                POP_JUMP_IF_NOT_NONE    15 (to L1)
                NOT_TAKEN

 437            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 438            LOAD_CONST               2 ('failed')

 439            LOAD_CONST               1 (None)

 440            LOAD_CONST               3 ('missing_brokerage_id')

 437            LOAD_CONST               4 (('status', 'brokerage_id', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 442    L1:     NOP

 443    L2:     LOAD_SMALL_INT           0
                LOAD_CONST               5 (('brokerage_action_history',))
                IMPORT_NAME              2 (app.services.operator.audit_service)
                IMPORT_FROM              3 (brokerage_action_history)
                STORE_FAST               3 (brokerage_action_history)
                POP_TOP

 446            LOAD_FAST_BORROW         3 (brokerage_action_history)
                PUSH_NULL
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 33 (bid, limit)
                LOAD_CONST               6 (('limit',))
                CALL_KW                  2
                STORE_FAST               4 (env)

 447            LOAD_FAST_BORROW         4 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               7 ('status')
                CALL                     1
                LOAD_CONST               8 ('ok')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       95 (to L10)
                NOT_TAKEN

 448            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 449            LOAD_FAST_BORROW         4 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               7 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
        L3:     NOT_TAKEN
        L4:     POP_TOP
                LOAD_CONST               9 ('skipped')

 450    L5:     LOAD_FAST                2 (bid)

 452            LOAD_CONST              10 ('rows')
                BUILD_LIST               0

 453            LOAD_CONST              11 ('count')
                LOAD_SMALL_INT           0

 451            BUILD_MAP                2

 455            LOAD_GLOBAL             11 (list + NULL)
                LOAD_FAST_BORROW         4 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              12 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
        L6:     NOT_TAKEN
        L7:     POP_TOP
                BUILD_LIST               0
        L8:     CALL                     1

 456            LOAD_FAST_BORROW         4 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              13 ('error_code')
                CALL                     1

 448            LOAD_CONST              14 (('status', 'brokerage_id', 'payload', 'warnings', 'error_code'))
                CALL_KW                  5
        L9:     RETURN_VALUE

 458   L10:     LOAD_FAST_BORROW         4 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              10 ('rows')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
       L11:     NOT_TAKEN
       L12:     POP_TOP
                BUILD_LIST               0
       L13:     STORE_FAST               5 (rows)

 459            LOAD_CONST              15 (<code object <genexpr> at 0x0000018C18128360, file "app\services\tenant\tenant_visibility_service.py", line 459>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         5 (rows)
                GET_ITER
                CALL                     0
                GET_ITER
                LOAD_FAST_AND_CLEAR      6 (p)
                SWAP                     2
       L14:     BUILD_LIST               0
                SWAP                     2
       L15:     FOR_ITER                10 (to L18)
                STORE_FAST_LOAD_FAST   102 (p, p)
       L16:     POP_JUMP_IF_NOT_NONE     3 (to L17)
                NOT_TAKEN
                JUMP_BACKWARD            8 (to L15)
       L17:     LOAD_FAST_BORROW         6 (p)
                LIST_APPEND              2
                JUMP_BACKWARD           12 (to L15)
       L18:     END_FOR
                POP_ITER
       L19:     STORE_FAST               7 (projected)
                STORE_FAST               6 (p)

 460            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 461            LOAD_CONST               8 ('ok')

 462            LOAD_FAST_BORROW         2 (bid)

 464            LOAD_CONST              10 ('rows')
                LOAD_FAST_BORROW         7 (projected)

 465            LOAD_CONST              11 ('count')
                LOAD_GLOBAL             13 (len + NULL)
                LOAD_FAST_BORROW         7 (projected)
                CALL                     1

 463            BUILD_MAP                2

 460            LOAD_CONST              16 (('status', 'brokerage_id', 'payload'))
                CALL_KW                  3
       L20:     RETURN_VALUE

  --   L21:     SWAP                     2
                POP_TOP

 459            SWAP                     2
                STORE_FAST               6 (p)
                RERAISE                  0

  --   L22:     PUSH_EXC_INFO

 468            LOAD_GLOBAL             14 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       92 (to L27)
                NOT_TAKEN
                STORE_FAST               8 (e)

 469   L23:     LOAD_GLOBAL             16 (logger)
                LOAD_ATTR               19 (warning + NULL|self)

 470            LOAD_CONST              17 ('tenant_audit_history error type=')
                LOAD_GLOBAL             21 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               22 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 469            CALL                     1
                POP_TOP

 472            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 473            LOAD_CONST               9 ('skipped')

 474            LOAD_FAST                2 (bid)

 475            LOAD_CONST              18 ('unexpected:')
                LOAD_GLOBAL             21 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               22 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 476            LOAD_CONST              19 ('tenant_audit_unavailable')

 472            LOAD_CONST              20 (('status', 'brokerage_id', 'warnings', 'error_code'))
                CALL_KW                  4
       L24:     SWAP                     2
       L25:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RETURN_VALUE

  --   L26:     LOAD_CONST               1 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RERAISE                  1

 468   L27:     RERAISE                  0

  --   L28:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L22 [0]
  L4 to L6 -> L22 [0]
  L7 to L9 -> L22 [0]
  L10 to L11 -> L22 [0]
  L12 to L14 -> L22 [0]
  L14 to L16 -> L21 [2]
  L17 to L19 -> L21 [2]
  L19 to L20 -> L22 [0]
  L21 to L22 -> L22 [0]
  L22 to L23 -> L28 [1] lasti
  L23 to L24 -> L26 [1] lasti
  L24 to L25 -> L28 [1] lasti
  L26 to L28 -> L28 [1] lasti

Disassembly of <code object <genexpr> at 0x0000018C18128360, file "app\services\tenant\tenant_visibility_service.py", line 459>:
 459           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                16 (to L3)
               STORE_FAST               1 (r)
               LOAD_GLOBAL              1 (_project_tenant_audit_row + NULL)
               LOAD_FAST_BORROW         1 (r)
               CALL                     1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           18 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "app\services\tenant\tenant_visibility_service.py", line 518>:
518           RESUME                   0
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

Disassembly of <code object _bound_entry_id at 0x0000018C18010B30, file "app\services\tenant\tenant_visibility_service.py", line 518>:
518           RESUME                   0

519           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

520           LOAD_CONST               0 (None)
              RETURN_VALUE

521   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

522           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_FALSE       17 (to L2)
              NOT_TAKEN
              LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         1 (s)
              CALL                     1
              LOAD_SMALL_INT         200
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

523   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

524   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "app\services\tenant\tenant_visibility_service.py", line 527>:
527           RESUME                   0
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

Disassembly of <code object _bound_notes_token at 0x0000018C1801C410, file "app\services\tenant\tenant_visibility_service.py", line 527>:
527            RESUME                   0

528            LOAD_FAST_BORROW         0 (value)
               POP_JUMP_IF_NOT_NONE     3 (to L1)
               NOT_TAKEN

529            LOAD_CONST               0 (None)
               RETURN_VALUE

530    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (value)
               LOAD_GLOBAL              2 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

531            LOAD_CONST               0 (None)
               RETURN_VALUE

532    L2:     LOAD_FAST_BORROW         0 (value)
               LOAD_ATTR                5 (strip + NULL|self)
               CALL                     0
               STORE_FAST               1 (s)

533            LOAD_FAST_BORROW         1 (s)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN

534            LOAD_CONST               0 (None)
               RETURN_VALUE

535    L3:     LOAD_GLOBAL              7 (len + NULL)
               LOAD_FAST_BORROW         1 (s)
               CALL                     1
               LOAD_SMALL_INT         200
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN

536            LOAD_CONST               0 (None)
               RETURN_VALUE

537    L4:     LOAD_GLOBAL              8 (any)
               COPY                     1
               LOAD_COMMON_CONSTANT     4 (<built-in function any>)
               IS_OP                    0 (is)
               POP_JUMP_IF_FALSE       28 (to L8)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 (<code object <genexpr> at 0x0000018C18128470, file "app\services\tenant\tenant_visibility_service.py", line 537>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         1 (s)
               GET_ITER
               CALL                     0
       L5:     FOR_ITER                12 (to L7)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L6)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L5)
       L6:     POP_ITER
               LOAD_CONST               2 (True)
               JUMP_FORWARD            17 (to L9)
       L7:     END_FOR
               POP_ITER
               LOAD_CONST               3 (False)
               JUMP_FORWARD            13 (to L9)
       L8:     PUSH_NULL
               LOAD_CONST               1 (<code object <genexpr> at 0x0000018C18128470, file "app\services\tenant\tenant_visibility_service.py", line 537>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         1 (s)
               GET_ITER
               CALL                     0
               CALL                     1
       L9:     TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN

538            LOAD_CONST               0 (None)
               RETURN_VALUE

539   L10:     LOAD_FAST_BORROW         1 (s)
               RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18128470, file "app\services\tenant\tenant_visibility_service.py", line 537>:
 537           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                13 (to L3)
               STORE_FAST_LOAD_FAST    17 (ch, ch)
               LOAD_GLOBAL              0 (_ALLOWED_NOTES_TOKEN_CHARS)
               CONTAINS_OP              1 (not in)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           15 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026230, file "app\services\tenant\tenant_visibility_service.py", line 542>:
542           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage')

543           LOAD_CONST               2 ('Any')

542           LOAD_CONST               3 ('entry_id')

544           LOAD_CONST               2 ('Any')

542           LOAD_CONST               4 ('actor_token')

546           LOAD_CONST               5 ('Optional[str]')

542           LOAD_CONST               6 ('notes_token')

547           LOAD_CONST               5 ('Optional[str]')

542           LOAD_CONST               7 ('now')

548           LOAD_CONST               2 ('Any')

542           LOAD_CONST               8 ('return')

549           LOAD_CONST               9 ('Dict[str, Any]')

542           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object acknowledge_tenant_audit_entry at 0x0000018C17F7B2B0, file "app\services\tenant\tenant_visibility_service.py", line 542>:
 542            RESUME                   0

 561            LOAD_GLOBAL              1 (_resolve_brokerage_id + NULL)
                LOAD_FAST_BORROW         0 (brokerage)
                CALL                     1
                STORE_FAST               5 (bid)

 562            LOAD_FAST_BORROW         5 (bid)
                POP_JUMP_IF_NOT_NONE    15 (to L1)
                NOT_TAKEN

 563            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 564            LOAD_CONST               2 ('failed')

 565            LOAD_CONST               1 (None)

 566            LOAD_CONST               3 ('missing_brokerage_id')

 563            LOAD_CONST               4 (('status', 'brokerage_id', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 568    L1:     LOAD_GLOBAL              5 (_bound_entry_id + NULL)
                LOAD_FAST_BORROW         1 (entry_id)
                CALL                     1
                STORE_FAST               6 (eid)

 569            LOAD_FAST_BORROW         6 (eid)
                POP_JUMP_IF_NOT_NONE    15 (to L2)
                NOT_TAKEN

 570            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 571            LOAD_CONST               2 ('failed')

 572            LOAD_FAST_BORROW         5 (bid)

 573            LOAD_CONST               5 ('missing_or_invalid_entry_id')

 570            LOAD_CONST               4 (('status', 'brokerage_id', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 575    L2:     LOAD_GLOBAL              7 (_bound_notes_token + NULL)
                LOAD_FAST_BORROW         3 (notes_token)
                CALL                     1
                STORE_FAST               7 (note)

 576            LOAD_FAST_BORROW         3 (notes_token)
                POP_JUMP_IF_NONE        19 (to L3)
                NOT_TAKEN
                LOAD_FAST_BORROW         7 (note)
                POP_JUMP_IF_NOT_NONE    15 (to L3)
                NOT_TAKEN

 577            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 578            LOAD_CONST               2 ('failed')

 579            LOAD_FAST_BORROW         5 (bid)

 580            LOAD_CONST               6 ('invalid_notes_token')

 577            LOAD_CONST               4 (('status', 'brokerage_id', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 582    L3:     LOAD_FAST_BORROW         2 (actor_token)
                TO_BOOL
                POP_JUMP_IF_FALSE       12 (to L4)
                NOT_TAKEN
                LOAD_GLOBAL              7 (_bound_notes_token + NULL)
                LOAD_FAST_BORROW         2 (actor_token)
                CALL                     1
                JUMP_FORWARD             1 (to L5)
        L4:     LOAD_CONST               1 (None)
        L5:     STORE_FAST               8 (bounded_actor)

 585            NOP

 586    L6:     LOAD_SMALL_INT           0
                LOAD_CONST               7 (('record_tenant_audit_acknowledgement',))
                IMPORT_NAME              4 (app.services.tenant.tenant_audit_ack_store)
                IMPORT_FROM              5 (record_tenant_audit_acknowledgement)
                STORE_FAST               9 (record_tenant_audit_acknowledgement)
                POP_TOP

 589            LOAD_FAST_BORROW         9 (record_tenant_audit_acknowledgement)
                PUSH_NULL

 590            LOAD_FAST_BORROW         5 (bid)

 591            LOAD_CONST               8 ('AUDIT_ENTRY_VIEWED')

 592            LOAD_CONST               9 ('TENANT')

 593            LOAD_FAST_BORROW         8 (bounded_actor)

 594            LOAD_FAST_BORROW         6 (eid)

 595            LOAD_FAST_BORROW         7 (note)

 596            LOAD_FAST_BORROW         4 (now)

 589            LOAD_CONST              10 (('brokerage_id', 'acknowledgement_type', 'actor_type', 'actor_id', 'audit_entry_id', 'notes_token', 'now'))
                CALL_KW                  7
                STORE_FAST              10 (durable)

 598            LOAD_FAST_BORROW        10 (durable)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              11 ('status')
                CALL                     1
                LOAD_CONST              12 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE      106 (to L11)
                NOT_TAKEN

 599            LOAD_FAST_BORROW        10 (durable)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              13 ('ack_row')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
        L7:     NOT_TAKEN
        L8:     POP_TOP
                BUILD_MAP                0
        L9:     STORE_FAST              11 (row)

 600            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 601            LOAD_CONST              12 ('ok')

 602            LOAD_FAST_BORROW         5 (bid)

 604            LOAD_CONST              14 ('entry_id')
                LOAD_FAST_BORROW         6 (eid)

 605            LOAD_CONST              15 ('duplicate')
                LOAD_GLOBAL             15 (bool + NULL)
                LOAD_FAST_BORROW        10 (durable)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              15 ('duplicate')
                CALL                     1
                CALL                     1

 606            LOAD_CONST              16 ('acknowledged_at')
                LOAD_FAST_BORROW        11 (row)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              16 ('acknowledged_at')
                CALL                     1

 607            LOAD_CONST              17 ('notes_token')
                LOAD_FAST_BORROW        11 (row)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              17 ('notes_token')
                CALL                     1

 603            BUILD_MAP                4

 609            LOAD_CONST              18 ('tenant_audit_ack_store_is_durable')
                BUILD_LIST               1

 600            LOAD_CONST              19 (('status', 'brokerage_id', 'payload', 'warnings'))
                CALL_KW                  4
       L10:     RETURN_VALUE

 616   L11:     LOAD_FAST_BORROW        10 (durable)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              11 ('status')
                CALL                     1
                LOAD_CONST               2 ('failed')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       30 (to L13)
                NOT_TAKEN

 617            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 618            LOAD_CONST               2 ('failed')

 619            LOAD_FAST_BORROW         5 (bid)

 620            LOAD_FAST_BORROW        10 (durable)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              20 ('error_code')
                CALL                     1

 617            LOAD_CONST               4 (('status', 'brokerage_id', 'error_code'))
                CALL_KW                  3
       L12:     RETURN_VALUE

 616   L13:     NOP

 629   L14:     NOP

 630   L15:     LOAD_SMALL_INT           0
                LOAD_CONST              22 (('datetime', 'timezone'))
                IMPORT_NAME             13 (datetime)
                IMPORT_FROM             13 (datetime)
                STORE_FAST              13 (_dt)
                IMPORT_FROM             14 (timezone)
                STORE_FAST              14 (_tz)
                POP_TOP

 631            LOAD_GLOBAL             31 (isinstance + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 77 (now, _dt)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       66 (to L21)
                NOT_TAKEN

 632            LOAD_FAST_BORROW         4 (now)
                LOAD_ATTR               32 (tzinfo)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L18)
       L16:     NOT_TAKEN
       L17:     LOAD_FAST                4 (now)
                JUMP_FORWARD            27 (to L19)
       L18:     LOAD_FAST_BORROW         4 (now)
                LOAD_ATTR               35 (replace + NULL|self)
                LOAD_FAST_BORROW        14 (_tz)
                LOAD_ATTR               36 (utc)
                LOAD_CONST              23 (('tzinfo',))
                CALL_KW                  1
       L19:     LOAD_ATTR               39 (isoformat + NULL|self)
                LOAD_CONST              24 ('seconds')
                LOAD_CONST              25 (('timespec',))
                CALL_KW                  1
                STORE_FAST              15 (iso_now)
       L20:     JUMP_FORWARD            44 (to L23)

 634   L21:     LOAD_FAST_BORROW        13 (_dt)
                LOAD_ATTR               41 (now + NULL|self)
                LOAD_FAST_BORROW        14 (_tz)
                LOAD_ATTR               36 (utc)
                CALL                     1
                LOAD_ATTR               39 (isoformat + NULL|self)
                LOAD_CONST              24 ('seconds')
                LOAD_CONST              25 (('timespec',))
                CALL_KW                  1
                STORE_FAST              15 (iso_now)
       L22:     NOP

 637   L23:     LOAD_FAST_BORROW         5 (bid)
                FORMAT_SIMPLE
                LOAD_CONST              27 ('::')
                LOAD_FAST_BORROW         6 (eid)
                FORMAT_SIMPLE
                BUILD_STRING             3
                STORE_FAST              16 (key)

 638            LOAD_GLOBAL             42 (_TENANT_ACK_LOCK)
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
       L24:     POP_TOP

 639            LOAD_GLOBAL             44 (_TENANT_ACK_REGISTRY)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_FAST_BORROW        16 (key)
                CALL                     1
                STORE_FAST              17 (existing)

 640            LOAD_FAST_BORROW        17 (existing)
                POP_JUMP_IF_NONE        65 (to L26)
                NOT_TAKEN

 641            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 642            LOAD_CONST              12 ('ok')

 643            LOAD_FAST_BORROW         5 (bid)

 645            LOAD_CONST              14 ('entry_id')
                LOAD_FAST_BORROW         6 (eid)

 646            LOAD_CONST              15 ('duplicate')
                LOAD_CONST              28 (True)

 647            LOAD_CONST              16 ('acknowledged_at')
                LOAD_FAST_BORROW        17 (existing)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              16 ('acknowledged_at')
                CALL                     1

 648            LOAD_CONST              17 ('notes_token')
                LOAD_FAST_BORROW        17 (existing)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              17 ('notes_token')
                CALL                     1

 644            BUILD_MAP                4

 650            LOAD_CONST              29 ('tenant_audit_ack_store_is_process_local')
                BUILD_LIST               1

 641            LOAD_CONST              19 (('status', 'brokerage_id', 'payload', 'warnings'))
                CALL_KW                  4

 638   L25:     SWAP                     3
                SWAP                     2
                LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                CALL                     3
                POP_TOP
                RETURN_VALUE

 653   L26:     LOAD_CONST              30 ('brokerage_id')
                LOAD_FAST_BORROW         5 (bid)

 654            LOAD_CONST              14 ('entry_id')
                LOAD_FAST_BORROW         6 (eid)

 655            LOAD_CONST              31 ('actor_token')
                LOAD_FAST_BORROW         8 (bounded_actor)

 656            LOAD_CONST              17 ('notes_token')
                LOAD_FAST_BORROW         7 (note)

 657            LOAD_CONST              16 ('acknowledged_at')
                LOAD_FAST_BORROW        15 (iso_now)

 652            BUILD_MAP                5
                LOAD_GLOBAL             44 (_TENANT_ACK_REGISTRY)
                LOAD_FAST_BORROW        16 (key)
                STORE_SUBSCR

 659            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 660            LOAD_CONST              12 ('ok')

 661            LOAD_FAST_BORROW         5 (bid)

 663            LOAD_CONST              14 ('entry_id')
                LOAD_FAST_BORROW         6 (eid)

 664            LOAD_CONST              15 ('duplicate')
                LOAD_CONST              32 (False)

 665            LOAD_CONST              16 ('acknowledged_at')
                LOAD_FAST_BORROW        15 (iso_now)

 666            LOAD_CONST              17 ('notes_token')
                LOAD_FAST_BORROW         7 (note)

 662            BUILD_MAP                4

 668            LOAD_CONST              29 ('tenant_audit_ack_store_is_process_local')
                BUILD_LIST               1

 659            LOAD_CONST              19 (('status', 'brokerage_id', 'payload', 'warnings'))
                CALL_KW                  4

 638   L27:     SWAP                     3
                SWAP                     2
                LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                CALL                     3
                POP_TOP
                RETURN_VALUE

  --   L28:     PUSH_EXC_INFO

 622            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       55 (to L32)
                NOT_TAKEN
                STORE_FAST              12 (e)

 623   L29:     LOAD_GLOBAL             18 (logger)
                LOAD_ATTR               21 (warning + NULL|self)

 624            LOAD_CONST              21 ('acknowledge_tenant_audit_entry durable layer error type=')

 625            LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST               12 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE

 624            BUILD_STRING             2

 623            CALL                     1
                POP_TOP
       L30:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              12 (e)
                DELETE_FAST             12 (e)
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 359 (to L14)

  --   L31:     LOAD_CONST               1 (None)
                STORE_FAST              12 (e)
                DELETE_FAST             12 (e)
                RERAISE                  1

 622   L32:     RERAISE                  0

  --   L33:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L34:     PUSH_EXC_INFO

 635            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L36)
                NOT_TAKEN
                POP_TOP

 636            LOAD_CONST              26 ('')
                STORE_FAST              15 (iso_now)
       L35:     POP_EXCEPT
                JUMP_BACKWARD_NO_INTERRUPT 247 (to L23)

 635   L36:     RERAISE                  0

  --   L37:     COPY                     3
                POP_EXCEPT
                RERAISE                  1

 638   L38:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L39)
                NOT_TAKEN
                RERAISE                  2
       L39:     POP_TOP
       L40:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
                LOAD_CONST               1 (None)
                RETURN_VALUE

  --   L41:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L6 to L7 -> L28 [0]
  L8 to L10 -> L28 [0]
  L11 to L12 -> L28 [0]
  L15 to L16 -> L34 [0]
  L17 to L20 -> L34 [0]
  L21 to L22 -> L34 [0]
  L24 to L25 -> L38 [2] lasti
  L26 to L27 -> L38 [2] lasti
  L28 to L29 -> L33 [1] lasti
  L29 to L30 -> L31 [1] lasti
  L31 to L33 -> L33 [1] lasti
  L34 to L35 -> L37 [1] lasti
  L36 to L37 -> L37 [1] lasti
  L38 to L40 -> L41 [4] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "app\services\tenant\tenant_visibility_service.py", line 672>:
672           RESUME                   0
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

Disassembly of <code object reset_tenant_audit_ack_registry_for_tests at 0x0000018C18011370, file "app\services\tenant\tenant_visibility_service.py", line 672>:
 672           RESUME                   0

 674           LOAD_GLOBAL              0 (_TENANT_ACK_LOCK)
               COPY                     1
               LOAD_SPECIAL             1 (__exit__)
               SWAP                     2
               SWAP                     3
               LOAD_SPECIAL             0 (__enter__)
               CALL                     0
       L1:     POP_TOP

 675           LOAD_GLOBAL              2 (_TENANT_ACK_REGISTRY)
               LOAD_ATTR                5 (clear + NULL|self)
               CALL                     0
               POP_TOP

 674   L2:     LOAD_CONST               1 (None)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA1D40, file "app\services\tenant\tenant_visibility_service.py", line 678>:
678           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('Dict[str, Dict[str, Any]]')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _peek_tenant_audit_ack_registry_for_tests at 0x0000018C1804D3B0, file "app\services\tenant\tenant_visibility_service.py", line 678>:
 678            RESUME                   0

 679            LOAD_GLOBAL              0 (_TENANT_ACK_LOCK)
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
        L1:     POP_TOP

 680            LOAD_GLOBAL              2 (_TENANT_ACK_REGISTRY)
                LOAD_ATTR                5 (items + NULL|self)
                CALL                     0
                GET_ITER
                LOAD_FAST_AND_CLEAR      0 (k)
                LOAD_FAST_AND_CLEAR      1 (v)
                SWAP                     3
        L2:     BUILD_MAP                0
                SWAP                     2
        L3:     FOR_ITER                17 (to L4)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST    1 (k, v)
                LOAD_FAST_BORROW         0 (k)
                LOAD_GLOBAL              7 (dict + NULL)
                LOAD_FAST_BORROW         1 (v)
                CALL                     1
                MAP_ADD                  2
                JUMP_BACKWARD           19 (to L3)
        L4:     END_FOR
                POP_ITER
        L5:     SWAP                     3
                STORE_FAST               1 (v)
                STORE_FAST               0 (k)

 679    L6:     SWAP                     3
                SWAP                     2
                LOAD_CONST               0 (None)
                LOAD_CONST               0 (None)
                LOAD_CONST               0 (None)
                CALL                     3
                POP_TOP
                RETURN_VALUE

  --    L7:     SWAP                     2
                POP_TOP

 680            SWAP                     3
                STORE_FAST               1 (v)
                STORE_FAST               0 (k)
                RERAISE                  0

 679    L8:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L9)
                NOT_TAKEN
                RERAISE                  2
        L9:     POP_TOP
       L10:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
                LOAD_CONST               0 (None)
                RETURN_VALUE

  --   L11:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L8 [2] lasti
  L2 to L5 -> L7 [5]
  L5 to L6 -> L8 [2] lasti
  L7 to L8 -> L8 [2] lasti
  L8 to L10 -> L11 [4] lasti
```
