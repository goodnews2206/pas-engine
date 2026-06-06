# operator/cutover_approval

- **pyc:** `app\services\operator\__pycache__\cutover_approval.cpython-314.pyc`
- **expected source path (absent):** `app\services\operator/cutover_approval.py`
- **co_filename (from bytecode):** `app\services\operator\cutover_approval.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** operator

## Module docstring

```
PAS187 — Two-person cutover approval service.

Programmatic enforcement of the two-person discipline
documented in
``docs/pas186_final_pilot_cutover.md`` § 5 (operator
ownership boundaries). A brokerage cannot be moved between
pilot stages until two **distinct** admin/operator actors
have approved the cutover.

Doctrine:

* **Append-only event semantics.** Each call writes a row
  / updates a row whose status transitions monotonically:
  REQUESTED -> FIRST_APPROVED -> APPROVED  (or terminal
  REJECTED / CANCELLED / EXPIRED).
* **Distinct second approver.** ``approve_cutover_second``
  refuses if the actor matches the first approver. This is
  enforced at the application layer here AND at the DB
  layer by the CHECK constraint in v35.
* **No automatic stage mutation.** Marking a cutover
  APPROVED records the decision; it does NOT mutate the
  brokerage's pilot stage. That mutation remains an
  explicit operator action (PAS173 dispatcher) requiring a
  separate audit-logged ``execute_action`` call.
* **No PII / no secrets / no raw payloads.** Free-text
  ``rationale`` is trimmed to <= 2 KB and stored in
  ``metadata.rationale_text`` only when explicitly
  supplied; rotation events are emitted via
  ``log_event_bg``.
* **NEVER raises.** Any unexpected exception collapses to
  ``status="skipped"`` + ``error_code="unexpected:<TypeName>"``
  and a logger warning.

Public surface:

  * ``request_cutover_approval(...)``
  * ``approve_cutover_first(...)``
  * ``approve_cutover_second(...)``
  * ``reject_cutover(...)``
  * ``cancel_cutover(...)``
  * ``cutover_status_report(...)``
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.db.event_logger`, `app.db.supabase_client`, `datetime`, `get_supabase`, `log_event_bg`, `logging`, `timezone`, `typing`, `uuid`

## Classes

_none_

## Functions / methods

`__annotate__`, `_db_fetch_one`, `_db_insert_request`, `_db_update_status`, `_emit_event`, `_final`, `_get_db`, `_now_iso`, `_project_row`, `_safe_actor_id`, `_safe_actor_type`, `_safe_brokerage`, `_safe_int`, `_safe_rationale`, `_safe_str`, `_safe_target_stage`, `_scan_for_forbidden`, `approve_cutover_first`, `approve_cutover_second`, `cancel_cutover`, `cutover_status_report`, `reject_cutover`, `request_cutover_approval`

## Env-key candidates

`ADMIN`, `APPROVED`, `CANCELLED`, `EXPANDED_PILOT`, `EXPIRED`, `FIRST_APPROVED`, `OPERATOR`, `PRODUCTION_READY_REVIEW`, `REJECTED`, `REJECTED_SELF_SECOND_APPROVAL`, `REQUESTED`, `TRUSTED_PILOT`

## String constants (redacted where noted)

- '\nPAS187 — Two-person cutover approval service.\n\nProgrammatic enforcement of the two-person discipline\ndocumented in\n``docs/pas186_final_pilot_cutover.md`` § 5 (operator\nownership boundaries). A brokerage cannot be moved between\npilot stages until two **distinct** admin/operator actors\nhave approved the cutover.\n\nDoctrine:\n\n* **Append-only event semantics.** Each call writes a row\n  / updates a row whose status transitions monotonically:\n  REQUESTED -> FIRST_APPROVED -> APPROVED  (or terminal\n  REJECTED / CANCELLED / EXPIRED).\n* **Distinct second approver.** ``approve_cutover_second``\n  refuses if the actor matches the first approver. This is\n  enforced at the application layer here AND at the DB\n  layer by the CHECK constraint in v35.\n* **No automatic stage mutation.** Marking a cutover\n  APPROVED records the decision; it does NOT mutate the\n  brokerage\'s pilot stage. That mutation remains an\n  explicit operator action (PAS173 dispatcher) requiring a\n  separate audit-logged ``execute_action`` call.\n* **No PII / no secrets / no raw payloads.** Free-text\n  ``rationale`` is trimmed to <= 2 KB and stored in\n  ``metadata.rationale_text`` only when explicitly\n  supplied; rotation events are emitted via\n  ``log_event_bg``.\n* **NEVER raises.** Any unexpected exception collapses to\n  ``status="skipped"`` + ``error_code="unexpected:<TypeName>"``\n  and a logger warning.\n\nPublic surface:\n\n  * ``request_cutover_approval(...)``\n  * ``approve_cutover_first(...)``\n  * ``approve_cutover_second(...)``\n  * ``reject_cutover(...)``\n  * ``cancel_cutover(...)``\n  * ``cutover_status_report(...)``\n'
- 'pas.operator.cutover_approval'
- 'pas_cutover_approvals'
- 'REQUESTED'
- 'FIRST_APPROVED'
- 'APPROVED'
- 'REJECTED'
- 'CANCELLED'
- 'EXPIRED'
- 'TRUSTED_PILOT'
- 'EXPANDED_PILOT'
- 'PRODUCTION_READY_REVIEW'
- 'ADMIN'
- 'OPERATOR'
- 'brokerage_id'
- 'status'
- 'actor_id'
- 'rationale'
- 'limit'
- 'return'
- 'str'
- 'seconds'
- 'value'
- 'Any'
- 'max_len'
- 'int'
- 'Optional[str]'
- 'envelope'
- 'obj'
- 'env'
- 'Dict[str, Any]'
- 'surface'
- 'cutover_approval surface='
- ' collapsed — forbidden token leaked'
- 'failed'
- 'error_code'
- 'cutover_envelope_forbidden_token'
- 'warnings'
- 'row'
- 'event_type'
- 'payload'
- 'None'
- 'Fire-and-forget audit event. Never raises.'
- 'target_stage'
- 'actor_type'
- 'cutover_id'
- 'requested_at'
- 'requested_by_actor_type'
- 'requested_by_actor_id'
- 'warning_count'
- 'rationale_text'
- 'skipped'
- 'metadata'
- 'warning'
- 'db_unavailable'
- 'cutover_approval insert error type='
- 'db_insert_failed:'
- 'Optional[Dict[str, Any]]'
- 'cutover_approval fetch error type='
- 'data'
- 'updates'
- 'cutover_approval update error type='
- 'db_update_failed:'
- 'Open a new cutover approval. Returns the canonical\nenvelope with the new ``cutover_id`` + bounded row.'
- 'ops.cutover.request'
- 'invalid_brokerage_id'
- 'invalid_target_stage'
- 'invalid_actor_type'
- 'cutover.requested'
- 'request_cutover_approval error type='
- 'unexpected:'
- 'Record the first approval. Status must be REQUESTED.\nReturns failed if cutover not found or already past REQUESTED.'
- 'ops.cutover.approve_first'
- 'invalid_arguments'
- 'cutover_not_found'
- 'invalid_status_transition'
- 'current_status:'
- 'first_approved_at'
- 'first_approved_by_actor_type'
- 'first_approved_by_actor_id'
- 'cutover.first_approved'
- 'approve_cutover_first error type='
- 'Record the second approval. **Refuses self-second-\napproval** — actor_id must be distinct from the\nfirst-approval actor. Status must be FIRST_APPROVED.\nTransitions to APPROVED on success.'
- 'ops.cutover.approve_second'
- 'cutover.rejected'
- 'REJECTED_SELF_SECOND_APPROVAL'
- 'self_second_approval_forbidden'
- 'second_approved_at'
- 'second_approved_by_actor_type'
- 'second_approved_by_actor_id'
- 'cutover.second_approved'
- 'action_required'
- 'operator_must_invoke_mark_pilot_stage'
- 'approve_cutover_second error type='
- 'Reject a cutover at any non-terminal status.'
- 'ops.cutover.reject'
- 'rejection_text'
- 'reject_cutover error type='
- 'Cancel a cutover. The same actor who requested it may\ncancel it; anyone with admin auth may also cancel it.'
- 'ops.cutover.cancel'
- 'cancel_cutover error type='
- 'Read-only report of cutover rows. Bounded to the\nclosed allow-list. Returns ``status="skipped"`` when DB\nis unavailable so the operator surface can still render.'
- 'ops.cutover.list'
- 'rows'
- 'count'
- 'cutover_status_report query error type='
- 'db_query_failed:'
- 'db_query_failed'
- 'cutover_status_report error type='
- 'default'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS187 — Two-person cutover approval service.\n\nProgrammatic enforcement of the two-person discipline\ndocumented in\n``docs/pas186_final_pilot_cutover.md`` § 5 (operator\nownership boundaries). A brokerage cannot be moved between\npilot stages until two **distinct** admin/operator actors\nhave approved the cutover.\n\nDoctrine:\n\n* **Append-only event semantics.** Each call writes a row\n  / updates a row whose status transitions monotonically:\n  REQUESTED -> FIRST_APPROVED -> APPROVED  (or terminal\n  REJECTED / CANCELLED / EXPIRED).\n* **Distinct second approver.** ``approve_cutover_second``\n  refuses if the actor matches the first approver. This is\n  enforced at the application layer here AND at the DB\n  layer by the CHECK constraint in v35.\n* **No automatic stage mutation.** Marking a cutover\n  APPROVED records the decision; it does NOT mutate the\n  brokerage\'s pilot stage. That mutation remains an\n  explicit operator action (PAS173 dispatcher) requiring a\n  separate audit-logged ``execute_action`` call.\n* **No PII / no secrets / no raw payloads.** Free-text\n  ``rationale`` is trimmed to <= 2 KB and stored in\n  ``metadata.rationale_text`` only when explicitly\n  supplied; rotation events are emitted via\n  ``log_event_bg``.\n* **NEVER raises.** Any unexpected exception collapses to\n  ``status="skipped"`` + ``error_code="unexpected:<TypeName>"``\n  and a logger warning.\n\nPublic surface:\n\n  * ``request_cutover_approval(...)``\n  * ``approve_cutover_first(...)``\n  * ``approve_cutover_second(...)``\n  * ``reject_cutover(...)``\n  * ``cancel_cutover(...)``\n  * ``cutover_status_report(...)``\n')
              STORE_NAME               0 (__doc__)

 45           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 47           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 48           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              4 (uuid)
              STORE_NAME               4 (uuid)

 49           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('datetime', 'timezone'))
              IMPORT_NAME              5 (datetime)
              IMPORT_FROM              5 (datetime)
              STORE_NAME               5 (datetime)
              IMPORT_FROM              6 (timezone)
              STORE_NAME               6 (timezone)
              POP_TOP

 50           LOAD_SMALL_INT           0
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

 53           LOAD_NAME                3 (logging)
              LOAD_ATTR               24 (getLogger)
              PUSH_NULL
              LOAD_CONST               5 ('pas.operator.cutover_approval')
              CALL                     1
              STORE_NAME              13 (logger)

 60           LOAD_CONST               6 ('pas_cutover_approvals')
              STORE_NAME              14 (_TABLE_NAME)

 62           LOAD_CONST               7 ('REQUESTED')
              STORE_NAME              15 (STATUS_REQUESTED)

 63           LOAD_CONST               8 ('FIRST_APPROVED')
              STORE_NAME              16 (STATUS_FIRST_APPROVED)

 64           LOAD_CONST               9 ('APPROVED')
              STORE_NAME              17 (STATUS_APPROVED)

 65           LOAD_CONST              10 ('REJECTED')
              STORE_NAME              18 (STATUS_REJECTED)

 66           LOAD_CONST              11 ('CANCELLED')
              STORE_NAME              19 (STATUS_CANCELLED)

 67           LOAD_CONST              12 ('EXPIRED')
              STORE_NAME              20 (STATUS_EXPIRED)

 69           LOAD_NAME               21 (frozenset)
              PUSH_NULL

 70           LOAD_NAME               15 (STATUS_REQUESTED)

 71           LOAD_NAME               16 (STATUS_FIRST_APPROVED)

 72           LOAD_NAME               17 (STATUS_APPROVED)

 73           LOAD_NAME               18 (STATUS_REJECTED)

 74           LOAD_NAME               19 (STATUS_CANCELLED)

 75           LOAD_NAME               20 (STATUS_EXPIRED)

 69           BUILD_SET                6
              CALL                     1
              STORE_NAME              22 (_VALID_STATUSES)

 78           LOAD_CONST              13 ('TRUSTED_PILOT')
              STORE_NAME              23 (TARGET_TRUSTED_PILOT)

 79           LOAD_CONST              14 ('EXPANDED_PILOT')
              STORE_NAME              24 (TARGET_EXPANDED_PILOT)

 80           LOAD_CONST              15 ('PRODUCTION_READY_REVIEW')
              STORE_NAME              25 (TARGET_PRODUCTION_READY_REVIEW)

 82           LOAD_NAME               21 (frozenset)
              PUSH_NULL

 83           LOAD_NAME               23 (TARGET_TRUSTED_PILOT)

 84           LOAD_NAME               24 (TARGET_EXPANDED_PILOT)

 85           LOAD_NAME               25 (TARGET_PRODUCTION_READY_REVIEW)

 82           BUILD_SET                3
              CALL                     1
              STORE_NAME              26 (_VALID_TARGET_STAGES)

 88           LOAD_CONST              16 ('ADMIN')
              STORE_NAME              27 (_ACTOR_TYPE_ADMIN)

 89           LOAD_CONST              17 ('OPERATOR')
              STORE_NAME              28 (_ACTOR_TYPE_OPERATOR)

 90           LOAD_NAME               21 (frozenset)
              PUSH_NULL
              LOAD_NAME               27 (_ACTOR_TYPE_ADMIN)
              LOAD_NAME               28 (_ACTOR_TYPE_OPERATOR)
              BUILD_SET                2
              CALL                     1
              STORE_NAME              29 (_VALID_ACTOR_TYPES)

 92           LOAD_SMALL_INT         200
              STORE_NAME              30 (_BROKERAGE_ID_MAX_LEN)

 93           LOAD_SMALL_INT         200
              STORE_NAME              31 (_ACTOR_ID_MAX_LEN)

 94           LOAD_CONST              18 (2048)
              STORE_NAME              32 (_RATIONALE_MAX_LEN)

 96           LOAD_CONST              67 (('cutover_id', 'brokerage_id', 'requested_at', 'requested_by_actor_type', 'requested_by_actor_id', 'first_approved_at', 'first_approved_by_actor_type', 'first_approved_by_actor_id', 'second_approved_at', 'second_approved_by_actor_type', 'second_approved_by_actor_id', 'status', 'target_stage', 'warning_count'))
              STORE_NAME              33 (_ROW_ALLOWLIST)

113           LOAD_CONST              68 (('phone', 'email', 'name_token', 'transcript', 'raw_payload', 'raw_email', 'raw_body', 'secret', 'signature', 'dedupe_key', 'api_key', 'token', 'stack_trace', 'prompt_text', 'env_values'))
              STORE_NAME              34 (_FORBIDDEN_RESPONSE_TOKENS)

125           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA3870, file "app\services\operator\cutover_approval.py", line 125>)
              MAKE_FUNCTION
              LOAD_CONST              22 (<code object _now_iso at 0x0000018C18038B70, file "app\services\operator\cutover_approval.py", line 125>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              35 (_now_iso)

129           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C18025530, file "app\services\operator\cutover_approval.py", line 129>)
              MAKE_FUNCTION
              LOAD_CONST              24 (<code object _safe_str at 0x0000018C17972D90, file "app\services\operator\cutover_approval.py", line 129>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              36 (_safe_str)

138           LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA3690, file "app\services\operator\cutover_approval.py", line 138>)
              MAKE_FUNCTION
              LOAD_CONST              26 (<code object _safe_brokerage at 0x0000018C18025A30, file "app\services\operator\cutover_approval.py", line 138>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              37 (_safe_brokerage)

142           LOAD_CONST              27 (<code object __annotate__ at 0x0000018C17FA2A60, file "app\services\operator\cutover_approval.py", line 142>)
              MAKE_FUNCTION
              LOAD_CONST              28 (<code object _safe_actor_id at 0x0000018C18025130, file "app\services\operator\cutover_approval.py", line 142>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              38 (_safe_actor_id)

146           LOAD_CONST              29 (<code object __annotate__ at 0x0000018C17FA3780, file "app\services\operator\cutover_approval.py", line 146>)
              MAKE_FUNCTION
              LOAD_CONST              30 (<code object _safe_actor_type at 0x0000018C18038F30, file "app\services\operator\cutover_approval.py", line 146>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              39 (_safe_actor_type)

156           LOAD_CONST              31 (<code object __annotate__ at 0x0000018C17FA3C30, file "app\services\operator\cutover_approval.py", line 156>)
              MAKE_FUNCTION
              LOAD_CONST              32 (<code object _safe_target_stage at 0x0000018C180388F0, file "app\services\operator\cutover_approval.py", line 156>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              40 (_safe_target_stage)

166           LOAD_CONST              33 (<code object __annotate__ at 0x0000018C17FA3A50, file "app\services\operator\cutover_approval.py", line 166>)
              MAKE_FUNCTION
              LOAD_CONST              34 (<code object _safe_rationale at 0x0000018C17FF10B0, file "app\services\operator\cutover_approval.py", line 166>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              41 (_safe_rationale)

179           LOAD_CONST              35 (<code object __annotate__ at 0x0000018C17FA2F10, file "app\services\operator\cutover_approval.py", line 179>)
              MAKE_FUNCTION
              LOAD_CONST              36 (<code object _scan_for_forbidden at 0x0000018C18024B30, file "app\services\operator\cutover_approval.py", line 179>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              42 (_scan_for_forbidden)

203           LOAD_CONST              37 (<code object __annotate__ at 0x0000018C18024E30, file "app\services\operator\cutover_approval.py", line 203>)
              MAKE_FUNCTION
              LOAD_CONST              38 (<code object _final at 0x0000018C17FE1680, file "app\services\operator\cutover_approval.py", line 203>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              43 (_final)

219           LOAD_CONST              39 (<code object __annotate__ at 0x0000018C17FA3000, file "app\services\operator\cutover_approval.py", line 219>)
              MAKE_FUNCTION
              LOAD_CONST              40 (<code object _project_row at 0x0000018C18052F70, file "app\services\operator\cutover_approval.py", line 219>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              44 (_project_row)

227           LOAD_CONST              41 (<code object __annotate__ at 0x0000018C18025D30, file "app\services\operator\cutover_approval.py", line 227>)
              MAKE_FUNCTION
              LOAD_CONST              42 (<code object _emit_event at 0x0000018C18038DF0, file "app\services\operator\cutover_approval.py", line 227>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              45 (_emit_event)

239           LOAD_CONST              43 (<code object _get_db at 0x0000018C18053BD0, file "app\services\operator\cutover_approval.py", line 239>)
              MAKE_FUNCTION
              STORE_NAME              46 (_get_db)

251           LOAD_CONST              44 (<code object __annotate__ at 0x0000018C18025E30, file "app\services\operator\cutover_approval.py", line 251>)
              MAKE_FUNCTION
              LOAD_CONST              45 (<code object _db_insert_request at 0x0000018C17D8AB50, file "app\services\operator\cutover_approval.py", line 251>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              47 (_db_insert_request)

301           LOAD_CONST              46 (<code object __annotate__ at 0x0000018C17FA33C0, file "app\services\operator\cutover_approval.py", line 301>)
              MAKE_FUNCTION
              LOAD_CONST              47 (<code object _db_fetch_one at 0x0000018C17EDA5A0, file "app\services\operator\cutover_approval.py", line 301>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              48 (_db_fetch_one)

326           LOAD_CONST              48 (<code object __annotate__ at 0x0000018C18025C30, file "app\services\operator\cutover_approval.py", line 326>)
              MAKE_FUNCTION
              LOAD_CONST              49 (<code object _db_update_status at 0x0000018C17ECE220, file "app\services\operator\cutover_approval.py", line 326>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              49 (_db_update_status)

356           LOAD_CONST              50 ('actor_id')

361           LOAD_CONST               2 (None)

356           LOAD_CONST              51 ('rationale')

362           LOAD_CONST               2 (None)

356           BUILD_MAP                2
              LOAD_CONST              52 (<code object __annotate__ at 0x0000018C18024930, file "app\services\operator\cutover_approval.py", line 356>)
              MAKE_FUNCTION
              LOAD_CONST              53 (<code object request_cutover_approval at 0x0000018C17D8BF50, file "app\services\operator\cutover_approval.py", line 356>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              50 (request_cutover_approval)

432           LOAD_CONST              54 (<code object __annotate__ at 0x0000018C18025830, file "app\services\operator\cutover_approval.py", line 432>)
              MAKE_FUNCTION
              LOAD_CONST              55 (<code object approve_cutover_first at 0x0000018C17D51B20, file "app\services\operator\cutover_approval.py", line 432>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              51 (approve_cutover_first)

505           LOAD_CONST              56 (<code object __annotate__ at 0x0000018C18025F30, file "app\services\operator\cutover_approval.py", line 505>)
              MAKE_FUNCTION
              LOAD_CONST              57 (<code object approve_cutover_second at 0x0000018C17E89970, file "app\services\operator\cutover_approval.py", line 505>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              52 (approve_cutover_second)

604           LOAD_CONST              51 ('rationale')

609           LOAD_CONST               2 (None)

604           BUILD_MAP                1
              LOAD_CONST              58 (<code object __annotate__ at 0x0000018C18026030, file "app\services\operator\cutover_approval.py", line 604>)
              MAKE_FUNCTION
              LOAD_CONST              59 (<code object reject_cutover at 0x0000018C177AF070, file "app\services\operator\cutover_approval.py", line 604>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              53 (reject_cutover)

680           LOAD_CONST              60 (<code object __annotate__ at 0x0000018C18025230, file "app\services\operator\cutover_approval.py", line 680>)
              MAKE_FUNCTION
              LOAD_CONST              61 (<code object cancel_cutover at 0x0000018C17E7E2C0, file "app\services\operator\cutover_approval.py", line 680>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              54 (cancel_cutover)

741           LOAD_CONST              19 ('brokerage_id')

743           LOAD_CONST               2 (None)

741           LOAD_CONST              20 ('status')

744           LOAD_CONST               2 (None)

741           LOAD_CONST              62 ('limit')

745           LOAD_SMALL_INT          50

741           BUILD_MAP                3
              LOAD_CONST              63 (<code object __annotate__ at 0x0000018C18025930, file "app\services\operator\cutover_approval.py", line 741>)
              MAKE_FUNCTION
              LOAD_CONST              64 (<code object cutover_status_report at 0x0000018C17E8B240, file "app\services\operator\cutover_approval.py", line 741>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              55 (cutover_status_report)

816           LOAD_CONST              65 (<code object __annotate__ at 0x0000018C18025630, file "app\services\operator\cutover_approval.py", line 816>)
              MAKE_FUNCTION
              LOAD_CONST              66 (<code object _safe_int at 0x0000018C18039070, file "app\services\operator\cutover_approval.py", line 816>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              56 (_safe_int)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "app\services\operator\cutover_approval.py", line 125>:
125           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038B70, file "app\services\operator\cutover_approval.py", line 125>:
125           RESUME                   0

126           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C18025530, file "app\services\operator\cutover_approval.py", line 129>:
129           RESUME                   0
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

Disassembly of <code object _safe_str at 0x0000018C17972D90, file "app\services\operator\cutover_approval.py", line 129>:
129           RESUME                   0

130           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

131           LOAD_CONST               0 (None)
              RETURN_VALUE

132   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               2 (s)

133           LOAD_FAST_BORROW         2 (s)
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

134   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

135   L3:     LOAD_FAST_BORROW         2 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "app\services\operator\cutover_approval.py", line 138>:
138           RESUME                   0
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

Disassembly of <code object _safe_brokerage at 0x0000018C18025A30, file "app\services\operator\cutover_approval.py", line 138>:
138           RESUME                   0

139           LOAD_GLOBAL              1 (_safe_str + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (_BROKERAGE_ID_MAX_LEN)
              CALL                     2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "app\services\operator\cutover_approval.py", line 142>:
142           RESUME                   0
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

Disassembly of <code object _safe_actor_id at 0x0000018C18025130, file "app\services\operator\cutover_approval.py", line 142>:
142           RESUME                   0

143           LOAD_GLOBAL              1 (_safe_str + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (_ACTOR_ID_MAX_LEN)
              CALL                     2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "app\services\operator\cutover_approval.py", line 146>:
146           RESUME                   0
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

Disassembly of <code object _safe_actor_type at 0x0000018C18038F30, file "app\services\operator\cutover_approval.py", line 146>:
146           RESUME                   0

147           LOAD_GLOBAL              1 (_safe_str + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_SMALL_INT          32
              CALL                     2
              STORE_FAST               1 (s)

148           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

149           LOAD_CONST               1 (None)
              RETURN_VALUE

150   L1:     LOAD_FAST_BORROW         1 (s)
              LOAD_ATTR                3 (upper + NULL|self)
              CALL                     0
              STORE_FAST               2 (up)

151           LOAD_FAST_BORROW         2 (up)
              LOAD_GLOBAL              4 (_VALID_ACTOR_TYPES)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

152           LOAD_CONST               1 (None)
              RETURN_VALUE

153   L2:     LOAD_FAST_BORROW         2 (up)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "app\services\operator\cutover_approval.py", line 156>:
156           RESUME                   0
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

Disassembly of <code object _safe_target_stage at 0x0000018C180388F0, file "app\services\operator\cutover_approval.py", line 156>:
156           RESUME                   0

157           LOAD_GLOBAL              1 (_safe_str + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_SMALL_INT          64
              CALL                     2
              STORE_FAST               1 (s)

158           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

159           LOAD_CONST               1 (None)
              RETURN_VALUE

160   L1:     LOAD_FAST_BORROW         1 (s)
              LOAD_ATTR                3 (upper + NULL|self)
              CALL                     0
              STORE_FAST               2 (up)

161           LOAD_FAST_BORROW         2 (up)
              LOAD_GLOBAL              4 (_VALID_TARGET_STAGES)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

162           LOAD_CONST               1 (None)
              RETURN_VALUE

163   L2:     LOAD_FAST_BORROW         2 (up)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "app\services\operator\cutover_approval.py", line 166>:
166           RESUME                   0
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

Disassembly of <code object _safe_rationale at 0x0000018C17FF10B0, file "app\services\operator\cutover_approval.py", line 166>:
166           RESUME                   0

167           LOAD_FAST_BORROW         0 (value)
              POP_JUMP_IF_NOT_NONE     3 (to L1)
              NOT_TAKEN

168           LOAD_CONST               0 (None)
              RETURN_VALUE

169   L1:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

170           LOAD_CONST               0 (None)
              RETURN_VALUE

171   L2:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

172           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN

173           LOAD_CONST               0 (None)
              RETURN_VALUE

174   L3:     LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         1 (s)
              CALL                     1
              LOAD_GLOBAL              8 (_RATIONALE_MAX_LEN)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       10 (to L4)
              NOT_TAKEN

175           LOAD_FAST_BORROW         1 (s)
              LOAD_CONST               0 (None)
              LOAD_GLOBAL              8 (_RATIONALE_MAX_LEN)
              BINARY_SLICE
              STORE_FAST               1 (s)

176   L4:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "app\services\operator\cutover_approval.py", line 179>:
179           RESUME                   0
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

Disassembly of <code object _scan_for_forbidden at 0x0000018C18024B30, file "app\services\operator\cutover_approval.py", line 179>:
  --           MAKE_CELL                1 (walk)

 179           RESUME                   0

 180           LOAD_CONST               0 (<code object __annotate__ at 0x0000018C17FA1E30, file "app\services\operator\cutover_approval.py", line 180>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         1 (walk)
               BUILD_TUPLE              1
               LOAD_CONST               1 (<code object walk at 0x0000018C17CC2960, file "app\services\operator\cutover_approval.py", line 180>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_DEREF              1 (walk)

 200           LOAD_DEREF               1 (walk)
               PUSH_NULL
               LOAD_FAST_BORROW         0 (envelope)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "app\services\operator\cutover_approval.py", line 180>:
180           RESUME                   0
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

Disassembly of <code object walk at 0x0000018C17CC2960, file "app\services\operator\cutover_approval.py", line 180>:
  --            COPY_FREE_VARS           1

 180            RESUME                   0

 181            NOP

 182    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      111 (to L16)
        L2:     NOT_TAKEN

 183    L3:     LOAD_FAST_BORROW         0 (obj)
                LOAD_ATTR                5 (items + NULL|self)
                CALL                     0
                GET_ITER
        L4:     FOR_ITER                88 (to L14)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   18 (k, v)

 184            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (k)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       42 (to L10)
                NOT_TAKEN

 185            LOAD_FAST_BORROW         1 (k)
                LOAD_ATTR                9 (lower + NULL|self)
                CALL                     0
                STORE_FAST               3 (kl)

 186            LOAD_GLOBAL             10 (_FORBIDDEN_RESPONSE_TOKENS)
                GET_ITER
        L5:     FOR_ITER                15 (to L9)
                STORE_FAST               4 (tok)

 187            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, kl)
                CONTAINS_OP              0 (in)
        L6:     POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L5)

 188    L7:     LOAD_FAST_BORROW         4 (tok)
                SWAP                     2
                POP_TOP
                SWAP                     2
                POP_TOP
        L8:     RETURN_VALUE

 186    L9:     END_FOR
                POP_ITER

 189   L10:     LOAD_DEREF               6 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                STORE_FAST               5 (sub)

 190            LOAD_FAST_BORROW         5 (sub)
                TO_BOOL
       L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           86 (to L4)

 191   L12:     LOAD_FAST_BORROW         5 (sub)
                SWAP                     2
                POP_TOP
       L13:     RETURN_VALUE

 183   L14:     END_FOR
                POP_ITER

 199   L15:     LOAD_CONST               0 (None)
                RETURN_VALUE

 192   L16:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL             12 (list)
                LOAD_GLOBAL             14 (tuple)
                BUILD_TUPLE              2
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       30 (to L22)
                NOT_TAKEN

 193            LOAD_FAST_BORROW         0 (obj)
                GET_ITER
       L17:     FOR_ITER                23 (to L21)
                STORE_FAST               2 (v)

 194            LOAD_DEREF               6 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                STORE_FAST               5 (sub)

 195            LOAD_FAST_BORROW         5 (sub)
                TO_BOOL
       L18:     POP_JUMP_IF_TRUE         3 (to L19)
                NOT_TAKEN
                JUMP_BACKWARD           21 (to L17)

 196   L19:     LOAD_FAST_BORROW         5 (sub)
                SWAP                     2
                POP_TOP
       L20:     RETURN_VALUE

 193   L21:     END_FOR
                POP_ITER

 199   L22:     LOAD_CONST               0 (None)
                RETURN_VALUE

  --   L23:     PUSH_EXC_INFO

 197            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L25)
                NOT_TAKEN
                POP_TOP

 198   L24:     POP_EXCEPT
                LOAD_CONST               0 (None)
                RETURN_VALUE

 197   L25:     RERAISE                  0

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

Disassembly of <code object __annotate__ at 0x0000018C18024E30, file "app\services\operator\cutover_approval.py", line 203>:
203           RESUME                   0
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

Disassembly of <code object _final at 0x0000018C17FE1680, file "app\services\operator\cutover_approval.py", line 203>:
203           RESUME                   0

204           LOAD_GLOBAL              1 (_scan_for_forbidden + NULL)
              LOAD_FAST_BORROW         0 (env)
              CALL                     1
              STORE_FAST               2 (leak)

205           LOAD_FAST_BORROW         2 (leak)
              TO_BOOL
              POP_JUMP_IF_FALSE       37 (to L1)
              NOT_TAKEN

206           LOAD_GLOBAL              2 (logger)
              LOAD_ATTR                5 (warning + NULL|self)

207           LOAD_CONST               0 ('cutover_approval surface=')
              LOAD_FAST_BORROW         1 (surface)
              FORMAT_SIMPLE
              LOAD_CONST               1 (' collapsed — forbidden token leaked')
              BUILD_STRING             3

206           CALL                     1
              POP_TOP

211           LOAD_CONST               2 ('status')
              LOAD_CONST               3 ('failed')

212           LOAD_CONST               4 ('surface')
              LOAD_FAST_BORROW         1 (surface)

213           LOAD_CONST               5 ('error_code')
              LOAD_CONST               6 ('cutover_envelope_forbidden_token')

214           LOAD_CONST               7 ('warnings')
              LOAD_CONST               6 ('cutover_envelope_forbidden_token')
              BUILD_LIST               1

210           BUILD_MAP                4
              RETURN_VALUE

216   L1:     LOAD_FAST_BORROW         0 (env)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3000, file "app\services\operator\cutover_approval.py", line 219>:
219           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('row')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               2 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _project_row at 0x0000018C18052F70, file "app\services\operator\cutover_approval.py", line 219>:
219           RESUME                   0

220           BUILD_MAP                0
              STORE_FAST               1 (out)

221           LOAD_GLOBAL              0 (_ROW_ALLOWLIST)
              GET_ITER
      L1:     FOR_ITER                21 (to L3)
              STORE_FAST               2 (k)

222           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (k, row)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L1)

223   L2:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (row, k)
              BINARY_OP               26 ([])
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (out, k)
              STORE_SUBSCR
              JUMP_BACKWARD           23 (to L1)

221   L3:     END_FOR
              POP_ITER

224           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025D30, file "app\services\operator\cutover_approval.py", line 227>:
227           RESUME                   0
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

Disassembly of <code object _emit_event at 0x0000018C18038DF0, file "app\services\operator\cutover_approval.py", line 227>:
 227            RESUME                   0

 229            NOP

 230    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               1 (('log_event_bg',))
                IMPORT_NAME              0 (app.db.event_logger)
                IMPORT_FROM              1 (log_event_bg)
                STORE_FAST               2 (log_event_bg)
                POP_TOP

 233    L2:     NOP

 234    L3:     LOAD_FAST                2 (log_event_bg)
                PUSH_NULL
                LOAD_FAST_LOAD_FAST      1 (event_type, payload)
                CALL                     2
                POP_TOP
        L4:     LOAD_CONST               2 (None)
                RETURN_VALUE

  --    L5:     PUSH_EXC_INFO

 231            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L7)
                NOT_TAKEN
                POP_TOP

 232    L6:     POP_EXCEPT
                LOAD_CONST               2 (None)
                RETURN_VALUE

 231    L7:     RERAISE                  0

  --    L8:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
        L9:     PUSH_EXC_INFO

 235            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L11)
                NOT_TAKEN
                POP_TOP

 236   L10:     POP_EXCEPT
                LOAD_CONST               2 (None)
                RETURN_VALUE

 235   L11:     RERAISE                  0

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

Disassembly of <code object _get_db at 0x0000018C18053BD0, file "app\services\operator\cutover_approval.py", line 239>:
 239           RESUME                   0

 240           NOP

 241   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('get_supabase',))
               IMPORT_NAME              0 (app.db.supabase_client)
               IMPORT_FROM              1 (get_supabase)
               STORE_FAST               0 (get_supabase)
               POP_TOP

 242           LOAD_FAST_BORROW         0 (get_supabase)
               PUSH_NULL
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 243           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 244   L4:     POP_EXCEPT
               LOAD_CONST               2 (None)
               RETURN_VALUE

 243   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025E30, file "app\services\operator\cutover_approval.py", line 251>:
251           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

253           LOAD_CONST               2 ('str')

251           LOAD_CONST               3 ('target_stage')

254           LOAD_CONST               2 ('str')

251           LOAD_CONST               4 ('actor_type')

255           LOAD_CONST               2 ('str')

251           LOAD_CONST               5 ('actor_id')

256           LOAD_CONST               6 ('Optional[str]')

251           LOAD_CONST               7 ('rationale')

257           LOAD_CONST               6 ('Optional[str]')

251           LOAD_CONST               8 ('return')

258           LOAD_CONST               9 ('Dict[str, Any]')

251           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _db_insert_request at 0x0000018C17D8AB50, file "app\services\operator\cutover_approval.py", line 251>:
 251            RESUME                   0

 259            LOAD_GLOBAL              1 (_get_db + NULL)
                CALL                     0
                STORE_FAST               5 (db)

 260            LOAD_GLOBAL              3 (str + NULL)
                LOAD_GLOBAL              4 (uuid)
                LOAD_ATTR                6 (uuid4)
                PUSH_NULL
                CALL                     0
                CALL                     1
                STORE_FAST               6 (cutover_id)

 261            LOAD_GLOBAL              9 (_now_iso + NULL)
                CALL                     0
                STORE_FAST               7 (requested_at)

 263            LOAD_CONST               0 ('cutover_id')
                LOAD_FAST_BORROW         6 (cutover_id)

 264            LOAD_CONST               1 ('brokerage_id')
                LOAD_FAST_BORROW         0 (brokerage_id)

 265            LOAD_CONST               2 ('requested_at')
                LOAD_FAST_BORROW         7 (requested_at)

 266            LOAD_CONST               3 ('requested_by_actor_type')
                LOAD_FAST_BORROW         2 (actor_type)

 267            LOAD_CONST               4 ('requested_by_actor_id')
                LOAD_FAST_BORROW         3 (actor_id)

 268            LOAD_CONST               5 ('status')
                LOAD_GLOBAL             10 (STATUS_REQUESTED)

 269            LOAD_CONST               6 ('target_stage')
                LOAD_FAST_BORROW         1 (target_stage)

 270            LOAD_CONST               7 ('warning_count')
                LOAD_SMALL_INT           0

 262            BUILD_MAP                8
                STORE_FAST               8 (row)

 272            LOAD_FAST_BORROW         4 (rationale)
                TO_BOOL
                POP_JUMP_IF_FALSE        6 (to L1)
                NOT_TAKEN

 276            LOAD_CONST               8 ('rationale_text')
                LOAD_FAST_BORROW         4 (rationale)
                BUILD_MAP                1
                STORE_FAST               9 (row_meta)
                JUMP_FORWARD             2 (to L2)

 278    L1:     BUILD_MAP                0
                STORE_FAST               9 (row_meta)

 279    L2:     LOAD_FAST_BORROW         5 (db)
                POP_JUMP_IF_NOT_NONE    11 (to L3)
                NOT_TAKEN

 281            LOAD_CONST               5 ('status')
                LOAD_CONST              10 ('skipped')

 282            LOAD_CONST              11 ('row')
                LOAD_FAST_BORROW         8 (row)

 283            LOAD_CONST              12 ('metadata')
                LOAD_FAST_BORROW         9 (row_meta)

 284            LOAD_CONST              13 ('warning')
                LOAD_CONST              14 ('db_unavailable')

 280            BUILD_MAP                4
                RETURN_VALUE

 286    L3:     NOP

 287    L4:     LOAD_FAST_BORROW         5 (db)
                LOAD_ATTR               13 (table + NULL|self)
                LOAD_GLOBAL             14 (_TABLE_NAME)
                CALL                     1
                LOAD_ATTR               17 (insert + NULL|self)
                BUILD_MAP                0
                LOAD_FAST_BORROW         8 (row)
                DICT_UPDATE              1
                LOAD_CONST              12 ('metadata')
                LOAD_FAST_BORROW         9 (row_meta)
                BUILD_MAP                1
                DICT_UPDATE              1
                CALL                     1
                LOAD_ATTR               19 (execute + NULL|self)
                CALL                     0
                POP_TOP

 288            LOAD_CONST               5 ('status')
                LOAD_CONST              15 ('ok')
                LOAD_CONST              11 ('row')
                LOAD_FAST_BORROW         8 (row)
                LOAD_CONST              12 ('metadata')
                LOAD_FAST_BORROW         9 (row_meta)
                BUILD_MAP                3
        L5:     RETURN_VALUE

  --    L6:     PUSH_EXC_INFO

 289            LOAD_GLOBAL             20 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       86 (to L11)
                NOT_TAKEN
                STORE_FAST              10 (e)

 290    L7:     LOAD_GLOBAL             22 (logger)
                LOAD_ATTR               25 (warning + NULL|self)

 291            LOAD_CONST              16 ('cutover_approval insert error type=')
                LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 290            CALL                     1
                POP_TOP

 294            LOAD_CONST               5 ('status')
                LOAD_CONST              10 ('skipped')

 295            LOAD_CONST              11 ('row')
                LOAD_FAST                8 (row)

 296            LOAD_CONST              12 ('metadata')
                LOAD_FAST                9 (row_meta)

 297            LOAD_CONST              13 ('warning')
                LOAD_CONST              17 ('db_insert_failed:')
                LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 293            BUILD_MAP                4
        L8:     SWAP                     2
        L9:     POP_EXCEPT
                LOAD_CONST               9 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RETURN_VALUE

  --   L10:     LOAD_CONST               9 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RERAISE                  1

 289   L11:     RERAISE                  0

  --   L12:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L4 to L5 -> L6 [0]
  L6 to L7 -> L12 [1] lasti
  L7 to L8 -> L10 [1] lasti
  L8 to L9 -> L12 [1] lasti
  L10 to L12 -> L12 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "app\services\operator\cutover_approval.py", line 301>:
301           RESUME                   0
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
              LOAD_CONST               4 ('Optional[Dict[str, Any]]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _db_fetch_one at 0x0000018C17EDA5A0, file "app\services\operator\cutover_approval.py", line 301>:
 301            RESUME                   0

 302            LOAD_GLOBAL              1 (_get_db + NULL)
                CALL                     0
                STORE_FAST               1 (db)

 303            LOAD_FAST_BORROW         1 (db)
                POP_JUMP_IF_NOT_NONE     3 (to L1)
                NOT_TAKEN

 304            LOAD_CONST               0 (None)
                RETURN_VALUE

 305    L1:     NOP

 307    L2:     LOAD_FAST_BORROW         1 (db)
                LOAD_ATTR                3 (table + NULL|self)
                LOAD_GLOBAL              4 (_TABLE_NAME)
                CALL                     1

 308            LOAD_ATTR                7 (select + NULL|self)
                LOAD_CONST               1 ('*')
                CALL                     1

 309            LOAD_ATTR                9 (eq + NULL|self)
                LOAD_CONST               2 ('cutover_id')
                LOAD_FAST_BORROW         0 (cutover_id)
                CALL                     2

 310            LOAD_ATTR               11 (limit + NULL|self)
                LOAD_SMALL_INT           1
                CALL                     1

 311            LOAD_ATTR               13 (execute + NULL|self)
                CALL                     0

 306            STORE_FAST               2 (resp)

 318    L3:     LOAD_GLOBAL             25 (getattr + NULL)
                LOAD_FAST                2 (resp)
                LOAD_CONST               4 ('data')
                LOAD_CONST               0 (None)
                CALL                     3
                STORE_FAST               4 (data)

 319            LOAD_GLOBAL             27 (isinstance + NULL)
                LOAD_FAST                4 (data)
                LOAD_GLOBAL             28 (list)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       42 (to L4)
                NOT_TAKEN
                LOAD_FAST                4 (data)
                TO_BOOL
                POP_JUMP_IF_FALSE       34 (to L4)
                NOT_TAKEN

 320            LOAD_FAST                4 (data)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                STORE_FAST               5 (first)

 321            LOAD_GLOBAL             27 (isinstance + NULL)
                LOAD_FAST                5 (first)
                LOAD_GLOBAL             30 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L4)
                NOT_TAKEN

 322            LOAD_FAST                5 (first)
                RETURN_VALUE

 323    L4:     LOAD_CONST               0 (None)
                RETURN_VALUE

  --    L5:     PUSH_EXC_INFO

 313            LOAD_GLOBAL             14 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       55 (to L9)
                NOT_TAKEN
                STORE_FAST               3 (e)

 314    L6:     LOAD_GLOBAL             16 (logger)
                LOAD_ATTR               19 (warning + NULL|self)

 315            LOAD_CONST               3 ('cutover_approval fetch error type=')
                LOAD_GLOBAL             21 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR               22 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 314            CALL                     1
                POP_TOP

 317    L7:     POP_EXCEPT
                LOAD_CONST               0 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                LOAD_CONST               0 (None)
                RETURN_VALUE

  --    L8:     LOAD_CONST               0 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 313    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L5 [0]
  L5 to L6 -> L10 [1] lasti
  L6 to L7 -> L8 [1] lasti
  L8 to L10 -> L10 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025C30, file "app\services\operator\cutover_approval.py", line 326>:
326           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('cutover_id')

328           LOAD_CONST               2 ('str')

326           LOAD_CONST               3 ('updates')

329           LOAD_CONST               4 ('Dict[str, Any]')

326           LOAD_CONST               5 ('return')

330           LOAD_CONST               4 ('Dict[str, Any]')

326           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _db_update_status at 0x0000018C17ECE220, file "app\services\operator\cutover_approval.py", line 326>:
 326            RESUME                   0

 331            LOAD_GLOBAL              1 (_get_db + NULL)
                CALL                     0
                STORE_FAST               2 (db)

 332            LOAD_FAST_BORROW         2 (db)
                POP_JUMP_IF_NOT_NONE     7 (to L1)
                NOT_TAKEN

 333            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('skipped')
                LOAD_CONST               3 ('warning')
                LOAD_CONST               4 ('db_unavailable')
                BUILD_MAP                2
                RETURN_VALUE

 334    L1:     NOP

 336    L2:     LOAD_FAST_BORROW         2 (db)
                LOAD_ATTR                3 (table + NULL|self)
                LOAD_GLOBAL              4 (_TABLE_NAME)
                CALL                     1

 337            LOAD_ATTR                7 (update + NULL|self)
                LOAD_FAST_BORROW         1 (updates)
                CALL                     1

 338            LOAD_ATTR                9 (eq + NULL|self)
                LOAD_CONST               5 ('cutover_id')
                LOAD_FAST_BORROW         0 (cutover_id)
                CALL                     2

 339            LOAD_ATTR               11 (execute + NULL|self)
                CALL                     0
                POP_TOP

 341            LOAD_CONST               1 ('status')
                LOAD_CONST               6 ('ok')
                BUILD_MAP                1
        L3:     RETURN_VALUE

  --    L4:     PUSH_EXC_INFO

 342            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       82 (to L9)
                NOT_TAKEN
                STORE_FAST               3 (e)

 343    L5:     LOAD_GLOBAL             14 (logger)
                LOAD_ATTR               17 (warning + NULL|self)

 344            LOAD_CONST               7 ('cutover_approval update error type=')
                LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 343            CALL                     1
                POP_TOP

 347            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('skipped')

 348            LOAD_CONST               3 ('warning')
                LOAD_CONST               8 ('db_update_failed:')
                LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 346            BUILD_MAP                2
        L6:     SWAP                     2
        L7:     POP_EXCEPT
                LOAD_CONST               0 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RETURN_VALUE

  --    L8:     LOAD_CONST               0 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 342    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L4 [0]
  L4 to L5 -> L10 [1] lasti
  L5 to L6 -> L8 [1] lasti
  L6 to L7 -> L10 [1] lasti
  L8 to L10 -> L10 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024930, file "app\services\operator\cutover_approval.py", line 356>:
356           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

358           LOAD_CONST               2 ('Any')

356           LOAD_CONST               3 ('target_stage')

359           LOAD_CONST               2 ('Any')

356           LOAD_CONST               4 ('actor_type')

360           LOAD_CONST               2 ('Any')

356           LOAD_CONST               5 ('actor_id')

361           LOAD_CONST               2 ('Any')

356           LOAD_CONST               6 ('rationale')

362           LOAD_CONST               2 ('Any')

356           LOAD_CONST               7 ('return')

363           LOAD_CONST               8 ('Dict[str, Any]')

356           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object request_cutover_approval at 0x0000018C17D8BF50, file "app\services\operator\cutover_approval.py", line 356>:
 356            RESUME                   0

 366            LOAD_CONST               1 ('ops.cutover.request')
                STORE_FAST               5 (surface)

 367            NOP

 368    L1:     LOAD_GLOBAL              1 (_safe_brokerage + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                STORE_FAST               6 (bid)

 369            LOAD_GLOBAL              3 (_safe_target_stage + NULL)
                LOAD_FAST_BORROW         1 (target_stage)
                CALL                     1
                STORE_FAST               7 (stage)

 370            LOAD_GLOBAL              5 (_safe_actor_type + NULL)
                LOAD_FAST_BORROW         2 (actor_type)
                CALL                     1
                STORE_FAST               8 (atype)

 371            LOAD_GLOBAL              7 (_safe_actor_id + NULL)
                LOAD_FAST_BORROW         3 (actor_id)
                CALL                     1
                STORE_FAST               9 (aid)

 372            LOAD_GLOBAL              9 (_safe_rationale + NULL)
                LOAD_FAST_BORROW         4 (rationale)
                CALL                     1
                STORE_FAST              10 (rat)

 373            LOAD_FAST_BORROW         6 (bid)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L3)
                NOT_TAKEN

 374            LOAD_GLOBAL             11 (_final + NULL)

 375            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 376            LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         5 (surface)

 377            LOAD_CONST               5 ('error_code')
                LOAD_CONST               6 ('invalid_brokerage_id')

 378            LOAD_CONST               7 ('warnings')
                LOAD_CONST               6 ('invalid_brokerage_id')
                BUILD_LIST               1

 374            BUILD_MAP                4

 379            LOAD_FAST_BORROW         5 (surface)

 374            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
        L2:     RETURN_VALUE

 380    L3:     LOAD_FAST_BORROW         7 (stage)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L7)
        L4:     NOT_TAKEN

 381    L5:     LOAD_GLOBAL             11 (_final + NULL)

 382            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 383            LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         5 (surface)

 384            LOAD_CONST               5 ('error_code')
                LOAD_CONST               9 ('invalid_target_stage')

 385            LOAD_CONST               7 ('warnings')
                LOAD_CONST               9 ('invalid_target_stage')
                BUILD_LIST               1

 381            BUILD_MAP                4

 386            LOAD_FAST_BORROW         5 (surface)

 381            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
        L6:     RETURN_VALUE

 387    L7:     LOAD_FAST_BORROW         8 (atype)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L11)
        L8:     NOT_TAKEN

 388    L9:     LOAD_GLOBAL             11 (_final + NULL)

 389            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 390            LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         5 (surface)

 391            LOAD_CONST               5 ('error_code')
                LOAD_CONST              10 ('invalid_actor_type')

 392            LOAD_CONST               7 ('warnings')
                LOAD_CONST              10 ('invalid_actor_type')
                BUILD_LIST               1

 388            BUILD_MAP                4

 393            LOAD_FAST_BORROW         5 (surface)

 388            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L10:     RETURN_VALUE

 394   L11:     LOAD_GLOBAL             13 (_db_insert_request + NULL)

 395            LOAD_FAST_BORROW         6 (bid)

 396            LOAD_FAST_BORROW         7 (stage)

 397            LOAD_FAST_BORROW         8 (atype)

 398            LOAD_FAST_BORROW         9 (aid)

 399            LOAD_FAST_BORROW        10 (rat)

 394            LOAD_CONST              11 (('brokerage_id', 'target_stage', 'actor_type', 'actor_id', 'rationale'))
                CALL_KW                  5
                STORE_FAST              11 (write)

 401            BUILD_LIST               0
                STORE_FAST              12 (warnings)

 402            LOAD_FAST_BORROW        11 (write)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              12 ('warning')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L12)
                NOT_TAKEN

 403            LOAD_FAST_BORROW        12 (warnings)
                LOAD_ATTR               17 (append + NULL|self)
                LOAD_FAST_BORROW        11 (write)
                LOAD_CONST              12 ('warning')
                BINARY_OP               26 ([])
                CALL                     1
                POP_TOP

 404   L12:     LOAD_FAST_BORROW        11 (write)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              13 ('row')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L15)
       L13:     NOT_TAKEN
       L14:     POP_TOP
                BUILD_MAP                0
       L15:     STORE_FAST              13 (row)

 405            LOAD_GLOBAL             19 (_emit_event + NULL)
                LOAD_CONST              14 ('cutover.requested')

 406            LOAD_CONST              15 ('brokerage_id')
                LOAD_FAST_BORROW         6 (bid)

 407            LOAD_CONST              16 ('cutover_id')
                LOAD_FAST_BORROW        13 (row)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              16 ('cutover_id')
                CALL                     1

 408            LOAD_CONST              17 ('target_stage')
                LOAD_FAST_BORROW         7 (stage)

 409            LOAD_CONST              18 ('actor_type')
                LOAD_FAST_BORROW         8 (atype)

 410            LOAD_CONST              19 ('actor_id')
                LOAD_FAST_BORROW         9 (aid)

 411            LOAD_CONST               2 ('status')
                LOAD_GLOBAL             20 (STATUS_REQUESTED)

 405            BUILD_MAP                6
                CALL                     2
                POP_TOP

 413            LOAD_GLOBAL             11 (_final + NULL)

 414            LOAD_CONST               2 ('status')
                LOAD_FAST_BORROW        11 (write)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST               2 ('status')
                CALL                     1
                LOAD_CONST              20 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L16)
                NOT_TAKEN
                LOAD_CONST              20 ('ok')
                JUMP_FORWARD             1 (to L17)
       L16:     LOAD_CONST              21 ('skipped')

 415   L17:     LOAD_CONST               4 ('surface')
                LOAD_FAST                5 (surface)

 416            LOAD_CONST              13 ('row')
                LOAD_GLOBAL             23 (_project_row + NULL)
                LOAD_FAST_BORROW        13 (row)
                CALL                     1

 417            LOAD_CONST               7 ('warnings')
                LOAD_FAST               12 (warnings)

 418            LOAD_CONST               5 ('error_code')
                LOAD_FAST_BORROW        11 (write)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST               2 ('status')
                CALL                     1
                LOAD_CONST              20 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L18)
                NOT_TAKEN
                LOAD_CONST              22 (None)
                JUMP_FORWARD             1 (to L19)
       L18:     LOAD_CONST              23 ('db_unavailable')

 413   L19:     BUILD_MAP                5

 419            LOAD_FAST_BORROW         5 (surface)

 413            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L20:     RETURN_VALUE

  --   L21:     PUSH_EXC_INFO

 420            LOAD_GLOBAL             24 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       97 (to L26)
                NOT_TAKEN
                STORE_FAST              14 (e)

 421   L22:     LOAD_GLOBAL             26 (logger)
                LOAD_ATTR               29 (warning + NULL|self)

 422            LOAD_CONST              24 ('request_cutover_approval error type=')
                LOAD_GLOBAL             31 (type + NULL)
                LOAD_FAST               14 (e)
                CALL                     1
                LOAD_ATTR               32 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 421            CALL                     1
                POP_TOP

 424            LOAD_GLOBAL             11 (_final + NULL)

 425            LOAD_CONST               2 ('status')
                LOAD_CONST              21 ('skipped')

 426            LOAD_CONST               4 ('surface')
                LOAD_FAST                5 (surface)

 427            LOAD_CONST               5 ('error_code')
                LOAD_CONST              25 ('unexpected:')
                LOAD_GLOBAL             31 (type + NULL)
                LOAD_FAST               14 (e)
                CALL                     1
                LOAD_ATTR               32 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 428            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 424            BUILD_MAP                4

 429            LOAD_FAST                5 (surface)

 424            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L23:     SWAP                     2
       L24:     POP_EXCEPT
                LOAD_CONST              22 (None)
                STORE_FAST              14 (e)
                DELETE_FAST             14 (e)
                RETURN_VALUE

  --   L25:     LOAD_CONST              22 (None)
                STORE_FAST              14 (e)
                DELETE_FAST             14 (e)
                RERAISE                  1

 420   L26:     RERAISE                  0

  --   L27:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L21 [0]
  L3 to L4 -> L21 [0]
  L5 to L6 -> L21 [0]
  L7 to L8 -> L21 [0]
  L9 to L10 -> L21 [0]
  L11 to L13 -> L21 [0]
  L14 to L20 -> L21 [0]
  L21 to L22 -> L27 [1] lasti
  L22 to L23 -> L25 [1] lasti
  L23 to L24 -> L27 [1] lasti
  L25 to L27 -> L27 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025830, file "app\services\operator\cutover_approval.py", line 432>:
432           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('cutover_id')

434           LOAD_CONST               2 ('Any')

432           LOAD_CONST               3 ('actor_type')

435           LOAD_CONST               2 ('Any')

432           LOAD_CONST               4 ('actor_id')

436           LOAD_CONST               2 ('Any')

432           LOAD_CONST               5 ('return')

437           LOAD_CONST               6 ('Dict[str, Any]')

432           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object approve_cutover_first at 0x0000018C17D51B20, file "app\services\operator\cutover_approval.py", line 432>:
 432            RESUME                   0

 440            LOAD_CONST               1 ('ops.cutover.approve_first')
                STORE_FAST               3 (surface)

 441            NOP

 442    L1:     LOAD_GLOBAL              1 (_safe_str + NULL)
                LOAD_FAST_BORROW         0 (cutover_id)
                LOAD_SMALL_INT          64
                CALL                     2
                STORE_FAST               4 (cid)

 443            LOAD_GLOBAL              3 (_safe_actor_type + NULL)
                LOAD_FAST_BORROW         1 (actor_type)
                CALL                     1
                STORE_FAST               5 (atype)

 444            LOAD_GLOBAL              5 (_safe_actor_id + NULL)
                LOAD_FAST_BORROW         2 (actor_id)
                CALL                     1
                STORE_FAST               6 (aid)

 445            LOAD_FAST_BORROW         4 (cid)
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L5)
                NOT_TAKEN
                LOAD_FAST_BORROW         5 (atype)
                TO_BOOL
                POP_JUMP_IF_FALSE        9 (to L5)
        L2:     NOT_TAKEN
        L3:     LOAD_FAST_BORROW         6 (aid)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L7)
        L4:     NOT_TAKEN

 446    L5:     LOAD_GLOBAL              7 (_final + NULL)

 447            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 448            LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         3 (surface)

 449            LOAD_CONST               5 ('error_code')
                LOAD_CONST               6 ('invalid_arguments')

 450            LOAD_CONST               7 ('warnings')
                LOAD_CONST               6 ('invalid_arguments')
                BUILD_LIST               1

 446            BUILD_MAP                4

 451            LOAD_FAST_BORROW         3 (surface)

 446            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
        L6:     RETURN_VALUE

 452    L7:     LOAD_GLOBAL              9 (_db_fetch_one + NULL)
                LOAD_FAST_BORROW         4 (cid)
                CALL                     1
                STORE_FAST               7 (existing)

 453            LOAD_FAST_BORROW         7 (existing)
                POP_JUMP_IF_NOT_NONE    23 (to L9)
                NOT_TAKEN

 454            LOAD_GLOBAL              7 (_final + NULL)

 455            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 456            LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         3 (surface)

 457            LOAD_CONST               5 ('error_code')
                LOAD_CONST              10 ('cutover_not_found')

 458            LOAD_CONST               7 ('warnings')
                LOAD_CONST              10 ('cutover_not_found')
                BUILD_LIST               1

 454            BUILD_MAP                4

 459            LOAD_FAST_BORROW         3 (surface)

 454            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
        L8:     RETURN_VALUE

 460    L9:     LOAD_FAST_BORROW         7 (existing)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               2 ('status')
                CALL                     1
                STORE_FAST               8 (cur_status)

 461            LOAD_FAST_BORROW         8 (cur_status)
                LOAD_GLOBAL             12 (STATUS_REQUESTED)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       26 (to L11)
                NOT_TAKEN

 462            LOAD_GLOBAL              7 (_final + NULL)

 463            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 464            LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         3 (surface)

 465            LOAD_CONST               5 ('error_code')
                LOAD_CONST              11 ('invalid_status_transition')

 466            LOAD_CONST               7 ('warnings')
                LOAD_CONST              12 ('current_status:')
                LOAD_FAST_BORROW         8 (cur_status)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 462            BUILD_MAP                4

 467            LOAD_FAST_BORROW         3 (surface)

 462            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L10:     RETURN_VALUE

 469   L11:     LOAD_CONST               2 ('status')
                LOAD_GLOBAL             14 (STATUS_FIRST_APPROVED)

 470            LOAD_CONST              13 ('first_approved_at')
                LOAD_GLOBAL             17 (_now_iso + NULL)
                CALL                     0

 471            LOAD_CONST              14 ('first_approved_by_actor_type')
                LOAD_FAST_BORROW         5 (atype)

 472            LOAD_CONST              15 ('first_approved_by_actor_id')
                LOAD_FAST_BORROW         6 (aid)

 468            BUILD_MAP                4
                STORE_FAST               9 (updates)

 474            LOAD_GLOBAL             19 (_db_update_status + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 73 (cid, updates)
                LOAD_CONST              16 (('cutover_id', 'updates'))
                CALL_KW                  2
                STORE_FAST              10 (write)

 475            BUILD_LIST               0
                STORE_FAST              11 (warnings)

 476            LOAD_FAST_BORROW        10 (write)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              17 ('warning')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L12)
                NOT_TAKEN

 477            LOAD_FAST_BORROW        11 (warnings)
                LOAD_ATTR               21 (append + NULL|self)
                LOAD_FAST_BORROW        10 (write)
                LOAD_CONST              17 ('warning')
                BINARY_OP               26 ([])
                CALL                     1
                POP_TOP

 478   L12:     LOAD_GLOBAL             23 (_emit_event + NULL)
                LOAD_CONST              18 ('cutover.first_approved')

 479            LOAD_CONST              19 ('brokerage_id')
                LOAD_FAST_BORROW         7 (existing)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              19 ('brokerage_id')
                CALL                     1

 480            LOAD_CONST              20 ('cutover_id')
                LOAD_FAST_BORROW         4 (cid)

 481            LOAD_CONST              21 ('actor_type')
                LOAD_FAST_BORROW         5 (atype)

 482            LOAD_CONST              22 ('actor_id')
                LOAD_FAST_BORROW         6 (aid)

 483            LOAD_CONST               2 ('status')
                LOAD_GLOBAL             14 (STATUS_FIRST_APPROVED)

 478            BUILD_MAP                5
                CALL                     2
                POP_TOP

 485            BUILD_MAP                0
                LOAD_FAST_BORROW         7 (existing)
                DICT_UPDATE              1
                LOAD_FAST_BORROW         9 (updates)
                DICT_UPDATE              1
                STORE_FAST              12 (new_row)

 486            LOAD_GLOBAL              7 (_final + NULL)

 487            LOAD_CONST               2 ('status')
                LOAD_FAST_BORROW        10 (write)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               2 ('status')
                CALL                     1
                LOAD_CONST              23 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L13)
                NOT_TAKEN
                LOAD_CONST              23 ('ok')
                JUMP_FORWARD             1 (to L14)
       L13:     LOAD_CONST              24 ('skipped')

 488   L14:     LOAD_CONST               4 ('surface')
                LOAD_FAST                3 (surface)

 489            LOAD_CONST              25 ('row')
                LOAD_GLOBAL             25 (_project_row + NULL)
                LOAD_FAST_BORROW        12 (new_row)
                CALL                     1

 490            LOAD_CONST               7 ('warnings')
                LOAD_FAST               11 (warnings)

 491            LOAD_CONST               5 ('error_code')
                LOAD_FAST_BORROW        10 (write)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               2 ('status')
                CALL                     1
                LOAD_CONST              23 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L15)
                NOT_TAKEN
                LOAD_CONST               9 (None)
                JUMP_FORWARD             1 (to L16)
       L15:     LOAD_CONST              26 ('db_unavailable')

 486   L16:     BUILD_MAP                5

 492            LOAD_FAST_BORROW         3 (surface)

 486            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L17:     RETURN_VALUE

  --   L18:     PUSH_EXC_INFO

 493            LOAD_GLOBAL             26 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       97 (to L23)
                NOT_TAKEN
                STORE_FAST              13 (e)

 494   L19:     LOAD_GLOBAL             28 (logger)
                LOAD_ATTR               31 (warning + NULL|self)

 495            LOAD_CONST              27 ('approve_cutover_first error type=')
                LOAD_GLOBAL             33 (type + NULL)
                LOAD_FAST               13 (e)
                CALL                     1
                LOAD_ATTR               34 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 494            CALL                     1
                POP_TOP

 497            LOAD_GLOBAL              7 (_final + NULL)

 498            LOAD_CONST               2 ('status')
                LOAD_CONST              24 ('skipped')

 499            LOAD_CONST               4 ('surface')
                LOAD_FAST                3 (surface)

 500            LOAD_CONST               5 ('error_code')
                LOAD_CONST              28 ('unexpected:')
                LOAD_GLOBAL             33 (type + NULL)
                LOAD_FAST               13 (e)
                CALL                     1
                LOAD_ATTR               34 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 501            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 497            BUILD_MAP                4

 502            LOAD_FAST                3 (surface)

 497            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L20:     SWAP                     2
       L21:     POP_EXCEPT
                LOAD_CONST               9 (None)
                STORE_FAST              13 (e)
                DELETE_FAST             13 (e)
                RETURN_VALUE

  --   L22:     LOAD_CONST               9 (None)
                STORE_FAST              13 (e)
                DELETE_FAST             13 (e)
                RERAISE                  1

 493   L23:     RERAISE                  0

  --   L24:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L18 [0]
  L3 to L4 -> L18 [0]
  L5 to L6 -> L18 [0]
  L7 to L8 -> L18 [0]
  L9 to L10 -> L18 [0]
  L11 to L17 -> L18 [0]
  L18 to L19 -> L24 [1] lasti
  L19 to L20 -> L22 [1] lasti
  L20 to L21 -> L24 [1] lasti
  L22 to L24 -> L24 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025F30, file "app\services\operator\cutover_approval.py", line 505>:
505           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('cutover_id')

507           LOAD_CONST               2 ('Any')

505           LOAD_CONST               3 ('actor_type')

508           LOAD_CONST               2 ('Any')

505           LOAD_CONST               4 ('actor_id')

509           LOAD_CONST               2 ('Any')

505           LOAD_CONST               5 ('return')

510           LOAD_CONST               6 ('Dict[str, Any]')

505           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object approve_cutover_second at 0x0000018C17E89970, file "app\services\operator\cutover_approval.py", line 505>:
 505            RESUME                   0

 515            LOAD_CONST               1 ('ops.cutover.approve_second')
                STORE_FAST               3 (surface)

 516            NOP

 517    L1:     LOAD_GLOBAL              1 (_safe_str + NULL)
                LOAD_FAST_BORROW         0 (cutover_id)
                LOAD_SMALL_INT          64
                CALL                     2
                STORE_FAST               4 (cid)

 518            LOAD_GLOBAL              3 (_safe_actor_type + NULL)
                LOAD_FAST_BORROW         1 (actor_type)
                CALL                     1
                STORE_FAST               5 (atype)

 519            LOAD_GLOBAL              5 (_safe_actor_id + NULL)
                LOAD_FAST_BORROW         2 (actor_id)
                CALL                     1
                STORE_FAST               6 (aid)

 520            LOAD_FAST_BORROW         4 (cid)
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L5)
                NOT_TAKEN
                LOAD_FAST_BORROW         5 (atype)
                TO_BOOL
                POP_JUMP_IF_FALSE        9 (to L5)
        L2:     NOT_TAKEN
        L3:     LOAD_FAST_BORROW         6 (aid)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L7)
        L4:     NOT_TAKEN

 521    L5:     LOAD_GLOBAL              7 (_final + NULL)

 522            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 523            LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         3 (surface)

 524            LOAD_CONST               5 ('error_code')
                LOAD_CONST               6 ('invalid_arguments')

 525            LOAD_CONST               7 ('warnings')
                LOAD_CONST               6 ('invalid_arguments')
                BUILD_LIST               1

 521            BUILD_MAP                4

 526            LOAD_FAST_BORROW         3 (surface)

 521            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
        L6:     RETURN_VALUE

 527    L7:     LOAD_GLOBAL              9 (_db_fetch_one + NULL)
                LOAD_FAST_BORROW         4 (cid)
                CALL                     1
                STORE_FAST               7 (existing)

 528            LOAD_FAST_BORROW         7 (existing)
                POP_JUMP_IF_NOT_NONE    23 (to L9)
                NOT_TAKEN

 529            LOAD_GLOBAL              7 (_final + NULL)

 530            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 531            LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         3 (surface)

 532            LOAD_CONST               5 ('error_code')
                LOAD_CONST              10 ('cutover_not_found')

 533            LOAD_CONST               7 ('warnings')
                LOAD_CONST              10 ('cutover_not_found')
                BUILD_LIST               1

 529            BUILD_MAP                4

 534            LOAD_FAST_BORROW         3 (surface)

 529            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
        L8:     RETURN_VALUE

 535    L9:     LOAD_FAST_BORROW         7 (existing)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               2 ('status')
                CALL                     1
                STORE_FAST               8 (cur_status)

 536            LOAD_FAST_BORROW         8 (cur_status)
                LOAD_GLOBAL             12 (STATUS_FIRST_APPROVED)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       26 (to L11)
                NOT_TAKEN

 537            LOAD_GLOBAL              7 (_final + NULL)

 538            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 539            LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         3 (surface)

 540            LOAD_CONST               5 ('error_code')
                LOAD_CONST              11 ('invalid_status_transition')

 541            LOAD_CONST               7 ('warnings')
                LOAD_CONST              12 ('current_status:')
                LOAD_FAST_BORROW         8 (cur_status)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 537            BUILD_MAP                4

 542            LOAD_FAST_BORROW         3 (surface)

 537            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L10:     RETURN_VALUE

 543   L11:     LOAD_FAST_BORROW         7 (existing)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              13 ('first_approved_by_actor_id')
                CALL                     1
                STORE_FAST               9 (first_actor)

 544            LOAD_FAST_BORROW         9 (first_actor)
                TO_BOOL
                POP_JUMP_IF_FALSE       68 (to L15)
       L12:     NOT_TAKEN
       L13:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 150 (first_actor, aid)
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       62 (to L15)
                NOT_TAKEN

 548            LOAD_GLOBAL             15 (_emit_event + NULL)
                LOAD_CONST              14 ('cutover.rejected')

 549            LOAD_CONST              15 ('brokerage_id')
                LOAD_FAST_BORROW         7 (existing)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              15 ('brokerage_id')
                CALL                     1

 550            LOAD_CONST              16 ('cutover_id')
                LOAD_FAST_BORROW         4 (cid)

 551            LOAD_CONST              17 ('actor_type')
                LOAD_FAST_BORROW         5 (atype)

 552            LOAD_CONST              18 ('actor_id')
                LOAD_FAST_BORROW         6 (aid)

 553            LOAD_CONST               2 ('status')
                LOAD_CONST              19 ('REJECTED_SELF_SECOND_APPROVAL')

 554            LOAD_CONST               5 ('error_code')
                LOAD_CONST              20 ('self_second_approval_forbidden')

 548            BUILD_MAP                6
                CALL                     2
                POP_TOP

 556            LOAD_GLOBAL              7 (_final + NULL)

 557            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 558            LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         3 (surface)

 559            LOAD_CONST               5 ('error_code')
                LOAD_CONST              20 ('self_second_approval_forbidden')

 560            LOAD_CONST               7 ('warnings')
                LOAD_CONST              20 ('self_second_approval_forbidden')
                BUILD_LIST               1

 556            BUILD_MAP                4

 561            LOAD_FAST_BORROW         3 (surface)

 556            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L14:     RETURN_VALUE

 563   L15:     LOAD_CONST               2 ('status')
                LOAD_GLOBAL             16 (STATUS_APPROVED)

 564            LOAD_CONST              21 ('second_approved_at')
                LOAD_GLOBAL             19 (_now_iso + NULL)
                CALL                     0

 565            LOAD_CONST              22 ('second_approved_by_actor_type')
                LOAD_FAST_BORROW         5 (atype)

 566            LOAD_CONST              23 ('second_approved_by_actor_id')
                LOAD_FAST_BORROW         6 (aid)

 562            BUILD_MAP                4
                STORE_FAST              10 (updates)

 568            LOAD_GLOBAL             21 (_db_update_status + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 74 (cid, updates)
                LOAD_CONST              24 (('cutover_id', 'updates'))
                CALL_KW                  2
                STORE_FAST              11 (write)

 569            BUILD_LIST               0
                STORE_FAST              12 (warnings)

 570            LOAD_FAST_BORROW        11 (write)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              25 ('warning')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L16)
                NOT_TAKEN

 571            LOAD_FAST_BORROW        12 (warnings)
                LOAD_ATTR               23 (append + NULL|self)
                LOAD_FAST_BORROW        11 (write)
                LOAD_CONST              25 ('warning')
                BINARY_OP               26 ([])
                CALL                     1
                POP_TOP

 572   L16:     LOAD_GLOBAL             15 (_emit_event + NULL)
                LOAD_CONST              26 ('cutover.second_approved')

 573            LOAD_CONST              15 ('brokerage_id')
                LOAD_FAST_BORROW         7 (existing)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              15 ('brokerage_id')
                CALL                     1

 574            LOAD_CONST              16 ('cutover_id')
                LOAD_FAST_BORROW         4 (cid)

 575            LOAD_CONST              17 ('actor_type')
                LOAD_FAST_BORROW         5 (atype)

 576            LOAD_CONST              18 ('actor_id')
                LOAD_FAST_BORROW         6 (aid)

 577            LOAD_CONST               2 ('status')
                LOAD_GLOBAL             16 (STATUS_APPROVED)

 578            LOAD_CONST              27 ('target_stage')
                LOAD_FAST_BORROW         7 (existing)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              27 ('target_stage')
                CALL                     1

 572            BUILD_MAP                6
                CALL                     2
                POP_TOP

 580            BUILD_MAP                0
                LOAD_FAST_BORROW         7 (existing)
                DICT_UPDATE              1
                LOAD_FAST_BORROW        10 (updates)
                DICT_UPDATE              1
                STORE_FAST              13 (new_row)

 584            LOAD_GLOBAL              7 (_final + NULL)

 585            LOAD_CONST               2 ('status')
                LOAD_FAST_BORROW        11 (write)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               2 ('status')
                CALL                     1
                LOAD_CONST              28 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L17)
                NOT_TAKEN
                LOAD_CONST              28 ('ok')
                JUMP_FORWARD             1 (to L18)
       L17:     LOAD_CONST              29 ('skipped')

 586   L18:     LOAD_CONST               4 ('surface')
                LOAD_FAST                3 (surface)

 587            LOAD_CONST              30 ('row')
                LOAD_GLOBAL             25 (_project_row + NULL)
                LOAD_FAST_BORROW        13 (new_row)
                CALL                     1

 588            LOAD_CONST               7 ('warnings')
                LOAD_FAST               12 (warnings)

 589            LOAD_CONST               5 ('error_code')
                LOAD_FAST_BORROW        11 (write)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               2 ('status')
                CALL                     1
                LOAD_CONST              28 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L19)
                NOT_TAKEN
                LOAD_CONST               9 (None)
                JUMP_FORWARD             1 (to L20)
       L19:     LOAD_CONST              31 ('db_unavailable')

 590   L20:     LOAD_CONST              32 ('action_required')
                LOAD_CONST              33 ('operator_must_invoke_mark_pilot_stage')

 584            BUILD_MAP                6

 591            LOAD_FAST_BORROW         3 (surface)

 584            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L21:     RETURN_VALUE

  --   L22:     PUSH_EXC_INFO

 592            LOAD_GLOBAL             26 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       97 (to L27)
                NOT_TAKEN
                STORE_FAST              14 (e)

 593   L23:     LOAD_GLOBAL             28 (logger)
                LOAD_ATTR               31 (warning + NULL|self)

 594            LOAD_CONST              34 ('approve_cutover_second error type=')
                LOAD_GLOBAL             33 (type + NULL)
                LOAD_FAST               14 (e)
                CALL                     1
                LOAD_ATTR               34 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 593            CALL                     1
                POP_TOP

 596            LOAD_GLOBAL              7 (_final + NULL)

 597            LOAD_CONST               2 ('status')
                LOAD_CONST              29 ('skipped')

 598            LOAD_CONST               4 ('surface')
                LOAD_FAST                3 (surface)

 599            LOAD_CONST               5 ('error_code')
                LOAD_CONST              35 ('unexpected:')
                LOAD_GLOBAL             33 (type + NULL)
                LOAD_FAST               14 (e)
                CALL                     1
                LOAD_ATTR               34 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 600            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 596            BUILD_MAP                4

 601            LOAD_FAST                3 (surface)

 596            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L24:     SWAP                     2
       L25:     POP_EXCEPT
                LOAD_CONST               9 (None)
                STORE_FAST              14 (e)
                DELETE_FAST             14 (e)
                RETURN_VALUE

  --   L26:     LOAD_CONST               9 (None)
                STORE_FAST              14 (e)
                DELETE_FAST             14 (e)
                RERAISE                  1

 592   L27:     RERAISE                  0

  --   L28:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L22 [0]
  L3 to L4 -> L22 [0]
  L5 to L6 -> L22 [0]
  L7 to L8 -> L22 [0]
  L9 to L10 -> L22 [0]
  L11 to L12 -> L22 [0]
  L13 to L14 -> L22 [0]
  L15 to L21 -> L22 [0]
  L22 to L23 -> L28 [1] lasti
  L23 to L24 -> L26 [1] lasti
  L24 to L25 -> L28 [1] lasti
  L26 to L28 -> L28 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026030, file "app\services\operator\cutover_approval.py", line 604>:
604           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('cutover_id')

606           LOAD_CONST               2 ('Any')

604           LOAD_CONST               3 ('actor_type')

607           LOAD_CONST               2 ('Any')

604           LOAD_CONST               4 ('actor_id')

608           LOAD_CONST               2 ('Any')

604           LOAD_CONST               5 ('rationale')

609           LOAD_CONST               2 ('Any')

604           LOAD_CONST               6 ('return')

610           LOAD_CONST               7 ('Dict[str, Any]')

604           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object reject_cutover at 0x0000018C177AF070, file "app\services\operator\cutover_approval.py", line 604>:
 604            RESUME                   0

 612            LOAD_CONST               1 ('ops.cutover.reject')
                STORE_FAST               4 (surface)

 613            NOP

 614    L1:     LOAD_GLOBAL              1 (_safe_str + NULL)
                LOAD_FAST_BORROW         0 (cutover_id)
                LOAD_SMALL_INT          64
                CALL                     2
                STORE_FAST               5 (cid)

 615            LOAD_GLOBAL              3 (_safe_actor_type + NULL)
                LOAD_FAST_BORROW         1 (actor_type)
                CALL                     1
                STORE_FAST               6 (atype)

 616            LOAD_GLOBAL              5 (_safe_actor_id + NULL)
                LOAD_FAST_BORROW         2 (actor_id)
                CALL                     1
                STORE_FAST               7 (aid)

 617            LOAD_GLOBAL              7 (_safe_rationale + NULL)
                LOAD_FAST_BORROW         3 (rationale)
                CALL                     1
                STORE_FAST               8 (rat)

 618            LOAD_FAST_BORROW         5 (cid)
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L5)
                NOT_TAKEN
                LOAD_FAST_BORROW         6 (atype)
                TO_BOOL
                POP_JUMP_IF_FALSE        9 (to L5)
        L2:     NOT_TAKEN
        L3:     LOAD_FAST_BORROW         7 (aid)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L7)
        L4:     NOT_TAKEN

 619    L5:     LOAD_GLOBAL              9 (_final + NULL)

 620            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 621            LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         4 (surface)

 622            LOAD_CONST               5 ('error_code')
                LOAD_CONST               6 ('invalid_arguments')

 623            LOAD_CONST               7 ('warnings')
                LOAD_CONST               6 ('invalid_arguments')
                BUILD_LIST               1

 619            BUILD_MAP                4

 624            LOAD_FAST_BORROW         4 (surface)

 619            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
        L6:     RETURN_VALUE

 625    L7:     LOAD_GLOBAL             11 (_db_fetch_one + NULL)
                LOAD_FAST_BORROW         5 (cid)
                CALL                     1
                STORE_FAST               9 (existing)

 626            LOAD_FAST_BORROW         9 (existing)
                POP_JUMP_IF_NOT_NONE    23 (to L9)
                NOT_TAKEN

 627            LOAD_GLOBAL              9 (_final + NULL)

 628            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 629            LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         4 (surface)

 630            LOAD_CONST               5 ('error_code')
                LOAD_CONST              10 ('cutover_not_found')

 631            LOAD_CONST               7 ('warnings')
                LOAD_CONST              10 ('cutover_not_found')
                BUILD_LIST               1

 627            BUILD_MAP                4

 632            LOAD_FAST_BORROW         4 (surface)

 627            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
        L8:     RETURN_VALUE

 633    L9:     LOAD_FAST_BORROW         9 (existing)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               2 ('status')
                CALL                     1
                STORE_FAST              10 (cur_status)

 634            LOAD_FAST_BORROW        10 (cur_status)
                LOAD_GLOBAL             14 (STATUS_APPROVED)
                LOAD_GLOBAL             16 (STATUS_REJECTED)
                LOAD_GLOBAL             18 (STATUS_CANCELLED)
                LOAD_GLOBAL             20 (STATUS_EXPIRED)
                BUILD_TUPLE              4
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       26 (to L11)
                NOT_TAKEN

 635            LOAD_GLOBAL              9 (_final + NULL)

 636            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 637            LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         4 (surface)

 638            LOAD_CONST               5 ('error_code')
                LOAD_CONST              11 ('invalid_status_transition')

 639            LOAD_CONST               7 ('warnings')
                LOAD_CONST              12 ('current_status:')
                LOAD_FAST_BORROW        10 (cur_status)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 635            BUILD_MAP                4

 640            LOAD_FAST_BORROW         4 (surface)

 635            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L10:     RETURN_VALUE

 641   L11:     LOAD_CONST               2 ('status')
                LOAD_GLOBAL             16 (STATUS_REJECTED)
                BUILD_MAP                1
                STORE_FAST              11 (updates)

 642            LOAD_FAST_BORROW         8 (rat)
                TO_BOOL
                POP_JUMP_IF_FALSE       67 (to L19)
       L12:     NOT_TAKEN

 643   L13:     LOAD_FAST_BORROW         9 (existing)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              13 ('metadata')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L16)
       L14:     NOT_TAKEN
       L15:     POP_TOP
                BUILD_MAP                0
       L16:     STORE_FAST              12 (existing_meta)

 644            LOAD_GLOBAL             23 (isinstance + NULL)
                LOAD_FAST_BORROW        12 (existing_meta)
                LOAD_GLOBAL             24 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       10 (to L17)
                NOT_TAKEN

 645            BUILD_MAP                0
                LOAD_FAST_BORROW        12 (existing_meta)
                DICT_UPDATE              1
                LOAD_CONST              14 ('rejection_text')
                LOAD_FAST_BORROW         8 (rat)
                BUILD_MAP                1
                DICT_UPDATE              1
                STORE_FAST              13 (merged)
                JUMP_FORWARD             4 (to L18)

 647   L17:     LOAD_CONST              14 ('rejection_text')
                LOAD_FAST_BORROW         8 (rat)
                BUILD_MAP                1
                STORE_FAST              13 (merged)

 648   L18:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 219 (merged, updates)
                LOAD_CONST              13 ('metadata')
                STORE_SUBSCR

 649   L19:     LOAD_GLOBAL             27 (_db_update_status + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 91 (cid, updates)
                LOAD_CONST              15 (('cutover_id', 'updates'))
                CALL_KW                  2
                STORE_FAST              14 (write)

 650            BUILD_LIST               0
                STORE_FAST              15 (warnings)

 651            LOAD_FAST_BORROW        14 (write)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              16 ('warning')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L20)
                NOT_TAKEN

 652            LOAD_FAST_BORROW        15 (warnings)
                LOAD_ATTR               29 (append + NULL|self)
                LOAD_FAST_BORROW        14 (write)
                LOAD_CONST              16 ('warning')
                BINARY_OP               26 ([])
                CALL                     1
                POP_TOP

 653   L20:     LOAD_GLOBAL             31 (_emit_event + NULL)
                LOAD_CONST              17 ('cutover.rejected')

 654            LOAD_CONST              18 ('brokerage_id')
                LOAD_FAST_BORROW         9 (existing)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              18 ('brokerage_id')
                CALL                     1

 655            LOAD_CONST              19 ('cutover_id')
                LOAD_FAST_BORROW         5 (cid)

 656            LOAD_CONST              20 ('actor_type')
                LOAD_FAST_BORROW         6 (atype)

 657            LOAD_CONST              21 ('actor_id')
                LOAD_FAST_BORROW         7 (aid)

 658            LOAD_CONST               2 ('status')
                LOAD_GLOBAL             16 (STATUS_REJECTED)

 653            BUILD_MAP                5
                CALL                     2
                POP_TOP

 660            BUILD_MAP                0
                LOAD_FAST_BORROW         9 (existing)
                DICT_UPDATE              1
                LOAD_FAST_BORROW        11 (updates)
                DICT_UPDATE              1
                STORE_FAST              16 (new_row)

 661            LOAD_GLOBAL              9 (_final + NULL)

 662            LOAD_CONST               2 ('status')
                LOAD_FAST_BORROW        14 (write)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               2 ('status')
                CALL                     1
                LOAD_CONST              22 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L21)
                NOT_TAKEN
                LOAD_CONST              22 ('ok')
                JUMP_FORWARD             1 (to L22)
       L21:     LOAD_CONST              23 ('skipped')

 663   L22:     LOAD_CONST               4 ('surface')
                LOAD_FAST                4 (surface)

 664            LOAD_CONST              24 ('row')
                LOAD_GLOBAL             33 (_project_row + NULL)
                LOAD_FAST_BORROW        16 (new_row)
                CALL                     1

 665            LOAD_CONST               7 ('warnings')
                LOAD_FAST               15 (warnings)

 666            LOAD_CONST               5 ('error_code')
                LOAD_FAST_BORROW        14 (write)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               2 ('status')
                CALL                     1
                LOAD_CONST              22 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L23)
                NOT_TAKEN
                LOAD_CONST               9 (None)
                JUMP_FORWARD             1 (to L24)
       L23:     LOAD_CONST              25 ('db_unavailable')

 661   L24:     BUILD_MAP                5

 667            LOAD_FAST_BORROW         4 (surface)

 661            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L25:     RETURN_VALUE

  --   L26:     PUSH_EXC_INFO

 668            LOAD_GLOBAL             34 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       97 (to L31)
                NOT_TAKEN
                STORE_FAST              17 (e)

 669   L27:     LOAD_GLOBAL             36 (logger)
                LOAD_ATTR               39 (warning + NULL|self)

 670            LOAD_CONST              26 ('reject_cutover error type=')
                LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST               17 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 669            CALL                     1
                POP_TOP

 672            LOAD_GLOBAL              9 (_final + NULL)

 673            LOAD_CONST               2 ('status')
                LOAD_CONST              23 ('skipped')

 674            LOAD_CONST               4 ('surface')
                LOAD_FAST                4 (surface)

 675            LOAD_CONST               5 ('error_code')
                LOAD_CONST              27 ('unexpected:')
                LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST               17 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 676            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 672            BUILD_MAP                4

 677            LOAD_FAST                4 (surface)

 672            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L28:     SWAP                     2
       L29:     POP_EXCEPT
                LOAD_CONST               9 (None)
                STORE_FAST              17 (e)
                DELETE_FAST             17 (e)
                RETURN_VALUE

  --   L30:     LOAD_CONST               9 (None)
                STORE_FAST              17 (e)
                DELETE_FAST             17 (e)
                RERAISE                  1

 668   L31:     RERAISE                  0

  --   L32:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L26 [0]
  L3 to L4 -> L26 [0]
  L5 to L6 -> L26 [0]
  L7 to L8 -> L26 [0]
  L9 to L10 -> L26 [0]
  L11 to L12 -> L26 [0]
  L13 to L14 -> L26 [0]
  L15 to L25 -> L26 [0]
  L26 to L27 -> L32 [1] lasti
  L27 to L28 -> L30 [1] lasti
  L28 to L29 -> L32 [1] lasti
  L30 to L32 -> L32 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025230, file "app\services\operator\cutover_approval.py", line 680>:
680           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('cutover_id')

682           LOAD_CONST               2 ('Any')

680           LOAD_CONST               3 ('actor_type')

683           LOAD_CONST               2 ('Any')

680           LOAD_CONST               4 ('actor_id')

684           LOAD_CONST               2 ('Any')

680           LOAD_CONST               5 ('return')

685           LOAD_CONST               6 ('Dict[str, Any]')

680           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object cancel_cutover at 0x0000018C17E7E2C0, file "app\services\operator\cutover_approval.py", line 680>:
 680            RESUME                   0

 688            LOAD_CONST               1 ('ops.cutover.cancel')
                STORE_FAST               3 (surface)

 689            NOP

 690    L1:     LOAD_GLOBAL              1 (_safe_str + NULL)
                LOAD_FAST_BORROW         0 (cutover_id)
                LOAD_SMALL_INT          64
                CALL                     2
                STORE_FAST               4 (cid)

 691            LOAD_GLOBAL              3 (_safe_actor_type + NULL)
                LOAD_FAST_BORROW         1 (actor_type)
                CALL                     1
                STORE_FAST               5 (atype)

 692            LOAD_GLOBAL              5 (_safe_actor_id + NULL)
                LOAD_FAST_BORROW         2 (actor_id)
                CALL                     1
                STORE_FAST               6 (aid)

 693            LOAD_FAST_BORROW         4 (cid)
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L5)
                NOT_TAKEN
                LOAD_FAST_BORROW         5 (atype)
                TO_BOOL
                POP_JUMP_IF_FALSE        9 (to L5)
        L2:     NOT_TAKEN
        L3:     LOAD_FAST_BORROW         6 (aid)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L7)
        L4:     NOT_TAKEN

 694    L5:     LOAD_GLOBAL              7 (_final + NULL)

 695            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 696            LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         3 (surface)

 697            LOAD_CONST               5 ('error_code')
                LOAD_CONST               6 ('invalid_arguments')

 698            LOAD_CONST               7 ('warnings')
                LOAD_CONST               6 ('invalid_arguments')
                BUILD_LIST               1

 694            BUILD_MAP                4

 699            LOAD_FAST_BORROW         3 (surface)

 694            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
        L6:     RETURN_VALUE

 700    L7:     LOAD_GLOBAL              9 (_db_fetch_one + NULL)
                LOAD_FAST_BORROW         4 (cid)
                CALL                     1
                STORE_FAST               7 (existing)

 701            LOAD_FAST_BORROW         7 (existing)
                POP_JUMP_IF_NOT_NONE    23 (to L9)
                NOT_TAKEN

 702            LOAD_GLOBAL              7 (_final + NULL)

 703            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 704            LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         3 (surface)

 705            LOAD_CONST               5 ('error_code')
                LOAD_CONST              10 ('cutover_not_found')

 706            LOAD_CONST               7 ('warnings')
                LOAD_CONST              10 ('cutover_not_found')
                BUILD_LIST               1

 702            BUILD_MAP                4

 707            LOAD_FAST_BORROW         3 (surface)

 702            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
        L8:     RETURN_VALUE

 708    L9:     LOAD_FAST_BORROW         7 (existing)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               2 ('status')
                CALL                     1
                STORE_FAST               8 (cur_status)

 709            LOAD_FAST_BORROW         8 (cur_status)
                LOAD_GLOBAL             12 (STATUS_APPROVED)
                LOAD_GLOBAL             14 (STATUS_REJECTED)
                LOAD_GLOBAL             16 (STATUS_CANCELLED)
                LOAD_GLOBAL             18 (STATUS_EXPIRED)
                BUILD_TUPLE              4
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       26 (to L11)
                NOT_TAKEN

 710            LOAD_GLOBAL              7 (_final + NULL)

 711            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 712            LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         3 (surface)

 713            LOAD_CONST               5 ('error_code')
                LOAD_CONST              11 ('invalid_status_transition')

 714            LOAD_CONST               7 ('warnings')
                LOAD_CONST              12 ('current_status:')
                LOAD_FAST_BORROW         8 (cur_status)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 710            BUILD_MAP                4

 715            LOAD_FAST_BORROW         3 (surface)

 710            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L10:     RETURN_VALUE

 716   L11:     LOAD_CONST               2 ('status')
                LOAD_GLOBAL             16 (STATUS_CANCELLED)
                BUILD_MAP                1
                STORE_FAST               9 (updates)

 717            LOAD_GLOBAL             21 (_db_update_status + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 73 (cid, updates)
                LOAD_CONST              13 (('cutover_id', 'updates'))
                CALL_KW                  2
                STORE_FAST              10 (write)

 718            BUILD_LIST               0
                STORE_FAST              11 (warnings)

 719            LOAD_FAST_BORROW        10 (write)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              14 ('warning')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L12)
                NOT_TAKEN

 720            LOAD_FAST_BORROW        11 (warnings)
                LOAD_ATTR               23 (append + NULL|self)
                LOAD_FAST_BORROW        10 (write)
                LOAD_CONST              14 ('warning')
                BINARY_OP               26 ([])
                CALL                     1
                POP_TOP

 721   L12:     BUILD_MAP                0
                LOAD_FAST_BORROW         7 (existing)
                DICT_UPDATE              1
                LOAD_FAST_BORROW         9 (updates)
                DICT_UPDATE              1
                STORE_FAST              12 (new_row)

 722            LOAD_GLOBAL              7 (_final + NULL)

 723            LOAD_CONST               2 ('status')
                LOAD_FAST_BORROW        10 (write)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               2 ('status')
                CALL                     1
                LOAD_CONST              15 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L13)
                NOT_TAKEN
                LOAD_CONST              15 ('ok')
                JUMP_FORWARD             1 (to L14)
       L13:     LOAD_CONST              16 ('skipped')

 724   L14:     LOAD_CONST               4 ('surface')
                LOAD_FAST                3 (surface)

 725            LOAD_CONST              17 ('row')
                LOAD_GLOBAL             25 (_project_row + NULL)
                LOAD_FAST_BORROW        12 (new_row)
                CALL                     1

 726            LOAD_CONST               7 ('warnings')
                LOAD_FAST               11 (warnings)

 727            LOAD_CONST               5 ('error_code')
                LOAD_FAST_BORROW        10 (write)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               2 ('status')
                CALL                     1
                LOAD_CONST              15 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L15)
                NOT_TAKEN
                LOAD_CONST               9 (None)
                JUMP_FORWARD             1 (to L16)
       L15:     LOAD_CONST              18 ('db_unavailable')

 722   L16:     BUILD_MAP                5

 728            LOAD_FAST_BORROW         3 (surface)

 722            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L17:     RETURN_VALUE

  --   L18:     PUSH_EXC_INFO

 729            LOAD_GLOBAL             26 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       97 (to L23)
                NOT_TAKEN
                STORE_FAST              13 (e)

 730   L19:     LOAD_GLOBAL             28 (logger)
                LOAD_ATTR               31 (warning + NULL|self)

 731            LOAD_CONST              19 ('cancel_cutover error type=')
                LOAD_GLOBAL             33 (type + NULL)
                LOAD_FAST               13 (e)
                CALL                     1
                LOAD_ATTR               34 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 730            CALL                     1
                POP_TOP

 733            LOAD_GLOBAL              7 (_final + NULL)

 734            LOAD_CONST               2 ('status')
                LOAD_CONST              16 ('skipped')

 735            LOAD_CONST               4 ('surface')
                LOAD_FAST                3 (surface)

 736            LOAD_CONST               5 ('error_code')
                LOAD_CONST              20 ('unexpected:')
                LOAD_GLOBAL             33 (type + NULL)
                LOAD_FAST               13 (e)
                CALL                     1
                LOAD_ATTR               34 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 737            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 733            BUILD_MAP                4

 738            LOAD_FAST                3 (surface)

 733            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L20:     SWAP                     2
       L21:     POP_EXCEPT
                LOAD_CONST               9 (None)
                STORE_FAST              13 (e)
                DELETE_FAST             13 (e)
                RETURN_VALUE

  --   L22:     LOAD_CONST               9 (None)
                STORE_FAST              13 (e)
                DELETE_FAST             13 (e)
                RERAISE                  1

 729   L23:     RERAISE                  0

  --   L24:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L18 [0]
  L3 to L4 -> L18 [0]
  L5 to L6 -> L18 [0]
  L7 to L8 -> L18 [0]
  L9 to L10 -> L18 [0]
  L11 to L17 -> L18 [0]
  L18 to L19 -> L24 [1] lasti
  L19 to L20 -> L22 [1] lasti
  L20 to L21 -> L24 [1] lasti
  L22 to L24 -> L24 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025930, file "app\services\operator\cutover_approval.py", line 741>:
741           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

743           LOAD_CONST               2 ('Any')

741           LOAD_CONST               3 ('status')

744           LOAD_CONST               2 ('Any')

741           LOAD_CONST               4 ('limit')

745           LOAD_CONST               2 ('Any')

741           LOAD_CONST               5 ('return')

746           LOAD_CONST               6 ('Dict[str, Any]')

741           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object cutover_status_report at 0x0000018C17E8B240, file "app\services\operator\cutover_approval.py", line 741>:
 741            RESUME                   0

 750            LOAD_CONST               1 ('ops.cutover.list')
                STORE_FAST               3 (surface)

 751            NOP

 752    L1:     LOAD_FAST_BORROW         0 (brokerage_id)
                POP_JUMP_IF_NONE        12 (to L2)
                NOT_TAKEN
                LOAD_GLOBAL              1 (_safe_brokerage + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               2 (None)
        L3:     STORE_FAST               4 (bid)

 753            LOAD_CONST               2 (None)
                STORE_FAST               5 (stat)

 754            LOAD_FAST_BORROW         1 (status)
                POP_JUMP_IF_NONE        62 (to L4)
                NOT_TAKEN

 755            LOAD_GLOBAL              3 (_safe_str + NULL)
                LOAD_FAST_BORROW         1 (status)
                LOAD_SMALL_INT          32
                CALL                     2
                STORE_FAST               6 (cand)

 756            LOAD_FAST_BORROW         6 (cand)
                TO_BOOL
                POP_JUMP_IF_FALSE       42 (to L4)
                NOT_TAKEN
                LOAD_FAST_BORROW         6 (cand)
                LOAD_ATTR                5 (upper + NULL|self)
                CALL                     0
                LOAD_GLOBAL              6 (_VALID_STATUSES)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       17 (to L4)
                NOT_TAKEN

 757            LOAD_FAST_BORROW         6 (cand)
                LOAD_ATTR                5 (upper + NULL|self)
                CALL                     0
                STORE_FAST               5 (stat)

 758    L4:     LOAD_GLOBAL              9 (_safe_int + NULL)
                LOAD_FAST_BORROW         2 (limit)
                LOAD_SMALL_INT           1
                LOAD_SMALL_INT         200
                LOAD_SMALL_INT          50
                LOAD_CONST               3 (('lo', 'hi', 'default'))
                CALL_KW                  4
                STORE_FAST               7 (cap)

 759            LOAD_GLOBAL             11 (_get_db + NULL)
                CALL                     0
                STORE_FAST               8 (db)

 760            LOAD_FAST_BORROW         8 (db)
                POP_JUMP_IF_NOT_NONE    27 (to L6)
                NOT_TAKEN

 761            LOAD_GLOBAL             13 (_final + NULL)

 762            LOAD_CONST               4 ('status')
                LOAD_CONST               5 ('skipped')

 763            LOAD_CONST               6 ('surface')
                LOAD_FAST_BORROW         3 (surface)

 764            LOAD_CONST               7 ('rows')
                BUILD_LIST               0

 765            LOAD_CONST               8 ('count')
                LOAD_SMALL_INT           0

 766            LOAD_CONST               9 ('warnings')
                LOAD_CONST              10 ('db_unavailable')
                BUILD_LIST               1

 767            LOAD_CONST              11 ('error_code')
                LOAD_CONST              10 ('db_unavailable')

 761            BUILD_MAP                6

 768            LOAD_FAST_BORROW         3 (surface)

 761            LOAD_CONST              12 (('surface',))
                CALL_KW                  2
        L5:     RETURN_VALUE

 769    L6:     NOP

 770    L7:     LOAD_FAST_BORROW         8 (db)
                LOAD_ATTR               15 (table + NULL|self)
                LOAD_GLOBAL             16 (_TABLE_NAME)
                CALL                     1
                LOAD_ATTR               19 (select + NULL|self)
                LOAD_CONST              13 ('*')
                CALL                     1
                STORE_FAST               9 (query)

 771            LOAD_FAST_BORROW         4 (bid)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L10)
        L8:     NOT_TAKEN

 772    L9:     LOAD_FAST_BORROW         9 (query)
                LOAD_ATTR               21 (eq + NULL|self)
                LOAD_CONST              14 ('brokerage_id')
                LOAD_FAST_BORROW         4 (bid)
                CALL                     2
                STORE_FAST               9 (query)

 773   L10:     LOAD_FAST_BORROW         5 (stat)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L13)
       L11:     NOT_TAKEN

 774   L12:     LOAD_FAST_BORROW         9 (query)
                LOAD_ATTR               21 (eq + NULL|self)
                LOAD_CONST               4 ('status')
                LOAD_FAST_BORROW         5 (stat)
                CALL                     2
                STORE_FAST               9 (query)

 775   L13:     LOAD_FAST_BORROW         9 (query)
                LOAD_ATTR               23 (order + NULL|self)
                LOAD_CONST              15 ('requested_at')
                LOAD_CONST              16 (True)
                LOAD_CONST              17 (('desc',))
                CALL_KW                  2
                LOAD_ATTR               25 (limit + NULL|self)
                LOAD_FAST_BORROW         7 (cap)
                CALL                     1
                STORE_FAST               9 (query)

 776            LOAD_FAST_BORROW         9 (query)
                LOAD_ATTR               27 (execute + NULL|self)
                CALL                     0
                STORE_FAST              10 (resp)

 789   L14:     LOAD_GLOBAL             39 (getattr + NULL)
                LOAD_FAST               10 (resp)
                LOAD_CONST              21 ('data')
                LOAD_CONST               2 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L17)
       L15:     NOT_TAKEN
       L16:     POP_TOP
                BUILD_LIST               0
       L17:     STORE_FAST              12 (data)

 790            BUILD_LIST               0
                STORE_FAST              13 (rows)

 791            LOAD_FAST               12 (data)
                LOAD_CONST               2 (None)
                LOAD_FAST                7 (cap)
                BINARY_SLICE
                GET_ITER
       L18:     FOR_ITER                53 (to L21)
                STORE_FAST              14 (r)

 792            LOAD_GLOBAL             41 (isinstance + NULL)
                LOAD_FAST               14 (r)
                LOAD_GLOBAL             42 (dict)
                CALL                     2
                TO_BOOL
       L19:     POP_JUMP_IF_TRUE         3 (to L20)
                NOT_TAKEN
                JUMP_BACKWARD           27 (to L18)

 793   L20:     LOAD_FAST               13 (rows)
                LOAD_ATTR               45 (append + NULL|self)
                LOAD_GLOBAL             47 (_project_row + NULL)
                LOAD_FAST               14 (r)
                CALL                     1
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           55 (to L18)

 791   L21:     END_FOR
                POP_ITER

 794            LOAD_GLOBAL             13 (_final + NULL)

 795            LOAD_CONST               4 ('status')
                LOAD_CONST              22 ('ok')

 796            LOAD_CONST               6 ('surface')
                LOAD_FAST                3 (surface)

 797            LOAD_CONST               7 ('rows')
                LOAD_FAST               13 (rows)

 798            LOAD_CONST               8 ('count')
                LOAD_GLOBAL             49 (len + NULL)
                LOAD_FAST               13 (rows)
                CALL                     1

 799            LOAD_CONST               9 ('warnings')
                BUILD_LIST               0

 800            LOAD_CONST              11 ('error_code')
                LOAD_CONST               2 (None)

 794            BUILD_MAP                6

 801            LOAD_FAST                3 (surface)

 794            LOAD_CONST              12 (('surface',))
                CALL_KW                  2
       L22:     RETURN_VALUE

  --   L23:     PUSH_EXC_INFO

 777            LOAD_GLOBAL             28 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      102 (to L29)
                NOT_TAKEN
                STORE_FAST              11 (e)

 778   L24:     LOAD_GLOBAL             30 (logger)
                LOAD_ATTR               33 (warning + NULL|self)

 779            LOAD_CONST              18 ('cutover_status_report query error type=')
                LOAD_GLOBAL             35 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               36 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 778            CALL                     1
                POP_TOP

 781            LOAD_GLOBAL             13 (_final + NULL)

 782            LOAD_CONST               4 ('status')
                LOAD_CONST               5 ('skipped')

 783            LOAD_CONST               6 ('surface')
                LOAD_FAST                3 (surface)

 784            LOAD_CONST               7 ('rows')
                BUILD_LIST               0

 785            LOAD_CONST               8 ('count')
                LOAD_SMALL_INT           0

 786            LOAD_CONST               9 ('warnings')
                LOAD_CONST              19 ('db_query_failed:')
                LOAD_GLOBAL             35 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               36 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 787            LOAD_CONST              11 ('error_code')
                LOAD_CONST              20 ('db_query_failed')

 781            BUILD_MAP                6

 788            LOAD_FAST                3 (surface)

 781            LOAD_CONST              12 (('surface',))
                CALL_KW                  2
       L25:     SWAP                     2
       L26:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
       L27:     RETURN_VALUE

  --   L28:     LOAD_CONST               2 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RERAISE                  1

 777   L29:     RERAISE                  0

  --   L30:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L31:     PUSH_EXC_INFO

 802            LOAD_GLOBAL             28 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      101 (to L36)
                NOT_TAKEN
                STORE_FAST              11 (e)

 803   L32:     LOAD_GLOBAL             30 (logger)
                LOAD_ATTR               33 (warning + NULL|self)

 804            LOAD_CONST              23 ('cutover_status_report error type=')
                LOAD_GLOBAL             35 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               36 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 803            CALL                     1
                POP_TOP

 806            LOAD_GLOBAL             13 (_final + NULL)

 807            LOAD_CONST               4 ('status')
                LOAD_CONST               5 ('skipped')

 808            LOAD_CONST               6 ('surface')
                LOAD_FAST                3 (surface)

 809            LOAD_CONST               7 ('rows')
                BUILD_LIST               0

 810            LOAD_CONST               8 ('count')
                LOAD_SMALL_INT           0

 811            LOAD_CONST              11 ('error_code')
                LOAD_CONST              24 ('unexpected:')
                LOAD_GLOBAL             35 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               36 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 812            LOAD_CONST               9 ('warnings')
                BUILD_LIST               0

 806            BUILD_MAP                6

 813            LOAD_FAST                3 (surface)

 806            LOAD_CONST              12 (('surface',))
                CALL_KW                  2
       L33:     SWAP                     2
       L34:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RETURN_VALUE

  --   L35:     LOAD_CONST               2 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RERAISE                  1

 802   L36:     RERAISE                  0

  --   L37:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L5 -> L31 [0]
  L7 to L8 -> L23 [0]
  L9 to L11 -> L23 [0]
  L12 to L14 -> L23 [0]
  L14 to L15 -> L31 [0]
  L16 to L19 -> L31 [0]
  L20 to L22 -> L31 [0]
  L23 to L24 -> L30 [1] lasti
  L24 to L25 -> L28 [1] lasti
  L25 to L26 -> L30 [1] lasti
  L26 to L27 -> L31 [0]
  L28 to L30 -> L30 [1] lasti
  L30 to L31 -> L31 [0]
  L31 to L32 -> L37 [1] lasti
  L32 to L33 -> L35 [1] lasti
  L33 to L34 -> L37 [1] lasti
  L35 to L37 -> L37 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025630, file "app\services\operator\cutover_approval.py", line 816>:
816           RESUME                   0
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

Disassembly of <code object _safe_int at 0x0000018C18039070, file "app\services\operator\cutover_approval.py", line 816>:
 816           RESUME                   0

 817           NOP

 818   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               4 (v)

 821   L2:     LOAD_FAST_LOAD_FAST     65 (v, lo)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 822           LOAD_FAST                1 (lo)
               RETURN_VALUE

 823   L3:     LOAD_FAST_LOAD_FAST     66 (v, hi)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN

 824           LOAD_FAST                2 (hi)
               RETURN_VALUE

 825   L4:     LOAD_FAST                4 (v)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 819           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L7)
               NOT_TAKEN
               POP_TOP

 820           LOAD_FAST                3 (default)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

 819   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti
```
