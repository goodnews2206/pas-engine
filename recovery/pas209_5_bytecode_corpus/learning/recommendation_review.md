# learning/recommendation_review

- **pyc:** `app\services\learning\__pycache__\recommendation_review.cpython-314.pyc`
- **expected source path (absent):** `app\services\learning/recommendation_review.py`
- **co_filename (from bytecode):** `app/services/learning/recommendation_review.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** learning

## Module docstring

```
PAS180 — Operator learning recommendation review service.

Wraps the v28 `pas_learning_recommendations` table with a
*strict* operator-driven transition table:

    CANDIDATE                 → APPROVED_FOR_MANUAL_TEST
    CANDIDATE                 → REJECTED
    CANDIDATE                 → EXPIRED
    APPROVED_FOR_MANUAL_TEST  → EXPIRED

Any other transition (e.g. APPROVED_FOR_MANUAL_TEST → REJECTED,
or a walk-back to CANDIDATE) is rejected at the service layer
with a structural ``error_code``. PAS180 never exposes a
helper that bypasses the transition table; PAS180 never
mutates any live PAS behaviour.

Doctrine:

* **Operator-only.** Every mutation helper accepts a closed
  ``actor_type`` (OPERATOR / ADMIN) and a bounded ``actor_id``.
  Tenant callers are NEVER exposed to mutation helpers via
  routes; the tenant route module imports ONLY the read helpers.
* **Append-only audit.** Every successful transition writes a
  bounded structural row to ``pas_operator_actions_log`` via
  ``app.services.operator.audit_service.log_operator_action``.
  No PII, no rationale_text, no raw payload.
* **No live behaviour mutation.** This module NEVER imports
  the outbound FSM, Memory Review, booking, slack core,
  worker, or any other live PAS subsystem. The readiness gate
  enforces the import bans structurally.
* **NEVER raises.** All failures collapse to structural
  envelopes.
* **No LLM calls.** Deterministic structural transitions only.
* **DB unavailable → ``status="skipped"``.**

Public surface:

  * ``ALLOWED_REVIEW_STATUSES``                          — closed enum.
  * ``ALLOWED_TRANSITIONS``                              — closed map.
  * ``list_learning_recommendations(...)``               — bounded read.
  * ``get_learning_recommendation(...)``                 — single read.
  * ``review_learning_recommendation(...)``              — generic transition.
  * ``approve_recommendation_for_manual_test(...)``      — wrapper.
  * ``reject_learning_recommendation(...)``              — wrapper.
  * ``expire_learning_recommendation(...)``              — wrapper.
  * ``recommendation_review_history(...)``               — paginated audit-log read.
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `Tuple`, `__future__`, `annotations`, `app.db.supabase_client`, `app.services.operator.audit_service`, `datetime`, `get_supabase`, `log_operator_action`, `logging`, `operator_action_history`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_audit_review_action`, `_bound_actor_id`, `_bound_brokerage_id`, `_bound_recommendation_id`, `_clamp_limit`, `_get_db_safe`, `_now_iso`, `_project_row`, `_safe_envelope`, `_validate_reason_token`, `_validate_transition`, `approve_recommendation_for_manual_test`, `expire_learning_recommendation`, `get_learning_recommendation`, `list_learning_recommendations`, `recommendation_review_history`, `reject_learning_recommendation`, `review_learning_recommendation`

## Env-key candidates

`ALLOWED_ACTOR_TYPES`, `ALLOWED_REVIEW_REASON_TOKENS`, `ALLOWED_REVIEW_STATUSES`, `ALLOWED_TRANSITIONS`, `APPROVED_FOR_MANUAL_TEST`, `CANDIDATE`, `EXPIRED`, `FAILED`, `REJECTED`, `SUCCESS`

## String constants (redacted where noted)

- '\nPAS180 — Operator learning recommendation review service.\n\nWraps the v28 `pas_learning_recommendations` table with a\n*strict* operator-driven transition table:\n\n    CANDIDATE                 → APPROVED_FOR_MANUAL_TEST\n    CANDIDATE                 → REJECTED\n    CANDIDATE                 → EXPIRED\n    APPROVED_FOR_MANUAL_TEST  → EXPIRED\n\nAny other transition (e.g. APPROVED_FOR_MANUAL_TEST → REJECTED,\nor a walk-back to CANDIDATE) is rejected at the service layer\nwith a structural ``error_code``. PAS180 never exposes a\nhelper that bypasses the transition table; PAS180 never\nmutates any live PAS behaviour.\n\nDoctrine:\n\n* **Operator-only.** Every mutation helper accepts a closed\n  ``actor_type`` (OPERATOR / ADMIN) and a bounded ``actor_id``.\n  Tenant callers are NEVER exposed to mutation helpers via\n  routes; the tenant route module imports ONLY the read helpers.\n* **Append-only audit.** Every successful transition writes a\n  bounded structural row to ``pas_operator_actions_log`` via\n  ``app.services.operator.audit_service.log_operator_action``.\n  No PII, no rationale_text, no raw payload.\n* **No live behaviour mutation.** This module NEVER imports\n  the outbound FSM, Memory Review, booking, slack core,\n  worker, or any other live PAS subsystem. The readiness gate\n  enforces the import bans structurally.\n* **NEVER raises.** All failures collapse to structural\n  envelopes.\n* **No LLM calls.** Deterministic structural transitions only.\n* **DB unavailable → ``status="skipped"``.**\n\nPublic surface:\n\n  * ``ALLOWED_REVIEW_STATUSES``                          — closed enum.\n  * ``ALLOWED_TRANSITIONS``                              — closed map.\n  * ``list_learning_recommendations(...)``               — bounded read.\n  * ``get_learning_recommendation(...)``                 — single read.\n  * ``review_learning_recommendation(...)``              — generic transition.\n  * ``approve_recommendation_for_manual_test(...)``      — wrapper.\n  * ``reject_learning_recommendation(...)``              — wrapper.\n  * ``expire_learning_recommendation(...)``              — wrapper.\n  * ``recommendation_review_history(...)``               — paginated audit-log read.\n'
- 'pas.learning.recommendation_review'
- 'pas_learning_recommendations'
- 'CANDIDATE'
- 'APPROVED_FOR_MANUAL_TEST'
- 'Tuple[str, ...]'
- 'ALLOWED_REVIEW_STATUSES'
- 'ALLOWED_ACTOR_TYPES'
- 'Dict[str, Tuple[str, ...]]'
- 'ALLOWED_TRANSITIONS'
- 'ALLOWED_REVIEW_REASON_TOKENS'
- 🔒 '<REDACTED:high-entropy blob, len=64>'
- 'recommendation_id'
- 'brokerage_id'
- 'status'
- 'record'
- 'transition'
- 'audit_row'
- 'warnings'
- 'error_code'
- 'limit'
- 'warning_count'
- 'actor_id'
- 'reason_token'
- 'return'
- 'str'
- 'seconds'
- 'recommendation_review db client unavailable type='
- 'value'
- 'Any'
- 'Optional[str]'
- 'int'
- 'row'
- 'Optional[Dict[str, Any]]'
- 'Optional[List[str]]'
- 'Dict[str, Any]'
- 'from_status'
- 'to_status'
- 'Returns None if the transition is permitted, else a\nstructural ``error_code``.'
- 'invalid_target_status'
- 'walk_back_to_candidate_forbidden'
- 'missing_current_status'
- 'invalid_transition'
- 'Returns the bounded token, or None on rejection.'
- 'Bounded list of recommendations. NEVER raises. NEVER\nreturns PII. Operator-side surface; tenant route uses the\nPAS180 tenant projection on top of this.'
- 'failed'
- 'rows'
- 'count'
- 'invalid_status'
- 'skipped'
- 'learning_recommendations_store_unavailable'
- 'created_at'
- 'data'
- 'list_learning_recommendations read error type='
- 'db_read_failed:'
- 'Single read. Optionally scoped to a brokerage for the\ntenant-side route. NEVER raises.'
- 'invalid_recommendation_id'
- 'get_learning_recommendation read error type='
- 'recommendation_not_found_or_cross_brokerage'
- 'actor_type'
- "Best-effort append-only audit row via PAS174's\n``log_operator_action``. NEVER raises."
- 'review_learning_recommendation'
- 'SUCCESS'
- 'FAILED'
- 'learning_recommendation'
- 'event'
- 'learning.recommendation.reviewed'
- 'target_status'
- '_audit_review_action error type='
- 'Generic recommendation transition. Validates the closed\ntransition table; refuses walk-backs; writes an audit row.\nNEVER raises.'
- 'invalid_actor_type'
- 'invalid_actor_id'
- 'invalid_reason_token'
- 'review_learning_recommendation lookup error type='
- 'recommendation_not_found'
- 'recommendation_corrupt'
- 'from'
- 'reviewed_at'
- 'reviewed_by_actor_type'
- 'reviewed_by_actor_id'
- 'review_learning_recommendation update error type='
- 'db_write_failed'
- 'db_write_failed:'
- 'policy_refused_or_no_rows'
- 'REJECTED'
- 'EXPIRED'
- 'Paginated read of the PAS174 audit log scoped to\n``review_learning_recommendation`` actions. NEVER raises.\nNEVER returns PII.'
- 'recommendation_review_history error type='
- 'unexpected:'
- 'action'
- 'target_type'
- 'target_id'

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS180 — Operator learning recommendation review service.\n\nWraps the v28 `pas_learning_recommendations` table with a\n*strict* operator-driven transition table:\n\n    CANDIDATE                 → APPROVED_FOR_MANUAL_TEST\n    CANDIDATE                 → REJECTED\n    CANDIDATE                 → EXPIRED\n    APPROVED_FOR_MANUAL_TEST  → EXPIRED\n\nAny other transition (e.g. APPROVED_FOR_MANUAL_TEST → REJECTED,\nor a walk-back to CANDIDATE) is rejected at the service layer\nwith a structural ``error_code``. PAS180 never exposes a\nhelper that bypasses the transition table; PAS180 never\nmutates any live PAS behaviour.\n\nDoctrine:\n\n* **Operator-only.** Every mutation helper accepts a closed\n  ``actor_type`` (OPERATOR / ADMIN) and a bounded ``actor_id``.\n  Tenant callers are NEVER exposed to mutation helpers via\n  routes; the tenant route module imports ONLY the read helpers.\n* **Append-only audit.** Every successful transition writes a\n  bounded structural row to ``pas_operator_actions_log`` via\n  ``app.services.operator.audit_service.log_operator_action``.\n  No PII, no rationale_text, no raw payload.\n* **No live behaviour mutation.** This module NEVER imports\n  the outbound FSM, Memory Review, booking, slack core,\n  worker, or any other live PAS subsystem. The readiness gate\n  enforces the import bans structurally.\n* **NEVER raises.** All failures collapse to structural\n  envelopes.\n* **No LLM calls.** Deterministic structural transitions only.\n* **DB unavailable → ``status="skipped"``.**\n\nPublic surface:\n\n  * ``ALLOWED_REVIEW_STATUSES``                          — closed enum.\n  * ``ALLOWED_TRANSITIONS``                              — closed map.\n  * ``list_learning_recommendations(...)``               — bounded read.\n  * ``get_learning_recommendation(...)``                 — single read.\n  * ``review_learning_recommendation(...)``              — generic transition.\n  * ``approve_recommendation_for_manual_test(...)``      — wrapper.\n  * ``reject_learning_recommendation(...)``              — wrapper.\n  * ``expire_learning_recommendation(...)``              — wrapper.\n  * ``recommendation_review_history(...)``               — paginated audit-log read.\n')
               STORE_NAME               1 (__doc__)

  50           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  52           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (logging)
               STORE_NAME               4 (logging)

  53           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              5 (datetime)
               IMPORT_FROM              5 (datetime)
               STORE_NAME               5 (datetime)
               IMPORT_FROM              6 (timezone)
               STORE_NAME               6 (timezone)
               POP_TOP

  54           LOAD_SMALL_INT           0
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

  57           LOAD_NAME                4 (logging)
               LOAD_ATTR               26 (getLogger)
               PUSH_NULL
               LOAD_CONST               5 ('pas.learning.recommendation_review')
               CALL                     1
               STORE_NAME              14 (logger)

  60           LOAD_CONST               6 ('pas_learning_recommendations')
               STORE_NAME              15 (_TABLE)

  64           LOAD_CONST              64 (('CANDIDATE', 'APPROVED_FOR_MANUAL_TEST', 'REJECTED', 'EXPIRED'))
               STORE_NAME              16 (ALLOWED_REVIEW_STATUSES)
               LOAD_CONST               9 ('Tuple[str, ...]')
               LOAD_NAME               17 (__annotations__)
               LOAD_CONST              10 ('ALLOWED_REVIEW_STATUSES')
               STORE_SUBSCR

  72           LOAD_CONST              65 (('OPERATOR', 'ADMIN'))
               STORE_NAME              18 (ALLOWED_ACTOR_TYPES)
               LOAD_CONST               9 ('Tuple[str, ...]')
               LOAD_NAME               17 (__annotations__)
               LOAD_CONST              11 ('ALLOWED_ACTOR_TYPES')
               STORE_SUBSCR

  78           LOAD_CONST               7 ('CANDIDATE')
               LOAD_CONST              66 (('APPROVED_FOR_MANUAL_TEST', 'REJECTED', 'EXPIRED'))

  83           LOAD_CONST               8 ('APPROVED_FOR_MANUAL_TEST')
               LOAD_CONST              67 (('EXPIRED',))

  77           BUILD_MAP                2
               STORE_NAME              19 (ALLOWED_TRANSITIONS)
               LOAD_CONST              12 ('Dict[str, Tuple[str, ...]]')
               LOAD_NAME               17 (__annotations__)
               LOAD_CONST              13 ('ALLOWED_TRANSITIONS')
               STORE_SUBSCR

  89           LOAD_CONST              68 (('OPERATOR_APPROVED_FOR_MANUAL_TEST', 'OPERATOR_REJECTED', 'OPERATOR_EXPIRED', 'SYSTEM_EXPIRED', 'LOW_CONFIDENCE', 'HIGH_RISK', 'STALE', 'DUPLICATE_RECOMMENDATION'))
               STORE_NAME              20 (ALLOWED_REVIEW_REASON_TOKENS)
               LOAD_CONST               9 ('Tuple[str, ...]')
               LOAD_NAME               17 (__annotations__)
               LOAD_CONST              14 ('ALLOWED_REVIEW_REASON_TOKENS')
               STORE_SUBSCR

 101           LOAD_SMALL_INT         200
               STORE_NAME              21 (_BROKERAGE_ID_MAX_LEN)

 102           LOAD_SMALL_INT         200
               STORE_NAME              22 (_ACTOR_ID_MAX_LEN)

 103           LOAD_SMALL_INT         200
               STORE_NAME              23 (_REC_ID_MAX_LEN)

 104           LOAD_CONST              15 (500)
               STORE_NAME              24 (_LIST_HARD_CAP)

 105           LOAD_SMALL_INT          50
               STORE_NAME              25 (_DEFAULT_LIMIT)

 108           LOAD_CONST              16 ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_')

 107           STORE_NAME              26 (_ALLOWED_TOKEN_CHARS)

 115           LOAD_CONST              69 (('recommendation_id', 'brokerage_id', 'recommendation_type', 'source_type', 'source_id', 'status', 'confidence_score', 'risk_score', 'usefulness_score', 'recommended_action', 'rationale_token', 'created_at', 'reviewed_at', 'reviewed_by_actor_type', 'reviewed_by_actor_id', 'metadata'))
               STORE_NAME              27 (_STRUCTURAL_COLUMNS)

 139           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA2B50, file "app/services/learning/recommendation_review.py", line 139>)
               MAKE_FUNCTION
               LOAD_CONST              21 (<code object _now_iso at 0x0000018C18038670, file "app/services/learning/recommendation_review.py", line 139>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              28 (_now_iso)

 143           LOAD_CONST              22 (<code object _get_db_safe at 0x0000018C17FF10B0, file "app/services/learning/recommendation_review.py", line 143>)
               MAKE_FUNCTION
               STORE_NAME              29 (_get_db_safe)

 155           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA2D30, file "app/services/learning/recommendation_review.py", line 155>)
               MAKE_FUNCTION
               LOAD_CONST              24 (<code object _bound_brokerage_id at 0x0000018C17F95FD0, file "app/services/learning/recommendation_review.py", line 155>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              30 (_bound_brokerage_id)

 164           LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA3960, file "app/services/learning/recommendation_review.py", line 164>)
               MAKE_FUNCTION
               LOAD_CONST              26 (<code object _bound_recommendation_id at 0x0000018C17FA92F0, file "app/services/learning/recommendation_review.py", line 164>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              31 (_bound_recommendation_id)

 177           LOAD_CONST              27 (<code object __annotate__ at 0x0000018C17FA35A0, file "app/services/learning/recommendation_review.py", line 177>)
               MAKE_FUNCTION
               LOAD_CONST              28 (<code object _bound_actor_id at 0x0000018C1800AD80, file "app/services/learning/recommendation_review.py", line 177>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              32 (_bound_actor_id)

 189           LOAD_CONST              29 (<code object __annotate__ at 0x0000018C17FA3780, file "app/services/learning/recommendation_review.py", line 189>)
               MAKE_FUNCTION
               LOAD_CONST              30 (<code object _clamp_limit at 0x0000018C17972D90, file "app/services/learning/recommendation_review.py", line 189>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              33 (_clamp_limit)

 201           LOAD_CONST              31 (<code object __annotate__ at 0x0000018C17FA2880, file "app/services/learning/recommendation_review.py", line 201>)
               MAKE_FUNCTION
               LOAD_CONST              32 (<code object _project_row at 0x0000018C17FE1290, file "app/services/learning/recommendation_review.py", line 201>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              34 (_project_row)

 211           LOAD_CONST              33 ('record')

 214           LOAD_CONST               2 (None)

 211           LOAD_CONST              34 ('transition')

 215           LOAD_CONST               2 (None)

 211           LOAD_CONST              35 ('audit_row')

 216           LOAD_CONST               2 (None)

 211           LOAD_CONST              36 ('warnings')

 217           LOAD_CONST               2 (None)

 211           LOAD_CONST              37 ('error_code')

 218           LOAD_CONST               2 (None)

 211           BUILD_MAP                5
               LOAD_CONST              38 (<code object __annotate__ at 0x0000018C180909C0, file "app/services/learning/recommendation_review.py", line 211>)
               MAKE_FUNCTION
               LOAD_CONST              39 (<code object _safe_envelope at 0x0000018C18053630, file "app/services/learning/recommendation_review.py", line 211>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              35 (_safe_envelope)

 230           LOAD_CONST              40 (<code object __annotate__ at 0x0000018C18024930, file "app/services/learning/recommendation_review.py", line 230>)
               MAKE_FUNCTION
               LOAD_CONST              41 (<code object _validate_transition at 0x0000018C18010F50, file "app/services/learning/recommendation_review.py", line 230>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              36 (_validate_transition)

 252           LOAD_CONST              42 (<code object __annotate__ at 0x0000018C17FA3C30, file "app/services/learning/recommendation_review.py", line 252>)
               MAKE_FUNCTION
               LOAD_CONST              43 (<code object _validate_reason_token at 0x0000018C18010DF0, file "app/services/learning/recommendation_review.py", line 252>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              37 (_validate_reason_token)

 270           LOAD_CONST              18 ('brokerage_id')

 272           LOAD_CONST               2 (None)

 270           LOAD_CONST              19 ('status')

 273           LOAD_CONST               2 (None)

 270           LOAD_CONST              44 ('limit')

 274           LOAD_NAME               25 (_DEFAULT_LIMIT)

 270           BUILD_MAP                3
               LOAD_CONST              45 (<code object __annotate__ at 0x0000018C18024F30, file "app/services/learning/recommendation_review.py", line 270>)
               MAKE_FUNCTION
               LOAD_CONST              46 (<code object list_learning_recommendations at 0x0000018C17D8C050, file "app/services/learning/recommendation_review.py", line 270>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              38 (list_learning_recommendations)

 336           LOAD_CONST              18 ('brokerage_id')

 339           LOAD_CONST               2 (None)

 336           BUILD_MAP                1
               LOAD_CONST              47 (<code object __annotate__ at 0x0000018C18025830, file "app/services/learning/recommendation_review.py", line 336>)
               MAKE_FUNCTION
               LOAD_CONST              48 (<code object get_learning_recommendation at 0x0000018C17EDA7C0, file "app/services/learning/recommendation_review.py", line 336>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              39 (get_learning_recommendation)

 400           LOAD_CONST              37 ('error_code')

 406           LOAD_CONST               2 (None)

 400           LOAD_CONST              49 ('warning_count')

 407           LOAD_SMALL_INT           0

 400           BUILD_MAP                2
               LOAD_CONST              50 (<code object __annotate__ at 0x0000018C18090580, file "app/services/learning/recommendation_review.py", line 400>)
               MAKE_FUNCTION
               LOAD_CONST              51 (<code object _audit_review_action at 0x0000018C179C3C30, file "app/services/learning/recommendation_review.py", line 400>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              40 (_audit_review_action)

 435           LOAD_CONST              52 ('actor_id')

 440           LOAD_CONST               2 (None)

 435           LOAD_CONST              53 ('reason_token')

 441           LOAD_CONST               2 (None)

 435           BUILD_MAP                2
               LOAD_CONST              54 (<code object __annotate__ at 0x0000018C18025930, file "app/services/learning/recommendation_review.py", line 435>)
               MAKE_FUNCTION
               LOAD_CONST              55 (<code object review_learning_recommendation at 0x0000018C17E02060, file "app/services/learning/recommendation_review.py", line 435>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              41 (review_learning_recommendation)

 601           LOAD_CONST              52 ('actor_id')

 605           LOAD_CONST               2 (None)

 601           LOAD_CONST              53 ('reason_token')

 606           LOAD_CONST               2 (None)

 601           BUILD_MAP                2
               LOAD_CONST              56 (<code object __annotate__ at 0x0000018C18024C30, file "app/services/learning/recommendation_review.py", line 601>)
               MAKE_FUNCTION
               LOAD_CONST              57 (<code object approve_recommendation_for_manual_test at 0x0000018C18025530, file "app/services/learning/recommendation_review.py", line 601>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              42 (approve_recommendation_for_manual_test)

 617           LOAD_CONST              52 ('actor_id')

 621           LOAD_CONST               2 (None)

 617           LOAD_CONST              53 ('reason_token')

 622           LOAD_CONST               2 (None)

 617           BUILD_MAP                2
               LOAD_CONST              58 (<code object __annotate__ at 0x0000018C18025130, file "app/services/learning/recommendation_review.py", line 617>)
               MAKE_FUNCTION
               LOAD_CONST              59 (<code object reject_learning_recommendation at 0x0000018C18025A30, file "app/services/learning/recommendation_review.py", line 617>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              43 (reject_learning_recommendation)

 633           LOAD_CONST              52 ('actor_id')

 637           LOAD_CONST               2 (None)

 633           LOAD_CONST              53 ('reason_token')

 638           LOAD_CONST               2 (None)

 633           BUILD_MAP                2
               LOAD_CONST              60 (<code object __annotate__ at 0x0000018C18025330, file "app/services/learning/recommendation_review.py", line 633>)
               MAKE_FUNCTION
               LOAD_CONST              61 (<code object expire_learning_recommendation at 0x0000018C18025B30, file "app/services/learning/recommendation_review.py", line 633>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              44 (expire_learning_recommendation)

 653           LOAD_CONST              17 ('recommendation_id')

 655           LOAD_CONST               2 (None)

 653           LOAD_CONST              18 ('brokerage_id')

 656           LOAD_CONST               2 (None)

 653           LOAD_CONST              44 ('limit')

 657           LOAD_NAME               25 (_DEFAULT_LIMIT)

 653           BUILD_MAP                3
               LOAD_CONST              62 (<code object __annotate__ at 0x0000018C18025630, file "app/services/learning/recommendation_review.py", line 653>)
               MAKE_FUNCTION
               LOAD_CONST              63 (<code object recommendation_review_history at 0x0000018C17E93A90, file "app/services/learning/recommendation_review.py", line 653>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              45 (recommendation_review_history)

 702           BUILD_LIST               0
               LOAD_CONST              70 (('ALLOWED_REVIEW_STATUSES', 'ALLOWED_ACTOR_TYPES', 'ALLOWED_TRANSITIONS', 'ALLOWED_REVIEW_REASON_TOKENS', 'list_learning_recommendations', 'get_learning_recommendation', 'review_learning_recommendation', 'approve_recommendation_for_manual_test', 'reject_learning_recommendation', 'expire_learning_recommendation', 'recommendation_review_history'))
               LIST_EXTEND              1
               STORE_NAME              46 (__all__)
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "app/services/learning/recommendation_review.py", line 139>:
139           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038670, file "app/services/learning/recommendation_review.py", line 139>:
139           RESUME                   0

140           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object _get_db_safe at 0x0000018C17FF10B0, file "app/services/learning/recommendation_review.py", line 143>:
 143           RESUME                   0

 144           NOP

 145   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('get_supabase',))
               IMPORT_NAME              0 (app.db.supabase_client)
               IMPORT_FROM              1 (get_supabase)
               STORE_FAST               0 (get_supabase)
               POP_TOP

 146           LOAD_FAST_BORROW         0 (get_supabase)
               PUSH_NULL
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 147           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       55 (to L7)
               NOT_TAKEN
               STORE_FAST               1 (e)

 148   L4:     LOAD_GLOBAL              6 (logger)
               LOAD_ATTR                9 (warning + NULL|self)

 149           LOAD_CONST               2 ('recommendation_review db client unavailable type=')

 150           LOAD_GLOBAL             11 (type + NULL)
               LOAD_FAST                1 (e)
               CALL                     1
               LOAD_ATTR               12 (__name__)
               FORMAT_SIMPLE

 149           BUILD_STRING             2

 148           CALL                     1
               POP_TOP

 152   L5:     POP_EXCEPT
               LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               LOAD_CONST               3 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               RERAISE                  1

 147   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "app/services/learning/recommendation_review.py", line 155>:
155           RESUME                   0
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

Disassembly of <code object _bound_brokerage_id at 0x0000018C17F95FD0, file "app/services/learning/recommendation_review.py", line 155>:
155           RESUME                   0

156           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

157           LOAD_CONST               0 (None)
              RETURN_VALUE

158   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

159           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_FALSE       21 (to L2)
              NOT_TAKEN
              LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         1 (s)
              CALL                     1
              LOAD_GLOBAL              8 (_BROKERAGE_ID_MAX_LEN)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

160   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

161   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "app/services/learning/recommendation_review.py", line 164>:
164           RESUME                   0
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

Disassembly of <code object _bound_recommendation_id at 0x0000018C17FA92F0, file "app/services/learning/recommendation_review.py", line 164>:
164           RESUME                   0

165           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

166           LOAD_CONST               0 (None)
              RETURN_VALUE

167   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

168           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_FALSE       21 (to L2)
              NOT_TAKEN
              LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         1 (s)
              CALL                     1
              LOAD_GLOBAL              8 (_REC_ID_MAX_LEN)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

169   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

171   L3:     LOAD_FAST_BORROW         1 (s)
              GET_ITER
      L4:     FOR_ITER                17 (to L6)
              STORE_FAST               2 (ch)

172           LOAD_FAST_BORROW         2 (ch)
              LOAD_GLOBAL             10 (_ALLOWED_TOKEN_CHARS)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              JUMP_BACKWARD           16 (to L4)

173   L5:     POP_TOP
              LOAD_CONST               0 (None)
              RETURN_VALUE

171   L6:     END_FOR
              POP_ITER

174           LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "app/services/learning/recommendation_review.py", line 177>:
177           RESUME                   0
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

Disassembly of <code object _bound_actor_id at 0x0000018C1800AD80, file "app/services/learning/recommendation_review.py", line 177>:
177           RESUME                   0

178           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

179           LOAD_CONST               0 (None)
              RETURN_VALUE

180   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

181           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_FALSE       21 (to L2)
              NOT_TAKEN
              LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         1 (s)
              CALL                     1
              LOAD_GLOBAL              8 (_ACTOR_ID_MAX_LEN)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

182   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

183   L3:     LOAD_FAST_BORROW         1 (s)
              GET_ITER
      L4:     FOR_ITER                17 (to L6)
              STORE_FAST               2 (ch)

184           LOAD_FAST_BORROW         2 (ch)
              LOAD_GLOBAL             10 (_ALLOWED_TOKEN_CHARS)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              JUMP_BACKWARD           16 (to L4)

185   L5:     POP_TOP
              LOAD_CONST               0 (None)
              RETURN_VALUE

183   L6:     END_FOR
              POP_ITER

186           LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "app/services/learning/recommendation_review.py", line 189>:
189           RESUME                   0
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
              LOAD_CONST               4 ('int')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _clamp_limit at 0x0000018C17972D90, file "app/services/learning/recommendation_review.py", line 189>:
 189           RESUME                   0

 190           NOP

 191   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               1 (v)

 194   L2:     LOAD_FAST                1 (v)
               LOAD_SMALL_INT           1
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 195           LOAD_SMALL_INT           1
               RETURN_VALUE

 196   L3:     LOAD_FAST                1 (v)
               LOAD_GLOBAL              8 (_LIST_HARD_CAP)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        7 (to L4)
               NOT_TAKEN

 197           LOAD_GLOBAL              8 (_LIST_HARD_CAP)
               RETURN_VALUE

 198   L4:     LOAD_FAST                1 (v)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 192           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       10 (to L7)
               NOT_TAKEN
               POP_TOP

 193           LOAD_GLOBAL              6 (_DEFAULT_LIMIT)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

 192   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "app/services/learning/recommendation_review.py", line 201>:
201           RESUME                   0
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

Disassembly of <code object _project_row at 0x0000018C17FE1290, file "app/services/learning/recommendation_review.py", line 201>:
201           RESUME                   0

202           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (row)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

203           LOAD_CONST               0 (None)
              RETURN_VALUE

204   L1:     BUILD_MAP                0
              STORE_FAST               1 (out)

205           LOAD_GLOBAL              4 (_STRUCTURAL_COLUMNS)
              GET_ITER
      L2:     FOR_ITER                21 (to L4)
              STORE_FAST               2 (col)

206           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (col, row)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

207   L3:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (row, col)
              BINARY_OP               26 ([])
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (out, col)
              STORE_SUBSCR
              JUMP_BACKWARD           23 (to L2)

205   L4:     END_FOR
              POP_ITER

208           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180909C0, file "app/services/learning/recommendation_review.py", line 211>:
211           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')

213           LOAD_CONST               2 ('str')

211           LOAD_CONST               3 ('record')

214           LOAD_CONST               4 ('Optional[Dict[str, Any]]')

211           LOAD_CONST               5 ('transition')

215           LOAD_CONST               4 ('Optional[Dict[str, Any]]')

211           LOAD_CONST               6 ('audit_row')

216           LOAD_CONST               4 ('Optional[Dict[str, Any]]')

211           LOAD_CONST               7 ('warnings')

217           LOAD_CONST               8 ('Optional[List[str]]')

211           LOAD_CONST               9 ('error_code')

218           LOAD_CONST              10 ('Optional[str]')

211           LOAD_CONST              11 ('return')

219           LOAD_CONST              12 ('Dict[str, Any]')

211           BUILD_MAP                7
              RETURN_VALUE

Disassembly of <code object _safe_envelope at 0x0000018C18053630, file "app/services/learning/recommendation_review.py", line 211>:
211           RESUME                   0

221           LOAD_CONST               0 ('status')
              LOAD_FAST                0 (status)

222           LOAD_CONST               1 ('record')
              LOAD_FAST                1 (record)

223           LOAD_CONST               2 ('transition')
              LOAD_FAST                2 (transition)

224           LOAD_CONST               3 ('audit_row')
              LOAD_FAST                3 (audit_row)

225           LOAD_CONST               4 ('warnings')
              LOAD_GLOBAL              1 (list + NULL)
              LOAD_FAST                4 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

226           LOAD_CONST               5 ('error_code')
              LOAD_FAST_BORROW         5 (error_code)

220           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024930, file "app/services/learning/recommendation_review.py", line 230>:
230           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('from_status')

232           LOAD_CONST               2 ('Optional[str]')

230           LOAD_CONST               3 ('to_status')

233           LOAD_CONST               4 ('str')

230           LOAD_CONST               5 ('return')

234           LOAD_CONST               2 ('Optional[str]')

230           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _validate_transition at 0x0000018C18010F50, file "app/services/learning/recommendation_review.py", line 230>:
230           RESUME                   0

237           LOAD_FAST_BORROW         1 (to_status)
              LOAD_GLOBAL              0 (ALLOWED_REVIEW_STATUSES)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN

238           LOAD_CONST               1 ('invalid_target_status')
              RETURN_VALUE

239   L1:     LOAD_FAST_BORROW         1 (to_status)
              LOAD_CONST               2 ('CANDIDATE')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

241           LOAD_CONST               3 ('walk_back_to_candidate_forbidden')
              RETURN_VALUE

242   L2:     LOAD_FAST_BORROW         0 (from_status)
              POP_JUMP_IF_NOT_NONE     3 (to L3)
              NOT_TAKEN

243           LOAD_CONST               5 ('missing_current_status')
              RETURN_VALUE

244   L3:     LOAD_FAST_BORROW         0 (from_status)
              LOAD_GLOBAL              2 (ALLOWED_TRANSITIONS)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN

245           LOAD_CONST               6 ('invalid_transition')
              RETURN_VALUE

246   L4:     LOAD_GLOBAL              2 (ALLOWED_TRANSITIONS)
              LOAD_FAST_BORROW         0 (from_status)
              BINARY_OP               26 ([])
              STORE_FAST               2 (allowed)

247           LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (to_status, allowed)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN

248           LOAD_CONST               6 ('invalid_transition')
              RETURN_VALUE

249   L5:     LOAD_CONST               4 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "app/services/learning/recommendation_review.py", line 252>:
252           RESUME                   0
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

Disassembly of <code object _validate_reason_token at 0x0000018C18010DF0, file "app/services/learning/recommendation_review.py", line 252>:
252           RESUME                   0

254           LOAD_FAST_BORROW         0 (value)
              POP_JUMP_IF_NOT_NONE     3 (to L1)
              NOT_TAKEN

255           LOAD_CONST               1 (None)
              RETURN_VALUE

256   L1:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

257           LOAD_CONST               2 ('')
              RETURN_VALUE

258   L2:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

259           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN

260           LOAD_CONST               1 (None)
              RETURN_VALUE

261   L3:     LOAD_FAST_BORROW         1 (s)
              LOAD_GLOBAL              6 (ALLOWED_REVIEW_REASON_TOKENS)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN

262           LOAD_CONST               2 ('')
              RETURN_VALUE

263   L4:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024F30, file "app/services/learning/recommendation_review.py", line 270>:
270           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

272           LOAD_CONST               2 ('Optional[str]')

270           LOAD_CONST               3 ('status')

273           LOAD_CONST               2 ('Optional[str]')

270           LOAD_CONST               4 ('limit')

274           LOAD_CONST               5 ('Any')

270           LOAD_CONST               6 ('return')

275           LOAD_CONST               7 ('Dict[str, Any]')

270           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object list_learning_recommendations at 0x0000018C17D8C050, file "app/services/learning/recommendation_review.py", line 270>:
 270            RESUME                   0

 279            LOAD_FAST_BORROW         0 (brokerage_id)
                POP_JUMP_IF_NONE        12 (to L1)
                NOT_TAKEN
                LOAD_GLOBAL              1 (_bound_brokerage_id + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                JUMP_FORWARD             1 (to L2)
        L1:     LOAD_CONST               1 (None)
        L2:     STORE_FAST               3 (bid)

 280            LOAD_FAST_BORROW         1 (status)
                POP_JUMP_IF_NONE        26 (to L3)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (status)
                LOAD_GLOBAL              2 (ALLOWED_REVIEW_STATUSES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       15 (to L3)
                NOT_TAKEN

 282            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 283            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST_BORROW         3 (bid)

 284            LOAD_CONST               5 ('rows')
                BUILD_LIST               0

 285            LOAD_CONST               6 ('count')
                LOAD_SMALL_INT           0

 286            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 287            LOAD_CONST               8 ('error_code')
                LOAD_CONST               9 ('invalid_status')

 281            BUILD_MAP                6
                RETURN_VALUE

 289    L3:     LOAD_GLOBAL              5 (_clamp_limit + NULL)
                LOAD_FAST_BORROW         2 (limit)
                CALL                     1
                STORE_FAST               4 (capped)

 290            LOAD_GLOBAL              7 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               5 (db)

 291            LOAD_FAST_BORROW         5 (db)
                POP_JUMP_IF_NOT_NONE    16 (to L4)
                NOT_TAKEN

 293            LOAD_CONST               2 ('status')
                LOAD_CONST              10 ('skipped')

 294            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST_BORROW         3 (bid)

 295            LOAD_CONST               5 ('rows')
                BUILD_LIST               0

 296            LOAD_CONST               6 ('count')
                LOAD_SMALL_INT           0

 297            LOAD_CONST               7 ('warnings')
                LOAD_CONST              11 ('learning_recommendations_store_unavailable')
                BUILD_LIST               1

 298            LOAD_CONST               8 ('error_code')
                LOAD_CONST              11 ('learning_recommendations_store_unavailable')

 292            BUILD_MAP                6
                RETURN_VALUE

 300    L4:     NOP

 302    L5:     LOAD_FAST_BORROW         5 (db)
                LOAD_ATTR                9 (table + NULL|self)
                LOAD_GLOBAL             10 (_TABLE)
                CALL                     1

 303            LOAD_ATTR               13 (select + NULL|self)
                LOAD_CONST              12 (',')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_GLOBAL             16 (_STRUCTURAL_COLUMNS)
                CALL                     1
                CALL                     1

 304            LOAD_ATTR               19 (order + NULL|self)
                LOAD_CONST              13 ('created_at')
                LOAD_CONST              14 (True)
                LOAD_CONST              15 (('desc',))
                CALL_KW                  2

 305            LOAD_ATTR               21 (limit + NULL|self)
                LOAD_FAST_BORROW         4 (capped)
                CALL                     1

 301            STORE_FAST               6 (query)

 307            LOAD_FAST_BORROW         3 (bid)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L8)
        L6:     NOT_TAKEN

 308    L7:     LOAD_FAST_BORROW         6 (query)
                LOAD_ATTR               23 (eq + NULL|self)
                LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST_BORROW         3 (bid)
                CALL                     2
                STORE_FAST               6 (query)

 309    L8:     LOAD_FAST_BORROW         1 (status)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L11)
        L9:     NOT_TAKEN

 310   L10:     LOAD_FAST_BORROW         6 (query)
                LOAD_ATTR               23 (eq + NULL|self)
                LOAD_CONST               2 ('status')
                LOAD_FAST_BORROW         1 (status)
                CALL                     2
                STORE_FAST               6 (query)

 311   L11:     LOAD_FAST_BORROW         6 (query)
                LOAD_ATTR               25 (execute + NULL|self)
                CALL                     0
                STORE_FAST               7 (result)

 312            LOAD_GLOBAL             27 (list + NULL)
                LOAD_GLOBAL             29 (getattr + NULL)
                LOAD_FAST_BORROW         7 (result)
                LOAD_CONST              16 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L14)
       L12:     NOT_TAKEN
       L13:     POP_TOP
                BUILD_LIST               0
       L14:     CALL                     1
                STORE_FAST               8 (rows)

 313            LOAD_CONST              17 (<code object <genexpr> at 0x0000018C18090140, file "app/services/learning/recommendation_review.py", line 313>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         8 (rows)
                GET_ITER
                CALL                     0
                GET_ITER
                LOAD_FAST_AND_CLEAR      9 (p)
                SWAP                     2
       L15:     BUILD_LIST               0
                SWAP                     2
       L16:     FOR_ITER                10 (to L19)
                STORE_FAST_LOAD_FAST   153 (p, p)
       L17:     POP_JUMP_IF_NOT_NONE     3 (to L18)
                NOT_TAKEN
                JUMP_BACKWARD            8 (to L16)
       L18:     LOAD_FAST_BORROW         9 (p)
                LIST_APPEND              2
                JUMP_BACKWARD           12 (to L16)
       L19:     END_FOR
                POP_ITER
       L20:     STORE_FAST              10 (projected)
                STORE_FAST               9 (p)

 315            LOAD_CONST               2 ('status')
                LOAD_CONST              18 ('ok')

 316            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST_BORROW         3 (bid)

 317            LOAD_CONST               5 ('rows')
                LOAD_FAST_BORROW        10 (projected)

 318            LOAD_CONST               6 ('count')
                LOAD_GLOBAL             31 (len + NULL)
                LOAD_FAST_BORROW        10 (projected)
                CALL                     1

 319            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 320            LOAD_CONST               8 ('error_code')
                LOAD_CONST               1 (None)

 314            BUILD_MAP                6
       L21:     RETURN_VALUE

  --   L22:     SWAP                     2
                POP_TOP

 313            SWAP                     2
                STORE_FAST               9 (p)
                RERAISE                  0

  --   L23:     PUSH_EXC_INFO

 322            LOAD_GLOBAL             32 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       91 (to L28)
                NOT_TAKEN
                STORE_FAST              11 (e)

 323   L24:     LOAD_GLOBAL             34 (logger)
                LOAD_ATTR               37 (warning + NULL|self)

 324            LOAD_CONST              19 ('list_learning_recommendations read error type=')
                LOAD_GLOBAL             39 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               40 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 323            CALL                     1
                POP_TOP

 327            LOAD_CONST               2 ('status')
                LOAD_CONST              10 ('skipped')

 328            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST                3 (bid)

 329            LOAD_CONST               5 ('rows')
                BUILD_LIST               0

 330            LOAD_CONST               6 ('count')
                LOAD_SMALL_INT           0

 331            LOAD_CONST               7 ('warnings')
                LOAD_CONST              20 ('db_read_failed:')
                LOAD_GLOBAL             39 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               40 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 332            LOAD_CONST               8 ('error_code')
                LOAD_CONST              11 ('learning_recommendations_store_unavailable')

 326            BUILD_MAP                6
       L25:     SWAP                     2
       L26:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RETURN_VALUE

  --   L27:     LOAD_CONST               1 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RERAISE                  1

 322   L28:     RERAISE                  0

  --   L29:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L5 to L6 -> L23 [0]
  L7 to L9 -> L23 [0]
  L10 to L12 -> L23 [0]
  L13 to L15 -> L23 [0]
  L15 to L17 -> L22 [2]
  L18 to L20 -> L22 [2]
  L20 to L21 -> L23 [0]
  L22 to L23 -> L23 [0]
  L23 to L24 -> L29 [1] lasti
  L24 to L25 -> L27 [1] lasti
  L25 to L26 -> L29 [1] lasti
  L27 to L29 -> L29 [1] lasti

Disassembly of <code object <genexpr> at 0x0000018C18090140, file "app/services/learning/recommendation_review.py", line 313>:
 313           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                16 (to L3)
               STORE_FAST               1 (r)
               LOAD_GLOBAL              1 (_project_row + NULL)
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

Disassembly of <code object __annotate__ at 0x0000018C18025830, file "app/services/learning/recommendation_review.py", line 336>:
336           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('recommendation_id')

338           LOAD_CONST               2 ('str')

336           LOAD_CONST               3 ('brokerage_id')

339           LOAD_CONST               4 ('Optional[str]')

336           LOAD_CONST               5 ('return')

340           LOAD_CONST               6 ('Dict[str, Any]')

336           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object get_learning_recommendation at 0x0000018C17EDA7C0, file "app/services/learning/recommendation_review.py", line 336>:
 336            RESUME                   0

 343            LOAD_GLOBAL              1 (_bound_recommendation_id + NULL)
                LOAD_FAST_BORROW         0 (recommendation_id)
                CALL                     1
                STORE_FAST               2 (rid)

 344            LOAD_FAST_BORROW         2 (rid)
                POP_JUMP_IF_NOT_NONE    11 (to L1)
                NOT_TAKEN

 346            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 347            LOAD_CONST               4 ('record')
                LOAD_CONST               1 (None)

 348            LOAD_CONST               5 ('warnings')
                BUILD_LIST               0

 349            LOAD_CONST               6 ('error_code')
                LOAD_CONST               7 ('invalid_recommendation_id')

 345            BUILD_MAP                4
                RETURN_VALUE

 351    L1:     LOAD_FAST_BORROW         1 (brokerage_id)
                POP_JUMP_IF_NONE        12 (to L2)
                NOT_TAKEN
                LOAD_GLOBAL              3 (_bound_brokerage_id + NULL)
                LOAD_FAST_BORROW         1 (brokerage_id)
                CALL                     1
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               1 (None)
        L3:     STORE_FAST               3 (bid)

 352            LOAD_GLOBAL              5 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               4 (db)

 353            LOAD_FAST_BORROW         4 (db)
                POP_JUMP_IF_NOT_NONE    12 (to L4)
                NOT_TAKEN

 355            LOAD_CONST               2 ('status')
                LOAD_CONST               8 ('skipped')

 356            LOAD_CONST               4 ('record')
                LOAD_CONST               1 (None)

 357            LOAD_CONST               5 ('warnings')
                LOAD_CONST               9 ('learning_recommendations_store_unavailable')
                BUILD_LIST               1

 358            LOAD_CONST               6 ('error_code')
                LOAD_CONST               9 ('learning_recommendations_store_unavailable')

 354            BUILD_MAP                4
                RETURN_VALUE

 360    L4:     NOP

 362    L5:     LOAD_FAST_BORROW         4 (db)
                LOAD_ATTR                7 (table + NULL|self)
                LOAD_GLOBAL              8 (_TABLE)
                CALL                     1

 363            LOAD_ATTR               11 (select + NULL|self)
                LOAD_CONST              10 (',')
                LOAD_ATTR               13 (join + NULL|self)
                LOAD_GLOBAL             14 (_STRUCTURAL_COLUMNS)
                CALL                     1
                CALL                     1

 364            LOAD_ATTR               17 (eq + NULL|self)
                LOAD_CONST              11 ('recommendation_id')
                LOAD_FAST_BORROW         2 (rid)
                CALL                     2

 365            LOAD_ATTR               19 (limit + NULL|self)
                LOAD_SMALL_INT           2
                CALL                     1

 361            STORE_FAST               5 (query)

 367            LOAD_FAST_BORROW         3 (bid)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L8)
        L6:     NOT_TAKEN

 368    L7:     LOAD_FAST_BORROW         5 (query)
                LOAD_ATTR               17 (eq + NULL|self)
                LOAD_CONST              12 ('brokerage_id')
                LOAD_FAST_BORROW         3 (bid)
                CALL                     2
                STORE_FAST               5 (query)

 369    L8:     LOAD_FAST_BORROW         5 (query)
                LOAD_ATTR               21 (execute + NULL|self)
                CALL                     0
                STORE_FAST               6 (result)

 370            LOAD_GLOBAL             23 (list + NULL)
                LOAD_GLOBAL             25 (getattr + NULL)
                LOAD_FAST_BORROW         6 (result)
                LOAD_CONST              13 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L11)
        L9:     NOT_TAKEN
       L10:     POP_TOP
                BUILD_LIST               0
       L11:     CALL                     1
                STORE_FAST               7 (rows)

 381   L12:     LOAD_FAST                7 (rows)
                TO_BOOL
                POP_JUMP_IF_TRUE        11 (to L13)
                NOT_TAKEN

 383            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 384            LOAD_CONST               4 ('record')
                LOAD_CONST               1 (None)

 385            LOAD_CONST               5 ('warnings')
                BUILD_LIST               0

 386            LOAD_CONST               6 ('error_code')
                LOAD_CONST              16 ('recommendation_not_found_or_cross_brokerage')

 382            BUILD_MAP                4
                RETURN_VALUE

 389   L13:     LOAD_CONST               2 ('status')
                LOAD_CONST              17 ('ok')

 390            LOAD_CONST               4 ('record')
                LOAD_GLOBAL             37 (_project_row + NULL)
                LOAD_FAST                7 (rows)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                CALL                     1

 391            LOAD_CONST               5 ('warnings')
                BUILD_LIST               0

 392            LOAD_CONST               6 ('error_code')
                LOAD_CONST               1 (None)

 388            BUILD_MAP                4
                RETURN_VALUE

  --   L14:     PUSH_EXC_INFO

 371            LOAD_GLOBAL             26 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       87 (to L19)
                NOT_TAKEN
                STORE_FAST               8 (e)

 372   L15:     LOAD_GLOBAL             28 (logger)
                LOAD_ATTR               31 (warning + NULL|self)

 373            LOAD_CONST              14 ('get_learning_recommendation read error type=')
                LOAD_GLOBAL             33 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               34 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 372            CALL                     1
                POP_TOP

 376            LOAD_CONST               2 ('status')
                LOAD_CONST               8 ('skipped')

 377            LOAD_CONST               4 ('record')
                LOAD_CONST               1 (None)

 378            LOAD_CONST               5 ('warnings')
                LOAD_CONST              15 ('db_read_failed:')
                LOAD_GLOBAL             33 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               34 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 379            LOAD_CONST               6 ('error_code')
                LOAD_CONST               9 ('learning_recommendations_store_unavailable')

 375            BUILD_MAP                4
       L16:     SWAP                     2
       L17:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RETURN_VALUE

  --   L18:     LOAD_CONST               1 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RERAISE                  1

 371   L19:     RERAISE                  0

  --   L20:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L5 to L6 -> L14 [0]
  L7 to L9 -> L14 [0]
  L10 to L12 -> L14 [0]
  L14 to L15 -> L20 [1] lasti
  L15 to L16 -> L18 [1] lasti
  L16 to L17 -> L20 [1] lasti
  L18 to L20 -> L20 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18090580, file "app/services/learning/recommendation_review.py", line 400>:
400           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('record')

402           LOAD_CONST               2 ('Dict[str, Any]')

400           LOAD_CONST               3 ('to_status')

403           LOAD_CONST               4 ('str')

400           LOAD_CONST               5 ('actor_type')

404           LOAD_CONST               4 ('str')

400           LOAD_CONST               6 ('actor_id')

405           LOAD_CONST               7 ('Optional[str]')

400           LOAD_CONST               8 ('error_code')

406           LOAD_CONST               7 ('Optional[str]')

400           LOAD_CONST               9 ('warning_count')

407           LOAD_CONST              10 ('int')

400           LOAD_CONST              11 ('return')

408           LOAD_CONST              12 ('Optional[Dict[str, Any]]')

400           BUILD_MAP                7
              RETURN_VALUE

Disassembly of <code object _audit_review_action at 0x0000018C179C3C30, file "app/services/learning/recommendation_review.py", line 400>:
 400            RESUME                   0

 411            NOP

 412    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               1 (('log_operator_action',))
                IMPORT_NAME              0 (app.services.operator.audit_service)
                IMPORT_FROM              1 (log_operator_action)
                STORE_FAST               6 (log_operator_action)
                POP_TOP

 413            LOAD_FAST                6 (log_operator_action)
                PUSH_NULL

 414            LOAD_FAST_BORROW         0 (record)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               2 ('brokerage_id')
                CALL                     1

 415            LOAD_FAST                2 (actor_type)

 416            LOAD_FAST                3 (actor_id)

 417            LOAD_CONST               3 ('review_learning_recommendation')

 418            LOAD_FAST_BORROW         4 (error_code)
                POP_JUMP_IF_NOT_NONE     3 (to L2)
                NOT_TAKEN
                LOAD_CONST               5 ('SUCCESS')
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               6 ('FAILED')

 419    L3:     LOAD_CONST               7 ('learning_recommendation')

 420            LOAD_FAST_BORROW         0 (record)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               8 ('recommendation_id')
                CALL                     1

 421            LOAD_FAST_BORROW         5 (warning_count)

 423            LOAD_CONST               9 ('event')
                LOAD_CONST              10 ('learning.recommendation.reviewed')

 424            LOAD_CONST              11 ('target_status')
                LOAD_FAST_BORROW         1 (to_status)

 425            LOAD_CONST              12 ('error_code')
                LOAD_FAST_BORROW         4 (error_code)

 422            BUILD_MAP                3

 413            LOAD_CONST              13 (('brokerage_id', 'actor_type', 'actor_id', 'action', 'status', 'target_type', 'target_id', 'warning_count', 'metadata'))
                CALL_KW                  9
        L4:     RETURN_VALUE

  --    L5:     PUSH_EXC_INFO

 428            LOAD_GLOBAL              6 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       55 (to L9)
                NOT_TAKEN
                STORE_FAST               7 (e)

 429    L6:     LOAD_GLOBAL              8 (logger)
                LOAD_ATTR               11 (warning + NULL|self)

 430            LOAD_CONST              14 ('_audit_review_action error type=')
                LOAD_GLOBAL             13 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               14 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 429            CALL                     1
                POP_TOP

 432    L7:     POP_EXCEPT
                LOAD_CONST               4 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                LOAD_CONST               4 (None)
                RETURN_VALUE

  --    L8:     LOAD_CONST               4 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RERAISE                  1

 428    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L4 -> L5 [0]
  L5 to L6 -> L10 [1] lasti
  L6 to L7 -> L8 [1] lasti
  L8 to L10 -> L10 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025930, file "app/services/learning/recommendation_review.py", line 435>:
435           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('recommendation_id')

437           LOAD_CONST               2 ('str')

435           LOAD_CONST               3 ('to_status')

438           LOAD_CONST               2 ('str')

435           LOAD_CONST               4 ('actor_type')

439           LOAD_CONST               2 ('str')

435           LOAD_CONST               5 ('actor_id')

440           LOAD_CONST               6 ('Optional[str]')

435           LOAD_CONST               7 ('reason_token')

441           LOAD_CONST               6 ('Optional[str]')

435           LOAD_CONST               8 ('return')

442           LOAD_CONST               9 ('Dict[str, Any]')

435           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object review_learning_recommendation at 0x0000018C17E02060, file "app/services/learning/recommendation_review.py", line 435>:
 435            RESUME                   0

 446            LOAD_FAST_BORROW         2 (actor_type)
                LOAD_GLOBAL              0 (ALLOWED_ACTOR_TYPES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       14 (to L1)
                NOT_TAKEN

 447            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_CONST               2 ('invalid_actor_type')
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 448    L1:     LOAD_CONST               4 (None)
                STORE_FAST               5 (actor)

 449            LOAD_FAST_BORROW         3 (actor_id)
                POP_JUMP_IF_NONE        29 (to L2)
                NOT_TAKEN

 450            LOAD_GLOBAL              5 (_bound_actor_id + NULL)
                LOAD_FAST_BORROW         3 (actor_id)
                CALL                     1
                STORE_FAST               5 (actor)

 451            LOAD_FAST_BORROW         5 (actor)
                POP_JUMP_IF_NOT_NONE    14 (to L2)
                NOT_TAKEN

 452            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_CONST               5 ('invalid_actor_id')
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 453    L2:     LOAD_GLOBAL              7 (_bound_recommendation_id + NULL)
                LOAD_FAST_BORROW         0 (recommendation_id)
                CALL                     1
                STORE_FAST               6 (rid)

 454            LOAD_FAST_BORROW         6 (rid)
                POP_JUMP_IF_NOT_NONE    14 (to L3)
                NOT_TAKEN

 455            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_CONST               6 ('invalid_recommendation_id')
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 456    L3:     LOAD_FAST_BORROW         1 (to_status)
                LOAD_GLOBAL              8 (ALLOWED_REVIEW_STATUSES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       14 (to L4)
                NOT_TAKEN

 457            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_CONST               7 ('invalid_target_status')
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 458    L4:     LOAD_FAST_BORROW         1 (to_status)
                LOAD_CONST               8 ('CANDIDATE')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       14 (to L5)
                NOT_TAKEN

 459            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 460            LOAD_CONST               1 ('failed')

 461            LOAD_CONST               9 ('walk_back_to_candidate_forbidden')

 459            LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 463    L5:     LOAD_GLOBAL             11 (_validate_reason_token + NULL)
                LOAD_FAST_BORROW         4 (reason_token)
                CALL                     1
                STORE_FAST               7 (bounded_reason)

 464            LOAD_FAST_BORROW         4 (reason_token)
                POP_JUMP_IF_NONE        21 (to L6)
                NOT_TAKEN
                LOAD_FAST_BORROW         7 (bounded_reason)
                LOAD_CONST              10 ('')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       14 (to L6)
                NOT_TAKEN

 465            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_CONST              11 ('invalid_reason_token')
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 467    L6:     LOAD_GLOBAL             13 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               8 (db)

 468            LOAD_FAST_BORROW         8 (db)
                POP_JUMP_IF_NOT_NONE    16 (to L7)
                NOT_TAKEN

 469            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 470            LOAD_CONST              12 ('skipped')

 471            LOAD_CONST              13 ('learning_recommendations_store_unavailable')
                BUILD_LIST               1

 472            LOAD_CONST              13 ('learning_recommendations_store_unavailable')

 469            LOAD_CONST              14 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 476    L7:     NOP

 478    L8:     LOAD_FAST_BORROW         8 (db)
                LOAD_ATTR               15 (table + NULL|self)
                LOAD_GLOBAL             16 (_TABLE)
                CALL                     1

 479            LOAD_ATTR               19 (select + NULL|self)
                LOAD_CONST              15 (',')
                LOAD_ATTR               21 (join + NULL|self)
                LOAD_GLOBAL             22 (_STRUCTURAL_COLUMNS)
                CALL                     1
                CALL                     1

 480            LOAD_ATTR               25 (eq + NULL|self)
                LOAD_CONST              16 ('recommendation_id')
                LOAD_FAST_BORROW         6 (rid)
                CALL                     2

 481            LOAD_ATTR               27 (limit + NULL|self)
                LOAD_SMALL_INT           2
                CALL                     1

 482            LOAD_ATTR               29 (execute + NULL|self)
                CALL                     0

 477            STORE_FAST               9 (result)

 484            LOAD_GLOBAL             31 (list + NULL)
                LOAD_GLOBAL             33 (getattr + NULL)
                LOAD_FAST_BORROW         9 (result)
                LOAD_CONST              17 ('data')
                LOAD_CONST               4 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L11)
        L9:     NOT_TAKEN
       L10:     POP_TOP
                BUILD_LIST               0
       L11:     CALL                     1
                STORE_FAST              10 (rows)

 495   L12:     LOAD_FAST               10 (rows)
                TO_BOOL
                POP_JUMP_IF_TRUE        14 (to L13)
                NOT_TAKEN

 496            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 497            LOAD_CONST               1 ('failed')

 498            LOAD_CONST              20 ('recommendation_not_found')

 496            LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 500   L13:     LOAD_FAST               10 (rows)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                STORE_FAST              12 (current)

 501            LOAD_GLOBAL             45 (isinstance + NULL)
                LOAD_FAST               12 (current)
                LOAD_GLOBAL             46 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        14 (to L14)
                NOT_TAKEN

 502            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_CONST              21 ('recommendation_corrupt')
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 504   L14:     LOAD_FAST               12 (current)
                LOAD_ATTR               49 (get + NULL|self)
                LOAD_CONST              22 ('status')
                CALL                     1
                STORE_FAST              13 (from_status)

 505            LOAD_GLOBAL             51 (_validate_transition + NULL)
                LOAD_FAST_LOAD_FAST    209 (from_status, to_status)
                LOAD_CONST              23 (('from_status', 'to_status'))
                CALL_KW                  2
                STORE_FAST              14 (err)

 506            LOAD_FAST               14 (err)
                POP_JUMP_IF_NONE        49 (to L15)
                NOT_TAKEN

 507            LOAD_GLOBAL             53 (_audit_review_action + NULL)

 508            LOAD_FAST               12 (current)

 509            LOAD_FAST                1 (to_status)

 510            LOAD_FAST                2 (actor_type)

 511            LOAD_FAST                5 (actor)

 512            LOAD_FAST               14 (err)

 513            LOAD_SMALL_INT           1

 507            LOAD_CONST              24 (('record', 'to_status', 'actor_type', 'actor_id', 'error_code', 'warning_count'))
                CALL_KW                  6
                STORE_FAST              15 (audit_env)

 515            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 516            LOAD_CONST               1 ('failed')

 517            LOAD_GLOBAL             55 (_project_row + NULL)
                LOAD_FAST               12 (current)
                CALL                     1

 519            LOAD_CONST              25 ('from')
                LOAD_FAST               13 (from_status)

 520            LOAD_CONST              26 ('to')
                LOAD_FAST                1 (to_status)

 521            LOAD_CONST              27 ('ok')
                LOAD_CONST              28 (False)

 518            BUILD_MAP                3

 523            LOAD_FAST               15 (audit_env)

 524            LOAD_FAST               14 (err)

 515            LOAD_CONST              29 (('status', 'record', 'transition', 'audit_row', 'error_code'))
                CALL_KW                  5
                RETURN_VALUE

 528   L15:     LOAD_CONST              22 ('status')
                LOAD_FAST                1 (to_status)

 529            LOAD_CONST              30 ('reviewed_at')
                LOAD_GLOBAL             57 (_now_iso + NULL)
                CALL                     0

 530            LOAD_CONST              31 ('reviewed_by_actor_type')
                LOAD_FAST                2 (actor_type)

 531            LOAD_CONST              32 ('reviewed_by_actor_id')
                LOAD_FAST                5 (actor)

 527            BUILD_MAP                4
                STORE_FAST              16 (patch)

 534            NOP

 536   L16:     LOAD_FAST                8 (db)
                LOAD_ATTR               15 (table + NULL|self)
                LOAD_GLOBAL             16 (_TABLE)
                CALL                     1

 537            LOAD_ATTR               59 (update + NULL|self)
                LOAD_FAST               16 (patch)
                CALL                     1

 538            LOAD_ATTR               25 (eq + NULL|self)
                LOAD_CONST              16 ('recommendation_id')
                LOAD_FAST                6 (rid)
                CALL                     2

 539            LOAD_ATTR               29 (execute + NULL|self)
                CALL                     0

 535            STORE_FAST              17 (upd)

 541            LOAD_GLOBAL             31 (list + NULL)
                LOAD_GLOBAL             33 (getattr + NULL)
                LOAD_FAST               17 (upd)
                LOAD_CONST              17 ('data')
                LOAD_CONST               4 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L17)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
       L17:     CALL                     1
                STORE_FAST              18 (rows_after)

 562   L18:     LOAD_FAST               18 (rows_after)
                TO_BOOL
                POP_JUMP_IF_TRUE        49 (to L19)
                NOT_TAKEN

 566            LOAD_GLOBAL             53 (_audit_review_action + NULL)

 567            LOAD_FAST               12 (current)

 568            LOAD_FAST                1 (to_status)

 569            LOAD_FAST                2 (actor_type)

 570            LOAD_FAST                5 (actor)

 571            LOAD_CONST              37 ('policy_refused_or_no_rows')

 572            LOAD_SMALL_INT           1

 566            LOAD_CONST              24 (('record', 'to_status', 'actor_type', 'actor_id', 'error_code', 'warning_count'))
                CALL_KW                  6
                STORE_FAST              15 (audit_env)

 574            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 575            LOAD_CONST               1 ('failed')

 576            LOAD_GLOBAL             55 (_project_row + NULL)
                LOAD_FAST               12 (current)
                CALL                     1

 577            LOAD_CONST              25 ('from')
                LOAD_FAST               13 (from_status)
                LOAD_CONST              26 ('to')
                LOAD_FAST                1 (to_status)
                LOAD_CONST              27 ('ok')
                LOAD_CONST              28 (False)
                BUILD_MAP                3

 578            LOAD_FAST               15 (audit_env)

 579            LOAD_CONST              37 ('policy_refused_or_no_rows')

 574            LOAD_CONST              29 (('status', 'record', 'transition', 'audit_row', 'error_code'))
                CALL_KW                  5
                RETURN_VALUE

 582   L19:     LOAD_GLOBAL             55 (_project_row + NULL)
                LOAD_FAST               18 (rows_after)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                CALL                     1
                STORE_FAST              19 (new_record)

 583            LOAD_GLOBAL             53 (_audit_review_action + NULL)

 584            LOAD_FAST               19 (new_record)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L20)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST               12 (current)

 585   L20:     LOAD_FAST                1 (to_status)

 586            LOAD_FAST                2 (actor_type)

 587            LOAD_FAST                5 (actor)

 583            LOAD_CONST              38 (('record', 'to_status', 'actor_type', 'actor_id'))
                CALL_KW                  4
                STORE_FAST              15 (audit_env)

 589            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 590            LOAD_CONST              27 ('ok')

 591            LOAD_FAST               19 (new_record)

 592            LOAD_CONST              25 ('from')
                LOAD_FAST               13 (from_status)
                LOAD_CONST              26 ('to')
                LOAD_FAST                1 (to_status)
                LOAD_CONST              27 ('ok')
                LOAD_CONST              39 (True)
                BUILD_MAP                3

 593            LOAD_FAST               15 (audit_env)

 589            LOAD_CONST              40 (('status', 'record', 'transition', 'audit_row'))
                CALL_KW                  4
                RETURN_VALUE

  --   L21:     PUSH_EXC_INFO

 485            LOAD_GLOBAL             34 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       91 (to L26)
                NOT_TAKEN
                STORE_FAST              11 (e)

 486   L22:     LOAD_GLOBAL             36 (logger)
                LOAD_ATTR               39 (warning + NULL|self)

 487            LOAD_CONST              18 ('review_learning_recommendation lookup error type=')

 488            LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE

 487            BUILD_STRING             2

 486            CALL                     1
                POP_TOP

 490            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 491            LOAD_CONST              12 ('skipped')

 492            LOAD_CONST              19 ('db_read_failed:')
                LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 493            LOAD_CONST              13 ('learning_recommendations_store_unavailable')

 490            LOAD_CONST              14 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
       L23:     SWAP                     2
       L24:     POP_EXCEPT
                LOAD_CONST               4 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RETURN_VALUE

  --   L25:     LOAD_CONST               4 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RERAISE                  1

 485   L26:     RERAISE                  0

  --   L27:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L28:     PUSH_EXC_INFO

 542            LOAD_GLOBAL             34 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      109 (to L33)
                NOT_TAKEN
                STORE_FAST              11 (e)

 543   L29:     LOAD_GLOBAL             36 (logger)
                LOAD_ATTR               39 (warning + NULL|self)

 544            LOAD_CONST              33 ('review_learning_recommendation update error type=')

 545            LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE

 544            BUILD_STRING             2

 543            CALL                     1
                POP_TOP

 547            LOAD_GLOBAL             53 (_audit_review_action + NULL)

 548            LOAD_FAST               12 (current)

 549            LOAD_FAST                1 (to_status)

 550            LOAD_FAST                2 (actor_type)

 551            LOAD_FAST                5 (actor)

 552            LOAD_CONST              34 ('db_write_failed')

 553            LOAD_SMALL_INT           1

 547            LOAD_CONST              24 (('record', 'to_status', 'actor_type', 'actor_id', 'error_code', 'warning_count'))
                CALL_KW                  6
                STORE_FAST              15 (audit_env)

 555            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 556            LOAD_CONST              12 ('skipped')

 557            LOAD_CONST              35 ('db_write_failed:')
                LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 558            LOAD_CONST              13 ('learning_recommendations_store_unavailable')

 559            LOAD_FAST               15 (audit_env)

 555            LOAD_CONST              36 (('status', 'warnings', 'error_code', 'audit_row'))
                CALL_KW                  4
       L30:     SWAP                     2
       L31:     POP_EXCEPT
                LOAD_CONST               4 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RETURN_VALUE

  --   L32:     LOAD_CONST               4 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RERAISE                  1

 542   L33:     RERAISE                  0

  --   L34:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L8 to L9 -> L21 [0]
  L10 to L12 -> L21 [0]
  L16 to L18 -> L28 [0]
  L21 to L22 -> L27 [1] lasti
  L22 to L23 -> L25 [1] lasti
  L23 to L24 -> L27 [1] lasti
  L25 to L27 -> L27 [1] lasti
  L28 to L29 -> L34 [1] lasti
  L29 to L30 -> L32 [1] lasti
  L30 to L31 -> L34 [1] lasti
  L32 to L34 -> L34 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "app/services/learning/recommendation_review.py", line 601>:
601           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('recommendation_id')

603           LOAD_CONST               2 ('str')

601           LOAD_CONST               3 ('actor_type')

604           LOAD_CONST               2 ('str')

601           LOAD_CONST               4 ('actor_id')

605           LOAD_CONST               5 ('Optional[str]')

601           LOAD_CONST               6 ('reason_token')

606           LOAD_CONST               5 ('Optional[str]')

601           LOAD_CONST               7 ('return')

607           LOAD_CONST               8 ('Dict[str, Any]')

601           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object approve_recommendation_for_manual_test at 0x0000018C18025530, file "app/services/learning/recommendation_review.py", line 601>:
601           RESUME                   0

608           LOAD_GLOBAL              1 (review_learning_recommendation + NULL)

609           LOAD_FAST_BORROW         0 (recommendation_id)

610           LOAD_CONST               0 ('APPROVED_FOR_MANUAL_TEST')

611           LOAD_FAST_BORROW         1 (actor_type)

612           LOAD_FAST_BORROW         2 (actor_id)

613           LOAD_FAST_BORROW         3 (reason_token)

608           LOAD_CONST               1 (('recommendation_id', 'to_status', 'actor_type', 'actor_id', 'reason_token'))
              CALL_KW                  5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025130, file "app/services/learning/recommendation_review.py", line 617>:
617           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('recommendation_id')

619           LOAD_CONST               2 ('str')

617           LOAD_CONST               3 ('actor_type')

620           LOAD_CONST               2 ('str')

617           LOAD_CONST               4 ('actor_id')

621           LOAD_CONST               5 ('Optional[str]')

617           LOAD_CONST               6 ('reason_token')

622           LOAD_CONST               5 ('Optional[str]')

617           LOAD_CONST               7 ('return')

623           LOAD_CONST               8 ('Dict[str, Any]')

617           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object reject_learning_recommendation at 0x0000018C18025A30, file "app/services/learning/recommendation_review.py", line 617>:
617           RESUME                   0

624           LOAD_GLOBAL              1 (review_learning_recommendation + NULL)

625           LOAD_FAST_BORROW         0 (recommendation_id)

626           LOAD_CONST               0 ('REJECTED')

627           LOAD_FAST_BORROW         1 (actor_type)

628           LOAD_FAST_BORROW         2 (actor_id)

629           LOAD_FAST_BORROW         3 (reason_token)

624           LOAD_CONST               1 (('recommendation_id', 'to_status', 'actor_type', 'actor_id', 'reason_token'))
              CALL_KW                  5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025330, file "app/services/learning/recommendation_review.py", line 633>:
633           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('recommendation_id')

635           LOAD_CONST               2 ('str')

633           LOAD_CONST               3 ('actor_type')

636           LOAD_CONST               2 ('str')

633           LOAD_CONST               4 ('actor_id')

637           LOAD_CONST               5 ('Optional[str]')

633           LOAD_CONST               6 ('reason_token')

638           LOAD_CONST               5 ('Optional[str]')

633           LOAD_CONST               7 ('return')

639           LOAD_CONST               8 ('Dict[str, Any]')

633           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object expire_learning_recommendation at 0x0000018C18025B30, file "app/services/learning/recommendation_review.py", line 633>:
633           RESUME                   0

640           LOAD_GLOBAL              1 (review_learning_recommendation + NULL)

641           LOAD_FAST_BORROW         0 (recommendation_id)

642           LOAD_CONST               0 ('EXPIRED')

643           LOAD_FAST_BORROW         1 (actor_type)

644           LOAD_FAST_BORROW         2 (actor_id)

645           LOAD_FAST_BORROW         3 (reason_token)

640           LOAD_CONST               1 (('recommendation_id', 'to_status', 'actor_type', 'actor_id', 'reason_token'))
              CALL_KW                  5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025630, file "app/services/learning/recommendation_review.py", line 653>:
653           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('recommendation_id')

655           LOAD_CONST               2 ('Optional[str]')

653           LOAD_CONST               3 ('brokerage_id')

656           LOAD_CONST               2 ('Optional[str]')

653           LOAD_CONST               4 ('limit')

657           LOAD_CONST               5 ('Any')

653           LOAD_CONST               6 ('return')

658           LOAD_CONST               7 ('Dict[str, Any]')

653           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object recommendation_review_history at 0x0000018C17E93A90, file "app/services/learning/recommendation_review.py", line 653>:
 653            RESUME                   0

 662            LOAD_FAST_BORROW         0 (recommendation_id)
                POP_JUMP_IF_NONE        12 (to L1)
                NOT_TAKEN
                LOAD_GLOBAL              1 (_bound_recommendation_id + NULL)
                LOAD_FAST_BORROW         0 (recommendation_id)
                CALL                     1
                JUMP_FORWARD             1 (to L2)
        L1:     LOAD_CONST               1 (None)
        L2:     STORE_FAST               3 (rid)

 663            LOAD_FAST_BORROW         1 (brokerage_id)
                POP_JUMP_IF_NONE        12 (to L3)
                NOT_TAKEN
                LOAD_GLOBAL              3 (_bound_brokerage_id + NULL)
                LOAD_FAST_BORROW         1 (brokerage_id)
                CALL                     1
                JUMP_FORWARD             1 (to L4)
        L3:     LOAD_CONST               1 (None)
        L4:     STORE_FAST               4 (bid)

 664            LOAD_GLOBAL              5 (_clamp_limit + NULL)
                LOAD_FAST_BORROW         2 (limit)
                CALL                     1
                STORE_FAST               5 (capped)

 665            NOP

 666    L5:     LOAD_SMALL_INT           0
                LOAD_CONST               2 (('operator_action_history',))
                IMPORT_NAME              3 (app.services.operator.audit_service)
                IMPORT_FROM              4 (operator_action_history)
                STORE_FAST               6 (operator_action_history)
                POP_TOP

 667            LOAD_FAST_BORROW         6 (operator_action_history)
                PUSH_NULL
                LOAD_FAST_BORROW         5 (capped)
                LOAD_CONST               3 (('limit',))
                CALL_KW                  1
                STORE_FAST               7 (env)

 679    L6:     LOAD_GLOBAL             21 (list + NULL)
                LOAD_FAST                7 (env)
                LOAD_ATTR               23 (get + NULL|self)
                LOAD_CONST               7 ('rows')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
        L7:     CALL                     1
                STORE_FAST               9 (rows)

 680            BUILD_LIST               0
                STORE_FAST              10 (filtered)

 681            LOAD_FAST                9 (rows)
                GET_ITER
        L8:     FOR_ITER               156 (to L14)
                STORE_FAST              11 (r)

 682            LOAD_GLOBAL             25 (isinstance + NULL)
                LOAD_FAST               11 (r)
                LOAD_GLOBAL             26 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN

 683            JUMP_BACKWARD           27 (to L8)

 684    L9:     LOAD_FAST               11 (r)
                LOAD_ATTR               23 (get + NULL|self)
                LOAD_CONST              12 ('action')
                CALL                     1
                LOAD_CONST              13 ('review_learning_recommendation')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN

 685            JUMP_BACKWARD           51 (to L8)

 686   L10:     LOAD_FAST               11 (r)
                LOAD_ATTR               23 (get + NULL|self)
                LOAD_CONST              14 ('target_type')
                CALL                     1
                LOAD_CONST              15 ('learning_recommendation')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE        3 (to L11)
                NOT_TAKEN

 687            JUMP_BACKWARD           75 (to L8)

 688   L11:     LOAD_FAST                3 (rid)
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L12)
                NOT_TAKEN
                LOAD_FAST               11 (r)
                LOAD_ATTR               23 (get + NULL|self)
                LOAD_CONST              16 ('target_id')
                CALL                     1
                LOAD_FAST                3 (rid)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE        3 (to L12)
                NOT_TAKEN

 689            JUMP_BACKWARD          107 (to L8)

 690   L12:     LOAD_FAST                4 (bid)
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L13)
                NOT_TAKEN
                LOAD_FAST               11 (r)
                LOAD_ATTR               23 (get + NULL|self)
                LOAD_CONST              17 ('brokerage_id')
                CALL                     1
                LOAD_FAST                4 (bid)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE        3 (to L13)
                NOT_TAKEN

 691            JUMP_BACKWARD          139 (to L8)

 692   L13:     LOAD_FAST               10 (filtered)
                LOAD_ATTR               29 (append + NULL|self)
                LOAD_FAST               11 (r)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          158 (to L8)

 681   L14:     END_FOR
                POP_ITER

 694            LOAD_CONST               5 ('status')
                LOAD_FAST                7 (env)
                LOAD_ATTR               23 (get + NULL|self)
                LOAD_CONST               5 ('status')
                CALL                     1
                LOAD_CONST              18 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L15)
                NOT_TAKEN
                LOAD_CONST              18 ('ok')
                JUMP_FORWARD            26 (to L16)
       L15:     LOAD_FAST                7 (env)
                LOAD_ATTR               23 (get + NULL|self)
                LOAD_CONST               5 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L16)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               6 ('skipped')

 695   L16:     LOAD_CONST               7 ('rows')
                LOAD_FAST               10 (filtered)

 696            LOAD_CONST               8 ('count')
                LOAD_GLOBAL             31 (len + NULL)
                LOAD_FAST               10 (filtered)
                CALL                     1

 697            LOAD_CONST               9 ('warnings')
                LOAD_GLOBAL             21 (list + NULL)
                LOAD_FAST                7 (env)
                LOAD_ATTR               23 (get + NULL|self)
                LOAD_CONST               9 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L17)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
       L17:     CALL                     1

 698            LOAD_CONST              11 ('error_code')
                LOAD_FAST                7 (env)
                LOAD_ATTR               23 (get + NULL|self)
                LOAD_CONST              11 ('error_code')
                CALL                     1

 693            BUILD_MAP                5
                RETURN_VALUE

  --   L18:     PUSH_EXC_INFO

 668            LOAD_GLOBAL             10 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      111 (to L23)
                NOT_TAKEN
                STORE_FAST               8 (e)

 669   L19:     LOAD_GLOBAL             12 (logger)
                LOAD_ATTR               15 (warning + NULL|self)

 670            LOAD_CONST               4 ('recommendation_review_history error type=')
                LOAD_GLOBAL             17 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               18 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 669            CALL                     1
                POP_TOP

 673            LOAD_CONST               5 ('status')
                LOAD_CONST               6 ('skipped')

 674            LOAD_CONST               7 ('rows')
                BUILD_LIST               0

 675            LOAD_CONST               8 ('count')
                LOAD_SMALL_INT           0

 676            LOAD_CONST               9 ('warnings')
                LOAD_CONST              10 ('unexpected:')
                LOAD_GLOBAL             17 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               18 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 677            LOAD_CONST              11 ('error_code')
                LOAD_CONST              10 ('unexpected:')
                LOAD_GLOBAL             17 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               18 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 672            BUILD_MAP                5
       L20:     SWAP                     2
       L21:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RETURN_VALUE

  --   L22:     LOAD_CONST               1 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RERAISE                  1

 668   L23:     RERAISE                  0

  --   L24:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L5 to L6 -> L18 [0]
  L18 to L19 -> L24 [1] lasti
  L19 to L20 -> L22 [1] lasti
  L20 to L21 -> L24 [1] lasti
  L22 to L24 -> L24 [1] lasti
```
