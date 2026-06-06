# operator/operator_actions

- **pyc:** `app\services\operator\__pycache__\operator_actions.cpython-314.pyc`
- **expected source path (absent):** `app\services\operator/operator_actions.py`
- **co_filename (from bytecode):** `app\services\operator\operator_actions.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** operator

## Module docstring

```
PAS173 — Operator action dispatcher (closed allow-list).

Every operator-driven mutation flows through ``execute_action``.
The set of allowed actions is closed; arbitrary DB mutations,
secret exports, and transcript access are NEVER reachable from
this surface.

Doctrine:

* **Closed action allow-list.** ``ALLOWED_OPERATOR_ACTIONS``
  enumerates every valid action. Anything else returns
  ``status="refused"`` + ``action_not_allowed``.
* **Audit-safe.** Every successful action returns the
  structural envelope WITH an ``audit`` block carrying
  ``actor_type``, ``actor_id`` (bounded), ``action``,
  ``brokerage_id``, ``status``, and the deterministic
  ``operator.action.executed`` event id. NEVER carries
  secrets / phone / email / transcript / raw payload.
* **Operator/admin context required.** The route layer is
  responsible for the auth gate (X-Admin-Key); this module
  validates that the ``actor_type`` / ``actor_id`` arguments
  it receives are bounded structural tokens.
* **No autonomy.** No action here triggers another action.
  No background scheduling. No retries. No autonomous
  decisioning.
* **Bounded.** Each action's payload is parsed against a
  closed argument schema; unrecognised arguments are
  dropped.

Public surface:

  * ``ALLOWED_OPERATOR_ACTIONS``
  * ``execute_action(...)``
```

## Imports

`ALLOWED_METADATA_KEYS`, `ALLOWED_ONBOARDING_STATUSES`, `ALLOWED_PILOT_STAGES`, `Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.db.brokerage_store`, `app.services.brokerage.config_validator`, `app.services.brokerage.profile_service`, `app.services.callbacks.callback_schedule`, `app.services.ingestion.pending_call_recovery`, `app.services.operator.audit_service`, `app.services.worker.heartbeat_monitor`, `datetime`, `get_brokerage_by_id`, `get_profile`, `heartbeat_monitor_report`, `log_operator_action`, `logging`, `mark_callback_completed`, `mark_onboarding_completed`, `pause_brokerage`, `queue_status_report`, `resume_brokerage`, `timezone`, `typing`, `update_onboarding_status`, `update_pilot_stage`, `uuid`, `validate_brokerage_launch_ready`

## Classes

_none_

## Functions / methods

`__annotate__`, `_audit_actor_type`, `_audit_status_from_dispatch`, `_bound_str`, `_emit_audit_entry`, `_handle_acknowledge_alert`, `_handle_mark_callback_completed`, `_handle_mark_onboarding_stage`, `_handle_mark_pilot_stage`, `_handle_mark_pilot_stage_with_evidence`, `_handle_pause`, `_handle_request_readiness_email`, `_handle_resume`, `_handle_rotate_brokerage_api_key`, `_handle_run_readiness_snapshot`, `_now_iso`, `_safe_envelope`, `_validate_context`, `execute_action`

## Env-key candidates

`ADMIN`, `FAILED`, `LIVE`, `OPERATOR`, `SKIPPED`, `SUCCESS`, `SYSTEM`, `VERIFIED`

## String constants (redacted where noted)

- '\nPAS173 — Operator action dispatcher (closed allow-list).\n\nEvery operator-driven mutation flows through ``execute_action``.\nThe set of allowed actions is closed; arbitrary DB mutations,\nsecret exports, and transcript access are NEVER reachable from\nthis surface.\n\nDoctrine:\n\n* **Closed action allow-list.** ``ALLOWED_OPERATOR_ACTIONS``\n  enumerates every valid action. Anything else returns\n  ``status="refused"`` + ``action_not_allowed``.\n* **Audit-safe.** Every successful action returns the\n  structural envelope WITH an ``audit`` block carrying\n  ``actor_type``, ``actor_id`` (bounded), ``action``,\n  ``brokerage_id``, ``status``, and the deterministic\n  ``operator.action.executed`` event id. NEVER carries\n  secrets / phone / email / transcript / raw payload.\n* **Operator/admin context required.** The route layer is\n  responsible for the auth gate (X-Admin-Key); this module\n  validates that the ``actor_type`` / ``actor_id`` arguments\n  it receives are bounded structural tokens.\n* **No autonomy.** No action here triggers another action.\n  No background scheduling. No retries. No autonomous\n  decisioning.\n* **Bounded.** Each action\'s payload is parsed against a\n  closed argument schema; unrecognised arguments are\n  dropped.\n\nPublic surface:\n\n  * ``ALLOWED_OPERATOR_ACTIONS``\n  * ``execute_action(...)``\n'
- 'pas.operator.actions'
- 'pause_brokerage'
- 'resume_brokerage'
- 'mark_onboarding_stage'
- 'mark_pilot_stage'
- 'mark_callback_completed'
- 'acknowledge_alert'
- 'run_readiness_snapshot'
- 'request_readiness_email'
- 'rotate_brokerage_api_key'
- 'mark_pilot_stage_with_evidence'
- 'action'
- 'brokerage_id'
- 'actor_type'
- 'actor_id'
- 'result'
- 'warnings'
- 'error_code'
- 'payload'
- 'value'
- 'Any'
- 'max_len'
- 'int'
- 'return'
- 'Optional[str]'
- 'str'
- 'seconds'
- 'status'
- 'Optional[Dict[str, Any]]'
- 'Optional[List[str]]'
- 'Dict[str, Any]'
- 'event'
- 'operator.action.executed'
- 'audit'
- 'failed'
- 'invalid_actor_type'
- 'invalid_actor_id'
- 'profile'
- 'target_status'
- 'VERIFIED'
- 'stage'
- 'invalid_onboarding_status'
- 'LIVE'
- 'invalid_pilot_stage'
- 'callback_id'
- 'missing_callback_id'
- 'callback'
- 'Operator says "I saw this alert; it\'s being worked on".\nPAS173 does NOT persist alert acknowledgement to a durable\nstore (PAS174+ may add it); the action returns a\nstructural envelope so the operator\'s audit trail records\nthe human acknowledgement. NEVER triggers an automated\nresponse.'
- 'alert_id'
- 'missing_alert_id'
- 'notes_token'
- 'Run the per-brokerage readiness snapshot — combines the\nconfiguration validator + (if a profile exists) the\nlaunch-ready check + the heartbeat + queue snapshot. NEVER\nraises.'
- 'run_readiness_snapshot brokerage read error type='
- 'launch_ready'
- 'warning_count'
- 'error_count'
- 'errors'
- 'heartbeat'
- 'total'
- 'by_status'
- 'oldest_age_seconds'
- 'queue'
- 'profile_present'
- 'Generate a structural readiness snapshot and record the\nrequest. PAS175 does NOT send real email — the action\nrecords the request_id; the operator picks up the snapshot\nvia an audited mechanism (e.g. their email gateway).\n\nThe ``send_real_email`` payload kwarg is reserved for a\nfuture explicit-opt-in surface; in PAS175 it is honoured\nonly as a structural marker — the value is recorded in\nthe audit metadata but the action never actually sends.\n'
- 'request_id'
- 'snapshot'
- 'real_email_sent'
- 'email_send_dispatched'
- 'pas175_request_only_no_email_sent'
- "Record an operator request to rotate the brokerage's\nAPI key. PAS175 keeps this **proposal-only** — the action\ndoes NOT call the existing rotate helper; the operator\nmust use the existing ``POST /admin/brokerages/{id}/\nrotate-key`` route to actually execute. The audit row\ncaptures who requested the rotation and when, preserving\naccountability without duplicating mutation paths.\n\nThe PAS175 secrets-handling doctrine: NEVER echo the\nrotated key. NEVER return the new key in the operator\naction envelope. The operator retrieves the new key from\nthe audited admin route's response.\n"
- 'rotation_proposal_only'
- 'execute_via'
- 'POST /admin/brokerages/{id}/rotate-key'
- 'key_rotated'
- 'fingerprint'
- 'pas175_rotation_proposal_only'
- 'use_admin_rotate_route_to_execute'
- 'Same as ``mark_pilot_stage`` but requires a structural\nevidence pointer in the payload — typically the\n``action_id`` of a prior ``run_readiness_snapshot`` audit\nrow. NEVER stores raw docs / notes / transcripts.\n\nRequired payload keys:\n  * ``stage`` — one of ALLOWED_PILOT_STAGES.\n  * ``evidence_audit_row_id`` — bounded UUID-shaped or\n    opaque token, ≤ 200 chars. NEVER a URL containing PII.\n'
- 'evidence_audit_row_id'
- 'missing_evidence_audit_row_id'
- 'Map the PAS173 actor_type (lowercase: admin / operator /\nautomation) to the PAS174 audit closed enum (uppercase:\nADMIN / OPERATOR / SYSTEM). NEVER raises.'
- 'admin'
- 'ADMIN'
- 'automation'
- 'SYSTEM'
- 'OPERATOR'
- 'env'
- "Map the dispatcher's status field to the PAS174 audit\nclosed enum (SUCCESS / FAILED / SKIPPED)."
- 'SUCCESS'
- 'skipped'
- 'SKIPPED'
- 'FAILED'
- 'None'
- 'Best-effort append to the PAS174 audit log. NEVER raises.\nNEVER persists raw payload contents — only structural\nmetadata.'
- 'onboarding_status'
- 'pilot_stage'
- 'brokerage'
- 'alert'
- '_emit_audit_entry error action='
- ' type='
- "Dispatch ``action`` against the closed allow-list. Returns\na structural envelope. NEVER raises. NEVER allows arbitrary\nDB mutation.\n\n**PAS174:** every action — successful or not — produces a\ndurable audit entry via the append-only audit service.\nRefused / failed-validation actions log a SKIPPED /\nFAILED audit row so the operator's accountability trail\nis preserved even when the dispatcher rejects upstream."
- 'refused'
- 'action_not_allowed'
- 'unknown'
- 'operator'
- 'missing_brokerage_id'
- 'execute_action handler error action='
- 'unexpected:'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS173 — Operator action dispatcher (closed allow-list).\n\nEvery operator-driven mutation flows through ``execute_action``.\nThe set of allowed actions is closed; arbitrary DB mutations,\nsecret exports, and transcript access are NEVER reachable from\nthis surface.\n\nDoctrine:\n\n* **Closed action allow-list.** ``ALLOWED_OPERATOR_ACTIONS``\n  enumerates every valid action. Anything else returns\n  ``status="refused"`` + ``action_not_allowed``.\n* **Audit-safe.** Every successful action returns the\n  structural envelope WITH an ``audit`` block carrying\n  ``actor_type``, ``actor_id`` (bounded), ``action``,\n  ``brokerage_id``, ``status``, and the deterministic\n  ``operator.action.executed`` event id. NEVER carries\n  secrets / phone / email / transcript / raw payload.\n* **Operator/admin context required.** The route layer is\n  responsible for the auth gate (X-Admin-Key); this module\n  validates that the ``actor_type`` / ``actor_id`` arguments\n  it receives are bounded structural tokens.\n* **No autonomy.** No action here triggers another action.\n  No background scheduling. No retries. No autonomous\n  decisioning.\n* **Bounded.** Each action\'s payload is parsed against a\n  closed argument schema; unrecognised arguments are\n  dropped.\n\nPublic surface:\n\n  * ``ALLOWED_OPERATOR_ACTIONS``\n  * ``execute_action(...)``\n')
              STORE_NAME               0 (__doc__)

 37           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 39           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 40           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('datetime', 'timezone'))
              IMPORT_NAME              4 (datetime)
              IMPORT_FROM              4 (datetime)
              STORE_NAME               4 (datetime)
              IMPORT_FROM              5 (timezone)
              STORE_NAME               5 (timezone)
              POP_TOP

 41           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('Any', 'Dict', 'List', 'Optional'))
              IMPORT_NAME              6 (typing)
              IMPORT_FROM              7 (Any)
              STORE_NAME               7 (Any)
              IMPORT_FROM              8 (Dict)
              STORE_NAME               8 (Dict)
              IMPORT_FROM              9 (List)
              STORE_NAME               9 (List)
              IMPORT_FROM             10 (Optional)
              STORE_NAME              10 (Optional)
              POP_TOP

 44           LOAD_NAME                3 (logging)
              LOAD_ATTR               22 (getLogger)
              PUSH_NULL
              LOAD_CONST               5 ('pas.operator.actions')
              CALL                     1
              STORE_NAME              12 (logger)

 51           LOAD_CONST              60 (('pause_brokerage', 'resume_brokerage', 'mark_onboarding_stage', 'mark_pilot_stage', 'mark_callback_completed', 'acknowledge_alert', 'run_readiness_snapshot', 'request_readiness_email', 'rotate_brokerage_api_key', 'mark_pilot_stage_with_evidence'))
              STORE_NAME              13 (ALLOWED_OPERATOR_ACTIONS)

 66           LOAD_CONST              61 (('admin', 'operator', 'automation'))
              STORE_NAME              14 (ALLOWED_ACTOR_TYPES)

 72           LOAD_SMALL_INT         200
              STORE_NAME              15 (_ACTOR_ID_MAX_LEN)

 73           LOAD_SMALL_INT         200
              STORE_NAME              16 (_ALERT_ID_MAX_LEN)

 74           LOAD_SMALL_INT         200
              STORE_NAME              17 (_CALLBACK_ID_MAX_LEN)

 75           LOAD_SMALL_INT         200
              STORE_NAME              18 (_BROKERAGE_ID_MAX_LEN)

 76           LOAD_SMALL_INT         200
              STORE_NAME              19 (_NOTES_TOKEN_MAX_LEN)

 83           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C18025130, file "app\services\operator\operator_actions.py", line 83>)
              MAKE_FUNCTION
              LOAD_CONST              17 (<code object _bound_str at 0x0000018C18010DF0, file "app\services\operator\operator_actions.py", line 83>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              20 (_bound_str)

 94           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA3B40, file "app\services\operator\operator_actions.py", line 94>)
              MAKE_FUNCTION
              LOAD_CONST              19 (<code object _now_iso at 0x0000018C18038670, file "app\services\operator\operator_actions.py", line 94>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              21 (_now_iso)

 98           LOAD_CONST              20 ('action')

101           LOAD_CONST               2 (None)

 98           LOAD_CONST              21 ('brokerage_id')

102           LOAD_CONST               2 (None)

 98           LOAD_CONST              22 ('actor_type')

103           LOAD_CONST               2 (None)

 98           LOAD_CONST              23 ('actor_id')

104           LOAD_CONST               2 (None)

 98           LOAD_CONST              24 ('result')

105           LOAD_CONST               2 (None)

 98           LOAD_CONST              25 ('warnings')

106           LOAD_CONST               2 (None)

 98           LOAD_CONST              26 ('error_code')

107           LOAD_CONST               2 (None)

 98           BUILD_MAP                7
              LOAD_CONST              27 (<code object __annotate__ at 0x0000018C180C4470, file "app\services\operator\operator_actions.py", line 98>)
              MAKE_FUNCTION
              LOAD_CONST              28 (<code object _safe_envelope at 0x0000018C17FE1290, file "app\services\operator\operator_actions.py", line 98>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              22 (_safe_envelope)

129           LOAD_CONST              29 (<code object __annotate__ at 0x0000018C18025A30, file "app\services\operator\operator_actions.py", line 129>)
              MAKE_FUNCTION
              LOAD_CONST              30 (<code object _validate_context at 0x0000018C1804D210, file "app\services\operator\operator_actions.py", line 129>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              23 (_validate_context)

153           LOAD_CONST              31 (<code object __annotate__ at 0x0000018C18024B30, file "app\services\operator\operator_actions.py", line 153>)
              MAKE_FUNCTION
              LOAD_CONST              32 (<code object _handle_pause at 0x0000018C1804C9F0, file "app\services\operator\operator_actions.py", line 153>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              24 (_handle_pause)

173           LOAD_CONST              33 (<code object __annotate__ at 0x0000018C18025D30, file "app\services\operator\operator_actions.py", line 173>)
              MAKE_FUNCTION
              LOAD_CONST              34 (<code object _handle_resume at 0x0000018C17F01250, file "app\services\operator\operator_actions.py", line 173>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              25 (_handle_resume)

198           LOAD_CONST              35 (<code object __annotate__ at 0x0000018C18025E30, file "app\services\operator\operator_actions.py", line 198>)
              MAKE_FUNCTION
              LOAD_CONST              36 (<code object _handle_mark_onboarding_stage at 0x0000018C17D8B340, file "app\services\operator\operator_actions.py", line 198>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              26 (_handle_mark_onboarding_stage)

237           LOAD_CONST              37 (<code object __annotate__ at 0x0000018C18025C30, file "app\services\operator\operator_actions.py", line 237>)
              MAKE_FUNCTION
              LOAD_CONST              38 (<code object _handle_mark_pilot_stage at 0x0000018C17FEDA30, file "app\services\operator\operator_actions.py", line 237>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              27 (_handle_mark_pilot_stage)

270           LOAD_CONST              39 (<code object __annotate__ at 0x0000018C18024930, file "app\services\operator\operator_actions.py", line 270>)
              MAKE_FUNCTION
              LOAD_CONST              40 (<code object _handle_mark_callback_completed at 0x0000018C17F001D0, file "app\services\operator\operator_actions.py", line 270>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              28 (_handle_mark_callback_completed)

301           LOAD_CONST              41 (<code object __annotate__ at 0x0000018C18025730, file "app\services\operator\operator_actions.py", line 301>)
              MAKE_FUNCTION
              LOAD_CONST              42 (<code object _handle_acknowledge_alert at 0x0000018C1804CB90, file "app\services\operator\operator_actions.py", line 301>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              29 (_handle_acknowledge_alert)

333           LOAD_CONST              43 (<code object __annotate__ at 0x0000018C18026530, file "app\services\operator\operator_actions.py", line 333>)
              MAKE_FUNCTION
              LOAD_CONST              44 (<code object _handle_run_readiness_snapshot at 0x0000018C17D8BF50, file "app\services\operator\operator_actions.py", line 333>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              30 (_handle_run_readiness_snapshot)

401           LOAD_CONST              45 (<code object __annotate__ at 0x0000018C18026630, file "app\services\operator\operator_actions.py", line 401>)
              MAKE_FUNCTION
              LOAD_CONST              46 (<code object _handle_request_readiness_email at 0x0000018C18060A50, file "app\services\operator\operator_actions.py", line 401>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              31 (_handle_request_readiness_email)

446           LOAD_CONST              47 (<code object __annotate__ at 0x0000018C18026430, file "app\services\operator\operator_actions.py", line 446>)
              MAKE_FUNCTION
              LOAD_CONST              48 (<code object _handle_rotate_brokerage_api_key at 0x0000018C180C47A0, file "app\services\operator\operator_actions.py", line 446>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              32 (_handle_rotate_brokerage_api_key)

484           LOAD_CONST              49 (<code object __annotate__ at 0x0000018C18025830, file "app\services\operator\operator_actions.py", line 484>)
              MAKE_FUNCTION
              LOAD_CONST              50 (<code object _handle_mark_pilot_stage_with_evidence at 0x0000018C17D8C830, file "app\services\operator\operator_actions.py", line 484>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              33 (_handle_mark_pilot_stage_with_evidence)

545           LOAD_CONST               6 ('pause_brokerage')
              LOAD_NAME               24 (_handle_pause)

546           LOAD_CONST               7 ('resume_brokerage')
              LOAD_NAME               25 (_handle_resume)

547           LOAD_CONST               8 ('mark_onboarding_stage')
              LOAD_NAME               26 (_handle_mark_onboarding_stage)

548           LOAD_CONST               9 ('mark_pilot_stage')
              LOAD_NAME               27 (_handle_mark_pilot_stage)

549           LOAD_CONST              10 ('mark_callback_completed')
              LOAD_NAME               28 (_handle_mark_callback_completed)

550           LOAD_CONST              11 ('acknowledge_alert')
              LOAD_NAME               29 (_handle_acknowledge_alert)

551           LOAD_CONST              12 ('run_readiness_snapshot')
              LOAD_NAME               30 (_handle_run_readiness_snapshot)

553           LOAD_CONST              13 ('request_readiness_email')
              LOAD_NAME               31 (_handle_request_readiness_email)

554           LOAD_CONST              14 ('rotate_brokerage_api_key')
              LOAD_NAME               32 (_handle_rotate_brokerage_api_key)

555           LOAD_CONST              15 ('mark_pilot_stage_with_evidence')
              LOAD_NAME               33 (_handle_mark_pilot_stage_with_evidence)

544           BUILD_MAP               10
              STORE_NAME              34 (_DISPATCH)

563           LOAD_CONST              51 (<code object __annotate__ at 0x0000018C17FA2A60, file "app\services\operator\operator_actions.py", line 563>)
              MAKE_FUNCTION
              LOAD_CONST              52 (<code object _audit_actor_type at 0x0000018C17FE1530, file "app\services\operator\operator_actions.py", line 563>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              35 (_audit_actor_type)

575           LOAD_CONST              53 (<code object __annotate__ at 0x0000018C17FA3690, file "app\services\operator\operator_actions.py", line 575>)
              MAKE_FUNCTION
              LOAD_CONST              54 (<code object _audit_status_from_dispatch at 0x0000018C18053BD0, file "app\services\operator\operator_actions.py", line 575>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              36 (_audit_status_from_dispatch)

586           LOAD_CONST              55 (<code object __annotate__ at 0x0000018C180C4140, file "app\services\operator\operator_actions.py", line 586>)
              MAKE_FUNCTION
              LOAD_CONST              56 (<code object _emit_audit_entry at 0x0000018C181A2DC0, file "app\services\operator\operator_actions.py", line 586>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              37 (_emit_audit_entry)

686           LOAD_CONST              57 ('payload')

692           LOAD_CONST               2 (None)

686           BUILD_MAP                1
              LOAD_CONST              58 (<code object __annotate__ at 0x0000018C18025F30, file "app\services\operator\operator_actions.py", line 686>)
              MAKE_FUNCTION
              LOAD_CONST              59 (<code object execute_action at 0x0000018C17E8AF90, file "app\services\operator\operator_actions.py", line 686>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              38 (execute_action)

780           BUILD_LIST               0
              LOAD_CONST              62 (('ALLOWED_OPERATOR_ACTIONS', 'ALLOWED_ACTOR_TYPES', 'execute_action'))
              LIST_EXTEND              1
              STORE_NAME              39 (__all__)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025130, file "app\services\operator\operator_actions.py", line 83>:
 83           RESUME                   0
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

Disassembly of <code object _bound_str at 0x0000018C18010DF0, file "app\services\operator\operator_actions.py", line 83>:
 83           RESUME                   0

 84           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

 85           LOAD_CONST               0 (None)
              RETURN_VALUE

 86   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               2 (s)

 87           LOAD_FAST_BORROW         2 (s)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

 88           LOAD_CONST               0 (None)
              RETURN_VALUE

 89   L2:     LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         2 (s)
              CALL                     1
              LOAD_FAST_BORROW         1 (max_len)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

 90           LOAD_CONST               0 (None)
              RETURN_VALUE

 91   L3:     LOAD_FAST_BORROW         2 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "app\services\operator\operator_actions.py", line 94>:
 94           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038670, file "app\services\operator\operator_actions.py", line 94>:
 94           RESUME                   0

 95           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C180C4470, file "app\services\operator\operator_actions.py", line 98>:
 98           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')

100           LOAD_CONST               2 ('str')

 98           LOAD_CONST               3 ('action')

101           LOAD_CONST               4 ('Optional[str]')

 98           LOAD_CONST               5 ('brokerage_id')

102           LOAD_CONST               4 ('Optional[str]')

 98           LOAD_CONST               6 ('actor_type')

103           LOAD_CONST               4 ('Optional[str]')

 98           LOAD_CONST               7 ('actor_id')

104           LOAD_CONST               4 ('Optional[str]')

 98           LOAD_CONST               8 ('result')

105           LOAD_CONST               9 ('Optional[Dict[str, Any]]')

 98           LOAD_CONST              10 ('warnings')

106           LOAD_CONST              11 ('Optional[List[str]]')

 98           LOAD_CONST              12 ('error_code')

107           LOAD_CONST               4 ('Optional[str]')

 98           LOAD_CONST              13 ('return')

108           LOAD_CONST              14 ('Dict[str, Any]')

 98           BUILD_MAP                9
              RETURN_VALUE

Disassembly of <code object _safe_envelope at 0x0000018C17FE1290, file "app\services\operator\operator_actions.py", line 98>:
 98           RESUME                   0

110           LOAD_CONST               0 ('actor_type')
              LOAD_FAST_BORROW         3 (actor_type)

111           LOAD_CONST               1 ('actor_id')
              LOAD_FAST_BORROW         4 (actor_id)

112           LOAD_CONST               2 ('action')
              LOAD_FAST_BORROW         1 (action)

113           LOAD_CONST               3 ('brokerage_id')
              LOAD_FAST_BORROW         2 (brokerage_id)

114           LOAD_CONST               4 ('status')
              LOAD_FAST_BORROW         0 (status)

115           LOAD_CONST               5 ('event')
              LOAD_CONST               6 ('operator.action.executed')

116           LOAD_CONST               7 ('ts')
              LOAD_GLOBAL              1 (_now_iso + NULL)
              CALL                     0

109           BUILD_MAP                7
              STORE_FAST               8 (audit)

119           LOAD_CONST               4 ('status')
              LOAD_FAST                0 (status)

120           LOAD_CONST               2 ('action')
              LOAD_FAST                1 (action)

121           LOAD_CONST               3 ('brokerage_id')
              LOAD_FAST                2 (brokerage_id)

122           LOAD_CONST               8 ('result')
              LOAD_FAST                5 (result)

123           LOAD_CONST               9 ('audit')
              LOAD_FAST                8 (audit)

124           LOAD_CONST              10 ('warnings')
              LOAD_GLOBAL              3 (list + NULL)
              LOAD_FAST                6 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

125           LOAD_CONST              11 ('error_code')
              LOAD_FAST_BORROW         7 (error_code)

118           BUILD_MAP                7
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025A30, file "app\services\operator\operator_actions.py", line 129>:
129           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('actor_type')

130           LOAD_CONST               2 ('Any')

129           LOAD_CONST               3 ('actor_id')

131           LOAD_CONST               2 ('Any')

129           LOAD_CONST               4 ('return')

132           LOAD_CONST               5 ('Optional[Dict[str, Any]]')

129           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _validate_context at 0x0000018C1804D210, file "app\services\operator\operator_actions.py", line 129>:
129           RESUME                   0

133           LOAD_FAST_BORROW         0 (actor_type)
              LOAD_GLOBAL              0 (ALLOWED_ACTOR_TYPES)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE       54 (to L2)
              NOT_TAKEN

134           LOAD_GLOBAL              3 (_safe_envelope + NULL)

135           LOAD_CONST               0 ('failed')

136           LOAD_GLOBAL              5 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (actor_type)
              LOAD_GLOBAL              6 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       18 (to L1)
              NOT_TAKEN
              LOAD_GLOBAL              7 (str + NULL)
              LOAD_FAST_BORROW         0 (actor_type)
              CALL                     1

137           LOAD_CONST               2 ('invalid_actor_type')

134           LOAD_CONST               3 (('status', 'actor_type', 'error_code'))
              CALL_KW                  3
              RETURN_VALUE

136   L1:     LOAD_CONST               1 (None)

137           LOAD_CONST               2 ('invalid_actor_type')

134           LOAD_CONST               3 (('status', 'actor_type', 'error_code'))
              CALL_KW                  3
              RETURN_VALUE

139   L2:     LOAD_GLOBAL              9 (_bound_str + NULL)
              LOAD_FAST_BORROW         1 (actor_id)
              LOAD_GLOBAL             10 (_ACTOR_ID_MAX_LEN)
              CALL                     2
              STORE_FAST               2 (bounded_actor)

140           LOAD_FAST_BORROW         2 (bounded_actor)
              POP_JUMP_IF_NOT_NONE    15 (to L3)
              NOT_TAKEN

141           LOAD_GLOBAL              3 (_safe_envelope + NULL)

142           LOAD_CONST               0 ('failed')

143           LOAD_FAST_BORROW         0 (actor_type)

144           LOAD_CONST               4 ('invalid_actor_id')

141           LOAD_CONST               3 (('status', 'actor_type', 'error_code'))
              CALL_KW                  3
              RETURN_VALUE

146   L3:     LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024B30, file "app\services\operator\operator_actions.py", line 153>:
153           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

155           LOAD_CONST               2 ('str')

153           LOAD_CONST               3 ('actor_type')

156           LOAD_CONST               2 ('str')

153           LOAD_CONST               4 ('actor_id')

157           LOAD_CONST               2 ('str')

153           LOAD_CONST               5 ('payload')

158           LOAD_CONST               6 ('Dict[str, Any]')

153           LOAD_CONST               7 ('return')

159           LOAD_CONST               6 ('Dict[str, Any]')

153           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _handle_pause at 0x0000018C1804C9F0, file "app\services\operator\operator_actions.py", line 153>:
153           RESUME                   0

160           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('pause_brokerage',))
              IMPORT_NAME              0 (app.services.brokerage.profile_service)
              IMPORT_FROM              1 (pause_brokerage)
              STORE_FAST               4 (pause_brokerage)
              POP_TOP

161           LOAD_FAST_BORROW         4 (pause_brokerage)
              PUSH_NULL
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (brokerage_id, actor_id)
              LOAD_CONST               2 (('brokerage_id', 'actor_id'))
              CALL_KW                  2
              STORE_FAST               5 (env)

162           LOAD_GLOBAL              5 (_safe_envelope + NULL)

163           LOAD_FAST_BORROW         5 (env)
              LOAD_CONST               3 ('status')
              BINARY_OP               26 ([])
              LOAD_CONST               4 ('ok')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_CONST               4 ('ok')
              JUMP_FORWARD             8 (to L2)
      L1:     LOAD_FAST_BORROW         5 (env)
              LOAD_CONST               3 ('status')
              BINARY_OP               26 ([])

164   L2:     LOAD_CONST               5 ('pause_brokerage')

165           LOAD_FAST_BORROW         0 (brokerage_id)

166           LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (actor_type, actor_id)

167           LOAD_CONST               6 ('profile')
              LOAD_FAST_BORROW         5 (env)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               6 ('profile')
              CALL                     1
              BUILD_MAP                1

168           LOAD_FAST_BORROW         5 (env)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               7 ('warnings')
              CALL                     1

169           LOAD_FAST_BORROW         5 (env)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               8 ('error_code')
              CALL                     1

162           LOAD_CONST               9 (('status', 'action', 'brokerage_id', 'actor_type', 'actor_id', 'result', 'warnings', 'error_code'))
              CALL_KW                  8
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025D30, file "app\services\operator\operator_actions.py", line 173>:
173           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

175           LOAD_CONST               2 ('str')

173           LOAD_CONST               3 ('actor_type')

176           LOAD_CONST               2 ('str')

173           LOAD_CONST               4 ('actor_id')

177           LOAD_CONST               2 ('str')

173           LOAD_CONST               5 ('payload')

178           LOAD_CONST               6 ('Dict[str, Any]')

173           LOAD_CONST               7 ('return')

179           LOAD_CONST               6 ('Dict[str, Any]')

173           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _handle_resume at 0x0000018C17F01250, file "app\services\operator\operator_actions.py", line 173>:
173           RESUME                   0

180           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('resume_brokerage',))
              IMPORT_NAME              0 (app.services.brokerage.profile_service)
              IMPORT_FROM              1 (resume_brokerage)
              STORE_FAST               4 (resume_brokerage)
              POP_TOP

181           LOAD_FAST_BORROW         3 (payload)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               2 ('target_status')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               3 ('VERIFIED')
      L1:     STORE_FAST               5 (target)

182           LOAD_GLOBAL              7 (isinstance + NULL)
              LOAD_FAST_BORROW         5 (target)
              LOAD_GLOBAL              8 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

183           LOAD_CONST               3 ('VERIFIED')
              STORE_FAST               5 (target)

184   L2:     LOAD_FAST_BORROW         4 (resume_brokerage)
              PUSH_NULL

185           LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (brokerage_id, target)
              LOAD_FAST_BORROW         2 (actor_id)

184           LOAD_CONST               4 (('brokerage_id', 'target_status', 'actor_id'))
              CALL_KW                  3
              STORE_FAST               6 (env)

187           LOAD_GLOBAL             11 (_safe_envelope + NULL)

188           LOAD_FAST_BORROW         6 (env)
              LOAD_CONST               5 ('status')
              BINARY_OP               26 ([])
              LOAD_CONST               6 ('ok')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               6 ('ok')
              JUMP_FORWARD             8 (to L4)
      L3:     LOAD_FAST_BORROW         6 (env)
              LOAD_CONST               5 ('status')
              BINARY_OP               26 ([])

189   L4:     LOAD_CONST               7 ('resume_brokerage')

190           LOAD_FAST_BORROW         0 (brokerage_id)

191           LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (actor_type, actor_id)

192           LOAD_CONST               8 ('profile')
              LOAD_FAST_BORROW         6 (env)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               8 ('profile')
              CALL                     1
              BUILD_MAP                1

193           LOAD_FAST_BORROW         6 (env)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               9 ('warnings')
              CALL                     1

194           LOAD_FAST_BORROW         6 (env)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST              10 ('error_code')
              CALL                     1

187           LOAD_CONST              11 (('status', 'action', 'brokerage_id', 'actor_type', 'actor_id', 'result', 'warnings', 'error_code'))
              CALL_KW                  8
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025E30, file "app\services\operator\operator_actions.py", line 198>:
198           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

200           LOAD_CONST               2 ('str')

198           LOAD_CONST               3 ('actor_type')

201           LOAD_CONST               2 ('str')

198           LOAD_CONST               4 ('actor_id')

202           LOAD_CONST               2 ('str')

198           LOAD_CONST               5 ('payload')

203           LOAD_CONST               6 ('Dict[str, Any]')

198           LOAD_CONST               7 ('return')

204           LOAD_CONST               6 ('Dict[str, Any]')

198           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _handle_mark_onboarding_stage at 0x0000018C17D8B340, file "app\services\operator\operator_actions.py", line 198>:
198           RESUME                   0

205           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('update_onboarding_status', 'mark_onboarding_completed', 'ALLOWED_ONBOARDING_STATUSES'))
              IMPORT_NAME              0 (app.services.brokerage.profile_service)
              IMPORT_FROM              1 (update_onboarding_status)
              STORE_FAST               4 (update_onboarding_status)
              IMPORT_FROM              2 (mark_onboarding_completed)
              STORE_FAST               5 (mark_onboarding_completed)
              IMPORT_FROM              3 (ALLOWED_ONBOARDING_STATUSES)
              STORE_FAST               6 (ALLOWED_ONBOARDING_STATUSES)
              POP_TOP

209           LOAD_FAST_BORROW         3 (payload)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               2 ('stage')
              CALL                     1
              STORE_FAST               7 (stage)

210           LOAD_FAST_BORROW_LOAD_FAST_BORROW 118 (stage, ALLOWED_ONBOARDING_STATUSES)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE       17 (to L1)
              NOT_TAKEN

211           LOAD_GLOBAL             11 (_safe_envelope + NULL)

212           LOAD_CONST               3 ('failed')

213           LOAD_CONST               4 ('mark_onboarding_stage')

214           LOAD_FAST_BORROW         0 (brokerage_id)

215           LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (actor_type, actor_id)

216           LOAD_CONST               5 ('invalid_onboarding_status')

211           LOAD_CONST               6 (('status', 'action', 'brokerage_id', 'actor_type', 'actor_id', 'error_code'))
              CALL_KW                  6
              RETURN_VALUE

218   L1:     LOAD_FAST_BORROW         7 (stage)
              LOAD_CONST               7 ('LIVE')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE       11 (to L2)
              NOT_TAKEN

219           LOAD_FAST_BORROW         5 (mark_onboarding_completed)
              PUSH_NULL

220           LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (brokerage_id, actor_id)

219           LOAD_CONST               8 (('brokerage_id', 'actor_id'))
              CALL_KW                  2
              STORE_FAST               8 (env)
              JUMP_FORWARD            10 (to L3)

223   L2:     LOAD_FAST_BORROW         4 (update_onboarding_status)
              PUSH_NULL

224           LOAD_FAST_BORROW_LOAD_FAST_BORROW 7 (brokerage_id, stage)
              LOAD_FAST_BORROW         2 (actor_id)

223           LOAD_CONST               9 (('brokerage_id', 'new_status', 'actor_id'))
              CALL_KW                  3
              STORE_FAST               8 (env)

226   L3:     LOAD_GLOBAL             11 (_safe_envelope + NULL)

227           LOAD_FAST_BORROW         8 (env)
              LOAD_CONST              10 ('status')
              BINARY_OP               26 ([])
              LOAD_CONST              11 ('ok')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST              11 ('ok')
              JUMP_FORWARD             8 (to L5)
      L4:     LOAD_FAST_BORROW         8 (env)
              LOAD_CONST              10 ('status')
              BINARY_OP               26 ([])

228   L5:     LOAD_CONST               4 ('mark_onboarding_stage')

229           LOAD_FAST_BORROW         0 (brokerage_id)

230           LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (actor_type, actor_id)

231           LOAD_CONST              12 ('profile')
              LOAD_FAST_BORROW         8 (env)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST              12 ('profile')
              CALL                     1
              LOAD_CONST               2 ('stage')
              LOAD_FAST_BORROW         7 (stage)
              BUILD_MAP                2

232           LOAD_FAST_BORROW         8 (env)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST              13 ('warnings')
              CALL                     1

233           LOAD_FAST_BORROW         8 (env)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST              14 ('error_code')
              CALL                     1

226           LOAD_CONST              15 (('status', 'action', 'brokerage_id', 'actor_type', 'actor_id', 'result', 'warnings', 'error_code'))
              CALL_KW                  8
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025C30, file "app\services\operator\operator_actions.py", line 237>:
237           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

239           LOAD_CONST               2 ('str')

237           LOAD_CONST               3 ('actor_type')

240           LOAD_CONST               2 ('str')

237           LOAD_CONST               4 ('actor_id')

241           LOAD_CONST               2 ('str')

237           LOAD_CONST               5 ('payload')

242           LOAD_CONST               6 ('Dict[str, Any]')

237           LOAD_CONST               7 ('return')

243           LOAD_CONST               6 ('Dict[str, Any]')

237           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _handle_mark_pilot_stage at 0x0000018C17FEDA30, file "app\services\operator\operator_actions.py", line 237>:
237           RESUME                   0

244           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('update_pilot_stage', 'ALLOWED_PILOT_STAGES'))
              IMPORT_NAME              0 (app.services.brokerage.profile_service)
              IMPORT_FROM              1 (update_pilot_stage)
              STORE_FAST               4 (update_pilot_stage)
              IMPORT_FROM              2 (ALLOWED_PILOT_STAGES)
              STORE_FAST               5 (ALLOWED_PILOT_STAGES)
              POP_TOP

247           LOAD_FAST_BORROW         3 (payload)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               2 ('stage')
              CALL                     1
              STORE_FAST               6 (stage)

248           LOAD_FAST_BORROW_LOAD_FAST_BORROW 101 (stage, ALLOWED_PILOT_STAGES)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE       17 (to L1)
              NOT_TAKEN

249           LOAD_GLOBAL              9 (_safe_envelope + NULL)

250           LOAD_CONST               3 ('failed')

251           LOAD_CONST               4 ('mark_pilot_stage')

252           LOAD_FAST_BORROW         0 (brokerage_id)

253           LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (actor_type, actor_id)

254           LOAD_CONST               5 ('invalid_pilot_stage')

249           LOAD_CONST               6 (('status', 'action', 'brokerage_id', 'actor_type', 'actor_id', 'error_code'))
              CALL_KW                  6
              RETURN_VALUE

256   L1:     LOAD_FAST_BORROW         4 (update_pilot_stage)
              PUSH_NULL

257           LOAD_FAST_BORROW_LOAD_FAST_BORROW 6 (brokerage_id, stage)
              LOAD_FAST_BORROW         2 (actor_id)

256           LOAD_CONST               7 (('brokerage_id', 'new_stage', 'actor_id'))
              CALL_KW                  3
              STORE_FAST               7 (env)

259           LOAD_GLOBAL              9 (_safe_envelope + NULL)

260           LOAD_FAST_BORROW         7 (env)
              LOAD_CONST               8 ('status')
              BINARY_OP               26 ([])
              LOAD_CONST               9 ('ok')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               9 ('ok')
              JUMP_FORWARD             8 (to L3)
      L2:     LOAD_FAST_BORROW         7 (env)
              LOAD_CONST               8 ('status')
              BINARY_OP               26 ([])

261   L3:     LOAD_CONST               4 ('mark_pilot_stage')

262           LOAD_FAST_BORROW         0 (brokerage_id)

263           LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (actor_type, actor_id)

264           LOAD_CONST              10 ('profile')
              LOAD_FAST_BORROW         7 (env)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST              10 ('profile')
              CALL                     1
              LOAD_CONST               2 ('stage')
              LOAD_FAST_BORROW         6 (stage)
              BUILD_MAP                2

265           LOAD_FAST_BORROW         7 (env)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST              11 ('warnings')
              CALL                     1

266           LOAD_FAST_BORROW         7 (env)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST              12 ('error_code')
              CALL                     1

259           LOAD_CONST              13 (('status', 'action', 'brokerage_id', 'actor_type', 'actor_id', 'result', 'warnings', 'error_code'))
              CALL_KW                  8
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024930, file "app\services\operator\operator_actions.py", line 270>:
270           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

272           LOAD_CONST               2 ('str')

270           LOAD_CONST               3 ('actor_type')

273           LOAD_CONST               2 ('str')

270           LOAD_CONST               4 ('actor_id')

274           LOAD_CONST               2 ('str')

270           LOAD_CONST               5 ('payload')

275           LOAD_CONST               6 ('Dict[str, Any]')

270           LOAD_CONST               7 ('return')

276           LOAD_CONST               6 ('Dict[str, Any]')

270           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _handle_mark_callback_completed at 0x0000018C17F001D0, file "app\services\operator\operator_actions.py", line 270>:
270           RESUME                   0

277           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('mark_callback_completed',))
              IMPORT_NAME              0 (app.services.callbacks.callback_schedule)
              IMPORT_FROM              1 (mark_callback_completed)
              STORE_FAST               4 (mark_callback_completed)
              POP_TOP

278           LOAD_GLOBAL              5 (_bound_str + NULL)
              LOAD_FAST_BORROW         3 (payload)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               2 ('callback_id')
              CALL                     1
              LOAD_GLOBAL              8 (_CALLBACK_ID_MAX_LEN)
              CALL                     2
              STORE_FAST               5 (callback_id)

279           LOAD_FAST_BORROW         5 (callback_id)
              POP_JUMP_IF_NOT_NONE    17 (to L1)
              NOT_TAKEN

280           LOAD_GLOBAL             11 (_safe_envelope + NULL)

281           LOAD_CONST               3 ('failed')

282           LOAD_CONST               4 ('mark_callback_completed')

283           LOAD_FAST_BORROW         0 (brokerage_id)

284           LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (actor_type, actor_id)

285           LOAD_CONST               5 ('missing_callback_id')

280           LOAD_CONST               6 (('status', 'action', 'brokerage_id', 'actor_type', 'actor_id', 'error_code'))
              CALL_KW                  6
              RETURN_VALUE

287   L1:     LOAD_FAST_BORROW         4 (mark_callback_completed)
              PUSH_NULL

288           LOAD_FAST_BORROW_LOAD_FAST_BORROW 80 (callback_id, brokerage_id)
              LOAD_FAST_BORROW         2 (actor_id)

287           LOAD_CONST               7 (('completed_by',))
              CALL_KW                  3
              STORE_FAST               6 (env)

290           LOAD_GLOBAL             11 (_safe_envelope + NULL)

291           LOAD_FAST_BORROW         6 (env)
              LOAD_CONST               8 ('status')
              BINARY_OP               26 ([])
              LOAD_CONST               9 ('ok')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               9 ('ok')
              JUMP_FORWARD             8 (to L3)
      L2:     LOAD_FAST_BORROW         6 (env)
              LOAD_CONST               8 ('status')
              BINARY_OP               26 ([])

292   L3:     LOAD_CONST               4 ('mark_callback_completed')

293           LOAD_FAST_BORROW         0 (brokerage_id)

294           LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (actor_type, actor_id)

295           LOAD_CONST              10 ('callback')
              LOAD_FAST_BORROW         6 (env)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST              10 ('callback')
              CALL                     1
              BUILD_MAP                1

296           LOAD_FAST_BORROW         6 (env)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST              11 ('warnings')
              CALL                     1

297           LOAD_FAST_BORROW         6 (env)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST              12 ('error_code')
              CALL                     1

290           LOAD_CONST              13 (('status', 'action', 'brokerage_id', 'actor_type', 'actor_id', 'result', 'warnings', 'error_code'))
              CALL_KW                  8
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025730, file "app\services\operator\operator_actions.py", line 301>:
301           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

303           LOAD_CONST               2 ('str')

301           LOAD_CONST               3 ('actor_type')

304           LOAD_CONST               2 ('str')

301           LOAD_CONST               4 ('actor_id')

305           LOAD_CONST               2 ('str')

301           LOAD_CONST               5 ('payload')

306           LOAD_CONST               6 ('Dict[str, Any]')

301           LOAD_CONST               7 ('return')

307           LOAD_CONST               6 ('Dict[str, Any]')

301           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _handle_acknowledge_alert at 0x0000018C1804CB90, file "app\services\operator\operator_actions.py", line 301>:
301           RESUME                   0

314           LOAD_GLOBAL              1 (_bound_str + NULL)
              LOAD_FAST_BORROW         3 (payload)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               1 ('alert_id')
              CALL                     1
              LOAD_GLOBAL              4 (_ALERT_ID_MAX_LEN)
              CALL                     2
              STORE_FAST               4 (alert_id)

315           LOAD_FAST_BORROW         4 (alert_id)
              POP_JUMP_IF_NOT_NONE    17 (to L1)
              NOT_TAKEN

316           LOAD_GLOBAL              7 (_safe_envelope + NULL)

317           LOAD_CONST               2 ('failed')

318           LOAD_CONST               3 ('acknowledge_alert')

319           LOAD_FAST_BORROW         0 (brokerage_id)

320           LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (actor_type, actor_id)

321           LOAD_CONST               4 ('missing_alert_id')

316           LOAD_CONST               5 (('status', 'action', 'brokerage_id', 'actor_type', 'actor_id', 'error_code'))
              CALL_KW                  6
              RETURN_VALUE

323   L1:     LOAD_GLOBAL              1 (_bound_str + NULL)
              LOAD_FAST_BORROW         3 (payload)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               6 ('notes_token')
              CALL                     1
              LOAD_GLOBAL              8 (_NOTES_TOKEN_MAX_LEN)
              CALL                     2
              STORE_FAST               5 (notes)

324           LOAD_GLOBAL              7 (_safe_envelope + NULL)

325           LOAD_CONST               7 ('ok')

326           LOAD_CONST               3 ('acknowledge_alert')

327           LOAD_FAST_BORROW         0 (brokerage_id)

328           LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (actor_type, actor_id)

329           LOAD_CONST               1 ('alert_id')
              LOAD_FAST_BORROW         4 (alert_id)
              LOAD_CONST               6 ('notes_token')
              LOAD_FAST_BORROW         5 (notes)
              BUILD_MAP                2

324           LOAD_CONST               8 (('status', 'action', 'brokerage_id', 'actor_type', 'actor_id', 'result'))
              CALL_KW                  6
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026530, file "app\services\operator\operator_actions.py", line 333>:
333           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

335           LOAD_CONST               2 ('str')

333           LOAD_CONST               3 ('actor_type')

336           LOAD_CONST               2 ('str')

333           LOAD_CONST               4 ('actor_id')

337           LOAD_CONST               2 ('str')

333           LOAD_CONST               5 ('payload')

338           LOAD_CONST               6 ('Dict[str, Any]')

333           LOAD_CONST               7 ('return')

339           LOAD_CONST               6 ('Dict[str, Any]')

333           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _handle_run_readiness_snapshot at 0x0000018C17D8BF50, file "app\services\operator\operator_actions.py", line 333>:
 333            RESUME                   0

 344            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('get_brokerage_by_id',))
                IMPORT_NAME              0 (app.db.brokerage_store)
                IMPORT_FROM              1 (get_brokerage_by_id)
                STORE_FAST               4 (get_brokerage_by_id)
                POP_TOP

 345            LOAD_SMALL_INT           0
                LOAD_CONST               2 (('get_profile',))
                IMPORT_NAME              2 (app.services.brokerage.profile_service)
                IMPORT_FROM              3 (get_profile)
                STORE_FAST               5 (get_profile)
                POP_TOP

 346            LOAD_SMALL_INT           0
                LOAD_CONST               3 (('validate_brokerage_launch_ready',))
                IMPORT_NAME              4 (app.services.brokerage.config_validator)
                IMPORT_FROM              5 (validate_brokerage_launch_ready)
                STORE_FAST               6 (validate_brokerage_launch_ready)
                POP_TOP

 349            LOAD_SMALL_INT           0
                LOAD_CONST               4 (('heartbeat_monitor_report',))
                IMPORT_NAME              6 (app.services.worker.heartbeat_monitor)
                IMPORT_FROM              7 (heartbeat_monitor_report)
                STORE_FAST               7 (heartbeat_monitor_report)
                POP_TOP

 352            LOAD_SMALL_INT           0
                LOAD_CONST               5 (('queue_status_report',))
                IMPORT_NAME              8 (app.services.ingestion.pending_call_recovery)
                IMPORT_FROM              9 (queue_status_report)
                STORE_FAST               8 (queue_status_report)
                POP_TOP

 356            LOAD_CONST               6 (None)
                STORE_FAST               9 (brokerage)

 357            NOP

 358    L1:     LOAD_FAST_BORROW         4 (get_brokerage_by_id)
                PUSH_NULL
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                STORE_FAST               9 (brokerage)

 365    L2:     LOAD_FAST_BORROW         5 (get_profile)
                PUSH_NULL
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                STORE_FAST              11 (profile_env)

 366            LOAD_GLOBAL             31 (isinstance + NULL)
                LOAD_FAST_BORROW        11 (profile_env)
                LOAD_GLOBAL             32 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L3)
                NOT_TAKEN
                LOAD_FAST_BORROW        11 (profile_env)
                LOAD_ATTR               35 (get + NULL|self)
                LOAD_CONST               8 ('profile')
                CALL                     1
                JUMP_FORWARD             1 (to L4)
        L3:     LOAD_CONST               6 (None)
        L4:     STORE_FAST              12 (profile)

 367            LOAD_FAST_BORROW         6 (validate_brokerage_launch_ready)
                PUSH_NULL
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 156 (brokerage, profile)
                LOAD_CONST               9 (('profile',))
                CALL_KW                  2
                STORE_FAST              13 (launch_env)

 368            LOAD_FAST_BORROW         7 (heartbeat_monitor_report)
                PUSH_NULL
                LOAD_SMALL_INT          50
                LOAD_CONST              10 (('limit',))
                CALL_KW                  1
                STORE_FAST              14 (hb)

 369            LOAD_FAST_BORROW         8 (queue_status_report)
                PUSH_NULL
                LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_CONST              11 (('brokerage_id',))
                CALL_KW                  1
                STORE_FAST              15 (queue)

 371            LOAD_GLOBAL             37 (_safe_envelope + NULL)

 372            LOAD_CONST              12 ('ok')

 373            LOAD_CONST              13 ('run_readiness_snapshot')

 374            LOAD_FAST_BORROW         0 (brokerage_id)

 375            LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (actor_type, actor_id)

 377            LOAD_CONST              14 ('launch_ready')
                LOAD_GLOBAL             39 (bool + NULL)
                LOAD_FAST_BORROW        13 (launch_env)
                LOAD_ATTR               35 (get + NULL|self)
                LOAD_CONST              14 ('launch_ready')
                CALL                     1
                CALL                     1

 378            LOAD_CONST              15 ('warning_count')
                LOAD_FAST_BORROW        13 (launch_env)
                LOAD_ATTR               35 (get + NULL|self)
                LOAD_CONST              15 ('warning_count')
                LOAD_SMALL_INT           0
                CALL                     2

 379            LOAD_CONST              16 ('error_count')
                LOAD_FAST_BORROW        13 (launch_env)
                LOAD_ATTR               35 (get + NULL|self)
                LOAD_CONST              16 ('error_count')
                LOAD_SMALL_INT           0
                CALL                     2

 380            LOAD_CONST              17 ('warnings')
                LOAD_FAST_BORROW        13 (launch_env)
                LOAD_ATTR               35 (get + NULL|self)
                LOAD_CONST              17 ('warnings')
                BUILD_LIST               0
                CALL                     2

 381            LOAD_CONST              18 ('errors')
                LOAD_FAST_BORROW        13 (launch_env)
                LOAD_ATTR               35 (get + NULL|self)
                LOAD_CONST              18 ('errors')
                BUILD_LIST               0
                CALL                     2

 382            LOAD_CONST              19 ('heartbeat')

 383            LOAD_CONST              20 ('total')
                LOAD_FAST_BORROW        14 (hb)
                LOAD_ATTR               35 (get + NULL|self)
                LOAD_CONST              20 ('total')
                LOAD_SMALL_INT           0
                CALL                     2

 384            LOAD_CONST              21 ('by_status')
                LOAD_FAST_BORROW        14 (hb)
                LOAD_ATTR               35 (get + NULL|self)
                LOAD_CONST              21 ('by_status')
                BUILD_MAP                0
                CALL                     2

 385            LOAD_CONST              22 ('oldest_age_seconds')
                LOAD_FAST_BORROW        14 (hb)
                LOAD_ATTR               35 (get + NULL|self)
                LOAD_CONST              22 ('oldest_age_seconds')
                CALL                     1

 382            BUILD_MAP                3

 387            LOAD_CONST              23 ('queue')

 388            LOAD_CONST              24 ('status')
                LOAD_FAST_BORROW        15 (queue)
                LOAD_ATTR               35 (get + NULL|self)
                LOAD_CONST              24 ('status')
                CALL                     1

 389            LOAD_CONST              20 ('total')
                LOAD_FAST_BORROW        15 (queue)
                LOAD_ATTR               35 (get + NULL|self)
                LOAD_CONST              20 ('total')
                LOAD_SMALL_INT           0
                CALL                     2

 390            LOAD_CONST              22 ('oldest_age_seconds')
                LOAD_FAST_BORROW        15 (queue)
                LOAD_ATTR               35 (get + NULL|self)
                LOAD_CONST              22 ('oldest_age_seconds')
                CALL                     1

 387            BUILD_MAP                3

 392            LOAD_CONST              25 ('profile_present')
                LOAD_FAST_BORROW        12 (profile)
                LOAD_CONST               6 (None)
                IS_OP                    1 (is not)

 376            BUILD_MAP                8

 371            LOAD_CONST              26 (('status', 'action', 'brokerage_id', 'actor_type', 'actor_id', 'result'))
                CALL_KW                  6
                RETURN_VALUE

  --    L5:     PUSH_EXC_INFO

 359            LOAD_GLOBAL             20 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       55 (to L9)
                NOT_TAKEN
                STORE_FAST              10 (e)

 360    L6:     LOAD_GLOBAL             22 (logger)
                LOAD_ATTR               25 (warning + NULL|self)

 361            LOAD_CONST               7 ('run_readiness_snapshot brokerage read error type=')

 362            LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE

 361            BUILD_STRING             2

 360            CALL                     1
                POP_TOP
        L7:     POP_EXCEPT
                LOAD_CONST               6 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 363 (to L2)

  --    L8:     LOAD_CONST               6 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RERAISE                  1

 359    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L10 [1] lasti
  L6 to L7 -> L8 [1] lasti
  L8 to L10 -> L10 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026630, file "app\services\operator\operator_actions.py", line 401>:
401           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

403           LOAD_CONST               2 ('str')

401           LOAD_CONST               3 ('actor_type')

404           LOAD_CONST               2 ('str')

401           LOAD_CONST               4 ('actor_id')

405           LOAD_CONST               2 ('str')

401           LOAD_CONST               5 ('payload')

406           LOAD_CONST               6 ('Dict[str, Any]')

401           LOAD_CONST               7 ('return')

407           LOAD_CONST               6 ('Dict[str, Any]')

401           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _handle_request_readiness_email at 0x0000018C18060A50, file "app\services\operator\operator_actions.py", line 401>:
401           RESUME                   0

418           LOAD_SMALL_INT           0
              LOAD_CONST               1 (None)
              IMPORT_NAME              0 (uuid)
              STORE_FAST               4 (_uuid)

422           LOAD_GLOBAL              3 (_handle_run_readiness_snapshot + NULL)

423           LOAD_FAST_BORROW         0 (brokerage_id)

424           LOAD_FAST_BORROW         1 (actor_type)

425           LOAD_FAST_BORROW         2 (actor_id)

426           LOAD_FAST_BORROW         3 (payload)

422           LOAD_CONST               2 (('brokerage_id', 'actor_type', 'actor_id', 'payload'))
              CALL_KW                  4
              STORE_FAST               5 (snapshot_env)

430           LOAD_FAST_BORROW         4 (_uuid)
              LOAD_ATTR                5 (uuid4 + NULL|self)
              CALL                     0
              LOAD_ATTR                6 (hex)
              STORE_FAST               6 (request_id)

431           LOAD_GLOBAL              9 (_safe_envelope + NULL)

432           LOAD_FAST_BORROW         5 (snapshot_env)
              LOAD_ATTR               11 (get + NULL|self)
              LOAD_CONST               3 ('status')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('ok')

433   L1:     LOAD_CONST               5 ('request_readiness_email')

434           LOAD_FAST_BORROW         0 (brokerage_id)

435           LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (actor_type, actor_id)

437           LOAD_CONST               6 ('request_id')
              LOAD_FAST_BORROW         6 (request_id)

438           LOAD_CONST               7 ('snapshot')
              LOAD_FAST_BORROW         5 (snapshot_env)
              LOAD_ATTR               11 (get + NULL|self)
              LOAD_CONST               8 ('result')
              CALL                     1

439           LOAD_CONST               9 ('real_email_sent')
              LOAD_CONST              10 (False)

440           LOAD_CONST              11 ('email_send_dispatched')
              LOAD_CONST              10 (False)

436           BUILD_MAP                4

442           LOAD_CONST              12 ('pas175_request_only_no_email_sent')
              BUILD_LIST               1

431           LOAD_CONST              13 (('status', 'action', 'brokerage_id', 'actor_type', 'actor_id', 'result', 'warnings'))
              CALL_KW                  7
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026430, file "app\services\operator\operator_actions.py", line 446>:
446           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

448           LOAD_CONST               2 ('str')

446           LOAD_CONST               3 ('actor_type')

449           LOAD_CONST               2 ('str')

446           LOAD_CONST               4 ('actor_id')

450           LOAD_CONST               2 ('str')

446           LOAD_CONST               5 ('payload')

451           LOAD_CONST               6 ('Dict[str, Any]')

446           LOAD_CONST               7 ('return')

452           LOAD_CONST               6 ('Dict[str, Any]')

446           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _handle_rotate_brokerage_api_key at 0x0000018C180C47A0, file "app\services\operator\operator_actions.py", line 446>:
446           RESUME                   0

466           LOAD_GLOBAL              1 (_safe_envelope + NULL)

467           LOAD_CONST               1 ('ok')

468           LOAD_CONST               2 ('rotate_brokerage_api_key')

469           LOAD_FAST_BORROW         0 (brokerage_id)

470           LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (actor_type, actor_id)

472           LOAD_CONST               3 ('rotation_proposal_only')
              LOAD_CONST               4 (True)

473           LOAD_CONST               5 ('execute_via')
              LOAD_CONST               6 ('POST /admin/brokerages/{id}/rotate-key')

474           LOAD_CONST               7 ('key_rotated')
              LOAD_CONST               8 (False)

475           LOAD_CONST               9 ('fingerprint')
              LOAD_CONST              10 (None)

471           BUILD_MAP                4

478           LOAD_CONST              11 ('pas175_rotation_proposal_only')

479           LOAD_CONST              12 ('use_admin_rotate_route_to_execute')

477           BUILD_LIST               2

466           LOAD_CONST              13 (('status', 'action', 'brokerage_id', 'actor_type', 'actor_id', 'result', 'warnings'))
              CALL_KW                  7
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025830, file "app\services\operator\operator_actions.py", line 484>:
484           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

486           LOAD_CONST               2 ('str')

484           LOAD_CONST               3 ('actor_type')

487           LOAD_CONST               2 ('str')

484           LOAD_CONST               4 ('actor_id')

488           LOAD_CONST               2 ('str')

484           LOAD_CONST               5 ('payload')

489           LOAD_CONST               6 ('Dict[str, Any]')

484           LOAD_CONST               7 ('return')

490           LOAD_CONST               6 ('Dict[str, Any]')

484           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _handle_mark_pilot_stage_with_evidence at 0x0000018C17D8C830, file "app\services\operator\operator_actions.py", line 484>:
484           RESUME                   0

501           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('update_pilot_stage', 'ALLOWED_PILOT_STAGES'))
              IMPORT_NAME              0 (app.services.brokerage.profile_service)
              IMPORT_FROM              1 (update_pilot_stage)
              STORE_FAST               4 (update_pilot_stage)
              IMPORT_FROM              2 (ALLOWED_PILOT_STAGES)
              STORE_FAST               5 (ALLOWED_PILOT_STAGES)
              POP_TOP

504           LOAD_FAST_BORROW         3 (payload)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               2 ('stage')
              CALL                     1
              STORE_FAST               6 (stage)

505           LOAD_FAST_BORROW_LOAD_FAST_BORROW 101 (stage, ALLOWED_PILOT_STAGES)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE       17 (to L1)
              NOT_TAKEN

506           LOAD_GLOBAL              9 (_safe_envelope + NULL)

507           LOAD_CONST               3 ('failed')

508           LOAD_CONST               4 ('mark_pilot_stage_with_evidence')

509           LOAD_FAST_BORROW         0 (brokerage_id)

510           LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (actor_type, actor_id)

511           LOAD_CONST               5 ('invalid_pilot_stage')

506           LOAD_CONST               6 (('status', 'action', 'brokerage_id', 'actor_type', 'actor_id', 'error_code'))
              CALL_KW                  6
              RETURN_VALUE

513   L1:     LOAD_GLOBAL             11 (_bound_str + NULL)

514           LOAD_FAST_BORROW         3 (payload)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               7 ('evidence_audit_row_id')
              CALL                     1
              LOAD_SMALL_INT         200

513           CALL                     2
              STORE_FAST               7 (evidence)

516           LOAD_FAST_BORROW         7 (evidence)
              POP_JUMP_IF_NOT_NONE    17 (to L2)
              NOT_TAKEN

517           LOAD_GLOBAL              9 (_safe_envelope + NULL)

518           LOAD_CONST               3 ('failed')

519           LOAD_CONST               4 ('mark_pilot_stage_with_evidence')

520           LOAD_FAST_BORROW         0 (brokerage_id)

521           LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (actor_type, actor_id)

522           LOAD_CONST               8 ('missing_evidence_audit_row_id')

517           LOAD_CONST               6 (('status', 'action', 'brokerage_id', 'actor_type', 'actor_id', 'error_code'))
              CALL_KW                  6
              RETURN_VALUE

524   L2:     LOAD_FAST_BORROW         4 (update_pilot_stage)
              PUSH_NULL

525           LOAD_FAST_BORROW_LOAD_FAST_BORROW 6 (brokerage_id, stage)
              LOAD_FAST_BORROW         2 (actor_id)

524           LOAD_CONST               9 (('brokerage_id', 'new_stage', 'actor_id'))
              CALL_KW                  3
              STORE_FAST               8 (env)

527           LOAD_FAST_BORROW         8 (env)
              LOAD_CONST              10 ('status')
              BINARY_OP               26 ([])
              LOAD_CONST              11 ('ok')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST              11 ('ok')
              JUMP_FORWARD             8 (to L4)
      L3:     LOAD_FAST_BORROW         8 (env)
              LOAD_CONST              10 ('status')
              BINARY_OP               26 ([])
      L4:     STORE_FAST               9 (status)

528           LOAD_GLOBAL              9 (_safe_envelope + NULL)

529           LOAD_FAST_BORROW         9 (status)

530           LOAD_CONST               4 ('mark_pilot_stage_with_evidence')

531           LOAD_FAST_BORROW         0 (brokerage_id)

532           LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (actor_type, actor_id)

534           LOAD_CONST              12 ('profile')
              LOAD_FAST_BORROW         8 (env)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST              12 ('profile')
              CALL                     1

535           LOAD_CONST               2 ('stage')
              LOAD_FAST_BORROW         6 (stage)

536           LOAD_CONST               7 ('evidence_audit_row_id')
              LOAD_FAST_BORROW         7 (evidence)

533           BUILD_MAP                3

538           LOAD_FAST_BORROW         8 (env)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST              13 ('warnings')
              CALL                     1

539           LOAD_FAST_BORROW         8 (env)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST              14 ('error_code')
              CALL                     1

528           LOAD_CONST              15 (('status', 'action', 'brokerage_id', 'actor_type', 'actor_id', 'result', 'warnings', 'error_code'))
              CALL_KW                  8
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "app\services\operator\operator_actions.py", line 563>:
563           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('actor_type')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               2 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _audit_actor_type at 0x0000018C17FE1530, file "app\services\operator\operator_actions.py", line 563>:
563           RESUME                   0

567           LOAD_FAST                0 (actor_type)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 ('')
      L1:     LOAD_ATTR                1 (lower + NULL|self)
              CALL                     0
              LOAD_ATTR                3 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (a)

568           LOAD_FAST_BORROW         1 (a)
              LOAD_CONST               2 ('admin')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

569           LOAD_CONST               3 ('ADMIN')
              RETURN_VALUE

570   L2:     LOAD_FAST_BORROW         1 (a)
              LOAD_CONST               4 ('automation')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

571           LOAD_CONST               5 ('SYSTEM')
              RETURN_VALUE

572   L3:     LOAD_CONST               6 ('OPERATOR')
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "app\services\operator\operator_actions.py", line 575>:
575           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('env')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _audit_status_from_dispatch at 0x0000018C18053BD0, file "app\services\operator\operator_actions.py", line 575>:
575           RESUME                   0

578           LOAD_FAST_BORROW         0 (env)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               1 ('status')
              CALL                     1
              STORE_FAST               1 (s)

579           LOAD_FAST_BORROW         1 (s)
              LOAD_CONST               2 ('ok')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN

580           LOAD_CONST               3 ('SUCCESS')
              RETURN_VALUE

581   L1:     LOAD_FAST_BORROW         1 (s)
              LOAD_CONST               4 ('skipped')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

582           LOAD_CONST               5 ('SKIPPED')
              RETURN_VALUE

583   L2:     LOAD_CONST               6 ('FAILED')
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180C4140, file "app\services\operator\operator_actions.py", line 586>:
586           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('action')

588           LOAD_CONST               2 ('str')

586           LOAD_CONST               3 ('brokerage_id')

589           LOAD_CONST               4 ('Optional[str]')

586           LOAD_CONST               5 ('actor_type')

590           LOAD_CONST               2 ('str')

586           LOAD_CONST               6 ('actor_id')

591           LOAD_CONST               2 ('str')

586           LOAD_CONST               7 ('env')

592           LOAD_CONST               8 ('Dict[str, Any]')

586           LOAD_CONST               9 ('payload')

593           LOAD_CONST              10 ('Optional[Dict[str, Any]]')

586           LOAD_CONST              11 ('return')

594           LOAD_CONST              12 ('None')

586           BUILD_MAP                7
              RETURN_VALUE

Disassembly of <code object _emit_audit_entry at 0x0000018C181A2DC0, file "app\services\operator\operator_actions.py", line 586>:
 586            RESUME                   0

 598            NOP

 599    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               1 (('log_operator_action', 'ALLOWED_METADATA_KEYS'))
                IMPORT_NAME              0 (app.services.operator.audit_service)
                IMPORT_FROM              1 (log_operator_action)
                STORE_FAST               6 (log_operator_action)
                IMPORT_FROM              2 (ALLOWED_METADATA_KEYS)
                STORE_FAST               7 (ALLOWED_METADATA_KEYS)
                POP_TOP

 606            BUILD_MAP                0
                STORE_FAST               8 (md)

 607            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW         4 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               2 ('result')
                CALL                     1
                LOAD_GLOBAL             10 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L2)
                NOT_TAKEN
                LOAD_FAST_BORROW         4 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               2 ('result')
                CALL                     1
                JUMP_FORWARD             1 (to L3)
        L2:     BUILD_MAP                0
        L3:     STORE_FAST               9 (result)

 609            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW         5 (payload)
                LOAD_GLOBAL             10 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       87 (to L5)
                NOT_TAKEN

 610            LOAD_FAST_BORROW         5 (payload)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               3 ('stage')
                CALL                     1
                STORE_FAST              10 (stage)

 611            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW        10 (stage)
                LOAD_GLOBAL             12 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        5 (to L4)
                NOT_TAKEN

 612            LOAD_FAST_BORROW_LOAD_FAST_BORROW 168 (stage, md)
                LOAD_CONST               3 ('stage')
                STORE_SUBSCR

 613    L4:     LOAD_FAST_BORROW         5 (payload)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               4 ('target_status')
                CALL                     1
                STORE_FAST              11 (target_status)

 614            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW        11 (target_status)
                LOAD_GLOBAL             12 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        5 (to L5)
                NOT_TAKEN

 615            LOAD_FAST_BORROW_LOAD_FAST_BORROW 184 (target_status, md)
                LOAD_CONST               4 ('target_status')
                STORE_SUBSCR

 618    L5:     LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW         9 (result)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               5 ('profile')
                CALL                     1
                LOAD_GLOBAL             10 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L6)
                NOT_TAKEN
                LOAD_FAST_BORROW         9 (result)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               5 ('profile')
                CALL                     1
                JUMP_FORWARD             1 (to L7)
        L6:     LOAD_CONST               6 (None)
        L7:     STORE_FAST              12 (profile)

 619            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW        12 (profile)
                LOAD_GLOBAL             10 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       99 (to L9)
                NOT_TAKEN

 620            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW        12 (profile)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               7 ('onboarding_status')
                CALL                     1
                LOAD_GLOBAL             12 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       13 (to L8)
                NOT_TAKEN

 621            LOAD_FAST_BORROW        12 (profile)
                LOAD_CONST               7 ('onboarding_status')
                BINARY_OP               26 ([])
                LOAD_FAST_BORROW         8 (md)
                LOAD_CONST               7 ('onboarding_status')
                STORE_SUBSCR

 622    L8:     LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW        12 (profile)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               8 ('pilot_stage')
                CALL                     1
                LOAD_GLOBAL             12 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       13 (to L9)
                NOT_TAKEN

 623            LOAD_FAST_BORROW        12 (profile)
                LOAD_CONST               8 ('pilot_stage')
                BINARY_OP               26 ([])
                LOAD_FAST_BORROW         8 (md)
                LOAD_CONST               8 ('pilot_stage')
                STORE_SUBSCR

 625    L9:     LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW         9 (result)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               9 ('launch_ready')
                CALL                     1
                LOAD_GLOBAL             14 (bool)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       22 (to L10)
                NOT_TAKEN

 626            LOAD_GLOBAL             15 (bool + NULL)
                LOAD_FAST_BORROW         9 (result)
                LOAD_CONST               9 ('launch_ready')
                BINARY_OP               26 ([])
                CALL                     1
                LOAD_FAST_BORROW         8 (md)
                LOAD_CONST               9 ('launch_ready')
                STORE_SUBSCR

 627   L10:     LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW         9 (result)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              10 ('warning_count')
                CALL                     1
                LOAD_GLOBAL             16 (int)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       22 (to L11)
                NOT_TAKEN

 628            LOAD_GLOBAL             17 (int + NULL)
                LOAD_FAST_BORROW         9 (result)
                LOAD_CONST              10 ('warning_count')
                BINARY_OP               26 ([])
                CALL                     1
                LOAD_FAST_BORROW         8 (md)
                LOAD_CONST              10 ('warning_count')
                STORE_SUBSCR

 629   L11:     LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW         9 (result)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              11 ('error_count')
                CALL                     1
                LOAD_GLOBAL             16 (int)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       22 (to L12)
                NOT_TAKEN

 630            LOAD_GLOBAL             17 (int + NULL)
                LOAD_FAST_BORROW         9 (result)
                LOAD_CONST              11 ('error_count')
                BINARY_OP               26 ([])
                CALL                     1
                LOAD_FAST_BORROW         8 (md)
                LOAD_CONST              11 ('error_count')
                STORE_SUBSCR

 631   L12:     LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW         4 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              12 ('error_code')
                CALL                     1
                LOAD_GLOBAL             12 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       13 (to L13)
                NOT_TAKEN

 632            LOAD_FAST_BORROW         4 (env)
                LOAD_CONST              12 ('error_code')
                BINARY_OP               26 ([])
                LOAD_FAST_BORROW         8 (md)
                LOAD_CONST              12 ('error_code')
                STORE_SUBSCR

 634   L13:     LOAD_FAST_BORROW         8 (md)
                LOAD_ATTR               19 (items + NULL|self)
                CALL                     0
                GET_ITER
                LOAD_FAST_AND_CLEAR     13 (k)
                LOAD_FAST_AND_CLEAR     14 (v)
                SWAP                     3
       L14:     BUILD_MAP                0
                SWAP                     2
       L15:     FOR_ITER                15 (to L18)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST  222 (k, v)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 215 (k, ALLOWED_METADATA_KEYS)
                CONTAINS_OP              0 (in)
       L16:     POP_JUMP_IF_TRUE         3 (to L17)
                NOT_TAKEN
                JUMP_BACKWARD           13 (to L15)
       L17:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 222 (k, v)
                MAP_ADD                  2
                JUMP_BACKWARD           17 (to L15)
       L18:     END_FOR
                POP_ITER
       L19:     STORE_FAST               8 (md)
                STORE_FAST              13 (k)
                STORE_FAST              14 (v)

 639            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW         5 (payload)
                LOAD_GLOBAL             10 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       71 (to L22)
                NOT_TAKEN

 640            LOAD_FAST_BORROW         5 (payload)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              13 ('evidence_audit_row_id')
                CALL                     1
                STORE_FAST              15 (ev)

 641            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW        15 (ev)
                LOAD_GLOBAL             12 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       32 (to L22)
                NOT_TAKEN
                LOAD_SMALL_INT           0
                LOAD_GLOBAL             21 (len + NULL)
                LOAD_FAST_BORROW        15 (ev)
                CALL                     1
                SWAP                     2
                COPY                     2
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        8 (to L20)
                NOT_TAKEN
                LOAD_SMALL_INT         200
                COMPARE_OP              58 (bool(<=))
                POP_JUMP_IF_FALSE        8 (to L22)
                NOT_TAKEN
                JUMP_FORWARD             2 (to L21)
       L20:     POP_TOP
                JUMP_FORWARD             4 (to L22)

 642   L21:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 248 (ev, md)
                LOAD_CONST              13 ('evidence_audit_row_id')
                STORE_SUBSCR

 643   L22:     LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW         9 (result)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              14 ('request_id')
                CALL                     1
                LOAD_GLOBAL             12 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       13 (to L23)
                NOT_TAKEN

 644            LOAD_FAST_BORROW         9 (result)
                LOAD_CONST              14 ('request_id')
                BINARY_OP               26 ([])
                LOAD_FAST_BORROW         8 (md)
                LOAD_CONST              14 ('request_id')
                STORE_SUBSCR

 645   L23:     LOAD_FAST_BORROW         9 (result)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              15 ('rotation_proposal_only')
                CALL                     1
                LOAD_CONST              16 (True)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE        6 (to L24)
                NOT_TAKEN

 646            LOAD_CONST              16 (True)
                LOAD_FAST_BORROW         8 (md)
                LOAD_CONST              15 ('rotation_proposal_only')
                STORE_SUBSCR

 649   L24:     LOAD_CONST               6 (None)
                STORE_FAST              16 (target_type)

 650            LOAD_CONST               6 (None)
                STORE_FAST              17 (target_id)

 651            LOAD_FAST_BORROW         0 (action)
                LOAD_CONST              28 (('pause_brokerage', 'resume_brokerage', 'mark_onboarding_stage', 'mark_pilot_stage', 'mark_pilot_stage_with_evidence', 'run_readiness_snapshot', 'request_readiness_email', 'rotate_brokerage_api_key'))
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        6 (to L25)
                NOT_TAKEN

 657            LOAD_CONST              17 ('brokerage')
                STORE_FAST              16 (target_type)

 658            LOAD_FAST                1 (brokerage_id)
                STORE_FAST              17 (target_id)
                JUMP_FORWARD           173 (to L41)

 659   L25:     LOAD_FAST_BORROW         0 (action)
                LOAD_CONST              18 ('mark_callback_completed')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       81 (to L33)
                NOT_TAKEN

 660            LOAD_CONST              19 ('callback')
                STORE_FAST              16 (target_type)

 661            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW         5 (payload)
                LOAD_GLOBAL             10 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       28 (to L29)
                NOT_TAKEN
                LOAD_FAST                5 (payload)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L28)
       L26:     NOT_TAKEN
       L27:     POP_TOP
                BUILD_MAP                0
       L28:     LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              20 ('callback_id')
                CALL                     1
                JUMP_FORWARD             1 (to L30)
       L29:     LOAD_CONST               6 (None)
       L30:     STORE_FAST              18 (cid)

 662            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW        18 (cid)
                LOAD_GLOBAL             12 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L31)
                NOT_TAKEN
                LOAD_FAST               18 (cid)
                JUMP_FORWARD             1 (to L32)
       L31:     LOAD_CONST               6 (None)
       L32:     STORE_FAST              17 (target_id)
                JUMP_FORWARD            86 (to L41)

 663   L33:     LOAD_FAST_BORROW         0 (action)
                LOAD_CONST              21 ('acknowledge_alert')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       80 (to L41)
                NOT_TAKEN

 664            LOAD_CONST              22 ('alert')
                STORE_FAST              16 (target_type)

 665            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW         5 (payload)
                LOAD_GLOBAL             10 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       28 (to L37)
                NOT_TAKEN
                LOAD_FAST                5 (payload)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L36)
       L34:     NOT_TAKEN
       L35:     POP_TOP
                BUILD_MAP                0
       L36:     LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              23 ('alert_id')
                CALL                     1
                JUMP_FORWARD             1 (to L38)
       L37:     LOAD_CONST               6 (None)
       L38:     STORE_FAST              19 (aid)

 666            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW        19 (aid)
                LOAD_GLOBAL             12 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L39)
                NOT_TAKEN
                LOAD_FAST               19 (aid)
                JUMP_FORWARD             1 (to L40)
       L39:     LOAD_CONST               6 (None)
       L40:     STORE_FAST              17 (target_id)

 668   L41:     LOAD_FAST                6 (log_operator_action)
                PUSH_NULL

 669            LOAD_FAST                1 (brokerage_id)

 670            LOAD_GLOBAL             23 (_audit_actor_type + NULL)
                LOAD_FAST_BORROW         2 (actor_type)
                CALL                     1

 671            LOAD_FAST                3 (actor_id)

 672            LOAD_FAST                0 (action)

 673            LOAD_GLOBAL             25 (_audit_status_from_dispatch + NULL)
                LOAD_FAST_BORROW         4 (env)
                CALL                     1

 674            LOAD_FAST               16 (target_type)

 675            LOAD_FAST               17 (target_id)

 676            LOAD_GLOBAL             21 (len + NULL)
                LOAD_FAST_BORROW         4 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              24 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L42)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
       L42:     CALL                     1

 677            LOAD_FAST_BORROW         8 (md)

 668            LOAD_CONST              25 (('brokerage_id', 'actor_type', 'actor_id', 'action', 'status', 'target_type', 'target_id', 'warning_count', 'metadata'))
                CALL_KW                  9
                POP_TOP
       L43:     LOAD_CONST               6 (None)
                RETURN_VALUE

  --   L44:     SWAP                     2
                POP_TOP

 634            SWAP                     3
                STORE_FAST              14 (v)
                STORE_FAST              13 (k)
                RERAISE                  0

  --   L45:     PUSH_EXC_INFO

 679            LOAD_GLOBAL             26 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       58 (to L49)
                NOT_TAKEN
                STORE_FAST              20 (e)

 680   L46:     LOAD_GLOBAL             28 (logger)
                LOAD_ATTR               31 (warning + NULL|self)

 681            LOAD_CONST              26 ('_emit_audit_entry error action=')
                LOAD_FAST                0 (action)
                FORMAT_SIMPLE
                LOAD_CONST              27 (' type=')

 682            LOAD_GLOBAL             33 (type + NULL)
                LOAD_FAST               20 (e)
                CALL                     1
                LOAD_ATTR               34 (__name__)
                FORMAT_SIMPLE

 681            BUILD_STRING             4

 680            CALL                     1
                POP_TOP
       L47:     POP_EXCEPT
                LOAD_CONST               6 (None)
                STORE_FAST              20 (e)
                DELETE_FAST             20 (e)
                LOAD_CONST               6 (None)
                RETURN_VALUE

  --   L48:     LOAD_CONST               6 (None)
                STORE_FAST              20 (e)
                DELETE_FAST             20 (e)
                RERAISE                  1

 679   L49:     RERAISE                  0

  --   L50:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L14 -> L45 [0]
  L14 to L16 -> L44 [3]
  L17 to L19 -> L44 [3]
  L19 to L26 -> L45 [0]
  L27 to L34 -> L45 [0]
  L35 to L43 -> L45 [0]
  L44 to L45 -> L45 [0]
  L45 to L46 -> L50 [1] lasti
  L46 to L47 -> L48 [1] lasti
  L48 to L50 -> L50 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025F30, file "app\services\operator\operator_actions.py", line 686>:
686           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('action')

688           LOAD_CONST               2 ('str')

686           LOAD_CONST               3 ('brokerage_id')

689           LOAD_CONST               2 ('str')

686           LOAD_CONST               4 ('actor_type')

690           LOAD_CONST               2 ('str')

686           LOAD_CONST               5 ('actor_id')

691           LOAD_CONST               2 ('str')

686           LOAD_CONST               6 ('payload')

692           LOAD_CONST               7 ('Optional[Dict[str, Any]]')

686           LOAD_CONST               8 ('return')

693           LOAD_CONST               9 ('Dict[str, Any]')

686           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object execute_action at 0x0000018C17E8AF90, file "app\services\operator\operator_actions.py", line 686>:
 686            RESUME                   0

 703            LOAD_FAST_BORROW         0 (action)
                LOAD_GLOBAL              0 (ALLOWED_OPERATOR_ACTIONS)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE      168 (to L8)
                NOT_TAKEN

 704            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 705            LOAD_CONST               1 ('refused')

 706            LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (action)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       12 (to L1)
                NOT_TAKEN
                LOAD_GLOBAL              7 (str + NULL)
                LOAD_FAST_BORROW         0 (action)
                CALL                     1
                JUMP_FORWARD             1 (to L2)
        L1:     LOAD_CONST               2 (None)

 707    L2:     LOAD_CONST               3 ('action_not_allowed')

 704            LOAD_CONST               4 (('status', 'action', 'error_code'))
                CALL_KW                  3
                STORE_FAST               5 (env)

 709            LOAD_GLOBAL              9 (_emit_audit_entry + NULL)

 710            LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (action)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       12 (to L3)
                NOT_TAKEN
                LOAD_GLOBAL              7 (str + NULL)
                LOAD_FAST_BORROW         0 (action)
                CALL                     1
                JUMP_FORWARD             1 (to L4)
        L3:     LOAD_CONST               5 ('unknown')

 711    L4:     LOAD_GLOBAL             11 (_bound_str + NULL)
                LOAD_FAST_BORROW         1 (brokerage_id)
                LOAD_GLOBAL             12 (_BROKERAGE_ID_MAX_LEN)
                CALL                     2

 712            LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST_BORROW         2 (actor_type)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN
                LOAD_FAST                2 (actor_type)
                JUMP_FORWARD             1 (to L6)
        L5:     LOAD_CONST               6 ('operator')

 713    L6:     LOAD_GLOBAL             11 (_bound_str + NULL)
                LOAD_FAST_BORROW         3 (actor_id)
                LOAD_GLOBAL             14 (_ACTOR_ID_MAX_LEN)
                CALL                     2
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               5 ('unknown')

 714    L7:     BUILD_MAP                0
                LOAD_FAST_BORROW         5 (env)
                DICT_UPDATE              1
                LOAD_CONST               7 ('status')
                LOAD_CONST               8 ('skipped')
                BUILD_MAP                1
                DICT_UPDATE              1

 715            LOAD_FAST_BORROW         4 (payload)

 709            LOAD_CONST               9 (('action', 'brokerage_id', 'actor_type', 'actor_id', 'env', 'payload'))
                CALL_KW                  6
                POP_TOP

 717            LOAD_FAST_BORROW         5 (env)
                RETURN_VALUE

 718    L8:     LOAD_GLOBAL             17 (_validate_context + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (actor_type, actor_id)
                CALL                     2
                STORE_FAST               6 (ctx_err)

 719            LOAD_FAST_BORROW         6 (ctx_err)
                POP_JUMP_IF_NONE        92 (to L12)
                NOT_TAKEN

 720            LOAD_FAST_BORROW_LOAD_FAST_BORROW 6 (action, ctx_err)
                LOAD_CONST              10 ('action')
                STORE_SUBSCR

 721            LOAD_GLOBAL              9 (_emit_audit_entry + NULL)

 722            LOAD_FAST                0 (action)

 723            LOAD_GLOBAL             11 (_bound_str + NULL)
                LOAD_FAST_BORROW         1 (brokerage_id)
                LOAD_GLOBAL             12 (_BROKERAGE_ID_MAX_LEN)
                CALL                     2

 724            LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST_BORROW         2 (actor_type)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L9)
                NOT_TAKEN
                LOAD_FAST                2 (actor_type)
                JUMP_FORWARD             1 (to L10)
        L9:     LOAD_CONST               6 ('operator')

 725   L10:     LOAD_GLOBAL             11 (_bound_str + NULL)
                LOAD_FAST_BORROW         3 (actor_id)
                LOAD_GLOBAL             14 (_ACTOR_ID_MAX_LEN)
                CALL                     2
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L11)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               5 ('unknown')

 726   L11:     BUILD_MAP                0
                LOAD_FAST_BORROW         6 (ctx_err)
                DICT_UPDATE              1
                LOAD_CONST               7 ('status')
                LOAD_CONST              11 ('failed')
                BUILD_MAP                1
                DICT_UPDATE              1

 727            LOAD_FAST_BORROW         4 (payload)

 721            LOAD_CONST               9 (('action', 'brokerage_id', 'actor_type', 'actor_id', 'env', 'payload'))
                CALL_KW                  6
                POP_TOP

 729            LOAD_FAST_BORROW         6 (ctx_err)
                RETURN_VALUE

 730   L12:     LOAD_GLOBAL             11 (_bound_str + NULL)
                LOAD_FAST_BORROW         1 (brokerage_id)
                LOAD_GLOBAL             12 (_BROKERAGE_ID_MAX_LEN)
                CALL                     2
                STORE_FAST               7 (bid)

 731            LOAD_FAST_BORROW         7 (bid)
                POP_JUMP_IF_NOT_NONE    74 (to L14)
                NOT_TAKEN

 732            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 733            LOAD_CONST              11 ('failed')

 734            LOAD_FAST_BORROW         0 (action)

 735            LOAD_FAST_BORROW         2 (actor_type)

 736            LOAD_GLOBAL             11 (_bound_str + NULL)
                LOAD_FAST_BORROW         3 (actor_id)
                LOAD_GLOBAL             14 (_ACTOR_ID_MAX_LEN)
                CALL                     2

 737            LOAD_CONST              12 ('missing_brokerage_id')

 732            LOAD_CONST              13 (('status', 'action', 'actor_type', 'actor_id', 'error_code'))
                CALL_KW                  5
                STORE_FAST               5 (env)

 739            LOAD_GLOBAL              9 (_emit_audit_entry + NULL)

 740            LOAD_FAST                0 (action)

 741            LOAD_CONST               2 (None)

 742            LOAD_FAST                2 (actor_type)

 743            LOAD_GLOBAL             11 (_bound_str + NULL)
                LOAD_FAST_BORROW         3 (actor_id)
                LOAD_GLOBAL             14 (_ACTOR_ID_MAX_LEN)
                CALL                     2
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               5 ('unknown')

 744   L13:     LOAD_FAST_BORROW         5 (env)

 745            LOAD_FAST_BORROW         4 (payload)

 739            LOAD_CONST               9 (('action', 'brokerage_id', 'actor_type', 'actor_id', 'env', 'payload'))
                CALL_KW                  6
                POP_TOP

 747            LOAD_FAST_BORROW         5 (env)
                RETURN_VALUE

 748   L14:     LOAD_GLOBAL             18 (_DISPATCH)
                LOAD_FAST_BORROW         0 (action)
                BINARY_OP               26 ([])
                STORE_FAST               8 (handler)

 749            LOAD_GLOBAL             11 (_bound_str + NULL)
                LOAD_FAST_BORROW         3 (actor_id)
                LOAD_GLOBAL             14 (_ACTOR_ID_MAX_LEN)
                CALL                     2
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L15)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               6 ('operator')
       L15:     STORE_FAST               9 (bounded_actor)

 750            NOP

 751   L16:     LOAD_FAST                8 (handler)
                PUSH_NULL

 752            LOAD_FAST                7 (bid)

 753            LOAD_FAST                2 (actor_type)

 754            LOAD_FAST                9 (bounded_actor)

 755            LOAD_GLOBAL             21 (dict + NULL)
                LOAD_FAST                4 (payload)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L19)
       L17:     NOT_TAKEN
       L18:     POP_TOP
                BUILD_MAP                0
       L19:     CALL                     1

 751            LOAD_CONST              14 (('brokerage_id', 'actor_type', 'actor_id', 'payload'))
                CALL_KW                  4
                STORE_FAST              10 (result_env)

 769   L20:     LOAD_GLOBAL              9 (_emit_audit_entry + NULL)

 770            LOAD_FAST_BORROW         0 (action)

 771            LOAD_FAST_BORROW         7 (bid)

 772            LOAD_FAST_BORROW         2 (actor_type)

 773            LOAD_FAST_BORROW         9 (bounded_actor)

 774            LOAD_FAST_BORROW        10 (result_env)

 775            LOAD_FAST_BORROW         4 (payload)

 769            LOAD_CONST               9 (('action', 'brokerage_id', 'actor_type', 'actor_id', 'env', 'payload'))
                CALL_KW                  6
                POP_TOP

 777            LOAD_FAST_BORROW        10 (result_env)
                RETURN_VALUE

  --   L21:     PUSH_EXC_INFO

 757            LOAD_GLOBAL             22 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       95 (to L25)
                NOT_TAKEN
                STORE_FAST              11 (e)

 758   L22:     LOAD_GLOBAL             24 (logger)
                LOAD_ATTR               27 (warning + NULL|self)

 759            LOAD_CONST              15 ('execute_action handler error action=')
                LOAD_FAST                0 (action)
                FORMAT_SIMPLE
                LOAD_CONST              16 (' type=')

 760            LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE

 759            BUILD_STRING             4

 758            CALL                     1
                POP_TOP

 762            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 763            LOAD_CONST              11 ('failed')

 764            LOAD_FAST                0 (action)

 765            LOAD_FAST                7 (bid)

 766            LOAD_FAST_LOAD_FAST     41 (actor_type, bounded_actor)

 767            LOAD_CONST              17 ('unexpected:')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 762            LOAD_CONST              18 (('status', 'action', 'brokerage_id', 'actor_type', 'actor_id', 'error_code'))
                CALL_KW                  6
                STORE_FAST              10 (result_env)
       L23:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                JUMP_BACKWARD_NO_INTERRUPT 119 (to L20)

  --   L24:     LOAD_CONST               2 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RERAISE                  1

 757   L25:     RERAISE                  0

  --   L26:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L16 to L17 -> L21 [0]
  L18 to L20 -> L21 [0]
  L21 to L22 -> L26 [1] lasti
  L22 to L23 -> L24 [1] lasti
  L24 to L26 -> L26 [1] lasti
```
